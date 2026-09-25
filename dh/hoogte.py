"""Hoe steil is een perceel? Uit het officiële hoogtemodel van Spanje.

Waarom dit er is: Jan rekent € 15.000 grondwerk op een licht hellend perceel en € 50.000 op een
steil perceel (25-09-2026). Om dat te kunnen toepassen moet per perceel de helling vaststaan.

Bron: IGN, WCS "Modelos Digitales del Terreno", laag `Elevacion25830_5` — een hoogteraster van
5 meter uit PNOA-LiDAR, dekkend voor heel Spanje. Het capabilities-document zegt zelf
`Fees: "No se aplican condiciones"` en `AccessConstraints: "CC BY 4.0 scne.es"`; geen sleutel, geen
aanmelding, geen kosten. Onderzocht en getoetst in onderzoek/N08-helling-percelen.md (25-09-2026).

Met `format=application/asc` komt het raster als platte tekst terug. Daardoor is er geen rasterio,
GDAL of pyproj nodig en hoeft er niets geïnstalleerd te worden. De omzetting naar UTM staat hieronder
zelf uitgeschreven.

Valstrik uit het onderzoek: vraag je een vak dat niet op de celranden valt, dan herschaalt de server
en schrijft hij `dx`/`dy` in plaats van `cellsize`. Daarom wordt het vak eerst op het rooster gelegd.
"""
from __future__ import annotations

import math
import re
import threading
import time

import httpx

from . import config

WCS = "https://servicios.idee.es/wcs-inspire/mdt"
LAAG = "Elevacion25830_5"
CELSIZE = 5.0
OORSPRONG_X, OORSPRONG_Y = -19450.0, 4865680.0     # raster-oorsprong, DescribeCoverage 25-09-2026
BRON = ("IGN, WCS Modelos Digitales del Terreno, laag Elevacion25830_5 (MDT05 uit PNOA-LiDAR), "
        "CC BY 4.0 scne.es")
VERZOEKEN_PER_S = 1.4                               # beleefd; het onderzoek deed 0,7 s per vak

# Drempels op de mediane celhelling (onderzoek N08 §5). De 15 % is op vijf onafhankelijke manieren
# onderbouwd; de 8 % rust op één commerciële kostenbron en is dus de zwakkere van de twee.
GRENS_VLAK = 0.08
GRENS_STEIL = 0.15

_lock = threading.Lock()
_next = [0.0]


def _wacht() -> None:
    with _lock:
        nu = time.monotonic()
        if nu < _next[0]:
            time.sleep(_next[0] - nu)
        _next[0] = max(nu, _next[0]) + 1.0 / VERZOEKEN_PER_S


# ---------------------------------------------------------------- projectie

_A = 6378137.0                       # GRS80, gelijk aan WGS84 voor onze nauwkeurigheid
_F = 1 / 298.257222101
_E2 = _F * (2 - _F)
_K0 = 0.9996
_LON0 = math.radians(-3.0)           # UTM-zone 30N
_FE, _FN = 500000.0, 0.0


def naar_utm30(lon: float, lat: float) -> tuple[float, float]:
    """WGS84/ETRS89 lengte en breedte naar EPSG:25830 (UTM 30N), in meters.

    De gewone reeksontwikkeling voor de transversale mercatorprojectie. Uitgeschreven omdat pyproj
    hier niet geïnstalleerd is en niet geïnstalleerd mag worden."""
    lat_r, lon_r = math.radians(lat), math.radians(lon)
    ep2 = _E2 / (1 - _E2)
    n = _A / math.sqrt(1 - _E2 * math.sin(lat_r) ** 2)
    t = math.tan(lat_r) ** 2
    c = ep2 * math.cos(lat_r) ** 2
    a = math.cos(lat_r) * (lon_r - _LON0)
    m = _A * ((1 - _E2 / 4 - 3 * _E2 ** 2 / 64 - 5 * _E2 ** 3 / 256) * lat_r
              - (3 * _E2 / 8 + 3 * _E2 ** 2 / 32 + 45 * _E2 ** 3 / 1024) * math.sin(2 * lat_r)
              + (15 * _E2 ** 2 / 256 + 45 * _E2 ** 3 / 1024) * math.sin(4 * lat_r)
              - (35 * _E2 ** 3 / 3072) * math.sin(6 * lat_r))
    x = _FE + _K0 * n * (a + (1 - t + c) * a ** 3 / 6
                         + (5 - 18 * t + t ** 2 + 72 * c - 58 * ep2) * a ** 5 / 120)
    y = _FN + _K0 * (m + n * math.tan(lat_r) * (a ** 2 / 2 + (5 - t + 9 * c + 4 * c ** 2) * a ** 4 / 24
                     + (61 - 58 * t + t ** 2 + 600 * c - 330 * ep2) * a ** 6 / 720))
    return x, y


def ringen(geojson) -> list[list[tuple[float, float]]]:
    """Alle buitenringen uit een GeoJSON-geometrie, omgezet naar UTM 30N."""
    if not geojson:
        return []
    g = geojson.get("geometry", geojson) if isinstance(geojson, dict) else None
    if not isinstance(g, dict):
        return []
    soort, co = g.get("type"), g.get("coordinates")
    stukken = []
    if soort == "Polygon":
        stukken = [co[0]] if co else []
    elif soort == "MultiPolygon":
        stukken = [pol[0] for pol in (co or []) if pol]
    elif soort in ("FeatureCollection", "GeometryCollection"):
        for f in (g.get("features") or g.get("geometries") or []):
            stukken += [r for r in _ruwe_ringen(f)]
    return [[naar_utm30(float(p[0]), float(p[1])) for p in ring] for ring in stukken if ring]


def _ruwe_ringen(f) -> list:
    g = f.get("geometry", f) if isinstance(f, dict) else None
    if not isinstance(g, dict):
        return []
    if g.get("type") == "Polygon":
        return [g["coordinates"][0]] if g.get("coordinates") else []
    if g.get("type") == "MultiPolygon":
        return [pol[0] for pol in (g.get("coordinates") or []) if pol]
    return []


def in_ring(x: float, y: float, ring: list[tuple[float, float]]) -> bool:
    """Ligt het punt binnen de ring? Gewone straaltoets."""
    binnen = False
    j = len(ring) - 1
    for i in range(len(ring)):
        xi, yi = ring[i]
        xj, yj = ring[j]
        if (yi > y) != (yj > y) and x < (xj - xi) * (y - yi) / ((yj - yi) or 1e-12) + xi:
            binnen = not binnen
        j = i
    return binnen


# ---------------------------------------------------------------- raster ophalen

def _snap_laag(v: float, oorsprong: float) -> float:
    return oorsprong + math.floor((v - oorsprong) / CELSIZE) * CELSIZE


def _snap_hoog(v: float, oorsprong: float) -> float:
    return oorsprong + math.ceil((v - oorsprong) / CELSIZE) * CELSIZE


def raster(x0: float, y0: float, x1: float, y1: float, client=None) -> dict | None:
    """Haalt het hoogteraster over een vak op. Het vak wordt eerst op het rooster gelegd."""
    ax, ay = _snap_laag(x0, OORSPRONG_X), _snap_laag(y0, OORSPRONG_Y)
    bx, by = _snap_hoog(x1, OORSPRONG_X), _snap_hoog(y1, OORSPRONG_Y)
    par = {"service": "WCS", "version": "2.0.1", "request": "GetCoverage", "coverageId": LAAG,
           "subset": [f"x({ax},{bx})", f"y({ay},{by})"], "format": "application/asc"}
    _wacht()
    eigen = client is None
    cl = client or httpx.Client(timeout=config.HTTP_TIMEOUT)
    try:
        r = cl.get(WCS, params=par, headers={"User-Agent": config.USER_AGENT})
        if r.status_code != 200:
            return None
        return lees_asc(r.text)
    except Exception:  # noqa: BLE001
        return None
    finally:
        if eigen:
            cl.close()


KOP = re.compile(r"^\s*(ncols|nrows|xllcorner|yllcorner|cellsize|dx|dy|NODATA_value)\s+(-?[\d.eE+]+)\s*$")


def lees_asc(tekst: str) -> dict | None:
    """Leest het ASCII-grid uit het multipart-antwoord. Geeft kop en rijen met hoogtes."""
    kop: dict[str, float] = {}
    rijen: list[list[float]] = []
    for regel in tekst.splitlines():
        m = KOP.match(regel)
        if m:
            kop[m.group(1)] = float(m.group(2))
            continue
        if not kop.get("ncols"):
            continue
        deel = regel.split()
        if len(deel) >= 2 and all(_getal(d) for d in deel[:2]):
            try:
                rij = [float(d) for d in deel]
            except ValueError:
                continue
            if len(rij) == int(kop["ncols"]):
                rijen.append(rij)
    if not rijen or "xllcorner" not in kop:
        return None
    cs = kop.get("cellsize") or kop.get("dx") or CELSIZE
    return {"ncols": int(kop["ncols"]), "nrows": len(rijen), "x0": kop["xllcorner"],
            "y0": kop["yllcorner"], "cell": cs, "nodata": kop.get("NODATA_value", -9999.0),
            "z": rijen}


def _getal(s: str) -> bool:
    try:
        float(s)
        return True
    except ValueError:
        return False


# ---------------------------------------------------------------- helling

def hellingen(r: dict, ring: list[tuple[float, float]]) -> list[float]:
    """Helling per cel binnen het perceel, met de methode van Horn over 3 × 3 cellen."""
    z, n, m, cs = r["z"], r["nrows"], r["ncols"], r["cell"]
    uit = []
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            # rij 0 is de bovenste rij van het vak; y loopt van boven naar beneden
            x = r["x0"] + (j + 0.5) * cs
            y = r["y0"] + (n - i - 0.5) * cs
            if ring and not in_ring(x, y, ring):
                continue
            buurt = [z[i + di][j + dj] for di in (-1, 0, 1) for dj in (-1, 0, 1)]
            if any(abs(v - r["nodata"]) < 0.001 for v in buurt):
                continue
            dzdx = ((z[i - 1][j + 1] + 2 * z[i][j + 1] + z[i + 1][j + 1])
                    - (z[i - 1][j - 1] + 2 * z[i][j - 1] + z[i + 1][j - 1])) / (8 * cs)
            dzdy = ((z[i + 1][j - 1] + 2 * z[i + 1][j] + z[i + 1][j + 1])
                    - (z[i - 1][j - 1] + 2 * z[i - 1][j] + z[i - 1][j + 1])) / (8 * cs)
            uit.append(math.sqrt(dzdx * dzdx + dzdy * dzdy))
    return uit


def oordeel(helling: float | None) -> str | None:
    if helling is None:
        return None
    if helling < GRENS_VLAK:
        return "vlak"
    return "licht" if helling < GRENS_STEIL else "steil"


def meet(geojson, client=None) -> dict | None:
    """Van een perceelgrens naar helling en oordeel. Geeft None als er niets te meten valt."""
    rs = ringen(geojson)
    if not rs:
        return None
    ring = max(rs, key=len)
    xs = [p[0] for p in ring]
    ys = [p[1] for p in ring]
    r = raster(min(xs) - 10, min(ys) - 10, max(xs) + 10, max(ys) + 10, client)
    if not r:
        return None
    h = hellingen(r, ring)
    if not h:
        h = hellingen(r, [])          # klein perceel: dan het hele vak nemen
    if not h:
        return None
    h.sort()
    mid = h[len(h) // 2] if len(h) % 2 else (h[len(h) // 2 - 1] + h[len(h) // 2]) / 2
    p90 = h[min(int(len(h) * 0.9), len(h) - 1)]
    binnen = [z for rij in r["z"] for z in rij if abs(z - r["nodata"]) > 0.001]
    return {"helling": round(mid, 4), "helling_p90": round(p90, 4), "cellen": len(h),
            "hoogte_min": round(min(binnen), 1) if binnen else None,
            "hoogte_max": round(max(binnen), 1) if binnen else None,
            "oordeel": oordeel(mid), "bron": BRON}

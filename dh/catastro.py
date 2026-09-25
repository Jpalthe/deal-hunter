"""Kadaster: van een punt naar een perceel, en van een perceel naar de feiten.

Drie diensten van de Sede Electrónica del Catastro, alle drie openbaar en gratis:

  Consulta_RCCOOR_Distancia   punt → kadastrale referenties in de buurt, met afstand
  Consulta_DNPRC              referentie → adres, gebruik, bebouwd oppervlak, bouwjaar
  INSPIRE wfsCP GetParcel     referentie → officiële perceeloppervlakte en de perceelgrens

Wat hier binnenkomt is openbaar en niet persoonlijk: het kadaster geeft via deze diensten geen
eigenaren. Namen van eigenaren vragen wij niet op en slaan wij niet op.

Een punt uit een advertentie is geen perceelidentificatie. De pin staat vaak tientallen meters
naast het echte perceel. Daarom slaan wij de afstand op en markeren wij alles boven de 25 meter
als onzeker; bevestigen gebeurt met een nota simple.
"""
from __future__ import annotations

import json
import re
import threading
import time
from collections import OrderedDict

import httpx
from defusedxml import ElementTree as ET

from . import config

NS = {"c": "http://www.catastro.meh.es/"}
RCCOOR = "https://ovc.catastro.meh.es/ovcservweb/OVCSWLocalizacionRC/OVCCoordenadas.asmx/Consulta_RCCOOR_Distancia"
DNPRC = "https://ovc.catastro.meh.es/ovcservweb/OVCSWLocalizacionRC/OVCCallejero.asmx/Consulta_DNPRC"
WFS_CP = "https://ovc.catastro.meh.es/INSPIRE/wfsCP.aspx"
SEDE = "https://www1.sedecatastro.gob.es/Cartografia/mapa.aspx?refcat={rc}"
RC_RE = re.compile(r"^[0-9A-Z]{14}$")
ZEKER_M = 25.0          # boven deze afstand is de koppeling punt → perceel onzeker

_lock = threading.Lock()
_next = [0.0]           # vroegste tijdstip voor het volgende verzoek aan Catastro
_cache: "OrderedDict[str, dict]" = OrderedDict()
CACHE_MAX = 800


def _throttle() -> None:
    """Maximaal één verzoek per seconde, en wachten buiten het slot."""
    with _lock:
        now = time.time()
        slot = max(now, _next[0])
        _next[0] = slot + 1.05
    wait = slot - time.time()
    if wait > 0:
        time.sleep(wait)


def _get(url: str, params: dict) -> bytes:
    _throttle()
    r = httpx.get(url, params=params, timeout=25, headers={"User-Agent": config.USER_AGENT})
    r.raise_for_status()
    return r.content


def _cached(key: str, fn):
    with _lock:
        if key in _cache:
            _cache.move_to_end(key)
            return _cache[key]
    val = fn()
    with _lock:
        _cache[key] = val
        while len(_cache) > CACHE_MAX:
            _cache.popitem(last=False)
    return val


def _txt(el, path: str) -> str | None:
    if el is None:
        return None
    v = el.findtext(path, default=None, namespaces=NS)
    return v.strip() if isinstance(v, str) and v.strip() else None


# ------------------------------------------------------------------ punt → perceel

def parcels_at(lat: float, lon: float) -> dict:
    """Kadastrale referenties bij een punt, dichtstbij eerst."""
    if not config.valid_coord(lat, lon):
        return {"parcels": [], "error": "punt buiten het werkgebied"}

    def fetch():
        root = ET.fromstring(_get(RCCOOR, {"SRS": "EPSG:4326", "Coordenada_X": f"{lon:.6f}", "Coordenada_Y": f"{lat:.6f}"}))
        out = []
        for pd in root.findall(".//c:pcd", NS):
            pc1 = _txt(pd, ".//c:pc1") or ""
            pc2 = _txt(pd, ".//c:pc2") or ""
            if not re.fullmatch(r"[0-9A-Z]{7}", pc1) or not re.fullmatch(r"[0-9A-Z]{7}", pc2):
                continue
            dis = _txt(pd, ".//c:dis")
            try:
                dis_m = float(dis) if dis is not None else None
            except ValueError:
                dis_m = None
            out.append({"rc": pc1 + pc2, "address": _txt(pd, ".//c:ldt"), "distance_m": dis_m,
                        "sede_url": SEDE.format(rc=pc1 + pc2)})
        out.sort(key=lambda x: (x["distance_m"] is None, x["distance_m"] or 0))
        err = root.findtext(".//c:des", default=None, namespaces=NS)
        return {"parcels": out[:5], "error": None if out else err,
                "source": "Sede Electrónica del Catastro, Consulta_RCCOOR_Distancia"}

    return _cached(f"rccoor:{round(lat, 5)}:{round(lon, 5)}", fetch)


# ------------------------------------------------------------------ perceel → feiten

def detail(rc: str) -> dict:
    """Adres, gebruik, bebouwd oppervlak en bouwjaar bij een kadastrale referentie."""
    rc = (rc or "").strip().upper()
    if not RC_RE.match(rc):
        return {"error": "ongeldige kadastrale referentie"}

    def fetch():
        root = ET.fromstring(_get(DNPRC, {"Provincia": "", "Municipio": "", "RC": rc}))
        err = _txt(root, ".//c:err/c:des") or _txt(root, ".//c:des")
        bi = root.find(".//c:bico/c:bi", NS) or root.find(".//c:bi", NS)
        if bi is None:
            return {"rc": rc, "error": err or "geen gegevens", "sede_url": SEDE.format(rc=rc)}
        debi = bi.find(".//c:debi", NS)
        sfc = _txt(debi, "c:sfc") if debi is not None else None
        ant = _txt(debi, "c:ant") if debi is not None else None
        parts = []
        for cons in root.findall(".//c:lcons/c:cons", NS):
            parts.append({"use": _txt(cons, "c:lcd"),
                          "floor": _txt(cons, ".//c:pt"),
                          "door": _txt(cons, ".//c:pu"),
                          "m2": _num(_txt(cons, "c:dfcons/c:stl"))})
        return {
            "rc": rc,
            "address": _txt(bi, "c:ldt"),
            "municipality": _txt(bi, ".//c:nm"),
            "province": _txt(bi, ".//c:np"),
            "postcode": _txt(bi, ".//c:dp"),
            "use": _txt(debi, "c:luso") if debi is not None else None,
            "built_m2": _num(sfc),
            "year": int(ant) if ant and ant.isdigit() else None,
            "parts": parts,
            "unbuilt": _num(sfc) == 0,
            "error": None,
            "sede_url": SEDE.format(rc=rc),
            "source": "Sede Electrónica del Catastro, Consulta_DNPRC",
        }

    return _cached(f"dnprc:{rc}", fetch)


def _num(v) -> float | None:
    if v is None:
        return None
    try:
        return float(str(v).replace(".", "").replace(",", ".")) if "," in str(v) else float(v)
    except ValueError:
        return None


# ------------------------------------------------------------------ perceel → grens

def geometry(rc: str) -> dict:
    """Officiële perceeloppervlakte en de perceelgrens als GeoJSON (WGS84)."""
    rc = (rc or "").strip().upper()
    if not RC_RE.match(rc):
        return {"error": "ongeldige kadastrale referentie"}

    def fetch():
        raw = _get(WFS_CP, {"service": "wfs", "version": "2.0.0", "request": "getfeature",
                            "STOREDQUERIE_ID": "GetParcel", "refcat": rc, "srsname": "EPSG::4326"})
        txt = raw.decode("iso-8859-1", errors="replace")
        m = re.search(r"<cp:areaValue[^>]*>([\d.]+)<", txt)
        area = float(m.group(1)) if m else None
        rings: list[list[list[float]]] = []
        for pl in re.findall(r"<gml:posList[^>]*>([^<]+)</gml:posList>", txt):
            nums = [float(x) for x in pl.split()]
            # de dienst levert breedte, lengte; GeoJSON wil lengte, breedte
            ring = [[nums[i + 1], nums[i]] for i in range(0, len(nums) - 1, 2)]
            if len(ring) >= 4:
                rings.append(ring)
        if not rings:
            return {"rc": rc, "area_m2": area, "geojson": None, "error": "geen geometrie in het antwoord"}
        geo = {"type": "Polygon", "coordinates": rings} if len(rings) == 1 else \
              {"type": "MultiPolygon", "coordinates": [[r] for r in rings]}
        lats = [p[1] for r in rings for p in r]
        lons = [p[0] for r in rings for p in r]
        return {"rc": rc, "area_m2": area, "geojson": geo,
                "center": [sum(lons) / len(lons), sum(lats) / len(lats)],
                "bbox": [min(lons), min(lats), max(lons), max(lats)],
                "error": None, "source": "Catastro INSPIRE, wfsCP GetParcel"}

    return _cached(f"cp:{rc}", fetch)


# ------------------------------------------------------------------ alles in één

def enrich(lat: float, lon: float, rc: str | None = None) -> dict:
    """Volledige perceelketen vanaf een punt of een bekende referentie.

    Geeft altijd terug wat wél vastgesteld is en zegt expliciet wat onzeker blijft."""
    out: dict = {"input": {"lat": lat, "lon": lon, "rc": rc}, "warnings": []}
    if not rc:
        near = parcels_at(lat, lon)
        out["nearby"] = near.get("parcels", [])
        if not near.get("parcels"):
            out["error"] = near.get("error") or "geen perceel gevonden op dit punt"
            return out
        first = near["parcels"][0]
        rc = first["rc"]
        out["distance_m"] = first.get("distance_m")
        if first.get("distance_m") and first["distance_m"] > ZEKER_M:
            out["warnings"].append(
                f"De pin ligt {first['distance_m']:.0f} m van dit perceel. Welk perceel werkelijk te koop staat is "
                "hiermee niet vastgesteld; bevestigen met een nota simple.")
        if len(near["parcels"]) > 1:
            out["warnings"].append(f"{len(near['parcels'])} percelen binnen bereik van de pin: {', '.join(p['rc'] for p in near['parcels'][:3])}")
    out["rc"] = rc
    try:
        out["detail"] = detail(rc)
    except Exception as e:  # noqa: BLE001
        out["detail"] = {"error": f"niet bereikbaar: {str(e)[:120]}"}
    try:
        out["geometry"] = geometry(rc)
    except Exception as e:  # noqa: BLE001
        out["geometry"] = {"error": f"niet bereikbaar: {str(e)[:120]}"}
    d, g = out.get("detail") or {}, out.get("geometry") or {}
    if g.get("area_m2"):
        out["plot_m2"] = g["area_m2"]
    if d.get("built_m2") is not None:
        out["built_m2_catastro"] = d["built_m2"]
    if d.get("unbuilt"):
        out["warnings"].append("Het kadaster kent geen bebouwing op dit perceel.")
    return out


def compare(enriched: dict, ad_plot_m2: float | None, ad_built_m2: float | None) -> list[str]:
    """Verschillen tussen de advertentie en het kadaster, in gewone taal."""
    out: list[str] = []
    k_plot = enriched.get("plot_m2")
    k_built = enriched.get("built_m2_catastro")
    if ad_plot_m2 and k_plot:
        d = (ad_plot_m2 - k_plot) / k_plot
        if d > 0.05:
            out.append(f"Perceel: de advertentie noemt {ad_plot_m2:.0f} m², het kadastrale perceel onder de pin is "
                       f"{k_plot:.0f} m² ({d * 100:+.0f} %). Twee verklaringen: het object ligt op meer dan één perceel, "
                       "of de advertentie overdrijft. De nota simple geeft uitsluitsel.")
        elif d < -0.05:
            out.append(f"Perceel: de advertentie noemt {ad_plot_m2:.0f} m², het kadastrale perceel onder de pin is "
                       f"{k_plot:.0f} m² ({d * 100:+.0f} %). Er wordt dus minder aangeboden dan er op het perceel ligt, "
                       "of de pin wijst het verkeerde perceel aan. Bevestigen met de nota simple.")
    if ad_built_m2 and k_built is not None:
        if k_built == 0:
            out.append(f"Bebouwing: de advertentie noemt {ad_built_m2:.0f} m² gebouwd, het kadaster kent hier niets. "
                       "Dat wijst op een bouwwerk zonder inschrijving; controleer de vergunninghistorie.")
        else:
            d = (ad_built_m2 - k_built) / k_built
            if abs(d) > 0.10:
                out.append(f"Bebouwing: de advertentie noemt {ad_built_m2:.0f} m², het kadaster {k_built:.0f} m² "
                           f"({d * 100:+.0f} %). Het verschil is vaak terras of kelder, maar kan ook onvergund werk zijn.")
    return out

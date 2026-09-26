"""Overstroming en kustwet per perceel, uit de kaarten van het ministerie.

Bron: MITECO GeoServer, https://gis.miteco.gob.es/geoserver/. De GetCapabilities van beide
werkruimten verklaart zelf `Fees: CC BY 4.0, Nombrar a la fuente: Ministerio para la Transición
Ecológica y el Reto Demográfico` en `AccessConstraints: Sin limitaciones al acceso público`
(gelezen 26-09-2026). Geen sleutel, geen kosten. Onderzoek: onderzoek/N09-risico-water-en-kust.md.

Waarom hier in bulk wordt gewerkt en niet per perceel: zeven verzoeken halen de zones van heel Jávea
op, waarna 622 percelen lokaal zijn door te rekenen. Per perceel bevragen zou 4.300 verzoeken kosten.

Twee valstrikken uit het onderzoek, hier vastgelegd zodat ze niet opnieuw toeslaan:

1. **Het coördinatenstelsel verschilt per laag, niet per dienst.** De overstromingslagen staan in
   EPSG:4258 (breedte eerst), de kustlagen in EPSG:25830 (meters). Met de verkeerde volgorde krijg
   je HTTP 200 met een lege lijst en géén waarschuwing. Daarom controleert `_normaliseer` de
   getallen zelf en draait ze om als dat nodig is.
2. **Neem nooit de 100 meter uit de kustwet aan.** De strook tussen de DPMT-lijn en de SP-lijn is ter
   plaatse gemeten 60,9 m en 20,0 m. Meet hem; reken hem niet.
"""
from __future__ import annotations

import json
import math
import threading
import time

import httpx

from . import config

WFS = "https://gis.miteco.gob.es/geoserver/{ruimte}/ows"
BRON = ("MITECO (Ministerio para la Transición Ecológica y el Reto Demográfico), "
        "GeoServer agua en costas, CC BY 4.0")
CACHE = config.DATA / "water-kust-zones.json"
# Jávea met ruime marge, in graden
BBOX = (0.05, 38.66, 0.32, 38.86)

LAGEN = [
    ("zfp", "agua", "ZI_Laminas_ZFP", "vlak"),
    ("t100", "agua", "Zi_laminas_q100", "vlak"),
    ("t500", "agua", "Zi_laminas_q500", "vlak"),
    ("dph", "agua", "DPH_Estimado", "vlak"),
    ("marien_t100", "costas", "zim_laminas_q100", "vlak"),
    ("dpmt", "costas", "dominio_publico_maritimo_terrestre", "lijn"),
]

_lock = threading.Lock()
_next = [0.0]
PAUZE_S = 2.0


def _wacht() -> None:
    with _lock:
        nu = time.monotonic()
        if nu < _next[0]:
            time.sleep(_next[0] - nu)
        _next[0] = max(nu, _next[0]) + PAUZE_S


def _normaliseer(co):
    """Zet een coördinatenpaar om naar (lon, lat), wat de volgorde in de bron ook was.

    Jávea ligt rond lon 0,2 en lat 38,8. Een paar waarvan het eerste getal boven de 38 ligt, staat
    dus omgekeerd. Zo hoeven wij niet per laag te onthouden welke volgorde geldt."""
    x, y = float(co[0]), float(co[1])
    if 38.0 < x < 39.5 and -1.0 < y < 1.5:
        return (y, x)
    return (x, y)


def _ringen_uit(geom) -> list[list[tuple[float, float]]]:
    if not isinstance(geom, dict):
        return []
    t, co = geom.get("type"), geom.get("coordinates")
    if t == "Polygon":
        return [[_normaliseer(p) for p in ring] for ring in (co or [])[:1]]
    if t == "MultiPolygon":
        return [[_normaliseer(p) for p in pol[0]] for pol in (co or []) if pol]
    if t == "LineString":
        return [[_normaliseer(p) for p in (co or [])]]
    if t == "MultiLineString":
        return [[_normaliseer(p) for p in lijn] for lijn in (co or []) if lijn]
    return []


def haal_zones(client=None, opnieuw: bool = False) -> dict:
    """Haalt de zones van heel Jávea op en bewaart ze. Zeven verzoeken, daarna lokaal rekenen."""
    if CACHE.exists() and not opnieuw:
        try:
            return json.loads(CACHE.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            pass
    eigen = client is None
    cl = client or httpx.Client(timeout=120)
    uit: dict = {"bron": BRON, "bbox": BBOX, "lagen": {}}
    try:
        for sleutel, ruimte, laag, soort in LAGEN:
            par = {"service": "WFS", "version": "2.0.0", "request": "GetFeature",
                   "typeNames": f"{ruimte}:{laag}", "outputFormat": "application/json",
                   "srsName": "EPSG:4326", "count": "3000",
                   "bbox": f"{BBOX[1]},{BBOX[0]},{BBOX[3]},{BBOX[2]},urn:ogc:def:crs:EPSG::4326"}
            _wacht()
            try:
                r = cl.get(WFS.format(ruimte=ruimte), params=par,
                           headers={"User-Agent": config.USER_AGENT})
                d = r.json() if r.status_code == 200 else {}
            except Exception:  # noqa: BLE001 — één laag die hapert mag de rest niet tegenhouden
                d = {}
            vormen = []
            for f in (d.get("features") or []):
                for ring in _ringen_uit(f.get("geometry")):
                    if len(ring) >= 2:
                        vormen.append({"ring": ring, "eig": f.get("properties") or {}})
            uit["lagen"][sleutel] = {"soort": soort, "laag": f"{ruimte}:{laag}", "vormen": vormen}
    finally:
        if eigen:
            cl.close()
    CACHE.parent.mkdir(parents=True, exist_ok=True)
    CACHE.write_text(json.dumps(uit, ensure_ascii=False), encoding="utf-8")
    return uit


# ---------------------------------------------------------------- meetkunde

def in_ring(x: float, y: float, ring) -> bool:
    binnen = False
    j = len(ring) - 1
    for i in range(len(ring)):
        xi, yi = ring[i]
        xj, yj = ring[j]
        if (yi > y) != (yj > y) and x < (xj - xi) * (y - yi) / ((yj - yi) or 1e-15) + xi:
            binnen = not binnen
        j = i
    return binnen


def _m_per_graad(lat: float) -> tuple[float, float]:
    return 111320.0 * math.cos(math.radians(lat)), 110540.0


def afstand_tot_ring_m(punt, ring, lat_ref: float) -> float:
    """Kortste afstand van een punt tot een lijn of rand, in meters."""
    mx, my = _m_per_graad(lat_ref)
    px, py = punt[0] * mx, punt[1] * my
    best = float("inf")
    for i in range(len(ring) - 1):
        ax, ay = ring[i][0] * mx, ring[i][1] * my
        bx, by = ring[i + 1][0] * mx, ring[i + 1][1] * my
        dx, dy = bx - ax, by - ay
        lang = dx * dx + dy * dy
        t = 0.0 if lang == 0 else max(0.0, min(1.0, ((px - ax) * dx + (py - ay) * dy) / lang))
        qx, qy = ax + t * dx, ay + t * dy
        best = min(best, math.hypot(px - qx, py - qy))
    return best


def raakt(perceel: list, ring: list) -> bool:
    """Overlappen het perceel en de zone? Een hoekpunt van de een binnen de ander is genoeg."""
    if any(in_ring(x, y, ring) for x, y in perceel):
        return True
    return any(in_ring(x, y, perceel) for x, y in ring)


def perceel_ringen(geojson) -> list:
    """De buitenring van een perceel uit parcels.geojson, als (lon, lat)."""
    g = geojson.get("geometry", geojson) if isinstance(geojson, dict) else None
    return _ringen_uit(g) if g else []


# ---------------------------------------------------------------- oordeel

def meet(geojson, zones: dict) -> dict | None:
    """Wat er voor dit perceel geldt. Alles lokaal; de zones zijn al opgehaald."""
    rs = perceel_ringen(geojson)
    if not rs:
        return None
    ring = max(rs, key=len)
    lat_ref = sum(p[1] for p in ring) / len(ring)
    uit: dict = {"bron": zones.get("bron", BRON)}

    for sleutel in ("zfp", "t100", "t500", "marien_t100"):
        laag = (zones.get("lagen") or {}).get(sleutel) or {}
        treffer, dichtst = None, float("inf")
        for v in laag.get("vormen") or []:
            if raakt(ring, v["ring"]):
                treffer = v
                break
            d = min(afstand_tot_ring_m(p, v["ring"], lat_ref) for p in ring[::3] or ring)
            dichtst = min(dichtst, d)
        uit[sleutel] = bool(treffer)
        if treffer:
            e = treffer["eig"]
            uit[f"{sleutel}_zone"] = e.get("id_zona") or e.get("zona")
            uit[f"{sleutel}_rio"] = e.get("rio") or e.get("zona")
            uit[f"{sleutel}_studie"] = " ".join(str(e.get(k)) for k in ("estudio", "fecha_apro") if e.get(k)) or None
        elif dichtst < float("inf"):
            uit[f"{sleutel}_afstand_m"] = round(dichtst)

    dph = (zones.get("lagen") or {}).get("dph") or {}
    uit["dph_zone"] = None
    for v in dph.get("vormen") or []:
        if raakt(ring, v["ring"]):
            uit["dph_zone"] = (v["eig"].get("tipo_zona") or v["eig"].get("zona"))
            break

    # Kustwet: afstand tot de goedgekeurde grenslijnen, en de strook ter plaatse méten.
    dpmt = (zones.get("lagen") or {}).get("dpmt") or {}
    per_soort: dict[str, float] = {}
    dossier = None
    for v in dpmt.get("vormen") or []:
        d = min(afstand_tot_ring_m(p, v["ring"], lat_ref) for p in ring[::3] or ring)
        if d > 1500:
            continue
        soort = str(v["eig"].get("tipo_linea") or "onbekend")
        if d < per_soort.get(soort, float("inf")):
            per_soort[soort] = d
            if "DPMT" in soort.upper():
                dossier = " ".join(str(v["eig"].get(k)) for k in ("referencia", "sit_admin") if v["eig"].get(k)) or None
    dpmt_m = min((d for s, d in per_soort.items() if "DPMT" in s.upper()), default=None)
    sp_m = min((d for s, d in per_soort.items() if "SP" in s.upper() or "PROTEC" in s.upper()), default=None)
    uit["kust_dpmt_m"] = round(dpmt_m) if dpmt_m is not None else None
    uit["kust_sp_m"] = round(sp_m) if sp_m is not None else None
    uit["kust_dossier"] = dossier
    uit["kust_oordeel"] = _kustoordeel(dpmt_m, sp_m)
    uit["kust_strook_m"] = (round(dpmt_m + sp_m) if (dpmt_m is not None and sp_m is not None
                                                     and uit["kust_oordeel"] == "in_servidumbre") else None)
    uit["uitsluiting"] = _uitsluiting(uit)
    return uit


# De servidumbre de protección is ter plaatse gemeten 20 tot 100 meter breed (onderzoek N09). Verder
# dan dit van de kustgrens kán een perceel er niet in liggen, hoe de lijnen ook lopen.
SERVIDUMBRE_MAX_M = 150
NABIJ_M = 250


def _kustoordeel(dpmt_m, sp_m) -> str:
    """Zie de rekenregel in onderzoek/N09 §5.1. Nooit de 100 m uit de wet aannemen: méét hem.

    De eerste versie hiervan zei "in de servidumbre" over een perceel op 1.012 meter van zee, alleen
    omdat dat net iets dichter bij de DPMT-lijn lag dan bij de SP-lijn. Op die afstand zegt dat
    niets. Daarom eerst een harde afstandsgrens, en pas daarbinnen de vergelijking tussen de twee
    lijnen."""
    if dpmt_m is None:
        return "buiten"
    if dpmt_m < 1:
        return "in_dpmt"
    if dpmt_m > NABIJ_M:
        return "buiten"
    if sp_m is not None and sp_m < 1:
        return "in_servidumbre"
    # Binnen de strook: dichter bij het water dan bij de landwaartse grens van de beschermingszone.
    if sp_m is not None and dpmt_m <= SERVIDUMBRE_MAX_M and dpmt_m < sp_m:
        return "in_servidumbre"
    return "nabij"


def _uitsluiting(m: dict) -> str | None:
    """Jan 26-09-2026: alleen het zwaarste valt af. T100 blijft staan met een waarschuwing.

    Geen extra kostenpost; de zone komt als waarschuwing in het dossier."""
    if m.get("zfp"):
        return "zona de flujo preferente: de doorstroomzone van de rivier, hier wordt niet gebouwd"
    if m.get("kust_oordeel") == "in_dpmt":
        return "dominio público marítimo-terrestre: openbaar zeegebied"
    return None


def waarschuwing(m: dict) -> str | None:
    if not m:
        return None
    if m.get("t100"):
        rio = m.get("t100_rio") or "een waterloop"
        return (f"Ligt in de honderdjaarszone van {rio}. Eisen aan het bouwpeil, geen souterrain, "
                f"en de opstalverzekering wordt duurder of wordt geweigerd.")
    if m.get("kust_oordeel") == "in_servidumbre":
        return ("Ligt in de servidumbre de protección van de kustwet. Bouwen vraagt naast de "
                "gemeentelijke vergunning toestemming van de provincie.")
    if m.get("t500"):
        return "Ligt in de vijfhonderdjaarszone. Lage kans, maar het staat op de kaart."
    return None

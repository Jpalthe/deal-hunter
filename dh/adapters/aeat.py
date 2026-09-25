"""Adapter AEAT-veilinglijst bienes.js (CC BY 4.0; bronvermelding verplicht, zie config.AEAT_ATTRIBUTION).

Het bestand is JavaScript met twee arrays (inmueblesSubasta, mueblesSubasta). Wij lezen alleen de
eerste (onroerend goed). Velden (gezien 14/15-09-2026): id, tipo, subasta (SUB-id), derecho,
porcTitularidad, codProvincia (int), direccion, refCatastro, valoracion, cargas, finSubasta,
descripcion, cru, gpsLat, gpsLong, capital, interes, municipioCod, cp (int, zonder voorloopnul), fotos.
Structuurwijziging → SourceUnavailable (BRON NIET BEREIKBAAR).
"""
from __future__ import annotations

import json
import re

import httpx

from .. import config

# Benaderende begrenzingen (WGS84) — alleen als laatste redmiddel, met label 'gps-schatting'.
BBOX = {
    "javea": (38.715, 38.835, 0.095, 0.245),
    "benitachell": (38.695, 38.745, 0.110, 0.190),
    "moraira": (38.655, 38.745, 0.045, 0.150),
}
PROVINCE_ALICANTE = 3


class SourceUnavailable(Exception):
    pass


def parse(text: str) -> tuple[list[dict], str]:
    m = re.search(r"Version:\s*([0-9]{8}\s+[0-9:]{8})", text)
    version = m.group(1) if m else ""
    i = text.find("[")
    if i < 0:
        raise SourceUnavailable("geen array gevonden in bienes.js")
    try:
        arr, _ = json.JSONDecoder().raw_decode(text[i:])
    except json.JSONDecodeError as e:
        raise SourceUnavailable(f"bienes.js niet te parsen: {e}") from e
    if not isinstance(arr, list) or not arr or "subasta" not in arr[0]:
        raise SourceUnavailable("bienes.js heeft een andere structuur dan verwacht")
    return arr, version


def fetch() -> tuple[list[dict], str]:
    with httpx.Client(timeout=config.HTTP_TIMEOUT, headers={"User-Agent": config.USER_AGENT}) as c:
        r = c.get(config.AEAT_BIENES_URL)
        r.raise_for_status()
    return parse(r.text)


def _f(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def _town_from_address(addr: str) -> str:
    # adres eindigt op "... 03700 DENIA"
    m = re.search(r"\b0?(\d{4,5})\s+([A-ZÁÉÍÓÚÑ' .-]+)$", addr.strip())
    return m.group(2).strip() if m else ""


def normalise(rec: dict) -> dict:
    cp = str(rec.get("cp") or "").strip()
    if cp and len(cp) == 4:
        cp = "0" + cp
    addr = str(rec.get("direccion") or "")
    town = _town_from_address(addr)
    lat, lon = _f(rec.get("gpsLat")), _f(rec.get("gpsLong"))
    area = config.area_of(town, cp, addr)
    area_note = ""
    if not area and lat and lon:
        for k, (la0, la1, lo0, lo1) in BBOX.items():
            if la0 <= lat <= la1 and lo0 <= lon <= lo1:
                area, area_note = k, "gps-schatting"
                break
    blockers: list[str] = []
    derecho = str(rec.get("derecho") or "")
    pct = _f(rec.get("porcTitularidad"))
    if derecho != "1":
        blockers.append(f"aangeboden recht is geen volle eigendom (derecho={derecho})")
    if pct is not None and pct < 100:
        blockers.append(f"onverdeeld aandeel: {pct:g} %")
    cargas = _f(rec.get("cargas"))
    if cargas:
        blockers.append(f"lasten volgens lijst: {cargas:,.0f} €".replace(",", "."))
    return {
        "source_ref": str(rec.get("id")),
        "sub_ids": [rec.get("subasta")] if rec.get("subasta") else [],
        "boe_id": None,
        "title": (str(rec.get("descripcion") or "")[:120] or "AEAT-veiling"),
        "department": "AEAT",
        "area": area,
        "town": (town + (f" ({area_note})" if area_note else "")) or None,
        "postcode": cp or None,
        "address": addr[:200],
        "ref_catastral": rec.get("refCatastro"),
        "cru": rec.get("cru"),
        "tipo": str(rec.get("tipo")),
        "valuation": _f(rec.get("valoracion")),
        "cargas": cargas,
        "derecho": derecho,
        "pct": pct,
        "end_date": rec.get("finSubasta"),
        "lat": lat, "lon": lon,
        "url": f"https://subastas.boe.es/detalleSubasta.php?idSub={rec.get('subasta')}" if rec.get("subasta") else None,
        "blockers": blockers,
        "raw": {"provincia": rec.get("codProvincia"), "municipioCod": rec.get("municipioCod"), "capital": rec.get("capital"),
                "fotos": len(rec.get("fotos") or []), "bron": config.AEAT_ATTRIBUTION},
    }


def select(arr: list[dict]) -> list[dict]:
    """Alle Alicante-records (provincie 3); het werkgebied wordt in 'area' gemarkeerd."""
    out = []
    for r in arr:
        try:
            if int(r.get("codProvincia")) != PROVINCE_ALICANTE:
                continue
        except (TypeError, ValueError):
            continue
        out.append(normalise(r))
    return out

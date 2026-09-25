"""Adapter Background Properties via onze eigen woningfeed-dienst (poort 3100).

De dienst leest zes Kyero v3-exports en houdt een momentopname in het geheugen. Wij lezen
alleen (nooit de dienst herstarten). Bescherming: een lege of sterk gekrompen momentopname
telt als BRON NIET BEREIKBAAR en levert geen 'verdwenen'-gebeurtenissen op (masterprompt §8, §10).
Gebruiksrechten: schriftelijke afspraak volgens Jan (15-09-2026); document nog niet in de map.
"""
from __future__ import annotations

import hashlib

import httpx

from .. import config


class SourceUnavailable(Exception):
    pass


def _num(v):
    try:
        return float(v) if v is not None and v != "" else None
    except (TypeError, ValueError):
        return None


def fetch(base_url: str | None = None, page_size: int = 100) -> tuple[list[dict], dict]:
    base = (base_url or config.BP_LOCAL_API).rstrip("/")
    with httpx.Client(timeout=config.HTTP_TIMEOUT, headers={"User-Agent": config.USER_AGENT}) as c:
        h = c.get(f"{base}/api/health")
        h.raise_for_status()
        health = h.json()
        if not health.get("properties"):
            raise SourceUnavailable(f"feed leeg (properties={health.get('properties')}, lastFetch={health.get('lastFetch')})")
        items: list[dict] = []
        page = 1
        while True:
            r = c.get(f"{base}/api/properties", params={"page": page, "limit": page_size, "sort": "ref", "order": "asc"})
            r.raise_for_status()
            j = r.json()
            items.extend(j.get("properties", []))
            pag = j.get("pagination", {})
            if page >= int(pag.get("totalPages", 1)):
                break
            page += 1
    meta = {"total": health.get("properties"), "lastFetch": health.get("lastFetch"), "fetched": len(items)}
    if len(items) != int(health.get("properties", 0)):
        meta["warning"] = f"paginering onvolledig: {len(items)} van {health.get('properties')}"
    return items, meta


def normalise(p: dict) -> dict:
    desc = p.get("desc") or {}
    text = desc.get("en") or desc.get("es") or desc.get("nl") or ""
    town = p.get("town") or ""
    loc = p.get("locationDetail") or ""
    urls = p.get("url") or {}
    url = urls.get("en") or urls.get("es") or urls.get("nl") or ""
    features = p.get("features") or []
    ftext = " ".join(features)
    return {
        "source_ref": str(p.get("ref") or p.get("id")),
        "area": config.area_of(town, p.get("postcode"), f"{loc} {text[:200]}"),
        "town": config.norm_place(town),
        "town_raw": town,
        "postcode": p.get("postcode") or None,
        "type": (p.get("type") or "").strip(),
        "price": _num(p.get("price")),
        "currency": p.get("currency") or "EUR",
        "built_m2": _num(p.get("builtArea")),
        "plot_m2": _num(p.get("plotArea")),
        "beds": int(p["beds"]) if _num(p.get("beds")) is not None else None,
        "baths": int(p["baths"]) if _num(p.get("baths")) is not None else None,
        "lat": _num(p.get("latitude")) if config.valid_coord(p.get("latitude"), p.get("longitude")) else None,
        "lon": _num(p.get("longitude")) if config.valid_coord(p.get("latitude"), p.get("longitude")) else None,
        "location_detail": loc,
        "url": url,
        "title": f"{p.get('type') or ''} {loc or town}".strip(),
        "desc_hash": hashlib.sha256((text + "|" + ftext).encode("utf-8")).hexdigest()[:16],
        "desc_excerpt": text[:600],
        "features": features,
        "images_count": len(p.get("images") or []),
        "image_url": next((str(u) for u in (p.get("images") or []) if str(u).startswith("http")), None),
        "source_date": p.get("date") or None,   # Kyero: datum laatste wijziging, geen publicatiedatum
        "new_build": 1 if p.get("newBuild") else 0,
        "_text": text,      # niet opgeslagen; voor signaalherkenning
        "_features": ftext,
    }

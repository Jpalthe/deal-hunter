"""Haalt de coördinaat van het object uit de pagina van een makelaar — maar alleen waar dat mag.

Waarom dit zo omslachtig is. Op de meeste makelaarssites staat wel érgens een coördinaat, maar het
is die van het kantoor of van het midden van het werkgebied. Op 27-09-2026 bleek dat op tien van de
drieëndertig sites het geval: dezelfde coördinaat op élke objectpagina. Wie die overneemt, rekent
daarna helling, overstromingsrisico, bestemming en prijspeil uit op het kantoor van de makelaar, en
het systeem meldt dat met dezelfde stelligheid als een echte meting.

Daarom staat hier geen lijst van patronen die "meestal wel kloppen", maar een lijst van sites
waarvan is gemeten dat de coördinaat per object verschilt. Die meting doet
`tools/coordinaten-verkennen.py` (vier objectpagina's per site) en legt hij vast in
`onderzoek/N12-coordinaten-makelaarssites.json`. Dit bestand leest die uitkomst; zonder meting
gebeurt er niets. Zo kan een site er alleen bij komen doordat iemand hem heeft gemeten, niet
doordat iemand een patroon heeft toegevoegd.

Uitkomst van de meting van 27-09-2026: 3 van de 33 sites, samen 450 van de 3.382 objecten. Bij de
rest staat de coördinaat niet in de pagina — de kaart haalt hem apart op, of er is alleen een
wijknaam. Die objecten houden "ligging onbekend"; dat is eerlijker dan een punt dat er niet is.
"""
from __future__ import annotations

import json
import logging
import re
from functools import lru_cache

from . import config

log = logging.getLogger(__name__)
METING = config.ROOT / "onderzoek" / "N12-coordinaten-makelaarssites.json"
MIN_PAGINAS = 3          # onder drie pagina's zegt "verandert per object" niets

# Dezelfde patronen die de meting gebruikt; het gereedschap importeert ze hiervandaan, zodat wat
# gemeten is en wat gebruikt wordt niet uit elkaar kunnen lopen.
PATRONEN = {
    "data-attribuut": re.compile(
        r'data-(?:lat|latitude)\s*=\s*["\']?(-?\d{1,2}\.\d{3,})["\']?.{0,120}?'
        r'data-(?:lng|lon|longitude)\s*=\s*["\']?(-?\d{1,3}\.\d{3,})', re.S | re.I),
    "json": re.compile(
        r'"lat(?:itude)?"\s*:\s*"?(-?\d{1,2}\.\d{3,})"?.{0,80}?'
        r'"(?:lng|lon|longitude)"\s*:\s*"?(-?\d{1,3}\.\d{3,})"?', re.S | re.I),
    "javascript": re.compile(
        r'\blat\w*\s*[:=]\s*"?(-?\d{1,2}\.\d{3,})"?.{0,80}?\b(?:lng|lon|long\w*)\s*[:=]\s*"?(-?\d{1,3}\.\d{3,})"?',
        re.S | re.I),
    "google-maps": re.compile(
        r'!3d(-?\d{1,2}\.\d{3,})!.{0,40}?!2d(-?\d{1,3}\.\d{3,})|!2d(-?\d{1,3}\.\d{3,})!3d(-?\d{1,2}\.\d{3,})'),
    "maps-parameter": re.compile(
        r'[?&](?:q|ll|center|sll|daddr)=(-?\d{1,2}\.\d{3,})[,%]\s*2?C?(-?\d{1,3}\.\d{3,})', re.I),
    "leaflet": re.compile(r'\[\s*(-?\d{1,2}\.\d{3,})\s*,\s*(-?\d{1,3}\.\d{3,})\s*\]'),
    "osm-bbox": re.compile(r'bbox=(-?\d{1,3}\.\d{3,})(?:%2C|,)(-?\d{1,2}\.\d{3,})', re.I),
}

# Punten die tijdens de meting op élke objectpagina van een site terugkwamen. Eén ervan
# (38,7039 / 0,15677) dook bij twee verschillende sites op, wat erop wijst dat een CRM hem als
# standaardwaarde meegeeft. Zulke punten weigeren wij overal, ook op een site die verder in orde is.
EXTRA_GEWEIGERD = [
    (38.7039, 0.15677),      # vast punt bij randofrealestate; ook als los punt bij remaxinmomas
    (38.78894, 0.16642),     # dook op bij remaxinmomas én bij 52 objecten van atinainmobiliaria:
                             # het midden van het Arenal, dat een CRM als standaard meegeeft. Het
                             # lijkt juist bij elke strandwoning, en dat maakt hem gevaarlijk.
]
GELIJK_GRAAD = 0.0002          # ongeveer 20 meter: genoeg om afrondingsverschillen op te vangen


def _bijna(a: tuple[float, float], b: tuple[float, float]) -> bool:
    return abs(a[0] - b[0]) < GELIJK_GRAAD and abs(a[1] - b[1]) < GELIJK_GRAAD


@lru_cache(maxsize=1)
def _meting() -> tuple[dict, list]:
    """(host → patroonnaam, lijst geweigerde punten) uit het meetrapport."""
    try:
        d = json.loads(METING.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        log.info("geen meetrapport %s: geen enkele site levert een coördinaat", METING.name)
        return {}, list(EXTRA_GEWEIGERD)
    if int(d.get("paginas_per_site") or 0) < MIN_PAGINAS:
        log.warning("meetrapport op %s pagina's per site: te weinig om op te vertrouwen",
                    d.get("paginas_per_site"))
        return {}, list(EXTRA_GEWEIGERD)
    toegestaan, geweigerd = {}, list(EXTRA_GEWEIGERD)
    for host, v in (d.get("sites") or {}).items():
        for p in (v.get("patronen") or {}).values():
            geweigerd += [tuple(pt) for pt in p.get("vast_op_elke_pagina") or []]
        naam = v.get("bruikbaar_patroon")
        if naam and naam in PATRONEN:
            toegestaan[host] = naam
    return toegestaan, geweigerd


def toegestane_sites() -> dict[str, str]:
    return dict(_meting()[0])


def uit_pagina(html: str, host: str) -> tuple[float, float] | None:
    """De coördinaat van dít object, of None.

    Drie eisen, alle drie nodig:
      1. van deze site is gemeten dat de coördinaat per object verschilt;
      2. het afgesproken patroon vindt precies één punt op de pagina — twee punten betekent dat
         wij niet weten welk van de twee het object is, en dan raden wij niet;
      3. het punt ligt in het werkgebied en staat niet op de lijst van vaste punten.
    """
    toegestaan, geweigerd = _meting()
    naam = toegestaan.get((host or "").lower().replace("www.", ""))
    if not naam or not html:
        return None
    punten = set()
    for m in PATRONEN[naam].finditer(html):
        g = [x for x in m.groups() if x]
        if len(g) < 2:
            continue
        a, b = float(g[0]), float(g[1])
        paar = (a, b) if config.valid_coord(a, b) else ((b, a) if config.valid_coord(b, a) else None)
        if paar and not any(_bijna(paar, w) for w in geweigerd):
            punten.add((round(paar[0], 6), round(paar[1], 6)))
    if len(punten) != 1:
        return None
    return punten.pop()

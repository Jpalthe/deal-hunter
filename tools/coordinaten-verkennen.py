#!/usr/bin/env python3
"""Meet per makelaarssite of er een coördinaat van het object zelf op de pagina staat.

Waarom deze meting bestaat. Op 27-09-2026 leverde één objectpagina per site zes treffers op.
Bij nameting op drie pagina's bleek op drie van die zes élke pagina dezelfde coördinaat te geven:
het kantooradres. Wie op één pagina afgaat, schrijft dat adres stilletjes in honderden objecten en
rekent daarna helling, overstromingsrisico en bestemming uit op het kantoor van de makelaar.

De toets is daarom niet "staat er een coördinaat" maar "verandert hij per object". Wat op elke
pagina hetzelfde is, is per definitie niet van het object. Wat op elke pagina anders is, is dat
vrijwel zeker wel — en dat wordt daarna nog eens getoetst tegen de wijk uit de advertentie.

  python tools/coordinaten-verkennen.py [--paginas 4] [--hosts a.com,b.com] [--uit rapport.json]

Leest alleen kantoren met advies "lezen", via dezelfde Site-klasse als de monitor, dus robots.txt
en de pauze tussen verzoeken gelden ook hier.
"""
from __future__ import annotations

import argparse
import collections
import json
import re
import sqlite3
import sys
from pathlib import Path

import httpx

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from dh import config, coordinaat                        # noqa: E402
from dh.adapters.makelaars import Site, laad_kantoren    # noqa: E402

# De patronen staan in dh/coordinaat.py, zodat wat hier gemeten wordt en wat de monitor
# gebruikt niet uit elkaar kunnen lopen.
PATRONEN = coordinaat.PATRONEN


def paren(tekst: str) -> dict[str, set[tuple[float, float]]]:
    """Alle plausibele lon/lat-paren per patroon. De volgorde wordt rechtgezet op het werkgebied."""
    uit: dict[str, set] = collections.defaultdict(set)
    for naam, p in PATRONEN.items():
        for m in p.finditer(tekst):
            g = [x for x in m.groups() if x]
            if len(g) < 2:
                continue
            a, b = float(g[0]), float(g[1])
            paar = (a, b) if config.valid_coord(a, b) else ((b, a) if config.valid_coord(b, a) else None)
            if paar:
                uit[naam].add((round(paar[0], 5), round(paar[1], 5)))
    return uit


def oordeel(per_pagina: list[set]) -> tuple[str, str]:
    """Kan dit patroon op deze site de coördinaat van het object leveren?

    `per_pagina` is per bekeken objectpagina de verzameling gevonden punten, al ontdaan van de
    punten die op álle pagina's voorkomen (dat is de kaart van het kantoor of van het werkgebied)."""
    gevuld = [s for s in per_pagina if s]
    if len(gevuld) < max(2, len(per_pagina) - 1):
        return "te weinig", "op te weinig pagina's iets gevonden"
    if all(len(s) == 1 for s in gevuld) and len({tuple(s) for s in gevuld}) == len(gevuld):
        return "bruikbaar", "één punt per pagina, en op elke pagina een ander"
    if len({tuple(sorted(s)) for s in gevuld}) == 1:
        return "vast", "op elke pagina hetzelfde punt: niet van het object"
    return "meerdere", f"meerdere punten per pagina ({max(len(s) for s in gevuld)} op de drukste)"


def run(paginas: int = 4, hosts: list[str] | None = None) -> dict:
    con = sqlite3.connect(str(config.DB_PATH))
    con.row_factory = sqlite3.Row
    kantoren = {k.host: k for k in laad_kantoren()}
    rijen = con.execute("""SELECT source, count(*) n FROM listings
        WHERE gone_at IS NULL AND area IS NOT NULL AND lat IS NULL AND source LIKE 'makelaar:%'
        GROUP BY 1 ORDER BY n DESC""").fetchall()
    doel = [(r["source"].split(":", 1)[1], r["n"]) for r in rijen]
    if hosts:
        doel = [d for d in doel if d[0] in hosts]
    rapport: dict = {"paginas_per_site": paginas, "sites": {}}
    with httpx.Client(timeout=config.HTTP_TIMEOUT, follow_redirects=True,
                      headers={"User-Agent": config.USER_AGENT, "Accept-Language": "es,en;q=0.8,nl;q=0.6"}) as c:
        for host, aantal in doel:
            k = kantoren.get(host)
            if not k:
                rapport["sites"][host] = {"objecten": aantal, "overgeslagen": "niet in kader/makelaars.json"}
                continue
            if not k.toegestaan:
                rapport["sites"][host] = {"objecten": aantal, "overgeslagen": f"advies: {k.advies}"}
                continue
            urls = [r["url"] for r in con.execute(
                "SELECT url FROM listings WHERE source=? AND gone_at IS NULL AND url IS NOT NULL "
                "ORDER BY id LIMIT ?", (f"makelaar:{host}", paginas))]
            s = Site(k, c)
            gevonden, gelezen = [], 0
            for u in urls:
                t = s.haal(u)
                if t is None:
                    gevonden.append({})
                    continue
                gelezen += 1
                gevonden.append(paren(t))
            # punten die op álle gelezen pagina's staan zijn van de site, niet van het object
            namen = {n for g in gevonden for n in g}
            per_patroon = {}
            for n in namen:
                sets = [g.get(n, set()) for g in gevonden]
                vast = set.intersection(*[s_ for s_ in sets if s_]) if any(sets) else set()
                schoon = [s_ - vast for s_ in sets]
                soort, waarom = oordeel(schoon)
                per_patroon[n] = {"oordeel": soort, "waarom": waarom,
                                  "vast_op_elke_pagina": sorted(vast)[:3],
                                  "per_pagina": [sorted(s_)[:3] for s_ in schoon]}
            beste = next((n for n, v in per_patroon.items() if v["oordeel"] == "bruikbaar"), None)
            rapport["sites"][host] = {"objecten": aantal, "kantoor": k.naam, "cms": (k.cms or "")[:60],
                                      "paginas_gelezen": gelezen, "bruikbaar_patroon": beste,
                                      "patronen": per_patroon}
            vlag = "JA " if beste else "nee"
            print(f"{vlag} {host:32s} {aantal:4d} objecten  {beste or '—'}", flush=True)
    con.close()
    bruikbaar = {h: v for h, v in rapport["sites"].items() if v.get("bruikbaar_patroon")}
    rapport["samenvatting"] = {
        "sites_bekeken": len(rapport["sites"]),
        "sites_met_coordinaat_per_object": len(bruikbaar),
        "objecten_daarmee_bereikbaar": sum(v["objecten"] for v in bruikbaar.values()),
        "objecten_totaal": sum(v["objecten"] for v in rapport["sites"].values()),
    }
    return rapport


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--paginas", type=int, default=4)
    ap.add_argument("--hosts", default="")
    ap.add_argument("--uit", default="onderzoek/N12-coordinaten-makelaarssites.json")
    a = ap.parse_args(argv)
    r = run(a.paginas, [h.strip() for h in a.hosts.split(",") if h.strip()] or None)
    p = config.ROOT / a.uit
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(r, ensure_ascii=False, indent=1), encoding="utf-8")
    print("\n" + json.dumps(r["samenvatting"], ensure_ascii=False, indent=1))
    print("rapport:", p)
    return 0


if __name__ == "__main__":
    sys.exit(main())

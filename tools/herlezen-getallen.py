#!/usr/bin/env python3
"""Leest objecten opnieuw waarvan de getallen niet kunnen kloppen.

Aanleiding 27-09-2026: `_num` haalde élke punt uit een getal weg, omdat een punt in Spanje
duizendtallen scheidt. In een JSON-LD-veld is hij een decimaalteken: `"floorSize": "795.00"` werd
zo 79.500 m². 191 objecten hadden daardoor een bebouwd oppervlak dat niet bestaat, tot 83.235 m²
aan toe. Die getallen gaan rechtstreeks de bouwkosten en de verkoopwaarde in, dus een fout hier
verandert elk bedrag in het dossier.

De lezer is hersteld; dit haalt de pagina's van de getroffen objecten opnieuw op en zet de
gecorrigeerde waarden terug. Alleen prijs, oppervlak, slaapkamers en badkamers worden bijgewerkt —
verder blijft de advertentie zoals zij was.

  python tools/herlezen-getallen.py           # laat zien wat er zou veranderen
  python tools/herlezen-getallen.py --doen
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import httpx

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from dh import config                                              # noqa: E402
from dh.adapters.makelaars import Site, laad_kantoren, ontleed     # noqa: E402
from dh.store import Store                                         # noqa: E402

# Grenzen waarboven een waarde niet van een woning kan zijn. Ruim genomen: een perceel van
# 108.000 m² bestaat hier wél (en staat ook echt in de lijst), een woning van 1.500 m² niet.
ONMOGELIJK = "(built_m2 > 1500 OR plot_m2 > 60000 OR price > 15000000)"
VELDEN = ("price", "built_m2", "plot_m2", "beds", "baths")


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--doen", action="store_true")
    ap.add_argument("--limit", type=int, default=0)
    a = ap.parse_args(argv)
    store = Store()
    q = (f"SELECT id, source, url, title, price, built_m2, plot_m2, beds, baths FROM listings "
         f"WHERE gone_at IS NULL AND source LIKE 'makelaar:%' AND {ONMOGELIJK} ORDER BY id")
    if a.limit:
        q += f" LIMIT {int(a.limit)}"
    rijen = store.con.execute(q).fetchall()
    kantoren = {k.host: k for k in laad_kantoren()}
    print(f"{len(rijen)} objecten met een onmogelijke waarde")
    sites: dict[str, Site] = {}
    gewijzigd = mislukt = ongewijzigd = 0
    with httpx.Client(timeout=config.HTTP_TIMEOUT, follow_redirects=True,
                      headers={"User-Agent": config.USER_AGENT, "Accept-Language": "es,en;q=0.8,nl;q=0.6"}) as c:
        for r in rijen:
            host = r["source"].split(":", 1)[-1]
            k = kantoren.get(host)
            if not k or not k.toegestaan:
                mislukt += 1
                continue
            s = sites.get(host) or sites.setdefault(host, Site(k, c))
            t = s.haal(r["url"])
            rec = ontleed(t, r["url"], k) if t else None
            if not rec:
                mislukt += 1
                continue
            # Alleen bijwerken waar de nieuwe lezing werkelijk iets oplevert. Geeft zij niets,
            # dan houden wij wat er stond: een leeg veld is geen correctie maar verlies.
            anders = {v: rec.get(v) for v in VELDEN
                      if rec.get(v) and (rec.get(v) or 0) != (r[v] or 0)}
            if not anders:
                ongewijzigd += 1
                continue
            gewijzigd += 1
            print(f"  {r['id']:5d} {host:24s} " + ", ".join(
                f"{v}: {r[v] or 0:.0f} → {n or 0:.0f}" for v, n in anders.items()))
            if a.doen:
                store.con.execute(
                    "UPDATE listings SET " + ", ".join(f"{v}=?" for v in anders) + " WHERE id=?",
                    tuple(anders.values()) + (r["id"],))
    if a.doen:
        store.con.commit()
    store.close()
    print(f"\ngewijzigd {gewijzigd} · ongewijzigd {ongewijzigd} · niet gelukt {mislukt}"
          + ("" if a.doen else "  — niets opgeslagen; met --doen wel"))
    return 0


if __name__ == "__main__":
    sys.exit(main())

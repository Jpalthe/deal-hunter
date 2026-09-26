#!/usr/bin/env python3
"""Haalt zoekresultaatpagina's uit de database die als woning waren binnengekomen.

Gevonden 27-09-2026: 280 van de 3.382 objecten van makelaarssites waren geen woning maar een
filterpagina — `/results/?type[0]=1&id_tipo_operacion=1&od=prd.d` en varianten. Elk zo'n "object"
droeg de prijs en het oppervlak van de woning die toevallig bovenaan dat filter stond. Eén prijs
van € 1.950.000 met 389/409 m² kwam eenentwintig keer voor. Over één ervan is al een melding
gestuurd.

De lezer weigert ze sinds dezelfde dag (`makelaars.is_zoekopdracht`); dit ruimt op wat er al staat.
Niet verwijderen maar op `gone_at` zetten, met een gebeurtenis erbij: dan blijft zichtbaar dat ze
er ooit waren en waarom ze weg zijn.

  python tools/opruimen-zoekpaginas.py            # laat zien wat er zou gebeuren
  python tools/opruimen-zoekpaginas.py --doen     # voert het uit
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from dh.adapters.makelaars import is_overzichtspagina   # noqa: E402
from dh.store import Store, now_iso                     # noqa: E402

REDEN = "zoekresultaat- of overzichtspagina, geen woning"


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--doen", action="store_true", help="werkelijk opruimen")
    a = ap.parse_args(argv)
    store = Store()
    rijen = store.con.execute(
        "SELECT id, source, url, title, price FROM listings WHERE gone_at IS NULL AND source LIKE 'makelaar:%'"
    ).fetchall()
    raak = [r for r in rijen if is_overzichtspagina(r["url"], r["title"])]
    per: dict[str, int] = {}
    for r in raak:
        k = r["source"].split(":", 1)[-1]
        per[k] = per.get(k, 0) + 1
    print(f"{len(raak)} van {len(rijen)} actieve makelaarsobjecten zijn geen woning")
    for k, n in sorted(per.items(), key=lambda x: -x[1]):
        print(f"  {n:4d}  {k}")
    for r in raak[:3]:
        print(f"  voorbeeld: € {r['price'] or 0:,.0f} — {(r['title'] or '')[:40]} — {r['url'][:80]}".replace(",", "."))
    if not a.doen:
        print("\nniets gewijzigd; met --doen worden ze op 'verdwenen' gezet")
        store.close()
        return 0
    nu = now_iso()
    for r in raak:
        store.con.execute("UPDATE listings SET gone_at=? WHERE id=?", (nu, r["id"]))
        store.add_event(None, "OPGERUIMD", listing_id=r["id"], details={"reden": REDEN, "url": r["url"]})
    store.con.commit()
    store.close()
    print(f"\n{len(raak)} objecten op verdwenen gezet, met de reden erbij in de gebeurtenissen")
    return 0


if __name__ == "__main__":
    sys.exit(main())

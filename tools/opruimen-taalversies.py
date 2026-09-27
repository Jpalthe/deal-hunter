#!/usr/bin/env python3
"""Ruimt dezelfde woning op die onder meer dan één taal in de lijst staat.

Meertalige makelaarssites geven elke woning een eigen adres per taal, met hetzelfde objectnummer
erin: `...-es1660088.html`, `...-da1660088.html`, `...-se1660088.html`. De lezer kende alleen
es/gb/en/nl/de/fr, dus Deens, Zweeds, Italiaans, Fins en Portugees kwamen als losse objecten
binnen — 51 woningen, 172 overtollige rijen (foutenjacht 27-09-2026).

Erger dan de dubbeling zelf: de taalversies droegen verschillende prijzen, en de meldingenlijst
sorteert op de grootste ruimte. Systematisch won dus de goedkoopste versie, en dat is de foutste.

Welke versie blijft staan: de Spaanse als die er is — die heeft de meest complete velden — anders
de rij met de meeste ingevulde gegevens. De rest gaat op 'verdwenen' met de reden erbij; niets
wordt gewist.

  python tools/opruimen-taalversies.py           # laat zien wat er zou gebeuren
  python tools/opruimen-taalversies.py --doen
"""
from __future__ import annotations

import argparse
import collections
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from dh.store import Store, now_iso                      # noqa: E402

TAAL_IN_URL = re.compile(r"-([a-z]{2})(\d{4,9})\.html$", re.I)
GEVULD = ("price", "built_m2", "plot_m2", "beds", "baths", "lat", "desc_excerpt", "image_url")


def rijkdom(r) -> int:
    return sum(1 for v in GEVULD if r[v])


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--doen", action="store_true")
    a = ap.parse_args(argv)
    store = Store()
    groepen: dict[tuple, list] = collections.defaultdict(list)
    for r in store.con.execute(
            "SELECT id, source, url, " + ", ".join(GEVULD) + " FROM listings WHERE gone_at IS NULL"):
        m = TAAL_IN_URL.search(r["url"] or "")
        if m:
            groepen[(r["source"], m.group(2))].append((m.group(1).lower(), r))
    dubbel = {k: v for k, v in groepen.items() if len(v) > 1}
    weg, blijft = [], 0
    for (bron, nummer), leden in sorted(dubbel.items()):
        spaans = [r for t, r in leden if t == "es"]
        houden = spaans[0] if spaans else max((r for _, r in leden), key=rijkdom)
        blijft += 1
        for taal, r in leden:
            if r["id"] != houden["id"]:
                weg.append((r, houden, taal, nummer))
    print(f"{len(dubbel)} woningen staan meer dan één keer in de lijst; {len(weg)} overtollige rijen")
    print(f"{blijft} blijven staan, {len(weg)} gaan op verdwenen\n")
    for r, houden, taal, nummer in weg[:5]:
        print(f"  {r['id']:5d} ({taal}) → blijft {houden['id']} · object {nummer} · "
              f"{r['source'].split(':')[-1]}")
    if not a.doen:
        print("\nniets gewijzigd; met --doen worden ze op verdwenen gezet")
        store.close()
        return 0
    nu = now_iso()
    for r, houden, taal, nummer in weg:
        store.con.execute("UPDATE listings SET gone_at=? WHERE id=?", (nu, r["id"]))
        store.add_event(None, "OPGERUIMD", listing_id=r["id"], details={
            "reden": f"zelfde woning als {houden['id']}, alleen de {taal}-versie van de pagina",
            "objectnummer": nummer, "blijft_staan": houden["id"], "url": r["url"]})
    store.con.commit()
    store.close()
    print(f"\n{len(weg)} taalversies op verdwenen gezet")
    return 0


if __name__ == "__main__":
    sys.exit(main())

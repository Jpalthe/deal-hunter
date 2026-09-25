"""Herberekent signalen en voorfilter voor alle actieve advertenties zonder bronnen op te halen.
Gebruik na een wijziging van de regels of nadat kader/comparables.json of parameters.json is bijgewerkt.
  python -m dh.reanalyse
"""
from __future__ import annotations

import json
import sys

from . import prefilter, signals
from .store import Store


def main() -> int:
    store = Store()
    pf = prefilter.Prefilter()
    rows = store.active_listings(area_only=False)
    n = 0
    for r in rows:
        # Idealista-kandidaten krijgen hun analyse uit dh.import_kandidaten; al het andere hoort hier
        # opnieuw langs de signalen. Dat gold eerder alleen voor de woningfeed, waardoor de objecten
        # van makelaarssites hun categorie van het moment van inlezen hielden en een nieuwe regel
        # nooit met terugwerkende kracht werkte.
        bron = str(r["source"] or "")
        if not (bron == "bp" or bron.startswith("makelaar:")):
            continue
        rec = dict(r)
        # Titel én omschrijving, net als bij het inlezen. Alleen de omschrijving nemen kostte de
        # herkenning van objecten waar het beslissende woord in de titel staat: "zu urbanisieren",
        # "para reformar", "traspaso". Bij makelaarssites is de omschrijving soms zelfs de
        # cookiemelding van de site, en dan is de titel het enige wat er staat.
        rec["_text"] = " ".join(x for x in (r["title"], r["desc_excerpt"]) if x)
        try:
            feats = " ".join(json.loads(r["features"] or "[]"))
        except json.JSONDecodeError:
            feats = ""
        rec["_features"] = feats
        sig = signals.analyse(rec["_text"], feats, r["type"] or "", bool(r["new_build"]))
        res = pf.run(rec, sig)
        store.set_analysis(int(r["id"]), signals=sig, category=res["category"], prefilter=res)
        n += 1
    store.close()
    from . import import_kandidaten
    import_kandidaten.main()
    print(f"herberekend: {n} advertenties; vergelijkingsprijzen {'geladen' if pf.comps else 'ontbreken'}; parameters {'geladen' if pf.params else 'ontbreken'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

"""Zet de handmatig gevonden Idealista-kandidaten (kader/kandidaten.json) in de database als bron 'idealista',
zodat ze op de kaart, in de lijst en in de reviews meedoen. Idempotent.

  python -m dh.import_kandidaten
"""
from __future__ import annotations

import hashlib
import json
import sys

from . import config, feasibility
from .store import Store

TYPE = {"renovatie": "Villa", "perceel": "Land", "appartement": "Apartment", "pand": "Town house"}
CAT = {"renovatie": "renovatie", "perceel": "perceel", "appartement": "appartement-renovatie", "pand": "renovatie"}


def main() -> int:
    _, _, _, kand = feasibility.inputs()
    store = Store()
    run_id = store.start_run("import-kandidaten")
    n = 0
    for c in kand:
        text = " · ".join(c.get("claims") or [])
        rec = {
            "source_ref": str(c["code"]), "area": "javea", "town": "javea", "town_raw": "Jávea", "postcode": None,
            "type": TYPE.get(c.get("type"), c.get("type") or ""), "price": c.get("price_ask"), "currency": "EUR",
            "built_m2": c.get("built_m2") or None, "plot_m2": c.get("plot_m2") or None, "beds": None, "baths": None,
            "lat": c.get("lat") if config.valid_coord(c.get("lat"), c.get("lon")) else None,
            "lon": c.get("lon") if config.valid_coord(c.get("lat"), c.get("lon")) else None,
            "location_detail": (c.get("zone") or "") + (" · pakket van 16 kavels voor 725.000 €, prijs per kavel" if c["id"] == "K10" else ""), "url": c.get("url"), "title": f"{c['id']} {c.get('zone') or ''}",
            "desc_hash": hashlib.sha256(text.encode("utf-8")).hexdigest()[:16], "desc_excerpt": text[:600],
            "features": [], "images_count": 0, "source_date": None, "new_build": 0,
        }
        lid, kind, _ = store.upsert_listing(run_id, "idealista", rec)
        row = dict(store.con.execute("SELECT * FROM listings WHERE id=?", (lid,)).fetchone())
        res = feasibility.compute(row)
        best = next((s for s in res.get("scenarios", []) if s.get("key") == res.get("best_key")), None)
        cls = feasibility.classify(rec["price"], best)
        verdict = {"groen": "kandidaat: haalt eis (indicatief)", "blauw": "kandidaat: haalt eis in basis (indicatief)",
                   "oranje": "kandidaat: onderhandelbaar tot 30 % (indicatief)", "grijs": "kandidaat: onder eis bij vraagprijs (indicatief)",
                   "onzeker": "kandidaat: niet betrouwbaar te rekenen", "geen": "afwijzen" if c["id"] == "K11" else "kandidaat: geen indicatie"}[cls]
        indicative = None
        if best:
            indicative = {"scenario": best["label"], "comps_n": best["comps"]["n"], "max_price": best["max_price"],
                          "max_price_25_conservative": best["max_price"]["conservative"],
                          "margin_on_sale": best["margin_at_asking"], "roi_base": None, "roi_conservative": None,
                          "warnings": best["warnings"], "label": "vraagprijzen, geen transacties"}
        store.set_analysis(lid, signals={"kandidaat_id": c["id"], "blockers": c.get("blockers", []), "claims": c.get("claims", [])},
                           category=CAT.get(c.get("type"), "overig"),
                           prefilter={"category": CAT.get(c.get("type"), "overig"), "zone": c.get("comps_zone"), "verdict": verdict,
                                      "class": cls, "indicative": indicative, "reasons": c.get("blockers", [])[:3]})
        n += 1
    store.mark_gone(run_id, "idealista", {str(c["code"]) for c in kand})
    store.con.execute("UPDATE events SET kind='GEÏMPORTEERD' WHERE run_id=? AND kind IN ('NIEUW','NULMETING')", (run_id,))
    store.con.commit()
    store.finish_run(run_id, "ok", {"kandidaten": n})
    store.close()
    print(f"geïmporteerd: {n} kandidaten")
    return 0


if __name__ == "__main__":
    sys.exit(main())

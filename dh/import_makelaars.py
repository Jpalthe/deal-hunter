"""Leest de toegestane makelaarssites en zet hun aanbod in de database, per kantoor als eigen bron.

  python -m dh.import_makelaars [--alleen xabiacasa.com] [--max 50]

Bronsleutel per kantoor: makelaar:<host>. Zo blijft zichtbaar bij wie een object vandaan komt, en
kan één woning die bij drie kantoren staat drie keer voorkomen zonder dat de tellingen elkaar
overschrijven.

Wat dit extra doet ten opzichte van de andere importeurs: per object nagaan of het al op een
portaal staat (de BP-feed of de Idealista-oogst). Staat het nergens anders, dan is het alleen bij
die makelaar te vinden, en dat is precies wat Jan zoekt. Die vergelijking gaat op plaats, prijs
en oppervlakte, want een referentie of adres hebben we zelden aan twee kanten.
"""
from __future__ import annotations

import argparse
import json
import logging
import sys

from . import config, prefilter, signals
from .adapters import makelaars
from .store import Store

log = logging.getLogger("dh.import_makelaars")

PRIJS_MARGE = 0.02      # zelfde woning, misschien afgerond
M2_MARGE = 0.06         # oppervlakten verschillen per kantoor een paar procent


def portaal_kandidaten(store: Store) -> list[dict]:
    """Alles wat op een portaal of in de feed staat, compact voor de vergelijking."""
    rows = store.con.execute(
        "SELECT id, source, source_ref, area, price, built_m2, plot_m2, type FROM listings "
        "WHERE gone_at IS NULL AND source IN ('bp', 'idealista', 'idealista-zoek') AND price IS NOT NULL").fetchall()
    return [dict(r) for r in rows]


def _dichtbij(a, b, marge) -> bool:
    if not a or not b:
        return False
    return abs(float(a) - float(b)) <= marge * max(float(a), float(b))


def zoek_op_portaal(rec: dict, kandidaten: list[dict]) -> dict | None:
    """Zoekt dezelfde woning bij de portaalbronnen: zelfde gebied, prijs binnen 2 %, en de bebouwde
    of de perceeloppervlakte binnen 6 %. Twee treffers op maat zijn sterker dan één."""
    beste = None
    for k in kandidaten:
        if k["area"] != rec.get("area"):
            continue
        if not _dichtbij(k["price"], rec.get("price"), PRIJS_MARGE):
            continue
        score = 0
        if _dichtbij(k["built_m2"], rec.get("built_m2"), M2_MARGE):
            score += 1
        if _dichtbij(k["plot_m2"], rec.get("plot_m2"), M2_MARGE):
            score += 1
        if rec.get("type") == "Land" and k.get("type") == "Land" and score:
            score += 1
        if score and (beste is None or score > beste["score"]):
            beste = {"score": score, "source": k["source"], "ref": k["source_ref"], "id": k["id"]}
    return beste


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--alleen", default="", help="komma-gescheiden hosts of namen")
    ap.add_argument("--max", type=int, default=None, help="maximaal objecten per site (test)")
    a = ap.parse_args(argv)
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s: %(message)s")
    logging.getLogger("httpx").setLevel(logging.WARNING)

    alleen = [x.strip() for x in a.alleen.split(",") if x.strip()] or None
    per_site, verslag = makelaars.lees_alles(alleen=alleen, max_per_site=a.max)

    pf = prefilter.Prefilter()
    store = Store()
    run_id = store.start_run("import-makelaars")
    kandidaten = portaal_kandidaten(store)
    totaal = {"kantoren": 0, "objecten": 0, "in_werkgebied": 0, "nieuw": 0, "alleen_bij_makelaar": 0, "ook_op_portaal": 0}
    try:
        for host, recs in per_site.items():
            bron = f"makelaar:{host}"
            gezien: set[str] = set()
            totaal["kantoren"] += 1
            for rec in recs:
                totaal["objecten"] += 1
                if not rec.get("area"):
                    continue
                totaal["in_werkgebied"] += 1
                kantoor = rec.pop("_kantoor", host)
                rec.pop("_verhuur", None)
                gezien.add(rec["source_ref"])
                lid, kind, _ = store.upsert_listing(run_id, bron, rec)
                if kind in ("NIEUW", "NULMETING"):
                    totaal["nieuw"] += 1
                sig = signals.analyse(rec["_text"], rec["_features"], rec["type"], bool(rec["new_build"]))
                match = zoek_op_portaal(rec, kandidaten)
                sig["kantoor"] = kantoor
                sig["portaal"] = match
                if match:
                    totaal["ook_op_portaal"] += 1
                else:
                    totaal["alleen_bij_makelaar"] += 1
                    sig["alleen_bij_makelaar"] = True
                pfr = pf.run(rec, sig)
                store.set_analysis(lid, signals=sig, category=pfr["category"], prefilter=pfr)
            gone = store.mark_gone(run_id, bron, gezien)
            store.source_status(bron, True, count=len(gezien))
            if gone:
                log.info("%s: %s objecten niet meer gevonden", host, len(gone))
        for host, v in verslag.get("kantoren", {}).items():
            if v.get("fout"):
                store.source_status(f"makelaar:{host}", False, error=v["fout"])
        store.finish_run(run_id, "ok", {**totaal, "verslag": verslag})
    finally:
        store.close()
    print(json.dumps({**totaal, "verslag": verslag}, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())

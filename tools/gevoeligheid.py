#!/usr/bin/env python3
"""Gevoeligheidsanalyse op de haalbaarheid: welke aanname beslist? (masterprompt §21)
Draait de rekenaar met varianten van rendementseis, honoraria, commissie en bouwprijs.
  python3 tools/gevoeligheid.py            → markdown-tabel op stdout
"""
import copy, importlib.util, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); K = os.path.join(HERE, "..", "kader")
spec = importlib.util.spec_from_file_location("haalbaarheid", os.path.join(HERE, "haalbaarheid.py"))
m = importlib.util.module_from_spec(spec); sys.modules["haalbaarheid"] = m; spec.loader.exec_module(m)
kader = json.load(open(os.path.join(K, "investeringskader.json"))); params = json.load(open(os.path.join(K, "parameters.json")))["values"]
comps = json.load(open(os.path.join(K, "comparables.json")))["zones"]; kand = json.load(open(os.path.join(K, "kandidaten.json")))["kandidaten"]

def run(k, p, roi=None):
    k = copy.deepcopy(k)
    if roi: k["rendementseis_op_projectkosten"] = roi
    out = {}
    for e in m.evaluate(k, p, comps, kand):
        for s in e["scenarios"]:
            if s.get("status") == "berekend":
                out[(e["id"], s["key"])] = (s["at_asking"]["base"]["roi_on_costs"], s["at_asking"]["conservative"]["roi_on_costs"],
                                            s["max_price_for_roi"]["conservative"], s["max_price_for_roi"]["base"])
    return out

def bk(k, reno=None, nieuw=None):
    k = copy.deepcopy(k)
    if reno: k["bouwkosten_eur_per_m2"]["renovatie"] = reno
    if nieuw: k["bouwkosten_eur_per_m2"]["nieuwbouw"] = nieuw
    return k

def roi(margin):
    return margin / (1 - margin)


FEES = params["architect_pct_of_pem"] + params["aparejador_pct_of_pem"]
MARGIN = kader.get("winstmarge_op_verkoop_min", 0.20)
VARIANTS = [
    (f"Basis (Jan: {MARGIN:.0%} marge op verkoop, honoraria {FEES:.0%}, courtage {params['agent_commission_pct']:.0%}, 2.000 / 1.000 €/m²)".replace("%", " %"), kader, params, None),
    ("Marge-eis 15 % op verkoop", kader, params, roi(0.15)),
    ("Marge-eis 10 % op verkoop", kader, params, roi(0.10)),
    ("Honoraria 12 % in plaats van 8 %", kader, {**params, "architect_pct_of_pem": 0.09, "aparejador_pct_of_pem": 0.03}, None),
    ("Courtage 3 % in plaats van 5 %", kader, {**params, "agent_commission_pct": 0.03}, None),
    ("Nieuwbouw 1.700 €/m² (eigen uitvoering)", bk(kader, nieuw=1700), params, None),
    ("Renovatie 800 €/m² (eigen uitvoering)", bk(kader, reno=800), params, None),
    ("Alles gunstig (15 % marge, 3 % courtage, 1.700 / 800 €/m²)", bk(kader, 800, 1700), {**params, "agent_commission_pct": 0.03}, roi(0.15)),
]
if __name__ == "__main__":
    base = run(kader, params)
    keys = sorted(base.keys())
    print("| Variant | Scenario's die de eis halen (conservatief / basis) | " + " | ".join(f"{a} {b}" for a, b in keys) + " |")
    print("|---|---|" + "---:|" * len(keys))
    for name, k, p, roi in VARIANTS:
        r = run(k, p, roi); eis = roi or k["rendementseis_op_projectkosten"]
        nc = sum(1 for v in r.values() if v[1] >= eis); nb = sum(1 for v in r.values() if v[0] >= eis)
        print(f"| {name} | {nc} / {nb} van {len(r)} | " + " | ".join(f"{int(r[x][2]/1000)}k / {int(r[x][3]/1000)}k" if x in r else "—" for x in keys) + " |")
    print("\nCellen: maximale koopprijs bij de eis, conservatief / basis (verkoop op p25 / mediaan van de wijk).")

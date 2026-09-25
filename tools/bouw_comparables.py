#!/usr/bin/env python3
"""Bouwt kader/comparables.json uit de gestructureerde wijkresultaten en past controle-uitkomsten toe.

Invoer: een of meer JSON-bestanden met {"zones": {zone: {series:{...}}}, "verifs": {zone: {"verdicts":[...]}}}.
Regels:
- 'refuted' met gecorrigeerde cijfers → de gecorrigeerde cijfers worden gebruikt (oude staan in 'original').
- 'refuted' zonder cijfers → reeks krijgt n=0 en wordt niet gebruikt.
- 'unverifiable' of geen controle → cijfers blijven, met label in 'verification'.
Gebruik: python3 tools/bouw_comparables.py invoer1.json [invoer2.json ...]
"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(HERE, "..", "kader", "comparables.json")
zones, verifs = {}, {}
for path in sys.argv[1:]:
    d = json.load(open(path, encoding="utf-8"))
    zones.update(d.get("zones", {}))
    for z, v in d.get("verifs", {}).items():
        verifs[z] = v
out = {"versie": "2026-09-15", "bron": "Idealista-assistent; vraagprijzen per m² gebouwd; geen transacties; controle per wijk in onderzoek/H01-*.verificatie.md", "zones": {}}
report = []
for z, r in sorted(zones.items()):
    series = {}
    vmap = {}
    for x in (verifs.get(z, {}).get("verdicts") or []):
        vmap[(x.get("series") or "").strip()] = x
    for name, s in r["series"].items():
        e = {k: s.get(k) for k in ("n", "min", "p25", "median", "p75", "max", "source", "date", "note")}
        e["examples"] = [{k: ex.get(k) for k in ("code", "price", "m2", "eur_m2", "year", "label")} for ex in (s.get("examples") or [])][:8]
        v = vmap.get(name)
        if v is None:
            e["verification"] = "niet gecontroleerd" if z not in verifs else "niet afzonderlijk beoordeeld"
        elif v["verdict"] == "confirmed":
            e["verification"] = "bevestigd"
        elif v["verdict"] == "refuted":
            if v.get("corrected_median"):
                e["original"] = {k: e.get(k) for k in ("n", "p25", "median", "p75")}
                for k in ("n", "p25", "median", "p75"):
                    ck = "corrected_" + k
                    if v.get(ck) is not None:
                        e[k] = v[ck]
                e["verification"] = "gecorrigeerd na controle: " + (v.get("note") or "")[:200]
            else:
                e["original"] = {k: e.get(k) for k in ("n", "p25", "median", "p75")}
                e["n"] = 0
                e["verification"] = "weerlegd zonder correctie; niet gebruiken: " + (v.get("note") or "")[:200]
        else:
            e["verification"] = "niet te bevestigen: " + (v.get("note") or "")[:160]
        if e.get("n") and e.get("median"):
            series[name] = e
        report.append((z, name, e.get("n"), e.get("median"), e["verification"][:60]))
    series["_caveats"] = r.get("caveats", [])
    out["zones"][z] = series
json.dump(out, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
for row in report:
    print("%-18s %-30s n=%-4s med=%-6s %s" % row)
print("geschreven:", OUT)

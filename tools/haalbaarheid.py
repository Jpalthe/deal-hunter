#!/usr/bin/env python3
"""Haalbaarheidsrekenaar TREE Deal Hunter.

Geteste rekenregels (masterprompt §21–22): bedragen worden hier berekend, niet door een
taalmodel. Invoer: drie JSON-bestanden.

  kader/investeringskader.json   rendementseis, doorlooptijd, bouwkosten per m² (Jan)
  kader/parameters.json          belastingen en kosten met bron en bewijstype (uit R14)
  kader/comparables.json         vraagprijzen per m² van gerenoveerd/nieuw per wijk
  kader/kandidaten.json          kandidaten met scenario's (m², sloop, zwembad, ...)

Uitvoer: kader/haalbaarheid.json en een markdown-tabel op stdout.

Alle bedragen in euro, exclusief btw tenzij anders vermeld. Verkoopprijzen zijn
vraagprijzen van vergelijkingsobjecten, geen transactieprijzen.

Gebruik:  python3 tools/haalbaarheid.py [--kader DIR] [--markdown]
Tests:    python3 tools/haalbaarheid.py --selftest
"""
from __future__ import annotations

import argparse
import json
import math
import os
import sys
from dataclasses import dataclass, field, asdict
from typing import Any

# ----------------------------------------------------------------------------- kosten


def itp(price: float, p: dict) -> float:
    """Overdrachtsbelasting Comunitat Valenciana. Boven de drempel geldt het hoge tarief
    over het HELE bedrag (geen schijf), zoals R14 vaststelt."""
    if price > p["itp_threshold"]:
        return price * p["itp_rate_above_threshold"]
    return price * p["itp_rate"]


def purchase_taxes(price: float, p: dict, vat_purchase: bool) -> dict:
    """Belasting bij aankoop: ITP (tweedehands van particulier/vennootschap zonder btw)
    of btw + AJD (perceel of nieuwbouw van een btw-plichtige verkoper)."""
    if vat_purchase:
        vat = price * p["vat_purchase_rate"]
        ajd = price * p["ajd_rate"]
        return {"itp": 0.0, "vat_purchase": vat, "ajd": ajd, "total": vat + ajd}
    t = itp(price, p)
    return {"itp": t, "vat_purchase": 0.0, "ajd": 0.0, "total": t}


def purchase_costs(price: float, p: dict) -> float:
    """Notaris, register, gestoría, juridische en technische due diligence."""
    return price * p["notary_registry_pct"] + p["legal_dd_eur"] + p["technical_dd_eur"]


@dataclass
class Scenario:
    key: str
    label: str
    kind: str                      # "renovatie" | "nieuwbouw" | "renovatie_plus_uitbreiding" | "geen"
    renovation_m2: float = 0.0     # m² te renoveren tegen renovatietarief
    newbuild_m2: float = 0.0       # m² nieuw te bouwen tegen nieuwbouwtarief
    demolition_m2: float = 0.0     # m² te slopen
    pool: bool = False             # nieuw zwembad
    pool_renovation: bool = False  # bestaand zwembad opknappen
    exterior_m2: float = 0.0       # buitenruimte/terras/keermuren aan te leggen
    result_m2: float = 0.0         # verkoopbaar gebouwd m² na afloop
    comps_key: str = "villa_renovated"  # welke vergelijkingsreeks de verkoopprijs geeft
    months: int = 18               # totaal; wordt berekend zodra de drie blokken bekend zijn
    permit_months: int | None = None   # vergunning: obra menor 0, obra mayor via ECUV ~5 (Jan 25-09-2026)
    build_months: int | None = None    # bouw met eigen ploeg
    sale_months: int | None = None     # oplevering tot notaris
    slope: str | None = None           # None | "vlak" | "licht" | "steil" — bepaalt het grondwerk
    vat_recoverable: bool = False  # btw op bouw terugvorderbaar (nieuwbouw verkocht met btw)
    renovation_vat_rate: float | None = None  # None = standaardtarief uit parameters
    units: int = 1                 # aantal verkoopbare woningen (splitsing/appartementen)
    kitchens: int = 0              # aantal keukens; Jan 17-09-2026: zit NIET in het €/m²-tarief
    bathrooms: int = 0             # aantal badkamers; idem
    fitout_level: str = "midden"   # "midden" | "hoog" — bepaalt de keukenprijs
    unknown_costs: list[str] = field(default_factory=list)  # kostenposten die niet te ramen zijn → niet betrouwbaar
    notes: str = ""
    assumptions: list[str] = field(default_factory=list)

    def __post_init__(self):
        # Jan 25-09-2026: de doorlooptijd is opgebouwd uit vergunning, bouw en verkoop. Staan die
        # blokken er, dan is het totaal daarvan afgeleid en niet meer een los vast getal.
        if self.build_months is not None:
            self.months = int((self.permit_months or 0) + self.build_months + (self.sale_months or 0))


def default_fitout(result_m2: float, units: int = 1, level: str = "midden") -> dict:
    """Aantal keukens en badkamers als het scenario ze niet zelf noemt.

    Eén keuken per woning. Het aantal badkamers volgt de grootte per woning; dat is een aanname
    op wat in dit segment gebruikelijk is en moet per object bevestigd worden."""
    u = max(int(units or 1), 1)
    per_unit = (result_m2 or 0) / u
    if per_unit < 90:
        baths = 1
    elif per_unit < 160:
        baths = 2
    elif per_unit < 260:
        baths = 3
    elif per_unit < 400:
        baths = 4
    else:
        baths = 5
    return {"kitchens": u, "bathrooms": baths * u, "fitout_level": level}


def fitout(sc: Scenario, p: dict) -> dict:
    """Keukens en badkamers. Jan levert die zelf via SKP; ze zitten niet in het €/m²-bouwtarief.

    Badkamers zijn bouwwerk en tellen mee in de PEM (en dus in honoraria en ICIO). Een keuken is
    meubilair en valt daarbuiten, maar telt wel mee voor btw en reserve."""
    hoog = sc.fitout_level == "hoog"
    kitchen_rate = p["kitchen_eur_high"] if hoog else p["kitchen_eur"]
    bath_rate = p.get("bathroom_eur_high", p["bathroom_eur"]) if hoog else p["bathroom_eur"]
    kitchen = sc.kitchens * kitchen_rate
    bath = sc.bathrooms * bath_rate
    # Een aanneemsom bevat al tegelwerk, leidingwerk en een eenvoudige keuken- en badkameruitrusting
    # (N05 §9.2). Zonder die aftrek tel je dat deel twee keer.
    overlap = (sc.renovation_m2 + sc.newbuild_m2) * p.get("fitout_overlap_eur_per_m2", 0)
    overlap = min(overlap, kitchen + bath)      # nooit meer aftrekken dan je erbij telt
    total = kitchen + bath - overlap
    return {"kitchens": sc.kitchens, "bathrooms": sc.bathrooms, "level": sc.fitout_level,
            "kitchen_rate": kitchen_rate, "bathroom_rate": bath_rate,
            "kitchen": kitchen, "bathroom": bath, "overlap": overlap, "total": total,
            "skp_revenue": kitchen + bath, "skp_margin": (kitchen + bath) * p["skp_margin_pct"]}


def construction(sc: Scenario, k: dict, p: dict) -> dict:
    """Bouwkosten exclusief btw, uitgesplitst."""
    rates = k["bouwkosten_eur_per_m2"]
    reno = sc.renovation_m2 * rates["renovatie"]
    new = sc.newbuild_m2 * rates["nieuwbouw"]
    demo = sc.demolition_m2 * p["demolition_eur_per_m2"]
    pool = (p["pool_new_eur"] if sc.pool else 0.0) + (p["pool_renovation_eur"] if sc.pool_renovation else 0.0)
    ext = sc.exterior_m2 * p["exterior_eur_per_m2"]
    fo = fitout(sc, p)
    # de netto-toevoeging verdelen over badkamer (bouwwerk, in de PEM) en keuken (meubilair, erbuiten)
    _bruto = (fo["bathroom"] + fo["kitchen"]) or 1
    _bath_net = fo["total"] * fo["bathroom"] / _bruto
    _kitchen_net = fo["total"] * fo["kitchen"] / _bruto
    pem = reno + new + demo + pool + ext + _bath_net  # presupuesto de ejecución material (benadering)
    fees = pem * (p["architect_pct_of_pem"] + p["aparejador_pct_of_pem"])
    icio = pem * p["icio_pct_of_pem"]
    tasa = pem * p["tasa_licencia_pct_of_pem"]
    other = p["surveys_geotech_eur"] if sc.kind == "nieuwbouw" else p["surveys_renovation_eur"]
    contingency = (pem + fees + _kitchen_net) * p["contingency_pct"]
    subtotal_ex_vat = pem + fees + icio + tasa + other + contingency + _kitchen_net
    # btw: over werk, honoraria en keuken; ICIO/tasa zijn heffingen zonder btw
    if sc.kind == "nieuwbouw":
        vat_rate = p["vat_construction_rate"]
    else:
        vat_rate = sc.renovation_vat_rate if sc.renovation_vat_rate is not None else p["vat_renovation_rate"]
    vat_base = pem + fees + other + contingency + _kitchen_net
    vat = vat_base * vat_rate
    vat_cost = 0.0 if sc.vat_recoverable else vat
    return {
        "renovation": reno, "newbuild": new, "demolition": demo, "pool": pool, "exterior": ext,
        "kitchen": _kitchen_net, "bathroom": _bath_net, "fitout": fo,
        "pem": pem, "fees": fees, "icio": icio, "tasa": tasa, "surveys": other,
        "contingency": contingency, "subtotal_ex_vat": subtotal_ex_vat,
        "vat_rate": vat_rate, "vat": vat, "vat_cost": vat_cost,
        "total": subtotal_ex_vat + vat_cost,
    }


def holding(months: int, p: dict) -> float:
    return months * p["holding_eur_per_month"]


def earthworks(sc: Scenario, p: dict) -> float:
    """Grondwerk en keermuren op een hellend perceel (Jan 25-09-2026).

    Op de hellingen bij Montgó en Balcón al Mar is dit vaak de grootste tegenvaller, en het stond
    tot nu toe nergens in de som. Vlak kost niets; licht hellend en steil krijgen een vast bedrag.
    Is de helling niet vastgesteld, dan rekenen wij niets en zegt het scenario dat erbij."""
    return {"licht": p.get("earthworks_light_eur", 0.0),
            "steil": p.get("earthworks_steep_eur", 0.0)}.get(sc.slope or "", 0.0)


def financing(price: float, aankoopbijkomend: float, bouwkosten: float, sc: Scenario, p: dict,
              rate: float | None = None) -> dict:
    """Rente over een project dat volledig geleend is (Jan 25-09-2026).

    Jan financiert aankoop én bouw voor 100 %. Over de aankoopsom plus de kosten koper loopt rente
    vanaf de dag van levering tot de verkoop. Over de bouwsom loopt rente naar rato van de opgenomen
    tranches; omdat die gelijkmatig oplopen rekenen wij met gemiddeld de helft over de bouwperiode.
    Er zijn geen afsluitkosten en geen boete bij vervroegd aflossen.

    Het percentage is per project te wijzigen: Jan werkt met meerdere investeerders die elk een
    ander tarief rekenen. Zonder opgave geldt het standaardtarief uit de parameters."""
    r = p.get("finance_rate_default", 0.0) if rate is None else float(rate)
    loopt = max(sc.months, 0) / 12
    bouwt = max(sc.build_months if sc.build_months is not None else sc.months, 0) / 12
    op_aankoop = (price + aankoopbijkomend) * r * loopt
    op_bouw = bouwkosten * r * bouwt / 2          # gemiddeld de helft opgenomen
    fee = (price + aankoopbijkomend + bouwkosten) * p.get("finance_fee_pct", 0.0)
    return {"rate": r, "months": sc.months, "build_months": sc.build_months,
            "on_purchase": op_aankoop, "on_build": op_bouw, "fee": fee,
            "total": op_aankoop + op_bouw + fee,
            "per_month": (op_aankoop + op_bouw) / sc.months if sc.months else 0.0}


def selling_costs(sale: float, p: dict, internal: bool = False) -> dict:
    """Verkoopkosten. Jan 17-09-2026: TREE Properties verkoopt het eindproduct zelf, dus de
    courtage verlaat de groep niet. Wat overblijft zijn de echte verkoopkosten: fotografie,
    portalen, advertenties en de tijd van het kantoor."""
    if internal:
        comm = sale * p["internal_selling_cost_pct"]
        saved = sale * p["agent_commission_pct"] * (1 + p["commission_vat_rate"]) - comm
    else:
        comm = sale * p["agent_commission_pct"] * (1 + p["commission_vat_rate"])
        saved = 0.0
    plusv = sale * p["plusvalia_pct_of_sale"]
    misc = p["selling_misc_eur"]
    return {"commission_incl_vat": comm, "plusvalia": plusv, "misc": misc, "total": comm + plusv + misc,
            "channel": "intern" if internal else "extern", "saved_vs_extern": saved}


def project(price: float, sc: Scenario, sale: float, k: dict, p: dict, vat_purchase: bool,
            internal_sale: bool | None = None, finance_rate: float | None = None) -> dict:
    """Volledig projectresultaat bij gegeven koopprijs en verkoopopbrengst (§21)."""
    if internal_sale is None:
        internal_sale = bool(k.get("verkoop_via_eigen_kantoor", False))
    taxes = purchase_taxes(price, p, vat_purchase)
    pc = purchase_costs(price, p)
    con = construction(sc, k, p)
    grond = earthworks(sc, p)
    hold = holding(sc.months, p)
    fin = financing(price, taxes["total"] + pc, con["total"] + grond, sc, p, finance_rate)
    sell = selling_costs(sale, p, internal_sale)
    total_costs = price + taxes["total"] + pc + con["total"] + grond + hold + fin["total"] + sell["total"]
    result = sale - total_costs
    skp = con["fitout"]["skp_margin"]
    return {
        "price": price, "sale": sale, "purchase_taxes": taxes, "purchase_costs": pc,
        "construction": con, "earthworks": grond, "holding": hold, "financing": fin, "selling": sell,
        "total_costs": total_costs, "result": result,
        "margin_on_sale": result / sale if sale else 0.0,
        "roi_on_costs": result / total_costs if total_costs else 0.0,
        # Jan financiert 100 %, dus dit is geen eigen inleg meer maar de piek van de lening.
        "equity_needed": price + taxes["total"] + pc + con["total"] + grond + hold + fin["total"],
        "break_even_sale": total_costs - sell["total"] + selling_costs(total_costs, p, internal_sale)["total"],
        # wat de groep er bovenop verdient: de marge van SKP op keuken en sanitair
        "skp_margin": skp,
        "group_result": result + skp,
        "group_margin_on_sale": (result + skp) / sale if sale else 0.0,
    }


def max_price(sc: Scenario, sale: float, k: dict, p: dict, vat_purchase: bool, roi: float,
              internal_sale: bool | None = None, finance_rate: float | None = None) -> float:
    """Maximale koopprijs waarbij het resultaat precies roi × totale kosten is.
    Iteratief, omdat belastingen en notariskosten van de prijs afhangen (§22)."""
    lo, hi = 0.0, sale
    for _ in range(60):
        mid = (lo + hi) / 2
        r = project(mid, sc, sale, k, p, vat_purchase, internal_sale, finance_rate)
        if r["roi_on_costs"] >= roi:
            lo = mid
        else:
            hi = mid
    return math.floor(lo / 1000) * 1000


def sale_band(comps: dict, key: str, m2: float, units: int = 1) -> dict | None:
    """Verkoopprijs per m² uit de vergelijkingsreeks, zo veel mogelijk uit dezelfde maatklasse.

    Waarom die maatklasse: in dit gebied daalt de prijs per m² sterk met de omvang. Een reeks die
    wordt gedragen door gerenoveerde villa's van 200 m² geeft een veel te hoge prijs voor een huis
    van 380 m². Die fout kostte in de tegenspraak van 18-09-2026 ruim zes ton aan verbeelde
    opbrengst. Zijn er minstens vier vergelijkingsobjecten binnen 0,7 tot 1,4 keer de maat van dit
    object, dan rekenen wij met die groep; anders met de hele reeks en met een waarschuwing erbij.
    """
    c = comps.get(key)
    if not c or not c.get("n"):
        return None
    alle = c.get("examples") or []
    ex = [e for e in alle if e.get("m2") and e.get("eur_m2")]     # bruikbaar voor een eigen mediaan
    ex_m2 = sorted(e["m2"] for e in alle if e.get("m2"))          # alleen de maten, voor de maatcontrole
    unit_m2 = m2 / max(units, 1)
    warnings: list[str] = []
    basis = "hele reeks"

    def kwartielen(waarden: list[float]) -> tuple[float, float, float]:
        s = sorted(waarden)
        n = len(s)
        return s[max(0, int(n * 0.25) - (1 if n % 4 == 0 else 0))], s[n // 2], s[min(n - 1, int(n * 0.75))]

    med, conservative, upside = c["median"], c.get("p25") or c["median"] * 0.9, c.get("p75") or c["median"] * 1.1
    n_used = c["n"]
    # De prijs per m² daalt in dit gebied met de omvang. Onze reeksen zijn te klein om per maatklasse
    # een eigen mediaan te trekken: één uitschieter tilt hem op. Daarom schuiven wij binnen de reeks in
    # plaats van hem opnieuw te berekenen. Groter dan de reeks betekent naar het laagste kwart, kleiner
    # dan de reeks naar het hoogste kwart. Eén richting, geen nieuw getal.
    if unit_m2 and ex_m2:
        mid = ex_m2[len(ex_m2) // 2]
        f = unit_m2 / mid if mid else 1.0
        if f >= 1.20:
            conservative, med, upside = (c.get("p25") or med * 0.9) * 0.9, c.get("p25") or med * 0.9, med
            basis = f"laagste kwart van de reeks: {unit_m2:.0f} m² is {f:.1f} keer de maat van de vergelijkingsobjecten ({mid:.0f} m²)"
            warnings.append(
                f"Dit object is met {unit_m2:.0f} m² flink groter dan de vergelijkingsobjecten (mediaan {mid:.0f} m²). "
                "De prijs per m² daalt hier met de omvang, dus er is met het laagste kwart van de wijkprijzen gerekend. "
                "Dat blijft een schatting: voor deze maatklasse zijn te weinig vergelijkingsobjecten.")
        elif f <= 0.80:
            conservative, med, upside = med, c.get("p75") or med * 1.1, (c.get("p75") or med * 1.1) * 1.1
            basis = f"hoogste kwart van de reeks: {unit_m2:.0f} m² is kleiner dan de vergelijkingsobjecten ({mid:.0f} m²)"
    size = {"examples_m2_min": ex_m2[0] if ex_m2 else None, "examples_m2_max": ex_m2[-1] if ex_m2 else None,
            "examples_m2_median": ex_m2[len(ex_m2) // 2] if ex_m2 else None}
    if c["n"] < 5:
        warnings.append(f"reeks te klein (n={c['n']}): geen betrouwbare mediaan")
    return {
        "n": c["n"], "n_used": n_used, "basis": basis,
        "eur_m2": {"conservative": conservative, "base": med, "upside": upside},
        "sale": {"conservative": conservative * m2, "base": med * m2, "upside": upside * m2},
        "source": c.get("source", ""), "date": c.get("date", ""), "size": size, "warnings": warnings,
        "verification": c.get("verification"),
    }


def sensitivity(price: float, sc: Scenario, sale: float, k: dict, p: dict, vat_purchase: bool) -> dict:
    base = project(price, sc, sale, k, p, vat_purchase)["roi_on_costs"]
    out = {"base": base}
    out["sale_-10pct"] = project(price, sc, sale * 0.9, k, p, vat_purchase)["roi_on_costs"]
    p2 = dict(p); k2 = json.loads(json.dumps(k))
    k2["bouwkosten_eur_per_m2"]["renovatie"] *= 1.15
    k2["bouwkosten_eur_per_m2"]["nieuwbouw"] *= 1.15
    out["build_+15pct"] = project(price, sc, sale, k2, p2, vat_purchase)["roi_on_costs"]
    sc2 = Scenario(**{**asdict(sc), "months": sc.months + 6})
    out["delay_+6m"] = project(price, sc2, sale, k, p, vat_purchase)["roi_on_costs"]
    return out


# ----------------------------------------------------------------------------- run


def evaluate(kader: dict, params: dict, comps_all: dict, kandidaten: list[dict]) -> list[dict]:
    roi = kader["rendementseis_op_projectkosten"]
    results = []
    for c in kandidaten:
        zone_comps = comps_all.get(c["comps_zone"], {})
        entry = {"id": c["id"], "code": c.get("code"), "url": c.get("url"), "zone": c.get("zone"),
                 "comps_zone": c["comps_zone"], "type": c.get("type"), "price_ask": c["price_ask"],
                 "built_m2": c.get("built_m2"), "plot_m2": c.get("plot_m2"), "year": c.get("year"),
                 "claims": c.get("claims", []), "blockers": c.get("blockers", []), "scenarios": []}
        for s in c["scenarios"]:
            sc = Scenario(**{kk: vv for kk, vv in s.items() if kk in Scenario.__dataclass_fields__})
            if ":" in sc.comps_key:
                zkey, skey = sc.comps_key.split(":", 1)
                band = sale_band(comps_all.get(zkey, {}), skey, sc.result_m2, sc.units)
            else:
                band = sale_band(zone_comps, sc.comps_key, sc.result_m2, sc.units)
            if band is not None and sc.unknown_costs:
                band["warnings"] = band["warnings"] + ["kosten niet te ramen: " + ", ".join(sc.unknown_costs)]
            row: dict[str, Any] = {"key": sc.key, "label": sc.label, "kind": sc.kind, "months": sc.months,
                                   "result_m2": sc.result_m2, "comps_key": sc.comps_key,
                                   "vat_recoverable": sc.vat_recoverable, "notes": sc.notes,
                                   "assumptions": sc.assumptions}
            if band is None:
                row["status"] = "GEEN VERGELIJKINGSOBJECTEN"
                entry["scenarios"].append(row)
                continue
            # keuken en badkamers afvullen als het scenario ze niet noemt (zelfde regel als het dashboard)
            if not sc.kitchens and not sc.bathrooms:
                fo = default_fitout(sc.result_m2, sc.units, "hoog" if band["eur_m2"]["base"] >= 5000 else "midden")
                sc.kitchens, sc.bathrooms, sc.fitout_level = fo["kitchens"], fo["bathrooms"], fo["fitout_level"]
            row["fitout"] = {"kitchens": sc.kitchens, "bathrooms": sc.bathrooms, "level": sc.fitout_level}
            vat_purchase = bool(c.get("vat_purchase", False))
            over = sc.months > kader["doorlooptijd_max_maanden"]
            res = {}
            for name, sale in band["sale"].items():
                res[name] = project(c["price_ask"], sc, sale, kader, params, vat_purchase)
            mp = {name: max_price(sc, sale, kader, params, vat_purchase, roi) for name, sale in band["sale"].items()}
            row.update({
                "status": "berekend",
                "sale_band": band,
                "at_asking": {n: {"result": r["result"], "roi_on_costs": r["roi_on_costs"],
                                  "margin_on_sale": r["margin_on_sale"], "total_costs": r["total_costs"],
                                  "equity_needed": r["equity_needed"], "construction_total": r["construction"]["total"],
                                  "purchase_taxes": r["purchase_taxes"]["total"]} for n, r in res.items()},
                "max_price_for_roi": mp,
                "meets_roi_at_asking": {n: r["roi_on_costs"] >= roi for n, r in res.items()},
                "over_max_duration": over,
                "reliable": not band["warnings"],
                "warnings": band["warnings"],
                "within_budget": kader["koopbudget_eur"]["min"] <= c["price_ask"] <= kader["koopbudget_eur"]["max"],
                "sensitivity_at_asking_base": sensitivity(c["price_ask"], sc, band["sale"]["base"], kader, params, vat_purchase),
                "detail_base": res["base"],
            })
            entry["scenarios"].append(row)
        results.append(entry)
    return results


def fmt(x: float) -> str:
    return f"{x:,.0f}".replace(",", ".")


def markdown(results: list[dict], kader: dict) -> str:
    roi = kader["rendementseis_op_projectkosten"]
    lines = [f"| Kandidaat | Scenario | Vraagprijs | Verkoop conservatief / basis | Resultaat basis | ROI basis | Max. koopprijs bij {roi:.0%} (cons. / basis) | Oordeel |",
             "|---|---|---:|---:|---:|---:|---:|---|"]
    for e in results:
        for s in e["scenarios"]:
            if s.get("status") != "berekend":
                lines.append(f"| {e['id']} | {s['label']} | {fmt(e['price_ask'])} | — | — | — | — | {s['status']} |")
                continue
            sb = s["sale_band"]["sale"]; aa = s["at_asking"]; mp = s["max_price_for_roi"]
            verdict = ("haalt eis" if aa["conservative"]["roi_on_costs"] >= roi else
                       "haalt eis alleen in basis" if aa["base"]["roi_on_costs"] >= roi else
                       "onder eis")
            if s["over_max_duration"]:
                verdict += "; te lang"
            if not s.get("reliable", True):
                verdict += "; ONBETROUWBAAR (" + "; ".join(w.split(":")[0].split(";")[0] for w in s["warnings"]) + ")"
            lines.append(f"| {e['id']} | {s['label']} | {fmt(e['price_ask'])} | {fmt(sb['conservative'])} / {fmt(sb['base'])} | "
                         f"{fmt(aa['base']['result'])} | {aa['base']['roi_on_costs']:.0%} | {fmt(mp['conservative'])} / {fmt(mp['base'])} | {verdict} |")
    return "\n".join(lines)


def selftest() -> None:
    k = {"rendementseis_op_projectkosten": 0.25, "doorlooptijd_max_maanden": 24,
         "koopbudget_eur": {"min": 500000, "max": 1000000},
         "bouwkosten_eur_per_m2": {"renovatie": 1000, "nieuwbouw": 2000}}
    p = {"itp_rate": 0.09, "itp_rate_above_threshold": 0.11, "itp_threshold": 1_000_000,
         "vat_purchase_rate": 0.21, "ajd_rate": 0.015, "notary_registry_pct": 0.002,
         "legal_dd_eur": 3000, "technical_dd_eur": 1500, "demolition_eur_per_m2": 60,
         "pool_new_eur": 35000, "pool_renovation_eur": 12000, "exterior_eur_per_m2": 120,
         "architect_pct_of_pem": 0.08, "aparejador_pct_of_pem": 0.03, "icio_pct_of_pem": 0.04,
         "tasa_licencia_pct_of_pem": 0.01, "surveys_geotech_eur": 4000, "surveys_renovation_eur": 1500,
         "contingency_pct": 0.10, "vat_construction_rate": 0.21, "vat_renovation_rate": 0.10,
         "holding_eur_per_month": 250, "agent_commission_pct": 0.04, "commission_vat_rate": 0.21,
         "plusvalia_pct_of_sale": 0.005, "selling_misc_eur": 1500,
         "kitchen_eur": 15000, "kitchen_eur_high": 30000, "bathroom_eur": 9000, "bathroom_eur_high": 18000,
         "skp_margin_pct": 0.30, "internal_selling_cost_pct": 0.015, "fitout_overlap_eur_per_m2": 0}
    # ITP-sprong: 1.000.001 kost meer belasting dan 1.000.000
    assert itp(1_000_000, p) == 90_000 and round(itp(1_000_001, p)) == 110_000
    sc = Scenario(key="R", label="test", kind="renovatie", renovation_m2=200, result_m2=200, months=12)
    con = construction(sc, k, p)
    assert con["pem"] == 200_000 and con["vat_rate"] == 0.10
    r = project(500_000, sc, 1_000_000, k, p, False)
    assert abs(r["result"] - (r["sale"] - r["total_costs"])) < 1e-6
    mp = max_price(sc, 1_000_000, k, p, False, 0.25)
    chk = project(mp, sc, 1_000_000, k, p, False)["roi_on_costs"]
    assert chk >= 0.25 - 0.002, chk
    assert project(mp + 20_000, sc, 1_000_000, k, p, False)["roi_on_costs"] < 0.25
    # nieuwbouw met terugvorderbare btw is goedkoper dan zonder
    n1 = Scenario(key="N", label="n", kind="nieuwbouw", newbuild_m2=300, result_m2=300, vat_recoverable=True)
    n2 = Scenario(**{**asdict(n1), "vat_recoverable": False})
    assert construction(n1, k, p)["total"] < construction(n2, k, p)["total"]
    comps = {"villa_renovated": {"n": 6, "median": 4000, "p25": 3500, "p75": 4500,
                                 "examples": [{"code": "a", "price": 1, "m2": 200}, {"code": "b", "price": 1, "m2": 300}]}}
    b = sale_band(comps, "villa_renovated", 500)
    assert b["warnings"] and "groter" in b["warnings"][0], b["warnings"]
    assert not sale_band(comps, "villa_renovated", 260)["warnings"]            # zelfde maat als de reeks
    assert not sale_band(comps, "villa_renovated", 780, units=3)["warnings"]   # 260 m² per woning
    # maatklasse: vier vergelijkingsobjecten rond de maat van het object wegen zwaarder dan de hele reeks
    groot = {"villa_renovated": {"n": 20, "median": 6000, "p25": 5500, "p75": 6500, "examples": [
        {"m2": 200, "eur_m2": 6100}, {"m2": 210, "eur_m2": 6200}, {"m2": 220, "eur_m2": 6000}, {"m2": 230, "eur_m2": 5900},
        {"m2": 350, "eur_m2": 4000}, {"m2": 360, "eur_m2": 4200}, {"m2": 380, "eur_m2": 4400}, {"m2": 400, "eur_m2": 4600}]}}
    bk = sale_band(groot, "villa_renovated", 500)          # mediaan van de voorbeelden is 350 m²
    assert bk["basis"].startswith("laagste kwart") and bk["eur_m2"]["base"] == 5500, bk["eur_m2"]
    assert bk["warnings"] and "groter" in bk["warnings"][0]
    bk2 = sale_band(groot, "villa_renovated", 170)
    assert bk2["eur_m2"]["base"] == 6500, bk2["eur_m2"]
    assert sale_band(groot, "villa_renovated", 360)["eur_m2"]["base"] == 6000   # zelfde maat: geen verschuiving

    # --- keuken en badkamers (Jan 17-09-2026: los van het €/m²-tarief)
    kaal = Scenario(key="R0", label="zonder", kind="renovatie", renovation_m2=200, result_m2=200, months=12)
    met = Scenario(**{**asdict(kaal), "kitchens": 1, "bathrooms": 3})
    c0, c1 = construction(kaal, k, p), construction(met, k, p)
    assert c1["total"] > c0["total"], "keuken en badkamers moeten de bouwsom verhogen"
    # badkamers horen in de PEM (en dus in honoraria en ICIO), een keuken niet
    assert abs(c1["pem"] - (c0["pem"] + 3 * 9000)) < 1e-6
    assert c1["fees"] > c0["fees"] and c1["icio"] > c0["icio"]
    assert abs(c1["fitout"]["skp_revenue"] - (15000 + 27000)) < 1e-6
    assert abs(c1["fitout"]["skp_margin"] - 0.30 * 42000) < 1e-6
    hoog = Scenario(**{**asdict(met), "fitout_level": "hoog"})
    assert construction(hoog, k, p)["fitout"]["kitchen"] == 30000
    # met overlapaftrek wordt de netto toevoeging kleiner, maar de omzet naar SKP niet
    p_ov = dict(p, fitout_overlap_eur_per_m2=100)
    c_ov = construction(met, k, p_ov)
    assert c_ov["fitout"]["overlap"] == 200 * 100
    assert c_ov["fitout"]["total"] == 42000 - 20000 and c_ov["fitout"]["skp_revenue"] == 42000
    assert c_ov["total"] < construction(met, k, p)["total"]
    fo = default_fitout(300, units=1)
    assert fo["kitchens"] == 1 and fo["bathrooms"] == 4
    fo3 = default_fitout(450, units=3)          # 150 m² per woning → 2 badkamers elk
    assert fo3["kitchens"] == 3 and fo3["bathrooms"] == 6

    # --- verkoop via eigen kantoor
    ext = project(500_000, met, 1_000_000, k, p, False, internal_sale=False)
    intern = project(500_000, met, 1_000_000, k, p, False, internal_sale=True)
    assert intern["result"] > ext["result"], "eigen verkoop moet goedkoper zijn dan een externe makelaar"
    assert intern["selling"]["channel"] == "intern" and ext["selling"]["saved_vs_extern"] == 0
    assert intern["selling"]["saved_vs_extern"] > 0
    mp_ext = max_price(met, 1_000_000, k, p, False, 0.25, internal_sale=False)
    mp_int = max_price(met, 1_000_000, k, p, False, 0.25, internal_sale=True)
    assert mp_int > mp_ext, "eigen verkoop moet de maximale koopprijs verhogen"
    # het kader kan de standaard zetten zonder dat de aanroep hem meegeeft
    k_int = json.loads(json.dumps(k)); k_int["verkoop_via_eigen_kantoor"] = True
    assert project(500_000, met, 1_000_000, k_int, p, False)["selling"]["channel"] == "intern"
    # groepsresultaat telt de marge van SKP erbij op
    assert abs(intern["group_result"] - (intern["result"] + intern["construction"]["fitout"]["skp_margin"])) < 1e-6
    print("selftest OK")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--kader", default=os.path.join(os.path.dirname(__file__), "..", "kader"))
    ap.add_argument("--markdown", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        selftest(); return 0
    d = a.kader
    kader = json.load(open(os.path.join(d, "investeringskader.json"), encoding="utf-8"))
    params = json.load(open(os.path.join(d, "parameters.json"), encoding="utf-8"))["values"]
    comps = json.load(open(os.path.join(d, "comparables.json"), encoding="utf-8"))["zones"]
    kandidaten = json.load(open(os.path.join(d, "kandidaten.json"), encoding="utf-8"))["kandidaten"]
    results = evaluate(kader, params, comps, kandidaten)
    out = os.path.join(d, "haalbaarheid.json")
    json.dump({"kader_versie": kader.get("versie"), "results": results}, open(out, "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    if a.markdown:
        print(markdown(results, kader))
    print(f"geschreven: {out}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())

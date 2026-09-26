"""Haalbaarheid per object, ook met 'wat als'-aanpassingen vanuit het dashboard.

Eén bron van waarheid: de rekenregels in tools/haalbaarheid.py. Dit module kiest per object het
scenario (renovatie, uitbreiding of nieuwbouw), past eventuele schuifwaarden toe en rekent de drie
verkoopscenario's (voorzichtig = p25, basis = mediaan, gunstig = p75 van de wijkreeks) door.
"""
from __future__ import annotations

import copy
import importlib.util
import json
import sys
from functools import lru_cache

from . import config, oppervlakte, zonewaarde
from .prefilter import comps_zone


@lru_cache(maxsize=1)
def bouwregels() -> dict:
    """Bouwregels per wijk uit kader/bouwregels.json (onderzoek N01)."""
    p = config.KADER / "bouwregels.json"
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}


def plotrules(area: str | None, zone: str | None, location: str = "") -> dict:
    """Coëfficiënt, minimale perceelgrootte en plafond voor deze wijk.

    Valt terug op de standaard van 0,20 als de wijk niet is uitgezocht, en zegt dat er dan."""
    br = bouwregels()
    std = dict(br.get("standaard") or {"edificabilidad_neto": 0.20, "parcela_minima_m2": 1000, "max_per_woning_m2": 600})
    zones = br.get("zones") or {}
    z = zones.get(f"{area}:{zone}") or zones.get(zone or "") or zones.get(area or "") or {}
    uit = {**std, **{k: v for k, v in z.items() if v is not None}}
    # de zeven gebieden met de afwijkende coëfficiënt herkennen aan de wijknaam in de advertentie
    loc = (location or "").lower()
    if any(g in loc for g in (br.get("hoge_coefficient_gebieden") or [])):
        uit["edificabilidad_neto"] = 0.28
        uit["hoge_coefficient"] = True
    uit["uitgezocht"] = bool(z) and z.get("edificabilidad_neto") is not None
    uit["let_op"] = z.get("let_op")
    uit["bron"] = br.get("bron")
    return uit


@lru_cache(maxsize=1)
def calc():
    p = config.ROOT / "tools" / "haalbaarheid.py"
    spec = importlib.util.spec_from_file_location("haalbaarheid", p)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["haalbaarheid"] = mod
    spec.loader.exec_module(mod)  # type: ignore[union-attr]
    return mod


def _load(name: str) -> dict:
    return json.loads((config.KADER / name).read_text(encoding="utf-8"))


def inputs() -> tuple[dict, dict, dict, list]:
    kader = _load("investeringskader.json")
    params = _load("parameters.json")["values"]
    comps = _load("comparables.json")["zones"]
    kand = _load("kandidaten.json")["kandidaten"]
    return kader, params, comps, kand


def margin_to_roi(margin: float) -> float:
    return margin / (1 - margin)


def is_rustic(row: dict, category: str, signals: dict | None = None) -> str | None:
    """Geeft de reden terug waarom dit geen bouwkavel is, of None als er wel gebouwd mag worden.

    Twee detectors. De tekst is de eerste: "rústica", "no urbanizable", "polígono X parcela Y".
    De prijs is de tweede: grond waar je een villa op mag zetten kost in dit gebied nooit 12 euro
    per vierkante meter. Grote goedkope percelen zijn landbouwgrond, en daar mag geen woning op."""
    sg = signals or {}
    if category == "perceel-geen-wonen" or sg.get("no_housing_signals"):
        return ("Geen woonbestemming: deze grond is dotacional, equipamiento of terciario. Er mag geen woning op, "
                "dus een villaberekening zegt hier niets.")
    if category == "perceel-rustiek" or sg.get("rustic"):
        return ("Rustieke grond: de advertentie zelf zegt rústico of no urbanizable. Zonder planwijziging "
                "mag hier geen woning worden gebouwd.")
    plot = row.get("plot_m2") or 0
    price = row.get("price") or 0
    if category == "perceel" and plot >= 5000 and price and price / plot < 60:
        return (f"Vermoedelijk rustieke grond: {plot:,.0f} m² voor {price / plot:.0f} €/m². Bouwgrond kost in dit "
                "gebied een veelvoud daarvan. Eerst de planklasse vaststellen, anders is elke bouwsom fantasie."
                ).replace(",", ".")
    return None


ZWAAR = ("reformar integralmente", "renovar integramente", "renovar íntegramente", "reforma integral",
         "integrale renovatie", "complete renovation", "full renovation", "gut renovation",
         "a rehabilitar", "rehabilitacion integral", "rehabilitación integral")


def zware_renovatie(row: dict) -> bool:
    """Zegt de advertentie dat het pand helemaal op de schop moet?"""
    t = (row.get("desc_excerpt") or "").lower() + " " + (row.get("title") or "").lower()
    return any(z in t for z in ZWAAR)


def default_scenarios(row: dict, category: str, zone: str | None, signals: dict | None = None) -> list[dict]:
    """Standaardscenario's voor een BP-advertentie (zelfde logica als de voorfilter)."""
    built = row.get("built_m2") or 0
    plot = row.get("plot_m2") or 0
    out = []
    if is_rustic(row, category, signals):
        return []
    if category == "perceel":
        if plot:
            r = plotrules(row.get("area"), zone, row.get("location_detail") or "")
            coef = r["edificabilidad_neto"]
            pmin = r["parcela_minima_m2"] or 1000
            hoe = f"{coef:.2f} × perceel" + ("" if r["uitgezocht"] else ", standaardaanname want deze wijk is nog niet uitgezocht")
            # Eén villa. Het plafond van 450 m² is geen planregel maar een marktgrens: daarboven
            # vallen de vergelijkingsobjecten weg en is er geen onderbouwde verkoopprijs meer.
            m2 = min(coef * plot, 450)
            out.append(dict(key="N_villa", label=f"Nieuwbouw villa {m2:.0f} m² ({hoe})", kind="nieuwbouw",
                            newbuild_m2=m2, result_m2=m2, pool=True, exterior_m2=150,
                            comps_key="villa_new", **looptijd("nieuwbouw"), vat_recoverable=True))
            # Splitsen mag pas vanaf twee keer de minimale perceelgrootte (TRLOTUP art. 248.c). Dat is
            # een ontwikkelproject: parcelación, wegen, aansluitingen. Die kosten kennen wij niet, dus
            # het scenario staat er wel maar telt niet mee als betrouwbare kans.
            if plot >= 2 * pmin and coef * plot > 500:
                units = min(int(plot // pmin), 4)
                per = min(coef * plot / units, 450)
                out.append(dict(key="N_split", label=f"Splitsen in {units} kavels met {per:.0f} m² per woning ({hoe})",
                                kind="nieuwbouw", newbuild_m2=per * units, result_m2=per * units, units=units,
                                pool=True, exterior_m2=150 * units, comps_key="villa_new",
                                **looptijd("splitsen"), vat_recoverable=True,
                                unknown_costs=["parcelación, wegen, aansluitingen en de doorlooptijd van het splitsen"]))
    else:
        apt = category.startswith("appartement")
        # Een dorpshuis of rijwoning is geen vrijstaande villa; die hebben hun eigen prijs per m².
        rij = (row.get("type") or "").strip().lower() in ("town house", "townhouse", "rijwoning")
        reeks = "apartment_renovated" if apt else ("townhouse_renovated" if rij else "villa_renovated")
        if built:
            # Welke m² staan er in de advertentie? Zie onderzoek N06: soms zit terras, kelder of garage erin.
            b = oppervlakte.bepaal(row.get("desc_excerpt") or "", built, row.get("beds"), (signals or {}).get("catastro_built"))
            woon = b.get("m2_woon") or built
            suffix = "" if b["regime"] == "A" else f", gecorrigeerd van {built:.0f} m² opgave"
            out.append(dict(key="R_integraal", label=f"Integrale renovatie {woon:.0f} m²{suffix}", kind="renovatie",
                            renovation_m2=woon, result_m2=woon, pool_renovation=not apt,
                            comps_key=reeks, **looptijd("renovatie"),
                            notes=oppervlakte.toelichting(b)))
        if not apt and plot and plot >= 800 and built:
            r = plotrules(row.get("area"), zone, row.get("location_detail") or "")
            coef = r["edificabilidad_neto"]
            m2 = min(coef * plot, 450)
            if m2 > built * 1.15:
                hoe = f"{coef:.2f} × perceel" + ("" if r["uitgezocht"] else ", standaardaanname")
                out.append(dict(key="N_sloop", label=f"Sloop en nieuwbouw {m2:.0f} m² ({hoe})", kind="nieuwbouw",
                                demolition_m2=built, newbuild_m2=m2, result_m2=m2, pool=True, exterior_m2=150,
                                comps_key="villa_new", **looptijd("nieuwbouw"), vat_recoverable=True))
    return out


def looptijd(soort: str) -> dict:
    """Vergunning, bouw en verkoop als drie blokken (Jan 25-09-2026).

    Vrijwel elke renovatie binnen de bestaande buitenmuren gaat met een obra menor, en die is er in
    een dag. Uitbreiden, slopen en nieuw bouwen moet via een obra mayor bij een ECUV: 4 tot 6
    maanden, hier gerekend als 5. De bouw doet de eigen ploeg. Verkoop via het eigen kantoor."""
    kader, _, _, _ = inputs()
    d = kader.get("doorlooptijd") or {}
    verg = d.get("vergunning_maanden") or {}
    bouw = d.get("bouw_maanden") or {}
    verkoop = d.get("verkoop_maanden", 3)
    menor = soort == "renovatie"
    return {"permit_months": int(verg.get("obra_menor", 0) if menor else verg.get("obra_mayor_ecuv", 5)),
            "build_months": int(bouw.get(soort, bouw.get("nieuwbouw", 12))),
            "sale_months": int(verkoop)}


def scenarios_for(row: dict) -> tuple[list[dict], str | None, bool]:
    """Geeft (scenario's, wijk, btw bij aankoop) voor een advertentie of Idealista-kandidaat."""
    kader, params, comps, kand = inputs()
    if row["source"] == "idealista":
        k = next((c for c in kand if str(c.get("code")) == str(row["source_ref"])), None)
        if k:
            # De kandidaten uit het onderzoek van september dragen hun eigen vaste doorlooptijd mee.
            # Die komt nu ook uit `looptijd()`, anders staan er in één lijst scenario's van 24 maanden
            # naast identieke scenario's van 20 en zijn de uitkomsten niet vergelijkbaar.
            uit = []
            for sc in k["scenarios"]:
                if sc.get("kind") == "geen":
                    continue
                sc = dict(sc)
                soort = "splitsen" if (sc.get("units") or 1) > 1 else (
                    "renovatie" if sc.get("kind") == "renovatie" else "nieuwbouw")
                sc.pop("months", None)
                sc.update(looptijd(soort))
                uit.append(sc)
            return uit, k["comps_zone"], bool(k.get("vat_purchase"))
        return [], None, False
    pf = json.loads(row.get("prefilter") or "{}")
    sg = json.loads(row.get("signals") or "{}")
    zone = pf.get("zone")
    cat = pf.get("category") or row.get("category") or ""
    return default_scenarios(row, cat, zone, sg), zone, False


def compute(row: dict, overrides: dict | None = None, scenario_key: str | None = None) -> dict:
    m = calc()
    kader, params, comps, _ = inputs()
    ov = overrides or {}
    k = copy.deepcopy(kader)
    p = dict(params)
    margin = float(ov.get("margin", k.get("winstmarge_op_verkoop_min", 0.20)))
    roi = margin_to_roi(margin)
    if "reno_rate" in ov:
        k["bouwkosten_eur_per_m2"]["renovatie"] = float(ov["reno_rate"])
    if "new_rate" in ov:
        k["bouwkosten_eur_per_m2"]["nieuwbouw"] = float(ov["new_rate"])
    if "fees_pct" in ov:
        tot = float(ov["fees_pct"])
        p["architect_pct_of_pem"], p["aparejador_pct_of_pem"] = tot * 0.75, tot * 0.25
    if "commission_pct" in ov:
        p["agent_commission_pct"] = float(ov["commission_pct"])
    if "kitchen_eur" in ov:
        p["kitchen_eur"] = float(ov["kitchen_eur"])
        p["kitchen_eur_high"] = max(float(ov["kitchen_eur"]) * 2, float(ov["kitchen_eur"]))
    if "bathroom_eur" in ov:
        p["bathroom_eur"] = float(ov["bathroom_eur"])
    # Jan werkt met meerdere investeerders die elk een ander tarief rekenen (25-09-2026), dus het
    # rentepercentage is per object te wijzigen. Zonder opgave geldt het tarief uit de parameters.
    finance_rate = float(ov["finance_rate"]) if "finance_rate" in ov else None
    # Helling van het perceel: bepaalt de toeslag voor grondwerk en keermuren.
    slope_ov = str(ov["slope"]) if ov.get("slope") in ("vlak", "licht", "steil") else None
    # Verkoopkanaal: standaard uit het kader (Jan verkoopt via TREE Properties zelf), per object te wijzigen
    intern = bool(k.get("verkoop_via_eigen_kantoor", False))
    if "sale_channel" in ov:
        intern = str(ov["sale_channel"]) == "intern"
    sale_adj = float(ov.get("sale_adj", 0.0))
    price = float(ov.get("price", row.get("price") or 0))

    # Het gemiddelde werkelijk betaalde peil van de kadastrale waardezone waarin dit object ligt.
    # Tweede opinie op onze verkoopwaarde, die op vraagprijzen rust (onderzoek N11).
    zw = zonewaarde.module_voor(row.get("id"))
    scen, zone, vat_purchase = scenarios_for(row)
    if not scen:
        pf = json.loads(row.get("prefilter") or "{}")
        sg = json.loads(row.get("signals") or "{}")
        reden = is_rustic(row, pf.get("category") or row.get("category") or "", sg)
        return {"available": False, "scenarios": [],
                "reason": reden or "geen scenario: oppervlak of categorie onbekend"}
    if not zone:
        return {"available": False, "reason": "wijk onbekend: geen vergelijkingsprijzen", "scenarios": [], "scenario_labels": [s["label"] for s in scen]}
    results = []
    for s in scen:
        sd = dict(s)
        # Urbanisatie niet opgeleverd: de kosten daarvan zijn niet te ramen, dus het scenario is
        # per definitie onbetrouwbaar. Jan koopt hier niet, maar hij wil wel zien wat er staat.
        sg_row = json.loads(row.get("signals") or "{}")
        if sg_row.get("not_urbanised"):
            sd["unknown_costs"] = list(dict.fromkeys((sd.get("unknown_costs") or []) +
                                                     ["urbanisatiekosten en doorlooptijd: urbanisatie niet opgeleverd"]))
        base_m2 = float(sd.get("result_m2") or 0)
        if ov.get("result_m2") and scenario_key is not None and scenario_key == s["key"]:
            target = float(ov["result_m2"])
            if sd["kind"] == "nieuwbouw":
                # nieuwbouw: bouw-m² schaalt één op één met het verkoopbare oppervlak
                f = target / max(base_m2, 1)
                sd["newbuild_m2"] = float(sd.get("newbuild_m2") or 0) * f
                sd["result_m2"] = target
            else:
                # renovatie: het bestaande oppervlak wordt gerenoveerd; alles daarboven is uitbreiding tegen het nieuwbouwtarief
                existing = float(sd.get("renovation_m2") or 0)
                sd["renovation_m2"] = min(target, existing) if existing else 0.0
                sd["newbuild_m2"] = max(target - existing, 0.0)
                sd["result_m2"] = target
        # Helling van het perceel: gemeten bij het hoogtemodel van het IGN en alleen doorgezet als
        # vaststaat dat het perceel het object is (zie dh/enrich_helling.koppel).
        gemeten = json.loads(row.get("signals") or "{}").get("helling")
        if gemeten:
            sd["slope"] = gemeten
        if slope_ov:
            sd["slope"] = slope_ov
        sc = m.Scenario(**{kk: vv for kk, vv in sd.items() if kk in m.Scenario.__dataclass_fields__})
        if ":" in sc.comps_key:
            zk, sk = sc.comps_key.split(":", 1)
            band = m.sale_band(comps.get(zk, {}), sk, sc.result_m2, sc.units)
        else:
            band = m.sale_band(comps.get(zone, {}), sc.comps_key, sc.result_m2, sc.units)
        if not band:
            results.append({"key": sc.key, "label": sc.label, "available": False, "reason": f"geen vergelijkingsreeks {sc.comps_key} in {zone}"})
            continue
        # Keuken en badkamers zitten niet in het €/m²-tarief (Jan 17-09-2026). Noemt het scenario ze
        # niet, dan vullen we ze af uit de grootte per woning; het prijsniveau volgt de wijkprijs.
        if not sc.kitchens and not sc.bathrooms:
            lvl = "hoog" if band["eur_m2"]["base"] >= 5000 else "midden"
            fo = m.default_fitout(sc.result_m2, sc.units, lvl)
            sc.kitchens, sc.bathrooms, sc.fitout_level = fo["kitchens"], fo["bathrooms"], fo["fitout_level"]
        # Onderscheid dat er eerst niet was: een waarschuwing raakt de betrouwbaarheid van de som,
        # een toelichting niet. Zonder dat onderscheid maakte elke nuttige opmerking het hele
        # scenario "onbetrouwbaar", waardoor goede renovaties uit de ranglijst vielen.
        warnings = list(band["warnings"]) + (["kosten niet te ramen: " + ", ".join(sc.unknown_costs)] if sc.unknown_costs else [])
        notities: list[str] = []
        # Onze verkoopwaarde naast wat er in deze zone werkelijk voor woningen is betaald. Ver
        # erboven kan kloppen na een grondige renovatie; extreem erboven betekent dat er iets mis is
        # met de vergelijkingsobjecten, en dat raakt de som zelf. Zie de drempels in dh/zonewaarde.py.
        zw_oordeel = zonewaarde.oordeel(band["eur_m2"]["base"], zw)
        if zw_oordeel:
            (warnings if zw_oordeel[0] == "waarschuwing" else notities).append(zw_oordeel[1])
        # Een integrale renovatie van een oud huis is geen middenrenovatie. Onderzoek N05 zet dat op
        # 1.400 tot 1.800 €/m² tegenover de 1.000 uit het kader. Dat is geen reden om het tarief van Jan
        # stilletjes te veranderen, wel om het als open punt te tonen.
        # De opmerking over onderzoek N05 (1.400–1.800 €/m² voor casco strippen) stond hier tot
        # 26-09-2026. Jan heeft toen bevestigd dat € 1.000/m² zijn eigen kostprijs is, ook bij een
        # volledige renovatie, omdat hij het met eigen vaklieden doet en N05 aannemersprijzen geeft.
        # De waarschuwing is eruit omdat zij alleen twijfel zaaide over een getal dat vaststaat.
        sales = {n: v * (1 + sale_adj) for n, v in band["sale"].items()}
        at = {n: m.project(price, sc, v, k, p, vat_purchase, intern, finance_rate) for n, v in sales.items()}
        mp = {n: m.max_price(sc, v, k, p, vat_purchase, roi, intern, finance_rate) for n, v in sales.items()}
        # Wat het andere verkoopkanaal zou opleveren, zodat het verschil zichtbaar blijft
        other_channel = {n: m.max_price(sc, v, k, p, vat_purchase, roi, not intern, finance_rate)
                         for n, v in sales.items()}
        base = at["base"]
        con = base["construction"]
        fo = con["fitout"]
        breakdown = [
            ("Koopprijs", price), ("Belasting bij aankoop", base["purchase_taxes"]["total"]), ("Notaris, register, due diligence", base["purchase_costs"]),
            ("Bouw en sloop", con["renovation"] + con["newbuild"] + con["demolition"]), ("Zwembad en buitenruimte", con["pool"] + con["exterior"]),
            (f"Keukens ({fo['kitchens']}) en badkamers ({fo['bathrooms']})", fo["total"]),
            ("Honoraria", con["fees"]), ("ICIO en leges", con["icio"] + con["tasa"]), ("Onderzoek en keuring", con["surveys"]),
            ("Reserve", con["contingency"]), ("Niet-terugvorderbare btw", con["vat_cost"]),
            ("Grondwerk en keermuren", base["earthworks"]),
            (f"Rente {base['financing']['rate']*100:.1f} % over {base['financing']['months']} maanden", base["financing"]["total"]),
            ("Vaste lasten", base["holding"]),
            ("Verkoopkosten" + (" (eigen kantoor)" if intern else " (externe makelaar)"), base["selling"]["total"]),
        ]
        acquisition = price + base["purchase_taxes"]["total"] + base["purchase_costs"]
        build = (con["renovation"] + con["newbuild"] + con["demolition"] + con["pool"] + con["exterior"] + fo["total"]
                 + con["fees"] + con["icio"] + con["tasa"] + con["surveys"] + con["contingency"] + con["vat_cost"])
        # Grondwerk hoort bij de bouw, rente bij de overige kosten. Zonder deze twee tellen de drie
        # groepen niet meer op tot de totale kosten, en dan klopt het kaartje in de app niet.
        build = build + base["earthworks"]
        other = base["holding"] + base["selling"]["total"] + base["financing"]["total"]
        results.append({
            "sum": {   # korte rekensom voor de overzichten, alles in het basisscenario
                "acquisition": round(acquisition), "build": round(build), "other": round(other),
                "earthworks": round(base["earthworks"]),
                "financing": round(base["financing"]["total"]),
                "financing_rate": base["financing"]["rate"],
                # Rente is recht evenredig met het percentage, dus dit ene getal maakt elk ander
                # tarief uit het hoofd uit te rekenen (Jan 26-09-2026).
                "financing_per_5pct": round(base["financing"]["total"] / base["financing"]["rate"] * 0.05)
                if base["financing"]["rate"] else 0,
                "financing_per_month": round(base["financing"]["per_month"]),
                "total_costs": round(base["total_costs"]), "sale": round(sales["base"]),
                "result": round(base["result"]), "margin": round(base["margin_on_sale"], 4),
                "roi_on_costs": round(base["roi_on_costs"], 4),
                "eur_m2_sale": round(band["eur_m2"]["base"]), "eur_m2_build": round(build / sc.result_m2) if sc.result_m2 else None,
                "months": sc.months,
                "skp_revenue": round(fo["skp_revenue"]), "skp_margin": round(fo["skp_margin"]),
                "group_result": round(base["group_result"]), "group_margin": round(base["group_margin_on_sale"], 4),
            },
            "key": sc.key, "label": sc.label, "kind": sc.kind, "available": True, "months": sc.months, "result_m2": round(sc.result_m2),
            "base_result_m2": round(base_m2), "renovation_m2": round(sc.renovation_m2), "newbuild_m2": round(sc.newbuild_m2),
            "fitout": {"kitchens": fo["kitchens"], "bathrooms": fo["bathrooms"], "level": fo["level"],
                       "kitchen_rate": round(fo["kitchen_rate"]), "bathroom_rate": round(fo["bathroom_rate"]),
                       "total": round(fo["total"])},
            "channel": {"used": "intern" if intern else "extern",
                        "max_price_other": other_channel,
                        "saved_vs_extern": round(base["selling"]["saved_vs_extern"])},
            "comps": {"zone": zone, "series": sc.comps_key, "n": band["n"], "eur_m2": {kk: round(vv) for kk, vv in band["eur_m2"].items()},
                      "verification": band.get("verification")},
            "zonewaarde": ({"zona_valor": zw["zona_valor"], "cod_zona": zw["cod_zona"],
                            "eur_m2": round(zw["val_tipo_m2"]), "val_tipo": round(zw["val_tipo"]),
                            "ejercicio": zw["ejercicio"],
                            "verhouding": round(band["eur_m2"]["base"] / zw["val_tipo_m2"], 2)}
                           if zw and zw.get("val_tipo_m2") else None),
            "sale": {kk: round(vv) for kk, vv in sales.items()},
            "max_price": mp,
            "margin_at_asking": {kk: round(vv["margin_on_sale"], 4) for kk, vv in at.items()},
            "result_at_asking": {kk: round(vv["result"]) for kk, vv in at.items()},
            "total_costs_base": round(base["total_costs"]),
            "equity_needed": round(base["equity_needed"]),
            "breakdown": [{"label": a, "eur": round(b)} for a, b in breakdown if round(b) != 0],
            "warnings": warnings, "notes": notities, "reliable": not warnings,
            "over_max_duration": sc.months > kader["doorlooptijd_max_maanden"],
        })
    avail = [r for r in results if r.get("available")]
    best = _best_scenario(avail)
    return {"available": bool(avail), "price": price, "margin_required": margin, "zone": zone, "scenarios": results,
            "best_key": best["key"] if best else None,
            "sale_channel": "intern" if intern else "extern",
            "assumptions": {"reno_rate": k["bouwkosten_eur_per_m2"]["renovatie"], "new_rate": k["bouwkosten_eur_per_m2"]["nieuwbouw"],
                            "fees_pct": round(p["architect_pct_of_pem"] + p["aparejador_pct_of_pem"], 4), "commission_pct": p["agent_commission_pct"],
                            "kitchen_eur": p["kitchen_eur"], "bathroom_eur": p["bathroom_eur"],
                            "sale_channel": "intern" if intern else "extern",
                            "sale_adj": sale_adj, "margin": margin}}


def _best_scenario(avail: list[dict]) -> dict | None:
    """Welk scenario tonen we als hét scenario van dit object.

    Betrouwbaar gaat voor onbetrouwbaar, daarna de hoogste maximale koopprijs. Bij een verschil van
    minder dan 5 % wint het kortste project: Jan 17-09-2026, geld eerder terug is meer waard dan een
    paar duizend euro extra op papier."""
    if not avail:
        return None
    ok = [r for r in avail if r.get("reliable")] or avail
    top = max(r["max_price"]["base"] for r in ok)
    near = [r for r in ok if r["max_price"]["base"] >= 0.95 * top] or ok
    return min(near, key=lambda r: (r["months"], -r["max_price"]["base"]))


def classify(price: float | None, best: dict | None) -> str:
    """Kleurklasse voor kaart en lijst."""
    if not price or not best or not best.get("available"):
        return "geen"
    mp = best["max_price"]
    if not best.get("reliable"):
        return "onzeker"
    if price <= mp["conservative"]:
        return "groen"
    if price <= mp["base"]:
        return "blauw"
    if mp["base"] >= 0.70 * price:
        return "oranje"
    return "grijs"

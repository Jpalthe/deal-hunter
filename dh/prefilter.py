"""Voorfilter en indicatieve haalbaarheid per advertentie.

Gebruikt het investeringskader van Jan en, als ze bestaan, de vergelijkingsprijzen per wijk
(kader/comparables.json) en de fiscale parameters (kader/parameters.json) met de geteste
rekenregels uit tools/haalbaarheid.py. Zonder die bestanden blijft het bij budget en categorie.
Uitkomst is een INDICATIE op vraagprijzen van één bron; geen waardering, geen advies.
"""
from __future__ import annotations

import importlib.util
import json
import re
from pathlib import Path

from . import config

_ZONE_WORDS = [
    # `tosal` stond hier zonder grens en ving daardoor óók El Tosalet, dat een eigen wijk met een
    # eigen prijsreeks is (110 objecten kregen zo de prijzen van Montgó–Ermita, 27-09-2026).
    ("montgo_ermita", [r"montg", r"ermita", r"\btosals?\b", r"castellans", r"garroferal", r"carrasquetes", r"jesus pobre"]),
    ("centro", [r"centro", r"casco", r"pueblo", r"old town", r"town centre", r"town center", r"historic", r"dorp"]),
    ("puerto_arenal", [r"puerto", r"\bport\b", r"arenal", r"montañar", r"montanar", r"playa", r"beach", r"primera l[ií]nea", r"frontline", r"grava", r"sant antoni", r"san antonio", r"la corona", r"muntanyar"]),
    ("tosalet_adsubia", [r"tosalet", r"cap mart", r"adsubia", r"cansalades", r"toscamar", r"cala blanca"]),
    ("granadella_balcon", [r"granadella", r"costa nova", r"portichol", r"portitxol", r"balc[oó]n al mar", r"ambolo", r"cap de la nau", r"cabo la nao", r"la guardia"]),
    ("rafalet_pinosol", [r"rafalet", r"pinosol", r"pinomar", r"lluca", r"tarraula", r"golf", r"la plana", r"valls", r"cami cabanes", r"tossals"]),
]


_GENERIC = {r"playa", r"beach", r"primera l[ií]nea", r"frontline", r"centro", r"pueblo", r"old town", r"town centre", r"town center", r"historic", r"dorp", r"golf", r"la plana", r"valls"}


def comps_zone(area: str | None, location_detail: str, text: str = "") -> str | None:
    """Wijk voor de vergelijkingsreeks. Eerst op het locatieveld (alle patronen), daarna op de
    tekst met alleen specifieke urbanisatienamen; generieke woorden (playa, centro) tellen daar niet."""
    if area in ("benitachell", "moraira"):
        return area
    if area != "javea":
        return None
    loc = (location_detail or "").lower()
    for key, pats in _ZONE_WORDS:
        if any(re.search(p, loc) for p in pats):
            return key
    t = (text or "").lower()
    for key, pats in _ZONE_WORDS:
        if any(_echt_de_ligging(p, t) for p in pats if p not in _GENERIC):
            return key
    return None


# Woorden die van een plaatsnaam een uitzicht maken in plaats van een ligging. De Montgó is vanaf
# vrijwel heel Jávea te zien; "vistas al Montgó" zegt niets over waar het object staat. Bij 98 van
# de 850 objecten waarvan de wijk uit de advertentietekst kwam, was dit het geval (27-09-2026).
# Het uitzichtwoord moet vlák voor de plaatsnaam staan, met hoogstens een voorzetsel ertussen.
# Ruimer kijken gaat mis: in "vistas al Montgó en El Arenal" ligt het object wél in het Arenal,
# en een venster van zestig tekens onderdrukte dat ook.
_UITZICHT = re.compile(
    r"(vista|view|blick|uitzicht|panor[aá]mic|overlooking|sicht|mirando|frente)s?\s*"
    r"(?:al|a la|a|sobre|over|to the|to|towards|auf|op|naar|richting|del|de la|de|of the|of|van|sur|su)?\s*"
    r"(?:el|la|los|las|the|den|der|die|das|dem|de|het)?\s*$", re.I)


def _echt_de_ligging(patroon: str, tekst: str) -> bool:
    """Zoekt het patroon, maar slaat treffers over die achter een uitzichtwoord staan."""
    for m in re.finditer(patroon, tekst):
        if not _UITZICHT.search(tekst[max(0, m.start() - 30):m.start()]):
            return True
    return False


def _load_json(p: Path):
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None


def _calc():
    p = config.ROOT / "tools" / "haalbaarheid.py"
    spec = importlib.util.spec_from_file_location("haalbaarheid", p)
    mod = importlib.util.module_from_spec(spec)
    import sys
    sys.modules["haalbaarheid"] = mod   # nodig voor dataclasses met 'from __future__ import annotations'
    spec.loader.exec_module(mod)  # type: ignore[union-attr]
    return mod


class Prefilter:
    def __init__(self):
        self.kader = _load_json(config.KADER / "investeringskader.json") or {}
        params = _load_json(config.KADER / "parameters.json")
        comps = _load_json(config.KADER / "comparables.json")
        self.params = params.get("values") if params else None
        self.comps = comps.get("zones") if comps else None
        self.calc = _calc() if (self.params and self.comps) else None
        b = self.kader.get("koopbudget_eur", {})
        self.bmin, self.bmax = b.get("min", config.BUDGET_MIN), b.get("max", config.BUDGET_MAX)
        self.roi = self.kader.get("rendementseis_op_projectkosten", 0.25)

    def run(self, rec: dict, sig: dict) -> dict:
        price = rec.get("price") or 0
        cat = sig["category"]
        out: dict = {"category": cat, "zone": comps_zone(rec.get("area"), rec.get("location_detail", ""), (rec.get("_text") or rec.get("desc_excerpt") or "")[:400]),
                     "within_budget": None, "verdict": "buiten kader", "reasons": [], "indicative": None}
        if rec.get("area") is None:
            out["reasons"].append("buiten werkgebied")
            return out
        if cat == "perceel":
            out["within_budget"] = config.PLOT_BUDGET_MIN <= price <= self.bmax
        else:
            out["within_budget"] = self.bmin <= price <= self.bmax
        if not out["within_budget"]:
            out["reasons"].append(f"prijs {price:,.0f} buiten budget".replace(",", "."))
        if cat == "perceel-rustiek":
            out["reasons"].append("rustieke grond: geen bouwrecht voor een woning zonder planwijziging")
        interesting = cat in ("renovatie", "perceel", "appartement-renovatie", "bijzonder")
        if not interesting:
            out["reasons"].append(f"categorie {cat}: geen renovatie- of perceelsignaal")
        if out["within_budget"] and interesting:
            out["verdict"] = "kandidaat"
        elif interesting and price and price <= self.bmax * 1.2:
            out["verdict"] = "watchlist"
        # indicatieve haalbaarheid
        if self.calc and out["zone"] and price and interesting:
            out["indicative"] = self._indicative(rec, cat, out["zone"], price)
            ind = out["indicative"]
            if ind and ind.get("warnings") and out["verdict"] == "kandidaat":
                out["verdict"] = "kandidaat: niet betrouwbaar te rekenen (indicatief)"
                out["reasons"].extend(ind["warnings"])
            elif ind and ind.get("roi_base") is not None and out["verdict"] == "kandidaat":
                if ind["roi_conservative"] is not None and ind["roi_conservative"] >= self.roi:
                    out["verdict"] = "kandidaat: haalt eis (indicatief)"
                elif ind["roi_base"] >= self.roi:
                    out["verdict"] = "kandidaat: haalt eis in basis (indicatief)"
                else:
                    out["verdict"] = "kandidaat: onder eis bij vraagprijs (indicatief)"
        return out

    def _indicative(self, rec: dict, cat: str, zone: str, price: float) -> dict | None:
        m = self.calc
        built, plot = rec.get("built_m2") or 0, rec.get("plot_m2") or 0
        zc = self.comps.get(zone) or {}
        if cat == "perceel":
            if not plot:
                return {"note": "perceeloppervlak onbekend"}
            if plot >= 5000 and price and price / plot < 60:
                return {"note": f"vermoedelijk rustieke grond: {plot:,.0f} m² voor {price / plot:.0f} €/m²; planklasse eerst vaststellen".replace(",", ".")}
            m2 = min(0.20 * plot, 450)   # aanname zona E netto; markeren
            sc = m.Scenario(key="N", label="nieuwbouw (0,20 × perceel, aanname)", kind="nieuwbouw", newbuild_m2=m2, result_m2=m2,
                            pool=True, exterior_m2=150, comps_key="villa_new", months=24, vat_recoverable=True)
            vat_purchase = False
        else:
            if not built:
                return {"note": "gebouwd oppervlak onbekend"}
            key = "apartment_renovated" if cat.startswith("appartement") else "villa_renovated"
            sc = m.Scenario(key="R", label="integrale renovatie", kind="renovatie", renovation_m2=built, result_m2=built,
                            pool_renovation=not cat.startswith("appartement"), comps_key=key, months=15)
            vat_purchase = False
        band = m.sale_band(zc, sc.comps_key, sc.result_m2)
        if not band:
            return {"note": f"geen vergelijkingsreeks {sc.comps_key} voor {zone}"}
        r_base = m.project(price, sc, band["sale"]["base"], self.kader, self.params, vat_purchase)
        r_cons = m.project(price, sc, band["sale"]["conservative"], self.kader, self.params, vat_purchase)
        r_up = m.project(price, sc, band["sale"]["upside"], self.kader, self.params, vat_purchase)
        mp = m.max_price(sc, band["sale"]["conservative"], self.kader, self.params, vat_purchase, self.roi)
        mp_b = m.max_price(sc, band["sale"]["base"], self.kader, self.params, vat_purchase, self.roi)
        mp_u = m.max_price(sc, band["sale"]["upside"], self.kader, self.params, vat_purchase, self.roi)
        return {
            "max_price": {"conservative": mp, "base": mp_b, "upside": mp_u},
            "margin_on_sale": {"conservative": round(r_cons["margin_on_sale"], 3), "base": round(r_base["margin_on_sale"], 3), "upside": round(r_up["margin_on_sale"], 3)},
            "sale_upside": round(band["sale"]["upside"]), "warnings": band.get("warnings", []),
            "scenario": sc.label, "result_m2": sc.result_m2, "comps_key": sc.comps_key, "comps_n": band["n"],
            "sale_conservative": round(band["sale"]["conservative"]), "sale_base": round(band["sale"]["base"]),
            "result_base": round(r_base["result"]), "roi_base": round(r_base["roi_on_costs"], 3),
            "roi_conservative": round(r_cons["roi_on_costs"], 3), "max_price_25_conservative": mp,
            "label": "vraagprijzen, geen transacties; aannames zoals in tools/haalbaarheid.py",
        }

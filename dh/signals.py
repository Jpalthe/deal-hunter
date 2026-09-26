"""Signaalherkenning in advertentietekst (masterprompt §13). Regels, geen AI.

Een signaal is geen bewijs. Negatieve vormen ("reforma integral realizada") worden herkend en
tellen niet mee als renovatiesignaal. Meertalig: ES, EN, NL, DE, FR.
"""
from __future__ import annotations

import re
import unicodedata

RENOVATION = [
    # Spaans
    r"para reformar", r"a reformar", r"necesita (una )?reforma", r"reforma integral(?! realizada| hecha| terminada| completa realizada)",
    r"de origen", r"para actualizar", r"a actualizar", r"para renovar", r"a renovar", r"obra inacabada", r"sin terminar",
    r"gran potencial", r"mucho potencial", r"para modernizar", r"necesita actualizaci[oó]n", r"para restaurar", r"en estado original",
    # Engels
    r"to renovate", r"to be renovated", r"in need of (renovation|modernisation|modernization|updating|refurbishment)",
    r"needs (renovation|modernising|modernizing|updating|work|refurbishment|tlc)", r"renovation project", r"requires (renovation|modernisation|updating|work)",
    r"unfinished", r"original (state|condition)", r"fixer.?upper", r"some (attention|updating|tlc)", r"ready (for|to) (renovation|renovate)", r"potential to",
    # Nederlands
    r"opknapp", r"te renoveren", r"renovatie ?(nodig|behoevend)", r"moderniseren", r"op te knappen", r"originele staat", r"veel potentie",
    # Duits
    r"renovierungsbed[uü]rftig", r"sanierungsbed[uü]rftig", r"zu renovieren", r"modernisierungsbed[uü]rftig", r"originalzustand",
    # Frans
    r"[aà] r[eé]nover", r"[aà] rafra[iî]chir", r"travaux [aà] pr[eé]voir", r"[eé]tat d'origine",
]
NEGATIVE = [
    r"reforma integral (realizada|hecha|terminada|completa)", r"totalmente reformad", r"completamente reformad", r"recién reformad", r"reformad[oa] en 20\d\d",
    r"fully (renovated|refurbished|reformed)", r"completely (renovated|refurbished)", r"newly (renovated|refurbished|built)", r"brand new",
    r"a estrenar", r"obra nueva", r"nueva construcci[oó]n", r"new build", r"nieuwbouw", r"neubau", r"neuf", r"volledig gerenoveerd", r"kernsaniert",
]
PLOT = [r"\bparcela\b", r"\bsolar\b", r"\bterreno\b", r"\bplot\b", r"\bbouwkavel\b", r"\bgrundst[uü]ck\b", r"\bterrain\b", r"\bland\b"]
LICENCE = [r"licencia (de obra|de obras|de construcci[oó]n|concedida|vigente|en vigor|aprobada)", r"con licencia", r"building (licen[cs]e|permit)", r"bouwvergunning", r"baugenehmigung", r"permis de construire", r"proyecto (aprobado|incluido|b[aá]sico|de ejecuci[oó]n)"]
EXTENSION = [r"edificabilidad", r"ampliar", r"ampliaci[oó]n", r"m2 m[aá]s", r"extend", r"extension", r"uitbreid", r"erweitern", r"agrandir", r"posibilidad de construir"]
# Grond waarop je zonder planwijziging geen woning mag bouwen. Dit is de duurste val in de hele
# lijst: een goedkope "parcela" van 10.000 m² is meestal rustieke grond, geen bouwkavel.
RUSTIC = [
    r"r[uú]stic[oa]", r"suelo no urbanizable", r"\bsnu\b", r"no urbanizable", r"finca r[uú]stica",
    r"terreno r[uú]stico", r"parcela r[uú]stica", r"uso agr[ií]cola", r"suelo agrario", r"pol[ií]gono \d+ parcela \d+",
    r"rural land", r"agricultural (land|plot|use)", r"landbouwgrond", r"agrarisch",
]
# Tekst die juist zegt dat er wél mag worden gebouwd. Let op: "urbanizable" hoort hier NIET;
# dat betekent dat de grond stedelijk kan wórden, niet dat het al zo is.
URBAN = [
    r"suelo urbano(?! no consolidado)", r"parcela urbana", r"solar urbano", r"urbanizado", r"edificable",
    r"building (plot|land)", r"bouwkavel", r"bouwgrond", r"con licencia", r"edificabilidad",
]
# Grond zonder woonbestemming: hier komt geen woning, hoe goedkoop hij ook is.
NO_HOUSING = [
    r"dotacional", r"equipamiento(s)? (p[uú]blico|comunitario|deportivo|educativo|sanitario)?",
    r"\bterciario\b", r"comercial concentrado", r"calificad[oa] para (uso )?(terciario|comercial|industrial)",
    r"uso (exclusivo )?(terciario|comercial|industrial|hotelero)", r"suelo industrial", r"zona verde",
    r"ideal para (supermercado|restaurante|empresas de servicios)", r"local comercial en suelo",
]
# Urbanisatie nog niet afgerond of nog niet overgedragen aan de gemeente. Dit is de enige harde
# uitsluiting van Jan: hier koopt hij niet, want de kosten en de termijn liggen bij de koper.
NOT_URBANISED = [
    r"no consolidado", r"urbanizable", r"sin urbanizar", r"pendiente de urbaniz", r"falta(n)? (la )?urbanizaci[oó]n",
    r"unidad de ejecuci[oó]n", r"\bUE-?\s?\d", r"reparcelaci[oó]n", r"plan parcial", r"\bPAI\b",
    r"programa de actuaci[oó]n", r"aval bancario", r"garant[ií]a bancaria", r"bankgarantie",
    r"cuotas de urbanizaci[oó]n", r"gastos de urbanizaci[oó]n", r"urbanizaci[oó]n no recepcionada",
    # Duits en Engels: makelaarssites in Jávea publiceren vaak in vier talen
    r"zu urbanisieren", r"noch zu erschlie[sß]en", r"nicht erschlossen", r"erschlie[sß]ungskosten",
    r"to be urbani[sz]ed", r"not yet urbani[sz]ed", r"pending urbani[sz]ation", r"urbani[sz]ation costs",
    r"nog te verkavelen", r"niet bouwrijp",
]

# Een traspaso is de overname van een lopend bedrijf, geen koop van vastgoed. Die advertenties staan
# tussen de woningen met een prijs van een paar honderd euro en kwamen zo boven aan de lijst als
# fantastische koopjes. Het gaat om de goodwill en de inventaris, niet om de stenen.
GEEN_KOOP = [
    r"\btraspaso\b", r"se traspasa", r"en traspaso", r"traspaso de (negocio|restaurante|local|bar)",
    r"business transfer", r"lease(hold)? transfer", r"overname van (een )?(zaak|bedrijf|horeca)",
    r"fondo de comercio", r"\balquiler de local\b",
]
SPECIAL = [r"\bsubasta\b", r"\bbanco\b", r"\bde banco\b", r"\bbank repossession\b", r"\bliquidaci[oó]n\b", r"\bherencia\b", r"\bproindiviso\b", r"\bnuda propiedad\b", r"\bokupa", r"\bocupad", r"sociedad limitada", r"\bs\.l\.", r"paralizad", r"stalled", r"unfinished development"]


def _norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s or "")
    return s.lower()


def _find(patterns: list[str], text: str) -> list[str]:
    hits = []
    for p in patterns:
        m = re.search(p, text, re.I)
        if m:
            hits.append(m.group(0).strip())
    return hits


def analyse(text: str, features: str = "", type_: str = "", new_build: bool = False) -> dict:
    t = _norm(f"{text} {features}")
    neg = _find(NEGATIVE, t)
    reno = _find(RENOVATION, t)
    plot = _find(PLOT, t)
    lic = _find(LICENCE, t)
    ext = _find(EXTENSION, t)
    spec = _find(SPECIAL, t)
    rust = _find(RUSTIC, t)
    urb = _find(URBAN, t)
    geen_wonen = _find(NO_HOUSING, t)
    niet_geurbaniseerd = _find(NOT_URBANISED, t)
    geen_koop = _find(GEEN_KOOP, t)
    # Harde uitsluiting van Jan (26-09-2026): appartement boven de tweede zonder lift.
    from .verkoopbaarheid import appartement_zonder_lift_hoog
    zonder_lift = appartement_zonder_lift_hoog(text or "")
    typ = (type_ or "").lower()
    is_land = typ in ("land", "plot", "terreno", "parcela", "solar") or (typ == "" and bool(plot) and not reno)
    is_apartment = typ in ("apartment", "piso", "flat", "penthouse", "atico", "ático")
    renovation_score = len(reno) - (1 if neg else 0)
    if new_build or (neg and not reno):
        renovation_score = 0
    # Rustieke grond blijft "perceel", maar zonder bouwrecht; dat onderscheid moet zichtbaar zijn.
    rustic = bool(rust) and not (urb and len(urb) > len(rust))
    # Een bedrijfsovername is geen vastgoedkoop. Die advertentie krijgt een eigen categorie, en die
    # staat niet in de focus, dus hij verdwijnt uit de lijst in plaats van bovenaan te komen met een
    # prijs van een paar honderd euro.
    if geen_koop:
        category = "geen-koop"
    elif is_land and geen_wonen:
        category = "perceel-geen-wonen"
    elif is_land:
        category = "perceel-rustiek" if rustic else "perceel"
    elif spec and any(re.search(p, t) for p in (r"subasta", r"banco", r"liquidaci", r"paralizad", r"unfinished development", r"okupa", r"ocupad", r"proindiviso", r"nuda propiedad")):
        category = "bijzonder"
    elif renovation_score > 0 and is_apartment:
        category = "appartement-renovatie"
    elif renovation_score > 0:
        category = "renovatie"
    elif is_apartment:
        category = "appartement"
    else:
        category = "overig"
    return {
        "category": category,
        "renovation_signals": reno,
        "negative_signals": neg,
        "renovation_score": max(renovation_score, 0),
        "plot_signals": plot,
        "licence_claims": lic,
        "extension_claims": ext,
        "special_signals": spec,
        "rustic_signals": rust,
        "urban_signals": urb,
        "rustic": rustic,
        "no_housing_signals": geen_wonen,
        "not_urbanised_signals": niet_geurbaniseerd,
        "geen_koop_signals": geen_koop,
        "zonder_lift_hoog": zonder_lift,
        "geen_koop": bool(geen_koop),
        "not_urbanised": bool(niet_geurbaniseerd),
        "blockers": (
            (["Rustieke grond (suelo rústico of no urbanizable): een woning bouwen mag hier niet zonder "
              "planwijziging. Wat er wél mag staat in het informe urbanístico van de gemeente."] if rustic else [])
            + ([f"Geen woonbestemming: de tekst noemt {', '.join(geen_wonen[:2])}. Op deze grond mag geen woning komen, "
                "alleen onderwijs, sport, zorg, publieke dienst of parkeren."] if geen_wonen else [])
            + ([f"Urbanisatie niet opgeleverd: de tekst noemt {', '.join(niet_geurbaniseerd[:3])}. Dit is de harde "
                "uitsluiting van Jan. De urbanisatiekosten en de termijn liggen bij de koper en zijn niet te ramen "
                "zolang het programma niet is vastgesteld."] if niet_geurbaniseerd else [])
        ),
    }

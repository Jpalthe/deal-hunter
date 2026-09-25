"""Is dit een pand om te renoveren? Vier kenmerken, door Jan zelf benoemd (25-09-2026).

  1. oud en niet aangepakt      bouwjaar uit het kadaster vóór 1995, geen claim van een verbouwing
  2. prijs onder de wijkprijs   vraagprijs per m² onder het laagste kwart van de wijkreeks
  3. de tekst zegt het zelf     "para reformar", "te renoveren", "needs updating"
  4. groot perceel, klein huis  veel grond, weinig gebouwd: ruimte om bij te bouwen of te vervangen

Eén kenmerk is genoeg om in beeld te komen; meer kenmerken is een sterker vermoeden. Dit is een
vermoeden op grond van de advertentie en het kadaster, geen bouwkundige opname. Wat er werkelijk
moet gebeuren blijkt pas bij een bezichtiging.
"""
from __future__ import annotations

import re

BOUWJAAR_GRENS = 1995
PERCEEL_MIN_M2 = 600
BEBOUWINGSDEEL_MAX = 0.20     # gebouwd ten opzichte van perceel
# Let op de Spaanse uitgangen: "reformada" en "reformado" komen allebei voor, net als "renovada".
VERBOUWD = re.compile(r"(gerenoveerd|gerenoveerde|recent(ly)? renovated|fully renovated|newly renovated|"
                      r"reformad[oa]s?|renovad[oa]s?|kernsaniert|neuwertig|"
                      r"obra nueva|nieuwbouw|new build|brand new)", re.I)


def _eur_m2(item: dict) -> float | None:
    p, b = item.get("price"), item.get("built_m2")
    return round(p / b) if p and b else None


def _wijkgrens(comps: dict, zone: str | None, typologie: str) -> int | None:
    """Het laagste kwart van de gerenoveerde reeks in deze wijk, in €/m²."""
    z = (comps or {}).get(zone or "")
    if not isinstance(z, dict):
        return None
    voorkeur = [f"{typologie}_renovated", "villa_renovated", "townhouse_renovated", "apartment_renovated"]
    for k in voorkeur:
        r = z.get(k)
        if isinstance(r, dict) and r.get("p25"):
            return int(r["p25"])
    return None


def beoordeel(item: dict, parcel: dict | None, sig: dict | None, comps: dict | None,
              tekst: str = "") -> dict:
    """Geeft punten (0–4), de redenen in gewone taal, en of het object renovatiewaardig oogt.

    `tekst` is de advertentietekst (titel plus omschrijving); de aanroeper geeft die mee, want de
    samenvatting draagt de omschrijving zelf niet."""
    sig = sig or {}
    redenen: list[str] = []
    tekst = " ".join(x for x in (tekst, str(item.get("title") or ""), str(item.get("location") or "")) if x)

    # 1 — oud en niet aangepakt
    jaar = (parcel or {}).get("year")
    verbouwd = bool(VERBOUWD.search(tekst))
    if jaar and int(jaar) < BOUWJAAR_GRENS and not verbouwd:
        redenen.append(f"Gebouwd in {int(jaar)} en geen teken van een verbouwing")

    # 2 — prijs onder de wijkprijs
    em2 = _eur_m2(item)
    grens = _wijkgrens(comps or {}, item.get("zone"), (item.get("type") or "villa").lower())
    if em2 and grens and em2 < grens:
        redenen.append(f"€ {em2:,}/m² tegenover € {grens:,}/m² in de wijk".replace(",", "."))

    # 3 — de tekst zegt het zelf
    rs = [s for s in (sig.get("renovation_signals") or []) if s]
    if rs:
        redenen.append(f"De advertentie zegt het zelf: {rs[0]}")

    # 4 — groot perceel, klein huis
    plot, built = item.get("plot_m2"), item.get("built_m2")
    if plot and built and plot >= PERCEEL_MIN_M2 and built / plot <= BEBOUWINGSDEEL_MAX:
        redenen.append(f"{int(built)} m² gebouwd op {int(plot)} m² grond: ruimte over")

    return {"punten": len(redenen), "redenen": redenen, "waardig": bool(redenen),
            "verbouwd_geclaimd": verbouwd}

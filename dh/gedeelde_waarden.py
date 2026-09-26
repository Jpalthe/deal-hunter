"""Streept waarden weg die een hele bron domineren, want die komen uit een keuzelijst.

Op 27-09-2026 bleek dat de prijs- en oppervlaktefilters bovenaan een makelaarssite als paginatekst
meetelden. 293 van de 320 objecten van één site stonden op € 50.000 terwijl de woning € 690.000
kostte; 138 van een andere site hadden 50 m² bebouwd. Dat is aan de lezerskant hersteld
(`makelaars._tekst` slaat <select>, <option> en <datalist> over), maar een site die morgen zijn
filter anders bouwt, kan hetzelfde opnieuw veroorzaken. Dit is het vangnet daaronder.

Het onderscheid met een prijs die toevallig vaker voorkomt is het **aandeel van de bron**. Bij een
portaalbron haalt de vaakste prijs een paar procent — Idealista had 19 woningen van € 750.000 op
ruim achthonderd. Bij een keuzelijstwaarde was het 70 tot 92 procent. Alle gevallen van die nacht
lagen boven de 20 %; de drempel staat op 15 % en minstens negen objecten.

Besluit Jan, 27-09-2026: automatisch wegstrepen en in het ochtendbericht melden. Het veld gaat op
onbekend, niet op een geraden waarde — en de weggestreepte waarde blijft in de gebeurtenis staan,
zodat altijd terug te vinden is wat er stond. `tools/herlezen-getallen.py --gedeeld` haalt de
pagina's opnieuw op en zet de echte waarde terug.
"""
from __future__ import annotations

from .store import Store

VELDEN = ("price", "built_m2", "plot_m2")
MIN_AANTAL = 9
MIN_AANDEEL = 0.15
# Bronnen die geen pagina's zijn maar velden leveren. Daar is een herhaalde waarde geen
# leesfout maar een feit, dus die slaan wij over.
NIET_CONTROLEREN = ("bp",)


def vind(store: Store) -> list[dict]:
    """Waarden die een te groot deel van één bron beslaan om een echte waarde te kunnen zijn."""
    uit = []
    for veld in VELDEN:
        for r in store.con.execute(f"""
            WITH v AS (SELECT source, {veld} AS w, count(*) AS n FROM listings
                       WHERE gone_at IS NULL AND {veld} IS NOT NULL GROUP BY 1, 2),
                 t AS (SELECT source, count(*) AS tot FROM listings
                       WHERE gone_at IS NULL AND {veld} IS NOT NULL GROUP BY 1)
            SELECT v.source, v.w, v.n, t.tot FROM v JOIN t ON t.source = v.source
            WHERE v.n >= ? AND v.n * 1.0 / t.tot >= ?
            ORDER BY v.n DESC""", (MIN_AANTAL, MIN_AANDEEL)):
            if r["source"] in NIET_CONTROLEREN:
                continue
            uit.append({"source": r["source"], "veld": veld, "waarde": r["w"],
                        "aantal": r["n"], "totaal": r["tot"],
                        "aandeel": round(r["n"] / r["tot"], 3)})
    # Twijfelgevallen aanmerken. Een perceel van precies 1.000 m² is in Jávea doodgewoon, dus een
    # bron waar één veld net boven de drempel uitkomt en verder niets opvalt, kán gelijk hebben.
    # Die waarde gaat er wél uit (besluit Jan 27-09-2026), maar met een aantekening — en het object
    # blijft zichtbaar onder "onvolledig", dus er raakt niets zoek.
    velden_per_bron: dict[str, int] = {}
    for g in uit:
        velden_per_bron[g["source"]] = velden_per_bron.get(g["source"], 0) + 1
    for g in uit:
        g["twijfel"] = g["aandeel"] < 0.25 and velden_per_bron[g["source"]] == 1
    return uit


def zin(g: dict) -> str:
    """Eén regel voor het ochtendbericht."""
    bron = g["source"].split(":", 1)[-1]
    naam = {"price": "vraagprijs", "built_m2": "bebouwd oppervlak", "plot_m2": "perceel"}[g["veld"]]
    waarde = (f"€ {g['waarde']:,.0f}" if g["veld"] == "price" else f"{g['waarde']:,.0f} m²").replace(",", ".")
    staart = ("— weggestreept, maar dit kán een echte waarde zijn: kijk na"
              if g.get("twijfel") else "— weggestreept, dat komt uit een keuzelijst")
    return (f"{bron}: {naam} {waarde} stond bij {g['aantal']} van de {g['totaal']} objecten "
            f"({g['aandeel'] * 100:.0f} %) {staart}")


def opruimen(store: Store, run_id: int | None = None, doen: bool = True) -> dict:
    """Zet de gevonden waarden op onbekend en legt per waarde één gebeurtenis vast."""
    gevonden = vind(store)
    geraakt = 0
    for g in gevonden:
        rijen = [r["id"] for r in store.con.execute(
            f"SELECT id FROM listings WHERE gone_at IS NULL AND source = ? AND {g['veld']} = ?",
            (g["source"], g["waarde"]))]
        g["listing_ids"] = rijen[:50]          # genoeg om terug te vinden, niet de hele lijst in het log
        geraakt += len(rijen)
        if not doen:
            continue
        store.con.execute(
            f"UPDATE listings SET {g['veld']} = NULL WHERE gone_at IS NULL AND source = ? AND {g['veld']} = ?",
            (g["source"], g["waarde"]))
        store.add_event(run_id, "WAARDE WEGGESTREEPT", details={
            "bron": g["source"], "veld": g["veld"], "weggestreepte_waarde": g["waarde"],
            "objecten": len(rijen), "van_totaal": g["totaal"], "aandeel": g["aandeel"],
            "reden": "waarde domineert de bron en komt vrijwel zeker uit een keuzelijst",
            "herstel": "tools/herlezen-getallen.py --gedeeld leest die pagina's opnieuw"})
    if doen:
        store.con.commit()
    return {"waarden": gevonden, "objecten_geraakt": geraakt,
            "regels": [zin(g) for g in gevonden]}

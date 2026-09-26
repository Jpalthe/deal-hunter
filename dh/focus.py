"""Waar de dealmaker naar kijkt, en op welk tabblad het terechtkomt.

Jan, 25-09-2026: Jávea is de hoofdlijst; panden om te renoveren, percelen om op te bouwen en
woningen die groot genoeg zijn om te slopen en opnieuw op te bouwen. Benitachell en Moraira worden
gelezen en doorgerekend, maar staan apart. Geen bovengrens meer aan de prijs; wel een ondergrens.
Appartementen doen mee met een eigen merkje.

Drie tabbladen:

  kansen   Jávea, binnen de grenzen, bestemming stedelijk of nog niet opgevraagd
  later    Jávea, maar de officiële bestemming is vastgesteld en niet stedelijk
  buiten   Benitachell en Moraira

Over "streng op bestemming": een niet-gestelde vraag is geen afwijzing. Alleen een vastgestelde
niet-stedelijke bestemming verhuist een object naar `later`. Staat de bestemming op ONBEKEND — bij
255 van de 512 objecten, omdat makelaarssites geen coördinaten meegeven en er dus geen kadastrale
referentie ligt — dan blijft het object in de hoofdlijst, met die onzekerheid erbij vermeld.

Eén plek, zodat de telefoon, de meldingen, het dagrapport en de dossiers hetzelfde bedoelen.
"""
from __future__ import annotations

import json
from functools import lru_cache

from . import config

KANSEN, LATER, BUITEN, TE_DUUR = "kansen", "later", "buiten", "teduur"

STANDAARD = {
    "gebieden": ["javea"],
    "gebieden_apart": ["benitachell", "moraira"],
    "categorieen": ["renovatie", "appartement-renovatie", "perceel", "bijzonder"],
    "sloop_nieuwbouw_telt_mee": True,
    "ondergrens_perceel": 100000,
    "ondergrens_pand": 500000,
    "bovengrens": None,
    "bestemming_streng": True,
    "later_alleen_urbaniseerbaar": True,
    "opknapper_vermoeden": {"aan": True, "bouwjaar_voor": 1995, "korting_op_wijkprijs_min": 0.40},
    "dubbel_samenvoegen": True,
}


@lru_cache(maxsize=1)
def instelling() -> dict:
    try:
        d = json.loads((config.KADER / "investeringskader.json").read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return dict(STANDAARD)
    return {**STANDAARD, **(d.get("focus") or {})}


def is_perceel(cat: str | None) -> bool:
    return (cat or "").lower().startswith("perceel")


def binnen_prijs(item: dict, f: dict | None = None) -> bool:
    """Prijsgrenzen. Een object zonder prijs valt nooit af: dat is een gebrek aan gegevens."""
    f = f or instelling()
    p = item.get("price")
    if not p:
        return True
    onder = f["ondergrens_perceel"] if is_perceel(item.get("category")) else f["ondergrens_pand"]
    if onder and p < onder:
        return False
    boven = f.get("bovengrens")
    return not (boven and p > boven)


def juiste_soort(item: dict, f: dict | None = None) -> bool:
    """Is dit iets om te renoveren of op te bouwen?"""
    f = f or instelling()
    cats = [c.lower() for c in (f.get("categorieen") or [])]
    cat = (item.get("category") or "").lower()
    # Exact vergelijken, niet op beginletters: anders glipt "perceel-geen-wonen" mee met "perceel",
    # en dat is juist grond waar geen woning op mag.
    if not cats or cat in cats:
        return True
    if f.get("sloop_nieuwbouw_telt_mee"):
        scen = (item.get("scenario") or "").lower()
        if "sloop" in scen or "nieuwbouw" in scen:
            return True
    # Jan 26-09-2026: een gewoon huis waarvan de advertentie niets zegt, telt tóch mee als het oud is
    # én meer dan 40 % onder de wijkprijs staat. Zie renovatie.opknapper_vermoeden.
    if (f.get("opknapper_vermoeden") or {}).get("aan") and item.get("opknapper"):
        return True
    return False


def tab(item: dict, urb: dict | None = None, f: dict | None = None) -> str | None:
    """Op welk tabblad hoort dit object? None betekent: helemaal niet in beeld."""
    f = f or instelling()
    area = (item.get("area") or "").lower()
    if not juiste_soort(item, f) or not binnen_prijs(item, f):
        return None
    if area in [g.lower() for g in (f.get("gebieden") or [])]:
        # Jan 26-09-2026: kan er geen serieus bod worden gedaan omdat de vraagprijs te ver boven het
        # haalbare staat, dan hoort dat object niet in de hoofdlijst maar op een eigen tabblad. Zakt
        # de prijs later, dan komt het vanzelf terug.
        bod = item.get("bod") or {}
        if bod.get("serieus_mogelijk") is False:
            return TE_DUUR
        if f.get("bestemming_streng") and urb:
            soort = (urb.get("duiding") or {}).get("soort")
            if soort and soort != "stedelijk":
                # Jan 25-09-2026: op 'misschien later' hoort alleen terrein dat ooit bebouwd mág
                # worden. Rustieke en beschermde grond verdwijnt helemaal uit beeld.
                if f.get("later_alleen_urbaniseerbaar") and soort != "urbaniseerbaar":
                    return None
                return LATER
        return KANSEN
    if area in [g.lower() for g in (f.get("gebieden_apart") or [])]:
        return BUITEN
    return None


def past(item: dict, f: dict | None = None) -> bool:
    """Staat dit object in de hoofdlijst? De bestemming zit al in het item als hij is opgevraagd."""
    return tab(item, item.get("urbanisme"), f) == KANSEN


def rijen(store, alle_gebieden: bool = True) -> list:
    """De databaserijen die op één van de tabbladen kunnen belanden.

    Scheelt rekenwerk: de rest wordt niet eens doorgerekend. De sloop-en-nieuwbouwuitzondering volgt
    uit het scenario en kan SQL niet zien; wat SQL wel kan is er alvast op filteren dat zo'n scenario
    een perceel van enige omvang met bebouwing nodig heeft."""
    f = instelling()
    geb = list(f.get("gebieden") or [])
    if alle_gebieden:
        geb += list(f.get("gebieden_apart") or [])
    cats = list(f.get("categorieen") or [])
    if not geb and not cats:
        return store.active_listings(area_only=True)
    q = "SELECT * FROM listings WHERE gone_at IS NULL AND area IS NOT NULL"
    args: list = []
    if geb:
        q += f" AND area IN ({','.join('?' * len(geb))})"
        args += geb
    if cats:
        q += f" AND (category IN ({','.join('?' * len(cats))})"
        args += cats
        if f.get("sloop_nieuwbouw_telt_mee"):
            q += " OR (plot_m2 >= 800 AND built_m2 IS NOT NULL)"
        ok = f.get("opknapper_vermoeden") or {}
        if ok.get("aan"):
            # Kandidaten voor het opknappervermoeden alvast binnenhalen: een bouwjaar uit het
            # kadaster is in SQL te toetsen, de wijkprijs niet. Dat laatste doet `past()`.
            q += (" OR (price IS NOT NULL AND built_m2 IS NOT NULL AND EXISTS("
                  "SELECT 1 FROM parcels p WHERE p.listing_id = listings.id AND p.year IS NOT NULL"
                  " AND p.year < ?))")
            args.append(int(ok.get("bouwjaar_voor", 1995)))
        q += ")"
    # Prijsondergrens alvast in SQL: het laagste van de twee, de rest zeeft `binnen_prijs`.
    onder = min(x for x in (f.get("ondergrens_perceel"), f.get("ondergrens_pand")) if x) if (
        f.get("ondergrens_perceel") or f.get("ondergrens_pand")) else None
    if onder:
        q += " AND (price IS NULL OR price >= ?)"
        args.append(onder)
    return store.con.execute(q + " ORDER BY area, price", args).fetchall()


def filter(items: list[dict]) -> list[dict]:
    f = instelling()
    return [i for i in items if past(i, f)]


def per_tab(items: list[dict]) -> dict[str, list[dict]]:
    f = instelling()
    uit: dict[str, list[dict]] = {KANSEN: [], LATER: [], BUITEN: [], TE_DUUR: []}
    for i in items:
        t = i.get("tab") or tab(i, i.get("urbanisme"), f)
        if t in uit:
            uit[t].append(i)
    return uit


def omschrijving() -> str:
    """Eén zin voor bovenaan een rapport of de app."""
    f = instelling()
    g = ", ".join({"javea": "Jávea", "benitachell": "Benitachell", "moraira": "Moraira"}.get(x, x)
                  for x in f["gebieden"])
    return (f"Alleen {g}: panden om te renoveren, percelen om op te bouwen en woningen die groot "
            f"genoeg zijn om te slopen en opnieuw op te bouwen.")

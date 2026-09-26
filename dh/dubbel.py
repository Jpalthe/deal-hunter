"""Dezelfde woning die via twee bronnen binnenkwam, tot één kaartje maken.

Jan, 26-09-2026: negentien keer stond dezelfde woning twee keer in de lijst, meestal omdat wij hem
zowel via Idealista als via de site van het kantoor zelf hadden. Eén regel in de lijst dus, met alle
bronnen eronder — want dat een woning bij meerdere kantoren staat, is onderhandelinformatie.

Wanneer noemen wij twee advertenties dezelfde woning? Zelfde gebied, vraagprijs binnen 1 %, en een
oppervlakte die binnen 5 % overeenkomt. Dat laatste is de strenge eis: zonder een maat om op te
vergelijken voegen wij niets samen, want twee percelen van dezelfde prijs in dezelfde wijk zijn
doodgewoon en géén dubbeling.
"""
from __future__ import annotations

PRIJS_MARGE = 0.01
MAAT_MARGE = 0.05


def _maten_kloppen(a: dict, b: dict) -> bool:
    vergeleken = False
    for veld in ("plot_m2", "built_m2"):
        x, y = a.get(veld), b.get(veld)
        if x and y:
            vergeleken = True
            if abs(x - y) / max(x, y) > MAAT_MARGE:
                return False
    return vergeleken


def zelfde(a: dict, b: dict) -> bool:
    # Twee advertenties bij hetzelfde kantoor zijn twee verschillende woningen. Een makelaar zet
    # dezelfde woning niet twee keer op zijn eigen site. Zonder deze regel werden tien appartementen
    # van xabiacasa.com met dezelfde vraagprijs tot één kaartje geplakt.
    if (a.get("source") or "?") == (b.get("source") or "!"):
        return False
    if (a.get("area") or "") != (b.get("area") or ""):
        return False
    pa, pb = a.get("price"), b.get("price")
    if not pa or not pb:
        return False
    if abs(pa - pb) / max(pa, pb) > PRIJS_MARGE:
        return False
    return _maten_kloppen(a, b)


def _rijker(i: dict) -> tuple:
    """Welke van twee vermeldingen de hoofdregel wordt.

    Voorkeur voor de vermelding met een coördinaat, want daar hangen het perceel, de bestemming en
    de helling aan. Daarna voor de oudste: die staat er het langst en draagt het prijsverloop."""
    return (1 if i.get("lat") is not None else 0,
            1 if i.get("plot_m2") or i.get("built_m2") else 0,
            -(len(str(i.get("first_seen") or "9999"))),
            str(i.get("first_seen") or "9999"))


def bron_naam(i: dict) -> str:
    if i.get("kantoor"):
        return str(i["kantoor"])
    b = str(i.get("source") or "")
    if b.startswith("makelaar:"):
        return b.split(":", 1)[1]
    return {"bp": "Background Properties", "idealista": "Idealista",
            "idealista-zoek": "Idealista"}.get(b, b)


def voeg_samen(items: list[dict]) -> list[dict]:
    """Geeft de lijst terug met dubbelingen samengevoegd.

    De hoofdregel krijgt `ook_bij`: de andere bronnen met hun eigen vraagprijs en adres. Verschilt de
    vraagprijs tussen twee kantoren, dan is dat zichtbaar, want dat is precies het soort ding waar je
    een gesprek mee opent."""
    gedaan: set[int] = set()
    uit: list[dict] = []
    for i, a in enumerate(items):
        if id(a) in gedaan:
            continue
        groep = [a]
        for b in items[i + 1:]:
            if id(b) in gedaan:
                continue
            # Vergelijken met de eerste, niet met de hele groep: anders rijgt A~B en B~C ook A en C
            # aan elkaar terwijl die twee niets met elkaar te maken hebben.
            if zelfde(a, b) and all((g.get("source") or "?") != (b.get("source") or "!") for g in groep):
                groep.append(b)
                gedaan.add(id(b))
        gedaan.add(id(a))
        if len(groep) == 1:
            uit.append(a)
            continue
        groep.sort(key=_rijker, reverse=True)
        hoofd = dict(groep[0])
        hoofd["ook_bij"] = [{"bron": bron_naam(x), "ref": x.get("ref"), "prijs": x.get("price"),
                             "url": x.get("url"), "id": x.get("id")} for x in groep[1:]]
        hoofd["bronnen"] = len(groep)
        prijzen = [x.get("price") for x in groep if x.get("price")]
        if prijzen and max(prijzen) - min(prijzen) > 0:
            hoofd["prijsverschil_tussen_bronnen"] = round(max(prijzen) - min(prijzen))
        uit.append(hoofd)
    return uit

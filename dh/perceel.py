"""Hoort dit kadastrale perceel bij deze advertentie, en waar spreken ze elkaar tegen?

Eigen module omdat zowel de samenvatting als de rekenaar dit nodig heeft: de rekenaar mag de
grondwerktoeslag alleen toepassen als vaststaat dat het gemeten perceel het object ís. Anders reken
je de helling van een sportcomplex toe aan een appartement dat erboven staat — dat geval kwam
werkelijk voor (onderzoek N08 §4).
"""
from __future__ import annotations


def perceel_is_het_object(item: dict, parcel: dict | None) -> bool:
    """Is het kadastrale perceel aantoonbaar hetzelfde als wat te koop staat?

    Dit moet hard zijn, want er hangt een bedrag aan. De pin uit een advertentie valt vaak binnen een
    veel groter kadastraal perceel: bij object 615 stond 700 m² te koop terwijl het perceel onder de
    pin 31.353 m² meet. De fiscale waarde van dát perceel zegt niets over de koop. Daarom eisen wij
    dat de afstand klein is én dat de opgegeven maat en de kadastrale maat elkaar niet tegenspreken."""
    if not parcel or (parcel.get("distance_m") or 0) > 25:
        return False
    # Als de advertentie kale grond aanbiedt en het kadaster ziet er een gebouw staan, dan is er
    # iets mis: óf de pin wijst het verkeerde perceel aan, óf er staat bebouwing die de advertentie
    # verzwijgt. In beide gevallen is het perceel niet vastgesteld.
    if not item.get("built_m2") and (parcel.get("built_m2") or 0) > 40:
        return False
    vergeleken = False
    for eigen, kadaster, onder, boven in (("plot_m2", "plot_m2", 0.75, 1.35),
                                          ("built_m2", "built_m2", 0.70, 1.40)):
        a, b = item.get(eigen), parcel.get(kadaster)
        if a and b:
            vergeleken = True
            if not (onder <= (b / a) <= boven):
                return False
    return vergeleken          # zonder iets om te vergelijken is het niet vastgesteld


def tegenspraak(item: dict, parcel: dict | None) -> list[str]:
    """Waar de advertentie en het kadaster elkaar tegenspreken.

    Geen oordeel, wel een reden om te bellen: het kadaster zegt niets over eigendom en de pin uit een
    advertentie kan naast het echte perceel liggen. Beide verklaringen zijn de moeite van het
    uitzoeken waard, en de tweede is soms een kans."""
    if not parcel or (parcel.get("distance_m") or 0) > 25:
        return []
    uit = []
    kb, kp = parcel.get("built_m2") or 0, parcel.get("plot_m2") or 0
    # Een kadastraal perceel dat vele malen groter is dan de advertentie, telt hier niet als
    # tegenspraak: dan ligt de pin vrijwel zeker in een groot gemeenschappelijk of rustiek perceel.
    # Dat is een onzekere koppeling, geen uitspraak over het object. Zie `perceel_is_het_object`.
    if kp and item.get("plot_m2") and kp / item["plot_m2"] > 3:
        return []
    if not item.get("built_m2") and kb > 40:
        jaar = f" uit {int(parcel['year'])}" if parcel.get("year") else ""
        uit.append(f"Aangeboden als grond, maar het kadaster ziet {int(kb)} m² bebouwing{jaar}")
    if item.get("built_m2") and kb and kb / item["built_m2"] > 1.4:
        uit.append(f"Kadaster telt {int(kb)} m² gebouwd, de advertentie {int(item['built_m2'])} m²")
    return uit


def grond_is_hetzelfde(item: dict, parcel: dict | None) -> bool:
    """Is dit dezelfde lap grond? Een lossere toets, en met opzet.

    Voor de fiscale waarde moet het perceel het object zíjn: daar hangt een bedrag aan een gebouw.
    Voor de helling gaat het alleen om het terrein. Dat een advertentie zwijgt over een schuur die
    het kadaster wél ziet, zegt niets over hoe steil de grond is. Daarom telt hier alleen of het om
    hetzelfde stuk grond gaat: de pin ligt er dichtbij en de perceelmaten spreken elkaar niet tegen.

    Niet voor appartementen: wie een verdieping koopt, koopt de helling eronder niet.
    """
    if not parcel or (parcel.get("distance_m") or 0) > 25:
        return False
    cat = (item.get("category") or "").lower()
    if cat.startswith("appartement") or (item.get("type") or "").lower() in (
            "apartment", "flat", "penthouse", "studio", "duplex"):
        return False
    eigen, kadaster = item.get("plot_m2"), parcel.get("plot_m2")
    if eigen and kadaster:
        # ruimer dan de fiscale toets: opgaven van perceelmaten in advertenties zijn slordig
        return 0.6 <= (kadaster / eigen) <= 1.7
    if eigen or kadaster:
        return True          # één van de twee ontbreekt: de grond is nog steeds die grond
    return False             # geen enkel perceelgegeven: niets om op te varen

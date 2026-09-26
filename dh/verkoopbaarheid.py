"""Waar de eindkoper op let, per object zichtbaar gemaakt.

Jan, 26-09-2026: zeezicht, zwembad, loopafstand tot strand of dorp en gelijkvloers wonen zijn
allemaal belangrijk — maar hij wil projecten die er niet aan voldoen **niet links laten liggen**.
Daarom is dit een indicator en nooit een uitsluiting. Wat hier staat verandert geen enkel bedrag;
het zegt alleen hoe makkelijk het eindproduct straks wegloopt.

Wat hier een claim is en wat een feit:
- zeezicht en gelijkvloers komen uit de advertentietekst. Dat is wat de aanbieder zegt, niet wat wij
  hebben gezien. Ze staan daarom als "volgens de advertentie" in het dossier.
- het zwembad komt uit de kenmerken of de tekst, en is bij een bezichtiging te controleren.
- de afstanden zijn gerekend vanaf de coördinaat van de advertentie tot het middelpunt van de wijk
  Puerto–Arenal en dat van het Centrum. Die twee punten zijn het gemiddelde van 66 respectievelijk
  64 woningen uit onze eigen database (kader/ankerpunten.json), niet een adres dat ik heb bedacht.
  Het is dus "afstand tot het hart van die wijk", niet "afstand tot het water".
"""
from __future__ import annotations

import json
import math
import re
from functools import lru_cache

from . import config

ZEEZICHT = re.compile(r"(vistas? al mar|vista mar|sea ?view|zeezicht|meerblick|blick aufs meer|"
                      r"vue sur (la )?mer|panor[aá]mica del mar)", re.I)
ZWEMBAD = re.compile(r"(piscina|swimming ?pool|\bpool\b|zwembad|schwimmbad)", re.I)
GELIJKVLOERS = re.compile(r"(una (sola )?planta|planta [uú]nica|single ?(storey|level)|one ?level|"
                          r"gelijkvloers|ebenerdig|bungalow|todo en una planta)", re.I)
LIFT = re.compile(r"(ascensor|elevator|\blift\b|aufzug)", re.I)
GEEN_LIFT = re.compile(r"(sin ascensor|no ascensor|zonder lift|kein aufzug|no lift|without (a )?lift)", re.I)
HOGE_VERDIEPING = re.compile(r"\b([3-9]|1[0-9])\s*[ªaº°]?\s*(planta|piso|floor|etage|verdieping)\b|"
                             r"\b(tercera|cuarta|quinta|third|fourth|fifth)\s+(planta|floor)\b", re.I)


@lru_cache(maxsize=1)
def ankers() -> dict:
    try:
        return json.loads((config.KADER / "ankerpunten.json").read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}


def afstand_m(lat1, lon1, lat2, lon2) -> int:
    """Hemelsbrede afstand in meters. Goed genoeg op deze schaal."""
    r = 6371000.0
    p1, p2 = math.radians(lat1), math.radians(lat2)
    dp, dl = math.radians(lat2 - lat1), math.radians(lon2 - lon1)
    a = math.sin(dp / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return int(round(2 * r * math.asin(math.sqrt(a))))


def _afstanden(item: dict) -> dict:
    """Afstand tot het hart van Puerto–Arenal en van het Centrum, als er een coördinaat is."""
    uit = {}
    a = ankers()
    if item.get("lat") is not None and item.get("lon") is not None:
        for sleutel, naam in (("puerto_arenal", "Puerto–Arenal"), ("centro", "Centrum")):
            p = a.get(sleutel)
            if p:
                uit[naam] = afstand_m(item["lat"], item["lon"], p["lat"], p["lon"])
    return uit


def beoordeel(item: dict, tekst: str = "", features: list | None = None) -> dict:
    """Vier punten waar de eindkoper op let. Nooit een reden om iets uit de lijst te halen."""
    t = " ".join(x for x in (tekst, " ".join(str(f) for f in (features or []))) if x)
    # Onderscheid tussen "staat er niet" en "wij weten het niet". Van 2.928 woningen in Jávea hebben
    # er maar 298 een kenmerkenlijst en 399 een coördinaat; de rest komt van makelaarssites waar wij
    # alleen een afgeknipte omschrijving hebben. Een 0 uitdelen zou dan zeggen dat er geen zeezicht
    # is, terwijl wij er niets van weten.
    genoeg = len(t.strip()) >= 80 or bool(features)
    if not genoeg:
        return {"punten": None, "van": 4, "redenen": [], "missers": [], "soort": None,
                "afstanden_m": _afstanden(item),
                "toelichting": ("Niet te beoordelen: van dit object hebben wij te weinig tekst. "
                                "Dat betekent niet dat het zeezicht of zwembad mist, alleen dat de "
                                "bron het ons niet vertelt.")}
    # Bij een perceel zeggen zwembad en gelijkvloers niets: die bouw je er zelf bij. Daar tellen
    # alleen het uitzicht en de ligging, en dan uit twee in plaats van uit vier.
    perceel = str(item.get("category") or "").startswith("perceel") or \
        str(item.get("type") or "").strip().lower() in ("land", "plot", "terreno", "parcela")
    punten, redenen, missers = 0, [], []

    if ZEEZICHT.search(t):
        punten += 1
        redenen.append("zeezicht volgens de advertentie")
    else:
        missers.append("geen zeezicht genoemd")

    if not perceel:
        if ZWEMBAD.search(t):
            punten += 1
            redenen.append("zwembad")
        else:
            missers.append("geen zwembad genoemd")
        if GELIJKVLOERS.search(t):
            punten += 1
            redenen.append("gelijkvloers")

    afst = _afstanden(item)
    if True:
        if afst:
            dichtst = min(afst.values())
            if dichtst <= 1200:
                punten += 1
                redenen.append(f"{dichtst} m van {min(afst, key=afst.get)}")
            elif dichtst > 3000:
                missers.append(f"{dichtst} m van de bewoonde kern")

    return {"punten": punten, "van": 2 if perceel else 4, "redenen": redenen, "missers": missers[:2],
            "soort": "perceel" if perceel else "woning",
            "afstanden_m": afst,
            "toelichting": ("Vier dingen waar de koper op let. Dit verandert geen bedrag; het zegt "
                            "alleen hoe vlot het eindproduct wegloopt. Jan wil objecten die hier "
                            "niet aan voldoen uitdrukkelijk niet laten liggen.")}


def appartement_zonder_lift_hoog(tekst: str) -> str | None:
    """Harde uitsluiting van Jan (26-09-2026): een appartement boven de tweede zonder lift.

    Alleen uitsluiten als de tekst allebei zegt. Zwijgt de advertentie over de lift, dan sluiten wij
    niets uit — een niet-gestelde vraag is geen antwoord."""
    if not tekst:
        return None
    m = HOGE_VERDIEPING.search(tekst)
    if not m:
        return None
    if GEEN_LIFT.search(tekst):
        return f"{m.group(0).strip()} zonder lift"
    return None

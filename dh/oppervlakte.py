"""Welke vierkante meters staan er in een advertentie, en wat is daarvan het bebouwde woondeel.

Uit onderzoek N06 (18-09-2026): het veld "oppervlakte" heeft geen vaste betekenis. Soms is het
de woonruimte, soms de woonruimte plus muren, soms alles bij elkaar inclusief garage, kelder en
overdekt terras. In ons eigen materiaal loopt het verschil bij hetzelfde huis op tot een factor 2,4.

De fout doet pas pijn als je twee maten door elkaar gebruikt, en dat doet het model: de prijs per
m² komt uit advertentie-oppervlakten en wordt vermenigvuldigd met het aantal m² dat wij werkelijk
bouwen. Daarom bepalen wij per object het regime en rekenen wij met het bebouwde woondeel.

Drie regimes, met de factor uit N06 §6.3:

  A woon        de tekst noemt woonoppervlak en dat komt overeen met het veld    × 1,00
  B construida  geen tegenaanwijzing, gangbaar in Spanje                         × 0,96
  C totaal      de tekst telt terras, garage of kelder mee                       × 0,62
  onbekend      alleen een kaal getal                                            × 0,90

De winst zit niet in de factor maar in de indeling. Regime C is het enige dat echt schade doet,
en dat is aan de tekst te herkennen.
"""
from __future__ import annotations

import re
import unicodedata

FACTOR = {"A": 1.00, "B": 0.96, "C": 0.62, "onbekend": 0.90}
LABEL = {
    "A": "woonoppervlak: de tekst noemt het zo en het veld komt overeen",
    "B": "bebouwd oppervlak (superficie construida), de gangbare maat",
    "C": "totaal inclusief terras, garage of kelder",
    "onbekend": "niet vast te stellen uit de tekst",
}

# Regime A: de tekst noemt uitdrukkelijk woonoppervlak
WOON = [
    r"superficie (de )?vivienda", r"m2?\s*(de\s*)?vivienda\b", r"[aá]rea habitable", r"superficie habitable",
    r"living (area|space)\b", r"habitable (area|surface)", r"woonoppervlak", r"wohnfl[aä]che",
    r"metros (cuadrados )?(de )?vivienda", r"superficie [uú]til",
]
# Regime C: de tekst telt buitenruimte, garage of kelder mee in het getal
TOTAAL = [
    r"inclu(ye|yendo|ido|idos|sive)\s+(el\s+)?(terraza|garaje|s[oó]tano|p[aá]rking|trastero|porche|naya)",
    r"including\s+(the\s+)?(terrace|garage|basement|parking|storage)",
    r"inclusief\s+(terras|garage|kelder|berging)",
    r"superficie total construida", r"total construido", r"construidos en total",
    r"(terraza|garaje|s[oó]tano)s?\s*(de\s*)?\d{2,4}\s*m2?\s*(incluid|inclu)",
]
# Losse m²-posten per bouwdeel: als die optellen tot het veld is het regime C
POSTEN = re.compile(r"(vivienda|planta|s[oó]tano|garaje|terraza|porche|[aá]tico|bajo|trastero|naya|trastero)"
                    r"[^.\n]{0,40}?(\d{2,4})\s*m", re.I)


def _norm(s: str) -> str:
    return unicodedata.normalize("NFKD", s or "").lower()


def _find(pats: list[str], t: str) -> list[str]:
    out = []
    for p in pats:
        m = re.search(p, t, re.I)
        if m:
            out.append(m.group(0).strip())
    return out


def bepaal(text: str, size: float | None, rooms: int | None = None,
           catastro_built: float | None = None) -> dict:
    """Bepaalt het regime en het bebouwde woondeel.

    Geeft altijd terug waar het antwoord vandaan komt, zodat het in het dossier verantwoord kan
    worden. Zonder oppervlakte is er niets te bepalen."""
    if not size:
        return {"regime": "onbekend", "factor": None, "m2_woon": None, "hard": False,
                "reden": "geen oppervlakte in de bron", "signalen": []}
    t = _norm(text or "")
    woon = _find(WOON, t)
    totaal = _find(TOTAAL, t)
    redenen: list[str] = []

    # sterkste signaal: losse posten die samen ongeveer het veld vullen
    posten = [float(m.group(2)) for m in POSTEN.finditer(t)]
    som = sum(posten)
    if len(posten) >= 2 and size and 0.85 * size <= som <= 1.25 * size:
        redenen.append(f"de tekst noemt {len(posten)} losse m²-posten die samen {som:.0f} m² zijn, "
                       f"ongeveer gelijk aan de opgegeven {size:.0f} m²")
        return {"regime": "C", "factor": FACTOR["C"], "m2_woon": round(size * FACTOR["C"]),
                "hard": False, "reden": "; ".join(redenen), "signalen": totaal + [f"{len(posten)} losse posten"]}

    # het kadaster als tweede mening: staat het woondeel er veel lager in, dan telt de advertentie meer mee
    if catastro_built and size and catastro_built > 0 and size / catastro_built >= 1.30:
        redenen.append(f"het kadaster kent {catastro_built:.0f} m² bebouwd tegenover {size:.0f} m² in de advertentie")
        return {"regime": "C", "factor": FACTOR["C"], "m2_woon": round(size * FACTOR["C"]),
                "hard": False, "reden": "; ".join(redenen), "signalen": totaal}

    if totaal:
        redenen.append(f"de tekst zegt zelf dat er buitenruimte of bijruimte in zit: {totaal[0]}")
        return {"regime": "C", "factor": FACTOR["C"], "m2_woon": round(size * FACTOR["C"]),
                "hard": False, "reden": "; ".join(redenen), "signalen": totaal}

    # veel m² per slaapkamer wijst op meegetelde bijruimte
    if rooms and rooms >= 2 and size / rooms > 130:
        redenen.append(f"{size:.0f} m² op {rooms} slaapkamers is {size / rooms:.0f} m² per kamer; "
                       "dat wijst op meegetelde garage, kelder of terras")
        return {"regime": "C", "factor": FACTOR["C"], "m2_woon": round(size * FACTOR["C"]),
                "hard": False, "reden": "; ".join(redenen), "signalen": []}

    if woon:
        redenen.append(f"de tekst noemt het woonoppervlak: {woon[0]}")
        return {"regime": "A", "factor": FACTOR["A"], "m2_woon": round(size), "hard": True,
                "reden": "; ".join(redenen), "signalen": woon}

    if text and len(text) > 200:
        redenen.append("geen tegenaanwijzing in een uitgebreide beschrijving; aangenomen dat het "
                       "bebouwd oppervlak is, de gangbare maat in Spanje")
        return {"regime": "B", "factor": FACTOR["B"], "m2_woon": round(size * FACTOR["B"]), "hard": False,
                "reden": "; ".join(redenen), "signalen": []}

    redenen.append("alleen een kaal getal zonder beschrijving; hier is niet vast te stellen wat er in zit")
    return {"regime": "onbekend", "factor": FACTOR["onbekend"], "m2_woon": round(size * FACTOR["onbekend"]),
            "hard": False, "reden": "; ".join(redenen), "signalen": []}


def toelichting(b: dict) -> str:
    """Eén zin voor in het dossier."""
    if not b or not b.get("m2_woon"):
        return "Het bebouwde woondeel is niet vast te stellen."
    r = b["regime"]
    if r == "A" and b.get("hard"):
        return f"De opgegeven oppervlakte is woonoppervlak; wij rekenen met {b['m2_woon']} m². {b['reden'].capitalize()}."
    return (f"Wij rekenen met {b['m2_woon']} m² bebouwd woondeel in plaats van de opgegeven oppervlakte "
            f"({LABEL[r]}, factor {b['factor']:.2f}). Reden: {b['reden']}. "
            "Dat is een schatting; de nota simple of een meting geeft uitsluitsel.")

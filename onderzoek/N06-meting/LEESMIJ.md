# Meetmateriaal bij N06 — oppervlaktedefinities

Gemeten op 18-09-2026. Alles alleen-lezen; er is niets aangepast aan draaiende diensten.

| Bestand | Wat het is |
|---|---|
| `catastro_meting.py` | Vraagt per villa met coördinaten de kadastrale referentie op (`Consulta_RCCOOR`) en daarna de opbouw van de bebouwing (`Consulta_DNPRC`). 1 verzoek per 1,2 s. Levert alleen *datos no protegidos* — geen eigenaarsnamen. |
| `catastro_meting.json` | Ruwe uitkomst, 120 objecten. |
| `tekst_analyse.py` | Zoekt in de volledige advertentieteksten (feed poort 3100, alle talen) naar oppervlaktegetallen en de woorden eromheen. |
| `tekst_analyse.json` | Per object de gevonden getallen met hun context. |
| `analyse2.py` | Groepeert de kadastrale bouwdelen en rekent de verhoudingen uit §4.2 en §5.2 van het rapport. |
| `analyse2.json` | `alles` = alle opvragingen met bebouwing; `schoon` = de 48 eengezins-villapercelen waarop de statistiek rust. |

Opnieuw draaien: `python3 catastro_meting.py` (duurt ongeveer vijf minuten), daarna
`python3 analyse2.py`. De paden in de scripts wijzen naar de sessiemap en moeten dan worden
aangepast.

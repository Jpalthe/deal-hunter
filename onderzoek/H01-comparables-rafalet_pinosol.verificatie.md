# Verificatie H01 — Vergelijkingsprijzen El Rafalet · Pinomar–Pinosol · La Lluca–Tarraula

**Gecontroleerd bestand:** `onderzoek/H01-comparables-rafalet_pinosol.md` (zone_key `rafalet_pinosol`)
**Rol:** tegenspreker · **controledatum:** 15-09-2026 · **bron:** officiële Idealista-assistent (MCP `property_detail` 24×, `search_properties` 6×), locale es-ES, land es
**Let op:** alle bedragen zijn **vraagprijzen** van lopende advertenties op 15-09-2026, geen transactieprijzen en geen marktwaarde. Het originele bestand is **niet** gewijzigd; gecorrigeerde waarden staan alleen hier.

---

## 1. Oordeel in het kort

| Reeks (origineel) | n | mediaan orig. | Oordeel | Gecorrigeerde waarde / opmerking |
|---|---|---|---|---|
| `villa_renovated` | 20 | 4.807 | **BEVESTIGD** | Rekenkunde klopt exact; 11 van 20 objecten met `property_detail` bevestigd; onafhankelijke zoekopdracht geeft mediaan 4.396 (−8,5 %, binnen ±15 %). Kanttekening: 110895902 (9.203 €/m²) is een ontwikkelaarsproduct dat onder IVA wordt verkocht met veld "Construido en 2026" — hoort eerder bij nieuwbouw. Zonder dat object: mediaan 4.760 (n = 19). |
| `villa_renovated (zonder 2 fincas)` | 18 | 4.807 | **BEVESTIGD** | Rekenkunde klopt (p25 4.250, p75 5.662). |
| `villa_new` | 9 | 5.717 | **BEVESTIGD** | Rekenkunde klopt; 7 van 9 met `property_detail` bevestigd; onafhankelijke zoekopdracht geeft mediaan 5.717 (identiek, n = 5). Kanttekening: 112527650 (5.278) is géén aantoonbare nieuwbouw (zie §4). |
| `villa_new (zonder op plan)` | 6 | 4.573 | **WEERLEGD (indeling)** | De regel "op plan" is inconsequent toegepast: 111656885 (oplevering **maart 2027**, tegels nog te kiezen, foto's zijn plattegronden) is niet minder "op plan" dan 112158635 (juni 2027) dat wél is uitgesloten. Consequent toegepast: **n = 5, mediaan 5.278** (3.307–9.750). Strikt (ook zonder het twijfelgeval 112527650): n = 4, mediaan 4.638. |
| `villa_renovated_tosal` | 6 | 4.726 | **BEVESTIGD** | Rekenkunde klopt; 5 van 6 bevestigd. Onafhankelijke zoekopdracht vindt slechts 2 van de 6 terug (mediaan 5.338, +13 %, binnen ±15 % maar n = 2 — zwak). |
| `villa_new_tosal` | 1 | 6.848 | **BEVESTIGD** | Zelfde enige object (111928138) onafhankelijk teruggevonden. |
| Per-zone-medianen (Rafalet 5.660 / Pinosol 4.760 / La Lluca 4.546) | 5/7/8 | — | **BEVESTIGD** | Rekenkunde klopt exact. |
| Deduplicatie | — | — | **BEVESTIGD** | Zie §5; geen dubbele advertentie als apart object geteld. |
| "Para reformar" of nieuwbouw in de gerenoveerde reeks | — | — | **BEVESTIGD (met 1 kanttekening)** | Geen renovatieobject aangetroffen. Eén grensgeval nieuwbouw-of-renovatie: 110895902 (§4). |

**Netto-effect voor Jan:** de hoofdcijfers (4.807 gerenoveerd, 5.717 nieuwbouw, 4.726 Tosal) staan overeind. Alleen de subreeks "nieuwbouw zonder op plan" moet worden gelezen als **5.278 (n = 5)** in plaats van 4.573 (n = 6) — en met n = 4–6 is elke variant van die subreeks fragiel.

---

## 2. Controle 1 — `property_detail` op de voorbeelden (prijs, m², renovatie/nieuwbouw)

Alle 24 opgevraagde objecten geven vandaag **exact** de prijs en m² gebouwd uit het originele bestand (bewijstype 1, tool-uitvoer 15-09-2026). Per object wat de tekst en het veld *Construido en* werkelijk zeggen:

### `villa_renovated` (11 van 20 geopend)

| Code | Prijs / m² (tool) | €/m² | Veld bouwjaar | Wat de tekst zegt | Oordeel |
|---|---|---|---|---|---|
| 111452530 | 600.000 / 140 | 4.286 | 1955 | "Completamente reformada", geen renovatiejaar, geen zwembad, label G | gerenoveerd ✔ |
| 111909291 | 850.000 / 236 | 3.602 | 1980 | "renovada por completo en 2024" | gerenoveerd ✔ |
| 112229028 | 1.149.000 / 203 | 5.660 | 1980 | "Recientemente renovada por completo", label G (!) | gerenoveerd ✔ (label G rijmt slecht met "volledig gerenoveerd") |
| 109546138 | 1.495.000 / 264 | 5.663 | 2017 | "villa contemporánea", label B/A | modern ✔ |
| 108153256 | 1.520.000 / 221 | 6.878 | — | tekst opent met "villa de nueva construcción", sluit met "renovación completa en julio de 2026"; veld "Segunda mano/buen estado"; label C | gerenoveerd ✔, maar de aanbieder verkoopt het als nieuwbouw |
| 111952972 | 1.190.000 / 373 | 3.190 | — | "Cuidadosamente modernizada", architectuur behouden, label G, prijs −5 % (1.250.000 → 1.190.000) | zwakste renovatieclaim, zoals het origineel al zegt |
| 112509325 | 1.795.000 / 360 | 4.986 | 1983 | "actualmente en proceso de una completa renovación y ampliación", klaar eind november; particuliere verkoper; 306 m² nuttig | **nog niet gerenoveerd** — vraagprijs voor het eindproduct |
| 112310283 | 695.000 / 146 | 4.760 | — | alleen "Esta villa reformada", geen jaar, label G | zwak, zoals origineel zegt |
| 111229059 | 845.000 / 130 | 6.500 | — | "recientemente reformada", 130 m² op 1.999 m² | gerenoveerd ✔ (grondwaarde weegt zwaar) |
| 110895902 | 1.675.000 / 182 | 9.203 | **2026** | "Villa totalmente renovada", "producto desarrollado y ofrecido exclusivamente por [ontwikkelaar]", **verkoop onder IVA in plaats van ITP**, label A | **grensgeval**: fiscaal en volgens het veld een nieuw product |
| 112504358 (Tosal) | zie §2c | | | | |

Niet geopend (9): 109969426, 111189527, 110676663, 110765633, 112342262, 108679725, 112501089, 109645331, 110668828, 112329948. Van 109645331, 110668828, 112329948, 110676663, 110765633 en 112509325 is de renovatieclaim wél bevestigd via de beschrijving in de onafhankelijke zoekresultaten (§3).

### `villa_new` (7 van 9 geopend)

| Code | Prijs / m² | €/m² | Status / veld | Wat de tekst zegt | Oordeel |
|---|---|---|---|---|---|
| 111918606 | 1.088.000 / 329 | 3.307 | `newdevelopment`, promotie notFinished | "lista en marzo de 2026 (sujeto a cambios)"; foto's zijn gevel + plattegronden | nieuwbouw ✔, oplevering al 6 maanden over datum |
| 112527650 | 950.000 / 180 | 5.278 | `good`, veld "Construido en 2026", label G | "tradicional villa … bien cuidada", petanquebaan, cocina de verano; nergens "nueva construcción" | **twijfel**: veld en tekst spreken elkaar tegen |
| 112462622 (dubbel van 112527650) | 950.000 / 180 | 5.278 | `good`, **geen** bouwjaar | "La construcción es joven", "nueva zona de Pinomar"; garage al omgebouwd tot 4e slaapkamer | zelfde object; "joven" ≠ 2026 |
| 112093850 | 1.150.000 / 177 | 6.497 | `newdevelopment` | perceel 889 m² + goedgekeurde licentie, "listo para construir", prijs excl. IVA, notaris, aansluitingen | op plan ✔ (niets gebouwd) |
| 106823897 | 1.275.000 / 223 | 5.717 | `good`, geen bouwjaar, label G | "fase final de su construcción"; advertentie > 1 jaar niet bijgewerkt | in aanbouw (status onbekend sinds > 1 jaar) |
| 111656885 | 1.288.000 / 333 | 3.868 | `good`, veld 2026, label G | "Finalización marzo de 2027", "todavía existe la oportunidad de elegir azulejos y acabados"; foto's grotendeels plattegronden/renders | **op plan / in aanbouw, oplevering 2027** |
| 112165476 | 1.495.000 / 420 | 3.560 | `good`, veld 2026 | "cerca de su finalización"; foto's tonen gebouwde villa | in eindfase ✔ |
| 112515850 | 1.950.000 / 200 | 9.750 | `newdevelopment`, notFinished, projectlabel A | volledige uitrusting beschreven; 12 foto's incl. plattegronden | nieuwbouw ✔ (opleverstatus onbekend) |

Niet geopend: 111718472 (op plan, "14 meses desde el inicio de las obras" bevestigd in zoekresultaat §3), 112158635.

### `villa_renovated_tosal` (5 van 6) en `villa_new_tosal` (1 van 1)

| Code | Prijs / m² | €/m² | Veld | Tekst | Oordeel |
|---|---|---|---|---|---|
| 110753189 | 720.000 / 165 | 4.364 | — | "Completamente renovada", label C | gerenoveerd ✔ |
| 107385205 | 794.000 / 250 | 3.176 | 1978 | "reformada recientemente"; **advertentie > 1 jaar niet bijgewerkt**; 240 m² nuttig | gerenoveerd ✔, langloper |
| 111361293 | 1.399.000 / 275 | 5.087 | — | "actualizada en su totalidad", elektra + leidingen vernieuwd; 220 m² nuttig | gerenoveerd ✔ |
| 112504358 | 2.250.000 / 300 | 7.500 | — | "recientemente renovada", vloerverwarming 2026, gastenhuis, perceel 3.000 m² | gerenoveerd ✔ (300 m² is hoofdhuis + gastenhuis samen? tekst zegt 6 slk over beide) |
| 111433078 | 3.550.000 / 380 | 9.342 | — | "Ca Malva", "arquitectura contemporánea", lift, infinity pool; **label G**, geen bouwjaar | modern-claim ✔; label G is vreemd voor een nieuwe villa |
| 111928138 (new) | 1.575.000 / 230 | 6.848 | `newdevelopment`, notFinished | "villa moderna de lujo"; foto's = gevel + plattegronden + omgeving | nieuwbouw ✔ (niet af) |

Niet geopend: 110122731.

---

## 3. Controle 2 — Onafhankelijke zoekopdrachten per reeks

Andere formulering dan het origineel ("villa renovada …" / "villa de nueva construcción …" in plaats van "chalet reformado …" / "chalet obra nueva …"), CHALET, SALE, maxResults 50, één per zone. Bevinding (bewijstype 1): het woord **"villa"** in de query zet bij de assistent het subtype-filter **"Villas"** aan, waardoor minder advertenties terugkomen dan bij "chalet" (Rafalet 7 i.p.v. 22; Pinosol 29 in de band 600.000–2.000.000 i.p.v. 71 totaal; La Lluca 25 in de band 700.000–2.000.000 i.p.v. 70; Tosal 15 i.p.v. 38). De onafhankelijke set is dus een **deelverzameling**, geen tweede volledige telling.

| Reeks | Zoekopdracht(en) | Resultaten | Objecten met bevestigde renovatie-/nieuwbouwclaim (allemaal al in de originele reeks) | Onafh. mediaan | Orig. | Afwijking |
|---|---|---|---|---|---|---|
| `villa_renovated` | "villa renovada en El Rafalet, Jávea" (7) · "… Pinomar - Pinosol …, entre 600.000 y 2.000.000" (29) · "… La Lluca - Tarraula …, entre 700.000 y 2.000.000" (25) | 61 | Rafalet: 108153256 (6.878), 111909291/111064307 (3.602) · Pinosol: 109645331 (3.216), 110668828 (6.391), 112329948 (4.554) · La Lluca: 112509325/110843020 (4.986), 110676663 (3.873), 110765633 (4.238) → **n = 8** | **4.396** (3.216–6.878) | 4.807 | **−8,5 %** ✔ |
| `villa_new` | "villa de nueva construcción en Pinomar - Pinosol, Jávea" (1) + nieuwbouw die in de Rafalet/Pinosol-renovatiezoekopdracht meekwam | — | 112515850 (9.750), 111718472 (8.250), 106823897 (5.717), 112165476/112422911 (3.560), 111918606/110831782 (3.297 op 330 m²) → **n = 5** | **5.717** | 5.717 | **0 %** ✔ |
| `villa_renovated_tosal` | "villa renovada en Partida Tosal - Zona dels Castellans, Jávea" (15) | 15 | 112504358/112512860/112469782 (7.500), 107385205 (3.176) → **n = 2** | **5.338** | 4.726 | **+13 %** (binnen ±15 %, maar n = 2) |
| `villa_new_tosal` | "villa de nueva construcción en Partida Tosal …" (1) | 1 | 111928138 (6.848) | 6.848 | 6.848 | 0 % ✔ |

Nieuwe objecten in de onafhankelijke set die **niet** in het origineel staan, zijn allemaal terecht afwezig: geen enkele heeft een renovatie- of nieuwbouwclaim in de tekst (gecontroleerd: 110105556, 111970788, 111916747, 112454356, 112278142/112189339, 110773851 — tekst zegt Adsubia —, 112544882 — tekst zegt Cansalades —, 111725571, 111947244, 106990380, 111773506, 112271843, 109644424, 112517043). 111284532 zegt "potencial de modernización" (renovatieobject, terecht buiten de reeks). 83667869 (Tosal, 720.000 / 805 m²) zegt alleen dat de zwembadzone in 2020 is gerenoveerd — terecht uitgesloten.

---

## 4. Controle 3 — Verkeerd ingedeelde objecten en dubbele advertenties

**Renovatieobjecten ("para reformar") in de gerenoveerde reeks:** geen gevonden. De uitsluitingslijst in §9 van het origineel is consistent met wat de zoekresultaten van vandaag laten zien.

**Nieuwbouw in de gerenoveerde reeks — één grensgeval:** 110895902 (Pinosol, 1.675.000 €, 182 m², 9.203 €/m²). Feiten uit `property_detail`: veld "Construido en 2026", "producto desarrollado y ofrecido exclusivamente por [ontwikkelaar]", "se vende sujeta al IVA español en lugar del ITP", energielabel A. Een verkoop onder IVA betekent dat de fiscus dit als een eerste levering door een ontwikkelaar ziet (nieuwbouw of ingrijpende rehabilitatie). Het is de bovenste waarde van de reeks. Het origineel houdt het in `villa_renovated` en meldt de bijzonderheid in §8.6. Dat is verdedigbaar, maar voor het dossier is het zuiverder dit object als **ontwikkelaarsrenovatie / nieuw product** apart te zetten. Effect: `villa_renovated` n = 19, mediaan **4.760**, p25 4.056, p75 5.662, max 7.510 (−1 % op de mediaan, p75-max verandert wel).

**Nog-niet-gerenoveerd in de gerenoveerde reeks:** 112509325 (La Lluca, 4.986) is per tekst nog in renovatie/uitbreiding, oplevering eind november. Het origineel meldt dit (§4 en §8.5). Weglaten geeft mediaan 4.760 (n = 19). Geen correctie nodig, wel een reden om dit object niet als bewijs van een gerealiseerde renovatieprijs te gebruiken.

**Twijfelgeval in `villa_new`:** 112527650 (Pinomar, 950.000 €, 180 m², 5.278). Het veld zegt 2026, maar beide advertenties van hetzelfde object zeggen "tradicional villa … bien cuidada" resp. "la construcción es joven" zonder jaar; garage al omgebouwd; label G; status "Segunda mano/buen estado". Er is geen bewijs dat dit een nieuwbouwvilla is. Het origineel noemt dit zelf het zwakste geval. **Advies:** buiten `villa_new` houden totdat een bouwjaar is bevestigd. Effect: `villa_new` n = 8, mediaan **6.107**.

**Inconsequente "op plan"-regel in `villa_new (zonder op plan)`:** uitgesloten zijn 112093850 (niets gebouwd), 111718472 (14 maanden na start) en 112158635 (juni 2027). **Niet** uitgesloten is 111656885 met "Finalización marzo de 2027" en afwerking nog te kiezen — dat is dezelfde categorie als 112158635. Consequent toegepast ("oplevering ná vandaag = op plan/in aanbouw, niet opgeleverd"):

| Variant | Objecten | n | min | p25 | mediaan | p75 | max |
|---|---|---|---|---|---|---|---|
| origineel "zonder op plan" | 111918606, 112527650, 106823897, 111656885, 112165476, 112515850 | 6 | 3.307 | 3.637 | 4.573 | 5.607 | 9.750 |
| **gecorrigeerd** (ook zonder 111656885) | 111918606, 112527650, 106823897, 112165476, 112515850 | **5** | 3.307 | 3.560 | **5.278** | 5.717 | 9.750 |
| strikt (ook zonder twijfelgeval 112527650) | 111918606, 106823897, 112165476, 112515850 | 4 | 3.307 | 3.497 | 4.638 | 6.725 | 9.750 |

Let op: 111918606 ("lista en marzo de 2026", nog steeds notFinished) en 106823897 ("fase final", > 1 jaar niet bijgewerkt) zijn óók niet aantoonbaar opgeleverd. Een reeks "opgeleverde nieuwbouw" bestaat in deze zone feitelijk niet; alles is in aanbouw, op plan of van onbekende status.

**Dubbele advertenties:** gecontroleerd in de zoekresultaten van vandaag. Hetzelfde object komt inderdaad meervoudig voor en is in het origineel steeds als één geteld: Pinosol 1.685.000 / 370 m² (112329948, 112158285, 112158272, 112156107), La Lluca 1.495.000 / 386 m² (110676663, 111225638, 110694600, 111485403), La Lluca 1.795.000 (112509325 360 m² / 110843020 359 m²), Rafalet 850.000 (111909291 236 m² / 111064307 270 m²), Rafalet 1.088.000 (111918606 329 m² / 110831782 330 m²), Pinosol 1.495.000 / 420 m² (112165476 / 112422911), Tosal 2.250.000 / 300 m² (112504358 / 112512860 / 112469782), Pinomar 950.000 / 180 m² (112527650 / 112462622). Niet in de reeks maar ook netjes gebundeld: Pinosol 1.650.000 / 437 m² (3×), Pinosol 1.685.000 / 262 m² (2×), La Lluca 995.000 / 300 m² (4×), Tosal 1.395.000 / 405 m² (2×). **Geen dubbele telling gevonden.**

**Prijshistorie die het origineel mist:** de dubbele advertentie 111064307 van de Rafalet-villa van 850.000 € toont in de tool een **eerdere prijs van 1.495.000 € (−43 %)**. Het origineel zegt bij §8.1 dat er geen prijsdaling is, alleen een andere aanbieding met bouwperceel (1.299.000 €). Beide kunnen waar zijn (de 1.495.000 was vermoedelijk de prijs met perceel), maar het is een sterk onderhandelingssignaal dat in het dossier van K08 thuishoort. [te verifiëren bij de aanbieder]

---

## 5. Controle 4 — Rekenkunde

Herberekend in Python (lineaire interpolatie, afronding op hele euro's) op de 20 + 9 + 6 + 1 waarden uit de tabellen van het origineel. **Alle** waarden in §3 van het origineel komen exact overeen:

| Reeks | n | min | p25 | mediaan | p75 | max | Klopt |
|---|---|---|---|---|---|---|---|
| `villa_renovated` | 20 | 3.190 | 4.147 | 4.807 | 5.845 | 9.203 | ✔ |
| `villa_renovated (zonder 2 fincas)` | 18 | 3.190 | 4.250 | 4.807 | 5.662 | 9.203 | ✔ |
| `villa_new` | 9 | 3.307 | 3.868 | 5.717 | 8.185 | 9.750 | ✔ |
| `villa_new (zonder op plan)` | 6 | 3.307 | 3.637 | 4.573 | 5.607 | 9.750 | ✔ (rekenkundig; indeling zie §4) |
| `villa_renovated_tosal` | 6 | 3.176 | 3.869 | 4.726 | 6.897 | 9.342 | ✔ |
| `villa_new_tosal` | 1 | 6.848 | — | 6.848 | — | 6.848 | ✔ |
| Rafalet / Pinosol / La Lluca | 5 / 7 / 8 | — | — | 5.660 / 4.760 / 4.546 | — | — | ✔ |

Ook de €/m²-waarden per object (prijs ÷ m²) kloppen alle 36 met het `priceByArea`-veld van de tool.

---

## 6. Wat er wél aan schort (voor het dossier, niet als correctie op de reeks)

1. **De subreeks "nieuwbouw zonder op plan" is de enige aantoonbare fout** (inconsequente regel); lees **5.278 (n = 5)** of erken dat opgeleverde nieuwbouw in deze zone niet in de tool zit.
2. **Energielabel G bij "volledig gerenoveerde" villa's** (112229028, 111452530, 111952972, 112310283) en bij de "contemporaine" 111433078: dit is de standaardwaarde als de aanbieder niets invult, maar het betekent ook dat de renovatieclaim niet door een certificaat wordt gedragen. Pas bij een concreet dossier het echte CEE opvragen.
3. **Drie "gerenoveerd/modern"-prijzen zijn ontwikkelaars- of nog-niet-klare producten** (110895902 onder IVA, 108153256 "nueva construcción", 112509325 in renovatie). Ze trekken de bovenkant van de reeks op. De mediaan is er robuust tegen (4.760–4.807), de p75 en max niet.
4. **Onafhankelijke controle van Tosal is dun** (2 van 6 teruggevonden). De reeks `villa_renovated_tosal` staat rekenkundig, maar de zoekgevoeligheid van de tool (chalet vs. villa) laat zien dat de dekking per zoekopdracht sterk wisselt. Voor een herhaalbare meting: altijd "chalet" gebruiken, nooit "villa", en de prijsbanden vasthouden.
5. **Alle cijfers blijven vraagprijzen.** Zichtbare prijsdalingen in de tool vandaag: 111952972 −5 %, 111064307 −43 % (dubbel van 111909291). Transactieprijzen zijn nergens in deze reeksen aanwezig.

---

## 7. Uitgevoerde tool-aanroepen (log, 15-09-2026)

`property_detail` (24×): 111452530, 111909291, 110895902, 112310283, 111229059, 112509325, 108153256, 111952972, 111918606, 112527650, 112093850, 106823897, 112165476, 112515850, 110753189, 107385205, 111361293, 111433078, 111928138, 112462622, 111656885, 109546138, 112229028, 112504358.
`search_properties` (6×, CHALET, SALE, maxResults 50, es-ES/es): "villa renovada en El Rafalet, Jávea" (7 / 7) · "villa renovada en Pinomar - Pinosol, Jávea, entre 600.000 y 2.000.000 euros" (29 / 29) · "villa renovada en La Lluca - Tarraula, Jávea, entre 700.000 y 2.000.000 euros" (25 / 25) · "villa de nueva construcción en Pinomar - Pinosol, Jávea" (1 / 1) · "villa renovada en Partida Tosal - Zona dels Castellans, Jávea" (15 / 15) · "villa de nueva construcción en Partida Tosal - Zona dels Castellans, Jávea" (1 / 1).
Rekenscript en ruwe zoekuitvoer: sessie-scratchpad `h01v/` (tijdelijk). Geen telefoonnummers, makelaarsnamen of sleutels overgenomen.

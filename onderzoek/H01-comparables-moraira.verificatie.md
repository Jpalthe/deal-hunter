# Verificatie H01 — Vergelijkingsprijzen Moraira / Teulada

**Gecontroleerd bestand:** `onderzoek/H01-comparables-moraira.md` (zone_key `moraira`)
**Rol:** tegenspreker · **controledatum:** 15-09-2026 · **bron:** officiële Idealista-assistent (MCP `property_detail` 12×, `search_properties` 5×), locale es-ES, country es, SALE, maxResults 50
**Let op:** alle bedragen zijn **vraagprijzen** van lopende advertenties op 15-09-2026. Het zijn geen transactieprijzen en geen marktwaarde. Het originele bestand is **niet** gewijzigd. Alleen de vijf reeksen die de rekenaar gebruikt zijn gecontroleerd.

---

## 1. Oordelen

| Reeks | n | p25 / mediaan / p75 (origineel) | Oordeel | Toelichting in één regel |
|---|---|---|---|---|
| `villa_renovated` | 20 | 4.184 / **4.641** / 5.859 | **BEVESTIGD** | 3 van 3 detailfiches kloppen, de rekenkunde klopt en een onafhankelijke zoekopdracht geeft een mediaan van 4.668 (+0,6 %). Er ontbreekt één object (112302765); dat verschuift de mediaan maar met +0,6 %. |
| `villa_renovated (kern)` | 18 | 3.904 / **4.580** / 5.006 | **BEVESTIGD** | De rekenkunde klopt. Onafhankelijk zonder eerstelijnsobjecten: 4.661 (+1,8 %). |
| `villa_new` | 44 | 4.283 / **5.112** / 6.546 | **BEVESTIGD** | 3 van 3 fiches kloppen en de rekenkunde klopt. Onafhankelijke inventaris (39 advertenties) na opschoning: mediaan **5.112** (0,0 %). Er ontbreken vier advertenties; met die vier erbij blijft de mediaan 5.112. |
| `villa_new (kern)` | 38 | 4.720 / **5.141** / 6.584 | **BEVESTIGD** | De rekenkunde klopt. Met de drie ontbrekende objecten die niet als uitschieter gelden: 5.135. |
| `apartment_renovated` | 5 | 3.571 / **4.350** / 4.622 | **BEVESTIGD** (grensgeval) | 3 van 3 fiches kloppen. Onafhankelijke mediaan 4.096 (−5,8 %, n = 4). n = 5 zit precies op de grens en de kwartielen zijn indicatief. Het zwakste object is 109771748 ("modernizado"); zonder dat object is n = 4 en daarmee te klein voor een betrouwbare mediaan. |
| `apartment_new` | 0 | — (in de tabel "0") | **BEVESTIGD** (n = 0) | Een onafhankelijke zoekopdracht met het obra-nueva-filter levert 0 resultaten op. **Er is geen mediaan.** De nullen in de tabel zijn plaatshouders en geen prijs: de rekenaar moet deze reeks als ontbrekend behandelen. |
| `townhouse_renovated` | 4 | 2.040 / **2.326** / 2.468 | **BEVESTIGD**, maar **te klein voor een betrouwbare mediaan** | 3 van 3 fiches kloppen. De onafhankelijke zoekopdracht vindt exact dezelfde 4 objecten (mediaan 2.326, 0,0 %). Bij n = 4 is de reeks alleen indicatief. De reeks gaat over de casco van **Teulada**, niet over Moraira zelf. |

**Netto voor Jan:** de hoofdcijfers staan overeind. Een gerenoveerde villa in Moraira vraagt ±4.600 €/m² gebouwd, een nieuwbouwvilla ±5.100 €/m² en een gerenoveerd appartement ±4.350 €/m² (n = 5, dun). Voor dorpshuizen in de casco van Teulada (±2.300 €/m²) en voor nieuwbouwappartementen (geen aanbod) is er geen betrouwbare referentie.

---

## 2. Controle 1 — `property_detail` op voorbeelden (goedkoopste, duurste en een middenobject)

Alle 12 opgevraagde objecten zijn actief. Prijs en m² gebouwd komen **exact** overeen met het originele bestand, en `priceByArea` van de tool is gelijk aan de €/m² in het bestand.

| Reeks | Code (rol) | Prijs / m² gebouwd (tool) | €/m² | Status fiche | Wat de tekst zegt | Oordeel |
|---|---|---|---|---|---|---|
| villa_renovated | 111142549 (goedkoopste) | 915.000 / 321 | 2.850 | good, geen bouwjaar | "villa de lujo, recientemente renovada"; de >60 m² grote benedenverdieping moet nog tot appartement worden omgebouwd | gerenoveerd ✔ (de 321 m² bevat onafgewerkte ruimte, wat de lage €/m² verklaart) |
| villa_renovated | 111568858 (midden) | 895.000 / 207 | 4.324 | good, gebouwd 1980 | "fue reformada en 2014" | gerenoveerd ✔ |
| villa_renovated | 105615749 (duurste) | 5.400.000 / 360 | 15.000 | good, fiche "Construido en 2024" | "Completamente renovada en 2024", eerste lijn El Portet | gerenoveerd ✔ (fiche en tekst spreken elkaar tegen, net als bij 109301382) |
| villa_new | 109248610 (goedkoopste) | 2.085.000 / 756 | 2.758 | newdevelopment, promotie "notFinished" | The White Collection; fiche: 756 m² gebouwd / **246 m² útil** | nieuwbouw ✔ (de fiche noemt geen kelder; "incl. kelder" in het origineel is een interpretatie van de m²-kloof) |
| villa_new | 111996460 (midden) | 1.965.000 / 385 | 5.104 | newdevelopment, "notFinished" | Benimeit-Tabaira, villa contemporánea, kelder 165 m² in de tekst | nieuwbouw ✔ |
| villa_new | 110514198 (duurste) | 8.800.000 / 831 | 10.590 | newdevelopment, "notFinished" | "residencia de nueva construcción", eerste lijn op klif | nieuwbouw ✔ (terecht als uitschieter uit de kern gehaald) |
| apartment_renovated | 112097940 (goedkoopste) | 274.500 / 82 | 3.348 | good, gebouwd 1979 | "completamente reformado en 2020" | gerenoveerd ✔ |
| apartment_renovated | 110104344 (mediaan) | 261.000 / 60 | 4.350 | good, gebouwd 1975 | "Moderno y completamente renovado" | gerenoveerd ✔ |
| apartment_renovated | 109771748 (duurste) | 295.000 / 54 | 5.463 | good, gebouwd 1983 | alleen "apartamento modernizado", geen jaar en geen "completamente" | ✔ maar de **zwakste claim** in de reeks; valt strikt genomen buiten de eigen definitie ("expliciet geheel gerenoveerd") |
| townhouse_renovated | 111996463 (goedkoopste) | 255.000 / 160 | 1.594 | good, gebouwd 1900 | "renovada en su totalidad" | gerenoveerd ✔ |
| townhouse_renovated | 112332296 (midden) | 299.900 / 137 | 2.189 | good | "casa adosada renovada"; prijsverlaging van 325.000 (−8 %) klopt | gerenoveerd ✔ |
| townhouse_renovated | 109952365 (duurste) | 340.000 / 137 | 2.482 | good, gebouwd 1900 | "completamente modernizada" | gerenoveerd ✔ |

Geen van de gecontroleerde objecten heeft status `renew` of "para reformar".

---

## 3. Controle 2 — één onafhankelijke zoekopdracht per reeks

| Reeks | Query (door de tool toegepast filter) | total / opgehaald | Wat telt (tekst expliciet, ontdubbeld) | n | Mediaan | Afwijking t.o.v. origineel |
|---|---|---|---|---|---|---|
| villa_renovated | "chalet independiente renovado en Moraira, Alicante", CHALET (Moraira · chalets independientes · usada/buen estado) | 378 / 50 | 105965027≡108986148 (2.836), 112056687 (4.461), 108536057≡108919992-groep (4.654), 112526858 (4.668), **112302765 (5.842)**, 111621178≡111084437 (7.237), 105615749 (15.000) | 7 | **4.668** | +0,6 % ✔ |
| — variant | idem, plus grensgeval 106244503 (El Portet eerste lijn, 2.500.000 / 174 = 14.368; "el interior ha sido renovado") | | | 8 | 5.255 | +13,2 % ✔ (nog binnen ±15 %) |
| — kern | zonder 105615749 | | | 6 | 4.661 | +1,8 % t.o.v. 4.580 ✔ |
| villa_new | "casas de obra nueva en Moraira, Alicante", CHALET (Moraira · casas y chalets · obra nueva) | 39 / 39 | alle 39 behalve 111596570 (casco, verworpen), 108642432 (datafout, verworpen) en 108587629 (dubbel van 112547722) | 36 | **5.112** | 0,0 % ✔ (ongeschoond, n = 39: 4.921, −3,7 %) |
| apartment_renovated | "piso completamente reformado en Moraira, Alicante", HOME (Moraira · pisos/áticos/dúplex · usada/buen estado) | 62 / 50 | 112097940 (3.348), 111298766 (3.571), 111656724≡111959253 (4.622), 109771748 (5.463). 110104344 zat niet bij de 50 opgehaalde. | 4 | **4.096** | −5,8 % ✔ |
| apartment_new | "pisos y apartamentos de obra nueva en Moraira, Alicante", HOME (Moraira · pisos · obra nueva) | 0 / 0 | — | 0 | — | n = 0 bevestigd |
| townhouse_renovated | poging 1: "casa de pueblo renovada en el centro de Teulada, Alicante" → door de tool gegeocodeerd als **Centro, Alicante-stad**, verworpen | 11 / 11 | — | — | — | onbruikbaar (bekende geocodeervalkuil) |
| townhouse_renovated | poging 2: "casas adosadas y casas de pueblo en Teulada, Alicante", HOME (Teulada · casas y chalets, geen staatfilter) | 93 / 50 | casco (±38,727–38,731 N / 0,100–0,105 O), tekst expliciet: 111996463 (1.594), 112332296 (2.189), 112298899 (2.464), 109952365 (2.482) | 4 | **2.326** | 0,0 % ✔ (zelfde 4 objecten; 110736204 terecht uitgesloten wegens renovatie in 2002) |

**Kanttekeningen bij de zoekopdrachten**
- Zoekresultaten tonen de advertentietekst soms ingekort (tot ±3.900 tekens). Een renovatievermelding verderop in de tekst kan dus gemist zijn. De onafhankelijke sets zijn daarom een ondergrens.
- **Dekking villa_renovated.** Het origineel noemt 217 villa's in "buen estado" en ±63 % daarvan gezien. Met het bredere filter "chalets independientes" staan er 378 advertenties. De werkelijke dekking van het aanbod is dus lager dan 63 %. Dat maakt de reeks niet fout, maar ontbrekende objecten zoals 112302765 zijn te verwachten.
- Bij townhouse_renovated zijn 43 van de 93 Teulada-advertenties niet gezien. Het origineel meldt wel dat #21 (adosados) volledig bekeken is.

---

## 4. Controle 3 — deduplicatie en rekenkunde

**Rekenkunde:** alle €/m² (prijs / m² gebouwd) en alle p25/mediaan/p75 (lineaire interpolatie, PERCENTILE.INC) zijn herberekend op de voorbeeldlijsten. Ze kloppen **exact** voor alle zes reeksen/varianten:

| Reeks | n | p25 | mediaan | p75 | min | max |
|---|---|---|---|---|---|---|
| villa_renovated | 20 | 4.184 | 4.641 | 5.859 | 2.850 | 15.000 |
| villa_renovated (kern) | 18 | 3.904 | 4.580 | 5.006 | 2.850 | 7.237 |
| villa_new | 44 | 4.283 | 5.112 | 6.546 | 2.758 | 10.590 |
| villa_new (kern) | 38 | 4.720 | 5.141 | 6.584 | 3.824 | 8.723 |
| apartment_renovated | 5 | 3.571 | 4.350 | 4.622 | 3.348 | 5.463 |
| townhouse_renovated | 4 | 2.040 | 2.326 | 2.468 | 1.594 | 2.482 |

**Deduplicatie:** in geen enkele reeks komen twee rijen met dezelfde prijs én dezelfde m² voor. De bekende dubbele advertenties staan in de kolom "Dubbel" en zijn één keer geteld (111013342-groep, 108919992-groep, 111621178/111084437, 106691029-groep, 111720175/111813480, 112547722/108587629, 111959253/111656724/111958559). Bij deze controle vond ik nog **drie extra dubbele codes** die niet in het origineel staan. Geen daarvan wordt dubbel geteld, dus de statistiek verandert niet:
- 108986148 (1.500.000 / 529 m², El Portet, "Completamente renovada"): hetzelfde object als de 111013342-groep.
- 111564038 (915.000 / 321 m², Moravit-Cap Blanc): zelfde prijs en m² als 111142549 (Villa Alegría). Waarschijnlijk hetzelfde huis via een makelaar (perceel 960 tegenover 906 m²).
- 108252332 (280.000 / 160 m², Teulada casco): zelfde prijs en m² als 110736204. Staat buiten de reeks.

Camino de Benimeit 17 (110763617: 1.650.000 / 420 m² en 108682286: 2.450.000 / 520 m²) is terecht níet samengevoegd: prijs en m² verschillen, dus volgens de eigen regel zijn het twee objecten.

---

## 5. Ontbrekende objecten (informatief, geen weerlegging)

| Reeks | Code | Prijs / m² | €/m² | Waarom relevant | Effect als toegevoegd |
|---|---|---|---|---|---|
| villa_renovated | 112302765 | 1.145.000 / 196 | 5.842 | Benimeit, "villa mediterránea reformada … completamente renovada" (geen jaar; valt binnen de eigen regel) | n = 21: p25 4.324 · **mediaan 4.668** · p75 5.842. Kern n = 19: 4.044 · **4.614** · 5.394 (p75 kern +7,8 %) |
| villa_renovated | 106244503 | 2.500.000 / 174 | 14.368 | eerste lijn El Portet, alleen "el interior ha sido renovado" | grensgeval; zou net als de twee strandvilla's een uitschieter buiten de kern zijn |
| villa_new | 109462611 | 1.800.000 / 466 | 3.863 | Benimeit, "villa de nueva construcción" | — |
| villa_new | 108183806 | 800.000 / 190 | 4.211 | Benimeit, promotie "desde 800.000 €" (tekst: ±210 m²) | — |
| villa_new | 111905357 | 1.490.000 / 187 | 7.968 | Moravit-Cap Blanc, "villa de obra nueva" | — |
| villa_new | 112549978 | 4.250.000 / 350 | 12.143 | Moravit-Cap Blanc (Ctra. Moraira-Calpe), obra nueva | alle vier erbij, n = 48: p25 4.223 · **mediaan 5.112** · p75 6.618. Kern + de eerste drie, n = 41: 4.691 · **5.135** · 6.602 |

Het origineel noemt query #12 (filter "villas · obra nueva", 35 advertenties) de "volledige inventaris". Met het filter "casas y chalets · obra nueva" staan er vandaag 39. Het verschil zit in het typefilter en verandert de mediaan niet.

---

## 6. Wat de rekenaar hiermee moet doen

1. `villa_renovated` en `villa_new`: medianen zijn bruikbaar zoals gerapporteerd. De kernvarianten zijn de betere verkoopreferentie; dat zegt het origineel ook.
2. `apartment_renovated`: bruikbaar, met een waarschuwing. Bij n = 5 hangt de mediaan af van één zwak geclassificeerd object (109771748).
3. `apartment_new`: **niet gebruiken**. Er is geen aanbod en dus geen mediaan. De "0" in de tabel is geen prijs.
4. `townhouse_renovated`: **te klein voor een betrouwbare mediaan** (n = 4) en geografisch Teulada-casco. Alleen als indicatie gebruiken, niet als verkoopreferentie voor Moraira.
5. Alles blijft vraagprijs. Voor nieuwbouw geldt meestal "exclusief 10 % btw + AJD" (bij 111640774 expliciet vermeld). Dat is een kanttekening uit het origineel die hier niet opnieuw is gecontroleerd.

Geen telefoonnummers, namen van particulieren of sleutels overgenomen. Ruwe tool-uitvoer staat alleen in de sessiemap, niet in het project.

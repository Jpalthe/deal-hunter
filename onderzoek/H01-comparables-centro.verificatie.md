# H01: tegenspraak op de vergelijkingsprijzen zone `centro`

**Gecontroleerd bestand:** `onderzoek/H01-comparables-centro.md`. De cijfers daarin zijn niet aangepast.
**Rol:** tegenspreker. **Controledatum:** 15-09-2026.
**Bron:** officiële Idealista-assistent (MCP `property_detail` en `search_properties`, locale es-ES, country es, SALE, maxResults 50). Bewijstype 1: toolresultaat, letterlijk gelezen.
**Omvang:** alleen de vijf reeksen die de rekenaar gebruikt: villa_renovated, villa_new, apartment_renovated, apartment_new en townhouse_renovated. townhouse_new is niet gecontroleerd.

> Alle bedragen zijn **vraagprijzen** en geen transactieprijzen. €/m² is steeds de vraagprijs gedeeld door `size` (m² gebouwd) zoals de tool die geeft. Contactgegevens van aanbieders zijn niet overgenomen.

## 1. Oordelentabel

| Reeks (origineel) | Oordeel | Onderbouwing (kort) | Gevoeligheid / gecorrigeerd |
|---|---|---|---|
| **townhouse_renovated** (n 8 · p25 2.674 · mediaan 2.872 · p75 3.316) | **Bevestigd** | Met `property_detail` 3 van de 8 geopend: het goedkoopste (110212994), het duurste (112149106) en 112029927. Bij alle drie klopt de m² en staat er een expliciete renovatieclaim. Eén prijs is vandaag gewijzigd: 112149106 kost nu 599.000 in plaats van 595.000 (3.993 in plaats van 3.967 €/m²). Alleen het maximum verschuift daardoor; p25, mediaan en p75 blijven gelijk. De onafhankelijke zoekopdracht vond 7 van de 8 objecten terug, met een mediaan van 2.730 (−4,9 %). De rekenkunde klopt exact. | max 3.993 in plaats van 3.967. Verder niets. |
| **villa_renovated** (n 6 · p25 3.071 · mediaan 3.531 · p75 4.063) | **Bevestigd, met kanttekening** | 3 van de 6 geopend: het goedkoopste (111936571), het duurste (107009337) en het zwakst onderbouwde object (111536032). Prijs en m² kloppen bij alle drie. 111936571 is "completamente renovada" en 107009337 is "Construido en 2013". Bij 111536032 staat **geen bouwjaar en geen renovatieclaim**, alleen "villa contemporánea". Volgens de eigen definitie van het origineel hoort dat object er dus niet in. De onafhankelijke zoekopdrachten leveren maar 2 geschikte villa's op, met een mediaan van 3.422 (−3,1 %). De rekenkunde klopt exact. | Strikt volgens de definitie: **n 5 · p25 2.941 · mediaan 3.460 · p75 3.602** (−2,0 %). |
| **villa_new** (n 1 · 6.781) | **Bevestigd als feit, onbruikbaar als reeks** | Het ene object (111672511) is geopend: 1.980.000 / 292 m² / 6.781 €/m², "villa de obra nueva", "Construido en 2025". Een onafhankelijke zoekopdracht op villa's met obra nueva in Centro Ciudad geeft **0** treffers, net als in het origineel. **Te klein voor een betrouwbare mediaan.** Het is bovendien vrijwel zeker **hetzelfde huis** als 111938184 (en waarschijnlijk 111080148), dat in `montgo_ermita` al in villa_new meetelt. Daarover meer in §4. | Geen centro-mediaan opvoeren. |
| **apartment_renovated** (n 9 · p25 3.631 · mediaan 4.008 · p75 5.443) | **Bevestigd, met kanttekening** | 3 van de 9 geopend: het goedkoopste (111574952, "Construido en 2023"), het duurste (109777059, "Construido en 2024") en 109854808. Prijs en m² kloppen. 109854808 is **nog niet gerenoveerd**: de renovatie loopt en moet volgens de advertentie in september 2026 klaar zijn. Ook 111771483 heeft volgens het origineel zelf geen bouwjaar. Onafhankelijk vond ik 3 geschikte objecten, met een mediaan van 4.392 (+9,6 %, binnen ±15 %). De rekenkunde klopt exact. | Zonder 109854808: n 8 · mediaan 4.200 (+4,8 %). Strikt, ook zonder 111771483: **n 7 · p25 3.632 · mediaan 4.392 · p75 5.667** (+9,6 %). |
| **apartment_new** (n 50 · p25 3.436 · mediaan 3.620 · p75 4.132) | **Bevestigd, exact** | 3 van de 50 geopend: het goedkoopste (111479225), het duurste (111705285) en 112539584. Prijs, m² en status kloppen: twee keer `newdevelopment` / `notFinished` en één keer "Construido en 2026", nog in aanbouw. De onafhankelijke zoekopdracht gaf 49 objecten met een mediaan van 3.629 (+0,2 %). Samen met de twee objecten die deze filter mist en zonder één dubbel kom ik op dezelfde 50 uit, met **exact** p25 3.436, mediaan 3.620 en p75 4.132. De uitsplitsing per promotie klopt ook bij de twee promoties die ik heb nagerekend. | Mogelijke dubbel 111928252 / 112539584 weglaten: mediaan 3.625. Verwaarloosbaar. |

**Kern:** alle vijf reeksen kloppen met wat de tool vandaag laat zien. Wat niet deugt, zit niet in de rekenkunde maar in de dunne onderbouwing. **villa_new heeft voor centro geen bruikbare waarde**: het is één huis, en dat huis telt al mee in Montgó–Ermita. **villa_renovated** rust op 5 à 6 objecten. **apartment_renovated** komt bij een strikte definitie ongeveer 10 % hoger uit (4.392). **townhouse_renovated**, de reeks die voor K01, K02, K13 en K14 het meest telt, is stevig: 7 van de 8 objecten kwamen onafhankelijk terug.

## 2. Controle 1: `property_detail` op de voorbeelden (13 objecten)

| Reeks | Code | In de tool: prijs / m² / €/m² | Klopt met origineel | Staat volgens de tool | Oordeel |
|---|---|---|---|---|---|
| townhouse_renovated | 110212994 (goedkoopst) | 765.000 / 321 / 2.383; "Construido en 1957"; label E | ja | "bellamente renovada", "Renovada con esmero"; centro histórico, C/ Roques | gerenoveerd ✔ |
| townhouse_renovated | 112149106 (duurst) | **599.000** / 150 / **3.993**; 146 m² útiles; label D; advertentie "hace 46 minutos" bijgewerkt | prijs **nee** (origineel 595.000 / 3.967), m² ja | "completamente renovada en 2026", casco antiguo, licencia turística | gerenoveerd ✔; prijs is vandaag verhoogd |
| townhouse_renovated | 112029927 | 285.000 / 106 / 2.689; was 310.000 (−8 %); label C | ja | "totalmente reformada", "Reforma integral con acabados actuales"; C/ de la Coma 2 | gerenoveerd ✔ |
| villa_renovated | 111936571 (goedkoopst) | 820.000 / 346 / 2.370; perceel 734 m²; label G | ja | "completamente renovada", Senioles | gerenoveerd ✔ (label G) |
| villa_renovated | 107009337 (duurst) | 850.000 / 190 / 4.474; perceel 995 m² | ja | "Construido en 2013", Piver; de tekst zegt 200 m², de tool 190 | modern (≥ 2005) ✔ |
| villa_renovated | 111536032 (zwakst) | 1.400.000 / 332 / 4.217; 290 m² útiles; label C; advertentie "más de 3 meses" oud | ja | "villa contemporánea", Piver; **geen bouwjaar, geen renovatieclaim** | **voldoet niet aan de eigen definitie** (renovatie óf bouwjaar ≥ 2005) |
| villa_new | 111672511 (enig object) | 1.980.000 / 292 / 6.781; perceel 1.500 m²; label A | ja | status `good` (tweedehands), tekst "villa de obra nueva", "Construido en 2025"; El Garroferal, "a 3 km del centro urbano"; gastenappartement op het onderste niveau, garage | nieuwbouw ✔; ligt buiten het dorp; zie §4 |
| apartment_renovated | 111574952 (goedkoopst) | 620.000 / 235 / 2.638; 115 m² útiles; label G (382,6 kWh/m²·jaar) | ja | "Construido en 2023", Essential, ático dúplex, dakterras 120 m² | recent ✔; €/m² gedrukt door het terras |
| apartment_renovated | 109777059 (duurst) | 540.000 / 69 / 7.826; label B | ja | "Construido en 2024", C/ Castellet, 3e verdieping | recent ✔; uitschieter (69 m²) |
| apartment_renovated | 109854808 | 255.000 / 64 / 3.984; label C | ja | "Construido en 2000"; "en proceso de reforma integral", klaar naar verwachting september 2026 | **nog niet gerenoveerd**; randgeval |
| apartment_new | 111479225 (goedkoopst) | 528.500 / 188 / 2.811 | ja | `newdevelopment`, promotie Natura Beach Xàbia, `notFinished`; energielabel "del proyecto" | nieuwbouw ✔ |
| apartment_new | 111705285 (duurst) | 548.500 / 85 / 6.453 | ja | `newdevelopment`, Natura Beach, `notFinished`; tekst: terras 25 m² + **privétuin 181 m²** | nieuwbouw ✔; €/m² opgedreven door de tuin, die niet in `size` zit |
| apartment_new | 112539584 | 428.000 / 129 / 3.318; label G | ja | status `good`, maar "Construido en 2026" en "actualmente en construcción", 9 woningen, rand van het centro histórico | nieuwbouw ✔ (in aanbouw) |

Bij alle 13 objecten is de `priceByArea` van de tool gelijk aan vraagprijs / `size`. Geen van de 13 is "para reformar".

## 3. Controle 2: onafhankelijke zoekopdrachten

| # | Query (letterlijk) | Filter waar Idealista op uitkwam | Treffers (`total` / opgehaald) | URL |
|---|---|---|---|---|
| S1 | casa de pueblo renovada en Centro Ciudad, Jávea/Xàbia, Alicante (CHALET) | casas y chalets · buen estado | 101 / 50 | https://www.idealista.com/es/venta-viviendas/javeaxabia/centro-ciudad/con-chalets,buen-estado/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_list |
| S2 | villa con piscina completamente renovada en Centro Ciudad, Jávea/Xàbia, Alicante (CHALET) | villas · buen estado · piscina | 11 / 11 | https://www.idealista.com/es/venta-viviendas/javeaxabia/centro-ciudad/con-villa,piscina,buen-estado/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_list |
| S3 | villa de obra nueva en Centro Ciudad, Jávea/Xàbia, Alicante (CHALET) | villas · obra nueva | **0** / 0 | https://www.idealista.com/es/venta-viviendas/javeaxabia/centro-ciudad/con-villa,obra-nueva/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_list |
| S4 | apartamento reformado o de construcción reciente en Centro Ciudad, Jávea/Xàbia, Alicante (HOME) | pisos, áticos, dúplex · obra nueva **+** buen estado | 171 / 50 | https://www.idealista.com/es/venta-viviendas/javeaxabia/centro-ciudad/con-pisos,obra-nueva,buen-estado/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_list |
| S5 | pisos y áticos de obra nueva en Centro Ciudad, Jávea/Xàbia, Alicante (HOME) | pisos, áticos · obra nueva | 49 / 49 | https://www.idealista.com/es/venta-viviendas/javeaxabia/centro-ciudad/con-solo-pisos,aticos,obra-nueva/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_list |

Ik heb de resultaten zelf ingedeeld volgens de definities van het origineel (§2.2 daar). Per reeks:

- **townhouse_renovated (S1).** Onder de 50 opgehaalde chalets van de 101 staan 7 unieke gerenoveerde casco-huizen: 110212994, 112029927 (+ dubbel 111821811), 112501218, 112342304 (+ dubbel 111542413), 111260725, 112281781 en 112149106. Dat is de lijst van het origineel zonder 111473433, dat ik in deze helft niet tegenkwam. De mediaan is **2.730 (−4,9 %)** en valt binnen ±15 %. Terecht buiten beschouwing gebleven: twee hotels in de casco (110749062, 109165181), huizen "que requiere renovación" of met "necesita modernización" (109619126 / 111388848, 111137854) en de drie advertenties van K02 (112342283, 112205878, 110900124). Het origineel noemt ze niet, maar ze vallen ook buiten zijn definitie: twee adosados uit 2019 met "sin necesidad de reformas" en zonder renovatieclaim (112497565, 625.000 / 179 m² = 3.492; 112554733, 625.000 / 254 m² = 2.461). Die objecten liggen in een kleine urbanisatie vlak bij het centrum en niet in de casco.
- **villa_renovated (S2 + S1).** S2 levert na toepassing van de definitie maar één villa op: 111936571, samen met dubbel 111473645 (zelfde prijs, zelfde m², pergola en gastenhuis). De rest valt af. 112262137 (Montgó), 108630311 (Cap Martí, 1982), 112233839 (Cap Martí) en 111401357 hebben geen renovatieclaim of bouwjaar ≥ 2005. 109974326 heeft geen bouwjaar en 112277619 / 112342304 zijn casco-huizen. S1 voegt 107009337 toe (2013). Op die twee is de mediaan **3.422 (−3,1 %)**. Neem ik ook 106375115 mee (Cansalades, gebouwd 2009, maar de m² spreken elkaar tegen), dan wordt het 3.233 (−8,4 %). Dat valt binnen ±15 %, maar met n = 2–3 is dit een zwakke controle. De overige 51 chalets van de 101 heb ik niet opgehaald (zuinig gewerkt).
- **villa_new (S3).** 0 treffers, in overeenstemming met het origineel. Het ene object staat bij Idealista als tweedehands en verscheen in S2 (tweedehands villa's).
- **apartment_renovated (S4).** De tool mengde nieuwbouw erdoor: van de 50 zijn er 33 obra nueva. Onder de tweedehands appartementen voldoen er 3 aan de definitie: 111051168 (2019, 4.392), 108606753 (2023, 3.255) en 112319877 (Essential, 5.891). De mediaan is **4.392 (+9,6 %)** en valt binnen ±15 %. Buiten de definitie vallen onder meer 111918833 (casco, 2006), 112443965 (geen claim), 109801825 ("requiere renovación") en 112342260 (Arenal, geen jaar). 110289135 (C.ª Cabo de la Nao Pla, 415.000 / 76 m² = 5.461) heeft dezelfde complexvoorzieningen als 109777059, maar geen bouwjaar in de zoektekst. Dat object heb ik niet geopend.
- **apartment_new (S5).** 49 objecten, mediaan **3.629 (+0,2 %)**. Per promotie komen de aantallen overeen met het origineel: Jávea Garden 15, Serestar 11, Natura Beach 5, Blooming Village 5, Palmela 6 (origineel 5, zie §4), Rei Juan Carlos I 6 (origineel 7) en "Apartamentos en Jávea" 1 (origineel 2). S5 mist 109912036 (dúplex, 555.000 / 177 m² = 3.136, wel gezien in S4) en 112539584 (tweedehands gelabeld). Met die twee erbij en zonder 112372811 kom ik op **exact** de 50 van het origineel: n 50 · min 2.811 · p25 3.436 · mediaan 3.620 · p75 4.132 · max 6.453. Nagerekend per promotie: Palmela (5) mediaan 3.911 ✔ en Rei Juan Carlos I (7) mediaan 4.181 ✔.

## 4. Controle 3: ontdubbeling en rekenkunde

**Rekenkunde.** Op de voorbeeldlijsten van townhouse_renovated (8), villa_renovated (6), villa_new (1) en apartment_renovated (9) heb ik min, p25, mediaan, p75 en max nagerekend met lineaire interpolatie. Alle vier de rijen van de conclusietabel kloppen tot op de euro, en ook elke €/m² per rij. Bij apartment_new staan maar 8 van de 50 objecten in het bestand, dus daar kon ik niet op de voorbeeldlijst rekenen. Via de reconstructie uit S4 + S5 (§3) kwamen de cijfers wel exact uit.

**Ontdubbeling.**

| Geval | Bevinding |
|---|---|
| 112029927 = 111821811 (285.000 / 106) | Beide in S1, zelfde tekst. Eén keer geteld ✔ |
| 112342304 = 111542413 (1.990.000 / 729) | Beide in S1 en S2, zelfde casa señorial (1.134 m² volgens Catastro). Eén keer geteld ✔ |
| 111936571 = 111473645 (820.000 / 346) | Beide in S2, zelfde huis (pergola, gastenhuis, Senioles). Eén keer geteld ✔. 112075070 (795.000 / 346, Comunes-Adsubia/Senioles, zelfde tekst) staat in S1. Het origineel noemt het als lagere vraagprijs van hetzelfde huis ✔ |
| K02 onder 112342283 / 112205878 / 110900124 (499.000 / 264) | Alle drie in S1. Niet in een reeks ✔ |
| 112372503 / 112372811 (Palmela, ático 650.000 / 102) | Het origineel telt er één, volgens de regel "zelfde prijs + zelfde m²". Het kunnen ook twee gespiegelde penthouses in dezelfde promotie zijn. Niet te beslissen; het effect op de mediaan is 0 |
| 111928252 (428.000 / 125) en 112539584 (428.000 / 129) | Zelfde project van 9 woningen, zelfde prijs, andere m². Het origineel telt beide. **Mogelijk een dubbel** [te verifiëren]. Zonder 112539584 is de mediaan 3.625 (+0,1 %) |
| **villa_new 111672511 ↔ montgo_ermita 111938184 (en 111080148)** | **Dubbel over twee zones heen.** 111672511 (centro) en 111938184 (montgo_ermita) hebben dezelfde prijs (1.980.000), dezelfde m² (292), dezelfde €/m² (6.781), hetzelfde perceel (1.500 m²), dezelfde wijk (El Garroferal) en in beide advertenties een gastenappartement op het onderste niveau. De verificatie van montgo_ermita acht 111938184 = 111080148 al waarschijnlijk. De centro-reeks villa_new bestaat dus uit een huis dat in Montgó–Ermita al meetelt. De tekst plaatst het bovendien "a 3 km del centro urbano". [te verifiëren bij de aanbieders] |
| 110212994 = 111816211 | Door het origineel genoemd; 111816211 kwam ik in S1 niet tegen. Niet gecontroleerd |

## 5. Wat dit betekent voor de rekenaar

1. **townhouse_renovated** (mediaan 2.872) kan blijven staan. Het is de enige reeks die echt uit de casco antiguo komt en hij houdt stand. Houd de gevoeligheid in het oog die het origineel zelf noemt: met zes huizen in "buen estado" zonder renovatieclaim erbij zakt de mediaan naar ongeveer 2.660.
2. **villa_renovated** (3.531) is bruikbaar als orde van grootte. De strikte variant is 3.460 bij n = 5. Het verschil is klein, maar de onafhankelijke controle rust op maar 2–3 objecten.
3. **villa_new** heeft voor `centro` **geen eigen waarde**: n = 1, **te klein voor een betrouwbare mediaan**, en het is een dubbel met montgo_ermita. Gebruik voor centro geen 6.781 als nieuwbouwvilla-referentie. Markeer de waarde als ONBEKEND of verwijs expliciet naar de reeks van Montgó–Ermita.
4. **apartment_renovated** (4.008) ligt eerder aan de lage kant. Strikt volgens de eigen definitie is het 4.392. Beide vallen binnen ±15 % van elkaar. Geen van deze appartementen ligt in de casco, dus voor de splitsing van K13 en K14 blijft het een referentie buiten de casco (dat meldt het origineel ook).
5. **apartment_new** (3.620) is exact reproduceerbaar. Twee kanttekeningen blijven: de tool zegt niet of de btw in de prijs zit, en bij begane-grondwoningen van Natura Beach telt de privétuin niet mee in `size`.
6. Alles hierboven zijn vraagprijzen van 15-09-2026. **[te verifiëren]** met transactieprijzen.

## 6. Bronnen `property_detail` (15-09-2026)

- https://www.idealista.com/es/inmueble/110212994/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail
- https://www.idealista.com/es/inmueble/112149106/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail
- https://www.idealista.com/es/inmueble/112029927/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail
- https://www.idealista.com/es/inmueble/111936571/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail
- https://www.idealista.com/es/inmueble/107009337/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail
- https://www.idealista.com/es/inmueble/111536032/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail
- https://www.idealista.com/es/inmueble/111672511/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail
- https://www.idealista.com/es/inmueble/111574952/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail
- https://www.idealista.com/es/inmueble/109777059/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail
- https://www.idealista.com/es/inmueble/109854808/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail
- https://www.idealista.com/es/inmueble/111479225/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail
- https://www.idealista.com/es/inmueble/111705285/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail
- https://www.idealista.com/es/inmueble/112539584/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail

De ruwe tooluitvoer van S1, S4 en S5 staat in de sessie-scratchpad en niet in de repo. De berekeningen staan in `centro_arith.py` en `centro_check2.py`, ook in de scratchpad.

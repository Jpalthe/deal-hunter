# H01 — Vergelijkingsprijzen Centro Ciudad / casco antiguo (Jávea)

**Zone-sleutel:** `centro` · **Datum van de meting:** 15-09-2026 · **Bron:** officiële Idealista-assistent (MCP; `search_properties` en `property_detail`, locale es-ES, country es, operation SALE, maxResults 50) · **Dient voor kandidaten:** K01, K02, K13, K14 (alle vier "para reformar" in de casco antiguo; gegevens uit `kader/kandidaten.json`).

> **Lees dit eerst.** Alle bedragen zijn **vraagprijzen** zoals ze op 15-09-2026 op Idealista stonden — geen transactieprijzen. "m² gebouwd" is het getal dat de tool geeft (`size`); bij appartementen en áticos zit daar soms een groot terras in, wat de €/m² drukt. De statistiek is een berekening op een kleine steekproef; p25/p75 zijn lineair geïnterpoleerd. Het Idealista-district **"Centro Ciudad" is breder dan de casco antiguo**: het bevat ook de villapartidas rond het dorp (Senioles, Piver, Comunes-Adsubia, Cansalades, Cap Martí, Garroferal) en de nieuwbouwgordel richting de haven, én objecten die de tekst elders plaatst (Rafalet, Tosalet, Granadella, Arenal, Cabo San Antonio, Calpe). Per object staat daarom wat de tekst zelf over de ligging zegt. Dit bestand vervangt de versie van 09:41 van dezelfde dag (nieuwe meting, zelfde methode; oude versie bewaard in de sessie-scratchpad).

## 1. Conclusie in één oogopslag

| Reeks | Definitie (kort) | n | min €/m² | p25 | mediaan | p75 | max |
|---|---|---|---|---|---|---|---|
| **townhouse_renovated** | dorpshuis/adosado/casa señorial in casco of centrum, expliciet gerenoveerd/gerestaureerd | 8 | 2.383 | 2.674 | 2.872 | 3.316 | 3.967 |
| **villa_renovated** | vrijstaande villa in district Centro Ciudad, expliciet gerenoveerd óf gebouwd ≥ 2005 | 6 | 2.370 | 3.071 | 3.531 | 4.063 | 4.474 |
| **villa_new** | villa obra nueva in district Centro Ciudad — **n = 1, geen reeks** | 1 | 6.781 | 6.781 | 6.781 | 6.781 | 6.781 |
| **townhouse_new** | adosado obra nueva (Blooming Village) — **n = 3, minder dan 6** | 3 | 3.551 | 3.674 | 3.797 | 3.818 | 3.839 |
| **apartment_renovated** | appartement gebouwd ≥ 2015 of integraal gerenoveerd; ligt in de gordel dorp–haven, niet in de casco | 9 | 2.638 | 3.631 | 4.008 | 5.443 | 7.826 |
| **apartment_new** | appartement obra nueva, alle promoties in district Centro Ciudad | 50 | 2.811 | 3.436 | 3.620 | 4.132 | 6.453 |

**Wat dit zegt voor K01, K02, K13 en K14.** De vier kandidaten vragen 1.068–1.890 €/m² gebouwd. Gerenoveerde dorpshuizen in de casco vragen 2.383–3.967 €/m² (mediaan 2.872). Het verschil is de **bruto** ruimte per m² voor aankoopkosten, renovatie, architect, vergunning, marge en onderhandeling — vóór aftrek van alles en gerekend met vraagprijzen aan beide kanten.

| Kandidaat | Code | Vraagprijs € | m² gebouwd | €/m² | Verschil met mediaan townhouse_renovated (2.872) | Verschil met p25 (2.674) |
|---|---|---|---|---|---|---|
| K01 | 108910753 | 399.000 | 232 | 1.720 | 1.152 | 954 |
| K02 | 110974608 | 499.000 | 264 | 1.890 | 982 | 784 |
| K13 | 111439256 | 520.000 | 487 | 1.068 | 1.804 | 1.606 |
| K14 | 108456665 | 650.000 | 434 | 1.498 | 1.374 | 1.176 |

- De bovenkant van de reeks (3.750–3.967 €/m²) zijn kleine, volledig gerenoveerde huizen van 140–150 m² met dakterras en/of licencia turística (111473433, 112149106). Grote huizen (321–729 m²) zitten aan de onderkant (2.383–2.730 €/m²): m² boven de ±250 worden in de casco minder betaald.
- Voor K13 en K14 (splitsing in meerdere woningen) is `apartment_renovated` (mediaan 4.008) en `apartment_new` (mediaan 3.620) de referentie, maar met een grote kanttekening: die appartementen liggen in nieuwbouwcomplexen met lift, zwembad en garage in de gordel dorp–haven, niet in de casco. De enige casco-appartementen in de steekproef zonder renovatieclaim vragen 3.702 €/m² (112443965/112498840/112498774, 104 m², 3e verdieping met lift, "buen estado") en 4.342 €/m² (111918833, complex uit 2006 in de casco antiguo).
- K02 staat onder drie codes in deze meting (112342283, 112205878, 110900124: 499.000 / 264 m²) en K01 onder 110967853 (399.000 / 232 m²). Beide zijn uit alle reeksen gehouden.
- **[te verifiëren]** met werkelijke verkoopprijzen (Registradores / notariaat / makelaarsopgave) zodra beschikbaar; dit zijn uitsluitend vraagprijzen.

## 2. Werkwijze

### 2.1 Zoekopdrachten (alle: locale es-ES, country es, SALE, maxResults 50)

De tool negeert vrije tekst grotendeels en zet de query om in een structurele filter (district + typologie + staat). "Jávea centro histórico / casco antiguo" wordt **verkeerd gegeocodeerd naar Málaga**; "Centro Ciudad, Jávea/Xàbia" werkt wel. De tool geeft maximaal 50 resultaten zonder paginering; daarom is de chalet-inventaris op prijsband gesplitst.

| # | Query | propertyType | Door de tool toegepast filter | `total` | Opgehaald | Gebruik |
|---|---|---|---|---|---|---|
| 1 | chalet reformado en Jávea centro histórico casco antiguo | CHALET | Centro Histórico, **Málaga** | 5 | 5 | verworpen |
| 2 | casa de pueblo reformada en Jávea centro histórico casco antiguo | HOME | Centro Histórico, **Málaga** | 5 | 5 | verworpen |
| 3 | obra nueva en Jávea centro histórico casco antiguo | HOME | promociones Centro Histórico, **Málaga** | 3 | 3 | verworpen |
| 4 | villa moderna reformada en Jávea centro ciudad | CHALET | Centro Ciudad, Jávea/Xàbia · villas · buen estado | 11 | 11 | villa_renovated |
| 5 | chalet reformado en Centro Ciudad, Jávea/Xàbia, Alicante, hasta 600.000 euros | CHALET | casas y chalets · < 600.000 · buen estado | 24 | 24 | alle reeksen |
| 6 | idem, entre 600.000 y 1.000.000 euros | CHALET | idem · 600.000–1.000.000 | 40 | 40 | alle reeksen |
| 7 | idem, más de 1.000.000 euros | CHALET | idem · > 1.000.000 | 37 | 37 | alle reeksen (5+6+7 = **101 = volledige inventaris**) |
| 8 | chalet de obra nueva a estrenar en Centro Ciudad, Jávea/Xàbia, Alicante | CHALET | casas y chalets · obra nueva | 3 | 3 | townhouse_new |
| 9 | casa de pueblo reformada en Centro Ciudad, Jávea/Xàbia, Alicante | HOME | casas y chalets · buen estado (vrije tekst genegeerd) | 101 | 50 | controle op 5–7 |
| 10 | casa adosada reformada en Centro Ciudad, Jávea/Xàbia, Alicante | HOME | chalets adosados · buen estado | 13 | 13 | townhouse_renovated |
| 11 | piso reformado en Centro Ciudad, Jávea/Xàbia, Alicante | HOME | pisos, áticos, dúplex · buen estado | 127 | 50 | apartment_renovated (steekproef, niet volledig) |
| 12 | piso de obra nueva a estrenar en Centro Ciudad, Jávea/Xàbia, Alicante | HOME | pisos, áticos, dúplex · obra nueva | 50 | 50 | apartment_new (volledig) |
| 13 | villa a estrenar de nueva construcción en Centro Ciudad, Jávea/Xàbia, Alicante | CHALET | villas · obra nueva | **0** | 0 | villa_new |

### 2.2 Classificatie en rekenregels

- **Gerenoveerd** = de advertentietekst of `property_detail` zegt letterlijk reformada/renovada/restaurada/rehabilitada (integraal, niet alleen "cocina renovada"), óf geeft een bouwjaar ≥ 2005 (villa's) / ≥ 2015 (appartementen). "Buen estado" alleen telt niet. "Para reformar", "necesita modernización", "requiere renovación" en "proyecto" zijn uitgesloten. Hotels, hostels en albergues zijn uitgesloten (ander product).
- **Nieuw** = `isNewDevelopment`/"Promoción de obra nueva", of tekst + `property_detail` met "obra nueva"/"Construido en 2025/2026".
- **Zone**: Idealista-district Centro Ciudad, met per object de ligging uit de tekst. Villa's die de tekst buiten het centrum en zijn partidas plaatst, zijn uit de kernreeks gehaald (§5).
- **€/m²** = vraagprijs / m² gebouwd (`size`), afgerond op hele euro's. Objecten zonder m² zijn overgeslagen (de zeven obra-nueva-promotiepagina's uit query 3 en de verworpen Málaga-resultaten spelen geen rol).
- **Deduplicatie**: zelfde prijs + zelfde m² in hetzelfde district = één object; de andere codes staan in de toelichting. Bij 111936571 (820.000) en 112075070 (795.000) gaat het aantoonbaar om hetzelfde huis met twee prijzen; geteld als één object tegen 820.000 (drie van de vier advertenties), de lagere vraagprijs staat erbij.
- **Percentielen**: lineaire interpolatie tussen gesorteerde waarden (bij n = 1 zijn alle percentielen gelijk aan de waarde).
- **Bevestiging**: `property_detail` op 36 objecten (12 dorpshuizen, 8 villa's, 1 villa nieuw, 3 adosados nieuw, 6 appartementen gerenoveerd, 6 appartementen nieuw). Rijen met "(detail)" zijn zo bevestigd; rijen met "(tekst)" komen uit de zoekresultaten.

## 3. Reeks townhouse_renovated — gerenoveerde dorpshuizen casco/centrum

Dorpshuis / casa adosada / casa señorial in de casco antiguo of het centrum van Jávea, waarvan de advertentietekst of `property_detail` expliciet zegt dat het gerenoveerd, gerestaureerd of integraal verbouwd is. Casco-huizen "para reformar", hotels/hostels en de kandidaten zelf zijn uitgesloten.

**n = 8 · min 2.383 · p25 2.674 · mediaan 2.872 · p75 3.316 · max 3.967 €/m²**

| Code | Vraagprijs € | m² geb. | €/m² | Bouwjaar / staat | Toelichting | URL |
|---|---|---|---|---|---|---|
| 112281781 | 348.900 | 110 | 3.172 | 1960, renovada 2025 | Casa de pueblo, hart van Jávea; property_detail: "Construido en 1960", tekst "renovada en 2025"; label E | https://www.idealista.com/es/inmueble/112281781/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 112149106 | 595.000 | 150 | 3.967 | renovada 2026 | Casa de pueblo casco antiguo, "completamente renovada en 2026", licencia turística; label D (detail) | https://www.idealista.com/es/inmueble/112149106/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 111473433 | 525.000 | 140 | 3.750 | onbekend | Casa adosada casco antiguo, "totalmente renovada a un alto nivel", 3 lagen (detail) | https://www.idealista.com/es/inmueble/111473433/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 112029927 | 285.000 | 106 | 2.689 | onbekend | C/ de la Coma 2, casa de pueblo, "reforma integral con acabados actuales"; label C (detail; dubbel 111821811) | https://www.idealista.com/es/inmueble/112029927/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 110212994 | 765.000 | 321 | 2.383 | 1957 | C/ Roques, centro histórico, "bellamente renovada", gastenhuis 2 slk (detail; dubbel 111816211) | https://www.idealista.com/es/inmueble/110212994/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 112501218 | 620.000 | 236 | 2.627 | reformada 2018 | Casa de pueblo de lujo, centrum, "reformada en 2018", patio met zwembad, vloerverwarming (detail) | https://www.idealista.com/es/inmueble/112501218/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 111260725 | 995.000 | 330 | 3.015 | 1960 | Casco antiguo, 4 lagen, "meticulosamente reinventada" met architect, "renovación de alta calidad" (detail) | https://www.idealista.com/es/inmueble/111260725/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 112342304 | 1.990.000 | 729 | 2.730 | onbekend | Casa señorial casco antiguo (Portal del Clot), "restauración… con especial respeto", patio+zwembad+garage; 1.134 m² totaal volgens kadaster, 729 m² hoofdwoning (detail; dubbel 111542413) | https://www.idealista.com/es/inmueble/112342304/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |

Niet opgenomen, maar wel gezien (casco, "buen estado", zonder aantoonbare renovatie): 112277619 (C/ Major, 1.600.000 / 746 m² = 2.145 €/m², gebouwd 1957, "excelente estado de conservación", patio met zwembad, garage); 110940495 (749.000 / 250 m² = 2.996, gebouwd 1970, "diseñada con esmero… moderna cocina"); 112480897 (C/ En Finestrat, 280.000 / 110 m² = 2.545, gebouwd 1840, "comodidades modernas", label F); 108293796 (285.000 / 108 m² = 2.639, licencia turística); 99233578 (800.000 / 400 m² = 2.000, casa señorial, geen renovatieclaim); 98488973 (480.000 / 194 m² = 2.474, Placeta del Convent, oud bedrijfspand). Zou je die zes tóch meetellen, dan zakt de mediaan naar ca. 2.660 €/m² — de reeks is dus gevoelig voor de definitie.

## 4. Reeks villa_renovated — gerenoveerde of moderne villa's

Vrijstaande villa in het Idealista-district Centro Ciudad waarvan de tekst/`property_detail` een volledige renovatie noemt óf een bouwjaar ≥ 2005 geeft, en die volgens de tekst in het centrum of een aangrenzende partida ligt (Senioles, Piver, Comunes, Cansalades). Villa's die de tekst in Rafalet, Tosalet, Granadella, Arenal, Cabo San Antonio of Calpe plaatst, zijn uitgesloten (zie §5).

**n = 6 · min 2.370 · p25 3.071 · mediaan 3.531 · p75 4.063 · max 4.474 €/m²**

| Code | Vraagprijs € | m² geb. | €/m² | Bouwjaar / staat | Toelichting | URL |
|---|---|---|---|---|---|---|
| 111936571 | 820.000 | 346 | 2.370 | onbekend (renovada) | Senioles, "completamente renovada", gastenapp., perceel 734 m² (detail; dubbels 111473645/111225913; 112075070 vraagt 795.000 = 2.298 €/m²) | https://www.idealista.com/es/inmueble/111936571/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 112284489 | 850.000 | 236 | 3.602 | reformada 2024 | "Completamente reformada en 2024", 6 slk, perceel 1.210 m², zwembad (detail) | https://www.idealista.com/es/inmueble/112284489/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 107009337 | 850.000 | 190 | 4.474 | 2013 | Piver, "Construido en 2013", gelijkvloers, perceel 995 m², verwarmd zwembad (detail) | https://www.idealista.com/es/inmueble/107009337/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 111672497 | 750.000 | 255 | 2.941 | 2009 | "Construido en 2009", perceel 1.037 m², zwembad (detail) | https://www.idealista.com/es/inmueble/111672497/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 107770973 | 519.000 | 150 | 3.460 | 1975 (reformada) | "Villa reformada", landelijk tussen sinaasappelvelden, perceel 1.414 m², 1 badkamer; label G (detail) — jaar van de reforma onbekend | https://www.idealista.com/es/inmueble/107770973/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 111536032 | 1.400.000 | 332 | 4.217 | onbekend (contemporánea, label C) | Piver, "villa contemporánea… arquitectura moderna", vloerverwarming + zonnepanelen, zeezicht (detail) — geen bouwjaar; zwakste bewijs van de reeks | https://www.idealista.com/es/inmueble/111536032/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |

Zonder het zwakst bewezen object (111536032) is de mediaan 3.460 €/m² (n = 5). Niet opgenomen, wel gezien in het district: 109974326 (1.315.000 / 450 m² = 2.922, "materiales sostenibles", geen bouwjaar, label G); 111375418 (1.745.000 / 200 m² = 8.725, "estética moderna", geen bouwjaar, label G); 110782663 / 112175270 (hetzelfde huis voor 990.000 én 1.200.000, 269 m², alleen keuken gerenoveerd, perceel 4.008 m²); 106375115 (750.000, tekst zegt 152 m² gebouwd, tool zegt 232 m² — tegenstrijdig, overgeslagen).

## 5. Reeks villa_new en townhouse_new — nieuwbouw

**villa_new — n = 1, geen reeks.** Vrijstaande villa obra nueva / a estrenar in het district Centro Ciudad. De obra-nueva-filter van de tool op "villas" geeft 0 resultaten; dit ene object staat als tweedehands gelabeld maar is volgens tekst en `property_detail` nieuwbouw.

| Code | Vraagprijs € | m² geb. | €/m² | Bouwjaar / staat | Toelichting | URL |
|---|---|---|---|---|---|---|
| 111672511 | 1.980.000 | 292 | 6.781 | 2025 | El Garroferal (zuidflank Montgó, "3 km del centro urbano"), "villa de obra nueva", "Construido en 2025", label A, gastenapp. (detail) | https://www.idealista.com/es/inmueble/111672511/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |

**townhouse_new — n = 3 (minder dan 6).** Adosado obra nueva in het district Centro Ciudad (alle drie in de promotie Blooming Village, C/ José de Espronceda 2, promotie "niet afgerond").

**min 3.551 · mediaan 3.797 · max 3.839 €/m²**

| Code | Vraagprijs € | m² geb. | €/m² | Bouwjaar / staat | Toelichting | URL |
|---|---|---|---|---|---|---|
| 109710781 | 696.000 | 196 | 3.551 | obra nueva (niet afgerond) | Blooming Village, adosado 4 slk, kelder 66 m², label A-project (detail) | https://www.idealista.com/es/obra-nueva/109710781/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 111031699 | 691.000 | 182 | 3.797 | obra nueva (niet afgerond) | Blooming Village, adosado 4 slk, parkeerplaats inbegrepen (detail) | https://www.idealista.com/es/obra-nueva/111031699/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 110314601 | 595.000 | 155 | 3.839 | obra nueva (niet afgerond) | Blooming Village, adosado 4 slk, 140 m² útiles (detail) | https://www.idealista.com/es/obra-nueva/110314601/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |

Villa's die de tool onder Centro Ciudad zet maar die volgens de tekst elders liggen (niet meegeteld, ter oriëntatie): 108485037 Rafalet, "completamente renovada en los últimos tres años", 895.000 / 299 m² = 2.993; 110976637 Granadella, "completamente renovada", 2.625.000 / 400 m² = 6.562; 111208179 Tarraula, finca 10.103 m², "totalmente renovada en 2025", 3.950.000 / 526 m² = 7.510; 111635459 Tosalet (alleen keuken), 610.000 / 166 m² = 3.675; 112155396 / 111518003 ibicenco 1,1 km van Arenal, 1.250.000 / 260 m² = 4.808; 106796760 nieuwbouw in **Calpe**, 1.550.000 / 350 m² = 4.441; 111057788 Cabo San Antonio, 1.790.000 / 350 m² = 5.114; 112157322 Tosalet, 2.050.000 / 606 m² = 3.383.

## 6. Reeks apartment_renovated — recente/gerenoveerde appartementen

Tweedehands appartement in het district Centro Ciudad met bouwjaar ≥ 2015 (tekst of `property_detail`) of een expliciete integrale renovatie. Let op: géén van deze objecten ligt in de casco antiguo zelf; ze liggen in de nieuwe gordel tussen het dorp en de haven (UNIC, Essential, Trenc d'Alba, Av. Rei Juan Carlos I).

**n = 9 · min 2.638 · p25 3.631 · mediaan 4.008 · p75 5.443 · max 7.826 €/m²**

| Code | Vraagprijs € | m² geb. | €/m² | Bouwjaar / staat | Toelichting | URL |
|---|---|---|---|---|---|---|
| 111051168 | 650.000 | 148 | 4.392 | 2019 | Ático dúplex "Haya", "Construido en 2019"; 148 m² gebouwd waarvan 87 m² woning (tekst) — €/m² gedrukt door terras | https://www.idealista.com/es/inmueble/111051168/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 108606753 | 485.000 | 149 | 3.255 | 2023 | Av. Trenc d'Alba, "construida en 2023", tussen casco en haven, gemeubileerd (tekst) | https://www.idealista.com/es/inmueble/108606753/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 107684589 | 529.000 | 132 | 4.008 | 2023 | Essential, "Construido en 2023", label B, garage (tekst) | https://www.idealista.com/es/inmueble/107684589/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 111771483 | 512.000 | 141 | 3.631 | onbekend (label A) | UNIC III, "residencial contemporáneo", aerotermia, label A; 99 m² útiles; geen bouwjaar in detail | https://www.idealista.com/es/inmueble/111771483/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 111575229 | 430.000 | 79 | 5.443 | 2025 | UNIC, C/ Castellet 6, "Construido en 2025", label B (detail) | https://www.idealista.com/es/inmueble/111575229/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 109777059 | 540.000 | 69 | 7.826 | 2024 | C/ Castellet, modern complex tussen haven en casco, "Construido en 2024" (detail) | https://www.idealista.com/es/inmueble/109777059/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 112319877 | 595.000 | 101 | 5.891 | 2023 | Essential, ático dúplex, "Construido en 2023", solárium 97 m², zeezicht (detail; dubbel 112518530) | https://www.idealista.com/es/inmueble/112319877/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 111574952 | 620.000 | 235 | 2.638 | 2023 | Essential (Taylor Wimpey), ático dúplex, "Construido en 2023"; 235 m² gebouwd, 115 m² útiles, dakterras 120 m² (detail) — €/m² sterk gedrukt door terras | https://www.idealista.com/es/inmueble/111574952/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 109854808 | 255.000 | 64 | 3.984 | 2000, reforma integral (oplevering sept. 2026) | C/ Thiviers, 1 slk, "en proceso de reforma integral", label C (detail) — verkocht als gerenoveerd, nog niet klaar | https://www.idealista.com/es/inmueble/109854808/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |

De spreiding is groot omdat `size` bij áticos het dakterras meetelt (111574952: 235 m² gebouwd, 115 m² útiles) en kleine units in UNIC/Castellet per m² veel duurder zijn (5.443–7.826). Op basis van m² útiles waar de tool die geeft: 111574952 → 5.391 €/m², 111771483 → 5.172 €/m², 112319877 → 6.919 €/m². Query 11 haalde 50 van 127 "buen estado"-appartementen op; de reeks is een steekproef, geen inventaris. Casco-referenties buiten de reeks: 111918833 (495.000 / 114 m² = 4.342, complex uit 2006 in de casco antiguo, zwembad) en 112443965 (385.000 / 104 m² = 3.702, casco histórico, lift, geen renovatieclaim).

## 7. Reeks apartment_new — nieuwbouwappartementen

Appartementen obra nueva in het district Centro Ciudad (filter "Obra nueva" van de tool, 50 van 50 opgehaald, plus één in aanbouw dat als tweedehands gelabeld staat). Promoties: Residencial Living Jávea (Av. Palmela, 20 won.), Natura Beach Xàbia (C/ Garcilaso de la Vega 8, 36 won.), Serestar Jávea (C/ Arquitecte Urteaga 2, 85 won., "centro histórico", licentie verleend), Blooming Village (C/ José de Espronceda 2), Jávea Garden (C/ Historiador Palau 23, 72 won.), Av. Rei Juan Carlos I s/n (7 eenheden, naam niet opgevraagd), "Apartamentos en Jávea" (9 won.). Alle prijzen exclusief btw-vermelding tenzij de tekst anders zegt.

**n = 50 · min 2.811 · p25 3.436 · mediaan 3.620 · p75 4.132 · max 6.453 €/m²**

Per promotie (€/m² gebouwd): Jávea Garden, C/ Historiador Palau 23 — n 15, 3.112–3.629, mediaan 3.530 · Serestar Jávea, C/ Arquitecte Urteaga 2 ("centro histórico", licentie verleend, start bouw) — n 11, 3.366–4.168, mediaan 3.696 · Av. Rei Juan Carlos I s/n — n 7, 3.136–5.725, mediaan 4.181 · Residencial Living Jávea, Av. Palmela — n 5, 3.377–6.373, mediaan 3.911 · Natura Beach Xàbia, C/ Garcilaso de la Vega 8 — n 5, 2.811–6.453, mediaan 4.004 · Blooming Village, C/ José de Espronceda 2 — n 5, 3.372–5.269, mediaan 4.313 · "Apartamentos en Jávea" (9 won., rand centro histórico, oplevering zomer 2026) — 3.318–3.424.

Voorbeelden (8 van 50, gespreid over de promoties en de bandbreedte):

| Code | Vraagprijs € | m² geb. | €/m² | Bouwjaar / staat | Toelichting | URL |
|---|---|---|---|---|---|---|
| 112372503 | 650.000 | 102 | 6.373 | obra nueva | Ático en Avenida de Palmela & Carrer del Tenista David Ferrer s/n | https://www.idealista.com/es/obra-nueva/112372503/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 112503269 | 362.300 | 95 | 3.814 | obra nueva | Piso en Calle Arquitecte Urteaga, 2 | https://www.idealista.com/es/obra-nueva/112503269/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 111705285 | 548.500 | 85 | 6.453 | obra nueva | Piso en Calle garcilaso de la vega, 8 | https://www.idealista.com/es/obra-nueva/111705285/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 111479225 | 528.500 | 188 | 2.811 | obra nueva | Piso en Calle garcilaso de la vega, 8 | https://www.idealista.com/es/obra-nueva/111479225/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 108918177 | 498.000 | 129 | 3.860 | obra nueva | Piso en Calle José de Espronceda, 2 | https://www.idealista.com/es/obra-nueva/108918177/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 111059780 | 351.000 | 100 | 3.510 | obra nueva | Piso en Calle de l'Historiador Palau, 23 | https://www.idealista.com/es/obra-nueva/111059780/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 109912037 | 512.000 | 99 | 5.172 | obra nueva | Piso en Avenida Rei Juan Carlos I s/n | https://www.idealista.com/es/obra-nueva/109912037/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 112539584 | 428.000 | 129 | 3.318 | 2026 (in aanbouw) | 9 woningen, rand centro histórico, "Construido en 2026", 2e-hands gelabeld (detail) — zelfde project als 111928252 | https://www.idealista.com/es/inmueble/112539584/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |

Kanttekening: bij nieuwbouw komt 10 % btw + AJD bovenop de vraagprijs, terwijl bij de tweedehands reeksen ITP geldt; de tool vermeldt niet consequent of de btw in de prijs zit (bij de Málaga-resultaten stond expliciet "IVA no incluido"; bij deze Jávea-promoties staat er niets over).

## 8. Kanttekeningen

1. **Vraagprijzen, geen transacties.** Alles hierboven is een vraagprijs op 15-09-2026. Onderhandelingsmarges in Jávea zijn niet uit deze bron af te leiden. Verschillende advertenties van hetzelfde huis met verschillende prijzen (111936571 vs 112075070; 110782663 vs 112175270) laten zien dat de vraagprijs zelf al zacht is.
2. **Steekproef.** townhouse_renovated n = 8, villa_renovated n = 6 (waarvan één met zwak bewijs), villa_new n = 1, townhouse_new n = 3. Alleen apartment_new (n = 50) is een volledige inventaris. Eén object erbij of eraf verschuift de mediaan van de kleine reeksen met honderden euro's per m².
3. **Zonelabels.** Het district "Centro Ciudad" van Idealista is geen casco antiguo. Van de 101 chalets in het district liggen er volgens de tekst hooguit ±25 in de casco of het directe centrum; de rest is villapartida of foutief gelabeld. Coördinaten van de tool zijn vervaagd (privacy) en niet bruikbaar als controle.
4. **m² gebouwd.** De tool geeft één getal; bij áticos en dorpshuizen met dakterras zit het terras erin. Kadastrale oppervlakten zijn niet opgevraagd; alleen 112342304 noemt zelf het kadaster (1.134 m² totaal tegenover 729 m² in de advertentie).
5. **Staat.** "Buen estado" is een aanbiedersfilter, geen keuring. Energielabels G bij "totalmente renovada" (111473433, 111260725) zijn een signaal dat "gerenoveerd" niet altijd "geïsoleerd" betekent; bij een verkoopcalculatie voor K01–K14 moet je zelf definiëren wat de opgeleverde staat is.
6. **Tool-gedrag.** Vrije tekst wordt vrijwel genegeerd; "centro histórico"/"casco antiguo" geocodeert naar Málaga; geen paginering (max 50), dus grote sets alleen via prijsbanden; `total` geeft wel de echte omvang van de set.
7. **Geen telefoonnummers of contactgegevens overgenomen**; alleen codes en de letterlijke URL's van de tool.

## 9. Bronbestanden van deze meting

Ruwe tool-uitvoer (JSON, sessie-scratchpad, niet in de repo): `chalet_lt600.json`, `chalet_600_1000.json`, `chalet_gt1000.json`, `pueblo.json`, `piso_ref.json`, `piso_new.json`; classificatie en cijfers in `series_final.json`. Verwerking met `parse.py`, `excerpt.py`, `build.py`, `write_md.py`. Kandidaatgegevens uit `/Users/root-admin/tree-es/deal-hunter/kader/kandidaten.json`.

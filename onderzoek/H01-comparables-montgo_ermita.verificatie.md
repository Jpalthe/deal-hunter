# H01 — Tegenspraak op de vergelijkingsprijzen zone `montgo_ermita`

**Gecontroleerd bestand:** `onderzoek/H01-comparables-montgo_ermita.md` (cijfers daarin niet aangepast).  
**Rol:** tegenspreker. **Controledatum: 15-09-2026.** Bron: officiële Idealista-assistent (MCP `property_detail` + `search_properties`, Spanje, es-ES); bewijstype 1 (toolresultaat, letterlijk). Alle bedragen zijn **vraagprijzen**, geen transactieprijzen.

## 1. Oordelentabel

| Reeks / onderdeel | Oordeel | Onderbouwing (kort) | Gecorrigeerde waarde |
|---|---|---|---|
| **villa_renovated** (n=17, mediaan 4.364) | **Bevestigd, met aanvulling** | 9/17 via `property_detail` nagelopen: prijs, m², €/m² en renovatie-/bouwjaarclaim kloppen bij alle 9. Onafhankelijke zoekopdracht geeft mediaan 4.146 (−5 %, binnen ±15 %). Geen "para reformar" en geen nieuwbouw in de reeks. **Eén object ontbreekt** dat aan de eigen definitie voldoet: 112551618, "Construido en 2022", 1.440.000 € / 377 m² = 3.820 €/m². | **n=18, mediaan 4.325** (p25 3.846, p75 5.081) |
| – deelreeks Montgó–Ermita (n=12, mediaan 4.325) | Bevestigd, met aanvulling | Rekenkunde klopt; met 112551618 erbij: | n=13, mediaan 4.286 |
| – deelreeks Tosal–Castellans (n=5, mediaan 5.087) | Bevestigd als rekensom, **onbruikbaar als cijfer** | n=5 en de twee hoogste waarden hangen aan dunne claims (zie §4: 112512860 alleen vloerverwarming 2026; 111433078 zonder bouwjaar). | geen eigen mediaan opvoeren |
| – gevoeligheid zonder uitschieters (n=15, mediaan 4.364) | Bevestigd | Rekenkunde klopt. | – |
| **villa_new** (n=14, mediaan 5.002) | **Bevestigd, met kanttekening** | 7/14 via `property_detail` nagelopen (incl. Ca Áurea, dat in het origineel "niet bevestigd" heette): prijs, m² en status kloppen. Onafhankelijke zoekopdrachten geven dezelfde 6 obra-nueva-villa's als het origineel (mediaan alleen-projecten 4.452, −11 %, binnen ±15 %). Dubbel 111080148/111938184 is **waarschijnlijk** hetzelfde huis (zelfde prijs, m², perceel, 59 m) — niet bewijsbaar. | als dubbel: n=13, mediaan 4.746 (gevoeligheid) |
| – laag "opgeleverd 2025–2026: 6.750–7.550 €/m²" | Bevestigd | 111080148, 112229257 via detail: "Construido en 2026/2025", status *good*. | – |
| – laag "projecten 3.646–5.258 €/m²" | Bevestigd | 108643937, 106741296, 111697961, 111928138 via detail: `promotionType: notFinished`. | – |
| Rekenkunde min/p25/mediaan/p75/max (beide reeksen + deelreeksen + gevoeligheden) | **Bevestigd, exact** | Nagerekend op de 17 en 14 voorbeeldwaarden (lineaire-interpolatiepercentiel); alle 6 rijen van de conclusietabel komen op het cijfer overeen. | – |
| Ontdubbeling | Bevestigd, één reden fout | Uitkomst klopt; maar 111155783 is niet "zonder renovatieclaim" — de tekst zegt "Vivienda principal – Reformada en 2022". Het is hetzelfde object als 112332323 (terecht één keer geteld). | – |
| Uitsluiting 110554212 (Rutilius) | Bevestigd, reden bijstellen | De tool geeft nu "Promoción de obra nueva / Villa Rutilius, notFinished", 184 m², 9.103 €/m²; de tekst noemt geen "proyecto de reforma" meer. Uitsluiten blijft juist (niets gebouwd, geen bestaand huis), maar de reden in het origineel klopt niet meer met de advertentie van vandaag. | – |

**Kern:** de mediaan van ±4.300–4.400 €/m² voor gerenoveerde/moderne villa's houdt stand; de correcte n is 18 en de mediaan 4.325. De nieuwbouwreeks houdt stand, met de waarschuwing dat de mediaan 5.002 tussen 4.746 (als 111080148 = 111938184) en 5.258 (zonder Ca Áurea) beweegt: de reeks is te heterogeen (projecten vs. opgeleverd) om als één mediaan te gebruiken — het origineel zegt dat zelf ook in §4.

## 2. Controle 1 — `property_detail` op de voorbeelden

### 2.1 villa_renovated (9 van 17 geopend)

| Code | Prijs / m² / €/m² in tool | Klopt met origineel | Claim in tool (letterlijk) | Oordeel |
|---|---|---|---|---|
| 107385205 | 794.000 / 250 / 3.176; "Construido en 1978"; 240 m² útiles | ja | "en un estado excelente, muy bien cuidada y reformada recientemente" | gerenoveerd volgens aanbieder; claim dun (geen omvang, energielabel G 382,6 kWh/m²·jaar); advertentie ">1 jaar" oud |
| 99656305 | 2.950.000 / 885 / 3.333; "Construido en 2014"; 680 m² útiles | ja | "construcción del año 2014 la arquitectura es moderna … espacio adicional de 200m2 que se podría convertir en zona habitable" | modern (2014). 885 m² bevat ±200 m² ruwbouw; op 680 m² útiles = 4.338 €/m² |
| 112088816 | 1.025.000 / 281 / 3.648; "Construido en 1981"; prijsdaling −5 % (was 1.075.000) | ja | "completamente renovada … lista para entrar a vivir" | gerenoveerd |
| 110122731 | 800.000 / 216 / 3.704; "Construido en 1982"; Carretera de Jesús Pobre | ja | "reforma integral de alta gama" | gerenoveerd |
| 110437594 | 720.000 / 165 / 4.364; geen bouwjaar; perceel 973 m² | ja | "completamente renovada" | gerenoveerd |
| 110002941 | 1.350.000 / 305 / 4.426; Pic de la Batalla 14; perceel 1.700 m² | ja | "La casa principal fue completamente rehabilitada en 2022"; toeristische licentie | gerenoveerd (hoofdwoning); tweede woning is B&B |
| 111361293 | 1.399.000 / 275 / 5.087; 220 m² útiles; Calle Elche | ja | "renovación ha sido integral, incluyendo sistemas eléctricos y de fontanería" | gerenoveerd |
| 112512860 | 2.250.000 / 300 / 7.500; geen bouwjaar; geen perceel in velden (tekst: 3.000 m²) | ja | "Recién actualizada en 2026 con un sistema de calefacción por suelo radiante zonificado … tres baños modernos" | **twijfel**: de enige concrete claim is een installatie (vloerverwarming); geen "reforma integral". Volgens de eigen regel van het origineel (deelrenovaties uitgesloten) hoort dit object op de wip |
| 111433078 | 3.550.000 / 380 / 9.342; geen bouwjaar; energielabel G | ja | "Ca Malva … arquitectura contemporánea, materiales nobles … ascensor privado … domótica" | modern volgens tekst, geen bouwjaar; uitschieter, zoals het origineel al markeert |

Alle 9: `priceByArea` van de tool = vraagprijs / `size`, zonder afwijking. Geen van de 9 is "para reformar" of nieuwbouw.

### 2.2 villa_new (7 van 14 geopend)

| Code | Prijs / m² / €/m² in tool | Klopt | Status in tool | Oordeel |
|---|---|---|---|---|
| 108643937 | 1.495.000 / 410 / 3.646 | ja | `newdevelopment`, promotie 108641469 "Villa Nova", `notFinished`; energiecertificaat "del proyecto" | project |
| 106741296 | 2.975.000 / 759 / 3.920 | ja | `newdevelopment`, promotie 106737805 "Ca Áurea", `notFinished`; tekst: "759 m2 construidos de los cuales son 394 m² de la propiedad y 365 m² de terrazas"; "lista para comenzar su construcción en Junio 2025"; advertentie ">1 jaar" oud | project; **nu wél via detail bevestigd** (origineel: "niet bevestigd"). Op 394 m² woning = 7.551 €/m² |
| 111697961 | 1.840.000 / 459 / 4.009 | ja | `newdevelopment`, promotie 111693653, `notFinished`; "FINALIZACIÓN DE CONSTRUCCIÓN AGOSTO 2026"; kelder met garage voor 4 auto's | in aanbouw; opleverdatum is inmiddels verstreken volgens tekst, advertentie ">1 maand" oud |
| 111080148 | 1.980.000 / 293 / 6.758; "Construido en 2026"; 224 m² útiles; perceel 1.500 m² | ja | `good` (tweedehands) | opgeleverd 2026; tekst zegt "292 m²" en "una sola planta" |
| 111938184 | 1.980.000 / 292 / 6.781; perceel 1.500 m²; Pic de Rebalsadors | ja | `good`, maar tekst: "actualmente en construcción y se entregará a finales de 2026 (Bajo reserva)"; semisótano met appartement | in aanbouw. **Zelfde prijs, zelfde m² (292), zelfde perceel (1.500 m²), 59 m van 111080148, beide Garroferal**: waarschijnlijk hetzelfde huis via twee makelaars; verschil in indeling (1 laag vs. semisouterrain) is niet doorslaggevend omdat 111080148 een garage-in-huis noemt. [te verifiëren] |
| 111928138 | 1.575.000 / 230 / 6.848 | ja | `newdevelopment`, promotie 111911746, `notFinished`; alleen plattegronden en omgevingsfoto's; energielabel "Aún no dispone" | project (Tosal–Castellans) |
| 112229257 | 2.350.000 / 312 / 7.532; "Construido en 2025"; energielabel B | ja | `good` | opgeleverd 2025 |

## 3. Controle 2 — onafhankelijke zoekopdrachten

| # | Query (letterlijk) | Filter waar Idealista op uitkwam | Treffers | URL |
|---|---|---|---|---|
| V1 | villa completamente reformada en Jávea, zona Montgó - Ermita | ME: villa, buen estado | 41 / 41 | https://www.idealista.com/es/venta-viviendas/javeaxabia/montgo-ermita/con-villa,buen-estado/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_list |
| V2 | villa reformada en Jávea, zona Partida Tosal - Zona dels Castellans | TC: villa, buen estado | 15 / 15 | https://www.idealista.com/es/venta-viviendas/javeaxabia/partida-tosal-zona-dels-castellans/con-villa,buen-estado/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_list |
| V3 | chalet reformado en Jávea, zona Partida Tosal - Zona dels Castellans | TC: chalets, buen estado | 38 / 38 | https://www.idealista.com/es/venta-viviendas/javeaxabia/partida-tosal-zona-dels-castellans/con-chalets,buen-estado/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_list |
| V4 | villa de obra nueva o a estrenar en Jávea, zona Montgó - Ermita | ME: villa, obra nueva | 6 / 6 | https://www.idealista.com/es/venta-viviendas/javeaxabia/montgo-ermita/con-villa,obra-nueva/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_list |
| V5 | chalet construido en 2025 o 2026 en Jávea, zona Montgó - Ermita, más de 1.500.000 euros | ME: chalets, obra nueva, >1,5M | 7 / 7 | https://www.idealista.com/es/venta-viviendas/javeaxabia/montgo-ermita/con-precio-desde_1500000,chalets,obra-nueva/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_list |

Bevestigd: de assistent vertaalt "reformada" naar het filter *buen estado* en "construido en 2025" naar *obra nueva* — precies de beperking die het origineel in §2 noemt. Alle 41 + 15 + 38 + 6 + 7 beschrijvingen zijn gelezen (tekstclassificatie op reformad/renovad/rehabilitad/actualizad, para reformar/necesita reforma/por finalizar, construido en 20xx/obra nueva).

**villa_renovated, onafhankelijke reeks (V1+V2, alleen villa-tag, ontdubbeld op prijs+m²+tekst):** 3.176 (107385205), 3.333 (99656305), 3.648 (110560477 = 112088816), 3.820 (112551618, gebouwd 2022), 3.922 (112261358), 4.007 (111669594 = 109920552), 4.286 (111224213 = 109732217), 4.286 (111055096), 4.426 (110002941; 111139864 is dezelfde met 300 m²), 5.475/5.227 (112332323 = 111155783 = 112342282), 5.615 (111006962), 7.500 (112512860 = 112469782) → **n=12, mediaan 4.146**, p25 3.777, p75 4.688. Verschil met het origineel (4.364): −5 %, binnen ±15 %. De villa-tag mist de "chalets"-treffers (110122731, 110437594, 111361293, 110085864, 112387090, 111433078 kwamen in V3 en in het origineel via #7–#11 wél boven), wat de lagere mediaan verklaart. V3 (TC chalets) bevestigt 107385205, 110122731, 111361293, 112512860 (+3 dubbelen), 111433078 en 110753189 (= 110437594) als de enige objecten met een renovatie- of moderne-bouwclaim in Tosal–Castellans; de overige 30 hebben géén claim (o.a. 111773506, 112271843, 106990380, 110041015, 107666492, 111859645, 111388814) of zijn "para reformar" (112342297, 97576604).

**villa_new, onafhankelijk (V4/V5):** V4 geeft exact de 6 obra-nueva-villa's van het origineel (108643937, 106741296, 111697961, 109556480, 111598568, 111398703 → mediaan projecten-only 4.452); V5 voegt 111003199 en 110554212 toe. De opgeleverde villa's 112208312 (6.973) en 111656915 (6.906) verschenen in V1 als tweedehands; 112229257 en 111080148 zijn via detail bevestigd. De samenstelling van het origineel is dus reproduceerbaar; mediaan alleen-projecten 4.452 vs. origineel 5.002 (−11 %, binnen ±15 %; het verschil is de laag opgeleverde villa's).

## 4. Controle 3 — foute indeling en dubbelen

1. **Ontbrekend object in villa_renovated: 112551618** (Euro Javea, ref. EJV-1559), Calle del Puig Campana, Montgó–Ermita. Tool 15-09-2026: 1.440.000 € / 377 m² = **3.820 €/m²**, status *good*, veld "Construido en 2022", tekst "exclusiva villa contemporánea … Construida en 2022 … preparada para entrar a vivir". Voldoet aan de definitie "modern = bouwjaar 2014 of later" uit §3 van het origineel. Kanttekening: de advertentie stond bij controle op "actualizado hace 0 minutos" — mogelijk (her)geplaatst ná de zoekronde van het origineel; niet vast te stellen. Hoort er in elk geval per 15-09-2026 in. URL: https://www.idealista.com/es/inmueble/112551618/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail
2. **Dunne claim: 112512860** (7.500 €/m², tweede hoogste). De enige concrete renovatiezin is "Recién actualizada en 2026 con un sistema de calefacción por suelo radiante zonificado"; verder "tres baños modernos". Dat is een installatie-update, geen integrale renovatie. Het origineel sluit "deelrenovaties (alleen keuken of badkamers)" uit; consequent toegepast valt dit object er ook uit. Ik laat het als **twijfelgeval** staan (aanbieder noemt het "recién actualizada") en geef de reeks in beide varianten.
3. **Reden van uitsluiting 111155783 klopt niet.** Tekst (V1, ook onder code 112342282, Calle Fènix): "Vivienda principal – Reformada en 2022", twee woningen op 3.359 m², licentie turística. Dat is hetzelfde object als 112332323 (2.190.000 €, "completamente reformada en 2022", twee woningen, perceel ±3.500 m²); ontdubbeling is dus juist, alleen de reden ("geen renovatieclaim") niet. Let op: 112332323 geeft 400 m² (5.475 €/m²), de twee andere advertenties 419 m² (5.227 €/m²); het origineel houdt de hoogste €/m² aan.
4. **109929510 / 109786704 / 110002941 zijn zeer waarschijnlijk dezelfde finca** (alle drie: perceel 1.700 m², hoofdwoning ±200 m² met gastenhuis, "algarrobos centenarios", buganvillas, zwembad, zuid). Alleen 110002941 draagt de claim "rehabilitada en 2022" en alleen dat exemplaar is geteld — geen dubbeltelling. Het "pin 1,8 km verderop"-voorbehoud van het origineel is daarmee waarschijnlijk opgelost: pins zijn benaderend bij `showAddress=false`.
5. **Geen "para reformar"- en geen nieuwbouwobject in villa_renovated.** De twee "para reformar"-treffers in TC (112342297, 97576604: 595.000 / 220) en de projecten (110554212, 111120425-groep) zitten in geen van beide reeksen. 103848413 (Villa Hermitage, 2.950.000 / 820, "moderna villa de lujo") heeft in de detailvelden géén bouwjaar en geen renovatieclaim → terecht buiten de reeks; verdient wel een regel in §5 van het origineel.
6. **Dubbel in villa_new, waarschijnlijk: 111080148 = 111938184** (zie §2.2). Het origineel telt ze apart met markering. Ik acht ze eerder wél dan niet hetzelfde huis; bewijs ontbreekt. Gevoeligheid hieronder.
7. **110554212 (Rutilius):** volgens de tool vandaag "Promoción de obra nueva — Villa Rutilius, notFinished", 184 m², 1.675.000 € = 9.103 €/m², alleen plattegronden + enkele foto's. De tekst spreekt niet meer van een "proyecto de reforma integral". Uitsluiting blijft verdedigbaar (geen bestaand, geen opgeleverd huis); als je het als project in villa_new zou tellen wordt de mediaan 5.258 (n=15). Reden in het origineel bijwerken.
8. Zonelabels: bevestigd dat 110753189 (TC-label) = 110437594 (ME-label); 111351541 (TC-label) is inderdaad een "Chalet adosado" (V3) → terecht uitgesloten.

## 5. Controle 4 — rekenkunde

Nagerekend (Python, percentiel met lineaire interpolatie zoals numpy-standaard) op de 17 resp. 14 voorbeeldwaarden uit de tabellen:

| Rij in conclusietabel | Origineel | Nagerekend | Oordeel |
|---|---|---|---|
| villa_renovated n=17 | 3.176 / 3.922 / 4.364 / 5.087 / 9.342 | 3.176 / 3.922 / 4.364 / 5.087 / 9.342 | exact |
| – Montgó–Ermita n=12 | 3.333 / 3.986 / 4.325 / 4.680 / 5.615 | 3.333 / 3.986 / 4.325 / 4.680 / 5.615 | exact |
| – Tosal–Castellans n=5 | 3.176 / 3.704 / 5.087 / 7.500 / 9.342 | idem | exact |
| – zonder 2 uitschieters n=15 | 3.176 / 3.964 / 4.364 / 5.075 / 7.500 | idem | exact |
| villa_new n=14 | 3.646 / 4.393 / 5.002 / 6.831 / 7.532 | idem | exact |
| – zonder Ca Áurea n=13 | 3.646 / 4.572 / 5.258 / 6.848 / 7.532 | idem | exact |

Ook de 31 individuele €/m²-waarden (vraagprijs ÷ m²) kloppen op de euro, en komen overeen met `priceByArea` van de tool bij alle 16 geopende objecten.

## 6. Gecorrigeerde reeksen (vraagprijzen €/m² gebouwd, 15-09-2026)

| Reeks | n | min | p25 | mediaan | p75 | max | Wat er anders is |
|---|---|---|---|---|---|---|---|
| **villa_renovated, gecorrigeerd** | **18** | 3.176 | 3.846 | **4.325** | 5.081 | 9.342 | + 112551618 (3.820, gebouwd 2022) |
| – idem, zonder twijfelgeval 112512860 | 17 | 3.176 | 3.820 | 4.286 | 5.063 | 9.342 | gevoeligheid |
| – Montgó–Ermita, gecorrigeerd | 13 | 3.333 | 3.922 | 4.286 | 4.552 | 5.615 | + 112551618 |
| – Tosal–Castellans | 5 | – | – | – | – | – | niet apart opvoeren (n=5, twee dunne claims) |
| **villa_new, origineel** | 14 | 3.646 | 4.393 | **5.002** | 6.831 | 7.532 | houdt stand |
| – als 111080148 = 111938184 | 13 | 3.646 | 4.333 | 4.746 | 6.848 | 7.532 | gevoeligheid [te verifiëren] |
| – alleen opgeleverd / in afbouw | 6 | 4.009 | 6.764 | 6.844 | 6.956 | 7.532 | 111697961, 111080148, 111938184, 111656915, 112208312, 112229257 |
| – alleen projecten met licentie | 8 | 3.646 | 4.230 | 4.632 | 4.874 | 6.848 | 108643937, 106741296, 109556480, 111598568, 109864461, 111003199, 111398703, 111928138 |

Advies voor het model: gebruik voor "gerenoveerd/modern" **4.325 (n=18)**, met 3.850–5.100 als kern; gebruik voor nieuwbouw **niet** de gecombineerde mediaan maar de twee lagen (opgeleverd ±6.800; project ±4.600, vaak grote volumes en soms excl. IVA).

## 7. Gevolgen voor K03, K04, K07

Marginaal. K03 (4.708 €/m² niet-gerenoveerd) blijft boven de gecorrigeerde mediaan (4.325); K04 (2.158 €/m²) krijgt een gat van ±2.170 €/m² tot de mediaan en ±1.690 tot p25 (3.846) — vrijwel gelijk aan het origineel. Voor K07 verandert niets: de laag "opgeleverd 2025–2026" (6.750–7.550 €/m²) is bevestigd. Alles blijft rekenwerk op vraagprijzen, geen taxatie.

## 8. Wat niet gecontroleerd is

- 8 van de 17 gerenoveerde objecten (112261358, 109920552, 109732217, 111055096, 110085864, 112387090, 112332323, 111006962) en 7 van de 14 nieuwbouwobjecten zijn niet opnieuw via `property_detail` geopend; hun teksten zijn wel gelezen in V1/V3/V4/V5 (waar ze verschenen) en stroken met het origineel.
- Of 112551618 al bestond op het moment van de oorspronkelijke zoekronde: niet vast te stellen (advertentie stond op "actualizado hace 0 minutos").
- Fysieke kwaliteit van renovaties, vergunningen, IVA-behandeling van projectprijzen: niet controleerbaar via de tool.
- Geen telefoonnummers of persoonsgegevens overgenomen; makelaarsnaam/referentie alleen zoals de advertentie ze toont.

## 9. Bestanden

- Dit rapport: `onderzoek/H01-comparables-montgo_ermita.verificatie.md`
- Ruwe toolresultaten V1–V5 en detailpagina's: sessie-scratchpad (niet in de repo).

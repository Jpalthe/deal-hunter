# H01 — Vergelijkingsprijzen Benitachell / El Poble Nou de Benitatxell (incl. Cumbre del Sol)

**zone_key:** `benitachell` · **status:** nieuw werkgebied, alleen referentieprijzen — nog geen kandidaten
**Bron:** officiële Idealista-assistent (MCP `search_properties` + `property_detail`), locale es-ES, country es, maxResults 50 · **peildatum:** 15-09-2026 · **bewijstype:** 2 (portaaldata via officiële tool)

> **Alle bedragen zijn VRAAGPRIJZEN** (prijs gedeeld door "m² construidos" zoals de tool die geeft), geen transactieprijzen. Ze zeggen wat aanbieders vragen, niet wat kopers betalen. Idealista-vraagprijzen in deze zone liggen doorgaans boven de uiteindelijke koopsom; hoeveel, is uit deze bron niet af te leiden.

## 1. Conclusie in cijfers

| Reeks | n | min | p25 | mediaan | p75 | max | bron / datum |
|---|---|---|---|---|---|---|---|
| **villa_renovated (gerenoveerd óf modern gebouwd ≥ 2014)** | 37 | 1.180 | 3.451 | **4.614** | 5.960 | 8.996 | Idealista-assistent, 15-09-2026 |
| **· waarvan gerenoveerd (renovatieclaim, ouder casco)** | 11 | 1.180 | 2.646 | **3.738** | 4.470 | 7.362 | idem |
| **· waarvan modern gebouwd ≥ 2014, verkocht als tweedehands** | 26 | 2.363 | 4.245 | **5.320** | 6.025 | 8.996 | idem |
| **· alleen Cumbre del Sol** | 34 | 1.180 | 3.545 | **4.696** | 6.025 | 8.996 | idem |
| **villa_new (obra nueva, a estrenar, in aanbouw, project)** | 17 | 2.832 | 3.312 | **4.577** | 4.843 | 7.971 | idem |
| **· alleen Cumbre del Sol** | 13 | 2.832 | 4.273 | **4.729** | 4.843 | 6.706 | idem |
| **townhouse_renovated — casco Poble Nou** | 2 | 1.853 | 1.928 | **2.003** | 2.078 | 2.153 | idem — **n < 6**, indicatief |
| **townhouse_renovated — casco + adosados in urbanisaties** | 5 | 1.853 | 2.153 | **2.714** | 2.889 | 3.646 | idem — **n < 6**, indicatief |
| **apartment_new (Cumbre del Sol)** | 10 | 2.489 | 2.805 | **3.847** | 5.543 | 6.543 | idem — brede spreiding door m²-definitie, zie §8 |
| **· alleen de 5 promotie-units Montecala Gardens (SJW)** | 5 | 4.579 | 5.231 | **5.648** | 5.699 | 6.543 | idem — n < 6 |
| **apartment_renovated (Cumbre del Sol, 1× Alcassar)** | 9 | 2.111 | 2.907 | **3.318** | 3.794 | 4.358 | idem |

Alle cijfers in € per m² gebouwd, afgerond. p25/p75 met lineaire interpolatie tussen gesorteerde waarden; mediaan is de standaardmediaan. Berekend over ontdubbelde objecten (§2), niet over advertenties.

**Lezing voor Jan (kort):**
- Een **gerenoveerde of moderne villa in Cumbre del Sol** wordt aangeboden rond **4.600–4.700 €/m²** (helft van het aanbod tussen ±3.500 en ±6.000). Dat is duidelijk lager dan Jávea-Balcón al Mar (mediaan 6.412 in H01-granadella_balcon) en in de buurt van Granadella/Costa Nova (5.777). Cumbre del Sol is per m² dus een goedkopere villamarkt dan de Jávea-kust, met wel dezelfde bovenkant (tot ±9.000 €/m² voor de beste kliflocaties aan Dalias/Lirios).
- Binnen de reeks is er een echt verschil tussen **gerenoveerde oudere villa's** (mediaan **3.738**, n=11) en **modern gebouwde villa's van na 2014 die als tweedehands worden verkocht** (mediaan **5.320**, n=26). Een renovatieproduct wordt hier dus ±30% lager per m² geprijsd dan een moderne villa — deels een echt kwaliteitsverschil, deels omdat oudere villa's grotere, minder efficiënte m²-totalen opgeven.
- **Nieuwbouw** staat op mediaan **4.577 €/m²** (Cumbre del Sol: 4.729), nauwelijks anders dan "modern tweedehands". Net als in Jávea telt de aanbieder bij nieuwbouw terrassen, kelder en parking mee in "m² construidos" (bijv. Villa Nara: 471 m² gebouwd tegenover 217 m² nuttig; Magnolias 179: 441 gebouwd / 240 woning). Vergelijk nieuwbouw-€/m² daarom nooit één-op-één met renovatie-€/m².
- **Let op het m²-probleem in deze zone:** hetzelfde huis staat bij verschillende makelaars met sterk afwijkende m² (Palmeras 111 p: 188 / 214 / 317 m² bij één prijs, dus 7.973 tegenover 4.729 €/m²; Blue Square-villa 2020: 200 tegenover 418 m²). De €/m² in deze reeksen is dus een ruwe maat; per object altijd de m²-opbouw (woning / terras / kelder) checken.
- Het **casco van Poble Nou** is een aparte, veel goedkopere markt: twee integraal gerenoveerde dorpshuizen worden aangeboden op **1.853 en 2.153 €/m²** (365.000 en 435.000 €). Meer gerenoveerd aanbod is er op de peildatum niet; het overige casco-aanbod is "para reformar".
- **Appartementen** in Cumbre del Sol: gerenoveerd rond **3.300 €/m²** (2.100–4.400); nieuwbouw in Montecala Gardens (promotie-units) rond **5.600 €/m²** op basis van de opgegeven m², maar zodra makelaars terrassen en gemeenschappelijke delen meetellen zakt dat naar 2.500–2.700.

## 2. Hoe de reeksen zijn opgebouwd

**Zonelabels.** De assistent beeldt "Benitachell, Poble Nou de Benitatxell, Cumbre del Sol" bijna altijd af op de Idealista-zone **Cumbre del Sol, Benitachell** (193 casas y chalets, 63 villa's op de peildatum). Twee queries ("villa moderna reformada …" en "villa moderna en Poble Nou de Benitatxell") leverden een *zona personalizada* (eigen polygoon) op. De gemeente als geheel heet bij de tool **Benitachell, Alicante** (286 casas y chalets) en kent daarnaast de zones **Alcassar** (Golden Valley, Vall del Portet, Pueblo Alcasar), **Les Fonts** (Los Molinos, Racó de Nadal), **Calistros** (Las Mimosas) en **Centro** (het casco van Poble Nou). Advertenties met label "Centro, Benitachell" beschrijven soms tóch een villa in Cumbre del Sol; die zijn op tekst bij Cumbre del Sol gezet. Vijf advertenties met label "Paichi, Moraira" (Golden Valley, 1.990.000 €) vallen buiten de gemeente en zijn niet gebruikt.

**Volledigheid.** De tool geeft maximaal 50 resultaten zonder paginering. Daarom is de gemeente in zes prijsbanden bevraagd (tot 500 k; 500–700 k; 700–900 k; 900–1,2 M; 1,2–1,8 M; > 1,8 M) en Cumbre del Sol apart in drie banden voor villa's en twee voor appartementen. Na samenvoeging van 30 zoekopdrachten: **384 unieke advertenties** (283 Cumbre del Sol, 46 "Centro/Benitachell", 26 Alcassar, 15 Les Fonts, 9 Calistros, 5 Paichi). Drie prijsbanden (< 500 k, 500–700 k, 700–900 k, 1,2–1,8 M) telden meer dan 50 advertenties; daar zijn er dus enkele gemist.

**Selectie villa_renovated.** Opgenomen als de advertentietekst of `property_detail` zegt: gerenoveerd / reforma integral / totalmente reformada (met of zonder jaartal, mits niet ouder dan ±2015), óf bouwjaar ≥ 2014 en niet als obra nueva/a estrenar aangeboden, óf "villa moderna/contemporánea" als hoofdomschrijving zonder bouwjaar (gevlagd **[claim agent]**). Uitgesloten: "para reformar", "potencial de reforma", "posibilidades de modernización", alleen keuken/bad/ramen vernieuwd, "buen estado" of "bien mantenida" zonder renovatieclaim, renovaties van vóór 2015 (2006, 2011), bouwjaar 2013 zonder renovatieclaim, en alles wat als nieuwbouw wordt vermarkt.

**Selectie villa_new.** Obra nueva, "a estrenar", promotie (ook 'notFinished'), in aanbouw of project; alleen advertenties waarvoor de tool een m²-veld geeft. Zes promotie-vermeldingen zonder m² (Montecala Gardens 473.000; Vall del Portet 890.000; Villa Nara 1.375.000; Villa Moraig 1.880.000; Villas Benitachell 2.155.975; Villa Alcassar 1.650.000) zijn overgeslagen, maar hun losse units mét m² zitten in de reeks. Eén nieuwbouwvilla (111712601, FALC, 1.850.000 / "870 m²") is geschrapt omdat de 870 m² aantoonbaar de perceelgrootte is.

**Ontdubbeling.** Zelfde prijs + zelfde m² + zelfde zone = één object. Daarbovenop handmatig samengevoegd waar meerdere makelaars aantoonbaar hetzelfde huis aanbieden met afwijkende m² of prijs (zelfde perceel, straat, indeling, tekst). Opvallende gevallen: de Ibiza-villa uit 1988 op perceel 1.032 m² staat bij 7 makelaars (1.485.000–1.700.000 €); Palmeras 111 p bij 3 makelaars met 188/214/317 m²; het gerenoveerde dorpshuis in het casco bij 8 makelaars met 192–219 m². Zo bleven 37 + 17 objecten over uit 74 + 26 advertenties.

**Verificatie.** `property_detail` opgevraagd voor **28 van de 37** villa_renovated-objecten, **16 van de 17** villa_new-objecten, alle 5 townhouses, 6 van de 10 nieuwbouwappartementen en 7 van de 9 gerenoveerde appartementen (kolom "detail"). Bouwjaar komt uit het veld "Construido en …" van de tool; let op: bij de gerenoveerde 1988-villa zet één makelaar daar het renovatiejaar (2025), en bij projecten staat het geplande opleverjaar (2026/2027).

## 3. Zoeklogboek (Idealista-assistent, 15-09-2026)

| # | Query | Zone die de tool koos | Filters die de tool toepaste | Totaal | Ontvangen |
|---|---|---|---|---|---|
| 1 | villa moderna reformada en Benitachell, Poble Nou de Benitatxell, Cumbre del Sol | zona personalizada | Villas; Usada / buen estado | 1 | 1 |
| 2 | chalet reformado en Benitachell, Poble Nou de Benitatxell, Cumbre del Sol | Cumbre del Sol, Benitachell | Casas y chalets; Usada / buen estado | 193 | 50 |
| 3 | villa de diseño en Benitachell, Poble Nou de Benitatxell, Cumbre del Sol | Cumbre del Sol | Villas | 63 | 50 |
| 4 | obra nueva en Benitachell, Poble Nou de Benitatxell, Cumbre del Sol | Cumbre del Sol | Promociones de obra nueva | 4 | 4 (zonder m²) |
| 5 | villa a estrenar en Benitachell, Poble Nou de Benitatxell, Cumbre del Sol | Cumbre del Sol | Villas; Obra nueva | 2 | 2 |
| 6 | villa de nueva construcción en Benitachell, Poble Nou de Benitatxell, Cumbre del Sol | Cumbre del Sol | Villas; Obra nueva | 2 | 2 |
| 7 | villa en Cumbre del Sol, Benitachell hasta 900.000 euros | Cumbre del Sol | < 900.000; Villas | 22 | 22 |
| 8 | villa en Cumbre del Sol, Benitachell entre 900.000 y 1.500.000 euros | Cumbre del Sol | 900.000–1.500.000; Villas | 29 | 29 |
| 9 | villa en Cumbre del Sol, Benitachell de más de 1.500.000 euros | Cumbre del Sol | > 1.500.000; Villas | 12 | 12 |
| 10 | chalet reformado en Benitachell | Benitachell, Alicante | Casas y chalets; Usada / buen estado | 286 | 50 |
| 11 | villa moderna en Poble Nou de Benitatxell | zona personalizada | Villas | 35 | 35 |
| 12 | apartamento de obra nueva a estrenar en Cumbre del Sol, Benitachell | Cumbre del Sol | Pisos, áticos, dúplex; Obra nueva | 5 | 5 |
| 13 | apartamento reformado en Cumbre del Sol, Benitachell | Cumbre del Sol | Pisos, áticos, dúplex; Usada / buen estado | 94 | 50 |
| 14 | casa de pueblo o adosado reformado en el casco urbano de Benitachell, Poble Nou de Benitatxell | Benitachell, Alicante | Casas y chalets; Usada / buen estado | 286 | 50 |
| 15 | villa reformada en Cumbre del Sol, Benitachell | Cumbre del Sol | Villas; Usada / buen estado | 59 | 50 |
| 16 | villa moderna en Cumbre del Sol, Benitachell | Cumbre del Sol | Villas | 63 | 50 |
| 17 | casa o chalet en Benitachell hasta 500.000 euros | Benitachell, Alicante | < 500.000; Casas y chalets | 62 | 50 |
| 18 | casa o chalet en Benitachell entre 500.000 y 700.000 euros | Benitachell, Alicante | 500.000–700.000 | 60 | 50 |
| 19 | casa o chalet en Benitachell entre 700.000 y 900.000 euros | Benitachell, Alicante | 700.000–900.000 | 59 | 50 |
| 20 | casa o chalet en Benitachell entre 900.000 y 1.200.000 euros | Benitachell, Alicante | 900.000–1.200.000 | 33 | 33 |
| 21 | casa o chalet en Benitachell entre 1.200.000 y 1.800.000 euros | Benitachell, Alicante | 1.200.000–1.800.000 | 65 | 50 |
| 22 | casa o chalet en Benitachell de más de 1.800.000 euros | Benitachell, Alicante | > 1.800.000 | 31 | 31 |
| 23 | villa a estrenar en Benitachell | Benitachell, Alicante | Villas; Obra nueva | 3 | 3 |
| 24 | obra nueva en Benitachell | Benitachell, Alicante | Promociones de obra nueva | 6 | 6 (zonder m²) |
| 25 | adosado reformado en Benitachell | Benitachell, Alicante | Chalets adosados; Usada / buen estado | 18 | 18 |
| 26 | casa adosada en Cumbre del Sol, Benitachell | Cumbre del Sol | Chalets adosados | 5 | 5 |
| 27 | apartamento en Cumbre del Sol, Benitachell hasta 350.000 euros | Cumbre del Sol | < 350.000; Pisos, áticos, dúplex | 55 | 50 |
| 28 | apartamento en Cumbre del Sol, Benitachell de más de 350.000 euros | Cumbre del Sol | > 350.000; Pisos, áticos, dúplex | 42 | 42 |
| 29 | villa reformada en Les Fonts, Benitachell | Les Fonts, Benitachell | Villas; Usada / buen estado | 4 | 4 |
| 30 | villa moderna en Alcassar, Benitachell | Alcassar, Benitachell | Villas | 6 | 6 |

Let op: de tool vertaalt trefwoorden als *reformada* en *moderna* niet naar een renovatiefilter maar naar "Usada / buen estado" of helemaal niets. De selectie is daarom volledig op de tekst en op `property_detail` gedaan (§2).

## 4. Reeks villa_renovated — alle 37 objecten (gesorteerd op €/m²)

Zone: CdS = Cumbre del Sol. "detail" = bevestigd met `property_detail`. Soort: *gerenoveerd* = renovatieclaim op ouder casco; *modern* = bouwjaar ≥ 2014 (of hedendaags zonder bouwjaar, dan [claim agent]) en niet als nieuwbouw vermarkt. Prijzen in €, vraagprijs.

| Code | Zone | Vraagprijs € | m² | €/m² | Bouwjaar (tool/tekst) | detail | Soort | Label | Doublures (zelfde object) | URL |
|---|---|---|---|---|---|---|---|---|---|---|
| 106265412 | CdS | 590.000 | 500 | 1.180 | — | ja | gerenoveerd | Girasoles (Villas Costa Mar): 'recién reformada', 500 m² gebouwd / 360 m² útiles, 3 woonlagen; prijs verlaagd van 690.000 [uitschieter] | — | https://www.idealista.com/es/inmueble/106265412/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 107271254 | CdS | 950.000 | 402 | 2.363 | 2020 | ja | modern | Begonias 33 b: 'reciente construcción', bouwjaar 2020; 402 m² = 181 woning + 136 terras + 23 + 62 parking | 111380959 | https://www.idealista.com/es/inmueble/107271254/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 112039120 | Les Fonts | 669.000 | 263 | 2.544 | 2003 | ja | gerenoveerd | Les Fonts (The White Collection): 'totalmente renovada en 2023', bouwjaar 2003, perceel 918 m² | — | https://www.idealista.com/es/inmueble/112039120/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 107642605 | CdS | 650.000 | 250 | 2.600 | 1987 | ja | gerenoveerd | Camelias 12: 'completamente reformada', bouwjaar 1987, perceel 978 m² | — | https://www.idealista.com/es/inmueble/107642605/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 91606045 | CdS | 1.750.000 | 650 | 2.692 | 2001 | ja | gerenoveerd | Palmeras 100 eerste lijn: 'recientemente reformada', bouwjaar 2001; 650 m² = 350 m² binnen + 300 m² terrassen | 105093757 | https://www.idealista.com/es/inmueble/91606045/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 106706046 | CdS | 1.429.000 | 490 | 2.916 | 2024 | nee | modern | E&V: 'construida en 2024' (tekst) | 111904823 (499 m²) | https://www.idealista.com/es/inmueble/106706046/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 106525761 | CdS | 875.000 | 282 | 3.103 | 2020 | ja | modern | Kalmias 48: 'villa contemporánea', bouwjaar 2020, 2 slk, perceel 1.385 m² | 110480392 | https://www.idealista.com/es/inmueble/106525761/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 110186887 | CdS | 1.950.000 | 600 | 3.250 | 2025 | nee | modern | Dalias (Terramar): 'construida en 2025', 600 m² gebouwd / 400 m² útiles, ibicenco (tekst) | — | https://www.idealista.com/es/inmueble/110186887/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 112458498 | Alcassar | 930.000 | 272 | 3.419 | 2025 | ja | modern | Via Pista (Imperia): bouwjaar 2025, perceel 243 m², 3 lagen; feitelijk Vall del Portet-type | — | https://www.idealista.com/es/inmueble/112458498/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 111710430 | CdS | 1.850.000 | 536 | 3.451 | — | ja | modern | Villa Calia, Magnolias (BHHS): 'villa de lujo contemporánea', Technal, fotovoltaïsch; bouwjaar niet vermeld [claim agent] | — | https://www.idealista.com/es/inmueble/111710430/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 110510628 | CdS | 1.490.000 | 428 | 3.481 | 1995 | ja | gerenoveerd | Kalmias/Dalias (RE/MAX): 'villa reformada', bouwjaar 1995, perceel 1.758 m², bijgebouw | 108987280 | https://www.idealista.com/es/inmueble/110510628/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 110131127 | CdS | 1.495.000 | 400 | 3.738 | — | ja | gerenoveerd | Terramar: 'recientemente reformada', 16 zonnepanelen + 24 kWh batterij; staat als 'adosado' maar perceel 1.017 m² | — | https://www.idealista.com/es/inmueble/110131127/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 109384452 | CdS | 1.680.000 | 412 | 4.078 | 2002 | ja | gerenoveerd | Kalmias (KW): 'totalmente reformada', bouwjaar 2002, EPS-isolatie, vloerverwarming, Fibaro | — | https://www.idealista.com/es/inmueble/109384452/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 111762071 | CdS | 970.000 | 229 | 4.236 | 2020 | nee | modern | Lirios 141: 'construida en 2020', toeristische licentie (tekst) | 111941980 (975.000 / 220 m², NL-tekst) | https://www.idealista.com/es/inmueble/111762071/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 110480516 | CdS | 1.295.000 | 303 | 4.274 | 2021 | nee | modern | Lirios 100: 'construida en el año 2021', 191 m² woning + 86 m² terras + 26 m² parking (tekst) | 100133536 | https://www.idealista.com/es/inmueble/110480516/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 112313264 | Calistros | 865.000 | 200 | 4.325 | 2000 | ja | gerenoveerd | Calistros (Oceanic): 'reformado con mucho gusto en 2020', bouwjaar 2000, perceel 722 m² | 111598976 | https://www.idealista.com/es/inmueble/112313264/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 111554015 | CdS | 1.380.000 | 317 | 4.353 | 2014 | ja | modern | Magnolias 154 (CdS Pre-Owned): 'villa moderna', bouwjaar 2014, 'estado impecable'; tekst noemt 297 m² | — | https://www.idealista.com/es/inmueble/111554015/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 107882388 | CdS | 1.680.000 | 380 | 4.421 | 2024 | ja | modern | Kalmias: 'moderna casa de lujo', mediterrane buitenkant, bouwjaar 2024, 370 m² útiles | 108013993 (zelfde tekst, 1.890.000) | https://www.idealista.com/es/inmueble/107882388/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 110881013 | CdS | 1.495.000 | 324 | 4.614 | 1988 | ja | gerenoveerd | Ibiza-stijl villa, perceel 1.032 m², 5 slk/5 bad: 'completamente renovada' (tool zet renovatiejaar 2025 als bouwjaar; 110675119 geeft bouwjaar 1988) | 110059043, 110675119, 111012205, 110147233; 110189147 op 1.700.000 (Blue Square); 110430078 op 1.485.000 | https://www.idealista.com/es/inmueble/110881013/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 104829390 | CdS | 1.295.000 | 279 | 4.642 | 2020 | ja | modern | Villa ARES, Lirios (Abahana): bouwjaar 2020, 173 m² útiles, verhuurvilla | — | https://www.idealista.com/es/inmueble/104829390/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 110936304 | CdS | 950.000 | 200 | 4.750 | 2020 | ja | modern | Blue Square: 'construida en 2020', perceel 836 m², keuken Miele; toeristisch potentieel | 110629102 (zelfde huis, 418 m²!), 109087836, 111446224, 108400743, 109337867 (199 m²) | https://www.idealista.com/es/inmueble/110936304/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 109194891 | CdS | 1.422.000 | 268 | 5.306 | 2021 | ja | modern | Lirios 213: 'chalet contemporáneo', bouwjaar 2021, perceel 891 m² | 112178451, 111381139 (265 m²) | https://www.idealista.com/es/inmueble/109194891/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 107251836 | CdS | 1.600.000 | 300 | 5.333 | 2022 | ja | modern | Camelias 54 C: 'villa contemporánea', bouwjaar 2022, aerothermie + zonnepanelen | — | https://www.idealista.com/es/inmueble/107251836/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 111710771 | CdS | 999.000 | 184 | 5.429 | 2014 | ja | modern | Blue Square: gelijkvloerse hedendaagse villa, bouwjaar 2014, perceel 780 m² | — | https://www.idealista.com/es/inmueble/111710771/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 106552167 | CdS | 1.490.000 | 273 | 5.458 | 2020 | nee | modern | Magnolias 128: 'construida en 2020' (tekst) | — | https://www.idealista.com/es/inmueble/106552167/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 110022033 | CdS | 2.195.000 | 398 | 5.515 | 2024 | nee | modern | Jazmines 161: 'construida en 2024, reciente construcción' (tekst) | — | https://www.idealista.com/es/inmueble/110022033/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 110651943 | CdS | 1.350.000 | 244 | 5.533 | 2021 | nee | modern | Magnolias: 'construida en 2021' (tekst) | 109133568 | https://www.idealista.com/es/inmueble/110651943/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 110704352 | CdS | 1.490.000 | 250 | 5.960 | 2020 | nee | modern | Costa Houses: 'construida en 2020' op perceel 684 m² (tekst) | — | https://www.idealista.com/es/inmueble/110704352/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 111798161 | CdS | 1.300.000 | 215 | 6.047 | — | ja | modern | Casaman: 'arquitectura contemporánea', perceel 813 m²; bouwjaar niet vermeld [claim agent] | 111613504 | https://www.idealista.com/es/inmueble/111798161/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 111168428 | CdS | 1.429.000 | 229 | 6.240 | 2024 | nee | modern | Lirios: 'villa moderna construida en 2024' (tekst) | — | https://www.idealista.com/es/inmueble/111168428/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 104423998 | CdS | 1.200.000 | 190 | 6.316 | — | ja | gerenoveerd | 'completamente renovada en 2018', tuin geheel opnieuw aangelegd, sauna, jacuzzi | — | https://www.idealista.com/es/inmueble/104423998/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 104832335 | CdS | 1.980.000 | 270 | 7.333 | 2021 | ja | modern | Lirios (Unique Homes): 'la villa es nueva', 170 m² útiles, bouwjaar 2021, verkocht als tweedehands | — | https://www.idealista.com/es/inmueble/104832335/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 104929998 | CdS | 1.200.000 | 163 | 7.362 | 1985 | ja | gerenoveerd | Camelias 100: 'villa reformada', perceel 1.113 m², bouwjaar 1985 | 105110243, 105802839 ('totalmente modernizada') | https://www.idealista.com/es/inmueble/104929998/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 111681917 | CdS | 2.249.000 | 266 | 8.455 | 2025 | ja | modern | Villa Altair, Lirios: 3 niveaus, aerothermie, domotica; tool 'construido en 2025', verkocht als tweedehands | 112175280 | https://www.idealista.com/es/inmueble/111681917/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 111019375 | CdS | 1.865.000 | 215 | 8.674 | — | ja | modern | Villa Iseo, Lirios (Montgó Villas): 'lujo contemporáneo', energielabel A; bouwjaar niet vermeld [claim agent] | — | https://www.idealista.com/es/inmueble/111019375/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 111522880 | CdS | 2.450.000 | 279 | 8.781 | 2014 | ja | modern | Dalias: contemporary villa, 179 m² útiles, gastenappartement, infinity pool 13 m | 111103870 (zegt 2017), 110937633 | https://www.idealista.com/es/inmueble/111522880/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 111992299 | CdS | 4.516.000 | 502 | 8.996 | — | ja | modern | Fine & Country, C. Dalias: 'obra maestra del lujo moderno', spa, cine; bouwjaar niet vermeld [claim agent] | 111971400 (zelfde prijs, 1.100 m²) | https://www.idealista.com/es/inmueble/111992299/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |

**Voorbeelden om te onthouden (villa_renovated):**
1. 111522880 Calle Dalias, Cumbre del Sol — 2.450.000 € / 279 m² = 8.781 €/m²; bouwjaar 2014, 179 m² nuttig, 180°-zeezicht, drie makelaars. Bovenkant van de "moderne tweedehands"-markt.
2. 104929998 Camelias 100 — 1.200.000 € / 163 m² = 7.362 €/m²; 'villa reformada' op casco uit 1985, perceel 1.113 m². De duurste echte renovatie per m², vooral omdat de m² klein zijn opgegeven.
3. 104423998 Cumbre del Sol (Grupo CLD) — 1.200.000 € / 190 m² = 6.316 €/m²; 'completamente renovada en 2018', infinity pool, sauna, jacuzzi.
4. 110881013 e.a. Ibiza-villa Dalias — 1.495.000 € / 324 m² = 4.614 €/m²; casco 1988, 'completamente renovada' (2025), 5 slaapkamers en-suite, perceel 1.032 m²; bij 7 makelaars tussen 1.485.000 en 1.700.000 €. Het meest zichtbare renovatieproduct in de zone.
5. 109384452 Kalmias (Keller Williams) — 1.680.000 € / 412 m² = 4.078 €/m²; 'totalmente reformada' op casco 2002 met grafiet-EPS-isolatie, triple glas, Fibaro-domotica — technisch de zwaarste renovatie in de reeks.
6. 110510628 Kalmias/Dalias (RE/MAX) — 1.490.000 € / 428 m² = 3.481 €/m²; 'villa reformada', bouwjaar 1995, hoekperceel 1.758 m² met bijgebouw.
7. 107642605 Camelias 12 — 650.000 € / 250 m² = 2.600 €/m²; 'completamente reformada', bouwjaar 1987. Onderkant van het gerenoveerde aanbod.
8. 110936304 Blue Square, bouwjaar 2020 — 950.000 € / 200 m² = 4.750 €/m²; hetzelfde huis staat bij LT Property met 418 m² (2.273 €/m²) — het schoolvoorbeeld van het m²-probleem.

## 5. Reeks villa_new — alle 17 objecten (gesorteerd op €/m²)

| Code | Zone | Vraagprijs € | m² | €/m² | Bouwjaar (tool/tekst) | detail | Soort | Label | Doublures (zelfde object) | URL |
|---|---|---|---|---|---|---|---|---|---|---|
| 112509895 | CdS | 1.300.000 | 459 | 2.832 | 2026 | ja | en construcción | Century 21: 'villa en construcción', bouwjaar 2026; status bij tool 'para reformar' | — | https://www.idealista.com/es/inmueble/112509895/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 111273264 | CdS | 1.375.000 | 471 | 2.919 | — | ja | en construcción | Villa Nara, Magnolias 123 (Unique Homes): 'actualmente en construcción'; 471 m² = 217 útiles + 141 terras + rest | 112401888; 111271661 (promotie) | https://www.idealista.com/es/obra-nueva/111273264/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 111130564 | Alcassar | 915.000 | 290 | 3.155 | — | nee | promotie | Vall del Portet: tweede geschakelde unit, 290 m² | — | https://www.idealista.com/es/obra-nueva/111130564/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 111130611 | Alcassar | 890.000 | 273 | 3.260 | — | ja | promotie | Vall del Portet (Excent/Aliseda): geschakelde nieuwbouw ('pareado'), notFinished | 111130609 (promotie) | https://www.idealista.com/es/obra-nueva/111130611/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 101278717 | CdS | 1.378.000 | 416 | 3.312 | 2024 | ja | en construcción | Greenwich Village: bouwjaar 2024, 328 m² útiles; 111100574 zegt 'en plena construcción' | 111100574 | https://www.idealista.com/es/inmueble/101278717/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 109456777 | Les Fonts | 925.000 | 225 | 4.111 | — | ja | a estrenar | Racó de Nadal (Leader): 'villa minimalista de diseño de autor a estrenar', perceel 700 m² | — | https://www.idealista.com/es/inmueble/109456777/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 111704123 | CdS | 1.880.000 | 440 | 4.273 | — | ja | promotie | Villa Moraig, Encinas 136 (VITA): notFinished, prijs verlaagd van 2.280.000 (-18%) | 111697231 (promotie) | https://www.idealista.com/es/obra-nueva/111704123/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 110908251 | CdS | 1.200.000 | 280 | 4.286 | — | ja | project | Inmo Plaza Mayor: 'proyecto de villa rústica-moderna', bij Adelfas; alleen render | — | https://www.idealista.com/es/inmueble/110908251/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 112548902 | CdS | 2.155.975 | 471 | 4.577 | — | ja | promotie | López & Henderson: promotie 'Villas Benitachell', notFinished, perceel 878 m² | 112546386 (promotie) | https://www.idealista.com/es/obra-nueva/112548902/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 111499349 | CdS | 1.499.000 | 317 | 4.729 | 2026 | ja | a estrenar | Palmeras 111 p, perceel 535 m²: 'a estrenar', bouwjaar 2026; 317 m² = 192 woning + 125 terras; zelfde huis bij E&V 214 m² (7.005) en Villas de Autor 188 m² (7.973) | 111803869 (214 m²), 111543515 (188 m²) | https://www.idealista.com/es/inmueble/111499349/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 105209614 | CdS | 1.429.000 | 299 | 4.779 | 2024 | ja | a estrenar | Lirios 84: 'obra nueva a estrenar', bouwjaar 2024; 299 m² = 181 woning + 93 terras + 25 parking | — | https://www.idealista.com/es/inmueble/105209614/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 106110267 | CdS | 1.600.000 | 331 | 4.834 | 2021 | ja | a estrenar | Real Villas: 'villa de lujo a estrenar', bouwjaar 2021, bouwgarantie nog geldig | — | https://www.idealista.com/es/inmueble/106110267/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 111787138 | CdS | 2.891.000 | 597 | 4.843 | — | ja | nueva construcción | Villa Rubik, Jazmines (BHHS): 'villa de nueva construcción', 3 niveaus, perceel 1.054 m² | — | https://www.idealista.com/es/inmueble/111787138/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 110511033 | CdS | 2.250.000 | 441 | 5.102 | 2024 | ja | a estrenar | Magnolias 179: 'villa de lujo a estrenar', bouwjaar 2024; 441 m² = 240 woning + 45 kelder + 153 terras | 112368280, 110111013, 108545934 | https://www.idealista.com/es/inmueble/110511033/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 110510885 | CdS | 3.250.000 | 544 | 5.974 | 2025 | ja | a estrenar | Jazmines 140 j: 'obra nueva terminada en 2025', lift, 523 m² útiles; NB Estates geeft 424 m² (7.665 €/m²) | 108977506; 111863984 (424 m²) | https://www.idealista.com/es/inmueble/110510885/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 110880346 | CdS | 1.690.000 | 252 | 6.706 | 2027 | ja | project | Camelias (Coldwell Banker): project, start bouw juni 2026, 14 maanden; tool 'construido en 2027' | — | https://www.idealista.com/es/inmueble/110880346/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 112516125 | Alcassar | 1.650.000 | 207 | 7.971 | — | ja | promotie | Spain Life: promotie 'Villa en Benitachell', notFinished, lift met 4 stops, perceel 1.000 m² | 112512718 (promotie) | https://www.idealista.com/es/obra-nueva/112516125/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |

**Voorbeelden om te onthouden (villa_new):**
1. 112516125 Alcassar (Spain Life) — 1.650.000 € / 207 m² = 7.971 €/m²; promotie in aanbouw, lift met 4 stops, perceel 1.000 m². Hier zijn de m² krap opgegeven (alleen woning), vandaar de hoge €/m².
2. 110510885 Jazmines 140 j — 3.250.000 € / 544 m² = 5.974 €/m²; 'obra nueva terminada en 2025', lift, gastenappartement; NB Estates geeft 424 m² (7.665 €/m²). Het duurste nieuwbouwobject in absolute prijs.
3. 110511033 Magnolias 179 — 2.250.000 € / 441 m² = 5.102 €/m²; 'a estrenar', bouwjaar 2024; 240 m² woning + 45 m² kelder + 153 m² terras.
4. 105209614 Lirios 84 — 1.429.000 € / 299 m² = 4.779 €/m²; 'obra nueva a estrenar', bouwjaar 2024; 181 m² woning + 93 m² terras + 25 m² parking.
5. 111499349 Palmeras 111 p — 1.499.000 € / 317 m² = 4.729 €/m²; bouwjaar 2026; bij E&V 214 m² (7.005) en bij Villas de Autor 188 m² (7.973) — één huis, drie m²-opgaven.
6. 111704123 Villa Moraig, Encinas 136 — 1.880.000 € / 440 m² = 4.273 €/m²; promotie bij Cala Moraig, prijs verlaagd van 2.280.000 (-18%).
7. 111273264 Villa Nara, Magnolias 123 — 1.375.000 € / 471 m² = 2.919 €/m²; in aanbouw; 217 m² nuttig + 141 m² terras. Laagste €/m² van de reeks, uitsluitend door de ruime m²-opgave.
8. 111130611 Vall del Portet (Alcassar) — 890.000 € / 273 m² = 3.260 €/m²; geschakelde nieuwbouw ('pareado'), promotie; geen vrijstaande villa, daarom apart gevlagd.

## 6. Reeks townhouse_renovated — 5 objecten (casco + urbanisaties)

Casco Poble Nou (Centro) telt op de peildatum slechts **2 unieke gerenoveerde objecten** (n < 6). Ter aanvulling de drie gerenoveerde adosados in urbanisaties (Las Mimosas/Calistros en Cumbre del Sol), apart gelabeld. De rest van het casco-aanbod is "para reformar" of "parcialmente reformado" (uitgesloten).

| Code | Zone | Vraagprijs € | m² | €/m² | Bouwjaar (tool/tekst) | detail | Soort | Label | Doublures (zelfde object) | URL |
|---|---|---|---|---|---|---|---|---|---|---|
| 111508676 | Centro | 365.000 | 197 | 1.853 | 1930 | ja | gerenoveerd | Casa de pueblo ibicenco, Calle de l'Església: reforma integral 2019/2020, 3 lagen, patio; 6 agents met 192–219 m² | 111087573 (192), 111486866 (192), 111601082 (192), 111947534 (197), 111937710 (197), 110907230 (200), 110948222 (219) | https://www.idealista.com/es/inmueble/111508676/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 112205586 | Centro | 435.000 | 202 | 2.153 | 1940 | ja | gerenoveerd | Hoekhuis casco (Blue Square): 'reformada íntegramente en 2026', nieuw dak/gevel/installaties, 4 lagen | — | https://www.idealista.com/es/inmueble/112205586/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 110955242 | CdS | 190.000 | 70 | 2.714 | 2006 | ja | gerenoveerd | Zurbarán (El Portet): 'reformado en 2016', bouwjaar 2006; 70 m² incl. beglaasd terras | 109778069 | https://www.idealista.com/es/inmueble/110955242/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 110120728 | CdS | 260.000 | 90 | 2.889 | — | ja | gerenoveerd | Thomas-Wilson 51 (particulier): 'recién reformada', 60 m² útiles | — | https://www.idealista.com/es/inmueble/110120728/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 109365710 | Calistros | 350.000 | 96 | 3.646 | 1999 | ja | gerenoveerd | Las Mimosas (Unique Homes): 'reformada en 2025', geschakeld, perceel 140 m² | — | https://www.idealista.com/es/inmueble/109365710/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |

**Voorbeelden (townhouse_renovated):**
1. 112205586 Centro (Blue Square) — 435.000 € / 202 m² = 2.153 €/m²; hoekhuis uit 1940, 'reformada íntegramente en 2026' met nieuw dak, gevel en installaties, 4 lagen, dakterras met zeezicht.
2. 111508676 e.a. Calle de l'Església — 365.000 € / 197 m² = 1.853 €/m²; dorpshuis uit 1930, reforma integral 2019/2020, Ibiza-stijl, patio, dakterras met zicht op zee en Peñón; bij 8 makelaars met 192–219 m². Verkoopfoto's deels digitaal gemeubileerd.
3. 109365710 Las Mimosas (Calistros) — 350.000 € / 96 m² = 3.646 €/m²; geschakelde woning uit 1999, 'reformada en 2025', gemeenschappelijke zwembaden.
4. 110120728 Thomas-Wilson 51, Cumbre del Sol — 260.000 € / 90 m² = 2.889 €/m²; particulier, 'recién reformada', 60 m² nuttig.
5. 110955242 Zurbarán, Cumbre del Sol — 190.000 € / 70 m² = 2.714 €/m²; 'reformado en 2016', bouwjaar 2006; twee makelaars.

## 7. Reeks apartment_renovated — 9 objecten (Cumbre del Sol, 1× Alcassar)

| Code | Zone | Vraagprijs € | m² | €/m² | Bouwjaar (tool/tekst) | detail | Soort | Label | Doublures (zelfde object) | URL |
|---|---|---|---|---|---|---|---|---|---|---|
| 111284282 | CdS | 190.000 | 90 | 2.111 | 2010 | nee | gerenoveerd | Zurbarán 47: 'interior renovado', bouwjaar 2010 [claim agent] | — | https://www.idealista.com/es/inmueble/111284282/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 110755051 | CdS | 259.000 | 109 | 2.376 | 2002 | ja | gerenoveerd | Pueblo de la Paz dúplex, Rotblat 4: 'reformada recientemente', bouwjaar 2002; 109 m² = 73 woning + 18 terras + 18 tuin | — | https://www.idealista.com/es/inmueble/110755051/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 111168791 | CdS | 282.000 | 97 | 2.907 | 2002 | ja | gerenoveerd | Pueblo Panorama: 'vivienda renovada', bouwjaar 2002, 68 m² útiles | — | https://www.idealista.com/es/inmueble/111168791/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 112441505 | Alcassar | 265.000 | 86 | 3.081 | — | nee | gerenoveerd | Villotel-Benirrama (Alcassar): 'renovado y listo para entrar a vivir' | — | https://www.idealista.com/es/inmueble/112441505/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 111419972 | CdS | 219.000 | 66 | 3.318 | — | ja | gerenoveerd | NB Estates: 'interior reformado', ático 2 slk | — | https://www.idealista.com/es/inmueble/111419972/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 112012203 | CdS | 890.000 | 248 | 3.589 | 2016 | ja | gerenoveerd | Novamar Suites II, Atalaya 12 a: bouwjaar 2016, 'reformado en profundidad en 2025'; 248 m² = 122 binnen + 70 terras + 56 gemeenschappelijk | — | https://www.idealista.com/es/inmueble/112012203/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 110959894 | CdS | 239.000 | 63 | 3.794 | 1998 | ja | gerenoveerd | Pueblo de la Paz, Cordell Hull 4: 'reformado', bovenwoning, bouwjaar 1998 | 111522538 (58 m²), 111586472 (249.000, Adelfas 1) | https://www.idealista.com/es/inmueble/110959894/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 112369674 | CdS | 510.000 | 127 | 4.016 | 1990 | ja | gerenoveerd | Pueblo de la Luz 162: 'remodelación interior concluida en 2026', bouwjaar 1990; 129 m² incl. 8 m² gemeenschappelijk + 14 m² trastero | — | https://www.idealista.com/es/inmueble/112369674/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 110844494 | CdS | 475.000 | 109 | 4.358 | 2005 | ja | gerenoveerd | Pueblo Panorama dúplex (Select Villas): 'bellamente reformado, recientemente renovada', bouwjaar 2005 | — | https://www.idealista.com/es/inmueble/110844494/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |

**Voorbeelden (apartment_renovated):**
1. 110844494 Pueblo Panorama dúplex — 475.000 € / 109 m² = 4.358 €/m²; 'bellamente reformado', bouwjaar 2005, 180°-zeezicht; prijs verlaagd van 495.000.
2. 112369674 Pueblo de la Luz 162 — 510.000 € / 127 m² = 4.016 €/m²; casco 1990, 'remodelación interior concluida en 2026' door interieurontwerper, klifrand; 86,7 m² binnen.
3. 110959894 Pueblo de la Paz — 239.000 € / 63 m² = 3.794 €/m²; 'reformado', bouwjaar 1998, bovenwoning in complex van 8; ook aangeboden als 58 m² en op 249.000 €.
4. 112012203 Novamar Suites II — 890.000 € / 248 m² = 3.589 €/m²; bouwjaar 2016, 'reformado en profundidad en 2025'; 122 m² binnen + 70 m² terras + 56 m² gemeenschappelijk meegeteld.
5. 110755051 Pueblo de la Paz dúplex — 259.000 € / 109 m² = 2.376 €/m²; 'reformada recientemente', bouwjaar 2002; 73 m² woning + terrassen + tuin.

## 8. Reeks apartment_new — 10 objecten (Cumbre del Sol)

Nieuwbouwappartementen zijn er alleen in Cumbre del Sol (Montecala Gardens / Pueblo Montecala, Jardines Montecarlo, Calle Greco). Let op de spreiding: de promotie-units van SJW geven alleen de woning-m² (4.579–6.543 €/m²), makelaars die dezelfde promotie doorverkopen tellen terras en gemeenschappelijke delen mee (2.489–2.720 €/m²). Drie advertenties dragen dezelfde prijs (473.000 €) met 83, 176 en 190 m² — vermoedelijk de "vanaf"-prijs van de promotie.

| Code | Zone | Vraagprijs € | m² | €/m² | Bouwjaar (tool/tekst) | detail | Soort | Label | Doublures (zelfde object) | URL |
|---|---|---|---|---|---|---|---|---|---|---|
| 111087729 | CdS | 473.000 | 190 | 2.489 | — | ja | nieuw | Montecala Gardens, Palmeras (Costa Soñada): nieuwbouw, oplevering 2026, 109 m² útiles | — | https://www.idealista.com/es/inmueble/111087729/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 110881337 | CdS | 473.000 | 176 | 2.688 | — | ja | nieuw | Coldwell Banker: 'dúplex de nueva construcción', 106 m² útiles; status bij tool 'para reformar' (fout) | — | https://www.idealista.com/es/inmueble/110881337/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 109808739 | CdS | 389.000 | 143 | 2.720 | 2025 | ja | nieuw | Montecala Gardens, Greco 21 (CdS Pre-Owned): 'a estrenar', bouwjaar 2025; 143 m² = 91 binnen + 23 terras + 29 gemeenschappelijk | — | https://www.idealista.com/es/inmueble/109808739/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 106847061 | CdS | 355.000 | 116 | 3.060 | — | ja | nieuw | Jardines Montecarlo (Sky Blue): 'terminado en 2024' | — | https://www.idealista.com/es/inmueble/106847061/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 109493518 | CdS | 355.000 | 114 | 3.114 | 2023 | ja | nieuw | Calle Greco (Adam & Behrens): 'nueva construcción', bouwjaar 2023; 114 m² = 91 woning + 23 terras | — | https://www.idealista.com/es/inmueble/109493518/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 112440344 | CdS | 499.150 | 109 | 4.579 | — | nee | nieuw | Montecala Gardens: dúplex 2 slk | — | https://www.idealista.com/es/obra-nueva/112440344/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 112440545 | CdS | 612.000 | 117 | 5.231 | — | ja | nieuw | Montecala Gardens: piso 3 slk; promotie 'finished' | — | https://www.idealista.com/es/obra-nueva/112440545/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 112440537 | CdS | 593.000 | 105 | 5.648 | — | nee | nieuw | Montecala Gardens: piso 3 slk | — | https://www.idealista.com/es/obra-nueva/112440537/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 112440488 | CdS | 473.000 | 83 | 5.699 | — | nee | nieuw | Montecala Gardens: ático 2 slk | — | https://www.idealista.com/es/obra-nueva/112440488/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 112440425 | CdS | 687.000 | 105 | 6.543 | — | nee | nieuw | Montecala Gardens (SJW, promotie 'terminada'): ático 3 slk | — | https://www.idealista.com/es/obra-nueva/112440425/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |

**Voorbeelden (apartment_new):**
1. 112440425 Montecala Gardens ático 3 slk — 687.000 € / 105 m² = 6.543 €/m²; promotie 'terminada' (SJW).
2. 112440545 Montecala Gardens piso 3 slk — 612.000 € / 117 m² = 5.231 €/m²; detail bevestigt promotie 'finished'.
3. 109493518 Calle Greco (Adam & Behrens) — 355.000 € / 114 m² = 3.114 €/m²; bouwjaar 2023, 91 m² woning + 23 m² terras.
4. 106847061 Jardines Montecarlo — 355.000 € / 116 m² = 3.060 €/m²; 'terminado en 2024'.
5. 109808739 Montecala Gardens, Greco 21 (CdS Pre-Owned) — 389.000 € / 143 m² = 2.720 €/m²; 'a estrenar', bouwjaar 2025; 91 m² binnen + 23 m² terras + 29 m² gemeenschappelijk.
6. 111087729 Montecala Gardens (Costa Soñada) — 473.000 € / 190 m² = 2.489 €/m²; oplevering 2026, 109 m² nuttig.

## 9. Afgevallen — opvallende gevallen

| Code | Vraagprijs / m² | Waarom niet opgenomen |
|---|---|---|
| 111522274 | 1.250.000 / 247 | 'villa moderna', maar bouwjaar 2013 (tool) en geen renovatieclaim — net onder de drempel ≥ 2014 |
| 102364128 | 585.000 / 330 | 'la villa ha sido renovada' zonder datum of omvang; bouwjaar 1987; te vage claim |
| 110008894 | 2.350.000 / 451 | 'completamente renovada', maar reforma afgerond in 2006; rustieke elegantie |
| 111136902 (+5× Paichi) | 1.990.000 / 434 | Golden Valley, 'renovada en 2011'; label deels Moraira |
| 109842635 | 720.000 / 330 | 'estilo ibicenco, acabados contemporáneos' — geen renovatie- of bouwjaarclaim |
| 112086939 | 1.850.000 / 621 | 'excelente estado' zonder renovatie- of bouwjaarclaim |
| 111449053, 112278071, 109627299 | 520.000–950.000 | 'parcialmente reformada' / 'requiere reforma parcial' / 'para reformar' |
| 112093174, 110724631, 112145044 | 449.000–475.000 / 217–220 | bouwjaar 1996, alleen badkamers vernieuwd |
| 111331198, 112093187 | 599.000 / 101 | Golden Valley: alleen keuken 'completamente renovada' |
| 111712601 | 1.850.000 / 870 | nieuwbouw (FALC), maar 870 m² is het perceel — geen bruikbaar m²-veld |
| 112198822 | 175.000 / 50 | appartement 'parcialmente reformado en 2023' |
| 111560913 | 263.000 / 129 | dúplex casco: alleen keuken 'totalmente reformada' |
| 107852674, 109175336, 110822871 | 250.000–330.000 | casco/finca: 'potencial de ser renovada', 'partially renovated 1960', 'requiere renovación completa' |

## 10. Kanttekeningen

1. **Vraagprijzen, geen transacties.** Alles hierboven is aanbod op Idealista op 15-09-2026. Prijsverlagingen die de tool meldt (Villa Moraig -18%, Girasoles-villa -14%, Pueblo Panorama -4%) laten zien dat de eerste vraagprijs hier regelmatig te hoog zit. Verkoopprijzen vragen een andere bron (notariële registers, Registradores, taxatiedata).
2. **Steekproef.** villa_renovated (n=37) en villa_new (n=17) zijn stevig genoeg voor een mediaan; de deelreeksen "gerenoveerd" (n=11), townhouse (n=2 casco / 5 totaal), apartment_new (n=10, sterk vertekend) en apartment_renovated (n=9) zijn indicatief. Vier prijsbanden overschreden de 50-limiet van de tool, dus enkele advertenties in de gemeente zijn niet gezien.
3. **m²-definitie.** "m² construidos" is in deze zone geen vaste maat: makelaars geven voor hetzelfde huis 188 tot 317 m² (Palmeras 111 p), 200 tot 418 m² (Blue Square/LT villa 2020) of 424 tot 544 m² (Jazmines 140 j). Nieuwbouw en appartementen tellen terrassen, kelders, parking en zelfs gemeenschappelijke delen mee. Gebruik de €/m² als eerste zeef, nooit als taxatie.
4. **Zonelabels.** "Cumbre del Sol" bij de tool omvat ook de randzones Encinas/Adelfas/Fresnos bij de klif én de lagere zones Kalmias/Magnolias/Palmeras bij Moraira; binnen die ene zone verschillen ligging en uitzicht enorm (eerste lijn klif tegenover binnenland). "Centro, Benitachell" is deels het casco, deels een verzamellabel voor villa's zonder straatnaam. Poble Nou de Benitatxell als eigen zone bestaat bij de tool niet.
5. **Gerenoveerd versus modern.** De reeks villa_renovated mengt bewust twee producten (gerenoveerd casco en modern gebouwd ≥ 2014, tweedehands); de deelmedianen (3.738 tegenover 5.320) zeggen meer dan de totaalmediaan (4.614). Vier moderne villa's dragen [claim agent] omdat een bouwjaar ontbreekt.
6. **Dubbele advertenties en prijsverschillen.** Meerdere objecten staan bij 3–8 makelaars, soms met 100–200 k€ prijsverschil (1.485.000–1.700.000 voor dezelfde villa; 1.680.000–1.890.000 voor Kalmias). Voor elk zo'n object is de meest voorkomende of best onderbouwde vermelding gekozen; de doublures staan in de tabel.
7. **Geen kandidaten.** Dit bestand levert alleen referentieprijzen. Het is niet gecontroleerd op vergunbaarheid, kadaster of bouwkundige staat; niets hiervan is een koopadvies.

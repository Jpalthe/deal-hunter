# H01 — Tegenspraak op de vergelijkingsprijzen zone `puerto_arenal`

**Gecontroleerd bestand:** `onderzoek/H01-comparables-puerto_arenal.md` (niet aangepast).
**Rol:** tegenspreker. **Controledatum:** 15-09-2026. **Bron:** officiële Idealista-assistent (MCP `property_detail` + `search_properties`, locale es-ES, country es, maxResults ≤ 50). Bewijstype 2: portaaldata via de officiële tool; het oordeel is van de agent.
Alle bedragen zijn **vraagprijzen** (advertenties), geen transactieprijzen. €/m² = vraagprijs / m² gebouwd zoals de tool die geeft.

## 1. Oordelentabel

| Reeks | Oordeel | Kern | Gecorrigeerd (n / p25 / mediaan / p75) |
|---|---|---|---|
| **villa_renovated** (n=12, mediaan 6.253) | **Bevestigd, met kanttekening** | 4 objecten geopend (goedkoopste en duurste €/m² erbij): prijs, m² en €/m² kloppen. Onafhankelijke zoekopdracht: mediaan 6.254 (0 % t.o.v. 6.253; −7,5 % t.o.v. Puerto 6.759), dus binnen ±15 %. Rekenkunde klopt. **Waarschijnlijk dubbel:** 112209448 en 112265864 (zie §2.1). Dat is niet sluitend te bewijzen, dus alleen als gevoeligheid meegenomen. De mediaan valt precies in een gat tussen 5.749 en 6.757: haal je één lage waarde weg, dan springt hij naar 6.757. | Gevoeligheid (als het een dubbel is): n=11 / 4.280–4.529 / **6.757** / 7.335. El Arenal dan n=2: **te klein voor een betrouwbare mediaan**. |
| **villa_new** (n=2, mediaan 8.318) | **Bevestigd als gegevens, onbruikbaar als mediaan** | Beide objecten geopend: prijs, m² en status (in aanbouw) kloppen. Rekenkunde klopt. De onafhankelijke zoekopdracht vindt er maar 1 (110755799): Villa Imperio staat bij Idealista als "para reformar" en valt dus buiten het filter obra nueva. Het origineel zegt dat zelf ook. | **n=2: te klein voor een betrouwbare mediaan.** |
| **apartment_renovated** (n=45, mediaan 4.235) | **Weerlegd** (ontdubbeling fout) | Alle 11 geopende advertenties hebben de prijs en m² uit het origineel en zijn volgens de tekst gerenoveerd (geen "para reformar"). Maar de ontdubbeling op "zelfde prijs + zelfde m²" mist dubbels waarbij makelaars verschillende m² opgeven. Bewezen: **4 advertenties zijn één appartement** in Puerto, en **2 andere advertenties zijn één duplex** aan de Calle Churruca (§2.3). De mediaan van de hele reeks verandert nauwelijks (−1 %), maar n, de kwartielen en vooral de deelreeks Puerto wel. | **n=41 / 3.457 / 4.189 / 5.000** (min 2.633, max 6.611). |
| – deelreeks **apartment_renovated_puerto** (n=10, mediaan 5.024; **deze gebruikt de rekenaar voor K06**) | **Weerlegd** | Na ontdubbeling blijven 6 unieke objecten over. De onafhankelijke zoekopdracht vindt dezelfde 10 advertenties, inclusief dezelfde dubbels. | **n=6 / 3.924 / 4.803 / 5.468** (representant = laagste code, zoals het origineel voorschrijft). Welke advertentie je als representant neemt, bepaalt de mediaan: 4.515–4.803. **n=6: nauwelijks betrouwbaar.** |
| – deelreeks Puerto 80–150 m² (n=4, mediaan 4.515) | **Weerlegd** | 109870004 en 110279888 zijn hetzelfde appartement. | n=2–3, mediaan 4.032–4.286: **te klein voor een betrouwbare mediaan**. |
| **apartment_new** (n=43, mediaan 3.944) | **Bevestigd** | 5 objecten geopend (goedkoopste, duurste, het enige in Puerto en een mogelijk dubbel paar): alles klopt. Onafhankelijke zoekopdracht: 34 obra-nueva-units in El Arenal, mediaan 3.720 (−5,7 %), dus binnen ±15 %. Alle 34 codes staan in het origineel en er zijn geen dubbels op prijs + m². Rekenkunde klopt (p25 3.411 tegenover 3.412 is een afrondingsverschil). Puerto heeft n=1: **te klein voor een betrouwbare mediaan**. | – |
| **townhouse_renovated** | **Niet te controleren** | Het bestand heeft voor deze zone geen reeks ("geen aparte reeks", §7). Het noemt alleen 5 losse advertenties (Puerto 2, El Arenal 3). In `kader/comparables.json` staat ook geen `townhouse_renovated` onder `puerto_arenal`. | n ≤ 3 per zone: **te klein voor een betrouwbare mediaan**. |

**Kern voor Jan:** de nieuwbouwreeks klopt. Voor gerenoveerde villa's ligt de vraagprijs grofweg tussen 6.250 en 6.750 €/m²; bij zo'n kleine reeks is het cijfer gevoelig voor één advertentie meer of minder. Het belangrijkste punt: **de Puerto-vergelijking voor K06 is te rooskleurig**. Er staan dubbele advertenties in: hetzelfde appartement bij vier makelaars, telkens met andere m². Na ontdubbeling is de mediaan 4.500–4.800 €/m² vraagprijs, op n=6, in plaats van 5.024 op n=10. De ondergrens p25 zakt van 4.400 naar 3.924. De band van 3.800–4.900 €/m² die het origineel voor K06 noemt, blijft verdedigbaar, maar leunt nu op 2–3 objecten van 80–150 m². Het blijven vraagprijzen: er is geen transactiebewijs.

## 2. Toelichting per reeks

### 2.1 villa_renovated

**Controle 1 — `property_detail` (4 geopend)**

| Code | In de tool (prijs / m² / €/m²) | Klopt met origineel | Staat en claim volgens de tool | Oordeel |
|---|---|---|---|---|
| 111071067 (laagste €/m²) | 2.600.000 / 795 / 3.270; "Construido en 1983"; 653 m² nuttig | ja | Segunda mano/buen estado. De tekst noemt het een villa moderna, met een keuken die 1,5 jaar geleden is vernieuwd en recent vernieuwde elektra | Past binnen de eigen regel van het origineel ("villa moderna"), maar de renovatieclaim is dun. Het origineel zegt dat zelf ook (gevoeligheidsregel). |
| 108111394 (hoogste €/m²) | 2.750.000 / 240 / 11.458; gebouwd 2020 | ja | buen estado; villa contemporánea van 2020 | Modern, niet gerenoveerd. Past binnen de definitie "gerenoveerd óf modern". Uitschieter. |
| 112209448 | 1.250.000 / 290 / 4.310; perceel 1.695 m²; 6 slk / 4 badk | ja | buen estado; "bellamente renovada", "modernizada" | Gerenoveerd volgens de tekst. |
| 112265864 | 1.250.000 / 260 / 4.808; perceel 1.700 m²; 6 slk / 4 badk; energielabel C | ja | buen estado; "Completamente reformado en 2018" | Gerenoveerd. |

Geen van de vier is "para reformar" of nieuwbouw.

**Waarschijnlijk dubbel: 112209448 en 112265864.** Ze hebben dezelfde vraagprijs (1.250.000 €), hetzelfde aantal slaap- en badkamers (6 / 4) en vrijwel hetzelfde perceel (1.695 tegenover 1.700 m²). Beide liggen aan de Cap de la Nau bij El Arenal, met zwembad en gedeeltelijk zeezicht. Ze staan bij verschillende makelaars en de m² verschillen (290 tegenover 260). Het origineel vond voor 112265864 al 5 andere advertenties met dezelfde prijs en m², dus deze villa wordt breed aangeboden. Toch is dit niet sluitend: twee vergelijkbare villa's in dezelfde urbanisatie zijn niet uitgesloten. Daarom staat het alleen als gevoeligheid in de tabel: n=11, mediaan 6.757. Zonder 111071067 én zonder deze dubbel komt de mediaan ook op 6.757–6.758 uit.

**Controle 2 — onafhankelijke zoekopdracht.** Opdracht: "villa totalmente reformada con vistas al mar en Puerto, Jávea/Xàbia" (CHALET). De tool paste toe: Puerto · villas · buen estado · zeezicht. Resultaat: 15 advertenties, allemaal opgehaald. Op tekst gerenoveerd of modern, zonder "para reformar": 111071067 (met dubbel 110604173), 109709911, 111286574 en 108111394. Die geven n=4 en mediaan **6.254 €/m²**: −7,5 % tegenover Puerto 6.759 en 0 % tegenover 6.253. Dat valt binnen ±15 %. 111343157 (het nieuwbouwproject Villa Imperio) zit er ook tussen; het origineel heeft dat terecht naar villa_new verplaatst.

**Controle 3 — rekenkunde.** Nagerekend op de 12 regels uit de volledige tabel (percentielen lineair geïnterpoleerd). Totaal, Puerto, El Arenal en de beide gevoeligheidsregels komen op het cijfer uit; alleen p25 van de reeks zonder 111071067/108111394 is 4.435 in plaats van 4.434 (afronding). Er zijn geen dubbels op prijs + m² over het hoofd gezien.

### 2.2 villa_new

| Code | In de tool | Klopt | Status | Kanttekening |
|---|---|---|---|---|
| 111823302 Villa Imperio | 3.950.000 / 580 / 6.810; "Construido en 2027"; 455 m² nuttig | ja | Idealista-staat "Segunda mano/para reformar", maar de tekst zegt nieuwbouw in vergevorderde uitvoering, met de structuur klaar | Nieuwbouw op plan. De staat bij Idealista is fout, zoals het origineel ook zegt. |
| 110755799 Villa Azure | 3.950.000 / 402 / 9.826; `promotionType: notFinished`; oplevering laatste kwartaal 2027 | ja | Promoción de obra nueva | De 402 m² bevatten volgens de tekst 44 m² terras. Op 358 m² woning is het 11.034 €/m². |

**Onafhankelijke zoekopdracht:** "chalet de obra nueva en construcción en Puerto, Jávea/Xàbia" (CHALET). De tool paste toe: Puerto · casas y chalets · obra nueva. Totaal **1** (110755799, 9.826 €/m²). Een vergelijking met ±15 % heeft bij n=1 tegenover n=2 geen betekenis. Rekenkunde (6.810 en 9.826 → p25 7.564, mediaan 8.318, p75 9.072) klopt. **Te klein voor een betrouwbare mediaan.** Het gaat om prijzen op plan, niet om opgeleverde woningen.

### 2.3 apartment_renovated

**Controle 1 — `property_detail` (11 geopend)**

| Code | Zone | In de tool (prijs / m² gebouwd / €/m²) | Kamers / verdieping | Renovatieclaim (tool) | Klopt |
|---|---|---|---|---|---|
| 112219701 (laagste €/m²) | El Arenal | 395.000 / 150 (120 nuttig) / 2.633 | 3 slk · 1e verd. | "recientemente renovado"; verkocht met huurders | ja |
| 112431449 (hoogste €/m²) | Puerto | 389.000 / 40 / 9.725 | 2 slk · 2 badk · twee bovenste verdiepingen | "meticulosamente renovada" | ja (m² onwaarschijnlijk, zoals het origineel zegt) |
| 109870004 | Puerto | 389.000 / 82 / 4.744; bouwjaar 1960 | 2 / 2 · twee niveaus | "completamente reformado"; de tekst noemt 40 m² | ja |
| 108883032 | Puerto | 389.000 / 70 / 5.557 | 2 / 2 | "recientemente reformado" | ja |
| 110279888 | Puerto | 389.000 / 80 (70 nuttig) / 4.863 | 2 / 2 | "perfectamente renovado" | ja (tool 4.863; origineel 4.862 = afronding) |
| 108899315 | Puerto | 389.000 / 75 / 5.187 | 2 / 2 · duplex · 2e verd. | "completamente modernizada en 2025" | ja |
| 108819856 | Puerto | 399.000 / 75 (60 nuttig) / 5.320; bouwjaar 1960 | 2 / 2 · duplex · 2e verd. | "reformada completamente en 2025" | ja |
| 110905573 | El Arenal | 389.000 / 78 (70) / 4.987 | 2 / 2 · 3e verd. | "recién reformado" (particuliere verkoper; naam niet overgenomen) | ja |
| 112214123 | El Arenal | 390.000 / 78 / 5.000 | 2 / 2 · 3e verd. | "completamente reformado" | ja |
| 111759336 | El Arenal | 399.999 / 78 / 5.128 | 2 / 2 · 3e verd. | "reformado recientemente" | ja |
| 112521823 | El Arenal | 414.000 / 78 / 5.308 | 2 / 2 · 3e verd. | "completamente reformado"; label D | ja |

Geen enkele advertentie is "para reformar". Prijs, m² en €/m² kloppen bij alle 11.

**Bewezen dubbels die het origineel mist.** De ontdubbelregel "zelfde prijs + zelfde m² + zelfde zone" werkt niet als makelaars verschillende m² opgeven.

| Cluster | Advertenties (m² → €/m²) | Bewijs |
|---|---|---|
| **A: één appartement, Puerto, 389.000 €** | 108883032 (70 → 5.557), 109870004 (82 → 4.744), 110279888 (80 → 4.862), 112431449 (40 → 9.725) | (1) 109870004 en 108883032 hebben een **identiek energiecertificaat**: verbruik F 195 kWh/m²·jaar en uitstoot E 40 kg CO2/m²·jaar. (2) 108883032 en 110279888 hebben bijna letterlijk dezelfde tekst: 2 dubbele slaapkamers en 2 badkamers, bij de playa La Grava, open keuken, terras met zeezicht en zonsondergang boven de Montgó. (3) 112431449 en 109870004 beschrijven dezelfde indeling: twee niveaus, op elk een slaapkamer met badkamer, dakterras met zeezicht. Beide noemen 40 m². Alle vier: 389.000 €, 2 slk / 2 badk, Puerto, geen lift. |
| **B: één duplex, Calle Churruca** | 108819856 (399.000 / 75 → 5.320), 108899315 (389.000 / 75 → 5.187; plus de al bekende dubbel 110085576) | Zelfde straat, duplex, 75 m², 2e verdieping, geen lift, gerenoveerd in 2025. Dezelfde indeling: beneden slaapkamer, salon, balkon, keuken en badkamer; boven slaapkamer en badkamer; terras van 15 m² met panoramazicht, ingericht voor paella en barbecue. Alleen de vraagprijs verschilt. |
| Mogelijk A = B | – | Beide in Puerto, bouwjaar 1960, 2/2 op twee niveaus. Maar de energiecertificaten verschillen (F/E tegenover C/D). **Niet bewezen**, dus niet samengevoegd. |
| **Mogelijk: El Arenal, Urb. La Isla, 78 m²** | 110905573 (389.000), 112214123 (390.000), 111463998 (395.000, niet geopend), 111759336 (399.999), 112521823 (414.000) | Alle vijf: 78 m², 2 slk / 2 badk, 3e verdieping, op het zuiden, twee terrassen (één bij de hoofdslaapkamer), gemeenschappelijk zwembad en parkeerplaats, gerenoveerd. La Isla is echter een groot complex met veel gelijke units. De teksten, afwerking en energielabels verschillen (vrijgesteld / G / G / D). **Niet bewezen.** Alleen gevoeligheid: als het één object is, dan geldt voor de hele reeks n=37, p25 3.442, mediaan 4.119, p75 4.700. |

**Gecorrigeerde cijfers** (clusters A en B elk één object; representant = laagste code, de terugvalregel van het origineel):

| Reeks | Origineel | Gecorrigeerd | Spreiding door keuze van representant |
|---|---|---|---|
| apartment_renovated (totaal) | 45 / 3.580 / 4.235 / 5.064 | **41 / 3.457 / 4.189 / 5.000** | mediaan 4.189 in alle varianten; p75 4.990–5.000 |
| · Puerto | 10 / 4.400 / 5.024 / 5.468 | **6 / 3.924 / 4.803 / 5.468** | mediaan 4.515–4.803; p75 5.076–5.468 |
| · El Arenal | 35 / 3.401 / 4.174 / 4.988 | ongewijzigd (afronding 4.989) | – |
| · Puerto 80–150 m² | 4 / 4.159 / 4.515 / 4.774 | 2–3 objecten, mediaan 4.032–4.286 | te klein |
| · Puerto + Arenal 80–150 m² | 23 / 3.232 / 3.778 / 4.463 | 21–22 / 3.130–3.181 / 3.636–3.707 / 4.235–4.273 | – |

**Controle 2 — onafhankelijke zoekopdracht.** Opdracht: "piso completamente reformado en Puerto, Jávea/Xàbia" (HOME). De tool paste toe: Puerto · pisos · buen estado. Totaal 58, opgehaald 50 (limiet van de tool). Op tekst gerenoveerd, zonder deelrenovatie: precies dezelfde 10 advertenties als het origineel, plus de bekende dubbels 111665579, 110602085 en 110085576. Twee advertenties noemen alleen "diseño contemporáneo" (112106274, 112510218); die tellen volgens de regel van het origineel niet bij appartementen. Mediaan zonder ontdubbeling: 5.025, dus het origineel is reproduceerbaar. Na ontdubbeling: 4.515–4.803 (−4 % tot −10 %). De les zit dus niet in de zoekopdracht maar in de ontdubbelregel.

**Controle 3 — rekenkunde.** Op de 45 regels van de volledige tabel klopt alles, inclusief de vijf gevoeligheidsregels. Enige afwijking: Puerto-mediaan 5.025 in plaats van 5.024 (afronding).

### 2.4 apartment_new

| Code | In de tool | Klopt | Status |
|---|---|---|---|
| 110963269 (laagste €/m²) | 440.000 / 270 (55 nuttig) / 1.630 | ja | promotie Marina Bay Sunset, `notFinished`, begane grond met tuin. De €/m² is vertekend, zoals het origineel ook zegt. |
| 109077990 (hoogste €/m²) | 771.000 / 92 / 8.380 | ja | promotie Arenal Jávea Beach, ático, `notFinished` |
| 110983899 (enige in Puerto) | 495.000 / 90 (77 nuttig) / 5.500; "Construido en 2026"; label A | ja | Staat bij Idealista als "segunda mano/buen estado", maar is volgens de tekst modern en gebouwd in 2026. Nieuwbouw, terecht. |
| 111003829 (dubbelcheck) | 500.000 / 104 / 4.808; 2 slk · 2 badk; 122 m² buitenruimte | ja | Tekst: obra nueva. Mogelijk dezelfde unit als 111035010 (490.000 / 103 m², 110 m² terras). Die heeft volgens de tool echter **3** slaapkamers, dus geen bewezen dubbel. |

**Onafhankelijke zoekopdracht:** "apartamento de nueva construcción en El Arenal, Jávea/Xàbia" (HOME). De tool paste toe: El Arenal · pisos · obra nueva. Totaal 34, allemaal opgehaald, allemaal status `newdevelopment`, geen dubbels op prijs + m². Uitkomst: n=34, p25 3.275, **mediaan 3.720**, p75 5.114. Dat is −5,7 % tegenover 3.944 en −4,0 % tegenover El Arenal 3.876, dus binnen ±15 %. De 9 "segunda mano"-advertenties met nieuwbouwsignaal (het verschil tussen 34 en 43) vallen buiten dit filter; ze trekken de mediaan van het origineel iets omhoog. Rekenkunde op de 43 regels klopt (p25 3.411 tegenover 3.412 is afronding). Heterogeen: units van 175–314 m² drukken de onderkant, strandunits ≤ 100 m² van 6.000–8.400 €/m² de bovenkant. Het origineel geeft daarvoor terecht gevoeligheidsregels.

### 2.5 townhouse_renovated

Het bestand heeft voor deze zone geen reeks. Het noemt 5 losse advertenties: Puerto 112374691 en 110117537; El Arenal 107723159, 112412197 en 112197785. Omdat er geen reeks is, is er niets te bevestigen of te weerleggen. Die advertenties zijn niet geopend: zuinig werken, en het zijn er te weinig voor een mediaan. **Te klein voor een betrouwbare mediaan.**

## 3. Gevolgen voor de rekenaar

- `apartment_renovated_puerto` (K06, scenario R_integraal) gebruikt nu n=10, p25 4.400 en mediaan 5.024. Voorstel: **n=6, p25 3.924, mediaan 4.803, p75 5.468**, met de waarschuwing dat de mediaan tussen 4.515 en 4.803 schommelt. Omdat n klein is, is de 80–150 m²-reeks voor beide zones samen (n=21–22, mediaan 3.636–3.707) een zinvolle conservatieve toets. Het blijven vraagprijzen.
- `apartment_renovated`: n=41, p25 3.457, mediaan 4.189, p75 5.000.
- `villa_renovated`: cijfers laten staan, met de gevoeligheid mediaan 6.757 bij n=11. El Arenal apart niet gebruiken.
- `villa_new`: laten staan, maar niet als mediaan gebruiken (n=2, prijzen op plan).
- `apartment_new`: bevestigd.
- Structureel: de ontdubbelregel moet ook dubbels herkennen bij gelijke prijs, kamers en badkamers en een gelijk energiecertificaat of perceel, ook als de m² verschillen. Anders tellen advertenties die bij meerdere makelaars met verschillende m² staan dubbel mee.

## 4. Werkwijze en grenzen

- `property_detail` op 22 advertenties: 4 villa's (reeks villa_renovated), 2 nieuwbouwvilla's, 11 appartementen (reeks apartment_renovated) en 5 nieuwbouwappartementen (goedkoopste, duurste en het enige in Puerto, plus het paar 111003829/111035010 voor de dubbelcheck). Alle 22 waren op 15-09-2026 "active".
- 4 onafhankelijke zoekopdrachten (één per reeks; townhouse overgeslagen, want er is geen reeks). Een gecombineerde zoekopdracht "Puerto y Arenal" werkt niet (§8 van het origineel). Daarom is per reeks de zone gekozen die de reeks domineert: villa's, nieuwbouwvilla's en gerenoveerde appartementen in Puerto; nieuwbouwappartementen in El Arenal.
- Ruwe toolantwoorden en rekenscripts staan in de scratchpad van deze sessie (`ver/`), niet in de projectmap.
- Geen telefoonnummers, namen van particulieren of sleutels overgenomen. Het oordeel "dubbel" steunt op de velden en teksten die de tool gaf; zonder bezichtiging of kadastrale referentie blijft het een identificatie op basis van advertenties.

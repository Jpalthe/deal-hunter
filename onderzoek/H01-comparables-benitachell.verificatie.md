# H01 — Tegenspraak op de vergelijkingsprijzen zone `benitachell`

**Gecontroleerd bestand:** `onderzoek/H01-comparables-benitachell.md` (niet aangepast).
**Rol:** tegenspreker. **Controledatum: 15-09-2026.** Bron: officiële Idealista-assistent (MCP `property_detail` + `search_properties`, es-ES, country es, maxResults 50); bewijstype 1 (toolresultaat, zelf gezien). Alle bedragen zijn **vraagprijzen in € per m² gebouwd**, geen transactieprijzen.
Gecontroleerd: alleen de vijf reeksen die de rekenaar gebruikt (villa_renovated, villa_new, apartment_renovated, apartment_new, townhouse_renovated).

## 1. Oordelentabel

| Reeks (origineel) | Oordeel | Kern | Gecorrigeerd |
|---|---|---|---|
| **villa_renovated** (n=37, p25 3.451 · mediaan 4.614 · p75 5.960) | **Bevestigd** | 3/3 details kloppen (goedkoopste + duurste); eigen zoekopdracht mediaan 4.373 (−5,2 %); rekenkunde exact. Eén gemist object volgens de eigen definitie (111406940, bouwjaar 2023). | Gevoeligheid met 111406940: n=38 · 3.459 / **4.628** / 5.853 (+0,3 %) — geen correctie nodig |
| **villa_new** (n=17, 3.312 · 4.577 · 4.843) | **Bevestigd, met kanttekening** | 3/3 details kloppen; eigen zoekopdracht (filter obra nueva) mediaan 4.273 (−6,6 %, maar n=3); rekenkunde exact. Twee van de 17 zijn *chalet pareado*, geen vrijstaande villa. | Gevoeligheid zonder pareados: n=15 · 4.192 / **4.729** / 4.972 |
| **apartment_renovated** (n=9, 2.907 · 3.318 · 3.794) | **Bevestigd, met kanttekening** | 3/3 details kloppen; eigen zoekopdracht mediaan 3.589 (+8,2 %); rekenkunde exact. Claims bij 111284282 en 112441505 zijn dun. | Gevoeligheid zonder 112441505: n=8 · mediaan 3.453 |
| **apartment_new** (n=10, 2.805 · 3.847 · 5.543) | **Weerlegd** | Eigen zoekopdracht (filter obra nueva) geeft mediaan **5.648 (+46,8 %)**. Twee van de 10 zijn geen prijs van één woning: ze combineren de "vanaf"-prijs van de promotie (473.000) met de m² van een groot model. | **n=8 · p25 3.101 · mediaan 4.905 · p75 5.660** (blijft fragiel, zie §5) |
| **townhouse_renovated** — casco + adosados (n=5, 2.153 · 2.714 · 2.889) | **Bevestigd** | 3/3 details kloppen; eigen zoekopdracht (chalets adosados, 18 van 18 ontvangen) levert na ontdubbeling exact dezelfde 5 objecten op, mediaan 2.714 (0 %). | — |
| townhouse_renovated — alleen casco Poble Nou (n=2, mediaan 2.003) | Rekensom klopt | **Te klein voor een betrouwbare mediaan** (n=2). | niet als eigen cijfer gebruiken |

**Rekenkunde.** Alle 11 rijen van de conclusietabel (incl. deelreeksen) zijn nagerekend op de voorbeeldlijsten (prijs ÷ m², lineaire interpolatie voor p25/p75): elk cijfer komt exact overeen.

## 2. Controle 1 — `property_detail`

| Reeks | Code | Tool: prijs / m² / €/m² | Staat volgens tool en tekst | Oordeel |
|---|---|---|---|---|
| villa_renovated | 106265412 (goedkoopste) | 590.000 / 500 / 1.180 | "villa recién reformada"; *buen estado*; 360 m² nuttig, 3 woonlagen; prijs verlaagd van 690.000 | klopt; terecht als uitschieter gemarkeerd |
| villa_renovated | 111992299 (duurste) | 4.516.000 / 502 / 8.996 | "obra maestra del lujo moderno"; geen bouwjaar; *buen estado* | klopt; modern alleen volgens tekst — [claim agent] terecht |
| villa_renovated | 110704352 | 1.490.000 / 250 / 5.960 | "Construido en 2020"; *buen estado* | klopt (origineel had hier geen detail; nu bevestigd) |
| villa_new | 112509895 (goedkoopste) | 1.300.000 / 459 / 2.832 | tekst "villa en construcción"; tool-status "Segunda mano/para reformar" en "Construido en 2026" | nieuwbouw volgens tekst; tool-status is fout (origineel meldt dit ook). Let op: 458 m² nuttig op 459 gebouwd is onwaarschijnlijk |
| villa_new | 112516125 (duurste) | 1.650.000 / 207 / 7.971 | "Promoción de obra nueva", `notFinished` | klopt |
| villa_new | 111130564 | 915.000 / 290 / 3.155 | obra nueva, `notFinished`; **Chalet pareado** | klopt, maar geen vrijstaande villa |
| apartment_renovated | 111284282 (goedkoopste) | 190.000 / 90 / 2.111 | "El interior ha sido renovado"; bouwjaar 2010; energielabel G | klopt; claim dun — [claim agent] terecht |
| apartment_renovated | 110844494 (duurste) | 475.000 / 109 / 4.358 | "bellamente reformado", "recientemente renovada"; bouwjaar 2005 | klopt |
| apartment_renovated | 112441505 | 265.000 / 86 / 3.081 | "renovado y actualizado"; concreet: keuken 2020, badkamer 2021; gebouw ±1982 | prijs klopt; renovatie is feitelijk keuken + bad — volgens de eigen villaregel ("alleen keuken/bad") zou dit afvallen |
| apartment_new | 111087729 (goedkoopste) | 473.000 / 190 / 2.489 | "nueva construcción", oplevering 2026; *buen estado*; 3 slk; "según el modelo puede incluir jardín privado o solárium" | **geen prijs van één woning**: 473.000 is de vanafprijs van de promotie (zie 112440425), terwijl de 3-slaapkamerunits van de promotor 593.000–687.000 kosten |
| apartment_new | 112440425 (duurste) | 687.000 / 105 / 6.543 | "obra nueva terminada", promotie Montecala Gardens (`finished`), promotieprijs 473.000 | klopt |
| apartment_new | 110881337 | 473.000 / 176 / 2.688 | "Duplex de nueva construcción … varios modelos entre los que elegir"; tool-status "para reformar" | **geen prijs van één woning**: algemene modeladvertentie tegen dezelfde vanafprijs |
| townhouse_renovated | 111508676 (goedkoopste) | 365.000 / 197 / 1.853 | "completamente reformada", "rehabilitación integral" incl. dak; tekst: bouw/reforma 2019 | klopt (bouwjaar 1930 staat niet in deze advertentie) |
| townhouse_renovated | 109365710 (duurste) | 350.000 / 96 / 3.646 | "recientemente reformada en 2025"; bouwjaar 1999; adosado | klopt |
| townhouse_renovated | 110955242 | 190.000 / 70 / 2.714 | "reformado en 2016"; bouwjaar 2006 | klopt; renovatie is 10 jaar oud |

Geen van de gecontroleerde objecten is feitelijk "para reformar"; waar de tool dat zegt (112509895, 110881337) spreekt de advertentietekst het tegen.

## 3. Controle 2 — onafhankelijke zoekopdracht per reeks

| Reeks | Query (tool koos) | Totaal / ontvangen | Na eigen selectie + ontdubbeling | Mediaan | Afwijking |
|---|---|---|---|---|---|
| villa_renovated | "villa totalmente reformada o de construcción reciente en Benitachell" (Benitachell; Villas; Obra nueva + Usada/buen estado) | 83 / 50 | n=14 (alleen tekstclaim in het resultaat) | 4.373 | −5,2 % ✔ |
| villa_new | "villa de obra nueva a estrenar o en construcción en Benitachell" (Villas; Obra nueva) | 3 / 3 | n=3: 112516125, 111704123, 111273264 | 4.273 | −6,6 % ✔ (n=3) |
| apartment_renovated | "piso o apartamento reformado en Benitachell" (Pisos; Usada/buen estado) | 128 / 50 | n=7 | 3.589 | +8,2 % ✔ |
| apartment_new | "piso o apartamento de obra nueva en Benitachell" (Pisos; Obra nueva) | 5 / 5 | n=5, allemaal SJW-units Montecala Gardens | 5.648 | **+46,8 % ✘** |
| townhouse_renovated | "chalet adosado reformado en Benitachell" (Chalets adosados; Usada/buen estado) | 18 / 18 | n=5 (casa de pueblo 1× ondanks 3 vermeldingen) | 2.714 | 0 % ✔ |

Een eerste townhouse-query ("casa adosada o casa de pueblo reformada en Benitachell") gaf alleen villa's terug en is niet gebruikt.

**Gemist object villa_renovated.** 111406940 — `property_detail`: 1.595.000 / 323 m² = 4.938 €/m², "Construido en 2023", *Segunda mano/buen estado*, Distrito Centro, rustiek perceel van ±10 ha (diseminado). Past in de eigen definitie (bouwjaar ≥ 2014, geen nieuwbouwverkoop) maar staat nergens in het origineel. Effect op de mediaan: +14 €/m². Door het perceel is het object nauwelijks vergelijkbaar met urbanisatievilla's.

## 4. Controle 3 — ontdubbeling

- **Consistent waar ik het zag.** In de zoekresultaten stonden de door het origineel genoemde doublures inderdaad met dezelfde prijs/m²: 108987280 = 110510628, 112178451 = 109194891, 109133568 = 110651943, 100133536 = 110480516, 111103870 = 111522880, 111971400 = 111992299 (1.100 m²), 108977506 = 110510885, 108545934 = 110511033, 109778069 = 110955242; de casa de pueblo staat als 110907230 / 111947534 / 111601082 (192–200 m², 365.000). Geen van deze is dubbel geteld.
- **Niet te bewijzen:** 111586472 (249.000 / 63 m², "Adelfas 1") als doublure van 110959894 ("Cordell Hull 4", 239.000). Ander adres en andere prijs. Telt hij apart mee, dan wordt apartment_renovated n=10, mediaan 3.453 (+4 %) — niet materieel.
- **apartment_new:** de drie advertenties met prijs 473.000 zijn geen drie objecten. 112440488 is een echte SJW-unit; 111087729 en 110881337 zijn modeladvertenties tegen de vanafprijs (§2). Dit is de fout die de mediaan omlaag trekt.

## 5. Toelichting weerlegging apartment_new

1. De vanafprijs van promotie Montecala Gardens is volgens de tool 473.000 (promotie-ID van 112440425). 111087729 zegt 3 slaapkamers en 190 m² bij 473.000 en "según el modelo …". De 3-slaapkamerunits van de promotor zelf kosten 593.000–687.000 bij 105–117 m². Prijs en m² horen dus niet bij dezelfde woning, en 2.489 €/m² is een rekenartefact. 110881337 ("varios modelos entre los que elegir", 473.000 / 176 m²) is hetzelfde type advertentie.
2. Zonder die twee: 2.720 · 3.060 · 3.114 · 4.579 · 5.231 · 5.648 · 5.699 · 6.543 → **n=8, p25 3.101, mediaan 4.905, p75 5.660**. Dat ligt −13 % onder de zoekmediaan (5.648) en +27,5 % boven het origineel.
3. **Waarom dit cijfer toch fragiel is.** (a) 5 van de 8 komen uit één prijslijst (SJW); (b) er zijn twee m²-bases: SJW geeft ongeveer de woning-m², makelaars tellen terras en gemeenschappelijke delen mee; (c) in de zoekresultaten staan nog drie Montecala Gardens-units bij makelaars zonder claim "nieuw/a estrenar" (106909209 = 111381001: 355.000 / 143; 108636953 = 112401902: 549.000 / 165; 109032691: 403.000 / 108). Het origineel nam ze terecht niet op, want er is geen nieuwbouwclaim. Blijken het toch eerste bewoning, dan zakt de mediaan naar ±3.730. **Advies:** gebruik voor apartment_new geen enkele mediaan zonder de m²-basis te kiezen; n=5 SJW-units (mediaan 5.648, woning-m²) is de schoonste basis, maar het blijft één promotie.

## 6. Kanttekeningen die geen weerlegging zijn

- **villa_new** mengt vrijstaande villa's met twee geschakelde units (111130564, 111130611) en met twee projecten op papier (110880346 "start bouw juni 2026", 110908251 "alleen render"). Zonder de pareados wordt de mediaan 4.729 (+3,3 %).
- **villa_renovated** blijft een mengreeks (gerenoveerd tegenover modern ≥ 2014). De spreiding 1.180–8.996 hangt vooral aan de m²-opgave; 106265412 (500 m² over drie woonlagen) en 111992299 (geen bouwjaar) zijn de randen.
- **townhouse_renovated (n=5)** combineert twee markten: casco 1.853–2.153 en urbanisatie-adosados 2.714–3.646. De mediaan 2.714 is één appartementachtig huisje van 70 m² in Cumbre del Sol. n=5 ligt op de ondergrens; de casco-rij (n=2) is **te klein voor een betrouwbare mediaan**.
- **apartment_renovated:** de goedkoopste (111284282, "interior renovado", label G) en 112441505 (keuken + bad) hebben dunne renovatieclaims; zonder 112441505 wordt de mediaan 3.453 (+4 %).
- Alle cijfers zijn vraagprijzen op één peildatum; prijsverlagingen (106265412 −14 %, 110844494 −4 %, 111704123 −18 %) laten zien dat vraagprijzen hier boven de koopsom liggen. Hoeveel, is uit deze bron niet af te leiden.

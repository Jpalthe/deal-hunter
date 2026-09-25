# 110566607 — Tegenspraak op ons eigen basisscenario

Villa te renoveren, Carretera de la Granadella / La Guardia, Jávea · vraagprijs € 640.000
Opgesteld 18-09-2026 · opdracht: probeer ons eigen rekenmodel onderuit te halen.

**Bronnen.** Officiële Idealista-assistent (`property_detail` en `search_properties`,
18-09-2026), ons eigen dossier `rapporten/dossiers/110566607.html` (18-09-2026), en onze eigen
onderzoeksbestanden `onderzoek/H01-comparables-granadella_balcon.md` (15-09-2026),
`onderzoek/N05-bouwkosten-keuken-badkamer.md` (18-09-2026), `onderzoek/N01-bouwregels-xabia.md`
(18-09-2026), `kader/comparables.json` en `kader/parameters.json`. Niet gescrapet, niet ingelogd.

---

## Oordeel vooraf

**Valt af op de vraagprijs.** Niet omdat het pand slecht is, maar omdat de opbrengstkant van ons
model op dit object aantoonbaar te hoog staat. Gecorrigeerd zakt de maximale koopprijs van
€ 955.000 naar grofweg € 520.000 — en dat is nog vóór de renovatiekosten zijn rechtgezet.
€ 640.000 vragen is dan al te veel, laat staan dat er "€ 315.000 speling" zit.

Ons eigen dossier zegt dit trouwens zelf al, zonder het te zien: in het **voorzichtige** scenario
staat de maximale koopprijs op **€ 612.000**. Dat is lager dan de vraagprijs van € 640.000. De
kopregel "de deal draagt € 955.000, dus de vraagprijs past met € 315.000 speling" en die € 612.000
staan op dezelfde bladzijde en spreken elkaar tegen.

---

## 1. Welke vierkante meters zitten er in de opgave

De advertentie geeft **378 m² construidos** (kenmerkenblok: "378 m² construidos", "Parcela de
2260 m²", "3 habitaciones", "3 baños", "Construido en 1970"). Het gegevensveld `areas.usableArea`
geeft hetzelfde getal 378 terug — dat kan niet allebei: *construida* is altijd groter dan *útil*.
Er is geen losse útil-opgave, geen uitsplitsing, en nergens het woord *incluye*.

Wat er wél staat, en dit is het hele punt:

> "cuenta con vivienda principal y **varias construcciones auxiliares**"

Hoofdwoning **plus meerdere bijgebouwen**. Aantal, aard en oppervlakte: ONBEKEND. Verder noemt de
tekst een "zona de terraza"; negen foto's zijn als *terraza* gelabeld terwijl het kenmerkveld
`hasTerrace` op `false` staat — die vlaggen zijn hier dus niet ingevuld, niet leeg omdat er niets is.
Kelder en garage worden niet genoemd, maar `hasParking` en `hasBoxRoom` staan om dezelfde reden op
`false` en bewijzen niets.

**Conclusie: 378 m² is bebouwd oppervlak van het hele perceel, inclusief bijgebouwen.** Het is geen
woonoppervlak van één woning. Ons model zet daar 363 m² verkoopbaar woonoppervlak van (378 × 0,96)
en dat is de eerste helft van de fout — zie punt 4, want de tweede helft maakt het erger.

Twee losse signalen die dezelfde kant op wijzen:
- 378 m² met **3 slaapkamers en 3 badkamers**. Dat is 126 m² per slaapkamer. Een woning van 363 m²
  woonoppervlak met drie slaapkamers bestaat niet; die meters zitten ergens anders.
- Ons model rekent de keuken-en-badkamerpost af op **4 badkamers** terwijl de advertentie er 3
  noemt. Klein bedrag, maar het laat zien dat de indeling in het model niet uit de advertentie komt.

---

## 2. Planklasse en vergunning — hier zit het grootste risico

**De advertentie zegt hier niets over.** Geen *suelo urbano*, geen *urbanizable*, geen *rústico*,
geen kadastrale referentie, geen *licencia de obra*, geen *aval bancario*. De enige zin die erop
lijkt — "una tranquila zona residencial consolidada" — is verkooptaal, geen planologische
categorie. Status: **ONBEKEND**, en daarmee niet uitgesloten én niet vrijgegeven.

Maar ons eigen dossier heeft op 18-09-2026 wél het kadaster bevraagd, en wat daar uitkwam is
alarmerend:

| Wat het kadaster zegt (dossier 18-09-2026) | Wat de advertentie zegt |
|---|---|
| Perceel 7919001BC5971N, **976 m²** | **2.260 m²** |
| **Bebouwd: 0 m²** | **378 m² gebouwd** |
| Gebruik: "Obras de urbanización y jardinería, **suelos sin edificar**" (onbebouwde grond) | villa met zwembad, tuin, bijgebouwen |
| Adres: CR GUARDIA LA 799(C) | Carretera de la Granadella |

Twee mogelijkheden, allebei slecht voor het scenario:

1. **Het gekoppelde perceel is niet het verkochte perceel.** 976 tegenover 2.260 m² is geen
   afrondingsverschil. Dan is álles wat ons model over dit perceel zegt — bouwvolume, maximale
   bebouwing, de hele "wat hier mag"-tabel — op de verkeerde grond gebaseerd.
2. **Het perceel klopt en er staat 378 m² niet-ingeschreven bouwwerk op.** Dat is de klassieke
   *obra sin licencia* uit 1970, precies passend bij "varias construcciones auxiliares" die er in
   de loop van decennia zijn bijgezet.

Waarom mogelijkheid 2 het plan doodt en niet alleen duurder maakt: uit `N01-bouwregels-xabia.md`
§4 en de zonetabel:

> Wijk **Granadella / Balcón al Mar**, zone E, parcela mínima 1.000 m², edificabilidad 0,20.
> "La Granadella werd in 1991 **SNUEP**: geen nieuwbouw." (resolución 08-03-1991)
> SNUEP, Parque Natural, PATIVEL → **edificabilidad 0**.

Valt dit perceel binnen dat SNUEP-perimeter, dan is de bouwcoëfficiënt nul. Een integrale renovatie
is in Xàbia een *licencia de obra mayor*, en op dat moment kijkt de gemeente naar het hele perceel.
Niet-vergund volume gaat er dan af, het wordt niet mee-gerenoveerd. Het scenario dat de verkooptekst
belooft ("crear una villa contemporánea de alto valor") is dan juist het scenario dat niet mag.

En let op de rekensom met het kleinere perceel: 0,20 × 976 m² = **195 m² maximaal bebouwd**,
tegenover 378 m² opgegeven. Met 2.260 m² is het 452 m² en past het nét. Het verschil tussen die
twee percelen is het verschil tussen "mag" en "mag niet". Ook is 976 m² **onder de parcela mínima
van 1.000 m²** voor deze zone.

Dit is allemaal [te verifiëren] bij de gemeente — maar het is precies het punt waarop je niet mag
gokken.

---

## 3. Wat er werkelijk moet gebeuren, en of € 1.000/m² genoeg is

Wat de advertentie zelf zegt: "villa **a renovar íntegramente**", "necesita una **actualización
completa**", bouwjaar **1970**, energielabel **G** met **382,6 kWh/m² per jaar**. Dat laatste is
een huis zonder isolatie, zonder dubbel glas, met installaties uit een andere eeuw.

Ons eigen onderzoek `N05` §2.2 beantwoordt de vraag letterlijk. Teruggerekend is € 1.000/m²
aanneemsom € 840/m² PEM, en dat is 75 % van de IVE-norm bij middenafwerking:

> "In gewone taal: 1.000 €/m² is een **grondige maar niet totale** renovatie met middenkwaliteit
> afwerking. Het is **niet genoeg voor casco strippen, nieuwe fundering onder een uitbouw, nieuw
> dak, nieuwe gevel én topafwerking**. Dat wordt 1.400 – 1.800 €/m²."

De tabel in datzelfde bestand:

| Ingreep | Aanneemsom excl. btw |
|---|---|
| Grondige renovatie, casco blijft, middenafwerking | 950 – 1.250, **1.100 €/m²** |
| Volledige strip-en-herbouw binnen, hoge afwerking | 1.400 – 1.800, **1.550 €/m²** |

**Nee, € 1.000/m² is niet genoeg.** Twee redenen:

1. Het pand vraagt om de onderste regel van die tabel, niet de bovenste. "Íntegramente" plus label
   G plus 1970 plus een herindeling van 3 naar meer slaapkamers is strip-en-herbouw.
2. **Het model is intern tegenstrijdig.** Het budgetteert een middenkwaliteits-renovatie
   (€ 1.000/m²) en verkoopt vervolgens tegen € 6.081/m², een prijs die in deze wijk alleen wordt
   gevraagd voor topafwerking: vloerverwarming, domotica, infinity pool, lift. Je kunt niet
   tegelijk het goedkope budget en de dure verkoopprijs aanhouden.

`kader/parameters.json` waarschuwt hier zelf al voor: *"N05 geeft voor renovatie 1.100 €/m² als
richtgetal… Jouw kader staat op 1.000. Bevestig of die tarieven blijven staan; het verschil werkt
direct door in elke maximale koopprijs."* Die bevestiging is er niet.

Op 363 m² scheelt 1.000 → 1.550 €/m² bijna **€ 200.000 aan bouwsom**, en met honoraria, ICIO,
reserve en niet-terugvorderbare btw erbovenop ongeveer **€ 290.000 aan totale kosten**.

Daar komt bij, niet gekwantificeerd maar wel reëel voor 1970 in deze regio: uralita (asbestcement)
in dak- en leidingwerk was toen standaard. Aandachtspunt, geen vaststelling over dit pand.

---

## 4. De verkoopprijs per m² — hier valt het plan om

### Wat het model doet

Het model pakt € 6.081/m². Dat is uit `kader/comparables.json` de **mediaan van twee wijken samen**
(Portichol–Balcón al Mar én Granadella–Costa Nova). Drie dingen kloppen daar niet aan:

**a. Verkeerde wijk.** Dit object ligt in **La Granadella – Costa Nova**. Diezelfde
`comparables.json` geeft de cijfers per wijk: Balcón al Mar mediaan **6.306** (n = 25), Granadella
mediaan **5.777** (n = 9). Het model gebruikt de gemengde mediaan, die omhoog wordt getrokken door
de duurdere buurwijk.

**b. De n klopt niet.** Het veld zegt `"n": 43`, terwijl de toelichting in hetzelfde veld zegt
"25 Portichol–Balcón al Mar, 9 La Granadella–Costa Nova" = 34. Ook het rapport `H01` komt op 34.
Het dossier meldt vervolgens aan Jan "43 vergelijkbare woningen". Dat getal is nergens onderbouwd.

**c. En dit is de kern: verkeerde maat.** De mediaan van 6.081 komt uit een reeks die wordt
gedomineerd door **kleine** gerenoveerde villa's, gemeten als het huis alleen:

| Object uit de reeks | m² | €/m² |
|---|---|---|
| Calle de la Xicoria 4 (het object dat exact op 6.081 staat) | 222 | 6.081 |
| Villa Marina, Costa Nova | 206 | 5.777 |
| Villa Granados (180 m² binnen, 260 incl. terrassen) | 260 | 5.750 |
| Isaac Albéniz 9 | 260 | 7.269 |
| Villa Silenzia | 211 | 9.384 |

Ons object heeft **378 m² construidos inclusief bijgebouwen**. Het model vermenigvuldigt dus een
**huis-alleen-prijs per m²** met een **oppervlakte die het hele perceel bebouwd telt**. Dat is twee
keer dezelfde fout in dezelfde richting: te veel meters, en een te hoge prijs per meter.

`H01` zegt dit zelf, in zoveel woorden: *"Vergelijk nieuwbouw-€/m² dus nooit één-op-één met
renovatie-€/m²"* en *"m² gebouwd is niet uniform. Nieuwbouw telt terras, zwembadplateau en kelder
mee; tweedehands vaak alleen het huis."* Ons object is het geval waarin je wél alles meetelt.

### Drie voorbeelden, vandaag opgehaald

Ik heb met `search_properties` gezocht naar wat er in **precies deze wijk** (La Granadella – Costa
Nova) wordt gevraagd voor **gerenoveerde of nieuwe** woningen van **320 tot 450 m²** — de maatklasse
van dit object na renovatie. De officiële assistent geeft **vier** objecten, `total: 4`:

| # | Object | m² | Vraagprijs | €/m² | Wat het is |
|---|---|---|---|---|---|
| 1 | **Costa Nova Pla 107** (108771720) | 350 | € 1.290.000 | **3.686** | Nieuwbouw, "completamente terminada". Tekst: 200 m² woning op 1.170 m² perceel — de rest is parking en terras |
| 2 | **Villa Bellagio**, Calle de la Guatla 1 (108642958) | 345 | € 1.395.000 | **4.043** | Nieuwbouw, 1.000 m² perceel, 3 slk / 3 bad |
| 3 | **Villa ONYX**, Calle del Escabusso 35 (108643000) | 320 | € 1.520.000 | **4.750** | Nieuwbouw, zeezicht, infinity pool, home cinema, sauna, 950 m² perceel |
| 4 | Casa Bellavista, Urb. Atalayas 210, Cap Martí (110942219) | 429 | € 3.100.000 | **7.226** | "Totalmente renovada", zeezicht, lift, souterrain met garage, 5 slk / 5 bad |

Bron: Idealista-assistent, `search_properties`, 18-09-2026,
<https://www.idealista.com/nl/venta-viviendas/javeaxabia/la-granadella-costa-nova/con-metros-cuadrados-mas-de_320,metros-cuadrados-menos-de_450,villa,obra-nueva,para-reformar/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_list>

**Mediaan van deze vier: € 4.397/m².** Niet 6.081.

En nummer 4 is geen tegenvoorbeeld, die bewijst het punt. Die haalt 7.226 €/m² met zeezicht, een
lift, een souterraingarage en **5 slaapkamers en 5 badkamers**. Ons object heeft **3 en 3**, en de
advertentie noemt **geen enkele keer zeezicht** — opvallend in een wijk waar iedere makelaar
*vistas al mar* in de eerste zin zet. Drie slaapkamers in 363 m² is bovendien een zwak product in
dit segment; de villa's die hier boven de 2 miljoen worden gevraagd hebben er vijf of zes.

Zelfde beeld in de gerenoveerde reeks van `H01` bij deze maat: Calle del Morell 318 m² →
**3.428 €/m²**, Felix Mendelssohn 12 380 m² → **3.750 €/m²**, Rimontgó 300 m² → **4.500 €/m²**.

---

## 5. Wat er van het basisscenario overblijft

Ik heb het rekenmodel uit het dossier nagebouwd. Het reproduceert de gepubliceerde opbrengst van
€ 2.207.403 exact en de totale kosten binnen 1,2 %, dus de vergelijking is zuiver.

| Scenario | Opbrengst | Kosten | Resultaat | Marge |
|---|---|---|---|---|
| **Dossier basis** (1.000 €/m² bouw, 6.081 €/m² verkoop) | € 2.207.403 | € 1.403.000 | **+ € 804.000** | 36 % |
| Alleen renovatie recht (**1.550 €/m²**, N05) | € 2.207.403 | € 1.694.000 | + € 513.000 | 23 % |
| Alleen verkoopprijs recht (**4.397 €/m²**, wijk + maat) | € 1.596.111 | € 1.388.000 | + € 208.000 | 13 % |
| **Beide recht** | € 1.596.111 | € 1.679.000 | **− € 83.000** | −5 % |
| Beide recht, maar verkoop op de béste van de drie (4.750) | € 1.724.250 | € 1.682.000 | + € 42.000 | 2 % |

Met de eigen gevoeligheid van het dossier (4.746 €/m² → max € 612.000; 6.081 → € 955.000, dus
€ 257 maximale koopprijs per euro verkoopprijs per m²) komt de maximale koopprijs bij 4.397 €/m²
uit op ongeveer **€ 520.000** — met de renovatie nog op 1.000 €/m². Corrigeer die ook, en er gaat
nog eens circa € 290.000 af.

**€ 640.000 vragen past daar niet in.** De "€ 315.000 speling" is er niet.

---

## 6. Wat het plan het snelst onderuit haalt

**De verkoopprijs per m².** Dat is het punt dat je vandaag kunt controleren, zonder de verkoper,
zonder de gemeente, zonder een bouwkundige. In de wijk waar dit object staat, in de maatklasse
waarin het na renovatie valt, bestaan vier vergelijkbare objecten en drie ervan worden aangeboden
tussen **3.686 en 4.750 €/m²**. Ons model rekent met **6.081**. Dat is 30 tot 60 procent te hoog, en
het werkt één-op-één door in de maximale koopprijs. Alleen die correctie brengt de maximale
koopprijs al onder de vraagprijs.

Het **grootste** risico is een ander: het kadaster kent op het gekoppelde perceel **0 m² bebouwing**
en noemt de grond onbebouwd, terwijl de advertentie 378 m² opgeeft — in een wijk die in 1991 deels
SNUEP werd, waar de bouwcoëfficiënt nul is. Als dat niet-ingeschreven volume niet vergunbaar is, is
er geen renovatiescenario, hoe de rekensom er verder ook uitziet.

---

## 7. Correcties die in het model moeten

1. **Verkoopprijs**: niet de gemengde tweewijkenmediaan van 6.081, maar de wijk- én maatklasse. Voor
   dit object 4.397 €/m² (mediaan van de vier objecten van 320–450 m² in La Granadella – Costa Nova,
   18-09-2026). Structureel: koppel de comparabelenreeks aan de maatklasse van het object, want in
   deze wijk daalt de €/m² sterk met de omvang.
2. **Renovatietarief**: 1.550 €/m² (N05, "volledige strip-en-herbouw binnen, hoge afwerking") in
   plaats van 1.000 €/m², zodra de tekst "renovar íntegramente" zegt en het label G is. Een
   middenbudget en een topverkoopprijs mogen niet in hetzelfde scenario staan.
3. **Oppervlakte**: `m2_woon` = 363 is niet houdbaar zolang "varias construcciones auxiliares" niet
   is uitgesplitst. Zet het label op ONBEKEND in plaats van "geschat", of reken met de
   C-variant (234 m²) tot het tegendeel blijkt.
4. **Perceel**: het dossier toont "Perceel —" terwijl `property_detail` gewoon 2.260 m² geeft. Dat
   veld wordt niet ingelezen. En 2.260 tegenover 976 m² uit het kadaster moet worden opgelost
   vóór er iets over bouwvolume wordt gezegd.
5. **`comparables.json`**: `"n": 43` klopt niet met de eigen toelichting (25 + 9 = 34). Het dossier
   vertelt Jan "43 vergelijkbare woningen". Rechtzetten.
6. **Badkamers**: het model rekent 4, de advertentie zegt 3.
7. **Interne tegenspraak signaleren**: als het voorzichtige scenario een maximale koopprijs onder de
   vraagprijs geeft, mag de kop niet "Kopen" zijn.

---

## 8. Wat wél blijft staan

Eerlijk is eerlijk — dit is niet allemaal fout:

- Het object is echt en de advertentie is actief (Lucas Fox Jávea, ref. JAV64216).
- De **koopkant** van het model klopt: 9 % ITP over € 640.000 = € 57.600, notaris en register 0,4 %,
  due diligence € 7.500. Dat is netjes onderbouwd in `parameters.json` met wetsverwijzing.
- De vraagprijs van **1.693 €/m²** is voor deze wijk laag, en dat is terecht opgemerkt. Er zit
  ruimte tussen huidige staat en eindproduct; de vraag is alleen hoeveel, en het antwoord is minder
  dan het model zegt.
- **Onderhandelingspositie**: "Anuncio actualizado hace más de 3 meses", geen prijsdaling gemeld in
  drie onafhankelijke zoeksnapshots. Het staat er een tijd, tegen een prijs die nooit is bijgesteld.
  Dat is een koperssignaal.
- Het dossier signaleert het kadasterverschil zelf al in het onderhandelplan. Goed gezien — het is
  alleen niet doorgerekend in het oordeel.

---

## ⏸️ ACTIE VOOR JAN

**Eerste vraag aan Lucas Fox, vóór alles:** vraag om de **nota simple en de kadastrale referentie**,
en laat uitleggen hoe 378 m² gebouwd zich verhoudt tot een kadaster dat op dit perceel niets kent —
en welk deel van die 378 m² de hoofdwoning is en welk deel de bijgebouwen.

Daarna pas, en alleen als dat antwoord goed is:
- *Informe urbanístico* of *cédula urbanística* bij de gemeente Xàbia op de kadastrale referentie:
  planklasse, en of het perceel binnen het SNUEP-perimeter van La Granadella valt.
- Vergunninghistorie van de bijgebouwen.
- Bouwkundige opname met asbestcontrole (1970).

**Niet bieden op € 640.000.** Als het pand na die antwoorden schoon blijkt, ligt het gesprek rond
**€ 500.000 of lager**, niet rond de vraagprijs.

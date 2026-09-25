# N06 — Oppervlaktebegrippen in Spaanse advertenties, en wat dat met onze prijs per m² doet

Onderzoek voor TREE Deal Hunter · opgesteld 18-09-2026 · werkgebied Jávea, Benitachell, Moraira en omgeving

---

## Wat dit oplost

Het rekenmodel vergelijkt vraagprijzen per m². Die m² komt uit één veld in een feed of op
een portaal, en dat veld heeft geen vaste betekenis. Soms is het de woonruimte, soms de
woonruimte plus muren, soms de woonruimte plus garage, kelder, overdekt terras en zwembad.
Wij hebben dat gemeten in ons eigen aanbod en in het kadaster. De uitkomst: het verschil
tussen de smalste en de ruimste uitleg loopt in ons materiaal op tot een factor 2,4 bij
hetzelfde huis.

Drie conclusies vooraf.

**Eén.** Er is geen enkele omrekenfactor die altijd klopt. Er zijn drie herkenbare regimes,
en het werk zit in het bepalen welk regime een advertentie volgt — niet in het kiezen van een
getal. Voorstel voor de indeling en de factoren staat in §6.

**Twee.** De fout doet pas pijn als je twee maten door elkaar gebruikt. Zolang de
vergelijkingsobjecten én het object dezelfde maat hanteren, valt de fout grotendeels tegen
elkaar weg. In ons model gebeurt dat níét: de €/m² komt uit advertentie-oppervlakten en
wordt vermenigvuldigd met `result_m2`, het aantal m² dat wij werkelijk bouwen. Dat is de
concrete plek waar wij percelen te laag waarderen. Zie §7.

**Drie.** Het kadaster is een bruikbare tweede mening, maar geen meetlat. Van 120
opgevraagde objecten kwamen er 48 als schoon villaperceel uit de bus, en daarvan lag maar
4 van de 48 binnen 15 % van de advertentieopgave. Het gat is een sein om te kijken, geen
correctiefactor. Zie §5.

---

## 1. De begrippen

### 1.1 Superficie útil — het nuttige oppervlak

De maatgevende definitie staat in **Orden ECO/805/2003, artikel 4**, de taxatienorm waar
banken en taxateurs in Spanje op werken. Letterlijk:

> "Es la superficie del suelo delimitado por el perímetro definido por la cara interior de
> los cerramientos externos de un edificio o de un elemento de un edificio, incluyendo la
> mitad de la superficie del suelo de sus espacios exteriores de uso privativo cubiertos
> (tales como terrazas, balcones y tendederos, porches, muelles de carga, voladizos, etc.),
> medida sobre la proyección horizontal de su cubierta."

Bron: <https://www.boe.es/buscar/act.php?id=BOE-A-2003-7253> — bewijstype 2, gecontroleerd 18-09-2026.

In gewone taal: de vloer waar je op kunt lopen, gemeten aan de binnenkant van de
buitenmuren. Muren, pilaren en leidingkokers boven 100 cm² tellen niet mee, en ruimte lager
dan 1,50 m ook niet. Overdekte privé-buitenruimte telt voor de **helft** mee — terras,
balkon, wasruimte, porche. Onoverdekte buitenruimte telt niet mee.

Let op dat laatste: ook *útil* is dus niet zuiver "binnen". Een villa met een royaal
overdekt terras krijgt daar de helft van mee in het nuttige oppervlak.

### 1.2 Superficie construida sin partes comunes — het bebouwde oppervlak

Dezelfde Orden, hetzelfde artikel 4:

> "Superficie útil, sin excluir la superficie ocupada por los elementos interiores
> mencionados en dicha definición e incluyendo los cerramientos exteriores al 100 por 100 o
> al 50 por 100, según se trate, respectivamente, de cerramientos de fachada o medianeros, o
> de cerramientos compartidos con otros elementos del mismo edificio."

Dus: útil plus de binnenmuren en pilaren, plus de gevel voor 100 % en de muur die je met de
buren deelt voor 50 %.

### 1.3 Superficie construida con partes comunes — bebouwd inclusief gemeenschappelijk

> "Superficie construida sin partes comunes más la parte proporcional que le corresponda
> según su cuota en la superficie de los elementos comunes del edificio."

Dit is het appartementenbegrip: je eigen bebouwde oppervlak plus jouw aandeel in trappenhuis,
lift, gangen, portiek en technische ruimten, naar rato van je *cuota de participación*, het
aandeel in de vereniging van eigenaars. Bij een vrijstaande villa speelt dit niet, behalve in
gesloten urbanisaties met gedeelde voorzieningen.

Voor appartementen kan dit begrip de opgave flink optillen zonder dat er één vierkante meter
bij de koper hoort. Franke & de la Fuente (advocatenkantoor Marbella) beschrijft het net zo:
de gemeenschappelijke ruimten worden "added to the total calculation" naar rato van de cuota.
<https://www.frankedelafuente.com/calculation-of-surface-area-on-the-spanish-property-market/>
— bewijstype 6, 18-09-2026.

### 1.4 Het kadastrale bebouwde oppervlak — een vierde begrip

Het kadaster rekent met een eigen definitie, vastgelegd in **Real Decreto 1020/1993,
Norma 11, apartado 3**:

> "Se entiende como superficie construida la superficie incluida dentro de la línea exterior
> de los paramentos perimetrales de una edificación y, en su caso, de los ejes de las
> medianerías, deducida la superficie de los patios de luces.
>
> Los balcones, terrazas, porches y demás elementos análogos, que estén cubiertos se
> computarán al 50 por 100 de su superficie, salvo que estén cerrados por tres de sus cuatro
> orientaciones, en cuyo caso se computarán al 100 por 100.
>
> En uso residencial, no se computarán como superficie construida los espacios de altura
> inferior a 1,50 metros."

Bron: <https://www.boe.es/buscar/act.php?id=BOE-A-1993-19265> — bewijstype 2, 18-09-2026.

Twee dingen die hieruit volgen en die de meeste kopers niet weten:

- Een porche die aan drie van de vier zijden dicht is, telt voor **100 %** mee. Een open
  porche voor 50 %. Wie zijn terras laat dichtzetten, verdubbelt daarmee de kadastrale
  meters van die ruimte.
- Het kadaster telt bij een villa óók het **zwembad** en de **garage** als bebouwd oppervlak,
  onder eigen gebruikscodes. Dat blijkt uit onze eigen opvragingen, §5.

### 1.5 Wat de verkoper wettelijk moet geven

**Real Decreto 515/1989, artikel 4, lid 3** verplicht de verkoper om de koper te geven:

> "Descripción de la vivienda con expresión de su superficie útil, y descripción general del
> edificio"

Bron: <https://www.boe.es/buscar/act.php?id=BOE-A-1989-11181> — bewijstype 2, 18-09-2026.

Praktisch: je hebt recht op het **nuttige** oppervlak. Een makelaar die alleen een
"built area" noemt, heeft niet geleverd wat de wet vraagt. Dat is een nette opening om ernaar
te vragen zonder dat het als wantrouwen landt.

### 1.6 Samengevat

| Begrip | Wat er in zit | Waar je het tegenkomt |
|---|---|---|
| Superficie útil | Beloopbaar binnen, overdekt terras voor 50 %, geen muren | Taxatie, energiecertificaat, RD 515/1989 |
| Superficie construida sin partes comunes | Útil plus muren en gevel | Escritura, nota simple, meeste advertenties |
| Superficie construida con partes comunes | Voorgaande plus aandeel in gemeenschappelijk | Appartementen, escritura |
| Kadastrale superficie construida | Eigen definitie; terras 50 % of 100 %, plus garage, berging en zwembad als aparte posten | Catastro, IBI-aanslag |

De literatuur zet het verschil tussen útil en construida op **15 tot 25 %**. Idealista's eigen
nieuwsartikel: "se calcula que la diferencia entre la superficie útil y la construida varía
entre un 15% y un 25% aproximadamente"
(<https://www.idealista.com/news/inmobiliario/construccion/2023/02/17/804021-diferencia-entre-superficie-util-y-construida-de-un-inmueble>
— bewijstype 6, 18-09-2026). Franke & de la Fuente noemt dezelfde marge. Die 15–25 % geldt voor
een appartement of een compact huis. Bij een villa met terras, kelder en garage klopt hij niet,
zoals §4 laat zien.

---

## 2. Wat de portalen en de feeds werkelijk in het veld zetten

### 2.1 Idealista — één veld, en dat is *construida*

Getest via de officiële Idealista-assistent op 18-09-2026 (bewijstype 1, geen scraping).

Het zoekresultaat geeft één oppervlakteveld, `size`, plus `priceByArea`. Bij object
**111563779** (Cap Negre 135, Balcón al Mar, Jávea) staat in de vaste kenmerken letterlijk:

> "395 m² construidos, 293 m² útiles"

met `size: 395`, `areas.usableArea: 293`, `price: 1.850.000` en `priceByArea: 4.684`.
Reken na: 1.850.000 / 395 = 4.684. **Idealista rekent de prijs per m² dus over de
*construida*, niet over de útil.** Over de útil zou dezelfde woning op 6.314 €/m² uitkomen,
35 % hoger.
<https://www.idealista.com/inmueble/111563779/>

Belangrijke valkuil bij het veld `usableArea`. Bij twee andere Jávea-villa's gaf de API
`usableArea` gelijk aan `size`: object **112243449** (300 en 300) en object **111666124**
(320 en 320). In beide advertenties staat in de kenmerken alleen "X m² construidos", zonder
útil. Conclusie: **`usableArea` is alleen echt als hij afwijkt van `size`.** Is hij gelijk,
dan is het veld niet ingevuld en spiegelt de API de bebouwde maat terug. Wie dat veld
klakkeloos als woonoppervlak leest, krijgt systematisch de bebouwde maat binnen.

Wat Idealista adviseert aan adverteerders is niet als officiële instructie terug te vinden.
Wel schrijft hun eigen redactie dat het aan te raden is beide getallen te noemen en het terras
apart te zetten. Dat is een aanbeveling, geen veldvereiste.

### 2.2 Fotocasa — vraagt expliciet om *construida*

Fotocasa's eigen publicatie-instructie is ondubbelzinnig:

> "A continuación deberás indicar la superficie construida en metros cuadrados. Si no lo
> sabes con exactitud, puedes consultarlo en el catastro."

<https://www.fotocasa.es/fotocasa-life/alquiler/como-puedo-publicar-un-anuncio-gratis-en-fotocasa/>
— bewijstype 1, 18-09-2026.

Dat is meteen het meest verhelderende zinnetje uit dit hele onderzoek. Fotocasa stuurt de
adverteerder naar het kadaster. En het kadastrale bebouwde oppervlak bevat, zoals §1.4 en §5
laten zien, bij een villa ook de garage, de berging en het zwembad. Wie dat advies opvolgt,
zet een getal in het veld dat voor een derde uit niet-woonruimte bestaat.

### 2.3 Kyero v3 — het formaat waar onze eigen feed op draait

De importspecificatie geeft dit:

```xml
<surface_area>
  <built>200</built>
  <plot>3000</plot>
</surface_area>
```

met als hele toelichting: *"Optional numeric. Constructed and plot area in square metres.
Empty, missing tags or '0' if unknown"*.
<https://feeds.kyero.com/assets/kyero_v3_import_spec.txt> — bewijstype 1, 18-09-2026.

Dat is alles. **Er staat nergens wat er in `built` hoort te zitten.** Geen definitie, geen
verwijzing naar útil of construida, geen apart veld voor terras, kelder of garage. De
helppagina van Kyero voegt alleen toe dat `built` en `plot` sinds versie 2.12 verplicht zijn
(<https://help.kyero.com/estate-agents/xml-import-specification> — bewijstype 1).

⚠️ **Toegangsnotitie.** `feeds.kyero.com/robots.txt` geeft `User-agent: *` met `Disallow: /`.
Het specificatiebestand is één keer opgehaald vóór die controle; dat had andersom gemoeten.
Regel voor het vervolg: dit bestand met de hand openen, niet automatiseren. De inhoud
hierboven blijft geldig, de manier van ophalen niet herhalen.

Onze eigen momentopname bevestigt de armoede van het formaat. De woningfeed op poort 3100
levert per object precies deze velden:

```
baths, beds, builtArea, country, currency, date, desc, energyConsumption, energyEmissions,
features, id, images, latitude, locationDetail, longitude, newBuild, plotArea, pool,
postcode, price, priceFreq, province, ref, town, type, url
```

Eén `builtArea`, één `plotArea`, verder niets. Geen útil, geen terras, geen kelder, geen
garage-oppervlak (gemeten 18-09-2026, bewijstype 1). Wat een makelaar bedoelt met dat getal,
staat hooguit in de vrije tekst.

Kyero v4 bestaat niet; dat is in B05 al vastgesteld en hier niet opnieuw onderzocht.

### 2.4 Wat makelaars op de Costa Blanca invullen — gemeten

224 objecten uit onze eigen momentopname, 154 daarvan villa-achtig. De volledige
beschrijvingen in alle talen doorzocht op oppervlaktegetallen (18-09-2026, bewijstype 1):

| Bevinding | Aantal |
|---|---|
| Advertenties met een m²-getal in de tekst | 106 van 224 |
| Tekst noemt een terras-, porche- of solariumoppervlak | 23 |
| Tekst noemt een kelderoppervlak | 7 |
| Tekst noemt een garageoppervlak | 6 |
| Tekst noemt expliciet een útil-, woon- of habitable-oppervlak | 10 |
| `builtArea` komt letterlijk terug in de tekst | 30 |
| Tekst noemt een groter getal dan `builtArea` | 32 |

Minder dan de helft van de advertenties geeft dus überhaupt een tweede getal, en maar tien
van de 224 noemen een woonoppervlak apart. Zes concrete gevallen, die het hele spectrum laten
zien:

**Geval 1 — de opgave is de woonruimte, terras staat erbuiten.**
`4458BELL`, villa Benitachell, `builtArea` 189. Tekst: *"a total living area of 189 m² and a
generous terrace of 112 m²"*. Het terras zit er niet in. Dit is de eerlijke variant.

**Geval 2 — de opgave is de woonruimte, kelder staat erbuiten.**
Idealista 111666124, Portichol, `size` 320, prijs 1.999.000, `priceByArea` 6.247. Tekst:
*"la vivienda ofrece 320 m² en dos plantas"* én *"un amplio sótano diáfano de 160 m²"*. Die
kelder zit niet in de 320. Was hij er wel in gerekend, dan stond er 480 m² en 4.165 €/m² —
**33 % lager, bij exact hetzelfde huis en dezelfde prijs.**
<https://www.idealista.com/inmueble/111666124/>

**Geval 3 — de opgave is bebouwd, útil staat erbij.**
`4512BEN`, villa Benissa, `builtArea` 359. Tekst: *"a total built area of 359 m2 and a usable
area of 250 m2"*. Verhouding 359 / 250 = **1,436**.

**Geval 4 — de opgave telt de terrassen mee.**
`4553CAL`, villa Calpe, `builtArea` 225. Tekst: *"a total built area of 139.61 m2"*, plus een
overdekte veranda van 32,37 m² en een open terras van 52,28 m². Tel op: 139,61 + 32,37 +
52,28 = 224,26 ≈ 225. Het veld is dus binnen plus beide terrassen, inclusief het **open**
terras dat volgens geen enkele definitie meetelt. Verhouding tot de binnenruimte:
225 / 139,61 = **1,612**.

**Geval 5 — de opgave telt alles mee, tot de bestrating aan toe.**
`4554BEN`, villa Benissa, `builtArea` 532. De tekst geeft de hele opsomming:

```
Ground floor:                      122,38 m2
Upper floor:                       101,50 m2
Porches:                            33,09 m2
Pergola BBQ:                        11,30 m2
Terraces:                           93,15 m2
Swimming pool:                      39,60 m2
Exterior paving and sidewalks:     115,31 m2
Technical rooms (underground):      17,45 m2
                                  ---------
                                   533,78 m2
```

533,78 ≈ 532. Het veld is de som van alles, inclusief het zwembad en **115 m² bestrating en
stoepen**. De werkelijke woonruimte is 122,38 + 101,50 = 223,88 m². Verhouding
532 / 223,88 = **2,376**. Bij een vraagprijs die op 532 m² lijkt te slaan, is de prijs per m²
van de echte woning **138 % hoger** dan hij in het veld oogt.

**Geval 6 — de opgave telt de kelder met garage mee.**
`4480JAV`, villa Jávea, `builtArea` 337. Tekst: *"a total built-up area of 337.72 m2"* en
*"The basement comprises a 130m2 garage, a gym, a home cinema and a wine cellar"*. De kelder
zit erin, en hij is groter dan die 130 m² alleen.

---

## 3. Hoe je het herkent

### 3.1 Aan de tekst

Getest op de 224 beschrijvingen. Deze signalen werken, in volgorde van zekerheid:

**Sterk — de opgave bevat buitenruimte of bijgebouw:**

- Een opsomming per bouwdeel met losse m²-posten die optellen tot (bijna) het opgavegetal.
  Zoek naar drie of meer m²-getallen in één advertentie en tel ze op; kom je binnen 3 % van
  het veld uit, dan is de zaak rond. Dit vond geval 5.
- Een getal in de tekst dat **kleiner** is dan het veld, met woorden als *built area*,
  *superficie construida*, *bebouwde oppervlakte* eromheen. Dan is het veld dus iets ruimers.
  Dit vond geval 4.
- *incluye*, *including*, *inclusief*, *incl.* vlak voor terraza, garaje, sótano, porche of
  basement. 37 van de 224 advertenties hebben zo'n constructie.
- Het woord *total* of *en total* bij het grote getal, met daarnaast een kleiner getal voor
  de woning zelf. 37 van de 224.

**Sterk — de opgave is juist krap, er komt nog iets bij:**

- Een los genoemd terras-, kelder- of gastenverblijfoppervlak dat **niet** in het veld zit.
  Dat herken je doordat veld en genoemde getallen niet optellen. Gevallen 1 en 2.
- Woorden als *living area*, *superficie habitable*, *woonoppervlakte*, *Wohnfläche*,
  *superficie útil* bij een getal dat gelijk is aan het veld: dan is het veld de woonruimte
  en staat het terras er los van.

**Zwak, alleen als vlag:**

- Aanwezigheid van de woorden terras (177 van 224), garage (144), berging (113) of kelder
  (64) zonder getal. Dat zegt alleen dat er iets te tellen valt, niet of het geteld is.
- Een groot verschil tussen `builtArea` en het aantal slaapkamers. Vier slaapkamers bij
  500 m² opgave is een sein.

**Rekenregel die goed werkt als eerste zeef:** `builtArea` gedeeld door het aantal
slaapkamers. In ons materiaal zit een normale villa op 60 tot 100 m² per slaapkamer. Boven de
130 m² per slaapkamer zit er vrijwel altijd garage, kelder of terras in de opgave.

### 3.2 Aan de gegevens

- **Idealista:** `areas.usableArea` ≠ `size` → beide maten zijn echt, gebruik ze.
  `usableArea` = `size` → de útil is niet ingevuld, behandel de opgave als *construida*.
- **Kyero-feed:** `builtArea` zonder enige andere oppervlakte. Altijd onbekend regime. Val
  terug op de tekst.
- **Ontbrekende `plotArea` bij een villa** is een teken van slordig ingevulde velden in het
  algemeen; bij geval 5 was `plotArea` leeg terwijl de tekst 1.000 m² noemde.
- **Foto's met de tag `plan`** (plattegrond) op Idealista: daar staat de verdeling vaak op.
  Handmatig, maar het is de snelste zekerheid. Vier van de door ons bekeken objecten hadden er
  een.

### 3.3 Aan het energiecertificaat

Het energiecertificaat rekent het verbruik per **superficie útil habitable**, en dat
certificaat is bij verkoop verplicht en wordt aan het contract gehecht
(Real Decreto 390/2021, <https://www.boe.es/buscar/act.php?id=BOE-A-2021-9176> — bewijstype 2,
18-09-2026). Staat er op het certificaat een oppervlak, dan heb je daarmee een útil uit
onafhankelijke hand. Idealista toont de energieklasse wel, het onderliggende oppervlak niet;
dat moet je opvragen. ⏸️ **ACTIE VOOR JAN:** bij een serieuze kandidaat het volledige
certificaat opvragen, niet alleen de letter — daar staat de útil op.

---

## 4. Wat zijn gangbare verhoudingen

Er is geen één getal. Dit is wat wij konden meten, met de herkomst erbij.

### 4.1 Uit de advertenties zelf, waar beide getallen erin staan

| Object | Opgave | Werkelijke woonruimte | Factor | Wat zat erin |
|---|---|---|---|---|
| `4554BEN` Benissa | 532 | 223,9 | **2,376** | porches, terrassen, zwembad, bestrating |
| `3578PED` Pedreguer | 230 | 122 | **1,885** | terras 77 m², rest onverklaard |
| `4553CAL` Calpe | 225 | 139,6 | **1,612** | overdekte veranda + open terras |
| `4512BEN` Benissa | 359 | 250 (útil) | **1,436** | muren, garage, gastenverblijf |
| Idealista 111563779 | 395 | 293 (útil) | **1,348** | muren, overdekt terras |
| Idealista 111666124 | 320 | 320 | **1,000** | kelder van 160 m² stond erbuiten |
| `4458BELL` Benitachell | 189 | 189 | **1,000** | terras van 112 m² stond erbuiten |

Mediaan over deze zeven: **1,436**. Bandbreedte 1,00 tot 2,38. Dat is de hele boodschap in
één regel: de spreiding is groter dan de correctie.

*Let op de selectie.* Dit zijn de gevallen waarin de makelaar zélf twee getallen noemde. Dat
is geen willekeurige greep — juist makelaars die iets uit te leggen hebben, leggen het uit.
De gemeten mediaan is daarom eerder een boven- dan een ondergrens voor de hele markt.
Bewijstype 1 voor elk afzonderlijk geval, bewijstype 5 voor de mediaan.

### 4.2 Uit het kadaster, 48 villapercelen in het werkgebied

Opgevraagd via de officiële webdienst van de Sede Electrónica del Catastro, 18-09-2026,
bewijstype 3. 120 objecten bevraagd, 48 daarvan bleken een schoon eengezins-villaperceel
(één bien inmueble, gebruik Residencial, met woning, zonder bedrijfsbestemming, 60–1.500 m²).

Waaruit bestaat de kadastrale *superficie construida* van zo'n villa:

| Bestanddeel | Mediaan aandeel | p25 – p75 | Op hoeveel percelen |
|---|---|---|---|
| VIVIENDA — de woning zelf | **71,1 %** | 63,2 – 83,8 % | 48 van 48 |
| Garage, berging, kelder | 12,3 % | 0 – 20,8 % | 35 van 48 |
| Overig, vrijwel altijd het zwembad (`DEPORTIVO`) | 12,1 % | 8,1 – 16,8 % | 37 van 48 |
| Overdekte buitenruimte (`SOPORT. 50%`, `PORCHE 100%`, `TERR.C 100%`) | 0 % | 0 – 4,2 % | 16 van 48 |

In absolute meters, medianen: totaal 226 m², waarvan woning 158 m², garage en berging 26 m²,
zwembad 31 m², overdekt terras 22 m² waar het geregistreerd staat.

**Kadastraal totaal gedeeld door het woondeel: mediaan 1,40** (p25 1,2 · p75 1,6 · max 2,8).

Dat is het getal dat telt voor Fotocasa-advertenties en voor iedere makelaar die de opgave
uit het kadaster overneemt, precies zoals Fotocasa adviseert (§2.2). Neemt hij het kadastrale
totaal over, dan noemt hij een oppervlak dat **40 % boven de woning** ligt, met het zwembad
en de garage erin.

De codes zijn veelzeggend: `SOPORT. 50%` en `PORCHE 100%` staan er letterlijk, met het
rekenpercentage uit RD 1020/1993 in de naam. Het kadaster is dus transparant over hoe het
terras is meegeteld — je hoeft het alleen op te vragen.

### 4.3 Uit de literatuur

15 tot 25 % verschil tussen útil en construida (Idealista-redactie, Franke & de la Fuente;
bewijstype 6). Dat komt neer op een factor 1,18 tot 1,33. Onze twee harde útil-paren zitten
op 1,348 en 1,436 — **boven** die marge. Logisch: die 15–25 % is gemeten aan appartementen,
en onze villa's hebben meer gevel per m² en meer overdekt terras.

### 4.4 Antwoord op de vraag "hoeveel procent hoger, bij een villa met terras en kelder"

Eerlijke samenvatting van het bovenstaande:

- **Villa waarvan de opgave het kadastrale totaal is:** ongeveer **40 % boven de woonruimte**
  (mediaan 1,40, bandbreedte 1,2–1,6). Bewijstype 3 en 5.
- **Villa waarvan de opgave de bebouwde woning is, terras en kelder erbuiten:** ongeveer
  **20 tot 35 % boven het nuttige oppervlak** (1,35–1,44 in onze twee harde gevallen,
  1,18–1,33 volgens de literatuur). Bewijstype 1 en 6.
- **Villa waarvan de opgave alles meetelt, inclusief open terras en bestrating:** **60 tot
  140 % boven de woonruimte** (1,61 en 2,38 in onze gevallen). Bewijstype 1, twee waarnemingen,
  te weinig voor een mediaan.

Wie toch één getal wil: **in de gevallen waarin wij het konden nameten, lag de opgave mediaan
44 % boven de werkelijke woonruimte** (§4.1, n = 7). Zet daar meteen bij dat die zeven zijn
geselecteerd op het feit dat de makelaar zelf twee getallen noemde, en dat drie van de zeven
op factor 1,00 uitkwamen. Het is geen factor om toe te passen. Het is een orde van grootte
van wat er mis kan gaan.

Welk regime in ons aanbod overheerst, weten wij **niet**. De kadastervergelijking (§5.2) is
daarvoor te ruisig, en de zeven gevallen hierboven zijn niet representatief. Werkhypothese:
regime B is de norm en regime C de uitzondering, maar een dure. **[te verifiëren]**

---

## 5. Het kadaster als controle

### 5.1 Hoe het werkt, en wat het kost

Twee gratis webdiensten van de Sede Electrónica del Catastro, zonder sleutel, zonder inlog.
Beide leveren uitsluitend *datos no protegidos* — geen eigenaarsnamen, dus geen
persoonsgegevens. Getest en werkend op 18-09-2026, bewijstype 1.

**Stap 1 — van coördinaat naar kadastrale referentie**

```
https://ovc.catastro.meh.es/ovcservweb/OVCSWLocalizacionRC/OVCCoordenadas.asmx/Consulta_RCCOOR
  ?SRS=EPSG:4326&Coordenada_X=<lon>&Coordenada_Y=<lat>
```

Levert `pc1` + `pc2` (samen de referentie van 14 tekens) en een omschrijving van de ligging.
Het dashboard gebruikt hier al de variant `Consulta_RCCOOR_Distancia`, die ook de dichtstbijzijnde
percelen geeft als het punt net naast een perceel valt.

**Stap 2 — van referentie naar de opbouw van de bebouwing**

```
https://ovc.catastro.meh.es/ovcservweb/OVCSWLocalizacionRC/OVCCallejero.asmx/Consulta_DNPRC
  ?Provincia=&Municipio=&RC=<referentie van 14 tekens>
```

Geeft per object het totale bebouwde oppervlak (`debi/sfc`), het bouwjaar (`debi/ant`), het
gebruik (`debi/luso`) en — dit is de kern — onder `lcons/cons` een lijst bouwdelen met per
deel de gebruikscode (`lcd`) en het oppervlak (`dfcons/stl`).

Voorbeeld, een villa aan Balcón al Mar in Jávea (referentie `8617806BC5981N`):

```
Totaal (sfc)   239 m²   bouwjaar 1979   Residencial
  VIVIENDA      146 m²
  ALMACEN        42 m²
  APARCAMIENTO   24 m²
  DEPORTIVO      27 m²
```

Daar staat het, uitgesplitst: 146 m² woning, 42 m² berging, 24 m² garage en 27 m² zwembad.

Snelheid: houd één verzoek per seconde aan, zoals het dashboard al doet. `ovc.catastro.meh.es`
publiceert geen robots.txt; dit zijn de bedoelde webdiensten, geen scraping.

### 5.2 Wat het waard is, en wat niet

Wij hebben 123 objecten uit de feed met coördinaten door deze twee stappen gehaald. Uitkomst:

| | Aantal |
|---|---|
| Bevraagd | 120 |
| Geen kadastrale referentie op het punt | 32 |
| Referentie gevonden, maar perceel zonder bebouwing | 35 |
| Bruikbare bebouwing gevonden | 53 |
| Daarvan schoon eengezins-villaperceel | 48 |

En van die 48:

| Advertentie versus kadastraal totaal | Aantal |
|---|---|
| Binnen 15 % | 4 |
| Meer dan 15 % hoger | 33 |
| Meer dan 15 % lager | 11 |

**Slechts 4 van de 48 komen overeen.** Dat betekent niet dat 44 advertenties liegen. Er zijn
drie oorzaken door elkaar, en ze zijn niet uit elkaar te halen zonder handwerk:

1. **De speld staat verkeerd.** Portalen verschuiven de coördinaat bewust bij objecten waarvan
   het adres verborgen is. Van de vijf Idealista-objecten die wij naliepen, had er één
   `showAddress: true` — en juist bij die ene kwam het adres van de advertentie
   ("Calle Cap Negre, 135") overeen met het kadaster ("UR BALCON AL MAR D 135"). Bij de rest
   is de match onbewezen. Dit is veruit de grootste bron van ruis.
2. **Het kadaster loopt achter.** Een aanbouw, een dichtgezet terras of een uitgegraven kelder
   die nooit is aangemeld, staat er niet in. Bij dezelfde Cap Negre-villa zegt de advertentie
   bouwjaar 1989 en 395 m², het kadaster 1979 en 239 m². Dat verschil kan een niet-aangemelde
   uitbreiding zijn — en dan is het geen meetprobleem maar een **legalisatierisico** en dus
   een kostenpost in ons model.
3. **De advertentie is opgeblazen.** De gevallen 3 tot en met 6 uit §2.4.

**Conclusie: gebruik het kadaster als sein, niet als meetlat.** Het is uitstekend om te
bepalen wélke objecten handwerk verdienen, en waardeloos als automatische correctiefactor.

### 5.3 De echte meetlat: nota simple en escritura

Voor een object waar wij serieus op bieden is de volgorde:

1. **Nota simple** bij het Registro de la Propiedad. Daar staat de *superficie construida*
   zoals die juridisch is vastgelegd, plus de lasten. Kosten enkele euro's per object.
2. **Escritura** van de verkoper, met de *declaración de obra nueva* als er is aangebouwd.
3. **Kadaster** ernaast om te zien of registro en catastro elkaar tegenspreken.
4. **Energiecertificaat** voor de útil (§3.3).
5. Wijken die drie van elkaar af, dan **zelf laten inmeten** voordat je biedt. Franke &
   de la Fuente adviseert dat expliciet bij afwijkingen tussen registro en catastro.

⏸️ **ACTIE VOOR JAN:** vaststellen of wij per serieuze kandidaat standaard een nota simple
opvragen, en wie dat doet. Dat is de enige stap die de oppervlaktevraag echt sluit.

---

## 6. Voorstel: twee reeksen naast elkaar

### 6.1 De twee reeksen

**Reeks O — opgegeven oppervlakte (`m2_opgave`)**

Precies wat de bron zegt, ongewijzigd, met vermelding van de bron. Dit is de maat waarin de
markt praat: waarin Idealista `priceByArea` berekent, waarin makelaars onderhandelen, waarin
een koper zijn eigen vergelijking maakt. Nooit corrigeren, nooit weggooien.

Gebruik: marktvergelijking, onderhandelingspositie, communicatie met makelaars en kopers.

**Reeks W — bebouwd woondeel (`m2_woon`)**

De *superficie construida van het woongedeelte*: de gesloten, overdekte, bewoonbare bouwmassa,
buitenmuren meegerekend. Zonder open terras, zonder zwembad, zonder bestrating. Garage, kelder
en berging apart in `m2_bijruimte`, want die kosten en brengen niet hetzelfde op als
hoofdruimte.

Waarom bebouwd en niet nuttig: **bouwkosten worden in Spanje per m² construida geraamd**, en
onze eigen tarieven van 1.000 en 2.000 €/m² (`kader/investeringskader.json`) zijn dat ook. Een
reeks op nuttig oppervlak zou de kosten en de opbrengst weer uit elkaar trekken — precies de
fout die wij aan het repareren zijn.

Gebruik: bouwkosten, opbrengstraming, maximale koopprijs, perceelwaardering.

**Derde kolom, ter controle: `m2_util`.** Het nuttige oppervlak, als het uit een harde bron
komt. Niet nodig voor het rekenwerk, wel voor de onderhandeling — dit is het getal waar de
koper recht op heeft (RD 515/1989, §1.5) en waarmee je een makelaar kunt laten uitleggen
waarom zijn opgave zoveel hoger ligt.

Elk object krijgt reeks O en reeks W, plus een label voor de kwaliteit van `m2_woon`.

### 6.2 Hoe `m2_woon` tot stand komt — laddertje, hoogste beschikbare wint

| Trap | Bron | Bewijstype | Label |
|---|---|---|---|
| 1 | Eigen meting of bouwtekening | 1 | `gemeten` |
| 2 | Nota simple of escritura — construida van het woondeel | 2 | `akte` |
| 3 | Uitsplitsing per bouwdeel in de advertentietekst die optelt (geval 5) | 1 | `tekst_opbouw` |
| 4 | Woon-/living-getal letterlijk in de advertentietekst (geval 1) | 1 | `tekst` |
| 5 | Som van de `VIVIENDA`-posten uit Catastro, mits het perceel bevestigd is | 3 | `kadaster` |
| 6 | Opgave maal de factor uit §6.3 | 5 | `geschat` |

Alleen trap 1 tot en met 4 telt als hard. Trap 5 en 6 leveren een schatting waarmee je mag
rekenen, maar waarop je niet biedt.

Voor `m2_util` geldt een eigen laddertje: eigen meting → energiecertificaat →
Idealista `usableArea` **mits ≠ `size`** → útil-getal in de tekst. Geen schatting; is er niets,
dan blijft de kolom leeg.

### 6.3 De omrekenfactor — drie regimes, geen enkel getal

Als er niets hards is, bepaal eerst het regime uit de signalen in §3, dan pas de factor.
De factor brengt de opgave naar het **bebouwde woondeel**, niet naar het nuttige oppervlak.

| Regime | Herkenning | `m2_woon` = | Basis |
|---|---|---|---|
| **A — woon** | Tekst noemt living/habitable/woonoppervlakte bij een getal gelijk aan het veld; óf terras en kelder worden apart genoemd en tellen niet op tot het veld | opgave × **1,00** | Gevallen 1 en 2, §2.4 |
| **B — construida** | Geen tegenaanwijzing; kenmerk luidt "X m² construidos"; escritura-achtige formulering | opgave × **0,96** (band 0,90 – 1,00) | Het enige dat er te veel in zit, is overdekt terras tegen 50 %. Kadastermeting: mediaan 0 %, gemiddeld 3,4 %, p75 4,2 %, maximaal 43,5 % van het totaal (§4.2). Bij een zichtbaar groot overdekt terras of *naya*: 0,90 |
| **C — totaal** | Opsomming per bouwdeel die optelt tot het veld; *incluye/including/inclusief* bij terras, garage of kelder; meer dan 130 m² opgave per slaapkamer; opgave binnen 10 % van het kadastrale totaal terwijl `VIVIENDA` veel lager ligt | opgave × **0,62** (band 0,42 – 0,71) | Kadastermediaan 1/1,40 = 0,71 als bovengrens; gevallen 4 en 5 geven 0,62 en 0,42; wij nemen 0,62 als middenwaarde |
| **onbekend** | Geen enkel signaal, alleen een kaal getal | opgave × **0,90**, label `geschat`, object **niet** in de biedlijst | Midden tussen regime B en de kans dat het toch C is. Bewijstype 5 — dit is een keuze, geen meting |

Voor wie de útil erbij wil ramen: **útil ≈ construida ÷ 1,35** (band 1,18 – 1,45). Onze twee
harde paren geven 1,348 en 1,436; de literatuur 1,18 tot 1,33. Alleen ter controle gebruiken,
niet in het rekenmodel.

Waarom niet één factor over alles: één factor van 0,71 corrigeert regime A en B kapot — die
hadden nauwelijks correctie nodig — en regime C onvoldoende. Een correctie op een al kloppend
getal verlaagt de opbrengstraming zonder grond, en dat is precies het probleem dat wij
oplossen, alleen dan zelf veroorzaakt.

**De winst zit niet in de factor maar in de indeling.** Regime C is het enige regime dat echt
schade doet, en het is met de signalen uit §3 te herkennen. Het sterkste signaal — losse
m²-posten in de tekst die optellen tot het veld — klopte in beide gevallen waarin het van
toepassing was (gevallen 4 en 5, n = 2). Twee waarnemingen is weinig; de regel moet meelopen
en bijgehouden worden.

### 6.4 De vergelijkingsreeksen in `comparables.json`

Nu staat er één reeks per wijk, met als bron letterlijk
*"Idealista-assistent; vraagprijzen per m² gebouwd; geen transacties"*
(`kader/comparables.json`, veld `bron`). Dat is dus reeks O, en dat is op zichzelf goed —
zolang je hem ook alleen tegen reeks O afzet.

Voorstel: twee reeksen per wijk naast elkaar.

- `eur_m2_opgave` — ongewijzigd wat er nu staat, met `n` erbij.
- `eur_m2_woon` — dezelfde objecten, maar de prijs gedeeld door `m2_woon`, en **alleen de
  objecten waar `m2_woon` hard is** (trap 1 t/m 4). Beter een reeks van acht harde objecten
  dan van dertig geschatte.

Bij elke reeks: `n`, mediaan, p25, p75, en de datum. Is `n` voor `eur_m2_woon` kleiner dan
vijf voor een wijk, gebruik hem niet als hoofdreeks maar als controle op de andere.

De verhouding tussen beide reeksen per wijk is meteen een nuttige eigen meting: verschilt
die verhouding sterk per wijk, dan vullen de makelaars daar anders in, en dat is op zich
handelsinformatie.

---

## 7. Wat dit voor het rekenmodel betekent

Dit is de plek waar het geld zit.

In `tools/haalbaarheid.py` doet `sale_band(comps, key, m2, units)` dit:

```python
"sale": {"conservative": conservative * m2, "base": med * m2, "upside": upside * m2}
```

waarbij `m2` = `sc.result_m2`, en `conservative/med/upside` de €/m² uit `comparables.json`
zijn. Diezelfde `result_m2` voedt ook de bouwkosten (`renovation_m2`, `newbuild_m2` maal
1.000 respectievelijk 2.000 €/m²), en het terras zit daar als aparte post naast
(`exterior_m2` maal 120 €/m²).

Die scheiding laat zien dat het model `result_m2` bedoelt als **echt bebouwd oppervlak**, want
anders zou je het terras dubbel tellen. Maar de €/m² waarmee het vermenigvuldigd wordt, komt
uit **advertentie-oppervlakten**. Dat zijn twee verschillende maten.

Het gevolg, in één voorbeeld:

> Wij bouwen 200 m² woning. De wijkreeks zegt 4.000 €/m², maar die 4.000 is gerekend over
> advertentiemeters. Zitten daar gemiddeld terrassen in die de opgave 1,3 keer zo groot maken,
> dan is de echte prijs per m² woning 5.200 €. Ons model rekent 200 × 4.000 = 800.000 €
> verkoopopbrengst. Een vergelijkbaar huis in die wijk staat als 260 m² te koop voor
> 1.040.000 €. Wij ramen dus **23 % te laag** — en daarmee ook de maximale koopprijs en de
> perceelwaarde.

Bij factor 1,1 is de fout 9 %; bij 1,6 is hij 38 %. Wij weten niet welke factor geldt, en dat
is nu juist de reden om de fout niet met een factor te willen repareren. De klacht waarmee dit
onderzoek begon klopt dus; de richting staat vast, de omvang niet.

**Drie mogelijke oplossingen, in volgorde van voorkeur:**

1. **Reken de verkoopopbrengst in reeks O.** Zet naast `result_m2` een tweede veld
   `result_m2_opgave` = de m² zoals wíj het object straks zullen adverteren, inclusief
   overdekt terras op de gebruikelijke manier. Vermenigvuldig `eur_m2_opgave` daarmee. De
   bouwkosten blijven op `result_m2`. Dit is het meest getrouw aan de werkelijkheid: wij
   verkopen straks óók met een advertentieoppervlak.
2. **Reken alles in reeks W.** Gebruik `eur_m2_woon` maal `result_m2`. Zuiverder, maar alleen
   bruikbaar in wijken waar genoeg harde objecten zijn.
3. **Corrigeer de reeks met één factor.** Snelst te bouwen, minst betrouwbaar, en het verbergt
   de onzekerheid in plaats van hem te tonen. Alleen als tussenstap.

Wat er in de database bij moet, naast de bestaande `built_m2`:

| Kolom | Inhoud |
|---|---|
| `m2_opgave` | de bronopgave, ongewijzigd (= huidige `built_m2`) |
| `m2_bijruimte` | garage, kelder en berging, apart |
| `m2_util` | nuttig oppervlak, alleen uit harde bron; leeg als die er niet is |
| `m2_woon` | bebouwd woondeel volgens de ladder van §6.2 |
| `m2_woon_bron` | `gemeten` / `akte` / `epc` / `portaal_util` / `tekst` / `kadaster` / `geschat` |
| `opp_regime` | `A` / `B` / `C` / `onbekend` volgens §6.3 |
| `opp_signalen` | welke signalen uit §3 aansloegen, voor navolgbaarheid |
| `cat_rc` | kadastrale referentie, als die met redelijke zekerheid gevonden is |
| `cat_vivienda_m2`, `cat_totaal_m2` | uit `Consulta_DNPRC` |

En één regel in het dagrapport en op het dossier: bij regime C en bij label `geschat` een
zichtbare waarschuwing dat de oppervlakte niet vaststaat, met beide getallen naast elkaar.
De rekenaar waarschuwt nu al bij afwijkende grootte; dit past in dezelfde plek.

---

## 8. Wat wij niet hebben kunnen vaststellen

- **Wat Idealista adverteerders precies voorschrijft.** De helppagina's voor professionals
  zijn niet ingezien; er is geen openbaar veldvoorschrift gevonden dat zegt of `size`
  construida of útil moet zijn. Dat het in de praktijk construida is, blijkt uit de gegevens
  (§2.1), niet uit een voorschrift. **ONBEKEND / [te verifiëren]**
- **Wat Kyero bedoelt met `built`.** De specificatie zegt alleen "Constructed area". Er is
  geen definitie, en de rest van de documentatie staat achter een robots-verbod. **ONBEKEND**
- **Wat Fotocasa's invoerscherm voor professionals precies vraagt.** Alleen de publieke
  instructie voor particulieren is gecontroleerd; die zegt *superficie construida*. Of het
  Fotocasa Pro-scherm een apart útil-veld heeft, is niet vastgesteld. **[te verifiëren]**
- **Of de gemeten mediaan van 1,40 representatief is voor het hele werkgebied.** 48 percelen,
  gevonden via portaalcoördinaten die deels verschoven zijn. De samenstelling van de
  kadastrale opgave is robuust (dat is een eigenschap van villapercelen, niet van de match),
  de koppeling met de advertentie niet.
- **Hoe vaak het verschil tussen advertentie en kadaster een niet-aangemelde uitbreiding is
  in plaats van een opgeblazen opgave.** Dat vraagt per object een nota simple. Dit is
  waarschijnlijk de waardevolste vervolgstap, want het is tegelijk een risicosignaal.
- **Habitaclia, Milanuncios, Thinkspain en Rightmove** zijn niet onderzocht. Habitaclia en
  Milanuncios delen het Fotocasa Pro-invoerscherm, dus daar geldt vermoedelijk hetzelfde;
  niet bevestigd. **[te verifiëren]**
- **Of onze eigen woningfeed van Background Properties één invulconventie volgt.** De feed
  bundelt zes exports; de spreiding in §4.1 suggereert van niet, maar per leverende makelaar
  is het niet uitgesplitst.

---

## 9. Bronnen

| # | Bron | Type | Datum |
|---|---|---|---|
| 1 | Orden ECO/805/2003, art. 4 — definities útil en construida · <https://www.boe.es/buscar/act.php?id=BOE-A-2003-7253> | 2 | 18-09-2026 |
| 2 | RD 1020/1993, Norma 11.3 — kadastrale superficie construida · <https://www.boe.es/buscar/act.php?id=BOE-A-1993-19265> | 2 | 18-09-2026 |
| 3 | RD 515/1989, art. 4.3 — verkoper moet útil geven · <https://www.boe.es/buscar/act.php?id=BOE-A-1989-11181> | 2 | 18-09-2026 |
| 4 | RD 390/2021 — energiecertificaat, rekent op útil habitable · <https://www.boe.es/buscar/act.php?id=BOE-A-2021-9176> | 2 | 18-09-2026 |
| 5 | Kyero v3 importspecificatie, `surface_area` · <https://feeds.kyero.com/assets/kyero_v3_import_spec.txt> — let op robots-verbod, zie §2.3 | 1 | 18-09-2026 |
| 6 | Kyero help, XML import specification · <https://help.kyero.com/estate-agents/xml-import-specification> | 1 | 18-09-2026 |
| 7 | Fotocasa, publicatie-instructie "superficie construida" · <https://www.fotocasa.es/fotocasa-life/alquiler/como-puedo-publicar-un-anuncio-gratis-en-fotocasa/> | 1 | 18-09-2026 |
| 8 | Idealista-redactie, útil vs construida, 15–25 % · <https://www.idealista.com/news/inmobiliario/construccion/2023/02/17/804021-diferencia-entre-superficie-util-y-construida-de-un-inmueble> | 6 | 18-09-2026 |
| 9 | Franke & de la Fuente (Marbella), berekening oppervlakten · <https://www.frankedelafuente.com/calculation-of-surface-area-on-the-spanish-property-market/> | 6 | 18-09-2026 |
| 10 | Idealista-assistent, object 111563779 — "395 m² construidos, 293 m² útiles" · <https://www.idealista.com/inmueble/111563779/> | 1 | 18-09-2026 |
| 11 | Idealista-assistent, object 111666124 — 320 m² met sótano 160 m² erbuiten · <https://www.idealista.com/inmueble/111666124/> | 1 | 18-09-2026 |
| 12 | Idealista-assistent, objecten 112243449 en 111329930 — `usableArea` spiegelt `size` · <https://www.idealista.com/inmueble/112243449/> | 1 | 18-09-2026 |
| 13 | Catastro OVC `Consulta_RCCOOR` en `Consulta_DNPRC`, 120 opvragingen · <https://ovc.catastro.meh.es/ovcservweb/OVCSWLocalizacionRC/OVCCallejero.asmx/Consulta_DNPRC> | 3 | 18-09-2026 |
| 14 | Eigen woningfeed poort 3100, 224 objecten, veldenlijst en beschrijvingen | 1 | 18-09-2026 |
| 15 | `kader/comparables.json`, veld `bron` — reeks is gebouwd op vraagprijzen per m² gebouwd | 1 | 18-09-2026 |
| 16 | `tools/haalbaarheid.py`, functie `sale_band` — €/m² maal `result_m2` | 1 | 18-09-2026 |

Meetscripts en ruwe uitkomsten staan in `onderzoek/N06-meting/`
(`catastro_meting.py`, `tekst_analyse.py`, `analyse2.py` met de bijbehorende JSON en een
LEESMIJ). Gaan ze meedraaien, dan horen ze in `tools/` met een testje erbij.

---

## 10. Wat er nu moet gebeuren

1. Kolommen `m2_opgave`, `m2_woon`, `m2_woon_bron` en `opp_regime` toevoegen aan `listings`,
   en de classificatie uit §3 en §6.3 bouwen als functie met tests. Halve dag.
2. `comparables.json` uitbreiden met `eur_m2_woon` naast de bestaande reeks, en per wijk
   tellen hoeveel harde objecten er zijn. Halve dag, plus het handwerk om de útil van de
   vergelijkingsobjecten te achterhalen.
3. `sale_band` laten kiezen welke reeks hij gebruikt, met oplossing 1 uit §7 als standaard.
   Daarna `python -m dh.reanalyse` en kijken hoeveel de maximale koopprijzen verschuiven. Dat
   getal wil je zien voordat je het vertrouwt.
4. ⏸️ **ACTIE VOOR JAN** — beslissen of wij per serieuze kandidaat standaard een nota simple
   opvragen (§5.3), en het volledige energiecertificaat opvragen in plaats van alleen de
   letter (§3.3).

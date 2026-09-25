# N08 — Steilheid per perceel: welke gratis hoogtebron werkt, en waar leggen wij de grens

Onderzoek voor TREE Deal Hunter · opgesteld en getoetst **25-09-2026** · werkgebied Jávea/Xàbia
(provincie Alicante) · alle HTTP-toetsen op die datum zelf uitgevoerd

**Bewijstypen (masterprompt §5):** 1 door aanbieder vermeld · 2 officiële bron · 3 door ons
vastgesteld · 4 AI-gevolgtrekking · 5 berekening · 6 professional · 7 onbekend of tegenstrijdig.

---

## Conclusie

1. **Er is een bruikbare gratis bron en die werkt vandaag: het MDT05 van het IGN via hun WCS-dienst**
   — een hoogteraster van 5 bij 5 meter over heel Spanje, CC BY 4.0, zonder sleutel, zonder kosten en
   zonder aanmelding. Getoetst op de drie opgegeven percelen; de antwoorden staan in §4.
2. **Goolzoom heeft géén hoogte- of hellingendpoint.** De documentatie noemt vijf endpointfamilies
   (cadastre, landregistry, delimitations, statistics, urbanplanning) en geen daarvan gaat over
   hoogte. Ik heb alle documentatiepagina's op woorden als *elevación, altitud, pendiente, cota,
   MDT, LiDAR* doorzocht: nul treffers. Zie §3.3.
3. Het Institut Cartogràfic Valencià (ICV/IDEV) heeft wél een **reliëfkaart, maar alleen als
   plaatje** — een WMTS/WMS met één RGB-laag, niet bevraagbaar, dus geen getallen. Zie §3.4.
4. **Voorstel voor de drempels** (§7), gerekend op de mediane celhelling van het perceel:
   **vlak < 8 %** (€ 0) · **licht hellend 8–15 %** (€ 15.000) · **steil ≥ 15 %** (€ 50.000).
   In een steekproef van 125 Jávea-percelen valt dat uiteen in 30 % / 28 % / 42 %. De grens van
   **15 % is goed onderbouwd** (FAO-bodemklassen, escalonamiento-plicht in Spaanse ordenanzas, het
   CTE-maximum van 12 % voor een oprit, en een Jávea-makelaar die "ideal slope 0–15 %" schrijft);
   de grens van **8 % is zwakker** en leunt op één commerciële kostenbron. Zie §7.3 en §7.4.
5. **Jans bedragen blijken plausibel.** Een Spaanse kostenbron geeft voor het bouwrijp maken van een
   kavel drie banden: € 1.500–6.000 (vlak), € 8.000–25.000 (helling 8–15 %) en € 25.000–60.000
   (steil en rots). € 15.000 zit midden in de middenband, € 50.000 bovenin de hoge band. Commerciële
   bron, geen officiële prijsbasis — zie §7.5.
6. Het rekenmodel heeft de haak er al in zitten: `tools/haalbaarheid.py::earthworks` leest
   `sc.slope` ∈ {vlak, licht, steil} en telt € 0 / € 15.000 / € 50.000 op. Wat ontbreekt is het
   automatisch **vullen** van dat veld. Dat kan met wat in dit rapport staat.
7. **Hoeveel het uitmaakt is meteen gemeten.** Van de 340 focus-objecten met een perceelgrens is
   45 % steil en 33 % licht hellend; bij de bouwkavels is **52 % steil**. Gemiddeld ontbreekt er nu
   **€ 27.441 per object** in de som. Zie §6.1. Dat kostte 68 verzoeken aan het IGN, dus het is ook
   goedkoop om bij te houden.

---

## 1. Waarom dit nodig is

`kader/parameters.json` heeft sinds 25-09-2026 twee bedragen: `earthworks_light_eur: 15000` en
`earthworks_steep_eur: 50000`. Ze worden alleen gebruikt als iemand handmatig in het dashboard de
schuif `slope` zet (`dh/dashboard.py`, endpoint `POST /api/listing/{id}/wat-als`). Staat die niet,
dan rekent `tools/haalbaarheid.py` **nul** grondwerk — ook voor een perceel aan de Tosal met 50 %
helling. Dat is precies de tegenvaller die Jan genoemd heeft, en hij zit nu structureel níét in de
som.

Er staat al één waarschuwing over in de dossiers (`kader/kandidaten.json`: *"helling maakt
keermuren waarschijnlijk (kosten niet begroot)"*), maar dat is tekst, geen bedrag.

---

## 2. Wat er per perceel al klaar ligt

De tabel `parcels` in `data/dealhunter.sqlite` bevat per object de kadastrale referentie én de
**perceelgrens als GeoJSON** (kolom `geojson`), opgehaald bij Catastro INSPIRE. Stand vandaag
(type 3, eigen telling):

| | aantal |
|---|---|
| actieve advertenties | 1.889 |
| rijen in `parcels` | 630 |
| daarvan met perceelgrens | **622** |
| actief, met coördinaat maar zonder perceelgrens | 99 |

Per categorie (actief, met perceelgrens / totaal): perceel 151/253 · renovatie 84/97 ·
appartement 114/330 · bijzonder 4/5 · overig 226/1.159.

Dus voor de categorieën die er in de focus toe doen (perceel, renovatie, bijzonder) is de geometrie
er al voor ruwweg twee derde. Voor de rest kan een cirkel rond het coördinaat dienen als noodoplossing
(§8.4).

---

## 3. De bronnen, één voor één getoetst

### 3.1 IGN MDT05 via WCS — **werkt, en is de winnaar**

**Dienst:** `https://servicios.idee.es/wcs-inspire/mdt`
GetCapabilities: <https://servicios.idee.es/wcs-inspire/mdt?request=GetCapabilities&service=WCS>
— zelf opgehaald 25-09-2026, HTTP 200, 11.928 bytes (type 3).

Wat er letterlijk in dat antwoord staat (type 2, het is het officiële capabilities-document):

- **Titel:** "Modelos Digitales del Terreno de España"
- **Aanbieder:** "Instituto Geográfico Nacional"
- **`ows:Fees`:** "No se aplican condiciones" — er gelden geen voorwaarden
- **`ows:AccessConstraints`:** "CC BY 4.0 scne.es" — bronvermelding verplicht, verder vrij
- **Herkomst:** "procedentes de sensores LiDAR aerotransportados del proyecto PNOA-LiDAR"

**Beschikbare hoogtelagen** (17 stuks, per coördinaatstelsel × maaswijdte):

| Maaswijdte | EPSG:25830 (UTM30) | EPSG:4258 (ETRS89 geo) | EPSG:4326 | EPSG:4083 (Canarias) |
|---|---|---|---|---|
| 5 m | `Elevacion25830_5` | `Elevacion4258_5` | — | `Elevacion4083_5` |
| 25 m | `Elevacion25830_25` | `Elevacion4258_25` | — | `Elevacion4083_25` |
| 200 m | ✔ | ✔ | — | ✔ |
| 500 m | ✔ | ✔ | ✔ | ✔ |
| 1000 m | ✔ | ✔ | ✔ | ✔ |

**Er is géén 2 m-laag in deze dienst.** Ik heb dat expliciet getoetst: een verzoek aan het pad
`/wcs-inspire/mdt-2m` geeft HTTP 200 met een antwoord dat **bit voor bit identiek** is aan dat van
`/wcs-inspire/mdt` (md5 `671dd515547d33963bdb933cf556899c` voor beide). De server negeert het pad;
dat is dus geen bewijs van een 2 m-dienst maar het tegendeel (type 3).

**Het raster.** DescribeCoverage van `Elevacion25830_5`
(<https://servicios.idee.es/wcs-inspire/mdt?service=WCS&version=2.0.1&request=DescribeCoverage&coverageId=Elevacion25830_5>,
25-09-2026, type 3):

- coördinaatstelsel EPSG:25830 (ETRS89 / UTM zone 30N), assen `x y`, eenheid meter
- oorsprong `-19450.000000 4865680.000000`, offsetvectoren `5 0` en `0 -5` → celranden liggen op
  x = −19452,5 + 5·k en y = 4.865.682,5 − 5·k
- envelop `-19452.5 3901197.5` tot `1140352.5 4865682.5` — heel schiereilandelijk Spanje
- native formaat COG

**Opvragen van hoogtes.** GetCoverage met `format=application/asc` geeft een **ASCII-grid in
platte tekst** binnen een multipart-antwoord. Dat is de sleutel tot bruikbaarheid hier: het is
leesbaar met de standaardbibliotheek, er is géén rasterio, GDAL of pyproj voor nodig — en er hoeft
dus niets geïnstalleerd te worden. Voorbeeld (werkelijk antwoord, 25-09-2026):

```
ncols        12
nrows         9
xllcorner    776520.000000000000
yllcorner    4295435.000000000000
cellsize     5.000000000000
 12.031 12.380 12.995 12.999 13.000 12.998 13.009 13.020 12.824 12.296 11.999 11.971
 ...
```

> **Valstrik.** Vraag je een vak dat niet precies op de celranden valt, dan herschaalt de server
> en schrijft hij `dx`/`dy` in plaats van `cellsize` — met bijvoorbeeld `dx 5.038461538459`. Snap
> het gevraagde vak eerst op het rooster van §3.1 (oorsprong + 5 m), dan krijg je exact 5,000.
> Zelf tegengekomen en opgelost (type 3).

**Snelheid.** Eén perceel (vak van ~80 × 80 m) duurt onder de halve seconde. Een vak van
**2 × 2 km, 401 × 401 = 160.801 cellen, kwam in 0,7 seconde binnen** (type 3). Dat betekent dat het
hele gemeentegebied van Jávea in een stuk of twintig verzoeken past (oppervlakte gemeente
[te verifiëren]) — zie §8.2.

### 3.2 IGN MDT02 (2 m) — bestaat, maar niet als dienst

Het Centro de Descargas van het CNIG noemt MDT02 als product: maaswijdte 2 m, 2e dekking 2015–2021,
formaat COG (Cloud Optimized GeoTIFF).
<https://centrodedescargas.cnig.es/CentroDescargas/modelos-digitales-elevaciones>, 25-09-2026
(type 1).

Twee dingen ontbreken:

- **Er is geen WCS of API voor MDT02** — zie de toets in §3.1. Je zou de bladen als bestand moeten
  downloaden.
- **Of Alicante gedekt is, is ONBEKEND.** De nieuwspagina van de serie
  (<https://centrodedescargas.cnig.es/CentroDescargas/novedades?codSerie=MDT02>, 25-09-2026) noemt
  alleen "la zona de Castilla la Mancha Suroeste" en geeft geen dekkingslijst per provincie (type 7).

⏸️ **ACTIE VOOR JAN (klein, optioneel):** als wij ooit naar 2 m willen, moet iemand in de kaartzoeker
van het Centro de Descargas kijken of het blad over Jávea er staat, en dan één bestand downloaden.
Dat is een download van vermoedelijk honderden MB's; ik heb dat bewust **niet** gedaan.

### 3.3 Goolzoom — geen hoogte, definitief

De sleutel staat in `.env` en de koppeling draait al (`dh/goolzoom.py`). Ik heb de documentatie
gelezen zoals gevraagd, en alle zes pagina's als ruwe HTML opgehaald en doorzocht (25-09-2026,
type 3):

| Pagina | bytes | treffers op elevación / altitud / altura / pendiente / cota / relieve / topograf / MDT / DEM / LiDAR / elevation / slope |
|---|---|---|
| General.aspx | 78.985 | 0 (de enige schijntreffer op "lidar" zit in het woord va**lidar**se) |
| Cadastre.aspx | 487.832 | 0 |
| LandRegistry.aspx | 77.950 | 0 |
| Delimitations.aspx | 82.521 | 0 |
| StatisticalData.aspx | 75.052 | 0 |
| UrbanPlanning.aspx | 79.283 | 0 |

De volledige lijst endpointpaden die in die documentatie voorkomt (uit de HTML zelf geschraapt) is:
`cadastre/provinces`, `cadastre/municipalities/{provincecode}`, `cadastre/streets/…`,
`cadastre/streetnumbers/…`, `cadastre/exactaddress/…`, `cadastre/cadastralparcel/{rc14}` met
`/cadastralreferences` en `/facade`, `cadastre/cadastralreference/{rc20}` met `/data`, `/geo`,
`/value` en `/referencevalue`, `cadastre/polygonparcel/…`, `cadastre/latlng/{lat}/{lng}`,
`cadastre/tilesets/{tilesetid}/{z}/{x}/{y}`, `landregistry/cadastralreference/…`,
`landregistry/idufir/…`, `delimitations/…`, `statistics/{groupkey}/{delimitationcode}`,
`urbanplanning/cadastralparcel/{rc14}/{layer}` (`/data`, `/geo`) en `urbanplanning/latlng/…`.

**Geen daarvan levert hoogte, helling of terrein.** Ik heb dus géén Goolzoom-verzoek voor dit
onderzoek gedaan: er valt niets te bevragen, en elke bevraging kost geld. De sleutel is nergens
afgedrukt of overgenomen.

De officiële Engelse API-referentie op <https://apireference.goolzoom.com/> laadt haar inhoud pas
met JavaScript en gaf bij het ophalen alleen een lege Stoplight-schil — dat is dus **geen** bewijs
in de ene of andere richting (type 7). De Spaanse documentatiepagina's hierboven zijn wel volledig
en die zijn leidend.

### 3.4 ICV / IDEV (Generalitat Valenciana) — alleen een reliëfplaatje

De officiële dienstenlijst <https://idev.gva.es/es/servicios-web> (25-09-2026, type 2) noemt als
enige terreinproduct de "Mapa de relieve" op `https://terramapas.icv.gva.es/mapabase_isohipsas`.

Getoetst (type 3): GetCapabilities als WMS 1.3.0 geeft HTTP 200, titel "MAPABASE RELIEVE de la
Comunitat Valenciana", **één laag** `01_8bits_01_RGB_05_PNG`, en **nul lagen met `queryable="1"`**.
Het is dus een gerenderd 8-bits RGB-plaatje: mooi om op de kaart te leggen, maar er komt geen
hoogte in meters uit. Er staat op die pagina geen WCS-endpoint voor hoogte.

`https://terrasit.gva.es` gaf geen verbinding (curl exit, HTTP 000, twee pogingen 25-09-2026) —
ONBEKEND of die dienst nog bestaat (type 7).

Het ICV heeft wél LiDAR-bestanden om te downloaden, maar dat is dezelfde route als MDT02: handmatig,
per blad, geen dienst.

### 3.5 EU-DEM 25 m — als tegenproef gebruikt, niet bruikbaar als bron

Voor een onafhankelijke tweede mening heb ik de publieke OpenTopoData-API met de dataset `eudem25m`
(Copernicus EU-DEM) bevraagd op de zwaartepunten van de drie percelen
(<https://api.opentopodata.org/v1/eudem25m>, 25-09-2026, type 3):

| perceel | EU-DEM 25 m | MDT05 op het perceel |
|---|---|---|
| 0481122BC5907N | 98,8 m | 91,5 – 98,5 m |
| 5246308BC5954N | 17,2 m | 13,0 – 14,5 m |
| 0010004BC5905S | 10,9 m | 7,3 – 9,0 m |

EU-DEM ligt stelselmatig 2,5 tot 4 meter hóger. Dat past bij wat EU-DEM is (25 m maaswijdte,
afgeleid van SRTM/ASTER, met een bekende opwaartse afwijking in bebouwd en begroeid gebied). Het
bevestigt de orde van grootte, maar het is te grof voor een perceel van duizend vierkante meter.
**Niet gebruiken als bron; wel bruikbaar als grove controle.**

---

## 4. De toets op de drie opgegeven percelen

Methode: perceelgrens uit `parcels.geojson`, omgezet naar EPSG:25830, MDT05 opgehaald over het
omhullende vak plus 10 m, en alle rastercellen genomen waarvan het middelpunt binnen het perceel
valt. Werkelijke antwoorden van 25-09-2026 (type 3/5):

### 0481122BC5907N — Penyaparda, El Garroferal (stedelijk)

| | |
|---|---|
| kadaster | CL PENYAPARDA PROLG. 3, 1.622 m², "suelos sin edificar" |
| advertentie | Villa El Garroferal, € 2.350.000, plot 1.646 m², bebouwd 337 m² |
| rastercellen in het perceel | 65 (= 1.625 m², klopt met de kadastrale maat) |
| hoogte | **91,5 tot 98,5 m** boven zee |
| hoogteverschil | **6,99 m** (p5–p95: 5,91 m) |
| langste as van het perceel | 61,5 m |
| helling via een kleinste-kwadratenvlak | **12,2 %**, afdalend naar 214° (zuidwest), rms 0,18 m |
| mediane celhelling (Horn 3×3) | **13,9 %** · p90 17,1 % |
| **oordeel** | **licht hellend** (€ 15.000) — maar dicht tegen de grens met steil |

WCS-verzoek: `…&coverageId=Elevacion25830_5&subset=x(771482.5,771552.5)&subset=y(4298527.5,4298612.5)&format=application/asc`

### 5246308BC5954N — Jaume Huguet 6, Adsubia (stedelijk)

| | |
|---|---|
| kadaster | CL JAUME HUGUET 6, 1.024 m² perceel, 275 m² bebouwd, bouwjaar 2005, "Residencial" |
| advertentie | "Land Adsubia", € 850.000, plot 2.600 m² — **let op: kadaster zegt 1.024 m²** |
| rastercellen in het perceel | 41 (= 1.025 m², klopt met het kadaster, niet met de advertentie) |
| hoogte | **13,0 tot 14,5 m** |
| hoogteverschil | **1,47 m** (p5–p95: 0,80 m) |
| langste as | 48,7 m |
| vlakhelling | **2,3 %**, afdalend naar 303°, rms 0,21 m |
| mediane celhelling | **6,8 %** · p90 11,0 % |
| **oordeel** | **vlak** (€ 0) |

### 0010004BC5905S — Camí la Fontana 10, Montañar

| | |
|---|---|
| kadaster | CM FONTANA LA 10, 1.949 m² perceel, 3.493 m² bebouwd, bouwjaar 1990, gebruik **"Deportivo"** |
| advertentie | *Ático* in Montañar, € 225.000, 20 m² bebouwd |
| rastercellen in het perceel | 135 (= 3.375 m², meer dan de kadastrale 1.949 m²) |
| hoogte | **7,3 tot 9,0 m** |
| hoogteverschil | **1,70 m** (p5–p95: 1,00 m) |
| langste as | 202,1 m (multipolygoon) |
| vlakhelling | **1,1 %**, rms 0,22 m |
| mediane celhelling | **0,0 %** · p90 6,7 % |
| **oordeel** | **vlak** (€ 0) — maar zie de waarschuwing hieronder |

> **Dit derde perceel is het schoolvoorbeeld van waarom de helling alleen niets zegt.** De
> advertentie is een appartement van 20 m² op de derde verdieping; het kadastrale perceel eronder
> is een sportcomplex van bijna 2.000 m². Een helling van het *perceel* is voor dit object
> betekenisloos. De bestaande toets `summary.perceel_is_het_object` (25-09-2026) moet hier
> hetzelfde werk doen als bij de fiscale waarschuwing: geen hellingtoeslag als het perceel het
> object niet ís.

Het rustieke perceel dat in de opdracht stond (0010004BC5905S) blijkt in het kadaster dus géén
rustiek perceel maar een stedelijk sportterrein. Dat is geen fout van deze meting — het is wat het
kadaster zegt.

---

## 5. Klopt het MDT wel? Drie controles

| Controle | Verwacht | MDT05/MDT25 zegt | Uitkomst |
|---|---|---|---|
| Zee vóór de haven van Jávea (0,190 O / 38,790 N) | 0 m | **0,0 m** | ✔ |
| Strand Arenal (0,1869 O / 38,7676 N) | een paar meter | **2,0 – 3,0 m** | ✔ |
| Hoogste punt van het Montgó-massief | 753 m (algemeen gepubliceerd); de geodetische pilaar zelf 751 m | **752,0 m** volgens MDT25 over een vak van 9,4 × 6,4 km | ✔ binnen 1 m |

Bron voor de Montgó-hoogte: <https://en.javea.com/el-paraje-del-montgo-uno-de-los-mejores-sitios-para-hacer-senderismo/ruta-montgo-2/>
en de beschrijving van het natuurpark bij de Generalitat
<https://parquesnaturales.gva.es/es/web/pn-el-montgo/ruta-verde-claro-descripcion> (25-09-2026,
type 1). De 753 m is een veelgenoemd getal, geen door mij bij het IGN geverifieerde kaartwaarde —
maar de overeenkomst binnen één meter is sterk genoeg om te zeggen dat het model niet scheef staat.

**De coördinaatomzetting is apart gecontroleerd.** Wij hebben geen `pyproj` op deze machine, dus de
omzetting WGS84 → UTM 30N is met de standaard Krüger-reeks in gewone Python gedaan. Toetsing: van
perceel 5246308BC5954N heb ik dezelfde grens twee keer opgehaald bij Catastro INSPIRE — eenmaal in
EPSG:4326 (zoals die in onze database staat) en eenmaal rechtstreeks in EPSG:25830
(`…wfsCP.aspx?…&srsname=EPSG::25830`). Beide keren 87 punten; het verschil in het omhullende vak
is **0,32 en 0,36 m in x, 0,05 en 0,06 m in y** (type 3/5). Dat is kleiner dan de rasterresolutie
van 5 m en grotendeels het gevolg van de zes decimalen waarmee wij lengte- en breedtegraad opslaan.
Voor de productiekant is het schoner om de grens meteen in EPSG:25830 op te vragen; dan valt de
omzetting helemaal weg.

**Nauwkeurigheid van de bron zelf.** Het PNOA-LiDAR-portaal
(<https://pnoa.ign.es/web/portal/pnoa-lidar/presentacion>, 25-09-2026, type 1) geeft voor de
1e dekking (2009–2015) een puntdichtheid van 0,5 punt/m² en een **hoogtefout van 40 cm (RMSE Z)**,
en voor de 3e dekking (2022–2025) 5 punten/m² en 10 cm. Het MDT05 hoort bij de 1e dekking; het
MDT02 bij de 2e. Voor de 2e dekking staat er geen getal (type 7).

**Wat 40 cm betekent voor ons.** Een hoogteverschil van 7 m over een perceel is ruim boven de ruis
en dus hard. Een hoogteverschil van 1,5 m over veertig meter is dat niet: daar zit de meting op
hetzelfde niveau als de fout. Daarom telt hieronder de **hellingsklasse**, nooit een exact bedrag
aan kuub grondverzet.

---

## 6. Hoe steil is Jávea eigenlijk? Steekproef van 125 percelen

Ik heb de methode over een steekproef van 125 percelen met geometrie laten lopen (één op vijf uit
de 622, alfabetisch op kadastrale referentie, 1 verzoek per 2 seconden). 120 daarvan hadden acht of
meer rastercellen; 5 percelen waren te klein voor een betrouwbare meting op 5 m.

**Verdeling van de mediane celhelling** (n = 120, type 5):

| | p10 | p25 | mediaan | p75 | p90 | max |
|---|---|---|---|---|---|---|
| mediane celhelling (%) | 2,6 | 6,7 | **12,9** | 25,7 | 39,5 | 62,6 |
| helling via vlakfit (%) | 1,9 | 3,5 | 9,6 | 18,6 | 39,8 | 73,3 |
| hoogteverschil over het perceel (m) | 1,3 | 2,8 | 5,8 | 14,5 | 54,2 | 192,2 |

Het beeld klopt met wat je in Jávea ziet, en dat is meteen de belangrijkste plausibiliteitstoets:

**Steilste percelen in de steekproef** (categorie perceel/renovatie/bijzonder):

| kadastrale ref. | mediane celhelling | hoogteverschil | wijk | vraagprijs |
|---|---|---|---|---|
| 03082A00300026 | 54,3 % | 36,7 m | Puerto | € 1.135.000 |
| 03082A00200037 | 52,9 % | 58,1 m | Partida Tosal – Zona dels Castellans | € 995.000 |
| 3177713BC5937N | 43,0 % | 24,7 m | Calle Langreo 11, Tosal/Castellans | € 950.000 |
| 2166816BC5826N | 35,0 % | 5,2 m | El Portet (Moraira) | € 240.000 |
| 0585208BC5808N | 34,8 % | 11,2 m | Benimeit-Tabaira (Moraira) | € 240.000 |
| 7826607BC5972N | 34,5 % | 16,3 m | La Granadella – Costa Nova | € 419.000 |

**Vlakste percelen:** Montañar (0,0 %), Paichi (0,8 %), Centro Ciudad (1,8 % en 2,4 %),
Pinomar-Pinosol (2,8 %).

Precies de hellingen die Jan noemt (Tosal, Granadella, Portet) komen bovenaan, en de kustvlakte
(Montañar, Centro, Pinosol) onderaan. Dat is geen bewijs, maar het is wel het soort uitkomst dat je
wilt zien voordat je dit in het geld laat meetellen.

### 6.1 En hoeveel scheelt dat in het rekenmodel? Alle focus-objecten doorgemeten

Omdat de tegelmethode uit §8.2 zo licht is, heb ik hem meteen over de **hele focuslijst** gehaald:
763 objecten in beeld, 361 daarvan met een perceelgrens, 340 met genoeg rastercellen voor een
uitspraak. Dat kostte **68 verzoeken** aan het IGN (32 tegels van 2 × 2 km plus 36 objecten die
over een tegelrand liggen) in ongeveer drie minuten (25-09-2026, type 3/5).

| Categorie | gemeten | vlak | licht hellend | steil |
|---|---|---|---|---|
| perceel | 146 | 27 | 43 | **76** |
| overig | 106 | 22 | 34 | 50 |
| renovatie | 76 | 20 | 31 | 25 |
| appartement-renovatie | 8 | 4 | 3 | 1 |
| bijzonder | 4 | 2 | 1 | 1 |
| **totaal** | **340** | **75 (22 %)** | **112 (33 %)** | **153 (45 %)** |

**Wat dat betekent in geld.** Over deze 340 objecten telt de toeslag op tot € 9,3 miljoen, ofwel
**gemiddeld € 27.441 per object** dat nu nergens in de som staat. Bij de bouwkavels is het beeld het
scherpst: **76 van de 146 percelen (52 %) vallen in de steile klasse** en krijgen dus € 50.000 erbij.

Dat is de kern van dit onderzoek. Het gaat niet om een verfijning van de derde decimaal — bij ruim
de helft van de percelen die wij nu doorrekenen ontbreekt een post die in dezelfde orde ligt als
een halve keuken tot een hele badkamerverbouwing. En omdat die post ontbreekt, ziet elk hellend
perceel er in de huidige rangschikking te goed uit ten opzichte van een vlak perceel.

> Getallen berekend met de voorgestelde drempels uit §7.2. Bij een bovengrens van 20 % in plaats
> van 15 % zou de verdeling 22 % / 46 % / 32 % zijn; de keuze van die ene grens verschuift dus
> **44 objecten** van de € 50.000-band naar de € 15.000-band, goed voor € 1,54 miljoen verschil in
> de totale toeslag. Dat is precies waarom §7.3 zo uitvoerig is.

---

## 7. Voorstel voor de drempels

### 7.1 Welke maat

Drie maten zijn berekend; de **mediane celhelling** is de beste:

- **Hoogteverschil (max − min) over het perceel.** Intuïtief, maar hangt volledig af van de
  perceelgrootte. 5 m verschil op 400 m² is steil; 5 m op 5.000 m² is bijna vlak. Alleen bruikbaar
  in combinatie met de perceelmaat.
- **Helling via een kleinste-kwadratenvlak door het perceel.** Prima op een normaal bouwperceel,
  maar hij faalt op grote en geplooide percelen: perceel 001500400BC78G (5.870 cellen, 95,6 m
  hoogteverschil) komt met een vlakfit op 11,8 % uit terwijl de mediane celhelling 31,9 % is — het
  vlak legt zich netjes door een dal heen. Bij percelen vanaf ongeveer 5.000 m² loopt het verschil
  tussen de twee maten op tot mediaan 4,3 procentpunt en p90 20,1 procentpunt (type 5).
- **Mediane celhelling (Horn 3×3 over het 5 m-raster).** Ongevoelig voor de vorm en voor
  uitschieters, en hij meet wat je wilt weten: hoe schuin ligt de grond waar je gaat bouwen.
  **Dit is de voorgestelde hoofdmaat.**

Over de hele steekproef zouden de twee maten 33 van de 120 percelen (28 %) in een andere klasse
zetten — dus de keuze is niet vrijblijvend.

### 7.2 De grenzen

| Klasse | Mediane celhelling | Toeslag | Aandeel in de steekproef |
|---|---|---|---|
| **vlak** | **< 8 %** | € 0 | 36 van 120 (30 %) |
| **licht hellend** | **8 % tot 15 %** | € 15.000 | 34 van 120 (28 %) |
| **steil** | **≥ 15 %** | € 50.000 | 50 van 120 (42 %) |
| **onbekend** | minder dan 8 rastercellen in het perceel, of geen perceelgrens | geen toeslag, mét vermelding | 5 van 125 (4 %) |

### 7.3 Waarom 15 % — dit is de sterke grens

De bovengrens van 15 % komt op **vijf onafhankelijke manieren** terug (alle gecontroleerd
25-09-2026):

1. **Bodemkundige standaard.** FAO, *Guidelines for Soil Description* (4e editie, 2006): de klasse
   *strongly sloping* loopt tot 15 %, daarboven begint *moderately steep* (15–30 %).
   <https://www.fao.org/4/a0541e/a0541e.pdf> (type 2, gelezen als zoekmachine-samenvatting van de
   officiële PDF, niet woordelijk — zie de waarschuwing onderaan).
   De USDA/NRCS Soil Survey Manual legt de vergelijkbare knip bij 12 % en 20 %
   (*moderately steep* 12–20 %, *steep* 20–30 %):
   <https://www.nrcs.usda.gov/sites/default/files/2022-09/SSM-ch8.pdf> (type 2, idem).
2. **Spaanse gemeentelijke ordenanzas.** Boven 15 % helling geldt in verschillende Spaanse
   ordenanzas een verplichting tot *escalonamiento* — getrapt bouwen — zodra het hoogteverschil
   tussen twee gevellijnen meer dan één bouwlaag bedraagt, met terrassen die hooguit 3 m van het
   oorspronkelijke maaiveld mogen afwijken (ordenanza de edificación Agüimes,
   <https://aguimes.es/transparencia-11-ordenanza-edificacion-04-05-21/>). Santa Cruz de Tenerife
   hanteert een apart regime onder en boven 15 %, met een band 15–35 %
   (<https://www.urbanismosantacruz.es/sites/default/files/ordenanzas/Edificacion/22-12-21_orden_edif.pdf>).
   **Let op:** dit zijn Canarische gemeenten. Of Xàbia of de Comunitat Valenciana een eigen
   hellingsdrempel kent is **ONBEKEND** (type 7) — zie §11.
3. **De markt hier.** Een makelaar in Jávea zelf schrijft over kavelkeuze op de Costa Blanca:
   *"Ideal slope: 0–15%"*, en 15–30 % alleen als het uitzicht het compenseert; toegangsoprit
   maximaal 12 %. <https://www.costa-houses.com/en/blog/how-to-choose-solar-luxury-villa-costa-blanca/>
   (18-09-2025, commerciële bron, type 1).
4. **Het kostenomslagpunt.** Boven ongeveer 10–15 % worden keermuren nodig en schuift het
   grondwerkbudget naar de middenband. <https://gestland-grup.com/articulos/cuanto-cuesta-construir-casa-teniendo-terreno/>
   (20-11-2025, commerciële bron, type 1).
5. **Onze eigen meetkunde.** Bij 15 % overbrug je over vijftien meter gevelbreedte 2,25 m — meer
   dan één verdiepingshoogte, dus per definitie niet meer met wat grondverzet op te lossen (type 5).

**De 12 % uit het CTE is de harde toegangsgrens.** In het Código Técnico de la Edificación, DB-SUA 1
§4, geldt een vlak boven 4 % al als *rampa*, mag een toegankelijke helling maximaal 6 tot 10 %
zijn (afhankelijk van de lengte) en een niet-toegankelijke maximaal 12 %
(<https://www.codigotecnico.org/pdf/Documentos/SUA/DBSUA.pdf>, weergegeven via
<https://www.verificacioncte.es/blog/rampas-accesibilidad>, type 2/1). Boven 12 % is een rechte
oprit dus geen optie meer en moet je zwenken of graven — nog een reden waarom 15 % de goede
bovengrens is en niet 20 %.

### 7.4 Waarom 8 % — dit is de zwakkere grens

De ondergrens van 8 % rust op één bron: de kostenbanden van Gestland Grup, die *adecuación media*
precies definieert als "pendiente 8–15 %" (zelfde URL als hierboven, commerciële bron, type 1). Dat
valt toevallig samen met wat ik zelf had gekozen op grond van de meetkunde (8 % × 15 m = 1,2 m, één
insteek en geen muur) en met de verdeling in ons eigen aanbod.

Alternatieven, als Jan of een architect er anders over denkt:

| Grens | Herkomst | Gevolg in onze steekproef |
|---|---|---|
| **4 %** | CTE: hierboven heet een vlak juridisch een *rampa* | veel meer objecten met toeslag |
| **5 %** | FAO: overgang *gently sloping* → *sloping* | vlak 21 % · licht 38 % · steil 42 % |
| **8 %** (voorstel) | kostenband *adecuación media* | vlak 30 % · licht 28 % · steil 42 % |

**Advies: 8 % aanhouden**, omdat die grens het kostengedrag volgt en niet het bodemprofiel — en het
gaat hier om een kostentoeslag, niet om een bodemkaart.

### 7.5 Kloppen de bedragen € 15.000 en € 50.000?

Dit was een open vraag; er is nu een eerste antwoord. Dezelfde Spaanse bron geeft drie
kostenbanden voor het bouwrijp maken van een kavel (type 1, commercieel, 20-11-2025):

| Band | Situatie | Bedrag |
|---|---|---|
| *adecuación mínima* | vlak, geconsolideerd stedelijk | € 1.500 – 6.000 |
| *adecuación media* | **helling 8–15 %**: gematigd grondwerk, lage keermuren, puntdrainage | **€ 8.000 – 25.000** |
| *adecuación alta* | steil en rots: forse keermuren, rotsontgraving, machinetoegang, drainage | **€ 25.000 – 60.000** |

**Jans € 15.000 zit midden in de middenband en zijn € 50.000 in de bovenkant van de hoge band.
Beide zijn dus plausibel** — en zijn klassegrenzen 8–15 % vallen samen met die van de bron.

Ter controle de kale eenheidsprijzen uit de Generador de precios van CYPE (op de pagina zelf
gelezen, 25-09-2026, type 1):

| Post | Code | Prijs |
|---|---|---|
| Desmonte en tierra (excl. transport) | ADD010 | € 2,12/m³ |
| Excavación mecánica a cielo abierto | ADE002 | € 5,33/m³ |
| Transporte de tierras ≤ 10 km | — | € 4,96/m³ |
| Canon de vertido | GTB020 | € 2,23/m³ |
| Muro de contención de hormigón armado, tot 3 m | UNM020 | € 164,86/m³ |
| Cuerpo de muro de escollera (stapelmuur) | CCE020 | € 95,79/m³ |

Ontgraven + afvoeren + storten komt daarmee op ongeveer € 9–14 per m³ (eigen optelsom, type 5).
Consumentenprijzen voor een keermuur liggen twee tot drie keer boven deze kale eenheden
(€ 150–350 per m² muurvlak, tot € 500 voor gewapend beton) — logisch, want CYPE rekent hier zonder
uitgraving, drainage, bekisting en marge.

> **Waarschuwing bij dit hele blok.** De prijsbanden komen van **commerciële aanbieders**, niet van
> een officiële prijsbasis. De twee Spaanse standaardbases — BEDEC van het ITeC en de prijsbasis van
> het Institut Valencià de l'Edificació — zitten achter een abonnement en zijn dus **niet**
> geraadpleegd (<https://en.itec.cat/services/bedec/>, <https://www.five.es/>, type 7). Gebruik dit
> als plausibiliteitstoets, niet als begroting.

⏸️ **ACTIE VOOR JAN:** neem één perceel dat je kent en waarvan je weet wat het grondwerk werkelijk
gekost heeft. Dan meten wij de helling van dat perceel na en weten wij binnen een uur of 8 % en
15 % goed liggen of moeten schuiven. Dat is de enige echte ijking.

---

## 8. Hoe je dit inbouwt

### 8.1 Waar het in past

`tools/haalbaarheid.py::earthworks` leest al `sc.slope`. Het enige dat mist is een module die per
listing dat veld vult, vergelijkbaar met `dh/enrich_urbanisme.py`. Voorstel: `dh/helling.py` met
een tabel `slope` (`listing_id`, `rc`, `cellen`, `z_min`, `z_max`, `hoogteverschil_m`,
`celhelling_mediaan_pct`, `vlak_helling_pct`, `vlak_richting_graden`, `klasse`, `fetched_at`,
`bron`), plus `dh/enrich_helling.py` als stap in `dh/run.py`.

Het terrein verandert niet, dus opnieuw ophalen hoeft nooit — één keer per perceel is genoeg. Alleen
als de perceelgrens verandert (nieuwe kadastrale referentie) opnieuw meten.

### 8.2 Doe het per tegel, niet per perceel

Per perceel één WCS-verzoek is de simpele weg (622 percelen × 2 s = ~21 minuten). Efficiënter en
veel vriendelijker voor het IGN: haal **tegels van 2 × 2 km** op (0,7 s per stuk, gemeten) en knip
alle percelen daar lokaal uit.

Dat is niet theoretisch — het is precies hoe §6.1 gedaan is. **361 percelen kostten 68 verzoeken:**
32 tegels plus 36 losse vakken voor percelen die over een tegelrand liggen. Per perceel zou dat
361 verzoeken zijn geweest, dus een factor vijf minder verkeer en in drie minuten klaar in plaats
van twaalf. Ter vergelijking: alle 718 actieve objecten met een coördinaat passen in 75 tegels van
2 × 2 km (of 158 van 1 × 1 km), dus ook de 99 objecten zónder perceelgrens komen daar gratis in mee
(type 3/5, gemeten 25-09-2026).

De werkende proefcode van dit onderzoek (coördinaatomzetting, WCS-ophaler, maskering op de
perceelgrens, drie hellingmaten) staat in de sessie-scratchpad als `geo.py` en `helling.py` onder
`/private/tmp/claude-501/-Users-root-admin-tree-es/a3ae9710-3e66-42bb-b602-476120d4027d/scratchpad/`.
Die map is tijdelijk — de code is bedoeld om overgenomen te worden in `dh/`, niet om daar te blijven
staan.

### 8.3 De valkuilen die ik tegenkwam

1. **Vak snappen op het rooster**, anders krijg je `dx 5.038…` in plaats van `cellsize 5` (§3.1).
2. **Het antwoord is multipart.** Na het ASCII-grid volgen nog `out.asc.aux.xml` en `out.prj`; knip
   op de eerstvolgende `--wcs`.
3. **Rij 0 is de bovenste** (noord). `yllcorner` hoort bij de onderste rij.
4. **TLS.** In deze omgeving faalt `urllib` op `servicios.idee.es` met
   `CERTIFICATE_VERIFY_FAILED: self-signed certificate in certificate chain`, terwijl `httpx` en
   `curl` het wél doen. Gebruik `httpx` (staat al in de Hermes-venv), net als `dh/goolzoom.py`.
5. **Geen pyproj.** De Krüger-omzetting in gewone Python werkt (§5), maar netter is de perceelgrens
   meteen in EPSG:25830 bij Catastro opvragen.

### 8.4 Wanneer je géén uitspraak doet

- **Minder dan 8 rastercellen in het perceel** (kleiner dan ongeveer 200 m²): 5 m is dan te grof.
  In de steekproef 5 van de 125. Noodoplossing: meet over een schijf van 25 m rond het middelpunt
  en label de uitkomst als *omgeving*, niet als *perceel*.
- **Het perceel is het object niet** — appartementen, en alles wat `summary.perceel_is_het_object`
  al afkeurt. Geen toeslag, want je meet het verkeerde stuk grond.
- **Geen perceelgrens en geen coördinaat.** Klasse blijft ONBEKEND, toeslag € 0, en dat moet in het
  dossier staan — precies zoals `earthworks` het nu al doet.

---

## 9. Grenzen van wat hier staat

- **Het MDT is de grond, niet het gebouw.** Bij een bestaand huis meet je het terrein zoals het na
  eerdere terrassering ligt. Dat is meestal precies wat je wilt, maar het betekent ook dat een
  perceel "vlak" kan heten terwijl het vlak ís doordat er al een keermuur staat — waarvan de staat
  onbekend is. Perceel 4569629BC5946N in Montañar is daar een voorbeeld van: 64 cellen exact op
  9,00 m, en direct naast de perceelgrens zakt het raster naar 4,3 m.
- **De meting zegt niets over de bodem.** Rots kost heel iets anders dan zand, en op de Montgó-hellingen
  is dat geen detail. Het MDT weet dat niet. [te verifiëren]
- **Niets over bouwrecht.** Een steil perceel kan planologisch onbebouwbaar zijn; dat blijft de
  urbanismelaag (`dh/goolzoom.py`) en uiteindelijk de *informe urbanística*.
- **De 40 cm hoogtefout** maakt de klasse betrouwbaar en het bedrag niet. Gebruik dit nooit om een
  hoeveelheid grondverzet te begroten.
- **De bedragen zijn alleen tegen commerciële bronnen getoetst**, niet tegen een officiële
  prijsbasis (BEDEC/ITeC en IVE zitten achter een abonnement) — zie §7.5.
- **De 15 %-drempel steunt op Spaanse ordenanzas van Canarische gemeenten.** Of Xàbia of de
  Comunitat Valenciana een eigen hellingsdrempel kent, is **ONBEKEND** (type 7). Dat is de
  belangrijkste openstaande verificatie en hoort bij de PGOU/NUT-stukken die ook in N01 aan de orde
  kwamen.
- **§6 is een steekproef** (125 van de 622 percelen, één op vijf); **§6.1 is dat niet** — daar zijn
  alle 340 meetbare focus-objecten geteld. Waar de twee verschillen (30/28/42 tegenover 22/33/45),
  komt dat doordat de focuslijst meer bouwkavels bevat en die liggen gemiddeld steiler.

---

## 10. Bronnen, met controledatum

Alle controles op **25-09-2026**, alle verzoeken met de eigen User-Agent van het project, maximaal
één verzoek per twee seconden per host.

| # | Bron | URL | Hoe gecontroleerd | Type |
|---|---|---|---|---|
| 1 | IGN — WCS Modelos Digitales del Terreno, capabilities | <https://servicios.idee.es/wcs-inspire/mdt?request=GetCapabilities&service=WCS> | HTTP 200, 11.928 bytes; Fees "No se aplican condiciones", AccessConstraints "CC BY 4.0 scne.es" | 2 |
| 2 | IGN — DescribeCoverage `Elevacion25830_5` | zelfde dienst, `request=DescribeCoverage&coverageId=Elevacion25830_5` | HTTP 200; 5 m raster, EPSG:25830, oorsprong −19450 / 4865680 | 2 |
| 3 | IGN — GetCoverage, ASCII-grid | zelfde dienst, `request=GetCoverage&…&format=application/asc` | HTTP 200 op elk van ca. 230 vakken: de drie percelen, een steekproef van 125, een proeftegel van 2 × 2 km en de 68 vakken van §6.1 | 3 |
| 4 | Toets "geen 2 m-WCS" | `…/wcs-inspire/mdt-2m?request=GetCapabilities` | HTTP 200, md5 identiek aan #1 → pad wordt genegeerd | 3 |
| 5 | PNOA-LiDAR, technische specificatie | <https://pnoa.ign.es/web/portal/pnoa-lidar/presentacion> | 1e dekking 0,5 pt/m² en 40 cm RMSE Z; 3e dekking 5 pt/m² en 10 cm | 1 |
| 6 | CNIG Centro de Descargas, hoogtemodellen | <https://centrodedescargas.cnig.es/CentroDescargas/modelos-digitales-elevaciones> | MDT02 2 m, 2e dekking 2015–2021, COG; dekking Alicante niet vermeld | 1 |
| 7 | CNIG, nieuws MDT02 | <https://centrodedescargas.cnig.es/CentroDescargas/novedades?codSerie=MDT02> | alleen "Castilla la Mancha Suroeste"; geen dekkingslijst | 7 |
| 8 | IDEE-catalogus, record van de WCS | <https://www.idee.es/csw-codsi-idee/srv/api/records/spaignwcs_mdt> | "Sin limitaciones al acceso público", "CC BY 4.0 scne.es" | 2 |
| 9 | Goolzoom, API-documentatie (6 pagina's) | <https://www.goolzoom.com/api/documentation/General.aspx> en Cadastre/LandRegistry/Delimitations/StatisticalData/UrbanPlanning | HTTP 200; nul treffers op hoogte-/hellingwoorden; endpointlijst in §3.3 | 1 |
| 10 | Goolzoom, robots.txt | <https://www.goolzoom.com/robots.txt> | alleen `Disallow: /usuario/*` — documentatie mag gelezen worden | 2 |
| 11 | Goolzoom, Engelse API-referentie | <https://apireference.goolzoom.com/> | lege Stoplight-schil zonder inhoud; geen uitsluitsel | 7 |
| 12 | IDEV Generalitat Valenciana, dienstenlijst | <https://idev.gva.es/es/servicios-web> | enige terreinproduct is de reliëf-WMTS `mapabase_isohipsas` | 2 |
| 13 | ICV reliëfdienst, capabilities | <https://terramapas.icv.gva.es/mapabase_isohipsas?request=GetCapabilities&service=WMS&version=1.3.0> | HTTP 200; één laag `01_8bits_01_RGB_05_PNG`, nul queryable lagen | 3 |
| 14 | terrasit.gva.es | <https://terrasit.gva.es> | geen verbinding (HTTP 000), twee pogingen | 7 |
| 15 | Catastro INSPIRE wfsCP, grens in EPSG:25830 | `https://ovc.catastro.meh.es/INSPIRE/wfsCP.aspx?…&refcat=5246308BC5954N&srsname=EPSG::25830` | HTTP 200, 87 punten; gebruikt om de eigen coördinaatomzetting te controleren | 2 |
| 16 | OpenTopoData, EU-DEM 25 m | <https://api.opentopodata.org/v1/eudem25m> | HTTP 200 op drie punten; 2,5–4 m hoger dan MDT05 | 3 |
| 17 | Hoogte Montgó (753 m) | <https://en.javea.com/el-paraje-del-montgo-uno-de-los-mejores-sitios-para-hacer-senderismo/ruta-montgo-2/> · <https://parquesnaturales.gva.es/es/web/pn-el-montgo/ruta-verde-claro-descripcion> | gebruikt als onafhankelijke controle; MDT25 geeft 752,0 m | 1 |
| 18 | FAO, Guidelines for Soil Description (4e ed. 2006) — hellingsklassen | <https://www.fao.org/4/a0541e/a0541e.pdf> | strongly sloping 10–15 %, moderately steep 15–30 %; via zoekmachine-samenvatting, PDF niet woordelijk gelezen | 2/7 |
| 19 | USDA/NRCS Soil Survey Manual, hoofdstuk 8 — hellingsklassen | <https://www.nrcs.usda.gov/sites/default/files/2022-09/SSM-ch8.pdf> | moderately steep 12–20 %, steep 20–30 %; idem via samenvatting | 2/7 |
| 20 | FAO-klassen in Spaanse weergave (Univ. Granada) | <http://edafologia.ugr.es/programas_suelos/practgen/factform5/media/descpend.htm> | inclinado 6–13 %, moderadamente escarpado 13–25 % | 2 |
| 21 | CTE DB-SUA 1 §4, hellingen van rampas | <https://www.codigotecnico.org/pdf/Documentos/SUA/DBSUA.pdf> · weergave <https://www.verificacioncte.es/blog/rampas-accesibilidad> | boven 4 % geldt een vlak als rampa; toegankelijk max 6–10 %, niet-toegankelijk max 12 % | 2/1 |
| 22 | Ordenanza de edificación Agüimes — escalonamiento boven 15 % | <https://aguimes.es/transparencia-11-ordenanza-edificacion-04-05-21/> | getrapt bouwen verplicht boven 15 %; terras max 3 m van het oorspronkelijke maaiveld. Canarische gemeente, niet Valenciaans | 2/7 |
| 23 | Ordenanza de edificación Santa Cruz de Tenerife | <https://www.urbanismosantacruz.es/sites/default/files/ordenanzas/Edificacion/22-12-21_orden_edif.pdf> | apart regime ≤15 % en >15 %, met band 15–35 % | 2/7 |
| 24 | COSTA HOUSES (makelaar Jávea) — kavelkeuze Costa Blanca | <https://www.costa-houses.com/en/blog/how-to-choose-solar-luxury-villa-costa-blanca/> | "Ideal slope: 0–15 %"; 15–30 % alleen bij compenserend uitzicht; oprit ≤12 %. Commerciële bron, 18-09-2025 | 1 |
| 25 | Gestland Grup — kostenbanden bouwrijp maken | <https://gestland-grup.com/articulos/cuanto-cuesta-construir-casa-teniendo-terreno/> | € 1.500–6.000 / € 8.000–25.000 (helling 8–15 %) / € 25.000–60.000. Commerciële bron, 20-11-2025 | 1 |
| 26 | CYPE Generador de precios — eenheidsprijzen grondwerk en keermuren | <https://generadordeprecios.info/> (posten ADD010, ADE002, GTB020, UNM020, CCE020) | € 2,12 tot € 164,86 per m³, zie §7.5 | 1 |
| 27 | Urbimed (Dénia) — verborgen kosten villabouw Costa Blanca | <https://www.urbimed.com/en/blog/hidden-costs-when-building-a-luxury-villa-on-the-costa-blanca/> | steile hellingen en hard rots met blasting zijn hier gangbaar; geen percentages | 1 |
| 28 | ITeC BEDEC en IVE — officiële prijsbases | <https://en.itec.cat/services/bedec/> · <https://www.five.es/> | **niet geraadpleegd**: abonnement vereist | 7 |

**robots.txt gecontroleerd** voor elke host die geautomatiseerd benaderd is: `www.ign.es` (404),
`centrodedescargas.cnig.es` (404), `api-features.idee.es` (404), `geocataleg.gva.es` (404),
`visor.gva.es` (404), `www.goolzoom.com` (alleen `/usuario/*` verboden). Een 404 op robots.txt
betekent: geen beperking opgelegd. `servicios.idee.es` gaf geen robots.txt (verbinding geweigerd op
dat pad) — het is een OGC-dienst, geen website, en het capabilities-document zegt zelf dat er geen
gebruiksvoorwaarden gelden.

**Bronvermelding die wij moeten voeren als dit in een rapport voor derden komt:** de licentie is
CC BY 4.0 met attributie "scne.es" (Sistema Cartográfico Nacional / PNOA-LiDAR, Instituto
Geográfico Nacional).

---

## 11. Openstaand

| Wie | Wat |
|---|---|
| S | `dh/helling.py` + `dh/enrich_helling.py` bouwen volgens §8, tegelgewijs, en `slope` vullen in de haalbaarheid |
| S | Hellingklasse tonen in het dossier en op de kaartjes, met de vier getallen (hoogteverschil, helling, richting, aantal cellen) |
| S | De hellingsdrempel in de Jáveaanse PGOU/NUT opzoeken, plus een eventuele maximale keermuurhoogte — nu **ONBEKEND**, en het is de enige grond waarop de 15 %-grens hier lokaal zou kunnen afwijken |
| J | Eén perceel noemen waarvan je het werkelijke grondwerk kent, om 8 % en 15 % aan te ijken (§7.5) |
| J | Optioneel: wil je 2 m in plaats van 5 m, dan moet iemand het MDT02-blad over Jávea handmatig downloaden (§3.2) |

**Afgevallen als openstaand punt:** de toets van € 15.000 en € 50.000 tegen een kostenbron is
gedaan (§7.5). Wat nog ontbreekt is een toets tegen een **officiële** prijsbasis; BEDEC en IVE zitten
achter een abonnement, dus dat lukt niet zonder dat Jan daar toegang voor regelt.

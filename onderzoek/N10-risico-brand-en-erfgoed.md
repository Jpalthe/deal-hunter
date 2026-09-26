# N10 — Bosbrandgevoelig gebied en erfgoedbescherming per perceel: wat kunnen wij automatisch vaststellen

Onderzoek voor TREE Deal Hunter · opgesteld en getoetst **26-09-2026** · werkgebied Jávea/Xàbia ·
elk HTTP-verzoek in dit rapport is op die datum zelf vanaf de Mac mini uitgevoerd, met hoogstens
1 verzoek per 2 seconden per host.

**Bewijstypen (masterprompt §5):** 1 door aanbieder vermeld · 2 in een officiële bron aangetroffen ·
3 door ons rechtstreeks vastgesteld · 4 AI-gevolgtrekking · 5 berekening · 6 professional ·
7 onbekend of tegenstrijdig.

Vervolg op N03 (risicokaarten, 18-09-2026). Waar N03 en dit rapport verschillen, geldt dit rapport:
N03 is op één testpunt getoetst, dit op drie echte percelen uit onze eigen database.

---

## Conclusie in tien regels

1. **Ja voor brand, en preciezer dan gedacht.** De juiste laag is niet de brandinterface maar de
   **Zona de Influencia Forestal (ZIF) van 500 m** in de ArcGIS-dienst `prevencion_de_incendios` van
   het ICV. Die laag is per perceelvlak te bevragen en geeft een hard ja/nee.
2. De ZIF is ook de **wettelijke reikwijdte**: disposición adicional séptima van de TRLOTUP noemt
   letterlijk "en terrenos forestales y en la zona de influencia forestal, definida por el artículo 57
   de la Ley 3/1993". Wie daarin ligt, is *sujeto obligado* voor bijlage XI (bewijstype 2).
3. Van de drie proefpercelen ligt er **één in de ZIF 500 m**: `0481122BC5907N` (Villa El Garroferal,
   Penyaparda). De andere twee niet. Onafhankelijk nagemeten met de bosgrondlaag: 312 m, 913 m en
   999 m tot de dichtstbijzijnde bosgrond — precies passend bij de ZIF-uitkomst.
4. **De brandinterfacekaart is onbruikbaar per perceel.** Ik heb de celgrootte gemeten: **1.000 m**.
   Perceel 2 krijgt daardoor "4 - Alta" terwijl er 913 m geen bosgrond ligt, en perceel 3 krijgt
   "1 - Sin interfaz" terwijl het er 999 m vandaan ligt. Niet gebruiken.
5. **De vrije strook is rekenwerk, geen kaartlaag.** Minimaal 30 m vanaf de buitenrand van het
   gebouw, **minimaal 50 m zodra de helling boven de 30 % komt**, halvering mogelijk met een muur van
   ≥ 1 m. Onderhoud elke 2 jaar (maaien) en 4 jaar (hele strook), eigenaar verantwoordelijk. Letterlijk
   nagelezen op boe.es op 26-09-2026 (bewijstype 2).
6. **De klok loopt alleen in Xàbia.** De gemeentelijke interfacekaart is in Xàbia vastgesteld op
   28-05-2026 → termijn van zes maanden loopt tot ± **28-11-2026**. Benitachell en Teulada staan op
   *Pendiente*: daar is de verplichting nog niet in werking. Benissa, Dénia, Calp en Gata zijn al
   vastgesteld (data in §3.4).
7. **Ja voor gebouwd erfgoed, nee voor archeologie.** BIC, BRL en de beschermingszones zijn gratis en
   automatisch op te vragen. Archeologische vindplaatsen niet: `yacimientos.edu.gva.es` stuurt door
   naar GVLogin en `cultura.gva.es` verbiedt AI-agents in robots.txt. Blijft een handmatige stap.
8. Geen van de drie percelen heeft een BIC, BRL, *entorno de protección* of *delimitación* op zich.
   Dichtstbijzijnde: 722 m (BRL Ermita del Popul) bij perceel 1, 962 m en 1.156 m bij perceel 2,
   niets binnen 1,5 km bij perceel 3.
9. **Montgó is volledig op te halen**: parkgrens, PORN-gebied én de zonering daarbinnen, met de
   wettelijke grondslag in de laag zelf (Decreto 180/2002). Perceel 1 ligt **binnen het PORN-gebied**,
   in de zone *Áreas urbanas y urbanizables*, 307 m van de parkgrens en 230 m van de ZEPA.
10. **Vier stille valkuilen gevonden** in de erfgoeddiensten, waarvan drie een naïef script laten
    concluderen "hier ligt niets". Ze staan met bewijs in §4.4. Eén ervan zit in N03 nog fout.

---

## 1. Wat er is getoetst

### 1.1 De drie percelen

Gegevens uit `data/dealhunter.sqlite` (tabellen `parcels` en `listings`), coördinaten omgerekend naar
EPSG:25830 met `dh/hoogte.naar_utm30`.

| | Perceel 1 | Perceel 2 | Perceel 3 |
|---|---|---|---|
| Kadastrale referentie | `0481122BC5907N` | `5246308BC5954N` | `6442010BC5964S` |
| listing_id | 47 | 58 | 638 |
| Advertentie | Villa El Garroferal | Land Adsubia | Terreno Calle de la Orquídea |
| Adres (Catastro) | CL Penyaparda Prolg. 3 | CL Jaume Huguet 6 | PD Cam Cap Martí 317 |
| Perceel / bebouwd | 1.622 / 0 m² | 1.024 / 275 m² | 697 / 251 m² |
| Vraagprijs | € 2.350.000 | € 850.000 | € 289.000 |
| Zwaartepunt EPSG:25830 | 771518,07 / 4298560,03 | 776554,39 / 4295450,26 | 777589,32 / 4295058,72 |
| Helling gem. / p90 (N08) | 13,8 % / 17,1 % | 6,0 % / 8,8 % | 18,2 % / 28,2 % |

### 1.2 robots.txt, vóór elk verzoek gecontroleerd (bewijstype 3)

| Host | robots.txt op 26-09-2026 | Gebruikt? |
|---|---|---|
| `terramapas.icv.gva.es` | HTTP 404 — geen robots.txt | **ja** |
| `carto.icv.gva.es` | HTTP 404 — geen robots.txt | **ja** |
| `www.idee.es` | `User-Agent: *` / `Disallow:` (alles vrij) | **ja** |
| `www.boe.es` | geen AI-blok; `/buscar/act.php` in het Spaans is vrij | **ja** |
| `servicios.idee.es` | verbinding wordt verbroken op `/robots.txt`, via http én https | nee — niet nodig |
| `idev.gva.es` | blok met `ClaudeBot`, `Claude-User`, `Claude-Web`, `Claude-SearchBot`, `anthropic-ai` → `Disallow: /` | **nee, verboden** |
| `cultura.gva.es` | zelfde AI-blok → `Disallow: /` | **nee, verboden** |
| `mediambient.gva.es` | zelfde AI-blok → `Disallow: /` (bevestigd) | **nee, verboden** |
| `terrasit.gva.es` | geen A-record; `www.terrasit.gva.es` = 158.42.255.99 maar tweemaal ConnectTimeout | nee, onbereikbaar |
| `yacimientos.edu.gva.es` | `/robots.txt` geeft een foutpagina; de homepage stuurt door naar `gvlogin.gva.es` | nee, inlog vereist |
| `dogv.gva.es` | geen AI-blok, wel een lange lijst losse pdf's | niet nodig |
| `descargas.icv.gva.es` | Drupal-standaard, niets relevants geblokkeerd | niet gebruikt |
| `visor.gva.es` | HTTP 404 — geen robots.txt | niet gebruikt |

**Belangrijk:** de opdracht noemde alleen `mediambient.gva.es` als verboden. Er zijn er **drie**:
`mediambient.gva.es`, `cultura.gva.es` en `idev.gva.es`. Dat betekent ook dat de `ficha`-links naar
`cultura.gva.es` die in de erfgoedlagen staan, wél in het dossier mogen als link voor Jan, maar door
ons **niet automatisch opgehaald** mogen worden.

De twee diensten die wij gebruiken — `terramapas.icv.gva.es` en `carto.icv.gva.es` — staan niet op
`mediambient.gva.es` en hebben geen robots.txt. De WMS/WFS-capabilities van beide melden zelf
`<Fees>No se aplican condiciones</Fees>` en `<AccessConstraints>CC BY 4.0 Generalitat</AccessConstraints>`
(bewijstype 2, in de dienst zelf).

---

## 2. Bosbrandgevoelig gebied

### 2.1 Bosgrond zelf — PATFOR, WMS én WFS

| | |
|---|---|
| Dienst | `https://terramapas.icv.gva.es/0506_PATFOR` |
| Protocollen | WMS 1.3.0 (GetFeatureInfo) en **WFS 2.0.0** (GetFeature, o.a. `application/json; subtype=geojson`) |
| Laag / feature type | `SF.Forestal` resp. `ms:SF.Forestal` |
| Gratis / toegestaan | ja — Fees "No se aplican condiciones", CC BY 4.0 Generalitat |
| Formaat | text/plain, geojson, gml, csv, gpkg, shp |

Puntbevraging (WMS) gaf op **alle drie de percelen leeg**: geen bosgrond op het perceel. Dat is het
antwoord op "ligt het *in*". Voor "ligt het *naast*" is de puntbevraging waardeloos; daarvoor de WFS.

Werkelijk uitgevoerde WFS-aanroep (perceel 1, venster van 500 m rond de perceelgrens):

```
https://terramapas.icv.gva.es/0506_PATFOR?SERVICE=WFS&VERSION=2.0.0&REQUEST=GetFeature
  &TYPENAMES=ms:SF.Forestal&SRSNAME=EPSG:25830
  &BBOX=770995.36,4298041.46,772040.91,4299101.48,EPSG:25830
  &COUNT=500&OUTPUTFORMAT=application/json;%20subtype=geojson
```

Antwoord: 1 vlak, 351.916 bytes, `{"forestal":"FORESTAL","compatible":"1","prov":"ALICANTE",
"shape_Area":"19348960.93"}`. Afstand van de perceelgrens tot dat vlak, zelf berekend uit de
geometrie: **312,5 m** (bewijstype 5 op een bron van bewijstype 3).

| Perceel | Venster | Bosvlakken gevonden | Kortste afstand perceelgrens → bosgrond |
|---|---|---|---|
| 1 `0481122BC5907N` | 500 m | 1 | **312,5 m** |
| 2 `5246308BC5954N` | 500 m → 0, daarna 2.000 m | 3 | **912,9 m** |
| 3 `6442010BC5964S` | 500 m → 0, daarna 2.000 m | 11 | **999,3 m** |

### 2.2 De laag die het écht beslist: ZIF 500 m

| | |
|---|---|
| Dienst | `https://carto.icv.gva.es/arcgis/rest/services/tm_medio_ambiente/prevencion_de_incendios/MapServer` |
| Lagen | **90** = ZIF 500 m, *Detalle* · **100** = ZIF 100 m, *Detalle* (103 en 107 zijn de groepen, 104–106 en 108–110 zijn generalisaties voor uitzoomen) |
| Bevraging | `/{laag}/query` met de **perceelgeometrie** als `esriGeometryPolygon`, `spatialRel=esriSpatialRelIntersects` |
| Gratis / toegestaan | ja — geen sleutel, geen robots.txt; licentie CC BY 4.0 volgens de WMS-variant van dezelfde ICV-diensten |

Werkelijk uitgevoerde aanroep (verkort; de ring is de perceelgrens uit `parcels.geojson`, omgerekend
naar EPSG:25830):

```
POST/GET https://carto.icv.gva.es/arcgis/rest/services/tm_medio_ambiente/prevencion_de_incendios/MapServer/90/query
  geometry={"rings":[[[771495.36,4298541.46], …]],"spatialReference":{"wkid":25830}}
  geometryType=esriGeometryPolygon&inSR=25830&spatialRel=esriSpatialRelIntersects
  &outFields=*&returnGeometry=false&f=json
```

| Perceel | laag 90 (ZIF 500 m) | laag 100 (ZIF 100 m) |
|---|---|---|
| 1 | **1 treffer** — `{"OBJECTID":19671,"FORESTAL":"ZIF 500m"}` | 0 |
| 2 | 0 | 0 |
| 3 | 0 | 0 |

**Controle dat "0" ook echt "0" betekent:** binnen 2 km van perceel 1 heeft laag 100 wél 3 vlakken.
De laag is daar dus gevuld; de nul is een echte nul (bewijstype 3).

Let op twee dingen bij de bouw:
- laag 90 heeft `minScale = 53000`. Bij `identify` met een ruime `mapExtent` slaat ArcGIS de laag
  stilzwijgend over. **`query` kent geen schaalgrens** — gebruik daarom altijd `query`, nooit `identify`.
- de lagen 104/105/106 geven hetzelfde vlak maar vereenvoudigd (omtrek 18,6 / 23,9 / 27,8 miljoen m
  tegen 28,4 miljoen m bij laag 90). Voor een perceeluitspraak alleen laag 90 en 100 gebruiken.

### 2.3 Wat je níet moet gebruiken: de brandinterfacekaart

`Regulacion.Incendios.Urbano` in `0506_PATFOR` geeft een interfaceklasse, maar het is een raster. Het
antwoord bevat het middelpunt van de cel, en ik heb de celmaat gemeten door in stappen van 250 m op
te schuiven:

| Vraagpunt (x) | Celmidden | Klasse |
|---|---|---|
| 776.659,03 | 776409,03 / 4295311,1 | 4 - Alta |
| 776.909,03 | 776409,03 / 4295311,1 | 4 - Alta |
| 777.159,03 | 777409,03 / 4295311,1 | 1 - Sin interfaz |
| 777.409,03 | 777409,03 / 4295311,1 | 1 - Sin interfaz |

De celgrens ligt tussen 776.909 en 777.159, de celmiddens liggen 1.000 m uit elkaar: **cellen van
1 bij 1 km** (bewijstype 3; N03 schatte nog ~500 m). Uitkomst op de drie percelen, met het
celmiddelpunt erbij:

| Perceel | Klasse | Celmidden ligt van het perceel af | Bosgrond werkelijk op |
|---|---|---|---|
| 1 | `2 - Casos aislados` | 272 m | 312 m |
| 2 | `4 - Alta` | 201 m | 913 m |
| 3 | `1 - Sin interfaz` | 310 m | 999 m |

Perceel 2 zou op deze laag "hoog risico" heten terwijl er bijna een kilometer geen bos ligt. **Niet
opnemen in het model.** Ook `Regulacion.Incendios.Peligrosidad` helpt niet: perceel 1 krijgt
`clase = Moderado` op een vlak van 4,4 ha, maar percelen 2 en 3 vallen in een vulvlak van 28 km² met
`clase = ' '`. `Regulacion.Incendios.Recurrencia` en `Recomendaciones.Incendio` gaven op alle drie
niets.

### 2.4 Wie is verplicht, en vanaf wanneer

Laag **114** (*Municipios interfaz*) geeft per gemeente de stand van de kaart die de TRLOTUP eist.
Aanroep: `/114/query?where=municipio LIKE '%…%'&outFields=cod_ine,municipio,estado,fechapleno&f=json`.

| INE | Gemeente | Stand | Raadsbesluit | Termijn van 6 maanden loopt tot |
|---|---|---|---|---|
| 03082 | **Jávea/Xàbia** | Aprobado | **28-05-2026** | **± 28-11-2026** |
| 03042 | **Benitachell** | **Pendiente** | — | nog niet begonnen |
| 03128 | **Teulada** (Moraira) | **Pendiente** | — | nog niet begonnen |
| 03041 | Benissa | Aprobado | 30-07-2024 | verstreken |
| 03063 | Dénia | Aprobado | 29-02-2024 | verstreken |
| 03047 | Calp | Aprobado | 31-01-2024 | verstreken |
| 03071 | Gata de Gorgos | Aprobado | 19-12-2024 | verstreken |
| 03101 | Pedreguer | En tramitación | — | nog niet begonnen |

De wettekst, letterlijk nagelezen op `https://www.boe.es/buscar/act.php?id=DOGV-r-2021-90283`
(TRLOTUP geconsolideerd, 26-09-2026, bewijstype 2):

- **Disposición adicional séptima, punt 1:** gemeenten met bosgrond moeten elke urbanisatie, kern,
  gebouw of installatie in kaart brengen die risico loopt "por estar situadas en terrenos forestales
  o en zona de influencia forestal, definida por el artículo 57 de la Ley 3/1993". De gemeenteraad
  stelt die kaart vast.
- **punt 3:** de eigenaren van die panden zijn *sujetos obligados* voor bijlage XI; is er een VvE of
  *entidad urbanística colaboradora*, dan is die het.
- **punt 7 en 8:** gedwongen erfdienstbaarheid om het werk op andermans grond uit te voeren, met
  schadeloosstelling ten laste van de verplichte partij.
- **punt 10:** zes maanden vanaf de gemeentelijke vaststelling.

### 2.5 Hoe breed is de strook

Geen kaartlaag. Bijlage XI, punt 1 (letterlijk gelezen, bewijstype 2):

- **Algemeen:** *faja perimetral de protección* van **minimaal 30 m**, gemeten vanaf de buitenrand van
  het gebouw of het samenstel van gebouwen.
- **1.a — tussen stedelijk gebied en bosvegetatie:** breedte van een *área cortafuegos de orden dos*
  volgens het Plan de Selvicultura Preventiva, "aplicando una corrección en función de la pendiente".
  Minimaal **25 m plus een weg van 5 m**; die weg mag vervallen als aanleg onmogelijk is, mits er een
  afgeschraapte strook van dezelfde breedte komt. En: "se ampliará en función de la pendiente,
  alcanzando, como mínimo, los **50 metros cuando la pendiente sea superior al 30 %**".
- **1.c — losstaande gebouwen op of grenzend aan bosgrond:** verdedigingszone van **ten minste 30 m**,
  eveneens **ten minste 50 m boven 30 % helling**. Verkleining tot de helft is mogelijk bij
  compenserende voorzieningen, bijvoorbeeld een muur van ten minste 1 m hoog.
- **Onderhoud:** de maaistrook elke twee jaar, de hele strook elke vier jaar. De eigenaar is
  verantwoordelijk.

**Wat dat voor onze drie betekent** (bewijstype 5, met de hellingen uit N08):

| Perceel | In ZIF 500 m | Grenst aan bosgrond | Helling p90 | Strook volgens bijlage XI |
|---|---|---|---|---|
| 1 | **ja** | nee (312 m) | 17,1 % | 30 m zodra de gemeentelijke kaart het perceel aanwijst; niet 50 m, helling ruim onder 30 % |
| 2 | nee | nee (913 m) | 8,8 % | geen |
| 3 | nee | nee (999 m) | 28,2 % | geen — maar bij een perceel dat wél in de ZIF ligt zou 28,2 % vlak onder de 50 m-drempel zitten |

Bijlage XI 1.c spreekt van "op of grenzend aan" bosgrond; DA 7 hangt de verplichting op aan de ZIF.
Dat is geen tegenspraak maar een volgorde: de ZIF bepaalt wie op de gemeentelijke kaart komt, de
gemeentelijke kaart bepaalt of jouw pand is aangewezen, en pas dan zegt bijlage XI hoe breed. **De
gemeentelijke kaart van Xàbia zelf is niet als kaartlaag gevonden** — laag 114 geeft alleen de
gemeente, de stand en de datum, met een sleutel `acplenario = "03082_Xàbia"` waarvan de basis-URL
onbekend is. ONBEKEND; loopt via Urbanisme van het Ajuntament.

### 2.6 Overige brandlagen in dezelfde dienst

Alle drie de percelen: **nul treffers** op laag 112 (*Instalaciones en riesgo*), 113 (*Áreas
susceptibles de actuación*) en 127 (*Fajas Perimetrales* uit het PLPIF). Dat is een echte nul: binnen
5 km van perceel 1 heeft laag 112 er 874, laag 113 er 205 en laag 127 er 97. Binnen 500 m van
perceel 1 nul. Laag 112 inventariseert bestaande bebouwing, dus een leeg perceel staat er per definitie
niet in — bouw je er, dan kom je erin (bewijstype 4).

Xàbia heeft een goedgekeurd PLPIF: `estado = Aprobado`, `resolucion = 2020/6092`, 6.894,87 ha.

---

## 3. Montgó: parkgrens en bufferzone

| | |
|---|---|
| Dienst | `https://terramapas.icv.gva.es/0505_PORN` (WMS 1.3.0 + WFS 2.0.0) |
| Lagen | `Montgo.Parque` (het park), `Montgo.PORN` (het PORN-gebied = de ruimere schil), `Montgo.Zonificacion` (de zonering binnen het PORN) |
| Gratis / toegestaan | ja — Fees "No se aplican condiciones", CC BY 4.0 |
| Formaat | text/plain, geojson, gml, csv, gpkg |

De wettelijke grondslag zit in de laag zelf. Puntbevraging op perceel 1 gaf:

```
Layer 'Montgo.PORN'
  figura = 'Parque Natural'      nombre = 'El Montgó'
  l_mun  = 'Dénia, Gata de Gorgos, Xàbia / Jávea, Ondara, Pedreguer'
  legislacio = 'Decreto 180/2002, de 5 de noviembre'   n_docv = '4374'   data_publicacio = '2002-11-08'
  leg_link = 'http://www.docv.gva.es/datos/2002/11/08/pdf/2002_12109.pdf'
  area_ha = '7432.85'
Layer 'Montgo.Zonificacion'
  descrip = 'Áreas urbanas y urbanizables'
```

Afstanden, gemeten uit de WFS-geometrie tot de perceelgrens (bewijstype 5 op bewijstype 3):

| Perceel | Montgo.Parque | Montgo.PORN | Montgo.Zonificacion | ZEC | ZEPA |
|---|---|---|---|---|---|
| 1 | **307 m** | **0 m — ligt erin** | 0 m, *Áreas urbanas y urbanizables* | niets binnen 3 km | **230 m** — Montgó–Cap de Sant Antoni |
| 2 | 3.640 m | 2.318 m | 2.318 m, *Conectores ambientales* | 1.855 m — Penya-segats de la Marina | 1.855 m |
| 3 | geen vlak binnen 3 km | 3.316 m | 3.316 m, *Conectores ambientales* | 1.582 m | 1.582 m |

Het park zelf is een aparte laag met een eigen grondslag: `Montgo.Parque` geeft
`nombre = 'Parque Natural de El Montgó'`, `legislacio = 'Decreto 25/1987, de 16 de marzo'`,
DOGV 556 van 30-03-1987 met correctie DOGV 1844 van 14-08-1992, `hect_geo = 2094,07`
(officiële opgave 2.086,36 ha), `site_code = ES521003`.

Dus: **de parkgrens is een laag, en de "bufferzone" bestaat als het PORN-gebied** — 7.432,85 ha
tegen 2.094,07 ha park, ruim drie keer zo groot — met daarbinnen een zonering die per perceel te
lezen is. Voor perceel 1 is het
antwoord genuanceerd en precies wat je wilt weten: het ligt binnen het PORN, maar in de zone die als
stedelijk/verstedelijkbaar is aangemerkt. Wat die zone in het decreet aan voorschriften meebrengt, is
in dit onderzoek niet gelezen — het decreet staat op `docv.gva.es` (die host verbiedt AI-agents niet)
maar is niet opgehaald. **[te verifiëren]**

De natuurlagen in `0701_InfraestructuraVerde` (`IVR.ParquesNaturales`, `IVR.ZEC`, `IVR.ZEPA`) geven
hetzelfde park op exact dezelfde afstand — twee onafhankelijke diensten, zelfde antwoord.

---

## 4. Archeologie en erfgoed

### 4.1 Gebouwd erfgoed: gratis en compleet, maar via drie verschillende ingangen

| Vraag | Dienst | Formaat | Waarom deze |
|---|---|---|---|
| Ligt er een BIC of BRL op/bij het perceel? | `https://terramapas.icv.gva.es/22_IGPCV_wfs` — WFS 2.0.0, `ms:BIC` en `ms:BRL` | geojson, csv, gpkg | de enige WFS waar **beide** puntlagen in zitten |
| Ligt het perceel in een *entorno de protección* of een *delimitación*? | `https://terramapas.icv.gva.es/22_IGPCV` — WFS `ms:BIC.Entornos`, `ms:BIC.Delimitaciones` | geojson | vlakken, werkt goed |
| Kruiscontrole | `https://terramapas.icv.gva.es/0701_InfraestructuraVerde` — `ms:IVR.Cultura.BIC.BIC`, `ms:IVR.Cultura.BRL`, `…BIC.Entornos`, `…BIC.Delimitaciones`, `ms:IVR.Cultura.PiedraSeca` | geojson | gaf exact dezelfde uitkomsten |

Beide diensten melden `Fees: No se aplican condiciones` en `AccessConstraints: CC BY 4.0 Generalitat`.

### 4.2 Het werkelijke antwoord op de drie percelen

Puntbevraging (WMS, `BIC,BIC.Entornos,BIC.Delimitaciones,BRL`): **op alle drie leeg**. Geen van de
percelen is zelf beschermd en geen ligt in een beschermingszone.

WFS binnen 1,5 km rond de perceelgrens, afstanden zelf berekend:

| Perceel | Dichtstbijzijnde BIC | Dichtstbijzijnde BRL | Entorno / delimitación binnen 1,5 km |
|---|---|---|---|
| 1 | niets binnen 1,5 km | **722 m** — Ermita del Popul (*Monumento de interés local*) | geen |
| 2 | **1.156 m** — Casa forta de la Bardissa (*Monumento*); 1.435 m — Torre Capçades | **962 m** — Campo de Aviación del Plà | geen |
| 3 | niets binnen 1,5 km | niets binnen 1,5 km | geen |

**Positieve controle** dat dit geen lege dienst is: dezelfde WFS-aanroep rond de Iglesia de San
Bartolomé (774771 / 4298148) geeft het *entorno* met `codigo = 1697`, en de BRL-laag geeft daar
10 monumenten met echte, onderling verschillende coördinaten (o.a. Casas del Pósito, La Sultana,
Ermita del Pilar y Casa Conejo).

### 4.3 Archeologie: nee, en dat is beleid

- `https://yacimientos.edu.gva.es/` geeft HTTP 200 met een script dat meteen doorstuurt naar
  `https://gvlogin.gva.es/gvlogin/login.xhtml?app=YACIMIENTOS` — **inloggen vereist** (bewijstype 3,
  26-09-2026). Er is geen open raadpleging en dus zeker geen dienst.
- `cultura.gva.es`, waar de beleidstekst en de *fichas* staan, verbiedt AI-agents in robots.txt
  (`Disallow: /` voor ClaudeBot en Claude-User). Wij halen daar niets op.
- In de erfgoeddienst `22_IGPCV` bestaan maar vier bevraagbare lagen: `BIC`, `BIC.Entornos`,
  `BIC.Delimitaciones`, `BRL`. **Geen archeologielaag** (bewijstype 3, GetCapabilities gelezen).
- In `0702_Planeamiento` bestaan zeven lagen (`Planeamiento.Clasificacion`, `…Zonificacion`,
  `…Dotaciones`, `…ElementosSingulares`, `InventarioSuSuz`, `DeclaracionInteresComunitario`,
  `MinimizacionViviendasSNU`). Geen catálogo de bienes protegidos, geen archeologie.
  `Planeamiento.ElementosSingulares` gaf op alle drie de percelen niets.
- De nationale IDEE-catalogus (`https://www.idee.es/csw-inspire-idee/srv/spa/csw`, CSW 2.0.2, vrij te
  bevragen) geeft op `AnyText like '%arqueol%'` 127 records, maar die gaan over Andalusië, Aragón,
  Baskenland en losse onderzoeksprojecten (IDEARQ). **Geen Valenciaanse archeologiedienst.**

Conclusie: archeologie blijft een handmatige stap per serieus dossier. Automatiseren kan niet en mag
niet.

### 4.4 Vier stille valkuilen — met bewijs

Deze vier laten een naïef script ten onrechte "hier ligt niets" concluderen. Alle vier op 26-09-2026
zelf vastgesteld (bewijstype 3).

1. **`ms:BIC` op `22_IGPCV` geeft via WFS altijd een lege verzameling.** Niet alleen bij onze percelen:
   ook met een bbox van 10 × 10 km over heel Xàbia, en zelfs *zonder* bbox, komt er
   `"features": []` terug. Dezelfde laag antwoordt via WMS GetFeatureInfo wél (bij San Bartolomé:
   `codigo = 1697`). Oorzaak is zichtbaar in het antwoord: `Cluster_FeatureCount` — de laag is in
   MapServer geclusterd en dat breekt de WFS. **Gebruik `22_IGPCV_wfs` of `0701_InfraestructuraVerde`
   voor de puntlagen.**
2. **De puntcoördinaten uit WMS zijn clusterposities, geen locaties.** "Caseta de Don Juan Tena" komt
   via WMS op 774957 / 4298297 en via WFS op 774093 / 4298086 — **880 m verschil**. Bij een grof
   uitgezoomde bevraging (bbox 20 km, 11 × 11 beeldpunten) kwamen 144 BRL's terug op één en dezelfde
   coördinaat. Nooit afstanden rekenen met WMS-punten.
3. **`INFO_FORMAT=text/plain` geeft voor `BRL` wél de features maar géén enkel veld** — kaal
   `Feature 486:` en verder niets. Met `INFO_FORMAT=geojson` komt alles mee (denominacion, codigo,
   categoria, ficha). **Altijd geojson vragen bij `22_IGPCV`.**
4. **Twee lagen tegelijk in één geojson-GetFeatureInfo mislukt volledig zodra één van de twee leeg is.**
   `LAYERS=BIC,BRL` geeft dan `msOGRWriteFromQuery(): OGR_DS_CreateLayer failed for layer 'BRL' with
   driver 'GEOJSON'` — een ServiceException, dus je verliest ook de treffer van de andere laag.
   **Eén laag per verzoek bij geojson.**

**Correctie op N03 §8.1.** Dat rapport schreef over de erfgoedlagen in `0701_InfraestructuraVerde`:
"Via WFS is diezelfde laag wel op te halen, maar dat is een omweg zonder reden." Die reden is er wel.
Voor de *vlakken* (entornos, delimitaciones) klopt N03 en werkt `22_IGPCV` prima; voor de *puntlagen*
BIC en BRL is de WFS van `0701` of van `22_IGPCV_wfs` de enige weg die bruikbare coördinaten geeft.

---

## 5. Bronnen die alleen als download bestaan

Kort antwoord: **voor deze twee vragen is er geen bron die alleen als download bestaat.** Alles wat
wij nodig hebben, is als dienst beschikbaar. Wat er niet is, is er helemaal niet:

| Wat | Als dienst? | Als download? | Omvang |
|---|---|---|---|
| Bosgrond, ZIF, PLPIF, brandinterface | ja, WMS + WFS + ArcGIS REST | ja, via dezelfde WFS (`outputformat=gpkg`, `shp`, `csv`) | niet opgehaald; het geojson-antwoord voor één perceelvenster is 352 KB, een leeg antwoord 157 bytes |
| BIC, BRL, entornos, delimitaciones | ja | ja — de IDEE-catalogus noemt `https://terramapas.icv.gva.es/22_IGPCV_wfs?request=GetFeature&service=WFS&version=2.0.0&typename=BRL&outputformat=gpkg` en dezelfde URL met `outputformat=csv` | ONBEKEND, niet opgehaald |
| Montgó park, PORN, zonering | ja | ja, via WFS | ONBEKEND |
| **Archeologische vindplaatsen** | **nee** | **nee** — achter GVLogin | n.v.t. |
| **Gemeentelijke interfacekaart Xàbia (de vlakken zelf)** | **nee** — laag 114 geeft alleen gemeente + stand + datum | ONBEKEND — sleutel `acplenario = "03082_Xàbia"`, basis-URL niet gevonden | ONBEKEND |
| Gemeentelijke catálogo de bienes protegidos van Xàbia | nee | ONBEKEND — loopt via Urbanisme | n.v.t. |

Ter grootte-indicatie van de capabilities die je eenmalig moet lezen: `0506_PATFOR` WMS 238.668 bytes,
`0506_PATFOR` WFS 126.231 bytes, `22_IGPCV` WMS 24.540 bytes, `0505_PORN` WFS 127.767 bytes.

---

## 6. Voorstel: hoe wij dit aanroepen en wat wij bewaren

### 6.1 De aanroepen, per perceel

Volgorde zo gekozen dat de twee hosts afwisselen; met 1 verzoek per 2 seconden per host kost een
perceel ongeveer **15 seconden**.

| # | Host | Aanroep | Levert |
|---|---|---|---|
| 1 | carto | `prevencion_de_incendios/MapServer/90/query`, perceelpolygoon, `spatialRel=esriSpatialRelIntersects` | `zif_500` ja/nee |
| 2 | terramapas | `0506_PATFOR` WFS `ms:SF.Forestal`, bbox = perceel + 600 m, geojson | `bos_afstand_m` (zelf berekend); `bos_op_perceel` als de afstand 0 is |
| 3 | carto | `…/MapServer/100/query`, perceelpolygoon | `zif_100` ja/nee |
| 4 | terramapas | `22_IGPCV_wfs` WFS `ms:BIC`, bbox = perceel + 600 m, geojson | `bic_afstand_m`, `bic_naam` |
| 5 | carto | `…/MapServer/114/query?where=cod_ine='03082'` — **per gemeente cachen, niet per perceel** | `interfaz_kaart_status`, `interfaz_kaart_datum` |
| 6 | terramapas | `22_IGPCV_wfs` WFS `ms:BRL`, zelfde bbox, geojson | `brl_afstand_m`, `brl_naam` |
| 7 | carto | `…/MapServer/112/query` en `113/query`, perceelpolygoon (samen 2 verzoeken) | `instalacion_en_riesgo`, `area_actuacion` |
| 8 | terramapas | `22_IGPCV` WFS `ms:BIC.Entornos` + `ms:BIC.Delimitaciones`, zelfde bbox | `entorno_bic` ja/nee + naam |
| 9 | terramapas | `0505_PORN` WMS GetFeatureInfo op het zwaartepunt, `LAYERS=Montgo.Parque,Montgo.PORN,Montgo.Zonificacion`, `INFO_FORMAT=text/plain` | `porn_montgo` ja/nee, `porn_zone` |
| 10 | terramapas | `0505_PORN` WFS `ms:Montgo.Parque`, bbox = perceel + 3.000 m | `park_afstand_m` |

Vaste regels, alle uit dit onderzoek:
- **`query`, nooit `identify`** bij de ArcGIS-dienst (schaalgrens `minScale`).
- **Eén laag per verzoek** zodra `INFO_FORMAT=geojson` of `OUTPUTFORMAT=…geojson`.
- **Nooit WMS-puntcoördinaten** gebruiken om afstanden te rekenen.
- **`Regulacion.Incendios.Urbano` niet opnemen** (cellen van 1 km).
- Loopt een WFS-venster leeg, dan is het antwoord "niets binnen X m", niet "niets". Sla het venster
  mee op, anders is de nul niet te lezen.
- Bosgrond, ZIF, parkgrenzen en monumenten verschuiven niet van maand tot maand: **één keer meten per
  perceel** en jaarlijks verversen, zoals `enrich_helling` het al doet. Voor 621 percelen met een
  perceelgrens is dat ongeveer **2,5 uur** eenmalig.
- De `ficha`-URL's wijzen naar `cultura.gva.es`; die host verbiedt AI-agents. **Opslaan als link voor
  Jan, nooit zelf ophalen.**

### 6.2 De velden

Nieuwe tabel `risico`, één regel per `listing_id`, in de vorm van de bestaande tabel `urbanism`;
gevuld door een nieuwe `dh/enrich_risico.py` naar het voorbeeld van `dh/enrich_helling.py`.

| Veld | Type | Inhoud |
|---|---|---|
| `listing_id`, `rc` | INTEGER, TEXT | sleutel |
| `bos_op_perceel` | INTEGER | 1 als `SF.Forestal` het perceel raakt |
| `bos_afstand_m` | REAL | kortste afstand perceelgrens → bosgrond, binnen het gebruikte venster |
| `bos_venster_m` | INTEGER | het gebruikte venster (600, anders 2.000) — nodig om een nul te kunnen lezen |
| `zif_500`, `zif_100` | INTEGER | in de forestale invloedszone van 500 resp. 100 m |
| `instalacion_en_riesgo`, `area_actuacion` | INTEGER | lagen 112 en 113 |
| `interfaz_status`, `interfaz_datum` | TEXT | stand en raadsdatum van de gemeentelijke kaart |
| `interfaz_deadline` | TEXT | raadsdatum + 6 maanden (DA 7.10) |
| `strook_m` | REAL | 30, of 50 bij `helling_p90 > 0,30`; NULL als `zif_500` = 0 |
| `strook_grond` | TEXT | "TRLOTUP bijlage XI punt 1.c" |
| `bic_afstand_m`, `bic_naam`, `bic_codigo` | REAL, TEXT, TEXT | dichtstbijzijnde BIC |
| `brl_afstand_m`, `brl_naam`, `brl_codigo` | REAL, TEXT, TEXT | dichtstbijzijnde BRL |
| `entorno_bic` | INTEGER | perceel ligt in een *entorno de protección* of *delimitación* |
| `entorno_naam`, `entorno_ficha` | TEXT | naam en de link naar cultura.gva.es (niet ophalen) |
| `porn_montgo` | INTEGER | binnen het PORN-gebied |
| `porn_zone` | TEXT | zonering, bv. "Áreas urbanas y urbanizables" |
| `park_afstand_m`, `zepa_afstand_m`, `zec_afstand_m` | REAL | afstanden tot park en Natura 2000 |
| `archeologie` | TEXT | vast op `"handmatig"` — er is geen dienst |
| `bron_urls` | TEXT (json) | per veld de exacte aanroep-URL |
| `fetched_at`, `error` | TEXT | zoals bij `urbanism` |

### 6.3 Wat het model ermee doet

- `zif_500 = 1` **én** `interfaz_status = Aprobado` → kostenregel voor de vrije strook en de
  tweejaarlijkse onderhoudsplicht, plus een datum in het dossier. Hoeveel die strook kost, is in dit
  onderzoek niet uitgezocht: **ONBEKEND**, zie de vragen hieronder.
- `entorno_bic = 1` → geen kostenregel maar een doorlooptijdregel: extra toets bij elke verbouwing.
- `porn_montgo = 1` → markeren, niet automatisch afwaarderen: perceel 1 ligt erin maar in de
  stedelijke zone.
- `archeologie` blijft een handmatig vinkje in het dossier voor elk object dat serieus wordt.

---

## 7. Wat er niet is uitgezocht

| Punt | Stand |
|---|---|
| Artikel 57 van Ley 3/1993 (de wettelijke definitie van de ZIF, en of dat inderdaad 500 m is) | **[te verifiëren]** — de laag heet "ZIF 500 m" en de TRLOTUP verwijst naar dat artikel, maar de wettekst zelf is niet gelezen |
| Decreto 180/2002 (PORN Montgó): wat de zone *Áreas urbanas y urbanizables* aan voorschriften meebrengt | **[te verifiëren]** — pdf staat op docv.gva.es, niet opgehaald |
| Kosten van aanleg en onderhoud van de faja perimetral | **ONBEKEND** |
| De gemeentelijke interfacekaart van Xàbia als geometrie | **ONBEKEND** — loopt via Urbanisme |
| Gemeentelijke catálogo de bienes y espacios protegidos van Xàbia | **ONBEKEND** — N03 vond CartOXàbia niet, en dat is hier niet opnieuw geprobeerd |
| Benitachell en Teulada: eigen brandregels naast de TRLOTUP | niet onderzocht |
| Omvang van de bulkdownloads (gpkg) | **ONBEKEND** — bewust niet opgehaald |

---

## 8. Vragen voor Jan

Jan vroeg om zoveel mogelijk vragen. Hieronder alle open keuzes; de eerste drie zijn de enige die de
bouw nu ophouden.

**Nu nodig**

1. Nemen we de vrije strook als **kostenregel** op in de rekensom, en zo ja met welk bedrag per m²
   aanleg en per keer onderhoud? Zonder jouw getal rekent het model niets, net als bij de helling.
2. Moet een perceel **binnen het PORN-gebied van Montgó** automatisch een lagere kansklasse krijgen,
   of alleen een waarschuwing in het dossier? Perceel 1 (Villa El Garroferal, € 2,35 mln) is precies
   zo'n geval: binnen het PORN, maar in de stedelijke zone.
3. Vraag jij bij het Ajuntament de **gemeentelijke interfacekaart** op (vastgesteld 28-05-2026)? Dat
   is het enige document dat definitief zegt of een pand is aangewezen. ⏸️ ACTIE VOOR JAN.

**Daarna, wanneer het uitkomt**

4. Willen we voor archeologie de **volledige raadpleging** aanvragen bij de Conselleria (toegang tot
   `yacimientos.edu.gva.es`), of blijft het per dossier een handmatige vraag aan de gestor?
5. Moet `bos_afstand_m` ook in de **melding bij sterke kansen** meewegen, of alleen in het dossier?
6. Hoe ver moet "naast bosgebied" reiken in onze eigen beoordeling: houden we de wettelijke 500 m
   aan, of wil je ook percelen tussen 500 m en 1 km zien gemarkeerd?
7. Trekken we dit ook over Benitachell en Teulada, waar de gemeentelijke kaart nog *Pendiente* is?
   Daar is de verplichting nog niet in werking, maar ze komt er wel — koop je nu, dan erf je hem.
8. Mag ik `dh/enrich_risico.py` **meteen bouwen en één keer over alle 621 percelen draaien**
   (ongeveer 2,5 uur, geen installatie, alleen gratis diensten), of wil je eerst de uitkomst op tien
   percelen zien?
9. Moeten de nieuwe velden ook op de **telefoonpagina** (`/m`) en in het dagrapport, of alleen in het
   dossier en op het dashboard?
10. Wil je dat ik de gevonden fout in N03 §8.1 daar **corrigeer met een banner**, zoals bij de
    tegenspraakrapporten, of laten we N03 staan en geldt N10 als de nieuwere?

---

## Bronnenlijst — alles wat op 26-09-2026 werkelijk is aangeroepen

1. `https://terramapas.icv.gva.es/robots.txt` — 404
2. `https://carto.icv.gva.es/robots.txt` — 404
3. `https://idev.gva.es/robots.txt` — AI-agents verboden
4. `https://cultura.gva.es/robots.txt` — AI-agents verboden
5. `https://mediambient.gva.es/robots.txt` — AI-agents verboden (bevestigd)
6. `https://www.idee.es/robots.txt` — alles vrij
7. `https://www.boe.es/robots.txt` · `https://dogv.gva.es/robots.txt` · `https://descargas.icv.gva.es/robots.txt` · `https://visor.gva.es/robots.txt`
8. `https://www.terrasit.gva.es/` en `https://www.terrasit.gva.es/robots.txt` — ConnectTimeout, tweemaal
9. `https://terramapas.icv.gva.es/0506_PATFOR` — WMS GetCapabilities, WFS GetCapabilities, GetFeatureInfo op `SF.Forestal`, `Forestal.Forestal`, `Forestal.Estrategico`, `Planeamiento.TFE`, `Regulacion.Incendios.Urbano`, `Regulacion.Incendios.Peligrosidad`, `Regulacion.Incendios.Recurrencia`, `Recomendaciones.Incendio`; WFS GetFeature op `ms:SF.Forestal`
10. `https://carto.icv.gva.es/arcgis/rest/services/tm_medio_ambiente/prevencion_de_incendios/MapServer` — laaglijst, `identify`, laaginfo 90/100/112/113/114, `query` op 90, 100, 112, 113, 114, 127, 143
11. `https://terramapas.icv.gva.es/22_IGPCV` — WMS GetCapabilities, WFS GetCapabilities, GetFeatureInfo op `BIC`, `BIC.Entornos`, `BIC.Delimitaciones`, `BRL` (text/plain én geojson), WFS GetFeature op `ms:BIC`, `ms:BIC.Entornos`, `ms:BIC.Delimitaciones`
12. `https://terramapas.icv.gva.es/22_IGPCV_wfs` — WFS GetCapabilities, GetFeature op `ms:BIC` en `ms:BRL`
13. `https://terramapas.icv.gva.es/0701_InfraestructuraVerde` — WFS GetCapabilities, GetFeature op `ms:IVR.Cultura.BIC.BIC`, `ms:IVR.Cultura.BRL`, `ms:IVR.Cultura.BIC.Entornos`, `ms:IVR.Cultura.BIC.Delimitaciones`, `ms:IVR.Cultura.PiedraSeca`, `ms:IVM.CulturalPol`, `ms:IVM.CulturalPun`, `ms:IVR.ParquesNaturales`, `ms:IVR.ZEC`, `ms:IVR.ZEPA`
14. `https://terramapas.icv.gva.es/0505_PORN` — WFS GetCapabilities, GetFeatureInfo en GetFeature op `Montgo.Parque`, `Montgo.PORN`, `Montgo.Zonificacion`
15. `https://terramapas.icv.gva.es/0702_Planeamiento` — WMS GetCapabilities, GetFeatureInfo en WFS op `Planeamiento.ElementosSingulares`
16. `https://www.idee.es/csw-inspire-idee/srv/spa/csw` — CSW GetCapabilities en GetRecords op "arqueol", "incendios forestales", "Patrimonio Cultural Valenciano", "Bienes de Relevancia Local"
17. `https://www.boe.es/buscar/act.php?id=DOGV-r-2021-90283` — TRLOTUP geconsolideerd: disposición adicional séptima en bijlage XI punt 1
18. `https://yacimientos.edu.gva.es/` — doorverwijzing naar GVLogin

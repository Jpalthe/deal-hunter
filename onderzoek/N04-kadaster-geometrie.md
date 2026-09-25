# N04 — Van kadastrale referentie naar oppervlakte, geometrie en gebouwen

Onderzoeksrapport Deal Hunter · opgesteld 18-09-2026 · alle tests die dag zelf uitgevoerd

**Vraag van Jan:** wij halen nu alleen de kadastrale referentie op bij een punt. Wat kunnen we
nog meer krijgen, en hoe?

**Bewijstype per bewering:** 1 = zelf getest of opgehaald · 2 = officiële wettekst of
planvoorschrift · 3 = officiële kaart of database · 4 = officiële publicatie van een overheid ·
5 = eigen afleiding of berekening · 6 = bericht van een marktpartij · 7 = onbekend of onbevestigd.

Alle Spaanse vaktermen krijgen bij eerste gebruik een korte uitleg. Bedragen en oppervlakten
zoals de bron ze geeft.

---

## 1. Het korte antwoord

Alle vijf de vragen zijn te beantwoorden met gratis diensten, zonder sleutel, zonder registratie
en zonder in te loggen. Er is geen enkele betaalde laag nodig.

| # | Vraag | Antwoord | Dienst | Bewijs |
|---|---|---|---|---|
| 1 | Officiële perceeloppervlakte in m² | Ja, twee onafhankelijke bronnen die bij ons altijd gelijk waren | `Consulta_DNPRC` veld `ss`, en WFS `cp:areaValue` | 1 |
| 2 | Geometrie als GeoJSON of GML | Ja. WFS levert GML 3.2, omzetten naar GeoJSON is 20 regels code | INSPIRE WFS Cadastral Parcels | 1 |
| 3 | Gebouwen: bouwjaar, bouwlagen, m² per bouwdeel, gebruik | Ja, maar uit twee verschillende diensten die je moet combineren | `Consulta_DNPRC` (`lcons`) + INSPIRE WFS Buildings | 1 |
| 4 | Verschil *superficie construida* en *superficie útil* | Ja, en het is groot: circa 12 % in ons testgeval. Advertenties gebruiken bijna altijd **construida**; de wet eist **útil** | RD 1020/1993 Norma 11.3 en RD 3148/1978 | 2 |
| 5 | Staat een gebouw wel of niet in het kadaster | Ja, hard vast te stellen. Maar het is een **signaal**, geen bewijs van illegaliteit | WFS Buildings + `sfc` | 1 + 2 |

Wat we vandaag nieuw hebben vastgesteld en wat nog niet in R11 stond:

1. De WFS voor gebouwen heeft **vijf** opgeslagen zoekopdrachten, niet één. `GetBuildingPartByParcel`
   geeft het aantal bouwlagen per bouwdeel; `GetOtherBuildingByParcel` geeft zwembaden en andere
   bijwerken apart. Dat stond nergens in ons materiaal en het is precies wat een renovatierekening
   nodig heeft.
2. Het zwembad staat in het kadaster als `constructionNature: openAirPool`. Bij beide geteste villa's
   klopte dat met de foto's in de advertentie.
3. De WFS negeert `resulttype=hits`. Je kunt dus niet goedkoop tellen hoeveel percelen er in een
   gebied liggen; je moet ze binnenhalen.
4. Een gebied van circa 8,7 km² geeft een serverfout na bijna twee minuten. Heel Jávea in één
   WFS-verzoek kan niet. Dat moet via het ATOM-bestand per gemeente.
5. De SOAP-variant werkt alleen met een ongebruikelijke opbouw van het bericht: de drie parameters
   staan los naast elkaar in de `Body`, niet verpakt in een `Consulta_DNPRC`-element. Met de voor de
   hand liggende opbouw krijg je "LA REFERENCIA CATASTRAL ES OBLIGATORIA".
6. **Jávea heeft tussen eind 2016 en eind 2018 een *regularización catastral* gehad**, een
   opsporingsronde van de belastingdienst naar niet-aangegeven bouwwerken. Dat maakt vraag 5 veel
   sterker: een gebouw van vóór 2016 dat nu nog steeds niet in het kadaster staat, is de dans
   ontsprongen én is dus een uitgesproken afwijking.

Er is één ding dat het kadaster **niet** kan: zeggen of er een vergunning is. Zie hoofdstuk 8.

---

## 2. Wat je nodig hebt om te beginnen

Niets. Geen API-sleutel, geen account, geen certificaat.

| Host | Waarvoor | Certificaat | robots.txt |
|---|---|---|---|
| `ovc.catastro.meh.es` | Webservices, WFS, WMS | Werkt overal | HTTP 404, dus geen regels (getest 18-09-2026) |
| `www.catastro.hacienda.gob.es` | ATOM-bestanden, documentatie | **Valkuil**, zie hieronder | Geeft een "pagina niet gevonden"-pagina, dus geen regels |
| `www1.sedecatastro.gob.es` | Kaartkijker, certificaten | Werkt | HTTP 404 |
| `www.sedecatastro.gob.es` | Sede, massadownload | Werkt | HTTP 404 |

**De certificaatvalkuil.** `www.catastro.hacienda.gob.es` gebruikt een certificaat van de Spaanse
FNMT. De `curl` van macOS en de standaard-`urllib` van Python weigeren de verbinding met "unable to
get local issuer certificate". `httpx` uit de Hermes-venv doet het wel, want die gebruikt de
certifi-bundel. Gebruik dus `httpx` voor alles wat op die host staat, en nooit `curl -k`. Bewijstype 1,
opnieuw bevestigd vandaag.

De officiële handleiding is
[`Webservices_Libres.pdf`](https://www.catastro.hacienda.gob.es/ws/Webservices_Libres.pdf),
versie 2.6 van 09-10-2025 (bewijstype 4, zelf opgehaald en uitgelezen). Daarin staat letterlijk
dat deze diensten "pueden ser invocados por cualquier ciudadano" en dat ze alle gegevens geven
"todos excepto titularidad y valor" — alles behalve eigenaar en kadastrale waarde. Dat laatste is
precies wat wij volgens onze eigen regels ook niet willen opslaan.

---

## 3. De diensten, één voor één

### 3.1 COVCCallejero — gegevens bij een kadastrale referentie

Basis-URL: `https://ovc.catastro.meh.es/OVCServWeb/OVCWcfCallejero/COVCCallejero.svc`

Drie uitvoervormen, dezelfde inhoud:

| Vorm | Pad | Antwoord |
|---|---|---|
| JSON | `/json/Consulta_DNPRC?...` | `application/json` |
| XML (REST) | `/rest/Consulta_DNPRC?...` | `application/xml` |
| SOAP | `/soap` met POST | multipart/XOP, XML in de `Body` |

Hulp-eindpunten die de dienst zelf aanbiedt: `/rest/help` en `/json/help`. WSDL:
`?singleWsdl` (100 KB, bevat alle operaties en SOAP-acties).

**De zeven operaties** (bewijstype 4, uit de handleiding, alle zelf uitgeprobeerd):

| Operatie | Waarvoor | Verplichte parameters |
|---|---|---|
| `ObtenerProvincias` | lijst provincies | — |
| `ObtenerMunicipios` | lijst gemeenten van een provincie | `Provincia` |
| `ObtenerCallejero` | straten van een gemeente | `Provincia`, `Municipio` |
| `ObtenerNumerero` | huisnummers van een straat | `Provincia`, `Municipio`, `TipoVia`, `NomVia` |
| `Consulta_DNPLOC` | gegevens op adres | `Provincia`, `Municipio`, `Sigla`, `Calle`, `Numero` |
| `Consulta_DNPRC` | gegevens op kadastrale referentie | `RefCat` |
| `Consulta_DNPPP` | gegevens op polígono/parcela (landelijk gebied) | `Provincia`, `Municipio`, `Poligono`, `Parcela` |

**Let op de parameternamen.** De JSON- en REST-variant willen `RefCat`. De oude ASMX-variant
(`.../OVCSWLocalizacionRC/OVCCallejero.asmx/Consulta_DNPRC`) wil `RC`. En die oude variant geeft
**geen** perceeloppervlakte terug — alleen `sfc` en `ant`. Getest vandaag op 6442021BC5964S: ASMX
gaf `sfc 320` en `ant 2005`, maar geen `ss`. Gebruik dus altijd de nieuwe dienst. Bewijstype 1.

**Werkend voorbeeld, JSON:**

```
https://ovc.catastro.meh.es/OVCServWeb/OVCWcfCallejero/COVCCallejero.svc/json/Consulta_DNPRC?Provincia=&Municipio=&RefCat=6442021BC5964S
```

Antwoord (HTTP 200, 1.331 bytes, 0,32 s), ingekort:

```json
{"consulta_dnprcResult": {
  "control": {"cudnp": 1, "cucons": 4},
  "bico": {
    "bi": {
      "idbi": {"cn": "UR", "rc": {"pc1":"6442021","pc2":"BC5964S","car":"0001","cc1":"P","cc2":"S"}},
      "ldt": "CL NADALETA 3 03730 JAVEA/XABIA (ALICANTE)",
      "debi": {"luso":"Residencial", "sfc":"320", "cpt":"100,000000", "ant":"2005"}
    },
    "finca": {
      "ltp": "Parcela construida sin división horizontal",
      "dff": {"ss": "1151"},
      "infgraf": {"igraf": "https://www1.sedecatastro.gob.es/Cartografia/mapa.aspx?del=3&mun=82&refcat=6442021BC5964S"}
    },
    "lcons": [
      {"lcd":"VIVIENDA",     "dt":{"lourb":{"loint":{"pt":"00","pu":"01"}}}, "dfcons":{"stl":"118"}, "dvcons":{"dtip":"VIVIENDA UNIFAMILIAR"}},
      {"lcd":"VIVIENDA",     "dt":{"lourb":{"loint":{"pt":"01","pu":"01"}}}, "dfcons":{"stl":"105"}, "dvcons":{"dtip":"VIVIENDA UNIFAMILIAR"}},
      {"lcd":"APARCAMIENTO", "dt":{"lourb":{"loint":{"pt":"00","pu":"02"}}}, "dfcons":{"stl":"64"},  "dvcons":{"dtip":"ANEJOS DE VIVIENDA Y LOCALES EN ESTRUCTURA"}},
      {"lcd":"DEPORTIVO",    "dt":{"lourb":{"loint":{"pt":"00","pu":"03"}}}, "dfcons":{"stl":"33"},  "dvcons":{"dtip":"DEPORTES AIRE LIBRE"}}
    ]
  }
}}
```

**De velden die ertoe doen** (betekenis letterlijk uit de handleiding, bewijstype 4):

| Veld | Betekenis volgens de handleiding | In het voorbeeld |
|---|---|---|
| `cn` | `UR` = urbano, `RU` = rústico | UR |
| `ss` | SUPERFICIE DEL SOLAR — de perceeloppervlakte | 1.151 m² |
| `sfc` | SUPERFICIE — de bebouwde oppervlakte van dit onroerend goed | 320 m² |
| `ant` | ANTIGÜEDAD — het bouwjaar | 2005 |
| `luso` | hoofdgebruik | Residencial |
| `cpt` | COEFICIENTE DE PARTICIPACIÓN — aandeel in het perceel, in procenten | 100 % |
| `ltp` | soort perceel | Parcela construida sin división horizontal |
| `lcd` | gebruik van het bouwdeel | VIVIENDA, APARCAMIENTO, DEPORTIVO |
| `pt` | *planta*, de bouwlaag: `00` = begane grond, `01` = eerste, `-1` = kelder | 00, 01 |
| `stl` | SUPERFICIE DE LA UNIDAD CONSTRUCTIVA — m² van dat bouwdeel | 118, 105, 64, 33 |
| `dtip` | typologie van het bouwdeel | VIVIENDA UNIFAMILIAR |
| `lspr` | lijst *subparcelas* bij landbouwgrond, met gewas en m² | zie 3.2 |

**Controle die altijd moet kloppen:** de som van alle `stl` is gelijk aan `sfc`. In dit geval
118 + 105 + 64 + 33 = 320. Bewijstype 5. Klopt dat niet, dan heb je een parseerfout gemaakt.

**De SOAP-variant.** Endpoint `/soap`, SOAPAction
`http://www.catastro.meh.es/ICOVCCallejero/Consulta_DNPRC`. De parameters staan los in de `Body`,
niet verpakt:

```xml
<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"
               xmlns:c="http://www.catastro.meh.es/">
  <soap:Body>
    <c:Provincia></c:Provincia>
    <c:Municipio></c:Municipio>
    <c:RefCat>6442021BC5964S</c:RefCat>
  </soap:Body>
</soap:Envelope>
```

Getest: HTTP 200, 2.167 bytes, 0,31 s, met `<ss>1151</ss>` en de vier `<stl>`-regels. Bewijstype 1.
SOAP geeft niets extra's boven JSON. Wij hebben het niet nodig; het staat hier omdat het gevraagd is.

### 3.2 Vier soorten percelen, vier soorten antwoorden

Dit is de belangrijkste valkuil van deze dienst. Eén kadastrale referentie van 14 tekens kan
verwijzen naar één onroerend goed, naar tachtig, of naar geen enkel.

**Geval A — gewone villa, één eigendom.** `6442021BC5964S`. Antwoord bevat `bico` met `bi`,
`finca` en `lcons`. Dit is het makkelijke geval.

**Geval B — appartementengebouw (*división horizontal*, splitsing in appartementsrechten).**
`5656508BC5955N`, AV PARIS 10 in Jávea. De referentie van 14 tekens geeft **niets**:

```
Consulta_DNPRC?RefCat=5656518BC5955N
  → {"control":{"cuerr":1},"lerr":[{"cod":"5","des":"NO EXISTE NINGÚN INMUEBLE CON LOS PARÁMETROS INDICADOS"}]}
```

Je moet dan via het adres binnenkomen. `Consulta_DNPLOC` op AV PARIS 10 geeft `cudnp: 87` en een
lijst `lrcdnp` met 87 referenties van 20 tekens, elk met eigen `sfc` en `cpt`. Eén daarvan
uitvragen:

```
Consulta_DNPRC?RefCat=5656508BC5955N0003KL
  → ldt  "AV PARIS 10 Es:8 Pl:00 Pt:03 03730 JAVEA/XABIA"
    ltp  "Parcela con varios inmuebles (division horizontal)"
    ss   726   (het hele perceel)
    sfc  73    (dit appartement)
    cpt  2,373 %
    ant  1970
    lcons: VIVIENDA, planta 00, 73 m², VIVIENDA COLECTIVA
```

**Voor Deal Hunter:** bij een appartement is `ss` de oppervlakte van het hele perceel onder het
gebouw, niet van de woning. Nooit als perceeloppervlakte in een rekenmodel zetten.

**Geval C — één perceel, meerdere eigendommen van verschillende soort.** `6817951BC5961N` aan de
CR GUARDIA LA in Jávea. `Consulta_DNPRC` geeft geen `bico` maar `lrcdnp` met twee regels: `...0000UZ`
(landbouwgrond, luso "Agrario") en `...0001IX` (stedelijk, "Obras de urbanización y jardineria,
suelos sin edificar"). Pas als je de referentie van 20 tekens uitvraagt krijg je `finca` met
`ss` = 100.690 m² en, bij de landbouwregel, vijf *subparcelas*:

```
lspr: a  C-  LABOR O LABRADÍO SECANO  1.268 m²
      b  C-  LABOR O LABRADÍO SECANO    390 m²
      c  C-  LABOR O LABRADÍO SECANO    735 m²
      d  C-  LABOR O LABRADÍO SECANO  1.748 m²
      e  C-  LABOR O LABRADÍO SECANO    695 m²
```

`ltp` luidt hier: "Parcela, a efectos catastrales, con inmuebles de distinta clase (urbano y
rústico)". Dit soort percelen komt in het achterland van Jávea veel voor en is precies de categorie
waar Deal Hunter naar zoekt. Bewijstype 1.

**Geval D — onbebouwd perceel.** `2944017BC5924S`, CL MAR AMARILLO 4. `ss` = 1.074 m², `sfc` = 0,
`luso` = "Obras de urbanización y jardineria, suelos sin edificar", geen `ant`, geen `lcons`. De
WFS voor gebouwen geeft een lege `FeatureCollection` zonder één `featureMember`. Bewijstype 1.

**Landelijke percelen zonder adres:** `Consulta_DNPPP` met `Poligono` en `Parcela`. Getest met
polígono 10 / parcela 100 in Jávea: foutcode 5, dat nummerpaar bestaat daar niet. De dienst
werkt wel; je moet de juiste nummers hebben, bijvoorbeeld uit een *nota simple*, het uittreksel
uit het eigendomsregister.

### 3.3 COVCCoordenadas — van punt naar referentie en terug

Basis-URL: `https://ovc.catastro.meh.es/OVCServWeb/OVCWcfCallejero/COVCCoordenadas.svc`

| Operatie | Waarvoor | Parameters |
|---|---|---|
| `Consulta_RCCOOR` | referentie van het perceel waarin het punt ligt | `SRS`, `CoorX`, `CoorY` |
| `Consulta_RCCOOR_Distancia` | lijst van nabije percelen met afstand in meters | `SRS`, `CoorX`, `CoorY` |
| `Consulta_CPMRC` | coördinaten bij een referentie | `Provincia`, `Municipio`, `SRS`, `RC` |

**Let op:** in de JSON-variant heten de parameters `CoorX` en `CoorY`, in de oude XML-variant
`Coordenada_X` en `Coordenada_Y`. `CoorX` is de **lengtegraad**, `CoorY` de **breedtegraad**. Dat is
omgekeerd aan hoe je het in een kaartbibliotheek intypt.

Voorbeeld op de pin van een echte advertentie (Calle Nadaleta 3):

```
.../COVCCoordenadas.svc/json/Consulta_RCCOOR_Distancia?SRS=EPSG:4326&CoorX=0.1950078&CoorY=38.7602155

6442021BC5964S  dis 0      CL NADALETA 3
6442009BC5964S  dis 16,01  PD CM CAP MARTI 421
6442019BC5964S  dis 16,94  CL NADALETA 1
6442008BC5964S  dis 18,37  PD CM CAP MARTI 355
```

`dis` = 0 betekent dat het punt ín dat perceel valt. Dat is de enige situatie waarin je de
koppeling zonder verdere controle mag aannemen.

### 3.4 INSPIRE WFS Cadastral Parcels — de perceelgrens

Eindpunt: `https://ovc.catastro.meh.es/INSPIRE/wfsCP.aspx`

Uit `GetCapabilities` (getest, 14.510 bytes):

- Titel: "Spanish INSPIRE Download Service - Cadastral Parcels"
- Aanbieder: "Spanish General Directorate for Cadastre"
- `Fees`: **"No conditions apply"**
- `AccessConstraints`: "License documentation:
  https://www.catastro.hacienda.gob.es/webinspire/documentos/Licencia_en.pdf"
- Objecttypen: `cp:CadastralParcel`, `cp:CadastralZoning`
- Standaard-CRS `EPSG::4326`; verder onder meer 4258, 25829, **25830**, 25831, 3857, 3035
- `ImplementsResultPaging` = **FALSE**

Vijf opgeslagen zoekopdrachten (uit `DescribeStoredQueries`, bewijstype 1):
`GetParcel`, `GetFeatureById`, `GetNeighbourParcel`, `GetZoning`, `GetParcelByZoning`.

**Werkend voorbeeld:**

```
https://ovc.catastro.meh.es/INSPIRE/wfsCP.aspx?service=wfs&version=2.0.0&request=GetFeature&STOREDQUERIE_ID=GetParcel&refcat=6442021BC5964S&srsname=EPSG::4326
```

HTTP 200, 2.918 bytes, 0,14 s, `text/xml`. Kern van het antwoord:

```xml
<cp:CadastralParcel gml:id="ES.SDGC.CP.6442021BC5964S">
  <cp:areaValue uom="m2">1151</cp:areaValue>
  <cp:beginLifespanVersion>...</cp:beginLifespanVersion>
  <cp:geometry>
    <gml:MultiSurface srsName="http://www.opengis.net/def/crs/EPSG/0/4326">
      ... <gml:posList srsDimension="2" count="20">38.760142 0.195341 ...</gml:posList>
    </gml:MultiSurface>
  </cp:geometry>
  <cp:nationalCadastralReference>6442021BC5964S</cp:nationalCadastralReference>
  <cp:referencePoint><gml:Point>...</gml:Point></cp:referencePoint>
</cp:CadastralParcel>
```

Let op de parameternaam: het is `STOREDQUERIE_ID`, met een spelfout die van de dienst zelf komt.
En op de assenvolgorde: in `EPSG::4326` staat **breedtegraad eerst**, dus `lat lon`. GeoJSON wil
`lon lat`. Omdraaien dus.

Vraag je `srsname=EPSG::25830` (ETRS89 / UTM zone 30N, het Spaanse projectiestelsel in meters),
dan krijg je dezelfde vorm in meters. Dat is handig, want daarin kun je met de schoenveterformule
zelf de oppervlakte narekenen zonder bibliotheek.

**Kaart-bbox zonder referentie:**

```
...?service=wfs&version=2.0.0&request=GetFeature&Typenames=cp.cadastralparcel&bbox=38.760,0.150,38.775,0.165&srsname=EPSG::4326
```

Getest: 953 percelen, 2.089.786 bytes, 23,9 s. Zie hoofdstuk 9 voor de grenzen.

### 3.5 INSPIRE WFS Buildings — de gebouwen

Eindpunt: `https://ovc.catastro.meh.es/INSPIRE/wfsBU.aspx`

**Vijf** opgeslagen zoekopdrachten (uit `DescribeStoredQueries`, bewijstype 1). Dit is de vondst
van deze ronde:

| Zoekopdracht | Wat het geeft |
|---|---|
| `GetBuildingByParcel` | het gebouw als geheel: bouwjaar, staat, gebruik, aantal woningen, totale m² |
| `GetBuildingPartByParcel` | de bouwdelen apart, **met aantal bouwlagen boven en onder maaiveld** |
| `GetOtherBuildingByParcel` | bijwerken: zwembad, en andere `constructionNature` |
| `GetAllConstructionByParcel` | gebouw plus bijwerken in één antwoord (niet de bouwdelen) |
| `GetFeatureById` | op interne id |

**Voorbeeld 1, het gebouw:**

```
https://ovc.catastro.meh.es/INSPIRE/wfsBU.aspx?service=wfs&version=2.0.0&request=GetFeature&STOREDQUERIE_ID=GetBuildingByParcel&refcat=6442021BC5964S&srsname=EPSG::4326
```

Levert onder meer:

```xml
<bu-core2d:conditionOfConstruction>functional</bu-core2d:conditionOfConstruction>
<bu-core2d:dateOfConstruction><bu-core2d:DateOfEvent>
  <bu-core2d:beginning>2005-01-01T00:00:00</bu-core2d:beginning>
</bu-core2d:DateOfEvent></bu-core2d:dateOfConstruction>
<bu-ext2d:currentUse>1_residential</bu-ext2d:currentUse>
<bu-ext2d:numberOfBuildingUnits>1</bu-ext2d:numberOfBuildingUnits>
<bu-ext2d:numberOfDwellings>1</bu-ext2d:numberOfDwellings>
<bu-ext2d:numberOfFloorsAboveGround xsi:nil="true" nilReason="other:unpopulated"/>
<bu-ext2d:officialArea><bu-ext2d:OfficialArea>
  <bu-ext2d:officialAreaReference>grossFloorArea</bu-ext2d:officialAreaReference>
  <bu-ext2d:value uom="m2">320</bu-ext2d:value>
</bu-ext2d:OfficialArea></bu-ext2d:officialArea>
<bu-ext2d:document><bu-ext2d:Document>
  <bu-ext2d:documentLink>http://ovc.catastro.meh.es/OVCServWeb/OVCWcfLibres/OVCFotoFachada.svc/RecuperarFotoFachadaGet?ReferenciaCatastral=6442021BC5964S</bu-ext2d:documentLink>
  <bu-ext2d:format>jpeg</bu-ext2d:format>
  <bu-ext2d:sourceStatus>NotOfficial</bu-ext2d:sourceStatus>
</bu-ext2d:Document></bu-ext2d:document>
```

Belangrijk: `numberOfFloorsAboveGround` is op gebouwniveau **leeg**. Wie alleen deze zoekopdracht
gebruikt, concludeert ten onrechte dat het aantal bouwlagen onbekend is.

En let op `officialAreaReference: grossFloorArea`. Het Catastro zegt dus zelf, in INSPIRE-termen,
dat zijn 320 m² een brutovloeroppervlak is. Dat is het scharnier van hoofdstuk 7.

**Voorbeeld 2, de bouwdelen:**

```
...&STOREDQUERIE_ID=GetBuildingPartByParcel&refcat=6442021BC5964S&srsname=EPSG::4326
```

Vijf bouwdelen, elk met een eigen omtrek:

| Bouwdeel | Bouwlagen boven | Bouwlagen onder | Punten in de omtrek |
|---|---|---|---|
| `_part1` | 2 | 0 | 13 |
| `_part2` | 1 | 0 | 6 |
| `_part3` | 1 | 0 | 6 |
| `_part4` | 2 | 0 | 5 |
| `_part5` | 1 | 0 | 9 |

**Voorbeeld 3, de bijwerken:**

```
...&STOREDQUERIE_ID=GetOtherBuildingByParcel&refcat=6442021BC5964S&srsname=EPSG::4326
  → <bu-ext2d:OtherConstruction gml:id="ES.SDGC.BU.6442021BC5964S_PI.1">
      <bu-ext2d:constructionNature>openAirPool</bu-ext2d:constructionNature>
```

Een zwembad staat dus als apart object in het kadaster, met eigen omtrek. Dat bevestigden we ook
op 0281206BC5908S in de Montgó. Voor een renovatiebegroting is dat rechtstreeks bruikbaar: je weet
of er een bad ligt, hoe groot, en of het is aangegeven.

Elk antwoord van deze dienst draagt de opmerking mee: "La precisión es la que corresponde
nominalmente a la escala de captura de la cartografía". Vertaald: de nauwkeurigheid is die van de
schaal waarop de kaart is ingemeten. Het veld `horizontalGeometryEstimatedAccuracy` staat op 0,1 m,
maar dat is een opgegeven waarde, geen garantie per pand.

### 3.6 INSPIRE WMS — een kaartplaatje

Eindpunt: `https://ovc.catastro.meh.es/cartografia/INSPIRE/spadgcwms.aspx`

Getest met een `GetMap` over het testperceel: HTTP 200, 10.611 bytes, `image/png`, 600 × 600,
RGBA. Lagen: `CP.CadastralParcel`, `CP.CadastralZoning`, `AD.Address`, `BU.Building`.

```
...spadgcwms.aspx?service=WMS&request=GetMap&version=1.3.0&layers=CP.CadastralParcel&styles=&crs=EPSG:4326&bbox=38.7598,0.1945,38.7607,0.1956&width=600&height=600&format=image/png
```

Dit is wat het dashboard nu al gebruikt. Prima voor beeld, ongeschikt voor rekenwerk.

### 3.7 ATOM — het hele gemeentebestand

Overzicht: `https://www.catastro.hacienda.gob.es/webinspire/index.html`. Daar staat letterlijk:
"Estos servicios permiten la descarga completa por municipios de los diferentes conjuntos de datos
INSPIRE. **Los datos se actualizan 2 veces al año**." Bewijstype 4.

Landelijke feed → provinciefeed → gemeente-entry:

```
https://www.catastro.hacienda.gob.es/INSPIRE/CadastralParcels/ES.SDGC.CP.atom.xml
https://www.catastro.hacienda.gob.es/INSPIRE/CadastralParcels/03/ES.SDGC.CP.atom_03.xml
```

De entry voor Jávea (INE-code **03082**), zelf uitgelezen op 18-09-2026:

| Bestandsset | URL van het zip | Grootte | Bijgewerkt |
|---|---|---|---|
| Percelen (CP) | `.../CadastralParcels/03/03082-JAVEA XABIA/A.ES.SDGC.CP.03082.zip` | 8.400.856 bytes | 21-08-2026 12.47 uur |
| Gebouwen (BU) | `.../Buildings/03/03082-JAVEA XABIA/A.ES.SDGC.BU.03082.zip` | 13.252.024 bytes | 21-08-2026 16.07 uur |
| Adressen (AD) | `.../Addresses/03/03082-JAVEA XABIA/A.ES.SDGC.AD.03082.zip` | 863.348 bytes | 21-08-2026 13.23 uur |

Samen **22,5 MB**. De spatie in "03082-JAVEA XABIA" moet als `%20` in de URL.

De omhullende rechthoek van Jávea uit de feed zelf: 38,7151 – 38,8193 noorderbreedte en
0,1015 – 0,2351 oosterlengte, oftewel circa 11,6 bij 11,6 km. Coördinaatstelsel van de bestanden:
EPSG 25830 (ETRS89 / UTM 30N). Bewijstype 3.

De feed draagt zijn eigen licentieregel mee, letterlijk:

> "This service can be used free of charge in every instance, as long as that the D. G. of the
> Cadastre (Ministry of Finance) is mentioned as author and owner of the information"

Gratis, mits bronvermelding. Bewijstype 4.

**De licentie-PDF zelf is niet machinaal te lezen.** Zowel `Licencia.pdf` (100.483 bytes) als
`Licencia_en.pdf` (92.784 bytes) zijn opgehaald; alleen de titel komt eruit ("LICENSE OF ACCESS AND
USE OF INSPIRE DATASETS AND SERVICES OF THE DIRECTORATE GENERAL FOR CADASTRE"), de rest gebruikt
een eigen lettercodering. R11 liep hier ook op vast. Wij houden ons daarom aan de twee regels die
wél leesbaar zijn: `Fees: No conditions apply` en de `<rights>`-regel hierboven. Bewijstype 1
voor het feit dat de tekst onleesbaar is.

### 3.8 Descarga masiva — de zware bestanden achter een certificaat

`https://www.sedecatastro.gob.es/Accesos/SECAccDescargaDatos.aspx`. De alfanumerieke CAT-bestanden
per provincie, de shapefile-cartografie en de historische kaarten vereisen een digitaal certificaat
of Cl@ve, plus aanvaarding van een licentie. Dat is de route die R11 al beschreef; wij hebben er
vandaag niets aan veranderd en gebruiken hem niet.

De bijbehorende regel is de Resolución van 23-03-2011 van de Dirección General del Catastro
(`https://www.catastro.hacienda.gob.es/documentos/normativa/res_230311.pdf`). Kern: toestemming is
gratis en automatisch na identificatie met elektronische handtekening, maar de informatie mag
alleen worden gebruikt "a los efectos de que la misma sea transformada por el interesado,
elaborando nuevos productos de valor añadido" — dus bewerken mag, doorverkopen in ruwe vorm niet.
Bronvermelding en raadpleegdatum zijn verplicht in elk afgeleid product. Bewijstype 2, overgenomen
uit R11.

---

## 4. Vraag 1 — de officiële perceeloppervlakte

Twee onafhankelijke bronnen, en een derde die je zelf kunt narekenen:

| Bron | Veld | Testperceel 6442021BC5964S |
|---|---|---|
| `Consulta_DNPRC` | `finca.dff.ss` | 1.151 m² |
| WFS Cadastral Parcels | `cp:areaValue uom="m2"` | 1.151 m² |
| Eigen berekening op de WFS-geometrie in EPSG 25830 | schoenveterformule | 1.151,4 m² |

Ze kwamen bij alle geteste percelen op de meter overeen. Op 0281206BC5908S (Montgó): 1.572 / 1.572 /
1.572,6 m². Bewijstype 1 en 5.

**Gebruik `ss`** als het snel moet: één verzoek, klein antwoord. **Gebruik `areaValue`** als je toch
al de geometrie ophaalt. **Reken zelf na** als controle: wijkt je eigen som meer dan een procent af,
dan heb je de assen omgedraaid of een gat in het perceel gemist.

Twee waarschuwingen:

1. Bij *división horizontal* is `ss` de oppervlakte van het hele blok, niet van de woning (zie 3.2).
2. De kadastrale oppervlakte is niet automatisch de juridische. De akte en de *nota simple* kunnen
   een ander getal noemen. De wet zegt het zelf, in artikel 3.3 van het Texto Refundido de la Ley
   del Catastro Inmobiliario: "Salvo prueba en contrario y sin perjuicio del Registro de la
   Propiedad, cuyos pronunciamientos jurídicos prevalecerán, los datos contenidos en el Catastro
   Inmobiliario se presumen ciertos." Vermoed waar, tenzij tegenbewijs, en het eigendomsregister
   gaat juridisch voor. Bron:
   [BOE-A-2004-4163](https://www.boe.es/buscar/act.php?id=BOE-A-2004-4163), bewijstype 2,
   geraadpleegd 18-09-2026.

---

## 5. Vraag 2 — de geometrie als GeoJSON

De WFS geeft GML 3.2. GeoJSON maak je er zelf van; dat is eenvoudiger dan het klinkt, want de
Catastro levert alleen eenvoudige vlakken zonder gaten.

Drie dingen om goed te doen:

1. **Assenvolgorde.** In `EPSG::4326` staat er `lat lon` in de `posList`. GeoJSON wil `[lon, lat]`.
2. **Ring sluiten.** De `gml:LinearRing` van de Catastro is al gesloten; eerste en laatste punt zijn
   gelijk. Niet nog een keer sluiten.
3. **Oppervlakte reken je in 25830, niet in 4326.** Graden zijn geen meters. Haal het perceel
   desnoods twee keer op, één keer in elk stelsel. Dat scheelt een projectiebibliotheek.

### Het script

`onderzoek/N04-voorbeelden/kadaster_perceel.py`, getest en werkend met de kale `/usr/bin/python3`
van macOS. Geen enkele bibliotheek geïnstalleerd, alleen `urllib`, `json`, `re` en `math` uit de
standaardbibliotheek. Er zit een wachtrem van één verzoek per seconde in.

```
$ python3 kadaster_perceel.py 6442021BC5964S

Kadastrale referentie : 6442021BC5964S
Adres                 : CL NADALETA 3 03730 JAVEA/XABIA (ALICANTE)
Perceeltype           : Parcela construida sin división horizontal
Perceel (DNPRC ss)    : 1151 m2
Perceel (WFS areaValue): 1151 m2
Perceel (zelf berekend): 1151.4 m2  [shoelace op EPSG:25830]
Bebouwd (sfc)         : 320 m2 superficie construida
Bouwjaar (ant / WFS)  : 2005 / 2005
Voetafdruk gebouw     : 198.5 m2 ; staat: functional
Bouwlagen per bouwdeel: boven [2, 1, 1, 2, 1] / onder [0, 0, 0, 0, 0]
Zwembad in kadaster   : ja
Bebouwingsgraad       : 17.2 % van het perceel
   - VIVIENDA     verdieping  00    118 m2  VIVIENDA UNIFAMILIAR
   - VIVIENDA     verdieping  01    105 m2  VIVIENDA UNIFAMILIAR
   - APARCAMIENTO verdieping  00     64 m2  ANEJOS DE VIVIENDA Y LOCALES EN ESTRUCTURA
   - DEPORTIVO    verdieping  00     33 m2  DEPORTES AIRE LIBRE
   som bouwdelen      : 320 m2 (moet gelijk zijn aan sfc 320)
GeoJSON geschreven    : ./6442021BC5964S.geojson
```

Het bestand `6442021BC5964S.geojson` staat naast het script en bevat acht objecten: het perceel,
het gebouw, vijf bouwdelen en het zwembad. Het is rechtstreeks in Leaflet te laden, dus in het
dashboard en op de telefoonpagina.

De kern van de omzetting, voor wie hem ergens anders wil inbouwen:

```python
def ringen(xml_tekst, lat_eerst):
    """Alle gml:posList in het document -> lijst van ringen [[lon,lat],...]."""
    uit = []
    for m in re.finditer(r"<gml:posList[^>]*>([^<]+)</gml:posList>", xml_tekst):
        g = [float(x) for x in m.group(1).split()]
        paren = list(zip(g[0::2], g[1::2]))
        uit.append([[b, a] if lat_eerst else [a, b] for a, b in paren])
    return uit

def shoelace(ring):
    """Oppervlakte in vierkante eenheden van het stelsel (dus m2 bij UTM)."""
    s = 0.0
    for (x1, y1), (x2, y2) in zip(ring, ring[1:]):
        s += x1 * y2 - x2 * y1
    return abs(s) / 2.0
```

### Waarvoor je de geometrie nodig hebt

- **Punt in polygoon.** Ligt de pin van de advertentie werkelijk in dit perceel? Een advertentie
  zonder adres heeft een verschoven pin; zie hoofdstuk 10.
- **Bebouwingsgraad.** Voetafdruk van het gebouw gedeeld door de perceeloppervlakte. In het
  testgeval 198,5 / 1.151 = 17,2 %. Dat is een eerste toets op restbouwrecht, geen conclusie: wat
  het plan toestaat komt uit R12.
- **Buren en samenvoegen.** `GetNeighbourParcel` geeft de belendende percelen in één verzoek.
- **Hellingen en afstand tot de grens.** Met het IGN-hoogtemodel over dezelfde omtrek.

---

## 6. Vraag 3 — de gebouwen op het perceel

Je hebt beide diensten nodig, want ze weten elk iets wat de ander niet heeft.

| Wat je wilt weten | Waar het staat | Voorbeeldwaarde |
|---|---|---|
| Bouwjaar | `debi.ant` én `dateOfConstruction.beginning` | 2005 / 2005-01-01 |
| Oppervlakte per bouwdeel | `lcons[].dfcons.stl` | 118, 105, 64, 33 m² |
| Op welke bouwlaag | `lcons[].dt.lourb.loint.pt` | 00, 01, 02, ook `-1` |
| Gebruik per bouwdeel | `lcons[].lcd` en `dvcons.dtip` | VIVIENDA / VIVIENDA UNIFAMILIAR |
| **Aantal bouwlagen** | WFS `GetBuildingPartByParcel` → `numberOfFloorsAboveGround` | 2, 1, 1, 2, 1 |
| Kelder | idem → `numberOfFloorsBelowGround` | 0 |
| Staat van het gebouw | WFS → `conditionOfConstruction` | `functional`, ook `ruin`, `declined` |
| Aantal woningen | WFS → `numberOfDwellings` | 1 |
| Hoofdgebruik | WFS → `currentUse` | `1_residential` |
| Totale bebouwde m² | `debi.sfc` = WFS `officialArea` | 320 = 320 |
| Voetafdruk in m² | zelf berekenen op de WFS-omtrek | 198,5 m² |
| Zwembad en bijwerken | WFS `GetOtherBuildingByParcel` → `constructionNature` | `openAirPool` |
| Gevelfoto | `documentLink`, `sourceStatus: NotOfficial` | JPEG |

Tweede testobject, midden in het oude centrum, `3964301BC5937S` aan de CL DEL MESTRE JESUS
MONTANER 8. Hier zie je de bouwlagen echt terug in `lcons`:

```
ss   822 m²   sfc 341 m²   ant 1958   ltp "Parcela construida sin división horizontal"
  VIVIENDA  verdieping 00   166 m²
  VIVIENDA  verdieping 01   131 m²
  VIVIENDA  verdieping 02    14 m²
  ALMACEN   verdieping 00    30 m²
                            ---
                            341 m²  = sfc
```

Een pand uit 1958 van drie lagen met 14 m² op de tweede verdieping: dat is een dakopbouw of een
trappenhuis, geen volwaardige etage. Zulke details zijn precies wat een splitsingsplan maakt of
breekt, en ze zijn gratis. Bewijstype 1.

**De gevelfoto** is bruikbaar maar niet betrouwbaar gedateerd: `sourceStatus` is `NotOfficial` en
bij het Montgó-object was de EXIF-datum 2017 (uit R11). Gebruik hem om te zien of er iets staat,
niet om te bepalen wanneer.

---

## 7. Vraag 4 — *superficie construida* tegenover *superficie útil*

### De twee definities, letterlijk

**Superficie construida**, de bebouwde oppervlakte. Real Decreto 1020/1993, Norma 11, punt 3
([BOE nr. 174 van 22-07-1993](https://www.boe.es/diario_boe/xml.php?id=BOE-A-1993-19265),
bewijstype 2, tekst zelf opgehaald 18-09-2026):

> "Se entiende como superficie construida la superficie incluida dentro de la línea exterior de los
> parámetros perimetrales de una edificación y, en su caso, de los ejes de las medianerías, deducida
> la superficie de los patios de luces. Los balcones, terrazas, porches y demás elementos análogos,
> que estén cubiertos se computarán al 50 por 100 de su superficie, salvo que estén cerrados por
> tres de sus cuatro orientaciones, en cuyo caso se computarán al 100 por 100. En uso residencial,
> no se computarán como superficie construida los espacios de altura inferior a 1,50 metros."

In gewone woorden: meet aan de **buitenkant** van de muren. Een overdekt terras of een porche telt
voor de **helft** mee, maar voor honderd procent als hij aan drie van de vier kanten dicht is.
Lichtschachten gaan eraf, en bij wonen telt ruimte lager dan 1,50 m niet mee.

**Superficie útil**, de nuttige oppervlakte. Real Decreto 3148/1978
([BOE-A-1979-1217](https://www.boe.es/buscar/act.php?id=BOE-A-1979-1217), bewijstype 2):

> "Se entiende por superficie útil la del suelo de la vivienda, cerrada por el perímetro definido
> por la cara interior de sus cerramientos con el exterior o con otras viviendas o locales de
> cualquier uso. Asimismo incluirá la mitad de la superficie de suelo de los espacios exteriores de
> uso privativo de la vivienda tales como terrazas, miradores, tendederos, u otros hasta un máximo
> del diez por ciento de la superficie útil cerrada."

Dus: meet aan de **binnenkant**. Binnenmuren, dragende kolommen en leidingschachten groter dan
100 cm² gaan eraf, evenals ruimte lager dan 1,50 m. Terrassen tellen voor de helft mee, tot
maximaal 10 % van de gesloten nuttige oppervlakte.

Het Catastro noemt zijn eigen `sfc` in INSPIRE-termen `grossFloorArea`, brutovloeroppervlak. Dat
sluit één op één aan bij *construida*. Bewijstype 1, zelf gezien in het WFS-antwoord.

### Wat staat er in advertenties

De wet en de praktijk lopen uiteen, en dat is het punt.

**De wet eist útil.** Real Decreto 515/1989 over consumentenbescherming bij verkoop en verhuur van
woningen, artikel 4.3
([BOE-A-1989-11181](https://www.boe.es/buscar/act.php?id=BOE-A-1989-11181), bewijstype 2):
"Descripción de la vivienda con expresión de su superficie útil". De term *superficie construida*
komt in dat besluit niet voor. Deze plicht geldt voor wie beroepsmatig verkoopt, en gaat over de
informatie die ter beschikking moet staan — niet letterlijk over de kop van de advertentie.

**De praktijk geeft construida.** Vandaag zelf opgehaald via de officiële Idealista-assistent,
drie advertenties in Jávea (bewijstype 1 voor het ophalen, 6 voor de inhoud):

| Advertentie | Veld `size` | Wat de tekst zegt |
|---|---|---|
| 102601416, El Tosalet, Panorama | 432 | "cuenta con 432 m² construidos y 378,09 m² de espacio habitable" |
| 110085499, El Tosalet | 240 | "Con una superficie construida de 240 m2 y ubicada en una parcela de 1.100 m2" |
| 111643516, Calle Nadaleta 3 | 549 | geen m²-vermelding in de tekst |

De eerste advertentie is het bewijs in één regel: dezelfde makelaar noemt 432 m² *construidos* en
378,09 m² bewoonbaar, en het getal dat in het veld `size` terechtkomt is de 432. **Het getal dat je
op een portaal ziet is de superficie construida.**

### De rekenregel voor het model

378,09 / 432 = **87,5 %**. Bewijstype 5, één waarneming.

Uit R11 kwam een tweede paar: een advertentie in de Montgó noemde "superficie construida de 310 m²"
terwijl het kadaster 348 m² had. Dat is een andere vergelijking (advertentie tegen kadaster, niet
útil tegen construida), maar hij wijst dezelfde kant op: makelaars rapporteren meestal minder dan
het kadaster, en de getallen lopen 10 tot 15 % uiteen.

**Voorstel voor `tools/haalbaarheid.py`:**

- Reken opbrengst per m² altijd op **construida**, want de wijkprijzen in `kader/comparables.json`
  komen uit advertenties en zijn dus ook op construida gebaseerd. Consistent is belangrijker dan
  juist.
- Reken bouwkosten ook op construida, want aannemers in de Marina Alta offreren per m² gebouwd.
  [te verifiëren met een offerte van een aannemer]
- Bewaar per object wél beide getallen als ze er zijn, met het label erbij. Eén veld `m2` zonder
  label is de bron van de meeste rekenfouten.
- Vuistregel als alleen útil bekend is: construida ≈ útil / 0,875, dus circa **+14 %**. Eén
  waarneming, dus een werkhypothese. Markeer in het rapport als [te verifiëren].

### Wat we niet weten

De handleiding noemt "Superficie de los elementos comunes" als uitvoerveld van `Consulta_DNPRC`,
maar in geen van onze zes testantwoorden kwam zo'n veld voor — ook niet bij het appartement aan de
AV PARIS 10. Of de `sfc` van een appartement het aandeel in de gemeenschappelijke ruimten al
bevat, is daarmee **ONBEKEND**. Dat is voor Deal Hunter nu geen blokker, want we rekenen voorlopig
aan villa's en percelen, maar zodra er appartementen in het model komen moet dit uitgezocht worden.

---

## 8. Vraag 5 — staat het gebouw wel of niet in het kadaster

### Hoe je het vaststelt

Vier controles, alle vier gratis en in één ronde te doen:

1. **`sfc` = 0 en geen `lcons`.** Dan kent het kadaster geen bebouwing op dat perceel. Getest op
   2944017BC5924S, CL MAR AMARILLO 4: `sfc` 0, `luso` "Obras de urbanización y jardineria, suelos
   sin edificar", geen bouwdelen.
2. **WFS Buildings geeft niets.** `GetBuildingByParcel` op datzelfde perceel levert een
   `FeatureCollection` zonder één `featureMember`. Harde, eenduidige uitkomst. Bewijstype 1.
3. **Er staat wél iets op de luchtfoto.** Leg de perceelgrens uit de WFS over de PNOA-luchtfoto die
   het dashboard al toont. Ziet u een dak binnen de grens en geeft de WFS niets, dan is er een
   verschil.
4. **De advertentie noemt meer m² dan het kadaster.** De eenvoudigste en de vaakst bruikbare toets.

### Het verschil dat we vandaag vonden

Testobject `6442021BC5964S`, Calle Nadaleta 3, El Tosalet. Advertentie 111643516 van vandaag,
vraagprijs € 2.900.000 (eerder € 3.500.000), `size` 549 m². Het kadaster geeft **320 m²**, bouwjaar
2005, vier bouwdelen. Verschil: **229 m²**, ruim 70 % meer dan geregistreerd.

De advertentietekst beschrijft daarbij een gastenappartement met eigen badkamer en keuken, een
gym, een zomerkeuken met apparatuur, een verwarmd zwembad, een buitenbadkamer en een pergola voor
vier auto's.

**Wat dit is en wat het niet is.** Dit is een verschil tussen twee beschrijvingen, meer niet.
Verklaringen die geen enkele onregelmatigheid inhouden:

- de makelaar telt overdekte terrassen voor 100 % mee waar het kadaster ze voor 50 % telt;
- de makelaar telt de gastenwoning en de garage mee in één getal;
- er is uitgebouwd mét vergunning en de eigenaar heeft de aangifte bij het kadaster nog niet gedaan
  of die is nog in behandeling;
- de advertentie klopt gewoon niet.

Verklaringen die er wél toe doen voor een koper: er is uitgebouwd zonder vergunning, of de
uitbouw is zonder vergunning gebouwd en inmiddels verjaard. Welke van die zes het is, kan alleen
de gemeente zeggen. Wij zetten het in het dossier als **signaal**, nooit als conclusie, en nooit
in een tekst die naar buiten gaat.

### Waarom dit signaal in Jávea sterker is dan elders

Hier is het echte nieuws van deze ronde. **Jávea heeft een *regularización catastral* gehad**, de
ambtshalve opsporingsronde waarmee het Catastro niet-aangegeven bouwwerken alsnog inschrijft.

- Grondslag: disposición adicional tercera van het Texto Refundido de la Ley del Catastro
  Inmobiliario. Letterlijk: het gaat om "los supuestos de incumplimiento de la obligación de
  declarar de forma completa y correcta las circunstancias determinantes de un alta o modificación,
  con el fin de garantizar la adecuada concordancia de la descripción catastral de los bienes
  inmuebles con la realidad inmobiliaria."
  [BOE-A-2004-4163](https://www.boe.es/buscar/act.php?id=BOE-A-2004-4163), bewijstype 2.
- Kosten voor de eigenaar: "La cuantía de la tasa de regularización catastral será de **60 euros
  por inmueble** objeto del procedimiento." Idem, punt 8.d. De boete voor niet aangeven vervalt wel;
  de regularisatie sluit sancties uit.
- Jávea staat er met naam in: Resolución van 20-12-2016 van de Dirección General del Catastro,
  onder "Gerencia Territorial de Alicante … **Jávea/Xàbia** …", geldig tot 30-11-2017.
  [BOE-A-2016-12570](https://www.boe.es/diario_boe/txt.php?id=BOE-A-2016-12570), bewijstype 4,
  zelf in de BOE-tekst nagelezen.
- Verlengd tot 01-07-2018 bij Resolución van 11-07-2017
  ([BOE-A-2017-8506](https://www.boe.es/diario_boe/txt.php?id=BOE-A-2017-8506)) en daarna tot
  **31-12-2018** bij Resolución van 26-06-2018
  ([BOE-A-2018-8909](https://www.boe.es/diario_boe/txt.php?id=BOE-A-2018-8909), letterlijk:
  "ampliar hasta el 31 de diciembre de 2018 el plazo determinado"). Of er ná die datum nog is
  verlengd: **ONBEKEND**, niet gecontroleerd.

Gevolg voor onze weging: een uitbouw uit bijvoorbeeld 2008 die in 2026 nog steeds niet in het
kadaster staat, heeft een ronde van twee jaar ambtshalve controle overleefd. Dat maakt het signaal
zwaarder dan in een gemeente die nooit is doorgelicht. Omgekeerd geldt: staat de uitbouw er sinds
2017 wél in, dan kan dat juist het gevolg zijn van die ronde, en zegt de inschrijving niets over
een vergunning.

### De grens van wat het kadaster kan zeggen

Dit moet in elk dossier staan, want hier gaan kopers de mist in.

**Het kadaster is geen vergunningenregister.** Het beschrijft wat er staat, voor de belasting. Iets
kan keurig in het kadaster staan en toch zonder vergunning zijn gebouwd — de regularisatieprocedure
schrijft de werkelijkheid in, niet de legaliteit. En andersom kan iets met vergunning gebouwd zijn
en nog niet zijn aangegeven.

Wel is er een scharnier tussen de twee. Artikel 28.4 van de Ley de Suelo y Rehabilitación Urbana
(Real Decreto Legislativo 7/2015,
[BOE-A-2015-11723](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11723), bewijstype 2) regelt de
*declaración de obra nueva por antigüedad*, het inschrijven van een bouwwerk waarvoor de gemeente
niet meer kan optreden omdat de termijn is verlopen. Letterlijk:

> "en el caso de construcciones, edificaciones e instalaciones respecto de las cuales ya no proceda
> adoptar medidas de restablecimiento de la legalidad urbanística que impliquen su demolición, por
> haber transcurrido los plazos de prescripción correspondientes … Se inscribirán en el Registro de
> la Propiedad las escrituras de declaración de obra nueva que se acompañen de certificación
> expedida por el Ayuntamiento o por técnico competente, acta notarial descriptiva de la finca o
> **certificación catastral descriptiva y gráfica** de la finca, en las que conste la terminación
> de la obra en fecha determinada"

Het kadastrale uittreksel is dus een van de toegestane bewijsstukken voor de datum waarop het
gebouw af was. Daarom is de `ant` uit `Consulta_DNPRC` niet zomaar een jaartal: het is het getal
waarop een verjaringsverweer wordt gebouwd. Hoelang die termijn in de Comunitat Valenciana precies
is en wanneer hij níet loopt — bij beschermd landschap loopt hij niet af — staat in R12; zie daar,
en neem er geen aanname over mee in dit rapport.

De registrator moet bij zo'n inschrijving bovendien controleren dat er geen lopende
handhavingszaak op de *finca* is aangetekend en dat de grond niet publiek of met een openbare
erfdienstbaarheid belast is. Dat komt uit de *nota simple*, niet uit het kadaster.

**Conclusie voor het model:** het ontbreken van een gebouw in het kadaster is een sterk signaal om
de gemeente te bevragen, en het is een onderhandelingsargument. Het is geen bewijs, en wij
publiceren het niet.

---

## 9. Heel Jávea in één keer binnenhalen

### Via WFS: nee

Drie metingen, alle vandaag zelf gedaan:

| Gebied | Oppervlakte | Percelen | Grootte | Tijd | Uitkomst |
|---|---|---|---|---|---|
| Eén perceel op referentie | — | 1 | 2,9 KB | 0,14 s | HTTP 200 |
| bbox 38,7618–38,7623 / 0,1540–0,1547 | 0,004 km² | 7 | 16 KB | 0,37 s | HTTP 200 |
| bbox 38,760–38,775 / 0,150–0,165 | 2,2 km² | **953** | 2.089.786 bytes | 23,9 s | HTTP 200 |
| bbox 38,76–38,79 / 0,15–0,18 | 8,7 km² | — | 3,5 KB | **115,7 s** | **HTTP 500, "Runtime Error"** |

Uit R11 kwam daar nog bij: 486 percelen in circa 1 km², 1,09 MB, 12,1 s.

Dus: de praktische bovengrens van een WFS-bbox in Jávea ligt tussen 2,2 en 8,7 km². Daarboven valt
de dienst om met een kale ASP.NET-foutpagina, niet eens met een nette OGC-fout.

Verzachten kan niet:

- `ImplementsResultPaging` staat op **FALSE** in `GetCapabilities`. Er is geen paginering.
- `resulttype=hits` wordt **genegeerd**. Getest: het verzoek gaf gewoon alle zeven percelen met
  geometrie terug, 16.396 bytes. Je kunt dus niet eerst tellen en dan besluiten. Bewijstype 1.

Heel Jávea via WFS zou dus neerkomen op ongeveer dertig tot veertig aparte bbox-verzoeken van elk
20 tot 30 seconden, met dubbele percelen op de naden. Dat is geen oplossing, dat is een last voor
een gratis overheidsdienst.

### Via ATOM: ja, en het is licht

Drie bestanden, samen **22,5 MB**, twee keer per jaar ververst:

```
CP  A.ES.SDGC.CP.03082.zip    8.400.856 bytes
BU  A.ES.SDGC.BU.03082.zip   13.252.024 bytes
AD  A.ES.SDGC.AD.03082.zip      863.348 bytes
```

Alle drie `Last-Modified` 21-08-2026. Getest met een HEAD-verzoek; het downloaden zelf is
**bewust niet gedaan** zonder jouw akkoord.

Grove schatting van wat erin zit: in de WFS kost één perceel gemiddeld 2.193 bytes GML
(2.089.786 / 953). Een XML-zip comprimeert doorgaans acht tot twaalf keer, dus 8,4 MB komt neer op
grofweg 67 tot 101 MB uitgepakt, oftewel **orde van grootte 30.000 tot 45.000 percelen**.
Bewijstype 5, brede marge. De dichtheid in het geteste stedelijke vak was 438 percelen per km²;
over de hele gemeente van circa 68,6 km² [te verifiëren] zou dat ruim 30.000 zijn, maar het
Montgó-park heeft veel grotere percelen, dus de werkelijke dichtheid ligt lager. Een exact aantal
hebben we **niet** kunnen vaststellen; de statistiekpagina van het Catastro is een JavaScript-app
zonder downloadbare tabel.

**Mag het?** Ja.

- `Fees` in `GetCapabilities`: "No conditions apply".
- De ATOM-feed zelf: "This service can be used free of charge in every instance, as long as that
  the D. G. of the Cadastre (Ministry of Finance) is mentioned as author and owner of the
  information."
- De INSPIRE-pagina noemt de ATOM-dienst zelf "la descarga completa por municipios". Volledige
  download per gemeente is dus het bedoelde gebruik, niet een omweg.
- Geen van de vier Catastro-hosts heeft een `robots.txt`. Er zijn dus geen crawlregels die we
  zouden kunnen overtreden. Getest 18-09-2026.

Voorwaarde: **bronvermelding**. Elke kaart, tabel of export die hierop teruggaat krijgt de regel
"Bron: Dirección General del Catastro, geraadpleegd [datum]". En doorverkopen van de ruwe data mag
niet; bewerkte, afgeleide producten wel (Resolución 23-03-2011, zie 3.8).

### Wat ik aanraad

| Doel | Route | Belasting |
|---|---|---|
| Eén kandidaat beoordelen | `Consulta_DNPRC` + WFS per referentie | 4 verzoeken, < 2 s, 20 KB |
| Buren en samenvoegkansen | WFS `GetNeighbourParcel` | 1 verzoek |
| Wijkanalyse tot circa 2 km² | WFS bbox | 1 verzoek, 25 s, 2 MB |
| Heel Jávea, kaartlaag of zoekopdracht over alle percelen | ATOM, twee keer per jaar | 22,5 MB |
| Heel Jávea, actueel op de dag | bestaat niet, ATOM is het meest actueel | — |

De regel die we al hanteren blijft staan: maximaal één verzoek per seconde, antwoorden cachen op
de kadastrale referentie, en geen sweep over de gemeente met de losse webservices.

---

## 10. De valkuilen, alle zelf tegengekomen

| # | Valkuil | Gevolg als je hem mist | Oplossing |
|---|---|---|---|
| 1 | Certificaat van `www.catastro.hacienda.gob.es` | `curl` en `urllib` weigeren de verbinding | `httpx` gebruiken; nooit `-k` |
| 2 | `RefCat` tegenover `RC` | Lege of foute antwoorden | Nieuwe dienst met `RefCat`; oude ASMX heeft ook geen `ss` |
| 3 | `CoorX` is lengtegraad, `CoorY` is breedtegraad | Je zoekt in de Middellandse Zee | X = lon, Y = lat |
| 4 | Assenvolgorde in `EPSG::4326` GML is `lat lon` | Perceel op de verkeerde plek op de kaart | Omdraaien voor GeoJSON |
| 5 | Oppervlakte rekenen in graden | Uitkomst is onzin | Reken in `EPSG::25830` |
| 6 | `STOREDQUERIE_ID` met spelfout | HTTP 200 met een leeg antwoord | Precies zo overnemen |
| 7 | `numberOfFloorsAboveGround` is leeg op gebouwniveau | "Aantal bouwlagen onbekend" terwijl het er staat | `GetBuildingPartByParcel` gebruiken |
| 8 | Bij *división horizontal* geeft de referentie van 14 tekens foutcode 5 | Object wordt ten onrechte "niet gevonden" | Via `Consulta_DNPLOC` naar de referenties van 20 tekens |
| 9 | Bij `lrcdnp` in het antwoord ontbreekt `finca`, dus ook `ss` | Perceeloppervlakte lijkt te ontbreken | Eén referentie van 20 tekens uitvragen |
| 10 | `ss` van een appartement is het hele blok | Rekenmodel rekent met 726 m² grond voor één woning | Op `ltp` controleren |
| 11 | WFS negeert `resulttype=hits` | "Ik tel eerst even" kost 2 MB | Niet proberen |
| 12 | Een bbox van 8,7 km² geeft HTTP 500 na bijna 2 minuten | Vastgelopen import | Kleine bbox, of ATOM |
| 13 | De pin van een advertentie zonder adres is verschoven | Verkeerd perceel in het dossier | Zie hieronder |
| 14 | SOAP met verpakte parameters | "LA REFERENCIA CATASTRAL ES OBLIGATORIA" | Parameters los in de `Body` |

**Valkuil 13 uitgewerkt, want die kost echt geld.** Advertentie 102601416 in El Tosalet beschrijft
"432 m² construidos", bouwjaar 2016, perceel 3.063 m², wijk Panorama, en heeft `showAddress: false`.
De pin staat op 38,7425963 / 0,1987295. `Consulta_RCCOOR_Distancia` daarop geeft als dichtstbijzijnde
perceel 6817951BC5961N op 0 m, en als tweede 6621109BC5962S op 1,43 m. Uitvragen:

- 6817951BC5961N: 100.690 m², gemengd landbouw en stedelijk, geen bebouwing.
- 6621109BC5962S: 935 m², bouwjaar 1970, 112 m² bebouwd.

Geen van beide is de advertentie. De pin is dus verschoven, zoals het portaal ook aangeeft. Voor
advertenties met `showAddress: false` mag de koppeling pin → perceel **nooit** automatisch worden
vastgelegd. Alleen als de opgegeven perceeloppervlakte en het bouwjaar met het kadaster
overeenkomen, is de match zeker genoeg. Bewijstype 1.

---

## 11. Wat hiervan in Deal Hunter kan

Concreet, in volgorde van opbrengst per uur werk.

1. **`tools/kadaster.py`** met één functie `perceel(rc)` die het volledige beeld geeft:
   `ss`, `sfc`, `ant`, `ltp`, bouwdelen met verdieping en m², bouwlagen, voetafdruk, zwembad,
   GeoJSON. Het script in `onderzoek/N04-voorbeelden/kadaster_perceel.py` is de werkende basis en
   draait op de kale systeem-Python. Cache op referentie in de bestaande SQLite.

2. **Twee nieuwe kolommen in het dossier:** `m2_kadaster` en `m2_advertentie`, met het verschil in
   procenten ernaast. Kleur het verschil oranje boven 20 % en rood boven 50 %, met altijd de zin
   erbij: verschil is een signaal, geen oordeel; alleen de gemeente kan uitsluitsel geven.

3. **Perceelgrens op de kaart.** Het dashboard en `/m` tonen nu de Catastro-WMS als plaatje. Met de
   GeoJSON kun je de grens van het gekozen perceel echt tekenen, in de kleur van de beoordeling,
   plus het gebouw en het zwembad. Dat is de grootste zichtbare verbetering voor weinig werk.

4. **Bebouwingsgraad als vroeg filter.** Voetafdruk gedeeld door perceeloppervlakte. Bij het
   testobject 17,2 %. Een perceel van 1.500 m² met 8 % bebouwing en een bouwjaar vóór 1990 is een
   ander verhaal dan hetzelfde perceel met 30 %. Wat er mág komt uit R12, maar dit filter zeeft
   alvast.

5. **Zwembad, bouwjaar en bouwlagen in de renovatierekening.** `ant` bepaalt de bouwkundige
   uitgangssituatie; `conditionOfConstruction: ruin` is direct een andere categorie; een bestaand
   aangegeven zwembad scheelt een post in de begroting.

6. **Waarschuwing bij *división horizontal*.** Zodra `ltp` "Parcela con varios inmuebles" bevat,
   het rekenmodel laten stoppen met de melding dat `ss` het hele blok is.

7. **De ATOM-bestanden één keer binnenhalen** (22,5 MB) zodra er een vraag komt die over alle
   percelen gaat: "alle percelen boven 2.000 m² met minder dan 10 % bebouwing in Jávea".
   ⏸️ **ACTIE VOOR JAN:** ik heb de bestanden bewust niet gedownload. Zeg het als het mag, dan haal
   ik ze binnen en zet ik ze naast `data/dealhunter.sqlite`.

8. **Bronvermelding automatisch.** Elke kaart en elk rapport dat kadastergegevens toont, krijgt
   onderaan "Bron: Dirección General del Catastro, geraadpleegd [datum]". Dat is een licentieplicht,
   geen nettigheid.

---

## 12. Wat ONBEKEND blijft

1. Of de `sfc` van een appartement het aandeel in de gemeenschappelijke ruimten bevat. De
   handleiding noemt een uitvoerveld "Superficie de los elementos comunes"; het kwam in geen van
   onze antwoorden voor.
2. Het exacte aantal kadastrale percelen in Jávea. De statistiekpagina van het Catastro is een
   JavaScript-toepassing zonder downloadbare tabel, en `resulttype=hits` werkt niet. Schatting
   30.000 tot 45.000 (bewijstype 5).
3. De volledige tekst van de INSPIRE-licentie. De PDF is opgehaald maar niet machinaal leesbaar.
   Wij houden ons aan de wél leesbare regels: gratis, met bronvermelding.
4. Of er na 31-12-2018 nog verlengingen van de *regularización catastral* zijn geweest die Jávea
   raken.
5. Of het Catastro een formele limiet stelt aan het aantal verzoeken per seconde. In de
   handleiding versie 2.6 staat er niets over. Onze eigen rem van één per seconde is een keuze,
   geen voorschrift.
6. Of de verhouding útil/construida van 87,5 % representatief is. Eén waarneming.
7. Of `Consulta_DNPPP` bruikbaar is voor het landelijk gebied van Jávea zonder dat je de
   polígono- en parcela-nummers al kent. Onze ene test met een verzonnen nummerpaar gaf foutcode 5,
   wat verwacht was; een echte test vraagt een nummerpaar uit een *nota simple*.

---

## 13. Test- en bronnenregister

Alle tests uitgevoerd op 18-09-2026 vanaf de Mac mini. Tijden zijn eenmalige metingen.

### Geteste objecten in Jávea

| Referentie | Adres | `ss` | `sfc` | `ant` | Soort |
|---|---|---|---|---|---|
| `6442021BC5964S` | CL NADALETA 3 | 1.151 | 320 | 2005 | villa, 4 bouwdelen, zwembad |
| `0281206BC5908S` | CL PIC DE REBALSADORS 46 | 1.572 | 348 | 2006 | villa, 3 bouwdelen, zwembad |
| `3964301BC5937S` | CL DEL MESTRE JESUS MONTANER 8 | 822 | 341 | 1958 | centrumpand, 3 bouwlagen |
| `2944017BC5924S` | CL MAR AMARILLO 4 | 1.074 | 0 | — | onbebouwd perceel |
| `5656508BC5955N0003KL` | AV PARIS 10, Es 8, Pl 00, Pt 03 | 726 | 73 | 1970 | appartement, 87 in het blok |
| `6817951BC5961N0000UZ` | CR GUARDIA LA 676 | 100.690 | 0 | — | landbouw, 5 subparcelas |
| `6621109BC5962S` | UR COSTA NOVA PANORAMA 291 | 935 | 112 | 1970 | villa |

### Eindpunten

| Dienst | URL |
|---|---|
| Callejero en gegevens, JSON | `https://ovc.catastro.meh.es/OVCServWeb/OVCWcfCallejero/COVCCallejero.svc/json/…` |
| Idem, XML | `…/COVCCallejero.svc/rest/…` |
| Idem, SOAP | `…/COVCCallejero.svc/soap` |
| Idem, WSDL | `…/COVCCallejero.svc?singleWsdl` |
| Op codes in plaats van namen | `…/COVCCallejeroCodigos.svc/json/…` |
| Coördinaten | `…/COVCCoordenadas.svc/json/…` |
| Gevelfoto | `https://ovc.catastro.meh.es/OVCServWeb/OVCWcfLibres/OVCFotoFachada.svc/RecuperarFotoFachadaGet?ReferenciaCatastral=…` |
| WFS percelen | `https://ovc.catastro.meh.es/INSPIRE/wfsCP.aspx` |
| WFS gebouwen | `https://ovc.catastro.meh.es/INSPIRE/wfsBU.aspx` |
| WFS adressen | `https://ovc.catastro.meh.es/INSPIRE/wfsAD.aspx` |
| WMS | `https://ovc.catastro.meh.es/cartografia/INSPIRE/spadgcwms.aspx` |
| ATOM percelen, landelijk | `https://www.catastro.hacienda.gob.es/INSPIRE/CadastralParcels/ES.SDGC.CP.atom.xml` |
| ATOM percelen, Alicante | `…/CadastralParcels/03/ES.SDGC.CP.atom_03.xml` |
| ATOM gebouwen, Alicante | `…/buildings/03/ES.SDGC.BU.atom_03.xml` |
| ATOM adressen, Alicante | `…/Addresses/03/ES.SDGC.AD.atom_03.xml` |
| Kaartkijker per referentie | `https://www1.sedecatastro.gob.es/Cartografia/mapa.aspx?del=3&mun=82&refcat=…` |
| Massadownload (certificaat nodig) | `https://www.sedecatastro.gob.es/Accesos/SECAccDescargaDatos.aspx` |

### Documenten en wetteksten

| Bron | URL | Type |
|---|---|---|
| Handleiding vrije webservices v2.6 (09-10-2025) | https://www.catastro.hacienda.gob.es/ws/Webservices_Libres.pdf | 4 |
| INSPIRE-overzichtspagina Catastro | https://www.catastro.hacienda.gob.es/webinspire/index.html | 4 |
| INSPIRE-licentie (niet leesbaar) | https://www.catastro.hacienda.gob.es/webinspire/documentos/Licencia_en.pdf | 4 |
| RD 1020/1993, Norma 11.3, superficie construida | https://www.boe.es/diario_boe/xml.php?id=BOE-A-1993-19265 | 2 |
| RD 3148/1978, superficie útil | https://www.boe.es/buscar/act.php?id=BOE-A-1979-1217 | 2 |
| RD 515/1989 art. 4.3, informatie aan de koper | https://www.boe.es/buscar/act.php?id=BOE-A-1989-11181 | 2 |
| TRLCI (RDLeg 1/2004): art. 3, 11, 13, 18, DA 3ª | https://www.boe.es/buscar/act.php?id=BOE-A-2004-4163 | 2 |
| Ley de Suelo (RDLeg 7/2015) art. 28.4 | https://www.boe.es/buscar/act.php?id=BOE-A-2015-11723 | 2 |
| Regularización catastral, Jávea genoemd | https://www.boe.es/diario_boe/txt.php?id=BOE-A-2016-12570 | 4 |
| Verlenging tot 01-07-2018 | https://www.boe.es/diario_boe/txt.php?id=BOE-A-2017-8506 | 4 |
| Verlenging tot 31-12-2018 | https://www.boe.es/diario_boe/txt.php?id=BOE-A-2018-8909 | 4 |
| Resolución 23-03-2011, licentie massadownload | https://www.catastro.hacienda.gob.es/documentos/normativa/res_230311.pdf | 2 |
| Advertenties Jávea, opgehaald via de officiële Idealista-assistent | codes 111643516, 102601416, 110085499 | 6 |

### Bestanden bij dit rapport

| Pad | Inhoud |
|---|---|
| `/Users/root-admin/tree-es/deal-hunter/onderzoek/N04-voorbeelden/kadaster_perceel.py` | Werkend script, geen bibliotheken nodig |
| `/Users/root-admin/tree-es/deal-hunter/onderzoek/N04-voorbeelden/6442021BC5964S.geojson` | Uitvoer van dat script: perceel, gebouw, 5 bouwdelen, zwembad |

---

Bron van alle kadastrale gegevens in dit rapport: Dirección General del Catastro, Ministerio de
Hacienda, geraadpleegd 18-09-2026.

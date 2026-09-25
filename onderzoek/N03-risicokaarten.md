# N03 — Risico's en beperkingen per perceel: welke kaartdienst geeft antwoord

**Controledatum:** 18-09-2026. Alles wat hieronder "getest" heet, is op die dag zelf opgehaald vanaf de Mac mini.
**Stroom:** N03 · TREE Deal Hunter · vervolg op R11 (perceelidentificatie), R12 (urbanisme Xàbia) en R13 (geoportalen)
**Bewijstypen:** 1 = zelf getest of opgehaald · 2 = officiële wettekst of planvoorschrift · 3 = officiële kaart of database · 4 = officiële publicatie van een overheid · 5 = eigen afleiding of berekening · 6 = bericht van een marktpartij · 7 = onbekend of onbevestigd

## Testpunt

Alle voorbeeld-URL's in dit rapport zijn uitgevoerd op het punt uit de opdracht:

| | Waarde |
|---|---|
| Coördinaat | 38,7789 NB / 0,1660 OL (EPSG:4326) |
| Zelfde punt in EPSG:25830 (ETRS89 / UTM 30N) | 775031,106 / 4297003,252 |
| Zelfde punt in EPSG:3857 | 18479,035 / 4690050,197 |
| Kadastrale referentie (getest, bewijstype 1) | `03082A02500001` — Polígono 25, Parcela 1, CHOVAES, Jávea/Xàbia |
| Perceeloppervlak volgens Catastro (getest) | 43.447 m² |

Waar een laag op dit punt niets teruggeeft, is een tweede punt gebruikt om te bewijzen dát de laag antwoordt. Die controlepunten:

| Code | Coördinaat | EPSG:25830 | Waarvoor |
|---|---|---|---|
| P-B Granadella | 38,7312412 / 0,1934719 | 777602,9 / 4291796,0 | Natura 2000, bosgrond, brandinterface |
| P-C Montgó | 38,8045 / 0,1500 | 773542,9 / 4299796,9 | PORN en parque natural |
| P-D San Bartolomé | — | 774771 / 4298148 | BIC en entorno de protección |
| Kust Arenal (vlak) | — | bbox 776400,4296300,777200,4297000 | deslinde en servidumbre de protección |

De standaard-bevraging is steeds dezelfde: een vierkant van 100 m rond het punt, 101 bij 101 beeldpunten, en het middelste beeldpunt uitlezen (`I=50&J=50`). Zo weet je zeker dat je precies op de coördinaat kijkt en niet op de rand.

---

## Samenvatting in tien regels

1. Zeven van de acht risico's zijn per coördinaat automatisch te bevragen met officiële diensten die dat uitdrukkelijk toestaan. Alleen de archeologische vindplaatsen zijn dat niet — daar verbiedt de Generalitat het vrijgeven van locatiegegevens.
2. De Valenciaanse lagen (PATRICOVA, bosgrond, Natura 2000, PORN, planclassificatie, BIC/BRL) staan allemaal op `terramapas.icv.gva.es` of `carto.icv.gva.es`, onder CC BY 4.0 zonder gebruiksbeperking in de dienst zelf.
3. De landelijke lagen voor kust en water staan op `gis.miteco.gob.es`, eveneens CC BY 4.0, met in de dienst zelf de tekst "Sin limitaciones al acceso público".
4. **De oude MITECO-adressen (`wms.mapama.gob.es/sig/...`) werken niet meer.** Ze geven een NullReferenceException. Dat verklaart waarom R13 op 15-09 concludeerde dat de kustlagen onbereikbaar waren. De juiste adressen zijn nu GeoServer-adressen.
5. **Waarschuwing voor de bouw:** `gis.miteco.gob.es` is vanaf deze Mac niet met `curl` te bereiken — de TLS-handdruk wordt door de server verbroken (LibreSSL 3.3.6). Met Node 20 werkt hetzelfde verzoek wel. Bouw die aanroepen dus in Node, of onderzoek eerst een andere TLS-bibliotheek.
6. Het testperceel valt in PATRICOVA-gevarenniveau 4 en is tegelijk `SNU-C` (niet-bebouwbare grond, gewone landelijke zone, bosbestemming). Die combinatie sluit een nieuwe woning in beginsel uit; zie §1 en §6.
7. Het perceel ligt binnen de Q100-overstromingsvlak en binnen de zone van voorkeursstroming (ZFP) van de Riu Gorgos, maar buiten de 100 m-politiezone — die begint tussen 100 en 300 m verderop.
8. Op 900 tot 1.000 m van het punt loopt de **Colada de Cabañes**, een veedrift met een wettelijke breedte van 6 m, geclassificeerd op 27-01-1969 en nog niet ingemeten (`deslinde = No`). Over dit perceel loopt hij niet.
9. Xàbia heeft zijn kaart van de bos-bebouwingsgrens op **28-05-2026** door de gemeenteraad laten vaststellen. Vanaf die datum hebben eigenaren zes maanden om aan bijlage XI van de TRLOTUP te voldoen, dus tot ongeveer **28-11-2026**. Dat is een concrete kostenpost en een concrete deadline.
10. "Niets gevonden" is geen vrijbrief. Drie lagen geven structureel een misleidend antwoord: de brandinterface is een rasterkaart met cellen van ongeveer 500 m, de `BIC.Entornos` van de oude dienst is niet bevraagbaar, en de servidumbre de protección is geen vlak maar een lijn die je zelf moet vertalen naar een zone.

---

## De tabel

Voorbeeld-URL's staan hieronder ingekort tot de kern; de volledige, geteste URL staat per risico in het eigen hoofdstuk.

| # | Risico | Dienst | Exacte laagnaam | Type bevraging | Voorbeeld-URL (kern) | Getest 18-09 | Gebruiksrecht |
|---|---|---|---|---|---|---|---|
| 1 | Overstromingsgevaar PATRICOVA | ICV WMS `0701_InfraestructuraVerde` | `IVR.Inundacion` | WMS GetFeatureInfo | `terramapas.icv.gva.es/0701_InfraestructuraVerde?...LAYERS=IVR.Inundacion` | **ja** — niveau 4 | CC BY 4.0 Generalitat, "No se aplican condiciones" |
| 1b | PATRICOVA per niveau + risico | ICV ArcGIS `ordenacion_territorial` | lagen `2,4–10,12` | ArcGIS `identify` | `carto.icv.gva.es/arcgis/.../ordenacion_territorial/MapServer/identify` | **ja** — laag 7 en 12 | CC BY 4.0 (niet in de dienst vermeld, wel op icv.gva.es) |
| 1c | Landelijke controlekaart | IDEE WMS inundaciones | `NZ.Flood.FluvialT100` | WMS GetFeatureInfo | `servicios.idee.es/wms-inspire/riesgos-naturales/inundaciones` | **ja** — 0,962 | vrij, met vermelding MITECO |
| 2 | Bosgrond en terreno forestal estratégico | ICV WMS `0506_PATFOR` | `SF.Forestal`, `Forestal.Estrategico`, `Planeamiento.TFE` | WMS GetFeatureInfo | `terramapas.icv.gva.es/0506_PATFOR?...LAYERS=SF.Forestal` | **ja** — leeg op testpunt, raak op P-B | CC BY 4.0 Generalitat |
| 2b | Brandinterface (raster) | ICV WMS `0506_PATFOR` | `Regulacion.Incendios.Urbano` | WMS GetFeatureInfo | idem met `LAYERS=Regulacion.Incendios.Urbano` | **ja** — "1 - Sin interfaz" | CC BY 4.0 Generalitat |
| 2c | Gemeentelijke bos-bebouwingsgrens (DA 7) | ICV ArcGIS `prevencion_de_incendios` | laag `114` (Municipios interfaz), `112`, `113` | ArcGIS `query` | `carto.icv.gva.es/arcgis/.../prevencion_de_incendios/MapServer/114/query` | **ja** — Xàbia, Aprobado 28-05-2026 | CC BY 4.0 |
| 2d | Verplichte brandstrook van 30 m | **geen kaartlaag** — wettekst | TRLOTUP bijlage XI, punt 1 en 1.c | handmatig, per gebouw te berekenen | `boe.es/buscar/act.php?id=DOGV-r-2021-90283` | **ja** (tekst gelezen) | openbare wettekst |
| 3 | Natura 2000: ZEC, LIC, ZEPA | ICV WMS `0701_InfraestructuraVerde` | `IVR.ZEC`, `IVR.LIC`, `IVR.ZEPA` | WMS GetFeatureInfo | `terramapas.icv.gva.es/0701_InfraestructuraVerde?...LAYERS=IVR.ZEC` | **ja** — ES5213018 op P-B | CC BY 4.0 Generalitat |
| 3b | Parques naturales en overige ENP | ICV WMS `0701_InfraestructuraVerde` | `IVR.ParquesNaturales`, `IVR.ParajesNaturales`, `IVR.ReservasNaturales`, `IVR.PaisajesProtegidos`, `IVR.MonumentosNaturales` | WMS GetFeatureInfo | idem | **ja** — Montgó op P-C | CC BY 4.0 Generalitat |
| 3c | PORN en zonering Montgó | ICV WMS `0505_PORN` | `Montgo.PORN`, `Montgo.Zonificacion`, `Montgo.Parque` | WMS GetFeatureInfo | `terramapas.icv.gva.es/0505_PORN?...LAYERS=Montgo.Zonificacion` | **ja** — "Uso Moderado" op P-C | CC BY 4.0; laag is "carácter informativo" |
| 4 | Kust: deslinde en servidumbre de protección | MITECO GeoServer `costas` | `dominio_publico_maritimo_terrestre` (velden `tipo_linea` = "Límite DPMT aprobado" / "Límite SP aprobada") | WFS GetFeature met bbox | `gis.miteco.gob.es/geoserver/costas/dominio_publico_maritimo_terrestre/ows` | **ja** — DES01/13/03/0007 | CC BY 4.0 MITECO, "Sin limitaciones al acceso público" |
| 4b | Volledig getroffen percelen | MITECO GeoServer `costas` | `Servidumbre_Proteccion` | WMS/WFS | `gis.miteco.gob.es/geoserver/costas/Servidumbre_Proteccion/wms` | **ja** (capabilities) | idem |
| 5 | Waterloop: DPH, 5 m servidumbre, 100 m politiezone | MITECO GeoServer `agua` | `DPH_Estimado`, veld `tipo_zona` = "DPH Cartográfico" / "Zona de Servidumbre" / "Zona de Policía" | WFS met CQL `DWITHIN` | `gis.miteco.gob.es/geoserver/agua/DPH_Estimado/ows` | **ja** — alle drie op 100–300 m | CC BY 4.0 MITECO |
| 5b | Overstromingsvlakken en voorkeursstroming | MITECO GeoServer `agua` | `Zi_laminas_q10`, `Zi_laminas_q50`, `Zi_laminas_q100`, `Zi_laminas_q500`, `ZI_Laminas_ZFP`, `Zi_arpsi` | WMS GetFeatureInfo | `gis.miteco.gob.es/geoserver/agua/Zi_laminas_q100/wms` | **ja** — Q100 en ZFP raak | CC BY 4.0 MITECO |
| 5c | Barranco-geometrie zelf | ICV ArcGIS `ordenacion_territorial` | laag `3` (Red de Cauces) | ArcGIS `query` | `carto.icv.gva.es/arcgis/.../ordenacion_territorial/MapServer/3/query` | nee (wel in laagoverzicht gezien) | CC BY 4.0 |
| 6 | Planclassificatie SU / SUZ / SNU | ICV WMS/WFS `0702_Planeamiento` | `Planeamiento.Clasificacion` (velden `clas_suelo`, `zon_suelo`) | WMS GetFeatureInfo of WFS | `terramapas.icv.gva.es/0702_Planeamiento?...LAYERS=Planeamiento.Clasificacion` | **ja** — SNU-C / ZRC-FO | CC BY 4.0 Generalitat |
| 6b | Perceelgeometrie om het antwoord aan op te hangen | Catastro INSPIRE WFS | `GetParcel` op `refcat` | WFS stored query | `ovc.catastro.meh.es/INSPIRE/wfsCP.aspx?...refcat=03082A02500001` | **ja** — 43.447 m² | gratis; **massale download en tegelverzoeken verboden** |
| 6c | Landelijke planviewer SIU | Ministerio de Vivienda | — | — | hostnamen `visorsiu.*` lossen niet op | **nee** — ONBEKEND | ONBEKEND |
| 7 | Vías pecuarias | ICV ArcGIS `forestal` | laag `9` (Vías pecuarias), `8` (elementos), `44` (límites) | ArcGIS `query` met `distance` | `carto.icv.gva.es/arcgis/.../forestal/MapServer/9/query` | **ja** — Colada de Cabañes op 900–1.000 m | CC BY 4.0; laag is "sólo carácter informativo" |
| 8 | BIC, BRL en beschermingszones | ICV WMS `22_IGPCV` | `BIC`, `BRL`, `BIC.Entornos`, `BIC.Delimitaciones` | WMS GetFeatureInfo | `terramapas.icv.gva.es/22_IGPCV?...LAYERS=BIC.Entornos` | **ja** — raak op P-D | CC BY 4.0 Generalitat |
| 8b | Archeologische vindplaatsen | Conselleria de Cultura | — | **alleen handmatig, met toestemming** | `yacimientos.edu.gva.es` | **nee** — niet toegestaan | locatiegegevens niet openbaar |
| 8c | Gemeentelijke catálogo Xàbia | Ajuntament de Xàbia | — | **alleen handmatig** | CartOXàbia via `ajxabia.com` | **nee** — adres niet gevonden | ONBEKEND |

---

## 1. Overstromingsgevaar volgens PATRICOVA

### Wat het is

PATRICOVA is het regionale overstromingsplan van de Generalitat Valenciana. Het deelt het gebied in in zes gevarenniveaus plus een categorie "geomorfologisch gevaar". Het plan is bindend voor iedereen, niet alleen voor de overheid, en op niet-bebouwbare grond met niveau 2 tot en met 5 of met geomorfologisch gevaar zijn woningen verboden (PATRICOVA-normativa art. 18.2; overgenomen uit R13, bewijstype 2, controledatum 15-09-2026 — de officiële kaart- en normpagina staat op mediambient.gva.es en was op 18-09-2026 bereikbaar, bewijstype 4).

### Endpoint

| | |
|---|---|
| Dienst | `https://terramapas.icv.gva.es/0701_InfraestructuraVerde` (WMS 1.3.0 en WFS) |
| Laagnaam | `IVR.Inundacion` |
| Coördinatenstelsels | EPSG:25830, EPSG:4326, EPSG:3857 en meer (in GetCapabilities) |
| Antwoordformaten voor GetFeatureInfo | `text/plain`, `geojson`, `text/html`, `application/vnd.ogc.gml`, `text/xml` |
| Gebruiksrecht | `<Fees>No se aplican condiciones</Fees>`, `<AccessConstraints>CC BY 4.0 Generalitat</AccessConstraints>` — geautomatiseerd bevragen toegestaan |

**Geteste URL:**

```
https://terramapas.icv.gva.es/0701_InfraestructuraVerde?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetFeatureInfo&LAYERS=IVR.Inundacion&QUERY_LAYERS=IVR.Inundacion&CRS=EPSG:25830&BBOX=774981,4296953,775081,4297053&WIDTH=101&HEIGHT=101&I=50&J=50&INFO_FORMAT=text/plain&FEATURE_COUNT=10
```

**Antwoord op het testpunt (bewijstype 1):**

```
Layer 'IVR.Inundacion'
  Feature 739:
    codigo = 'AC07'
    zona = 'Riu de Xaló o de Gorgos'
    d_pelig = 'Peligrosidad 4. Frecuencia media (100 años) y calado bajo (<0.8 m)'
    n_pelig = '4'
    corriente = 'GORGOS'
    tipo = 'RIO'
    calado = '< 0.8 m'
    retorno = '100'
```

Het veld dat je in het systeem wilt vastleggen is `n_pelig` (de gevarenklasse, hier 4), met `d_pelig` als toelichting en `zona` als naam van het overstromingsgebied.

### Tweede weg: dezelfde vraag via ArcGIS

Als je liever één verzoek doet dat meteen álle PATRICOVA-lagen langsloopt, gebruik dan `identify` op de ArcGIS-dienst. Daar zitten de gevarenniveaus als aparte lagen in (2 = gevaar algemeen, 4 tot en met 9 = niveau 1 tot en met 6, 10 = geomorfologisch, 12 = risico, 3 = beeknetwerk).

```
https://carto.icv.gva.es/arcgis/rest/services/tm_infraestructuras/ordenacion_territorial/MapServer/identify?geometry=%7B%22x%22%3A775031.106%2C%22y%22%3A4297003.252%7D&geometryType=esriGeometryPoint&sr=25830&layers=all%3A2%2C4%2C5%2C6%2C7%2C8%2C9%2C10%2C12&tolerance=2&mapExtent=774931%2C4296903%2C775131%2C4297103&imageDisplay=400%2C400%2C96&returnGeometry=false&f=json
```

Antwoord op het testpunt: laag 7 ("Peligrosidad 4") tweemaal, en laag 12 ("Riesgo de Inundación") met `leyenda = Muy Bajo`. Laag 10, geomorfologisch gevaar, geeft niets. Let op het verschil tussen *peligrosidad* (kans dat het water komt) en *riesgo* (kans maal schade): niveau 4 met risico "muy bajo" betekent dat er nu weinig te beschadigen valt, niet dat er weinig water komt.

### Controle met de landelijke kaart

De nationale ARPSI-kaart van het IDEE geeft op hetzelfde punt voor T100 de waarde 0,962 (eenheid niet vermeld, vermoedelijk meter waterdiepte):

```
https://servicios.idee.es/wms-inspire/riesgos-naturales/inundaciones?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetFeatureInfo&LAYERS=NZ.Flood.FluvialT100&QUERY_LAYERS=NZ.Flood.FluvialT100&CRS=EPSG:25830&BBOX=774981,4296953,775081,4297053&WIDTH=101&HEIGHT=101&I=50&J=50&INFO_FORMAT=text/plain&FEATURE_COUNT=3
```

PATRICOVA zegt "calado < 0,8 m", de landelijke kaart 0,96. Dezelfde tegenstrijdigheid vond R13 op een ander punt. Leg beide getallen vast en laat een deskundige oordelen; ga niet zelf middelen.

---

## 2. Brandgevaar, terreno forestal estratégico en de brandstrook

Dit risico valt uiteen in vier vragen die elk hun eigen bron hebben. Dat is precies waar het in de praktijk misgaat.

### 2.1 Is het bosgrond?

| | |
|---|---|
| Dienst | `https://terramapas.icv.gva.es/0506_PATFOR` |
| Lagen | `SF.Forestal` (suelo forestal volgens PATFOR), `Forestal.Forestal`, `Forestal.Estrategico` en `Planeamiento.TFE` (terreno forestal estratégico) |
| CRS | EPSG:25830 en verder als bij PATRICOVA |
| Gebruiksrecht | CC BY 4.0 Generalitat |

```
https://terramapas.icv.gva.es/0506_PATFOR?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetFeatureInfo&LAYERS=SF.Forestal&QUERY_LAYERS=SF.Forestal&CRS=EPSG:25830&BBOX=774981,4296953,775081,4297053&WIDTH=101&HEIGHT=101&I=50&J=50&INFO_FORMAT=text/plain&FEATURE_COUNT=3
```

Op het testpunt: leeg. Op controlepunt P-B (Granadella), bbox `777553,4291746,777653,4291846`:

```
Layer 'SF.Forestal'        → forestal = 'FORESTAL', compatible = '1'
Layer 'Forestal.Estrategico' → produc = 'PRODUCTIVIDAD'
Layer 'Planeamiento.TFE'     → produc = 'PRODUCTIVIDAD'
```

`Forestal.Estrategico` en `Planeamiento.TFE` gaven op P-B exact hetzelfde object (7628). Het zijn dus twee ingangen op dezelfde gegevens; kies er één en vraag die op.

### 2.2 Ligt het in de bos-bebouwingsinterface?

`Regulacion.Incendios.Urbano` in dezelfde dienst geeft de interfaceklasse. **Dit is een rasterlaag.** Het antwoord bevat de coördinaat van het midden van de cel, en die lag op het testpunt 378 m in de x en 308 m in de y naast de opgevraagde coördinaat. Je krijgt dus een cel van ongeveer 500 m, geen perceeluitspraak.

Testpunt: `class = '1 - Sin interfaz'`. Controlepunt P-B: `class = '4 - Alta'`.

### 2.3 Staat het perceel op de gemeentelijke kaart van de bos-bebouwingsgrens?

Dit is de kaart die de TRLOTUP in disposición adicional séptima van elke gemeente met bosgrond eist. Hij bepaalt wie er verplichtingen heeft.

```
https://carto.icv.gva.es/arcgis/rest/services/tm_medio_ambiente/prevencion_de_incendios/MapServer/114/query?geometry=775031.106%2C4297003.252&geometryType=esriGeometryPoint&inSR=25830&distance=2000&units=esriSRUnit_Meter&spatialRel=esriSpatialRelIntersects&outFields=*&returnGeometry=false&f=json
```

Antwoord (bewijstype 1):

```json
{"cod_ine":"03082","municipio":"Jávea/Xàbia","estado":"Aprobado","fechapleno":1779926400000,"acplenario":"03082_Xàbia"}
```

`fechapleno` is een tijdstempel in milliseconden en staat voor **28-05-2026**. Laag 112 is "Instalaciones en riesgo", laag 113 "Áreas susceptibles de actuación"; beide gaven binnen 2 km van het testpunt niets.

### 2.4 Hoe breed is de verplichte brandstrook?

Hier is **geen kaartlaag** voor. Het staat in bijlage XI van de TRLOTUP, en het is rekenwerk per gebouw (bewijstype 2, wettekst zelf gelezen op boe.es op 18-09-2026):

- Algemene regel: een **faja perimetral de protección van minimaal 30 m breed**, gemeten vanaf de buitenrand van het gebouw of het samenstel van gebouwen.
- Tussen stedelijk terrein en bosvegetatie: een onderbreking ter breedte van een *área cortafuegos de orden dos*, met een **minimum van 25 m plus een weg van 5 m**. Die 5 m mag vervallen als aanleg onmogelijk is, mits er een strook van dezelfde breedte wordt afgeschraapt.
- Losstaande gebouwen op of grenzend aan bosgrond: een verdedigingszone van **minstens 30 m**, oplopend tot **minstens 50 m bij een helling van meer dan 30 %**. Verkleining tot de helft is mogelijk, maar alleen onderbouwd en met extra voorzieningen.

En de termijn: disposición adicional séptima, punt 10, geeft de verplichte partijen **zes maanden** vanaf de gemeentelijke vaststelling van de kaart. Voor Xàbia is dat 28-05-2026, dus **ongeveer 28-11-2026** (bewijstype 5, aanname dat de datum in de laag de raadsdatum is; te bevestigen bij het Ajuntament).

De eigenaar is de verplichte partij, en bij een vereniging van eigenaren is dat die vereniging. Punt 7 en 8 regelen bovendien een gedwongen erfdienstbaarheid: de verplichte partij mag het terrein van de buurman op om het werk te doen, tegen vergoeding. Voor de Deal Hunter betekent dat: bij elk object op of tegen bosgrond hoort een kostenregel voor de brandstrook, én een controle of de vorige eigenaar die al heeft aangelegd.

---

## 3. Beschermde natuur

Alle natuurlagen zitten in één dienst, dus je kunt ze in één verzoek meegeven in `LAYERS` en `QUERY_LAYERS`, gescheiden door komma's.

| | |
|---|---|
| Dienst | `https://terramapas.icv.gva.es/0701_InfraestructuraVerde` |
| Lagen Natura 2000 | `IVR.ZEC`, `IVR.LIC`, `IVR.ZEPA`, `IVR.ZEPIM` |
| Lagen beschermde gebieden | `IVR.ParquesNaturales`, `IVR.ParajesNaturales`, `IVR.ReservasNaturales`, `IVR.PaisajesProtegidos`, `IVR.MonumentosNaturales`, `IVR.Montes`, `IVR.ZonasHumedas`, `IVR.ZonasHumedas500m`, `IVR.Ramsar`, `IVR.Cavidades` |
| Overige nuttige lagen | `IVR.CorredoresTerritoriales`, `IVR.PaisajesRelevancia`, `IVR.TFEPATFOR` |
| Gebruiksrecht | CC BY 4.0 Generalitat |

Op het testpunt geven ZEC, LIC, ZEPA en ParquesNaturales alle vier niets. Op controlepunt P-B (Granadella) wel:

```
https://terramapas.icv.gva.es/0701_InfraestructuraVerde?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetFeatureInfo&LAYERS=IVR.ZEC&QUERY_LAYERS=IVR.ZEC&CRS=EPSG:25830&BBOX=777553,4291746,777653,4291846&WIDTH=101&HEIGHT=101&I=50&J=50&INFO_FORMAT=text/plain&FEATURE_COUNT=5
```

```
nombre = 'Penya-segats de la Marina'
codigo = 'ES5213018'
decreto = 'Decreto 197/2022, de 18 de noviembre'
leg_link = 'https://dogv.gva.es/datos/2022/11/28/pdf/2022_11078.pdf'
hectareas = '952.6'
municipio = 'XÀBIA; POBLE NOU DE BENITATXELL, EL; TEULADA'
```

`IVR.ZEPA` en `IVR.LIC` geven op datzelfde punt hetzelfde gebied met site_code ES5213018. Het veld `leg_link` verwijst rechtstreeks naar het besluit in de DOGV — dat is de bron die je in een dossier wilt hebben, niet de kaartlaag.

### PORN en parque natural

| | |
|---|---|
| Dienst | `https://terramapas.icv.gva.es/0505_PORN` |
| Lagen | `Montgo.PORN` (het PORN-gebied), `Montgo.Zonificacion` (de zonering), `Montgo.Parque` (het park zelf), `Montgo.ZonificacionSantAntoni` |

Op controlepunt P-C (in het park):

```
Montgo.PORN          → figura = 'Parque Natural', nombre = 'El Montgó',
                       legislacio = 'Decreto 180/2002, de 5 de noviembre'
Montgo.Zonificacion  → uso = 'Uso Moderado'
Montgo.Parque        → municipio = 'DÉNIA; XÀBIA / JÁVEA', figura_pro = 'PORN / PRUG'
```

De dienst zelf waarschuwt dat de PORN-begrenzing "carácter informativo" heeft. Gebruik de laag dus als zeef, en haal de harde begrenzing uit het decreet zodra een object echt in beeld komt.

---

## 4. Kustzone: deslinde en servidumbre de protección

### De wettelijke maat

De servidumbre de protección beslaat een strook van **100 m** landinwaarts vanaf de binnengrens van de *ribera del mar* (Ley 22/1988, art. 23.1). Die zone kan in overleg tot nog eens 100 m worden verruimd (art. 23.2). Op grond die bij de inwerkingtreding van de wet al als *suelo urbano* was geclassificeerd, is de breedte **20 m** (disposición transitoria tercera, punt 3). Alle drie de bepalingen zijn op 18-09-2026 in de geconsolideerde tekst op boe.es gelezen (bewijstype 2).

Dat verschil van 100 tegen 20 m maak je niet zelf uit. Daarom is de officieel vastgestelde lijn de enige bruikbare bron.

### Endpoint

| | |
|---|---|
| Dienst | `https://gis.miteco.gob.es/geoserver/costas/dominio_publico_maritimo_terrestre/` (WMS op `/wms`, WFS op `/ows`) |
| Laagnaam | `dominio_publico_maritimo_terrestre` |
| CRS | EPSG:25830, 25828, 25829, 25831, 4326, 4258, 3857, 32627 tot en met 32631, CRS:84 |
| Gebruiksrecht | `Fees: CC BY 4.0. Nombrar a la fuente: Ministerio para la Transición Ecológica y el Reto Demográfico`; `AccessConstraints: Sin limitaciones al acceso público` |

**Het is één laag met lijnen van verschillend soort.** Het veld `tipo_linea` vertelt welke:

- `Límite DPMT aprobado` (interne code `0801DPMT`) — de grens van het openbaar kustdomein zelf;
- `Límite SP aprobada` (interne code `0805DPMT`) — de buitengrens van de servidumbre de protección.

**Geteste URL (vlakbevraging over de Arenal):**

```
https://gis.miteco.gob.es/geoserver/costas/dominio_publico_maritimo_terrestre/ows?service=WFS&version=2.0.0&request=GetFeature&typeNames=dominio_publico_maritimo_terrestre&bbox=776400,4296300,777200,4297000,urn:ogc:def:crs:EPSG::25830&count=3&outputFormat=application/json&propertyName=tm,referencia,tipo_linea,sit_admin
```

**Antwoord (bewijstype 1):**

```json
[{"referencia":"DES01/13/03/0007","tm":"Jávea","sit_admin":"Aprobado (O.M. 27/04/2016)","tipo_linea":"Límite DPMT aprobado"},
 {"referencia":"DES01/13/03/0007","tm":"Jávea","sit_admin":"Aprobado (O.M. 27/04/2016)","tipo_linea":"Límite SP aprobada"},
 {"referencia":"DES01/13/03/0007","tm":"Jávea","sit_admin":"Aprobado (O.M. 27/04/2016)","tipo_linea":"Límite SP aprobada"}]
```

Voor Jávea geldt dus deslinde-dossier **DES01/13/03/0007**, goedgekeurd bij ministerieel besluit van 27-04-2016. De lijnen zijn er, mét het `vertices`-veld dat aangeeft of er gemeten hoekpunten bij zitten.

### Hoe je hier een perceeluitspraak van maakt

De dienst geeft lijnen, geen zones. Een puntbevraging op een lijn levert vrijwel altijd niets op. De werkwijze is dus:

1. Haal met één WFS-verzoek de `Límite SP aprobada`-lijnen binnen een kilometer rond het perceel op.
2. Bepaal aan welke kant van die lijn het perceel ligt (landzijde of zeezijde). Ligt het aan de zeezijde, dan zit het perceel in de servidumbre de protección.
3. Leg daarnaast de `Límite DPMT aprobado` — grond die daarbinnen valt is openbaar domein en niet in privé-eigendom te hebben.

Er is nog een tweede dienst, `https://gis.miteco.gob.es/geoserver/costas/Servidumbre_Proteccion/wms`, laag `Servidumbre_Proteccion`. Die bevat volgens de eigen omschrijving alleen **vlakken van kleine terreinen, meestal eilandjes, die door hun geringe omvang volledig binnen de servidumbre vallen** en waar een lijn dus niet te tekenen is. Het is geen algemene zonekaart. Niet verwarren.

### Waarschuwing over het oude adres

`https://wms.mapama.gob.es/sig/Costas/DPMT` en de varianten `/SP`, `/NucleosExcluidos`, `/TerrenosIncluidos` geven op 18-09-2026 nog steeds een `ServiceException` met een NullReferenceException uit de ASP.NET-laag. Die adressen zijn dood. Gebruik de GeoServer-adressen hierboven.

---

## 5. Waterlopen: barrancos, 5 m servidumbre en 100 m politiezone

### De wettelijke maat

De oevers van openbare waterlopen zijn over hun hele lengte onderworpen aan een **zone van servidumbre van 5 m breed** voor openbaar gebruik en aan een **zone de policía van 100 m breed** waarin het grondgebruik en de activiteiten aan voorwaarden zijn gebonden (Texto Refundido de la Ley de Aguas, RDL 1/2001, art. 6.1.a en 6.1.b, gelezen op boe.es op 18-09-2026, bewijstype 2). Bij een monding in zee of bij bijzondere topografie kan die breedte worden gewijzigd (art. 6.2).

### Endpoint — en dit is de vondst van dit rapport

De Confederación Hidrográfica del Júcar heeft een eigen WMS-park op `siajucar.chj.es`, maar dat bevat **geen** laag met het DPH of de zones (156 kaarten doorgenomen; de enige overstromingskaarten daar zijn ARPSI en tramos-inventarissen). Wat je nodig hebt staat bij het ministerie, en het staat allemaal in één laag:

| | |
|---|---|
| Dienst | `https://gis.miteco.gob.es/geoserver/agua/DPH_Estimado/` (WMS op `/wms`, WFS op `/ows`) |
| Laagnaam | `DPH_Estimado` |
| Onderscheid via veld | `tipo_zona` = `DPH Cartográfico` / `Zona de Servidumbre` / `Zona de Policía` |
| Veld `hipotesis` | `Máxima Crecida Ordinaria / Geomorfología` · `Buffer 5 m desde DPH` · `Buffer 100 m desde DPH` |
| Geometriekolom (voor CQL) | `shape` |
| Gebruiksrecht | CC BY 4.0 MITECO |

**Geteste URL (afstand tot het punt, 300 m):**

```
https://gis.miteco.gob.es/geoserver/agua/DPH_Estimado/ows?service=WFS&version=2.0.0&request=GetFeature&typeNames=DPH_Estimado&outputFormat=application/json&count=10&propertyName=id_zona,tipo_zona,zona,rio&cql_filter=DWITHIN(shape,POINT(38.7789%200.1660),300,meters)
```

**Antwoord:** `DPH Cartográfico`, `Zona de Policía` en `Zona de Servidumbre`, alle drie voor `70.30 RIU XALO O GORGOS`, Río Gorgos. Bij 100 m: niets. Het perceel ligt dus **buiten** de politiezone, maar die begint tussen 100 en 300 m verderop.

Wil je alleen weten of het punt zélf erin ligt, vervang `DWITHIN(...)` door `INTERSECTS(shape,POINT(38.7789 0.1660))`. Dat gaf hier nul objecten.

### Twee valkuilen die uren kosten

1. **De coördinaatvolgorde in een CQL-filter is breedtegraad eerst.** `POINT(38.7789 0.1660)` werkt; `POINT(0.1660 38.7789)` geeft stil nul objecten. Hetzelfde geldt voor `BBOX(...)` in een CQL-filter. In de gewone `bbox=`-parameter van WFS mag je wél projecteerde coördinaten met een expliciete CRS-urn meegeven, zoals hierboven bij de kust.
2. **De laag is niet in EPSG:25830 opgeslagen maar in graden.** Een CQL-filter met UTM-coördinaten geeft geen foutmelding, alleen nul resultaten. Dat is het gevaarlijkste soort antwoord.

### Overstromingsvlakken erbij

Dezelfde GeoServer heeft de overstromingsvlakken per herhalingstijd en de zone van voorkeursstroming:

| Laag | Dienstpad |
|---|---|
| `Zi_laminas_q10` | `/geoserver/agua/Zi_laminas_q10/wms` |
| `Zi_laminas_q50` | `/geoserver/agua/Zi_laminas_q50/wms` |
| `Zi_laminas_q100` | `/geoserver/agua/Zi_laminas_q100/wms` |
| `Zi_laminas_q500` | `/geoserver/agua/Zi_laminas_q500/wms` |
| `ZI_Laminas_ZFP` | `/geoserver/agua/ZI_Laminas_ZFP/wms` |
| `Zi_arpsi` | `/geoserver/agua/Zi_arpsi/wms` |

```
https://gis.miteco.gob.es/geoserver/agua/Zi_laminas_q100/wms?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetFeatureInfo&LAYERS=Zi_laminas_q100&QUERY_LAYERS=Zi_laminas_q100&CRS=EPSG:25830&BBOX=774981,4296953,775081,4297053&WIDTH=101&HEIGHT=101&I=50&J=50&INFO_FORMAT=text/plain&FEATURE_COUNT=5
```

Antwoord op het testpunt: `id_zona = ES080_T100_301`, `zona = 70.30 RIU XALO O GORGOS`, `rio = Río Gorgos`, studie "SNCZI. Zonas Inundables del Sistema Marina Alta", vastgesteld 31-10-2011, `q_m3_s = 863,119`. De ZFP-laag geeft op hetzelfde punt `ES080_ZFP_301`.

Gebruik voor deze lagen `INFO_FORMAT=text/plain` en niet `application/json`: de polygonen hebben duizenden punten en een JSON-antwoord wordt dan onwerkbaar groot. Bij `text/plain` geeft GeoServer alleen de kenmerken, met de geometrie samengevat als `[GEOMETRY (Polygon) with 3459 points]`.

Wie de beek zelf als lijn wil, kan laag 3 ("Red de Cauces") van de ICV-dienst `ordenacion_territorial` gebruiken. Die is in dit onderzoek niet bevraagd.

---

## 6. Planologische klasse van de grond

| | |
|---|---|
| Dienst | `https://terramapas.icv.gva.es/0702_Planeamiento` (WMS 1.3.0 en WFS 1.1.0) |
| Lagen | `Planeamiento.Clasificacion`, `Planeamiento.Zonificacion`, `Planeamiento.Dotaciones`, `Planeamiento.ElementosSingulares`, `InventarioSuSuz`, `MinimizacionViviendasSNU`, `DeclaracionInteresComunitario` |
| Velden die ertoe doen | `clas_suelo` (SU, SUZ, SNU-C, SNU-P), `zon_suelo`, `descripcio`, `denominaci`, `cod_ine_mun` |
| Gebruiksrecht | `Fees: No se aplican condiciones`, `AccessConstraints: CC BY 4.0 Generalitat` |

```
https://terramapas.icv.gva.es/0702_Planeamiento?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetFeatureInfo&LAYERS=Planeamiento.Clasificacion&QUERY_LAYERS=Planeamiento.Clasificacion&CRS=EPSG:25830&BBOX=774981,4296953,775081,4297053&WIDTH=101&HEIGHT=101&I=50&J=50&INFO_FORMAT=text/plain&FEATURE_COUNT=3
```

Antwoord op het testpunt:

```
cod_ine_mun = '03082'      noms_mun = 'Xàbia/Jávea'
denominaci  = 'Plan general'
clas_suelo  = 'SNU-C'
zon_suelo   = 'ZRC-FO'
descripcio  = 'Zona rural común forestal'
```

Wil je het vlak zelf in plaats van één punt, dan werkt WFS met een bbox in EPSG:25830 (getest, geeft één object):

```
https://terramapas.icv.gva.es/0702_Planeamiento?SERVICE=WFS&VERSION=1.1.0&REQUEST=GetFeature&TYPENAME=Planeamiento.Clasificacion&SRSNAME=EPSG:25830&BBOX=775021,4296993,775041,4297013,EPSG:25830&MAXFEATURES=3
```

### Het perceel eronder

De klasse hangt aan een vlak, niet aan een pin. Haal daarom eerst de kadastrale referentie en de perceelgrens op (bewijstype 1, beide getest):

```
https://ovc.catastro.meh.es/ovcservweb/OVCSWLocalizacionRC/OVCCoordenadas.asmx/Consulta_RCCOOR?SRS=EPSG:4326&Coordenada_X=0.1660&Coordenada_Y=38.7789
```

geeft `03082A0` + `2500001` en de omschrijving "Polígono 25 Parcela 1 CHOVAES. JAVEA/XABIA (ALICANTE)". Daarna:

```
https://ovc.catastro.meh.es/INSPIRE/wfsCP.aspx?service=wfs&version=2.0.0&request=getfeature&STOREDQUERIE_ID=GetParcel&refcat=03082A02500001&srsname=EPSG::25830
```

geeft de geometrie en `areaValue = 43447 m²`. Het gebruiksrecht van de Catastro-WMS staat in de dienst zelf: *"Acceso libre, pero se prohíbe la descarga masiva de porciones de cartografía y peticiones teseladas."* Vraag dus per perceel op, met een wachttijd tussen de verzoeken, en bewaar het antwoord in de eigen database. Dat doet het dashboard al zo (één verzoek per seconde, gecachet).

### Wat deze laag níet zegt

Twee dingen, en ze zijn allebei belangrijk voor Jávea.

De laag geeft "Plan general" als bron. Voor Xàbia is het geldende plan het PGOU van 1990, dat sinds 2021 gedeeltelijk is geschorst, met Normas Urbanísticas Transitorias de Urgencia erbovenop waarvan het onzeker is of ze na maart 2025 nog gelden. R12 heeft dat uitgezocht en houdt het op bewijstype 7. De kaartlaag zegt daar niets over. Een uitslag `SNU-C` uit deze laag is dus een signaal, geen bouwrecht.

En: het landelijke alternatief ontbreekt. De hostnamen van de SIU-viewer (`visorsiu.fomento.es`, `visorsiu.mivau.gob.es`, `visorsiu.transportes.gob.es`) lossen op 18-09-2026 geen van alle op in DNS, en de ministeriële pagina die de nieuwe adressen zou geven antwoordt met HTTP 403. **ONBEKEND** waar de SIU-dienst nu staat.

### Combinatie op het testperceel

`SNU-C` plus PATRICOVA-niveau 4 is geen neutrale uitkomst. Op niet-bebouwbare grond met gevaarniveau 2 tot en met 5 verbiedt PATRICOVA woningbouw (art. 18.2 van de normativa; overgenomen uit R13, bewijstype 2, controledatum 15-09-2026, opnieuw te bevestigen in de normtekst zelf vóór het in een dossier gaat). Voor dit perceel van 4,34 ha betekent dat: een nieuwe *vivienda aislada* is in beginsel uitgesloten, ondanks dat de oppervlakte ruim boven het minimum van 1 ha uit TRLOTUP art. 211.1.b ligt. Dat is precies het soort conclusie waar deze automatisering voor bedoeld is: hij komt vóór de rekensom, niet erna.

---

## 7. Vías pecuarias

### Wat het is

Veedriften zijn openbaar domein: **onvervreemdbaar, onverjaarbaar en niet voor beslag vatbaar** (Ley 3/1995, art. 2). Ze verdwijnen dus niet doordat er al dertig jaar een muur overheen staat. De breedte hangt af van het soort: een *cañada* is maximaal 75 m, een *cordel* maximaal 37,5 m en een *vereda* maximaal 20 m (art. 4.1). Bij een *colada* wordt de breedte bepaald door het classificatiebesluit zelf (art. 4.3). Alles gelezen op boe.es op 18-09-2026 (bewijstype 2).

### Endpoint

| | |
|---|---|
| Dienst | `https://carto.icv.gva.es/arcgis/rest/services/tm_medio_ambiente/forestal/MapServer` |
| Lagen | `9` — Vías pecuarias (lijnen) · `8` — Elementos pecuarios · `44` — Límites · `7` — groepslaag, niet bevraagbaar |
| Bevraging | ArcGIS REST `query` met `geometry`, `inSR`, `distance` en `units` |
| Sleutelvelden | `nomb_vp`, `tipo_leyen`, `legal_1` (wettelijke breedte in meters), `munic_1`, `deslinde`, `aproba_1`, `boe_1`, `long_desli` |
| Gebruiksrecht | CC BY 4.0 volgens icv.gva.es; de ICV-viewer vermeldt bij deze laag uitdrukkelijk: *"La cartografía de vías pecuarias … sólo tiene carácter informativo."* |

**Geteste URL:**

```
https://carto.icv.gva.es/arcgis/rest/services/tm_medio_ambiente/forestal/MapServer/9/query?geometry=775031.106%2C4297003.252&geometryType=esriGeometryPoint&inSR=25830&distance=1000&units=esriSRUnit_Meter&spatialRel=esriSpatialRelIntersects&outFields=nomb_vp%2Cmunic_1%2Clegal_1%2Ctipo_leyen%2Cdeslinde%2Caproba_1&returnGeometry=false&f=json
```

**Antwoord:**

```json
{"nomb_vp":"Colada de Cabañes","munic_1":"Xàbia/Jávea","legal_1":"6",
 "tipo_leyen":"Colada","deslinde":"No","aproba_1":"27/01/1969"}
```

Met `distance=900` komen er nul objecten terug, met `distance=1000` één. De veedrift loopt dus op 900 tot 1.000 m van het testpunt, niet over het perceel.

Twee dingen om vast te leggen bij elk object: `legal_1` (hier 6 m, want een colada) en `deslinde`. Staat daar `No`, dan is de veedrift nooit officieel ingemeten en is de getekende lijn een benadering. Dat is geen geruststelling maar het tegendeel — bij een latere *deslinde* kan de strook ergens anders blijken te liggen dan op de kaart. Doe de bevraging daarom met een ruime marge, bijvoorbeeld 100 m rond de perceelgrens, en niet alleen op de perceelgrens zelf.

---

## 8. Archeologische en cultuurhistorische bescherming

Hier lopen twee dingen uiteen die vaak op één hoop gaan.

### 8.1 Gebouwd erfgoed: wél automatisch te bevragen

De Generalitat heeft in juni 2024 nieuwe adressen gepubliceerd voor de erfgoeddiensten. De oude ArcGIS-WmsServer-adressen onder `tm_cultura` zijn buiten dienst.

| | |
|---|---|
| Dienst | `https://terramapas.icv.gva.es/22_IGPCV` (WMS), `https://terramapas.icv.gva.es/22_IGPCV_wfs` (WFS) |
| Lagen | `BIC` (Bien de Interés Cultural, punten) · `BIC.Entornos` (beschermingszones, vlakken) · `BIC.Delimitaciones` (begrenzingen) · `BRL` (Bien de Relevancia Local) |
| Gebruiksrecht | CC BY 4.0 Generalitat |

**Geteste URL (controlepunt P-D, Iglesia de San Bartolomé):**

```
https://terramapas.icv.gva.es/22_IGPCV?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetFeatureInfo&LAYERS=BIC.Entornos&QUERY_LAYERS=BIC.Entornos&CRS=EPSG:25830&BBOX=774721,4298098,774821,4298198&WIDTH=101&HEIGHT=101&I=50&J=50&INFO_FORMAT=text/plain&FEATURE_COUNT=3
```

**Antwoord:**

```
codigo = '1697'
denominacion = 'Iglesia Parroquial de San Bartolomé Apóstol'
noms_mun = 'Xàbia/Jávea'
categoria = 'Monumento'
ficha = 'https://cultura.gva.es/.../ficha-inmueble.php&id=1697&lang=es'
```

Op het testpunt geven `BIC`, `BIC.Entornos`, `BIC.Delimitaciones` en `BRL` alle vier niets.

De `entornos de protección` zijn hier belangrijker dan de monumenten zelf. Een perceel dat niet zelf beschermd is maar wel binnen de beschermingszone van een BIC ligt, krijgt bij elke verbouwing een extra toets. Gebruik daarom de **nieuwe** dienst `22_IGPCV` en niet de erfgoedlagen in `0701_InfraestructuraVerde`: daar is `IVR.Cultura.BIC.Entornos` als `queryable="0"` gepubliceerd, zodat een GetFeatureInfo de foutmelding `LayerNotDefined` geeft en een naïef script concludeert dat er niets ligt. Via WFS is diezelfde laag wel op te halen, maar dat is een omweg zonder reden.

### 8.2 Archeologische vindplaatsen: niet automatisch, en dat is beleid

De Conselleria de Cultura stelt op haar eigen pagina dat de administratie de locatiegegevens van archeologische vindplaatsen **niet mag verstrekken aan wie daartoe niet bevoegd is**: *"la administración no puede facilitar la consulta de datos relativos a la situación de los yacimientos arqueológicos si no se está debidamente autorizado."* En: *"los resultados de la consulta tienen carácter informativo y provisional"*, omdat de inventaris doorlopend wordt bijgewerkt (geraadpleegd 18-09-2026, bewijstype 4).

Er zijn drie ingangen: een openbare beperkte raadpleging, een volledige raadpleging met wachtwoord, en de toepassing zelf op `https://yacimientos.edu.gva.es`. Voor ons betekent dat:

- **Geen geautomatiseerde bevraging.** Niet omdat het technisch niet kan, maar omdat het niet mag.
- **Wel een handmatige stap in het dossier.** Bij elk object dat serieus wordt: openbare raadpleging doen, en bij een perceel in landelijk gebied of in de oude kern een schriftelijke bevestiging vragen.
- ⏸️ **ACTIE VOOR JAN:** overweeg of TREE de toestemming voor volledige raadpleging aanvraagt. Dat scheelt per dossier een wachttijd, en het is de enige manier om deze controle voorspelbaar te maken. Welk formulier daarvoor geldt, is nog niet uitgezocht — ONBEKEND.

### 8.3 Gemeentelijke catalogus Xàbia: handmatig

Xàbia heeft sinds februari 2018 een eigen kaartviewer, **CartOXàbia**, waarin het plangebied en de stedenbouwkundige omstandigheden per perceel zijn op te zoeken, zonder registratie. Het exacte adres van die viewer is in dit onderzoek niet gevonden: `cartoxabia.ajxabia.com` en `cartografia.ajxabia.com` lossen niet op, en `ajxabia.com/cartoxabia` geeft 404. **ONBEKEND.** De aankondiging staat op `https://www.ajxabia.com/ver/7175/urbanismo-hace-publica-la-nueva-cartografia-municipal-de-xabia-en-la-web-del-ayuntamiento.html` (bewijstype 4).

Tot dat adres bekend is, loopt de gemeentelijke *catálogo de bienes y espacios protegidos* via de afdeling Urbanisme van het Ajuntament. Die weg is sowieso nodig voor het formele *informe urbanístico* (TRLOTUP art. 246.4), en dat document is uiteindelijk het enige dat telt.

---

## De werkwijze per perceel

Zo zou een controle er in het systeem uit moeten zien. Twaalf verzoeken, ongeveer, en met caching per perceel maar één keer.

1. **Punt naar perceel.** `Consulta_RCCOOR` voor de kadastrale referentie, dan de INSPIRE-WFS voor de geometrie. Vanaf hier werk je met een vlak, niet met een pin. Van de 40 objecten met coördinaten in de BP-feed hadden er volgens R13 al vier een onbruikbare pin; dat probleem lost deze stap op.
2. **Harde uitsluiters eerst.** PATRICOVA (`IVR.Inundacion`), planclassificatie (`Planeamiento.Clasificacion`), Natura 2000 (`IVR.ZEC`, `IVR.LIC`, `IVR.ZEPA`) en PORN (`Montgo.Zonificacion`). Vier verzoeken, en samen bepalen ze of er überhaupt iets kan.
3. **Zones met afstand.** DPH en de 5 m- en 100 m-zones via CQL `DWITHIN` op `DPH_Estimado`, veedriften via `distance` op de forestal-laag 9, en langs de kust de deslindelijnen via bbox. Doe dit met een marge van 100 m rond de perceelgrens, niet op één punt.
4. **Kosten en termijnen.** Bosgrond (`SF.Forestal`), interface (`Regulacion.Incendios.Urbano`) en de gemeentelijke kaart (laag 114). Is de gemeente "Aprobado", zet dan de brandstrook als kostenregel in de rekensom.
5. **Erfgoed.** `22_IGPCV` met `BIC`, `BIC.Entornos` en `BRL`.
6. **Vlag zetten voor handwerk.** Archeologie altijd, gemeentelijke catalogus altijd, en het *informe urbanístico* zodra het object op de shortlist komt.

Leg per bevraging vast: de volledige URL, het tijdstip, de ruwe uitslag en de laagnaam. Een risicoscore zonder die vier dingen is in een onderhandeling waardeloos.

### Drie regels voor de bouw

**Gebruik `text/plain`, niet `geojson`.** De vlakken van PATRICOVA en de overstromingskaarten hebben duizenden hoekpunten. Het geojson-antwoord op het testpunt was 12.937 bytes, hetzelfde antwoord in text/plain 1.101 bytes in 37 regels (beide gemeten). Bij de MITECO-waterlagen loopt dat verder uiteen: één polygoon daar heeft 3.459 punten.

**Ga niet uit van één coördinatenstelsel.** EPSG:25830 werkt in de bbox-parameter van alle geteste diensten. Maar in een CQL-filter op de MITECO-lagen moet je graden gebruiken, met de breedtegraad eerst. Een verkeerd stelsel geeft geen foutmelding maar een leeg antwoord, en dat is in een geautomatiseerde zeef het gevaarlijkste wat er is. Bouw daarom per laag een vaste testcoördinaat in waarvan je weet dat hij raak is, en laat het systeem alarm slaan als die test ineens leeg terugkomt.

**Wees zuinig met verzoeken.** Geen enkele dienst noemt een limiet, maar Catastro verbiedt uitdrukkelijk massale download en tegelverzoeken, en de rest zijn overheidsservers zonder commerciële capaciteit. Eén verzoek per seconde per dienst, antwoorden bewaren, en per perceel hooguit één keer per kwartaal opnieuw ophalen.

### Het netwerkprobleem op deze Mac

`gis.miteco.gob.es` verbreekt de TLS-handdruk met de curl van macOS (LibreSSL 3.3.6): `Recv failure: Connection reset by peer`, meteen na het Client Hello. Python 3.9 uit de Command Line Tools geeft dezelfde fout. Node 20 doet hetzelfde verzoek wel goed en kreeg alle antwoorden in dit hoofdstuk binnen. Voor de kust- en waterlagen moet de koppeling dus via Node lopen, of via een andere TLS-bibliotheek. Ook `https://gis.miteco.gob.es/robots.txt` is om die reden niet op te halen — ONBEKEND wat daarin staat. De diensten zelf verklaren in hun GetCapabilities "Sin limitaciones al acceso público" en CC BY 4.0, en dat is de uitspraak van de aanbieder zelf over zijn eigen dienst.

### Wat robots.txt zegt

| Host | robots.txt | Gevolg |
|---|---|---|
| `terramapas.icv.gva.es` | HTTP 404 | geen beperking |
| `carto.icv.gva.es` | HTTP 404 | geen beperking |
| `ovc.catastro.meh.es` | HTTP 404; de dienst zelf verbiedt massale download en tegelverzoeken | per perceel opvragen, niet in bulk |
| `www.miteco.gob.es` | `User-agent: * / Crawl-delay: 10 / Disallow: /*?` | de wébsite niet met parameters crawlen; dit raakt de geoservers op de andere host niet |
| `gis.miteco.gob.es` | niet op te halen (verbinding verbroken) | ONBEKEND; de diensten verklaren zelf vrij gebruik |
| `servicios.idee.es` | niet op te halen | ONBEKEND |
| `www.chj.es` | HTTP 404 | geen beperking |

---

## Wat alleen handmatig kan

| Onderwerp | Waarom | Directe link |
|---|---|---|
| Archeologische vindplaatsen | De Generalitat mag locatiegegevens niet vrijgeven zonder toestemming | https://yacimientos.edu.gva.es · toelichting op https://cultura.gva.es/es/web/patrimonio-cultural-y-museos/arqueologia |
| Gemeentelijke catalogus en het geldende plan van Xàbia | PGOU 1990 deels geschorst, status van de NUTU onzeker; geen kaartdienst met de gemeentelijke catalogus gevonden | Ajuntament de Xàbia, Urbanisme — https://www.ajxabia.com · informe urbanístico volgens TRLOTUP art. 246.4 |
| Breedte van de brandstrook per gebouw | Hangt af van de helling en de ligging van het gebouw; geen kaartlaag | Bijlage XI TRLOTUP — https://www.boe.es/buscar/act.php?id=DOGV-r-2021-90283 |
| Deslinde-dossier zelf (kaartbladen, hoekpunten) | De WFS geeft de lijn, niet het dossier | https://www.miteco.gob.es/es/costas/temas/procedimientos-gestion-dominio-publico-maritimo-terrestre/linea-deslinde.html |
| Landelijke planviewer SIU | Hostnamen lossen niet op; ministeriële pagina geeft 403 | https://www.mivau.gob.es/urbanismo-y-suelo/sistema-de-informacion-urbana |

---

## Wat we niet weten

- Waar de SIU-dienst van het ministerie tegenwoordig staat. Alle drie de bekende hostnamen lossen niet op en de ministeriële pagina weigert ons verzoek (HTTP 403). **ONBEKEND.**
- Het adres van CartOXàbia. **ONBEKEND.**
- Wat er in de robots.txt van `gis.miteco.gob.es` en `servicios.idee.es` staat. **ONBEKEND.**
- Of de PATRICOVA-laag en de landelijke ARPSI-kaart op te lossen zijn tot één getal. Ze spreken elkaar tegen op waterdiepte (< 0,8 m tegen 0,96). **[te verifiëren door een waterbouwkundige.]**
- Of de datum in het veld `fechapleno` van laag 114 werkelijk de datum van het raadsbesluit is, en dus of de zesmaandentermijn op 28-11-2026 afloopt. **[te verifiëren bij het Ajuntament de Xàbia.]**
- Of de Generalitat aan TREE toestemming zou verlenen voor de volledige raadpleging van de archeologische inventaris, en welke procedure daarvoor geldt. **ONBEKEND.**
- Of er een kaartlaag bestaat met de *deslinde*-status van individuele veedriften buiten het veld `deslinde` (ja/nee). Niet onderzocht.
- De precieze voorwaarden van de ICV-ArcGIS-diensten. Het veld `copyrightText` in de servicebeschrijving is leeg; de CC BY 4.0-voorwaarde komt van de algemene pagina van het ICV en van de WMS-varianten van dezelfde gegevens. **[te verifiëren voor de ArcGIS-diensten afzonderlijk.]**

---

## Bronnen

Alle URL's hieronder zijn op **18-09-2026** opgehaald, tenzij anders vermeld.

**Kaartdiensten, zelf bevraagd (bewijstype 1 en 3)**

1. https://terramapas.icv.gva.es/0701_InfraestructuraVerde — GetCapabilities, GetFeatureInfo op `IVR.Inundacion`, `IVR.ZEC`, `IVR.ZEPA`, `IVR.LIC`, `IVR.ParquesNaturales`, `IVR.TFEPATFOR`, `IVR.Cultura.BIC.BIC`, `IVR.Cultura.BRL`; WFS op `IVR.Cultura.BIC.BIC` en `IVR.Cultura.BIC.Entornos`
2. https://terramapas.icv.gva.es/0702_Planeamiento — GetCapabilities, GetFeatureInfo en WFS op `Planeamiento.Clasificacion` en `Planeamiento.Zonificacion`
3. https://terramapas.icv.gva.es/0506_PATFOR — GetCapabilities en GetFeatureInfo op `SF.Forestal`, `Forestal.Estrategico`, `Planeamiento.TFE`, `Regulacion.Incendios.Urbano`
4. https://terramapas.icv.gva.es/0505_PORN — GetFeatureInfo op `Montgo.PORN`, `Montgo.Zonificacion`, `Montgo.Parque`
5. https://terramapas.icv.gva.es/22_IGPCV — GetCapabilities en GetFeatureInfo op `BIC`, `BIC.Entornos`, `BIC.Delimitaciones`, `BRL`
6. https://carto.icv.gva.es/arcgis/rest/services/tm_infraestructuras/ordenacion_territorial/MapServer — laaglijst en `identify` op de PATRICOVA-lagen
7. https://carto.icv.gva.es/arcgis/rest/services/tm_medio_ambiente/forestal/MapServer — laaglijst en `query` op laag 9 (vías pecuarias)
8. https://carto.icv.gva.es/arcgis/rest/services/tm_medio_ambiente/prevencion_de_incendios/MapServer — laaglijst en `query` op lagen 112, 113, 114, 103 tot en met 110
9. https://gis.miteco.gob.es/geoserver/costas/dominio_publico_maritimo_terrestre/ — GetCapabilities en WFS GetFeature
10. https://gis.miteco.gob.es/geoserver/costas/Servidumbre_Proteccion/ — GetCapabilities
11. https://gis.miteco.gob.es/geoserver/agua/DPH_Estimado/ — WFS GetFeature met bbox en met CQL `INTERSECTS` en `DWITHIN`
12. https://gis.miteco.gob.es/geoserver/agua/Zi_laminas_q100/, .../ZI_Laminas_ZFP/, .../Zi_arpsi/ — GetCapabilities en GetFeatureInfo
13. https://servicios.idee.es/wms-inspire/riesgos-naturales/inundaciones — GetFeatureInfo op `NZ.Flood.FluvialT100`
14. https://ovc.catastro.meh.es/ovcservweb/OVCSWLocalizacionRC/OVCCoordenadas.asmx/Consulta_RCCOOR — punt naar kadastrale referentie
15. https://ovc.catastro.meh.es/INSPIRE/wfsCP.aspx — `GetParcel` op `refcat`
16. https://ovc.catastro.meh.es/Cartografia/WMS/ServidorWMS.aspx — GetCapabilities, voor de gebruiksvoorwaarden
17. https://siajucar.chj.es/gis?SERVICE=WMS&MAP=services/SIA/Areas_con_riesgo_potencial_significativo_de_inundacion_ARPSI&REQUEST=GetCapabilities — CHJ-dienst, werkt; `Fees: conditions unknown`
18. https://wms.mapama.gob.es/sig/Costas/DPMT — **mislukt**, ServiceException NullReferenceException; het oude adres
19. https://icvficherosweb.icv.gva.es/00/geovisorgva/params/pro/configCapas.js — de laagconfiguratie van het ICV-viewer, gebruikt om laagnamen en laagnummers terug te vinden

**Wetteksten en officiële publicaties (bewijstype 2 en 4)**

20. https://www.boe.es/buscar/act.php?id=DOGV-r-2021-90283 — TRLOTUP geconsolideerd: disposición adicional séptima en bijlage XI (brandstrook)
21. https://www.boe.es/buscar/act.php?id=BOE-A-1988-18762 — Ley 22/1988 de Costas, art. 23 en disposición transitoria tercera
22. https://www.boe.es/buscar/act.php?id=BOE-A-2001-14276 — Texto Refundido de la Ley de Aguas, art. 6 (5 m servidumbre, 100 m politiezone)
23. https://www.boe.es/buscar/act.php?id=BOE-A-1995-7241 — Ley 3/1995 de Vías Pecuarias, art. 2 en 4
24. https://mediambient.gva.es/es/web/planificacion-territorial-e-infraestructura-verde/cartografia-del-patricova — PATRICOVA-cartografie en normativa (pagina bereikbaar; de normatieve artikelen 18 en 20 zijn overgenomen uit R13, controledatum 15-09-2026)
25. https://cultura.gva.es/es/web/patrimonio-cultural-y-museos/arqueologia — beperking op raadpleging van archeologische vindplaatsen
26. https://cultura.gva.es/es/web/patrimonio-cultural-y-museos/inventario-general — Inventario General del Patrimonio Cultural Valenciano
27. https://idev.gva.es/es/inicio/-/asset_publisher/Ly4ZDXKwJLAZ/content/nuevas-urls-de-servicios-wms-wfs-de-cultura-bics-brls-y-pedra-seca — nieuwe adressen voor de erfgoeddiensten, 25-06-2024
28. https://icv.gva.es/es/condiciones-de-uso-de-la-geoinformacion-icv — gebruiksvoorwaarden ICV, CC BY 4.0
29. https://www.miteco.gob.es/es/cartografia-y-sig/ide/directorio_datos_servicios/costas/wms-inspire-costas.html — catalogus kustdiensten, met de GeoServer-adressen
30. https://www.miteco.gob.es/es/cartografia-y-sig/ide/directorio_datos_servicios/agua/wms-inspire-agua.html — catalogus waterdiensten
31. https://www.chj.es/es-es/medioambiente/sistemasdeinformacion/Paginas/ServiciosIDE.aspx en http://aps.chj.es/down/html/descargas.html — CHJ-diensten en downloads
32. https://www.ajxabia.com/ver/7175/urbanismo-hace-publica-la-nueva-cartografia-municipal-de-xabia-en-la-web-del-ayuntamiento.html — aankondiging CartOXàbia, 15-02-2018
33. https://www.mivau.gob.es/urbanismo-y-suelo/sistema-de-informacion-urbana — SIU; de pagina met de dienstadressen gaf HTTP 403

**Eigen eerder werk**

34. `onderzoek/R11-catastro-registro-perceelidentificatie.md` — perceelidentificatie
35. `onderzoek/R12-urbanisme-xabia-plan-en-vergunning.md` — status PGOU en NUTU van Xàbia
36. `onderzoek/R13-regionaal-sectoraal-geoportalen.md` en het bijbehorende verificatiebestand — de eerste inventarisatie van de geoportalen, 15-09-2026

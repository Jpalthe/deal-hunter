# R11 — Catastro, Registro de la Propiedad en perceelidentificatie (met live tests)

> **NA TEGENSPRAAK (15-09-2026).** Dit rapport is door een tweede agent gecontroleerd; zie `R11-catastro-registro-perceelidentificatie.verificatie.md`. Betrouwbaarheid volgens die controle: middel.
> Weerlegd en in de eindstukken gecorrigeerd: R11-04; R11-06; R11-07; R11-11. Gebruik voor die punten de gecorrigeerde tekst in het verificatiebestand, niet de tekst hieronder.


**Project:** TREE Deal Hunter, fase A — onderzoeksstroom R11
**Controledatum:** 14-09-2026 (live tests uitgevoerd tussen 23:19 en 23:40 uur lokale tijd, vanaf de Mac mini)
**Masterprompt-secties:** 14 (percelen: identificatie vóór bouwconclusies), 11 (objectidentiteit), 5 en 7 (bewijs en bronnenregister)
**Bewijstypen:** 1 aanbieder · 2 officiële bron · 3 door ons rechtstreeks vastgesteld · 4 AI-inferentie · 5 berekening · 6 professional · 7 onbekend/tegenstrijdig

## Samenvatting (10 regels)

1. De vrije webservices van het Catastro (coördinaat → referencia catastral, RC → beschrijvende gegevens, RC → coördinaten, adres → RC) werken zonder login, zonder sleutel en binnen 0,1–0,4 s; de XML-, REST-XML- en JSON-varianten zijn alle drie live getest (bewijstype 3).
2. De JSON/REST-variant (`COVCCallejero.svc/json/Consulta_DNPRC?RefCat=…`) geeft méér dan de oude XML-variant: ook de perceeloppervlakte (`finca/dff/ss`), het perceeltype (`ltp`) en een kaartlink; de parameternamen verschillen per variant (`CoorX/CoorY` en `RefCat` in JSON; `Coordenada_X/Y` en `RC` in XML).
3. INSPIRE WFS (perceelgeometrie + `areaValue` in GML), WMS (kaartbeeld) en ATOM (complete gemeentebestanden, Xàbia = INE 03082, bijgewerkt 21-08-2026) zijn alle drie getest en vrij toegankelijk, onder bronvermelding "Dirección General del Catastro" en met een verbod op massale downloads via de interactieve/WMS-diensten.
4. Live test Montgó-pin (38.7940774, 0.123362): perceel 0281206BC5908S, 1.572 m² (advertentie 1.570 m² — 0,1 % verschil), maar Catastro toont een **bebouwd** perceel (villa uit 2006, 348 m² gebouwd). De Idealista-advertentie zelf (112256480, "Terreno", 505.000 €) beschrijft in de tekst een gebouwde villa van 310 m² — de categorie "terreno" is dus fout, niet de koppeling.
5. Live test Rafalet-pin (38.7620527, 0.1543695): perceel 2944017BC5924S, "suelo sin edificar", 1.074 m² (advertentie 1.000–1.120 m²). De pin ligt 2,1 m van de perceelgrens, het buurperceel ligt op 2,7 m en binnen 60 m liggen zeven percelen van 749–1.120 m² waarvan twee in de geadverteerde bandbreedte: koppeling **middel**, geen geforceerde keuze.
6. Adres slaat pin: een advertentie met zichtbaar adres ("Calle Mar Amarillo 5") levert via de Callejero-dienst direct 2944002BC5924S met 1.060 m² (advertentie 1.060 m²), terwijl de pin van diezelfde advertentie op de openbare weg ligt met vier percelen binnen 10 m.
7. Sede Electrónica: de per-perceelpagina ("datos no protegidos") en de PDF "Consulta descriptiva y gráfica" zijn zonder identificatie op te vragen (getest), maar de gebruiksvoorwaarden verbieden geautomatiseerd/massaal gebruik van de interactieve diensten; de valor de referencia, de CAT/Shapefile-downloads en de beschermde gegevens (eigenaar) vereisen Cl@ve/certificaat.
8. Registro de la Propiedad: geen openbare API gevonden. Nota simple (descripción, titularidad, cargas; informatief) en certificación (fehaciente) zijn per finca en tegen arancel aan te vragen via registradores.org (FLOTI, telematisch circa 24 uur volgens het Colegio); de koppeling RC ↔ finca loopt via de coördinatie van Ley 13/2015 (código registral único in art. 9 LH; vermoeden van ligging in art. 10.5 LH). Dit blijft handwerk per dossier.
9. Ontwerp: advertentie → (RC in tekst | adres | coördinaat) → kandidaat-RC's met afstanden → WFS-geometrie → punt-in-polygoon en oppervlaktevergelijking → zekerheid hoog/middel/laag → handmatige controle → pas daarna bouwmogelijkheden. Bij twee of meer plausibele percelen: "Bouwmogelijkheden nog niet betrouwbaar te bepalen: exacte perceelidentificatie ontbreekt."
10. Alles wat hierboven staat kan met de bestaande Python-omgeving (stdlib `xml.etree`, `json`, `urllib`/`httpx`; oppervlakte en punt-in-polygoon zijn met stdlib getest). `pyproj`/`shapely` zijn pas nodig voor CRS-transformaties en robuuste geometrie (overlap, buffers) en vergen akkoord van Jan; let op: de downloadhost `www.catastro.hacienda.gob.es` werkt met `httpx` maar niet met `curl`/`urllib` (certificaatketen FNMT).

---

## 1. Scope en werkwijze

Onderzocht en live getest zijn uitsluitend openbare, gratis diensten, met één of enkele verzoeken per dienst (`curl -sS -m 20`, `httpx` in de Hermes-venv, WebFetch). Er is niets geïnstalleerd, niets gestart en geen enkel lokaal bestand gewijzigd buiten dit rapport. De twee opgegeven testcoördinaten komen uit de Idealista-assistent (R01). Persoonsgegevens van eigenaren zijn nergens opgevraagd (die vallen onder "datos protegidos" en zijn zonder identificatie niet toegankelijk) en niet overgenomen.

Beperking van deze sessie: het WebSearch-budget was bij aanvang van deze stroom al opgebruikt (200/200 aanroepen sessiebreed). Alle bronnen zijn daarom rechtstreeks via bekende officiële URL's benaderd; waar een URL niet bekend was, staat dat in hoofdstuk 10.

---

## 2. Catastro — vrije webservices ("Servicios web libres", datos no protegidos)

### 2.1 Documentatie

Officieel document: `https://www.catastro.hacienda.gob.es/ws/Webservices_Libres.pdf` (bewijstype 2, gecontroleerd 14-09-2026). WebFetch kon de PDF niet lezen; de tekst is lokaal met een eigen zlib/CMap-parser uit het bestand gehaald. Versiehistorie in het document (letterlijk, tabel "Control de cambios"):

| Versie | Wijziging | Datum |
|---|---|---|
| 1.0 | Eén document voor de vrije webservices | 13-01-2014 |
| 2.0 | "Se migran los servicios libres de tecnología ASMX a WCF permitiendo operaciones SOAP y REST (GET y POST)" | 27-10-2022 |
| 2.1 | "Se incluyen respuestas en formato JSON" | 28-12-2022 |
| 2.2 | Etiket `<dtip>` (tipologie) | 23-06-2023 |
| 2.3 | Anexo III voorbeelden | 04-12-2023 |
| 2.4 | Nieuwe domeinnaam www.catastro.hacienda.gob.es | 22-05-2024 |
| 2.5 | "Se ofrece la información de la finca en los datos de un inmueble" | 09-10-2025 |
| 2.6 | INE-codes in de stratenlijst | 01-12-2025 |

Uit de documentatie (bewijstype 2):
- `RefCat`: "Obligatorio. Referencia catastral. Puede tener 14, 18 o 20 posiciones." De 14-tekenvorm is het perceel (`pc1` 7 tekens + `pc2` 7 tekens); 20 tekens = perceel + 4 cijfers "cargo" + 2 controletekens.
- Ondersteunde SRS bij coördinaatdiensten: EPSG:4230 (ED50), EPSG:4326 (WGS84), EPSG:4258 (ETRS89), EPSG:32627–32631 (UTM WGS84), en verdere UTM-varianten (lijst in het document).
- Veldbetekenissen: `luso` = gebruik, `sfc` = "SUPERFICIE" (gebouwd, per inmueble), `cpt` = "COEFICIENTE DE PARTICIPACIÓN", `ant` = "ANTIGÜEDAD" (bouwjaar), `stl` = "SUPERFICIE DE LA UNIDAD CONSTRUCTIVA", `ltp` = "LITERAL DE TIPO DE FINCA", `dff/ss` = "SUPERFICIE DEL SOLAR" (perceeloppervlakte), `igraf` = kaartlink, `cudnp` = aantal inmuebles in het antwoord, `cuerr` = aantal fouten.
- Gebruikslimieten: het document bevat **geen** getalsmatige limiet (aantal verzoeken per dag/seconde). ONBEKEND — zie 5.3 voor de algemene gebruiksvoorwaarden.

### 2.2 Endpoints die wij zelf werkend hebben gezien (bewijstype 3, 14-09-2026)

| # | Dienst | URL (getest) | Invoer | Resultaat |
|---|---|---|---|---|
| T1 | Consulta_RCCOOR (XML, ASMX) | `https://ovc.catastro.meh.es/ovcservweb/OVCSWLocalizacionRC/OVCCoordenadas.asmx/Consulta_RCCOOR?SRS=EPSG:4326&Coordenada_X=0.123362&Coordenada_Y=38.7940774` | lon, lat | HTTP 200, 0,35 s; `pc1=0281206 pc2=BC5908S`, `ldt` "CL PIC DE REBALSADORS 46 PARCELA 47 GARROFERAL JAVEA/XABIA (ALICANTE)" |
| T2 | idem, Rafalet | `…Consulta_RCCOOR?SRS=EPSG:4326&Coordenada_X=0.1543695&Coordenada_Y=38.7620527` | lon, lat | HTTP 200; `2944017 BC5924S`, "CL MAR AMARILLO 4 JAVEA/XABIA" |
| T3/T4 | Consulta_RCCOOR_Distancia (XML) | `…OVCCoordenadas.asmx/Consulta_RCCOOR_Distancia?SRS=EPSG:4326&Coordenada_X=…&Coordenada_Y=…` | lon, lat | lijst van percelen met `dis` in meter (0 = punt ligt in het perceel); zie hoofdstuk 3 |
| T5/T6 | Consulta_DNPRC (XML, ASMX) | `https://ovc.catastro.meh.es/ovcservweb/OVCSWLocalizacionRC/OVCCallejero.asmx/Consulta_DNPRC?Provincia=&Municipio=&RC=0281206BC5908S` | RC 14 tekens | HTTP 200; `luso`, `sfc`, `ant`, `lcons` — maar **zonder** `finca/ss` (perceeloppervlakte) |
| T7/T8 | Consulta_CPMRC (XML) | `…OVCCoordenadas.asmx/Consulta_CPMRC?Provincia=&Municipio=&SRS=EPSG:4326&RC=0281206BC5908S` | RC | HTTP 200; referentiepunt van het perceel (Montgó: 0.1234509, 38.7941604; Rafalet: 0.1544605, 38.7619144) |
| T9b | Consulta_RCCOOR (JSON, WCF) | `https://ovc.catastro.meh.es/OVCServWeb/OVCWcfCallejero/COVCCoordenadas.svc/json/Consulta_RCCOOR?SRS=EPSG:4326&CoorX=0.123362&CoorY=38.7940774` | **CoorX/CoorY** | HTTP 200, `application/json`; zelfde inhoud als T1 |
| T9 | idem met `Coordenada_X` | — | verkeerde parameternaam | JSON-fout `{"cod":"76","des":"LA COORDENADA X OBLIGATORIA"}` |
| T10b/T10c | Consulta_DNPRC (JSON, WCF) | `https://ovc.catastro.meh.es/OVCServWeb/OVCWcfCallejero/COVCCallejero.svc/json/Consulta_DNPRC?Provincia=&Municipio=&RefCat=2944017BC5924S` | **RefCat** (14 of 20 tekens; T21 met 20 tekens werkt ook) | HTTP 200; bevat extra `finca`: `ltp`, `dff.ss` (perceel-m²), `infgraf.igraf` (kaartlink) en per constructie `dvcons.dtip` |
| T10 | idem met `RC=` | — | verkeerde parameternaam | `{"cod":"17","des":"LA REFERENCIA CATASTRAL ES OBLIGATORIA"}` |
| T30 | Consulta_DNPRC (REST-XML, WCF) | `https://ovc.catastro.meh.es/OVCServWeb/OVCWcfCallejero/COVCCallejero.svc/rest/Consulta_DNPRC?RefCat=2944017BC5924S` | RefCat | HTTP 200, `application/xml`, met `<ss>1074</ss>` |
| T18 | Consulta_DNPLOC (Callejero, XML) | `…OVCCallejero.asmx/Consulta_DNPLOC?Provincia=ALICANTE&Municipio=JAVEA/XABIA&Sigla=CL&Calle=MAR%20AMARILLO&Numero=4&Bloque=&Escalera=&Planta=&Puerta=` | adres | HTTP 200; RC 2944017BC5924S |
| T28 | Consulta_DNPLOC (JSON) | `https://ovc.catastro.meh.es/OVCServWeb/OVCWcfCallejero/COVCCallejero.svc/json/Consulta_DNPLOC?Provincia=ALICANTE&Municipio=JAVEA/XABIA&Sigla=CL&Calle=MAR%20AMARILLO&Numero=5` | adres | HTTP 200; RC 2944002BC5924S, `ss=1060` |
| T19 | ConsultaMunicipio (Callejero) | `…OVCCallejero.asmx/ConsultaMunicipio?Provincia=ALICANTE&Municipio=JAVEA` | naam | `nm=JAVEA/XABIA`, `loine cp=3 cm=82` (INE), `locat cd=3 cmc=82` (Catastro-delegación 3, gemeentecode 82) |
| T20b | Fotofachada (WCF) | `https://ovc.catastro.meh.es/OVCServWeb/OVCWcfLibres/OVCFotoFachada.svc/RecuperarFotoFachadaGet?ReferenciaCatastral=0281206BC5908S` | RC | HTTP 200, `image/jpeg`, 574 KB, 2623×1967 px (EXIF-datum 28-09-2017); HEAD geeft 405, alleen GET |

De WCF-helppagina's (`…COVCCallejero.svc/help`) gaven op het testmoment "Sistema no disponible. Inténtelo más tarde." (bewijstype 3) — de diensten zelf werkten wel.

### 2.3 Wat de diensten wél en níet leveren

Wel (bewijstype 3, gezien in de antwoorden): referencia catastral (14/20 tekens), tekstadres (`ldt`), INE- en Catastro-gemeentecode, postcode, gebruik (`luso`), gebouwde oppervlakte per inmueble (`sfc`) en per bouweenheid (`stl` + `dtip`), bouwjaar (`ant`), perceeloppervlakte (`ss`, alleen in de WCF-varianten), perceeltype (`ltp`, bv. "Parcela construida sin división horizontal"), referentiepunt-coördinaat, kaartlink, gevelfoto.

Niet (bewijstype 3, afwezig in alle antwoorden): eigenaar/titular, lasten, valor catastral, valor de referencia, registrale gegevens (finca, CRU), coördinatiestatus met het Registro, planologische bestemming, bouwrecht. Sectie 14 van de masterprompt blijft dus onverkort van kracht: Catastro is geen bewijs van eigendom, bouwrecht of legaliteit.

---

## 3. Live tests op Jávea-coördinaten en vergelijking met de advertenties

### 3.1 Montgó-Ermita, pin 38.7940774 / 0.123362

| Gegeven | Advertentie (Idealista 112256480, bewijstype 1) | Catastro (bewijstype 2/3) |
|---|---|---|
| Type | "Terreno", urbano; titel "Terreno en Calle Pic de Rebalsadors, Montgó - Ermita" | `ltp` "Parcela construida sin división horizontal"; `luso` Residencial |
| Perceel | 1.570 m² | `ss` 1.572 m²; WFS `areaValue` 1572 m²; eigen shoelace-berekening op de WFS-geometrie (EPSG:25830) 1.572,6 m² (bewijstype 5) |
| Bebouwing | Tekst: "superficie construida de 310 m²", vier slaapkamers, vier badkamers, piscina, energielabel B | `sfc` 348 m² (VIVIENDA UNIFAMILIAR 247 + DEPORTES AIRE LIBRE 47 + ANEJOS 54), `ant` 2006; INSPIRE Buildings: `conditionOfConstruction` functional, `dateOfConstruction` 2006-01-01, `currentUse` 1_residential, `numberOfDwellings` 1 |
| Prijs | 505.000 € (322 €/m² perceel) | n.v.t. |
| Adres | verborgen (`showAddress=false`) | CL PIC DE REBALSADORS 46 PARCELA 47 GARROFERAL, 03730 |
| RC | niet vermeld | 0281206BC5908S (20 tekens: 0281206BC5908S0001PP) |
| Pin ↔ perceel | — | `Consulta_RCCOOR_Distancia`: 0281206 op 0 m (pin ligt ín het perceel); buren 0280104 en 0280105 op 15,16 m, 0281205 op 22,27 m |

Conclusie (bewijstype 4): de perceelkoppeling is **hoog** (pin binnen het perceel, oppervlakte 0,1 % verschil, geen tweede kandidaat binnen 15 m). Maar het object is géén kavel: de advertentietekst zelf beschrijft een gebouwde villa en Catastro bevestigt een woning uit 2006. De categorie "terreno" in de portaal-metadata is fout (bewijstype 7 voor "terreno"). Voor Deal Hunter: objecttype uit Catastro (`luso`/`ltp`/`ant`) altijd naast het advertentietype leggen en bij conflict het object als "woning op perceel" behandelen, niet als perceel.

Nabijgelegen advertentiepins (zelfde straat) laten zien hoe snel het misgaat (bewijstype 3):
- Idealista 35285631 ("Terreno en Calle Pic de Rebalsadors s/n", 1.651 m², 375.000 €, particulier, pin 38.7939957 / 0.1236449 — circa 25 m van de eerste pin): `Consulta_RCCOOR_Distancia` geeft **geen** perceel op 0 m; dichtstbijzijnde percelen 0281206 (4,43 m), 0381205 (5,77 m), 0280105 (7,87 m), 0280106 (12,48 m). De pin ligt op de weg; drie kandidaten binnen 8 m; oppervlakte van die kandidaten pas via WFS te bepalen → zekerheid **laag** zonder verdere stappen.
- Idealista 112283303 ("Terreno en Calle Pic de Rebalsadors, 30", 1.571 m², 500.000 €, "licencia de obra y proyecto incluido", adres zichtbaar): niet getest, maar met zichtbaar huisnummer is de Callejero-route (adres → RC) beschikbaar.

### 3.2 Rafalet, pin 38.7620527 / 0.1543695

| Gegeven | Opgave in de opdracht (uit R01, bewijstype 1) | Catastro (bewijstype 2/3) |
|---|---|---|
| Type | terreno met licentie | `luso` "Obras de urbanización y jardineria, suelos sin edificar"; `sfc` 0; Sede: "Clase Urbano, Uso principal Suelo sin edif." |
| Perceel | 1.000–1.120 m² | `ss` 1.074 m²; WFS `areaValue` 1074; Sede "Superficie gráfica 1.074 m²" |
| RC | — | 2944017BC5924S (0001AL); adres CL MAR AMARILLO 4, 03730 |
| Pin ↔ perceel | — | pin ín het perceel (`dis` 0); punt-in-polygoon op de WFS-geometrie (EPSG:4326) = waar; afstand tot de dichtstbijzijnde perceelgrens ≈ 2,1 m (bewijstype 5) |
| Buren | — | 2944010 op 2,7 m (960 m²), 2944012 op 7,57 m (1.120 m²), 2944011 op 10,57 m (883 m²), 2944013 op 20,81 m (898 m²) |
| bbox 60×60 m rond de pin | — | WFS: 7 percelen: 2944009 (749), 2944010 (960), 2944011 (883), 2944012 (1.120), 2944013 (898), 2944015 (963), 2944017 (1.074) m² |
| Geometrie-versie | — | `beginLifespanVersion` 2001-10-30 |

Conclusie (bewijstype 4): de pin wijst 2944017 aan, maar ligt 2,1 m van de grens en 2,7 m van een buurperceel; binnen de geadverteerde bandbreedte 1.000–1.120 m² passen **twee** percelen (2944017 met 1.074 en 2944012 met 1.120). Zekerheid **middel**: rapporteren als "waarschijnlijk 2944017BC5924S, alternatief 2944012BC5924S; bevestiging via adres, RC van de verkoper of nota simple nodig". Geen bouwconclusies vóór die bevestiging (masterprompt sectie 14).

De exacte advertentie bij deze coördinaat is in de hernieuwde zoekopdracht (8 resultaten voor El Rafalet, terrenos urbanos) niet teruggevonden; wel twee advertenties op "Calle Mar Amarillo, 5":
- Idealista 112433736: 1.060 m², 160.000 €, "aún no se ha solicitado la licencia de construcción", afbeelding "generada por IA con fines meramente ilustrativos" (bewijstype 1) — een schoolvoorbeeld van "perceel + voorbeeldvilla".
- Idealista 36575877: "Parcela urbana de 1064 m2", 150.000 €, particulier (bewijstype 1).
- Beide delen dezelfde pin 38.7622476 / 0.1547447. `Consulta_RCCOOR_Distancia` op die pin: geen perceel op 0 m; 2944013 (2,5 m), 2944012 (5,73 m), 2944003 (6,66 m), 2944002 (9,29 m), 2944017 (21,12 m). De pin ligt dus op de straat en het perceel met huisnummer 5 is pas de vierde kandidaat.
- Callejero `Consulta_DNPLOC` "CL MAR AMARILLO 5" → 2944002BC5924S, `ss` 1.060 m² (bewijstype 3): exacte match met 1.060 m² (112433736) en 0,4 % met 1.064 m² (36575877). Twee advertenties, één perceel, twee prijzen — precies het deduplicatiegeval van sectie 11.

### 3.3 Wat de tests leren voor het ontwerp

1. Een advertentiepin die ín een perceel valt is nog geen identificatie: bij Rafalet lag de pin 2 m van de grens.
2. Pins liggen geregeld op de openbare weg (twee van de vier geteste pins); dan geeft `Consulta_RCCOOR` niets en moet de afstandsvariant plus WFS-geometrie het werk doen.
3. Een zichtbaar adres (Idealista `showAddress=true`) is de betrouwbaarste automatische route: Callejero → RC → `ss`.
4. Oppervlaktevergelijking werkt alleen bij unieke kandidaten; in verkavelde urbanisaties liggen binnen 60 m zeven percelen van 749–1.120 m².
5. Advertentietype en Catastro-gebruik moeten worden vergeleken: "terreno" kan een villa zijn (Montgó) en "parcela con licencia" kan een kavel zonder aanvraag zijn (Mar Amarillo 5, "aún no se ha solicitado").
6. Idealista-beschrijvingen bevatten soms de RC letterlijk (bv. 103305763, Montgó-Ermita: "Referencia catastral: 8989318BC4988N0001XX", met ordenanza E, parcela mínima 1.500 m², edificabilidad 0,20 m²t/m²s — bewijstype 1, niet gecontroleerd). Een regex op de beschrijving is dus stap 1 van de keten.

---

## 4. INSPIRE-diensten van het Catastro

### 4.1 Overzicht (bewijstype 2 uit `https://www.catastro.hacienda.gob.es/webinspire/index.html`, bewijstype 3 waar getest)

| Dienst | URL | Getest | Uitkomst |
|---|---|---|---|
| WFS Cadastral Parcels | `https://ovc.catastro.meh.es/INSPIRE/wfsCP.aspx` | ja | GetFeature per RC en per bbox, GML 3.2 / INSPIRE CP 4.0 |
| WFS Buildings | `https://ovc.catastro.meh.es/INSPIRE/wfsBU.aspx` | ja | `STOREDQUERIE_ID=GetBuildingByParcel&refcat=…` |
| WFS Addresses | `https://ovc.catastro.meh.es/INSPIRE/wfsAD.aspx` | nee | — |
| WMS | `https://ovc.catastro.meh.es/cartografia/INSPIRE/spadgcwms.aspx` | ja | GetCapabilities 1.3.0 en GetMap (PNG) |
| ATOM (download per gemeente) | `https://www.catastro.hacienda.gob.es/INSPIRE/CadastralParcels/ES.SDGC.CP.atom.xml` (landelijk) → per provincie `…/CadastralParcels/03/ES.SDGC.CP.atom_03.xml`; idem `…/buildings/03/ES.SDGC.BU.atom_03.xml` en `…/Addresses/03/ES.SDGC.AD.atom_03.xml` | ja (feed + HEAD op de zips) | zie 4.4 |
| Licentie | `https://www.catastro.hacienda.gob.es/webinspire/documentos/Licencia.pdf` (ES) en `Licencia_en.pdf` (EN) | opgehaald | tekst niet machinaal leesbaar in deze omgeving (zie hoofdstuk 10) |

### 4.2 WFS — getest (bewijstype 3)

- `…/wfsCP.aspx?service=wfs&version=2&request=GetFeature&STOREDQUERIE_ID=GetParcel&refcat=0281206BC5908S&srsname=EPSG::25830` → HTTP 200, 2,9 KB, `numberMatched="1"`, `cp:areaValue uom="m2">1572`, `cp:beginLifespanVersion` 2018-02-20, `gml:posList` met 15 hoekpunten in EPSG:25830, `cp:referencePoint`, `cp:label` "06".
- Zelfde query met `srsname=EPSG::4326` voor 2944017BC5924S → coördinaten als **lat lon** (asvolgorde volgens EPSG), 19 hoekpunten, `areaValue` 1074.
- bbox-query zonder stored query: `…?service=wfs&version=2&request=GetFeature&Typenames=cp.cadastralparcel&bbox=38.7618,0.1540,38.7623,0.1547&srsname=EPSG::4326` → 7 percelen, 16 KB, 0,4 s.
- bbox circa 1 km² (38.760–38.769 / 0.150–0.160) → `numberMatched="486"`, `numberReturned="486"`, 1,09 MB, 12,1 s. Geen paginering: GetCapabilities meldt `ImplementsResultPaging = FALSE`; grote gebieden dus niet via WFS maar via ATOM.
- GetCapabilities: `ows:Fees` "No conditions apply"; `ows:AccessConstraints` "License documentation: https://www.catastro.hacienda.gob.es/webinspire/documentos/Licencia_en.pdf"; feature types `cp:CadastralParcel` en `cp:CadastralZoning`; CRS o.a. EPSG::4326, CRS::84, 4258, 25829/25830/25831, 3035, 3857.
- Buildings (`wfsBU.aspx`, GetBuildingByParcel op 0281206BC5908S): `conditionOfConstruction` functional, `dateOfConstruction` 2006-01-01, `currentUse` 1_residential, `numberOfBuildingUnits` 1, `numberOfDwellings` 1, `officialArea` met `officialAreaReference` grossFloorArea, `documentLink` naar de gevelfoto, `sourceStatus` NotOfficial. De commentaarregel in elk antwoord: "La precisión es la que corresponde nominalmente a la escala de captura de la cartografía".

### 4.3 WMS — getest (bewijstype 3)

- GetCapabilities: titel "Spanish General Directorate for Cadastre - INSPIRE View Services - WMS"; lagen `CP.CadastralParcel` (stijlen Default, LabelOnReferencePoint, BoundariesOnly, ReferencePointOnly, ElfCadastre), `CP.CadastralZoning`, `AD.Address`, `BU.Building`.
- Letterlijk: `<Fees>no conditions apply.</Fees>` en `<AccessConstraints>Free access, but it is not allowed massive downloads of cartography portions and tiled petitions</AccessConstraints>`.
- GetMap (`…spadgcwms.aspx?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&LAYERS=CP.CadastralParcel,BU.Building&STYLES=&CRS=EPSG:4326&BBOX=38.7615,0.1535,38.7625,0.1555&WIDTH=400&HEIGHT=400&FORMAT=image/png`) → 400×400 PNG, 15 KB. Bruikbaar als kaartplaatje in een dossier; niet als tegelserver.

### 4.4 ATOM — gemeentebestanden, INE-code Xàbia (bewijstype 2/3)

- INE-code **03082** voor Xàbia/Jávea is op drie plaatsen bevestigd: INE-tabel "Alicante/Alacant: Población por municipios y sexo" (`https://www.ine.es/jaxiT3/Tabla.htm?t=2856`, regel "03082 Xàbia/Jávea"); Catastro ConsultaMunicipio `loine cp=3 cm=82`; ATOM-entry "03082-JAVEA XABIA". De Catastro-eigen gemeentecode (`cmc`) is toevallig ook 82, met delegación 3.
- Provinciefeed 03 (250 KB, ISO-8859-1): entry `<title> 03082-JAVEA XABIA Cadastral Parcels</title>`, enclosure `https://www.catastro.hacienda.gob.es/INSPIRE/CadastralParcels/03/03082-JAVEA XABIA/A.ES.SDGC.CP.03082.zip` (let op de spatie in het pad, URL-encoderen als `%20`), `<updated>2026-08-21T00:00:00Z</updated>`, `georss:polygon` 38.7151–38.8193 N / 0.1015–0.2351 E, `category term` EPSG/0/25830 label ETRS89.
- Letterlijke licentieregel in de feed: `<rights>This service can be used free of charge in every instance, as long as that the D. G. of the Cadastre (Ministry of Finance) is mentioned as author and owner of the information</rights>`.
- HEAD (geen download uitgevoerd): `A.ES.SDGC.CP.03082.zip` 8.400.856 bytes, `A.ES.SDGC.BU.03082.zip` 13.252.024 bytes, `A.ES.SDGC.AD.03082.zip` 863.348 bytes; alle `Last-Modified` 21-08-2026. Volgens de INSPIRE-pagina worden de ATOM-bestanden tweemaal per jaar per gemeente ververst (bewijstype 2, samenvatting van de pagina).
- **Certificaatvalkuil (bewijstype 3):** `www.catastro.hacienda.gob.es` gebruikt een certificaat van "FNMT-RCM / AC SERVIDORES SEGUROS TIPO2". macOS-`curl` en Python-`urllib` (OpenSSL-standaardbundel) weigeren met "unable to get local issuer certificate"; `openssl s_client` met de systeemwinkel zegt "Verify return code: 0 (ok)"; `httpx` (certifi-bundel, in de Hermes-venv) haalt de feed gewoon op (HTTP 200). `ovc.catastro.meh.es` (webservices, WFS, WMS) werkt overal. Gebruik voor downloads dus `httpx` of geef expliciet een CA-bundel mee; niets omzeilen met `-k`.

---

## 5. Sede Electrónica del Catastro: PDF, cartografie, valor de referencia, voorwaarden

### 5.1 Zonder identificatie (bewijstype 2 via `https://www.sedecatastro.gob.es/`, bewijstype 3 waar getest)

- Buscador/visor: `https://www1.sedecatastro.gob.es/Cartografia/mapa.aspx?buscar=S`; informatie per RC: `…mapa.aspx?buscar=S&pest=urbana`.
- Per-perceelpagina "datos no protegidos" (getest, HTTP 200 zonder login): `https://www1.sedecatastro.gob.es/CYCBienInmueble/OVCConCiud.aspx?del=3&mun=82&RefC=2944017BC5924S0001AL` toont "Referencia catastral 2944017BC5924S0001AL … Localización CL MAR AMARILLO 4 Suelo 03730 JAVEA/XABIA (ALICANTE) Clase Urbano Uso principal Suelo sin edif. … Superficie gráfica 1.074 m²" en voor 0281206BC5908S0001PP "Uso principal Residencial … Año construcción 2006".
- PDF "Consulta descriptiva y gráfica" (getest): `https://www1.sedecatastro.gob.es/CYCBienInmueble/SECImprimirCroquisYDatos.aspx?del=3&mun=82&refcat=2944017BC5924S0001AL` → HTTP 200, `application/pdf`, 234 KB, zonder login. De variant `Cartografia/ImprimirPDFCroquisParcela.aspx?del=3&mun=82&refcat=2944017BC5924S` (14 tekens) gaf een lege body; de 20-tekenreferentie is dus nodig. Kaartlink uit de JSON-dienst (`igraf`): `https://www1.sedecatastro.gob.es/Cartografia/mapa.aspx?del=3&mun=82&refcat=2944017BC5924S` → HTTP 200, titel "Mapa Sede Electrónica del Catastro" (JavaScript-viewer).
- Deze Sede-pagina's zijn interactieve diensten; de gebruiksvoorwaarden (5.3) verbieden geautomatiseerd of massaal gebruik ervan. In Deal Hunter alleen als **handmatige** controlestap of hoogstens één PDF per bevestigd dossier, nooit in een lus.

### 5.2 Met identificatie (bewijstype 2)

- **Valor de referencia** (`https://www1.sedecatastro.gob.es/Accesos/SECAccvr.aspx`): de pagina biedt "Buscador del valor de referencia", "Mapas de valores urbanos/rústicos" en marktrapporten, achter een keuze "Certificado electrónico de identificación o DNI electrónico" / "Cl@ve PIN – Cl@ve permanente". Wat precies zonder identificatie zichtbaar is, kon niet worden vastgesteld (WebFetch zag alleen het identificatiescherm) → ⏸️ ACTIE VOOR JAN: met Cl@ve één keer proberen; tot dan ONBEKEND.
- **Descarga masiva** (`https://www.sedecatastro.gob.es/Accesos/SECAccDescargaDatos.aspx`): CAT-bestanden (alfanumeriek, per provincie), Shapefile-cartografie, topo-geodetische netten en historische cartografie vereisen certificaat/Cl@ve én aanvaarding van de licentie-tipo; "Consulta masiva" (XML in, offline resultaat) vereist authenticatie; webservices "datos protegidos" vereisen registratie. Webservices "datos no protegidos" en INSPIRE: vrij.

### 5.3 Gebruiksvoorwaarden en licentie (bewijstype 2)

- Aviso legal (`https://www.catastro.hacienda.gob.es/ayuda/avisolegal.htm`): beperkte licentie voor "descarga de dicho contenido y el uso privado del mismo", mits de inhoud intact blijft en de bron wordt vermeld, met verwijzing naar Ley 37/2007 (hergebruik overheidsinformatie).
- Condiciones de uso (`https://www.catastro.hacienda.gob.es/ayuda/condicionesuso.htm`): uitgangspunten "garantizar la disponibilidad del servicio" en "eficiencia"; monitoring van verzoeken per IP per tijdsinterval, automatische en handmatige blokkades, penalisatie van massale downloads; de **interactieve** diensten mogen niet voor automatische/massale downloads worden gebruikt; incidenten die daaruit voortkomen worden niet in behandeling genomen. Getallen (verzoeken per minuut) staan er niet.
- Resolución de 23 de marzo de 2011 (`https://www.catastro.hacienda.gob.es/documentos/normativa/res_230311.pdf`, 10 pagina's; tekst lokaal geëxtraheerd): licentie-tipo voor de **descarga masiva** via de Sede. Kernpunten letterlijk: "La autorización para el acceso, descarga y reutilización de la información catastral se produce de manera automática, una vez que se han cumplimentado todos los requisitos formales"; identificatie "mediante firma electrónica"; gratis; de informatie wordt uitsluitend toegestaan "a los efectos de que la misma sea transformada por el interesado, elaborando nuevos productos de valor añadido", dus "no se autoriza la distribución o comercialización de la información suministrada sin su previa transformación"; bronvermelding "a la Dirección General del Catastro, del Ministerio de Economía y Hacienda del Reino de España" plus de toegangsdatum in alle afgeleide producten; looptijd 10 jaar, wereldwijd. Deze resolutie gaat over de massadownload; voor INSPIRE gelden de licentie-PDF (niet leesbaar gekregen) en de `<rights>`-regel in de feeds; voor de webservices libres is geen aparte licentietekst gevonden → ONBEKEND of dezelfde bronvermeldingsplicht formeel geldt; wij passen haar in elk geval toe.

Praktische regel voor Deal Hunter (bewijstype 4): webservices en WFS alleen per kandidaatobject aanroepen (geen sweep over heel Jávea), antwoorden cachen op RC, maximaal circa één verzoek per seconde, en voor bulk-geometrie het ATOM-gemeentebestand gebruiken (twee keer per jaar). Elke afgeleide tabel of kaart krijgt de vermelding "Bron: Dirección General del Catastro, geraadpleegd <datum>".

---

## 6. Registro de la Propiedad

### 6.1 Wat een nota simple is en wat erin staat (bewijstype 2)

- Colegio de Registradores, FAQ "¿Cuál es el contenido de una nota simple o una certificación?" (`https://www.registradores.org/-/%C2%BFcua-l-es-el-contenido-de-una-nota-simple-o-una-certificacio-n-`): beide bevatten "la descripción de la finca, la titularidad y las posibles cargas"; de nota simple heeft alleen informatieve waarde, de certificación is het door de registrador ondertekende openbare document dat de registerinhoud fehaciente bewijst.
- Pagina "Registro de la Propiedad" (`https://www.registradores.org/el-colegio/registro-de-la-propiedad`): nota simple op schriftelijke aanvraag, via elke registrador ongeacht district, telematisch (FLOTI) in circa 24 uur; certificación 4 dagen per finca, eventueel met "información continuada" (30 dagen) of registradorrapport; telematische toegang tot nota simple, certificación, documentconsultatie (CSV) en "alertas geográficas".
- FAQ "nota simple desde municipio diferente": via het FLOTI-systeem op `https://www.registradores.org`, "a cualquier hora del día"; helpdesk 91 270 17 96 (ma–vr 8:30–18:00).
- Sede (`https://sede.registradores.org/`, Angular-app): navigatie "Propiedad" met Nota simple, Nota de localización, Información Continuada, Certificaciones, Alertas geográficas, Alertas al titular, Presentación telemática, Estadísticas a medida; verder Geoportal en "Portal de datos abiertos"; gebruikersomgeving "Mi Carpeta" (Notificaciones, Cómo va lo mío, Mis presentaciones, Facturas) — inloggen dus vereist voor bestellingen. Contact: Príncipe de Vergara 70, Madrid; 912701796; soporte.usuarios@corpme.es.
- Of oppervlakte, IDUFIR/CRU en referencia catastral in de nota simple staan, staat niet letterlijk op deze pagina's. Wettelijk (art. 9 LH, zie 6.3) moet het folio real de "código registral único" en "la referencia catastral del inmueble" bevatten; dat de nota simple die weergeeft is aannemelijk (bewijstype 4) en bij het eerste dossier te controleren.

### 6.2 Kosten en levertijd

- Arancel de los Registradores (Real Decreto 1427/1989, geconsolideerd, `https://www.boe.es/buscar/act.php?id=BOE-A-1989-28112`, laatste bijwerking volgens de BOE-pagina 17-11-2011; bewijstype 2): número 4 "Publicidad formal": "Por nota simple informativa o exhibición, por cada finca… 3,005061 euros"; certificación de dominio 9,015182 €, de cargas 24,040484 €, negativa de cargas 9,015182 €, otras 6,010121 € per finca.
- Wat de online nota simple via het Colegio in de praktijk kost (toeslagen, btw, per finca) is niet in een officiële bron gevonden → [te verifiëren] bij de eerste bestelling. Levertijd telematisch: "aproximadamente 24 horas" (bewijstype 2, pagina Colegio); certificación 4 dagen per finca.

### 6.3 Coördinatie Catastro–Registro, Ley 13/2015 (bewijstype 2)

Ley 13/2015, de 24 de junio, de Reforma de la Ley Hipotecaria … y del texto refundido de la Ley de Catastro Inmobiliario (`https://www.boe.es/buscar/act.php?id=BOE-A-2015-7046`, BOE 151 van 25-06-2015):
- Art. 9 LH (gewijzigd): "El folio real de cada finca incorporará necesariamente el código registral único de aquélla" en de inschrijving vermeldt "la referencia catastral del inmueble" en, waar van toepassing, de georefereerde grafische weergave.
- Art. 10 LH: de registrador neemt de kadastrale grafische weergave op wanneer die overeenkomt met de beschrijving; art. 10.5: "se presumirá, con arreglo a lo dispuesto en el artículo 38, que la finca objeto de los derechos inscritos tiene la ubicación y delimitación geográfica expresada en la representación gráfica catastral que ha quedado incorporada al folio real".
- Art. 198–210 LH: procedures voor concordantie tussen register en werkelijkheid (inmatriculación, deslinde, rectificación).
- Gevolg voor ons: een "finca coordinada" heeft een RC en een geometrie die met het Catastro overeenkomen; bij niet-gecoördineerde fincas kunnen registrale oppervlakte, Catastro-oppervlakte en advertentie alle drie verschillen. Sectie 14 ("relatie tussen advertentie, Catastro, eigendomsstukken en topografische meting") is precies dit onderscheid. De term IDUFIR (vóór 2015) versus CRU (art. 9 LH) is in de bronnen niet naast elkaar aangetroffen → bewijstype 7 voor de exacte omzettingsregel.

### 6.4 Geoportal / Base Gráfica Registral

- `https://geoportal.registradores.org/` is een JavaScript-app (1,3 KB HTML, geen inhoud zonder browser); de introductiepagina `https://www.registradores.org/geoportal` noemt zes onderdelen: "Localiza tu registro", "Visor de Alertas Geográficas", "Nota simple por geolocalización", "Geoportal", "GeoEditPro", "Visor Emergencias" (bewijstype 2). Zoeken op RC of coördinaten, lagen, WMS/WFS, login of kosten: niet vastgesteld → TECHNISCH ONDERZOEK NODIG (handmatig in de browser).
- "Nota simple por geolocalización" is voor Deal Hunter interessant (van kaart naar finca zonder RC), maar werking en prijs zijn ONBEKEND.

### 6.5 Wat geautomatiseerd kan en wat niet (bewijstype 3/4)

| Stap | Automatiseerbaar? | Toelichting |
|---|---|---|
| RC bepalen (coördinaat/adres/tekst) | ja | Catastro-webservices, hoofdstuk 2 |
| Perceelgeometrie en oppervlakte | ja | WFS per RC of ATOM-bestand |
| Gebouwgegevens (jaar, gebruik, m²) | ja | DNPRC + WFS Buildings |
| Eigenaar, lasten, hypotheken, beslagen | nee | alleen nota simple/certificación, per finca, betaald, na inloggen; geen API gevonden |
| Finca ↔ RC | half | de nota simple vermeldt de RC (art. 9 LH) → handmatig opvragen, daarna in het dossier vastleggen |
| Coördinatiestatus | nee (nog) | niet in de vrije webservices gezien; mogelijk in de Sede-PDF of de nota simple → [te verifiëren] |
| Bewaking van registrale wijzigingen | onbekend | "Alertas geográficas"/"Información Continuada" bestaan als dienst; voorwaarden en prijs ONBEKEND |

Status voor het bronnenregister: Registro de la Propiedad = **ALLEEN HANDMATIG** (per dossier, na akkoord van Jan op de kosten); Geoportal = **TECHNISCH ONDERZOEK NODIG**.

---

## 7. Ontwerp van de perceelkoppelingsketen

### 7.1 Stappen

```
advertentie (bron-ID, type, prijs, m² perceel, m² gebouwd, lat/lon, showAddress, adres, beschrijving)
  │
  ├─ 0. Normaliseer: municipio moet Jávea/Xàbia zijn (INE 03082); m²-getallen uit tekst en velden apart bewaren
  │
  ├─ 1. RC in de tekst?  regex [0-9]{7}[A-Z]{2}[0-9]{4}[A-Z]([0-9]{4}[A-Z]{2})?  → Consulta_DNPRC (JSON, RefCat)
  │        gevonden en municipio klopt → kandidaat met herkomst "tekst", basiszekerheid HOOG (na oppervlaktecheck)
  │
  ├─ 2. Adres zichtbaar (showAddress=true, straat+nummer)?  → Consulta_DNPLOC (JSON)
  │        precies één inmueble/finca → kandidaat "adres", basiszekerheid HOOG (na oppervlaktecheck)
  │        meerdere (bloque/escalera/planta) → alleen het perceel (14 tekens) overnemen
  │
  ├─ 3. Coördinaat → Consulta_RCCOOR_Distancia (JSON of XML, EPSG:4326)
  │        kandidaten = alle percelen met dis ≤ 25 m (Jávea-urbanisaties: buren op 2–20 m gezien)
  │        + WFS bbox (±30 m) voor de percelen die de afstandsdienst niet noemt
  │
  ├─ 4. Per kandidaat: WFS GetParcel (EPSG::4326 voor punt-in-polygoon, EPSG::25830 voor oppervlakte)
  │        - PIP(pin) waar/onwaar; afstand pin→grens (m)
  │        - areaValue vs geadverteerde m²: afwijking% = |ss − adv| / adv
  │        - DNPRC: luso/ltp/ant/sfc (bebouwd of "suelo sin edificar")
  │
  ├─ 5. Zekerheidsniveau (7.2)  → HOOG / MIDDEL / LAAG
  │
  ├─ 6. Bij MIDDEL/LAAG: dossierregel "Bouwmogelijkheden nog niet betrouwbaar te bepalen:
  │        exacte perceelidentificatie ontbreekt" + lijst kandidaten + wat nodig is
  │        (RC van verkoper, nota simple, plattegrond, bezoek/meting)
  │
  └─ 7. Handmatige controle (Sede-kaartlink, PDF, gevelfoto, satellietbeeld) → bevestigde RC
           → pas dan sectie 15–17 (bouwregels) en nota simple (eigendom/lasten)
```

### 7.2 Regels voor het zekerheidsniveau (bewijstype 4, kalibreren op de eerste 30 dossiers)

| Niveau | Voorwaarden (alle) | Voorbeeld uit de tests |
|---|---|---|
| **HOOG** | precies één kandidaat met afwijking ≤ 3 %; én (RC uit tekst, of adres-match, of PIP waar met grensafstand ≥ 5 m); én advertentietype ≠ in strijd met Catastro-gebruik | Mar Amarillo 5 via adres: 1.060 vs 1.060 m² |
| **MIDDEL** | één kandidaat ≤ 3 % maar grensafstand < 5 m; óf twee kandidaten binnen ±10 %; óf afwijking 3–10 % bij unieke kandidaat | Rafalet-pin: 2944017 (1.074) én 2944012 (1.120) in 1.000–1.120; pin 2,1 m van de grens |
| **LAAG** | pin buiten elk perceel en ≥ 2 kandidaten binnen 10 m zonder adres; óf geen kandidaat binnen ±10 %; óf oppervlakte in de advertentie ontbreekt; óf conflict advertentietype ↔ Catastro (zie 7.3) | Pic de Rebalsadors s/n: pin op de weg, 3 kandidaten binnen 8 m |

Bij LAAG of MIDDEL nooit bouwmogelijkheden berekenen; wel rapporteren welke informatie de koppeling zou sluiten en hoe die rechtmatig te krijgen is (verkoper om RC vragen — die staat op elk IBI-aanslagbiljet; nota simple; Sede-kaart handmatig).

### 7.3 Bijzondere gevallen (sectie 11 en 14)

| Geval | Herkenning | Regel |
|---|---|---|
| Meerdere percelen | tekst: "dos parcelas", "dividir", "2.098 m² … dos parcelas independientes" (Idealista 112050209); of geadverteerde m² ≈ som van 2–3 aangrenzende percelen | zoek combinaties van aangrenzende kandidaten waarvan de som ±3 % klopt; koppel nooit één perceel als de tekst er meer noemt; dossier krijgt n RC's of status "onbepaald" |
| Adres verborgen | `showAddress=false` | pin kan verplaatst/afgerond zijn; maximaal MIDDEL tenzij RC in tekst; bij HOOG-criteria toch "adres verborgen" als voorbehoud vermelden |
| Perceel + voorbeeldvilla | tekst: "proyecto", "licencia", "imagen generada por IA", "ejemplo orientativo", "villa puede construirse"; Catastro: "suelo sin edificar", sfc 0 | objecttype = perceel; villa-m² uit de tekst apart opslaan als "projectvoorstel", niet als bestaand; prijs = grond (+ eventueel project/licentie) |
| Prijs alleen grond vs grond + bouw | tekst met "parcela + proyecto", "coste estimado de construcción", "inversión total" (Idealista 110509726: 778.000 + 122.000 = 900.000 €, bouw ca. 1,8 mln apart) | bewaar prijscomponenten gescheiden: grond, licentie/project/taksen, bouwkosten; €/m² perceel alleen op de grondcomponent berekenen |
| "Terreno" is een woning | Catastro `ltp` "Parcela construida…", `ant` gevuld, `sfc` > 0, tekst beschrijft slaapkamers/badkamers (Montgó 112256480) | objecttype = woning op perceel; advertentiecategorie markeren als fout (bewijstype 7); door naar renovatieanalyse in plaats van perceelanalyse |
| Twee advertenties, één perceel | zelfde RC na koppeling, verschillende bron-ID's/prijzen (Mar Amarillo 5: 150.000 en 160.000 €) | één objectdossier, beide advertenties bewaren, prijsverschil zichtbaar houden (sectie 11) |
| Oppervlaktebegrippen | advertentie "1.064" vs Catastro `ss` 1.060 vs "superficie gráfica" 1.074 vs registrale oppervlakte | elk getal met eigen bron en definitie opslaan; nooit overschrijven |

### 7.4 Python-bouwstenen zonder installatie (bewijstype 3, getest in de Hermes-venv, Python 3.11)

| Onderdeel | Bouwsteen | Status |
|---|---|---|
| HTTP naar `ovc.catastro.meh.es` | `urllib.request` of `httpx` | beide werken |
| HTTP naar `www.catastro.hacienda.gob.es` (ATOM/zip) | `httpx` (certifi) | werkt; `urllib`/`curl` falen op de FNMT-keten |
| JSON-antwoorden | `json` (stdlib) | getest |
| XML/GML parsen | `xml.etree.ElementTree` met namespaces `cp` (`http://inspire.ec.europa.eu/schemas/cp/4.0`) en `gml` (`http://www.opengis.net/gml/3.2`) | getest: `areaValue`, `posList`, `nationalCadastralReference` |
| Oppervlakte uit geometrie | shoelace-formule op EPSG:25830-coördinaten | getest: 1.572,6 m² vs `areaValue` 1572 |
| Punt-in-polygoon | ray casting in lat/lon (WFS in EPSG::4326 opvragen) | getest: Rafalet-pin binnen 2944017 |
| Afstand pin→grens | equirectangulaire benadering (111.320 m/° lon × cos φ, 110.540 m/° lat) | getest: 2,1 m; voor Jávea ruim nauwkeurig genoeg |
| Kaartplaatje in dossier | WMS GetMap PNG + `Pillow` (aanwezig) | GetMap getest |
| Cache/opslag | `sqlite3` (stdlib) met RC als sleutel, of JSON-bestanden per RC; géén gebruik van de Tree AI OS-Postgres | ontwerpkeuze |
| Rate limiting/retry | `time.sleep`, eigen teller; `httpx` timeouts | ontwerpkeuze |

Waar `pyproj`/`shapely` nodig zouden zijn (akkoord van Jan vereist vóór `pip install`):
- `pyproj`: transformatie EPSG:4326 ↔ 25830 als één geometrie in beide stelsels nodig is (nu omzeild door de WFS tweemaal te bevragen; voor ATOM-bestanden, die alleen in ETRS89/UTM 30N komen, is punt-in-polygoon in projectiecoördinaten mogelijk als de pin eerst wordt omgezet — dat vergt pyproj of een eigen UTM-formule).
- `shapely`: overlap/adjacency van kandidaten, buffers ("welke percelen binnen 25 m"), multipolygonen met gaten, geldigheidscontroles. Tot die tijd: WFS bbox en de afstandsdienst van het Catastro leveren dezelfde informatie server-side.
- `lxml`/`bs4`: niet nodig (ElementTree volstaat, er wordt geen HTML gescraped).
- Geo-database (PostGIS): niet beschikbaar en voor fase A niet nodig; het ATOM-bestand van Xàbia (8,4 MB zip) past in geheugen.

---

## 8. Bronnenregister (sectie 7 van de masterprompt)

| Bron | URL | Type | Toegang | Status | Opmerkingen |
|---|---|---|---|---|---|
| Catastro — Servicios web libres (Callejero, Coordenadas; XML/REST/JSON) | `https://ovc.catastro.meh.es/OVCServWeb/OVCWcfCallejero/…` en `…/ovcservweb/OVCSWLocalizacionRC/…` | overheid, primaire bron | vrij, geen sleutel | GEVERIFIEERD EN ACTIEF | per object aanroepen; limieten niet gepubliceerd; bronvermelding DGC |
| Catastro — INSPIRE WFS CP/BU/AD | `https://ovc.catastro.meh.es/INSPIRE/wfsCP.aspx` (BU/AD analoog) | overheid | vrij | GEVERIFIEERD EN ACTIEF | geen paginering; licentie-PDF; niet massaal |
| Catastro — INSPIRE WMS | `https://ovc.catastro.meh.es/cartografia/INSPIRE/spadgcwms.aspx` | overheid | vrij | GEVERIFIEERD EN ACTIEF | "not allowed massive downloads … and tiled petitions" |
| Catastro — INSPIRE ATOM (Xàbia 03082) | `https://www.catastro.hacienda.gob.es/INSPIRE/CadastralParcels/03/ES.SDGC.CP.atom_03.xml` | overheid | vrij | GEVERIFIEERD EN ACTIEF (HEAD; download nog niet uitgevoerd) | 2×/jaar; bronvermelding; certificaatketen |
| Catastro — Sede: datos no protegidos, kaart, PDF CDyG, gevelfoto | `https://www1.sedecatastro.gob.es/…` | overheid | vrij, interactief | ALLEEN HANDMATIG | condiciones de uso verbieden automatisering |
| Catastro — Sede: valor de referencia | `https://www1.sedecatastro.gob.es/Accesos/SECAccvr.aspx` | overheid | Cl@ve/certificaat | ALLEEN HANDMATIG | wat zonder identificatie kan: ONBEKEND |
| Catastro — descarga masiva CAT/Shapefile | `https://www.sedecatastro.gob.es/Accesos/SECAccDescargaDatos.aspx` | overheid | certificaat + licentie-tipo | CONTRACT OF TOESTEMMING NODIG | Resolución 23-03-2011; alleen als INSPIRE niet volstaat |
| Catastro — webservices datos protegidos | idem | overheid | registratie | NIET GEBRUIKEN | eigenaargegevens; niet nodig en niet gemachtigd |
| Registradores — Sede (nota simple, certificación) | `https://sede.registradores.org/` | beroepsorganisatie (publiek register) | login, betaald per finca | ALLEEN HANDMATIG | arancel 3,005061 €/finca (basis); online prijs [te verifiëren] |
| Registradores — Geoportal | `https://geoportal.registradores.org/` | idem | JS-app | TECHNISCH ONDERZOEK NODIG | "nota simple por geolocalización", "alertas geográficas" |
| BOE — Ley 13/2015 (LH art. 9, 10, 198–210) | `https://www.boe.es/buscar/act.php?id=BOE-A-2015-7046` | wet, geconsolideerd | vrij | GEVERIFIEERD (referentie) | coördinatie, CRU |
| BOE — Arancel registradores RD 1427/1989 | `https://www.boe.es/buscar/act.php?id=BOE-A-1989-28112` | wet | vrij | GEVERIFIEERD (referentie) | número 4 publicidad formal |
| INE — gemeentecodes | `https://www.ine.es/jaxiT3/Tabla.htm?t=2856` | overheid | vrij | GEVERIFIEERD (referentie) | 03082 Xàbia/Jávea |
| Idealista-assistent (MCP) | zie R01 | portaal | via MCP | zie R01 | hier alleen gebruikt om de vier advertenties terug te vinden |

---

## 9. Open vragen

1. Getalsmatige limieten van de Catastro-webservices en WFS zijn niet gepubliceerd; zelf begrenzen (≤ 1 verzoek/s, cache op RC) en bij blokkade niet omzeilen maar melden.
2. De INSPIRE-licentietekst (Licencia.pdf / Licencia_en.pdf) kon hier niet gelezen worden; Jan of een collega opent hem in de browser en bevestigt: bronvermelding volstaat, geen verdere beperking voor intern/commercieel gebruik? [te verifiëren]
3. Werkelijke prijs en voorwaarden van de online nota simple (FLOTI) en van "Información Continuada"/"Alertas geográficas"; is er een professioneel abonnement voor makelaars? ⏸️ ACTIE VOOR JAN: één proefbestelling voor een bevestigd dossier.
4. Toont de nota simple standaard RC, CRU en coördinatiestatus, en hoe vaak zijn Jávea-fincas gecoördineerd? Te leren van de eerste dossiers.
5. Wat het Geoportal van de Registradores kan (zoeken op RC/coördinaat, "nota simple por geolocalización") — handmatig in de browser bekijken.
6. Nauwkeurigheid van Idealista-pins bij `showAddress=false`: op een steekproef van 30 Jávea-advertenties meten hoe vaak de pin ín een perceel valt (in deze test 2 van 4 op de weg).
7. Wat de valor de referencia-pagina zonder Cl@ve laat zien; en of Jan met zijn Cl@ve de valor per RC wil opvragen als waarderingsanker (sectie 20).
8. Akkoord van Jan nodig zodra `pyproj`/`shapely` of een eigen geodatabase gewenst is; tot dan stdlib.
9. Of de Catastro-eigen gemeentecode (`cmc`) in andere gemeenten afwijkt van de INE-code (voor Jávea beide 82); bij uitbreiding buiten Jávea altijd via ConsultaMunicipio ophalen.
10. Of het gebruik van de Idealista-assistent voor dit soort verificatie binnen de voorwaarden valt (vraag ligt in R01).

---

## 10. Geblokkeerd of mislukt

- **WebSearch**: sessiebudget uitgeput (200/200) vóór deze stroom; geen enkele zoekopdracht mogelijk. Alle bronnen rechtstreeks benaderd.
- **PDF's via WebFetch**: `Webservices_Libres.pdf`, `Licencia.pdf`, `Licencia_en.pdf` en `res_230311.pdf` worden door WebFetch als binaire data teruggegeven; `pdftoppm` ontbreekt op de Mac. Met een eigen zlib/CMap-parser zijn de documentatie en de Resolución 2011 leesbaar gemaakt; de twee licentie-PDF's niet (glyph-gecodeerde fonts).
- **Certificaatketen** `www.catastro.hacienda.gob.es`: `curl` en Python-`urllib` weigeren (FNMT-RCM AC SERVIDORES SEGUROS TIPO2); `httpx` werkt. Niet omzeild.
- **404**: `https://www.catastro.hacienda.gob.es/esp/wsinspire.asp`; `https://www.ine.es/daco/daco42/codmun/codmunmapa.htm`.
- **JavaScript-apps zonder inhoud voor fetch**: `https://geoportal.registradores.org/`, `https://sede.registradores.org/` (alleen navigatielabels).
- **Registradores-FAQ** "¿Cómo se obtiene la publicidad del Registro de la Propiedad?": de URL leverde een andere FAQ (hypotheekdoorhaling); antwoord niet gezien.
- **WCF-helppagina's** (`…/COVCCallejero.svc/help`, `…/COVCCoordenadas.svc/help`): "Sistema no disponible".
- **`ImprimirPDFCroquisParcela.aspx`** met 14-tekens-RC: lege body; de `SECImprimirCroquisYDatos.aspx`-route met 20 tekens werkt wel.
- **Niet getest** (bewust, om verzoeken te beperken): WFS Addresses, `Consulta_DNPPP` (rústica polígono/parcela), WMS GetFeatureInfo, daadwerkelijke download van de ATOM-zips (alleen HEAD).

---

## 11. Bronnenlijst (URL · controledatum · bewijstype)

1. `https://www.catastro.hacienda.gob.es/ws/Webservices_Libres.pdf` · 14-09-2026 · 2 (documentatie webservices libres, v2.6 van 01-12-2025)
2. `https://ovc.catastro.meh.es/ovcservweb/OVCSWLocalizacionRC/OVCCoordenadas.asmx/Consulta_RCCOOR` · 14-09-2026 · 3
3. `https://ovc.catastro.meh.es/ovcservweb/OVCSWLocalizacionRC/OVCCoordenadas.asmx/Consulta_RCCOOR_Distancia` · 14-09-2026 · 3
4. `https://ovc.catastro.meh.es/ovcservweb/OVCSWLocalizacionRC/OVCCoordenadas.asmx/Consulta_CPMRC` · 14-09-2026 · 3
5. `https://ovc.catastro.meh.es/ovcservweb/OVCSWLocalizacionRC/OVCCallejero.asmx/Consulta_DNPRC` · 14-09-2026 · 3
6. `https://ovc.catastro.meh.es/ovcservweb/OVCSWLocalizacionRC/OVCCallejero.asmx/Consulta_DNPLOC` · 14-09-2026 · 3
7. `https://ovc.catastro.meh.es/ovcservweb/OVCSWLocalizacionRC/OVCCallejero.asmx/ConsultaMunicipio` · 14-09-2026 · 3
8. `https://ovc.catastro.meh.es/OVCServWeb/OVCWcfCallejero/COVCCoordenadas.svc/json/Consulta_RCCOOR` · 14-09-2026 · 3
9. `https://ovc.catastro.meh.es/OVCServWeb/OVCWcfCallejero/COVCCallejero.svc/json/Consulta_DNPRC` en `…/rest/Consulta_DNPRC` en `…/json/Consulta_DNPLOC` · 14-09-2026 · 3
10. `https://ovc.catastro.meh.es/OVCServWeb/OVCWcfLibres/OVCFotoFachada.svc/RecuperarFotoFachadaGet` · 14-09-2026 · 3
11. `https://www.catastro.hacienda.gob.es/webinspire/index.html` · 14-09-2026 · 2
12. `https://ovc.catastro.meh.es/INSPIRE/wfsCP.aspx` (GetCapabilities, GetParcel, bbox) · 14-09-2026 · 3
13. `https://ovc.catastro.meh.es/INSPIRE/wfsBU.aspx` (GetBuildingByParcel) · 14-09-2026 · 3
14. `https://ovc.catastro.meh.es/cartografia/INSPIRE/spadgcwms.aspx` (GetCapabilities, GetMap) · 14-09-2026 · 3
15. `https://www.catastro.hacienda.gob.es/INSPIRE/CadastralParcels/03/ES.SDGC.CP.atom_03.xml` · 14-09-2026 · 2/3
16. `https://www.catastro.hacienda.gob.es/INSPIRE/CadastralParcels/03/03082-JAVEA%20XABIA/A.ES.SDGC.CP.03082.zip` (HEAD), idem `…/buildings/…/A.ES.SDGC.BU.03082.zip`, `…/Addresses/…/A.ES.SDGC.AD.03082.zip` · 14-09-2026 · 3
17. `https://www.catastro.hacienda.gob.es/webinspire/documentos/Licencia.pdf` en `Licencia_en.pdf` · 14-09-2026 · 7 (niet leesbaar gekregen)
18. `https://www.sedecatastro.gob.es/` · 14-09-2026 · 2
19. `https://www1.sedecatastro.gob.es/CYCBienInmueble/OVCConCiud.aspx` (RC 2944017BC5924S0001AL en 0281206BC5908S0001PP) · 14-09-2026 · 3
20. `https://www1.sedecatastro.gob.es/CYCBienInmueble/SECImprimirCroquisYDatos.aspx` · 14-09-2026 · 3
21. `https://www1.sedecatastro.gob.es/Cartografia/mapa.aspx?del=3&mun=82&refcat=2944017BC5924S` · 14-09-2026 · 3
22. `https://www1.sedecatastro.gob.es/Accesos/SECAccvr.aspx` · 14-09-2026 · 2
23. `https://www.sedecatastro.gob.es/Accesos/SECAccDescargaDatos.aspx` · 14-09-2026 · 2
24. `https://www.catastro.hacienda.gob.es/ayuda/avisolegal.htm` · 14-09-2026 · 2
25. `https://www.catastro.hacienda.gob.es/ayuda/condicionesuso.htm` · 14-09-2026 · 2
26. `https://www.catastro.hacienda.gob.es/documentos/normativa/res_230311.pdf` · 14-09-2026 · 2
27. `https://www.ine.es/jaxiT3/Tabla.htm?t=2856` · 14-09-2026 · 2
28. `https://www.boe.es/buscar/act.php?id=BOE-A-2015-7046` (Ley 13/2015) · 14-09-2026 · 2
29. `https://www.boe.es/buscar/act.php?id=BOE-A-1989-28112` (Arancel registradores) · 14-09-2026 · 2
30. `https://sede.registradores.org/` · 14-09-2026 · 2
31. `https://www.registradores.org/el-colegio/registro-de-la-propiedad` · 14-09-2026 · 2
32. `https://www.registradores.org/-/%C2%BFcua-l-es-el-contenido-de-una-nota-simple-o-una-certificacio-n-` · 14-09-2026 · 2
33. `https://www.registradores.org/-/%C2%BFco-mo-puede-solicitarse-una-nota-simple-desde-municipio-diferente-al-de-situacio-n-de-la-finca-` · 14-09-2026 · 2
34. `https://www.registradores.org/-/%C2%BFco-mo-se-obtiene-la-publicidad-1?redirect=%2F` · 14-09-2026 · 2
35. `https://www.registradores.org/geoportal` en `https://geoportal.registradores.org/` · 14-09-2026 · 2 / 7
36. Idealista-assistent (MCP), zoekopdrachten "terreno urbano en Jávea zona Montgó Ermita de 1.570 m2" en "terreno urbano con licencia en Jávea urbanización Rafalet"; advertenties `https://www.idealista.com/es/inmueble/112256480/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail`, `https://www.idealista.com/es/inmueble/35285631/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail`, `https://www.idealista.com/es/inmueble/112433736/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail`, `https://www.idealista.com/es/inmueble/36575877/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail`, `https://www.idealista.com/es/inmueble/112283303/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail`, `https://www.idealista.com/es/inmueble/103305763/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail`, `https://www.idealista.com/es/inmueble/112050209/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail`, `https://www.idealista.com/es/inmueble/110509726/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail` · 14-09-2026 · 1
37. Eigen berekeningen (shoelace-oppervlakte, punt-in-polygoon, grensafstand) op de WFS-antwoorden, stdlib Python 3.11 in de Hermes-venv · 14-09-2026 · 5

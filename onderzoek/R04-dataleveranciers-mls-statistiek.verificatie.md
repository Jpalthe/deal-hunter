# Verificatie R04 — Dataleveranciers, aggregators, MLS-netwerken en officiële statistiek

**Rol:** tegenspreker van `R04-dataleveranciers-mls-statistiek.md` (versie 14-09-2026)
**Controledatum:** 15-09-2026 (alle controles hieronder zelf uitgevoerd op deze dag, tenzij anders vermeld)
**Methode:** elke kernclaim opnieuw tegen de primaire bron gehouden (WebFetch op de bronpagina, curl op openbare endpoints en open-databestanden, dig voor DNS). Geen inlog, geen omzeiling van blokkades, niets geïnstalleerd. XLS-bestanden van het MIVAU zijn op byte-niveau doorzocht (geen XLS-parser aanwezig). WebSearch werkte in deze ronde (3 zoekvragen gebruikt).
**Bewijstypes:** 1 aanbieder · 2 officiële bron · 3 zelf vastgesteld · 4 AI-inferentie · 5 berekening · 6 professional · 7 onbekend/tegenstrijdig

## Samenvatting van het oordeel

- 20 kernclaims gecontroleerd: **18 bevestigd** (waarvan 9 met een correctie of nuance), **1 weerlegd** (R04-10, Witei), **1 bevestigd met bronfout** (R04-07: de datum 01-03-2023 staat niet in de opgegeven bron, wel in een ander supportartikel).
- **Belangrijkste fout buiten de claimlijst:** het rapport stelt dat de MIVAU-gemeentebestanden ook de *waarde* (totaal/gemiddeld) van transacties per gemeente geven en noemt dat "hét toetsingscijfer per gemeente". Dat klopt niet: per gemeente geeft het Boletín Online alleen het **aantal** transacties; waarde en gemiddelde waarde staan uitsluitend per autonome regio en provincie (type 3, zelf vastgesteld).
- **Tweede systematische fout:** de status "GEVERIFIEERD EN ACTIEF" is gegeven aan bronnen die niet aangesloten zijn en niet draaien (Tinsa Radar zonder abonnement; MIVAU, INE, datos.gob.es en Catastro OVC na één handmatige test). Volgens de projectregels heet iets pas "actief" als het getest draait.
- Kleinere punten: prijzen zonder btw-vermelding (Inmobalia is expliciet "VAT not included"; bij Tinsa Radar niet vermeld), een Apibolsa-toegangseis die ontbreekt (INMOPC-software), een verouderd voorbeeld bij Registradores (1T 2025 terwijl 2T 2026 er is) en MLS 03724-dekking die op een derdenblog uit 2023 rust.
- **Totaalbeoordeling betrouwbaarheid: middel-hoog.** De bronnen en citaten zijn vrijwel allemaal echt en correct, maar twee dragende conclusies (gemeentelijke transactiewaarde, "actief"-statussen) moeten worden gecorrigeerd voordat het rapport in de bronnenkaart wordt overgenomen.

---

## 1. Oordeel per claim

| id | Claim (kort) | Oordeel | Gecorrigeerde claim / nuance | Bron-URL (zelf geopend) | Datum |
|---|---|---|---|---|---|
| R04-01 | Casafari indexeert 30.000+ bronnen, publiceert niets, ontdubbelt; REST-API, MCP, iFrame, Data Exports; prijs op offerte; 12 maanden looptijd | **Bevestigd** | API-pagina: "30.000+ classified portals and agencies", "60+ million properties with history", "100% deduplication accuracy", prijs "depends on the type of API, data volume, and integration needs". De 12 maanden (met automatische verlenging, betaling maandelijks of jaarlijks) staat **niet** op de API-pagina maar in de FAQ. FAQ: "CASAFARI does not publish properties, it only indexes the listings". Alle getallen zijn aanbiederclaims (type 1). | https://www.casafari.com/products/property-data-api/ · https://www.casafari.com/faq/ | 15-09-2026 |
| R04-02 | Casafari-voorwaarden: persoonlijke, herroepbare licentie; verbod op systematische verzameling en afgeleide werken; API gebonden aan format/throughput | **Bevestigd** | Letterlijk aanwezig ("personal, revocable, non-transferable and non-exclusive license"; "Systematically collect … data spiders, robots"; "Make derivative works"). Let op: de gebruiksvoorwaarden dateren volgens de pagina van **27-03-2018**; abonnementsvoorwaarden zijn een apart document dat niet is ingezien. Wat een API-contract toestaat is dus ONBEKEND. | https://www.casafari.com/terms-of-use | 15-09-2026 |
| R04-03 | uDA op 14-05-2024 door Tinsa Group gekocht van Alantra LLP; op 22-05-2025 met Tinsa Digital, Deyde Datacentric en on-geo opgegaan in Accumin Intelligence (120 medewerkers) | **Bevestigd** | Letterlijk: "The Tinsa Group has reached an agreement with the financial services company Alantra LLP to acquire urbanData Analytics". Persbericht fusie gedateerd 22-05-2025, noemt on-geo en "120 people". Kleine precisering: het persbericht spreekt van "Tinsa Digital", niet "Tinsa Digital AVM". Datum 14-05-2024 is de datum van de *overeenkomst*/het persbericht, niet per se van closing [te verifiëren]. | https://www.accumin.com/newsroom/corporate-actions/the-tinsa-group-acquires-urbandata-analytics · https://www.accumin.com/newsroom/corporate-actions/tinsa-digital-deyde-datacentric-and-urbandata-analytics-join-forces-in-accumin-intelligence | 15-09-2026 |
| R04-04 | Tinsa Radar €29/studie, €99/mnd (15), €259/mnd (45), 7 dagen proef, PDF; geen API | **Bevestigd, met correctie** | Prijzen en proef kloppen ("Gratis los primeros 7 días", "sin permanencia", "Descarga PDF con Logotipo personalizado"). **Btw: niet vermeld op de pagina → ONBEKEND of €29/€99/€259 incl. of excl. IVA.** "Geen API" = niet genoemd op deze pagina (afwezigheid, geen uitsluiting). | https://radar.tinsa.es/es | 15-09-2026 |
| R04-05 | Tinsa IMIE provincie Alicante €1.981/m² 2T 2026 (+20,83%); gemeentepagina's alleen Alicante, Alcoy, Benidorm, Elche, Elda, Orihuela, Torrevieja | **Bevestigd** | Exact zo op de pagina. Aanvullend zelf getest: `/alicante/javea-xabia/`, `/alicante/javea/` en `/alicante/denia/` geven HTTP 404, `/alicante/torrevieja/` HTTP 200 (type 3; de geteste slugs zijn door mij gekozen, dus zwakke aanvulling). | https://www.tinsa.es/precio-vivienda/comunitat-valenciana/alicante/ | 15-09-2026 |
| R04-06 | Resales-Online: andermans objecten alleen op eigen website volgens deelrechten; feeds naar derden verboden; afgeleide data eigendom ReSales Andalucía | **Bevestigd** | Letterlijk aanwezig; artikel bijgewerkt **04-05-2026**. Nuance: het verbod kent een uitzondering ("other than for the express purpose of displaying the details on your own website(s)"; doorgifte aan portalen alleen met schriftelijke toestemming van de listing agent die dan zelf een feed levert). | https://support.resales-online.com/en/articles/4885689-terms-conditions-of-usage-resales-online | 15-09-2026 |
| R04-07 | API-key werkt alleen op opgegeven IP; aanmaken via Properties > Feed Out > API Keys; WebAPI V6 verplicht sinds 01-03-2023 | **Bevestigd, met bronfout** | Menupad en IP-beperking staan in het genoemde artikel (bijgewerkt 03-03-2025). **De datum 01-03-2023 staat daar niet**, en ook niet in het V6-documentatieartikel. Wel in het supportartikel "25-07-2022 Email to web developers": "From the 1st of March of 2023, V4.x and V5.x will be removed from the System". Dat is een aankondiging uit 2022 (type 1), geen bevestiging achteraf. De "vier standaardfilters" uit §3.2 van het rapport staan niet in het API-key-artikel (niet teruggevonden). | https://support.resales-online.com/en/articles/4639804-how-to-create-an-api-key · https://support.resales-online.com/en/articles/6495932-25-07-2022-email-to-web-developers-webapi-xml-feeds-2-new-property-types-added | 15-09-2026 |
| R04-08 | MLS 03724: vereniging die gedeelde exclusieven uitwisselt; volgens rapport 02-10-2023 16 kantoren, dekt Benissa t/m Jávea/Dénia, leden wisselen verkoopdata uit (420 objecten) | **Bevestigd als weergave van de bron, met correctie** | De Hispania Homes-pagina (02-10-2023) zegt dit inderdaad ("compuesta por 16 agencias"; 420 verkochte objecten; áticos 2.550 €/m², villa's 2.087 €/m²). Maar: (a) het is een **marketingblog van één makelaar uit 2023**, geen ledenrapport van de vereniging — of Hispania Homes lid is, is niet vastgesteld; (b) de **officiële site** noemt alleen vier oprichters, het gebied "Teulada-Moraira" en het delen van "shared exclusive"-objecten; zij noemt géén ledental, géén dekking van Jávea/Dénia en géén uitwisseling van verkoopdata. CIF zelf bevestigd in het aviso legal: G-42632737, "ASOCIACION INMOBILIARIA MLS TEULADA-MORAIRA". Dekking Jávea en data-uitwisseling blijven **[te verifiëren]** (type 1, derde partij, 3 jaar oud). | https://hispaniahomesmoraira.com/informe-del-mercado-inmobiliario-en-moraira-costa-blanca-norte/ · https://www.mls03724.com/en/about-us/ · http://www.mls03724.com/aviso-legal/ | 15-09-2026 |
| R04-09 | Inmobalia-MLS uitsluitend Costa del Sol (€150–300/mnd + €450 setup); Agora MLS geen kantoren in Jávea, Dénia, Moraira/Teulada, Calp, Benitachell (wel Benissa) | **Bevestigd, met correctie** | Agora: lijst van 22 kantoren in Alicante, dichtstbij Benimo-villas in Benissa — klopt. Inmobalia: prijzen kloppen maar zijn **"VAT not included"** (plus "No refunds"); dat ontbreekt in het rapport. "Uitsluitend Costa del Sol" is een lezing: de site noemt zich "Costa del Sol Property MLS" en bedient "agencies on the Costa del Sol"; alleen de nieuwbouw-MLS staat letterlijk als "(Costa del Sol only)". Voor ons gebied: praktisch geen dekking (type 1 + 4). | https://www.inmobalia.com/ · https://www.agoramls.es/inmobiliarias-alicante/ | 15-09-2026 |
| R04-10 | Witei: geen publieke API, wel XML-export (realtime bijgewerkte link) en webhooks; Inmovilla: API realtime, dagelijkse XML, iframe; Mobilia: publieke API met Swagger | **Weerlegd (deels)** | Witei-XML is **niet realtime**: "Witei updates XML files every 60 minutes". Het XML-formaat is een **export** in Kyero V3 (max. 50 foto's per object), niet "import van Kyero v3" zoals §3.5 zegt. Geen publieke API en webhooks kloppen. Inmovilla klopt (API "al momento", XML "cada noche"/"de forma diaria"). Mobilia: artikel zegt "La documentación pública de la API está disponible mediante Swagger, bajo el nombre Mobilia Public API"; een Swagger-URL staat er niet in en is niet zelf geopend. | https://faq.witei.com/en/articles/2038460-api · https://faq.witei.com/en/articles/865807-xml-export-with-your-properties · https://inmovilla.freshdesk.com/support/solutions/articles/103000118125-conectar-web-externa-con-inmovilla-api-xml-o-iframe · https://www.mobiliagestion.es/noticias-software-inmobiliario/api-crm-mobilia-zapier-n8n-wordpress-agente-ia | 15-09-2026 |
| R04-11 | MIVAU gemeentebestanden 34010210–34010250 (±6,3 MB) bevatten Jávea/Xàbia, Dénia, Teulada, Benitachell, Benissa, Calp; open CSV VDP003_01 (18.512 rijen, bijgewerkt 30-07-2026) alleen provincie | **Bevestigd, met correctie** | Zelf gedownload: 34010210.XLS = 6.307.840 bytes, bevat "Jávea/Xàbia", "Dénia", "Teulada", "Benitachell/Poble Nou…", "Benissa", "Calp"; jaartallen t/m "Año 2026"; HTTP Last-Modified 11-06-2026. **Correctie:** de titels van 34010210–34010250 luiden "Número (total) de transacciones inmobiliarias … por municipios" — **alleen aantallen**; de waardetabellen (3.1–3.4) staan onder "Desagregación territorial: comunidades autónomas y provincias". VDP003_01.csv: 18.512 datarijen, geen gemeentekolom, laatste periode 2026-T1; HTTP Last-Modified 03-07-2026; "30-07-2026" is de *catalogusdatum* op datos.gob.es, de distributiedatum is 29-04-2026. | https://apps.fomento.gob.es/BoletinOnline2/?nivel=2&orden=34000000 · https://apps.fomento.gob.es/BoletinOnline2/sedal/34010210.XLS · https://cdn.mivau.gob.es/portal-web-mivau/Datos_MIVAU/CSV/VDP003_01.csv | 15-09-2026 |
| R04-12 | 35103500.XLS (valor tasado gemeenten >25.000 inw.) bevat Jávea/Xábia, Calpe/Calp, Dénia; Teulada ontbreekt | **Bevestigd** | Zelf gedownload (3.958.784 bytes, laatst opgeslagen 27-05-2026): "Jávea/Xábia", "Calpe/Calp", "Dénia", "Benidorm", "Torrevieja" aanwezig; "Teulada", "Benissa", "Altea" niet. | https://apps.fomento.gob.es/BoletinOnline2/?nivel=2&orden=35000000 · https://apps.fomento.gob.es/BoletinOnline2/sedal/35103500.XLS | 15-09-2026 |
| R04-13 | MIVAU-datasets op datos.gob.es onder CC BY 4.0, kwartaal; commercieel hergebruik toegestaan (Ley 37/2007, RD 1495/2011) met bronvermelding | **Bevestigd, met nuance** | Beide datasetpagina's: "CC_BY_4_0", "Trimestral", "Cobertura geográfica España". Maar de enige distributie per dataset is de **CSV op provincieniveau**; de gemeentelijke XLS-bestanden van het Boletín Online zijn **geen** distributie van die datasets. De licentie van die XLS-bestanden is dus niet via datos.gob.es vastgesteld → **[te verifiëren]** (het MIVAU-aviso legal gaf 403). Het aviso legal van datos.gob.es is de algemene regeling van dat portaal (Red.es), "sin perjuicio de las condiciones particulares". Als "Legislación aplicable" noemt de datasetpagina RD 1225/2024 (Plan Estadístico Nacional 2025-2028). | https://datos.gob.es/es/catalogo/e05233601-transacciones-inmobiliarias-de-vivienda · https://datos.gob.es/es/catalogo/e05233601-valor-tasado-de-la-vivienda · https://datos.gob.es/es/aviso-legal · https://www.boe.es/eli/es/rd/2024/12/03/1225 | 15-09-2026 |
| R04-14 | INE-API IPV (Id 15): zes tabellen, alle nationaal of CCAA; 2T 2026 gepubliceerd 07-09-2026 (+12,2%), basis 2025 vanaf 1T 2026 | **Bevestigd** | Zelf getest: `OPERACION/IPV` → Id 15, Cod_IOE 30457; `TABLAS_OPERACION/IPV` → 6 tabellen (ponderaciones nacional; índices por CCAA). `DATOS_TABLA/80270?nult=1` → Nacional general variación anual 12,2 (2026, periode 20), nieuw 7,4, tweedehands 12,9. INE-pagina: "Trimestre 2/2026", 07/09/2026, base 2025 vanaf 1T 2026. | https://servicios.ine.es/wstempus/js/ES/TABLAS_OPERACION/IPV · https://www.ine.es/dyngs/INEbase/es/operacion.htm?c=Estadistica_C&cid=1254736152838&menu=ultiDatos&idp=1254735976607 | 15-09-2026 |
| R04-15 | INE ETDP maandelijks nationaal/regio/provincie zonder gemeenten; juni 2026: 206.138 fincas, 59.288 woningverkopen, gepubliceerd 07-08-2026 | **Bevestigd** | INE-pagina bevestigt cijfers en datum. Zelf via API: tabel 6150 heeft 360 reeksen (landelijk + CCAA + provincies × 5 varianten), o.a. "Alicante/Alacant. General. Compraventa. Número."; geen gemeenten; laatste waarde nationaal 59.288 (2026, periode 6). | https://www.ine.es/dyngs/INEbase/es/operacion.htm?c=Estadistica_C&cid=1254736171438&menu=ultiDatos&idp=1254735576757 · https://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/6150?nult=1 | 15-09-2026 |
| R04-16 | Registradores ERI: land/regio/provincie/hoofdsteden (1T 2025: 181.625 verkopen; CV 28,3% buitenlandse kopers); opendata.registradores.org weigert | **Bevestigd, met nuance** | Cijfers kloppen (publicatie 08-05-2025). Het voorbeeld is **verouderd**: op de statistiekpagina staan ERI-rapporten t/m **2T 2026**. opendata.registradores.org gaf op 15-09-2026 opnieuw "Request Rejected" (curl én WebFetch). Via zoekresultaten blijkt het portaal datasets als "Compraventas de inmuebles, uso residencial, por provincia" te hebben; of er gemeentedata is, blijft onbekend. Er bestaan losse monografieën op gemeenteniveau (bv. Elche). | https://www.registradores.org/en/navegacion-por-categorias/-/asset_publisher/eXXttUcwzL5U/content/estadistica-registral-inmobiliaria-1er-trimestre-de-2025 · https://www.registradores.org/actualidad/portal-estadistico-registral/estadisticas-de-propiedad · https://opendata.registradores.org/dataset/dataset | 15-09-2026 |
| R04-17 | Portal Estadístico del Notariado (sinds 23-10-2025): maandelijks €/m², oppervlak, totaalprijs, aantal verkopen op land t/m postcode en zelfgetekend gebied; registratie gratis en vrijwillig | **Bevestigd** | Letterlijk: "nacional, autonómico, provincial, municipal, código postal e incluso dibujando tu propia área", "periodicidad mensual", "El registro es voluntario y gratuito". De startdatum staat niet op penotariado.com zelf, wel in Infoconstrucción (23-10-2025; secundaire bron, type 1). Download = "gráficos comparativos", geen ruwe data gezien. | https://www.penotariado.com/ · https://www.infoconstruccion.es/noticias/20251023/presentacion-portal-estadistico-notariado | 15-09-2026 |
| R04-18 | Voorwaarden penotariado: alleen persoonlijk gebruik, geen commercieel gebruik, geen opname in databanken voor commerciële raadpleging, ook met bronvermelding | **Bevestigd, met precisering** | Letterlijk: "para su uso exclusivo personal", "no permitiéndose el uso comercial", en het databankverbod betreft bestanden "susceptibles de consulta individualizada con fines comerciales por otras personas físicas o jurídicas … aunque se exprese la procedencia". Het databankverbod mikt dus op raadpleging door derden; intern zakelijk gebruik valt al onder het algemene verbod op commercieel gebruik. Geen versiedatum van de voorwaarden vermeld. | https://www.penotariado.com/inmobiliario/terminos-y-condiciones | 15-09-2026 |
| R04-19 | Valor de referencia per object in de Sede, alleen met certificaat/DNIe of Cl@ve; waardekaarten openbaar (laatste 09-10-2025); vrije OVC-webservice zonder sleutel (JAVEA/XABIA) | **Bevestigd** | Sede-pagina: keuze tussen "Certificado electrónico … o DNI electrónico" en "Cl@ve"; waardekaarten 2026 gepubliceerd 09-10-2025 (2025: 25-09-2024). OVC zelf getest: HTTP 200, `"nm":"JAVEA/XABIA"`, cd 3, cmc 82. Niet vastgesteld: of een niet-eigenaar met Cl@ve de referentiewaarde van *elk* object mag opvragen [te verifiëren]. | https://www1.sedecatastro.gob.es/Accesos/SECAccvr.aspx · https://ovc.catastro.meh.es/OVCServWeb/OVCWcfCallejero/COVCCallejero.svc/json/ObtenerMunicipios?Provincia=ALICANTE&Municipio=JAVEA | 15-09-2026 |
| R04-20 | "Propertyflows" bestaat niet als Spaans makelaars-CRM; propertyflows.com is Engelstalig AI-leadplatform; propertyflows.es bestaat niet in DNS | **Bevestigd (als "niet gevonden")** | dig: propertyflows.es en www.propertyflows.es → NXDOMAIN; propertyflows.com → Cloudflare, titel "PropertyFlows", tekst "We Help Property Managers Turn Leads Into Booked Appointments Using AI Automation", geen "Spain/España". Een zoekvraag "PropertyFlows CRM inmobiliario" gaf geen treffer. Niet-bestaan is niet te bewijzen: formuleer als "niet gevonden". De naam komt niet voor in MASTERPROMPT.md; herkomst van de naam onbekend. | https://propertyflows.com/ | 15-09-2026 |

---

## 2. Aanvullende bevindingen (nieuw, met bron)

| # | Bevinding | Bron | Datum | Type |
|---|---|---|---|---|
| A1 | MIVAU Boletín Online geeft per gemeente **alleen het aantal** transacties (totaal, libre, protegida, nueva, segunda mano). "Valor de las transacciones" en "Valor medio" zijn uitsluitend "Desagregación territorial: comunidades autónomas y provincias". | https://apps.fomento.gob.es/BoletinOnline2/?nivel=2&orden=34000000 | 15-09-2026 | 3 |
| A2 | Het gemeentebestand 34010210.XLS loopt t/m "Año 2026"; HTTP Last-Modified 11-06-2026 (opgeslagen 05-06-2026). VDP003_01.csv loopt t/m 2026-T1. Vertraging voor gemeentecijfers: ruim een kwartaal. | https://apps.fomento.gob.es/BoletinOnline2/sedal/34010210.XLS · https://cdn.mivau.gob.es/portal-web-mivau/Datos_MIVAU/CSV/VDP003_01.csv | 15-09-2026 | 3 |
| A3 | datos.gob.es-catalogus van MIVAU (publisher E05233601) telt 8 datasets (SIU grafisch, Precio medio del suelo, SIU alfanumeriek, Viviendas iniciadas/terminadas, Transacciones, Valor tasado, Parque de viviendas, Vivienda protegida); VDP001_01 staat er niet in. API-veld `license` is leeg, HTML-pagina toont CC_BY_4_0. | https://datos.gob.es/apidata/catalog/dataset/publisher/E05233601.json | 15-09-2026 | 3 |
| A4 | VDP001_01.csv: kolommen `COD_PROVINCIA;PROVINCIA;COD_POSTAL;NOMBRE_MUNICIPIO;ELEMENTO;TIPO_VIVIENDA;TIPO_MEDIDA;AÑO;VALOR`, 37.788.115 bytes, Last-Modified 22-05-2026. Titel/licentie blijven onbekend (alleen eerste 1,5 KB opgehaald). | https://cdn.mivau.gob.es/portal-web-mivau/Datos_MIVAU/CSV/VDP001_01.csv | 15-09-2026 | 3 |
| A5 | Resales-Online omschrijft WebAPI V6 als "Add a property search on your website that will update in real time and without the need of a database" — de API is bedoeld voor live weergave, niet voor opslag. Dat versterkt het juridische punt uit §3.2. Er bestaat ook een apart artikel "NEW Static XML feed for shared properties" dat R04 niet heeft onderzocht. | https://support.resales-online.com/en/articles/5682509-webapi-v6-full-documentation-for-web-developers | 15-09-2026 | 1 |
| A6 | Apibolsa: deelname is voor "asociados o colegiados que tengan contratado nuestra aplicación inmobiliaria INMOPC"; automatische upload "siempre y cuando su software inmobiliario genere un XML con formato Kyero 3.0". Dus een extra softwarevoorwaarde naast het colegiado-lidmaatschap. | https://www.apibolsa.es/bolsa-inmobiliaria-como-funciona-mls.html | 15-09-2026 | 1 |
| A7 | Witei-XML wordt elk uur ververst en volgt Kyero V3 met maximaal 50 foto's per object. | https://faq.witei.com/en/articles/865807-xml-export-with-your-properties | 15-09-2026 | 1 |
| A8 | Casafari's "45 Million Registered property sales with closing prices" staat zonder landenopgave op de homepage; of Spaanse (Marina Alta) verkoopprijzen erin zitten is ONBEKEND. | https://www.casafari.com/ | 15-09-2026 | 1/7 |
| A9 | Tinsa Digital AVM gebruikt volgens eigen zeggen "solo … datos de viviendas a las cuales ha accedido, medido y verificado un tasador" en noemt markten Spanje, Chili, Mexico en Colombia. | https://www.tinsadigital.com/que-hacemos/avm/ | 15-09-2026 | 1 |
| A10 | Inmobalia: alle prijzen "VAT not included. No refunds"; jaarbetaling 10% korting. | https://www.inmobalia.com/ | 15-09-2026 | 1 |
| A11 | Notariado CIEN (juni, jaar niet expliciet in de samenvatting maar in lijn met 2026): 67.529 verkopen, −4,0% j/j, 2.114 €/m² — het rapport klopt hier. | https://www.notariado.org/liferay/web/cien/estadisticas-principales/inmuebles/evolucion-de-compraventa-de-viviendas | 15-09-2026 | 2 |
| A12 | mls03724.com toont bij curl een JavaScript-"Security Check"; WebFetch kon de pagina's wel lezen. Niet omzeild. | https://www.mls03724.com/en/ | 15-09-2026 | 3 |

---

## 3. Wat blijft onbewezen

1. Of TREE Properties lid is van Resales-Online, MLS 03724, MLS Costa of het Colegio API Alicante — geen bron gezien.
2. Werkelijke dekking van Jávea bij Casafari, Brainsre, Accumin, MLS Costa, MLS Mediaelx en Resales-Online (aantallen objecten, ververstijd). De Resales-Online-blog "MLS Javea" is marketingtekst, geen ledentelling.
3. MLS 03724: huidig ledental, dekking buiten Teulada-Moraira, en of verkoopdata onder leden contractueel wordt gedeeld (alleen een derdenblog uit 2023).
4. Btw-status van de Tinsa Radar-prijzen.
5. Licentie van de gemeentelijke XLS-bestanden in het Boletín Online (CC BY 4.0 is alleen aan de provinciale CSV's gekoppeld).
6. Bron "ANCERT" voor MIVAU Transacciones (samenvatting regel 8): de methodologiepagina van mivau.gob.es gaf 403; niet bevestigd.
7. MLS Mediaelx "45+ kantoren, 100+ agenten": niet op de geciteerde pagina gevonden (wel "Over 3,000 properties").
8. Of de Mobilia Swagger-documentatie echt openbaar bereikbaar is (geen URL gezien).
9. Of een niet-eigenaar de Catastro-referentiewaarde van willekeurige objecten mag opvragen, en of de consulta masiva die waarde bevat.
10. Fijnmazigheid van opendata.registradores.org (geblokkeerd).
11. Inhoudelijke cijfers per gemeente uit de MIVAU-XLS (niet geparseerd; geen XLS-lezer beschikbaar).
12. De juridische lijn "eigen objecten wel, netwerkobjecten niet" (type 4, jurist nodig).

---

## 4. Fouten in het rapport buiten de claimlijst

| # | Plaats in R04 | Wat er staat | Wat klopt | Ernst |
|---|---|---|---|---|
| F1 | §4.1 tabel "MIVAU — Transacciones", §4.3 tabel (rij 1 en 5), samenvatting regel 8 | "Aantal en waarde (totaal, gemiddeld) … Gemeente"; "MIVAU Transacciones (gemiddelde waarde per gemeente per kwartaal)"; "hét toetsingscijfer per gemeente" | Per gemeente alleen **aantal** transacties; waarde/gemiddelde waarde alleen per regio en provincie (A1). MIVAU levert dus géén gemeentelijke transactieprijs om vraagprijzen in Jávea mee te toetsen; alleen marktdiepte. Voor prijsniveau per gemeente blijven valor tasado (taxatie, geen transactie) en penotariado (alleen handmatig) over. | **Hoog** — dragende conclusie |
| F2 | §2.1 (Tinsa Radar), §4.1 en §5 register (MIVAU Transacciones, MIVAU Valor tasado, INE IPV, INE ETDP, Catastro OVC, datos.gob.es) | Status "GEVERIFIEERD EN ACTIEF" | Niets hiervan is aangesloten of draait; er is één handmatige test gedaan en Tinsa Radar is niet afgenomen. Volgens de projectregels ("monitoring heet pas actief als ze getest draait") hoort hier "TECHNISCH ONDERZOEK NODIG" (open data, nog geen koppeling) of "ALLEEN HANDMATIG" (Radar, zolang er geen abonnement is). | **Hoog** — misleidt het bronnenregister |
| F3 | §3.5 tabel Witei, register | "XML-link realtime bijgewerkt"; "import van Kyero v3" | Elk uur ververst; export in Kyero V3-formaat (A7). | Middel |
| F4 | §3.1 en §5 Inmobalia | "Starter €150, Full €225, Pro €300 per maand; €450 setup" | Allemaal **exclusief btw** (A10). | Middel (regel: geen bedragen zonder btw-vermelding) |
| F5 | §2.1, §5, §6.5 Tinsa Radar | €29/€99/€259 zonder btw-vermelding | Btw-status niet vermeld op bron → markeren als ONBEKEND. | Laag-middel |
| F6 | §3.1 en §3.4 APIred/Apibolsa | "Leden: alleen colegiados; import via XML Kyero 3.0" | Deelname vereist ook een contract voor de software INMOPC (A6); Kyero 3.0 staat op apibolsa.es, niet op apired.com. | Middel |
| F7 | §3.1, §3.3 MLS 03724 | "Dekt Jávea: Ja"; "deelt exclusieven én verkoopdata"; "ledenrapport" | Alleen onderbouwd door een blog van één makelaar uit 2023; officiële site noemt alleen Teulada-Moraira en gedeelde exclusieven. Dekking en data-uitwisseling [te verifiëren]. | Middel |
| F8 | §4.3 laatste alinea | Casafari's "45 Million Registered property sales" als bron die transacties kan bevestigen | Geen landenopgave; voor Spanje/Marina Alta onbewezen (A8). | Middel |
| F9 | §3.2 | "Bij aanmaak worden vier standaardfilters meegegeven" en V6 verplicht sinds 01-03-2023 met het API-key-artikel als bron | Filters niet teruggevonden; datum komt uit een ander artikel (zie R04-07). | Laag |
| F10 | §3.1 MLS Mediaelx | "45+ kantoren, 100+ agenten" | Niet op de geciteerde pagina gevonden. | Laag |
| F11 | §4.1 Registradores | Voorbeeldcijfers 1T 2025 | Rapporten t/m 2T 2026 beschikbaar; voorbeeld is ruim een jaar oud. | Laag |
| F12 | §4.1 MIVAU Transacciones | "CSV laatst bijgewerkt 30-07-2026" | 30-07-2026 is de catalogusdatum; bestand Last-Modified 03-07-2026, distributiedatum 29-04-2026, data t/m 2026-T1. | Laag |
| F13 | §4.1 MIVAU Transacciones / Valor tasado | Licentie "CC BY 4.0" ook toegepast op de gemeentelijke XLS | CC BY 4.0 is gekoppeld aan de CSV-distributies; XLS-licentie niet vastgesteld. | Middel |
| F14 | §2.2 | Casafari-voorwaarden als actuele contractbasis | Gebruiksvoorwaarden dateren van 2018 en regelen de website; abonnements-/API-voorwaarden zijn niet ingezien. | Laag-middel |

Geen persoonsgegevens van particulieren aangetroffen in R04. De vermelde telefoonnummers en e-mailadressen zijn zakelijke contactgegevens van bedrijven en instanties (toegestaan). De auteursmetadata in de MIVAU-XLS-bestanden bevatten namen van ambtenaren; die zijn hier bewust niet overgenomen.

---

## 5. Bronnenlijst (URL · controledatum · bewijstype)

| # | URL | Datum | Type |
|---|---|---|---|
| 1 | https://www.casafari.com/products/property-data-api/ | 15-09-2026 | 1 |
| 2 | https://www.casafari.com/faq/ | 15-09-2026 | 1 |
| 3 | https://www.casafari.com/terms-of-use | 15-09-2026 | 1 |
| 4 | https://www.casafari.com/ | 15-09-2026 | 1 |
| 5 | https://www.accumin.com/newsroom/corporate-actions/the-tinsa-group-acquires-urbandata-analytics | 15-09-2026 | 1 |
| 6 | https://www.accumin.com/newsroom/corporate-actions/tinsa-digital-deyde-datacentric-and-urbandata-analytics-join-forces-in-accumin-intelligence | 15-09-2026 | 1 |
| 7 | https://www.accumin.com/intelligence/data/real-estate | 15-09-2026 | 1 |
| 8 | https://radar.tinsa.es/es | 15-09-2026 | 1 |
| 9 | https://www.tinsa.es/precio-vivienda/comunitat-valenciana/alicante/ (+ slugtests javea/denia) | 15-09-2026 | 1/3 |
| 10 | https://www.tinsadigital.com/que-hacemos/avm/ | 15-09-2026 | 1 |
| 11 | https://support.resales-online.com/en/articles/4885689-terms-conditions-of-usage-resales-online | 15-09-2026 | 1 |
| 12 | https://support.resales-online.com/en/articles/4639804-how-to-create-an-api-key | 15-09-2026 | 1 |
| 13 | https://support.resales-online.com/en/articles/5682509-webapi-v6-full-documentation-for-web-developers | 15-09-2026 | 1 |
| 14 | https://support.resales-online.com/en/articles/6495932-25-07-2022-email-to-web-developers-webapi-xml-feeds-2-new-property-types-added | 15-09-2026 | 1 |
| 15 | https://www.resales-online.com/ (HTTP 403) | 15-09-2026 | 3 |
| 16 | https://hispaniahomesmoraira.com/informe-del-mercado-inmobiliario-en-moraira-costa-blanca-norte/ | 15-09-2026 | 1 |
| 17 | https://www.mls03724.com/en/about-us/ | 15-09-2026 | 1 |
| 18 | http://www.mls03724.com/aviso-legal/ | 15-09-2026 | 1 |
| 19 | https://www.agoramls.es/inmobiliarias-alicante/ | 15-09-2026 | 1 |
| 20 | https://www.inmobalia.com/ | 15-09-2026 | 1 |
| 21 | https://www.inmoba.com/779-faq-inmobalia-mls-equals-quality | 15-09-2026 | 1 |
| 22 | https://www.mlscosta.com/ | 15-09-2026 | 1 |
| 23 | https://mediaelx.net/en/mls-mediaelx/ | 15-09-2026 | 1 |
| 24 | http://www.apired.com/ | 15-09-2026 | 1 |
| 25 | https://www.apibolsa.es/bolsa-inmobiliaria-como-funciona-mls.html | 15-09-2026 | 1 |
| 26 | https://www.deniacasas.es/en/about-us/ | 15-09-2026 | 1 |
| 27 | https://faq.witei.com/en/articles/2038460-api | 15-09-2026 | 1 |
| 28 | https://faq.witei.com/en/articles/865807-xml-export-with-your-properties | 15-09-2026 | 1 |
| 29 | https://inmovilla.freshdesk.com/support/solutions/articles/103000118125-conectar-web-externa-con-inmovilla-api-xml-o-iframe | 15-09-2026 | 1 |
| 30 | https://www.mobiliagestion.es/noticias-software-inmobiliario/api-crm-mobilia-zapier-n8n-wordpress-agente-ia | 15-09-2026 | 1 |
| 31 | https://propertyflows.com/ + dig propertyflows.es / www.propertyflows.es (NXDOMAIN) | 15-09-2026 | 3 |
| 32 | https://apps.fomento.gob.es/BoletinOnline2/?nivel=2&orden=34000000 | 15-09-2026 | 2/3 |
| 33 | https://apps.fomento.gob.es/BoletinOnline2/sedal/34010210.XLS | 15-09-2026 | 3 |
| 34 | https://apps.fomento.gob.es/BoletinOnline2/?nivel=2&orden=35000000 | 15-09-2026 | 2/3 |
| 35 | https://apps.fomento.gob.es/BoletinOnline2/sedal/35103500.XLS | 15-09-2026 | 3 |
| 36 | https://cdn.mivau.gob.es/portal-web-mivau/Datos_MIVAU/CSV/VDP003_01.csv | 15-09-2026 | 3 |
| 37 | https://cdn.mivau.gob.es/portal-web-mivau/Datos_MIVAU/CSV/VDP001_01.csv (eerste 1,5 KB) | 15-09-2026 | 3 |
| 38 | https://datos.gob.es/es/catalogo/e05233601-transacciones-inmobiliarias-de-vivienda | 15-09-2026 | 2 |
| 39 | https://datos.gob.es/es/catalogo/e05233601-valor-tasado-de-la-vivienda | 15-09-2026 | 2 |
| 40 | https://datos.gob.es/apidata/catalog/dataset/publisher/E05233601.json | 15-09-2026 | 3 |
| 41 | https://datos.gob.es/es/aviso-legal | 15-09-2026 | 2 |
| 42 | https://www.boe.es/eli/es/rd/2024/12/03/1225 | 15-09-2026 | 2 |
| 43 | https://servicios.ine.es/wstempus/js/ES/OPERACION/IPV · /TABLAS_OPERACION/IPV · /DATOS_TABLA/80270?nult=1 | 15-09-2026 | 3 |
| 44 | https://www.ine.es/dyngs/INEbase/es/operacion.htm?c=Estadistica_C&cid=1254736152838&menu=ultiDatos&idp=1254735976607 | 15-09-2026 | 2 |
| 45 | https://servicios.ine.es/wstempus/js/ES/TABLAS_OPERACION/ETDP · /DATOS_TABLA/6150?nult=1 | 15-09-2026 | 3 |
| 46 | https://www.ine.es/dyngs/INEbase/es/operacion.htm?c=Estadistica_C&cid=1254736171438&menu=ultiDatos&idp=1254735576757 | 15-09-2026 | 2 |
| 47 | https://www.registradores.org/en/navegacion-por-categorias/-/asset_publisher/eXXttUcwzL5U/content/estadistica-registral-inmobiliaria-1er-trimestre-de-2025 | 15-09-2026 | 2 |
| 48 | https://www.registradores.org/actualidad/portal-estadistico-registral/estadisticas-de-propiedad | 15-09-2026 | 2 |
| 49 | https://opendata.registradores.org/ (Request Rejected) | 15-09-2026 | 3 |
| 50 | https://www.notariado.org/liferay/web/cien/estadisticas-principales/inmuebles/evolucion-de-compraventa-de-viviendas | 15-09-2026 | 2 |
| 51 | https://www.penotariado.com/ | 15-09-2026 | 2 |
| 52 | https://www.penotariado.com/inmobiliario/terminos-y-condiciones | 15-09-2026 | 2 |
| 53 | https://www.infoconstruccion.es/noticias/20251023/presentacion-portal-estadistico-notariado | 15-09-2026 | 1 |
| 54 | https://www1.sedecatastro.gob.es/Accesos/SECAccvr.aspx | 15-09-2026 | 2 |
| 55 | https://ovc.catastro.meh.es/OVCServWeb/OVCWcfCallejero/COVCCallejero.svc/json/ObtenerMunicipios?Provincia=ALICANTE&Municipio=JAVEA | 15-09-2026 | 3 |

**Geblokkeerd of mislukt (niet omzeild):** resales-online.com (403); mivau.gob.es (403, dus ANCERT-bron en XLS-licentie niet te controleren); opendata.registradores.org ("Request Rejected", ook via WebFetch); confilegal.com (403); mls03724.com via curl (JavaScript-beveiligingscheck; WebFetch werkte wel).

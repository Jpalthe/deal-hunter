# B05 — Portalen, feedstandaarden en feed-tussenpartijen

Controledatum van alles hieronder: **16-09-2026**. Bewijstypen: 1 = door aanbieder vermeld,
2 = officiële bron, 3 = zelf vastgesteld, 4 = afleiding, 5 = berekening, 6 = professional,
7 = onbekend/tegenstrijdig.

## Samenvatting (8 regels)

1. Er zijn drie **buitenlandse portalen met échte Jávea-voorraad** die nog niet in het register staan: Rightmove Overseas (489 objecten Jávea), Immowelt (643 "Haus kaufen" Xàbia/Jávea) en Zoopla Overseas/PrimeLocation (2.096 huizen provincie Alicante). Alle drie alleen handmatig leesbaar; geen leesfeed, geen API.
2. Nederlands: **huisenaanbod.nl** toont 233 woningen in Jávea en importeert van 30+ CRM-formaten; Costa Select bleek een aankoopmakelaar, geen portaal.
3. Spaanse tweede ring: **tucasa.com** (Iberanuncios S.L.) en **hogaria.net** nemen ook advertenties van particulieren — de enige nieuwe kans op *niet-makelaarsaanbod* in dit onderzoek; beide zonder leesroute.
4. Twee gemiste routes bij partijen die we al kennen: **Inmovilla/apinmo** publiceert een openbare API-documentatie én een demo-XML (159 velden, mét `rcatastral` en `conservacion`), en **Resales-Online** heeft een volledig openbaar ontwikkelaarsportaal (devdocs) plus een "Static Network feed" — die laatste mag contractueel alleen op de eigen website.
5. **Inmofactory bestaat niet meer als eigen partij**: het domein leidt door naar Fotocasa Pro (Adevinta). **miparcela.com** leidt door naar Indomio. Beide dus geen nieuwe bronnen.
6. **Kyero v4 bestaat niet**: de v4-bestanden op feeds.kyero.com geven 404 terwijl het v3-bestand 200 geeft. Er is ook geen Europese "Real Estate Standard Feed"; RESO/RETS is Amerikaans, en de Spaanse markt is te versnipperd voor één standaard.
7. **Nestoria Spanje is dood** (401 + zelfondertekend certificaat) — een van de weinige ooit vrij leesbare vastgoed-API's is daarmee weg.
8. Advies: naast Kyero v3 alleen **Inmovilla/apinmo-XML** (eerst) en **Resales-Online v1.5/export** (tweede) inbouwen, plus een generieke CSV/Excel-val; samen ongeveer drie tot vier dagdelen werk. OpenImmo pas als een Duitstalige partner erom vraagt.

---

## 1. Methode en beperkingen

Per site één of twee verzoeken (WebFetch of `curl` met een gewone browser-User-Agent). Niets omzeild,
geen inlogmuren gepasseerd, geen scrapers gebruikt. Waar een site 403 of 500 gaf, staat dat in §10.
Tellingen die uit een zoekresultaat komen en niet zelf zijn gezien, staan als bewijstype 7 met
[te verifiëren]. Alle "aantallen in Jávea" zijn momentopnamen van 16-09-2026 en zeggen niets over
overlap met wat we al hebben — die overlap is niet gemeten en is per portaal een open vraag (§9).

Onderscheid dat in dit hele stuk wordt volgehouden:
- **Publiceerkoppeling** = wij (of een partner) zetten ónze advertenties op een portaal. Voor Deal Hunter waardeloos, behalve als hefboom: wie zelf publiceert, kan ons dezelfde feed geven.
- **Leesroute** = wij mogen het aanbod van anderen ophalen. Alleen dit levert objecten op.
- **Partnerfeed** = een makelaar geeft ons rechtmatig zijn eigen bestand. Dat is in de praktijk de enige schaalbare weg in dit segment.

---

## 2. Deel A — Portalen die nog niet in het register stonden

### 2.1 Rightmove Overseas (VK)

- Pagina https://www.rightmove.co.uk/overseas-property-for-sale/Javea.html gaf op 16-09-2026 letterlijk **"489 results"** (bewijstype 3).
- Zichtbare aanbieders op die pagina (bewijstype 3): Fine and Country Costa Blanca North (Dénia), Blumelia Real Estate, The Agency Costa Blanca North, COSTA HOUSES LUXURY VILLAS SLU, BARTOLOME BAS SL, AREA Costa Blanca, Welcome Estates, Hamiltons of London, Prestige Property Group, TEKCE, Tabaira Real Estate, Chersun Properties S.L. Een deel daarvan staat in ons kantorenregister (R06), een deel niet — dat zijn concrete acquisitie-ingangen.
- Leesroute: **geen**. Rightmove heeft alleen een publiceer-API (zie §3.6). De categoriepagina https://www.rightmove.co.uk/overseas-property/in-Javea.html leverde bij ophalen alleen navigatie op, geen objecten (bewijstype 3).
- Beoordeling: **deels uniek** — UK-gerichte kantoren (Hamiltons, Prestige, Fine & Country) publiceren hier soms wél en op de Spaanse portalen niet. Waarde zit in ontdekking, niet in massale import.

### 2.2 Zoopla Overseas / PrimeLocation (VK)

- https://www.zoopla.co.uk/overseas/houses/spain/valencia/alicante/ gaf **"2096 results"** voor huizen te koop in de provincie Alicante, met Jávea-objecten zichtbaar (twee voorbeelden van € 2.690.000 en € 1.890.000) en Moraira en Benitachell als aangrenzende zoekgebieden (bewijstype 3).
- Zichtbare aanbieders: Baerz & Co South Europe, **Properstar**, Petra Honig Inmobiliaria S.L, Spain Property Shop SL (bewijstype 3). Dat Properstar zelf als "makelaar" adverteert, laat zien dat een deel van deze voorraad via syndicatie binnenkomt en dus dubbel is.
- Leesroute: **geen openbare API**. Wat er aan "Zoopla API" te vinden is, zijn commerciële scrapers (Apify, ScrapingBee, PropAPIS, RealtyAPI) — die vallen onder het scraping-verbod en gebruiken we niet.
- Beoordeling: **deels uniek**, zelfde patroon als Rightmove.

### 2.3 A Place in the Sun (VK)

- https://www.aplaceinthesun.com/advertise/website/list-your-properties (bewijstype 1): "Properties uploaded manually or by XML feed"; "Prices vary depending on the number of properties you wish to advertise and where your properties are located"; landen: Spanje, Frankrijk, Portugal, Italië, Florida, Cyprus, Griekenland, Turkije.
- Volgens leveranciers van feedsoftware (Mediaelx, Kyero-addons; bewijstype 7) accepteert APITS Kyero-, Resales- en vergelijkbare feeds. Zelf niet bevestigd door APITS.
- Leesroute: **geen**. Dekking Jávea niet gemeten.
- Beoordeling: **laag**. Zelfde kantoren als Kyero/Rightmove; alleen handmatig als extra vindplaats.

### 2.4 Immowelt / Immonet (Duitsland) — de grootste nieuwe vindplaats

- https://www.immowelt.de/suche/ausland/kaufen/haus/valencianische-gemeinschaft/xabia-javea/ad08es2329 gaf HTTP 200 met paginatitel **"Haus kaufen in Xàbia / Jávea, Alicante - 643 Angebote"** (bewijstype 3, alleen huizen, dus exclusief appartementen en percelen).
- Duitstalige kantoren met zwaartepunt in onze driehoek adverteren hier (zoekresultaat, bewijstype 7: Schaich Immobilien S.L., Els Poblets, "über 1.000 Immobilien" rond Dénia, Jávea, Els Poblets, Oliva, Moraira, Benissa en Calpe) — [te verifiëren] op de kantoorpagina zelf.
- Leesroute: **geen**. Import bij Duitse portalen loopt via **OpenImmo** (§3.7); dat is een publiceerformaat, maar het betekent wel dat een Duitstalige partner ons zonder extra werk een OpenImmo-bestand kan geven (bewijstype 4).
- Beoordeling: **deels uniek en hoog geprioriteerd voor ontdekking** — dit is het enige kanaal in dit onderzoek waar de Duitstalige helft van de markt zichtbaar wordt, en die overlapt maar deels met Kyero.

### 2.5 huisenaanbod.nl (Nederland)

- https://www.huisenaanbod.nl/nl/Huizen-te-koop-in-Javea-Xabia-Costa-Blanca-Valencia-Spanje/ — paginatitel op 16-09-2026: **"233 Huizen te koop in Javea Xabia Costa Blanca Valencia Spanje"** (bewijstype 3).
- Makelaarspagina https://www.huisenaanbod.nl/nl/buitenlandse-woningen-aanbieden-voor-makelaars/ (bewijstype 1): tarief "ca. € 15 p.m. (kosten per dag = € 0,50)", 25 advertenties ≈ € 38/maand, 250 ≈ € 90/maand, "Géén contract; U kunt iedere dag stoppen"; telefoon +31 575 - 55 22 08.
- Zelfde pagina noemt de systemen waaruit automatisch geïmporteerd wordt (bewijstype 1, letterlijke lijst): *ActivImmo, Adaptimmo, Apimo, Dizio, Dragonstack, Ego, Espacos-web, Expertagent, Gestao de Portais, Gestim, Hektor, Immofacile-Orisha, Inmoba, Inmoenter, Inmoweb, Kyero, La Boite Immo, Moonshapes, Mydatafeed, Netty, Novoportal, OnOffice, Openimmo, Pyber, Realworks, Resales Online, Sooprema, Thinkspain, Ubiflow, XML2U, X-IMO*. Dat is meteen het beste openbare overzicht van de feedfamilies die in dit marktsegment rondgaan.
- Leesroute: **geen** (niets over export naar derden op de pagina).
- Beoordeling: **deels uniek** — Nederlandstalige kantoren die niet op Kyero staan.

Niet meegeteld: **Costa Select** (costaselect.com) bleek geen portaal maar een Nederlandse *aankoop*makelaar: "Costa Management BV (KVK 96824522)", Amersfoort, met kantoren in Benitachell en Valencia en Spaanse partner "Stam Immo Group SL" (ASAPI 556, RAICV 1292); één Jávea-object zichtbaar (bewijstype 1/3). Hoort thuis in het kantorenregister R06, niet hier.

### 2.6 tucasa.com (Iberanuncios S.L.) — particulieren én banken

- Eigenaar: "Copyright © 2026, Iberanuncios, S.L., todos los derechos reservados" (bewijstype 1, homepage).
- Volgens het zoekresultaat van de Jávea-pagina: **148 woningen te koop in Jávea (Xàbia) vanaf € 265.000, van particulieren, makelaars én banken** (bewijstype 7, [te verifiëren]). De pagina zelf gaf zowel via WebFetch (502) als via curl (500) een serverfout — zie §10.
- Leesroute: **geen** vermeld. Wel gratis plaatsen door particulieren ("publicar gratis"), en tucasa komt terug in de doorplaatslijsten van distributiesoftware.
- Beoordeling: **deels uniek**. Het particuliere en bancaire deel is precies wat in onze makelaarsfeeds ontbreekt. Waarde staat of valt met een hertelling zodra de site het weer doet.

### 2.7 hogaria.net

- Homepage bereikbaar (bewijstype 3); voetnoot "© 2002-2026 hogaria.net", geen vennootschap genoemd. Directe links naar "pisos en venta Javea" (/venta-piso/alicante/javea-xabia.aspx) en een rubriek "Publica tu anuncio gratis" plus "Para profesionales".
- Aantallen niet getoond op de homepage; leesroute niet vermeld.
- Beoordeling: **laag/onbekend**. Klein, oud portaal; interessant alleen omdat particulieren er gratis plaatsen.

### 2.8 Trovimap

- Homepage (bewijstype 1): "Encuentra tu casa de alquiler o compra entre más de 1 millón de inmuebles"; "Herramientas para profesionales"; direct plaatsen door particulieren ("Subes los datos del piso, fotos y su descripción. Publicado al instante"). Geen vennootschap, geen API, geen XML op de homepage. Volgens secundaire bronnen (bewijstype 7): opgericht 2016 in Barcelona, kaartgedreven, met waarderingstool en CRM.
- Leesroute: **onbekend/geen**.
- Beoordeling: **middel voor context** (kaart- en waarderingslaag), **niet bewezen voor unieke objecten in de Marina Alta**. Dekking Jávea niet gemeten.

### 2.9 Spain Property Portal

- https://www.spainpropertyportal.com/support/estate-agents.html (bewijstype 1): "We have setup Spain Property Portal to be able to import Kyero valid XML feeds and also we have created our unique XML Valid feed"; met eigen validator. Populaire zoekgebieden die genoemd worden zijn Torrevieja, Orihuela Costa, Estepona en Marbella — **Jávea niet**.
- Leesroute: **geen**; export naar derden niet genoemd.
- Beoordeling: **laag** (Costa Blanca-Zuid en Costa del Sol, niet ons gebied).

### 2.10 Luxe-portalen

- **JamesEdition**: https://www.jamesedition.com/real_estate/javea-spain gaf **HTTP 403** (bewijstype 3). Dekking en route onbekend.
- **LuxuryEstate.com**: hoort tot Immobiliare.it (indomio.com noemt het als groepsmerk), en die groep staat al in het register bij Indomio/pisos.com (R2-16, R2-12). Geen nieuwe partij, geen leesroute.

### 2.11 Aggregators

- **Nestoria (ES) is opgeheven.** `https://api.nestoria.es/api?...` faalt op een zelfondertekend certificaat; `https://www.nestoria.es/` geeft **HTTP 401 "Access Denied"** (bewijstype 3, beide 16-09-2026). De ooit vrij bruikbare Nestoria-API — jarenlang de enige legale gratis leesroute op Spaans portaalaanbod — bestaat voor Spanje niet meer.
- **Trovit, Mitula, Nuroa** (Lifull Connect) nemen feeds ván portalen en makelaars en sturen verkeer terug; zij bieden geen leesroute. FeedCruncher noemt Trovit en Mitula als "free-to-list portals" (bewijstype 1).
- Beoordeling: **nee** — geen unieke objecten, geen route.

### 2.12 Direct-van-eigenaar (FSBO)

- **Spanish Property Insight**: https://www.spanishpropertyinsight.com/property-for-sale-in-spain/direct-from-owner-fsbo meldt "We're currently redeveloping our selection of properties for sale in Spain direct from owners" en kondigt een nieuwe AI-ondersteunde verkoopdienst aan (bewijstype 1). Nu dus **geen aanbod**; wel de moeite om over een kwartaal terug te kijken.
- Verder is het FSBO-kanaal in Spanje verspreid over partijen die we al hebben (Idealista-particulieren, Milanuncios, Wallapop, Fotocasa) plus de twee nieuwe hierboven (tucasa, hogaria).
- **spanishestate.com** ("properties directly from owners and estate agents") weigerde de verbinding (§10).

### 2.13 Overzicht Deel A

| Portaal | Dekking Jávea (16-09-2026) | Leesroute | Unieke objecten | Prioriteit |
|---|---|---|---|---|
| Rightmove Overseas | 489 objecten (type 3) | portaal handmatig | deels | hoog |
| Immowelt (DE) | 643 huizen (type 3) | portaal handmatig | deels | hoog |
| Zoopla Overseas / PrimeLocation | 2.096 huizen prov. Alicante (type 3) | portaal handmatig | deels | middel |
| huisenaanbod.nl | 233 woningen (type 3) | portaal handmatig | deels | middel |
| tucasa.com | 148 (type 7, [te verifiëren]) | portaal handmatig | deels (particulier + bank) | middel |
| Trovimap | onbekend | onbekend | onbekend | middel (context) |
| A Place in the Sun | onbekend | portaal handmatig | nee/deels | laag |
| hogaria.net | onbekend | portaal handmatig | onbekend | laag |
| Spain Property Portal | niet genoemd | onbekend | nee | laag |
| JamesEdition | onbekend (403) | onbekend | onbekend | laag |
| Nestoria ES | — | **weg** | nee | — |
| Trovit/Mitula/Nuroa | n.v.t. | alleen publiceren | nee | laag |

---

## 3. Deel B — Feedstandaarden: wat moet onze importer kunnen lezen?

### 3.1 Kyero v3 — en v4 bestaat niet

R03 documenteerde v3 al volledig. Nieuw vastgesteld op 16-09-2026 (bewijstype 3):

| Bestand | Status |
|---|---|
| `https://feeds.kyero.com/assets/kyero_v3_import_spec.txt` | HTTP 200 |
| `https://feeds.kyero.com/assets/kyero_v4_import_spec.txt` | **HTTP 404** |
| `https://feeds.kyero.com/assets/kyeroV4.0.xsd` | **HTTP 404** |
| `https://feeds.kyero.com/validator/` | HTTP 200 (kent alleen V2.0, V2.1, V3.0 — R03) |

Conclusie: er is **geen Kyero v4**. Wie "v4" zegt, bedoelt een eigen uitbreiding. De helppagina
zegt verder alleen: "Your programmer will need this document to be able to build an EXPORT from
your system that can be used to IMPORT to Kyero.com" (bewijstype 1) — de lijst met compatibele
CRM's staat achter https://www.kyero.com/en/join/features/integrations, dat wij niet konden lezen.

### 3.2 Inmovilla / apinmo — de belangrijkste gemiste route (bekende partij, nieuwe weg)

Inmovilla stond al als CRM in het register (R2-29). Nieuw is dat de **specificatie én een werkende
voorbeeldfeed openbaar zijn** en dat het formaat velden bevat die Kyero v3 mist.

- `https://procesos.apinmo.com/api/v1/apidoc/` → HTTP 200, "Documentación API REST v1", auteur Inmovilla (bewijstype 3).
- `https://procesos.apinmo.com/xml/xml2demo/2-web.xml` → HTTP 200, `application/xml`, 5,46 MB, **1.546 `<propiedad>`-elementen, 159 verschillende tags** (bewijstype 3, zelf geteld).
- Kernvelden (bewijstype 3): `id`, `ref`, `numagencia`, `accion`, `tipo_ofer`, `precioinmo`, `precioalq`, `ciudad`, `zona`, `cp`, `latitud`, `altitud`, `m_cons`, `m_parcela`, `m_uties`, `habitaciones`, `banyos`, `conservacion`, `antiguedad`, `energialetra`/`energiavalor`/`emisionesletra`, **`rcatastral`**, `descrip1`/`descrip2`, `titulo1`/`titulo2`, `numfotos`, `foto1`…`foto36`, `panoramica1`…, `videos`, plus ±90 ja/nee-kenmerken (piscina_prop, piscina_com, vistasalmar, primera_line, trastero, garajedoble …).
- Gemeten op de demo (bewijstype 3/5): `rcatastral` gevuld bij **574 van 1.546** objecten (37%); `latitud` bij 1.546 van 1.546; `accion` = Vender 1.185, Alquilar 301, Vender o Alquilar 58; `conservacion` met waarden als "Para reformar" (151), "Reformar Parcialmente" (186), "Obra Nueva" (202), "Reformado" (207). *Let op: dit is testdata (Madrid-coördinaten, onzin-teksten) — de percentages zeggen iets over wélke velden het formaat aanbiedt, niet over de echte vulgraad bij een kantoor in Jávea.*
- Foto's via vaste URL-opbouw (`https://fotos15.apinmo.com/<numagencia>/<cod_ofer>/<fotoletra>-<n>.jpg`).
- **Semantiek:** volgens Inmovilla's eigen support (bewijstype 1, [te verifiëren] aan de brontekst) bevat de XML elke nacht de volledige catalogus van alleen de objecten met "Publicar web" + "Disponible"; een verkocht of gedepubliceerd object **verdwijnt zonder meer**. In de demofeed komt geen enkel datum- of statusveld voor behalve `fecha_caducidad` (vervaldatum energiecertificaat) — dus **geen `last modified`, geen status** (bewijstype 3).
- **Betekenis voor ons:** dezelfde momentopname-logica als Kyero (verdwijnen = NIET MEER GEVONDEN, nooit "verkocht"), maar met twee velden die Kyero v3 niet heeft en die voor Deal Hunter kerninformatie zijn: **kadastrale referentie** (perceelkoppeling) en **staat van onderhoud** (renovatiesignaal). Contact voor techniek: webs@inmovilla.com (bewijstype 1).

### 3.3 Resales-Online — openbaar ontwikkelaarsportaal (bekende partij, nieuwe weg)

De open vraag in registerregel R2-24 ("artikel Static XML feed for shared properties") is hiermee beantwoord.

- **devdocs.resales-online.com is openbaar** en bevat de secties: *Export XML Feeds*, *Resales-Online Property Imports* (XML-specificatie v1.5), *API to create WebAPI Keys*, *WebAPI* (versie 6), *New Development updates API* (bewijstype 1/3).
- **Exportfeeds** (bewijstype 1): `OwnProperties` ("your own listings"), `ReSales` ("all shared sale listings"), `Rentals`, plus portaalspecifieke uitvoer `KYERO@`, `SPAINHOUSES@`, `FOTOCASA@`, `THINKSPAIN@`, en `PROPERTYBACKUP@`/`CLIENTBACKUP@`/`NEWDEVS@`. Dus: **een partnerkantoor op Resales kan ons met één handeling een Kyero-conforme feed van zijn eigen objecten geven.**
- **Rechtenzin op diezelfde pagina** (bewijstype 1): *"Note that it is prohibited to send other agent's listings to your property portal account."*
- **Static Network feed** (https://support.resales-online.com/en/articles/9773072-…, bewijstype 1): een niet-incrementele XML met de gedeelde objecten van het hele netwerk, "Properties will be updated over night (every 24 hours)", met optie "Send Property Type as Kyero's Type", aan te vragen bij support en vastgezet op één IP-adres. Beslissende beperking, letterlijk: **"can only be used for your own website. It cannot be used with portals or other third-party sites."**
- **Importspecificatie**: V1.4 is *deprecated*; actueel is **V1.5** op https://devdocs.resales-online.com/index.php/docs/property-import-xml-definition-1-5/ met onderdelen *Header*, *Property Details*, *Basic flow of import system* → *Property Updates* en **/off-market/**. Het importproces draait "once a day, every day" en "compares the XML data against the data received in the previous day" (bewijstype 1) — dit formaat kent dus wél een expliciete **off-market/verkocht-toestand**, iets wat Kyero v3 mist.
- **Beoordeling:** de netwerkfeed is voor ons **niet bruikbaar zonder schriftelijke afwijking** (eigen website only). De `OwnProperties`- en `KYERO@`-feed van een partner is dat wél. Prioriteit hoog, maar als *partnerroute*, niet als portaalroute.

### 3.4 SpainHouses en thinkSPAIN

Al in R03 gedocumenteerd (SpainHouses: eigen XSD `cartera.xsd`, verwijderen door weglaten van de
referentie — dezelfde snapshotlogica). Nieuw is alleen dat Resales en de tussenpartijen kant-en-klare
`SPAINHOUSES@`- en `THINKSPAIN@`-uitvoer hebben; dat maakt die formaten kandidaat-invoer als een
partner ze toevallig al genereert.

### 3.5 Fotocasa / Inmofactory en Idealista

- **Inmofactory is opgegaan in Fotocasa Pro**: `https://profesionales.inmofactory.com/` geeft **301 → https://pro.fotocasa.es/campanas/inmofactory/** (bewijstype 3). Die pagina (bewijstype 1) beschrijft "Publicación simultánea en los principales portales inmobiliarios" naar Fotocasa, Habitaclia en Milanuncios; exploitant Fotocasa Group SLU. **Alleen publiceren**, geen leesroute. Dit is dus geen nieuwe partij maar een naamswijziging binnen R2-07/R2-09.
- **Fotocasa-XML**: geen openbare specificatie gevonden; leveranciers verwijzen naar "vraag het bij het portaal op" (bewijstype 7). Generieke voorbeelden noemen een root `<ads>` met `<ad>`-elementen, `agency_cod`, datum in `d/m/Y` en een vlag professioneel/particulier — dat is een *voorbeeld* van een CRM-leverancier, niet de officiële Fotocasa-spec. Niet bruikbaar als bron.
- **Idealista**: massale invoer loopt sinds eind 2018 via **JSON** in idealista/tools, niet meer via XML (bewijstype 7, secundaire bron 1001portales; [te verifiëren]). Publiceerkanaal, geen leesroute; de leeskant staat al in het register (R2-02 t/m R2-06).

### 3.6 Rightmove en Zoopla

- **Rightmove Real Time Data Feed (RTDF)**: openbare specificatie als PDF, https://media.rightmove.co.uk/ps/pdf/guides/adf/Rightmove_Real_Time_Datafeed_Specification.pdf (v1.4.1) en overzichtspagina https://www.rightmove.co.uk/adf.html. HTTPS-webservice met JSON-aanroepen; voor buitenlandse objecten bestaat een aparte aanroep **`OverseasSendProperty`**, alleen beschikbaar voor "Overseas branches"; het oude ADF v3/3a is op 06-01-2016 uitgezet (bewijstype 1/7 — uit de documentbeschrijving, PDF zelf niet geopend).
- **Zoopla**: geen openbare feedspecificatie of leesbare API gevonden; alles wat zich "Zoopla API" noemt is een scraper. Niet gebruiken.
- Beide zijn **publiceerformaten**. Ze horen niet in onze importer, tenzij een Britse partner ons ooit een RTDF-uitdraai aanbiedt — onwaarschijnlijk.

### 3.7 OpenImmo (DACH) — relevant zodra een Duitstalige partner meedoet

- Officiële download: http://www.openimmo.de/go.php/p/24/download.htm — **versie 1.2.7d, stand juni 2026**, XML Schema met ruim 300 attributen (bewijstype 1).
- Licentie, letterlijk (bewijstype 1): *"Der Lizenznehmer erhält das Recht auf Basis dieser Beschreibung eigene OpenImmo Datensätze zu erstellen oder einzulesen."* Gratis en onbeperkt gebruik van de beschrijving; het schema zelf mag niet worden doorverspreid, niet worden gewijzigd of uitgebreid en niet worden vertaald.
- OpenImmo is de de-facto standaard voor gegevensuitwisseling in Duitsland, Oostenrijk en Zwitserland en staat ook in de importlijst van huisenaanbod.nl (bewijstype 1). Dat Immowelt/Immonet erop draaien is aannemelijk maar door ons niet bij die portalen zelf nagelezen (bewijstype 4, [te verifiëren]).

### 3.8 "Real Estate Standard Feed" — bestaat niet als Europese standaard

- Wat er in Spanje over standaardisatie is geschreven, komt uit op het Amerikaanse **RESO** (Real Estate Standards Organization) en de RETS-syndicatieformaten; Inmoblog (24-10-2016, bewijstype 1) beschrijft RESO als "een woordenboek van meer dan 1.000 velden" en stelt vast dat standaardisatie in Spanje strandt omdat "geen enkel vastgoedprogramma meer dan 10% van de markt beheerst". Advies daar: kleine stappen met bestaande formaten.
- **The International MLS** (theimls.com, Delray Beach, Florida) presenteert wel een "International Spec" en zegt: "The IMLS takes feeds that match the RESO spec used by USA MLSs", naast Zillow-, "Kyero Spec"-, xml2u- en KV Core-formaten (bewijstype 1). Amerikaans, publiceergericht, geen aangetoonde dekking in de Marina Alta → **niet interessant**.
- Conclusie: in ons werkgebied zijn de feitelijke standaarden **Kyero v3** (internationaal aanbod in Spanje), **Inmovilla/apinmo** (Spaans CRM-landschap), **Resales v1.5** (MLS-netwerken aan de kust), **OpenImmo** (DACH) en **RTDF** (VK). Meer is er niet.

### 3.9 Formatenoverzicht

| Formaat | Specificatie openbaar? | Lezen of publiceren | Status/verkocht-veld | Kadastrale ref. | Relevantie voor ons |
|---|---|---|---|---|---|
| Kyero v3 (3.8/3.9) | ja (feeds.kyero.com) | beide | nee (snapshot) | ja, `catastral` (optioneel) | **in gebruik** |
| Kyero v4 | bestaat niet (404) | — | — | — | n.v.t. |
| Inmovilla/apinmo `2-web.xml` | ja (apidoc + demo-XML) | lezen via partner | nee (verdwijnt) | **ja, `rcatastral`** | **hoog** |
| Resales-Online v1.5 (import) | ja (devdocs) | beide | **ja (off-market)** | onbekend | hoog (partner) |
| Resales export `OwnProperties`/`KYERO@` | ja (devdocs) | lezen via partner | zie boven | via Kyero-veld | hoog (partner) |
| Resales "Static Network feed" | ja (support) | lezen, **maar alleen eigen website** | onbekend | onbekend | geblokkeerd door voorwaarden |
| SpainHouses `cartera.xsd` | ja (R03) | publiceren | nee (weglaten) | nee | laag |
| OpenImmo 1.2.7d | ja (openimmo.de, licentie vrij) | beide | ja (eigen velden) | nee (DE-context) | middel (DACH-partner) |
| Rightmove RTDF v1.4.1 | ja (PDF) | publiceren | ja (send/remove) | nee | laag |
| Zoopla | nee | publiceren | onbekend | nee | laag |
| Fotocasa-XML | nee (op aanvraag) | publiceren | onbekend | onbekend | laag |
| Idealista (JSON) | nee (achter tools-account) | publiceren | n.v.t. | onbekend | laag |
| RESO / RETS | ja (VS) | beide | ja | n.v.t. | niet in ons gebied |

---

## 4. Deel C — Tussenpartijen die feeds bouwen en rondsturen

Deze partijen leveren zelf geen aanbod, maar ze zijn de praktische sleutel tot partnerfeeds: wie al
bij zo'n dienst zit, kan ons met een paar klikken een bestand geven.

| Partij | Wie/waar | Wat | Kosten (eigen opgave) | Bewijs |
|---|---|---|---|---|
| **UltraIT — XML4U** (ultrait.net/xml4u) | Spanje +34 966 260 870 (Alicante) en VK | Zet objecten om naar feeds voor Rightmove, Zoopla, Kyero, Think Spain, A Place in the Sun, Idealista, Fotocasa, Habitaclia, **Immowelt, Immonet** e.a. | 35 €/mnd (75 € setup) handmatig; 55 €/mnd (275 € setup) met nachtelijke herimport | 1 |
| **Property Portal Marketing** (propertyportalmarketing.com) | VK, Bath (+44 1225 941 018) | Bouwt en onderhoudt feeds voor Spaanse kantoren; "Most major ones will accept the Kyero V3 format"; "Rightmove and Zoopla … accepting the Real-Time Data Feed" | 50 € setup + 25 €/mnd, tot drie feeds, minimaal zes maanden | 1 |
| **FeedCruncher** (feedcruncher.com, Casafari) | verwijst naar casafaricrm.com | Export naar ±40 portalen (abonnement: o.a. Rightmove, Kyero, Idealista, Juwai; gratis: Trovit, Mitula, BPI) | niet gepubliceerd | 1 |
| **Mediaelx** (Costa Blanca) | al in register (R2-26) | Webs, CRM en export naar Fotocasa, Idealista, Kyero, A Place in the Sun | — | 1 |
| **Inmoweb, Inmoenter, Novoportal, XML2U, Mydatafeed, Apimo, eGO, onOffice, Hektor** | divers | De feedfamilies die huisenaanbod.nl noemt; geen openbare specificaties gevonden voor Apimo en eGO | — | 1/7 |

**De route die hieruit volgt (bewijstype 4):** al deze diensten zien een ontvanger als "een portaal".
Een partnerkantoor kan Deal Hunter dus als extra bestemming opgeven, precies zoals het Kyero of
thinkSPAIN opgeeft — mits wij een vaste ontvangst-URL of een ophaaladres aanbieden en de afspraak
op papier staat. Dat is dezelfde constructie als bij Background Properties, maar dan zonder dat de
partner iets hoeft te bouwen.

---

## 5. Gebruiksrechten: de bepalende zinnen

| Bron | Bepalende zin (letterlijk) | Gevolg |
|---|---|---|
| Resales-Online, Static Network feed | "can only be used for your own website. It cannot be used with portals or other third-party sites." | Netwerkaanbod **niet** in onze database zonder schriftelijke afwijking |
| Resales-Online, Export XML Feeds | "Note that it is prohibited to send other agent's listings to your property portal account." | Bevestigt: partner mag alleen zijn **eigen** objecten doorgeven |
| OpenImmo | "Der Lizenznehmer erhält das Recht auf Basis dieser Beschreibung eigene OpenImmo Datensätze zu erstellen oder einzulesen." | Lezen/schrijven van het formaat is vrij; schema niet doorverspreiden of wijzigen |
| Kyero (voorwaarden, R03) | verbod op "any type of robot, spider, scraper … without express written consent" | Portaal alleen handmatig; feed alleen via de eigenaar van het aanbod |
| Zoopla/Rightmove | geen openbare leeslicentie; alle "API's" van derden zijn scrapers | Alleen handmatig raadplegen |
| Spain Property Portal | "We have setup Spain Property Portal to be able to import Kyero valid XML feeds…" | Alleen publiceren |

Voor élke nieuwe partnerfeed blijft de afspraak uit R04/R16 staan: doel (acquisitieanalyse),
AI-verwerking toegestaan, bewaartermijn, geen herpublicatie, beeldvergelijking alleen intern.

---

## 6. Advies: welke formaten ondersteunen we naast Kyero v3?

**Bouw dit, in deze volgorde.**

1. **Inmovilla/apinmo-XML (`<propiedades><propiedad>`) — doen.**
   Reden: het is het meest gebruikte CRM-formaat in het Spaanse makelaarslandschap, de specificatie
   en een voorbeeldbestand zijn openbaar, en het levert twee velden die Kyero v3 niet heeft:
   `rcatastral` (directe perceelkoppeling) en `conservacion` (staat/renovatiesignaal).
   Werk: nieuwe adapter naast `dh/adapters/bp.py` (~120–150 regels), veldafbeelding naar ons
   objectmodel, waardelijsten voor `tipo_ofer` en `conservacion`, foto-URL-opbouw, en dezelfde
   leegte-beveiliging als bij BP (lege of gekrompen momentopname = BRON NIET BEREIKBAAR).
   **Raming: één dagdeel bouwen, één dagdeel testen met een echt partnerbestand.**

2. **Resales-Online v1.5 / `OwnProperties`-export — doen zodra er één partner op Resales zit.**
   Reden: het enige formaat in ons gebied met een expliciete **off-market/verkocht**-toestand; dat
   is voor prijs- en doorlooptijdanalyse veel waard. De `KYERO@`-variant kunnen we vandaag al lezen
   met de bestaande Kyero-parser — begin daarmee, en bouw de eigen v1.5-vorm pas als een partner
   die levert. **Raming: nul extra werk voor `KYERO@`; één dagdeel voor v1.5 inclusief statusveld.**

3. **Generieke CSV/Excel-val — doen.**
   Een deel van de kleine kantoren stuurt geen XML maar een uitdraai. Eén kolomafbeelding-bestand
   per partner is goedkoper dan een adapter. **Raming: één dagdeel, eenmalig.**

4. **OpenImmo 1.2.7d — pas bij vraag.**
   Alleen als een Duitstalig kantoor (Immowelt-segment) partner wordt. Het schema is groot
   (300+ attributen) en we hebben er maar dertig van nodig. **Raming: twee dagdelen, uitgesteld.**

**Niet bouwen:** Rightmove RTDF, Zoopla, Fotocasa-XML, Idealista-JSON, SpainHouses en de
IMLS/RESO-specificaties. Dat zijn publiceerkanalen; wij zouden er data in stoppen, niet uit halen.

**Wel doen buiten de importer om (geen bouwwerk):**
- Rightmove Overseas, Immowelt en Zoopla Overseas opnemen als **handmatige wekelijkse ronde** voor ontdekking van kantoren en objecten die niet in de feeds zitten — en van elk nieuw kantoor de vraag stellen of ze ons hun eigen feed willen geven.
- Bij bestaande en nieuwe partners standaard vragen: *"Op welk systeem draait u — Inmovilla, Resales, Inmoweb, iets anders?"* Dat ene antwoord bepaalt of aansluiting een uur of een dag kost.

---

## 7. Voorstel voor nieuwe registerregels

| Voorstel-id | Naam | Type | Toegang | Uniek | Status |
|---|---|---|---|---|---|
| B05-01 | Rightmove Overseas | portaal VK | portaal handmatig | deels | GEEN LEESROUTE — handmatig |
| B05-02 | Immowelt / Immonet | portaal DE | portaal handmatig | deels | GEEN LEESROUTE — handmatig |
| B05-03 | Zoopla Overseas / PrimeLocation | portaal VK | portaal handmatig | deels | GEEN LEESROUTE — handmatig |
| B05-04 | huisenaanbod.nl | portaal NL | portaal handmatig | deels | GEEN LEESROUTE — handmatig |
| B05-05 | tucasa.com (Iberanuncios S.L.) | portaal ES | portaal handmatig | deels | TECHNISCH ONDERZOEK NODIG (site gaf 500) |
| B05-06 | hogaria.net | portaal ES | portaal handmatig | onbekend | LAAG |
| B05-07 | Trovimap | portaal + waardering ES | onbekend | onbekend | TECHNISCH ONDERZOEK NODIG |
| B05-08 | A Place in the Sun | portaal VK | portaal handmatig | nee/deels | LAAG |
| B05-09 | Inmovilla/apinmo-XML (formaat + openbare doc) | feedstandaard | partnerfeed | n.v.t. | BOUWEN (advies 1) |
| B05-10 | Resales-Online devdocs, exportfeeds en Static Network feed | feedstandaard + route | partnerfeed / lidmaatschap | n.v.t. | **aanvulling op R2-24** |
| B05-11 | OpenImmo 1.2.7d | feedstandaard | partnerfeed | n.v.t. | UITGESTELD |
| B05-12 | Rightmove RTDF v1.4.1 | feedstandaard | alleen publiceren | nee | NIET GEBRUIKEN |
| B05-13 | UltraIT XML4U / Property Portal Marketing / FeedCruncher | tussenpartijen | partnerroute | n.v.t. | CONTACT VIA PARTNER |

Aanvullingen op bestaande regels: **R2-07/R2-09** (Inmofactory = Fotocasa Pro), **R2-16** (miparcela.com
leidt door naar indomio.es/venta-terrenos; LuxuryEstate hoort bij dezelfde groep), **R2-24** (openbare
devdocs + Static Network feed + v1.5-importspec; open vraag gesloten), **R2-29** (openbare apinmo-doc
en demo-XML), **R2-10** (geen v4).

---

## 8. Open vragen

1. Hoeveel van de 489 Rightmove- en 643 Immowelt-objecten zitten al in de Kyero-feed van Background Properties? Niet gemeten; bepaalt of handmatige rondes de moeite waard blijven.
2. Tucasa: hertellen zodra de site weer werkt, en vaststellen hoe groot het particuliere en bancaire deel werkelijk is.
3. Inmovilla: bevestiging bij webs@inmovilla.com dat de nachtelijke XML inderdaad geen wijzigingsdatum en geen statusveld kent, en of `rcatastral` bij Jávea-kantoren in de praktijk gevuld is.
4. Resales-Online: is er een schriftelijke afwijking mogelijk voor intern analytisch gebruik van de Static Network feed? Zo niet, dan blijft alleen de partner-eigen feed over.
5. Immowelt/Immonet: draait de invoer echt op OpenImmo, en staan er Jávea-kantoren tussen die nergens anders publiceren?
6. Trovimap: waar komt die "1 millón de inmuebles" vandaan, en is er dekking in de Marina Alta?
7. Spanish Property Insight: wanneer komt de FSBO-sectie terug en met welke voorwaarden?

---

## 9. Geblokkeerd of mislukt (niet omzeild)

| Site | Waarneming 16-09-2026 |
|---|---|
| jamesedition.com (Jávea-pagina) | HTTP 403 |
| tucasa.com (Jávea-zoekpagina) | HTTP 502 via WebFetch, HTTP 500 via curl — serverfout, geen blokkade |
| spanishestate.com | verbinding geweigerd (ECONNREFUSED 94.46.221.11:443) |
| nestoria.es | HTTP 401 "Access Denied"; api.nestoria.es zelfondertekend certificaat → dienst opgeheven |
| rightmove.co.uk/overseas-property/in-Javea.html | alleen navigatie, geen objecten (wel volledig op /overseas-property-for-sale/Javea.html) |
| kyero.com/en/join/features/integrations | niet gelezen (Kyero blokkeert ophalen, zie R03) |
| resales-online.com (hoofdsite) | onveranderd 403 (R04); support- en devdocs-subdomeinen wel open |

---

## 10. Bronnenlijst (URL · bewijstype)

Alle gecontroleerd op 16-09-2026.

1. https://www.rightmove.co.uk/overseas-property-for-sale/Javea.html — 3
2. https://www.rightmove.co.uk/adf.html — 1
3. https://media.rightmove.co.uk/ps/pdf/guides/adf/Rightmove_Real_Time_Datafeed_Specification.pdf — 1/7 (niet geopend)
4. https://www.zoopla.co.uk/overseas/houses/spain/valencia/alicante/ — 3
5. https://www.aplaceinthesun.com/advertise/website/list-your-properties — 1
6. https://www.immowelt.de/suche/ausland/kaufen/haus/valencianische-gemeinschaft/xabia-javea/ad08es2329 — 3
7. https://www.huisenaanbod.nl/nl/Huizen-te-koop-in-Javea-Xabia-Costa-Blanca-Valencia-Spanje/ — 3
8. https://www.huisenaanbod.nl/nl/buitenlandse-woningen-aanbieden-voor-makelaars/ — 1
9. https://www.costaselect.com/nl/huizen-te-koop-in-spanje?city[]=Javea — 1
10. https://www.tucasa.com/ — 1 · https://www.tucasa.com/compra-venta/viviendas/alicante/javea-xabia/ — 3 (fout) / 7 (telling uit zoekresultaat)
11. https://www.hogaria.net/ — 3
12. https://www.trovimap.com/ — 1
13. https://www.spainpropertyportal.com/support/estate-agents.html — 1
14. https://www.jamesedition.com/real_estate/javea-spain — 3 (403)
15. https://api.nestoria.es/… en https://www.nestoria.es/ — 3 (dood)
16. https://www.miparcela.com/ → 301 https://www.indomio.es/venta-terrenos/ — 3
17. https://profesionales.inmofactory.com/ → 301 https://pro.fotocasa.es/campanas/inmofactory/ — 3 · inhoud 1
18. https://feeds.kyero.com/assets/kyero_v3_import_spec.txt (200), …/kyero_v4_import_spec.txt (404), …/kyeroV4.0.xsd (404), https://feeds.kyero.com/validator/ (200) — 3
19. https://help.kyero.com/estate-agents/compatible-property-management-systems — 1
20. https://procesos.apinmo.com/api/v1/apidoc/ — 3
21. https://procesos.apinmo.com/xml/xml2demo/2-web.xml — 3 (1.546 objecten, 159 tags, eigen telling)
22. https://soporte.inmovilla.com/support/solutions/articles/103000130917-información-importación-xml — 1/7
23. https://devdocs.resales-online.com/ — 1/3
24. https://devdocs.resales-online.com/index.php/docs/export-xml-feeds/ — 1
25. https://devdocs.resales-online.com/index.php/docs/property-import-xml-definition-1-5/ — 1
26. https://support.resales-online.com/en/articles/9773072-new-static-xml-feed-for-shared-properties — 1
27. https://support.resales-online.com/en/articles/4046798-property-import-xml-definition-v1-4 — 1 (verouderd)
28. http://www.openimmo.de/go.php/p/24/download.htm — 1
29. https://www.ultrait.net/xml4u — 1
30. https://www.morairaonline24.com/info/guide-to-xml-feed-building-and-maintenance-information-from-property-portal-marketing — 1
31. https://www.propertyportalmarketing.com/blog/xml-feeds-what-are-they.html — 1
32. https://www.feedcruncher.com/ — 1
33. https://theimls.com/MLS/xmlspec/ — 1
34. https://www.inmoblog.com/camino-estandar-intercambio-informacion/ (24-10-2016) — 1
35. https://mediaelx.net/noticias/172/importacion-xml-en-paginas-webs-inmobiliarias/ — 1
36. https://www.spanishpropertyinsight.com/property-for-sale-in-spain/direct-from-owner-fsbo — 1

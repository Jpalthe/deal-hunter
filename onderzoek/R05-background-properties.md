# R05 — Background Properties: netwerk, Kyero-feed, rechten, actualiteit en importcontroles

> **NA TEGENSPRAAK (15-09-2026).** Dit rapport is door een tweede agent gecontroleerd; zie `R05-background-properties.verificatie.md`. Betrouwbaarheid volgens die controle: hoog: 16 van 18 kernclaims zijn bij verse controle bevestigd; de 2 weerleggingen betreffen alleen een getal (41 kantoren in plaats van 45, 4 ingetrokken objecten in plaats van 5), niet de strekking.
> Weerlegd en in de eindstukken gecorrigeerd: R05-03; R05-12. Gebruik voor die punten de gecorrigeerde tekst in het verificatiebestand, niet de tekst hieronder.


**Project:** TREE Deal Hunter, fase A · **Stroom:** R05 · **Controledatum:** 14-09-2026 (avond, 22:40–23:10 CEST)
**Masterprompt-secties:** 8 (BP-feedprioriteit), 10 (actualiteit), 11 (objectidentiteit), 12 (gegevens per object)
**Bewijstypen** (sectie 5): 1 = door aanbieder vermeld · 2 = in officiële bron aangetroffen · 3 = door ons rechtstreeks vastgesteld · 4 = AI-inferentie · 5 = berekening op benoemde aannames · 6 = door bevoegde professional bevestigd · 7 = onbekend of tegenstrijdig

## Samenvatting

1. Background Properties (BP) is geen makelaar en geen aggregator van de markt, maar een **listingdienst** in Jávea: een eenmanszaak (handelsnaam Background Properties, sinds 2017) die woningen van eigenaren in beheer neemt en ze laat verkopen door een netwerk van **45 partnermakelaars** in Spanje, België en Duitsland. TREE Properties staat op 14-09-2026 niet in die openbare partnerlijst.
2. De feed is een **WordPress-export (Houzez-thema, WP All Export)** in Kyero-v3-opmaak: zes exportbestanden achter een geheime sleutel. Wij halen ze elk uur (properties-api) en elke twee uur (site-import) op; BP genereert ze **één keer per nacht** (alle zes tussen 01:34 en 02:55 CEST gemeten). Vaker ophalen dan één keer per dag levert dus niets op.
3. De feed is een **volledige momentopname zonder status, verwijderingsmelding, prijshistorie, bouwjaar, staat, kadastrale referentie of makelaarsreferentie**. Verdwijnen betekent "niet meer gevonden", nooit "verkocht".
4. Correctie op een eerder lokaal feit: de feed levert **wél** een `pool`-element, maar als vrije tekst in drie talen ("Private", "Privé", "Nee", "Gemeenschappelijk" …), niet als 0/1 zoals de Kyero-specificatie eist. Verder wijkt BP af bij `energy_rating` ("Processing", "In aanvraag"), `url` (alleen Engels), postcode (30 % gevuld) en coördinaten (**11 objecten staan op een punt in Miami**, waaronder twee in Jávea).
5. Aanbod op 14-09-2026 23:00: **225 objecten, 57 in Jávea** (26 villa's, 24 percelen, 5 appartementen, 2 zonder type), 27 vanaf € 750.000. Verloop sinds 25-08: circa 6 nieuwe en 5 verdwenen objecten in drie weken — een dunne stroom.
6. **Overlap met Idealista: 6 van 6 geteste Jávea-objecten staan er ook**, meestal meerdere keren (1 tot 10 advertenties per object, via verschillende partnermakelaars, met vertaalde BP-teksten). BP is voor Jávea dus geen unieke bron; Idealista toont bovendien prijshistorie die BP niet geeft (bijv. € 1.200.000 → € 990.000).
7. Onze site-import heeft al goede beschermingen (lege feed = niets schrijven, krimpdrempel 30 %, `withdrawn` in plaats van verwijderen, alarm). De **properties-api (poort 3100) heeft die niet**: bij een storing zet hij het aanbod op 0 — precies wat vanavond om 22:12 gebeurde en wat na 10 van de latere herstarts ook gebeurde (DNS nog niet klaar bij het opstarten).
8. **Rechten:** de feed-URL's zijn aan TREE verstrekt voor de website; er is geen schriftelijke afspraak gevonden over opslag, historie, AI-analyse, beeldvergelijking of tonen aan derden. De aviso legal van BP eist voor reproductie "autorización escrita previa" en verbiedt expliciet direct doorlinken naar site-inhoud (relevant voor hotlinken van foto's). Status: **CONTRACT OF TOESTEMMING NODIG** vóór Deal Hunter-gebruik.
9. De concept-mail met acht vragen aan BP staat in sectie 6.4; niet verzonden. ⏸️ ACTIE VOOR JAN: mail beoordelen en versturen, en bevestigen wie bij BP de contactpersoon is.
10. Rol van BP in Deal Hunter: **"ons netwerk"** (schone, gestructureerde data van 225 objecten met commissielabel), niet "de markt". Voor dekking van Jávea is een bredere bron nodig; BP blijft nuttig als eerste, goedkope en gelicentieerde adapter en als testset voor de importketen.

---

## 1. Wie is Background Properties (opdracht a)

### 1.1 Bedrijf en vestiging

| Gegeven | Waarde | Bron | Type |
|---|---|---|---|
| Juridische naam | Filip van Horenbeeck (natuurlijke persoon / eenmanszaak; "Denominación Social") | backgroundproperties.com/aviso-legal/ | 1 |
| Handelsnaam | Background Properties | idem | 1 |
| CIF/NIF | Y4016867T | idem | 1 |
| Adres | Carrer de la Vinya 20, 03730 Jávea (Alicante) | idem, privacybeleid | 1 |
| E-mail / telefoon (zakelijk) | hola@backgroundproperties.com · +34 670 412 191 | idem | 1 |
| Recht en forum | Spaans recht; rechtbanken van Elche | idem | 1 |
| Actief sinds | "family-run business active on the Costa Blanca since 2017" | backgroundproperties.com/en/ | 1 |
| Certificering | "API-certified, professional company" (API = Agente de la Propiedad Inmobiliaria) | idem | 1 — niet zelf gecontroleerd bij het API-college [te verifiëren] |
| Team | vier personen op de site (oprichter, twee "property listers", office manager) | homepage | 1 |

### 1.2 Wat voor netwerk

BP is een **listingdienst tussen eigenaar en makelaars**, geen klassieke makelaardij en geen marktaggregator:

- "We are an API-certified, professional company representing more than 40 leading national and international real estate agents." (type 1)
- Aan eigenaren: "Your property will be added to our database and published by the real estate agencies that we represent." Geen exclusiviteit ("No, we don't ask for exclusivity"), geen extra kosten, "we only charge the common commission in case of a sale through one of our real estate agents". (type 1)
- Aan makelaars: "Our property information is for the exclusive use of our estate agents." Toegang via een aanvraagformulier voor een "tijdelijke toegangscode" (pagina /toegang/ en /en/access/). (type 1)
- De pagina /makelaars/ noemt **45 partnerkantoren** met plaats en land. Circa 20 daarvan zitten in of rond Jávea (o.a. Miralbo, Arzuaga, Prima Villas, Blanca International, Elite Costa Properties, Javea Estates, Moment Estates, Villas-Plots, Crown Properties, Maravilla Costa, Paradise Real Estate, Lucas Fox), de rest in Calpe, Moraira, Altea, Denia, Benissa, Orihuela Costa, Madrid (REMAX España), België (Azull, Kaza Exclusiva, Second Home Spanje, Immofy) en Duitsland (Da Vinci Immobilien). **TREE Properties staat niet in de lijst** (type 3, 14-09-2026). Of dat een achterstand op de site is of een bewuste keuze: ONBEKEND.
- De feed zelf draagt een `<agent>`-blok met de gegevens van BP (naam, e-mail, mobiel, plaats, regio, postcode, land) — BP presenteert zich in de Kyero-feed dus als "de makelaar"; de eigenlijke verkopende partner staat er niet in. (type 3)

### 1.3 Dekking

- Site: "Altea, Benidorm, Benissa, Benitachell, Calpe, Denia, Finestrat, Jávea, Monte Pego, Moraira, Valle de Jalón, Valle de Orba", met de opmerking dat objecten daarbuiten bespreekbaar zijn. (type 1)
- Feed op 14-09-2026 23:00 (lokale API `/api/stats`, type 3): 225 objecten in 26 plaatsen; provincie Alicante 223, Valencia 1 (Oliva), leeg 1. Jávea 57, Benissa 30, Moraira 25, Calpe 23, Denia 18, Benitachell 12, Altea 12, Pedreguer 11, Alcalalí 7; de rest ≤ 3. Prijzen € 58.500 – € 4.500.000. Typen: Villa 149, Land 49, Apartment 18, Town house 4, Commercial property 2, Country house 1, leeg 2.
- Het is dus **Costa Blanca Noord (Marina Alta + een deel van de Marina Baixa)**, geen landelijke dekking en ook geen volledige Marina Alta: van de 57 Jávea-objecten liggen er 24 in de categorie perceel, tegenover 238 percelen die de Idealista-assistent op 14-09-2026 voor Jávea gaf (lokaal feit R00). Ordegrootte: BP dekt in Jávea een tiende van het perceelaanbod op Idealista (type 5, ruwe vergelijking van twee tellingen op dezelfde dag).

### 1.4 Hoe BP feeds levert

- Techniek (type 3, rechtstreeks vastgesteld op 14-09-2026 23:07): de feed-URL `wp-load.php?security_key=…&export_id=N&action=get_data` geeft een **HTTP 302** naar een statisch bestand `/wp-content/uploads/wpallexport/exports/<hash>/current-Houzez-Kyero-<naam>.xml`. Dat is het patroon van de WordPress-plug-in **WP All Export** op een site met het **Houzez**-vastgoedthema. De bestandsnamen: `current-Houzez-Kyero-5-pct.xml` (26), `…-3-en-4-pct.xml` (27), `…-Nieuwbouw-5-pct.xml` (29), `…-Nieuwbouw-3-4-pct.xml` (30), `…-Resale-5-pct.xml` (31), `…-Resale-3-4-pct.xml` (32). Export 36 ("alles") wordt door de site-import gebruikt; naam niet gecontroleerd.
- BP maakt per partner kennelijk exports op maat (de zes van TREE zijn gesplitst op commissie 5 % versus 3–4 % en op nieuwbouw/resale). Of andere partners dezelfde of andere exports krijgen: ONBEKEND.
- Partners publiceren de BP-objecten onder eigen naam: op ikzoekeenhuisinspanje.nl staat object 4676JAV als "BP-4676JAV" met foto's `4676JAV_02.jpg`, zonder vermelding van BP als bron (type 3). Op Idealista staan dezelfde objecten via meerdere partners (sectie 5).
- **Voorwaarden voor de feed publiceert BP niet.** Gevonden: aviso legal, privacybeleid, cookiebeleid. Geen partnerovereenkomst, geen feedvoorwaarden, geen API-documentatie. De link "Terms of Use" onder het contactformulier op een objectpagina verwijst naar de objectpagina zelf (type 3).
- Beveiliging: de site draait een bot-check (CleanTalk); een `curl` zonder browser-User-Agent kreeg op de homepage en op een objectpagina een 403 met een JavaScript-wachtpagina. De feed-URL's zelf worden door onze Node-dienst zonder User-Agent gewoon bediend (type 3). Objectpagina's zijn openbaar (WebFetch kreeg de volledige pagina): referentie, prijs, label "Resale", perceel, type, plaats, wijk, oriëntatie, afstand tot zee, terrein, nutsvoorzieningen; **geen** publicatiedatum, energielabel of kadastrale referentie (type 3).

### 1.5 BP op Kyero en Idealista

- Kyero: via zoeken geen makelaarspagina "Background Properties" gevonden; de pagina "Estate agents in Javea" op kyero.com gaf voor onze fetch een 403 (niet omzeild). Conclusie: **niet vastgesteld** of BP zelf op Kyero adverteert (type 7).
- Idealista: geen pro-pagina gevonden (`/pro/background-properties/` gaf 403; niet omzeild). De Idealista-assistent toont geen makelaarsnaam. Wel vastgesteld: BP-objecten staan op Idealista via partnermakelaars, vaak vijf tot tien keer (sectie 5). Of BP daarnaast zelf adverteert: ONBEKEND.

---

## 2. Wat onze eigen code nu doet (opdracht b)

Alle bevindingen hieronder zijn type 3 (bestanden gelezen op 14-09-2026; geen sleutels overgenomen).

### 2.1 properties-api (`~/tree-hermes/properties-api`, dienst `com.tree.properties-api`, poort 3100)

| Aspect | Bevinding |
|---|---|
| Bron | Zes exports (26, 27, 29, 30, 31, 32) uit `feeds.js`, gelabeld op commissie (5 / 3) en categorie (all / newbuild / resale). |
| Ophalen | Bij start en daarna `cron.schedule("0 * * * *")` — **elk heel uur**. Sequentieel, time-out 30 s, volgt redirects. |
| Parser (xml2js) | `id, ref, date, price, currency, price_freq, type, new_build, town, postcode, province, country, location_detail, location/latitude+longitude, beds, baths, pool, surface_area/built+plot, energy_rating/consumption+emissions, url/{en,es,nl,de,fr}, desc/{en,es,nl,de,fr}, features/feature, images/image`. Interne velden `_feed, _commission, _category` (niet in de API-uitvoer). |
| Dedupe | Op `ref`; bij dubbel wint de feed met de hoogste commissie. 450 feedregels → 225 unieke objecten (26 ∪ 27 = 225; 29+30 = 97 nieuwbouw; 31+32 = 128 resale; sommen kloppen exact). |
| Opslag | Alleen in het geheugen (`Map`). Geen database, geen bestand, geen historie. |
| Importcontroles | **Geen.** `properties = newProperties` vervangt de hele set, ook als alle zes ophaalacties mislukken → 0 objecten. Fouten alleen zichtbaar in `/api/stats.errors`. Geen krimpdrempel, geen `withdrawn`, geen alarm. |
| Dienst | launchd `RunAtLoad`, `KeepAlive true`, logs naar `logs/stdout.log` en `stderr.log` (zonder tijdstempels). |
| API | `/api/health`, `/api/stats`, `/api/filters`, `/api/properties` (filters, zoeken, sortering, paginering max 100), `/api/properties/:ref`. CORS open (`*`) zolang `ALLOWED_ORIGINS` niet is gezet. |

**Wat de logs laten zien** (2.805 ophaalrondes sinds april, type 3):

- Unieke aantallen schommelden tussen **220 en 251** objecten; het meest voorkomend 224 (450 rondes) en 225 (299 rondes). De feed beweegt dus, maar langzaam.
- **184 rondes met 0 objecten** (alle zes `getaddrinfo ENOTFOUND backgroundproperties.com`), in twee lange blokken (ca. 37 en ca. 130 opeenvolgende uurrondes — datum onbekend omdat de log geen tijdstempels heeft) en verder **bij 10 van de 17 latere herstarts van de dienst**: de eerste ronde na het opstarten mislukt omdat DNS nog niet klaar is, en het aanbod staat dan tot het volgende hele uur op 0. Vanavond (22:12) gebeurde exact dat; om 23:00:08 stond het aanbod weer op 225.
- Incidentele fouten van BP-zijde: HTTP 500 (29 keer verdeeld over alle exports), 502 (1), 504 (1), "socket hang up" (3). Elke keer verdwenen de objecten van díe export uit de API tot de volgende ronde (bijv. export 27 → 64 objecten weg).

### 2.2 Site-import treeproperties.es (`~/tree-website/tree-properties/src/lib/import/`)

| Aspect | Bevinding |
|---|---|
| Bron | `BP_FEED_ALL` = export 36 ("alles", bron van alle woningdata); `BP_FEED_COMMISSION_HIGH` = 26 en `…_STANDARD` = 27 leveren alleen refs voor het label `commissionClass` (high / standard / unknown). Sleutels alleen in `.env.local` en Vercel. |
| Parser (fast-xml-parser, `kyero.ts`) | Zelfde velden als hierboven plus `part_ownership, leasehold, notes`; leest `feed_version` uit `root/kyero`; `url` mag string of per taal zijn; `date` wordt als Spaanse tijd (+02:00) naar ISO gezet — let op: in de winter is dat +01:00, dus één uur fout in de winter [te verifiëren, klein]. |
| Mapping (`map.ts`) | Document-id `property-<ref>`; `feedId` = BP-`id`; `feedDate` = `date`; `town` genormaliseerd (El Vergel → El Verger), `townSlug` via werkgebied-aliassen (Xàbia → javea); `pool` = `toBool(pool)` en anders uit de kenmerkenlijst (Pool / piscina / zwembad); `newBuild` standaard `false` als leeg. |
| Verversing | launchd `com.tree.properties-import` **elke 2 uur** (`StartInterval 7200`, `RunAtLoad`) via `scripts/import-periodiek.sh` met lock-map en daglog; daarnaast Vercel-cron `/api/import` **dagelijks 06:00 UTC** (`vercel.json`). README zegt "elke 2 uur via vercel.json" — dat klopt niet met het bestand; feitelijk: lokaal 2-uurlijks, Vercel dagelijks. |
| Controles die er al zijn | (1) HTTP ≠ 200, geen `<property` of lege parse → `FeedError`, niets geschreven. (2) **Krimpdrempel**: minder objecten dan `(1 − IMPORT_MAX_SHRINK_PCT)` × actief in Sanity (standaard 30 %) → afbreken + alarm "kritiek". (3) Objecten buiten het werkgebied (Marina Alta) worden overgeslagen (24 van 225). (4) Objecten die niet meer in de feed staan → `status = withdrawn` (niet verwijderd), `lastImportAt` gezet; `lastSeenAt` per gezien object. (5) Foto's: hergebruik op `sourceUrl`, upload naar Sanity, max 40 per object, time-outs 30/60 s. (6) `treeRef` wordt één keer toegekend en nooit gewijzigd. (7) Alarmkanalen: webhook (Slack/Discord/Telegram/Teams), Resend-mail of GHL-mail. |
| Praktijk 25-08 → 14-09 (daglogs) | 12 runs/dag, elk ca. 9 s; gevonden 224–226; bijgewerkt 199–201; **nieuw: 27-08 (1), 01-09 (1), 02-09 (1), 12-09 (2), 14-09 (1); ingetrokken: 28-08 (1), 02-09 (1), 12-09 (1), 14-09 (1)** (de 42 op 25-08 waren de werkgebiedsverkleining); 0 keer afgebroken op de krimpdrempel; 3 mislukte runs (31-08, 07-09, 14-09 22:11:58 "Feed niet bereikbaar: fetch failed", alarm verstuurd). Commissielabel: 162 high / 63 standard tot 13-09, 161 / 64 vanaf 14-09 — één object wisselde van klasse. |
| Waarschuwingen | Terugkerend: "Geen typecijfer voor onbekend type" (objecten zonder `type`) en "Geen plaatscode voor Beniarbeig". |

### 2.3 Wat ontbreekt voor deal hunting (in feed én in onze code)

| Nodig (masterprompt 8, 10, 12) | In BP-feed | In properties-api | In site-import |
|---|---|---|---|
| Prijshistorie | nee (alleen actuele prijs) | nee | nee (laatste prijs overschrijft) |
| Bouwjaar | nee | — | — |
| Staat / renovatiebehoefte | nee (alleen vrije tekst; 25 van 225 omschrijvingen noemen reform/renovate/opknappen) | — | — |
| Kadastrale referentie | nee (`catastral`-node afwezig; Kyero-spec kent hem) | — | — |
| Aanbiederreferentie (verkopende makelaar) | nee (`agent` = BP zelf) | — | — |
| Verwijderingsmelding / status / verkoopdatum | nee | nee | `withdrawn` afgeleid uit afwezigheid |
| Wijzigingsdatum | `date` (per Kyero: laatste wijziging), betekenis bij BP niet bevestigd | opgeslagen als tekst | `feedDate` |
| Eerste publicatiedatum | nee | nee (`first_seen_at` ontbreekt) | nee (`_createdAt` van Sanity is een benadering) |
| Plattegronden / documenten | nee (`image@id` alleen; geen `floorplan`-tag) | — | — |
| Video / virtuele tour | nee | — | — |
| Oriëntatie, afstand tot zee, terrein | **niet in de feed, wél op de BP-objectpagina** (Houzez-velden) | — | — |
| Bescherming tegen lege of halve feed | n.v.t. | **nee** | ja (drempel 30 %) |
| Nulmeting en wijzigingsdetectie (NIEUW / PRIJS / NIET MEER GEVONDEN) | n.v.t. | nee | deels (`created`, `updated`, `withdrawn` alleen als telling in het rapport, niet als gebeurtenis per object) |

---

## 3. Kyero v3 versus wat BP werkelijk levert (opdracht c)

### 3.1 De officiële specificatie (type 2: help.kyero.com en feeds.kyero.com, gelezen 14-09-2026)

- **Structuur**: `<root><kyero><feed_version>3</feed_version></kyero><agent>…</agent><property>…</property>…</root>` (exportspec). Importspec: "All tags are CaSe SenSiTiVe and MUST be in lower case throughout".
- **Verplicht** (importspec): `id` ("alphanumeric, max 50 characters. Your database or other unique identifier"), `date` ("datetime, 19 characters. Last modified date for this property", formaat `YYYY-MM-DD HH:MM:SS`), `ref` ("Your customer-visible reference", max 255), `price` (max 8 cijfers), `price_freq` (`sale` of `month`; `week` in V3.3 geschrapt), `type` ("converted to Kyero standard property type"), `town`, `province`, `beds`, `baths`, `pool` ("numeric. '1' if available, '0' if unknown"), `desc` (verplicht sinds V3.2).
- **Optioneel**: `currency` (EUR/GBP/USD), `part_ownership`, `leasehold`, `new_build` ("'1' if less than 12 months old"), `country` (default Spain), `location` (latitude/longitude, max 15 tekens), `location_detail` (max 50 tekens: "Village/urbanisation description"), `surface_area` (`built`, `plot`, in m²), `energy_rating` (`consumption`, `emissions`: A–G of X), `url` per taal (13 codes), `video_url`, `virtual_tour_url`, `catastral` ("20 characters. Property cadastral reference"), `features` (max 35 tekens per kenmerk, Spaans of Engels), `notes` (max 255), `images` (max 50, minimaal 1280×960, optionele `floorplan`-tag), `prime`, `email`, `whatsapp_number`, `contact_number`.
- **id versus ref**: `id` is de interne databasesleutel, `ref` de klantzichtbare referentie. Kyero koppelt op `id`; "When we see a change in the `<date>` tag, the property will be UPDATED".
- **Verwijderen / status**: er is **geen status- of verwijderingselement**. "Your property feed must be an absolute feed of all your property information - not an incremental one." Kyero verwijdert "when there is no matching property record in your feed". Ook de exportspec kent geen status.
- **Oppervlaktedefinities**: alleen "built" en "plot" in vierkante meters; geen onderscheid bebouwd/bruto/netto/gebruiksoppervlak. Die definitie moet dus bij de aanbieder worden nagevraagd.
- **Standaardtypen** (help.kyero.com/property-types-used-in-kyero): Apartment (apartment, duplex, penthouse, studio, triplex) · Villa (bungalow, villa) · Town house (terraced house, town house, village house) · Country house (farm, cortijo, country house, farmhouse, finca) · Land (land, ruin) · Cave house · Garage · Commercial property · Wooden home.
- **Versies**: V3 (09-12-2013) t/m V3.8 (03-09-2024, contact/whatsapp-nummers) volgens het tekstbestand; de helppagina noemt dezelfde wijziging V3.9. Kleine inconsistentie in Kyero's eigen documentatie (type 7).
- Context: Kyero zelf verwerkt makelaarsfeeds 's nachts (Prime: vijf nachten per week; gratis account: wekelijks) — dat zegt niets over BP, maar wel over wat "actueel" in dit ecosysteem betekent.

### 3.2 Wat BP werkelijk levert (type 3: één leesverzoek aan export 26 op 14-09-2026 23:07, 161 objecten, 1,98 MB; plus de 225 objecten in de lokale API)

| Element | Kyero-spec | BP-feed | Oordeel |
|---|---|---|---|
| root / kyero / feed_version | verplicht | aanwezig, `3` | conform |
| agent | exportspec | aanwezig: naam, e-mail, mob, plaats, regio, postcode, land van BP | conform; identificeert BP, niet de verkopende makelaar |
| id | verplicht, uniek | 225/225 gevuld en uniek; waarden 164522 – 2086428; de wp-json-pagina-id's van de site liggen in dezelfde reeks → vrijwel zeker het **WordPress-post-id** (type 4) | stabiele sleutel |
| ref | verplicht | 225/225 uniek; patronen `9999JAV`, `C3XY9999JAV`, `C4XY9999CAL`; betekenis van het voorvoegsel `C3XY`/`C4XY` ONBEKEND (hangt mogelijk samen met commissie 3/4 %, niet bevestigd) | bij **39 van 225** wijkt de ref af van het ref-deel in de URL-slug (bijv. ref 4544JAV, slug 4541jav; ref 4594CAL, slug 4594jav; ref C3XY442222BEN, slug c3xy4421bell) → refs worden bewerkt of objecten opnieuw gepubliceerd; `id` is de betere identiteit |
| date | verplicht, laatste wijziging | 225/225, alle uniek, met seconden; bereik 2024-09-11 12:34:25 → 2026-09-12 10:47:44; **35 objecten op 2026-05-14** (bulkbewerking) | formaat conform; betekenis bij BP (aanmaak of wijziging) **niet bevestigd** [te verifiëren] |
| price / currency / price_freq | verplicht | 225/225; EUR; `sale` | conform; geen huur |
| type | verplicht | Villa 149, Land 49, Apartment 18, Town house 4, Commercial property 2, Country house 1, **leeg 2** (4679JAV, C3XY4678JAV; omschrijving zegt townhouse resp. appartement) | 2 objecten buiten spec |
| new_build | optioneel 0/1 | 225/225 (97 × `1`) | conform; "minder dan 12 maanden oud" wordt door BP ook voor projecten in aanbouw gebruikt (type 4) |
| town / province / country | verplicht | town 225; province 224; country 225 | conform; spelling wisselt (Javea, El Vergel/El Verger) |
| postcode | — | **67/225** gevuld | mager |
| location_detail | ≤ 50 tekens | 182/225; urbanisatienamen (Tosalet 5, Ambolo, Cumbre del Sol …) | conform; waardevol als microlocatie |
| location lat/long | optioneel | 188/225 gevuld; **11 daarvan = 25.68654, −80.431345 (Miami)**: 4652BEN, 4554BEN, 4573BEN, 4553CAL, 4432JAV, C4XY4505CAL, 4664ALB, C4XY4683JAV, 9008XAR, 8319MOR, C3XY4638JAV | geocoder-standaardwaarde; **plausibiliteitscontrole verplicht** |
| beds / baths | verplicht | 174/225 (percelen leeg) | acceptabel |
| pool | verplicht, 0/1 | 223/225 gevuld met **tekst**: Private 97, Privé 71, Nee 29, Gemeenschappelijk 10, No 7, Common 3, Communal 3, communal 2, Privat 1 | **niet conform**; onze `toBool` geeft altijd `undefined`, de kenmerkenlijst vangt het op. Corrigeert het lokale feit "geen pool-element". |
| surface_area built / plot | optioneel, m² | built 176/225; plot 198/225 | definitie onbekend; voorbeelden van tegenstrijdigheid: 4628JAV plot 7276 m² in het veld, 2.210 + 2.541 + 639 + 1.963 = 7.353 m² in de tekst; C3XY4395JAV plot 1.227 m² in het veld, "1000 m2" in de tekst |
| energy_rating | A–G of X | consumption 60/225: A 16, B 6, E 5, D 4, C 1, X 1, **"Processing" 19, "In aanvraag" 5, "In request" 3**; emissions 2/225 | deels niet conform (vrije tekst) |
| url | per taal | alleen `url/en` (225/225), patroon `https://backgroundproperties.com/en/property/<slug>/` | conform maar eentalig |
| desc | verplicht | en/es/fr/nl 222, de 218; lengte 170 – >2.000 tekens; bevat **HTML-fragmenten** (`<p>`, `<ul>/<li>`, `<strong>`, `<div>`, `<blockquote>` met attributen als `data-start`/`data-end`/`class`) en dubbel gecodeerde regelovergangen (`&amp;#13;`) | tekst schoonmaken vóór gebruik; teksten zijn kennelijk deels uit tekstverwerkers/AI-tools geplakt (type 4) |
| features | ≤ 35 tekens | 210/225; 66 unieke kenmerken in het 5 %-bestand, mengeling van Engels, Nederlands, Spaans ("Pool", "Paneles fotovoltaicos", "21% VAT", "water", "sewerage") | bruikbaar na normalisatie |
| images | ≤ 50, ≥ 1280×960 | 225/225; **2 – 130 per object, mediaan 23** (4.142 foto's in export 26); alleen attribuut `id`; geen `floorplan`; alle op backgroundproperties.com | boven Kyero-maximum bij een deel; resolutie niet gemeten |
| notes / part_ownership / leasehold | optioneel | aanwezig maar **altijd leeg** | — |
| catastral / video_url / virtual_tour_url / prime / email / contact_number / whatsapp_number | optioneel | **afwezig** | kadastrale referentie ontbreekt dus structureel |

Conclusie: BP volgt de Kyero-v3-opmaak, maar met genoeg afwijkingen (pool-tekst, energie-tekst, ontbrekende types, valse coördinaten, HTML in teksten, wisselende refs) dat een Deal Hunter-adapter **eigen validatie** nodig heeft in plaats van vertrouwen op "het is Kyero v3".

---

## 4. Actualiteit en wijzigingsdetectie (opdracht d, masterprompt 10)

### 4.1 Hoe vaak genereert BP, hoe vaak halen wij op

| Meting (type 3, 14-09-2026 23:08 CEST) | export 26 | 27 | 29 | 30 | 31 | 32 |
|---|---|---|---|---|---|---|
| `Last-Modified` van het exportbestand (UTC) | 13-09 23:34:03 | 13-09 23:47:03 | 14-09 00:02:03 | 14-09 00:16:03 | 14-09 00:32:03 | 14-09 00:55:03 |
| Grootte | 1,99 MB | 0,95 MB | 1,03 MB | 0,21 MB | 0,96 MB | 0,74 MB |

Alle zes bestanden zijn in **één nachtelijk venster** aangemaakt (01:34 – 02:55 CEST), elk op `:03` seconden en telkens 13–23 minuten na elkaar: het patroon van een geplande batch (WP All Export "scheduled export"). Dit is één waarneming; dat het élke nacht gebeurt is een gevolgtrekking (type 4) die door een tweede meting op een andere dag of door BP moet worden bevestigd. Consequentie: **onze uurlijkse (api) en tweeuurlijkse (site) ophaalrondes zien 23 van de 24 keer hetzelfde bestand.** De `Last-Modified`-header is bovendien een gratis "is er iets veranderd?"-signaal dat nu niet wordt gebruikt.

Effectieve vertraging, uitgaand van één nachtelijke export (type 5): wijziging bij BP overdag → volgende export de nacht erna (≤ 24 h) → onze volgende ronde (≤ 1–2 h) → **tot ca. 26 h** tussen wijziging en zichtbaarheid bij ons; niets is "realtime".

### 4.2 Wat `date` betekent

- Kyero: "Last modified date for this property". BP levert unieke tijdstempels met seconden; de jongste (12-09-2026 10:47:44) ligt twee dagen vóór de meting; 35 objecten delen 14-05-2026 (bulkbewerking, vermoedelijk een sitebrede opslag). Dat past bij "laatst gewijzigd in WordPress" (type 4). Niet bewezen: of een prijswijziging de `date` altijd bijwerkt, en of `date` bij een nieuw object gelijk is aan de publicatiedatum. Vraag 5 aan BP (sectie 6.3).
- Gevolg voor het datamodel: `source_modified_at` = `date`; `source_published_at` = ONBEKEND (niet in de feed); `first_seen_at` = ons eigen tijdstip van eerste waarneming.

### 4.3 Ontwerp: nulmeting en wijzigingsdetectie op een momentopname zonder statusveld

Uitgangspunt: **een ophaalronde mag alleen iets wijzigen als hij "geldig" is; ongeldige rondes registreren alleen BRON NIET BEREIKBAAR.**

**Stap 1 — geldigheidspoort per ronde (harde eisen)**
1. HTTP 200 op de feed-URL na redirect; `Content-Type: application/xml`.
2. XML parseert; `root/kyero/feed_version` = 3; er is een `agent`-blok.
3. Aantal `property` ≥ 1 én ≥ `min_count` (voor export 36: bijvoorbeeld 70 % van de mediaan van de laatste 7 geldige rondes; voor elk deelbestand een eigen drempel).
4. Structuurcontrole: `id`, `ref`, `price`, `town`, `type` aanwezig bij ≥ 95 % van de objecten (een halve of afgekapte export geeft parsefouten of lege velden).
5. Als meerdere exports worden gebruikt: kruiscontrole 26 ∪ 27 = 36 (nu exact 225 = 225); wijkt dat af, markeer de ronde als "onvolledig" en pas geen verwijderingen toe.
6. `Last-Modified` opslaan als `feed_file_modified_at`. Is hij gelijk aan de vorige ronde, dan is de inhoud per definitie ongewijzigd: alleen `last_successful_fetch_at` bijwerken en de diff overslaan (spaart werk en voorkomt schijnbewegingen).

**Stap 2 — identiteit** (masterprompt 11): primaire sleutel `source_id` = BP-`id` (WordPress-post-id, stabiel); `ref` als secundaire sleutel (39 van 225 wijken af van de slug, dus refs bewegen). Een nieuwe `id` met dezelfde combinatie van plaats + type + plot + built + prijs, of dezelfde fotobestandsnamen (`4676JAV_02.jpg`), is een kandidaat voor OPNIEUW AANGEBODEN / herpublicatie — ter beoordeling, niet automatisch samenvoegen.

**Stap 3 — gebeurtenissen per object** (vergelijking van de huidige geldige momentopname met de laatst bekende toestand):

| Gebeurtenis (sectie 10) | Regel |
|---|---|
| NIEUW DOOR ONS ONTDEKT | `id` niet eerder gezien → `first_seen_at` = nu. |
| NIEUW GEPUBLICEERD | idem én `date` ≤ 72 h oud. Zonder publicatiedatum in de feed blijft dit een benadering; als `date` ouder is, was het object al langer bij BP (of bij een partner) in de handel. |
| PRIJS GEWIJZIGD | `price` ≠ vorige `price` → nieuwe rij in `price_history` (oude prijs, nieuwe prijs, `date`, `observed_at`). Nooit overschrijven. |
| STATUS / INHOUD GEWIJZIGD | `date` of de hash van (type, beds, baths, built, plot, location_detail, features, aantal foto's, desc) verandert → materieel? Alleen heranalyse bij prijs, oppervlak, type, foto's of tekstlengte ± 20 %. |
| NIET MEER GEVONDEN | `id` ontbreekt in **twee opeenvolgende geldige rondes met verschillende `Last-Modified`** (dus twee verschillende nachtelijke exports) → `last_seen_at` blijft staan, status "niet meer gevonden", **nooit** "verkocht" (masterprompt 8 en 10). Bij één ontbrekende ronde: nog niets. |
| OPNIEUW AANGEBODEN | `id` keert terug na "niet meer gevonden", of een nieuwe `id`/`ref` matcht op sleutelkenmerken of fotobestandsnamen → gebeurtenis + koppeling ter beoordeling. |
| DOOR BRON ALS VERKOCHT GEMELD | niet mogelijk met deze feed; alleen na een handmatige of per e-mail ontvangen melding van BP. |
| BRON NIET BEREIKBAAR | elke mislukte poort → teller; alarm na 3 opeenvolgende mislukkingen of > 6 h zonder geldige ronde; dagrapport meldt "geen nieuwe gegevens ontvangen sinds …" apart van "geen nieuwe kansen". |

**Stap 4 — bescherming tegen lege en halve feeds (het incident van vanavond als toets)**
- 22:12: DNS-fout → poort 1 faalt → ronde ongeldig → geen enkele objectstatus verandert, wel BRON NIET BEREIKBAAR; om 23:00 slaagt de ronde en is er niets te melden (zelfde `Last-Modified`). In de huidige properties-api leidde hetzelfde incident tot "0 objecten" gedurende 48 minuten; in de site-import correct tot "afgebroken, niets geschreven".
- Een export die wél 200 geeft maar half is (bijv. afgebroken schrijfactie bij BP) valt op poort 3 of 4.
- Uitval van één deelbestand (HTTP 500 op export 27 is 6 keer gezien) mag nooit tot verwijderingen leiden: verwijderingen alleen op basis van export 36, of alleen als álle deelbestanden geldig zijn.
- Ophaalfrequentie: één geldige ronde per dag na 03:30 CEST is inhoudelijk genoeg; een tweede rond 12:00 als vangnet. Vaker belast BP zonder opbrengst.

**Stap 5 — dienstverbetering die nu al kan** (alleen na overleg, raakt draaiende dienst): in `feeds.js` de bestaande set behouden als een ronde 0 objecten of > 30 % minder oplevert; DNS-wachtlus bij start (zoals bij Tree AI OS gedaan); tijdstempels in de log; `Last-Modified` en `If-Modified-Since` gebruiken.

---

## 5. Overlap met Idealista (opdracht e)

Methode: zes Jávea-objecten uit de lokale API (dus uit de BP-feed van 14-09-2026 23:00) opgezocht met de officiële Idealista-assistent (MCP van Idealista, locale es-ES, country es, maxResults 50, steeds met "Jávea" in de zoekopdracht). Match = zelfde prijs én zelfde oppervlak(ten) én een omschrijving die een vertaling van de BP-tekst is. Alle waarnemingen type 3; de toeschrijving "via een BP-partner" is type 4.

| BP-ref | BP-feed (prijs · built · plot · wijk) | Op Idealista gevonden | Zekerheid |
|---|---|---|---|
| 4432JAV | € 990.000 · 269 m² · 4.008 m² · Las Laderas · coördinaten fout (Miami) | 3 advertenties à € 990.000: 106204351 (269 m², "parcela de 4.008 m²", Sol de Este–Puerta Fenicia), 108329572 (269 m², "4008 m²", Monte Olimpo), 106630682 (239 m², "4000 m²", Monte Olimpo) — alle drie met **prijsdaling € 1.200.000 → € 990.000 (−18 %)** | hoog: prijs + m² + vertaalde tekst identiek; let op: drie verschillende wijkaanduidingen voor hetzelfde huis |
| 4628JAV | € 725.000 · 200 m² · 7.276 m² · Las Laderas (finca, geen water/stroom) | 6 advertenties à € 725.000 / 200 m²: 110839669, 112516511, 110837390, 110844607, 110961581, 111672523 (deze noemt "7.353 m2, vier parcelas registrales"); twee met status `renew` | hoog |
| 4649JAV | € 530.000 · 3.737 m² · Portichol / Mar Azul, "Dotacional Privado" | 112165477 (€ 530.000, 3.737 m², **vorige prijs € 555.000, −5 %**, vertaalde BP-tekst); daarnaast 106761721 (€ 525.000, 3.737 m², **particuliere** adverteerder, vorige prijs € 555.000) | hoog; tweede advertentie is dezelfde grond via de eigenaar zelf, € 5.000 goedkoper |
| C3XY4395JAV | € 375.000 · 157 m² · 1.227 m² · Tarraula (voormalig restaurant, horecalicentie) | 6 advertenties à € 375.000 / 157 m²: 111123687, 105231157, 106467694, 111123654, 109356272, 111624873 (deze: 1 badkamer, status `renew`, tekst nadrukkelijk als renovatie- en horecaproject); zonelabels lopen uiteen (La Lluca–Tarraula, Montgó–Ermita, Centro Ciudad) | hoog |
| 4544JAV | € 850.000 · 152 m² huis · 2.600 m² · Adsubia, splitsbaar in twee kavels | 110436215 (€ 850.000, 2.600 m², Adsubia, letterlijke vertaling van de BP-tekst) | hoog |
| 4676JAV | € 505.000 · 1.570 m² · Montgó–Ermita / Garroferal, met bouwvergunning en 70 % project | **10 advertenties**: 112256480, 112280961, 112386422, 112297090, 112297374, 112447297, 112311948, 112278145, 112410200 (à € 505.000, 1.570 m²) en 112283303 (€ 500.000, 1.571 m², met adres); ook op ikzoekeenhuisinspanje.nl als "BP-4676JAV" | hoog |

**Uitkomst: 6 van 6 (100 %) BP-Jávea-objecten staan op Idealista, samen in 27 advertenties** (1 tot 10 per object). Het patroon is consistent met het bedrijfsmodel van BP: partnermakelaars publiceren elk zelf op Idealista, met vertaalde BP-teksten en BP-foto's, zonder BP als bron te noemen. Twee bijvangsten die voor Deal Hunter tellen:

1. **Idealista toont prijshistorie die de BP-feed niet heeft** (`formerPrice`, percentage): 4432JAV −18 %, 4649JAV −5 %. Voor "PRIJS GEWIJZIGD" is Idealista dus de rijkere bron, zolang gebruik binnen de voorwaarden van de assistent valt (niet bewezen, zie R00).
2. **Dezelfde grond kan via een particulier goedkoper staan** (4649JAV: € 525.000 tegenover € 530.000 via het netwerk). Een acquisitiedossier moet die route zichtbaar houden.

Beperking: zes objecten is een steekproef, gekozen op onderscheidende kenmerken (grote percelen, renovatieobjecten). Voor gewone villa's in de € 1–2 miljoen-klasse is de overlap niet gemeten, maar er is geen reden om een ander patroon te verwachten (type 4). Wat níet is vastgesteld: of BP-objecten eerder bij BP zichtbaar zijn dan op Idealista (BP heeft geen publicatiedatum; Idealista geeft er ook geen).

---

## 6. Rechten (opdracht f)

### 6.1 Wat we weten (type 3 tenzij anders vermeld)

- De zes feed-URL's mét sleutel zijn aan TREE verstrekt en worden sinds april (properties-api) en 25-08-2026 (site-import) gebruikt om het aanbod op treeproperties.es te tonen; de sleutel stond eerder ook in een intern leadgen-plan (conflictregister #13; rotatie nog een open punt).
- Doel waarvoor ze zijn verstrekt: de website (tree-properties/CLAUDE.md: "Woningaanbod komt uit Background Properties via Kyero v3 XML feeds"). Een schriftelijke overeenkomst, e-mail met voorwaarden of licentietekst is in de onderzochte mappen **niet gevonden**.
- BP publiceert geen feedvoorwaarden. De aviso legal (type 1) zegt over de site-inhoud: "la reproducción total o parcial, uso, explotación, distribución y comercialización, requiere en todo caso de la autorización escrita previa por parte del prestador", en: "El prestador NO AUTORIZA expresamente a que terceros puedan redirigir directamente a los contenidos concretos del sitio web". Het privacybeleid noemt geen doorgifte aan makelaars of partners.
- De toegangspagina (type 1): "Our property information is for the exclusive use of our estate agents." TREE Properties is zo'n makelaar in de praktijk, maar staat niet op de openbare partnerlijst.
- Foto's: alle 4.142 foto-URL's wijzen naar backgroundproperties.com; onze site-import kopieert ze naar Sanity (`IMPORT_UPLOAD_IMAGES=true`); de properties-api en het embed-script hotlinken. README en CLAUDE.md van de site noteren al als open punt: "Bevestigen bij Background Properties of foto's gehotlinkt mogen worden en of foto URL's stabiel zijn."
- Teksten: omschrijvingen zijn van BP (of van de eigenaar/partner), staan op treeproperties.es onder TREE-naam.
- Persoonsgegevens: de feed bevat geen eigenaarsgegevens; wel exacte locaties, foto's van interieurs en soms adresachtige omschrijvingen. Idealista-advertenties bevatten soms een straatnaam en nummer.

### 6.2 Wat we níet weten (allemaal type 7)

| Vraag | Stand |
|---|---|
| Mogen we de feed opslaan en historisch bewaren (ook van objecten die uit de feed zijn)? | ONBEKEND |
| Mogen we de gegevens met AI analyseren voor interne selectie, waardering en dossiers? | ONBEKEND |
| Mogen we foto's onderling en met andere bronnen vergelijken (beeldhashes) voor deduplicatie? | ONBEKEND |
| Mogen we objectgegevens tonen aan derden buiten de website (dossier voor koper/investeerder, Rocksure)? | ONBEKEND; aviso legal wijst op schriftelijke toestemming |
| Mogen foto's gehotlinkt worden? | ONBEKEND; aviso legal verbiedt direct doorlinken naar site-inhoud, wat op hotlinking kan slaan |
| Is de sleutel persoons- of bedrijfsgebonden, mag hij in meer systemen (Deal Hunter naast de site)? | ONBEKEND |
| Wie is eigenaar van foto's en teksten (BP, eigenaar, fotograaf)? | ONBEKEND |
| Bestaat er een partnerovereenkomst met commissieafspraken die het gebruik regelt? | Niet gevonden; ⏸️ ACTIE VOOR JAN: nagaan wat er destijds is afgesproken (mail, WhatsApp, mondeling) |
| Hoe vaak, hoe laat en met welke logica wordt de export gemaakt? | Vermoedelijk nachtelijk (sectie 4.1), te bevestigen |
| Betekenis van `date`, van de ref-voorvoegsels `C3XY`/`C4XY`, en van wisselende refs | ONBEKEND |

### 6.3 De exacte vragen aan BP

1. Bevestig je schriftelijk dat TREE Properties de zes (zeven) export-URL's mag gebruiken, en voor welke doelen: website, intern aanbodbeheer, acquisitieanalyse?
2. Mogen we de feedgegevens **opslaan en historisch bewaren**, inclusief prijsverloop en de datum van eerste en laatste vermelding, ook nadat een object uit de feed is verdwenen? Zo ja, hoe lang?
3. Mogen we teksten en kenmerken **met AI laten analyseren** voor eigen selectie, waardering en dossiers?
4. Mogen we **foto's vergelijken** (onderling en met foto's uit andere bronnen) om dubbele advertenties te herkennen, en mogen we daarvan beeldkenmerken (hashes) bewaren?
5. Mogen we objectgegevens **tonen aan derden** buiten treeproperties.es: in een dossier voor een koper of investeerder, in een intern rapport, of via een ander merk van de groep?
6. Mogen **foto's rechtstreeks vanaf jullie server** worden geladen (hotlinken), of moeten we ze kopiëren? Zijn de foto-URL's stabiel? Wie heeft het auteursrecht op foto's en teksten?
7. **Hoe vaak en hoe laat** wordt de export aangemaakt (wij zien alle zes bestanden tussen 01:30 en 03:00 's nachts)? Is een frequentere export of een melding bij wijziging mogelijk?
8. Wat betekent het veld `date` precies (laatste wijziging, eerste publicatie)? Wordt hij bij een prijswijziging bijgewerkt? Waarom wijken bij 39 objecten `ref` en URL-slug af, en wat betekenen de voorvoegsels `C3XY` en `C4XY`?
9. Kunnen jullie **verkochte of ingetrokken objecten** markeren (status, verkoopdatum) of een aparte lijst van ingetrokken referenties leveren?
10. Kunnen de velden die wél op jullie objectpagina staan (oriëntatie, afstand tot zee, terrein) en, als jullie die hebben, **bouwjaar en kadastrale referentie** (`catastral`, standaard in Kyero v3) aan de export worden toegevoegd? En kunnen `pool` en `energy_rating` in de Kyero-notatie (0/1; A–G/X)?
11. Is de sleutel gebonden aan TREE als bedrijf of aan de website? Krijgen we bericht als hij wordt vervangen, en is een tweede sleutel voor een testomgeving mogelijk?
12. Wie is bij BP het aanspreekpunt voor techniek, en wie voor de zakelijke afspraken?

### 6.4 Conceptmail (niet verzenden; ⏸️ ACTIE VOOR JAN: nalezen, naam invullen, versturen)

> **Onderwerp:** Onze koppeling op jullie Kyero-feed: een paar vragen over gebruik en verversing
>
> Beste [naam],
>
> Sinds augustus draait treeproperties.es op jullie Kyero-feed (export 36 plus de commissie-exports 26 en 27) en dat werkt goed: elke twee uur halen we het bestand op, 225 objecten op dit moment. Omdat we de gegevens breder willen gaan gebruiken dan alleen de site, wil ik een paar dingen zwart op wit hebben voordat we verder bouwen.
>
> 1. Mogen we de feed opslaan en de historie bewaren (prijs, beschikbaarheid, datum van eerste en laatste vermelding), ook van objecten die niet meer in de feed staan?
> 2. Mogen we teksten en kenmerken met AI laten analyseren voor eigen selectie en advies, en mogen we foto's onderling en met andere bronnen vergelijken om dubbele advertenties te herkennen?
> 3. Wat mogen we tonen aan derden: alleen op treeproperties.es, of ook in een dossier voor een koper of investeerder? En mogen foto's rechtstreeks vanaf jullie server geladen worden, of moeten we ze kopiëren?
> 4. Hoe vaak wordt de export aangemaakt? Wij zien nu één keer per nacht, tussen 01.30 en 03.00 uur. Klopt dat, en is vaker mogelijk?
> 5. Wat betekent het veld `date` precies: laatste wijziging of eerste publicatie? En verandert een referentie weleens voor hetzelfde object?
> 6. Verkochte of ingetrokken objecten verdwijnen nu gewoon uit het bestand. Kunnen jullie een status of verkoopdatum meegeven, of een aparte lijst van ingetrokken referenties?
> 7. Op jullie objectpagina staan velden die niet in de export zitten: oriëntatie, afstand tot zee, terrein. Kunnen die erin, net als bouwjaar en kadastrale referentie als jullie die hebben?
> 8. Is de sleutel gebonden aan TREE of aan de website, en horen we het als hij wordt vervangen? Een tweede sleutel voor een testomgeving zou ons helpen.
>
> Een korte schriftelijke bevestiging per punt is voor ons genoeg; daar hoeft geen contract van te komen. Wil je liever bellen, dan schikt donderdag of vrijdag.
>
> Groet,
> Jan

---

## 7. Veldmapping BP → intern datamodel (opdracht g, masterprompt 12)

Regels vooraf: (1) lege of ontbrekende waarde = `ONBEKEND`, nooit 0, "nee" of "vrij"; (2) elke waarde krijgt `source = "bp"`, `evidence_type = 1` (door aanbieder vermeld), `checked_on` = ophaaltijd; (3) afgeleide velden krijgen `evidence_type = 4` en de regel waarmee ze zijn afgeleid.

| Intern veld (sectie 12) | BP-veld | Transformatie | ONBEKEND-regel / opmerking |
|---|---|---|---|
| **Identificatie** | | | |
| `source` | — | vaste waarde `bp` | |
| `source_id` | `id` | string, primaire sleutel (WordPress-post-id) | ontbreekt → record weigeren |
| `source_ref` | `ref` | string, trim, hoofdletters | wijzigt soms; nooit als identiteit gebruiken |
| `source_url` | `url/en` | string | andere talen: ONBEKEND |
| `listing_agent` | `agent/name` (BP) | bedrijfsnaam BP; verkopende partner ONBEKEND | vraag 12 |
| `source_modified_at` | `date` | `YYYY-MM-DD HH:MM:SS` + tijdzone Europe/Madrid (zomer/winter) → UTC | betekenis te bevestigen (vraag 8) |
| `source_published_at` | — | ONBEKEND | |
| `first_seen_at` / `last_seen_at` / `last_successful_fetch_at` | — | eigen tijdstempels (sectie 4.3) | |
| `feed_file_modified_at` | HTTP `Last-Modified` | per export | |
| `commission_class` | export-lidmaatschap (26/29/31 = 5 %; 27/30/32 = 3–4 %) | `high` / `standard` / `unknown` | intern, nooit naar buiten |
| **Locatie** | | | |
| `municipality` | `town` | normaliseren (Javea/Xàbia → Jávea; El Vergel → El Verger; Calp → Calpe) | leeg → ONBEKEND |
| `microlocation` | `location_detail` | string; urbanisatienaam | leeg (43/225) → ONBEKEND |
| `postcode` | `postcode` | string | leeg (158/225) → ONBEKEND |
| `province` / `country` | `province` / `country` | string | |
| `address` | — | ONBEKEND | Idealista/BP-pagina soms met straat; niet uit feed |
| `lat` / `lng` | `location/latitude`, `longitude` | float; **verwerpen** buiten bbox Spanje (lat 36–44, lng −9,5–4,5) en markeren buiten Marina Alta/Baixa (lat 38,45–38,95, lng −0,35–0,30) | 11 objecten met 25.68654/−80.431345 → ONBEKEND |
| `location_accuracy` | afgeleid | `urbanisation` als coördinaat geldig en `location_detail` gevuld; `municipality` als alleen plaats; `none` | type 4 |
| **Aanbod** | | | |
| `property_type` | `type` | Kyero-standaard → intern: Land → perceel; Villa → vrijstaand; Apartment → appartement; Town house → rijwoning; Country house → finca; Commercial property → commercieel | leeg (2/225) → ONBEKEND, eventueel uit tekst afleiden (type 4, markeren) |
| `offered_right` | — | ONBEKEND (volle eigendom niet aannemen); `part_ownership`/`leasehold` altijd leeg | |
| `asking_price` / `currency` / `price_type` | `price` / `currency` / `price_freq` | integer EUR; `sale` | |
| `price_history[]` | afgeleid | rij per waargenomen wijziging (sectie 4.3) | eerste waarneming = nulmeting, geen "daling" |
| `price_includes_vat` | `features` bevat "21% VAT" | `true` bij nieuwbouw/grond met 21 %; anders ONBEKEND | type 4 |
| `availability` | afgeleid | `seen` / `not_found` (na 2 geldige rondes) / `re_listed` | nooit "verkocht" |
| `sales_route` | — | vaste waarde `netwerk_makelaar` | veiling/bank niet uit feed af te leiden (5 teksten noemen bank/embargo/subasta: alleen als signaal) |
| `is_new_build` | `new_build` | `1` → true; `0` → false | leeg → ONBEKEND |
| **Afmetingen** | | | |
| `plot_area_m2` | `surface_area/plot` | float, definitie ONBEKEND (kadastraal of aanbiederschatting) | leeg → ONBEKEND; bij meerdere kavels in de tekst: markeren "pakket" |
| `built_area_m2` | `surface_area/built` | float, definitie ONBEKEND (bruto/netto/bebouwd) | leeg → ONBEKEND |
| `usable_area_m2` | — | ONBEKEND | |
| **Kenmerken** | | | |
| `bedrooms` / `bathrooms` | `beds` / `baths` | integer | leeg of 0 bij grond → ONBEKEND/n.v.t. |
| `build_year` | — | ONBEKEND | niet in feed; eventueel uit tekst (type 4) |
| `condition` | — | ONBEKEND; tekstsignalen (reform, renovate, opknappen, "para reformar") als `renovation_signal = true` (type 4) | 25/225 |
| `pool` | `pool` (tekst) | normaliseren: Private/Privé/Privat → `private`; Gemeenschappelijk/Common/Communal → `communal`; Nee/No → `none`; leeg → ONBEKEND; terugvallen op `features` | |
| `garage` / `terrace` / `views` / `orientation` | `features` | woordenlijst per kenmerk (Garage, Carport, Terrace, Solarium, Sea view …) | niet genoemd → ONBEKEND, niet "nee"; oriëntatie/afstand zee alleen op BP-pagina |
| `energy_label` | `energy_rating/consumption` | A–G of X; "Processing", "In aanvraag", "In request" → `pending`; leeg → ONBEKEND | emissions bijna nooit gevuld |
| `features[]` | `features/feature` | lijst, ontdubbelen, taal normaliseren | |
| **Onderbouwing** | | | |
| `description{lang}` | `desc/{en,es,nl,de,fr}` | HTML strippen, `&amp;#13;` ontcijferen, alinea's | |
| `images[]` | `images/image/url` | lijst, volgorde behouden, bestandsnaam bewaren (bevat ref → dedupe-signaal) | ≤ 130 per object; downloaden alleen na toestemming (vraag 6) |
| `floorplans[]` / `documents[]` / `video_url` / `virtual_tour_url` | — | ONBEKEND | |
| `cadastral_reference` | — | ONBEKEND (`catastral` afwezig) | koppeling via Catastro op coördinaat/adres is een aparte stroom |
| **Risico's** | | | |
| `occupancy` / `rental_status` / `legal_unknowns` / `planning_unknowns` | — | ONBEKEND; tekstsignalen (tenant, rented, okupa; licencia, project) alleen als markering | |
| `data_quality_flags[]` | afgeleid | `coord_invalid`, `type_missing`, `ref_slug_mismatch`, `plot_text_mismatch`, `energy_text`, `html_in_desc` | |

---

## 8. Registerregel en rol van BP

**Registerregel (masterprompt 7)**

| Veld | Waarde |
|---|---|
| Naam / website | Background Properties — backgroundproperties.com |
| Type aanbieder | Listingdienst met partnernetwerk (45 makelaars ES/BE/DE); eenmanszaak, Jávea; sinds 2017 |
| Dekking | Costa Blanca Noord (Marina Alta + deel Marina Baixa); 225 objecten, 57 in Jávea; koop, geen huur |
| Technische toegang | Kyero-v3-XML via WP All Export; 7 export-URL's met geheime sleutel (26, 27, 29, 30, 31, 32, 36); 302 → statisch bestand |
| Velden | zie sectie 3.2; geen status, historie, bouwjaar, staat, kadaster, makelaarsref, plattegrond |
| Foto's / documenten | 2–130 foto's per object op BP-server; geen documenten |
| Publicatie- en wijzigingsinformatie | alleen `date` (laatste wijziging, te bevestigen); geen publicatiedatum |
| Historie | geen; alleen wat wij zelf bewaren |
| Verversing | export nachtelijk (gemeten 01:34–02:55 CEST, te bevestigen); wij: elk uur (api) / elke 2 h (site) |
| Rate limits | onbekend; zes verzoeken per uur worden al ruim een half jaar bediend |
| Kosten | geen bekende kosten; commissiemodel bij verkoop via partner |
| Contractstatus | geen schriftelijke feedvoorwaarden gevonden; URL's verstrekt voor de website |
| Toegestane doelen | website (feitelijk); overige doelen ONBEKEND |
| AI-analyse / opslag / afgeleide gegevens / beeldvergelijking | ONBEKEND — vragen 2, 3, 4 |
| Contact / aanvraagroute | hola@backgroundproperties.com, +34 670 412 191; concept-mail sectie 6.4 |
| Laatste verificatie | 14-09-2026 |
| Open vragen | sectie 6.3 (12 vragen) |
| **Operationele status** | **Technisch: GEVERIFIEERD EN ACTIEF (website). Voor Deal Hunter: CONTRACT OF TOESTEMMING NODIG.** |

**Rol: unieke bron of "ons netwerk"?**

- Niet uniek: 6 van 6 geteste Jávea-objecten staan op Idealista, gemiddeld 4,5 keer. Wat BP heeft, heeft de markt ook — en Idealista heeft er in Jávea een veelvoud van (238 percelen tegenover 24 bij BP).
- Wel waardevol als **ons netwerk**: gestructureerde, gelicentieerde (nog te bevestigen) data zonder scraping, met commissieklasse en direct contact met een partij die de eigenaar kent; lage kosten; al draaiende adapter en drie weken importlogboek als testset voor validatie en wijzigingsdetectie; route D (bemiddeling) en route C (renovatie-opdrachten) profiteren van de relatie meer dan van de data.
- Wat BP níet levert: prijshistorie, publicatiedatum, staat, bouwjaar, kadaster, bijzondere verkopen (0 bank/veilingobjecten aangetroffen; 5 teksten noemen zulke woorden alleen terloops).
- Aanbeveling voor fase B: BP als **eerste, kleine, goed geteste adapter** (nulmeting, validatiepoort, gebeurtenissen) en als kwaliteitsreferentie bij deduplicatie met Idealista; niet als maat voor "de markt in Jávea".

---

## 9. Open vragen en blokkades

**Open (inhoudelijk)**
1. Wat is destijds met BP afgesproken over de feed (mondeling, mail)? Wie is de contactpersoon? ⏸️ ACTIE VOOR JAN
2. Bevestiging van de nachtelijke exportfrequentie met een tweede meting op een andere dag (`Last-Modified` van de zes bestanden).
3. Betekenis van `date`, van `C3XY`/`C4XY` en van wisselende refs (vraag 8).
4. Definitie van `built` en `plot` bij BP (vraag 10).
5. Staat TREE Properties bewust niet op de partnerlijst van BP?
6. Mag de properties-api (poort 3100) worden aangepast (krimpbescherming, DNS-wachtlus, tijdstempels)? Raakt een draaiende dienst; alleen na overleg.
7. Tijdzonefout in `toIsoDate` (vast +02:00, ook in de winter) — klein, wel corrigeren bij de volgende wijziging van de site-import.

**Geblokkeerd of mislukt (niet omzeild)**
- `curl` op homepage en objectpagina van backgroundproperties.com: HTTP 403 met JavaScript-bot-check (CleanTalk) voor een niet-browser-User-Agent. WebFetch kreeg de pagina's wél.
- kyero.com "Estate agents in Javea": HTTP 403 voor WebFetch; niet vastgesteld of BP daar als makelaar staat.
- idealista.com `/pro/background-properties/`: HTTP 403 voor WebFetch; bestaan van een BP-pro-pagina niet vastgesteld.
- backgroundproperties.com/about-us/ en /legal-notice/: 404 (juiste pagina's zijn /aviso-legal/, /privacy/, /cookies-policy/, /makelaars/, /toegang/, /huiseigenaren/).
- Het WebSearch-budget van deze sessie raakte op (200 zoekopdrachten) vóór een laatste zoekopdracht naar de WP All Export-URL-documentatie; de exportmechaniek is daarom uit de HTTP-antwoorden zelf afgeleid (302 naar `wpallexport/exports/…/current-….xml`), niet uit de documentatie van de plug-in.
- De raw feed van export 36 is niet apart geïnspecteerd (sleutel alleen in `.env.local` van de site); export 26 is als representatief genomen (26 ∪ 27 = 36 in aantallen).

---

## Bronnen

| # | Bron | URL | Datum | Type |
|---|---|---|---|---|
| 1 | BP aviso legal (bedrijfsgegevens, IE-bepalingen) | https://backgroundproperties.com/aviso-legal/ | 14-09-2026 | 1 |
| 2 | BP homepage EN (bedrijfsmodel, sinds 2017, commissie, exclusiviteit) | https://backgroundproperties.com/en/ | 14-09-2026 | 1 |
| 3 | BP partnerlijst (45 kantoren) | https://backgroundproperties.com/makelaars/ | 14-09-2026 | 1 |
| 4 | BP "Onze makelaars" / our-agents | https://backgroundproperties.com/onze-makelaars/ · https://backgroundproperties.com/our-agents/ | 14-09-2026 | 1 |
| 5 | BP toegang voor makelaars | https://backgroundproperties.com/toegang/ · https://backgroundproperties.com/en/access/ | 14-09-2026 | 1 |
| 6 | BP huiseigenaren | https://backgroundproperties.com/huiseigenaren/ | 14-09-2026 | 1 |
| 7 | BP privacybeleid | https://backgroundproperties.com/privacy/ | 14-09-2026 | 1 |
| 8 | BP objectpagina 4676JAV (openbaar; velden; "Terms of Use"-link) | https://backgroundproperties.com/en/property/4676jav-spacious-plot-with-building-permit-for-sale-on-the-montgo-javea/ | 14-09-2026 | 1 |
| 9 | BP robots.txt, HTTP-headers, wp-json paginalijst | https://backgroundproperties.com/robots.txt · https://backgroundproperties.com/wp-json/wp/v2/pages | 14-09-2026 | 3 |
| 10 | BP export 26: één leesverzoek (302 → wpallexport-bestand; elementinventaris; Last-Modified) en Last-Modified van exports 27, 29–32 | feed-URL's met sleutel (niet opgenomen) | 14-09-2026 23:07–23:08 | 3 |
| 11 | Kyero XML Import Specification (helppagina) | https://help.kyero.com/estate-agents/xml-import-specification | 14-09-2026 | 2 |
| 12 | Kyero v3 import spec (tekstbestand, velddefinities) | https://feeds.kyero.com/assets/kyero_v3_import_spec.txt | 14-09-2026 | 2 |
| 13 | Kyero v3 export spec | https://feeds.kyero.com/assets/kyero_v3_export_spec.txt · https://help.kyero.com/xml-export-specification | 14-09-2026 | 2 |
| 14 | Kyero standaard-objecttypen | https://help.kyero.com/property-types-used-in-kyero | 14-09-2026 | 2 |
| 15 | Kyero verwerkingsfrequentie van feeds | https://help.kyero.com/how-often-my-xml-feed-is-updated | 14-09-2026 | 2 |
| 16 | Houzez Property Feed: verkochte objecten blijven in Kyero-export (voorbeeld van Houzez-gedrag) | https://wordpress.org/support/topic/sold-properties-in-kyero-xml-feed-export/ | 14-09-2026 | 4 (illustratief; BP's export is WP All Export, niet deze plug-in) |
| 17 | WP All Export documentatie (real-time exports; geen URL-details gevonden) | https://www.wpallimport.com/documentation/how-to-run-real-time-exports/ | 14-09-2026 | 2 (beperkt) |
| 18 | Partnerpublicatie "BP-4676JAV" | https://ikzoekeenhuisinspanje.nl/woning/land-in-javea-alicante-bp-4676jav/ | 14-09-2026 | 3 |
| 19 | Idealista-assistent (officiële MCP), zoekopdrachten Jávea: terrenos Montgó–Ermita; terrenos € 520–540k; terrenos € 840–860k; chalets € 370–380k; chalets € 720–730k; chalets € 980k–1M; villas La Lluca–Tarraula | zoeklinks o.a. https://www.idealista.com/es/venta-terrenos/javeaxabia-alicante/con-precio-hasta_540000,precio-desde_520000/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_list | 14-09-2026 | 3 |
| 20 | Idealista-advertenties (matches), o.a. | https://www.idealista.com/es/inmueble/112165477/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail · https://www.idealista.com/es/inmueble/110436215/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail · https://www.idealista.com/es/inmueble/106204351/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail · https://www.idealista.com/es/inmueble/112386422/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail · https://www.idealista.com/es/inmueble/111123687/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail · https://www.idealista.com/es/inmueble/110839669/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail | 14-09-2026 | 3 |
| 21 | Lokaal: `~/tree-hermes/properties-api/feeds.js`, `server.js`, `package.json`, `logs/stdout.log`, `logs/stderr.log`; `~/Library/LaunchAgents/com.tree.properties-api.plist` | lokaal | 14-09-2026 | 3 |
| 22 | Lokaal: `~/tree-website/tree-properties/src/lib/import/{kyero,map,run,images,tree-ref}.ts`, `src/lib/work-area.ts`, `src/lib/alarm.ts`, `src/app/api/import/route.ts`, `README.md`, `CLAUDE.md`, `vercel.json`, `scripts/import-periodiek.sh`, `logs/import-2026-08-25…09-14.log`, `var/import-status.txt`, `test/fixture-kyero.xml`; `~/Library/LaunchAgents/com.tree.properties-import.plist` | lokaal | 14-09-2026 | 3 |
| 23 | Lokaal: lokale API http://127.0.0.1:3100 (`/api/health`, `/api/stats`, `/api/filters`, `/api/properties`) | lokaal | 14-09-2026 22:56 (0 objecten) en 23:00–23:05 (225 objecten) | 3 |
| 24 | Lokaal: `~/tree-es/properties/leadgen/docs/marktdata-bronnen.md`, `conflictregister.md`; `~/tree-es/controle-31-08-2026/treeproperties.md` | lokaal | 14-09-2026 | 3 |
| 25 | Masterprompt TREE Deal Hunter, secties 5–12, 27–31 | `~/tree-es/deal-hunter/MASTERPROMPT.md` | 14-09-2026 | — |

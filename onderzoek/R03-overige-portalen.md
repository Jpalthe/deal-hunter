# R03 — Overige portalen: pisos.com, yaencontre, Kyero, thinkSPAIN, SpainHouses, Green-Acres, Indomio

> **NA TEGENSPRAAK (15-09-2026).** Dit rapport is door een tweede agent gecontroleerd; zie `R03-overige-portalen.verificatie.md`. Betrouwbaarheid volgens die controle: middel.
> Weerlegd en in de eindstukken gecorrigeerd: R03-04; R03-05; R03-09; R03-11. Gebruik voor die punten de gecorrigeerde tekst in het verificatiebestand, niet de tekst hieronder.


**Project:** TREE Deal Hunter, fase A (bronnen en investeringskader)
**Stroom:** R03 — overige vastgoedportalen (masterprompt secties 6 en 7)
**Controledatum:** 14-09-2026
**Auteur:** onderzoeksagent R03 (AI), in opdracht van Jan

Bewijstypen volgens masterprompt sectie 5: **1** door aanbieder vermeld · **2** in officiële bron aangetroffen · **3** door ons rechtstreeks vastgesteld · **4** AI-inferentie · **5** berekening op benoemde aannames · **6** door bevoegde professional bevestigd · **7** onbekend of tegenstrijdig.

---

## Samenvatting (10 regels)

1. Geen van de zeven portalen biedt een officiële **lees-API, leesfeed of dataproduct** waarmee wij advertenties van anderen mogen ophalen; alle gevonden koppelingen zijn **publicatie-koppelingen** (eigen advertenties erop zetten).
2. **Kyero** hanteert de de-facto standaard voor makelaarsfeeds: de **Kyero v3 XML-importspecificatie** (laatste wijziging 03-09-2024; versielabel V3.8 in de spectekst, V3.9 op de helppagina). Een v4 bestaat niet; de validator kent alleen V2.0, V2.1 en V3.0.
3. De Kyero v3-feed is per definitie een **volledige momentopname** ("absolute feed … not an incremental one"); er is **geen status-, verkocht- of verwijderveld**. Verdwijnen uit de feed = verwijderd bij Kyero. Het `<date>`-veld is "last modified date … in your database" en stuurt alleen updates aan, geen publicatiedatum.
4. De Background Properties-feed wijkt op twee punten af van de Kyero-importspec: `postcode` op objectniveau (bestaat daar niet; wel in de exportspec en in de agent-node van de XSD) en het ontbreken van `pool` (in de spectekst "Mandatory", in de XSD optioneel).
5. Eigenaren: Kyero = Portal47 Ltd (VK), sinds 12-2024 onderdeel van idealista; thinkSPAIN = Think Web Content SL (Paterna, Valencia); pisos.com = Habitat.Soft S.L., sinds 03-2025 van Immobiliare.it S.p.A. (Indomio-groep, samen met indomio.es en enalquiler.com); yaencontre = sinds 2020 idealista-deelneming, later volledig opgegaan [te verifiëren]; SpainHouses = Entersoftweb S.L. (Málaga); Green-Acres = Green-Acres S.A.S. (Parijs, voorheen Realist).
6. Gebruiksvoorwaarden: Kyero verbiedt expliciet robots/scrapers en systematische extractie zonder schriftelijke toestemming; thinkSPAIN, HabitatSoft (pisos.com) en Green-Acres verbieden reproductie/commerciële exploitatie; Green-Acres sluit in robots.txt `ClaudeBot` uit; yaencontre en indomio.es blokkeren geautomatiseerde toegang technisch (403/DataDome). Voorwaarden van yaencontre en Indomio zijn niet leesbaar gebleken.
7. **E-mailalerts/opgeslagen zoekopdrachten** bestaan bij Kyero (dagelijks, alleen nieuw), thinkSPAIN ("Create Alert" + filter "Price Reduced in last 30 days"), SpainHouses (nieuwe advertenties + prijsalerts + filters "To reform"/"Reduced"), Green-Acres (dagelijks/wekelijks) en yaencontre (zoek-, prijsdaling- en wijzigingsalerts). Of geautomatiseerde verwerking van die e-mails is toegestaan, zegt geen enkel portaal.
8. Indicatief aanbod Jávea (te koop, 14-09-2026): thinkSPAIN 2.607 (waarvan 151 bouwkavels), Green-Acres 813, SpainHouses 488 woningen (322 huizen); via zoekmachinesnippets (datum onbekend): Kyero ±1.717, Indomio ±1.994, yaencontre ±1.755 casas + 742 pisos + 413 terrenos; pisos.com niet meetbaar. Ter vergelijking: de BP-feed had 56 objecten in Jávea (25-08-2026).
9. Partnerprogramma's of dataservices voor investeerders: niet gevonden. Kyero heeft een marktdatapagina (kyero.com/en/data, niet leesbaar) en Immobiliare.it een "Insights"-product voor Italië; dekking voor Spanje/Jávea is niet aangetoond. pisos.com publiceert maandelijkse prijsrapporten (persberichten).
10. Registerstatus (sectie 7): alle zeven portalen **ALLEEN HANDMATIG** voor het lezen van aanbod (via site en e-mailalerts); geautomatiseerd lezen bij Kyero, Green-Acres, yaencontre en Indomio **NIET GEBRUIKEN**; publicatiefeeds overal **CONTRACT OF TOESTEMMING NODIG** (adverteerdersaccount). Geen enkele bron is GEVERIFIEERD EN ACTIEF.

---

## 1. Methode en beperkingen

| Middel | Gebruik | Bewijstype |
|---|---|---|
| WebFetch van officiële pagina's | voorwaarden, helpcentra, feeddocumentatie, zoekpagina's Jávea | 2 (of 1 bij eigen claims van de aanbieder) |
| `curl` van `robots.txt` (eenmalig per domein) | crawl-regels, uitgesloten bots, sitemaps | 3 |
| `curl` van openbare Kyero-specbestanden (spec.txt, XSD, testfeed) | exacte formuleringen en XSD-structuur | 3 |
| WebSearch (zoekmachinesnippets) | alleen waar de pagina zelf geblokkeerd was; gemarkeerd als snippet | 7 / [te verifiëren] |
| Lokale bestanden (alleen-lezen, geen sleutels) | `~/tree-hermes/properties-api/server.js`: parserveldnamen | 3 |

**Geblokkeerd voor WebFetch (niet omzeild):** www.kyero.com (alle pagina's, incl. voorwaarden, /data, /aboutus, /join — HTTP 403; het helpcentrum help.kyero.com en feeds.kyero.com werken wél), www.pisos.com ("unable to fetch"), www.yaencontre.com (403 + DataDome-captcha, ook op robots.txt), www.indomio.es (403), www.green-acres.com/en/legal-notice (redirect naar 404), www.immobiliare.it/en/info/report-professionali (403), eleconomista.es en ejeprime.com (403). Zie sectie 10.

Alle tellingen zijn **indicatief**: portalen tellen verschillend (per advertentie, niet per object), en dezelfde woning staat vaak bij meerdere makelaars. Aantallen zeggen niets over uniek aanbod (masterprompt sectie 28).

---

## 2. Overzicht per portaal

| Portaal | Eigenaar (bron) | Dekking | Lees-API / leesfeed / dataproduct | Publicatie-import | E-mailalerts | Voorwaarden geautomatiseerde toegang | Jávea indicatief (14-09-2026) | Status sectie 7 (lezen) |
|---|---|---|---|---|---|---|---|---|
| **Kyero** | Portal47 Ltd, Engeland nr. 6536265 (snippet voorwaarden, [te verifiëren]); sinds 05-12-2024 onderdeel idealista (2) | Spanje, Portugal, Frankrijk, Italië; internationale kopers | Geen. Marktdatapagina bestaat (niet leesbaar). robots.txt: `Disallow: /*api/*` | Kyero v3 XML (absolute feed) + eigen exportfeed per makelaar | Ja: "Create property alert", standaard dagelijks, alleen nieuwe objecten | Expliciet verbod robots/scrapers/systematische extractie (snippet) | ±1.717 (snippet, datum onbekend) — pagina 403 | ALLEEN HANDMATIG; geautomatiseerd NIET GEBRUIKEN |
| **thinkSPAIN** | Think Web Content SL, CIF B02283380, Paterna (2) | Heel Spanje; 12 talen; internationale kopers | Geen. Analytics alleen voor adverteerders | XML-feeds van "a large number of property software companies"; eigen formaat niet openbaar; gratis XML-exportservice voor eigen aanbod | Ja: "Create Alert"/"Save Search"; filter "Price Reduced in last 30 days" | Reproductieverbod zonder schriftelijke toestemming; geen expliciete scraping-clausule | **2.607** te koop, **151** bouwkavels (pagina) | ALLEEN HANDMATIG |
| **pisos.com** | Habitat.Soft S.L., CIF B61562088, Barcelona; sinds 18-03-2025 Immobiliare.it S.p.A. (2, nieuws/CNMV-melding) | Heel Spanje; Spaanse kopers | Geen gevonden. Maandelijkse prijsrapporten (pers) | Niet openbaar gedocumenteerd; pakketten gekoppeld aan indomio.es (04-2025) | Niet controleerbaar (site geblokkeerd); robots.txt kent pad `/PriceDrop/` | HabitatSoft-aviso legal: geen commerciële exploitatie van inhoud | Niet meetbaar | ALLEEN HANDMATIG; TECHNISCH ONDERZOEK NODIG |
| **yaencontre** | Oorspr. Grupo Godó; idealista-deelneming sinds 02-2020 (2); volledige absorptie gemeld (snippet, [te verifiëren]) | Heel Spanje, oorsprong Catalonië; Spaanse kopers | Geen gevonden | Niet leesbaar (403) | Ja (helpcentrum, snippet): zoekalerts, prijsdalingsalerts, wijzigingen in bewaarde advertenties | Voorwaarden niet leesbaar; DataDome-blokkade (3) | ±1.755 casas, 742 pisos, 413 terrenos (snippets) | ALLEEN HANDMATIG; geautomatiseerd NIET GEBRUIKEN |
| **SpainHouses** | Entersoftweb, S.L., CIF B92308949, Málaga (2) | Heel Spanje; meertalig; eigenaren én professionals | Geen. Wel widgets voor eigen aanbod | Eigen XML (XSD cartera.xsd), 32+ CRM's, vanaf 10 €/maand | Ja: nieuwe advertenties per e-mail, "Save search", prijsalerts; filters "To reform" en "Reduced" | Geen IP-/scrapingclausule gevonden (alleen privacybeleid) | **488** woningen, waarvan **322** huizen (pagina) | ALLEEN HANDMATIG |
| **Green-Acres** | GREEN-ACRES S.A.S. (voorheen Realist), Parijs, RCS 453 785 156 (2) | 22 landen (snippet); Spanje 51.375 objecten (1); Europese tweedewoningkopers | Geen | Eigen XML "Gateway" (Envelope/add_adverts), cancel-and-replace, dagelijks opgehaald | Ja: "Save alert" dagelijks/wekelijks; filter "To renovate" | Reproductieverbod (art. 7); robots.txt: `ClaudeBot Disallow: /`, Request-rate 1/1 | **813** te koop (pagina) | ALLEEN HANDMATIG; geautomatiseerd NIET GEBRUIKEN |
| **Indomio** | Immobiliare.it S.p.A., Milaan; Spaans beheer "Indomio", Barcelona (snippet); groep omvat pisos.com en enalquiler.com (1) | Zuid-Europa; Spanje via indomio.es | Geen leesfeed; feedback-API's (leads, telefoons) alleen voor eigen advertenties; Immobiliare "Insights" (Italië) | REST-push-API, XML-payload, "almost real time", HTTP BASIC + IP-whitelist | Niet controleerbaar (403) | Voorwaarden niet leesbaar (403) | ±1.994 (snippet) | ALLEEN HANDMATIG; geautomatiseerd NIET GEBRUIKEN |

---

## 3. Kyero — portaal én feedstandaard

### 3.1 Eigenaar en positie
- Kyero.com wordt volgens de zoekmachinesnippet van de eigen voorwaarden "owned, operated and hosted in the UK by Portal47 Limited, a company registered in England with company number 6536265" — de voorwaardenpagina zelf (https://www.kyero.com/en/docs/terms/, titel "Updated 20-04-2026") gaf HTTP 403. Bewijstype 7/[te verifiëren].
- idealista/news, 05-12-2024: "idealista acquires Kyero"; Kyero is opgericht in 2003, gevestigd in Bath (VK), 33 medewerkers, "more than 7,000 estate agents"; "Kyero will retain its operational independence and will maintain its collaboration with key software providers and operators across its active markets." Bewijstype 2. Of Kyero sindsdien de idealista-database deelt: nergens vermeld → ONBEKEND.
- Dekking: Spanje, Portugal, Frankrijk, Italië (idealista/news; Apify-beschrijvingen bevestigen dit maar zijn geen officiële bron).

### 3.2 Feedspecificatie Kyero v3 (import) — de de-facto standaard
**Bronnen (bewijstype 3, ruwe bestanden via curl opgehaald 14-09-2026):** `https://feeds.kyero.com/assets/kyero_v3_import_spec.txt` (335 regels), `https://feeds.kyero.com/assets/kyeroV3.0.xsd` (11.171 bytes), `https://feeds.kyero.com/assets/kyero_v3_test_feed.xml` (3.021 bytes). Helppagina (bewijstype 2): https://help.kyero.com/estate-agents/xml-import-specification. Validator: https://feeds.kyero.com/validator/ (kent V2.0, V2.1, V3.0 en autodetect; **geen v4**).

**Versie:** de spectekst opent met "New in V3.8 - 03-09-2024 (added `<contact_number>`, `<whatsapp_number>`)"; de helppagina zegt "Last modified 03rd September 2024 - V3.9". Zelfde datum, ander nummer → bewijstype 7 (inconsistent, functioneel irrelevant). Versiegeschiedenis: V3.0 09-12-2013 (import/export gelijkgetrokken, `new_build` uit `price_freq`, `surface_area`/`location`/`energy_rating`/`url` toegevoegd), V3.1 10-02-2015 (max 50 foto's), V3.2 11-03-2016 (ref max 255, `desc` verplicht als geen `features`), V3.3 01-06-2016 ('week' uit `price_freq`), V3.4 11-08-2017 (`country`), V3.5 08-04-2020 (`video_url`, `virtual_tour_url`, `catastral`), V3.6 19-08-2020 (image-tag floorplan), V3.7 07-07-2021/14-05-2022 (`email`, `prime`), V3.8 03-09-2024.

**Veldtabel (spectekst vs. XSD):**

| Element | Spectekst | XSD (`minOccurs`) | Opmerking |
|---|---|---|---|
| `root` > `kyero` > `feed_version` = 3 | verplicht | verplicht | XSD kent ook optioneel `feed_generated` |
| `agent` (id, name, email, tel, fax, mob, addr1, addr2, town, region, **postcode**, country) | niet in importtekst | optioneel (alle subvelden optioneel) | Makelaarsblok uit de exportspec; `postcode` is hier de postcode van het kantoor |
| `property` > `id` | verplicht, alfanumeriek max 50 — "Your database or other unique identifier … Used in conjunction with the `<date>` tag to determine if the property should be added or updated" | verplicht | Sleutel voor deduplicatie binnen één feed |
| `date` | verplicht, `YYYY-MM-DD HH:MM:SS` — **"Last modified date for this property in your database. If a last modified date is not available or accurate, the feed will only be processed once a week"** | verplicht | Géén publicatiedatum. Helppagina: "When we see a change in the `<date>` tag, the property will be UPDATED … if the date does not change, we will not update the property." |
| `ref` | verplicht, max 255 — "Your customer-visible reference" | verplicht | |
| `price` | verplicht, numeriek max 8 tekens, hele getallen | verplicht | |
| `currency` | optioneel: EUR, GBP, USD (GBP/USD worden naar EUR omgerekend) | optioneel | |
| `price_freq` | verplicht: 'sale' of 'month' | verplicht | 'week' verwijderd in V3.3 |
| `part_ownership`, `leasehold` | optioneel, '1' bij deelrecht/leasehold | optioneel | Relevant voor "aangeboden recht" (masterprompt 11/19) |
| `new_build` | optioneel, '1' als jonger dan 12 maanden | optioneel | |
| `type` | verplicht, "converted to a Kyero standard property type" | verplicht | Geen vaste waardelijst in de spectekst |
| `town`, `province` | verplicht, "preferably a valid Correos location eg: Javea, Nerja" | verplicht | |
| `country` | optioneel, standaard Spain | optioneel | |
| `location` > `latitude`, `longitude` | optioneel, max 15 tekens, "'0' if unknown" | optioneel | |
| `location_detail` | optioneel, max 50, "village or urbanisation" | optioneel | Bruikbaar voor microlocatie/urbanisatie |
| `beds`, `baths` | "Mandatory numeric … '0' if unknown" | optioneel, nillable | Tekst en XSD verschillen |
| `pool` | **"Mandatory numeric — '1' if a pool is available, Empty, missing tag or '0' if unknown"** | **optioneel** | Tekst en XSD verschillen; '0' betekent onbekend, niet "geen zwembad" |
| `surface_area` > `built`, `plot` | optioneel, m² | optioneel | Geen definitie van "built" (bruto/netto) → oppervlaktebegrip ONBEKEND |
| `energy_rating` > `consumption`, `emissions` | optioneel, A–G of X | optioneel | |
| `url` (per taal: ca, da, de, en, es, fi, fr, it, nl, no, pt, ru, sv) | optioneel | optioneel | |
| `video_url`, `virtual_tour_url` | optioneel, max 255 | optioneel | |
| `catastral` | optioneel, 20 tekens zonder spaties — "Property cadastral reference" | optioneel | **Direct bruikbaar voor perceelkoppeling (masterprompt 14) als de makelaar het vult** |
| `desc` (per taal) | verplicht als geen `features`; UTF-8, geen HTML | verplicht | |
| `features` > `feature` | optioneel, max 35 tekens per feature, Spaans of Engels | optioneel | |
| `notes` | optioneel, max 255 | optioneel | |
| `images` > `image id="1..50"` > `url` (+ `tags` > `tag` floorplan) | max 50; min. 1280×960; volgorde behouden; geen placeholders; geen CDATA | verplicht element | Plattegrond alleen herkenbaar via tag |
| `prime`, `email`, `whatsapp_number`, `contact_number` | optioneel | optioneel | |
| **Status / beschikbaarheid / verkocht / verwijderd** | **niet aanwezig** | **niet aanwezig** | grep op delete/remov/sold/status in spec.txt en XSD: alleen versiehistorie-regels; geen veld |
| `postcode` op objectniveau | **niet aanwezig** | **niet aanwezig** | Wel in de **export**spec (v3.1) als verplicht objectveld |

**Semantiek verwijderen en verversen (helppagina, bewijstype 2, letterlijk):**
- "Your property feed must be an absolute feed of all your property information - not an incremental one."
- "If a property is DELETED from your database, there will be no property record for it in your feed. We DELETE properties and any associated images from our database when there is no matching property record in your feed."
- "Once your properties are live, we will process your feed every day at approximately 01:30 CET."
- "Feeds that do not conform to our specification or display adverse behaviour may be updated once per week only or disabled."
- Aanvullend (help.kyero.com/how-often-my-xml-feed-is-updated en Prime-pagina): Prime-accounts "the following nights: Sunday/Monday … Thursday/Friday"; "Free accounts … once per week"; "Prime accounts will receive a daily update where Free accounts will be weekly".

**Gevolg voor Deal Hunter (bewijstype 4):** een Kyero v3-feed kent alleen de toestanden "staat erin" en "staat er niet meer in". Verdwijnen = NIET MEER GEVONDEN, nooit DOOR BRON ALS VERKOCHT GEMELD. `<date>` is `source_modified_at`; `source_published_at` bestaat niet in dit formaat; `first_seen_at` is onze eigen waarneming. Prijshistorie moet zelf worden opgebouwd uit opeenvolgende snapshots. Een lege of mislukte download mag nooit als "alles verkocht" worden gelezen — precies wat op 14-09-2026 lokaal gebeurde (0 objecten na DNS-fout).

### 3.3 Kyero v3 exportspecificatie
Bron: https://help.kyero.com/xml-export-specification en `https://feeds.kyero.com/assets/kyero_v3_export_spec.txt` (bewijstype 2). "Every estate agent using Kyero.com can access a unique property feed" met uitsluitend de **eigen** objecten; bedoeld als distributiehub naar andere portalen. Versie 3.1 (16-07-2015). Verplicht: `feed_version`, volledig `agent`-blok, `property` (id, date, ref, price), `price_freq` (hier nog sale/week/month), `type`, `location_id`, `town`, **`postcode`**, `province`. Geen gebruiksbeperkingen in het document. **Dit is geen toegang tot andermans aanbod.**

### 3.4 Vergelijking met de Background Properties-feed (lokaal vastgesteld, bewijstype 3)
| Punt | BP-feed (parser `properties-api`, waargenomen velden) | Kyero v3 import | Beoordeling |
|---|---|---|---|
| Kernvelden id/ref/date/price/currency/price_freq/type/new_build/town/province/country/location_detail/location/beds/baths/surface_area/energy_rating/url/desc/features/images | aanwezig | aanwezig | Conform |
| `postcode` per object | aanwezig | ontbreekt in importspec/XSD; wél in exportspec | BP-generator volgt (deels) het exportformaat of een eigen uitbreiding; hoe Kyero een onbekend element behandelt is ONBEKEND |
| `pool` | ontbreekt (0 van 225 op 30-08-2026) | spectekst "Mandatory", XSD optioneel | BP-feed voldoet niet aan de tekst; onze API filtert op `pool` maar dat veld is altijd leeg |
| `catastral` | niet waargenomen in de parser | optioneel | Navragen bij BP of hun export dit veld kan vullen (kadastrale koppeling) |
| Status/verwijdering/prijshistorie | afwezig | afwezig (per ontwerp) | Volledige momentopname; zes exports (export_id 26, 27, 29, 30, 31, 32) overlappen → dedupliceren op `id`/`ref` |
| Verversing | lokale cron elk uur (`server.js`, node-cron `0 * * * *`) | Kyero leest 1×/dag 01:30 CET | De feed van BP zelf kan vaker of minder vaak veranderen dan wij ophalen — actualiteit is ONBEKEND tot BP dit bevestigt |

### 3.5 Gebruiksvoorwaarden en robots.txt
- **Voorwaarden** (pagina 403; zoekmachinesnippet, bewijstype 7/[te verifiëren]): Kyero verbiedt het benaderen, controleren of kopiëren van informatie "by using any type of robot, spider, scraper, or other automated method or through any manual process without express written consent"; verbiedt om "systematically extract and/or re-utilize any Kyero.com content without prior written consent, including but not limited to using any data harvesting bots, scrapers or spiders"; verbiedt het schenden van "robot exclusion notices" en het omzeilen van toegangsbeperkingen; bij overtreding kan Kyero listings verwijderen/blokkeren en is de gebruiker aansprakelijk.
- **robots.txt** (bewijstype 3, 14-09-2026): `User-agent: * / Crawl-delay: 1`; `Disallow: /*api/*`, `/*advice/api/*`, vrijwel alle filterparameters (`min_price`, `max_price`, `beds`, `sort`, `days_since_created`, `agent_id`, `reference_no`, `location_id`), galerijen, plattegronden en contactpagina's. Sitemap: https://www.kyero.com/sitemap/root.xml. Gevolgtrekking (4): de site kent intern een parameter `days_since_created` en een `/api/`-pad, maar beide zijn voor robots afgesloten; dat is geen bewijs van een openbare API.
- Er bestaan meerdere **commerciële scrapers** (Apify) voor Kyero; dit zijn geen geautoriseerde databronnen (masterprompt sectie 6) → NIET GEBRUIKEN.

### 3.6 Alerts, adverteren en data
- **E-mailalert** (help.kyero.com/how-do-i-set-up-an-email-alert-for-new-properties, bewijstype 2): "Click Create property alert to save the search and schedule a regular email update"; "By default, you'll receive an email update once a day, but you can change that to never, every three days or once a week." Alleen nieuwe objecten; prijsdalingen niet genoemd.
- **Adverteren:** gratis onbeperkt plaatsen + betaald "Prime" per listing (prijzen alleen bij derde partij Luxinmo gezien: 6/4/3 € per listing per maand bij 25/50/100 listings — bewijstype 7, [te verifiëren]). Prime: "access to more detailed market & performance analyses" — alleen over het eigen aanbod.
- **Marktdata:** https://www.kyero.com/en/data en /en/join/spain/market-insight bestaan (zoekresultaten), 403 bij ophalen; snippet: "instant access to data, research and statistics on the property market in Spain", "checks government and market data sources daily". Granulariteit, prijs en licentie ONBEKEND.
- **Jávea:** https://www.kyero.com/en/javea-property-for-sale-0l1895 (403). Snippets: ±1.717 objecten te koop, 1.595 villa's, 527 appartementen, 81 town houses, 1.271 boven 1 mln — de deeltellingen zijn samen groter dan het totaal, dus verouderd of overlappend (bewijstype 7). Niet meetbaar.

---

## 4. thinkSPAIN

- **Eigenaar (2):** https://www.thinkspain.com/legal-info — "Think Web Content SL, Tax ID B02283380, C/ Thomas Alva Edison 7, 46980 Paterna (Valencia)". Opgericht 2003; 12 talen (about-us).
- **Omvang (1):** "2,000+ clients listing some 250,000 properties for sale and to rent throughout Spain"; "over 50,000 enquiries every month".
- **Publicatie-import (1):** "We accept data feeds from a large number of property software companies and property portals"; Client Control Panel; "free XML feeds export service". Prijzen: vanaf 25 €/maand (jaarabonnement); introductie 90 dagen 118 € (25 objecten + 1 featured) tot 625 € (500 objecten + 25 featured). Een openbare importspecificatie van thinkSPAIN zelf is **niet gevonden**; ReSales Online noemt thinkSPAIN als voorbeeld van een niet-incrementele (absolute) feed (snippet, 7). Property Hive biedt een "thinkSPAIN Export"-add-on; of thinkSPAIN het Kyero-formaat rechtstreeks accepteert is door thinkSPAIN niet bevestigd [te verifiëren].
- **Lees-API/dataproduct:** geen. "Google-type Analytics for Property" is alleen voor adverteerders over eigen advertenties.
- **Voorwaarden (2):** "The texts, images, sounds, animations, software and all other content included on this website are the exclusive property of Think Web Content SL or its licensors"; transmissie/reproductie/opslag vereist "express written consent". Snippet uit dezelfde pagina: kopiëren toegestaan "except for your own personal or non-commercial use". Geen expliciete robots-/scrapingclausule aangetroffen (3).
- **robots.txt (3):** algemene crawl toegestaan; specifieke bots geweerd (Seekport, TurnitinBot, MauiBot, MJ12bot, AhrefsBot); `Disallow: */alert/count*`, `*/saved/list*`; sitemaps incl. `latest-properties.xml` en `all-properties.xml` (openbaar, maar robots.txt is geen licentie — masterprompt 7).
- **Alerts (3, pagina 14-09-2026):** "Create Alert" en "Save Search"; filter "Price Reduced in last 30 days" onder "Other Search Options". Dit is het enige onderzochte portaal met een expliciete prijsdalingsfilter in de zoekinterface.
- **Jávea (3, 14-09-2026):** https://www.thinkspain.com/property-for-sale/javea → "2,607 found"; bouwkavels https://www.thinkspain.com/property-for-sale/javea/building-plots → "151 found" (prijzen op de pagina 195.000–1.195.000 €). Zoekmachinesnippets toonden eerder 2.720 resp. 310 (verouderd).
- **Uniek aanbod:** internationaal georiënteerd (talen, buitenlandse kopers), maar het aanbod komt via CRM-feeds van makelaars → vermoedelijk grotendeels dezelfde voorraad als elders (4). Bewijs van unieke objecten: geen.

---

## 5. pisos.com

- **Eigenaar (2):** HabitatSoft-aviso legal (https://www.habitatsoft.com/legal-notice?culture=es-ES) noemt "HabitatSoft, S.L., CIF B61562088, C/ Roger de Lluria, 50 P-1, 08009 Barcelona" als verantwoordelijke voor o.a. www.pisos.com, www.pisos.cat, www.pisocompartido.com. Verkoop: Servimedia 18-03-2025 — verkoper Desarrollo de Clasificados, S.L.U. (100% Vocento), verkocht 100% van Habitat Soft S.L. aan Immobiliare.it voor 22,5 mln € contant, gemeld aan de CNMV, geschatte boekwinst ±18 mln €. Online Marketplaces 08-04-2025: Immobiliare.it koppelde de listingpakketten van pisos.com en indomio.es ("both portal's services could now be contracted together"). indomio.com noemt Pisos.com, Indomio.es en Enalquiler.com als de Spaanse portalen van de groep (1). Wikipedia (es) is verouderd (noemt nog Vocento).
- **Site (3):** WebFetch kon www.pisos.com niet ophalen; robots.txt wél: `Disallow: /*.aspx`, `/WS/`, `/mapa/`, `/PriceDrop/`, `/Grid/GetAdsense`, `/en/`, `/ca/`, `/de/`, `/fr/`, `/alquiler-temporada/`; expliciete blokkade van downloaders (HTTrack, WebCopier, Teleport, WebZIP, libwww e.a.). Gevolgtrekking (4): er is een prijsdalingsfunctie (`/PriceDrop/`), maar die is voor robots afgesloten.
- **Publicatie-import:** geen openbare specificatie gevonden. Derden (Inmogesco, terrenos.es) noemen betaalde publicatiepakketten en producten als "informes de oferta y demanda, prospección inmobiliaria, valoración online" (7). Of de Indomio-feed-API ook naar pisos.com publiceert, staat niet in feed.indomio.com (de welkomstpagina noemt pisos.com niet) → ONBEKEND.
- **Lees-API/dataproduct:** geen gevonden. pisos.com publiceert maandelijkse prijsrapporten via persberichten (Inmonews-snippet noemt "Ferran Font, director de Estudios de pisos.com") — geen dataproduct voor derden aangetroffen.
- **Voorwaarden (2, HabitatSoft):** "Los contenidos, elementos e información … están sujetos a derechos de propiedad industrial e intelectual"; "El Usuario se compromete a utilizar los contenidos … para su propio uso y necesidades, y a no realizar en ningún caso una explotación comercial, directa o indirecta de los mismos." Geen expliciete robots-/scrapingclausule in dat document. De eigen aviso legal van pisos.com na de overname is niet gelezen → [te verifiëren].
- **Alerts:** niet controleerbaar (geblokkeerd). Derde-partijdiensten (FlatRadar, Piso:Alerta) claimen compatibiliteit; dit zijn geen geautoriseerde bronnen.
- **Jávea:** niet meetbaar (site geblokkeerd; `site:pisos.com`-zoekopdracht gaf geen resultaten).

---

## 6. yaencontre

- **Eigenaar:** idealista/news 13-02-2020 (2): idealista nam een niet-bekendgemaakte "inversión relevante" in YaEncontré (destijds Grupo Godó); "Tanto idealista como YaEncontré continuarán trabajando de manera autónoma…". EjePrime (403; snippet): "Idealista completa la absorción del portal inmobiliario Yaencontré" (entiteit "Yaencontre-Jahetrobat", volgens Registro Mercantil; idealista is eigendom van EQT/Cinven volgens de snippets) — datum en huidige rechtsvorm [te verifiëren]. Het idealista/news-onderdeel "yaencontre" (quienes-somos) geeft geen bedrijfsinformatie.
- **Site (3):** WebFetch 403; `curl` op robots.txt gaf 403 met een DataDome-pagina ("Please enable JS and disable any ad blocker") — de site weert elke niet-browsertoegang.
- **Publicatie-import / lees-API:** professionalspagina (https://www.yaencontre.com/inmobiliarias/nuevo-profesional) niet leesbaar; geen documentatie gevonden → ONBEKEND.
- **Alerts (snippets van het helpcentrum, 7/[te verifiëren]):** "Alertas de búsqueda" per e-mail bij nieuwe advertenties; "Alertas de bajada de precio" ("si activas esta alerta y el precio del inmueble que te gusta baja, te avisamos"); alerts bij wijzigingen (prijs, foto's) in bewaarde advertenties. URL's: https://www.yaencontre.com/ayuda/gestion-de-alertas-y-comunicaciones/que-es-una-alerta, https://www.yaencontre.com/noticias/vivienda/crear-una-alerta-en-yaencontre.
- **Voorwaarden:** niet leesbaar → ONBEKEND. Gezien de DataDome-blokkade is geautomatiseerde toegang in elk geval technisch niet gewenst (4).
- **Jávea (snippets, datum onbekend, 7):** 1.755 casas (https://www.yaencontre.com/venta/casas/javea-xabia), 742 pisos y viviendas (/venta/pisos/javea-xabia), 413 terrenos (/venta/terrenos/javea-xabia). Niet meetbaar via WebFetch.
- **Uniek aanbod:** Spaans publiek, Catalaanse oorsprong; door de idealista-band mogelijk (deels) gedeelde voorraad — niet aangetoond (7).

---

## 7. SpainHouses

- **Eigenaar (2):** https://www.spainhouses.net/en/legal-information.html — "Entersoftweb, S.L., CIF B92308949, Plaza de la Solidaridad, 12 - 5ª Planta - 29006 Málaga". De eigenaar levert ook een "Real Estate Solution (CRM + Web)".
- **Omvang (1):** "More than 3,300 real estate" agencies in de professionalsgids. Totaal aantal objecten: niet vermeld.
- **Publicatie-import (2):** https://www.spainhouses.net/es/inmobiliarias/especificaciones-publicacion.html — **eigen XML-formaat**, XSD `https://xcp.entersoftweb.com/sh/xsd/cartera.xsd`. Verplicht: `referencia`, `fecha` (`aaaa-mm-ddThh:mm:ss`, laatste wijziging of invoegdatum), `tipoInmueble`, `tipoOferta`, `precio`, `provincia`, `localidad`, `geoLocalizacion`, `direccion`, `descripcionPrincipal`. Verwijdering via ontbreken van de `referencia` (zelfde snapshotlogica als Kyero). Onbeperkt aantal foto's. Leesfrequentie niet vermeld. "Automatic Publication" vanuit 32+ CRM's (Inmoenter, HabitatSoft, inmofactory, idealista, NetFincas, inmoweb, eGO …). Plannen "starting at 10.00 €/month".
- **Distributie:** aanbod wordt doorgeplaatst naar Mundocasas, Worldhouses, nuroa, mitula, trovit, venderya.es (1). Widgets voor de eigen site.
- **Lees-API/dataproduct:** geen.
- **Voorwaarden (3):** de pagina "legal information" is een privacybeleid; géén IP-, database- of scrapingclausule aangetroffen. robots.txt: `OrangeBot` geweerd; veel oude paden uitgesloten; geen crawl-delay.
- **Alerts (3, pagina 14-09-2026):** "Receive new listings in your email", "Save search", en in het privacybeleid "tus alertas de precios". Filters: **"To reform"** (State) en **"Reduced"** (Opportunities) — beide direct relevant voor renovatiesignalen en prijsverlagingen.
- **Jávea (3, 14-09-2026):** https://www.spainhouses.net/en/sale-houses-javea-alicante.html → 322 huizen; totaal "488 homes" in Jávea; ±27 per pagina.
- **Uniek aanbod:** richt zich op eigenaren én professionals; een deel particulier aanbod is denkbaar maar niet gemeten (7).

---

## 8. Green-Acres

- **Eigenaar (2):** voorwaarden https://www.green-acres.fr/en/terms-of-use en https://www.green-acres.es/en/terms-of-use (versie 1.1, 06-04-2021): "GREEN-ACRES S.A.S, 100 boulevard du Montparnasse, 75014 Paris", RCS Paris 453 785 156, btw FR56453785156, kapitaal 1.000.000 €. Handelsregister-aggregator societe.com: voorheen "REALIST", naamswijziging 26-04-2024 (2, secundair). Directeur publicatie: de president van Green-Acres S.A.S. (snippet). green-acres.com/en/legal-notice → redirect naar 404.
- **Omvang (1):** green-acres.es toont "51,375 houses and apartments" te koop in Spanje (14-09-2026); registratiepagina: "10 million prospects worldwide", "20,000 agents and representatives already use Green acres", "70% some visitors are foreign". Snippet: 400.000 objecten in 22 landen (7).
- **Publicatie-import (2):** https://www.green-acres.es/en/GatewayInfo — eigen XML (`<Envelope><Body><add_adverts><advert>`), verplicht o.a. `account_id`, `reference`, `advert_type`, `price`, `has_included_fees`, `agency_rates_type`, `agency_rates`, `fees`, `currency`, `city`, `country_code`, `postal_code`, `property_type`, plus lat/long; tot 60 foto's (`<pic order='X'>`, optioneel `last_update`); **"cancel and replace mode: All the listings not present in the feed will automatically be deleted"**; bestand wordt "daily" via HTTP opgehaald of via FTP aangeleverd; activering via tab "Transfer" in het agency-account. Registratieformulier noemt 200+ compatibele CRM's; 30 dagen gratis proef. Verdienmodel (pay-per-lead volgens derde partij immoedge) [te verifiëren].
- **Lees-API/dataproduct:** geen. robots.txt kent paden `EstimationActions` (waardering) en `MailAlert` — interne functies, geen API.
- **Voorwaarden (2):** art. 7: "Any representation, reproduction or adaptation of logos, textual, pictographic or video content … is strictly prohibited"; geen expliciete robots-/scraping-/databankclausule.
- **robots.txt (3, 14-09-2026):** `Request-rate: 1/1`, `Crawl-delay: 1`; `Disallow: /` voor AhrefsBot, dotbot, BLEXBot, Pompos, **ClaudeBot**, SemrushBot, Amazonbot, DataForSeoBot, Barkrowler. Consequentie: Green-Acres wil expliciet niet door onze categorie tooling gecrawld worden; de handmatige WebFetch van vandaag valt daar buiten, maar systematisch ophalen is NIET GEBRUIKEN.
- **Alerts (3):** "Save alert" met frequentie "Once a day" / "Once a week"; filter "To renovate" bij type; geen prijsdalingsfilter gezien.
- **Jávea (3, 14-09-2026):** https://www.green-acres.es/property-for-sale/javea-xabia → "Real estate Jávea: 813 properties and houses for sale". Snippets toonden 1.203 / 1.054 / 515 luxe / 188 appartementen / 27 kavels (verouderd of anders geteld, 7).
- **Uniek aanbod:** Europese tweedewoningkopers (FR/UK/BE/NL); makelaars leveren via CRM-feed → grotendeels gedeelde voorraad (4).

---

## 9. Indomio (indomio.es)

- **Eigenaar:** zoekmachinesnippet van https://www.indomio.es/en/terms/ (pagina 403; 7/[te verifiëren]): "Indomio (indomio.es) is the property of Immobiliare.it S.p.A., with registered office in Via Carlo Farini 41, 20159 Milan"; het Spaanse beheer is toegewezen aan "Indomio with registered office in c/ Roger de Lluria 50, 08009 Barcelona" — hetzelfde adres als HabitatSoft (pisos.com). indomio.com (1): groep met Immobiliare.it, Trovacasa, MioAffitto (IT), Pisos.com, Indomio.es, Enalquiler.com (ES), Spitogatos e.a. (GR), Nepremicnine.net (SI), Crozilla (HR), Nekretnine.rs (RS), Immotop.lu (LU), LuxuryEstate.com; "9 offices in 6 countries". Moederbedrijf "Real Web" volgens Online Marketplaces (7).
- **Publicatie-API (2, https://feed.indomio.com/docs/ies/):** "Indomio data exchange's API" — REST-push, "publish your data using our almost real time APIs"; "send listing updates at any time and without limits (even for the same listing several times a day)". Authenticatie: HTTP BASIC met door Support verstrekt account, opgave van publieke IP's, header `X-IMMO-SOURCE`; proefperiode met testagentschap. XML-payload: één `<property>` per REST-call (batch `<feed><properties>` is deprecated); `@operation` = `write` of `archive`; `<publish>` true/false regelt zichtbaarheid; `date-updated` (ISO 8601) "must always be updated after each change to the listing" — "otherwise we do not take care of the changes"; "the absence of an element or attribute in a feed is interpreted to mean that the relevant information is to be removed"; prijs met `@currency` (EUR) en `@reserved`; XSD `https://feed.indomio.es/ws/import/docs/import-schema`; Swagger `https://feed.indomio.es/ws/import/docs/swagger-ui.html`. Objecttypen: residential, business, terrain, construction sites; de kennisbank heeft ook een onderdeel "Auctions catalog" (alleen als titel gezien — inhoud niet onderzocht, relevantie voor veilingstroom ONBEKEND).
- **Feedback-API's (2):** `out/leads`, `out/phones`, `out/backlinks`, audience — uitsluitend over de eigen advertenties. Geen leesfeed van andermans aanbod.
- **Dataproduct:** Immobiliare.it "Insights" (snippet: "supply, demand, and transaction data"; pagina 403) is een Italiaans product; dekking van Spanje/indomio.es niet aangetoond (7). indomio.es heeft een pagina "Mercado inmobiliario en Jávea - Xàbia" (https://www.indomio.es/en/mercado-inmobiliario/comunitat-valenciana/javea-xabia/) — 403.
- **Voorwaarden:** niet leesbaar → ONBEKEND. robots.txt (3): `Disallow: /search-map`, `/search-list`, `/ricerca.php`, `/dettaglio.php`, `*?lang=` e.a.
- **Alerts:** niet controleerbaar.
- **Jávea (snippet, 7):** "1,994 listings of homes for sale in Jávea - Xàbia starting from 192,315 euros" (https://www.indomio.es/en/venta-casas/javea-xabia/). Niet meetbaar via WebFetch.
- **Uniek aanbod:** door de pakketkoppeling met pisos.com waarschijnlijk grotendeels dezelfde adverteerders als pisos.com (4); geen bewijs van uniek aanbod.

---

## 10. Uniek aanbod: internationaal versus Spaans (analyse, bewijstype 4)

| Groep | Portalen | Kanaal waarlangs aanbod binnenkomt | Verwachting uniekheid | Bewijs |
|---|---|---|---|---|
| Internationaal | Kyero, thinkSPAIN, Green-Acres, (Indomio-groep gedeeltelijk) | CRM-/XML-feeds van makelaars; Kyero fungeert zelf als distributiehub (exportfeed) | Laag: dezelfde makelaarsvoorraad die ook bij BP/idealista staat, mogelijk met andere presentatie en Engelstalige teksten | Geen; alleen aantallen. thinkSPAIN 2.607 vs. BP 56 in Jávea zegt iets over **onze** dekking, niet over uniekheid |
| Spaans | pisos.com, yaencontre, SpainHouses | CRM-feeds + particulieren (pisos.com: 2 gratis advertenties voor particulieren volgens derde partij; SpainHouses richt zich ook op eigenaren) | Mogelijk beperkt particulier aanbod dat niet in makelaarsfeeds zit | Niet gemeten |

Conclusie: uniekheid is voor geen enkel portaal aangetoond. De enige rechtmatige manier om dat te meten is handmatig (of via toegestane alerts) een steekproef van Jávea-objecten te vergelijken op referentie/locatie/foto — met inachtneming van de voorwaarden (geen systematische extractie).

## 11. Partnerprogramma's en dataservices voor investeerders/makelaars

| Portaal | Gevonden | Aard | Status |
|---|---|---|---|
| Kyero | kyero.com/en/data, market-insight (Spanje) | Marktstatistieken en vraagtrends van buitenlandse kopers; granulariteit, prijs en licentie onbekend (pagina 403) | TECHNISCH ONDERZOEK NODIG (alleen via browser/Jan) |
| thinkSPAIN | Analytics voor adverteerders | Alleen eigen advertenties | n.v.t. voor lezen |
| pisos.com | Maandelijkse prijsrapporten (pers); derden noemen "informes de oferta y demanda" | Marketing/marktdata, geen ruwe advertentiedata | ONBEKEND |
| Indomio/Immobiliare | "Insights" (Italië) | Vraag/aanbod/transactiedata; Spanje-dekking niet aangetoond | ONBEKEND |
| Green-Acres, SpainHouses, yaencontre | niets | — | — |

Geen van de zeven biedt een licentie op advertentiedata voor investeerders. Wie meer wil, moet dat per portaal schriftelijk aanvragen (CONTRACT OF TOESTEMMING NODIG).

## 12. Indicatieve meting Jávea (samenvatting)

| Portaal | Aantal te koop | Waarvan kavels | Meetmethode | Bewijstype |
|---|---|---|---|---|
| thinkSPAIN | 2.607 | 151 | pagina, 14-09-2026 | 3 |
| Green-Acres | 813 | 27 (snippet) | pagina, 14-09-2026 | 3 (kavels 7) |
| SpainHouses | 488 woningen (322 huizen) | onbekend | pagina, 14-09-2026 | 3 |
| Kyero | ±1.717 | onbekend | snippet, datum onbekend | 7 |
| Indomio | ±1.994 | onbekend | snippet | 7 |
| yaencontre | ±1.755 casas + 742 pisos | 413 terrenos | snippet | 7 |
| pisos.com | niet meetbaar | — | geblokkeerd | 7 |
| Background Properties (referentie) | 56 (25-08-2026) | onbekend | eigen API | 3 |

## 13. Consequenties voor het ontwerp van Deal Hunter (bewijstype 4)

1. **Kyero v3 is het formaat om te ondersteunen** — het is de BP-feed en wordt door veel CRM's als export geleverd. Elke extra makelaar die ons "een Kyero-feed" wil geven, past in dezelfde adapter. Bouw de adapter tolerant: accepteer `postcode` op objectniveau, ontbrekende `pool`, en behandel `'0'` in `pool`/`beds`/`baths` als ONBEKEND, niet als nul.
2. **Wijzigingsdetectie moet snapshot-gebaseerd zijn**: NIEUW DOOR ONS ONTDEKT (id/ref nieuw), PRIJS GEWIJZIGD (price-verschil), OPNIEUW AANGEBODEN (id terug na afwezigheid), NIET MEER GEVONDEN (afwezig in een **geslaagde** volledige download). Bij een mislukte of lege download: BRON NIET BEREIKBAAR en geen statuswijzigingen (14-09-2026 is het praktijkvoorbeeld).
3. **Publicatiedatum bestaat niet** in Kyero v3, SpainHouses-XML, Green-Acres-XML of de Indomio-payload; alleen "laatst gewijzigd". `first_seen_at` is dus onze eigen nulmeting; "dagen te koop" is pas na weken opbouw betrouwbaar.
4. **Lezen van de zeven portalen kan alleen handmatig of via hun eigen e-mailalerts.** Of automatisch verwerken van alertmails is toegestaan, is nergens geregeld; dat is een open juridische vraag (masterprompt 6: "toegestane verwerking van zoekmeldingen"). Tot die vraag beantwoord is: alerts naar een aparte mailbox laten lopen en door een mens laten beoordelen.
5. **thinkSPAIN en SpainHouses** zijn de meest bruikbare handmatige signaalbronnen voor renovatie- en prijsdalingskandidaten (filters "Price Reduced in last 30 days", "To reform", "Reduced", "To renovate" bij Green-Acres).

---

## 14. Registerregels (masterprompt sectie 7)

| Naam | Website | Type | Dekking | Technische toegang | Velden/foto's | Publicatie-/wijzigingsinfo | Historie | Verversing | Rate limits | Kosten | Contract | Toegestane doelen | AI/afgeleide data | Aanvraagroute | Laatste verificatie | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kyero (Portal47 Ltd / idealista) | https://www.kyero.com | Internationaal portaal + feedstandaard | ES/PT/FR/IT | Lezen: geen. Publiceren: v3-importfeed; eigen exportfeed | v3-velden (sectie 3.2); max 50 foto's | `date` = laatst gewijzigd; geen status | Geen | Kyero leest 1×/dag 01:30 CET (Prime), wekelijks (Free) | robots Crawl-delay 1 | Gratis + Prime per listing [te verifiëren] | Geen | Eigen advertenties publiceren; alerts als bezoeker | Verboden zonder schriftelijke toestemming | help.kyero.com; adverteerdersaccount | 14-09-2026 | Lezen: **ALLEEN HANDMATIG**; geautomatiseerd: **NIET GEBRUIKEN**; publiceren: **CONTRACT OF TOESTEMMING NODIG** |
| thinkSPAIN (Think Web Content SL) | https://www.thinkspain.com | Internationaal portaal | Heel Spanje | Lezen: geen. Publiceren: XML-feeds (formaat niet openbaar) | Onbekend | Filter "Price Reduced in last 30 days" | Geen | Onbekend | Geen algemene beperking in robots | Vanaf 25 €/mnd (adverteren) | Geen | Alerts als bezoeker; reproductie verboden | Onbekend | client.thinkspain.com / advertise | 14-09-2026 | **ALLEEN HANDMATIG**; publiceren: CONTRACT OF TOESTEMMING NODIG |
| pisos.com (Habitat.Soft S.L. / Immobiliare.it) | https://www.pisos.com | Spaans portaal | Heel Spanje | Onbekend (site geblokkeerd) | Onbekend | `/PriceDrop/` bestaat | Onbekend | Onbekend | Onbekend | Betaald voor professionals | Geen | Geen commerciële exploitatie (HabitatSoft) | Onbekend | Via Indomio/pisos.com professionals | 14-09-2026 | **TECHNISCH ONDERZOEK NODIG** → voorlopig ALLEEN HANDMATIG |
| yaencontre (idealista-groep) | https://www.yaencontre.com | Spaans portaal | Heel Spanje | Geen; DataDome-blokkade | Onbekend | Alerts: nieuw, prijsdaling, wijziging | Onbekend | Onbekend | Anti-bot | Onbekend | Geen | Alerts als bezoeker | Onbekend | Onbekend | 14-09-2026 | **ALLEEN HANDMATIG**; geautomatiseerd NIET GEBRUIKEN |
| SpainHouses (Entersoftweb S.L.) | https://www.spainhouses.net | Spaans/meertalig portaal | Heel Spanje | Lezen: geen. Publiceren: eigen XML (cartera.xsd) | Eigen velden; foto's onbeperkt | `fecha` = wijziging/invoer; filters "To reform", "Reduced" | Geen | Onbekend | Geen | Vanaf 10 €/mnd | Geen | Alerts als bezoeker | Onbekend | administracion@entersoftweb.com, 952 020 401 | 14-09-2026 | **ALLEEN HANDMATIG**; publiceren: CONTRACT OF TOESTEMMING NODIG |
| Green-Acres (Green-Acres S.A.S.) | https://www.green-acres.es | Internationaal portaal | 22 landen; ES 51.375 | Lezen: geen. Publiceren: XML Gateway, cancel-and-replace | Eigen velden; 60 foto's | Geen status; dagelijkse import | Geen | Dagelijks (import) | robots Request-rate 1/1; ClaudeBot geweerd | 30 dagen gratis; daarna [te verifiëren] | Geen | Alerts als bezoeker; reproductie verboden | Onbekend | Register/Agency | 14-09-2026 | **ALLEEN HANDMATIG**; geautomatiseerd **NIET GEBRUIKEN** |
| Indomio (Immobiliare.it S.p.A.) | https://www.indomio.es | Zuid-Europees portaal | Spanje (+ groep) | Lezen: geen. Publiceren: REST-push-API (BASIC auth, IP-whitelist) | XML-payload; `date-updated`; `@operation` archive | Geen publicatiedatum | Geen | "almost real time", geen limiet | Geen vermeld | Onbekend | Geen | Eigen advertenties | Onbekend | Support (feed.indomio.com) | 14-09-2026 | **ALLEEN HANDMATIG**; publiceren: CONTRACT OF TOESTEMMING NODIG |

---

## 15. Open vragen

1. **Voor Jan (via browser, niet geautomatiseerd):** de voorwaarden van kyero.com (/en/docs/terms/, versie 20-04-2026), indomio.es (/en/terms/) en pisos.com lezen en de scraping-/databankclausules bevestigen; de Kyero-datapagina (/en/data) beoordelen op granulariteit (is er Alicante/Jávea-niveau?) en prijs.
2. Aan **Background Properties** vragen: welke generator maakt hun Kyero-feed (WordPress-export), waarom `postcode` op objectniveau en geen `pool`, of `catastral` gevuld kan worden, hoe vaak de export ververst, en of ons gebruik (analyse, deduplicatie, beeldvergelijking) binnen hun afspraak valt.
3. Is geautomatiseerde verwerking van **e-mailalerts** van deze portalen toegestaan? Geen portaal spreekt zich uit; juridisch advies nodig vóór automatisering.
4. Accepteert **thinkSPAIN** het Kyero v3-formaat rechtstreeks (relevant als TREE Properties daar wil adverteren)?
5. Publiceert de **Indomio-feed-API** ook naar pisos.com sinds de pakketkoppeling van april 2025? Wat bevat het onderdeel "Auctions catalog" in de Indomio-kennisbank?
6. Huidige juridische status van **yaencontre** (zelfstandige vennootschap of opgegaan in idealista) en of het aanbod met idealista gedeeld wordt.
7. Dekt **Immobiliare Insights** Spanje?
8. Discrepantie V3.8/V3.9 bij Kyero — welk nummer geldt (irrelevant voor de velden, relevant voor documentatieverwijzingen).

## 16. Geblokkeerd of mislukt (niet omzeild)

| URL | Resultaat | Alternatief gebruikt |
|---|---|---|
| https://www.kyero.com/en/terms, /en/docs/terms/, /en/data, /data/en/data/spain, /en/aboutus, /join// | HTTP 403 | help.kyero.com, feeds.kyero.com (200), idealista/news, zoekmachinesnippets |
| https://www.kyero.com/en/javea-property-for-sale-0l1895 | niet opgehaald (host 403) | snippet |
| https://www.pisos.com/aviso-legal/ en overige pisos.com-pagina's | "unable to fetch" | habitatsoft.com legal notice, Servimedia, Online Marketplaces, robots.txt (200) |
| https://www.yaencontre.com/* (aviso-legal, nuevo-profesional, ayuda) | HTTP 403; robots.txt 403 met DataDome | idealista/news 13-02-2020, snippets helpcentrum |
| https://www.indomio.es/terminos-y-condiciones/, /en/terms/ | HTTP 403 | feed.indomio.com (200), indomio.com (200), snippet |
| https://www.green-acres.com/en/legal-notice | 301 → green-acres.fr/en/error 404 | green-acres.fr en .es /en/terms-of-use (200) |
| https://www.thinkspain.com/terms-and-conditions, /terms | HTTP 404 | /legal-info (200) |
| https://www.spainhouses.net/en/legal-notice.html | HTTP 404 | /en/legal-information.html (200) |
| https://www.immobiliare.it/en/info/report-professionali/ | HTTP 403 | snippet |
| https://www.eleconomista.es/… (Vocento-verkoop) | HTTP 403 | Servimedia (200) |
| https://www.ejeprime.com/… (yaencontre-absorptie) | HTTP 403 | snippet |
| Kyero v3-pdf (api.estatesit.uk) | binaire pdf niet leesbaar; lokale pdf-renderer ontbreekt | officiële spec.txt + XSD (200) |
| help.kyero.com/ (index) | wel bereikbaar, maar toont alleen secties | directe artikel-URL's |

---

## 17. Bronnenlijst (URL · controledatum · bewijstype)

**Kyero**
- https://help.kyero.com/estate-agents/xml-import-specification · 14-09-2026 · 2
- https://feeds.kyero.com/assets/kyero_v3_import_spec.txt · 14-09-2026 · 3 (ruw opgehaald)
- https://feeds.kyero.com/assets/kyeroV3.0.xsd · 14-09-2026 · 3
- https://feeds.kyero.com/assets/kyero_v3_test_feed.xml · 14-09-2026 · 3
- https://feeds.kyero.com/validator/ · 14-09-2026 · 2
- https://help.kyero.com/xml-export-specification · 14-09-2026 · 2
- https://feeds.kyero.com/assets/kyero_v3_export_spec.txt · 14-09-2026 · 2
- https://help.kyero.com/estate-agents/kyero-xml-feed · 14-09-2026 · 2
- https://help.kyero.com/how-often-my-xml-feed-is-updated · 14-09-2026 · 2
- https://help.kyero.com/how-can-i-check-if-my-xml-feed-is-working-fine · 14-09-2026 · 2
- https://help.kyero.com/what-are-the-prime-package-features · 14-09-2026 · 1
- https://help.kyero.com/how-do-i-set-up-an-email-alert-for-new-properties · 14-09-2026 · 2
- https://help.kyero.com/visitors · 14-09-2026 · 2
- https://www.kyero.com/en/docs/terms/ · 14-09-2026 · 7 (403; alleen zoekmachinesnippet)
- https://www.kyero.com/robots.txt · 14-09-2026 · 3
- https://www.idealista.com/en/news/property-for-sale-in-spain/2024/12/05/821343-idealista-acquires-kyero · 14-09-2026 · 2
- https://www.kyero.com/en/data en https://www.kyero.com/en/join/spain/market-insight · 14-09-2026 · 7 (403; snippet)
- https://www.luxinmo.com/portals/kyero (Prime-prijzen) · 14-09-2026 · 7 (derde partij)

**thinkSPAIN**
- https://www.thinkspain.com/legal-info · 14-09-2026 · 2
- https://www.thinkspain.com/about-us · 14-09-2026 · 1
- https://www.thinkspain.com/advertise/property-agent · 14-09-2026 · 1
- https://www.thinkspain.com/property-for-sale/javea · 14-09-2026 · 3
- https://www.thinkspain.com/property-for-sale/javea/building-plots · 14-09-2026 · 3
- https://www.thinkspain.com/robots.txt · 14-09-2026 · 3
- https://wp-property-hive.com/addons/thinkspain-export/ · 14-09-2026 · 7 (derde partij)

**pisos.com**
- https://www.habitatsoft.com/legal-notice?culture=es-ES · 14-09-2026 · 2
- https://www.servimedia.es/noticias/vocento-vende-habitat-soft-inmobiliarieit-22-5-millones-euros/1411519299 · 14-09-2026 · 2 (nieuws over CNMV-melding)
- https://dircomfidencial.com/medios/vocento-vende-pisos-com-y-habitatsoft-al-grupo-italiano-immobiliare-it-por-225-m-20250318-1718/ · 14-09-2026 · 7 (403)
- https://www.onlinemarketplaces.com/articles/immobiliare-it-links-listings-packages-for-spanish-portals-pisos-com-and-indomio-es/ · 14-09-2026 · 2 (vakpers)
- https://es.wikipedia.org/wiki/Pisos.com · 14-09-2026 · 7 (verouderd)
- https://www.pisos.com/robots.txt · 14-09-2026 · 3
- https://inmogesco.com/blog/pisos-com/ en https://terrenos.es/en/portals/pisos-com · 14-09-2026 · 7 (derde partij)

**yaencontre**
- https://www.idealista.com/news/inmobiliario/blog-de-idealista/2020/02/13/779990-idealista-invierte-en-yaencontre · 14-09-2026 · 2
- https://www.1001portales.com/blog/idealista-invierte-en-el-portal-inmobiliario-yaencontre/ · 14-09-2026 · 7 (derde partij)
- https://www.ejeprime.com/empresa/idealista-completa-la-absorcion-del-portal-inmobiliario-yaencontre · 14-09-2026 · 7 (403; snippet)
- https://www.yaencontre.com/ayuda/gestion-de-alertas-y-comunicaciones/que-es-una-alerta · 14-09-2026 · 7 (403; snippet)
- https://www.yaencontre.com/venta/casas/javea-xabia, /venta/pisos/javea-xabia, /venta/terrenos/javea-xabia · 14-09-2026 · 7 (snippets)
- https://www.yaencontre.com/robots.txt · 14-09-2026 · 3 (403 DataDome)

**SpainHouses**
- https://www.spainhouses.net/en/legal-information.html · 14-09-2026 · 2
- https://www.spainhouses.net/es/inmobiliarias/especificaciones-publicacion.html · 14-09-2026 · 2
- https://www.spainhouses.net/en/real-estates/information.html · 14-09-2026 · 1
- https://www.spainhouses.net/en/ · 14-09-2026 · 1
- https://www.spainhouses.net/en/sale-houses-javea-alicante.html · 14-09-2026 · 3
- https://www.spainhouses.net/robots.txt · 14-09-2026 · 3

**Green-Acres**
- https://www.green-acres.fr/en/terms-of-use · 14-09-2026 · 2
- https://www.green-acres.es/en/terms-of-use · 14-09-2026 · 2
- https://www.green-acres.es/en/GatewayInfo · 14-09-2026 · 2
- https://www.green-acres.fr/en/Register/Agency · 14-09-2026 · 1
- https://www.green-acres.es/en/ · 14-09-2026 · 1
- https://www.green-acres.es/property-for-sale/javea-xabia · 14-09-2026 · 3
- https://www.green-acres.es/robots.txt · 14-09-2026 · 3
- https://www.societe.com/societe/green-acres-453785156.html · 14-09-2026 · 2 (registeraggregator, secundair)

**Indomio**
- https://feed.indomio.com/ · 14-09-2026 · 2
- https://feed.indomio.com/docs/ies/ · 14-09-2026 · 2
- https://feed.indomio.com/docs/ies/in/introduction-specifications · 14-09-2026 · 2
- https://feed.indomio.com/docs/ies/in/get-start · 14-09-2026 · 2
- https://feed.indomio.com/docs/ies/in/payload-specifications · 14-09-2026 · 2
- https://feed.indomio.com/docs/ies/in/faq · 14-09-2026 · 2
- https://feed.indomio.com/docs/iit/ · 14-09-2026 · 2
- https://www.indomio.com/ · 14-09-2026 · 1
- https://www.indomio.es/en/terms/ · 14-09-2026 · 7 (403; snippet)
- https://www.indomio.es/en/venta-casas/javea-xabia/ · 14-09-2026 · 7 (snippet)
- https://www.indomio.es/robots.txt · 14-09-2026 · 3
- https://www.immobiliare.it/en/info/report-professionali/ · 14-09-2026 · 7 (403; snippet)

**Lokaal (alleen-lezen, geen sleutels overgenomen)**
- /Users/root-admin/tree-hermes/properties-api/server.js (parservelden, cron `0 * * * *`) · 14-09-2026 · 3
- Lokale feiten uit de opdracht (BP-feedvelden, tellingen 25-08/30-08/14-09-2026) · 3

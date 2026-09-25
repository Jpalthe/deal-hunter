# Javea Estates — toets op automatisch lezen

- **Website:** https://www.javeaestates.com (Engels op `/en/`, ook `/es/` en `/nl/`)
- **Kantoor (volgens de voettekst van de site, 24-09-2026):** Calle Corriol 6 en Calle Thiviers 6, Puerta 11, 03730 Jávea. Algemene kanalen: +34 960 130 339, info@javeaestates.com, WhatsApp +34 683 407 888. Familiebedrijf, "over 25 years in Jávea", geregistreerd als API (Agente de la Propiedad Inmobiliaria). Staat in `K01-kantoren-javea.json`.
- **Datum toets:** 24-09-2026, ca. 23:33–23:35 lokale tijd (server-datumkoppen 21:33–21:35 UTC)
- **Opgehaald (6 verzoeken, telkens ≥ 10 s ertussen):** robots.txt, /sitemap.xml (404), homepage, privacy-link uit de voettekst (404), aanbodpagina `/en/properties`, één objectpagina. Dus 5 HTML-antwoorden (waarvan twee 404-pagina's) plus robots.txt. De zoekmachine-hulp van deze sessie was op, dus alles komt rechtstreeks van de site.
- **Let op bij het lezen:** "API" in het menu van deze site is de Spaanse beroepstitel *Agente de la Propiedad Inmobiliaria*, geen technische koppeling of feed.

## Advies: LEZEN (gemiddelde prioriteit)

Het mag (robots.txt staat de objectpagina's toe voor iedereen), er is geen voorwaardentekst gevonden die het verbiedt (de enige juridische link is stuk), en de pagina's zijn gewone server-gerenderde HTML met prijs, m², perceel en referentie in de tekst. Omvang ca. 260–280 vermeldingen, waarvan op de eerste pagina grofweg de helft in Jávea, Benitachell (Cumbre del Sol) of Moraira ligt. Twee aandachtspunten: 10 seconden tussen verzoeken aanhouden (de site vraagt dat expliciet aan AI-lezers) en dubbele vermeldingen ontdubbelen (zie 6).

## 1. robots.txt — toegestaan, met beperkingen voor AI-lezers

Bron: https://www.javeaestates.com/robots.txt (24-09-2026, HTTP 200). Standaard Joomla-bestand met eigen toevoegingen. Relevante regels, letterlijk:

```
User-agent: *
Disallow: /administrator/
Disallow: /api/
Disallow: /bin/
Disallow: /cache/
Disallow: /cli/
Disallow: /components/
Disallow: /includes/
Disallow: /installation/
Disallow: /language/
Disallow: /layouts/
Disallow: /libraries/
Disallow: /logs/
Disallow: /modules/
Disallow: /plugins/
Disallow: /tmp/
Disallow: /images/Logo/Javea_Estates.png
```

```
User-agent: ClaudeBot
User-agent: Claude-SearchBot
User-agent: OAI-SearchBot
User-agent: ChatGPT-User
User-agent: meta-externalagent
User-agent: facebookexternalhit
Disallow: /index.php?*option=com_osproperty*task=property_pdf*
Disallow: /images/osproperty/properties/
Crawl-delay: 10
```

Verder: `PetalBot`, `barkrowler` en de Amazon-bots zijn helemaal geweerd (`Disallow: /`); `GPTBot`, `SemrushBot`, `Baiduspider`, `Bytespider`, `IbouBot` krijgen `Crawl-delay: 10`, `Applebot` 5. **Geen `Sitemap:`-regel.**

Betekenis: voor `User-agent: *` zijn alleen Joomla-systeemmappen en één logo geblokkeerd; `/en/properties/...` (aanbod en objecten) mag. Voor een lezer die zich als ClaudeBot meldt geldt extra: **geen PDF-export** van objecten (`task=property_pdf`), **geen objectfoto's** (`/images/osproperty/properties/`) en **10 seconden tussen verzoeken**. Bij deze toets zijn die strengste regels aangehouden en dat is ook het advies voor de lezer.

## 2. Gebruiksvoorwaarden — niet gevonden; de enige juridische link is stuk

Op homepage, aanbodpagina en objectpagina (24-09-2026) staat maar één juridische link, in de voettekst: "Privacy & Cookie Policy" → `/en/component/content/article/privacy-policy?catid=8&Itemid=112`. Die stuurt door naar `/en/component/content/article/0?catid=8&Itemid=112` en geeft **HTTP 404 "Page not found"** (opgehaald 24-09-2026 21:34 UTC). Een aviso legal, términos, terms of disclaimer is nergens gelinkt. Er staat geen cookiebanner-tekst in de HTML.

Conclusie: er is geen tekst die automatisch lezen of scraping verbiedt, maar er is ook geen tekst die iets toestaat. Voorzichtigheidshalve: alleen kale feiten noteren (prijs, plaats, m², perceel, referentie, link naar de bron), geen foto's of beschrijvingsteksten overnemen — de foto's zijn voor AI-lezers sowieso uitgesloten in robots.txt.

## 3. Sitemap — geen

- robots.txt heeft geen `Sitemap:`-regel.
- https://www.javeaestates.com/sitemap.xml → omleiding naar `/en/sitemap.xml` → **HTTP 404** (24-09-2026).
- `/sitemap_index.xml` is niet geprobeerd (pagina-budget). Joomla-sites hebben soms een OSMap-sitemap op een ander adres [te verifiëren].
- Tellen van object-URL's via de sitemap is dus niet mogelijk; de telling hieronder komt van de paginering van de aanbodpagina.

## 4. Aanbodpagina en objectpagina

**Aanbodpagina:** https://www.javeaestates.com/en/properties (24-09-2026, HTTP 200, 139 kB). Titel "Properties". 20 kaarten per pagina; paginering `/en/properties/page-2` … `/page-10` en `/page-14` (laatste). Per kaart: label (For sale / New Build / Holiday rental), type (Villa, Plot, Apartment, Townhouse), prijs (bijv. `€ 1.960.000,00`), bebouwde m² ("285 sqmt"), aantal slaapkamers, titel, eerste regels van de beschrijving. **Geen apart plaatsveld** op de kaart; de plaats staat in titel of beschrijving. Objectlinks volgen het patroon `/en/properties/<categorie>/<referentie>-<slug>-<intern-id>`, bijvoorbeeld `/en/properties/featured-sales/60-4650-5-60-4650-5traditional-villa-with-sea-view-for-sale-in-tosalet-5-javea-1353`. Zoekformulier (GET, `task=property_advsearch`) met type, prijs, plaats, bed/bad, m² en perceel.

**Objectpagina bekeken:** https://www.javeaestates.com/en/properties/featured-sales/60-4650-5-60-4650-5traditional-villa-with-sea-view-for-sale-in-tosalet-5-javea-1353 (24-09-2026, HTTP 200, 144 kB).

- **JSON-LD:** ja, één blok `<script type="application/ld+json">`, maar alleen `@type: BreadcrumbList` (Home › Properties › Featured villas). **Geen** `RealEstateListing`, `Product`, `Offer`, prijs, oppervlakte of adres in JSON-LD. (De homepage heeft alleen een `Organization`-blok met naam en url.)
- **og-tags:** ja — `og:title` "Traditional villa with sea view for sale in tosalet 5 javea", `og:url`, `og:type` = "website", `og:image` (medium-foto uit `/images/osproperty/properties/1353/`), `og:description` (eerste ~450 tekens van de beschrijving, met daarin "plot of approximately 1,000 m2"). **Geen prijs** in de og-tags. Geen `<link rel="canonical">`.
- **In de leesbare tekst (server-gerenderd):** referentie **60-4650-5**; **€ 750.000,00**; 3 slaapkamers, 3 badkamers; **255.00 sqmt** bebouwd; **Lot Size 1037 sqmt** (perceel); label "For sale"; "4 month(s) ago" (plaatsingsleeftijd) en "957 views"; plaats alleen in de tekst: Cansalades / Tosalet, Jávea (geen adres- of coördinaatveld gevonden; de kaart wordt via Google Maps geladen). Voorzieningen als lijst (zwembad, terras, airco, automatische poort, enz.). Fotobestanden heten `2026_05_4650JAV_04.jpg` — de interne referentie is dus 4650JAV, met "60-" ervoor en "-5" erachter op de site.
- Onderaan "Related properties" en "Properties in same Property type" met referentie, titel, label en prijs van tien andere objecten (bijna allemaal Jávea).
- Links "PDF" (`task=property_pdf&id=1353`) en "Print" (`task=property_print`): de PDF-variant is voor AI-lezers verboden in robots.txt — niet gebruiken.

Conclusie: goed leesbaar, maar de gegevens moeten uit de HTML-tekst worden gehaald (labels "Square meter", "Lot Size", prijs in `span.price`), niet uit gestructureerde data.

## 5. Systeem achter de site — Joomla met OS Property (geen van de bekende makelaars-CMS'en)

Aanwijzingen (24-09-2026):

- `<meta name="generator" content="Joomla! - Open Source Content Management">` op elke pagina; robots.txt is het standaard Joomla-bestand.
- Component `com_osproperty` (OS Property van joomdonation) overal: paden `/components/com_osproperty/templates/theme3/…`, `/media/com_osproperty/assets/js/…`, `/images/osproperty/properties/<id>/medium/…`, formulieren met `option=com_osproperty` en taken `property_advsearch`, `property_requestmoredetails`, `property_pdf`, `property_print`; JS-functies `OspropertySearchChangeDiv`, `OspropertyChangeValue`.
- Template `osprealestate4` (foutpagina's laden `/templates/osprealestate4/css/jpages.css`) op het T4-framework van JoomlArt (`/plugins/system/t4/`, klassen `t4-section`, `t4-megamenu`, `t4-footer`); slider `mod_trulyresponsiveslides`.
- Server: `Server: Apache`; sessiecookie met een 32-tekens hexadecimale naam (typisch Joomla), HttpOnly.
- Geen sporen van Inmoweb, Mediaelx/LetsINMO, Sooprema, Inmovilla, Witei of WordPress. AddThis-deelknoppen, Google Maps, Google Fonts.

OS Property kent geen standaard exportfeed voor derden [te verifiëren]; een feed vragen is hier dus niet de aangewezen route — lezen is dat wel.

## 6. Omvang en dekking Jávea / Benitachell / Moraira

- **Totaal:** 14 pagina's × 20 kaarten = **ca. 261–280 vermeldingen** op `/en/properties` (alle types door elkaar: te koop, nieuwbouw, vakantieverhuur; mogelijk ook langetermijnverhuur). Alleen pagina 1 is gelezen.
- **Pagina 1 (20 kaarten):** 12 "For sale", 7 "New Build", 1 "Holiday rental". Plaatsen: Jávea 4 (perceel € 500.000, villa Cansalades € 750.000, appartement bij de haven € 355.000, plus één dubbeling), Moraira 4 (nieuwbouw € 2.250.000, villa La Arnella € 550.000, perceel Paichi € 386.400, plus één dubbeling), Cumbre del Sol/Benitachell 2 (nieuwbouw € 2.150.000, villa € 900.000), en verder Altea Hills, Torrevieja, Alcalalí, Calpe (2), Benissa, Beniarbeig, Jalón (2), Pedreguer, en één vakantievilla zonder plaats op de kaart. **Jávea + Benitachell + Moraira: 10 van 20 kaarten (50 %)**, of 7–8 van 19 koopobjecten na ontdubbeling (ca. 40 %).
- **Homepage "Featured properties for sale":** 10 van 10 in Jávea (prijzen € 259.600 – € 3.150.000; 3 percelen, 7 villa's waarvan 5 nieuwbouw). Het kantoor zet Jávea dus zelf voorop; de eigen kern lijkt Jávea, de rest van Costa Blanca Noord komt erbij.
- **Dubbele vermeldingen:** referenties met voorvoegsel `72-` (bijv. `72-680646-29640-villa-for-sale-1389`) hebben de generieke titel "Villa for sale" en exact dezelfde beschrijving, prijs en m² als een `60-`-object (72-680646 = 60-4650-5 Cansalades; 72-680081 = 60-8272-5 Moraira La Arnella). 14 van de 20 kaarten op pagina 1 hebben voorvoegsel `60-`; de andere (`70-`, `72-`, `73-`, `33-`) zien eruit als aanbod uit een gedeeld netwerk of import [te verifiëren]. Ontdubbelen op prijs + m² + eerste 100 tekens beschrijving.
- Schatting koopaanbod na ontdubbeling: **ca. 200–250 objecten**, waarvan naar schatting 40–50 % in het doelgebied (alleen pagina 1 en de homepage gezien — [te verifiëren] bij de eerste volledige leesronde). Ook de "Pending" en "Sold" filters in het zoekformulier zijn interessant: verkochte objecten geven referentieprijzen.

## Samenvatting voor de lezer-configuratie

| Onderdeel | Waarde |
|---|---|
| Startpunt | https://www.javeaestates.com/en/properties en `/en/properties/page-2` … `/page-14` |
| Objectpatroon | `/en/properties/<categorie>/<ref>-<slug>-<id>` |
| Per object uit HTML | referentie (bijv. `60-4650-5`), prijs (`span.price` / "EUR x"), "Square meter … sqmt", "Lot Size … sqmt", bed/bad, label For sale / New Build, "x month(s) ago", plaats uit titel/tekst |
| Gestructureerde data | JSON-LD alleen breadcrumbs; og-tags zonder prijs — dus HTML-tekst parsen |
| Tempo | 1 verzoek per 10 s (strengste regel in robots.txt), max. ca. 300 verzoeken per volledige ronde → ca. 50 minuten |
| Niet doen | `/images/osproperty/properties/` (foto's), `task=property_pdf`, formulieren, inloggen |
| Ontdubbelen | `72-`-vermeldingen tegen `60-`-vermeldingen op prijs + m² + beschrijving |
| Frequentie | wekelijks volstaat; menu "New on the market" (`/en/properties/new-on-the-market`) als snelle check tussendoor |
| Voorwaarden | niet gevonden (privacy-link 404) — alleen feiten opslaan, niets herpubliceren |

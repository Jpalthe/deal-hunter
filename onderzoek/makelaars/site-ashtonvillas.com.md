# Ashton Villas — ashtonvillas.com — toets op automatisch lezen

Datum toets: 24-09-2026 · Onderzoeker: TREE Deal Hunter (automatische toets)
Kantoor: Ashton Villas, "Estate Agents in Javea & Moraira" (eigen omschrijving op de site)
Algemene kanalen: info@ashtonvillas.com · +34 637 052 484 (ook WhatsApp) · Facebook /ashtonvillasjavea
Kantooradres: niet gevonden op de vijf bekeken pagina's (footer toont alleen e-mail en telefoon).
(bron: https://www.ashtonvillas.com/property/villa-in-javea-11/ en JSON-LD Organization-blok, 24-09-2026)

## Advies in één zin

**Lezen.** robots.txt staat de aanbod- en objectpagina's toe, de site heeft geen gebruiksvoorwaarden die
automatisch lezen verbieden (alleen een gewone auteursrechtclausule tegen kopiëren/verspreiden), de
sitemap geeft alle objecten netjes weer en elke objectpagina bevat een schema.org `RealEstateListing`
met prijs, bouwoppervlak, slaapkamers en referentie. Kanttekening: de sitemap is sinds 03-07-2025 niet
meer bijgewerkt, dus het aanbod kan deels verouderd zijn — bij het lezen datum en status controleren.

## 1. robots.txt — toegestaan

Bron: https://www.ashtonvillas.com/robots.txt (opgehaald 24-09-2026, HTTP 200, server LiteSpeed).
Volledige inhoud:

```
# START YOAST BLOCK
# ---------------------------
User-agent: *
Disallow: /?s=
Disallow: /page/*/?s=
Disallow: /search/
Disallow: /wp-json/
Disallow: /?rest_route=

User-agent: AdsBot
Disallow: /

Sitemap: https://www.ashtonvillas.com/sitemap_index.xml
# ---------------------------
# END YOAST BLOCK
```

Voor `User-agent: *` zijn alleen de interne zoekfunctie (`/?s=`, `/search/`) en de WordPress-API
(`/wp-json/`, `/?rest_route=`) afgesloten. De aanbodpagina `/property/` en alle objectpagina's
`/property/<slug>/` vallen daar niet onder en mogen dus gelezen worden. Alleen Googles AdsBot is
volledig geweerd. Gevolg voor ons: de objectpagina's zelf lezen mag; de REST-API (`/wp-json/`) niet
gebruiken, ook al zou die technisch de gegevens als JSON kunnen geven.

## 2. Gebruiksvoorwaarden — geen verbod op automatisch lezen, wel auteursrecht

Er is geen pagina "terms", "aviso legal" of "condiciones". De footer van de objectpagina linkt naar:
`/disclaimer/`, `/privacy-statement-eu/`, `/privacy-statement-uk/`, `/cookie-policy-eu/`,
`/cookie-policy-uk/` (de laatste vier zijn standaard Complianz-pagina's; niet opgehaald).

Bron: https://www.ashtonvillas.com/disclaimer/ (opgehaald 24-09-2026, HTTP 200). De tekst gaat over
juistheid van informatie, aansprakelijkheid, webformulieren en privacy. De enige relevante bepaling
(Engelse tekst, letterlijk, naam van de eigenaar weggelaten):

> "All intellectual property rights to content on this website are vested in [de eigenaar] or in third
> parties who have placed the content themselves or from whom [de eigenaar] has obtained a user license.
> Copying, disseminating and any other use of these materials is not permitted without the written
> permission of [de eigenaar], except and only insofar as otherwise stipulated in regulations of
> mandatory law (such as the right to quote), unless specific content dictates otherwise."

De woorden scraping, crawling, robots, automated of extraction komen niet voor. Het is een gewone
auteursrechtclausule: de foto's en teksten niet overnemen of doorplaatsen. Intern lezen en analyseren
(prijs, oppervlak, plaats, referentie) om een deal te signaleren valt daar niet onder; wel: geen foto's
of beschrijvingen kopiëren naar eigen systemen of publicaties.

## 3. Sitemap — 157 objecten, laatst bijgewerkt 03-07-2025

Bron: https://www.ashtonvillas.com/sitemap_index.xml (opgehaald 24-09-2026). Vier deelsitemaps:

| Deelsitemap | lastmod in index |
|---|---|
| page-sitemap.xml | 2024-02-08 |
| **property-sitemap.xml** | **2025-07-03** |
| property-type-sitemap.xml | 2025-07-03 |
| property-city-sitemap.xml | 2025-07-03 |

Bron: https://www.ashtonvillas.com/property-sitemap.xml (opgehaald 24-09-2026): **158 URL's**, waarvan
1 de archiefpagina `/property/` en **157 objectpagina's** `/property/<slug>/`. lastmod-waarden lopen
van 2023-10-31 tot 2025-07-03. Alle objectpagina's zitten in één sitemap; er zijn geen aparte
verkoop/verhuur-sitemaps (de slugs bevatten "for-sale" of geen aanduiding; verhuur niet gezien).

Let op: de sitemap (en de property-taxonomieën) zijn op 24-09-2026 al bijna 15 maanden niet gewijzigd.
Ofwel het aanbod is sindsdien niet aangevuld, ofwel de sitemap-cache loopt achter. Bij het lezen
`datePublished`/`dateModified` van elke pagina meenemen en de status ("For Sale") controleren.

Twee slugs heten `villa-in-array` en `villa-in-array-2` — een importfout waarbij het plaatsveld een
lijst was. Samen met de bestandsnamen van de foto's (`property_image_<id>_<tijdstempel>.jpg`) wijst dat
op een geautomatiseerde import vanuit een extern CRM of feed in WordPress; welk systeem is niet
vast te stellen uit de HTML.

## 4. Objectpagina — leesbaar, met JSON-LD en Open Graph

Aanbodpagina: https://www.ashtonvillas.com/property/ (uit de sitemap en de breadcrumb "Home > Properties";
niet apart opgehaald, het budget van vijf verzoeken was op). Het hoofdmenu van de objectpagina toont
alleen Home, Contact Us en My Account; het aanbod wordt op de homepage getoond (niet bekeken).

Bekeken object: https://www.ashtonvillas.com/property/villa-in-javea-11/ (opgehaald 24-09-2026,
HTTP 200, 224 kB). Zichtbaar op de pagina:

| Veld | Waarde |
|---|---|
| Titel | villa in Jávea |
| Status | For Sale |
| Prijs | 2,600,000€ |
| Ref | AV421 |
| Slaapkamers / badkamers | 5 / 6 |
| Bouwjaar | 2015 |
| Build (bouwoppervlak) | 550 m² |
| Plot (perceel) | 1250 m² |
| Plaats | Jávea, bij Cala la Granadella (uit de beschrijving; geen adres- of kaartveld) |

**JSON-LD** (`<script type="application/ld+json">`): twee blokken.
1. Yoast-blok met `@graph`: WebPage (datePublished 2024-08-19), ImageObject, BreadcrumbList, WebSite
   ("Javea & Moraira Estate Agents"), Organization (logo, Facebook-link).
2. **`RealEstateListing`** (uit het thema): `name` "villa in Jávea", `url`, `offers.price` "2600000",
   `priceCurrency` "€" (let op: geen ISO-code EUR), `availability` ForSale, `additionalProperty`:
   Bedrooms 5, Bathrooms 5 (de pagina zelf zegt 6), Area Size 550 m², Year Built 2015.
   `address` en `geo` zijn aanwezig maar **leeg**; het **perceel staat niet in de JSON-LD** — dat moet
   uit de zichtbare HTML (`Plot … m²`) worden gelezen, net als de referentie (`rh_property__id`).

**Open Graph**: `og:title`, `og:description`, `og:url`, `og:type` article, `og:site_name`, `og:locale`
en_GB, `og:image` (thumbnail 210×210) — twee keer aanwezig (Yoast en thema), plus `twitter:card`.
Geen prijs of oppervlak in de og-tags.

De pagina is gewone server-side HTML (LiteSpeed-cache, geen JavaScript nodig om prijs en velden te
lezen). Geen `set-cookie` in de antwoordheaders. De site heeft WPML met hreflang voor en, es, nl, de, fr
(de bekeken pagina had alleen de Engelse variant als URL).

## 5. Systeem achter de site — WordPress met het thema RealHomes

Aanwijzingen uit de HTML van de objectpagina (24-09-2026):
- Themapaden `wp-content/themes/realhomes` en `wp-content/themes/realhomes-child`; CSS-klassen
  `rh_property__…` (156 keer), `data-property-id`, vergelijk-knop `rh_single_compare_button`,
  contactformulier `send_message_to_agent` — allemaal kenmerkend voor **RealHomes** (InspiryThemes).
- `<meta name="generator" content="WPML ver:4.6.14">`; Yoast-blok in robots.txt en Yoast-JSON-LD.
- HTML-commentaar: "Page cached by LiteSpeed Cache 7.8.1", "QUIC.cloud CCSS loaded"; server LiteSpeed.
- Cookie- en privacypagina's met de Complianz-slugs (`cookie-policy-eu`, `privacy-statement-eu`).
- Geen Inmoweb, Mediaelx/LetsINMO, Sooprema, Inmovilla of Witei gezien: geen van hun script- of
  afbeeldingspaden, geen "powered by".

Conclusie: **WordPress + RealHomes-thema** (eigen vastgoedmodule van het thema), vermoedelijk gevuld
via een geautomatiseerde import (zie §3). RealHomes kent geen standaard exportfeed voor derden; een
feed zou het kantoor zelf moeten leveren.

## 6. Omvang en dekking Jávea / Benitachell / Moraira

Geteld op de 157 object-URL's in property-sitemap.xml (plaatsnaam in de slug, 24-09-2026):

| Plaats (uit slug) | Aantal |
|---|---|
| Jávea/Xàbia | 53 |
| Moraira | 14 |
| Benitachell / Cumbre del Sol | 0 |
| **Subtotaal doelgebied** | **67 (43 %)** |
| Calpe | 35 |
| Benissa | 20 |
| Altea | 13 |
| Pedreguer | 4 |
| Finestrat | 3 |
| Teulada, Dénia, Gata | 2 elk |
| Overig (Benidorm, Alfaz, Alcalalí, Tàrbena, Els Poblets, San Vicente, Mallorca, "array") | 9 |

Binnen Jávea + Moraira: 54 villa's, 5 appartementen, 3 bouwpercelen, 2 rijwoningen, 1 penthouse,
1 finca, 1 project. Schatting aanbod: **circa 150–160 objecten** volgens de sitemap, maar omdat die
sinds juli 2025 niet is bijgewerkt is het werkelijke actuele aanbod onbekend [te verifiëren bij het
lezen van de pagina's zelf].

## Verzoeken gedaan (budget 5, tempo minimaal 2 s ertussen)

1. /robots.txt · 2. /sitemap_index.xml · 3. /property-sitemap.xml · 4. /property/villa-in-javea-11/ ·
5. /disclaimer/. Niet opgehaald: homepage, /property/, page-sitemap.xml, property-city-sitemap.xml,
privacy- en cookiepagina's.

## Aanbevolen leesstrategie

- Bron van de lijst: property-sitemap.xml (157 URL's); tempo 1 verzoek per 2–3 s → ruim 8 minuten
  per volledige ronde; wekelijks volstaat gezien de lage mutatiefrequentie.
- Per pagina lezen: JSON-LD `RealEstateListing` (prijs, bouwoppervlak, slaapkamers, bouwjaar) én de
  HTML-velden `rh_property__id` (Ref) en "Plot … m²" (perceel) en de status "For Sale".
- Plaats afleiden uit de slug/titel; de JSON-LD-adresvelden zijn leeg.
- Geen foto's of beschrijvingsteksten opslaan of hergebruiken (auteursrechtclausule in de disclaimer).
- `/wp-json/` en de zoekfunctie niet aanspreken (robots.txt).

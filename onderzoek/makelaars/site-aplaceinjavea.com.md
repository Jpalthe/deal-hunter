# A Place in Javea — toets op automatisch lezen

**Site:** https://www.aplaceinjavea.com
**Datum controle:** 24-09-2026 (5 verzoeken, ruim 2 s ertussen: robots.txt, sitemap.xml, startpagina, voorwaarden, één objectpagina)
**Advies: LEZEN** — met twee kanttekeningen (zie onderaan).

## Eerst dit: het is geen makelaar, maar een portaal

De site noemt zichzelf in de eigen JSON-LD "Independent property portal covering Javea, Moraira, Denia, Benitachell and Cumbre del Sol" (bron: https://www.aplaceinjavea.com/, 24-09-2026). De voorwaarden zeggen hetzelfde: het is een onafhankelijke informatie- en advertentiesite, beheerd door een particulier, "not an estate agency, property broker, lawyer, surveyor or financial adviser". De objecten zijn advertenties van makelaars, projectontwikkelaars en particuliere verkopers (bron: https://www.aplaceinjavea.com/terms-and-conditions/, versie 12-08-2026).

Gevolg voor Deal Hunter: de objecten hier staan vermoedelijk ook op de sites van de oorspronkelijke makelaars. De referenties verraden dat: `SEOJON-EHS…`, `SEOJON-MLS…`, `SEOJON-FMLS…`, `SEOJON-MMC…`, `SEOJON-SPE…`, `SEOJON-MRG…`, `SEOJON-WEN…`, `SEOJON-MANS_…`, `SEOJON-AG…` — meerdere bronnen achter één prefix. In de beschrijving van het geteste object staat zelfs de oorspronkelijke makelaarsreferentie (`ref:ENJ-VI-00500-C`). Ontdubbelen tegen andere bronnen is dus nodig.

Wél interessant: de site toont per object "Listed on this site" (datum), een **prijshistorie** ("Unchanged since first listed") en een vergelijking met de mediane vraagprijs in de wijk. Dat zijn precies de signalen die voor dealjacht nuttig zijn.

## 1. robots.txt — toegestaan

Bron: https://www.aplaceinjavea.com/robots.txt (24-09-2026). Eén blok voor `User-agent: *`. Relevante regels:

```
User-agent: *
Disallow: /wp-admin/
Allow: /property-type/
Allow: /property-city/
Allow: /property-area/
Disallow: /property_tag/
Disallow: /search/
Disallow: /?s=
Disallow: /*?
Disallow: /partner/
Disallow: /municipality/
Disallow: /province/
Sitemap: https://www.aplaceinjavea.com/sitemap.xml
```

Objectpagina's staan onder `/property/…` en zijn nergens uitgesloten; de stads- en wijkpagina's (`/property-city/`, `/property-area/`) zijn expliciet toegestaan. Let op `Disallow: /*?`: elke URL met een vraagteken (dus gefilterde zoekresultaten zoals `/property-search/?…`) mag niet. Lezen moet dus via de gewone objectpagina's en de stads-/wijkpagina's, niet via de zoekfunctie.

## 2. Voorwaarden — scraping niet verboden, herpublicatie wel

Bron: https://www.aplaceinjavea.com/terms-and-conditions/ ("Last updated: 12 August 2026"), gelezen 24-09-2026. Er is ook een `/legal-notice/`, `/privacy-policy/` en `/cookie-policy/` (niet opgehaald, budget).

Relevante passages:
- Acceptable Use: "You may use the website for lawful personal and business research. You must not misuse the website, interfere with its operation, attempt unauthorised access, submit unlawful or misleading material or use automated systems in a way that places an unreasonable load on the service."
- Copyright: "Listing photographs and supplied descriptions may belong to the relevant advertiser or another rights holder. Material must not be copied, republished or commercially reused without permission from the applicable rights holder."

Uitleg: automatisch lezen wordt niet verboden; zakelijk onderzoek is uitdrukkelijk toegestaan, zolang de belasting redelijk blijft. Wat níet mag: foto's en teksten overnemen of commercieel hergebruiken. Voor intern analyseren (prijs, m², perceel, wijk, prijsverloop) is dat geen belemmering; foto's en beschrijvingen niet opslaan voor eigen publicaties.

## 3. Sitemap — objecten staan er niet in

Bron: https://www.aplaceinjavea.com/sitemap.xml (24-09-2026, gemaakt door All in One SEO Pro 5.0.1.1). Het is een sitemap-index met vijf deelsitemaps: `addl-sitemap.xml`, `page-sitemap.xml`, `post-sitemap.xml`, `property_city-sitemap.xml`, `property_area-sitemap.xml`. **Er is geen `property-sitemap.xml`**: de objectpagina's zelf zitten niet in de sitemap. Aantal object-URL's in de sitemap: 0. De deelsitemaps zijn niet opgehaald (budget van vijf pagina's); de stads- en wijksitemaps zijn wel de logische ingang om alle objecten te vinden.

Praktische route: de startpagina toont al 32 objecten per pagina en linkt naar 28 wijkpagina's onder `/javea/<wijk>/` (Arenal, Portichol, Montgó, Tosalet, Cap Martí, Granadella, Balcón al Mar, Costa Nova, …). Via die wijkpagina's zijn alle objecten te bereiken zonder de zoekfunctie.

## 4. Objectpagina — JSON-LD én og-tags aanwezig

Aanbodpagina: https://www.aplaceinjavea.com/property-search/ (menu "Jávea"; startpagina toont "200 properties for sale in Javea", 24-09-2026).
Geteste objectpagina: https://www.aplaceinjavea.com/property/seojon-ehs11515d-villas-in-javea/ (24-09-2026).

JSON-LD (`<script type="application/ld+json">`), gemaakt door AIOSEO: `BreadcrumbList`, `Organization`, `Person`, `WebSite` en een **`RealEstateListing`** met `mainEntity` → `Offer`:
- `price`: 1350000, `priceCurrency`: EUR
- `itemOffered`: `House`, `identifier`: SEOJON-EHS11515D
- `description`: beschrijving met "plot of more than 1,000 m²" en "222 m² built"
- `datePublished` 2026-09-17, `dateModified` 2026-09-18

Oppervlakte en perceel staan niet als aparte JSON-LD-velden (geen `floorSize`), wel netjes in de zichtbare HTML: "Bedrooms 3 · Bathrooms 3 · Built area 222 m² · Plot 1000 m² · Listed on this site 17 September 2026 · Price history: Unchanged since first listed · Municipality Javea · Area Portichol · Property type Villas · Asking price €1,350,000".

og-tags: `og:type` article, `og:title`, `og:description`, `og:url`, `article:published_time`, `article:modified_time`. Let op: `og:image` is het sitelogo, niet de objectfoto. Voor de gegevens is JSON-LD dus de betere bron, aangevuld met de HTML-feitenblokjes.

## 5. Systeem achter de site

**WordPress, eigen bouw** (geen Inmoweb, Mediaelx, Sooprema, Inmovilla of Witei). Bewijs (bron: HTML van startpagina en objectpagina, 24-09-2026):
- `<meta name="generator" content="WordPress 7.1.2">`, plus AIOSEO Pro 5.0.1.1, Redux 4.5.7, Site Kit 1.171.0
- Thema: `wp-content/themes/apj-generatepress` (eigen childthema op GeneratePress); body-class `single-property` → eigen posttype `property` met taxonomieën `property_city`, `property_area`, `property-type`
- Plugins in de HTML: Elementor, Revolution Slider, Responsive Lightbox, Breeze (cache); hosting op Cloudways (header `cache-provider: CLOUDWAYS-CACHE-DE`), server nginx
- Restanten van het Houzez-vastgoedthema in CSS/JS (`houzez_sticky`, `houzez-search-form-js`), maar het actieve thema is GeneratePress
- Geen cookies gezet bij een gewoon bezoek; geen "powered by" van een makelaars-CMS
- Objecten worden geïmporteerd uit meerdere bronnen (prefix `SEOJON-` + broncode); er is geen bekende exportfeed voor derden gevonden

## 6. Omvang en dekking

- Jávea: **200 objecten** ("200 current properties" / "200 properties for sale in Javea", startpagina 24-09-2026), in 28 wijken.
- Daarnaast aparte secties voor Moraira, Benitachell, Cumbre del Sol en Denia (menu). Aantallen daarvan zijn niet geteld (zou extra pagina's kosten).
- Dekking Jávea/Benitachell/Moraira: de site is er om gebouwd; alleen Denia valt buiten het zoekgebied. Schatting: ruim de meerderheid van het totaal ligt in het doelgebied, met Jávea als zwaartepunt [te verifiëren via `property_city-sitemap.xml`].

## Advies: lezen

Robots.txt staat het toe, de voorwaarden staan zakelijk onderzoek toe en verbieden alleen onredelijke belasting en herpublicatie, en de objectpagina's zijn machineleesbaar (JSON-LD met prijs en referentie, feiten in vaste HTML-blokken).

Kanttekeningen:
1. **Ontdubbelen.** Dit is een portaal met advertenties van meerdere makelaars; dezelfde woning komt waarschijnlijk ook via de makelaarssites binnen. Gebruik de oorspronkelijke referentie in de beschrijving (bijv. `ENJ-VI-00500-C`) en prijs+m²+wijk om dubbelen te herkennen.
2. **Alleen gegevens, geen foto's of teksten overnemen.** Rustig tempo (≥ 2 s per verzoek), alleen `/property/…`, `/javea/<wijk>/`, `/property-city/…` en `/property-area/…`; geen URL's met `?`.
3. De prijshistorie en "listed on this site"-datum per object zijn een extra bron voor prijsdalingen en lang lopende objecten — dat heeft een gewone makelaarssite meestal niet.

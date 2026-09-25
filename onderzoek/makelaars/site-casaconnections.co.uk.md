# Casa Connections — casaconnections.co.uk

Toets op automatisch lezen · TREE Deal Hunter · 24-09-2026
Ophalingen: 5 (robots.txt, sitemap-index, objectsitemap, één objectpagina, privacypagina), telkens ruim meer dan twee seconden uit elkaar. De zoekfunctie was in deze sessie niet beschikbaar (budget op); alles hieronder komt rechtstreeks van de site zelf.

## Advies: **lezen**

robots.txt staat alles toe, er zijn geen gebruiksvoorwaarden die automatisch lezen verbieden, en de objectpagina's zijn gewone WordPress-pagina's met een vast, goed leesbaar detailblok (Property ID, Price, Property Size, Land Area, Bedrooms, Bathrooms). Klein kantoor: 84 objecten, vrijwel alles in Jávea. Prijs en oppervlakte staan **niet** in de JSON-LD of de og-tags, dus die moeten uit de zichtbare HTML komen.

## 1. robots.txt — toegestaan

Bron: https://casaconnections.co.uk/robots.txt (HTTP 200, 24-09-2026)

```
User-agent: *
Allow: /
Sitemap: https://casaconnections.co.uk/sitemap.xml
Sitemap: https://casaconnections.co.uk/sitemap_index_0.xml
…
Sitemap: https://casaconnections.co.uk/sitemap_index_30.xml
```

Geen enkele `Disallow`-regel. `User-agent: *` mag dus alles lezen, ook de aanbodpagina's. De 31 regels `sitemap_index_0.xml` t/m `_30.xml` heb ik niet opgehaald (buiten het budget van vijf pagina's); de werkelijke sitemap van de site is de Yoast-index hieronder.

## 2. Gebruiksvoorwaarden — niet gevonden, geen verbod

De site heeft alleen een privacyverklaring; een terms/aviso legal/disclaimer-pagina bestaat niet (niet in de navigatie, niet in de voettekst, niet in de sitemap-index).

Bron: https://casaconnections.co.uk/privacy-policy/ (HTTP 200, 24-09-2026), "Last updated: February 23, 2022", gemaakt met een privacy-policy-sjabloon. Kopjes: Interpretation, Definitions, Types of Data Collected, Personal Data, Usage Data, Tracking Technologies and Cookies, Use/Retention/Transfer/Disclosure of Your Personal Data, Security.

Doorzocht op: scrap, crawl, spider, robot, automat, harvest, data mining, reproduc, copyright, intellectual property, licen, prohibit, not permitted, terms and conditions, terms of use, aviso legal. Enige treffers: drie keer "automatically" — telkens over gebruiksgegevens die de site zelf verzamelt ("Usage Data is collected automatically when using the Service"). Niets over automatisch lezen, kopiëren of hergebruik van het aanbod.

## 3. Sitemap — 84 objecten

- https://casaconnections.co.uk/sitemap.xml → stuurt door naar https://casaconnections.co.uk/sitemap_index.xml (Yoast SEO). Bevat 9 deelsitemaps: post, page, **property**, category, post_tag, property_type, property_status, property_city, author.
- https://casaconnections.co.uk/property-sitemap.xml (HTTP 200, 24.900 bytes, 24-09-2026): **85 URL's, waarvan 84 objectpagina's** onder `/property/<slug>/` plus 1 archiefpagina `/property/`. 84 afbeeldingen.
- `lastmod`: 71 objecten bijgewerkt in 2026, 11 in 2025, 2 in 2024, 1 in 2023; nieuwste 2026-09-24 11:32 — de site wordt dus actief bijgehouden.
- 61 slugs bevatten "sale", 0 "rent": alleen verkoop.

Alle 84 URL's staan lokaal in de scratchpad (`property-urls.txt`) voor de volgende stap.

## 4. Aanbodpagina en objectpagina

- Aanbodpagina (uit de navigatie): https://casaconnections.co.uk/properties/ — plus per plaats https://casaconnections.co.uk/javea/, /moraira/, /benitachell/, /jesus-pobre/ en per type bijv. /property-type/land/.
- Voorbeeldobject: https://casaconnections.co.uk/property/javea-plot-for-sale-with-project/ (HTTP 200, 130 kB, 24-09-2026)

Wat er in de zichtbare HTML staat (Houzez-detailblok):
`Property ID 5133 · Price €380,000 · Property Size 212 m2 · Land Area 1069 m2 · Bedrooms 3 · Bathrooms 2`, ligging "urbanization Piver", Jávea (perceel met bouwvergunning en project).

- **JSON-LD:** één blok `<script type="application/ld+json">`, afkomstig van Yoast: `@graph` met WebPage, ImageObject, BreadcrumbList (Home › Properties › object), WebSite en Organization ("Casa Connections", logo). **Geen** RealEstateListing/Offer, dus geen prijs, oppervlakte, perceel of referentie in de JSON-LD.
- **og-tags:** `og:locale en_GB`, `og:type article`, `og:title "Javea Plot for Sale with Project - Casa Connections"`, `og:description` (korte tekst), `og:url`, `og:site_name`, `og:image` (725×510). Geen prijs of oppervlakte.
- Gevolg voor de lezer: prijs, oppervlaktes en referentie ("Property ID") uit het detailblok in de HTML halen; plaats uit de slug/breadcrumb/plaatspagina.

## 5. Systeem achter de site: WordPress + Houzez

Aanwijzingen (objectpagina, 24-09-2026):
- Paden `wp-content/themes/houzez/` (en een variant `houzez%20Aug`), `wp-content/plugins/gtranslate/`
- `<meta name="generator" content="Elementor 4.3.1">` en `Redux 4.5.15`
- HTML-commentaar: "This site is optimized with the Yoast SEO plugin v28.5"
- Houzez-klassen/commentaar: `property-banner`, `property-detail-wrap`, `hs-gallery-v4-grid`
- Server: Apache; geen cookies gezet bij een gewone GET
- Yoast-sitemaps met de Houzez-taxonomieën property_type, property_status, property_city
- WP REST API staat open: `<link rel="alternate" href="https://casaconnections.co.uk/wp-json/wp/v2/properties/24157">` — Houzez publiceert objecten dus ook als JSON via de standaard WordPress-API (niet opgehaald; kan een nette bron zijn, maar valt ook onder "alles toegestaan" van robots.txt).

Dus: geen Inmoweb, Mediaelx, Sooprema, Inmovilla of Witei; een gewone WordPress-site met het Houzez-vastgoedthema. Er is geen standaard exportfeed zoals bij de Spaanse CMS'en; de HTML (of de REST-API) is de bron.

## 6. Omvang en dekking Jávea / Benitachell / Moraira

Geteld op de plaatsnaam in de 84 objectslugs (property-sitemap.xml, 24-09-2026):

| Plaats | Objecten |
|---|---|
| Jávea | 77 |
| Moraira | 3 |
| Benitachell | 1 |
| Benissa | 1 |
| Teulada | 1 |
| Jesús Pobre (Dénia, grenst aan Jávea) | 1 |

**81 van 84 (96 %) in Jávea, Benitachell of Moraira**; Jávea alleen al 92 %. Slugs zonder plaatsnaam: geen. Let op: dit is de slug, niet een gecontroleerd adres — een enkel object kan anders liggen dan de slug suggereert.

## Kantoor (alleen bedrijfsgegevens)

Casa Connections; de privacyverklaring noemt het bedrijf "Casaconnections, Spain". Algemene kanalen op de site: sales@casaconnections.com, telefoon UK +44 7712073041, openingstijden ma–vr 9:00–17:00; contactpagina https://casaconnections.co.uk/contact/. Site in het Engels (en-GB) met GTranslate-vertaling.

## Praktisch voor de lezer

1. Startpunt: property-sitemap.xml (84 URL's) — elke twee seconden één pagina is 3 minuten voor het hele aanbod.
2. Per object: `Property ID`, `Price`, `Property Size`, `Land Area`, `Bedrooms`, `Bathrooms` uit het detailblok; titel en beschrijving uit og:title/og:description; plaats uit de slug of breadcrumb.
3. `lastmod` in de sitemap gebruiken om alleen gewijzigde objecten opnieuw te lezen.
4. Aandachtspunt voor Deal Hunter: het kantoor heeft ook percelen (`/property-type/land/`), zoals dit voorbeeld met bouwvergunning.

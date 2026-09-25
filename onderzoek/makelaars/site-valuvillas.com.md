# ValuVillas — www.valuvillas.com

Toets op automatisch lezen · TREE Deal Hunter · datum: 24-09-2026

**Advies: lezen** — robots.txt staat het toe, er zijn geen gebruiksvoorwaarden
gevonden (laat staan een verbod), en de objectpagina's zijn gewone server-HTML
met referentie, prijs, perceel en bouwoppervlak als losse label/waarde-velden.
Eigen Yoast-sitemap met 176 object-URL's, waarvan ruim 80% in Jávea, Moraira of
Benitachell. Goede bron: middelgroot kantoor, veel villa's en 20+ percelen.
Let op: JSON-LD bevat géén prijs/oppervlak — die moeten uit de HTML-velden komen.

## Kantoor

- Bedrijf: ValuVillas (site-naam "Valuvillas"), presenteert zich als
  "family-run Javea estate agency", "over 30 years" actief in Jávea.
- Kantooradres: niet op de site gevonden; het LocalBusiness-schema op de
  homepage heeft lege adresvelden (`streetAddress: null`, `addressCountry: "GB"`).
- Algemeen contact: telefoon 965 771 312 (og:description) en +34 634 011 766
  (voettekst); e-mailadres is afgeschermd door Cloudflare e-mail-protection.
- Verwante domeinen [te verifiëren]: robots.txt verwijst naar sitemaps op
  `javea.properties` (eigen WordPress-site met 125 objecten, logo-bestand
  `javea-properties-logo-new.png` staat op cdn.valuvillas.com); de homepage
  linkt ook naar `javeaestateagent.com/contact-us/`. Lijkt één eigenaar met
  meerdere domeinen — niet dubbel tellen bij het samenvoegen van aanbod.
- Bron: https://www.valuvillas.com/ (HTTP 200, 24-09-2026)

## 1. robots.txt — toegestaan

Bron: https://www.valuvillas.com/robots.txt (HTTP 200, 24-09-2026). Volledige inhoud:

```
User-agent: *
Disallow: /wp-admin/
Disallow: /wp-includes/
Allow: /wp-content/uploads/
Disallow: /tag/
Disallow: /author/
Disallow: /refer/
Disallow: /date/

Sitemap: http://www.javea.properties/post-sitemap.xml
Sitemap: http://www.javea.properties/page-sitemap.xml
Sitemap: http://www.javea.properties/properties-sitemap.xml
Sitemap: http://www.javea.properties/category-sitemap.xml
Sitemap: http://www.javea.properties/property-types-sitemap.xml
```

Uitleg: alleen de WordPress-beheermappen en de archieven `/tag/`, `/author/`,
`/refer/` en `/date/` zijn verboden. De aanbodpagina `/properties/` en de
objectpagina's `/properties/<slug>/` vallen daar niet onder. Een
`User-agent: *` mag het aanbod dus lezen. Opvallend: de Sitemap-regels wijzen
naar het andere domein `javea.properties`, niet naar valuvillas.com zelf
(waarschijnlijk een gekopieerd robots-bestand; de eigen sitemap bestaat wél,
zie punt 3).

## 2. Voorwaarden — niet gevonden

- De homepage (kop, menu, voettekst) bevat geen enkele link naar aviso legal,
  terms, privacy of cookies. Voettekst-links: About Us, Spain – The Guide,
  Testimonials, News, Contact Us, Sitemap. Bron: https://www.valuvillas.com/
  (24-09-2026).
- https://www.valuvillas.com/privacy-policy/ → HTTP 301 naar de homepage
  (24-09-2026); die standaard-WordPress-pagina bestaat dus niet.
- Het enige "gebruiks"-tekstje staat onder het contactformulier van een
  objectpagina en gaat alleen over misbruik van het formulier (aanbieders van
  "guest posting, backlink building, AI, social media" worden gemeld). Niets
  over automatisch lezen van de site of hergebruik van gegevens. Bron:
  https://www.valuvillas.com/properties/lovely-5-bedroom-villa-in-javea/ (24-09-2026).
- Niet opgehaald (paginabudget van vijf was op): de HTML-pagina `/sitemap/`
  en `page-sitemap.xml`; bij een volgende ronde daar nakijken of er toch ergens
  een juridische pagina staat.

Conclusie: verbod niet gevonden.

## 3. Sitemap — aanwezig, 176 object-URL's

- Eigen sitemap (Yoast SEO, niet in robots.txt genoemd):
  https://www.valuvillas.com/properties-sitemap.xml (HTTP 200, text/xml,
  24-09-2026). 177 `<loc>`-regels: 1 index (`/properties/`) + **176 objecten**
  onder `/properties/<slug>/`. `lastmod` loopt van 18-09-2024 tot 24-09-2026;
  de oudste items kunnen verkocht of verlopen zijn.
- Sitemap uit robots.txt: http://www.javea.properties/properties-sitemap.xml
  → 301 → https://javea.properties/properties-sitemap.xml (HTTP 200,
  24-09-2026): 125 objecten, andere slugs (bijv. `villa-4-bed-javea-11`),
  `lastmod` 02-09-2026 t/m 24-09-2026. Aparte WordPress-installatie van
  vermoedelijk hetzelfde kantoor.
- Telling op slug (valuvillas.com, 176):
  - Type: villa 106 · apartment 36 · plot/land 22 · townhouse 6 · duplex 3 ·
    project 2 · finca 1 · penthouse 1 · leasehold 1 · business 1 (overlap mogelijk).
  - Plaats: Jávea ±125 (116× "javea", 6× typo "jvea", plus Montgó, El Tosalet,
    Cala Blanca) · Moraira 11 · Benitachell/Cumbre del Sol 7 · Pedreguer 8 ·
    Dénia 7 · Calpe 4 · Benissa 4 · Teulada 3 · Gata 2 · Els Poblets 2 ·
    Ondara 1 · La Xara 1 · L'Alfàs 1.

## 4. Aanbodpagina en objectpagina

- Aanbodpagina: https://www.valuvillas.com/properties/ (in menu "Property
  Type" en in de sitemap; niet apart opgehaald). Filters per type:
  `/property-types/javea-villas-for-sale/`, `.../javea-apartments-for-sale/`,
  `.../building-plots-and-land-for-sale-in-javea/`,
  `.../townhouses-for-sale-in-javea/`, `.../businesses-for-sale-javea/`;
  prijsfilters `/properties-under-200000/` en `/properties-under-300000/`.
- Voorbeeldobject: https://www.valuvillas.com/properties/lovely-5-bedroom-villa-in-javea/
  (HTTP 200, 387 kB, 24-09-2026), titel "5 Bedroom Villa in Javea - Valuvillas".
- In de gewone HTML (JetEngine-velden, dus server-side, geen JavaScript nodig):
  `Ref No.: VV627` · Bedroom 5 · Bathroom 4 · `Plot Size 1266 M2` ·
  `Build Size 253 M2` · Has Pool Yes · Sea View N.A · prijs `€1,315,000` ·
  plaats: Javea (titel/breadcrumb; geen wijk in de velden) · kenmerken o.a.
  "construction year: 2012", "near the golf course" · energielabel "PENDING".
  "Related Properties" onderaan tonen ook ref, prijs, bouw- en perceelmaat
  (bijv. VV4077 · €2,590,000 · 636 m² · 1670 m²).
- `<script type="application/ld+json">`: 3 blokken — Yoast (`WebPage`,
  `ImageObject`, `BreadcrumbList`; wel `datePublished`/`dateModified`), Schema
  Pro (`SiteNavigationElement`) en een `BreadcrumbList`. **Geen** Product,
  Offer, RealEstateListing, prijs of oppervlak in JSON-LD.
- og-tags: `og:type` article · `og:title` "5 Bedroom Villa in Javea" ·
  `og:url` · `og:site_name` Valuvillas · `og:image`
  `.../2025/03/sooprema-propiedades_536765dfb067b-source.jpg`
  (`og:image:width`/`height` staan foutief op 1) · `twitter:card`
  summary_large_image. Geen prijs in og.

## 5. Systeem achter de site

**WordPress**, eigen opbouw met page-builder; de woningdata komen uit
**Sooprema**. Aanwijzingen (24-09-2026):
- `<meta name="generator" content="Elementor 4.3.1 ...">` en
  `content="WP Rocket 3.21.3"`; header `x-powered-by: WP Rocket/3.21.3`,
  `x-turbo-charged-by: LiteSpeed`, `server: cloudflare`.
- Thema `hello-elementor` + `hello-elementor-child`; plugins `elementor`,
  `elementor-pro`, `elementskit-lite`, `jet-engine`, `jet-smart-filters`
  (objecten als custom post type met `jet-listing-dynamic-field`-velden),
  `wordpress-seo` (Yoast Premium, ook de sitemap-stylesheet), `wp-schema-pro`,
  `dynamic-content-for-elementor`, `vqt-arithmetic-captcha` (rekencaptcha op
  het formulier).
- HTML-commentaar: "Yoast SEO Premium plugin", "Schema optimized by Schema Pro".
- Alle objectfoto's heten `sooprema-propiedades_<id>-source.jpg` (80+ keer op
  de objectpagina): het aanbod wordt vanuit Sooprema (makelaars-CRM met
  exportfeed) in WordPress geladen. Er is dus ook een feed-route als dat ooit
  nodig is.
- Cookies: geen `Set-Cookie` bij de opgehaalde pagina's; geen Cloudflare-
  challenge tegen een gewone curl-aanroep.

## 6. Omvang en dekking

- Geschat aanbod: **±176 objecten** (sitemap 24-09-2026); een deel daarvan
  is mogelijk verkocht (oudste `lastmod` sept. 2024). Ref-nummers lopen van
  VV106 tot VV7102, dus het kantoor heeft een lange historie.
- Jávea + Benitachell + Moraira: **±143 van 176 (±81%)**, waarvan Jávea zelf
  ±125 (71%). Rest: Marina Alta-binnenland (Pedreguer, Gata, Ondara, Teulada,
  Benissa) en Dénia/Calpe.
- Interessant voor Deal Hunter: 22 percelen/land-URL's (o.a.
  `investors-18-building-plots-for-sale-rafalet-javea`,
  `4-superb-building-plots-on-montgo-for-sale`, `rustic-land-javea-valls-21000m2`),
  2 projecten (`project-granadella-javea`, `new-construction-for-sale-in-javea`),
  gerenoveerde/te renoveren dorpshuizen (`reformed-townhouse-for-sale-in-javea-centre`)
  en `ideal-investment-5-bedroom-villa-in-javea`.

## Hoe lezen

1. Eén keer per dag `https://www.valuvillas.com/properties-sitemap.xml`
   ophalen; nieuwe of gewijzigde `lastmod` → objectpagina ophalen.
2. Per objectpagina de velden uit de HTML halen: `Ref No.`, `Plot Size`,
   `Build Size`, `Bedroom`, `Bathroom`, prijs (`€…` bij "ENQUIRE NOW"), titel
   (type + plaats), en de features-lijst (o.a. "construction year").
   Plaats staat alleen in titel/slug; wijk soms in de beschrijving.
3. Tempo: één pagina per twee seconden of langzamer; identificeerbare
   User-Agent met contactadres. Cloudflare zit ervoor — bij een 403/challenge
   stoppen en niet omzeilen.
4. Ook `javea.properties` (125 objecten) is dezelfde bron [te verifiëren];
   samenvoegen op referentienummer om dubbelingen te vermijden.

## Opgehaalde pagina's (6, waarvan 5 op valuvillas.com)

1. https://www.valuvillas.com/robots.txt — 200
2. http://www.javea.properties/properties-sitemap.xml → https://javea.properties/properties-sitemap.xml — 200
3. https://www.valuvillas.com/ — 200
4. https://www.valuvillas.com/properties-sitemap.xml — 200
5. https://www.valuvillas.com/privacy-policy/ — 301 → homepage
6. https://www.valuvillas.com/properties/lovely-5-bedroom-villa-in-javea/ — 200

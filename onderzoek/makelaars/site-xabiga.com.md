# Xabiga S.L. — www.xabiga.com

Toets op automatisch lezen · TREE Deal Hunter · datum: 24-09-2026

**Advies: lezen (met één voorbehoud)** — robots.txt staat het toe, de
objectpagina's zijn gewone HTML (WordPress met het vastgoedthema Houzez) en de
sitemap geeft alle 141 object-URL's kant-en-klaar. Het aanbod is sterk op Jávea
gericht (kantoor in de haven van Jávea). Voorbehoud: er bestaat een pagina
`/aviso-legal/`; die is binnen het budget van vijf pagina's niet meer gelezen.
Lees die eerst (één extra pagina) voordat het lezen begint; staat daar een
verbod, dan wordt het advies "overslaan" (er is geen exportfeed).

## Kantoor

- Bedrijf: Xabiga S.L. (site-naam op de pagina's: "Xabiga - . Real Estate ·
  Inmobiliaria Calpe Alicante" — de site-naam noemt Calpe, het kantoor zit in Jávea)
- Kantooradres: C/ Cristo del Mar 33, 03730 Puerto de Jávea (Alicante)
- Algemeen contact: 965 795 219 · 672 635 795 · inmoxabiga@gmail.com
- Registratie: RAICV 0476 (register van makelaars Comunidad Valenciana)
- Openingstijden volgens de site: 9:30–16:30, maandag t/m zaterdag
- Doet naast verkoop ook verhuur (menu: "Alquiler temporal", "Alquiler anual",
  "Alquiler turístico") en heeft bedrijfsruimtes in het aanbod (locales, naves).
- Bron: koptekst/voettekst van
  https://www.xabiga.com/property/ref-1609ch-chalet-en-venta-cerca-de-comercios/ (24-09-2026)

## 1. robots.txt — toegestaan

Bron: https://www.xabiga.com/robots.txt (HTTP 200, 24-09-2026). Volledige inhoud:

```
User-agent: *
Disallow: /wp-admin/
Allow: /wp-admin/admin-ajax.php

Sitemap: https://www.xabiga.com/wp-sitemap.xml
```

Uitleg: dit is de standaard WordPress-robots.txt. Alleen het beheerdersgedeelte
`/wp-admin/` is verboden. De aanbodpagina (`/ventas/`) en de objectpagina's
(`/property/…/`) vallen daar niet onder. Een `User-agent: *` mag het aanbod dus
lezen. Er staat geen crawl-delay.

## 2. Voorwaarden — pagina bestaat, niet gelezen

- De paginasitemap https://www.xabiga.com/wp-sitemap-posts-page-1.xml (HTTP 200,
  24-09-2026) noemt een pagina **https://www.xabiga.com/aviso-legal/**.
- Die pagina is **niet opgehaald**: het budget van vijf pagina's was op (robots.txt,
  sitemap-index, objectsitemap, objectpagina, paginasitemap).
- Opvallend: op de objectpagina staat nergens een link naar aviso legal, privacy
  of cookiebeleid — niet in het menu en niet in de voettekst. De cookiebanner
  (CookieYes / cookie-law-info) linkt alleen naar cookieyes.com. De pagina is dus
  alleen via de sitemap vindbaar.
- Andere voorwaardenpagina's (términos, condiciones, privacidad) staan **niet** in
  de paginasitemap; er zijn 13 pagina's in totaal (blog, quienes-somos,
  search-results, contact, home-properties-slider, aviso-legal, quienes-somos-2,
  ventas, alquiler-anual, alquiler-temporal, alquiler-turistico, startpagina, entorno).

Conclusie: verbod niet gevonden, maar ook niet uitgesloten. **Eerste stap bij de
volgende ronde: `/aviso-legal/` lezen en citeren.**

## 3. Sitemap — aanwezig, 141 object-URL's

- Sitemap-index (uit robots.txt): https://www.xabiga.com/wp-sitemap.xml (HTTP 200,
  24-09-2026). Standaard WordPress-sitemap met 11 deelsitemaps: pagina's,
  `property` (objecten), `houzez_agency`, en de taxonomieën property_type,
  property_status, property_feature, property_label, property_country,
  property_state, property_city, property_area.
- Objectsitemap: https://www.xabiga.com/wp-sitemap-posts-property-1.xml (HTTP 200,
  24-09-2026): **141 URL's**, allemaal van de vorm `/property/<slug>/`. Alle 141
  lijken objecten (slugs als `ref-1609ch-chalet-en-venta-…`, `apartamento-en-…`,
  `parcela`, `local-comercial`). Er is maar één deelsitemap, dus minder dan 2.000
  objecten. Geen `<lastmod>`-datums.
- Referentienummers in de slugs lopen van 0000 tot 1620; 130 unieke nummers (een
  paar URL's zijn dubbel, met `-2` erachter).
- Let op: de objectsitemap bevat óók verhuur en bedrijfsruimte. Uit de slugs:
  7× `alquiler`, 2× `alquiler-turistico`, 5× local/nave/almacén. Verkoop en verhuur
  zijn dus pas op de objectpagina te scheiden (Houzez-veld "Estado"/status).

Ruwe indeling op de slugs (24-09-2026):

| Type (uit de slug) | Aantal |
|---|---|
| apartamento / ático / estudio / dúplex | 99 |
| chalet / villa / casa / adosado / finca | 29 |
| parcela / terreno | 4 |
| local / nave / almacén | 5 |
| overig / niet herkenbaar | 4 |

## 4. Aanbodpagina en objectpagina

**Aanbodpagina:** https://www.xabiga.com/ventas/ (link "Ventas" in het hoofdmenu
van de objectpagina; staat ook in de paginasitemap). Niet opgehaald (budget).
Daarnaast bestaan `/search-results/` (Houzez-zoekpagina), `/alquiler-anual/`,
`/alquiler-temporal/` en `/alquiler-turistico/`.

**Objectpagina:** https://www.xabiga.com/property/ref-1609ch-chalet-en-venta-cerca-de-comercios/
(HTTP 200, 191 kB, 24-09-2026)

- `<script type="application/ld+json">`: **niet aanwezig** (0 blokken).
- og-tags: `og:title` = "Ref.: 1609CH Chalet en venta cerca de comercios",
  `og:type` = article, `og:url`, `og:site_name`, `og:image` (foto uit
  `/wp-content/uploads/2026/07/`), `og:description` = de eerste regels van de
  beschrijving ("Única en Jávea: Gran Finca Exclusiva de 2.500 m² …").
  Dus: og aanwezig, maar **zonder prijs, oppervlakte of plaats** als apart veld.
- Geen `<meta name="robots">` met noindex.
- In de gewone HTML (Houzez-opmaak) staat wél alles:
  - Referentie: 1609CH (in de titel `Ref.: 1609CH …`)
  - Prijs: 1.700.000 € (Houzez-veld `item-price`, weergegeven als "1,700,000€")
  - Overzicht ("Descripción general"): Chalet · 5 slaapkamers · 4 badkamers ·
    1 garage · 347 m²
  - Perceel: alleen in de beschrijvingstekst: "parcela de 2.500 m² segregable a
    dos calles", hoofdwoning 350 m² — geen apart perceelveld gevuld.
  - Plaats: "Ciudad: Javea / Xabia", "Zona: Crtra del Portichol", "País: España";
    het veld "Provincia" is verkeerd gevuld met "Venta". De beschrijving noemt
    Cala Blanca op minder dan 1.000 m.
  - Kaart: de coördinaten in de pagina (25.68654, -80.431345) zijn de
    standaardwaarde van het Houzez-thema (Miami) — geen bruikbare geolocatie.
- De pagina is dus goed leesbaar: vaste labels (Tipo de inmueble, Dormitorios,
  Baños, Garaje, M2, Ciudad, Zona) plus een vrije beschrijving waar perceel en
  bijzonderheden in staan.

## 5. Systeem achter de site

**WordPress met het vastgoedthema Houzez** (eigen ingerichte site, geen
makelaars-CMS zoals Inmoweb, Mediaelx, Sooprema, Inmovilla of Witei).
Aanwijzingen (alle uit de objectpagina, 24-09-2026):

- `<meta name="generator" content="WordPress 6.2.2">`; http-header
  `link: <https://www.xabiga.com/wp-json/>` (WordPress REST API staat aan, met
  `wp-json/wp/v2/properties/26640` als JSON-versie van dit object).
- Thema: 35 verwijzingen naar `/wp-content/themes/houzez/`; post type `property`,
  `houzez_agency` en de taxonomieën `property_*` in de sitemap.
- Plugins: Elementor 3.11.2, Slider Revolution 6.6.9, Redux 4.3.26, GTranslate
  (automatische vertaling), CookieYes/cookie-law-info (cookiebanner), WP Simple
  Booking Calendar Premium (verhuurkalender), Simple Custom CSS and JS.
- Server: Apache. Eén cookie met een hash-naam, geen sessie-eis.
- Geen spoor van een portaalkoppeling of exportfeed (geen Inmoweb-, Mediaelx-,
  Sooprema-, Inmovilla-, Witei-, Kyero- of Idealista-verwijzingen in de HTML).
- WordPress-versie 6.2.2 en Elementor 3.11 zijn oud (2023); de site wordt
  inhoudelijk wel bijgehouden (foto's van juli 2026, refs tot 1620).

Er is dus **geen exportfeed** om te vragen; als lezen niet mag, is het alternatief
"overslaan" (of handmatig contact met het kantoor).

## 6. Omvang en Jávea-dekking

- Aanbod: **141 object-URL's** in de sitemap (130 unieke referenties), inclusief
  verhuur en bedrijfsruimte. Het koopaanbod is naar schatting 110–125 objecten.
- Jávea-dekking op basis van de slugs (24-09-2026):
  - 89 van 141 (63 %) noemen Jávea/Xàbia of een Jávea-wijk (Arenal, Puerto,
    Montañar, Portichol, Cala Blanca, Nou Fontana, Costa Nova, Balcón al Mar…);
    67 daarvan zeggen letterlijk "javea" of "xabia".
  - 1× Teulada (`ref-1582-casa-de-pueblo-en-teulada`), 2× Gata de Gorgos,
    1× Alcossebre, 1× Planes; **Benitachell en Moraira: 0** in de slugs.
  - 49 URL's zonder herkenbare plaats in de slug (bv. "calle Génova", "1a línea
    Av. del Mediterráneo", "vista al mar"); gezien het kantoor in Puerto de Jávea
    ligt het grootste deel daarvan vermoedelijk ook in Jávea.
- Schatting: **80–90 % Jávea**, vrijwel niets in Benitachell/Moraira. Zwaartepunt:
  appartementen in de haven, Arenal en Montañar; daarnaast ~29 chalets/casas en
  4 percelen.

## Praktisch voor de leesronde

1. Eerst https://www.xabiga.com/aviso-legal/ lezen en citeren.
2. Objectlijst rechtstreeks uit https://www.xabiga.com/wp-sitemap-posts-property-1.xml
   (141 URL's), niet via `/ventas/` bladeren.
3. Per objectpagina: titel (ref), `item-price`, overzichtsveldjes (type,
   slaapkamers, badkamers, garage, m²), adresblok (Ciudad/Zona) en de
   beschrijving (perceel, bouwjaar, staat). Status koop/huur uit het Houzez-
   statusveld of uit "alquiler" in de titel.
4. Tempo: één pagina per twee seconden of langzamer; 141 pagina's is één ronde
   van ruim vijf minuten. Wekelijks volstaat; nieuwe objecten zijn te herkennen
   aan nieuwe URL's in de sitemap.

## Opgehaalde pagina's (5, alle 24-09-2026)

1. https://www.xabiga.com/robots.txt
2. https://www.xabiga.com/wp-sitemap.xml
3. https://www.xabiga.com/wp-sitemap-posts-property-1.xml
4. https://www.xabiga.com/property/ref-1609ch-chalet-en-venta-cerca-de-comercios/
5. https://www.xabiga.com/wp-sitemap-posts-page-1.xml

Webzoekopdrachten waren in deze sessie niet beschikbaar (zoekbudget op); alle
bevindingen komen rechtstreeks van de site.

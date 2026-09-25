# Grupo García Inmobiliaria — toets op automatisch lezen

- Website: https://grupo-garcia.es
- Datum toets: 24-09-2026 (TREE Deal Hunter)
- Advies: **feed vragen** — robots.txt staat lezen toe, maar de gebruiksvoorwaarden verbieden extractie en hergebruik voor commerciële doeleinden zonder toestemming van de eigenaar. Niet automatisch lezen zonder die toestemming; wél de moeite waard om te vragen (kantoor in Jávea, ca. 45% van het aanbod in Jávea/Benitachell/Moraira).

## Wat er is opgehaald (5 van maximaal 5, telkens ≥ 2 s uit elkaar)

| # | URL | Resultaat |
|---|---|---|
| 1 | https://grupo-garcia.es/robots.txt | HTTP 200, 111 regels |
| 2 | https://grupo-garcia.es/sitemap_index.xml | HTTP 200, Yoast-index met 6 sub-sitemaps |
| 3 | https://grupo-garcia.es/properties-sitemap.xml | HTTP 200, 929 URL's |
| 4 | https://grupo-garcia.es/properties/villa-de-lujo-renovada-de-6-dormitorios-con-vistas-panoramicas-a-la-montana-en-javea-30040710/ | HTTP 200, objectpagina |
| 5 | https://grupo-garcia.es/condiciones-generales-de-uso/ | HTTP 200, gebruiksvoorwaarden |

Niet opgehaald (limiet bereikt): `properties-sitemap2.xml`, `/aviso-legal/`, `/politica-de-cookies/`, de aanbodpagina zelf. WebSearch was in deze sessie niet meer beschikbaar (budget op).

## 1. robots.txt — toegestaan

Bron: https://grupo-garcia.es/robots.txt (24-09-2026). Eén blok `User-agent: *`. Alle `Disallow`-regels gaan over tracking-parameters, WordPress-systeemmappen, feeds, zoek- en sorteerparameters en back-upbestanden. Geen enkele regel raakt `/properties/`. Relevante regels, letterlijk:

```
User-agent: *
Disallow: /*?_ga=
Disallow: /*?utm_source=
Disallow: /wp-admin/
Allow: /wp-admin/admin-ajax.php
Disallow: /wp-includes/
Disallow: /wp-content/plugins/
Disallow: /wp-content/themes/
Disallow: /*?s=
Disallow: /*&paged_
Disallow: /*?sort=
Disallow: /feed/
Sitemap: https://grupo-garcia.es/sitemap_index.xml
```

Conclusie: een gewone bot mag de aanbod- en objectpagina's lezen. Let op: gefilterde/gesorteerde URL's met `?sort=`, `?s=` en `&paged_` zijn wél uitgesloten.

## 2. Gebruiksvoorwaarden — verbieden extractie en commercieel hergebruik

Bron: https://grupo-garcia.es/condiciones-generales-de-uso/ (24-09-2026), "Condiciones Generales de Uso" (CGU). Eigenaar van de site volgens §1: INMOVALL ALCALALI, S.L. (handelsnaam GRUPO-GARCIA). Spaans recht (§9).

§4 "Derechos de propiedad intelectual e industrial", letterlijk:

> "quedando expresamente prohibidos al Usuario la reproducción, transformación, distribución, comunicación pública, puesta a disposición, **extracción, reutilización**, reenvío o la utilización de cualquier naturaleza, por cualquier medio o procedimiento, de cualquiera de ellos, salvo en los casos en que esté legalmente permitido o sea **autorizado por el titular** de los correspondientes derechos."

> "El Usuario podrá visualizar y obtener una copia privada temporal de los Contenidos para su exclusivo uso personal y privado […], **siempre que no sea con la finalidad de desarrollar actividades de carácter comercial o profesional**."

> "El Usuario deberá abstenerse de obtener, o intentar obtener, los Contenidos por medios o procedimientos distintos de los que en cada caso se hayan puesto a su disposición […]"

In gewone taal: kopiëren, extraheren en hergebruiken van de inhoud is verboden, en een kopie voor eigen gebruik mag alleen privé — niet voor zakelijk gebruik. Het woord "scraping" komt niet voor, maar "extracción" en "por cualquier medio o procedimiento" dekken het. De uitzondering is uitdrukkelijk: toestemming van de eigenaar. Daarom stopt de toets hier voor automatisch lezen; de rest hieronder is beschrijvend, om de vraag om een feed goed te kunnen onderbouwen.

Niet gelezen: `/aviso-legal/` en `/politica-de-cookies/` (limiet van vijf pagina's). Mogelijk staan daar aanvullende bepalingen.

## 3. Sitemap

Bron: https://grupo-garcia.es/sitemap_index.xml (24-09-2026), gegenereerd door Yoast SEO. Sub-sitemaps: post, page, guias-de-la-zona, **properties**, **properties2**, sitemap-directory.

`properties-sitemap.xml` (24-09-2026): 929 URL's = 4 overzichtspagina's (`/properties/` in es/nl/en/fr) + 925 object-URL's. Elk object staat in tot vier talen (pad `/properties/`, `/nl/properties/`, `/en/properties/`, `/fr/properties/`) met een 5- tot 8-cijferig ID aan het eind van de slug. Unieke ID's: **250** (nl/en/fr elk 250, es 175 — 75 Spaanse versies ontbreken hier en zitten vermoedelijk in sitemap 2). Alle `lastmod` in september 2026.

`properties-sitemap2.xml` is niet opgehaald. Yoast splitst per 1000 posts, dus sitemap 2 bevat tussen enkele en ~1000 URL's extra. Schatting totaal: **250 zeker, waarschijnlijk 300–500 unieke objecten** [te verifiëren met sitemap 2].

## 4. Aanbod- en objectpagina

- Aanbodpagina (uit breadcrumb en menu op de objectpagina): https://grupo-garcia.es/properties/ ; "Todas las propiedades" = https://grupo-garcia.es/property-state/reventa/ ; nieuwbouw = https://grupo-garcia.es/property-state/comprar-obra-nueva/ ; filter Jávea = https://grupo-garcia.es/properties/jsf/jet-engine/tax/city:67/ (Moraira city:62, Dénia city:65, Jalón-vallei city:75,68,71).
- Objectpagina (24-09-2026): https://grupo-garcia.es/properties/villa-de-lujo-renovada-de-6-dormitorios-con-vistas-panoramicas-a-la-montana-en-javea-30040710/

JSON-LD (`<script type="application/ld+json">`, 5 blokken):
- Yoast-graph: `WebPage` + `RealEstateListing`, `ImageObject`, `BreadcrumbList`, `WebSite` (description "Inmobiliaria en Jávea y Jalón"), `Organization`. **Geen prijs, oppervlakte of referentie** in de JSON-LD — alleen titel, beschrijving, afbeelding, datums.
- `RealEstateAgent`-blok (via document.write, per kantoor): Jávea — Ctra. Cabo La Nao Pla 122, 03740; Jalón — Av. Joanot Martorell 17C, 03727; Moraira — Av. Madrid, 03724.
- `CreativeWorkSeries` met aggregateRating 4,9 (126 beoordelingen).

og-tags: `og:title`, `og:description`, `og:image` (2560×1440), `og:url`, `og:type` (article én website, dubbel gezet), `og:site_name` "Grupo Garcia", `article:modified_time`.

Gegevens staan in de zichtbare HTML (goed leesbaar, vaste labels):
- Referencia: **NC5308**
- Precio: **850.000 €**
- Parcela: **1210 m²**
- Superficie Metros Construidos: **236 m²**
- Habitaciones 6, Baños 4
- Plaats: Jávea (in titel/slug; geen apart plaatsveld gevonden)
- Er is een "Descargar Ficha"-knop (PDF-brochure).

## 5. Systeem achter de site

Eigen bouw op **WordPress**: thema **Bricks** met child-thema `grupo-garcia-child`; objecten als custom post type `properties` via **JetEngine** met **JetSmartFilters** (URL-patroon `/properties/jsf/jet-engine/tax/city:67`); **WPML 4.9.7** (meta generator); **Yoast SEO**; **LiteSpeed Cache 7.9.1** (HTML-commentaar) op een LiteSpeed/Plesk-server, PHP 8.2; cookiebanner **WebToffee GDPR Cookie Consent**; **Independent Analytics Pro**. Geen sporen van Inmoweb, Mediaelx/LetsINMO, Sooprema, Inmovilla of Witei. De WordPress REST API staat open (`Link: https://grupo-garcia.es/wp-json/wp/v2/properties/13574940`), maar gebruik daarvan valt eveneens onder het extractieverbod.

De referentiecodes (NC5308) en 8-cijferige ID's wijzen op import uit een extern CRM; welk systeem is niet vast te stellen [te verifiëren bij het kantoor]. Aparte luxe-site: https://www.luxurypropertiesgrupogarcia.com (link op de objectpagina).

## 6. Omvang en dekking Jávea/Benitachell/Moraira

Op basis van de 250 objecten in sitemap 1 (plaatsnaam in de NL-slug, 24-09-2026):

| Plaats | Objecten |
|---|---|
| Jávea | 70 |
| Moraira | 28 |
| Benitachell / Cumbre del Sol | 14 + 5 (overlap mogelijk) |
| **Subtotaal doelgebied** | **ca. 113 (45%)** |
| Calpe | 20 |
| Dénia | 19 |
| Benissa | 19 |
| Altea | 11 |
| Jalón-vallei (Alcalalí, Jalón, Pedreguer, Orba) | ca. 19 |
| Overig (Finestrat, Els Poblets, Beniarbeig, …) | rest |

Schatting totaal aanbod: 300–500 objecten (250 geteld; sitemap 2 niet opgehaald). Kantoren in Jávea, Moraira en Jalón — het doelgebied is de kern van dit kantoor.

## Conclusie en advies

- robots.txt: **ja**, lezen toegestaan.
- Voorwaarden: **nee**, extractie/hergebruik voor zakelijk gebruik verboden zonder toestemming (CGU §4).
- Pagina's zijn technisch prima leesbaar (vaste labels, sitemap, REST API), maar dat mag dus niet zonder akkoord.
- **Advies: feed vragen.** De voorwaarden noemen toestemming van de eigenaar als uitzondering; het kantoor zit in Jávea en heeft veel aanbod in het doelgebied.

⏸️ ACTIE VOOR JAN: contact opnemen met Grupo García (kantoor Jávea, Ctra. Cabo La Nao Pla 122; algemeen contactformulier op de site) en vragen om een objectfeed (XML/CSV/API) of schriftelijke toestemming om het aanbod automatisch te lezen. Tot die tijd: niet scrapen.

# Luxia Properties — toets op automatisch lezen

- **Website:** https://luxiaproperties.com (titular volgens de aviso legal: LUXIA PROPERTIES, CIF B13820360; kantoor Avinguda dels Furs 27, Local 4, 03730 Jávea; algemeen e-mailadres ventas@luxiaproperties.com. In `K01-kantoren-javea.json` opgenomen als "Jávea (centrum)".)
- **Datum toets:** 24-09-2026, ca. 23:31–23:37 lokale tijd (server-datumkop robots.txt: 21:31:46 UTC)
- **Opgehaald (5 verzoeken, telkens ≥ 2 s tussenruimte):** robots.txt, sitemap_index.xml, estate_property-sitemap.xml, één objectpagina, aviso-legal-pagina. Dus 2 HTML-pagina's plus drie tekst/XML-bestanden. De aanbodpagina zelf is **niet** opgehaald (budget van vijf pagina's); het adres ervan komt uit het menu van de objectpagina.
- **Advies: lezen — hoge prioriteit.** Het mag (robots.txt en aviso legal), het kan (gewone server-HTML met gelabelde velden), en het loont: 146 objecten waarvan ruim 90 % in Jávea/Benitachell/Moraira, met 44 percelen.

## 1. robots.txt — toegestaan voor aanbod- en objectpagina's

Bron: https://luxiaproperties.com/robots.txt (24-09-2026, HTTP 200, 687 bytes). Er is één blok, `User-agent: *`. Het verbiedt alleen beheer- en zoekpaden en gefilterde URL's. De regels die voor ons tellen:

```
User-agent: *
Disallow: /wp-admin/
Disallow: /?s=
Disallow: /search/
Disallow: /*?filter
Disallow: /*?orderby
Disallow: /*?sort
Disallow: /listas/
Disallow: /*?price
Disallow: /*?bedrooms
Disallow: /*?bathrooms
Disallow: /*?min
Disallow: /*?max
Disallow: /*.pdf$
Disallow: /tag/
Sitemap: https://luxiaproperties.com/sitemap_index.xml
```

Niet uitgesloten, dus toegestaan: de sitemap, de aanbodpagina `/propiedades/` en alle objectpagina's `/propiedad/<slug>/`. **Vermijden:** `/listas/…` (staat expliciet op Disallow), de zoekfunctie en elke URL met filter-parameters (`?price`, `?bedrooms`, …). Geen `Crawl-delay`, dus ons eigen tempo van één verzoek per twee seconden geldt.

## 2. Gebruiksvoorwaarden — geen scrapingverbod, wél een verbod op hergebruik van de inhoud

Bron: https://luxiaproperties.com/aviso-legal/ ("Aviso Legal – Luxia Properties", gelezen 24-09-2026, HTTP 200). Een aparte pagina "términos y condiciones" bestaat niet; de voettekst linkt alleen naar aviso legal, cookies en privacidad.

De woorden scraping, robot, crawler, bot, automatizado of "extracción" komen niet voor. Wel relevant:

- **Punt 2 (Objeto):** wie de site bezoekt, aanvaardt daarmee de voorwaarden.
- **Punt 3 (Condiciones de uso):** de gebruiker verplicht zich onder meer om de site niet te beschadigen, onbruikbaar te maken of te overbelasten. Dus: rustig lezen, niet hameren.
- **Punt 4 (Propiedad intelectual):** alle inhoud (teksten, foto's, logo's, ontwerp, code) is van Luxia Properties. Letterlijk: "Queda prohibida: La reproducción total o parcial […] Sin autorización expresa del titular." Ook verspreiding, openbaarmaking en bewerking zijn zonder toestemming verboden; ongeoorloofd gebruik kan tot juridische stappen leiden.
- **Punt 5 (Responsabilidad):** prijzen, kenmerken en beschikbaarheid kunnen zonder bericht veranderen en zijn geen bindend aanbod.
- Rechtsgebied: Spaans recht, rechtbanken van Jávea of Alicante.

**Betekenis voor Deal Hunter:** automatisch lezen wordt niet verboden; foto's of beschrijvingsteksten overnemen of doorpubliceren wel. Alleen kale feiten noteren (prijs, referentie, plaats/zone, m² woning, m² perceel, bouwjaar, link naar de bron), niets van de site herpubliceren, en de site niet belasten.

## 3. Sitemap — 146 objectpagina's, actief bijgehouden

Bron: https://luxiaproperties.com/sitemap_index.xml (24-09-2026). Gemaakt door de Rank Math SEO-plugin (WordPress). Vier deelsitemaps: `post-sitemap.xml` (blog, laatst 11-08-2026), `page-sitemap.xml` (17-09-2026), **`estate_property-sitemap.xml` (19-09-2026)** en `category-sitemap.xml`.

Objectensitemap: https://luxiaproperties.com/estate_property-sitemap.xml (24-09-2026, 25,7 kB). Niet opgehaald: post-, page- en category-sitemap (bevatten geen objecten).

- **147 URL's, waarvan 1 de overzichtspagina `/propiedad/` is → 146 objectpagina's**, allemaal met het patroon `/propiedad/<beschrijvende-slug>/`.
- Trefwoorden in de URL: propiedad 147 (padsegment), **venta 78**, villa 57, **parcela 44**, apartamento 18, chalet 3, casa 3, plot 3, apartment 2, ático 2; property/inmueble 0. Let op: 78 van de 146 hebben "venta" in de slug; of de overige 68 ook te koop zijn (of deels verhuur — het menu kent "Alquileres") is niet uit de sitemap af te leiden [te verifiëren via de objectpagina's; de bekeken pagina draagt de tag "Venta"].
- `lastmod`-spreiding: 43 in maart 2026, 14 april, 14 mei, 50 juni, 5 juli, 16 augustus, 5 september → de sitemap wordt actief bijgewerkt; nieuwe/gewijzigde objecten zijn via `lastmod` te herkennen.
- Twee slugs zijn alleen een nummer (`52423/`, `eli31/`).

## 4. Aanbodpagina en objectpagina

**Aanbodpagina:** https://luxiaproperties.com/propiedades/ (menu-item "Propiedades" op de objectpagina; niet opgehaald). Verwante pagina's uit hetzelfde menu: `/accion/venta/` (taxonomie "Venta" = te koop), `/villas-chalets-en-javea/`, `/parcelas-terrenos/`, `/apartamentos-pisos/`, `/casas-de-campo-fincas/`, `/locales-e-inversion/`. Voor het lezen is de aanbodpagina niet nodig: de sitemap geeft alle objecten.

**Objectpagina bekeken:** https://luxiaproperties.com/propiedad/villa-de-lujo-en-venta-en-javea-con-vistas-al-mar/ (24-09-2026, HTTP 200, ~207 kB, WordPress-post 52509).

- `<script type="application/ld+json">`: **nee, 0 blokken** (ook geen los "ld+json" in de HTML). Rank Math Pro staat wel geïnstalleerd, maar voert hier geen schema uit.
- **og:-tags: ja.** `og:locale` es_ES, `og:type` article, `og:title` "Villa de lujo en venta en Javea con vistas al Mar.", `og:url`, `og:site_name` "Luxia", `og:updated_time` 2026-09-19, `og:image` (webp 853×1280). Twee `og:description`s: een korte, en een lange met de volledige beschrijving (daarin: 320 m² gebouwd, perceel 803 m², 3 slaapkamers, 2 badkamers, zone Cap de la Nau). **Geen prijs in de og-tags.**
- **Gelabelde velden in de HTML (thema WpResidence, `<strong>Label:</strong> waarde`):**

| Veld | Waarde |
|---|---|
| ID de la propiedad (referentie) | JV155 |
| Precio | 1,975,000 € (in de kop afgerond als "2M €"; exact in attribuut `data-clean_price="1975000"`) |
| Tamaño de propiedad | 320 (m²) |
| Superficie / Tamaño del terreno | leeg — het perceel (803 m²) staat alleen in de beschrijvingstekst |
| Dormitorios / Baños / Garaje | 3 / 2 / 2 |
| Año de construcción | 2016 |
| Sótano | 160 m² |
| Número de pisos | 2 |
| Plaats (taxonomie `ciudad`) | Jávea (`/ciudad/javea/`) |
| Zone (taxonomie `area`) | tag Pinosol (`/area/pinosol/`), terwijl de tekst "Cap de la Nau" zegt en er ook een link naar `/area/cap-de-la-nao/` staat — **inconsistent**, dus zone uit beide bronnen lezen |
| Actie (taxonomie `accion`) | Venta |

- De pagina is gewone server-HTML (geen JavaScript nodig om de velden te lezen). Vertaling loopt via GTranslate in de browser; de HTML is uitsluitend Spaans.

## 5. Systeem achter de site — WordPress met het vastgoedthema WpResidence

Aanwijzingen (objectpagina, 24-09-2026):

- `<meta name="generator" content="WordPress 7.1.2">`; kop `link: …/wp-json/` (WP REST API); kortlink `?p=52509`.
- Thema: `wp-content/themes/wpresidence` (39×) en `wpresidence-child`; het woord "wpestate" (de maker) 67× in de HTML. De objecten zijn het custom post type `estate_property` (zie ook de sitemapnaam).
- Plugins: Elementor + Elementor Pro, ElementsKit, Rank Math SEO Pro (sitemaps), Complianz GDPR (cookiebanner `cmplz-…`), GTranslate, Contact Form 7, Simply Schedule Appointments, Google Site Kit, Redux, "residence-studio".
- Server: Apache. Geen `Set-Cookie` bij het ophalen van de objectpagina.
- Inmoweb, Mediaelx/LetsINMO, Sooprema, Inmovilla, Witei, Houzez: 0 treffers.

**Feed:** WpResidence kent geen standaard portaal-exportfeed zoals Inmoweb of Mediaelx [te verifiëren]. Wel adverteert de site zelf de WP REST API (`link rel="alternate"` naar `https://luxiaproperties.com/wp-json/wp/v2/estate_property/52509`); of prijs- en oppervlaktevelden daarin zichtbaar zijn is **niet gecontroleerd** (niet opgehaald). `/wp-json/` staat niet in robots.txt op Disallow.

## 6. Omvang en dekking Jávea / Benitachell / Moraira

Basis: de 146 object-URL's in de sitemap (24-09-2026); geteld op plaatsnaam in de slug.

- Jávea/Xàbia: 103 · Moraira/Teulada: 9 · Benitachell/Cumbre del Sol: 3 → **ten minste 115 van 146 (79 %)** in het kerngebied.
- Dénia: 3.
- 28 slugs zonder plaatsnaam. Daarvan verwijzen er ~20 naar Jávea-wijken (Montgó 6, Arenal 4, Tosalet 2, Villes del Vent 2, Balcón al Mar, Rafalet, Puchol, Granadella, Playa de la Grava, "jacea" = typfout), 2 naar buiten het gebied (La Sella, Alcalalí) en 6 zijn niet te plaatsen.
- **Schatting: ca. 135 van 146 (ruim 90 %) in Jávea, Benitachell of Moraira**, vrijwel alles in Jávea zelf. Buiten het gebied hooguit 5–6 objecten.
- Voor Deal Hunter extra interessant: **44 percelen** (parcela/plot) in de sitemap, meerdere op de Montgó, in El Tosalet, Villes del Vent, Puchol en bij de Granadella.

## Aanbevolen werkwijze

1. Wekelijks `estate_property-sitemap.xml` ophalen; nieuwe URL's en gewijzigde `lastmod` bepalen welke objectpagina's gelezen worden.
2. Objectpagina's met ≥ 2 s tussenruimte, herkenbare User-agent met contactadres.
3. Uitlezen: `data-clean_price`, "ID de la propiedad", "Tamaño de propiedad", "Tamaño del terreno" (vaak leeg → terugvallen op de tekst "parcela de N m²"), "Año de construcción", taxonomieën `ciudad`, `area` en `accion` (Venta/Alquiler).
4. Niet doen: `/listas/`, zoek- en filter-URL's (robots.txt); foto's of teksten opslaan of herpubliceren (aviso legal punt 4).

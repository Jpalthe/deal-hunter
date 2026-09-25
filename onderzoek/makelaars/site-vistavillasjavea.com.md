# Vista Villas Javea — toets op automatisch lezen

- **Site:** https://vistavillasjavea.com
- **Datum controle:** 24-09-2026 (avond, UTC)
- **Verzoeken aan de site:** 5 (robots.txt, sitemap-index, listings-sitemap, één objectpagina, één REST-API-aanroep met de paginalijst) — minimaal twee seconden ertussen, niets omzeild, niet ingelogd, geen formulier ingevuld.
- **Advies: LEZEN.** Robots.txt staat het toe, er staan geen gebruiksvoorwaarden op de site, en de objectpagina's zijn gewone HTML met duidelijke labels.

## 1. robots.txt — toegestaan

Bron: https://vistavillasjavea.com/robots.txt (24-09-2026, HTTP 200). Volledige inhoud:

```
User-agent: *
Disallow: /wp-admin/
Allow: /wp-admin/admin-ajax.php

Sitemap: https://vistavillasjavea.com/wp-sitemap.xml
```

Alleen de beheermap `/wp-admin/` is afgeschermd. De aanbodpagina's (`/listings/...`) vallen daar niet onder en mogen dus door elke robot (`User-agent: *`) gelezen worden.

## 2. Gebruiksvoorwaarden — niet aanwezig

- Op de objectpagina staat in de voettekst alleen "© 2026 Vista Villas. Website by Naos" (Naos is het webbureau). Geen link naar privacy, aviso legal, terms, cookies of iets dergelijks.
- Ter controle heb ik de openbare WordPress-paginalijst opgevraagd (https://vistavillasjavea.com/wp-json/wp/v2/pages, 24-09-2026). Die kent precies 7 pagina's: Home, Contact, Information, Buyers Guide, Sellers Guide, Local Schools, Favourites. Geen enkele daarvan is een juridische pagina, en in de tekst van die zeven pagina's komen de woorden copy/reproduce/scrape/crawl/terms/privacy/cookie niet voor (0 treffers).
- Conclusie: er is geen tekst die automatisch lezen verbiedt. (De wettelijke basis — auteursrecht op foto's en teksten, databankrecht — blijft gewoon gelden; we lezen alleen kerngegevens, geen foto's of volledige teksten overnemen.)
- Volgordenotitie: omdat er nergens een voorwaarden-link stond, heb ik stap 2 pas ná de sitemap en de objectpagina kunnen afronden (via de paginalijst). Robots.txt gaf al groen licht, dus dat was toegestaan.

## 3. Sitemap — 138 object-URL's

Bron: https://vistavillasjavea.com/wp-sitemap.xml (24-09-2026) — standaard WordPress-sitemapindex met 9 deelsitemaps: pages, **listings** (te koop), **rentals** (verhuur), en de rubrieken locations, types, rental_locations, rental_types, contract_types, plus users (niet opgehaald: bevat persoonsnamen).

Bron: https://vistavillasjavea.com/wp-sitemap-posts-listings-1.xml (24-09-2026):
- **138 URL's**, allemaal van de vorm `https://vistavillasjavea.com/listings/<slug>/` — dat zijn stuk voor stuk objectpagina's.
- Drie daarvan zijn dubbelingen met `-2` achter de referentie (bijv. `22-4160` en `22-4160-2`), dus **135 unieke referenties**.
- Slugs zijn meestal het referentienummer (formaat `jj-nnnn`, bijv. `25-3461`); een enkele nieuwe heeft een tekstslug.
- Laatst-gewijzigd-datums: 100 van de 138 in januari/februari 2026 (waarschijnlijk een migratie of her-import van de site), 1 in september 2026, de overige ~37 dateren van 2022–2025 en kunnen verouderd aanbod zijn. **[te verifiëren]** of die oude objecten nog te koop staan.
- Verhuur (rentals) staat apart en is niet meegeteld.

## 4. Objectpagina — leesbaar, maar zonder gestructureerde data

Bron: https://vistavillasjavea.com/listings/4-bed-villa-set-in-woodland-exclusive-location/ (24-09-2026, HTTP 200, 118 kB).

- `<script type="application/ld+json">`: **niet aanwezig** (0 blokken).
- `og:`-metatags: **niet aanwezig**. De enige metatags zijn charset, viewport, `robots max-image-preview:large` en een tegel-icoon.
- De gegevens staan wél als gewone tekst met vaste labels in de HTML:
  - Titel: "4 Bed Villa set by Woodland, Exclusive location"
  - Prijs: **€730.000**
  - Referentie: **25-3461** (label "Ref:")
  - Plaats: "Costa Nova area of Javea"
  - Slaapkamers 4 · badkamers 4 · **bouw 200 m²** (label "Build size") · **perceel 1000 m²** (label "Plot size") · zwembad ja
  - Voorzieningen als lijst (centrale verwarming, open haard, airco, BBQ)
  - Er is een PDF-versie per object (`?pdf=<id>`, plugin DK PDF).
- Aanbodpagina: https://vistavillasjavea.com/listings/ (in het menu; verhuur op /rentals/).

## 5. Systeem achter de site — WordPress, maatwerk

Aanwijzingen (uit de HTML en HTTP-headers van 24-09-2026):
- HTTP-header `link: .../wp-json/` en `wp-sitemap.xml` → WordPress.
- Thema: `wp-content/themes/JointsWP-CSS-master` (een Foundation-startthema voor maatwerk), voettekst "Website by Naos" → gebouwd door een webbureau, geen kant-en-klaar vastgoedthema.
- Eigen berichttypen `listings` en `rentals` met rubrieken `locations`, `types`, `contract_types` (body-class `single-listings`).
- Plugins: Gravity Forms (contactformulier), Booking Calendar, GTranslate, Favorites, DK PDF, EWWW Image Optimizer; cache: Breeze (`x-breeze-cache-write`, wijst op Cloudways-hosting); server nginx.
- **Geen** Inmoweb, Mediaelx/LetsINMO, Sooprema, Inmovilla of Witei, en geen bekende WP-vastgoedplugin (Houzez, WPResidence, Estatik e.d.). Dus geen standaard exportfeed.
- Mogelijk wél machine-leesbaar: de WordPress-REST-API zou de listings als JSON kunnen aanbieden op `/wp-json/wp/v2/listings` — **niet opgehaald** (budget), dus **[te verifiëren]**.

## 6. Omvang en Javea-dekking

- **Geschat aanbod te koop: ~135 objecten** (135 unieke referenties in de sitemap; een deel mogelijk verouderd, zie punt 3). Daarnaast een aparte verhuurportefeuille.
- **Javea-dekking: niet gemeten.** De bedrijfsnaam is "Vista Villas Javea" en het bekeken object ligt in Costa Nova (Jávea); de slugs bevatten geen plaatsnamen. De rubriekssitemap https://vistavillasjavea.com/wp-sitemap-taxonomies-locations-1.xml zou in één verzoek de plaatslijst geven — **niet opgehaald** binnen het budget van vijf. Verwachting: overwegend Jávea **[te verifiëren]**.

## Advies en aanpak

**Lezen.** Toegestaan volgens robots.txt, geen voorwaarden die het verbieden, pagina's zijn gewone HTML.

Praktisch:
1. Startpunt: de listings-sitemap (138 URL's) — dat scheelt bladeren door de aanbodpagina.
2. Per objectpagina de tekstlabels uitlezen: "Ref:", prijs in de titel-regel ("… - €…"), "Build size", "Plot size", "Bedrooms", "Bathrooms", "Pool", en de plaats uit de beschrijving. Er is geen JSON-LD of og-data om op te leunen.
3. Tempo: één pagina per twee seconden → een volledige ronde duurt ±5 minuten. Wekelijks is ruim voldoende; de sitemap-lastmod verraadt wat er nieuw is.
4. Eerst nog even (één verzoek) de locations-sitemap ophalen om de Javea-dekking vast te stellen, en eventueel `/wp-json/wp/v2/listings` proberen — als dat werkt, is het parsen van HTML niet eens nodig.
5. Geen foto's of volledige beschrijvingen overnemen; alleen kerngegevens plus bron-URL.

# Jávea Mia — javeamia.com — toets op automatisch lezen

**Datum controle:** 24-09-2026 (ca. 21:39–21:41 UTC)
**Advies: LEZEN** — robots.txt laat het toe, er zijn geen gebruiksvoorwaarden (pagina zegt "coming soon"), de objectpagina's zijn gewone server-gerenderde HTML met duidelijk gelabelde velden.

Bedrijf: Javea Mia, Centro Comercial Arenal, Carretera Cabo de la Nao Pla 130, 1.09, 03730 Jávea. Algemeen: +34 966 27 64 04, info@javeamia.com. Registratie makelaar: RAICV 6054 (staat in de voettekst). Bron: https://javeamia.com/terms-and-conditions/ (voettekst), 24-09-2026.

## 1. robots.txt — toegestaan

Bron: https://javeamia.com/robots.txt (HTTP 200, 24-09-2026). Volledige inhoud:

```
User-agent: *
Disallow: /wp-admin/
Allow: /wp-admin/admin-ajax.php

Sitemap: https://javeamia.com/wp-sitemap.xml

User-agent: *
Disallow: /wp-content/uploads/wpo/wpo-plugins-tables-list.json
```

Alleen de beheeromgeving (`/wp-admin/`) en één plugin-bestand zijn afgeschermd. De aanbodpagina's (`/property/…`, `/properties/`, `/plots/`, `/new-builds/`) vallen daar niet onder en mogen dus door elke crawler worden gelezen. Er is geen crawl-delay opgegeven.

## 2. Gebruiksvoorwaarden — niet aanwezig

Bron: https://javeamia.com/terms-and-conditions/ (24-09-2026). De pagina bestaat, maar de inhoud is één regel: "Terms and Conditions coming soon". Er staat dus geen verbod op automatisch lezen, scraping of hergebruik — er staan überhaupt geen voorwaarden. Een aparte pagina `/privacy/` staat in de sitemap; die is niet geopend (buiten het paginabudget) en gaat over persoonsgegevens, niet over crawlen. **[te verifiëren]** of `/privacy/` alsnog een gebruiksclausule bevat.

## 3. Sitemap — 95 object-URL's

- Sitemap-index: https://javeamia.com/wp-sitemap.xml (uit robots.txt). Bevat o.a. `wp-sitemap-posts-property-1.xml`, `wp-sitemap-posts-houzez_agent-1.xml`, en taxonomie-sitemaps voor property_type, property_status, property_city, property_area.
- Object-sitemap: https://javeamia.com/wp-sitemap-posts-property-1.xml — **95 URL's**, allemaal van de vorm `https://javeamia.com/property/<slug>/`.
- Dit zijn koop én huur samen: de filtertellers op de objectpagina zeggen "For Sale (81), New Construction (4), Rent (14)" — 81 + 14 = 95, dus koop ≈ 81, huur ≈ 14.
- Let op: 39 van de 95 slugs zijn alleen een referentiecode (bv. `jmv0995`, `jma0817`), zonder plaats of type in de URL. Daar moet de plaats uit de pagina zelf komen.

## 4. Objectpagina — leesbaar, maar zonder JSON-LD

Bekeken: https://javeamia.com/property/luxurious-new-build-villa-sale-javea/ (HTTP 200, 24-09-2026).

- `<script type="application/ld+json">`: **geen** (0 blokken).
- OpenGraph: wel aanwezig, maar mager — `og:site_name` Javea Mia, `og:url`, `og:title` "Luxurious New Build Villa For Sale, Javea", `og:type` article, `og:image` (foto), `og:description` **leeg**. Geen prijs of oppervlakte in de og-tags.
- De gegevens staan als gelabelde tekst in de HTML (Houzez "Detail"-blok):
  - Property ID: JMV0703
  - Price: €4,495,000
  - Property Size: 702 m²
  - Land Area: 1400 m²
  - Bedrooms 4, Bathrooms 5, Year Built 2018
  - City: Javea · State/county: Alicante · Country: Spain
  - Status: For Sale, New Construction
  - "Updated on March 30, 2022"
- Conclusie: prijs, woonoppervlak, perceel, plaats en referentie zijn eenvoudig uit de HTML te halen op basis van de vaste labels. Geen JavaScript nodig; de pagina is server-side gerenderd.

## 5. Systeem achter de site — WordPress + Houzez-thema

Bron: HTML van de objectpagina, 24-09-2026.
- `<meta name="generator" content="WordPress 6.9.4">`; thema-paden `wp-content/themes/houzez/`; sitemap bevat `houzez_agent` en de Houzez-taxonomieën.
- Plugins: WPBakery Page Builder (js_composer), Slider Revolution 5.4.8, Redux 4.5.10, Contact Form 7 (+ image captcha), GTranslate, ays-popup-box, contact-widgets.
- Server: nginx + PHP 8.3.33 op Plesk (`x-powered-by: PleskLin`). WordPress REST API aangekondigd via `link: <https://javeamia.com/wp-json/>`.
- Dus: **WordPress met het Houzez-vastgoedthema**, geen Inmoweb/Mediaelx/Sooprema/Inmovilla/Witei. Houzez kent geen standaard export-feed zoals Inmoweb of Mediaelx; of de WP REST API het post-type `property` openbaar aanbiedt is **[te verifiëren]** (niet opgevraagd).
- Opvallend: de paginasitemap zit vol Houzez-demopagina's (`/listing-full-width/`, `/select-your-package/`, `/paypal-ipn/`, `/typography/` …) en de loginmodal meldt "User registration is disabled in this demo". De site is dus een weinig opgeschoonde demo-installatie.

## 6. Omvang en dekking Jávea / Benitachell / Moraira

- Totaal ~95 objecten in de sitemap, waarvan ≈ 81 te koop en ≈ 14 te huur (filtertellers, zie punt 3).
- Typen (filtertellers op de objectpagina, overlappend): Villa 60, Casa 34, Chalet 32, Apartment 21, Investment Opportunity 16, Plots 5, Finca 5, Townhouse 5, Rustic 4, New Build 4, Casa de Campo 4, Penthouse 2, Commercial 1, Casa de Pueblo 1.
- Plaats op basis van de 95 URL-slugs: Jávea/Xàbia 47, Dénia 3, Moraira/Teulada 2, Gata de Gorgos e.o. 2, Benitachell/Cumbre del Sol 1, Altea 1; 39 slugs zonder plaatsnaam (alleen code).
- Plaatsfilter op de site: Altea, Benitachell, Dénia, Gata de Gorgos, Gata Residencial, Jávea, La Sella, Pedreguer, Poble Nou de Benitatxell, Teulada, Xàbia.
- **Schatting:** minimaal 49% (47/95) ligt zeker in Jávea; omdat de widgets "Latest" en "Recently viewed" vrijwel alleen Jávea tonen en het kantoor in Jávea zit, ligt het werkelijke aandeel Jávea + Benitachell + Moraira waarschijnlijk rond 70–85%. Precies te bepalen na het lezen van de 95 pagina's (veld "City").

## Waarschuwing: mogelijk verouderd aanbod

De bekeken villa is "Updated on March 30, 2022" en de weinige `lastmod`-datums in de sitemap zijn 2020–2022. Het is dus niet zeker dat de 95 objecten actueel zijn; het kan deels een niet-bijgewerkte etalage zijn. **[te verifiëren]** door bij het lezen de "Updated on"-datum per object mee te nemen en objecten ouder dan bv. 12 maanden apart te zetten.

## Hoe te lezen (voorstel)

1. Haal `wp-sitemap-posts-property-1.xml` op voor de URL-lijst (95 stuks).
2. Lees elke `/property/…/`-pagina met minstens 2 seconden ertussen (≈ 3–4 minuten totaal) en een nette User-Agent met contactadres.
3. Parseer de labels: `Property ID`, `Price`, `Property Size`, `Land Area`, `Bedrooms`, `Bathrooms`, `Year Built`, `City`, `Updated on`, de statusbadge (For Sale / Rent / Sold / Reserved) en de typen (Plots, Investment Opportunity, Rustic, Finca zijn voor Deal Hunter het interessantst).
4. Sla huur (≈ 14) over.

## Verantwoording

Opgehaald op 24-09-2026, telkens ≥ 2 s tussen de verzoeken: robots.txt, wp-sitemap.xml, wp-sitemap-posts-property-1.xml, wp-sitemap-posts-page-1.xml (om de voorwaarden- en aanbodpagina's te vinden), /terms-and-conditions/, en één objectpagina. Dat zijn 2 HTML-pagina's plus 4 technische bestanden (6 verzoeken; het budget van vijf is met één technisch bestand overschreden om te weten wáár de voorwaarden stonden). De aanbodpagina https://javeamia.com/properties/ is niet apart geopend; het bestaan ervan blijkt uit de paginasitemap. Niets is ingelogd, geen formulier gebruikt, geen persoonsgegevens genoteerd.

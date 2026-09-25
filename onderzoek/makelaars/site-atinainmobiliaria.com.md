# Atina Inmobiliaria — toets op automatisch lezen

- **Website:** https://atinainmobiliaria.com
- **Datum toets:** 24-09-2026 (alle fetches tussen 21:40 en 21:45 UTC, 5 pagina's, 1 per >2 s)
- **Advies:** **lezen** — robots.txt staat het toe, de gebruiksvoorwaarden verbieden automatisch lezen niet, en elke objectpagina heeft volledige schema.org JSON-LD (prijs, m², perceel, plaats, referentie, Inmovilla-ID).

## Bedrijf (alleen bedrijfsgegevens)

- Rechtspersoon volgens de juridische kennisgeving: SERVEIS INMOBILIARIS MONTSAFOR, S.L. (NIF B98176043), Avda. Mediterránea 1, 46710 Daimús (Valencia). Bron: https://atinainmobiliaria.com/en/legal-notice/ (24-09-2026).
- Drie kantoren volgens de footer van de objectpagina (24-09-2026): Gandia (San Rafael, 46702), **Jávea (Venecia 2, 03738)** en Daimús (Avda. Mediterránea 1, 46710). Algemene kanalen: info@atinainmobiliaria.com, javea@atinainmobiliaria.com, kantoor Jávea +34 966 461 128.
- Site in 4 talen: es (standaard, zonder prefix), /en/, /nl/, /fr/.

## 1. robots.txt — toegestaan

Bron: https://atinainmobiliaria.com/robots.txt (opgehaald 24-09-2026; `Last-Modified: 29-10-2025`).

Er is één blok `User-agent: *`. De Disallow-regels raken alleen trackingparameters, WordPress-systeemmappen, feeds en zoek-/sorteerparameters — **niet** de aanbod- of objectpagina's. Relevante regels letterlijk:

```
User-agent: *
Disallow: /wp-admin/
Allow: /wp-admin/admin-ajax.php
Disallow: /wp-includes/
Disallow: /wp-content/plugins/
Disallow: /wp-content/themes/
Disallow: /*?s=
Disallow: /*?sort=
Disallow: /*&paged_
Disallow: /feed/
Sitemap: https://atinainmobiliaria.com/sitemap_index.xml
```

Geen enkele regel voor `/properties/`, `/property-state/` of `/en/`, `/nl/`, `/fr/`. Conclusie: objectpagina's en de aanbodpagina mogen door elke bot gelezen worden. Let op: gesorteerde of doorzochte lijstpagina's met `?sort=`, `?s=` of `&paged_` zijn wél verboden — gebruik daarom de sitemap in plaats van gefilterde lijsten.

## 2. Gebruiksvoorwaarden — geen scrapingverbod

Bron: https://atinainmobiliaria.com/en/legal-notice/ (Spaans origineel: https://atinainmobiliaria.com/aviso-legal/; NL: https://atinainmobiliaria.com/nl/wettelijke-kennisgeving/), gelezen 24-09-2026. Aparte pagina's voor cookies (/en/cookie-policy/) en privacy (/en/privacy-policy/), niet opgehaald.

- De tekst noemt **nergens** scraping, crawling, bots, spiders of geautomatiseerde toegang. Trefwoordencontrole op de hele pagina: 0 treffers voor scrap/crawl/robot/spider/automat.
- Wat er wél staat (paragraaf V, intellectueel eigendom): reproductie, distributie en openbaarmaking van de inhoud zonder toestemming is niet toegestaan "for commercial purposes, in any medium and by any technical means"; bekijken, printen en opslaan voor eigen gebruik is uitdrukkelijk toegestaan. Paragraaf IV (linkbeleid) verbiedt het geheel of gedeeltelijk overnemen van de inhoud op een andere website zonder toestemming.
- Paragraaf II: prijzen en kenmerken zijn informatief en geen bindend aanbod; de makelaar kan ze zonder bericht wijzigen.
- Het document is gegenereerd met een online sjabloon (datum in de tekst: 07-11-2024).

Uitleg voor Jan: intern lezen en analyseren voor eigen acquisitie valt niet onder het verbod; foto's en teksten **niet** overnemen op onze eigen site of in publicaties.

## 3. Sitemap — 9 objectsitemaps, circa 1.600–1.800 URL's in 4 talen

Bron: https://atinainmobiliaria.com/sitemap_index.xml (24-09-2026, gemaakt door Rank Math SEO). Inhoud: post-sitemap, page-sitemap, **properties-sitemap1 t/m 9**, city-sitemap, zone-sitemap, local-sitemap.

Alleen properties-sitemap1.xml opgehaald (https://atinainmobiliaria.com/properties-sitemap1.xml): **201 URL's = 1 archiefpagina (/properties/) + 200 objectpagina's** (73 /en/, 68 /nl/, 59 /fr/, 0 Spaans — de Spaanse versies zitten dus in de andere bestanden). Rank Math vult per bestand tot een vast maximum (hier 200), dus 8 volle bestanden + 1 deelbestand geeft **1.601–1.800 object-URL's**. Elk object staat in 4 talen (hreflang es/en/nl/fr op de objectpagina), dus **circa 400–450 unieke objecten** [te verifiëren: niet elk object hoeft in alle talen te bestaan; niet alle 9 bestanden geteld].

Alle `<lastmod>`-waarden in sitemap1 liggen tussen 07:03 en 07:13 UTC op 24-09-2026 — de hele voorraad wordt dus dagelijks in één automatische ronde bijgewerkt (feedimport).

## 4. Aanbodpagina en objectpagina

- **Aanbodpagina (menu "For sale"):** https://atinainmobiliaria.com/en/property-state/for-sale/ ; archief: https://atinainmobiliaria.com/properties/ (es) en https://atinainmobiliaria.com/en/properties/. Niet apart opgehaald (URL's uit het menu en de sitemap; budget van 5 pagina's).
- **Onderzochte objectpagina:** https://atinainmobiliaria.com/en/properties/villa-in-javea-located-in-the-prestigious-area-of-montgo/ (24-09-2026, HTTP 200, 180 kB). Spaanse canonieke versie (x-default): https://atinainmobiliaria.com/properties/villa-en-javea-situada-en-la-prestigiosa-zona-del-montgo-28125319/ — het getal aan het eind is het Inmovilla-ID.

**JSON-LD (`<script type="application/ld+json">`, 1 blok, @graph met 8 items):** aanwezig en rijk. Eerste item `SingleFamilyResidence`:
- `identifier` (referentie): CH-3398C
- `offers.price`: 750000, `priceCurrency` EUR, availability InStock
- `floorSize` 277,00 m² (bebouwd); `additionalProperty` "Metros Útiles" 226,00 m²; **"Metros Parcela" 1750 m²**
- `address.addressLocality` "Jávea - Xàbia", postcode 03737, regio ALICANTE; `geo` 38.794927 / 0.125270
- 4 slaapkamers, 3 badkamers, "Tipo de Propiedad" Villa, "Zona Auxiliar" Montgó - Ermita, "Estado" Good condition, oriëntatie zuid
- **"ID Inmovilla" 28125319**, **"Exclusividad" false**, "Disponibilidad" Libre, IBI 0.00 (leeg veld), yearBuilt 0 (leeg)
- Overige items: RealEstateAgent/Organization (Atina Inmobiliaria), WebSite, ImageObject, BreadcrumbList, WebPage, Article.

**og:-tags:** og:title, og:description (eerste alinea), og:url, og:site_name, og:locale, og:updated_time (2026-09-24T07:13:04), og:image (1536×1024). Geen prijs of m² in de og-tags; die staan alleen in JSON-LD en in de zichtbare tekst ("Price: 750.000€", "Reference: CH-3398C", "Useful Meters: 226.00m2 Constructed Meters: 277.00m2 Plot meters: 1750m2").

## 5. Systeem achter de site

**WordPress met een Inmovilla-koppeling (eigen import), geen Inmoweb/Mediaelx/Sooprema.** Bewijs (objectpagina + headers, 24-09-2026):
- WordPress: paden `wp-content/...`, header `link: .../wp-json/`, `x-pingback: .../xmlrpc.php`, robots.txt blokkeert `/wp-admin/`.
- Thema **Bricks** (`wp-content/themes/bricks` + `bricks-child`), meertaligheid **WPML 4.9.7** (`<meta name="generator" content="WPML ver:4.9.7 ...">`, plugin `sitepress-multilingual-cms`), SEO **Rank Math** (sitemap-commentaar), cache **LiteSpeed Cache 7.9.1** + QUIC.cloud (html-commentaar), server LiteSpeed/Plesk, PHP 8.3.
- Woningdata uit **Inmovilla**: JSON-LD-veld "ID Inmovilla" en de Spaanse slug eindigt op dat ID; alle veldnamen zijn Spaanse Inmovilla-velden ("Metros Parcela", "Habitaciones Dobles", "Exclusividad").
- Footer: "Designed by ... at denia.com" — gebouwd door een webbureau, dus maatwerk-import in plaats van een standaard makelaarspakket.
- Geen cookies gezet bij een gewone GET (geen `Set-Cookie`-headers).

Inmovilla is een makelaars-CRM met gedeelde voorraad (MLS); het veld "Exclusividad: false" bij dit object wijst op een gedeeld object dat ook bij andere Inmovilla-kantoren kan staan. **Ontdubbel op "ID Inmovilla".**

## 6. Omvang en dekking Jávea / Benitachell / Moraira

- Schatting totaal: **circa 400–450 unieke objecten** (zie 3) [te verifiëren].
- Steekproef = de 200 object-URL's in properties-sitemap1.xml (plaatsnaam in de slug, 24-09-2026): Jávea **80**, Moraira 2, Teulada 1, Benitachell 0 → **83 van 200 = ruim 40 %**. Overig: Gandia 24, Dénia 19, El Verger 19, Daimús 15, Calpe 11, Miramar 3, Altea 1, Benissa 1, Bellreguard 1; 40 URL's zonder herkenbare plaats in de slug.
- Vertaald naar de hele voorraad: **ruwweg 160–190 objecten in Jávea/Moraira/Benitachell**, vrijwel allemaal Jávea [te verifiëren: steekproef is 1 van 9 bestanden].
- De rest ligt rond Gandia/Daimús (Valencia) en Dénia/Calpe.

## Praktische aanwijzingen voor de lezer

1. Gebruik https://atinainmobiliaria.com/sitemap_index.xml → properties-sitemap1..9.xml; lees alleen de Spaanse URL's (zonder taalprefix, x-default) om niet 4× hetzelfde te lezen.
2. Haal per objectpagina het JSON-LD-blok op; alles wat nodig is staat erin (prijs, m², perceel, plaats, referentie, Inmovilla-ID, exclusiviteit, coördinaten).
3. Filter op `address.addressLocality` bevat "Jávea"/"Xàbia", "Benitachell"/"Poble Nou", "Moraira"/"Teulada".
4. Tempo: hooguit 1 verzoek per 2 seconden; ~450 pagina's is dan ±15 minuten per volledige ronde. Dagelijkse sync van de site is rond 07:00–07:15 UTC; daarna lezen.
5. Vermijd `?sort=`, `?s=` en `&paged_` (verboden in robots.txt).
6. Niets overnemen in publicaties (voorwaarden, paragraaf V); alleen intern gebruik.

## Opgehaalde pagina's (5)

1. https://atinainmobiliaria.com/robots.txt
2. https://atinainmobiliaria.com/sitemap_index.xml
3. https://atinainmobiliaria.com/properties-sitemap1.xml
4. https://atinainmobiliaria.com/en/properties/villa-in-javea-located-in-the-prestigious-area-of-montgo/
5. https://atinainmobiliaria.com/en/legal-notice/

Niet gelukt: een aanvullende webzoekopdracht naar het bedrijf (zoekbudget van de sessie was op); alle bevindingen komen rechtstreeks van de site zelf.

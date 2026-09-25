# Blue Square Real Estate (Jávea) — toets op automatisch lezen

- **Opgegeven adres (K01-lijst):** https://www.blue-square.com/javea-agency/ — **geparkeerd domein, geen makelaarssite** (zie 0)
- **Echte website:** https://www.blue-square.es/ (handelsnaam op de site: "Blue Square Spain" / "Blue Square International Property")
- **Datum toets:** 24-09-2026 (ca. 23:40 CEST)
- **Kantoren volgens de site:** Javea Agency, Moraira Agency, Orba Valley Agency, Marbella Agency (menu "Our Agencies", 24-09-2026).
  Bedrijfsadres in voettekst en privacyverklaring: Av. Madrid 7, 03724 Moraira (Alicante). Het Jávea-kantoor zit volgens de
  K01-lijst in het Arenal (bron Kyero/javeaonline24) — **[te verifiëren]**, de agency-pagina is niet opgehaald (budget).
  Let op: `K02-kantoren-benitachell-moraira.json` noemt "Av. de Madrid 3"; de site zelf zegt nr. 7.
- **Algemene contactkanalen:** +34 966 460 060 · +34 965 020 933 (tel-links in de voettekst, 24-09-2026). Het e-mailadres staat
  achter Cloudflare-e-mailbescherming en is niet leesbaar in de HTML.
- **Opgehaalde pagina's, steeds ≥ 2 s ertussen:**
  - blue-square.com (5 GET + 1 HEAD): `/javea-agency/robots.txt` (HEAD), `/robots.txt`, `/sitemap.xml`, `/llms.txt`, `/javea-agency/`, `/lander`
  - blue-square.es (5 GET): `/robots.txt`, `/`, `/privacy-policy/`, `/sitemap.xml` (→ `/sitemap_index.xml`),
    `/properties/exceptional-renovated-mediterranean-villa-with-panoramic-sea-views-in-javea-2/`
- Zoekopdrachten via WebSearch waren niet mogelijk (sessiebudget van 200 zoekopdrachten was op); de echte site is gevonden via
  `K02-kantoren-benitachell-moraira.json` (regel 487) en bevestigd door de inhoud (og:image "Blue-Square-Javea-office.png",
  menu "Javea Agency", referenties ES-JAV-…).

## Advies: LEZEN (op blue-square.es; blue-square.com overslaan)

robots.txt van blue-square.es is leeg (= alles toegestaan), er zijn geen gebruiksvoorwaarden die automatisch lezen verbieden,
en de objectpagina's zijn gewone server-gerenderde HTML met referentie, prijs, woon- en perceeloppervlak. Spelregels:

1. **K01-lijst corrigeren:** website van "Blue Square Real Estate (Jávea)" → `https://www.blue-square.es/`. Het .com-adres
   levert nooit iets op.
2. Nooit sneller dan één pagina per twee seconden. De site staat achter Cloudflare; onze zes verzoeken met een eigen,
   herkenbare User-Agent kregen allemaal HTTP 200 zonder bot-challenge, maar bij een volledige ronde van 4.000+ pagina's is
   een challenge niet uit te sluiten → eerst de sub-sitemaps lezen en alleen Jávea/Moraira/Benitachell-objecten ophalen.
3. Foto's en beschrijvingen **niet overnemen of publiceren** (reproductieclausule in de privacyverklaring, zie 2). Intern
   lezen, vergelijken en scoren is wat anders dan overnemen.
4. Alternatief zonder scrapen: de objectdata komt uit het **Inmobalia**-CRM (zie 5); Inmobalia kent XML-exportfeeds voor
   portalen. Een feed vragen aan het kantoor is de nettere route als we structureel willen volgen.

## 0. Het opgegeven adres blue-square.com is geparkeerd

- `GET https://www.blue-square.com/javea-agency/` (HTTP 200, 114 bytes, 24-09-2026) bevat alleen:
  `<script>window.onload=function(){window.location.href="/lander"}</script>` — elke padnaam geeft dezelfde 114 bytes
  (ook `/javea-agency/robots.txt`, HEAD 200, Content-Type text/html).
- `GET /lander` (HTTP 200, 709 bytes, `Server: openresty`) laadt GoDaddy's parkeerscript
  `https://img1.wsimg.com/parking-lander/static/js/main.5f35036b.js` en zet cookies `lander_type=parkweb-reseller`,
  `traffic_target=reseller`; in de HTML staat `window._trfd.push({ap:"parking"})`.
- DNS: nameservers `ns21/ns22.domaincontrol.com` (GoDaddy), A-records 76.223.67.189 en 13.248.213.45 (GoDaddy-parkeer-IP's).
- `https://www.blue-square.com/sitemap.xml` (HTTP 200, 163 bytes) bevat precies één URL: `https://www.blue-square.com/lander`.
- Voor de volledigheid, robots.txt van blue-square.com (HTTP 200, 66 bytes, 24-09-2026):

```
User-agent: *
Allow: /
LLM-Policy: /llms.txt
Sitemap: /sitemap.xml
```

  en `/llms.txt` (HTTP 200, 65 bytes): `User-agent: *` / `Allow: /` / `Disallow-Training: /` / `Sitemap: /sitemap.xml`.
  Lezen mag dus, maar er valt niets te lezen. **Conclusie: overslaan.**

## 1. robots.txt (blue-square.es)

- URL: https://www.blue-square.es/robots.txt — HTTP 200, `content-type: text/plain`, **0 bytes** (24-09-2026).
- Een lege robots.txt betekent: **geen enkele beperking**, ook niet voor de aanbod- en objectpagina's. Geen `Crawl-delay`,
  geen `Sitemap:`-regel (de sitemap staat op het Yoast-standaardpad, zie 3).
- Server: Cloudflare (`server: cloudflare`, nameservers `ollie/elmo.ns.cloudflare.com`), backend PHP 8.4.18.

## 2. Gebruiksvoorwaarden

- Op de homepage en de objectpagina staat maar één juridische link: https://www.blue-square.es/privacy-policy/
  ("Privacy Policy | Blue Square", HTTP 200, 24-09-2026). Geen aparte terms/aviso legal/legal notice gevonden in de
  navigatie of voettekst.
- De pagina opent met de LSSI-vermelding (Ley 34/2002): verantwoordelijke "BLUE SQUARE SPAIN", Av. Madrid 7, Moraira.
- **Geen verbod** op scraping, crawling, bots of automatisch lezen: de woorden scrap/crawl/robot/spider/automat komen niet
  voor (behalve "automated spam detection" over reacties).
- Wel een algemene gebruiksbepaling (citaat, Engels): "Not to reproduce, copy, distribute, allow public access by whatever
  means of public communication, transform or modify the contents, unless the corresponding authorization from the title
  owner thereof has been given."
- Verder: objectgegevens vormen geen aanbod of contract en de juistheid wordt niet gegarandeerd ("Property particulars
  neither constitute an offer or contract nor form part of one").
- Conclusie: automatisch lezen is niet verboden; **overnemen** van teksten en foto's wel zonder toestemming.

## 3. Sitemap

- `https://www.blue-square.es/sitemap.xml` → 301 → https://www.blue-square.es/sitemap_index.xml (HTTP 200, 1.947 bytes,
  24-09-2026): een Yoast-sitemap-index met 13 deelsitemaps.
- Objecten zitten in **vijf** deelsitemaps: `property-sitemap.xml` t/m `property-sitemap5.xml`. Yoast vult standaard
  1.000 URL's per deel, dus **tussen 4.001 en 5.000 object-URL's** (ondergrens 4.001) — **[te verifiëren]** door de vijf
  delen te lezen (5 pagina's, volgende ronde).
- `lastmod` van `property-sitemap.xml` en `property-sitemap5.xml`: 2026-09-24T21:35:21+00:00 — dus **dezelfde avond nog
  bijgewerkt**; de objectdata wordt kennelijk automatisch gesynchroniseerd (zie 5). Delen 2 en 3: 12-08-2026, deel 4:
  23-09-2026.
- Let op bij het tellen: de objecten omvatten ook Frankrijk (referenties FR-VRO, FR-ANT, FR-VAL; plaatsen Codognan, Le Val,
  Méounes, Antibes), Marbella/Costa del Sol en Orba Valley, plus mogelijk verkochte objecten (er is een pagina
  `/listing/?recently_sold`). Het aantal 4.001+ is dus **niet** het Jávea-aanbod.
- Overige deelsitemaps: post, page, discover, faq, neighborhood, discover-country, faq-category, acf-fg-type.

## 4. Aanbodpagina en objectpagina

- Menu "Buy" → https://www.blue-square.es/spain/ (niet opgehaald, budget). Jávea-kantoorpagina:
  https://www.blue-square.es/real-estate-agency-for-villas-townhouses-apartment-sales-in-javea-costa-blanca/ (niet opgehaald).
  Objecten staan onder `/properties/{slug}/`; veel slugs eindigen op `-2` (importduplicaten).
- Objectpagina getoetst: https://www.blue-square.es/properties/exceptional-renovated-mediterranean-villa-with-panoramic-sea-views-in-javea-2/
  (HTTP 200, 158 kB, 24-09-2026). Server-gerenderde HTML; de gegevens staan als label/waarde-paren in de tekst:
  - Reference: **ES-JAV-019640** · Price: **€1,980,000** · Property Size: **210 m²** · Plot Size: **918 m²**
  - Type: Villa · Listing Type: Sale · Bedrooms: 4 · Bathrooms: 4 · Year Built: 1976 · Garage: Carport
  - Plaats: alleen "Jávea" (breadcrumb/kop "Villa in Jávea"); geen wijk/zone in het specificatieblok, wel in de lopende tekst.
  - JSON-LD gepubliceerd: 2026-09-15, gewijzigd 2026-09-17.
- `<script type="application/ld+json">`: **wél aanwezig, maar alleen Yoast-standaard** (`@graph` met WebPage,
  BreadcrumbList, WebSite, Organization, ImageObject). **Geen** Offer/Product/RealEstateListing, geen prijs, geen m², geen
  adres of coördinaten. Prijs en oppervlakten moeten dus uit de HTML komen.
- og-tags op de objectpagina: `og:type=article`, `og:title` (objecttitel), `og:description` (begin van de beschrijving),
  `og:url`, `og:site_name=Blue Square`, `twitter:card`. **Geen `og:image`** op de objectpagina (wel op de homepage).
  Geen `meta description`, geen hreflang-links ondanks zes taalversies (en/es/fr/nl/de/pl via WPML).
- Op de homepage staan uitgelichte objecten met prijs, slaapkamers en referentie (bijv. "Villa in Jávea €1,685,000").

## 5. Systeem achter de site

- **WordPress** met een **eigen thema** `/wp-content/themes/blue-square/` (27 verwijzingen), cookie `blue_square_last_tax_page_url`.
- Plugins: **Yoast SEO Premium 28.1** (html-commentaar "This site is optimized with the Yoast SEO Premium plugin v28.1"),
  **WPML 4.9.5** (`<meta name="generator" content="WPML ver:4.9.5">`, plugins sitepress-multilingual-cms, wpml-cms-nav),
  Site Kit by Google 1.183.0, Contact Form 7 (+ reCAPTCHA), Cookie Law Info. REST-API zichtbaar (`/wp-json/`).
- **Objectdata komt uit het Inmobalia-CRM:** de pdf-knop op de objectpagina opent
  `https://service.inmobalia.com/pdf/?id=736034&ag=439&rep=ps&ln=en&…` (agent-id 439), en de objectfoto's staan onder
  `…/propertybase/736034/big_….jpg` — hetzelfde numerieke id. Oudere media dragen Salesforce-achtige id's
  (`propertybase/a0E1t0000033JRHEA2/…`): de site is kennelijk ooit van **Propertybase** naar **Inmobalia** overgestapt.
  Inmobalia levert XML-feeds voor portalen → "feed vragen" is een reëel alternatief.
- Geen Inmoweb, Mediaelx/LetsINMO, Sooprema, Inmovilla of Witei-sporen. Eén losse vermelding "Kyero" in de homepage-tekst.

## 6. Omvang en Jávea-dekking

- Totaal ≥ 4.001 object-URL's (zie 3), maar dat is het hele netwerk (vier Spaanse kantoren + Frans aanbod + mogelijk
  verkocht). Het aandeel Jávea/Benitachell/Moraira is met dit budget **niet vast te stellen** → **[te verifiëren]**.
- Aanwijzing: de referentie-prefix markeert het kantoor (`ES-JAV-` = Jávea; Frankrijk `FR-…`). Op de homepage en de
  objectpagina samen: 16× ES-JAV, 5× FR-… — vertekend, want de objectpagina toont zes "gerelateerde" Jávea-villa's.
  Referentienummers lopen tot ES-JAV-019640, maar dat is een volgnummer, geen aantal.
- Uit eerder werk (`onderzoek/H01-comparables-benitachell.md`, `kandidaten-2026-09-18/111558091-brongegevens.json`): Blue
  Square adverteert op Idealista als "Blue Square Spain" met objecten in Jávea (Montgó–Ermita) en Benitachell (Cumbre del
  Sol), dus het kantoor is voor ons zoekgebied relevant.
- Volgende stap (5 pagina's): de vijf property-sitemaps lezen en per slug/plaats tellen; daarna alleen ES-JAV/Moraira-
  objecten ophalen.

## Bronnen (alle 24-09-2026)

- https://www.blue-square.com/robots.txt · https://www.blue-square.com/llms.txt · https://www.blue-square.com/sitemap.xml ·
  https://www.blue-square.com/javea-agency/ · https://www.blue-square.com/lander
- https://www.blue-square.es/robots.txt · https://www.blue-square.es/ · https://www.blue-square.es/privacy-policy/ ·
  https://www.blue-square.es/sitemap_index.xml ·
  https://www.blue-square.es/properties/exceptional-renovated-mediterranean-villa-with-panoramic-sea-views-in-javea-2/
- Lokaal: `onderzoek/makelaars/K01-kantoren-javea.json` (regel 328–332), `K02-kantoren-benitachell-moraira.json` (regel 486–489)

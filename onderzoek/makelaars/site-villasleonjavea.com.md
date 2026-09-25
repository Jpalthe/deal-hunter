# Villas Leon Javea — toets op automatisch lezen

- **Website:** https://www.villasleonjavea.com
- **Datum toets:** 24-09-2026 (ca. 23:40 CEST)
- **Bedrijf:** Villas Leon Javea Servicios Inmobiliarios, S.L.U. — bron: `og:site_name` en JSON-LD `RealEstateAgent` op de objectpagina (24-09-2026)
- **Kantoor:** Avenida Trenc d'Alba 5, 03730 Jávea — bron: JSON-LD `RealEstateAgent` + voettekst (24-09-2026)
- **Algemene contactkanalen:** info@villasleonjavea.com · +34 677 548 159 — bron: voettekst (24-09-2026)
- **Opgehaalde URL's (steeds ≥ 2 s ertussen):** `/robots.txt`, `/sitemap.xml`, `/sitemap-es-es.xml`,
  `/inmueble/villa-en-venta-en-el-tosalet-fase-iii-en-javea-alicante-costa-blanca/21720027`, `/terminos-y-condiciones`.
  Eerlijkheidshalve: de objectpagina is **twee keer** opgehaald — mijn lokale kopie was tussen twee stappen overschreven
  door een parallel proces (bestand bleek van een andere makelaarssite), dus in totaal 6 verzoeken, waarvan 3 HTML-pagina's.

## Advies: LEZEN (met kanttekening)

robots.txt staat de aanbod- en objectpagina's toe, de "Aviso Legal"-pagina bevat géén tekst (dus ook geen verbod), en de
objectpagina's dragen schema.org-JSON-LD met prijs, titel en coördinaten. Maar: **oppervlakte, perceel en referentie staan
niet in de kale HTML** — die worden pas in de browser door JavaScript opgehaald bij de API van het systeem (eGO Real Estate).
Spelregels:

1. Nooit sneller dan één pagina per twee seconden. 111 objectpagina's = ca. 4 minuten voor een volledige ronde; alleen de
   Spaanse URL's (`/inmueble/…`) lezen, de EN- en DE-varianten zijn dezelfde objecten.
2. Uit de kale HTML halen: prijs, titel, plaats/wijk (breadcrumb), gps-coördinaten, hoofdfoto-URL, beschrijving. Voor m²,
   perceel en referentie is óf een browser-render nodig (Playwright-achtig), óf een feed van het kantoor.
3. De data-API `websiteapi.egorealestate.com` **niet rechtstreeks aanroepen** zonder toestemming: dat is een andere host
   (van de softwareleverancier), niet gedekt door de robots.txt van de makelaar.
4. Foto's en beschrijvingen niet overnemen of publiceren; intern lezen, vergelijken en scoren.
5. Aanvullend "feed vragen" is zinvol: het systeem eGO Real Estate is een CRM dat aanbod naar portalen exporteert
   [te verifiëren — zoekbudget was op; niet met bron bevestigd].

## 1. robots.txt

- URL: https://www.villasleonjavea.com/robots.txt (HTTP 200, 521 bytes, 24-09-2026)
- Volledige inhoud:

```
User-agent: *
Disallow: /virtual/PrintProperty.aspx
Disallow: /virtual/PrintDevelopment.aspx
Disallow: /virtual/SmartLink.aspx
Disallow: /virtual/SmartLinkDetail.aspx
Disallow: /tel:
Disallow: */smartLink/*
Disallow: */{{parentLinkUrl}}
Disallow: */{{linkTarget}}
Disallow: */{{linkUrl}}
Disallow: */gerir-dados-rgpd
Disallow: */rgpd-update
Disallow: /404
Disallow: /500
Disallow: /en-gb/404
Disallow: /en-gb/500
Disallow: /de-de/404
Disallow: /de-de/500

Sitemap: https://www.villasleonjavea.com/sitemap.xml
```

- **Conclusie: ja, `User-agent: *` mag de aanbodpagina's lezen.** Uitgesloten zijn alleen printweergaven, "smartlinks",
  de AVG-beheerpagina's en foutpagina's. `/inmueble/…`, `/inmuebles/…` en `/venta-de-inmuebles…` staan nergens op
  Disallow. Geen `Crawl-delay`. Wél een `Sitemap:`-regel.

## 2. Gebruiksvoorwaarden

- De voettekst linkt "Aviso Legal" naar https://www.villasleonjavea.com/terminos-y-condiciones (HTTP 200, 24-09-2026).
- **De pagina is leeg.** Na het strippen van menu en voettekst blijft er alleen het woord "Párrafo" over — de
  standaardtekst van een lege alinea in de site-editor. Geen `<title>`, geen meta-omschrijving, geen juridische tekst,
  geen bedrijfsgegevens (NIF/CIF), niets over scraping, robots, reproductie of auteursrecht.
- Verder bestaan `/politica-de-privacidad` en `/politica-de-cookies` (niet opgehaald, budget). Die gaan over
  persoonsgegevens en cookies, niet over gebruik van de site.
- In de HTML staan `<!--googleoff: all-->`-commentaren rond de navigatie; dat is een aanwijzing voor Google's
  zoekmachine om navigatie niet te indexeren, geen verbod.
- **Conclusie: geen voorwaarden gevonden die automatisch lezen verbieden** ("niet gevonden": er is wel een pagina,
  maar zonder inhoud).

## 3. Sitemap

- Index: https://www.villasleonjavea.com/sitemap.xml (HTTP 200, 490 bytes, 24-09-2026) verwijst naar drie
  taalsitemaps — `sitemap-es-es.xml`, `sitemap-en-gb.xml`, `sitemap-de-de.xml` — alle drie met
  `lastmod 2026-09-24T04:57:06+01:00` (de sitemap wordt dus dagelijks/'s nachts vernieuwd).
- Alleen de Spaanse gelezen: https://www.villasleonjavea.com/sitemap-es-es.xml (HTTP 200, 41 kB, 24-09-2026).
  Geen `lastmod` per URL, dus niet bruikbaar als wijzigingsdetector per object; wel als volledige lijst.
- **143 URL's**, waarvan:
  - **111 objectpagina's** onder `/inmueble/{slug}/{id}` (id = 7–8 cijfers, bijv. `21720027`)
    - 66 met huurwoorden in de slug (alquiler / temporada / invierno / vacacional / turístico) → **huur**
      (vakantie-, winter- en jaarverhuur)
    - **45 zonder huurwoord → vermoedelijk te koop** (15 daarvan met "venta" in de slug; de rest is naar de titel te
      oordelen ook koop: villa's, chalets, een perceel `suelo-urbano-parcela-…`, een lot van vier villa's)
  - 9 zoek-/lijstpagina's: `/inmuebles`, `/venta-de-inmuebles?bus=1`, `/vacaciones/alquilerturistico…`,
    `/alquiler-a-largo-plazo/…`, `/busqueda-de-inmuebles`, `/favoritos`, `/comparar`, …
  - 5 plaatsfilters: `/inmuebles/javea--xabia`, `/moraira`, `/denia`, `/pedreguer`, `/teulada`
  - 11 typefilters: `/inmuebles/villa`, `/chalet`, `/casa-con-parcela`, `/suelo-urbano`, `/atico`, …
  - de rest: bedrijfspagina's (`/nosotros`, `/consultores`, `/empleo`, `/promociones`, `/contactos`,
    `/javea-moraira-denia`)
- De EN- en DE-sitemaps bevatten naar verwachting dezelfde 111 objecten onder `/en-gb/property/…` en `/de-de/…`
  (de objectpagina toont `hreflang`-alternatieven met hetzelfde id) — niet opgehaald.

## 4. Aanbodpagina en objectpagina

- **Aanbodpagina (te koop):** https://www.villasleonjavea.com/venta-de-inmuebles?bus=1 — uit de sitemap; de
  breadcrumb-JSON-LD op de objectpagina gebruikt `/venta-de-inmuebles/viviendas-casas/venta/javea-xabia/…`.
  Niet apart opgehaald (budget); objecten zijn rechtstreeks via de sitemap te bereiken.
- **Objectpagina gelezen:**
  https://www.villasleonjavea.com/inmueble/villa-en-venta-en-el-tosalet-fase-iii-en-javea-alicante-costa-blanca/21720027
  (HTTP 200, 75 kB, `<!--Published:05/02/2026 08:05-->`, 24-09-2026)
- **JSON-LD: ja, drie blokken** (`<script type="application/ld+json">`):
  1. `BreadcrumbList`: Viviendas/Casas › Venta › Jávea / Xàbia › La Granadella - Costa Nova › object
  2. `RealEstateAgent`: bedrijfsnaam, adres Avenida Trenc d'Alba 5, 03730, `areaServed: "Jávea / Xàbia"`
  3. `RealEstateListing`: `name` "Villa en venta en el Tosalet (fase III) en Jávea (Alicante - Costa Blanca)",
     volledige `description`, `image` (images.egorealestate.com, 1280×960),
     `about: { @type: Accommodation, accommodationCategory: "RESI", latitude 38.747148, longitude 0.212340 }`,
     `offers: { price: "1399000", priceCurrency: "EUR", businessFunction: …#Sell }`.
     **Niet aanwezig:** `floorSize`, perceeloppervlak, `numberOfRooms`, referentie/`sku`.
- **Open Graph: ja** — `og:site_name`, `og:title` (afgekapt op ca. 60 tekens: "Villa en venta en el Tosalet (fase III)
  en Jávea (Alicante -"), `og:description`, `og:image` (+ type/width/height), `og:url`, `og:type website`,
  `og:locale ES_ES`; plus `twitter:card`, `twitter:title`, `twitter:image`, `twitter:description`.
- **Wat er in de kale HTML staat:** prijs 1.399.000 EUR (alleen in JSON-LD), plaats Jávea / wijk La Granadella -
  Costa Nova (breadcrumb), coördinaten, beschrijving, hoofdfoto.
  **Wat er níet in staat:** oppervlakte, perceel, referentie, slaapkamers/badkamers — de zichtbare tekst bevat geen
  enkele "m²", geen "Ref." en ook de prijs niet. Het element `class="specsText"` is leeg; de kenmerken worden in de
  browser geladen door `dataApi.realestates.bundle.min.js` met configuratie
  `DataApi.push({'apiUrl':'//websiteapi.egorealestate.com/v1', …})`.
- Cookies: geen `Set-Cookie` op een kale GET; de cookiebanner zet clientside een cookie `cookieOK`.

## 5. Systeem achter de site: eGO Real Estate (Janela Digital)

Niet een van de Spaanse standaardsystemen (Inmoweb, Mediaelx, Sooprema, Inmovilla, Witei) en geen WordPress, maar het
Portugese **eGO Real Estate** van Janela Digital (CRM + websites). Bewijs (alles 24-09-2026):

- HTTP-header op elke response: `x-served-by: JanelaDigital`, `x-served-from: 204-5_14579-2`
- Scripts/CSS van `https://static.egorealestate.com/egoforge/websiteeditor/…` en
  `//media.egorealestate.com/SysV4Websites/WebsiteEditorResources/…`; foto's van `images.egorealestate.com`
- Voettekst: "CRM y páginas inmobiliarias por eGO Real Estate"
- Data-API: `//websiteapi.egorealestate.com/v1`
- robots.txt met ASP.NET-paden (`/virtual/PrintProperty.aspx`) en Portugese paden (`gerir-dados-rgpd`)
- Handlebars-menutemplates (`{{menuName}}`, `{{linkUrl}}`) in de HTML — dezelfde tokens die in robots.txt op Disallow staan

## 6. Omvang en dekking

- **Geschat aanbod: ca. 111 objecten** op de site (Spaanse sitemap, 24-09-2026), waarvan **ca. 45 te koop** en
  ca. 66 te huur (slug-analyse; marge van enkele stuks).
- **Dekking Jávea/Benitachell/Moraira: hoog, vrijwel alles Jávea.** Van de 111 objectslugs noemen er 56 Jávea/Xàbia,
  1 Moraira, 1 Dénia, 1 Teulada, 3 Pedreguer/Jesús Pobre en 50 geen plaats. Benitachell komt in geen enkele slug voor.
  Het kantoor zit in Jávea, `areaServed` is "Jávea / Xàbia" en de plaatsfilters in de sitemap zijn Jávea, Moraira,
  Dénia, Pedreguer en Teulada. Schatting: 80–90 % Jávea, Moraira marginaal, Benitachell nihil [te verifiëren via
  de plaatsfilterpagina's].
- Voor Deal Hunter interessant in de sitemap-titels: een perceel (`suelo-urbano-parcela-bastante-llana/21127091`),
  een "pequeña villa … para reformar" (`…/23451424`) en een lot van vier luxevilla's (`…/23215588`).

## Bronnen

- https://www.villasleonjavea.com/robots.txt (24-09-2026)
- https://www.villasleonjavea.com/sitemap.xml en /sitemap-es-es.xml (24-09-2026)
- https://www.villasleonjavea.com/inmueble/villa-en-venta-en-el-tosalet-fase-iii-en-javea-alicante-costa-blanca/21720027 (24-09-2026)
- https://www.villasleonjavea.com/terminos-y-condiciones (24-09-2026)

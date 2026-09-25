# iad España (asesores Jávea) — toets op automatisch lezen

- **Site:** https://www.iadespana.es — startpunt https://www.iadespana.es/encontrar-un-asesor/javea-03738
- **Datum toets:** 24-09-2026
- **Opgehaald (5 van max. 5, elk ruim 2 s na elkaar):** robots.txt, sitemap.xml, sitemap/es/ads.xml, de asesor-pagina Jávea, één objectpagina.
- **Advies: lezen** — onder voorbehoud van de gebruiksvoorwaarden (zie punt 2; niet meer opgehaald binnen het budget van vijf pagina's).

## 1. robots.txt — toegestaan

Bron: https://www.iadespana.es/robots.txt (HTTP 200, 24-09-2026). Let op: een robots.txt geldt alleen op de
domeinwortel; de opgegeven variant onder `/encontrar-un-asesor/javea-03738/robots.txt` is geen geldige plek en is
niet opgehaald.

Voor `User-agent: *` staat géén algemeen verbod. Wel uitgesloten (letterlijk uit het bestand):

```
User-agent: *
Disallow: */account/*
Disallow: */print
Disallow: /agente-inmobiliario/*/valoracion
Disallow: /liste/annonces*
Disallow: *?sort=priceAsc
Disallow: *?priceMin=*
Disallow: *?priceMax=*
Disallow: *?location=*
Disallow: /*&*
Disallow: /*modal=property_media*
...
User-agent: Scrapy
Disallow: /
Sitemap: https://www.iadespana.es/sitemap.xml
```

Conclusie: objectpagina's (`/anuncio/...`) en de schone aanbodpagina's (`/anuncios/javea_03/venta/...`) mogen
gelezen worden. **Niet** toegestaan: gefilterde of gesorteerde zoek-URL's met parameters (`?priceMin=`, `?sort=`,
`?location=`, alles met `&`), print-versies, accountpagina's en waarderingspagina's. De user-agent `Scrapy` is
volledig geblokkeerd (net als FacebookBot, msnbot-media en SemrushBot) — dus nooit met Scrapy of een
Scrapy-achtige naam lezen.

## 2. Gebruiksvoorwaarden — niet gecontroleerd (URL wel bekend)

In de voettekst van de objectpagina staan de links `/aviso-legal`, `/politica-de-privacidad`,
`/politica-de-cookies` en `/hoja-reclamacion` (bron: objectpagina hieronder, 24-09-2026). De asesor-pagina
bevatte die voettekst niet in de server-HTML, waardoor de URL pas bij de vijfde en laatste ophaalbeurt bekend werd.
**De tekst van https://www.iadespana.es/aviso-legal is dus niet gelezen.** Of daar automatisch lezen wordt
verboden is onbekend. Eerste stap bij een volgende ronde: die ene pagina ophalen. Verbiedt hij het, dan wordt het
advies "overslaan" (iad kent geen exportfeed zoals Inmoweb of Mediaelx).

## 3. Sitemap — aanwezig, gelaagd, niet geteld

- https://www.iadespana.es/sitemap.xml (HTTP 200, lastmod 23-09-2026) is een **index** met vijf deelsitemaps:
  `sitemap/main.xml`, `sitemap/es/agents.xml`, `sitemap/es/ads.xml`, `sitemap/es/propertylisting.xml`,
  `sitemap/es/propertylisting/deindex.xml`.
- https://www.iadespana.es/sitemap/es/ads.xml (HTTP 200, lastmod 24-09-2026) is **opnieuw een index** met zes
  deelsitemaps per objecttype: `ads/apartment.xml`, `ads/building.xml`, `ads/business.xml`, `ads/land.xml`,
  `ads/house.xml`, `ads/parking.xml`.
- De object-URL's zelf staan pas in die zes bestanden; die zijn niet meer opgehaald (budget). **Aantal object-URL's:
  onbekend.** Het gaat om het landelijke aanbod van iad (de site meldt "+ 850 agentes"), dus dat worden vele
  duizenden URL's waarvan maar een klein deel in onze regio ligt.
- Bruikbaar voor later: de object-URL's bevatten de plaatsnaam in de slug, en de site gebruikt **beide spellingen**
  (`...-javea-...` én `...-xabia-...`). Filteren op `javea|xabia|benitachell|benitatxell|moraira|teulada` in
  `house.xml`, `apartment.xml` en `land.xml` geeft dan de regionale lijst zonder elke objectpagina te openen.

## 4. Aanbodpagina en objectpagina — goed leesbaar

- Aanbodpagina's (uit broodkruimels en voettekst van de objectpagina, niet apart geopend):
  https://www.iadespana.es/anuncios/javea_03/venta (alles Jávea), plus per type `/anuncios/javea_03/venta/casa`,
  `/piso`, `/terreno/nuevo`, `/inmueble-comercial`. Dénia idem met `denia_03`.
- Geopende objectpagina: https://www.iadespana.es/anuncio/piso-venta-3-habitaciones-javea-114m2/r777904
  (HTTP 200, 67 kB, 24-09-2026). De HTML is **server-side gerenderd** (Nuxt): alle inhoud staat in de bron, geen
  JavaScript nodig.
- **JSON-LD aanwezig** (`<script type="application/ld+json">`, schema.org `@graph`): `BreadcrumbList`, `WebPage`,
  `Apartment`, `Offer`, `ImageObject`. Wat erin staat:
  - prijs: `Offer.price` = "320.000 €", `priceCurrency` EUR, `availability` InStock, `validFrom` 30/12/2025
  - oppervlakte: `Apartment.floorSize` 114 (MTK); `numberOfBedrooms` 3, `numberOfRooms` 4, `yearBuilt` 1978
  - perceel: niet in JSON-LD (appartement); bij huizen staat het in de tekst ("94 m² de terreno" bij een ander object)
  - plaats: `address.addressLocality` "Jávea", `postalCode` 03730, `addressCountry` ES
  - referentie: niet als apart JSON-LD-veld, wel in de URL (`r777904`), de `<title>` en de tekst ("Referencia: 777904")
  - let op: `Offer.seller.name` bevat de **naam van de asesor** — persoonsgegeven, bij lezen weggooien
- **Open Graph aanwezig:** `og:title` "Piso 3 habitaciones de 114 m² en Jávea (03730)", `og:type` article,
  `og:url`, `og:image` (images.iadespana.es), `og:locale` es met alternates en/fr/ca. `og:description` is
  generiek ("Anuncio inmobiliario: ..."); de echte tekst staat in `meta name="description"`.
- Extra in de tekst: "114 m² construidos, 90 m² útiles", "Precio por m² 2807 € / m²", energielabel E, 17 foto's.
  Pagina bestaat ook in en/fr/ca (`/en/ad/...`).

## 5. Systeem — eigen bouw (Nuxt)

Aanwijzingen (24-09-2026): response-header `x-powered-by: Nuxt`, `server: nginx/1.26.3`, geleverd via AWS
CloudFront (`via: ...cloudfront.net`); 376 verwijzingen naar `/_nuxt/`-assets en `window.__NUXT__` in de HTML;
beelden op `images.iadespana.es` en `images.playiad.com`; Datadog RUM-monitoring. Geen sporen van Inmoweb,
Mediaelx/LetsINMO, Sooprema, Inmovilla, Witei of WordPress. Dit is het internationale iad-platform (zelfde bouw als
iadfrance.fr, iadportugal.pt enz.) — er is geen makelaars-CMS met exportfeed.

## 6. Omvang en dekking Jávea/Benitachell/Moraira

Bron: https://www.iadespana.es/encontrar-un-asesor/javea-03738 (HTTP 200, 24-09-2026), zonder namen:

- "12 asesores inmobiliarios en Jávea (03738) o alrededores": volgens de kaartjes 1 gevestigd in Jávea (03738),
  1 in Moraira (03724) en 10 in Dénia (03700).
- Bij 10 van de 12 staat een aantal "propiedades disponibles": 14, 17, 5, 11, 1, 4, 8, 8, 9 en 3 = **80 objecten**
  samen; bij 2 asesores staat geen aantal.
- Het blok "Últimos anuncios en Jávea y alrededores" toont 4 objecten: Dénia, Ondara, Beniarbeig en 1× Jávea. Op de
  objectpagina staan 6 "propiedades similares": 2× Jávea/Xàbia, 4× Dénia.
- Schatting: ~80 objecten bij deze groep asesores, waarvan naar schatting een **minderheid (grofweg een kwart tot
  een derde) in Jávea, Benitachell of Moraira** ligt; het zwaartepunt is Dénia. [te verifiëren] — het exacte aantal
  staat op https://www.iadespana.es/anuncios/javea_03/venta (nog niet geopend) en in de deelsitemaps.
- iad-asesores zijn zelfstandigen die doorgaans óók op de portalen adverteren; de meerwaarde zit vooral in objecten
  die alleen op iad staan. Dat is pas te zien door de regionale lijst tegen Idealista/Fotocasa te leggen.

## Praktisch voor een leesrobot

1. Eerst `/aviso-legal` lezen (1 pagina). Verbod → stoppen.
2. Regionale URL-lijst uit `sitemap/es/ads/house.xml`, `apartment.xml`, `land.xml` (filter op plaatsnaam in de slug,
   beide spellingen).
3. Per object alleen de schone `/anuncio/...`-URL openen; JSON-LD uitlezen (prijs, m², slaapkamers, bouwjaar,
   plaats, postcode) plus "Referencia" en "m² de terreno" uit de tekst.
4. Nooit filter-/sorteer-URL's met parameters, nooit als "Scrapy", niet sneller dan één pagina per 2 seconden,
   en de asesor-naam (`seller.name`) niet opslaan.

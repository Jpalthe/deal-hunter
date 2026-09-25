# MG Villas — toets op automatisch lezen

- **Website:** https://www.mgvillas.com (handelsnaam "MG Villas Luxury Property"; rechtspersoon volgens de eigen aviso legal: MARSAL PROPIEDADES S.L., NIF B01947944; kantoor Avenida de La Libertad 11 - Local 11, 03730 Playa del Arenal, Jávea; algemeen contact info@mgvillas.com en +34 657 433 723). Zusterdomeinen met dezelfde inhoud in andere talen: mgvillas.co.uk, mgvillas.de, mgvillas.fr, mgvillas.nl (uit de hreflang-tags op de objectpagina); bouwtak op mgvillasconstrucciones.com.
- **Datum toets:** 24-09-2026, ca. 23:16–23:18 lokale tijd (server-datumkoppen 21:16–21:18 UTC).
- **Opgehaald (5 verzoeken, telkens ≥ 2 s tussenruimte):** robots.txt (21:16:36 UTC), sitemap.xml (21:16:49), aviso legal (21:17:52), aanbodpagina /venta/ (21:17:54), één objectpagina (21:17:56). Alles daarna is lokaal geanalyseerd zonder nieuwe verzoeken.
- **Advies: lezen — hoge prioriteit.** robots.txt staat het toe, de voorwaarden verbieden automatisch lezen niet, en de pagina's zijn kant-en-klaar leesbaar (server-side HTML met schema.org JSON-LD). Groot aanbod: 346 objecten te koop, waarvan naar schatting driekwart in Jávea, Benitachell of Moraira, met ruim 50 percelen in dat gebied. Twee spelregels: lees via de sitemap en niet via de paginering (die gebruikt `?page=` en dat verbiedt robots.txt), en gebruik de gegevens alleen intern — de aviso legal verbiedt hergebruik van teksten en foto's voor commerciële doeleinden zonder toestemming.

## 1. robots.txt — toegestaan

Bron: https://www.mgvillas.com/robots.txt (24-09-2026, HTTP 200). Volledige inhoud:

```
# START nuxt-robots (indexable)
User-agent: *
Disallow: /_edit
Disallow: /_canvas
Disallow: /_debug
Disallow: /__sitemap__
Disallow: /*?

Sitemap: https://www.mgvillas.com/sitemap.xml
# END nuxt-robots
```

Elke lezer (`User-agent: *`) mag de site lezen, behalve vier technische paden en **alle URL's met een vraagteken** (`Disallow: /*?`). Gevolg:

- Objectpagina's zoals `/propiedad/venta/...-mg6730cr/` hebben geen vraagteken → **toegestaan**.
- De aanbodpagina `/venta/` zelf is toegestaan, maar de vervolgpagina's `/venta/?page=2`, `?page=3` enz. **niet** (de site gebruikt `<link rel="next" href="https://www.mgvillas.com/venta/?page=2">`). Ook filters via de URL vallen hieronder.
- De sitemap staat expliciet vermeld en is de aangewezen ingang.

Geen `Crawl-delay`. De HTTP-antwoorden dragen `x-robots-tag: index, follow`.

## 2. Gebruiksvoorwaarden — geen scrapingverbod, wél een verbod op hergebruik voor commerciële doeleinden

Bron: https://www.mgvillas.com/aviso-legal/ ("Aviso legal y términos de uso", met daaronder de privacy- en cookieverklaring), gelezen 24-09-2026. Een aparte pagina "términos y condiciones" bestaat niet; de sitemap noemt alleen `/aviso-legal/`.

De woorden scraping, robot, crawler, bot, "extracción" of "acceso automatizado" komen niet voor (het enige "automatizadas" gaat over hun eigen databanken). Wel relevant:

- Onder "Compromisos y obligaciones de los usuarios": "Respecto de los contenidos de esta web, se prohíbe: su reproducción, distribución o modificación, total o parcial, a menos que se cuente con la autorización de sus legítimos titulares; cualquier vulneración de los derechos del prestador o de los legítimos titulares; su utilización para fines comerciales o publicitarios."
- Zelfde paragraaf: de gebruiker mag niets doen dat het portaal kan "dañar, inutilizar o sobrecargar" — dus rustig lezen, niet hameren.
- Onder "Derechos de propiedad intelectual e industrial": "quedan expresamente prohibidas la reproducción, la distribución y la comunicación pública, incluida su modalidad de puesta a disposición, de la totalidad o parte de los contenidos de esta página web, con fines comerciales, en cualquier soporte y por cualquier medio técnico, sin la autorización de mgvillas.com."
- Onder "Enlaces externos": wie vanaf een eigen site een link naar mgvillas.com wil leggen, heeft daarvoor "la autorización previa y escrita" nodig. (Praktisch niet handhaafbaar, maar het staat er.)

Uitleg in gewone taal: lezen om te weten wat er te koop staat is niet verboden; teksten of foto's overnemen, doorpubliceren of commercieel hergebruiken wél. Voor Deal Hunter (intern signaleren, daarna zelf contact opnemen) past dat: alleen prijs, oppervlakten, plaats, referentie en de link bewaren, geen beschrijvingen of foto's kopiëren.

## 3. Sitemap — 359 objectpagina's, waarvan 346 te koop

Bron: https://www.mgvillas.com/sitemap.xml (24-09-2026, HTTP 200, 82.913 bytes). Eén platte sitemap, geen sitemap-index, geen hreflang-alternates (de andere talen staan op eigen domeinen).

- 473 URL's in totaal.
- **359 onder `/propiedad/`** = objectpagina's:
  - `/propiedad/venta/…` → **346 te koop**
  - `/propiedad/alquiler/…` en `/propiedad/alquiler-vacacional/…` → 13 huur
- 54 onder `/blog/`.
- ±60 landings- en zoekpagina's (bijv. `/villas-en-venta-en-javea/`, `/parcelas-en-javea/`, `/obra-nueva-en-moraira/`, `/propiedades-a-la-venta-en-benitachell-cumbre-del-sol/`).

Elke URL heeft een `<lastmod>`-datum (473 van 473; op 24-09-2026 waren er 51 URL's met de datum van diezelfde dag, de overige recente wijzigingen liggen tussen 14 en 23 september). Daarmee is per object te zien wanneer het voor het laatst is aangepast, zonder de pagina zelf op te halen. Geen `changefreq` of `priority`.

Het getal 346 klopt met de teller op de aanbodpagina ("346 propiedades encontradas", zie punt 4). 342 van de 359 objectslugs eindigen op een referentiecode (bijv. `-mg6730cr`, `-mgar202852`, `-mgc507538`, `-mghd032827`, `-mgi336559`); de betekenis van de verschillende voorvoegsels (MG6…, MGAR, MGC, MGI, MGHD, MGAV, MGGH, MGR, MGU, MGOH, MGCB) is niet uit de site af te leiden **[te verifiëren]** — mogelijk eigen portefeuille versus objecten van samenwerkende kantoren.

## 4. Aanbodpagina en objectpagina — JSON-LD én og-tags aanwezig

**Aanbodpagina:** https://www.mgvillas.com/venta/ ("Propiedades en venta en la Costa Blanca | MG Villas", 24-09-2026). Toont "346 propiedades encontradas", 21 kaarten per pagina met prijs, bebouwd, perceel, kamers en badkamers in de HTML (server-side gerenderd, dus zonder JavaScript leesbaar). Paginering via `?page=2` — verboden door robots.txt, zie punt 1. Filters: alle / alleen nieuwbouw / percelen / bestaande bouw ("Resales").

**Objectpagina (voorbeeld):** https://www.mgvillas.com/propiedad/venta/villa-de-lujo-a-la-venta-en-puerta-fenicia-con-vistas-impresionantes-al-montgo-mg6730cr/ (24-09-2026, HTTP 200, 611 KB).

Eén `<script type="application/ld+json">` met een `@graph` van zes knopen: WebSite, WebPage, RealEstateAgent, **RealEstateListing**, ItemList, ImageObject. In RealEstateListing staat:

| Veld | Waarde |
|---|---|
| `offers.price` / `priceCurrency` | 1395000 / EUR (`availability: InStock`) |
| `floorSize` | 220 (unitCode MTK = m²) |
| `numberOfRooms` / `numberOfBathroomsTotal` | 3 / 3 |
| `address.addressLocality` | Jávea (regio Alicante, land ES, postcode 03739) |
| `datePosted` | 2026-03-24 |
| `image` | 30 foto's op app-api.paagees.com |
| `name` / `description` | titel en (ingekorte) beschrijving |

**Niet** in de JSON-LD: perceeloppervlak, referentie en bouwjaar. Die staan wél in de zichtbare HTML ("Ref. MG6730CR", "Superficie construida: 220 m²", "Superficie parcela: 1019 m²", "Año de construcción: 2019", "Chalet/Villa en Jávea - Partidas Comunes - Adsubia") en gestructureerd in de Nuxt-payload `<script id="__NUXT_DATA__">` (266 KB; bevat o.a. `"reference":"MG6730CR"`, `"price":1395000`, `constructionYear: 2019`, velden voor plot en built).

De RealEstateAgent-knoop geeft kantooradres, algemeen telefoonnummer, e-mail, openingstijden (ma–vr 10:00–15:00) en coördinaten (38.7722461, 0.1896733).

**og-/twitter-tags:** `og:title`, `og:description`, `og:image` (1200×630, op app-api.paagees.com), `og:type = website`, `og:url`, `og:locale = es_ES`, `og:site_name = MG Villas Luxury Property`, `twitter:card = summary_large_image`. Geen prijs- of producttags in de og-set. Verder `<link rel="canonical">` en hreflang es/en/de/fr/nl naar de zusterdomeinen.

## 5. Systeem achter de site — Paagees (op Nuxt), geen van de bekende makelaars-CMS'en

Aanwijzingen (alle 24-09-2026):

- robots.txt begint met `# START nuxt-robots (indexable)` → Nuxt-module.
- Cookie `paagees_cid` op elk antwoord (`Set-Cookie: paagees_cid=…; Max-Age=34560000; HttpOnly; Secure`).
- Scripts onder `/_nuxt/*.js`, payload in `<script id="__NUXT_DATA__">`, `<html data-page="property-detail" lang="es">`.
- Alle afbeeldingen, logo en social-previews op `https://app-api.paagees.com/uploads/019f7eb6-…/property/…` (175 verwijzingen op één objectpagina); statistiek via `https://analytics.paagees.com/script.js`; daarnaast Google Tag Manager.
- Nul treffers op Inmoweb, Mediaelx/LetsINMO, Sooprema, Inmovilla, Witei, WordPress (`wp-content`), Kyero of Idealista in de HTML. Geen "powered by"-vermelding en geen `generator`-meta.

Conclusie: **Paagees**, een Spaans website-/vastgoedplatform gebouwd op Nuxt (Vue). Het is geen "eigen bouw" maar ook geen van de zes systemen uit de vraag. Of Paagees een exportfeed (XML/Kyero) voor derden aanbiedt is niet uit de site af te leiden **[te verifiëren]**; niet nodig zolang lezen via de sitemap is toegestaan.

## 6. Omvang en dekking Jávea / Benitachell / Moraira

Basis: de 346 verkoop-URL's uit de sitemap (24-09-2026), ingedeeld op plaats- of wijknaam in de URL (Jávea incl. Arenal, Montgó, Tosalet, Granadella, Portichol, Cala Blanca, Costa Nova, Adsubia enz.; Moraira incl. Teulada, El Portet, Sabatera, Estret; Benitachell incl. Cumbre del Sol). Marge van enkele procenten, want 12 URL's noemen geen plaats en een wijknaam kan verkeerd worden toegewezen; bij het echte lezen geeft `addressLocality` in de JSON-LD per object de exacte gemeente.

| Gebied | Aantal | Aandeel |
|---|---|---|
| Jávea / Xàbia | ±209 | 60 % |
| Moraira / Teulada | ±44 | 13 % |
| Benitachell / Cumbre del Sol | ±17 | 5 % |
| **Kerngebied samen** | **±270** | **78 %** |
| Benissa | 19 | 5 % |
| Dénia | 13 | 4 % |
| Calpe | 12 | 3 % |
| Altea | 6 | 2 % |
| Overig (Pedreguer, Benidorm, Llíber, Benigembla, Ibiza…) | 14 | 4 % |
| Geen plaats in URL | 12 | 3 % |

Type binnen het kerngebied (op URL): ±148 villa's, **±58 percelen/bouwgrond** (55 parcela + 2 terreno + 1 solar), ±33 appartementen, ±14 chalets, 4 áticos, 4 casas, 2 fincas, 2 locales. Voor Deal Hunter zijn vooral de percelen en de oudere villa's interessant; het kantoor heeft ook aparte landingspagina's `/parcelas-en-javea/` en `/parcelas-en-moraira/`.

Daarnaast 13 huurobjecten (jaarverhuur en vakantieverhuur, vrijwel allemaal Jávea/Arenal) — niet relevant voor aankoop.

## Hoe te lezen (als Jan akkoord gaat)

1. Eén keer per dag `sitemap.xml` ophalen; alleen de URL's onder `/propiedad/venta/` bewaren. Nieuwe of verdwenen URL's = nieuw aanbod / verkocht of ingetrokken.
2. Alleen nieuwe of gewijzigde objectpagina's ophalen, één per ≥ 2 seconden (alle 346 in één keer ≈ 12 minuten; daarna alleen de verschillen). Nette User-Agent met contactadres.
3. Per pagina uitlezen: JSON-LD RealEstateListing (prijs, bebouwd, kamers, gemeente, datum geplaatst) plus referentie, perceel en bouwjaar uit de zichtbare HTML of de `__NUXT_DATA__`-payload.
4. Niet doen: `?page=`-paginering of URL-filters (robots.txt), rechtstreeks `app-api.paagees.com` aanroepen (niet voor derden bedoeld en niet door de robots.txt van mgvillas.com gedekt), beschrijvingen of foto's kopiëren of doorpubliceren (aviso legal).
5. Overweging voor Jan: MG Villas zit op 500 m van het Arenal en is een directe collega; een korte vraag om samenwerking of een feed kan op termijn meer opleveren dan stil meelezen. Dat is een zakelijke keuze, geen vereiste.

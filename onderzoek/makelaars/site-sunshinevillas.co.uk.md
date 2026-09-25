# Sunshine Villas — sunshinevillas.co.uk

Toets op automatisch lezen · TREE Deal Hunter · 24-09-2026

**Advies: LEZEN.** robots.txt laat de aanbodpagina's toe, de pagina's zijn gewone HTML
zonder inlog, en de sitemap geeft alle objectadressen kant-en-klaar. Eén voorbehoud:
de juridische pagina's staan voor robots dicht, dus de gebruiksvoorwaarden zijn niet
automatisch gelezen (zie punt 2 en "Actie voor Jan").

| | |
|---|---|
| Kantoor | Sunshine Villas, Av. de la Fontana 2, 03730 Xàbia (bron: JSON-LD op objectpagina, 24-09-2026) |
| Algemeen contact | ask@sunshinevillas.co.uk · +34 630 949 196 (zelfde bron) |
| Systeem | **Mediaelx** (footer "Design: Mediaelx" → mediaelx.net) |
| Aanbod | teller op de site: **303** objecten (koop + huur); sitemap: **712** objectadressen |
| Jávea / Benitachell / Moraira | **414 van 712** sitemap-objecten (58 %) |
| Pagina's opgehaald | 4 (robots.txt, sitemap.xml, aanbodpagina, één objectpagina), minimaal 3 s tussen de fetches |

## 1. robots.txt — toegestaan

Bron: https://sunshinevillas.co.uk/robots.txt (HTTP 200, gewijzigd 24-09-2026 05:00, opgehaald 24-09-2026).

Er is één blok `User-agent: *`. Het verbiedt alleen systeemmappen en de juridische,
privacy-, cookie-, rss-, klant- en zoekpagina's — niet het aanbod. Relevante regels:

```
User-agent: *
Disallow: /Connections
Disallow: /includes
Disallow: /intramedianet
Disallow: /xml
Disallow: /templates
Disallow: /modules
Disallow: /nota-legal
Disallow: /en/legal-note
Disallow: /nl/nota-legale
Disallow: /privacidad
Disallow: /en/privacy
Disallow: /cookies
Disallow: /rss/
Disallow: /customer/
Disallow: /catalogsearch/
Sitemap: https://sunshinevillas.co.uk/sitemap.xml
```

(De regels voor /ru, /fr, /se, /no, /zh zijn gelijk aan die voor /en en hier weggelaten.)
`/properties/`, `/property/<id>/…` en de landingspagina's `…-for-sale-in-javea.html`
komen nergens voor → **toegestaan voor `User-agent: *`**.

Let op: `/xml` en `/rss/` zijn dicht. Als daar een exportfeed achter zit, mag die dus
niet zomaar gelezen worden; die vraag je aan het kantoor (zie punt 5).

## 2. Gebruiksvoorwaarden — niet automatisch gelezen

De objectpagina linkt in de footer naar `/legal-note/`, `/privacy/` en `/cookies/`
(bron: HTML van de objectpagina, 24-09-2026). robots.txt sluit de juridische pagina's
in alle zeven taalvarianten uit (`/nota-legal`, `/en/legal-note`, `/nl/nota-legale`, …).
De Engelse pagina op de root staat er niet letterlijk in, maar de bedoeling is duidelijk:
die pagina's zijn niet voor robots. Daarom is `/legal-note/` **niet opgehaald** en is
er geen citaat. Of scraping daar verboden wordt: **niet vastgesteld**.

Wat wél vaststaat: geen enkele opgehaalde pagina bevat een verbod, een inlogmuur of
een technische blokkade (geen Cloudflare-challenge, gewone HTTP 200 op alles).

## 3. Sitemap — 712 objectadressen

Bron: https://sunshinevillas.co.uk/sitemap.xml (HTTP 200, 985 kB, gegenereerd
24-09-2026 07:00, "SimpleSitemapGenerator/1.2.0").

- Totaal **4.636 URL's**: Engels op de root, plus kopieën onder `/es/`, `/fr/`, `/ru/`, `/pl/`.
- Engelse objectpagina's (`/property/<id>/<slug>/`): **712**.
- Vorm: `https://sunshinevillas.co.uk/property/25087/4-bedroom-villa-for-sale-in-tosalet-javea-alicante/`
- 291 slugs bevatten `for-sale`, 64 `plot`, 10 `rent`/`rental` (de rest heeft een korte
  slug zoals `4-bedroom-detached-villa-javea-javea`).
- ID's lopen van 740 tot 25.088; 644 van de 712 hebben een ID ≥ 20.000. De laagste
  ID's zijn vermoedelijk oude of verkochte objecten die nog in de sitemap staan.
- Alle 712 hebben `lastmod` september 2026 (de generator stempelt alles opnieuw, dus
  die datum zegt niets over echte wijzigingen).
- Daarnaast ± 130 landingspagina's per plaats/wijk, bijv.
  `villas-for-sale-in-tosalet-javea.html`, `plots-for-sale-in-el-montgo-javea.html`,
  `detached-villas-for-sale-in-cumbre-del-sol-benitachell.html` — handig als
  voorgesorteerde lijsten.

## 4. Aanbodpagina en objectpagina

**Aanbod:** https://sunshinevillas.co.uk/properties/ (HTTP 200, 24-09-2026).
Teller op de pagina: "Search Results 303". Paginering met offset:
`/properties/?p=13`, `?p=25`, … (12 per pagina; keuze 12/24/48). De standaardsortering
toont eerst de huurobjecten (120 €, 1.200 €/maand …), dus koop en huur zitten in één
lijst. Op de lijst staan per kaart al: referentie, type, plaats, prijs, bebouwd, perceel,
slaap- en badkamers.

**Object:** https://sunshinevillas.co.uk/property/25087/4-bedroom-villa-for-sale-in-tosalet-javea-alicante/
(HTTP 200, 24-09-2026).

- `<script type="application/ld+json">`: **1 blok, maar alleen `RealEstateAgent`**
  (naam, logo, adres, e-mail, telefoon, priceRange "500€ - 6.000.000€"). Géén
  Product/Offer/Residence — prijs en maten staan dus **niet** in JSON-LD.
- `og:`-tags: **aanwezig** — `og:title` "4 bedroom villa for sale in Tosalet, Javea,
  Alicante", `og:url`, `og:type` "blog", `og:description`, `og:image`
  (`/media/images/properties/thumbnails/557250_lg.jpg`). Geen prijs of oppervlakte.
- In de zichtbare HTML (goed te lezen, vaste labels):
  - Prijs: **949,000€** (met knop "Notify price drop")
  - Referentie: **Ref: 34-26751**
  - Bebouwd: **237 m²** · Perceel: **784 m²**
  - Slaapkamers 4 · badkamers 3 · Energielabel "In process"
  - Plaats: **Javea, Tosalet** (kop "Villa for sale in Javea Alicante · Javea")
  - Beschrijving: bouwjaar 1985, gerenoveerd 2018, 600 m van zee, gastenappartement.

Conclusie: de gegevens zijn er, maar moeten uit de HTML-tekst komen (labels
"Ref:", "Built area:", "Plot:", "Bedrooms:", "Bathrooms:") en niet uit metadata.

## 5. Systeem: Mediaelx

Aanwijzingen (alle uit de opgehaalde HTML en headers, 24-09-2026):

- Footer: `Design: <a href="https://www.mediaelx.net">Mediaelx</a>` — doorslaggevend.
- Mediaelx-kenmerken: URL-vorm `/property/<id>/<slug>/`, referenties met kantoorprefix
  (`34-26751`, `10-48077`), body-class `en property interior`, cookie `viewed-props`,
  paden `/css/website.<stempel>.css`, `/js/website.<stempel>.js`,
  `/media/images/properties/thumbnails/…`, wijk-landingspagina's als `.html`.
- Server: nginx, Plesk, `x-powered-by: PHP/5.6.40` (verouderde PHP; wees zuinig met
  verzoeken), sessiecookie `PHPSESSID`. Geen Cloudflare.
- robots.txt sluit `/xml` en `/rss/` uit — typisch de plek waar Mediaelx-feeds staan.

Mediaelx-sites hebben doorgaans een XML-export voor portalen. Wil je liever een
feed dan lezen, dan is dit kantoor daarvoor een geschikte kandidaat.

## 6. Omvang en dekking Jávea

Op basis van de 712 Engelse objectadressen in de sitemap (plaatsnaam in de slug):

| Plaats | Objecten | Aandeel |
|---|---|---|
| Jávea / Xàbia | 205 | 29 % |
| Moraira | 123 | 17 % |
| Benitachell / Cumbre del Sol | 86 | 12 % |
| **Samen** | **414** | **58 %** |
| Benissa | 71 | 10 % |
| Calpe | 59 | 8 % |
| Dénia | 56 | 8 % |
| overig (Pedreguer, La Sella, Teulada, Jalón, Altea, Orba, Alcalalí …) | ± 120 | ± 17 % |

Schatting actief aanbod: **± 300** (teller van de site: 303, koop en huur samen);
de sitemap is ruimer (712) en bevat waarschijnlijk ook oude/verkochte objecten. Het
kantoor zit fysiek in Jávea; ruim de helft van het aanbod ligt in het kerngebied.
64 slugs bevatten `plot` — interessant voor percelen.

## Advies en werkwijze

**Lezen.** Loop de sitemap door (`/property/…`), één verzoek per 2 seconden, met een
herkenbare User-agent. Bij 712 pagina's is dat ± 25 minuten per volledige ronde; voor
alleen Jávea/Benitachell/Moraira (414) ± 14 minuten. Prijs, maten en referentie uit de
HTML-labels halen; `og:image` voor de hoofdfoto. Verkochte objecten herken je doordat
de pagina niet meer in de sitemap staat.

⏸️ ACTIE VOOR JAN
1. Open zelf in de browser https://sunshinevillas.co.uk/legal-note/ en kijk of daar
   iets staat over geautomatiseerd gebruik. Robots mogen die pagina niet lezen; een
   mens wel. Staat er een verbod, dan wordt het advies "feed vragen".
2. Optioneel: het kantoor vragen om hun Mediaelx-XML-feed (ask@sunshinevillas.co.uk).
   Dat is netter en lichter dan elke pagina apart lezen.

## Bronnen

- https://sunshinevillas.co.uk/robots.txt — 24-09-2026
- https://sunshinevillas.co.uk/sitemap.xml — 24-09-2026
- https://sunshinevillas.co.uk/properties/ — 24-09-2026
- https://sunshinevillas.co.uk/property/25087/4-bedroom-villa-for-sale-in-tosalet-javea-alicante/ — 24-09-2026

Niet opgehaald (robots): /legal-note/, /privacy/, /cookies/, /rss/, /xml.
Webzoekopdrachten waren in deze sessie niet beschikbaar (zoekbudget op); alles hierboven
komt uit de vier opgehaalde pagina's.

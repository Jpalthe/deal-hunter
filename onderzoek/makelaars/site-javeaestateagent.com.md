# Javea Estate Agent — www.javeaestateagent.com

**Toets op automatisch lezen · 24-09-2026 (21:33–21:36 UTC)**
Onderzoek voor TREE Deal Hunter. Vijf ophaalacties op de site gedaan (het maximum), telkens minstens twee seconden ertussen, met een eigen herkenbare user-agent. Niets omzeild, niet ingelogd, geen formulieren. Het zoekmachinebudget van deze sessie was op, dus alles hieronder komt rechtstreeks van de site zelf.

## Kort

**Lezen mag.** robots.txt geeft `User-agent: *` vrij toegang (`Allow: /`) en sluit alleen WordPress-beheer, zoekpagina's en parameter-URL's uit. Er zijn géén gebruiksvoorwaarden, privacyverklaring of aviso legal te vinden — de site heeft er simpelweg geen. De objectpagina's zijn gewone, server-gerenderde HTML met referentie, prijs en bouwoppervlak als leesbare tekst.

**Maar de oogst is mager.** 86 objecten in de sitemap, allemaal gelabeld als Jávea. De geteste objectpagina heeft geen omschrijving ("Not Available"), geen perceelgrootte ("N.A"), geen zone of adres, en de JSON-LD bevat alleen Yoast-standaardblokken zonder prijs of oppervlak. Bovendien staan in de voettekst van de site links naar casino-/gokpagina's op hetzelfde domein — een sterke aanwijzing dat deze WordPress-installatie besmet is met SEO-spam.

**Advies: lezen, lage prioriteit.** Kleine, dunne bron; via de sitemap ophalen, niet via zoek- of parameter-URL's.

## 1. robots.txt — mag een gewone bot de aanbodpagina's lezen?

Bron: https://www.javeaestateagent.com/robots.txt (opgehaald 24-09-2026 21:33 UTC, HTTP 200, 780 bytes).

**Ja.** Voor `User-agent: *` staat letterlijk:

```
User-agent: *
Allow: /

# WordPress core
Disallow: /wp-admin/
Allow: /wp-admin/admin-ajax.php

# Login & sensitive
Disallow: /wp-login.php
Disallow: /xmlrpc.php

# Internal/search
Disallow: /?s=
Disallow: /search/

# Parameter spam (VERY IMPORTANT for your case)
Disallow: /*?p=
Disallow: /*?replytocom=

# Optional (depends on site)
Disallow: /author/
Disallow: /tag/

Sitemap: https://www.javeaestateagent.com/sitemap_index.xml
Sitemap: http://www.javeaestateagent.com/sitemap27.xml
Sitemap: http://www.javeaestateagent.com/sitemap24.xml
```

Wat dit betekent voor automatisch lezen:
- De aanbodpagina's (`/properties/`, `/property-types/...`) en de objectpagina's (`/properties/<slug>/`) zijn nergens uitgesloten.
- Verboden: de zoekfunctie (`/?s=`, `/search/`), URL's met `?p=` of `?replytocom=`, auteurs- en tagpagina's, en de WordPress-beheerpaden. Een lezer moet dus de nette URL's uit de sitemap gebruiken, nooit `?p=123`.
- Geen `Crawl-delay`.
- Daarboven staan aparte blokken die zeven SEO-bots volledig weren (`Baiduspider`, `AhrefsBot`, `MJ12bot`, `BLEXBot`, `DotBot`, `SemrushBot`, `YandexBot` — elk `Disallow: /`). Een eigen lezer valt daar niet onder zolang hij een eigen naam voert.
- Drie `Sitemap:`-regels; alleen de eerste (`sitemap_index.xml`) is gecontroleerd en werkt. De twee `http://...sitemap27.xml` / `sitemap24.xml`-regels zijn niet opgevraagd (limiet) en zien eruit als overblijfsels.

## 2. Gebruiksvoorwaarden — verbieden ze scraping?

**Niet gevonden — de site heeft er geen.** Bewijs:
- De pagina-sitemap https://www.javeaestateagent.com/page-sitemap.xml (24-09-2026 21:35 UTC, HTTP 200) bevat in totaal zes pagina's: `/`, `/properties-in-javea-under-200000/`, `/properties-in-javea-under-300000/`, `/sitemap/`, `/guide-to-buying-in-spain/`, `/contact-us/`. Geen privacy-, cookie-, terms- of legal-pagina.
- De voettekst van de objectpagina (zie 4) bevat geen enkele link met legal/privacy/terms/cookie/aviso in URL of linktekst; er is ook geen cookiebanner-plugin in de HTML te zien.

Er is dus geen verbod, maar ook geen toestemmingstekst. Voor een Spaans kantoor is het ontbreken van een privacyverklaring en aviso legal op zichzelf al een teken van weinig onderhoud.

## 3. Sitemap

- Index: https://www.javeaestateagent.com/sitemap_index.xml (24-09-2026 21:33 UTC, HTTP 200, Yoast SEO). Bevat: `post-sitemap.xml` t/m `post-sitemap10.xml` (tien stuks), `page-sitemap.xml`, `properties-sitemap.xml`, `property-types-sitemap.xml`.
- Objecten: https://www.javeaestateagent.com/properties-sitemap.xml (24-09-2026 21:33 UTC, HTTP 200, 26.154 bytes). **87 URL's, waarvan 86 objectpagina's** plus de overzichtspagina `/properties/`. Elke URL heeft de vorm `/properties/<type>-<n>-bed-javea-<volgnr>/` en bijna elke (83) heeft een afbeeldingstag.

Telling per type op basis van de slug (bron: dezelfde sitemap):

| Type | Aantal |
|---|---|
| villa | 52 |
| apartment | 14 |
| plot | 9 |
| commercial | 7 |
| townhouse | 4 |
| **totaal** | **86** |

`lastmod` van de objecten ligt tussen 29-06-2026 en 13-08-2026 (85 in augustus, 1 in juni) — het aanbod is dus deze zomer in één keer (opnieuw) ingeladen of aangeraakt; sindsdien (zes weken) geen wijziging in de sitemap.

Opvallend: tien `post-sitemap`-bestanden. Yoast splitst per 1.000 URL's, dus dat wijst op duizenden blogberichten — veel te veel voor een makelaarssite. Negen van de tien hebben een kapotte `lastmod` (`-0001-11-30`). Niet opgevraagd (limiet), maar zie de spam-aanwijzing onder 4.

## 4. Aanbodpagina en objectpagina

**Aanbodpagina:** https://www.javeaestateagent.com/properties/ (kruimelpad "Home › Properties" in de JSON-LD van de objectpagina), met deelpagina's per type: `/property-types/villas-for-sale-in-javea/`, `/apartments-for-sale-in-javea/`, `/plots-for-sale-in-javea/`, `/townhouses-for-sale-in-javea/`, `/commercial-for-sale-in-javea/`, plus `/properties-in-javea-under-200000/` en `/-under-300000/`. Niet apart opgevraagd (limiet); de URL's komen uit de sitemap en de navigatie van de objectpagina.

**Objectpagina getest:** https://www.javeaestateagent.com/properties/villa-3-bed-javea-13/ (24-09-2026 21:34 UTC, HTTP 200, 233.747 bytes, server-gerenderd).

Wat er staat (zichtbare tekst):
- Referentie: **JEA3868**
- Prijs: **€949,000** (ook in `<title>`: "Villa for Sale Javea Spain | 3 Bed | €949000")
- 3 slaapkamers, 2 badkamers
- Build Size: **286 M2**
- Plot Size: **N.A**
- Has Pool: No · Sea View: N.A
- Plaats: alleen "Javea" (in titel en kop "3 Bedroom Villa in Javea"); geen zone, straat of kaart
- Omschrijving: "Not Available, Contact here for more details"
- Energielabel: "(PENDING)"

**JSON-LD** (`<script type="application/ld+json">`, één blok): Yoast-standaardgraaf met `WebPage`, `ImageObject`, `BreadcrumbList`, `WebSite` en `Organization` (naam "Javea Estate Agent"). **Geen** `Offer`, `Product`, `RealEstateListing` of `Residence`; geen prijs, oppervlak, perceel of referentie in de gestructureerde data. Wel `datePublished: 2026-06-29`.

**og:-tags** (Yoast): `og:type article`, `og:locale en_GB`, `og:title` met prijs, `og:url`, `og:image` (1200×800), `og:site_name "Javea Property"`, en `og:description`: "Sale 3 bed villa with 2 baths for sale in Javea on a plot of 286m2 for only €949000 ...". Let op: de og-tekst noemt 286 m² als **perceel**, de pagina zelf als **bouwoppervlak** met perceel N.A — de sjabloontekst is dus niet betrouwbaar voor perceel/bouw.

Praktisch: referentie, prijs, slaap-/badkamers, bouwoppervlak en pool staan als platte tekst in de HTML naast vaste labels ("Ref No.:", "Build Size", "Plot Size") — makkelijk te lezen. Perceel en omschrijving ontbreken op dit object; hoe vaak dat bij de andere 85 zo is, is niet getoetst.

**Spam-aanwijzing.** In de voettekst staat een blok "Latest Articles" met zes links naar pagina's op ditzelfde domein zoals `/deposit-10-get-200-free-slots-uk/`, `/live-auto-french-roulette-casino-uk/`, `/best-bitcoin-casino-minimum-deposit-casino-uk/`. Dat zijn geen makelaarsartikelen. Samen met de tien post-sitemaps is de meest waarschijnlijke verklaring dat de WordPress-installatie is gekaapt voor SEO-spam (dit is mijn conclusie, niet bevestigd door het kantoor). Voor Deal Hunter betekent dit: het objectgedeelte zelf oogt intact, maar de site wordt kennelijk niet goed beheerd en de blogberichten moeten worden genegeerd.

## 5. Systeem achter de site

**WordPress, eigen opbouw met Elementor + JetEngine** — geen bekend vastgoed-CMS en geen bekende vastgoedplugin. Bewijs (bron: objectpagina en HTTP-headers, 24-09-2026 21:34 UTC):
- HTML-commentaar: "This site is optimized with the Yoast SEO plugin v28.5".
- `<meta name="generator">`: "Elementor 4.3.1" en "WP Rocket 3.19.4".
- Paden onder `/wp-content/themes/`: `hello-elementor`, `hello-elementor-child`. Onder `/wp-content/plugins/`: `elementor`, `elementor-pro`, `jet-engine` (custom post type "properties" en 64× `jet-listing` in de HTML), `elementskit-lite`, `dynamic-content-for-elementor`, `captcha-for-contact-form-7`, `wp-rocket`.
- Headers: `server: cloudflare`, `x-powered-by: PHP/8.2.30`, `cf-cache-status: DYNAMIC`. Geen `Set-Cookie` bij een gewone opvraging.
- Sitemaps door Yoast; robots.txt noemt `/wp-admin/`.
- Geen sporen van Inmoweb, Mediaelx/LetsINMO, Sooprema, Inmovilla, Witei, Houzez, WPResidence, Estatik of WP All Import in de HTML.

Aanwijzingen voor een bulk-import (niet bewezen): alle 86 slugs volgen precies hetzelfde sjabloon, fotobestanden heten `1-<hash>-56.jpg`, `2-<hash>-57.jpg` enz. in `/wp-content/uploads/2026/06/`, en de sjabloontekst in `og:description` is identiek van opbouw. Waarvandaan de import komt, is niet te zien.

Verwante domeinen: de contactlink op de objectpagina wijst naar `https://www.javeaproperty.com/contact/` en de knop "Request a Visit" naar `http://www.javea.properties/contact-us/`; `og:site_name` is "Javea Property". Hetzelfde kantoor lijkt dus meerdere domeinen te voeren — mogelijk staat het aanbod daar vollediger. Niet onderzocht.

Kantoor (voettekst, alleen bedrijfsgegevens): "Estate Agent In Javea, Suite C, Ctr Cabo La Nao 160, Javea, Alicante 03730" · telefoon 965 771 312 · e-mailadres staat op de site (door Cloudflare afgeschermd, niet uitgelezen).

## 6. Omvang en dekking Jávea / Benitachell / Moraira

- **86 objecten** in de sitemap (24-09-2026): 52 villa's, 14 appartementen, 9 percelen, 7 commercieel, 4 rijtjeswoningen.
- **Dekking: alles is gelabeld als Jávea.** 86 van de 86 slugs bevatten "javea"; alle vijf typepagina's heten "...for-sale-in-javea"; Benitachell, Moraira of andere plaatsen komen nergens voor in sitemap, navigatie of typepagina's. Kanttekening: op de geteste objectpagina staat geen zone of adres, dus of elk object werkelijk in Jávea ligt (en niet bijvoorbeeld op de grens met Benitachell) is per object niet te controleren.
- Voor Deal Hunter interessant: 9 percelen en 7 commerciële objecten, allemaal Jávea.

## Advies

**Lezen — met lage prioriteit.** Motivatie:
- robots.txt staat het toe; voorwaarden bestaan niet; de HTML is gewoon leesbaar.
- Klein aanbod (86) en dunne data (geen omschrijving, geen perceel, geen zone op het geteste object). De og-tekst verwart perceel en bouwoppervlak.
- Spam-besmetting maakt de site onbetrouwbaar als bron voor alles buiten `/properties/`.

Spelregels bij het lezen: alleen URL's uit `properties-sitemap.xml`, geen `?p=`, geen `/search/`; eigen herkenbare user-agent; minstens twee seconden tussen opvragingen; velden lezen uit de labels "Ref No.:", "Build Size", "Plot Size" en de prijs in `<title>`; blogberichten negeren.

⏸️ **ACTIE VOOR JAN:** vraag het kantoor (algemeen kanaal) of het aanbod ook op javeaproperty.com of javea.properties staat en of ze een exportfeed hebben — de site zelf laat niet zien waar de 86 objecten vandaan komen. En wees erop bedacht dat hun site vermoedelijk gehackt is; als je met ze spreekt, is dat een nuttige tip voor hen.

## Bronnen en tijdstippen

| Wat | URL | Wanneer (UTC) | Resultaat |
|---|---|---|---|
| robots.txt | https://www.javeaestateagent.com/robots.txt | 24-09-2026 21:33 | HTTP 200, 780 bytes |
| Sitemap-index | https://www.javeaestateagent.com/sitemap_index.xml | 24-09-2026 21:33 | HTTP 200, 13 deelsitemaps (Yoast) |
| Objecten-sitemap | https://www.javeaestateagent.com/properties-sitemap.xml | 24-09-2026 21:33 | HTTP 200, 87 URL's (86 objecten) |
| Objectpagina | https://www.javeaestateagent.com/properties/villa-3-bed-javea-13/ | 24-09-2026 21:34 | HTTP 200, 233.747 bytes |
| Pagina-sitemap | https://www.javeaestateagent.com/page-sitemap.xml | 24-09-2026 21:35 | HTTP 200, 6 pagina's, geen legal/privacy |

Niet gedaan (en waarom): aanbodpagina `/properties/` en typepagina's zelf openen (limiet van vijf bereikt; URL's bekend uit sitemap en navigatie); post-sitemaps en `sitemap27/24.xml` (limiet); zoekmachine-onderzoek (sessiebudget op); verwante domeinen javeaproperty.com en javea.properties (buiten opdracht).

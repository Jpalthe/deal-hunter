# Engel & Völkers Jávea — toets op automatisch lezen

**Datum:** 24-09-2026
**Site:** https://www.engelvoelkers.com/es/en/shops/valencia-javea
**Advies: OVERSLAAN.** De gebruiksvoorwaarden van engelvoelkers.com verbieden automatisch lezen uitdrukkelijk, en het platform is eigen bouw zonder exportfeed. Het onderzoek is daarom na stap 2 gestopt; sitemap en objectpagina zijn bewust niet opgehaald.

## Wat is er opgehaald (4 verzoeken, telkens minstens 2 seconden ertussen)

| # | URL | Resultaat |
|---|-----|-----------|
| 1 | https://www.engelvoelkers.com/es/en/shops/valencia-javea/robots.txt | 404 (robots.txt staat alleen op de root van het domein) |
| 2 | https://www.engelvoelkers.com/robots.txt | 200, 42 regels |
| 3 | https://www.engelvoelkers.com/es/en/shops/valencia-javea | 200, kantoorpagina (toegestaan volgens robots.txt) |
| 4 | https://www.engelvoelkers.com/de/en/terms-of-use | 200, gebruiksvoorwaarden (link uit de voettekst van pagina 3) |

## 1. robots.txt — DEELS toegestaan

Bron: https://www.engelvoelkers.com/robots.txt (24-09-2026). Relevante regels voor `User-agent: *`:

```
User-agent: *
Disallow: */search/*
Disallow: */suche?*
Disallow: */propertysearch?*
Disallow: */busca?*
(… dezelfde regel in nog zeven talen …)
Disallow: /*/account/
```

- **Zoek- en resultaatpagina's zijn verboden** (`*/propertysearch?*`, `*/search/*`, `*/busca?*` enz.). Precies de pagina met het volledige aanbod van het kantoor valt hieronder.
- **Objectpagina's (`/es/en/exposes/<id>`) en kantoorpagina's zijn niet uitgesloten.**
- Sitemaps staan in robots.txt: o.a. `https://www.engelvoelkers.com/es/sitemap.xml` (niet geopend, zie stap 3).

## 2. Gebruiksvoorwaarden — scraping VERBODEN

Bron: https://www.engelvoelkers.com/de/en/terms-of-use — "General Terms of Use and Business", versie 2.0, stand februari 2026 (opgehaald 24-09-2026). Artikel 7 "User obligations and rights of use":

> 7.2. Any form of automated reading, extraction, or collection of content and data from the Platform (in particular through "text and data mining") for any purpose, in particular for the development or training of software or artificial intelligence systems, is expressly prohibited.

> 7.3. The data and exposés obtained through your queries may not be used for commercial purposes or to build your own database.

> 7.4. E&V is the owner of all property rights (e.g., copyrights and trademark rights) to the design and functionalities of the Platform and the database. […]

Dit is ondubbelzinnig: automatisch lezen is verboden, en een eigen database bouwen uit hun aanbod ook. **Hier is gestopt.**

## 3. Sitemap — niet geopend

robots.txt noemt `https://www.engelvoelkers.com/es/sitemap.xml` (plus per land één sitemap en `sitemap_shop_profile.xml`). Niet opgehaald en niet geteld, omdat stap 2 het verbiedt.

## 4. Objectpagina — niet geopend

De kantoorpagina toont zes koopobjecten met links van de vorm `https://www.engelvoelkers.com/es/en/exposes/<uuid>`, bijvoorbeeld `…/exposes/047cd24a-ff83-5fdd-b279-ce8960dd29ab`. Geen daarvan is geopend; JSON-LD en og-tags van een objectpagina zijn dus **onbekend**.

Wat wél op de kantoorpagina zelf staat (bron: pagina 3, 24-09-2026):
- JSON-LD `RealEstateAgent`: naam "Engel & Völkers Valencia Jávea", adres Avenida del Mediterráneo 238, 03738 Jávea; algemeen telefoonnummer +34 963 51 78 97; algemeen e-mailadres Valencia@engelvoelkers.com; openingstijden ma–vr 09:00–18:00.
- og-tags aanwezig (`og:title` "Engel & Völkers Valencia Jávea", `og:type` website, `og:image`).
- De pagina bevat de volledige gegevens van de zes teasers in de `__NEXT_DATA__`-JSON: prijs, woonoppervlak, kamers, type, plaatsaanduiding. Objectpagina's zijn dus vrijwel zeker ook machinaal leesbaar — maar dat mag niet.

## 5. Systeem achter de site — EIGEN BOUW

Aanwijzingen (pagina 3, 24-09-2026):
- HTTP-header `x-powered-by: Next.js`, `x-vercel-cache: HIT`, `server: cloudflare` → Next.js-app op Vercel, achter Cloudflare.
- `__NEXT_DATA__` met `buildId: "spearhead"`, paden `/_next/static/…`, afbeeldingen via ucarecdn.com / Google Cloud Storage.
- Geen spoor van Inmoweb, Mediaelx/LetsINMO, Sooprema, Inmovilla, Witei of WordPress.

Dit is het wereldwijde E&V-platform, geen Spaans makelaars-CMS. Er is dus **geen bekende exportfeed** waar je om kunt vragen.

## 6. Omvang en dekking Jávea/Benitachell/Moraira — ONBEKEND

- De kantoorpagina toont een blok van **6 koop- en 6 huurobjecten** (`totalHits: 6` per blok is de blokgrootte, niet het totale aanbod). Het volledige overzicht zit achter de zoekpagina `…/propertysearch?masterDataShopIds[]=906d38b1&…`, die robots.txt verbiedt.
- Alle twaalf getoonde teasers dragen in de paginadata als kantoornaam "Engel & Völkers Valencia MMC" en als plaatsaanduiding "Dénia" (Google-plaatscomponent). De zes koopobjecten: 3 huizen en 3 appartementen, € 199.000 – € 590.000, 57–193 m² woonoppervlak. **Niet geverifieerd** of dat werkelijk Dénia is of een eigenaardigheid van de plaatscodering — de objectpagina's zijn niet geopend.
- Het kantoor is een vestiging van de licentiepartner Valencia (telefoonnummer en e-mail zijn van Valencia); de eigen tekst zegt "buying or renting a property in Jávea and surroundings".

Schatting totaal aanbod: **niet te geven** zonder de verboden zoekpagina. Aandeel Jávea/Benitachell/Moraira: onbekend; de zichtbare steekproef wijst eerder naar Dénia.

## Advies en alternatief voor Jan

**Overslaan** als automatische bron. Er is geen feed om te vragen (eigen platform), en de voorwaarden sluiten zowel automatisch lezen als een eigen database uit.

⏸️ ACTIE VOOR JAN (menselijke route, geen scraping): wil je toch zicht op hun stille aanbod, dan is de enige nette weg het kantoor zelf — Avenida del Mediterráneo 238, Jávea, +34 963 51 78 97, Valencia@engelvoelkers.com — en een zoekprofiel of samenwerking afspreken. Objecten die E&V ook op portalen zet, vallen onder de voorwaarden van dát portaal, niet onder deze toets.

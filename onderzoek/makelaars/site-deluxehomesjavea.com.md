# Deluxe Homes Javea — www.deluxehomesjavea.com

Toets op automatisch lezen · TREE Deal Hunter · datum: 24-09-2026

**Advies: feed vragen** — robots.txt staat het lezen toe en de pagina's zijn
technisch prima leesbaar (alle objectgegevens zitten als nette JSON in de HTML),
maar de gebruiksvoorwaarden verbieden uitdrukkelijk "extraction, re-use" en
sluiten kopieën voor "commercial or professional activities" uit. Wij lezen
voor een commercieel doel, dus automatisch lezen mag hier niet. De site draait
op het Tesoro-platform en de objecten komen binnen via een Kyero-import; er is
dus een exportfeed in het spel. Vraag het kantoor om die feed (Kyero-XML) of om
een samenwerkingsafspraak.

Kanttekening voor Jan: de ~1.216 objecten zijn voor een groot deel
**gedeelde/collega-aanbod** — de interne referenties (`ENJ-VI-00514-D`,
`TACAL4724`, `4917`) horen bij andere kantoren. Het eigen, mogelijk niet op
portalen gepubliceerde aanbod is waarschijnlijk maar een klein deel
[te verifiëren]. Dat maakt een feed-afspraak nuttiger dan scrapen: je wilt juist
weten wélke objecten exclusief van dit kantoor zijn.

## Kantoor

- Bedrijf: DELUXE HOMES JAVEA, S.L. (site-naam "DELUXE HOMES JÁVEA")
- Algemeen contact: +34 679 341 493 · info@deluxehomesjavea.com
- Kantooradres: niet in de voettekst gevonden; de voorwaarden verwijzen naar
  een "Legal Notice" die niet apart is opgehaald (budget).
- Talen: EN, ES, NL, DE, FR. Menu: Buy, Rent, Projects, Lifestyle, Blog.
- Logo's van RAICV en APIAL in de voettekst (branchekoepels).
- Bron: voettekst van https://www.deluxehomesjavea.com/en/properties/property-dhj2235a
  en https://www.deluxehomesjavea.com/en/general-terms (beide 24-09-2026)

## 1. robots.txt — toegestaan

Bron: https://www.deluxehomesjavea.com/robots.txt (HTTP 200, 24-09-2026, via
Cloudflare). Volledige inhoud:

```
User-agent: *
Disallow: /404
Disallow: /payload-error
Disallow: /en/not-found
Disallow: /es/not-found
Disallow: /nl/not-found
Disallow: /de/not-found
Disallow: /fr/not-found
Allow: /

Sitemap: https://www.deluxehomesjavea.com/sitemap.xml
```

Uitleg: alleen foutpagina's zijn uitgesloten. Alles daarbuiten, dus ook
`/en/properties` en `/en/properties/property-…`, is met `Allow: /` voor elke
`User-agent: *` toegestaan. Geen `Crawl-delay`.

## 2. Voorwaarden — verbod gevonden

Bron: https://www.deluxehomesjavea.com/en/general-terms (HTTP 200, 24-09-2026),
"General Terms of Use", eigenaar DELUXE HOMES JAVEA, S.L. Artikel 4
("Intellectual and industrial property rights") zegt letterlijk:

> "The reproduction, transformation, distribution, public communication,
> making available, extraction, re-use, re-sending or use of any nature, by any
> means or procedure, of any of them is expressly prohibited, except in cases
> legally permitted or authorised by the holder of the corresponding rights."

en daarna:

> "The User may view and obtain a temporary private copy of the content for
> his/her exclusive personal and private use on his/her computer systems
> (software and hardware), provided that this is not for the purpose of
> carrying out commercial or professional activities. The User must refrain
> from obtaining or attempting to obtain the content by means or procedures
> other than those which, in each case, have been made available or indicated
> for this purpose or which are commonly used on the Internet (provided that
> the latter do not involve a risk of damage to or disablement of the Website)."

Het woord "scraping" komt niet voor, maar "extraction" en "re-use" zijn expliciet
verboden en een kopie voor commercieel of professioneel gebruik is uitgesloten.
Voor TREE Deal Hunter (commercieel doel) is dat een verbod. Artikel 3.2 meldt
verder dat de inhoud deels van "third-party sources" komt — past bij het
gedeelde aanbod hieronder.

Andere juridische pagina's in de voettekst (niet opgehaald, budget):
`/en/privacy-policy`, `/en/cookie-policy`.

## 3. Sitemap — aanwezig, 1.216 objecten

- `Sitemap:`-regel in robots.txt → https://www.deluxehomesjavea.com/sitemap.xml
  (HTTP 200, 24-09-2026). Dit is een **sitemap-index** met 7 deelbestanden:
  `/sitemaps/sitemap-1.xml` t/m `sitemap-7.xml` (1-6: 1.000 URL's elk,
  7: 136 URL's).
- Totaal 6.136 URL's. Daarvan:

| Soort | Aantal |
|---|---|
| Objectpagina's `/{taal}/properties/property-…` | 6.080 (1.216 objecten × 5 talen) |
| Aanbodpagina's `/{taal}/properties` | 5 |
| Blogartikelen (7 × 5 talen) | 35 |
| Overig (home, contact, our-company, blog-overzicht) | 16 |

- Objectslugs: 1.154 × `property-dhjNNNNa`, 59 × `property-delNNN`, 3 × overig
  (`dhjvN`, `dhjtN`, `dhjdN`). Alle slugs zijn uniek over de talen heen; elke
  URL heeft `xhtml:link`-alternates voor de vijf talen.
- `lastmod`: het gros staat op 2026-09-15 (839 van de 1.000 in deel 1), met
  dagelijkse bijwerkingen tot en met 24-09-2026 — het aanbod wordt actief
  bijgehouden.
- De slugs bevatten geen plaatsnaam; de plaats staat alleen ín de pagina.

## 4. Aanbodpagina en objectpagina

**Aanbodpagina:** https://www.deluxehomesjavea.com/en/properties (HTTP 200,
24-09-2026). Twaalf objecten per pagina, pagineringslinks tot `?page=102`
→ ca. 1.213–1.224 objecten, in lijn met de 1.216 uit de sitemap. Filters:
prijsklasse, slaapkamers, badkamers (geen plaatsfilter met aantallen).
Alle gegevens van de 12 objecten staan als JSON in de HTML
(Astro-island `PropertiesPageIsland`), inclusief `city`, `price`, `type`,
`transaction`, `plot_size`, `builded_area` en coördinaten (`"type":"Point"`).

**Objectpagina:** https://www.deluxehomesjavea.com/en/properties/property-dhj2235a
(HTTP 200, 24-09-2026, 230 kB, `cf-cache-status: DYNAMIC`)

- `<script type="application/ld+json">`: **aanwezig, maar leeg qua object** —
  alleen `@type: WebSite` met `publisher: Tesoro (https://tesorohq.io)`; geen
  prijs, geen adres, geen `RealEstateListing`/`Offer`.
- og-tags: `og:title` = "Property #DHJ2235A | EN | DELUXE HOMES JÁVEA",
  `og:type` = website, `og:url`, `og:image` (Cloudflare Images via
  tesoro-image-delivery.tesoro.properties, met watermerk-overlay);
  `twitter:card` = summary_large_image. `meta description` = "Astro description"
  (placeholder). **Geen prijs of oppervlakte in de og-tags.**
- Zichtbare tekst: Ref. DHJ2235A · villa · for sale · Jávea (Piver) ·
  € 775.000 · Total 1.088 m² (perceel) · House 202 m² (bebouwd) ·
  4 slaapkamers · 2 badkamers · privézwembad, vloerverwarming, kelder.
- Verborgen maar netjes gestructureerd: de Astro-island-props bevatten
  `"tesoro_reference":"DHJ2235A"`, `"reference":"V684"` (interne ref),
  `"price":775000`, `"currency":"EUR"`, `"transaction":"for_sale"`,
  `"type":"villa"`, `"builded_area":202`, `"plot_size":1088`,
  `"number_of_bedrooms":4`, `"number_of_bathrooms":2`,
  `"new_construction":false`, `"status":"active"`, `"energy_rating":null`,
  beschrijvingen in 5 talen, en per foto `"tags":["kyero","import"]`.
- Geen `<meta name="robots">`, dus indexeerbaar.

## 5. Systeem achter de site — eigen bouw op het Tesoro-platform

- `<meta name="generator" content="Astro v5.13.2">`; scripts onder `/_astro/`
  (`PropertyPreview`, `SinglePropertyFormWithCalendar`, `PropertiesPageIsland`).
- JSON-LD `publisher` = "Tesoro", https://tesorohq.io; beelden via
  `tesoro-image-delivery.tesoro.properties` en `cdn-tesoro.fra1.digitaloceanspaces.com/deluxe-homes/`;
  "Powered by" in de voettekst.
- robots.txt sluit `/payload-error` uit en de HTML bevat 4× "PAYLOAD":
  Payload CMS als contentlaag.
- Fototags `kyero` + `import`: objecten komen binnen via een Kyero-XML-feed.
- Geen Inmoweb, Mediaelx/LetsINMO, Sooprema, Inmovilla, Witei of WordPress
  gevonden. Cloudflare als CDN; geen cookies bij een kale GET.

Conclusie: **eigen bouw (Astro + Payload) op het Tesoro-vastgoedplatform**,
gevoed met een Kyero-import. Niet in de lijst van bekende feed-systemen, maar
een feed bestaat aantoonbaar.

## 6. Omvang en dekking Jávea / Benitachell / Moraira

- Geschat aantal objecten: **1.216** (sitemap, bevestigd door paginering 102 × 12).
- Dekking: alleen een steekproef van de 12 objecten op de eerste aanbodpagina
  (24-09-2026): **Jávea 7, Altea 2, Dénia 1, Benissa 1, Calpe 1**; geen
  Benitachell of Moraira in de steekproef. Prijzen in die steekproef: € 285.000
  t/m € 2.590.000, mediaan € 775.000; types: 7 villa, 3 finca, 2 apartment;
  alle `for_sale`, geen nieuwbouw.
- Het aandeel Jávea/Benitachell/Moraira over het hele aanbod is **onbekend**
  [te verifiëren]; het kantoor zit in Jávea en de eerste pagina is ruim
  Jávea-gewogen, maar 12 van 1.216 is te weinig om iets over het geheel te
  zeggen. Een volledige telling zou alle 102 pagina's vereisen, wat de
  voorwaarden niet toestaan.
- Interne referenties op pagina 1: `V684`, `V692`, `A323`, `V690`, `4917`,
  `TACAL4724`, `ENJ-VI-00514-D`, `ENJ-AP-00253-D`, `ENJ-VI-00508-E`,
  `ENJ-VI-00513-D`, `ENJ-VI-00511-D`, `ENJ-VI-00512-D`. Minstens drie
  referentiestelsels → gedeeld aanbod van meerdere kantoren; het eigen aanbod
  lijkt de `V`/`A`-reeks [te verifiëren].

## Wat is opgehaald (verzoeklog, 24-09-2026, ca. 23:08–23:11 lokale tijd)

Alle verzoeken met minimaal 2 seconden tussenruimte en een herkenbare
User-Agent (`TREE-DealHunter-check/1.0`). Niet ingelogd, geen formulieren.

| # | URL | Soort | Status |
|---|---|---|---|
| 1 | /robots.txt | machinebestand | 200 |
| 2 | /sitemap.xml | sitemap-index | 200 |
| 3–9 | /sitemaps/sitemap-1.xml … sitemap-7.xml | sitemap-delen | 200 |
| 10 | /en/properties/property-dhj2235a | HTML-objectpagina | 200 |
| 11 | /en/general-terms | HTML-voorwaarden | 200 |
| 12 | /en/properties | HTML-aanbodpagina | 200 |

Drie HTML-pagina's (binnen het budget van vijf). De zeven sitemap-delen zijn
apart opgehaald omdat stap 3 een telling vraagt en de index anders niets zegt;
dat zijn XML-bestanden die de site zelf in robots.txt aanbiedt aan robots.
Interpretatie: "vijf pagina's" = vijf HTML-pagina's. Mocht het strenger bedoeld
zijn, dan is dit de afwijking.

## ⏸️ ACTIE VOOR JAN

- Deluxe Homes Javea benaderen (info@deluxehomesjavea.com / +34 679 341 493)
  met de vraag om hun Kyero-feed of een samenwerkingsafspraak, met de
  nadruk op het **eigen** aanbod (renovatieobjecten, percelen) — niet op het
  gedeelde aanbod dat toch al op portalen staat.
- Niet automatisch laten lezen zolang artikel 4 van de voorwaarden zo staat.

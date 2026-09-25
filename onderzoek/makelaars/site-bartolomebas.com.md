# Bartolomé Bas — bartolomebas.com

Toets op automatisch lezen · TREE Deal Hunter · datum: 24-09-2026

**Advies: feed vragen** — robots.txt staat het lezen van de aanbodpagina's toe en
de pagina's zijn technisch goed uitleesbaar, maar de *Condiciones generales de
uso* (clausule 4) verbieden uitdrukkelijk extractie en hergebruik van de inhoud
voor commerciële of professionele doeleinden, tenzij de eigenaar daar
toestemming voor geeft. Automatisch lezen zonder toestemming valt dus af. De site
draait op een eigen WordPress-bouw (geen Inmoweb/Mediaelx/Sooprema-feed), maar
het is een groot kantoor (schatting ±120 objecten, ruim 90% in Jávea, Benitachell
en Moraira). Dat is te waardevol om over te slaan: vraag het kantoor om
toestemming of een export (de voorwaarden laten dat met zoveel woorden toe).

## Kantoor

- Bedrijf: Bartolomé Bas, S.L. (site-naam "Inmobiliaria Bartolomé Bas";
  rechtspersoon volgens de gebruiksvoorwaarden)
- Kantooradressen (voettekst): Avenida de la Libertad 2 bajo, 03738 Jávea –
  Arenal (Alicante) en Ctra. Portichol 31, 03738 Jávea (Alicante)
- Algemeen contact: +34 96 579 53 86 · info@bartolomebas.com
- Eigen omschrijving: ruim 45 jaar ervaring, verkoop én bouw van woningen in
  Jávea en Dénia; diensten "Bas 360", Construcción, Arquitectura, Legal,
  waardebepaling, verhuur (menu `alquiler-de-propiedades`). Site in vier talen
  (es, en, fr, de).
- Bron: voettekst en menu van
  https://bartolomebas.com/propiedades/villa-con-4-dormitorios-con-vistas-de-180-entre-el-montg-y-el-mediterrneo-en-la-zona-de-trencall-jvea/
  en clausule 1 van https://bartolomebas.com/condiciones-generales-de-uso/ (beide 24-09-2026)

## 1. robots.txt — toegestaan

Bron: https://bartolomebas.com/robots.txt (HTTP 200, Last-Modified 29-10-2025,
opgehaald 24-09-2026). Eén blok `User-agent: *`. Er staat **geen** `Disallow` op
`/propiedades/` of op een andere aanbodmap. Wat wél geblokkeerd is (relevante
regels, letterlijk):

```
User-agent: *
Disallow: /*?_ga=          (en verder ?_gl= ?gclid= ?utm_… ?fbclid= ?glang= …)
Disallow: /*?p=
Disallow: /*?sort=
Disallow: /*?rand=
Disallow: /wp-admin/
Allow: /wp-admin/admin-ajax.php
Disallow: /wp-includes/
Disallow: /wp-content/plugins/
Disallow: /wp-content/themes/
Disallow: /*?s=
Disallow: /*&paged_
Disallow: /feed/
Disallow: /*/feed/$
Disallow: /trackback
Disallow: /*?orderby=
Disallow: /*?filter_
Sitemap: https://bartolomebas.com/sitemap_index.xml
```

Uitleg: alleen tracking-parameters, de WordPress-beheeromgeving, plugin- en
themabestanden, RSS-feeds, zoekresultaten (`?s=`), sorteer-/filterparameters en
back-upbestanden zijn uitgesloten. Gewone object-URL's zoals
`/propiedades/<slug>/` (en de taalversies `/en/`, `/fr/`, `/de/`) mag een
`User-agent: *` lezen. Let op: sorteren of filteren via URL-parameters
(`?sort=`, `?orderby=`, `?filter_…`) is wél verboden — dus alleen de kale
URL's gebruiken.

## 2. Voorwaarden — verbod gevonden

Bron: https://bartolomebas.com/condiciones-generales-de-uso/ (HTTP 200,
24-09-2026), titel "Condiciones generales de uso", 10 clausules, houder
"BARTOLOME BAS, S.L.".

Clausule 4 (*Derechos de propiedad intelectual e industrial*) zegt, samengevat
in gewone taal:

- Er wordt geen enkel recht op de website of onderdelen ervan overgedragen; de
  gebruiker mag niets reproduceren, transformeren, verspreiden, openbaar maken,
  beschikbaar stellen, **extraheren, hergebruiken** of doorsturen — op welke
  manier ook — behalve waar de wet dat toestaat of de rechthebbende het
  autoriseert. Kernwoorden letterlijk: "quedando expresamente prohibidos al
  Usuario la reproducción, […] extracción, reutilización".
- De gebruiker mag alleen een tijdelijke privékopie maken voor strikt
  persoonlijk gebruik, en uitdrukkelijk **niet** voor commerciële of
  professionele activiteiten.
- De gebruiker moet zich onthouden van het verkrijgen van de inhoud via andere
  middelen dan die de site aanbiedt of die op internet gebruikelijk zijn (mits
  die geen schade of uitval van de website kunnen veroorzaken).

Conclusie: **ja, verbod.** Deal Hunter is een professionele/commerciële
toepassing, dus de privékopie-uitzondering geldt niet, en "extracción" en
"reutilización" zijn met naam en toenaam verboden. De ontsnappingsclausule is
"autorizado por el titular": met toestemming van het kantoor mag het wél.

Kanttekeningen:
- https://bartolomebas.com/aviso-legal/ (in de voettekst, naast
  `politica-de-privacidad` en `politica-de-cookies`) is **niet** gelezen: het
  paginabudget was op. Bij een volgende ronde alsnog nalopen; het verbod in de
  CGU staat hoe dan ook.
- https://bartolomebas.com/legal/ (voettekst "Legal") bleek de dienstenpagina van
  hun juridische afdeling ("Servicio jurídico…"), geen voorwaarden.

## 3. Sitemap — aanwezig (Rank Math, gesplitst)

- Index: https://bartolomebas.com/sitemap_index.xml (uit robots.txt; HTTP 200,
  24-09-2026), gegenereerd door Rank Math SEO. Negen deelsitemaps: `post`,
  `page`, **`propiedades-sitemap1/2/3.xml`** (alle drie lastmod 24-09-2026),
  `poblacion`, `zona`, `tipo`, `local`.
- Gelezen: https://bartolomebas.com/propiedades-sitemap1.xml → **201 URL's**,
  allemaal onder `/propiedades/`: 1 archiefpagina + **200 object-URL's**
  (dus 200 op het patroon villa/propiedad/parcela enz.). Geen afbeeldingen in
  de sitemap; lastmod 23/24-09-2026.
- Belangrijk: de sitemap bevat **vier taalversies per object** (Spaans zonder
  voorvoegsel, `/en/`, `/fr/`, `/de/`). In sitemap 1: 119 × `/de/`, 77 × `/fr/`,
  2 × `/en/`, 2 × Spaans. De 200 URL's zijn dus géén 200 objecten.
- Niet gelezen (budget): `propiedades-sitemap2.xml` en `-sitemap3.xml`. Rank
  Math splitst standaard per 200 URL's, dus totaal 401–600 object-URL's; gedeeld
  door vier talen ≈ **100–150 unieke objecten**, beste schatting ±120 (de
  Duitse reeks in sitemap 1 lijkt compleet met 119) [te verifiëren].

## 4. Aanbodpagina en objectpagina

**Aanbodpagina** (uit het menu, niet geopend):
https://bartolomebas.com/todas-las-propiedades/ (menu-item "Propiedades");
daarnaast het archief https://bartolomebas.com/propiedades/ (breadcrumb
"Propiedades", voettekst "Otras poblaciones") en
https://bartolomebas.com/alquiler-de-propiedades/ (verhuur). De voettekst
heeft ook plaats- en zonepagina's (Javea, Denia, Jesús Pobre, Moraira/Teulada,
Pedreguer; Puerto, Tosalet/Adsubia, Montgó, Balcón al Mar/Portichol, La
Lluca/Pinosol, Arenal/Montañar, Villas de Lujo).

**Objectpagina:** https://bartolomebas.com/propiedades/villa-con-4-dormitorios-con-vistas-de-180-entre-el-montg-y-el-mediterrneo-en-la-zona-de-trencall-jvea/
(HTTP 200, 24-09-2026, 218 kB)

- `<script type="application/ld+json">`: **aanwezig** (1 blok, Rank Math
  `@graph`): RealEstateAgent/Organization, WebSite, ImageObject, BreadcrumbList,
  WebPage, Article (+ auteur). **Geen** prijs, oppervlakte, Offer, Product of
  RealEstateListing — de JSON-LD is puur SEO-boilerplate.
- og-tags: **aanwezig**, zelfs dubbel (Rank Math + thema): `og:title`,
  `og:description` (eerste alinea van de omschrijving), `og:url`, `og:image`
  (1536×1024), `og:site_name`, `og:locale` = es_ES, `og:updated_time`
  = 2026-09-24T10:52. Geen prijs of oppervlakte in og.
- De echte gegevens staan als gewone tekst in de HTML (JetEngine-velden,
  klasse `jet-listing-dynamic-field__content`), goed uitleesbaar:
  - Referentie: **REF. 1114** · Type: Chalet · Zone: Trencall · Plaats: Jávea
  - Prijs: **799.000 €** (ook als kaal getal `799000 €`)
  - Bebouwd: 161 m² · Perceel: 711 m² · 4 slaapkamers · 2 badkamers
  - Energielabel: "EN TRÁMITE"; omschrijving in vier talen (hreflang via WPML)
  - Bijzonderheid: de shortcode `[bws_pdfprint display='pdf']` staat onverwerkt
    op de pagina (PDF-plugin werkt niet) — onschuldig, wel een teken van een
    handmatig onderhouden site.

## 5. Systeem achter de site

**WordPress, eigen bouw** — geen Inmoweb, Mediaelx/LetsINMO, Sooprema,
Inmovilla of Witei (nul sporen in HTML, paden of cookies). Aanwijzingen
(objectpagina en headers, 24-09-2026):

- `<meta name="generator" content="WPML ver:4.9.7">`; paden `/wp-content/…`;
  `<link rel="https://api.w.org/" href="https://bartolomebas.com/wp-json/">`.
- Thema **Bricks** met child-thema `bricks-child-9` (883 `brxe-`-klassen).
- **JetEngine** (Crocoblock) voor het custom post type `propiedades` en de
  dynamische velden (prijs, m², ref) — LiteSpeed-tag `d7b_propiedades`.
- Rank Math SEO (sitemaps, JSON-LD), WPML (es/en/fr/de), LiteSpeed Cache 7.9.1
  + QUIC.cloud (html-commentaar "Page cached by LiteSpeed Cache"), PDF & Print
  (`bws_pdfprint`).
- Server: LiteSpeed, PHP 8.4.25, Plesk. Geen `Set-Cookie` op de objectpagina
  (gastcache).
- Mogelijke machine-interface: de WordPress REST API (`/wp-json/`). Of het
  post type `propiedades` daar zichtbaar is, is **niet getest**; gebruik ervan
  valt onder hetzelfde verbod uit de voorwaarden.

Classificatie: **WordPress (Bricks + JetEngine, eigen bouw)** — geen bekende
standaard-exportfeed.

## 6. Omvang en dekking Jávea

- Geschat aanbod: **±120 objecten** (bandbreedte 100–150, zie §3) [te verifiëren].
- Dekking op basis van de 200 slugs in sitemap 1 (alle talen; 182 slugs noemen
  een plaats): Jávea 160 (88%), Dénia 10 (5%), Benitachell/Cumbre del Sol 7
  (4%), Moraira 4 (2%), Pedreguer 3, Pego 2, Gata 2, Teulada 1, Benissa 1,
  Beniarbeig 1. **Jávea + Benitachell + Moraira ≈ 171 van 182 ≈ 94%.**
- Typen in de slugs (talen door elkaar): villa/chalet 93, perceel
  (Grundstück/terrain/solar) 35, appartement 29, penthouse 18, garage 5,
  bar-restaurant 4, finca 2. Opvallend veel percelen en een paar
  investeringsobjecten (bar-restaurant eerste lijn Montañar) — relevant voor
  Deal Hunter.

## Werkwijze en beperkingen

- Zes ophaalacties, elk minstens twee seconden na elkaar, met een herkenbare
  user-agent: robots.txt, sitemap_index.xml, propiedades-sitemap1.xml, één
  objectpagina, /legal/ en /condiciones-generales-de-uso/. Dat is **één meer
  dan het budget van vijf**: de eerste "Legal"-link uit de voettekst bleek een
  dienstenpagina, en zonder de voorwaarden was geen advies mogelijk. Drie van
  de zes zijn machinebestanden (robots, twee sitemaps), drie zijn pagina's.
- Niet ingelogd, geen formulieren gebruikt, niets omzeild.
- Niet bekeken: aviso-legal, propiedades-sitemap2/3, page-sitemap, de
  aanbodpagina `todas-las-propiedades`, de verhuurpagina.
- Zoekmachine-onderzoek was niet mogelijk (zoekbudget van de sessie was op).

## ⏸️ ACTIE VOOR JAN

- Wil je dit kantoor als bron? Vraag dan Bartolomé Bas (info@bartolomebas.com,
  +34 96 579 53 86) om toestemming of een export van het aanbod — hun eigen
  voorwaarden noemen "autorizado por el titular" als uitweg. Tot die tijd:
  **niet automatisch lezen.**

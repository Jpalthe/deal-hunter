# A.V. Costamar S.L. — toets op automatisch lezen

**Website:** https://www.avcostamar.com
**Datum toets:** 24-09-2026
**Opgehaald (5 van max. 5 pagina's, 2 s tussenpauze):** robots.txt, wp-sitemap.xml, wp-sitemap-posts-property-1.xml, één objectpagina, /aviso-legal/

## Advies: LEZEN — met één voorbehoud

robots.txt staat het toe, de pagina's zijn gewoon leesbaar en prijs, referentie,
oppervlakte, plaats en zelfs GPS-coördinaten staan in vaste HTML-velden. Er is
geen JSON-LD, maar dat is niet nodig. Voorbehoud: de pagina
`/condiciones-generales` bestaat (footerlink) maar is niet gelezen omdat het
paginabudget op was — die eerst bekijken (1 pagina) vóór een volledige leesronde.

## 1. robots.txt — toegestaan

Bron: https://www.avcostamar.com/robots.txt (24-09-2026, HTTP 200). Volledige inhoud:

```
# Termly scanner
User-agent: TermlyBot
Allow: /

User-agent: *
Disallow: /wp-admin/
Allow: /wp-admin/admin-ajax.php

Sitemap: https://www.avcostamar.com/wp-sitemap.xml
```

Voor `User-agent: *` is alleen `/wp-admin/` verboden. De objectpagina's staan
onder `/propiedad/…` en de aanbodpagina's onder `/estado-propiedad/…` en
`/ciudad-propiedad/…` — allemaal toegestaan.

## 2. Gebruiksvoorwaarden — geen verbod gevonden (deels gecontroleerd)

- **Aviso Legal** — https://www.avcostamar.com/aviso-legal/ (24-09-2026, HTTP 200).
  Bevat uitsluitend de bedrijfsidentificatie volgens art. 10 LSSI (Ley 34/2002):
  bedrijfsnaam A.V. Costamar, S.L., CIF B53047791, kantoor Avda. Jaime I, 15,
  03730 Jávea, telefoon 966 460 047, e-mail info@avcostamar.com, inschrijving
  Registro Mercantil Alicante. Geen gebruiksvoorwaarden, geen woord over
  scraping, robots, reproductie of databankrechten (gezocht op: scrap, robot,
  automat, extrac, reproduc, indexa, base de datos, uso comercial, crawler,
  copiar, descarg, minería — 0 treffers).
- **Condiciones Generales** — `/condiciones-generales` (footerlink op de
  objectpagina). **Niet gelezen** (paginabudget). Ook aanwezig:
  `/politica-de-privacidad`, `/politica-de-cookies`.

## 3. Sitemap — 44 object-URL's

- Sitemap-index: https://www.avcostamar.com/wp-sitemap.xml (24-09-2026) met
  7 deelsitemaps: pages, **property**, agent, en de taxonomieën
  property-feature, property-type, property-city, property-status.
- Objecten: https://www.avcostamar.com/wp-sitemap-posts-property-1.xml
  (24-09-2026): **44 URL's**, alle onder `/propiedad/<slug>/`.
  Daarvan lijken 2 geen koopobject: `pidenos-presupuesto-sin-compromiso`
  (offertepagina) en `apartamento-el-alquiler-vacacional` (vakantieverhuur).
  Netto circa **42 objecten**, waarvan een deel mogelijk verhuur (er bestaat
  een status `en-alquiler` naast `en-venta`).
- Nog niet opgehaald maar nuttig: `wp-sitemap-taxonomies-property-city-1.xml`
  (plaatsen) en `wp-sitemap-taxonomies-property-status-1.xml` (koop/huur).

## 4. Aanbodpagina en voorbeeldobject

- Aanbod te koop: https://www.avcostamar.com/estado-propiedad/en-venta/
  (menulink; niet opgehaald). Per plaats:
  https://www.avcostamar.com/ciudad-propiedad/javea/ (idem benitachell, moraira).
- Voorbeeldobject: https://www.avcostamar.com/propiedad/villa-en-primera-linea-de-mar-en-javea/
  (24-09-2026, HTTP 200, 123 kB).

Wat er in de HTML staat:

| Veld | Waarde | Waar in de HTML |
|---|---|---|
| Prijs | 1.700.000 € | `<span class="price-and-type">` |
| Type | Villa de Lujo | zelfde span, `<small>` |
| Referentie | 1870 | `<div class="property-meta">` → `<span title="Ref. ">` |
| Woonoppervlak | 250 m² | `<span class="property-meta-size" title="Tamaño del Área">` |
| Perceel | **niet vermeld** | geen perceelveld op de pagina |
| Slaap-/badkamers | 5 / 5 | property-meta |
| Plaats | Jávea | titel/URL; coördinaten in pagina: lat 38.7390, lng 0.2316 |
| Omschrijving | wel, Spaans | "Villa totalmente reformada encima del acantilado…" |

- **JSON-LD (schema.org): nee** — 0 blokken `application/ld+json`.
- **Open Graph: ja** — `og:title`, `og:description` (eerste 160 tekens van de
  omschrijving), `og:type=article`, `og:url`, `og:site_name=AV Costamar`,
  `og:image`. **Geen prijs in de og-tags.**
- Kenmerken (piscina, vistas al mar, reformado, …) staan als
  `property-feature-…`-klassen op de pagina — makkelijk te lezen.

## 5. Systeem: WordPress + RealHomes-thema (eigen WP-site, geen makelaars-CMS)

Bewijs uit de objectpagina (24-09-2026):
- `<meta name="generator" content="WordPress 6.9">`
- 30× `wp-content/themes/realhomes` (RealHomes van Inspiry Themes, vastgoedthema)
- `<meta name="generator" content="WPML ver:4.8.6">` — meertalig: es, en, de, fr, ru, zh
- Plugins: revslider (Slider Revolution 5.4.8.1), cookie-law-info (CookieYes),
  contact-form-7, mortgage-calculator, sitepress-multilingual-cms (WPML)
- Server: `Apache/2`; body-class `wp-theme-realhomes single-property`
- HTTP-`Link`-header: `https://www.avcostamar.com/wp-json/wp/v2/propiedades/15441`
  → de **WordPress REST API staat open** voor het posttype `propiedades`.
  Dat is een nette gestructureerde ingang (JSON) in plaats van HTML ontleden;
  niet getest.
- Geen sporen van Inmoweb, Mediaelx/LetsINMO, Sooprema, Inmovilla of Witei.
  Er is dus geen bekende exportfeed; lezen gaat via de site zelf (HTML of REST).

## 6. Omvang en dekking Jávea/Benitachell/Moraira

- Omvang: circa 42 objecten (zie 3). Klein kantoor, gevestigd in Jávea.
- Plaatsen in het menu (property-city): Altea, Benidorm, Benissa, Benitachell,
  Calpe, Dénia, Jávea, Montgó, Moraira, Pedreguer, Teulada.
- Van de 44 URL's noemen er 14 een plaats: Jávea (incl. puerto, Arenal,
  Montgó, bahía de Jávea) 8, Benitachell 2, Moraira 1, Benissa 1, Dénia 1,
  Mascarat (Altea/Calpe) 1. Dus **minstens 11 van 44 zeker in het doelgebied**;
  van de overige 30 is de plaats uit de URL niet af te leiden. Gezien de
  vestiging in Jávea ligt vermoedelijk de meerderheid in het doelgebied —
  [te verifiëren] via `/ciudad-propiedad/javea/` of de city-sitemap.

## Volgende ronde (voorstel)

1. `/condiciones-generales` lezen (1 pagina) — pas daarna doorgaan.
2. `wp-sitemap-taxonomies-property-city-1.xml` + `/ciudad-propiedad/javea/`,
   `/benitachell/`, `/moraira/` voor de exacte dekking.
3. Volledige leesronde: 44 pagina's à 2 s = ruim 1,5 minuut; of via de REST API
   (`/wp-json/wp/v2/propiedades?per_page=100`) als die de prijsvelden meegeeft.
   Prijs/ref/m² uit de vaste RealHomes-klassen; perceel ontbreekt, dus
   perceelgrootte alleen uit de omschrijvingstekst.

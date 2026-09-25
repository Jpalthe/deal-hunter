# Inmo Villas Jávea — toets op automatisch lezen

- **Website:** https://www.inmovillasjavea.com
- **Datum toets:** 24-09-2026 (alle pagina's opgehaald tussen 21:10 en 21:12 UTC; vijf pagina's, minimaal twee seconden tussenruimte)
- **Advies: LEZEN.** robots.txt staat het toe, er zijn geen voorwaarden gevonden die het verbieden, en elke objectpagina heeft nette schema.org-data.

## 1. robots.txt — mag een gewone robot de aanbodpagina's lezen? Ja

Bron: https://www.inmovillasjavea.com/robots.txt (24-09-2026, HTTP 200). Volledige inhoud:

```
User-Agent: *
Disallow: /wp-admin/
Allow: /wp-admin/admin-ajax.php

Sitemap: https://www.inmovillasjavea.com/sitemap_index.xml

# Block dynamically generated image URLs from being indexed
Disallow: /wp-content/plugins/inmobaliaplugin/image.php
Disallow: /*/wp-content/plugins/inmobaliaplugin/image.php
```

Alleen de WordPress-beheeromgeving en één dynamisch afbeeldingsscript zijn afgeschermd. De aanbodpagina's (`/propiedades`, `/propiedad/...`) vallen nergens onder een Disallow. Het bestand is aangemaakt door de Rank Math SEO-plugin (staat in het commentaar bovenaan).

**Afspraak voor ons:** `image.php` niet aanroepen; foto's zo nodig via de `og:image` (`/wp-content/uploads/og-images/...`), niet via het geblokkeerde script.

## 2. Gebruiksvoorwaarden — geen verbod gevonden

- Op de objectpagina staat in kop- en voettekst geen link naar een "aviso legal", "condiciones" of "terms". De enige juridische link is **Política de privacidad / Privacy Policy & Cookies**: https://www.inmovillasjavea.com/privacy (stuurt door naar https://www.inmovillasjavea.com/en/privacy, 24-09-2026).
- Die pagina is de standaard-privacytekst van WordPress (over reacties, Gravatar, ingesloten media, cookies). Gezocht op: scrap, robot, crawl, bot, extract, reproduc, prohib, copyright / propiedad intelectual, aviso legal / condiciones / terms — **nul relevante treffers**. Er staat dus niets over automatisch lezen, hergebruik of intellectueel eigendom.
- Niet gecontroleerd (limiet van vijf pagina's): `page-sitemap1.xml` en `page-sitemap2.xml` zouden nog een losse aviso-legal-pagina kunnen bevatten die niet in het menu staat. Kans klein; bij twijfel één extra pagina ophalen in de volgende ronde.

Conclusie: **niet gevonden** — er is geen voorwaardenpagina die scraping verbiedt.

## 3. Sitemap — 330 koopobjecten, 42 huurobjecten

- Index: https://www.inmovillasjavea.com/sitemap_index.xml (24-09-2026) met acht deelbestanden; de relevante is **https://www.inmovillasjavea.com/property-sitemap.xml** (lastmod 24-09-2026 15:57 UTC — wordt dus dagelijks bijgewerkt).
- Inhoud: **1.668 URL's** = 417 Spaanse object-URL's × 4 talen (es zonder prefix, `/en/property/`, `/fr/propriete/`, `/nl/eigendom/`).
- Van de 417 Spaanse URL's: **330 × `venta-` (koop)**, 42 × `alquiler-`, 41 × `vacacional-`, 4 × `largatemporada-` (huur; dezelfde 42 huurobjecten staan onder twee slugs). Unieke referenties in totaal: 372.
- Oudste lastmod 17-09-2024, nieuwste 24-09-2026.

Elke URL eindigt op een nummer (bijv. `-737972`): dat is het interne Inmobalia-ID. De eigen kantoorreferentie (bijv. `JV1153`) staat alleen op de pagina zelf.

## 4. Aanbodpagina en één objectpagina

- **Aanbod te koop:** https://www.inmovillasjavea.com/propiedades ("Propiedades en Venta"). Daarnaast SEO-landingspagina's per plaats en type, bijv. https://www.inmovillasjavea.com/propiedades/venta/javea/ en https://www.inmovillasjavea.com/propiedades/venta/javea/parcelas-y-terrenos/ . Opvallend voor Deal Hunter: er zijn filters **`.../oportunidad/`** (bijv. `/propiedades/venta/javea/apartamentos-y-pisos/oportunidad/`) en een aparte pagina **https://inmovillasjavea.com/ventas-discretas** ("Ventas discretas" — stille verkoop, mogelijk aanbod dat niet op portals staat). Beide nog niet geopend.
- **Geopende objectpagina (24-09-2026):** https://www.inmovillasjavea.com/propiedad/venta-javea-villa-737972 (canonieke URL volgens og:url: `/propiedad/venta-xabia-villa-737972` — de sitemap gebruikt "javea", de pagina zelf "xabia"; beide werken).

**JSON-LD (`<script type="application/ld+json">`): ja, één blok.** `@type`: RealEstateListing, SingleFamilyResidence, Offer, House. Inhoud:

| Veld | Waarde |
|---|---|
| name | Villa reformada en Puerta Fenicia con vistas al Montgó |
| priceSpecification.price / currency | 850000 / EUR |
| floorSize | 218 M2 (bebouwd) |
| address | addressLocality Jávea, addressRegion Alicante, ES |
| numberOfBedrooms / Bathrooms | 4 / 2 |
| yearBuilt | 1999 |
| datePosted | 2026-09-21 |
| businessFunction | sell |
| description | volledige verkooptekst (o.a. "reformada en 2024", "parcela ... de 1.006 m²") |

**Niet in JSON-LD, wel in de zichtbare tekst:** perceel ("Parcela m² 1.006"), bebouwd ("Construido m² 218"), kantoorreferentie ("Referencia JV1153"), prijs ("850.000 €"), plaats ("Jávea"). Er is ook een PDF-brochure via `https://service.inmobalia.com/pdf/?id=737972&ag=819&...`.

**Open Graph: ja.** `og:title`, `og:description` (verkooptekst), `og:type` = website, `og:url`, `og:image` (`/wp-content/uploads/og-images/737972-og-thumb.jpg`). Geen prijs in de og-tags. `hreflang`-links naar en/es/fr/nl-versies aanwezig.

## 5. Systeem achter de site: WordPress met Inmobalia-plugin

Aanwijzingen (alle uit de HTML van de objectpagina, 24-09-2026):
- `<meta name="generator" content="WordPress 7.0.1">`, WPML 4.6.13 (vier talen), Site Kit by Google; `link: .../wp-json/` in de HTTP-headers.
- Aanbod komt uit **Inmobalia** (CRM uit Marbella): 93 verwijzingen naar `/wp-content/plugins/inmobaliaplugin/`, plugin `inmobalia-landing-pages`, foto's van `media.inmobalia.com`, PDF via `service.inmobalia.com` met `ag=819` (kantoornummer bij Inmobalia).
- Verder: eigen thema `inmovillasjavea`, Rank Math SEO (robots + sitemap), Breeze-cache (HTML-commentaar "Cache served by breeze CACHE"), Complianz GDPR (`cmplz_*`-cookies), Cloudflare als CDN (`server: cloudflare`, cookie `__cf_bm`).

Dus **niet** Inmoweb, Mediaelx, Sooprema, Inmovilla of Witei. Inmobalia levert doorgaans XML-exportfeeds aan partners [te verifiëren], maar dat is hier niet nodig: lezen mag.

## 6. Omvang en Jávea-dekking (schatting uit de URL-slugs in de sitemap)

**330 koopobjecten**, per type: 219 villa's, 43 percelen, 40 appartementen, 11 rijwoningen (adosado), 4 duplex, 3 finca's, 3 benedenwoningen, 3 penthouses, 2 huizen, 1 bedrijfspand, 1 gebouw.

| Gebied | Aantal | Aandeel |
|---|---|---|
| Jávea (incl. wijken: Tosalet, Montgó, Montañar, Adsubia, Puerto, Balcón al Mar, Valle del Sol, Rafalet, Pinosol, Tarraula, Nova Xàbia, Portichol, Granadella, Ambolo, Castellans, La Corona, La Lluca, Cap Martí, Cala Blanca, Arenal, casco antiguo e.a.) | 246 | 75 % |
| Benitachell / Cumbre del Sol | 24 | 7 % |
| Moraira (incl. Benimeit-Tabaira) | 18 | 5 % |
| **Samen Jávea + Benitachell + Moraira** | **288** | **87 %** |
| Overig: Dénia 14 (+ Jesús Pobre 2, Pamis 1), Benissa 9, Calpe 7, Altea 7, Pedreguer 1, Benidorm 1 | 42 | 13 % |

Kanttekening: de toewijzing van wijknamen aan Jávea is mijn interpretatie van de slug; "montgo" (11) kan deels Dénia zijn. De ruwe telling staat in de sitemap zelf.

## Praktisch leesplan (als Jan akkoord is)

1. Dagelijks `property-sitemap.xml` lezen; alleen nieuwe of gewijzigde `lastmod` verwerken.
2. Alleen de Spaanse `/propiedad/venta-...`-pagina's ophalen (330 stuks, één per twee seconden ≈ 11 minuten), of de `/nl/eigendom/te-koop-...`-variant voor Nederlandse teksten.
3. Per pagina JSON-LD uitlezen (prijs, m² bebouwd, plaats, slaapkamers, bouwjaar, datum) en uit de zichtbare tekst "Parcela m²" en "Referencia" halen.
4. `image.php` nooit aanroepen; kenbare user-agent met contactadres gebruiken.
5. Extra ronde: de pagina "Ventas discretas" en de `oportunidad`-filters bekijken — daar zit mogelijk het aanbod dat niet op portals staat.

## Bedrijfsgegevens (alleen kantoor, geen personen)

- Kantoor: Avenida Augusta nº 22, Bajo 7, Jávea (Alicante) — volgens de voettekst van de objectpagina.
- Telefoon: +34 966 46 00 33 en +34 607 42 99 26; e-mail: info@inmovillasjavea.com.
- Registratienummer makelaar Comunidad Valenciana in de voettekst: EGVT-00230-A [te verifiëren in het register].

## Opgehaalde pagina's (logboek)

| # | URL | Tijd (UTC) | Resultaat |
|---|---|---|---|
| 1 | https://www.inmovillasjavea.com/robots.txt | 21:10:23 | 200 |
| 2 | https://www.inmovillasjavea.com/sitemap_index.xml | 21:10:48 | 200 |
| 3 | https://www.inmovillasjavea.com/property-sitemap.xml | 21:11:00 | 200 |
| 4 | https://www.inmovillasjavea.com/propiedad/venta-javea-villa-737972 | 21:11:19 | 200 |
| 5 | https://www.inmovillasjavea.com/privacy → /en/privacy | 21:12:38 | 301 → 200 |

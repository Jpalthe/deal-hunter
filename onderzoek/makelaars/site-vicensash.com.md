# Vicens Ash Properties — www.vicensash.com

Toets op automatisch lezen · TREE Deal Hunter · datum: 24-09-2026

**Advies: overslaan** — niet omdat het verboden is (robots.txt staat lezen toe en
er is geen verbod gevonden), maar omdat er op dit domein **niets eigens te lezen
valt**. www.vicensash.com is nog slechts een lege schil op het platform Mobilia
Gestión die live de startpagina van **valuvillas.com** toont; elk ander pad geeft
een 404. Het aanbod staat dus op valuvillas.com (WordPress) en dat kantoor is al
apart getoetst in `site-valuvillas.com.md`. Vicens Ash hier meenemen zou
dubbel lezen en dubbel tellen betekenen.

## Kantoor

- Bedrijf: Vicens Ash Properties (naam en website uit `K01-kantoren-javea.json`).
- Kantooradres en contactkanalen: **niet vast te stellen vanaf de site** — de
  pagina die vicensash.com toont is die van Valu Villas (voettekst "Copyright ©
  2026 Valuvillas"); het woord "Vicens" komt in de hele HTML niet voor.
- Bron: https://www.vicensash.com/ (HTTP 200, 24-09-2026).

## 1. robots.txt — toegestaan

Bron: https://www.vicensash.com/robots.txt (HTTP 200, 24-09-2026). Volledige inhoud:

```
# robots.txt
User-agent: *
Disallow: /app_code/
Disallow: /aspnet_client/
Disallow: /bin/
Disallow: /configuration/
Disallow: /DesktopModules/
Disallow: /Portals/
```

Uitleg: alleen zes systeemmappen van het ASP.NET/DNN-platform zijn uitgesloten.
Aanbodpagina's zouden voor `User-agent: *` gewoon leesbaar zijn — alleen bestaan
ze op dit domein niet (zie 4). Geen `Sitemap:`-regel.

Ter vergelijking, de site waar het aanbod echt staat:
https://valuvillas.com/robots.txt (HTTP 200, 24-09-2026) sluit alleen
`/wp-admin/`, `/wp-includes/`, `/tag/`, `/author/`, `/refer/` en `/date/` uit;
`/properties/` en `/wp-json/` zijn toegestaan. De vijf `Sitemap:`-regels wijzen
naar het domein `www.javea.properties` (o.a. `properties-sitemap.xml`).

## 2. Voorwaarden — niet gevonden

- Op vicensash.com is geen juridische pagina bereikbaar: elk pad behalve `/`
  geeft `302 → /app_support/ErrorCode.aspx?id=404 → /app_support/error_pages/404.html`
  ("Error 404 - Página no encontrada", 24-09-2026).
- De getoonde startpagina (Valu Villas) heeft in de voettekst geen link naar
  privacy, aviso legal of terms; alleen "Copyright © 2026 Valuvillas Sitemap".
- Volledige paginalijst van valuvillas.com via de WordPress-API
  (https://valuvillas.com/wp-json/wp/v2/pages?per_page=100, 40 pagina's, HTTP
  200, 24-09-2026): **geen** privacybeleid, aviso legal of gebruiksvoorwaarden.
  De enige treffers zijn het woord "privacy" in een beschrijving van percelen op
  de Montgó en "Terms and Conditions Accepted" bij een klantbeoordeling.

Conclusie: geen verbod op automatisch lezen gevonden; er zijn simpelweg geen
voorwaarden gepubliceerd.

## 3. Sitemap — niet op vicensash.com; wel op valuvillas.com

- https://www.vicensash.com/sitemap.xml → 302 naar de Mobilia-404-pagina (24-09-2026).
- https://valuvillas.com/properties-sitemap.xml (HTTP 200, text/xml, 24-09-2026):
  **177 `<loc>`-regels** = 176 objectpagina's onder `/properties/…/` plus het
  archief `/properties/` zelf. `lastmod` loopt van 2024-09-18 tot 2026-09-24
  (151 URL's in 2026 bijgewerkt).
- Controle via de API: `X-WP-Total: 177` op
  https://valuvillas.com/wp-json/wp/v2/properties?per_page=1 (24-09-2026).

## 4. Aanbodpagina en objectpagina

**Op vicensash.com:** geen eigen aanbodpagina. De getoonde startpagina linkt
naar https://www.valuvillas.com/properties/ en naar de typepagina's
`/property-types/villas-for-sale-in-javea/`, `…/apartments-…`, `…/plots-…`,
`…/townhouses-…`, `…/commercial-…`. De objectlink
https://www.vicensash.com/properties/lovely-5-bedroom-villa-in-javea/ geeft de
Mobilia-404 (24-09-2026).

**Objectpagina op valuvillas.com:**
https://www.valuvillas.com/properties/lovely-5-bedroom-villa-in-javea/ (HTTP 200,
24-09-2026, titel "5 Bedroom Villa in Javea - Valuvillas").

- `<script type="application/ld+json">`: 3 blokken, maar alleen site-schema:
  Yoast (WebSite, WebPage, BreadcrumbList, ImageObject, SearchAction), Schema Pro
  (SiteNavigationElement) en een BreadcrumbList. **Geen** RealEstateListing,
  Product of Offer; geen prijs, oppervlakte of referentie in JSON-LD.
- og-tags: `og:type` = article, `og:title` = "5 Bedroom Villa in Javea",
  `og:url`, `og:site_name` = "Valuvillas", `og:image` =
  cdn.valuvillas.com/…/sooprema-propiedades_536765dfb067b-source.jpg
  (`og:image:width/height` staan foutief op 1), `twitter:card`. Geen prijs of
  oppervlakte in og.
- Zichtbaar in de HTML (label/waarde, goed leesbaar): prijs **€1,315,000**;
  "Ref No." **VV627**; 5 slaapkamers, 4 badkamers; "Plot Size 1266 M2";
  "Build Size 253 M2"; "Has Pool Yes"; plaats **Javea** (uit de titel; een
  apart plaatsveld is er niet, wel een zoekfilter "Location" met Benissa,
  Benitachell, Calpe, Denia, Els Poblets …).

## 5. Systeem achter de site

**vicensash.com — Mobilia Gestión (ASP.NET-portaalplatform), lege schil.**
Bewijs (24-09-2026): cookies `Esperantus_Language_vicensash.mobiliagestion.es`,
`ZwPortalAlias=www.vicensash.com`, `ZenWorksSecurity`, `ASP.NET_SessionId`,
`__AntiXsrfToken`; foutafhandeling via `/app_support/ErrorCode.aspx`; robots.txt
met DNN-mappen (`/DesktopModules/`, `/Portals/`). De startpagina die het platform
teruggeeft is een live kopie van valuvillas.com: canonical
`https://valuvillas.com/`, `og:url` valuvillas.com, WP Rocket-stempel
`cached@1790285059` (= 24-09-2026 ±21:24 UTC, dezelfde minuut als de cookie).

**valuvillas.com — WordPress + Elementor + JetEngine, gevoed vanuit Sooprema.**
Bewijs: `<meta name="generator" content="Elementor 4.3.1 …">` en
`"WP Rocket 3.21.3"`; commentaar Yoast SEO Premium v19.2 en Schema Pro; thema
`hello-elementor-child`; plugins `jet-engine`, `jet-smart-filters`,
`elementor-pro`, `dynamic-content-for-elementor`; eigen posttype `properties`
(`<link rel="alternate" … href="…/wp-json/wp/v2/properties/926759">`). Alle
objectfoto's heten `sooprema-propiedades_<id>-source.jpg` (723 vermeldingen op
de objectpagina) — de gegevens komen dus **waarschijnlijk** uit het CRM Sooprema
en worden in WordPress geïmporteerd [te verifiëren; afgeleid uit bestandsnamen].

## 6. Omvang en dekking (= aanbod Valu Villas, niet dubbel tellen)

Bron: slugs in https://valuvillas.com/properties-sitemap.xml (24-09-2026),
176 objecten. Telling op plaatsnaam in de URL, dus een schatting:

| Plaats (uit slug) | Aantal |
|---|---|
| Jávea (incl. Montgó, Tosalet, Cala Blanca, typefout "jvea") | ≈126 |
| Moraira / Teulada | 14 |
| Benitachell / Cumbre del Sol | 7 |
| Overig Marina Alta (Dénia, La Xara, Pedreguer, Calpe, Benissa …) | 28 |
| Buiten de regio (l'Alfàs del Pi) | 1 |

Dus ≈147 van 176 (≈83%) in Jávea, Benitachell of Moraira. Typen (uit slug):
villa 106, appartement 35, perceel 19 (+2 "land"), townhouse 6, en enkele
penthouse/finca/duplex/leasehold/business/nieuwbouwproject.

## Wat dit betekent voor Jan

- vicensash.com **niet** als bron opnemen; het levert alleen een kopie van de
  Valu Villas-startpagina en geeft op elk ander pad een 404.
- Het aanbod lezen via valuvillas.com — dat staat al in `site-valuvillas.com.md`.
- Wil Jan ooit rechtstreeks een feed: Sooprema kent een exportfeed; vragen bij
  Valu Villas, niet bij het (in de praktijk niet meer bestaande) vicensash.com.

## Opgehaalde pagina's (alle 24-09-2026, ≥2 s tussenpoos)

vicensash.com (4 van 5): `/robots.txt`, `/sitemap.xml` (→404), `/`,
`/properties/lovely-5-bedroom-villa-in-javea/` (→404).
valuvillas.com (5 van 5): `/robots.txt`, `/properties/lovely-5-bedroom-villa-in-javea/`,
`/properties-sitemap.xml`, `/wp-json/wp/v2/pages?per_page=100&_fields=…`,
`/wp-json/wp/v2/properties?per_page=1&_fields=id`.
Webzoekopdrachten: geen (zoekbudget van de sessie was op).

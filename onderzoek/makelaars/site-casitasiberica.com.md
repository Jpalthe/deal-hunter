# Casitas Ibérica — toets op automatisch lezen

**Website:** https://www.casitasiberica.com
**Datum toets:** 24-09-2026
**Kantoor (footer van de site):** Ctra. Jesús Pobre 164, 03730 Jávea (Alicante) · (+34) 965 794 408 · (+34) 686 453 801 · info@casitasiberica.com · ma–vr 9.30–17.30, za op afspraak
**Opgehaald:** 5 pagina's (het maximum), minimaal 2 seconden tussen elke aanvraag, geen formulieren, geen inlog.

## Advies: LEZEN

robots.txt staat het toe, er zijn geen gebruiksvoorwaarden gevonden die het verbieden, en alle objectgegevens staan als gewone tekst in de HTML. Wel: geen sitemap en geen gestructureerde data, dus de lezer moet de aanbodpagina's en objectpagina's zelf uitlezen (≈ 100 aanvragen voor een volledige ronde).

## 1. robots.txt — toegestaan

Bron: https://www.casitasiberica.com/robots.txt (24-09-2026, HTTP 200). Volledige inhoud:

```
User-agent: *
Disallow: /wp-admin/
Allow: /wp-admin/admin-ajax.php
```

Alleen de beheeromgeving `/wp-admin/` is verboden. De aanbodpagina `/property-list/`, de objectpagina's `/properties/…/` en de locatiepagina's `/locations/…/` vallen daar niet onder en mogen dus gelezen worden. Er staat geen `Sitemap:`-regel in.

## 2. Gebruiksvoorwaarden — niet gevonden

- In het menu en de footer van alle vier opgehaalde HTML-pagina's staat geen link naar aviso legal, terms, privacy of cookies.
- In de HTML van die pagina's: 0 treffers op "privacy", "legal", "terms", "cookie", "disclaimer", "aviso", "condicion".
- Een webzoekopdracht was in deze sessie niet meer mogelijk (zoekbudget op). Een gok als `/privacy-policy/` paste niet binnen de vijf pagina's.

Conclusie: er is op de site geen tekst gevonden die automatisch lezen verbiedt. **[te verifiëren]** in een volgende ronde: `/privacy-policy/` proberen.

## 3. Sitemap — geen

- `https://www.casitasiberica.com/sitemap.xml` → HTTP 404 (24-09-2026).
- Geen `Sitemap:`-regel in robots.txt.
- De site draait WordPress **5.1.19** (versiestring in de script-URL's). Die versie heeft nog geen ingebouwde sitemap (die kwam pas in 5.5) en er is geen SEO-plugin (Yoast, RankMath) zichtbaar in de HTML.
- Niet geprobeerd (paginabudget): `/sitemap_index.xml`, `/wp-sitemap.xml`.

Aantal object-URL's via sitemap: onbekend. In plaats daarvan telt de aanbodpagina zelf (zie 4).

## 4. Aanbodpagina en objectpagina

**Aanbod:** https://www.casitasiberica.com/property-list/ (24-09-2026, HTTP 200, titel "Listings"). Toont "**91 Properties Found**", verdeeld over 10 pagina's (`/property-list/page/2/` … `/page/10/`, ± 10 per pagina). Elke kaart bevat: titel, plaats, referentie, slaap-/badkamers, bouwoppervlak, perceel, prijs en een statusbadge (op p.1: 1× Sold, 2× Reserved, 2× Exclusive, 1× 360 Tour). Object-URL's hebben de vorm `/properties/<slug>/`.

**Objectpagina:** https://www.casitasiberica.com/properties/avs-57684v/ (24-09-2026, HTTP 200)

| Veld | Waarde op de pagina |
|---|---|
| Titel | Plot in Javea |
| Referentie | AVS 57684V |
| Prijs | 320,000 EUR |
| Plaats | Location: Javea |
| Type | Plot |
| Perceel | Plot: 1000 m² |
| Bouw | niet vermeld (perceel) |
| Energielabel | X |
| Kenmerken | Flat plot, South Facing |
| Beschrijving | vlak bouwperceel in Villes del Vent, vrij van bouwverplichting (samengevat) |

- `<script type="application/ld+json">`: **nee** (0 gevonden).
- `og:`-meta-tags: **nee** (geen enkele og:, twitter: of description-meta; alleen een favicon-tag).
- Alles staat als gewone, server-side gerenderde HTML op de pagina; de body-class is `single-listings postid-41251` (WordPress custom post type "listings"). Er is een PDF-knop (`?pdf=41251`, plugin DK PDF).

## 5. Systeem achter de site

**WordPress 5.1.19 met een eigen (maatwerk)thema**, geen vastgoed-CMS.

Aanwijzingen (alle uit de HTML van 24-09-2026):
- Header `Link: https://www.casitasiberica.com/wp-json/` en paden `/wp-content/`, `/wp-includes/` → WordPress.
- Versiestring `?ver=5.1.19` op de core-scripts → sterk verouderde WordPress.
- Thema `/wp-content/themes/CasitasIberica/` op Foundation 6.4.1; footer: "Website By Twenty-Two Creations" (webbureau).
- Plugins: GTranslate (machinevertaling; de /es/, /nl/, /fr/, /de/ versies zijn geen aparte inhoud), Contact Form 7, Favorites, DK PDF, reCAPTCHA v3.
- Geen signaturen van Inmoweb, Mediaelx/LetsINMO, Sooprema, Inmovilla of Witei. Geen "powered by" van een vastgoedsysteem.
- Het zoekfilter is een POST-formulier (velden: locations, types, beds, baths, minprice, maxprice, buildsize, plotsize, reference, sort) — niet gebruikt, en filteren via de URL is dus niet beschikbaar. De locatiepagina's `/locations/<plaats>/` zijn wél gewone links met paginering.

Bijzonderheid: naast eigen referenties (2836*LC, 2845, 2865*LC, soms met badge "Exclusive") staan er veel referenties als `AVS 57684V` en `17977_PH026V`. Die lijken uit een gedeeld netwerk of collega-aanbod te komen **[te verifiëren]** — voor deal hunting relevant, want die objecten staan dan mogelijk ook bij andere kantoren.

## 6. Omvang en dekking Jávea / Benitachell / Moraira

- Totaal: **91 objecten** (aanbodpagina, 24-09-2026), inclusief enkele met status Sold/Reserved.
- **Jávea: 55 van 91 (≈ 60 %)** — bron https://www.casitasiberica.com/locations/javea/ ("55 Properties Found", 6 pagina's, 24-09-2026). Let op: de site telt Jesús Pobre mee onder Jávea (een woning in Jesús Pobre staat op de Jávea-pagina); formeel hoort Jesús Pobre bij Dénia **[te verifiëren]**.
- Benitachell/Cumbre del Sol en Moraira: niet apart geteld (buiten het paginabudget). Steekproef aanbodpagina p.1: 1 van 10 in Cumbre del Sol (Benitachell).
- Overige plaatsen in het filter: Dénia, Gata de Gorgos, Llíber, Altea, Teulada.

Schatting Jávea + Benitachell + Moraira samen: **60–75 %** van het aanbod **[te verifiëren]** (Jávea is hard, de rest is steekproef).

## Praktisch voor de lezer

1. Tempo: hooguit 1 aanvraag per 2 seconden; volledige ronde = 10 aanbodpagina's + ± 91 objectpagina's.
2. Geen sitemap → nieuw/verdwenen aanbod bijhouden door de slugs op de aanbodpagina te vergelijken; statusbadges (Sold, Reserved) direct meenemen.
3. Objectgegevens uit de HTML halen: `ref:`, prijs "… EUR", `Location:`, `Type:`, `Build:`, `Plot:`, `Energy Cert.:`, kenmerkenlijst, beschrijving.
4. Mogelijk eenvoudiger alternatief **[te verifiëren, niet opgehaald]**: de WordPress REST API op `/wp-json/wp/v2/listings` — robots.txt verbiedt `/wp-json/` niet, maar controleer eerst of die open staat en wat erin zit.
5. Open punt: voorwaarden alsnog zoeken (`/privacy-policy/`) vóór de eerste volledige ronde.

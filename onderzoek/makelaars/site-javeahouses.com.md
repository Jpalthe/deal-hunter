# Toets op automatisch lezen: javeahouses.com

**Kantoor:** Houses Investment Holding S.L. (handelsnaam Javea Houses / Inmobiliaria Javea Houses)
**Website:** https://www.javeahouses.com
**Datum toets:** 24-09-2026 (avond)
**Advies: LEZEN**

Vijf pagina's opgehaald, met minstens 2 seconden tussenpoos: robots.txt, sitemap-index,
property-sitemap, één objectpagina, de pagina "Avisos legales". Geen inlog, geen formulier.

## 1. robots.txt — toegestaan

Bron: https://www.javeahouses.com/robots.txt (HTTP 200, 24-09-2026). Volledige inhoud:

```
User-agent: *
Disallow: /wp-admin/
Allow: /wp-admin/admin-ajax.php

Sitemap: https://www.javeahouses.com/wp-sitemap.xml
```

Voor `User-agent: *` is alleen het beheergedeelte `/wp-admin/` afgeschermd. De aanbodpagina's
(`/property/...`, `/busqueda-propiedades/`, `/property-city/...`) vallen daar niet onder en mogen
dus gelezen worden.

## 2. Voorwaarden — geen verbod gevonden

Bron: https://www.javeahouses.com/avisos-legales/ (HTTP 200, 24-09-2026). Dit is de enige
juridische pagina waarnaar de site verwijst (footerlink "Avisos legales"; geen aparte
términos/condiciones-pagina in de links van de objectpagina).

De pagina bevat de LSSI-vermelding (art. 9 Ley 34/2002) en een privacyverklaring (AVG/RGPD):
eigenaar Houses Investment Holding SL, Avenida de la Libertad Local 7-F, 03730 Jávea;
algemeen e-mailadres info@javeahouses.com, telefoon +34 966 461 702. Verder: doorgifte aan
derden, externe links, Spaans recht, wijzigingen in de privacyverklaring.

Zoektermen in de tekst (3.503 tekens): scrap 0, robot 0, automat 0, bot 0, crawler 0,
extrac 0, reproduc 0, prohib 0, "propiedad intelectual" 0. Er staat **geen** verbod op
automatisch lezen, geen gebruiksvoorwaarden en geen auteursrechtclausule.

## 3. Sitemap — 80 object-URL's

- Index: https://www.javeahouses.com/wp-sitemap.xml (standaard WordPress-sitemap) met 14
  deelsitemaps, o.a. `wp-sitemap-posts-property-1.xml` en taxonomieën `property-type`,
  `property-city`, `property-status`.
- Objecten: https://www.javeahouses.com/wp-sitemap-posts-property-1.xml — **80 URL's**,
  allemaal van de vorm `/property/<slug>/`. Alle 80 zijn dus objectachtige URL's.
- `lastmod` loopt van 24-07-2026 tot 24-09-2026 06:02 — de sitemap is vanochtend nog bijgewerkt.

## 4. Aanbodpagina en objectpagina

- Aanbod/zoekpagina (uit de navigatie): https://www.javeahouses.com/busqueda-propiedades/
- Per plaats: https://www.javeahouses.com/property-city/javea/
- Bekeken objectpagina (HTTP 200, 190 kB):
  https://www.javeahouses.com/property/chalet-con-vistas-al-mar-y-piscina-privada-a-solo-1-km-de-la-playa-del-arenal-de-javea/

**JSON-LD** (1 blok, `@type: RealEstateListing`):
- `name`: CHALET CON VISTAS AL MAR Y PISCINA PRIVADA A SOLO 1 KM DE LA PLAYA DEL ARENAL DE JÁVEA
- `address.addressLocality`: "Jávea" (regio, postcode en land leeg); `geo` leeg
- `offers.price`: 1260000, `priceCurrency`: "€", `availability`: "https://schema.org/Venta"
  (geen geldige schema.org-waarde, maar wel bruikbaar als koop/huur-kenmerk)
- `additionalProperty`: Bedrooms 3, Bathrooms 3, Area Size 200 met `unitText` "190m²"
  (tegenstrijdig; de zichtbare pagina zegt 2 badkamers en "Área 200 190m²")
- **Ontbreekt in JSON-LD:** perceeloppervlak, referentie, coördinaten, beschrijving
  (`description` is alleen "Ocasión").

**og:/twitter:-tags:** geen. Ook geen meta description.

**Zichtbaar op de pagina:** "Venta 1.260.000€", "ID de la propiedad: W2455", in de tekst
"[IW] ref.: W2455", plaats Jávea (taxonomie property-city/javea), zone Adsubia,
3 slaapkamers, 2 badkamers, Área 200 / 190 m². Perceel alleen in woorden ("amplia parcela"),
niet als veld.

## 5. Systeem achter de site: WordPress + RealHomes (eigen site, geen makelaars-CMS)

Bewijs uit de objectpagina (24-09-2026):
- `<meta name="generator" content="WordPress 7.1.2">`, plus Elementor 4.1.4 en Slider Revolution 6.7.50
- Thema `wp-content/themes/realhomes` (versie 4.5.2, Inspiry Themes) — 23 verwijzingen,
  html-commentaar `<!-- /.rh_header -->` e.d., body class `wp-theme-realhomes`
- Vastgoedplugin `wp-content/plugins/easy-real-estate` (versie 2.4.2) + `realhomes-elementor-addon`
- Header: `link: <https://www.javeahouses.com/wp-json/wp/v2/properties/6591>; rel="alternate"` —
  de WordPress REST API staat aan en kent het objecttype `properties`
- Server nginx, PHP 8.4.17, `x-microcache: True`; GTranslate voor vertalingen
- Geen scripts, iframes of paden van Inmoweb, Sooprema, Mediaelx/LetsINMO, Inmovilla of Witei.
  De tekst "[IW] ref.: W2455" in de beschrijving wijst mogelijk op een import uit een extern
  CRM (IW = Inmoweb?) — **[te verifiëren]**, geen bewijs op de pagina zelf.

## 6. Omvang en dekking Jávea / Benitachell / Moraira

Slug-analyse van de 80 sitemap-URL's (bron: property-sitemap, 24-09-2026):
- 33 slugs noemen "javea"; daarbovenop Jávea-wijken zonder de plaatsnaam: arenal 9, montgo 3,
  tosalet 2, costa nova, cap martí, barranc de l'encantada, casco antiguo, puerto.
- 1 Benitachell, 1 Dénia (bedrijfsruimte), 1 Castell de Castells (rustiek), 0 Moraira/Teulada.
- 25 slugs zijn alleen een nummer (`6610-2`, `6631-2` …) — plaats pas zichtbaar na het openen
  van de pagina.
- 7 slugs zijn verhuur (alquiler), ongeveer 10 zijn bedrijfsruimte/traspaso/bar.

**Schatting:** ~80 objecten online, waarvan ~60–65 koopobjecten (woningen, percelen, fincas)
en naar schatting **90% of meer in Jávea**; Benitachell 1, Moraira 0. Het kantoor is een echte
Jávea-makelaar met een klein aanbod, incl. percelen, solares en "oportunidad"-objecten — precies
het soort aanbod dat Deal Hunter zoekt.

## Advies en werkwijze

**Lezen.** robots.txt laat alles toe, de aviso legal verbiedt niets, en elke objectpagina heeft
JSON-LD met prijs, plaats en koop/huur. Het aanbod is klein: 80 pagina's met 2 seconden pauze is
een doorloop van ~3 minuten per dag.

Aandachtspunten voor de lezer:
1. Bron voor de lijst: de property-sitemap (`lastmod` geeft aan wat er veranderd is).
2. Prijs en plaats uit JSON-LD; referentie uit "ID de la propiedad"; perceel en bouwjaar uit de
   beschrijvingstekst (niet als veld aanwezig); badkamers liever van de zichtbare pagina.
3. De nummer-slugs (25 stuks) altijd openen om de plaats te bepalen.
4. Alternatief zonder HTML te ontleden: de open REST API
   `https://www.javeahouses.com/wp-json/wp/v2/properties` — niet getest (paginabudget),
   robots.txt verbiedt het niet. Eerst één keer voorzichtig proberen.
5. Verhuur (`alquiler`) en bedrijfsruimte (`local`, `traspaso`) uitsluiten.
6. Geen persoonsgegevens overnemen: de site toont een agentprofiel (`/agente/houses-investment/`);
   alleen de bedrijfsnaam gebruiken.

# Andrea y Olaf Inmobiliaria — toets op automatisch lezen

- **Site:** https://www.andreayolaf.com (Spaans; taalversies op en./fr./de./nl.andreayolaf.com)
- **Datum toets:** 24-09-2026, ca. 21:50 UTC
- **Opgehaald (5 pagina's, 2 s tussenpauze):** robots.txt, sitemap.xml, /aviso-legal, één objectpagina, /propiedades-en-venta
- **Kantoor (uit JSON-LD op de objectpagina):** Calle Sertorio 5, 03730 Jávea · info@andreayolaf.immo · +34 722 347 648 (JSON-LD) / +34 606 935 434 (sitekop)

## Advies: **lezen**

robots.txt staat alles toe, de gebruiksvoorwaarden verbieden automatisch lezen niet, en elke objectpagina bevat volledige schema.org-data (prijs, woonoppervlak, slaapkamers, badkamers, referentie, coördinaten, publicatiedatum). Het is een van de best leesbare makelaarssites voor ons doel.

**Kanttekening voor Jan:** de Aviso Legal verbiedt wel *reproductie, distributie en commercieel gebruik* van de inhoud zonder toestemming. Intern lezen en analyseren om deals te vinden is iets anders dan de teksten/foto's overnemen. Foto's en beschrijvingen dus niet hergebruiken of doorpubliceren — alleen de kerncijfers (prijs, m², plaats, referentie) in onze eigen database.

## 1. robots.txt — toegestaan

Bron: https://www.andreayolaf.com/robots.txt (HTTP 200, 24-09-2026). Volledige inhoud:

```
User-agent: *
Disallow:
```

Een lege `Disallow:` betekent: niets uitgesloten, alles mag gelezen worden. Er staat geen `Sitemap:`-regel in en geen `Crawl-delay`.

## 2. Gebruiksvoorwaarden — geen scrapingverbod

Bron: https://www.andreayolaf.com/aviso-legal (HTTP 200, 24-09-2026). Gezocht op scrap, robot, crawl, automat, bot, rastre, extrac, minería, base de datos, spider — geen enkele treffer over automatisch lezen. Wel relevante bepalingen (citaten):

- Onder "Compromisos y Obligaciones de los Usuarios": *"Respecto de los contenidos de esta web, se prohíbe: Su reproducción, distribución o modificación, total o parcial, a menos que se cuente con la autorización de sus legítimos titulares [...] Su utilización para fines comerciales o publicitarios"*
- Ook: de gebruiker verplicht zich *"a no llevar a cabo ninguna conducta que pudiera [...] dañar, inutilizar o sobrecargar el portal"* — dus rustig lezen (1 pagina per 2 s) is verstandig.
- Onder "Derechos de Propiedad Intelectual e Industrial": *"quedan expresamente prohibidas la reproducción, la distribución y la comunicación pública [...] de la totalidad o parte de los contenidos de esta página web, con fines comerciales [...] sin la autorización de www.andreayolaf.immo."*

Let op: de voorwaarden noemen het domein **andreayolaf.immo**, de site draait op andreayolaf.com. Eigen privacy- en cookiebeleid staan apart (/politica-de-privacidad, /politica-de-cookies) — niet opgehaald.

## 3. Sitemap — 440 objectpagina's

Bron: https://www.andreayolaf.com/sitemap.xml (HTTP 200, 590 kB, 565 URL's, 24-09-2026). Geen sitemap-index; één bestand met hreflang-alternatieven per URL (es/en/fr/de/nl).

Opbouw onder `/propiedades-en-venta/`:

| Soort | Aantal | Herkenning |
|---|---|---|
| Plaatsoverzicht (`/javea`, `/moraira`, …) | 25 | prioriteit 0.8 |
| Zone-overzicht (`/javea/arenal`, …) | 77 | prioriteit 0.7 |
| **Objectpagina** (`/javea/cap-marti/villa-…`) | **440** | prioriteit 0.6, changefreq weekly |

Van de 440 objectslugs bevatten er 555 URL's in totaal een objectwoord (venta/villa/apartamento/parcela …), maar dat telt ook overzichts- en landingspagina's mee. De zuivere objecttelling is 440.

Typen op basis van de slug: villa 294 · apartamento 39 · parcela 34 · terreno 14 · chalet 15 · casa 13 · finca 6 · ático 4 · local 4 · solar 2 · overig 15.

## 4. Objectpagina — JSON-LD én OpenGraph aanwezig

Bron: https://www.andreayolaf.com/propiedades-en-venta/javea/cap-marti/villa-tradicional-en-javea-cap-marti-con-piscina-privada (HTTP 200, 24-09-2026). Server-side gerenderde HTML, geen JavaScript nodig.

**`<script type="application/ld+json">`** — twee blokken, geldig JSON:
1. `RealEstateListing` met o.a.:
   - `identifier`: "GV-1" (referentie)
   - `offers.price`: "790000", `priceCurrency`: "EUR", `availability`: InStock
   - `floorSize`: 240 (MTK = m²), `numberOfBedrooms`: 6, `numberOfBathroomsTotal`: 3
   - `address.addressLocality`: "Cap Martí", `postalCode`: 03730, `geo`: 38.789 / 0.163
   - `datePosted`: 2026-03-22, `validThrough`: 2027-03-22
   - `amenityFeature`-lijst (piscina privada, jardín, terraza …), 28 afbeeldingen, `seller` = RealEstateAgent met kantooradres
   - **Perceel ontbreekt** in JSON-LD (geen `lotSize`); wél in de zichtbare tekst: "1,100m²" en in de beschrijving "parcela llana de 1.100 metros cuadrados"
2. `BreadcrumbList`: Inicio → Propiedades → Villa → Jávea → Cap Martí → object

**og:-tags:** og:type (website én product), og:title, og:description, og:url, og:image (meerdere, 1200×630), og:published_time, og:updated_time (2026-09-24T20:31:22), og:locale es_ES, plus twitter:card. Ook `<link rel="canonical">` en meta description.

Zichtbaar in de tekst: "790.000€", "Ref: GV-1", "240m²" (bebouwd), "1,100m²" (perceel), 6 slaapkamers, 3 badkamers. De extra prijzen (€799.000, €850.000 …) en m²-waarden op de pagina horen bij de "vergelijkbare woningen"-blokken — daar rekening mee houden bij het uitlezen.

## 5. Systeem — eigen bouw (Laravel)

Geen sporen van Inmoweb, Mediaelx/LetsINMO, Sooprema, Inmovilla, Witei of WordPress (geen wp-content, geen generator-meta, geen "powered by"). Aanwijzingen voor een maatwerksite op Laravel:

- Cookies: `XSRF-TOKEN` + `andrea-y-olaf-session` (Laravel-naamgeving), `csrf-token`-meta in de HTML
- Afbeeldingen onder `/storage/properties/{id}/images/es/…` (Laravel public-storage-koppeling); logo onder `/images/`
- Eigen `/css/app.css`, `/js/app.js`, `/js/search.js`, `/js/favorites.js`, `/js/property-detail.js`
- Bibliotheken via CDN: GSAP, Splide, Pace, Font Awesome, intl-tel-input; Tailwind-klassen
- Header `server: o2switch-PowerBoost-v3` (Franse hoster); Ahrefs-analytics
- Site heeft een login/registratie-modal (favorieten) en een reCAPTCHA — we loggen niet in en vullen niets in

Gevolg: geen standaard exportfeed (zoals bij Inmoweb/Mediaelx). Als lezen ooit niet meer mag, moet een feed apart gevraagd worden.

## 6. Omvang en Jávea-dekking

- **Aanbodpagina** https://www.andreayolaf.com/propiedades-en-venta (HTTP 200, 24-09-2026): "Mostrando 1-24 de 476", JSON-LD `ItemList` met `numberOfItems: 476`, 24 per pagina, 20 pagina's (`?page=2` … `?page=20`). Kaartjes tonen prijs en linken naar de objectpagina.
- **Sitemap:** 440 objectpagina's. Verschil met 476 (~36) is niet verklaard — mogelijk nieuwe of tijdelijk uit de sitemap gehouden objecten. Schatting: **circa 440–476 objecten**.
- Plaatsverdeling van de 440 sitemap-objecten: Jávea 185 · Moraira 57 · Benissa 56 · Benitachell 25 · Calpe 24 · Dénia 19 · Teulada 12 (deels Moraira-zones) · Pedreguer 12 · Altea 10 · Alcalalí 7 · overige 33.
- **Jávea + Benitachell + Moraira: 267 van 440 = ~61 %** (Jávea alleen: 42 %). Rekent men de Teulada-objecten met Moraira-zone mee, dan iets hoger.

## Praktisch voor de lezer

- Startpunt: sitemap.xml (440 objecturls, wekelijks bijgewerkt) of de aanbodpagina met `?page=N` (20 pagina's à 24).
- Per object: JSON-LD `RealEstateListing` uitlezen (prijs, m², slaapkamers, badkamers, referentie, geo, datum); perceel uit de zichtbare tekst halen (patroon `\d[\d\.,]*\s?m²` in het kenmerkenblok, niet in het blok "vergelijkbare woningen").
- Tempo: max. 1 pagina per 2 s; hele aanbod = ~460 pagina's ≈ 16 minuten; volstaat wekelijks.
- Verandering opsporen: `og:updated_time` en `datePosted` per object; `validThrough` = 1 jaar na plaatsing.
- Geen foto's of beschrijvende teksten opslaan of hergebruiken (voorwaarden, punt 2).

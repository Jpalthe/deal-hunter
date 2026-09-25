# Ahermar — www.ahermar.com

Toets op automatisch lezen · 24-09-2026 (opgehaald 21:30–21:33 UTC) · TREE Deal Hunter

**Advies: lezen** — er is geen robots.txt en geen gebruiksvoorwaarde die het verbiedt; de pagina's zijn gewone, server-gerenderde HTML met duidelijke labels. Wel netjes: één pagina per twee seconden, herkenbare user-agent. Er is geen sitemap, dus objecten vind je alleen via de aanbodpagina `/venta`.

Vijf pagina's opgehaald (het maximum): robots.txt, homepage, sitemap.xml, aviso-legal en één objectpagina. Niet opgehaald: `/venta` (aanbodlijst), `/sitemap_index.xml`, `/politica-privacidad`, `/cookies`.

## 1. robots.txt — bestaat niet

- Bron: https://www.ahermar.com/robots.txt → **HTTP 404** (24-09-2026). De server geeft de gewone "Página no encontrada - Error 404"-pagina terug.
- Gevolg: er is niets verboden voor `User-agent: *`; er is ook geen `Sitemap:`-regel. Zonder robots.txt geldt de gangbare conventie dat lezen is toegestaan, maar het is geen uitdrukkelijke toestemming.

## 2. Gebruiksvoorwaarden — pagina bestaat, maar is leeg

- Bron: https://www.ahermar.com/aviso-legal → HTTP 200 (24-09-2026). De pagina bevat alleen de kop "Aviso Legal" en de vaste kop- en voettekst (adres, telefoon, links). Geen enkele zin met voorwaarden, geen woorden als scraping, robots, extracción, base de datos of prohibido.
- Aparte pagina's `/politica-privacidad` en `/cookies` zijn niet geopend (paginabudget); die gaan normaal over persoonsgegevens en cookies, niet over lezen van het aanbod.
- Conclusie: **geen verbod gevonden**. Omdat de aviso legal leeg is, is er ook geen uitdrukkelijk kader; bij twijfel kan het kantoor gewoon gevraagd worden (algemeen e-mailadres in voettekst: javea@ahermar.com).

## 3. Sitemap — niet aanwezig

- https://www.ahermar.com/sitemap.xml → **HTTP 404** (24-09-2026).
- robots.txt ontbreekt, dus ook geen Sitemap-verwijzing. `/sitemap_index.xml` niet geprobeerd (budget van vijf pagina's op).
- Aantal object-URL's in sitemap: **onbekend / 0**. Objecten ontdek je via de lijstpagina `/venta` (met filters op operatie, plaats, type, slaapkamers, prijs).

## 4. Aanbodpagina en objectpagina

- Aanbodpagina (uit het menu): https://www.ahermar.com/venta — sub-lijsten zoals `/venta/apartamentos/javea-xabia`. Niet geopend.
- Objectpagina geopend: https://www.ahermar.com/apartamento-en-javea-206.html (HTTP 200, 24-09-2026).
- URL-patroon objecten: `/<type>-en-<plaats>-<id>.html`, bijvoorbeeld `/apartamento-en-javea-206.html`; verhuur `/apartamento-en-alquiler-en-javea-189.html`.

**JSON-LD** (`<script type="application/ld+json">`): aanwezig, maar alleen een `LocalBusiness`-blok over het kantoor zelf (naam, adres Avenida de la Fontana 4, Local 33, 03730 Jávea; telefoon; openingstijden; coördinaten). Het staat op elke pagina, ook de 404-pagina. **Geen** `Product`, `Offer` of `RealEstateListing` met objectgegevens.

**og:-tags**: **geen** (ook geen twitter:-tags). Alleen `<title>`: "Apartamento en Jávea - B/1313 | Inmobiliaria AHERMAR".

**Wat er wél in de gewone HTML staat** (labels en waarden, makkelijk te lezen):

| Veld | Waarde op de voorbeeldpagina |
|---|---|
| Prijs | 395.000 € |
| Referentie | B/1313 |
| Plaats | Playa del Arenal, Jávea |
| Oppervlakte (Superficie) | 100 m2 |
| Terras | 30 m2 |
| Perceel | niet vermeld (appartement; label "Parcela" ontbreekt op deze pagina) |
| Kamers / badkamers | 3 / 1 |
| Overig | uitzicht open, zuid, staat "Muy Buena", gerenoveerd, energielabel in aanvraag, 1.000 m tot zee |

Let op: de `<link rel="canonical">` op de objectpagina wijst naar de homepage (SEO-fout van de site), niet naar het object zelf. Voor ons maakt dat niet uit, maar het verklaart waarom objecten slecht in Google zitten.

## 5. Systeem achter de site — eigen bouw (PHP)

Aanwijzingen (24-09-2026):
- Cookie `PHPSESSID`, server `Apache/2.4.58 (Ubuntu)`; headers `cache-control: no-store` op elke pagina.
- Eén css- en één js-bestand met een tijdstempel als naam: `/assets/css/1788615695.css`, `/assets/js/1688735195.js`. Objectfoto's op een eigen subdomein: `https://img.ahermar.com/f/lg/<datum>/<bestand>.jpeg` (fotogalerij met Owl Carousel + lightbox, `data-plugin-options` zoals in het Porto-HTML-template).
- Geen HTML-commentaar, geen `generator`-meta, geen "powered by", geen `wp-content`, geen sporen van Inmoweb, Mediaelx/LetsINMO, Sooprema, Inmovilla of Witei. Zoekformulier met eigen `data-codigo`-attributen (V, AA, AV, T).
- Front-end: Bootstrap/Porto-achtige klassen, Owl Carousel, Font Awesome 5, Modernizr, Google Fonts, reCAPTCHA, Google Analytics (UA-property).

Conclusie: **eigen bouw**, geen bekende makelaars-CMS. Dus ook geen standaard exportfeed om te vragen; eventueel wel een handmatige export of een portalfeed (Idealista/Kyero) als het kantoor die gebruikt [te verifiëren].

## 6. Omvang en dekking Jávea/Benitachell/Moraira

- Aantal objecten: **niet te schatten** zonder de lijstpagina. De referentienummers (B/1309, B/1312, B/1313 voor verkoop; A/015, A/057 voor verhuur) zijn doorlopende tellers sinds de start, geen actueel aantal. De homepage toont maar drie "laatste" verkoopobjecten, waarvan één "RESERVADO" en één "VENDIDO".
- Dekking: het kantoor is een Jávea-kantoor (Arenal; volgens de eigen omschrijving sinds 1984). De plaatsenlijst in het zoekformulier: Jávea, Denia, Pedreguer, Jesus Pobre, Ondara, **Benitachell**. **Moraira staat er niet in.** Alle getoonde objecten liggen in Jávea (Playa del Arenal). Verwachting: overgrote deel Jávea, klein deel Benitachell/Denia [te verifiëren via /venta].
- Types in het formulier: appartementen, bungalows, dorpshuizen, garages, moestuinen (huertos), winkels, loodsen, kantoren, **parcelas, solares**, villa's, duplex, penthouses, ligplaatsen, geschakeld, casitas de campo, studio's. Ook "traspaso" (overname) als operatie. Interessant voor Deal Hunter: percelen en oudere/renovatie-objecten.

## Praktisch voor de lezer

1. Startpunt: `https://www.ahermar.com/venta` en de type/plaats-sublijsten (`/venta/<type>/<plaats>`), paginering nog te bekijken.
2. Objectpagina: lees de label-waarde-paren (Precio, Referencia, Ubicación, Superficie, Terraza, Parcela, Habitaciones, Baños, Conservación, Tipo construcción, Distancia al mar). Status ("RESERVADO", "VENDIDO") staat in de titel.
3. Tempo: één pagina per twee seconden, met een herkenbare user-agent en contactadres.
4. Geen JSON-LD/og voor objecten, dus geen snelle metadata-route; gewone HTML-parsing is nodig.

Bronnen: alle URL's hierboven, opgehaald op 24-09-2026 tussen 21:30 en 21:33 UTC.

# Alensol S.L. — www.alensol-javea.com

Toets op automatisch lezen · TREE Deal Hunter · datum: 24-09-2026

**Advies: lezen** — robots.txt staat het toe, er is geen verbod gevonden en de
objectpagina's zijn gewone HTML met een nette label/waarde-tabel. Maar let op:
het aanbod is heel klein (2 objecten beschikbaar, 2 gereserveerd, 13 verkochte
objecten die nog online staan). Lage prioriteit als bron, hooguit één keer per
week kijken.

## Kantoor

- Bedrijf: Alensol S.L. (site-naam "ALENSOL-JAVEA")
- Kantooradres: Carretera de la Granadella 23, 03730 Xàbia/Jávea (Alicante)
- Algemeen contact: 966 470 221 · info@alensol.com
- Doet naast verkoop ook verhuur (`alquiler-490-2902`), bouw, renovatie en
  onderhoud (menu-items "Construcción", "Reformas", "Mantenimiento").
- Bron: voettekst van https://www.alensol-javea.com/producto-d-2026-01-490-493446-2903-es.html (24-09-2026)

## 1. robots.txt — toegestaan

Bron: https://www.alensol-javea.com/robots.txt (HTTP 200, 24-09-2026). Volledige inhoud:

```
User-agent: *
Disallow: /*.php
Disallow: /*.css
Disallow: /*.htaccess
Allow:/index.php
Allow:/login.php
Allow:/empresa.php
Allow:/clients/
```

Uitleg: alleen URL's die op `.php`, `.css` of `.htaccess` eindigen zijn verboden.
De aanbodpagina (`/venta-490-2903`, zonder extensie) en de objectpagina's
(`producto-…-2903-es.html`) vallen daar niet onder. Een `User-agent: *` mag het
aanbod dus lezen. (De `Allow:`-regels missen een spatie na de dubbele punt; dat
verandert niets aan de conclusie.)

## 2. Voorwaarden — geen verbod gevonden

- Aviso legal: https://www.alensol-javea.com/aviso-legal-490-25.html (HTTP 200,
  24-09-2026). De pagina is **leeg**: alleen de kop "Aviso legal", de inhoudsdiv
  (`<div class="row-fluid privacy">`) bevat niets. Geen enkele bepaling over
  scraping, robots, databankrechten of hergebruik.
- Niet opgehaald (paginabudget van vijf was op): `condiciones-venta-490-14.html`
  en `politica-privacidad-490-19.html`. Die staan wel in de voettekst; bij een
  volgende ronde alsnog nalopen.

Conclusie: verbod niet gevonden.

## 3. Sitemap — niet aanwezig

- robots.txt heeft geen `Sitemap:`-regel.
- https://www.alensol-javea.com/sitemap.xml → HTTP 404 (eigen 404-pagina:
  "Lo sentimos página no encontrada"), 24-09-2026.
- `/sitemap_index.xml` niet geprobeerd (budget).
- Aantal object-URL's in sitemap: n.v.t.

## 4. Aanbodpagina en objectpagina

**Aanbodpagina:** https://www.alensol-javea.com/venta-490-2903
De startpagina stuurt met een 302 meteen door naar deze pagina (24-09-2026).
Op de eerste pagina staan 17 objectkaarten (uit de links `producto-…-2903-es.html`):

| Status (uit de URL) | Aantal |
|---|---|
| beschikbaar (`d-2026-01`, `parcela-en-denia`) | 2 |
| `reservada` | 2 |
| `vendida` / `vendido` (verkocht, nog online) | 13 |

Paginering is niet vastgesteld; waarschijnlijk is dit het hele aanbod.

**Objectpagina:** https://www.alensol-javea.com/producto-d-2026-01-490-493446-2903-es.html (HTTP 200, 24-09-2026)

- `<script type="application/ld+json">`: **niet aanwezig**.
- og-tags: `og:title` = "D-2026-01", `og:description` = leeg, `og:type` = article,
  `og:image` = foto op hadbos.com, `og:url`, `og:site_name` = "ALENSOL-JAVEA".
  Dus: og aanwezig, maar zonder prijs of oppervlakte.
- `<meta name="robots" content="all | index | follow">`.
- De gegevens staan als gewone tekst in een label/waarde-tabel in de HTML
  (goed uitleesbaar):
  - Referentie: D-2026-01 · "Ref: CARRER ROGET - JAVEA"
  - Prijs: 885.000,00 €
  - Type: chalet · Plaats: Jávea (Xàbia) · Zone: Urb. Costa Nova (La Guardia)
  - Bebouwd: 120 m² + 15 m² · Perceel: 2.044 m² · Bouwjaar 1969
  - 4 slaapkamers + buitenslaapkamer, 1 badkamer + 2 toiletten met douche,
    twee verdiepingen, zeezicht, overdekte parkeerplaats, geen zwembad
  - Omschrijving: "chalet con vistas al mar, aconsejable reformar. Posibilidad
    de obtener dos parcelas" — renovatieobject, perceel mogelijk splitsbaar.
    **Interessant voor Deal Hunter** [te verifiëren: splitsbaarheid en prijs].

## 5. Systeem achter de site

Geen van de bekende vastgoed-CMS'en. Aanwijzingen (objectpagina, 24-09-2026):

- Alle media en favicons staan op `https://www.hadbos.com/wpm/docs/lagaleria/docs/236/490/…`
  (klantnummer 236/490) — een gehost platform van Hadbos ("wpm").
- Sjabloonpaden `plantillas_bootstrap/plantilla1/…` en `plantilla_inmo_1/…`,
  html-commentaar "import css hadbos", klant-css op
  `clients/www.alensol-javea.com/css/dominio.css`.
- Winkelachtige opzet: `assets/js/functions_shop.js`, `login.php` ("Mi cuenta"),
  categorie-id's 2903 (venta) en 2902 (alquiler). De 404-pagina heeft nog een
  PrestaShop-sjabloontekst, maar de site zelf is geen PrestaShop.
- Server: nginx, PHP 7.4.33, Plesk; cookie `PHPSESSID`.
- Geen sporen van Inmoweb, Mediaelx/LetsINMO, Sooprema, Inmovilla, Witei of
  WordPress (`wp-content`).

Classificatie: **eigen / gehost webshop-platform van Hadbos** — geen bekende
exportfeed [te verifiëren].

## 6. Omvang en dekking Jávea

- Geschat aanbod te koop: **2 beschikbaar** (+2 gereserveerd; 13 verkochte
  objecten staan nog online).
- Dekking Jávea/Benitachell/Moraira: van de 2 beschikbare objecten ligt er 1 in
  Jávea (Costa Nova) en 1 is een perceel in Dénia. De verkochte objecten zijn
  niet geopend, dus onbekend. Het kantoor zit zelf in Jávea (Granadella).

## Werkwijze en beperkingen

- Vijf ophaalacties, elk minstens twee seconden na elkaar: robots.txt,
  startpagina (→ venta), sitemap.xml, aviso legal, één objectpagina.
- Niet ingelogd, geen formulieren gebruikt.
- Niet bekeken: condiciones de venta, política de privacidad, sitemap_index.xml,
  de tweede beschikbare kaart (perceel Dénia), de verhuurpagina.
- Bij het lezen: houd de eigen wachttijd aan (1 pagina per 2 s), het aanbod is
  zo klein dat één wekelijkse controle van `/venta-490-2903` volstaat.

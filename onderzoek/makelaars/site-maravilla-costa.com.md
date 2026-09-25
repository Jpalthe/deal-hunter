# Maravilla Costa S.L. — toets op automatisch lezen

- **Website:** https://www.maravilla-costa.com (bedrijf: Maravilla Costa, S.L. volgens de eigen "Legal notice"; kantoor Avda. del Plá 124, local 8, 03730 Jávea; algemeen kanaal info@maravilla-costa.com, +34 965 794 515 — uit de voettekst van de site, 24-09-2026)
- **Datum toets:** 24-09-2026, ca. 23:15–23:22 lokale tijd (server-datumkop 21:16 UTC)
- **Opgehaald (5 verzoeken, telkens ≥ 14 s tussenruimte vanwege `Crawl-delay: 14`):** robots.txt, sitemap.xml, homepage, legal-notice-pagina, één objectpagina. Dus 3 HTML-pagina's plus twee tekst/XML-bestanden. De aanbodpagina `/for-sale/` zelf is **niet** opgehaald (budget van vijf pagina's op); de link staat wel in sitemap en menu.
- **Advies: feed vragen.** robots.txt laat lezen toe (met 14 s wachttijd), maar de voorwaarden verbieden commercieel gebruik en reproductie van de inhoud. De site draait op **Sooprema**, dat aanbod naar portalen exporteert; een feed is schoner, sneller en vollediger dan zelf lezen. Het aanbod is klein (ca. 25 eigen objecten) maar voor ca. 60 % in Jávea/Moraira/Benitachell, dus de moeite waard.

## 1. robots.txt — deels toegestaan (lezen mag, met beperkingen)

Bron: https://www.maravilla-costa.com/robots.txt (24-09-2026, HTTP 200). Geen `Sitemap:`-regel. Relevante regels voor iedereen (`User-agent: *`):

```
User-agent: *
Disallow: /cgi-bin/
Disallow: /images/
Disallow: /html/formulario/llamanos/
Disallow: /html/formulario/48horas/
Disallow: /admin/
Disallow: /html/galeriamodal/*
Disallow: /html/formucontraoferta/*
Disallow: /*/*/*/pagina/*
Disallow: /*/*/*/pages/*
Disallow: /*/*/*/page/*
Disallow: /*/*/*/seite/*
...
Disallow: */imprimir/*
Disallow: */print/*
Disallow: */afdrukken/*
Allow: /

[... ca. 140 blokken met "Disallow: /" voor specifieke programma's, o.a. Wget, HTTrack, Python-urllib, WebZip, Offline Explorer, WebCopier, EmailCollector ...]

User-agent: *
Crawl-delay: 14
```

Uitleg:
- `Allow: /` voor `User-agent: *`: de aanbodpagina (`/for-sale/`), de categoriepagina's en de objectpagina's (`/for-sale/<slug>-<nummer>/`) mogen gelezen worden.
- Wél verboden: de beeldmap `/images/`, formulieren, de fotogalerij-modal, printversies, en **paginering op diepere filterpagina's** (`/*/*/*/page/*` — pas vanaf drie padniveaus, dus bv. `/for-sale/javea/villa/page/2/`). Of de hoofdlijst `/for-sale/` zelf pagineert via zo'n pad is niet gecontroleerd [te verifiëren].
- Het tweede `User-agent: *`-blok zet **`Crawl-delay: 14`**: maximaal één verzoek per 14 seconden. Dat is de norm voor elke lezer van ons. Bij ca. 25 objecten is een volledige ronde dan ~6 minuten.
- De lange lijst met verboden programma's zegt iets over de houding: downloaders en scrapers zijn expliciet ongewenst. Een eigen lezer valt niet onder een van die namen, maar het is een duidelijk signaal — vandaar dat een feed netter is.

## 2. Gebruiksvoorwaarden — geen expliciet scrapingverbod, wél verbod op commercieel gebruik en reproductie

Bron: https://www.maravilla-costa.com/legal-notice/ (24-09-2026, HTTP 200). De pagina staat ook op de Engelse site alleen in het **Spaans** en bevat aviso legal, condiciones generales, privacybeleid en cookiebeleid in één stuk. De woorden scraping, robot, crawler, bot, "automatizado" of "automático" komen niet voor in relatie tot lezen van de site. Wel relevant:

- Onder "CONDICIONES GENERALES DE USO": de voorwaarden regelen het gebruik "(incluyendo el mero acceso)" van de site; wie de site bezoekt "acepta someterse a las Condiciones Generales".
- Onder "COMPROMISOS Y OBLIGACIONES DE LOS USUARIOS": "Respecto de los contenidos de esta web, se prohíbe: Su reproducción, distribución o modificación, total o parcial, a menos que se cuente con la autorización de sus legítimos titulares; [...] Su utilización para fines comerciales o publicitarios." Verder mag de gebruiker niets doen dat het portaal kan "dañar, inutilizar o sobrecargar".
- Onder "DERECHOS DE PROPIEDAD INTELECTUAL E INDUSTRIAL": op grond van art. 8 en 32.1 tweede lid van de Ley de Propiedad Intelectual zijn "expresamente prohibidas la reproducción, la distribución y la comunicación pública [...] de la totalidad o parte de los contenidos de esta página web, con fines comerciales, en cualquier soporte y por cualquier medio técnico, sin la autorización de www.maravilla-costa.com."

**Betekenis voor Deal Hunter:** automatisch lezen wordt niet met zoveel woorden verboden, maar (a) het gebruik van de inhoud voor commerciële doelen is verboden en (b) reproductie van de inhoud zonder toestemming ook. Een acquisitiesysteem is een commercieel doel. Kale feiten (prijs, plaats, m², perceel, referentie, link) zijn geen auteursrechtelijk beschermde "inhoud", maar foto's en beschrijvingsteksten wél; die nooit overnemen. Omdat de tekst zo breed is geformuleerd, is de veilige route: **toestemming of een feed vragen**. Beoordeling in de structuur: "voorwaarden verbieden scraping: nee" (niet expliciet), met deze kanttekening.

## 3. Sitemap — 39 URL's, waarvan 24 objectpagina's

Bron: https://www.maravilla-costa.com/sitemap.xml (24-09-2026, HTTP 200, 7,8 kB; `lastmod` van de homepage is 2026-09-24, dus dagelijks ververst).

- 39 URL's: homepage, 6 informatiepagina's (about-us, services, sell, buy, contact, promos), `/for-sale/`, `/rentals/`, 6 categoriepagina's (commercial, apartments, new builds, luxury villas, villas in Jávea, plots) en **24 objectpagina's** met patroon `/for-sale/<beschrijvende-slug>-<p|m>-<nummer>/` (nummers 2274 t/m 2547; de letter p/m lijkt een interne code, geen plaats).
- Trefwoorden: "villa" komt in bijna elke URL voor maar ook in de domeinnaam (mara**villa**), dus niet bruikbaar als teller; "plot" 7×, "apartment" 2×, "finca" 1×, "commercial" 1×. Geen Spaanse woorden (venta, inmueble, parcela) — de sitemap is Engels.
- **Let op:** het nieuwste object P-2548 (staat op de homepage en als "You might like" op de objectpagina) zit nog niet in de sitemap. De sitemap loopt dus iets achter op het echte aanbod.
- Aparte domeinen per taal (`hreflang`): maravilla-costa.es (ES), maravillacostablanca.de (DE), maravilla-costa.fr (FR). Zelfde aanbod, niet apart getoetst.

## 4. Aanbodpagina en objectpagina

**Aanbodpagina te koop:** https://www.maravilla-costa.com/for-sale/ (in sitemap en hoofdmenu "Buy"; niet opgehaald). Het menu op de homepage toont filterpagina's per plaats (`/for-sale/javea/`, `/benitachell/`, `/moraira/` — laatste [te verifiëren], gezien: altea, benissa, benitachell, calpe, denia), per type (`/apartment/`, `/country-house/` ...), per aantal slaapkamers/badkamers en per bouwoppervlak (`/build-200-to-300-m2/`). Er staan ook zes SEO-categoriepagina's (o.a. `villas-for-sale-in-javea`, `plots-for-sale-in-costa-blanca`).

**Objectpagina bekeken:** https://www.maravilla-costa.com/for-sale/very-well-maintained-mediterranean-style-single-story-house-for-sale-in-javea-p-2547/ (24-09-2026, HTTP 200, ~208 kB).

- `<script type="application/ld+json">`: **nee, 0 blokken.** Geen schema.org op de objectpagina.
- **og:-tags: ja** — `og:url`, `og:type` (= "website", niet product/offer), `og:title` ("Very well-maintained, Mediterranean-style single-story house for sale in Jávea."), `og:description` (afgekapte beschrijving, ~150 tekens), `og:image` (https://www.maravilla-costa.com/opi/363865, 640×425), `og:locale` en_GB, `og:site_name` "Maravilla Costa". **Geen prijs, oppervlak of plaats in de og-tags.**
- In de leesbare HTML staan de feiten wél helder en als vaste velden: **Ref. P-2547 · 745.000 € · 161 m² bebouwd · 1.019 m² perceel · 3 + 1 slaapkamers · 2 + 1 badkamers · Type: Villa · Town: Jávea · Area: La Cala · Floors: 1 · Terrain type: Flat land**, plus label "Exclusive", energiecertificaat-sectie en "Approximate location" (kaart via Leaflet). Handig voor een lezer: `data-property-id="363865"`, `data-property-ref="P-2547"` en `data-property-url="..."` als attributen in de HTML.
- Onder "You might like these properties too" staat naast P-2548 ook een object met **Ref. 4628JAV** (Villa in Javea, 725.000 €, 200 m²) — een ander referentieformaat, wat wijst op gedeelde/collega-objecten uit het Sooprema-netwerk [te verifiëren]. Het eigen aanbod is dus mogelijk kleiner dan wat de site toont.

## 5. Systeem achter de site: Sooprema

Bewijs (homepage en objectpagina, 24-09-2026):
- Alle CSS/JS staat onder `/crm/pages/vendor/sooprema/...` (o.a. `sooprema-captcha`, `sooprema/favorites`, `sooprema/analytics/1.0/analyzer.js`, `sooprema/prevent-images-rightclick`), het thema onder `/crm/pages/agencies/maravillacosta/theme/` en de widgets onder `/crm/pages/widgets/base/...`, alles met versiestring `?v=0.3.23`. Het woord "sooprema" komt 40× voor in de homepage-HTML.
- Beeld-URL's via `/opi/<id>` (og:image `/opi/363865`), zoekformulier post naar `/for-sale/` en directe referentiezoek via `/ref-{{ref}}/`.
- Server: Apache; geen cookies bij een kale GET; geen `generator`-meta en geen "powered by"-tekst; HTML-commentaar alleen swiper-restanten en een rendertijd (`<!-- 0.713 s -->`).
- Opvallend: het script `prevent-images-rightclick` — foto's zijn bewust beschermd tegen kopiëren. Sluit aan op de voorwaarden.

Sooprema is een Spaans CRM/website-platform voor makelaars met portaalexport (XML-feeds) en een samenwerkingsnetwerk tussen kantoren [te verifiëren — sooprema.com is niet opgehaald; zoekbudget van de sessie was op]. Aanpak bij Jan's verzoek: vragen om een XML-/feed-export van het eigen aanbod (Kyero- of Idealista-formaat, zoals Sooprema aan portalen levert).

## 6. Omvang en Jávea-dekking

Op basis van de 24 objectpagina's in de sitemap (plaats afgelezen uit de URL-slug, 24-09-2026):

| Plaats | Aantal |
|---|---|
| Jávea (incl. Ambolo, Tosalet, Cala Blanca, Costa Nova, La Cala) | 10 |
| Moraira (incl. Benimeit; 1× Fanadix/Teulada-Moraira) | 4 |
| Benitachell | 1 |
| Teulada (excl. Moraira) | 1 |
| Calpe | 2 |
| La Sella (Pedreguer/Dénia) | 2 |
| Altea | 1 |
| Benissa (Canor) | 1 |
| Zonder plaats in de URL (2543, m-2530) | 2 |

- **Jávea + Benitachell + Moraira: 15 van 24 (63 %)**; van de 10 Jávea-objecten zijn 4 percelen (Ambolo, Costa Nova 3 percelen, m-2274) en 1 apartement bij de Arenal/Canal de la Fontana.
- Type over de hele sitemap: ca. 7 percelen, 2 apartementen, 1 finca, ca. 14 villa's/huizen (incl. 3 in aanbouw/nieuwbouw).
- **Schatting eigen aanbod: ~25 objecten** (24 in de sitemap + P-2548 op de homepage). Het echte getal op `/for-sale/` is niet geteld [te verifiëren]; door gedeelde objecten (zoals 4628JAV) kan de site meer tonen dan het eigen aanbod.
- Prijsniveau (uit de sitemap-titels en de bekeken pagina's): "luxury villa", "under construction", percelen met zeezicht; de bekeken villa 745.000 € en de twee buren 725.000 en 769.000 €. Voor Deal Hunter zijn vooral de 7 percelen en de oudere Mediterrane huizen (renovatiekans) interessant.

## Conclusie en aanbevolen werkwijze

1. **Feed vragen** bij Maravilla Costa (info@maravilla-costa.com): Sooprema-export van het eigen aanbod. Dat past binnen de voorwaarden en geeft alle velden netjes (prijs, m², perceel, plaats, referentie), inclusief objecten die nog niet in de sitemap staan.
2. Tot die tijd, als Jan toch wil meekijken: alleen de sitemap (dagelijks ververst, 8 kB) lezen en per nieuw object hooguit één keer de pagina, met **≥ 14 s tussen verzoeken**, alleen kale feiten opslaan, geen foto's of teksten, geen paginering op filterpagina's. Dat blijft binnen robots.txt maar schuurt tegen de clausule "fines comerciales" — dus liever punt 1.
3. Geen JSON-LD, dus een lezer moet de vaste tekstvelden ("Plot size:", "Constructed area:", "Town:", "Area:") en de `data-property-*`-attributen gebruiken; die zijn stabiel binnen Sooprema-sites.

⏸️ ACTIE VOOR JAN: beslissen of we Maravilla Costa om een feed vragen (één mail via het algemene adres) en of de Sooprema-portaalexport [te verifiëren] als standaardroute geldt voor alle Sooprema-kantoren in de lijst.

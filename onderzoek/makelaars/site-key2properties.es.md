# Key2 Properties — toets op automatisch lezen

- **Website:** https://key2properties.es
- **Datum toets:** 24-09-2026 (ca. 23:36–23:38 CEST)
- **Rechtspersoon:** KEY 2 RENTALS SL (CIF B09793894) — bron: https://key2properties.es/privacy-policy (24-09-2026)
- **Kantoor:** Avda. Príncipe de Asturias 33, 03730 Jávea — bron: kop van de site (24-09-2026)
- **Algemene contactkanalen:** info@key2properties.es · +34 674 095 028 · ma–vr 10.00–17.00 — bron: kop/voettekst (24-09-2026)
- **Opgehaalde pagina's (5, steeds ≥ 2 s ertussen):** `/robots.txt`, `/sitemap.xml`,
  `/property/4-bedroom-villa-for-sale-in-javea-ks3406`, `/privacy-policy`, `/property-search/sale/javea/xabia`

## Advies: LEZEN

robots.txt staat alles toe, er zijn geen gebruiksvoorwaarden die automatisch lezen verbieden (er is überhaupt
geen voorwaarden- of aviso-legal-pagina), en de objectpagina's zijn gewone server-gerenderde HTML waar prijs,
bouw- en perceeloppervlak, plaats en referentie leesbaar in staan. Spelregels:

1. Nooit sneller dan één pagina per twee seconden. 141 koopobjecten = ca. 5 minuten voor een volledige ronde.
   Daarna alleen nieuwe of gewijzigde URL's ophalen via de sitemap.
2. De aanbodlijst bladert via JavaScript (geen paginalinks in de HTML) — gebruik de **sitemap** als bron van
   alle object-URL's, niet de zoekpagina.
3. 30 van de 141 koopobjecten (Cumbre del Sol en Altea, referenties `21222_...`) lijken een doorgeplaatste
   nieuwbouwfeed van een projectontwikkelaar **[te verifiëren]**; die staan waarschijnlijk ook bij andere
   kantoren. Ontdubbelen op referentie.
4. Foto's en beschrijvingen niet overnemen of publiceren; intern lezen, vergelijken en scoren.

## 1. robots.txt

- URL: https://key2properties.es/robots.txt (HTTP 200, 76 bytes, 24-09-2026)
- Volledige inhoud:

```
User-agent: *
Disallow:
Sitemap: https://key2properties.es/sitemap.xml
```

- Een lege `Disallow:` betekent: **alles mag gelezen worden**, ook de aanbod- en objectpagina's.
  Geen `Crawl-delay`. Wél een `Sitemap:`-regel.

## 2. Gebruiksvoorwaarden

- **Niet gevonden.** De voettekst linkt alleen naar `/privacy-policy` en `/cookie-policy`; de navigatie en de
  sitemap (236 URL's) bevatten geen pagina met terms, aviso legal, condiciones of disclaimer.
- https://key2properties.es/privacy-policy (HTTP 200, 24-09-2026) is een Spaanstalige AVG-verklaring
  (verwerkingen, rechten van betrokkenen, verantwoordelijke). De woorden scraping, crawl, robot, bot of
  "uso automatizado" komen er niet in voor; de enige treffers op "automatizad" gaan over het recht op
  dataportabiliteit en over geautomatiseerde besluitvorming — niets over het lezen van de site.
- `/cookie-policy` is niet opgehaald (budget van vijf pagina's).
- Conclusie: geen verbod op automatisch lezen gevonden. Er staat ook geen auteursrechtclausule op de site,
  maar normale terughoudendheid met foto's en teksten blijft gelden.

## 3. Sitemap

- URL: https://key2properties.es/sitemap.xml (HTTP 200, 38 kB, 24-09-2026; genoemd in robots.txt).
  Eén platte `urlset`, geen sitemap-index.
- **236 URL's**, waarvan **225 objectpagina's** onder `/property/{slug}-{referentie}` en 11 informatiepagina's
  (home, about-us, contact-us, buying/selling, property-management, the-team, faqs, services, privacy, cookies).
- Verdeling van de 225 objecten (op basis van de slug):
  - **141 te koop** ("for-sale"): 80 villa's, 22 percelen, 18 appartementen, 6 penthouses, 6 rijtjes-/
    dorpshuizen, 4 finca's, 3 bedrijfspanden, 1 duplex, 1 bungalow
  - 83 huur (langetermijn en winter; 58 daarvan in Jávea)
  - 1 traspaso (restaurant in Dénia)
- Te koop per plaats: **Jávea 68**, Cumbre del Sol 26 (gemeente Benitachell; 25 daarvan uit de `21222_`-feed),
  **Benitachell 13**, **Moraira 3**; verder Dénia 5, Altea 5 (feed), Calpe 4, Benissa 3, Jesús Pobre 2,
  Orba 2, Pedreguer 2, Teulada 2, en 1 elk in Alicante, Bétera, Gata de Gorgos, Jijona, Llíber, Yecla.
- Referentiecodes: `KS` = koop, `KR` = huur, `KCS` (4 stuks) onduidelijk, `21222_xxx` = externe feed.
  Sommige slugs eindigen op `-0` (waarschijnlijk een versienummer van het platform).
- De sitemap heeft `lastmod`-velden (gezien bij de informatiepagina's, o.a. home 2026-06-12); voor de
  objectpagina's niet apart gecontroleerd. Bruikbaar als wijzigingsdetector zodra dat bevestigd is.

## 4. Aanbod- en objectpagina

- Aanbodpagina's (uit de navigatie): `/villas-for-sale`, `/apartments-for-sale`, `/penthouses-for-sale`,
  `/townhouses-for-sale`, `/plots-for-sale`, `/commercials-for-sale`, en per plaats
  `/property-search/sale/javea/xabia`, `/denia`, `/benitachell`, `/pedreguer`, `/ondara`.
- Bekeken lijst: https://key2properties.es/property-search/sale/javea/xabia (HTTP 200, 120 kB, 24-09-2026).
  Server-gerenderd: 30 objectkaarten in de HTML, alle 30 in Jávea, met prijs en referentie. Teller
  "1 to 30 of 140"; bladeren gaat via JavaScript (`_prev`/`_next`, geen paginalinks). Of "140" het hele
  koopaanbod is of alleen Jávea, is uit de HTML niet af te leiden **[te verifiëren]** — de sitemap zegt
  141 koop totaal en 68 in Jávea.
- Bekeken object: https://key2properties.es/property/4-bedroom-villa-for-sale-in-javea-ks3406
  (HTTP 200, 61 kB, 24-09-2026)
- **JSON-LD (schema.org): NEE** — geen `<script type="application/ld+json">`, geen microdata.
- **Open Graph: JA** — `og:title` "4 Bedroom Villa for Sale in Javea - KS3406", `og:description`,
  `og:type` "property", `og:url`, `og:image` (https://key2properties.es/images/w800_2037/D38668.jpg, 800×600).
  Ook Twitter-cards (`twitter:site` bevat per ongeluk de beschrijving), `meta description`, `meta keywords`
  ("Javea,Villa,Sale") en een `canonical`. Geen prijs in de meta-tags.
- De gegevens staan als gewone tekst in de HTML:
  - Titel: 4 Bedroom Villa for Sale in Javea · Ref: KS3406
  - Prijs: €1,999,950
  - Slaapkamers/badkamers: 4 / 3
  - Bouwoppervlak: 280 m² · Perceel: 1050 m² (labels "Plot Area", "Built Year", "Refuse Tax:" aanwezig)
  - Plaats: Jávea (titel en keywords); wijk/zone alleen eventueel in de vrije tekst, geen apart veld gezien
  - Blok "Similar properties in Javea" met vier extra objecten (bouw, perceel, prijs, ref)
- Talen: alleen Engels; vertaling via een Google Translate-widget (dus geen aparte NL/ES-URL's).

## 5. Systeem achter de site

- **Onbekend Java-platform, niet een van de bekende Spaanse makelaarssystemen.** Aanwijzingen:
  - Cookie `JSESSIONID` op elke respons (Java-servletcontainer).
  - Een weggelekte JSP-tag `<compress:html>` in de HTML (HtmlCompressor-taglib).
  - CSS/JS: `/res/5/rg.min.css`, `/res/5/rg.min.js`, `/combined.js?id=...`; attributen `data-rg`, klassen `rg_`
    en `rgi-` (iconen); paginabouwer met tijdstempelklassen zoals `._1758877009612`.
  - Beeldpaden `/images/w800_2037/...` en favicon `/images/2003-2037.png`: nummer 2037 lijkt een kantoor-ID,
    dus een gedeeld (multi-tenant) platform en geen eigen bouw van het kantoor.
  - Geen `generator`-meta, geen html-commentaar, geen "powered by". Geen sporen van Inmoweb, Mediaelx/LetsINMO,
    Sooprema, Inmovilla, Witei of WordPress.
- Of dit platform een exportfeed kent is onbekend; niet nodig, want lezen mag.

## 6. Schatting omvang en dekking

- **Ca. 141 koopobjecten** (sitemap 24-09-2026; de zoekpagina zegt 140), plus 83 huurobjecten.
- **Jávea/Benitachell/Moraira: 110 van 141 = ca. 78 %** (Jávea 68, Cumbre del Sol 26, Benitachell 13, Moraira 3).
  Zonder de 25 Cumbre del Sol-feedobjecten: 85 van 116 = ca. 73 % eigen aanbod in het doelgebied.
- Voor de Deal Hunter interessant: 22 percelen (de meeste in Jávea en Benitachell), 4 finca's en het
  Jávea-villa-aanbod; 30 feedobjecten ontdubbelen.

# HG Hamburg (Hanseatische Gesellschaft Hamburg S.L.) — toets op automatisch lezen

Datum: 24-09-2026 · Website: https://www.hg-hamburg.de · Opgehaald: 5 verzoeken (het maximum), telkens ≥ 2 seconden tussenruimte.

**Kantoor:** Calle Amedeo Modigliani 3, Jávea (bron: voettekst homepage, 24-09-2026). Tweede vestiging in Hamburg (Sierichstrasse 126, 22299 Hamburg). Algemeen contact: info@hg-hamburg.de, +34 96 646 84 02. Registratie RAICV 4277 (voettekst).
Werkgebied volgens de site: Jávea, Moraira, Altea, Benissa, Benitachell, Calpe, Dénia, Pedreguer (categoriepagina's in de sitemap).

## 1. robots.txt — toegestaan

Bron: https://www.hg-hamburg.de/robots.txt (HTTP 200, 24-09-2026).
`User-agent: *` mag de aanbodpagina's lezen. Alleen deze paden zijn uitgesloten (letterlijk):

```
User-agent: *
Disallow: /virtual/PrintProperty.aspx
Disallow: /virtual/PrintDevelopment.aspx
Disallow: /virtual/SmartLink.aspx
Disallow: /virtual/SmartLinkDetail.aspx
Disallow: /tel:
Disallow: */smartLink/*
Disallow: */gerir-dados-rgpd
Disallow: */rgpd-update
Disallow: /404  /500  /410  (ook onder /es-es/ en /en-gb/)
Disallow: /kaufguide-herunterladen
Disallow: /laden-sie-den-verkaufsleitfaden-herunter
Disallow: /startdpl
Disallow: /sie-haben-unseren-brief-erhalten
(+ Spaanse en Engelse tegenhangers: descargue-guia-de-compra/-venta, iniciodpl, ha-recibido-nuestra-carta, download-buyers-guide/-sellers-guide, homedpl, you-found-our-letter)
Sitemap: https://www.hg-hamburg.de/sitemap.xml
```

Conclusie: printversies, "smartlinks", AVG-formulieren, foutpagina's en downloadgidsen zijn dicht; `/unser-angebot` en `/immobilie/...` staan open.

## 2. Voorwaarden — tekst niet leesbaar zonder browser

Bron: https://www.hg-hamburg.de/terms-and-conditions ("Rechtlicher Hinweis", HTTP 200, 89 kB, 24-09-2026).
De opgehaalde HTML bevat alleen het sitegeraamte (menu, voettekst, nieuwsbriefformulier); de juridische tekst zelf wordt na het laden door JavaScript opgehaald bij `websiteapi.egorealestate.com/v1`. Er is dus **geen tekst gevonden** die scraping verbiedt of toestaat — er is überhaupt geen tekst gevonden. Dit hoort in een vervolgstap één keer met een renderende browser bekeken te worden (één pagina).
Links in de voettekst: `/terms-and-conditions`, `/privacy-policy`, `/cookie-policy`.

## 3. Sitemap — 151 objecten

- https://www.hg-hamburg.de/sitemap.xml = index met drie taalsitemaps (de-de, es-es, en-gb), lastmod 2026-09-24.
- https://www.hg-hamburg.de/sitemap-de-de.xml: 320 URL's, waarvan **151 onder `/immobilie/`** (objectpagina's) en 16 onder `/unser-angebot/` (categorieën per plaats en type). 127 URL's zijn nieuwsberichten. Objecten hebben geen lastmod.
- Objectpatroon: `https://www.hg-hamburg.de/immobilie/<slug>/<referentienummer>`, bijv. `/immobilie/villa-alenia-eleganz-und-luxus-in-strandnahe/19816026`.
- De Spaanse en Engelse sitemaps zijn niet opgehaald (limiet); dat zijn naar verwachting vertalingen van dezelfde 151 objecten.
- Type volgens slug: 135× villa, 20× "haus", 11× grundstück (bouwgrond), 4× finca, 1× apartment. De plaatsnaam staat maar bij 6 slugs (4× Jávea, 2× Moraira).

## 4. Objectpagina — niet geopend

Het maximum van vijf verzoeken was bereikt na robots.txt, sitemap-index, homepage, voorwaardenpagina en de Duitse sub-sitemap. Wat wél bekend is uit de homepage (24-09-2026):
- Drie `application/ld+json`-blokken: `RealEstateAgent` (naam, telefoon, e-mail, omschrijving) en 2× `Organization`. Geen productdata.
- og-tags aanwezig: og:site_name, og:type, og:title, og:url, og:image, og:description.
- Aandachtspunt: de voorwaardenpagina laadt inhoud via JavaScript; het is aannemelijk (niet gecontroleerd) dat objectpagina's dat ook doen. Vervolgstap: één objectpagina ophalen en kijken of prijs/oppervlakte/perceel/plaats/referentie in de kale HTML staan; zo niet, dan met een renderende browser.

Voorbeeld-URL voor die test: https://www.hg-hamburg.de/immobilie/villa-alenia-eleganz-und-luxus-in-strandnahe/19816026

## 5. Systeem — eGO Real Estate (Janela Digital)

Bewijs (24-09-2026):
- HTTP-headers: `x-served-by: JanelaDigital`, `x-pb: EGR`.
- Scripts/CSS/afbeeldingen van `static.egorealestate.com/egoforge/websiteeditor/...`, `media.egorealestate.com`, API `websiteapi.egorealestate.com/v1`; lokale paden `/DevGear/...`.
- Voettekst: "CRM and property websites by eGO Real Estate".
- robots.txt noemt ASP.NET-paden (`/virtual/PrintProperty.aspx`).
Dit is dus geen Inmoweb, Mediaelx, Sooprema, Inmovilla, Witei of WordPress, maar het Portugese platform eGO Real Estate. Dat platform kent portaalfeeds (te verifiëren bij het kantoor) — een alternatief als lezen later toch niet mag.

## 6. Omvang en dekking Jávea/Benitachell/Moraira

- Circa **151 objecten** (Duitse sitemap, 24-09-2026), overwegend villa's in het hogere segment (slogan "Exklusive Immobilien an der Costa Blanca Nord").
- Dekking: het kantoor zit in Jávea en de site voert "Jávea, Moraira & Altea" in de paginatitel. Categoriepagina's bestaan voor Jávea, Benitachell en Moraira, maar ook voor Altea, Benissa, Calpe, Dénia en Pedreguer. Het exacte aandeel per plaats staat niet in de sitemap; dat lees je van de categoriepagina's `/unser-angebot/javea--xabia`, `/unser-angebot/benitachell--el-poble-nou-de-benitatxell` en `/unser-angebot/moraira` (niet opgehaald).

## Advies: lezen (onder voorbehoud)

robots.txt staat het toe en de sitemap geeft alle objectpagina's kant-en-klaar. Twee dingen eerst nog doen, elk één pagina:
1. De "Rechtlicher Hinweis" in een renderende browser lezen — de tekst staat niet in de kale HTML.
2. Eén objectpagina testen op leesbaarheid (JSON-LD/og en of de kerngegevens in de HTML zitten).
Verbiedt de juridische tekst het alsnog, dan: feed vragen (eGO Real Estate levert portaalfeeds) of overslaan.

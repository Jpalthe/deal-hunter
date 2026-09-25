# Blanca International — toets op automatisch lezen

- **Opgegeven adres (K01/K02-lijst):** https://www.blancainternational.com — een WordPress-brochuresite
- **Het aanbod staat op een tweede domein:** https://www.blanca-properties.com (alle "Properties for sale"-links van de hoofdsite wijzen daarheen)
- **Datum toets:** 24-09-2026 (ca. 23:48–23:53 CEST)
- **Kantoor volgens de site:** Avenida Arenal 1, Local C, 03730 Jávea (voettekst homepage, 24-09-2026) · tel. +34 722 595 313 ·
  e-mail in de tekst weergegeven als "post(a)blancainternational.com" (in de HTML achter Cloudflare-e-mailbescherming).
  Zustersite voor autoverhuur: blancacars.com.
- **Opgehaalde pagina's (nooit sneller dan één per 2 s; op blanca-properties.com 14 s ertussen, zoals robots.txt vraagt):**
  - blancainternational.com (5): `/robots.txt`, `/sitemap.xml`, `/`, `/page-sitemap.xml`, `/terms-and-conditions/`
  - blanca-properties.com (3): `/robots.txt`, `/sitemap.xml`, `/en/for-sale/javea/relevant/`
  - Niet ingelogd, geen formulieren, niets omzeild. WebSearch was niet beschikbaar (sessiebudget van 200 zoekopdrachten was op).

## Samenvatting in gewone taal

De hoofdsite blancainternational.com mag van robots.txt volledig gelezen worden en de pagina "Terms and Conditions" bevat
alleen vultekst (Lorem ipsum), dus daar staat geen verbod. Maar op die site staan **geen woningen**: het is een
WordPress-brochuresite (thema Houzez) waarvan elke aanbodlink naar het aparte domein **blanca-properties.com** gaat.
Dat tweede domein staat lezen op papier ook toe (robots.txt: `Allow: /`, wel 14 seconden pauze en geen vervolgpagina's),
maar geeft aan een gewone lezer alleen een JavaScript-beveiligingspagina terug: "Verifying your browser — Powered by
Paagees Shield". Die controle mogen wij niet omzeilen, dus daar ben ik gestopt. Objectpagina's, prijzen en aantallen
zijn daardoor niet vastgesteld. Paagees is een weblaag die altijd op een bestaand CRM met XML-feed of API draait
(zie B01), dus het kantoor hééft al een feed. **Advies: feed vragen.**

## 1. robots.txt

### 1a. https://www.blancainternational.com/robots.txt
HTTP 200, `content-type: text/plain`, `server: cloudflare`, Last-Modified 24-03-2023, opgehaald 24-09-2026. Letterlijk:
```
User-agent: *
Allow: /
Sitemap: https://www.blancainternational.com/sitemap.xml
Sitemap: https://www.blancainternational.com/sitemap_index_0.xml
… (t/m sitemap_index_36.xml, 37 Sitemap-regels in totaal)
```
**Uitleg:** `User-agent: *` met alleen `Allow: /` — alles mag gelezen worden, ook de aanbodpagina's. Geen `Crawl-delay`.

### 1b. https://www.blanca-properties.com/robots.txt
HTTP 200, `server: Apache`, Last-Modified 07-01-2025, opgehaald 24-09-2026. Voor `User-agent: *` geldt, letterlijk:
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
Disallow: /*/*/*/stranitsa/*
Disallow: /*/*/*/siden/*
Disallow: /portal/proceso/secciones/
Disallow: /portal/proceso/newsletter/
Disallow: /giuliano/proceso/enviar/
Disallow: */html/galeriamodal/*
Disallow: */imprimir/*
Disallow: */print/*
Disallow: */drucken/*
Disallow: */imprimer/*
Disallow: */afdrukken/*
Allow: /
```
en helemaal onderaan een tweede blok:
```
User-agent: *
Crawl-delay: 14
```
Daartussen staan ruim 100 kopieerprogramma's met naam op `Disallow: /` (o.a. `Wget`, `Python-urllib`, `httplib`,
`HTTrack 3.0`, `WebZip`, `WebCopier`, `Offline Explorer`, `EmailCollector`).
**Uitleg:** de eerste pagina van elke aanbodlijst en de objectpagina's mogen gelezen worden; vervolgpagina's
(`/*/*/*/page/*` en de vertalingen daarvan), printversies, formulieren en de fotogalerij-modal niet; 14 seconden tussen
verzoeken. Geen `Sitemap:`-regel. Dit bestand is **woordelijk gelijk** aan de robots.txt van costablancajaveaproperties.com
(Giuliano Villas, zie `site-giuliano-villas.com.md`), inclusief de regel `/giuliano/proceso/enviar/` — dezelfde
webleverancier/hetzelfde sjabloon **[te verifiëren]**.

**Conclusie robots:** lezen is op beide domeinen toegestaan (op blanca-properties.com met beperkingen). Maar zie 4: de
server van blanca-properties.com laat een gewone lezer in de praktijk niet binnen.

## 2. Gebruiksvoorwaarden

- https://www.blancainternational.com/terms-and-conditions/ (HTTP 200, 24-09-2026): titel "Terms and Conditions", maar de
  inhoud bestaat uit tien alinea's **Lorem ipsum**-vultekst ("Lorem ipsum dolor sit amet, consectetur adipiscing elit…").
  Er staan dus geen echte voorwaarden, en dus ook geen verbod op automatisch lezen, kopiëren of scraping.
- https://www.blancainternational.com/privacy/ bestaat volgens de page-sitemap, maar is niet opgehaald (paginabudget van vijf
  was op). Op de homepage en de voorwaardenpagina staat geen link naar een privacy- of aviso-legal-pagina.
- Op blanca-properties.com kon geen voorwaardenpagina worden gezocht: elke HTML-pagina komt terug als beveiligingspagina (zie 4).

**Conclusie:** geen verbod gevonden ("nee"), met de kanttekening dat de privacypagina niet is gelezen en de voorwaarden
van het aanboddomein onbereikbaar waren.

## 3. Sitemap

- https://www.blancainternational.com/sitemap.xml (HTTP 200, `x-robots-tag: noindex, follow`, 24-09-2026): dynamisch gemaakt
  door "All in One SEO v4.7.3.1" (WordPress). Het is een index met **63 deelsitemaps**: `post-sitemap.xml`, `page-sitemap.xml`,
  `attachment-sitemap.xml` t/m `attachment-sitemap55.xml` (55 stuks, foto's), `houzez_agency-`, `houzez_agent-`,
  `houzez_partner-`, `houzez_invoice-sitemap.xml`, `post-archive-sitemap.xml`, `post_tag-sitemap.xml`.
  **Er is géén property-sitemap.** Aantal object-URL's in de sitemap: **0**.
- https://www.blancainternational.com/page-sitemap.xml (HTTP 200, 24-09-2026): **88 pagina-URL's**, waaronder tientallen
  ongebruikte Houzez-demopagina's (`/homepage-with-map/`, `/listing-with-video/`, `/membership-packages/`, `/paypal-ipn/`,
  `/stripe/`, `/typography/` …) en de echte pagina's `/javea/`, `/moraira/`, `/denia/`, `/costa-blanca-north/`, `/for-sale/`,
  `/for-rent/`, `/privacy/`, `/terms-and-conditions/`. Geen enkele URL met venta/property/inmueble/villa/apartamento/parcela
  als objectpagina.
- De 37 `sitemap_index_N.xml`-bestanden uit robots.txt (robots.txt dateert van maart 2023) zijn niet opgehaald (budget);
  vermoedelijk een restant van een vorige sitemap-opzet **[te verifiëren]**.
- https://www.blanca-properties.com/sitemap.xml (HTTP 200, 5.882 bytes, 24-09-2026): **geen sitemap** maar dezelfde
  beveiligingspagina als in 4 (byte-voor-byte identiek aan het antwoord op de aanbodpagina).

## 4. Aanbodpagina en objectpagina — gestopt bij de botcontrole

- Op de hoofdsite staan menu- en voettekstlinks "Properties for sale / Villas / Apartments / Townhouse / Finca / Plots" en
  per plaats (Javea, Benitachell, Benissa, Moraira, Denia, Altea). **Alle 32 aanbodlinks** op de homepage wijzen naar
  blanca-properties.com, bijvoorbeeld `https://www.blanca-properties.com/en/for-sale/javea/relevant/`,
  `/en/for-sale/benitachell/relevant/`, `/en/for-sale/moraira/relevant/`, `/en/for-sale/villa/relevant/`,
  `/en/for-sale/plot/relevant/`, `/en/for-sale/new-build/relevant/`. Op de WordPress-site zelf staat geen enkele
  `/property/…`-link; het blok "Latest Properties" op de voorwaardenpagina linkt ook naar blanca-properties.com.
- **Aanbodpagina Jávea:** `GET https://www.blanca-properties.com/en/for-sale/javea/relevant/` (24-09-2026, eigen User-Agent
  "TREE-DealHunter-check", 14 s na het vorige verzoek) → HTTP 200, `server: nginx`, `x-robots-tag: noindex, nofollow`,
  `cache-control: no-store`, 5.882 bytes. De inhoud is geen aanbod maar een pagina met `<title>Security Check</title>`,
  "Verifying your browser — This is an automatic security check. You will be redirected shortly." en onderaan
  "Powered by Paagees Shield". Het script laat de browser SHA-256-rekenwerk doen (moeilijkheid 5), zet daarna het cookie
  `__shield=…` (1 uur geldig) en herlaadt de pagina; zonder JavaScript en cookies: "JavaScript is required to access this site".
- Dit is botdetectie. Die wordt **niet omzeild** (geen browser nabootsen, geen challenge oplossen). Daarmee stopt de toets:
  **objectpagina niet geopend; JSON-LD en og-tags van objectpagina's onbekend; prijs, oppervlakte, perceel, plaats en
  referentie niet vastgesteld.**
- Ter informatie over de hoofdsite: de homepage heeft wel og-tags (`og:site_name="Blanca International | Luxury Property
  Specialist on Costa Blanca North"`, `og:type=article`, `og:title`, `og:description`, `og:url`) en één
  `<script type="application/ld+json" class="aioseo-schema">`, maar dat gaat over de site/organisatie, niet over woningen.

## 5. Systeem achter de site

- **blancainternational.com:** WordPress 6.6.9 (`<meta name="generator">`), thema **Houzez** + `houzez-child`
  (paden `wp-content/themes/houzez/…`; Redux 4.5.0), plugins Elementor + Elementor Pro, All in One SEO 4.7.3.1,
  Contact Form 7 (+ conditional fields, redirection), Revolution Slider 6.5.9, GTranslate, Site Kit by Google 1.138.0,
  Google Tag Manager; `wp-json`-API zichtbaar; achter **Cloudflare** (server-header, e-mailbescherming). Geen cookies bij
  onze verzoeken. De Houzez-woningfunctie wordt niet gebruikt (geen property-sitemap, geen objectlinks).
- **blanca-properties.com (het aanbod):** "Powered by Paagees Shield" + robots.txt identiek aan de Giuliano-site
  ("Mattis-Framework", zie `site-giuliano-villas.com.md`). Volgens `B01-crm-feeds.md` §2.3 (bron paagees.com, 16-09-2026)
  is **Paagees** (Dénia) geen CRM maar een weblaag die zich koppelt aan een bestaand CRM: Inmovilla, Inmoweb, Sooprema,
  Mobilia, Inmogesco, Inmotek, Witei, Casafari of "cualquier CRM con XML o API". Welk CRM Blanca International eronder
  draait is **onbekend [te verifiëren]** — het is dus geen van de vaste keuzes (Inmoweb/Mediaelx/Sooprema/Inmovilla/Witei)
  met zekerheid, en ook geen eigen bouw. Dezelfde Paagees-schermpagina zagen we eerder bij Villalux, Klaus Hildenbrand,
  AR Luxury Living, Hamiltons, Paradise, Crown en TerramaR (R06-verificatie A4, 15-09-2026).

## 6. Schatting aanbod en dekking Jávea/Benitachell/Moraira

- **Aantal objecten:** niet vast te stellen — de lijstpagina's zijn onbereikbaar (4) en de sitemap van de hoofdsite bevat
  geen objecten (3). Geen getal op de homepage gevonden. `geschat_aantal_objecten` blijft daarom leeg.
- **Dekking:** de site positioneert zich op Jávea (`<title>Luxury Villa and Apartments in Javea</title>`; omschrijving
  "luxury villas, apartments and townhouses in Javea and surrounding areas on the Costa Blanca North"; kantoor in het Arenal,
  Jávea) met aanbodlinks voor Jávea, Benitachell, Moraira, Benissa, Dénia en Altea. Het gidsprofiel in K02 noemt
  "aanbod Moraira, Benitachell, Benissa". Verwachting: **overwegend Jávea/Benitachell/Moraira**, aandeel niet te
  kwantificeren **[te verifiëren]**.

## Advies: FEED VRAGEN

- robots.txt staat lezen toe en er is geen verbod in voorwaarden gevonden, maar de aanbodpagina's zijn voor een
  automatische lezer **niet leesbaar** (Paagees Shield). Omzeilen doen we niet. Dagelijks pagina 1 lezen, zoals bij
  Giuliano, is hier dus niet mogelijk.
- Het systeem is een Paagees-weblaag op een CRM met XML/API-uitgang: de feed die blanca-properties.com voedt, bestaat al.
  De vraag aan het kantoor is niet "kunt u iets bouwen" maar "mag die feed ook naar ons".
- Zonder feed: alleen handmatig via de browser, of via portalen waar het kantoor adverteert (niet onderzocht).

⏸️ ACTIE VOOR JAN: Blanca International (Av. Arenal 1, Local C, Jávea; +34 722 595 313) benaderen met de vraag of de
CRM-feed achter blanca-properties.com (Paagees) ook aan TREE Deal Hunter geleverd kan worden — en daarbij vragen welk CRM
zij gebruiken. Zonder die afspraak valt dit kantoor buiten het automatische lezen.

## Bronnen

- https://www.blancainternational.com/robots.txt · 24-09-2026
- https://www.blancainternational.com/sitemap.xml · 24-09-2026
- https://www.blancainternational.com/ · 24-09-2026
- https://www.blancainternational.com/page-sitemap.xml · 24-09-2026
- https://www.blancainternational.com/terms-and-conditions/ · 24-09-2026
- https://www.blanca-properties.com/robots.txt · 24-09-2026
- https://www.blanca-properties.com/sitemap.xml · 24-09-2026 (Security Check)
- https://www.blanca-properties.com/en/for-sale/javea/relevant/ · 24-09-2026 (Security Check)
- `B01-crm-feeds.md` §2.3 (Paagees, bron paagees.com 16-09-2026); `R06-makelaars-javea-register.verificatie.md` A4;
  `site-giuliano-villas.com.md` (identieke robots.txt); `K01-kantoren-javea.json` regel 394; `K02-kantoren-benitachell-moraira.json` regel 348

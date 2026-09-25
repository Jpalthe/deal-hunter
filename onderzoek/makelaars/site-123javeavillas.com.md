# 123 Javea Villas — toets op automatisch lezen

- **Website:** https://www.123javeavillas.com
- **Datum toets:** 24-09-2026 (ca. 23:30 CEST)
- **Kantoor:** Avenida Marina Española 5, 03730 Jávea (haven) — bron: https://www.123javeavillas.com/legal-notice (24-09-2026)
- **Algemene contactkanalen:** info@123javeavillas.com · +34 865 824 482 — bron: voettekst van de site (24-09-2026)
- **Opgehaalde pagina's (5, steeds ≥ 2 s ertussen):** `/robots.txt`, `/`, `/sitemap.xml`, `/property/1880860-villa-for-sale-in-javea`, `/legal-notice`

## Advies: LEZEN

robots.txt staat alles toe, de voorwaarden verbieden automatisch lezen niet, en de objectpagina's zijn gewone
server-gerenderde HTML waar prijs, bouw- en perceeloppervlak en referentie leesbaar in staan. Wel drie spelregels:

1. Nooit sneller dan één pagina per twee seconden (641 objectpagina's = ca. 22 minuten voor een volledige ronde;
   daarna alleen de gewijzigde pagina's ophalen op basis van `lastmod` in de sitemap).
2. Foto's en beschrijvingen **niet overnemen of publiceren** — de voorwaarden verbieden reproductie/verspreiding
   zonder toestemming (zie punt 2). Intern lezen, vergelijken en scoren is wat anders dan overnemen.
3. Deep links in eigen rapporten zijn intern gebruik; de voorwaarden zeggen dat hyperlinks *naar buiten toe* alleen
   naar de hoofdpagina mogen (art. 6). Bij externe publicatie dus alleen naar de homepage linken.

## 1. robots.txt

- URL: https://www.123javeavillas.com/robots.txt (HTTP 200, 24-09-2026)
- Volledige inhoud (2 regels):

```
User-agent: *
Disallow:
```

- Een lege `Disallow:` betekent: **alles mag gelezen worden**, ook de aanbod- en objectpagina's.
  Geen `Crawl-delay`, geen `Sitemap:`-regel.

## 2. Gebruiksvoorwaarden

- Gevonden op https://www.123javeavillas.com/legal-notice ("Legal Notice", gedateerd 27/11/2025). Verder zijn er
  `/privacy-policy` en `/cookies-policy` (niet opgehaald, budget).
- De verantwoordelijke is een **natuurlijk persoon** (naam en NIF staan op de pagina; bewust niet overgenomen).
- **Geen expliciet verbod** op scraping, crawling, bots of automatisch lezen. De woorden scraping/crawl/robot/automat
  komen niet voor.
- Wel twee algemene auteursrechtbepalingen (citaten, Engels):
  - art. 3.1: "Not reproduce or distribute content without authorization."
  - art. 4: "Their reproduction, distribution or modification without express authorization is prohibited."
- art. 6 over hyperlinks: "The hyperlink may only direct to the main page of the Website."
- art. 3.2: de inhoud is informatief en het kantoor garandeert de juistheid of actualiteit niet.
- Conclusie: automatisch lezen is niet verboden; **overnemen** van teksten en foto's wel zonder toestemming.

## 3. Sitemap

- URL: https://www.123javeavillas.com/sitemap.xml (HTTP 200, 299 kB, 24-09-2026). Niet in robots.txt vermeld;
  gevonden op het standaardpad.
- **1.434 URL's** in totaal, waarvan:
  - **663** objectpagina's onder `/property/{id}-{slug}` (663 unieke ID's, één URL per object, geen taalvarianten)
    - 641 met "for-sale" in de slug → **te koop**
    - 15 huur (winter- en langetermijnverhuur, vrijwel allemaal Jávea)
    - 7 overig (1 villa "under construction" Jávea, 4 winter lets, 2 winkelpanden te huur in de haven)
  - 304 filterpagina's `/properties-for-sale/...` (plaats × type) en 304 `/properties-to-rent/...`
  - de rest: informatiepagina's in EN/ES/FR/NL (bijv. `/huiseigenaren`, `/verkoop`)
- `lastmod`: 1.232 van de 1.434 URL's zijn in 2026 bijgewerkt — de sitemap wordt dus onderhouden en is bruikbaar
  als wijzigingsdetector.

## 4. Objectpagina

- Aanbodpagina (uit de navigatie van de homepage):
  https://www.123javeavillas.com/properties-for-sale/location-javea/order-lowest-price
- Bekeken object: https://www.123javeavillas.com/property/1880860-villa-for-sale-in-javea (HTTP 200, 24-09-2026;
  `lastmod` in sitemap: 2025-12-12)
- **JSON-LD (schema.org): NEE** — geen `<script type="application/ld+json">`, ook geen microdata (`itemprop`).
- **Open Graph: beperkt** — alleen `og:image` (foto op cdn.advanceagent.co.uk). Verder `meta description` en
  `meta keywords`, beide gelijk aan de titel ("4 bedroom Villa for sale in Javea"). Geen `og:title`, `og:price`,
  canonical of hreflang.
- De gegevens staan als gewone tekst in de HTML (blok "Key Features"):
  - Titel: 4 bedroom Villa for sale in Javea
  - Prijs: €1,300,000
  - Slaapkamers/badkamers: 4 / 4
  - Bouwoppervlak: 391 m² · Perceel: 1414 m² · Zwembad: ja
  - Referentie: 679501 (kantoorreferentie; het getal in de URL, 1880860, is het CMS-ID)
  - Plaats: Jávea; wijk alleen in de vrije tekst ("Valsol area, Javea") — er is **geen apart wijkveld**
  - Let op: de beschrijving noemt een verwachte oplevering "summer of 2024" — de tekst is dus verouderd
    (vandaag 24-09-2026). Sluit aan bij art. 3.2: geen garantie op actualiteit. Bij scoren: datum in de tekst
    meewegen.
- Er staat een blok "Similar Properties" onder het object; handig voor kruisverwijzingen, niet nodig voor de feed.

## 5. Systeem achter de site: Advance Agent (niet in de standaardlijst)

Bewijs (24-09-2026):
- Voettekst: "Powered by Advance Agent - Estate Agency Software" met link naar advanceagent.co.uk
- CSS/JS-paden: `/stylesheets/advanceagent.min.css`, `/javascripts/advanceagent.cookies.js`
- Sessiecookie: `_advance_agent_session` (HttpOnly)
- Foto's op `cdn.advanceagent.co.uk/...`
- Serverkoppen: `Server: nginx`, `X-Powered-By: Phusion Passenger`, `X-NodeId: app02/app03` (gedeeld platform,
  meerdere app-servers; Passenger wijst op Ruby on Rails)
- Front-end: Bootstrap 3 + jQuery 1.11.1, AddThis, Google Analytics — oudere maar stabiele opzet

Het is dus **geen** Inmoweb, Mediaelx, Sooprema, Inmovilla, Witei of WordPress, maar het Britse Advance Agent
(veel gebruikt door Engelstalige kantoren aan de Costa Blanca). Of Advance Agent een exportfeed voor derden kent
[te verifiëren] — voor dit advies niet nodig, want lezen mag.

## 6. Omvang en dekking Jávea / Benitachell / Moraira

Geteld op de plaatsnaam in de URL-slug van de 641 te-koop-objecten in de sitemap (24-09-2026):

| Plaats | Objecten | Aandeel |
|---|---|---|
| Jávea (incl. 4× "arenal" zonder plaatsnaam) | 307 | 48 % |
| Moraira | 40 | 6 % |
| Benitachell | 19 | 3 % |
| **Subtotaal doelgebied** | **366** | **57 %** |
| Calpe | 65 | 10 % |
| Dénia | 43 | 7 % |
| Benissa | 29 | 5 % |
| Pedreguer | 22 | 3 % |
| Altea | 16 | 2 % |
| Finestrat / La Nucía / Villajoyosa / El Verger / Polop e.a. (Marina Baixa, zuidelijker) | ca. 80 | 12 % |
| Overig (Lliber, Gata, Orba, Teulada, Oliva, Pego, Sevilla, Alzira …) | ca. 20 | 3 % |

- Geschatte omvang: **ca. 640 objecten te koop**, waarvan **ca. 365 (57 %) in Jávea, Benitachell of Moraira**.
- Type (slug): villa 361 · appartement 188 · house 53 · penthouse 31 · townhouse 21 · **perceel 16** · finca 8.
- Kanttekening: de aanwezigheid van objecten in Finestrat, La Nucía, Sevilla en Alzira plus een pagina
  `/properties-for-sale/tag-agents` en een voetlink "Agents" wijst erop dat een deel van het aanbod van
  **samenwerkende kantoren** komt en dus ook elders zichtbaar kan zijn [te verifiëren]. Voor Deal Hunter tellen
  vooral de 16 percelen en de 300+ Jávea-objecten.
- Nuttige filterpagina's op de homepage: "Bank Repossessions Javea"
  (`/properties-for-sale/location-4-javea/type-villa/tag-bank-repossession/order-lowest-price`) en
  "Bargain" (`/properties-for-sale/location-javea/type-villa/tag-bargain/order-lowest-price`) — precies de hoek
  waar Deal Hunter naar zoekt. Niet opgehaald (budget); wel via de sitemap/homepage geverifieerd dat ze bestaan.

## Aanbevolen leesstrategie

1. Eén keer per dag `/sitemap.xml` lezen (1 verzoek). Nieuwe of gewijzigde `/property/`-URL's bepalen via `lastmod`.
2. Alleen die pagina's ophalen, 1 per 2 s, met een herkenbare User-Agent en contactadres.
3. Velden uit de HTML: titel, prijs (`€1,300,000`-notatie), bouw m², perceel m², slaap-/badkamers, referentie,
   plaats (uit slug/titel), wijk uit de vrije tekst. Geen JSON-LD beschikbaar, dus een eigen parser op het
   "Key Features"-blok.
4. Foto's niet downloaden; alleen de URL van `og:image` bewaren als verwijzing.

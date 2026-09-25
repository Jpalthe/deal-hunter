# Promociones Jávea — toets op automatisch lezen

- **Website:** https://www.promocionesjavea.com
- **Datum toets:** 24-09-2026
- **Kantoor (uit de schema.org-gegevens op de site):** Avda. Pla 124, local 15, 03730 Jávea; tel. 965 79 27 69
  (bron: JSON-LD `RealEstateAgent` op https://www.promocionesjavea.com, 24-09-2026)
- **Opgehaald:** 6 verzoeken, met minimaal 2 seconden ertussen: robots.txt, sitemap.xml (index), sitemap-es-es.xml,
  de homepage, /terminos-y-condiciones en één objectpagina. De aanbodpagina /comprar is niet apart geopend
  (draait op hetzelfde systeem als de objectpagina en zou de zesde HTML-pagina zijn geweest).

## 1. robots.txt — toegestaan

Bron: https://www.promocionesjavea.com/robots.txt (24-09-2026, HTTP 200). Voor `User-agent: *` zijn alleen
print-, deel- en foutpagina's uitgesloten; de aanbod- en objectpagina's (`/comprar`, `/inmuebles/...`,
`/inmueble/...`) staan nergens op Disallow. Relevante regels, letterlijk:

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
Disallow: /404
Disallow: /500
(idem /en-gb, /fr-fr, /de-de, /nl-nl voor 404 en 500)
Sitemap: https://www.promocionesjavea.com/sitemap.xml
```

Geen Crawl-delay, geen aparte regels voor specifieke bots.

## 2. Gebruiksvoorwaarden — niet gevonden (pagina is leeg zonder JavaScript)

De footer linkt "Aviso Legal" naar https://www.promocionesjavea.com/terminos-y-condiciones (naast
/politica-de-privacidad en /politica-de-cookies). Die pagina opgehaald op 24-09-2026 (HTTP 200, 79 kB): de HTML
bevat alleen het menu, de footer en de cookiebalk; de juridische tekst zelf staat niet in de HTML. De link heeft de
class `rgpd-update terms-and-conditions`, wat erop wijst dat de tekst door JavaScript uit het eGO-platform wordt
geladen. In de opgehaalde HTML komt geen enkele vermelding voor van scraping, robots, automatisch lezen, databank of
"uso no autorizado". **Conclusie: er is geen verbod gevonden, maar de voorwaarden zijn ook niet echt gelezen.**
Wie de tekst wil zien, moet de pagina in een browser openen (met JavaScript) — dat is niet gedaan om binnen het
maximum aantal opvragingen te blijven.

## 3. Sitemap — 37 objecten in de Spaanse sitemap

- https://www.promocionesjavea.com/sitemap.xml is een index met vijf taalsitemaps (es-es, en-gb, fr-fr, de-de, nl-nl).
- https://www.promocionesjavea.com/sitemap-es-es.xml (24-09-2026): 77 URL's in totaal, waarvan **37 objectpagina's**
  (`/inmueble/<slug>/<nummer>`). De andere taalsitemaps zijn niet opgehaald; volgens de hreflang-tags op de objectpagina
  bestaat elk object ook in en-gb (`/property/`), fr-fr (`/bien-immobilier/`), de-de (`/immobilie/`) en nl-nl (`/woning/`),
  dus die bevatten vermoedelijk dezelfde 37 objecten [te verifiëren].
- Verder in de sitemap: locatiepagina's `/inmuebles/altea`, `/benissa`, `/denia`, `/javea--xabia`, `/moraira`,
  `/pedreguer`, `/sector-1`, `/sector-6` en typepagina's (apartamento, chalet, duplex, atico, pareado, vivienda-adosada, villa).
- Aanbodpagina: https://www.promocionesjavea.com/comprar (huur: /alquiler; nieuwbouw: /obra-nueva).

## 4. Objectpagina — JSON-LD en og-tags aanwezig, maar de details staan niet in de HTML

Geopend: https://www.promocionesjavea.com/inmueble/exclusiva-villa-de-obra-nueva-con-piscina-en-javea/24884367
(24-09-2026, HTTP 200, 103 kB).

**`<script type="application/ld+json">`** — drie blokken:
1. `BreadcrumbList`: Viviendas/Casas > Venta > **Jávea / Xàbia** > **Cap Martí - El Tossalet - Pinomar** > object.
   De plaats en de wijk zijn dus uit de broodkruimels te halen.
2. `RealEstateAgent`: bedrijfsgegevens van het kantoor (naam, adres, openingstijden, telefoon).
3. `RealEstateListing`: `name`, `url`, `description`, `image`, en `offers` met **`price: 1090000`, `priceCurrency: EUR`**,
   `businessFunction: Sell`. Geen veld voor woonoppervlak, perceel of referentie; in de beschrijvingstekst staat wel
   "269,71 m² construidos", "terrazas de casi 220 m²", "piscina privada de 35 m²", 4 slaapkamers, 3 badkamers.

**og-tags:** `og:title`, `og:description` (zelfde beschrijving), `og:image` (foto op images.egorealestate.com),
`og:url`, `og:type=website`, `og:locale=ES_ES`, `og:site_name`.

**Wat er níet in de HTML staat:** de zichtbare pagina-inhoud (prijsblok, kenmerkentabel, referentie, perceel, kaart)
wordt pas in de browser opgebouwd. De HTML zonder JavaScript bevat alleen menu, footer en cookiebalk (ca. 1.200
tekens tekst); de objectgegevens komen via `Websiteapi.egorealestate.com/v1` (JavaScript, met een in de pagina
ingebakken API-sleutel — die gebruiken we niet, dat zou omzeilen zijn). Een **referentienummer** is alleen het
nummer in de URL (24884367, het eGO-objectnummer); **perceeloppervlak** is zonder JavaScript niet te lezen.

Samengevat per gevraagd veld: prijs **ja** (JSON-LD), woonoppervlak **alleen in de beschrijvingstekst**, perceel **nee**,
plaats **ja** (broodkruimels), referentie **alleen het URL-nummer**.

## 5. Systeem achter de site — eGO Real Estate (Janela Digital), niet op de lijst

Aanwijzingen (alle op 24-09-2026):
- HTTP-header `x-served-by: JanelaDigital` op elke opvraging (robots.txt, sitemap, homepage, objectpagina).
- HTML-commentaar `<!-- 18612-3 | WebsiteBuilder -->` bovenaan elke pagina.
- CSS/JS geladen van `https://admin.egorealestate.com/egocore/WebsiteBuilder/...`
  (liveBase.min.css, website.realestates.min.js, dataApi.realestates.min.js, handlebars).
- Footer: "CRM y páginas inmobiliarias por eGO Real Estate".
- Foto's op `images.egorealestate.com` / `media.egorealestate.com`; de robots.txt noemt Portugese paden (`gerir-dados-rgpd`)
  en `.aspx`-bestanden, typisch voor dit Portugese platform.

Dit is dus geen Inmoweb, Mediaelx, Sooprema, Inmovilla, Witei of WordPress. eGO Real Estate is een CRM met
websitebouwer; het platform kent koppelingen naar portalen (feeds naar o.a. Idealista) [te verifiëren], dus een
exportfeed vragen is in principe mogelijk als dat later nodig blijkt.

## 6. Omvang en dekking

- **Geschat aanbod: 37 objecten** (Spaanse sitemap, 24-09-2026), koop en huur samen; de sitemap maakt dat onderscheid niet.
- **Jávea/Benitachell/Moraira:** afgeleid uit de URL-slugs (niet uit de objectpagina's zelf, want die zijn niet allemaal
  geopend):
  - 16 slugs noemen Jávea of een Jávea-wijk expliciet (Arenal, Tosalet/Cumbres del Tosalet, Granadella, Ambolo, Canal de
    la Fontana, Montgó, Balcón al Mar, Golden Gardens, Puerto de Jávea).
  - 3 liggen aantoonbaar elders: Dénia (1), La Sella (1), Dubai Islands (1).
  - 18 slugs zijn alleen een villanaam (Villa Veritas, Villa Aralar, Villa Mariola, Villa Aitana, Point East, Bellevue, ...);
    een deel daarvan hoort vermoedelijk bij de eigen nieuwbouw "Villas Cumbres del Tosalet" in Jávea (de slug van Villa
    Talaia zegt dat letterlijk), en "Mercedes-Benz Places" is vermoedelijk ook Dubai [te verifiëren].
  - Er is een locatiepagina voor Moraira, dus mogelijk staat daar één of meer objecten; niets voor Benitachell gezien.
  - **Schatting: ruwweg 16 tot 30 van de 37 in Jávea; ten minste 3 daarbuiten.** De broodkruimels in de JSON-LD van elke
    objectpagina geven de exacte plaats — daarmee is dit bij het inlezen precies vast te stellen.
- Bijzonderheid: dit is primair een **projectontwikkelaar/bouwer** (sinds 1984, eigen nieuwbouw zoals Residencial Cumbres del
  Tosalet, Golden Ray, Beach Trade Center) met daarnaast makelaardij. Voor Deal Hunter is vooral hun eigen nieuwbouw en
  eventuele percelen interessant; renovatieobjecten zijn er vermoedelijk weinig.

## Advies: lezen

robots.txt staat het toe, er is geen verbod in voorwaarden gevonden (maar die zijn niet leesbaar zonder JavaScript), en
de objectpagina's zijn met de sitemap volledig te vinden. Praktisch: haal per object de HTML op en lees de JSON-LD
(`RealEstateListing` voor prijs en beschrijving, `BreadcrumbList` voor plaats en wijk). Voor perceel, referentie en de
kenmerkentabel is een browser met JavaScript nodig, of anders een exportfeed vragen bij het kantoor (eGO kan dat
vermoedelijk leveren [te verifiëren]). Niet doen: de ingebakken API-sleutel van het eGO-platform gebruiken.
Tempo: niet sneller dan één pagina per twee seconden; met 37 objecten is een volledige leesbeurt ca. 2 minuten.

⏸️ ACTIE VOOR JAN: als je zeker wilt zijn over de voorwaarden, open dan
https://www.promocionesjavea.com/terminos-y-condiciones in een gewone browser en kijk of daar iets over automatisch
lezen staat. Zo niet, dan kan het kantoor op de leeslijst.

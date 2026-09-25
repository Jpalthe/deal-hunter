# EuroJavea Inmobiliaria — toets op automatisch lezen

Datum: 24-09-2026 · Website: https://www.eurojavea.com · Onderzoek voor TREE Deal Hunter

**Kort:** de site is technisch prima leesbaar (schone URL's, JSON-LD met prijs en referentie,
og-tags), en robots.txt staat het toe. Maar de gebruiksvoorwaarden verbieden extractie,
hergebruik en commercieel/professioneel gebruik van de inhoud. Daarom **niet scrapen** en
in plaats daarvan het kantoor om een feed of samenwerking vragen.

**Advies: feed vragen.**

## Bedrijfsgegevens (uit de legal notice)

- Eigenaar site: EUROJAVEA, S.L. (CIF B53282257)
- Kantoor: Plaça President Adolfo Suárez 9, 03730 Xàbia (Alicante)
- Algemeen: tel. 965 794 290 · contacto@eurojavea.com
- Bron: https://www.eurojavea.com/legal-notice (opgehaald 24-09-2026, Thu, 24 Sep 2026 21:12:09 GMT)

## 1. robots.txt — staat lezen toe

Bron: https://www.eurojavea.com/robots.txt (opgehaald 24-09-2026 21:08 UTC; bestand
gedateerd 01-06-2023). Volledige inhoud:

```
User-agent: *
Disallow: /wp-admin/
Disallow: /*=*
Disallow: /*?*
Disallow: /*&*
Sitemap: https://www.eurojavea.com/sitemap/sitemap.xml.gz
Sitemap: https://www.eurojavea.com/sitemap_index.xml
```

Uitleg: elke robot (`User-agent: *`) mag alles lezen behalve de beheeromgeving en URL's
met een vraagteken, `=` of `&` (zoekfilters, paginering). De aanbodpagina's en
objectpagina's hebben schone URL's zonder parameters en vallen dus **niet** onder een
verbod. Oordeel: **toegestaan**.

## 2. Gebruiksvoorwaarden — verbieden extractie en commercieel gebruik

Bron: https://www.eurojavea.com/legal-notice ("Condiciones generales de uso de
www.eurojavea.com", Spaanstalig; opgehaald 24-09-2026, Thu, 24 Sep 2026 21:12:09 GMT).

De woorden "scraping", "robot" of "automatisch" komen er niet in voor, maar artikel 4
(Derechos de propiedad intelectual e industrial) dekt het wel. Letterlijke citaten:

> "La Persona Usuaria únicamente podrá acceder, visualizar y utilizar los Contenidos para su
> uso personal y privado, quedando prohibida su utilización con fines comerciales o
> profesionales, así como su modificación, copia, alteración, reproducción, adaptación o
> traducción, total o parcial, sin la autorización expresa de los titulares de dichos derechos."

> "...quedando expresamente prohibidos a la Persona Usuaria la reproducción, transformación,
> distribución, comunicación pública, puesta a disposición, **extracción, reutilización**,
> reenvío o la utilización de cualquier naturaleza, por cualquier medio o procedimiento, de
> cualquiera de ellos, salvo en los casos en que esté legalmente permitido o sea autorizado
> por el titular de los correspondientes derechos."

Onder "Contenidos" vallen uitdrukkelijk ook "bases de datos" (art. 4, eerste alinea). Artikel
3.1 verbiedt daarnaast het "reproducir, copiar, distribuir ... los contenidos de la Web sin la
autorización expresa del titular". Artikel 7 kondigt juridische stappen aan bij overtreding.

In gewone taal: alleen persoonlijk en privé gebruik; automatisch uitlezen van het aanbod
voor een commercieel doel (deal hunting voor TREE) is zonder schriftelijke toestemming
verboden. Oordeel: **verboden**, tenzij EuroJavea toestemming geeft.

## 3. Sitemap — 204 objecten

De Yoast-sitemap-index (https://www.eurojavea.com/sitemap_index.xml, opgehaald 24-09-2026
21:08 UTC) bevat alleen posts, pagina's, testimonials, "javea" en categorieën — geen
woningen. Het aanbod zit in de tweede sitemap uit robots.txt:

- https://www.eurojavea.com/sitemap/sitemap.xml.gz → verwijst naar
- https://www.eurojavea.com/sitemap/sitemap-search-1.xml.gz (opgehaald 24-09-2026 21:10 UTC,
  bestand gedateerd 24-09-2026 01:30 — wordt dus dagelijks vernieuwd)

Inhoud: 3.105 URL's in vier talen (EN zonder prefix, /es/, /fr/, /nl/), waarvan 789 Engelse.
Het grootste deel zijn filterpagina's (plaats → wijk → type, bijv.
/properties/javea/puerto/villa). Echte objectpagina's eindigen op een referentie
(EJV-1519, Eja-960 enz.):

| | aantal |
|---|---|
| Objectpagina's (EN, uniek) | **204** (in elke taal hetzelfde aantal) |
| waarvan referentie EJV (villa's) | 135 |
| waarvan EJP (percelen) | 36 |
| waarvan EJA (appartementen) | 30 |
| overig (EJG, EJL) | 3 |
| Sitemap-URL's met "villa" in het pad | 1.484 (alle talen, incl. filterpagina's) |
| met "parcela" | 100 · "apartamento" 101 · "chalet" 251 · "piso" 65 · "terreno" 66 · "finca" 56 |

De trefwoorden "venta", "property" en "inmueble" komen niet voor (de site gebruikt
/properties, /es/propiedades, /nl/eigenschappen). "javea" staat in vrijwel elke URL omdat
het domein zelf zo heet — daarom is per padsegment geteld, niet op het hele adres.

## 4. Aanbodpagina en één objectpagina

- Aanbodpagina (uit sitemap en broodkruimel "All properties for sale"):
  https://www.eurojavea.com/properties — niet apart geopend (budget).
- Geopende objectpagina: https://www.eurojavea.com/properties/javea/costa-nova/villas/EJV-1519
  (opgehaald 24-09-2026, Thu, 24 Sep 2026 21:11:23 GMT; HTTP 200, 113 kB, geen cookies gezet).

**JSON-LD** (`<script type="application/ld+json">`): ja, twee blokken.
1. `Product`: name "Villa Gafarro with Panoramic Views of Montgó in Costa Nova",
   sku/productId **EJV-1519**, offers.price **1250000 EUR**, availability InStock,
   priceValidUntil 2026-12-24, image via media.inmobalia.com.
   Let op: het `brand`-deel bevat demo-gegevens van de plugin-leverancier (dev11.inmoba.com,
   adres in Estepona, coördinaten bij Estepona, telefoon 123456789). Dat is een
   configuratiefout aan hun kant; de geo-gegevens in de JSON-LD zijn dus onbruikbaar.
2. `BreadcrumbList`: All properties for sale → Jávea → Costa Nova → Villas → Villa → EJV-1519.

Oppervlakte en perceel staan **niet** in de JSON-LD, wel in de pagina-tekst:
prijs 1.250.000 €, 4 slaapkamers, 3 badkamers, perceel 1.704 m², bebouwd 221 m²,
plaats Jávea / wijk Costa Nova, referentie EJV-1519.

**og-tags**: ja — og:locale en_GB, og:title, og:description, og:url, og:site_name
"Euro Javea Real Estate", og:image (media.inmobalia.com), twitter:card summary_large_image.
Geen prijs in de og-tags.

## 5. Systeem: WordPress + Inmoba-plugin (data uit Inmobalia)

Aanwijzingen op de objectpagina (24-09-2026):
- Thema-pad `wp-content/themes/inmobasolidbase/` (22×) en `/wp-admin/` in robots.txt → WordPress.
- Voettekst "· Built by Inmoba" met link naar www.inmoba.com; JSON-LD noemt
  "Inmoba Plugin Web" / "Inmoba SolidBase".
- Alle foto's komen van `media.inmobalia.com/imgV1/...` → het aanbod wordt gevoed vanuit het
  Inmobalia-CRM.
- Sitemap-index is van Yoast SEO (main-sitemap.xsl); het aanbod zit in een aparte,
  door de plugin gegenereerde `/sitemap/sitemap-search-N.xml.gz`.
- Geen "generator"-meta, geen html-commentaar, geen cookies bij een kale GET.
- Tracking: Google Tag Manager en Meta Pixel op de pagina's.

Dus: **niet** Inmoweb, Mediaelx, Sooprema, Inmovilla of Witei, maar WordPress met de
Inmoba-plugin bovenop Inmobalia. Inmobalia is een CRM waarin makelaars hun aanbod beheren en
delen; of en hoe EuroJavea daaruit een XML-feed kan aanzetten, is **[te verifiëren]** — dat
moet aan het kantoor gevraagd worden.

## 6. Omvang en dekking Jávea/Benitachell/Moraira

Telling op de 204 Engelse objectpagina's in de sitemap (24-09-2026), per plaats in het pad:

| Plaats | objecten |
|---|---|
| Jávea | 173 (85 %) |
| Dénia | 13 |
| Teulada/Moraira | 7 (waarvan 5 met "moraira" in het pad) |
| Benissa | 3 |
| Benitachell | 2 |
| overig (Pedreguer, Gata, Calpe, Benicasim, Beniarbeig, Altea) | 6 |

Jávea + Benitachell + Moraira samen: circa **180 van 204 objecten (≈ 88 %)**. De sitemap
noemt ook 1 project onder /developments (Jávea pueblo). Kanttekening: dit telt wat in de
sitemap staat; verkochte of verborgen objecten zie je hier niet.

Opvallend voor Deal Hunter: de navigatie heeft een pagina **"Secret sales"**
(https://www.eurojavea.com/secret-sales) — mogelijk stil aanbod. Niet geopend; handmatig
bekijken loont.

## Advies en vervolg

**Feed vragen.** Robots.txt en de techniek maken lezen makkelijk, maar de voorwaarden verbieden
extractie en commercieel gebruik uitdrukkelijk. Het kantoor zit op 200 meter van het
gemeentehuis van Xàbia; een rechtstreekse vraag om samenwerking (gedeeld aanbod / XML-feed
uit Inmobalia, of gewoon een wekelijkse lijst per mail) is de nette en snelste weg.

⏸️ ACTIE VOOR JAN
- Beslissen of TREE EuroJavea benadert voor samenwerking of een feed (contacto@eurojavea.com,
  965 794 290). Zonder hun toestemming dit aanbod niet automatisch uitlezen.
- Eventueel zelf de pagina "Secret sales" bekijken.

## Verantwoording

- Verzoeken aan de site: 6 in totaal, elk ≥ 2 seconden na de vorige, met herkenbare
  user-agent: robots.txt, sitemap_index.xml, sitemap/sitemap.xml.gz,
  sitemap/sitemap-search-1.xml.gz (4 machinebestanden) en 2 HTML-pagina's (één objectpagina,
  de legal notice). Homepage en aanbodpagina zijn niet geopend.
- Niet ingelogd, geen formulieren, niets omzeild.
- Zoekmachines konden niet worden gebruikt (zoekbudget van de sessie was op); alles komt van de
  site zelf.
- Persoonsgegevens (namen, mobiele nummers) zijn bewust weggelaten.

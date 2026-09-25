# Spainlife and Houses — toets op automatisch lezen

**Datum controle:** 24-09-2026 (ca. 21:41–21:43 uur, 4 pagina's opgehaald, 1 per ±2 s)
**Website:** https://www.spainlifeandhouses.es
**Bedrijf (uit het aviso legal):** Spainlife and Houses, S.L. — kantoor Canal Sur 1, Local 1A, 03730 Jávea (Alicante); tel. 865 510 883; info@spainlifeandhouses.com
Bron: https://www.spainlifeandhouses.es/aviso-legal (24-09-2026)

## Conclusie in één zin

Technisch is het aanbod goed leesbaar (objectpagina's staan niet in robots.txt en staan netjes in een sitemap), maar de **gebruiksvoorwaarden verbieden extractie en hergebruik voor commerciële/professionele doeleinden**. Het systeem (eGO Real Estate) kan aanbod naar portalen exporteren, dus: **advies "feed vragen"** — niet zelf scrapen.

## 1. robots.txt — gedeeltelijk toegestaan

Bron: https://www.spainlifeandhouses.es/robots.txt (24-09-2026, HTTP 200)

Er is één blok `User-agent: *`. Het verbiedt vooral de **zoek-/filterpagina's**, printversies en hulppagina's; de **individuele objectpagina's** (`/realestate-details/...`) en de categoriepagina's (`/realestate/<plaats of type>`) staan er **niet** in en zijn dus toegestaan.

Relevante regels (letterlijk):

```
User-agent: *
Disallow: /virtual/PrintProperty.aspx
Disallow: /virtual/PrintDevelopment.aspx
Disallow: /busqueda-de-inmuebles
Disallow: /compare
Disallow: /busco-un-inmueble
Disallow: /busqueda-de-promociones
Disallow: /galeria
Disallow: /en-gb/property-search
Disallow: /nl-nl/zoeken-in-ons-aanbod
Disallow: /nl-nl/bekijke-nieuwbouw
...
Sitemap: https://www.spainlifeandhouses.es/sitemap.xml
```

(Zelfde patroon herhaald voor fr-fr, de-de, pl-pl, cs-cz, sk-sk, uk-ua, ru-ru.)

**Gevolg:** een automatische lezer mag de zoekresultatenpagina's niet gebruiken, maar mag wél via de sitemap rechtstreeks naar de objectpagina's. Oordeel: **deels**.

## 2. Gebruiksvoorwaarden — verbieden extractie/hergebruik voor commercieel gebruik

Bron: https://www.spainlifeandhouses.es/aviso-legal (24-09-2026). De pagina bevat de "Condiciones Generales de Uso". Let op: de tekst noemt het domein `www.spainlifeandhouses.com`, terwijl de site op `.es` draait.

Relevante passages (Spaans, letterlijk):

- Art. 4: "quedando expresamente prohibidos al Usuario la reproducción, transformación, distribución, comunicación pública, puesta a disposición, **extracción, reutilización**, reenvío o la utilización de cualquier naturaleza, por cualquier medio o procedimiento, de cualquiera de ellos, salvo en los casos en que esté legalmente permitido o sea autorizado por el titular"
- Art. 4: "El Usuario podrá visualizar y obtener una copia privada temporal de los Contenidos para su exclusivo uso personal y privado (...) **siempre que no sea con la finalidad de desarrollar actividades de carácter comercial o profesional**."
- Art. 4: "El Usuario deberá abstenerse de obtener, o intentar obtener, los Contenidos por medios o procedimientos distintos de los que en cada caso se hayan puesto a su disposición (...) o de los que se utilicen habitualmente en Internet"

In gewone taal: kopiëren, uittrekken en hergebruiken van de inhoud is verboden zonder toestemming; een kopie mag alleen voor privégebruik, uitdrukkelijk niet voor zakelijke doeleinden. Het woord "scraping" komt niet voor, maar "extracción" en "reutilización" dekken precies wat een deal-hunter doet. Oordeel: **ja, verboden** (voor ons doel).

Omdat de opdracht zegt "stop zodra iets niet mag", is hierna **geen objectpagina geopend**.

## 3. Sitemap — 238 object-achtige URL's

Bron: https://www.spainlifeandhouses.es/sitemap.xml (24-09-2026) → sitemap-index met 10 taalversies (es-es, en-gb, fr-fr, de-de, nl-nl, pl-pl, cs-cz, sk-sk, uk-ua, ru-ru), alle `lastmod 2026-09-24T04:52:25+01:00` (dagelijks bijgewerkt).

Spaanse deelsitemap https://www.spainlifeandhouses.es/sitemap-es-es.xml: **325 URL's**, waarvan:

| Soort | Aantal | Patroon |
|---|---|---|
| Objectpagina's (unieke ID's) | **220** | `/realestate-details/<slug>/<id>` |
| Nieuwbouwprojecten (unieke ID's) | **18** | `/newbuild-details/<slug>/<id>` |
| Categoriepagina's plaats/type | 60 | `/realestate/<plaats>` of `/realestate/<type>` |
| Overig (over ons, contact, legal, agentpagina's) | 27 | |

Het aanbod is per taal hetzelfde (zelfde ID's), dus 220 + 18 = **238** te tellen objecten.

## 4. Objectpagina — niet geopend

Bewust overgeslagen wegens de voorwaarden (zie 2). Wat wél bekend is uit de al opgehaalde legal-pagina (zelfde sjabloon): de site zet **Open Graph-tags** (`og:site_name`, `og:type`, `og:title`, `og:url`, `og:image`, `og:description`); op die pagina stond **geen** `application/ld+json`. Of objectpagina's JSON-LD hebben: **onbekend**.

Voorbeeld-object-URL uit de sitemap (niet geopend):
https://www.spainlifeandhouses.es/realestate-details/villa-en-construccion-a-la-venta-en-javea/22125333

Vermoedelijke aanbodpagina uit de sitemap (niet geopend): https://www.spainlifeandhouses.es/inmuebles

## 5. Systeem: eGO Real Estate (Janela Digital)

Niet een van de "bekende" Spaanse systemen, maar het Portugese **eGO Real Estate** (CRM + websites) van Janela Digital. Bewijs (24-09-2026):

- HTTP-headers op elke pagina: `x-served-by: JanelaDigital`, `x-pb: EGR`
- Footer: "CRM y páginas inmobiliarias por eGO Real Estate" met link naar https://www.egorealestate.es/
- Scripts/CSS van `https://static.egorealestate.com/egoforge/websiteeditor/...` (o.a. `dataApi.realestates.bundle.min.js`, `website.realestates.bundle.min.js`), media van `https://media.egorealestate.com/`
- robots.txt noemt `/virtual/PrintProperty.aspx` (ASP.NET, typisch eGO)
- Handlebars-sjablonen (`{{menuName}}`) in de HTML: het menu en delen van de pagina worden client-side gevuld

**Exportfeed:** eGO Real Estate adverteert op zijn eigen site "The only property CRM that allows simultaneous advertising on more than 200 portals worldwide" (bron: https://www.egorealestate.com/en/, 24-09-2026). Het kantoor kan dus een portaal-/XML-export aanzetten. Hoe die technisch werkt (XML, API) staat daar niet; **[te verifiëren]** bij het kantoor of bij eGO.

## 6. Omvang en Jávea-dekking

Schatting op basis van de URL-slugs in de Spaanse sitemap (24-09-2026) — een **ondergrens**, want een slug hoeft de plaats niet te noemen:

| Gebied | Objecten | Aandeel van 220 |
|---|---|---|
| Jávea | 18 | 8 % |
| Benitachell / Cumbre del Sol | 23 | 10 % |
| Moraira / Teulada | 5 | 2 % |
| **Samen** | **46** | **±21 %** |
| Dénia | 21 | 10 % |
| Alicante(-stad/-provincie in slug) | 15 | 7 % |
| Calpe | 12 | 5 % |
| Finestrat / Benidorm | 16 | 7 % |
| Overig (Murcia, Torrevieja, Altea, …) | rest | |

Plus 1 van de 18 nieuwbouwprojecten in Jávea. Opvallend voor Deal Hunter: slugs als "villa en construcción a la venta en Jávea", "chalet en estructura en Jávea", "villa privada … gran potencial de reforma" — precies het soort object dat we zoeken.

## Advies: feed vragen

- Zelf lezen mag technisch (robots.txt), maar de voorwaarden verbieden extractie/hergebruik voor zakelijk gebruik → niet doen zonder toestemming.
- Het systeem (eGO Real Estate) kent portaalexport; het kantoor zit in Jávea en heeft ±46 relevante objecten → de moeite waard om te vragen.

⏸️ **ACTIE VOOR JAN:** Spainlife and Houses (Jávea) benaderen met de vraag of ze hun aanbod als feed (XML/portaalexport uit eGO) of via een samenwerking willen delen. Zonder toestemming blijft deze site buiten de automatische lezer.

## Verantwoording

Opgehaald (4 van max. 5): robots.txt, sitemap.xml, sitemap-es-es.xml, aviso-legal. Niet opgehaald: homepage, aanbodpagina, objectpagina. Externe bron: egorealestate.com (portaalexport). Geen inlog, geen formulieren, geen persoonsgegevens overgenomen (de agentpagina's in de sitemap zijn bewust niet vermeld).

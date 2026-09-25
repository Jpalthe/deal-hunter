# Proxabia Inmobiliaria — toets op automatisch lezen

**Datum controle:** 24-09-2026 · **Website:** https://www.proxabia.com · **Kantoor:** Avda. la Fontana nº 2, local 5, 03730 Jávea · **Algemeen contact:** info@proxabia.com, (+34) 865 60 98 24 (bron: voettekst homepage, 24-09-2026)

**Advies: lezen** — mag volgens robots.txt en de voorwaarden, maar het aanbod is alleen bereikbaar via de eigen zoekaanroep van de site (POST). Zie "Wat dit betekent" onderaan.

Opgehaalde pagina's (5 van maximaal 5, steeds minimaal 2 seconden ertussen): robots.txt, sitemap.xml, homepage, aviso legal, /es/propiedades.

## 1. robots.txt — toegestaan

Bron: https://www.proxabia.com/robots.txt (24-09-2026, HTTP 200). Volledige inhoud:

```
User-agent: *
Disallow:

Sitemap: http://www.proxabia.com/sitemap.xml
```

Een lege `Disallow:` betekent: alles mag gelezen worden, ook de aanbodpagina's. Geen crawl-delay, geen uitzonderingen per bot.

## 2. Gebruiksvoorwaarden — geen scrapingverbod

Bron: https://www.proxabia.com/es/aviso_legal (24-09-2026, HTTP 200). Er is ook een privacybeleid op /es/politica_privacidad (niet opgehaald).

- De aviso legal noemt scraping, robots, geautomatiseerd lezen of gegevensextractie **nergens**.
- Wel staat er een algemene hergebruiksclausule: zonder voorafgaande schriftelijke toestemming is verboden "transmisión, cesión, venta, alquiler y/o exposición pública de esta Web" (overdracht, verkoop, verhuur en/of openbaar tonen van de site of een deel ervan).
- De inhoud wordt "simplemente orientativos" genoemd (louter indicatief); de site aanvaardt geen aansprakelijkheid voor juistheid. Rechtbank: Madrid.

Gevolg voor ons: lezen en intern analyseren is niet verboden; de gegevens **niet opnieuw publiceren** of doorgeven aan derden. De prijzen en oppervlakten zijn volgens de site zelf indicatief — altijd **[te verifiëren]** vóór een bod.

## 3. Sitemap — 8 URL's, geen objecten

Bron: http://www.proxabia.com/sitemap.xml (24-09-2026, HTTP 200, 1.759 bytes).

- 8 URL's, allemaal statische pagina's: `/`, `/es/inicio`, `/es/venta`, `/es/quienes_somos`, `/es/contacto`, `/es/error404`, `/es/politica_privacidad`, `/es/aviso_legal`.
- 0 URL's die op een object lijken (venta/property/inmueble/villa/apartamento/parcela komen alleen voor als de zoekpagina `/es/venta`).
- Gemaakt met de gratis generator xml-sitemaps.com; alle `lastmod` staan op 22-09-2016. De sitemap is dus verouderd en onbruikbaar om het aanbod te tellen.

## 4. Aanbodpagina en objectpagina

- Aanbodpagina: https://www.proxabia.com/es/propiedades (en identiek sjabloon op `/es/inicio` en `/es/venta`). Bron: HTML van beide pagina's, 24-09-2026.
- De HTML bevat een **lege lijst** (`<div id="list"></div>`). Bij het laden roept de pagina zelf `BuscarPropiedades(1)` aan: een **POST** naar `https://www.proxabia.com/web/include/BuscarPropiedades.php` met de velden idioma, localidad, habitaciones, tipo_inmueble, precio, referencia, banyos, oferta, ordenar en pagina. Het antwoord is een HTML-fragment dat in de lijst wordt gezet.
- Die POST heb ik **niet** uitgevoerd (de opdracht sluit formulierverzending uit). Daardoor kon ik geen objectpagina openen: het URL-patroon van objecten staat nergens in de statische HTML of de sitemap.
- **JSON-LD:** op homepage en aanbodpagina afwezig; op objectpagina's onbekend.
- **Open Graph:** homepage/aanbodpagina hebben alleen 4 basistags (og:title "Proxabia Inmobiliaria", og:type website, og:url, og:image = logo). Geen prijs, oppervlakte, perceel, plaats of referentie. Op objectpagina's onbekend.
- Wat de zoekvelden wél verraden (bron: homepage-HTML, 24-09-2026): een veld **Referencia** (objecten hebben dus een referentienummer), prijsklassen tot "+2.000.000 €", sortering op prijs én oppervlakte (oppervlakte is dus een gestructureerd veld), soorten van Ático tot Parcela, Solar en Finca, en een filter "construible" en "Obra nueva".

## 5. Systeem achter de site — eigen bouw (AiDweb)

Bronnen: HTML homepage en antwoordheaders van /es/aviso_legal, 24-09-2026.

- Voettekst "©AiDweb 2015 - 2026" met link naar aidweb.es en `<meta name="author" content="aidweb">`: gebouwd door een klein webbureau.
- Headers: `Server: Apache/2.4.68 (Unix)`, `X-Powered-By: PHP/8.3.33`; cookie `privacy=1`. Eigen PHP-scripts in `/web/include/` (BuscarPropiedades.php, FormularioPropiedad.php), assets in `/web/site_media/` en `/files_proxabia/`.
- Front-end: jQuery, jQuery UI, Owl Carousel, Fancybox, "Galileory"-galerij, Font Awesome via CDN.
- **Geen** sporen van Inmoweb, Mediaelx/LetsINMO, Sooprema, Inmovilla, Witei of WordPress. Geen bekende exportfeed (XML/Kyero) gevonden — die zou het bureau of het kantoor moeten leveren.

## 6. Omvang en dekking Jávea — niet geteld

- Aantal objecten: **onbekend**; zonder de POST-aanroep is er geen lijst en geen teller.
- Aanwijzing (bron: plaatsfilter op de homepage, 24-09-2026): de keuzelijst telt ruim 40 plaatsen — o.a. Jávea, Arenal de Javea, Benitachell, Cumbre del Sol, Moraira, Teulada, Benissa, Dénia, Calpe, Altea, maar ook Valencia, Madrid, Teruel en "FRANCIA". Het kantoor profileert zich als "Su inmobiliaria en Jávea" (meta-omschrijving: "Inmobiliaria en Jávea ... Costa Blanca"), maar de lijst wijst op een aanbod dat breder is dan Jávea/Benitachell/Moraira. Of de keuzelijst het actuele aanbod weerspiegelt of een vaste tabel is, is niet vast te stellen.

## Wat dit betekent

Lezen mag. Technisch is er maar één weg naar het aanbod: dezelfde POST-zoekaanroep doen die de browser van elke bezoeker automatisch doet bij het laden (alle filters op "Indiferente", pagina 1, 2, 3 ...), en daarna de objectlinks uit het antwoord volgen. Dat is geen inlog en geen omzeiling, maar het is wel een formulierverzending in technische zin — daarom niet gedaan in deze toets.

**⏸️ ACTIE VOOR JAN**
1. Akkoord geven om de zoekaanroep (POST, alleen standaardfilters, maximaal één verzoek per twee seconden, met herkenbare user-agent) te gebruiken voor een eerste inventarisatie. Pas daarna is te zeggen hoeveel objecten er zijn en hoeveel in Jávea/Benitachell/Moraira liggen.
2. Alternatief zonder techniek: het kantoor zit op de Avda. la Fontana in Jávea — gewoon vragen of ze hun aanbod (of een feed) willen delen voor samenwerking. Dat levert waarschijnlijk meer op dan lezen, ook omdat de site zelf zegt dat de gegevens slechts indicatief zijn.

Niet gevonden of niet vastgesteld: object-URL-patroon, JSON-LD op objectpagina's, aantal objecten, dekking Jávea. Zoekopdrachten op internet waren in deze sessie niet beschikbaar (zoekbudget op), dus er is geen objectpagina via Google gevonden.

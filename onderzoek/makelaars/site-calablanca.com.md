# Toets automatisch lezen: calablanca.com (Inmobiliaria Calablanca)

Datum toets: 24-09-2026 (ca. 21:03–21:07 UTC). Opgehaald: precies 5 pagina's, telkens meer dan 2 seconden ertussen: robots.txt, homepage, aviso legal, /sitemap.xml en één objectpagina. Zoekmachine-budget van de sessie was op, dus alles komt van de site zelf.

**Let op de bedrijfsnaam.** De opdracht noemt "Cala Blanca Villas S.L.". Het aviso legal op de site noemt als verantwoordelijke **MEDITERRANEAN LIVING, S.L.**, kantoor Avda. Fontana 2, Local 6, 03730 Jávea (Alicante); algemeen contactkanaal voor rechtenkwesties: gerencia@calablanca.com. Bron: https://www.calablanca.com/aviso-legal/ (24-09-2026). Welke rechtspersoon het kantoor nu precies exploiteert: **[te verifiëren]**.

## 1. robots.txt: automatisch lezen toegestaan, met rem

Bron: https://www.calablanca.com/robots.txt (24-09-2026; `Last-Modified` 25-07-2025; 421 regels).

Voor `User-agent: *` staat er, na een reeks uitzonderingen, uitdrukkelijk `Allow: /`:

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
...
Disallow: */imprimir/*
Disallow: */print/*
Allow: /
```

Helemaal onderaan staat een tweede blok voor iedereen:

```
User-agent: *
Crawl-delay: 14
```

Wat dit betekent:
- Aanbod- en objectpagina's (`/propiedades-en-venta-...`, `/propiedad/...`) vallen onder `Allow: /` en mogen gelezen worden.
- Uitgesloten zijn formulieren, de fotogalerij-modals, printversies en **de bladerpagina's** (`/*/*/*/pagina/*`, `/page/*`, ...). Pagina 2, 3, ... van een lijst op drie niveaus diep is dus verboden; objecten moet je via de eerste lijstpagina of via losse links vinden.
- `Crawl-delay: 14`: maximaal één verzoek per 14 seconden. Dat is strenger dan onze eigen regel (2 s) en moet gerespecteerd worden.
- 131 specifieke tools worden met naam geblokkeerd, waaronder `Wget`, `Python-urllib`, `HTTrack`, `WebZip`, `WebCopier`, `Teleport`. Geen AI-bots (GPTBot, CCBot e.d.) genoemd. Een lezer moet zich dus niet als Wget of Python-urllib melden.
- Er staat **geen `Sitemap:`-regel** in.

## 2. Gebruiksvoorwaarden: geen expliciet verbod op automatisch lezen

Bron: https://www.calablanca.com/aviso-legal/ (24-09-2026). Er is ook een `/privacidad/` en een `/politica-de-cookies/`; die zijn niet geopend (paginabudget).

In het aviso legal komen de woorden robot, scraping, crawler, automatisch, extractie of databank **niet** voor (gecontroleerd op de kale tekst). Wel staat er een brede clausule over intellectueel eigendom (paragraaf 2), vertaald samengevat: gehele of gedeeltelijke reproductie, gebruik, exploitatie, distributie en commercialisering van de site-inhoud vereist altijd voorafgaande schriftelijke toestemming van de verantwoordelijke; ongeautoriseerd gebruik geldt als ernstige inbreuk. Letterlijk (kort): "la reproducción total o parcial, uso, explotación, distribución y comercialización, requiere en todo caso de la autorización escrita previa".

Oordeel: automatisch lezen wordt niet verboden. Foto's en teksten overnemen of doorpubliceren wél. Voor intern gebruik (signaleren van deals, eigen analyse) is dat werkbaar; niets van deze site mag in onze eigen publicaties terechtkomen.

## 3. Sitemap: niet gevonden

- robots.txt: geen `Sitemap:`-regel.
- https://www.calablanca.com/sitemap.xml → 301 naar `/sitemap.xml/` → **404** (24-09-2026 21:05 UTC; het 404-scherm is een lege boilerplate-pagina met `noindex,nofollow`).
- `/sitemap_index.xml` is niet getest: dat zou de vijfde fetch hebben gekost, en de objectpagina was belangrijker.

Aantal object-URL's in de sitemap: **niet vast te stellen**.

## 4. Aanbodpagina en objectpagina

Aanbodpagina (menu "Ventas" op de homepage): https://www.calablanca.com/propiedades-en-venta-en-costa-blanca/ . Deelpagina's: `/chalets-en-venta-javea/`, `/apartamentos-en-venta-javea/`, `/chalets-en-venta-costa-blanca/`, `/apartamentos-en-venta-costa-blanca/`. Verhuur: `/propiedades-en-alquiler-en-costa-blanca/`. Bron: homepage https://www.calablanca.com/ (24-09-2026).

Objectpagina getest: https://www.calablanca.com/propiedad/chalet-en-primera-linea-en-venta-con-vistas-al-mar-en-javea-c-3510r/ (link stond op de homepage) → **HTTP 404** (24-09-2026 21:06 UTC). De pagina was op dat moment blijkbaar al verwijderd of de homepage-cache liep achter (het object stond op de homepage met prijs "CONSULTAR"). Daardoor kon ik op een objectpagina **niet** controleren of er `application/ld+json` of `og:`-tags staan: **onbekend**.

Wat wél bekend is (uit de homepage-HTML, 24-09-2026):
- De homepage zelf bevat 0 ld+json-blokken en 0 `og:`-meta-tags. Dat is een aanwijzing dat de site weinig gestructureerde data uitzendt, maar geen bewijs voor de objectpagina's.
- De **referentie zit in de URL-slug**: `c-3510r`, `c-3518r`, `c-6214` (chalets), `a-5071` (gebouw), `l-5073` (horeca), `g-7327` (garage), `rent-...` (verhuur).
- Prijzen op de homepage-kaarten: gebouw in de haven van Jávea 1.495.000 €; chalet Balcón al Mar, Jávea 760.000 €; projecthuis Moraira 595.000 €; chalet eerste lijn Jávea "CONSULTAR". Oppervlakte/perceel staan niet op de kaarten.
- Zoekformulier kent filters voor bewoonde oppervlakte en perceel (m²), dus die velden bestaan in het systeem.

## 5. Systeem achter de site: Sooprema

Aanwijzingen (homepage-HTML, 24-09-2026):
- `<meta name="generator" content="Mattis-Framework 4.0">` en `<meta name="application-name" content="App-pagina-web-mattis">`.
- Footer-credit: link naar https://www.sooprema.com/ met titel "Software Inmobiliario Sooprema".
- Paden: `/objetos/cache/calablanca/css/...`, `/objetos/temp/source/calablanca/2026/09/24/...`, `/core/objetos/js/...`; objecten onder `/propiedad/...`; robots.txt-uitsluitingen als `/html/formulario/`, `/portal/proceso/` horen bij hetzelfde platform.
- Server: Apache, PHP-sessiecookie `PHPSESSID` (8 uur), cookiebanner met klassen `cookies-necessary` / `cookies-marketing`.
- Geen WordPress, Inmoweb, Mediaelx of Inmovilla-sporen.

Sooprema kent exportfeeds (XML/portaalkoppelingen). Dat is een schone alternatieve route als lezen te traag of te wankel blijkt.

## 6. Omvang en dekking Jávea/Benitachell/Moraira

Totaal aantal objecten: **niet vastgesteld** (geen sitemap, aanbodpagina niet geopend binnen het budget). Indicaties uit de homepage (24-09-2026):
- 11 objectlinks op de homepage: 8 met "javea" in de slug (4 koop, 3 huur, 1 opvang), 1 Moraira, 2 garages zonder plaatsnaam.
- Zoekfilter "Localidad" biedt alleen: Benitachell, Calpe, Denia, Jávea, Moraira, Teulada. Bij Sooprema-sites is die lijst normaliter gevuld vanuit het actuele aanbod, dus het aanbod ligt in die zes gemeenten **[te verifiëren]**.
- Zoekfilter "Zona" biedt tien wijken en die liggen álle in Jávea (Arenal, Arnella, Cap Martí, Costa Nova, Granadella, Montgó, Puerta Fenicia, Puerto, Tosalet, Adsubia-Rebaldí).

Inschatting: een Jávea-kantoor met het zwaartepunt in Jávea, plus Benitachell en Moraira/Teulada en enkele objecten in Dénia en Calpe. Precieze verhouding pas te geven na het lezen van de aanbodpagina.

## Advies: lezen (voorwaardelijk)

- robots.txt staat het toe, de voorwaarden verbieden automatisch lezen niet, homepage en aviso legal zijn gewoon leesbaar.
- Voorwaarden voor de lezer: **één verzoek per 14 s** (Crawl-delay), gewone browser-achtige User-Agent (Wget/Python-urllib zijn met naam geblokkeerd), geen bladerpagina's (`/pagina/`, `/page/`), geen printversies, geen formulieren.
- Eerst opnieuw één objectpagina testen met een verse link van de aanbodpagina; de eerste test gaf 404. Pas daarna ld+json/og beoordelen.
- Alleen intern gebruik: geen foto's of teksten overnemen (IE-clausule).
- Parallel spoor: het kantoor om een Sooprema-exportfeed vragen; dat is netter en sneller dan lezen met 14 s vertraging.

## Bronnen

- https://www.calablanca.com/robots.txt (24-09-2026)
- https://www.calablanca.com/ (24-09-2026)
- https://www.calablanca.com/aviso-legal/ (24-09-2026)
- https://www.calablanca.com/sitemap.xml (24-09-2026, 301 → 404)
- https://www.calablanca.com/propiedad/chalet-en-primera-linea-en-venta-con-vistas-al-mar-en-javea-c-3510r/ (24-09-2026, 404)

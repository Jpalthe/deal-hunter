# Javea Homes — www.javeahomes.com

**Toets op automatisch lezen · 24-09-2026 (21:12–21:14 UTC)**
Onderzoek voor TREE Deal Hunter. Vijf ophaalacties op de site gedaan (het maximum), met minimaal 14 seconden ertussen omdat robots.txt daarom vraagt. Niets omzeild, niet ingelogd, geen formulieren.

## Kort

**De site staat in onderhoud.** De homepage en /sitemap.xml geven allebei dezelfde lege pagina "System Updating" (HTTP 200, 1529 bytes), ook via een tweede, onafhankelijke ophaalmethode. Er is nu dus niets te lezen: geen aanbodpagina, geen objectpagina, geen voorwaarden. Robots.txt staat lezen grotendeels toe, maar verbiedt het doorbladeren van de lijstpagina's en vraagt 14 seconden tussen elke opvraging.

**Advies: overslaan (voorlopig).** Over twee weken opnieuw toetsen. Blijft de site plat, dan is het kantoor waarschijnlijk niet meer via deze site actief.

## 1. robots.txt — mag een gewone bot de aanbodpagina's lezen?

Bron: https://www.javeahomes.com/robots.txt (opgehaald 24-09-2026 21:12 UTC, HTTP 200, 5717 bytes).

**Ja, grotendeels ("deels").** Voor `User-agent: *` staat er `Allow: /`, met deze relevante uitzonderingen (letterlijk geciteerd):

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

en onderaan, in een tweede blok voor dezelfde `User-agent: *`:

```
User-agent: *
Crawl-delay: 14
```

Wat dit betekent voor automatisch lezen:
- Objectpagina's zelf zijn niet uitgesloten.
- **Het doorbladeren van lijstpagina's is verboden** (`/*/*/*/pagina/*`, `/page/*`, `/seite/*` enz. — pagina 2, 3, ... van het aanbod in elke taal). Een lezer moet dus via de sitemap werken, niet via "volgende pagina".
- Formulieren, fotogalerij-vensters en printversies zijn verboden.
- **14 seconden wachttijd** tussen opvragingen.
- Daarnaast worden ruim honderd specifieke bots met `Disallow: /` geweerd, waaronder `Python-urllib`, `Wget`, `HTTrack 3.0`, `WebCopier`, `Offline Explorer`, `EmailCollector`. Een eigen lezer moet dus onder een eigen, herkenbare naam draaien en zeker niet met de standaard user-agent van Python of wget.
- Geen `Sitemap:`-regel.

## 2. Gebruiksvoorwaarden — verbieden ze scraping?

**Niet gevonden.** De site geeft op elke opgevraagde pagina de onderhoudspagina; de link naar een aviso legal / voorwaarden kon daardoor niet worden gevonden en niet worden gelezen. Het zoekbudget van deze sessie was op, dus ook via zoekmachines niet te achterhalen. Het Internet Archive is vanuit deze omgeving niet te openen. Dit punt is dus **open**, niet "nee".

## 3. Sitemap

- robots.txt noemt geen sitemap.
- https://www.javeahomes.com/sitemap.xml → 301 naar `/sitemap.xml/` → HTTP 200, maar de inhoud is de HTML-onderhoudspagina, byte-voor-byte identiek aan de homepage (24-09-2026 21:12 UTC). Geen XML, dus **0 telbare URL's; werkelijk aantal onbekend**.
- /sitemap_index.xml niet geprobeerd: het maximum van vijf opvragingen was bereikt en alles wijst erop dat elke pagina dezelfde onderhoudspagina geeft.

## 4. Aanbodpagina en objectpagina

**Niet bereikbaar.** Homepage (https://www.javeahomes.com/, 24-09-2026 21:12 UTC, HTTP 200, 1529 bytes) bevat alleen:

```
<title>System Updating</title>
... <div class="contenedor"><div class="imagen"></div></div>
```

De enige inhoud is een achtergrondafbeelding `/imagenes/web/info.png` (770×610 px, opgehaald 21:14 UTC) met de tekst: "(system) Updating — We are updating our system... Soon You get all the information of interest". Geen navigatie, geen links, geen JSON-LD, geen og:-tags. Prijs, oppervlakte, perceel, plaats, referentie: **onbekend**.

Controle met een tweede methode (WebFetch, andere user-agent, 24-09-2026 ca. 21:13 UTC): zelfde "System Updating"-pagina. Het is dus geen blokkade van mijn ophaalprogramma, maar echt onderhoud.

## 5. Systeem achter de site

**Onbekend — niet vast te stellen zolang de site plat ligt.** Wel zichtbare aanwijzingen (bron: HTTP-headers en robots.txt, 24-09-2026):

- `server: Apache`, cookie `PHPSESSID` op `.javeahomes.com` → PHP-systeem.
- Spaanstalige mappen: `/imagenes/web/`, `/html/formulario/llamanos/`, `/html/formulario/48horas/`, `/html/formucontraoferta/` (tegenbod-formulier), `/html/galeriamodal/`, `/portal/proceso/secciones/`, `/portal/proceso/newsletter/`, `/giuliano/proceso/enviar/`.
- Meertalige slugs voor bladeren (pagina/pages/page/seite/stranitsa/siden) en printen (imprimir/print/drucken/imprimer/afdrukken) → een Spaans vastgoed-CMS met minstens zes talen, waaronder Nederlands en Russisch.
- De onderhoudspagina is een generieke leverancierspagina ("(system) Updating"), niet iets van het kantoor zelf.
- Geen sporen van WordPress (`/wp-content/`, `/wp-admin/`) in robots.txt — maar dat is zwak bewijs zolang de HTML niet te zien is.

Welke leverancier dit precies is (Inmoweb, Mediaelx, Sooprema, Inmovilla, Witei of eigen bouw) heb ik **niet** kunnen bevestigen; ik gok niet.

## 6. Omvang en dekking Jávea / Benitachell / Moraira

**Onbekend.** Geen aanbod zichtbaar. De domeinnaam wijst op Jávea als kernmarkt, maar dat is niet geverifieerd.

Extra signaal: de Wayback-beschikbaarheids-API (https://archive.org/wayback/available?url=javeahomes.com, geraadpleegd 24-09-2026) meldt als meest recente bewaarde kopie **29-08-2024** (`http://web.archive.org/web/20240829104208/https://www.javeahomes.com/`). Dat de site ruim twee jaar niet meer is gearchiveerd kán betekenen dat hij al lang plat ligt of weinig bezocht wordt — maar dat is een aanwijzing, geen bewijs.

## Advies

**Overslaan (voorlopig).** Motivatie:
- Er is nu niets te lezen; robots.txt verbiedt niets wezenlijks maar de site zelf werkt niet.
- Het systeem is onbekend, dus ook niet te zeggen of er een exportfeed bestaat om te vragen.

**Opnieuw toetsen rond 08-10-2026.** Komt de site terug, dan gelden bij automatisch lezen: eigen herkenbare user-agent (niet Python-urllib/wget), 14 s tussen opvragingen, via de sitemap en niet via "volgende pagina", en eerst de voorwaarden lezen.

⏸️ **ACTIE VOOR JAN:** ga na of Javea Homes als kantoor nog actief is (en of ze onder een andere domeinnaam zijn verdergegaan). Dat kan lokaal sneller dan via internet. Blijkt het kantoor actief maar de site blijvend uit, dan is rechtstreeks contact via het algemene kantoorkanaal de enige route naar hun aanbod.

## Bronnen en tijdstippen

| Wat | URL | Wanneer (UTC) | Resultaat |
|---|---|---|---|
| robots.txt | https://www.javeahomes.com/robots.txt | 24-09-2026 21:12 | HTTP 200, 5717 bytes |
| Homepage | https://www.javeahomes.com/ | 24-09-2026 21:12 | HTTP 200, onderhoudspagina 1529 bytes |
| Sitemap | https://www.javeahomes.com/sitemap.xml → /sitemap.xml/ | 24-09-2026 21:12 | 301 → 200, zelfde onderhoudspagina |
| Homepage (2e methode) | https://www.javeahomes.com/ | 24-09-2026 ca. 21:13 | onderhoudspagina |
| Onderhoudsafbeelding | https://www.javeahomes.com/imagenes/web/info.png | 24-09-2026 21:14 | PNG 770×610, tekst "We are updating our system..." |
| Wayback-API | https://archive.org/wayback/available?url=javeahomes.com | 24-09-2026 | laatste kopie 29-08-2024 |

Niet gedaan (en waarom): zoekmachine-onderzoek (sessiebudget op), Wayback-kopie zelf lezen (web.archive.org niet bereikbaar vanuit deze omgeving), meer dan vijf opvragingen (limiet).

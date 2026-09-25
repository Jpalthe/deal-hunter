# Indarte Inmobiliaria — toets op automatisch lezen

- **Website:** https://www.indarteinmobiliaria.com
- **Datum toets:** 24-09-2026
- **Bedrijfsgegevens (uit de footer van de homepage):** REAL ESTATE INDARTE, Thiviers 2A, 03730 Jávea — tel. 965 79 35 26 — javea@indarteinmobiliaria.com. Volgens de footer opgericht in 1999.
- **Opgehaald:** precies 5 pagina's (robots.txt, sitemap.xml, /condiciones-de-uso/, één objectpagina, homepage), met minimaal 2 seconden ertussen.

## Conclusie in één zin

De site is **geen levende website meer** maar een statische, onvolledige archiefkopie ("gratis demo" van een Wayback-Machine-downloader) van de oude WordPress-site uit 2019: alle objectpagina's zijn dood, de voorwaardenpagina is leeg, en het getoonde aanbod is ruim zeven jaar oud. **Advies: overslaan** voor automatisch lezen. Het kantoor zelf kan nog wel bestaan — zie onderaan.

## 1. robots.txt — toegestaan

Bron: https://www.indarteinmobiliaria.com/robots.txt (HTTP 200, 51 bytes, last-modified 06-11-2025, opgehaald 24-09-2026).

Het bestand bevat één regel:

    Sitemap: http://indarteinmobiliaria.com/sitemap.xml

Er staat geen enkele `User-agent:`- of `Disallow:`-regel in. Voor `User-agent: *` is dus niets verboden; de aanbodpagina's mogen gelezen worden. **Oordeel: ja.**

## 2. Gebruiksvoorwaarden — niet gevonden (lege pagina)

Bron: https://www.indarteinmobiliaria.com/condiciones-de-uso/ (HTTP 200 maar **0 bytes**, last-modified 18-08-2026, opgehaald 24-09-2026).

De pagina bestaat in de sitemap en in het footermenu (naast AVISO LEGAL, COPYRIGHT, POLÍTICA DE PRIVACIDAD en LEY DE COOKIES), maar levert een leeg document op. Er is dus geen tekst die scraping verbiedt of toestaat. De overige juridische pagina's heb ik niet geopend (limiet van vijf pagina's); gezien punt 4 hieronder (de kopie bevat maar vier echte pagina's) zijn die vrijwel zeker ook leeg — **niet geverifieerd**. **Oordeel: niet gevonden.**

## 3. Sitemap — 40 URL's, 23 objecten, maar een "demo"-sitemap

Bron: https://www.indarteinmobiliaria.com/sitemap.xml (HTTP 200, 4.381 bytes, last-modified 06-11-2025, opgehaald 24-09-2026).

- 40 `<loc>`-vermeldingen in totaal.
- 23 daarvan zijn objectpagina's onder `/inmueble/` (bijv. `/inmueble/jv-1951-encantadora-villa-en-balcon-al-mar-de-javea/`, `/inmueble/jv-1628-solar-en-javea-urbano/`).
- 3 statuspagina's onder `/inmueble-estado/ofertas/` (+ `view-list`, `view-grid`), 4 pagineringspagina's (`/page/2/` t/m `/page/4/` en `/page/53/`), en verder servicios, contactar, busqueda, quiero-vender en de juridische pagina's.
- In de XML staat een html-commentaar dat dit de sitemap van een gratis demoversie is en géén volledige lijst; de betaalde versie zou een grotere sitemap hebben. Geen sitemap-index gevonden (niet nodig: robots.txt wijst rechtstreeks naar dit bestand).

## 4. Aanbodpagina en objectpagina — objectpagina's zijn dood

**Aanbod:** de homepage https://www.indarteinmobiliaria.com/ toont zelf het aanbod (blok "home-properties"): 12 kaarten met titel, foto en prijs, met paginering "1 2 3 4 Siguiente Último" waarbij Último naar `/page/53/` wijst. In het menu staat verder OFERTAS → `/inmueble-estado/ofertas/` (niet geopend). Prijsnotatie op de kaarten: `<span class="price">545,000€ EUR</span>`.

Prijzen op de homepage (stand van de kopie, dus 2019): 78.000 / 120.000 / 155.000 / 155.000 / 157.000 / 159.000 / 175.000 / 259.000 / 299.000 / 350.000 / 395.000 / 545.000 EUR.

**Objectpagina:** https://www.indarteinmobiliaria.com/inmueble/jv-1951-encantadora-villa-en-balcon-al-mar-de-javea/ (HTTP 200, **719 bytes**, last-modified 06-11-2025, opgehaald 24-09-2026).

Dit is géén woningpagina maar een stub-tekst: de demoversie bevat volgens die tekst maar vier pagina's (de homepage, `servicios`, `inmueble-estado/ofertas` en `como-comprar-2`) en verwijst naar waybackmachinedownloader.com om "een volledig werkende site" te kopen. De homepage zegt zelf ook dat dit het gratis demoresultaat is en dat een complete website van archive.org gedownload kan worden.

- `<script type="application/ld+json">` op de objectpagina: **geen**. (Op de homepage staat alleen een Yoast-blok van het type WebSite/SearchAction, geen woninggegevens.)
- `og:`-tags op de objectpagina: **geen**. (Homepage: alleen generieke og:locale, og:type=website, og:title, og:url, og:site_name.)
- Prijs, oppervlakte, perceel, plaats, referentie op de objectpagina: **niets** — alleen de URL zelf verraadt referentie JV-1951, type villa, zone Balcón al Mar, Jávea; de prijs (545.000 EUR) staat uitsluitend op de homepage-kaart.

## 5. Systeem achter de site

Oorspronkelijk **WordPress** met het vastgoedthema **RealHomes** (13 verwijzingen naar `wp-content/themes/realhomes`), plus plugins js_composer (Visual Composer), Slider Revolution 5.2.6, Yoast SEO v5.7, Contact Form 7, Google Language Translator, GDPR Cookie Compliance en Awesome Weather (alle uit de html van de homepage). Ontwerp door ZONADEWEB (footer).

Maar: het draait **niet meer als CMS**. Aanwijzingen: server `Apache` met `etag`/`last-modified` op statische bestanden, geen enkele `Set-Cookie`, de demo-stub op elke objectpagina, de demo-commentaarregel in de sitemap, en uploadmappen `wp-content/uploads/2016/03` t/m `2019/04` (nieuwste = april 2019). Yoast v5.7 dateert uit 2017. De kopie is op 06-11-2025 op de server gezet (last-modified van homepage, sitemap, robots en stub). Kortom: **eigen bouw / statische archiefkopie van een WordPress-site**; geen Inmoweb, Mediaelx, Sooprema, Inmovilla of Witei, en dus ook geen exportfeed.

## 6. Omvang en Jávea-dekking

- Leesbaar nú: **0 objectpagina's** (allemaal stub).
- Zichtbaar op de homepage: 12 kaarten met prijs, 20 verschillende objectlinks (incl. 8 bedrijfsruimtes/locales, deels verhuur); 23 object-URL's in de sitemap. Alles stand ±april 2019.
- Toen (2019): paginering tot pagina 53 × 12 per pagina ≈ **630 items** incl. verhuur en bedrijfsruimte — afgeleid, niet geteld.
- **Jávea-dekking:** alle 20 objecttitels bevatten "javea" (Arenal, Puerto, Pueblo, Thiviers, Balcón al Mar, Costa Nova, La Cala, Montañar, Urbatenis, Vía Augusta) → **100 % Jávea** in het zichtbare deel. Benitachell en Moraira komen alleen voor in de plaatsenlijst van het zoekformulier (een lijst met ook Valenciaanse plaatsen als Mislata en Liria), niet in het aanbod.

## Advies: overslaan

Niet omdat het verboden is (robots.txt staat alles toe, voorwaarden ontbreken), maar omdat er niets te lezen valt: geen werkende objectpagina's, geen gestructureerde data, verouderd aanbod uit 2019, geen feed. Een scraper zou hier alleen twaalf prijzen van zeven jaar geleden ophalen.

**Wat wél interessant is voor Deal Hunter:** een kantoor sinds 1999 in Jávea waarvan de website dood is, is precies het type makelaar dat zijn aanbod niet op portalen zet. Of het kantoor nog actief is kon ik niet controleren (het zoekbudget van deze sessie was op; geen web-zoekopdracht mogelijk).

⏸️ **ACTIE VOOR JAN (optioneel):** even bellen (965 79 35 26) of mailen (javea@indarteinmobiliaria.com) of het kantoor nog bestaat en wat het in portefeuille heeft — renovatieobjecten, solares (de sitemap noemt JV-1628 en JV-528 als "solar en Javea"), bedrijfsruimte in het Pueblo. Off-market, niet via de site.

## Bronnen (alle opgehaald 24-09-2026)

1. https://www.indarteinmobiliaria.com/robots.txt
2. https://www.indarteinmobiliaria.com/sitemap.xml
3. https://www.indarteinmobiliaria.com/condiciones-de-uso/
4. https://www.indarteinmobiliaria.com/inmueble/jv-1951-encantadora-villa-en-balcon-al-mar-de-javea/
5. https://www.indarteinmobiliaria.com/

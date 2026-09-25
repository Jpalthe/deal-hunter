# TerramaR Costa Blanca — terramar.es: toets op automatisch lezen

**Kantoor:** Terramar Costa Blanca S.L. (handelsnaam "TerramaR Costa Blanca"), Plaza Adolfo Suárez 18, 03730 Jávea (Alicante), Apdo. correos 524 · algemeen contact info@terramar.es · 966 460 560 (bron: voettekst homepage via de standaard ophaaltool, 24-09-2026; kantoorlijst `K01-kantoren-javea.json` op basis van xabia.org/ver/2098, 24-09-2026).
**Website:** https://www.terramar.es · talen /es/ /en/ /de/ /fr/ /nl/ /ru/ /no/ /sv/.
**Datum toets:** 24-09-2026, ca. 23:22–23:29 lokale tijd (serverkoppen 21:22–21:28 UTC).
**Verzoeken aan de site:** zes, nooit sneller dan één per twee seconden (in de praktijk ≥ 1 minuut ertussen): robots.txt, homepage (curl), sitemap.xml (curl), homepage-koppen (curl), sitemap.xml (standaard ophaaltool, gaf alleen een 301), homepage (standaard ophaaltool). Drie daarvan leverden inhoud op. Geen inlog, geen formulieren, geen browser nagebootst, geen rekenpuzzel opgelost, geen cookie gezet. Daarna niets meer opgehaald.
**Webzoeken:** niet beschikbaar in deze sessie (zoekbudget op); Wayback Machine heeft geen kopie van terramar.es (`archive.org/wayback/available`, 24-09-2026).

## Advies in één zin

**Feed vragen.** robots.txt staat een gewone lezer toe (met pauze van 14 s en zonder bladerpagina's), maar de site zet vóór elke HTML-pagina een JavaScript-botcontrole ("Powered by Paagees Shield") die een gewone automatische lezer tegenhoudt. Die omzeilen we niet, dus voorwaarden, aanbodlijst en objectpagina's konden niet gelezen worden. De site draait op **Sooprema**; Sooprema kent een API/feed-route die via het kantoor loopt (B01 §2.2). Het kantoor zit in Jávea, bouwt en verkoopt zelf en heeft renovatie- en perceelobjecten — de moeite van een verzoek waard.

## 1. robots.txt — toegestaan met beperkingen (maar zie de botcontrole)

Bron: https://www.terramar.es/robots.txt (HTTP 200, opgehaald 24-09-2026). Voor `User-agent: *` staat letterlijk:

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

Uitleg in gewone taal:
- De aanbodpagina (`/propiedades/venta/todas/`) en objectpagina's vallen onder `Allow: /` en **mogen** gelezen worden.
- Vervolgpagina's van lijsten (`/…/…/…/pagina/2/`, `/page/2/`, `/seite/2/` enz.) mogen **niet** — alleen de eerste pagina van elke lijst. Printversies, formulieren (bel-mij, 48 uur, tegenbod) en de fotogalerij-modal mogen ook niet.
- Tussen twee verzoeken wordt **14 seconden** pauze gevraagd.
- Daarnaast staan ruim 100 programma's met naam op `Disallow: /`, o.a. `Wget`, `Python-urllib`, `httplib`, `lwp-trivial`, `HTTrack 3.0`, `WebCopier`, `Offline Explorer`, `EmailCollector`. Een lezer die zich eerlijk onder eigen naam meldt valt onder de `*`-regels, maar het signaal is duidelijk: massaal kopiëren is ongewenst.
- **Geen `Sitemap:`-regel.**
- Dit bestand is hetzelfde sjabloon als bij calablanca.com en costablancajaveaproperties.com (Giuliano Villas), zie de verslagen in deze map: het robots.txt-sjabloon van het Sooprema/"Mattis"-platform.

**Belangrijk voorbehoud:** wat robots.txt toestaat, houdt de server in de praktijk tegen. Een gewone HTTP-client (curl, eigen herkenbare User-Agent `TREE-DealHunter-check/1.0`) kreeg op de homepage én op /sitemap.xml geen inhoud maar een HTML-pagina van 5.882 bytes, titel "Security Check", tekst "Verifying your browser … This is an automatic security check", voettekst "Powered by Paagees Shield". Koppen: `server: nginx`, `x-robots-tag: noindex, nofollow`, `cache-control: no-store`. De pagina laat de browser een SHA-256-rekenpuzzel oplossen (5 leidende hex-nullen), zet dan een cookie `__shield` (1 uur geldig) en herlaadt. Zonder JavaScript en cookies kom je er niet doorheen. **Niet opgelost, niet omzeild.** Dat is een bewuste keuze van het kantoor of zijn leverancier om geautomatiseerd lezen te bemoeilijken; daar houden we ons aan.

## 2. Gebruiksvoorwaarden — bestaan, maar niet gelezen

- De voettekst van de homepage (standaard ophaaltool, 24-09-2026) toont één juridische link: `/aviso-legal/`. Geen aparte pagina "condiciones" of "términos" gezien.
- De inhoud van https://www.terramar.es/aviso-legal/ is **niet gelezen**: dat zou een zevende verzoek zijn geweest en voor een gewone lezer staat de Shield ervoor.
- Ter vergelijking: de zusterkantoren op hetzelfde Sooprema-platform (calablanca.com, verslag 24-09-2026) en op de Paagees-weblaag (javeaimmo.com, verslag 24-09-2026) verbieden in hun aviso legal **reproductie en commercieel gebruik** van de inhoud zonder toestemming; een letterlijk scrapingverbod staat daar niet in. Aannemelijk dat Terramar een vergelijkbare tekst heeft **[te verifiëren]**.
- Conclusie: **niet gevonden/niet gelezen**. Ga er niet van uit dat teksten of foto's vrij herbruikbaar zijn.

## 3. Sitemap — geen bruikbare sitemap

- Geen `Sitemap:`-regel in robots.txt.
- https://www.terramar.es/sitemap.xml met curl → HTTP 200, maar de inhoud is de Shield-pagina (byte-voor-byte gelijk aan de homepage-Shield), geen XML.
- Dezelfde URL via de standaard ophaaltool → **301** naar `http://www.terramar.es/sitemap.xml/` (met slash). Niet gevolgd (paginabudget). Bij calablanca.com en Giuliano Villas — zelfde platform, zelfde robots.txt — eindigt precies deze omleiding op een **404**, dus een echte sitemap is hier niet te verwachten **[te verifiëren]**.
- `/sitemap_index.xml` niet geprobeerd.
- Aantal object-URL's in de sitemap: **niet vast te stellen**. (De vermelding "sitemap 200" in register R06 van 14-09-2026 was hoogstwaarschijnlijk óók de Shield-pagina met status 200.)

## 4. Aanbodpagina en objectpagina — niet leesbaar voor een automatische lezer

- **Aanbodpagina (menu "Venta"):** https://www.terramar.es/propiedades/venta/todas/ (uit de navigatie van de homepage, standaard ophaaltool, 24-09-2026). Verder in het menu: `/propiedades/alquiler-anual/todas/`, `/propiedades/alquiler-vacacional/todas/`, `/vender/`, `/quienes-somos/`, `/contacto/`. Een "Obra Nueva"-filter is zichtbaar. De aanbodpagina zelf is **niet opgehaald** (budget; Shield).
- **Objectpagina:** **niet opgehaald.** Er is geen letterlijke object-URL vastgelegd; op zustersites van hetzelfde platform staan objecten onder `/propiedad/…` (calablanca.com) of `/property/…` (Giuliano Villas).
- **JSON-LD (`application/ld+json`) en og:-tags: onbekend.** De ruwe HTML is niet te zien zonder de Shield te omzeilen, en de standaard ophaaltool geeft alleen leesbare tekst terug. Bij de twee zustersites op dit platform was er **geen** JSON-LD; Giuliano had wél og-tags (type product, zonder prijs) en de prijs/m²/perceel/plaats/referentie gewoon in de HTML (`input[name=precio]`, `class="constru"`, `class="parcela"`, verborgen JSON `formvisitadatos`). Aannemelijk dat Terramar dezelfde structuur heeft **[te verifiëren]**.
- Wat de homepage (leesbare tekst) wél toonde: referenties in de vorm **TM119, TM010, TM185, TM176** en **TMEX101, TMEX326** ("TM" = TerramaR, "TMEX" vermoedelijk exclusief **[te verifiëren]**); prijzen van € 230.000 (appartementen) tot € 3.525.000 (villa, TM119); labels als "obra nueva", "proyecto con licencia", "inversión". Eerdere waarneming (R06-verificatie A13, 15-09-2026): objecten "totalmente para reformar" en "Parcela edificable".

## 5. Systeem achter de site — Sooprema (met Paagees Shield ervoor)

Aanwijzingen (24-09-2026):
- Voettekst-credit **"Sooprema"** (logo/link) op de homepage (standaard ophaaltool).
- robots.txt is het sjabloon van het Sooprema/"Mattis"-platform: paden `/html/formulario/`, `/html/galeriamodal/`, `/html/formucontraoferta/`, `/portal/proceso/`, meertalige `pagina/page/seite/stranitsa/siden` en `imprimir/print/drucken/imprimer/afdrukken` — identiek aan calablanca.com (daar met `<meta name="generator" content="Mattis-Framework 4.0">` en voettekstlink "Software Inmobiliario Sooprema") en aan costablancajaveaproperties.com.
- HTML-pagina's komen van `nginx` met de botcontrole "Powered by Paagees Shield" (cookie `__shield`). Volgens B01 §2.3 (paagees.com, 16-09-2026) is Paagees géén CRM maar een weblaag/beschermlaag die zich via XML of API koppelt aan o.a. Sooprema; de R06-verificatie (15-09-2026) stelde al vast dat de Shield ook vóór Sooprema-sites staat, waaronder Terramar.
- Hosting: IP 31.170.101.188, nameservers dondominio.com (dig, 24-09-2026).
- Geen sporen van WordPress, Inmoweb, Mediaelx/LetsINMO, Inmovilla of Witei in wat leesbaar was.
- **Exportmogelijkheid:** Sooprema biedt live data via een REST-API, maar alleen als "la agencia en cuestión deberá ser cliente activo de Sooprema" (B01 §2.2, 16-09-2026). De route loopt dus via het kantoor: Terramar vraagt (of machtigt) bij Sooprema een uitgang voor TREE.

## 6. Schatting aanbod en dekking Jávea/Benitachell/Moraira

- **Aantal:** de homepage toont "ongeveer 40+" objecten in carrousel en raster (standaard ophaaltool, 24-09-2026); register R06 (14-09-2026) schatte "± 40". De aanbodlijst zelf is niet geteld → schatting **≈ 40 objecten te koop, mogelijk meer** **[te verifiëren]**.
- **Dekking (steekproef homepage, 24-09-2026):** Jávea/Xàbia **20+** (o.a. villa met baaizicht € 1.695.000 TMEX101; villa moderne stijl € 3.525.000 TM119; havenhuis € 1.250.000 TMEX326; appartementen € 230.000–365.000; villa's € 485.000–995.000), Benitachell/Cumbre del Sol **3** (TM010 € 895.000, TM185 € 1.495.000, TM176 nieuwbouw € 1.950.000), Moraira **0 gezien**, elders **10+** (Calpe, Orba, Pedreguer, Parcent, Benissa, Altea). Ruwweg **twee derde** in het doelgebied, vrijwel allemaal Jávea **[te verifiëren op de volledige lijst]**.
- **Profiel:** volgens de bedrijvengids javea.com (24-09-2026, https://en.javea.com/terramar-costa-blanca/) "buying, selling, and managing properties in the Xàbia area and its surroundings", ruim 25 jaar actief; volgens R06 bouwt en verkoopt het kantoor ook eigen nieuwbouw en doet het projectmanagement. Op de homepage: nieuwbouw, "proyecto con licencia", investeringsobjecten, vakantieverhuurbeheer.

## Advies: **feed vragen**

1. **Niet zelf lezen.** De Paagees Shield houdt een gewone automatische lezer tegen, ook al staat robots.txt het toe. Dat de standaard ophaaltool van dit platform er bij de homepage doorheen kwam, is geen toestemming en geen stabiele basis (zelfde lijn als de verslagen paradiserealestate.es en javeaimmo.com).
2. **Voorwaarden zijn niet gelezen;** zusterkantoren op hetzelfde platform verbieden commerciële reproductie. Alleen intern signaleren, nooit teksten of foto's overnemen.
3. **De nette weg bestaat al:** Sooprema-API via het kantoor. Vraag Terramar of de gegevens van zijn **eigen** objecten (prijs, m², perceel, plaats, referentie, link) alleen-lezen naar TREE mogen — geen objecten van collega's (juridische lijn R04 §3.5).
4. Tot die tijd: handmatig kijken in een browser op https://www.terramar.es/propiedades/venta/todas/ (filter Obra Nueva; let op "para reformar" en "parcela"). Werkt het kantoor niet mee: overslaan.

⏸️ ACTIE VOOR JAN: beslis of TREE Terramar (Jávea Puerto, bouwt en verkoopt zelf, renovatie- en perceelobjecten) benadert voor een Sooprema-feed van het eigen aanbod. Conceptbericht pas na jouw akkoord.

## Opgehaalde pagina's (24-09-2026)

1. https://www.terramar.es/robots.txt (curl, 200, echte robots.txt)
2. https://www.terramar.es/ (curl, 200, Shield-pagina 5.882 bytes)
3. https://www.terramar.es/sitemap.xml (curl, 200, Shield-pagina)
4. https://www.terramar.es/ (curl, alleen koppen; `server: nginx`, `x-robots-tag: noindex, nofollow`)
5. https://www.terramar.es/sitemap.xml (standaard ophaaltool → 301 naar `/sitemap.xml/`, niet gevolgd)
6. https://www.terramar.es/ (standaard ophaaltool, leesbare tekst van de echte homepage)
Extern: https://archive.org/wayback/available?url=terramar.es (geen kopie) · https://en.javea.com/zona/comercios/inmobiliaria/agencia-inmobiliaria/ (bedrijvengids).
Lokale bronnen: `onderzoek/R06-makelaars-javea-register.md` (#37), `R06-…verificatie.md` (A13, F2), `onderzoek/B01-crm-feeds.md` (§2.2–2.4), verslagen `site-calablanca.com.md`, `site-giuliano-villas.com.md`, `site-paradiserealestate.es.md`, `site-javeaimmo.com.md`.

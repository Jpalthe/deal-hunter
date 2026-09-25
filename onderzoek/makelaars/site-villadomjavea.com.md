# Villadom Immo Jávea — toets op automatisch lezen

- **Website:** https://www.villadomjavea.com
- **Datum toets:** 24-09-2026 (23:43–23:45 CEST; servertijd 21:43–21:44 UTC in de antwoordheaders)
- **Kantoor:** Jávea, Av. Fontana 8 (Arenal) — bron: kantorenlijst K01 (spainhouses.net, 24-09-2026).
  **Niet bevestigd op de site zelf** (die was niet leesbaar, zie hieronder).
- **Algemene contactkanalen:** niet vastgesteld (site niet leesbaar zonder botcontrole).
- **Verzoeken aan de site (3, met 57 s en 15 s ertussen; crawl-delay 14 s gerespecteerd):**
  `/robots.txt` (echt bestand), `/` (alleen botcontrole-pagina), `/sitemap.xml` (alleen botcontrole-pagina).
  Geen inlog, geen formulier, geen browser nagebootst, geen rekenpuzzel opgelost, geen andere user-agent geprobeerd.

## Advies: FEED VRAGEN

In één zin: robots.txt staat lezen toe, maar de site zet een JavaScript-botcontrole ("Paagees Shield") vóór
elke pagina, ook vóór de sitemap, en die houdt een gewone automatische lezer tegen. Omzeilen doen we niet —
dat is de stopregel. Villadom draait op de Paagees-weblaag en zo'n site wordt per definitie gevoed door een
XML- of API-feed uit het CRM van het kantoor (B01 §2.3, paagees.com, 16-09-2026). Die feed bestaat dus al;
de nette weg is het kantoor vragen of een kopie ervan naar ons mag.

Wat ik daardoor **niet** heb kunnen vaststellen: de gebruiksvoorwaarden, de sitemap, hoe een objectpagina
eruitziet (JSON-LD, og-tags), het aantal objecten en het aandeel Jávea/Benitachell/Moraira. Die velden staan
hieronder eerlijk op "onbekend".

## 1. robots.txt — lezen toegestaan, met beperkingen

- URL: https://www.villadomjavea.com/robots.txt (HTTP 200, `server: Apache`, `last-modified: 07-01-2025`,
  5.717 bytes, 421 regels; opgehaald 24-09-2026 21:43 UTC).
- Dit bestand kwam wél gewoon door (van Apache); de HTML-pagina's komen van een nginx-laag met de botcontrole.
- Het blok voor iedereen, letterlijk (regels 2–25):

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

- Helemaal onderaan (regels 420–421) staat een tweede blok voor iedereen:

```
User-agent: *
Crawl-delay: 14
```

- Daartussen: ruim honderd blokken die specifieke bots volledig uitsluiten (`Disallow: /`), waaronder
  `Python-urllib`, `wget`/`Wget`, `Teleport`, `WebZip`, `Offline Explorer`, `WebCopier`, `EmailCollector`.
  Dat is de bekende lijst van download- en e-mailoogsttools; een bot die zich zelf netjes benoemt valt onder `*`.
- **Geen `Sitemap:`-regel.**
- Uitleg in gewone taal: een gewone bot **mag de aanbod- en objectpagina's lezen** (`Allow: /`), maar
  - **niet** de vervolgpagina's van een aanbodlijst (`/*/*/*/pagina/*`, `/page/*`, `/seite/*` enz. — dus alleen
    pagina 1 van elke lijst; de rest moet via objectlinks of een sitemap),
  - **niet** de formulieren, galerij-vensters, printversies en `/images/`,
  - en **niet sneller dan één verzoek per 14 seconden** (`Crawl-delay: 14`). Bij bijvoorbeeld 150 objecten is
    dat ruim 35 minuten per volledige ronde.
- Oordeel robots.txt: **deels toegestaan** — inhoud ja, paginering nee, tempo begrensd.

## 2. Gebruiksvoorwaarden — niet gevonden (niet leesbaar)

- Elke HTML-pagina van de site zit achter de botcontrole (zie 3). De aviso legal / voorwaarden kon ik daardoor
  niet ophalen en niet citeren. Een pad gokken (bijv. `/aviso-legal/`) zou alleen weer de controlepagina geven.
- Status: **niet gevonden**. Bij Javea Immo, ook een Paagees-site, verbood de aviso legal reproductie voor
  commerciële doeleinden zonder toestemming (verslag site-javeaimmo.com.md, 24-09-2026). Of Villadom dezelfde
  tekst gebruikt is **[te verifiëren]**; niet aannemen.

## 3. Sitemap — niet bereikbaar

- https://www.villadomjavea.com/sitemap.xml (24-09-2026 21:44 UTC): HTTP 200, maar `content-type: text/html`,
  5.882 bytes, byte-voor-byte identiek aan het antwoord op de homepage. Het is de botcontrole-pagina, geen sitemap.
- Headers van dat antwoord: `server: nginx`, `x-robots-tag: noindex, nofollow`, `cache-control: no-store`.
- `/sitemap_index.xml` niet geprobeerd: dat had hetzelfde antwoord gegeven en het budget is beperkt.
- **Aantal object-URL's: onbekend.**

## 4. Aanbodpagina en objectpagina — niet geopend (stopregel)

- Wat de botcontrole precies is, uit de opgehaalde pagina zelf (24-09-2026):
  - Titel "Security Check", tekst "Verifying your browser — This is an automatic security check",
    voettekst "Powered by Paagees Shield", melding "JavaScript is required to access this site".
  - Het script laat de browser een SHA-256-rekenpuzzel oplossen (een hash met 5 leidende hex-nullen zoeken,
    in porties van 2.000 pogingen), zet daarna een cookie `__shield=<id>.<oplossing>` (1 uur geldig,
    `Secure`, `SameSite=Lax`) en herlaadt de pagina. Zonder JavaScript én cookies kom je er niet door.
  - Dit is botdetectie. Die puzzel programmatisch oplossen of een browser nabootsen om erdoor te komen is
    omzeilen, en dat doen we niet. Hier is dus gestopt.
- Gevolg: **JSON-LD, og-tags, prijs, oppervlakte, perceel, plaats en referentie: onbekend.**
- Kanttekening voor Jan: in het verslag over javeaimmo.com kwam de standaard-ophaaltool van dit platform wél
  langs de Shield. Hier bewust niet geprobeerd, omdat niet vast te stellen is óf die tool erdoor komt doordat
  Paagees hem toelaat, óf doordat hij de puzzel oplost — en dat laatste zou omzeilen zijn. Als Jan dat anders
  weegt, is het een keuze voor hem, niet voor het script.

## 5. Systeem achter de site — Paagees-weblaag, onderliggend CRM onbekend

- "Powered by Paagees Shield" op de controlepagina; `server: nginx` voor de HTML, `server: Apache` voor robots.txt.
- De robots.txt is het standaardbestand van Paagees: exact dezelfde paden (`/html/formulario/48horas/`,
  `/html/formucontraoferta/`, `/html/galeriamodal/`, `/portal/proceso/`) staan in de robots.txt van negen andere
  sites in deze map (o.a. arluxuryliving.com, calablanca.com, javeahomes.com, giuliano-villas.com, villalux.com,
  terramar.es; verslagen van 24-09-2026). Het pad `/giuliano/proceso/enviar/` is dus een sjabloonrestant, geen
  aanwijzing over Villadom zelf.
- Paagees (Dénia) is **geen CRM maar een weblaag** die zich koppelt aan Inmovilla, Inmoweb, Sooprema, Mobilia,
  Inmogesco, Inmotek, Witei, Casafari of "cualquier CRM con XML o API" (B01 §2.3, paagees.com, 16-09-2026).
  B01 §2.3 en de tabel in B01 noemen Villadom al als Paagees-kantoor in Jávea.
- Welk CRM daarachter zit is hier **niet** vast te stellen (geen html-commentaar, css-paden of cookies van de
  echte site gezien). Geen sporen van WordPress, Inmoweb, Mediaelx/LetsINMO, Inmovilla of Witei in wat wél
  leesbaar was — maar dat was alleen robots.txt en de controlepagina, dus dat zegt weinig.

## 6. Omvang en dekking Jávea / Benitachell / Moraira — onbekend

- Aantal objecten: **niet meetbaar** (geen aanbodpagina, geen sitemap).
- Dekking: **niet meetbaar**. Het kantoor zit in Jávea-Arenal en de naam en het domein wijzen op Jávea als
  kerngebied; dat is een aanname op basis van naam en adres, geen telling. Volgens de K01-lijst kwam het
  kantoor via spainhouses.net in beeld, dus (een deel van) het aanbod staat vermoedelijk ook op dat portaal
  [te verifiëren].

## ⏸️ ACTIE VOOR JAN

1. Villadom benaderen met de vraag of de XML/API-feed die hun website al voedt ook naar TREE mag
   (zelfde vraag als bij de andere Paagees-kantoren in B01 §2.3). Dat is de enige nette leesroute.
2. Beslissen of de kanttekening in punt 4 (standaard-ophaaltool die bij Javea Immo wél doorkwam) een route is
   die hij wil — het script neemt die beslissing niet.
3. Als het kantoor liever niet levert: aanbod van Villadom via de portalen (spainhouses.net [te verifiëren],
   idealista/Kyero) meenemen in plaats van via de eigen site.

## Verzoekenlijst (volledig)

| # | Tijd (UTC) | URL | Antwoord |
|---|---|---|---|
| 1 | 21:43:15 | https://www.villadomjavea.com/robots.txt | 200, text/plain, 5.717 B — echte robots.txt (Apache) |
| 2 | 21:44:12 | https://www.villadomjavea.com/ | 200, text/html, 5.882 B — "Security Check / Paagees Shield" (nginx) |
| 3 | 21:44:27 | https://www.villadomjavea.com/sitemap.xml | 200, text/html, 5.882 B — identiek aan #2 |

User-agent bij alle drie: `TREE-DealHunter-check/1.0 (+contact via tree.es; respecteert robots.txt en crawl-delay)`.
Ruwe bestanden: `/private/tmp/claude-501/-Users-root-admin-tree-es/a3ae9710-3e66-42bb-b602-476120d4027d/scratchpad/villadom/`.

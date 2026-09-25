# Paradise Real Estate (Paradise Property Solutions) — paradiserealestate.es: toets op automatisch lezen

**Kantoor:** Paradise Real Estate (Paradise Property Solutions), Jávea — Av. de la Libertad 5 / bl. 5 47C (bron: `K01-kantoren-javea.json`, gemeentelijst xabia.org/ver/2098, 24-09-2026). Website https://www.paradiserealestate.es (er bestaat ook paradiserealestate.co.uk; niet bekeken).
**Datum toets:** 24-09-2026, 23:19–23:21 lokale tijd (21:19–21:21 UTC volgens de serverkoppen). Drie verzoeken aan de site, nooit sneller dan één per twee seconden, eerlijke eigen User-Agent (`TREE-DealHunter-check/1.0`), geen inlog, geen formulieren, geen cookies.
**Webzoeken:** niet beschikbaar in deze sessie (zoekbudget op); alles hieronder komt van de site zelf en van eerdere verslagen in deze map.

## Advies in één zin

**Feed vragen.** robots.txt staat lezen toe, maar de site zet vóór elke HTML-pagina een JavaScript-botcontrole ("Paagees Shield") die een gewone automatische lezer tegenhoudt. Die omzeilen we niet, dus voorwaarden, sitemap, aanbod en objectpagina's konden niet bekeken worden. De site draait op de Paagees-weblaag, die gevoed wordt door een XML/API-feed uit het CRM van het kantoor (zie punt 5) — die feed bestaat dus al en is de nette weg.

## 1. robots.txt — toegestaan, met beperkingen (maar zie punt 3 en 4)

Bron: https://www.paradiserealestate.es/robots.txt (HTTP 200, 5.717 bytes, `Last-Modified` 07-01-2025, server **Apache**, opgehaald 24-09-2026 21:19 UTC).

Voor `User-agent: *` staat letterlijk:

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

- **Uitleg:** een `User-agent: *` mag de aanbodpagina's en objectpagina's lezen (`Allow: /`). Níet toegestaan: vervolgpagina's van lijsten (`/*/*/*/page/*` en de vertalingen daarvan), printversies, formulieren en de fotogalerij-modal. Geen `Crawl-delay`.
- Daarnaast 131 regels `Disallow: /` voor met naam genoemde bots (enkele dubbel), onder meer `Wget`, `Python-urllib`, `httplib`, `lwp-trivial`, `WebCopier`, `Offline Explorer`, `EmailCollector`, `TurnitinBot`. Signaal: massaal kopiëren is ongewenst; een lezer die zich eerlijk onder eigen naam meldt valt onder de `*`-regels.
- **Geen `Sitemap:`-regel.**
- Dit bestand is byte-voor-byte even groot (5.717 bytes) als dat van arluxuryliving.com en heeft hetzelfde `*`-blok als calablanca.com en costablancajaveaproperties.com (Giuliano Villas) — het sjabloon van het Sooprema/"Mattis"-platform (zie het verslag over Calablanca, punt 5). De regel `/giuliano/proceso/enviar/` is een overblijfsel uit dat sjabloon, niet iets van dit kantoor.

## 2. Gebruiksvoorwaarden — niet gevonden (niet bereikbaar)

De homepage (en daarmee de voettekst met een eventuele link naar aviso legal / voorwaarden) was niet leesbaar: zie punt 4. Binnen de opdracht ("stop zodra iets niet mag") is niet naar `/aviso-legal/` of vergelijkbare adressen geraden; die zouden dezelfde controlepagina geven. Conclusie: **geen vindbaar verbod op automatisch lezen, maar ook geen toestemming.** Let op: bij een zusterkantoor op hetzelfde platform (javeaimmo.com) verbiedt de aviso legal commerciële reproductie van de inhoud zonder toestemming; of dat hier ook zo is, is **[te verifiëren]**.

## 3. Sitemap — niet beschikbaar

- Geen `Sitemap:`-regel in robots.txt.
- https://www.paradiserealestate.es/sitemap.xml → HTTP 200, maar **geen XML**: 5.882 bytes HTML met `<title>Security Check</title>`, server **nginx**, koppen `cache-control: no-store, no-cache, must-revalidate` en `x-robots-tag: noindex, nofollow` (24-09-2026 21:19 UTC). Nul `<loc>`-vermeldingen.
- `/sitemap_index.xml` niet geprobeerd (zou dezelfde controlepagina geven). **Aantal object-URL's: niet vast te stellen.**

## 4. Aanbodpagina en objectpagina — geblokkeerd door "Paagees Shield"

- https://www.paradiserealestate.es/ → HTTP 200, exact dezelfde 5.882 bytes als bij de sitemap: kop "Verifying your browser", tekst "This is an automatic security check. You will be redirected shortly.", voettekst "Powered by Paagees Shield", en in `<noscript>` de melding dat JavaScript vereist is (24-09-2026 21:20 UTC).
- Wat de controle doet (uit het script op die pagina): de browser moet een SHA-256-rekenpuzzel oplossen (een hash vinden die met 5 hexadecimale nullen begint, gemiddeld ruim een half miljoen pogingen), zet dan een cookie `__shield=…` (1 uur geldig, `Secure`, `SameSite=Lax`) en laadt de pagina opnieuw. Zonder JavaScript én cookies kom je er niet doorheen. Of de controle ook voor gewone browsers verschijnt of alleen voor onbekende clients, is niet vastgesteld — dat testen zou neerkomen op een browser nabootsen, en dat doen we niet.
- Gevolg: **geen aanbodpagina en geen objectpagina gezien.** `<script type="application/ld+json">`, og-tags, prijs, oppervlakte, perceel, plaats en referentie: **onbekend.** Opvallend: robots.txt komt wél rechtstreeks van de Apache-server erachter, de HTML-pagina's van de nginx-laag ervoor.

## 5. Systeem achter de site — Paagees-weblaag, onderliggend CRM te verifiëren

Aanwijzingen (24-09-2026):
- HTML-pagina's: server `nginx`, botcontrole "Powered by Paagees Shield" (cookie `__shield`).
- robots.txt: server `Apache`, het Sooprema/Mattis-sjabloon (paden `/html/formulario/`, `/html/galeriamodal/`, `/portal/proceso/`, meertalige `page/seite/stranitsa/siden` en `print/drucken/imprimer/afdrukken`). Bij calablanca.com hoort precies dit sjabloon bij `Mattis-Framework 4.0` met een voettekstlink naar Sooprema.
- Paagees is volgens eerder onderzoek (B01 §2.3, paagees.com, 16-09-2026; zie ook het verslag over javeaimmo.com) **geen CRM maar een weblaag** die zich via XML of API koppelt aan Inmovilla, Inmoweb, Sooprema, Mobilia, Inmogesco, Inmotek, Witei, Casafari of elk ander CRM met XML/API.
- Geen html-commentaar, css-paden of cookies van de eigenlijke site gezien (Shield). Geen sporen van WordPress, Inmoweb, Mediaelx/LetsINMO, Inmovilla of Witei in wat wél leesbaar was.

Conclusie: **Paagees-weblaag met daaronder vermoedelijk Sooprema** (op grond van robots.txt) **[te verifiëren]**. Hoe dan ook wordt de site al gevoed door een XML/API-feed uit het CRM; een exportfeed bestaat dus.

## 6. Schatting aanbod en dekking Jávea/Benitachell/Moraira — niet vast te stellen

- **Aantal objecten:** onbekend; geen sitemap, geen lijstpagina leesbaar, geen webzoeken beschikbaar.
- **Dekking:** onbekend. Het kantoor zit in Jávea en staat op de gemeentelijke lijst van Xàbia (xabia.org/ver/2098, 24-09-2026), dus een overwegend Jávea-gericht aanbod ligt voor de hand **[te verifiëren]**.

## Advies: **feed vragen**

1. Niet zelf lezen: de Paagees Shield houdt een gewone automatische lezer tegen, ook al staat robots.txt het toe. Dat een andere ophaaltool er bij een zustersite een keer doorheen kwam (verslag arluxuryliving.com) is geen toestemming en geen stabiele basis; het gaat in tegen de bedoeling van die controle.
2. De voorwaarden zijn niet gelezen; bij een zusterkantoor op hetzelfde platform verbiedt de aviso legal commerciële reproductie. Ga er niet van uit dat teksten en foto's vrij herbruikbaar zijn.
3. De website wordt al gevoed door een XML/API-feed uit het CRM (Paagees). De vraag aan het kantoor is dus niet "kunt u iets bouwen", maar "mag de feed die uw site al voedt ook naar TREE, alleen om te lezen".
4. Tot die tijd: alleen handmatig kijken in een browser. Als het kantoor niet meewerkt: overslaan.

⏸️ ACTIE VOOR JAN: Paradise Real Estate benaderen (kantoor Av. de la Libertad, Jávea; algemene contactgegevens staan op de site zelf, alleen in een browser te zien) met de vraag om een kopie van de aanbodfeed (XML/API uit hun CRM via Paagees) voor eigen gebruik door TREE, met de afspraak: alleen lezen, niet herpubliceren. Pas na jouw "ja" wordt er iets verstuurd (regel 2).

## Verzoekenlogboek (24-09-2026, chronologisch, telkens > 2 s ertussen)

| # | URL | Client | Tijd (UTC) | Resultaat |
|---|---|---|---|---|
| 1 | https://www.paradiserealestate.es/robots.txt | curl, eigen User-Agent | 21:19:17 | 200, echte robots.txt (Apache, 5.717 bytes) |
| 2 | https://www.paradiserealestate.es/sitemap.xml | curl, eigen User-Agent | 21:19:36 | 200, controlepagina Paagees Shield (nginx, 5.882 bytes), geen XML |
| 3 | https://www.paradiserealestate.es/ | curl, eigen User-Agent | 21:20:49 | 200, identieke controlepagina Paagees Shield |

Daarna gestopt: elke verdere HTML-pagina zou dezelfde controle geven en de opdracht zegt te stoppen zodra iets niet mag. Twee van de vijf toegestane verzoeken ongebruikt gelaten. Geen browser gebruikt, geen JavaScript uitgevoerd, geen cookie gezet, geen andere User-Agent geprobeerd.

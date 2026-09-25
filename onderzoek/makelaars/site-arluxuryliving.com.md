# AR Luxury Living — arluxuryliving.com: toets op automatisch lezen

**Kantoor:** AR Luxury Living (Antonio Roselló Luxury Living), Jávea — website https://www.arluxuryliving.com
**Datum toets:** 24-09-2026 (alle verzoeken tussen 23:00 en 23:15 lokale tijd; 5 verzoeken aan de site, nooit sneller dan één per twee seconden)
**Bron kantoorgegevens:** `K01-kantoren-javea.json` en `K02-kantoren-benitachell-moraira.json` in deze map (24-09-2026).
**Verzoeker:** TREE Deal Hunter, toets op automatisch lezen (subagent).

## Advies in één zin

**Lezen mag volgens robots.txt, maar de site zit achter een bot-controle ("Paagees Shield") die een gewone HTTP-client niet doorlaat.** Alleen een client die de site zelf toelaat (zoals de WebFetch-lezer van dit platform, die er zonder kunstgrepen doorkwam) kan de pagina's lezen. Advies: **lezen**, uitsluitend met de voorwaarden onderaan; zodra de controlepagina verschijnt niet omzeilen maar het kantoor om een feed vragen.

## 1. robots.txt — toegestaan, met beperkingen

Bron: https://www.arluxuryliving.com/robots.txt (HTTP 200, 5.717 bytes, 421 regels na omzetting van CR-regeleinden, opgehaald 24-09-2026).

Het bestand begint met een blok voor alle bots dat het lezen toestaat (`Allow: /`) maar formulieren, galerij-modals, printversies en **paginanummer-URL's** afsluit. Letterlijk:

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

Daarna volgen **129 met naam genoemde bots die volledig geblokkeerd zijn** (`Disallow: /`), waaronder Python-urllib, Wget, HTTrack, WebZip, WebCopier, Teleport, larbin en e-mailverzamelaars (curl staat er niet bij). Het bestand eindigt met een tempo-eis voor iedereen:

```
User-agent: *
Crawl-delay: 14
```

**Oordeel:** een `User-agent: *` mag de aanbod- en objectpagina's lezen (`Allow: /`), maar niet de vervolgpagina's van lijsten (`pagina/page/seite/...`), geen printversies, geen formulieren — en hooguit **één verzoek per 14 seconden**. Er staat **geen Sitemap-regel** in. De eigenaar sluit met dit bestand nadrukkelijk kopieer- en scraperprogramma's uit; een net, langzaam lezende bot wordt niet uitgesloten.

## 2. Gebruiksvoorwaarden — niet gevonden

- De homepage (https://www.arluxuryliving.com/) gaf met een gewone HTTP-client alleen de controlepagina "Security Check / Verifying your browser — Powered by Paagees Shield" (HTTP 200, 5.882 bytes, header `x-robots-tag: noindex, nofollow`). Daardoor is de voettekst met eventuele juridische links niet leesbaar.
- Op de enige inhoudspagina die wél leesbaar was (zie punt 4) stonden **geen links** naar aviso legal, voorwaarden, privacy of cookies, en **geen tekst** over scraping of automatisch lezen.
- Er is dus **geen verbod gevonden**, maar ook geen voorwaardenpagina gelezen. Status: **niet gevonden** — bij een volgende ronde met een toegelaten client eerst de voettekst van de homepage bekijken.

## 3. Sitemap — onbereikbaar

- robots.txt noemt geen sitemap.
- https://www.arluxuryliving.com/sitemap.xml gaf HTTP 200 maar met de controlepagina van Paagees Shield in plaats van XML (24-09-2026). `/sitemap_index.xml` is niet geprobeerd (verzoekbudget).
- Aantal object-URL's in de sitemap: **onbekend**.

## 4. Aanbodpagina en objectpagina

**Aanbodpagina gelezen:** https://www.arluxuryliving.com/en/villas-for-sale-cumbre-del-sol-benitachell/ (via de WebFetch-lezer van dit platform, 24-09-2026; die kwam zonder aanpassingen door de controle — de site laat die client kennelijk toe).

Wat er stond: **8 objecten** in Benitachell / Cumbre del Sol. De eerste vijf:

| Referentie | Vraagprijs | Plaats | Kenmerken | URL |
|---|---|---|---|---|
| 6232BELL | € 2.720.000 | Benitachell – Cumbre del Sol | 4 slaapkamers, 832 m² | https://www.arluxuryliving.com/en/for-sale/-modern-new-build-villa-for-sale-in-benitachell-with-sea-views-6232bell/ |
| DG5140/4038 | € 2.179.000 | Benitachell – Cumbres del Sol | 3 slaapkamers, 542 m² | https://www.arluxuryliving.com/en/for-sale/villa-for-sale-in-benitachell-dg51404038/ |
| 4043BELL | € 2.150.000 | Benitachell – Cumbre del Sol | 4 slaapkamers, 387 m² | https://www.arluxuryliving.com/en/for-sale/-luxury-villa-with-sea-views-for-sale-in-cumbre-del-sol-4043bell/ |
| 4178BELL | € 2.073.000 | Benitachell – Cumbre del Sol | 3 slaapkamers, 615 m² | https://www.arluxuryliving.com/en/for-sale/4178jav-unique-new-build-villa-for-sale-with-sea-views-in-cumbre-del-sol-4178bell/ |
| MRD5-231 | € 1.429.000 | Benitachell – Cumbre del Sol | 4 slaapkamers, 177 m² | https://www.arluxuryliving.com/en/for-sale/villa-for-sale-in-benitachell-el-poble-nou-de-benitatxell-mrd5-231/ |

(De m²-waarden komen uit de lijstweergave; of het woon- of perceeloppervlak is, is niet vastgesteld.)

**Objectpagina:** niet geopend — het budget van vijf verzoeken was op. Daarom is **onbekend** of er `<script type="application/ld+json">` en `og:`-metatags op een objectpagina staan. Voorbeeld-URL om in een volgende ronde te openen: https://www.arluxuryliving.com/en/for-sale/villa-for-sale-in-benitachell-dg51404038/

**Opvallend:** de referenties dragen een plaatscode (…BELL = Benitachell, …JAV = Jávea) en er komen ook referenties met andere voorvoegsels voor (DG…, MRD5-…). Dat wijst mogelijk op objecten van samenwerkende kantoren in het aanbod **[te verifiëren]**.

Menu op de aanbodpagina noemt zeven gebieden: Jávea, Moraira, Altea, Calpe, Dénia, Benissa, Benitachell. Geen bedrijfsadres of telefoonnummer zichtbaar in de gelezen pagina.

## 5. Systeem achter de site — onbekend

- HTML van de site was met een gewone client niet leesbaar (controlepagina), dus geen commentaar, css-paden of cookies bekeken.
- Bekende aanwijzingen: server `nginx`; beveiliging "Paagees Shield" (zet via JavaScript een cookie `__shield`, geldig 1 uur, en laadt de pagina dan opnieuw); URL-patronen `/en/villas-for-sale-<gebied>/` en `/en/for-sale/<omschrijving>-<referentie>/`; robots.txt met meertalige paden (`pagina/pages/page/seite/stranitsa/siden`, `imprimir/print/drucken/imprimer/afdrukken`) en paden als `/html/formulario/`, `/portal/proceso/`, `/giuliano/proceso/enviar/`.
- Dit is geen standaard WordPress-, Inmoweb-, Sooprema-, Inmovilla- of Witei-handtekening die ik met zekerheid herken. **CMS: onbekend** (waarschijnlijk een Spaanse makelaars-CMS op maat of van een klein bureau; niet bevestigd).

## 6. Schatting omvang en dekking

- **Totaal aanbod: onbekend.** Slechts één van de zeven gebiedspagina's is gelezen (Benitachell: 8 objecten). Een totaal noemen zou gissen zijn.
- **Dekking doelgebied:** het menu bevat drie van onze doelgebieden (Jávea, Benitachell, Moraira) naast vier andere (Altea, Calpe, Dénia, Benissa). De 8 gelezen objecten liggen allemaal in Benitachell (Cumbre del Sol); de referentiecodes (…BELL, …JAV) doen vermoeden dat Jávea en Benitachell kerngebieden zijn **[te verifiëren]**. Prijsniveau van het gelezen aanbod: € 1,4–2,7 miljoen — luxe segment.

## Logboek van verzoeken (24-09-2026)

| # | URL | Client | Uitkomst |
|---|---|---|---|
| 1 | /robots.txt | curl, eigen user-agent | 200, echte inhoud |
| 2 | /robots.txt (herhaald ter controle, bestand was lokaal overschreven) | curl | 200, echte inhoud |
| 3 | /sitemap.xml | curl | 200, controlepagina Paagees Shield |
| 4 | / (homepage) | curl | 200, controlepagina Paagees Shield |
| 5 | /en/villas-for-sale-cumbre-del-sol-benitachell/ | WebFetch | echte inhoud, 8 objecten |

Niets omzeild: geen cookies nagebootst, geen browser-user-agent voorgewend, geen JavaScript-controle uitgevoerd.

## Voorwaarden als we gaan lezen

1. Hooguit **één verzoek per 14 seconden** (Crawl-delay), met een eerlijke, herkenbare user-agent en contactadres.
2. Alleen gebiedspagina's en objectpagina's; **geen** paginanummer-URL's, printversies, galerij-modals of formulier-URL's (verboden in robots.txt).
3. Verschijnt de controlepagina "Verifying your browser": **stoppen**, niet omzeilen. Dan het kantoor vragen om een XML-feed of samenwerking.
4. Eerst de voorwaardenpagina in de voettekst lezen zodra die met een toegelaten client zichtbaar is; verbiedt die het automatisch lezen, dan alsnog overstappen op "feed vragen".

⏸️ ACTIE VOOR JAN: geen directe actie. Als de eerste leesronde op de controlepagina strandt, is het aan jou om AR Luxury Living om een feed of samenwerking te vragen (het kantoor zit in dezelfde markt als TREE Properties).

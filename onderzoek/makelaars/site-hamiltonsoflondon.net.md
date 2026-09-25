# Toets automatisch lezen: Hamiltons of London (Jávea) — hamiltonsoflondon.net

Datum toets: 24-09-2026 · Door: TREE Deal Hunter (agent) · Verzoeken aan de site: 5 (maximum)

## Advies in één zin

**Feed vragen.** De site staat achter een bot-schild ("Paagees Shield") dat scripts een
JavaScript-rekenpuzzel voorschotelt in plaats van de pagina. Dat omzeilen we niet. Het
systeem erachter (Sooprema) heeft wél een API en publiceert automatisch naar 70+ portalen,
dus vraag het kantoor om een feed of kijk op de portalen.

## Wie is dit

- Bedrijf: INMO HAMILTONS REAL ESTATE SL (op de site: "Hamiltons Real Estate", actief sinds 1999).
  Bron: https://www.hamiltonsoflondon.net/ (24-09-2026).
- Hoofdkantoor Moraira (Ctra. Moraira-Calpe 15, 03724 Moraira); kantoren in Altea, Calpe,
  Jalón en **Jávea (Av. Lepanto 13)**. Algemeen: tel. +34 966 491 883, WhatsApp +34 665 635 731,
  moraira@moraira-hamiltons.net. Bron: homepage, 24-09-2026.
- Het is één site voor het hele Hamiltons-netwerk (er is ook hamiltonsfranchise.com), niet
  alleen het kantoor Jávea. De referenties op de homepage hebben verschillende voorvoegsels
  (HB, HG, HS, SH, HI, HO) — mogelijk per kantoor/franchisenemer [interpretatie, te verifiëren].

## 1. robots.txt — deels toegestaan

Bron: https://www.hamiltonsoflondon.net/robots.txt (24-09-2026, HTTP 200, 421 regels, 133
User-agent-blokken, géén Sitemap-regel).

Voor `User-agent: *` geldt `Allow: /` met deze uitzonderingen (letterlijk):

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

Wat dat betekent: aanbod- en objectpagina's zijn voor een gewone bot niet uitgesloten;
formulieren, galerij-modals, printversies en (via jokertekens) paginering wél. Daarna volgen
132 blokken die specifieke tools volledig uitsluiten (`Disallow: /`), waaronder
`Python-urllib`, `Wget`, `httplib`, `lwp-trivial`, `WebZip`, `Teleport`, `EmailCollector`.
De strekking is duidelijk: generieke download-/scrapetools zijn niet welkom.
Het bestand oogt als een standaardsjabloon (paden als `/html/formulario/` en
`/portal/proceso/` bestaan op deze site niet) [observatie].

## 2. Gebruiksvoorwaarden — niet gevonden

De voettekst toont de labels "Legal notice", "Privacy Policy" en "Cookies Policy", maar in de
opgehaalde paginatekst stond geen adres achter die labels (vermoedelijk pop-ups). Binnen het
maximum van vijf verzoeken heb ik die pagina's niet kunnen openen. Of scraping daar
uitdrukkelijk verboden wordt is dus **niet vastgesteld**. Bron: homepage, 24-09-2026.

## 3. Sitemap — niet bereikbaar

- robots.txt bevat geen `Sitemap:`-regel.
- https://www.hamiltonsoflondon.net/sitemap.xml gaf op 24-09-2026 HTTP 200 maar **geen XML**:
  een HTML-pagina met titel "Security Check" (5.882 bytes, 0 `<loc>`-vermeldingen).
- /sitemap_index.xml niet geprobeerd (verzoekbudget + zelfde schild te verwachten).

## Het bot-schild (doorslaggevend)

Twee van mijn scriptverzoeken (sitemap.xml en /for-sale/price-asc/) kregen dezelfde
tussenpagina, letterlijk: "Verifying your browser" — "This is an automatic security check.
You will be redirected shortly." — "Powered by Paagees Shield" — en zonder JavaScript:
"JavaScript is required to access this site." De pagina laat de browser een SHA-256-rekenpuzzel
oplossen (5 nullen vooraan) en zet dan een cookie `__shield` (1 uur geldig), waarna de echte
pagina laadt. robots.txt zelf werd wél gewoon geleverd.

Ik heb de puzzel **niet** opgelost, geen browser nagebootst en geen cookie vervalst: dit is
een opzettelijke toegangsbeperking voor automatische lezers. Een scraper bouwen betekent dat
schild omzeilen — dat doen we niet. (Twee pagina's, de homepage en één objectpagina, kwamen
via de tekst-ophaler van de agent wél door zonder puzzel; het schild werkt dus per client,
maar de bedoeling van de site-eigenaar is helder.)

## 4. Aanbodpagina en objectpagina

- Aanbod te koop: https://www.hamiltonsoflondon.net/for-sale/price-asc/ (ook
  /properties-for-sale-javea/, /properties-for-sale-moraira/, /properties-for-sale-benitachell/,
  /villas-for-sale-javea/ enz.). Voor mijn script: geblokkeerd door het schild (24-09-2026).
- Objectpagina (tekstversie, 24-09-2026):
  https://www.hamiltonsoflondon.net/for-sale/newly-built-villa-under-construction-moraira-ho474703/
  — Ref. HO474703 · 1.490.000 € · 187 m² bebouwd · 969 m² perceel · 3 slaapkamers · 2 badkamers ·
  Moraira - Moravit · Villa · titel "Newly built villa under construction, Moraira".
- JSON-LD (schema.org) en og:-tags: **onbekend**. In de tekstversie waren ze niet zichtbaar,
  maar de ruwe HTML was voor een script niet op te halen (schild), dus ik kan niet zeggen dat
  ze ontbreken.

## 5. Systeem achter de site

- **Sooprema** (CRM/backend): voettekstlink naar sooprema.com en bestandspad
  `/crm/pages/agencies/hamiltons/assets/` op homepage én objectpagina (24-09-2026).
- Websitelaag door **Paagees** (Dénia): "Powered by Paagees Shield". Paagees noemt Sooprema
  als gekoppeld CRM ("+ cualquier CRM con XML o API"). Bron: https://www.paagees.com/ (24-09-2026).
- Sooprema biedt een REST-API (sleutel aanvragen via estate@sooprema.com; het kantoor moet
  actieve Sooprema-klant zijn) en publiceert automatisch naar "+70 portales" (Idealista,
  Fotocasa, Kyero, Pisos.com, Yaencontre). Bronnen: https://www.sooprema.com/ en
  https://www.sooprema.com/api-desarrolladores/ (24-09-2026).

## 6. Omvang en dekking Jávea/Benitachell/Moraira

Tellers op de homepage (24-09-2026): "Moraira: 64 · Jávea: 106 · Jalón: 38 · Calpe: 140 ·
Benissa Costa: 51 · Altea: 46" = **445** objecten in die zes gebieden. Daarnaast staan er
objecten in Dénia, Alfaz del Pi, Benidorm, Finestrat, Els Poblets en Orba (uitgelichte
objecten en landingspagina's) zonder teller, en Benitachell heeft een eigen pagina zonder
teller. Het totaal ligt dus **boven 445** [schatting; exact aantal niet vastgesteld].

Jávea + Moraira = 170 van de 445 getelde objecten (≈ 38%); met Benitachell erbij iets meer,
op het (hogere) werkelijke totaal iets minder. Kortom: ruwweg een derde van het aanbod ligt in
ons doelgebied.

## Wat dit betekent voor Deal Hunter

1. Niet scrapen: bot-schild + expliciete uitsluiting van scrapetools in robots.txt.
2. Sooprema-kantoren publiceren doorgaans naar de grote portalen; het "verborgen aanbod"-
   argument is hier dus zwakker — controleer op Idealista/Kyero of Hamiltons daar volledig staat.
3. ⏸️ ACTIE VOOR JAN: als Hamiltons interessant blijft, vraag het kantoor Jávea (Av. Lepanto 13)
   om een XML-feed of samenwerking (Sooprema kan dat leveren). Zonder hun "ja" doen we niets.

## Verzoekenlog (24-09-2026)

1. GET /robots.txt — 200, tekst (script)
2. GET /sitemap.xml — 200, schildpagina (script)
3. GET / — echte pagina (tekst-ophaler)
4. GET /for-sale/price-asc/ — 200, schildpagina (script)
5. GET /for-sale/newly-built-villa-under-construction-moraira-ho474703/ — echte pagina (tekst-ophaler)

Buiten de site: paagees.com, sooprema.com, sooprema.com/api-desarrolladores/ (tekst-ophaler).
Websearch was niet beschikbaar (sessiebudget op); niets uit het geheugen aangevuld.

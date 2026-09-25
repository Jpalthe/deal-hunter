# Javea Casas — www.javeacasas.com

**Toets op automatisch lezen · 24-09-2026 (ca. 21:45–21:55 UTC)**
Onderzoek voor TREE Deal Hunter. Zeven verzoeken aan de site, waarvan vijf inhoudspagina's (robots.txt, homepage, aanbodpagina Jávea, legal notice, één objectpagina); de twee overige (homepage en /sitemap.xml met curl) gaven alleen de botcontrolepagina. Minimaal 14 seconden tussen de curl-verzoeken (Crawl-delay), de overige verzoeken één voor één. Niets omzeild, niet ingelogd, geen formulieren. Zoekmachinebudget van deze sessie was op; alles komt van de site zelf en van eerdere verslagen in deze map.

## Kort

- **robots.txt:** een gewone bot mag de objectpagina's lezen ("deels": bladerpagina's, formulieren, galerij- en printversies zijn verboden; 14 s wachttijd).
- **In de praktijk:** vóór elke HTML-pagina staat een JavaScript-botcontrole ("Powered by Paagees Shield") die een gewone HTTP-client tegenhoudt. Die omzeilen we niet.
- **Voorwaarden:** geen letterlijk scrapingverbod, wél een verbod op reproductie en op gebruik voor commerciële doeleinden zonder toestemming.
- **Systeem:** Sooprema (CRM/website) met de Paagees-weblaag/Shield ervoor — een systeem met een exportroute.
- **Aanbod:** tellers op de homepage: 124 objecten Jávea, 87 Dénia; Moraira en Benitachell hebben eigen pagina's maar zonder zichtbare teller. Het grootste deel is gedeeld aanbod van andere Sooprema-kantoren; het eigen aanbod (referenties "JC-…") is klein.

**Advies: feed vragen.** Zelfde lijn als bij Terramar, Javea Immo en Crown Property (verslagen 24-09-2026): robots.txt zegt "mag", de Shield zegt "alleen echte browsers", en Sooprema kent een API/feed die via het kantoor loopt.

## 1. robots.txt — mag een gewone bot de aanbodpagina's lezen?

Bron: https://www.javeacasas.com/robots.txt (opgehaald 24-09-2026 ca. 21:45 UTC, HTTP 200, 421 regels).

**Ja, grotendeels ("deels").** Voor `User-agent: *` staat `Allow: /` met deze uitzonderingen (letterlijk):

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

en helemaal onderaan, in een tweede blok voor dezelfde `User-agent: *`:

```
User-agent: *
Crawl-delay: 14
```

Betekenis voor automatisch lezen:
- Objectpagina's (`/for-sale/…-jc-1062ab/`) en de aanbodpagina's per plaats zijn niet uitgesloten.
- **Doorbladeren is verboden** (`/*/*/*/pagina/*`, `/page/*`, `/seite/*` enz.): pagina 2, 3, … van het aanbod mag een bot niet openen. Een lezer moet dus via een sitemap werken.
- Formulieren, galerijvensters en printversies zijn verboden; `/images/` ook.
- **14 seconden** tussen opvragingen.
- Ruim honderd specifieke bots krijgen `Disallow: /`, onder meer `Python-urllib`, `Wget`, `wget`, `HTTrack 3.0`, `WebCopier`, `Offline Explorer`, `EmailCollector`. Een eigen lezer moet dus onder een eigen, herkenbare naam draaien.
- Geen `Sitemap:`-regel.

Dit is hetzelfde robots.txt-sjabloon als bij llidomarjavea.com, terramar.es, calablanca.com en javeahomes.com (verslagen 24-09-2026): het sjabloon van het Sooprema-platform.

**Belangrijk voorbehoud — wat robots.txt toestaat, houdt de server in de praktijk tegen.** Een gewone HTTP-client (curl, eigen herkenbare User-Agent `TREE-DealHunter-check/1.0`) kreeg op https://www.javeacasas.com/ (21:45:51 UTC) én op /sitemap.xml (21:46:05 UTC) geen inhoud maar een HTML-pagina van 5.882 bytes: titel "Security Check", kop "Verifying your browser", tekst "This is an automatic security check. You will be redirected shortly.", voettekst "Powered by Paagees Shield". Koppen: `server: nginx`, `x-robots-tag: noindex, nofollow`, `cache-control: no-store`. De pagina laat de browser een SHA-256-rekenpuzzel oplossen (5 leidende hex-nullen), zet dan een cookie `__shield` (1 uur geldig) en herlaadt. Zonder JavaScript en cookies kom je er niet doorheen. **Niet opgelost, niet omzeild.** De standaard ophaaltool van dit platform kreeg de pagina's wél gewoon binnen; dat is geen toestemming en geen stabiele basis voor een eigen lezer.

## 2. Gebruiksvoorwaarden — geen scrapingverbod, wél verbod op reproductie en commercieel gebruik

Bron: https://www.javeacasas.com/legal-notice/ (24-09-2026, ca. 21:52 UTC; pad afgeleid van het patroon `/legal-notice/` bij Engelstalige zustersites, bleek te kloppen). Eén pagina "Legal notice / Aviso legal y términos de uso" met daaronder General Terms of Use, Personal Data, User Commitments and Obligations, Security Measures, Complaints, Dispute Resolution Platform, Intellectual and Industrial Property Rights, External Links, Comments Policy, Exclusion of Warranties and Liability, Applicable Law and Jurisdiction, Privacy Policy en Cookies Policy. Aparte links: Privacy Policy, Cookies Policy.

- De woorden **scraping, robot, crawler, automated, extraction en database komen niet voor.** Er is dus geen expliciet verbod op automatisch lezen.
- Wél (samengevat uit de gelezen tekst): reproductie, distributie of wijziging van de inhoud, geheel of gedeeltelijk, vereist toestemming van de rechthebbenden; verboden is gebruik van de site voor onrechtmatige of schadelijke doeleinden, "use for commercial or advertising purposes", en handelingen die het portaal kunnen beschadigen, uitschakelen of overbelasten.
- Gevolg: alleen kale feiten intern signaleren (referentie, prijs, m², perceel, plaats, URL, datum). **Geen foto's en geen beschrijvingsteksten overnemen.**

Vertrouwelijkheid: de exploitant in de legal notice is een **natuurlijk persoon** (eenmanszaak) met een NIF van een natuurlijk persoon; naam en nummer bewust niet overgenomen. Kantooradres volgens de legal notice en de voettekst: **C/ Llidoner 474, 03730 Jávea (Alicante)**; algemene kanalen: sales@javeacasas.com, +34 654 976 836, openingstijden ma–vr 09:30–19:00, za 09:30–14:00. Het register R06 noemde "C/ Cicerón 8" (bron Javea Guide) — dat verschil is **[te verifiëren]**.

## 3. Sitemap

- robots.txt noemt geen sitemap.
- https://www.javeacasas.com/sitemap.xml met curl (24-09-2026 21:46 UTC) → HTTP 200, maar de inhoud is de Shield-pagina (byte-voor-byte gelijk aan de homepage-Shield), geen XML.
- `/sitemap_index.xml` niet geprobeerd (verzoekbudget). Met de standaard ophaaltool niet opnieuw geprobeerd: het budget ging naar voorwaarden, aanbodpagina en objectpagina.
- Aantal object-URL's in de sitemap: **niet vast te stellen.** (De vermelding "sitemap 200" in register R06 van 15-09-2026 was hoogstwaarschijnlijk ook de Shield-pagina met status 200.)

## 4. Aanbodpagina en objectpagina

**Aanbodpagina's** (uit de navigatie van de homepage, standaard ophaaltool, 24-09-2026):
- Alles te koop: https://www.javeacasas.com/for-sale/relevant/
- Per plaats: https://www.javeacasas.com/properties-for-sale-in-javea/ · /properties-for-sale-in-denia/ · /property-for-sale-in-moraira/ · /properties-for-sale-in-benitachell/
- Verder in het menu: New Construction, About us, Info, Blog, Contact; talen EN/ES/DE/FR/NL. Slogan "Turning houses into homes since 1999".

De pagina Jávea (opgehaald ca. 21:49 UTC) toont per kaart referentie, prijs, plaats, bebouwd m² óf perceel m² en de link; gesorteerd op prijs oplopend. Eerste 15 kaarten: 169.000 € t/m ± 300.000 €, waaronder **vijf percelen** (AR-VF8J6N 1.500 m² 169.000 €; MC-N3J5OC 1.500 m² 169.000 €; BL-1Y3GRAZ Montgó 1.500 m² 179.000 €; MC-19LF6ST 1.500 m² 195.000 €; TB-008489 752 m² 285.000 €; AR-UQX40W 1.045 m² 300.000 €) en appartementen van 50–95 m². De voettekst en de pagineringslinks vielen buiten wat de ophaaltool teruggaf.

**Let op de referentievoorvoegsels:** van de 14 leesbare kaarten hadden er maar 2 het eigen voorvoegsel **JC-** (JC-1062AB, JC-1059AB); de overige komen van andere kantoren (AR-, MC-, BL-, JI-, CP-, GU-, TB-, VL-). CP-FZCZD3 is hetzelfde object dat op llidomarjavea.com uit het Sooprema-account `crown` kwam (verslag llidomar, 24-09-2026). De lijst op javeacasas.com is dus het **gedeelde Sooprema-netwerk**, niet alleen eigen aanbod. Andersom stond op llidomarjavea.com een object uit het account `javeacasas`.

**Objectpagina bekeken:** https://www.javeacasas.com/for-sale/apartment-with-a-spacious-terrace-garage-and-storage-room-near-the-port-of-javea-jc-1062ab/ (24-09-2026 ca. 21:55 UTC, standaard ophaaltool). Leesbaar op de pagina:

| Veld | Waarde |
|---|---|
| Referentie | JC-1062AB |
| Prijs | 279.000 € |
| Bebouwd / nuttig / terras | 84 m² / 59 m² / 20 m² |
| Perceel | 0 m² (appartement) |
| Plaats | Jávea (bij de haven), Alicante |
| Type, kamers | appartement, 1 slaapkamer, 1 badkamer, bouwjaar 2007, energielabel "in process" |

- **JSON-LD (`application/ld+json`) en og:-tags: onbekend.** De ophaaltool geeft alleen de leesbare tekst terug, niet de `<head>`; de ruwe HTML kon niet worden opgehaald omdat curl de Shield krijgt. Bij de zustersite llidomarjavea.com (zelfde Sooprema-platform, verslag 24-09-2026) was er géén JSON-LD en wél og-tags zonder prijs of oppervlakte; aannemelijk dat het hier hetzelfde is **[te verifiëren]**.
- Foto's op `javeacasas.com/objetos/temp/source/…`; geen tekst over gedeelde objecten of samenwerkende kantoren op de pagina.

## 5. Systeem achter de site — Sooprema, met Paagees Shield ervoor

Aanwijzingen (alle 24-09-2026):
- Logo op `javeacasas.com/crm/pages/agencies/javeacasas/assets/logo.svg` (homepage). Het pad `crm/pages/agencies/<naam>` is in B01 §2.4 vastgesteld als Sooprema (zelf gezien bij Llidomar en AREA Costa Blanca).
- Objectfoto's op `/objetos/temp/source/…` — het Sooprema-fotopad, identiek aan llidomarjavea.com, waar bovendien een gedeeld object uit het account `javeacasas` stond.
- robots.txt is het Sooprema-sjabloon (zie punt 1).
- Botcontrole "Powered by Paagees Shield", server nginx. Paagees is volgens B01 §2.3 géén CRM maar een weblaag die zich via XML/API aan o.a. Sooprema koppelt.
- Geen sporen van WordPress, Inmoweb, Mediaelx/LetsINMO, Inmovilla of Witei. Geen "powered by"-vermelding in de tekstextractie van homepage of objectpagina.

**Exportmogelijkheid:** Sooprema biedt live data via een REST-API, maar alleen als "la agencia en cuestión deberá ser cliente activo de Sooprema" (B01 §2.2, sooprema.com/api-desarrolladores, 16-09-2026). Daarnaast levert Sooprema kantoren standaard XML-portaalfeeds. De route loopt dus via het kantoor.

## 6. Omvang en dekking Jávea / Benitachell / Moraira

- Tellers op de homepage (24-09-2026): **124 objecten Jávea/Xàbia, 87 Dénia.** Moraira en Benitachell hebben eigen aanbodpagina's, maar de teller was niet zichtbaar. Zichtbaar totaal dus **≥ 211**, werkelijk totaal hoger (Moraira, Benitachell, nieuwbouw).
- Dekking: ongeveer 60 % van het getelde aanbod ligt in Jávea, ± 40 % in Dénia; Moraira en Benitachell komen erbij maar zijn niet geteld. Op de homepage stond onder meer een villa boven El Portet (Moraira, JC-1060AC, 2.250.000 €).
- **Eigen aanbod is klein:** op de aanbodpagina Jávea 2 van 14 kaarten met voorvoegsel JC-; op de homepage vier uitgelichte eigen objecten (JC-1053AB, JC-1058AC, JC-1060AC, JC-1068AB; 625.000 € tot 2.250.000 €). De doorlopende nummering rond 1053–1068 wijst op een eigen portefeuille van hooguit enkele tientallen objecten **[te verifiëren]**. De rest is gedeeld Sooprema-aanbod dat ook bij de bronkantoren (o.a. Crown Property, Llidomar) opduikt.
- Voor Deal Hunter interessant: percelen van 750–1.500 m² tussen 169.000 en 300.000 € stonden bovenaan de Jávea-lijst — maar vrijwel allemaal met een vreemd voorvoegsel, dus van andere kantoren.

## Advies: **feed vragen**

1. **Niet zelf lezen.** De Paagees Shield houdt een gewone automatische lezer tegen, ook al staat robots.txt het toe. Dat de standaard ophaaltool er doorheen kwam, is geen toestemming en geen stabiele basis (zelfde lijn als terramar.es, javeaimmo.com en crown-property.com).
2. **Voorwaarden verbieden commerciële reproductie.** Alleen intern signaleren; nooit teksten of foto's overnemen.
3. **Het eigen aanbod is klein en het meeste is gedeeld.** Een feed van Javea Casas levert vooral objecten op die ook bij Llidomar, Crown en andere Sooprema-kantoren zichtbaar zijn. Prioriteit daarom **laag**: eerst de Sooprema-kantoren met een groter eigen aanbod (Llidomar ≈ 85 eigen objecten, Terramar). Vraag Javea Casas alleen om de gegevens van de **eigen** objecten (JC-referenties: prijs, m², perceel, plaats, referentie, link), niet die van collega's (juridische lijn R04 §3.5).
4. Komt er een feed, dan zijn de vier eigen uitgelichte objecten (625.000 € – 2.250.000 €) en eventuele eigen percelen het enige unieke; voor Jan is dit kantoor vooral een aanvulling, geen hoofdbron.

⏸️ **ACTIE VOOR JAN:** beslis of TREE Javea Casas benadert voor een Sooprema-feed van het eigen aanbod (algemeen kanaal: sales@javeacasas.com). Gezien de kleine eigen portefeuille kan dit ook wachten tot na de grotere Sooprema-kantoren. Conceptbericht pas na jouw akkoord.

## Bronnen en tijdstippen

| Nr | Wat | URL | Wanneer (UTC) | Resultaat |
|---|---|---|---|---|
| 1 | robots.txt | https://www.javeacasas.com/robots.txt | 24-09-2026 ca. 21:45 | HTTP 200, 421 regels |
| 2 | Homepage (curl) | https://www.javeacasas.com/ | 24-09-2026 21:45:51 | HTTP 200, Shield-pagina 5.882 bytes |
| 3 | Sitemap (curl) | https://www.javeacasas.com/sitemap.xml | 24-09-2026 21:46:05 | HTTP 200, zelfde Shield-pagina, geen XML |
| 4 | Homepage (standaard ophaaltool) | https://www.javeacasas.com/ | 24-09-2026 ca. 21:47 | echte pagina: navigatie, tellers 124/87, 4 eigen objecten |
| 5 | Aanbod Jávea | https://www.javeacasas.com/properties-for-sale-in-javea/ | 24-09-2026 ca. 21:49 | 15 kaarten, 2× JC- |
| 6 | Legal notice | https://www.javeacasas.com/legal-notice/ | 24-09-2026 ca. 21:52 | voorwaarden gelezen |
| 7 | Objectpagina | https://www.javeacasas.com/for-sale/apartment-with-a-spacious-terrace-garage-and-storage-room-near-the-port-of-javea-jc-1062ab/ | 24-09-2026 ca. 21:55 | JC-1062AB, 279.000 €, 84 m² |

Lokaal gebruikt: `onderzoek/R06-makelaars-javea-register.md` (regel 45), `onderzoek/B01-crm-feeds.md` (§2.2–2.4), verslagen `site-llidomarjavea.com.md`, `site-terramar.es.md`, `site-javeaimmo.com.md`, `site-crown-property.com.md` (alle 24-09-2026).

Niet gedaan (en waarom): zoekmachine-onderzoek (sessiebudget op), `/sitemap_index.xml` en de pagina's Moraira/Benitachell (verzoekbudget), ruwe HTML van een objectpagina (alleen mogelijk door de Shield te omzeilen — niet gedaan).

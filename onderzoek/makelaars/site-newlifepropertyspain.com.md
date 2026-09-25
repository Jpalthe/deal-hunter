# New Life Property Spain — www.newlifepropertyspain.com — toets op automatisch lezen

**Datum toets:** 24-09-2026, 21:16–21:25 UTC · **Voor:** TREE Deal Hunter
**Rechtspersoon (volgens de legal notice van de site):** NL PROPERTY INVESTMENTS SL, CIF B06960686, Río Nalón, 03725 Moraira (Alicante)
**Kantoor Jávea (volgens gemeentelijst xabia.org, zie K01-kantoren-javea.json):** Av. de Lepanto 7, Puerto, Jávea — de site zelf toont alleen het adres in Moraira; of er twee vestigingen zijn is **[te verifiëren]**
**Algemeen contact (site):** +34 865 615 010 · ma–vr 09:00–17:00, za op afspraak
**Advies: FEED VRAGEN**

In één zin: robots.txt staat lezen toe en de voorwaarden noemen scraping niet met zoveel woorden, maar (a) de site zet een JavaScript-botcontrole ("Paagees Shield") vóór elke pagina die een gewone automatische lezer tegenhoudt, en (b) de voorwaarden verbieden reproductie en gebruik voor commerciële doeleinden zonder toestemming. Omzeilen doen we niet. Het systeem is Sooprema (op het Paagees-platform), dat exportfeeds kent — de feed is dus de nette en betrouwbare weg. Zelfde situatie als bij crown-property.com en javeaimmo.com (allebei getoetst 24-09-2026).

Vijf verzoeken aan de site gedaan (het maximum), nooit twee tegelijk, telkens meer dan 2 seconden uit elkaar: robots.txt (twee keer, twee methoden), sitemap.xml, één objectpagina, de legal notice. Latere vragen over dezelfde pagina's zijn beantwoord uit de cache van de ophaaltool (15 minuten per URL), zonder nieuw verzoek. Geen inlog, geen formulier, geen browser nagebootst, geen rekenpuzzel opgelost. Volledige verzoekenlijst onderaan.

## 1. robots.txt — toegestaan, maar achter een botcontrole

Bron: https://www.newlifepropertyspain.com/robots.txt (24-09-2026, 21:17 UTC).

**Eerste poging (curl, eigen herkenbare user-agent, 21:16:51 UTC):** HTTP 200, maar géén robots.txt. In plaats daarvan een HTML-pagina met titel "Security Check", tekst "Verifying your browser — This is an automatic security check. You will be redirected shortly." en voettekst "Powered by Paagees Shield". Headers: `server: cloudflare`, `x-robots-tag: noindex, nofollow`, `cache-control: no-store`. De pagina laat de browser een SHA-256-rekenpuzzel oplossen (5 leidende hex-nullen), zet dan een cookie `__shield` (1 uur geldig) en herlaadt. Zonder JavaScript en cookies kom je er niet doorheen. **Niet opgelost, niet omzeild.**

Let op voor een eigen lezer: de controlepagina komt met **HTTP 200**. Een naïef script denkt dus dat het de pagina heeft en slaat de controlepagina op als "inhoud".

**Tweede poging (standaard ophaaltool WebFetch, 21:17 UTC):** wél het echte bestand. Letterlijk:

```
User-agent: *
Allow: /
Disallow: /admin/
Disallow: /crm/
Disallow: /api/
Disallow: /ajax/
Disallow: /cgi-bin/
Disallow: /tmp/
Disallow: /cache/
```

- De aanbodpagina's (`/for-sale/`, `/for-sale/<omschrijving>-<referentie>/`, gebiedspagina's zoals `/villas-for-sale-benitachell/`) vallen onder `Allow: /` en staan in geen enkele Disallow-regel → **een `User-agent: *` mag ze lezen.**
- Geen `Crawl-delay`, geen `Sitemap:`-regel.
- De botcontrole verschilt dus per client: mijn curl werd tegengehouden, de standaard ophaaltool niet. Welke regel daarachter zit is niet zichtbaar. Voor de praktijk: **er is geen garantie dat een eigen lezer wordt doorgelaten**, en de controle omzeilen doen we niet.

## 2. Gebruiksvoorwaarden — geen expliciet scrapingverbod, wel verbod op reproductie en commercieel gebruik

Bron: https://www.newlifepropertyspain.com/legal-notice/ (24-09-2026, 21:20 UTC). Eén gecombineerd document in het Spaans ("Aviso legal y términos de uso" met daarin ook privacy- en cookiebeleid; de voettekstlinks "Legal notice", "Privacy Policy" en "Cookies Policy" wijzen alle drie naar deze pagina). Datum in het privacydeel: 27/12/2020. De sitemap bevat geen juridische URL's; de pagina is gevonden via de voettekst van de objectpagina.

Kopjes, in volgorde: Condiciones generales de uso · Datos personales que recabamos y cómo lo hacemos · Compromisos y obligaciones de los usuarios · Medidas de seguridad · Reclamaciones · Plataforma de resolución de conflictos · Derechos de propiedad intelectual e industrial · Enlaces externos · Política de comentarios · Exclusión de garantías y responsabilidad · Ley aplicable y jurisdicción · Contacto.

De woorden robot, crawler, scraping, automatisch lezen, extractie of databank komen **niet** voor (volgens de tekstextractie). Wel, onder **"Compromisos y obligaciones de los usuarios"**, een opsomming van verboden gebruik waaruit de ophaaltool deze regels letterlijk aanhaalt:

> "Se prohíbe la reproducción, distribución o modificación, total o parcial, a menos que se cuente con la autorización de sus legítimos titulares"
> "Cualquier vulneración de los derechos del prestador o de los legítimos titulares"
> "Su utilización para fines comerciales o publicitarios"

en verderop:

> "el usuario se compromete a no llevar a cabo ninguna conducta que pudiera dañar la imagen, los intereses y los derechos de www.newlifepropertyspain.com"

Toepasselijk recht: Spaanse wet en rechtbanken; verwijzingen naar LSSI-CE (Ley 34/2002) en de AVG (Reglamento (UE) 2016/679).

**Oordeel:** automatisch lezen wordt niet met zoveel woorden verboden ("nee" op de vraag of scraping wordt verboden), maar reproductie van de inhoud en gebruik "para fines comerciales" zonder toestemming wél. Deal Hunter is een commerciële toepassing. Dat is de standaardclausule die ook bij Cala Blanca en Javea Immo staat; voor intern signaleren is het werkbaar, maar het pleit — samen met de botcontrole — voor de feedroute met expliciete toestemming van het kantoor. Foto's en teksten van deze site nooit overnemen in eigen publicaties.

## 3. Sitemap — 628 URL's, circa 400 objecten

- robots.txt noemt geen sitemap.
- https://www.newlifepropertyspain.com/sitemap.xml (24-09-2026, 21:18 UTC): een gewone URL-sitemap (geen index) met **628 `<loc>`-URL's**, `lastmod` van 2026-07-28 tot 2026-09-24. De meeste objectpagina's hebben een lastmod in september 2026: het aanbod wordt bijgehouden.
- Opbouw: objecten onder `/for-sale/<omschrijving>-<referentie>/`; lijstpagina's `/for-sale/`, `/rentals/`, `/holiday-rentals/`, `/property-for-sale-spain/`, `/latest-properties-for-sale-costa-blanca/`; ruim 70 gebiedspagina's (wijken, urbanisaties, gemeenten); ruim 130 nieuws-/blogartikelen; `/area-guides/`, `/buying-advice/`, `/currency/`; geen losse huur-objectpagina's.
- Trefwoorden in de object-URL's (telling ophaaltool, eerste doorloop): villa 149 · property/properties 86 · plot 24 · apartment 8 · for-sale in alle object-URL's; venta/inmueble/parcela/apartamento 0 (Engelstalige site).
- **Aantal objecten: geschat circa 400, marge 340–420.** Motivering: de ophaaltool telde in drie doorlopen 341 en 419 individuele `/for-sale/`-URL's (en één keer 541, wat niet klopt met de 200+ niet-objectpagina's die ze zelf beschreef); de opgevraagde volledige lijst bevatte 284 unieke URL's maar werd afgekapt. 628 minus circa 210 niet-objectpagina's geeft ongeveer 415. Een exacte telling vraagt de ruwe XML, en die was met curl niet te krijgen (botcontrole). **[te verifiëren zodra er een feed is]**

## 4. Aanbod- en objectpagina

Aanbodpagina: https://www.newlifepropertyspain.com/for-sale/ (niet apart opgehaald: verzoekbudget; bestaat volgens de sitemap).

Objectpagina: https://www.newlifepropertyspain.com/for-sale/villa-for-sale-in-javea-xabia-nl79-665358/ (24-09-2026, 21:19 UTC). Zichtbare gegevens (via tekstextractie):

| Veld | Waarde |
|---|---|
| Referentie | NL79-665358 |
| Type | Villa ("Villa Paradise") |
| Plaats | Jávea, zone Cap Martí |
| Vraagprijs | € 1.288.000 |
| Bebouwd | 339 m² in de tekst; de pagina toont ook 264 m² (vermoedelijk woonoppervlak vs. bebouwd; niet eenduidig) |
| Perceel | 1.050 m² |
| Slaap-/badkamers | 5 / 5 |
| Energielabel | "IN PROCESS" |
| Kenmerken | zwembad, parkeren, tuin, terrassen, vloerverwarming, airco via kanalen, zonnepanelen, laadpunt EV, domotica, alarm/video-intercom |
| Datum plaatsing | niet op de pagina; de foto-uploads staan in een map `.../property/2026/09/24/` → op de toetsdag (opnieuw) geüpload |

**JSON-LD (`application/ld+json`) en og:-meta-tags: onbekend.** De ophaaltool zet de pagina om naar tekst en laat `<head>`-tags en scripts weg; in die tekst komen `ld+json`, `@context`, `schema.org`, `og:title`, `og:image` en `product:price` niet voor. De ruwe HTML was met curl niet te krijgen door de botcontrole uit punt 1, en die omzeil ik niet. Bij een feed is dit ook niet meer nodig. (Bij zustersites op hetzelfde platform, crown-property.com en javeaimmo.com, was het antwoord om dezelfde reden onbekend.)

## 5. Systeem achter de site — Sooprema op het Paagees-platform

Aanwijzingen (24-09-2026, objectpagina en legal notice):
- Voettekst bevat een logolink naar `https://www.sooprema.com/` (Spaans vastgoed-CRM/CMS met exportfeeds). Op zustersite calablanca.com heeft diezelfde link de titel "Software Inmobiliario Sooprema".
- Foto's komen van `https://app-api.paagees.com/uploads/<uuid>/property/2026/09/24/…`.
- Bestanden in `/agencies/newlife/assets/` en `/widgets/base/propertyextra/` — een platform met meerdere kantoren ("agencies"), elk met een eigen map.
- De botcontrole noemt zichzelf "Powered by Paagees Shield".
- Geen sporen van WordPress (`/wp-content/`), Inmoweb, Mediaelx/LetsINMO, Inmovilla, Witei of Kyero-widgets.
- Exact dezelfde handtekening als crown-property.com en javeaimmo.com (toetsen 24-09-2026). Of Paagees de weblaag van Sooprema is dan wel een aparte leverancier die Sooprema-data toont, kon ik niet nazoeken (zoekbudget van de sessie op) → **[te verifiëren]**. Voor het advies maakt het niet uit: in beide gevallen wordt de site gevoed uit een CRM met een XML/API-feed, dus die feed bestaat al.

## 6. Omvang en dekking Jávea / Benitachell / Moraira

Telling op de 284 object-URL's die de ophaaltool wél kon opsommen (de verhouding is stabiel: een tweede, onafhankelijke telling op 341 URL's gaf 42 %):

| Gebied | Aantal | Aandeel |
|---|---|---|
| Jávea/Xàbia (incl. Montgó, Arenal, Tosalet, Costa Nova) | 34 | 12 % |
| Benitachell / Cumbre del Sol / Les Fonts | 41 | 14 % |
| Moraira (incl. Portet, Paichi) | 48 | 17 % |
| **Drie doelplaatsen samen** | **123** | **43 %** |
| Calpe (incl. La Fossa, Oltamar, Les Bassetes) | 77 | 27 % |
| Benissa (incl. Racó de Galeno, Senija) | 30 | 11 % |
| Altea, Finestrat, Benidorm, Albir, La Nucía | 23 | 8 % |
| Dénia | 9 | 3 % |
| Binnenland (Jalón, Llíber, Parcent, Orba, Tormos, Gata, Beniarbeig, Ràfol, Teulada) | 16 | 6 % |
| Zonder plaatsnaam in de URL | 7 | 2 % |

Omgerekend naar circa 400 objecten: **ruwweg 170 in Jávea, Benitachell en Moraira**, waarvan zo'n 50 in Jávea zelf.

**Belangrijke nuance — gedeeld aanbod.** De referenties dragen een voorvoegsel (`nl47`, `nld27`, `nl51`, `nl41`, `nl23`, `nl31`, `nl80`, …) dat er sterk op wijst dat dit aanbod van samenwerkende kantoren is: `nl47` alleen al levert 97 van de 284 URL's (vrijwel allemaal Calpe/Benissa-kust/Altea/Finestrat), `nld27` 28 (bijna allemaal Benitachell), `nl31` 11 (allemaal Cumbre del Sol). Slechts **16 van de 284 (6 %)** hebben een "eigen" referentie zonder partnernummer (`NLD0333` … `NLD0373`, `NLNS0354`, `NLNS0400`, `NLAS0245`). Zelfde patroon als bij Crown Properties. Interpretatie **[te verifiëren]**: het meeste van wat hier staat, staat ook bij de partnerkantoren; de unieke waarde van deze bron zit in de circa 16 eigen objecten.

Eigen objecten in de doelplaatsen (URL-omschrijving, niet opgehaald): villa met grote garage en werkplaats in Jávea oude stad (NLD0360) · vrijstaande villa 5 slk/7 badk. met zeezicht Jávea (NLD0350) · vrijstaande villa 4–5 slk Jávea (NLD0373) · villa Les Fonts, Benitachell (NLD0337) · appartement Cumbre del Sol (NLD0364) · vrijstaande villa met zeezicht Cumbre del Sol (NLD0314) · originele finca Benitachell (NLD0366) · halfvrijstaande villa met zeezicht Moraira (NLNS0400) · **villa "for reform", 5 slk, zeezicht, perceel 1.400 m², Moraira (NLD0371)** — die laatste is precies het type object waar Deal Hunter naar zoekt.

Overige signalen voor Deal Hunter in de URL-lijst: 20 percelen (o.a. Jávea/Xàbia NL58-lz4u30, Cumbre del Sol NL8-z66vuz, Moraira NL51-129zwmc, NL23-426220, NL58-1qltiae), 5 bedrijfspanden, 12 nieuwbouw-/projectobjecten.

## Wat dit betekent voor Deal Hunter

1. **Feed vragen** bij New Life Property: een XML-exportfeed uit Sooprema (doorgaans in Kyero-/Idealista-formaat) met prijs, m², perceel, plaats en referentie, mét toestemming voor intern gebruik. Daarmee vervalt het hele scrapingvraagstuk: botcontrole, commercieel-gebruik-clausule en auteursrecht op foto's. Vraag daarbij of de feed onderscheid maakt tussen eigen aanbod en partneraanbod.
2. Zolang er geen feed is: **niet** met een eigen scraper de Paagees Shield omzeilen, en niet met een nagebootste browser werken. Een lichte lezing via de standaard ophaaltool bleek vandaag te werken, maar daar is geen garantie op en het staat haaks op de bedoeling van die controle.
3. Prioriteit: **middel**. Circa 43 % van het aanbod ligt in de doelplaatsen, maar het grootste deel is gedeeld partneraanbod dat ook via andere kantoren binnenkomt. De eigen objecten (circa 16) zijn klein in aantal maar bevatten wel een renovatieobject in Moraira en een finca in Benitachell.
4. Nooit teksten of foto's van deze site in eigen publicaties gebruiken (voorwaarden, punt 2).

⏸️ **ACTIE VOOR JAN:** New Life Property benaderen via het algemene kantoornummer (+34 865 615 010) of het contactformulier op de site, met de vraag om een Sooprema-exportfeed voor intern gebruik door TREE, plus of ze een samenwerkingsafspraak (collaboración) willen voor hun eigen aanbod in Jávea, Benitachell en Moraira. Meteen navragen of het adres Av. de Lepanto 7 (Puerto, Jávea) uit de gemeentelijst nog klopt naast het kantoor in Moraira.

## Verzoeken aan de site (24-09-2026)

| # | URL | Methode | Tijd (UTC) | Resultaat |
|---|---|---|---|---|
| 1 | /robots.txt | curl, eigen user-agent | 21:16:51 | HTTP 200, controlepagina "Security Check — Powered by Paagees Shield" (geen robots.txt) |
| 2 | /robots.txt | WebFetch | ca. 21:17 | echte robots.txt, geciteerd in punt 1 |
| 3 | /sitemap.xml | WebFetch | ca. 21:18 | URL-sitemap, 628 URL's |
| 4 | /for-sale/villa-for-sale-in-javea-xabia-nl79-665358/ | WebFetch | ca. 21:19 | objectpagina, punt 4 |
| 5 | /legal-notice/ | WebFetch | ca. 21:20 | aviso legal y términos de uso, punt 2 |

Vervolgvragen over verzoeken 3, 4 en 5 zijn beantwoord uit de cache van de ophaaltool (geldig 15 minuten per URL), zonder nieuw verzoek aan de site.

Niet gedaan (en waarom): `/sitemap_index.xml` en `/for-sale/` niet apart opgehaald (verzoekbudget; sitemap.xml was al compleet); zoekmachine-onderzoek naar Paagees/Sooprema (zoekbudget van de sessie was op); ruwe HTML (botcontrole, niet omzeild); tweede objectpagina (budget).

Lokale bronnen: `K01-kantoren-javea.json` (gemeentelijst xabia.org/ver/2098, 24-09-2026) en `K02-kantoren-benitachell-moraira.json`; vergelijkingsverslagen `site-crown-property.com.md`, `site-javeaimmo.com.md`, `site-calablanca.com.md` (alle 24-09-2026).

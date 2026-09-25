# Crown Properties S.L. — crown-property.com — toets op automatisch lezen

Datum toets: 24-09-2026 · Voor: TREE Deal Hunter · Site: https://www.crown-property.com

## Advies in één zin

**Feed vragen.** robots.txt en de voorwaarden verbieden lezen niet, maar de site zet een
JavaScript-botcontrole ("Paagees Shield") vóór elke pagina die een gewone automatische lezer
tegenhoudt — die omzeilen we niet. Het systeem achter de site (Sooprema/Paagees, zie punt 5)
kent een exportfeed, dus een feed is de nette en betrouwbare weg.

## 1. robots.txt — toegestaan

Bron: https://www.crown-property.com/robots.txt (24-09-2026)

Letterlijke regels:

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

- De aanbodpagina's (`/venta/...`, `/villas-de-lujo-javea/` enz.) vallen onder `Allow: /` en
  staan niet in een Disallow-regel → **een `User-agent: *` mag ze lezen.**
- Er staat **geen `Sitemap:`-regel** in.
- Bijzonderheid: de eerste poging (curl met een eigen, herkenbare user-agent) kreeg **niet**
  robots.txt maar een HTML-pagina "Security Check / Verifying your browser — Powered by
  Paagees Shield": een JavaScript-rekenpuzzel (SHA-256 proof-of-work) die een cookie
  `__shield` zet en daarna herlaadt. Zonder JavaScript en cookies kom je er niet doorheen.
  De tweede poging via de standaard ophaaltool kreeg het bestand wél. De controle lijkt dus
  per client te verschillen; welke regel daarachter zit is niet zichtbaar. Ik heb de puzzel
  niet opgelost en geen browser nagebootst.

## 2. Voorwaarden — geen expliciet scrapingverbod, wel auteursrecht

Bron: https://www.crown-property.com/aviso-legal/ (24-09-2026) — Aviso legal + privacy + cookies
op één pagina. Op de homepage staat geen zichtbare link naartoe (mogelijk in een footer die
via JavaScript wordt geladen); de URL is geraden en bleek te bestaan.

- Rechtspersoon: CROWN PROPERTIES S.L., CIF B03092723, Avd. París 2, Playa Arenal,
  03730 Jávea (Alicante).
- Over automatisch lezen, scraping, robots of crawlers: **niets** gevonden.
- Wel een gebruikelijke clausule intellectueel eigendom: reproductie, distributie of
  wijziging van de inhoud (teksten, foto's, software) is verboden zonder toestemming
  ("se prohíbe: Su reproducción, distribución o modificación, total o parcial…"), en wie de
  site bezoekt aanvaardt de algemene voorwaarden.
- Betekenis voor ons: intern lezen en analyseren is niet verboden; foto's en
  woningteksten overnemen of opnieuw publiceren wél.

## 3. Sitemap — ca. 850–900 object-URL's

Bron: https://www.crown-property.com/sitemap.xml (24-09-2026). Gewone `urlset`, geen index.
Tellingen zijn schattingen van de ophaaltool (geen exacte telling mogelijk zonder ruwe XML):

- Totaal ca. **1.062 URL's**, waarvan ca. **1.056 onder `/venta/`**.
- Ca. **850–900** eindigen op een referentie, in twee vormen:
  - eigen viercijferige referenties, bijv. `…-4642/`, `…-4865/`, `…-4917/`;
  - referenties met `crm`/`crmi`-voorvoegsel, bijv. `…-crm534672/`, `…-crmi486127/` —
    waarschijnlijk gedeeld aanbod van collega-kantoren via een CRM-koppeling **[te verifiëren]**.
- `lastmod` loopt van 13-05-2026 tot 24-09-2026: de sitemap wordt actueel gehouden.
- Voorbeeld-URL's:
  - https://www.crown-property.com/venta/chalet-villa-en-javea-crm534672/
  - https://www.crown-property.com/venta/villa-con-vista-al-mar-en-venta-en-moraira-a-poca-distancia-del-centro-crmi486127/
  - https://www.crown-property.com/venta/apartamento-con-impresionantes-zonas-comunes-a-escasos-metros-de-la-playa-el-arenal-4865/
  - https://www.crown-property.com/venta/villa-de-lujo-en-venta-en-javea-con-2-piscinas-vistas-al-montgo-y-buena-orientacion-4917/

## 4. Eén objectpagina — leesbaar, gegevens in de HTML

Bron: https://www.crown-property.com/venta/espectacular-y-moderna-villa-en-construccion-en-una-demandada-zona-de-javea-4642/ (24-09-2026)

| Veld | Waarde |
|---|---|
| Titel | "Espectacular y moderna villa en construccion en una demandada zona de Javea. \| Ref: 4642" |
| Prijs | € 1.840.000 |
| Bebouwd | 459 m² |
| Perceel | 1.500 m² |
| Slaap-/badkamers | 4 / 4 (+1 toilet) |
| Plaats / zone | Jávea, Montgó |
| Referentie | 4642 |

- De inhoud (prijs, kenmerken, beschrijving) staat in de HTML zelf, niet alleen via JavaScript.
- **JSON-LD (schema.org) en og:-tags: onbekend.** De ophaaltool zet de pagina om naar tekst en
  laat `<head>`-tags en scripts weg; de ruwe HTML was met curl niet te krijgen door de
  botcontrole uit punt 1. Bij een feed is dit ook niet meer nodig.

## 5. Systeem achter de site — Sooprema op het Paagees-platform [te verifiëren]

Aanwijzingen (24-09-2026):
- Afbeeldingen komen van `https://app-api.paagees.com/uploads/…`.
- CSS/logo's staan in `/agencies/crown/assets/` — een pad dat op een platform met meerdere
  kantoren ("agencies") wijst.
- De botcontrole noemt zichzelf "Powered by Paagees Shield".
- De tekstextractie van de objectpagina meldt in de footer "Powered by Sooprema"; op de
  homepage-extractie kwam die vermelding niet voor. Sooprema is een Spaans vastgoed-CMS met
  exportfeeds. Of Paagees de technische laag van Sooprema is, kon ik niet nazoeken
  (zoekbudget van deze sessie was op) → **[te verifiëren]**.
- URL-structuur `/venta/<slug>-<ref>/`, talen via `/es/`, `/en/`, `/de/`, `/fr/`, `/nl/`.

Conclusie: niet Inmoweb, Mediaelx, Inmovilla, Witei of WordPress; meest waarschijnlijk
Sooprema (Paagees), en daarmee een systeem dat een exportfeed kent.

## 6. Omvang en dekking Jávea / Benitachell / Moraira

- Homepage (24-09-2026) toont per categorie: villas de lujo 147, villas 420, casas de pueblo 13,
  apartamentos 132 → **712 objecten**. De sitemap telt meer (ca. 850–900 object-URL's);
  het verschil zit vermoedelijk in verlopen of dubbele pagina's **[te verifiëren]**.
- Plaatsnamen in de sitemap-URL's (schatting van de tool; veel URL's noemen geen plaats):
  Jávea/Xàbia ca. 420 · Moraira ca. 95 · Benitachell ca. 45 · Cumbre del Sol ca. 10 —
  samen ca. 570 van ca. 795 URL's mét plaatsnaam, dus **grofweg 70 %**. Rest: Dénia ca. 85,
  Benissa ca. 60, Calpe ca. 25, Pedreguer ca. 20, Jesús Pobre ca. 15, Teulada ca. 12,
  Gata de Gorgos ca. 8.
- Kantoor zit aan het Arenal in Jávea; het aanbod is dus vooral lokaal, met een schil
  Dénia–Benissa–Calpe.

## Wat dit betekent voor Deal Hunter

1. **Feed vragen** bij Crown Properties: een XML-exportfeed (Sooprema levert die doorgaans in
   Kyero-/Idealista-formaat) met prijs, m², perceel, plaats en referentie. Daarmee vervalt
   het hele scrapingvraagstuk, inclusief de botcontrole en het auteursrecht op foto's.
2. Zolang er geen feed is: **niet** met een eigen scraper de Paagees Shield omzeilen. Een
   lichte, trage lezing via een standaard ophaaltool bleek vandaag te werken, maar daar is
   geen garantie op en het staat haaks op de bedoeling van die controle.
3. Let bij de feed op het onderscheid eigen aanbod (viercijferige ref.) versus
   `crm`/`crmi`-referenties (waarschijnlijk gedeeld aanbod) — dubbelingen met andere
   kantoren zijn dan te verwachten.

⏸️ ACTIE VOOR JAN: Crown Properties benaderen (kantoor Avd. París 2, Playa Arenal, Jávea;
algemeen e-mailadres info@crown-property.com) met de vraag om een exportfeed van het
verkoopaanbod, en afspreken wat we ermee doen (intern analyseren, niets herpubliceren).

## Verantwoording

- 6 HTTP-verzoeken over 5 verschillende pagina's (robots.txt tweemaal, met twee
  verschillende clients), verspreid over enkele minuten; homepage-analyses daarna uit de
  cache van de ophaaltool zonder nieuw verzoek.
- Niet ingelogd, geen formulieren, geen cookies gezet, botcontrole niet omzeild.
- Geen persoonsgegevens overgenomen; alleen bedrijfsnaam, kantooradres, CIF en het algemene
  e-mailadres.
- Zoekmachinecontrole (o.a. relatie Sooprema–Paagees) niet gedaan: zoekbudget van de sessie
  was op. Punten met **[te verifiëren]** zijn daarom nog open.

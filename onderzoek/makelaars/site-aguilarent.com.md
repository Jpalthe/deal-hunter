# Aguila Rent a Villa — toets op automatisch lezen

- **Website:** https://www.aguilarent.com (bedrijf: Aguila rent a villa s.l.; kantoor Jávea, Av. de Palmela 56 volgens de gemeentelijst in `K01-kantoren-javea.json`)
- **Datum toets:** 24-09-2026, ca. 23:03–23:06 lokale tijd (server-datumkoppen 21:03–21:06 UTC)
- **Opgehaald (6 verzoeken, telkens ≥ 2 s tussenruimte):** robots.txt, sitemap_gb.xml, homepage, voorwaardenpagina, aanbodpagina "for sale", één objectpagina. Dus 4 HTML-pagina's plus twee tekst/XML-bestanden.
- **Advies: lezen — maar lage prioriteit.** Het mag en het kan, maar er staan maar 2 woningen te koop en geen daarvan ligt in Jávea, Benitachell of Moraira. Eén verzoek per maand naar de verkooppagina volstaat.

## 1. robots.txt — toegestaan

Bron: https://www.aguilarent.com/robots.txt (24-09-2026, HTTP 200). Volledige inhoud:

```
User-agent:*
Allow: /
Sitemap: https://www.aguilarent.com/sitemap_gb.xml?lang=gb
Sitemap: https://www.aguilarent.com/sitemap_fr.xml?lang=fr
```

Elke lezer (`User-agent:*`) mag de hele site lezen (`Allow: /`), dus ook de aanbod- en objectpagina's. Geen `Disallow`, geen `Crawl-delay`.

## 2. Gebruiksvoorwaarden — geen scrapingverbod, wél een verbod op commercieel hergebruik van de inhoud

Bron: https://www.aguilarent.com/holiday-rentals/information/leral-notice-and-disclaimer ("LEGAL NOTICE AND DISCLAIMER"; de link in de voettekst `/info/leral-notice-and-disclaimer` stuurt door naar dit adres), gelezen 24-09-2026.

De woorden scraping, robot, crawler, bot of "automated" komen niet voor. Wel relevant:

- Gebruiker mag de site niet gebruiken om (b) "hinder the access of other users to the website and its services through the massive consumption of computer resources" — dus: rustig lezen, niet hameren.
- (d) niet "Reproducing, copying, distributing, making available or in any other way publicly communicating, transforming or modifying the contents, unless the authorisation of the holder of the corresponding rights has been obtained or this is legally permitted."
- (e) geen gegevens verzamelen voor reclamedoeleinden of ongevraagde commerciële berichten.
- Intellectueel eigendom: "The reproduction, transformation, distribution and public communication [...] of all or part of the contents of this website, for commercial purposes, in any medium and by any technical means, without the prior written authorisation of Aguila Rent a Villa is expressly prohibited." Bekijken, printen en opslaan mag "solely and exclusively for your personal and private use".
- Opvallend: voor het plaatsen van een hyperlink vragen ze vooraf schriftelijke toestemming.

**Betekenis voor Deal Hunter:** automatisch lezen wordt niet verboden, maar foto's en beschrijvingsteksten overnemen of doorpubliceren wel. Alleen kale feiten noteren (prijs, plaats, m², perceel, link naar de bron) en niets van de site herpubliceren. Contactkanalen van eigenaren niet gebruiken voor ongevraagde aanbiedingen (punt e).

## 3. Sitemap — 755 URL's, bijna allemaal vakantieverhuur

Bron: https://www.aguilarent.com/sitemap_gb.xml?lang=gb (24-09-2026). De Franse sitemap is niet opgehaald (zelfde objecten, andere taal).

- 755 URL's in totaal; **672 zijn detailpagina's van accommodaties** met het patroon `/holiday-rentals/spain/<regio>/<plaats>/<type>/<naam>`.
- Type: 407 villas, 184 apartments, 49 holiday-homes, 14 houses, 6 holiday-houses, 5 penthouses, 4 chalets, 3 studios.
- Plaats: Jávea 324, Dénia 88, Calpe 72, Moraira 58, Altea 37, Benissa 28, Benitachell 26, rest kleiner (Andalusië 9, Murcia 6, enz.).
- **Jávea + Benitachell + Moraira: 408 van 672 (61 %)** — maar dit zijn verhuurobjecten, geen koopaanbod.
- URL's die op een koopobject lijken: **0**. De enige verkoop-URL is de lijstpagina `/holiday-rentals/for-sale`. Woorden als venta, property, inmueble, parcela komen niet voor; "villa/apartment" wel (591 keer), maar dat is het accommodatietype van de verhuur.
- Verder 22 informatiepagina's (`/holiday-rentals/info/...`), waaronder `Buy-a-home-in-javea` en `let-my-property`.

## 4. Aanbodpagina en objectpagina

**Aanbodpagina te koop:** https://www.aguilarent.com/holiday-rentals/for-sale (24-09-2026, HTTP 200). Kop: "Homes for sale — 2 Villas with pool and apartaments for sale in Jávea"; paginatitel "2 Homes for sale in Jávea and the surrounding area". Het is een filter op de verhuurdatabase (cookie `SearchParameters=...&on-sale=1`). Twee objecten:

| Naam | Plaats | Verkoopprijs (site) | Personen / slaapk. / badk. |
|---|---|---|---|
| Clem | Calpe | € 995.000 | 8 / 4 / 3 |
| Daru dunya | Dénia | € 890.000 | 8 / 4 / 3 |

Geen van beide in Jávea, Benitachell of Moraira, ondanks de kop.

**Objectpagina bekeken:** https://www.aguilarent.com/holiday-rentals/spain/costa-blanca/calpe/villas/clem (24-09-2026, HTTP 200, ~397 kB).

- `<script type="application/ld+json">`: **ja, 1 blok**, `@type: VacationRental`. Bevat: naam "Clem", beschrijving, url, 18 foto-URL's (ik.imagekit.io/agrpv/104042_xx.jpg — 104042 is het interne objectnummer), `identifier` "CV-VUT0479284-A" (dit is het toeristische verhuurnummer, geen verkoopreferentie), adres (Partida Enginent II 45, 03710 Calpe, ES), geo (38.64594 / 0.06201), beoordeling 8,5 uit 13 reviews, `containsPlace` met 4 slaapkamers, 3 badkamers, bezetting 8, **`floorSize` 260 m²** en voorzieningen. **Geen prijs en geen `offers`** in de JSON-LD; **geen perceel** in de JSON-LD.
- In de leesbare tekst wél: "Building size 260 m2." en **"Plot size 631 m2."**, plus de verhuurlicentie. **De verkoopprijs staat niet op de objectpagina**, alleen op de lijstpagina ("Sale Price: € 995.000").
- og-tags: alleen `og:image`, `og:image:type/width/height` en `og:locale` (en_GB). Geen `og:title`, `og:url`, `og:type`, `og:description`. Wel `twitter:title` ("Villa Clem in Calpe, Costa Blanca, Spain"), `twitter:description` en een gewone `meta description`.

Conclusie: leesbaar en gestructureerd, maar de verkoopgegevens (prijs) staan alleen op de lijstpagina; oppervlakte en perceel op de objectpagina.

## 5. Systeem achter de site — verhuurplatform i-rent.net op ASP.NET, geen makelaars-CMS

Aanwijzingen (homepage en objectpagina, 24-09-2026):

- Serverkoppen: `Server: Microsoft-IIS/10.0`, `X-Powered-By: ASP.NET`, `X-AspNet-Version: 4.0.30319`.
- ASP.NET WebForms: `__VIEWSTATE` (4×), `<form id="FormMaster">`, element-id's `ctl00_...`, `ctl10_Hyperlink_Info_Terms`, CSS via `/handlers/css_handler.ashx`.
- JavaScript-functie `OpenAccoAdminConditionsDialog(...)` ("AccoAdmin").
- Voettekst linkt naar https://www.i-rent.net ("Login page for owners"), https://www.rentalbookingsystem.com en https://www.checkmyreservation.com — de merken van het i-rent-verhuurplatform.
- Beelden via ik.imagekit.io, prijsbeacon beacon.beyondpricing.com, Google Tag Manager/gtag, reCAPTCHA v3.
- Geen sporen van Inmoweb, Mediaelx/LetsINMO, Sooprema, Inmovilla, Witei of WordPress.

Dit is dus vakantieverhuursoftware waar "te koop" een vinkje op een verhuurobject is. Een exportfeed voor koopobjecten is niet bekend [te verifiëren]; voor 2 objecten is die ook niet de moeite waard.

## 6. Schatting aanbod en dekking

- **Verhuur:** ca. 672 accommodaties in de sitemap, 61 % in Jávea/Benitachell/Moraira (Jávea alleen: 324).
- **Te koop:** **2 objecten** op 24-09-2026, **0 in Jávea, Benitachell of Moraira** (1 Calpe, 1 Dénia). Prijsniveau € 890.000–995.000.

## Advies

**Lezen, lage prioriteit.** robots.txt staat het toe, de voorwaarden verbieden automatisch lezen niet, en de pagina's zijn goed leesbaar (JSON-LD op de objectpagina). Maar het koopaanbod is verwaarloosbaar voor Deal Hunter. Voorstel:

1. Eén keer per maand alleen https://www.aguilarent.com/holiday-rentals/for-sale ophalen (1 verzoek) en kijken of er iets in Jávea/Benitachell/Moraira bijkomt. Prijs van de lijstpagina halen; bij een treffer de objectpagina openen voor m² en perceel.
2. Geen foto's of teksten overnemen (IP-clausule); alleen feiten en de bron-URL bewaren.
3. Interessanter dan het koopaanbod: dit kantoor beheert 324 verhuurvilla's in Jávea en vraagt eigenaren zelf "Want to sell Your Property?" (`/holiday-rentals/info/Buy-a-home-in-javea`). Een zakelijke relatie met het kantoor kan meer opleveren dan de site lezen — ⏸️ ACTIE VOOR JAN als hij dat wil oppakken.

# Rimontgó — toets op automatisch lezen

- **Website:** https://www.rimontgo.com (bedrijf: RIMONTGÓ, CIF B03901964, Avenida de Lepanto 1, 03730 Jávea — volgens de eigen Legal Notice; kantoren in Valencia, Jávea, Jávea Arenal en Madrid; lid van Forbes Global Properties en Luxury Portfolio International)
- **Datum toets:** 24-09-2026, 's avonds (lokale tijd)
- **Opgehaald (5 verzoeken, telkens ≥ 2 s tussenruimte):** robots.txt, sitemap.xml, aanbodpagina Jávea, één objectpagina, Legal Notice. Dus 3 HTML-pagina's plus twee tekst/XML-bestanden. Niets anders aangeraakt: geen inlog, geen formulier.
- **Advies: lezen.** robots.txt staat alles toe, de voorwaarden verbieden automatisch lezen niet, en de objectpagina's zijn gestructureerd (schema.org JSON-LD met prijs, m², plaats). Luxesegment: dit kantoor zit hoog in de markt, dus verwacht weinig "deals" maar wél percelen en oudere villa's in Jávea-zones die elders niet altijd staan. Alleen kale feiten opslaan, geen teksten of foto's overnemen (zie punt 2).

## 1. robots.txt — toegestaan

Bron: https://www.rimontgo.com/robots.txt (24-09-2026, HTTP 200). Volledige inhoud:

```
User-agent: *
Allow: /

Sitemap: https://www.rimontgo.com/sitemap.xml
```

Elke lezer (`User-agent: *`) mag de hele site lezen (`Allow: /`), dus ook de aanbod- en objectpagina's. Geen `Disallow`, geen `Crawl-delay`. De sitemap wordt expliciet genoemd.

## 2. Gebruiksvoorwaarden — geen scrapingverbod, wél een brede auteursrechtclausule

Bron: https://www.rimontgo.com/legal-notice ("Legal Notice | Rimontgó Real Estate"), gelezen 24-09-2026, HTTP 200. Gelinkt vanuit de voettekst van elke pagina; er is ook een aparte privacyverklaring (https://www.rimontgo.com/privacy-policy, niet opgehaald). Aparte "terms" of "condiciones" zijn er niet; de Legal Notice is het enige gebruiksdocument. Hij staat niet in de sitemap.

De woorden scraping, crawler, robot, bot, spider, automated, extract, data mining, database, download, bulk of API komen in de hele tekst (ca. 14.000 tekens) niet voor. Wel relevant:

- **Intellectueel eigendom:** "The intellectual property rights of the contents of the web pages, their graphic design and codes are the property of RIMONTGÓ and, therefore, their reproduction, distribution, public communication, transformation or any other activity which may be carried out with the contents of its web pages is prohibited, even when quoting the sources, except with the written consent of RIMONTGÓ."
- **Hyperlinks:** een link naar de homepage mag zonder toestemming; "Any other form of Hyperlink shall require the express and unequivocal written authorisation of RIMONTGÓ." Geen frames.
- **Toegang:** "access to this website does not in any way imply the commencement of a commercial relationship" — geen gebruiksovereenkomst die je stilzwijgend aangaat.
- **Recht en rechtbank:** Spaans recht, rechtbanken van Valencia.

**Betekenis voor Deal Hunter:** automatisch lezen wordt nergens verboden, en robots.txt zegt uitdrukkelijk dat het mag. De auteursrechtclausule is wel breed ("any other activity ... with the contents"). Daarom: alleen feiten vastleggen die geen auteursrecht dragen (prijs, plaats, zone, bouw- en perceeloppervlak, slaapkamers, referentie, bron-URL, datum) voor intern gebruik; geen beschrijvingsteksten of foto's kopiëren, niets herpubliceren, en geen diepe links naar objectpagina's op een publieke site zetten zonder toestemming. Intern (in het Deal Hunter-overzicht) is een link naar de bron gewoon een bronvermelding.

## 3. Sitemap — 2.280 URL's, 181 objectpagina's (in zes talen)

Bron: https://www.rimontgo.com/sitemap.xml (24-09-2026, HTTP 200, ca. 2,0 MB). Eén platte sitemap, geen index; geen `<lastmod>`-datums; elke URL heeft hreflang-koppelingen naar zes talen.

- **2.280 URL's** in totaal: 385 Engels (zonder taalprefix) en 379 per taal voor es, fr, de, pl en nl (`/nl/eigendommen/...`). Het zijn steeds dezelfde pagina's in zes talen.
- Engelse structuur: 282 onder `/properties/`, 27 `/guides/`, 22 `/about-us/`, 18 `/agents/`, 13 `/collections/`, en losse pagina's (contact, buyers-guide, sellers-guide, outstanding-sales, investment, private-sales, enz.).
- Van de 282 `/properties/`-URL's zijn **101 gebiedspagina's** (`/properties/javea`, `/properties/benitachell`, `/properties/moraira`, `/properties/cumbre-del-sol`, `/properties/balcon-al-mar`, ... tot en met Madrid, Marbella, Mallorca) en **181 objectpagina's** met het vaste patroon `/properties/<zone>/<type>/<referentie>`. Over zes talen zijn dat ca. 1.086 object-URL's, maar het blijven 181 objecten.
- Objecttypen (EN): 110 villa, 20 apartment, 9 house, 7 ground-floor-apartment, 6 duplex-penthouse, 5 penthouse, 5 country-house, 4 flat, 3 plot, 3 town-house, 2 unique-building, en telkens 1 bar, building, castle, duplex, palace, semi-detached-house, semi-detached-villa.
- Referenties verraden de bron: 101 kale nummers (bijv. 6909 — kantoor Jávea), 57 met `V` (Valencia), 8 `AV`, 6 `ALI` (Arenal-appartementen), 8 `RMG-...P` (Marbella/partnernetwerk).
- Woorden als venta, inmueble, parcela komen in de URL's niet voor (de site is Engelstalig in de root); "villa", "apartment", "plot" wel, als typesegment.

Handig voor Deal Hunter: de sitemap is één bestand, klein genoeg om wekelijks te lezen en te vergelijken met de vorige week. Nieuwe object-URL's = nieuw aanbod; verdwenen URL's = verkocht of ingetrokken. Dat kost één verzoek per week.

## 4. Aanbodpagina en objectpagina

**Aanbodpagina:** https://www.rimontgo.com/properties/javea (24-09-2026, HTTP 200, ca. 197 kB). Titel: "Villas, apartments and flats for sale in Jávea | Rimontgó Real Estate". De pagina toont **10 objecten per pagina** met paginering `?page=2`, `?page=3` ... `?page=6` — dus hoogstens ca. 60 objecten onder het kopje Jávea [te verifiëren: pagina's 2–6 niet opgehaald]. Onderaan een zone-index met 29 deelgebieden die de site zelf onder Jávea hangt: Adsubia, Arenal, Avda. Augusta, Balcón al Mar, Cala Blanca, Cap Martí, Castellans, Costa Nova Panorama, Covatelles, Cuesta San Antonio, Cumbre del Sol (dat is Benitachell), El Garroferal, Granadella, Jávea Pueblo, La Corona, La Lluca, La Mandarina, Mar Azul, Montañar I en II, Montgó, Pinosol, Portichol, Puerto Jávea, Rafalet, Tarraula, Tossalet en Tossals. De lijstpagina zelf heeft geen JSON-LD; de objectkaarten linken met absolute URL's naar de objectpagina's.

**Objectpagina bekeken:** https://www.rimontgo.com/properties/balcon-al-mar/villa/6909 (24-09-2026, HTTP 200, ca. 173 kB, server-side gerenderd — alle gegevens staan in de HTML, geen JavaScript nodig).

- `<script type="application/ld+json">`: **ja, 1 blok**, `@type: RealEstateListing` met `mainEntity` van `@type: House`. Inhoud: `name` "6909 - Traditional Ibizan-style villa with sea views in Cap Negre, Jávea (Alicante)" (de **referentie 6909** zit dus in de naam en in de URL, niet in een apart veld), beschrijving, `url`, hoofdfoto (cdn.rimontgo.com → assets.rimontgo.com/images/properties/6909/...), `numberOfBedrooms` 4, `numberOfBathroomsTotal` 4, **`floorSize` 335.15**, adres met `addressLocality` **Jávea**, `addressRegion` Alicante, `addressCountry` ES. Onder `potentialAction` een `SellAction` met **`price` 3100000, `priceCurrency` EUR** en een `RealEstateAgent`-blok met het kantooradres Av. de Lepanto 1, 03730 Jávea, algemeen telefoonnummer en algemeen e-mailadres. (Dat blok bevat ook de naam van een contactpersoon; die is bewust niet overgenomen.)
- **Perceel staat niet in de JSON-LD**, wel in de leesbare tekst: de kerncijferbalk toont "4 · 4 · 335 m² · 1.118 m² · €3,100,000" — dus **bebouwd 335 m², perceel 1.118 m², prijs € 3.100.000**. Geen geo-coördinaten, geen bouwjaar, geen energielabel in de HTML gevonden.
- **og-tags: ja, compleet.** `og:title`, `og:description`, `og:url`, `og:site_name` (Rimontgó), `og:locale` en_GB met vijf `og:locale:alternate`, `og:image` (1200 px), `og:image:alt`, `og:type` website; plus `twitter:card/title/description/image`, een gewone `meta description` en een `canonical`.

Conclusie: uitstekend leesbaar. Prijs, bebouwd oppervlak, slaapkamers en plaats komen rechtstreeks uit de JSON-LD; perceel uit de kerncijferbalk; referentie en zone uit de URL.

## 5. Systeem achter de site — eigen bouw op Next.js, geen makelaars-CMS

Aanwijzingen (aanbod- en objectpagina, 24-09-2026):

- Antwoordkoppen: `server: nginx/1.28.3`, `x-powered-by: Next.js`, `x-next-i18n-router-locale: en`, `x-middleware-rewrite: /en/properties/balcon-al-mar/villa/6909`.
- 27 verwijzingen naar `_next/static`; beelden via `https://cdn.rimontgo.com/_next/image?url=https://assets.rimontgo.com/images/properties/<ref>/original_<uuid>.jpg` — eigen CDN en eigen asset-domein.
- Geen enkele `Set-Cookie` bij het ophalen (geen sessie of tracking nodig om te lezen).
- Geen sporen van Inmoweb, Mediaelx/LetsINMO, Sooprema, Inmovilla, Witei, WordPress (geen wp-content/wp-json), Elementor of "powered by". HTML-commentaar bestaat alleen uit lege React-markeringen.
- De verschillende referentiereeksen (kale nummers, V, AV, ALI, RMG-) wijzen op meerdere bronnen achter één eigen website: de kantoren Jávea en Valencia en het partnernetwerk (Marbella, Forbes Global Properties).

Een openbare exportfeed is niet gevonden en niet bekend [te verifiëren]. Omdat het kantoor zijn aanbod al deelt met internationale netwerken (Forbes Global Properties, Luxury Portfolio, Leading Real Estate Companies of the World, volgens de eigen menupagina's), is een feed op verzoek denkbaar, maar voor lezen is die niet nodig.

## 6. Schatting aanbod en dekking

Basis: de 181 objectpagina's in de Engelse sitemap (24-09-2026), ingedeeld op het zone-segment van de URL. De zone-index op de eigen Jávea-pagina (punt 4) bevestigt welke zones de site onder Jávea rekent.

| Gebied | Objecten | Toelichting |
|---|---|---|
| **Jávea** | **80** (+2 onzeker) | Arenal 11, Balcón al Mar 8, Cala Blanca 8, Tossalet 5, Adsubia 4, La Corona 4, Portichol 4, Puerto Jávea 4, Cuesta San Antonio 2, Jávea Pueblo 2, Mar Azul 2, Montgó 2, Pinosol 2, Tarraula 2, en telkens 1 in Alborada, Ambolo, Avda. Augusta, Castellans, Costa Nova (3 varianten), Covatelles, El Garroferal, Granadella, La Lluca, La Mandarina, La Plana, Mezquides, Montañar I, Montañar II, Partida Puchol, Rafalet, Tossals, Valls. Onzeker: `casco-antiguo` (1) en `la-marquesa-v` (1) — die zones staan niet in de Jávea-index van de site. |
| **Benitachell** | **1** | Cumbre del Sol (villa 7112) |
| **Moraira** | **2** | villa 6833 en 6847 |
| **Samen** | **83–85 van 181 ≈ 46 %** | |
| Overig Costa Blanca | ca. 22 | Dénia 5, La Sella Golf 5, San Juan 6, Sierra Cortina 4, Altea 2 |
| Valencia stad/provincie | ca. 35 | El Ensanche, Ciutat Vella, Rocafort, Torre en Conill, Ontinyent, enz. |
| Madrid, Marbella/Costa del Sol, Balearen, rest van Spanje | ca. 39 | |

Kanttekening: de eigen Jávea-pagina toont hoogstens ca. 60 objecten (6 pagina's × 10), terwijl de sitemap er 83–85 in Jávea/Benitachell/Moraira heeft. Het verschil is waarschijnlijk verkocht of ingetrokken aanbod dat nog in de sitemap staat, of objecten onder een andere gebiedspagina [te verifiëren bij de eerste volledige lees-ronde].

Voor Deal Hunter interessant in Jávea: de **3 percelen** (`adsubia/plot/6406`, `montgo/plot/7341`, `tossals/plot/7087`), het **bedrijfspand/bar in Jávea Pueblo** (`javea-pueblo/bar/6295`), de **huizen in het dorp en de haven** (`javea-pueblo/house/7297`, `puerto-javea/house/6028` en `6813`) en oudere villa's met lage referentienummers (bijv. `tossalet/villa/4727`, `denia/villa/4254`, `la-sella-golf/villa/3238` — hoe lager het nummer, hoe langer het object vermoedelijk al in de portefeuille zit). Prijsniveau is hoog (voorbeeldobject € 3,1 mln.).

## Aanpak (voorstel)

1. **Wekelijks** `sitemap.xml` ophalen (1 verzoek), de 181 object-URL's vergelijken met de vorige week: nieuw, verdwenen, gebleven.
2. Alleen **nieuwe** objectpagina's ophalen, één per ≥ 2 seconden, met een herkenbare User-Agent en contactadres.
3. Per object uit de JSON-LD halen: prijs, valuta, bebouwd m², slaapkamers, badkamers, plaats; uit de kerncijferbalk: perceel m²; uit de URL: zone, type, referentie. Opslaan met bron-URL en datum. Geen tekst, geen foto's.
4. Lang openstaande objecten (referentie blijft weken staan, prijs zakt) markeren als onderhandelingskans.
5. Zones die de site onder Jávea rekent (lijst in punt 4) gebruiken als filter; `cumbre-del-sol` en `moraira` apart tellen.

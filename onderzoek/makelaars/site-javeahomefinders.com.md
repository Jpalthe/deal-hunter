# Toets op automatisch lezen: javeahomefinders.com

**Kantoor:** Javea Home Finders (rechtspersoon volgens de voorwaarden: JAVEA HOME FINDERS XXI, S.L.)
**Website:** https://www.javeahomefinders.com
**Kantooradres (uit JSON-LD en footer):** Avda. de la Libertad 19, local 11, 03730 Jávea
**Algemene contactkanalen:** +34 966 470 133 · WhatsApp +34 661 299 625 · info@javeahomefinders.com
**Datum toets:** 24-09-2026 (avond)
**Advies: FEED VRAGEN**

Vijf pagina's van de site opgehaald, met minstens 2 seconden tussenpoos: robots.txt, sitemap.xml,
de aanbodpagina "Property Sales Javea", één objectpagina en de pagina "Terms & Conditions".
Daarnaast één pagina van de softwareleverancier (easyinmo.es). Geen inlog, geen formulier.

## 1. robots.txt — toegestaan

Bron: https://www.javeahomefinders.com/robots.txt (HTTP 200, 24-09-2026). Volledige inhoud:

```
User-agent: *
disallow: /your-page/
disallow: /admin/
disallow: /admin2/
```

Voor `User-agent: *` zijn alleen `/your-page/` en de twee beheermappen afgeschermd. De
objectpagina's (`/<nummer>/property/<slug>`) en de aanbodpagina's (`/property-sales-javea`,
`/search-property`) vallen daar niet onder en mogen dus technisch gelezen worden.
Er staat **geen** `Sitemap:`-regel in.

## 2. Voorwaarden — verbieden hergebruik en "extractie" voor commerciële doelen

Bron: https://www.javeahomefinders.com/terms-and-conditions (HTTP 200, 24-09-2026), gelinkt
vanuit de footer ("Terms and Conditions") en bij elk formulier. Het is een Engelse vertaling van
Spaanse gebruiksvoorwaarden ("This is a translation. In case of doubt, the Spanish version will
take precedence" — een link naar die Spaanse versie staat niet in de HTML).

Het woord "scraping" of "robot" komt niet voor, maar artikel 4 (Intellectual and Industrial
Property Rights) verbiedt wél precies wat een automatische lezer doet:

> "...the User is expressly prohibited from reproducing, transforming, distributing, publicly
> communicating, making available, **extracting, reusing**, resending, or using any of them by
> any means or procedure, except in cases where this is legally permitted or is authorised by
> the owner of the corresponding rights."

> "The User may view and obtain a temporary private copy of the Contents for his/her exclusive
> personal and private use ... **provided that this is not for the purpose of carrying out any
> commercial or professional activities.** The User shall refrain from obtaining, or attempting
> to obtain, the Contents by means or procedures other than those which in each case was made
> available or indicated for that purpose or those which are normally used on the Internet..."

Verder: artikel 7 (het kantoor behoudt zich rechtsmaatregelen voor bij overtreding), artikel 9
(Spaans recht, rechtbanken van Dénia). Een aparte "Legal Notice" wordt genoemd maar is niet
als eigen pagina gelinkt; de contactgegevens staan in de footer.

**Conclusie:** Deal Hunter is een commerciële/professionele activiteit; systematisch uitlezen
en hergebruiken van het aanbod valt onder het verbod van artikel 4. Dat mag dus niet zonder
toestemming van het kantoor. De GDPR-pagina (`/our-gdpr-policies`) is niet geopend (paginabudget).

## 3. Sitemap — 154 URL's, waarvan 107 objectpagina's

Bron: https://www.javeahomefinders.com/sitemap.xml (HTTP 200, 24,9 kB, 24-09-2026). Eén platte
sitemap, zonder `lastmod`. Telling:

- 154 URL's in totaal; 47 gewone pagina's (over Jávea, kopersgids, team, blog, GDPR, enz.)
- **107 objectpagina's** van de vorm `/<id>/property/<type>-for-sale-in-<plaats>-<referentie>`
- Per plaats in de URL: **Jávea 60, Benitachell 25, Moraira 5**, Llíber 4, Dénia 4, Benissa 3,
  Altea 3, Calpe 2, 1 zonder plaats in de slug
  (`/1932/property/contemporary-luxury-villa-with-pool-jacuzzi-and-custom-features`)
- Per type: villa 78, apartment 22, penthouse 3, land-plot 2, townhouse 1 (+1 zonder type)
- Zoektermen uit de opdracht: "property" 111 treffers, "villa" 80, "apartment" 23, "plot" 3;
  "venta", "inmueble", "apartamento", "parcela" 0 (de sitemap is Engelstalig). De Spaanse,
  Nederlandse, Franse en Duitse versies staan op subdomeinen (`es.`, `nl.`, `fr.`, `de.`) en zitten
  niet in deze sitemap.

## 4. Aanbodpagina en objectpagina

- **Aanbodpagina uit de navigatie:** https://www.javeahomefinders.com/property-sales-javea
  (HTTP 200, 42 kB). Dit blijkt een tekstpagina (uitleg over villa's, appartementen, wijken) met
  **nul objectlinks**; de drie `property-card`-blokken zijn typebeschrijvingen, geen woningen.
  De echte zoekpagina staat in de footer als "Search": https://www.javeahomefinders.com/search-property
  — niet geopend (paginabudget), dus onbekend of die statisch of via JavaScript laadt.
  Ook: `/exclusive-properties`, `/property-sales-benitachell`, `/property-sales-moraira`.
- **Objectpagina bekeken** (HTTP 200, 92 kB, `meta robots: index,follow`, canonical aanwezig):
  https://www.javeahomefinders.com/2147/property/villa-for-sale-in-javea-1771H2-vlc

**JSON-LD:** 1 blok, maar alleen `@type: RealEstateAgent` (kantoornaam, adres, telefoon).
**Geen** `RealEstateListing`/`Offer` — prijs, oppervlakte en plaats staan **niet** in JSON-LD.

**og:-tags (wel aanwezig):**
- `og:title` en `og:description`: "Ref: 1771H2-vlc | €1,200,000 | Beds: 4 | Baths: 6 | Villa for sale in Jávea, Alicante"
- `og:url`: generiek `https://www.javeahomefinders.com/property` (niet de eigen URL)
- `og:image`: het kantoorlogo (`/images/fblogo.png`), `og:image:alt` bevat de korte omschrijving
- `og:locale`: en-gb; `og:site_name`: JaveaHomeFinders.com

**Zichtbaar op de pagina (platte tekst, geen tabelvelden):** referentie `1771H2-vlc`, prijs
`€1,200,000`, type Villa, plaats "Jávea, Tesoro Park", 4 Bedrooms, 6 Bathrooms, **Build 349m²**,
**Plot 1,390m²**, "Good condition", "Private pool", "Mountain View", label "Exclusive",
60 foto's, lange Engelse beschrijving. `<title>` en `meta description` zijn identiek aan de og-tags.
`hreflang`-links naar es/nl/fr/de-subdomeinen per object.

## 5. Systeem achter de site: EasyInmo (makelaars-CMS uit Alicante, eigen platform)

Bewijs (24-09-2026):
- `<meta name="generator" content="EasyInmo">` op de aanbod- én objectpagina
- Eigen paden, geen WordPress: `/clientPages/js/portfolio.js`, `/functions/popUpQuestionsSite/`,
  `/modules/forms/css/forms.css`, `/js/property-view.js`, `/globalJS/jquery.colorbox.js`;
  beelden en css op `cdn.javeahomefinders.com` en `images.javeahomefinders.com`
- Server `nginx`; geen server-side cookies bij het ophalen; wel Google Tag Manager en Meta Pixel
- Geen sporen van Inmoweb, Mediaelx/LetsINMO, Sooprema, Inmovilla, Witei, Kyero-widgets of
  `wp-content` (0 treffers in beide pagina's); één verwijzing naar getsmart.es (niet uitgezocht)
- Leverancier: https://easyinmo.es ("EasyInmo Website and CRM System", Alicante, algemeen adres
  info@easyinmo.es; HTTP 200, 24-09-2026) adverteert letterlijk met "Automated XML Exports",
  "Unlimited XML Feeds Out", "XML Feed Specifications" en "Kyero". Het CMS kent dus een exportfeed.
  Dit sluit aan bij B01-crm-feeds.md (16-09-2026), waar Javea Home Finders al op de reservelijst
  "feed vragen" staat.

## 6. Omvang en dekking Jávea / Benitachell / Moraira

Op basis van de 107 object-URL's in de sitemap (24-09-2026):
- **Jávea 60 (56%)**, Benitachell 25 (23%), Moraira 5 (5%) → **samen 90 van 107 = 84%**
- Buiten ons gebied: Llíber 4, Dénia 4, Benissa 3, Altea 3, Calpe 2 (16%)
- Aanbod is vrijwel geheel koop (URL's zeggen "for-sale"); 2 percelen ("land-plot") in Jávea,
  78 villa's — het profiel van een klassieke Jávea-resale-makelaar in het hogere segment.
- Referenties met achtervoegsel `-vlc` (Jávea-objecten) en losse nummers (Benitachell/Cumbre del
  Sol, bv. 21294, 25427) wijzen op minstens twee bronnen/feeds in het CRM **[te verifiëren]**.

**Schatting:** ~107 objecten online, ~90 in Jávea/Benitachell/Moraira.

## Advies en werkwijze

**Feed vragen.** robots.txt laat het lezen toe en de pagina's zijn goed leesbaar (prijs, plaats,
bouw- en perceeloppervlak staan als tekst, og-tags geven ref/prijs/type/plaats), maar de
gebruiksvoorwaarden verbieden uitdrukkelijk het extraheren en hergebruiken van de inhoud voor
commerciële of professionele doeleinden. Zonder toestemming dus niet automatisch lezen.
Het systeem (EasyInmo) heeft een ingebouwde XML-exportfeed (Kyero-formaat), dus de nette weg is
een feedverzoek aan het kantoor.

⏸️ ACTIE VOOR JAN
1. Kantoor benaderen via de algemene kanalen (info@javeahomefinders.com / +34 966 470 133) met
   het verzoek om een XML-feed (Kyero-formaat) van het koopaanbod in Jávea, Benitachell en Moraira,
   of om schriftelijke toestemming om de site te lezen. Contactvoorstel staat al klaar in de
   reservelijst van B01-crm-feeds.md.
2. Bij akkoord: feed-URL vastleggen in het bronnenregister; niet de website lezen.

Als er wél toestemming komt om de site te lezen, dan zo:
1. Lijst uit `/sitemap.xml` (107 URL's, geen `lastmod` — dagelijks vergelijken op nieuwe id's).
2. Per object: referentie, prijs, type en plaats uit `og:title`; bouw- en perceeloppervlak uit de
   tekstregels "Build ...m²" / "Plot ...m²"; wijk uit de regel na het type ("Jávea, Tesoro Park").
3. JSON-LD is hier onbruikbaar voor objectdata (alleen kantoorgegevens).
4. Objecten buiten Jávea/Benitachell/Moraira (Llíber, Dénia, Benissa, Altea, Calpe) overslaan.
5. Geen persoonsgegevens: de site heeft een teampagina (`/meet-the-team`); alleen de bedrijfsnaam
   en de algemene contactkanalen gebruiken.

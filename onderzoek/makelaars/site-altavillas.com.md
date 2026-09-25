# Alta Villas — altavillas.com — toets op automatisch lezen

Datum toets: 24-09-2026 · Onderzoeker: TREE Deal Hunter (automatische toets)
Kantoor: Alta Villas Properties, S.L. · Avenida de la Libertad 19, Local 12, 03730 Jávea (Alicante)
Algemene kanalen: office@altavillas.com · +34 965 796 311 · WhatsApp +34 635 720 355
(bron: https://altavillas.com/ en https://altavillas.com/privacy-policy, 24-09-2026)

## Advies in één zin

**Overslaan voor automatisch lezen.** robots.txt staat alles toe, maar de gebruiksvoorwaarden
van het kantoor verbieden het overnemen en hergebruiken van de inhoud voor commercieel of
professioneel gebruik, en het systeem achter de site is geen bekend platform met een exportfeed.
De enige nette weg is een directe afspraak met het kantoor (handmatig, niet geautomatiseerd).

## 1. robots.txt — toegestaan

Bron: https://altavillas.com/robots.txt (opgehaald 24-09-2026, HTTP 200). Volledige inhoud:

```
User-agent: *
Disallow:
Sitemap: https://altavillas.com/sitemap.xml
```

Een lege `Disallow:` betekent: alles mag worden gelezen, ook de aanbod- en objectpagina's.
Er staat geen aparte regel voor specifieke bots.

## 2. Gebruiksvoorwaarden — verbieden overnemen voor commercieel gebruik

Op de homepage staat alleen een link "Privacy Policy" (https://altavillas.com/privacy-policy);
er is geen aparte pagina "terms" of "aviso legal". Die ene pagina bevat echter drie stukken:
de wettelijke kennisgeving (Legal Notice, art. 10 LSSI), de **General Conditions of Use of
www.altavillas.com** (GCU) en de privacyverklaring. Opgehaald 24-09-2026.

Relevante bepalingen uit de GCU (Engelse tekst, letterlijk):

- Hoofdstuk 4, Intellectual and Industrial Property Rights: "the User is expressly prohibited
  from the following reproduction, transformation, distribution, public communication, making
  available, **extraction, reuse**, resending or use of any nature, by any means or procedure,
  of any of them, except in the cases in which it is legally permitted or authorised by the
  owner of the corresponding rights."
- Idem: "The User may view and obtain a temporary private copy of the Contents for his or her
  exclusive personal and private use ... **as long as this is not for the purpose of carrying
  out commercial or professional**. The User shall refrain from obtaining or attempt to obtain
  the Contents by means or procedures other than those which in each case have been made
  available or indicated for this purpose or those normally used on the Internet".
- Hoofdstuk 7: het kantoor behoudt zich het recht voor juridische stappen te nemen bij
  overtreding; hoofdstuk 9: Spaans recht, rechtbank Dénia.

De woorden "scraping" of "robots" komen niet letterlijk voor, maar "extraction" en "reuse" voor
commercieel/professioneel gebruik zijn expliciet verboden zonder toestemming. Voor een
acquisitiesysteem als Deal Hunter (professioneel gebruik) geldt dat verbod.

## 3. Sitemap — kapot

robots.txt wijst naar https://altavillas.com/sitemap.xml. Die URL gaf op 24-09-2026 een
**HTTP 500** (serverfout, body: "500"). Aantal object-URL's kon daardoor niet worden geteld.
`/sitemap_index.xml` is niet geprobeerd: het budget van vijf verzoeken was nodig voor de
homepage, de voorwaarden en een objectpagina.

## 4. Aanbodpagina en objectpagina

- Aanbod te koop: https://altavillas.com/property-search (zoekpagina) en per plaats
  https://altavillas.com/properties/for-sale/javea, `/moraira`, `/denia`, `/jalon`.
  Filters staan als base64-gecodeerde JSON in de URL (`?q=...`), bijvoorbeeld
  `{"available_for":{"key":"1","txt":"FOR SALE"},"property_type":{"key":"3179","txt":"Villa"}}`.
- Objectpagina's: patroon `/property/<omschrijving>-avs-<nummer>` (referenties "AVS 57814",
  "AVSS 104908").

Bekeken objectpagina (24-09-2026, HTTP 200):
https://altavillas.com/property/4-bedroom-villa-for-sale-in-javea-avs-57814

| Kenmerk | Gevonden |
|---|---|
| `<script type="application/ld+json">` | **Nee** — geen schema.org-blok |
| og:-tags | Ja: og:title, og:type ("property"), og:url, og:image (800×600); twitter:card. **Geen** prijs, oppervlakte of plaats in de og-tags |
| Prijs | "Price on request" (geen bedrag); bij de "Similar properties"-blokken staan wél bedragen als platte tekst (bv. €4,200,000) |
| Bouwoppervlak | 277 m² Built Area |
| Perceel | 1141 m² Plot Area |
| Plaats | Javea (kop: "4 Bedroom Villa for Sale in Javea - AVS 57814"; nabij Arenal) |
| Referentie | AVS 57814 |
| Overig | 4 slaapkamers, 3 badkamers, bouwjaar 2027 (projectbouw), lijst met voorzieningen als kommagescheiden tekst |

De gegevens staan als gewone HTML-tekst in de pagina (geen JavaScript nodig), maar zonder
gestructureerde markering: elke waarde moet uit de opmaak worden gevist.

## 5. Systeem achter de site — onbekend, geen bekend Spaans makelaars-CMS

Aanwijzingen (homepage en objectpagina, 24-09-2026):

- Cookie `JSESSIONID` op elke pagina → Java-serverapplicatie (servlet/Tomcat-achtig).
- Scripts en stijlen: `/res/7/rg.min.js`, `/res/7/rg.min.css`, `/res/cdn/jquery.min.js`,
  `/combined.js?id=...`; eigen JS-namespace `WUtils.showPopup`, `WUtils.like`, `WUtils.postForm`;
  icoonklassen met voorvoegsel `rgi-`.
- Zoekfilters als base64-JSON in de URL en MongoDB-achtige query's in de pagina (`"bedrooms" : { "$gte" : 3.0 }`).
- Afbeeldingen onder `/images/<id>-2034.jpeg` en `/images/w800_2034/...` (2034 lijkt een klant-id).
- Cookiebanner van CookieScript, Google Translate-widget, lettertypen Roboto/Play via Google Fonts.
- Geen `wp-content`, geen html-commentaar, geen "powered by", geen sporen van Inmoweb, Mediaelx/LetsINMO,
  Sooprema, Inmovilla of Witei.

Conclusie: een eigen of niche-platform op Java; welk bedrijf erachter zit is niet vastgesteld
(de zoekmachine was in deze sessie niet meer beschikbaar). Of dit systeem een exportfeed
(bijv. Kyero/Idealista-XML) kan leveren, is onbekend.

## 6. Omvang en dekking Jávea

- Aantal objecten: **niet vast te stellen** (sitemap kapot, aanbodpagina niet opgehaald binnen
  het budget). Op de twee bekeken pagina's samen kwamen 15 unieke objecten voor.
- Dekking: **hoog voor Jávea.** Alle 11 uitgelichte objecten op de homepage en alle 8 gelinkte
  objecten op de objectpagina liggen in Jávea (24-09-2026). Het kantoor zit in Jávea en noemt als
  werkgebied Jávea, Moraira, Dénia en de Jalón/Orba-vallei. Benitachell wordt niet apart genoemd.
- Aparte site voor het luxe segment: https://altavillasluxury.com (niet getoetst).

## Advies en vervolg

**Advies: overslaan** (automatisch lezen). robots.txt laat het toe, maar de voorwaarden
verbieden extractie en hergebruik voor professioneel gebruik, en er is geen bekend systeem met
een feed om netjes om te vragen.

⏸️ ACTIE VOOR JAN (optioneel): dit kantoor heeft veel Jávea-aanbod. Wil je het toch meenemen,
dan is een directe afspraak met het kantoor de enige nette route (samenwerking tussen makelaars
of een gedeelde feed). Algemene kanalen: office@altavillas.com, +34 965 796 311.

## Verzoeken aan de site (max. 5, ≥ 2 s tussenpoos)

1. https://altavillas.com/robots.txt — 200
2. https://altavillas.com/sitemap.xml — 500
3. https://altavillas.com/ — 200
4. https://altavillas.com/property/4-bedroom-villa-for-sale-in-javea-avs-57814 — 200
5. https://altavillas.com/privacy-policy — 200

# Villalux — www.villalux.com — toets op automatisch lezen

Datum toets: 24-09-2026 (avond). Onderzoek voor TREE Deal Hunter.
Opgehaald: robots.txt, homepage, legal notice, sitemap.xml, één objectpagina (vijf inhoudspagina's; twee extra
verzoeken vanuit een scriptclient kregen alleen een "Security Check"-pagina, zie hieronder). Tussen de verzoeken
ruim 14 seconden, zoals robots.txt vraagt.

## Kort antwoord

**Advies: lezen — met drie voorwaarden.** Robots.txt staat het toe, de voorwaarden verbieden het niet en de
pagina's zijn leesbaar. Maar: (1) via de sitemap werken, want bladerpagina's zijn verboden; (2) minstens 14 seconden
tussen twee verzoeken (Crawl-delay); (3) de site heeft een JavaScript-botschild dat kale scripts tegenhoudt — als
onze lezer daar tegenaan loopt, niet omzeilen maar het kantoor om een feed vragen.

## 1. robots.txt — toegestaan, met beperkingen

Bron: https://www.villalux.com/robots.txt (24-09-2026, HTTP 200).

Voor `User-agent: *` is bijna alles toegestaan (`Allow: /`), behalve formulieren, galerij-modals, printversies,
`/images/`, `/admin/` en — belangrijk — alle bladerpagina's van overzichten:

```
User-agent: *
Disallow: /images/
Disallow: /html/formulario/llamanos/
Disallow: /html/galeriamodal/*
Disallow: /html/formucontraoferta/*
Disallow: /*/*/*/pagina/*
Disallow: /*/*/*/pages/*
Disallow: /*/*/*/page/*
...
Allow: /
```

Onderaan staat bovendien:

```
User-agent: *
Crawl-delay: 14
```

Daarnaast een lange lijst met verboden bots (Wget, Python-urllib, HTTrack, WebZip, WebCopier, e.d.). Er staat
géén `Sitemap:`-regel in.

Betekenis: objectpagina's en de eerste overzichtspagina mag je lezen; pagina 2, 3, … van een overzicht niet.
Alle objecten bereik je dus alleen via de sitemap. En: maximaal één verzoek per 14 seconden.

## 2. Voorwaarden — geen verbod op automatisch lezen

Bron: https://www.villalux.com/legal-notice/ (24-09-2026). Koppen: Legal notice, General Terms of Use, Personal
Data, User Commitments, Security, Complaints, Intellectual and Industrial Property Rights, External Links,
Applicable Law, Contact, Privacy Policy, Cookies Policy.

Er staat **geen bepaling over robots, crawlers, scraping of geautomatiseerde toegang**. Wel het gebruikelijke
auteursrechtartikel: de hele site, "el texto, software, contenidos (...) fotografías, material audiovisual y gráficos,
está protegida por marcas, derechos de autor y otros derechos legítimos" — reproductie, verspreiding of wijziging
zonder toestemming is verboden. Dat raakt hergebruik van foto's en teksten, niet het lezen en analyseren zelf.

Let op: de rechtspersoon in de legal notice is **Sanders Mediterráneo S.L.** (CIF B53634770), Avenida del Pla 135,
03730 Xàbia — niet "Villalux S.L." zoals in onze lijst. Algemene kanalen: +34 96 579 40 59, info@villalux.com.

## 3. Sitemap — 153 URL's, ongeveer 86 objecten

Bron: https://www.villalux.com/sitemap.xml (24-09-2026). Gewone urlset, geen index.
- Totaal 153 URL's.
- Ongeveer 86 objectpagina's, herkenbaar aan `/for-sale/<omschrijving>-v####/` (referentie V2815, V2814c, …).
- Ongeveer 67 overige pagina's (blog, dienstenpagina's, locatiepagina's zoals
  `/properties-for-sale-in-javea-with-sea-views/`).
- Voorbeelden: `/for-sale/renovated-golfside-villa-with-montgo-views-v2815/`,
  `/for-sale/villa-for-sale-in-javea-with-sea-views-pool-tourist-licence-v2811/`.

De tellingen komen uit een geautomatiseerde lezing van de XML en zijn bij benadering.

## 4. Objectpagina — prijs, maten en referentie staan er gewoon

Bron: https://www.villalux.com/for-sale/renovated-golfside-villa-with-montgo-views-v2815/ (24-09-2026).
- Vraagprijs € 700.000 · bebouwd 240 m² · perceel 924 m² · 5 slaapkamers · 4 badkamers
- Plaats: Jávea, zone La Mandarina (tegenover de golfclub) · referentie V2815

JSON-LD (`application/ld+json`) en og:-metatags: **onbekend.** De lezer die de pagina wél binnenkreeg (WebFetch)
laat scripts en meta-tags niet zien; de ruwe HTML via een scriptclient kreeg het botschild (zie 5). Niet verder
geprobeerd om binnen vijf pagina's te blijven en het schild niet te omzeilen.

## 5. Systeem achter de site — eigen/onbekend platform met botschild

- Aanwijzingen: assets onder `/crm/pages/agencies/villaluxjavea/assets/` → een CRM-platform dat meerdere
  kantoren host (white-label). Geen wp-content, geen kenmerken van Inmoweb, Mediaelx/LetsINMO, Sooprema,
  Inmovilla of Witei. Paden in robots.txt (`/html/formulario/`, `/portal/proceso/`, `/html/galeriamodal/`) wijzen
  op een eigen sjabloon.
- **Botschild:** een verzoek zonder browser (curl) naar de homepage én naar sitemap.xml kreeg op 24-09-2026
  een pagina "Verifying your browser — This is an automatic security check", "Powered by Paagees Shield",
  HTTP 200, header `x-robots-tag: noindex, nofollow`. Het is een JavaScript-rekenpuzzel (SHA-256 proof-of-work)
  die een cookie `__shield` zet. Een tweede lezer (WebFetch) kreeg de echte pagina's wél gewoon. Het schild is dus
  selectief; welke regel het hanteert is niet bekend.
- Vermoeden: Paagees is de leverancier van het platform — **[te verifiëren]** (zoekbudget voor vandaag was op).
- Exportfeed: onbekend. Een kantoor met dit soort CRM levert meestal wel een XML-feed aan portalen (Kyero,
  Idealista); dat is de route om te vragen als het schild ons tegenhoudt.

## 6. Omvang en dekking Jávea

- Sitemap: ~86 objectpagina's. Homepage (24-09-2026) noemt per categorie: 94 villa's, 20 appartementen,
  68 luxe woningen, 25 nieuwbouw — categorieën overlappen, dus niet optellen. Schatting: **circa 90–115 objecten**.
- Dekking: van de ~86 object-URL's noemen er ~76 Jávea/Xàbia in de slug, 1 Moraira, 1 Benitachell/Cumbre.
  Ruwweg **90 % Jávea**, vrijwel niets in Moraira of Benitachell. Voor de Deal Hunter is dit een kernkantoor.

## Wat het voor de Deal Hunter betekent

1. Lezen mag, met 14 s tussen verzoeken: ~86 objecten kost zo'n 20–25 minuten per volledige ronde.
2. Alleen via sitemap.xml; nooit `/page/`-, `/pagina/`-URL's opvragen.
3. Bouw de lezer zo dat hij bij "Verifying your browser" stopt en dit meldt — niet oplossen, niet cookie namaken.
4. Foto's en teksten niet overnemen of publiceren (auteursrecht); alleen kenmerken en prijzen analyseren.
5. Als het schild structureel blokkeert: kantoor vragen om de portaalfeed (info@villalux.com).

⏸️ ACTIE VOOR JAN: niets nu. Pas als het schild onze lezer blokkeert: feed vragen bij het kantoor.

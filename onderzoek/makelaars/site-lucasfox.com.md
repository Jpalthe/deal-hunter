# Lucas Fox Jávea — toets op automatisch lezen

Datum: 24-09-2026 · Onderdeel van TREE Deal Hunter (makelaarssites Jávea)
Site: https://www.lucasfox.com/property/spain/costa-blanca/javea.html

## Kort oordeel

**Advies: overslaan** (voor nu). robots.txt staat lezen toe, maar de site zit achter
Cloudflare-botbeveiliging: elke automatische ophaalactie van een inhoudspagina krijgt
een "Just a moment..."-controlepagina (HTTP 403, header `cf-mitigated: challenge`).
Die controle omzeilen we niet. De gebruiksvoorwaarden konden daardoor niet gelezen
worden, en er is geen objectpagina gezien. Het systeem is een eigen bouw, dus een
standaard-exportfeed (Inmoweb/Mediaelx/Sooprema) is er niet.

## 1. robots.txt — toegestaan, met 10 seconden wachttijd

Bron: https://www.lucasfox.com/robots.txt (HTTP 200, 24-09-2026).
Let op: het bestand staat op de root van het domein; het letterlijke pad uit de
opdracht (`.../javea.html/robots.txt`) geeft een 404-pagina.

Relevante regels, letterlijk:

```
User-agent: *
Crawl-delay: 10
Disallow: /admin/
Disallow: /udf/
Disallow: /pdf/
Disallow: /information-request.html
Disallow: /viewing-request.html
Sitemap: https://www.lucasfox.com/sitemap.xml
```

Conclusie: een `User-agent: *` mag de aanbod- en objectpagina's onder `/property/`
lezen; alleen beheer, `/udf/`, pdf's en de twee aanvraagformulieren zijn verboden.
Voorwaarde: minimaal 10 seconden tussen twee verzoeken (strenger dan onze eigen
regel van 2 seconden). Daar heb ik me tijdens deze toets aan gehouden.

## 2. Gebruiksvoorwaarden — niet leesbaar (niet gevonden)

- Poging: https://www.lucasfox.com/legal-notice.html → HTTP 403 (Cloudflare), 24-09-2026.
- De 404-pagina van de site bevat geen footerlinks naar juridische pagina's, dus de
  exacte URL van de voorwaarden is niet vastgesteld.
- Een zoekmachine-opzoeking was niet mogelijk (zoekbudget van deze sessie was op).

Er kan dus **niet** gezegd worden of de voorwaarden scraping verbieden. Status:
"niet gevonden". Dit moet opnieuw bekeken worden zodra iemand de pagina handmatig
in een browser opent.

## 3. Sitemap — bestaat volgens robots.txt, maar niet leesbaar

- URL (uit robots.txt): https://www.lucasfox.com/sitemap.xml
- Ophalen op 24-09-2026: HTTP 403, Cloudflare-controlepagina in plaats van XML.
- Aantal object-URL's: **niet vast te stellen**.

## 4. Aanbodpagina en objectpagina — geblokkeerd

- https://www.lucasfox.com/property/spain/costa-blanca/javea.html → HTTP 403,
  `server: cloudflare`, `cf-mitigated: challenge`, `<title>Just a moment...</title>`
  (24-09-2026).
- Geen objectpagina geopend. JSON-LD en og:-tags: **onbekend**.

## 5. Systeem achter de site — eigen bouw

Aanwijzingen (alle uit de 404-pagina, de enige echte sitepagina die wél doorkwam,
24-09-2026):
- Eén eigen stylesheet `/assets/css/styles.css`, eigen webfonts
  `/assets/webfonts/figtree-*.woff2`, `/manifest.json`, `<html data-theme="classic">`.
- Geen `wp-content`, geen "powered by", geen sporen van Inmoweb, Mediaelx/LetsINMO,
  Sooprema, Inmovilla of Witei.
- Voor de site staat Cloudflare (headers `server: cloudflare`, `cf-ray ...-MAD`).
- Footer: "Dils Lucas Fox Head Office", tel. (+34) 933 562 989, info@lucasfox.com,
  "Registro de Agentes Inmobiliarios de Cataluña: AICAT 3265".

Conclusie: **eigen bouw** van een groot kantoor, geen standaard-CMS met exportfeed.

## 6. Omvang en Jávea-dekking — niet gemeten

- Aantal objecten: **onbekend** (aanbodpagina en sitemap niet leesbaar).
- Dekking Jávea/Benitachell/Moraira: **onbekend**. Wat wel vaststaat: de URL-opbouw
  `/property/spain/costa-blanca/javea.html` is land → regio → plaats, en het
  hoofdkantoor heeft een Barcelonees netnummer (93). Jávea is dus één vestiging van
  een landelijk kantoor; het Jávea-aanbod is naar verwachting een klein deel van het
  totaal. Dat is een afleiding, geen telling — **[te verifiëren]**.

## Wat er gedaan is (logboek)

| # | Verzoek | Resultaat |
|---|---|---|
| 1 | /robots.txt | 200, leesbaar |
| 2 | /property/spain/costa-blanca/javea.html/robots.txt (letterlijk pad) | 404-pagina |
| 3 | /sitemap.xml | 403 Cloudflare-controle |
| 4 | /property/spain/costa-blanca/javea.html | 403 Cloudflare-controle |
| 5 | /legal-notice.html (via WebFetch) | 403 |

Vijf verzoeken, telkens minstens 10 seconden ertussen, gewone browser-identificatie,
geen omzeiling van de controle.

## Vervolg

⏸️ ACTIE VOOR JAN (optioneel): Lucas Fox is een landelijk kantoor met eigen
techniek; als hun Jávea-aanbod belangrijk is voor Deal Hunter, is de nette route
om het kantoor rechtstreeks te vragen naar een XML-feed of samenwerking
(algemeen kanaal: info@lucasfox.com, +34 933 562 989). Tot die tijd: overslaan en
hun objecten via de portalen volgen waar ze zelf publiceren.

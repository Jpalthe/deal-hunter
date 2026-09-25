# Hernani Homes S.L. — toets op automatisch lezen

**Datum:** 24-09-2026
**Site:** http://www.hernanihomes.com
**Advies: OVERSLAAN.** Er staat op dit moment géén website op dit domein. De server geeft alleen de standaardpagina van het hostingpakket (Plesk) terug; er is geen robots.txt, geen sitemap, geen aanbodpagina en geen objectpagina. Er valt dus niets te lezen en ook niets om een feed voor te vragen. Volgens het internetarchief is de site sinds uiterlijk 30-08-2024 uit de lucht.

## Wat is er opgehaald (4 pagina's met antwoord + 3 verbindingspogingen, telkens minstens 2 seconden ertussen)

| # | URL | Resultaat |
|---|-----|-----------|
| 1 | http://www.hernanihomes.com/robots.txt | **404 Not Found** (Apache) |
| 2 | https://www.hernanihomes.com/robots.txt | geen antwoord: TLS-certificaat hoort niet bij dit domein (zie stap 5) |
| 3 | http://www.hernanihomes.com/ | 200, maar alleen "Web Server's Default Page" van Plesk (1.658 bytes, `Last-Modified: 27-02-2026`) |
| 4 | http://hernanihomes.com/ | 200, dezelfde Plesk-standaardpagina |
| 5 | http://www.hernanihomes.com/sitemap.xml | **404 Not Found** |

Daarnaast alleen DNS-opvragingen en het internetarchief (archive.org), die de server van het kantoor niet belasten.

## 1. robots.txt — GEEN robots.txt

Bron: http://www.hernanihomes.com/robots.txt (24-09-2026) → HTTP 404, standaard Apache-foutpagina:

```
HTTP/1.1 404 Not Found
Server: Apache
<title>404 Not Found</title> … The requested URL was not found on this server.
```

Formeel verbiedt niets een `User-agent: *`, maar dat is hier zonder betekenis: er zijn geen aanbodpagina's om te lezen.

## 2. Gebruiksvoorwaarden — NIET GEVONDEN

De enige pagina die de server nog uitlevert is de Plesk-standaardpagina (bron: http://www.hernanihomes.com/, 24-09-2026), met alleen tekst over Plesk zelf ("What is Plesk … Try Plesk Now!"). Geen aviso legal, geen términos, geen cookiebeleid. In het archief van 07-08-2020 stond wel een link naar `/cookies-policy/` (bron: https://web.archive.org/web/20200807121457/https://www.hernanihomes.com/apartments-in-javea/), maar die pagina bestaat nu niet meer en is niet geopend. Er is dus geen verbod gevonden — er is simpelweg geen site.

## 3. Sitemap — GEEN

- robots.txt bestaat niet, dus ook geen `Sitemap:`-regel.
- http://www.hernanihomes.com/sitemap.xml → 404 (24-09-2026).
- `sitemap_index.xml` niet apart geprobeerd: het paginabudget was op en de kans op een sitemap zonder site is nihil.

Aantal object-URL's: **0 / niet te tellen.**

## 4. Objectpagina — GEEN

Er is geen aanbodpagina en geen objectpagina. JSON-LD en og-tags: **onbekend**.

Ter vergelijking, uit het archief (07-08-2020, bron: https://web.archive.org/web/20200807121457/https://www.hernanihomes.com/apartments-in-javea/): de toenmalige aanbodpagina had **geen** `application/ld+json` en **geen** `og:`-tags; prijzen en referenties stonden als gewone tekst in objectkaarten ("Ref. A-199 … 99.000€", labels "Reduced" en "Sold"). Dat zegt alleen iets over de oude site, niet over een eventuele nieuwe.

## 5. Systeem achter de site — NU: NIETS (hostingpagina); TOT 2024: SOOPREMA

Nu (24-09-2026):
- HTTP-headers: `Server: Apache`, `X-Powered-By: PleskLin` → Plesk-hostingpakket zonder website erin.
- DNS: A-record 82.223.139.69, naamservers `ns2.dondominio.com` / `ns8.dondominio.com` (het domein is dus nog geregistreerd). MX: 10 mx01.dondominio.com..
- Het TLS-certificaat op poort 443 is uitgegeven voor `*.segipsa.es` (een niet-verwant bedrijf op dezelfde gedeelde server). Er is dus geen eigen certificaat meer voor hernanihomes.com; https werkt niet.

Vroeger, volgens het internetarchief:
- 2019–2020: **Sooprema** — `<meta name="generator" content="Mattis-Framework 4.0">`, `<meta name="application-name" content="App-pagina-web-mattis">`, voettekst met link naar sooprema.com, css/js onder `/objetos/cache/hernani/…`, formulieren onder `/html/formulario/…`, aanbodpagina's `/apartments-in-javea/` en `/luxury-villas-for-sale-in-javea/page/0…3/` (bron: archiefcaptures 17-07-2019 t/m 07-08-2020).
- 2013–2016: Joomla met `com_properties` en JoomFish, object-URL's als `/es/propiedad/v-2xx.html` (bron: archiefindex, o.a. capture 15-09-2013).

Tijdlijn van het verdwijnen (bron: archiefindex https://web.archive.org/cdx/search/cdx?url=hernanihomes.com* en homepage-captures, geraadpleegd 24-09-2026):
- 10-04-2024: laatste captures van echte pagina's (formulieren `/html/formulario/llamanos/`, `/48horas/`).
- 30-08-2024, 10-02-2025, 17-06-2025: homepage toont alleen "System Updating".
- 27-02-2026 (`Last-Modified` van de huidige pagina): Plesk-standaardpagina.

Sooprema kent een exportfeed, maar dat helpt hier niet: er is geen draaiende Sooprema-site meer om uit te exporteren. Daarom niet "feed vragen" maar "overslaan".

## 6. Omvang en dekking Jávea/Benitachell/Moraira — ONBEKEND

Huidig aanbod: **niet vast te stellen** (geen site). Onbekend is ook of het kantoor nog actief is.

Wat het archief over de oude situatie zegt (alleen ter oriëntatie, geen huidige feiten):
- 07-08-2020: de appartementenpagina toonde 12 referenties (A-152 t/m A-201); het zoekformulier kende als plaatsen alleen **Dénia en Jávea** en als wijken uitsluitend Jávea-wijken (Arenal, Montgó, Tosalet, Rafalet, Puchol, …) plus **Benitachell**. Moraira kwam niet voor.
- 17-08-2019: de villapagina had vier deelpagina's (`page/0` t/m `page/3`).
- Voorzichtige indruk: een klein kantoor met vrijwel uitsluitend Jávea-aanbod (plus wat Benitachell), in de orde van enkele tientallen objecten. **[te verifiëren]** — en zes jaar oud.

## Advies en alternatief voor Jan

**Overslaan** als automatische bron. Niets verboden, maar ook niets aanwezig. Hernani Homes staat in `kader/makelaars.json` het best als "overslaan — site offline sinds 2024; opnieuw toetsen zodra er weer een site is".

⏸️ ACTIE VOOR JAN (menselijke route): het kantoor staat op javeaguide.com nog vermeld op Av. Fontana 2, Edif. Estrella del Sur, local 7B, Jávea (bron: K01-kantoren-javea.json, javeaguide.com 24-09-2026). Even langslopen of bellen is de enige manier om te weten of ze nog bestaan en waar hun aanbod nu staat (alleen portalen? nieuw domein?). Het algemene adres info@hernanihomes.com stond in 2020 op de site [te verifiëren of dat nog werkt, zie MX hierboven]. Komt er een nieuw domein boven water, dan deze toets daarop opnieuw draaien.

# Homes To Be Happy — toets op automatisch lezen

Datum: 24-09-2026 · Onderdeel van TREE Deal Hunter (makelaarssites Jávea)
Site: https://www.homestobehappy.com

## Kort oordeel

**Advies: feed vragen.** robots.txt staat een gewone lezer toe om de aanbod- en
objectpagina's te lezen, maar in de praktijk zet de site vóór élke pagina (ook de
sitemap) een JavaScript-botcontrole ("Powered by Paagees Shield") die een automatische
lezer tegenhoudt. Die controle omzeilen we niet. Daardoor konden de voorwaarden, de
sitemap, de aanbodpagina en een objectpagina niet gelezen worden. Het systeem achter de
site is de Paagees-weblaag, die per definitie gevoed wordt door een XML/API-feed uit het
CRM van het kantoor (zeer waarschijnlijk Sooprema, zie punt 5). Die feed bestaat dus al;
de vraag aan het kantoor is of hij ook naar ons mag.

Zelfde lijn als de eerdere verslagen over javeaimmo.com, javeacasas.com, terramar.es,
crown-property.com en paradiserealestate.es (alle 24-09-2026).

## Wat is er opgehaald (3 verzoeken, telkens ruim meer dan 2 seconden ertussen)

| # | URL | Tijd (UTC) | Resultaat |
|---|---|---|---|
| 1 | https://www.homestobehappy.com/robots.txt | 21:50:30 | HTTP 200, echte robots.txt (5.717 bytes, `server: Apache`, `last-modified` 07-01-2025) |
| 2 | https://www.homestobehappy.com/sitemap.xml | 21:50:53 | HTTP 200, maar géén XML: controlepagina "Security Check" (5.882 bytes, `server: nginx`, `x-robots-tag: noindex, nofollow`) |
| 3 | https://www.homestobehappy.com/ | 21:51:24 | HTTP 200, identieke controlepagina |

Gebruikte lezer: curl met eigen herkenbare user-agent `TREE-DealHunter-check/1.0`.
Na verzoek 3 gestopt: elke verdere pagina zou dezelfde controle geven en verder gaan
zou neerkomen op omzeilen. Een zoekmachine-opzoeking (bedrijfsprofiel, aanbodomvang,
voorwaarden via zoekfragment) was niet mogelijk: het zoekbudget van deze sessie was op.

## 1. robots.txt — DEELS toegestaan

Bron: https://www.homestobehappy.com/robots.txt (HTTP 200, 24-09-2026 21:50 UTC).
Het blok voor alle lezers, letterlijk:

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

- **Uitleg:** een `User-agent: *` mag de aanbod- en objectpagina's lezen (`Allow: /`).
  Níet toegestaan: vervolgpagina's van lijsten (`/*/*/*/page/*` en de vertalingen
  `pagina`, `pages`, `seite`, `stranitsa`, `siden`), printversies, formulieren
  (bel-mij-terug, 48 uur, tegenbod), de fotogalerij-modal, `/images/` en `/admin/`.
  Geen `Crawl-delay`.
- Daarnaast **132 regels `Disallow: /` voor met naam genoemde bots** (enkele dubbel),
  onder meer `Wget`, `Python-urllib`, `httplib`, `lwp-trivial`, `WebCopier`,
  `Offline Explorer`, `WebZip`, `EmailCollector`, `TurnitinBot`. Signaal: massaal
  kopiëren is ongewenst; een lezer die zich eerlijk onder eigen naam meldt valt onder
  de `*`-regels.
- **Geen `Sitemap:`-regel.**
- Het bestand is byte-voor-byte even groot (5.717 bytes) en heeft hetzelfde `*`-blok
  als de robots.txt van arluxuryliving.com, calablanca.com, javeacasas.com en
  villalux.com (verslagen 24-09-2026): het sjabloon van het Sooprema/"Mattis"-platform.
  De regel `/giuliano/proceso/enviar/` is een overblijfsel van dat sjabloon, niet iets
  van dit kantoor.

**Oordeel: deels.** Op papier mag lezen van objectpagina's; bladeren via paginering
mag niet, dus een lezer zou via de sitemap moeten werken — en die is niet bereikbaar
(punt 3).

## 2. Gebruiksvoorwaarden — NIET GEVONDEN (niet bereikbaar)

De homepage, en daarmee de voettekst met een eventuele link naar aviso legal /
condiciones / terms, was niet leesbaar (controlepagina, zie punt 4). Binnen de opdracht
("stop zodra iets niet mag") is niet naar `/aviso-legal/` of vergelijkbare adressen
geraden; die zouden dezelfde controlepagina geven. Ook een zoekmachine-opzoeking was
niet mogelijk (budget op).

Conclusie: **geen vindbaar verbod op automatisch lezen, maar ook geen toestemming.**
Let op: bij zusterkantoren op hetzelfde platform (javeaimmo.com, javeacasas.com,
terramar.es; verslagen 24-09-2026) verbiedt de aviso legal reproductie van de inhoud
voor commerciële doeleinden zonder toestemming. Of dat hier ook zo is, is
**[te verifiëren]** zodra iemand de pagina handmatig in een browser opent.

## 3. Sitemap — niet leesbaar

- robots.txt noemt geen sitemap.
- https://www.homestobehappy.com/sitemap.xml (24-09-2026 21:50:53 UTC): HTTP 200, maar
  in plaats van XML de HTML-controlepagina "Security Check" (zie punt 4).
- `/sitemap_index.xml` niet geprobeerd: zou dezelfde controle geven.
- Of er überhaupt een XML-sitemap is, en hoeveel object-URL's die telt: **onbekend**.

## 4. Aanbodpagina en objectpagina — niet geopend (botcontrole)

Op https://www.homestobehappy.com/ (21:51:24 UTC) én op /sitemap.xml (21:50:53 UTC)
kwam geen inhoud maar een HTML-pagina van 5.882 bytes: titel "Security Check", kop
"Verifying your browser", tekst "This is an automatic security check. You will be
redirected shortly.", voettekst "Powered by Paagees Shield". Koppen: `server: nginx`,
`x-robots-tag: noindex, nofollow`, `cache-control: no-store`.

Wat de pagina doet (uit het meegestuurde script, alleen gelezen): de browser moet een
SHA-256-rekenpuzzel oplossen (een hash met 5 leidende hex-nullen zoeken), zet dan een
cookie `__shield` (1 uur geldig, `Secure`, `SameSite=Lax`) en herlaadt de pagina.
Zonder JavaScript en cookies kom je er niet doorheen. **Niet opgelost, niet omzeild,
ook niet met een andere ophaaltool geprobeerd** — de bedoeling van die controle is
duidelijk: alleen echte browsers.

Opvallend: robots.txt komt rechtstreeks van de oorsprongsserver (`server: Apache`),
de HTML-pagina's lopen via een voorgeschakelde nginx met het schild. robots.txt is dus
bewust vrijgegeven voor bots; de rest niet.

Gevolg: **geen** aanbodpagina, **geen** objectpagina, en dus onbekend of er
`<script type="application/ld+json">` of `og:`-metatags op een objectpagina staan.
Prijs, oppervlakte, perceel, plaats, referentie: **niet gezien**.

## 5. Systeem achter de site — Paagees-weblaag, onderliggend zeer waarschijnlijk Sooprema

Aanwijzingen (alle 24-09-2026):

- **Paagees Shield** als botcontrole, `server: nginx` voor alle HTML. Paagees is volgens
  B01 §2.3 (`onderzoek/B01-crm-feeds.md`, bron paagees.com 16-09-2026) géén CRM maar
  een weblaag die "zich verbindt met het CRM dat je al gebruikt" (Inmovilla, Inmoweb,
  Sooprema, Mobilia, Inmogesco, Inmotek, Witei, Casafari, "cualquier CRM con XML o
  API"). Homes to be Happy staat daar al als Paagees-kantoor genoemd (R06 §3, B01 §2.3).
- **robots.txt is het Sooprema/"Mattis"-sjabloon**: identiek aan calablanca.com, waar
  Sooprema is bevestigd via `<meta name="generator" content="Mattis-Framework 4.0">` en
  een footer-link naar sooprema.com (verslag site-calablanca.com.md, punt 5), en aan
  javeacasas.com (Sooprema + Paagees Shield). De oorsprongsserver is hier eveneens
  Apache, net als bij Calablanca.
- HTML, css-paden, cookies en "powered by"-vermeldingen van de site zelf zijn **niet
  gezien** (controlepagina). De CRM-toewijzing is dus een sterk vermoeden op basis van
  het sjabloon, geen bevestiging: **Sooprema [te verifiëren]**.
- Geen aanwijzing voor Inmoweb, Mediaelx/LetsINMO, Inmovilla, Witei of WordPress.

Sooprema kent exportfeeds (XML/portaalkoppelingen, REST-API via het kantoor; B01 §5).
En omdat Paagees alleen kan draaien op een feed uit het CRM, bestaat die feed hoe dan
ook al.

## 6. Omvang en dekking Jávea / Benitachell / Moraira — ONBEKEND

- Geen aanbodpagina, sitemap of objectpagina gezien; geen zoekmachine beschikbaar.
- Uit het register: het kantoor is in K01 opgenomen als Jávea-kantoor (bron: Google
  "immobilier Javea" en "Immobilienmakler Javea", 24-09-2026), zonder aantal objecten.
- Aantal objecten: **niet te schatten**. Aandeel Jávea/Benitachell/Moraira: **onbekend**;
  gezien de vindplaats vermoedelijk Jávea-gericht, maar dat is geen meting.

## Advies en alternatief voor Jan

**Feed vragen.** Drie redenen om niet zelf te lezen:

1. De Paagees Shield houdt een automatische lezer tegen, ook al staat robots.txt het
   toe. Omzeilen is geen optie — het staat haaks op de bedoeling van die controle.
2. De voorwaarden zijn niet gelezen; bij zusterkantoren op hetzelfde platform verbiedt de
   aviso legal commerciële reproductie. Alleen intern signaleren, nooit teksten of foto's
   overnemen — en dat kan pas als er überhaupt iets te lezen valt.
3. Het systeem is een Paagees-weblaag op (zeer waarschijnlijk) Sooprema: de XML/API-feed
   bestaat al. De vraag aan het kantoor is niet "kunt u iets bouwen" maar "mag de feed
   die uw site al voedt ook naar ons" (B01 §2.3). Vraag alleen de **eigen** objecten
   (juridische lijn R04 §3.5), met prijs, m², perceel, plaats, referentie en link.

Prioriteit: **middel/laag** zolang de omvang van het eigen aanbod onbekend is. Eerst
één handmatige blik in een browser (aantal objecten, aandeel Jávea, aviso legal) en dan
pas beslissen of dit kantoor in de eerste ronde feedverzoeken hoort.

⏸️ ACTIE VOOR JAN
- Open https://www.homestobehappy.com één keer zelf in een browser: hoeveel objecten
  staan er te koop, hoeveel daarvan in Jávea/Benitachell/Moraira, en wat zegt de aviso
  legal? Noteer datum en aantallen; daarmee wordt dit verslag compleet.
- Als het de moeite waard is: het kantoor bellen of langsgaan met de feedvraag
  (conceptbericht in `onderzoek/B01-crm-feeds.md` §8; niets versturen zonder jouw ja).

## Openstaand / te verifiëren

- CRM achter de Paagees-weblaag (vermoedelijk Sooprema) — te bevestigen zodra HTML van
  een objectpagina gezien is (bijv. `meta generator Mattis-Framework`, footer-credit).
- Inhoud van de aviso legal / voorwaarden.
- Bestaan en omvang van een XML-sitemap.
- Aantal objecten en gebiedsdekking.

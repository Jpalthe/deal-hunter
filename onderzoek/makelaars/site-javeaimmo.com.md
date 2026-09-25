# Toets op automatisch lezen: javeaimmo.com

**Kantoor:** Javea Immo (handelsnaam; sinds 1997 volgens eerder register R06)
**Website:** https://www.javeaimmo.com
**Kantoor:** Avenida de Estrasburgo, Local 3, 03730 Jávea (Alicante) · algemeen e-mailadres info@javeaimmo.com
**Datum toets:** 24-09-2026 (avond)
**Advies: FEED VRAGEN**

In één zin: robots.txt staat lezen toe, maar (a) de site zet een JavaScript-botcontrole
("Paagees Shield") vóór elke pagina die een gewone automatische lezer tegenhoudt, en (b) de
aviso legal verbiedt reproductie van de inhoud voor commerciële doeleinden zonder toestemming.
Omzeilen doen we niet. De site draait op de Paagees-weblaag, die per definitie gevoed wordt
door een XML/API-feed uit het CRM van het kantoor — die feed bestaat dus al en is de nette weg.

Vijf verschillende pagina's opgehaald (robots.txt, sitemap.xml, één objectpagina, aviso legal,
aanbodpagina /venta/), nooit twee tegelijk, telkens meer dan 2 seconden uit elkaar. Geen inlog,
geen formulier, geen browser nagebootst, geen rekenpuzzel opgelost. Volledige verzoekenlijst
onderaan.

## 1. robots.txt — toegestaan, maar achter een botcontrole

Bron: https://www.javeaimmo.com/robots.txt (24-09-2026).

**Eerste twee pogingen (curl, eigen herkenbare user-agent):** HTTP 200, maar geen robots.txt.
In plaats daarvan een HTML-pagina van 5.882 bytes, titel "Security Check", tekst "Verifying your
browser … This is an automatic security check", voettekst "Powered by Paagees Shield". Headers:
`server: nginx`, `x-robots-tag: noindex, nofollow`, `cache-control: no-store`. De pagina laat de
browser een SHA-256-rekenpuzzel oplossen (5 leidende hex-nullen), zet dan een cookie `__shield`
(1 uur geldig) en herlaadt. Zonder JavaScript en cookies kom je er niet doorheen. **Niet
opgelost, niet omzeild.**

**Derde poging (standaard ophaaltool van dit platform):** kreeg het echte bestand. Letterlijke
inhoud:

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

Voor `User-agent: *` is alles toegestaan behalve beheer-, CRM-, API- en cachepaden. De
aanbodpagina's (`/venta/`, `/venta/<slug>-<ref>/`, `/comprar/`) vallen daar niet onder en mogen
volgens robots.txt gelezen worden. Er staat **geen `Sitemap:`-regel** in.

Let op de tegenstrijdigheid: robots.txt zegt "mag", de Shield zegt in de praktijk "alleen echte
browsers". Welke clients de Shield doorlaat is niet zichtbaar; dat hij een gewone HTTP-client
tegenhoudt, is een duidelijk signaal dat het kantoor (of Paagees) geautomatiseerd lezen niet wil.
Zie ook de eerdere waarneming in R06-verificatie R06-06 en B01 §2.3.

## 2. Voorwaarden — reproductie voor commerciële doeleinden verboden

Bron: https://www.javeaimmo.com/aviso-legal/ (24-09-2026; pad geraden naar de footerlink
"Aviso Legal", bleek te kloppen). Eén pagina van ca. 3.800 woorden met Aviso Legal, Condiciones
Generales de Uso, Política de Privacidad en Política de Cookies. Spaans recht, Spaanse rechter;
verwijst naar AVG/RGPD en LSSI-CE (Ley 34/2002).

Letterlijk, onder "Derechos de Propiedad Intelectual e Industrial":

> "En virtud de lo dispuesto en los artículos 8 y 32.1, párrafo segundo, de la Ley de Propiedad
> Intelectual, quedan expresamente prohibidas la reproducción, la distribución y la comunicación
> pública, incluida su modalidad de puesta a disposición, de la totalidad o parte de los
> contenidos de esta página web, con fines comerciales, en cualquier soporte y por cualquier
> medio técnico, sin la autorización de www.javeaimmo.com."

En onder "Compromisos y Obligaciones de los Usuarios":

> "Respecto de los contenidos de esta web, se prohíbe: Su reproducción, distribución o
> modificación, total o parcial, a menos que se cuente con la autorización de sus legítimos
> titulares; Cualquier vulneración de los derechos del prestador o de los legítimos titulares;
> Su utilización para fines comerciales o publicitarios."

Woorden als robot, bot, scraping, rastreo, automatizado, crawler of extracción komen **niet**
voor. Er staat dus geen letterlijk scrapingverbod, maar wél een algemeen verbod op het
reproduceren en commercieel gebruiken van de inhoud (tekst, foto's, "estructura, selección,
ordenación") zonder toestemming. Deal Hunter kopieert aanbodgegevens voor een commercieel doel;
dat valt onder deze clausule. Oordeel: **ja, verbiedt (indirect) wat wij zouden doen** — met
toestemming van het kantoor vervalt het bezwaar.

Vertrouwelijkheid: de aviso legal noemt de exploitant met een NIF van een natuurlijk persoon
(eenmanszaak). Bewust niet overgenomen; alleen bedrijfsnaam, kantooradres en het algemene
e-mailadres.

## 3. Sitemap — 409 URL's, waarvan 289 objectpagina's te koop

Bron: https://www.javeaimmo.com/sitemap.xml (24-09-2026; HTTP 200 via de standaard
ophaaltool; met curl zou ook hier de Shield komen). Gewone `<urlset>`, geen index.

Tellingen (gedaan door de AI-lezer van de ophaaltool, dus **bij benadering**; de ruwe XML was
niet lokaal op te slaan zonder de Shield te omzeilen):

| Wat | Aantal |
|---|---|
| Totaal `<loc>` | 409 |
| Pad begint met `/venta/` (koopobjecten) | **289** |
| `/alquiler/` en `/alquiler-vacacional/` (huur) | 13 |
| `/promos/` (nieuwbouwprojecten) | 1 |
| Overig: homepage, `/comprar/`, `/vender/`, `/servicios/`, `/contacto/`, rubriekpagina's zoals `/villas-en-venta-en-javea-alicante-costa-blanca/`, blog | ca. 106 |

Binnen de 289 `/venta/`-URL's, op slug: chalet/villa 157 · parcela/terreno/solar **49** ·
apartamento/ático/estudio 42 · finca 5 · local/traspaso/negocio 5.

`lastmod` loopt van 02-06-2020 tot 24-09-2026; 267 URL's hebben een datum in 2026, 26 in
september 2026. De sitemap bevat dus ook oude pagina's — de live teller op /venta/ (punt 6)
staat lager dan 289.

URL-patroon objecten: `/venta/<omschrijving>-<referentie>/`, bijv.
`/venta/villa-en-venta-en-cap-marti-javea-jiv1528/`,
`/venta/parcela-urbana-en-venta-en-javea-alicante-costa-blanca-jip1117/`,
`/venta/villa-para-reforma-integral-en-montgo-carrasquetes-javea-4522/`.

## 4. Aanbodpagina en objectpagina

- **Aanbodpagina:** https://www.javeaimmo.com/venta/ (ook `/comprar/`). Toont
  "Se han encontrado un total de **174 propiedades**", 24 per pagina, met paginering.
  Filters: type (Apartamento, Ático, Casa adosada, Casa de pueblo, Chalet/Villa, Dúplex, Finca,
  Garaje, Local comercial, Parcela, Parking) en plaats (Benigembla, Benissa, Benitachell, Calpe,
  Denia, Els Poblets, Gata de Gorgos, Jávea, La Sella, Moraira, Murla, Pedreguer, Teulada).
  Sortering op prijs aflopend; bovenaan o.a. Chalet/Villa Jávea € 4.500.000 (ref. AVS 52785),
  Parcela Jávea € 3.864.000 (ref. JIP1109D), Parcela Jávea € 2.869.000 (ref. 4795).
- **Bekeken objectpagina:** https://www.javeaimmo.com/venta/villa-en-venta-en-cap-marti-javea-jiv1528/
  (24-09-2026). Titel "VILLA EN VENTA EN CAP MARTÍ, JÁVEA | Ref: JIV1528". Zichtbaar:
  prijs **1.125.000 €**, referentie **JIV1528**, type Chalet/Villa, plaats **Jávea – Cap Martí**,
  **260 m² bebouwd**, **perceel 1.300 m²**, 3 slaapkamers, 2 badkamers, bouwjaar ca. 2016,
  energiecertificaat "en trámite", label "Novedad". Prijsregel letterlijk: "Ref. JIV1528 …
  1.125.000 €".
- **JSON-LD en og:-tags: onbekend.** De ophaaltool geeft alleen de leesbare tekst terug, niet
  de `<head>`; de ruwe HTML kon ik niet ophalen omdat curl de Shield krijgt. Geen bewijs voor of
  tegen `application/ld+json` of `og:`-metatags.

Referenties op de aanbodpagina hebben verschillende vormen: JIV/JIP/JIA-nummers (vermoedelijk
eigen aanbod, "JI" = Javea Immo), viercijferige nummers (4744, 4475, 4795), "AVS 52785",
"C-7318E", "JV965", "de-cv15", "ls-0479". Dat wijst op **deels gedeeld aanbod** van andere
kantoren of netwerken **[te verifiëren]** — bij een feed dus ontdubbelen op referentie en
coördinaten.

## 5. Systeem achter de site — Paagees-weblaag, onderliggend CRM onbekend

Aanwijzingen (24-09-2026):
- Voettekst op object- en aanbodpagina: "© 2026 Javea Immo - Todos los Derechos Reservados —
  **Paagees Webs para Inmobiliarias**" met link naar https://www.paagees.com/.
- Objectfoto's op `https://app-api.paagees.com/uploads/<uuid>/property/2026/05/20/…webp`.
- Logo op `/agencies/javeaimmo/assets/logo-alt.svg` — multi-kantoorplatform ("agencies").
- Botcontrole "Powered by Paagees Shield"; server nginx.
- robots.txt sluit `/crm/`, `/api/` en `/ajax/` uit: er zit een CRM-koppeling achter.
- Geen sporen van WordPress, Inmoweb, Mediaelx/LetsINMO, Inmovilla of Witei in de leesbare tekst;
  ruwe HTML/CSS-paden niet gezien (Shield).

Paagees is volgens eerder onderzoek (B01 §2.3, paagees.com, 16-09-2026) **geen CRM maar een
weblaag** die zich koppelt aan Inmovilla, Inmoweb, Sooprema, Mobilia, Inmogesco, Inmotek, Witei,
Casafari of "cualquier CRM con XML o API". Welk CRM Javea Immo gebruikt is hier niet vast te
stellen; zeker is dat de website al gevoed wordt door een XML- of API-feed.

## 6. Omvang en dekking Jávea / Benitachell / Moraira

- **Live aanbod te koop: 174 objecten** (teller op /venta/, 24-09-2026). Sitemap: 289
  koop-URL's, waarvan een deel verlopen (lastmod tot 2020 terug).
- Plaats in de 289 sitemap-slugs (AI-telling, bij benadering; ca. 97 slugs noemen geen
  plaats, maar een deel daarvan noemt wél Jávea-zones als Montgó, Tosalet, Arenal):
  Jávea ≥ 127 (44 %), Benitachell/Cumbre del Sol 12, Moraira/Teulada 18, Dénia 18,
  Pedreguer/La Sella/Jalón-vallei ca. 11, Gata 3, Calpe 1, Benissa 1.
- Aanbodpagina: 8 van de 10 duurste objecten liggen in Jávea.

**Schatting:** ruwweg **55–65 % Jávea**, plus ca. 4 % Benitachell en ca. 6 % Moraira/Teulada —
samen zo'n **twee derde in ons doelgebied**; de rest Dénia, La Sella/Pedreguer en de
Jalón-vallei. Opvallend voor Deal Hunter: **49 percelen** in de sitemap (ruim een op zes
objecten), meerdere expliciet in Jávea (Montgó, nabij casco antiguo "con anteproyecto"), en
minstens één object met "villa para reforma integral" in de slug.

## Advies en werkwijze

**Feed vragen.** Drie redenen om niet zelf te lezen:
1. De Paagees Shield houdt een gewone automatische lezer tegen — ook al laat robots.txt alles
   toe. Dat een enkele ophaaltool er vandaag doorheen kwam, is geen toestemming en geen
   garantie; het staat haaks op de bedoeling van die controle.
2. De aviso legal verbiedt reproductie van de inhoud voor commerciële doeleinden zonder
   toestemming van het kantoor.
3. Het systeem is een Paagees-weblaag: de XML/API-feed uit het CRM bestaat al. De vraag aan het
   kantoor is niet "kunt u iets bouwen" maar "mag de feed die uw site al voedt ook naar ons"
   (zie B01 §2.3). Met die feed vervalt het hele scrapingvraagstuk, inclusief de Shield en het
   auteursrecht op tekst en foto's.

Aandachtspunten bij een feed: ontdubbelen op referentie (JI-eigen vs. AVS/C-/JV-/viercijferige
referenties), verhuur (`/alquiler/`) en bedrijfsruimte (traspaso, local) uitsluiten, en
perceelobjecten (49) apart markeren voor module B (kadaster/planologie).

⏸️ ACTIE VOOR JAN: Javea Immo benaderen (kantoor Avenida de Estrasburgo, Local 3, Jávea;
algemeen e-mailadres info@javeaimmo.com) met de vraag om een kopie van de aanbodfeed
(XML/API uit hun CRM via Paagees) voor eigen gebruik door TREE, met de afspraak: alleen lezen,
niet herpubliceren. Pas na Jans "ja" wordt er iets verstuurd (regel 2). Tot die tijd: alleen
handmatig kijken in een browser.

## Verzoekenlogboek (24-09-2026, chronologisch, telkens > 2 s tussen live verzoeken)

| # | URL | Client | Resultaat |
|---|---|---|---|
| 1 | /robots.txt | curl, eigen user-agent | 200, Paagees Shield-controlepagina (5.882 bytes) |
| 2 | /robots.txt (headers vastleggen) | curl | 200, identieke controlepagina |
| 3 | /robots.txt | standaard ophaaltool | 200, echte robots.txt |
| 4 | /sitemap.xml | standaard ophaaltool | 200, urlset met 409 URL's (2× nagelezen uit cache, geen nieuw verzoek) |
| 5 | /venta/villa-en-venta-en-cap-marti-javea-jiv1528/ | standaard ophaaltool | 200, objectpagina (1× nagelezen uit cache) |
| 6 | /aviso-legal/ | standaard ophaaltool | 200, aviso legal + privacy + cookies (1× nagelezen uit cache) |
| 7 | /venta/ | standaard ophaaltool | 200, aanbodpagina, "174 propiedades" |

Vijf verschillende pagina's; zeven live verzoeken (drie op robots.txt). Niet gedaan:
homepage, `/comprar/`, `/promos/`, `/sitemap_index.xml`, ruwe HTML van een objectpagina
(Shield), zoekmachinecontrole (zoekbudget van deze sessie was op — punten met
**[te verifiëren]** blijven open).

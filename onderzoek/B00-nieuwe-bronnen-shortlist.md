# B00 — Nieuwe bronnen: controle en shortlist

**Rol:** controleur en samensteller over de zes zoekrapporten B01–B06.
**Zoekagents werkten op:** 16-09-2026. **Mijn eigen controles:** 17-09-2026 (de server
draaide dit gesprek een dag later; elke "verified: true" hieronder is door mij op
17-09-2026 zelf opgehaald, niet overgenomen van de zoekagent).
**Register waartegen is ontdubbeld:** `/Users/root-admin/tree-es/deal-hunter/bronnenregister.json`, 75 regels (R2-01 t/m R2-75).

---

## 1. Wat dit oplevert in het kort

De zes agents leverden 54 kandidaten. Daarvan waren er 16 een **bekende partij** uit het
register — bij twaalf daarvan vonden ze wel een route die wij nog niet hadden (een XML-export,
een API, een aparte module). 38 waren echt nieuw. Na controle houden we **16 kandidaten** over
die de moeite waard zijn; **22 vallen af** omdat ze geen dekking hebben in Jávea, Benitachell
of Moraira, geen leesroute kennen, of voorwaarden hebben die opslag en analyse verbieden.

De twee beste vondsten zijn gratis en openbaar en kosten Jan niets: de **publicatieborden van
Benitatxell en Teulada-Moraira**. Het register kende alleen dat van Xàbia. Twee van onze drie
gemeenten stonden er dus domweg niet in. Beide borden zijn server-gerenderd en vandaag door mij
opgehaald.

Daarna komen twee betaalde maar concrete routes: de **gratis exportfeed van Inmoweb** via een
Jávea-kantoor (drie kantoren gebruiken dat CRM) en de nieuwbouwdatabank **Metainmo**, waar ik
zelf 19 promoties in Benitachell en 7 in Moraira heb geteld.

---

## 2. Shortlist — op volgorde van opbrengst per eenheid moeite

| # | Bron | Toegang | Unieke objecten hier | Kosten | Rechten | Wie | Volgende stap | Zelf gezien |
|---|---|---|---|---|---|---|---|---|
| 1 | **Tablón Benitatxell** `benitatxell.sedelectronica.es/board` | portaal handmatig (server-HTML) | ja | gratis | overheidspublicatie: opslaan, historie, AI en tonen mag; geen particuliere namen overnemen | systeem | Naast het Xàbia-bord in de monitor zetten; filteren op caducidad de licencia, órdenes de ejecución, ruina, PAI-inzage | **ja** |
| 2 | **Tablón Teulada-Moraira** `teuladamoraira.sedelectronica.es/board` | portaal handmatig (server-HTML) | ja | gratis | idem | systeem | Zelfde monitor en filters. Let op: `teulada.sedelectronica.es` is het verkeerde adres | **ja** |
| 3 | **Inmoweb — exportfeed per colaborador** | XML-feed | ja (eigen objecten van het kantoor) | feed **gratis** binnen het abonnement | feed is bedoeld voor "cualquier portal o colaborador", sleutel per ontvanger, intrekbaar; bevat alleen wat het kantoor zelf publiceert | Jan | RANDOF, Javea Continental en Xabiacasa bellen en om een exportsleutel vragen; daarna schriftelijke afspraak (sjabloon R16 §6.3) | **ja** |
| 4 | **Metainmo** (Propiedad Inmobiliaria Online S.L., Alicante) | XML-feed (abonnement "Básico + XML") | deels — nieuwbouw | 125 € eenmalig + abonnement (bedrag niet publiek) | voorwaarden verbieden reproductie "sin autorización previa, expresa y por escrito"; XML is wél bedoeld "para integrarse con su sitio web o CRM"; historie en AI ongeregeld | Jan | Offerte vragen én schriftelijk laten bevestigen: opslaan, prijshistorie bewaren, intern met AI analyseren | **ja** (19 Benitachell, 7 Moraira) |
| 5 | **Aliseda — sitemap-investors.xml** (nieuwe route bij R2-33) | XML-feed (sitemap) | deels — grond | gratis | robots.txt nodigt uit tot ophalen, maar de site is een JS-schil, ook het aviso legal: gebruiksrechten ONBEKEND | Jan + systeem | Jan: de Jávea- en Teulada-grondpagina's in een browser openen en doorgeven wat erin staat. Systeem: wekelijks één verzoek als signalering | **ja** (3.639 URL's, 114 Alicante, Jávea en Teulada bevestigd) |
| 6 | **Mediaelx / LetsINMO — CRM-export** (nieuwe route bij R2-26) | XML-feed | ja | onbekend | "you can create as many XML Feed as you want … send it to your collaborators"; wij moeten expliciet om *alleen eigen* objecten vragen, niet om "Imported/All properties" | Jan | Casas Ambiente (Moraira) benaderen; laten kiezen voor "Genuine properties" | nee (zoekagent) |
| 7 | **BORME — sumario-API** (nieuwe route naast R2-36) | API | deels — vroegsignaal | gratis | zelfde hergebruikregeling als BOE: mag, met bronvermelding; PDF's bevatten bestuurdersnamen — alleen rechtspersoon, handeling en datum bewaren | systeem | Dagelijkse lezer die het Alicante-item ophaalt en ontleedt op disolución, liquidación, concurso | **ja** (item BORME-A-2026-178-03 "ALICANTE/ALACANT") |
| 8 | **AEDAS Homes — Portal de Colaboradores** | API (achter overeenkomst) | nee (eigen aanbod, wel exclusief) | onbekend | geen openbare voorwaarden; alles onbekend tot er een overeenkomst ligt | Jan | Voorwaarden van het collaborator-programma opvragen: provisie, en of het portaal beschikbaarheid en prijzen als feed geeft die wij mogen bewaren | **ja** (Unic Jávea "En comercialización", vanaf 370.000 €; API-endpoint antwoordt) |
| 9 | **VAPF — extranet voor makelaars** (nieuwe route bij R2-56/K-2) | lidmaatschap | deels — Cumbre del Sol, incl. losse percelen | onbekend | achter login, geen openbare voorwaarden | Jan | Toegang aanvragen als samenwerkende makelaar; tegelijk vragen of prijslijst en beschikbaarheid in XML of Excel komen en of wij die mogen bewaren | nee (zoekagent) |
| 10 | **Rightmove Overseas — als kantorenradar** | portaal handmatig | nee als feed; ja als vindplaats van kantoren | gratis lezen | geen leeslicentie, geen API; alleen handmatig | systeem | Wekelijkse handmatige ronde Jávea/Moraira/Benitachell; elk kantoor dat hier wél en in onze feeds níet voorkomt, op de partnerlijst | **ja** (489 objecten Jávea) |
| 11 | **MLS Costa — betaald lidmaatschap met XML feed out** (nieuwe route bij R2-26) | XML-feed (betaald) | deels | gratis account bevestigd; betaald tarief niet publiek | beslissend: de feed is "for your own website/property portals" — dat is een gebruiksbeperking; interne analyse vooraf schriftelijk regelen | Jan | Offerte opvragen; vragen naar aantal objecten in Xàbia, Benitachell en Teulada én naar de gebruiksvoorwaarden | **ja** (tekst letterlijk; ~3.000 objecten, gratis tier kan de database níet doorzoeken) |
| 12 | **Asociación Inmocalpe ("MLS Calpe")** | lidmaatschap | deels — leden ook in Moraira, Benitachell, Jávea | contributie niet publiek | geen gepubliceerde voorwaarden; ledenreglement onbekend | Jan | Eén zakelijke mail naar info@inmocalpe.es: toelatingseisen, contributie, bestaat er een XML/API voor leden, en wat zegt het reglement over bewaren en met AI analyseren | nee — site blokkeert (zie correctie C-1) |
| 13 | **Sooprema — REST-API** (nieuwe route bij R2-50) | API | ja (eigen objecten van het kantoor) | Starter vanaf 39 €/mnd, Enterprise vanaf 99 €/mnd | "Para realizar llamadas a la API se deberá proporcionar una clave"; voor echte data "la agencia deberá ser cliente activo de Sooprema" — route loopt via kantoor én leverancier | Jan | estate@sooprema.com vragen of een klant een derde leestoegang tot zijn eigen objecten mag geven | **ja** (tekst letterlijk) |
| 14 | **Partnerlijst promotoren en kantoren** (aanvulling op R2-52 en K-2): GestaliHome, Hispania Homes/Keller Williams Moraira, Villas Buigues, JOG Promociones, Grupo Moraira, Max Villas, Costa Privee | onbekend / rechtstreeks | deels | n.v.t. | geen feeds; elk stuk materiaal alleen na expliciete toestemming per partij | Jan | Opnemen in de partnerlijst R2-52; pas benaderen na akkoord. Geen van deze partijen levert een feed — de waarde zit in de afspraak, niet in data | nee |
| 15 | **RedSP — nieuwbouwdatabase Costa Blanca** | XML-feed | deels | 29 €/mnd bij jaarbetaling, na setupkosten | voorwaarden niet ingezien; volgens de zoekagent worden adressen verwijderd — dat heb ik níet kunnen terugvinden (correctie C-4) | Jan | Proefaccount vragen; tellen hoeveel promociones in Xàbia, Benitachell en Teulada zitten en of adressen echt ontbreken | **ja** (1.940 listings, 730 developments, 29 €/mnd — Jávea nergens genoemd) |
| 16 | **Babysteps MLS** | lidmaatschap | onbekend | aanbieden en bladeren gratis; samenwerken 39 €/mnd | "any standard XML or JSON feed"; wie deelt bepaalt de plaatsende agent; verbod op oogsten van contactgegevens | systeem | Gratis registreren en tellen hoeveel objecten in Xàbia, Benitachell en Teulada staan vóór er iets wordt betaald | **ja** (bestaat, 39 €/mnd, gratis tier) |

**Op de lange baan, wel noteren:** Brainsre-module *licencias de obra nueva* (nieuwe route bij
R2-19 — proefaccount vragen, toetsen of vergunningen 2021–2023 zonder oplevering zichtbaar zijn);
Resales-Online *New Development MLS* (nieuwe route bij R2-24 — meenemen in het lopende
lidmaatschapsspoor R04 §3.2); Diario de Subastas (gratis e-mailmelding op provincie Alicante,
géén koppeling — zie afwijzing A-13 voor waarom dit lager staat dan de zoekagent voorstelde);
subastasprocuradores-sitemap (nieuwe route bij R2-40, pas ná de BORME-lezer);
MIVAU-visados-reeks (nieuwe route bij R2-46, contextcijfer).

---

## 3. Afgewezen, met reden

| Partij | Reden |
|---|---|
| A-1 Paagees | Weblaag bóven bestaande CRM's: publiceren, geen leesroute. Wel bruikbaar als argument richting een kantoor ("de feed bestaat al"). |
| A-2 Property Portal Marketing | Bouwt feeds voor makelaars, levert zelf geen data. Achter de hand als een gewenst kantoor technisch niet kan leveren. |
| A-3 InmoMatch | Zet een eigen landingspagina om een geplakte idealista-link: hergebruik van advertenties van derden, rechtenrisico. |
| A-4 Viveku / FAI | Aviso legal verbiedt reproductie en distributie zonder voorafgaande schriftelijke toestemming, en er staat één object in Jávea en nul in Teulada en Benitachell. |
| A-5 Comprarcasa | Angular-schil: homepage en sitemap leveren niets; geen enkel aangesloten kantoor in de Marina Alta aangetoond. |
| A-6 Addmeet | Nul objecten in onze drie gemeenten, één in de hele provincie; primair een publicatieplatform. |
| A-7 Escrapalia Inmuebles | robots.txt sluit de hele vastgoedcategorie en alle filters uitdrukkelijk uit; nul kavels in Alicante. |
| A-8 subastapublica.info | Sitemap telt drie URL's en bevat geen vastgoedindex. |
| A-9 TED (EU-aanbestedingen) | Levert geen enkel object, alleen context over wie welk Sareb-mandaat beheert. |
| A-10 Culmia | Enige project in de regio ligt in Dénia, buiten onze drie gemeenten. |
| A-11 viviendasnuevas.com | Geen XML, API of dataproduct; dubbelt met wat de promotorsites zelf tonen. |
| A-12 Taylor Wimpey España | Geen makelaarspagina, geen feed, eigen verkoopkanaal. Aqua Moraira blijft nuttig als prijsbenchmark. |
| A-13 Zoopla Overseas / PrimeLocation | Geen officiële API of feedspecificatie; wat zich "Zoopla API" noemt is een commerciële scraper. Aanbod dubbelt via syndicatie. |
| A-14 Immowelt / Immonet | Geen leesroute. De bruikbare kern is niet het portaal maar het inzicht dat Duitse portalen op OpenImmo draaien — dat nemen we mee als geaccepteerd feedformaat voor Duitstalige partners. |
| A-15 huisenaanbod.nl | Alleen invoerkoppelingen, geen export naar derden. De openbare lijst met 30+ ondersteunde systemen is wel bruikbaar als overzicht van feedfamilies. |
| A-16 Optima-CRM | Ruime exportvrijheid ("export to wherever you want"), maar geen enkel partnerkantoor in ons gebied aangetoond. Pas oppakken als dat verandert. |
| A-17 Inmogesco | Geen kantoor in Jávea, Benitachell of Moraira aangetoond. |
| A-18 FreeMLS.es | Of een lid een uitgaande feed met andermans objecten krijgt staat nergens; geen dekkingscijfer. |
| A-19 MLS España / Anaconda Solutions | Geen API of XML op de gelezen pagina's; statistiek dateert uit 2019; deelregels niet in te zien. |
| A-20 MLS.es / "MLS Nacional" | 66–120 €/maand zonder één aangetoond lid in de Marina Alta. |
| A-21 Inmoweb MLS (het netwerk) | Objecten van andere kantoren zijn alleen te tónen binnen hun eigen websiteproduct; geen API of XML, geen exportrecht. De Inmoweb-exportfeed (shortlist 3) blijft wél staan. |
| A-22 EstateNearMe / Inmofind | Geen aparte bron: zelfde platform als Metainmo (zie correctie C-3). Bovendien vandaag Cloudflare 403. |
| A-23 Casafari Connect | Samenwerkings- en commissielaag, geen datafeed; data valt onder het al bekende Casafari-contract (R2-18) dat systematische extractie verbiedt. |
| A-24 Witei-feed | Het servicecontract verbiedt gebruik van Witei om samenwerking tussen zelfstandige makelaars te faciliteren, op straffe van onmiddellijke beëindiging. Witei-kantoren niet om een feed vragen. |
| A-25 Resales-Online static XML | "This feed can only be used for your own website. It cannot be used with portals or other third-party sites." Sluit de openstaande vraag in R2-24: niet gebruiken. |
| A-26 Agora MLS + Club Notegés-alliantie | Achtergrondartikel uit 2020; het register stelt al vast dat Agora MLS geen kantoren in Jávea, Dénia of Moraira heeft. |

---

## 4. Dubbelingen — partijen die al in het register staan

Twaalf hiervan leveren wél een route die wij nog niet hadden. Die staan hieronder met **NIEUWE ROUTE**.

| Kandidaat | Registerregel | Oordeel |
|---|---|---|
| MLS Costa | R2-26 | **NIEUWE ROUTE** — betaalde "XML Feed out" met de gedeelde voorraad; gratis tier kan de database niet eens doorzoeken |
| MLS Mediaelx (netwerk) | R2-26 | bekend; maar de **CRM-export van LetsINMO** naar een collaborator is een **NIEUWE ROUTE** |
| Resales-Online | R2-24 | **NIEUWE ROUTE** ×2 — static XML feed (afgewezen, zie A-25) en New Development MLS (Alicante/Murcia, noemt Jávea) |
| Apibolsa / INMOPC | R2-27 | **NIEUWE ROUTE** — aansluiten met elk CRM dat Kyero 3.0 kan, plus downloadbare back-ups van gedeelde objecten. Let op correctie C-5 |
| Inmovilla | R2-29 | **NIEUWE ROUTE** — openbare REST-API-documentatie (token via Inmovilla) en de bolsa met wederkerige kringen |
| Witei | R2-29 | bekend; rechten nu wél vastgesteld — en ze blokkeren ons (A-24) |
| idealista/tools "grupos de oficinas" | R2-06 | **NIEUWE ROUTE** — MLS-laag binnen een portaal dat we al gebruiken. Zie correctie C-2 |
| Casafari Connect | R2-18 | bekend; geen aparte bron (A-23) |
| Brainsre — licencias de obra nueva | R2-19 | **NIEUWE ROUTE** — vergunningendatabank per gemeente, gekoppeld aan promotor |
| Aliseda — sitemaps | R2-33 | **NIEUWE ROUTE** — sitemap-investors.xml met gemeentenamen (shortlist 5) |
| BORME | naast R2-36 | **NIEUWE ROUTE** — eigen sumario-API naast die van de BOE (shortlist 7) |
| subastasprocuradores — sitemap | R2-40 | **NIEUWE ROUTE** — robots staat het toe en de sitemap wordt zelf aangeboden |
| MIVAU — visados en certificaciones fin de obra | R2-46 | **NIEUWE ROUTE** — maandreeks naast de al bekende transactiestatistiek |
| VAPF | R2-56 / R07 tabel K-2 | **NIEUWE ROUTE** — het makelaarsextranet (shortlist 9) |
| Sooprema | genoemd in R2-50 | **NIEUWE ROUTE** — REST-API (shortlist 13) |
| Paagees | genoemd in R2-50 ("Paagees Shield") | bekend als botcontrole; als platform afgewezen (A-1) |
| Agora MLS | R2-28 | bekend, geen dekking |

---

## 5. Correcties op de zoekagents

**C-1 — Inmocalpe is niet zelf gezien.** De zoekagent citeert de about-us-pagina van
inmocalpe.es (17 kantoren, "shared properties"). Op 17-09-2026 geeft die URL mij HTTP 200 met
`<title>Security Check</title>`: een JavaScript-botcontrole, geen inhoud. De agent noteerde die
blokkade zelf ook, maar presenteerde de inhoud toch als bewijstype 1. Het aantal kantoren (17
versus circa 20) blijft onbevestigd. De partij bestaat wel; alleen de mail is nu de route.

**C-2 — de idealista-MLS-tekst komt uit een zoekfragment.** De helppagina
`idealista.com/tools/centrodeayuda/articulos/que-es-la-mls-inmobiliaria/` gaf mij opnieuw HTTP
403. Alles over commissie 50/50, gedragscode en reglement staat dus op één zoekfragment. Of er
een *grupo de oficinas* voor de Marina Alta bestaat, is niet vastgesteld. Meenemen als vraag in
het lopende Search-API-traject, niet als feit opschrijven.

**C-3 — EstateNearMe en Metainmo zijn hetzelfde platform.** B03 voert ze op als twee
kandidaten. De homepage van `spain.metainmo.com` linkt naar `/alicante/companies/promotoras` —
exact de URL die B03 aan EstateNearMe toeschrijft, met dezelfde paginastructuur. Vandaag geeft
estatenearme Cloudflare 403 en metainmo HTTP 200. Eén regel in het register, niet twee. Het
aantal promotoras in de provincie stond bij mij op **264**, niet op de 236 die B03 noteerde.

**C-4 — RedSP: twee claims niet teruggevonden.** Bevestigd op de eigen site: 1.940 listings,
+730 developments, +330 developers, +545 agencies, synchronisatie "via XML feed or directly in
Inmovilla", en het tarief 40 € → 29 €/maand bij jaarbetaling. **Niet** teruggevonden op de
gelezen pagina's: de feedversies "Kyero V3, redsp v3 or redsp v4" en de bewering dat RedSP
adressen en developerlogo's verwijdert. Dat laatste is nu juist het punt dat bepaalt of de feed
bruikbaar is voor perceelidentificatie — expliciet navragen, niet aannemen.

**C-5 — INMOPC-pagina bestaat niet meer op die URL.** `inmopc.com/software-para-inmobiliaria-bolsa-mls.html`
gaf mij HTTP 404 met de titel "Neodigit". De twee geciteerde zinnen over Kyero 3.0 en het
downloaden van back-ups van gedeelde objecten kon ik dus niet reproduceren. De route via het
Colegio API Alicante blijft de moeite waard, maar de technische claim is nu bewijstype 7.

**C-6 — Metainmo: Jávea niet gereproduceerd.** Benitachell **19** en Moraira **7** promoties kon
ik bevestigen, Teulada 0. De 9 promoties voor Jávea/Xàbia niet: vier slugs (`javea`, `xabia`,
`javea-xabia`, `xàbia`) gaven alle `total: 0`. De dekking in Benitachell en Moraira is op
zichzelf al genoeg om de offerte aan te vragen, maar reken niet op Jávea.

**C-7 — Inmoweb: de feed is gratis, niet "inbegrepen in het pakket".** De helppagina zegt
letterlijk: "Inmoweb te ofrece, **gratuitamente**, la posibilidad de crear y distribuir con tus
colaboradores accesos a un feed de exportación". Verder bevestigd: sleutel per ontvanger,
"Podrás revocar el acceso en cualquier momento", alleen "todos los inmuebles publicados en tu
página web", beschikbaar van 18:00 tot 09:00, en een "XML personalizado" als het kantoor een
selectie wil sturen. Dat laatste is nieuw en nuttig: een kantoor kan ons dus een deelverzameling
geven.

**C-8 — Aliseda: 114 Alicante-URL's, niet 99.** De sitemap telt 3.639 URL's, waarvan 114 onder
`/alicante` (de agent telde vermoedelijk maar één taalversie). Bevestigd: eigen landpagina's voor
`javeaxabia` (finca rústica, suelo urbano, todos) en `teulada` (suelo urbanizable, todos) in drie
talen. Benitachell komt inderdaad niet voor.

**C-9 — Diario de Subastas is lager gewaardeerd dan de agent voorstelde.** De agent gaf "hoog",
maar noteerde zelf vier kavels in onze drie gemeenten en dat het alle vier trasteros in Teulada
zijn, met nul in Jávea, Benitachell en Moraira. De onderliggende feiten lezen wij al rechtstreeks
als BOE-open-data. Een gratis e-mailmelding is prima; een koppeling bouwen niet.

**C-10 — MLS Costa: het gratis account kan niets opzoeken.** De agent stelde voor gratis te
registreren en te tellen. Dat kan niet: doorzoeken van de database staat uitdrukkelijk onder
"PAID Membership". Het gratis account laat alleen úpload toe. Het aantal objecten in ons gebied
moet dus in de offerteaanvraag worden gevraagd.

**C-11 — Tellingen die ik bevestigde.** Rightmove Overseas Jávea: **489** (klopt exact met B05).
BORME-sumario van 15-09-2026: item **BORME-A-2026-178-03**, titel "ALICANTE/ALACANT" (klopt exact
met B04). AEDAS Unic Jávea: "En comercialización", "Obra iniciada", vanaf 370.000 €, 64,23 m²,
2-3 slaapkamers (klopt exact met B03), en `colaboradores-api.aedashomes.com` antwoordt met
"Bienvenido al API del Portal de Colaboradores de AEDAS". Sooprema en MLS Costa citeerden de
agents woordelijk correct.

---

## 6. Wat Jan zelf moet doen

⏸️ **ACTIE VOOR JAN** — vijf dingen, in deze volgorde:

1. **Bellen: drie Jávea-kantoren op Inmoweb** (RANDOF, Javea Continental, Xabiacasa) en één
   Moraira-kantoor op Mediaelx (Casas Ambiente). Vraag om een exportsleutel voor hun eigen
   objecten. De feed kost hén niets. Dit is de goedkoopste echte uitbreiding van onze voorraad.
2. **Eén mail naar info@inmocalpe.es** met vier vragen: toelating, contributie, bestaat er een
   XML- of API-koppeling voor leden, en wat zegt het reglement over bewaren en met AI analyseren.
3. **Offerte Metainmo** ("Básico + XML", 125 € registratie plus abonnement) — maar alleen
   aansluiten als zij schriftelijk bevestigen dat wij mogen opslaan, prijshistorie bewaren en
   intern met AI analyseren. Dit kost geld: jouw akkoord nodig.
4. **Vijf Aliseda-links in een browser openen** (drie Jávea/Xàbia, twee Teulada) en doorgeven wat
   erin staat. Hun site werkt niet zonder JavaScript, dus wij kunnen er niet bij.
5. **Toegang vragen tot het VAPF-extranet** en tot het AEDAS-collaboratorprogramma, in beide
   gevallen met de vraag of prijslijst en beschikbaarheid als bestand komen en of wij die mogen
   bewaren.

Alles wat "systeem" is in de tabel kunnen wij zonder jou bouwen: de twee gemeentelijke
publicatieborden, de BORME-lezer en de wekelijkse Rightmove-ronde.

# R04 — Commerciële dataleveranciers, aggregators, MLS-netwerken en officiële statistiek

> **NA TEGENSPRAAK (15-09-2026).** Dit rapport is door een tweede agent gecontroleerd; zie `R04-dataleveranciers-mls-statistiek.verificatie.md`. Betrouwbaarheid volgens die controle: middel.
> Weerlegd en in de eindstukken gecorrigeerd: R04-10. Gebruik voor die punten de gecorrigeerde tekst in het verificatiebestand, niet de tekst hieronder.


**Project:** TREE Deal Hunter, fase A (bronnenkaart)
**Stroom:** R04
**Controledatum:** 14-09-2026 (alle webcontroles en lokale tests op deze dag)
**Bewijstypes:** 1 door aanbieder vermeld · 2 in officiële bron aangetroffen · 3 door ons rechtstreeks vastgesteld · 4 AI-inferentie · 5 berekening op benoemde aannames · 6 door bevoegde professional bevestigd · 7 onbekend of tegenstrijdig
**Statussen (masterprompt §7):** GEVERIFIEERD EN ACTIEF · TOEGANG AANGEVRAAGD · CONTRACT OF TOESTEMMING NODIG · TECHNISCH ONDERZOEK NODIG · ALLEEN HANDMATIG · NIET GEBRUIKEN

## Samenvatting (10 regels)

1. Geen enkele commerciële aggregator (Casafari, Brainsre, uDA/Accumin, Tinsa, Gloval, Grupo ST) publiceert prijzen voor datalevering of API-toegang; overal geldt offerte en contract. Casafari is de enige die aantoonbaar marktbreed *aanbod* (advertenties uit 30.000+ portalen en makelaarssites, ontdubbeld) via een REST-API levert — en dus mogelijk unieke objecten. De rest levert context (comparables, AVM, indicatoren).
2. Casafari's gebruiksvoorwaarden verbieden systematische verzameling, afgeleide werken en gebruik buiten de licentie; wat wij willen (dagelijks volgen, AI-analyse, opslag) moet contractueel expliciet worden geregeld.
3. uDA is niet meer van Alantra: op 14-05-2024 overgenomen door Tinsa Group, op 22-05-2025 opgegaan in **Accumin Intelligence** (samen met Tinsa Digital AVM, Deyde en Datacentric). Tinsa en uDA zijn nu één leverancier.
4. Tinsa Radar is de enige aggregator met openbare prijzen: €29 per studie, €99/maand (15 studies) of €259/maand (45 studies), 7 dagen proef, PDF-uitvoer — geen API. Tinsa's gratis IMIE-cijfers stoppen op provincieniveau; Jávea heeft geen eigen pagina.
5. MLS-netwerken die Jávea werkelijk dekken: **MLS 03724 Teulada-Moraira** (vereniging, deelt exclusieven én verkoopdata onder leden; Benissa t/m Dénia), **Resales-Online** (Costa Blanca-netwerk, WebAPI V6), **MLS Costa** (gratis basis, betaald XML-feed), **MLS Mediaelx** (3.000+ objecten Costa Blanca/Cálida), **APIred** (Colegio API Alicante, alleen colegiados) en **MLS Denia Realtor**. Inmobalia en Agora MLS dekken Jávea niet.
6. Resales-Online verbiedt in zijn voorwaarden uitdrukkelijk het doorgeven van andermans netwerkobjecten aan derden en beperkt gebruik tot de eigen website van het lid; een deal-hunter-database met netwerkobjecten valt daar niet vanzelf onder.
7. Wat een makelaar ons rechtmatig kán geven: zijn **eigen** objecten via een CRM-export (Inmovilla: API of dagelijkse XML; Witei: XML-link en webhooks, geen API; Mobilia: publieke API met Swagger). Kyero v3 is de feitelijke standaard. Netwerkobjecten van anderen mag hij niet doorgeven. "Propertyflows" bestaat niet als Spaans makelaars-CRM.
8. Officiële transactiedata op gemeenteniveau bestaat en is gratis: **MIVAU "Transacciones inmobiliarias"** (kwartaal, alle gemeenten, notariële bron ANCERT) — wij hebben Jávea/Xàbia, Dénia, Teulada, Benitachell, Benissa en Calp in de gemeentelijke XLS-bestanden aangetroffen. **MIVAU "Valor tasado"** per gemeente >25.000 inwoners bevat Jávea/Xábia (en ook Calp en Dénia). Beide onder CC BY 4.0 via datos.gob.es.
9. Het nieuwe **Portal Estadístico del Notariado** (penotariado.com, sinds 23-10-2025) geeft maandelijks werkelijke koopsommen per gemeente en postcode — maar de voorwaarden verbieden commercieel gebruik en opname in databanken, ook met bronvermelding. Alleen handmatig als context. INE (IPV: alleen autonome regio; ETDP: provincie, maandelijks) en Registradores (nationaal/regio/provincie/hoofdsteden; open-dataportaal blokkeert ons) leveren geen gemeentecijfers.
10. Catastro's *valor de referencia* is per object opvraagbaar in de Sede, maar alleen na authenticatie (certificaat/Cl@ve); een openbare webservice ervoor is niet aangetroffen. De waardekaarten (mapas de valores, laatste 09-10-2025) zijn wel openbaar. Conclusie: **geen enkele officiële bron levert objecten**; ze leveren de transactiecontext waarmee vraagprijzen en veilingwaarden getoetst worden.

---

## 1. Methode en beperkingen

- Alle claims hieronder zijn op 14-09-2026 gecontroleerd via de officiële website van de partij, via een officiële publicatie, of door ons zelf getest (curl op openbare, niet-geauthenticeerde endpoints; downloads van open data). Zoekresultaten zonder bevestiging op de bronsite zijn gemarkeerd met een lager vertrouwen.
- Geblokkeerd voor geautomatiseerd ophalen (niet omzeild): resales-online.com (HTTP 403 op alle pagina's, ook curl), pulse.urbandataanalytics.com (403), urbandataanalytics.com (TLS-handshake mislukt, ook met curl), mivau.gob.es (403; de CSV's op cdn.mivau.gob.es en het Boletín Online op apps.fomento.gob.es werken wel), opendata.registradores.org ("Request Rejected" door een WAF, ook met curl), notariado.org hoofdportaal (404 op de CIE-pagina; de liferay-pagina's werken), bdt.gva.es (503 tijdens de test), grupo-st.es (alleen JavaScript, geen inhoud), agora-mls.com (DNS bestaat niet; het domein is agoramls.es), brainsre.com/en/prices (prijstabel alleen client-side gerenderd).
- Lokale beperking: op deze Mac is geen `xlrd`/`openpyxl` beschikbaar (regel: niets installeren). De gemeentelijke MIVAU-bestanden zijn oude `.xls` (BIFF); ik heb ze op byte-niveau doorzocht op gemeentenamen, niet inhoudelijk geparseerd. Cijfers per gemeente zijn dus nog niet uitgelezen.
- Persoonsgegevens: geen namen van particulieren overgenomen; auteurmetadata in overheidsbestanden bewust niet vermeld.

---

## 2. Aggregators en commerciële dataleveranciers

### 2.1 Overzichtstabel

| Partij | Wat ze leveren | Dekking Costa Blanca/Jávea | Toegang | Prijs (gepubliceerd) | Unieke objecten of context? | Status |
|---|---|---|---|---|---|---|
| **Casafari** | Ontdubbeld aanbod uit "30,000+ Portals & Agency Websites", prijshistorie, transacties ("45 Million Registered property sales with closing prices"), AVM, Area Insights, alerts | Spanje is een van de landen met "a dedicated database for each territory"; Jávea-specifieke dekking niet bewezen | REST-API, MCP, iFrame, Data Exports, FeedCruncher, webplatform, Chrome-extensie | Geen; "Pricing depends on the type of API, data volume, and integration needs" | **Mogelijk unieke objecten** (marktbreed aanbod) + context | CONTRACT OF TOESTEMMING NODIG |
| **Brainsre** (Grupo Aura) | Adreszoeker met actueel/oud aanbod, registertransacties, AVM, rapporten (Excel/PDF), maatwerk: eenmalige levering, terugkerend via e-mail/FTP, API op maat | Spanje, Portugal, Italië, Frankrijk; lokaal niet getoetst | Webplatform (gratis proef), API op maat | Prijspagina bestaat maar is niet leesbaar zonder JavaScript → ONBEKEND | Context (comparables, transacties); objecten alleen als "aanbod" in hun platform | TECHNISCH ONDERZOEK NODIG |
| **uDA / Accumin Intelligence** (voorheen Alantra, nu Tinsa/Accumin) | Pulse (waardering, comparables uit ">20 fuentes de comparables (portales inmobiliarios, notarías, servicers, Registro, etc.)"), API "para integrar cualquier dato o funcionalidad", AVM; Accumin: "70M Real Estate Comparables", "100K New Properties Added … Each Month" | Spanje-breed; lokaal niet getoetst | Platform Pulse (403 voor ons), API | Geen | Context (comparables, indicatoren) | CONTRACT OF TOESTEMMING NODIG; site geblokkeerd → TECHNISCH ONDERZOEK NODIG |
| **Tinsa** (nu Accumin-groep) | Radar (marktstudies met testigos van taxaties + aanbod), RadarGO (particulieren), IMIE Mercados Locales (gratis kwartaalrapport), Tinsa Digital AVM via bestand of API, comparables-API | IMIE: provincie Alicante 2T 2026 "1.981 €/m²", "incremento anual del 20,83%"; gemeentepagina's alleen Alicante, Alcoy, Benidorm, Elche, Elda, Orihuela, Torrevieja — **niet Jávea** | Radar: web + PDF; AVM: bestand/API | Radar: "€29 per study", "€99/month (15 studies)", "€259/month (45 studies)", 7 dagen proef; AVM/API: geen | Context | Radar: GEVERIFIEERD EN ACTIEF (beschikbaar zonder contract, maar ALLEEN HANDMATIG); AVM/API: CONTRACT OF TOESTEMMING NODIG |
| **Gloval** | AVM, "Big Data del Mercado Inmobiliario": kadastrale, sociodemografische, prijs-, EPC- en risicodata "desde sección censal hasta nivel nacional"; GreenDataLens | Landelijk; lokaal niet getoetst | API, widgets, bestanden | "Depende de la tipología y la cantidad de inmuebles a valorar" | Context | CONTRACT OF TOESTEMMING NODIG |
| **Grupo ST (Sociedad de Tasación)** | Tools: Informe de tendencias, Agregador inmobiliario, Semáforo inmobiliario, Vigilancia Estratégica de Mercado, "Valores en tu zona" (login); diensten: ECO/RICS-taxaties, AVM, statistische modelwaardering | Landelijk (23 delegaties); publieke cijfers grof | Webtools (deels login); geen API-documentatie gevonden | Geen | Context | TECHNISCH ONDERZOEK NODIG |
| **idealista/data** (kruisverwijzing, zie R01) | API's, AVM, comparables, rapporten; "2.6+ million properties across 15,583 zones", data sinds 2005 | Landelijk | Offerte ("Pedir más información") | Geen | Context (+ aanbodhistorie) | zie R01 |

### 2.2 Casafari — detail

- **Wat het is.** Casafari indexeert advertenties, publiceert er zelf geen: "CASAFARI does not publish properties, it only indexes the listings found on these sources." Dubbele advertenties worden samengevoegd tot één objectpagina (FAQ, type 1).
- **Omvang (claims van de aanbieder, type 1):** "50+ Million Unique Properties Analysed", "7+ years Data history on closing prices", "45 Million Registered property sales with closing prices", "60,000 real estate PROFESSIONALS across 20+ COUNTRIES". Op de API-pagina: "60+ million properties with history", "100% deduplication accuracy". Deze getallen zijn niet door ons te toetsen.
- **Producten relevant voor Deal Hunter:** Property Data API (REST, "clear API references, step-by-step integration guides"), MCP en iFrame worden op de API-pagina genoemd; "Market Leads"/!Alerts geven realtime meldingen bij nieuwe objecten die aan criteria voldoen; Data Exports.
- **Commercieel:** abonnement "monthly or annually" met een vaste looptijd van "12 months" die automatisch verlengt; betaling per kaart of SEPA. Prijzen alleen via demo/offerte. Contact: commercial@casafari.com.
- **Gebruiksvoorwaarden (type 2, terms-of-use):** licentie is "personal, revocable, non-transferable and non-exclusive"; verboden zijn "Systematically collect and use of any data or content including the use of any data spiders, robots, or similar data gathering" en "Make derivative works based upon the Site or Site Content"; alle inhoud "is owned by and is the copyrighted work of CASAFARI and/or its suppliers and is licensed, not sold"; Casafari bewaart van foto's alleen thumbnails. Voor API-gebruik gelden "CASAFARI API specifications for the format and throughput limits".
- **Beoordeling.** Dit is de enige onderzochte partij die marktbreed *aanbod* kan leveren, inclusief wat op Idealista/Fotocasa staat, zonder dat wij zelf portalen benaderen. Maar: (a) de juridische basis van Casafari's eigen indexering is Casafari's zaak, niet een vrijwaring voor ons; (b) de standaardvoorwaarden sluiten precies uit wat Deal Hunter doet (systematisch verzamelen, afgeleide analyses, opslag). Alleen bruikbaar met een contract dat AI-analyse, opslagduur, afgeleide gegevens en beeldvergelijking expliciet toestaat.

### 2.3 Brainsre — detail

- Positioneert zich als "Bloomberg" van Europees vastgoed (Grupo Aura, gestart 2020); doelgroep "grandes inversores" (fondsen, banken, ontwikkelaars) én "pequeños asesores" (type 1).
- Datalagen: actueel en historisch aanbod, registertransacties, grote deals; waardering "la herramienta de valoración más completa del mercado"; rapporten naar Excel/PDF/afbeelding.
- Maatwerk: "One-time data delivery", "Recurring data via email or FTP", "API development tailored to client needs". Gratis proef via app.brainsre.com; verkoopcontact sales@brainsre.com.
- Prijzen: de pagina brainsre.com/en/prices toont alleen "Select subscription type"; de tabel wordt client-side geladen en was voor ons niet leesbaar → ONBEKEND.
- Beoordeling: sterk voor comparables en transactiehistorie op adresniveau; of het aanbod in Jávea vollediger is dan Idealista, is onbekend. Objecten hooguit als neveneffect.

### 2.4 uDA → Accumin Intelligence — detail (eigendomsketen geverifieerd)

| Datum | Gebeurtenis | Bron | Type |
|---|---|---|---|
| 2013 | uDA opgericht in Madrid | LinkedIn/Accumin (via zoekresultaat) | 1 |
| mei 2019 | Alantra CPA neemt meerderheidsbelang | alantra.com (zoekresultaat) | 1 |
| 14-05-2024 | Tinsa Group koopt uDA van Alantra LLP | accumin.com newsroom | 1 |
| sept. 2024 | Tinsa Group presenteert merk Accumin | accumin.com | 1 |
| 22-05-2025 | Accumin Intelligence: Deyde, Datacentric, uDA, Tinsa Digital AVM en on-geo samengevoegd; 120 medewerkers | accumin.com newsroom | 1 |

- Producten: Pulse (Desktop/Asset) voor waardering en comparables; de uDA-API "allows clients to integrate any uDA data or functionality … including … the automatic valuation AVM, or complete sections like a comparable grid" (zoekfragment van urbandataanalytics.com/servicios/data; de site zelf was voor ons onbereikbaar, dus vertrouwen middel).
- Accumin noemt als contact intelligence@accumin.com en +34 913 822 002 — hetzelfde nummer als Tinsa Digital. Praktisch: één offerte-aanvraag bij Accumin dekt uDA, Tinsa Digital AVM en de comparables-API.
- De masterprompt noemt "uDA (urban Data Analytics / Alantra)": die aanduiding is verouderd.

### 2.5 Tinsa / Tinsa Digital — detail

- **Tinsa Radar** (radar.tinsa.es): gebruiker tekent een gebied; uitvoer bevat "valores promedio de los testigos presentes en el área" — taxatiewaarden, aanbodprijzen, huurindicaties, onderhandelingsmarge, verdeling woningvoorraad. Testigos zijn "de oferta (capturados por Tinsa de inmuebles en venta)" of comparables uit Tinsa-taxaties. Abonnementen worden maandelijks ververst, testigos ouder dan 12 maanden vervallen. Prijzen zoals in de tabel; PDF met eigen logo; "más de 8.500 profesionales". Geen API of export genoemd.
- **RadarGO**: consumentenversie (erfenissen, particuliere investeerders), gratis via voucher; geen granulariteit gepubliceerd.
- **IMIE Mercados Locales**: gratis kwartaalrapport, laatste 2T 2026 (30-06-2026), opgebouwd uit "un histórico de más de 6 millones de valoraciones"; gemeentedetail beperkt tot grotere steden (voor Alicante: zeven gemeenten, Jávea ontbreekt).
- **Tinsa Digital AVM**: "vía fichero o directamente integrando tu herramienta con nuestra API"; "único en España aprobado por la EAA (European AVM Alliance)"; doelgroepen verzekeraars, banken, fondsen/servicers, marketing, vastgoedbedrijven; bevat betrouwbaarheidsmaten CL en FSD; "más de 1.000 new homes to the database daily". Prijs: geen. Contact hi@tinsadigital.com, 913 822 002.
- Beoordeling: Radar is direct inzetbaar als handmatige second opinion bij een dealdossier (€29 per studie) — geen bron van objecten. Voor geautomatiseerde waardering (fase B+) is de AVM-API de route, via Accumin.

### 2.6 Gloval en Grupo ST — detail

- **Gloval**: "+5M Valoraciones", "+12M Inmuebles visitados"; Big Data-dienst combineert kadaster (perceel- en elementniveau), sociodemografie per sección censal, waarden koop/huur, EPC's (ES/PT/UK), fysieke en klimaatrisico's; levering via "API, widgets, and files", responstijd "rondan los 2 segundos". Contact info@gloval.es, (+34) 915 613 388. Alleen context.
- **Grupo ST**: hoofdsite is een JavaScript-app zonder leesbare inhoud; de toolpagina tools.st-tasacion.es toont de vijf tools uit de tabel, waarvan "Valores en tu zona" achter een login zit. Geen API-documentatie, geen prijzen, geen gemeentelijke reeksen gevonden. Volgens de branchepagina van Observatorio Inmobiliario levert ST ook AVM en "valoraciones por modelo estadístico". Alleen context; eerst een gesprek nodig om te weten of er iets fijnmazigs bestaat.

---

## 3. MLS- en samenwerkingsnetwerken

### 3.1 Overzichtstabel

| Netwerk | Wat het is | Dekt Jávea? | Toegang | Prijs (gepubliceerd) | Unieke objecten? | Status |
|---|---|---|---|---|---|---|
| **Resales-Online** | MLS + CRM, Costa del Sol, Costa Blanca, Costa Cálida; New Development MLS Alicante & Murcia "550+ Live Projects" | Ja: blog noemt Javea, Torrevieja, Orihuela Costa; "more than 100 member agents" op de Costa Blanca (zoekfragment, niet zelf gezien) | Lidmaatschap; WebAPI V6 met API-key per IP-adres | Prijspagina geblokkeerd → ONBEKEND | **Ja** (directe objecten van leden), maar gebruik contractueel beperkt | CONTRACT OF TOESTEMMING NODIG |
| **MLS 03724 Teulada-Moraira** | Vereniging (CIF G42632737), opgericht door vier kantoren; volgens derdenrapport 16 kantoren; deelt exclusieven én verkoopdata | Ja: Benissa, Benitachell, Calpe, Dénia, Jávea, Moraira, Teulada | Lidmaatschap; publieke zoekfunctie op mls03724.com | Niet gepubliceerd | **Ja** (gedeelde exclusieven) + transactiedata van leden | CONTRACT OF TOESTEMMING NODIG (lidmaatschap) |
| **MLS Costa** (mlscosta.com) | Deelnetwerk resales Costa Blanca, Cálida, Almería, del Sol | Ja (Alicante als provincie); aantallen ONBEKEND | Gratis account: eigen resales delen; betaald: "extract a customized XML feed", contactgegevens listing agency, microsite | Betaald tarief niet gepubliceerd | Mogelijk | TECHNISCH ONDERZOEK NODIG |
| **MLS Mediaelx / LetsINMO** | Netwerk van webbureau Mediaelx (Elche): "over 3,000 properties", 45+ kantoren, 100+ agenten; XML-import/export | Costa Blanca, Cálida, del Sol; Jávea-aandeel ONBEKEND | Lidmaatschap; XML | Niet gepubliceerd | Mogelijk | TECHNISCH ONDERZOEK NODIG |
| **APIred — Colegio API Alicante** | Bolsa inmobiliaria van het Colegio (platform Apibolsa); publieke zoekfunctie op apired.com (filters tonen o.a. "Piscina (2009)") | Provincie Alicante; Jávea-aantal niet getoetst | Leden: alleen colegiados; import via "XML en formato Kyero 3.0" | Niet gepubliceerd | Ja (objecten van colegiados) | Publiek: ALLEEN HANDMATIG; als lid: CONTRACT OF TOESTEMMING NODIG |
| **MLS Denia Realtor®** | Lokale vereniging, multi-exclusief; "25 companies will work for you" | Dénia, ook Moraira/Calpe genoemd | Lidmaatschap | Niet gepubliceerd | Ja | ALLEEN HANDMATIG |
| **Agora MLS** (agoramls.es) | Landelijke MLS-groep, "500 member agencies", 33 provincies direct | **Nee** — in Alicante alleen Benissa (Benimo-villas) dichtbij; geen kantoren in Jávea/Dénia/Moraira | Lidmaatschap; publieke objecten op site | Niet gepubliceerd | Nauwelijks | NIET GEBRUIKEN (geen dekking) |
| **Inmobalia CRM/MLS** | CRM + MLS "Costa del Sol Property MLS", "20,000+ properties", "No freelances allowed by default" | **Nee** — uitsluitend Costa del Sol | Abonnement + XML/API | Starter €150, Full €225, Pro €300 per maand; €450 setup | Nee voor ons gebied | NIET GEBRUIKEN (geen dekking) |

### 3.2 Resales-Online — detail

- **Technisch (type 1, supportartikelen):** WebAPI V6 is sinds 01-03-2023 verplicht; oudere versies zijn verwijderd. Een API-key wordt aangemaakt onder Properties > Feed Out > API Keys en "will only function on the IP address provided". Bij aanmaak worden vier standaardfilters meegegeven. De volledige documentatie staat op webapi-v6.learning.resales-online.com (voor ons leeg/geblokkeerd).
- **Voorwaarden (type 1, Terms & Conditions of Usage):** leden mogen "display the property listings of other Member Agents only on their own website(s), and in accordance with the sharing permissions that have been set by the Listing Agent"; "It is prohibited to provide feeds including other Member Agents' property listings to any 3rd party", tenzij de listing agent schriftelijk toestemt en zelf een feed levert; afgeleide data "remains the sole property of ReSales Andalucia"; portalen mogen geen volledige databasefeeds accepteren; kopiëren van teksten/foto's van andere leden is verboden; opzeggen kan altijd zonder boete.
- **Beoordeling.** Dit is het grootste professionele netwerk met Costa Blanca-dekking en een echte API. Maar de voorwaarden zijn geschreven voor "toon op je eigen website", niet voor "bewaar, analyseer met AI en vergelijk foto's". Een interne Deal Hunter-database met netwerkobjecten van andere leden is minstens een grijs gebied. Vereist: (1) lidmaatschap van TREE Properties (of bevestiging als het al bestaat), (2) schriftelijke bevestiging van Resales-Online over intern analytisch gebruik, opslagduur en beeldvergelijking. Eigen objecten van TREE Properties mogen uiteraard wel.

### 3.3 MLS 03724 Teulada-Moraira — detail

- Officiële site mls03724.com: "four founding agencies, some with more than 20 years of experience"; deelt "properties that have been captured as a shared exclusive"; eigen ethische code; streeft naar "self-regulation at a municipal and regional level". Kantoor: Carretera Moraira a Calpe 27, 03724 Teulada; info@mls03724.com, +34 965 058 105.
- Derdenrapport (Hispania Homes, 02-10-2023, type 1): "16 agencias inmobiliarias de la zona"; leden wisselen verkoopdata uit; analyse van 420 verkochte objecten: 64% villa's; "áticos (2.550€/m2), seguido de las villas (2.087€/m2)".
- Beoordeling: het enige netwerk waar *bevestigde verkoopdata* van de Marina Alta onder leden circuleert — precies wat masterprompt §20 vraagt (transactieprijzen boven vraagprijzen). Lidmaatschapsvoorwaarden en of data-uitwisseling contractueel is vastgelegd: ONBEKEND.

### 3.4 Colegio API Alicante / APIred — detail

- Colegio: C/ Arzobispo Loaces 5, 03003 Alicante; 965 98 41 25; coapi@apialicante.com. APIred "Busca la coordinación para vender más y mejor, tratando de unir fuerzas". Platform Apibolsa (info@apibolsa.es, 919 298 360), ook in gebruik bij API Castellón en API Tarragona. Leden kunnen objecten automatisch exporteren als hun software XML in Kyero 3.0 maakt.
- Toegang tot de bolsa vereist het colegiado-lidmaatschap van het Colegio; de publieke zoekfunctie op apired.com is voor iedereen. Aantal colegiados/objecten in Jávea: niet gepubliceerd.

### 3.5 Makelaars-CRM's: wat kan een makelaar ons rechtmatig geven?

| CRM | Exportmogelijkheid (type 1, eigen documentatie) | Realtime? | Wie autoriseert | Opmerking |
|---|---|---|---|---|
| **Inmovilla** | Drie routes: iframe, API ("Integración del producto mediante programación a medida", realtime), XML-bestand dat "de forma diaria" wordt gegenereerd; daarnaast export naar Excel/XML | API ja; XML dagelijks | Het kantoor zelf | Documentatie op portal.apinmo.com; er circuleren openbare testgegevens (hier bewust niet overgenomen) |
| **Witei** | "Witei does not offer a public API service"; wel XML-export ("copy XML link", realtime bijgewerkt) en webhooks bij aanmaken/wijzigen van objecten; import van Kyero v3 | XML-link realtime | Het kantoor zelf | Geen API-keys; plan-afhankelijkheid niet vermeld |
| **Mobilia** | "Mobilia Public API" met openbare Swagger-documentatie; lezen/schrijven van objecten, contacten, leads, taken, bezoeken, documenten; integraties Zapier, n8n, WordPress, Webflow, AI-agents | Ja | Het kantoor zelf | Welke abonnementen de API bevatten en kosten: ONBEKEND |
| **Propertyflows** | Niet gevonden als Spaans makelaars-CRM. propertyflows.com is een Engelstalig AI-leadplatform voor "Property Managers" ("3-in-1 AI Sales Growth System"), zonder Spanje-verwijzing; propertyflows.es en www.propertyflows.es bestaan niet (DNS) | — | — | NIET GEBRUIKEN / niet bestaand in deze zin |
| **Inmobalia** | XML-feeds, Zapier/n8n, API | Ja | Het kantoor zelf | Alleen Costa del Sol-kantoren |
| **Resales-Online** | WebAPI V6, XML "Feed Out" | Ja | Kantoor + netwerkregels | Zie 3.2: alleen eigen objecten mogen naar derden |

**Juridische lijn (type 4, afgeleid uit de gelezen voorwaarden — [te verifiëren] door een Spaanse jurist):** een makelaar kan ons zonder probleem een feed van zijn **eigen** objecten geven (hij is licentiehouder van eigen teksten en foto's, met de gebruikelijke voorbehouden van fotografen en eigenaren). Objecten die hij zelf via een MLS van collega's ontvangt, mag hij niet doorgeven — Resales-Online verbiedt dat letterlijk, en Apibolsa/MLS 03724 werken met deelregels tussen leden. Voor elke makelaarsfeed hoort dus een korte schriftelijke afspraak: doel (acquisitieanalyse), AI-verwerking, opslagduur, geen herpublicatie, beeldvergelijking alleen intern. Dat past bij wat er al ligt met Background Properties (Kyero-feed, zes exports; sleutels blijven in feeds.js).

---

## 4. Officiële statistiek en transactiegegevens

### 4.1 Overzichtstabel

| Bron | Wat | Fijnmazigheid | Frequentie / actualiteit | Route | Licentie | Uniek/context | Status |
|---|---|---|---|---|---|---|---|
| **MIVAU — Transacciones inmobiliarias (compraventa)** | Aantal en waarde (totaal, gemiddeld) van notarieel verleden woningverkopen; libre/protegida; nieuw/tweedehands; buitenlandse kopers (per provincie) | **Gemeente** (alle gemeenten; Jávea/Xàbia, Dénia, Teulada, Benitachell, Benissa en Calp aangetroffen — type 3), provincie, regio, land | Kwartaal; voorlopig, definitief een kwartaal later; CSV laatst bijgewerkt 30-07-2026; XLS laatst opgeslagen 05-06-2026 | Boletín Online (XLS, `apps.fomento.gob.es/BoletinOnline2/?nivel=2&orden=34000000`, bestanden 34010210–34010250 voor gemeenten) en open CSV `VDP003_01.csv` (alleen provincie) | CC BY 4.0 (datos.gob.es-pagina) | Context — hét toetsingscijfer per gemeente per kwartaal | GEVERIFIEERD EN ACTIEF (handmatig/scriptbaar; XLS-parser ontbreekt lokaal) |
| **MIVAU — Valor tasado de la vivienda** | Getaxeerde waarde €/m² vivienda libre (ECO-taxaties), nieuw (<5 jaar)/ouder, protegida, aantal taxaties | Land, regio, provincie; **gemeenten >25.000 inwoners** — Jávea/Xábia staat erin (type 3), ook Calpe/Calp en Dénia; Teulada niet | Kwartaal | Boletín Online (`orden=35000000`, bestand 35103500.XLS voor gemeenten) en open CSV `VDP006_01.csv` (alleen provincie) | CC BY 4.0 | Context (taxatiewaarde, geen transactie) | GEVERIFIEERD EN ACTIEF |
| **MIVAU — VDP001_01.csv** (titel in catalogus niet gevonden) | Per gemeente: mediaan/P25/P75 van PRECIO en SUPERFICIE en aantallen (RECUENTO), colectiva/unifamiliar, 2011–2024; Jávea 2024: mediaan PRECIO colectiva 647, unifamiliar 869,3; 1.390 resp. 380 eenheden | Gemeente (kolom heet COD_POSTAL maar bevat de INE-gemeentecode 03082) | Jaar | `cdn.mivau.gob.es/.../VDP001_01.csv` (37 MB, 531.585 rijen) | Vermoedelijk CC BY 4.0 [te verifiëren] | Context; de prijsniveaus wijzen op **maandhuren** (huurreferentiesysteem) — [te verifiëren] | TECHNISCH ONDERZOEK NODIG |
| **INE — Índice de Precios de Vivienda (IPV)** | Prijsindex op basis van notariële koopakten ("bases de datos sobre viviendas escrituradas que proporciona el Consejo General del Notariado") | **Alleen land en autonome regio** — bevestigd: de INE-API geeft voor operatie IPV zes tabellen, alle "por CCAA" of nationaal (type 3) | Kwartaal; 2T 2026 gepubliceerd 07-09-2026 (+12,2% j/j nationaal); basis 2025 vanaf 1T 2026 | INE-API `servicios.ine.es/wstempus/js/ES/...` (HTTP 200, geen sleutel) | INE-hergebruik (open) | Context, grof | GEVERIFIEERD EN ACTIEF |
| **INE — Transmisiones de Derechos de la Propiedad (ETDP)** | Aantal overgedragen fincas en woningverkopen uit de Registros de la Propiedad (overeenkomst 2004) | Land, regio, **provincie**; geen gemeente | Maandelijks, ±1 maand vertraging; juni 2026: 206.138 fincas, 59.288 woningverkopen (publicatie 07-08-2026) | INE-tabellen/API | INE-hergebruik | Context | GEVERIFIEERD EN ACTIEF |
| **Registradores — Estadística Registral Inmobiliaria (SEREG)** | Compraventas, €/m², IPVVR (herhaalde verkopen), hypotheken, buitenlandse kopers | Land, regio, **provincie en provinciehoofdsteden**; geen gemeente (1T 2025: 181.625 verkopen, +5,3% k/k; Comunitat Valenciana 28,3% buitenlandse kopers) | Kwartaal (t/m 2T 2026) + jaarboeken 2004–2025 | PDF op registradores.org; opendata.registradores.org **geblokkeerd voor ons** (WAF "Request Rejected"); Baskische kopie op datos.gob.es (XLSX/CSV, CC BY 4.0, 2011–2022) | Niet vermeld | Context | ALLEEN HANDMATIG (PDF); opendata: TECHNISCH ONDERZOEK NODIG |
| **Consejo General del Notariado — CIEN** | Maandelijkse woningverkopen en €/m² uit de Índice Único Informatizado | Nationaal op de webpagina (juni 2026: 67.529 operaties, −4,0%; €2.114/m²) | Maandelijks | notariado.org/liferay/web/cien | Niet vermeld | Context | ALLEEN HANDMATIG |
| **Portal Estadístico del Notariado (penotariado.com)** | Werkelijke koopsommen: "El precio medio por m²", oppervlak, totaalprijs, aantal verkopen | **Land, regio, provincie, gemeente, postcode en zelf getekend gebied**, "siempre que los datos lo permitan" | Maandelijks; gestart 23-10-2025 | Web, kaart; registratie gratis en vrijwillig voor downloads van grafieken/rapporten; geen CSV/API gezien | **Alleen persoonlijk gebruik**: "no permitiéndose el uso comercial de los mismos"; verbod om data op te nemen "a bases de datos o ficheros informatizados … con fines comerciales", ook "aunque se exprese la procedencia" | Context van hoge kwaliteit, maar niet in een database te zetten | ALLEEN HANDMATIG; als datafeed NIET GEBRUIKEN |
| **Catastro — valor de referencia** | Fiscale referentiewaarde per object, sinds 01-01-2022 heffingsgrondslag ITP/AJD/ISD; certificaat op datum; motivering | Per object | Jaarlijks vastgesteld (2022–2026 beschikbaar) | Sede Electrónica, pagina SECAccvr: keuze uit certificaat/DNIe of Cl@ve verplicht; Guía deel II: "consultar y certificar el valor de referencia de un inmueble a una determinada fecha"; consulta masiva (XML, per NIF/referencia/polígono) voor geregistreerde gebruikers — of valor de referencia daarin zit is niet bevestigd | Geen open data | Context: fiscale ondergrens per object | ALLEEN HANDMATIG (⏸️ ACTIE VOOR JAN: met certificaat/Cl@ve, of via gestor) |
| **Catastro — mapas de valores / OVC-webservices** | Waardekaarten urbano/rústico (laatste 09-10-2025); vrije webservices (provinciero, municipiero, callejero, DNP — niet-beschermde gegevens) | Kaart per zone; objectgegevens per referencia | Jaarlijks (kaarten) | Test: `ObtenerMunicipios?Provincia=ALICANTE&Municipio=JAVEA` → HTTP 200, "JAVEA/XABIA" (cd 3, cmc 82) (type 3). Bulkdownload CAT/Shapefile vereist identificatie en licentie-acceptatie; INSPIRE-diensten | Catastro-voorwaarden | Context (identificatie, geen waarde via vrije WS) | GEVERIFIEERD EN ACTIEF (identificatie; zie perceelstroom) |
| **Generalitat Valenciana — PEGV / IVE** | Thema "Construcción y vivienda": IPV (provincie/CV), vivienda libre y protegida, bouwstatistiek; Banco de Datos Territorial met thema's valor tasado (IOEN20007) en transacciones inmobiliarias (IOEN25003); Fichas municipales | Gemeente/comarca via BDT (gespiegelde MIVAU-data) | Volgt MIVAU | pegv.gva.es (PC-Axis, Excel, CSV); bdt.gva.es gaf HTTP 503 tijdens de test | Niet expliciet (alleen "Aviso legal") | Context; geen meerwaarde boven MIVAU behalve gemak | TECHNISCH ONDERZOEK NODIG |
| **datos.gob.es** | Catalogus + API (`datos.gob.es/apidata/`, JSON/XML/CSV/RDF, geen sleutel); MIVAU heeft er 8 datasets (o.a. Transacciones, Valor tasado, Precio del suelo, Parque de viviendas) | Per dataset | Per dataset | API getest: trefwoord "vivienda" geeft 50 resultaten met veel ruis (Canarische volkstelling); publisher-filter E05233601 werkt | Hergebruik onder Ley 37/2007 en RD 1495/2011: "permit reuse … for commercial and non-commercial purposes", met bronvermelding | Catalogus | GEVERIFIEERD EN ACTIEF |

### 4.2 Wat we zelf hebben vastgesteld (type 3)

- `VDP003_01.csv` (MIVAU transacties, open data): 18.512 rijen, kolommen `CODCOMUNIDAD;COMUNIDAD;CODPROVINCIA;PROVINCIA;Tipo;Año;Trimestre;Numero_Transacciones;Valor_Transacciones` — **geen gemeentekolom**. Gemeentecijfers zitten uitsluitend in de XLS-bestanden van het Boletín Online.
- Boletín Online, sectie "Desagregación territorial: municipios": vijf XLS-bestanden (34010210 totaal, 34010220 libre, 34010230 protegida, 34010240 nueva, 34010250 segunda mano), elk ±6,3 MB met ±7.600 tekstreeksen (= vrijwel alle Spaanse gemeenten). Gemeentenamen aangetroffen: "Jávea/Xàbia", "Dénia", "Teulada", "Benitachell/Poble Nou de Benitatxell (el)", "Benissa", "Calp". De reeks 34020110–34020180 (die ik eerst aanzag voor gemeentedata) bevat provincietabellen over de waarde van transacties.
- `35103500.XLS` (valor tasado gemeenten >25.000 inw.): bevat "Jávea/Xábia", "Calpe/Calp", "Dénia", "Benidorm", "Torrevieja"; Teulada niet.
- INE-API: `OPERACION/IPV` → Id 15, Cod_IOE 30457; `TABLAS_OPERACION/IPV` → zes tabellen, alle nationaal of per CCAA. Dit bevestigt het interne onderzoek van 26-08-2026.
- Catastro OVC (vrije webservice) antwoordt zonder sleutel en kent Jávea als "JAVEA/XABIA".
- datos.gob.es-API werkt zonder sleutel; de JSON van de MIVAU-datasets toont `license: None`, terwijl de HTML-pagina "CC BY 4.0" vermeldt (type 7: klein verschil tussen API-metadata en pagina).

### 4.3 Beoordeling per bron: uniek aanbod of context?

Geen enkele officiële bron levert te koop staande objecten. Hun waarde voor Deal Hunter:

| Vraag uit masterprompt §20 | Beste officiële bron | Beperking |
|---|---|---|
| Bevestigde transactieprijzen per gemeente | MIVAU Transacciones (gemiddelde waarde per gemeente per kwartaal); penotariado.com (mediaan per gemeente/postcode, maandelijks) | MIVAU: gemiddelden, geen microlocatie; penotariado: alleen handmatig raadplegen, niet opslaan |
| Marktrichting | INE IPV (regio), INE ETDP (provincie, maandelijks), Registradores (provincie/hoofdstad) | Grof |
| Taxatieniveau | MIVAU valor tasado (Jávea, Calp, Dénia) | Alleen gemeenten >25.000; Teulada/Benitachell ontbreken |
| Fiscale ondergrens per object | Catastro valor de referencia | Per object, na authenticatie |
| Steekproefgrootte / marktdiepte per gemeente | MIVAU aantal transacties per gemeente per kwartaal | Kwartaalvertraging |

Een verdwenen advertentie is geen transactie (masterprompt §20); de enige bronnen die dat wél kunnen bevestigen zijn — in afnemende toegankelijkheid — MLS 03724 (onder leden), penotariado.com (handmatig), Casafari/Brainsre/uDA (contract, "45 Million Registered property sales" bij Casafari), en de Registro de la Propiedad per object (nota simple, buiten deze stroom).

---

## 5. Register — regels voor het bronnenregister (masterprompt §7)

| Naam | URL | Type | Toegang | Status | Notities |
|---|---|---|---|---|---|
| Casafari | https://www.casafari.com/ | Aggregator / data-API | REST-API, MCP, exports; contract | CONTRACT OF TOESTEMMING NODIG | Voorwaarden verbieden systematische extractie en afgeleide werken; 12 maanden looptijd; commercial@casafari.com |
| Brainsre | https://brainsre.com/ | Big-data-platform | Platform (gratis proef), API op maat, FTP/e-mail | TECHNISCH ONDERZOEK NODIG | Prijzen niet leesbaar; sales@brainsre.com |
| uDA / Accumin Intelligence | https://www.accumin.com/ (urbandataanalytics.com voor ons onbereikbaar) | Data/AVM/comparables | Pulse, API | CONTRACT OF TOESTEMMING NODIG | Sinds 2024 Tinsa Group, sinds 2025 Accumin; intelligence@accumin.com |
| Tinsa Radar | https://radar.tinsa.es/es | Marktstudies (PDF) | Web; €29/studie, €99 of €259 p/m | GEVERIFIEERD EN ACTIEF (ALLEEN HANDMATIG) | Geen API; testigos uit taxaties en aanbod |
| Tinsa Digital AVM / comparables-API | https://www.tinsadigital.com/que-hacemos/avm/ | AVM | Bestand of API | CONTRACT OF TOESTEMMING NODIG | hi@tinsadigital.com; nu Accumin |
| Tinsa IMIE Mercados Locales | https://www.tinsa.es/informes/imie-mercados-locales/ | Gratis kwartaalrapport | Download | ALLEEN HANDMATIG | Provincie Alicante; Jávea geen eigen reeks |
| Gloval Big Data / AVM | https://www.gloval.es/servicios/big-data-del-mercado-inmobiliario/ | Data/AVM | API, widgets, bestanden | CONTRACT OF TOESTEMMING NODIG | info@gloval.es |
| Grupo ST | https://tools.st-tasacion.es/ | Taxateur; tools | Web (deels login) | TECHNISCH ONDERZOEK NODIG | Hoofdsite JS-only |
| idealista/data | https://www.idealista.com/data/ | Data/AVM | Offerte | zie R01 | Kruisverwijzing |
| Resales-Online | https://www.resales-online.com/ (403); support.resales-online.com | MLS + CRM | Lidmaatschap; WebAPI V6, key per IP | CONTRACT OF TOESTEMMING NODIG | Netwerkobjecten niet naar derden; alleen eigen website |
| MLS 03724 Teulada-Moraira | https://www.mls03724.com/ | Lokale MLS-vereniging | Lidmaatschap | CONTRACT OF TOESTEMMING NODIG | Deelt exclusieven én verkoopdata; dekt Jávea |
| MLS Costa | https://www.mlscosta.com/ | Deelnetwerk resales | Gratis basis; betaald XML-feed | TECHNISCH ONDERZOEK NODIG | Aantallen onbekend |
| MLS Mediaelx / LetsINMO | https://mediaelx.net/en/mls-mediaelx/ | MLS van webbureau | Lidmaatschap; XML | TECHNISCH ONDERZOEK NODIG | 3.000+ objecten Costa Blanca/Cálida/Sol |
| APIred (Colegio API Alicante) | http://www.apired.com/ · https://www.apialicante.com/ | Bolsa van het Colegio | Publieke zoekfunctie; leden: colegiados | ALLEEN HANDMATIG / CONTRACT OF TOESTEMMING NODIG | Platform Apibolsa; Kyero 3.0 |
| MLS Denia Realtor | https://www.deniacasas.es/en/about-us/ (secundair) | Lokale MLS | Lidmaatschap | ALLEEN HANDMATIG | 25 kantoren volgens lid |
| Agora MLS | https://www.agoramls.es/ | Landelijke MLS | Lidmaatschap | NIET GEBRUIKEN | Geen kantoren in Jávea/Dénia/Moraira |
| Inmobalia | https://www.inmobalia.com/ | CRM + MLS Costa del Sol | Abonnement €150–300 p/m + €450 | NIET GEBRUIKEN | Geen Costa Blanca-dekking |
| Inmovilla (CRM van makelaars) | https://inmovilla.freshdesk.com/… | Makelaars-CRM | API realtime / XML dagelijks, door kantoor geautoriseerd | CONTRACT OF TOESTEMMING NODIG (per makelaar) | Alleen eigen objecten van het kantoor |
| Witei | https://faq.witei.com/en/articles/2038460-api | Makelaars-CRM | XML-link + webhooks; geen API | CONTRACT OF TOESTEMMING NODIG (per makelaar) | Kyero v3-compatibel |
| Mobilia | https://www.mobiliagestion.es/… | Makelaars-CRM | Publieke API (Swagger) | CONTRACT OF TOESTEMMING NODIG (per makelaar) | Kosten/plannen onbekend |
| Propertyflows | https://propertyflows.com/ | Niet-Spaans AI-leadplatform | — | NIET GEBRUIKEN | Geen makelaars-CRM in Spanje gevonden |
| MIVAU Transacciones inmobiliarias | https://apps.fomento.gob.es/BoletinOnline2/?nivel=2&orden=34000000 · https://datos.gob.es/es/catalogo/e05233601-transacciones-inmobiliarias-de-vivienda | Officiële statistiek | XLS (gemeente) / CSV (provincie) | GEVERIFIEERD EN ACTIEF | CC BY 4.0; kwartaal; Jávea aanwezig |
| MIVAU Valor tasado | https://apps.fomento.gob.es/BoletinOnline2/?nivel=2&orden=35000000 · https://datos.gob.es/es/catalogo/e05233601-valor-tasado-de-la-vivienda | Officiële statistiek | XLS (gemeenten >25k) / CSV (provincie) | GEVERIFIEERD EN ACTIEF | Jávea, Calp, Dénia aanwezig |
| MIVAU VDP001_01 (huurreferentie?) | https://cdn.mivau.gob.es/portal-web-mivau/Datos_MIVAU/CSV/VDP001_01.csv | Open CSV per gemeente | Download | TECHNISCH ONDERZOEK NODIG | Titel/licentie te bevestigen |
| INE IPV | https://www.ine.es/dyngs/INEbase/es/operacion.htm?c=Estadistica_C&cid=1254736152838&menu=ultiDatos&idp=1254735976607 · API servicios.ine.es | Officiële statistiek | API zonder sleutel | GEVERIFIEERD EN ACTIEF | Alleen CCAA |
| INE ETDP | https://www.ine.es/dyngs/INEbase/es/operacion.htm?c=Estadistica_C&cid=1254736171438&menu=ultiDatos&idp=1254735576757 | Officiële statistiek | Tabellen/API | GEVERIFIEERD EN ACTIEF | Provincie, maandelijks |
| Registradores ERI / SEREG | https://www.registradores.org/actualidad/portal-estadistico-registral | Officiële statistiek | PDF; open data geblokkeerd | ALLEEN HANDMATIG | contacto@registradores.org |
| Notariado CIEN | https://www.notariado.org/liferay/web/cien/inicio | Officiële statistiek | Web | ALLEEN HANDMATIG | Nationaal, maandelijks |
| Portal Estadístico del Notariado | https://www.penotariado.com/ | Officiële statistiek (gemeente/postcode) | Web; gratis registratie | ALLEEN HANDMATIG; als feed NIET GEBRUIKEN | Commercieel gebruik en databankopname verboden |
| Catastro valor de referencia | https://www1.sedecatastro.gob.es/Accesos/SECAccvr.aspx | Fiscale referentiewaarde | Certificaat/Cl@ve | ALLEEN HANDMATIG | Kaarten openbaar; consulta masiva voor geregistreerden |
| Catastro OVC vrije webservices | https://ovc.catastro.meh.es/OVCServWeb/OVCWcfCallejero/COVCCallejero.svc/json/… | Identificatie | Zonder sleutel | GEVERIFIEERD EN ACTIEF | Geen waardegegevens |
| PEGV / IVE (Generalitat) | https://pegv.gva.es/es/temas/industriaenergiamineriayconstruccion/0construccionyvivienda · https://bdt.gva.es/ | Regionale statistiek | PC-Axis/Excel/CSV | TECHNISCH ONDERZOEK NODIG | BDT gaf 503 |
| datos.gob.es | https://datos.gob.es/apidata/ | Catalogus-API | Zonder sleutel | GEVERIFIEERD EN ACTIEF | Ley 37/2007; commercieel hergebruik met bronvermelding |

---

## 6. Wat dit betekent voor fase A

1. **Objecten komen uit fase A niet van dataleveranciers of statistiek.** Binnen deze stroom zijn de enige kandidaten voor unieke objecten: Casafari (contract), Resales-Online (lidmaatschap + schriftelijke toestemming), MLS 03724 (lidmaatschap), MLS Costa/Mediaelx/APIred (nader onderzoek) en makelaarsfeeds van eigen objecten (per makelaar toestemming, zoals BP).
2. **Officiële context kan nu al draaien, zonder contract:** MIVAU-transacties en -taxatiewaarden per gemeente (kwartaal, CC BY 4.0), INE ETDP (provincie, maandelijks), INE IPV (regio). Praktische hobbel: de gemeentebestanden zijn `.xls`; een parser (`xlrd`) is niet aanwezig — ⏸️ ACTIE VOOR JAN: akkoord voor het installeren van een XLS-lezer in de Hermes-venv, of de bestanden één keer per kwartaal handmatig naar CSV omzetten.
3. **penotariado.com alleen als handmatige toets** in een dealdossier (met datum en schermafdruk als bewijs), nooit als geïmporteerde reeks.
4. **Eén offerte-aanvraag bij Accumin** dekt Tinsa Digital AVM, uDA/Pulse en comparables; een tweede bij Casafari voor marktbreed aanbod; Brainsre als alternatief. Vraag bij alle drie expliciet naar: dekking Marina Alta, AI-analyse, opslagduur, afgeleide gegevens, beeldvergelijking, rate limits, prijs.
5. **Tinsa Radar (€29/studie)** is direct bruikbaar als onafhankelijke second opinion in een dealdossier — geen contract nodig.

⏸️ ACTIE VOOR JAN (beslissingen, geen techniek):
- Is TREE Properties lid van Resales-Online, MLS 03724, MLS Costa of APIred (Colegio)? Zo ja: welke voorwaarden zijn getekend?
- Akkoord om offertes op te vragen bij Casafari, Accumin (Tinsa/uDA) en Brainsre?
- Akkoord voor een XLS-lezer op de Mac (of handmatig omzetten)?
- Valor de referencia per kandidaatobject: zelf met certificaat/Cl@ve, of via de gestor?

---

## 7. Open vragen

1. Casafari: werkelijke dekking van Jávea (aantal objecten, bronnen, ververstijd) en of de API-licentie AI-analyse, opslag en beeldvergelijking toestaat — alleen via demo/offerte.
2. Resales-Online: exact aantal Costa Blanca-leden (het cijfer "more than 100 member agents" komt uit een zoekfragment van de geblokkeerde site) en of intern analytisch gebruik van netwerkobjecten is toegestaan.
3. MLS 03724: lidmaatschapsvoorwaarden, kosten, en of de gedeelde verkoopdata contractueel voor leden beschikbaar is.
4. MLS Costa en MLS Mediaelx: aantal objecten in Jávea, tarief van de betaalde XML-feed, gebruiksvoorwaarden.
5. Brainsre en uDA/Accumin: prijzen en of er een instapabonnement bestaat dat voor een klein team betaalbaar is.
6. MIVAU VDP001_01: officiële titel en licentie van deze dataset (vermoedelijk huurreferentie); niet in de catalogus teruggevonden.
7. Catastro: of de "consulta masiva" voor geregistreerde gebruikers de valor de referencia bevat, en of een gestor/API-lid als "colaborador registrado" bulkopvragingen mag doen.
8. Registradores open data: welke fijnmazigheid het portaal biedt — voor ons geblokkeerd; ⏸️ handmatig in de browser controleren.
9. PEGV Banco de Datos Territorial: of Xàbia per kwartaal wordt getoond (503 tijdens de test).
10. Juridische toets (Spaanse jurist) van de lijn "eigen objecten wel, netwerkobjecten niet" en van de AVG-kant van makelaarsfeeds.
11. DataVenues (masterprompt §6) valt buiten deze stroom en is hier niet onderzocht.

## 8. Geblokkeerd of mislukt (niet omzeild)

- resales-online.com — HTTP 403 (homepage, /pricing/, /mls/), ook met curl; support- en blogsubdomeinen wel bereikbaar.
- www.urbandataanalytics.com — TLS-handshake mislukt (WebFetch en curl); pulse.urbandataanalytics.com — 403.
- www.grupo-st.es — 200 maar alleen JavaScript-shell; st-tasacion.es redirect ernaartoe.
- www.agora-mls.com — DNS onbekend (juiste domein: agoramls.es).
- mivau.gob.es (statistiekpagina's en methodologie-PDF's) — 403; open CSV's en Boletín Online werken.
- opendata.registradores.org — "Request Rejected" (WAF) voor WebFetch én curl.
- notariado.org/portal/centro-de-información-estadística — 404 (liferay-pagina's werken).
- bdt.gva.es — 503 op alle frames tijdens de test.
- brainsre.com/en/prices — prijstabel client-side, niet leesbaar.
- catastro.hacienda.gob.es/esp/wsvinculados.asp — 404; de PDF Webservices_Libres.pdf is binair opgehaald maar niet leesbaar zonder pdf-tools (niet geïnstalleerd).
- Lokaal: geen xlrd/openpyxl/pdftotext beschikbaar; XLS- en PDF-inhoud alleen op byte-niveau doorzocht.

---

## 9. Bronnenlijst (URL · controledatum · bewijstype)

| # | Bron | URL | Datum | Type |
|---|---|---|---|---|
| 1 | Casafari homepage | https://www.casafari.com/ | 14-09-2026 | 1 |
| 2 | Casafari Property Data API | https://www.casafari.com/products/property-data-api/ | 14-09-2026 | 1 |
| 3 | Casafari FAQ | https://www.casafari.com/faq/ | 14-09-2026 | 1 |
| 4 | Casafari Terms of Use | https://www.casafari.com/terms-of-use | 14-09-2026 | 2 |
| 5 | Brainsre homepage | https://brainsre.com/ | 14-09-2026 | 1 |
| 6 | Brainsre prijspagina (niet leesbaar) | https://brainsre.com/en/prices/ | 14-09-2026 | 7 |
| 7 | Observatorio Inmobiliario over uDA Pulse Desktop (21-04-2022) | https://observatorioinmobiliario.es/noticias/tecnologia/urbandata-analytics-lanza-una-herramienta-de-valoracion-para-profesionales/ | 14-09-2026 | 1 |
| 8 | Accumin: Tinsa Group koopt uDA (14-05-2024) | https://www.accumin.com/newsroom/corporate-actions/the-tinsa-group-acquires-urbandata-analytics | 14-09-2026 | 1 |
| 9 | Accumin: fusie tot Accumin Intelligence (22-05-2025) | https://www.accumin.com/newsroom/corporate-actions/tinsa-digital-deyde-datacentric-and-urbandata-analytics-join-forces-in-accumin-intelligence | 14-09-2026 | 1 |
| 10 | Accumin real-estate data | https://www.accumin.com/intelligence/data/real-estate | 14-09-2026 | 1 |
| 11 | uDA Data-dienst (alleen zoekfragment; site onbereikbaar) | https://www.urbandataanalytics.com/servicios/data | 14-09-2026 | 7 |
| 12 | Tinsa homepage | https://www.tinsa.es/ | 14-09-2026 | 1 |
| 13 | Tinsa Radar | https://radar.tinsa.es/es | 14-09-2026 | 1 |
| 14 | Tinsa RadarGO | https://www.tinsa.es/radar-go-big-data-inmobiliario/ | 14-09-2026 | 1 |
| 15 | Tinsa IMIE Mercados Locales | https://www.tinsa.es/informes/imie-mercados-locales/ | 14-09-2026 | 1 |
| 16 | Tinsa prijs provincie Alicante | https://www.tinsa.es/precio-vivienda/comunitat-valenciana/alicante/ | 14-09-2026 | 1 |
| 17 | Tinsa Digital AVM | https://www.tinsadigital.com/que-hacemos/avm/ | 14-09-2026 | 1 |
| 18 | Gloval homepage | https://www.gloval.es/ | 14-09-2026 | 1 |
| 19 | Gloval Big Data | https://www.gloval.es/servicios/big-data-del-mercado-inmobiliario/ | 14-09-2026 | 1 |
| 20 | Grupo ST tools | https://tools.st-tasacion.es/ | 14-09-2026 | 1 |
| 21 | Observatorio Inmobiliario bedrijfspagina ST | https://observatorioinmobiliario.es/empresas/st-sociedad-de-tasacion/ | 14-09-2026 | 1 |
| 22 | idealista/data | https://www.idealista.com/data/ | 14-09-2026 | 1 |
| 23 | Resales-Online T&C | https://support.resales-online.com/en/articles/4885689-terms-conditions-of-usage-resales-online | 14-09-2026 | 1 |
| 24 | Resales-Online API-key | https://support.resales-online.com/en/articles/4639804-how-to-create-an-api-key | 14-09-2026 | 1 |
| 25 | Resales-Online WebAPI V6 (supportartikel) | https://support.resales-online.com/en/articles/5682509-webapi-v6-full-documentation-for-web-developers | 14-09-2026 | 1 |
| 26 | Resales-Online blog | https://blog.resales-online.com/en/ | 14-09-2026 | 1 |
| 27 | Resales-Online homepage/pricing (403) | https://www.resales-online.com/pricing/ | 14-09-2026 | 7 |
| 28 | MLS 03724 Teulada-Moraira | https://www.mls03724.com/en/about-us/ | 14-09-2026 | 1 |
| 29 | Hispania Homes marktrapport Moraira (02-10-2023) | https://hispaniahomesmoraira.com/informe-del-mercado-inmobiliario-en-moraira-costa-blanca-norte/ | 14-09-2026 | 1 |
| 30 | MLS Costa | https://www.mlscosta.com/ | 14-09-2026 | 1 |
| 31 | MLS Mediaelx | https://mediaelx.net/en/mls-mediaelx/ | 14-09-2026 | 1 |
| 32 | APIred | http://www.apired.com/ | 14-09-2026 | 1 |
| 33 | Colegio API Alicante | https://www.apialicante.com/ | 14-09-2026 | 1 |
| 34 | Apibolsa werking | https://www.apibolsa.es/bolsa-inmobiliaria-como-funciona-mls.html | 14-09-2026 | 1 |
| 35 | Apibolsa klanten | https://www.apibolsa.es/bolsa-inmobiliaria-clientes-mls.html | 14-09-2026 | 1 |
| 36 | MLS Denia Realtor (via lid) | https://www.deniacasas.es/en/about-us/ | 14-09-2026 | 1 |
| 37 | Agora MLS Luxury | https://agoramlsluxury.es/en/who-we-are/ | 14-09-2026 | 1 |
| 38 | Agora MLS leden Alicante | https://www.agoramls.es/inmobiliarias-alicante/ | 14-09-2026 | 1 |
| 39 | Inmobalia homepage | https://www.inmobalia.com/ | 14-09-2026 | 1 |
| 40 | Inmobalia MLS FAQ | https://www.inmoba.com/779-faq-inmobalia-mls-equals-quality | 14-09-2026 | 1 |
| 41 | Inmovilla: web koppelen via API/XML/iframe | https://inmovilla.freshdesk.com/support/solutions/articles/103000118125-conectar-web-externa-con-inmovilla-api-xml-o-iframe | 14-09-2026 | 1 |
| 42 | Witei API-artikel | https://faq.witei.com/en/articles/2038460-api | 14-09-2026 | 1 |
| 43 | Mobilia API | https://www.mobiliagestion.es/noticias-software-inmobiliario/api-crm-mobilia-zapier-n8n-wordpress-agente-ia | 14-09-2026 | 1 |
| 44 | Propertyflows.com | https://propertyflows.com/ | 14-09-2026 | 1 |
| 45 | MIVAU Boletín Online — transacties | https://apps.fomento.gob.es/BoletinOnline2/?nivel=2&orden=34000000 | 14-09-2026 | 2/3 |
| 46 | MIVAU Boletín Online — valor tasado | https://apps.fomento.gob.es/BoletinOnline2/?nivel=2&orden=35000000 | 14-09-2026 | 2/3 |
| 47 | MIVAU open CSV transacties | https://cdn.mivau.gob.es/portal-web-mivau/Datos_MIVAU/CSV/VDP003_01.csv | 14-09-2026 | 3 |
| 48 | MIVAU open CSV valor tasado | https://cdn.mivau.gob.es/portal-web-mivau/Datos_MIVAU/CSV/VDP006_01.csv | 14-09-2026 | 3 |
| 49 | MIVAU open CSV VDP001_01 | https://cdn.mivau.gob.es/portal-web-mivau/Datos_MIVAU/CSV/VDP001_01.csv | 14-09-2026 | 3 |
| 50 | datos.gob.es dataset transacties (CC BY 4.0) | https://datos.gob.es/es/catalogo/e05233601-transacciones-inmobiliarias-de-vivienda | 14-09-2026 | 2 |
| 51 | datos.gob.es API | https://datos.gob.es/es/accessible-apidata | 14-09-2026 | 2/3 |
| 52 | datos.gob.es aviso legal | https://datos.gob.es/es/aviso-legal | 14-09-2026 | 2 |
| 53 | INE IPV | https://www.ine.es/dyngs/INEbase/es/operacion.htm?c=Estadistica_C&cid=1254736152838&menu=ultiDatos&idp=1254735976607 | 14-09-2026 | 2 |
| 54 | INE API (IPV-tabellen) | https://servicios.ine.es/wstempus/js/ES/TABLAS_OPERACION/IPV | 14-09-2026 | 3 |
| 55 | INE ETDP | https://www.ine.es/dyngs/INEbase/es/operacion.htm?c=Estadistica_C&cid=1254736171438&menu=ultiDatos&idp=1254735576757 | 14-09-2026 | 2 |
| 56 | Registradores portaal | https://www.registradores.org/actualidad/portal-estadistico-registral | 14-09-2026 | 2 |
| 57 | Registradores estadísticas de propiedad | https://www.registradores.org/actualidad/portal-estadistico-registral/estadisticas-de-propiedad | 14-09-2026 | 2 |
| 58 | Registradores ERI 1T 2025 | https://www.registradores.org/en/navegacion-por-categorias/-/asset_publisher/eXXttUcwzL5U/content/estadistica-registral-inmobiliaria-1er-trimestre-de-2025 | 14-09-2026 | 2 |
| 59 | datos.gob.es ERI-tabellen (Baskische kopie) | https://datos.gob.es/en/catalogo/a16003011-tablas-estadisticas-de-la-estadistica-registral-inmobiliaria | 14-09-2026 | 2 |
| 60 | Notariado CIEN inmuebles | https://www.notariado.org/liferay/web/cien/estadisticas-principales/inmuebles | 14-09-2026 | 2 |
| 61 | Notariado CIEN evolución compraventa | https://www.notariado.org/liferay/web/cien/estadisticas-principales/inmuebles/evolucion-de-compraventa-de-viviendas | 14-09-2026 | 2 |
| 62 | Portal Estadístico del Notariado | https://www.penotariado.com/ | 14-09-2026 | 2 |
| 63 | penotariado términos y condiciones | https://www.penotariado.com/inmobiliario/terminos-y-condiciones | 14-09-2026 | 2 |
| 64 | penotariado aviso legal | https://www.penotariado.com/inmobiliario/aviso-legal | 14-09-2026 | 2 |
| 65 | Infoconstrucción over lancering portaal (23-10-2025) | https://www.infoconstruccion.es/noticias/20251023/presentacion-portal-estadistico-notariado | 14-09-2026 | 1 |
| 66 | Catastro Sede — valor de referencia | https://www1.sedecatastro.gob.es/Accesos/SECAccvr.aspx | 14-09-2026 | 2 |
| 67 | Catastro Guía de servicios deel II (PDF) | https://www.catastro.hacienda.gob.es/ayuda/Guia_de_servicios_SEC_usuario_registrado.pdf | 14-09-2026 | 2 |
| 68 | Catastro consulta masiva (ayuda) | https://www.catastro.hacienda.gob.es/ayuda/masiva/Ayuda_Masiva.htm | 14-09-2026 | 2 |
| 69 | Catastro difusión de datos | https://www.sedecatastro.gob.es/Accesos/SECAccDescargaDatos.aspx | 14-09-2026 | 2 |
| 70 | Catastro OVC callejero (test JAVEA) | https://ovc.catastro.meh.es/OVCServWeb/OVCWcfCallejero/COVCCallejero.svc/json/ObtenerMunicipios?Provincia=ALICANTE&Municipio=JAVEA | 14-09-2026 | 3 |
| 71 | PEGV construcción y vivienda | https://pegv.gva.es/es/temas/industriaenergiamineriayconstruccion/0construccionyvivienda | 14-09-2026 | 2 |
| 72 | PEGV acerca del portal | https://pegv.gva.es/es/acercade | 14-09-2026 | 2 |
| 73 | Intern: marktdata-bronnen (25/26-08-2026) | ~/tree-es/properties/leadgen/docs/marktdata-bronnen.md | 14-09-2026 | 3 |

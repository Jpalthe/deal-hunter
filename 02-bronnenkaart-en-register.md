# Deliverable 2 — Geverifieerde bronnenkaart en bronnenregister

**Project:** TREE Deal Hunter, fase A (masterprompt §31.2)
**Controledatum:** 15-09-2026. Eigen controle vandaag: de lokale BP-dienst (http://127.0.0.1:3100, alleen lezen, 03:56 CEST en opnieuw 04:46 CEST: 224 objecten, 56 met plaatsnaam "Javea", ongewijzigd). Alle overige feiten komen uit de onderzoeksrapporten R01, R02, R03, R04, R05, R06, R07, R08, R10, R11 en R16 en hun verificatiebestanden in `onderzoek/`; waar een verificatie een claim weerlegde, staat hier de gecorrigeerde versie.
**Bewijstypen (§5):** 1 door aanbieder vermeld · 2 officiële bron · 3 door ons vastgesteld · 4 AI-gevolgtrekking · 5 berekening · 6 professional · 7 onbekend of tegenstrijdig.
**Machineleesbaar register:** `/Users/root-admin/tree-es/deal-hunter/bronnenregister.json` (75 regels: de velden uit §7, zeven rechtenvlaggen met onderbouwing, bewijstypen en bron-URL's; zes statussen). Het kantorenregister (tabel K-1) en de ontwikkelaarstabel (K-2) staan alleen in dit document.
**Geen geheimen:** feed-sleutels en privé-feed-URL's staan nergens in dit document; alleen export_id's.

## Samenvatting (10 regels)

1. Er zijn 75 registerregels onderzocht: 65 bron- en toegangsroutes plus 10 regels voor makelaars, netwerken, ontwikkelaars en eigen dealflow, met een kantorenregister van 79 kantoren. Statussen: ALLEEN HANDMATIG 39, CONTRACT OF TOESTEMMING NODIG 14, TECHNISCH ONDERZOEK NODIG 18, NIET GEBRUIKEN 4. **Geen enkele bron is vandaag "GEVERIFIEERD EN ACTIEF" voor Deal Hunter.** Twee werken technisch: de Background Properties-feed (224 objecten, 56 in Jávea op 15-09-2026) en de Idealista-assistent in een Claude-sessie.
2. Beide lopen vast op rechten zodra het systematisch wordt. BP gaf de feed voor de website; over opslag, historie, AI-analyse en beeldvergelijking is niets schriftelijk. Voor gepland gebruik van de assistent bestaat geen tekst, en de algemene Idealista-voorwaarden verbieden monitoren en opslaan voor commerciële doelen.
3. **Geen enkel portaal biedt een openbare lees-API**; bestaande koppelingen (Fotocasa Pro, Kyero v3, Green-Acres Gateway, Indomio-API, SpainHouses-XML) publiceren alleen eigen advertenties. Marktbreed lezen kan alleen tegen contract (Idealista Search API, idealista/data, DataVenues, Casafari); prijzen en licenties zijn nergens gepubliceerd.
4. **Lokale makelaars zijn een dealflowroute, geen databron.** Geen enkel kantoor publiceert een open feed, gedeeld aanbod is de norm (één perceel bij zeven kantoren) en bereidheid om vóór publicatie te delen is nergens vastgesteld; de samenwerkingsaanpak staat als concept in §2.7.
5. Zonder contract kan wél: handmatig raadplegen, e-mailalerts van portalen en servicers (accounts door Jan) en open overheidsdata (BOE-API/RSS, AEAT-veilinglijst onder CC BY 4.0, Catastro-webservices en INSPIRE, MIVAU, INE). Die zijn bereikbaar en getest, maar nog nergens aangesloten.
6. Aanbod Jávea op 15-09-2026, in advertenties en niet in objecten: Idealista 1.273 casas/chalets + 569 pisos + 333 terrenos; Fotocasa 1.805 + 295 terrenos; pisos.com 2.092; thinkSPAIN 2.605; Green-Acres 799; BP 56. Uniek aanbod is voor geen enkele bron gemeten.
7. **BP is "ons netwerk", niet "de markt".** Alle 6 geteste BP-objecten staan ook op Idealista (samen 27 advertenties). BP heeft 24 objecten van type Land in "Javea" (plaatsnaam zonder accent) tegenover 333 terrenos op Idealista, waarvan 238 met label urbano of urbanizable (15-09-2026), en levert geen status, publicatiedatum, prijshistorie of kadastrale referentie.
8. Bijzondere verkopen zijn in Jávea nu dun: 0 veilingen op het BOE-portaal, 0 bankwoningen en 1 bankperceel op Idealista, 2 Sareb-percelen bij Servihabitat Profesionales, waarvan één (perceel A) waarschijnlijk hetzelfde object is als dat Idealista-perceel en kandidaat K10. BOE-aankondigingen noemen de plaats van het goed niet; lokaliseren kan alleen via portaalalerts, de AEAT-lijst of handmatig.
9. Niets is realtime. De BP-export ontstaat vermoedelijk 's nachts (tot circa 26 uur vertraging), portaalalerts komen binnen minuten tot dagelijks, BOE en AEAT-lijst dagelijks, statistiek per maand of kwartaal.
10. ⏸️ ACTIE VOOR JAN: mail aan BP (bijlage A) nalezen en versturen, Idealista om toestemming vragen, offertes opvragen, accounts voor alerts aanmaken, het RAICV-nummer van TREE Properties opzoeken en de advocaatvragen uit R16 §7 laten beantwoorden.

---

## 1. Conclusie

**Wat Jan moet weten.**

- **De enige twee werkende bronnen zijn smal of juridisch niet af.** BP levert schone, gestructureerde data van ons eigen netwerk, maar dekt maar een klein deel van Jávea en zegt niets over status of historie. De Idealista-assistent geeft het breedste beeld van Jávea, maar alleen als handmatig hulpmiddel in een sessie; een dagelijkse, geplande monitor erop is niet toegestaan zolang Idealista dat niet schriftelijk goedkeurt (R01, R16).
- **Marktdekking van Jávea is zonder contract alleen handmatig te krijgen.** Er is geen enkele gratis, toegestane, geautomatiseerde route naar het portaalaanbod. De keuze is: handmatig werken met alerts en de assistent, of betalen voor een licentie (DataVenues, idealista/data of de Search API, Casafari).
- **Wat nu al rechtmatig te bouwen is,** zonder contract: adapters op open overheidsdata voor veilingen (BOE-sumario, AEAT-lijst) en perceelidentificatie (Catastro, INSPIRE). En de BP-adapter, zodra BP schriftelijk bevestigt wat mag.
- **Wat niet mag en niet gebouwd wordt:** scrapers of ingekochte scraper-"API's", het downloaden en hashen van portaalfoto's, en het opbouwen van een prijshistorie uit portaaldata (R16 §3.8).
- **Lokale makelaars en ontwikkelaars leveren geen feed, maar wel kansen.** Het kantorenregister (bijlage B-K) laat zien wie percelen met project en licentie verkoopt en wie renovatieobjecten voert. Vroege dealflow ontstaat alleen via een persoonlijke samenwerking met schriftelijke afspraken per partner (R06, R07; §2.7).

**Wat Jan moet beslissen (in volgorde van urgentie).** Deze besluiten worden niet los voorgelegd: de geconsolideerde top-3 vragen voor alle vijf deliverables staat in deliverable 01 §1.2 (besluit 1 hieronder valt onder vraag 2 daar; de volgorde van de rest staat in dezelfde tabel).

1. **BP:** mag de mail uit bijlage A de deur uit, en wil Jan de conceptclausule uit R16 §6.4 eerst door een advocaat laten toetsen?
2. **Idealista:** toestemming vragen voor gepland gebruik van de assistent en/of het Search API-formulier invullen. Beide vragen een eerlijke projectomschrijving die Jan zelf goedkeurt.
3. **Betaalde leesbron:** offertes opvragen bij DataVenues, idealista/data, Casafari en Accumin (plus Brainsre als alternatief), zodat Jan op prijs en rechten kan kiezen. Zonder een van deze blijft marktdekking handwerk.
4. **Accounts en lidmaatschappen:** accounts voor alerts (portalen, servicers, subastas.boe.es) zijn handelingen van Jan zelf. Daarnaast de vraag of TREE Properties al lid is van Resales-Online, MLS 03724, MLS Dénia, het Colegio API Alicante (APIred) of een Fotocasa Pro-pack heeft.
5. **Dealflow met makelaars:** keurt Jan het zoekprofiel, de prijsklassen en de opvolgtermijnen uit §2.7 goed, en staat TREE Properties in het RAICV? Zonder registernummer geen MLS-lidmaatschap en geen nummer in partnerberichten (R07 §7).

## 2. Onderbouwing

### 2.1 De bronnenkaart: wat is werkelijk gevonden

Legenda leesroute: **L-auto** = geautoriseerde machinale leesroute bestaat · **L-contract** = leesroute alleen tegen contract of toestemming · **L-hand** = alleen handmatig of via alerts · **P** = alleen publicatiekoppeling voor eigen advertenties · **–** = geen route. Details per bron: bijlage B (alle velden uit §7) en `bronnenregister.json`.

| # | Bron | Wat het Deal Hunter kan opleveren | Lezen | Publiceren | Status |
|---|---|---|---|---|---|
| R2-01 | Background Properties-feed | Objecten uit ons netwerk, commissielabel | L-contract (technisch werkend voor website; geen autorisatie voor Deal Hunter) | – | CONTRACT OF TOESTEMMING NODIG |
| R2-02 | Idealista-assistent | Breedste beeld Jávea, prijsdalingen, makelaarsnaam | L-hand (in sessie) | – | ALLEEN HANDMATIG |
| R2-03 | idealista.com, alerts, prijsrapporten | Nieuwe advertenties via alert; marktbarometer | L-hand | P (account) | ALLEEN HANDMATIG |
| R2-04 | Idealista Search API | Mogelijk portaalaanbod per API | L-contract | – | CONTRACT OF TOESTEMMING NODIG |
| R2-05 | idealista/data | Comparables, prijshistorie, AVM | L-contract | – | CONTRACT OF TOESTEMMING NODIG |
| R2-06 | idealista/tools, Market Navigator | Marktstudies; zone-download [te verifiëren] | L-contract | P | CONTRACT OF TOESTEMMING NODIG |
| R2-07 | Fotocasa en Habitaclia | Alerts ("a reformar"), index pisos Jávea | L-hand | P (Fotocasa Pro, API key) | ALLEEN HANDMATIG |
| R2-08 | Milanuncios | Particuliere advertenties | L-hand | P | ALLEEN HANDMATIG |
| R2-09 | DataVenues | Aanbod drie portalen + particulieren; API/feed op aanvraag | L-contract | – | CONTRACT OF TOESTEMMING NODIG |
| R2-10 | Kyero | Alerts; Kyero v3 is de feedstandaard | L-hand | P (Kyero v3) | ALLEEN HANDMATIG |
| R2-11 | thinkSPAIN | Filter "Price Reduced in last 30 days" | L-hand | P | ALLEEN HANDMATIG |
| R2-12 | pisos.com | "Avísame si baja", "Con precio rebajado" | L-hand | P | ALLEEN HANDMATIG |
| R2-13 | yaencontre | Alerts nieuw en prijsdaling (snippet) | L-hand | P | ALLEEN HANDMATIG |
| R2-14 | SpainHouses | Filters "To reform", "Reduced" | L-hand | P (eigen XML) | ALLEEN HANDMATIG |
| R2-15 | Green-Acres | Alerts dagelijks/wekelijks | L-hand | P (Gateway) | ALLEEN HANDMATIG |
| R2-16 | Indomio | – (403) | L-hand | P (REST-push) | ALLEEN HANDMATIG |
| R2-17 | Scraper-"API's" | – | – | – | NIET GEBRUIKEN |
| R2-18 | Casafari | Ontdubbeld marktbreed aanbod met historie | L-contract | – | CONTRACT OF TOESTEMMING NODIG |
| R2-19 | Brainsre | Aanbod- en transactiehistorie op adres | L-contract | – | TECHNISCH ONDERZOEK NODIG |
| R2-20 | Accumin (uDA, Tinsa Digital) | AVM en comparables | L-contract | – | CONTRACT OF TOESTEMMING NODIG |
| R2-21 | Tinsa Radar en IMIE | Second opinion per studie (PDF) | L-hand (betaald) | – | ALLEEN HANDMATIG |
| R2-22 | Gloval | AVM, risico- en EPC-data | L-contract | – | CONTRACT OF TOESTEMMING NODIG |
| R2-23 | Grupo ST | Onbekend | – | – | TECHNISCH ONDERZOEK NODIG |
| R2-24 | Resales-Online | Netwerkobjecten Costa Blanca | L-contract (lidmaatschap + toestemming) | P | CONTRACT OF TOESTEMMING NODIG |
| R2-25 | MLS 03724 Teulada-Moraira | Gedeelde exclusieven; verkoopdata [te verifiëren] | L-contract (lidmaatschap) | – | CONTRACT OF TOESTEMMING NODIG |
| R2-26 | MLS Costa, Mediaelx, Denia Realtor | Netwerkobjecten; betaalde XML-feed (MLS Costa) | onbekend | – | TECHNISCH ONDERZOEK NODIG |
| R2-27 | APIred / Apibolsa | Objecten van colegiados | L-hand (publiek) | P (Kyero 3.0) | ALLEEN HANDMATIG |
| R2-28 | Agora MLS, Inmobalia | Geen dekking Jávea | – | – | NIET GEBRUIKEN |
| R2-29 | CRM-exports van makelaars | Eigen objecten van meewerkende kantoren | L-contract (per makelaar) | – | CONTRACT OF TOESTEMMING NODIG |
| R2-30 | Servihabitat (+ Profesionales) | Bankgrond; 2 Sareb-percelen Jávea | L-hand (alerts met account) | – | ALLEEN HANDMATIG |
| R2-31 | Solvia (incl. Haya) | Bankwoningen Marina Alta | L-hand | – | ALLEEN HANDMATIG |
| R2-32 | Diglo (Santander) | Bankvastgoed Alicante | L-hand | – | ALLEEN HANDMATIG |
| R2-33 | Overige servicer- en bankportalen | Niet te tellen zonder browser | L-hand | P (Facilitea Casa) | ALLEEN HANDMATIG |
| R2-34 | NPL's, cesiones de remate | Vorderingen, geen huizen | – | – | NIET GEBRUIKEN |
| R2-35 | Portal de Subastas del BOE | Veilingdetails en documenten | L-hand (+ alerts, registratie) | – | ALLEEN HANDMATIG |
| R2-36 | BOE open data (sumario, RSS) | Dagelijkse trigger nieuwe veilingen | L-auto | – | TECHNISCH ONDERZOEK NODIG |
| R2-37 | AEAT bienes.js | AEAT-veilingen met RC, gps, waarde, lasten | L-auto (CC BY 4.0) | – | TECHNISCH ONDERZOEK NODIG |
| R2-38 | TGSS-veilingen | Beslagen goederen Seguridad Social | L-hand | – | ALLEEN HANDMATIG |
| R2-39 | Registro Público Concursal | Faillissementscontext | L-hand (captcha) | – | ALLEEN HANDMATIG |
| R2-40 | subastasprocuradores.com | Veilingen en venta directa | L-hand | – | TECHNISCH ONDERZOEK NODIG |
| R2-41 | eActivos | Concursale veilingen | L-hand (machinaal verboden) | – | ALLEEN HANDMATIG |
| R2-42 | Xàbia tablón, PLACSP, BOP | Gemeentelijke verkopen | L-hand (PLACSP-Atom te onderzoeken) | – | ALLEEN HANDMATIG |
| R2-43 | Catastro webservices en INSPIRE | Perceelidentificatie en geometrie | L-auto | – | TECHNISCH ONDERZOEK NODIG |
| R2-44 | Catastro Sede | PDF, valor de referencia (Cl@ve) | L-hand | – | ALLEEN HANDMATIG |
| R2-45 | Registro de la Propiedad | Eigendom en lasten per finca (9,02 EUR + btw) | L-hand (per dossier) | – | ALLEEN HANDMATIG |
| R2-46 | MIVAU | Aantal transacties per gemeente; taxatiewaarde Jávea | L-auto (CSV provincie; XLS gemeente) | – | TECHNISCH ONDERZOEK NODIG |
| R2-47 | INE | Marktrichting regio/provincie | L-auto | – | TECHNISCH ONDERZOEK NODIG |
| R2-48 | Portal Estadístico del Notariado | Koopsommen per gemeente/postcode | L-hand (geen commercieel gebruik) | – | ALLEEN HANDMATIG |
| R2-49 | Registradores-statistiek | Provinciecijfers | L-hand | – | ALLEEN HANDMATIG |
| R2-50 | Lokale makelaarssites (79 kantoren, tabel K-1) | Renovatie- en perceelaanbod per kantoor; referenties voor ontdubbelen | L-hand | – | ALLEEN HANDMATIG |
| R2-51 | Directories en gemeentelijke lijst (xabia.org, Trustlocal, Javea Guide, Jávea.com) | Startvoorraad van het kantorenregister | L-hand | – | ALLEEN HANDMATIG |
| R2-52 | Rechtstreekse aanlevering door partners (eigen dealflow) | Objecten met mandaatstatus, mogelijk vóór brede publicatie | L-contract (per partner) | – | CONTRACT OF TOESTEMMING NODIG |
| R2-53 | MLS Dénia | Gedeeld exclusief aanbod onder leden | L-contract (lidmaatschap) | – | CONTRACT OF TOESTEMMING NODIG |
| R2-54 | ASICVAL | "Exclusiva compartida" onder leden | L-contract (lidmaatschap) | – | CONTRACT OF TOESTEMMING NODIG |
| R2-55 | RAICV (register vastgoedbemiddelaars) | Controle van het registernummer van partners | L-hand (JavaScript-formulier) | – | ALLEEN HANDMATIG |
| R2-56 | Ontwikkelaarssites (7 partijen, tabel K-2) | Projectstatus, grondvraag, afnemers route C/D | L-hand | – | ALLEEN HANDMATIG |
| R2-57 | PROVIA (promotoren Alicante) | Netwerkkanaal naar promotoren | L-hand | – | ALLEEN HANDMATIG |
| R2-58 | Architecten-colegios (CTAA, COAT Alicante) | Architecten voor "proyecto sin cliente" | onbekend (inlog) | – | TECHNISCH ONDERZOEK NODIG |
| R2-59 | Wallapop en Facebook-groepen | Particuliere advertenties (handmatig) | L-hand | P (account) | ALLEEN HANDMATIG |
| R2-60 | ICV-planlaag Planeamiento (0702) | Planklasse, zone en instrument per perceel: eerste filter, informatief | L-auto (CC BY 4.0) | – | TECHNISCH ONDERZOEK NODIG |
| R2-61 | ICV-sectorlagen 0701, 0505, 0506 (o.a. PATRICOVA) | Signalen over overstroming, natuur, bos en brand en erfgoed per perceel | L-auto (CC BY 4.0) | – | TECHNISCH ONDERZOEK NODIG |
| R2-62 | ICV ArcGIS REST (ordenación territorial, espacios protegidos, incendios) | PATRICOVA-, PATIVEL-, Red Natura- en brandvlakken; query met perceelomtrek | onbekend (licentie niet vermeld) | – | TECHNISCH ONDERZOEK NODIG |
| R2-63 | IDEE ARPSI | Overstromingsgevaar als kruiscontrole op PATRICOVA | L-auto (vermelding MITECO) | – | TECHNISCH ONDERZOEK NODIG |
| R2-64 | MITECO kustdomein DPMT | Deslinde en servidumbre 20/100 m | onbekend (dienst onbereikbaar op 15-09-2026) | – | TECHNISCH ONDERZOEK NODIG |
| R2-65 | MITECO waterlopen DPH en SNCZI | Waterlopen en zonas inundables | onbekend (dienst onbereikbaar op 15-09-2026) | – | TECHNISCH ONDERZOEK NODIG |
| R2-66 | IGME geologische kaart (GEODE, MAGNA) | Geologie per punt, zonder juridische werking | L-auto onder voorwaarde (contact IGME bij betaalde dienst) | – | TECHNISCH ONDERZOEK NODIG |
| R2-67 | GVA-planregister Xàbia | Normdocumenten en modificaciones voor de regeltabel | L-hand | – | ALLEEN HANDMATIG |
| R2-68 | DOGV | Planstatus, schorsingen en regionale besluiten | L-hand | – | ALLEEN HANDMATIG |
| R2-69 | Xàbia sede en urbanismepagina's | Tasas, ordenanzas, loket voor informe urbanístico en cédula | L-hand | – | ALLEEN HANDMATIG |
| R2-70 | SUMA (suma.es) | Adjudicación directa; SUMA-veilingen zelf via R2-35 en R2-36 | L-hand (robots Disallow /) | – | ALLEEN HANDMATIG |
| R2-71 | ATV | Geen veilingkanaal gevonden | onbekend | – | TECHNISCH ONDERZOEK NODIG |
| R2-72 | GVA-patrimonium (hisenda.gva.es) | Verkoop van vastgoed van de Generalitat | L-hand | – | ALLEEN HANDMATIG |
| R2-73 | Patrimonio del Estado | Verkoop van rijksvastgoed; aankondigingen ook in BOE V-B | L-hand | – | ALLEEN HANDMATIG |
| R2-74 | TEJU (gerechtelijke edicten) | Notificatie-edicten, geen veilingen; bevat persoonsgegevens | L-hand (robots sluit pad uit) | – | ALLEEN HANDMATIG |
| R2-75 | ORGA FAQ-pdf | Alleen ORGA-regels; niet bruikbaar voor LEC-veilingen | – | – | NIET GEBRUIKEN |

Telling statussen (75 regels): ALLEEN HANDMATIG 39 · CONTRACT OF TOESTEMMING NODIG 14 · TECHNISCH ONDERZOEK NODIG 18 · NIET GEBRUIKEN 4 · TOEGANG AANGEVRAAGD 0 · GEVERIFIEERD EN ACTIEF 0.

**Enkele statussen zijn bewust strenger gezet dan in de onderzoeksrapporten.** R04, R08 en R11 gaven "GEVERIFIEERD EN ACTIEF" aan Tinsa Radar, MIVAU, INE, AEAT-lijst, BOE-API en Catastro. De verificaties wezen erop dat niets daarvan is aangesloten of draait; volgens de projectregel heet iets pas actief als het getest draait. Die bronnen staan hier op TECHNISCH ONDERZOEK NODIG (rechten in orde, koppeling nog te bouwen) of ALLEEN HANDMATIG (Tinsa Radar zonder abonnement) (R04-verificatie F2; R11-verificatie F13). Om dezelfde reden: R06 gaf BP "GEVERIFIEERD EN ACTIEF" (hier CONTRACT OF TOESTEMMING NODIG, R06-verificatie F1), en R07 gaf de gemeentelijke kantorenlijst en de Idealista-assistent "GEVERIFIEERD EN ACTIEF (handmatig)" (hier ALLEEN HANDMATIG). Voor de toegevoegde regels geldt hetzelfde: R12 gaf de ICV-planlaag, het GVA-planregister en de DOGV "GEVERIFIEERD EN ACTIEF"; hier staan ze op TECHNISCH ONDERZOEK NODIG (R2-60) en ALLEEN HANDMATIG (R2-67, R2-68), zoals in deliverable 05 §3.4.

**Eén status per regel geldt voor de toegestane leesroute.** Waar geautomatiseerd gebruik uitdrukkelijk verboden is (onder meer eActivos, Kyero, Servihabitat, Solvia, Diglo), staat de handmatige route op ALLEEN HANDMATIG en geldt voor elke automatisering NIET GEBRUIKEN. Deliverable 04 (§2.2 en §2.11) noteert eActivos nu ook als ALLEEN HANDMATIG, met "geautomatiseerd: niet gebruiken" als toelichting (eActivos aviso legal, https://www.eactivos.com/aviso-legal, 15-09-2026, type 2). R2-27 (APIred) geldt voor de openbare zoekfunctie; het ledendeel van APIRed vraagt colegiación en valt onder CONTRACT OF TOESTEMMING NODIG (R07-verificatie R07-03).

### 2.2 Publicatiekoppeling is geen leestoegang

Masterprompt §6 vraagt dit onderscheid expliciet. Alles wat hieronder als "publiceren" staat, geeft TREE **geen** recht op andermans advertenties. Bij Idealista werkt het zelfs andersom: wie publiceert, geeft Idealista een wereldwijde, sublicentieerbare licentie op de eigen data, ook voor prijsrapporten en historische referenties (voorwaarden §8.2, https://st1.idealista.com/ayuda/wp-content/uploads/2021/11/2021-Hasta-11-11-2021-Terminos-y-condiciones.pdf, 15-09-2026, type 2).

| Aanbieder | Publicatiekoppeling (eigen advertenties) | Leesroute voor andermans aanbod | Bron |
|---|---|---|---|
| Idealista | Professioneel account; CRM-/feedkoppeling (formaat [te verifiëren]) | Search API alleen op aanvraag; idealista/data tegen offerte; assistent alleen handmatig | R01 (type 2/3) |
| Fotocasa, Habitaclia, Milanuncios | Fotocasa Pro met API key via CRM (Witei, Inmoweb) | Portalen: geen. Wel DataVenues-API en data-feed op aanvraag ("Consúltanos por nuestras APIs y nuestro Data feed", https://datavenues.com/, 15-09-2026, type 1) | R02 + verificatie |
| Kyero | Kyero v3 XML-import; eigen exportfeed per makelaar met alleen eigen objecten | Geen | R03 (type 2) |
| Green-Acres | XML Gateway v4.1, cancel-and-replace | Geen | R03-verificatie (type 2) |
| Indomio | REST-push-API, HTTP BASIC, IP-whitelist, "almost real time" | Geen (feedback-API's alleen over eigen advertenties) | R03-verificatie (type 2) |
| SpainHouses | Eigen XML (cartera.xsd) via 32+ CRM's | Geen | R03 (type 2) |
| thinkSPAIN, pisos.com | XML via CRM, specificatie niet openbaar | Geen | R03 (type 1/7) |
| Resales-Online | WebAPI V6 / Feed Out | Netwerkobjecten alleen op eigen website tonen; doorgeven aan derden verboden | R04 (type 1) |
| Facilitea Casa (CaixaBank) | Makelaars publiceren kosteloos | Geen | R10 (type 1) |

### 2.3 Welke toegang is bevestigd — en wat de beperkingen zijn

#### Background Properties (R2-01) — technisch werkend, juridisch open

Bevestigd (type 3, R05 + verificatie, eigen controle 15-09-2026):

- Zes exports voor TREE (export_id 26, 27, 29, 30, 31, 32) plus export 36 voor de site-import leveren Kyero v3-XML. De lokale properties-api toonde om 03:56 CEST: **224 objecten, waarvan 56 met plaatsnaam "Javea"** (26 villa's, 24 percelen, 4 appartementen, 2 zonder type), 27 vanaf 750.000 EUR, laatste ophaalronde 15-09-2026 01:00 UTC (http://127.0.0.1:3100/api/stats en /api/properties?town=Javea&limit=100, type 3). Op 14-09-2026 23:00 waren het er 225 en 57.
- Filteren op "Jávea", "Xàbia" of "Xabia" geeft 0 treffers (type 3, 15-09-2026). Elke koppeling moet plaatsnamen normaliseren.
- De export-URL stuurt door naar een statisch bestand; een client met de standaard curl-User-Agent krijgt HTTP 403, een verzoek zonder User-Agent wordt bediend (R05-verificatie, type 3). Een nieuwe Python-adapter moet dit eerst testen.

Beperkingen (type 3 tenzij anders vermeld):

- **Momentopname zonder status**: geen verwijderingsmelding, publicatiedatum, prijshistorie, bouwjaar, staat, kadastrale referentie of verkopende makelaar. Verdwijnen betekent NIET MEER GEVONDEN, nooit verkocht.
- **Datakwaliteit**: `pool` is vrije tekst in drie talen (223 van 225 gevuld; het eerdere lokale feit "geen pool" is weerlegd, R03-verificatie); energielabel deels "Processing"/"In aanvraag"; 11 objecten met coördinaten op een standaardpunt in Miami (3 in Jávea); 39 refs wijken af van de URL; HTML in omschrijvingen.
- **Bronuitval is echt**: de properties-api heeft geen importbescherming en viel 184 keer naar 0 objecten (DNS), onder meer op 14-09-2026 om 22:12. Een herstartlus veroorzaakte ruim 800 verzoeken aan BP zonder blokkade. De site-import heeft wél bescherming (lege feed, krimpdrempel 30 %, `withdrawn`), maar draaide meerdaagse periodes niet (30-08→31-08, 02-09→07-09, 09-09→11-09) (R05-verificatie).
- **Rechten**: geen feedvoorwaarden of schriftelijke afspraak gevonden. De aviso legal van BP eist "autorización escrita previa" voor "reproducción total o parcial, uso, explotación" (https://backgroundproperties.com/aviso-legal/, 15-09-2026, type 2); die tekst is een websitesjabloon en regelt de feed niet, wat vastleggen juist nodiger maakt (R16-verificatie F-10).

#### Idealista-assistent (R2-02) — technisch werkend, alleen handmatig

Bevestigd (type 3, R01-verificatie 15-09-2026, exact gereproduceerd):

- `search_properties` geeft echte advertenties met `total`, prijs, prijsdaling, m², kamers, benaderde coördinaten, beschrijving, kenmerken en `userType`. `property_detail` geeft daarnaast makelaarsnaam (`commercialName`), externe referentie, energielabel, bouwjaar ("Construido en …"), een grove wijzigingsdatum en alle foto's met tag. Een onbestaande code geeft `outcome: "not_found"`.
- Tellingen Jávea 15-09-2026: 1.273 casas/chalets (70 para reformar), 569 pisos (19 para reformar), 333 terrenos (238 met label urbano of urbanizable — dat is geen bouwrijpheid), 77 obra nueva, 4 chalets in de laatste 48 uur, 0 bankwoningen, 1 bankperceel (111869151; waarschijnlijk hetzelfde Sareb-perceel als perceel A bij Servihabitat Profesionales en kandidaat K10, type 4, zie §2.5) (R01-verificatie, R10-verificatie).

Beperkingen:

- Maximaal 50 resultaten per aanroep, geen offset of sortering; volledige dekking vraagt deelzoekopdrachten (type 3).
- Filters worden uit tekst afgeleid en zijn niet stabiel: "bajada de precio" wordt een sortering; het typefilter bleef op 14-09 weg en op 15-09 staan; het filter "de bancos" viel één keer stil weg; bij buurgemeenten koos de tool soms een straat in Jávea. Altijd het veld `summary` controleren (R01-verificatie R01-14; R10 Q4, Q8, Q9; type 3).
- Geen publicatiedatum, geen prijshistorie (alleen laatste daling), exact adres meestal verborgen (43 van 50), afbeeldingen in zoekresultaten vervaagd (R16-verificatie N-5). Of `phone1` bij professionele advertenties een doorschakelnummer van Idealista is, is niet bewezen: het eerdere interne onderzoek (25/26-08-2026) en R10 §5 gaan ervan uit, maar geen bron toont het aan (R06-verificatie R06-15 en F15, type 4). Bij particuliere advertenties (`userType` "private") staat een gewoon mobiel nummer; dat is een persoonsgegeven en wordt niet overgenomen (type 3). Deliverables 04 (§2.10) en 05 (§3.3) volgen dezelfde voorzichtige lezing van de R06-verificatie.
- **Rechten**: geen voorwaarden voor de app of MCP gevonden. De algemene voorwaarden (versies 20-11-2020 en 17-02-2024) verbieden toegang via "robot, spider, scraper u otro medio automático o proceso manual" zonder schriftelijke toestemming en "monitorizar … guardar" voor commerciële activiteit; ze staan wel "registrarte para guardar búsquedas y favoritos" toe (R01-verificatie A1–A2, type 2). De actuele versie van 30-04-2025 gaf HTTP 403 (type 7). Gepland of systematisch gebruik: **ONBEKEND**, dus niet doen zonder schriftelijk akkoord.

#### Open overheidsdata — rechten in orde, nog niet aangesloten

Getest en bereikbaar, maar zonder draaiende koppeling (daarom TECHNISCH ONDERZOEK NODIG):

- **BOE-sumario-API** levert XML én JSON (met Accept-header; zonder header HTTP 400, vóór publicatie 404). Hergebruik mag commercieel met bronvermelding (licentie AEBOE 27-06-2024) (R08-verificatie, type 2/3). Beperking: aankondigingen bevatten alleen orgaan, nummer en portaallink, niet de plaats van het goed (LEC art. 646.1; RGR art. 101.3) (R08-verificatie A2, type 2).
- **AEAT `bienes.js`**: dagelijkse lijst onder CC BY 4.0 met referencia catastral, CRU, gps, waardering en lasten; 230 onroerende goederen landelijk, 0 in Xàbia; `cp` is een getal zonder voorloopnul (R08-verificatie, type 3).
- **Catastro-webservices en INSPIRE**: werken zonder sleutel; ATOM voor Xàbia staat in EPSG:25831; bij te veel verzoeken volgt weigering "generalmente 10 días"; de INSPIRE-licentie staat eigen gebruik en getransformeerde producten toe, geen doorlevering van de originele gegevens (R11-verificatie, type 2/3).

### 2.4 Actualiteit per bron

"Realtime" mag alleen heten wat over de hele keten realtime is (§10). Dat geldt voor geen enkele bron.

| Bron | Hoe actueel | Wat ontbreekt voor wijzigingsdetectie | Bewijs |
|---|---|---|---|
| BP-feed | Exportbestanden in één nachtvenster (01:34–02:55 CEST) aangemaakt; wij halen elk uur (api) en elke 2 uur (site); tot circa 26 uur vertraging | Publicatiedatum, status, prijshistorie; `date` = laatste wijziging (betekenis bij BP niet bevestigd) | R05 (3; "elke nacht" 4; vertraging 5) |
| Idealista-assistent | Stand van het portaal op het moment van aanroepen | Publicatiedatum; alleen filter "laatste 48 uur" en grove wijzigingstekst | R01 (3) |
| Idealista-alerts | Direct, dagelijks of wekelijks (helpcentrum 403, snippet; artikel 2015) | Alleen nieuwe advertenties; prijswijziging alleen voor gevolgde objecten | R01 (2/7) |
| Fotocasa-alerts | Binnen enkele minuten, gebundeld, beperkt aantal keren per dag, niet 00:00–06:00 (artikel 2020) | Actualiteit van het artikel [te verifiëren] | R02-verificatie (1) |
| Kyero-alerts | Standaard dagelijks, alleen nieuwe objecten | Prijsdalingen niet genoemd | R03 (2) |
| Green-Acres-alerts | Dagelijks of wekelijks | — | R03-verificatie (3) |
| DataVenues | "Actualizados diariamente" (aanbieder) | Specificatie API/feed onbekend | R02 (1) |
| Casafari | Alerts realtime volgens aanbieder | Niet getoetst | R04 (1) |
| BOE-sumario/RSS | Dagelijks 's ochtends | Plaats van het goed | R08-verificatie (3) |
| AEAT bienes.js | Dagelijkse versie (circa 15:23) | Alleen AEAT-veilingen | R08 (3) |
| Portal de Subastas (alerts) | Alert bij opening van de biedperiode; geen officiële notificatie | Deadlines alleen uit detailpagina of edicto | R08-verificatie (2) |
| Servicer-alerts | Solvia "al instante" (aanbieder); overige onbekend | Account nodig | R10 (1) |
| Catastro | Webservices en WFS actueel; ATOM 2 keer per jaar (laatst 21-08-2026) | — | R11-verificatie (2/3) |
| Fotocasa-index, Idealista-prijsrapport, Notariado | Maandelijks | Alleen pisos (Fotocasa); methodiekbreuk juli 2026 (Idealista) | R01, R02, R04 (2/3) |
| MIVAU, INE IPV, Registradores | Kwartaal, vertraging ruim een kwartaal (MIVAU t/m 2026-T1) | Gemeentelijke transactiewaarde bestaat niet (alleen aantal) | R04-verificatie (3) |

### 2.5 Dekking: eerlijk gerapporteerd

**Welke bronnen kennen we?** De 75 registerregels in bijlage B: 1 partnerfeed, 1 assistent, 14 routes van portalen en hun datadiensten, 1 categorie scrapers, 6 dataleveranciers, 6 MLS- en makelaarsroutes, 5 bank- en servicerroutes, 14 veiling-, insolventie- en overheidsverkooproutes (waarvan 6 toegevoegd als R2-70 t/m R2-75), 7 perceel-, register- en statistiekbronnen, 10 plan- en kaartbronnen voor de perceelmodule (R2-60 t/m R2-69) en 10 regels voor lokale makelaars, netwerken, ontwikkelaars en eigen dealflow (§9). Bij die laatste groep horen het kantorenregister (tabel K-1: 79 kantoren, 75 uit R06 en 4 uit de R06-verificatie en R07), een lijst van 48 kantoornamen die alleen uit directories, de gemeentelijke lijst of de BP-partnerlijst bekend zijn, en de ontwikkelaarstabel (K-2). Vier regels staan op NIET GEBRUIKEN: drie bewust uitgesloten bronnen en de ORGA-pdf als bron voor LEC-veilingen (R2-75).

**Welke zijn aangesloten?**

| Bron | Aangesloten? | Waarvoor | Beperking |
|---|---|---|---|
| BP-feed | Ja, als dienst (properties-api, site-import) | Website treeproperties.es | Geen Deal Hunter-rechten; geen importbescherming in properties-api |
| Idealista-assistent | Ja, als tool in een Claude-sessie | Ad-hoconderzoek | Geen draaiend systeem; gepland gebruik niet toegestaan zonder akkoord |
| Alle andere 73 | Nee | — | Accounts, contracten, samenwerkingsafspraken of een eerste koppeling ontbreken |

**Welke ontbreken voor een volledig beeld van Jávea?**

1. **Een geautoriseerde, geautomatiseerde bron voor het portaalaanbod.** Kandidaten: Idealista Search API, idealista/data, DataVenues, Casafari. Geen van vieren is aangevraagd; prijzen en rechten zijn onbekend.
2. **Transactieprijzen per gemeente.** MIVAU geeft per gemeente alleen het aantal transacties, geen waarde (R04-verificatie F1). Het Notariado-portaal heeft koopsommen per gemeente en postcode, maar verbiedt commercieel gebruik. Casafari claimt sluitprijzen zonder landenopgave; DataVenues kondigde notariële sluitprijzen aan zonder bevestigde livegang.
3. **Pre-market en netwerkaanbod:** gedeelde exclusieven van MLS 03724 en MLS Dénia, Resales-Online-netwerkobjecten, servicer-aanbod voor samenwerkende makelaars en rechtstreekse aanlevering door kantoren, ontwikkelaars en architecten (R2-52). Alles vraagt lidmaatschap of een samenwerkingsafspraak; MLS-lidmaatschap en bemiddeling vragen daarnaast een RAICV-inschrijving, en die van TREE Properties is ONBEKEND (R07 §1.1, §7).
4. **Veilinglokalisatie:** BOE-data noemt de plaats van het goed niet. Zonder alerts op het portaal (registratie door Jan) of toestemming van de AEBOE blijft dit handwerk, behalve voor AEAT-veilingen (`bienes.js`).
5. **Voorwaardenteksten** die we niet machinaal konden lezen: fotocasa.es (JavaScript), Milanuncios (403), Kyero (403), Indomio (403), de actuele Idealista-voorwaarden (403) en de gebruikersvoorwaarden van subastas.boe.es (alleen na registratie).

**Aanbod in Jávea per bron (te koop, advertenties, niet objecten).** Portalen tellen per advertentie en dezelfde woning staat vaak bij meerdere makelaars; de getallen zijn niet op te tellen en zeggen niets over uniek aanbod.

| Bron | Woningen | Percelen | Datum en methode | Bewijs |
|---|---|---|---|---|
| Idealista (assistent) | 1.273 casas/chalets + 569 pisos (+ 77 obra-nueva-promoties) | 333 terrenos | 15-09-2026, tool-teller `total` | 3 |
| Fotocasa | 1.805 casas y pisos (51 a reformar) | 295 | 15-09-2026, paginakop | 3 |
| Habitaclia | 1.757 | 285 terrenos y solares | 15-09-2026, paginakop | 3 |
| Milanuncios | 2.734 (incl. niet-vastgoed) | 275 | 15-09-2026, paginakop | 3 |
| pisos.com | 2.092 casas y pisos | onbekend | 15-09-2026, één verzoek | 3 |
| thinkSPAIN | 2.605 totaal | 151 bouwkavels | 15-09-2026, pagina | 3 |
| Green-Acres | 799 totaal | onbekend | 15-09-2026, pagina | 3 |
| SpainHouses | 488 (322 huizen) | onbekend | 15-09-2026, pagina | 3 |
| Kyero / Indomio / yaencontre | ±1.717 / ±1.994 / ±1.755 casas + 742 pisos | yaencontre ±413 | Zoekmachine-snippets zonder datum | 7 |
| Background Properties | 32 (26 villa, 4 appartement, 2 zonder type) | 24 | 15-09-2026 03:56, lokale API | 3 |
| Bank/servicer | 0 bankwoningen (Idealista, Servihabitat, Diglo) | 2 Sareb-percelen (Servihabitat Profesionales); perceel A daarvan is ook het enige "de bancos"-perceel op Idealista, dus 2 unieke objecten | 15-09-2026 | 3 (koppeling perceel A = 111869151: 4, zie onder) |
| Veilingen | 0 (BOE-portaal, AEAT-lijst) | 0 | 14 en 15-09-2026 | 3 |

**Bankvastgoed: één object, drie vermeldingen.** Het Idealista-bankperceel 111869151 (904.000 → 725.000 EUR) draagt `commercialName` "Servihabitat" en `externalReference` 60709763, en R10 koppelt het aan Servihabitat-promotie 06124187, perceel A "Balcón al Mar": 16 fincas, 17.775 m², eigendom van Sareb volgens de aanbieder (R10 §6; R10-verificatie R10-08, R10-17 en A1; https://inversores.servihabitat.com/es/venta/promociones/terreno-urbanonoconsolidado/alicante-marinaalta-balconalmarjavea/06124187, 15-09-2026, type 1/3). Waarschijnlijk is het ook kandidaat K10 in R15 (Idealista 107655781, dubbel met 111869151; R15-verificatie R15-09); prijs, eerdere prijs en m² zijn gelijk, maar kadastrale referenties ontbreken (type 4). De planologische status is **tegenstrijdig (type 7)**: Servihabitat noemt het "urbano no consolidado", Idealista "Terreno urbanizable" (R10-verificatie A4). Volgens de servicer valt de verkoop onder btw in plaats van ITP en is hij alleen voor professionals (R10 §6, type 1). Deliverables 01, 03, 04 en 05 lezen K10 op dezelfde manier; welke klasse geldt, moet uit het kadaster en de gemeente blijken, niet uit een van beide advertenties. "De bancos" in Jávea is 0 voor woningen (HOME) en 1 voor percelen (LAND) (R10-verificatie R10-09, type 3).

**Welke bronnen leveren waarschijnlijk unieke objecten?** Voor geen enkele bron is uniek aanbod gemeten; wat volgt is gevolgtrekking (type 4) op basis van hoe het aanbod binnenkomt.

| Waarschijnlijk vooral gedeelde voorraad | Mogelijk uniek of eerder zichtbaar | Onderbouwing |
|---|---|---|
| BP, Kyero, thinkSPAIN, Green-Acres, SpainHouses, Indomio, yaencontre: gevoed door makelaars-CRM-feeds | Particuliere advertenties (Milanuncios 38 op de particulierenpagina, deels geen vastgoed; Habitaclia 7; pisos.com; DataVenues GO met eigenaarscontact tegen contract) | BP: 6 van 6 op Idealista (R05, type 3) |
| Idealista zelf is de breedste verzamelbak (makelaars én particulieren) | Servihabitat Profesionales: perceel B (Toscal–Cap Martí) niet op Idealista gezien | R10 (type 3) |
| Casafari: indexeert portalen en makelaarssites, dus breed maar niet uniek | Gedeelde exclusieven MLS 03724 en MLS Dénia, netwerkobjecten Resales-Online (lidmaatschap) | R04, R07 (type 1/7) |
| De meeste lokale makelaarssites: één perceel in Garroferal del Montgó (1.570 m², 505.000 EUR) staat bij zeven kantoren, drie met BP-referentie 4676JAV; Paradise en Arzuaga tonen allebei exact "Jávea 225"; Casas Costa Blanca gebruikt beelden uit minstens negen externe bronnen | Eigen projecten van bouwers en ontwikkelaars (Miralbo, Promociones Jávea, Terramar) en objecten met eigen kantoorreferenties (Coldwell Banker Solaris "CBS…", Koch & Varlet "KV…"); exclusiviteit nergens bevestigd | R07-verificatie R07-08 (3); R06-verificatie A7, R06-08 (3; duiding 4); R06 §5 (1/4) |
| — | Veilingen (BOE-portaal, AEAT, TGSS) en gemeentelijke verkopen: verschijnen niet of later op portalen | R08 (type 2/4) |
| — | Aanbod dat kantoren, ontwikkelaars of architecten vóór brede publicatie willen delen (R2-52, route D); bereidheid per kantoor ONBEKEND | §2.7; R06 §8, R07 §5 (4) |

**Hoe actueel?** Zie §2.4. Kern: BP maximaal circa een dag oud; de assistent en portaalalerts het actueelst; veilingtriggers dagelijks; alle prijsstatistiek een maand tot ruim een kwartaal oud.

**Claim die we niet maken.** "100 % van de markt" of "heel Jávea": niet te onderbouwen. De Idealista-teller is de beste nulmeting van het zichtbare portaalaanbod, maar mist aanbod dat niet op Idealista staat (pre-market, veilingen, deel van het servicer-aanbod) en telt dubbele advertenties mee (R05: één object tot 10 advertenties).

### 2.6 Welke rol Background Properties kan spelen

**Conclusie: BP is ons netwerk, niet de markt.** Waardevol als eerste, kleine en goed geteste adapter; ongeschikt als maatstaf voor het aanbod in Jávea.

| Rol | Waarom wel | Waarom niet of nog niet | Bewijs |
|---|---|---|---|
| **Eerste adapter in fase B** (validatiepoort, nulmeting, gebeurtenissen NIEUW / PRIJS GEWIJZIGD / NIET MEER GEVONDEN / BRON NIET BEREIKBAAR) | Draait al, Kyero v3 is de standaard van veel CRM's, klein volume, lage kosten, drie weken importlogboek als testmateriaal | Opslag en historie pas na schriftelijk akkoord; logboek heeft meerdaagse gaten | R05 (3), R16 §6.1 C |
| **Testset voor datakwaliteit** | Bevat alle valkuilen die andere Kyero-feeds ook hebben: vrije tekst in `pool`, valse coördinaten, wisselende refs, HTML | — | R05 (3) |
| **Kwaliteitsreferentie bij deduplicatie met Idealista** | BP-teksten en -referenties zijn op Idealista terug te vinden (La Naya Real Estate publiceert letterlijk "4544JAV" en "4676JAV") | Deduplicatie op prijs en m² alleen is niet sluitend (hetzelfde huis met 269 en 239 m²) | R05-verificatie (3) |
| **Route D en C: relatie in plaats van data** | BP kent de eigenaren; objecten met renovatie- of splitsingspotentieel (bijv. 4544JAV splitsbaar, C3XY4395JAV ex-restaurant) | Verkopend partnerkantoor staat niet in de feed; TREE staat niet op de openbare partnerlijst | R05 (1/3) |
| **Maat voor het aanbod in Jávea** | — | 24 BP-objecten van type Land tegenover 333 terrenos op Idealista, waarvan 238 met label urbano of urbanizable (15-09-2026; R05 vergeleek met die 238, deliverables 01 en 05 gebruiken net als hier 333 als noemer; beide getallen zijn Idealista-tellers, geen bouwrijpheid); 6 van 6 geteste objecten ook elders | R05, R01-verificatie (3/5) |
| **Bron voor bijzondere verkopen** | — | 0 bank- of veilingobjecten; alleen terloopse tekstvermeldingen | R05, R10 (3/4) |
| **Bron voor prijsgeschiedenis** | Kan, als wij snapshots mogen bewaren | BP levert geen historie; Idealista toont prijsdalingen die BP niet heeft (4432JAV: 1.200.000 → 990.000 EUR) | R05-verificatie (3) |

**Voorwaarden voordat BP in Deal Hunter mag:** (1) schriftelijke bevestiging van de doelen, opslag, historie, AI-analyse en beeldvergelijking (vragen in bijlage A, clausule in R16 §6.4); (2) een importpoort die een lege of halve feed nooit als "alles verdwenen" leest; (3) plaatsnaamnormalisatie ("Javea" → Jávea/Xàbia, INE 03082); (4) een tweede `Last-Modified`-meting op een andere dag om de nachtelijke export te bevestigen.

### 2.7 Lokale makelaars, ontwikkelaars en eigen dealflow (masterprompt §9)

**Conclusie: lokale makelaars zijn een dealflowroute, geen databron.** Er is geen kantoor met een open feed, het aanbod is grotendeels gedeeld, en wat eventueel eerder of exclusief beschikbaar is, komt alleen via een persoonlijke samenwerking met schriftelijke afspraken binnen. Details per kantoor: bijlage B-K (tabel K-1); ontwikkelaars: tabel K-2.

**Wat werkelijk is gevonden** (R06 met controledatum 14-09-2026; R06-verificatie 15-09-2026; R07 en R07-verificatie 14-09-2026):

| Onderwerp | Bevinding | Bewijs |
|---|---|---|
| Omvang | 79 kantoren met eigen site of bedrijfsprofiel in tabel K-1 (50 met vestiging in Jávea, 25 erbuiten met Jávea-aanbod, plus Koch & Varlet, Lucas Fox, Six Seconds Properties en Euroholding Dénia); daarnaast 48 namen die alleen uit directories, de gemeentelijke lijst of de BP-partnerlijst bekend zijn. Directories: Trustlocal "95 opciones verificadas" (eigen label, ook kantoren buiten Jávea), Javea Guide 44, gemeentelijke lijst xabia.org 39 bedrijven (makelaars en promotoren door elkaar; de pagina noemt geen totaal) | R06 §2; R06-verificatie R06-02, A11; R07-verificatie R07-07 (1/2/3) |
| Feeds | Geen enkel kantoor publiceert een open XML/JSON-aanbodfeed (R06 §7). Dat is een negatieve bewering zonder lijst van geteste paden, dus niet reproduceerbaar (type 7). Het enige bekende feedbestand is de privé-feed van BP (R2-01). Sitemaps bestaan bij veel sites, maar zijn geen gebruikslicentie; de sitemap-telling van R06 was deels fout (redirects naar foutpagina's als 200 geteld) | R06 §7; R06-verificatie R06-19, F7 |
| Platforms | Dominant is **Sooprema** (CRM; credit of assetpatroon bij onder meer Villadom, Arzuaga, Homes to be Happy, Benimo, Villa Mediterránea, J. Morató, Paradise, Klaus Hildenbrand, Llidomar, AREA, Terramar, Calablanca, Benitachell Properties; waarschijnlijk ook Javea Casas, Selenhome en Villalux). **Paagees** is een web-, beeld- en botcontrolelaag bovenop CRM's (credit bij Montgó Villas, Javea Immo, MG Villas, Bindley, Holidaydream, Inmover). Verder Inmoweb, Mediaelx, Mobilia, Inmobalia, Inmovilla, EasyInmo, eGO Real Estate en WordPress-thema's. Sooprema "publiceert automatisch op +70 portales": dat is een publicatiekoppeling, geen leesroute | R06-verificatie R06-06, A1–A3, F2 (1/3) |
| Gedeeld aanbod | Aantoonbaar gedeeld: BP (listingdienst voor 41 kantoren), Casas Costa Blanca (beelden uit ≥ 9 bronnen, onder meer BP), AR Luxury Living (beelden van BP, Crown en Inmovilla), Xabiacasa ("Member of Inmoweb MLS"), 123 Javea Villas en Casitas Iberica (eigen claims). Het perceel van 1.570 m² en 505.000 EUR in Garroferal del Montgó staat bij zeven kantoren (Atina, Terramar, Arzuaga, Smart Invest, DEGIMOSOL, AR Luxury Living, La Naya), drie met externe referentie "4676JAV" | R06 §5; R06-verificatie R06-08, A7–A9; R07-verificatie R07-08, A3; R05-verificatie R05-03 (1/3/4) |
| Renovatieaanbod | Een echte "te renoveren"-rubriek is bevestigd bij Moraguespons (/venta/villa/javea/a-reformar/, HTTP 200) en Terramar ("totalmente para reformar"); R06 noemde ook Javea Mia ("POTENTIAL") en Plots Direct (niet herverifieerd). **Gecorrigeerd:** Euro Javea en 123 Javea Villas hebben geen renovatierubriek; "Reformas" bij Holidaydream is een dienst van hun bouwtak. Het Idealista-filter heet "Usada / para reformar": van 70 chalets noemen er 51 renovatie in de tekst en 4 zijn nieuwbouw. Koch & Varlet voert nieuwbouw, geen renovatie | R06-verificatie R06-10, R06-11, R06-13, R06-14, R06-15, R06-18, A13 (3) |
| Perceelaanbod | Coldwell Banker Solaris is de grootste zichtbare perceelvoerder op Idealista (11 van 50 "terreno urbano"-advertenties met referentie CBS…). Percelen met project en licentie worden door makelaars verkocht: Luxia (JP144, 1.323 m², 350.000 EUR), InmoVillas Jávea (JP135, 1.123 m², 420.000 EUR), Six Seconds Properties (JA-SO-1001, 192 m², licentie voor 6 woningen, 650.000 EUR), MG Villas en Rimontgó. Geen van zes onderzochte architectenbureaus bemiddelt percelen. Perceelaantallen van Holidaydream (48), Villa Mediterránea (72) en J. Morató (32) gelden voor hun hele werkgebied, niet voor Jávea | R06-verificatie R06-04, R06-14, F10; R07-verificatie R07-14 (1/3) |
| Bank en bijzonder | Bankrubrieken bij Paradise ("Bank repossessed"), 123 Javea Villas ("Bank Repossessions") en Benitachell Properties; het filter "Property of financial institution" bij Randof, Javea Continental en Xabiacasa zit in het standaard Inmoweb-sjabloon. Inhoud nergens gecontroleerd; geen signaal voor bankvoorraad (Idealista: 0 bankwoningen in Jávea) | R06-verificatie R06-07, R06-12, R06-13, F5 (3) |
| Delen vóór publicatie | Bij geen enkel kantoor vastgesteld: ONBEKEND. Alleen MLS Dénia en MLS 03724 delen exclusief aanbod onder leden. "Secret Sales" (Euro Javea) en "WhatsApp VIP off-market" (InmoVillas) zijn aanbiedersclaims | R07 §1.4, §1.7; R06 §5 (1/7) |
| Ontwikkelaars | Zeven partijen met bevestigde Jávea-projecten (tabel K-2). Stilgevallen projecten zijn op portalen niet te vinden (66 obra-nueva-chalets, 0 met "paralizado", "sin terminar" of "obra parada"); de route loopt via architecten, BOP-publicaties, veilingen en fysieke waarneming (type 4) | R07-verificatie R07-09 t/m R07-13 (1/3) |
| Netwerken en register | Bemiddeling in de Comunitat Valenciana vraagt inschrijving in het RAICV (grondslag Ley 2/2017 DA 6ª; uitwerking Decreto 98/2022; verplicht sinds 16-10-2022). COAPI Alicante (APIRed: openbare zoekfunctie, ledendeel voor colegiados), ASICVAL ("400 agencias asociadas", "exclusiva compartida"), MLS Dénia (20 kantoren volgens eigen site) en MLS 03724. In Jávea zelf is geen eigen MLS gevonden | R07-verificatie R07-01 t/m R07-06, R07-20 (1/2) |

**Dealflow-aanpak (concept uit R07 §5; niets verzonden, bedragen zijn werkhypothesen tot Jan ze bevestigt).**

| Onderdeel | Voorstel | Bron |
|---|---|---|
| Zoekprofiel | Werkgebied Jávea/Xàbia plus Benitatxell, Dénia, Gata de Gorgos en Teulada-Moraira. Categorie 1: bestaand vastgoed met renovatiepotentieel (vraagprijs 250.000–900.000 EUR). Categorie 2: percelen en ontwikkelobjecten (villapercelen 150.000–800.000 EUR; meergezinssolares per geval; licentiestatus concedida / vigente / en trámite apart vastleggen). Categorie 3: bijzondere verkopen (geen ondergrens; boven 1.500.000 EUR alleen met investeerder). Niet: afgebouwde nieuwbouw zonder korting, huurobjecten, objecten zonder duidelijke titel of van aanbieders buiten het RAICV | R07 §5.1 (4, werkhypothese) |
| Aanleverformulier | Webformulier in GoHighLevel (CRM van waarheid, ADR-0014) plus pdf; 24 velden in vier blokken: partner (bedrijf, contact, RAICV- of colegiado-nummer of CIF, rol, mandaat), object (categorie, zone, adres of referencia catastral, staat, m² met bron, prijs, planologische klasse en licentiestatus, "al gepubliceerd?" voor ontdubbeling), documenten (verplicht vóór een bod) en afspraken (vergoeding, rechtstreeks contact met verkoper, geheimhouding, bevestiging te goeder trouw, uitdrukkelijke toestemming voor e-mail en telefoon) | R07 §5.2 (4) |
| Opvolgprocedure | Ontvangst en ontdubbelcontrole binnen 1 werkdag; eerste oordeel binnen 5 (Jan en bouwkundige); besluit over bezichtiging of bod binnen 10, met reden bij afwijzing; verdieping na bezichtiging; bod alleen na akkoord van Jan en via de partner; terugkoppeling elke 2 weken zolang het dossier open is. Per partner bijhouden: aangeleverd, bezichtigd, geboden, gekocht, reactietijd TREE | R07 §5.3 (4) |
| Geheimhouding en vergoeding | Het object blijft van de partner; TREE benadert de verkoper niet buiten de partner om; korte geheimhoudingsafspraak (tekst door advocaat). Listing agent met mandaat houdt de eigen commissie. Finder's fee voor introducers zonder mandaat: bedrag ONBEKEND (besluit Jan), alleen aan partijen die het rechtmatig mogen ontvangen; of een introducer zelf onder de registerplicht valt, is [te verifiëren] (R07-verificatie A2). Alles schriftelijk vóór de bezichtiging; geen exclusiviteit of commissierecht veronderstellen | R07 §5.3; masterprompt §9 |
| Volgorde van benaderen | 1) kantoren die nu percelen met project verkopen (Luxia, InmoVillas Jávea, Six Seconds, MG Villas, Rimontgó); 2) kantoren met lokaal, niet-gedeeld aanbod, pas na een ontdubbelmeting; 3) MLS Dénia en MLS 03724 (eis: RAICV van TREE Properties); 4) ontwikkelaars (tabel K-2), ook voor route C; 5) architecten, partnerlijn "proyecto sin cliente" | R07 §5.3 (4) |
| Kanaal | Eerste contact telefonisch, persoonlijk of via het contactformulier van het kantoor; e-mail of WhatsApp pas na uitdrukkelijke instemming en altijd met afmeldmogelijkheid (LSSI art. 21; AEPD-informe 2018-0164). Zakelijke contactgegevens van kantoren mogen worden bewaard (LOPDGDD art. 19). Of een eerste zakelijke e-mail aan een kantoor onder art. 21 valt, is [te verifiëren] bij de advocaat. Geen massabenadering van particulieren | R07 §4.2 en verificatie R07-15 t/m R07-17 (2/4) |
| Conceptberichten | Spaanse en Engelse teksten voor makelaars, architecten en ontwikkelaars staan in R07 §5.4 (niet verzenden). Vóór gebruik door Jan te bevestigen: het jaartal ("desde 2022"; 2022 of 2023 is een open beslissing), de merkclaims "equipo de obra propio" en "cocinas y baños bajo el mismo techo", het RAICV-nummer en de prijsklassen | R07-verificatie F2 |

**Wat dit betekent voor Deal Hunter (type 4).** Een makelaarsadapter hoort niet in de eerste bouwfase zolang geen kantoor schriftelijk een export levert (sjabloon R16 §6.3; CRM-exportfuncties in R2-29). Aanleveringen komen binnen als dossier in GoHighLevel. Het register van kantoren is een momentopname: de platformindeling bleek bij controle voor een groot deel fout en sitemaps en zonetellingen waren niet reproduceerbaar (R06-verificatie F2, F7, F8). Elke kantoorregel dus opnieuw bekijken vóór een eerste gesprek.

## 3. Aannames en onzekerheden

| # | Aanname of onzekerheid | Gevolg als het anders blijkt | Type |
|---|---|---|---|
| 1 | BP maakt de exports elke nacht; gemeten is één nachtvenster op twee tijdstippen van dezelfde dag | Andere ophaalfrequentie en vertraging | 4 |
| 2 | De rechten op de BP-feed reiken nu niet verder dan de website | Als er toch een afspraak bestaat (mail, WhatsApp, mondeling), kan een deel van de vragen vervallen | 7 |
| 3 | Gepland gebruik van de Idealista-assistent valt onder "monitorizar" en "guardar" in de voorwaarden | Als Idealista het toestaat, wordt de assistent de goedkoopste brede bron voor Jávea | 4 [advocaat] |
| 4 | Portaalvoorwaarden binden ook een niet-geregistreerde bezoeker (browsewrap) | Naar Spaans recht niet uitgemaakt; verandert de handmatige route niet, wel het risicoprofiel | 7 [advocaat] |
| 5 | Portalen krijgen hun aanbod grotendeels via dezelfde makelaarsfeeds, dus weinig uniek aanbod per portaal | Een meting kan tot een andere keuze voor betaalde bron leiden | 4 |
| 6 | Tellingen zijn momentopnames; Idealista-tellers verschuiven dagelijks (chalets 1.275 op 14-09, 1.273 op 15-09) | Altijd met datum rapporteren | 3 |
| 7 | Verwerking van eigen alertmails (link, ID, prijs) is mogelijk toegestaan, maar geen enkel portaal regelt het | Tot advies: alerts door een mens laten beoordelen | 7 [advocaat] |
| 8 | Voor DataVenues, Casafari, idealista/data en de Search API zijn prijs, velden en licentie volledig ONBEKEND | Architectuur niet rond deze bronnen ontwerpen tot de offerte binnen is (§6) | 7 |
| 9 | De vrije Catastro-webservices vallen niet onder het verbod op automatisch gebruik van "servicios interactivos" | Bij twijfel schriftelijk bevestigen bij de DG del Catastro vóór opschaling | 4 |
| 10 | Het lidmaatschap van TREE Properties bij MLS-netwerken, het Colegio of Fotocasa Pro is niet bekend | Mogelijk is een route al beschikbaar zonder nieuwe kosten | 7 |
| 11 | "Uniek of gedeeld aanbod" per kantoor is niet gemeten; de indeling in tabel K-1 volgt uit platform, omvang, beeldbronnen en eigen claims | Een ontdubbelmeting kan de volgorde van benaderen omgooien | 4 |
| 12 | Of TREE Properties in het RAICV staat, is ONBEKEND (het openbare register laadt alleen via JavaScript en is niet gecontroleerd) | Zonder inschrijving geen MLS-lidmaatschap, geen nummer in partnerberichten en mogelijk geen bemiddelingsvergoeding | 7 |
| 13 | Kantoren willen objecten vóór brede publicatie delen met een koper-partner | Nergens bevestigd; alleen de twee MLS-verenigingen delen onder leden. Als het tegenvalt, blijft R2-52 vooral een kanaal voor gedeeld aanbod en tips van ontwikkelaars en architecten | 4 |
| 14 | Het zichtbare platform (credit, assetpad, botcontrole) wijst het CRM van een kantoor aan | Paagees werkt bovenop meerdere CRM's; exportmogelijkheden per kantoor pas vast te stellen in een gesprek | 4 |

## 4. Tegenargumenten en aandachtspunten

- **"Handmatig is te traag."** Klopt voor volledige dekking. Maar in Jávea zijn de bijzondere verkopen nu dun (0 veilingen, 0 bankwoningen, 2 Sareb-percelen, waarvan één ook op Idealista). Een wekelijkse, deels handmatige ronde met alerts levert voor dat segment bijna hetzelfde op als een dagelijkse crawler, zonder juridisch risico (R10 §8, type 4/5).
- **"De Idealista-assistent is door Idealista zelf aangeboden, dus systematisch gebruik is prima."** Het is een sterker argument dan bij scraping, maar de tool is consumentgericht (utm_project=leadGeneration, 8–15 resultaten aanbevolen) en de voorwaarden verbieden commercieel monitoren en opslaan. Een schriftelijke vraag kost weinig en haalt het risico weg (R01, R16).
- **"Een betaalde licentie lost alles op."** Niet vanzelf. De algemene voorwaarden van DataVenues beperken gebruik tot "sus propias necesidades" en verbieden "explotación comercial"; die van Casafari verbieden systematisch verzamelen en afgeleide werken. Opslag, AI-analyse, dossiers voor klanten en beeldvergelijking moeten expliciet in het contract staan (R02-verificatie, R04).
- **"BP is gratis en draait al."** Ja, maar de dekking is klein en BP-objecten staan toch al op Idealista. De waarde zit in de testbare keten en de relatie, niet in het aanbod.
- **"Open overheidsdata is vrij, dus daar begint de bouw."** Terecht voor veilingen en percelen, maar het levert geen renovatiewoningen of reguliere percelen op. Het is context en een trigger, geen dealflow op zich.
- **Persoonsgegevens:** pisos.com publiceert naam en telefoon van particulieren automatisch; tablón-edictos van Xàbia bevatten NIF's; NPL-fiches zijn herleidbaar tot schuldenaars. Deal Hunter slaat objecten op, geen personen (R16 §4).
- **"Makelaars mailen levert snel dealflow op."** Niet vanzelf. Het aanbod van de meeste kantoren is gedeeld (hetzelfde perceel bij zeven kantoren), bereidheid om vóór publicatie te delen is nergens vastgesteld, en ongevraagde elektronische reclame is verboden zonder uitdrukkelijke toestemming (LSSI art. 21; of dat ook voor een eerste zakelijke e-mail aan een kantoor geldt: [te verifiëren]). Eerste contact dus persoonlijk of telefonisch, één op één, met een helder zoekprofiel (R07 §4.2, §5; R07-verificatie R07-08, R07-15).
- **Veranderend landschap:** Scout24 consolideert Fotocasa en Habitaclia sinds maart 2026 (Scout24-bericht van 06-08-2026, https://www.scout24.com/en/investor-relations/financial-news/ir-news/detail/scout24-maintains-strong-momentum-in-q2-with-20-revenue-growth-double-digit-organic-revenue-growth-and-18-adjusted-eps-growth, 15-09-2026, type 2). Idealista meldde op 05-12-2024 de overname van Kyero (https://www.idealista.com/en/news/property-for-sale-in-spain/2024/12/05/821343-idealista-acquires-kyero, 15-09-2026, type 1). Vocento verkocht HabitatSoft, de uitgever van pisos.com, op 18-03-2025 aan Immobiliare.it (pers over een CNMV-melding, https://www.servimedia.es/noticias/vocento-vende-habitat-soft-inmobiliarieit-22-5-millones-euros/1411519299, 15-09-2026, type 1; de melding zelf niet ingezien). Intrum voegde Haya in december 2024 samen met Solvia (https://www.idealista.com/news/inmobiliario/empresas/2024/12/16/824621-intrum-fusiona-sus-servicers-inmobiliarios-para-simplificar-su-estructura-en-espana, 15-09-2026, type 1; haya.es gaf HTTP 522). Voor Servihabitat is een akkoord over verkoop aan Hipoges en Finsolutia gemeld, maar de pers spreekt elkaar tegen over de afronding: **[te verifiëren]**, type 7 (R10-verificatie R10-13). Contactroutes en voorwaarden kunnen binnen maanden wijzigen; register elk kwartaal herverifiëren (R02, R03, R10).

## 5. Concrete vervolgstap

1. **Deze week (Jan):** bijlage A nalezen, contactpersoon invullen en versturen; tegelijk nagaan wat destijds met BP is afgesproken.
2. **Deze week (Jan):** Idealista schriftelijk vragen naar gepland gebruik van de assistent (tekstvoorstel op verzoek); beslissen of het Search API-formulier wordt ingevuld.
3. **Binnen twee weken (Jan):** offertes met één vaste vragenlijst (dekking Marina Alta, velden, verversing, opslag, AI-analyse, afgeleide data en beeldvergelijking, prijs met en zonder btw) bij DataVenues, idealista/data, Casafari en Accumin.
4. **Binnen twee weken (Jan):** het RAICV-nummer van TREE Properties opzoeken; zoekprofiel, prijsklassen, vergoedingsbeleid en de eigenaar van de termijnen uit §2.7 vastleggen; daarna, na akkoord, de eerste gesprekken met de vijf kantoren die nu percelen met project verkopen. Niets verzenden of toezeggen zonder akkoord van Jan.
5. **Voor de bouw van fase B (Claude, na akkoord):** alleen adapters zonder rechtenrisico uitwerken — BOE-sumario, AEAT-lijst, Catastro — en de BP-adapter pas na de bevestiging van BP. Het register blijft poortwachter: een adapter draait niet zolang de rechtenvelden ONBEKEND zijn (R16 §6.5).

## 6. ⏸️ ACTIE VOOR JAN

**A. Aanvragen en toestemmingen**

| # | Actie | Waarom | Bron |
|---|---|---|---|
| 1 | Mail aan Background Properties versturen (bijlage A); conceptclausule R16 §6.4 laten toetsen en daarna voorleggen | Zonder schriftelijk akkoord geen opslag, historie, AI-analyse of beeldvergelijking | R05 §6.4, R16 §6.4 |
| 2 | Idealista schriftelijk vragen of gepland gebruik van de assistent (dagelijks, opslag van link, code en prijs) is toegestaan | Voorwaarden regelen dit niet; algemene clausules verbieden monitoren | R01, R16 |
| 3 | Besluiten over het Search API-formulier (https://developers.idealista.com/access-request) | Enige officiële route naar portaalaanbod per API | R01 |
| 4 | Account aanmaken op subastas.boe.es (alleen natuurlijke persoon) en maximaal 50 zoekalerts instellen (provincie Alicante; Xàbia, Jávea, Javea, Dénia, Benitachell, Teulada, Benissa, Calp) | Enige manier om veilingen op plaats te vinden zonder crawlen | R08 |
| 5 | Accounts en alerts bij Servihabitat (particulier en Profesionales, op bedrijfsnaam), Solvia, Diglo en Aliseda; portaalalerts bij Idealista, Fotocasa, pisos.com, thinkSPAIN en SpainHouses | Toegestane leesroute; wij mogen geen accounts aanmaken | R01, R02, R03, R10 |
| 6 | Voorwaarden handmatig in de browser openen en als pdf bewaren in `deal-hunter/onderzoek/bronnen/`: fotocasa.es/es/aviso-legal/ln, milanuncios.com/legal/condiciones-uso, kyero.com/en/docs/terms/, indomio.es/en/terms/, idealista.com/ayuda/articulos/legal-statement/ | Machinaal niet leesbaar (JavaScript of 403) | R02, R03, R16 |
| 7 | Spaanse advocaat de twaalf vragen uit R16 §7 laten beantwoorden (voorrang: 3 assistent, 4 alertmails, 6 beeldhashes, 12 BP-clausule), plus de twee LSSI-vragen uit R07 §7 (eerste zakelijke e-mail aan een kantoor; brief per post aan een particuliere eigenaar) | Vóór de bouw van onderdelen die portaal- of BP-inhoud opslaan of analyseren, of persoonsgegevens uit veilingstukken koppelen (vragen 3, 4, 6, 7, 10, 11, 12). Adapters op open overheidsdata zonder persoonsgegevens (BOE-sumario, AEAT-lijst, Catastro) hoeven daar niet op te wachten (§5 stap 5). Zo past dit bij de bouwvolgorde van deliverable 05, zolang B0 en B1 geen persoonsgegevens uit veilingstukken opslaan | R16 §6.5, §7; R07 §7 |
| 8 | Optioneel: AEBOE vragen om gerichte automatische raadpleging van één detailpagina per nieuw SUB-id | robots.txt verbiedt alle bots | R08 |

**B. Vragen aan Background Properties** (volledige lijst R05 §6.3; alle twaalf staan in de conceptmail van bijlage A)

1. Schriftelijke bevestiging van de doelen: website, intern aanbodbeheer, acquisitieanalyse.
2. Opslag en historie (prijs, beschikbaarheid, eerste en laatste vermelding), ook na verdwijnen uit de feed; hoe lang.
3. AI-analyse van teksten en kenmerken.
4. Foto's onderling en met andere bronnen vergelijken en hashes bewaren.
5. Tonen aan derden: koper- of investeerdersdossier, ander groepsmerk.
6. Hotlinken of kopiëren van foto's; stabiliteit van foto-URL's; wie het auteursrecht heeft.
7. Frequentie en tijdstip van de export; is vaker of een wijzigingsmelding mogelijk?
8. Betekenis van `date`; waarom wijken 39 refs af van de URL; wat betekenen C3XY en C4XY?
9. Status of lijst van verkochte en ingetrokken objecten.
10. Extra velden: oriëntatie, afstand tot zee, terrein, bouwjaar, kadastrale referentie; `pool` en energielabel in Kyero-notatie.
11. Is de sleutel gebonden aan TREE of aan de website; melding bij vervanging; testsleutel.
12. Wie is het aanspreekpunt voor techniek en voor zakelijke afspraken? En staat TREE bewust niet op de partnerlijst?

**C. Offertes en lidmaatschappen**

| # | Partij | Wat opvragen | Contactroute |
|---|---|---|---|
| 1 | DataVenues (Fotocasa Group) | API en data-feed: velden, verversing, dekking Marina Alta, prijs, condiciones particulares voor opslag, AI-analyse en dossiers; rechtsgrond eigenaarscontacten; zijn notariële sluitprijzen live | Formulier pro.fotocasa.es of commercial Fotocasa/Habitaclia; support@datavenues.com |
| 2 | idealista/data | Comparables- en prijshistorie-API voor Jávea/Marina Alta; licentie | Formulier op https://www.idealista.com/data/ |
| 3 | Casafari | Aantal objecten en bronnen in Jávea, verversing, Spaanse sluitprijzen, API-licentie voor opslag, AI en beeldvergelijking, prijs en looptijd (12 maanden, automatische verlenging) | commercial@casafari.com |
| 4 | Accumin (uDA, Tinsa Digital AVM) | Eén offerte voor AVM en comparables voor Marina Alta | intelligence@accumin.com |
| 5 | Brainsre (alternatief) | Prijzen en dekking | sales@brainsre.com |
| 6 | Fotocasa Pro | Heeft TREE Properties al een pack (Basic: DataVenues "Valoración"; Premium: "Lite" + captación de particulares)? | Eigen accountmanager |
| 7 | Resales-Online, MLS 03724, MLS Dénia, ASICVAL, Colegio API Alicante (APIred) | Is TREE lid; zo nee: kosten, voorwaarden, toetredingseisen (RAICV) en toestemming voor intern analytisch gebruik van netwerkobjecten | support.resales-online.com; info@mls03724.com; info@mlsdenia.com; asicval.es; coapi@apialicante.com |
| 8 | Servihabitat, Solvia, Aliseda | Voorwaarden om samenwerkend makelaar (API colaborador) te worden voor Marina Alta | Na akkoord Jan, via de portalen |

**D. Besluiten over techniek (raakt draaiende diensten of installaties)**

- Mag de properties-api (poort 3100) een krimpbescherming, DNS-wachtlus en tijdstempels in de log krijgen? Het is een productiedienst; alleen na overleg.
- Akkoord voor een XLS-lezer in de Hermes-venv voor de MIVAU-gemeentebestanden, of handmatig per kwartaal omzetten?

**E. Makelaars, ontwikkelaars en dealflow** (R07 §7, met correcties uit de R07-verificatie)

| # | Actie of besluit | Waarom | Bron |
|---|---|---|---|
| 1 | Nagaan of TREE Properties in het RAICV staat en met welk nummer (openbaar register via habitatge.gva.es, handmatig in de browser) | Verplicht voor bemiddeling (Ley 2/2017 DA 6ª); eis voor MLS-lidmaatschap; hoort in elk partnerbericht | R07 §1.1; R07-verificatie R07-20 |
| 2 | Besluiten of TREE lid wil worden van MLS Dénia en/of MLS 03724 | Gedeeld exclusief aanbod, maar ook de plicht eigen exclusieven te delen | R07 §1.4, §7 |
| 3 | Prijsklassen in het zoekprofiel bevestigen of wijzigen (250.000–900.000 EUR woningen; 150.000–800.000 EUR percelen) | Werkhypothese; pas daarna in teksten | R07 §5.1 |
| 4 | Vergoedingsbeleid voor introducers zonder mandaat (finder's fee ja/nee, hoogte) | Zonder besluit blijft die regel leeg | R07 §5.3 |
| 5 | Eén eigenaar aanwijzen voor de termijnen van 1, 5 en 10 werkdagen en de tweewekelijkse terugkoppeling | Zonder eigenaar sterft de procedure | R07 §7 |
| 6 | Jaartal (2022 of 2023), merkclaims en aanspreekvorm (tú of usted) in de conceptberichten vaststellen | Staat nu als open beslissing in de groepsnotities | R07 §7; R07-verificatie F2 |

---

## Bijlage A — Conceptmail aan Background Properties (NIET VERZENDEN)

> Gebaseerd op R05 §6.4 (`onderzoek/R05-background-properties.md`) en aangevuld met de vragen uit R05 §6.3 die daar ontbraken: doelen, bewaartermijn, fotorechten, afwijkende referenties (C3XY/C4XY) en aanspreekpunt met partnerlijst. Alle twaalf vragen uit §6-B staan er nu in. ⏸️ ACTIE VOOR JAN: nalezen, de velden tussen [haken] invullen en zelf versturen. Het aantal objecten op de verzenddag invullen (op 15-09-2026 om 04:46 CEST: 224, lokale API, type 3). Er staan geen sleutels of feed-URL's in.

> **Onderwerp:** Onze koppeling op jullie Kyero-feed: een paar vragen over gebruik en verversing
>
> Beste [naam],
>
> Sinds augustus draait treeproperties.es op jullie Kyero-feed (export 36 plus de commissie-exports 26 en 27): volgens planning halen we het bestand elke twee uur op, [aantal] objecten op dit moment. Omdat we de gegevens breder willen gaan gebruiken dan alleen de site, wil ik een paar dingen zwart op wit hebben voordat we verder bouwen.
>
> **Gebruik**
>
> 1. Kun je bevestigen voor welke doelen we de exports mogen gebruiken: de website, ons interne aanbodbeheer en onze eigen acquisitieanalyse?
> 2. Mogen we de feed opslaan en de historie bewaren (prijs, beschikbaarheid, datum van eerste en laatste vermelding), ook van objecten die niet meer in de feed staan? Zo ja, hoe lang?
> 3. Mogen we teksten en kenmerken met AI laten analyseren voor eigen selectie, waardering en dossiers?
> 4. Mogen we foto's onderling en met foto's uit andere bronnen vergelijken om dubbele advertenties te herkennen, en daarvan beeldkenmerken (hashes) bewaren?
> 5. Wat mogen we tonen aan derden: alleen op treeproperties.es, of ook in een dossier voor een koper of investeerder, in een intern rapport of via een ander merk van de groep?
> 6. Mogen foto's rechtstreeks vanaf jullie server geladen worden, of moeten we ze kopiëren? Zijn de foto-URL's stabiel, en wie heeft het auteursrecht op foto's en teksten?
>
> **Techniek**
>
> 7. Hoe vaak en hoe laat wordt de export aangemaakt? In onze meting van 14 september waren alle zes bestanden in één nachtelijk venster gemaakt, tussen 01.30 en 03.00 uur. Gebeurt dat elke nacht, en is vaker of een melding bij wijziging mogelijk?
> 8. Wat betekent het veld `date` precies: laatste wijziging of eerste publicatie, en wordt het bij een prijswijziging bijgewerkt? Waarom wijkt bij 39 objecten de referentie af van de URL, en wat betekenen de voorvoegsels C3XY en C4XY?
> 9. Verkochte of ingetrokken objecten verdwijnen nu gewoon uit het bestand. Kunnen jullie een status of verkoopdatum meegeven, of een aparte lijst van ingetrokken referenties?
> 10. Op jullie objectpagina staan velden die niet in de export zitten: oriëntatie, afstand tot zee, terrein. Kunnen die erin, net als bouwjaar en kadastrale referentie als jullie die hebben? En kunnen `pool` en `energy_rating` in de Kyero-notatie?
> 11. Is de sleutel gebonden aan TREE of aan de website, en horen we het als hij wordt vervangen? Een tweede sleutel voor een testomgeving zou ons helpen.
>
> **Contact**
>
> 12. Wie is bij jullie het aanspreekpunt voor de techniek, en wie voor de zakelijke afspraken? En staat TREE Properties bewust niet op jullie partnerlijst?
>
> [Keuze Jan, na advies van de advocaat: "Een schriftelijke bevestiging per punt helpt ons verder." óf "De antwoorden leggen we daarna graag vast in een korte bijlage bij onze samenwerking."] Wil je liever bellen, dan schikt [dag en tijdstip, in te vullen door Jan].
>
> Groet,
> Jan

**Kanttekeningen.**

1. **Bevestiging of addendum (R16 §6.4, type 4 [advocaat]).** R05 stelde voor dat een korte schriftelijke bevestiging per punt volstaat. Volgens R16 is een e-mail waarin BP de punten uitdrukkelijk aanvaardt beter dan niets, maar een ondertekend addendum sterker, vooral voor de garantie op fotorechten en voor wat na beëindiging mag blijven. De mail kiest daarom niet; Jan kiest na advies. De Spaanse conceptclausule staat in `onderzoek/R16-rechten-en-compliance.md` §6.4.
2. **Nachtvenster (type 3 voor de meting, type 4 voor "elke nacht").** Twee metingen op 14-09-2026 (21:08 en 21:41 UTC) toonden dezelfde zes bestanden, aangemaakt tussen 01:34 en 02:55 CEST. Dat BP dit elke nacht doet, is niet vastgesteld (R05-verificatie R05-05). De mail vraagt het daarom, in plaats van het te beweren.
3. **Geschrapt uit de eerdere versie:** "en dat werkt goed" (de properties-api viel 184 keer naar 0 objecten en de site-import draaide meerdaagse periodes niet, R05-verificatie), "daar hoeft geen contract van te komen" (strijdig met punt 1) en "dan schikt donderdag of vrijdag" (beschikbaarheid van Jan niet bekend). Het vaste getal "225 objecten" is vervangen door een invulveld.

---

## Bijlage B — Bronnenregister: alle velden uit masterprompt §7 per bron

Gegenereerd uit `bronnenregister.json` (zelfde inhoud). Nummering R2-01 t/m R2-75 gelijk aan §2.1; R2-60 t/m R2-75 staan in blok L. De tabellen K-1 (kantoren) en K-2 (ontwikkelaars) staan alleen in dit document. De rechtenvlaggen staan niet per blok, maar in één overzichtstabel aan het eind van deze bijlage ("Rechtenvlaggen per bron"); onderbouwing, bewijstypen en bron-URL's per regel staan alleen in het JSON-bestand. "ONBEKEND" betekent: in geen enkele bron gevonden. Controledatum per bron in de rij "Laatste verificatie".

#### A. Werkende bronnen: partnerfeed en officiële assistent

Bron voor de invulling: R05, R01, R16. Bewijstype staat tussen haken in de cellen (1–7, masterprompt §5).

| Veld | R2-01 Background Properties — Kyero v3 XML-feed (partnerfeed) | R2-02 Idealista-assistent (officiële MCP/ChatGPT-app van Idealista) |
|---|---|---|
| Naam en officiële website | https://backgroundproperties.com | https://www.idealista.com/en/news/property-for-sale-in-spain/2026/03/13/887103-idealista-launches-its-app-on-chatgpt |
| Type aanbieder | Listingdienst met partnernetwerk (geen makelaar, geen marktaggregator); eenmanszaak in Jávea, handelsnaam sinds 2017 (type 1) | Officiële, consumentgerichte AI-zoekassistent van het portaal; in deze Claude-sessie als MCP aangesloten (search_properties, property_detail, get_howto, guide) (type 2/3) |
| Geografische en inhoudelijke dekking | Costa Blanca Noord (Marina Alta + deel Marina Baixa), alleen koop. 15-09-2026 03:56 lokale API: 224 objecten, 56 met town 'Javea' (26 villa, 24 perceel, 4 appartement, 2 zonder type), 27 vanaf 750.000 EUR (type 3). 41 partnerkantoren ES/BE/DE, TREE staat niet op de openbare lijst (R05-verificatie, type 3) | Heel het Idealista-aanbod Spanje. Jávea 15-09-2026: 1.273 casas/chalets (70 para reformar), 569 pisos (19 para reformar), 333 terrenos (238 met label urbano/urbanizable — niet 'bouwrijp'), 77 obra nueva, 0 'de bancos' woningen, 1 bankperceel; 4 chalets in laatste 48 uur (R01-verificatie, R10, type 3) |
| Technische toegang | WordPress-export (vermoedelijk WP All Export op Houzez, type 4): export-URL met geheime sleutel geeft HTTP 302 naar statisch XML-bestand. TREE: export_id 26, 27, 29, 30, 31, 32 (properties-api, elk uur) en 36 (site-import, elke 2 uur). Standaard curl-User-Agent krijgt 403, verzoek zonder User-Agent 302/200 (type 3). Plaatsnaam 'Javea' zonder accent: filter op Jávea/Xàbia geeft 0 (type 3, 15-09-2026) | Tool-aanroep binnen een Claude-sessie; maxResults 1–50, geen offset en geen sorteerparameter; filters worden uit tekst afgeleid. 'Bajada de precio' wordt sortering rebajas-desc, geen filter; type- en 'de bancos'-filter kunnen stil vervallen — altijd veld summary controleren; bij buurgemeenten soms verkeerde locatie (R01, R10, type 3) |
| Beschikbare velden | id (stabiel, vermoedelijk WordPress-post-id), ref (wijkt bij 39/225 af van URL-slug), date, price, currency, price_freq, type, new_build, town, postcode (67/225), province, country, location_detail, lat/long (11 objecten op Miami-standaardpunt), beds, baths, pool (vrije tekst, 223/225), surface_area built/plot (definitie onbekend), energy_rating (deels vrije tekst), url (alleen en), desc per taal (met HTML), features, images. Geen status, catastral, bouwjaar, staat, verkopende makelaar (R05, type 3) | search: propertyCode, url (utm-parameters), price, priceDropInfo (genest in priceInfo.price), size, rooms, bathrooms, lat/long (benaderend), showAddress, detailedType, description, features (o.a. hasSwimmingPool), status, contactInfo (userType, phone1 — aard nummer [te verifiëren]), total, summary. detail: commercialName, externalReference, micrositeUrl, energyCertification, 'Construido en', modificationDateText, characteristicsDescriptions, alle foto's met tag; outcome 'not_found' bij onbestaande code (type 3) |
| Foto's en documenten | Foto's: 2–130 per object (mediaan 23) op BP-server; geen plattegrond-tag, geen documenten, geen video (type 3) | Search: vervaagde lage-resolutie afbeelding; detail: fotolijst met tags. Geen documenten, geen kadastrale referentie (type 3) |
| Publicatie- en wijzigingsinformatie | Alleen date (volgens Kyero 'last modified'; betekenis bij BP niet bevestigd). Geen publicatiedatum; source_published_at = ONBEKEND (R05, type 3/7) | Geen publicatiedatum; alleen grove tekst 'Anuncio actualizado hace …' en filter 'últimas 48 horas' (type 3) |
| Historische gegevens | Geen. Volledige momentopname; verdwijnen = NIET MEER GEVONDEN, nooit 'verkocht'. Prijshistorie alleen zelf op te bouwen (na toestemming) | Alleen laatste prijsdaling (formerPrice, percentage); geen volledige prijshistorie |
| Verversingsfrequentie | Alle zes exportbestanden in één nachtvenster aangemaakt (01:34–02:55 CEST, twee metingen op 14-09-2026); 'elke nacht' is gevolgtrekking (type 4). Wij halen elk uur/2 uur op; vertraging tot ca. 26 uur (type 5) | Live stand van het portaal op het moment van de aanroep (tellers wijzigen dagelijks, type 3/4) |
| Rate limits | Niet gepubliceerd. Zes verzoeken per uur worden sinds april bediend; ook een herstartlus van ruim 800 verzoeken gaf geen blokkade (type 3). Bronuitval komt voor: 184 nulrondes (DNS), incidentele HTTP 500 | Niet gepubliceerd; 50 resultaten per aanroep; tool beveelt 8–15 resultaten aan (type 1) |
| Kosten | Geen feedkosten bekend; commissiemodel bij verkoop via partner (type 1) | Gratis voor gebruiker (Idealista: 'free idealista app', type 1) |
| Contractstatus | Geen schriftelijke feedafspraak gevonden; URL's feitelijk verstrekt voor de website. Aviso legal van de site eist 'autorización escrita previa' voor reproductie en gebruik (type 2; sjabloontekst voor de website, beperkte bewijskracht voor de feed) | Geen. Geen aparte voorwaarden voor app/MCP gevonden. Algemene voorwaarden (versies 20-11-2020 en 17-02-2024) verbieden robots/monitoren/'guardar' voor commerciële activiteit zonder schriftelijke toestemming; versie 17-02-2024 staat 'guardar búsquedas y favoritos' toe; actuele versie (30-04-2025) gaf 403 (R01-verificatie, type 2/7) |
| Toegestane gebruiksdoelen | Feitelijk: tonen op treeproperties.es. Alle andere doelen (acquisitieanalyse, klantdossiers, groepsentiteiten) ONBEKEND | Verdedigbaar: ad-hoczoeken, samenvatten en vergelijken door een medewerker in de sessie; link + propertyCode + eigen oordeel bewaren (R16 §6.1 B, type 4). Gepland/systematisch gebruik: ONBEKEND |
| Rechten AI-analyse | ONBEKEND — schriftelijk vragen (R05 vraag 3; conceptclausule R16 §6.4 art. 4) | In de sessie: ja (door de aanbieder bedoeld gebruik). Buiten de sessie: ONBEKEND — toestemming nodig |
| Opslag en bewaren | ONBEKEND — opslag en historie pas na schriftelijke bevestiging (R16 §6.1 C) | Opslag van resultaten en prijsdalingshistorie: niet toegestaan zonder schriftelijke toestemming (voorwaarden §8.1 'guardar', type 2/4) |
| Afgeleide gegevens en beeldvergelijking | ONBEKEND — beeldhashes en vergelijking met andere bronnen pas na akkoord; hotlinken mogelijk strijdig met verbod op direct doorlinken (aviso legal) [advocaat/BP vragen] | Geen foto-download of dHash (TRLPI art. 18/128; robots.txt sluit /inmueble*/foto uit); geen dossiers met foto's/teksten naar klanten; ook links naar inhoud vragen volgens de voorwaarden (2020) toestemming [advocaat] |
| Contactpersoon of aanvraagroute | hola@backgroundproperties.com (zakelijk); conceptmail in bijlage A (niet verzonden). Telefoonnummer bewust weggelaten: BP is een eenmanszaak en het mobiele nummer is herleidbaar tot een natuurlijk persoon | Geen specifieke route voor de assistent gevonden; schriftelijk via Idealista S.A.U. (zakelijke contactroute via developers.idealista.com-formulier of idealista/data-contactformulier) |
| Laatste verificatie | 15-09-2026 (lokale API); feedtechniek en voorwaarden 14-09-2026 | 15-09-2026 |
| Openstaande vragen | 12 vragen R05 §6.3: rechten opslag/AI/hashes/derden, hotlinken, exportfrequentie, betekenis date en refs, status/verkocht, extra velden (catastral, bouwjaar), sleutelbinding, contactpersoon. Tweede Last-Modified-meting op andere dag nodig | Is dagelijks gepland gebruik met opslag van link/code/prijs toegestaan? Wat geeft property_detail bij een verkochte of ingetrokken advertentie? Is phone1 een doorschakelnummer? Inhoud actuele voorwaarden 30-04-2025? |
| **Operationele status** | **CONTRACT OF TOESTEMMING NODIG** | **ALLEEN HANDMATIG** |

#### B. Idealista: portaal, API en datadiensten

Bron voor de invulling: R01 + verificatie, R16. Bewijstype staat tussen haken in de cellen (1–7, masterprompt §5).

| Veld | R2-03 idealista.com — portaal, e-mailalerts en prijsrapporten | R2-04 Idealista Search API (developers.idealista.com) | R2-05 idealista/data (API testigos, valoraciones, AVM, Market Navigator) |
|---|---|---|---|
| Naam en officiële website | https://www.idealista.com | https://developers.idealista.com/access-request | https://www.idealista.com/data/ |
| Type aanbieder | Vastgoedportaal (Idealista, S.A.U., NIF A82505660) (type 2) | Officiële lees-API van het portaal, alleen op aanvraag (type 2) | Commerciële data- en waarderingstak van Idealista (type 2) |
| Geografische en inhoudelijke dekking | Landelijk; grootste aanbod in Jávea van de onderzochte bronnen (zie assistent). Prijsrapporten per gemeente maandelijks; Jávea-snippet 3.958 EUR/m² hoort bij augustus 2025 en vóór methodiekwijziging juli 2026 — niet gebruiken [te verifiëren] | Volgens de pagina 'property information published on idealista'; contractuele reikwijdte (advertenties van derden, doelen) niet gepubliceerd (type 2/4) | Landelijk; '2.632.762 inmuebles' (kwartaalcijfer), historie sinds 2005, zonemetrieken tot buurtniveau (type 1) |
| Technische toegang | Alleen browser. Geautomatiseerde verzoeken krijgen HTTP 403 op /ayuda/, /sala-de-prensa/, /valoracion-de-inmuebles/. robots.txt heeft géén 'Disallow: /' maar blokkeert taalmappen, /usuario/, /favoritos/, sortering, paginering en meer dan drie filters (R01-verificatie, type 3). Alerts: opgeslagen zoekopdracht direct/dagelijks/wekelijks, object volgen voor prijswijziging (type 2, deels oud/snippet) | https://developers.idealista.com/ → 302 → access-request-formulier (naam, e-mail, projectbeschrijving, reCAPTCHA). Geen openbare documentatie, endpoints of auth-beschrijving (R01-verificatie, type 3) | API ('API de testigos actuales e históricos', 'API de valoraciones y datos catastrales'), widget of databestanden op maat; alleen na contactformulier (type 2) |
| Beschikbare velden | Webweergave per advertentie; alerts leveren nieuwe advertenties die aan het zoekprofiel voldoen | ONBEKEND (alleen onofficiële client-readme, type 7) | Actuele en historische comparables, waarderingen, kadastergegevens, zonemetrieken; exacte velden ONBEKEND |
| Foto's en documenten | Foto's op het portaal; beschermd (TRLPI art. 128) en contractueel niet te downloaden voor commerciële doelen | ONBEKEND | ONBEKEND |
| Publicatie- en wijzigingsinformatie | Geen publicatiedatum; filter laatste 48 uur; prijsdaling als sortering | ONBEKEND | ONBEKEND |
| Historische gegevens | Alleen laatste prijsdaling zichtbaar; prijsrapporten met historische reeks (herberekend na methodiekwijziging juli 2026) | ONBEKEND | Ja volgens aanbieder (historische testigos, sinds 2005) |
| Verversingsfrequentie | Alerts direct/dagelijks/wekelijks; prijsrapport maandelijks (augustus 2026 gepubliceerd 02-09-2026, type 2) | ONBEKEND | Market Navigator 'en tiempo real' volgens aanbieder (type 1); API ONBEKEND |
| Rate limits | n.v.t. (geen API); botbeveiliging actief | ONBEKEND; '100 verzoeken per maand' alleen uit blogs (type 7) | ONBEKEND |
| Kosten | Gratis voor bezoekers; publiceren als particulier eerste 2 advertenties gratis (type 1) | ONBEKEND | Niet gepubliceerd; offerte |
| Contractstatus | Geen; voorwaarden verbieden robot, spider, scraper en monitoren zonder 'permiso expreso y por escrito' (type 2) | Niet aangevraagd. Voorwaarden 2024 noemen 'Servicio API' en 'Servicio de exportación de inmuebles' als aanvullende diensten, inhoud onbekend (type 2/7) | Geen; licentietekst niet online |
| Toegestane gebruiksdoelen | Handmatig bekijken; zoekopdrachten en favorieten bewaren (voorwaarden 2024, type 2); via portaalformulier reageren op een object | ONBEKEND tot acceptatie | ONBEKEND tot offerte. AVM is geen officiële taxatie (Idealista claimt conformiteit Orden ECO/805/2003 art. 21; AVM-regels staan in art. 15 bis) (type 1/2) |
| Rechten AI-analyse | Niet buiten een handmatige sessie; automatisch verwerken van eigen alertmails niet geregeld [advocaat] | ONBEKEND | ONBEKEND |
| Opslag en bewaren | Geen opslag van portaalcontent; alleen link, ID, handmatig genoteerde feiten met bron en datum (R16 §3.8, type 4) | ONBEKEND | ONBEKEND |
| Afgeleide gegevens en beeldvergelijking | Geen beeldvergelijking, geen prijshistorie-databank, geen herpublicatie | ONBEKEND | ONBEKEND |
| Contactpersoon of aanvraagroute | Idealista S.A.U., Madrid; voor toestemming schriftelijk (zie Search API / idealista/data) | Formulier https://developers.idealista.com/access-request (besluit Jan; eerlijke projectbeschrijving) | Formulier 'Pedir más información' op https://www.idealista.com/data/ |
| Laatste verificatie | 15-09-2026 | 15-09-2026 | 15-09-2026 |
| Openstaande vragen | Actuele voorwaarden (30-04-2025) in browser lezen; mag TREE eigen alertmails automatisch uitlezen (link, ID, prijs)? Exacte URL en peildatum van het Jávea-prijsrapport | Limieten, prijs, toegestane doelen, of advertenties van derden mogen worden teruggegeven voor acquisitie; verhouding tot 'Servicio API' in de voorwaarden | Prijs voor Jávea/Marina Alta; licentie voor opslag, AI-analyse en afgeleide dossiers; levert het ook actuele advertenties of alleen comparables? |
| **Operationele status** | **ALLEEN HANDMATIG** | **CONTRACT OF TOESTEMMING NODIG** | **CONTRACT OF TOESTEMMING NODIG** |

| Veld | R2-06 idealista/tools en Market Navigator (professioneel account) |
|---|---|
| Naam en officiële website | https://st3.idealista.com/static/es/pdf/es/servicios_profesionales_idealista.pdf |
| Type aanbieder | Makelaarssoftware en marktdatatool van Idealista (type 2, pdf november 2022) |
| Geografische en inhoudelijke dekking | Landelijk; ACM, 'valoraciones ilimitadas', marktstudies per zone, vergelijking met concurrentie (type 2, 2022) |
| Technische toegang | Klantaccount als professional; helpcentrum gaf 403. Zone-download van aanbod ('Cómo analizar la oferta en una zona') alleen via zoekmachine-snippet [te verifiëren] (type 7) |
| Beschikbare velden | ONBEKEND buiten de pdf-beschrijving (o.a. 'Datos históricos… días en mercado') |
| Foto's en documenten | ONBEKEND |
| Publicatie- en wijzigingsinformatie | ONBEKEND |
| Historische gegevens | Volgens pdf historische gegevens en dagen op de markt (type 2, 2022) |
| Verversingsfrequentie | ONBEKEND |
| Rate limits | ONBEKEND |
| Kosten | ONBEKEND |
| Contractstatus | ONBEKEND of TREE Properties een Idealista-klantaccount heeft |
| Toegestane gebruiksdoelen | ONBEKEND; publiceren via account geeft Idealista rechten op onze data (voorwaarden §8.2), geen leesrecht op andermans advertenties (type 2/4) |
| Rechten AI-analyse | ONBEKEND |
| Opslag en bewaren | ONBEKEND |
| Afgeleide gegevens en beeldvergelijking | ONBEKEND |
| Contactpersoon of aanvraagroute | Idealista professionele verkoop (via idealista/data-formulier of accountmanager) |
| Laatste verificatie | 15-09-2026 |
| Openstaande vragen | Bestaat de zone-download nog, voor welk abonnement, en mag de export worden opgeslagen en geanalyseerd? |
| **Operationele status** | **CONTRACT OF TOESTEMMING NODIG** |

#### C. Fotocasa Group, Milanuncios en DataVenues

Bron voor de invulling: R02 + verificatie, R16. Bewijstype staat tussen haken in de cellen (1–7, masterprompt §5).

| Veld | R2-07 Fotocasa en Habitaclia (incl. Índice Inmobiliario en Fotocasa Pro-publicatie) | R2-08 Milanuncios (categorie inmobiliaria) | R2-09 DataVenues (Fotocasa Pro Data: LITE, GO, ONE, PRO, API en data-feed) |
|---|---|---|---|
| Naam en officiële website | https://www.fotocasa.es · https://www.habitaclia.com · https://pro.fotocasa.es | https://www.milanuncios.com/inmobiliaria/ | https://datavenues.com |
| Type aanbieder | Vastgoedportalen op één platform van Fotocasa Group, S.L.U. (CIF B-70677125), sinds maart 2026 geconsolideerd door Scout24 (type 2) | Generalistische advertentiesite, Adevinta Motor S.L.U. (niet onder Fotocasa Group) (type 3) | Commerciële vastgoeddata-aanbieder van Fotocasa Group, S.L.U. (type 1/2) |
| Geografische en inhoudelijke dekking | Landelijk. Jávea 15-09-2026: Fotocasa 1.805 casas y pisos, 51 'a reformar', 295 terrenos; Habitaclia 1.757 viviendas, 285 terrenos y solares, 7 particulieren (type 3). Index Jávea sept. 2026: 4.236 EUR/m², +11,0 % j/j, negen wijken — alleen pisos y áticos, geen villa- of perceelindex (type 3/1) | Landelijk. Jávea 15-09-2026: 2.734 advertenties woningen, 38 particulier, 275 terrenos — lijsten bevatten ook niet-vastgoedadvertenties, dus geen zuivere objecttelling (type 3) | Volgens aanbieder landelijke aanbod- en waarderingsdata van Fotocasa, Habitaclia en Milanuncios; GO ook 'resto de grandes portales' en particulieren met eigenaarscontact, gebied 'Comarca' (productpagina uit 2024; marketingcijfers per pagina tegenstrijdig, type 1/7). Jávea-dekking niet gezien (app achter login) |
| Technische toegang | Lezen: alleen browser en alerts (e-mail/app). Geen openbare lees-API of dataset voor de portalen. Publiceren: Fotocasa Pro met API key via CRM (publicatiekoppeling, geen leesrecht). Aviso legal fotocasa.es alleen via JavaScript; hulpcentra 403 (R02, type 3) | Browser en 'Guardar búsqueda'. curl krijgt 403 'Pardon Our Interruption'. robots.txt blokkeert AI-trainingscrawlers en staat vijf zoek-/RAG-agents toe (o.a. Claude-User) — geen licentie voor een eigen scraper (R02, R16-verificatie, type 3/4) | Webapplicatie app.datavenues.com (login). Officieel aanbod: 'Consúltanos por nuestras APIs y nuestro Data feed' (homepage, gewijzigd 07-08-2026; doelgroep consultoras, servicers, banca). Export van 'El Ranking' naar Excel/CSV volgens FAQ (2020) (R02-verificatie, type 1) |
| Beschikbare velden | Lijstweergave: prijs, type, wijk, kamers, badkamers, oppervlak, labels ('Más de 3 meses', 'ayer', 'Oportunidad'). Paginacode noemt labels 'Inmuebles en subasta', 'ocupados', 'urge vender' — werking als filter niet getest (type 3/7) | Prijs, type, locatie, particulier/professioneel (via aparte pagina) | Volgens aanbieder: aanbod, ranking, waardering, vraag/aanbod, kadaster, particulieren met telefoon (GO). Notariële sluitprijzen op 29-05-2026 aangekondigd ('incorporará') — live-status ONBEKEND. Specificatie API/feed ONBEKEND |
| Foto's en documenten | Foto's ja (door adverteerders gratis aan het portaal gelicentieerd, Habitaclia CG); documenten ONBEKEND | Foto's; documenten ONBEKEND | ONBEKEND |
| Publicatie- en wijzigingsinformatie | Grove ouderdomslabels; geen exacte publicatiedatum | ONBEKEND | ONBEKEND |
| Historische gegevens | Geen voor advertenties; index sinds januari 2005 | ONBEKEND | ONBEKEND |
| Verversingsfrequentie | Alerts volgens Fotocasa (artikel 2020): binnen enkele minuten, gebundeld, beperkt aantal keren per dag, niet tussen 00:00 en 06:00, filter 'a reformar' (type 1). Index maandelijks, gemiddelde van laatste 4 weken | Kanaal en frequentie van opgeslagen zoekopdrachten ONBEKEND (hulpcentrum 403) | 'Actualizados diariamente' volgens aanbieder (type 1) |
| Rate limits | n.v.t.; botbeveiliging | n.v.t.; botbeveiliging | ONBEKEND; LITE 100 waarderingen en 3 rapporten per maand (pagina 2024, type 1) |
| Kosten | Lezen gratis; Fotocasa Pro-packs op aanvraag (Basic bevat DataVenues 'Valoración', Premium 'Lite' + captación de particulares) (type 1) | Lezen gratis; publiceren via Fotocasa Pro-packs of Milanuncios Pro | Niet gepubliceerd; widget via Witei 30 EUR/maand + btw (type 1) |
| Contractstatus | ONBEKEND of TREE Properties een Fotocasa Pro-pack heeft | Geen; voorwaarden niet leesbaar | Geen. Licenties via een commercial van Fotocasa/Habitaclia (type 1) |
| Toegestane gebruiksdoelen | Handmatig raadplegen en alerts. Habitaclia CG: geen recht op 'explotación … reproducción' zonder uitdrukkelijke toestemming (type 2) | Handmatig raadplegen; machineleesbaar voorbehoud tegen AI-training (RDL 24/2021 art. 67.3, type 4) | Condiciones Generales de Uso (gewijzigd 08-07-2026): gebruik 'únicamente para sus propias necesidades', geen 'explotación comercial', geen overname van teksten/beelden/advertenties zonder schriftelijke toestemming; 'condiciones particulares' niet openbaar (type 2) |
| Rechten AI-analyse | Niet buiten handmatige sessie zonder toestemming | Niet buiten handmatige sessie | ONBEKEND — in condiciones particulares te regelen |
| Opslag en bewaren | Geen opslag van content; link en eigen notities | Geen opslag van content | ONBEKEND |
| Afgeleide gegevens en beeldvergelijking | Geen beeldvergelijking of herpublicatie; hergebruiksrechten indexcijfers ONBEKEND | Geen | ONBEKEND; percelen alleen via comparables te waarderen (FAQ, type 1). Eigenaarscontacten en waarderingsradar: AVG-vraag |
| Contactpersoon of aanvraagroute | Formulier https://pro.fotocasa.es/form-alta-cliente-profesional-inmobiliario/; bestaande klanten 900 823 825 | Via Fotocasa Pro (900 823 825) of Milanuncios Pro | Formulier pro.fotocasa.es; support@datavenues.com; bestaande klanten 900 823 825 |
| Laatste verificatie | 15-09-2026 | 15-09-2026 | 15-09-2026 |
| Openstaande vragen | Tekst aviso legal fotocasa.es (handmatig opslaan); is parsen van alertmails toegestaan; bestaan filter-URL's voor subasta/ocupados; mag indexcijfer met bronvermelding in dossiers? | Voorwaardentekst (handmatig lezen); blijft Milanuncios na de eigendomssplitsing in de Fotocasa Pro-bundel? | Velden, verversing, dekking Marina Alta en prijs van API/feed; komt TREE als makelaar/acquisiteur in aanmerking; mag opslag, AI-analyse en dossiervorming; herkomst 'resto de grandes portales'; rechtsgrond eigenaarscontact; zijn sluitprijzen live en op welk niveau? |
| **Operationele status** | **ALLEEN HANDMATIG** | **ALLEEN HANDMATIG** | **CONTRACT OF TOESTEMMING NODIG** |

#### D. Overige portalen

Bron voor de invulling: R03 + verificatie, R16. Bewijstype staat tussen haken in de cellen (1–7, masterprompt §5).

| Veld | R2-10 Kyero (portaal en Kyero v3-feedstandaard) | R2-11 thinkSPAIN | R2-12 pisos.com |
|---|---|---|---|
| Naam en officiële website | https://www.kyero.com · https://help.kyero.com/estate-agents/xml-import-specification | https://www.thinkspain.com | https://www.pisos.com |
| Type aanbieder | Internationaal portaal; exploitant volgens snippet Portal47 Ltd (Companies House 06536265, Bath; koppeling met kyero.com [te verifiëren]); sinds 05-12-2024 van idealista (type 2/7) | Internationaal portaal, Think Web Content SL (B02283380, Paterna) (type 2) | Spaans portaal, Habitatsoft S.L. (B-61562088, RM Madrid); sinds 18-03-2025 van Immobiliare.it S.p.A. (nieuws over CNMV-melding) (type 2) |
| Geografische en inhoudelijke dekking | Spanje, Portugal, Frankrijk, Italië. Jávea ±1.717 alleen via snippet zonder datum (type 7) | Heel Spanje, 12 talen. Jávea 15-09-2026: 2.605 te koop, 151 bouwkavels (type 3) | Heel Spanje. Jávea 15-09-2026: 2.092 resultaten casas y pisos (één curl-verzoek, type 3) |
| Technische toegang | Lezen: geen API (robots.txt Disallow /*api/*, Crawl-delay 1); kyero.com geeft 403 aan tools. Publiceren: Kyero v3 XML-importfeed (absolute feed; afwezig = verwijderd) en eigen exportfeed per makelaar met alleen eigen objecten (type 2/3) | Lezen: browser, 'Create Alert', 'Save Search'; filter 'Price Reduced in last 30 days'. Publiceren: XML-feeds via CRM (formaat niet openbaar). Geen lees-API (R03, type 3) | Lezen: browser; 'Guardar búsqueda', per advertentie 'Avísame si baja', filter 'Con precio rebajado' en 'Última semana/mes'. WebFetch weigert, gewoon HTTP-verzoek werkt (geen omzeiling). Geen lees-API; publicatiespecificatie niet openbaar (R03-verificatie, type 3) |
| Beschikbare velden | Kyero v3: id, date (last modified), ref, price, price_freq, type, town, province, beds, baths, pool, surface_area, energy_rating, url, desc, features, images (max 50), optioneel catastral; geen status-, verkocht- of verwijderveld (type 2/3) | Webweergave; geen feed voor derden | Webweergave |
| Foto's en documenten | Foto's max 50 in feed; plattegrond via tag | Foto's op portaal | Foto's op portaal |
| Publicatie- en wijzigingsinformatie | Alleen date = laatste wijziging; geen publicatiedatum | Filter prijsdaling laatste 30 dagen; publicatiedatum ONBEKEND | Filters laatste week/maand en prijsdaling |
| Historische gegevens | Geen | Geen | Geen |
| Verversingsfrequentie | Kyero-documentatie tegenstrijdig: dagelijks ca. 01:30 CET, 'daily' of vijf nachten per week voor Prime; wekelijks voor Free (type 7). Alerts standaard dagelijks, alleen nieuwe objecten (type 2) | Alertfrequentie ONBEKEND | Alertfrequentie ONBEKEND |
| Rate limits | robots.txt Crawl-delay 1; API niet openbaar | robots.txt zonder algemene beperking; geen API | n.v.t.; robots.txt sluit downloaders uit |
| Kosten | Adverteren gratis + Prime per listing (prijzen alleen via derde partij, type 7) | Adverteren vanaf 25 EUR/maand; introductiepakketten 118–625 EUR exclusief btw (type 1) | Lezen gratis; publicatiepakketten gekoppeld aan indomio.es (vakpers, type 2) |
| Contractstatus | Geen | Geen | Geen |
| Toegestane gebruiksdoelen | Handmatig en alerts. Voorwaarden (403; snippet) verbieden robots/scrapers en systematische extractie zonder schriftelijke toestemming (type 7) | Handmatig en alerts. Reproductie, opslag e.d. vereist 'express consent' / 'consentimiento expreso' (Spaanse versie bindend; niet per se schriftelijk); geen scrapingclausule (R03-verificatie, type 2) | Handmatig en alerts. Aviso legal: eigen gebruik, 'no realizar en ningún caso una explotación comercial' (type 2) |
| Rechten AI-analyse | Niet buiten handmatige sessie | Niet zonder toestemming | Niet buiten handmatige sessie |
| Opslag en bewaren | Geen | Geen opslag zonder toestemming | Geen; let op: naam en telefoon van particuliere adverteerders worden automatisch gepubliceerd — persoonsgegevens niet opslaan (type 2) |
| Afgeleide gegevens en beeldvergelijking | Geen; marktdatapagina kyero.com/en/data niet leesbaar (403) | Geen | Geen |
| Contactpersoon of aanvraagroute | help.kyero.com; adverteerdersaccount | https://www.thinkspain.com/advertise/property-agent | Professionals via pisos.com/Indomio-verkoop |
| Laatste verificatie | 15-09-2026 | 15-09-2026 | 15-09-2026 |
| Openstaande vragen | Voorwaarden in browser lezen; granulariteit en prijs van Kyero-marktdata; welke verwerkingsfrequentie geldt echt | Is geautomatiseerde verwerking van alertmails toegestaan? Accepteert thinkSPAIN Kyero v3 rechtstreeks (voor eigen publicatie)? | Publiceert de Indomio-feed-API ook naar pisos.com? Is alertmailverwerking toegestaan? |
| **Operationele status** | **ALLEEN HANDMATIG** | **ALLEEN HANDMATIG** | **ALLEEN HANDMATIG** |

| Veld | R2-13 yaencontre | R2-14 SpainHouses | R2-15 Green-Acres |
|---|---|---|---|
| Naam en officiële website | https://www.yaencontre.com | https://www.spainhouses.net | https://www.green-acres.es |
| Type aanbieder | Spaans portaal; idealista-deelneming sinds 13-02-2020 (type 2); volledige absorptie alleen via snippet [te verifiëren] | Spaans/meertalig portaal, Entersoftweb S.L. (B92308949, Málaga) (type 2) | Internationaal portaal, Green-Acres S.A.S. (Parijs, RCS 453 785 156) (type 2) |
| Geografische en inhoudelijke dekking | Heel Spanje. Jávea alleen via snippets zonder datum: ±1.755 casas, 742 pisos, 413 terrenos (type 7) | Heel Spanje; eigenaren én professionals. Jávea 15-09-2026: 488 woningen (322 huizen, 166 flats) (type 3) | Spanje 51.375 objecten volgens site; Jávea 15-09-2026: 799 te koop (type 3); Europese tweedewoningkopers |
| Technische toegang | Elke niet-browsertoegang krijgt 403 met DataDome-captcha, ook robots.txt (type 3). Geen lees-API gevonden | Lezen: browser, 'Save search', e-mail met nieuwe advertenties, prijsalerts; filters 'To reform' en 'Reduced'. Publiceren: eigen XML (cartera.xsd) via 32+ CRM's; geen lees-API (type 2/3) | Lezen: browser, 'Save alert' dagelijks/wekelijks. robots.txt: ClaudeBot Disallow /, Request-rate 1/1. Publiceren: XML Gateway v4.1 (06.2026), cancel-and-replace, dagelijks opgehaald. Geen lees-API (R03-verificatie, type 2/3) |
| Beschikbare velden | ONBEKEND (niet leesbaar) | Publicatie-XML: referencia, fecha (laatste wijziging of invoer), tipoInmueble, tipoOferta, precio, provincia, localidad, geoLocalizacion, direccion, descripcionPrincipal | Webweergave; gateway-velden alleen voor eigen advertenties |
| Foto's en documenten | ONBEKEND | Onbeperkt aantal foto's in publicatie-XML | Tot 60 foto's in gateway |
| Publicatie- en wijzigingsinformatie | Alerts bij nieuwe advertenties, prijsdaling en wijzigingen in bewaarde advertenties (snippets helpcentrum, type 7) | fecha = wijziging of invoegdatum; filter 'Reduced' | Geen status; filter 'To renovate' niet teruggevonden in HTML [te verifiëren] |
| Historische gegevens | ONBEKEND | Geen | Geen |
| Verversingsfrequentie | ONBEKEND | Alertfrequentie ONBEKEND | Alerts dagelijks of wekelijks |
| Rate limits | Antibotbeveiliging | Geen crawl-delay; geen API | Request-rate 1/1, Crawl-delay 1; ClaudeBot uitgesloten |
| Kosten | ONBEKEND | Adverteren vanaf 10 EUR/maand (btw niet vermeld) | Adverteren: 30 dagen gratis proef, daarna ONBEKEND |
| Contractstatus | Geen; voorwaarden niet leesbaar | Geen | Geen |
| Toegestane gebruiksdoelen | Handmatig in browser en alerts | Handmatig en alerts; geen IP- of scrapingclausule gevonden (alleen privacybeleid) — dat is geen licentie (type 3/4) | Handmatig en alerts; art. 7 verbiedt reproductie van content ('strictly prohibited') (type 2) |
| Rechten AI-analyse | ONBEKEND; niet zonder toestemming | ONBEKEND; niet zonder toestemming | Niet zonder toestemming |
| Opslag en bewaren | ONBEKEND; geen opslag | ONBEKEND; geen opslag | Geen |
| Afgeleide gegevens en beeldvergelijking | ONBEKEND; geen | ONBEKEND; geen | Geen |
| Contactpersoon of aanvraagroute | Professionalspagina niet leesbaar; ONBEKEND | administracion@entersoftweb.com, 952 020 401 (zakelijk) | https://www.green-acres.fr/en/Register/Agency |
| Laatste verificatie | 15-09-2026 | 15-09-2026 | 15-09-2026 |
| Openstaande vragen | Juridische status (zelfstandig of opgegaan in idealista), gedeelde voorraad met idealista, voorwaarden | Aandeel particulier aanbod in Jávea; alertverwerking | Bestaat filter 'To renovate'; alertverwerking |
| **Operationele status** | **ALLEEN HANDMATIG** | **ALLEEN HANDMATIG** | **ALLEEN HANDMATIG** |

| Veld | R2-16 Indomio (indomio.es) |
|---|---|
| Naam en officiële website | https://www.indomio.es · https://feed.indomio.com/docs/ies/ |
| Type aanbieder | Portaal van Immobiliare.it S.p.A. (groep met pisos.com en enalquiler.com) (type 1/2) |
| Geografische en inhoudelijke dekking | Spanje. Jávea ±1.994 alleen via snippet (type 7) |
| Technische toegang | Lezen: indomio.es geeft 403. Publiceren: REST-push-API (HTTP BASIC, IP-whitelist, 'almost real time') — uitsluitend publiceer-API voor eigen advertenties; feedback-API's (leads, telefoons) alleen over eigen advertenties (R03-verificatie, type 2) |
| Beschikbare velden | Publicatiepayload met date-updated, @operation write/archive; geen leesfeed |
| Foto's en documenten | Alleen eigen advertenties |
| Publicatie- en wijzigingsinformatie | Geen publicatiedatum in payload |
| Historische gegevens | Geen |
| Verversingsfrequentie | Publicatie 'almost real time' (geldt voor publiceren, niet voor lezen) |
| Rate limits | Publiceren 'without limits'; lezen n.v.t. |
| Kosten | ONBEKEND |
| Contractstatus | Geen |
| Toegestane gebruiksdoelen | Handmatig in browser; voorwaarden niet leesbaar (403) |
| Rechten AI-analyse | ONBEKEND; niet zonder toestemming |
| Opslag en bewaren | ONBEKEND; geen |
| Afgeleide gegevens en beeldvergelijking | ONBEKEND; geen |
| Contactpersoon of aanvraagroute | Support via feed.indomio.com |
| Laatste verificatie | 15-09-2026 |
| Openstaande vragen | Voorwaarden; publiceert één feed ook naar pisos.com; inhoud kennisbankonderdeel 'Auctions catalog' |
| **Operationele status** | **ALLEEN HANDMATIG** |

#### E. Niet-geautoriseerde derden

Bron voor de invulling: R02, R16. Bewijstype staat tussen haken in de cellen (1–7, masterprompt §5).

| Veld | R2-17 Commerciële scrapers die zich 'API' noemen (Happy Endpoint, Apify, Oxylabs, WebScrapingHub, Spider e.a.) |
|---|---|
| Naam en officiële website | https://docs.happyendpoint.com/fotocasa/ · https://apify.com/parsebird/fotocasa-scraper · https://oxylabs.io/products/scraper-api/web/fotocasa |
| Type aanbieder | Derde partijen die portaaldata scrapen (eigen verklaring, type 1) |
| Geografische en inhoudelijke dekking | Fotocasa, Milanuncios, Idealista, Kyero e.a. volgens eigen reclame |
| Technische toegang | REST tegen betaling; Apify adviseert residentiële proxies tegen antibotbeveiliging, Oxylabs noemt captcha-afhandeling (type 1) |
| Beschikbare velden | n.v.t. |
| Foto's en documenten | n.v.t. |
| Publicatie- en wijzigingsinformatie | n.v.t. |
| Historische gegevens | n.v.t. |
| Verversingsfrequentie | n.v.t. |
| Rate limits | n.v.t. |
| Kosten | Niet onderzocht |
| Contractstatus | Geen autorisatie van de portalen |
| Toegestane gebruiksdoelen | Geen: in strijd met portaalvoorwaarden en databankrecht (TRLPI art. 133.2); medeaansprakelijkheid mogelijk (art. 138); omzeilen van beveiliging kan strafbaar zijn (CP 197 bis) [advocaat] (type 2/4) |
| Rechten AI-analyse | Geen |
| Opslag en bewaren | Geen |
| Afgeleide gegevens en beeldvergelijking | Geen |
| Contactpersoon of aanvraagroute | n.v.t. |
| Laatste verificatie | 15-09-2026 |
| Openstaande vragen | Geen — bewust uitgesloten |
| **Operationele status** | **NIET GEBRUIKEN** |

#### F. Commerciële dataleveranciers en taxateurs

Bron voor de invulling: R04 + verificatie. Bewijstype staat tussen haken in de cellen (1–7, masterprompt §5).

| Veld | R2-18 Casafari (Property Data API, alerts, exports) | R2-19 Brainsre | R2-20 Accumin Intelligence (uDA/Pulse, Tinsa Digital AVM, comparables-API) |
|---|---|---|---|
| Naam en officiële website | https://www.casafari.com/products/property-data-api/ | https://brainsre.com | https://www.accumin.com/intelligence/data/real-estate · https://www.tinsadigital.com/que-hacemos/avm/ |
| Type aanbieder | Commerciële aggregator: indexeert advertenties uit '30.000+' portalen en makelaarssites, ontdubbeld; publiceert zelf niets (type 1) | Big-data-platform vastgoed (Grupo Aura) (type 1) | Commerciële data-, AVM- en comparablesleverancier; uDA door Tinsa Group gekocht (akkoord 14-05-2024), sinds 22-05-2025 samen met Tinsa Digital, Deyde en Datacentric in Accumin (type 1) |
| Geografische en inhoudelijke dekking | 20+ landen met database per land, waaronder Spanje; Jávea-dekking niet bewezen. '45 Million registered property sales with closing prices' zonder landenopgave (type 1/7) | Spanje, Portugal, Italië, Frankrijk; lokaal niet getoetst | Spanje; '70M real estate comparables' volgens aanbieder; lokaal niet getoetst |
| Technische toegang | REST-API, MCP, iFrame, data-exports, webplatform, alerts ('Market Leads') (type 1) | Webplatform met gratis proef (app.brainsre.com); maatwerk: eenmalige levering, terugkerend via e-mail/FTP, API op maat (type 1) | Platform Pulse (voor ons 403), uDA-API, Tinsa Digital AVM via bestand of API (type 1/7) |
| Beschikbare velden | Volgens aanbieder: ontdubbeld aanbod met historie, prijshistorie, transacties, AVM, area insights; exacte velden ONBEKEND | Actueel en historisch aanbod, registertransacties, AVM, rapporten; velden ONBEKEND | Comparables, AVM met betrouwbaarheidsmaten, indicatoren; velden ONBEKEND |
| Foto's en documenten | Foto's: volgens voorwaarden alleen thumbnails bewaard (type 2) | ONBEKEND | ONBEKEND |
| Publicatie- en wijzigingsinformatie | Historie per object volgens aanbieder ('60+ million properties with history') | ONBEKEND | ONBEKEND |
| Historische gegevens | Ja volgens aanbieder ('7+ years data history on closing prices') | Historisch aanbod en transacties volgens aanbieder | Volgens aanbieder historische taxaties en comparables |
| Verversingsfrequentie | Alerts realtime volgens aanbieder (type 1) | ONBEKEND | ONBEKEND |
| Rate limits | 'CASAFARI API specifications for the format and throughput limits' — niet openbaar | ONBEKEND | ONBEKEND |
| Kosten | Niet gepubliceerd; prijs hangt af van type API, volume en integratie; abonnement 12 maanden met automatische verlenging (FAQ, type 1) | Prijspagina alleen via JavaScript, niet leesbaar — ONBEKEND | Niet gepubliceerd; offerte |
| Contractstatus | Geen | Geen | Geen |
| Toegestane gebruiksdoelen | Gebruiksvoorwaarden website (27-03-2018): persoonlijke, herroepbare licentie; verbod op systematisch verzamelen en afgeleide werken. Abonnements-/API-voorwaarden niet ingezien (type 2) | ONBEKEND | ONBEKEND; levert context (waardering), geen objectenstroom |
| Rechten AI-analyse | ONBEKEND — expliciet contractueel regelen | ONBEKEND | ONBEKEND |
| Opslag en bewaren | ONBEKEND — expliciet regelen | ONBEKEND | ONBEKEND |
| Afgeleide gegevens en beeldvergelijking | ONBEKEND; standaardvoorwaarden verbieden afgeleide werken | ONBEKEND | ONBEKEND |
| Contactpersoon of aanvraagroute | commercial@casafari.com; demo/offerte via website | sales@brainsre.com | intelligence@accumin.com; hi@tinsadigital.com; +34 913 822 002 (zakelijk) |
| Laatste verificatie | 15-09-2026 | 14-09-2026 | 15-09-2026 |
| Openstaande vragen | Aantal objecten en bronnen voor Jávea, verversing, Spaanse sluitprijzen, licentie voor opslag/AI/beeldvergelijking, prijs | Prijzen, dekking Jávea, voorwaarden | Eén offerte voor AVM + comparables voor Marina Alta; licentie voor opslag en dossiers |
| **Operationele status** | **CONTRACT OF TOESTEMMING NODIG** | **TECHNISCH ONDERZOEK NODIG** | **CONTRACT OF TOESTEMMING NODIG** |

| Veld | R2-21 Tinsa Radar (marktstudies) en Tinsa IMIE | R2-22 Gloval (Big Data, AVM) | R2-23 Grupo ST (Sociedad de Tasación) — tools |
|---|---|---|---|
| Naam en officiële website | https://radar.tinsa.es/es · https://www.tinsa.es/informes/imie-mercados-locales/ | https://www.gloval.es/servicios/big-data-del-mercado-inmobiliario/ | https://tools.st-tasacion.es/ |
| Type aanbieder | Marktstudietool van taxateur Tinsa (Accumin-groep) (type 1) | Taxateur met data- en AVM-dienst (type 1) | Taxateur met webtools (type 1) |
| Geografische en inhoudelijke dekking | Zelf getekend gebied; testigos uit taxaties en aanbod. IMIE: provincie Alicante 1.981 EUR/m² (2T 2026); geen eigen Jávea-reeks (type 1/3) | Landelijk, van sección censal tot nationaal; lokaal niet getoetst | Landelijk; publieke cijfers grof |
| Technische toegang | Web, PDF-uitvoer; geen API genoemd | API, widgets, bestanden (type 1) | Webtools, 'Valores en tu zona' achter login; hoofdsite alleen JavaScript; geen API-documentatie gevonden (type 3) |
| Beschikbare velden | Gemiddelde testigowaarden, aanbodprijzen, huur, onderhandelingsmarge, voorraadverdeling | Kadaster, sociodemografie, waarden, EPC's, fysieke en klimaatrisico's | ONBEKEND |
| Foto's en documenten | PDF-rapport | ONBEKEND | ONBEKEND |
| Publicatie- en wijzigingsinformatie | Testigos ouder dan 12 maanden vervallen (type 1) | ONBEKEND | ONBEKEND |
| Historische gegevens | Beperkt tot 12 maanden testigos | ONBEKEND | ONBEKEND |
| Verversingsfrequentie | Maandelijks ververst; IMIE per kwartaal | ONBEKEND | ONBEKEND |
| Rate limits | Per abonnement 15 of 45 studies per maand | Responstijd circa 2 s volgens aanbieder; limieten ONBEKEND | ONBEKEND |
| Kosten | 29 EUR per studie, 99 EUR/maand (15), 259 EUR/maand (45); 7 dagen gratis; btw-status niet vermeld (type 1) | Afhankelijk van type en aantal objecten; niet gepubliceerd | ONBEKEND |
| Contractstatus | Geen abonnement | Geen | Geen |
| Toegestane gebruiksdoelen | Handmatige second opinion in een dealdossier (type 4) | ONBEKEND; context, geen objecten | ONBEKEND |
| Rechten AI-analyse | ONBEKEND | ONBEKEND | ONBEKEND |
| Opslag en bewaren | PDF in dossier; overige ONBEKEND | ONBEKEND | ONBEKEND |
| Afgeleide gegevens en beeldvergelijking | ONBEKEND | ONBEKEND | ONBEKEND |
| Contactpersoon of aanvraagroute | Via radar.tinsa.es | info@gloval.es, +34 915 613 388 (zakelijk) | Via website; ONBEKEND |
| Laatste verificatie | 15-09-2026 | 14-09-2026 | 14-09-2026 |
| Openstaande vragen | Btw; voorwaarden voor gebruik in klantdossiers | Dekking en prijs Marina Alta | Bestaat er iets fijnmazigs voor Jávea? |
| **Operationele status** | **ALLEEN HANDMATIG** | **CONTRACT OF TOESTEMMING NODIG** | **TECHNISCH ONDERZOEK NODIG** |

#### G. MLS-netwerken en makelaarsfeeds

Bron voor de invulling: R04 + verificatie. Bewijstype staat tussen haken in de cellen (1–7, masterprompt §5).

| Veld | R2-24 Resales-Online (MLS + CRM, WebAPI V6) | R2-25 MLS 03724 Teulada-Moraira | R2-26 Overige MLS-netwerken Costa Blanca (MLS Costa, MLS Mediaelx/LetsINMO, MLS Denia Realtor) |
|---|---|---|---|
| Naam en officiële website | https://support.resales-online.com/en/articles/4885689-terms-conditions-of-usage-resales-online | https://www.mls03724.com/en/about-us/ | https://www.mlscosta.com/ · https://mediaelx.net/en/mls-mediaelx/ · https://www.deniacasas.es/en/about-us/ |
| Type aanbieder | MLS-netwerk en makelaars-CRM (Costa del Sol, Costa Blanca, Costa Cálida) (type 1) | Lokale MLS-vereniging (Asociación Inmobiliaria MLS Teulada-Moraira, CIF G-42632737) (type 1) | MLS-/samenwerkingsnetwerken van makelaars (type 1) |
| Geografische en inhoudelijke dekking | Costa Blanca-leden; aantal alleen via snippet ('more than 100 member agents'), Jávea-aandeel ONBEKEND | Officiële site: Teulada-Moraira, gedeelde exclusieven, vier oprichters. Derdenblog (2023): 16 kantoren, uitwisseling verkoopdata, gebied incl. Jávea en Dénia [te verifiëren] (type 1) | MLS Costa: resales Costa Blanca, Cálida, Almería, del Sol; Mediaelx: 'over 3,000 properties' (45+ kantoren niet teruggevonden); Denia Realtor: Dénia, '25 companies' volgens een lid. Jávea-aandeel ONBEKEND |
| Technische toegang | Lidmaatschap; WebAPI V6 met API-key per IP-adres, bedoeld voor live weergave 'without the need of a database'; resales-online.com geeft 403 (type 1/3) | Lidmaatschap; publieke zoekfunctie op de site (curl krijgt JavaScript-beveiligingscheck) (type 3) | MLS Costa: gratis account voor delen van eigen resales, betaald 'customized XML feed'; Mediaelx: lidmaatschap en XML; Denia Realtor: lidmaatschap (type 1) |
| Beschikbare velden | ONBEKEND (documentatie voor ons niet leesbaar) | ONBEKEND | ONBEKEND |
| Foto's en documenten | ONBEKEND; kopiëren van teksten/foto's van andere leden verboden | ONBEKEND | ONBEKEND |
| Publicatie- en wijzigingsinformatie | ONBEKEND | ONBEKEND | ONBEKEND |
| Historische gegevens | ONBEKEND | Verkoopdata onder leden volgens derdenblog [te verifiëren] | ONBEKEND |
| Verversingsfrequentie | Realtime via API volgens aanbieder | ONBEKEND | ONBEKEND |
| Rate limits | ONBEKEND | ONBEKEND | ONBEKEND |
| Kosten | Prijspagina 403 — ONBEKEND | Niet gepubliceerd | Betaalde tarieven niet gepubliceerd |
| Contractstatus | ONBEKEND of TREE Properties lid is | ONBEKEND of TREE lid is | Geen |
| Toegestane gebruiksdoelen | Voorwaarden (bijgewerkt 04-05-2026): netwerkobjecten van andere leden alleen op de eigen website volgens deelrechten; feeds met andermans objecten aan derden verboden; afgeleide data eigendom ReSales Andalucía (type 1) | ONBEKEND; deelregels tussen leden | ONBEKEND |
| Rechten AI-analyse | Niet geregeld; schriftelijke toestemming nodig | ONBEKEND | ONBEKEND |
| Opslag en bewaren | API bedoeld zonder eigen database; opslag van netwerkobjecten niet toegestaan zonder toestemming (type 1/4) | ONBEKEND | ONBEKEND |
| Afgeleide gegevens en beeldvergelijking | Afgeleide data eigendom ReSales; beeldvergelijking niet toegestaan zonder toestemming | ONBEKEND | ONBEKEND |
| Contactpersoon of aanvraagroute | support.resales-online.com | info@mls03724.com, +34 965 058 105 (zakelijk) | Via de websites |
| Laatste verificatie | 15-09-2026 | 15-09-2026 | 15-09-2026 |
| Openstaande vragen | Lidmaatschap TREE; kosten; schriftelijke bevestiging voor intern analytisch gebruik; artikel 'Static XML feed for shared properties' | Huidig ledental, dekking Jávea, kosten, of verkoopdata contractueel beschikbaar is voor leden | Aantal objecten in Jávea, tarief XML-feed, gebruiksvoorwaarden; is "MLS Denia Realtor" (via deniacasas.es) dezelfde vereniging als MLS Dénia (mlsdenia.com, R2-53)? Beide bronnen noemen "25" samenwerkende kantoren via Dénia Casas (type 4) |
| **Operationele status** | **CONTRACT OF TOESTEMMING NODIG** | **CONTRACT OF TOESTEMMING NODIG** | **TECHNISCH ONDERZOEK NODIG** |

| Veld | R2-27 APIred / Apibolsa (bolsa van het Colegio API Alicante) | R2-28 MLS-netwerken zonder dekking van Jávea (Agora MLS, Inmobalia) | R2-29 Makelaars-CRM-exports van eigen objecten (Inmovilla, Witei, Mobilia) |
|---|---|---|---|
| Naam en officiële website | http://www.apired.com/ · https://www.apibolsa.es/bolsa-inmobiliaria-como-funciona-mls.html | https://www.agoramls.es/inmobiliarias-alicante/ · https://www.inmobalia.com/ | https://inmovilla.freshdesk.com/support/solutions/articles/103000118125 · https://faq.witei.com/en/articles/865807-xml-export-with-your-properties · https://www.mobiliagestion.es/noticias-software-inmobiliario/api-crm-mobilia-zapier-n8n-wordpress-agente-ia |
| Type aanbieder | Beroepsorganisatie-MLS (Colegio de Agentes de la Propiedad Inmobiliaria de Alicante) (type 1) | Landelijke MLS-groep (Agora) en CRM/MLS Costa del Sol (Inmobalia) (type 1) | Exportfuncties in CRM's van individuele makelaars (type 1) |
| Geografische en inhoudelijke dekking | Provincie Alicante; Jávea-aantal niet getoetst | Agora: 22 kantoren in Alicante, dichtstbij Benissa, geen in Jávea/Dénia/Moraira. Inmobalia: Costa del Sol (type 1/3) | Alleen de eigen objecten van een makelaar die meewerkt |
| Technische toegang | Publieke zoekfunctie apired.com; deelname voor colegiados met contract voor software INMOPC; import via XML in Kyero 3.0 (type 1) | Lidmaatschap/abonnement; Inmobalia XML/API | Inmovilla: API (direct bijgewerkt), dagelijkse XML, iframe. Witei: geen publieke API; XML-export in Kyero V3 (elk uur ververst, max. 50 foto's) en webhooks. Mobilia: 'Mobilia Public API' met Swagger volgens artikel (URL niet gezien) (R04-verificatie, type 1) |
| Beschikbare velden | ONBEKEND | n.v.t. voor Jávea | Kyero v3 of CRM-eigen velden |
| Foto's en documenten | ONBEKEND | n.v.t. | Foto's van het kantoor (rechten fotografen/eigenaren te regelen) |
| Publicatie- en wijzigingsinformatie | ONBEKEND | n.v.t. | Afhankelijk van CRM; Kyero-export zonder publicatiedatum |
| Historische gegevens | ONBEKEND | n.v.t. | Geen in export |
| Verversingsfrequentie | ONBEKEND | n.v.t. | Witei elk uur; Inmovilla-XML dagelijks, API direct |
| Rate limits | ONBEKEND | n.v.t. | ONBEKEND |
| Kosten | Niet gepubliceerd | Inmobalia 150/225/300 EUR per maand + 450 EUR setup, exclusief btw (type 1) | ONBEKEND per CRM-abonnement |
| Contractstatus | ONBEKEND of TREE colegiado is | Geen | Per makelaar schriftelijk vast te leggen (sjabloon R16 §6.3) |
| Toegestane gebruiksdoelen | Publiek: handmatig zoeken; als lid volgens deelregels | n.v.t. | Eigen objecten van het kantoor; netwerkobjecten van collega's mag een makelaar niet doorgeven (Resales-voorwaarden; juridische lijn type 4 [advocaat]) |
| Rechten AI-analyse | ONBEKEND | n.v.t. | Per afspraak |
| Opslag en bewaren | ONBEKEND | n.v.t. | Per afspraak |
| Afgeleide gegevens en beeldvergelijking | ONBEKEND | n.v.t. | Per afspraak |
| Contactpersoon of aanvraagroute | coapi@apialicante.com, 965 98 41 25; info@apibolsa.es (zakelijk) | n.v.t. | Per makelaar (kantorenregister: bijlage B-K, tabel K-1; aanleverroute R2-52) |
| Laatste verificatie | 15-09-2026 | 15-09-2026 | 15-09-2026 |
| Openstaande vragen | Colegiado-status TREE; aantal objecten Jávea; deelregels | Geen | Welke makelaars in Jávea willen eigen aanbod vóór brede publicatie delen? |
| **Operationele status** | **ALLEEN HANDMATIG** | **NIET GEBRUIKEN** | **CONTRACT OF TOESTEMMING NODIG** |

#### H. Banken, servicers en fondsen

Bron voor de invulling: R10 + verificatie. Bewijstype staat tussen haken in de cellen (1–7, masterprompt §5).

| Veld | R2-30 Servihabitat (particulieren en Servihabitat Profesionales) | R2-31 Solvia (Intrum; incl. voormalig Haya, Aktua, HRE) | R2-32 Diglo (servicer van Banco Santander) |
|---|---|---|---|
| Naam en officiële website | https://www.servihabitat.com/es/ · https://inversores.servihabitat.com/es/ | https://www.solvia.es | https://digloservicer.com |
| Type aanbieder | Servicer (Servihabitat Servicios Inmobiliarios, S.L.U., CIF B-66082629); eigenaar Coral Homes, verkoop aan Hipoges/Finsolutia gemeld (pers tegenstrijdig over closing, type 7) | Servicer (CIF A-86744349), Intrum; Haya opgegaan in Solvia (dec. 2024), haya.es gaf HTTP 522 (type 1/3) | Servicer, Diglo Servicer Company 2021, S.L. (B-67915298), '100% Grupo Banco Santander' (type 1) |
| Geografische en inhoudelijke dekking | 15-09-2026 publiek: Alicante 74 woningen (Marina Alta 0), 41 terreinen (Marina Alta 18, Jávea 0). Profesionales: Alicante 66 terreinen, Marina Alta 9, Jávea 2 percelen (één verkeerd ingedeeld onder 'huerta sur'); beide volgens de eigen pagina eigendom van Sareb (R10-verificatie, type 1/3) | 15-09-2026: Alicante 511 woningen, 202 suelos; Calp 17, Dénia 6, Benissa 4, Teulada 1; Jávea-pagina toont geen telling (waarschijnlijk 0, type 4). Ook particulier aanbod ('De tú a tú'), dus niet alles bankbezit (type 3) | 15-09-2026: Alicante 4 woningen, 20 bedrijfsruimtes, obras paradas geen getal zichtbaar; Jávea 0 (type 3) |
| Technische toegang | Server-gerenderde webpagina's; alerts, 'Guardar búsqueda', prijsdalingsmelding met account; professioneel portaal met 'Alta como profesional'. Geen API of feed (type 3) | Server-gerenderd; alerts na registratie; professioneel login. Geen API (robots.txt sluit /api/ uit) (type 3) | Server-gerenderd; persoonlijke alerts met account; geen API (type 3) |
| Beschikbare velden | Webfiches: type, oppervlak, planologische omschrijving volgens aanbieder, prijs, referenties | Webfiches met labels 'INMUEBLE DE BANCO', 'EN SITUACIÓN ESPECIAL' | Webfiches |
| Foto's en documenten | Fiches en pdf's per object (download pas na akkoord Jan) | Foto's op portaal | Foto's op portaal |
| Publicatie- en wijzigingsinformatie | Bijwerkdatum op fiche (bijv. 09-09-2026); geen publicatiedatum | ONBEKEND | ONBEKEND |
| Historische gegevens | Prijsdaling zichtbaar via Idealista (perceel Balcón al Mar 904.000 → 725.000 EUR) | ONBEKEND | ONBEKEND |
| Verversingsfrequentie | Alerts met account; frequentie ONBEKEND | Alerts 'al instante' volgens aanbieder (type 1) | Alerts met account |
| Rate limits | n.v.t. | n.v.t. | n.v.t. |
| Kosten | Gratis raadplegen; prijzen objecten exclusief belastingen en kosten koper (type 1) | Gratis raadplegen | Gratis raadplegen |
| Contractstatus | Geen account; samenwerkend makelaar ('API colaborador') voorwaarden ONBEKEND | Geen | Geen |
| Toegestane gebruiksdoelen | Handmatig en alerts. Voorwaarden: 'Queda prohibida cualquier modalidad de explotación' (type 1) | Aviso legal 4.4.2: zonder voorafgaande toestemming alleen 'para uso propio y personal', geen commerciële exploitatie (type 1) | Aviso legal: zonder voorafgaande toestemming verboden 'extracción y/o reutilización' (type 1) |
| Rechten AI-analyse | Niet zonder toestemming | Niet zonder toestemming | Niet zonder toestemming |
| Opslag en bewaren | Geen opslag van content zonder toestemming | Niet zonder toestemming | Niet zonder toestemming |
| Afgeleide gegevens en beeldvergelijking | Geen | Niet zonder toestemming | Niet zonder toestemming |
| Contactpersoon of aanvraagroute | Accounts via de portalen (door Jan); samenwerking als API colaborador navragen na akkoord Jan | Account via solvia.es (door Jan); /es/login-profesional | Account via digloservicer.com (door Jan) |
| Laatste verificatie | 15-09-2026 | 15-09-2026 | 15-09-2026 |
| Openstaande vragen | Afronding overname; betekenis productBrand 8003; planologische status perceel A (urbano no consolidado vs urbanizable); voorwaarden API colaborador | Verlenging CaixaBank-contract (2023, 3 jaar + 18 mnd); Jávea werkelijk 0? | Verhouding Diglo-mandaat (vastgoed + bestaande probleemleningen) en doValue-SLA (nieuwe NPL-stromen vanaf 2026) |
| **Operationele status** | **ALLEEN HANDMATIG** | **ALLEEN HANDMATIG** | **ALLEEN HANDMATIG** |

| Veld | R2-33 Overige servicer- en bankportalen (Sareb-zoekfunctie, Aliseda/Anticipa, Hipoges, Altamira/doValue, Unicaja, Cimenta2, EscogeCasa, Bankinter, Facilitea Casa, Banca March via Idealista) | R2-34 Leningen, NPL's en cesiones de remate (Aliseda NPL, Diglo 'Venta de Créditos', Hipoges, tussenpersonen) |
|---|---|---|
| Naam en officiële website | https://www.sareb.es/buscador-de-inmuebles/ · https://www.alisedainmobiliaria.com · https://realestate.hipoges.com/es · https://www.altamirainmuebles.com · https://unicajainmuebles.com · https://cimenta2.com · https://www.escogecasa.es · https://www.faciliteacasa.com | https://digloservicer.com/oportunidades/venta-credito · https://www.alisedainmobiliaria.com/inversion/prestamos-y-cesiones-remate/npls |
| Type aanbieder | Servicers, bad bank en vastgoedportalen van banken (type 1/3) | Verkoop van vorderingen en veilingposities, niet van vastgoed (type 1/3) |
| Geografische en inhoudelijke dekking | Geen live telling voor Jávea mogelijk. Aliseda-sitemap: 5.505 object-URL's landelijk en een categoriepagina 'terrenos Jávea/Xàbia' (geen telling). Banca March: 1 bankwoning (Calp) en 3 bankpercelen in Marina Alta via Idealista (R10-verificatie, type 3) | Landelijk; Aliseda sitemap-loans: 6.432 NPL-URL's (type 3) |
| Technische toegang | Sareb 403 (Imperva); Bankinter Cloudflare-controle; Altamira 403 voor bots, met browser alleen JavaScript; Aliseda, Hipoges, Anticipa, EscogeCasa, Cimenta2 alleen JavaScript; Unicaja-formulier gaf foutpagina bij direct verzoek (filter 'publicado última semana/mes' bestaat). Niet omzeild (type 3) | Webportalen; tussenpersonen (Inmubi, Fencia e.a.) zonder bevestigd mandaat |
| Beschikbare velden | ONBEKEND zonder browser | Kunnen tot schuldenaars herleidbaar zijn |
| Foto's en documenten | ONBEKEND | n.v.t. |
| Publicatie- en wijzigingsinformatie | Unicaja: filter laatste week/maand | n.v.t. |
| Historische gegevens | ONBEKEND | n.v.t. |
| Verversingsfrequentie | ONBEKEND | n.v.t. |
| Rate limits | Botbeveiliging | n.v.t. |
| Kosten | Gratis raadplegen | n.v.t. |
| Contractstatus | Geen | Geen |
| Toegestane gebruiksdoelen | Handmatig in browser (voorstel: ronde per kwartaal) | Niet in fase A: juridische beoordeling verplicht (rangorde lasten, bewoning, executieduur); geen persoonsprofielen (masterprompt §19) |
| Rechten AI-analyse | ONBEKEND; niet zonder toestemming | n.v.t. |
| Opslag en bewaren | ONBEKEND; niet zonder toestemming | Niet opnemen |
| Afgeleide gegevens en beeldvergelijking | ONBEKEND; niet zonder toestemming | n.v.t. |
| Contactpersoon of aanvraagroute | Per portaal; Facilitea Casa biedt makelaars kosteloze publicatie (publicatie ≠ lezen) | n.v.t. |
| Laatste verificatie | 15-09-2026 | 15-09-2026 |
| Openstaande vragen | Tellingen Jávea per portaal (handmatig); BBVA-kanaal 2026 (pers noemt Servihabitat, tegenstrijdig); afloop bezwaar Sareb Lot A | Pas na besluit Jan en advies advocaat |
| **Operationele status** | **ALLEEN HANDMATIG** | **NIET GEBRUIKEN** |

#### I. Veilingen, insolventie en overheidsverkopen

Bron voor de invulling: R08 + verificatie, R16. Bewijstype staat tussen haken in de cellen (1–7, masterprompt §5).

| Veld | R2-35 Portal de Subastas del BOE (gerechtelijk, notarieel, AEAT, SUMA, algemene administratieve veilingen) | R2-36 BOE open data — sumario-API en RSS (Sección IV justicia, V-B administratie) | R2-37 AEAT — downloadbare lijst te veilen goederen (bienes.js) |
|---|---|---|---|
| Naam en officiële website | https://subastas.boe.es/ | https://www.boe.es/datosabiertos/api/api.php · https://www.boe.es/rss/boe.php?s=4 | https://sede.agenciatributaria.gob.es/Sede/subastas.html |
| Type aanbieder | Officieel veilingportaal van de AEBOE (sede electrónica) (type 2) | Officiële open data van de AEBOE (type 2) | Officiële lijst van de belastingdienst (type 2/3) |
| Geografische en inhoudelijke dekking | Landelijk; niet de TGSS. 15-09-2026, Alicante, onroerend goed: 41 'próxima apertura' (21 gerechtelijk, 17 SUMA, 3 AEAT) en 41 'celebrándose' (38 gerechtelijk, 3 AEAT); Xàbia/Jávea 0; 0 van een Dénia-orgaan (R08-verificatie, type 3) | Alle dagelijkse BOE-aankondigingen: gerechtelijke veilingen (Sección IV), AEAT/SUMA/TGSS-patrimonium/Hacienda (V-B); Sección IV op 14-09-2026: 45 items | Alleen AEAT-veilingen, landelijk: 230 onroerende goederen (14-09-2026), 3 in Alicante (Orihuela 100 %, Dénia 25 %, Torrevieja 50 % blote eigendom), 0 in Xàbia (type 3) |
| Technische toegang | HTML-zoekformulier en detailpagina's; robots.txt 'Disallow: /', X-Robots-Tag noindex. Geen RSS, API of downloadlijst. E-mailalerts voor geregistreerde gebruikers, alleen natuurlijke personen, max. 50 zoekopdrachten; alert volgens help bij opening van de biedperiode, geen officiële notificatie (type 2/3) | Sumario-API per dag in XML én JSON (Accept-header verplicht; zonder header HTTP 400; vóór publicatie 404); RSS s=4 en s=5B (elk met één extra 'Sumario'-item). robots.txt sluit /diario_boe/xml.php? uit; txt.php-route niet (R08-verificatie, type 3) | Statisch JavaScript-databestand data2/bienes.js achter de AEAT-zoekpagina; pad niet gedocumenteerd (kan wijzigen) (type 3) |
| Beschikbare velden | Openbaar: identificatie, type, data, waarde, taxatie, minimumbod, depósito, derecho subastado, IDUFIR/CRU, referencia catastral, situación posesoria, visitable, cargas; aanvullende documenten na inloggen | identificador, titulo, url_pdf/html/xml, departamento. Aankondigingen bevatten alleen orgaan, nummer en portaallink — niet de plaats van het goed (LEC 646.1, RGR 101.3); prefixen SUB-JA, SUB-JC, SUB-AT, SUB-RC | id, subasta (SUB-AT), derecho, porcTitularidad, codProvincia, municipioCod, cp (getal zonder voorloopnul), direccion, refCatastro, cru, valoracion, cargas, finSubasta, descripcion, fotos, gpsLat/gpsLong (ontbreekt bij 29/230) |
| Foto's en documenten | Edicto, certificación de dominio y cargas, taxatie, registerinformatie (deels alleen ingelogd) (LEC 646.2, 667.2, 668.2) | Aankondigingstekst; geen objectdocumenten | Foto-verwijzingen (ontbreken bij 3/230) |
| Publicatie- en wijzigingsinformatie | Status PU/EJ/SU/CA/PC/FS; start- en einddatum; gekoppeld BOE-anuncio | Publicatiedatum BOE = source_published_at | Versiekop per dag ('Version: 20260914 15:23:07') |
| Historische gegevens | Afgelopen veilingen via status; geen export | Historische sumarios per datum (getest t/m 2022) | Geen; dagelijks bestand, eigen diff nodig |
| Verversingsfrequentie | Live | Dagelijks (ochtend); RSS doorlopend | Dagelijks (laatste versie circa 15:23) |
| Rate limits | Niet gepubliceerd; robots verbiedt alle bots | Niet gepubliceerd (FAQ niet toegankelijk) (type 7) | Niet gepubliceerd |
| Kosten | Gratis; waarborg bij bieden per kanaal verschillend | Gratis | Gratis |
| Contractstatus | Geen registratie | Niet nodig: hergebruiklicentie AEBOE | Niet nodig: kop vermeldt CC BY 4.0 |
| Toegestane gebruiksdoelen | Handmatig raadplegen en alerts. Hergebruiklicentie AEBOE (27-06-2024) geldt voor documenten in de sede, maar is geen toestemming om robots.txt te negeren (type 2/4) | Kopiëren, extraheren, combineren, ook commercieel, met bronvermelding 'Fuente de los datos: Agencia Estatal Boletín Oficial del Estado'; AVG bij persoonsgegevens (type 2) | Gebruik met bronvermelding 'Lista de bienes a subastar por la AEAT a <datum>' (type 2) |
| Rechten AI-analyse | Objectgegevens in dossier; geen namen van schuldenaren in doorzoekbare velden | Toegestaan binnen licentie en AVG | Toegestaan (CC BY 4.0) |
| Opslag en bewaren | Objectgegevens; persoonsgegevens alleen in afgeschermd biedingsdossier met verwijderdatum (R16 §6.2) | Toegestaan; persoonsgegevens minimaliseren | Toegestaan |
| Afgeleide gegevens en beeldvergelijking | Met bronvermelding; geen persoonsprofielen | Toegestaan met bronvermelding; niet 'desnaturalizar' | Toegestaan met naamsvermelding |
| Contactpersoon of aanvraagroute | Registratie door Jan (natuurlijk persoon); AEBOE voor toestemming gerichte detailraadpleging | https://www.boe.es/datosabiertos/ | AEAT-sede; 'Suscripción a avisos de nuevos bienes' achter authenticatie (niet getest) |
| Laatste verificatie | 15-09-2026 | 15-09-2026 | 15-09-2026 |
| Openstaande vragen | Gebruiksvoorwaarden voor geregistreerde gebruikers; toestemming AEBOE voor één detailverzoek per nieuw SUB-id | Rate limits; verschijnen Dénia-veilingen altijd onder titel 'DENIA' (centrale veilingdiensten elders gebruiken andere titel) | Stabiliteit van het pad; gemeentecode Xàbia in municipioCod |
| **Operationele status** | **ALLEEN HANDMATIG** | **TECHNISCH ONDERZOEK NODIG** | **TECHNISCH ONDERZOEK NODIG** |

| Veld | R2-38 TGSS — Subastas de Bienes Embargados (Seguridad Social) | R2-39 Registro Público Concursal en Portal de liquidaciones concursales | R2-40 subastasprocuradores.com (Consejo General de Procuradores) |
|---|---|---|---|
| Naam en officiële website | https://w6.seg-social.es/subastas/ | https://www.publicidadconcursal.es/ | https://www.subastasprocuradores.com/ |
| Type aanbieder | Officieel eigen veilingportaal van de TGSS, niet op het BOE-portaal (RGRSS art. 117.1) (type 2) | Officieel insolventieregister (type 2) | Entidad especializada voor realisatie van beslagen goederen (CGPE) (type 2) |
| Geografische en inhoudelijke dekking | TGSS-executieveilingen landelijk; live telling Alicante niet uitgevoerd (type 7) | Landelijk; liquidatieportaal toont vooral productie-eenheden, geen losse woningen (type 2/4) | Landelijk: subasta, venta directa, unidad productiva; live telling Alicante niet mogelijk zonder JavaScript-filter |
| Technische toegang | Servlet-zoekformulier (tipo de bien, tasación, cargas, provincie); geen RSS, e-mail, API of open data (type 3) | Zoeken op documento identificativo of per publicatiedag, met draai-captcha; geen RSS, API of open data (type 3) | HTML; robots.txt sluit alleen /error/ uit; geen RSS, alerts of API gezien (type 3) |
| Beschikbare velden | Anuncio met beschrijving, titularidad, tipo, lasten die blijven bestaan (art. 117.2) | Edictos, registrale publiciteit, akkoorden; liquidaties met modo de venta | Per lot volgens normas: edicto, tasación, certificación de cargas |
| Foto's en documenten | Inzage eigendomstitels op aangegeven plaats en tijd | Edictos | Documenten per lot |
| Publicatie- en wijzigingsinformatie | Zittingsdatum in anuncio | Publicatiedatum | Rubrieken 'Novedades', 'Próximamente' |
| Historische gegevens | ONBEKEND | Per zoekopdracht | ONBEKEND |
| Verversingsfrequentie | ONBEKEND | ONBEKEND | ONBEKEND |
| Rate limits | ONBEKEND | Captcha | ONBEKEND |
| Kosten | Gesloten envelop met gecertificeerde cheque van 25 % van het tipo; betaling binnen 5 werkdagen na adjudicatie (art. 117.2.g) (type 2) | Gratis | Commissie 4 % van de verkoopprijs bij onroerend goed (btw-status ONBEKEND); bij concursale activa volgens liquidatieplan (type 2) |
| Contractstatus | n.v.t. | n.v.t. | n.v.t.; registratie voor natuurlijke en rechtspersonen |
| Toegestane gebruiksdoelen | Handmatig raadplegen | Alleen voor wettelijke doelen; 'indexaciones o robotizaciones' verboden; hergebruik van persoonsgegevens uitdrukkelijk verboden (aviso legal §IV, §VII) (type 2) | Handmatig; voorwaarden over automatisering niet aangetroffen |
| Rechten AI-analyse | Objectgegevens in dossier | Geen persoonsgegevens verwerken | ONBEKEND |
| Opslag en bewaren | Objectgegevens; geen persoonsgegevens | Geen persoonsgegevens opslaan | ONBEKEND |
| Afgeleide gegevens en beeldvergelijking | Geen persoonsprofielen | Geen | ONBEKEND |
| Contactpersoon of aanvraagroute | Dirección Provincial TGSS | n.v.t. | Via website |
| Laatste verificatie | 15-09-2026 | 15-09-2026 | 15-09-2026 |
| Openstaande vragen | Telling Alicante (handmatig, wekelijks) | Welk platform een concreet concurso gebruikt (per dossier handmatig) | Voorwaarden voor geautomatiseerde raadpleging; meldingsdienst |
| **Operationele status** | **ALLEEN HANDMATIG** | **ALLEEN HANDMATIG** | **TECHNISCH ONDERZOEK NODIG** |

| Veld | R2-41 eActivos (Activos Concursales, S.L.) | R2-42 Ajuntament de Xàbia — tablón, perfil del contratante (PLACSP) en BOP Alicante |
|---|---|---|
| Naam en officiële website | https://www.eactivos.com/ | https://xabia.sedelectronica.es/board · https://www.ajxabia.com · https://sede.diputacionalicante.es/consultas-bop/ |
| Type aanbieder | Private entidad especializada, online veilingen (NIF B98206790, Valencia) (type 2) | Officiële gemeentelijke en provinciale publicaties (type 2/3) |
| Geografische en inhoudelijke dekking | Landelijk; concursal, judicial, extrajudicial | Xàbia; op 15-09-2026 op de eerste 10 publicaties van het tablón geen verkoop van gemeentelijk vastgoed (oudere publicaties niet doorzocht) (type 3) |
| Technische toegang | HTML met filters per provincie; aviso legal verbiedt 'sistemas mecanizados que sean distintos a personas físicas' (type 2) | Tablón HTML zonder RSS; perfil del contratante op PLACSP met dagelijkse Atom-open-data (of patrimoniale verkopen erin staan: [te verifiëren]); BOP-zoekfunctie op datum (type 2/3) |
| Beschikbare velden | Per veiling op de site | Publicaties; tablón bevat edictos met NIF's van schuldenaren — niet opslaan |
| Foto's en documenten | ONBEKEND | Pdf-publicaties |
| Publicatie- en wijzigingsinformatie | ONBEKEND | Publicatiedatum |
| Historische gegevens | ONBEKEND | Per publicatie |
| Verversingsfrequentie | ONBEKEND | PLACSP dagelijks; tablón en BOP doorlopend |
| Rate limits | Machinale toegang verboden | ONBEKEND |
| Kosten | ONBEKEND | Gratis |
| Contractstatus | n.v.t. | n.v.t. |
| Toegestane gebruiksdoelen | Alleen handmatig door een persoon; geautomatiseerd: NIET GEBRUIKEN (zo ook deliverable 04) | Handmatig (wekelijks); gemeentelijke vervreemding van patrimonium via openbare veiling (TRRL art. 80) met voorafgaande taxatie (RBEL art. 118) (type 2) |
| Rechten AI-analyse | Niet geautomatiseerd | Objectgegevens |
| Opslag en bewaren | ONBEKEND | Geen persoonsgegevens |
| Afgeleide gegevens en beeldvergelijking | Inhoud auteursrechtelijk voorbehouden | Met bronvermelding |
| Contactpersoon of aanvraagroute | Via website | Ajuntament de Xàbia |
| Laatste verificatie | 15-09-2026 | 15-09-2026 |
| Openstaande vragen | Geen | Publiceert Xàbia patrimoniale verkopen op PLACSP? Doet Xàbia zelf invordering in vía de apremio en veilt het zelf? |
| **Operationele status** | **ALLEEN HANDMATIG** | **ALLEEN HANDMATIG** |

#### J. Perceel-, register- en marktcontext

Bron voor de invulling: R11, R04 + verificaties, R16. Bewijstype staat tussen haken in de cellen (1–7, masterprompt §5).

| Veld | R2-43 Catastro — vrije webservices en INSPIRE (WFS, WMS, ATOM) | R2-44 Catastro Sede Electrónica — perceelpagina, PDF, valor de referencia, massadownload | R2-45 Registro de la Propiedad — nota simple en certificación |
|---|---|---|---|
| Naam en officiële website | https://ovc.catastro.meh.es · https://www.catastro.hacienda.gob.es/webinspire/index.html | https://www1.sedecatastro.gob.es/Accesos/SECAccvr.aspx | https://www.registradores.org/el-colegio/registro-de-la-propiedad · https://sede.registradores.org/ |
| Type aanbieder | Officiële kadastrale diensten, Dirección General del Catastro (type 2) | Officiële interactieve diensten Catastro (type 2) | Openbaar eigendomsregister via Colegio de Registradores (type 2) |
| Geografische en inhoudelijke dekking | Heel Spanje behalve eigen regimes; Xàbia INE 03082. Identificatie en geometrie per perceel, geen objectaanbod en geen eigenaar of waarde (type 3) | Per object | Per finca; eigendom, beschrijving, lasten |
| Technische toegang | Zonder sleutel: coördinaat → RC (RCCOOR en afstandsvariant), RC → gegevens (DNPRC), adres → RC (DNPLOC); JSON/REST-varianten gebruiken ongedocumenteerde parameters CoorX/CoorY en RefCat. WFS zonder paginering (kop 486, inhoud 477 percelen — zelf tellen); WMS niet voor massale of tegelverzoeken; ATOM Xàbia in EPSG:25831, bijgewerkt 21-08-2026. www.catastro.hacienda.gob.es werkt met httpx, niet met curl/urllib (FNMT-keten) (R11-verificatie, type 3) | Perceelpagina en PDF 'Consulta descriptiva y gráfica' (20-tekens-RC) zonder login; valor de referencia met certificaat/DNIe of Cl@ve; massadownload CAT/Shapefile met certificaat en licentie (Resolución 23-03-2011) (type 2/3) | Sede (JavaScript-app, bestellen met login aannemelijk); geen openbare API gevonden; Geoportal functie en login ONBEKEND (type 3/7) |
| Beschikbare velden | RC, adres, gebruik (luso), gebouwde m² (sfc), bouwjaar (ant), perceel-m² (ss), perceeltype (ltp alleen bij bebouwd), geometrie, referentiepunt, gevelfoto | Perceelgegevens; valor de referencia per datum (na identificatie) | Beschrijving finca, titularidad, cargas; wettelijk ook RC en coördinatiestatus met Catastro (LH art. 10.4) — praktijk te controleren |
| Foto's en documenten | Gevelfoto, WMS-kaartbeeld | PDF-croquis ('no es una certificación catastral') | Nota simple (informatief), certificación (bewijskrachtig) |
| Publicatie- en wijzigingsinformatie | beginLifespanVersion per perceel | Waardekaarten 2026 gepubliceerd 09-10-2025 | Per aanvraag; 'nota online' 10 dagen live inzage |
| Historische gegevens | Beperkt (versiedatum geometrie) | Valor de referencia 2022–2026 | Per finca |
| Verversingsfrequentie | Webservices en WFS actueel; ATOM 2 keer per jaar | Jaarlijks (waarde) | Levertijd tegenstrijdig: 'en el plazo de 24 horas' tegenover 'plazo medio inferior a dos horas' (type 7) |
| Rate limits | Drempel niet gepubliceerd; bij overschrijding weigering van de dienst 'generalmente 10 días'; limieten op gelijktijdige toegang (condiciones de uso) (type 2) | Interactieve diensten niet automatisch of massaal gebruiken (condiciones de uso) (type 2) | Legitiem belang vereist; aanvrager wordt 3 jaar geregistreerd |
| Kosten | Gratis | Gratis | Nota simple 9,02 EUR + btw; nota online 12,03 EUR + btw (Colegio, type 2); arancel-basis 3,005061 EUR/finca |
| Contractstatus | Niet nodig; INSPIRE-licentie v1.0 (juli 2016) | Licentie bij massadownload | n.v.t. |
| Toegestane gebruiksdoelen | Eigen gebruik en nieuwe producten na transformatie; geen verspreiding van originele informatie; eigen product niet 'cartografía/información catastral' noemen; bronvermelding DGC (type 2) | Handmatige controlestap per bevestigd dossier | Per kandidaatobject met opgave van reden; makelaars hebben vermoeden van legitiem belang (RH 332.3) (type 2) |
| Rechten AI-analyse | Toegestaan voor eigen gebruik | Per dossier | Binnen het dossier |
| Opslag en bewaren | Toegestaan (cache per RC) | PDF in dossier | Alleen in objectdossier; eigenaarsnamen afgeschermd met verwijderdatum |
| Afgeleide gegevens en beeldvergelijking | Toegestaan na transformatie; originele data niet ongewijzigd aan klanten doorgeven [advocaat] | Massadownload alleen na transformatie; beschermde gegevens (eigenaar, valor catastral) niet (TRLCI 51, 53) | Geen opname in databank voor commercialisering of doorverkoop (RH 332.2) (type 2) |
| Contactpersoon of aanvraagroute | Dirección General del Catastro (bij opschaling schriftelijke bevestiging vragen) | Sede; Cl@ve van Jan of gestor | registradores.org; soporte.usuarios@corpme.es, 912 701 796 (zakelijk) |
| Laatste verificatie | 15-09-2026 | 15-09-2026 | 15-09-2026 |
| Openstaande vragen | Concrete verzoekdrempel; vallen de vrije webservices onder 'servicios interactivos'? | Mag een niet-eigenaar de valor de referencia van elk object opvragen? Openen de waardekaarten zonder Cl@ve? | Werkelijke levertijd en inhoud (RC, coördinatiestatus) bij eerste bestelling |
| **Operationele status** | **TECHNISCH ONDERZOEK NODIG** | **ALLEEN HANDMATIG** | **ALLEEN HANDMATIG** |

| Veld | R2-46 MIVAU — Transacciones inmobiliarias en Valor tasado | R2-47 INE — Índice de Precios de Vivienda en Transmisiones de Derechos de la Propiedad | R2-48 Portal Estadístico del Notariado (penotariado.com) |
|---|---|---|---|
| Naam en officiële website | https://apps.fomento.gob.es/BoletinOnline2/?nivel=2&orden=34000000 | https://servicios.ine.es/wstempus/js/ES/TABLAS_OPERACION/IPV | https://www.penotariado.com/ |
| Type aanbieder | Officiële statistiek ministerie van huisvesting (type 2) | Officiële statistiek (type 2) | Officiële statistiek notariaat (type 2) |
| Geografische en inhoudelijke dekking | Transacties: per gemeente alleen het AANTAL (Jávea/Xàbia aanwezig); waarde en gemiddelde waarde alleen per regio en provincie. Valor tasado: gemeenten boven 25.000 inwoners (Jávea, Calp, Dénia) (R04-verificatie, type 3) | IPV alleen nationaal en per autonome regio (2T 2026 +12,2 % j/j nationaal); ETDP tot provincie, geen gemeenten (type 3) | Werkelijke koopsommen per land, regio, provincie, gemeente, postcode en zelf getekend gebied, 'siempre que los datos lo permitan' (type 2) |
| Technische toegang | XLS per gemeente (Boletín Online); open CSV alleen provincie; lokaal geen XLS-lezer (installatie vergt akkoord Jan) | INE-API zonder sleutel (getest) (type 3) | Web en kaart; gratis vrijwillige registratie; download van grafieken, geen ruwe data of API gezien (type 3) |
| Beschikbare velden | Aantal transacties (totaal, vrij, beschermd, nieuw, tweedehands); taxatiewaarde EUR/m² | Indexen en aantallen | Prijs per m², oppervlak, totaalprijs, aantal verkopen |
| Foto's en documenten | n.v.t. | n.v.t. | Grafieken/rapporten |
| Publicatie- en wijzigingsinformatie | Kwartaal; voorlopig en definitief | Publicatiedata per operatie | Maandelijks |
| Historische gegevens | Reeksen per kwartaal | Reeksen | Reeksen |
| Verversingsfrequentie | Kwartaal, vertraging ruim een kwartaal (data t/m 2026-T1) | IPV per kwartaal; ETDP maandelijks met circa één maand vertraging | Maandelijks |
| Rate limits | n.v.t. | Niet gepubliceerd | n.v.t. |
| Kosten | Gratis | Gratis | Gratis |
| Contractstatus | n.v.t. | n.v.t. | n.v.t. |
| Toegestane gebruiksdoelen | CC BY 4.0 op de provinciale CSV's (datos.gob.es); licentie van de gemeentelijke XLS niet vastgesteld [te verifiëren] | Hergebruik met bronvermelding | Alleen persoonlijk gebruik; geen commercieel gebruik; geen opname in databanken voor commerciële raadpleging door derden, ook niet met bronvermelding (type 2) |
| Rechten AI-analyse | Toegestaan met bronvermelding (CSV) | Toegestaan | Niet als datafeed |
| Opslag en bewaren | Toegestaan (CSV) | Toegestaan | Niet in database; hooguit handmatige toets met datum in één dossier [advocaat] |
| Afgeleide gegevens en beeldvergelijking | Toegestaan met bronvermelding (CSV) | Toegestaan met bronvermelding | Niet |
| Contactpersoon of aanvraagroute | datos.gob.es / MIVAU | ine.es | penotariado.com |
| Laatste verificatie | 15-09-2026 | 15-09-2026 | 15-09-2026 |
| Openstaande vragen | Licentie gemeentelijke XLS; bron ANCERT niet bevestigd | Geen; alleen marktrichting, geen objectwaarde | Bestaat een commerciële licentie van het Consejo General del Notariado? |
| **Operationele status** | **TECHNISCH ONDERZOEK NODIG** | **TECHNISCH ONDERZOEK NODIG** | **ALLEEN HANDMATIG** |

| Veld | R2-49 Registradores — Estadística Registral Inmobiliaria (en open-dataportaal) |
|---|---|
| Naam en officiële website | https://www.registradores.org/actualidad/portal-estadistico-registral |
| Type aanbieder | Statistiek van het Colegio de Registradores (type 2) |
| Geografische en inhoudelijke dekking | Land, regio, provincie en provinciehoofdsteden; geen gemeentecijfers Jávea; rapporten t/m 2T 2026 (type 2/3) |
| Technische toegang | PDF-rapporten; opendata.registradores.org weigert onze verzoeken ('Request Rejected'), niet omzeild (type 3) |
| Beschikbare velden | Compraventas, EUR/m², herhaalde verkopen, hypotheken, buitenlandse kopers |
| Foto's en documenten | PDF |
| Publicatie- en wijzigingsinformatie | Kwartaal |
| Historische gegevens | Jaarboeken 2004–2025 |
| Verversingsfrequentie | Kwartaal |
| Rate limits | WAF-blokkade voor tools |
| Kosten | Gratis |
| Contractstatus | n.v.t. |
| Toegestane gebruiksdoelen | Handmatig overnemen met bron; licentie open data niet vermeld |
| Rechten AI-analyse | ONBEKEND |
| Opslag en bewaren | ONBEKEND |
| Afgeleide gegevens en beeldvergelijking | ONBEKEND |
| Contactpersoon of aanvraagroute | contacto@registradores.org |
| Laatste verificatie | 15-09-2026 |
| Openstaande vragen | Fijnmazigheid open-dataportaal (handmatig in browser) |
| **Operationele status** | **ALLEEN HANDMATIG** |

#### K. Makelaars, netwerken, ontwikkelaars en eigen dealflow (masterprompt §9)

Bron voor de invulling: R06 (controledatum 14-09-2026) en R06-verificatie (15-09-2026), R07 en R07-verificatie (14-09-2026), R05 §1.2 (BP-partnerlijst). Bewijstype staat tussen haken in de cellen (1–7, masterprompt §5). Waar de verificatie R06 of R07 corrigeerde, staat hier de gecorrigeerde versie.

| Veld | R2-50 Lokale makelaarssites in en rond Jávea (kantorenregister K-1) | R2-51 Directories en gemeentelijke lijst (xabia.org, Trustlocal, Javea Guide, Jávea.com) | R2-52 Rechtstreekse aanlevering door makelaars, ontwikkelaars en architecten (eigen dealflow) |
|---|---|---|---|
| Naam en officiële website | Per kantoor in tabel K-1 | https://www.xabia.org/ver/2098/Real-estate-agents-and-promoters.html · https://trustlocal.es/alacant-alicante/xabia-javea/agencia-inmobiliaria/ · https://www.javeaguide.com/javea-estate-agents · https://en.javea.com/zona/comercios/inmobiliaria/agencia-inmobiliaria/ | Nog geen; voorstel: formulier in GoHighLevel plus pdf (R07 §5.2) |
| Type aanbieder | Makelaarskantoren, ketens en bouwers met verkoop, in Jávea en in buurgemeenten met Jávea-aanbod (1/3) | Gemeentelijke publicatie (xabia.org, type 2) en commerciële directories (type 1) | Eigen inbound-kanaal van TREE voor professionele partners (voorstel, type 4) |
| Geografische en inhoudelijke dekking | 79 kantoren in K-1 (50 in Jávea, 25 erbuiten, 4 aanvullingen) plus 48 alleen op naam bekend. Jávea-aantallen alleen van eigen sites en momentopnames, bijv. Paradise 225, Arzuaga 225, Holidaydream 71, Casas Ambiente 42; E&V 109 is het hele netwerk in de gemeente (R06, R06-verificatie; 1/3) | xabia.org: 39 bedrijven, makelaars en promotoren door elkaar, geen totaal op de pagina (R07-verificatie R07-07, 2/3). Trustlocal: "95 opciones verificadas" (eigen label; ook Casasdediez, Bindley, Select Villas of Moraira). Javea Guide: 44 met adres. Jávea.com: circa 25 profielen incl. verhuurders en bouwers (7) | Jávea/Xàbia plus Benitatxell, Dénia, Gata de Gorgos, Teulada-Moraira; categorieën renovatie, perceel en ontwikkeling, bijzondere verkoop (R07 §5.1, werkhypothese) |
| Technische toegang | Alleen browser. Geen open XML/JSON-aanbodfeed gezien (negatieve bewering, niet reproduceerbaar: 7). Botcontrole "Security Check" (Paagees Shield) ook bij Sooprema-sites; Cloudflare bij Lucas Fox en Spanienobjekte. Aanbiederpagina's van Idealista, Kyero, Indomio en yaencontre: HTTP 403 (R06-verificatie R06-03, R06-19, A4; 3) | Open web (HTML); geen API of export gezien (3) | Niet gebouwd. 24 velden in vier blokken: partner, object, documenten, afspraken (R07 §5.2) |
| Beschikbare velden | Webfiches (prijs, type, zone, m², referentie). Kantoorreferenties helpen bij ontdubbelen: CBS… (Coldwell Banker Solaris), KV… (Koch & Varlet), BP-referentie 4676JAV bij drie kantoren (R07-verificatie A3; 3) | Naam, adres, website (xabia.org); beoordelingen (Trustlocal) | Partner met RAICV- of colegiado-nummer of CIF, rol en mandaat; object met zone, adres of referencia catastral, staat, m² met bron, prijs, licentiestatus, "al gepubliceerd?" |
| Foto's en documenten | Foto's op de sites; rechten bij kantoor, fotograaf of eigenaar; documenten niet gezien | n.v.t. | Foto's, plattegronden, nota simple, IBI, energielabel, licentie en project (verplicht vóór een bod) |
| Publicatie- en wijzigingsinformatie | ONBEKEND per site | Geen bijwerkdatum gezien; adressen deels tegenstrijdig met kantoorsites (E&V, InmoVillas: 7) | Aanleverdatum; publicatiestatus volgens partner |
| Historische gegevens | Geen | Geen | Eigen dossier |
| Verversingsfrequentie | ONBEKEND | ONBEKEND | Per aanlevering; TREE-termijnen 1 / 5 / 10 werkdagen, terugkoppeling elke 2 weken (voorstel) |
| Rate limits | Botcontroles; geen gepubliceerde limieten | ONBEKEND | n.v.t. |
| Kosten | Gratis raadplegen | Gratis | Vergoeding introducers ONBEKEND (besluit Jan); listing agent houdt eigen commissie (voorstel) |
| Contractstatus | Geen afspraak met enig kantoor gevonden | n.v.t. | Geen. Per partner een samenwerkingsbrief of nota de encargo en een geheimhoudingsafspraak (tekst advocaat); rechtenvelden volgens sjabloon R16 §6.3 |
| Toegestane gebruiksdoelen | Handmatig raadplegen. Een openbare site of sitemap is geen gebruikslicentie (masterprompt §7); geautomatiseerd uitlezen niet zonder toestemming van het kantoor (4) | Handmatig, als startvoorraad voor het kantorenregister; geen bulkcontact (masterprompt §26) | Eigen acquisitiebeoordeling; geen publicatie of doorgifte; verkoper niet buiten de partner om (voorstel R07 §5.3) |
| Rechten AI-analyse | Niet buiten een handmatige sessie zonder afspraak | Zakelijke gegevens van kantoren in eigen register (LOPDGDD art. 19, type 2) | In de samenwerkingsafspraak op te nemen [te verifiëren] |
| Opslag en bewaren | Link, referentie en eigen notities; geen kopie van teksten of foto's zonder afspraak (lijn R16 §3.8, type 4) | Alleen zakelijke gegevens van kantoren; geen persoonsgegevens van particulieren | In GoHighLevel (CRM van waarheid, ADR-0014); bewaartermijn per afspraak |
| Afgeleide gegevens en beeldvergelijking | Geen beeldvergelijking zonder afspraak | n.v.t. | Per afspraak |
| Contactpersoon of aanvraagroute | Per kantoor via website of contactformulier; eerste contact telefonisch of persoonlijk (R07 §4.2) | n.v.t. | Per partner; e-mail pas na uitdrukkelijke instemming, met afmeldmogelijkheid (LSSI art. 21) |
| Laatste verificatie | 15-09-2026 (steekproef R06-verificatie); overige kantoren 14-09-2026 | 15-09-2026 (Trustlocal, Javea Guide, Jávea.com); 14-09-2026 (xabia.org) | 14-09-2026 |
| Openstaande vragen | Welke kantoren hebben uniek aanbod (ontdubbelmeting)? Wie wil vóór brede publicatie delen? Wie zit achter de referenties "LTV…"? Zijn Costa Houses, Lucas Fox, Villas-Plots, Signature Villas, Spanienobjekte en Inmobiliaria Javea in een gewone browser bereikbaar? Welke alleen-op-naam-kantoren zijn nog actief? | Actualiteit van de gemeentelijke lijst; welke Javea Guide-kantoren nog actief zijn | RAICV-nummer TREE Properties; prijsklassen; finder's fee; eigenaar van de termijnen; aanspreekvorm; jaartal 2022 of 2023 in berichten; valt een introducer zonder mandaat zelf onder de registerplicht (R07-verificatie A2)? |
| **Operationele status** | **ALLEEN HANDMATIG** (export of aanlevering per kantoor: CONTRACT OF TOESTEMMING NODIG) | **ALLEEN HANDMATIG** (R07: "GEVERIFIEERD EN ACTIEF (handmatig)"; hier strenger) | **CONTRACT OF TOESTEMMING NODIG** |

| Veld | R2-53 MLS Dénia | R2-54 ASICVAL (Asociación de Inmobiliarias de la Comunitat Valenciana) | R2-55 RAICV — Registro de Agentes de Intermediación Inmobiliaria de la Comunitat Valenciana |
|---|---|---|---|
| Naam en officiële website | https://www.mlsdenia.com/en/about-us/ | https://asicval.es/ | https://habitatge.gva.es/es/registres-en-materia-habitatge · https://sede.gva.es/es/detall-tramit?id_proc=22848 |
| Type aanbieder | MLS-vereniging zonder winstoogmerk, opgericht 30-01-2014, CIF G-54768957 (1) | Vereniging van makelaarskantoren (1) | Verplicht openbaar register van de Generalitat Valenciana; grondslag Ley 2/2017 DA 6ª, uitwerking Decreto 98/2022 (2) |
| Geografische en inhoudelijke dekking | Dénia en omliggende gemeenten; "20 agencies" (about-us) tegenover "more than 25 collaborating agencies" (partnerpagina Dénia Casas): tegenstrijdig (7). Jávea bestaat als filteroptie "Localidad" (1) | Castellón, Valencia, Alicante; "400 agencias asociadas", "430 puntos de venta", "1317 inmuebles en exclusiva", zonder peildatum (R07-verificatie R07-06, 1); Jávea-aandeel ONBEKEND | Alle bemiddelaars in de Comunitat Valenciana; verplicht sinds 16-10-2022 (2) |
| Technische toegang | Lidmaatschap "upon request and approval" (kwalificatie, opleiding, ervaring); openbare zoekfunctie op de site (1) | Lidmaatschap via "ASÓCIATE"; werkwijze "exclusiva compartida" (1) | Raadpleegformulier (sforms.gva.es, formulier 62953) laadt via JavaScript; niet machinaal gelezen, niet omzeild (3/7) |
| Beschikbare velden | ONBEKEND | ONBEKEND | Registernummer; overige velden ONBEKEND |
| Foto's en documenten | ONBEKEND | ONBEKEND | n.v.t. |
| Publicatie- en wijzigingsinformatie | ONBEKEND | ONBEKEND | ONBEKEND |
| Historische gegevens | ONBEKEND | ONBEKEND | ONBEKEND |
| Verversingsfrequentie | ONBEKEND | ONBEKEND | ONBEKEND |
| Rate limits | ONBEKEND | ONBEKEND | ONBEKEND |
| Kosten | Niet gepubliceerd | Niet gepubliceerd; leden kunnen aansluiten bij collectieve polissen voor borg en aansprakelijkheid (1) | Register "gratuito" (Decreto 98/2022 art. 4.1, 2); inschrijvingseisen: opleiding, kantoor of fysiek adres, borg 60.000 EUR per vestiging, aansprakelijkheid 600.000 EUR per schadegeval (2) |
| Contractstatus | Geen; lidmaatschap TREE ONBEKEND | Geen | n.v.t. |
| Toegestane gebruiksdoelen | Als lid: exclusief aanbod delen in de "real estate pool" volgens de verenigingsregels, met de plicht eigen exclusieven te delen (1/4) | Als lid volgens de verenigingsregels; delen vóór publicatie niet vermeld (7) | Controle van partners vóór samenwerking; het nummer hoort in reclame en in de nota de encargo (Ley 2/2017 DA 6ª.4; Decreto 98/2022 art. 3; 2) |
| Rechten AI-analyse | ONBEKEND | ONBEKEND | n.v.t. |
| Opslag en bewaren | ONBEKEND | ONBEKEND | Registernummer per partner in het CRM (zakelijk gegeven) |
| Afgeleide gegevens en beeldvergelijking | ONBEKEND | ONBEKEND | n.v.t. |
| Contactpersoon of aanvraagroute | info@mlsdenia.com | Via asicval.es | habitatge.gva.es (raadplegen in de browser) |
| Laatste verificatie | 14-09-2026 | 14-09-2026 | 14-09-2026 |
| Openstaande vragen | Toetredingseisen voor TREE (RAICV), contributie, commissieverdeling, ledenlijst, aandeel Jávea-aanbod; is het dezelfde vereniging als "MLS Denia Realtor" in R2-26? | Voorwaarden, contributie, leden in Jávea | Staat TREE Properties ingeschreven en met welk nummer? Welke velden toont de raadpleging? Exacte tekst van de uitzonderingen in art. 2 (R07-verificatie A2, [te verifiëren]) |
| **Operationele status** | **CONTRACT OF TOESTEMMING NODIG** | **CONTRACT OF TOESTEMMING NODIG** | **ALLEEN HANDMATIG** |

| Veld | R2-56 Ontwikkelaarssites met Jávea-projecten (tabel K-2) | R2-57 PROVIA (Asociación de Promotores Inmobiliarios de la Provincia de Alicante) | R2-58 Architecten-colegios: CTAA "Bolsa de servicios al ciudadano" en COAT Alicante |
|---|---|---|---|
| Naam en officiële website | Zie tabel K-2 | https://provia.es/ | https://www.ctaa.net/bolsa-servicios-ciudadanos · COAT: aparejadoresalicante.org |
| Type aanbieder | Promotoras en bouwbedrijven (1) | Brancheorganisatie van promotoren (1) | Beroepsorden van architecten en aparejadores (1) |
| Geografische en inhoudelijke dekking | Zeven partijen met bevestigde Jávea-projecten of percelen direct naast Jávea (R07-verificatie R07-09 t/m R07-12, 1) | Provincie Alicante; geen openbare ledenlijst (/asociados/ gaf 404); homepage toont leveranciers en partners, geen promotoren (R07-verificatie A13, 1) | CTAA: architecten per specialisme en plaats, achter inlog als arquitecto, ciudadano of empresa (R07-verificatie A12, 1). COAT: bestaan van een openbaar ledenregister niet vastgesteld (7) |
| Technische toegang | Open web; geen feeds of exports gezien (3) | Website; contact per telefoon | CTAA: registratie vereist. COAT: certificaatfout volgens R07, HTTP 301 volgens de verificatie; niet gevolgd (7) |
| Beschikbare velden | Projectpagina's: aantal woningen, fase, vanafprijs + IVA, licentiestatus (1) | n.v.t. | ONBEKEND |
| Foto's en documenten | Projectbeelden; documenten niet gezien | n.v.t. | ONBEKEND |
| Publicatie- en wijzigingsinformatie | Fase per project; momentopname (Living Jávea: 11 van 20 beschikbaar volgens R07, 12 van 20 volgens de verificatie) | n.v.t. | ONBEKEND |
| Historische gegevens | Geen | n.v.t. | ONBEKEND |
| Verversingsfrequentie | ONBEKEND | n.v.t. | ONBEKEND |
| Rate limits | n.v.t. | n.v.t. | ONBEKEND |
| Kosten | Gratis raadplegen | Lidmaatschap niet gepubliceerd | ONBEKEND |
| Contractstatus | Geen | Geen | Geen |
| Toegestane gebruiksdoelen | Handmatig; kwartaalcontrole projectstatus (voorstel R07); relatie voor route B, C en D | Netwerkkanaal | Architecten vinden voor de partnerlijn "proyecto sin cliente" (4); geen van zes onderzochte bureaus bemiddelt percelen (1) |
| Rechten AI-analyse | Niet buiten een handmatige sessie zonder afspraak | n.v.t. | ONBEKEND |
| Opslag en bewaren | Link en eigen notities; zakelijke contactgegevens (LOPDGDD art. 19) | Zakelijke contactgegevens | Zakelijke contactgegevens |
| Afgeleide gegevens en beeldvergelijking | Geen zonder afspraak | n.v.t. | n.v.t. |
| Contactpersoon of aanvraagroute | Via de eigen sites (zakelijk) | Via provia.es | colegio@ctaa.net (CTAA) |
| Laatste verificatie | 14-09-2026 | 14-09-2026 | 14-09-2026 |
| Openstaande vragen | Promotor van Blooming Village en Lemon Residence; Marina Bay I en II (alleen zoekresultaat); stilgevallen projecten alleen via architecten, BOP-publicaties en veilingen (R07 §2.4, 4) | Welke promotoren met Jávea-grond zijn lid? | Werking van de CTAA-bolsa; bereikbaarheid en register van COAT Alicante |
| **Operationele status** | **ALLEEN HANDMATIG** | **ALLEEN HANDMATIG** | **TECHNISCH ONDERZOEK NODIG** |

| Veld | R2-59 Wallapop (inmobiliaria) en Facebook-groepen |
|---|---|
| Naam en officiële website | https://es.wallapop.com/inmobiliaria/javea · https://about.wallapop.com/en/legal-terms-and-conditions/ · https://www.facebook.com/legal/terms |
| Type aanbieder | Advertentieplatform voor particulieren en professionals; sociaal platform (1) |
| Geografische en inhoudelijke dekking | Wallapop Jávea: 30–35 advertenties, mix van particulieren en professionals, van 60 EUR/maand (garage) tot 3.610.000 EUR (14-09-2026, R07-verificatie A16, 1). Facebook-groepen: bestaan en omvang ONBEKEND (7) |
| Technische toegang | Wallapop: open web. Facebook: alleen ingelogd, per groep |
| Beschikbare velden | Webweergave per advertentie |
| Foto's en documenten | Foto's op het platform |
| Publicatie- en wijzigingsinformatie | ONBEKEND |
| Historische gegevens | Geen |
| Verversingsfrequentie | ONBEKEND |
| Rate limits | n.v.t.; geautomatiseerde toegang verboden |
| Kosten | Lezen gratis; zakelijk gebruik van Wallapop via Business-account (1) |
| Contractstatus | Geen |
| Toegestane gebruiksdoelen | Handmatig lezen; reageren op één concrete advertentie via het platform. Wallapop (versie 10-04-2026): "Not to systematically extract or reuse part or all of the content of the Platform, without our express written consent". Meta (01-01-2025) 3.2.3: geen geautomatiseerde verzameling zonder toestemming (R07-verificatie R07-18, 1) |
| Rechten AI-analyse | Niet buiten een handmatige sessie |
| Opslag en bewaren | Alleen objectkenmerken en advertentie-URL; geen naam of telefoon van particulieren (R07 §4.3) |
| Afgeleide gegevens en beeldvergelijking | Geen |
| Contactpersoon of aanvraagroute | n.v.t.; geen bulkberichten en geen massabenadering van particulieren (LSSI art. 21; masterprompt §26) |
| Laatste verificatie | 14-09-2026 |
| Openstaande vragen | Welke lokale Facebook-groepen bestaan en wat staan hun regels toe? |
| **Operationele status** | **ALLEEN HANDMATIG** (scrapers voor deze platforms: R2-17, NIET GEBRUIKEN) |

##### Tabel K-1 — Kantorenregister Jávea/Xàbia

**Legenda.** *Platform/CRM*: zoals zichtbaar in de HTML (credit, assetpad, botcontrole), gecorrigeerd volgens de R06-verificatie (type 3; het onderliggende CRM kan afwijken). *Renovatie* en *Percelen*: "rubriek ✓" = eigen rubriek of filter gezien; "object(en)" = renovatieobject of perceel zichtbaar zonder aparte rubriek, of met kantoornaam in een Idealista-advertentie (type 1); "–" = niet gezien. *Bank*: rubriek of filter voor bankvastgoed; inhoud nergens gecontroleerd. *Uniek aanbod*: "nee" = aantoonbaar gedeeld (3 of eigen claim 1); "vermoedelijk nee" = afgeleid uit omvang, MLS-platform of beeldbronnen (4); "ONBEKEND" = niet gemeten (claims over exclusiviteit zijn type 1 en niet bevestigd, masterprompt §9). *Feed/export*: "–" = geen open feed gezien (negatieve bewering, type 7); een sitemap is geen licentie. *Prioriteit* (voorstel, type 4): 1 = verkoopt nu aantoonbaar percelen met project of licentie (R07 §5.3 stap 1); 2 = eerste ring R06 §8 (eigen referenties of percelen/renovatie zichtbaar); 3 = tweede ring R06 §8 (groot, vermoedelijk gedeeld aanbod); O = bouwer of ontwikkelaar; – = geen voorstel. *Status*: voor het raadplegen van de site; een export of aanlevering van welk kantoor dan ook valt onder R2-52 (CONTRACT OF TOESTEMMING NODIG). *Gezien*: controledatum in R06 (14-09-2026) of in de R06-verificatie of R07 (15-09-2026 / 14-09-2026). Telefoonnummers en straatadressen staan in R06; hier alleen de plaats (R06-verificatie F17). "BP-partner" = staat op de partnerlijst van Background Properties (R05 §1.2, type 1).

| # | Kantoor | Website | Plaats | Platform/CRM | Renovatie | Percelen | Bank | Uniek aanbod | Feed/export | Prio | Status | Gezien |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Background Properties | backgroundproperties.com | Jávea | WordPress + Houzez | Enkele objecten met potentieel (bijv. 4544JAV splitsbaar) | 24 percelen Jávea in de feed | – | nee: listingdienst voor 41 kantoren; 6 van 6 geteste objecten ook op Idealista (3) | Privé Kyero v3-feed (R2-01) | – | CONTRACT OF TOESTEMMING NODIG | 15-09 |
| 2 | Costa Houses Luxury Villas | costa-houses.com (vanaf deze Mac onbereikbaar) | Jávea, Moraira | ONBEKEND | ONBEKEND | 1 perceel met naam (Idealista); perceel met "proyecto y licencia" in Balcón al Mar alleen via zoekresultaat (7) | ONBEKEND | ONBEKEND | ONBEKEND | – | TECHNISCH ONDERZOEK NODIG | 14-09 |
| 3 | Moraguespons | moraguespons.com | Jávea | ONBEKEND | rubriek ✓ (/venta/villa/javea/a-reformar/); 1 object (Idealista) | rubriek ✓ | – | ONBEKEND (claimt "exclusieve selectie") | – | 2 | ALLEEN HANDMATIG | 15-09 |
| 4 | Rimontgó (Forbes Global Properties) | rimontgo.com | Jávea | Eigen site | – | rubriek ✓; perceel met bouwvergunning en project (Montgó) | – | ONBEKEND | – | 1 | ALLEEN HANDMATIG | 15-09 |
| 5 | Ahermar | ahermar.com | Jávea | ONBEKEND | – | filter ✓ | – | ONBEKEND | – | – | ALLEEN HANDMATIG | 14-09 |
| 6 | Javea Home Finders | javeahomefinders.com | Jávea | EasyInmo / GetSmart | – | rubriek ✓ | – | ONBEKEND | – | 3 | ALLEEN HANDMATIG | 15-09 |
| 7 | Crown Properties | crown-property.com | Jávea | ONBEKEND; beelden via Paagees, botcontrole | Renovatiedienst niet teruggezien (7) | rubriek ✓ | – | vermoedelijk nee (beelden hergebruikt door AR Luxury Living; BP-partner) | – | 3 | ALLEEN HANDMATIG | 15-09 |
| 8 | Engel & Völkers València–Jávea | engelvoelkers.com/es/en/shops/valencia-javea | Jávea (adres tegenstrijdig met gemeentelijke lijst) | Concernplatform | 1 finca "reforma integral" (Idealista) | filter ✓; 3 percelen met naam (Idealista; tool-m² wijkt af van tekst) | – | ONBEKEND (109 = heel E&V-netwerk in de gemeente) | – | 2 | ALLEEN HANDMATIG | 15-09 |
| 9 | Hamiltons of London | hamiltonsoflondon.net | Jávea | ONBEKEND; botcontrole | – | filter ✓ | – | vermoedelijk deels gedeeld (BP-partner) | – | 3 | ALLEEN HANDMATIG | 15-09 |
| 10 | Vicens Ash Properties | vicensash.com | Jávea | Mobilia | Renovatieplanning (dienst) | "Terrenos" ✓ | – | ONBEKEND | – (CRM Mobilia heeft volgens aanbieder een Public API, R2-29) | 2 | ALLEEN HANDMATIG | 15-09 |
| 11 | Paradise Real Estate | paradiserealestate.co.uk | Jávea | Sooprema (niet "eigen CRM") | – | rubriek ✓ | "Bank repossessed" | vermoedelijk nee ("Jávea 225", gelijk aan Arzuaga; BP-partner) | – | 3 | ALLEEN HANDMATIG | 15-09 |
| 12 | Valuvillas | valuvillas.com | Jávea | WordPress | ONBEKEND (pagina 403) | ONBEKEND | ONBEKEND | ONBEKEND | – | – | TECHNISCH ONDERZOEK NODIG | 14-09 |
| 13 | Villalux | villalux.com | Jávea | Waarschijnlijk Sooprema | Object ✓ ("complete renovation in Montgó", ref. 4522; zelfde woning als twee Idealista-advertenties, 4) | rubriek ✓ | – | ONBEKEND ("built and sold") | – | 2 | ALLEEN HANDMATIG | 15-09 |
| 14 | Alta Villas | altavillas.com | Jávea | ONBEKEND | – | rubriek ✓ | – | ONBEKEND | – | – | ALLEEN HANDMATIG | 14-09 |
| 15 | InmoVillas Jávea | inmovillasjavea.com | Jávea (adres site en gemeentelijke lijst tegenstrijdig) | WordPress + Inmobalia-media | – | Parcelas-pagina ✓; JP135 met licentie en goedgekeurde plannen | – | ONBEKEND (claimt "WhatsApp VIP off-market") | – | 1 | ALLEEN HANDMATIG | 14-09 |
| 16 | Deseo Homes | deseohomes.com | Jávea | WordPress | – | – | – | ONBEKEND | – | – | ALLEEN HANDMATIG | 14-09 |
| 17 | Randof Real Estate | randofrealestate.com | Jávea (+ Dénia) | Inmoweb (geen MLS-lidmaatschap getoond) | 1 renovatievilla (Idealista) | rubriek ✓ | Filter in Inmoweb-sjabloon | ONBEKEND | – | – | ALLEEN HANDMATIG | 15-09 |
| 18 | Atina Inmobiliaria | atinainmobiliaria.com/javea | Jávea | WordPress | – | rubriek ✓; Garroferal-perceel ook bij zes andere kantoren | – | ONBEKEND (getest perceel gedeeld, 3) | – | – | ALLEEN HANDMATIG | 15-09 |
| 19 | Javea Mia | javeamia.com | Jávea | WordPress + Houzez | "POTENTIAL" ✓ | rubriek ✓ | – | ONBEKEND | – | – | ALLEEN HANDMATIG | 14-09 |
| 20 | Javea Continental | javeacontinental.com | Jávea | Inmoweb | – | rubriek ✓ | Filter in Inmoweb-sjabloon | ONBEKEND | – | – | ALLEEN HANDMATIG | 15-09 |
| 21 | Grupo García | grupo-garcia.es | Jávea (+ Jalón, Moraira) | WordPress | – | – | – | ONBEKEND | – | – | ALLEEN HANDMATIG | 14-09 |
| 22 | Luxia Properties | luxiaproperties.com | Jávea | WordPress + WPResidence | Rubriek "Reformada" (gerenoveerd, niet te renoveren, 4) | JP144 met project en licentie | – | ONBEKEND (claimt 22 exclusieve villa's) | – | 1 | ALLEEN HANDMATIG | 14-09 |
| 23 | Llidomar Properties | llidomarjavea.com | Jávea | Sooprema | Object(en) | rubriek ✓ | – | ONBEKEND | – | – | ALLEEN HANDMATIG | 15-09 |
| 24 | Villadom Immo | villadomjavea.com | Jávea | Sooprema | 1 object (Idealista) | – | – | ONBEKEND | – | – | ALLEEN HANDMATIG | 15-09 |
| 25 | Javea Immo | javeaimmo.com | Jávea | Paagees | – | Rústicas ✓ | – | ONBEKEND | – | – | ALLEEN HANDMATIG | 15-09 |
| 26 | Arzuaga Inmobiliaria | arzuagainmobiliaria.com | Jávea | Sooprema | – | filter ✓; Garroferal-perceel (AR4676) | – | vermoedelijk nee ("Jávea 225", gelijk aan Paradise; BP-partner) | – | 3 | ALLEEN HANDMATIG | 15-09 |
| 27 | AR Luxury Living | arluxuryliving.com | Jávea | Gemengd: beelden van BP, Crown en Inmovilla | – | rubriek ✓; Garroferal-perceel met BP-referentie 4676JAV | – | nee (beelden van BP en Crown, 3) | – | – | ALLEEN HANDMATIG | 15-09 |
| 28 | Homes to be Happy | homestobehappy.com | Jávea | Sooprema | – | rubriek ✓ | – | vermoedelijk nee (beelden van MG Villas en een ander domein) | – | O | ALLEEN HANDMATIG | 15-09 |
| 29 | Montgó Villas | montgovillas.com | Jávea | Paagees | – | rubriek ✓ | – | ONBEKEND | – | 2 | ALLEEN HANDMATIG | 15-09 |
| 30 | MG Villas Luxury Property | mgvillas.co.uk | Jávea | Paagees | Object(en) | Percelen "with a construction project and with a building license" (68 objecten op de plotspagina) | – | ONBEKEND | – | 1 | ALLEEN HANDMATIG | 15-09 |
| 31 | 123 Javea Villas | 123javeavillas.com | Jávea | Advance Agent | Geen te-renoveren-rubriek (gecorrigeerd) | rubriek ✓ | "Bank Repossessions" | nee (claimt "access to all major estate agents properties", 1) | – | 3 | ALLEEN HANDMATIG | 15-09 |
| 32 | Euro Javea Real Estate | eurojavea.com | Jávea | WordPress + Inmobalia-media | Geen renovatierubriek (gecorrigeerd) | "Plots and land" ✓; solar 1.190 m² "en exclusiva" en perceel Granadella (Idealista) | – | ONBEKEND (claimt "Secret Sales") | – | 2 | ALLEEN HANDMATIG | 15-09 |
| 33 | Xabiga S.L. | xabiga.com | Jávea | WordPress + Houzez; bouwbedrijf | – | – | – | ONBEKEND | – | O | ALLEEN HANDMATIG | 14-09 |
| 34 | Xabiacasa | xabiacasa.com | Jávea | Inmoweb; "Member of Inmoweb MLS" | – | rubriek ✓ | Filter in Inmoweb-sjabloon | vermoedelijk nee (MLS-lid) | – | – | ALLEEN HANDMATIG | 15-09 |
| 35 | Andrea & Olaf Real Estate | andreayolaf.com | Jávea | ONBEKEND | ONBEKEND | ONBEKEND | ONBEKEND | ONBEKEND | – | – | TECHNISCH ONDERZOEK NODIG | 14-09 |
| 36 | Klaus Hildenbrand | klaus-hildenbrand.com | Jávea | Sooprema | 1 object (Idealista) | rubriek ✓ | – | ONBEKEND | – | – | ALLEEN HANDMATIG | 15-09 |
| 37 | TerramaR Costa Blanca | terramar.es | Jávea | Sooprema | ✓ ("totalmente para reformar") | "Parcela edificable" ✓; Garroferal-perceel met perceelnummer | – | ONBEKEND (bouw en verkoop; getest perceel gedeeld) | – | 2 / O | ALLEEN HANDMATIG | 15-09 |
| 38 | Soluciones Inmobiliaria Jávea | solucionesinmojavea.com | Jávea | WordPress | – | rubriek ✓ | – | ONBEKEND | – | – | ALLEEN HANDMATIG | 14-09 |
| 39 | Casitas Iberica | casitasiberica.com | Jávea | WordPress | – | – | – | nee (claimt "network of local estate agents", 1) | – | – | ALLEEN HANDMATIG | 14-09 |
| 40 | Ashton Villas | ashtonvillas.com | Jávea | WordPress + RealHomes | – | – | – | ONBEKEND | – | – | ALLEEN HANDMATIG | 14-09 |
| 41 | AV Costamar | avcostamar.com | Jávea | WordPress + RealHomes | – | – | – | ONBEKEND | – | – | ALLEEN HANDMATIG | 14-09 |
| 42 | Coldwell Banker Solaris | coldwellbanker.es/inmobiliaria-javea-solaris | Jávea | Concernsite | 3 objecten > 700.000 EUR onder filter "para reformar" (renovatiebehoefte niet overal blijkend) | 11 van 50 "terreno urbano"-advertenties met ref. CBS…; "Plots" in concernzoeker | – | ONBEKEND (eigen referenties, niet bevestigd) | – | 2 | ALLEEN HANDMATIG | 15-09 |
| 43 | Miralbo Urbana | miralbo.com | Jávea | ONBEKEND | Totaalrenovaties (dienst) | – | – | Eigen projecten (1); BP-partner | – | O | ALLEEN HANDMATIG | 14-09 |
| 44 | Plots Direct | plotsdirect.com | Jávea | ONBEKEND | rubriek ✓ (niet herverifieerd) | rubriek ✓ (design and build) | – | ONBEKEND | – | 2 | ALLEEN HANDMATIG | 14-09 |
| 45 | Javea Casas | javeacasas.com | Jávea | Waarschijnlijk Sooprema | – | – | – | vermoedelijk nee (124 objecten) | – | 3 | ALLEEN HANDMATIG | 15-09 |
| 46 | Selenhome | selenhome.com | Jávea | Waarschijnlijk Sooprema | – | rubriek ✓ | – | ONBEKEND | – | – | ALLEEN HANDMATIG | 15-09 |
| 47 | Marina Villas Jávea | Niet gevonden | Jávea | ONBEKEND | ONBEKEND | ONBEKEND (bouw en ontwikkeling volgens Jávea.com) | ONBEKEND | ONBEKEND | ONBEKEND | – | TECHNISCH ONDERZOEK NODIG | 14-09 |
| 48 | Maravilla Costa | Niet gevonden in R06; gemeentelijke lijst noemt maravilla-costa.es (niet gecontroleerd) | Jávea | ONBEKEND | ONBEKEND | ONBEKEND | ONBEKEND | vermoedelijk deels gedeeld (BP-partner) | ONBEKEND | – | TECHNISCH ONDERZOEK NODIG | 14-09 |
| 49 | Promociones Jávea S.L. (in R06 als "Jávea Promotions", zelfde adres) | promocionesjavea.com | Jávea | ONBEKEND | – | 23 percelen Cumbres del Tosalet (eigen urbanisatie) | – | Eigen promoties (1) | – | O | ALLEEN HANDMATIG | 14-09 |
| 50 | Class & Villas | classandvillas.com | Jávea | Eigen site | – | – | – | Geen makelaar (magazine) | – | – | NIET GEBRUIKEN (geen makelaar) | 14-09 |
| 51 | Casas Ambiente | casas-ambiente.com | Moraira | Mediaelx | – | rubriek ✓ | – | vermoedelijk nee (MLS/REALTOR-vermeldingen; 42 in Jávea) | – | 3 | ALLEEN HANDMATIG | 14-09 |
| 52 | BoCasa | bocasa.nl | Moraira | Mediaelx | – | – | – | ONBEKEND | – | – | ALLEEN HANDMATIG | 14-09 |
| 53 | Tabaira Real Estate | tabairarealestate.com | Moraira | Mediaelx | – | – | – | ONBEKEND (beelden van Tabaira staan ook bij Casas Costa Blanca) | – | – | ALLEEN HANDMATIG | 15-09 |
| 54 | Orange Villas | orangevillas.com | Moraira | Mediaelx | – | rubriek ✓; 1 perceel met naam (Idealista) | – | ONBEKEND (Jávea-pagina toonde 0) | – | – | ALLEEN HANDMATIG | 14-09 |
| 55 | Casas Costa Blanca | casascostablanca.nl | Moraira | WordPress | – | rubriek ✓ | – | nee (beelden uit ≥ 9 externe bronnen, onder meer BP, 3) | – | – | ALLEEN HANDMATIG | 15-09 |
| 56 | Inmobiliaria Celenia | inmobiliariacelenia.com | Moraira | Drupal 7 | – | rubriek ✓ | – | ONBEKEND | – | – | ALLEEN HANDMATIG | 14-09 |
| 57 | Bindley Properties | bindleyproperties.com | Moraira | Paagees | – | rubriek ✓ | – | ONBEKEND | – | – | ALLEEN HANDMATIG | 15-09 |
| 58 | Ferrando Estate Agents | ferrando-moraira.com | Moraira | ONBEKEND (beelden via Paagees) | – | rubriek ✓ | – | ONBEKEND | – | – | ALLEEN HANDMATIG | 15-09 |
| 59 | Holidaydream Homes | holidaydream.es | Moraira | Paagees | "Reformas" is een bouwdienst, geen aanbodrubriek | 48 parcelas (heel werkgebied); 71 objecten in Jávea | – | ONBEKEND | – | 3 | ALLEEN HANDMATIG | 15-09 |
| 60 | Benitachell Properties | benitachellproperties.com | Benitachell | Sooprema | – | rubriek ✓ | "Propiedades de Banco" | ONBEKEND | – | – | ALLEEN HANDMATIG | 15-09 |
| 61 | Laura Villas | lauravillas.com | Benitachell | Eigen site | – | rubriek ✓ | – | ONBEKEND | – | – | ALLEEN HANDMATIG | 14-09 |
| 62 | AREA Costa Blanca | areacostablanca.es | Benissa, Calpe | Sooprema | – | – | – | ONBEKEND | – | – | ALLEEN HANDMATIG | 15-09 |
| 63 | Benimo-Villas | benimo-villas.com | Benissa | Sooprema | Object(en) | rubriek ✓ | – | ONBEKEND | – | – | ALLEEN HANDMATIG | 15-09 |
| 64 | Villa Mediterránea | villamediterranea.es | Calpe | Sooprema | Object(en) | 72 plots (heel werkgebied) | – | ONBEKEND | – | – | ALLEEN HANDMATIG | 15-09 |
| 65 | Agencia J. Morató | agenciamorato.com | Calpe | Sooprema | – | 32 percelen (heel werkgebied) | – | ONBEKEND | – | – | ALLEEN HANDMATIG | 15-09 |
| 66 | MP Villas | mpvillas.com | Calpe | Inmovilla | ONBEKEND | ONBEKEND | – | ONBEKEND | – (CRM Inmovilla heeft API en XML, R2-29) | – | TECHNISCH ONDERZOEK NODIG (aanbodpagina 404) | 14-09 |
| 67 | Calablanca (Cala Blanca Villas S.L.) | calablanca.com | Jávea | Sooprema | – | rubriek ✓; 1 perceel met naam (Idealista) | – | ONBEKEND | – | – | ALLEEN HANDMATIG | 15-09 |
| 68 | Fine & Country Costa Blanca North | fineandcountry.es | Dénia | MyF&C | – | – | – | ONBEKEND (6 in Jávea) | – | – | ALLEEN HANDMATIG | 14-09 |
| 69 | Berkshire Hathaway HomeServices Costa Blanca | bhhscostablanca.com | Dénia, Altea | WordPress | – | – | – | ONBEKEND | – | – | ALLEEN HANDMATIG | 14-09 |
| 70 | MNM Costa Blanca | mnmcostablanca.es | Els Poblets | ONBEKEND | – | – | – | ONBEKEND (4 in Jávea) | – | – | ALLEEN HANDMATIG | 14-09 |
| 71 | Villa Lingo | villalingo.com | Dénia (gemeentelijke lijst: Jávea) | ONBEKEND | – | rubriek ✓ | – | ONBEKEND | – | – | ALLEEN HANDMATIG | 14-09 |
| 72 | Inmover | inmover.com | Els Poblets, El Verger | Paagees | ONBEKEND | ONBEKEND | – | ONBEKEND (Jávea niet genoemd) | – | – | ALLEEN HANDMATIG | 15-09 |
| 73 | Alveo / J'achète en Espagne | alveo.co/agent-immobilier/javea | Alicante | Webflow; Witei-vermelding | – | – | – | 0 Jávea-objecten getoond | – | – | NIET GEBRUIKEN (geen Jávea-aanbod gezien) | 14-09 |
| 74 | Costa Blanca Sotheby's International Realty | spain-sothebysrealty.com | Alicante | Concernplatform | – | – | – | ONBEKEND (Jávea niet getoond, 7) | – | – | ALLEEN HANDMATIG | 14-09 |
| 75 | Casasdediez | casasdediez.com | Oliva Nova | WordPress | – | – | – | Niet op Jávea gericht | – | – | NIET GEBRUIKEN (geen Jávea-aanbod) | 14-09 |
| 76 | Koch & Varlet Luxury Realtors | kv-realtors.com (gevonden in verificatie) | Jávea | eGO Real Estate; bouwtak KVC Projects | – (twee objecten zijn nieuwbouw, geen renovatie) | – | – | ONBEKEND (eigen referenties KV…) | – | – | ALLEEN HANDMATIG | 15-09 |
| 77 | Lucas Fox Jávea | lucasfox.com/offices/jav.html (403 voor tools) | Jávea | Concernplatform | 1 "villa a renovar íntegramente" (Idealista) | – | – | vermoedelijk deels gedeeld (BP-partner); openingsjaar tegenstrijdig (7) | – | 2 | TECHNISCH ONDERZOEK NODIG (site 403) | 15-09 |
| 78 | Six Seconds Properties SL | sixsecondsproperties.com | ONBEKEND | ONBEKEND | – | JA-SO-1001: 192 m² in de haven, licentie voor 6 woningen | – | ONBEKEND | – | 1 | ALLEEN HANDMATIG | 14-09 |
| 79 | Euroholding Dénia Inmobiliaria | ehd.es | Dénia | ONBEKEND | – | – (verkoopt nieuwbouw Blooming Village) | – | ONBEKEND | – | – | ALLEEN HANDMATIG | 14-09 |

**Alleen op naam bekend (48; status TECHNISCH ONDERZOEK NODIG tot een site of profiel is gecontroleerd).**

- *Uit R06 §3C, site niet bereikbaar of niet gevonden (13; type 1/7):* Villas-Plots (403; BP-partner), Signature Villas (verbinding geweigerd), Inmobiliaria Javea (DNS-fout), Spanienobjekte (403), Giuliano Villas (R06 toetste giulianovillas.com; de gemeentelijke lijst noemt giuliano-villas.com, niet gecontroleerd), Immo Belgica, Blom Group Real Estate, Silvia Piera Inmobiliaria, Premium Villas Costa Blanca, Select Villas of Moraira, catorce inmobiliaria, Montesinos Falcón, Marti Projects (403).
- *Alleen in Javea Guide (15; type 1):* Hernani Homes, Euro Villas Javea, Casaconnections, A.F. Costa Blanca S.L., Be Spoiled, Casas de Levante, Acre, HG Hamburg, Houses, Javea 1, Javea Online, La Nao en Mestral, Sukup & Partner, Ultimate Property Javea, Villa Mia.
- *Vermoedelijk inactief (2; type 3):* Bemax Javea ("Account Suspended"), Grupo Moraira ("System Updating").
- *Alleen op de gemeentelijke lijst xabia.org, niet in R06 (11; type 2):* Alensol S.L., Bartolome Bas, Deluxe Homes Javea, FPI Inmobiliaria, Houses Investment Holdings, Indarte, Javea Homes (R06: javeahomes.com "System Updating"), L'Aurora Villas Selection, New Life Property Spain, Proxabia, RE/MAX Inmomas IV.
- *Uit R07 (3; type 1):* Javea Estates (ook BP-partner), Dénia Casas, iad España ("12 real estate agents in Jávea or nearby").
- *Alleen op de BP-partnerlijst (4; type 1):* Prima Villas, Blanca International, Elite Costa Properties, Moment Estates.
- *Geen verkoopmakelaar (buiten het register):* BonCasa / MMC Property Services, Aguila Rent a Villa, Quality Rent a Villa, Rental Villalux, Rentals Javea, Habitat Dénia, Denia Luxe Lofts, Jávea.com (mediabedrijf).

##### Tabel K-2 — Ontwikkelaars en promotoren met Jávea-projecten

| Partij | Website | Wat is bevestigd | Voor TREE (voorstel, type 4) | Status | Bron · datum · type |
|---|---|---|---|---|---|
| Ten Brinke España | tenbrinke.com | Kocht in 2024 een perceel van 2.000 m² aan Calle Haya voor Residencial Marina Bay Sunset, 30 woningen, ontwerpfase; derde meergezinsproject in Jávea. Marina Bay I en II alleen uit zoekresultaat (7) | Afnemer van grotere solares (route D); afnemer keukens en sanitair (route C) | ALLEEN HANDMATIG | https://www.tenbrinke.com/es/noticias/noticias-reader/ten-brinke-espana-adquiere-una-parcela-de-2-000-m2-donde-desarrollara-residencial-marina-bay-sunset-tercer-proyecto-residencial-multifamiliar-en-javea-alicante.html · 14-09-2026 · 1 |
| Prygesa (Planificación Residencial y Gestión S.A.U.) | prygesa.es | Jávea Garden, Calle Historiador Palau 23: 72 woningen, "Licencia de obra concedida", vanaf 214.000 EUR + IVA | Partij die grond in het centrum zoekt (D); route C | ALLEEN HANDMATIG | https://www.prygesa.es/obra-nueva/alicante/javea-garden · 14-09-2026 · 1 |
| Aelca | aelca.es | Adeya Jávea (25 woningen) en Adeya Jávea II (10), beide "Obras iniciadas", vanaf 411.000 en 377.000 EUR + IVA | D, C | ALLEEN HANDMATIG | https://www.aelca.es/es/proyectos/adeya-javea/ · https://www.aelca.es/es/proyectos/adeya-ii-javea/ · 14-09-2026 · 1 |
| Living Inversiones | livinginversiones.com | Living Jávea: 20 woningen (projectpagina) of 22 (Idealista en lamarina): tegenstrijdig (7); 12 van 20 beschikbaar op 14-09-2026 (momentopname); sloop van een chalet alleen in lamarina | Kent het traject sloop en herbouw van een chalet naar appartementen (D, C) | ALLEEN HANDMATIG | https://www.livinginversiones.com/en/projects/living-javea-residential/ · 14-09-2026 · 1 |
| Promociones Jávea S.L. | promocionesjavea.com | Sinds 1984; Cumbres del Tosalet (23 percelen), Golden Ray, Beach Trade Center; project management en beleggingsprojecten | Bron én afnemer van percelen (B, D) | ALLEEN HANDMATIG | https://www.promocionesjavea.com/ · 14-09-2026 · 1 |
| Miralbo Urbana S.L. | miralbo.com | Ontwerp, promotie en bouw van luxe villa's, "reformas integrales"; BP-partner | Concurrent op villabouw en partner voor percelen die zij niet zelf bebouwen (B, D) | ALLEEN HANDMATIG | https://www.miralbo.com/es-es · 14-09-2026 · 1 |
| VAPF | vapf.com | Benissa, "since 1963"; Cumbre del Sol (Benitatxell, tussen Jávea en Moraira), losse percelen te koop | Benchmark en bron van bouwrijpe kavels naast Jávea (B) | ALLEEN HANDMATIG | https://www.vapf.com/en/real-estate-developer/residential-areas/cumbre-del-sol · 14-09-2026 · 1 |

Projecten zonder vastgestelde promotor: Blooming Village (verkoop via ehd.es; oplevering "2026" volgens ehd.es tegenover "primer trimestre 2028" volgens lamarina: tegenstrijdig, 7), Lemon Residence (9 appartementen), Villas Aires de Jávea, Villa Pura Vida, Residencial Nusa Dua en Marina XI (alleen portaalsnippets, 7) (R07 §2.2; R07-verificatie A8).

#### L. Planologie, sectorale kaartlagen en aanvullende veiling- en overheidsverkoopkanalen (toegevoegd 15-09-2026)

Bron voor de invulling: R12, R13 en R08 met hun verificaties, deliverables 03 (stap 8–12, bijlage A), 04 (§2.2, §2.10, §2.11) en 05 (§3.4), en R16 voor de rechten. Bewijstype staat tussen haken in de cellen (1–7, masterprompt §5). Gaf een onderzoeksrapport een mildere status, dan staat dat als statusnoot bij de toegestane gebruiksdoelen. De BOP Alicante (R2-42), de Catastro-diensten (R2-43, R2-44), het Registro de la Propiedad (R2-45), de BOE-kanalen (R2-35, R2-36), de AEAT-lijst (R2-37) en PLACSP (R2-42) hadden al een regel en staan hier niet opnieuw.

| Veld | R2-60 ICV/GVA — Planeamiento urbanístico (WFS/WMS 0702_Planeamiento) | R2-61 ICV/GVA — sectorale kaartlagen 0701_InfraestructuraVerde (o.a. PATRICOVA-laag IVR.Inundacion, Red Natura 2000, erfgoed), 0505_PORN (Montgó) en 0506_PATFOR (WMS/WFS) | R2-62 ICV ArcGIS REST — ordenacion_territorial (PATRICOVA-lagen 4–10, PATIVEL), espacios_protegidos en prevencion_de_incendios |
|---|---|---|---|
| Naam en officiële website | https://terramapas.icv.gva.es/0702_Planeamiento · https://datos.gob.es/es/catalogo/a10002983-planeamiento-urbanistico-de-la-comunitat-valenciana-clasificacion-urbanistica | https://terramapas.icv.gva.es/0701_InfraestructuraVerde · https://terramapas.icv.gva.es/0505_PORN · https://terramapas.icv.gva.es/0506_PATFOR | https://carto.icv.gva.es/arcgis/rest/services/tm_infraestructuras/ordenacion_territorial/MapServer · https://carto.icv.gva.es/arcgis/rest/services/tm_medio_ambiente/espacios_protegidos/MapServer · https://carto.icv.gva.es/arcgis/rest/services/tm_medio_ambiente/prevencion_de_incendios/MapServer |
| Type aanbieder | Officiële geodatadienst van de Generalitat Valenciana / Institut Cartogràfic Valencià: mozaïek van planclassificatie en zonering (type 2) | Officiële geodatadiensten van de Generalitat Valenciana / ICV (type 2) | Officiële ArcGIS-kaartdiensten van het ICV (type 2) |
| Geografische en inhoudelijke dekking | Comunitat Valenciana. Xàbia (INE 03082): 356 zonevlakken (SUZ/ZND-RE 140, SU/ZUR-RE 126, SNU-P/ZRP-NA-MU 24, SNU-P/ZRP-NA-LG 18, SNU-C/ZRC-FO 12 e.a.); bevat nog 20 vlakken van de door de TSJCV vernietigde homologación Portitxol; geen PGE. Laag MinimizacionViviendasSNU: 585 percelen in Xàbia (R13, niet hercontroleerd) (R12 §2.8; R12-verificatie R12-02, R12-17; 03 stap 8, type 2/3) | Comunitat Valenciana. 0701: IVR.Inundacion (PATRICOVA gevaar 1–6 en geomorfologisch), IVR.ParquesNaturales, IVR.ZEC, IVR.LIC, IVR.ZEPA, IVR.Montes, IVR.TFEPATFOR, IVR.Cultura.BIC.BIC, IVR.Cultura.BIC.Entornos, IVR.Cultura.BRL, IVR.PaisajesRelevancia, IVR.Cavidades. 0505: Montgo.PORN, Montgo.Zonificacion, Montgo.ZonificacionSantAntoni, Montgo.Parque. 0506: SF.Forestal, Forestal.Estrategico, Regulacion.Incendios.Urbano, Regulacion.Incendios.Peligrosidad. Xàbia: PATRICOVA niveau 1–6 ≈ 827 ha = 12,0 % van de gemeente (R13-verificatie R13-07, type 5). De gemeentelijke erfgoedcatálogo zit niet in deze lagen (R13 §7; 03 stap 10, type 3) | Comunitat Valenciana. ordenacion_territorial: 1 estudios de inundabilidad, 3 red de cauces, 4–9 PATRICOVA peligrosidad 1–6, 10 geomorfológica, 12 riesgo (niet voor besluiten), 30–32 PATIVEL-ámbitos (lijnen), 33 catálogo de playas, 34 PATIVEL Litoral 1/2, 100 ámbito ejecución sentencia. espacios_protegidos: 21 zonering Red Natura. prevencion_de_incendios: o.a. 8 brandperimeters, 71 ámbito PPIF, 104 ZIF 500 m, 114, 123. Daarnaast tm_medio_ambiente/forestal (laag 25 montes). Xàbia: Litoral 1 ≈ 58,6 ha en Litoral 2 ≈ 9,8 ha; testpunt Granadella ligt binnen de brandperimeter van 2016 en op de rand (< 5 m, formeel buiten) van die van 2000 (R13 §7; R13-verificatie R13-14 en gecorrigeerde claim R13-10, type 3/5) |
| Technische toegang | WFS 2.0 en WMS zonder sleutel; typenames Planeamiento.Clasificacion, Planeamiento.Zonificacion, Planeamiento.Dotaciones, InventarioSuSuz, MinimizacionViviendasSNU, DeclaracionInteresComunitario. GetFeature alleen resultaat met bbox in EPSG:25830 (bbox in EPSG:4326 gaf 0 objecten, OGC-attribuutfilter gaf serverfout) of GetFeatureInfo op een kleine bbox rond het punt; R12 en R13 meldden verschillend gedrag, dus de werkende CRS-parameter met een regressietest vastleggen (R13 §7; R12-verificatie R12-17; 05 §3.4, type 3) | WMS GetFeatureInfo (INFO_FORMAT=geojson; bij WMS 1.3.0 met EPSG:4326 volgorde lat,lon) en WFS GetFeature, zonder sleutel; getest op de testpunten en de K07-pin (R13 §3.2, §7; R13-verificatie R13-05, R13-09, type 3). Ontwerp: per laag cachen en per laag een dienststatus (05 §3.4, type 4) | `?f=json` HTTP 200; identify en query (ArcGIS 10.61, maxRecordCount 2000, SR 3857), zonder sleutel. Een query met de perceelomtrek (esriGeometryPolygon, inSR 25830) geeft de geraakte vlakken; een overlappercentage is niet getest. Lagen 30–32 zijn lijnen: punt-in-polygoon geeft daar altijd 0, dus afstand berekenen (R13 §7, §11; 05 §3.4; 03 bijlage A E9, E12, E13, type 3) |
| Beschikbare velden | Instrument (naam en expediente, bijv. PLAN PARCIAL 'ERMITA II', exp. 19940463), klasse (SU, SUZ, SNU-P, SNU-C), zonecode (ZUR-RE, ZND-RE, ZRP-NA-MU e.a.), gemeentecode, geometrie per vlak (R12 §2.8, type 3) | PATRICOVA: n_pelig, codigo, zona, retorno, calado; PORN-ámbito en -zonering; Red Natura-code en zone; PATFOR bosgrond, strategisch bos, brandinterface; BIC/BRL-object en omgeving (R13-verificatie R13-05, R13-09, type 3) | Per laag attributen van de vlakken (bijv. PATRICOVA-niveau, PATIVEL-categorie, brandjaar en -naam, resolutie PPIF); volledige veldlijst niet vastgelegd |
| Foto's en documenten | Geen documenten; WMS-kaartbeeld. Normdocumenten staan in het GVA-planregister (R2-67) | Geen documenten; WMS-kaartbeeld. Normativa apart: PATRICOVA Decreto 201/2015, PORN Montgó Decreto 180/2002, PATFOR Decreto 58/2013 (03 §2.2) | Geen documenten; kaartbeeld |
| Publicatie- en wijzigingsinformatie | Laag bijgewerkt 25-08-2026 volgens datos.gob.es (R12-verificatie R12-17, type 2); datum per vlak ONBEKEND | Laagdatum per dienst niet vastgelegd (ONBEKEND) | ONBEKEND per laag; soms als attribuut (laag 71: 'Aprobada revisión en 2020', R13-verificatie R13-09) |
| Historische gegevens | ONBEKEND: alleen de actuele mozaïek gezien; vlakken van vernietigde plannen staan er deels nog in | ONBEKEND | Brandperimeters per jaar (laag 8); verder ONBEKEND |
| Verversingsfrequentie | ONBEKEND; laatste update 25-08-2026. Ontwerp: laagdatum per perceeldossier bijhouden en bij wijziging heranalyse (05 §3.4, type 4) | ONBEKEND. Ontwerp R13 §11: PATRICOVA- en PATIVEL-vlakken voor Xàbia wekelijks verversen volstaat (type 4) | ONBEKEND; ontwerp: gecachete vlakken wekelijks verversen (R13 §11, type 4) |
| Rate limits | Niet gepubliceerd (ONBEKEND); getest met één verzoek per punt (R12 §2.8) | Niet gepubliceerd (ONBEKEND); de verificatie hield het aantal verzoeken laag (één geometrie-opvraging per laag) | maxRecordCount 2000; verder niet gepubliceerd |
| Kosten | Geen: `Fees` 'No se aplican condiciones' (type 2) | Geen kosten of sleutel gezien (R13 §7, type 3) | Geen kosten of sleutel gezien (type 3) |
| Contractstatus | Niet nodig: `AccessConstraints` 'CC BY 4.0 Generalitat' (R12-verificatie R12-17, type 2) | Niet nodig: 'CC BY 4.0 Generalitat' (R13 §7, type 2) | Licentie 'niet vermeld in JSON' [te verifiëren] (R13 §7; 05 §3.4) |
| Toegestane gebruiksdoelen | Hergebruik met bronvermelding 'Generalitat Valenciana / ICV'; alleen als eerste planologisch filter met de vaste vermelding 'carácter informativo', nooit als bouwrecht; spreken twee GVA-lagen elkaar tegen, dan is de klasse type 7 (03 stap 8; 05 §3.4) — Statusnoot: R12 §8 gaf GEVERIFIEERD EN ACTIEF; hier strenger, want er draait nog niets (05 §3.4) | Signaal per perceelpolygoon met bronvermelding; nooit 'geen beperking' (05 §3.4; R13 §11). PORN-begrenzing 'carácter informativo'; een lokale inundabiliteitsstudie kan de PATRICOVA-afbakening wijzigen (R13 §3.6) | ONBEKEND zolang de licentie niet is vastgesteld; inhoudelijk alleen als signaal met laag, datum en bewijstype 3, nooit 'geen beperking' (05 §3.4) |
| Rechten AI-analyse | Toegestaan (CC BY 4.0) | Toegestaan (CC BY 4.0) | ONBEKEND (licentie niet vermeld) |
| Opslag en bewaren | Toegestaan; per perceel met laagdatum en dienststatus (05 §3.4) | Toegestaan; per laag gecachet met datum van laatste controle (R13 §11) | ONBEKEND (licentie niet vermeld) |
| Afgeleide gegevens en beeldvergelijking | Toegestaan met bronvermelding; overlappercentage perceel × zonevlak nog niet getest (05 §3.4) | Toegestaan met bronvermelding | ONBEKEND (licentie niet vermeld) |
| Contactpersoon of aanvraagroute | Geen contactroute vastgelegd in R12 of R13; catalogusfiche op datos.gob.es | Geen contactroute vastgelegd in R13 | Geen contactroute vastgelegd in R13 |
| Laatste verificatie | 15-09-2026 | 15-09-2026 | 15-09-2026 |
| Openstaande vragen | Werkende CRS-parameter vastleggen (R12 en R13 verschillen); tegenstrijdige GVA-lagen op de K07-pin (PP Ermita II tegenover 'Plan Parcial Montgó-2 / SUP Montgó-2', type 7); overlap via ArcGIS-query of eigen code niet getest; betekenis 'tipo D/R' in MinimizacionViviendasSNU; onherroepelijkheid van de Portitxol-uitspraak niet gecontroleerd | PATRICOVA niveau 1 ontbreekt in art. 18.2; Montgó alleen als LIC in de laag; bosgebied La Granadella/Montgó I 'gecatalogiseerd' of niet (tegenstrijdige lagen); geen conclusie bij tegenstrijdigheid met ARPSI (R2-63); aantallen BIC/BRL en minimización niet hercontroleerd (R13 §12; R13-verificatie §3) | Welke licentie geldt voor carto.icv.gva.es (dezelfde CC BY 4.0 als terramapas)? Overlap via query met perceelomtrek testen; afbakening van de brandinterface van Xàbia (pleno 28-05-2026) zit niet in de dienst; PATIVEL: lopende TSJCV-procedure en Plan de Ordenación Costera (R13 §12) |
| **Operationele status** | **TECHNISCH ONDERZOEK NODIG** | **TECHNISCH ONDERZOEK NODIG** | **TECHNISCH ONDERZOEK NODIG** |

| Veld | R2-63 IDEE — overstromingsgevaar ARPSI (WMS-INSPIRE riesgos-naturales/inundaciones; werkend alternatief voor SNCZI) | R2-64 MITECO — kustdomein DPMT: deslinde en servidumbre (viewer, WMS en download dpmt.zip) | R2-65 MITECO — waterlopen (DPH) en zonas inundables SNCZI (WMS en viewer) |
|---|---|---|---|
| Naam en officiële website | https://servicios.idee.es/wms-inspire/riesgos-naturales/inundaciones | https://gis.miteco.gob.es/web/dpmt · https://wms.mapama.gob.es/sig/Costas/DPMT · https://www.miteco.gob.es/es/cartografia-y-sig/ide/descargas/costas-medio-marino/deslinde-dpmt.html | https://wms.mapama.gob.es/sig/agua/ZI_LaminasQ100 · https://gis.miteco.gob.es/web/snczi |
| Type aanbieder | Officiële nationale geodatadienst (Infraestructura de Datos Espaciales de España): gevaarkaarten volgens RD 903/2010, met vermelding van MITECO (type 2) | Officiële geodata van het Ministerio para la Transición Ecológica y el Reto Demográfico (type 2) | Officiële geodata van MITECO (type 2) |
| Geografische en inhoudelijke dekking | ARPSI-gebieden in Spanje; lagen NZ.Flood.FluvialT10/T100/T500, NZ.Flood.MarinaT100/T500 en EL.GridCoverage (MDT LiDAR). Arenal (P1): T10 0,073 / T100 1,951 / T500 2,466; Granadella (P2): 999 (R13 §3.5; R13-verificatie R13-06, type 3) | Spaanse kust: deslindelijn van het DPMT, servidumbre de protección (100 m, of 20 m voor grond die in 1988 stedelijk was) en núcleos excluidos; kader Ley 22/1988 art. 23–30, DT 3ª–4ª en Ley 3/2025 art. 44–45 (R13 §6.1; R13-verificatie R13-15). Voor Xàbia niet getest. Signaal zonder deslindewaarde: GVA-planzone SNU-P/ZRP-CT (kust), 2 vlakken (03 stap 10, type 3) | Volgens de officiële catalogus Q10, Q50, Q100, Q500, zona de flujo preferente (ZFP), DPH en ARPSI (R13 §7). Kader waterlopen: RDL 1/2001 art. 6 (servidumbre 5 m, zona de policía 100 m) (03 stap 10). Voor Xàbia niet getest. Signaal zonder deslindewaarde: GVA-planzone SNU-P/ZRP-CA (waterlopen), 9 vlakken, en toponiemlijnen van het ICV (03 stap 10; R13 §9, type 3) |
| Technische toegang | WMS GetCapabilities en GetFeatureInfo (text/plain, veld GRAY_INDEX), zonder sleutel (R13 §7, type 3) | Op 15-09-2026 onbereikbaar: WMS (ook /SP, /NucleosExcluidos, /TerrenosIncluidos) gaf ServiceException NullReferenceException; viewer gis.miteco.gob.es gaf verbindingsreset (curl) of HTTP 503; sig.miteco.gob.es/dpmt/ geeft 301 naar een migratiepagina. Niet omzeild. Volgens de R13-verificatie eerder een gemigreerde of vervallen dienst dan een tijdelijke storing [te verifiëren] (R13 §6.4, §13; R13-verificatie R13-16, F12, type 3) | Op 15-09-2026 onbereikbaar: WMS ZI_LaminasQ100, ZI_LaminasQ500, ZI_LaminasZFP, ZI_ARPSI en DPHCartografico gaven ServiceException NullReferenceException; viewer gis.miteco.gob.es/web/snczi verbindingsreset of HTTP 503; sig.miteco.gob.es/snczi/ geeft 301 naar een migratiepagina. Adres van een aparte DPH-dienst niet vastgelegd (03 bijlage A E15). Niet omzeild (R13 §3.5, §13; R13-verificatie R13-16, F12, type 3) |
| Beschikbare velden | Rasterwaarde per punt (GRAY_INDEX). Eenheid niet vermeld in capabilities of metadata; de legenda (0,2–2) past bij waterdiepte in meters, maar dat blijft type 7. Nodata is 3,4·10³⁸; 999 is een aparte code met onbekende betekenis (R13-verificatie R13-06, A4) | ONBEKEND (dienst niet bereikt) | ONBEKEND (dienst niet bereikt) |
| Foto's en documenten | Geen documenten; kaartbeeld en legenda | Downloads volgens de MITECO-pagina: dpmt.zip (shapefile, 12,2 MB, 'Actualización 31/03/2026'), gml-dpmt.zip (18,7 MB), DPMT_con_nucleos.kmz (16,3 MB), sp.zip (44,6 KB, 30-09-2024) en 'Núcleos excluidos (DA 7ª Ley de Costas)' (31-12-2020). Niet gedownload; de downloadhost gaf een verbindingsreset (R13 §6.4; R13-verificatie A6, type 2/3) | ONBEKEND |
| Publicatie- en wijzigingsinformatie | ONBEKEND | Actualisatiedatum per downloadbestand (zie foto's en documenten) | ONBEKEND |
| Historische gegevens | ONBEKEND | ONBEKEND | ONBEKEND |
| Verversingsfrequentie | ONBEKEND | ONBEKEND; dpmt.zip laatst bijgewerkt 31-03-2026 volgens de downloadpagina | ONBEKEND |
| Rate limits | Niet gepubliceerd (ONBEKEND) | ONBEKEND | ONBEKEND |
| Kosten | Geen kosten of sleutel gezien (type 3) | Geen kosten vermeld (ONBEKEND) | ONBEKEND |
| Contractstatus | Niet nodig: vrij gebruik met vermelding van MITECO (R13 §3.5, §7, type 2) | Voorwaarden niet gelezen; MITECO: 'Los datos disponibles tienen un carácter meramente informativo' (R13 §6.4, type 2) | Niet getest; R13 §7 noemt voor SNCZI 'vrij met vermelding', maar dat is niet op een werkende dienst bevestigd (type 2/7) |
| Toegestane gebruiksdoelen | Kruiscontrole naast PATRICOVA (complementair volgens PATRICOVA art. 7 en 10.2). Bij tegenstrijdigheid (PATRICOVA < 0,8 m tegenover ARPSI T100 1,951) geen conclusie trekken, maar voorleggen aan een hydraulisch ingenieur of de gemeente (R13 §3.5). De waarde 999 nooit lezen als 'geen overstroming' of 'buiten studiegebied' (R13-verificatie A4) | ONBEKEND. Vaste uitkomst zolang de dienst niet werkt: 'dienst onbereikbaar; kusttoets 20/100 m ONBEKEND' (05 §3.4). Download alleen met akkoord van Jan (R13 §12) | ONBEKEND zolang de dienst niet werkt. Werkend alternatief voor overstromingsgevaar: IDEE-ARPSI (R2-63). Een toponiemlijn is geen deslinde (03 stap 10) |
| Rechten AI-analyse | Toegestaan met vermelding van MITECO | ONBEKEND | ONBEKEND |
| Opslag en bewaren | Toegestaan met vermelding van MITECO | ONBEKEND | ONBEKEND |
| Afgeleide gegevens en beeldvergelijking | Toegestaan met vermelding van MITECO; eenheid eerst verifiëren | ONBEKEND | ONBEKEND |
| Contactpersoon of aanvraagroute | Geen contactroute vastgelegd in R13; bevoegde stroomgebiedsbeheerder naar verwachting de Confederación Hidrográfica del Júcar [te verifiëren] | Kustdienst (Demarcación de Costas Comunitat Valenciana-Sur [te verifiëren]) of een kustjurist (R13 §12); MITECO noemt ook de Sede Electrónica del Catastro als raadpleegroute (R13-verificatie A5, niet getest) | Bevoegde stroomgebiedsbeheerder naar verwachting de Confederación Hidrográfica del Júcar [te verifiëren] (R13 §3.5) |
| Laatste verificatie | 15-09-2026 | 15-09-2026 | 15-09-2026 |
| Openstaande vragen | Eenheid en betekenis van de rasterwaarden (1,951 bij T100; code 999); verhouding tot PATRICOVA niveau 4 op het Arenal (R13 §12) | Werkt de dienst weer, of is hij vervallen? Mag dpmt.zip (12,2 MB) worden gedownload (akkoord Jan)? Classificatie van l'Arenal op 29-07-1988: servidumbre van 20 of 100 m (R13 §12) | Werkt de dienst weer, of is hij gemigreerd? Adres van de DPH-laag; afstand tot waterlopen per perceel (servidumbre 5 m, zona de policía 100 m) |
| **Operationele status** | **TECHNISCH ONDERZOEK NODIG** | **TECHNISCH ONDERZOEK NODIG** | **TECHNISCH ONDERZOEK NODIG** |

| Veld | R2-66 IGME — geologische kaart 1:50.000 (GEODE en MAGNA, WMS) | R2-67 GVA — Registro Autonómico de Instrumentos de Planeamiento, map Xàbia (open directory) | R2-68 DOGV — Diari Oficial de la Generalitat Valenciana (pdf-archief) |
|---|---|---|---|
| Naam en officiële website | https://mapas.igme.es/gis/services/Cartografia_Geologica/IGME_Geode_50/MapServer/WMSServer · https://mapas.igme.es/gis/services/Cartografia_Geologica/IGME_MAGNA_50/MapServer/WMSServer | https://mediambient.gva.es/auto/urbanismo/reg-planeamiento/2%20ALICANTE/03082%20X%C0BIA/ | dogv.gva.es (pdf-archief; voorbeeld https://dogv.gva.es/datos/2021/09/20/pdf/docv_9177.pdf) |
| Type aanbieder | Officiële geologische kaartdienst van het Instituto Geológico y Minero de España (type 2) | Officieel register van planinstrumenten van de Generalitat Valenciana; primaire planbron (type 2) | Officieel publicatieblad van de Generalitat Valenciana (type 2) |
| Geografische en inhoudelijke dekking | Spanje, schaal 1:50.000. GEODE-lagen o.a. 0 Zonas, 1 Recintos geología, 3 Cuaternario. Testpunten: Arenal 'Limos de albufera' (Holoceen), Granadella 'Calizas, calizas margosas y margas. Albiense-Cenomaniense', Montgó-flank 'Depósitos aluviales, fondo de valle'. Geen juridische werking; geen geotechnische dienst gevonden (R13 §7, §8.2, type 3; per punt niet hercontroleerd in R13-verificatie §3) | Xàbia: map P. GENERAL met 34 submappen (NUTU, Plan General en 32 wijzigingen of homologaciones) en P. DIFERIDO; o.a. PGOU-ordenanzas (240 blz.), Mod. XXV (BOP nº 240, 16-12-2016) en de vernietigde homologación Portitxol. Onvolledig: PP Ermita II en PP La Guardia-3 zonder documenten, 'PGOU UA BALCON AL MAR 1' niet in de lijst, geen PGE (R12 §1.3, §8; R12-verificatie F6, R12-02; 03 §2.2, type 2/3) | Comunitat Valenciana: regionale besluiten en plannen. Gebruikt: DOGV 9041 (15-03-2021, schorsing PGOU Xàbia), DOGV 9177 (20-09-2021, NUT Xàbia), DOGV 4374 (08-11-2002, PORN Montgó), Decreto 197/2022 (28-11-2022, ZEC/ZEPA Penya-segats de la Marina), PLPIF Jávea (29-07-2020) en DOGV 10093 (23-04-2025, pliego verkoop GVA-patrimonium) (R12 §8; R12-verificatie R12-01, R12-03; 03 §2.2; R08 §5, type 2) |
| Technische toegang | WMS GetCapabilities HTTP 200 en GetFeatureInfo op laag 1, zonder sleutel (R13 §7, type 3) | Open HTTP-directory zonder sleutel; pdf-scans zonder tekstlaag, dus OCR nodig (R12 gebruikte de ingebouwde macOS Vision; OCR-fouten in tabellen gemarkeerd [OCR]) (R12 §8, §10, type 3) | Pdf's open te downloaden; de zoekfunctie ('ficha_disposicion') laadt in een iframe en was voor ons niet bruikbaar (R12 §8, §10, type 3) |
| Beschikbare velden | Geologische eenheid (omschrijving en tijdperk) per punt | Documenten per instrument: aprobación, publicatie in BOP of DOGV, normas urbanísticas, plano's | Volledige tekst van besluiten (pdf) |
| Foto's en documenten | Kaartbeeld; geen documenten | Pdf-scans: normen, publicaties en plano's B.1–B.3 (niet gegeorefereerd); uitspraken zoals TSJCV 459/2012 over Portitxol (R12-verificatie R12-17; 03 stap 9) | Pdf per uitgave of per besluit |
| Publicatie- en wijzigingsinformatie | ONBEKEND | Datum per document in de publicatie; registerdatum ONBEKEND | Publicatiedatum en nummer per uitgave |
| Historische gegevens | ONBEKEND | Instrumenten sinds het PGOU 1990/1991, voor zover opgenomen | Archief per datum (o.a. uitgaven uit 1991, 2002 en 2020–2025 geraadpleegd) |
| Verversingsfrequentie | ONBEKEND | ONBEKEND | Per uitgave; frequentie niet vastgelegd |
| Rate limits | Niet gepubliceerd (ONBEKEND) | Niet gepubliceerd | ONBEKEND |
| Kosten | Geen kosten of sleutel gezien (type 3) | Gratis | Gratis |
| Contractstatus | Voorwaarde in de dienst: 'No está permitido implementar un servicio de valor añadido no gratuito sin establecer contacto con el IGME' (R13 §7, type 2) | n.v.t.; geen gebruiksvoorwaarden gelezen | n.v.t.; geen gebruiksvoorwaarden gelezen |
| Toegestane gebruiksdoelen | Optionele technische laag in het perceeldossier; bij commercieel gebruik eerst contact met het IGME; of intern gebruik onder die voorwaarde valt is [te verifiëren] (R13 §11; 05 §3.4). Vervangt geen grondonderzoek (R13 §8.2) | Handmatig: bron voor de versiebeheerde regeltabel en de documentstatustabel (05 §3.4; 03 stap 9) — Statusnoot: R12 §8 gaf GEVERIFIEERD EN ACTIEF; hier ALLEEN HANDMATIG volgens 05 §3.4 | Handmatig: planstatus en schorsingen maandelijks controleren, samen met BOP en pers (R12 §7). BOP Alicante heeft al een regel (R2-42) en is ook de bron voor planpublicaties zoals Mod. XXV (BOP nº 240, 16-12-2016) — Statusnoot: R12 §8 gaf GEVERIFIEERD EN ACTIEF; hier ALLEEN HANDMATIG, want er draait niets |
| Rechten AI-analyse | ONBEKEND | Binnen Ley 37/2007 (R16 §5.2, toepassing type 4); geen persoonsgegevens | Binnen Ley 37/2007 (R16 §5.2, toepassing type 4) |
| Opslag en bewaren | ONBEKEND | Documenten en eigen regeltabel met bronpagina; namen van particuliere bezwaarmakers niet overnemen (R12-verificatie) | Besluittekst en eigen samenvatting met bron; geen persoonsgegevens uit andere besluiten |
| Afgeleide gegevens en beeldvergelijking | ONBEKEND; een betaalde dienst met toegevoegde waarde alleen na contact met het IGME | Met bronvermelding; het register is onvolledig, dus 'niet gevonden' bewijst geen afwezigheid | Met bronvermelding |
| Contactpersoon of aanvraagroute | IGME (contactroute niet vastgelegd in R13) | Conselleria (register); per perceel het Ajuntament de Xàbia (R2-69) | n.v.t. |
| Laatste verificatie | 15-09-2026 | 15-09-2026 | 15-09-2026 |
| Openstaande vragen | Valt interne analyse in Deal Hunter onder de contactplicht? Mogen uitkomsten in klantdossiers? | Normen van PP Ermita II, PP La Guardia-3 en UA Balcón al Mar 1 (niet in het register); geen geconsolideerde tekst van de ordenanzas; wie keurde Mod. I formeel goed (DOGV 2227 [te verifiëren]) | Gelden de NUT (DOGV 9177) na ca. 15-03-2025 nog (type 7)? Is de zoekfunctie in een gewone browser bruikbaar? |
| **Operationele status** | **TECHNISCH ONDERZOEK NODIG** | **ALLEEN HANDMATIG** | **ALLEEN HANDMATIG** |

| Veld | R2-69 Ajuntament de Xàbia — urbanisme: sede electrónica (transparencia, ordenanzas, tasas, trámites) en ajxabia.com | R2-70 SUMA Gestión Tributaria (Diputación de Alicante) — suma.es, pagina veilingen en adjudicación directa | R2-71 ATV — Agència Tributària Valenciana (veilingkanaal gezocht) |
|---|---|---|---|
| Naam en officiële website | https://xabia.sedelectronica.es/transparency/9dc46a0e-8b13-4022-824e-000f75336158/ · https://www.ajxabia.com/ver/7823/el-pleno-aprueba-la-propuesta-definitiva-de-plan-general-estructural-.html/ | https://www.suma.es/procedimiento-subastas | https://atv.gva.es/ |
| Type aanbieder | Gemeente: sede electrónica (esPublico Gestiona) en persberichten van de gemeente (type 2) | Officiële provinciale belastinginvordering (type 2) | Officiële regionale belastingdienst (type 2) |
| Geografische en inhoudelijke dekking | Xàbia. Transparencia: rubriek '2.3.4. Tasas' met 27 documenten, plus 11 over impuestos en 12 over precios públicos; ordenanzas fiscales en trámites van Urbanismo niet gelezen; loket voor informe urbanístico en cédula de garantía urbanística (art. 246 TRLOTUP, termijn 1 maand). Het tablón van dezelfde sede staat in R2-42 (R12 §8; R12-verificatie R12-14, A5; 03 stap 12, type 2/3) | Provincie Alicante. De veilingen zelf staan op het BOE-portaal als SUB-RC ('Otras administraciones tributarias'): 17 loten 'próxima apertura' op 14 en 15-09-2026, met 17 aparte BOE V-B-aankondigingen (BOE-B-2026-29821 t/m 29837, gedateerd 29-06 of 22-07-2026). suma.es toont alleen informatie en een adjudicación directa als die openstaat; op 14 en 15-09-2026 'NO HAY ABIERTO PROCEDIMIENTOS EN PLAZO' (R08 §4; R08-verificatie R08-10, A3, type 2/3) | Comunitat Valenciana. Geen pagina over veilingen of vervreemding van beslagen goederen gevonden; wel pagina's over providència d'apremi, diligència d'embargament en modelo 603 (aangifteplicht voor organisatoren van veilingen van roerende zaken, geen veilingkanaal) (R08 §5, type 3/7) |
| Technische toegang | HTML leesbaar; documenten openen via Wicket-AJAX-links met sessietokens, niet nagebootst; /info.0 gaf 'Too many redirects'; urbanismo-pagina's van ajxabia.com verwijzen naar hetzelfde portaal. Handmatig in een browser (R12 §10; R12-verificatie F10, type 3) | HTML; robots.txt 'User-agent: * Disallow: /' (Googlebot deels toegestaan); geen meldingen of RSS (R08 §4, type 3) | Website; geen veilingkanaal gevonden (R08 §5, type 3) |
| Beschikbare velden | Ordenanzas en tasas (pdf), trámites, persberichten met datum | Procedure-informatie; bij een open adjudicación directa de loten | ONBEKEND |
| Foto's en documenten | Pdf-documenten per rubriek | ONBEKEND | ONBEKEND |
| Publicatie- en wijzigingsinformatie | Datum per document of persbericht | Alleen bij een lopende procedure | ONBEKEND |
| Historische gegevens | ONBEKEND | In 2011–2014 publiceerde SUMA veilingaankondigingen als BOE-B-anuncio (R08 §4) | ONBEKEND |
| Verversingsfrequentie | ONBEKEND | ONBEKEND | ONBEKEND |
| Rate limits | n.v.t. (handmatig) | robots.txt sluit alle bots uit | ONBEKEND |
| Kosten | Raadplegen gratis; tasa voor informe urbanístico, cédula en licentie ONBEKEND (R12-verificatie R12-14) | Veiling: waarborg minimaal 5 % van het tipo, 20 kalenderdagen, sluiting pas een uur na het laatste bod, betaling binnen 15 dagen na notificatie. Adjudicación directa: minimum de valoración van het lot, waarborg 5 %, één maand (R08-verificatie R08-10, A8, type 2) | ONBEKEND |
| Contractstatus | n.v.t. | n.v.t. | n.v.t. |
| Toegestane gebruiksdoelen | Handmatig raadplegen; een informe urbanístico of cédula per perceel aanvragen is een handeling van Jan of zijn architect (03 stap 12; 05 §3.4 poort 2) | Handmatig; SUMA-veilingen worden gevolgd via het portaal (R2-35) en BOE V-B (R2-36) | ONBEKEND |
| Rechten AI-analyse | Binnen Ley 37/2007 (R16 §5.2, toepassing type 4) | ONBEKEND | ONBEKEND |
| Opslag en bewaren | Documenten met bron in het dossier; geen persoonsgegevens (edictos met NIF's in dezelfde sede: zie R2-42) | ONBEKEND | ONBEKEND |
| Afgeleide gegevens en beeldvergelijking | Met bronvermelding | ONBEKEND | ONBEKEND |
| Contactpersoon of aanvraagroute | Ajuntament de Xàbia, Urbanisme en Gestió Tributària (via de sede) | adjudicacion.directa@suma.es (zakelijk, R08 §4) | Navragen bij de ATV (route niet vastgelegd) |
| Laatste verificatie | 15-09-2026 | 15-09-2026 | 14-09-2026 (R08; niet hercontroleerd in de verificatie) |
| Openstaande vragen | Hoogte van de tasas voor licentie, DR, cédula en informe; texto refundido van de normas urbanísticas als pdf; bestaat 'Cartoxabia' (gemeentelijke GIS, genoemd in 2018; R12 §8: TECHNISCH ONDERZOEK NODIG)? | Valt de gemeentelijke invordering van Xàbia onder SUMA? Het tablón van Xàbia toont eigen apremio-edictos [te verifiëren] (R08 §4) | Veilt de ATV via het BOE-portaal (filter 'Otras administraciones tributarias' met autoridad ATV)? ITP-grondslag bij veiling volgens de praktijk van de ATV [te verifiëren] (05 §3.5) |
| **Operationele status** | **ALLEEN HANDMATIG** | **ALLEEN HANDMATIG** | **TECHNISCH ONDERZOEK NODIG** |

| Veld | R2-72 Generalitat Valenciana — verkoop van eigen patrimonium (subastas, hisenda.gva.es) | R2-73 Patrimonio del Estado — Buscador de Subastas y Concursos (Ministerio de Hacienda) | R2-74 TEJU — Tablón Edictal Judicial Único (BOE) |
|---|---|---|---|
| Naam en officiële website | https://hisenda.gva.es/es/web/subastas | https://www.hacienda.gob.es/es-ES/Areas%20Tematicas/Patrimonio%20del%20Estado/Gestion%20Patrimonial%20del%20Estado/Paginas/Subastas/BuscadorSubastasConcursos.aspx | https://www.boe.es/edictos_judiciales · https://www.boe.es/buscar/ayudas/edictos_judiciales_ayuda.php |
| Type aanbieder | Officieel, Conselleria de Economía, Hacienda y Administración Pública (type 2) | Officieel: verkoop van rijksvastgoed (type 2) | Officieel elektronisch tablón voor gerechtelijke edicten, beheerd door de AEBOE (type 2) |
| Geografische en inhoudelijke dekking | Comunitat Valenciana: inmuebles, vehículos, acciones en muebles; rubrieken 'Enajenación efectuada' (historie) en 'Previsión de inmuebles para enajenar'. Inmuebles-lijst: 53 resultaten over 3 pagina's; pagina 1 (20 resultaten) zonder Alicante of Xàbia, pagina 2–3 niet bekeken (14-09-2026) (R08 §5; 04 §2.2 nr. 14, type 2/3) | Spanje, per Delegación de Economía y Hacienda (ALACANT/ALICANTE aanwezig); resultaten gesorteerd op veilingdatum. Aankondigingen verschijnen ook in BOE V-B (bijv. Cádiz 11-09 en Cuenca 14-09-2026) (R08 §7, type 2/3) | Spanje, sinds 01-06-2021 (RD 181/2008 art. 14 en 17): notificatie-edicten, geen veilingaankondigingen; die lopen via BOE Sección IV en het portaal (R08 §8; 04 §2.2 nr. 16, type 2/3) |
| Technische toegang | HTML-lijst; geen RSS of alerts (R08 §5, type 3) | ASP.NET-zoekformulier; 'RSS del Ministerio' alleen algemeen (R08 §7, §9, type 3) | HTML-zoekfunctie met filters (tekst inclusief personen, bedrijf, procedurenummer, NIG en NIF/NIE; órgano, jurisdicción, nummer, datum); geen RSS of API; robots.txt van boe.es sluit /edictos_judiciales/ uit (R08 §8; R16 §2.5 B-7, type 3) |
| Beschikbare velden | Per object op de lijst; documentatie anexos I–III (docx) | Per aankondiging (niet uitgewerkt) | Edicten per orgaan en procedure |
| Foto's en documenten | Pliego de condiciones generales (DOGV 10093, 23-04-2025); anexos I–III | ONBEKEND | Edicttekst |
| Publicatie- en wijzigingsinformatie | ONBEKEND | Veilingdatum per resultaat | Publicatiedatum; 4 maanden vrij toegankelijk, daarna met verificatiecode |
| Historische gegevens | Rubriek 'Enajenación efectuada' | ONBEKEND | 4 maanden vrij toegankelijk |
| Verversingsfrequentie | ONBEKEND; voorgesteld: handmatige controle per maand (R08 §5) | ONBEKEND | Doorlopend |
| Rate limits | ONBEKEND | ONBEKEND | robots.txt sluit het pad uit |
| Kosten | Volgens het pliego (niet uitgewerkt) | ONBEKEND | Gratis |
| Contractstatus | n.v.t. | n.v.t. | n.v.t. |
| Toegestane gebruiksdoelen | Handmatig (maandelijks) | Handmatig; de BOE V-B-aankondigingen komen al via R2-36 binnen | Hooguit handmatig per concreet dossier; niet geautomatiseerd inlezen en geen namen of NIF's opslaan (04 §2.10) |
| Rechten AI-analyse | ONBEKEND | ONBEKEND | Niet: bevat persoonsgegevens (04 §2.10) |
| Opslag en bewaren | ONBEKEND | ONBEKEND | Niet opslaan (04 §2.10) |
| Afgeleide gegevens en beeldvergelijking | ONBEKEND | ONBEKEND | Geen; geen persoonsprofielen (masterprompt §19) |
| Contactpersoon of aanvraagroute | Algemeen informatienummer 012 van de Generalitat (R08 §5) | Delegación de Economía y Hacienda in Alicante (route niet vastgelegd) | n.v.t. |
| Laatste verificatie | 14-09-2026 (R08; niet hercontroleerd in de verificatie) | 14-09-2026 (R08; niet hercontroleerd in de verificatie) | 14-09-2026 (R08; niet hercontroleerd in de verificatie) |
| Openstaande vragen | Staan er op pagina 2–3 objecten in Alicante of Xàbia? | Actuele objecten in de provincie Alicante (niet geteld) | Geen |
| **Operationele status** | **ALLEEN HANDMATIG** | **ALLEEN HANDMATIG** | **ALLEEN HANDMATIG** |

| Veld | R2-75 ORGA — veilingen van in beslag genomen goederen; FAQ-pdf van het Ministerio de Justicia (2018) |
|---|---|
| Naam en officiële website | https://www.mjusticia.gob.es/es/AreaTematica/OficinaRecuperacion/Documents/1292428756586-Preguntas_frecuentes_en_subastas_electronicas.PDF |
| Type aanbieder | Officieel informatiedocument van de Oficina de Recuperación y Gestión de Activos (type 2) |
| Geografische en inhoudelijke dekking | ORGA-veilingen (RD 948/2015) van in beslag genomen goederen uit strafzaken, op het BOE-portaal: 10 werkdagen voor roerende zaken en voertuigen, 40 werkdagen voor onroerend goed, waarborg volgens de ORGA, verlenging met een uur tot maximaal 24 uur. Gaat niet over LEC-executies en noemt geen 5 % (R08-verificatie R08-12, A12; 04 §2.4.5, type 2) |
| Technische toegang | Pdf (aangemaakt 16-04-2018) |
| Beschikbare velden | n.v.t. (regels, geen objecten) |
| Foto's en documenten | Pdf |
| Publicatie- en wijzigingsinformatie | Aangemaakt 16-04-2018; actualiteit ONBEKEND (R08 bronnenlijst: verouderd, type 7) |
| Historische gegevens | n.v.t. |
| Verversingsfrequentie | ONBEKEND |
| Rate limits | n.v.t. |
| Kosten | Gratis |
| Contractstatus | n.v.t. |
| Toegestane gebruiksdoelen | Alleen als achtergrond bij ORGA-regels; NIET GEBRUIKEN als bron of rekenregel voor gerechtelijke (LEC-)veilingen. ORGA-veilingen zelf via R2-35, handmatig (04 §2.11; R08-verificatie F10) |
| Rechten AI-analyse | ONBEKEND |
| Opslag en bewaren | ONBEKEND |
| Afgeleide gegevens en beeldvergelijking | ONBEKEND |
| Contactpersoon of aanvraagroute | n.v.t. |
| Laatste verificatie | 15-09-2026 (R08-verificatie) |
| Openstaande vragen | Actuele ORGA-regels (de pdf is van 2018) |
| **Operationele status** | **NIET GEBRUIKEN** |

#### Rechtenvlaggen per bron

Machineleesbaar in `bronnenregister.json`, waar elke regel ook de onderbouwing (`rights_basis`, met bestand en sectie), de bewijstypen (`evidence_type`) en de bron-URL's (`source_urls`) heeft. Ingevuld op basis van R16 (compliance-matrix §6.1, §3.8, §8) en de onderzoeksrapporten met hun verificaties; zonder bron staat er unknown.

**Wat de vlaggen betekenen.** `automated_access`: geplande of geautomatiseerde raadpleging door een adapter · `storage`: brongegevens opslaan buiten link, bron-ID en eigen oordeel · `history`: historie opbouwen (momentopnamen, prijs- of statusverloop) · `ai_analysis`: AI-analyse van de inhoud buiten een handmatige sessie · `image_hashing`: foto's downloaden en beeldkenmerken (hashes) berekenen en bewaren · `show_to_clients`: broninhoud tonen aan klanten of investeerders (niet alleen eigen analyse) · `personal_data`: verwerken zonder persoonsgegevensbeletsel.

**Waarden.** yes = de licentie of tekst staat het toe, hooguit met bronvermelding · conditional = alleen onder de voorwaarde in `rights_basis` (bijvoorbeeld laag volume, per object, alleen link en eigen oordeel, alleen objectvelden, alleen met vermelding) · no = een tekst verbiedt het, of R16 noemt het niet toegestaan · unknown = geen tekst of afspraak gevonden, of niet van toepassing (bron zonder foto's). Bij `personal_data`: yes = geen persoonsvelden of alleen zakelijke contactgegevens; conditional = de bron bevat persoonsgegevens, dus alleen objectvelden met privacyfilter en namen hooguit afgeschermd met verwijderdatum; no = persoonsgegevens uit deze bron niet verwerken. Een adapter weigert bij unknown of no (R16 §6.5; 04 §2.10 punt 6). De vlaggen vervangen de operationele status niet: die staat in §2.1 en in de blokken hierboven.

| id | Bron | automated_access | storage | history | ai_analysis | image_hashing | show_to_clients | personal_data |
|---|---|---|---|---|---|---|---|---|
| R2-01 | Background Properties-feed | conditional | unknown | unknown | unknown | unknown | unknown | unknown |
| R2-02 | Idealista-assistent | no | conditional | no | unknown | no | no | conditional |
| R2-03 | idealista.com, alerts, prijsrapporten | no | conditional | no | no | no | no | conditional |
| R2-04 | Idealista Search API | unknown | unknown | unknown | unknown | unknown | unknown | unknown |
| R2-05 | idealista/data | unknown | unknown | unknown | unknown | unknown | unknown | unknown |
| R2-06 | idealista/tools, Market Navigator | unknown | unknown | unknown | unknown | unknown | unknown | unknown |
| R2-07 | Fotocasa en Habitaclia | no | conditional | no | no | no | conditional | conditional |
| R2-08 | Milanuncios | no | conditional | no | no | no | conditional | conditional |
| R2-09 | DataVenues | unknown | unknown | unknown | unknown | unknown | unknown | unknown |
| R2-10 | Kyero | no | conditional | no | no | no | conditional | unknown |
| R2-11 | thinkSPAIN | no | conditional | no | no | no | conditional | unknown |
| R2-12 | pisos.com | no | conditional | no | no | no | conditional | conditional |
| R2-13 | yaencontre | no | conditional | no | no | no | conditional | unknown |
| R2-14 | SpainHouses | no | conditional | no | no | no | conditional | unknown |
| R2-15 | Green-Acres | no | conditional | no | no | no | conditional | unknown |
| R2-16 | Indomio | no | conditional | no | no | no | conditional | unknown |
| R2-17 | Scraper-"API's" | no | no | no | no | no | no | no |
| R2-18 | Casafari | unknown | unknown | unknown | unknown | unknown | unknown | unknown |
| R2-19 | Brainsre | unknown | unknown | unknown | unknown | unknown | unknown | unknown |
| R2-20 | Accumin (uDA, Tinsa Digital) | unknown | unknown | unknown | unknown | unknown | unknown | unknown |
| R2-21 | Tinsa Radar en IMIE | unknown | unknown | unknown | unknown | unknown | unknown | unknown |
| R2-22 | Gloval | unknown | unknown | unknown | unknown | unknown | unknown | unknown |
| R2-23 | Grupo ST | unknown | unknown | unknown | unknown | unknown | unknown | unknown |
| R2-24 | Resales-Online | unknown | unknown | unknown | unknown | no | conditional | unknown |
| R2-25 | MLS 03724 Teulada-Moraira | unknown | unknown | unknown | unknown | unknown | unknown | unknown |
| R2-26 | MLS Costa, Mediaelx, Denia Realtor | unknown | unknown | unknown | unknown | unknown | unknown | unknown |
| R2-27 | APIred / Apibolsa | unknown | unknown | unknown | unknown | unknown | unknown | unknown |
| R2-28 | Agora MLS, Inmobalia | unknown | unknown | unknown | unknown | unknown | unknown | unknown |
| R2-29 | CRM-exports van makelaars | unknown | unknown | unknown | unknown | unknown | unknown | unknown |
| R2-30 | Servihabitat (+ Profesionales) | no | conditional | no | no | no | conditional | unknown |
| R2-31 | Solvia (incl. Haya) | no | conditional | no | no | no | conditional | unknown |
| R2-32 | Diglo (Santander) | no | conditional | no | no | no | conditional | unknown |
| R2-33 | Overige servicer- en bankportalen | no | conditional | no | no | no | conditional | unknown |
| R2-34 | NPL's, cesiones de remate | no | no | no | no | no | no | no |
| R2-35 | Portal de Subastas del BOE | no | conditional | conditional | conditional | unknown | conditional | conditional |
| R2-36 | BOE open data (sumario, RSS) | conditional | yes | yes | yes | unknown | conditional | conditional |
| R2-37 | AEAT bienes.js | yes | yes | yes | yes | unknown | conditional | conditional |
| R2-38 | TGSS-veilingen | unknown | conditional | unknown | conditional | unknown | unknown | conditional |
| R2-39 | Registro Público Concursal | no | conditional | unknown | unknown | unknown | no | no |
| R2-40 | subastasprocuradores.com | unknown | unknown | unknown | unknown | unknown | unknown | unknown |
| R2-41 | eActivos | no | unknown | unknown | unknown | no | no | unknown |
| R2-42 | Xàbia tablón, PLACSP, BOP | unknown | conditional | unknown | conditional | unknown | conditional | conditional |
| R2-43 | Catastro webservices en INSPIRE | conditional | yes | yes | yes | unknown | conditional | conditional |
| R2-44 | Catastro Sede | no | conditional | unknown | conditional | unknown | conditional | conditional |
| R2-45 | Registro de la Propiedad | no | conditional | no | conditional | unknown | unknown | conditional |
| R2-46 | MIVAU | conditional | conditional | conditional | conditional | unknown | conditional | yes |
| R2-47 | INE | yes | yes | yes | yes | unknown | conditional | yes |
| R2-48 | Portal Estadístico del Notariado | no | no | no | no | unknown | no | yes |
| R2-49 | Registradores-statistiek | no | unknown | unknown | unknown | unknown | unknown | yes |
| R2-50 | Lokale makelaarssites (79 kantoren, tabel K-1) | no | conditional | no | no | no | conditional | conditional |
| R2-51 | Directories en gemeentelijke lijst (xabia.org, Trustlocal, Javea Guide, Jávea.com) | unknown | conditional | unknown | conditional | unknown | unknown | conditional |
| R2-52 | Rechtstreekse aanlevering door partners (eigen dealflow) | unknown | unknown | unknown | unknown | unknown | unknown | conditional |
| R2-53 | MLS Dénia | unknown | unknown | unknown | unknown | unknown | unknown | unknown |
| R2-54 | ASICVAL | unknown | unknown | unknown | unknown | unknown | unknown | unknown |
| R2-55 | RAICV (register vastgoedbemiddelaars) | unknown | conditional | unknown | unknown | unknown | unknown | conditional |
| R2-56 | Ontwikkelaarssites (7 partijen, tabel K-2) | no | conditional | no | no | no | conditional | conditional |
| R2-57 | PROVIA (promotoren Alicante) | unknown | conditional | unknown | unknown | unknown | unknown | conditional |
| R2-58 | Architecten-colegios (CTAA, COAT Alicante) | unknown | conditional | unknown | unknown | unknown | unknown | conditional |
| R2-59 | Wallapop en Facebook-groepen | no | conditional | no | no | no | conditional | conditional |
| R2-60 | ICV-planlaag Planeamiento (0702) | yes | yes | yes | yes | unknown | conditional | conditional |
| R2-61 | ICV-sectorlagen 0701, 0505, 0506 (o.a. PATRICOVA) | yes | yes | yes | yes | unknown | conditional | yes |
| R2-62 | ICV ArcGIS REST (ordenación territorial, espacios protegidos, incendios) | unknown | unknown | unknown | unknown | unknown | unknown | yes |
| R2-63 | IDEE ARPSI | yes | yes | yes | yes | unknown | conditional | yes |
| R2-64 | MITECO kustdomein DPMT | unknown | unknown | unknown | unknown | unknown | unknown | unknown |
| R2-65 | MITECO waterlopen DPH en SNCZI | unknown | unknown | unknown | unknown | unknown | unknown | unknown |
| R2-66 | IGME geologische kaart (GEODE, MAGNA) | conditional | unknown | unknown | unknown | unknown | unknown | yes |
| R2-67 | GVA-planregister Xàbia | unknown | conditional | conditional | conditional | unknown | conditional | conditional |
| R2-68 | DOGV | unknown | conditional | conditional | conditional | unknown | conditional | conditional |
| R2-69 | Xàbia sede en urbanismepagina's | unknown | conditional | conditional | conditional | unknown | conditional | conditional |
| R2-70 | SUMA (suma.es) | no | unknown | unknown | unknown | unknown | unknown | unknown |
| R2-71 | ATV | unknown | unknown | unknown | unknown | unknown | unknown | unknown |
| R2-72 | GVA-patrimonium (hisenda.gva.es) | unknown | unknown | unknown | unknown | unknown | unknown | unknown |
| R2-73 | Patrimonio del Estado | unknown | unknown | unknown | unknown | unknown | unknown | unknown |
| R2-74 | TEJU (gerechtelijke edicten) | no | no | no | no | unknown | no | no |
| R2-75 | ORGA FAQ-pdf | unknown | unknown | unknown | unknown | unknown | unknown | unknown |

---

## Bijlage C — Bronnenlijst (URL · controledatum · bewijstype)

**Onderzoeksbestanden (intern, volledig gelezen op 15-09-2026):** `onderzoek/R01-idealista.md` en `.verificatie.md` · `R02-adevinta-fotocasa-habitaclia-datavenues` · `R03-overige-portalen` · `R04-dataleveranciers-mls-statistiek` · `R05-background-properties` · `R06-makelaars-javea-register` · `R07-netwerken-ontwikkelaars-dealflow` · `R08-veilingen-portalen-toegang` · `R10-banken-servicers-fondsen` · `R11-catastro-registro-perceelidentificatie` · `R16-rechten-en-compliance` (steeds rapport + verificatie); voor K10 ook `R15-kandidaten-javea-live.verificatie.md`. Controledata van de externe bronnen hieronder zijn die van de laatste controle in die bestanden.

**Eigen controle deze deliverable**
- http://127.0.0.1:3100/api/stats en /api/properties?town=Javea&limit=100 (eigen dienst, alleen lezen; ook town=Jávea, Xàbia, Xabia → 0) · 15-09-2026 03:56 en 04:46 CEST · 3

**Background Properties**
- https://backgroundproperties.com/aviso-legal/ · 15-09-2026 · 2
- https://backgroundproperties.com/makelaars/ en https://backgroundproperties.com/wp-json/wp/v2/pages?slug=makelaars · 14-09-2026 · 1/3
- https://backgroundproperties.com/en/access/ · 14-09-2026 · 1
- Export-URL's 26, 27, 29, 30, 31, 32 (headers, sleutels niet opgenomen) · 14-09-2026 · 3
- https://ikzoekeenhuisinspanje.nl/woning/land-in-javea-alicante-bp-4676jav/ · 14-09-2026 · 3

**Idealista**
- https://developers.idealista.com/access-request · 15-09-2026 · 2/3
- https://www.idealista.com/data/ en https://www.idealista.com/data/asesoramiento-inmobiliario-tecnologico/api-comparables-y-metricas/ · 15-09-2026 · 2
- https://st1.idealista.com/ayuda/wp-content/uploads/2021/11/2021-Hasta-11-11-2021-Terminos-y-condiciones.pdf (versie 20-11-2020) · 15-09-2026 · 2
- https://st1.idealista.com/ayuda/wp-content/uploads/2025/04/Condiciones-generales-vigentes-hasta-29.04.2025-idealista.pdf (versie 17-02-2024, OCR) · 15-09-2026 · 2
- https://www.idealista.com/ayuda/articulos/legal-statement/ (HTTP 403) · 15-09-2026 · 7
- https://www.idealista.com/robots.txt · 15-09-2026 · 3
- https://st3.idealista.com/static/es/pdf/es/servicios_profesionales_idealista.pdf (nov. 2022) · 15-09-2026 · 2
- https://www.idealista.com/en/news/property-for-sale-in-spain/2026/03/13/887103-idealista-launches-its-app-on-chatgpt · 15-09-2026 · 2
- https://www.idealista.com/news/inmobiliario/vivienda/2026/09/02/912069-el-precio-de-la-vivienda-acumula-20-meses-de-subidas-anuales-a-doble-digito-tras-el · 15-09-2026 · 2
- Idealista-assistent (MCP): search_properties en property_detail, zoek-URL's o.a. https://www.idealista.com/es/venta-viviendas/javeaxabia-alicante/con-chalets,para-reformar/ · 15-09-2026 · 1/3

**Fotocasa Group, Milanuncios, DataVenues**
- https://www.habitaclia.com/hab_cliente/legalavisocontentmodal.asp · 15-09-2026 · 2
- https://www.fotocasa.es/es/aviso-legal/ln (tekst alleen via JavaScript) · 15-09-2026 · 3
- https://www.fotocasa.es/es/comprar/viviendas/javea-xabia/todas-las-zonas/l · …/a-reformar/l · https://www.fotocasa.es/es/comprar/terrenos/javea-xabia/todas-las-zonas/l · 15-09-2026 · 3
- https://www.fotocasa.es/es/indice-precio-vivienda/javea-xabia/todas-las-zonas · 15-09-2026 · 3
- https://www.fotocasa.es/fotocasa-life/fotocasa/fotocasa-renueva-alertas-ahora-mas-eficientes-ayudarte-encontrar-sitio/ · 15-09-2026 · 1
- https://www.habitaclia.com/viviendas-xabia.htm · https://www.habitaclia.com/terrenos_y_solares-xabia.htm · 15-09-2026 · 3
- https://www.milanuncios.com/venta-de-viviendas-en-javea%7Cxabia-alicante/ · https://www.milanuncios.com/robots.txt · https://www.milanuncios.com/legal/condiciones-uso (403) · 15-09-2026 · 3
- https://pro.fotocasa.es/soluciones-packs/ · https://pro.fotocasa.es/soluciones-fotocasa-pro-data/ · 15-09-2026 · 1
- https://datavenues.com/ · https://datavenues.com/contratacion/ · https://datavenues.com/aviso-legal/ · https://datavenues.com/productos/ · https://datavenues.com/faqs/ · 15-09-2026 · 1/2
- https://prensa.fotocasa.es/fotocasa-incorpora-el-precio-de-cierre-de-compraventa-del-consejo-general-del-notariado-en-su-herramienta-de-big-data-datavenues/ · 15-09-2026 · 1
- https://www.scout24.com/en/investor-relations/financial-news/ir-news/detail/scout24-maintains-strong-momentum-in-q2-with-20-revenue-growth-double-digit-organic-revenue-growth-and-18-adjusted-eps-growth · 15-09-2026 · 2

**Overige portalen**
- https://help.kyero.com/estate-agents/xml-import-specification · https://feeds.kyero.com/assets/kyero_v3_import_spec.txt · https://feeds.kyero.com/assets/kyeroV3.0.xsd · 15-09-2026 · 2/3
- https://help.kyero.com/how-often-my-xml-feed-is-updated · https://www.kyero.com/robots.txt · https://www.kyero.com/en/docs/terms/ (403) · 15-09-2026 · 2/3/7
- https://find-and-update.company-information.service.gov.uk/company/06536265 · 15-09-2026 · 2
- https://www.thinkspain.com/legal-info · https://www.thinkspain.com/property-for-sale/javea · 15-09-2026 · 2/3
- https://www.pisos.com/avisolegal · https://www.pisos.com/venta/pisos-xabia_javea/ · 15-09-2026 · 2/3
- https://www.yaencontre.com/robots.txt (403 DataDome) · 15-09-2026 · 3
- https://www.spainhouses.net/es/inmobiliarias/especificaciones-publicacion.html · https://www.spainhouses.net/en/sale-houses-javea-alicante.html · 15-09-2026 · 2/3
- https://www.green-acres.es/en/GatewayInfo · https://www.green-acres.es/en/terms-of-use · https://www.green-acres.es/robots.txt · https://www.green-acres.es/property-for-sale/javea-xabia · 15-09-2026 · 2/3
- https://feed.indomio.com/docs/ies/in/get-start · https://www.indomio.es/en/terms/ (403) · 15-09-2026 · 2/7
- https://docs.happyendpoint.com/fotocasa/ · https://apify.com/parsebird/fotocasa-scraper · 15-09-2026 · 1

**Dataleveranciers en MLS**
- https://www.casafari.com/products/property-data-api/ · https://www.casafari.com/faq/ · https://www.casafari.com/terms-of-use · 15-09-2026 · 1/2
- https://brainsre.com/ · 14-09-2026 · 1
- https://www.accumin.com/newsroom/corporate-actions/tinsa-digital-deyde-datacentric-and-urbandata-analytics-join-forces-in-accumin-intelligence · 15-09-2026 · 1
- https://radar.tinsa.es/es · https://www.tinsa.es/precio-vivienda/comunitat-valenciana/alicante/ · 15-09-2026 · 1
- https://www.gloval.es/servicios/big-data-del-mercado-inmobiliario/ · https://tools.st-tasacion.es/ · 14-09-2026 · 1
- https://support.resales-online.com/en/articles/4885689-terms-conditions-of-usage-resales-online · https://support.resales-online.com/en/articles/5682509-webapi-v6-full-documentation-for-web-developers · 15-09-2026 · 1
- https://www.mls03724.com/en/about-us/ · http://www.mls03724.com/aviso-legal/ · https://hispaniahomesmoraira.com/informe-del-mercado-inmobiliario-en-moraira-costa-blanca-norte/ · 15-09-2026 · 1
- https://www.mlscosta.com/ · https://mediaelx.net/en/mls-mediaelx/ · http://www.apired.com/ · https://www.apibolsa.es/bolsa-inmobiliaria-como-funciona-mls.html · 15-09-2026 · 1
- https://www.agoramls.es/inmobiliarias-alicante/ · https://www.inmobalia.com/ · 15-09-2026 · 1
- https://faq.witei.com/en/articles/865807-xml-export-with-your-properties · https://inmovilla.freshdesk.com/support/solutions/articles/103000118125-conectar-web-externa-con-inmovilla-api-xml-o-iframe · 15-09-2026 · 1

**Banken en servicers**
- https://inversores.servihabitat.com/es/venta/promociones/terreno-urbanonoconsolidado/alicante-marinaalta-balconalmarjavea/06124187 · …/alicante-huertasur-xabia/06124173 · 15-09-2026 · 1/3
- https://www.servihabitat.com/es/terminos-generales-de-uso · https://www.solvia.es/es/aviso-legal · https://digloservicer.com/aviso-legal · 15-09-2026 · 1
- https://www.idealista.com/es/venta-terrenos/alicante/marina-alta/con-de-bancos/ (assistent) · 15-09-2026 · 3
- https://www.boe.es/diario_boe/txt.php?id=BOE-A-2025-15292 (Orden PJC/784/2025) · https://www.boe.es/buscar/act.php?id=BOE-A-2012-14118 · 15-09-2026 · 2
- https://www.alisedainmobiliaria.com/robots.txt · https://www.alisedainmobiliaria.com/sitemap-loans.xml · 15-09-2026 · 3

**Veilingen en insolventie**
- https://subastas.boe.es/ayuda.php · https://subastas.boe.es/robots.txt · https://subastas.boe.es/subastas_ava.php · 15-09-2026 · 2/3
- https://www.boe.es/datosabiertos/api/boe/sumario/20260914 · https://www.boe.es/rss/boe.php?s=4 · https://www.boe.es/robots.txt · 15-09-2026 · 3
- https://www.boe.es/informacion/aviso_legal/index.php (hergebruiklicentie 27-06-2024) · 15-09-2026 · 2
- https://www2.agenciatributaria.gob.es/static_files/common/internet/dep/taiif/subastaInmuebles/data2/bienes.js · https://sede.agenciatributaria.gob.es/Sede/subastas.html · 15-09-2026 · 2/3
- https://w6.seg-social.es/subastas/ · https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-2004-11836/texto/bloque/a117 · 15-09-2026 · 2/3
- https://www.publicidadconcursal.es/aviso-legal · https://www.publicidadconcursal.es/consulta-publicidad-concursal-new · 15-09-2026 · 2
- https://www.subastasprocuradores.com/terms?culture=es · https://www.eactivos.com/aviso-legal · 15-09-2026 · 2
- https://xabia.sedelectronica.es/board · https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-1986-9865/texto/bloque/art80 · 15-09-2026 · 2/3

**Perceel, register en statistiek**
- https://ovc.catastro.meh.es/OVCServWeb/OVCWcfCallejero/COVCCallejero.svc/json/Consulta_DNPRC · https://ovc.catastro.meh.es/INSPIRE/wfsCP.aspx · 15-09-2026 · 3
- https://www.catastro.hacienda.gob.es/INSPIRE/CadastralParcels/03/ES.SDGC.CP.atom_03.xml · 15-09-2026 · 3
- https://www.catastro.hacienda.gob.es/ayuda/condicionesuso.htm · https://www.catastro.hacienda.gob.es/webinspire/documentos/Licencia.pdf · 15-09-2026 · 2
- https://www1.sedecatastro.gob.es/Accesos/SECAccvr.aspx · 15-09-2026 · 3
- https://www.registradores.org/en/-/cuando-cuesta-una-nota-simple-en-un-registro-de-la-propiedad · https://www.registradores.org/el-colegio/registro-de-la-propiedad · 15-09-2026 · 2
- https://www.boe.es/buscar/act.php?id=BOE-A-1946-2453 (Ley Hipotecaria art. 10.4) · https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-1947-3843/texto/bloque/a332 (RH art. 332) · 15-09-2026 · 2
- https://apps.fomento.gob.es/BoletinOnline2/?nivel=2&orden=34000000 · https://apps.fomento.gob.es/BoletinOnline2/sedal/35103500.XLS · https://datos.gob.es/es/catalogo/e05233601-transacciones-inmobiliarias-de-vivienda · 15-09-2026 · 2/3
- https://servicios.ine.es/wstempus/js/ES/TABLAS_OPERACION/IPV · 15-09-2026 · 3
- https://www.penotariado.com/inmobiliario/terminos-y-condiciones · 15-09-2026 · 2
- https://www.registradores.org/actualidad/portal-estadistico-registral/estadisticas-de-propiedad · https://opendata.registradores.org/ ("Request Rejected") · 15-09-2026 · 2/3

**Makelaars, directories en platforms (R06 en R06-verificatie)**
- https://trustlocal.es/alacant-alicante/xabia-javea/agencia-inmobiliaria/ · https://www.javeaguide.com/javea-estate-agents · https://en.javea.com/zona/comercios/inmobiliaria/agencia-inmobiliaria/ · 15-09-2026 · 1
- https://www.idealista.com/en/agencias-inmobiliarias/javeaxabia-alicante/inmobiliarias · https://www.kyero.com/en/spain/estate-agents/javea-l1895 · https://www.indomio.es/en/agencias-inmobiliarias/javea-xabia/ · https://www.yaencontre.com/inmobiliarias/javea-xabia (alle HTTP 403) · 15-09-2026 · 3
- Kantoorsites in tabel K-1, zelf geopend in de R06-verificatie: montgovillas.com, javeaimmo.com, villadomjavea.com, arzuagainmobiliaria.com, homestobehappy.com, javeacasas.com, selenhome.com, ferrando-moraira.com, benimo-villas.com, villamediterranea.es, agenciamorato.com, inmover.com, mgvillas.co.uk, bindleyproperties.com, holidaydream.es, terramar.es, klaus-hildenbrand.com, llidomarjavea.com, areacostablanca.es, calablanca.com, benitachellproperties.com, paradiserealestate.co.uk, arluxuryliving.com, crown-property.com, hamiltonsoflondon.net, villalux.com, xabiacasa.com, randofrealestate.com, javeacontinental.com, casascostablanca.nl, moraguespons.com (en /venta/villa/javea/a-reformar/), eurojavea.com, 123javeavillas.com, vicensash.com, coldwellbanker.es/inmobiliaria-javea-solaris, engelvoelkers.com (shop valencia-javea en munc-xabia), rimontgo.com/properties/javea/plots-and-lands, javeahomefinders.com, kv-realtors.com · 15-09-2026 · 3 (techniek) / 1 (inhoud)
- Overige kantoorsites uit R06 §3A/§3B (ahermar.com, altavillas.com, inmovillasjavea.com, deseohomes.com, atinainmobiliaria.com/javea, javeamia.com, grupo-garcia.es, luxiaproperties.com, xabiga.com, andreayolaf.com, solucionesinmojavea.com, casitasiberica.com, ashtonvillas.com, avcostamar.com, miralbo.com, plotsdirect.com, classandvillas.com, casas-ambiente.com, bocasa.nl, tabairarealestate.com, orangevillas.com, inmobiliariacelenia.com, lauravillas.com, mpvillas.com, fineandcountry.es, bhhscostablanca.com, mnmcostablanca.es, villalingo.com, alveo.co, spain-sothebysrealty.com, casasdediez.com, valuvillas.com) · 14-09-2026 · 3 / 1
- https://www.paagees.com/ · https://www.sooprema.com/ · 15-09-2026 · 1
- https://www.lucasfox.com/offices/jav.html (403) · https://www.classandvillas.com/en/news/inauguration-lucas-fox-javea-102.html · 15-09-2026 · 7 / 1
- Idealista-assistent (MCP), zoekopdrachten Jávea: "terreno urbano" (129), percelen ≥ 300.000 EUR (239), chalets "para reformar" (70), Puerto "para reformar" (15), "de bancos" woningen (0) en percelen (1) · 15-09-2026 · 1/3

**Netwerken, ontwikkelaars, dealflow en particuliere kanalen (R07 en R07-verificatie)**
- https://www.boe.es/buscar/act.php?id=BOE-A-2017-2421 (Ley 2/2017, DA 6ª) · 14-09-2026 · 2
- https://www.iberley.es/legislacion/decreto-98-2022-29-julio-consell-regula-registro-agentes-intermediacion-inmobiliaria-comunitat-valenciana-requisitos-inscripcion-27135412 (Decreto 98/2022, secundaire weergave) · 14-09-2026 · 2
- https://sede.gva.es/es/detall-tramit?id_proc=22848 · https://habitatge.gva.es/es/registres-en-materia-habitatge · 14-09-2026 · 2
- https://www.xabia.org/ver/2098/Real-estate-agents-and-promoters.html · 14-09-2026 · 2/3
- https://www.apialicante.com/registro-api-coapi-alicante/ · http://www.apired.com/ · https://inmodiario.com/187/26340/colegio-api-alicante-pone-marcha-bolsa-inmobiliaria/ · 14-09-2026 · 1
- https://asicval.es/ · https://www.mlsdenia.com/en/about-us/ · https://www.mlsdenia.com/ · https://www.deniacasas.es/en/mls-denia/ · https://www.mls03724.com/en/about-us/ · https://provia.es/ · 14-09-2026 · 1
- https://www.engelvoelkers.com/es/en/real-estate-agent/valencian-community/xabia · https://www.iadespana.es/en/find-real-estate-agent/xabia-javea-03730 · 14-09-2026 · 1
- https://www.ctaa.net/bolsa-servicios-ciudadanos · 14-09-2026 · 1
- Ontwikkelaars: zie de URL's in tabel K-2 · https://www.ehd.es/en/for-sale/ground-floor-apartment-in-residential-blooming-village-javea-5963/ · https://lamarina.eldiario.es/2026/04/16/el-urbanismo-voraz-de-xabia-complejos-de-lujo-se-alzan-a-velocidad-de-vertigo-al-lado-de-minipisos/ · 14-09-2026 · 1
- https://luxiaproperties.com/propiedad/parcela-en-venta-con-proyecto-y-licencia-en-puerta-fenicia-javea/ · https://www.inmovillasjavea.com/propiedad/venta-cami-cabanes-parcela-604163 · https://sixsecondsproperties.com/propiedad/1624/parcela-con-proyecto-y-licencia-en-javea-alicante/ · https://www.mgvillas.co.uk/plots-for-sale/ · 14-09-2026 · 1
- Architecten: https://vellomonfortarquitectes.com/ · https://arquitectosjavea.com.es/nuestra-empresas/ · https://studiobase.design/arquitectos-javea/ · https://innov-arq.com/en/architects-javea/ · 14-09-2026 · 1
- Idealista-assistent (MCP): property_detail 112280961, 112386422, 112297090, 112297374, 112447297, 112311948, 112278145 (Garroferal-perceel bij zeven kantoren); zoekopdracht obra nueva "proyecto paralizado" (66) · 14-09-2026 · 3
- https://www.boe.es/buscar/act.php?id=BOE-A-2002-13758&tn=1&p=20241224 (LSSI art. 21) · https://www.boe.es/buscar/act.php?id=BOE-A-2018-16673&tn=1&p=20230509 (LOPDGDD art. 19) · https://www.aepd.es/documento/2018-0164.pdf · 14-09-2026 · 2
- https://about.wallapop.com/en/legal-terms-and-conditions/ · https://es.wallapop.com/inmobiliaria/javea · https://www.facebook.com/terms.php?locale=en_US · 14-09-2026 · 1

**Eigendomsverschuivingen (§4) en bankperceel K10 (§2.5)**
- https://www.idealista.com/en/news/property-for-sale-in-spain/2024/12/05/821343-idealista-acquires-kyero · 15-09-2026 · 1
- https://www.servimedia.es/noticias/vocento-vende-habitat-soft-inmobiliarieit-22-5-millones-euros/1411519299 · https://www.inmonews.es/pisos-com-nueva-etapa-crecimiento-grupo-immobiliare-it-propietario-indomio-es-enalquiler-com/ · 15-09-2026 · 1 (pers)
- https://www.idealista.com/news/inmobiliario/empresas/2024/12/16/824621-intrum-fusiona-sus-servicers-inmobiliarios-para-simplificar-su-estructura-en-espana · 15-09-2026 · 1
- https://www.elnacional.cat/oneconomia/es/empresas/hipoges-finsolutia-compran-servihabitat-antiguo-servicer-caixabank_1676885_102.html · https://www.merca2.es/2026/08/04/hipoges-compra-servihabitat-gigante-60000-millones-2430054/ · https://inmodiario.com/138/87055/finsolutia-e-hipoges-acuerdan-adquirir-servihabitat/ · 15-09-2026 · 7 (pers, tegenstrijdig)
- https://www.idealista.com/es/inmueble/111869151/ (via assistent, property_detail) · https://inversores.servihabitat.com/es/venta/promociones/terreno-urbanonoconsolidado/alicante-marinaalta-balconalmarjavea/06124187 · 15-09-2026 · 1/3

**Recht (context rechtenvelden)**
- https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-1996-8930/texto/bloque/a133 (TRLPI art. 133) · …/a18 · …/a128 · …/a138 · 15-09-2026 · 2
- https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-2021-17910/texto/bloque/a6-9 (RDL 24/2021 art. 67) · 15-09-2026 · 2
- https://eur-lex.europa.eu/legal-content/ES/TXT/HTML/?uri=CELEX:62019CJ0762 (HvJ C-762/19) · https://eur-lex.europa.eu/legal-content/ES/TXT/HTML/?uri=CELEX:62014CJ0030 (HvJ C-30/14) · 15-09-2026 · 2
- https://www.aepd.es/documento/listas-dpia-es-35-4.pdf · 15-09-2026 · 2

**Geblokkeerd of niet uitgevoerd in deze deliverable:** geen nieuwe webcontroles gedaan; alleen de eigen lokale dienst gelezen (twee keer op 15-09-2026). WebSearch niet gebruikt. Alle blokkades (403, JavaScript-only, DataDome, Cloudflare, Imperva, Paagees Shield) staan per bron in de onderzoeksbestanden en zijn nergens omzeild. Niet opnieuw gecontroleerd in deze herziening: de 48 alleen-op-naam-kantoren, het RAICV-register (alleen JavaScript) en de kantoorsites met datum 14-09 in tabel K-1.

## Herzieningen

- 15-09-2026: register uitgebreid van 59 naar 75 regels (R2-60 t/m R2-75: ICV-plan- en sectorlagen, ICV ArcGIS, IDEE-ARPSI, MITECO DPMT en DPH/SNCZI, IGME, GVA-planregister, DOGV, urbanisme Xàbia, SUMA, ATV, GVA-patrimonium, Patrimonio del Estado, TEJU en ORGA; ingevuld uit R08, R12, R13 met hun verificaties en deliverables 03–05, zonder nieuw webonderzoek). Zeven rechtenvlaggen per regel toegevoegd op basis van R16 en de onderzoeksrapporten (tabel "Rechtenvlaggen per bron" in bijlage B). Statustelling nu ALLEEN HANDMATIG 39, CONTRACT OF TOESTEMMING NODIG 14, TECHNISCH ONDERZOEK NODIG 18, NIET GEBRUIKEN 4; samenvatting, kop, §2.1, §2.5 en bijlage B bijgewerkt. In `bronnenregister.json` heet het tekstveld voor historische gegevens nu `historical_data`, omdat `history` de rechtenvlag is.
- 15-09-2026 (samenhangscontrole): K10, Idealista 111869151 en Sareb-perceel A overal als waarschijnlijk hetzelfde object (type 4) met tegenstrijdige planklasse (type 7) en btw in plaats van ITP volgens de servicer (samenvatting, §2.3, §2.5); bankvastgoed overal als 0 woningen en 1 perceel op Idealista plus 2 Sareb-percelen bij Servihabitat Profesionales (ook bijlage C); verouderde verwijzingen naar deliverable 04 (eActivos, doorschakelnummers) en deliverable 01 (noemer 238, "0 de bancos") rechtgezet; BP-percelen als 24 objecten van type Land in "Javea" zonder accent met peildatum; verwijzing naar de top-3 in deliverable 01 §1.2 toegevoegd. Aantal registerregels (75) en statustelling gecontroleerd tegen `bronnenregister.json`: ongewijzigd juist.

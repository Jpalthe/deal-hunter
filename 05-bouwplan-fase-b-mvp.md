# 05 — Bouwplan fase B (MVP) en fasering A–D · TREE Deal Hunter

**Deliverable:** 5 van fase A (masterprompt §31.5): welke kleinste complete versie al bruikbare deals oplevert, welke koppelingen nodig zijn, welke kosten en afhankelijkheden bevestigd moeten worden.
**Controledatum:** 15-09-2026. Eigen controles tussen 03:50 en 04:00 CEST: lokale feeddienst (alleen lezen), Hermes-venv, launchd, cronstatus, kill-switch-marker, BOE-sumario, AEAT-lijst en Catastro. Herstelronde 04:45–04:55 CEST: feeddienst opnieuw gelezen (veldnamen en vulling), toelichting in `waakhond.sh`, structuur van `bronnenregister.json` en inhoud van de projectmap. Gegevens uit de onderzoeksrapporten en de deliverables 01–04 houden hun eigen controledatum (14- of 15-09-2026), steeds in de versie ná de tegenspraak.
**Herstelronde:** dit plan is na een kritiekronde aangevuld met de complete perceelketen uit deliverable 03, een waarderingsroute voor fase B, het datamodel met de BP-veldmapping, de partnerdealflow (route C/D) en een raming van menselijke inzet. Tegenstrijdigheden tussen documenten staan zichtbaar opgelost in "Verwerkte correcties".
**Bronverwijzing:** [Bxx] en [Lx] verwijzen naar de bronnenlijst onderaan (URL, datum, bewijstype). Het cijfer achter de puntkomma is het bewijstype: 1 aanbieder · 2 officiële bron · 3 door ons vastgesteld · 4 AI-inferentie of ontwerpvoorstel · 5 berekening · 6 professional · 7 onbekend of tegenstrijdig.
**Status:** plan. Er is niets gebouwd, gestart of geïnstalleerd. Niets in dit document "draait" of "monitort".

## Samenvatting in tien regels

1. De kleinste complete versie is een **dealdesk voor Jávea**. Het systeem haalt op wat mag (BOE, AEAT, Catastro, GVA/ICV-kaartlagen; Background Properties na akkoord), identificeert percelen, rekent en schrijft dossiers. De selectie op Idealista en de aanleveringen van partnermakelaars (route C/D) blijven mensenwerk via de reviewpagina; contacten staan in GoHighLevel.
2. Die versie kan **zonder één installatie**: Python 3.11.15 in de Hermes-venv met httpx, defusedxml, Pillow, numpy, anthropic, jinja2, fastapi en pytest, plus SQLite 3.50.4 met R-tree en FTS5 (gecontroleerd 15-09-2026). Aanbeveling: variant 1. Een geometriebibliotheek of Postgres met PostGIS pas als buffers of onregelmatige bouwvlakken nodig zijn, en alleen na akkoord.
3. **Rechten bepalen de bouwvolgorde:** fundament → **veilingmodule** → **perceelmodule** → **bestaand vastgoed en partnerinvoer**. BOE, AEAT, Catastro en de GVA/ICV-lagen zijn open data. BP-opslag, -historie en -AI-analyse wachten op schriftelijk akkoord van BP (tot dan draait de adapter droog). Gepland gebruik van Idealista wacht op schriftelijke toestemming.
4. BOE-veilingaankondigingen bevatten **geen plaats van het goed**. Jávea-objecten vinden we via Jans portaalmeldingen, handmatige controle en de AEAT-lijst (met coördinaten). Op 14 én 15-09-2026 liep er geen enkele veiling in Xàbia.
5. **Geen beeldvergelijking (dHash) op portaalfoto's**, want downloaden is al reproductie van een beschermde foto. In fase B ook niet op BP-foto's. Dubbele advertenties herkennen we op feiten en referenties, met menselijke controle.
6. **De perceelmodule is een complete keten** (deliverable 03): Catastro-koppeling met zekerheidsniveau, daarna automatisch de GVA/ICV-planlaag en de sectorale lagen op de perceelpolygoon (nooit op de pin), een versiebeheerde regeltabel voor zona E en SNU, en drie handmatige poorten (bevestigde RC, informe urbanístico of cédula, architect). Bij MIDDEL of LAAG geen bouwvolume.
7. **Een maximale koopprijs is in fase B alleen voorwaardelijk.** Er is geen toegestane bron van transactieprijzen. De waardebandbreedte komt uit handmatig vergeleken vraagprijzen (label "vraagprijzen, geen transacties", minimaal zes vergelijkingsobjecten), desgewenst met een Tinsa Radar-studie (29 € per studie, btw ONBEKEND).
8. Het ochtendrapport komt in drie niveaus (§24) als HTML en Markdown. Kanaal en tijdstip kiest Jan. Let op: cronbezorging vanuit het Hermes-profiel G-CEO faalt nu bij alle drie de jobs ("blocked_config").
9. Kosten: software fase B 60–90 uur en fase C 80–120 uur (schatting R17, geen offerte; effect van de aanvullingen ONBEKEND); hosting €0; AI < $10 per maand (USD, berekening); nota simple 9,02 € + btw per finca. Handmatige rondes: vast circa 1,7–3,9 uur per week op niet-gemeten werkhypothesen, plus een variabel deel per signaal en dossier (ONBEKEND). Advocaat, architect, gestor, gemeentelijke tasas en datalicenties: ONBEKEND, op offerte (plan in §6.7).
10. ⏸️ Eerst nodig van Jan: akkoord op variant 1 en het gebruik van de open kaartlagen, het BP-akkoord (mail en clausule, na toets door een advocaat), het investeringskader met de kopende entiteit, en een AI-budget met API-sleutel. Daarna: toestemming of API bij Idealista, registratie op het veilingportaal, een architect en advocaat met offerte, en tijdstip plus kanaal van het rapport.

---

## Conclusie

### Deel 1 — Samenvatting voor Jan in gewone taal

**Wat fase B oplevert.** Geen robot die "de markt" afzoekt, maar een werkplek die elke dag drie dingen voor je doet:

- **Veilingen:** het BOE en de AEAT-lijst lezen. Nieuwe veilingen van de rechtbank van Dénia (waar Xàbia onder valt), van de AEAT en van SUMA worden gesignaleerd, met alle termijnen en waarborgbedragen uitgerekend. De juridische en financiële blokkades staan erbij.
- **Percelen:** elk perceel dat binnenkomt (van BP, door jou aangedragen van Idealista, of aangeleverd door een partner) koppelen aan de juiste kadastrale referentie. Het systeem zegt eerlijk hoe zeker die koppeling is: hoog, middel of laag. Daarna legt het de perceelgrens over de openbare plankaart en de risicokaarten van de Generalitat (overstroming, natuurpark, Natura 2000, bos en brand, kust, erfgoed) en zet het de uitkomst als *signaal* in het dossier. Bouwrecht stelt het niet vast: dat doen de gemeente (informe urbanístico of cédula) en een architect.
- **Bestaand vastgoed:** BP-objecten volgen (nieuw, prijs gewijzigd, niet meer gevonden), zodra BP schriftelijk akkoord geeft. Interessante Idealista-advertenties voer je zelf in met link en een paar kerngegevens. Het systeem rekent en koppelt daarna.
- **Aanbod van partners:** een makelaar, architect of ontwikkelaar levert een object aan via een formulier. Het object komt op de reviewpagina met vaste opvolgtermijnen; de contactgegevens van de partner blijven in GoHighLevel.

Per serieuze kandidaat maakt het systeem een dossier volgens het vaste format (§25): wat vaststaat, wat onbekend is, welke blokkades er zijn, en welke stap nu nodig is. Elke ochtend krijg je een rapport. Zijn er geen sterke kansen, dan staat dat er. Viel een bron uit, dan staat dat er apart.

**Wat een dossier over waarde en prijs zegt.** Transactieprijzen zijn voor ons niet beschikbaar: het gemeentelijke overzicht van het ministerie geeft alleen aantallen verkopen, het notariële portaal verbiedt commercieel gebruik, en de betaalde databronnen vragen een contract [B115; 2] [B116; 2] [B35; 2]. In fase B vergelijk je dus vraagprijzen van vergelijkbare objecten, met het label "vraagprijzen, geen transacties". Daaruit volgt een voorzichtige, een basis- en een gunstige waarde. De maximale koopprijs die het systeem daarop berekent, is altijd **voorwaardelijk** (§3.7).

**Wat het nog níet doet.** Het volgt niet de hele markt. Het leest Idealista niet automatisch uit. Het mailt geen makelaars, biedt niet en betaalt niet. De eerste grenzen zijn niet technisch maar juridisch: portalen verbieden geautomatiseerd ophalen en opslaan, foto's zijn auteursrechtelijk beschermd, en BP heeft de feed voor de website verstrekt, zonder schriftelijke afspraak over ander gebruik [B31; 2] [B80; 2] [R05 §6.1; 3] [B20; 2]. Daarnaast trekt het bewust geen bouwconclusies zonder bevestigd perceel en geldend plan (§14–15).

**Waarom dit toch de moeite waard is.** Het deel dat vandaag al mag (BOE, AEAT, Catastro, de GVA/ICV-kaartlagen) is precies het deel waar makelaars het minst naar kijken: veilingtermijnen, kadastrale identificatie, planologische en sectorale knock-outs, en rekenwerk. Het deel dat nog niet mag (BP-historie, Idealista-breedte) ontgrendel je met twee brieven. De code staat dan klaar.

### Wat Jan nu moet beslissen (maximaal drie vragen)

Deze vragen worden niet los voorgelegd: de geconsolideerde top-3 voor alle vijf deliverables staat in deliverable 01 §1.2 (vraag 1 en 2 hieronder vallen onder vraag 2 en 1 daar; vraag 3 is de eerste vraag van ronde 2).

1. **Background Properties:** mogen we de conceptmail (R05 §6.4) en de conceptclausule (R16 §6.4) na een korte toets door een Spaanse advocaat aan BP voorleggen? En wie is daar het aanspreekpunt?
2. **Investeringskader en entiteit:** met welk budget, welke rendementseis en welke maximale doorlooptijd rekenen we, en koopt TREE of Rocksure Capital? Zonder die cijfers blijft "maximale koopprijs" een lege formule. En zelfs mét die cijfers blijft de uitkomst in fase B voorwaardelijk, omdat de verkoopwaarde op vraagprijzen rust (§3.7).
3. **Technische start:** akkoord met variant 1 (geen installaties, Hermes-venv, één SQLite-bestand in `~/tree-es/deal-hunter/data/`), inclusief het automatische gebruik per kandidaat en in laag volume van de open Catastro- en GVA/ICV-diensten als eerste filter (zelfde vraag als besluit 3 in deliverable 03 en besluit 6 in deliverable 01)? En welk maandplafond voor AI-kosten, in euro, met een eigen Anthropic-sleutel of via OpenRouter?

---

## Onderbouwing

### Deel 2 — Wat er vandaag al staat, wat we hergebruiken en wat er nog niet is

**2.1 Bestaande bouwstenen**

| Bouwsteen | Stand 15-09-2026 | Hergebruik in Deal Hunter | Wat níet (en waarom) | Bron |
|---|---|---|---|---|
| **Feeddienst** `com.tree.properties-api` (Node, poort 3100) | Draait; stand 15-09-2026 03:55 CEST: 224 objecten, `errors: []`, lastFetch 01:00 UTC; de plaatsnaam staat in de feed als "Javea" zonder accent: plaatsfilter "Javea" 56, "Jávea" 0, "Xàbia" 0 | Alleen-lezen bron voor BP in fase B via `/api/properties` (geen sleutel nodig, geen extra verzoeken aan BP) | Geen historie, alleen geheugen. Een (gedeeltelijk) mislukte ronde leegt of verkleint de lijst stil, historisch tot 17 objecten. `lastFetch` wordt ook na mislukking ververst. Het `pool=true`-filter telt "Nee" als zwembad. Na herstarts mislukt de eerste ronde vaak (12 van 17 starts begonnen met 0 objecten). Productiedienst: niet aanpassen. | [L1; 3] [B01; 3] [B25; 3] |
| **Importlogica treeproperties.es** | Krimpdrempel 30 %, `withdrawn` in plaats van verwijderen, alarm webhook → Resend → GHL met 30 min demping | Regels, veldenlijst en plaatsnaamnormalisatie overnemen in Python; alarm nabouwen met **opgeslagen** demping (in de site staat die in het geheugen) | De importlogboeken hebben meerdaagse gaten (o.a. 02-09 → 07-09). Geen schone testset voor wijzigingsdetectie. | [B02; 3] |
| **tree-ai-agentic-os** (FastAPI + SQLite, geen dienst) | Bevoegdheden A0–A4, approvals met maker-checker, audit, kostenregistratie, kill-switch op marker `~/.hermes/LOCKDOWN` (marker afwezig) | Kill-switch-controle vóór elke run; elke actie met externe werking via `authority.evaluate` en een approval; kosten boeken in de ledger | Het plafond van €400 per maand wordt niet afgedwongen, alleen gelogd. Elke actie met `cost_eur > 0` wordt minstens A3, dus elke betaalde AI-aanroep zou een approval vragen. Een onbekende actor krijgt maximaal A2. | [B03; 3] [B06; 3] [L5; 3] |
| **Hermes** (gateway, agentorganisatie) | Gateway draait. `hermes cron create --no-agent --script` bezorgt scriptuitvoer zonder LLM. Het cron-gereedschap staat voor agents uit ("routines zijn een Gate C-besluit"). | Optioneel bezorgkanaal voor het rapport | Alle drie de G-CEO-cronjobs op `blocked_config` (reeksen van 11, 2 en 1 mislukkingen); het default-profiel heeft 0 jobs en is niet getest | [L3; 3] [L4; 3] [B04; 3] |
| **Tree AI OS** | Postgres 16.6 in Docker (127.0.0.1:5433), geen PostGIS; back-upscript 03:30 met retentie 14; waakhond elke 600 s die rechtstreeks via de Discord-bot-API meldt | Alleen de **patronen**: back-up, waakhond, `.env` met rechten 600 | De database zelf: die is van Tree AI OS en wordt niet gedeeld. Volgens de toelichting in `waakhond.sh` (gedateerd 6 september 2026) stopte Docker in de nacht van 2 op 3 september 2026 en faalde de back-up daarna vier nachten lang ongemerkt; dat aantal is niet in back-uplogs nagerekend. Launchd meldt op 15-09 laatste exit 1 voor `com.tree.ai-os` en de waakhond (betekenis niet onderzocht). | [B05; 3] [L4; 3] [L7; 3] |
| **Gereedschapskist** | Python 3.11.15 (Hermes-venv), SQLite 3.50.4 met `rtree` en `fts5`, `zoneinfo` Europe/Madrid; Apple M4 (arm64), 32 GB | Alles voor fase B | Ontbreekt: psycopg, lxml, shapely, pyproj, imagehash, pdf-bibliotheek. Voor fase B niet nodig. | [L2; 3] [B05; 3] |
| **Claude Code en MCP** | CLI 2.1.241; Idealista-assistent verbonden; GHL-MCP vraagt authenticatie (14-09) | Idealista-assistent voor handmatige, ad-hoc selectie in een sessie | Een launchd-script kan de assistent niet aanroepen. Headless `claude -p` is niet getest, `--bare` wordt daar de standaard (en laat dan MCP weg), en `--permission-prompts none` vraagt versie ≥ 2.1.259 | [R17 §1.7; 3] [B09; 2] |
| **GoHighLevel** | CRM van waarheid voor TREE Properties (ADR-0014, lokale feiten). De site gebruikt `services.leadconnectorhq.com` al met header `Version: 2021-07-28`. | Fase C: custom object per fysiek object; makelaars als contact | Schema aanmaken via de API vraagt een **Agency**-token; records gaan met een sub-account-token. Limiet 100 verzoeken per 10 s en 200.000 per dag per app. Of dit ook voor Private Integration Tokens geldt: [te verifiëren]. | [B02; 3] [B10; 2] [B11; 2] |

**2.2 Wat er nog niet is**

| Onderdeel (keten §27) | Stand |
|---|---|
| Code, git-repository, database, `data/`-map in `~/tree-es/deal-hunter/` | Niet aanwezig. De map bevat op 15-09-2026 om 04:50: CLAUDE.md, MASTERPROMPT.md, de deliverables 01–05, `bronnenregister.json`, `onderzoek/` (R01–R17 met tegenspraakrapporten, plus het hulpbestand `ih.py` met imagehash-bibliotheekcode) en een lege `rapporten/`; geen `.git` [L6; 3] |
| Rechtenregister als poortwachter | **Register wel aanwezig:** `bronnenregister.json` met 75 regels (stand 15-09-2026: ALLEEN HANDMATIG 39, TECHNISCH ONDERZOEK NODIG 18, CONTRACT OF TOESTEMMING NODIG 14, NIET GEBRUIKEN 4), de velden uit masterprompt §7 als tekst, één status per regel en de machineleesbare rechtenvlaggen `automated_access`, `storage`, `history`, `ai_analysis`, `image_hashing`, `show_to_clients` en `personal_data` (waarden yes/no/conditional/unknown). De GVA/ICV-, IDEE-, IGME- en MITECO-lagen staan erin als R2-60 t/m R2-69 [L8; 3]. **Poortwachter niet aanwezig:** er draait nog geen adapter die deze vlaggen leest; `retention_days` uit R16 §6.5 staat niet als eigen veld in het register (alleen tekstveld `storage_retention`) |
| Historie, wijzigingsdetectie, objectidentiteit, dedupe | Niet aanwezig; ontwerp in R17 §6 (met correcties, zie hieronder) |
| Perceelkoppeling, planfilter en sectorale lagen, regeltabel, veilingadapter, deadlinecalculator | Niet aanwezig; ontwerp in R11 §7, deliverable 03 §2.1 en §5.2, R13 §11 en R08 §10 |
| Rekenmodel | Alleen de geteste schets uit R14 §6.4, met vijf nog te verwerken correcties [B90–B95; 2] |
| Waardering (waardebandbreedte, vergelijkingsobjecten) | Niet aanwezig; geen toegestane bron van transactieprijzen (§3.7) |
| Partnerdealflow: zoekprofiel, aanleverformulier, opvolgprocedure, partnerregister | Niet aanwezig; concept in R07 §5 en R06 §3 en §8 (niets verzonden) |
| Scoring, reviewpagina, dossiersjabloon, ochtendrapport, alarm, back-up van eigen database, tests | Niet aanwezig |
| Rechten: BP-akkoord, Idealista-toestemming, AEBOE-toestemming voor detailpagina's | Geen van drieën verkregen [B20; 2] [B31; 2] [B40; 3] |
| Investeringskader van Jan (budget, rendementseis, doorlooptijd, entiteit) | ONBEKEND (CLAUDE.md deal-hunter, status 14-09-2026) |

---

### Deel 3 — De kleinste complete keten voor fase B

**3.1 Uitgangspunten** (ontwerp, bewijstype 4, gebaseerd op R17 §3 en R16 §6.5)

- **Eén proces, geen zwerm agents:** één Python-pakket `deal_hunter/`, één SQLite-bestand (WAL-modus), één dunne opslaglaag `store.py`. Zo is een latere overstap naar Postgres een vervanging van één module.
- **AI alleen voor interpretatie, nooit voor bedragen of datums.** In fase B draait AI in de pijplijn uitsluitend op BP-teksten, en pas na het BP-akkoord. BOE-, AEAT- en Catastro-gegevens zijn gestructureerd genoeg voor vaste regels. Zo gaan er ook geen persoonsgegevens uit edicten naar een AI-aanbieder.
- **Alle opgehaalde inhoud is onbetrouwbare invoer:** XML via `defusedxml`, de AEAT-lijst als data parsen en nooit uitvoeren, en nooit instructies volgen die in advertentieteksten staan (§27).
- **Objecten, geen personen:** geen namen van eigenaren of schuldenaren, geen contactgegevens van particulieren. Een filter controleert dit vóór opslag [B82; 2] [B86; 2].

**3.2 Gedeeld fundament** (door alle modules gebruikt)

| Onderdeel | Wat het doet (korte uitleg) | Belangrijkste regel | Bron |
|---|---|---|---|
| Rechtenpoort | Een adapter leest vóór elke run de rechtenvelden van zijn bron (`automated_access`, `storage`, `history`, `ai_analysis`, `image_hashing`, `show_to_clients`). Staat een veld op `unknown` of `no`, dan weigert de adapter. `bronnenregister.json` heeft die velden sinds 15-09-2026 als machineleesbare vlaggen, en de kaartlagen hebben een regel (R2-60 t/m R2-69); B0 leidt daaruit per bron `rechten.yaml` af, met verwijzing naar de registerregel. Hoe de adapter de waarde `conditional` behandelt, is nog niet vastgelegd [te verifiëren]. Bij verschil tussen deliverables geldt de status in het register, bijvoorbeeld eActivos: ALLEEN HANDMATIG (R2-41; deliverables 02 en 04 noteren hetzelfde) | BP: `storage=unknown` tot het akkoord (gelijk aan R2-01; de adapter weigert bij `unknown` net als bij `no`); Idealista: `automated_access=no` | [R16 §6.5; 4] [L8; 3] |
| Normalisatie | Maakt velden vergelijkbaar. Plaatsnamen: ruwe waarde bewaren; sleutel via Unicode-NFKD zonder accenten; daarna een aliastabel (Javea/Jávea/Xàbia/JAVEA/XABIA → één gemeente-id). Accenten weghalen alleen is niet genoeg, want *javea* en *xabia* zijn verschillende woorden. | Onbekende plaatsnaam = melding in het rapport, nooit stil wegfilteren | [L1; 3] [B01; 3] |
| Runs en gebeurtenissen | Elke run krijgt een `run_id` met status ok/partial/failed. Per advertentie een inhouds-hash en de tijdstempels uit §10 (`source_published_at`, `source_modified_at`, `first_seen_at`, `last_successful_fetch_at`, `last_seen_at`, `analysis_completed_at`), opgeslagen in UTC en getoond in Europe/Madrid. | Een mislukte run schrijft niets en levert alleen BRON NIET BEREIKBAAR op | [R17 §6.1; 4] |
| Idempotentie | "Twee keer draaien geeft geen dubbele gegevens": uniek op bron + bron-id + inhouds-hash | Heranalyse alleen bij een materiële wijziging | [R17 §6.4; 4] |
| Kill-switch | Vóór netwerk, AI of bezorging: bestaat `~/.hermes/LOCKDOWN`, dan stopt de run en komt er een auditregel | Hergebruik `killswitch.is_locked()` (alleen lezen) | [B03; 3] |
| Kosten | Tokenbudget per run en per maand in `.env`; de run stopt zelf bij overschrijding; boeken in euro in de ledger van tree-ai-agentic-os | Het OS-plafond remt niet, dus Deal Hunter moet het zelf afdwingen | [B03; 3] [B07; 2] |
| Logging en geheimen | `logs/runs.jsonl` met aantallen, duur en fouten. Sleutels in `.env` (rechten 600), nooit in plists, logs, prompts, rapporten of de database. | Een test zoekt sleutelpatronen in logs en database-dump | [R17 §6.5, §6.9; 4] |
| Alarm | Port van `alarm.ts` met demping die in SQLite wordt bewaard. Voorwaarden: bron 2× achtereen mislukt, krimp > 30 %, run > 30 min, kostenlimiet, rapport niet bezorgd. | "Geen nieuwe kansen" ≠ "geen nieuwe gegevens" | [B02; 3] [MP §10] |
| Back-up | Nachtelijk `sqlite3 .backup`, gzip, retentie 14, na de Tree AI OS-back-up | Hersteltest hoort bij de acceptatie | [B05; 3] |
| Reviewpagina | FastAPI + Jinja2 op 127.0.0.1:8710 (naar voorbeeld van de cockpit): kandidaten, dossiers, knoppen *onderzoeken / watchlist / afwijzen (reden)*, handmatige invoer (Idealista-advertentie, perceel, partneraanlevering, vergelijkingsobject), taken met deadline (poorten, opvolgtermijnen partners) en de vijf gescheiden statussen uit §26 | Geen contactgegevens: contacten en commerciële contactstatus horen in GHL (ADR-0014); de reviewpagina bewaart hoogstens een verwijzing. Openstellen via Tailscale is een apart besluit. | [R17 §8.2; 4] [MP §26] |
| Rekenmodule `finance.py` | Port van R14 §6.4 met `Decimal`, parameters in `parameters-2026.yaml` (waarde, bron, datum, bewijstype). De verkoopopbrengst komt uit het waardeblad (§3.7), nooit uit een losse invoer zonder vergelijkingsobjecten | Eerst de R14-testuitvoer reproduceren, daarna de correcties verwerken (§ "Verwerkte correcties"). Uitkomst heet "voorwaardelijke prijsanalyse" zolang §3.7 niet is voldaan | [B90–B95; 2] [MP §22] |
| Beoordeling | **Geen numerieke score** zolang er geen methodiek is (§23), wel labels (verder onderzoeken / bezichtigen / watchlist / afwijzen), harde blokkades en bewijskwaliteit | Een aantrekkelijke prijs maakt een blokkade niet weg | [MP §23] |

**3.3 Module A — Bestaand vastgoed (BP + Idealista-assistent)**

| Schakel | Fase B-ontwerp | Status en bron |
|---|---|---|
| **Bron** | (1) BP-feed, Kyero v3, gelezen via de lokale API (volledige paginering met `limit=100`, niet via het plaatsfilter). (2) Idealista-assistent, uitsluitend handmatig in een Claude-sessie. (3) Opgeslagen zoekopdrachten met e-mailalerts in Jans Idealista-account. Die zijn officieel toegestaan: "registrarte para guardar búsquedas y favoritos". | BP: technisch werkend [L1; 3], rechten CONTRACT OF TOESTEMMING NODIG [B20; 2]. Idealista: ALLEEN HANDMATIG [B31; 2] [B32; 2] |
| **Adapter** | `bp_localapi.py` met een geldigheidspoort: totaal > 0, `/api/stats.errors` leeg, krimp ≤ 30 % ten opzichte van de vorige geldige run, en na een herstart van de dienst een volgende ronde afwachten. `lastFetch` telt **niet** als bewijs van versheid. Eén geldige run per dag is genoeg: BP maakte de exports in de gemeten nacht tussen 01:34 en 02:55 CEST (één meting). Normalisatie van plaats, `pool`-tekst (Private/Privé → privé; Nee/No → geen), energielabel ("Processing" → in aanvraag), HTML in omschrijvingen, en coördinaten (Miami-punt → ONBEKEND). `idealista_invoer`: formulier op de reviewpagina met URL zonder utm-parameters als sleutel, propertyCode, datum, vraagprijs, m² (veld en tekst apart), type, pin of adres, eigen oordeel. | Poortregels: [B01; 3] [R17-verificatie F7; 3]. Exportvenster: [B24; 3]. Afwijkingen in de feed: [B25; 3]. Handmatige invoer van enkele feiten is volgens R16 "verdedigbaar" [R16 §3.8; 4, advocaat] |
| **Opslag** | Tabellen volgens het datamodel in §3.8 (`listing`, `listing_event`, `property_object`, `object_listing` met `match_confidence`, `provider`, `offered_right`, `package`). Veldmapping BP → intern: §3.8. **BP-snapshots en -teksten pas na het akkoord.** Tot dan draait de BP-adapter droog: tellingen en poortuitkomst worden gelogd, inhoud wordt weggegooid. Idealista: nooit omschrijving, foto's of contactgegevens, ook niet het telefoonnummer dat de assistent toont (of dat een doorschakelnummer is, is niet bewezen). | [R16 §1 "Voor de bouw"; 4] [R06-verificatie R06-15; 4] |
| **Detectie** | BP: NIEUW DOOR ONS ONTDEKT, PRIJS GEWIJZIGD, INHOUD GEWIJZIGD, OPNIEUW AANGEBODEN, NIET MEER GEVONDEN (pas na afwezigheid in twee geldige runs op twee verschillende dagen), BRON NIET BEREIKBAAR. **Nooit NIEUW GEPUBLICEERD op basis van BP-`date`**: volgens de Kyero-specificatie is dat de datum van laatste wijziging, en die gaat naar `source_modified_at`. Nooit "verkocht". Idealista: alleen wat Jan invoert (prijs op datum; eerdere prijs zoals de assistent die in de sessie toont). | [B22; 2] [B23; 2] [MP §10] |
| **Analyse** | Na het BP-akkoord: AI-triage van de BP-omschrijvingen (Haiku 4.5), Sonnet 5 voor kandidaten, vaste JSON-uitvoer. "Render vermoed" is alleen een markering voor menselijke controle, want Claude kan niet betrouwbaar vaststellen of een beeld AI-gegenereerd is. Dedupe: trap 1 referentie (BP-`id` stabiel, `ref` wijkt bij 39 van 225 af van de URL), trap 2 feiten (type, ±5 % gebouwd, ±10 % perceel, afstand) = kandidaat voor menselijke controle. **Geen dHash** op portaalfoto's; op BP-foto's pas na akkoord en kalibratie. Idealista-advertenties worden alleen in de sessie geanalyseerd. Rekenmodule met Jans parameters en de waardebandbreedte uit §3.7; zonder die bandbreedte geen bedrag. | [B07; 2] [B08; 2] [B25; 3] [B80; 2] [B15; 2 en 3] |
| **Dossier** | Sjabloon §25 per fysiek object; alle bronadvertenties eronder; prijsverschillen en tegenstrijdige oppervlakten zichtbaar. Alleen intern. Idealista-links aan klanten doorsturen botst met de letterlijke voorwaarden van 2020, dus [advocaat]. | [B31; 2] [R16-verificatie F-1] |
| **Rapport** | Niveau 2 "beste renovatieobjecten", "interessante prijswijzigingen", "onderzoeksdossiers"; bronactualiteit BP; nulmeting expliciet gelabeld | [MP §24] |
| **Blokkade** | Zonder BP-akkoord: geen historie en geen AI op BP. Zonder Idealista-toestemming: geen enkele geautomatiseerde Idealista-stap. | ⏸️ Deel 8, punten 4 en 8 |

Wat deze module aan dekking levert, eerlijk gezegd: BP had op 15-09-2026 om 03:55 en om 04:48 56 objecten in "Javea" (24 percelen, 26 villa's, 4 appartementen, 2 zonder type) [L1; 3] [L9; 3] (op 14-09 om 23:00: 57 [B25; 3]). BP is **ons netwerk, niet de markt**: 6 van 6 geteste BP-objecten in Jávea stonden ook op Idealista, samen in 27 advertenties [B34; 3]. De Idealista-assistent telde op 15-09-2026 in Jávea 1.273 casas/chalets, waarvan 70 met het filter "Usada / para reformar" (daarvan noemen er 51 renovatie in de tekst en 4 nieuwbouw), plus 569 pisos en 333 terrenos, waarvan 238 met het label urbano of urbanizable [B34; 3] [R06-verificatie R06-15; 3]. Die 238 zijn **niet** automatisch bouwrijp. De vergelijking is dus 24 BP-objecten van type Land tegenover 333 terrenos, waarvan 238 met dat label; deliverables 01 en 02 gebruiken dezelfde noemer (333), omdat de BP-feed geen planklasse kent [R01-verificatie R01-12; 3].

**3.4 Module B — Percelen (Catastro, GVA/ICV-planlaag en sectorale lagen; keten van deliverable 03)**

Deze module bouwt de dertien stappen van deliverable 03 §2.1 na. Stappen 0–6, 8 en 10 zijn automatisch; stap 9 is een versiebeheerde regeltabel plus handwerk; stappen 7, 12 en 13 zijn handmatige poorten; stap 11 is deels automatisch. Na een MIDDEL of LAAG in stap 6 lopen stap 8 en 10 wél door (als signaal voor de beslissing om geld aan poort 1 te besteden), maar stap 9, 11 en 13 niet [D03 §2.1; 4]. Eerdere versies van dit plan lieten Jan de zonering per dossier handmatig invoeren; dat is vervangen door de automatische eerste filter hieronder, omdat deliverable 03 (op basis van R12, R13 en hun tegenspraak) de diensten live heeft getest.

| Schakel | Fase B-ontwerp | Status en bron |
|---|---|---|
| **Bron** | Invoer: BP-percelen (na akkoord), percelen die Jan invoert (pin, adres of RC) en partneraanleveringen (§3.6). Catastro vrije webservices (`Consulta_RCCOOR_Distancia`, `Consulta_DNPLOC`, `Consulta_DNPRC` in JSON), INSPIRE WFS percelen (`GetParcel`) en gebouwen, WMS-kaartbeeld. ATOM-gemeentebestand Xàbia (INE 03082) als nulmeting. GVA/ICV-planlaag (`0702_Planeamiento`) en sectorale lagen (ICV `0701`, `0505`, `0506`, ICV ArcGIS REST), IDEE-overstromingskaarten en IGME-geologie. | Catastro werkend en zonder sleutel [B61; 3] [B62; 3] [B63; 3] [B64; 3]; ConsultaMunicipio geeft "JAVEA/XABIA", cp 3, cm 82 [W3; 3]; ATOM bijgewerkt 21-08-2026, EPSG:25831 [B65; 3]. GVA/ICV, IDEE en IGME op 15-09-2026 bevraagd door R12/R13 en hun tegenspraak [B100–B109; 2/3]; MITECO-kust en -waterlopen onbereikbaar [B110; 3] |
| **Adapter** | `catastro.py`: alleen per kandidaatobject, nooit als sweep over heel Jávea. Cache per referentie. Eén verzoek tegelijk en ruim onder één per seconde; de werkelijke drempel is niet gepubliceerd, bij overschrijding volgt weigering "generalmente 10 días". WFS-objecten zelf tellen, want de kop `numberReturned` gaf 486 terwijl er 477 percelen in stonden. `httpx` voor `www.catastro.hacienda.gob.es`: curl en urllib falen daar op de certificaatketen, en dat omzeilen we niet. De JSON-parameters `CoorX`/`CoorY` zijn ongedocumenteerd, dus een regressietest. De Sede (perceel-pdf, kaart) blijft handwerk. | [B67; 2] [B63; 3] [B60; 2] [R11-verificatie R11-18; 3]. Drempel "ruim onder 1/s": aanname [4] |
| **Adapter planfilter (stap 8)** | `icv_planeamiento.py`: WFS/WMS `https://terramapas.icv.gva.es/0702_Planeamiento`, lagen `Planeamiento.Clasificacion`, `Planeamiento.Zonificacion`, `InventarioSuSuz` en `MinimizacionViviendasSNU`. Bevraging met GetFeature op een bbox in EPSG:25830 (R13: bbox in EPSG:4326 gaf 0 objecten, een OGC-attribuutfilter gaf een serverfout) of GetFeatureInfo op een kleine bbox rond het perceel (R12). Omdat R12 en R13 verschillend gedrag meldden, legt een regressietest de werkende CRS-parameter vast. **Altijd op de perceelpolygoon uit stap 5, nooit op de pin.** Uitvoer per perceel: klasse, zonecode, instrument, geraakte vlakken (en overlap, zie geometrieregel), laagdatum en de vaste vermelding "carácter informativo". Spreken twee GVA-lagen elkaar tegen (op de K07-pin: PP Ermita II tegenover "Plan Parcial Montgó-2 / SUP Montgó-2"), dan wordt de klasse bewijstype 7. Het instrument wordt vergeleken met de documentstatustabel: een vlak van een vernietigd of niet goedgekeurd plan levert "geen geldend recht". | Dienst: `Fees` "No se aplican condiciones", CC BY 4.0, laag bijgewerkt 25-08-2026 [B100; 2] [B101; 2]; tests en CRS-gedrag [R13 §7; 3] [R12-verificatie R12-17, A2; 3]; ontwerp [D03 stap 8; 4] |
| **Adapter sectorale lagen (stap 10)** | `icv_sectoraal.py`, één functie per laag, antwoord per laag gecachet (PATRICOVA- en PATIVEL-vlakken voor Xàbia zijn enkele honderden kB; wekelijks verversen volstaat): **PATRICOVA** ICV `0701_InfraestructuraVerde` laag `IVR.Inundacion` (GetFeatureInfo met `INFO_FORMAT=geojson`) en ArcGIS `ordenacion_territorial` lagen 4–10; **ARPSI** IDEE-WMS; **PORN Montgó** ICV `0505_PORN` (`Montgo.PORN`, `Montgo.Zonificacion`, `Montgo.Parque`); **Red Natura 2000** `0701` (`IVR.ZEC`, `IVR.LIC`, `IVR.ZEPA`) en ArcGIS `espacios_protegidos` laag 21; **PATFOR en brand** ICV `0506_PATFOR` en ArcGIS `prevencion_de_incendios` (lagen 8, 71, 104, 114, 123; rastercel ±500 m); **PATIVEL** ArcGIS `ordenacion_territorial` laag 34 (vlakken Litoral 1/2); lagen 30–32 zijn **lijnen**, dus afstand berekenen, want punt-in-polygoon geeft daar altijd 0; **erfgoed** `0701` (`IVR.Cultura.BIC.*`, `IVR.Cultura.BRL`); **geologie** IGME GEODE (geen juridische werking). **Kust en waterlopen** (MITECO): op 15-09-2026 onbereikbaar, dus vaste uitkomst "dienst onbereikbaar; kusttoets 20/100 m ONBEKEND". Per laag een dienststatus (bereikbaar / fout / vervallen) met datum van laatste controle. Uitkomst in het dossier: "signaal (laag, datum, bewijstype 3)" of "dienst onbereikbaar"; **nooit "geen beperking"**. | Endpoints en tests [D03 stap 10; 3] [B102–B109; 2/3]; MITECO [B110; 3]; ontwerp en cache [R13 §11; 4] |
| **Geometrie in variant 1** | Punt-in-polygoon, grensafstand en oppervlakte (shoelace) zijn getest met alleen de standaardbibliotheek. Overlap tussen perceelpolygoon en zonevlak kan via (a) een ArcGIS `query` met de perceelpolygoon (`esriGeometryPolygon`, inSR 25830) of (b) eigen code; **geen van beide is getest**. Tot een van beide een regressietest haalt, toont het dossier "raakt vlakken X en Y" (hoekpunten en zwaartepunt van het perceel getoetst) zonder overlappercentage. Buffers (brandstrook 30 m, kuststroken) en onregelmatige bouwvlakken vragen een geometriebibliotheek zoals `shapely`: installatie alleen met akkoord van Jan. | Getest [R11-verificatie R11-19; 3]; route (a) ontwerpnotitie [R13 §11 punt 2; 4]; bibliotheekregel [D03 W8; 4] |
| **Regeltabel (stap 9)** | `bouwregels-xabia.yaml`, versiebeheerd. Per regel: waarde, document, versie en datum, artikel, kaartblad, zone/grado/gebied, status (in werking / in procedure / vernietigd / onbekend), bewijstype, controledatum en de vlag **"alleen buiten planes parciales, PRI's, homologaciones en UA's"**. Inhoud in fase B: PGOU-zona E (parcela mínima 500–1.500 m² per gebied; edificabilidad 0,142 m²t/m² bruto of 0,20 netto; ocupación 20/30/50 % per grado, percentages [te verifiëren op het Mod. I-blad]; lagen en hoogte; afstanden) en SNU (TRLOTUP 210–211: ≥ 1 ha, ≤ 2 % bebouwing, landbouwrapport). Daarnaast een documentstatustabel: PGOU 1990/1991 in werking; PGE 2019 in procedure (geen recht); NUT 2021 bewijstype 7 (alleen na schriftelijke bevestiging); homologación Portitxol vernietigd (TSJCV 459/2012; onherroepelijkheid niet gecontroleerd); Mod. nº 41 in procedure. Zone, grado en regime per perceel blijven handwerk, omdat plano's B.1/B.2 niet-gegeorefereerde scans zijn. | Waarden en status [D03 §2.2, §2.3; 2]; ontwerp [D03 §5.2; 4]; Portitxol [R12-verificatie R12-17; 2] |
| **Zekerheidsregels (stap 6)** | `zekerheid.py` met de regels van deliverable 03 stap 6. **HOOG:** precies één kandidaat met ≤ 3 % oppervlakteafwijking, én adres-match van déze advertentie of een RC uit de tekst die de oppervlaktecheck doorstaat of pin in het perceel ≥ 5 m van de grens bij zichtbaar adres, én objecttype strookt met Catastro, én geen andere advertentie in het cluster wijst een ander perceel aan. **MIDDEL:** één kandidaat ≤ 3 % maar grensafstand < 5 m; of twee kandidaten binnen ±10 %; of koppeling via een dubbele advertentie; of adres verborgen (plafond). **LAAG:** pin in geen perceel en ≥ 2 kandidaten binnen 10 m zonder adres; of geen kandidaat binnen ±10 %; of oppervlakte ontbreekt; of objecttype botst met Catastro zonder verklaring. De drempels 3 %, 5 m en 25 m zijn ontwerpaannames, te kalibreren op de eerste 30 dossiers. | [D03 stap 6; 4] [R11-verificatie R11-07, R11-08; 3] |
| **Rekenregels bouwvolume** | `bouwvolume.py` met regels R1–R10 van deliverable 03 §2.4. Draait alleen bij zekerheid HOOG én vastgestelde zone, grado, regime en bruto- of nettolezing ("eerst parameters, dan rekenen"). Blokkeert: ocupación × lagen als vloeroppervlak, edificabilidad × lagen, Catastro-`sfc` of advertentie-m² als meetellend vloeroppervlak, en de zona E-tabel op een perceel in een plan parcial. | [D03 §2.4; 2/5] |
| **Opslag** | `parcel` (RC 14/20, oppervlakte `ss`, gebruik, bouwjaar, gebouwde m², geometrie als coördinatenlijst in EPSG:4326, raadpleegdatum), `object_parcel_candidate` (herkomst tekst/adres/pin, afstand, oppervlakteafwijking, zekerheid), `registry_unit` (finca registral), `zoning_signal` (laag, vlak, "raakt" of overlap, laagdatum, dienststatus, bewijstype) en `rule_version` (versie van de regeltabel waarmee een dossier is beoordeeld). Zie §3.8. | Ontwerp [R11 §7; 4] [D03 §5.2; 4] |
| **Detectie** | Percelen veranderen zelden (ATOM twee keer per jaar); hercontrole bij het openen van een dossier. Catastro onbereikbaar = BRON NIET BEREIKBAAR, geen verouderde koppeling als "actueel" tonen. Wijzigt de laagdatum van een GVA/ICV-laag of de versie van de regeltabel, dan krijgen open perceeldossiers een heranalysetaak. Een onbereikbare laag geeft BRON NIET BEREIKBAAR per laag, niet voor de hele run. | [B65; 2] [R13 §11; 4] |
| **Analyse** | Koppelingsketen met correcties: (1) RC in de tekst → alleen kandidaat, pas HOOG na oppervlaktecheck (voorbeeld: RC in advertentie 103305763 hoort bij 2.207 m², advertentie noemt 1.500 m²). (2) Zichtbaar adres → `Consulta_DNPLOC` (voorbeeld Mar Amarillo 5: 1.060 m², exacte match). (3) Pin → afstandsdienst en punt-in-polygoon. **Verborgen adres: hoogstens MIDDEL**, en eerst advertentie-tegen-advertentie vergelijken (zelfde straat, m², bebouwbare m²). Voorbeeld Montgó: pin in bebouwd perceel 0281206, maar een tweede advertentie met dezelfde cijfers ligt op 0281202 (onbebouwd, 129 m verderop), dus koppeling LAAG. Conflict tussen advertentietype en Catastro-gebruik = markering, geen automatische conclusie. Prijsbereik apart: alleen grond / grond + bouw / onbekend. | [B62; 3] [B61; 3] [R11-verificatie R11-07, A8; 3] |
| **Dossier** | Perceelblad: kandidaten met afstand en afwijking, kaartbeeld (intern), vermelding "Bron: Dirección General del Catastro, geraadpleegd <datum>". Niet presenteren als "información catastral" en originele Catastro-gegevens niet ongewijzigd aan derden geven. Bij MIDDEL of LAAG de vaste zin: "Bouwmogelijkheden nog niet betrouwbaar te bepalen: exacte perceelidentificatie ontbreekt." Volgende stap: RC bij de verkoper vragen, of een nota simple (A3-approval; 9,02 € + btw per finca). Die toont wettelijk de RC en of de finca met het Catastro gecoördineerd is. Bij HOOG na poort 1: het bouwmogelijkhedenoverzicht (§16) volgens het invulblad van deliverable 03 §2.3 D, per punt met document, artikel, status en bewijstype, met de vaste waarschuwing "Uitkomst van de GVA-laag en de PGOU-tabellen is een eerste filter. Bouwrecht pas na informe urbanístico of cédula (art. 246 TRLOTUP), controle van plan parcial/UA, en toets door een lokale architect." Bronvermelding kaartlagen: "Generalitat Valenciana / ICV" (CC BY 4.0), MITECO waar gebruikt. | [B66; 2] [B69; 2] [B72; 2] [D03 §2.3; 2/4] |
| **Handmatige poorten (stap 7, 12, 13)** | Taken op de reviewpagina, elk met approval van Jan waar geld of contact nodig is. **Poort 1 — perceel bevestigen:** RC schriftelijk van de aanbieder (bericht pas na Jans "ja"), Sede-pdf "Consulta descriptiva y gráfica" (handmatig), of nota simple (9,02 € + btw per finca; legitiem belang; aanvrager wordt 3 jaar bewaard). **Poort 2 — schriftelijke gemeentelijke informatie:** informe urbanístico of cédula de garantía urbanística (art. 246 TRLOTUP; wettelijke termijn 1 maand; tasa ONBEKEND; loket sede electrónica Xàbia, alleen handmatig), met de vragen G1–G12 uit deliverable 03 §5.3. **Poort 3 — architect:** interpretaties en scenario's laten toetsen (vragen A1–A9). Pas na poort 3 gaat een perceel naar de volledige financiële analyse. | [D03 stap 7, 12, 13 en §5.3; 2/4] |
| **Rapport** | Niveau 2 "beste percelen en ontwikkelkansen", altijd met zekerheidsniveau en per laag signaal of dienststatus; niveau 2 "onderzoeksdossiers met ontbrekende informatie" | [MP §24] |
| **Blokkade** | Geen rechtenblokkade voor Catastro (eigen gebruik en getransformeerde producten toegestaan; geen massale download) en de ICV-lagen (CC BY 4.0, bronvermelding). IGME: "No está permitido implementar un servicio de valor añadido no gratuito sin establecer contacto con el IGME"; of intern gebruik daaronder valt, is [te verifiëren]; de laag is optioneel. Bouwconclusies alleen na poorten 1–3. | [B66; 2] [B100; 2] [R13 §7; 2] |

**Registerregels die vóór de bouw van de perceeladapters in `bronnenregister.json` moeten komen** (velden uit masterprompt §7; statussen volgens de regel "actief pas als het getest draait"). Stand 15-09-2026: deze lagen staan in het register als R2-60 t/m R2-69 (zie deliverable 02 bijlage B, blok L).

| Naam | URL | Type | Toegang | Status | Opmerking |
|---|---|---|---|---|---|
| ICV Planeamiento (WFS/WMS) | https://terramapas.icv.gva.es/0702_Planeamiento | Officiële geodata | Open, geen sleutel; bbox in EPSG:25830 | TECHNISCH ONDERZOEK NODIG | CC BY 4.0, "carácter informativo"; bevat 20 vlakken van de vernietigde homologación Portitxol. R12 gaf "GEVERIFIEERD EN ACTIEF"; strenger gezet omdat nog niets draait |
| ICV sectorale lagen (0701, 0505, 0506) en ICV ArcGIS REST | https://terramapas.icv.gva.es/0701_InfraestructuraVerde · https://carto.icv.gva.es/arcgis/rest/services/tm_infraestructuras/ordenacion_territorial/MapServer | Officiële geodata | Open, geen sleutel | TECHNISCH ONDERZOEK NODIG | CC BY 4.0; licentie van de ArcGIS-diensten "niet vermeld in JSON" [te verifiëren]; PATIVEL-ámbitos zijn lijnen |
| IDEE — overstromingsgevaar (ARPSI) | https://servicios.idee.es/wms-inspire/riesgos-naturales/inundaciones | Officiële geodata | Open | TECHNISCH ONDERZOEK NODIG | Vermelding MITECO; eenheid T100-waarde niet vermeld |
| IGME GEODE (geologie) | https://mapas.igme.es/gis/services/Cartografia_Geologica/IGME_Geode_50/MapServer/WMSServer | Officiële geodata | Open | TECHNISCH ONDERZOEK NODIG | Contact vereist vóór een betaalde dienst met toegevoegde waarde; geen juridische werking |
| MITECO — kust (DPMT) en waterlopen (DPH) | https://wms.mapama.gob.es/sig/Costas/DPMT | Officiële geodata | Op 15-09-2026 onbereikbaar | TECHNISCH ONDERZOEK NODIG | Download `dpmt.zip` (12,2 MB) alleen met akkoord van Jan |
| GVA-planregister Xàbia (documenten) | https://mediambient.gva.es/auto/urbanismo/reg-planeamiento/2%20ALICANTE/03082%20X%C0BIA/ | Officieel register | Open directory met pdf-scans | ALLEEN HANDMATIG | Bron voor de regeltabel; register onvolledig (PP Ermita II en PP La Guardia-3 zonder documenten) |

Bron van deze regels: [D03 stap 8 en 10; 2/3] [R13 §7; 3] [R12 §8 en R12-verificatie R12-17; 2/3].

**3.5 Module C — Veilingen en bijzondere verkopen (BOE, AEAT, portaal)**

| Schakel | Fase B-ontwerp | Status en bron |
|---|---|---|
| **Bron** | (1) BOE-sumario-API, dagelijks; levert XML én JSON mits een `Accept`-header is gezet. (2) BOE-RSS Sección IV (justitie) en V-B (AEAT, SUMA, TGSS-patrimonium) als redundantie. (3) Tekst per aankondiging via `txt.php?id=`, niet via `xml.php`, want dat pad staat in de robots.txt van boe.es. (4) AEAT-lijst `bienes.js`, CC BY 4.0, met kadasterreferentie, gps, waardering, lasten en einddatum. (5) E-mailmeldingen van het veilingportaal in Jans account. | Sumario 20260914: HTTP 200, JSON [W1; 3]; `bienes.js` HTTP 200, Last-Modified 14-09-2026 13:24 GMT [W2; 3]; licentie en hergebruik [B45; 2]; robots [B44; 3] |
| **Adapter** | `boe.py`: Sección IV-items met Dénia/Denia in titel of orgaantekst (oude én nieuwe orgaannamen) worden signaal "rechtbank Xàbia". Overige gerechtelijke items in de provincie worden laag gelogd, want de locatie is onbekend. V-B-items van SUMA of AEAT worden signaal. Het SUB-id komt uit de tekst. Een 404 vóór publicatie (gezien om 03:00 op 15-09) is **geen** bronuitval. Ook prefix SUB-JC (concursaal) en centrale veilingdiensten met een andere stadsnaam herkennen. `aeat.py`: `cp` is een getal zonder voorloopnul; filter op gemeentecode, gps-bounding-box of genormaliseerde postcode (Xàbia-gemeentecode [te verifiëren]; gps ontbreekt bij 29 van 230). | [B43; 2] [R08-verificatie A1, A4, A5, A13; 3] |
| **Waarom geen automatische Jávea-filter op BOE** | Aankondigingen bevatten wettelijk alleen orgaan, nummer en portaallink, niet de plaats van het goed. Een Xàbia-object is aan BOE-data alleen niet te herkennen. Lokaliseren kan via de AEAT-lijst, via portaalmeldingen op plaats of postcode, via handmatige detailcontrole, of via toestemming van de AEBOE voor gerichte detailraadpleging. | [B47; 2] [R08-verificatie F1; 2 en 3] |
| **Opslag** | `auction` volgens R08 §10.3 en het veilingdossier van deliverable 04 §2.8 (portaal-id, BOE-id, type J/N/A/R/G/JC/TGSS, orgaan, status, data, waarde, taxatie, minimumbod, waarborg, aangeboden recht via `offered_right`, bezit, lasten, RC en finca via `registry_unit`, documenthashes) **zonder** namen van schuldenaren. Tijdstempels: alle zes uit masterprompt §10. Veld 44 van het veilingdossier in deliverable 04 noemt `source_modified_at` niet; dit plan vult dat aan (bijvoorbeeld de `Last-Modified` van `bienes.js` of het moment waarop de teksthash van een aankondiging wijzigt). | [B86; 2] [R16 §4.5; 4] [D04 §2.8; 4] [W2; 3] [MP §10] |
| **Detectie** | NIEUW GEPUBLICEERD (BOE-datum = `source_published_at`, deze bron heeft wél een publicatiedatum), NIEUW DOOR ONS ONTDEKT, STATUS GEWIJZIGD (uit portaalmelding of handmatig), DOCUMENTEN GEWIJZIGD (hash van de tekst), NIET MEER GEVONDEN (item verdwenen uit `bienes.js`), BRON NIET BEREIKBAAR (API-fout ná het publicatietijdstip op een werkdag; `bienes.js` > 48 uur niet ververst) | [R08 §10.3; 4] |
| **Analyse** | Deadlinecalculator per kanaal (tabel hieronder); waarborg als liquiditeitsbeslag, niet als kosten. Harde blokkades: aandeel < 100 %, blote eigendom, bezit onbekend, lasten onbekend, recht van terugkoop. **Geen biedadvies zonder juridische beoordeling** (bewijstype 6). ITP-grondslag bij veiling: volgens een secundaire bron hanteert de DGT het hoogste van valor de referencia en remate; de ATV-praktijk is [te verifiëren]. | [B47–B54; 2] [B96; 1] |
| **Dossier** | Veilingdossier (§19/§25) met documenten die Jan na inloggen handmatig ophaalt (edicto, certificación de cargas, taxatie, registerinformatie) en een taak "SUB-id handmatig openen" | [R08 §1.4; 2] |
| **Rapport** | Niveau 1 "naderende deadlines" (T−7, T−3, T−1); niveau 2 "beste veiling- en bijzondere verkoopkandidaten"; eerlijk "0 in Xàbia/Dénia vandaag" | [MP §24] |
| **Handmatige kanalen** | Wekelijkse en maandelijkse rondes M5–M8 uit deliverable 04 §2.9: portaalalerts (M5), detailcontrole binnen 1 werkdag na signaal (M6), checklist TGSS, tablón Xàbia, BOP Alicante, subastasprocuradores.com en eActivos (wekelijks), GVA-patrimonium en SUMA adjudicación directa (maandelijks) (M7), bank- en servicerkanalen (M8). Uitkomst als notitie met link op de reviewpagina; geen namen. Uren: §6.7. | [D04 §2.9; 4] |
| **Bank- en servicervastgoed** | Stand 15-09-2026: Idealista "de bancos" in Jávea **0 woningen en 1 perceel** (111869151, 904.000 → 725.000 €); Servihabitat Profesionales toont in Jávea **2 Sareb-percelen**. Het Idealista-perceel is waarschijnlijk hetzelfde object als kandidaat **K10** uit deliverable 03 (Idealista 107655781 met dubbel 111869151, zelfde prijs en m²) en als **Sareb-perceel A** "Balcón al Mar" (16 fincas, 17.775 m², sector "PGOU UA BALCON AL MAR 1", alleen voor professionals). Identiteit: bewijstype 4 (niet via RC bevestigd). Planklasse tegenstrijdig, bewijstype 7: Idealista "Terreno urbanizable", Servihabitat "urbano no consolidado". Volgens de servicer btw in plaats van ITP (bewijstype 1). Grondobjecten uit dit kanaal gaan eerst door module B. | [R10-verificatie R10-08, R10-09, A4; 1/3] [R01-verificatie R01-12; 3] [R15 K10 en R15-verificatie R15-09; 1/3] |
| **Blokkade** | Geen voor BOE en AEAT. Detailpagina's automatisch ophalen: toestemming AEBOE nodig (robots.txt `Disallow: /`). Portaalmeldingen: registratie door Jan als natuurlijk persoon, gebruiksvoorwaarden ONBEKEND tot registratie. Servicer-portalen: ALLEEN HANDMATIG (voorwaarden verbieden extractie). | [B40; 3] [B41; 2] [D04 §2.11; 1] |

Steekproef 15-09-2026, provincie Alicante, onroerend goed: 41 veilingen "próxima apertura" (21 gerechtelijk, 17 SUMA, 3 AEAT) en 41 "celebrándose" (38 gerechtelijk, 3 AEAT); 0 in Xàbia; 0 van een orgaan in Dénia [B42; 3]. De module moet een lege dag dus gewoon kunnen melden.

**Deadlineregels voor de calculator** (portaalveld en edicto zijn altijd leidend)

| Kanaal | Biedtermijn | Verlenging | Waarborg | Restbetaling | Bron |
|---|---|---|---|---|---|
| Gerechtelijk (LEC, sinds 03-04-2025) | 20 kalenderdagen, onverlengbaar; biedingen geheim tijdens de veiling | geen | onroerend goed 20 % (min. 1.000 €), LAJ mag afwijken | 20 dagen na sluiting (bij bod ≥ 70 %) | [B47; 2] |
| AEAT (RGR) | 20 kalenderdagen, één veiling | sluit pas 1 uur na het laatste bod, max. 24 uur | 5 % bij onroerend goed | 15 dagen na notificatie | [B48; 2] [B51; 2] |
| SUMA (Diputación Alicante) | 20 kalenderdagen | sluit pas 1 uur na het laatste bod | minimaal 5 % | 15 dagen na notificatie | [B52; 2] |
| Notarieel | ≥ 20 kalenderdagen; biedingen zichtbaar | [7] | 5 % | 10 werkdagen | [B49; 2] |
| TGSS (eigen portaal, niet op BOE) | gesloten enveloppen | n.v.t. | 25 % per cheque | 5 werkdagen; voorkeursrecht TGSS 30 dagen | [B50; 2] [B54; 2] |

**3.6 Module D — Dealflow van partners (route C en D), handmatig**

Masterprompt §9 vraagt een zoekprofiel, een aanleverformulier en een opvolgprocedure voor vroege dealflow, en §2 houdt de routes C en D apart. R07 §5 en R06 leveren daarvoor concepten; er is niets verzonden. In fase B wordt dit een klein, handmatig onderdeel van de reviewpagina (ontwerp, bewijstype 4).

| Onderdeel | Fase B-ontwerp | Bron |
|---|---|---|
| **Zoekprofiel** | `zoekprofiel.yaml`, versiebeheerd. Werkgebied: Jávea/Xàbia plus Benitatxell, Dénia, Gata de Gorgos en Teulada-Moraira; daarbuiten alleen bijzondere verkopen. Drie categorieën (renovatie, percelen en ontwikkeling, bijzondere verkopen) met hun signalen en een lijst "wat wij niet zoeken". Prijsklassen zijn WERKHYPOTHESEN tot Jans investeringskader er is (renovatie 250.000–900.000 €; villapercelen 150.000–800.000 €; bijzondere verkopen zonder ondergrens, boven 1.500.000 € alleen met een investeerder). Gebruikt voor de filters in het rapport en als basis voor de partnertekst. | [R07 §5.1; 4] |
| **Aanleverformulier (24 velden)** | Splitsing volgens ADR-0014. **In GoHighLevel** (formulier en contact): blok A partner (1 bedrijfsnaam, 2 contactpersoon en functie, 3 telefoon en e-mail, 4 RAICV-, colegiado- of CIF-nummer, 5 rol, 6 mandaat) en blok D afspraken (20 vergoeding, 21 contact met de verkoper, 22 geheimhouding, 23 bevestiging, 24 toestemming voor contact per e-mail en telefoon). **Op de reviewpagina** als "partneraanlevering": blok B object (7 categorie t/m 18 "al gepubliceerd, waar?") en blok C documenten (19). In fase B neemt een medewerker die objectvelden handmatig over uit het GHL-formulier of de mail; een automatische koppeling GHL → reviewpagina hoort bij fase C. De reviewpagina bewaart van de partner alleen: verwijzing naar het GHL-contact, bedrijfsnaam, rol (5) en mandaat volgens de partner (6, bewijstype 1), plus de vlaggen 21 en 22 als dealmakersvoorwaarden. Geen persoonsnaam, telefoon of e-mail. Veld 18 voedt de dedupe; veld 9 (adres, coördinaat of RC) voedt module B. | Velden [R07 §5.2; 4]; GHL als CRM van waarheid [ADR-0014, lokale feiten; 3]; geen contactvelden [R16 §6.5; 4] |
| **Opvolgprocedure** | Taken met deadline op de reviewpagina (voorstel R07): ontvangst binnen 1 werkdag, met dedupecontrole op referentie, coördinaten plus oppervlak, en prijs plus slaapkamers plus perceel; eerste oordeel binnen 5 werkdagen (kadaster, planologie via module B, vergelijking van vraagprijzen §3.7, dealhypothese); besluit binnen 10 werkdagen (bezichtigen, vragen of afwijzen met reden); terugkoppeling elke 2 weken zolang het dossier open is. Een overschreden termijn verschijnt in niveau 1 van het rapport. Berichten aan de partner gaan vanuit GHL, en pas na Jans akkoord. | [R07 §5.3; 4] |
| **Partnerregister** | Tabel `provider`: bedrijfsnaam, website, vestiging, rubrieken (percelen, renovatie, nieuwbouw, bank) zoals gezien, websiteplatform, bron, bewijstype en controledatum. Eerste vulling uit R06 §3, met de correcties uit de tegenspraak: bij een deel van de "Paagees"-sites is Sooprema het CRM; Koch & Varlet heeft wél een website; de renovatierubriek van Euro Javea en 123 Javea Villas is niet bevestigd; het bankfilter in het Inmoweb-sjabloon bewijst geen bankvoorraad. Partnerstatus als eigen veld (`onbekend` / `eerste ring` / `benaderd` / `actief` / `geen samenwerking`; ontwerp) plus partnerprestaties (aangeleverd, bezichtigd, geboden, gekocht, reactietijd van TREE). Contactpersonen, telefoon, e-mail, toestemmingsstatus en Robinson-controle staan alleen in GHL. | [R06 §3, §8; 1/3] [R06-verificatie R06-06, R06-07, R06-11, R06-13; 3] [R07 §5.3; 4] |
| **Route C (Build/Live)** | Label met reden (bijv. renovatiebehoefte, stilgevallen bouw) en een aparte beoordeling "commerciële aansluiting" (§23). Geen benadering van eigenaren vanuit Deal Hunter; de commerciële contactstatus staat in GHL. Een object met renovatiebehoefte is geen geïnteresseerde klant. | [MP §2, §23, §26] |
| **Harde grenzen** | Niets verzenden zonder expliciet "ja" van Jan. Geen exclusiviteit, mandaat of commissierecht veronderstellen. Commerciële e-mail aan een makelaarskantoor vraagt voorafgaande, uitdrukkelijke toestemming (LSSI art. 21; uitzondering bij een bestaande klantrelatie). De conceptberichten in R07 §5.4 bevatten merkclaims die eerst bevestigd moeten worden, waaronder het jaartal (2022 of 2023: [te verifiëren]). Afzender is TREE; Rocksure blijft erbuiten. | [MP §9] [R16 §4.7; 2/4] [R07-verificatie R07-15, R07-16, F2; 2/3] |

**3.7 Waardering en maximale koopprijs in fase B**

Masterprompt §20–22 vraagt per kandidaat een waardebandbreedte en een maximale koopprijs, teruggerekend vanuit een conservatieve verkoopopbrengst. Voor fase B is er géén toegestane bron van transactieprijzen. Dit onderdeel legt vast hoe een dossier toch aan een eerlijke bandbreedte komt, en waarom de koopprijs voorwaardelijk blijft.

| Waardebron | Wat het levert | Mag in fase B? | Gebruik | Bron |
|---|---|---|---|---|
| Idealista-assistent (in een sessie) | Vraagprijzen, m², perceel, type, zone, eventuele prijsdaling; in `property_detail` ook bouwjaar en energielabel | ALLEEN HANDMATIG. Per vergelijkingsobject alleen link, code, vraagprijs op datum, m², type en eigen notitie ("verdedigbaar", [advocaat]). Geen prijshistorie uit portaaldata opbouwen (niet toegestaan) | Vergelijkingsobjecten in het waardeblad | [R16 §3.8 handelingen 2, 3 en 6; 4] [B34; 3] |
| BP-feed | Vraagprijzen van het netwerk | Pas na het BP-akkoord | Idem | [B20; 2] |
| Tinsa Radar | Studie per zelf getekend gebied: gemiddelde testigowaarden uit taxaties en aanbod, onderhandelingsmarge; testigos ouder dan 12 maanden vervallen. 29 € per studie, 99 €/maand (15 studies) of 259 €/maand (45); btw ONBEKEND | ALLEEN HANDMATIG; geen abonnement; gebruik in klantdossiers [te verifiëren] | Second opinion per serieus dossier, pdf in het dossier, na akkoord van Jan (kosten = A3) | [B114; 1] [R04-verificatie R04-04; 1] |
| MIVAU | Per gemeente alleen het aantal transacties; taxatiewaarde per m² voor gemeenten boven 25.000 inwoners (Jávea hoort daarbij); kwartaal, ruim een kwartaal vertraging | Gemeentelijk XLS: licentie [te verifiëren]; geen XLS-lezer zonder installatie | Handmatige marktcontext per kwartaal, nooit als objectwaarde | [B115; 2/3] |
| Fotocasa-index Jávea | €/m² per wijk, alleen pisos y áticos, op basis van advertenties | ALLEEN HANDMATIG | Context voor appartementen | [B117; 1/3] |
| Portal Estadístico del Notariado | Koopsommen per gemeente en postcode | Alleen persoonlijk gebruik; geen commercieel gebruik en geen opname in databanken | **Niet** in Deal Hunter; hooguit een handmatige toets met datum in één dossier na advies van de advocaat | [B116; 2] |
| Catastro valor de referencia | Fiscale grondslag (ITP), geen marktwaarde | ALLEEN HANDMATIG (Cl@ve) | Alleen in het fiscale blok | [B68; 3] [B91; 2] |
| idealista/data, Accumin (Tinsa Digital AVM), Casafari, DataVenues | Comparables, AVM, sluitprijzen volgens aanbieder | CONTRACT OF TOESTEMMING NODIG; prijzen op offerte | Fase D | [B35; 2] [D02 §6-C; 1/7] |

**Waardeblad per dossier** (ontwerp, bewijstype 4)

1. Drie waarden apart (§20): huidige staat; na renovatie (route A) of opbrengstwaarde van het project (route B); waarde van het aangeboden recht. Een aandeel of blote eigendom is in fase B een harde blokkade, dus daar geen waarde.
2. Vergelijkingsobjecten worden door een mens gekozen, in dezelfde of aantoonbaar vergelijkbare microlocatie op basis van coördinaat of kadaster, niet op een zonenaam in de tekst: "een naam in de tekst is geen ligging" [R06-verificatie R06-16; 3]. Eerst ontdubbelen, dan tellen: in één set stonden 18 groepen dubbele advertenties, en K07 staat onder minstens 10 codes [R15-verificatie R15-04, R15-06; 3]. Per object: URL zonder utm-parameters, datum, vraagprijs, m² (veld en tekst apart), type, perceel, staat en correcties met reden.
3. **Minimaal zes vergelijkingsobjecten.** Die grens is ontleend aan de officiële taxatieregel voor de vergelijkingsmethode, "al menos seis transacciones u ofertas de comparables" (Orden ECO/805/2003 art. 21) [B118; 2]. Wij zijn geen taxateur: voor ons is dit een ontwerpregel, geen wettelijke plicht. Minder dan zes: label "steekproef te klein" en geen basisscenario.
4. Uitkomst: conservatief, basis en gunstig, in €/m² en in euro, met peildatum, aantal, spreiding en het vaste label **"vraagprijzen, geen transacties"**. Mediaan correct berekenen bij een even aantal (in R15 fout gegaan) [R15-verificatie R15-14; 3]. Een vaste korting van vraagprijs naar verwachte verkoopprijs is ONBEKEND en wordt niet verzonnen; het conservatieve scenario is voorlopig de onderkant van de gecorrigeerde bandbreedte.
5. Onbevestigde uitbreidingsrechten, toekomstige bestemmingswijzigingen en niet-geziene licenties tellen niet als waarde. De geclaimde licentie van K07 telt dus pas mee na poort 2 [MP §20] [D03 §2.6 K07; 1/4].
6. Bewijstype: vergelijkingsobjecten 1, bandbreedte 5; betrouwbaarheid "laag" zolang er geen transacties of taxatie zijn.

**Maximale koopprijs.** `finance.py` rekent terug vanuit het conservatieve scenario, met iteratie omdat belastingen en rente van de prijs afhangen [R14 §6.3; 5]. In fase B heet de uitkomst altijd **"voorwaardelijke prijsanalyse"**, met de voorwaarden zichtbaar: (a) de opbrengst rust op vraagprijzen; (b) de rendementseis van Jan; (c) bouwkosten uit eigen nacalculatie, of anders een gelabelde landelijke indicatie (bewijstype 1); (d) bij percelen poorten 1–3, bij veilingen het advocaatoordeel en de eigen marktwaarde (velden 35 en 39 van het veilingdossier). Ontbreekt de rendementseis, of heeft het waardeblad minder dan zes objecten, dan geen bedrag maar de regel "maximale koopprijs niet te bepalen: <wat ontbreekt>". Naast het maximum toont het dossier de vraagprijs, de indicatieve marktwaarde als bandbreedte, en de gevoeligheid voor −10 % opbrengst, +15 % bouwkosten en +6 maanden [R14 §6.3 punt 7; 5]. De indeling "geschikt voor onderhandeling" uit deliverable 01 §2.9 vraagt een maximale koopprijs met Jans eis; in fase B kan een dossier die indeling alleen krijgen met de vermelding dat die prijs voorwaardelijk is.

**3.8 Datamodel en veldmapping**

**Entiteiten (masterprompt §11)** — ontwerp, bewijstype 4. Alle relaties zijn waar nodig veel-op-veel; niets wordt samengevoegd op alleen urbanisatie en afmetingen.

| Entiteit | Tabel | Belangrijkste velden | Relaties en bijzondere gevallen | Bron |
|---|---|---|---|---|
| Advertentie | `listing`, `listing_event` | Bron, bron-id, URL zonder utm, vraagprijs, `price_scope` (grond / grond + bouw / onbekend) en prijscomponenten (grond, licentie, project, aval, tasas), m² per bron apart, zes tijdstempels uit §10, inhoudshash | Via `object_listing` (met `match_confidence`) naar één object; prijsverschillen en tegenstrijdige m² blijven zichtbaar | [MP §10, §11] [R11 §7.3; 4] [D03 stap 0; 4] |
| Fysiek vastgoedobject | `property_object` | Type, gemeente-id, microlocatie, locatie met nauwkeurigheid, kenmerken, vijf gescheiden statussen (object, onderzoek, investering, commercieel contact als verwijzing naar GHL, veiling) | Veel-op-veel naar percelen; kan deel zijn van een pakket of project | [MP §11, §26] |
| Kadastraal perceel | `parcel` | RC, `ss`, geometrie, gebruik, bouwjaar, raadpleegdatum | Veel-op-veel naar objecten en naar finca's; meerdere aangrenzende percelen bij één advertentie ("dos parcelas") | [R11 §7.3; 4] |
| Geregistreerde eigendomseenheid (finca registral) | `registry_unit` | Fincanummer, register, IDUFIR/CRU, registrale oppervlakte, coördinatiestatus met het Catastro (art. 10.4 LH), bron (nota simple met datum) | Veel-op-veel naar percelen; bij niet-gecoördineerde finca's blijven advertentie-, Catastro- en registrale oppervlakte apart. Eigenaar en lasten alleen in het afgeschermde dossierdeel | [R11 §6.3; 2] [B72; 2] [D04 §2.10; 4] |
| Aangeboden eigendomsrecht | `offered_right` | Soort (volle eigendom, onverdeeld aandeel, blote eigendom, vruchtgebruik, vordering, ander, ONBEKEND), percentage, bron, bewijstype | Per advertentie of veilinglot. Alles behalve 100 % volle eigendom is in fase B een harde blokkade. BP levert dit niet: ONBEKEND, nooit "volle eigendom" aannemen | [D04 §2.8 veld 12; 2/4] [R05 §7; 4] |
| Aanbieder | `provider` | Bedrijfsnaam, soort (makelaar, listingdienst, servicer, rechtbank, AEAT, particulier zonder naam), rol, partnerstatus, verwijzing naar GHL | Veel-op-veel naar advertenties. Bij een particuliere adverteerder geen naam of contact. `property_detail` van de Idealista-assistent toont de bedrijfsnaam, `search_properties` niet | §3.6 [R05-verificatie aanvulling 1; 3] |
| Veiling of verkoopprocedure | `auction` | Zie §3.5 | Eén procedure, meerdere loten; een lot kan meerdere objecten of finca's omvatten | [R08 §10.3; 4] [D04 §2.8; 4] |
| Ontwikkelproject | `development_project` | Naam, promotor (bedrijf), fase (plan, licentie, in aanbouw, stilgevallen), aantal eenheden, licentiegegevens als claim | Eén project, meerdere eenheden (objecten); gevoed door partneraanlevering veld 15 | [MP §11] [R07 §5.2; 4] |
| Pakket | `package` | Omschrijving, prijs voor het geheel, aantal delen | Meerdere objecten of finca's onder één prijs. Voorbeelden: K10 = Sareb-perceel A (identiteit waarschijnlijk, bewijstype 4; 16 fincas, 725.000 € voor 17.775 m² samen); BP 4628JAV ("cuatro parcelas registrales"; perceel 7.276 m² in het veld tegenover 7.353 m² in de tekst) | [R10-verificatie R10-08; 1/3] [R05 §3.2, R05-verificatie R05-13; 1/3] |
| Waardering | `valuation`, `comparable` | Zie §3.7 | Per dossier en peildatum; vergelijkingsobjecten ontdubbeld | [MP §20] |
| Planologische signalen en regels | `zoning_signal`, `rule_version` | Zie §3.4 | Per perceel, per laag, per regelversie | [D03 §5.2; 4] |

**Veldmapping Background Properties (lokale API → intern).** Adapter leest `/api/properties` met volledige paginering. Regels: lege waarde = ONBEKEND (nooit 0, "nee" of "vrij"); elke waarde krijgt bron `bp`, bewijstype 1 en de ophaaltijd; afgeleide velden krijgen bewijstype 4 en de regel waarmee ze zijn afgeleid. Vulling gemeten op de 56 Jávea-objecten op 15-09-2026 om 04:48 CEST [L9; 3]; percentages over de hele feed staan in R05 §3.2.

| API-veld | Kyero v3 | Intern veld | Transformatie en ONBEKEND-regel | Gevuld (n = 56) |
|---|---|---|---|---|
| `id` | `id` | `source_id` | String, primaire sleutel (vrijwel zeker het WordPress-post-id, bewijstype 4); ontbreekt → record weigeren | 56 |
| `ref` | `ref` | `source_ref` | Trimmen; nooit als identiteit (bij 39 van 225 wijkt de ref af van de URL) | 56 |
| `date` | `date` | `source_modified_at` | Europe/Madrid → UTC; volgens Kyero "last modified", dus nooit `source_published_at` (die blijft ONBEKEND) | 56 |
| `price`, `currency`, `priceFreq` | `price`, `currency`, `price_freq` | `asking_price`, `currency`, `price_type` | Geheel getal in EUR; `sale` | 56 |
| `type` | `type` | `property_type` | Land → perceel; Villa → vrijstaand; Apartment → appartement; Town house → rijwoning; Country house → finca; Commercial property → commercieel; leeg → ONBEKEND | 54 (2 leeg) |
| `newBuild` | `new_build` | `is_new_build` | Boolean; BP gebruikt dit ook voor projecten in aanbouw (bewijstype 4) | 56 (17 × waar) |
| `town` | `town` | `municipality_raw`, `municipality_id` | Ruwe waarde bewaren; sleutel via aliastabel (Javea/Jávea/Xàbia/JAVEA/XABIA → 03082) | 56 ("Javea") |
| `postcode` | `postcode` | `postcode` | Vijf tekens met voorloopnul; leeg → ONBEKEND | 19 |
| `province`, `country` | `province`, `country` | idem | — | 56 |
| `locationDetail` | `location_detail` | `microlocation` | Urbanisatienaam; leeg → ONBEKEND | 55 |
| `latitude`, `longitude` | `location` | `lat`, `lng`, `location_accuracy` | Buiten Spanje verwerpen; 25.68654 / −80.431345 → ONBEKEND; een pin is nooit planbewijs | 40 (waarvan 3 op het Miami-punt) |
| `beds`, `baths` | `beds`, `baths` | `bedrooms`, `bathrooms` | 0 of leeg → ONBEKEND of n.v.t. (Kyero: 0 = onbekend) | 32 |
| `builtArea` | `surface_area/built` | `built_area_m2` + definitie ONBEKEND | Bruto, netto of bebouwd is niet gespecificeerd; nooit overschrijven met tekst- of Catastro-m² | 33 |
| `plotArea` | `surface_area/plot` | `plot_area_m2` + definitie ONBEKEND | Kadastraal of aanbiederschatting onbekend; meerdere kavels in de tekst → markering "pakket" | 50 |
| `pool` | `pool` (spec: 0/1; BP: tekst) | `pool` | Private/Privé/Privat → privé; Gemeenschappelijk/Common/Communal/communal → gemeenschappelijk; Nee/No → geen; leeg → ONBEKEND. Het API-filter `pool=true` niet gebruiken | 55 (Privé 20, Private 15, Nee 12, No 3, Communal 2, communal 1, Gemeenschappelijk 1, Privat 1) |
| `energyConsumption`, `energyEmissions` | `energy_rating` | `energy_label` | A–G of X; Processing / In aanvraag / In request → "in aanvraag"; leeg → ONBEKEND | 10 (Processing 4, In request 1, A 2, B 1, E 1, X 1); emissions 0 |
| `url` (per taal) | `url` | `source_url` | De parser kent meerdere talen, de feed levert alleen `en` | 56 × `en`, andere talen 0 |
| `desc` (per taal) | `desc` | `description{taal}` (opslaan pas na BP-akkoord) | HTML strippen, `&#13;` ontcijferen | en en es 56, nl en fr 55, de 54 |
| `features` | `features` | `features[]`, afgeleid `garage`, `terrace`, `views`, `price_includes_vat` | Woordenlijst; niet genoemd → ONBEKEND, niet "nee"; "21% VAT" → btw inbegrepen (bewijstype 4) | 55 |
| `images` | `images` | `image_refs[]` | Alleen URL als verwijzing; geen download en geen hash in fase B | 56 |
| — | `catastral` (afwezig) | `cadastral_reference` | ONBEKEND; via module B | — |
| — | — | `offered_right` | ONBEKEND | — |
| — | `agent` (BP zelf) | `provider` | BP als listingdienst; verkopende partner ONBEKEND | — |

Bron mapping en afwijkingen: [L9; 3] [R05 §3.2 en §7; 2/3/4] [R05-verificatie R05-07, R05-08, R05-09; 3]. Een commissieklasse staat niet in `/api/properties` en is voor Deal Hunter niet nodig.

**Handmatige Idealista-invoer → intern:** propertyCode → `source_id`; URL zonder utm → `source_url`; vraagprijs met datum; eerdere prijs zoals de assistent die in de sessie toont → `listing_event` met bron "assistent"; m² uit veld en tekst apart (het veld kan fout zijn: 10.662 tegenover 1.066 m²); type; pin → `lat`/`lng` met nauwkeurigheid "benaderend"; `showAddress`; bedrijfsnaam uit `property_detail` → `provider` alleen bij een professionele adverteerder. Geen omschrijving, foto's of telefoonnummer [R16 §3.8; 4] [R06-verificatie R06-05, R06-15; 3] [B34; 3].

**3.9 Bouwvolgorde binnen fase B** (voorstel, bewijstype 4)

| Stap | Inhoud | Waarom in deze volgorde |
|---|---|---|
| B0 Fundament | Lokale git-repo, `store.py`, schema volgens §3.8, rechtenpoort met `rechten.yaml` afgeleid uit `bronnenregister.json` (inclusief de kaartlaagregels R2-60 t/m R2-69), normalisatie, kill-switch, logging, test-harness met `TEST-`-fixtures in een aparte `data/test.db` | Alles erna leunt hierop |
| B1 Veilingmodule | BOE-sumario/RSS, AEAT-lijst, deadlinecalculator, veilingdossier (met `source_modified_at`) | Geen rechtenblokkade; laat de hele keten zien, van bron tot rapport |
| B2 Perceelmodule | Catastro-keten op handmatige invoer; `zekerheid.py`; `icv_planeamiento.py` en `icv_sectoraal.py` met dienststatus per laag; `bouwregels-xabia.yaml` met documentstatustabel; `bouwvolume.py`; poorten als taken; perceelblad en bouwmogelijkhedenoverzicht; regressietests op de echte gevallen (T09, T10a–e, T27) | Geen rechtenblokkade; nodig voor elk perceel uit elke bron, ook voor bank- en partnergrond |
| B3 Bestaand vastgoed | Handmatige Idealista-invoer; BP-adapter droog, na akkoord met opslag en historie volgens de veldmapping | BP-opslag hangt aan het akkoord |
| B4 Waardering, rekenmodule en beoordeling | Waardeblad (§3.7); `finance.py` met gecorrigeerde parameters en het label "voorwaardelijke prijsanalyse"; labels en blokkades | Vraagt Jans rendementseis; zonder waardeblad geen bedrag |
| B5 Reviewpagina, dossier, rapport, partnerinvoer | 127.0.0.1:8710; sjabloon §25; partneraanlevering, partnerregister en opvolgtaken (§3.6); `zoekprofiel.yaml`; ochtendrapport als lokaal bestand, handmatig gestart | Productieschema pas na keuze van tijdstip en kanaal (§24); GHL-koppeling pas in fase C |
| B6 Proef | Nulmeting per bron, daarna 14 dagrapporten die Jan beoordeelt; meting van de werkelijke handmatige tijd per ronde (§6.7) | Acceptatie fase B |

---

### Deel 4 — Twee technische varianten

| Criterium | Variant 1: nul-installatie (aanbevolen voor B) | Variant 2: eigen Postgres + PostGIS (met akkoord) |
|---|---|---|
| Installaties | Geen. Hermes-venv en SQLite zijn aanwezig [L2; 3] | Docker-image downloaden plus `psycopg[binary]` in een **eigen** venv; beide vragen Jans akkoord (regel 1) |
| Opslag | Eén SQLite-bestand, WAL, R-tree voor bounding boxes, FTS5 voor tekstzoeken | Eigen container (niet de Tree AI OS-database), eigen volume, `pg_dump`-back-up |
| Geografie | Punten, haversine-afstand, eigen punt-in-polygoon en oppervlakte met de shoelace-formule (getest op WFS-geometrie: 1.572,6 m² tegen `areaValue` 1.572) | `ST_Contains`, `ST_DWithin`, buffers, overlap, echte geometrie |
| Gelijktijdig schrijven | Eén schrijver tegelijk; korte transacties | Meerdere processen |
| Afhankelijkheden | Hermes-upgrades kunnen pakketversies wijzigen; versies vastleggen en na elke Hermes-update testen | Docker Desktop (stopte in de nacht van 2 op 3 september 2026, waarna de back-up volgens `waakhond.sh` vier nachten faalde [L7; 3]); RAM in de Docker-VM (7,65 GiB voor alle containers) |
| Arm64-geschiktheid | n.v.t. | `postgis/postgis` bestaat alleen voor amd64. Kiezen uit: emulatie (niet getest, vermoedelijk trager), zelf bouwen, of een niet-officieel arm64-image (`imresamu/postgis`, ouder). `psycopg-binary` 3.3.5 heeft wél een wheel voor Python 3.11 op arm64-macOS. |
| Beheer | Laag | Extra dienst in waakhond en back-up |
| Schaal | Ruim voor Jávea: honderden objecten, duizenden percelen (inferentie) | Groeipad naar Marina Alta en landelijk |
| Bron | [L2; 3] [B05; 3] [R11 §7.4; 5] | [B12; 2] [B13; 1] [B14; 2] [B05; 3] |

**Aanbeveling:** fase B in variant 1, met `store.py` als enige plek die SQL kent.

**Polygonen in fase B: geen overstapmoment.** R17 §4.3 noemde "polygonen snijden" als overstapmoment naar variant 2. Deliverable 03 en R13 zien de toets van één perceelpolygoon tegen de plan- en sectorale lagen juist als standaardstap in fase B, uitvoerbaar met open diensten en eigen code (punt-in-polygoon en oppervlakte getest; overlap via ArcGIS `query` of eigen code nog niet getest, zie §3.4). Dit plan volgt deliverable 03, omdat die op live tests van R11–R13 en hun tegenspraak rust en masterprompt §29 de perceelmodule in fase B eist. Overstappen blijft een apart besluit van Jan, in twee stappen (bewijstype 4):
1. **Geometriebibliotheek** (bijvoorbeeld `shapely` in een eigen venv; installatie = akkoord): zodra buffers nodig zijn (brandstrook, kuststroken), bouwvlakken op onregelmatige percelen, of als de overlapberekening in variant 1 geen regressietest haalt [D03 W8; 4].
2. **Variant 2 (Postgres + PostGIS):** zodra de database voorbij circa 50.000 advertenties of snapshots groeit, of meerdere processen tegelijk moeten schrijven [R17 §4.3; 4], of zodra de perceelmodule veel percelen tegelijk moet toetsen, bijvoorbeeld een sweep over een gebied in plaats van per kandidaat (formulering van dit plan; let op: het Catastro staat geen massale download toe, "No está permitida la descarga masiva") [R13 §7; 2].

**Wat Jan goedkeurt:**

| Variant | Te keuren door Jan |
|---|---|
| 1 | Gebruik van de Hermes-venv (alleen lezen, zoals tree-ai-agentic-os doet); nieuwe bestanden in `~/tree-es/deal-hunter/` (code, `data/`, `logs/`, `.env` met rechten 600); automatisch gebruik per kandidaat en in laag volume van de open Catastro- en GVA/ICV-diensten; later een launchd-taak (nieuwe dienst = akkoord) |
| Tussenstap (alleen bij behoefte) | Een geometriebibliotheek in een eigen venv (download = akkoord) |
| 2 (niet nu) | De keuze voor een image (emulatie, eigen build of niet-officieel), de download ervan, `psycopg[binary]` in een eigen venv, een extra container in waakhond en back-up |

---

### Deel 5 — Het ochtendrapport

**5.1 Inhoud per niveau** (§24; generatie met Jinja2 naar HTML en Markdown, tijden in Europe/Madrid [L2; 3])

| Niveau | Inhoud in fase B | Regel |
|---|---|---|
| **1 — Managementsamenvatting** | Wat verdient vandaag aandacht; nieuwe kansen per module; materiële wijzigingen (BP-prijs, veilingstatus); naderende deadlines (T−7/T−3/T−1) en overschreden opvolgtermijnen van partneraanleveringen; bronnen en kaartlagen die onvolledig of onbereikbaar waren, met "laatste geldige run" | Bronuitval apart melden van "geen kansen" |
| **2 — Gerangschikte selecties** | Beste renovatieobjecten · beste percelen en ontwikkelkansen (met zekerheidsniveau en laagsignalen) · beste veiling- en bijzondere-verkoopkandidaten · interessante prijswijzigingen · commerciële renovatiekansen (route C: label met reden, plus partneraanleveringen; contactstatus in GHL) · onderzoeksdossiers met potentieel maar ontbrekende informatie | Rangschikking op labels, blokkades en bewijskwaliteit, niet op een verzonnen score; geen opvulling met zwakke objecten; een maximale koopprijs altijd met het label "voorwaardelijk" |
| **3 — Volledig overzicht** | Alle kwalificerende nieuwe en gewijzigde objecten met filters (module, route, label, bron) en link naar het dossier op de reviewpagina | Een top tien verbergt niets |
| **Telblok** | Ontvangen advertenties per bron · partneraanleveringen · unieke objecten · nieuwe publicaties (alleen BOE) · nieuwe ontdekkingen · wijzigingen · relevante kandidaten · openstaande controles en poorten · bronactualiteit en dienststatus per kaartlaag | Nulmeting expliciet gelabeld |
| **Slot** | Prioriteiten: welk object, welke actie, waarom, door wie, vóór wanneer | Harde grens: geen bied-, betaal- of verzendacties |

**5.2 Bezorgkanalen**

| Kanaal | Hoe | Bewezen? | Voordeel | Nadeel of voorwaarde | Bron |
|---|---|---|---|---|---|
| Discord rechtstreeks | Bot-API met token uit `.env` (waakhondpatroon); samenvatting ≤ 2.000 tekens, HTML als bijlage | Werkt voor de waakhond van Tree AI OS | Onafhankelijk van Hermes-profielen | Token op een extra plek | [B05; 3] |
| Hermes-cron zonder LLM | `hermes cron create … --no-agent --script … --deliver discord:<kanaal>` | **Nee**: alle drie de G-CEO-jobs `blocked_config`; default-profiel niet getest | Past in de agentorganisatie | Eerst de storing laten oplossen; routines zijn een Gate C-besluit | [L3; 3] [B04; 3] |
| Teams-webhook | Adaptive Card met samenvatting en link | Werkt voor site-alarmen; HTTP 202 bewijst niet dat de kaart zichtbaar is | Al ingericht | Alleen samenvatting | [B02; 3] |
| E-mail via Resend | HTML-rapport als mail | Sleutel niet ingesteld | Gratis tot 3.000 per maand, 100 per dag | Sleutel en afzenderdomein nodig | [B16; 1] |
| Telegram via Hermes | `--deliver telegram` | Niet getest | Mobiel | Zelfde risico als Discord via Hermes | [B04; 3] |

**5.3 Tijdstip: open keuze voor Jan.** De bronnen zijn op verschillende momenten klaar:

| Bron | Wanneer beschikbaar | Bewijs |
|---|---|---|
| BP-export | In de gemeten nacht 01:34–02:55 CEST (één meting); lokale API ververst elk heel uur | [B24; 3] [B01; 3] |
| BOE-sumario van vandaag | 's Ochtends; om 03:00 op 15-09 nog HTTP 404. Het exacte tijdstip is [te verifiëren]. | [R08-verificatie A1; 3] |
| AEAT-lijst | Versie van 15:23 op 14-09 gezien (Last-Modified 13:24 GMT) | [R08 §2; 3] [W2; 3] |
| Hermes G-CEO-routine | 09:00 op werkdagen (nu geblokkeerd) | [R17 §1.4; 3] [L3; 3] |

Drie opties (ontwerp, bewijstype 4): (a) 07:00 met BP van vannacht en BOE van gisteren; (b) rond 09:30 met BOE van vandaag, zodra de publicatietijd is bevestigd; (c) 07:00 met een korte BOE-aanvulling later op de ochtend, alleen als er een Dénia-, AEAT- of SUMA-signaal is. Het productieschema start pas als tijdstip en kanaal vastliggen (§24). Na een stroomuitval haalt `StartCalendarInterval` een gemiste run niet in [B17; 2]; de verwerkingsrun krijgt daarom ook `RunAtLoad`.

**5.4 Urgente meldingen** (configureerbaar, met demping, via het alarmkanaal): prijswijziging op een gevolgd BP-object; nieuwe kandidaat met label "bezichtigen"; veilingdeadline binnen 7 dagen; bron twee keer achter elkaar onbereikbaar.

---

### Deel 6 — Fasering A–D

**6.1 Overzicht**

| Fase | Doel | Uren (schatting) | Euro's | Harde afhankelijkheid |
|---|---|---|---|---|
| **A** Bronnen en kader | Toegang en rechten bevestigen, kader van Jan vastleggen | afronding 10–20 u [R17 §9.1; 4] | Advocaat ONBEKEND (offerte) | Jan: BP, Idealista, advocaat, investeringskader |
| **B** Bewijs in Jávea | Beperkte maar complete keten met drie modules plus handmatige partnerinvoer, in variant 1 | 60–90 u software [R17 §9.1; 4]; handmatige rondes §6.7 | Hosting €0; AI < $10 per maand (USD; btw niet vermeld; berekening) [R17 §2.3; 5]; nota simple 9,02 € + btw per finca; Tinsa Radar 29 € per studie indien gekozen (btw ONBEKEND); informe, cédula, architect en advocaat ONBEKEND | AI-sleutel en -budget; BP-akkoord voor module A; architect en advocaat aangewezen voor de poorten |
| **C** Betrouwbare dagelijkse operatie | Planning, alarm, back-up, bezorging, GHL, feedbacklus | 80–120 u [R17 §9.1; 4] | Resend €0 (als gekozen); beheer 4–8 u per maand [R17 §9.2; 4] | Tijdstip en kanaal; GHL-token; automatisch inloggen van de Mac |
| **D** Groei en verbetering | Meer bronnen en gebied; waardering met gelicentieerde comparables; kalibratie op echte uitkomsten | ONBEKEND | Datalicenties ONBEKEND (offertes) | Offertes; Idealista-API; eventueel variant 2 |

Een euro-bedrag voor ontwikkeluren is niet te geven: wie bouwt en tegen welk tarief is niet vastgelegd (ONBEKEND). De uren zijn een inschatting op basis van de componentenlijst in R17, zonder offerte. De correcties in dit plan verschuiven werk: dHash eruit; rechtenpoort, persoonsgegevensfilter, invoerformulieren, twee kaartlaagadapters met regeltabel, waardeblad en partnerregister erin. Het netto-effect op de urenraming is ONBEKEND; B6 meet de werkelijke uren van B0–B2.

**Valuta AI-kosten.** R17 rekent in §2.3 en §9.2 in dollars ("< $10/maand"), maar schrijft in de samenvatting "AI < €10". De berekening zelf is in USD op de officiële prijspagina, die geen btw vermeldt. Dit plan gebruikt daarom "< $10 per maand (USD)"; het maandplafond dat Jan kiest, wordt in euro vastgelegd en omgerekend in de kostenregistratie [R17 §2.2, §2.3, §9.2; 2/5] [B07; 2].

**6.2 Fase A — bronnen en investeringskader (loopt)**

| Onderdeel | Invulling |
|---|---|
| Doel | Weten wat werkelijk mag en werkt, en met welke cijfers Jan rekent |
| Afhankelijkheden | Jan (akkoorden, kader), advocaat |
| Opleveringen | Deliverables 01–05 (aanwezig); `bronnenregister.json` met statussen uit §7 (aanwezig, 75 regels op 15-09-2026, inclusief de kaartlagen uit §3.4); verstuurde BP-mail en -clausule; Idealista API-aanvraag en toestemmingsvraag; beantwoorde advocaatvragen (R16 §7, in de volgorde van de concrete vervolgstap); aangewezen architect en advocaat met offerte (§6.7); ingevuld investeringskader |
| Kosten | 10–20 u afronding; advocaat en architect ONBEKEND (offerte) |
| Risico's | Rechten blijven ONBEKEND (BP antwoordt niet, Idealista weigert); dan krimpt module A tot handmatig werk |
| Acceptatie | Register compleet en per bron een status; kader ingevuld; drie akkoordvragen verstuurd |

**6.3 Fase B — bewijs in Jávea**

| Onderdeel | Invulling |
|---|---|
| Doel | Aantonen dat één keten van bron tot dossier werkt voor bestaand vastgoed, percelen én veilingen, met eerlijke dekking, een voorwaardelijke prijsanalyse en handmatige partnerinvoer |
| Afhankelijkheden | Variant 1-akkoord (inclusief open kaartlagen); AI-sleutel en -budget; BP-akkoord (alleen module A); Jans parameters (rendement, doorlooptijd); registerregels voor de kaartlagen (§3.4; aanwezig als R2-60 t/m R2-69); architect en advocaat voor de poorten (alleen voor dossiers die zo ver komen) |
| Opleveringen | Stappen B0–B6 (Deel 3.9); `rechten.yaml`; `parameters-2026.yaml`; `bouwregels-xabia.yaml`; `zoekprofiel.yaml`; reviewpagina met partneraanlevering, partnerregister, waardeblad en poorttaken; sjabloon §25 met bouwmogelijkhedenoverzicht; rapport als lokaal bestand; testset T01–T22 en T24–T27 (met T10a–e); nulmeting per bron en per kaartlaag; 14 dagrapporten; gemeten handmatige tijd per ronde |
| Kosten | 60–90 u software; AI-nulmeting BP (225 objecten, tekst + 8 foto's) ≈ $3,94 met Haiku of $7,88 met Sonnet, met Batch de helft (bewijstype 5, aannames R17 §2.3); maandlast < $10 (USD) [B07; 2]; nota simple per bevestigd dossier 9,02 € + btw [B69; 2]; optioneel Tinsa Radar 29 € per studie [B114; 1]; handmatige rondes en professionals: §6.7 |
| Risico's | BP-akkoord blijft uit; Idealista-pins benaderend (2 van 4 geteste pins in geen enkel perceel); Catastro-blokkade bij te veel verzoeken (circa 10 dagen); GVA/ICV-dienst wijzigt zijn CRS-gedrag of MITECO blijft onbereikbaar; onverwachte feeduitval; Hermes-venv wijzigt na een update; auteursrecht bij onbedoelde fotoverwerking; te weinig vergelijkingsobjecten per microlocatie |
| Acceptatie | Tests T01–T22 (met T10a–e) en T24–T27 groen op `test.db`; nulmeting en 14 dagrapporten door Jan bekeken; per module minstens één volledig dossier door Jan beoordeeld, en minstens één perceeldossier dat stap 8 en 10 op de polygoon heeft doorlopen (voorstel, 4); meetwaarden §28 vastgelegd (6.9) |

**6.4 Fase C — betrouwbare dagelijkse operatie**

| Onderdeel | Invulling |
|---|---|
| Doel | Elke dag op tijd een betrouwbaar rapport, zonder stille storingen, met opvolging in GHL |
| Afhankelijkheden | Tijdstip en kanaal (§24); werkende bezorging (Hermes-storing opgelost of rechtstreeks kanaal); GHL: agency-toegang of handmatig aangemaakt schema, plus sub-account-token met `objects/record.*` [B10; 2]; automatisch inloggen van de Mac ([te verifiëren], open punt in ~/CLAUDE.md [L6; 3]); 2 TB USB-SSD voor back-ups (open punt [L6; 3]) |
| Opleveringen | Launchd-plists voor verwerking, rapport, back-up en waakhond; alarm met demping; hersteltest; GHL-koppeling idempotent binnen 100 verzoeken per 10 s [B11; 2], inclusief het partner-aanleverformulier in GHL en de overdracht van de objectvelden naar de reviewpagina [R07 §5.2; 4]; urgente meldingen; feedbacklus (afwijsredenen, modelversies §26, partnerprestaties); na advies van de advocaat eventueel het inlezen van portaalalerts uit de eigen mailbox |
| Kosten | 80–120 u; beheer 4–8 u per maand; Resend gratis tot 3.000 mails per maand [B16; 1]; GHL-kosten voor custom objects [te verifiëren] |
| Risico's | Bezorging via Hermes blijft haperen; Mac start niet door na stroomuitval; eerste ronde van de feeddienst mislukt na herstart; Docker-afhankelijkheid als toch variant 2; GHL-limieten voor Private Integration Tokens onbekend |
| Acceptatie | Alle tests T01–T27 groen; 30 dagen zonder stille storing; hersteltest geslaagd; bezorging aantoonbaar zichtbaar in het gekozen kanaal (T23) |

**6.5 Fase D — groei en verbetering**

| Onderdeel | Invulling |
|---|---|
| Doel | Aantoonbaar meer unieke kansen per euro en per uur, niet meer advertenties |
| Afhankelijkheden | Offertes datalicenties (idealista/data, DataVenues, Casafari e.a.: ONBEKEND) [R17 §11a.3; 1/7]; toekenning Idealista Search API (voorwaarden ONBEKEND) [B30; 2]; toestemming AEBOE voor detailraadpleging; eventueel variant 2 |
| Opleveringen | Extra adapters alleen met status GEVERIFIEERD; uitbreiding naar Marina Alta (let op: 12 gemeenten daar in EPSG:25831, de rest van de provincie in 25830 [B65; 3]); waardering met gelicentieerde comparables of AVM in plaats van alleen vraagprijzen (§3.7); kalibratie van beoordeling en waardeblad op werkelijke uitkomsten |
| Kosten | ONBEKEND; bekende prijspunten zijn geen objectbronnen: DataVenues-widget 30 €/maand + btw, Tinsa Radar 29 €/studie [R17 §11a.3; 1] |
| Risico's | Licentiekosten groter dan de opbrengst; schaalproblemen in SQLite |
| Acceptatie | Kosten per gekwalificeerde kans en foutieve-signaalratio gemeten en dalend; per nieuwe bron bewijs van unieke kansen |

**6.6 Kosten en afhankelijkheden die nog bevestigd moeten worden**

| Post | Wat vaststaat | Wat nog open is | Bron |
|---|---|---|---|
| BP-gebruik voor Deal Hunter | Feed verstrekt voor de website; aviso legal eist schriftelijke toestemming (sjabloon voor de website) | Opslag, historie, AI, beeldhashes, tonen aan klanten; kosten (geen bekend) | [B20; 2] [R05 §6] |
| Idealista | Search API alleen op aanvraag; idealista/data op offerte; assistent zonder aparte voorwaarden | Toestemming voor gepland gebruik; API-voorwaarden en -kosten | [B30; 2] [B35; 2] |
| AI-verwerking | Haiku 4.5 $1/$5, Sonnet 5 $2/$10 per miljoen tokens, Batch −50 %; bedragen in USD, btw niet vermeld; geldt voor de Claude API, niet voor OpenRouter | Keuze sleutel; verwerkersvoorwaarden en geen training op invoer [te verifiëren] | [B07; 2] |
| Nota simple | 9,02 € + btw (Colegio); arancelbasis 3,005061 €; levertijd tegenstrijdig: < 2 uur of 24 uur | Werkelijke factuur bij de eerste bestelling | [B69; 2] [B70; 2] [B71; 2] |
| Architect, advocaat | Colegios mogen geen tariefrichtlijnen publiceren | Bedrag per dossier: offerte (plan in §6.7) | [B95; 2] |
| Informe urbanístico, cédula, licentie | Wettelijke termijn informe en cédula 1 maand; cédula max. 1 jaar geldig (art. 246 TRLOTUP) | Tasas Xàbia ONBEKEND (rubriek "Tasas" alleen handmatig te openen) | [D03 stap 12; 2] [B112; 2] |
| Gestor, topograaf, geotechniek, Registro Mercantil | Nodig per deal volgens deliverables 03 en 04 (fiscale toets ITP of btw + AJD; topografisch plan; geotechniek; uittreksel bij SL-eigendom) | Alle bedragen ONBEKEND | [D03 §2.6 K08; 4] [D04 §2.5; 2/4] |
| Waardering | Tinsa Radar 29 € per studie, 99 €/maand (15), 259 €/maand (45); btw niet vermeld. MIVAU en INE gratis maar zonder objectwaarde. Notariado alleen persoonlijk gebruik | Btw Tinsa; gebruik van Tinsa-pdf's in klantdossiers; licentie gemeentelijk MIVAU-XLS | [B114; 1] [B115; 2] [B116; 2] |
| Handmatige opvolging | Frequenties van de handmatige rondes vastgelegd (deliverable 04 §2.9, R07 §5.3) | Werkelijke tijd per handeling ONBEKEND; raming op werkhypothesen in §6.7 | [D04 §2.9; 4] [R07 §5.3; 4] |
| Lokale heffingen Xàbia | IBI stedelijk 0,83 % en ICIO 4 % (2026, dataset Hacienda) | IIVTNU-tarief ONBEKEND (maximaal 30 %) | [B93; 2] |
| Financiering | Euríbor 12 maanden aug. 2026: 2,954 % | Voorwaarden voor SL of niet-resident: ONBEKEND | [B94; 2] |
| Bouwkosten Jávea | Alleen landelijke platformindicaties (bewijstype 1, lage zekerheid) | Jans eigen nacalculaties; eventueel IVE-BDC (69,99 €/jaar) | [B97; 1] [B98; 1] |
| Rendementseis | — | ONBEKEND, input van Jan | [R14 §6.1; 7] |
| DPIA | Vrijwel zeker nodig zodra veiling- of schuldenaarsgegevens met persoonsgegevens worden gekoppeld (criteria 4, 8, 10; criterium 11 bij beroep op art. 14.5.b AVG) | Beoordeling advocaat | [B82; 2] [R16-verificatie F-2] |

**6.7 Menselijke opvolging, juridisch en stedenbouwkundig onderzoek (§28)**

Masterprompt §28 vraagt naast software ook juridisch onderzoek, stedenbouwkundige controle en menselijke opvolging te begroten. Die posten zijn hieronder apart gezet. Aantallen en frequenties komen uit de deliverables; de **tijd per handeling is een werkhypothese** (WU-1 t/m WU-6, nergens gemeten en uit geen bron), dus de uren zijn een berekening op benoemde aannames (bewijstype 5) met status ONBEKEND tot de meting in B6.

**Werkhypothesen tijd per handeling** (door Jan te bevestigen of te vervangen door meting): WU-1 één handmatige kanaalcontrole 5–15 min · WU-2 één Idealista-sessie met vier zoekopdrachten 20–40 min · WU-3 invoer van één advertentie of vergelijkingsobject 5–10 min · WU-4 detailcontrole van één veilingsignaal op het portaal 15–30 min · WU-5 eerste bureauoordeel over één partneraanlevering 30–60 min · WU-6 ochtendrapport lezen en besluiten op de reviewpagina 10–20 min per werkdag.

| Handwerk | Frequentie en aantal (bron) | Wie | Raming per week (type 5 op WU) |
|---|---|---|---|
| M7 wekelijkse checklist: TGSS-portaal en tablón, tablón Xàbia, BOP Alicante, subastasprocuradores.com, eActivos | 5 kanalen per week [D04 §2.9] | Medewerker of Jan | 25–75 min (WU-1) |
| M7 maandelijks: GVA-patrimonium, SUMA adjudicación directa | 2 kanalen per maand [D04 §2.9] | idem | 2–7 min (WU-1, gemiddeld per week) |
| M8 bank en servicers: Idealista-assistent "de bancos" | 4 zoekopdrachten per week [D04 §2.9] | idem | 20–40 min (WU-2) |
| M8 kwartaalronde: Unicaja, Cimenta2, EscogeCasa, Bankinter, Altamira, Hipoges, Facilitea, Sareb | 8 kanalen per kwartaal [D04 §2.9] | idem | 3–9 min (WU-1, gemiddeld per week) |
| Ochtendrapport en reviewpagina | 5 werkdagen | Jan | 50–100 min (WU-6) |
| **Vast totaal** | | | **circa 100–230 min = 1,7–3,9 uur per week** |
| M5 portaal- en servicer-alerts lezen | Per e-mail; volume ONBEKEND [D04 §2.9] | Jan | ONBEKEND |
| M6 detailcontrole per veilingsignaal | Binnen 1 werkdag na signaal; 0 signalen in Xàbia/Dénia op 14 en 15-09-2026, geen basisfrequentie [D04 §2.3, §2.9] | Jan of medewerker | 15–30 min per signaal (WU-4) × aantal ONBEKEND |
| Handmatige Idealista-invoer en vergelijkingsobjecten | Per interessante advertentie; minimaal 6 vergelijkingsobjecten per waardeblad (§3.7) | Medewerker | 5–10 min per stuk (WU-3); per waardeblad dus 30–60 min × aantal dossiers ONBEKEND |
| Partneraanleveringen | Ontvangst ≤ 1 werkdag, oordeel ≤ 5, besluit ≤ 10 werkdagen, terugkoppeling per 2 weken [R07 §5.3] | Kantoor, Jan en bouwkundige | 30–60 min per aanlevering (WU-5) × aantal ONBEKEND |
| Beheer en onderhoud van de software | Maandelijks [R17 §9.2; 4] | Bouwer | 4–8 uur per maand (circa 0,9–1,8 uur per week) |

**Juridisch en stedenbouwkundig onderzoek per dossier** (alleen voor dossiers die de betreffende poort bereiken; elke uitgave is een A3-approval van Jan)

| Post | Wanneer | Bedrag of tijd | Bron |
|---|---|---|---|
| Nota simple | Poort 1, per finca (bij twee kandidaat-percelen twee) | 9,02 € + btw per finca; levertijd tegenstrijdig (< 2 uur of 24 uur) | [B69; 2] [R17 §11a.2; 5] |
| Informe urbanístico of cédula | Poort 2 | Tasa ONBEKEND; wettelijke termijn 1 maand; tijd van architect of Jan ONBEKEND | [D03 stap 12; 2] |
| Architect (interpretaties A1–A9, bouwmogelijkhedenoverzicht, scenario's) | Poort 3 | ONBEKEND, offerte | [B95; 2] [D03 §5.3] |
| Advocaat: eenmalig rechtenadvies (R16 §7) | Vóór B3 en vóór fase C (zie Concrete vervolgstap) | ONBEKEND, offerte | [R16 §7; 4] |
| Advocaat per veilingdossier (deliverable 04 §7) of due diligence | Vóór elk biedingsvoorstel | ONBEKEND, offerte | [D04 §7; 4] |
| Gestor (fiscale toets) | Per deal met onduidelijk belastingregime | ONBEKEND | [D03 §2.6 K08; 4] |
| Topograaf, geotechniek | Na poort 2, bij hellende of risicovolle percelen | ONBEKEND | [D03 §2.6 K07; 4] |
| Tinsa Radar | Per serieus dossier, optioneel | 29 € per studie (btw ONBEKEND) | [B114; 1] |

**Plan om offertes te verkrijgen** (⏸️ ACTIE VOOR JAN; niets wordt verstuurd zonder zijn "ja"; geen bedragen vooraf ingevuld)

1. **Spaanse advocaat (vastgoed, urbanismo en gegevensbescherming):** één vaste vragenlijst met de twaalf vragen uit R16 §7, de vaste punten per veilingdossier uit deliverable 04 §7 en de DPIA-vraag. Vraag om: prijs voor het eenmalige rechtenadvies, prijs of tarief per veilingdossier en per due diligence, en levertijd. Nodig vóór B3.
2. **Lokale architect:** vragen A1–A9 uit deliverable 03 §5.3, plus de prijs voor één bouwmogelijkhedenoverzicht per perceel en voor het voorbereiden van een informe-aanvraag. Deliverable 03 stelt voor de doorlooptijd van een licentie bij 2–3 lokale architecten na te vragen (W6); dezelfde ronde kan de offertes opleveren. Nodig vóór het eerste perceel dat poort 1 haalt (waarschijnlijk K07).
3. **Gestor:** prijs per fiscale toets (ITP tegenover btw + AJD, afstand van vrijstelling). Nodig vóór de eerste voorwaardelijke prijsanalyse die Jan wil gebruiken.
4. **Topograaf en geotechniek:** pas bij een concreet perceel na poort 2.
5. **Datalicenties:** de offerteronde uit deliverable 02 §6-C (DataVenues, idealista/data, Casafari, Accumin, Brainsre), met één vaste vragenlijst; relevant voor fase D.
6. Offertes en uren komen als parameters in `parameters-2026.yaml` (waarde, bron, datum, bewijstype), zodat "kosten per gekwalificeerde kans" (§28) meetbaar wordt.

**6.8 Acceptatietests** (masterprompt §28 plus de lessen uit de tegenspraak; testdata met prefix `TEST-` in `data/test.db`)

| # | Test | Fixture of stap | Verwacht | Fase |
|---|---|---|---|---|
| T01 | Dubbele advertenties | BP-object met gewijzigde `ref` maar zelfde `id`; handmatig ingevoerde Idealista-advertentie met zelfde prijs en m²; twee advertenties van één huis met 269 en 239 m² | Eén object bij gelijke `id`; bij feitenmatch alleen "kandidaat, menselijke controle"; beide prijzen en oppervlakten zichtbaar; geen dHash | B |
| T02 | Onjuiste locatiepinnen | BP-coördinaat 25.68654 / −80.431345 (Miami); pin die in geen enkel perceel valt | Locatie ONBEKEND; perceelkoppeling LAAG; rapport "locatie te controleren" | B |
| T03 | Oppervlaktebegrippen | Veld 1.100 m², tekst 1.064 m², Catastro 1.060 m² | Alle drie apart opgeslagen met bron; geen overschrijving | B |
| T04 | Herpublicaties | Object verdwijnt en keert terug met nieuwe `id` en dezelfde kenmerken | OPNIEUW AANGEBODEN als kandidaat; oorspronkelijke `first_seen_at` blijft | B |
| T05 | Lege of onvolledige feeds | Lokale API: totaal 0; `errors` niet leeg (één export HTTP 500); krimp > 30 %; `lastFetch` vers maar met fouten | Run failed of partial; geen gebeurtenissen; geen NIET MEER GEVONDEN; alarm na 2× | B |
| T06 | Verdwenen advertenties | Afwezig in één geldige run; daarna in twee geldige runs op verschillende dagen | Eerst niets; daarna NIET MEER GEVONDEN, nooit "verkocht" | B |
| T07 | Renders | Tekst "imagen generada por IA" of een beeld met rendervermoeden | Label "render vermoed"; mens bevestigt; geen automatische conclusie | B |
| T08 | Grondprijs met voorbeeldwoning | "parcela + proyecto" tegenover "solo terreno" | `price_scope` grond / grond+bouw / onbekend; €/m² alleen op grond | B |
| T09 | Verkeerde perceelkoppelingen | Verborgen adres met twee plausibele percelen op 129 m; RC in tekst met oppervlakteverschil; pin 2,1 m van de grens | Hoogstens MIDDEL of LAAG; RC uit tekst niet HOOG; vaste zin "Bouwmogelijkheden nog niet betrouwbaar te bepalen" | B |
| T10a | Plannen en pins: K07 | Opgenomen GVA-antwoorden van 15-09-2026: Idealista-pin 38,7936151 / 0,1214097 → PP "ERMITA II", SUZ, ZND-RE; BP-pin 38,794232 / 0,119842 → twee vlakken (PP Ermita II én "Plan general SU ZUR-RE"); inventarislaag → "Plan Parcial Montgó-2 / SUP Montgó-2"; zekerheid perceelkoppeling MIDDEL | Planfilter draait niet op een pin maar alleen op de perceelpolygoon; klasse bewijstype 7 "tegenstrijdig"; geen parameters en geen bouwvolume; vaste zin "Bouwmogelijkheden nog niet betrouwbaar te bepalen" | B |
| T10b | Plannen en pins: Villes del Vent | BP 4603JAV-pin → PP Cansalades-Umbría (SUZ); Idealista 111295146-pin (118 m verderop) → SNU-P ZRP-NA-MU | Geen planklasse uit een pin; "perceelidentificatie ontbreekt"; klasse bewijstype 7 | B |
| T10c | Vernietigd plan | Perceelpolygoon die een vlak "HOMOLOGACIÓN MODIFICATIVA… PORTITXOL" raakt (20 vlakken in de laag; vernietigd door TSJCV 459/2012) | Documentstatus "vernietigd" → "geen geldend recht"; onherroepelijkheid gemarkeerd als [te verifiëren] | B |
| T10d | Plan in procedure en status onbekend | Regel uit het PGE-voorstel 2019 (in procedure) en uit de NUT 2021 (bewijstype 7) | PGE: "geen geldend recht", alleen risico-informatie; NUT: "alleen na schriftelijke bevestiging"; geen bouwvolume op basis van een van beide | B |
| T10e | Eén object, twee planklassen uit twee kanalen | K10 = Sareb-perceel A: Idealista 107655781 en 111869151 ("Terreno urbanizable") tegenover Servihabitat Profesionales ("urbano no consolidado", "PGOU UA BALCON AL MAR 1"); pakket van 16 fincas, één prijs | Eén object met drie advertenties onder een pakket; klasse bewijstype 7; geen bouwvolume; scenario S0 tot programa en klasse schriftelijk vastliggen; waarde van het geheel, niet per finca | B |
| T11 | Beperkte eigendomsrechten | AEAT-lot "25% PLENO DOMINIO"; `derecho` blote eigendom 50 % | Harde blokkade; aangeboden recht zichtbaar | B |
| T12 | Onbekende lasten | Lasten onbekend of certificación ouder dan 6 maanden | Blokkade; taak "nota simple" met A3-approval | B |
| T13 | Gewijzigde of ingetrokken veilingen | Item verdwijnt uit `bienes.js`; teksthash wijzigt; BOE-sumario 404 vóór publicatie | STATUS of DOCUMENTEN GEWIJZIGD; deadlinemelding ingetrokken; 404 vóór publicatietijd is geen uitval | B |
| T14 | Plaatsnaamvarianten | Javea, Jávea, Xàbia, JAVEA/XABIA, Jávea/Xàbia, en "Xabiá" | Eerste vijf één gemeente-id; zesde "onbekende plaats" in het rapport | B |
| T15 | Kill-switch | `LOCKDOWN`-marker in testomgeving | Run stopt vóór netwerk, AI en bezorging; auditregel | B |
| T16 | Kostenplafond | Gesimuleerd tokengebruik boven het runbudget | AI-stap stopt, run partial, alarm; boeking in euro | B |
| T17 | Geheimen | Zoeken op sleutelpatronen in logs, rapporten en database-dump | Nul treffers | B |
| T18 | Back-up en herstel | Back-up terugzetten in `test.db` | Zelfde aantallen objecten en gebeurtenissen | B (hersteltest C) |
| T19 | Rechtenpoort | Bron met `storage=unknown` (BP vóór akkoord) | Adapter weigert opslag; alleen tellingen gelogd | B |
| T20 | Persoonsgegevensfilter | `userType=private` met telefoon in tekst; BOE-tekst met naam | Contactvelden en namen niet opgeslagen | B |
| T21 | Catastro-discipline | Zelfde RC twee keer; WFS-kop 486 bij 477 objecten | Tweede keer uit cache; telling op werkelijk ontvangen objecten | B |
| T22 | Deadlinecalculator | Gerechtelijk, AEAT, SUMA, notarieel, TGSS | Regels uit de tabel in 3.5; geen verlenging bij gerechtelijk | B |
| T23 | Bezorging | Rapport naar het gekozen kanaal | Zichtbaar ontvangen (niet alleen HTTP 202) | C |
| T24 | Lege dag | Geen kandidaten; één bron gefaald | "Geen sterke kansen vandaag" en apart "geen nieuwe gegevens van <bron> sinds <tijd>" | B |
| T25 | Waardering zonder transacties | Waardeblad met (a) vijf vergelijkingsobjecten, (b) acht objecten waarvan twee dubbel, (c) acht unieke objecten zonder rendementseis van Jan | (a) "steekproef te klein", geen basisscenario, geen koopprijs; (b) na ontdubbelen zes objecten, bandbreedte met label "vraagprijzen, geen transacties"; (c) bandbreedte wel, maximale koopprijs "niet te bepalen: rendementseis ontbreekt"; met eis: "voorwaardelijke prijsanalyse" met zichtbare voorwaarden | B |
| T26 | Partneraanlevering zonder contactgegevens | Aanlevering met bedrijfsnaam, contactpersoon, telefoon, e-mail, mandaat "gedeeld", veld 18 "al op Idealista", adres | Op de reviewpagina alleen bedrijfsnaam, verwijzing GHL, rol, mandaat (type 1) en objectvelden; persoonsnaam, telefoon en e-mail niet opgeslagen; dedupe tegen bestaande advertenties; taken met deadlines 1, 5 en 10 werkdagen; geen verzendactie | B |
| T27 | Sectorale lagen en dienststatus | MITECO-kustdienst geeft een fout; PATIVEL-lagen 30–32 (lijnen) op een punt; PATRICOVA-antwoord "geen zone" | Kust: "dienst onbereikbaar; ONBEKEND" en BRON NIET BEREIKBAAR voor die laag; PATIVEL-lijnen via afstand, niet via punt-in-polygoon; PATRICOVA: "geen signaal in laag X op datum", nooit "geen beperking" | B |

**6.9 Meetwaarden (§28)**, bijgehouden op de reviewpagina vanaf fase B: brondekking per bron per dag; verwerkingsvertraging (einde run min brontijd); dedupe-juistheid (steekproef door Jan); kwaliteit perceelkoppelingen (aandeel HOOG dat bij nota simple klopt); bruikbaarheid (interessant tegenover afgewezen, met reden); foutieve signalen; onderzoekstijd per bruikbare deal (inclusief de gemeten tijd per handmatige ronde, ter vervanging van WU-1 t/m WU-6); kosten per gekwalificeerde kans (inclusief nota's, tasas en offertes); commerciële uitkomst per bron en per partner.

---

### Deel 7 — Wat níet geclaimd wordt

| Claim die we níet doen | Waarom | Bron |
|---|---|---|
| "Realtime" | BP maakte de exports in één nachtelijk venster (één nacht gemeten), dus een wijziging kan tot circa 26 uur later zichtbaar zijn. BOE verschijnt dagelijks. Het Catastro-ATOM wordt twee keer per jaar ververst. Idealista is handwerk. | [B24; 3] [R05 §4.1; 5] [B65; 2] |
| "100 % van de markt" of "heel Jávea" | BP is een netwerk: 56 objecten in "Javea". Idealista is één portaal. Andere portalen en off-market routes zijn niet aangesloten; makelaars leveren alleen handmatig aan (§3.6). | [L1; 3] [L9; 3] [B34; 3] |
| "Monitoring actief" | Pas als koppeling, opslag, planning, bezorging en controles zijn ingesteld én getest (T23 en 30 dagen zonder stille storing). Vandaag draait er niets. | [MP §27] |
| "Verkocht" | Een verdwenen advertentie is "niet meer gevonden"; geen van de fase B-bronnen meldt verkoop | [B23; 2] |
| "Bouwrijp perceel" of "bouwrecht" | Catastro bewijst geen eigendom of bouwrecht; "urbanizable" is niet bouwrijp; zonder geldend plan geen conclusie | [R11 §2.3; 3] [B34; 3] |
| "Biedadvies" | Zonder juridische beoordeling (bewijstype 6) geen advies; veilingwaarde ≠ marktwaarde; eerdere lasten kunnen blijven bestaan | [B47; 2] [MP §19] |
| "Kans op winst" | Labels en blokkades zijn heuristisch, geen statistisch bewezen kans | [MP §23] |
| "Marktwaarde" of een onvoorwaardelijke "maximale koopprijs" | De bandbreedte rust op vraagprijzen, niet op transacties; een verdwenen advertentie bewijst geen transactieprijs | [MP §20, §22] [B115; 2] [B116; 2] |
| "Geen beperking" of "bouwrijp" op basis van kaartlagen | De GVA-planlaag is "carácter informativo"; PATIVEL-ámbitos zijn lijnen; de brandinterface is een raster van ±500 m; de kustdienst was onbereikbaar. "Geen signaal gevonden" is iets anders dan "geen beperking aanwezig" | [D03 §4; 3] [MP §17] |
| "Partner" of "exclusief aanbod" | Geen samenwerking, mandaat of exclusiviteit zonder schriftelijke bevestiging | [MP §9] |
| "AI herkent renders" | Volgens de aanbieder zelf niet betrouwbaar | [B08; 2] |
| "Toegestaan" voor zaken met [advocaat] | Handmatige invoer van Idealista-feiten en vergelijkingsobjecten, links aan klanten, inlezen van alertmails, beeldhashes: nog juridisch te toetsen | [R16 §7; 4] |

---

## Aannames en onzekerheden

| # | Werkhypothese | Bewijstype | Wat haar bevestigt of weerlegt |
|---|---|---|---|
| 1 | BP geeft binnen fase B schriftelijk akkoord voor opslag, historie en AI-analyse | 7 | Antwoord van BP |
| 2 | Handmatig en ad hoc gebruik van de Idealista-assistent door een medewerker, met opslag van alleen link, code, enkele feiten en eigen oordeel, is verdedigbaar | 4 | Advocaat (R16 §7 vragen 2 en 3) |
| 3 | Laagvolume geautomatiseerd gebruik van de vrije Catastro-webservices valt binnen de voorwaarden; de verzoekdrempel is onbekend | 4 | Uitdrukkelijke bevestiging DG Catastro bij opschaling |
| 4 | BP maakt zijn exports elke nacht (één nacht gemeten) | 4 | Tweede meting op een andere dag, of BP |
| 5 | Het BOE-sumario verschijnt in de ochtend; het exacte tijdstip is onbekend | 7 | Meting in de eerste proefweek |
| 6 | SQLite volstaat voor Jávea-schaal | 4 | Groei boven circa 50.000 snapshots of gelijktijdig schrijven |
| 7 | De Hermes-venv blijft na updates compatibel | 4 | Test na elke Hermes-update |
| 8 | Ontwikkelinzet 60–90 u (B) en 80–120 u (C) | 4 | Werkelijke uren in B0–B2 |
| 9 | AI-kosten < $10 per maand (USD) bij Jávea-volume | 5 | Werkelijk gebruik; OpenRouter-prijzen kunnen afwijken; R17 schrijft in zijn samenvatting "< €10" |
| 10 | De GVA/ICV-diensten blijven bereikbaar en beantwoorden een bbox in EPSG:25830 zoals op 15-09-2026; de laagkeuze uit deliverable 03 blijft juist | 4 | Regressietest in B2; wijziging in GetCapabilities |
| 11 | Automatisch inloggen van de Mac is hersteld of wordt hersteld (stand 25-08-2026: werkte niet) | 7 | Vuurproef 3 (~/CLAUDE.md) |
| 12 | Een reviewpagina met onderzoeksstatus, partnerstatus en partneraanleveringen, zonder contacten, is geen "tweede CRM" in de zin van ADR-0014 | 4 | Besluit van Jan |
| 13 | Handmatig vergeleken vraagprijzen (minimaal zes, ontdubbeld, zelfde microlocatie) geven een bruikbare, voorzichtige bandbreedte voor een voorwaardelijke prijsanalyse | 4 | Vergelijking met latere transacties, een Tinsa-studie of een gelicentieerde comparablesbron (fase D) |
| 14 | Tijd per handeling WU-1 t/m WU-6 (§6.7) | 4 | Meting in B6 |
| 15 | K10 (Idealista 107655781) en Sareb-perceel A (Idealista 111869151, Servihabitat 06124187) zijn één object | 4 | Referencias catastrales van de 16 fincas via aanbieder of nota simple |
| 16 | Overlap perceelpolygoon ↔ zonevlak is in variant 1 te bouwen zonder bibliotheek | 4 | Regressietest in B2; anders tussenstap geometriebibliotheek (Deel 4) |

---

## Tegenargumenten of aandachtspunten

1. **Is fase B zinvol als BP niet of laat antwoordt?** Dan levert module A alleen handmatige Idealista-invoer op, en de automatische objectstroom is dun. Tegenwicht: modules B en C hebben geen rechtenblokkade, en de bouwvolgorde zet ze vooraan. Zo is er ook zonder BP een werkende keten.
2. **De veilingmodule levert in Xàbia misschien weinig op:** 0 veilingen op 14 en 15-09-2026, en ook geen enkele van de rechtbank van Dénia. De masterprompt verbiedt de module stil te laten verdwijnen (§29). Houd haar klein: BOE en AEAT ophalen kost weinig, en lokaliseren gebeurt via Jans portaalmeldingen.
3. **Idealista-voorwaarden:** gebruiksrecht "estrictamente personal y privado" en een verbod op "monitorizar" voor commerciële doeleinden. Ook ad-hocgebruik voor acquisitie is dus niet zonder risico [B31; 2]. Daarom staat de toestemmingsvraag hoog in de actielijst.
4. **Links naar Idealista-advertenties aan klanten** botsen met de letterlijke tekst van de voorwaarden van 2020 ("Establecer un enlace a cualquier contenido") [R16-verificatie N-2; 2]. Dossiers voor derden dus zonder portaallinks, tot de advocaat anders adviseert.
5. **De bevoegdheden-engine is intern tegenstrijdig met AI-kosten:** elke betaalde aanroep wordt A3 [B03; 3]. Oplossing: Jan neemt vooraf een maandbudgetbesluit, en AI-aanroepen binnen dat budget blijven buiten `evaluate`. Leg dat vast als governance-uitzondering, of registreer de actor DEAL-HUNTER. Beide raken de governance-repo: dat is een besluit van Jan.
6. **Gedeelde Hermes-venv:** snel en zonder installaties, maar kwetsbaar bij updates. Tegenwicht: vastgelegde pakketversies en tests na elke update; een eigen venv vraagt downloads en dus akkoord.
7. **De feeddienst heeft zelf gebreken** (geen krimpbescherming, `pool`-filterfout, eerste ronde na herstart mislukt). Deal Hunter vangt dat af, maar repareert niets aan een productiedienst. Of de dienst wordt aangepast, is een apart overleg met Jan.
8. **Geheimen:** de BP-sleutels staan hardgecodeerd in `feeds.js` (rechten 644, geen git) [R05-verificatie punt 10; 3]. Deal Hunter voegt in fase B geen extra sleutelplek toe: hij leest via de lokale API. Of de sleutel moet worden vervangen, hoort in de BP-mail (vraag 11 in R05).
9. **Merk:** dit is een TREE-project. Koopt Rocksure, dan krijgt elke actie een apart merk-envelop; de engine blokkeert vermenging [B03; 3]. De keuze bepaalt ook wie in het BP-akkoord en in een DPIA wordt genoemd.
10. **Machine:** alle launchd-taken starten pas na inloggen. Zolang automatisch inloggen niet werkt (stand 25-08-2026), overleeft geen enkele planning een stroomuitval [L6; 3].
11. **Waardering blijft de zwakke schakel.** Zolang er alleen vraagprijzen zijn, valt een "voorwaardelijke" koopprijs te hoog uit als de werkelijke verkoopprijzen onder de vraagprijzen liggen; of en hoeveel dat in Jávea zo is, is ONBEKEND. Tegenwicht: altijd het conservatieve scenario, de gevoeligheid voor −10 % opbrengst, en bij een serieus dossier een tweede mening (een Tinsa Radar-studie vermeldt volgens de aanbieder ook een onderhandelingsmarge [B114; 1], of een taxatie). Een betaalde comparablesbron is een fase D-besluit.
12. **De kaartlagen kunnen een deal ten onrechte afwijzen of doorlaten.** Een pin 118–177 m naast het perceel gaf in de tests een andere planklasse; daarom draait de toets alleen op de perceelpolygoon, en is de uitkomst altijd een signaal. Bouwrecht komt pas uit poort 2 en 3 [R12-verificatie A2; 3].
13. **Partnerdealflow kost vooral menselijke tijd en vertrouwen.** De opvolgtermijnen (1, 5 en 10 werkdagen) zijn een belofte aan partners; wie ze niet haalt, verliest de stroom. En commerciële e-mail aan kantoren vraagt voorafgaande toestemming (LSSI art. 21), dus de eerste benadering loopt via een route die Jan en de advocaat kiezen [R16 §4.7; 2/4].

---

## Concrete vervolgstap

**Deze week, zonder blokkade:** B0 (fundament met tests, fixtures, `rechten.yaml` uit het register, waarin de kaartlagen sinds 15-09-2026 staan) en B1 (veilingmodule op BOE en AEAT) bouwen in variant 1, zodra Jan vraag 3 met ja beantwoordt. Direct daarna B2 (perceelmodule met Catastro, planfilter, sectorale lagen en regeltabel), omdat ook die geen rechtenblokkade heeft. Parallel: de conceptmail en -clausule voor BP laten toetsen, en de offerteronde voor advocaat en architect voorbereiden (§6.7). De drie vragen staan bovenaan onder "Conclusie".

**Volgorde advocaat en bouw (tegenstrijdigheid opgelost).** Een eerdere versie van deliverable 02 §6-A punt 7 zette alle twaalf advocaatvragen uit R16 §7 "vóór de bouw van fase B"; 02 zegt nu hetzelfde als dit plan (open overheidsdata zonder persoonsgegevens mag starten; portaal- en BP-opslag en persoonsgegevens wachten op de advocaat). R16 zelf, de primaire analyse, koppelt aan de bouw alleen drie regels: geen dHash op Idealista-foto's, geen opslag van ruwe portaaldata, en BP-snapshots pas na schriftelijke bevestiging [R16 §1; 4]. Deliverable 04 §2.10 stelt daarnaast dat een module die alleen objectvelden verwerkt, kan starten met een vastgelegde afweging waarom nog geen DPIA nodig is [D04 §2.10 punt 8; 2/4]. Dit plan volgt R16 en koppelt elke vraag aan de bouwstap die ervan afhangt:

| Advocaatvraag (R16 §7) | Onderwerp | Nodig vóór |
|---|---|---|
| geen | Open overheidsdata en kaartlagen, alleen objectvelden, geen persoonsgegevens | B0, B1 en B2 kunnen starten (met vastgelegde DPIA-afweging) |
| 1, 2, 3 | Binding van portaalvoorwaarden; handmatig noteren van enkele feiten; gepland gebruik van de assistent | B3 (Idealista-invoer) en B4 (vergelijkingsobjecten in het waardeblad) |
| 12 | Conceptclausule BP | Versturen van de BP-mail; BP-opslag in B3 |
| 4 | Inlezen van eigen alertmails | Fase C |
| 5, 6 | TDM-voorbehoud; beeldhashes | Niet in fase B (geen AI op portaalteksten buiten de sessie, geen dHash) |
| 7 | Links en eigen analyse naar klanten | Eerste dossier voor een derde (route D) |
| 8, 9 | Contact met particuliere adverteerders | Elk bericht aan een particulier |
| 10, 11 | Namen in biedingsdossiers; DPIA voor de veilingmodule | Afgeschermd dossierdeel met persoonsgegevens; eerste biedingsvoorstel |
| (R16 §4.7) | Eerste commerciële benadering van makelaarskantoren | Eerste partnerbericht (route D) |

### Deel 8 — ⏸️ ACTIE VOOR JAN (gerangschikt op wat het eerst nodig is)

Dit is de werklijst, geen losse vragenronde: wat nu aan Jan wordt gevraagd, staat in de geconsolideerde top-3 in deliverable 01 §1.2.

| # | Actie | Blokkeert | Nodig vóór | Bron |
|---|---|---|---|---|
| 1 | **Akkoord variant 1** en het gebruik van de Hermes-venv; bestanden in `~/tree-es/deal-hunter/`; automatisch gebruik per kandidaat en in laag volume van de open Catastro- en GVA/ICV-diensten als eerste filter | Start van alle bouw; perceelmodule | B0 / B2 | Deel 4 [D03 besluit 3] |
| 2 | **AI-budget en sleutel:** eigen Anthropic-sleutel of OpenRouter; maandplafond in euro; governance-uitzondering of registratie van actor DEAL-HUNTER | AI-stappen (BP-analyse) en kostenbewaking | B3 | [B03; 3] [B07; 2] |
| 3 | **Spaanse advocaat aanwijzen en offerte vragen** (vragenlijst §6.7); vragen beantwoorden in de volgorde van de tabel onder "Concrete vervolgstap" | Handmatige Idealista-invoer, vergelijkingsobjecten, BP-clausule, alertmails, klantdossiers, DPIA | B3 / C | [R16 §7; 4] |
| 4 | **Background Properties:** mail (R05 §6.4) en clausule (R16 §6.4) laten toetsen door de advocaat, aanspreekpunt invullen, versturen; nagaan wat destijds is afgesproken | Module A: opslag, historie, AI, BP-foto's | B3 | [B20; 2] |
| 5 | **Investeringskader en entiteit:** budget, rendementseis (op kosten, op eigen vermogen of als marge), maximale doorlooptijd, TREE of Rocksure; eventueel een vaste korting van vraagprijs naar verwachte verkoopprijs voor het conservatieve scenario | Rekenmodule, voorwaardelijke prijsanalyse, beoordeling, prijsklassen in het zoekprofiel | B4 | [R14 §6; 7] [R07 §5.1; 4] |
| 6 | **Lokale architect aanwijzen** (vragen A1–A9, offerte per bouwmogelijkhedenoverzicht; licentiedoorlooptijd bij 2–3 architecten navragen) en een **gestor** voor de fiscale toets | Poorten 2 en 3; fiscale variant in de prijsanalyse | B2 / B4 | [D03 §5.3, W6; 4] |
| 7 | **Veilingportaal:** registreren als natuurlijk persoon, de gebruiksvoorwaarden zelf lezen en accepteren, tot 50 meldingen instellen (Xàbia, Jávea, Javea, 03730/03737/03738 [volledigheid postcodes te verifiëren], Dénia en buurgemeenten) | Lokaliseren van gerechtelijke veilingen | B1 | [B41; 2] |
| 8 | **Idealista:** (a) Search API aanvragen via het formulier met een eerlijke projectbeschrijving; (b) schriftelijk vragen of gepland gebruik van de assistent mag; (c) opgeslagen zoekopdrachten met alerts instellen (toegestaan) | Elke automatisering rond Idealista | D (a, b) / B (c) | [B30; 2] [B32; 2] |
| 9 | **Waardering:** besluiten of per serieus dossier een Tinsa Radar-studie (29 €, btw ONBEKEND) mag worden afgenomen; akkoord op de regel "minimaal zes vergelijkingsobjecten" | Tweede mening in het waardeblad | B4 | [B114; 1] [B118; 2] |
| 10 | **Partnerdealflow:** prijsklassen in het zoekprofiel bevestigen; beslissen of het aanleverformulier in GHL komt; RAICV-nummer van TREE Properties nagaan; eerste ring van kantoren kiezen (geen bericht zonder "ja") | Route C/D, partnerregister | B5 / C | [R07 §5; 4] [R06 §8; 4] [D01 besluit 2] |
| 11 | **Nacalculaties:** 3–5 projecten uit de Excel-administratie (PEM en aanneemsom per m², excl. btw, met jaar); beslissen over IVE-BDC (69,99 €/jaar) | Kostenbandbreedtes in dossiers | B4 | [B97; 1] |
| 12 | **Catastro en Registro:** met Cl@ve één keer de valor de referencia proberen; bij het eerste bevestigde dossier één proefbestelling nota simple (betaling door Jan) | Fiscale grondslag; werkelijke prijs en levertijd nota simple | B2 / B4 | [B68; 3] [B69; 2] |
| 13 | **Xàbia Gestió Tributària:** ordenanzas IIVTNU en tasas 2026 opvragen, inclusief de tasas voor informe urbanístico, cédula en licentie (IBI 0,83 % en ICIO 4 % zijn al bekend) | Plusvalía en poortkosten in het rekenmodel | B4 | [B93; 2] [D03 stap 12] |
| 14 | **Ochtendrapport:** tijdstip (optie a, b of c) en kanaal kiezen | Productieschema | C | Deel 5 |
| 15 | **Hermes:** laten uitzoeken waarom alle drie de G-CEO-cronjobs op `blocked_config` staan, of voor een rechtstreeks kanaal kiezen | Bezorging via Hermes | C | [L3; 3] |
| 16 | **Machine:** automatisch inloggen herstellen en vuurproef 3 draaien; 2 TB USB-SSD aansluiten voor back-ups | Planning na stroomuitval; back-up buiten de Mac | C | [L6; 3] |
| 17 | **Git-remote** voor Deal Hunter ja/nee (zonder remote bestaat de code alleen op deze Mac) | Continuïteit | C | [L6; 3] |
| 18 | **GoHighLevel:** nagaan of TREE agency-toegang heeft of het schema handmatig aanmaken; sub-account-token met `objects/record.*`; controleren of het abonnement custom objects bevat; ADR-0014-interpretatie bevestigen (onderzoeks- en partnerstatus in de reviewpagina, contacten en commerciële status in GHL) | CRM-koppeling, partnerformulier | C | [B10; 2] [B11; 2] |
| 19 | **Feeddienst:** besluiten of `properties-api` krimpbescherming, een DNS-wachtlus en een correct `pool`-filter krijgt (raakt een productiedienst) | Alleen robuustheid | C | [B01; 3] |
| 20 | **Installatie-akkoord geometriebibliotheek of variant 2**, alleen bij het overstapmoment (Deel 4) | Buffers, onregelmatige bouwvlakken, sweeps | B2 (bij behoefte) / D | [B12; 2] [B14; 2] [D03 W8] |
| 21 | **Claude CLI updaten** (≥ 2.1.259), alleen als Idealista de headless route toestaat | Headless Idealista-route | D | [B09; 2] |

---

## Verwerkte correcties uit de tegenspraak

| Onderwerp | Stond in het onderzoeksrapport | In dit plan gebruikt | Bron |
|---|---|---|---|
| BP `pool` | "altijd leeg" (R17) | Vrije tekst bij 222 van 224; normaliseren; API-filter onbruikbaar | R17-verificatie F1 |
| BP `date` | basis voor NIEUW GEPUBLICEERD (R17) | `source_modified_at`; nooit NIEUW GEPUBLICEERD | [B22; 2] |
| Versheid feeddienst | `lastFetch` vers = goed (R17) | `errors` leeg + krimpdrempel; `lastFetch` geen bewijs | R17-verificatie A3, F7 |
| GHL-limieten | ONBEKEND (R17) | 100 per 10 s, 200.000 per dag per app; schema via Agency-token | [B10; 2] [B11; 2] |
| Kostenplafond | "OS-plafond leidend" (R17) | Niet afgedwongen; zelf afdwingen | [B03; 3] |
| AI-analyse | A1/A2 (R17) | Betaalde aanroep = A3; budgetbesluit nodig | [B03; 3] |
| dHash | derde dedupetrap, ook op Idealista (R17) | Niet op portaalfoto's; op BP pas na akkoord en kalibratie (bijsnijden 10 % gaf 20 bits) | [B80; 2] [B15; 2/3] |
| Renders | AI-classificatie als criterium (R17) | Vermoeden, menselijke bevestiging | [B08; 2] |
| PostGIS | "arm64-test met één pull" (R17) | Geen arm64-image; keuze emulatie, eigen build of niet-officieel | [B12; 2] [B13; 1] |
| BOE-lokalisatie | Jávea-filter op V-B-tekst; `url_xml` (R08) | Geen plaats in aankondigingen; `txt.php` in plaats van `xml.php` | R08-verificatie F1, F2 |
| BOE-formaat | alleen XML (R08) | XML en JSON, met Accept-header | [W1; 3] |
| Gerechtelijke veiling | verlenging tot 24 uur (R08) | Onverlengbaar, geheime biedingen | [B47; 2] |
| AEAT | adjudicación directa na veiling (art. 107) (R08) | "La subasta será única"; art. 104 bis | [B48; 2] [B51; 2] |
| Montgó-koppeling | HOOG, advertentietype fout (R11) | LAAG; verborgen adres hoogstens MIDDEL | R11-verificatie R11-07 |
| ATOM Xàbia | EPSG:25830 (R11) | EPSG:25831 | [B65; 3] |
| Catastro-limiet | geen getallen (R11) | Weigering "generalmente 10 días"; limiet op gelijktijdige toegang | [B67; 2] |
| INSPIRE-licentie | niet leesbaar (R11) | Eigen gebruik en getransformeerde producten; geen verspreiding van originelen | [B66; 2] |
| Nota simple | prijs [te verifiëren] (R11) | 9,02 € + btw; levertijd tegenstrijdig | [B69; 2] |
| Idealista robots.txt | `Disallow: /` (R01) | Geen `Disallow: /`; wel taalmappen en fotopagina's geblokkeerd; status steunt op de voorwaarden | [B33; 3] |
| 238 percelen | "bouwrijp" (R01) | "urbano of urbanizable volgens adverteerder" | R01-verificatie F2 |
| Idealista-makelaarsnaam | niet beschikbaar (lokale feiten) | Wel in `property_detail`, niet in `search_properties` | [B34; 3] |
| BP-partners | 45 kantoren (R05) | 41 kantoren; TREE staat er niet in | [B21; 1/3] |
| BP Jávea | 225/57 | 224/56 op 15-09 03:55; telling wisselt per uur | [L1; 3] |
| Btw bij afstand vrijstelling woning | 21 % (R14) | 10 % | [B92; 2] |
| IBI en ICIO Xàbia | ONBEKEND (R14) | 0,83 % en 4 % (2026) | [B93; 2] |
| Honoraria | 10–12 % totaal (R14) | Architect 10–12 % van PEM + ca. 5 % aparejador + 21 % btw (bewijstype 1) | [B98; 1] |

**Tegenstrijdigheden tussen documenten, opgelost in deze herstelronde**

| Onderwerp | Wat de documenten zeggen | Keuze in dit plan en waarom | Bron |
|---|---|---|---|
| Zonering in fase B | Eerdere versie van dit plan: Jan voert zonering per dossier handmatig in; "polygonen snijden" = overstap naar variant 2 (R17 §4.3). Deliverable 03 stap 8 en 10 en deliverable 01 besluit 6: GVA/ICV-lagen automatisch als eerste filter, op de perceelpolygoon | Deliverable 03 gevolgd: live getest door R12/R13 en hun tegenspraak, en masterprompt §29 eist de perceelmodule in fase B. Overstapcriteria herschreven (Deel 4) | [D03 stap 8, 10; 3/4] [R12-verificatie A2; 3] [R13 §11; 4] |
| K10 | Eerdere versie van deliverable 03 §2.6: "urbanizable" zonder programa (art. 226, PP La Guardia-3, scenario S0). Eerdere versie van deliverable 04 §2.3/§2.4.7: Sareb-perceel A, "urbano no consolidado", UA Balcón al Mar 1, btw + AJD, alleen voor professionals. Geen van beide legde de koppeling; na de kritiekronde van 15-09-2026 lezen 01–04 K10 zoals hier | Waarschijnlijk één object (identiteit bewijstype 4): R15 noemt 111869151 als dubbel van K10 (zelfde prijs en m²), R10 koppelt 111869151 aan Servihabitat-promotie 06124187. De planklasse is bewijstype 7 (aanbieders spreken elkaar tegen) tot poort 2; scenario S0 blijft tot het programa vastligt. Opgenomen als pakket en als test T10e | [R15 K10; 1/3] [R15-verificatie R15-09; 3] [R10 §6; 1/3] [R10-verificatie R10-08, A4; 1/3/7] |
| Bankvastgoed Idealista Jávea | Eerdere versie van deliverable 01: "0 de bancos". Deliverables 02 en 04: 0 woningen, 1 bankperceel | Beide juist voor hun deelverzameling: 0 geldt voor woningen (HOME en CHALET), LAND gaf 1 (111869151, waarschijnlijk K10). Alle deliverables noemen nu: 0 woningen en 1 perceel op Idealista; 2 Sareb-percelen bij Servihabitat Profesionales | [R01-verificatie R01-12; 3] [R10-verificatie R10-09; 3] |
| eActivos | Register/deliverable 02: ALLEEN HANDMATIG. Eerdere versie van deliverable 04: "NIET GEBRUIKEN (geautomatiseerd); handmatig mag" | Zelfde inhoud; de status uit het register geldt (ALLEEN HANDMATIG, R2-41) omdat de rechtenpoort daarop leest. Deliverable 04 §2.2 en §2.11 noteren nu ook ALLEEN HANDMATIG | [L8; 3] [D04 §2.11; 1] |
| BP-percelen tegenover Idealista | Eerdere versie van deliverable 01: 24 tegenover 238. Deliverable 02: 24 tegenover 333 | Geen tegenspraak: 333 terrenos in totaal, waarvan 238 met het label urbano of urbanizable. Eén noemer in 01, 02 en 05: 24 BP-objecten van type Land tegenover 333 terrenos (15-09-2026) | [R01-verificatie R01-12; 3] |
| Telefoonnummer uit de Idealista-assistent | Deliverable 02: doorschakelnummer niet bewezen (type 4). Eerdere versie van deliverable 04: "Idealista-doorschakelnummers" als vaststaand (04 §2.10 nu: niet bewezen) | Niet bewezen (R06-verificatie: aanname zonder bron; bij particulieren een gewoon mobiel nummer). Voor het ontwerp maakt het niet uit: geen enkel telefoonnummer wordt opgeslagen | [R06-verificatie R06-15; 4] |
| Advocaat vóór of tijdens de bouw | Eerdere versie van deliverable 02 §6-A punt 7: alle twaalf vragen vóór de bouw van fase B. Eerdere versie van dit plan: B0/B1 deze week, advocaat bij B3/C | R16 gevolgd (primaire analyse): vragen per bouwstap gekoppeld, tabel onder "Concrete vervolgstap". Deliverable 02 §6-A punt 7 en deliverable 01 §1.2 volgen nu dezelfde volgorde | [R16 §1, §7; 4] [D04 §2.10; 2/4] |
| Rechtenregister | Eerdere versie van dit plan: register "niet aanwezig" | Register bestaat: 75 regels (15-09-2026), met machineleesbare rechtenvlaggen en regels voor de kaartlagen (R2-60 t/m R2-69); nog geen adapter die ze leest | [L8; 3] |
| AI-kosten | Eerdere versie van dit plan: "AI < $10"; R17-samenvatting: "AI < €10"; R17 §2.3 en §9.2: USD | "< $10 per maand (USD)", berekening op de aannames van R17 §2.3; plafond door Jan in euro | [R17 §2.3, §9.2; 5] |
| Docker-storing | Eerdere versie: "stopte op 2 en 3 september, waarna vier nachten back-up faalden" (overgenomen uit R17) | Gecontroleerd in de bron: "Docker stopte in de nacht van 2 op 3 september … Vier nachten lang faalde de back-up" (toelichting `waakhond.sh`, 6 september 2026). Niet in de back-uplogs nagerekend | [L7; 3] |
| Veldmapping BP | Alleen in R05 §7; lokale feiten noemen `url` per taal | Mapping opgenomen in §3.8 met eigen telling: de parser kent talen, de feed levert alleen `en` | [L9; 3] [R05-verificatie R05-07; 3] |
| Tijdstempels veilingdossier | Deliverable 04 §2.8 veld 44 zonder `source_modified_at` | Aangevuld in `auction` (§3.5), conform masterprompt §10 | [MP §10] |
| Idealista "para reformar" | 70 renovatie-chalets | Filter heet "Usada / para reformar"; 51 van de 70 noemen renovatie in de tekst, 4 nieuwbouw | [R06-verificatie R06-15; 3] |

---

## Onderzoeksbestanden voor wie dieper wil

- `03-aanpak-percelen.md`: de dertien stappen, regeltabel, bouwmogelijkhedenoverzicht, K07–K11, vragen aan gemeente en architect
- `04-aanpak-veilingen-en-bijzondere-verkopen.md`: veilingdossier (§2.8), veilingmonitor en handmatige rondes (§2.9), persoonsgegevens (§2.10)
- `bronnenregister.json` en `02-bronnenkaart-en-register.md`: statussen per bron, offerteronde datalicenties (§6-C)
- `onderzoek/R12-urbanisme-xabia-plan-en-vergunning.md` en `onderzoek/R13-regionaal-sectoraal-geoportalen.md` met `.verificatie.md`: planlaag, sectorale lagen, endpoints en tests
- `onderzoek/R06-makelaars-javea-register.md` en `onderzoek/R07-netwerken-ontwikkelaars-dealflow.md` met `.verificatie.md`: makelaarsregister, zoekprofiel, aanleverformulier, opvolgprocedure
- `onderzoek/R04-dataleveranciers-mls-statistiek.md`, `onderzoek/R10-banken-servicers-fondsen.md` en `onderzoek/R15-kandidaten-javea-live.md` met `.verificatie.md`: waarderingsbronnen, bankpercelen, kandidaten
- `onderzoek/R17-architectuur-mvp-kosten.md` en `.verificatie.md`: bouwstenen, varianten, adapters, tests, kosten
- `onderzoek/R05-background-properties.md` en `.verificatie.md`: feedanalyse, conceptmail aan BP (§6.4), veldmapping (§7)
- `onderzoek/R01-idealista.md` en `.verificatie.md`: routes, assistent, voorwaarden, Jávea-metingen
- `onderzoek/R08-veilingen-portalen-toegang.md` en `.verificatie.md`: portalen, BOE-kanalen, deadlineregels
- `onderzoek/R11-catastro-registro-perceelidentificatie.md` en `.verificatie.md`: koppelingsketen en live tests
- `onderzoek/R16-rechten-en-compliance.md` en `.verificatie.md`: rechtenmatrix (§6.1), BP-clausule (§6.4), advocaatvragen (§7)
- `onderzoek/R14-financieel-fiscaal-kostenkengetallen.md` en `.verificatie.md`: parameters en rekenmodel (§6)

---

## Bronnenlijst (URL · controledatum · bewijstype)

**Eigen controles op 15-09-2026**

| Id | Bron | URL of pad | Datum | Type |
|---|---|---|---|---|
| L1 | Eigen feeddienst: health, stats (224, `errors: []`), plaatsfilter Javea 56 / Jávea 0 / Xàbia 0 | http://127.0.0.1:3100/api/health · http://127.0.0.1:3100/api/stats · http://127.0.0.1:3100/api/properties?town=Javea&limit=100 | 15-09-2026 03:55 | 3 |
| L2 | Hermes-venv: Python 3.11.15, pakketversies, SQLite 3.50.4 met rtree/fts5, zoneinfo | file:///Users/root-admin/.hermes/hermes-agent/venv | 15-09-2026 | 3 |
| L3 | G-CEO-cronjobs: drie keer `blocked_config` (reeksen 11, 2, 1) | file:///Users/root-admin/.hermes/profiles/g-ceo/cron/jobs.json | 15-09-2026 | 3 |
| L4 | `launchctl list`: properties-api, properties-web en hermes-gateway draaien; ai-os en waakhond laatste exit 1 | lokaal commando | 15-09-2026 | 3 |
| L5 | Kill-switch-marker afwezig | file:///Users/root-admin/.hermes/LOCKDOWN | 15-09-2026 | 3 |
| L6 | Map deal-hunter om 04:50: CLAUDE.md, MASTERPROMPT.md, deliverables 01–05, `bronnenregister.json`, `onderzoek/` (R01–R17 + verificaties, `ih.py`), lege `rapporten/`; geen code, `.git` of `data/`. ~/CLAUDE.md (open punten automatisch inloggen, USB-SSD, remote-loze repo's; stand 25-08/31-08-2026) | file:///Users/root-admin/tree-es/deal-hunter/ · file:///Users/root-admin/CLAUDE.md | 15-09-2026 | 3 |
| L7 | Toelichting in `waakhond.sh`, gedateerd 6 september 2026: Docker stopte in de nacht van 2 op 3 september; vier nachten faalde de back-up (alleen de commentaarkop gelezen) | file:///Users/root-admin/tree-ai-os/scripts/waakhond.sh | 15-09-2026 | 3 |
| L8 | `bronnenregister.json`: 75 regels (R2-01 t/m R2-75); statussen ALLEEN HANDMATIG 39, TECHNISCH ONDERZOEK NODIG 18, CONTRACT OF TOESTEMMING NODIG 14, NIET GEBRUIKEN 4; velden id, name, website, type, coverage, technical_access, fields, media_docs, publish_modify_info, historical_data, refresh, rate_limits, costs, contract_status, allowed_uses, ai_analysis_rights, storage_retention, derived_data_rights, contact_route, last_verified, open_questions, status, plus rechtenvlaggen automated_access, storage, history, ai_analysis, image_hashing, show_to_clients, personal_data en rights_basis, evidence_type, source_urls; GVA/ICV-, IDEE-, IGME- en MITECO-lagen als R2-60 t/m R2-69; eActivos (R2-41) ALLEEN HANDMATIG | file:///Users/root-admin/tree-es/deal-hunter/bronnenregister.json | 15-09-2026 | 3 |
| L9 | Eigen feeddienst om 04:48 CEST: `/api/stats` 224 objecten, "Javea" 56, `errors: []`, lastFetch 02:00:09 UTC; `/api/properties?town=Javea&limit=100` 56 objecten (1 pagina) met veldnamen en vulling zoals in §3.8 | http://127.0.0.1:3100/api/stats · http://127.0.0.1:3100/api/properties?town=Javea&limit=100 | 15-09-2026 04:48 | 3 |
| W1 | BOE-sumario 20260914 met `Accept: application/json`: HTTP 200 | https://www.boe.es/datosabiertos/api/boe/sumario/20260914 | 15-09-2026 | 3 |
| W2 | AEAT `bienes.js`: HTTP 200, Last-Modified 14-09-2026 13:24 GMT | https://www2.agenciatributaria.gob.es/static_files/common/internet/dep/taiif/subastaInmuebles/data2/bienes.js | 15-09-2026 | 3 |
| W3 | Catastro ConsultaMunicipio: JAVEA/XABIA, cp 3, cm 82 | https://ovc.catastro.meh.es/ovcservweb/OVCSWLocalizacionRC/OVCCallejero.asmx/ConsultaMunicipio?Provincia=ALICANTE&Municipio=JAVEA | 15-09-2026 | 3 |

**Uit de onderzoeksrapporten** (primaire bron zoals daar vastgesteld, na tegenspraak)

| Id | Bron | URL of pad | Datum | Type |
|---|---|---|---|---|
| B01 | properties-api: `feeds.js`, `server.js`, logs | file:///Users/root-admin/tree-hermes/properties-api/ | 15-09-2026 | 3 |
| B02 | Site-import en alarm: `run.ts`, `kyero.ts`, `map.ts`, `alarm.ts`, importlogs | file:///Users/root-admin/tree-website/tree-properties/src/lib/ | 15-09-2026 | 3 |
| B03 | tree-ai-agentic-os: `authority.py`, `approvals.py`, `costs.py`, `killswitch.py` | file:///Users/root-admin/tree-es/tree-ai-agentic-os/os_core/ | 15-09-2026 | 3 |
| B04 | Hermes `cron create --help`; toolregister | file:///Users/root-admin/tree-es/hermes-agent-organization/registry/tools.yaml | 14-09-2026 | 3 |
| B05 | Tree AI OS: `compose.yaml`, `backup.sh`, `waakhond.sh`; machinegegevens | file:///Users/root-admin/tree-ai-os/ | 14-09-2026 | 3 |
| B06 | Governance: hard cap 400 / waarschuwing 300 | file:///Users/root-admin/tree-es/hermes-agent-organization/governance/delegated-authority.yaml | 15-09-2026 | 3 |
| B07 | Anthropic-prijzen, Batch −50 %, tokenizer | https://platform.claude.com/docs/en/about-claude/pricing | 15-09-2026 | 2 |
| B08 | Anthropic vision: beeldtokens; geen betrouwbare detectie van AI-beelden | https://platform.claude.com/docs/en/build-with-claude/vision | 15-09-2026 | 2 |
| B09 | Claude Code headless (`--bare`, `--permission-prompts`) | https://code.claude.com/docs/en/headless | 15-09-2026 | 2 |
| B10 | GHL Custom Objects OpenAPI (Agency-Access voor schema) | https://raw.githubusercontent.com/GoHighLevel/highlevel-api-docs/main/apps/objects.json | 15-09-2026 | 2 |
| B11 | GHL rate limits | https://marketplace.gohighlevel.com/docs/other/rate-limits/ | 15-09-2026 | 2 |
| B12 | Docker Hub `postgis/postgis`: alleen amd64 | https://hub.docker.com/v2/repositories/postgis/postgis/tags/16-3.5 | 15-09-2026 | 2 |
| B13 | Docker Hub `imresamu/postgis` (niet-officieel, arm64) | https://hub.docker.com/v2/repositories/imresamu/postgis/tags/16-3.5 | 15-09-2026 | 1 |
| B14 | psycopg 3.3.5 en installatievarianten | https://pypi.org/pypi/psycopg/json · https://raw.githubusercontent.com/psycopg/psycopg/master/docs/basic/install.rst | 15-09-2026 | 2 |
| B15 | dHash-referentie-implementatie (+ synthetische test R17-verificatie) | https://raw.githubusercontent.com/JohannesBuchner/imagehash/master/imagehash/__init__.py | 15-09-2026 | 2 / 3 |
| B16 | Resend-prijzen | https://resend.com/pricing | 15-09-2026 | 1 |
| B17 | Apple launchd `StartCalendarInterval` | https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/ScheduledJobs.html | 15-09-2026 | 2 |
| B20 | BP aviso legal (schriftelijke toestemming; sjabloon voor website) | https://backgroundproperties.com/aviso-legal/ | 15-09-2026 | 2 |
| B21 | BP partnerlijst (41 kantoren) | https://backgroundproperties.com/wp-json/wp/v2/pages?slug=makelaars | 14-09-2026 | 1 / 3 |
| B22 | Kyero v3 importspecificatie (`date` = laatste wijziging) | https://feeds.kyero.com/assets/kyero_v3_import_spec.txt | 14-09-2026 | 2 |
| B23 | Kyero helppagina (volledige momentopname, verwijderen bij afwezigheid) | https://help.kyero.com/estate-agents/xml-import-specification | 14-09-2026 | 2 |
| B24 | BP-exports 26–32: Last-Modified, User-Agent-gedrag (URL's met sleutel niet opgenomen) | feed-URL's met sleutel, niet opgenomen | 14-09-2026 | 3 |
| B25 | BP-aanbodanalyse via lokale API (225/57, afwijkingen) | http://127.0.0.1:3100/api/stats | 14-09-2026 | 3 |
| B30 | Idealista Search API aanvraagformulier | https://developers.idealista.com/access-request | 15-09-2026 | 2 |
| B31 | Idealista-voorwaarden 20-11-2020 | https://st1.idealista.com/ayuda/wp-content/uploads/2021/11/2021-Hasta-11-11-2021-Terminos-y-condiciones.pdf | 15-09-2026 | 2 |
| B32 | Idealista-voorwaarden 17-02-2024 (opgeslagen zoekopdrachten toegestaan) | https://st1.idealista.com/ayuda/wp-content/uploads/2025/04/Condiciones-generales-vigentes-hasta-29.04.2025-idealista.pdf | 15-09-2026 | 2 |
| B33 | Idealista robots.txt | https://www.idealista.com/robots.txt | 15-09-2026 | 3 |
| B34 | Idealista-assistent (officiële MCP): tellingen Jávea, velden, overlap met BP | https://www.idealista.com/es/venta-viviendas/javeaxabia-alicante/con-chalets,para-reformar/ | 14/15-09-2026 | 3 |
| B35 | idealista/data (offerte) | https://www.idealista.com/data/ | 15-09-2026 | 2 |
| B40 | Veilingportaal robots.txt (`Disallow: /`) | https://subastas.boe.es/robots.txt | 15-09-2026 | 3 |
| B41 | Veilingportaal help (meldingen ≤ 50, alleen natuurlijke personen) | https://subastas.boe.es/ayuda.php | 15-09-2026 | 2 |
| B42 | Veilingportaal steekproef Alicante PU/EJ | https://subastas.boe.es/subastas_ava.php | 15-09-2026 | 3 |
| B43 | BOE open-data-API documentatie (XML en JSON) | https://www.boe.es/datosabiertos/api/api.php | 15-09-2026 | 2 |
| B44 | boe.es robots.txt (`xml.php` uitgesloten) | https://www.boe.es/robots.txt | 15-09-2026 | 3 |
| B45 | AEBOE hergebruiklicentie 27-06-2024 | https://www.boe.es/informacion/aviso_legal/index.php | 15-09-2026 | 2 |
| B46 | BOE-RSS Sección IV en V-B | https://www.boe.es/rss/boe.php?s=4 · https://www.boe.es/rss/boe.php?s=5B | 15-09-2026 | 3 |
| B47 | LEC art. 646, 648, 649, 669, 670 (versie sinds 03-04-2025) | https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-2000-323/texto/bloque/a649 | 15-09-2026 | 2 |
| B48 | Reglamento General de Recaudación art. 103 bis, 104, 104 bis | https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-2005-14803/texto/bloque/a1-4 | 15-09-2026 | 2 |
| B49 | Ley del Notariado art. 75 | https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-1862-4073/texto/bloque/a75 | 15-09-2026 | 2 |
| B50 | Reglamento Recaudación Seguridad Social art. 117, 121 | https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-2004-11836/texto/bloque/a117 | 15-09-2026 | 2 |
| B51 | AEAT-sede veilingen ("La subasta será única") | https://sede.agenciatributaria.gob.es/Sede/deudas-apremios-embargos-subastas/subastas/general.html | 15-09-2026 | 2 |
| B52 | SUMA procedure veilingen | https://www.suma.es/procedimiento-subastas | 15-09-2026 | 2 |
| B53 | BOE-B-2022-17675 (voorbeeld veiling rechtbank Dénia) | https://www.boe.es/diario_boe/txt.php?id=BOE-B-2022-17675 | 15-09-2026 | 2 |
| B54 | TGSS-veilingportaal | https://w6.seg-social.es/subastas/ | 15-09-2026 | 2 |
| B60 | Catastro Webservices Libres v2.6 | https://www.catastro.hacienda.gob.es/ws/Webservices_Libres.pdf | 15-09-2026 | 2 |
| B61 | Catastro `Consulta_RCCOOR_Distancia` | https://ovc.catastro.meh.es/ovcservweb/OVCSWLocalizacionRC/OVCCoordenadas.asmx/Consulta_RCCOOR_Distancia | 15-09-2026 | 3 |
| B62 | Catastro JSON `Consulta_DNPRC` / `Consulta_DNPLOC` | https://ovc.catastro.meh.es/OVCServWeb/OVCWcfCallejero/COVCCallejero.svc/json/Consulta_DNPLOC | 15-09-2026 | 3 |
| B63 | INSPIRE WFS percelen | https://ovc.catastro.meh.es/INSPIRE/wfsCP.aspx | 15-09-2026 | 3 |
| B64 | INSPIRE WMS | https://ovc.catastro.meh.es/cartografia/INSPIRE/spadgcwms.aspx | 15-09-2026 | 3 |
| B65 | ATOM-feed provincie 03 (Xàbia 03082, EPSG:25831, 21-08-2026) | https://www.catastro.hacienda.gob.es/INSPIRE/CadastralParcels/03/ES.SDGC.CP.atom_03.xml | 15-09-2026 | 3 |
| B66 | INSPIRE-licentie Catastro | https://www.catastro.hacienda.gob.es/webinspire/documentos/Licencia.pdf | 15-09-2026 | 2 |
| B67 | Catastro gebruiksvoorwaarden (weigering circa 10 dagen) | https://www.catastro.hacienda.gob.es/ayuda/condicionesuso.htm | 15-09-2026 | 2 |
| B68 | Sede Catastro valor de referencia (Cl@ve) | https://www1.sedecatastro.gob.es/Accesos/SECAccvr.aspx | 15-09-2026 | 3 |
| B69 | Registradores: prijs nota simple 9,02 € + btw | https://www.registradores.org/en/-/cuando-cuesta-una-nota-simple-en-un-registro-de-la-propiedad | 15-09-2026 | 2 |
| B70 | Registradores: Registro de la Propiedad (24 uur; legitiem belang) | https://www.registradores.org/el-colegio/registro-de-la-propiedad | 15-09-2026 | 2 |
| B71 | Arancel registradores RD 1427/1989 | https://www.boe.es/buscar/act.php?id=BOE-A-1989-28112 | 15-09-2026 | 2 |
| B72 | Ley Hipotecaria art. 10.4 | https://www.boe.es/buscar/act.php?id=BOE-A-1946-2453 | 15-09-2026 | 2 |
| B80 | TRLPI art. 18, 128, 133, 134 | https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-1996-8930/texto/bloque/a133 | 15-09-2026 | 2 |
| B82 | AEPD-lijst DPIA art. 35.4 | https://www.aepd.es/documento/listas-dpia-es-35-4.pdf | 15-09-2026 | 2 |
| B86 | Registro Público Concursal aviso legal | https://www.publicidadconcursal.es/aviso-legal | 15-09-2026 | 2 |
| B90 | Ley 13/1997 CV art. 13 (ITP 9 % / 11 %) | https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-1998-8202/texto/bloque/a13 | 15-09-2026 | 2 |
| B91 | TRLITPAJD art. 10 (valor de referencia) | https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-1993-25359/texto/bloque/a10 | 15-09-2026 | 2 |
| B92 | Ley del IVA art. 91 (10 % woningen) | https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-1992-28740/texto/bloque/a91 | 15-09-2026 | 2 |
| B93 | Ministerio de Hacienda, gemeentelijke tarieven 2026 (Xàbia) | https://serviciostelematicosext.hacienda.gob.es/SGFAL/ConsultaTipos/aspx/ImpuestosExcel.aspx?provincia=TODAS&anosel=2026 | 15-09-2026 | 2 |
| B94 | Banco de España tabel 19.1 (Euríbor, rentes) | https://www.bde.es/webbe/es/estadisticas/compartido/datos/pdf/a1901.pdf | 15-09-2026 | 2 |
| B95 | Ley 2/1974 art. 14 (verbod op tariefrichtlijnen) | https://www.boe.es/buscar/act.php?id=BOE-A-1974-289 | 15-09-2026 | 2 |
| B96 | Cuatrecasas over DGT V0453-22 (grondslag ITP bij veiling; secundair) | https://www.cuatrecasas.com/es/spain/art/espana-la-base-imponible-de-tpo-en-la-adjudicacion-judicial-de-inmuebles | 15-09-2026 | 1 |
| B97 | IVE Base de Datos de Construcción | https://productos.five.es/producto/base-de-datos-de-construccion | 15-09-2026 | 1 |
| B98 | habitissimo nieuwbouw (honoraria, btw-status) | https://www.habitissimo.es/presupuestos/construccion-casas | 15-09-2026 | 1 |

**Toegevoegd in de herstelronde** (primaire bron zoals vastgesteld in de genoemde deliverable of het genoemde onderzoeksbestand; niet opnieuw opgehaald)

| Id | Bron | URL of pad | Datum | Type |
|---|---|---|---|---|
| B100 | ICV WFS/WMS Planeamiento (GetCapabilities: "No se aplican condiciones", CC BY 4.0; tests K07 en Villes del Vent; bbox EPSG:25830) — via D03 [C27], R12-verificatie en R13 §7 | https://terramapas.icv.gva.es/0702_Planeamiento?service=WFS&request=GetCapabilities | 15-09-2026 | 2 (dienst) / 3 (tests) |
| B101 | datos.gob.es, dataset planeamiento urbanístico CV (update 25-08-2026, "carácter informativo") | https://datos.gob.es/es/catalogo/a10002983-planeamiento-urbanistico-de-la-comunitat-valenciana-clasificacion-urbanistica | 15-09-2026 | 2 |
| B102 | ICV Infraestructura Verde (`IVR.Inundacion`, `IVR.ZEC/LIC/ZEPA`, `IVR.Cultura.*`) | https://terramapas.icv.gva.es/0701_InfraestructuraVerde | 15-09-2026 | 3 |
| B103 | ICV ArcGIS REST ordenación territorial (PATRICOVA 4–10, PATIVEL 30–34) | https://carto.icv.gva.es/arcgis/rest/services/tm_infraestructuras/ordenacion_territorial/MapServer | 15-09-2026 | 3 |
| B104 | ICV PORN Montgó | https://terramapas.icv.gva.es/0505_PORN | 15-09-2026 | 3 |
| B105 | ICV PATFOR | https://terramapas.icv.gva.es/0506_PATFOR | 15-09-2026 | 3 |
| B106 | ICV ArcGIS espacios protegidos (laag 21) | https://carto.icv.gva.es/arcgis/rest/services/tm_medio_ambiente/espacios_protegidos/MapServer | 15-09-2026 | 3 |
| B107 | ICV ArcGIS prevención de incendios | https://carto.icv.gva.es/arcgis/rest/services/tm_medio_ambiente/prevencion_de_incendios/MapServer | 15-09-2026 | 3 |
| B108 | IDEE overstromingsgevaar (ARPSI) | https://servicios.idee.es/wms-inspire/riesgos-naturales/inundaciones | 15-09-2026 | 3 |
| B109 | IGME GEODE 50 (voorwaarde: contact bij betaalde dienst met toegevoegde waarde) | https://mapas.igme.es/gis/services/Cartografia_Geologica/IGME_Geode_50/MapServer/WMSServer | 15-09-2026 | 3 |
| B110 | MITECO DPMT-diensten (NullReferenceException, reset, 503) | https://wms.mapama.gob.es/sig/Costas/DPMT · https://gis.miteco.gob.es/web/dpmt | 15-09-2026 | 3 |
| B111 | GVA-planregister Xàbia (open directory; ordenanzas PGOU, Mod. XXV, sentencia Portitxol) | https://mediambient.gva.es/auto/urbanismo/reg-planeamiento/2%20ALICANTE/03082%20X%C0BIA/ | 15-09-2026 | 2 |
| B112 | TRLOTUP, geconsolideerd tot 02-07-2026 (art. 226, 246, 248) | https://www.boe.es/buscar/act.php?id=DOGV-r-2021-90283 | 15-09-2026 | 2 |
| B113 | GVA-register: SENTENCIA HOM PORTITXOL (TSJCV 459/2012, 26-04-2012) — pad in R12-verificatie bron 11 | https://mediambient.gva.es/auto/urbanismo/reg-planeamiento/2%20ALICANTE/03082%20X%C0BIA/ (submap 03082-1001 HOMOLOGACIÓN PG PORTITXOL (Anulado)) | 15-09-2026 | 2 |
| B114 | Tinsa Radar: 29 € per studie, 99 of 259 €/maand, 7 dagen proef, pdf; btw niet vermeld | https://radar.tinsa.es/es | 15-09-2026 | 1 |
| B115 | MIVAU Boletín Online: transacciones (gemeente alleen aantal), valor tasado (gemeenten > 25.000 inwoners) | https://apps.fomento.gob.es/BoletinOnline2/?nivel=2&orden=34000000 | 15-09-2026 | 2/3 |
| B116 | Portal Estadístico del Notariado, términos y condiciones (geen commercieel gebruik) | https://www.penotariado.com/inmobiliario/terminos-y-condiciones | 15-09-2026 | 2 |
| B117 | Fotocasa-index Jávea/Xàbia per wijk (alleen pisos y áticos) | https://www.fotocasa.es/es/indice-precio-vivienda/javea-xabia/todas-las-zonas | 15-09-2026 | 1/3 |
| B118 | Orden ECO/805/2003, art. 21 ("al menos seis transacciones u ofertas de comparables") — via R01-verificatie A6 | https://www.boe.es/buscar/act.php?id=BOE-A-2003-7253 | 15-09-2026 | 2 |
| B119 | Servihabitat Profesionales, Sareb-perceel A Balcón al Mar (promotie 06124187) — gebruikt in T10e | https://inversores.servihabitat.com/es/venta/promociones/terreno-urbanonoconsolidado/alicante-marinaalta-balconalmarjavea/06124187 | 15-09-2026 | 1 |
| B120 | Idealista-assistent: K10 107655781 en dubbel 111869151 — gebruikt in T10e | https://www.idealista.com/es/inmueble/107655781/ · https://www.idealista.com/es/inmueble/111869151/ (links zonder utm-parameters) | 15-09-2026 | 1 (inhoud) / 3 (bestaan) |
| B121 | Idealista-assistent: Villes del Vent 111295146 en BP 4603JAV — gebruikt in T10b | https://www.idealista.com/es/inmueble/111295146/ · http://127.0.0.1:3100/api/properties | 15-09-2026 | 1 / 3 |

**Overige verwijzingen:** `MP §n` = masterprompt, file:///Users/root-admin/tree-es/deal-hunter/MASTERPROMPT.md (14-09-2026, opdracht). `D01`–`D04` = deliverables file:///Users/root-admin/tree-es/deal-hunter/01-acquisitiekader-javea.md, 02-bronnenkaart-en-register.md, 03-aanpak-percelen.md en 04-aanpak-veilingen-en-bijzondere-verkopen.md (15-09-2026), met het bewijstype zoals daar per claim vastgesteld. `Rnn §x` en `Rnn-verificatie` = onderzoeksbestanden in file:///Users/root-admin/tree-es/deal-hunter/onderzoek/ (14/15-09-2026), met het bewijstype zoals daar vastgesteld. ADR-0014 (GoHighLevel als CRM van waarheid) komt uit de lokale feiten van de opdracht (14-09-2026, bewijstype 3). Datalicentieprijzen DataVenues-widget en Tinsa Radar: R17 §11a.3, overgenomen uit R02 en R04 (14-09-2026, bewijstype 1).

**Geblokkeerd of niet gedaan in deze ronde:** WebSearch niet gebruikt (sessiebudget eerder als uitgeput gemeld). Er is geen nieuw webonderzoek gedaan buiten drie enkelvoudige bereikbaarheidscontroles (W1–W3). Wetteksten, kaartdiensten (B100–B110) en waarderingsbronnen (B114–B118) zijn in de herstelronde niet opnieuw opgehaald; de deliverables 02–04 en de verificatierapporten van 15-09-2026 zijn gevolgd. Back-uplogs van Tree AI OS niet nagerekend (L7). Geen geheimen, feed-URL's met sleutel, telefoonnummers of persoonsnamen van particulieren overgenomen; `feeds.js` en `.env`-bestanden niet geopend.

## Herzieningen

- 15-09-2026 (samenhangscontrole): registeraantal 49 vervangen door de actuele stand van `bronnenregister.json` (75 regels; ALLEEN HANDMATIG 39, TECHNISCH ONDERZOEK NODIG 18, CONTRACT OF TOESTEMMING NODIG 14, NIET GEBRUIKEN 4), met rechtenvlaggen en kaartlaagregels R2-60 t/m R2-69 (Deel 2, Deel 3, 6.2, 6.3, Concrete vervolgstap, correctietabel, L8); bankvastgoed en K10 in §3.5-rij en correctietabel als "waarschijnlijk" één object (type 4) met tegenstrijdige planklasse (type 7), btw in plaats van ITP volgens de servicer, en 2 Sareb-percelen bij Servihabitat Profesionales; BP-feedrij met peildatum en plaatsnaam "Javea" zonder accent; noemer BP tegenover Idealista gelijkgetrokken (333); verouderde verwijzingen naar eerdere versies van 01, 02 en 04 (eActivos, doorschakelnummers, advocaatvolgorde, "0 de bancos") als eerdere versie gemarkeerd; verwijzing naar de top-3 in deliverable 01 §1.2 toegevoegd.

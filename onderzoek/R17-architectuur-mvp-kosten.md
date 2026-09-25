# R17 — Technische architectuur, hergebruik van bestaande bouwstenen, kostenraming en MVP-ontwerp

> **NA TEGENSPRAAK (15-09-2026).** Dit rapport is door een tweede agent gecontroleerd; zie `R17-architectuur-mvp-kosten.verificatie.md`. Betrouwbaarheid volgens die controle: hoog.
> Geen kernclaims weerlegd; wel eventuele aanvullingen en voorbehouden in het verificatiebestand.


**Project:** TREE Deal Hunter, fase A (bronnen en investeringskader)
**Stroom:** R17 — masterprompt secties 27 (architectuur), 28 (kwaliteit en acceptatietests), 29 (uitvoeringsvolgorde), 24 (ochtendrapport)
**Controledatum:** 14-09-2026 (alle lokale controles en webbronnen op deze datum)
**Aanvulling:** 15-09-2026 — §11a (actuele stand BP-feed, plaatsnaamnormalisatie, kosten per dossier en datalicenties uit andere stromen). Waar §11a iets in §1–§9 bijstelt, geldt §11a.
**Auteur:** onderzoeksagent R17, in opdracht van Jan (TREE Group, Jávea)

**Bewijstypes (masterprompt §5):** 1 door aanbieder vermeld · 2 in officiële bron aangetroffen · 3 door ons rechtstreeks vastgesteld · 4 AI-inferentie · 5 berekening op benoemde aannames · 6 door bevoegde professional bevestigd · 7 onbekend of tegenstrijdig

---

## Samenvatting in tien regels

1. **Er staat al meer dan de helft van de keten.** Op deze Mac mini draaien vier herbruikbare bouwstenen: de Kyero-feedparser en de importlogica van treeproperties.es (met krimpdrempel, `withdrawn`-status en een bewezen alarm naar Teams), de bevoegdheden-/approval-/audit-/kostenmodule van `tree-ai-agentic-os` (SQLite, 23 tests groen), de Hermes-agentorganisatie met een `cron`-planner die scriptuitvoer zonder LLM naar Discord kan bezorgen, en het back-up- en waakhondpatroon van Tree AI OS. Alles is rechtstreeks gelezen (bewijstype 3).
2. **De kleinste complete versie voor Jávea kan zonder één installatie.** Python 3.11.15 in de Hermes-venv heeft `httpx`, `defusedxml`, `Pillow`, `numpy`, `anthropic 0.86`, `jinja2` en `fastapi`; SQLite 3.50.4 heeft R-tree en FTS5 aan boord (getest). Wat ontbreekt (`psycopg`, `lxml`, `shapely`, `imagehash`) is voor fase B niet nodig.
3. **Aanbeveling: variant 1 (nul-installatie) voor fase B, met een opslaglaag die later naar Postgres+PostGIS kan.** PostGIS wordt pas nodig als de perceelmodule kadastrale polygonen gaat snijden (fase C/D). Het officiële `postgis/postgis`-image vermeldt alleen `amd64`; deze Mac is `arm64` (Apple M4). Of het image hier draait is **[te verifiëren]** vóór Jan daar akkoord op geeft.
4. **GoHighLevel heeft een echte Custom Objects API** (officiële OpenAPI-spec `apps/objects.json`): schema's aanmaken, records aanmaken/bijwerken/zoeken, header `Version: 2021-07-28`, scopes `objects/schema.*` en `objects/record.*`, paginering via `page`/`pageLimit`/`searchAfter`. Rate limits staan niet in die spec en de docs-site is JavaScript-only: **ONBEKEND**. Objectdossiers in GHL zijn dus conform ADR-0014 mogelijk.
5. **AI-analyse is goedkoop op deze schaal.** Officiële prijzen (14-09-2026): Haiku 4.5 $1/$5, Sonnet 5 $2/$10, Opus 5 $5/$25 per miljoen input/output-tokens; Batch API −50 %. Tekstclassificatie van 1.000 advertenties kost $4 (Haiku) of $8 (Sonnet); foto-analyse van 8 foto's per advertentie $13,50 (Haiku) of $27 (Sonnet), mits foto's vooraf verkleind worden. Een Jávea-maand (400 heranalyses + 150 fotosets) blijft onder $8.
6. **De Idealista-assistent is alleen in een Claude-sessie aanroepbaar.** Een launchd-script kan die MCP niet gebruiken. Opties: (a) `claude -p` headless met de connector (technisch beschreven in de officiële docs, hier niet getest; voorwaarden ONBEKEND), (b) een vaste interactieve ronde die naar JSON exporteert, (c) de officiële Search API aanvragen (R01). Advies: (b) voor fase B, (c) direct aanvragen.
7. **Wijzigingsdetectie op momentopname-feeds** vraagt een eigen historie: per run een `run_id`, per advertentie een inhouds-hash en `first_seen_at`/`last_seen_at`; "niet meer gevonden" pas na twee opeenvolgende geslaagde runs zonder de advertentie, nooit na een mislukte run (les van 14-09: DNS-uitval gaf 0 objecten). Dedupe in drie trappen: ref → coördinaat + oppervlakte → dHash op foto's (Pillow+numpy, 64 bits, Hamming-afstand; drempel te kalibreren).
8. **Ochtendrapport:** Python + Jinja2 genereert HTML en Markdown in `Europe/Madrid` (zoneinfo werkt in de venv). Bezorging via Hermes-cron (`--no-agent --script`, verbatim naar Discord), rechtstreeks via de Discord-bot-API (waakhondpatroon), Teams-webhook of Resend. Let op: de bestaande G-CEO-routine faalt al 11 keer op rij met "delivery platform 'discord' has no gateway credentials configured" — de bezorging moet dus eerst bewezen worden.
9. **Kostenraming:** ontwikkeling fase B ± 60–90 uur, fase C ± 80–120 uur, fase D open; maandkosten hosting €0 (eigen Mac), AI < €10, datalicenties ONBEKEND (alle aggregators werken op offerte, R04), nota simple en professionals per dossier **ONBEKEND/[te verifiëren]**.
10. **Drie beslissingen voor Jan:** (1) tijdstip en kanaal van het ochtendrapport; (2) toestemming voor `psycopg` + PostGIS-container als de perceelmodule dat vraagt (niet nu); (3) of de Idealista-assistent gepland gebruikt mag worden — pas na schriftelijke bevestiging van Idealista, anders handmatig.

---

## 0. Leeswijzer en afbakening

Dit rapport vertaalt de modulaire keten uit masterprompt §27 naar concrete onderdelen op deze Mac mini. Het is geschreven zodat Jan de keuzes begrijpt (technische termen worden kort uitgelegd) en een engineer ermee kan bouwen. Alles wat ik zelf heb gezien staat als bewijstype 3; wat ik uit officiële documentatie heb, als 2; eigen berekeningen als 5; eigen inschattingen (uren) als 4/5 en zo gemarkeerd. Geheimen (feed-sleutels, tokens, webhook-adressen) zijn nergens overgenomen; waar ik een bestand met sleutels heb gelezen, vermeld ik alleen de structuur.

Wat dit rapport **niet** doet: bronnen of rechten opnieuw onderzoeken (dat staat in R01–R09), en iets bouwen, starten of installeren.

---

## 1. Inventaris van bestaande bouwstenen (allemaal rechtstreeks gelezen, bewijstype 3)

### 1.1 Woningfeed-dienst `com.tree.properties-api` (Node 20, poort 3100)

| Aspect | Waargenomen |
|---|---|
| Bestanden | `~/tree-hermes/properties-api/server.js` (5,0 kB), `feeds.js` (6,6 kB), `package.json`: `express ^4.21`, `xml2js ^0.6.2`, `node-cron ^3.0.3`, `cors ^2.8.5` |
| Bronnen | Zes `FEED_SOURCES` (export_id 26, 27, 29, 30, 31, 32) met velden `id`, `commission` (5 of 3), `category` (`all`/`newbuild`/`resale`), `label`. De sleutel zit in de URL — niet overgenomen. |
| Opslag | **In-memory `Map`**, sleutel = `ref`; geen database, geen bestand, geen historie. Bij herstart is alles weg tot de eerste ophaalronde slaagt. |
| Dedupe | Per `ref`; bij dubbel wint de hoogste commissie (`prop._commission > existing._commission`). |
| Planning | `node-cron` `"0 * * * *"` (elk heel uur) plus één keer bij start. |
| Foutgedrag | Fouten per feed in `fetchErrors[]`; de ronde gaat door met de overige feeds; `properties = newProperties` wordt **altijd** overschreven — een ronde waarin alle zes feeds falen levert dus 0 objecten op (bevestigd in `logs/stderr.log`, regels 4096–4107: zes keer `getaddrinfo ENOTFOUND backgroundproperties.com` op 14-09-2026 22:12). Er is geen krimpdrempel. |
| Endpoints | `GET /api/health` (`status`, `properties`, `lastFetch`), `GET /api/stats`, `GET /api/properties` (filters `type`, `town`, `minPrice`, `maxPrice`, `beds`, `baths`, `pool`, `newBuild`, `search`, `lang`, `sort`, `order`, `page`, `limit` ≤ 100), `GET /api/properties/:ref`, `GET /api/filters`. Interne velden `_feed`, `_commission`, `_category` worden uit de uitvoer gestript. |
| Parser | `parseProperty()` leest: `id`, `ref`, `date`, `price`, `currency`, `price_freq`, `type`, `new_build`, `town`, `postcode`, `province`, `country`, `location_detail`, `location/latitude+longitude`, `beds`, `baths`, `pool` (altijd leeg in de praktijk), `surface_area/built+plot`, `energy_rating`, `url` en `desc` per taal (en/es/nl/de/fr), `features/feature`, `images/image`. |
| launchd | `com.tree.properties-api.plist`: `RunAtLoad` + `KeepAlive` = true, `PORT=3100`, logs in `logs/stdout.log` en `stderr.log`. |

**Betekenis voor Deal Hunter.** Deze dienst is een goede *bron van momentopnamen* maar geen historie-opslag en geen wijzigingsdetector. Hij blijft ongemoeid (productie). Twee manieren om hem te gebruiken staan in §5.1.

### 1.2 Importlogica treeproperties.es (`~/tree-website/tree-properties/src/lib/import/`, TypeScript)

| Bestand | Regels | Herbruikbaar idee |
|---|---|---|
| `kyero.ts` (179) | Kyero v3-parser op `fast-xml-parser` met `isArray` voor `property`, `image`, `feature`; `FeedError`; `fetchFeed(url, timeoutMs = 60_000)` met `AbortController`, eigen `User-Agent: treeproperties.es feed import`, `cache: 'no-store'`; typen `KyeroProperty` incl. `part_ownership`, `leasehold`, `notes` (velden die de BP-feed niet vult). | Veldenlijst en foutafhandeling één-op-één over te nemen in Python. |
| `run.ts` (322) | Rapport met `found`, `unchanged`, `withdrawn`, `aborted`; **krimpdrempel** `IMPORT_MAX_SHRINK_PCT` (default 30): meer dan 30 % minder woningen dan actief → afbreken, alarm, niets schrijven; verdwenen woningen krijgen `status=withdrawn` (nooit verwijderd); `lastSeenAt`/`lastImportAt`; `dryRun`. | Exact het gedrag dat §10 vraagt ("NIET MEER GEVONDEN" ≠ "verkocht"; lege feed = bronfout). |
| `images.ts` (131) | Sync op bron-URL: alleen nieuwe URL's ophalen, bestaande hergebruiken; `MAX_IMAGES_PER_PROPERTY = 40`. | Zelfde idee voor foto-hashes: hash één keer per URL. |
| `map.ts`, `tree-ref.ts` | Normalisatie van plaatsnamen (El Vergel → El Verger) en het TREE-nummer. | Plaatsnormalisatie hergebruiken. |
| `src/lib/alarm.ts` | Alarm bij stille storingen: kanaalvolgorde webhook (`ALARM_WEBHOOK_URL`, Teams/Slack/Discord; `isTeams()` kiest Adaptive Card) → Resend (`RESEND_API_KEY`) → GHL; demping 30 minuten per sleutel; altijd loggen in `var/alarm.log` met `[bezorgd]`/`[NIET BEZORGD]`; GHL overgeslagen als het alarm over GHL gaat. Bewezen in Teams op 26-08-2026 (CLAUDE.md, Openstaand punt 0). | Patroon in Python nabouwen (§6.6). |
| Planning | `com.tree.properties-import.plist`: `StartInterval` 7200 s + `RunAtLoad`; `scripts/import-periodiek.sh`. Site-CLAUDE.md: feed 36 = alle woningdata, 26/27 alleen commissielabels; "Nooit zeven keer dezelfde woning schrijven." | Zelfde feedkeuze. |

### 1.3 `tree-ai-agentic-os` (Python, SQLite, FastAPI; niet als dienst)

Gelezen: `README.md`, `os_core/authority.py`, `approvals.py`, `costs.py`, `killswitch.py`, `config.py`, `schema.sql`, `api/app.py`, `requirements.txt`, `run.sh`.

| Module | Wat het doet (letterlijk uit de code) | Bruikbaar voor Deal Hunter |
|---|---|---|
| `authority.evaluate(ActionRequest)` | A0–A2 autonoom, A3/A4 goedkeuring; `cost_eur > 0` of `external=True` → minstens A3; merkvermenging (meer dan één van `tree`, `rocksure`, `sani-kitchen`) → `blocked=True`; C4 nooit; C3 alleen `G-CEO`; agentplafond `max_autonomy` uit het register. | Elke actie met externe werking (mail aan makelaar, GHL-schrijfactie, biedvoorstel) door deze functie halen. |
| `approvals.create/decide/expire_stale` | Statemachine open → goedgekeurd/afgewezen/vervallen; maker-checker (`can_approve`); weigert beslissingen als `killswitch.is_locked()`. | Approval-inbox voor dossiers. |
| `costs.add/month_total/status` | `cost_ledger` per agent/merk/periode; hard plafond €400, waarschuwing €300 (`config.py`); audit-record bij overschrijding. | Tokenkosten van Deal Hunter hier bijschrijven. |
| `killswitch.is_locked()` | `~/.hermes/LOCKDOWN` bestaat → write-acties geblokkeerd; het OS zet of verwijdert de marker nooit zelf. Op 14-09-2026 23:40 bestond de marker niet. | Deal Hunter controleert dezelfde marker vóór elke run. |
| `schema.sql` | Tabellen `agents`, `tasks`, `handoffs`, `approvals`, `incidents`, `audit_log` (append-only), `cost_ledger`; `PRAGMA journal_mode = WAL`. | Schema-stijl overnemen; eigen database ernaast (niet delen). |
| `api/app.py` | Routes `/api/health`, `/api/status`, `/api/agents`, `/api/tasks`, `/api/approvals`, `/api/audit`, `/api/costs`, `POST /api/authority/evaluate`, `POST /api/approvals`, `POST /api/approvals/{id}/decide`, `POST /api/incidents`, `POST /api/costs`; cockpit op `127.0.0.1:8700` via `run.sh`. | Reviewpagina naar dit voorbeeld (§8.2). |

### 1.4 Hermes-agentorganisatie (`~/tree-es/hermes-agent-organization/`, Hermes v0.20.6)

- Acht agents `active` (`registry/agents.yaml`): G-CEO, G-RESEARCH, G-MARKETING, G-SALES, G-DEVELOPER, G-INTERIOR, G-ARCHITECT, G-HR. Modellen gepind (`registry/models.yaml`): frontier `anthropic/claude-opus-5`, workhorse `anthropic/claude-sonnet-5`, routine `anthropic/claude-haiku-4.5`, provider OpenRouter.
- Toolregister (`registry/tools.yaml`): `cronjob` staat voor alle agents **uit** — "agents mogen niet hun eigen routines plannen; routines zijn een Gate C-besluit". Routines worden door Jan/beheer met de CLI aangemaakt.
- `hermes cron create --help` (venv-CLI, gelezen): schema `'30m'`, `'every 2h'` of cron-expressie; `--deliver origin|local|telegram|discord|signal|platform:chat_id|bot-chat[:profile]`; `--script` (pad onder `~/.hermes/scripts/`); **`--no-agent`**: "Skip the LLM entirely — run --script on schedule and deliver its stdout directly. Empty stdout = silent."; `--monitor-script`/`--monitor-url` (hash-onderdrukking bij ongewijzigde uitvoer); `--workdir`; `--model`.
- **Waargenomen storing:** `~/.hermes/profiles/g-ceo/cron/jobs.json` — job "G-CEO Dagelijkse uitzonderingen" (`0 9 * * 1-5`, `deliver: discord:<kanaal-id>`) heeft `last_status: "blocked_config"`, `failure_streak: 11`, `last_error: "[blocked_config:silent] delivery platform 'discord' has no gateway credentials configured (not connected)"`. Het default-profiel (`~/.hermes/cron/jobs.json`) heeft nul jobs. De hoofdgateway zelf ís verbonden: `agent.log` 14-09-2026 22:16:38 "[Discord] Connected as TREE-Hermes-Bot#0545 … discord reconnected successfully" (na een DNS-fout om 22:14, dezelfde uitval als bij de feed). Conclusie: cron-bezorging vanuit een **profiel** naar Discord werkt op dit moment niet; vanuit het default-profiel is het niet getest.
- `scripts/kill-switch.sh`: zet `~/.hermes/LOCKDOWN`, boot alle `*hermes*`-launchd-jobs uit en `disable`t ze; opheffen alleen door Jan (runbook).

### 1.5 Tree AI OS (`~/tree-ai-os/`)

- `compose.yaml`: één service `postgres`, image `postgres:16.6-alpine`, container `tree-ai-os-postgres`, poort `127.0.0.1:5433:5432`, volume `pgdata`, healthcheck `pg_isready`. Deze database is van Tree AI OS en wordt niet gedeeld (afspraak in de opdracht).
- In die Postgres beschikbaar (gecontroleerd met `pg_available_extensions`): `cube 1.5`, `earthdistance 1.1`, `pg_trgm 1.6`; **geen `postgis`**.
- `scripts/backup.sh`: `pg_dump … | gzip` + `tar` van `var/storage` en `var/quarantine`, retentie 14, nachtelijk 03:30 via `com.tree.ai-os.backup.plist` (`StartCalendarInterval` Hour 3 / Minute 30); slotregel: "Kopieer back-ups periodiek naar een plek buiten deze Mac".
- `scripts/waakhond.sh` (elke 600 s via `com.tree.ai-os.waakhond.plist`): eerst repareren, dan melden; meldt **rechtstreeks via de Discord-bot-API** (`Authorization: Bot …` uit `.env`, kanaal opgezocht op naam) "want de database kan juist weg zijn"; alleen melden bij verandering of na 12 uur. Aanleiding: Docker stopte 2–3 september 2026, vier nachten back-up faalden ongemerkt.
- `.env` heeft rechten `-rw-------` (600); `.env.example` is leesbaar. Dit is het secretspatroon dat de opdracht noemt.

### 1.6 Planning op deze machine (launchd, `~/Library/LaunchAgents/`)

| Label | Soort | Planning | Status 14-09-2026 (`launchctl list`) |
|---|---|---|---|
| `com.tree.properties-api` | dienst | `RunAtLoad`, `KeepAlive` | PID 653, draait |
| `com.tree.properties-web` | dienst | `RunAtLoad`, `KeepAlive`, `HOST=127.0.0.1`, `PORT=3000` | PID 668, draait |
| `com.tree.properties-import` | taak | `StartInterval` 7200 s + `RunAtLoad` | geladen, laatste exit 1 |
| `com.tree.properties-blog` | taak | `StartCalendarInterval` zondag 07:00 | geladen |
| `com.tree.ai-os` | starter | `RunAtLoad`, `KeepAlive` false, `AbandonProcessGroup` | geladen, laatste exit 1 |
| `com.tree.ai-os.backup` | taak | `StartCalendarInterval` 03:30 | geladen |
| `com.tree.ai-os.waakhond` | taak | `StartInterval` 600 s | geladen, laatste exit 1 |
| `com.tree.leadgen-dagcontrole` | taak | `StartCalendarInterval` 08:00 | geladen |
| `ai.hermes.gateway` | dienst | — | PID 671, draait |

Apple-documentatie over `StartCalendarInterval` (bewijstype 2): "if the computer is asleep when the job should have run, your job will run when the computer wakes up. However, if the machine is off when the job should have run, the job does not execute until the next designated time occurs." Deze Mac slaapt nooit (CLAUDE.md), maar na stroomuitval wordt een gemiste run niet ingehaald — daarom `RunAtLoad` op de verwerkingsrun, niet op het rapport.

### 1.7 De machine en de gereedschapskist

| Onderdeel | Vastgesteld (bewijstype 3) |
|---|---|
| Hardware | Apple M4 (`arm64`), 32 GB RAM, 672 GB vrij op 926 GB |
| Docker | Docker Desktop 29.2.1, VM `aarch64`, 10 CPU's, 7,65 GiB toegewezen; enige lokale image `postgres:16.6-alpine` (381 MB) |
| Python | Hermes-venv `~/.hermes/hermes-agent/venv`: Python 3.11.15; aanwezig: `PIL 12.3.0`, `numpy 2.4.3`, `httpx 0.28.1`, `anthropic 0.86.0`, `jinja2 3.1.6`, `pyyaml 6.0.3`, `pydantic 2.13.4`, `fastapi 0.133.1`, `uvicorn 0.41.0`, `requests 2.33.0`, `aiohttp 3.14.3`, `pytest 9.0.2`, **`defusedxml 0.7.1`**, `openai 2.24.0`. Ontbreekt: `psycopg`, `psycopg2`, `lxml`, `shapely`, `pyproj`, `imagehash`, `sqlalchemy`, `bs4`, `pypdf`/`pdfminer`. |
| SQLite | bibliotheek 3.50.4; compile-opties bevatten `RTREE` en `FTS5`; `CREATE VIRTUAL TABLE … USING rtree` werkt; `json_extract()` werkt; `zoneinfo.ZoneInfo('Europe/Madrid')` werkt (tijd 23:44 +02:00). |
| Claude Code | CLI 2.1.241 op `~/.local/bin/claude`. `claude mcp list`: o.a. `claude.ai idealista: https://mcp-app.idealista.com/claude/v1/mcp – ✔ Connected`; `claude.ai GHL TREE: https://services.leadconnectorhq.com/mcp/anthropic/v2 – ! Needs authentication`. |
| Node | Node 20 (`/opt/homebrew/opt/node@20/bin`) voor de bestaande diensten. |
| PDF-gereedschap | `pdftoppm` ontbreekt; geen PDF-bibliotheek in de venv (relevant voor veilingdocumenten en de Catastro-licentie, zie §11). |

---

## 2. Webonderzoek

### 2.1 GoHighLevel: Custom Objects API (voor objectdossiers conform ADR-0014)

**Bron:** officiële OpenAPI-specificatie `apps/objects.json` in de openbare repository `GoHighLevel/highlevel-api-docs` ("This repo is our public documentation for API v2"), gelezen 14-09-2026 — bewijstype 2. De docs-site `marketplace.gohighlevel.com/docs/ghl/…` laadt alleen een titel zonder JavaScript en is dus hier niet leesbaar (geblokkeerd, niet omzeild).

| Eigenschap | Waarde (letterlijk uit de spec) |
|---|---|
| Titel | "CUSTOM_OBJECTS API" — "Custom objects are completely customizable objects that allow you to store and manage information tailored to your unique business needs." |
| Schema-endpoints | `GET /objects/{key}` "Get Object Schema by key / id"; `PUT /objects/{key}`; `GET /objects/` "Get all objects for a location"; `POST /objects/` "Create Custom Object" |
| Record-endpoints | `POST /objects/{schemaKey}/records` "Create Record"; `GET /objects/{schemaKey}/records/{id}`; `PUT /objects/{schemaKey}/records/{id}`; `DELETE /objects/{schemaKey}/records/{id}`; `POST /objects/{schemaKey}/records/search` "Search Object Records" |
| Verplichte header | `Version: 2021-07-28` |
| Scopes | `objects/schema.readonly`, `objects/schema.write`, `objects/record.readonly`, `objects/record.write` |
| Paginering | `SearchRecordsBody`: `page`, `pageLimit`, `searchAfter` |
| Rate limits | **Niet in de spec** → ONBEKEND (bewijstype 7). |
| Basis-URL | De bestaande site-integratie gebruikt `https://services.leadconnectorhq.com` met header `Version: 2021-07-28` (`src/lib/alarm.ts` regels 166–184: `contacts/upsert`, `conversations/messages`; `src/lib/ghl.ts` regel 14) — bewijstype 3. Dezelfde host is dus al in gebruik met een werkend token. |
| Verwante specs | `associations.json` en `custom-fields.json` bestaan in dezelfde map (gezien in de bestandslijst); inhoud niet gelezen. |
| MCP | GHL biedt een MCP-endpoint (`…/mcp/anthropic/v2`) dat in deze omgeving "Needs authentication" meldt — alleen voor interactief gebruik in een Claude-sessie, niet voor een launchd-script. |

**Wat dit betekent.** Een dossier kan als custom object `deal_hunter_object` in GHL leven, met records per fysiek object, gekoppeld aan contacten (makelaar) via associations. Welk authenticatiemodel (OAuth-app of Private Integration-token) de `objects/*`-scopes krijgt, staat niet in de spec: **[te verifiëren]** in de GHL-instellingen van TREE Properties. Rate limits: niet gevonden; ontwerp op maximaal enkele honderden schrijfacties per dag, met wachtrij en herpoging.

### 2.2 Anthropic-prijzen (officiële prijspagina, 14-09-2026, bewijstype 2)

Bron: `https://platform.claude.com/docs/en/about-claude/pricing` (de oude `docs.anthropic.com`-URL verwijst daarheen door).

| Model | Input / MTok | Output / MTok | 5-min cache write | Cache read | Batch input / output |
|---|---|---|---|---|---|
| Claude Opus 5 | $5 | $25 | $6,25 | $0,50 | $2,50 / $12,50 |
| Claude Sonnet 5 | $2 | $10 | $2,50 | $0,20 | $1 / $5 |
| Claude Haiku 4.5 | $1 | $5 | $1,25 | $0,10 | $0,50 / $2,50 |

Letterlijk: "The Batch API allows asynchronous processing of large volumes of requests with a 50% discount on both input and output tokens." En over Sonnet 5: "The $2/$10 per million input/output token pricing for Claude Sonnet 5, announced at launch as introductory pricing through August 31, 2026, is now the standard price." Tokenizer-noot: "Claude 4.7 and later models … produces approximately 30% more tokens for the same text" — dus Sonnet 5/Opus 5 tellen voor dezelfde advertentietekst ± 30 % meer tokens dan Haiku 4.5. Cache-multipliers stapelen met de batchkorting.

**Afbeeldingen** (`…/build-with-claude/vision`, bewijstype 2): kosten `⌈breedte/28⌉ × ⌈hoogte/28⌉` visuele tokens; standaard-tier (o.a. Haiku 4.5): lange zijde max 1568 px, max 1568 tokens; hoge-resolutie-tier (Claude 4.7 en later, dus Sonnet 5 en Opus 5): 2576 px, max 4784 tokens. Voorbeelden uit de tabel: 1000×1000 px = 1296 tokens op beide tiers; 1920×1080 = 1560 (standaard) tegen **2691** (hoge resolutie); 3840×2160 = 1560 tegen 4784. Advies uit de docs: "downsample images before sending to control token costs". Maximaal 600 afbeeldingen per verzoek (100 bij 200k-contextmodellen); Claude leest geen metadata; uploads worden niet bewaard.

### 2.3 Kosten van AI-analyse per 1.000 advertenties (bewijstype 5, berekening op de aannames uit de opdracht)

Aannames: tekstclassificatie 2.000 input + 400 output tokens per advertentie; foto-analyse 8 foto's × 1.500 tokens = 12.000 input tokens plus **eigen aanname** 300 output tokens per advertentie; prijzen uit §2.2; USD.

| Scenario | Haiku 4.5 | Sonnet 5 | Opus 5 |
|---|---|---|---|
| Tekst, 1.000 advertenties | **$4,00** (batch $2,00) | **$8,00** (batch $4,00) | $20,00 (batch $10,00) |
| Tekst, met 30 % tokenizer-opslag op input (Sonnet/Opus) | n.v.t. | $9,20 | $23,00 |
| Foto's, 1.000 advertenties, vooraf verkleind (8 × 1.500) | **$13,50** (batch $6,75) | **$27,00** (batch $13,50) | $67,50 (batch $33,75) |
| Foto's, niet verkleind, hoge-resolutie-tier (8 × 2.691) | n.v.t. (standaard-tier) | $46,06 (batch $23,03) | $115,14 (batch $57,57) |
| Jávea-nulmeting eenmalig: 600 advertenties tekst + foto | $10,50 | $21,00 | $52,50 |
| Jávea-maand: 400 tekst-heranalyses + 150 fotosets | **$3,62** (batch $1,81) | **$7,25** (batch $3,62) | $18,12 (batch $9,06) |

Conclusie: op Jávea-schaal zijn de tokenkosten verwaarloosbaar naast de menselijke tijd; het kostenplafond in `tree-ai-agentic-os` (€400/maand) wordt door Deal Hunter alleen geraakt bij landelijke schaal (tienduizenden advertenties per maand). Verklein foto's altijd tot ≤ 1.092 px lange zijde vóór verzending (dan ≤ 1.521 tokens op beide tiers) en gebruik de Batch API voor de nulmeting.

### 2.4 PostGIS als Docker-image versus SQLite

- **`postgis/postgis` (Docker Hub en README van `postgis/docker-postgis`, bewijstype 2):** tags voor PostgreSQL 14–18 met PostGIS 3.5/3.6, ook `-alpine`; start met `docker run … -e POSTGRES_PASSWORD=… postgis/postgis`; extensies `postgis`, `postgis_topology` en `postgis_tiger_geocoder` worden standaard aangemaakt; omgevingsvariabelen werken alleen bij een lege datamap. **Letterlijk: "Supported architecture: `amd64` (x86-64)"** — arm64 wordt op beide pagina's niet genoemd. Deze Mac is arm64 en de Docker-VM is aarch64 (§1.7). Mijn poging om via `docker manifest inspect` te zien of er tóch een arm64-manifest bestaat, bleef hangen (> 120 s) en is niet afgerond. **Status: [te verifiëren]** — dat kan pas met een pull, dus alleen na akkoord van Jan.
- **SQLite (in de venv, bewijstype 3):** R-tree-index werkt (snelle bounding-box-zoekopdrachten), FTS5 (volledige-tekstzoeken in omschrijvingen), JSON-functies. Geen echte geometrie: afstand = eigen haversine-formule (Python), punt-in-polygoon = eigen ray-casting over een lijst coördinaten. Voor Jávea (honderden objecten, enkele duizenden percelen) is dat ruim voldoende; het is pas een probleem bij polygoon-op-polygoon-analyses (overlap, buffers, snijdingen) of bij landelijke schaal.
- **Tussenweg zonder PostGIS:** de bestaande Postgres-image heeft `cube`/`earthdistance` (afstand tussen punten) en `pg_trgm` (fuzzy tekstvergelijking) beschikbaar — maar die database is van Tree AI OS en wordt niet gedeeld; een eigen container met `postgres:16.6-alpine` (al lokaal aanwezig, geen download) zou dezelfde extensies hebben zonder PostGIS.

### 2.5 psycopg-installatie (bewijstype 2)

Officiële installatiedocumentatie (`docs/basic/install.rst` in de psycopg-repository) en PyPI: psycopg 3.3.5 (31-08-2026), "Requires: Python >=3.10", ondersteunt Python "from version 3.10 to 3.15" en PostgreSQL "from version 10 to 18". Drie smaken: `pip install psycopg` (puur Python, "much slower"), `pip install "psycopg[c]"` (bouwt C-extensie, heeft libpq nodig), **`pip install "psycopg[binary]"`** ("Precompiled C extensions, packaged with client libraries") — geen libpq op het systeem nodig. Installatie in de Hermes-venv is een wijziging aan een gedeelde omgeving; beter een eigen venv voor Deal Hunter (`python -m venv`, stdlib, geen download) met daarin alleen wat nodig is — ook dat vraagt Jans akkoord omdat er pakketten worden gedownload.

### 2.6 dHash-beeldvergelijking met Pillow + numpy (bewijstype 2)

De referentie-implementatie in `imagehash/__init__.py` (JohannesBuchner/imagehash, verwijst naar Krawetz' "Kind of Like That"; die blog gaf hier HTTP 403): `image.convert('L').resize((hash_size + 1, hash_size), ANTIALIAS)`, daarna `pixels[:, 1:] > pixels[:, :-1]` (elke pixel vergeleken met zijn linkerbuur), standaard `hash_size = 8` → 8 × 8 = 64 bits. Afstand: `numpy.count_nonzero(self.hash.flatten() != other.hash.flatten())` (Hamming-afstand). Dat is 15 regels Python met alleen Pillow en numpy — de `imagehash`-bibliotheek zelf is niet nodig. Welke afstand "dezelfde foto" betekent (de blog noemt drempels, maar was niet leesbaar) is **[te verifiëren]**; werkhypothese (bewijstype 4): ≤ 6 bits = zelfde foto, 7–12 = twijfel (menselijke controle), > 12 = verschillend; kalibreren op de 4.142 foto-URL's van de BP-feed en de Idealista-dubbels uit R05 (bijv. de zes advertenties van C3XY4395JAV). dHash is gevoelig voor spiegeling en zware bijsnijding; bewaar daarom ook een gespiegelde hash.

### 2.7 Claude Code headless (`claude -p`) met MCP (officiële docs `code.claude.com/docs/en/headless`, bewijstype 2)

- `claude -p "…"` draait niet-interactief; `--output-format json` geeft `result`, `session_id`, en `total_cost_usd` ("client-side estimates"); `--json-schema` dwingt gestructureerde uitvoer af; `--allowedTools` en `--permission-mode` regelen rechten; `--permission-prompts none` "when nobody is available to answer permission prompts, for example in a scheduled job" (vereist v2.1.259+; hier staat 2.1.241 → **eerst updaten** [akkoord Jan]).
- MCP: "Without `--bare`, a `-p` session runs the hooks in a project's `.claude/settings.json` and connects the servers in its `.mcp.json`"; met `--mcp-config <file-or-json>` laad je servers expliciet; `--bare` slaat MCP-ontdekking over en "doesn't use your subscription login" (dan is `ANTHROPIC_API_KEY` nodig). Bij `--mcp-config` wacht Claude Code tot 30 s (`MCP_TIMEOUT`) op de servers; `system/init` meldt `mcp_servers` met status.
- De Idealista-connector is een claude.ai-connector (OAuth op accountniveau). Of een `claude -p`-run zonder `--bare` die connector meeneemt, staat niet letterlijk in de docs en is hier **niet getest** (ik heb bewust geen betaalde headless-run gestart). Bewijstype 7 voor "werkt gepland".

### 2.8 Bezorgkanalen

- **Resend** (prijspagina, bewijstype 1): gratis plan "3,000" e-mails per maand, "100 emails a day", "3 domains"; Pro "$20/mo" voor "50,000". De site heeft `RESEND_API_KEY` als reservekanaal in `alarm.ts` maar niet ingesteld (CLAUDE.md).
- **Teams-webhook** (bewijstype 3): werkt via een Power Automate-workflow met Adaptive Card; antwoordt HTTP 202 zodra aangenomen ("nog geen bewijs dat de kaart in het kanaal staat"). Adres staat in `.env.local` (600).
- **Discord** rechtstreeks (bewijstype 3): waakhondpatroon met bot-token uit `.env`; Hermes-gateway is verbonden als `TREE-Hermes-Bot#0545`.
- **Hermes-cron** (bewijstype 3): `--no-agent --script` bezorgt scriptuitvoer verbatim; profiel-jobs falen nu op ontbrekende gateway-credentials (§1.4).

### 2.9 Catastro (open bronnen; bewijstype 2 tenzij anders vermeld)

- **INSPIRE-diensten** (`catastro.hacienda.gob.es/webinspire/index.html`): WMS `http://ovc.catastro.meh.es/cartografia/INSPIRE/spadgcwms.aspx`; WFS voor percelen `http://ovc.catastro.meh.es/INSPIRE/wfsCP.aspx?`, adressen `wfsAD.aspx?`, gebouwen `wfsBU.aspx?`; ATOM-bulkdownloads per gemeente (`ES.SDGC.CP.atom.xml` enz.), "tweemaal per jaar bijgewerkt". Licentie in `documentos/Licencia.pdf` — het bestand is opgehaald (98 kB) maar de tekst is met de hier beschikbare middelen niet leesbaar (lettertypen zonder tekstlaag, geen PDF-tool): **[te verifiëren]**, zie §11.
- **OVC Coordenadas** (`ovc.catastro.meh.es/ovcservweb/OVCSWLocalizacionRC/OVCCoordenadas.asmx`): operaties `Consulta_RCCOOR` (coördinaat → referencia catastral), `Consulta_RCCOOR_Distancia` (referenties binnen afstand van een punt), `Consulta_CPMRC` (provincie + gemeente + referentie → coördinaten). Parameters staan in de WSDL (niet gelezen).
- **OVC Callejero JSON** (R04, bewijstype 3): `…/OVCWcfCallejero/COVCCallejero.svc/json/ObtenerMunicipios?Provincia=ALICANTE&Municipio=JAVEA` → HTTP 200, "JAVEA/XABIA"; status in R04 "GEVERIFIEERD EN ACTIEF", zonder sleutel; geen waardegegevens.
- Kadastrale referentie + polygoon zijn de sleutel tot de perceelmodule (masterprompt §14). Met de WFS-CP-dienst haal je één GML-polygoon per referentie; parsen kan met `defusedxml`/`xml.etree` (geen `lxml` nodig), punt-in-polygoon met eigen ray-casting (variant 1) of `ST_Contains` (variant 2).

### 2.10 BOE-veilingen (uit R08, bewijstype 2/3)

R08 stelt vast: het Portal de Subastas heeft "geen RSS, geen API en geen downloadlijst"; `robots.txt` `Disallow: /`; toegestane machinale ingang is de BOE-open-data-API van het sumario (`/datosabiertos/api/boe/sumario/AAAAMMDD`, XML, HTTP 200 getest), de RSS-kanalen Sección IV (`boe.php?s=4`) en V-B (`?s=5B`), en de AEAT-lijst `bienes.js` met expliciete licentie "Creative Commons Atribución 4.0 Internacional (CC BY 4.0)" (230 inmuebles op 14-09-2026). Detailpagina's per SUB-id: "CONTRACT OF TOESTEMMING NODIG" (AEBOE). Ratelimits van de BOE-API: ONBEKEND. De veilingadapter in fase B beperkt zich dus tot sumario-API + RSS + AEAT-lijst, met een handmatige stap voor detaildossiers.

### 2.11 Idealista-assistent (uit R01 en eigen test, bewijstype 3/7)

De ingebouwde gids (`guide_idealista_assistant`, 14-09-2026) beschrijft een consumentenassistent ("Where would you like to live?"): zoeken op locatie/budget/kamers, filters, kaart, vergelijken. Over gepland of geautomatiseerd gebruik zegt geen enkele gevonden tekst iets (R01, punt 8: "ONBEKEND; schriftelijke toestemming vragen is de veilige weg"). Idealista's algemene voorwaarden verbieden "robot, spider, scraper u otro medio automático" zonder schriftelijke toestemming (R01, punt 4). Daarom in dit ontwerp: de assistent alleen interactief, tenzij Idealista schriftelijk bevestigt dat een dagelijkse headless-run mag.

---

## 3. Ontwerp a) — de keten uit §27 vertaald naar componenten op deze Mac mini

Kort uitgelegd: een "adapter" is een stukje code dat één bron leest en in ons formaat omzet; "normalisatie" maakt velden gelijk (bijv. `m2` versus `m²`, `Jávea`/`Xàbia`/`JAVEA/XABIA`); "idempotent" betekent dat een run die twee keer draait geen dubbele gegevens oplevert.

| # | Ketenstap (§27) | Component op deze Mac | Bestaand en herbruikbaar? | Nieuw te bouwen | Akkoord van Jan nodig? |
|---|---|---|---|---|---|
| 1 | Bronnen- en rechtenregister | `bronnenregister.json` (deal-hunter, fase A) + tabel `sources` in de Deal Hunter-database met status uit §7 | Register uit fase A | Loader + controle: adapter draait alleen als status `GEVERIFIEERD EN ACTIEF` | Nee |
| 2 | Bronadapters | `adapters/bp_kyero.py`, `adapters/idealista_export.py`, `adapters/boe.py`, `adapters/catastro.py` | Veldenlijst en foutafhandeling uit `kyero.ts`/`feeds.js`; BOE-endpoints uit R08; Catastro-endpoints uit R04/§2.9 | Python-implementaties (§5) | BP: toestemming BP (R05). Idealista: zie §5.2. |
| 3 | Validatie | `validate.py`: verplichte velden, prijs > 0, coördinaten binnen Marina Alta-bbox, XML via `defusedxml` | Krimpdrempel-idee (30 %) uit `run.ts` | Regels + testset | Nee |
| 4 | Normalisatie | `normalize.py`: plaatsnamen (map.ts-tabel), types, oppervlakten (`built`/`plot`/"útil" apart houden), valuta | `map.ts`-normalisatie | Python | Nee |
| 5 | Objectidentiteit | `identity.py`: drie trappen (ref → geo+oppervlakte → dHash) met betrouwbaarheidsniveau; tabel `listing` ↔ `property_object` (n:1) | dHash-algoritme (§2.6) | Python | Nee |
| 6 | Historie en wijzigingsdetectie | tabellen `run`, `listing_snapshot`, `listing_event`; statussen uit §10 | `withdrawn`/`lastSeenAt`-logica uit `run.ts` | Python (§6.1) | Nee |
| 7 | Geografische verrijking | `geo.py`: haversine, bbox via SQLite R-tree, ray-casting; Catastro `Consulta_RCCOOR` per object | SQLite R-tree aanwezig; Catastro OVC geverifieerd | Python; bij variant 2 PostGIS | Variant 2: ja (§4) |
| 8 | Renovatieanalyse | `analyze_renovation.py`: Claude (Haiku/Sonnet) met vaste JSON-uitvoer (`output_config.format`), foto's verkleind; deterministische rekenregels apart (`rules.py`) | `anthropic 0.86` aanwezig; modellenkeuze uit `models.yaml` | Prompts, schema, tests | API-sleutel Anthropic (bestaat via OpenRouter voor Hermes; eigen sleutel: Jan) |
| 9 | Perceel- en stedenbouwkundige analyse | `analyze_plot.py`: referencia catastral → polygoon (WFS-CP) → zone (handmatig geladen zonering, bron R-stroom percelen) → bouwmogelijkhedenoverzicht (§16) | Catastro-diensten | Python; zoneringsdata is een aparte stroom | Nee (data-invoer wel werk) |
| 10 | Veilinganalyse | `analyze_auction.py`: deadlines, waarborg, regime oud/nieuw (R09), harde blokkades | R08/R09-regels | Python | Nee; detailpagina's: toestemming AEBOE |
| 11 | Waardering en financiële berekening | `finance.py`: `Decimal`, `ROUND_HALF_UP` (patroon Tree AI OS), scenario's, maximale koopprijs (§20–22); geen AI in de rekenregels | Rekenstijl Tree AI OS (250 tests op de cent) | Python + tests | Nee |
| 12 | Scoring | `score.py`: versie-genummerde regels (`model_version`), harde blokkades (§23), scores opgeslagen met versie | — | Python | Nee |
| 13 | Menselijke beoordeling | Reviewpagina `127.0.0.1:8710` (FastAPI + Jinja2, naar voorbeeld cockpit 8700) óf GHL-pipeline | `tree-ai-agentic-os` approvals/authority/audit | Pagina + koppeling | Nee (Tailscale-exposure = Gate) |
| 14 | CRM | GHL custom object `deal_hunter_object` + records; associations naar contacten | Bestaande GHL-koppeling (token, host, Version-header) | Adapter `crm_ghl.py` | Scopes/token: ⏸️ Jan in GHL |
| 15 | Dashboard en rapportage | `report.py` (Jinja2 → HTML + MD) + bezorging (§7) | Hermes-cron, Discord-bot-API, Teams-webhook, Resend | Templates + bezorger | Tijdstip/kanaal: Jan |
| — | Planning | `com.tree.deal-hunter.run.plist` (StartCalendarInterval, meerdere tijden/dag) en `com.tree.deal-hunter.report.plist` | launchd-patroon (§1.6) | Twee plists | Installeren = nieuwe dienst → ja |
| — | Bewaking | `alarm.py` (port van `alarm.ts`), waakhond-controle op `last_successful_run` | `alarm.ts`, `waakhond.sh` | Python | Nee |
| — | Bevoegdheden/kill-switch | `killswitch.is_locked()` hergebruikt (lees `~/.hermes/LOCKDOWN`) | `tree-ai-agentic-os` | Import als bibliotheek (read-only) | Nee |

**Ontwerpregel (§27):** één proces, geen zwerm agents. De keten is een reeks functies in één Python-pakket `deal_hunter/` met een SQLite-bestand; AI wordt alleen aangeroepen in stap 8 (en later 9/10 voor documentextractie), nooit voor bedragen of data.

---

## 4. Ontwerp b) — twee varianten voor de kleinste complete versie (fase B)

### 4.1 Variant 1 — nul-installatie

| Laag | Keuze | Bewijs |
|---|---|---|
| Taal/runtime | Python 3.11.15, Hermes-venv `~/.hermes/hermes-agent/venv/bin/python` (zoals `tree-ai-agentic-os/run.sh` doet) | §1.7 |
| Opslag | SQLite-bestand `~/tree-es/deal-hunter/data/dealhunter.db`, `journal_mode=WAL`, R-tree-index op lat/lon-bbox, FTS5 op omschrijvingen | §1.7 |
| XML | `defusedxml.ElementTree` (beschermt tegen entity-bommen; §27 "beveilig parsers") | aanwezig 0.7.1 |
| HTTP | `httpx` met timeouts (60 s zoals `kyero.ts`), eigen `User-Agent`, max 3 herpogingen met exponentiële wachttijd | aanwezig |
| Beeld | `Pillow` + `numpy`: verkleinen (≤ 1.092 px), dHash 64 bits + gespiegelde hash | aanwezig |
| AI | `anthropic` SDK: `messages.create` met `output_config.format` (JSON-schema), Haiku 4.5 voor triage, Sonnet 5 voor kandidaten; Batch API voor de nulmeting | aanwezig 0.86 |
| Rapport | `jinja2` → HTML + Markdown; `zoneinfo` Europe/Madrid | aanwezig |
| Reviewpagina | `fastapi` + `uvicorn` op `127.0.0.1:8710` | aanwezig |
| Planning | launchd `StartCalendarInterval` (bijv. 06:00, 12:00, 18:00 verwerking; rapport op Jans tijdstip) | §1.6 |
| Tests | `pytest` | aanwezig |

**Beperkingen van variant 1**
- Geo: alleen punten en eigen ray-casting; geen buffers/overlap; perceelpolygonen worden als coördinatenlijst in JSON opgeslagen.
- Eén schrijver tegelijk (SQLite); verwerkingsrun en reviewpagina moeten korte transacties gebruiken. Voor Jávea (honderden objecten) geen probleem.
- Geen `pg_trgm`: fuzzy tekstvergelijking via eigen normalisatie + FTS5.
- Gedeelde venv: elke toekomstige Hermes-upgrade kan pakketversies wijzigen; leg de gebruikte versies vast in `requirements.txt` (documentatie, zoals `tree-ai-agentic-os` doet) en test na elke Hermes-update.
- Geen PDF-verwerking (veilingdocumenten, Catastro-licentie): tekstextractie uit PDF's moet via de Anthropic API (PDF als `document`-blok) of wacht op een PDF-bibliotheek (akkoord).

### 4.2 Variant 2 — met akkoord: eigen Postgres + PostGIS-container en psycopg

| Laag | Keuze |
|---|---|
| Database | Eigen container `deal-hunter-postgres` (image `postgis/postgis:16-3.5` of `-alpine`), poort `127.0.0.1:5434`, eigen volume, eigen compose-bestand in `~/tree-es/deal-hunter/infra/` — **nooit** de Tree AI OS-database |
| Driver | `psycopg[binary]` in een **eigen** venv (`python -m venv ~/tree-es/deal-hunter/.venv`, stdlib) zodat de Hermes-venv onaangeroerd blijft |
| Geo | `geometry(Point,4326)` met GiST-index, `ST_DWithin`, `ST_Contains` op kadastrale polygonen (`ST_GeomFromGML` op de WFS-uitvoer), `ST_Area`, buffers |
| Tekst | `pg_trgm` voor fuzzy vergelijking van omschrijvingen en straatnamen |
| Back-up | `pg_dump | gzip` nachtelijk, retentie 14 — kopie van `backup.sh` |

**Winst:** echte geometrie voor de perceelmodule (§14–17), gelijktijdig lezen/schrijven, bewezen back-uppatroon, groeipad naar landelijke schaal.
**Prijs:** afhankelijkheid van Docker Desktop (die op 2–3 september 2026 vier nachten stil viel, §1.5); RAM (Docker-VM heeft 7,65 GiB voor alle containers); één dienst extra in de waakhond; arm64-geschiktheid van het image **[te verifiëren]** (Docker Hub noemt alleen amd64; emulatie op Apple Silicon is mogelijk maar traag en niet getest); installatie = download van image én pakketten → expliciet akkoord van Jan (regel 1).

### 4.3 Aanbeveling

**Fase B in variant 1.** Redenen: (1) alle benodigde stukken zijn er al en getest aanwezig; (2) de perceelmodule heeft in fase B eerst *identificatie* nodig (referencia catastral, polygoon ophalen en tonen), geen zware geometrie; (3) één SQLite-bestand is eenvoudig te back-uppen en te herstellen; (4) het vermijdt een tweede Docker-afhankelijkheid op een machine die daar net een incident mee had. Bouw een dunne opslaglaag (`store.py` met functies als `upsert_listing`, `find_within_radius`, `objects_changed_since`) zodat de overstap naar variant 2 een vervanging van één module is, niet een herbouw.

**Overstapmoment naar variant 2 (Gate-besluit van Jan):** zodra de perceelmodule polygonen gaat snijden of bufferen (fase C/D), of zodra de database meer dan ongeveer 50.000 advertenties/snapshots bevat, of zodra meerdere processen tegelijk moeten schrijven. Vóór dat besluit: arm64-test van het PostGIS-image (één pull na akkoord).

---

## 5. Ontwerp c) — bronadapters voor fase B

### 5.1 Background Properties (Kyero v3 XML)

Twee manieren:

| Optie | Hoe | Voordeel | Nadeel |
|---|---|---|---|
| **A. Via de lokale API (poort 3100)** | `GET http://127.0.0.1:3100/api/health` → als `properties > 0` en `lastFetch` vers: pagineer `GET /api/properties?limit=100&page=n` | Geen sleutel nodig in Deal Hunter; geen extra last op BP; nul wijzigingen aan de dienst | Alleen de laatste momentopname; velden `_feed`/`_commission`/`_category` ontbreken in de uitvoer (commissie zit wél in het TREE-nummer van de site, maar niet in deze API); na een mislukte ronde staat de API op 0 objecten tot het volgende hele uur (bewezen 14-09) — de adapter moet dat als BRON NIET BEREIKBAAR behandelen, niet als "alles verdwenen" |
| **B. Rechtstreeks de feed lezen (Python)** | `httpx.get(BP_FEED_ALL)` (export 36) plus 26/27 voor het commissielabel — dezelfde keuze als de website; URL's in `~/tree-es/deal-hunter/.env` (rechten 600) | Volledige velden en commissieklasse; eigen tempo (1–2× per dag is genoeg voor een dagrapport); eigen foutafhandeling | Sleutels op een tweede plek; extra verzoeken aan BP (de site vraagt al elke 2 uur, de API elk uur) |

**Aanbeveling:** herschrijven in Python (optie B), niet `feeds.js` hergebruiken: de Node-code heeft geen opslag, geen krimpdrempel en geen historie, en `xml2js` verschilt van wat we in Python nodig hebben; de *veldenlijst* en *dedupe-regel* (hoogste commissie wint) nemen we wél letterlijk over. Optie A als nul-sleutel-start voor de allereerste tests. Vóór productiegebruik: schriftelijke bevestiging van BP over opslag, AI-analyse en beeldvergelijking (R05: CONTRACT OF TOESTEMMING NODIG).

Idempotentie: een BP-run schrijft `listing_snapshot(run_id, source='bp', source_ref=ref, content_hash, raw_json)`; `content_hash` = SHA-256 over de genormaliseerde velden zonder volgorde-afhankelijkheid (JSON met gesorteerde sleutels). Dezelfde feed twee keer inlezen geeft dezelfde hash en dus geen nieuw event.

### 5.2 Idealista-assistent (officiële MCP)

**Waarom een launchd-script dit niet kan.** De MCP-server van Idealista is een claude.ai-connector: hij wordt aangeroepen door een Claude-sessie die met Jans account is ingelogd, en de tool zit "in het gesprek" (§1.7: `claude.ai idealista … ✔ Connected`). Een gewoon Python-script heeft die sessie niet en geen eigen toegang tot `mcp-app.idealista.com`; er is geen API-sleutel of gedocumenteerde HTTP-interface voor derden (R01). Een launchd-taak kan dus niet "even de assistent bevragen".

| Optie | Werking | Wat vaststaat | Wat niet vaststaat |
|---|---|---|---|
| 1. `claude -p` headless | launchd start `claude -p "<zoekopdracht>" --output-format json --json-schema <schema> --allowedTools "mcp__…__search_properties,mcp__…__property_detail"`; script parseert de JSON | CLI en vlaggen bestaan (§2.7); de connector is verbonden in deze omgeving | Of de claude.ai-connector in een `-p`-run zonder `--bare` beschikbaar is (niet getest); of Idealista dit gepland toestaat (ONBEKEND, R01); kosten per run (abonnement vs. API); `--permission-prompts none` vraagt CLI ≥ 2.1.259 |
| 2. Interactieve ronde | Jan of een agent opent 1–2× per week een Claude-sessie in `~/tree-es/deal-hunter`, draait de vaste zoekopdrachten (casas "para reformar", terrenos) en laat de resultaten als `data/idealista/YYYY-MM-DD.json` wegschrijven; de adapter leest die map | Werkt vandaag al (70 + 238 resultaten gezien, bewijstype 3); binnen het bedoelde gebruik van een assistent | Handwerk (± 15 min/ronde); maximaal 50 resultaten per aanroep, geen paginering gezien |
| 3. Officiële Search API | Aanvraag bij developers.idealista.com; daarna een normale HTTP-adapter met sleutel | Route bestaat (R01) | Toekenning, voorwaarden, kosten (ONBEKEND) |

**Aanbeveling:** optie 2 voor fase B (bewijs in Jávea), optie 3 direct aanvragen, optie 1 alleen als Idealista schriftelijk bevestigt dat gepland gebruik mag — dan is het een besluit van Jan (kosten + voorwaarden). Ongeacht de optie: de adapter bewaart `propertyCode`, prijs, `formerPrice`/percentage, m², kamers, lat/lon (benaderend), beschrijving, `detailedType`, `status`, en de URL **zonder** utm-parameters als sleutel (met utm-parameters als weergave-URL).

### 5.3 BOE-veilingen (afhankelijk van R08)

Adapter in drie delen, alle zonder scraping van het veilingportaal:
1. `boe_sumario.py`: dagelijks `GET https://www.boe.es/datosabiertos/api/boe/sumario/AAAAMMDD` (header `Accept: application/xml`), Sección IV en V-B filteren op provincie Alicante/plaatsnamen Marina Alta; per item `identificador`, `titulo`, `url_xml`.
2. `boe_rss.py`: `boe.php?s=4` en `?s=5B` als snelle signalering (RSS via `defusedxml`).
3. `aeat_bienes.py`: de AEAT-lijst `bienes.js` (CC BY 4.0, bronvermelding verplicht) parsen; bevat kadaster + coördinaten + einddatum (R08). Structuurwijziging → alarm.
Detailpagina's op `subastas.boe.es` blijven handmatig tot de AEBOE toestemming geeft; het dossier krijgt dan een taak "SUB-id handmatig ophalen" in de reviewpagina. Ratelimits van de BOE-API zijn onbekend: 1 verzoek per dag per sumario, geen bulk.

### 5.4 Catastro (open)

- Per object met coördinaten: `Consulta_RCCOOR` (SOAP, of de JSON-variant van de OVC-diensten zoals in R04) → referencia catastral (met onzekerheidsmarge: de pin van een advertentie is benaderend; bewaar de afstand en markeer > 25 m als "te controleren").
- Per referentie: WFS-CP `GetFeature` → GML-polygoon; opslaan als coördinatenlijst (variant 1) of geometrie (variant 2). ATOM-bulkdownload van de gemeente Xàbia kan als nulmeting (twee updates per jaar).
- Licentie/bronvermelding: **[te verifiëren]** in `Licencia.pdf` (§11). Tot die tijd: alleen intern gebruik, bronvermelding "Dirección General del Catastro" in elk dossier.

---

## 6. Ontwerp d) — wijzigingsdetectie, dedupe, nulmeting, idempotentie, logging, alarm, kosten, back-up, secrets

### 6.1 Wijzigingsdetectie op momentopname-feeds

De BP-feed en de Idealista-export zijn momentopnamen: ze zeggen wat er *nu* staat, niet wat er veranderde. Detectie gebeurt dus door vergelijking met de vorige geslaagde run.

| Status (§10) | Regel | Let op |
|---|---|---|
| NIEUW GEPUBLICEERD | `source_published_at` (BP: `date`-veld; Idealista: geen datum → nooit deze status) ligt binnen 48 uur én de advertentie was nog niet bekend | Feed `date` kan de datum van de laatste wijziging zijn — als [te verifiëren] markeren |
| NIEUW DOOR ONS ONTDEKT | Advertentie niet in vorige geslaagde run, wel in deze | Bij de nulmeting krijgt álles deze status; dat is expliciet zo gelabeld |
| PRIJS GEWIJZIGD | `price` verschilt van de laatste snapshot (drempel 0: elke wijziging loggen; rapportdrempel ≥ 2 % of ≥ €10.000 instelbaar) | Idealista levert `formerPrice` — als extra bron van historie opslaan |
| STATUS GEWIJZIGD | Idealista `status` of BP `new_build`/type verandert | BP heeft geen statusveld |
| DOCUMENTEN GEWIJZIGD | Alleen bij veilingen: `url_xml`/edicto-versie verschilt | — |
| OPNIEUW AANGEBODEN | Eerder NIET MEER GEVONDEN, nu opnieuw aanwezig (zelfde `source_ref` of dedupe-match) | Telt als herpublicatie (§11) |
| NIET MEER GEVONDEN | Afwezig in **twee** opeenvolgende geslaagde runs van dezelfde bron | Nooit na een mislukte run (§6.6); nooit "verkocht" noemen |
| DOOR BRON ALS VERKOCHT GEMELD | Alleen als een bron dat expliciet zegt (geen van de fase-B-bronnen doet dat) | — |
| BRON NIET BEREIKBAAR | HTTP-fout, DNS-fout, XML zonder `property`-elementen, of krimp > drempel | Run wordt als `failed` gemarkeerd; snapshots van die bron worden niet geschreven |

Tijdstempels per advertentie (§10): `source_published_at`, `source_modified_at`, `first_seen_at`, `last_successful_fetch_at`, `last_seen_at`, `analysis_completed_at` — allemaal in UTC opgeslagen, in `Europe/Madrid` getoond.

### 6.2 Deduplicatie in drie trappen (§11)

1. **Referentie:** zelfde bron + zelfde `source_ref` → zelfde advertentie (niet: zelfde object). Over bronnen heen: BP-`ref` komt soms letterlijk terug in Idealista-teksten (R05 vond "C3XY4395JAV" in zes advertenties) → regex op ref-patronen in omschrijvingen, betrouwbaarheid hoog.
2. **Coördinaat + oppervlakte:** afstand ≤ 150 m (Idealista-pins zijn benaderend) én `built` binnen ±5 % én `plot` binnen ±10 % (of beide onbekend) én zelfde type → kandidaat, betrouwbaarheid middel. Nooit samenvoegen op alleen "zelfde urbanisatie + vergelijkbare maat" (§11); dat is precies wat deze trap alleen niet mag doen — daarom trap 3.
3. **dHash op foto's:** per advertentie de hashes van maximaal 8 foto's (verkleind, grijs, 9×8); twee advertenties met ≥ 2 foto's op Hamming-afstand ≤ 6 → zelfde object, betrouwbaarheid hoog; 1 foto of afstand 7–12 → "twijfel, menselijke controle". Renders versus foto's van bestaande bebouwing (§28) worden zo niet herkend — dat is een AI-classificatievraag in stap 8 ("is dit een render?").

Resultaat: tabel `property_object` met `match_confidence` en een lijst gekoppelde advertenties; prijsverschillen en tegenstrijdige oppervlakten blijven per advertentie zichtbaar (§11).

### 6.3 Nulmeting

Eerste run per bron: alle advertenties krijgen `first_seen_at = run.started_at`, status NIEUW DOOR ONS ONTDEKT, en het rapport noemt de nulmeting expliciet ("225 advertenties uit BP, 56 in Jávea — nulmeting, geen nieuwe publicaties"). AI-analyse van de nulmeting via de Batch API (−50 %). De Idealista-nulmeting is de export van de eerste interactieve ronde.

### 6.4 Idempotentie en versiebeheer

- Elke run krijgt `run_id` (UUID), `source`, `started_at`, `finished_at`, `status` (`ok`/`failed`/`partial`), `items_received`, `items_unique`, `error`.
- Snapshots: `UNIQUE(source, source_ref, content_hash)`; een ongewijzigde advertentie levert geen nieuwe rij, alleen `last_seen_at` bijgewerkt.
- Analyses: `UNIQUE(listing_id, content_hash, analysis_version)`; heranalyse alleen bij materiële wijziging (prijs, tekst, foto's) of nieuwe `analysis_version` (§10 "Heranalyseer alleen materiële wijzigingen").
- Scoring: `score(model_version, inputs_hash)`; oude scores blijven staan (§26: modelversies bewaren).
- Code in git (`~/tree-es/deal-hunter/` heeft nog geen repo; aanmaken, `.env` en `data/` in `.gitignore`).

### 6.5 Logging

- Per run een regel in `logs/runs.jsonl` (JSON per regel: run_id, bron, aantallen, duur, fouten) plus de tabel `run`.
- launchd `StandardOutPath`/`StandardErrorPath` naar `logs/launchd.log` (patroon §1.6).
- Nooit sleutels of volledige feed-URL's loggen (les uit de opdracht: de bestaande logs bevatten feed-URL's met sleutel).

### 6.6 Bronuitval-alarm (hergebruik `alarm.ts`)

`alarm.py` met dezelfde regels: onderwerp, tekst, ernst (`kritiek`/`waarschuwing`), dempingssleutel (30 min), altijd `var/alarm.log` met `[bezorgd]`/`[NIET BEZORGD]`; kanaalvolgorde: 1) `ALARM_WEBHOOK_URL` (Teams via Power Automate met Adaptive Card, of Discord/Slack), 2) Resend, 3) niets via het systeem dat zelf verdacht is. Alarmvoorwaarden: bron 2× achtereen mislukt; krimp > 30 %; run duurt > 30 min; AI-kosten per run > limiet; rapport niet bezorgd vóór tijdstip + 30 min. Aanvullend een waakhondcontrole (`com.tree.ai-os.waakhond`-stijl, eigen plist) die `last_successful_run` ouder dan 26 uur meldt — "geen nieuwe kansen" en "geen nieuwe gegevens" zijn verschillende meldingen (§10).

### 6.7 Kostenlimieten

- Per run een tokenbudget (`MAX_INPUT_TOKENS_PER_RUN`, bijv. 2 miljoen ≈ $2–4) en per maand een plafond in `.env`; de SDK-`usage` van elk antwoord wordt opgeteld en als `cost_ledger`-regel (agent `DEAL-HUNTER`, merk `tree`) in `tree-ai-agentic-os` geschreven — via zijn API `POST /api/costs` als de cockpit draait, anders in de eigen database met latere synchronisatie. Het OS-plafond van €400/maand blijft leidend.
- Foto's altijd verkleinen (§2.2); nulmeting via Batch API; Haiku 4.5 voor de eerste triage, Sonnet 5 alleen voor advertenties die de triage overleven.

### 6.8 Back-up

- Variant 1: nachtelijk `sqlite3 … ".backup 'backups/dealhunter-YYYY-MM-DD.db'"` (of Python `Connection.backup()`), gzip, retentie 14 — kopie van het `backup.sh`-patroon; bestanden in `data/` (foto-hashes, exports) mee in een tar. Plist `StartCalendarInterval` 03:45 (na de Tree AI OS-back-up). Zodra de 2 TB-USB-SSD er is (open punt in ~/CLAUDE.md): `BACKUP_DIR` daarheen.
- Variant 2: `pg_dump` van de eigen container, zelfde retentie.
- Hersteltest hoort bij de acceptatie (§9.4).

### 6.9 Secrets

- Eén bestand `~/tree-es/deal-hunter/.env`, rechten `600` (`chmod 600`), nooit in git, met `.env.example` als sjabloon zonder waarden (patroon `~/tree-ai-os/.env` / `.env.example`, §1.5). Inhoud: `BP_FEED_ALL`, `BP_FEED_COMMISSION_HIGH`, `BP_FEED_COMMISSION_STANDARD` (dezelfde namen als de site), `ANTHROPIC_API_KEY`, `ALARM_WEBHOOK_URL`, `RESEND_API_KEY`, `GHL_TOKEN`, `GHL_LOCATION_ID`, `DISCORD_BOT_TOKEN` (alleen als rechtstreekse bezorging wordt gekozen).
- Niet via launchd `EnvironmentVariables` (plists zijn wereld-leesbaar, `-rw-r--r--`); het script laadt `.env` zelf.
- Sleutels komen nooit in prompts, rapporten, logs of de database.

---

## 7. Ontwerp e) — dagelijks ochtendrapport (§24)

**Generatie.** `report.py` bouwt uit de database één datastructuur en rendert twee Jinja2-sjablonen: `rapport.html.j2` (voor Jan, TREE-huisstijl, mobiel leesbaar) en `rapport.md.j2` (voor Discord/Telegram/e-mail-tekst). Drie niveaus exact als §24:
- Niveau 1: managementsamenvatting — wat vraagt aandacht, nieuwe kansen, materiële wijzigingen, naderende deadlines (veilingen), bronnen die onvolledig of niet bereikbaar waren.
- Niveau 2: gerangschikte selecties per categorie (renovatie, percelen, veiling/bijzondere verkoop, prijswijzigingen, commerciële renovatiekansen, onderzoeksdossiers met ontbrekende informatie) — geen opvulling: als de score onder de drempel blijft, staat er "geen sterke kansen vandaag".
- Niveau 3: volledig overzicht met filters en dossierverwijzingen (link naar de reviewpagina).
- Telblok: advertenties ontvangen, unieke objecten, nieuwe publicaties, nieuwe ontdekkingen, wijzigingen, relevante kandidaten, openstaande controles, bronactualiteit (per bron: laatste geslaagde run, leeftijd).
- Slot: prioriteiten "welk object, welke actie, waarom, door wie, vóór wanneer".

**Tijdzone.** Alle tijden via `zoneinfo.ZoneInfo("Europe/Madrid")` (werkt in de venv, §1.7); opslag in UTC.

**Bezorging — vier kanalen, in volgorde van eenvoud:**

| Kanaal | Hoe | Status |
|---|---|---|
| Hermes-cron, zonder LLM | `hermes cron create "0 7 * * *" --name "Deal Hunter ochtendrapport" --no-agent --script deal-hunter-rapport.sh --deliver discord:<kanaal-id>`; het script drukt de Markdown af | Mechanisme bestaat (§1.4); bezorging vanuit een profiel faalt nu (`blocked_config`); vanuit het default-profiel ongetest → eerst bewijzen |
| Discord rechtstreeks | Bot-API met `DISCORD_BOT_TOKEN` (waakhondpatroon), bericht ≤ 2.000 tekens + HTML als bijlage | Werkt voor de waakhond (bewijstype 3) |
| Teams-webhook | Adaptive Card met samenvatting + link | Werkt voor de site-alarmen (bewijstype 3) |
| E-mail via Resend | HTML-rapport als mail; gratis plan 3.000/maand, 100/dag | Sleutel niet ingesteld (reserve) |

**Tijdstip:** beslissing van Jan (§24: "Leg het exacte aflevermoment en kanaal vast voordat het productieschema wordt geactiveerd"). Technisch voorstel: verwerkingsrun 05:30, rapport 07:00 Europe/Madrid via `StartCalendarInterval`; Hermes' eigen G-CEO-routine loopt om 09:00 (weekdagen) — een rapport vóór 09:00 kan daar als input dienen. Urgente meldingen (§27: prijswijziging op gevolgd object, nieuwe sterke kandidaat, veilingdeadline binnen 5 dagen) gaan via hetzelfde alarmkanaal, met demping.

---

## 8. Ontwerp f) — menselijke beoordeling en CRM

### 8.1 Optie 1: GoHighLevel custom objects (CRM van waarheid, ADR-0014)

- Schema `deal_hunter_object` (eenmalig `POST /objects/`): velden o.a. `object_id`, `route` (A/B/C/D), `status_object`, `status_onderzoek`, `status_investering`, `status_contact`, `status_veiling` (vijf gescheiden statussen, §26), `score`, `score_version`, `max_koopprijs`, `bron_urls`, `dossier_url`, `blokkades`.
- Per kandidaat een record (`POST /objects/{schemaKey}/records`), updates idempotent via `PUT …/records/{id}` met ons `object_id` als zoeksleutel (`POST …/records/search`). Makelaar/instantie als contact via associations (spec `associations.json`, niet gelezen: [te verifiëren]). Nooit particuliere eigenaren als contact aanmaken zonder bewijs van interesse (§26, regel 9 van de opdracht).
- Voorwaarden: token met scopes `objects/schema.write`, `objects/record.write`, `objects/record.readonly` (⏸️ Jan in GHL); rate limits onbekend → wachtrij met maximaal 1 verzoek/seconde en herpoging bij 429.

### 8.2 Optie 2: lichte reviewpagina op localhost/Tailscale

FastAPI + Jinja2 op `127.0.0.1:8710`, naar het voorbeeld van de cockpit `tree-ai-agentic-os` (`api/app.py`): lijst kandidaten met filters, dossierpagina (advertenties, foto's met hash-matches, kaart-link, Catastro-referentie, analyse-JSON, financiële scenario's, blokkades), knoppen *interessant / afwijzen (reden) / onderzoeken / taak aanmaken*. Beslissingen gaan in `audit_log` en voeden §26 ("leer van onze werkelijke feedback"). Tailscale-exposure is een aparte stap (zoals bij de cockpit: Gate).

**Aanbeveling:** fase B optie 2 (snel, geen externe afhankelijkheid, alle velden zichtbaar); fase C optie 1 erbij voor opvolging en contactmomenten, waarbij de reviewpagina de *onderzoeksstatus* houdt en GHL de *commerciële status* — twee systemen, twee statussen, geen dubbele waarheid.

### 8.3 Approvals en kill-switch

- Vóór elke run: `if killswitch.is_locked(): log("LOCKDOWN") ; exit 0` — geen bezorging, geen AI-aanroep, geen CRM-schrijfactie. Marker `~/.hermes/LOCKDOWN` (afwezig op 14-09-2026).
- Elke actie met externe werking (mail aan makelaar, GHL-record aanmaken/wijzigen, bod, betaling, document opvragen tegen betaling) loopt door `authority.evaluate(ActionRequest(actor="DEAL-HUNTER", brand="tree", external=True, cost_eur=…))` → altijd minstens A3 → `approvals.create(...)` → Jan beslist in de cockpit of reviewpagina → pas dan uitvoeren. Lezen, analyseren en rapporteren is A1/A2 (gelogd).
- Biedingen, betalingen, registraties op veilingportalen: nooit geautomatiseerd (§27, R08). De reviewpagina toont hooguit een *voorbereid* biedvoorstel met alle blokkades uit §23.
- Merk: alle Deal Hunter-acties onder `brand="tree"`; als Jan besluit dat aankopen via Rocksure lopen, is dat een aparte taakenvelop met `brand="rocksure"` — nooit beide in één actie (engine blokkeert merkvermenging).

---

## 9. Ontwerp g) — kostenraming en acceptatietests

### 9.1 Ontwikkeluren per fase (bewijstype 4/5: inschatting op basis van de componentenlijst; geen offerte)

| Fase | Doel | Afhankelijkheden | Opleveringen | Uren (schatting) | Risico's | Acceptatie |
|---|---|---|---|---|---|---|
| **A** (loopt) | Bronnen en kader | — | 17 stromen, bronnenregister, vijf deliverables | grotendeels gedaan; afronding 10–20 u | Rechten blijven ONBEKEND (BP, Idealista, Catastro-licentie) | Register compleet met statussen; Jans investeringskader ingevuld |
| **B** | Bewijs in Jávea (variant 1) | Toestemming BP; Anthropic-sleutel; Idealista-export handmatig | Pakket `deal_hunter/` met BP-adapter, Idealista-import, BOE-sumario/RSS/AEAT-adapter, Catastro-identificatie, dedupe, historie, AI-triage, scoring v1, reviewpagina, ochtendrapport (handmatig gestart), tests | **60–90 u** | Dedupe-drempels verkeerd; benaderende Idealista-pins; feeduitval | Acceptatietests 1–6 en 8 groen; nulmeting + 14 dagen dagrapporten bekeken door Jan |
| **C** | Betrouwbare dagelijkse operatie | Besluit tijdstip/kanaal; GHL-scopes; eventueel variant 2 | launchd-plists, alarm + waakhond, back-up + hersteltest, GHL-koppeling, urgente meldingen, dossier-sjabloon (§25), feedbacklus | **80–120 u** | Bezorging Discord (nu kapot in profielen); GHL-limieten onbekend; Docker-afhankelijkheid bij variant 2 | Alle 13 tests groen; 30 dagen zonder stille storing; hersteltest geslaagd |
| **D** | Groei en verbetering | Datalicenties (offertes R04), Idealista-API, PostGIS | Extra bronnen, geografische uitbreiding, kalibratie scoring op werkelijke uitkomsten, waardering met AVM/comparables | ONBEKEND (afhankelijk van bronnen) | Kosten datalicenties; schaal | Kosten per gekwalificeerde kans en foutieve-signaalratio gemeten en dalend |

### 9.2 Maandelijkse kosten (variant 1, Jávea)

| Post | Bedrag | Bewijs |
|---|---|---|
| Hosting | €0 extra (eigen Mac mini, al 24/7 aan) | 3 |
| AI-tokens (Haiku-triage + Sonnet voor kandidaten, foto's verkleind) | < $10/maand na de nulmeting ($10–25 eenmalig) | 5 (§2.3) |
| Idealista-assistent | abonnement Claude (bestaat); gepland gebruik: ONBEKEND | 7 |
| Datalicenties (Casafari, Brainsre, Accumin/Tinsa, idealista/data, MLS-netwerken) | ONBEKEND — alle op offerte; alleen Tinsa Radar heeft prijzen (€29/studie, €99 of €259/maand) — geen objectbron | R04 |
| E-mail (Resend) | €0 tot 3.000/maand | 1 |
| Docker/PostGIS (variant 2) | €0 licentie; wel beheertijd | 2 |
| Beheer/onderhoud | ± 4–8 u/maand (schatting) | 4 |

### 9.3 Kosten per dossier (buiten software)

> Aanvulling 15-09-2026: zie §11a.2 voor het arancel van de nota simple (3,005061 €/finca, RD 1427/1989) en het wettelijke verbod op tariefrichtlijnen voor architecten en advocaten (art. 14 Ley 2/1974), overgenomen uit R11 en R14.

| Post | Bedrag | Status |
|---|---|---|
| Nota simple (Registro de la Propiedad, online) | ONBEKEND — de sede van de Registradores heeft een "Nota simple"-ingang, maar de tarievenpagina was niet bereikbaar (404 op de geprobeerde URL) | 7 — [te verifiëren] |
| Certificación de cargas bij veiling | Via het portaal/LAJ (R09, art. 656 LEC); kosten voor bieder: ONBEKEND | 7 |
| Architect (bouwmogelijkhedenoverzicht §16, cédula/informe urbanístico) | ONBEKEND — offerte per dossier | 7 |
| Advocaat (veilingdossier §19, lasten, bezetting) | ONBEKEND — offerte per dossier | 7 |
| Taxatie (Tinsa Radar als second opinion) | €29 per studie | R04 (1) |
| Waarborgsom veiling | 20 % veilingwaarde (min. €1.000) nieuw regime / 5 % oud; AEAT 5 %; TGSS 25 % | R09 (2) |

### 9.4 Acceptatietests (§28) als concrete testlijst

Testdata zichtbaar gescheiden van marktdata: fixtures in `tests/fixtures/` met prefix `TEST-`, en een aparte database `data/test.db`.

| # | Test (§28) | Fixture / stap | Verwacht |
|---|---|---|---|
| 1 | Dubbele advertenties | Twee advertenties met verschillende refs, zelfde coördinaten ±50 m, oppervlakte ±3 %, 3 identieke foto's (dHash 0) | Eén `property_object`, twee advertenties gekoppeld, `match_confidence=hoog`, beide prijzen zichtbaar |
| 2 | Onjuiste locatiepinnen | Advertentie met pin 3 km van de genoemde urbanisatie; tweede met pin in zee | Geo-validatie zet `location_quality=laag`; dedupe trap 2 slaat over; rapport markeert "locatie te controleren" |
| 3 | Verschillende oppervlaktebegrippen | `built` 180 / `plot` 1.200 tegenover een bron met alleen "m²" 1.200 | Velden blijven gescheiden; geen dedupe-match op oppervlakte alleen; `surface_basis` = `built`/`plot`/`onbekend` |
| 4 | Herpublicaties | Zelfde object verdwijnt in run n, verschijnt in run n+3 met nieuwe ref | Status OPNIEUW AANGEBODEN, gekoppeld aan het oude object; `first_seen_at` blijft de oorspronkelijke datum |
| 5 | Lege of onvolledige feeds | Feed met 0 `property`-elementen; feed met 40 % minder items; HTTP 500; DNS-fout | Run `failed`; geen snapshots; geen NIET MEER GEVONDEN; alarm `kritiek` na 2× ; rapport meldt BRON NIET BEREIKBAAR |
| 6 | Verdwenen advertenties | Advertentie afwezig in twee geslaagde runs | NIET MEER GEVONDEN, nooit "verkocht"; na één afwezigheid nog niets |
| 7 | Renders die op bestaande bebouwing lijken | Advertentie met 3D-render als eerste foto | AI-classificatie `is_render=true` met betrouwbaarheid; dossier gemarkeerd "render, bestaande toestand onbekend" |
| 8 | Grondprijzen met voorbeeldwoningen | Perceeladvertentie "villa incluida, precio llave en mano" en één "solo terreno" | `price_scope` = `grond` / `grond+bouw` / `onbekend`; €/m² alleen berekend bij `grond` |
| 9 | Verkeerde perceelkoppelingen | Pin op perceelgrens; twee referenties binnen 25 m | `catastro_confidence=laag`, beide referenties bewaard, taak "handmatig bevestigen" |
| 10 | Plannen die nog niet gelden | Zoneringsrecord met `status=in_tramitación` | Bouwmogelijkhedenoverzicht toont "geen geldend recht"; score krijgt harde blokkade |
| 11 | Beperkte eigendomsrechten | Veilingfixture "50% NUDA PROPIEDAD" (R09) | Harde blokkade voor biedvoorstel; dossier toont aangeboden recht |
| 12 | Onbekende lasten | Certificación ouder dan 6 maanden of ontbrekend | Blokkade "lasten onbekend"; taak "geactualiseerde nota opvragen" (A3) |
| 13 | Gewijzigde of ingetrokken veilingen | Sumario-item verdwijnt of edicto-XML wijzigt | DOCUMENTEN GEWIJZIGD / STATUS GEWIJZIGD; deadline-alarm ingetrokken |
| 14 | Kill-switch | `~/.hermes/LOCKDOWN` aanwezig (testomgeving) | Run stopt vóór netwerk/AI/bezorging; auditregel |
| 15 | Back-up en herstel | Nachtelijke back-up terugzetten in `data/test.db` | Zelfde aantallen objecten en events |
| 16 | Secrets | `grep` over logs, rapporten, database-dump op sleutelpatronen | Nul treffers |
| 17 | Kostenplafond | Simulatie usage > `MAX_INPUT_TOKENS_PER_RUN` | Analyse stopt, alarm `waarschuwing`, run `partial` |

Meetwaarden (§28) die de reviewpagina bijhoudt: brondekking (advertenties per bron per dag), verwerkingsvertraging (run-einde − feedtijd), dedupe-precisie (steekproef door Jan: goed/fout), kwaliteit perceelkoppelingen, bruikbaarheid van kandidaten (interessant/afgewezen + reden), foutieve signalen, onderzoekstijd per bruikbare deal, kosten per gekwalificeerde kans, commerciële uitkomsten.

---

## 10. Beslissingen en acties voor Jan

⏸️ **ACTIE VOOR JAN**
1. **Tijdstip en kanaal van het ochtendrapport** kiezen (voorstel: 07:00 Europe/Madrid, Discord + HTML-link; alternatief Teams of e-mail).
2. **Anthropic-API-sleutel** voor Deal Hunter (eigen sleutel met eigen limiet, los van de OpenRouter-sleutel van Hermes) — of besluiten dat OpenRouter ook hiervoor geldt.
3. **GoHighLevel:** een token/app met scopes `objects/schema.write`, `objects/record.write`, `objects/record.readonly` (fase C).
4. **Toestemming BP** (vragen uit R05) en de **Idealista-API-aanvraag** (R01) versturen — beide zijn voorwaarde vóór gepland gebruik.
5. **Installatie-akkoord** pas bij het overstapmoment: `psycopg[binary]` in een eigen venv en het PostGIS-image (na arm64-test). Nu niet nodig.
6. **Hermes:** laten nakijken waarom cron-bezorging vanuit het G-CEO-profiel naar Discord al 11 keer faalt (`blocked_config`) — dat raakt ook de bezorging van het ochtendrapport als Hermes het kanaal wordt.
7. Claude Code CLI updaten (2.1.241 → ≥ 2.1.259) als de headless-route voor Idealista ooit wordt gekozen (`--permission-prompts none`).

**Open vragen (bewijstype 7):**
- Rate limits van de GHL API en welk authenticatiemodel de `objects/*`-scopes krijgt.
- Draait `postgis/postgis` op arm64/Apple Silicon (native of via emulatie)?
- Toestaan Idealista en BP gepland/geautomatiseerd gebruik, opslag, AI-analyse en beeldvergelijking?
- Licentietekst Catastro INSPIRE (bronvermelding, commercieel hergebruik, bulk).
- Kosten nota simple online, architect en advocaat per dossier.
- Ratelimits BOE-open-data-API.
- Ideale dHash-drempel voor vastgoedfoto's (kalibratie op eigen data).
- Betekenis van het BP-`date`-veld (publicatie of laatste wijziging).

---

## 11. Geblokkeerd of mislukt (niet omzeild)

| Wat | Resultaat |
|---|---|
| `marketplace.gohighlevel.com/docs/ghl/objects/get-object-schema` en `…/rate-limits` | Pagina's tonen alleen een titel zonder JavaScript; niet leesbaar. Alternatief gebruikt: officiële OpenAPI-spec op GitHub. |
| `highlevel.stoplight.io/docs/integrations/` | Lege inhoud (JavaScript-only). |
| `raw.githubusercontent.com/GoHighLevel/highlevel-api-docs/main/apis/objects.json` | HTTP 404 (juiste pad bleek `apps/objects.json`, dat wél gelezen is). |
| `github.com/GoHighLevel/highlevel-api-docs/tree/main/docs` | Laadfout op GitHub ("There was an error while loading"). |
| `psycopg.org/psycopg3/docs/basic/install.html` | HTTP 403. Alternatief: dezelfde tekst als `install.rst` in de psycopg-repository + PyPI. |
| `hackerfactor.com/blog/…/529-Kind-of-Like-That.html` (dHash-origineel) | HTTP 403. Alternatief: implementatie in `imagehash` die ernaar verwijst. |
| `catastro.hacienda.gob.es/webinspire/documentos/Licencia.pdf` | Opgehaald (98 kB) maar tekst niet extraheerbaar: `pdftoppm` ontbreekt, geen PDF-bibliotheek in de venv, en de PDF gebruikt lettertypen zonder leesbare tekstlaag. |
| `docker manifest inspect postgis/postgis:16-3.5` (arm64-check) | Geen antwoord binnen 120 s; als achtergrondtaak niet afgerond. |
| `sede.registradores.org/site/propiedad/nota-simple` | HTTP 404 (URL geraden op basis van het menu "Nota simple"). |
| WebSearch | Sessiebudget (200 zoekopdrachten) was al verbruikt door eerdere stromen; alle webbronnen zijn met WebFetch op bekende officiële URL's opgehaald. |
| Headless-test `claude -p` met de Idealista-connector | Bewust niet uitgevoerd (kosten/voorwaarden onbekend); alleen documentatie gelezen. |

---

## 11a. Aanvulling 15-09-2026

Deze ronde is hervat na een onderbreking. Er is **geen nieuw webonderzoek** gedaan. Aangevuld zijn drie gaten ten opzichte van de opdracht: (1) de actuele stand van de BP-feed en de gevolgen voor normalisatie (opdrachtonderdeel c/d), (2) kosten per dossier voor nota simple, architect en advocaat, en (3) datalicenties "als bekend uit andere stromen" (opdrachtonderdeel g). Punt 1 is zelf gecontroleerd op de eigen, lokale dienst (alleen lezen); punten 2 en 3 zijn overgenomen uit de fase A-rapporten R01, R02, R03, R11 en R14 van 14-09-2026, met de oorspronkelijke bron en het bewijstype zoals daar vastgesteld.

### 11a.1 BP-feed hersteld; plaatsnaam staat er als "Javea" (bewijstype 3, 15-09-2026)

| Controle (lokaal, `curl -sS -m 20`) | Uitkomst |
|---|---|
| `GET http://127.0.0.1:3100/api/health` | `status: ok`, `properties: 225`, `lastFetch: 2026-09-15T00:00:10.914Z` (02:00 Europe/Madrid) |
| `GET /api/properties?town=Javea&limit=100` | `total: 57`; alle 57 met `town` = `"Javea"` (zonder accent) |
| `GET /api/properties?town=Jávea&limit=100` | `total: 0` |
| `GET /api/properties?town=Xàbia&limit=100` | `total: 0` |

**Oorzaak (gelezen in `~/tree-hermes/properties-api/server.js`, regels 53–55):** het filter vergelijkt exact na `toLowerCase()` — `towns.includes(p.town.toLowerCase())` — zonder accenten te verwijderen. "jávea" is voor de computer een ander woord dan "javea". De website vangt dit al op: `map.ts` (regels 60 en 76–80) zet de plaats om met `normaliseTown` en slaat een vaste slug op, met als uitdrukkelijke reden dat de feed morgen "Xàbia" in plaats van "Jávea" kan leveren.

**Bijstellingen van eerdere passages:**
- §1.1 en §5.1 (stand 14-09-2026 22:12: API op 0 objecten) zijn achterhaald: de feed is volgens de opdrachtgever op 14-09-2026 om 23:00 vanzelf hersteld en staat bij mijn controle op 225 objecten. De les blijft staan: een mislukte ronde leegt de lokale API tot de volgende geslaagde ronde, dus de adapter moet `properties = 0` behandelen als BRON NIET BEREIKBAAR.
- §6.3 (voorbeeldtekst nulmeting "56 in Jávea"): de actuele telling is **57** (15-09-2026); de 56 was de meting van 25-08-2026.

**Gevolg voor component 4 (`normalize.py`) — bouwvoorschrift:**
1. Bewaar de ruwe plaatsnaam altijd ongewijzigd (`town_raw`), zodat terug te zien is wat de bron leverde.
2. Maak een vergelijkingssleutel met alleen de standaardbibliotheek: Unicode-normalisatie NFKD, accenttekens weg, kleine letters, alles wat geen letter of cijfer is wordt een streepje. Getest in de Hermes-venv (bewijstype 3): `Javea` en `Jávea` → `javea`; `Xàbia` → `xabia`; `JAVEA/XABIA` en `Jávea/Xàbia` → `javea-xabia`; `El Vergel` → `el-vergel`; `Poble Nou de Benitatxell` → `poble-nou-de-benitatxell`.
3. Accenten weghalen is **niet genoeg**: Castiliaans en Valenciaans zijn verschillende woorden (`javea` ≠ `xabia`, `benitachell` ≠ `poble-nou-de-benitatxell`, `el-vergel` ≠ `el-verger`). Daarom een vaste aliastabel `town_aliases` (sleutel → gemeente), bijvoorbeeld `javea`, `xabia`, `javea-xabia` → één gemeente-id. De tabel is data (in de database of een YAML-bestand), geen code, en elke onbekende sleutel levert een waarschuwing "onbekende plaats" in het ochtendrapport op in plaats van een stille uitval.
4. Filteren en dedupe gebeuren uitsluitend op het gemeente-id, nooit op de ruwe tekst. Welke alias-varianten Idealista, Catastro (`JAVEA/XABIA`, R04) en BOE precies gebruiken, wordt bij de eerste run per bron vastgelegd; varianten die ik niet zelf in een bron heb gezien, staan niet in de tabel.
5. Extra acceptatietest (aanvulling op §9.4):

| # | Test | Fixture / stap | Verwacht |
|---|---|---|---|
| 18 | Plaatsnaamvarianten | Vijf advertenties met `town` = `Javea`, `Jávea`, `Xàbia`, `JAVEA/XABIA`, `Jávea/Xàbia`; één met `Xabiá` (onbekende spelling) | Eerste vijf krijgen hetzelfde gemeente-id en tellen samen; de zesde komt als "onbekende plaats" in het rapport en wordt niet stil weggefilterd |
| 19 | Lege lokale API na mislukte ronde | `/api/health` geeft `properties: 0` of `lastFetch` ouder dan 2 uur | Run `failed` voor bron BP, geen NIET MEER GEVONDEN, alarm volgens §6.6 |

### 11a.2 Kosten per dossier — wat andere stromen hebben gevonden (vervangt de ONBEKEND-regels in §9.3 waar er een bron is)

| Post | Wat vaststaat | Bron (zoals vastgesteld in de genoemde stroom, 14-09-2026) | Bewijstype | Wat nog open is |
|---|---|---|---|---|
| Nota simple (Registro de la Propiedad) | Arancel der registradores, número 4 "Publicidad formal": nota simple informativa **3,005061 € per finca**; certificación de dominio 9,015182 €, de cargas 24,040484 €, negativa de cargas 9,015182 € per finca | Real Decreto 1427/1989, geconsolideerd: https://www.boe.es/buscar/act.php?id=BOE-A-1989-28112 (via R11 §6.1) | 2 | Wat de online bestelling via het Colegio (FLOTI/sede) in de praktijk kost, inclusief toeslagen en btw: **[te verifiëren]** bij de eerste bestelling. Levertijd telematisch "aproximadamente 24 horas" (registradores.org, via R11). Bestellen vraagt een login → ⏸️ Jan. |
| Architect / aparejador | Beroepsorganisaties mogen **geen tariefrichtlijnen** publiceren (art. 14 Ley 2/1974, ingevoegd door Ley 25/2009), dus er bestaat geen officieel tarief | https://www.boe.es/buscar/act.php?id=BOE-A-1974-289 (via R14 §2.3) | 2 (verbod) | Bedrag per dossier: **ONBEKEND** — offerte. Marktindicatie op één platform: honoraria 10–12 % van de bouwsom bij nieuwbouw (habitissimo, bijgewerkt 18-06-2026; bewijstype 1, lage zekerheid). Dat is een projecthonorarium, geen prijs voor een bouwmogelijkhedenoverzicht of informe urbanístico per kandidaat. |
| Advocaat (due diligence, veilingdossier) | Zelfde verbod op tariefrichtlijnen (art. 14 Ley 2/1974) | idem (via R14 §2.3) | 2 (verbod) / 7 (bedrag) | Bedrag per dossier: **ONBEKEND** — offerte. |
| Certificación de cargas bij veiling | Wordt in de procedure door de LAJ bij het register opgevraagd; bij ouder dan 6 maanden een geactualiseerde nota simple (art. 656 LEC) | R09 | 2 | Kosten voor de bieder: ONBEKEND |

**Rekenregel voor het dossiersjabloon (bewijstype 5):** per kandidaat die de reviewstap overleeft minimaal één nota simple per finca (basisarancel 3,01 €, werkelijke online prijs [te verifiëren]); bij een perceel met twee mogelijke referenties (R11-voorbeeld: 2944017 en 2944012) twee notas. Architect en advocaat pas na een besluit van Jan per dossier (A3, want `cost_eur > 0`), nooit automatisch.

### 11a.3 Datalicenties uit andere stromen (vult §9.2, regel "Datalicenties", aan)

| Bron | Kosten | Stroom | Bewijstype | Opmerking voor de architectuur |
|---|---|---|---|---|
| Idealista Search API (developers.idealista.com) | ONBEKEND — alleen op aanvraag, geen gepubliceerde voorwaarden; de vaak genoemde "100 verzoeken per maand" komt alleen uit blogs | R01 | 7 | Adapter pas bouwen na toekenning |
| idealista/data | ONBEKEND — offerte | R01 | 7 | Geen bedrag verzonnen |
| idealista/tools + Market Navigator (professioneel account) | ONBEKEND | R01 | 7 | CONTRACT OF TOESTEMMING NODIG |
| DataVenues (Fotocasa/Habitaclia/Milanuncios) | Niet gepubliceerd; enige openbare prijs is de waarderingswidget: 30 €/maand + btw via Witei | R02 | 1 (widget) / 7 (licentie) | Levering per API niet bewezen; verwacht handmatig gebruik of exports |
| Kyero market data | ONBEKEND (pagina 403) | R03 | 7 | TECHNISCH ONDERZOEK NODIG |
| thinkSPAIN, SpainHouses | Alleen advertentietarieven voor aanbieders (vanaf 25 €/maand resp. 10 €/maand), **geen** leeslicentie | R03 | 1 | Niet bruikbaar als objectbron voor Deal Hunter |
| Casafari, Brainsre, Accumin/Tinsa, MLS-netwerken | ONBEKEND — offerte; Tinsa Radar 29 €/studie, 99 of 259 €/maand (geen objectbron) | R04 | 1 / 7 | Zie §9.2 |

**Conclusie van de aanvulling (bewijstype 4):** de maandbegroting voor fase B blijft zoals in §9.2 (hosting €0, AI < $10); de enige harde externe kosten per dossier die nu met een officiële bron te onderbouwen zijn, zijn de registerkosten volgens het arancel. Alle professionele honoraria en alle datalicenties vragen een offerte en blijven in de kostenraming ONBEKEND.

### 11a.4 Kleine aanvulling bij ontwerp e) — Telegram

§7 noemt Discord als eerste kanaal. De Hermes-CLI kent ook `--deliver telegram` (gelezen in `hermes cron create --help`, §1.4, bewijstype 3). Of cron-bezorging naar Telegram vanuit het default-profiel werkt, is niet getest; dezelfde `blocked_config`-waarschuwing als bij Discord (§1.4) kan gelden. Bewijzen vóór ingebruikname, net als bij Discord.

---

## 12. Bronnenlijst (URL · controledatum · bewijstype)

**Lokaal (alleen gelezen, 14-09-2026, bewijstype 3)**
- `~/tree-hermes/properties-api/server.js`, `feeds.js`, `package.json`, `logs/stderr.log` (regels 4096–4107)
- `~/tree-website/tree-properties/README.md`, `CLAUDE.md`, `src/lib/import/kyero.ts`, `run.ts`, `images.ts`, `map.ts`, `tree-ref.ts`, `src/lib/alarm.ts`, `src/lib/ghl.ts`
- `~/tree-es/tree-ai-agentic-os/README.md`, `os_core/authority.py`, `approvals.py`, `costs.py`, `killswitch.py`, `config.py`, `schema.sql`, `api/app.py`, `requirements.txt`, `run.sh`
- `~/tree-es/hermes-agent-organization/README.md`, `registry/agents.yaml`, `registry/models.yaml`, `registry/tools.yaml`, `operations/runbooks/kill-switch.md`, `scripts/kill-switch.sh`, `operations/changelog/2026-08-28-fase3-gate-c.md`
- `~/.hermes/profiles/g-ceo/cron/jobs.json`, `~/.hermes/cron/jobs.json`, `~/.hermes/logs/agent.log`, `errors.log`; `hermes cron --help`, `hermes cron create --help`
- `~/tree-ai-os/README.md`, `compose.yaml`, `scripts/backup.sh`, `scripts/waakhond.sh`, `.env` (alleen rechten), `.env.example`
- `~/Library/LaunchAgents/com.tree.*.plist`, `launchctl list`
- `~/tree-es/deal-hunter/MASTERPROMPT.md` (§5, 6, 7, 10, 11, 24, 26–29), `CLAUDE.md`; `onderzoek/R01`, `R04`, `R05`, `R08`, `R09` (kruisverwijzingen)
- `~/tree-es/properties/leadgen/docs/marktdata-bronnen.md`
- Systeem: `uname -m`, `sysctl`, `df`, `docker info`, `docker images`, `docker exec … pg_available_extensions`, venv-import-test, SQLite `pragma compile_options`, `claude --version`, `claude mcp list`, `claude --help`

**Lokaal, aanvulling 15-09-2026 (alleen gelezen, bewijstype 3)**
- `http://127.0.0.1:3100/api/health` en `/api/properties?town=Javea|Jávea|Xàbia&limit=100` (eigen dienst `com.tree.properties-api`)
- `~/tree-hermes/properties-api/server.js` regels 47–55 (townfilter); `~/tree-website/tree-properties/src/lib/import/map.ts` regels 60–80 (`normaliseTown`, `workAreaSlug`)
- Hermes-venv: test van `unicodedata`-normalisatie van plaatsnamen
- `onderzoek/R01-idealista.md`, `R02-adevinta-fotocasa-habitaclia-datavenues.md`, `R03-overige-portalen.md`, `R09-veilingen-juridisch-procedure.md`, `R11-catastro-registro-perceelidentificatie.md`, `R14-financieel-fiscaal-kostenkengetallen.md` (kruisverwijzingen, stand 14-09-2026)

**Web, overgenomen uit andere stromen voor §11a (controledatum van die stroom: 14-09-2026)**
- https://www.boe.es/buscar/act.php?id=BOE-A-1989-28112 — Arancel de los Registradores (RD 1427/1989), número 4 · 2 (via R11)
- https://www.registradores.org/el-colegio/registro-de-la-propiedad — nota simple telematisch ± 24 uur · 2 (via R11)
- https://www.boe.es/buscar/act.php?id=BOE-A-1974-289 — art. 14 Ley 2/1974, verbod op tariefrichtlijnen · 2 (via R14)
- https://www.habitissimo.es/presupuestos/construccion-casas — honoraria 10–12 % (marktindicatie) · 1 (via R14)
- faq.witei.com — DataVenues-widget 30 €/maand + btw · 1 (via R02)

**Web (14-09-2026)**
1. https://platform.claude.com/docs/en/about-claude/pricing — prijzen, caching, batch, tokenizer-noot · 2
2. https://platform.claude.com/docs/en/build-with-claude/vision — beeldtokens, resolutie-tiers, limieten · 2
3. https://code.claude.com/docs/en/headless — `claude -p`, `--mcp-config`, `--bare`, `--permission-prompts` · 2
4. https://raw.githubusercontent.com/GoHighLevel/highlevel-api-docs/main/apps/objects.json — Custom Objects OpenAPI · 2
5. https://github.com/GoHighLevel/highlevel-api-docs en `/tree/main/apps` — repositorybeschrijving en bestandslijst · 2
6. https://hub.docker.com/r/postgis/postgis en https://raw.githubusercontent.com/postgis/docker-postgis/master/README.md — tags, "Supported architecture: amd64" · 2
7. https://pypi.org/project/psycopg/ — versie 3.3.5, Python ≥ 3.10 · 2
8. https://raw.githubusercontent.com/psycopg/psycopg/master/docs/basic/install.rst — `psycopg[binary]` zonder libpq · 2
9. https://raw.githubusercontent.com/JohannesBuchner/imagehash/master/README.rst en `/imagehash/__init__.py` — dHash-implementatie, Hamming-afstand · 2
10. https://resend.com/pricing — gratis 3.000/maand, 100/dag; Pro $20 · 1
11. https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/ScheduledJobs.html — StartCalendarInterval-gedrag bij slaap/uit · 2
12. https://www.catastro.hacienda.gob.es/webinspire/index.html — INSPIRE WMS/WFS/ATOM-URL's · 2
13. https://ovc.catastro.meh.es/ovcservweb/OVCSWLocalizacionRC/OVCCoordenadas.asmx — `Consulta_RCCOOR`, `Consulta_RCCOOR_Distancia`, `Consulta_CPMRC` · 2
14. https://www.catastro.hacienda.gob.es/webinspire/documentos/Licencia.pdf — opgehaald, niet leesbaar · 7
15. Idealista-assistent, tool `guide_idealista_assistant` (MCP `mcp-app.idealista.com/claude/v1/mcp`) — gidstekst · 3
16. https://sede.registradores.org/site/home — menu "Nota simple", geen tarief · 3
17. Geblokkeerd (§11): marketplace.gohighlevel.com/docs/ghl/…, highlevel.stoplight.io, psycopg.org, hackerfactor.com, sede.registradores.org/site/propiedad/nota-simple

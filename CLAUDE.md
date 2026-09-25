# TREE Deal Hunter — vastgoedacquisitie, renovatieobjecten, percelen en veilingen

Werkmap voor het acquisitiesysteem van Jan: vastgoedaanbod volgen (eerst
Jávea/Xàbia, later heel Spanje), kansen vinden, controleren, financieel
onderbouwen en omzetten in een concreet acquisitieplan. De volledige opdracht
staat letterlijk in `MASTERPROMPT.md` (Jan, 14-09-2026) en is hier de bron van
waarheid; deze CLAUDE.md is de korte versie.

## Rol in deze map

Senior vastgoed-dealmaker, acquisition director, renovatie-expert en grond- en
projectontwikkelingsanalist. Niet: advertenties verzamelen of dashboards
bouwen. Wel: per kandidaat de tien vragen uit masterprompt §1 beantwoorden
(wat wordt werkelijk aangeboden, waarom interessant, welke waarde voegen wij
toe, wat mag, wat kost het, wat levert het op, welke risico's, maximale prijs,
onderhandelingsroute, volgende stap).

Vier routes, gescheiden beoordelen (§2): A kopen-renoveren-verkopen,
B grond en projectontwikkeling, C renovatie- en leveringsopdrachten
(Build/Live), D bemiddeling en samenwerking.

## Regels (samenvatting van de masterprompt)

1. **Verzin niets.** Geen endpoints, rechten, objecten, prijzen, bouwpercentages,
   vergunningen of werkende automatiseringen zonder bron. Ontbreekt bewijs:
   ONBEKEND of [te verifiëren]. Elke feitelijke bewering met bron-URL,
   controledatum en bewijstype 1–7 (§5).
2. **Geheimen blijven geheim.** De feed-sleutels van Background Properties
   staan in `~/tree-hermes/properties-api/feeds.js` en in logs; nooit
   overnemen in documenten, rapporten, prompts of geheugen.
3. **Alleen toegestane toegang.** Geen scraping van portalen die dat verbieden,
   geen omzeilen van beveiliging. Publiceer-API ≠ lees-API. Een chatgesprek is
   geen draaiend systeem: monitoring heet pas "actief" als ze getest draait.
4. **Nooit zelfstandig bieden, betalen, tekenen of verplichtingen aangaan.**
   Geen berichten aan makelaars, banken of eigenaren zonder expliciet "ja" van
   Jan. Geen ongevraagde massabenadering van particulieren. Geen
   persoonsprofielen van schuldenaren.
5. **Percelen:** eerst identificeren (kadastrale referentie, geometrie), dan
   pas bouwconclusies; nooit een standaardpercentage "voor heel Jávea"; een
   toekomstig plan is geen geldend bouwrecht (§14–17).
6. **Veilingen:** zonder juridische beoordeling geen biedadvies; veilingwaarde
   ≠ marktwaarde; eerdere lasten kunnen blijven bestaan (§18–19).
7. Communicatie in het Nederlands, besluitgericht (§30): conclusie,
   onderbouwing, aannames, tegenargumenten, vervolgstap. Maximaal drie vragen
   tegelijk. "⏸️ ACTIE VOOR JAN" voor wat hij zelf moet doen.
8. Merk: dit is een TREE-project (Find. Build. Live.); Rocksure Capital is
   een apart merk en wordt hier niet vermengd, tenzij Jan beslist dat
   aankopen via Rocksure lopen.

## Wat hier staat

| Pad | Inhoud |
|---|---|
| `TODO.md` | **De lopende todo-lijst** (bron van waarheid voor wat er nog moet; J = Jan, S = systeem) |
| `MASTERPROMPT.md` | De opdracht van Jan, letterlijk |
| `01-…` t/m `05-…` | De vijf deliverables van fase A (acquisitiekader, bronnenkaart, percelen, veilingen, bouwplan) |
| `bronnenregister.json` | Machineleesbaar bronnenregister: velden uit §7, zes statussen, per regel een `id` en rechtenvlaggen (`automated_access`, `storage`, `history`, `ai_analysis`, `image_hashing`, `show_to_clients`, `personal_data`: yes/no/conditional/unknown) |
| `onderzoek/` | Per onderzoeksstroom een rapport (`R01`–`R17`) en het tegenspraakrapport (`*.verificatie.md`) |
| `rapporten/` | Rapporten voor Jan (webpagina's), incl. `haalbaarheid.html` en `mobiel.html` |
| `acties/` | Conceptberichten die pas na akkoord van Jan de deur uit gaan |

## Bestaande bouwstenen buiten deze map (alleen lezen, niet aanraken)

- Woningfeed Background Properties (Kyero v3 XML): dienst `com.tree.properties-api`
  op poort 3100, code in `~/tree-hermes/properties-api/` (ververst elk uur op :00).
- Importlogica van treeproperties.es: `~/tree-website/tree-properties/src/lib/import/`.
- Officiële Idealista-assistent (MCP van Idealista): zoeken en detail opvragen,
  alleen binnen een Claude-sessie; geen scraping.
- Hermes-agents (Discord/Telegram) voor bezorging; `tree-ai-agentic-os` voor
  bevoegdheden en goedkeuringen; GoHighLevel is het CRM van TREE Properties
  (ADR-0014).

## Status

- **14-09-2026:** fase A gestart. Onderzoeksronde met 17 stromen, tegenspraak,
  vijf deliverables en kritiekronde. Investeringskader van Jan (budget,
  rendementseis, doorlooptijd, bouwcapaciteit, entiteit) nog ONBEKEND —
  werkhypothesen zijn als zodanig gemarkeerd.
- **15-09-2026:** fase A afgerond. 17 rapporten met tegenspraak (329
  kernclaims gecontroleerd, 40 weerlegd en gecorrigeerd; elk rapport heeft
  bovenaan een banner). Eindstukken 01–05 na kritiek- en samenhangsronde
  onderling afgestemd; register 75 regels, niets GEVERIFIEERD EN ACTIEF.
  Rapport voor Jan: `rapporten/fase-a.html`. De drie open vragen staan in
  01 §1.2 (investeringskader en koper; afspraak met BP; proef op perceel K07).
  Er draait niets en er is niets gebouwd. Fase B wacht op die antwoorden.
- **15-09-2026 (middag): fase B gestart en deels live.** Investeringskader van Jan
  vastgelegd in `kader/investeringskader.{md,json}` (budget 500k–1M, 25 % op
  projectkosten, eigen geld, 24 mnd, Jávea+Benitachell+Moraira, 1.000/2.000 €/m²
  excl. btw). Monitor `dh/` (SQLite `data/dealhunter.sqlite`): BP-feed via
  poort 3100, BOE-sumario, AEAT-lijst; signalen, voorfilter met indicatieve
  haalbaarheid (`tools/haalbaarheid.py`, geteste rekenregels), rapport in
  `rapporten/dagelijks/`. launchd `com.tree.deal-hunter` draait 10:00 en 15:00;
  `com.tree.deal-hunter-review` = reviewpagina op 127.0.0.1:8710, via Tailscale
  https://mac-mini-van-root-admin.tail69022d.ts.net:8710 (tailnet only).
  Bezorging (Discord/e-mail) en AI-classificatie wachten op sleutels in `.env`.
  Idealista blijft handmatig (Search API aangevraagd door Jan). Herberekenen na
  wijziging van kader/comparables/parameters: `python -m dh.reanalyse`.
- **15-09-2026 (avond): haalbaarheid afgerond.** Wijkprijzen na renovatie/nieuwbouw voor 8 wijken
  (`onderzoek/H01-*`, met controle; correcties verwerkt in `kader/comparables.json` via
  `tools/bouw_comparables.py`). Doorrekening 14 kandidaten: `tools/rapport_haalbaarheid.py` →
  `rapporten/haalbaarheid.html` (artifact https://claude.ai/artifact/76Wz2VDdj3kmMTEkB6E9fv).
  Uitkomst: bij vraagprijs haalt geen enkele kandidaat betrouwbaar 25 % voorzichtig; in basis
  alleen K08 (perceel Rafalet, licentie geclaimd) en K13 (centrumpand, splitsing in 3).
  Rekenaar waarschuwt bij afwijkende grootte (per woning) en onbekende kosten.
- **15-09-2026 (nacht): dashboard live.** `dh/dashboard.py` + `dh/static/` (Leaflet via cdnjs in de
  browser; niets geïnstalleerd) op dezelfde dienst `com.tree.deal-hunter-review` (poort 8710,
  Tailscale). Blokken per kansrijkheid, kaart met IGN-basiskaart, PNOA-luchtfoto, Catastro-percelen
  (klik = kadastrale referentie via Consulta_RCCOOR_Distancia, 1 verzoek/s, gecachet) en wijkprijzen;
  dossier met drie maximale koopprijzen en wat-als-schuiven (`/api/listing/{id}/wat-als`, rekent via
  `dh/feasibility.py` → `tools/haalbaarheid.py`). Kaderwijziging Jan: **20 % winstmarge op
  verkoopwaarde** (= 25 % op kosten) en **8 % honoraria**. Idealista-kandidaten staan als bron
  `idealista` in de database (`python -m dh.import_kandidaten`, pins benaderend). Coördinaten buiten
  de regio worden genegeerd (`config.valid_coord`). Kleuren: groen = marge ook voorzichtig, blauw =
  marge in basis, oranje = basis-richtprijs ≥ 70 % van vraagprijs, grijs = onder marge, paars = niet
  betrouwbaar.
- **16-09-2026: mobiel.** Dashboard heeft op kleine schermen een schakelaar Lijst/Kaart, horizontale
  kerncijfers en grotere raakvlakken. Daarnaast `tools/rapport_mobiel.py` →
  `rapporten/mobiel.html`: momentopname in één bestand, zonder server en zonder Tailscale te openen
  (artifact https://claude.ai/artifact/9qx4uzEj4vJWscQKjNMZAd). Geen kaart daarin: kaarttegels laden
  niet in een gepubliceerde pagina. Opnieuw genereren na een ronde: `python3 tools/rapport_mobiel.py`
  en het bestand opnieuw publiceren op dezelfde link.
  Codecontrole 15/16-09 door een aparte agent: 12 bevindingen, alle hersteld (m²-schaal bij renovatie
  verhoogde de opbrengst zonder kosten; verouderde wat-als-antwoorden konden in een ander dossier
  belanden; schuifbereik verschoof; review-validatie; Catastro-throttling; isolatie per object).
- **16-09-2026: weergave en rekensom.** Elke kaart toont aankoop, bouw, verwachte verkoop en resultaat
  met marge en rendement op kosten (`feasibility.compute` → `sum`). Objecten waarbij de rekensom bij de
  vraagprijs verlies geeft, staan standaard verborgen: dashboard via de schakelaar "Ook objecten met
  verlies", mobiel via de knop Verlies of Alles. Volgende bron in beeld: Resales-Online (WebAPI V6),
  wacht op lidmaatschap én schriftelijke toestemming voor intern gebruik (zie R04 §3.2).
- **17-09-2026: zoekronde nieuwe bronnen.** 6 stromen + controleagent (`onderzoek/B01`–`B06`, shortlist in
  `B00-nieuwe-bronnen-shortlist.md`). Register 75 → 91 regels. Belangrijkste vondsten: de publicatieborden
  van Benitatxell en Teulada ontbraken (gratis, mag meteen), Inmoweb en Mediaelx hebben een gratis
  exportfeed per samenwerkingspartner, Metainmo heeft nieuwbouw-XML met 19 promoties in Benitachell,
  BORME heeft een eigen sumario-API voor liquidaties. Witei is uitgesloten: hun contract verbiedt gebruik
  als samenwerkingsmiddel tussen kantoren. Resales-Online static feed mag alleen op de eigen website.
- **18-09-2026: gratis bronnen, telefoonpagina en meldingen.**
  - **BORME draait mee** (`dh/adapters/borme.py`): elke ronde de sumario-API plus het Alicante-item uit
    Sección A. Dat item heeft gestructureerde XML (`url_xml`), dus geen PDF-ontleding. Bewaard worden
    alleen rechtspersoon, registernummer, handeling (ontbinding, liquidatie, opheffing, faillissement,
    kapitaalvermindering) en datum — nooit de aankondigingstekst, want daarin staan bestuurders en
    vereffenaars bij naam. Tabel `companies`, endpoint `/api/companies`, eigen blok in het dagrapport.
  - **Publicatieborden mogen niet automatisch gelezen worden.** De robots.txt van xabia, benitatxell en
    teuladamoraira op sedelectronica.es zegt `Disallow: /*` met alleen `/info`, `/info.0` en `/` vrij;
    `/info.0` loopt bovendien in een omleidingslus. De documentenserver van het BOP Alicante weigert
    crawlers ook. Dus geen koppeling: de drie borden staan als handmatige link in het rapport en op de
    telefoonpagina (`config.TABLONES`, `/api/tablones`). Register R2-42, R2-76, R2-77 → ALLEEN HANDMATIG;
    R2-82 (BORME) → GEVERIFIEERD EN ACTIEF, de eerste regel met die status.
  - **Telefoonpagina `/m`** (`dh/static/m.{html,css,js}`): live, vier vlakken onderaan (Kansen, Kaart,
    Veilingen, Wijken), kaart met IGN, PNOA, Catastro en wijkprijzen, dossier met de drie maximale
    koopprijzen en zes wat-als-schuiven, beoordeling en kadasteropvraging. Met `manifest.webmanifest` en
    `icon-{180,192,512}.png` (gemaakt door `tools/maak_iconen.py`, geen bibliotheken) als icoon op het
    beginscherm. De momentopname `rapporten/mobiel.html` blijft de reserve zonder Tailscale en wordt nu
    aan het eind van elke ronde automatisch opnieuw gemaakt (`run.refresh_mobile`).
  - **Meldingen bij sterke kansen** (`dh/alerts.py`, tabel `alerts`, `/api/alerts`): categorie *direct*
    (klasse groen of blauw: haalt de marge al bij de vraagprijs) en *verzamel* (klasse oranje: haalbaar
    binnen 30 % korting). Eén melding per object per categorie; opnieuw alleen bij een betere categorie
    of meer dan 2 % prijsdaling. De eerste ronde is een nulmeting en wordt als zodanig gelabeld.
    Kanaal: Discord; zonder `DISCORD_WEBHOOK_URL` wordt niets verstuurd maar wel vastgelegd.
  - **Gedeelde rekenlaag** `dh/summary.py`: dashboard, telefoonpagina, meldingen en momentopname lezen
    nu dezelfde functie, zodat de bedragen overal gelijk zijn.
- **18-09-2026 (nacht): aanbod, kadaster, dossiers.** Jan gaf 's avonds een nieuw kader: keuken en badkamers
  zitten NIET in het €/m²-tarief en TREE Properties verkoopt zelf, dus de courtage verlaat de groep niet.
  Beide verwerkt in `tools/haalbaarheid.py`, met een aftrek van 115 €/m² voor wat al in de aanneemsom zit.
  - **Aanbod 117 → 656.** `dh/import_idealista.py` leest de oogst van de officiële Idealista-assistent uit
    `onderzoek/idealista/*.json` (bron `idealista-zoek`). 539 nieuwe objecten, 76 prijsdalingen, 83 met een
    signaal van verkoopdruk.
  - **Kadaster.** `dh/catastro.py` en `dh/enrich_parcels.py`: punt → kadastrale referentie → adres, gebruik,
    bebouwd oppervlak, bouwjaar → officiële perceeloppervlakte en perceelgrens (INSPIRE wfsCP). Tabel
    `parcels`, 621 objecten gevuld. De perceelgrens wordt in het dossier als tekening op schaal getoond.
  - **Valstrikken.** `dh/signals.py` herkent rustieke grond, grond zonder woonbestemming en urbanisaties die
    niet zijn opgeleverd (Jans harde uitsluiting). Die worden niet meer als bouwkavel doorgerekend.
  - **Bouwregels.** `kader/bouwregels.json` uit onderzoek N01: 0,20 m²/m² in zona E, 0,28 in zeven gebieden,
    parcela mínima per wijk. Benitatxell en Teulada nog niet uitgezocht (N02 brak af op het maandplafond).
  - **Oppervlakten.** `dh/oppervlakte.py` bepaalt uit de advertentietekst of de opgave woonoppervlak,
    bebouwd oppervlak of een totaal met terras en kelder is, en rekent met het bebouwde woondeel (N06).
  - **Dossiers.** `dh/dossier.py` + `tools/rapport_dossiers.py` → `rapporten/dossiers/`, ook via het
    dashboard op `/dossiers/`. Acht stuks gepubliceerd: https://claude.ai/artifact/SMpPkjFHzGt863SSwDUsjP
  - **Onderhandelplan.** `dh/negotiation.py`: openingsbod, streefprijs, weglooppunt, argumenten met bewijs,
    hefbomen en voorbehouden. Boven de vraagprijs wordt nooit geboden.
  - **Tegenspraak op de topkandidaten** (`onderzoek/kandidaten-2026-09-18/`): vier objecten nagelopen tegen
    de advertentie zelf. Drie echte fouten gevonden en hersteld: een perceel met bestemming *terciario
    comercial* dat als villakavel werd gerekend, een dorpshuis in het centrum dat als villa in Granadella
    werd gewaardeerd (typologie `casaDePueblo` en de wijk uit de titel), en een prijs per m² die uit
    vergelijkingsobjecten van een heel andere maat kwam. Sinds die laatste correctie schuift `sale_band`
    naar het laagste kwart van de wijkprijzen zodra een object duidelijk groter is dan de reeks.
  - Onderzoek van deze nacht: `onderzoek/N01`, `N03`, `N05`, `N06`, `N07`. N02 en N04 zijn afgebroken op
    het maandplafond, net als vier van de acht tegenspraakagents in de eerste ronde.
- **24-09-2026: eigen makelaarssites.** Op verzoek van Jan leest `dh/adapters/makelaars.py` de sites van
  makelaars die dat toestaan: robots.txt per site (urllib.robotparser, ook voor `*`), sitemap en
  aanbodpagina's, per object JSON-LD → Open Graph → tekstpatronen vanaf de echte referentieregel (het
  zoekformulier bovenaan Inmoweb-sites vervuilde anders prijs, verhuur en kamers). 1 verzoek per 2 s,
  bron `makelaar:<host>`. `dh/import_makelaars.py` vergelijkt elk object op gebied, prijs (±2 %) en
  oppervlakte (±6 %) met de feed en de Idealista-oogst; geen treffer = `alleen_bij_makelaar`, wat betekent "niet gezien in onze portaalbronnen",
  niet "staat nergens": wij volgen maar een deel van Idealista.
  `kader/makelaars.json` is de lijst met per kantoor advies lezen / feed vragen / overslaan. Stap
  `step_makelaars` in `dh/run.py`. Register R2-92. Inventaris 24/25-09 (`onderzoek/makelaars/`): 189 kantoren,
  69 door agents getoetst, de rest door `tools/toets_makelaars.py` (alleen robots.txt, sitemap, homepage; de
  voorwaarden blijven dan "handmatig toetsen"). Per ronde een budget van 75 minuten met rotatie
  (`data/makelaars-stand.json`) en de crawl-delay uit robots.txt. Overzicht: `tools/rapport_makelaars.py` →
  `rapporten/makelaars.html`, gepubliceerd op https://claude.ai/artifact/YHYhgjyzs5UD5iNpK4p3hL.
- **25-09-2026: focus en ritme.** Jan: alleen panden of percelen in Jávea die interessant zijn om te renoveren
  of op te bouwen, twee rondes per dag, een webapp op de iPhone met per object een korte haalbaarheid.
  - `dh/focus.py` is de ene plek die zegt wat binnen beeld valt (`kader/investeringskader.json` → `focus`):
    gebied Jávea, categorieën renovatie, appartement-renovatie, perceel en bijzonder, plus elk object waarvan
    het beste scenario sloop en nieuwbouw is. Categorieën worden exact vergeleken, anders glipt
    `perceel-geen-wonen` mee met `perceel`. Gebruikt door de dossiers, de meldingen en de app.
    `focus.rijen(store)` is de SQL-voorfilter: 1.214 actieve objecten → ongeveer 230 doorrekenen.
  - `/api/listings?focus=1` geeft alleen de focus (1 s, 400 kB tegenover 2 s en 1,6 MB). De app haalt dat op
    en laadt de rest pas als je "Alles tonen" aantikt.
  - Elke advertentie draagt nu `bod` uit `dh/negotiation.py`: oordeel, openingsbod, weglooppunt en wat de deal
    draagt. Dat staat op de kaartjes in de app, dezelfde regels als in het dossier.
  - launchd `com.tree.deal-hunter` draait 08:00 en 18:30 (was 10:00 en 15:00); back-up van de oude plist staat
    naast het origineel.
- **25-09-2026 (nacht): Goolzoom, drie tabbladen, nieuwe kaartjes.** Jan beantwoordde twaalf vragen
  (`kader/keuzes-25-09-2026.md`); alles daaruit is verwerkt in `kader/investeringskader.json`.
  - **Goolzoom gekoppeld** (`dh/goolzoom.py`, sleutel in `.env`). Per perceel de officiële
    bestemming uit de urbanismelaag van de Generalitat Valenciana (IDEV), plus de eenheden op het
    perceel en de valor de referencia. `dh/enrich_urbanisme.py` vult tabel `urbanism`; 254 percelen
    gedaan. Uitkomst: 148 stedelijk (SU), 84 urbaniseerbaar (SUZ), 22 niet-urbaniseerbaar (SNU).
    Die 22 werden tot nu toe als bouwkavel doorgerekend. **Grens:** de laag geeft classificatie en
    zonering, géén edificabilidad, bebouwingspercentage of hoogte. Een bouwvolume mag hier nooit uit
    worden afgeleid; dat blijft de informe urbanística. Limieten: 10 verzoeken/s, 100.000 per maand,
    elke bevraging kost geld — daarom 90 dagen bewaard vóór opnieuw ophalen.
  - **Drie tabbladen** (`dh/focus.py`): *Jávea* (hoofdlijst), *misschien later* (vastgestelde
    niet-stedelijke bestemming) en *buiten Jávea* (Benitachell, Moraira — blijven meelopen).
    Ondergrens € 100.000 voor een perceel en € 500.000 voor een pand, geen bovengrens meer.
    Een níet opgevraagde bestemming is geen afwijzing: die objecten blijven in de hoofdlijst met de
    vermelding ONBEKEND. Stand: 167 kansen, 68 later, 73 buiten.
  - **Nieuwe kaartjes in de app** (keuze van Jan: minder tekst). Foto, plaats en prijs, één oordeel
    van twee regels, de vier bedragen, drie knoppen. Onderbalk: Kansen · Boeiend · Gebeld · Kaart ·
    Meer. Markeringen in tabel `markeringen` via `POST /api/markeer`; wat je wegklikt komt niet
    terug. Volgorde: winst per maand (`per_maand` in de samenvatting).
  - **Foto's**: kolom `listings.image_url`, gevuld uit de feed (`images[0]`) en uit `og:image` van
    makelaarssites. Buiten de vingerafdruk gehouden, anders geldt elk object als gewijzigd zodra er
    een foto bij komt. Bestaande objecten bijgewerkt met `tools/backfill_fotos.py`.
  - **Renovatietoets** (`dh/renovatie.py`): de vier kenmerken die Jan zelf noemde — oud en niet
    aangepakt, prijs onder de wijkprijs, de tekst zegt het zelf, groot perceel en klein huis.
  - **Drie fouten gevonden en hersteld.** (1) Een fiscale waarschuwing van vier ton kwam uit een
    kadastraal perceel dat het object niet ís; `summary.perceel_is_het_object` eist nu dat de maten
    kloppen, waarna er van 49 waarschuwingen 2 overbleven. (2) 60 objecten worden als kále grond
    aangeboden terwijl het kadaster er bebouwing ziet — nu zichtbaar als *tegenspraak*, met beide
    verklaringen erbij. (3) 32 zoek- en categoriepagina's stonden als woning van € 50.000 in de
    database (`is_overzichtspagina`); op verdwenen gezet en voortaan geweerd.
  - **Bezorging**: naast Discord nu ook e-mail via Resend (`alerts.send_email`, `alerts.bezorg`).
    Zonder sleutels wordt er niets verstuurd en zegt de status waarom.
  - **Snelheid**: de samenvatting kostte 5 s en de telefoon wachtte 10 s op een gevuld scherm. De app
    toont nu eerst de lijst; `/api/summary` en `/api/listings` worden kort bewaard met een sleutel
    die aan de databasestand hangt, en de ronde stookt die cache zelf warm (`run.warm_cache`).
  - **Database op slot**: twee processen schreven tegelijk, waardoor een tik op een knop verloren
    ging. `PRAGMA busy_timeout=15000` in de Store, en de fotoronde legt per object vast.
  - 17 tests groen, waaronder nieuwe voor de tabbladen, de renovatietoets, de perceeltoets, de
    fiscale waarschuwing, de markeringen en de overzichtspagina's.
- **25-09-2026 (vervolg): financiering, doorlooptijd en kosten opnieuw vastgesteld.** Jan beantwoordde
  vijftien vragen; de besluiten staan in `kader/keuzes-25-09-2026.md` en `kader/investeringskader.json`.
  - **Geen prijsgrenzen meer**, boven noch onder. De rekensom beslist. Hoofdlijst 167 → 212.
  - **€ 1.000/m² is een kostprijs, geen aanname.** TREE heeft eigen vaklieden; de marktprijzen uit N05
    (1.400–1.800) zijn aannemersprijzen inclusief marge. De oude waarschuwing in `feasibility` is
    vervangen door een toelichting over het risico dat wél overblijft: bezetting en doorlooptijd.
  - **Doorlooptijd uit drie blokken** (`feasibility.looptijd`): vergunning (obra menor 0, obra mayor
    via ECUV 5), bouw (renovatie 6, nieuwbouw 12, splitsen 18 — afgeleid), verkoop 3. Geeft 9, 20 en
    26 maanden. De Idealista-kandidaten uit september droegen hun eigen vaste getal mee; dat komt nu
    ook uit `looptijd()`, anders staan er onvergelijkbare scenario's in één lijst.
  - **100 % financiering, 15 %, per project te wijzigen** (`haalbaarheid.financing`). Rente over de
    aankoopsom plus kosten koper vanaf dag één over de hele looptijd; over de bouwsom gemiddeld de
    helft over de bouwperiode. Geen afsluitkosten. Bij de koploper: € 191.666 rente, € 9.583 per maand.
    Schuif in het dossier en override `finance_rate` in `/api/listing/{id}/wat-als` (0–40 %).
  - **Kosten een derde omlaag** omdat de eigen ploeg het doet: keuken 8.000/19.000, badkamer
    6.000/12.000, zwembad nieuw 17.000 en opknappen 8.000, sloop 60 €/m². Oude waarden bewaard onder
    `herkomst` in `kader/parameters.json`.
  - **Grondwerk en keermuren** (`haalbaarheid.earthworks`): licht hellend € 15.000, steil € 50.000,
    gestuurd door `Scenario.slope`. De helling per perceel wordt nog uitgezocht (N08); tot die tijd
    rekent het model er niets voor.
  - **Capaciteit:** twee tot drie projecten tegelijk (Jan). Nog niet in de app verwerkt.
  - **Twee ontwerpfouten hersteld.** (1) `reliable` was `not warnings`, dus élke opmerking maakte een
    scenario onbetrouwbaar en haalde het uit de ranglijst; toelichtingen staan nu apart in `notes`.
    Van 56 renovaties worden er nu 39 betrouwbaar gerekend in plaats van een handvol. (2) Aankoop plus
    bouw plus overig telde niet meer op tot de totale kosten nadat rente en grondwerk erbij kwamen;
    er staat nu een test op die dat voor elk scenario natelt.
  - 26 tests groen. Rapport voor Jan: https://claude.ai/artifact/LoU5DGsRKK2wq9txQypKMy
- **25-09-2026 (slot): helling per perceel gemeten, en drie laatste keuzes.**
  - **Hoogtemodel gekoppeld** (`dh/hoogte.py`, `dh/enrich_helling.py`). Bron: IGN WCS
    `Elevacion25830_5`, het 5-meterraster uit PNOA-LiDAR — gratis, CC BY 4.0, geen sleutel, en met
    `format=application/asc` platte tekst, dus zonder rasterio, GDAL of pyproj. De omzetting naar
    UTM 30N staat met de hand uitgeschreven in `hoogte.naar_utm30`. Onderzoek: `onderzoek/N08-…`.
    Drempels op de mediane celhelling (Horn 3 × 3): vlak < 8 %, licht 8–15 %, steil ≥ 15 %; de 15 %
    is op vijf manieren onderbouwd, de 8 % rust op één commerciële bron. Alle **361 percelen
    gemeten**: 85 vlak, 119 licht, 149 steil. Eigen implementatie getoetst tegen de drie percelen uit
    het onderzoek en die reproduceert de waarden (13,8 % tegen 13,9 % enzovoort).
  - **Twee verschillende perceeltoetsen**, in `dh/perceel.py`. `perceel_is_het_object` blijft streng
    voor de fiscale waarde: daar hangt een bedrag aan een gebouw. `grond_is_hetzelfde` is losser en
    alleen voor de helling: dat een advertentie zwijgt over een schuur zegt niets over hoe steil de
    grond is. Niet voor appartementen. Gevolg: grondwerk telt mee bij 35 objecten in de hoofdlijst,
    samen € 1,12 miljoen die er eerder niet in zat.
  - **Keuzes van Jan:** splitsen 14 maanden bouwtijd (5 + 14 + 3 = 22, binnen zijn grens); op het
    tabblad *misschien later* alleen nog urbaniseerbaar terrein, rustiek en beschermd valt helemaal
    af (70 → 54); géén capaciteitswaarschuwing in de app, Boeiend is een verlanglijst.
  - **Register:** R3-93 IGN MDT05 (GEVERIFIEERD EN ACTIEF) en R3-94 het planningsregister van de
    Generalitat (**ALLEEN HANDMATIG** — hun robots.txt sluit `ClaudeBot` en `Claude-User` expliciet
    uit; daar gaan wij dus niet meer heen).
  - Openstaand: artikel 8.1.23 van het PGOU Xàbia 1990 over abancalamientos en keermuren is de
    ontbrekende schakel voor hellende kavels. De scan heeft geen tekstlaag; op te vragen bij de
    Oficina Técnica. 30 tests groen.
- **25-09-2026: de ronde verrijkt nu zelf.** `run.step_verrijken()` draait ná het lezen van de bronnen
  en vóór het rapport: perceel (Catastro, 400 per ronde), bestemming (Goolzoom, 250 per ronde omdat
  die betaald is), helling (IGN, 400 per ronde), daarna de koppeling en `reanalyse`. Elke stap heeft
  een eigen vangnet en er is een tijdbudget van 12 minuten; wat blijft liggen komt de volgende ronde
  aan de beurt, en er zijn twee rondes per dag. Zonder deze stap rekenden nieuwe objecten zonder
  grondwerk en met bestemming ONBEKEND.
- **De app op de telefoon:** https://mac-mini-van-root-admin.tail69022d.ts.net:8710/m — alleen binnen
  het Tailscale-netwerk. Manifest, apple-touch-icon en de drie iconen zijn gecontroleerd over
  Tailscale (alle 200), dus "Zet op beginscherm" in Safari geeft een echte app zonder adresbalk.
- **25-09-2026: de meldingen staan LIVE.** Jan zette de Discord-webhook via `/instellingen`; ze komen
  binnen in zijn kanaal **acquisitie**. Proefbericht bevestigd. De kansen van de ronde van 08:00 zijn
  nagestuurd. E-mail blijft uit tot er een `RESEND_API_KEY` is; `alerts.bezorg` meldt dat netjes en
  laat Discord gewoon doorgaan.
  Let op voor de telefoon: de Mac mini draagt `tag:server` en Jans iPhone was ongetagd, waardoor
  Tailscale het apparaat niet eens toonde en de naam niet oploste ("server onvindbaar"). Opgelost door
  de iPhone `tag:personal` te geven, hetzelfde label als de MacBook.
- **25-09-2026: instellingenscherm op de telefoon** (`/instellingen`, knop onder Meer). Jan kan vanaf
  zijn mobiel geen bestand bewerken, dus de sleutels voor de meldingen zijn nu via de app te zetten:
  `config.save_env_key` schrijft in `.env` met een vaste witte lijst (`config.INSTELBAAR`), houdt de
  rechten op 600, laat andere regels ongemoeid en weigert een waarde met een nieuwe regel erin.
  Het scherm toont een waarde nooit terug, alleen of een sleutel gevuld is. De Discord-webhook wordt
  op vorm gecontroleerd (`dashboard.WEBHOOK_VORM`), zodat een bot-token er niet in belandt. Er is een
  knop voor een proefbericht via alle ingestelde kanalen.
- **26-09-2026: foto's eruit, link naar de advertentie erin — en drie fouten die daarbij opvielen.**
  - Op verzoek van Jan is de foto van het kaartje verdwenen. Daarvoor in de plaats staat onderaan elk
    kaartje een link over de volle breedte: "Advertentie openen bij <kantoor of site> ↗". De kolom
    `listings.image_url` wordt nog gevuld, dus terugzetten kost alleen het stukje in `card()` en wat
    opmaak.
  - **De titel ging niet mee naar de signaalanalyse bij het herberekenen.** `reanalyse` bouwde de
    tekst op uit alleen `desc_excerpt`, terwijl het inlezen titel én omschrijving gebruikt. Daardoor
    verdween bij elke herberekening de herkenning van objecten waar het beslissende woord in de titel
    staat. Erger bij makelaarssites, waar de omschrijving soms de cookiemelding van de site is en de
    titel het enige bruikbare. Hersteld.
  - **`reanalyse` sloeg alle makelaarsobjecten over** (`if r["source"] != "bp": continue`). Een
    nieuwe signaalregel werkte dus nooit met terugwerkende kracht op de 1.600 objecten van
    makelaarssites. Nu 1.852 in plaats van 225 per herberekening.
  - **Bedrijfsovernames stonden als woning in de lijst.** Een *traspaso* is de overname van een
    lopend bedrijf, niet de koop van vastgoed. Drie ervan stonden met € 500 tot € 2.900 boven aan de
    goedkoopste objecten. Nieuw patroon `GEEN_KOOP` in `dh/signals.py` en de categorie `geen-koop`,
    die buiten de focus valt.
  - **Niet-verkavelde grond in het Duits en Engels werd niet herkend.** `NOT_URBANISED` kende alleen
    Spaanse patronen; makelaars in Jávea publiceren in vier talen. "Zu urbanisieren" is precies Jans
    harde uitsluiting en stond op een perceel van € 30.000 dat als kans in beeld kwam. Aangevuld met
    Duits, Engels en Nederlands; nu 25 objecten in Jávea herkend.
  - 35 tests groen.
- Let op bij de BP-feed: plaatsnaam staat als "Javea" zonder accent;
  filteren op "Jávea" of "Xàbia" geeft 0.

# TODO — TREE Deal Hunter

Eén lijst, bijgewerkt terwijl we werken. **J** = actie van Jan, **S** = actie van het systeem of van mij.
Status: `[ ]` open · `[~]` loopt · `[x]` klaar. Datum is de dag dat het punt is opgeschreven.
Conceptberichten staan in `acties/`; de gebruiksrechten per bron in `bronnenregister.json`.

## Bronnen uitbreiden

- [~] **S · Eigen makelaarssites lezen** (24-09, op verzoek van Jan). Lezer gebouwd en getest op
  Xabiacasa: robots.txt per site, dan sitemap en aanbodpagina's, dan per object de velden. Elk object
  wordt vergeleken met de feed en de Idealista-oogst; wat wij niet in onze portaalbronnen zien krijgt het kenmerk
  "niet gezien op de portalen die wij volgen" (filter op de telefoon, vermelding in het dossier). Draait mee in de
  dagelijkse ronde. Inventaris 24/25-09: 189 kantoren met eigen site gevonden; 69 door agents getoetst
  (45 lezen, 18 feed vragen, 6 overslaan), de rest met `tools/toets_makelaars.py` op robots.txt en
  sitemap, omdat de agents op het maandplafond strandden. Overzicht voor Jan:
  https://claude.ai/artifact/YHYhgjyzs5UD5iNpK4p3hL (`tools/rapport_makelaars.py`). Eerste brede
  leesronde loopt met een budget van 75 minuten per ronde en rotatie over de kantoren.
- [ ] **J · Feeds vragen aan kantoren die niet gelezen mogen worden.** Zodra de inventaris klaar is
  staat per kantoor of lezen mag. Voor de rest maak ik een conceptmail (Inmoweb, Mediaelx en
  Sooprema kennen alle drie een gratis exportfeed per samenwerkingspartner).

*Zoekronde 17-09: 54 kandidaten bekeken, 16 bruikbaar, 26 afgewezen, 12 nieuwe routes bij partijen
die we al kenden. Volledige lijst met bewijs: `onderzoek/B00-nieuwe-bronnen-shortlist.md`.*

- [x] 18-09 · **Publicatieborden: mag niet automatisch.** De robots.txt van alle drie de borden
  (Xàbia, Benitatxell, Teulada-Moraira, alle op sedelectronica.es) sluit geautomatiseerd lezen uit:
  `Disallow: /*`, met alleen `/info`, `/info.0` en `/` toegestaan. `/info.0` geeft bovendien een
  eindeloze omleiding. Ook de documentenserver van het BOP Alicante (dip-alicante.es) weigert
  crawlers. Daarom géén koppeling gebouwd; de drie borden staan nu als link in het dagrapport en op
  de telefoonpagina onder Veilingen. Register R2-42, R2-76 en R2-77 bijgewerkt naar ALLEEN HANDMATIG.
- [ ] **J · Wil je dat we de borden toch mogen lezen?** Eén mail of telefoontje naar de drie
  gemeenten om schriftelijke toestemming te vragen voor automatisch uitlezen van het tablón. Dan pas
  bouwen we de koppeling.
- [ ] **J · Inmoweb-exportfeed via drie Jávea-kantoren** (17-09). RANDOF, Javea Continental en Xabiacasa
  draaien op Inmoweb, dat een gratis exportfeed per samenwerkingspartner kent, met een sleutel die het
  kantoor zelf kan intrekken. Eén telefoontje per kantoor; daarna een korte schriftelijke afspraak.
  Goedkoopste echte uitbreiding van onze voorraad.
- [ ] **J · Mediaelx-export via Casas Ambiente (Moraira)** (17-09). Vier Moraira-kantoren draaien op dit
  CRM met een zelfbediende export. Vraag expliciet om alleen hun eigen objecten, niet de geïmporteerde.
- [ ] **J · Metainmo, nieuwbouwdatabank met XML** (17-09, betaald). Zelf geteld: 19 promoties in
  Benitachell en 7 in Moraira; Jávea kwam op nul, dus vraag dat na. Offerte vragen én schriftelijk laten
  bevestigen dat wij mogen opslaan, historie bewaren en intern analyseren.
- [ ] **J · Inmocalpe, de MLS van Calpe** (17-09). Lokale vereniging met gedeelde exclusieven; leden zijn
  ook actief in Moraira, Benitachell en Jávea. Eén mail naar info@inmocalpe.es met vier vragen:
  toelating, contributie, bestaat er een koppeling, en wat mag je met objecten van andere leden.
- [ ] **J · Sooprema** (17-09). Vijf kantoren in ons gebied gebruiken dit systeem, dat een API heeft.
  Vraag of een klant ons leestoegang tot zijn eigen objecten mag geven.
- [ ] **J · VAPF-extranet (Cumbre del Sol)** en **AEDAS-collaboratorportaal** (17-09). Beide bouwen in ons
  gebied. Toegang aanvragen en vragen of prijslijst en beschikbaarheid als bestand komen.
- [x] 18-09 · **BORME-signalering draait.** Adapter `dh/adapters/borme.py` leest elke ronde de
  sumario-API en het provincie-item van Alicante. Dat item blijkt gestructureerde XML te hebben, dus
  geen PDF-ontleding nodig. Opgeslagen worden alleen rechtspersoon, registernummer, handeling en
  datum; de aankondigingstekst met namen van bestuurders en vereffenaars niet. Eerste ronde: 7
  signalen, waarvan 2 in vastgoed of bouw. Staat in het dagrapport en onder Veilingen op de telefoon.
- [ ] **S · Aliseda-sitemap wekelijks volgen** (17-09). Hun eigen sitemap noemt landpagina's voor Jávea en
  Teulada. Alleen als signalering; gebruiksrechten zijn onbekend, dus Jan opent de pagina's zelf.
- [ ] **S · Rightmove Overseas als kantorenradar** (17-09). 489 Jávea-objecten. Niet als feed, wel om te
  zien welke kantoren daar adverteren en in onze feeds ontbreken.
- [ ] **J · MLS Costa, RedSP en Babysteps** (17-09, alle drie betaald of onbewezen). Eerst dekking in onze
  drie gemeenten laten aantonen voordat er iets wordt afgesloten.
- [x] 17-09 · **Witei valt af.** Hun servicecontract verbiedt gebruik als samenwerkingsmiddel tussen
  zelfstandige kantoren. Witei-kantoren niet om een feed vragen.

- [ ] **J · Resales-Online** (16-09). Grootste netwerk met echte dekking van Jávea, Benitachell en
  Moraira, met een koppeling die werkt (WebAPI V6, sleutel per IP-adres). Twee dingen nodig:
  1. **Lidmaatschap.** Is TREE Properties al lid? Zo niet: wat kost het? Hun prijspagina blokkeert
     onze verzoeken, dus dat is onbekend.
  2. **Schriftelijke toestemming.** Hun voorwaarden staan alleen weergave van andermans objecten op je
     eigen website toe en verbieden feeds met andermans objecten aan derden. Opslaan en analyseren voor
     Deal Hunter valt daar niet vanzelf onder. Eigen objecten van TREE mogen altijd.
  - **S, daarna:** koppeling bouwen als bron `resales`, met dezelfde behandeling als de andere bronnen
    (rechtenpoort, ontdubbeling tegen de BP-feed, wijkprijzen). Zie R04 §3.2 en registerregel R2-24.
- [ ] **J · Idealista Search API aanvragen.** Tekst klaar in
  `acties/2026-09-15-idealista-search-api-aanvraag.md`; formulier op developers.idealista.com.
- [ ] **J · Background Properties.** Schriftelijke afspraak in `kader/` zetten, zodat het register van
  "door Jan gemeld" naar "document gezien" gaat.
- [ ] **J/S · MLS 03724 Teulada-Moraira** (16-09). Enige netwerk in de Marina Alta waar volgens leden
  ook verkoopdata circuleert, dus echte transactieprijzen. Uitzoeken zodra Resales-Online duidelijk is.
- [ ] **J/S · Colegio API Alicante (APIred).** Bolsa voor colegiados, aanlevering via Kyero-bestand.
  Alleen zinvol als TREE colegiado is of wordt.
- [ ] **J · Accounts met e-mailmeldingen:** Idealista, Fotocasa, subastas.boe.es (alleen als natuurlijk
  persoon), Servihabitat Profesionales. Automatisch inlezen van die mails pas na juridische toets.

## Aanzetten en bevestigen

- [x] 25-09 · **Discord-meldingen staan LIVE.** Jan zette de webhook zelf via het instellingenscherm
  op `/instellingen`; kanaal **acquisitie**. Proefbericht aangekomen, en de kansen van de ronde van
  08:00 zijn alsnog nagestuurd (8 direct, 6 verzamel, in twee berichten). Vanaf 18:30 meldt het
  systeem uit zichzelf.
- [ ] **J · E-mail als tweede kanaal** (optioneel). Alleen `RESEND_API_KEY` ontbreekt nog; het adres
  staat er al. Zonder die sleutel gaat alles gewoon via Discord. Zet hem desgewenst op
  `/instellingen`.
- [x] 25-09 · **S · E-mailkanaal gebouwd.** `alerts.send_email` via de HTTPS-API van Resend; niets
  geïnstalleerd. `alerts.bezorg` stuurt naar beide kanalen en laat het ene doorgaan als het andere
  uitvalt.
- [ ] **J · AI-classificatie.** `ANTHROPIC_API_KEY` in dezelfde `.env`, binnen het plafond van 100 €/maand.
- [ ] **J · Nacalculaties.** Drie tot vijf projecten, €/m² exclusief btw met jaartal: nieuwe villa,
  integrale renovatie, keuken en badkamers, zwembad, keermuren.
- [ ] **J · Courtage bevestigen.** Het model rekent 5 % plus btw bij verkoop. Honoraria staan sinds
  15-09 op 8 % (jouw opgave).
- [ ] **J · Adviseurs.** Namen van de vaste advocaat, gestor en architect.

## Eerste dossiers

- [ ] **J · K07 Garroferal.** Bericht aan de aanbieder goedkeuren
  (`acties/2026-09-15-bericht-K07-aanbieder.md`), daarna nota simple en informe urbanístico.
  Let op: de bankgarantie wijst op een urbanisatie die de gemeente nog niet heeft overgenomen, en dat
  is jouw enige harde uitsluiting.
- [ ] **S · K08 en 4104JAV.** Vermoedelijk hetzelfde perceel in El Rafalet, nu twee keer op de kaart.
  Ontdubbelen zodra de kadastrale referentie bekend is.

## Systeem verbeteren

- [x] 25-09 · **De ronde verrijkt zelf.** Perceel, bestemming en helling worden nu in elke ronde
  aangevuld voor nieuwe objecten, met een portiegrootte per bron en een tijdbudget.

- [x] 25-09 · **Helling per perceel gemeten.** IGN MDT05 via WCS, gratis en zonder sleutel; 361
  percelen gemeten (85 vlak, 119 licht, 149 steil). Grondwerk telt nu mee bij 35 objecten in de
  hoofdlijst. Bij de overige percelen staat de koppeling pin → perceel niet vast; daar rekent het
  model bewust niets, dus dat blijft een kostenpost die kan opduiken.
- [ ] **J · Eén perceel noemen waarvan je het werkelijke grondwerk kent.** Daarmee is de grens van
  8 % tussen vlak en licht hellend te ijken; die rust nu op één commerciële bron.
- [ ] **J · Artikel 8.1.23 PGOU Xàbia 1990 opvragen** bij de Oficina Técnica (965 790 500) of via je
  architect. Dat artikel regelt abancalamientos en keermuren en bepaalt de praktijk op hellende
  kavels; de scan in het register heeft geen tekstlaag en is dus niet te lezen.
- [x] 25-09 · **Capaciteitswaarschuwing: niet doen.** Jan: Boeiend is een verlanglijst, geen planning.
- [x] 25-09 · **Bouwtijd splitsen: 14 maanden** (Jan). Totaal 5 + 14 + 3 = 22, binnen zijn grens.

- [ ] **S · Bestemming voor de 255 objecten zonder perceel.** Makelaarssites geven geen coördinaten,
  dus er is geen kadastrale referentie en de bestemming blijft ONBEKEND. De adresingang van Goolzoom
  (`cadastre/exactaddress/3082/{straatcode}/{nummer}`) is getoetst: van 255 objecten noemen er 22 een
  straat en maar 2 een huisnummer, dus die weg levert vrijwel niets op. Straatlijst bewaard in
  `data/javea-straten.json` (1.283 straten). Kansrijker: de kaartwidget op de objectpagina uitlezen,
  of de makelaar om de kadastrale referentie vragen.
- [ ] **S · 60 percelen die als kále grond worden aangeboden terwijl het kadaster bebouwing ziet.**
  Staan nu als tegenspraak op het kaartje en in het dossier. Uitzoeken of het een verkeerde
  koppeling is of verzwegen bebouwing — het tweede kan gunstig zijn, want een bestaand legaal gebouw
  geeft soms bouwrechten die kale grond niet krijgt.
- [x] 25-09 · **Prijsgrenzen eruit.** Jan: geen ondergrens en geen bovengrens. De rekensom bepaalt
  of iets interessant is, niet de vraagprijs. Hoofdlijst 167 → 202 objecten, waarvan 15 appartementen.
- [x] 25-09 · **Bouwtarief beslecht: € 1.000/m² is een kostprijs.** TREE heeft eigen vaklieden in
  dienst, dus de marktprijzen van N05 (1.400–1.800, inclusief aannemersmarge) gelden hier niet. Het
  openstaande risico verschuift naar eigen bezetting en doorlooptijd; dat zit niet in de rekensom.

- [x] 18-09 · **Oppervlakten gelijkgetrokken.** Onderzoek N06 wees drie regimes aan: woonoppervlak,
  bebouwd oppervlak en totaal inclusief terras, garage en kelder. Het verschil loopt bij hetzelfde huis
  op tot een factor 2,4. `dh/oppervlakte.py` herkent het regime uit de advertentietekst en rekent met het
  bebouwde woondeel. In de dossiers staat per object welk regime is aangehouden en waarom.
- [x] 18-09 · **Prijs per m² volgt nu de maat van het object.** De tegenspraak liet zien dat de reeks
  voor Granadella wordt gedragen door gerenoveerde villa's van 180 tot 285 m², terwijl wij daarmee een
  huis van 378 m² waardeerden. Een verse meting in dezelfde wijk en maatklasse gaf 4.397 €/m² in plaats
  van 6.081. Objecten die duidelijk groter zijn dan de vergelijkingsobjecten rekenen nu met het laagste
  kwart van de wijkprijzen, met een waarschuwing erbij.
- [ ] **J · Renovatietarief bevestigen.** Onderzoek N05 zegt dat 1.000 €/m² een grondige maar niet
  totale renovatie met middenafwerking is, en dat casco strippen met topafwerking 1.400 tot 1.800 €/m²
  kost. Bij een pand waarvan de advertentie zelf "integrale renovatie" zegt staat nu een waarschuwing.
  Zeg welk tarief je in die gevallen wilt aanhouden.
- [ ] **S · Vergelijkingsreeksen per wijk opnieuw opbouwen** op het bebouwde woondeel in plaats van de
  kale opgave. Nu is alleen de objectkant gecorrigeerd, de vergelijkingskant nog niet. Zolang dat
  verschil er is, overschat de verkoopprijs per m² waarschijnlijk iets. Zie N06 §6.4.
- [ ] **S · Bouwregels Benitatxell en Teulada uitzoeken.** Het onderzoek daarnaar (N02) brak af op het
  maandplafond. Voor die twee gemeenten geldt nu de standaardaanname van 0,20 m² per m², wat in de
  dossiers ook zo staat.
- [ ] **S · Risicokaarten per perceel bevragen.** De endpoints zijn getest en staan in N03:
  PATRICOVA, brandgevaar, Natura 2000, kustzone, waterlopen, vias pecuarias. Nog niet gekoppeld, dus de
  dossiers zeggen nu dat die kaarten niet zijn nagekeken.
- [x] 18-09 · **Mobiele versie automatisch verversen.** `rapporten/mobiel.html` wordt aan het eind
  van elke ronde opnieuw gemaakt. Publiceren naar dezelfde link blijft handwerk.
- [ ] **J · Tailscale op je telefoon** en daarna `https://mac-mini-van-root-admin.tail69022d.ts.net:8710/m`
  openen en op je beginscherm zetten (Safari: Deel → Zet op beginscherm). Dat is de live versie met
  kaart, kadaster en de wat-als-schuiven.
- [x] 25-09 · **Rapporttijden** op verzoek van Jan naar 08:00 en 18:30 Europe/Madrid: 's ochtends en aan
  het begin van de avond. Elke ronde leest ook de makelaarssites, met een budget van 75 minuten.

## Klaar

- [x] 18-09 · **Idealista-oogst.** 680 objecten via de officiële assistent, 539 nieuw in het systeem,
  76 met een geregistreerde prijsdaling en 83 met een signaal dat de verkoper onder druk staat.
  Aanbod van 117 naar 656 objecten.
- [x] 18-09 · **Kadaster gekoppeld.** Van 621 objecten zijn de kadastrale referentie, de officiële
  perceeloppervlakte, het gebruik en de perceelgrens opgehaald. Bij 408 wijkt de advertentie af van het
  kadaster; dat staat per object in het dossier.
- [x] 18-09 · **Valstrikken eruit.** Rustieke grond, grond zonder woonbestemming en urbanisaties die
  niet zijn opgeleverd worden herkend en niet meer doorgerekend als bouwkavel. Dat haalde vijftien
  schijnkansen uit de lijst, waaronder percelen van 10.000 m² voor 120.000 euro.
- [x] 18-09 · **Keuken, badkamers en eigen verkoop in het model.** Keuken en badkamers apart geteld met
  de bedragen uit N05, met aftrek van wat al in de aanneemsom zit. Courtage vervalt omdat TREE Properties
  zelf verkoopt; dat verschil staat per object in het dossier.
- [x] 18-09 · **Acht volledige dossiers** met besluit, kadaster, perceelgrens, bouwregels, rekensom en
  onderhandelplan: https://claude.ai/artifact/SMpPkjFHzGt863SSwDUsjP

- [x] 15-09 · Investeringskader vastgelegd: 20 % winstmarge op verkoopwaarde, 8 % honoraria,
  budget 500k–1M, 24 maanden, eigen geld, werkgebied Jávea, Benitachell en Moraira.
- [x] 15-09 · Monitor draait twee keer per dag op de BP-feed, het BOE en de AEAT-veilinglijst.
- [x] 15-09 · Haalbaarheid van veertien kandidaten doorgerekend, met wijkprijzen per m².
- [x] 15/16-09 · Dashboard met kaart, kadaster, luchtfoto, dossiers en wat-als-schuiven.
- [x] 16-09 · Mobiele versie, rekensom per object, objecten met verlies standaard verborgen.
- [x] 18-09 · Telefoonpagina `/m`: live, met kaart, dossier met schuiven, veilingen en wijkprijzen,
  en een icoon voor het beginscherm. Meldingen bij sterke kansen (twee tonen) met nulmeting.

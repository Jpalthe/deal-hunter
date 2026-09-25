# R09 — Veilingprocedure, waarborgsommen, lasten en het juridische dossier

> **NA TEGENSPRAAK (15-09-2026).** Dit rapport is door een tweede agent gecontroleerd; zie `R09-veilingen-juridisch-procedure.verificatie.md`. Betrouwbaarheid volgens die controle: hoog.
> Weerlegd en in de eindstukken gecorrigeerd: R09-16. Gebruik voor die punten de gecorrigeerde tekst in het verificatiebestand, niet de tekst hieronder.


**Project:** TREE Deal Hunter, fase A — stroom R09 (masterprompt secties 18 en 19)
**Controledatum van alle bronnen:** 14-09-2026
**Bewijstypen (masterprompt sectie 5):** 1 door aanbieder vermeld · 2 in officiële bron aangetroffen · 3 door ons rechtstreeks vastgesteld · 4 AI-inferentie · 5 berekening op benoemde aannames · 6 door bevoegde professional bevestigd · 7 onbekend of tegenstrijdig
**Status van dit stuk:** onderzoeksrapport, geen juridisch advies. Elke conclusie met bewijstype 4 of 5 en elk **[te verifiëren]** vraagt bevestiging door een Spaanse advocaat/gestor (bewijstype 6) vóór er ooit geboden wordt.

## Samenvatting (10 regels)

1. Alle gerechtelijke, notariële en AEAT-veilingen lopen via één portaal, subastas.boe.es; TGSS-veilingen volgens hun eigen reglement via de sede electrónica van de Seguridad Social (geen BOE-portaal aangetroffen). Het portaal verbiedt bots (`robots.txt: Disallow: /`); wél zijn e-mailalerts op opgeslagen zoekopdrachten toegestaan. Voor Jávea: 278 vastgoedveilingen (alle statussen) gevonden op 14-09-2026, van rechtbanken Dénia, AEAT, notarissen en de gemeente Xàbia.
2. **Twee LEC-regimes bestaan naast elkaar.** Ley Orgánica 1/2025 (in werking 03-04-2025) heeft de veilingartikelen ingrijpend gewijzigd, maar geldt volgens haar overgangsbepaling alleen voor procedures die ná die datum zijn ingeleid. Oudere zaken (bijv. expediente "0952/18") volgen de oude tekst. Per dossier moet dus eerst het regime worden vastgesteld.
3. Waarborgsom gerechtelijke veiling onroerend goed: **20 % van de veilingwaarde (min. 1.000 €)** onder het nieuwe regime; **5 %** onder het oude. AEAT: **5 %** van de tipo voor onroerend goed. TGSS: **25 %** per gecertificeerde cheque (30 % bij mondeling bod ter zitting).
4. Betaaltermijn na toewijzing: LEC nieuw **20 dagen** na sluiting (oud: 40 dagen); AEAT **15 dagen** na kennisgeving; TGSS **5 werkdagen**. Niet betalen = verlies van de waarborgsom (en bij AEAT/TGSS bovendien aansprakelijkheid voor schade).
5. Drempels LEC (onroerend goed, nieuw regime): bod ≥ 70 % van de veilingwaarde → toewijzing de dag erna; < 70 % → de schuldenaar heeft 10 dagen om iemand aan te dragen voor ≥ 60 %; daarna toewijzing bij ≥ 50 % (of bij een bedrag dat de schuld volledig dekt, min. 40 %); eigen woning van de schuldenaar: niet onder 70 %/60 %. Bij geen bieders kan de schuldeiser zich onder het nieuwe regime **niet** meer zelf het goed laten toewijzen (oud regime: wel, voor 50 %/70 %/60 %).
6. **Eerdere lasten blijven bestaan** en de koper subrogeert erin (LEC 668.2, 669.2, 670.5; RGR 97.6; RGR-SS 111.2): de veilingwaarde is tasación mínus eerdere lasten (LEC 666). Latere lasten worden doorgehaald via het mandamiento (LEC 674, LH 134). In faillissement: doorhaling van pre-concursale lasten, kosten voor de koper (TRLC 225).
7. Bezetting: de veilingpublicatie moet de bezitssituatie vermelden (LEC 661); "No consta" komt in de praktijk voor (waargenomen). Ontruiming van bezetters zonder titel kan tot 1 jaar na verkrijging binnen de executie worden gevraagd (LEC 675.2); daarna alleen via een aparte procedure.
8. Fiscaal bij toewijzing in de Comunitat Valenciana: ITP 9 % (11 % boven 1 M€ waarde) volgens de geconsolideerde Ley 13/1997; grondslag is een spanningsveld tussen "valor de referencia" (TRLITPAJD 10.2) en "valor de adquisición" bij veilingen (RITP 39) — **[te verifiëren]**. AJD in beginsel 1,4 % maar alleen bij een notariële akte; plusvalía is voor de vervreemder, maar de koper wordt vervangend belastingplichtige als de vervreemder een niet-ingezeten natuurlijke persoon is (TRLHL 106.2) — relevant in Jávea.
9. De waarborgsom is een liquiditeitsbeslag met een looptijd van 0 dagen (verliezer zonder reserva) tot maanden (met reserva de postura, tot de toewijzing rond is), en een verbeurterisico alleen bij eigen wanbetaling of niet-aantonen van vertegenwoordiging (LEC 647.1) — model in sectie 8.
10. Harde blokkades voor een biedvoorstel (sectie 7): aangeboden recht ≠ volle eigendom (in het portaal aangetroffen: "25% PLENO DOMINIO", "50% NUDA PROPIEDAD"), certificación de cargas ontbreekt of is ouder dan 6 maanden zonder actualisatie, bezetting zonder titel of "no consta", tasación 0,00 €/onbekend, procedure geschorst (concurso), regime (oud/nieuw) onbekend.

---

## 0. Werkwijze en beperkingen

- Alle wetsartikelen zijn rechtstreeks uit de **geconsolideerde teksten op boe.es** gehaald (HTML opgehaald op 14-09-2026, artikelblokken uitgelezen inclusief de wijzigingsnoten van de BOE). De datum "consolidatie" hieronder is de datum "Última actualización publicada" die de BOE bovenaan de tekst vermeldt.
- De WebSearch-tool was in deze sessie uitgeput (budget 200/200 vóór de start van deze stroom). Er is daarom uitsluitend gewerkt met rechtstreekse ophaling van officiële pagina's (boe.es, subastas.boe.es, sede.agenciatributaria.gob.es, seg-social.es, publicidadconcursal.es). Dat is een beperking: geen jurisprudentie- of DGT-consultas gezocht; die staan als open vraag.
- Op subastas.boe.es zijn drie openbare, niet-geauthenticeerde raadplegingen gedaan (één provinciale lijst, één zoekopdracht op plaatsnaam, twee detailpagina's). Daarna is vastgesteld dat `robots.txt` alle geautomatiseerde toegang verbiedt; verdere ophaling is gestaakt en er is niets gescrapet.
- Geen persoonsgegevens overgenomen: van veilingen zijn alleen dossiernummers, instanties, objecttypen en bedragen genoteerd.

---

## 1. Het BOE-veilingportaal (subastas.boe.es) — wat het is en wat wij mogen

| Bevinding | Bron | Bewijstype |
|---|---|---|
| Rechtsgrond: Ley 19/2015 gaf de AEBOE de opdracht één portaal voor gerechtelijke en administratieve veilingen te maken; Ley 1/2013 bracht de notariële venta extrajudicial erin. Sinds 01-09-2018 lopen ook de fiscale veilingen (AEAT) via het portaal; "otras subastas administrativas" worden stapsgewijs toegevoegd. Citaat: "En el Portal de Subastas del BOE se realizan las subastas judiciales, notariales, y desde el 1 de septiembre de 2018, las subastas tributarias." | https://subastas.boe.es/ayuda.php | 2 |
| Autoridad gestora per soort: rechtbank (Letrado de la Administración de Justicia), notaris, "unidad de recaudación" (fiscaal), de betreffende overheid (administratief), en de ORGA (strafrechtelijk verbeurd verklaarde goederen). | idem | 2 |
| Registratie: alleen natuurlijke personen; certificado electrónico of Cl@ve (alleen presentieel of met certificaat verkregen). Bieden namens een vennootschap kan door bij depósito en puja aan te geven dat men voor een derde handelt. | idem; https://sede.agenciatributaria.gob.es/Sede/deudas-apremios-embargos-subastas/subastas/licitadores.html | 2 |
| Depósito wordt uitsluitend via het portaal gesteld, via de betaalpassarelle van de AEAT, vanaf een rekening bij een "entidad colaboradora" waarvan de gebruiker houder/gemachtigde is; gezamenlijke rekeningen met meervoudige handtekening zijn niet bruikbaar. Advies van het portaal: meer dan één dag vóór sluiting storten. | ayuda.php | 2 |
| Duur: 20 kalenderdagen (LEC 649.1 / RGR 104). Verlenging: een hoogste bod in het laatste uur verlengt tot één uur na dat bod, in totaal maximaal 24 uur — afhankelijk van de toepasselijke regeling en de keuze van de autoridad gestora. | ayuda.php | 2 |
| Terugbetaling: verliezer zonder reserva de postura → direct na afloop; met reserva → pas nadat de autoridad gestora de toewijzing aan het portaal heeft gemeld ("El plazo de devolución, en este caso, depende del proceso de adjudicación"). | ayuda.php | 2 |
| Alerts: een ingelogde gebruiker kan een zoekopdracht (plaats/postcode, status "Celebrándose") opslaan en dagelijks e-mail ontvangen bij nieuwe veilingen die eraan voldoen. Dit is het door het portaal zelf aangeboden meldkanaal. | ayuda.php | 2 |
| `robots.txt`: `User-agent: * / Disallow: /` — geautomatiseerd ophalen is niet toegestaan. Geen API, geen RSS en geen open-datacatalogus voor veilingen gevonden (de pagina boe.es/datosabiertos gaf op 14-09-2026 een lege respons; de BOE-API voor geconsolideerde wetgeving gaf HTTP 400 op het geteste pad). | https://subastas.boe.es/robots.txt ; https://www.boe.es/datosabiertos/ | 3 |
| Zoekvelden van het portaal (uit het zoekformulier): SUBASTA.ORIGEN, SUBASTA.AUTORIDAD, SUBASTA.ESTADO.CODIGO, BIEN.TIPO, BIEN.DIRECCION, BIEN.CODPOSTAL, BIEN.LOCALIDAD, BIEN.COD_PROVINCIA, SUBASTA.POSTURA_MINIMA_MINIMA_LOTES, expediente-rekeningnummer, SUBASTA.ID_SUBASTA_BUSCAR, SUBASTA.ACREEDORES, FECHA_FIN, FECHA_INICIO; sorteren op einddatum, ID, status, minimumbod; 50–500 resultaten per pagina. | https://subastas.boe.es/subastas_ava.php | 3 |
| Velden op een detailpagina (algemeen): identificador, tipo de subasta, cuenta expediente, fecha inicio/conclusión, cantidad reclamada, lotes, anuncio BOE (BOE-B-nummer), valor subasta, tasación, puja mínima, tramos entre pujas, importe del depósito. Tabblad "bienes": descripción, dirección, CP, localidad, provincia, **vivienda habitual (Sí/No)**, **situación posesoria**, **visitable**. | detailpagina's SUB-JA-2026-257820 en SUB-AT-2026-26R2886001392 | 3 |
| Waargenomen op 14-09-2026: provincie Alicante, onroerend goed, status "Celebrándose": 43 veilingen (overwegend rechtbanken Torrevieja/Orihuela/Elche/Alicante/Novelda/Alcoy en enkele AEAT). Plaatsnaam "JAVEA", alle statussen: 278 resultaten, waaronder Sección Civil TI Dénia (plazas 1, 2, 5), Juzgado Mercantil 1 Alicante, U.R. Subastas Valencia en Madrid (AEAT), een notariële veiling en veilingen van het Ayuntamiento de Xàbia (prefix SUB-RC). | subastas_ava.php (twee raadplegingen) | 3 |
| Voorbeelden van aangeboden rechten die geen volle eigendom zijn, letterlijk in de titel: "50% NUDA PROPIEDAD" (AEAT, Torrevieja) en "25% PLENO DOMINIO DE VIVIENDA ... DENIA" (AEAT). | subastas_ava.php provincie Alicante | 3 |
| Voorbeeld gerechtelijk (Jávea, garage/berging Edificio Veles al Vent, TI Dénia plaza 2, expediente 0952/18): valor subasta 20.877,50 €, tasación **0,00 €**, cantidad reclamada 17.182,33 €, depósito 1.043,87 € (= 5 %), tramos 417,55 €, sin puja mínima, vivienda habitual: No, situación posesoria: **No consta**, visitable: No consta. | detalleSubasta.php?idSub=SUB-JA-2026-257820 | 3 |
| Voorbeeld AEAT (Dénia, 25 % pleno dominio): valor subasta = tasación 40.945,66 €, puja mínima 4.094,57 € (= 10 %), tramos 1.000 €, depósito 2.047,28 € (= 5 %). | detalleSubasta.php?idSub=SUB-AT-2026-26R2886001392 | 3 |

**Gevolgtrekking (bewijstype 4):** de 5 %-waarborgsom in de gerechtelijke veiling van expediente 0952/18 (gestart 2018, veiling februari 2026) is consistent met de overgangsregel van LO 1/2025 (oud regime voor oude procedures, zie 2.1). Dit is één waarneming, geen bewijs van de uitleg die rechtbanken hanteren.

---

## 2. Gerechtelijke veiling — Ley 1/2000 de Enjuiciamiento Civil (LEC)

**Bron:** https://www.boe.es/buscar/act.php?id=BOE-A-2000-323 — geconsolideerde tekst, "Última actualización publicada el 28/02/2025". De veilingartikelen 636, 640–642, 647–657, 667–671 dragen de noot "Se modifica, con efectos de 3 de abril de 2025, por el art. 22 de la Ley Orgánica 1/2025, de 2 de enero" (BOE-A-2025-76). Oude tekst vergeleken via de versie van 20-12-2023: https://www.boe.es/buscar/act.php?id=BOE-A-2000-323&tn=1&p=20231220. Bewijstype voor alle artikelcitaten hieronder: **2**.

### 2.1 Overgangsrecht — welk regime geldt?

- LO 1/2025, disposición transitoria novena, lid 1: "Las previsiones recogidas por la presente ley serán aplicables exclusivamente a los procedimientos incoados con posterioridad a su entrada en vigor." (https://www.boe.es/buscar/act.php?id=BOE-A-2025-76, bewijstype 2.)
- Inwerkingtreding van de LEC-wijzigingen: 03-04-2025 (BOE-noot bij elk artikel, bewijstype 2).
- **Gevolg (bewijstype 4, [te verifiëren] bij advocaat):** een executie die vóór 03-04-2025 is ingeleid, wordt geveild volgens de oude artikelen (5 % waarborg, 40 dagen betaaltermijn, zelftoewijzing door de schuldeiser bij een lege veiling). Het jaartal in het expedientenummer ("0952/18", "1779/25") is een eerste indicatie, geen bewijs; het decreto de convocatoria en het edicto in het portaal zijn leidend. Omdat executies jaren lopen, blijven beide regimes nog lang naast elkaar bestaan.

### 2.2 Vergelijkingstabel oud regime ↔ nieuw regime (onroerend goed)

| Onderwerp | Oud (tekst tot 02-04-2025) | Nieuw (LO 1/2025, vanaf 03-04-2025) | Artikel |
|---|---|---|---|
| Waarborgsom | 5 % van de waarde van art. 666 | 20 % van de waarde van art. 666, minimaal 1.000 €; de LAJ mag het percentage verhogen of verlagen | 669.1 |
| Waarborgsom roerend goed / algemene regel | 5 % | 10 % of minimaal 1.000 €; LAJ mag aanpassen | 647.1.3.º |
| Betaaltermijn rest van de prijs | 40 dagen | 20 dagen na sluiting van de veiling | 670.1 en 670.4 |
| Bod ≥ 70 % | Toewijzing dezelfde of volgende dag | Toewijzing de dag na sluiting | 670.1 |
| Bod < 70 %: verbetering door derde via schuldenaar | Derde moet > 70 % bieden (of schuld volledig dekken) binnen 10 dagen | Derde moet ≥ 60 % bieden (of schuld volledig dekken) binnen 10 dagen; eerst depósito storten, daarna 10 dagen om te betalen | 670.3 |
| Bod < 70 % zonder verbetering | Schuldeiser kon zich het goed laten toewijzen voor 70 % of het verschuldigde (≥ 60 % en > beste bod); anders toewijzing aan beste bod > 50 % of dekkend | Toewijzing aan beste bod ≥ 50 %, of aan bedrag dat de schuldeiser volledig voldoet met minimum 40 % (dan eindigt de executie); anders beslist de LAJ na horen partijen | 670.3 |
| Eigen woning schuldenaar | (regel via 671 bij lege veiling) | Niet onder 70 % van de veilingwaarde, tenzij voor het volledig verschuldigde, en dan niet onder 60 %; als de schuldeiser zelf te laag bood: toewijzing op 70 % of het verschuldigde (min. 60 %) | 670.3, laatste alinea |
| Geen bieders | Schuldeiser kon binnen 20 dagen toewijzing vragen voor 50 % (niet-eigen woning) of het verschuldigde; eigen woning 70 % / 60 % | Schuldeiser kan géén toewijzing vragen ("Si no hubiera habido pujas, tampoco podrá solicitar la adjudicación de los bienes", 647.2). De schuldenaar (zelf of op voorstel van de schuldeiser) kan een persoon aanwijzen voor ≥ 50 % of een dekkend bedrag ≥ 40 %; lager: LAJ beslist; partijen kunnen samen een nieuwe veiling of art. 640 vragen; anders opheffing beslag op verzoek schuldenaar | 671, 647.2 |
| Schuldeiser als bieder | Alleen als er andere bieders waren | Mag altijd bieden zonder waarborg; kan na sluiting niet meer verbeteren | 647.2 |
| Cesión del remate | Alleen schuldeiser/latere schuldeisers, met voorbehoud bij het bod, via comparecencia | Schuldeiser en latere schuldeisers hebben het recht van rechtswege; cessie binnen 5 dagen na betaling; cessieprijs mag lager zijn dan het remate; een sobreprecio gaat naar de executie | 647.3 |
| Geheimhouding biedingen | (portaal toonde hoogste bod) | Biedingen zijn geheim tot sluiting; het portaal meldt tijdens de veiling niet of er biedingen zijn | 648.6.ª |
| Realización por entidad especializada als aparte sectie | Art. 641–642 | Sectie 4.ª geschrapt; de figuur leeft voort in het convenio de realización (640.1: "incluida la realización por persona o entidad especializada") | 640, 641, 642 |
| Certificación de cargas ouder dan 6 maanden | — | LAJ kan vóór het decreto de convocatoria een geactualiseerde nota simple opvragen, die in het portaal wordt gepubliceerd; het register meldt tijdens de veiling nieuwe titels aan LAJ en portaal | 656.2 |

### 2.3 Artikel voor artikel (huidige tekst)

**Art. 637–639 — Avalúo.** Taxatie door een perito van de Administración de Justicia, subsidiair overheidsdiensten of erkende taxateurs (638.1). 639.3: "La tasación de bienes o derechos se hará por su valor de mercado, sin tener en cuenta, en caso de bienes inmuebles, las cargas y gravámenes". Partijen en latere schuldeisers hebben 5 dagen voor bezwaar en eigen rapport (639.4). Art. 639 gewijzigd door RDL 6/2023 (in werking 20-03-2024).

**Art. 640 — Convenio de realización.** Partijen en belanghebbenden kunnen een andere realisatie afspreken, inclusief via een gespecialiseerde persoon/entiteit; bij inschrijfbare goederen is instemming nodig van de later ingeschreven schuldeisers en derde-bezitters (640.2). Lid 4: de regels over voortbestaan en doorhaling van lasten gelden ook bij zo'n overdracht.

**Art. 643.2 — Geen veiling** als de opbrengst naar verwachting niet eens de veilingkosten dekt.

**Art. 647 — Toelating.** Identificatie, ook of men voor derden handelt en voor welk percentage; de winnaar moet zijn vertegenwoordiging binnen **3 dagen** aantonen, anders verlies van depósito en doorschuiven naar de volgende bieder met reserva (647.1.1.º). Verklaring dat men de algemene en bijzondere voorwaarden kent (1.2.º). Waarborg 10 %/min. 1.000 € algemeen (1.3.º), via het portaal en de AEAT-passarelle.

**Art. 648 — Elektronische veiling.** Uniek identificatienummer; opening minstens 24 uur na de BOE-aankondiging; de aanvrager betaalt de BOE-tasa; identificatie volgens art. 6 RDL 6/2023; ejecutante, ejecutado of derde-bezitter kunnen via de oficina judicial taxatierapporten en andere documenten naar het portaal sturen (regel 5.ª); biedingen met tijdstempel; een bieder mag hoger of lager herbieden, alleen het laatste bod telt; bij gelijke bedragen wint het eerdere; biedingen geheim (regel 6.ª).

**Art. 649 — Duur en einde.** "durante el plazo improrrogable de veinte días naturales desde su apertura"; kan niet eindigen op zaterdag, zondag, nationale feestdag, 24-12 t/m 06-01 of in augustus. Faillissement van de schuldenaar → schorsing en de veiling wordt zonder effect, ook als al gestart. Schorsing > 15 kalenderdagen → annulering met teruggave van depósitos; ≤ 15 dagen → pauze en hervatting (649.2). Na sluiting stuurt het portaal de gecertificeerde winnende bieding; als de winnaar niet betaalt, de volgende met reserva (649.3). Decreto de aprobación del remate onmiddellijk als het bod aan de eisen voldoet (649.4).

**Art. 650 — Roerend goed** (relevant als spiegel): ≥ 50 % → toewijzing, betaling binnen 10 dagen; < 50 % → schuldenaar 10 dagen voor een derde ≥ 50 %; anders toewijzing bij ≥ 30 % of dekkend bedrag.

**Art. 652 — Teruggave en reserva de postura.** "el Portal de Subastas devolverá inmediatamente los depósitos de los postores excepto lo que corresponda al mejor postor"; wie reserva vraagt, houdt zijn depósito vast zodat bij wanbetaling van de winnaar de volgende aan de beurt is; de tweede krijgt alleen het goed als zijn bod + het verbeurde depósito van de eerste het mislukte remate evenaart; nooit als het verbeurde depósito al kapitaal, rente en kosten dekt (652.1). Teruggave aan wie stortte, ook als hij voor een ander handelde (652.2).

**Art. 653 — Quiebra de la subasta.** Wie niet betaalt "perderá el depósito que hubiera efectuado y se procederá a nueva subasta"; het verbeurde depósito gaat naar de executie, eventueel eerst naar de kosten van de nieuwe veiling en compensatie van een lagere opbrengst (653.2).

**Art. 654 en 672 — Bestemming van de opbrengst.** Aan de schuldeiser tot het bedrag van de executie; overschot eerst voor later ingeschreven rechthebbenden (672.1), rest aan schuldenaar of derde-bezitter. Toerekening bij tekort: rente, hoofdsom, vertragingsrente, kosten (654.3).

**Art. 655 bis — vernietigd.** Toegevoegd door Ley 12/2023 (vivienda), ongrondwettig verklaard door STC 26/2025 van 29-01-2025 (BOE-A-2025-4079).

**Art. 656 — Certificación de dominio y cargas.** Elektronisch en gestructureerd; inhoud: eigendom en zakelijke rechten, "relación completa de las cargas inscritas que lo graven o, en su caso, que se halla libre de cargas". Nota marginal in het register; > 6 maanden → geactualiseerde nota simple naar het portaal; het register meldt nieuwe titels tijdens de veiling; código registral único (CRU) gaat mee naar het portaal (656.2).

**Art. 657 — Actuele stand van voorgaande lasten.** De LAJ vraagt ambtshalve aan voorgaande of gelijkrangige schuldeisers en aan de schuldenaar of het krediet nog bestaat en voor welk bedrag, met vervaldatum en dagrente; bij overeenstemming mandamiento ex art. 144 LH, bij onenigheid een zitting binnen 3 dagen. Niet antwoorden → boetes (657.3).

**Art. 658 — Goed op naam van een ander** dan de schuldenaar → beslag wordt opgeheven, tenzij de inschrijving van na het beslag dateert (dan art. 662).

**Art. 659 — Later ingeschreven rechthebbenden** worden door het register ingelicht; wie na de certificación inschrijft, krijgt geen bericht maar kan tussenkomen; latere schuldeisers die vóór het remate betalen, subrogeren.

**Art. 661 — Bezetters.** Bekende bewoners (huurders of feitelijke bezetters) krijgen 10 dagen om hun titel te tonen; de publicatie "expresará, con el posible detalle, la situación posesoria del inmueble o que, por el contrario, se encuentra desocupado" — alleen als dat aan de LAJ is aangetoond. De ejecutante kan vóór de aankondiging laten verklaren dat bezetters géén recht hebben om te blijven (661.2); die verklaring komt in de publicatie.

**Art. 662 — Tercer poseedor**, ook wie alleen vruchtgebruik of blote eigendom verwierf (662.2); kan het goed bevrijden door te betalen tot aan de aansprakelijkheidsgrens.

**Art. 666 — Veilingwaarde.** "saldrán a subasta por el valor que resulte de deducir de su avalúo ... el importe de todas las cargas y derechos anteriores al gravamen por el que se hubiera despachado ejecución"; als de lasten de waarde evenaren of overtreffen, wordt de executie op dat goed geschorst (666.2).

**Art. 667 — Convocatoria en registerkoppeling.** Het portaal vraagt via het Colegio de Registradores een elektronische registerinformatie die tot het einde permanent wordt bijgewerkt en via het portaal wordt geserveerd, met grafische gegevens; als die na 48 uur niet kan worden geleverd, start de veiling toch (667.2).

**Art. 668 — Inhoud van het edicto.** Identificatie van de finca met registergegevens, CRU en referencia catastral; "necesariamente, la certificación de dominio y cargas", het avalúo/de tasación inclusief het extrajudiciële taxatierapport uit de executoriale titel, de minoración de cargas preferentes met de ontvangen antwoorden (art. 657) en de bezitssituatie; de mogelijkheid tot bezichtiging (669.3). Verder: "las cargas, gravámenes y asientos anteriores al crédito del actor continuarán subsistentes y que, por el solo hecho de participar en la subasta, el licitador los admite y acepta quedar subrogado". De koper aanvaardt de titulación zoals die in de procedure is of het ontbreken ervan.

**Art. 669 — Bijzondere voorwaarden.** 20 %-waarborg (2.2). 669.2: de bieder aanvaardt de titulación en subrogeert in eerdere lasten. 669.3: iedere belangstellende kan tijdens de biedperiode het tribunal om bezichtiging vragen; werkt de bezitter mee, dan kan de schuld met maximaal 2 % van de toewijzingswaarde worden verminderd. 669.4: hervatting na > 15 dagen schorsing = nieuwe publicatie en nieuwe registerinformatie.

**Art. 670 — Toewijzing, betaling, lasten.** Drempels: zie 2.2. 670.5: "habrá de aceptar la subsistencia de las cargas o gravámenes anteriores, si los hubiere y subrogarse en la responsabilidad derivada de ellos." 670.6: op verzoek geeft de LAJ direct een testimonio van het decreto de aprobación om een hypotheek te vestigen (art. 107.12.º LH) — de betaaltermijn wordt daardoor opgeschort tot afgifte. 670.7: de schuldenaar kan tot de goedkeuring bevrijden door alles te betalen; de veiling wordt dan geannuleerd. 670.8: na storting van het restant worden de reserva-depósitos vrijgegeven en volgt het decreto de adjudicación.

**Art. 671 — Geen bieders.** Zie 2.2.

**Art. 673 — Titel voor inschrijving:** het testimonio van het decreto de adjudicación; vermeldt of de koper krediet heeft verkregen voor de prijs en het depósito, met bedragen en kredietgever (voor art. 134 LH).

**Art. 674 — Doorhaling van lasten.** "A instancia del adquirente, se expedirá ... mandamiento de cancelación de la anotación o inscripción del gravamen que haya originado el remate"; de LAJ beveelt doorhaling van alle latere inschrijvingen en aantekeningen, ook die van ná de certificación; het mandamiento vermeldt of de prijs ≤ de vordering was of dat het overschot is ingehouden; op verzoek elektronische verzending naar het register.

**Art. 675 — Bezit en ontruiming.** 675.1: bezitsverschaffing op verzoek als het goed niet bezet is. 675.2: bij bezetting bevel tot ontruiming "con fijación de día y hora exacta" als het tribunal al ex 661.2 heeft beslist; anders kan de koper binnen **1 jaar** na verkrijging het lanzamiento van bezetters zonder toereikende titel vragen; daarna alleen in de gewone procedure. 675.3: zitting binnen 10 dagen; auto zonder beroep; niet verschijnen = ontruiming. (Gewijzigd door Ley 12/2023, in werking 26-05-2023.)

**Art. 681–698 — Hypotheekexecutie.**
- 682.2.1.º: de in de hypotheekakte overeengekomen tipo "no podrá ser inferior, en ningún caso, al 75 por cien del valor señalado en la tasación" (verwijzing naar art. 18 RDL 24/2021; artikel gewijzigd door RDL 6/2023, in werking 20-03-2024).
- 685.2: de demanda moet vermelden of het de eigen woning van de schuldenaar is en of de eiser "gran tenedor" is; bij een gran tenedor, eigen woning en kwetsbare schuldenaar is voorafgaande bemiddeling vereist (Ley 12/2023; een deel van lid 2 is door STC 26/2025 vernietigd).
- 688: certificación met letterlijke inschrijving van de hypotheek; nota marginal die doorhaling om andere redenen blokkeert; bestaat de hypotheek niet of is zij doorgehaald → einde executie.
- 690: schuldeiser kan voorlopig beheer/bezit vragen (max. 2 jaar bij onroerend goed).
- 691: veiling na 20 dagen sinds requerimiento; volgens 667/668 en de regels voor onroerend goed (691.4); bij faillissement schorsing, hervatting alleen met verklaring van de faillissementsrechter dat het goed niet nodig is voor de activiteit (691.5); convenio en entidad especializada ook toegelaten (691.6).
- 692: opbrengst eerst aan de hypotheekhouder binnen de hypothecaire dekking; overschot voor latere ingeschrevenen; rest aan de eigenaar; het mandamiento vermeldt ook de kennisgevingen van 689 (692.3).
- 693: verzuim van ten minste 3 maandtermijnen (693.1); vervroegde opeisbaarheid bij consumentenhypotheken op woningen volgens art. 24 Ley 5/2019 (LCCI) en art. 129 bis LH (693.2; gewijzigd door Ley 5/2019, in werking 16-06-2019); de schuldenaar kan tot de sluiting van de veiling bevrijden door het achterstallige te consigneren — bij de eigen woning zelfs zonder instemming van de schuldeiser, herhaalbaar na 3 jaar (693.3). De drempels van art. 24 LCCI zelf zijn in deze sessie niet uit de brontekst gelezen (extractie mislukt) — **[te verifiëren]**.
- 695: beperkte verzetgronden, waaronder oneerlijke bedingen (695.1.4.ª); verzet schorst (695.2); 695.3 gewijzigd door RDL 6/2023.
- 696–698: tercería de dominio (titel van vóór de hypotheek), strafrechtelijke prejudicialiteit, andere geschillen schorsen niet.

**Notariële venta extrajudicial (art. 129 LH):** één elektronische veiling op het BOE-portaal; "Los tipos en la subasta y sus condiciones serán, en todo caso, los determinados por la Ley de Enjuiciamiento Civil" (129.2.d); tipo niet lager dan bij de gerechtelijke executie; de notaris schorst bij een ingeroepen oneerlijk beding. Bron: https://www.boe.es/buscar/act.php?id=BOE-A-1946-2453 (consolidatie 03-01-2025), bewijstype 2.

**Ley Hipotecaria 131–134 (zelfde bron):** 132 — de registrador toetst o.a. dat het verkochte ≤ de vordering was of dat het overschot is geconsigneerd; 133 — testimonio + mandamiento (art. 674 LEC) zijn de titel; 134 — inschrijving op naam van de koper en doorhaling van de geëxecuteerde hypotheek "así como la de todas las cargas, gravámenes e inscripciones de terceros poseedores que sean posteriores a ellas, sin excepción"; alleen latere obras nuevas en divisiones horizontales blijven als de hypotheek zich daartoe uitstrekt.

### 2.4 Wijzigingshistorie van de veilingartikelen (uit de BOE-noten, bewijstype 2)

| Wet | Effect op veilingregels | Bron-ID |
|---|---|---|
| Ley 13/2009 | Overheveling naar de Secretario judicial (nu LAJ) | BOE-A-2009-17493 |
| RDL 8/2011 en Ley 1/2013 | Verlaging waarborg naar 5 %, drempels 70/60/50 %, eigen-woningbescherming | BOE-A-2011-11641, BOE-A-2013-5073 |
| RDL 7/2013 | Art. 669.1 (waarborg) | BOE-A-2013-7062 |
| **Ley 19/2015** | Elektronische veiling op het BOE-portaal (648), 40 dagen betaaltermijn, cesión, certificación elektronisch | BOE-A-2015-7851 |
| Ley 42/2015 | 648, 649, 656, 660, 671 | BOE-A-2015-10727 |
| LO 7/2015 | "Secretario judicial" → "Letrado de la Administración de Justicia" | BOE-A-2015-8167 |
| **Ley 5/2019 (LCCI)** | 693.2 vervroegde opeisbaarheid (16-06-2019) | BOE-A-2019-3814 |
| **Ley 12/2023 (vivienda)** | 655 bis (vernietigd), 675 (ontruiming met dag en uur), 685.2 (gran tenedor) | BOE-A-2023-12203 |
| **RDL 6/2023** | 634, 635, 639, 682.2, 695.3; identificatie ex art. 6 (in werking 20-03-2024) | BOE-A-2023-25758 |
| **LO 1/2025** | Alle kernartikelen 636, 640–642, 647–657, 667–671 (03-04-2025): waarborg 20 %, 20 dagen, geheime biedingen, geen zelftoewijzing, nieuwe cessieregels | BOE-A-2025-76 |
| **STC 26/2025** | Vernietiging 655 bis en deel van 685.2 (28-02-2025) | BOE-A-2025-4079 |

Percentages 70/60/50 en de eigen-woningregel zijn dus ná Ley 19/2015 en Ley 5/2019 niet gewijzigd; RDL 6/2023 raakte ze niet; **LO 1/2025 wél** (waarborg, termijnen, 40 %-ondergrens, einde zelftoewijzing).

---

## 3. AEAT — Reglamento General de Recaudación (RD 939/2005)

**Bron:** https://www.boe.es/buscar/act.php?id=BOE-A-2005-14803 — "Última actualización publicada el 31/01/2024" (RD 117/2024, in werking 01-02-2024; eerder RD 1071/2017, in werking 01-01-2018). Ley 58/2003 (LGT) art. 172: https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186 (consolidatie 21-12-2024). AEAT-pagina's: https://sede.agenciatributaria.gob.es/Sede/subastas.html en .../subastas/licitadores.html. Bewijstype 2, tenzij anders vermeld.

| Onderwerp | Regel | Artikel |
|---|---|---|
| Via BOE-portaal? | Ja: "La subasta de los bienes será única y se realizará por medios electrónicos en el Portal de Subastas de la Agencia Estatal Boletín Oficial del Estado" (uitzondering: uitbesteed aan gespecialiseerde bedrijven, art. 105). AEAT-site: "La AEAT subasta regularmente a través del portal del BOE bienes de todo tipo"; eigen zoeker en abonnement op meldingen van nieuwe goederen; aparte pagina "Otras subastas" voor douane-veilingen buiten het portaal. | RGR 100.2; sede AEAT |
| Waardering en tipo | Marktwaarde; tegen-taxatie door de schuldenaar binnen 15 dagen; verschil ≤ 20 % → hoogste taxatie geldt; anders derde perito binnen de bandbreedte. Tipo = waardering − actuele waarde van eerdere zakelijke lasten; als de lasten de waarde overtreffen: tipo = schuld + kosten (max. de waarde). "Las cargas y gravámenes anteriores quedarán subsistentes sin aplicar a su extinción el precio del remate." Bij een tweede veiling coëfficiënt 0,8; derde en volgende 0,6 (RD 117/2024). Vermoeden van gesimuleerde lasten → juridische dienst. | 97.1–8 |
| Hypotheken van de Hacienda | Executie via apremio; certificación ex art. 688 LEC; tipo mag afwijken van de taxatie bij hypotheekvestiging. | 74.6 |
| Titels | Als er geen ingeschreven titels zijn, moet de koper zelf de inschrijving regelen (Título VI LH); de Staat geeft alleen het verkoopdocument. | 98.2 |
| Vormen | Subasta (gewoon), concurso (marktverstoring/openbaar belang), adjudicación directa (na concurso, bederfelijke goederen, geen concurrentie mogelijk). | 100.1, 106, 107; LGT 172.1 |
| Aankondiging | Kennisgeving aan schuldenaar, echtgenoot (gananciales/eigen woning), latere ingeschreven schuldeisers, mede-eigenaren, derde-bezitters; minstens 15 dagen daarna; BOE-aankondiging, opening ≥ 24 uur later. Het portaal vermeldt o.a.: tipo **exclusief indirecte belastingen** (101.4.b), depósito 5/10 % (101.4.c), lasten die blijven bestaan (101.4.e), betaaltermijn 15 dagen (101.4.f). | 101 |
| Bevrijding door schuldenaar | Tot de certificación del acta of de escritura: betaling ex art. 169.1 LGT → veiling geschorst. | 101.2, 101.4.d, 104.4; LGT 172.4 |
| Bieders | Iedereen met handelingsbekwaamheid behalve personeel van de invorderingsdienst, taxateurs, bewaarders en betrokken ambtenaren; registratie op het portaal. **Cesión del remate alleen** voor bieders die via "colaboración social" (vastgoedbemiddelaars met akkoord, 100.5) deelnemen (103.3); AEAT-site: "Si no indica que participa en representación de un tercero, habrá participado en nombre propio y no cabe la posibilidad de ceder el remate al tercero, tan solo se podría realizar una ulterior transmisión (con doble tributación)." | 103; sede AEAT licitadores |
| Depósito | "Un depósito del 5 por ciento del tipo de subasta cuando los bienes o los lotes por los que desee pujar sean bienes inmuebles"; 10 % bij uitsluitend roerend. Reserva de depósito op verzoek; een bod ≤ het hoogste bod wordt automatisch gereserveerd (103 bis.3). Na afloop komen niet-gereserveerde depósitos vrij behalve dat van de beste bieder; gereserveerde pas als de winnaar heeft betaald. | 103 bis |
| Verloop | 20 kalenderdagen; biedingen worden **direct gepubliceerd** en de overboden bieder wordt gewaarschuwd (anders dan LEC 648.6.ª); puja mínima = 10 % van de tipo, tenzij lasten ≥ 25 % van de waardering; verlenging tot één uur na het laatste bod, max. 24 uur. | 104 |
| Toewijzing | Mesa binnen 15 kalenderdagen na sluiting; bod ≥ 50 % van de tipo → toewijzing; < 50 % → de Mesa beslist "atendiendo al interés público y sin que exista precio mínimo de adjudicación". Voorkeursrechten (tanteo) van derden schorsen de toewijzing. | 104 bis.1, 104 bis.3.a |
| Betaling | Binnen 15 dagen na kennisgeving van de toewijzing, anders "perderá el importe del depósito que se aplicará a la cancelación de las deudas" plus aansprakelijkheid voor schade. Bij wanbetaling: toewijzing aan de hoogste bieder met gereserveerd depósito of veiling vervallen verklaard. | 104 bis.1.a, 104 bis.3.b–c |
| Titel en lasten | Certificación del acta de adjudicación = "documento público de venta"; vermeldt uitdoving van de anotación preventiva van de Hacienda; mandamiento tot doorhaling van **latere** lasten (111.3). Optie: escritura pública, te kiezen binnen 5 dagen, met **extra 5 %** storting; akte binnen 30 dagen. Sobrante naar de schuldenaar of Caja General de Depósitos. | 104 bis.3.e–f, 111 |
| Adjudicación directa | Na een concurso zonder toewijzing, bederfelijke goederen of gemotiveerd gebrek aan concurrentie; aankondiging op de sede electrónica, telematische offertes; minimumprijs = tipo van het concurso of marktwaarde; halen offertes dat niet, dan mogelijk zonder minimum; na het traject kan iedereen die de tipo van het concurso betaalt het goed krijgen vóór toewijzing aan de Hacienda. | 107 |
| Toewijzing aan de Hacienda | Voor het bedrag van de schuld, "sin que, en ningún caso, pueda rebasar el 75 por ciento del tipo inicial". | LGT 172.2; RGR 109 |
| Geen verkoop vóór onherroepelijke aanslag | "La Administración tributaria no podrá proceder a la enajenación ... hasta que el acto de liquidación de la deuda tributaria ejecutada sea firme" (uitzonderingen). | LGT 172.3 |

Normen die de AEAT zelf op haar veilingpagina opsomt (bewijstype 2): LGT art. 172; RGR art. 97–115; LEC; Ley 42/2015; Ley 19/2015; Ley del Notariado; Ley 15/2015; RD 1011/2015; Resolución de 13-10-2016 (procedure depósitos); Código Civil art. 1457 e.v.

---

## 4. TGSS — Reglamento General de Recaudación de la Seguridad Social (RD 1415/2004)

**Bron:** https://www.boe.es/buscar/act.php?id=BOE-A-2004-11836 — "Última actualización publicada el 30/07/2026" (art. 120.5 en 120.7 gewijzigd door RD 322/2024). Bewijstype 2.

| Onderwerp | Regel | Artikel |
|---|---|---|
| Kanaal | Aankondiging "en el tablón de anuncios de la Seguridad Social situado en la sede electrónica de la Secretaría de Estado de la Seguridad Social"; eventueel ook media. Offertes in **gesloten enveloppe** in te dienen bij de Dirección Provincial (118.3); mondelinge biedingen ter zitting. **Geen verwijzing naar het BOE-portaal aangetroffen** in dit reglement; op seg-social.es en sede.seg-social.gob.es is de veilingpagina op 14-09-2026 niet gevonden (zie blokkades). | 117.1, 118, 120 |
| Waardering en tipo | Marktwaarde, tegen-taxatie binnen 15 dagen, 20 %-regel, derde perito. Tipo = waarde − eerdere preferente lasten, "que quedarán subsistentes, sin aplicarse a su extinción el precio del remate"; overtreffen de lasten de waarde, dan tipo = schuld (max. waarde). | 110, 111 |
| Termijn offertes | Minstens één maand (providencia de subasta). Kennisgeving aan schuldenaar, echtgenoot, mede-eigenaren, hypotheek-/pandhouders en eerdere beslagleggers. | 116 |
| Depósito | Bij elke schriftelijke offerte een gecertificeerde/geconformeerde cheque op naam van de TGSS "por importe, en todo caso, del 25 por ciento del tipo de subasta"; mondeling bieden ter zitting (≥ 75 % van de tipo) vereist ter plekke 30 % van de tipo. | 117.2.e–f, 118.2, 120.2 |
| Toewijzingsdrempels | Eerste veiling: beste bod > 60 % van de tipo, of lager maar dekkend voor de schuld (bij onroerend goed nooit < 25 %); tweede veiling: > 50 % (idem 25 %-ondergrens), of tussen 25 % en 50 % met gemotiveerd besluit van de directeur. Mondelinge biedingen in stappen van ≥ 2 %. Bij een bod < 75 % dat de schuld niet dekt: schuldenaar mag binnen **3 werkdagen** een derde aandragen die tot 75 % verbetert. | 120.3, 120.5, 120.7 |
| Betaling | Verschil binnen **5 werkdagen** na toewijzing; anders verlies van depósito "y quedará obligado a resarcirle de los mayores perjuicios". | 117.2.g, 120.8, 120.10 |
| Cesión | Cessie aan een derde via gezamenlijke comparecencia bij de Dirección Provincial binnen dezelfde 5 werkdagen, na betaling. | 120.9 |
| **Voorkeursrecht TGSS** | "podrá ejercitar derecho de tanteo con anterioridad a la emisión del certificado de adjudicación ... en el plazo máximo de 30 días"; de koper krijgt depósito en betaalde prijs terug. Dit is een specifiek risico van TGSS-veilingen: winnen is pas zeker na 30 dagen. | 121 |
| Titel en lasten | Certificado de adjudicación (met lasten die blijven) = titel voor inschrijving; doorhaling van latere lasten; escritura op verzoek. "Los gastos que origine la transmisión de la propiedad del bien adjudicado, incluidos los fiscales y registrales, serán siempre a cargo del adjudicatario." Regeling voor btw-facturatie door een ondernemer-koper (DA 5.ª RIVA). | 122 |
| Adjudicación directa | Uitzonderlijk, na een lege tweede veiling of als concurrentie niet mogelijk/wenselijk is; zonder minimum, maar bij onroerend goed alleen ≥ 25 % van de tipo (tenzij ter zitting mondeling 25 % wordt geboden). | 123 bis |
| Toewijzing aan de TGSS | Voor de schuld, max. 80 % van de tipo. | 124.2 |

---

## 5. Faillissement — Texto Refundido de la Ley Concursal (RDL 1/2020)

**Bron:** https://www.boe.es/buscar/act.php?id=BOE-A-2020-4859 — "Última actualización publicada el 03/01/2025" (hervorming Ley 16/2022, in werking 26-09-2022). Bewijstype 2. Registro Público Concursal: https://www.publicidadconcursal.es/ (beheer: Colegio de Registradores in opdracht van het ministerie van Justitie; portal de liquidaciones: https://www.publicidadconcursal.es/liquidaciones).

| Onderwerp | Regel | Artikel |
|---|---|---|
| Vóór de liquidatie | Geen vervreemding zonder rechterlijke machtiging (205), behalve o.a. niet-noodzakelijke goederen met een bod dat het inventariswaarde benadert (< 10 % afwijking bij onroerend goed) en zonder hoger bod binnen 10 dagen (206.2). | 205, 206 |
| "Plan de liquidación" bestaat niet meer | Art. 416, 417, 419 staan als "(Suprimido)". In de plaats: **reglas especiales de liquidación** die de rechter bij de opening of later vaststelt (415); de rechter mag geen voorafgaande machtiging per verkoop eisen en geen regels die de liquidatie > 1 jaar rekken (415.2); schuldeisers met > 50 % van het passief kunnen de regels laten vervallen (415.4). Zonder regels: de administrador concursal verkoopt "del modo más conveniente para el interés del concurso" (421). | 415–421 |
| Publiciteit | De AC moet informatie voor de verkoop naar het "portal de liquidaciones concursales del Registro público concursal" sturen (rechtspersonen). Het portaal filtert op proceduretype (o.a. "venta de unidades productivas en la fase de liquidación concursal (art. 415 bis)") en verkoopwijze "Venta directa / Subasta / Otro". | 415 bis; RPC-portaal (bewijstype 3) |
| Veiling verplicht? | Goederen > 5 % van de inventariswaarde: elektronische veiling "bien en el portal de subastas de la Agencia Estatal Boletín Oficial del Estado, bien en cualquier otro portal electrónico especializado en la liquidación de activos", tenzij de rechter anders bepaalt. Ondernemingen/unidades productivas als geheel (422). | 422, 423 |
| Entidad especializada / directe verkoop | Rechter kan bij auto, ook bij lege veiling, directe verkoop of verkoop via een gespecialiseerde persoon/entiteit toestaan (216); bezwaarde goederen: realización directa alleen boven het bij vestiging overeengekomen minimum en contant, of lager met instemming en actuele officiële taxatie, gevolgd door publicatie met 10 dagen voor betere biedingen (210). | 210, 216 |
| Bezwaarde goederen (hypotheek) | Realisatie door de AC via elektronische veiling tenzij de rechter anders toestaat (209); dación en pago (211); verkoop **met behoud van de hypotheek en subrogatie van de koper** (212) — niet voor fiscale en SS-vorderingen; de bevoorrechte schuldeiser ontvangt tot zijn oorspronkelijke vordering (213, 430). Lege veiling: hypotheekhouder mag zich het goed laten toewijzen "en los términos ... establecidos por la legislación procesal civil"; anders toewijzing tegen inventariswaarde als die lager is dan de schuld, of nieuwe veiling zonder minimum (423 bis). | 209–213, 423 bis, 430 |
| Doorhaling van lasten | "se acordará la cancelación de todas las cargas anteriores al concurso constituidas a favor de créditos concursales. **Los gastos de la cancelación serán a cargo del adquirente.**" Niet bij verkoop met behoud van het gravamen. | 225 |
| Executie van zekerheden tijdens concurso | Vanaf de faillietverklaring geen nieuwe executies op goederen die nodig zijn voor de activiteit en schorsing van lopende, "aunque ya estuviesen publicados los anuncios de subasta" (145); hervatting alleen met verklaring van niet-noodzakelijkheid (146–147) of na een jaar zonder liquidatie / bij convenio (148); opening liquidatie: verlies van het recht op afzonderlijke executie, herstel na een jaar zonder verkoop (149). Spiegel in LEC 649.1 en 691.5. | 145–149 |

**Koop van een vordering versus koop van het actief (bewijstype 4, op basis van bovenstaande artikelen):**
- Wie een (hypothecaire) vordering koopt, wordt schuldeiser met privilegio especial; hij krijgt de opbrengst van het bezwaarde goed tot zijn oorspronkelijke vordering (213, 430), kan bij een lege veiling toewijzing vragen (423 bis) en heeft in de LEC-executie het cessierecht (647.3). Hij wordt **niet** eigenaar; de ejecución kan geschorst zijn (145) en de AC kan kiezen voor betaling uit de boedel zonder verkoop (430.2).
- Wie het actief koopt (veiling, directe verkoop, entidad especializada) verkrijgt eigendom met doorhaling van pre-concursale lasten (225), tenzij verkocht met behoud van het gravamen (212) — dan neemt hij de schuld over.
- Beide sporen vergen een eigen dossier; de prijs van een vordering zegt niets over de waarde van het huis (masterprompt sectie 18).

**Gebruiksvoorwaarden RPC (bewijstype 2, https://www.publicidadconcursal.es/aviso-legal):** persoonsgegevens in het RPC mogen uitsluitend voor de wettelijke doelen worden gebruikt: "Queda expresamente prohibida su reutilización, tratamiento ulterior, cesión a terceros o utilización para fines distintos"; het CORPME houdt de IE-rechten op platform en inhoud. Gevolg: objectgerichte handmatige raadpleging is mogelijk; systematisch kopiëren of profielen bouwen niet.

---

## 6. Fiscaal bij toewijzing (Comunitat Valenciana)

| Onderwerp | Bevinding | Bron | Bewijstype |
|---|---|---|---|
| Belastbaar feit / belastingplichtige ITP | Onerose overdracht van onroerend goed, ook "adjudicaciones en pago y para pago de deudas" (7.2.A); belastingplichtige is de verkrijger (8.a). | TRLITPAJD RDL 1/1993, https://www.boe.es/buscar/act.php?id=BOE-A-1993-25359 | 2 |
| Grondslag algemeen | Onroerend goed: "su valor será el valor de referencia previsto en la normativa reguladora del catastro inmobiliario"; is de verklaarde waarde of de prijs hoger, dan die (10.2). Alleen lasten die de waarde verminderen zijn aftrekbaar, "pero no las deudas aunque estén garantizadas con prenda o hipoteca" (10.1). | idem, art. 10 | 2 |
| Grondslag bij veiling | Reglamento ITP art. 39: "En las transmisiones realizadas mediante subasta pública, notarial, judicial o administrativa, servirá de base el valor de adquisición, siempre que consista en un precio en dinero marcado por la Ley o determinado por autoridades o funcionarios idóneos para ello." | RD 828/1995, https://www.boe.es/buscar/act.php?id=BOE-A-1995-15071 (consolidatie 09-11-2018) | 2 |
| **Spanning** | Art. 10.2 TRLITPAJD (wet, valor de referencia sinds Ley 11/2021) en art. 39 RITP (reglement, toewijzingsprijs) zeggen niet hetzelfde; welke de ATV (Generalitat) bij een veilingprijs onder de valor de referencia toepast, is in deze sessie niet uit een officiële bron vastgesteld. Reken in het model met **de hoogste van beide** tot een gestor/advocaat het tegendeel bevestigt. | — | 7 / **[te verifiëren]** |
| Tarief ITP CV | "El 9 % en las adquisiciones de inmuebles ... cuando el valor ... sea superior a un millón de euros, el tipo aplicable será el 11 %"; 8 % o.a. bij eerste eigen woning van jongeren < 35 jaar en bij bedrijfsvastgoed onder voorwaarden. Datum van inwerkingtreding van deze tariefstelling niet uitgelezen. | Ley 13/1997 CV, https://www.boe.es/buscar/act.php?id=BOE-A-1998-8202 (consolidatie 02-07-2026), art. 13 | 2, ingangsdatum **[te verifiëren]** |
| AJD | Alleen bij een notariële eerste kopie met inschrijfbare, waardeerbare inhoud (TRLITPAJD 31.2); grondslag = verklaarde waarde, niet lager dan art. 10 (30.1). CV-tarief: 1,4 % algemeen; 2 % bij afstand van btw-vrijstelling; 0,1 % eigen woning (Ley 13/1997 art. 14). | idem | 2 |
| AJD bij gerechtelijke toewijzing | De titel is het testimonio van het decreto de adjudicación (LEC 673), geen notariële akte; AEAT/TGSS geven een certificación del acta (RGR 104 bis.3.e; RGR-SS 122.1) — pas als de koper voor een escritura kiest (RGR 111; RGR-SS 122.2) ontstaat een notarieel document. Of AJD dan verschuldigd is en op welke grondslag: niet uit een fiscale bron vastgesteld. | LEC, RGR, RGR-SS | 4, **[te verifiëren]** |
| Btw in plaats van ITP | Is de ejecutado ondernemer en gaat het om een eerste levering, een bouwkavel of een verkoop met afstand van vrijstelling, dan kan btw (met AJD 2 % in CV) gelden in plaats van ITP. RGR-SS 122.3 regelt uitdrukkelijk dat een ondernemer-koper de factuur mag uitreiken en de vrijstelling mag afwijzen (DA 5.ª RIVA); RGR 101.4.b: tipo exclusief indirecte belastingen. De Ley del IVA zelf is niet geraadpleegd. | RGR-SS 122.3; RGR 101.4.b | 2 voor de reglementen; regime zelf **[te verifiëren]** |
| Plusvalía (IIVTNU) | Belastingplichtige bij onerose overdracht: "la persona ... que transmita el terreno" (106.1.b) — dus de ejecutado. **Maar:** is de vervreemder "una persona física no residente en España", dan is de verkrijger "sujeto pasivo sustituto del contribuyente" (106.2). Niet verschuldigd als geen waardestijging wordt aangetoond (104.5). Verschuldigd op de datum van overdracht (109.1). Coëfficiënten/tarief per gemeentelijke verordening Xàbia: niet geraadpleegd. | TRLHL RDL 2/2004, https://www.boe.es/buscar/act.php?id=BOE-A-2004-4214 (consolidatie 03-06-2026) | 2; verordening **[te verifiëren]** |
| Kosten doorhaling lasten | LEC 674: mandamiento op verzoek van de koper; wie het registerhonorarium betaalt, staat niet in de LEC (niet gevonden). TRLC 225.1: kosten voor de koper. RGR-SS 122.5: fiscale en registerkosten altijd voor de koper. Praktisch model: kosten van inschrijving en doorhaling voor de koper. | LEC, TRLC, RGR-SS | 2 (TRLC, TGSS); LEC-praktijk 4 **[te verifiëren]** |
| Eerdere lasten die blijven | Hypotheken/beslagen van vóór het geëxecuteerde recht (LEC 668.2/670.5; RGR 97.6; RGR-SS 111.2). Daarnaast bestaan wettelijke "afecciones" (IBI-schulden op het goed, gemeenschapsbijdragen VvE) die niet in deze bronnen zijn gecontroleerd. | zie art. | 2; afecciones **[te verifiëren]** |

---

## 7. Juridisch dossier-sjabloon (masterprompt sectie 19, uitgebouwd)

Per veld: waar de informatie vandaan komt en wanneer het veld een **blokkade** oplevert. "Portaal" = subastas.boe.es-detailpagina (tabbladen: algemeen, autoridad gestora, bienes, lotes, documenten); "edicto" = BOE-B-aankondiging; "certificación" = certificación de dominio y cargas (LEC 656/688; RGR 74.6/97.5; RGR-SS 111.2).

| # | Veld | Bron van de informatie | Blokkade / beslisgrens |
|---|---|---|---|
| 1 | Officiële bron en veiling-ID | Portaal (identificador SUB-JA/SUB-NN/SUB-AT/SUB-RC-…); anuncio BOE-B-nummer; voor TGSS: tablón sede electrónica; voor concurso: RPC + portaal | Geen officieel ID → geen dossier |
| 2 | Zaak- en veilingnummer, cuenta expediente | Portaal (cuenta expediente, expediente n.º/jaar) | Jaartal < 2025 bij gerechtelijke veiling → oud LEC-regime aannemen tot het edicto anders zegt |
| 3 | Verkopende/beherende instantie | Portaal (autoridad gestora), edicto | Onbekende of niet-officiële instantie → NIET GEBRUIKEN |
| 4 | Proceduretype | Portaal ("Judicial en vía de apremio", "Agencia Tributaria", notarieel, administratief); TRLC-veilingen via RPC | Type bepaalt waarborg, termijnen en drempels; type onbekend → geen bod |
| 5 | Toepasselijk regime (LEC oud/nieuw; RGR; RGR-SS; TRLC-regels) | Edicto, decreto de convocatoria, datum inleiding procedure; LO 1/2025 DT 9.ª | Regime niet vast te stellen → **blokkade** (waarborg 5 % vs 20 %, 40 vs 20 dagen) |
| 6 | Objectidentiteit | Portaal "bienes": beschrijving, adres, CP, localidad; CRU; referencia catastral (LEC 668.2) | Geen CRU/referencia catastral én geen eenduidige beschrijving → geen bod |
| 7 | Kadastrale/registerinformatie | Certificación (verplicht in het edicto, 668.2), geactualiseerde nota simple (656.2), registerinformatie via portaal (667.2); Sede Catastro | Certificación ontbreekt of > 6 maanden zonder actualisatie → **blokkade** |
| 8 | Documenten en versies | Portaal-tabblad documenten: certificación, taxatierapport, antwoorden art. 657, verklaring 661.2; datum per document noteren | Tasación "0,00 €" of ontbrekend taxatierapport → **blokkade** (waargenomen bij SUB-JA-2026-257820) |
| 9 | Aangeboden recht | Titel/beschrijving in portaal ("100 % pleno dominio", "50 % nuda propiedad", "25 % pleno dominio"), certificación | Alles behalve 100 % volle eigendom → **blokkade** tenzij bewust en met advocaat (onverdeeld aandeel, blote eigendom, vruchtgebruik, vordering) |
| 10 | Relevante data | Portaal: inicio, conclusión (+ verlengingsregel), datum certificación, datum taxatie, datum decreto; betaaltermijn na sluiting | Sluiting in augustus/24-12–06-01 onmogelijk (LEC 649.1); termijnen in het liquiditeitsmodel zetten |
| 11 | Waarborgsom | Portaal "importe del depósito"; wet: LEC 669.1 (20 %/5 %), 647.1 (10 %), RGR 103 bis (5 %), RGR-SS 117.2 (25 %/30 %) | Bedrag in portaal ≠ wettelijk percentage → navragen bij autoridad gestora (LAJ mag afwijken, 669.1) |
| 12 | Biedvoorwaarden | Portaal: puja mínima, tramos; LEC 648.6 (geheim, laatste bod telt), RGR 104 (openbaar, 10 % minimum), RGR-SS 120 (2 %-stappen) | Onbekend hoogste bod ≠ geen biedingen (LEC 648.6.ª: geheim) |
| 13 | Betaaltermijnen | LEC 670.1/4 (20 d; oud 40 d); 670.6 (hypotheek-testimonio schorst); RGR 104 bis.3.b (15 d na kennisgeving); RGR-SS 120.8 (5 werkdagen) | Financiering niet binnen de termijn zeker → geen bod (verbeurte 653/104 bis/120.10) |
| 14 | Beschikbare biedinformatie | Portaal: cantidad reclamada, valor subasta, tasación; edicto: minoración de cargas | Cantidad reclamada ≠ koopprijs; valor subasta ≠ marktwaarde (sectie 19) |
| 15 | Procedurestatus | Portaal-status (Celebrándose, Pendiente de finalización, Finalizada, Cancelada, Suspendida); LEC 649.2; RPC voor concurso | Geschorst/geannuleerd/concurso gemeld → **blokkade**; > 15 dagen schorsing = nieuwe veiling |
| 16 | Bezitssituatie | Portaal "situación posesoria" en "vivienda habitual"; verklaring 661.2 in de publicatie; bezichtiging via 669.3 | "No consta" of bezetting zonder titel zonder verklaring 661.2 → **blokkade** voor een bod boven de ontruimingsrisico-korting; huurcontract → doorlopen (LAU) |
| 17 | Lasten en rangorde | Certificación; antwoorden 657 (actueel saldo, dagrente); portaal registerinformatie; TRLC 225/212 | Eerdere lasten onbekend of niet geactualiseerd → **blokkade**; eerdere lasten ≥ waarde → executie hoort geschorst (666.2) |
| 18 | Juridische onzekerheden | Verzet (695), tercería (696), oneerlijke bedingen, tanteo TGSS (121)/derden (RGR 104 bis.3.a), STC-vernietigingen | Lopend verzet/tercería of niet-verstreken tanteotermijn → geen definitief oordeel |
| 19 | Fiscale positie | ITP/AJD/btw/plusvalía-tabel sectie 6; niet-ingezeten vervreemder (TRLHL 106.2) | Onbekend of de vervreemder ondernemer of niet-ingezetene is → rekenen met de duurste variant |
| 20 | Kosten na toewijzing | Doorhaling (674; TRLC 225; RGR-SS 122.5), inschrijving, eventuele escritura (+5 % RGR 111), ontruimingskosten | In het model als kosten, niet in de prijs |

**Harde beslisgrenzen (samengevat):** (a) aangeboden recht ≠ 100 % volle eigendom; (b) certificación de cargas ontbreekt, is niet geactualiseerd of toont niet-gekwantificeerde eerdere lasten; (c) bezetting zonder titel, "no consta" of eigen woning zonder ontruimingsperspectief; (d) tasación ontbreekt of 0,00 €; (e) procedure geschorst, concurso gemeld of status niet "Celebrándose"; (f) regime (oud/nieuw LEC) onbekend; (g) betaaltermijn niet financierbaar. Bij één blokkade: geen biedvoorstel, alleen een onderzoeksvraag.

---

## 8. Waarborgsom als liquiditeitsbeslag — model per procedure

Model (bewijstype 5, aannames benoemd): `D = p × T` met p = wettelijk percentage en T = veilingwaarde/tipo zoals in het portaal; `L = D × looptijd`; `R = kans op verbeurte × D`. De waarborg is **geen kostenpost** boven op de prijs: bij winst wordt D "parte del precio de la venta" (LEC 652.1; RGR 103 bis.4); bij verlies komt D terug.

| Procedure | p (onroerend goed) | Storting | Terugbetaling verliezer | Looptijd met reserva de postura | Verbeurte | Rest van de prijs |
|---|---|---|---|---|---|---|
| LEC nieuw (procedures vanaf 03-04-2025) | 20 % van art. 666-waarde, min. 1.000 €; LAJ mag afwijken (669.1) | Via portaal/AEAT-passarelle, elk moment in de 20 dagen | Direct na sluiting (652.1) | Tot storting van het restant door de winnaar of tot de veiling vervalt (670.8) — weken tot maanden | Niet betalen binnen 20 dagen (670.4, 653.1); vertegenwoordiging niet binnen 3 dagen aangetoond (647.1.1.º) | Binnen 20 dagen na sluiting (670.1); schorsing bij hypotheek-testimonio (670.6) |
| LEC oud (procedures vóór 03-04-2025) | 5 % (669.1 oud) | idem | idem | idem | Niet betalen binnen 40 dagen | 40 dagen (670.1 oud) |
| Notarieel (LH 129) | LEC-voorwaarden (129.2.d) | Portaal | LEC | LEC | LEC | LEC |
| AEAT (RGR) | 5 % van de tipo (103 bis.1.b); een bod ≤ het hoogste is automatisch gereserveerd (103 bis.3) | Portaal | Niet-gereserveerd: na einde biedperiode (103 bis.4) | Tot de winnaar heeft betaald; Mesa binnen 15 dagen, betaling binnen 15 dagen na kennisgeving → ordegrootte 1–2 maanden | Niet betalen binnen 15 dagen → depósito naar de schuld + schadeaansprakelijkheid (104 bis.3.b) | 15 dagen na kennisgeving; escritura-optie: +5 % binnen 5 dagen (111.1) |
| TGSS (RGR-SS) | 25 % per gecertificeerde cheque bij de offerte; 30 % bij mondeling bod ter zitting | Cheque, bank blokkeert ≥ 10 dagen na openbaarmaking (118.2) | Ter zitting teruggegeven (120.8) | n.v.t. (geen reserva-figuur; wel provisional bij 120.5.d) | Niet betalen binnen 5 werkdagen (120.10) + schade | 5 werkdagen; daarna nog **30 dagen tanteo-risico** (121): prijs én depósito komen dan terug |
| Concurso (TRLC) | Bepaald door AC/rechter/portaal (niet wettelijk vast); bij bezwaarde goederen via BOE-portaal of ander portaal (423.2) | Per veiling | Per veiling | Per veiling | Per veiling | Per veiling — reglas especiales lezen |

Aanvullende modelregels (bewijstype 2 waar een artikel staat):
- Annulering door schorsing > 15 dagen → teruggave aan iedereen (LEC 649.2). Bevrijding door de schuldenaar vóór goedkeuring → veiling vervalt, teruggave (670.7–8; RGR 104.4; RGR-SS 117.2.h).
- Bieder namens een vennootschap: het depósito komt terug naar wie stortte (652.2); leg de rekeninghouder en de vertegenwoordiging vóór de eerste puja vast (portaal-FAQ; LEC 647.1.1.º).
- Meerdere veilingen tegelijk = meerdere D's tegelijk vast; het portaal geeft per veiling één depósito.
- Reserva de postura is een optie met waarde (kans op toewijzing als tweede) tegen een kost (langere vastlegging); alleen kiezen bij een bod dat wij ook echt willen betalen.
- Verbeurte is alleen een risico bij eigen gedrag; zet daarom de financieringszekerheid (banktoezegging of eigen middelen op de rekening) als voorwaarde vóór elke puja.

---

## 9. Controlelijst vóór ieder biedingsvoorstel (geen biedadvies)

1. Veiling-ID, autoridad gestora en anuncio BOE-B genoteerd; status is "Celebrándose"; sluitdatum en verlengingsregel bekend.
2. Proceduretype en regime vastgesteld (LEC oud/nieuw via datum inleiding; RGR; RGR-SS; TRLC-regels); de daarbij horende waarborg, betaaltermijn en drempels in het dossier.
3. Aangeboden recht = 100 % volle eigendom, bevestigd in certificación en beschrijving; anders stop.
4. Certificación de dominio y cargas gelezen, datum < 6 maanden of geactualiseerde nota simple aanwezig; alle eerdere lasten gekwantificeerd met actueel saldo en dagrente (art. 657-antwoorden) en opgeteld bij de prijs; latere lasten gemarkeerd als "worden doorgehaald" (674/LH 134/TRLC 225).
5. Veilingwaarde herleid: tasación − eerdere lasten (666) klopt met het portaal; tasación ≠ 0 en taxatierapport aanwezig en gedateerd; eigen marktwaarde apart bepaald (sectie 20 masterprompt).
6. Bezitssituatie: portaalveld gelezen; "vivienda habitual" Sí/No; verklaring 661.2 aanwezig of ontruimingsrisico en -termijn (675.2, 1 jaar) in het model; bezichtiging aangevraagd via 669.3.
7. Cantidad reclamada en biedgeschiedenis: niet verward met prijs; bij LEC nieuw zijn biedingen geheim.
8. Drempels doorgerekend: wat gebeurt er met ons bod bij < 70 % (verbeteringsrecht schuldenaar 10 dagen), bij eigen woning (70/60 %), bij lege veiling (671), bij AEAT < 50 % (discretie Mesa), bij TGSS (tanteo 30 dagen).
9. Waarborgsom en restbetaling gefinancierd op de sluitdatum + termijn; rekening bij een entidad colaboradora op naam van de bieder/gemachtigde; vertegenwoordiging vooraf geregeld (3-dagenregel).
10. Fiscale post gerekend met de duurste variant (ITP op max(valor de referencia, prijs) 9 %/11 % of btw + AJD; plusvalía-substitutie bij niet-ingezeten vervreemder; kosten doorhaling/inschrijving).
11. Geen lopende verzet-, tercería- of concurso-signalen (portaalstatus, RPC-raadpleging op naam van de ejecutado alleen als rechtspersoon, geen persoonsprofielen).
12. Dossier beoordeeld door een Spaanse advocaat (bewijstype 6) — zonder dat geen biedvoorstel aan Jan.

---

## 10. Bronnenregister-invoer (masterprompt sectie 7)

| Bron | URL | Type | Toegang | Status | Opmerkingen |
|---|---|---|---|---|---|
| Portal de Subastas AEBOE | https://subastas.boe.es | Officieel veilingportaal (gerechtelijk, notarieel, AEAT, administratief, ORGA) | Web, zoekformulier, detailpagina's; account voor bieden en alerts; `robots.txt` Disallow: / | ALLEEN HANDMATIG (+ e-mailalerts op opgeslagen zoekopdracht) | Geen API/RSS/open data gevonden; 278 Jávea-resultaten (alle statussen) op 14-09-2026 |
| AEAT — Subastas (Portal BOE) | https://sede.agenciatributaria.gob.es/Sede/subastas.html | Belastingdienst, invordering | Web; eigen zoeker "Buscador de bienes en subastas" en abonnement op meldingen (www2.agenciatributaria.gob.es) | TECHNISCH ONDERZOEK NODIG (abonnement testen) | Veilingen zelf via BOE-portaal; douane-veilingen apart |
| TGSS — RGR Seguridad Social | https://www.boe.es/buscar/act.php?id=BOE-A-2004-11836 | Wetgeving; veilingen via tablón sede electrónica (URL niet gevonden) | Onbekend | TECHNISCH ONDERZOEK NODIG | Presentiële procedure, 25 % cheque, tanteo 30 dagen |
| Registro Público Concursal + Portal de liquidaciones | https://www.publicidadconcursal.es/ ; /liquidaciones | Officieel register (CORPME voor Min. Justicia) | Web; filters op proceduretype en "modo venta" | ALLEEN HANDMATIG | Hergebruik van persoonsgegevens uitdrukkelijk verboden; IE bij CORPME |
| boe.es geconsolideerde wetgeving | https://www.boe.es/buscar/act.php?id=… | Primaire wetsbron | Web, versies per datum (`&tn=1&p=JJJJMMDD`) | GEVERIFIEERD EN ACTIEF (raadpleging) | Voor wijzigingsbewaking: noten per artikel |
| SUMA (Diputación Alicante) | niet onderzocht in deze stroom | Provinciale belastinginvordering | ONBEKEND | TECHNISCH ONDERZOEK NODIG | Buiten opdracht R09; wél kandidaat sectie 18 |

---

## 11. Open vragen

1. Passen de rechtbanken van Dénia de overgangsregel van LO 1/2025 (DT 9.ª) toe op de veiling zelf, of op de datum van de demanda ejecutiva? Eén waarneming (5 % bij expediente 2018) wijst op "datum procedure", geen bewijs.
2. Welke grondslag hanteert de ATV (Generalitat Valenciana) voor ITP bij een toewijzingsprijs onder de valor de referencia: art. 10.2 TRLITPAJD of art. 39 RITP? DGT-consultas/jurisprudentie niet gezocht (WebSearch niet beschikbaar).
3. Sinds wanneer geldt 9 %/11 % ITP in de CV (geconsolideerde tekst 02-07-2026) en zijn er overgangsregels?
4. Is AJD verschuldigd over het testimonio van het decreto de adjudicación of over de certificación van AEAT/TGSS? Alleen over een gekozen escritura?
5. Drempels art. 24 Ley 5/2019 (vencimiento anticipado) — brontekst niet uitgelezen.
6. Waar publiceert de TGSS haar veilingen precies (URL tablón sede electrónica) en gebruikt zij in de praktijk toch het BOE-portaal?
7. Wettelijke afecciones (IBI, VvE-bijdragen) op het geveilde goed: omvang en bron.
8. Wat betekent de prefix "SUB-RC" (Ayuntamiento de Xàbia) en welke regeling volgt de gemeente (RGR via SUMA? eigen ordenanza?).
9. Is een "guardar búsqueda"-alert per postcode 03730/03737/03738/03739 in de praktijk volledig (dekt het ook AEAT-veilingen met plaatsnaam "XABIA-JAVEA")?
10. Mag de AEAT-abonnementsdienst op nieuwe goederen door TREE/Rocksure worden gebruikt (voorwaarden niet gelezen).

## 12. Geblokkeerd of mislukt

- **WebSearch**: budget van de sessie was al uitgeput (200/200) vóór deze stroom; geen enkele zoekopdracht mogelijk. Alle bronnen via rechtstreekse URL's.
- **seg-social.es / sede.seg-social.gob.es**: startpagina's geladen, maar geen veilingpagina gevonden; een geraden informatiepagina gaf "No se ha encontrado contenido". TGSS-praktijk dus alleen uit het reglement.
- **boe.es/datosabiertos**: lege respons op 14-09-2026; BOE-API voor geconsolideerde wetgeving gaf HTTP 400 op het geteste pad (URL-vorm onbekend).
- **subastas.boe.es/acerca.php**: 404. Geen aviso legal/gebruiksvoorwaarden van het portaal gevonden behalve `ayuda.php` en `robots.txt`.
- **LCCI art. 24**: extractie uit de geconsolideerde HTML mislukt (koptekst niet gevonden); niet opnieuw geprobeerd.
- **Eerste raadpleging van boe.es-ID's**: drie verkeerde ID's (RD 1415/2004, RD 828/1995, Ley 13/1997) door een fout in de dagoverzicht-parsing; gecorrigeerd naar BOE-A-2004-11836, BOE-A-1995-15071 en BOE-A-1998-8202 (titels gecontroleerd).

---

## Bronnenlijst (URL · controledatum · bewijstype)

| # | Bron | URL | Datum | Type |
|---|---|---|---|---|
| B1 | Ley 1/2000 (LEC), geconsolideerd, "Última actualización publicada el 28/02/2025" | https://www.boe.es/buscar/act.php?id=BOE-A-2000-323 | 14-09-2026 | 2 |
| B2 | LEC, versie 20-12-2023 (oud regime) | https://www.boe.es/buscar/act.php?id=BOE-A-2000-323&tn=1&p=20231220 | 14-09-2026 | 2 |
| B3 | Ley Orgánica 1/2025 (eficiencia Servicio Público de Justicia), DT 9.ª | https://www.boe.es/buscar/act.php?id=BOE-A-2025-76 | 14-09-2026 | 2 |
| B4 | RD 939/2005 Reglamento General de Recaudación, cons. 31-01-2024 | https://www.boe.es/buscar/act.php?id=BOE-A-2005-14803 | 14-09-2026 | 2 |
| B5 | Ley 58/2003 General Tributaria art. 172, cons. 21-12-2024 | https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186 | 14-09-2026 | 2 |
| B6 | RD 1415/2004 RGR Seguridad Social, cons. 30-07-2026 | https://www.boe.es/buscar/act.php?id=BOE-A-2004-11836 | 14-09-2026 | 2 |
| B7 | RDL 1/2020 Texto Refundido Ley Concursal, cons. 03-01-2025 | https://www.boe.es/buscar/act.php?id=BOE-A-2020-4859 | 14-09-2026 | 2 |
| B8 | Ley Hipotecaria (Decreto 08-02-1946) art. 129, 131–134, cons. 03-01-2025 | https://www.boe.es/buscar/act.php?id=BOE-A-1946-2453 | 14-09-2026 | 2 |
| B9 | RDL 1/1993 TR Ley ITP y AJD (art. 7, 8, 10, 29–31) | https://www.boe.es/buscar/act.php?id=BOE-A-1993-25359 | 14-09-2026 | 2 |
| B10 | RD 828/1995 Reglamento ITP art. 37–39, cons. 09-11-2018 | https://www.boe.es/buscar/act.php?id=BOE-A-1995-15071 | 14-09-2026 | 2 |
| B11 | Ley 13/1997 Comunitat Valenciana art. 13–14, cons. 02-07-2026 | https://www.boe.es/buscar/act.php?id=BOE-A-1998-8202 | 14-09-2026 | 2 |
| B12 | RDL 2/2004 TR Ley Haciendas Locales art. 104, 106, 107, 109, cons. 03-06-2026 | https://www.boe.es/buscar/act.php?id=BOE-A-2004-4214 | 14-09-2026 | 2 |
| B13 | Ley 5/2019 LCCI (verwijzing vanuit LEC 693.2; art. 24 niet uitgelezen) | https://www.boe.es/buscar/act.php?id=BOE-A-2019-3814 | 14-09-2026 | 2/7 |
| B14 | RDL 6/2023 (wijzigingen LEC 634, 635, 639, 682, 695; art. 6 identificatie) | https://www.boe.es/buscar/act.php?id=BOE-A-2023-25758 | 14-09-2026 | 2 |
| B15 | Portal de Subastas — hulppagina | https://subastas.boe.es/ayuda.php | 14-09-2026 | 2 |
| B16 | Portal de Subastas — robots.txt | https://subastas.boe.es/robots.txt | 14-09-2026 | 3 |
| B17 | Portal de Subastas — zoekformulier en resultaten (Alicante celebrándose; localidad JAVEA) | https://subastas.boe.es/subastas_ava.php | 14-09-2026 | 3 |
| B18 | Portal de Subastas — detail SUB-JA-2026-257820 (TI Dénia, Jávea) | https://subastas.boe.es/detalleSubasta.php?idSub=SUB-JA-2026-257820 | 14-09-2026 | 3 |
| B19 | Portal de Subastas — detail SUB-AT-2026-26R2886001392 (AEAT, Dénia, 25 %) | https://subastas.boe.es/detalleSubasta.php?idSub=SUB-AT-2026-26R2886001392 | 14-09-2026 | 3 |
| B20 | AEAT Sede — Subastas (Portal de Subastas del BOE) | https://sede.agenciatributaria.gob.es/Sede/subastas.html | 14-09-2026 | 2 |
| B21 | AEAT Sede — Licitadores: quién y cómo participar | https://sede.agenciatributaria.gob.es/Sede/deudas-apremios-embargos-subastas/subastas/licitadores.html | 14-09-2026 | 2 |
| B22 | AEAT Sede — Otras subastas (douane, buiten portaal) | https://sede.agenciatributaria.gob.es/Sede/deudas-apremios-embargos-subastas/otras-subastas.html | 14-09-2026 | 2 |
| B23 | Registro Público Concursal — start, portal de liquidaciones, aviso legal | https://www.publicidadconcursal.es/ ; https://www.publicidadconcursal.es/liquidaciones ; https://www.publicidadconcursal.es/aviso-legal | 14-09-2026 | 2 |
| B24 | Seguridad Social — startpagina's (geen veilingpagina gevonden) | https://www.seg-social.es/wps/portal/wss/internet/Inicio ; https://sede.seg-social.gob.es/wps/portal/sede/sede/Inicio | 14-09-2026 | 7 |

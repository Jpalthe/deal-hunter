# R08 — Veilingen: officiële portalen, zoekfuncties, meldingen en automatiseerbaarheid

> **NA TEGENSPRAAK (15-09-2026).** Dit rapport is door een tweede agent gecontroleerd; zie `R08-veilingen-portalen-toegang.verificatie.md`. Betrouwbaarheid volgens die controle: middel: het portaaloverzicht, de toegangsregels en de live steekproef kloppen en zijn reproduceerbaar, maar vier dragende claims zijn (deels) onjuist (JSON-API, aviso legal, AEAT-adjudicación directa, FAQ-pdf) en het ontwerp van de veilingmonitor rust op een BOE-plaatsfilter dat niet werkt omdat aankondigingen geen plaats van het goed bevatten.
> Weerlegd en in de eindstukken gecorrigeerd: R08-05; R08-06; R08-08; R08-12. Gebruik voor die punten de gecorrigeerde tekst in het verificatiebestand, niet de tekst hieronder.


**Project:** TREE Deal Hunter, fase A · **Stroom:** R08 · **Controledatum:** 14-09-2026 (live steekproef 23:01–23:10 CEST)
**Masterprompt-secties:** 18 (bankvastgoed, veilingen, faillissementen), 10 (actualiteit en wijzigingsdetectie), 5 en 7 (bewijstypen, bronnenregister).
**Bewijstypen:** 1 door aanbieder vermeld · 2 in officiële bron aangetroffen · 3 door ons rechtstreeks vastgesteld · 4 AI-inferentie · 5 berekening op benoemde aannames · 6 door bevoegde professional bevestigd · 7 onbekend of tegenstrijdig.

## Samenvatting (10 regels)

1. Er is één centraal, officieel veilingportaal: het **Portal de Subastas del BOE** (subastas.boe.es). Daar draaien de gerechtelijke, notariële, AEAT-, "otras administraciones tributarias" (o.a. SUMA) en algemene administratieve (patrimoniale) veilingen. **Uitzondering: de TGSS (Seguridad Social)** houdt haar executieveilingen op een eigen portaal (w6.seg-social.es/subastas) met gesloten enveloppen. [2/3]
2. Live steekproef 14-09-2026, provincie Alicante, onroerend goed: **43 veilingen "celebrándose"** (40 gerechtelijk, 3 AEAT) en **41 "próxima apertura"** (21 gerechtelijk, 3 AEAT, 17 SUMA). **In Xàbia/Jávea: 0.** Dichtstbij: één AEAT-lot in Dénia (25% onverdeeld aandeel van een appartement). Geen enkele lopende veiling van de rechtbank van Dénia. [3]
3. Het BOE-portaal heeft **geen RSS, geen API en geen downloadlijst**; `robots.txt` zegt `Disallow: /` en de pagina's dragen `X-Robots-Tag: noindex, nofollow`. Wél: gratis **e-mailmeldingen** voor geregistreerde gebruikers (maximaal 50 opgeslagen zoekopdrachten), maar registratie kan alleen als natuurlijk persoon. [3/2]
4. De **officiële, toegestane machinale ingang** is de BOE zelf: de open-data-API van het dagelijkse sumario (`/datosabiertos/api/boe/sumario/AAAAMMDD`, XML) en de RSS-kanalen van Sección IV (Administración de Justicia — elke gerechtelijke veiling wordt daar aangekondigd, titel = plaats van de rechtbank) en Sección V-B (AEAT, SUMA, TGSS-patrimonium). Hergebruik is gratis onder Ley 37/2007 met bronvermelding. Getest en werkend. [3/2]
5. De AEAT publiceert bovendien een **downloadbare lijst** van te veilen goederen (`data2/bienes.js`, dagelijks ververst, kop: "Licencia Creative Commons Atribución 4.0") met kadasterreferentie, CRU, coördinaten, waardering, lasten, einddatum en foto's: 230 onroerende goederen landelijk, 3 in Alicante, 0 in Xàbia. [3]
6. **Juridische regels zijn per kanaal verschillend** en de LEC is per 03-04-2025 (LO 1/2025) gewijzigd: gerechtelijk 20% waarborg voor onroerend goed (min. 1.000 €; LAJ mag afwijken), betaling binnen 20 dagen na sluiting; AEAT/SUMA 5% waarborg, betaling binnen 15 dagen; TGSS 25% (cheque) en betaling binnen 5 werkdagen; notarieel 5%. De FAQ-pdf van het Ministerio de Justicia (5%, 40 dagen) is **verouderd** en mag niet als rekenregel worden gebruikt. [2/7]
7. **Faillissementen:** het Registro Público Concursal is alleen handmatig raadpleegbaar (NIF of dag + CAPTCHA, gebruik beperkt tot wettelijke doelen); het Portal de liquidaciones toont vooral productie-eenheden. Liquidatie van vastgoed >5% van de boedel loopt verplicht via elektronische veiling op het BOE-portaal **of** een gespecialiseerd portaal (art. 423 TRLC). Bevestigd als "entidad especializada": het portaal van de **Consejo General de Procuradores** (subastasprocuradores.com, 4% commissie op onroerend goed) en **eActivos** (Activos Concursales S.L.; verbiedt expliciet machinale toegang). [2/3]
8. **Gemeente Xàbia:** geen lopende verkoop van gemeentelijk vastgoed gevonden op het tablón (sede electrónica, esPublico Gestiona) of via de gemeentesite; het perfil del contratante staat op de Plataforma de Contratación del Sector Público, waarvan dagelijkse Atom-feeds als open data bestaan. Verkoop van gemeentelijk patrimonium moet via openbare veiling met voorafgaande taxatie (RBEL art. 112 en 118). [3/2]
9. **Rechtbank Dénia** (partido judicial waar Xàbia onder valt): Sección Civil del Tribunal de Instancia de Dénia, zes plazas, Pl. Jaume I 23. Haar veilingedicten verschijnen als BOE Sección IV-aankondiging met titel "DENIA" plus het edicto op het portaal (voorbeeld 2022: BOE-B-2022-17675 → SUB-JA-2022-195732). [2/3]
10. **Ontwerp veilingmonitor:** dagelijks BOE-sumario/RSS + AEAT-lijst pollen (toegestaan), geregistreerde e-mailmeldingen van het portaal inlezen, per kandidaat een dossier met deadlines (opening +24 u, 20 kalenderdagen, verlenging ≤24 u, waarborg, betaaltermijn) en statusovergangen. **Nooit geautomatiseerd:** registreren, waarborg storten, bieden, reserva de postura, betalen, ondertekenen. Geautomatiseerd ophalen van portaal-detailpagina's pas na expliciete toestemming van de AEBOE (robots verbiedt).

---

## 1. Portal de Subastas del BOE (subastas.boe.es)

### 1.1 Officiële URL's en wat erop staat

| Onderdeel | URL | Vastgesteld | Bewijs |
|---|---|---|---|
| Startpagina (provinciekaart, categorieën Inmuebles / Bienes muebles / Vehículos) | https://subastas.boe.es/ | 14-09-2026 | 3 |
| Zoekformulier (búsqueda avanzada) | https://subastas.boe.es/subastas_ava.php | 14-09-2026 | 3 |
| Helppagina / FAQ | https://subastas.boe.es/ayuda.php | 14-09-2026 | 3 |
| Inloggen/registreren | https://subastas.boe.es/acceso.php | 14-09-2026 | 3 |
| Detailpagina per veiling | `detalleSubasta.php?idSub=SUB-…&ver=1..5` en korte link `ds.php?id=SUB-…` | 14-09-2026 | 3 |
| Beleidspagina | https://subastas.boe.es/textoPolitica.php | 14-09-2026 | 3 |

**Welke procedures er op het portaal draaien** (helppagina, letterlijk): "En el Portal de Subastas del BOE se realizan las subastas judiciales, notariales, y desde el 1 de septiembre de 2018, las subastas tributarias. También se realizan otras subastas administrativas generales." En: "Las subastas administrativas generales son aquellas realizadas para la enajenación de los bienes patrimoniales de cualquier Administración Pública u organismo vinculado o dependiente de la misma". [2]

Het zoekformulier bevestigt de indeling met veld `SUBASTA.ORIGEN` (`dato[0]`): **Todos / J Judicial / N Notarial / A AEAT / R Otras administraciones tributarias / G Subastas administrativas generales**. [3]

Bevestigd per type op 14-09-2026 (live, provincie Alicante):
- **Judicial (SUB-JA-…):** autoriteit = Sección Civil van een Tribunal de Instancia (Torrevieja, Orihuela, Elx, Novelda, Ibi, Alcoy, Benidorm, Alicante, Sant Vicent del Raspeig). [3]
- **AEAT (SUB-AT-…):** autoriteit "U.R. SUBASTAS MADRID/VALENCIA/ANDALUCÍA (AEAT)"; detailpagina toont "Tipo de subasta: AGENCIA TRIBUTARIA". [3]
- **Otras administraciones tributarias (SUB-RC-…):** autoriteit "Suma Gestión Tributaria. Diputación de Alicante"; detailpagina toont "Tipo de subasta: RECAUDACIÓN TRIBUTARIA" en "Cantidad reclamada". [3]
- **Notarial** en **administrativas generales**: aanwezig als filter; in de Alicante-steekproef (alleen onroerend goed, lopend/aanstaand) kwamen geen notariële of patrimoniale veilingen voor. [3]
- **TGSS staat NIET op dit portaal** (zie §3). [2/3]

Wettelijke basis van de exclusiviteit: LEC art. 648.1ª ("La subasta tendrá lugar en el Portal dependiente de la Agencia Estatal Boletín Oficial del Estado"), Ley del Notariado art. 73.1 ("La subasta será electrónica y se llevará a cabo en el Portal de Subastas de la Agencia Estatal Boletín Oficial del Estado"), RGR art. 104.1 ("La presentación de ofertas se llevará a cabo, en todo caso, de forma electrónica en el Portal de Subastas de la Agencia Estatal Boletín Oficial del Estado"). [2]

### 1.2 Zoekfilters (exact zoals in het formulier waargenomen)

Formulier: `<form method="post" action="subastas_ava.php">`. Velden zijn paren `campo[n]` (vaste naam) en `dato[n]` (waarde). [3]

| # | Veld (`campo[n]`) | Waarden / vorm |
|---|---|---|
| 0 | SUBASTA.ORIGEN | leeg = alle; J, N, A, R, G |
| 1 | SUBASTA.AUTORIDAD | vrije tekst (autoridad gestora) |
| 2 | SUBASTA.ESTADO.CODIGO | leeg = alle; **PU** Prox. apertura; **EJ** Celebrándose; **SU** Suspendida; **CA** Cancelada; **PC** Concluida en Portal de Subastas; **FS** Finalizada por Autoridad Gestora |
| 3 | BIEN.TIPO | I Inmuebles; V Vehículos; M Otros bienes muebles |
| 4 | (subtype) | bij I: codes 501–507 en 599 (Vivienda, Local comercial, Garaje, Trastero, Nave industrial, Solar, Finca rústica, Otros); bij V: 9101–9103; bij M: 1–99 |
| 5 | BIEN.DIRECCION | vrije tekst |
| 6 | BIEN.CODPOSTAL | 5 cijfers |
| 7 | BIEN.LOCALIDAD | vrije tekst (geen keuzelijst — spelling Xàbia/Jávea/Javea niet genormaliseerd) |
| 8 | BIEN.COD_PROVINCIA | keuzelijst; **Alicante/Alacant = "03"** |
| 9 | SUBASTA.POSTURA_MINIMA_MINIMA_LOTES | keuzelijst bedragen (50.000 – 3.000.000 €) |
| 10–14 | SUBASTA.NUM_CUENTA_EXPEDIENTE_1..5 | rekeningnummer expediente (gerechtelijk) |
| 15 | SUBASTA.ID_SUBASTA_BUSCAR | ID subasta |
| 16 | SUBASTA.ACREEDORES | schuldeiser |
| 17 | SUBASTA.FECHA_FIN | `dato[17][0]` van, `dato[17][1]` tot (dd/mm/yyyy) |
| 18 | SUBASTA.FECHA_INICIO | `dato[18][0]`, `dato[18][1]` |
| — | page_hits | 50 / 100 / 200 / 500 |
| — | sort_field[0], sort_order[0] | o.a. SUBASTA.FECHA_FIN, asc/desc |
| — | accion | Buscar |

Let op (les uit de steekproef): de datumvelden zijn arrays; een scalair `dato[17]=` geeft "ERROR: Se ha producido un error en la búsqueda". [3]

Er is géén filter op gemeente-code of kadastrale referentie; wel op postcode. Voor Xàbia zijn de postcodes 03730, 03737 en 03738 relevant [te verifiëren: volledigheid van de postcodelijst]. [4]

### 1.3 Wat een resultaat en een detailpagina tonen (openbaar, zonder inloggen)

**Resultatenlijst:** "Resultados 1 a N de N"; per veiling: identificatie (bijv. `SUB-JA-2026-263722 (2 lotes)`), autoridad gestora, expediente, "Estado: Celebrándose - [Conclusión prevista: dd/mm/yyyy a las hh:mm:ss]" of "Estado: Próxima apertura", korte omschrijving van het goed/lot, link naar de detailpagina. [3]

**Detailpagina, tabbladen:** `ver=1` Información general, `ver=2` Autoridad gestora, `ver=3` Bienes, `ver=5` Pujas. [3]

Velden onder *Información general* (waargenomen op twee lots): Identificador · Tipo de subasta · Fecha de inicio · Fecha de conclusión · Lotes · **Anuncio BOE** (BOE-B-nummer) · Valor subasta · Tasación · Puja mínima · Tramos entre pujas · **Importe del depósito** · (bij belastingveilingen) Cantidad reclamada. Daaronder: "Para consultar la información complementaria debe Iniciar sesión en el Portal de Subastas." [3]

Velden onder *Bienes*: beschrijving, derecho subastado (bijv. "25% PLENO DOMINIO"), IDUFIR/CRU, referencia catastral, dirección, código postal, localidad, provincia, **situación posesoria**, **visitable**, cargas (€), inscripción registral, título jurídico, información adicional (bijv. "EXISTEN CARGAS QUE AFECTAN AL BIEN: VER IMAGENES-ANEXOS"). [3]

### 1.4 Documenten per veiling

| Document | Wettelijke grondslag | Waar op het portaal | Bewijs |
|---|---|---|---|
| **Edicto** met algemene en bijzondere voorwaarden | LEC art. 646.2 ("se incorporará … el edicto … así como todos los documentos que contengan datos y circunstancias que sean relevantes"); art. 668.2 voor onroerend goed | tabblad Bienes / documentatie; deels alleen na inloggen | 2/3 |
| **Certificación de dominio y cargas** (bij aanvang executie) | LEC art. 668.2 ("necesariamente, la certificación de dominio y cargas") | idem | 2 |
| **Avalúo / valoración / informe de tasación extrajudicial** die als tipo dient | LEC art. 646.2 en 668.2; RGR art. 101 (tipo); helppagina: "documentación adicional aportada por el gestor de la subasta (edicto, documento de t[asación]…)" | Tasación-veld + bijlage | 2/3 |
| **Actuele registerinformatie** (permanent bijgewerkt tot einde veiling, via Colegio de Registradores) | LEC art. 667.2; Ley del Notariado art. 74.1 ("La certificación registral … podrá consultarse a través del Portal de Subastas") | alleen ingelogd: "información registral en caso de que esté disponible" | 2 |
| **Minoración de cargas preferentes**, **situación posesoria**, mogelijkheid tot bezichtiging | LEC art. 668.2 en 669.3 | velden Cargas / Situación posesoria / Visitable | 2/3 |
| **Pliego de condiciones** | bij notariële vrijwillige veiling (Ley del Notariado art. 77) en patrimoniale veilingen | per autoriteit | 2 |
| **Cargas que quedan subsistentes** | RGR art. 101.4.e; RGRSS art. 117.2.b; LEC art. 668.2 (subrogatie in eerdere lasten) | edicto/anuncio | 2 |

Belangrijk voor het dossier (masterprompt §19): het edicto vermeldt verplicht dat "las cargas, gravámenes y asientos anteriores al crédito del actor continuarán subsistentes y que, por el solo hecho de participar en la subasta, el licitador los admite y acepta quedar subrogado" (LEC art. 668.2). [2]

### 1.5 Meldingen, RSS, API, downloads

| Mogelijkheid | Bevinding | Bewijs |
|---|---|---|
| E-mailmeldingen | Ja, na registratie: "El Portal de Subastas permite a los usuarios registrados suscribirse a alertas por correo electrónico para recibir un aviso cuando haya alguna subasta que cumpla sus criterios de búsqueda." en "Suscribirse a alertas de cambios de estado de las subastas que se ajusten a sus criterios de búsqueda, hasta un máximo de 50 suscripciones." Voorbeeld in de help: localidad of postcode + estado "Celebrándose" + zoekopdracht opslaan. | 2 |
| Wie kan registreren | "En el Portal de Subastas únicamente pueden registrarse personas físicas." Identificatie: gekwalificeerd certificaat, Cl@ve of gebruiker (e-mail/telefoon) + wachtwoord. Registratie is een handeling van Jan zelf (⏸️ ACTIE VOOR JAN). | 2 |
| RSS | Niet aanwezig (0 treffers op "RSS" in help en beleidspagina; niet in de BOE-RSS-lijst). | 3 |
| API / open data | Niet aanwezig; de BOE-open-data-pagina documenteert alleen legislación consolidada, sumario BOE, sumario BORME en hulptabellen. Het portaal, de edictos judiciales en de anuncios zijn er niet als API. | 2/3 |
| Downloadbare lijst | Niet aanwezig. | 3 |
| Zonder inloggen | Zoeken en openbare details bekijken: "Los usuarios que no hayan realizado un proceso de registro previo podrán realizar búsquedas de subastas en curso por distintos criterios y consultar los detalles públicos de cada subasta". | 2 |

### 1.6 Gebruiksvoorwaarden en robots voor geautomatiseerde raadpleging

- `https://subastas.boe.es/robots.txt`: `User-agent: * / Disallow: /`. HTTP-headers: `X-Robots-Tag: noindex, nofollow`; Content-Security-Policy staat reCAPTCHA-domeinen toe (captcha op sommige stappen mogelijk; bij onze zoekopdrachten niet getoond). [3]
- `textoPolitica.php` bevat geen bepaling over geautomatiseerd gebruik of hergebruik (alleen browsercompatibiliteit en de AEMET-kaart). [3]
- Het algemene **aviso legal van de AEBOE** (boe.es/informacion/aviso_legal) staat hergebruik van de "conjuntos de datos" toe onder Ley 37/2007 en RD 1495/2011, gratis en niet-exclusief, met verplichte bronvermelding ("Fuente de los datos: Agencia Estatal Boletín Oficial del Estado"), verbod op "desnaturalizar el sentido de la información", en de AEBOE "puede denegar o suspender el acceso a los conjuntos de datos sin previo aviso" bij overtreding. Of het veilingportaal onder die "conjuntos de datos" valt, staat er niet: **ONBEKEND / te verifiëren bij de AEBOE.** [2/7]
- Conclusie: het portaal handmatig gebruiken en de e-mailmeldingen benutten is toegestaan; systematisch crawlen is door robots.txt uitgesloten. Voor gerichte automatische raadpleging (één detailpagina per nieuw gevonden SUB-id) is toestemming van de AEBOE de veilige route (status **CONTRACT OF TOESTEMMING NODIG**). [4]

### 1.7 Live steekproef 14-09-2026 (provincie Alicante en Xàbia/Jávea)

Uitgevoerd via twee POST-verzoeken (na twee mislukte pogingen door het datumveld-formaat) en drie detailpagina's; alle verzoeken 23:01–23:10 CEST; klok van het portaal: "Lunes, 14 de septiembre de 2026 23:01:21 CET". [3]

| Filter | Resultaat | Waarvan | Bewijs |
|---|---|---|---|
| Provincie 03 Alicante · Inmuebles · **Celebrándose** | **43** | 40 judicial (SUB-JA), 3 AEAT (SUB-AT); sluitingsdata 14-09 t/m 01-10-2026 | 3 |
| Provincie 03 Alicante · Inmuebles · **Próxima apertura** | **41** | 21 judicial, 3 AEAT, **17 SUMA** (SUB-RC-2026-0026I2025…) | 3 |
| Gemeente **Xàbia/Jávea** (tekst "Xàbia", "Jávea", "Javea", "Xabia", postcodes 0373x) in beide lijsten | **0** | — | 3 |
| Dichtstbijzijnde: Dénia | 1 (AEAT, SUB-AT-2026-26R2886001392): 25% pleno dominio van een appartement, tasación 40.945,66 €, puja mínima 4.094,57 €, depósito 2.047,28 €, conclusión 21-09-2026 18:00; "Se desconoce el estado de ocupación"; "HAY DERECHO DE RETRACTO" | | 3 |
| Veilingen van de rechtbank van Dénia (autoridad gestora bevat "Dénia") | **0** in beide lijsten | | 3 |

Verdeling autoriteiten "celebrándose" (43): TI Torrevieja 22, Orihuela 3, Ibi 3, Elx 3, Novelda 2, Alcoy 2, Alicante 2, Benidorm 1, Sant Vicent 1, Collado Villalba 1 (goed in Alicante), AEAT 3. [3]

SUMA-voorbeeldlot (SUB-RC-2026-0026I20250184, "Próxima apertura", Anuncio BOE-B-2026-29836): Tasación 93.007,47 €, Valor subasta 69.162,35 €, Puja mínima 34.581,18 € (= 50%), Depósito 3.458,12 € (= 5%), Cantidad reclamada 11.908,64 €. Illustreert masterprompt §19: de gevorderde schuld (11.908 €) is niet de koopprijs, en de veilingwaarde is niet de marktwaarde. [3/5]

### 1.8 Regels per proceduretype (huidige geconsolideerde teksten, opgehaald via de BOE-API op 14-09-2026)

| Onderwerp | Judicial (LEC, versie geldig sinds 03-04-2025, LO 1/2025) | Notarial (Ley del Notariado, art. 72–77) | AEAT / SUMA (RGR RD 939/2005) | TGSS (RGRSS RD 1415/2004) |
|---|---|---|---|---|
| Aankondiging | BOE-anuncio met alleen datum, oficina judicial, nummer en portaaladres (art. 646.1); opening ≥24 u na BOE-publicatie (art. 648.2ª) | BOE-anuncio (art. 74.1); opening ≥24 u (art. 75.1.2ª) | ≥15 dagen na notificaties; BOE-anuncio; opening ≥24 u (art. 101.2–3) | Tablón de anuncios op de sede electrónica van de Seguridad Social (art. 117.1); indieningstermijn ≥1 maand (art. 116.1) |
| Duur biedingen | 20 kalenderdagen, onverlengbaar; mag niet eindigen in weekend, nationale feestdag, 24-12 t/m 06-01 of augustus (art. 649.1) | ≥20 kalenderdagen (art. 75.1.3ª) | 20 kalenderdagen (art. 104.2) | Gesloten enveloppen tot de werkdag vóór de zitting (art. 118.1); mondelinge biedingen ter zitting |
| Verlenging | helppagina: autoriteit bepaalt of laatste-uur-bod verlengt "hasta un máximo de 24 horas" | idem (supletorio LEC) | idem; SUMA: "no se cerrará hasta que haya transcurrido una hora desde la realización de la última puja" | n.v.t. |
| Waarborg | **Onroerend goed 20%** van de waarde (min. 1.000 €), LAJ mag verhogen/verlagen (art. 669.1); roerend 10% (art. 647.1.3º) | **5%** (art. 75.1.4ª); bij vrijwillige veiling aanpasbaar in pliego (art. 77) | **5%** van het tipo voor onroerend goed, 10% roerend (AEAT-sede; SUMA "mínimo del 5%") | **25%** van het tipo, gecertificeerde cheque (art. 117.2.e, 118.2); 30% voor wie zonder envelop ter zitting meedoet (art. 120.2) |
| Minimumbod | geen vast minimum; gevolgen bij <70% (art. 670) | per pliego | 10% van het tipo, tenzij lasten ≥25% van de waardering (art. 104.2) | mondelinge biedingen ≥75% van het tipo (art. 117.2.f, 120.3) |
| Toewijzing | ≥70%: remate goedgekeurd de dag na sluiting (art. 670.1); <70%: ejecutado heeft 10 dagen om iemand met ≥60% aan te dragen (art. 670.3); zonder bieder: adjudicatie aan aangewezen persoon ≥50% of ≥40% mits volledige voldoening (art. 671) | per pliego / supletorio LEC | ≥50% van het tipo: automatisch; <50%: Mesa beslist (AEAT-sede); adjudicación directa daarna (art. 107; na twee licitaciones geen minimum) | hoogste bod; TGSS heeft **derecho de tanteo** binnen 30 dagen (art. 121) |
| Betaaltermijn rest | **20 dagen na sluiting** (art. 670.1) | per pliego / supletorio | **15 dagen na notificatie** van de adjudicatie (art. 101.4.f; SUMA-pagina) | 5 werkdagen (TGSS-informatiepagina; [te verifiëren in art. 120 RGRSS, tekst deels bekeken]) |
| Registratie/identificatie | verplicht registreren met veilige identificatie (art. 648.4ª) | idem | idem + AEAT-betaalpasarela | fysiek/per envelop bij Dirección Provincial (art. 118.3) |
| Bijzonderheden | lasten vóór de vordering blijven bestaan (art. 668.2); bezichtiging via rechtbank (art. 669.3); concurso van schuldenaar → schorsing (art. 649.1, 691.5) | RPC-raadpleging verplicht (art. 73.3) | schorsing bij betaling schuld (LGT art. 169.1) | — |

**Tegenstrijdige bron:** de FAQ-pdf van het Ministerio de Justicia (Oficina de Recuperación y Gestión de Activos) noemt "5% del valor de tasación" en "40 días" voor betaling. Dat is de LEC-tekst van vóór 03-04-2025. Bewijstype 7: niet gebruiken; de geconsolideerde LEC (art. 647, 669, 670) is leidend. [7/2]

### 1.9 BOE-kanalen als officiële, toegestane machinale ingang

| Kanaal | Getest 14-09-2026 | Resultaat | Bewijs |
|---|---|---|---|
| **Open-data-API sumario** `https://www.boe.es/datosabiertos/api/boe/sumario/AAAAMMDD` met header `Accept: application/xml` | 20260914, 20260911, 20220604 | HTTP 200; structuur `seccion → departamento → item {identificador, titulo, url_pdf, url_html, url_xml}`; **Sección IV "Administración de Justicia"** aanwezig op 14-09-2026 (45 items; departamentos o.a. "TRIBUNALES DE INSTANCIA. SECCIÓN CIVIL") en 04-06-2022; afwezig op 11-09-2026 (geen publicaties die dag). Sección V-B aanwezig. `Accept: application/json` gaf HTTP 400 "No soportado ningún mime type de la cabecera Accept" | 3 |
| **RSS Sección IV** `https://www.boe.es/rss/boe.php?s=4` | vandaag | 46 items; titels = plaatsnaam van de rechtbank (o.a. NOVELDA, SANT VICENT DEL RASPEIG, ORIHUELA, TORREVIEJA ×2) | 3 |
| **RSS Sección V-B** `https://www.boe.es/rss/boe.php?s=5B` | vandaag | 44 items, waaronder subasta-aankondigingen (Delegación de Economía y Hacienda de Cuenca; TGSS Sevilla patrimonium) | 3 |
| Verband anuncio ↔ portaal | BOE-B-2026-29751 (titel "TORREVIEJA") | "Anuncio de subasta judicial en vía de apremio", Sección Civil TI Torrevieja plaza 3, met `https://subastas.boe.es/ds.php?id=SUB-JA-2026-264695`; het AEAT-Dénia-lot verwijst naar BOE-B-2026-28134 (V-B); SUMA-lots naar BOE-B-2026-29836 (V-B) | 3 |
| Legislación consolidada `…/api/legislacion-consolidada/id/{BOE-id}/texto/indice` en `/texto/bloque/{id}` | LEC, RGR, RGRSS, Ley del Notariado, TRLC | HTTP 200 met versiehistorie en `fecha_vigencia` | 3 |
| BOE `robots.txt` | — | Disallow o.a. `/boe_j/`, `/edictos_judiciales/`, `/diario_boe/xml.php?`, `/buscar/edictos_judiciales.php?` → gebruik API/RSS, niet de HTML-zoekpagina's | 3 |
| Mi BOE-alertas | boe.es/alertas | Alerttypen LEG, PER, CPV (contratación), CAN (temáticas); volgens de Mi BOE-FAQ kunnen zoekopdrachten in "Anuncios de Administración de Justicia en el BOE" worden opgeslagen als dagelijkse e-mailalert [te verifiëren na registratie] | 2 |
| Ratelimits API | — | ONBEKEND (FAQ-pagina weigert: "El acceso a la dirección URL solicitada no está permitido"; documentatie-pdf niet tekstueel leesbaar) | 7 |

Praktische betekenis: **elke nieuwe gerechtelijke veiling van de rechtbank van Dénia levert een Sección IV-item met titel "DENIA"** op de dag van publicatie; AEAT- en SUMA-veilingen leveren een V-B-item. Dat is een gebeurtenisgestuurde trigger zonder het portaal te crawlen. [4, gebaseerd op 3]

---

## 2. AEAT (Agencia Estatal de Administración Tributaria)

| Onderdeel | Bevinding | URL | Bewijs |
|---|---|---|---|
| Publicatiekanaal | Via het BOE-portaal: de AEAT "publica regularmente a través del portal del BOE" (sede-pagina "Subastas") | https://sede.agenciatributaria.gob.es/Sede/subastas.html | 2 |
| Eigen buscador | JavaScript-pagina "Subastas de Bienes de la AEAT" ("Cargando datos…"); laadt het statische bestand `data2/bienes.js` | https://www2.agenciatributaria.gob.es/static_files/common/internet/dep/taiif/subastaInmuebles/index.html | 3 |
| **Downloadbare lijst** | `bienes.js`, kop: "Version: 20260914 15:23:07 / Lista de bienes a 14/09/2026 / Licencia Creative Commons Atribución 4.0 Internacional (CC BY 4.0) Permitido su uso referenciando … 'Lista de bienes a subastar por la AEAT a 14/09/2026. Más información en: https://sede.agenciatributaria.gob.es/Sede/subastas.html'". Arrays: `inmueblesSubasta` (230 records), `mueblesSubasta`, `vehiculosSubasta`, `fechaBienesSubasta`. Velden: id, tipo, subasta (SUB-AT-id), derecho (1 = pleno dominio, 2 = nuda propiedad, 99), porcTitularidad, codProvincia, municipioCod, cp, direccion, refCatastro, cru, valoracion, cargas, finSubasta, descripcion, fotos, gpsLat, gpsLong, interes, capital. 52 van 230 zijn aandelen <100%. Alicante (codProvincia 3): 3 (Orihuela 100%, Dénia 25%, Torrevieja 50% nuda propiedad). Xàbia: 0. finSubasta 14-09 t/m 28-09-2026. | (pad waargenomen in de paginabron; niet gedocumenteerd, kan wijzigen) | 3 |
| Meldingen | "Suscripción a notificaciones" bestaat, maar achter authenticatie (`wlpl/SREM-ENAJ/AutenticacionSubInm`) — niet getest | https://sede.agenciatributaria.gob.es/Sede/subastas.html | 2 |
| Procedure | RGR art. 101 (acuerdo de enajenación, anuncio, inhoud portaal), 103 (licitadores, depósito), 104 (20 kalenderdagen, puja mínima 10%), 107 (adjudicación directa: 6 maanden; na twee licitaciones geen minimumprijs). AEAT-pagina: "presentación de ofertas se llevará a cabo, en todo caso, de forma electrónica"; depósito 5% (inmuebles) / 10% (muebles); ≥50% van het tipo → adjudicatie; betaling "en los 15 días siguientes". Procedimiento RF02: primera licitación → segunda licitación → adjudicación directa → formalización y cancelación de cargas; "Nivel 4: Tramitación electrónica". | https://sede.agenciatributaria.gob.es/Sede/deudas-apremios-embargos-subastas/subastas/general.html · https://sede.agenciatributaria.gob.es/Sede/procedimientos/RF02.shtml | 2 |
| Wie voert uit | Landelijke "Unidades Regionales de Subastas" (Madrid, Valencia, Andalucía) — niet de lokale Delegación | live steekproef | 3 |
| Geblokkeerd | `/Sede/subastas-adjudicaciones.html` → 404; `/Sede/aviso-legal.html` (gegokte URL) → 404 | | 3 |

Waardering: **de best bruikbare officiële machinale bron** voor AEAT-veilingen (expliciete CC BY 4.0-licentie, dagelijkse versie, kadaster + coördinaten + einddatum). Beperking: alleen AEAT; het bestandspad is niet gedocumenteerd. Register-status: GEVERIFIEERD EN ACTIEF (lezen, met bronvermelding) — monitor moet pad-/structuurwijzigingen detecteren.

---

## 3. TGSS / Seguridad Social

| Onderdeel | Bevinding | Bewijs |
|---|---|---|
| Eigen portaal | "Subastas de Bienes Embargados": https://w6.seg-social.es/subastas/ — zoeken in drie stappen; búsqueda avanzada `SubaSeControladorInter?opcion=6&avanzada=1` met: tipo de bien (Finca Rústica, Finca Urbana, Vehículo, Embarcación, Resto de Bienes Muebles), Tasación van/tot, Cargas van/tot, fecha van/tot, tipo de enajenación van/tot, localización per comunidad/provincia (Alicante/Alacant aanwezig). Informatiepagina `opcion=5`. | 3 |
| Niet op BOE-portaal | RGRSS art. 117.1: "El anuncio de la subasta se publicará en el tablón de anuncios de la Seguridad Social situado en la sede electrónica de la Secretaría de Estado de la Seguridad Social"; TGSS-informatiepagina: "se publican dentro de la página web que la Seguridad Social tiene abierta en INTERNET". Geen verwijzing naar subastas.boe.es. | 2 |
| Procedure | Gesloten envelop met gecertificeerde cheque van 25% van het tipo (art. 117.2.e, 118.2); enveloppen tot de werkdag vóór de zitting bij de Dirección Provincial (art. 118); mondelinge biedingen ≥75% van het tipo (art. 120.3); wie zonder envelop verschijnt: 30% waarborg (art. 120.2); Mesa onder de Director Provincial (art. 119); derecho de tanteo TGSS binnen 30 dagen (art. 121); betaling binnen 5 werkdagen (informatiepagina TGSS) [te verifiëren in art. 120]. | 2 |
| Documenten | Anuncio met beschrijving, titularidad, tipo, plaats en tijden van inzage van "títulos de propiedad", lasten die blijven bestaan (art. 117.2.a–b). | 2 |
| RSS / e-mail / API / open data | Niet aangetroffen. datos.gob.es vermeldt alleen een **Android-app van een derde** (2015, laatste update 2016; "El autor de esta app no tiene ningún tipo de relación … con la Seguridad Social"). Geen officiële dataset. | 3 |
| Robots / voorwaarden | `w6.seg-social.es/robots.txt` geeft een HTML-foutpagina (geen robots-bestand); geen gebruiksvoorwaarden voor automatisering gezien. Servlet-formulier zonder gedocumenteerde parameters. | 3 |
| Live telling Alicante | **Niet uitgevoerd** (formulierparameters niet openbaar; geen bulkverzoeken). | 7 |
| Geblokkeerd | seg-social.es/wps/portal/wss/internet/InformacionUtil/5300/1502 → inhoud niet gevonden (foutpagina) | 3 |
| Apart kanaal | Verkoop van **eigen patrimonium** van de TGSS gaat via BOE Sección V-B ("procedimiento abierto de bien inmueble de su propiedad", Sevilla, 14-09-2026) — dat zijn geen executieveilingen. | 3 |

Register-status: ALLEEN HANDMATIG (wekelijkse handmatige controle op provincie Alicante/fincas urbanas y rústicas).

---

## 4. SUMA Gestión Tributaria (Diputación de Alicante)

| Onderdeel | Bevinding | Bewijs |
|---|---|---|
| Publicatie | Pagina "Subastas y adjudicación directa" (https://www.suma.es/procedimiento-subastas): "Para visualizar las subastas en trámite, debe acceder al Portal de subastas del BOE". Geen eigen lijst op suma.es; adjudicación directa wordt alleen gepubliceerd als er een procedure loopt: op 14-09-2026 "NO HAY ABIERTO PROCEDIMIENTOS EN PLAZO". | 2/3 |
| Op het BOE-portaal | Type "Otras administraciones tributarias" (SUB-RC-…), autoridad "Suma Gestión Tributaria. Diputación de Alicante", "Tipo de subasta: RECAUDACIÓN TRIBUTARIA". Op 14-09-2026: **17 lots** "Próxima apertura" in de provincie (één gezamenlijke aankondiging BOE-B-2026-29836). | 3 |
| Regels | Waarborg "mínimo del 5% del tipo de subasta"; 20 kalenderdagen; "La subasta no se cerrará hasta que haya transcurrido una hora desde la realización de la última puja"; betaling "15 días siguientes a la notificación"; adjudicación directa: 5% waarborg, één maand voor biedingen, betaling binnen 15 dagen, contact adjudicacion.directa@suma.es. Geen minimumbod in de tweede ronde van adjudicación directa als 25% van het tipo lager is dan schuld + kosten + 1.000 € (dan voorstel tot toewijzing aan de schuldeiser) — uit zoekresultaat op de SUMA-pagina, [te verifiëren]. | 2 |
| Historisch | 2011–2014 publiceerde SUMA "acuerdo de enajenación, providencia y anuncio de subasta de bienes inmuebles" als BOE-B-anuncio (bijv. BOE-B-2011-3186, BOE-B-2014-3225) — vóór het portaal. | 2 |
| Robots | `suma.es/robots.txt`: `User-agent: * Disallow: /` (Googlebot deels toegestaan). Geautomatiseerd raadplegen van suma.es: niet doen. | 3 |
| Meldingen/RSS | Niet aangetroffen. | 3 |

Register-status: SUMA-veilingen zijn dekkend te volgen via het BOE-portaal (meldingen) en BOE Sección V-B (API/RSS); suma.es zelf ALLEEN HANDMATIG. **Open vraag:** valt de gemeentelijke invordering van Xàbia onder SUMA? Het tablón van Xàbia toont eigen "Edicto"-publicaties over "recaudación en vía de constrenyiment" (apremio) — [te verifiëren].

---

## 5. ATV (Agència Tributària Valenciana) en Generalitat-patrimonium

| Onderdeel | Bevinding | Bewijs |
|---|---|---|
| ATV executieveilingen | **Niet gevonden.** Op atv.gva.es geen pagina over subastas/enajenación van in beslag genomen goederen; wel pagina's over "providència d'apremi", "diligència d'embargament", uitstel/fractionering, en "Declaración informativa por quienes organicen subastas de bienes muebles" (modelo 603 — een aangifteplicht voor veilinghuizen, geen veilingkanaal). Of de ATV via het BOE-portaal ("Otras administraciones tributarias") veilt: **ONBEKEND**. | 3/7 |
| Generalitat-patrimonium | https://hisenda.gva.es/es/web/subastas (Conselleria de Economía, Hacienda y Administración Pública): verkoop van eigen patrimoniale goederen — inmuebles, vehículos, acciones, muebles; "Enajenación efectuada" (historie); "Previsión de inmuebles para enajenar". Inmuebles-lijst: 53 resultaten over 3 pagina's; pagina 1 (20): Castellón, Valencia, Madrid — **geen Alicante/Xàbia op pagina 1** (pagina 2–3 niet bekeken). Pliego: "Pliego de condiciones generales que regirá la enajenación mediante subasta pública de inmuebles patrimoniales de la Generalitat" (DOGV núm. 10093, 23-04-2025). Documentatie: anexos I–III (docx). Geen RSS/alertas; contact 012. | 2/3 |

Register-status: ATV → TECHNISCH ONDERZOEK NODIG (navragen bij ATV of via het BOE-portaal filter R + autoridad "Agència Tributària Valenciana"); GVA-patrimonium → ALLEEN HANDMATIG (maandelijks).

---

## 6. Registro Público Concursal, liquidaties en "entidad especializada"

### 6.1 Registro Público Concursal (publicidadconcursal.es)

| Onderdeel | Bevinding | Bewijs |
|---|---|---|
| Secties | Sección I "edictos concursales"; Sección II "publicidad registral de resoluciones concursales"; Sección III "acuerdos extrajudiciales". | 2 |
| Zoeken | https://www.publicidadconcursal.es/consulta-publicidad-concursal-new: zoeken op **documento identificativo (verplicht)** (NIF/paspoort/otros), naam, provincie van de oficina judicial, número de expediente (NNNNNNN/YYYY), NIG (19 tekens) **of** "Búsqueda por Día" (fecha de publicación). **CAPTCHA** ("Gire la imagen hasta que aparezca en posición vertical"). | 2 |
| Gebruiksbeperking | Aviso legal: "El uso de los datos incorporados a este Registro queda circunscrito a las finalidades previstas en la legislación concursal y demás normativa aplicable, quedando prohibido su uso para fines distintos de los legalmente estipulados." "no constituye en ningún caso un registro de morosos". | 2 |
| Robots | `Disallow:` (leeg) + sitemap — technisch niet verboden, maar de captcha en de gebruiksbeperking sluiten geautomatiseerd zoeken uit. | 3 |
| RSS / API / open data | Niet aangetroffen. | 3 |
| Rol bij notariële veiling | Notaris moet het RPC raadplegen en het expediente melden (Ley del Notariado art. 73.3). | 2 |

### 6.2 Portal de liquidaciones concursales (art. 415 bis TRLC)

https://www.publicidadconcursal.es/liquidaciones — publiceert "VENTA DE UNIDADES PRODUCTIVAS" in vijf contexten (plan de reestructuración art. 614 e.v.; fase común arts. 215–224; fase de liquidación art. 415 bis; ejecución de convenio; extraconcursal). Filters: fecha de publicación, tipo de procedimiento, **modo de venta (Venta directa / Subasta / Otro)**, denominación social, CNAE, NIF, domicilio social en domicilio de actividad (provincia, municipio). Wettelijke basis art. 415 bis TRLC: de administrador concursal "deberá remitir, para su publicación en el portal de liquidaciones concursales del Registro público concursal, cuanta información resulte necesaria para facilitar la enajenación de la masa activa". Gericht op bedrijven/productie-eenheden; losse woningen of percelen verschijnen hier niet als zodanig [4]. Geen RSS/API. [2/3]

### 6.3 Wettelijk kader liquidatie (TRLC, geconsolideerd, versie 26-09-2022, Ley 16/2022)

- Art. 421: zonder bijzondere regels realiseert de administrador concursal "del modo más conveniente para el interés del concurso".
- Art. 422: regla del conjunto (productie-eenheden als geheel, tenzij de rechter individuele verkoop toestaat).
- **Art. 423.1–2:** goederen met een waarde >5% van de inventaris worden "mediante subasta electrónica" gerealiseerd, "bien en el portal de subastas de la Agencia Estatal Boletín Oficial del Estado, bien en cualquier otro portal electrónico especializado en la liquidación de activos".
- Art. 215–216: productie-eenheden via elektronische veiling; de rechter kan "la enajenación directa … o la enajenación a través de persona o de entidad especializada" toestaan.
- LEC art. 641: realisatie "por persona o entidad especializada"; de entiteit stelt een caución; de verkoop volgt "las reglas y usos de la casa o entidad que subasta o enajene". Art. 691.6: ook toepasbaar bij hypothecaire executie. [2]

### 6.4 Bevestigde gespecialiseerde platforms

| Platform | Beheerder | Wat bevestigd | Automatisering | Bewijs |
|---|---|---|---|---|
| **subastasprocuradores.com** | Consejo General de Procuradores de España (CGPE); Colegios de Procuradores als "entidades especializadas en la realización de los bienes embargados" (LEC) | Soorten: "Subasta", "Venta directa", "Cesión de remate", "Unidad productiva"; filters provincia (52 + Portugal/International), tipo de bien, tipo de proceso, vrije tekst; rubrieken "A punto de finalizar", "Próximamente", "Novedades". Commissie 4% (inmuebles) / 15% (muebles), verschuldigd vóór de overdracht; waarborg per bankoverschrijving; registratie één per persoon, bevestiging e-mail + sms; rechtbanken Madrid. Per lot volgens de normas: edicto, tasación, certificación de cargas. | robots: alleen `/error/` uitgesloten; geen RSS/alertas/API gezien; voorwaarden over scraping niet aangetroffen → TECHNISCH ONDERZOEK NODIG. Live telling Alicante: niet mogelijk zonder JS-filter (alleen 10 uitgelichte lots zichtbaar). | 2/3 |
| **eactivos.com** | Activos Concursales, S.L. (Valencia, NIF B98206790); "Entidad especializada extrajudicial. Subastas online" — concursales, judiciales, extrajudiciales; filters per provincie (52) en categorie | Aviso legal: **"Se prohíbe el acceso a los contenidos de este Sitio Web por medio de sistemas mecanizados que sean distintos a personas físicas"**; alle inhoud auteursrechtelijk voorbehouden. | **NIET GEBRUIKEN geautomatiseerd**; alleen handmatig. | 2 |
| CNMC-resolutie S/0001/21 "plataforma de subastas electrónicas" | — | Noemt CGPE/Subastas Procuradores, eActivos en Subastas BOE als partijen/platforms; inhoud van de beslissing niet tekstueel geverifieerd (pdf niet leesbaar via de tool). | — | 7 |

Andere in de markt genoemde platforms zijn **niet** geverifieerd en worden hier bewust niet genoemd. Welk platform in een concrete liquidatie wordt gebruikt, staat in het plan/de reglas de liquidación van dat concurso (handmatig via RPC per NIF).

---

## 7. Ajuntament de Xàbia — gemeentelijke verkopen (enajenaciones)

| Onderdeel | Bevinding | Bewijs |
|---|---|---|
| Gemeentesite | https://www.ajxabia.com/ → "Contratación" (/ver/7590/contratacion.html) verwijst naar ROLECE en "Plataforma de licitación electrónica" (/ver/8132/…) met handleidingen van de **Plataforma de Contratación del Sector Público**; nieuwsbericht 10-02-2020: "La plataforma está sincronizada con el perfil del Contratante ya implementado hace unos años, y que también forma parte de la plataforma del Estado." Geen enajenaciones op de site. | 2/3 |
| Sede electrónica (esPublico Gestiona) | https://xabia.sedelectronica.es → `/info`; **Tablón de anuncios** `/board` (200): zoekveld "Busca l'anunci que necessites" en filter "Seleccionar el tipus d'anunci"; publicaties 28-08 t/m 14-09-2026: personeelsbases, "BASES GALA DEL COMERÇ", tribunal del jurado, meerdere "Edicto" over "recaudación en vía de constrenyiment". **Geen subasta/enajenación/alienació/patrimonio.** Geen RSS/atom-link in de HTML. `/contractor` → 404. Root gaf bij WebFetch "too many redirects". | 3 |
| PLACSP open data | Atom-feed (max 500 entries per bestand) en maandelijkse zips: `https://contrataciondelsectorpublico.gob.es/sindicacion/sindicacion_643/licitacionesPerfilesContratanteCompleto3_AAAAMM.zip`; "Diariamente se publican las actualizaciones producidas durante el día anterior"; dekking "no es homogéneo para todas ellas". Of Xàbia haar **patrimoniale verkopen** (geen contrato del sector público) daar publiceert: **[te verifiëren]**. Het perfil van Xàbia zelf is niet gevonden (zoekbudget op; de gevonden PLACSP-URL was van València). | 2/7 |
| BOP Alicante | Buscador: https://sede.diputacionalicante.es/consultas-bop/ — gratis; op datum; "Tipo de organismo" (o.a. ADMINISTRACIÓN LOCAL, ADMINISTRACIÓN DE JUSTICIA); secties Sumario / BOP Completo / Edictos. Pdf's op dip-alicante.es/bop2 (curl → HTTP 403). Geen RSS/API aangetroffen. Gemeentelijke enajenaciones en TGSS-aankondigingen van hogere waarde kunnen hier verschijnen [4]. | 3 |
| Wettelijk kader | RBEL (RD 1372/1986) art. 109: vervreemding van onroerend patrimonium boven 25% van de gewone begrotingsmiddelen alleen met autorisatie van de Comunidad Autónoma; altijd communicatie; art. 112: "Las enajenaciones de bienes patrimoniales se regirán en cuanto su preparación y adjudicación por la normativa reguladora de la contratación de las Corporaciones locales" — openbare veiling als regel, permuta als uitzondering; art. 118: "Será requisito previo a toda venta o permuta de bienes patrimoniales la valoración técnica de los mismos que acredite de modo fehaciente su justiprecio." | 2 |
| Patrimonio del Estado (rijksvastgoed) | Buscador de Subastas y Concursos (hacienda.gob.es) per Delegación de Economía y Hacienda (ALACANT/ALICANTE aanwezig); resultaten gesorteerd op veilingdatum; "RSS del Ministerio" alleen algemeen. Aankondigingen verschijnen in BOE V-B (bijv. Cádiz 11-09, Cuenca 14-09-2026). | 2/3 |

Register-status: ALLEEN HANDMATIG (tablón wekelijks; BOP wekelijks), PLACSP-feed TECHNISCH ONDERZOEK NODIG.

---

## 8. Juzgados / Tribunal de Instancia de Dénia (partido judicial van Xàbia)

| Onderdeel | Bevinding | Bewijs |
|---|---|---|
| Orgaan | **Sección Civil del Tribunal de Instancia de Dénia**, Pl. Jaime I, 23, 03700 Dénia, tel. 965 35 31 28; zes plazas (nº 1–6); ressorteert onder de Audiencia Provincial de Alicante (sede.gva.es, id_dept 26350). Sinds LO 1/2025 heten de vroegere "Juzgados de Primera Instancia" zo; in het BOE-sumario van 14-09-2026 staan departamentos als "TRIBUNALES DE INSTANCIA. SECCIÓN CIVIL". | 2/3 |
| Partido judicial | Dénia is partido judicial nº 1 van Alicante; omvat o.a. Xàbia/Jávea, Benissa, Calp, Teulada (mjusticia-/Diputación-lijst via zoekresultaat; Diputación-pagina zelf onbereikbaar: DNS-fout). | 2 |
| Waar veilingedicten verschijnen | (1) BOE Sección IV "Administración de Justicia": item met **titel = plaats van de rechtbank** ("DENIA") en tekst "Anuncio de subasta judicial en vía de apremio" met portaal-id en `ds.php`-link — voorbeeld BOE-B-2022-17675 (Juzgado de Primera Instancia nº 1 de Dénia, 04-06-2022, SUB-JA-2022-195732); (2) het edicto zelf met documenten op subastas.boe.es (LEC art. 646.2, 668.2). | 2/3 |
| Andere edictos (notificaties, geen veiling) | **Tablón Edictal Judicial Único** (TEJU), https://www.boe.es/edictos_judiciales — sinds 01-06-2021; RD 181/2008 art. 14 en 17; vrij toegankelijk 4 maanden, daarna verificatiecode; filters: tekst (orgaan, personen, bedrijf, procedurenummer, NIG, NIF/NIE), órgano, jurisdicción, nummer, datum. Geen RSS/API; boe.es-robots sluit `/edictos_judiciales/` uit. Veilingaankondigingen lopen niet via TEJU maar via Sección IV + portaal. | 2/3 |
| Live | Op 14-09-2026 geen lopende of aanstaande veiling van onroerend goed met een Dénia-orgaan als autoridad gestora in de provincie Alicante. | 3 |

Register-status: BOE Sección IV via API/RSS — GEVERIFIEERD EN ACTIEF; TEJU — ALLEEN HANDMATIG.

---

## 9. Bronnenregister (sectie 7 masterprompt — samenvatting)

| Bron | Type | Technische toegang | Dekking | Status | Notities |
|---|---|---|---|---|---|
| Portal de Subastas BOE | Officieel veilingportaal (AEBOE) | HTML-zoek/detail; e-mailmeldingen na registratie; geen RSS/API/download; robots Disallow / | Landelijk: judicial, notarial, AEAT, otras adm. tributarias (SUMA), adm. generales | ALLEEN HANDMATIG + e-mailmeldingen; automatisering: CONTRACT OF TOESTEMMING NODIG | Registratie alleen natuurlijk persoon (Jan); ≤50 opgeslagen zoekopdrachten |
| BOE open-data-API sumario + RSS s=4 / s=5B | Officiële open data | XML-API (Accept: application/xml), RSS 2.0 | Alle dagelijkse aankondigingen (Sección IV justicia; V-B AEAT/SUMA/TGSS-patrimonium/Hacienda) | GEVERIFIEERD EN ACTIEF | Hergebruik gratis, bronvermelding verplicht; ratelimits onbekend |
| BOE API legislación consolidada | Officiële open data | XML-API | Wetteksten met versiehistorie | GEVERIFIEERD EN ACTIEF | Gebruikt voor LEC/RGR/RGRSS/Notariado/TRLC |
| AEAT sede "Subastas" + `bienes.js` | Officieel | Statisch JS-databestand, dagelijkse versie, CC BY 4.0 | Alleen AEAT, landelijk (230 inmuebles op 14-09-2026) | GEVERIFIEERD EN ACTIEF (lezen) | Ongedocumenteerd pad; wijzigingen bewaken |
| AEAT suscripción a notificaciones | Officieel | Achter authenticatie | AEAT | TECHNISCH ONDERZOEK NODIG | Alleen na inloggen door Jan te testen |
| TGSS w6.seg-social.es/subastas | Officieel portaal TGSS | Servlet-formulier; geen feeds | TGSS-executieveilingen landelijk | ALLEEN HANDMATIG | Gesloten envelop, 25% cheque, fysiek bij Dirección Provincial |
| SUMA suma.es/procedimiento-subastas | Officieel (Diputación de Alicante) | HTML; robots Disallow / | Provincie Alicante; veilingen zelf op BOE-portaal | ALLEEN HANDMATIG (dekking via BOE) | Adjudicación directa alleen als open |
| ATV | Officieel | Niets gevonden | ? | TECHNISCH ONDERZOEK NODIG | Navragen |
| GVA hisenda.gva.es/es/web/subastas | Officieel (patrimonium Generalitat) | HTML-lijst; geen feeds | Comunitat Valenciana | ALLEEN HANDMATIG | Pliego DOGV 23-04-2025 |
| Registro Público Concursal | Officieel (Colegio de Registradores / MJus) | Zoek op NIF of dag + CAPTCHA | Landelijk | ALLEEN HANDMATIG | Gebruik beperkt tot wettelijke doelen |
| Portal de liquidaciones concursales | Officieel | HTML-filters | Productie-eenheden landelijk | ALLEEN HANDMATIG | Geen losse woningen |
| subastasprocuradores.com | Entidad especializada (CGPE) | HTML; geen feeds gezien | Landelijk | TECHNISCH ONDERZOEK NODIG | 4% commissie inmuebles; voorwaarden over automatisering onbekend |
| eactivos.com | Entidad especializada (privaat) | HTML | Landelijk | NIET GEBRUIKEN (geautomatiseerd); handmatig mag | Verbod op "sistemas mecanizados" |
| Ajuntament de Xàbia sede/board | Officieel gemeentelijk | HTML; geen RSS gezien | Xàbia | ALLEEN HANDMATIG | Geen enajenaciones op 14-09-2026 |
| PLACSP open data (Atom/zip) | Officieel open data | Atom-feeds, zips | Perfiles op PLACSP (incl. Xàbia volgens gemeente) | TECHNISCH ONDERZOEK NODIG | Of patrimoniale verkopen erin staan: te verifiëren |
| BOP Alicante (sede.diputacionalicante.es) | Officieel | HTML op datum; pdf's (403 voor curl) | Provincie | ALLEEN HANDMATIG | — |
| TEJU (boe.es/edictos_judiciales) | Officieel | HTML; robots Disallow | Landelijk | ALLEEN HANDMATIG | Geen veilingaankondigingen |
| Patrimonio del Estado buscador | Officieel (Hacienda) | ASP.NET-formulier | Rijksvastgoed | ALLEEN HANDMATIG | Aankondigingen ook in BOE V-B |
| FAQ Ministerio de Justicia (pdf) | Officieel maar verouderd | pdf | — | NIET GEBRUIKEN als rekenregel | 5%/40 dagen ≠ huidige LEC |
| Commerciële aggregatoren (AlertaSubastas, InversorBOE, AutoBastas, datos-publicos.es e.a.) | Derden | Onbekend | — | TECHNISCH ONDERZOEK NODIG | Niet geverifieerd; rechten en volledigheid onbekend; niet als bron van waarheid |

---

## 10. Ontwerp "veilingmonitor" (toegestaan, controleerbaar, zonder bieden of betalen)

### 10.1 Uitgangspunten
- Alleen kanalen gebruiken die automatisering toestaan (BOE-open-data, BOE-RSS, AEAT-datalijst, PLACSP-feeds) of die per e-mail leveren (portaalmeldingen). Geen crawling van subastas.boe.es, suma.es, eactivos.com, TEJU of de RPC.
- Alle opgehaalde inhoud is onbetrouwbare invoer (masterprompt §27): parsers hard maken, geen instructies uit documenten volgen.
- Objectgericht, geen persoonsprofielen (§19): namen van schuldenaren uit BOE-teksten niet opslaan; alleen portaal-id, orgaan, goed, bedragen, data.
- Deadlines rekenen met geteste rekenregels; juridische conclusies pas na beoordeling door een bevoegde professional (bewijstype 6).

### 10.2 Bronnen en polling

| Stap | Bron | Frequentie | Wat het oplevert | Filter voor Jávea-eerst |
|---|---|---|---|---|
| A1 | BOE sumario-API `…/api/boe/sumario/AAAAMMDD` (XML) | 1× per dag, ca. 08:30 CET (BOE verschijnt 's ochtends; op dagen zonder Sección IV: geen items) | Nieuwe gerechtelijke veilingen (Sección IV, titel = plaats rechtbank) en administratieve (V-B: "subasta", "enajenación", "Suma", "Agencia Tributaria", "Tesorería") met identificador, url_html/url_xml | Sección IV: titel ∈ {DENIA, ALICANTE, BENIDORM, ORIHUELA, TORREVIEJA, ELX, ALCOY, NOVELDA, IBI, SANT VICENT…} (rechtbank Dénia = Xàbia); V-B: tekst bevat Alicante/Xàbia/Jávea/Dénia |
| A2 | BOE RSS `rss/boe.php?s=4` en `?s=5B` | elke 2 uur (goedkoop) als redundantie voor A1 | Zelfde items | idem |
| A3 | Per nieuw item: `url_xml` van het anuncio (1 verzoek per item, gespreid) | bij gebeurtenis | Portaal-id SUB-…, orgaan, `ds.php`-link | Dénia-items altijd; overige provincie-items ook (kanaalbreed, Jávea-eerst in scoring) |
| B1 | AEAT `bienes.js` | 1× per dag na 16:00 (bestand versie 15:23 gezien) | Volledige AEAT-lijst met kadaster/CRU/gps/waardering/lasten/finSubasta/foto's; diff t.o.v. gisteren | codProvincia = 3; cp 0373x; gps binnen bounding box Xàbia |
| C1 | Portaal-e-mailmeldingen (account van Jan; ≤50 zoekopdrachten, bijv. provincie 03 × estados PU/EJ × tipo I, plus localidad-varianten "Xàbia", "Jávea", "Javea", "Dénia", "Benitachell", "Teulada", "Moraira", "Benissa", "Calp") | per e-mail (event) | Statuswijzigingen en nieuwe veilingen die aan criteria voldoen | via IMAP-mailbox uitlezen (bestaande Resend/GHL-koppelingen niet nodig) |
| C2 | Handmatige controle detailpagina's (Jan of medewerker) voor elke kandidaat uit A/B/C | binnen 1 werkdag na signaal | Tabblad Bienes, Importe del depósito, Fecha de conclusión, documenten (na inloggen: edicto, certificación, tasación, registerinformatie) | — |
| D1 | TGSS-portaal, GVA-patrimonium, BOP Alicante, tablón Xàbia, RPC-dagzoekopdracht, procuradoresportaal | wekelijks handmatig (checklist) | Kanalen zonder feeds | provincie Alicante / Dénia / Xàbia |
| D2 | PLACSP Atom-feed | dagelijks (na verificatie dat patrimoniale verkopen erin staan) | Gemeentelijke enajenaciones | órgano bevat "Xàbia"/"Jávea" |

### 10.3 Datamodel en gebeurtenissen (masterprompt §10 en §19)
Per veiling: `portal_id` (SUB-…), `boe_anuncio_id`, `tipo` (J/N/A/R/G/TGSS/concursal/municipal), `autoridad_gestora`, `expediente`, `estado` (PU/EJ/SU/CA/PC/FS), `fecha_inicio`, `fecha_conclusion`, `valor_subasta`, `tasacion`, `puja_minima`, `tramo`, `importe_deposito`, `cantidad_reclamada`, `derecho_subastado` (pleno dominio / % aandeel / nuda propiedad / usufructo), `situacion_posesoria`, `visitable`, `cargas`, `ref_catastral`, `cru`, `localidad`, `cp`, `documentos[]` met versie/hash, plus tijdstempels `source_published_at` (BOE-datum), `first_seen_at`, `last_successful_fetch_at`, `last_seen_at`, `analysis_completed_at`.
Gebeurtenissen: NIEUW GEPUBLICEERD (BOE-item vandaag) · NIEUW DOOR ONS ONTDEKT (eerste keer gezien, BOE-datum ouder) · STATUS GEWIJZIGD (PU→EJ→PC/FS, SU, CA) · DOCUMENTEN GEWIJZIGD (hash) · PRIJS GEWIJZIGD (n.v.t. bij veiling; wel bij tweede licitación/adjudicación directa) · NIET MEER GEVONDEN · BRON NIET BEREIKBAAR (API 4xx/5xx, leeg sumario op een werkdag, bienes.js zonder nieuwe versie >48 u).

### 10.4 Deadlinebewaking (rekenregels, per kanaal)

| Moment | Judicial | Notarial | AEAT / SUMA | TGSS |
|---|---|---|---|---|
| Opening | ≥24 u na BOE-publicatie (LEC 648.2ª) | ≥24 u (LN 75.1.2ª) | ≥24 u na BOE (RGR 101.3) | zittingsdatum in anuncio |
| Sluiting | portaalveld "Fecha de conclusión" (20 kalenderdagen; niet in weekend/feestdag/24-12–06-01/augustus, LEC 649.1) | portaalveld (≥20 dagen) | portaalveld (20 dagen, RGR 104.2) | werkdag vóór zitting = uiterste envelop (RGRSS 118.1) |
| Verlengingsmarge | tot +24 u bij laatste-uur-bod (help) | idem | idem; SUMA: +1 u na laatste bod | n.v.t. |
| Waarborg klaarzetten | 20% (min. 1.000 €) of edicto-afwijking (LEC 669.1) — portaalveld "Importe del depósito" is leidend | 5% (LN 75.1.4ª) of pliego | 5% (portaalveld) | 25% cheque, fysiek |
| Betaling rest | 20 dagen na sluiting (LEC 670.1) | per pliego | 15 dagen na notificatie (RGR 101.4.f) | 5 werkdagen (TGSS-pagina) |
| Ná-veiling risico's | ejecutado kan 10 dagen iemand ≥60% aandragen bij bod <70% (670.3); reserva de postura (652); cesión de remate | — | tweede licitación / adjudicación directa (RGR 107) | tanteo TGSS 30 dagen (RGRSS 121) |
| Signalen | T-7, T-3, T-1, T-2 u vóór sluiting; T+1 (remate/decreto), betaaldeadline -5 dagen | | | |

Alle termijnen als **liquiditeitsbeslag** modelleren (§19), niet als kosten. Geen uniform percentage over kanalen heen.

### 10.5 Wat NIET geautomatiseerd wordt (harde grens)
- Registreren/inloggen op het portaal, waarborg storten, bieden, pujas automáticas, reserva de postura, cesión de remate, betalen, documenten ondertekenen, contact met schuldenaren/bewoners, bezichtiging aanvragen: **uitsluitend Jan zelf** (masterprompt §19 en §27; huisregels 2 en 3).
- Geen scraping van portalen met robots-Disallow of verbodsclausule (subastas.boe.es, suma.es, eactivos.com, TEJU) en geen captcha-omzeiling (RPC).
- Geen definitief biedadvies zonder juridische beoordeling (bewijstype 6): certificación de cargas, situación posesoria, rangorde lasten, aandeel/blote eigendom.

### 10.6 Bouwvolgorde (fase B-voorstel, geen toezegging dat iets al draait)
1. Nulmeting: A1 over de laatste 30 dagen (sumario per dag) + B1 vandaag → tabel per kanaal, Jávea = 0, Dénia-rechtbank = 0 (bevestigd 14-09-2026).
2. Dagelijkse A1/B1-run in de Hermes-venv (httpx, standaard `xml.etree` — geen lxml nodig; geen installaties), opslag in SQLite naast tree-ai-agentic-os (niet in de Tree-AI-OS-Postgres).
3. Meldingen via de bestaande Hermes-gateway (Discord/Telegram) — alleen signaleren.
4. Jan registreert op het portaal en stelt ≤50 meldingen in (⏸️ ACTIE VOOR JAN); mailbox-inlezing daarna.
5. Toestemmingsvraag aan de AEBOE over gerichte automatische detailraadpleging; tot dan handmatig.

---

## 11. Openstaande vragen
1. Valt het Portal de Subastas onder de hergebruiksvoorwaarden van de AEBOE (Ley 37/2007)? Kan gerichte automatische raadpleging van detailpagina's per SUB-id worden toegestaan? (navraag AEBOE)
2. Veilt de ATV in beslag genomen goederen, en zo ja via het BOE-portaal ("Otras administraciones tributarias") of anders?
3. Is de gemeentelijke invordering van Xàbia bij SUMA ondergebracht of doet de gemeente dat zelf (edictos "vía de constrenyiment" op het tablón)?
4. Publiceert Xàbia patrimoniale verkopen op PLACSP (en dus in de open-data-Atom-feed) of alleen in BOP/tablón?
5. Ratelimits en fair-use van de BOE-open-data-API (FAQ-pagina niet toegankelijk).
6. Blijft het AEAT-bestandspad `data2/bienes.js` stabiel; is er een gedocumenteerde downloadlocatie?
7. Betaaltermijn TGSS (5 werkdagen) — bevestigen in art. 120 RGRSS (tekst slechts deels gelezen).
8. Voorwaarden van subastasprocuradores.com over geautomatiseerd raadplegen; bestaat er een meldingsdienst?
9. Ondersteunt het BOE-portaal via Mi BOE een dagelijkse alert op Sección IV-aankondigingen met tekst "Dénia" (te testen na registratie)?
10. Welke aggregatoren zijn licentie-technisch bruikbaar als tweede lijn (niet geverifieerd)?

## 12. Geblokkeerd of mislukt (transparant)
- subastas.boe.es: eerste twee zoekverzoeken → "ERROR: Se ha producido un error en la búsqueda" (datumvelden moeten arrays zijn); daarna geslaagd. `textoPolitica.php` eenmalig HTTP 502 via WebFetch, later via curl OK.
- sede.agenciatributaria.gob.es/Sede/subastas-adjudicaciones.html → 404; /Sede/aviso-legal.html (gegokt) → 404; AEAT-buscador is JavaScript-only voor WebFetch (data via `bienes.js` gelezen).
- seg-social.es InformacionUtil-pagina → "No se ha encontrado contenido"; w6.seg-social.es/robots.txt → HTML-foutpagina.
- xabia.sedelectronica.es root → te veel redirects (board wel gelezen); /contractor → 404.
- dip-alicante.es/bop2 → HTTP 403 (curl); documentacion.diputacionalicante.es → DNS niet gevonden.
- boe.es/datosabiertos/faq/ → "El acceso a la dirección URL solicitada no está permitido" (WebFetch 403); API-documentatie-pdf's niet tekstueel leesbaar.
- BOE-API met `Accept: application/json` → 400; alleen `application/xml` werkte.
- CGPJ-directorypagina Dénia → 404 (gva.es-pagina gebruikt).
- Pdf's (Ministerio FAQ deels; Uría LO 1/2025; CNMC S/0001/21; normas procuradores) niet of slechts gedeeltelijk leesbaar via de tool.
- WebSearch-budget van de sessie was op vóór de laatste twee zoekopdrachten (RBEL-id — opgelost via ELI-URL; AEAT-aviso legal — niet gevonden).
- Niet uitgevoerd (bewust): live tellingen op TGSS-portaal, procuradoresportaal, RPC (captcha) en GVA-pagina's 2–3.

---

## 13. Bronnenlijst (URL · controledatum · bewijstype)

**Portal de Subastas / BOE**
- https://subastas.boe.es/ · 14-09-2026 · 3
- https://subastas.boe.es/subastas_ava.php (formulier + POST-resultaten Alicante EJ/PU) · 14-09-2026 · 3
- https://subastas.boe.es/ayuda.php · 14-09-2026 · 2
- https://subastas.boe.es/acceso.php · 14-09-2026 · 2
- https://subastas.boe.es/textoPolitica.php · 14-09-2026 · 3
- https://subastas.boe.es/robots.txt · 14-09-2026 · 3
- https://subastas.boe.es/detalleSubasta.php?idSub=SUB-AT-2026-26R2886001392 (ver=1, ver=3) · 14-09-2026 · 3
- https://subastas.boe.es/detalleSubasta.php?idSub=SUB-RC-2026-0026I20250184 · 14-09-2026 · 3
- https://www.boe.es/datosabiertos/ · 14-09-2026 · 2
- https://www.boe.es/datosabiertos/api/boe/sumario/20260914 · /20260911 · /20220604 · 14-09-2026 · 3
- https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-2000-323/texto/bloque/a641 (+ a643–a650, a652, a667–a671, a691) · 14-09-2026 · 2
- https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-2005-14803/texto/bloque/a101 (+ a103, a104, a107) · 14-09-2026 · 2
- https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-2004-11836/texto/bloque/a116 (+ a117–a121) · 14-09-2026 · 2
- https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-1862-4073/texto/bloque/a72 (+ a73–a77) · 14-09-2026 · 2
- https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-2020-4859/texto/bloque/a2-27 (art. 215), a2-28 (216), a4-114 (415 bis), a4-33 (421), a4-34 (422), a4-35 (423) · 14-09-2026 · 2
- https://www.boe.es/eli/es/rd/1986/06/13/1372/con (RBEL art. 109, 112, 118) · 14-09-2026 · 2
- https://www.boe.es/rss/ · https://www.boe.es/rss/boe.php?s=4 · ?s=5B · 14-09-2026 · 3
- https://www.boe.es/alertas/ · 14-09-2026 · 2
- https://www.boe.es/informacion/aviso_legal/index.php · 14-09-2026 · 2
- https://www.boe.es/robots.txt · 14-09-2026 · 3
- https://www.boe.es/diario_boe/txt.php?id=BOE-B-2026-29751 · 14-09-2026 · 3
- https://www.boe.es/diario_boe/txt.php?id=BOE-B-2022-17675 · 14-09-2026 · 2
- https://www.boe.es/buscar/ayudas/edictos_judiciales_ayuda.php (TEJU) · 14-09-2026 · 2
- https://www.boe.es/biblioteca_juridica/codigos/codigo.php?id=162_Codigo_de_Subastas_Electronicas&modo=2 · 14-09-2026 · 2 (alleen indexpagina)
- https://www.mjusticia.gob.es/es/AreaTematica/OficinaRecuperacion/Documents/1292428756586-Preguntas_frecuentes_en_subastas_electronicas.PDF · 14-09-2026 · 7 (verouderd)
- https://e-justice.europa.eu/topics/court-procedures/judicial-auctions/es_es · 14-09-2026 · 2

**AEAT**
- https://sede.agenciatributaria.gob.es/Sede/subastas.html · 14-09-2026 · 2
- https://sede.agenciatributaria.gob.es/Sede/deudas-apremios-embargos-subastas/subastas/general.html · 14-09-2026 · 2
- https://sede.agenciatributaria.gob.es/Sede/procedimientos/RF02.shtml · 14-09-2026 · 2
- https://www2.agenciatributaria.gob.es/static_files/common/internet/dep/taiif/subastaInmuebles/index.html · 14-09-2026 · 3
- https://www2.agenciatributaria.gob.es/static_files/common/internet/dep/taiif/subastaInmuebles/data2/bienes.js · 14-09-2026 · 3

**TGSS**
- https://w6.seg-social.es/subastas/ · ?opcion=5 · ?opcion=6 · ?opcion=6&avanzada=1 · 14-09-2026 · 2/3
- https://datos.gob.es/es/aplicaciones/subastas-seguridad-social · 14-09-2026 · 3

**SUMA / ATV / GVA**
- https://www.suma.es/ · https://www.suma.es/procedimiento-subastas · https://www.suma.es/robots.txt · 14-09-2026 · 2/3
- https://www.boe.es/buscar/doc.php?id=BOE-B-2011-3186 · BOE-B-2014-3225 (zoekresultaat) · 14-09-2026 · 2
- https://atv.gva.es/ (+ site-zoekresultaten) · 14-09-2026 · 3
- https://hisenda.gva.es/es/web/subastas · /inmuebles1 · /documentacion · 14-09-2026 · 2/3

**Concursal / entidad especializada**
- https://www.publicidadconcursal.es/ · /consulta-publicidad-concursal-new · /liquidaciones · /robots.txt · 14-09-2026 · 2/3
- https://subastasprocuradores.com/ · /terms?culture=es · /buscar?culture=es · /proyecto/rules?culture=es · https://www.subastasprocuradores.com/robots.txt · 14-09-2026 · 2/3
- https://www.eactivos.com/ · /aviso-legal · /robots.txt · 14-09-2026 · 2/3
- https://www.cnmc.es/sites/default/files/5563782.pdf · 14-09-2026 · 7 (niet volledig leesbaar)
- https://ga-p.com/publicaciones/liquidacion-concursal-de-bienes-por-subasta-electronica/ · 14-09-2026 · 4 (secundair; TRLC-tekst primair geverifieerd)
- https://enjusticia.es/?p=904 · 14-09-2026 · 4 (secundair)

**Xàbia / Dénia / provincie**
- https://www.ajxabia.com/ · /ver/7590/contratacion.html · /ver/8132/plataforma-de-licitacion-electronica.html · /ver/8130/el-ayuntamiento-de-xabia-activa-la-plataforma-de-licitacion-electronica.html/ · 14-09-2026 · 2/3
- https://xabia.sedelectronica.es/board · 14-09-2026 · 3
- https://www.hacienda.gob.es/en-GB/GobiernoAbierto/Datos%20Abiertos/Paginas/LicitacionesContratante.aspx (PLACSP open data) · 14-09-2026 · 2
- https://sede.diputacionalicante.es/consultas-bop/ · 14-09-2026 · 3
- https://sede.gva.es/es/detall-organ-juridic?id_dept=26350 (Sección Civil TI Dénia) · 14-09-2026 · 2
- https://www.hacienda.gob.es/es-ES/Areas%20Tematicas/Patrimonio%20del%20Estado/Gestion%20Patrimonial%20del%20Estado/Paginas/Subastas/BuscadorSubastasConcursos.aspx · 14-09-2026 · 2

**Lokale feiten (bewijstype 3, 14-09-2026):** Idealista-assistent gaf 0 resultaten met filter "de bancos" voor Jávea (eerdere test dezelfde dag); properties-api op 0 objecten na DNS-uitval — bronuitval is reëel en moet in de monitor als BRON NIET BEREIKBAAR worden gelogd.

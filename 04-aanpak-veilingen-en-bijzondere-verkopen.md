# Deliverable 4 — Aanpak veilingen en bijzondere verkopen

**Project:** TREE Deal Hunter, fase A · **Masterprompt:** §18, §19, §30, §31.4
**Controledatum:** 15-09-2026. Metingen uit de eerdere ronde staan met hun eigen datum (14-09-2026). De lokale feedcontrole (poort 3100) is zelf uitgevoerd op 15-09-2026.
**Status:** onderzoeksdeliverable, geen juridisch of fiscaal advies. Alles met bewijstype 4, 5 of 7 en elk **[te verifiëren]** vraagt bevestiging door een Spaanse advocaat of gestor (bewijstype 6) vóór er een biedingsvoorstel komt.
**Basis:** uitsluitend `onderzoek/R08`, `R09`, `R10`, `R14`, `R16` met hun `.verificatie.md`-bestanden, plus de lokale feiten. Voor de koppeling van Sareb-perceel A aan kandidaat K10 ook `R15` met verificatie en deliverables 02 §2.5, 03 §2.6 en 05. Weerlegde claims zijn in hun gecorrigeerde vorm gebruikt.
**Verwijzingen:** [S..] verwijst naar de bronnenlijst onderaan (URL, controledatum, bewijstype). Het bewijstype staat bij de bewering tussen haken: 1 aanbieder · 2 officiële bron · 3 door ons vastgesteld · 4 AI-gevolgtrekking · 5 berekening op aannames · 6 professional · 7 onbekend of tegenstrijdig.

## Samenvatting (10 regels)

1. In Jávea/Xàbia staat vandaag geen veiling open: 0 van de 41 aanstaande en 0 van de 41–43 lopende vastgoedveilingen in de provincie Alicante, en 0 van de rechtbank van Dénia (14 en 15-09-2026) [3].
2. Bank- en servicerkanalen tonen in Jávea 0 woningen en 2 unieke percelen, volgens de servicer allebei eigendom van Sareb en alleen voor professionals (15-09-2026) [1/3]: Idealista "de bancos" 1 perceel (111869151), Servihabitat Profesionales 2, waarvan perceel A waarschijnlijk hetzelfde object is als 111869151 en kandidaat K10 [4], met tegenstrijdige planklasse [7].
3. Signalen komen uit vier officiële ingangen: de BOE-sumario-API, de AEAT-lijst `bienes.js` (CC BY 4.0), e-mailalerts van het BOE-veilingportaal (account van Jan) en handmatige kanalen (TGSS, RPC, gespecialiseerde portalen) [2/3].
4. Correctie op R08 en R17: een BOE-aankondiging noemt nooit de plaats van het goed (LEC 646.1, RGR 101.3). Een Jávea-filter op BOE-data werkt dus niet; lokaliseren kan alleen via portaalalerts, `bienes.js`, een handmatige klik of toestemming van de AEBOE [2/3].
5. Het veilingportaal mag niet gecrawld worden (robots.txt `Disallow: /`). Registreren, storten, bieden, betalen en tekenen worden nooit geautomatiseerd [3].
6. De regels verschillen per kanaal. Gerechtelijk nieuw regime: 20 % waarborg en 20 dagen om te betalen; oud regime: 5 % en 40 dagen; AEAT/SUMA: 5 % en 15 dagen; TGSS: 25 % per cheque, 5 werkdagen en 30 dagen voorkeursrecht [2].
7. Eerdere lasten blijven bij executieveilingen bestaan en latere worden doorgehaald. In een faillissement worden pre-concursale lasten doorgehaald, op kosten van de koper [2].
8. ITP bij toewijzing is 9 % (11 % boven 1 M€). Volgens DGT en TSXG is de grondslag de hoogste van valor de referencia en toewijzingsprijs; de praktijk van de ATV is [te verifiëren] [2/1/7].
9. Harde blokkades: ander recht dan 100 % volle eigendom, ontbrekende of verouderde certificación, onduidelijke bezetting, tasación 0 of ontbrekend, geschorste procedure, onbekend regime, niet-financierbare betaaltermijn of een openstaand voorkeursrecht [2/4].
10. Geen persoonsprofielen: de monitor slaat alleen objectvelden op, de parser weigert namen en NIF's, en persoonsgegevens voor één concreet bod staan alleen in een afgeschermd dossier met verwijderdatum [4, op basis van 2].

---

## 1. Conclusie — wat Jan moet weten en beslissen

**Wat je moet weten**

- **De oogst in Jávea is klein.** Vandaag zijn er nul veilingen en nul bankwoningen; Idealista "de bancos" toont 1 perceel en Servihabitat Profesionales 2 Sareb-percelen voor professionals (§2.3). Eén daarvan (perceel A) is waarschijnlijk hetzelfde object als dat Idealista-perceel en kandidaat K10 uit deliverable 03 [4]. Reken op veel dagen met "geen sterke kansen". De waarde van deze stroom zit in twee dingen: vroeg zien wat er vrijkomt, en vooral verkeerde biedingen voorkomen.
- **Monitoren kost weinig en mag.** Het gaat om één API-aanroep per dag bij de BOE, één bestand per dag van de AEAT en e-mailalerts. Maar het BOE-signaal zegt niet wáár het goed ligt. Elke kandidaat vraagt daarom een portaalalert of een menselijke klik (§2.9).
- **Een veilingbod is vooral liquiditeit.** Bij een gerechtelijke veiling in een procedure die na 03-04-2025 is gestart, staat 20 % van de veilingwaarde vast tijdens de veiling. De rest moet binnen 20 dagen na sluiting betaald zijn (LEC 669.1, 670.1) [2]. Financiering moet dus rond zijn vóór het eerste bod.
- **Geen advocaat, geen bod.** Zonder oordeel van een Spaanse advocaat per dossier komt er geen biedingsvoorstel (§7). Losse leningen (NPL) en *cesiones de remate* blijven in fase A buiten beeld (§2.4.9); faillissementsverkopen alleen handmatig, per dossier (§2.4.6).

**Drie vragen aan Jan (nu)**

Deze vragen worden niet los voorgelegd: de geconsolideerde top-3 voor alle vijf deliverables staat in deliverable 01 §1.2 (het entiteitsdeel van vraag 2 valt onder vraag 1 daar; vraag 1 en 3 volgen in ronde 2 of 3).

1. Registreer je jezelf op subastas.boe.es? Registratie kan alleen als natuurlijk persoon [S30]. Wil je daarna de alerts instellen (lijst in §2.9) en de gebruiksvoorwaarden als pdf bewaren, zodat we kunnen nagaan of wij de alertmails mogen inlezen?
2. Welke Spaanse advocaat (executies en procesrecht) en welke gestor beoordelen veilingdossiers? En onder welke entiteit wordt later geboden? Dat laatste bepaalt de vertegenwoordiging (LEC 647.1.1º), de fiscale positie en wie verwerkingsverantwoordelijke is.
3. Mogen wij een conceptbrief aan de AEBOE opstellen met de vraag om toestemming voor gerichte, automatische raadpleging van één detailpagina per nieuw veiling-ID? Versturen gebeurt pas na jouw "ja".

**Later te beslissen (niet nu):** servicer-accounts en de route als samenwerkend makelaar (R10 §10), een plafond voor waarborgsommen die tegelijk vaststaan, en of onverdeelde aandelen of blote eigendom ooit bespreekbaar zijn (standaard: nee).

---

## 2. Onderbouwing

### 2.1 Zeven soorten bijzondere verkoop: wat je werkelijk koopt

| Type (§18) | Wat je verwerft | Verkoper of beherende instantie | Kanaal | Jávea, stand 14/15-09-2026 | Bron |
|---|---|---|---|---|---|
| **A. Hypothecaire executie** (gerechtelijk LEC 681–698; notarieel LH 129) | Het goed. Eerdere lasten blijven, latere worden doorgehaald | Letrado de la Administración de Justicia (rechtbank Dénia voor Xàbia) of notaris | BOE Sección IV + portaal (SUB-JA); notarieel via portaal | 0 lopend of aanstaand [3] | S1, S4, S32 |
| **B. Andere gerechtelijke verkoop** (beslag; convenio de realización LEC 640; entidad especializada) | Idem | LAJ; Colegios de Procuradores als entidad especializada | BOE IV + portaal; subastasprocuradores.com | 0 [3] | S1, S50 |
| **C. Fiscaal of administratief** (AEAT, SUMA, gemeente, TGSS; patrimoniale verkoop door overheden; ORGA) | Het goed; bij invordering blijven eerdere lasten. Patrimonium: volgens pliego | U.R. Subastas AEAT, SUMA, Ayuntamiento, TGSS Dirección Provincial, GVA, Hacienda, ORGA | BOE V-B + portaal (SUB-AT, SUB-RC); TGSS eigen portaal en tablón; hisenda.gva.es | Xàbia 0; dichtstbij één AEAT-lot in Dénia (25 % aandeel) [3] | S7, S9, S32, S45 |
| **D. Faillissementsliquidatie** (TRLC) | Het goed, met doorhaling van pre-concursale lasten (art. 225), tenzij verkocht met behoud van de hypotheek (art. 212) | Administrador concursal / rechter (Sección Mercantil) | BOE-portaal (SUB-JC) of een gespecialiseerd portaal; RPC | Niet geteld [7] | S10, S40, S49 |
| **E. REO van bank of fonds** | Het goed, onderhands verkocht; de servicer is zelden eigenaar | Servihabitat, Solvia, Aliseda, Hipoges, Altamira/doValue, Diglo; eigenaar o.a. Sareb | Servicerportalen (handmatig); Idealista "de bancos" | 0 woningen, 2 unieke percelen (Sareb): Idealista "de bancos" 1 (111869151), Servihabitat Profesionales 2, waarvan perceel A waarschijnlijk hetzelfde object als 111869151 [1/3; koppeling 4] | S70–S75, S81 |
| **F. Vrijwillige bijzondere verkoop** | Het goed; voorwaarden volgens pliego of biedreglement | Notaris (vrijwillige veiling, LN 77); biedprocessen van servicers ("WOW! Venta Especial", POV) | Portaal; servicerportaal; Idealista | Idealista 111869151, waarschijnlijk hetzelfde object als perceel A [4]: "posible proceso competitivo … (POV)", "periodo de transparencia de 20 días naturales máximo" [1] | S5, S72, S81 |
| **G. Koop van een vordering** (NPL, cesión de remate) | Een vordering of een positie in een veiling, **niet het huis** | Aliseda (NPL), Diglo ("Venta de Créditos"), Hipoges; portefeuilles gaan naar institutionele kopers | Servicerportalen; aanbestedingen (TED) | Buiten fase A [4] | S75, S76, S77 |

### 2.2 Waar de signalen vandaan komen: geteste toegang per kanaal

| # | Kanaal | Wat het levert | Geteste toegang | Rechten en voorwaarden | Status (§7) | Toelichting bij de status |
|---|---|---|---|---|---|---|
| 1 | **BOE-sumario-API** `…/datosabiertos/api/boe/sumario/AAAAMMDD` | Dagelijks sumario. Sección IV = gerechtelijke veilingen per rechtbank (SUB-JA, SUB-JC). Sección V-B = AEAT, SUMA, TGSS-patrimonium, Hacienda | HTTP 200 in XML én JSON, mits met Accept-header; zonder header HTTP 400; vóór publicatie HTTP 404 (15-09, 03:00). Sumario 14-09: 211 items, waarvan 45 in Sección IV [3] | Hergebruik, ook commercieel, toegestaan met bronvermelding (licentie van 27-06-2024) [2]. Ratelimits ONBEKEND [7] | TECHNISCH ONDERZOEK NODIG | Rechten in orde; draait nog niet |
| 2 | BOE-RSS `rss/boe.php?s=4` en `?s=5B` | Dezelfde items | 14-09: 46 en 44 items, telkens inclusief één "Sumario"-item [3] | Idem | TECHNISCH ONDERZOEK NODIG | Terugval als regel 1 faalt |
| 3 | Aankondigingstekst `diario_boe/txt.php?id=BOE-B-…` | SUB-id, orgaan en `ds.php`-link; **geen plaats, geen object, geen bedrag** | Getest op 13 items [3] | boe.es-robots sluit `xml.php?` uit, `txt.php` zonder taalparameter niet [3] | TECHNISCH ONDERZOEK NODIG | Alleen SUB-id en orgaan uitlezen |
| 4 | **AEAT `bienes.js`** | Alle AEAT-vastgoedloten van het hele land met refCatastro, CRU, gps, valoracion, cargas, finSubasta, derecho en porcTitularidad | HTTP 200; versie "20260914 15:23:07"; 230 inmuebles; om 03:09 op 15-09 nog niet ververst [3] | "Licencia Creative Commons Atribución 4.0", bronvermelding verplicht [2]. Het pad is niet gedocumenteerd [3] | TECHNISCH ONDERZOEK NODIG | Door R08 "actief" genoemd; draait nog niet |
| 5 | AEAT "Suscripción a avisos de nuevos bienes" | Meldingen van nieuwe goederen | Achter authenticatie, niet getest [2] | Voorwaarden niet gelezen | TECHNISCH ONDERZOEK NODIG | Niet getest (authenticatie) |
| 6 | **Portal de Subastas BOE** (zoeken, detail, alerts) | Alle gerechtelijke, notariële, AEAT-, SUMA- en patrimoniale veilingen. Detailpagina: tasación, depósito, recht, situación posesoria, cargas, CRU, referencia catastral | Handmatig zoeken en detail bekeken op 14 en 15-09 [3]. Alerts na registratie, "únicamente … personas físicas", max. 50 abonnementen, melding als de biedperiode opent; de avisos "no tendrán carácter de notificación oficial" [2] | robots.txt `Disallow: /`, `X-Robots-Tag: noindex, nofollow` [3]. Voorwaarden voor geregistreerde gebruikers ONBEKEND [7]. De hergebruiklicentie is geen toestemming om robots.txt te negeren [2/4] | ALLEEN HANDMATIG | Plus e-mailalerts na registratie door Jan; automatische raadpleging pas na toestemming van de AEBOE (contract of toestemming nodig) |
| 7 | **TGSS** `w6.seg-social.es/subastas` + tablón op de sede | Executieveilingen van de Seguridad Social; filters Finca Urbana/Rústica en provincie; tablón met type "subasta de bienes inmuebles" | Pagina's bereikbaar (15-09); geen live telling gedaan [3/7] | Geen RSS of API; voorwaarden niet gelezen | ALLEEN HANDMATIG | — |
| 8 | **SUMA** (Diputación de Alicante) | Veilingen staan op het BOE-portaal (SUB-RC); suma.es toont alleen informatie en adjudicación directa | 17 SUB-RC-loten "próxima apertura" (14 en 15-09); 17 aparte V-B-aankondigingen (BOE-B-2026-29821 t/m 29837), gedateerd 29-06 of 22-07-2026 [3] | suma.es robots `Disallow: /` [3] | ALLEEN HANDMATIG | Geldt voor suma.es; de SUMA-veilingen zelf komen binnen via regel 1 (V-B-aankondigingen) en regel 6 (portaal, SUB-RC) |
| 9 | **Ajuntament de Xàbia** (tablón; perfil contratante op PLACSP) | Gemeentelijke edictos over invordering ("Recaptació en Via de Constrenyiment", met NIF's) | Eerste 10 publicaties (18-08 t/m 14-09) zonder subasta of enajenación [3]. R09 zag op 14-09 SUB-RC-veilingen van het Ayuntamiento in een zoekopdracht over alle statussen [3, niet herhaald] | Edictos bevatten NIF's: **niet opslaan** [2/4] | ALLEEN HANDMATIG | Geldt voor het tablón; voor de PLACSP-feed (M10) is eerst technisch onderzoek nodig |
| 10 | **Rechtbank Dénia** (Sección Civil TI Dénia, plazas 1–6) | Veilingen als Sección IV-item met titel "DENIA" | BOE-B-2022-17675 → SUB-JA-2022-195732; BOE-B-2026-4679 (17-02-2026) → SUB-JA-2026-257820 [2/3] | — | TECHNISCH ONDERZOEK NODIG | Geen eigen kanaal: het signaal komt via regel 1 (sumario, titel "DENIA"; status van regel 1), het detail via regel 6 (portaal, alleen handmatig) |
| 11 | **Registro Público Concursal** + Portal de liquidaciones | Edicten, doorzoekbaar per NIF of per dag (met captcha); liquidaties alleen van productie-eenheden van rechtspersonen | [2/3] | Hergebruik van persoonsgegevens en "indexaciones o robotizaciones" verboden [2] | ALLEEN HANDMATIG | Per concreet dossier |
| 12 | subastasprocuradores.com (CGPE) | Subasta, venta directa, unidad productiva; filter op provincie | [2/3] | Commissie 4 % op onroerend goed; of dat incl. of excl. btw is, is ONBEKEND. Robots sluit alleen `/error/` uit; geen automatiseringsclausule gevonden | TECHNISCH ONDERZOEK NODIG | — |
| 13 | eActivos | Concursale en (buiten)gerechtelijke online veilingen | [2] | "Se prohíbe el acceso … por medio de sistemas mecanizados" | ALLEEN HANDMATIG | Geautomatiseerd: niet gebruiken (gelijk aan het bronnenregister, R2-41) |
| 14 | GVA-patrimonium (hisenda.gva.es) | Verkoop van onroerend goed van de Generalitat | 53 inmuebles; pagina 1 zonder Alicante (14-09) [2/3] | Pliego DOGV 23-04-2025 | ALLEEN HANDMATIG | — |
| 15 | ATV (Agència Tributària Valenciana) | — | Geen veilingkanaal gevonden [7] | — | TECHNISCH ONDERZOEK NODIG | Geen veilingkanaal gevonden |
| 16 | BOP Alicante, TEJU, Patrimonio del Estado | Aankondigingen en edicten | [2/3] | TEJU: robots sluit `/edictos_judiciales/` uit | ALLEEN HANDMATIG | — |
| 17 | Idealista-assistent, filter "de bancos" | Bankobjecten, met `commercialName` via `property_detail` | Werkt (15-09). Het filter kan stil vervallen (altijd `summary` controleren) en de tool plaatst zoekopdrachten voor buurgemeenten soms in een straat in Jávea [3] | Gepland of systematisch gebruik niet bewezen; Idealista-voorwaarden (2020) verbieden "monitorizar" en "guardar" zonder schriftelijke toestemming [2] | ALLEEN HANDMATIG | Gepland of systematisch gebruik pas na schriftelijke toestemming van Idealista (contract of toestemming nodig) |
| 18 | Servicerportalen | Servihabitat (+ Profesionales), Solvia en Diglo zijn server-gerenderd; Sareb (403), Altamira (403/JavaScript), Bankinter (Cloudflare), Aliseda, Hipoges, EscogeCasa en Cimenta2 (alleen JavaScript) niet | [3] | Servihabitat: "Queda prohibida cualquier modalidad de explotación"; Solvia: "uso propio y personal"; Diglo: verbod op "extracción y/o reutilización" [1] | ALLEEN HANDMATIG | Alerts met een account van Jan |
| 19 | Eigen BP-feed (poort 3100) | 56 objecten "Javea", 224 totaal | Zelf gelezen op 15-09-2026: 0 treffers op banco, servihabitat, solvia, sareb, aliseda, diglo, altamira, haya, subasta, embargo, ocupad en nuda propiedad [3]. De feed heeft geen verkopersveld, dus "geen bankobjecten" is een gevolgtrekking [4] | Zie R16 §6.4 | CONTRACT OF TOESTEMMING NODIG | Status van de feed in het bronnenregister (R2-01); voor deze veilingstroom levert de feed geen bankobjecten |

### 2.3 Tellingen van 14 en 15-09-2026: de eerlijke oogst

| Selectie | 14-09-2026 | 15-09-2026 | Bron |
|---|---|---|---|
| Portaal, provincie Alicante, onroerend goed, **"celebrándose"** | 43 (40 gerechtelijk, 3 AEAT) | 41 (38 gerechtelijk, 3 AEAT; twee gesloten op 14-09) | S32 [3] |
| Idem, **"próxima apertura"** | 41 (21 gerechtelijk, 17 SUMA, 3 AEAT) | 41, zelfde verdeling | S32 [3] |
| Waarvan in Xàbia/Jávea (Javea, Jávea, Xàbia, Xabia, 0373x) | **0** | **0** | S32 [3] |
| Waarvan met een Dénia-orgaan als autoridad gestora | **0** | **0** | S32 [3] |
| Dichtstbijzijnde lot: SUB-AT-2026-26R2886001392 (Dénia, AEAT) | "25% PLENO DOMINIO" van een appartement; tasación en valor subasta 40.945,66 €; puja mínima 4.094,57 €; depósito 2.047,28 €; sluiting 21-09-2026 18:00; situación posesoria "No consta"; "HAY DERECHO DE RETRACTO" | Bevestigd | S33 [3] |
| Portaal, localidad "JAVEA", **alle statussen** (incl. afgesloten) | 278 resultaten: TI Dénia (plazas 1, 2, 5), Juzgado Mercantil 1 Alicante, AEAT (U.R. Valencia en Madrid), één notariële veiling, Ayuntamiento de Xàbia (SUB-RC) | Niet opnieuw geteld (robots) | S32 [3 volgens R09; niet te controleren, **[te verifiëren]**] |
| Historisch Jávea-voorbeeld SUB-JA-2026-257820 (TI Dénia) | Garage, "TRES/NOVENTA Y DOS PARTES INDIVISAS"; valor subasta 20.877,50 €; tasación **0,00 €**; depósito 1.043,87 € (= 5 %); sluiting 12-03-2026 19:42:11; posesoria "No consta" | Bevestigd; status "concluido … pendiente de finalización" | S35, S40 [3] |
| AEAT `bienes.js`, heel Spanje | 230 inmuebles; 52 daarvan aandelen onder 100 %; Alicante 3 (Orihuela 100 %, Dénia 25 %, Torrevieja 50 % nuda propiedad); Xàbia 0 | Idem (bestand nog niet ververst) | S43 [3] |
| SUMA-voorbeeld SUB-RC-2026-0026I20250184 | Tasación 93.007,47 €; valor subasta 69.162,35 €; puja mínima 34.581,18 € (50 %); depósito 3.458,12 € (5 %); cantidad reclamada 11.908,64 € | — | S34 [3] |
| Idealista "de bancos", Jávea | Woningen 0 | Woningen 0 · percelen 1 (111869151; 904.000 → 725.000 €; "Terreno urbanizable"; `commercialName` "Servihabitat") · bedrijfsruimtes 0. Dit perceel is waarschijnlijk hetzelfde object als perceel A hieronder en als kandidaat K10 (Idealista 107655781, deliverable 03 §2.6) [4] | S70, S81 [3] |
| Idealista "de bancos", Marina Alta | — | Woningen 1 (Calp, Banca March) · percelen 20 (17 via het Servihabitat-nummer, 3 via Banca March) | S70 [3] |
| Servihabitat (publiek), Alicante | — | Woningen 74 (Marina Alta 0) · terreinen 41 (Marina Alta 18, Jávea 0) · bedrijfsruimtes 9 | S71 [3] |
| Servihabitat Profesionales, Jávea | — | 2 percelen: A "Balcón al Mar", promotie 06124187 (16 fincas, 17.775 m², "TERRENO URBANO NO CONSOLIDADO", sector "PGOU UA BALCON AL MAR 1", aandeel 26,85 %, 725.000 € excl. belastingen en kosten; op Idealista eerder 904.000 €) en B "Toscal–Cap Martí" (4.622 m², "72,22%" van de UA, prijs op aanvraag, ingedeeld onder "huerta sur"). Beide: "Inmueble propiedad de Sociedad de Gestión de Activos Procedentes de la Reestructuración Bancaria" (Sareb). **Perceel A is waarschijnlijk hetzelfde object als Idealista 111869151 en kandidaat K10 (Idealista 107655781)**: prijs, eerdere prijs, 17.775 m², 16 eenheden, 3.554 m² en 26,85 % zijn gelijk; niet bevestigd met kadastrale referenties [4]. De planklasse is tegenstrijdig: Idealista "Terreno urbanizable", Servihabitat "TERRENO URBANO NO CONSOLIDADO, PGOU UA BALCON AL MAR 1" [7] | S72, S81 [1/3] |
| Solvia / Diglo, Jávea | — | Solvia: pagina bestaat, geen telling (waarschijnlijk 0 [4]) · Diglo: 0 | S74, S75 [3/4] |

**Wat dit betekent**

- **Actuele veilingen in Jávea: nul.** Zelfs het dichtstbijzijnde lot, in Dénia, valt meteen af: 25 % aandeel, bezetting onbekend en een retractrecht (§6) [3/4].
- **Geen basisfrequentie.** De 278 historische resultaten zeggen niet hoeveel veilingen er per jaar zijn: de periode is niet vastgesteld en de telling is niet te herhalen zonder het portaal te bevragen. Een handmatige nulmeting door Jan (§5) lost dat op [7].
- **Veel loten vallen direct af.** Het ene Jávea-voorbeeld dat bekeken is, is een onverdeeld aandeel van 3/92 met tasación 0,00 €, en valt dus op twee blokkades af [3]. Bij de AEAT is 23 % van de loten een aandeel (52 van 230) [5].
- **Bankaanbod betekent hier grond.** Beide Jávea-percelen zijn eengezinsgrond van Sareb. Volgens de criteria van Orden PJC/784/2025 (meergezinsgrond voor 30 of meer woningen) vallen ze buiten de overdracht aan Casa 47. Ze blijven dus in de verkoop, tegen de achtergrond van de liquidatie van Sareb eind 2027 [2/4; S22, S23, S77]. Dat is route B (deliverable 3), geen veilingroute. Perceel A staat daar als K10 (deliverable 03 §2.6), met dezelfde tegenstrijdige planklasse; welke klasse geldt, moet uit het kadaster en de gemeente blijken, niet uit een van de advertenties [4/7].
- **Veilingwaarde, schuld en marktwaarde zijn drie verschillende bedragen.** In het SUMA-voorbeeld is de gevorderde schuld (11.908,64 €) geen koopprijs, en de veilingwaarde ligt 23.845,12 € onder de tasación [5]. Of dat verschil uit eerdere lasten bestaat (RGR 97.6), moet in het anuncio staan **[te verifiëren]**.

### 2.4 Regels per type

#### 2.4.1 Gerechtelijke veiling (type A en B) — LEC

Bron: Ley 1/2000 (LEC), geconsolideerd, "Última actualización publicada el 28/02/2025". De veilingartikelen zijn gewijzigd "con efectos de 3 de abril de 2025" door art. 22 LO 1/2025 [S1, S2, S3; 2; gecontroleerd 14-09 (R09) en 15-09-2026 (verificatie)].

**Welk regime geldt?** DT 9ª.1 LO 1/2025: "Las previsiones recogidas por la presente ley serán aplicables exclusivamente a los procedimientos incoados con posterioridad a su entrada en vigor." Beide regimes bestaan daardoor nog jaren naast elkaar [2]. Of "incoado" slaat op de demanda ejecutiva, het despacho of de convocatoria, is **[te verifiëren, advocaat]**. Het jaartal in het expediente is alleen een eerste aanwijzing. Bij SUB-JA-2026-257820 (expediente uit 2018) wijzen 5 % waarborg en een sluitingstijd van 19:42:11 (verlenging) op het oude regime [4].

| Onderwerp | Oud regime | Nieuw regime | Artikel (citaat) |
|---|---|---|---|
| Waarborg onroerend goed | 5 % | 20 % van de waarde (art. 666), min. 1.000 €; de LAJ mag het percentage aanpassen | 669.1: "una cantidad equivalente al 20 por ciento del valor … o un mínimo de 1.000 euros" |
| Duur en verlenging | 20 dagen; sluit pas "una hora desde la realización de la última postura", max. 24 u | 20 kalenderdagen zonder verlenging; niet eindigen op za/zo, feestdag, 24-12 t/m 06-01 of in augustus | 649.1: "plazo improrrogable de veinte días naturales" |
| Zicht op biedingen | Hoogste bod zichtbaar | Geheim tot sluiting: onbekend hoogste bod ≠ geen biedingen | 648.6ª: "el portal no informará de la existencia o inexistencia de pujas ni de su cuantía" |
| Toewijzing | ≥ 70 % direct; lager: derde > 70 % binnen 10 dagen, anders schuldeiser of > 50 % | ≥ 70 %: decreto de dag na sluiting. < 70 %: ejecutado heeft 10 dagen voor een derde ≥ 60 %; daarna ≥ 50 % of een dekkend bedrag ≥ 40 %. Eigen woning: niet onder 70 %, of 60 % bij het volledige verschuldigde | 670.1, 670.3 |
| Lege veiling | Schuldeiser kon zich het goed laten toewijzen (50 %; eigen woning 70/60 %) | Schuldeiser kan dat niet meer; de ejecutado kan een persoon aanwijzen (≥ 50 % of dekkend ≥ 40 %) | 647.2: "Si no hubiera habido pujas, tampoco podrá solicitar la adjudicación de los bienes"; 671 |
| Restbetaling | 40 dagen | 20 dagen na sluiting (bij de < 70 %-route na goedkeuring, 670.4); opgeschort bij een testimonio voor hypotheekvestiging (670.6) | 670.1: "en el plazo de veinte días siguientes al cierre" |
| Verbeurte | Niet betalen: depósito kwijt, nieuwe veiling | Idem; ook bij niet tijdig aangetoonde vertegenwoordiging (3 dagen) | 653: "perderá el depósito que hubiera efectuado y se procederá a nueva subasta"; 647.1.1º |
| Cesión del remate | Alleen schuldeiser, met voorbehoud | Schuldeiser en latere schuldeisers van rechtswege; binnen 5 dagen na betaling | 647.3 |
| Certificación ouder dan 6 maanden | — | De LAJ "podrá solicitar, de oficio, nota simple registral actualizada": een bevoegdheid, geen plicht | 656.2 |

**Lasten.**
- Art. 666.1: goederen "saldrán a subasta por el valor que resulte de deducir de su avalúo … el importe de todas las cargas y derechos anteriores".
- Art. 639.3: de taxatie gebeurt "sin tener en cuenta … las cargas y gravámenes".
- Het edicto vermeldt dat eerdere lasten "continuarán subsistentes" en dat de bieder aanvaardt "quedar subrogado" (668). Art. 670.5 herhaalt de subrogatie.
- Latere lasten worden doorgehaald via het mandamiento (674). LH 134 noemt de doorhaling "de todas las cargas, gravámenes e inscripciones de terceros poseedores que sean posteriores a ellas, sin excepción" [S4, cons. 03-01-2025].
- Zijn de lasten gelijk aan of hoger dan de waarde, dan wordt de executie op dat goed geschorst (666.2) [2].
- Wettelijke *afecciones* (IBI-achterstand, bijdragen aan de VvE) zijn in geen enkel bronrapport gecontroleerd: **[te verifiëren]**.

**Bezit.**
- De publicatie "expresará, con el posible detalle, la situación posesoria del inmueble o que … se encuentra desocupado" (661.1). "No consta" komt in de praktijk voor [3].
- De ejecutante kan vooraf laten verklaren dat de bewoners geen recht hebben om te blijven (661.2).
- Bezichtiging kan via de rechtbank (669.3).
- Ontruiming binnen de executie kan tot "un año desde la adquisición" (675.2); daarna alleen via een aparte procedure [2].
- Of een huurcontract doorloopt (LAU): **[te verifiëren]**.

**Hypothecair specifiek.**
- Tipo "no podrá ser inferior, en ningún caso, al 75 por cien" van de taxatie (682.2.1º).
- Bij eigen woning plus *gran tenedor* is voorafgaande bemiddeling vereist (685.2; deels vernietigd door STC 26/2025).
- Concurso van de schuldenaar schorst de executie (691.5, 649.1).
- De schuldenaar kan tot de sluiting het achterstallige consigneren (693.3).
- Verzet schorst (695); tercería de dominio is mogelijk (696).
- De drempels van art. 24 Ley 5/2019 zijn niet gelezen [7].

**Fiscaal:** §2.5. **Beslisgrenzen:** §2.4.10.

#### 2.4.2 Notariële veiling (hypothecair buitengerechtelijk en vrijwillig)

- **Kanaal.** LN 73.1: "La subasta será electrónica y se llevará a cabo en el Portal de Subastas de la Agencia Estatal Boletín Oficial del Estado"; de notaris moet het RPC raadplegen (73.3) [S5, cons. 03-01-2025; 2].
- **Algemene notariële veiling.**
  - Waarborg 5 % ("consignado en forma electrónica el 5 por 100 del valor").
  - Minstens 20 dagen; het portaal "informará durante su celebración de la existencia y cuantía de las pujas" (75.1.3ª).
  - Restbetaling binnen 10 días hábiles (75.3).
  - Bij waardering door een perito geen biedingen onder de tipo (74.3); bij een vrijwillige veiling zijn de voorwaarden aanpasbaar in het pliego (77) [2].
- **Hypothecair (venta extrajudicial).**
  - LH 129.2.d: "Los tipos en la subasta y sus condiciones serán, en todo caso, los determinados por la Ley de Enjuiciamiento Civil."
  - LH 129.2.e laat de te consigneren bedragen over aan het Reglamento Hipotecario, waarvan art. 236-h nog een verouderde 30 %-regeling bevat.
  - De waarborg bij een notariële hypotheekveiling is daardoor niet eenduidig: **[te verifiëren]** [2/7; S4, S6].
- **Notariskosten.** Het tarief (Número 2) wordt berekend over de *precio de remate o adjudicación* [2; S25].

#### 2.4.3 AEAT en SUMA (fiscale invordering)

Bron: RGR (RD 939/2005), geconsolideerd 31-01-2024 (RD 117/2024, in werking 01-02-2024) [S7; 2; 15-09-2026].

| Onderwerp | Regel | Artikel (citaat) |
|---|---|---|
| Kanaal | Eén elektronische veiling op het BOE-portaal. De AEAT schrijft: "La subasta será única". Procedurefiche RF02 ("sobre cerrado", "segunda licitación") is verouderd [7] | 100.2: "La subasta de los bienes será única y se realizará por medios electrónicos en el Portal de Subastas…" |
| Aankondiging | Minstens 15 dagen na de kennisgevingen; opening ≥ 24 u na de BOE-aankondiging; het portaal vermeldt de lasten die blijven | 101.2–3, 101.4.e |
| Waarborg | 5 % van de tipo bij onroerend goed; 10 % alleen bij uitsluitend roerende loten | 103 bis.1: "Un depósito del 5 por ciento del tipo de subasta cuando los bienes … sean bienes inmuebles" |
| Duur en biedingen | 20 kalenderdagen; biedingen direct zichtbaar; puja mínima 10 % van de tipo, tenzij de lasten ≥ 25 % van de waardering zijn; verlenging tot 1 u na het laatste bod, max. 24 u | 104.2–3 |
| Toewijzing | Mesa binnen 15 kalenderdagen. ≥ 50 % van de tipo: toewijzing. < 50 %: de Mesa beslist "sin que exista precio mínimo de adjudicación". Tanteorechten van derden schorsen | 104 bis.1, 104 bis.3.a |
| Betaling | Binnen 15 dagen na kennisgeving; anders "perderá el importe del depósito" plus schadeaansprakelijkheid | 104 bis.3.b |
| Titel | Certificación del acta; op verzoek een escritura (binnen 5 dagen kiezen, 5 % extra storten); doorhaling van latere lasten. Zijn er geen ingeschreven titels, dan regelt de koper zelf de inschrijving | 104 bis.3.e, 111, 98.2 |
| Lasten | "Las cargas y gravámenes anteriores quedarán subsistentes sin aplicar a su extinción el precio del remate"; volgende veilingen van hetzelfde goed met coëfficiënt 0,8 en daarna 0,6 | 97.6, 97.7 |
| Cessie | Alleen voor bieders via *colaboración social*. AEAT: "no cabe la posibilidad de ceder el remate al tercero, tan solo se podría realizar una ulterior transmisión (con doble tributación)" | 103.3; S42 |
| Na de veiling | Adjudicación directa volgt niet automatisch: alleen na een concurso, bij bederfelijke goederen of om gemotiveerde redenen (termijn één maand). Niet-toegewezen goederen kunnen in een nieuwe procedure | 107; 104 bis.4 |
| Toewijzing aan de Hacienda | Max. 75 % van de oorspronkelijke tipo | LGT 172.2 [S8] |

**SUMA** volgt op het portaal dezelfde lijn [S47; 2]:
- waarborg "al menos del 5% del tipo de subasta";
- "veinte días naturales";
- de veiling "no se cerrará hasta que haya transcurrido una hora desde la realización de la última puja";
- betaling "15 días siguientes a la notificación".

Bij adjudicación directa is de waardering het minimum, met 5 % waarborg en een maand voor biedingen. Het SUMA-lot met een puja mínima van 50 % wijkt af van de algemene 10 %-regel. Dat past bij de uitzondering van RGR 104.3 als het verschil tussen tasación en veilingwaarde uit lasten bestaat [4, **te verifiëren**].

#### 2.4.4 TGSS (Seguridad Social)

Bron: RGRSS (RD 1415/2004), geconsolideerd 30-07-2026; art. 120.5 en 120.7 gewijzigd door RD 322/2024 [S9; 2; 15-09-2026].

- **Kanaal.** 117.1: "El anuncio de la subasta se publicará en el tablón de anuncios de la Seguridad Social situado en la sede electrónica…". Niet op het BOE-portaal. Offertetermijn minstens één maand (116).
- **Waarborg.** Per gesloten envelop een gecertificeerde cheque "por importe, en todo caso, del 25 por ciento del tipo de subasta" (117.2.e, 118.2); de bank blokkeert die ≥ 10 dagen. Mondeling bieden ter zitting vraagt 30 % (120.2), en mondelinge biedingen moeten ≥ 75 % van de tipo zijn (120.3).
- **Drempels.**
  - Eerste veiling: > 60 % van de tipo, of lager maar schulddekkend; bij onroerend goed nooit < 25 %.
  - Tweede veiling: > 50 %, of 25–50 % bij gemotiveerd besluit.
  - De schuldenaar mag binnen 3 werkdagen een derde aandragen die verbetert (120.5, 120.7).
- **Betaling.** "dentro de los cinco días hábiles siguientes al de dicha adjudicación" (117.2.g); niet betalen = verlies van de waarborg en aansprakelijkheid "de los mayores perjuicios" (120.10).
- **Voorkeursrecht.** De TGSS "podrá ejercitar derecho de tanteo … en el plazo máximo de 30 días" (121): winnen is pas na 30 dagen zeker.
- **Lasten en kosten.** Eerdere preferente lasten "quedarán subsistentes" (111.2). "Los gastos que origine la transmisión …, incluidos los fiscales y registrales, serán siempre a cargo del adjudicatario" (122). Cessie kan binnen 5 werkdagen via een gezamenlijke comparecencia (120.9).
- **Eigen vastgoed van de TGSS.** Dit is iets anders: verkoop van eigen patrimonium, aangekondigd in BOE V-B, met een e-maildienst "Información venta de inmuebles" [3; S46].

#### 2.4.5 Patrimoniale verkoop door overheden en ORGA (type C, geen invordering)

- **Gemeente Xàbia.** TRRL art. 80: "Las enajenaciones de bienes patrimoniales habrán de realizarse por subasta pública. Se exceptúa el caso de enajenación mediante permuta" [S11; 2]. RBEL 118: "Será requisito previo a toda venta o permuta de bienes patrimoniales la valoración técnica de los mismos que acredite de modo fehaciente su justiprecio"; boven 25 % van de gewone begrotingsmiddelen is autorisatie van de Comunidad Autónoma nodig (109) [S12; 2]. Op het tablón (eerste 10 publicaties) stond op 15-09 geen verkoop [3]. Of Xàbia patrimoniale verkopen op PLACSP publiceert: **[te verifiëren]**.
- **Generalitat.** hisenda.gva.es, met het algemene pliego in DOGV 23-04-2025 [S48; 2]. Lasten, betaling en bezit volgen uit het pliego per verkoop [4].
- **ORGA** (in beslag genomen goederen uit strafzaken, RD 948/2015). Veilt op het BOE-portaal met eigen regels: betaling binnen "cuarenta días hábiles" voor onroerend goed, waarborg volgens de ORGA [S54; 2]. Deze pdf is **niet** bruikbaar als bron voor LEC-veilingen.

#### 2.4.6 Faillissementsliquidatie (type D) — TRLC

Bron: TRLC (RDL 1/2020), geconsolideerd 03-01-2025 (hervorming Ley 16/2022, in werking 26-09-2022) [S10; 2; 15-09-2026].

- **Verkoopwijze.**
  - Het "plan de liquidación" bestaat niet meer: art. 416 t/m 420 zijn "(Suprimido)". De rechter stelt *reglas especiales de liquidación* vast (415).
  - Goederen boven 5 % van de inventaris gaan per elektronische veiling, "bien en el portal de subastas de la Agencia Estatal Boletín Oficial del Estado, bien en cualquier otro portal electrónico especializado en la liquidación de activos", "salvo que el juez, al establecer las reglas especiales de liquidación, hubiera decidido otra cosa" (423.1).
  - Losse bezwaarde goederen kunnen ook direct worden verkocht, onder de voorwaarden van art. 210. Art. 216 gaat over ondernemingen en productie-eenheden.
  - Het portal de liquidaciones (415 bis) geldt alleen voor rechtspersonen en toonde alleen productie-eenheden [2/3].
- **Waarborg en termijnen.** Niet wettelijk vastgelegd; ze volgen uit de reglas, het platform en de veiling [2]. subastasprocuradores.com rekent 4 % commissie op onroerend goed [2].
- **Lasten.** Art. 225: "se acordará la cancelación de todas las cargas anteriores al concurso constituidas a favor de créditos concursales. Los gastos de la cancelación serán a cargo del adquirente." Dat geldt niet bij verkoop met behoud van de hypotheek en subrogatie van de koper (212) [2].
- **Procedurerisico.** Vanaf de faillietverklaring worden executies op goederen die nodig zijn voor de activiteit geschorst, "aunque ya estuviesen publicados los anuncios de subasta" (145) [2].
- **Toegang.** Het RPC is alleen handmatig raadpleegbaar; robotisering en hergebruik van persoonsgegevens zijn verboden [S49; 2].

#### 2.4.7 REO van bank of fonds (type E)

- **Verkoop.** Onderhands, via servicers; de servicer is zelden eigenaar. Beide Jávea-percelen staan te koop via Servihabitat Profesionales. Daar staat: "Los inmuebles no reúnen los requisitos técnicos o documentales para ser comprados por consumidores y usuarios" en "Los precios no incluyen impuestos y gastos a cargo del comprador" [S72; 1].
- **Bezitsrisico.** Er zijn aparte categorieën "Viviendas sin posesión" en "obra parada" [S71; 1/3].
- **Sareb.**
  - Mag hooguit 15 jaar bestaan (RD 1559/2012 art. 16.3: "no podrá ser superior a 15 años") en gaat eind 2027 in *liquidación mercantil*; de afwikkeling loopt daarna door [2/1 (pers); S22, S77].
  - Het nieuwe servicercontract ligt stil door een bezwaar van Hipoges tegen Lot A (sinds 03-08-2026; afloop onbekend) [1 (pers)/7; S78].
- **Toegang.** Geen lees-API of feed. Alerts werken alleen met een account, en de voorwaarden verbieden extractie [1]. Status: ALLEEN HANDMATIG.
- **Fiscaal.** De verkoper is ondernemer. Een tweede levering van een woning is btw-vrij, dus ITP 9 %; bij afstand van de vrijstelling btw 10 % (woning) plus AJD 2 %. Grond die "urbanizado o en curso de urbanización" is, valt niet onder de vrijstelling: btw 21 % plus AJD 1,4 %. Servihabitat noemt beide percelen "sujeta y no exenta de IVA" [S17, S72; 2/1]. Per deal **[te verifiëren, gestor]**.
- **Beslisgrenzen.**
  - "sin posesión";
  - onverdeeld aandeel (perceel B: 72,22 %);
  - planologische status tegenstrijdig (perceel A: "TERRENO URBANO NO CONSOLIDADO, PGOU UA BALCON AL MAR 1" bij Servihabitat, "Terreno urbanizable" bij Idealista 107655781 en 111869151, die waarschijnlijk hetzelfde object zijn [4]) [7];
  - geen nota simple.

  Grondkandidaten gaan eerst door deliverable 3 (percelen).

#### 2.4.8 Vrijwillige bijzondere verkoop (type F)

- **Vrijwillige notariële veiling.** Via het portaal; voorwaarden in het pliego (LN 77) [2].
- **Servihabitat "WOW! Venta Especial".** Online biedproces met tijdklok en borg, via een samenwerkend makelaar (*API colaborador*) [S71; 1].
- **POV bij bankgrond.** Idealista 111869151, waarschijnlijk hetzelfde object als perceel A [4]: "posible proceso competitivo o … (POV)" met een "periodo de transparencia de 20 días naturales máximo" [S70, S81; 1].
- **Wat het niet is.** Geen executie: er is geen certificación in een procedure, geen LEC-bescherming van de koper en geen doorhaling van lasten via een mandamiento. Due diligence verloopt als bij een gewone koop (nota simple, catastro, urbanisme) [4].
- **Beslisgrens.** Biedregels, borg en termijnen staan alleen in het reglement van de verkoper. Zonder dat reglement geen bod [4].

#### 2.4.9 Koop van een vordering (type G) — buiten fase A

- **Wat je koopt.** Een vordering of een veilingpositie, geen eigendom [4, op basis van 2].
  - LEC 647.3: de ejecutante en latere schuldeisers hebben een cessierecht van rechtswege.
  - TRLC: de bevoorrechte schuldeiser ontvangt tot zijn oorspronkelijke vordering (213, 430) en kan zich bij een lege veiling het goed laten toewijzen (423 bis). De executie kan geschorst zijn (145).
  - AEAT: cessie alleen via *colaboración social* (RGR 103.3). TGSS: via comparecencia (RGRSS 120.9) [2].
- **Kanalen.**
  - Diglo biedt "comprar cesión de créditos, venta en subastas y cesiones de remates con garantía de activos inmobiliarios" [S75; 1].
  - De sitemap-loans.xml van Aliseda telt 6.432 NPL-URL's [S76; 3]; die pagina's kunnen tot schuldenaars herleidbaar zijn.
  - Portefeuilles worden via adviseurs en aanbestedingen aan institutionele partijen verkocht (TED 140491-2026) [2/4].
- **Besluit.** NIET GEBRUIKEN in fase A. Tussenpersonen zonder aangetoond mandaat van een bank of servicer: NIET GEBRUIKEN (R10 §4.17). De fiscale behandeling van cessies is niet onderzocht [7].

#### 2.4.10 Overzicht per type: waarborg, termijnen, lasten, bezit, fiscaal, beslisgrenzen

| Type | Waarborg | Termijnen | Lasten die blijven | Bezitsrisico | Fiscaal bij toewijzing | Harde beslisgrenzen |
|---|---|---|---|---|---|---|
| A/B gerechtelijk, **nieuw** regime | 20 % (min. 1.000 €; LAJ kan afwijken; portaalveld leidend) | 20 kalenderdagen zonder verlenging; betalen 20 dagen na sluiting; vertegenwoordiging binnen 3 dagen | Eerdere (666, 668, 670.5); latere doorgehaald (674, LH 134) | "No consta" komt voor; ontruiming binnen 1 jaar (675.2) | ITP 9/11 % over max(valor de referencia, remate); of btw bij ondernemer-ejecutado | Regime onbekend; recht ≠ 100 % pleno dominio; certificación ontbreekt of oud; lasten niet gekwantificeerd; tasación 0; bezit onduidelijk; betaling niet gefinancierd; verzet/tercería/concurso |
| A/B gerechtelijk, **oud** regime | 5 % | 20 dagen + verlenging tot 24 u; 40 dagen betalen | Idem | Idem | Idem | Idem |
| Notarieel (LN) | 5 %; bij hypothecair **[te verifiëren]** | ≥ 20 dagen; 10 werkdagen betalen | Hypothecair: LEC-regels via LH 129 | Idem | Idem | Idem + pliego ontbreekt |
| AEAT / SUMA | 5 % van de tipo | 20 dagen, +1 u per laat bod (max. 24 u); Mesa ≤ 15 dagen; betalen 15 dagen na kennisgeving | Eerdere (RGR 97.6); latere doorgehaald (111) | Portaalveld; vaak "No consta" [3] | Idem; tipo excl. indirecte belastingen (101.4.b) | Idem + tanteo of retracto van derden open |
| TGSS | 25 % cheque (30 % mondeling) | Offertes ≥ 1 maand; 3 werkdagen verbeteringsrecht; betalen 5 werkdagen; tanteo 30 dagen | Eerdere preferente (111.2) | Anuncio; inzage títulos bij Dirección Provincial | Alle transmissiekosten voor de koper (122) | Idem + cheque niet tijdig; tanteo-periode |
| Patrimonium (gemeente, GVA, Estado) | Volgens pliego | Volgens pliego | Volgens pliego | Volgens pliego | ITP of btw volgens de verkoper **[te verifiëren]** | Pliego of valoración técnica ontbreekt |
| D faillissement | Per veiling/platform | Per reglas especiales | Pre-concursale doorgehaald op kosten koper (225), behalve bij 212 | Per dossier | Idem **[te verifiëren]** | Reglas onbekend; verkoop met behoud van hypotheek niet doorgerekend |
| E REO | Volgens servicer (POV/borg) | Transparantieperiode tot 20 dagen (Idealista 111869151, waarschijnlijk perceel A) | Alles volgens nota simple | "sin posesión"-categorie | ITP 9 % of btw 10/21 % + AJD | Geen bezit; aandeel; planologie tegenstrijdig |
| F vrijwillig | Reglement | Reglement | Nota simple | Nota simple | Als gewone koop | Reglement ontbreekt |
| G vordering | — | — | Niet van toepassing: geen eigendom | — | Niet onderzocht | Altijd stop in fase A |

### 2.5 Fiscale behandeling bij toewijzing

| Situatie | Regel | Bron | Type |
|---|---|---|---|
| Tarief ITP | "El 9 % en las adquisiciones de inmuebles"; 11 % over de hele grondslag boven 1.000.000 €; voor belastbare feiten vanaf 01-06-2026. ATV-code **TS0** voor veilingen = 9 % | Ley 13/1997 CV art. 13 (cons. 02-07-2026); Ley 5/2025 art. 33; ATV | 2 |
| Grondslag | Art. 10.2 TRLITPAJD: valor de referencia, tenzij prijs of aangegeven waarde hoger. RITP 39 (veilingprijs) is deels vernietigd door TS 3-11-1997. DGT (V0453-22, via Cuatrecasas) en TSXG (CGPJ 04-05-2026): de valor de referencia gaat voor als die hoger is. **Rekenregel: 9/11 % × max(valor de referencia, remate).** ATV-praktijk **[te verifiëren]** | S13, S14, S61, S62 | 2/1/7 |
| Gevolg | Een korting in de veiling onder de valor de referencia verlaagt de ITP niet | Afgeleid | 4 |
| Bonificatie art. 14 bis.Tres (50/70 %) | Niet bij "adjudicaciones de inmuebles en subasta pública" | S15 | 2 |
| Ejecutado is ondernemer | Btw kan ITP vervangen (eerste levering, bouwgrond, afstand van vrijstelling). Woning 10 %, ook bij afstand (LIVA 91.Uno.1.7º); grond en bedrijfsruimte 21 %; AJD 2 % bij afstand. De tipo is exclusief indirecte belastingen (RGR 101.4.b). RGRSS 122.3 staat een ondernemer-koper toe de factuur uit te reiken en de vrijstelling af te wijzen | S17, S7, S9 | 2; toepassing **[te verifiëren]** |
| AJD | Alleen bij een notariële eerste kopie. Het testimonio van het decreto (LEC 673) en de certificación del acta (RGR 104 bis.3.e; RGRSS 122.1) zijn geen notariële akte, dus AJD daarover is **[te verifiëren]**. Bij keuze voor een escritura (AEAT: +5 % binnen 5 dagen) ontstaat wel een notarieel document | S13, S7, S9 | 2/4 |
| Plusvalía (IIVTNU) | Belastingplichtig is de vervreemder (106.1.b). Is die "persona física no residente en España", dan is de koper "sujeto pasivo sustituto" (106.2). Geen heffing als de belanghebbende aantoont dat er géén waardestijging was (104.5). Vrijstelling voor de eigen woning bij hypothecaire executie, onder voorwaarden (105.1.c). Tarief Xàbia 2026 ONBEKEND (2021: 30 %; wettelijk max. 30 %): model rekent 30 % | S16, S64 | 2/7 |
| IRNR | Koper houdt 3 % in bij een niet-residente verkoper (art. 25.2 LIRNR). Of dat ook bij gerechtelijke of administratieve toewijzing geldt: **[te verifiëren]** | S18 | 2/7 |
| Doorhaling en inschrijving | TRLC 225: koper. RGRSS 122: "incluidos los fiscales y registrales … a cargo del adjudicatario". LEC: niet geregeld, model rekent de koper | S10, S9 | 2/4 |
| Notaris en register | Kleine posten volgens de degressieve schaal: bij 500.000 € ongeveer 483 € + 262 € (excl. btw) | S25, S26 | 5 |
| Holding Xàbia | IBI urbana 0,83 % (2026) van de kadastrale waarde | S64 | 2 |

### 2.6 Waarborgsom als liquiditeitsbeslag (§19)

De waarborg is geen kostenpost. Wie wint, ziet de waarborg als "parte del precio"; wie verliest, krijgt hem terug (LEC 652.1; RGR 103 bis) [2]. Model uit R09 §8 [5]: `D = p × T`, beslag = D × looptijd, risicopost = kans op verbeurte × D.

| Procedure | Waarborg per 100.000 € veilingwaarde of tipo [5] | Terug bij verlies | Vast bij reserva de postura | Verbeurte alleen bij |
|---|---|---|---|---|
| LEC nieuw | 20.000 € | Direct na sluiting (652.1) | Tot de winnaar heeft betaald (670.8): weken tot maanden | Niet betalen binnen 20 dagen; vertegenwoordiging niet binnen 3 dagen |
| LEC oud | 5.000 € | Idem | Idem | Niet betalen binnen 40 dagen |
| Notarieel (LN) | 5.000 € (hypothecair **[te verifiëren]**) | Portaal | Portaal | Niet betalen binnen 10 werkdagen |
| AEAT / SUMA | 5.000 €; een bod dat niet hoger is dan het hoogste bod wordt automatisch gereserveerd (103 bis.3) | Na de biedperiode | Mesa ≤ 15 dagen + betaling ≤ 15 dagen na kennisgeving, orde 1–2 maanden [4] | Niet betalen: depósito naar de schuld + schadeaansprakelijkheid |
| TGSS | 25.000 € per cheque (30.000 € mondeling) | Ter zitting (120.8); cheque ≥ 10 dagen geblokkeerd (118.2) | n.v.t. | Niet betalen binnen 5 werkdagen + schade; na betaling nog 30 dagen tanteo (prijs komt dan terug) |

**Praktische regels** [2, uit S30 en S42]:
- Storten gaat alleen via het portaal en de betaalpassarelle van de AEAT, vanaf een rekening bij een *entidad colaboradora* op naam van de bieder; rekeningen met meervoudige handtekening werken niet. Het portaal adviseert meer dan één dag vóór sluiting te storten.
- Wie voor een vennootschap biedt, meldt dat bij het depósito en bij het bod.

**Beleid (voorstel, type 4):** de restbetaling is gefinancierd vóór het eerste bod, en er is een plafond voor de som van gelijktijdige waarborgen.

### 2.7 Noodzakelijke documenten vóór een biedingsvoorstel

| Document | Type | Waar | Grondslag | Zonder dit document |
|---|---|---|---|---|
| Edicto met algemene en bijzondere voorwaarden | A, B, notarieel | Portaal (deels na inloggen) | LEC 646.2, 668 | Geen dossier |
| **Certificación de dominio y cargas** (+ datum); bij hypotheek met letterlijke inschrijving | A, B, C | Portaal/edicto | LEC 656, 668.2, 688; RGR 97.5; RGRSS 111.2 | Blokkade |
| Geactualiseerde nota simple bij certificación > 6 maanden | A, B | Portaal (656.2) of eigen aanvraag (RH 332.3, legitiem belang) | LEC 656.2 | Blokkade (TREE-beleid, geen wettelijke plicht) |
| Antwoorden over het actuele saldo van eerdere lasten (dagrente, vervaldatum) | A, B | Edicto (minoración de cargas) | LEC 657, 668.2 | Blokkade |
| Avalúo/tasación incl. extrajudicieel rapport; bij hypotheek de tasación uit de akte | A, B, C | Portaal (tasación-veld + bijlage) | LEC 638–639, 668.2, 682.2; RGR 97 | Blokkade bij 0,00 € of ontbrekend |
| Registerinformatie via het portaal, bijgewerkt tot het einde van de veiling | A, B, notarieel | Portaal, alleen ingelogd | LEC 667.2; LN 74.1 | Handmatig vervangen door nota simple |
| Situación posesoria, vivienda habitual, verklaring 661.2 | A, B | Portaal-tabblad Bienes | LEC 661, 668.2 | Blokkade bij "No consta" zonder ontruimingsperspectief |
| Anuncio met tipo, depósito en lasten die blijven | C (AEAT/SUMA/TGSS) | Portaal; TGSS-tablón | RGR 101.4; RGRSS 117.2.a–b | Geen dossier |
| Pliego de condiciones | Notarieel vrijwillig; patrimonium | Autoriteit | LN 77; pliego DOGV 23-04-2025 | Geen bod |
| Reglas especiales de liquidación + platformnormen | D | Rechtbank/AC; platform | TRLC 415, 423 | Geen bod |
| Kadastrale gegevens, geometrie, valor de referencia | Alle | Sede Catastro (valor de referencia alleen na authenticatie) | TRLITPAJD 10.2; deliverable 3 | Geen fiscale berekening, geen objectidentiteit |
| Urbanistische status | Alle (vooral grond) | Gemeente; deliverable 3 | LEC 668.3 ("si ello fuera posible") | Geen biedingsvoorstel voor grond |
| Advocaatverklaring (bewijstype 6) | Alle | Advocaat | Masterprompt §19 | Geen biedingsvoorstel |

### 2.8 Veilingdossier — invulsjabloon (§19)

Eén dossier per kandidaat. "Portaal" = detailpagina op subastas.boe.es (handmatig tot de AEBOE toestemming geeft). Velden met [afgeschermd] staan alleen in het afgeschermde dossierdeel (§2.10).

| # | Veld | Vorm | Bron van de waarde | Stopregel |
|---|---|---|---|---|
| **A. Bron en procedure** |||||
| 1 | Officiële bron | URL `ds.php?id=SUB-…`, BOE-B-nummer, `bienes.js`-record of TGSS-tablón | Portaal; sumario-API; `bienes.js` | Geen officieel ID → geen dossier |
| 2 | Veiling-ID en lot | SUB-JA / SUB-JC / SUB-AT / SUB-RC / notarieel / G + lotnummer | Portaal "Identificador", "Lotes" | — |
| 3 | Zaaknummer | Cuenta expediente, expediente nº/jaar | Portaal | Jaartal < 2025 bij gerechtelijke veiling → oud regime aannemen tot het edicto anders zegt |
| 4 | Beherende instantie | Autoridad gestora (oude en nieuwe benaming, Denia/Dénia) | Portaal "Autoridad gestora" | Onbekend of niet-officieel → NIET GEBRUIKEN |
| 5 | Proceduretype | A–G uit §2.1 + subkanaal | Portaal "Tipo de subasta"; anuncio | Onbekend → geen bod |
| 6 | Toepasselijk regime | LEC oud/nieuw · LN · LH 129 · RGR · RGRSS · TRLC-reglas · pliego | Edicto, decreto de convocatoria, datum inleiding (DT 9ª LO 1/2025) | Niet vast te stellen → **blokkade** |
| **B. Object** |||||
| 7 | Omschrijving, adres, postcode, gemeente | Postcode als 5 tekens (3730 → 03730); gemeente genormaliseerd (Xàbia/Jávea/Javea/Xabia → één code) | Portaal "Bienes"; `bienes.js` (cp numeriek, municipioCod) | — |
| 8 | Referencia catastral | 20 tekens | Portaal; `bienes.js` refCatastro; Catastro | Geen refcat én geen eenduidige omschrijving → geen bod |
| 9 | IDUFIR/CRU, finca registral | — | Portaal; certificación | — |
| 10 | Coördinaten | lat/long + bron + nauwkeurigheid | `bienes.js` (ontbreekt bij 29 van 230); Catastro | — |
| 11 | Koppeling perceel | Link naar perceeldossier | Deliverable 3 | Grond zonder perceelanalyse → geen bod |
| **C. Recht en documenten** |||||
| 12 | Aangeboden recht | 100 % pleno dominio / x % pleno dominio / nuda propiedad / usufructo / vordering / ander | Portaal "derecho subastado"; `bienes.js` derecho + porcTitularidad; certificación | Alles behalve 100 % pleno dominio → **blokkade** |
| 13 | Documenten en versies | Per document: soort, datum, versie, hash, bron-URL | Portaal (na inloggen), edicto, pliego | Certificación ontbreekt of > 6 maanden zonder actualisatie → **blokkade** |
| **D. Data** |||||
| 14 | Publicatie BOE | Datum | Sumario-API | — |
| 15 | Opening / sluiting | Datum en tijd; verlengingsregel per regime | Portaal "Fecha de inicio/conclusión"; LEC 649.1; RGR 104.3 | Alleen uit portaal of edicto, nooit uit een alertmail |
| 16 | Afgeleide deadlines | Depósito-streefdatum, go/no-go advocaat, vertegenwoordiging (3 dagen), restbetaling, tanteo-einde, ontruimingsvenster (1 jaar) | Rekenregels §2.9 | Betaling niet gefinancierd → geen bod |
| **E. Geld en bieden** |||||
| 17 | Valor subasta / tipo | € | Portaal | — |
| 18 | Tasación + datum + taxateur | € | Portaal; taxatierapport | 0,00 € of ontbrekend → **blokkade** |
| 19 | Puja mínima, tramos | € | Portaal | — |
| 20 | Importe del depósito | € + controle tegen het wettelijke percentage | Portaal; LEC 669.1, RGR 103 bis, RGRSS 117 | Afwijking → navragen bij de autoridad gestora |
| 21 | Cantidad reclamada [afgeschermd] | € | Portaal | Nooit als koopprijs gebruiken |
| 22 | Biedinformatie | Zichtbaar ja/nee; hoogste bod (alleen AEAT/notarieel) | Portaal "Pujas" | LEC nieuw: onbekend ≠ geen biedingen |
| 23 | Biedvoorwaarden | Reserva de postura, cesión, tanteo/retracto ("HAY DERECHO DE RETRACTO") | Portaal; edicto; RGR 104 bis.3.a; RGRSS 121 | Open voorkeursrecht → geen definitief oordeel |
| **F. Status** |||||
| 24 | Procedurestatus + historie | PU / EJ / SU / CA / PC / FS met tijdstempels | Portaal; alerts (alleen signaal) | SU, CA of concurso gemeld → **blokkade** |
| **G. Bezit** |||||
| 25 | Situación posesoria | Tekst portaal; verklaring 661.2 ja/nee | Portaal; edicto | "No consta" of bezetting zonder titel → **blokkade** tenzij ontruimingsscenario is doorgerekend en juridisch beoordeeld |
| 26 | Vivienda habitual [afgeschermd] | Sí / No | Portaal | Eigen woning: drempels 70/60 % en extra bescherming meenemen |
| 27 | Visitable / bezichtiging | Ja/nee; verzoek via rechtbank (669.3), alleen door Jan | Portaal | — |
| **H. Lasten** |||||
| 28 | Eerdere lasten | Per last: rang, houder (alleen rechtspersoon), saldo, dagrente, datum | Certificación; antwoorden 657; portaal "Cargas" | Niet gekwantificeerd → **blokkade** |
| 29 | Latere lasten | Worden doorgehaald: grondslag vermelden | LEC 674, LH 134, RGR 111, TRLC 225 | — |
| 30 | Afecciones (IBI, VvE) | € of ONBEKEND | Gemeente, VvE **[te verifiëren]** | ONBEKEND → risicopost |
| **I. Fiscaal en kosten** |||||
| 31 | Belastingregime | ITP / btw + AJD | Advocaat of gestor; §2.5 | Onbekend → rekenen met de duurste variant |
| 32 | Valor de referencia | € + datum | Sede Catastro (authenticatie) | Ontbreekt → geen fiscale berekening |
| 33 | Plusvalía-substitutie [afgeschermd] | Vervreemder niet-residente natuurlijke persoon: ja / nee / onbekend (alleen deze vlag, geen naam) | Advocaat | Onbekend → rekenen alsof het wel zo is |
| 34 | Kosten na toewijzing | Doorhaling, inschrijving, escritura (+5 % AEAT), ontruiming, platformcommissie | §2.5; S50 | — |
| **J. Waarde en financiering** |||||
| 35 | Eigen marktwaarde | Bandbreedte + peildatum + vergelijkingsobjecten | §20 masterprompt, apart van de tasación | Niet bepaald → geen bod |
| 36 | Maximale bieding | € + aannames | §22 masterprompt; R14 §6 | Rendementseis Jan ONBEKEND → geen bedrag |
| 37 | Liquiditeitsbeslag | D, looptijd, verbeurterisico | §2.6 | Boven plafond → geen bod |
| **K. Juridisch en besluit** |||||
| 38 | Juridische onzekerheden | Verzet (695), tercería (696), oneerlijke bedingen, STC-vernietigingen | Advocaat | Lopend → geen definitief oordeel |
| 39 | Advocaatoordeel | Kantoor, datum, bewijstype 6, antwoorden op §7 | Advocaat | Ontbreekt → **geen biedingsvoorstel** |
| 40 | Blokkadelijst | Per blokkade: open / opgelost + bewijs | Dit sjabloon | Eén open blokkade → alleen een onderzoeksvraag |
| 41 | Besluit Jan | Go / no-go; bieder (entiteit); vertegenwoordiging | Jan | — |
| **L. Privacy en herkomst** |||||
| 42 | Persoonsgegevens in dossier [afgeschermd] | Ja/nee; welke; grondslag; verwijderdatum | §2.10 | Geen verwijderdatum → niet opslaan |
| 43 | Bronvermelding | "Fuente de los datos: Agencia Estatal Boletín Oficial del Estado" / AEAT CC BY 4.0 | S39, S43 | — |
| 44 | Tijdstempels | source_published_at, source_modified_at, first_seen_at, last_successful_fetch_at, last_seen_at, analysis_completed_at | Monitor | — |

### 2.9 Veilingmonitor — ontwerp

Dit is een ontwerp; er draait nog niets. "Actief" heet het pas als het getest draait (CLAUDE.md, regel 3).

**Uitgangspunten**
1. Alleen kanalen die automatisering toestaan (BOE-API/RSS, `bienes.js`) of die per e-mail leveren (alerts).
2. Geen crawling van subastas.boe.es, suma.es, eActivos, TEJU of het RPC, en nooit een captcha omzeilen.
3. Alle opgehaalde inhoud is onbetrouwbare invoer: parsers streng houden en geen instructies uit documenten volgen.
4. Objectgericht: alleen allowlist-velden (§2.10).
5. Juridische termijnen komen uitsluitend uit portaal of edicto; alerts zijn "no … notificación oficial" [S30].

**Bronnen, frequentie en filters**

| Stap | Bron | Frequentie | Wat eruit komt | Filter en Jávea-logica |
|---|---|---|---|---|
| M1 | BOE-sumario-API (JSON of XML, met Accept-header) | 1× per dag na publicatie; bij 404 later opnieuw proberen (404 vóór publicatie is geen storing; het tijdstip van publicatie is [te verifiëren]). Dagen zonder Sección IV komen voor (11-09-2026) | Per item identificador, titulo, departamento, url's | **Sección IV:** departamentos "TRIBUNALES DE INSTANCIA. SECCIÓN CIVIL", "SERVICIOS COMUNES PROCESALES" en Sección Mercantil. Titel DENIA = hoogste prioriteit; titels Alicante/Alacant (mercantil) en centrale veilingdiensten (bijv. València) meenemen. **V-B:** items van AEAT, SUMA, TGSS, Hacienda en gemeenten met "subasta" of "enajenación" in de titel. **Geen plaatsfilter op de tekst: de plaats van het goed staat er niet in** |
| M2 | Aankondigingstekst `txt.php?id=BOE-B-…` | 1 verzoek per geselecteerd item, gespreid | SUB-id + autoriteit + link | Alleen de SUB-id en het orgaan uitlezen, niet de hele tekst opslaan |
| M3 | BOE-RSS s=4 / s=5B | Alleen als M1 faalt | Zelfde items | Idem |
| M4 | AEAT `bienes.js` | 1× per dag na ca. 16:00 (versie 15:23 gezien); diff met gisteren | Volledige AEAT-lijst | codProvincia 3; cp genormaliseerd naar 03730/03737/03738 (volledigheid [te verifiëren]); municipioCod Xàbia [te verifiëren; Dénia = 3063 gezien]; gps binnen Xàbia waar aanwezig; derecho ≠ 1 of porcTitularidad < 100 → direct gemarkeerd als blokkade; bronvermelding CC BY 4.0. Structuurwijziging → BRON NIET BEREIKBAAR |
| M5 | Portaalalerts (account Jan; ≤ 50 abonnementen) | Per e-mail | Nieuwe veilingen en statuswijzigingen die aan de criteria voldoen (bij opening van de biedperiode) | Voorstel: onroerend goed × localidad "Xàbia", "Jávea", "Javea", "Xabia" × postcodes 03730/03737/03738; buurgemeenten Dénia, Benitachell, Teulada (Moraira), Benissa, Calp, Gata de Gorgos, Pedreguer; autoridad bevat "Dénia/Denia". Inlezen van de mailbox pas na lezing van de portaalvoorwaarden **[te verifiëren]**; tot dan leest Jan of een medewerker zelf |
| M6 | Handmatige detailcontrole per kandidaat uit M1, M4 of M5 | Binnen 1 werkdag na signaal | Localidad, Bienes, depósito, sluiting, documenten (ingelogd) | Alleen Jan of een medewerker; tot AEBOE-toestemming geen scripts op het portaal |
| M7 | Handmatige checklist | Wekelijks: TGSS-portaal en tablón (Alicante), tablón Xàbia, BOP Alicante, subastasprocuradores.com, eActivos. Maandelijks: GVA-patrimonium, SUMA adjudicación directa | Kanalen zonder feed | Resultaat als notitie + link; geen namen overnemen |
| M8 | Bank- en servicerkanalen | Wekelijks in een sessie: Idealista-assistent 4× ("de bancos": Jávea woningen en grond, "comarca Marina Alta" woningen en grond; `summary` controleren). Servicer-alerts (accounts Jan): Servihabitat (particulier + profesionales), Solvia, Diglo, Aliseda. Handmatige kwartaalronde: Unicaja, Cimenta2, EscogeCasa, Bankinter, Altamira, Hipoges, Facilitea, Sareb | Nieuwe bankobjecten | Geen crawler (voorwaarden); gepland gebruik van de assistent pas na toestemming van Idealista |
| M9 | RPC | Alleen per concreet dossier waarin een concurso wordt vermoed, en alleen op rechtspersonen | Concursstatus | Nooit systematisch; geen persoonsgegevens overnemen |
| M10 | PLACSP Atom-feed | Na verificatie dat patrimoniale verkopen erin staan | Gemeentelijke enajenaciones | Orgaan bevat Xàbia/Jávea |

**Gebeurtenissen (§10 masterprompt)**

| Gebeurtenis | Trigger |
|---|---|
| NIEUW GEPUBLICEERD | BOE-item van vandaag met SUB-id; nieuw record in `bienes.js` |
| NIEUW DOOR ONS ONTDEKT | Eerste keer gezien via alert of handmatig, terwijl de BOE-datum ouder is |
| STATUS GEWIJZIGD | PU → EJ → PC/FS; SU; CA (portaal of alert, bevestigd door handmatige controle) |
| DOCUMENTEN GEWIJZIGD | Andere hash of versie van edicto, certificación of nota simple |
| PRIJS GEWIJZIGD | Niet binnen een veiling; wel bij een nieuwe veiling van hetzelfde goed (RGR 97.7: 0,8 / 0,6) of een prijswijziging bij een servicer |
| NIET MEER GEVONDEN | Record verdwenen uit `bienes.js` of Idealista (≠ verkocht) |
| BRON NIET BEREIKBAAR | API 4xx/5xx na publicatietijd; geen sumario op een dag dat er wel een verwacht wordt; `bienes.js` > 48 u zonder nieuwe versie of met gewijzigde structuur |

**Deadlines per kanaal (rekenregels)**

| Moment | Gerechtelijk nieuw | Gerechtelijk oud | Notarieel (LN) | AEAT / SUMA | TGSS |
|---|---|---|---|---|---|
| Opening | ≥ 24 u na BOE (648) | Idem | ≥ 24 u (75.1.2ª) | ≥ 24 u na BOE (101.3) | Datum in anuncio; offertes ≥ 1 maand (116) |
| Sluiting | Portaalveld; 20 kalenderdagen; **geen verlenging**; niet op za/zo, feestdag, 24-12 t/m 06-01 of augustus (649.1) | Portaalveld; verlenging tot 24 u | Portaalveld (≥ 20 dagen) | Portaalveld; +1 u per laat bod, max. 24 u (104.3) | Envelop uiterlijk de werkdag vóór de zitting (118.1) |
| Waarborg klaar | 20 % of portaalveld | 5 % of portaalveld | 5 % of pliego | 5 % (portaalveld) | 25 %-cheque; bank blokkeert ≥ 10 dagen |
| Na sluiting | Vertegenwoordiging 3 dagen (647.1.1º); ≥ 70 % decreto de dag erna; < 70 %: 10 dagen voor de ejecutado (670.3) | Idem, oude drempels | — | Mesa ≤ 15 kalenderdagen (104 bis.1) | Schuldenaar 3 werkdagen (120.7) |
| Restbetaling | 20 dagen na sluiting (670.1) | 40 dagen | 10 werkdagen (75.3) | 15 dagen na kennisgeving (104 bis.3.b); escritura kiezen binnen 5 dagen | 5 werkdagen (117.2.g) |
| Later | Ontruiming vragen ≤ 1 jaar na verkrijging (675.2) | Idem | — | Tanteo derden (104 bis.3.a) | Tanteo TGSS 30 dagen (121) |

**Meldingen (alleen signaleren)**
- Via de bestaande Hermes-gateway (Discord/Telegram) en het ochtendrapport.
- Standaardmomenten: nieuw signaal met Dénia-orgaan of Xàbia-postcode (direct), T−7, T−3, T−1 en T−2 u vóór sluiting (R08).
- Beleidsvoorstel [4]: go/no-go van de advocaat uiterlijk T−5 werkdagen; waarborg gestort uiterlijk T−2 werkdagen (portaaladvies: meer dan één dag vooraf); herinnering restbetaling 5 dagen vóór de deadline; einde tanteoperiode; 1-jaarsvenster voor ontruiming.
- Elke melding bevat bron-URL, controlemoment en de open blokkades.

**Nooit geautomatiseerd (harde grens)**
- Registreren of inloggen op het portaal, waarborg storten, bieden, reserva de postura, cesión del remate, betalen, documenten ondertekenen, envelop of cheque indienen (TGSS).
- Bezichtiging aanvragen en contact met ejecutados, bewoners, curatoren, servicers of makelaars. Dat doet uitsluitend Jan, of iemand na zijn expliciete "ja" (masterprompt §19 en §27; CLAUDE.md regel 4).
- Geen definitief biedadvies zonder advocaatoordeel (bewijstype 6).

**Technische randvoorwaarden** [3/4]
- Python 3.11 in de Hermes-venv met httpx en de standaardbibliotheek (`json`, `xml.etree`); niets installeren.
- Eigen SQLite-opslag, niet de Postgres van Tree AI OS.
- Pdf-tooling (pdftoppm) ontbreekt [S91: R14, slot "Geblokkeerd of mislukt"]: documenten worden voorlopig handmatig gelezen. Installatie vraagt akkoord van Jan.
- Bouw pas in fase B, na akkoord.

### 2.10 Geen persoonsprofielen van schuldenaren — hoe dat technisch wordt afgedwongen

**Regel (masterprompt §19):** geen profielen van mensen die vermoedelijk hun hypotheek niet kunnen betalen. Onderzoek blijft objectgericht.

**Juridische grond** [2]:
- Namen van schuldenaren in edictos, veilingen, het RPC en de nota simple zijn persoonsgegevens en tonen de "situación financiera o de solvencia patrimonial" (AEPD-criterium 4) [S85, R16 §4.1].
- De BOE-hergebruiklicentie verplicht bij persoonsgegevens tot naleving van AVG en LOPDGDD [S39].
- Het RPC verbiedt "reutilización, tratamiento ulterior, cesión a terceros" [S49].
- RH 332.2 verbiedt opname van registergegevens in een databank "para su comercialización o reventa" [S6].
- Ley 19/2015 DA 2ª.2 wil voorkomen dat veilingaankondigingen "por medio de motores de búsqueda desde Internet" automatisch vindbaar worden [S19].
- AEPD E/04809/2015 (subastafacil.com) laat zien dat herpublicatie van debiteurgegevens en het "localizar y negociar" met schuldenaren het risicopunt is [S86; 2, gevolgtrekking 4].

**Velden die we NIET opslaan (in geen enkele tabel, log of prompt-cache)**

| Gegeven | Waar het voorkomt | Maatregel |
|---|---|---|
| Naam en apellidos van ejecutado, deudor, titular, bewoner of mede-eigenaar (natuurlijk persoon) | Edictos, anuncio-teksten, tablón Xàbia, RPC, nota simple, TEJU | Niet in het schema; de parser verwerpt het veld; regex-filter op vrije tekst (zie punt 3 hieronder) |
| NIF/NIE/DNI, ook de 4 willekeurige cijfers volgens LOPDGDD DA 7ª | Tablón Xàbia (apremio), RPC, edictos | Regex op `[0-9XYZ]\d{7}[A-Z]` en varianten → record wordt gecensureerd vóór opslag en gelogd als "persoonsgegeven verwijderd" |
| Woonadres of domicilio van de schuldenaar (voor zover anders dan het object) | Edictos, RPC | Niet in het schema |
| Telefoon of e-mail van particulieren; telefoonnummers uit portaaladvertenties, zoals `phone1` van de Idealista-assistent (of dat doorschakelnummers zijn is niet bewezen [4]) | Portalen, assistent | Niet in het schema (R16 §6.5; R01-verificatie R01-09, R06-verificatie R06-15) |
| Schuldeiser als natuurlijk persoon | Portaalveld "Acreedores" | Alleen categorie opslaan (bank / Hacienda / SS / VvE / particulier); naam alleen als het een rechtspersoon is |
| NPL-fiches en debiteurpagina's | Aliseda sitemap-loans (6.432 URL's), Diglo "Venta de Créditos" | Niet ophalen en niet opslaan |
| Foto's met herkenbare personen | Portaal, `bienes.js` fotos | Alleen de foto-URL als verwijzing; geen download of hash zolang de rechten op foto's in `bienes.js` niet zijn vastgesteld; nooit gezichtsherkenning (AI-verordening art. 5.1.e) |
| Gegevens uit RPC, TEJU en tablón-edictos | — | Deze bronnen worden niet geautomatiseerd ingelezen |

**Wat wél wordt opgeslagen (allowlist):**
- veiling-ID, BOE-B-nummer, autoriteit, zaaknummer, type, regime, status en data;
- valor subasta, tasación, puja mínima, depósito;
- recht en percentage, refcat, CRU/IDUFIR, postcode, gemeente, coördinaten van het object;
- situación posesoria (tekst over het object), visitable, lasten als bedrag en rang (houder alleen als rechtspersoon);
- documentverwijzingen met hash;
- eigen analyses.

**Technische afdwinging** [4, uitvoering fase B]:
1. **Schema zonder persoonsvelden.** De monitortabellen hebben geen kolommen voor naam, NIF of adres van personen. Een record met onbekende velden wordt geweigerd (strikte validatie, geen `raw_json` van portaal- of edictotekst).
2. **Parser op allowlist.** Uit het sumario alleen de metadata (identificador, titulo, departamento, url's, datum); uit `txt.php` alleen het SUB-id en het orgaan via een vast patroon. De rest van de tekst wordt niet bewaard.
3. **Privacyfilter vóór opslag** op alle vrije tekst (descripcion, cargas, información adicional): patronen voor DNI/NIE/NIF, "D./Dña.", "don/doña", "herederos de", telefoon en e-mail. Bij een treffer wordt het stuk gemaskeerd, zonder origineel, met een logregel.
4. **Geen koppeling op personen.** Koppelen gebeurt alleen op refcat, CRU/IDUFIR, SUB-id en coördinaat. Er is geen zoekfunctie op naam en geen join tussen bronnen op een persoon.
5. **Afgeschermd dossierdeel.** Velden gemarkeerd als [afgeschermd] in §2.8 (cantidad reclamada, vivienda habitual, fiscale vlag, eventuele namen voor de match met de nota simple) staan alleen in het dossier van een kandidaat die Jan in behandeling neemt. Per veld: doel, grondslag, wie het mocht zien en een verwijderdatum (voorstel R16 §6.2: uiterlijk 12 maanden na de veiling, of onderdeel van het aankoopdossier bij aankoop). Een verwijderjob draait met logregel; daarna eerst blokkeren tot de verjaring (LOPDGDD art. 32).
6. **Rechtenregister als poortwachter.** Elke bronadapter controleert vooraf `automated_access`, `storage` en `personal_data`. Staat een veld op `unknown` of `no`, dan weigert de adapter (R16 §6.5).
7. **Acceptatietest.** Een testbestand met een fictieve naam en een fictief NIF in een descripcion moet leiden tot 0 opgeslagen persoonsgegevens en 1 logregel.
8. **DPIA.** Zolang de module alleen objectvelden verwerkt: een vastgelegde afweging waarom geen DPIA nodig is. Zodra het afgeschermde dossierdeel persoonsgegevens bevat en die worden gekoppeld aan BOE-, register- of portaaldata en AI-analyse, raakt dat AEPD-criteria 4, 8 en 10, en bij gebruik van de uitzondering van AVG art. 14.5.b ook 11 (mogelijk 3): **DPIA vooraf** [S85; 2/4].
9. **Nooit contact** met schuldenaren of bewoners op basis van edictos zonder juridisch akkoord [R16 §4.5, §4.7].

### 2.11 Bronnenregister-regels (§7)

| Naam | URL | Type | Toegang | Status | Notities |
|---|---|---|---|---|---|
| BOE-sumario-API | https://www.boe.es/datosabiertos/api/boe/sumario/AAAAMMDD | Officiële open data | XML/JSON met Accept-header; zonder sleutel | TECHNISCH ONDERZOEK NODIG | Hergebruik toegestaan met bronvermelding; geen plaats van het goed; ratelimits ONBEKEND; 404 vóór publicatie |
| BOE-RSS Sección IV / V-B | https://www.boe.es/rss/boe.php?s=4 · ?s=5B | Officiële open data | RSS 2.0 | TECHNISCH ONDERZOEK NODIG | Terugval voor de API; telkens één sumario-item extra |
| BOE-aankondigingstekst | https://www.boe.es/diario_boe/txt.php?id=BOE-B-… | Officieel | HTML/tekst; `xml.php?` uitgesloten door robots | TECHNISCH ONDERZOEK NODIG | Alleen SUB-id en orgaan uitlezen |
| Portal de Subastas BOE | https://subastas.boe.es | Officieel veilingportaal | Handmatig; alerts na registratie (natuurlijke persoon, ≤ 50) | ALLEEN HANDMATIG | Automatische raadpleging pas na toestemming van de AEBOE (contract of toestemming nodig); robots `Disallow: /`; gebruiksvoorwaarden voor geregistreerden ONBEKEND |
| AEAT `bienes.js` | https://www2.agenciatributaria.gob.es/static_files/common/internet/dep/taiif/subastaInmuebles/data2/bienes.js | Officiële lijst | Statisch bestand, dagelijks | TECHNISCH ONDERZOEK NODIG | CC BY 4.0; pad niet gedocumenteerd; cp numeriek; gps soms leeg; rechten op foto's [te verifiëren] |
| AEAT avisos de nuevos bienes | https://sede.agenciatributaria.gob.es/Sede/subastas.html | Officieel | Na authenticatie | TECHNISCH ONDERZOEK NODIG | Niet getest |
| TGSS veilingen | https://w6.seg-social.es/subastas/ · https://sede.seg-social.gob.es/wps/portal/sede/sede/TablonAnuncios | Officieel | Web | ALLEEN HANDMATIG | Envelop + 25 %-cheque; tanteo 30 dagen |
| SUMA | https://www.suma.es/procedimiento-subastas | Officieel | Web; robots `Disallow: /` | ALLEEN HANDMATIG | Veilingen zelf via het BOE-portaal (SUB-RC) |
| Ajuntament de Xàbia, tablón | https://xabia.sedelectronica.es/board | Officieel | Web, paginering | ALLEEN HANDMATIG | Edictos bevatten NIF's: niet opslaan |
| Registro Público Concursal | https://www.publicidadconcursal.es/ | Officieel register | Web + captcha; robotisering verboden | ALLEEN HANDMATIG | Alleen per dossier, alleen rechtspersonen |
| subastasprocuradores.com | https://www.subastasprocuradores.com/ | Entidad especializada (CGPE) | Web | TECHNISCH ONDERZOEK NODIG | 4 % commissie (btw ONBEKEND) |
| eActivos | https://www.eactivos.com/ | Private entidad especializada | Web | ALLEEN HANDMATIG | Geautomatiseerd: niet gebruiken (verbod op "sistemas mecanizados"); gelijk aan het bronnenregister (R2-41) |
| GVA-patrimonium | https://hisenda.gva.es/es/web/subastas | Officieel | Web | ALLEEN HANDMATIG | Maandelijks |
| ATV | https://atv.gva.es/ | Officieel | — | TECHNISCH ONDERZOEK NODIG | Geen veilingkanaal gevonden |
| ORGA (FAQ-pdf) | https://www.mjusticia.gob.es/es/AreaTematica/OficinaRecuperacion/Documents/1292428756586-Preguntas_frecuentes_en_subastas_electronicas.PDF | Officieel | Pdf | NIET GEBRUIKEN | Niet als bron voor LEC-veilingen; alleen bruikbaar voor ORGA-regels |
| Idealista-assistent "de bancos" | (MCP van Idealista) | Officiële assistent | Sessie-tool | ALLEEN HANDMATIG | Gepland gebruik pas na schriftelijke toestemming van Idealista (contract of toestemming nodig); controleer `summary`; comarca-formulering gebruiken |
| Servihabitat (+ Profesionales), Solvia, Diglo | https://www.servihabitat.com/es/ · https://inversores.servihabitat.com/es/ · https://www.solvia.es · https://digloservicer.com | Servicers | Web; alerts met account | ALLEEN HANDMATIG | Voorwaarden verbieden extractie |
| Aliseda NPL / Diglo Venta de Créditos | https://www.alisedainmobiliaria.com/inversion/prestamos-y-cesiones-remate/npls · https://digloservicer.com/oportunidades/venta-credito | Vorderingen | Web | NIET GEBRUIKEN | Geen huis; juridisch traject; persoonsgegevensrisico |

---

## 3. Aannames en onzekerheden

**Werkhypothesen**
1. De rechtbank van Dénia is het partido judicial van Xàbia en veilt via Sección IV met titel "DENIA". Bewijs: twee voorbeelden (2022, 2026) en een lijst die via een zoekresultaat is gevonden [2/3]. Centrale veilingdiensten elders laten zien dat de titel ook de stad van een centrale dienst kan zijn [4].
2. De postcodes van Xàbia zijn 03730, 03737 en 03738 (R08, volledigheid [te verifiëren]; R09 noemt ook 03739).
3. Het oude of nieuwe LEC-regime hangt af van de datum waarop de procedure is ingeleid; het jaartal in het expediente is een aanwijzing [4].
4. Hergebruik van BOE-sumario en `bienes.js` volgens de gepubliceerde licenties dekt ons gebruik. Eén aanroep per dag plus één per geselecteerd item blijft binnen redelijk gebruik [4; ratelimits ONBEKEND].
5. Het pad van `bienes.js` blijft stabiel (niet gedocumenteerd) [7].
6. De veilingstroom levert in Jávea gemiddeld zeer weinig kandidaten op. De basisfrequentie is ONBEKEND tot de handmatige nulmeting [4/7].
7. ITP wordt gerekend over max(valor de referencia, remate); plusvalía Xàbia met 30 %; bij een onbekende verkoper de duurste fiscale variant [5].
8. De bieder (entiteit), de rendementseis en de financiering zijn ONBEKEND: er is dus nog geen maximale bieding te berekenen [7].

**Onzekerheden die per dossier kunnen kantelen**
- ATV-praktijk voor de ITP-grondslag bij veilingen.
- AJD over testimonio of certificación.
- Waarborg bij een notariële hypotheekveiling (LN 5 %, LEC of RH 236-h).
- Wettelijke afecciones (IBI-achterstand, VvE) die niet in de certificación staan.
- Of IRNR-inhouding (3 %) bij toewijzing geldt.
- Of een huurcontract doorloopt.
- Drempels van art. 24 LCCI (niet gelezen).
- Voorwaarden voor geregistreerde portaalgebruikers en voor inlezen van alertmails.
- Of AEAT-, notariële en gemeentelijke veilingen altijd een BOE-item opleveren (AEAT en SUMA wel gezien in V-B; notarieel ONBEKEND).
- Betekenis van de velden `interes` en `capital` in `bienes.js` [7].

## 4. Tegenargumenten of aandachtspunten

- **Is het de moeite waard?** Vandaag levert de stroom in Jávea niets op. Tegenargument: de monitor kost 2 verzoeken per dag en een paar alerts, en één vermeden fout (bod op een aandeel, bezet huis, verkeerd regime) weegt zwaarder dan de bouwtijd [4].
- **Een veilingkorting is vaak schijn.**
  - Veilingwaarde is geen marktwaarde en de gevorderde schuld is geen koopprijs.
  - ITP wordt over de valor de referencia geheven, ook als de toewijzing lager is [2/4].
  - Eerdere lasten komen boven op de prijs [2].
- **Liquiditeit.** 20 % waarborg en 20 dagen voor de rest vragen direct beschikbaar geld. Hypotheekfinanciering via het testimonio (670.6) schort de termijn op, maar een bank moet dan wel meewerken [2/4].
- **Blinde biedingen.** Onder het nieuwe regime zijn biedingen geheim; je biedt zonder te weten of er concurrentie is [2].
- **Veel loten zijn geen huizen maar rechten.** Aandelen, blote eigendom en retractrechten: 52 van 230 AEAT-loten zijn aandelen [3].
- **Na winnen ben je nog niet klaar.** De schuldenaar kan bij een bod onder 70 % een derde aandragen (670.3) of de schuld aflossen (670.7, 693.3); de TGSS kan 30 dagen lang tanteo uitoefenen [2].
- **Bezetting.** "No consta" is gewoon; ontruiming binnen de executie kan maar tot een jaar na verkrijging [2].
- **Ontwerpfout in eerder werk.** R08 §10.2 en R17 §5.3 filteren BOE-items op plaatsnamen van Marina Alta. Dat vindt niets, omdat de aankondigingen die plaats niet bevatten [2/3]. R17 moet worden aangepast.
- **Licentie is geen robotstoestemming.** De BOE-hergebruiklicentie geldt voor documenten van de sede, maar robots.txt van het portaal blijft `Disallow: /`. Automatische detailraadpleging kan pas met toestemming van de AEBOE [2/4].
- **Servicerlandschap schuift.** Hipoges/Servihabitat, Sareb Lot A en Diglo/doValue staan in de pers en spreken elkaar deels tegen [1 (pers)/7]. Namen en mandaten per kwartaal hercontroleren.
- **Idealista "de bancos" dekt niet alles.** Solvia toont woningen in Dénia en Calp die Idealista niet als bankwoning telt; een deel is particulier aanbod [3/4].
- **Privacyrisico.** Juist omdat de tablón van Xàbia en edictos NIF's bevatten, is geautomatiseerd inlezen daarvan uitgesloten, ook als het technisch kan [2/4].

## 5. Concrete vervolgstap

| # | Stap | Wie | Akkoord nodig? |
|---|---|---|---|
| 1 | **Nulmeting BOE:** sumario-API van de laatste 30 dagen (30 verzoeken) plus `bienes.js` van vandaag. Tellen: Sección IV-items met titel DENIA en SUB-ids, V-B-items van AEAT, SUMA en TGSS. Alleen metadata, geen namen | Deal Hunter-agent | Nee (open data, alleen lezen) |
| 2 | ⏸️ **ACTIE VOOR JAN:** registreren op subastas.boe.es (Cl@ve of certificaat), gebruiksvoorwaarden als pdf bewaren, alerts instellen volgens §2.9 M5. Daarna één **handmatige** zoekopdracht "Jávea, onroerend goed, alle statussen" en per jaar tellen (geen namen noteren) om de basisfrequentie vast te stellen | Jan | — |
| 3 | ⏸️ **ACTIE VOOR JAN:** een Spaanse advocaat (executies/procesrecht) en een gestor kiezen; offerte per dossier vragen (tarieven zijn ONBEKEND; colegios mogen geen richtprijzen publiceren) en de vragenlijst uit §7 meesturen | Jan | — |
| 4 | Conceptbrief aan de AEBOE: toestemming voor gerichte detailraadpleging per SUB-id | Agent schrijft, Jan verstuurt | Ja, "ja" van Jan vóór verzending |
| 5 | Vastleggen in het rechtenregister: statussen uit §2.11; aanpassen van R17 §5.3 (geen plaatsfilter op BOE) | Agent | Nee (interne documenten) |
| 6 | Fase B (na akkoord): adapters M1, M2 en M4; dossierschema §2.8; privacyfilter en acceptatietest §2.10; deadlinerekenaar §2.9; DPIA-afweging vastleggen | Agent | Ja, bouwbesluit Jan |
| 7 | De twee Sareb-percelen door deliverable 3 (kadaster, register, stand van de UA); perceel A daar samen met K10 als één object behandelen (identiteit [4], planklasse [7]); geen contact met de verkoper | Agent | Downloads van fiches: akkoord Jan |

---

## 6. Controlelijst vóór ieder biedingsvoorstel

Een biedingsvoorstel aan Jan komt er alleen als **alle** punten "ja" zijn en bewijs in het dossier hebben. Eén "nee" of "onbekend" betekent geen voorstel, alleen een onderzoeksvraag.

1. **Bron.** Veiling-ID, BOE-B-nummer en autoridad gestora vastgelegd; status "celebrándose" of "próxima apertura"; sluitingsdatum uit portaal of edicto (niet uit een alert).
2. **Type en regime.** Proceduretype (A–G) en regime (LEC oud of nieuw, LN, LH 129, RGR, RGRSS, TRLC-reglas) vastgesteld en door de advocaat bevestigd. De bijbehorende waarborg, verlengingsregel, drempels en betaaltermijn staan in het dossier.
3. **Recht.** Aangeboden recht is 100 % pleno dominio, bevestigd in de portaalomschrijving én de certificación. Geen tanteo- of retractrecht open.
4. **Object.** Refcat en CRU/IDUFIR komen overeen met omschrijving en adres; perceel gekoppeld via deliverable 3; urbanistische status bekend.
5. **Certificación.** Aanwezig, niet ouder dan 6 maanden of met een geactualiseerde nota simple (TREE-beleid).
6. **Lasten.** Alle eerdere lasten gekwantificeerd met actueel saldo en dagrente (art. 657) en opgeteld bij de prijs. Latere lasten gemarkeerd als doorgehaald, met grondslag. Afecciones (IBI, VvE) nagevraagd of als risicopost opgenomen.
7. **Waarde.** Tasación aanwezig, niet 0,00 € en gedateerd; veilingwaarde herleid (tasación min eerdere lasten). Eigen marktwaarde apart bepaald (§20). Cantidad reclamada niet als prijs gebruikt.
8. **Bezit.** Situación posesoria gelezen; vivienda habitual bekend; bij bezetting een ontruimingsscenario met termijn (675.2) en kosten; bezichtiging aangevraagd via de rechtbank waar mogelijk (door Jan).
9. **Status en procedurerisico.** Geen schorsing, concurso, verzet of tercería bekend; aflossingsrecht van de schuldenaar (670.7, 693.3) en verbeteringsrecht (670.3; TGSS 120.7) doorgerekend.
10. **Biedscenario.** Wat gebeurt er met ons bod bij < 70 %, bij een eigen woning (70/60 %), bij AEAT < 50 % (discretie van de Mesa) en bij TGSS (tanteo)? Onder het nieuwe LEC-regime: rekening gehouden met geheime biedingen.
11. **Fiscaal.** Valor de referencia opgevraagd; ITP 9/11 % over max(valor de referencia, remate) of btw + AJD bevestigd door gestor; plusvalía-substitutie (106.2) als vlag; kosten van doorhaling en inschrijving opgenomen.
12. **Liquiditeit.** Waarborg beschikbaar op een rekening bij een entidad colaboradora op naam van de bieder; restbetaling gefinancierd binnen de wettelijke termijn; plafond voor gelijktijdige waarborgen niet overschreden.
13. **Bieder.** Entiteit gekozen door Jan; vertegenwoordiging vooraf geregeld (3-dagenregel LEC 647.1.1º; bij AEAT meteen "en representación" opgeven).
14. **Maximale bieding.** Berekend volgens §22 met de rendementseis van Jan en gevoeligheden (−10 % opbrengst, +15 % bouwkosten, +6 maanden). Waarborg als liquiditeitsbeslag, niet als kosten.
15. **Privacy.** Het dossier bevat alleen noodzakelijke persoonsgegevens in het afgeschermde deel, met grondslag en verwijderdatum; geen contact met ejecutado of bewoners.
16. **Advocaat.** Schriftelijk oordeel op alle vragen uit §7 (bewijstype 6), met datum.
17. **Besluit.** Jan geeft expliciet "ja" op het voorstel. Bieden, storten en betalen doet Jan zelf.

## 7. Wat een Spaanse advocaat per dossier moet bevestigen

1. **Regime en regels.** Welk regime geldt (DT 9ª LO 1/2025: wat is "incoado" in deze executie)? Welke waarborg, verlenging, drempels en betaaltermijn volgen daaruit? Bij een notariële hypotheekveiling: welke waarborg (LN 75, LEC via LH 129 of RH 236-h)?
2. **Aangeboden recht en titulación.** Is het werkelijk 100 % volle eigendom? Welke gebreken in de titulación aanvaardt de bieder (668, 669.2)? Zijn er voorkeursrechten van derden, zoals het in het portaal vermelde retracto of de tanteo van TGSS of derden?
3. **Lasten en rangorde.** Welke lasten blijven bestaan en voor welk actueel bedrag? Welke worden doorgehaald (674, LH 134, RGR 111, TRLC 225) en voor wiens rekening? Welke wettelijke afecciones (IBI, VvE) volgen het goed buiten de certificación om?
4. **Bezit en ontruiming.** Wat betekent de situación posesoria? Is er een verklaring volgens 661.2? Loopt een huurcontract door? Wat zijn termijn en kosten van ontruiming (675.2), en welke beschermingsregels voor de eigen woning of kwetsbare bewoners gelden (685.2, Ley 12/2023)?
5. **Procedurerisico.** Loopt er verzet (695), een tercería (696), een concurso van de schuldenaar (649.1, 691.5; TRLC 145), een schorsing of een bevrijdingsmogelijkheid (670.7, 693.3)?
6. **Ons bod.** Wat gebeurt er bij ons voorgenomen bod met de drempels (670.3, 671; RGR 104 bis; RGRSS 120), en wanneer is de toewijzing definitief (tanteo 30 dagen bij TGSS)?
7. **Bieder en vertegenwoordiging.** Hoe biedt de gekozen entiteit rechtsgeldig (647.1.1º; AEAT "en representación"; cessie alleen waar toegestaan)? Wat zijn de gevolgen van een latere doortransmissie (dubbele belasting)?
8. **Fiscaal (met gestor).** ITP-grondslag bij deze toewijzing (valor de referencia of remate; ATV-praktijk); btw in plaats van ITP als de ejecutado ondernemer is (10 % of 21 %, afstand van vrijstelling); AJD over testimonio, certificación of escritura; plusvalía-substitutie (106.2) en vrijstelling (105.1.c); IRNR-inhouding bij toewijzing.
9. **Titel en inschrijving.** Welke titel krijgen we (testimonio LEC 673, certificación RGR 104 bis.3.e, certificado RGRSS 122)? Is een escritura verstandig? Is de inschrijving haalbaar als er geen eerdere titels zijn (RGR 98.2)?
10. **Faillissement (indien type D).** Wat staat er in de reglas especiales? Welk platform, welke waarborg en commissie? Verkoop met of zonder behoud van de hypotheek (212 of 225)?
11. **Privacy.** Welke persoonsgegevens mogen voor dit dossier worden bewaard, op welke grondslag en hoe lang? Is contact met ejecutado of bewoners toegestaan (standaard: nee)?
12. **Urbanisme (samen met architect/urbanist).** Is het object legaal gebouwd of het perceel bebouwbaar volgens de geldende regels (deliverable 3)?

---

## 8. Bronnenlijst (URL · controledatum · bewijstype)

Controledatum "14-09" = meting in R08/R09 (14-09-2026); "15-09" = hercontrole in de verificatiebestanden of in R10/R16 (15-09-2026). Wetteksten: geldende geconsolideerde versie op boe.es.

**Wetgeving (geconsolideerd)**
- S1 — Ley 1/2000 LEC ("Última actualización publicada el 28/02/2025"; veilingartikelen met effect 03-04-2025), art. 634–698 — https://www.boe.es/buscar/act.php?id=BOE-A-2000-323 · 14-09 en 15-09-2026 · 2
- S2 — LEC, oude tekst (versie 20-12-2023) — https://www.boe.es/buscar/act.php?id=BOE-A-2000-323&tn=1&p=20231220 · 15-09-2026 · 2
- S3 — LO 1/2025, DT 9ª (cons. 04-06-2025) — https://www.boe.es/buscar/act.php?id=BOE-A-2025-76 · 15-09-2026 · 2
- S4 — Ley Hipotecaria art. 129, 131–134, 221–222 (cons. 03-01-2025) — https://www.boe.es/buscar/act.php?id=BOE-A-1946-2453 · 15-09-2026 · 2
- S5 — Ley del Notariado art. 72–77 (cons. 03-01-2025) — https://www.boe.es/buscar/act.php?id=BOE-A-1862-4073 · 15-09-2026 · 2
- S6 — Reglamento Hipotecario art. 236-h, 332 (cons. 26-11-2020) — https://www.boe.es/buscar/act.php?id=BOE-A-1947-3843 · 15-09-2026 · 2
- S7 — RD 939/2005 RGR art. 97–111 (cons. 31-01-2024) — https://www.boe.es/buscar/act.php?id=BOE-A-2005-14803 · 15-09-2026 · 2
- S8 — Ley 58/2003 LGT art. 172 (cons. 21-12-2024) — https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186 · 15-09-2026 · 2
- S9 — RD 1415/2004 RGRSS art. 110–124 (cons. 30-07-2026) — https://www.boe.es/buscar/act.php?id=BOE-A-2004-11836 · 15-09-2026 · 2
- S10 — RDL 1/2020 TRLC art. 145, 209–225, 415–423 bis, 430 (cons. 03-01-2025) — https://www.boe.es/buscar/act.php?id=BOE-A-2020-4859 · 15-09-2026 · 2
- S11 — TRRL (RDLeg 781/1986) art. 80 — https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-1986-9865/texto/bloque/art80 · 15-09-2026 · 2
- S12 — RBEL (RD 1372/1986) art. 109, 112, 118 — https://www.boe.es/eli/es/rd/1986/06/13/1372/con · 14-09-2026 · 2
- S13 — TRLITPAJD (RDLeg 1/1993) art. 7, 10, 29–31 (cons. 21-03-2026) — https://www.boe.es/buscar/act.php?id=BOE-A-1993-25359 · 15-09-2026 · 2
- S14 — RITP (RD 828/1995) art. 39 met vernietigingsnoot; Resolución 05-05-1998 (TS 3-11-1997) — https://www.boe.es/buscar/act.php?id=BOE-A-1995-15071 · https://www.boe.es/diario_boe/txt.php?id=BOE-A-1998-12015 · 15-09-2026 · 2
- S15 — Ley 13/1997 CV art. 13, 14, 14 bis, 14 ter (cons. 02-07-2026); Ley 5/2025 art. 33–34 — https://www.boe.es/buscar/act.php?id=BOE-A-1998-8202 · https://www.boe.es/diario_boe/txt.php?id=BOE-A-2025-11959 · 15-09-2026 · 2
- S16 — TRLHL (RDLeg 2/2004) art. 72, 102, 104–108 (cons. 03-06-2026) — https://www.boe.es/buscar/act.php?id=BOE-A-2004-4214 · 15-09-2026 · 2
- S17 — Ley 37/1992 LIVA art. 20, 90, 91 — https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740 · 15-09-2026 · 2
- S18 — RDLeg 5/2004 LIRNR art. 25 — https://www.boe.es/buscar/act.php?id=BOE-A-2004-4527 · 15-09-2026 · 2
- S19 — Ley 19/2015 DA 2ª — https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-2015-7851/texto/bloque/dasegunda · 15-09-2026 · 2
- S20 — LOPDGDD (LO 3/2018) art. 19, 23, 32, DA 7ª — https://www.boe.es/buscar/act.php?id=BOE-A-2018-16673 · 15-09-2026 · 2
- S21 — AVG (Verordening 2016/679) art. 5, 6, 14, 35 — https://www.boe.es/buscar/doc.php?id=DOUE-L-2016-80807 · 15-09-2026 · 2
- S22 — RD 1559/2012 art. 16.3 (Sareb) — https://www.boe.es/buscar/act.php?id=BOE-A-2012-14118 · 15-09-2026 · 2
- S23 — Orden PJC/784/2025 (Sareb → Casa 47) — https://www.boe.es/diario_boe/txt.php?id=BOE-A-2025-15292 · 15-09-2026 · 2
- S24 — TRLPI art. 133–134 (databankrecht) — https://www.boe.es/buscar/act.php?id=BOE-A-1996-8930 · 15-09-2026 · 2
- S25 — RD 1426/1989 arancel notarial, Anexo I Número 2 — https://www.boe.es/buscar/act.php?id=BOE-A-1989-28111 · 15-09-2026 · 2 (berekening: 5)
- S26 — RD 1427/1989 arancel registral, Número 2 — https://www.boe.es/buscar/act.php?id=BOE-A-1989-28112 · 15-09-2026 · 2 (berekening: 5)

**Portaal, BOE en officiële veilingkanalen**
- S30 — Portal de Subastas, helppagina — https://subastas.boe.es/ayuda.php · 15-09-2026 · 2
- S31 — Portal de Subastas, robots.txt — https://subastas.boe.es/robots.txt · 15-09-2026 · 3
- S32 — Portal de Subastas, zoekformulier en resultaten provincie Alicante (EJ/PU) en localidad JAVEA — https://subastas.boe.es/subastas_ava.php · 14-09-2026 (R08, R09) en 15-09-2026 (verificatie R08) · 3
- S33 — Detail SUB-AT-2026-26R2886001392 (Dénia, AEAT) — https://subastas.boe.es/detalleSubasta.php?idSub=SUB-AT-2026-26R2886001392 · 15-09-2026 · 3
- S34 — Detail SUB-RC-2026-0026I20250184 (SUMA) — https://subastas.boe.es/detalleSubasta.php?idSub=SUB-RC-2026-0026I20250184 · 14-09-2026 · 3
- S35 — Detail SUB-JA-2026-257820 (TI Dénia, Jávea) — https://subastas.boe.es/detalleSubasta.php?idSub=SUB-JA-2026-257820 · 15-09-2026 · 3
- S36 — BOE-sumario-API — https://www.boe.es/datosabiertos/api/boe/sumario/20260914 (ook /20260915, /20260217, /20220604) · 15-09-2026 · 3
- S37 — BOE-RSS Sección IV en V-B — https://www.boe.es/rss/boe.php?s=4 · https://www.boe.es/rss/boe.php?s=5B · 15-09-2026 · 3
- S38 — boe.es robots.txt — https://www.boe.es/robots.txt · 15-09-2026 · 3
- S39 — AEBOE aviso legal, condiciones de reutilización (licentie 27-06-2024) — https://www.boe.es/informacion/aviso_legal/index.php · 15-09-2026 · 2
- S40 — BOE-aankondigingen BOE-B-2026-29751, BOE-B-2026-4679, BOE-B-2022-17675, BOE-B-2026-29821 t/m 29837, BOE-B-2026-29754 — https://www.boe.es/diario_boe/txt.php?id=BOE-B-2026-4679 (en overeenkomstig per id) · 15-09-2026 · 2/3
- S41 — AEAT sede, Subastas — https://sede.agenciatributaria.gob.es/Sede/subastas.html · 15-09-2026 · 2
- S42 — AEAT sede, algemene regels en licitadores — https://sede.agenciatributaria.gob.es/Sede/deudas-apremios-embargos-subastas/subastas/general.html · https://sede.agenciatributaria.gob.es/Sede/deudas-apremios-embargos-subastas/subastas/licitadores.html · 15-09-2026 · 2
- S43 — AEAT `bienes.js` (CC BY 4.0) — https://www2.agenciatributaria.gob.es/static_files/common/internet/dep/taiif/subastaInmuebles/data2/bienes.js · 15-09-2026 · 3
- S44 — AEAT procedurefiche RF02 (verouderd) — https://sede.agenciatributaria.gob.es/Sede/procedimientos/RF02.shtml · 15-09-2026 · 7
- S45 — TGSS, Subastas de bienes embargados — https://w6.seg-social.es/subastas/ · 15-09-2026 · 2/3
- S46 — TGSS, tablón sede en "Información venta de inmuebles" — https://sede.seg-social.gob.es/wps/portal/sede/sede/TablonAnuncios · https://sede.seg-social.gob.es/wps/portal/sede/sede/Ciudadanos/Otros+Procedimientos/202285 · 15-09-2026 · 3
- S47 — SUMA, procedimiento subastas (+ robots.txt) — https://www.suma.es/procedimiento-subastas · 15-09-2026 · 2/3
- S48 — GVA, subastas patrimonio — https://hisenda.gva.es/es/web/subastas · 14-09-2026 · 2/3
- S49 — Registro Público Concursal: consulta, liquidaciones, aviso legal — https://www.publicidadconcursal.es/consulta-publicidad-concursal-new · https://www.publicidadconcursal.es/liquidaciones · https://www.publicidadconcursal.es/aviso-legal · 15-09-2026 · 2
- S50 — subastasprocuradores.com, voorwaarden — https://www.subastasprocuradores.com/terms?culture=es · 15-09-2026 · 2
- S51 — eActivos, aviso legal — https://www.eactivos.com/aviso-legal · 15-09-2026 · 2
- S52 — Ajuntament de Xàbia, tablón — https://xabia.sedelectronica.es/board · 15-09-2026 · 3
- S53 — Sección Civil TI Dénia — https://sede.gva.es/es/detall-organ-juridic?id_dept=26350 · 15-09-2026 · 2
- S54 — ORGA, FAQ subastas electrónicas (2018) — https://www.mjusticia.gob.es/es/AreaTematica/OficinaRecuperacion/Documents/1292428756586-Preguntas_frecuentes_en_subastas_electronicas.PDF · 15-09-2026 · 2 (alleen ORGA)
- S55 — BOP Alicante, buscador — https://sede.diputacionalicante.es/consultas-bop/ · 14-09-2026 · 3
- S56 — PLACSP open data — https://www.hacienda.gob.es/en-GB/GobiernoAbierto/Datos%20Abiertos/Paginas/LicitacionesContratante.aspx · 14-09-2026 · 2
- S57 — TEJU, help — https://www.boe.es/buscar/ayudas/edictos_judiciales_ayuda.php · 14-09-2026 · 2

**Fiscaal en gemeentelijk**
- S60 — ATV, ITPAJD-tariefcodes (TS0) — https://atv.gva.es/es/itpajd · 15-09-2026 · 2
- S61 — CGPJ, TSXG over valor de referencia bij veilingen (04-05-2026) — https://www.poderjudicial.es/cgpj/es/Poder-Judicial/Noticias-Judiciales/El-TSXG-ratifica-que-el-valor-de-referencia-de-los-inmuebles-prevalece-sobre-el-de-adquisicion-en-subastas-para-el-calculo-de-la-base-imponible-del-Impuesto-sobre-Transmisiones-Patrimoniales- · 15-09-2026 · 2
- S62 — Cuatrecasas, DGT V0453-22 (11-05-2022) — https://www.cuatrecasas.com/es/spain/art/espana-la-base-imponible-de-tpo-en-la-adjudicacion-judicial-de-inmuebles · 15-09-2026 · 1 (secundair)
- S63 — Iberley, DGT-consultas over veilingen — https://www.iberley.es/noticias/la-direccion-general-tributos-se-pronuncia-itpyajd-caso-adjudicaciones-inmuebles-subasta-publica-32825 · 15-09-2026 · 1 (secundair)
- S64 — Ministerio de Hacienda, Información Impositiva Municipal (Xàbia 2026: IBI 0,83 %, ICIO 4 %; 2021 IIVTNU 30 %) — https://serviciostelematicosext.hacienda.gob.es/SGFAL/ConsultaTipos/aspx/ImpuestosExcel.aspx?provincia=TODAS&anosel=2026 · 15-09-2026 · 2

**Bank-, fonds- en servicerkanalen**
- S70 — Idealista, "de bancos" Jávea en Marina Alta (via Idealista-assistent) — https://www.idealista.com/es/venta-viviendas/javeaxabia-alicante/con-de-bancos/ · https://www.idealista.com/es/venta-terrenos/javeaxabia-alicante/con-de-bancos/ · https://www.idealista.com/es/venta-viviendas/alicante/marina-alta/con-de-bancos/ · https://www.idealista.com/es/venta-terrenos/alicante/marina-alta/con-de-bancos/ · 15-09-2026 · 3
- S71 — Servihabitat, lijstpagina's en "WOW! Venta Especial" — https://www.servihabitat.com/es/venta/terreno/alicante-marinaalta · https://www.servihabitat.com/es/venta/vivienda/alicante · https://www.servihabitat.com/es/wowventasespeciales · 15-09-2026 · 1/3
- S72 — Servihabitat Profesionales, Jávea-percelen — https://inversores.servihabitat.com/es/venta/promociones/terreno-urbanonoconsolidado/alicante-marinaalta-balconalmarjavea/06124187 · https://inversores.servihabitat.com/es/venta/promociones/terreno-urbanonoconsolidado/alicante-huertasur-xabia/06124173 · 15-09-2026 · 1/3
- S73 — Servihabitat, gebruiksvoorwaarden — https://www.servihabitat.com/es/terminos-generales-de-uso · 15-09-2026 · 1
- S74 — Solvia, lijstpagina's en aviso legal — https://www.solvia.es/es/comprar/viviendas/alicante · https://www.solvia.es/es/comprar/viviendas/alicante/javea · https://www.solvia.es/es/aviso-legal · 15-09-2026 · 1/3
- S75 — Diglo, lijstpagina's, Venta de Créditos, aviso legal — https://digloservicer.com/venta-casas-pisos/cualquiera/alicante · https://digloservicer.com/oportunidades/venta-credito · https://digloservicer.com/aviso-legal · 15-09-2026 · 1/3
- S76 — Aliseda, sitemap-loans.xml — https://www.alisedainmobiliaria.com/sitemap-loans.xml · 15-09-2026 · 3
- S77 — eldiario.es 29-05-2026, Sareb-contract en liquidatie eind 2027 — https://www.eldiario.es/economia/servihabitat-anticipa-aliseda-llevan-ultimo-gran-contrato-sareb-174-millones-deshacerse-4-860-m_1_13260273.html · 15-09-2026 · 1 (pers)
- S78 — Brains RE News 12-08-2026, bezwaar Hipoges tegen Lot A — https://brainsre.news/disputa-hipoges-servihabitat-viviendas-sareb/ · 15-09-2026 · 1 (pers)
- S79 — TED 140491-2026, Sareb-adviseur portefeuilleverkoop — https://ted.europa.eu/es/notice/140491-2026/pdf · 15-09-2026 · 2
- S80 — Toegangstests (403/JavaScript) Sareb, Altamira, Bankinter — https://www.sareb.es/buscador-de-inmuebles/ · https://www.altamirainmuebles.com/ · https://www.bankinter.com/www/es-es/cgi/ebk+inm+home · 15-09-2026 · 3
- S81 — Idealista-detail 111869151 (`property_detail`: `commercialName` "Servihabitat", `externalReference` 60709763, "Terreno urbanizable"; R10-verificatie R10-17, A4) en kandidaat K10 107655781 (dubbel met 111869151; R15-verificatie R15-09), via de Idealista-assistent — https://www.idealista.com/es/inmueble/111869151/ · https://www.idealista.com/es/inmueble/107655781/ · 15-09-2026 · 1 (inhoud) / 3 (bestaan); koppeling aan perceel A (S72): 4

**Compliance**
- S85 — AEPD, lijst DPIA art. 35.4 (criteria 3, 4, 8, 10, 11) — https://www.aepd.es/documento/listas-dpia-es-35-4.pdf · 15-09-2026 · 2
- S86 — AEPD E/04809/2015 (subastafacil.com) — https://www.aepd.es/documento/e-04809-2015.pdf · 15-09-2026 (inhoud via R16) · 2
- S87 — Idealista, Términos y condiciones (versie 20-11-2020) — https://st1.idealista.com/ayuda/wp-content/uploads/2021/11/2021-Hasta-11-11-2021-Terminos-y-condiciones.pdf · 15-09-2026 · 2

**Lokaal en intern**
- S90 — Eigen woningfeed properties-api (alleen lezen): 56 objecten "Javea", 224 totaal, 0 treffers op bank-, servicer- en veilingwoorden — http://127.0.0.1:3100/api/properties?town=Javea&limit=100 · 15-09-2026 (zelf) · 3 (conclusie "geen bankobjecten": 4)
- S91 — Onderzoeksbestanden (voor wie dieper wil): `onderzoek/R08-veilingen-portalen-toegang.md` (+ `.verificatie.md`), `onderzoek/R09-veilingen-juridisch-procedure.md` (+ `.verificatie.md`), `onderzoek/R10-banken-servicers-fondsen.md` (+ `.verificatie.md`), `onderzoek/R14-financieel-fiscaal-kostenkengetallen.md` (+ `.verificatie.md`), `onderzoek/R16-rechten-en-compliance.md` (+ `.verificatie.md`); kruisverwijzing `onderzoek/R17-architectuur-mvp-kosten.md` §5.3; voor de koppeling perceel A = K10 ook `onderzoek/R15-kandidaten-javea-live.md` (+ `.verificatie.md`) en deliverables `02-bronnenkaart-en-register.md` §2.5, `03-aanpak-percelen.md` §2.6 en `05-bouwplan-fase-b-mvp.md` · 14/15-09-2026 · intern

**Niet zelf opnieuw gecontroleerd in deze schrijfronde:** alle externe bronnen zijn overgenomen uit de genoemde rapporten en verificaties, met hun controledatum. Zelf gecontroleerd op 15-09-2026 is alleen S90. WebSearch en het veilingportaal zijn in deze ronde niet gebruikt. Er zijn geen sleutels, geen telefoonnummers en geen namen van particulieren of schuldenaren opgenomen.

## Herzieningen

- 15-09-2026 (volledigheidskritiek): Sareb-perceel A gekoppeld aan Idealista 111869151 en kandidaat K10 (107655781) als waarschijnlijk hetzelfde object (type 4), met tegenstrijdige planklasse (type 7), in de samenvatting, §1, §2.1, §2.3, §2.4.7, §2.4.8, §2.4.10 en §5 (nieuwe bron S81); bankaanbod gesplitst in 0 woningen, 1 perceel op Idealista en 2 Sareb-percelen bij Servihabitat Profesionales (2 unieke objecten); "Idealista-doorschakelnummers" in §2.10 voorzichtig geformuleerd (niet bewezen); eActivos op ALLEEN HANDMATIG gezet, gelijk aan het register (R2-41); statuscellen in §2.2 en §2.11 teruggebracht tot één van de zes statussen, met een aparte toelichting (§2.2: nieuwe kolom); source_modified_at toegevoegd aan dossierveld 44. Gecontroleerd zonder wijziging: 04 noemt geen aantal regels voor het bronnenregister.
- 15-09-2026 (samenhangscontrole): bankaanbod in §1 ook als 1 perceel op Idealista plus 2 Sareb-percelen bij Servihabitat Profesionales geformuleerd; verwijzing naar de top-3 in deliverable 01 §1.2 bij de drie vragen toegevoegd. Gecontroleerd zonder verdere wijziging: K10-lezing, eActivos, `phone1`, geheimen en telefoonnummers.

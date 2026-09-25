# Deliverable 3 — De concrete aanpak voor percelen

**TREE Deal Hunter, fase A · masterprompt §14–17 (en §30–31.3)**
**Controledatum:** 15-09-2026. Wat ik zelf heb gecontroleerd (alleen de eigen BP-feed, 03:59 CEST; opnieuw gelezen na de kritiekronde, zelfde uitkomst) draagt die datum. Alle overige feiten komen uit de onderzoeksrapporten R10–R15 en R17 en hun tegenspraakrapporten; zij dragen hun eigen testdatum (R11: 14-09-2026, hercontrole 15-09-2026; R10-verificatie, R12, R13, R14-verificatie, R15-verificatie en R17-verificatie: 15-09-2026). Bij een weerlegde claim is de gecorrigeerde versie gebruikt.
**Bewijstypen (§5):** 1 aanbieder · 2 officiële bron · 3 door ons vastgesteld · 4 AI-inferentie · 5 berekening op benoemde aannames · 6 bevoegde professional · 7 onbekend of tegenstrijdig. Bronverwijzingen staan als [B..] (onderzoeksbestanden) en [C..] (externe bronnen, met URL) in de bronnenlijst achteraan. Technische adressen van de overheidsdiensten staan als [E..] in **bijlage A**.
**Status:** werkdocument, geen juridisch of stedenbouwkundig advies. Geen enkele bouwconclusie in dit document vervangt een informe urbanístico, een cédula of de toets van een lokale architect.
**Kritiekronde 15-09-2026 verwerkt:** K10 herkend als het Sareb-perceel "UA Balcón al Mar 1" (§2.6); kosten per scenario en een scenario voor herverkaveling toegevoegd (§2.5); wegen, toegang, erfdienstbaarheden en archeologie toegevoegd (stap 7, 10, 11 en §2.3); begrippenlijst en bijlage A toegevoegd.

**Leeswijzer voor Jan**
- Voor besluiten: §1 (conclusie en besluiten), §2.6 (echte percelen), §4 (tegenargumenten) en §5 (vervolgstappen).
- Voor de bouwer van het systeem: §2.1 (de keten), §2.3–2.4 (sjabloon en rekenregels) en bijlage A (technische adressen).

**Begrippen**

| Term | Betekenis in gewone taal |
|---|---|
| Referencia catastral (RC) | Kadastraal nummer van een perceel (14 tekens) of van een pand op dat perceel (20 tekens) |
| Catastro | Belastingkadaster: ligging, vorm, oppervlakte en bebouwing. Geen bewijs van eigendom, bouwrecht of legaliteit |
| Registro de la Propiedad · finca | Eigendomsregister · een perceel zoals het daar is ingeschreven |
| Nota simple | Uittreksel uit het eigendomsregister: omschrijving, eigenaar en ingeschreven lasten; alleen informatief |
| Cargas · servidumbre (de paso) | Ingeschreven lasten (hypotheek, beslag) · erfdienstbaarheid, bijvoorbeeld een recht van overpad |
| Informe urbanístico | Schriftelijke inlichting van de gemeente over bestemming, klasse en programmering van grond |
| Cédula de garantía urbanística | Gemeentelijke verklaring over de bouwregels van een perceel, maximaal 1 jaar geldig |
| PGOU · PGE · NUT | Geldend bestemmingsplan van Xàbia (1990/1991) · nieuw plan, niet in werking · tijdelijke noodregels uit 2021, geldigheid nu onbekend |
| Ordenanzas | De bouwvoorschriften bij een plan |
| Plan parcial (PP) · PRI · Estudio de Detalle (ED) | Deelplannen met eigen regels onder het PGOU |
| UA (unidad de actuación) | Plangebied dat als geheel bouwrijp moet worden gemaakt, met gedeelde lasten |
| Programa · PAI | Goedgekeurd uitvoeringsprogramma voor de urbanisatie van een gebied |
| Reparcelación | Herverkaveling: de grond in een plangebied wordt opnieuw verdeeld en de lasten worden omgeslagen |
| SU · SUZ · SNU | Stedelijke grond · urbaniseerbare grond · niet-bebouwbare (landelijke) grond |
| Urbano no consolidado | Stedelijke grond waar de urbanisatie nog niet af is |
| Solar | Bouwrijpe kavel: met toegang, water, stroom en afvoer |
| Urbanisatie · oplevering (recepción) | Wegen, riolering en nutsvoorzieningen van een wijk · de formele overdracht daarvan aan de gemeente |
| Aval de urbanización | Bankgarantie voor de nog niet uitgevoerde urbanisatiekosten |
| Cessie (cesión) | Grond die de eigenaar afstaat voor wegen en groen |
| Edificabilidad (m²t) | Maximaal meetellend vloeroppervlak, uitgedrukt in m² bouw per m² grond |
| Ocupación | Maximaal deel van het perceel dat overdekt of gesloten bebouwd mag worden |
| Grado | Subzone binnen zona E, met eigen bezetting en hoogte |
| Parcela mínima · frente | Minimumoppervlakte van een bouwkavel · minimale breedte aan de weg |
| Licencia (obra mayor) · DR | Bouwvergunning · *declaración responsable*: melding in plaats van vergunning |
| PEM | Kale bouwkosten, zonder algemene kosten, winst en btw |
| ICIO · tasa | Gemeentelijke bouwbelasting (4 % in Xàbia) · leges |
| ITP · AJD · btw (IVA) | Overdrachtsbelasting · aktebelasting · omzetbelasting |
| Valor de referencia | Door het Catastro vastgestelde minimumwaarde als belastinggrondslag |
| IBI | Jaarlijkse onroerendezaakbelasting |
| TRLOTUP · LH · LIVA | Valenciaanse wet op de ruimtelijke ordening (2021) · Spaanse hypotheekwet · Spaanse btw-wet |
| PATRICOVA · PORN Montgó · PATFOR · PATIVEL | Regionaal overstromingsplan · beheerplan natuurpark Montgó · regionaal bos- en brandplan · regionaal kustplan ("Litoral 1": geen nieuwbouw) |
| Red Natura 2000 · ZEC · ZEPA | Europese natuurgebieden |
| BIC · BRL · NHT | Beschermd erfgoed (hoogste niveau) · erfgoed van lokaal belang · historische kern |
| Costas: deslinde · servidumbre de protección | Grens van het openbare kustdomein · beschermingsstrook van 20 of 100 m landinwaarts |
| DPH | Openbaar domein van waterlopen |
| GVA · ICV | Generalitat Valenciana · haar kaartinstituut |
| Sareb · servicer | Staatsbeheerder van voormalig bankvastgoed · bedrijf dat dat vastgoed namens de eigenaar verkoopt |
| Pin | Coördinaat van een advertentie; vaak benaderend of verschoven |
| Open dienst (WFS, WMS, GetFeatureInfo) | Overheidsdienst die kaartgegevens op aanvraag teruggeeft; adressen in bijlage A |
| Perceelpolygoon · punt-in-polygoon · bbox | Omtrek van een perceel als lijst hoekpunten · toets of een punt binnen die omtrek valt · rechthoekig zoekgebied |
| EPSG · CRS | Code van een coördinatenstelsel (in graden of in meters) |

---

## 1. Conclusie

**Samenvatting (10 regels)**

1. De koppeling van advertentie → perceel → geldende regels → fysieke beperkingen → bouwscenario loopt in 13 stappen. De stappen 0–6 zijn grotendeels te automatiseren en de stappen 8 en 10 leveren automatisch signalen, met gratis officiële diensten zonder sleutel (Catastro, GVA/ICV, IDEE, IGME), die op 14 en 15-09-2026 live zijn getest [B1, B2, B3, B5]. De keten eindigt bewust in drie handmatige poorten: een **bevestigde kadastrale referentie** (makelaar of nota simple), **schriftelijke gemeentelijke informatie** (informe urbanístico of cédula, art. 246 TRLOTUP) en de **toets van een lokale architect**.
2. **Een pin is geen perceel.** De pins van één en dezelfde Garroferal-kavel (K07 en dubbels) liggen 129–340 m uit elkaar; de Rafalet-pin ligt 2,1 m van een perceelgrens; twee van vier geteste pins vielen in geen enkel perceel; een referencia catastral in een advertentietekst wees een perceel van 2.207 m² aan waar 1.500 m² werd geadverteerd [B2, type 3/5]. Regel: adres verborgen = hoogstens MIDDEL; bij MIDDEL of LAAG geen bouwconclusies.
3. **Geldend plan:** het PGOU van 1990/1991 met zijn modificaciones en planes parciales. Het nieuwe PGE (propuesta definitiva 30-04-2019) is **niet** in werking. Of de Normas Urbanísticas Transitorias (NUT, 2021) na ca. 15-03-2025 nog gelden, is onbekend (type 7) [B3, B4]. Veel urbanisaties vallen onder een eigen plan parcial dat niet in het GVA-register staat (bv. PP Ermita II), dus die normen moeten per perceel worden opgevraagd.
4. **Er bestaat geen bouwpercentage "voor heel Jávea".** Alleen voor percelen die feitelijk onder PGOU-zona E vallen, gelden: parcela mínima 500–1.500 m² per gebied, edificabilidad 0,142 m²t/m² bruto of 0,20 m²t/m² netto, ocupación 20/30/50 % per grado [percentages te verifiëren op het Mod. I-blad], 1–2 bouwlagen, 5 m tot grenzen [B3, B4]. Edificabilidad (totaal meetellend vloeroppervlak) en ocupación (footprint) zijn twee afzonderlijke plafonds; nooit nogmaals met het aantal bouwlagen vermenigvuldigen.
5. **Suelo no urbanizable en urbanizable zonder goedgekeurd programa hebben voor een gewone koper feitelijk geen woonbouwwaarde.** Een nieuwe woning in SNU vraagt ≥ 1 ha, ≤ 2 % bebouwing én een gunstig rapport van de Conselleria van Landbouw, dat alleen wordt gegeven bij een agrarisch bedrijf (≥ 1 UTA) of een beroepsboer (art. 211.1.b); op urbanizable zonder programa zijn woningen verboden (art. 226) [B4, type 2; gevolg type 4, te bevestigen door een urbanismo-advocaat].
6. **Sectorale toets vóór de financiële analyse.** Vier lagen die een deal direct kunnen breken zijn per perceel automatisch te bevragen: PATRICOVA, PORN Montgó, Red Natura 2000 met zonering en de planklasse; daarnaast PATFOR/brand, PATIVEL, BIC/BRL en geologie [B5, B6]. De kustdeslinde en de SNCZI-kaarten van MITECO waren onbereikbaar: de 20 m/100 m-kusttoets is daarom **ONBEKEND**. Wegen (carreteras), toegang en erfdienstbaarheden zijn in geen enkele onderzoeksstroom getoetst: die komen alleen uit de nota simple, de verkoper en een bezoek ter plaatse [B3, B1].
7. **K07 Garroferal (505.000 €, 1.570 m², licentie geclaimd) komt het verst.** Het meest waarschijnlijke perceel is 0281202BC5908S (onbebouwd, 1.567 m²), gevonden via een dubbele advertentie met zichtbaar adres. Die koppeling is niet bevestigd (type 4). De planlaag geeft PP Ermita II (SUZ) of SU, afhankelijk van welke pin je gebruikt; grondverzet vraagt een PORN-rapport; de "aval de la urbanización" wijst op een niet-opgeleverde urbanisatie. **Stop: "Bouwmogelijkheden nog niet betrouwbaar te bepalen: exacte perceelidentificatie ontbreekt."**
8. **K08 El Rafalet (150.000 €, eigendom van een SL, licentie geclaimd):** twee kandidaat-percelen (2944017 via de pin, 2944012 via de oppervlakte van 1.120 m²), en de GVA-laag geeft SUZ terwijl de advertentie "parcela urbana" zegt. Zelfde stop, plus een open klassevraag (type 7). **K10** (16 kavels, 17.775 m², 725.000 €) is waarschijnlijk hetzelfde object als Idealista 111869151 en het Sareb-perceel A "UA Balcón al Mar 1" bij Servihabitat (type 4): klasse tegenstrijdig (urbanizable of urbano no consolidado, type 7), alleen voor professionals, en btw in plaats van ITP [B9, B11, B12].
9. De documenten die deze stops opheffen zijn goedkoop, maar vragen akkoord van Jan: RC, licentie en project via de makelaar; een nota simple (9,02 € + btw per finca volgens het Colegio) [B2]; een informe urbanístico (wettelijke termijn 1 maand, tasa ONBEKEND) [B3]; en de ordenanzas van het plan parcial.
10. **Drie besluiten voor Jan** (zie hieronder): de aanbieders van K07, K08 en K10 laten benaderen, een eerste nota simple en informe urbanístico laten aanvragen, en het laagvolume-gebruik van de open overheidsdiensten als eerste filter goedkeuren.

**Wat Jan nu moet beslissen**

Deze besluiten worden niet los voorgelegd: de geconsolideerde top-3 vragen voor alle vijf deliverables staat in deliverable 01 §1.2 (besluit 1 en 2 vallen onder vraag 3 daar; besluit 3 volgt in ronde 2, samen met de technische vraag uit deliverable 05).

| # | Besluit | Waarom nu | Kosten/risico |
|---|---|---|---|
| 1 | ⏸️ ACTIE VOOR JAN — akkoord om de aanbieders van K07 (Atina Inmobiliaria en/of via de BP-relatie, ref. 4676JAV) en K08 (Grupo García) te vragen om: referencia catastral, kopie van de licentie (nummer, datum, voorwaarden, termijnen), het project en, bij K07, het bewijs van de aval; en Servihabitat (K10) om de 16 referencias catastrales, de ficha en het reglement van de biedprocedure | Zonder RC stopt de keten bij stap 6; bij K07/K08 is de licentieclaim de hele dealhypothese, bij K10 bepaalt de klasse of het S0 of S5 wordt | Geen kosten; een bericht namens TREE gaat pas uit na Jans "ja" |
| 2 | ⏸️ ACTIE VOOR JAN — akkoord voor een nota simple per bevestigd perceel (eerst K07) en voor één **informe urbanístico** via een lokale architect of de OAC Urbanismo, met de vragen uit §5.3 | Dit is de lakmoesproef voor de hele checklist van §16 | Nota simple 9,02 € + btw per finca [B2]; aanvraag wordt 3 jaar op naam van de aanvrager bewaard; tasa informe en architecthonorarium ONBEKEND |
| 3 | Akkoord dat de Deal Hunter de open diensten van Catastro en GVA/ICV **per kandidaat en in laag volume** automatisch gebruikt als eerste filter, met bronvermelding en zonder de originele Catastro-gegevens aan derden door te geven | Stappen 2–5, 8 en 10 zijn anders handwerk per object | Catastro weigert bij overschrijding van een onbekende drempel de dienst "generalmente 10 días" [B2]; Catastro-licentie verbiedt verspreiding van ongewijzigde gegevens [B2] |

---

## 2. Onderbouwing

### 2.1 De keten stap voor stap

Overzicht (details per stap hieronder):

| Stap | Wat | Automatisch | Handmatig / architect / gemeente | Zekerheid na de stap |
|---|---|---|---|---|
| 0 | Advertentie inlezen en normaliseren | ja | — | bronfeiten type 1 |
| 1 | Objectidentiteit: advertenties samenvoegen | voorstel | twijfelgevallen door mens | type 4 |
| 2 | Referencia catastral uit de tekst | ja | — | kandidaat |
| 3 | Adres → referencia catastral | ja | — | kandidaat |
| 4 | Coördinaat → kandidaat-percelen | ja | — | kandidaten |
| 5 | Kandidaten toetsen (geometrie, oppervlakte, bebouwing) | ja | — | type 3/5 |
| 6 | Zekerheidsniveau HOOG / MIDDEL / LAAG | ja | kalibratie | HOOG/MIDDEL/LAAG |
| **7** | **Poort 1: perceel bevestigen** | nee | makelaar, Sede-kaart, nota simple | HOOG (type 2/3) |
| 8 | Planologische eerste filter (GVA-laag) | ja, als signaal | zonering in het dossier na poort 2 | informatief (type 3) |
| 9 | Geldend document, zone en parameters | regeltabel | plankaarten B.1/B.2, plan parcial | type 2 (tekst) / 4 (toepassing) |
| 10 | Sectorale lagen, wegen, toegang | ja (lagen) | onbereikbare diensten, wegen, toegang en erfdienstbaarheden handmatig | signalen (type 3) of "niet getoetst" |
| 11 | Fysieke haalbaarheid, toegangsroute en bouwvlak | deels | topógrafo, architect, bezoek ter plaatse | type 5 → 6 |
| **12** | **Poort 2: schriftelijke gemeentelijke informatie** | nee | informe urbanístico / cédula / licentiedossier | type 2 |
| **13** | **Poort 3: bouwmogelijkhedenoverzicht en scenario's toetsen** | sjabloon | lokale architect | type 6 |

Een stap mag pas worden overgeslagen als de uitkomst ervan al met een hoger bewijstype vastligt. Na een MIDDEL of LAAG in stap 6 gaan stap 8 en 10 wél door (als signaal voor de beslissing om geld aan poort 1 te besteden), maar stap 9, 11 en 13 niet.

#### Stap 0 — Advertentie inlezen en normaliseren
- **Input:** Idealista-assistent (propertyCode, prijs, gestructureerde m², lat/long, `showAddress`, beschrijving, "situación urbanística", energielabel) en de BP-feed (ref, price, plotArea, latitude/longitude, locationDetail, desc).
- **Bron en test:** Idealista-assistent via MCP [B9, B10]. Eigen BP-dienst [E0], zelf gelezen op 15-09-2026 03:59: 56 objecten (Villa 26, Land 24, Apartment 4, 2 zonder type); 4676JAV plotArea 1.570, pin 38,794232 / 0,119842; 4104JAV plotArea 1.100, **zonder coördinaten** [C64, type 3]. Het townfilter is accentgevoelig: "Jávea" en "Xabia" geven 0 [B10]. Van 40 BP-Jávea-objecten met coördinaten hebben er 3 een nepcoördinaat in Florida en ligt er 1 buiten de gemeente [B6, type 3].
- **Output:** één record per advertentie, met elk m²-getal apart (veld, tekst, BP; nooit overschrijven), prijscomponenten gescheiden (grond, licentie, project, aval), alle stedenbouwkundige teksten als claim (type 1) en signalen voor het objecttype ("Inmueble exento", "imagen generada por IA", renders).
- **Regels:** gemeente = INE 03082; plaatsnamen normaliseren (Javea/Jávea/Xàbia/Xabia). Bij Idealista altijd `locationName`/`subtitle` controleren: een zoekopdracht "casco antiguo de Jávea" landde in Pamplona [B10]. Gestructureerde velden zijn geen bewijs: K07 en K08 staan als "Terreno urbanizable / Calificado para otra", terwijl de tekst "parcela urbana" of "solar" zegt [B10].
- **Wie:** automatisch.

#### Stap 1 — Objectidentiteit: advertenties samenvoegen
- **Input:** records uit stap 0.
- **Bron en test:** K07 staat onder minstens 10 Idealista-codes met vraagprijzen van 500.000 tot 550.000 € [B10, type 3]; twee advertenties op Calle Mar Amarillo 5 (150.000 en 160.000 €) blijken één perceel [B1, B2]; een dubbel met afwijkende m² (239 tegen 269) wordt door matching op prijs + m² gemist [B10]. K10 staat onder twee Idealista-codes én bij servicer Servihabitat, met een **andere planklasse** per kanaal [B9, B12]: het samenvoegen moet dus ook over portalen en servicerkanalen heen, en een klasseverschil binnen een cluster is een signaal, geen fout om weg te poetsen.
- **Output:** objectcluster met alle bron-ID's en prijzen zichtbaar, plus het beste adres en de beste pin uit het cluster. Een pin die exact op het Catastro-referentiepunt van een perceel valt, is een sterk signaal dat hij uit het Catastro is overgenomen [B2 A10, type 3/4].
- **Waarom vóór Catastro:** de werkelijke kavel van een advertentie met verborgen adres kan 129 m van de pin liggen en valt dan buiten elke zoekstraal van stap 4 [B2 A9/F10].
- **Zekerheid:** type 4. **Wie:** automatisch voorstel (prijs, m² uit veld én tekst, bebouwbare m², straat, tekstgelijkenis); twijfelgevallen door een mens.

#### Stap 2 — Referencia catastral uit de tekst
- **Input:** beschrijving. Het systeem zoekt naar tekenreeksen met de vorm van een kadastraal nummer (patroon in bijlage A, E1) [B1]. Landelijke percelen hebben een ander nummerformaat [B5]; de Catastro-dienst voor landelijke percelen is niet getest [B2 A14].
- **Bron:** Catastro-dienst "gegevens bij een RC" [E1, C4] (open, zonder sleutel).
- **Test:** advertentie 103305763 noemt RC 8989318BC4988N0001XX; die hoort bij CL CAPRICORNIO 1, onbebouwd, 2.207 m², terwijl de advertentie 1.500 m² noemt; de pin valt in een ander perceel [B2 A8, type 1 en 3].
- **Output:** kandidaat met herkomst "tekst". **Zekerheid:** nooit HOOG zonder oppervlaktecheck. **Wie:** automatisch.

#### Stap 3 — Adres → referencia catastral
- **Input:** straat en huisnummer (alleen als `showAddress=true` of uit een dubbele advertentie in het cluster).
- **Bron:** Catastro-dienst "RC bij een adres" [E2, C5] (open, zonder sleutel).
- **Tests:** MAR AMARILLO 5 → 2944002BC5924S, perceel 1.060 m² [B1, B2]; PIC DE REBALSADORS 30 → 0281202BC5908S, "suelos sin edificar", 1.567 m², gebouwd 0 m² [B2]; MAR AMARILLO 4 → 2944017BC5924S [B1]. Alles type 3.
- **Output:** kandidaat met herkomst "adres". **Zekerheid:** HOOG mogelijk na oppervlaktecheck, maar alleen voor de advertentie die dat adres zelf toont. **Wie:** automatisch.

#### Stap 4 — Coördinaat → kandidaat-percelen
- **Bronnen:** Catastro-dienst "percelen rond een coördinaat, met afstand" [E3, C2]; aanvullend de Catastro-kaartdienst voor alle percelen in een rechthoek [E4, C7]. Eén variant van de dienst werkt op ongedocumenteerde parameternamen; dat moet met een automatische test worden bewaakt [B2].
- **Tests:** Rafalet-pin → 2944017 op 0 m, 2944010 op 2,7 m, 2944012 op 7,57 m, 2944011 op 10,57 m, 2944013 op 20,81 m; rechthoek 60 × 60 m: 7 percelen van 749–1.120 m² [B1, B2]. Pin van Mar Amarillo 5: in geen enkel perceel, het perceel met huisnummer 5 is pas de vierde kandidaat (9,29 m) [B2]. Een rechthoek van ca. 0,87 km² meldde 486 percelen maar leverde er 477; de dienst geeft geen vervolgpagina's [B2]. Alles type 3.
- **Output:** kandidatenlijst met afstand tot de pin (straal 25 m) plus de kandidaten uit stap 1–3. **Wie:** automatisch.

#### Stap 5 — Kandidaten toetsen
- **Bronnen:** Catastro-kaartdienst "omtrek van één perceel" [E5, C7]; Catastro-dienst "gegevens bij een RC" voor gebruik, gebouwde m², bouwjaar en perceel-m² [E1, B2]; Catastro-kaartdienst "gebouwen op een perceel" [E6, C8].
- **Tests:** 0281206BC5908S: Catastro-oppervlakte 1.572 m², eigen berekening uit de hoekpunten 1.572,6 m², villa uit 2006, 348 m² gebouwd; 2944017: pin ligt binnen het perceel, 2,13 m van de grens [B1, B2, type 3/5]. Valkuil bij het omrekenen van coördinaten: zie bijlage A, E5 [B2].
- **Output per kandidaat:** pin in perceel (ja/nee), afstand tot de grens, oppervlakteafwijking in %, bebouwd (ja/nee, bouwjaar, m²).
- **Wie:** automatisch; alles met de standaardbibliotheek in de Hermes-venv, getest [B1, B2]. Catastro-m² zijn geen stedenbouwkundig meetellende m² (bij 0281206 tellen ook 47 m² "deportes aire libre" en 54 m² "anejos" mee) [B1; gevolg type 4].

#### Stap 6 — Zekerheidsniveau (regels na tegenspraak)

| Niveau | Voorwaarden (alle) | Voorbeeld |
|---|---|---|
| **HOOG** | precies één kandidaat met ≤ 3 % oppervlakteafwijking; én adres-match van déze advertentie, of een RC uit de tekst die de oppervlaktecheck doorstaat, of pin in het perceel met grensafstand ≥ 5 m bij zichtbaar adres; én objecttype strookt met Catastro; én geen andere advertentie in het cluster wijst een ander perceel aan | Mar Amarillo 5 via adres: 1.060 tegen 1.060 m² [B1, B2] |
| **MIDDEL** | één kandidaat ≤ 3 % maar grensafstand < 5 m; óf twee kandidaten binnen ±10 %; óf de koppeling loopt via een dubbele advertentie (type 4); óf het adres is verborgen (plafond) | Rafalet-pin: 2944017 (1.074 m²) en 2944012 (1.120 m²), pin 2,1 m van de grens [B2] |
| **LAAG** | pin in geen perceel en ≥ 2 kandidaten binnen 10 m zonder adres; óf geen kandidaat binnen ±10 %; óf oppervlakte ontbreekt; óf objecttype botst met Catastro zonder verklaring | Pic de Rebalsadors s/n: pin buiten percelen, 3 kandidaten binnen 8 m [B1]; 112256480: pin in bebouwd perceel, advertentie "terreno" met 310 m² bebouwbaar [B2] |

- Gelijke oppervlaktes in een verkaveling onderscheiden niets (1.567 tegen 1.572 m²) [B2 A9]. De drempels 3 %, 5 m en 25 m zijn ontwerpaannames (type 4), te kalibreren op de eerste 30 dossiers [B1].
- **Output bij MIDDEL of LAAG:** de vaste dossierregel "Bouwmogelijkheden nog niet betrouwbaar te bepalen: exacte perceelidentificatie ontbreekt", de kandidatenlijst, en welk document de koppeling sluit.

#### Stap 7 — Poort 1: perceel bevestigen
- **Routes (rechtmatig):** (a) de verkoper of makelaar om de RC vragen; die staat op elk IBI-aanslagbiljet [B1]; (b) de Sede-kaart en de PDF "Consulta descriptiva y gráfica" [E7] (zonder login, 234 KB; letterlijk "no es una certificación catastral"; interactieve dienst, dus alleen handmatig) [B2, C15]; (c) een nota simple via registradores.org: 9,02 € + btw per finca, levertijd tegenstrijdig ("24 horas" tegenover "inferior a dos horas"), legitiem belang vereist, aanvrager wordt 3 jaar bewaard [B2, C17, C18].
- **Waarom de nota simple beslissend is:** art. 10.4 Ley Hipotecaria verplicht elke registerpublicatie de RC te vermelden en of de finca grafisch met het Catastro is gecoördineerd [B2, C19, type 2]. Of dat in de praktijk altijd gebeurt: [te verifiëren] bij de eerste nota.
- **Lasten en erfdienstbaarheden:** nota simple en certificación bevatten volgens het Colegio "la descripción de la finca, la titularidad y las posibles cargas" [B2 R11-14, type 2]. Het Catastro toont geen lasten [B1 §2.3, type 3]. Of ingeschreven erfdienstbaarheden (bijvoorbeeld een recht van overpad, voor of tegen het perceel) altijd in de nota simple zichtbaar zijn, is in geen onderzoeksstroom gecontroleerd: [te verifiëren] bij de eerste nota. Niet-ingeschreven feitelijke paden of leidingen zie je alleen ter plaatse of via de verkoper (type 4).
- **Output:** bevestigde RC (HOOG), eigendom, lasten (met aparte regel voor erfdienstbaarheden en afecciones urbanísticas), registrale oppervlakte, coördinatiestatus. **Wie:** handmatig, na akkoord van Jan over kosten en contact.

#### Stap 8 — Planologische eerste filter
- **Bron:** GVA/ICV-kaartdienst planeamiento (klasse en zonering) [E8]; voorwaarden "No se aplican condiciones", licentie "CC BY 4.0 Generalitat"; laag bijgewerkt 25-08-2026; disclaimer "carácter informativo" [B3, B4, C27, C28]. R12 en R13 kregen alleen antwoord met verschillende instellingen van het zoekgebied; die instelling moet dus met een automatische test worden vastgelegd [B3, B5] (details E8).
- **Tests:** K07 Idealista-pin → PP "ERMITA II", SUZ, ZND-RE; K07 BP-pin (152 m verderop) → twee vlakken, PP Ermita II én "Plan general SU ZUR-RE"; Villes del Vent: BP-pin → PP Cansalades-Umbría, Idealista-pin (118 m verderop) → SNU-P ZRP-NA-MU [B4, B6]. De laag bevat nog 20 vlakken van de door de TSJCV vernietigde Portitxol-homologación [B4]. Op de K07-pin noemt de GVA-inventarislaag "Plan Parcial Montgó-2 / SUP Montgó-2": twee GVA-lagen spreken elkaar tegen (type 7) [B5].
- **Juiste gebruik:** de perceelpolygoon uit stap 5 tegen de zonevlakken leggen, nooit de pin [B4 A2]. Wat vandaag met de bestaande gereedschapskist kan en wat niet:
  - *Welke* zonevlakken het perceel raken: een kaartvraag met de perceelomtrek aan de GVA-kaartdienst [E8, E9], door R13 getest met de gemeentegrens als omtrek [B5 §3.4 en §11, type 3].
  - *Hoeveel procent* van het perceel in elk vlak ligt: met de standaardbibliotheek alleen **benaderend**, door een raster van punten over het perceel te leggen, zoals R13 dat voor PATRICOVA deed (type 5) [B5]. Een exacte snijding van twee omtrekken kan de standaardbibliotheek niet. Deliverable 05 §3.4 noemt twee routes zonder installatie, een ArcGIS-`query` met de perceelpolygoon of eigen code, die allebei nog niet getest zijn; lukt geen van beide, dan is een geometriebibliotheek zoals `shapely` nodig, met installatie-akkoord van Jan. PostGIS is voor fase B geen voorwaarde (05 Deel 4) [B13 §2.4 en §4.1, B14 R17-05].
- **Afstemming met deliverable 05 (afgestemd 15-09-2026):** deliverable 05 §3.4 volgt deze stap: in fase B geeft de planlaag automatisch een **signaal** op de perceelpolygoon (welke vlakken, benaderend aandeel). Handmatige zoneringsinvoer per dossier is niet de hoofdroute meer, en "polygonen snijden" is in 05 Deel 4 geen overstapmoment naar PostGIS meer. De zonering die als dossierfeit telt, komt pas uit poort 2 (informe urbanístico). Raakt het perceel meer dan één zonevlak, dan beslist een mens. Een exact overlappercentage als dossierfeit komt pas nadat een van de routes uit 05 §3.4 een regressietest haalt [B13].
- **Output:** klasse, zonecode, instrument, geraakte vlakken en benaderend aandeel (met methode). **Zekerheid:** laaguitslag type 3, aandeel type 5, juridisch informatief. **Wie:** automatisch als signaal; zonering als dossierfeit pas na poort 2.

#### Stap 9 — Geldend document, zone en parameters
- **Bronnen:** GVA-register Xàbia (open directory) [C21]; PGOU-ordenanzas, 240 blz. scan zonder tekstlaag [C22]; Mod. XXV (BOP nº 240, 16-12-2016) [C23]; DOGV 9041 en 9177 (schorsing en NUT) [C24, C25]; TRLOTUP geconsolideerd tot 02-07-2026 [C26].
- **Hoe:** (1) klasse en instrument uit stap 8, gecontroleerd tegen het register; ligt het perceel in een plan parcial, PRI, homologación of UA, dan gelden eerst díe normen [B3]; (2) zone en grado uit plano B.1 ("letras A–H"; zonder letter = E2) [B3, B4]; (3) gebied voor parcela mínima en edificabilidad uit plano B.2 [B3]; (4) modificaciones per gebied; (5) status van elk document (§2.2).
- **Beperking vandaag:** B.1, B.2 en B.3 zijn scans, niet gegeorefereerd en door niemand per perceel gelezen [B4]. PP Ermita II en PP La Guardia-3 staan niet in het register [B3].
- **Output:** regelset met document, versie, datum, artikel, blad, zone en status. **Zekerheid:** tekst type 2, toepassing type 4 → 6 na architect. **Wie:** regeltabel automatisch (PGOU zona E en SNU, versiebeheerd met bronpagina); zone- en planbepaling handmatig.

#### Stap 10 — Sectorale lagen (per perceelpolygoon)

| Laag | Juridische werking | Dienst (adres in bijlage A) | Testresultaat | Waarschuwing |
|---|---|---|---|---|
| PATRICOVA gevaar 1–6 + geomorfologisch | bindend (art. 3); SNU niveau 2–5 + geomorf.: woningen verboden (18.2); SU: eisen met bijlage I als referentie (20) [C34] | GVA/ICV infraestructura verde en ArcGIS ordenación territorial [E9] | Arenal: niveau 4 (AC07, T100, < 0,8 m); Granadella en K07-pin: geen zone; ca. 827 ha (12 %) van Xàbia in niveau 1–6 [B6] | lokale inundabiliteitsstudies (laag 1) kunnen afwijken; niveau 1 staat niet in 18.2 |
| ARPSI (nationaal) | complementair aan PATRICOVA | IDEE overstromingsrisico [E10] | Arenal T100 = 1,951, eenheid niet vermeld; "999" is een onbekende code [B6] | tegenstrijdig met PATRICOVA < 0,8 m → hydraulisch deskundige |
| PORN Montgó | PORN art. 56 (bouwverbod park), 57, 109.5 (rapport Conselleria) [C36] | GVA/ICV PORN Montgó [E11] | K07-pin: in het ámbito, zone "Áreas urbanas y urbanizables", niet in het park [B6] | begrenzing "carácter informativo" |
| Red Natura 2000 + zonering | Decreto 197/2022 norma de gestión [C40] | GVA/ICV infraestructura verde en ArcGIS espacios protegidos [E12] | Granadella: ZEC/ZEPA Penya-segats, zone B [B6] | Montgó alleen als LIC in de laag |
| PATFOR en brand | PATFOR art. 28–32; TRLOTUP art. 7.4 (30 jaar), DA 7 + bijlage XI (strook 30 m, tot 50 % te verkleinen) [B6] | GVA/ICV PATFOR en ArcGIS prevención de incendios [E13] | K07-pin: geen bosgrond, interface "2 – Casos aislados", binnen ZIF 500 m en PPIF Montgó; Xàbia: interface-afbakening "Aprobado", pleno 28-05-2026 [B5, B6] | rastercel ±500 m; start van de 6-maandstermijn is afgeleid (type 4). DA 7.7–8 kent bij brandpreventie een gedwongen erfdienstbaarheid van toegang [B5 §4.2, type 2] |
| PATIVEL / kustplan | Decreto 58/2018 onder Ley 3/2025 [C41, C49] | ArcGIS ordenación territorial, kustlagen [E9] | ca. 59 ha Litoral 1 en 10 ha Litoral 2 rond Portitxol/Cap Negre [B6] | de ámbito-grenzen zijn **lijnen**: de toets "ligt het punt erin" geeft altijd 0; afstand berekenen |
| Costas: deslinde, servidumbre 100/20 m | Ley 22/1988 art. 23–30, DT 3ª–4ª; Ley 3/2025 art. 44–45 [C42, C41] | MITECO kustdomein [E14] | **niet getest**: serverfout, verbindingsreset, 503 [B6] | ONBEKEND; download `dpmt.zip` (12,2 MB, bijgewerkt 31-03-2026) vraagt akkoord. Signaal: de GVA-planlaag kent de zone SNU-P/ZRP-CT (kust), 2 vlakken in Xàbia [B3 §2.8, §3.1, type 3]; dat is geen deslinde |
| Waterlopen (DPH) | RDL 1/2001 art. 6: 5 m servidumbre, 100 m zona de policía [C43] | MITECO waterlopen [E15] | **niet getest** (zelfde storing) [B5] | een toponiemlijn is geen deslinde. Signaal: GVA-planzone SNU-P/ZRP-CA (waterlopen), 9 vlakken in Xàbia [B3 §2.8, §3.1, type 3] |
| **Wegen (carreteras)** | sectorwetgeving; in R12 gesignaleerd maar **niet onderzocht** [B3 §3.3]. Welke wegenwet per weg geldt en welke afstanden die oplegt: ONBEKEND | geen geteste dienst. Signaal: GVA-planzone SNU-P/ZRP-CR (wegen), 4 vlakken in Xàbia [B3 §2.8, §3.1, type 3] | niet getest | ONBEKEND. Afstand tot de weg en eventuele beschermingsstrook per perceel vragen in het informe urbanístico (G13) |
| **Toegang en erfdienstbaarheden** | solar vereist toegang (PGOU-ord. 8.1.6); kavel onder de uitzonderingsregel ≥ 3 m toegang (Mod. XXV); SNU: frente 20 m aan een kadastrale weg (PGOU); lasten staan in de nota simple [B3 §2.2, §3.2; B4 R12-08; B2 R11-14] | geen open dienst: nota simple (stap 7), Sede-kaart visueel [E7], bezoek ter plaatse | niet getest | of het perceel juridisch (openbare weg of ingeschreven overpad) en feitelijk bereikbaar is, ook voor bouwverkeer: ONBEKEND tot nota simple en bezoek. Catastro toont geen lasten [B1 §2.3] |
| Minimización SNU | TRLOTUP 228–231, DT 28 [C26] | GVA/ICV planeamiento, laag minimización [E16] | 585 percelen in Xàbia [B5; niet hercontroleerd in B6] | opname ≠ illegaal; ontbreken ≠ legaal |
| Erfgoed en archeologie | Ley 4/1998; TRLOTUP 232.f (vergunningplichtig), 233.1.a en c (geen DR bij beschermde elementen, hun omgeving en archeologische aandachtsgebieden), 240.1.c (termijn 3 maanden) [C48, B5 §8.1] | GVA/ICV erfgoedlagen [E17] | 10 BIC en 28 BRL in Xàbia, waaronder de archeologische zone "Yacimiento romano Illeta del Portichol" (BIC) [B5 §8.1; aantallen niet hercontroleerd in B6] | de gemeentelijke catálogo (Mod. XVII) met eventuele archeologische zones is **niet gelezen**: [te verifiëren]. "Geen BIC/BRL" is dus geen "geen archeologie" |
| Geologie | geen juridische werking | IGME geologische kaart 1:50.000 [E18] | K07-pin: "Depósitos aluviales, fondo de valle" [B5] | geen geotechnische dienst; IGME wil contact bij betaalde dienst met toegevoegde waarde |

- **Output:** per laag "signaal (laag, datum, bewijstype 3)" of "dienst onbereikbaar" of "niet getoetst" (wegen, toegang, erfdienstbaarheden, gemeentelijke catálogo). Nooit "geen beperking". **Wie:** automatisch, per laag gecachet [B5]; wegen, toegang en erfdienstbaarheden handmatig.

#### Stap 11 — Fysieke haalbaarheid, toegangsroute en bouwvlak
- **Input:** perceelgeometrie (stap 5), afstanden en perceeleisen (stap 9), topografie, lasten en erfdienstbaarheden uit de nota simple (stap 7), toegang en wegen uit stap 10.
- **Toegangsroute (masterprompt §14 en §17):** vastleggen (1) aan welke weg het perceel ligt en of die openbaar is; (2) de frente aan die weg (20 m, of 10 m aan een doodlopende weg; bij de uitzonderingsregel ≥ 3 m toegang) [B3, B4 R12-08]; (3) of de toegang via een ingeschreven erfdienstbaarheid over een ander perceel loopt (nota simple, [te verifiëren] of die altijd zichtbaar is); (4) of bouwverkeer het perceel kan bereiken (breedte, helling). Punt 1 en 4 staan in geen onderzoeksstroom: bezoek ter plaatse of topógrafo (type 3 na bezoek).
- **Bron:** afstanden en eisen uit de ordenanzas (5 m tot rooilijn en grens bij grado I/II, rechthoek 15 × 24 m, frente 20 m of 10 m aan een doodlopende weg) [B3, B4]; keermuren max. 2,5 m hoog (art. 8.1.23.2, [OCR]) [B3]; water en riolering via AMJASA, elektriciteit via i-DE (procedure AMJASA [te verifiëren]) [B5]; nutsbedrijven leveren alleen tegen vergunning (TRLOTUP art. 245) [B5]. Een hoogtemodel voor helling is in fase A **niet** getest.
- **Output:** bouwvlak (perceel min afstanden), rechthoek- en frontcontrole, hellings- en keermuurrisico, aansluitstatus, toegangsstatus (openbare weg ja/nee, frente, erfdienstbaarheid nodig of aanwezig, bereikbaar voor bouwverkeer).
- **Zekerheid:** type 5 → 6 na topografisch plan en architect. **Wie:** bouwvlak voor eenvoudige vormen automatisch met de standaardbibliotheek; buffers op onregelmatige vormen vragen `shapely` (installatie alleen met akkoord van Jan) [B1]; helling, grondverzet en aansluitingen handmatig.

#### Stap 12 — Poort 2: schriftelijke gemeentelijke informatie
- **Instrumenten (TRLOTUP, geconsolideerd tot 02-07-2026) [B3, B4, C26]:** informe urbanístico schriftelijk over zonering, classificatie en programmering, voor "cualquier solicitante", binnen 1 maand (art. 246.4); cédula de garantía urbanística binnen 1 maand, geldig max. 1 jaar, opgeschort tijdens een licentieschorsing, geeft recht op schadevergoeding bij planwijziging als er geen openstaande cessie-, verdelings- of urbanisatieplicht op staat (art. 246.1–3); of een koper-in-spe als "parte interesada" telt: [te verifiëren].
- **Daarnaast per perceel:** licentiedossier (start binnen 6 en afbouw binnen 24 maanden als de licentie niets anders zegt, art. 188.2; verval na hoorzitting, art. 244); stand van de oplevering van de urbanisatie (art. 168) en een eventuele aval (art. 187); ordenanzas van het plan parcial.
- **Loket:** sede electrónica Xàbia; de rubriek "2.3.4. Tasas" (27 documenten) is handmatig in een browser te openen, niet automatisch [B4]. Tasa voor informe, cédula en licentie: ONBEKEND [B3].
- **Wie:** ⏸️ ACTIE VOOR JAN of zijn architect.

#### Stap 13 — Poort 3: bouwmogelijkhedenoverzicht en scenario's
- Het sjabloon van §2.3 invullen, de rekenregels van §2.4 toepassen en de scenario's van §2.5 uitwerken. De lokale architect bevestigt de interpretaties (type 6). Pas daarna gaat het object naar de financiële analyse (§21–22 masterprompt).

### 2.2 Welke documenten gelden in Xàbia (status op 15-09-2026)

Masterprompt §15: nooit een toekomstig plan als geldend bouwrecht toepassen; per document de status vastleggen.

| Document | Versie en datum | Status | Toepassen als bouwrecht? | Bron |
|---|---|---|---|---|
| PGOU Xàbia ("Revisión-Adaptación del Plan General") | Comisión Provincial de Urbanismo 31-01-1990 (BOP 26-02-1990); restgebieden (La Granadella, SUP residencial intensivo) bij resolución 08-03-1991 (BOP nº 125, 03-06-1991; DOGV 1548, 22-05-1991) | vastgesteld, gepubliceerd, **in werking** | ja | [B3, B4, C24] type 2 |
| Ordenanzas van het PGOU | scan van 240 blz., "Març 1989" / "Texte refundit, Gener 1990", met vervangende bladen van Mod. I en een zona C-wijziging ("MOD. P. Nº 5") | in werking; **geen geconsolideerde tekst**: latere wijzigingen (o.a. Mod. 27, Mod. XXV) staan er niet in verwerkt | ja, per artikel, na controle op latere wijziging | [B3 §2.1, C22] type 2 |
| Modificaciones in het GVA-register | 32 wijzigingen/homologaciones plus PG en NUTU, o.a. Mod. I (DOGV 2227, 15-03-1994), Mod. 27 (DOGV 4665, 08-01-2004: art. 10.5.4 en 10.5.7), **Mod. XXV** (pleno 27-10-2016, BOP nº 240, 16-12-2016: art. 8.1.2, 8.1.3, 10.5.1.1), Mod. 71 (pleno 30-04-2019) | in werking per instrument; register onvolledig (nummering loopt tot ten minste 71). Bij Mod. XXV is alleen de goedkeuring van de wijziging van art. 8.1.6 opgeschort: het oude art. 8.1.6 geldt | ja, per instrument | [B3 §1.3, B4 R12-08/F6, C23] type 2 |
| Planes parciales, PRI's, UA's, homologaciones | per instrument; PP "Ermita II" (exp. 19940463) en PP "La Guardia-3" (exp. 19981338) staan in de GVA-laag **zonder** documenten in het register; het register kent o.a. "mod. PP La Guardia-1" en UA-wijzigingen (Mar Azul, ACM-26, CVM-2, Lluca-Rafalets 5 en 12, MC-11-A). De "PGOU UA BALCON AL MAR 1" die Servihabitat bij K10 noemt, staat **niet** in de door R12 overgenomen registerlijst (het register is onvolledig) | in werking per instrument; inhoud ONBEKEND waar niet in register | ja, na opvragen | [B3 §1.3, B11 §6] type 2/7 |
| Homologación modificativa Portitxol | CTU 03-05-2006 | **vernietigd** (TSJCV sentencia 459/2012, 26-04-2012); of die uitspraak onherroepelijk is, is niet gecontroleerd | nee | [B4 R12-17] type 2 |
| Gedeeltelijke schorsing PGOU | Acuerdo del Consell 05-03-2021 (DOGV 9041, 15-03-2021) | beëindigd, uiterlijk ca. 15-03-2025 (vier jaar na publicatie; datumberekening) | n.v.t. | [B4 R12-03] type 2/5 |
| Normas Urbanísticas Transitorias de Urgencia (NUT) | Acuerdo 10-09-2021 (DOGV 9177, 20-09-2021) | **type 7**: tekst zegt "hasta la aprobación del PGE", maar gekoppeld aan een schorsing die ca. 15-03-2025 eindigde. De Generalitat-brief van feb. 2025 (pers) gaat over de licentieschorsing 2017–2019, niet over de NUT | alleen na schriftelijke bevestiging | [B4 R12-04/F9, B6 R13-19] |
| Plan General Estructural (PGE) | propuesta definitiva, pleno 30-04-2019 | **in procedure**, niet goedgekeurd, niet gepubliceerd; volgens pers (feb. 2025) noemde de Generalitat het "carente de validez y eficacia" | **nee**; wel risico-informatie (declassificatie van ca. 8 mln m² urbanizable, nieuwe red primaria) | [B3, B4, C29, C30] type 2/1 |
| Mod. nº 41 PGOU (toeristische verhuur) | aanvankelijke goedkeuring pleno 28-05-2026 | in procedure; licentieschorsing voor meergezins-VUT na BOP-publicatie [te verifiëren in BOP] | nee (schorsing wel zodra gepubliceerd) | [B4 R12-20, C67] type 1 |
| TRLOTUP (Decreto Legislativo 1/2021) | geconsolideerd op boe.es tot 02-07-2026 (Ley 3/2026), "actualización en proceso" | **in werking** | ja | [B6 R13-01, C26] type 2 |
| Anteproyecto Ley del Suelo CV | openbare inzage aangekondigd 08-01-2026 | in procedure, niet van kracht | nee | [B5] type 2/1 |
| PATRICOVA (Decreto 201/2015) | normativa oktober 2015 | in werking, bindend (art. 3), onbepaalde geldigheid | ja | [B6 R13-04, C34] type 2 |
| PORN Montgó (Decreto 180/2002) | DOGV 4374, 08-11-2002 | in werking tot herziening (art. 12) | ja | [B6 R13-08, C36] type 2 |
| PATFOR (Decreto 58/2013) | DOGV 7019, 08-05-2013 | in werking; wijzigingen na 2013 niet gecontroleerd | ja [te verifiëren] | [B5] type 2 |
| PATIVEL (Decreto 58/2018) | versie GVA 04-06-2025; TS 491/2022 casseerde de nietigverklaring | **van kracht**, gedeeltelijke vernietigingen 2025–2026 raken Xàbia niet; Ley 3/2025 (in werking 15-06-2025) gaat voor bij strijdigheid; Plan de Ordenación Costera in voorbereiding (geen recht) | ja | [B6 R13-12/13, C41, C49] type 2 |
| Ley 22/1988 de Costas | geconsolideerd tot 11-12-2015 op boe.es | in werking | ja | [B6 R13-15, C42] type 2 |
| ZEC/ZEPA Penya-segats de la Marina (Decreto 197/2022) | DOGV 28-11-2022 | in werking (norma de gestión) | ja | [B6 R13-10, C40] type 2 |
| PLPIF Jávea | resolución 21-07-2020, 15 jaar met herziening per 5 jaar | in werking; status van de herziening van ca. juli 2025 onbekend | ja | [B6 R13-11, C68] type 2 |

### 2.3 Het verplichte bouwmogelijkhedenoverzicht (§16) als invulsjabloon

**Voorwaarde:** alleen invullen voor een perceel met zekerheid HOOG na poort 1 (stap 7). Anders staat bovenaan het dossier: "Bouwmogelijkheden nog niet betrouwbaar te bepalen: exacte perceelidentificatie ontbreekt."

**Vaste waarschuwing in elk dossier** [B3 §6]: "Uitkomst van de GVA-laag en de PGOU-tabellen is een eerste filter. Bouwrecht pas na informe urbanístico of cédula (art. 246 TRLOTUP), controle van plan parcial/UA, en toets door een lokale architect."

**Leeswijzer kolom "Huidig antwoord Xàbia":** dit is wat R12 en R13 in de documenten vonden. Het geldt **alleen** voor percelen die onder het genoemde regime vallen (meestal PGOU-zona E of SNU). Voor een perceel in een plan parcial of UA is het antwoord ONBEKEND tot die ordenanzas zijn gelezen. Documentcodes: **PGOU-ord.** = ordenanzas PGOU (vastgesteld 1990/1991, in werking; scan in het GVA-register [C22]); **TRLOTUP** = DL 1/2021, geconsolideerd tot 02-07-2026, in werking [C26]. [OCR] = alleen via tekstherkenning gelezen, niet visueel gecontroleerd.

#### A. Wat is planologisch toegestaan?

| # | Onderdeel (§16) | Waar komt het antwoord vandaan | Huidig antwoord Xàbia (document · artikel · datum · status) | Autom.? | Type na afronding |
|---|---|---|---|---|---|
| 1 | Geldende grondclassificatie en bestemming | plano A.1/B.1 PGOU + instrument (PP/PRI/UA); GVA-WFS als filter; **informe urbanístico** (TRLOTUP art. 246.4) | Klassen SU / SUZ / SNU. GVA-laag (bijgewerkt 25-08-2026, informatief): 356 zonevlakken, o.a. SUZ ZND-RE 140, SU ZUR-RE 126, SNU-P 57, SNU-C 12, SU ZUR-NHT 5 [B3 §2.8, B4 R12-17]. Per perceel: pas vast na informe | filter ja | 3 (laag) → 2 (informe) |
| 2 | Toegestane hoofd- en nevenfuncties | PGOU-ord. titel X per zone; PP-ordenanzas; TRLOTUP 210–216 (SNU) | Zona E: "Uso global: residencia unifamiliar. Edificación aislada" (art. 10.5.4, tekst Mod. 27, DOGV 08-01-2004). Nevenfuncties onder voorwaarden: commercieel/recreatief/hotel alleen aan een weg > 10 m; hotel buiten hoofdwegen alleen 4–5 sterren, perceel ≥ 5.000 m², max. 1.500 m²; niet-woonfuncties ≥ 10 m tot grenzen (art. 10.5.7) [B3 §2.3c]. SNU: woning alleen onder 211.1.b (zie #6). PP: ONBEKEND | deels | 2 |
| 3 | Status van bouwrijpheid | PGOU-ord. 8.1.6 (solar); TRLOTUP 168 (oplevering), 186–187; gemeente: recepción-akte; ter plaatse | Solar in extensief gebied: water, stroom, toegang en zuivering volgens 10.5.2.3 (oud art. 8.1.6 geldt). Bouwen vóór oplevering van de urbanisatie alleen met aval voor de volledige urbanisatiekosten en zonder gebruik vóór oplevering; die voorwaarde gaat mee bij verkoop (TRLOTUP 187.1). Gemeentelijke lijst niet-opgeleverde urbanisaties dateert van 2013 (o.a. Pou de Moro I, Adsubia-Rebaldí 29, La Cala) en is verouderd [B3 §5, B4 R12-16] | nee | 2 + 3 |
| 4 | Minimumperceel en andere perceelvereisten | PGOU-ord. tabel 10.5.1.1 (full nº 145–146) + plano B.2; Mod. XXV (BOP 16-12-2016) | Zona E per gebied: 500 m² (Caleta-Puerto) tot 1.500 m² (o.a. Montgó, Montgó-Ermita, -Castellans, -Barranqueres, Lluca, Covatelles, Senioles, Valls); 1.000 m² o.a. Tosalet, Balcón al Mar, Cap Martí, Adsubia-gebieden, Lluca-Rafalet. Frente 20 m (doodlopende weg 10 m); rechthoek 15 × 24 m moet passen; uitzondering bij bestaande kavels: > 70 % van het minimum en ≥ 700 m², met ≥ 3 m toegang (Mod. XXV) [B3 §2.3a–b, B4 R12-05/08]. Latere wijzigingen per gebied niet uitgesloten | tabel ja; geometrie ja | 2 / 5 |
| 5 | Splitsen of samenvoegen | TRLOTUP 247–248; PGOU-ord. 8.1.3 (Mod. XXV) | Percelen kleiner dan tweemaal het minimum zijn ondeelbaar (248.c); splitsing vraagt een licencia de parcelación, beslistermijn 1 maand (240.1.a); samenvoegingen die het aantal woningen verlagen zijn toegestaan (8.1.3). Urbanizable zonder programa: niet splitsbaar (248.e). PORN Les Planes: splitsen verboden [B3, B4, B6] | rekenregel ja | 2 / 5 |
| 6 | Toegestaan aantal woningen of eenheden | PGOU-ord. 10.5.4–10.5.6; casco plano B.1 + NHT; TRLOTUP 211.1.b | Zona E: één vrijstaande woning per perceel. Meer alleen via Estudio de Detalle: **agrupación** (10.5.5: perceel ≥ 5.000 m², ≥ 100 m² per woning, groepen max. 10, niet meer woningen dan bij losse verkaveling) of **parcela mancomunada** (10.5.6: perceel ≥ 1,3 × n × parcela mínima, 10 m tussen woningen, ondeelbaar ingeschreven) [B3 §2.3c, deels OCR]. SNU: geen groepering op één perceel (211.1.b.5) | rekenregel ja; ED nee | 2 / 5 |
| 7 | Edificabilidad | PGOU-ord. 4.1.8–4.1.9, 8.1.13–8.1.15; PP-ordenanzas | Zona E: **0,142 m²t/m² bruto = 0,20 m²t/m² netto** (verschil = 29,07 % cessies); gebieden Calvario, Puchol, Soberana, Mesquides, Cuesta S. Antonio, Caleta-Puerto (en La Corona, Mod. I): 0,198 bruto / 0,28 netto; zones C, F, G, H: 0,58 / 1 (full nº 37, visueel) [B3 §2.2, B4 R12-06]. SNU PGOU grado I/II 0,03 m²/m² (max. 300 m²), maar TRLOTUP beperkt tot 2 % bezetting en 1 ha. **Interpretatievraag:** netto direct op een bestaande kavel of eerst cessie aantonen? | ja, met aanname | 5 → 6 |
| 8 | Ocupación | PGOU-ord. 8.1.5; tabel zona E per grado (plano B.1) | Ocupación = overdekte of gesloten oppervlakte t.o.v. het **totale** perceel (8.1.5). Zona E: grado I 20 %, II 30 %, III 50 % — **alleen zichtbaar op het doorgehaalde oorspronkelijke blad** (full nº 147); op het vervangende Mod. I-blad afgedekt door een stempel [te verifiëren] [B4 R12-07]. Zone C: 70/50/50/50 % [OCR]. SNU: ≤ 2 % (211.1.b.2) | ja, met aanname grado | 5 → 2 |
| 9 | Maximale bouwhoogte en bouwlagen | PGOU-ord. 10.5.1.4, 8.1.19, 8.1.26; casco plano B.1 + NUT; TRLOTUP 210.2 | Zona E grado I: 1 laag, kroonlijst 3,5 m, totaal 6,00 m; grado II/III: 2 lagen, 7 m, 9,50 m (Mod. I-blad 114-B, visueel). Semisótanos en ruimte onder hellend dak tellen niet als laag (8.1.19, [OCR]). Casco (Mod. I): per blok volgens B.1, II t/m V lagen (kroonlijst 6,1–15,0 m); NUT NHT: PB+I+cambra (status NUT type 7). SNU: max. 2 lagen (210.2) [B3, B4 R12-07/18] | deels | 2 |

#### B. Welke technische eisen gelden voor het beoogde gebouw?

| # | Onderdeel (§16) | Waar komt het antwoord vandaan | Huidig antwoord Xàbia | Autom.? | Type |
|---|---|---|---|---|---|
| 10 | Rooilijnen en afstanden tot perceelgrenzen | plano B.3 (alineaciones, niet gelezen); PGOU-ord. 10.5.1.5; 8.1.27.D; topografische meting | Zona E grado I en II: 5 m tot rooilijn en 5 m tot grens; grado III: 0 m en 2,5 m. Kelders en hellingbanen onder maaiveld ≥ 2,5 m van de grens (8.1.27.D, Mod. I). SNU PGOU: 10 m tot grenzen. Casco: geen terugliggende gevels [B3, B4] | nee | 2 + 3 |
| 11 | Kelders en ondergrondse ruimten | PGOU-ord. 8.1.15.a, 8.1.19, 8.1.27; NUT NT 2; PATRICOVA bijlage I | Buiten zone A/B: kelder = bouwdeel **onder de footprint** met bovenkant plafond < 1,20 m boven natuurlijk terrein op alle punten van de omtrek; telt niet mee voor edificabilidad; ≥ 2,5 m van de grens (Mod. I). Casco: één kelder binnen het bezetbare oppervlak (Mod. I), maar NUT: nieuwe semisótanos verboden (status 7). PATRICOVA niveaus 3, 4, 6: geen kelder of semi-kelder (bijlage I-B; in SU als "referencia") [B3, B5] | nee | 2 → 6 |
| 12 | Naya's, terrassen en overkappingen | PGOU-ord. 8.1.5, 8.1.15.b; 10.5.1.7 | Geen aparte regel voor zona E. Overdekt = bezet (8.1.5). Overdekte terrassen tellen mee voor edificabilidad, "se considerará la mitad cuando sean terrazas cubiertas y no esté cerrado por alguno de sus frentes" (8.1.15, visueel). Carport: geen zijwanden, doorlatend dak, max. 30 m² en 2,20 m hoog [B3 §2.3c] | nee | 7 → 6 |
| 13 | Garages en bijgebouwen | PGOU-ord. 10.5.1.7, 10.5.3.7 | Gesloten en overdekte bijgebouwen tellen als bebouwd. Poorten 1 m terug van de rooilijn, max. 3 m hoog. Ingegraven garage: deur ≥ 1 m terug van de rooilijn en ≥ 5 m van de grens met overliggende percelen. Overdekte barbecue ≥ 5 m van de grens; septic tank 5 m van de gevel, 2 m van de grens; watertank ≥ 10.000 l verplicht [B3 §2.3c] | nee | 2 |
| 14 | Zwembadmogelijkheden | PGOU-ord. 10.5.1.7; PORN art. 109 | Bassin 2 m van de grens, max. 2,5 m boven natuurlijk terrein; pomphuis > 1 m hoog op ≥ 5 m van de grens; zuivering verplicht [B3]. Montgó-flank (PORN B.4): zwembaden genoemd in 109.3 (rapport over SUZ-deelplannen); per project vermoedelijk via grondverzet (109.5.f) (type 4) [B6 F6] | nee | 2 |
| 15 | Parkeervereisten | PGOU-ord. 10.5.4.3 (Mod. 27); 10.1.4.3 | Zona E: "dos plazas por vivienda en el interior de la parcela". Casco: bij ≤ 4 woningen geen reserve, anders 0,6 plaats per woning [OCR] [B3] | ja | 2 |
| 16 | Ontsluiting en aansluitvoorwaarden | PGOU-ord. 8.1.6, 10.5.2; Mod. XXV; NUT NT 3; TRLOTUP 186, 211.1.b.4, 245; PORN 109.5; AMJASA, i-DE; nota simple; bezoek ter plaatse | Solar-eisen zie #3. **Toegang:** solar vereist toegang (8.1.6); frente 20 m (10 m aan een doodlopende weg); kavel onder de uitzonderingsregel ≥ 3 m toegang (Mod. XXV); SNU frente 20 m aan een kadastrale weg (PGOU). Erfdienstbaarheden alleen via nota simple of verkoper; openbaarheid van de weg en bereikbaarheid voor bouwverkeer: ONBEKEND tot bezoek [B3 §2.3, §3.2; B4 R12-08]. Zonder collector binnen 100 m: gecertificeerde afvalwatertank (NUT NT 3, status 7). Nutsbedrijven leveren alleen met vergunning (245). Montgó-flank: rapport Conselleria voor nieuwe water- of rioolaansluiting (109.5.b/e). SNU: water, afval en zuivering voor rekening van de eigenaar [B3, B5, B6] | deels | 3 |

#### C. Welke vergunningen en voorafgaande voorwaarden zijn nodig?

| # | Onderdeel (§16) | Waar komt het antwoord vandaan | Huidig antwoord Xàbia | Autom.? | Type |
|---|---|---|---|---|---|
| 17 | Bestaande bebouwing en eventuele afwijkende status | licentiearchief gemeente; Catastro-bouwjaar (geen bewijs van legaliteit); nota simple; TRLOTUP 206, 228–231, 255–256, DT 26, DT 28; Ley de Costas DT 4ª | Fuera de ordenación: alleen "obras de mera conservación" (206). SNU: handhaving verjaart niet (255.5); minimización alleen voor gebouwen af vóór 20-08-2014 (228.3), nooit extra m² (231.3), en geen procedure vóór het effectief functioneren van de Agencia Valenciana de Protección del Territorio (DT 28; toetreding Xàbia ONBEKEND). Gebouwen in SNU van vóór Ley 19/1975: gelijkgesteld met vergund (DT 26). Kust: werken zonder volume-, hoogte- of oppervlaktetoename alleen voor bouw vergund vóór 29-07-1988; na sloop geldt de wet volledig [B5, B6] | nee | 2 |
| 18 | Stedenbouwkundige lasten en uitvoeringsverplichtingen | PGOU-ord. 4.1.6–4.1.9; TRLOTUP 150–153, 187, 246.2; nota simple (afecciones) | Zona E: 29,07 % cessie (verrekend in 0,142/0,20). UA: cessie vóór licentie. PAI: cuotas en retasación. Aval bij gelijktijdig bouwen en urbaniseren (187). Een cédula moet openstaande cessie-, verdelings- en urbanisatieplichten vermelden (246.2) [B3 §5, B6 R13-17] | nee | 2 |
| 19 | Relevante sectorale beperkingen | stap 10; PATRICOVA; PORN; ZEC-norma; PATFOR/brand; PATIVEL; Costas; Aguas; Ley 4/1998 | Zie stap 10. Kernregels: PATRICOVA SNU niveau 2–5 + geomorfologisch: woningen verboden; PORN park: bouwverbod (56.1), Les Planes ≥ 10.000 m² na plan especial (56.2–3); afgebrande bosgrond 30 jaar geen herclassificatie (7.4); strook 30 m bij bos (bijlage XI); PATIVEL Litoral 1: geen nieuwbouw, rehabilitatie volgens 9.5; kust: 100 m (20 m bij grond die op 29-07-1988 stedelijk was), bindend rapport Generalitat (Ley 3/2025 art. 45); waterlopen 5 m / 100 m; NHT: toestemming cultuur; archeologische aandachtsgebieden: geen DR (233.1.a/c) [B5, B6]. **Wegen (carreteras):** niet onderzocht, alleen de GVA-planzone ZRP-CR als signaal [B3 §3.3] | ja (signalen); wegen nee | 3 → 2 |
| 20 | Benodigde onderzoeken | architect; TRLOTUP; PATFOR 28.3/30.1; PATRICOVA art. 11–13; Decreto 60/2012 | Topografisch plan; estudio geotécnico (bv. bij "limos de albufera" in l'Arenal); estudio de inundabilidad bij PATRICOVA- of ARPSI-signaal; landschapsstudie (SNU, PATIVEL 9.6); brandpreventieplan door bostechnicus (PATFOR 28.3); archeologie volgens de gemeentelijke catálogo (Mod. XVII, niet gelezen) en bij de BIC-zone "Yacimiento romano Illeta del Portichol"; evaluatie Red Natura bij SNU-bouw; toegang en erfdienstbaarheden (nota simple, bezoek) [B5 §8.1]. Kosten: ONBEKEND [B5] | nee | 6 |
| 21 | Vergunningsroute | TRLOTUP 232–246; Hacienda SGFAL (ICIO) | Nieuwbouw: licencia, beslistermijn 2 maanden, stilzwijgen = weigering (240.1.b, 242.2). Renovatie zonder vervanging hoofddraagelementen en 1e/2e ingebruikname: declaración responsable (233.1); constructieve verbouw, sloop, gebruikswijziging: DR plus certificaat (233.2). Erfgoed: 3 maanden (240.1.c). Kust: bindend rapport Generalitat vóór de bouwvergunning (238.4). Plan op beslisdatum (238.2), bij DR op indieningsdatum (241.6). **ICIO 4,00 %** over de PEM (2025 en 2026) [B4 R12-13, B8]. Tasa: ONBEKEND. Praktijk: "hasta un año" (pers 27-11-2023, type 1); planningsaanname 6–12 maanden vanaf volledig dossier (type 5) [B3 §4] | beslisboom ja | 2 |
| 22 | Planstatus en PGE-risico | §2.2; per perceel de PGE-kaart 2019 | PGOU in werking; NUT type 7; PGE geen recht. Wat het PGE-voorstel op een perceel zou doen (bv. declassificatie van urbanizable) is risico-informatie, geen waarde [B3, B4] | nee | 7 → 2/6 |
| 23 | Openstaande interpretatievragen | architect, gemeente, urbanismo-advocaat | Zie §5.3 | — | 7 |

#### D. Invulblad per perceel (kopiëren naar het dealdossier)

| Veld | Waarde | Document · versie · datum · status | Artikel / kaartblad / zone | Bewijstype | Controledatum | Interpretatievraag |
|---|---|---|---|---|---|---|
| Referencia catastral (14/20) + zekerheid | | | | | | |
| Registrale finca + coördinatiestatus (art. 10.4 LH) | | | | | | |
| Oppervlakte: advertentie (veld/tekst) · Catastro `ss` · WFS · registraal · topografisch | | | | | | |
| Klasse en instrument (PGOU / PP / PRI / UA) | | | | | | |
| Zone, grado, gebied B.2 | | | | | | |
| Punten 2–22 uit tabel A–C | | | | | | |
| Sectorale signalen per laag (met dienststatus) | | | | | | |
| Toegangsroute: weg, openbaar ja/nee, frente, bereikbaar voor bouwverkeer | | | | | | |
| Lasten en erfdienstbaarheden (nota simple), apart: voor en tegen het perceel | | | | | | |
| Afstand tot wegen, waterlopen en kust (met dienststatus of "niet getoetst") | | | | | | |
| Erfgoed en archeologie: Inventario (BIC/BRL) én gemeentelijke catálogo | | | | | | |
| Theoretisch recht · ruimtelijke inpasbaarheid · technische uitvoerbaarheid · vergunningverlening (§16, vier aparte oordelen) | | | | | | |

### 2.4 Rekenregels (§17): hoe het bouwvolume wordt bepaald

**Regel 0 — eerst parameters, dan rekenen.** Rekenen mag pas als zone, grado, regime (PGOU of plan parcial), bruto- of nettolezing en de relevante oppervlakte zijn vastgesteld. Tot die tijd staat in het dossier alleen de methode, geen getal.

| # | Rekenregel | Bron | Type |
|---|---|---|---|
| R1 | **Theoretisch meetellend vloeroppervlak = relevante perceeloppervlakte × edificabilidad.** Bij de nettocoëfficiënt (0,20) is de relevante oppervlakte het netto perceel exclusief wegen en cessies (art. 8.1.14); bij de brutocoëfficiënt (0,142) het polígono inclusief interne wegen en cessiegronden (art. 8.1.13) | PGOU-ord. 8.1.13–14, 4.1.9 [B3, B4] | 2 |
| R2 | De twee coëfficiënten zijn consistent: 0,20 × (1 − 0,2907) = 0,142. Een nettocoëfficiënt op een bruto-oppervlakte (of andersom) overschat of onderschat met ca. 29 % | eigen berekening op [B3] | 5 |
| R3 | **Maximale grondoppervlakte van bebouwing = totale perceeloppervlakte × ocupación.** Meetellend: elke doorlopende permanente overkapping (dus ook naya's en porches) en alles wat gesloten is met verticale elementen > 40 cm; niet: uitkragingen boven 3 m die niet gesloten zijn | PGOU-ord. 8.1.5 [B3] | 2 |
| R4 | **Edificabilidad en ocupación zijn verschillende plafonds.** Daarnaast gelden bouwlagen/hoogte, het bouwvlak (perceel min afstanden) en de parcela mínima als drempel. Het laagste plafond bindt | masterprompt §17; [B3] | 2/4 |
| R5 | **Het toegestane totaalvloeroppervlak nooit nogmaals met het aantal bouwlagen vermenigvuldigen.** Het aantal lagen verdeelt de m²t, het vermenigvuldigt ze niet | masterprompt §17 | — |
| R6 | Wat meetelt: alle beloopbare verdiepingen behalve toegestane kelders; overdekte terrassen, balkons en uitbouwen volledig, "la mitad" als het overdekte terras aan een zijde open is; permanente bijgebouwen. Niet: binnenpatio's, platte daken, openbare arcades, lichte afdaken. Zolder telt boven 1,80 m vrije hoogte [OCR]. Maximaal volume = m²t × 3 m | PGOU-ord. 8.1.15 (visueel), 8.1.26 [B3] | 2 |
| R7 | Oppervlaktebegrippen nooit door elkaar: advertentie (veld en tekst), Catastro `ss`, WFS `areaValue`, registrale oppervlakte en topografische meting apart vastleggen. Rekenen op de topografische of registraal gecoördineerde oppervlakte; tot die er is, op de laagste plausibele waarde (ontwerpregel) | [B1 §7.3, B2]; masterprompt §12 | 4 |
| R8 | Restcapaciteit bij bestaande bouw = perceel × coëfficiënt − bestaande meetellende m² volgens R6 (niet de Catastro-m², die ook sportvelden en bijgebouwen anders tellen), en alleen als de bestaande bouw legaal is | [B1, B3]; afleiding | 4 |
| R9 | SNU: vanaf 10.000 m² per woning, bezetting ≤ 2 % (bij 1 ha: 200 m²), max. 2 lagen, plus landbouwrapport (alleen agrarisch bedrijf of beroepsboer) | TRLOTUP 210.2, 211.1.b [B4, B6] | 2/4 |
| R10 | Meerdere woningen: splitsen vraagt ≥ 2 × parcela mínima; mancomunada ≥ 1,3 × n × parcela mínima; agrupación ≥ 5.000 m². Het totaal aan m²t blijft perceel × coëfficiënt | TRLOTUP 248.c; PGOU-ord. 10.5.5–10.5.6 [B3] | 2/5 |

**Rekenvoorbeeld op een fictief perceel (bewijstype 5; uitsluitend om de methode te tonen, geen bouwrecht voor een bestaand perceel).**
Aannames: rechthoekig perceel 30 × 50 m = 1.500 m² netto; PGOU-zona E grado II (E2); gebied met parcela mínima 1.500 m²; nettocoëfficiënt direct toepasbaar; geen plan parcial; geen sectorale beperking; vlak terrein.

| Toets | Berekening | Uitkomst |
|---|---|---|
| Drempel parcela mínima | 1.500 ≥ 1.500 m² | bebouwbaar |
| Frente en rechthoek | 30 m ≥ 20 m; 15 × 24 m past in 30 × 50 m | voldoet |
| Splitsen | 1.500 < 2 × 1.500 | ondeelbaar |
| Plafond 1: edificabilidad | 1.500 × 0,20 | **300 m²t** (bij bruto-lezing: 1.500 × 0,142 = 213 m²t) |
| Plafond 2: ocupación | 1.500 × 30 % | 450 m² footprint |
| Plafond 3: lagen en hoogte | grado II | 2 lagen; kroonlijst 7 m, totaal 9,50 m |
| Plafond 4: bouwvlak | (30 − 2 × 5) × (50 − 2 × 5) | 800 m² |
| Bindend | laagste plafond | **edificabilidad: 300 m²t** |
| Maximaal volume | 300 × 3 m | 900 m³ |

Een verdeling die binnen alle plafonds blijft: begane grond 170 m² gesloten + 40 m² overdekt terras dat aan één zijde open is (telt 20 m²t, interpretatievraag) + verdieping 110 m² = 300 m²t; footprint 170 + 40 = 210 m² (≤ 450 m²); kelder van 120 m² onder de footprint, plafond < 1,20 m boven natuurlijk terrein en ≥ 2,5 m van de grens (telt niet mee); zwembad op ≥ 2 m van de grens; 2 parkeerplaatsen op eigen terrein.

**Fouten die het systeem moet blokkeren:**
- 1.500 × 30 % × 2 lagen = 900 m²: ocupación maal lagen is geen edificabilidad; drie keer te veel.
- 1.500 × 0,20 × 2 lagen = 600 m²: dubbel geteld met de lagen; twee keer te veel.
- Catastro-`sfc` of advertentie-m² als meetellend vloeroppervlak gebruiken.
- De PGOU-zona E-tabel toepassen op een perceel in een plan parcial.

### 2.5 Ontwikkelscenario's

Per scenario: volume (volgens §2.4), onzekerheden, kosten, doorlooptijd en commerciële logica. Alle kostencijfers zijn landelijke marktindicaties (bewijstype 1, lage zekerheid) of wettelijke tarieven (type 2); ze zijn geen begroting. Voor het villasegment in Jávea ontbreken eigen nacalculaties [B7 §4.4]. Vraagprijzen zijn exclusief ITP/btw en kosten [B10 A8].

**Kosten die in elk bouwscenario terugkomen** [B7, B8]:

| Post | Waarde | Bron en type |
|---|---|---|
| Belasting op de grond | Van een particulier: ITP 9 % (11 % over het geheel boven 1.000.000 €). Van een ondernemer: solar, grond met bouwvergunning en grond "urbanizados o en curso de urbanización" = btw 21 % + AJD 1,4 %; rústico of niet-bebouwbare grond = btw-vrij, dus ITP 9 %, maar bij afstand van die vrijstelling btw 21 % + AJD 2 %. Grondslag ITP = hoogste van prijs en valor de referencia | Ley 13/1997 CV art. 13–14; TRLITPAJD art. 10.2; LIVA art. 20.Uno.20º, 20.Dos, 90 [C51, C52; B7 §1.3–1.7; B8 R14-06] · 2 (toepassing per deal: 4, gestor) |
| Notaris en register (aankoop) | Samen < 0,2 % van de koopsom; bij 500.000 € ca. 483 € notaris en 262 € register (alleen hoofdtarief, na 5 % korting, excl. btw en bijkomende posten). Bij segregación, agrupación en división horizontal rekent het register 70 % van het tarief | RD 1426/1989 en RD 1427/1989 [C69, C70; B7 §2.1–2.2; B8 R14-08] · 2 / 5 |
| Gestoría, advocaat, taxatie | ONBEKEND; geen gepubliceerde tarieven gevonden | [B7 §2.3] · 7 |
| Bouw villa | 800–1.200 €/m² "sin incluir el IVA", landelijk; voor "unifamiliar" kan het boven 1.200 €/m² uitkomen | habitissimo, bijgewerkt 18-06-2026 [C54] · 1 |
| Btw op de bouw | 10 % bij een contract promotor–aannemer voor overwegend woningen; aftrekbaar voor een promotor die met btw verkoopt | LIVA art. 91.Uno.3.1º [C52] · 2 / 4 |
| Honoraria | architect 10–12 % van de PEM plus arquitecto técnico ca. 5 %, plus 21 % btw | habitissimo [C54] · 1 |
| ICIO | **4,00 %** over de PEM (Xàbia 2025 en 2026). Habitissimo noemt licenties en ICIO samen "alrededor de un 6% del PEM" (landelijk) | Ministerio de Hacienda SGFAL [C31]; TRLRHL art. 102 [C53] · 2; habitissimo [B8 aanvulling 7] · 1 |
| Tasa licencia urbanística | ONBEKEND | [B3] · 7 |
| Zwembad, keermuren, sloop | zwembad 10.000–19.000 € (btw komt erbij); keermuur 90–250 €/m² muurvlak; sloop 10–90 €/m² (btw niet vermeld) | habitissimo [C55] · 1 |
| AJD declaración de obra nueva / división horizontal | 1,4 %; grondslag [te verifiëren] | Ley 13/1997 art. 14 [C51] · 2 / 7 |
| Seguro decenal bij verkoop nieuwbouw | premie ONBEKEND | [B7] · 7 |
| Jaarlijkse lasten tijdens bezit | IBI Xàbia 2026: 0,83 % (stedelijk) en 0,60 % (rústico) over de kadastrale waarde; afvalheffing variabel, bedrag per object ONBEKEND; verzekering en onderhoud ONBEKEND | Ministerio de Hacienda SGFAL, gemeentelijke tarieven 2026 [C71; B8 aanvulling 1; B7 §5.2] · 2 / 7 |
| Financiering | Referentie: nieuwe leningen aan niet-financiële vennootschappen juli 2026 3,68 % (voorlopig); Euríbor 12 maanden augustus 2026 2,954 %. Rente en voorwaarden van een promotor- of overbruggingslening: ONBEKEND | Banco de España, tabellen 19.1 en 19.3 [C72; B7 §5.1; B8 R14-15] · 2 / 7 |

**Illustratie** (type 5, alleen orde van grootte): voor 300 m²t uit het rekenvoorbeeld geeft 800–1.200 €/m² een bouwsom van 240.000–360.000 € excl. btw. Als de PEM daar ongeveer gelijk aan is (aanname), is de ICIO 9.600–14.400 € en zijn de honoraria (15–17 % van de PEM) 36.000–61.200 € plus 21 % btw. Zwembad, keermuren, aansluitingen en tasas komen erbij. Voor S5 is geen illustratie te maken: het lastenaandeel en de begroting van de urbanisatie ontbreken.

| Scenario | Wanneer denkbaar | Bouwvolume | Belangrijkste onzekerheden | Kosten bovenop de vaste posten (orde van grootte) | Doorlooptijd (aannames) | Commerciële logica |
|---|---|---|---|---|---|---|
| **S0 Geen ontwikkeling** | SNU zonder agrarisch bedrijf (211.1.b); urbanizable zonder vastgesteld programa (226); dotacional zonder woonbestemming (K11); PORN-park (56.1); PATIVEL Litoral 1 (nieuwbouw verboden); PATRICOVA SNU niveau 2–5 of geomorfologisch; perceel onder het minimum zonder uitzondering | 0 m² woning | of een uitzondering of lopend programa bestaat | grondprijs, grondbelasting en notaris/register zonder bouwopbrengst; daarna elk jaar IBI (0,83 % of 0,60 % van de kadastrale waarde) en afvalheffing; financieringskosten lopen door | n.v.t. | niet kopen voor route B; hooguit route D of een ander gebruik met eigen business case. Een prijsdaling maakt dit niet tot een kans [B9 K11] |
| **S1 Eén villa** | solar met bevestigde zone en opgeleverde urbanisatie, of met aval (187) | min(perceel × coëfficiënt, footprintplafond, lagen, bouwvlak) | netto/bruto; grado; plan parcial; helling en keermuren; urbanisatiestatus; toegang; sectorale rapporten (bv. PORN 109.5) | bouw 800–1.200 €/m² excl. btw × m²t (landelijke ondergrens); btw 10 % (promotorcontract); honoraria 15–17 % van de PEM + 21 % btw; ICIO 4 %; tasa ONBEKEND; zwembad 10.000–19.000 €; keermuren 90–250 €/m² muurvlak; aansluitingen ONBEKEND; AJD obra nueva 1,4 %; seguro decenal ONBEKEND (zie illustratie) | licentie wettelijk 2 maanden, praktijk "hasta un año" (pers 2023); planningsaanname 6–12 maanden vanaf volledig dossier; start ≤ 6 en afbouw ≤ 24 maanden tenzij de licentie anders zegt (188.2); bouwduur ONBEKEND [B3, B4] | waarde uit het bouwrijp maken en verkopen; eindwaarde nog niet onderbouwd (vraagprijzen ≠ marktwaarde) |
| **S1b Bouwklaar pakket doorverkopen** | perceel met verleende licentie en project (K07-type) | zoals in het project, mits binnen de plafonds | licentie nog geldig? (188.2, verval 244); overdraagbaarheid van licentie en projectrechten ONBEKEND; herontwerp = nieuwe licentie | grondprijs inclusief licentie en project; van een ondernemer: grond met bouwvergunning = btw 21 % + AJD 1,4 %, geen ITP [B7 §1.4]; rest van het project (K07-claim: 70 % betaald; rest ONBEKEND); juridische toets overdraagbaarheid ONBEKEND; wie bouwt, betaalt daarna S1-kosten (of de ICIO al betaald is: ONBEKEND) | kort, als documenten kloppen | tijdwinst van het vergunningstraject is de waarde; zonder licentiekopie is die waarde nul |
| **S2 Meerdere eenheden** | splitsen (≥ 2 × minimum, parcelación-licentie, per kavel frente en rechthoek); mancomunada (≥ 1,3 × n × minimum, Estudio de Detalle); agrupación (≥ 5.000 m², ED) | totaal blijft perceel × coëfficiënt; wel verdeeld over meer woningen | ED-procedure (termijn en tasa ONBEKEND); per kavel toegang ≥ 3 m | als S1 per woning; parcelación-licentie en Estudio de Detalle: tasa en honoraria ONBEKEND; AJD 1,4 % op segregación en división horizontal (grondslag [te verifiëren]); register 70 % van het tarief bij segregación en división horizontal [B7 §1.3, §2.2]; aansluitingen per kavel ONBEKEND | parcelación: beslistermijn 1 maand (240.1.a); ED ONBEKEND | kleinere, beter verkoopbare eenheden; geen extra m² |
| **S3 Behoud plus uitbreiding** | bestaande legale woning met restcapaciteit (R8) | perceel × coëfficiënt − bestaande meetellende m² | legaliteit bestaande bouw; betekenis van claims als "edificabilidad no agotada del 20%" (K03) [B9]; niet in SNU (231.3), PORN-amortiguación-SNU (57), kustservidumbre (DT 4ª), fuera de ordenación (206) | aankoop: van een particulier ITP 9 %; van een ondernemer meestal ITP (tweede levering), maar niet vrijgesteld bij levering "para su rehabilitación por el adquirente" ([te verifiëren], fiscalist) [B8 aanvulling 3]; extra m²: nieuwbouwindicatie 800–1.200 €/m² (toepassing type 4); aanpassing van het bestaande deel: renovatieband 400–1.200 €/m² (bron tegenstrijdig, type 7) [B7 §4.5]; btw op de werken 21 % voor een vennootschap, 10 % alleen onder voorwaarden [B7 §1.4]; honoraria, ICIO 4 %, tasa ONBEKEND | licentie voor uitbreiding als S1 | minder bouwrisico dan sloop; waarde als het huis klein is op een groot perceel |
| **S4 Sloop en nieuwbouw** | bestaand volume veel kleiner dan toegestaan, of bouwkundig niet te redden | als S1 over het hele perceel | na sloop geldt de kustwet volledig (DT 4ª.2); casco/NHT: gevels van vóór 1940 en toestemming cultuur (NUT, status 7); sloop = DR plus certificaat (233.2) | sloop 10–90 €/m² (gemiddeld 50 €/m², btw niet vermeld) [C55]; aankoop van een ondernemer om te slopen: btw 21 %, geen vrijstelling en geen 10 % [B7 §1.4, B8 R14-06]; kosten van het certificaat ONBEKEND; daarna als S1 | sloop + licentie + bouw; termijnen als S1 | alleen zinvol als de extra m² de sloop- en belastingkosten ruim dekken |
| **S5 Deelname in een plangebied met herverkaveling** | pakket grond in een UA of plan waarvan de urbanisatie nog niet af is (K10; ook Sareb-perceel B Toscal–Cap Martí, 72,22 % van een UA) [B11 §6] | volgens het plan en de herverkaveling; nooit zelf rekenen met de zona E-tabel. K10-claim: max. 3.554 m²c "tras las gestiones y transformaciones pertinentes" (type 1) | klasse (urbanizable of urbano no consolidado); bestaan een vastgesteld programa en een reparcelación?; aandeel in de lasten (K10: 26,85 %); stilstand (in 2017 werden de PAI's ADN-4, MES-2 en MES-3 geschorst) en het PGE-voorstel dat ca. 8 mln m² urbanizable wil declassificeren [B3 §1.1, §5]. Is het urbanizable zonder vastgesteld programa, dan geldt S0 (226) | aankoop van een ondernemer: btw 21 % + AJD 1,4 % (2 % bij afstand van vrijstelling) [B7 §1.3–1.4]; cessies en urbanisatiekosten naar aandeel (PGOU-ord. 4.1.6–4.1.9; bij een PAI cuotas en retasación, TRLOTUP 150–153): bedrag ONBEKEND; aval bij bouwen vóór oplevering (187.1); daarna per kavel S1-kosten | ONBEKEND; geen termijn in de bronnen. R15 spreekt van een "lange horizon" (type 4) [B9] | waarde uit grondontwikkeling: van niet-geconsolideerde grond naar bouwrijpe kavels (route B, kapitaalintensief). K10: 41 €/m² perceel, tegenover "in deze set 272–828 €/m²" voor Balcón al Mar volgens R15 (vraagprijzen, type 1/5) [B9] |

### 2.6 Toepassing op echte percelen uit R15 (en R10)

#### K07 — Perceel met geclaimde licentie, Garroferal del Montgó (Idealista 112280961 = BP 4676JAV)

**Aanbod (type 1):** 505.000 €, 1.570 m², zuid; "En el precio de venta se incluye la licencia de obras del Ayuntamiento, las tasas, el aval bancario de la urbanización y el 70 % del proyecto" [B9, C56]. BP-tekst: villaproject van 310 m² over twee lagen [C64, C65]. Gestructureerd Idealista-veld: "Terreno urbanizable / Calificado para otra" [B10].

| Stap | Wat vandaag vaststaat | Bron · type | Status |
|---|---|---|---|
| 0 Intake | Idealista-pin 38,7936151 / 0,1214097, adres niet getoond; BP-pin 38,794232 / 0,119842, 152 m verderop; BP plotArea 1.570 | [B4, B6, C64] · 1/3 | gedaan |
| 1 Identiteit | ≥ 10 Idealista-codes met 500.000–550.000 €; dubbel 112283303 toont adres Calle Pic de Rebalsadors 30 (1.571 m², 500.000 €, "licencia de obra y proyecto incluido", 310 m² bebouwbaar); dubbel 112256480 (adres verborgen, 1.570 m², 310 m² bebouwbaar, "2 plantas edificables"); één dubbel noemt zelf perceel- en huisnummer (waarde niet in de rapporten) | [B2 R11-07, B10 R15-06] · 1/3; identiteit 4 | gedaan, identiteit niet bewezen |
| 2 RC in tekst | niet aangetroffen in de gelezen teksten | [B9, B10] · 3 | — |
| 3 Adres | Pic de Rebalsadors 30 → **0281202BC5908S**, "suelos sin edificar", 1.567 m², 0 m² gebouwd; de pin van 112283303 valt exact op het Catastro-referentiepunt van dit perceel | [B2 R11-07, A10] · 3 | gedaan |
| 4 Coördinaat | pin van 112256480 → 0281206BC5908S (villa uit 2006, 348 m², 1.572 m²). De eigen K07-pin en de BP-pin zijn **niet** tegen Catastro bevraagd. Afstand van de K07-pin tot het referentiepunt van 0281202: ca. 258 m; van de BP-pin: ca. 340 m; tussen de pins van 112256480 en 112283303: 129 m | [B1, B2] · 3; afstanden eigen berekening · 5 | deels |
| 5 Toetsen | oppervlakte onderscheidt niet: 1.567 m² (0,2 % van 1.570) tegen 1.572 m² (0,1 %) [B2 A9]; typeconsistentie: 0281202 onbebouwd past bij "terreno", 0281206 bebouwd niet | [B2] · 3/5; typeoordeel 4 | gedaan |
| 6 Zekerheid | voor advertentie 112283303: HOOG-criteria gehaald. Voor K07 zelf: **MIDDEL** (koppeling via een dubbele advertentie, type 4; eigen adres verborgen; eigen pins 150–340 m verspreid) | regels §2.1 stap 6 · 4 | **stop** |
| 7 Poort 1 | niet uitgevoerd | — | open |
| 8 Planfilter (signaal) | Idealista-pin → PP "ERMITA II", SUZ, ZND-RE; BP-pin → PP Ermita II én "Plan general SU ZUR-RE"; GVA-inventarislaag noemt op de Idealista-pin "Plan Parcial Montgó-2 / SUP Montgó-2" (PAI toegewezen, reparcelación goedgekeurd). Perceelpolygoon van 0281202 is niet over de laag gelegd | [B4 R12-09, B5 §2.6, B6 A3] · 3; klasse 7 | tegenstrijdig |
| 9 Regels | PP Ermita II staat niet in het register: ordenanzas ONBEKEND. De PGOU-zona E-tabel geldt alleen als het perceel onder het PGOU valt. Consistentietoets: 310 m² bebouwbaar / 1.567 m² = 0,198 m²t/m², dicht bij 0,20 netto (type 5; bewijst niets over de geldende norm) | [B3, B4] · 2/5 | open |
| 10 Sectoraal (op Idealista-pin) | geen PATRICOVA-zone; PORN Montgó: in het ámbito, zone "Áreas urbanas y urbanizables", niet in het park → rapport Conselleria nodig voor grondverzet, nieuwe wateronttrekking en aansluitingen (PORN 109.5); geen bosgrond; brandinterface "2 – Casos aislados"; binnen ZIF 500 m en PPIF Montgó; geologie "Depósitos aluviales, fondo de valle"; niet in de minimización-laag. Costas/PATIVEL niet bevraagd | [B5, B6 R13-09] · 3 | signalen; op perceel te herhalen |
| 11 Fysiek | helling, toegang en aansluitingen niet onderzocht | — | open |
| 12 Poort 2 | licentie niet gezien; de aval past bij bouwen vóór oplevering van de urbanisatie (art. 187.1: geen gebruik vóór oplevering, voorwaarde gaat mee bij verkoop) | [B4 R12-16] · 2 (wet) / 4 (toepassing) | open |

**Uitkomst K07:** "Bouwmogelijkheden nog niet betrouwbaar te bepalen: exacte perceelidentificatie ontbreekt." Het gat is klein: één bevestigde RC. Maar ook met die RC blijven de regels van PP Ermita II, de klassevraag (SUZ of SU), de stand van de urbanisatie en de licentie zelf open. Dealhypothese blijft "verder onderzoeken" (route B of D) [B9].

**Les uit dezelfde straat:** R11 kende de pin van 112256480 eerst zekerheid HOOG toe en noemde de categorie "terreno" fout. De tegenspraak liet zien dat de advertentie zelf "Superficie edificable 310 m²" en "Inmueble exento" vermeldt en vrijwel zeker over de onbebouwde buurkavel gaat [B2 R11-07]. Precies daarom geldt: adres verborgen = hoogstens MIDDEL, en advertenties eerst tegen elkaar matchen.

**Documenten die nodig zijn en hoe ze rechtmatig te krijgen:**

| Document | Waarom | Route | Wie / kosten |
|---|---|---|---|
| Referencia catastral en adres, schriftelijk van de aanbieder | sluit stap 6–7 | vraag aan Atina Inmobiliaria of via de BP-relatie (4676JAV) | ⏸️ ACTIE VOOR JAN: akkoord op het bericht; geen kosten |
| Kopie van de bouwlicentie (nummer, datum, houder, voorwaarden, termijnen, verlengingen) en betaalbewijs tasas/ICIO | de licentie is de waarde van S1b; verval volgens 188.2/244 | aanbieder; daarna bevestigen in het informe urbanístico | idem |
| Project en contract met de architect (70 % betaald) | overdraagbaarheid van project en licentie ONBEKEND | aanbieder | juridische toets nodig (kosten ONBEKEND) |
| Aval de urbanización (bedrag, begunstigde, voorwaarden) | art. 187; wat gebeurt er bij verkoop | aanbieder | idem |
| Nota simple van 0281202BC5908S (na bevestiging) | eigendom, lasten, registrale oppervlakte, RC en coördinatiestatus (art. 10.4 LH) | sede.registradores.org (login, legitiem belang) | 9,02 € + btw [B2] |
| Informe urbanístico (art. 246.4) | klasse, instrument (PP Ermita II of PG), parameters, stand urbanisatie, NUT, PGE | Ajuntament de Xàbia, Urbanismo (sede electrónica / OAC) | architect of Jan; termijn 1 maand; tasa ONBEKEND |
| Ordenanzas PP Ermita II (exp. 19940463) | parameters §16 | gemeente of GVA (niet in het register) | ONBEKEND |
| Topografisch plan, geotechniek | bouwvlak, keermuren, fundering | topógrafo / laboratorium | na akkoord; kosten ONBEKEND |

#### K08 — Perceel met geclaimde "licencia vigente", eigendom van een SL, El Rafalet (Idealista 90705084)

**Aanbod (type 1):** 150.000 €; gestructureerd 1.120 m², tekst "1000 m2"; adres getoond "Calle Mar Amarillo 300"; hellend; "parcela urbana… con licencia de construcción vigente… la parcela pertenece actualmente a una sociedad limitada española (SL)"; hoofdfoto volgens de aanbieder AI-gegenereerd; gestructureerd veld "Terreno urbanizable / Calificado para otra" [B9, B10, C59].

| Stap | Wat vandaag vaststaat | Bron · type | Status |
|---|---|---|---|
| 0 Intake | pin ±38,7621 / 0,1544 (R15, vier decimalen); die valt samen met het Rafalet-testpunt 38,7620527 / 0,1543695 van R11, dat R12 als K08-pin gebruikte. Volledige gelijkheid van de coördinaat staat niet in R15 [te verifiëren] | [B1, B3, B9] · 1/3 | gedaan |
| 1 Identiteit | mogelijk BP 4104JAV (150.000 €, 1.100 m², doodlopende straat, "up to 2 floors"), maar zwak: er zijn meer Rafalet-percelen rond die prijs (91806635: 150.000 €/1.215 m²; 112433736: 160.000 €/1.060 m²). 4104JAV heeft in de feed **geen coördinaten** | [B10 R15-07] · 4; [C64] · 3 | onbeslist |
| 2 RC in tekst | niet aangetroffen | [B9] · 3 | — |
| 3 Adres | "Calle Mar Amarillo 300" is **niet** door de adresdienst [E2] gehaald; getest zijn alleen nr. 4 (→ 2944017) en nr. 5 (→ 2944002, 1.060 m², twee andere advertenties) | [B1, B2] · 3 | eerste automatische actie |
| 4 Coördinaat | pin → 2944017BC5924S op 0 m; buren 2944010 (2,7 m, 960 m²), 2944012 (7,57 m, 1.120 m²), 2944011 (10,57 m, 883 m²), 2944013 (20,81 m, 898 m²); bbox 60 × 60 m: 7 percelen van 749–1.120 m² | [B2 R11-08] · 3 | gedaan |
| 5 Toetsen | 2944017: 1.074 m², onbebouwd, grensafstand 2,13 m, Sede "Clase Urbano, Uso principal Suelo sin edif."; afwijking t.o.v. veld 1.120 m²: 4,1 %; t.o.v. tekst 1.000 m²: 7,4 %. 2944012: 1.120 m² = 0,0 % t.o.v. het veld | [B2] · 3; afwijkingen · 5 | gedaan |
| 6 Zekerheid | **MIDDEL**: twee kandidaten binnen ±10 % (2944017 via de pin, 2944012 via de oppervlakte), pin 2,1 m van de grens, adresnummer niet getoetst | regels stap 6 · 4 | **stop** |
| 8 Planfilter (signaal) | op de pin: "Plan general · SUZ · ZND-RE". Dat spreekt "parcela urbana" (tekst) tegen; de Catastro-klasse "Urbano" zegt niets over de planologische klasse, want Catastro levert geen bestemming | [B3 §2.8, B1 §2.3] · 3; klasse 7 | tegenstrijdig |
| 9 Regels | welk regime (PGOU zona E, gebied Lluca-Rafalet met parcela mínima 1.000 m², of een UA/plan) is niet vastgesteld. Het register kent Mod. nº 7 "UA Lluca-Rafalets 5 en 12" (CTU 19-11-1993); of K08 daarin ligt: [te verifiëren]. Als het perceel SUZ zonder programa is, is woningbouw verboden (226) | [B3, B4] · 2/7 | open; bewust niet gerekend |
| 10 Sectoraal | **niet** op deze pin uitgevoerd | — | eerste automatische actie |
| 11 Fysiek | "hellend" (claim): keermuren en fundering als kostenrisico; keermuren max. 2,5 m (8.1.23.2, [OCR]) | [B3, B9] · 1/2 | open |
| 12 Poort 2 | licentie zonder nummer of datum; SL-eigendom | [B9] · 1 | open |

**Uitkomst K08:** "Bouwmogelijkheden nog niet betrouwbaar te bepalen: exacte perceelidentificatie ontbreekt." Daarbovenop een klassevraag (SU of SUZ) die, als het SUZ zonder programa blijkt, de licentieclaim ongeloofwaardig maakt en scenario S0 oplevert. Dealhypothese blijft "verder onderzoeken" (route B, bijzondere situatie SL) [B9].

**Documenten en rechtmatige route:** (1) adresdienst [E2] op "MAR AMARILLO 300" (open dienst, automatisch); (2) RC en licentiekopie van Grupo García (⏸️ akkoord Jan op het bericht); (3) nota simple op het bevestigde perceel (op naam van de SL; 9,02 € + btw); (4) uittreksel Registro Mercantil van de SL, want een aandelenkoop neemt ook schulden en verplichtingen van de vennootschap over [B9]; (5) informe urbanístico met de vragen klasse, programa, UA en oplevering; (6) fiscale toets door een gestor: een solar van een ondernemer valt onder btw 21 % + AJD 1,4 %, niet onder ITP; grond die niet bebouwbaar is kan btw-vrij zijn (LIVA art. 20.Uno.20º) [B7 §1.4, B8 R14-06; toepassing type 4].

#### K09 — Perceel Pinosol met geclaimde parameters (Idealista 109915149), kort

- **Claim (type 1):** "Suelo Urbano – Residencial Extensivo (Zona E, grado II)… Edificabilidad 0,20 m²/m² (aprox. 259 m² construibles)… Ocupación máxima del 30%… PB + 1 planta… Parcela mínima 1.000 m²"; 1.299 m²; prijsveld 299.000 €, tekst 325.000 € [B9, B10].
- **Toets tegen de documenten:** de getallen kloppen met de PGOU-waarden voor zona E grado II (0,20 netto; 30 % [te verifiëren op Mod. I-blad]; 2 lagen) [B3]; 1.299 × 0,20 = 259,8 m²t (type 5). "Pinosol" staat niet als gebied in de tabel van 10.5.1.1, dus de parcela mínima is niet te controleren zonder plano B.2 [B3].
- **Tegenstrijdig:** gestructureerd veld "Terreno urbanizable / residencial unifamiliar" [B10]; in dezelfde zone rekent advertentie 111340209 met 700 m², 140 m² footprint (20 %) en 210 m² (0,30 m²t/m²) [B10 R15-08].
- **Waar de keten stopt:** stap 2–10 zijn voor K09 niet uitgevoerd. Consistente getallen in een advertentie zijn geen bewijs: ze kunnen uit de PGOU-tabel zijn overgeschreven terwijl een plan parcial geldt. **Stop bij stap 6 (nog niet uitgevoerd).**

#### K10 — 16 kavels "Ciudad La Guardia" in Balcón al Mar = Sareb-perceel A bij Servihabitat (Idealista 107655781 en 111869151)

**Correctie na de kritiekronde (15-09-2026).** De eerste versie behandelde K10 als urbaniseerbaar pakket onder "PP La Guardia-3", met art. 226 en scenario S0. Die koppeling werd door geen bron gedragen. R10 beschrijft vrijwel zeker hetzelfde object bij de verkoper, met een andere klasse, een ander plangebied en een ander belastingregime. Hieronder de gecorrigeerde versie.

**Drie advertenties, vermoedelijk één object** (bronfeiten type 1, door ons gezien type 3; identiteit type 4):

| Kenmerk | Idealista 107655781 (K10) | Idealista 111869151 | Servihabitat Profesionales, promotie 06124187 ("perceel A") |
|---|---|---|---|
| Aanbieder | Leukante Realty S.L. (Calpe), ref. SH0697 [B9 §2] | `commercialName` "Servihabitat", externalReference 60709763 [B12 R10-17] | Servihabitat als verkoper; eigenaar volgens de pagina: "Sociedad de Gestión de Activos Procedentes de la Reestructuración Bancaria, S.A." (Sareb) [B12 A1] |
| Prijs | 725.000 €, was 904.000 € (−20 %) [B9, B10 R15-09] | 725.000 €, was 904.000 € (−20 %) [B12 R10-09] | 725.000 € "Desde"; eenheidspagina 60709759: 17.775 m² voor 725.000 € [B12 R10-08] |
| Oppervlakte en aantal | 17.775 m²; "Se venden 16 suelos urbanizables" [B9] | zelfde cijfers [B9] | "16 fincas con un total de 17.775 m2"; promotiepagina "16 unidades de venta" [B11 §6, B12] |
| Bouwclaim | "Edificabilidad máxima tras las gestiones y transformaciones pertinentes de 3.554 m2"; 2 plantas [B9] | — | max. 3.554 m²c; gemiddeld 222 m²c per woning; "vivienda aislada" [B11 §6, B12 A2] |
| Aandeel in het plangebied | "Porcentaje de participación en el ámbito de 26,85 %" [B9] | — | 26,85 % [B11 §6] |
| **Klasse volgens de aanbieder** | gestructureerd "Terreno urbanizable"; tekst "plan de reparcelación Ciudad La Guardia" [B9, B10] | "Situación urbanística": "Terreno urbanizable" [B12 A4] | **"TERRENO URBANO NO CONSOLIDADO"**, sector **"PGOU UA BALCON AL MAR 1"** [B11 §6, B12 R10-08] |
| Adres en pin | Calle Sergei Rachmaninov 8; pin ±38,7411 / 0,2175 [B9] | Calle Sergei Rachmaninov 4 [B9] | "balcon al mar (javea)" [B11 §6] |
| Verkoopvoorwaarden | — | het enige perceel "de bancos" van Idealista in Jávea (0 woningen); "posible proceso competitivo o … (POV)" en "periodo de transparencia de 20 días naturales máximo" [B11 §5–6, B12 R10-09] | "destinada a profesionales"; "sujeta y no exenta de IVA / IGIC"; "Los precios no incluyen impuestos y gastos a cargo del comprador"; bijgewerkt 09-09-2026 [B11 §6, B12 R10-08, A3] |

**Waarom één object (type 4):** prijs, eerdere prijs, 17.775 m², 16 eenheden, 3.554 m² en 26,85 % zijn in de kanalen gelijk; R15 merkte 111869151 al aan als dubbel van 107655781 [B9], en R10 koppelde 111869151 via `property_detail` aan Servihabitat [B12]. Niet bevestigd met kadastrale referenties (werkhypothese W9).

**Wat dit verandert:**
1. **De klasse is tegenstrijdig (type 7).** Twee Idealista-advertenties zeggen "urbanizable", de verkoper namens de eigenaar zegt "urbano no consolidado" in de "UA Balcón al Mar 1". Beide zijn aanbiedersclaims; geen officiële bron is geraadpleegd. De Servihabitat-pagina is het meest specifiek (sectornaam) en staat het dichtst bij de eigenaar; het gestructureerde Idealista-veld bleek bij K07 en K08 onbetrouwbaar [B10]. Dat maakt de Servihabitat-lezing waarschijnlijker, niet bewezen (type 4). Van de twee is Servihabitat daarom de best gedocumenteerde bron; toch rekent het dossier met geen van beide tot het informe urbanístico er is. De GVA-planlaag is op deze pin en op deze percelen niet bevraagd. De eerdere koppeling aan "PP La Guardia-3" berust alleen op naamsgelijkenis met "Ciudad La Guardia" en is geschrapt; het register kent zowel "mod. PP La Guardia-1" als, in de GVA-laag, "PLAN PARCIAL LA GUARDIA-3", en "UA Balcón al Mar 1" staat niet in de door R12 overgenomen registerlijst [B3 §1.3] (type 4, [te verifiëren]).
2. **Welke regel geldt, hangt van die klasse af** (tekst type 2 [B3 §2.6, §5; B4 R12-16, R12-19], toepassing type 4):
   - *urbanizable zonder vastgesteld programa:* woningen verboden (226.1) en niet splitsbaar (248.e) → **S0**;
   - *plangebied mét vastgesteld programa en herverkaveling:* parameters uit het plan; kavels worden pas solar na urbanisatie → **S5**;
   - *urbano no consolidado in een UA:* cessie vóór licentie (PGOU-ord. 4.1.7–4.1.9), urbanisatiekosten voor de eigenaar (4.1.6; TRLOTUP 187.2), bij een PAI cuotas en retasación (150–153), bouwen vóór oplevering alleen met aval (187.1) → **S5**. De eigen normen van deze UA: ONBEKEND.
   Art. 226 is dus niet zonder meer de toepasselijke regel. S0 geldt pas als het informe urbanístico "urbanizable sin programa" bevestigt.
3. **Consistentietoets (type 5, bewijst niets over de geldende norm):** 3.554 / 17.775 = 0,20 m²t/m²; 3.554 / 16 = 222 m² per kavel, gelijk aan de Servihabitat-claim; 17.775 / 16 = gemiddeld 1.111 m² per kavel. Die getallen lijken op de zona E-waarden (0,20 netto; parcela mínima Balcón al Mar 1.000 m² [B4 R12-05]), maar de zona E-tabel mag op een UA of plan niet worden toegepast (§2.4, fout 4).
4. **Belasting: btw in plaats van ITP.** Servihabitat meldt "sujeta y no exenta de IVA" (type 1). Grond die "urbanizados o en curso de urbanización" is, valt niet onder de btw-vrijstelling (LIVA 20.Uno.20º) [B8 R14-06, type 2]; dan geldt btw 21 % plus AJD 1,4 % [B7 §1.3–1.4]. Komt de btw voort uit afstand van de vrijstelling (20.Dos), dan is de AJD 2 % [B7 §1.3]. Welke van de twee: ONBEKEND (gestor). Orde van grootte over de vraagprijs (type 5; grondslag [te verifiëren]): btw 152.250 €; AJD 10.150 € bij 1,4 % of 14.500 € bij 2 %. De btw is alleen aftrekbaar voor een koper met btw-aftrekrecht (type 4) [B7 §1.4]. De vraagprijs is exclusief die belastingen en kosten [B12 A3].
5. **Koper en proces.** "Destinada a profesionales"; volgens het portaal "Los inmuebles no reúnen los requisitos técnicos o documentales para ser comprados por consumidores y usuarios" [B11 §2, type 1]. Via welke entiteit TREE zou kopen: ONBEKEND (investeringskader van Jan). De biedprocedure (POV, 20 dagen) staat alleen in het reglement van de verkoper; zonder dat reglement geen bod.
6. **Per kavel of als pakket:** de eenheidspagina toont één eenheid van 17.775 m² voor 725.000 €, de promotiepagina "16 unidades de venta": ONBEKEND [B12].

| Stap | Status K10 | Bron · type |
|---|---|---|
| 0 Intake | drie advertenties ingelezen | [B9, B11, B12] · 1/3 |
| 1 Identiteit | één object waarschijnlijk (zes gelijke kenmerken) | · 4 |
| 2–5 | niet uitgevoerd. 16 fincas betekent 16 RC's en 16 perceelpolygonen; de adressen Sergei Rachmaninov 4 en 8 zijn niet via de adresdienst [E2] getoetst | — |
| 6 Zekerheid | niet bepaald: meerdere percelen zonder RC → **stop** | regels stap 6 · 4 |
| 8 Planfilter | niet uitgevoerd op de pin of de percelen | — |
| 9 Regels | klasse type 7 (zie punt 1); normen van UA of plan ONBEKEND; bewust niet gerekend | [B3, B11, B12] · 7 |
| 10 Sectoraal | niet uitgevoerd. PATIVEL Litoral 1 ligt in de partida el Portitxol (ca. 49 ha) [B5 §5.4]; of dat de 16 percelen raakt, is niet getoetst | [B5] · 3 (laag) |
| 11 Fysiek | toegang, helling en aansluitingen niet onderzocht; bij niet-geconsolideerde grond is de toegang zelf onderdeel van de urbanisatie (type 4) | — |
| 12 Poort 2 | informe urbanístico met klasse, UA of plan, programa, stand van de reparcelación "Ciudad La Guardia", lastenaandeel en aval | — |

**Uitkomst K10:** "Bouwmogelijkheden nog niet betrouwbaar te bepalen: exacte perceelidentificatie ontbreekt." Daarbovenop een klassevraag (type 7) die bepaalt of het S0 of S5 wordt, en een btw-regime in plaats van ITP. Horizon, urbanisatiekosten en lastenaandeel in euro's: ONBEKEND. Dealhypothese blijft "watchlist" (route B) [B9].

**Documenten die nodig zijn en hoe ze rechtmatig te krijgen:**

| Document | Waarom | Route | Wie / kosten |
|---|---|---|---|
| 16 referencias catastrales en fincanummers | stap 2–7 | Servihabitat-ficha (download pas na akkoord van Jan) of schriftelijke vraag aan Servihabitat | ⏸️ ACTIE VOOR JAN: akkoord op contact en eventueel een account op Servihabitat Profesionales (portaal alleen handmatig; voorwaarden verbieden automatisch hergebruik) [B11 §9, B12 R10-14] |
| Nota simple per finca | eigendom (Sareb), lasten, afecciones urbanísticas, oppervlakte | registradores.org | 16 × 9,02 € = 144,32 € + btw (type 5) [B2] |
| Informe urbanístico (art. 246.4) | klasse, UA of plan, programa, reparcelación, cuotas, aval | Ajuntament de Xàbia, Urbanismo | architect of Jan; termijn 1 maand; tasa ONBEKEND |
| Stand en begroting van de urbanisatie en het aandeel van 26,85 % | kosten S5 | gemeente; wie de urbanisatie uitvoert: [te verifiëren] | ONBEKEND |
| Fiscale toets btw en AJD (1,4 % of 2 %), aftrekbaarheid, koopentiteit | punt 4 en 5 | gestor of fiscalist | ONBEKEND |
| Reglement van de biedprocedure (POV) | proces, termijn, borg | Servihabitat | geen kosten |

**Ook in dit kanaal:** Sareb-perceel B "Toscal–Cap Martí" (Servihabitat 06124173): "1 finca de suelo urbano no consolidado" van 4.622 m², "72,22%" van de UA Toscal-Cap Martí; volgens de aanbieder zijn programa en urbanisatieproject goedgekeurd en is de herverkaveling "en curso", met "edificabilidad prevista es de 623 m2, para un total de 3 viviendas unifamiliares"; prijs op aanvraag; op het portaal verkeerd ingedeeld onder "huerta sur" [B11 §6, B12 R10-08]. Zelfde aanpak (S5), plus de vraag wat een onverdeeld aandeel van 72,22 % in een lopende herverkaveling juridisch inhoudt. Niet in R15 of op Idealista gezien.

#### K11 — dotacional, waar de keten vóór het perceel al stopt

- **K11 (dotacional, 229.000 €, was 336.000 €):** de aanbieder zegt zelf "No se permite el uso residencial" [B10]. Scenario S0 voor route A/B; afwijzen blijft een afweging, geen feit.

---

## 3. Aannames en onzekerheden

### 3.1 Werkhypothesen (als zodanig gemarkeerd, niet door Jan of een professional bevestigd)

| # | Werkhypothese | Waarom gebruikt | Wat het weerlegt |
|---|---|---|---|
| W1 | Laagvolume-gebruik per kandidaat (met cache op RC) valt binnen de Catastro-voorwaarden. De "≤ 1 verzoek per seconde" uit R11 heeft geen bron; de werkelijke drempel staat nergens, de sanctie wel ("generalmente 10 días") [B2 F14, R11-11] | anders geen automatische stap 2–5 | schriftelijke bevestiging van de DG del Catastro of een blokkade |
| W2 | De drempels 3 % oppervlakte, 5 m grensafstand en 25 m zoekstraal zijn bruikbaar | eerste kalibratie | meting op de eerste 30 dossiers [B1] |
| W3 | Een pin die exact op een Catastro-referentiepunt valt, is uit het Catastro overgenomen | één waarneming (112283303) [B2 A10] | steekproef |
| W4 | De ≥ 10 Idealista-codes van K07 en BP 4676JAV zijn één object, en 112283303 hoort daarbij [B10] | enige route naar een adres | RC of adres van de aanbieder |
| W5 | De K08-pin in R15 (vier decimalen) is dezelfde als het R11-testpunt [B1, B3, B9] | anders zijn de Catastro-tests niet op K08 van toepassing | volledige pin uit de assistent |
| W6 | Licentie obra mayor in Xàbia: 6–12 maanden vanaf een volledig dossier (type 5) [B3 §4.5] | planning scenario's | 2–3 lokale architecten (type 6) |
| W7 | Landelijke bouwkosten 800–1.200 €/m² zijn een ondergrens voor een Jávea-villa (type 4) en PEM ≈ bouwsom in de illustratie (type 5) | geen eigen nacalculaties beschikbaar [B7 §4.4] | nacalculaties TREE Constructions |
| W8 | De standaardbibliotheek in de Hermes-venv volstaat in fase B voor punt-in-polygoon, afstanden, oppervlakte en bouwvlakken van eenvoudige vormen, en voor een **benaderend** overlapaandeel met een puntraster. Exacte overlap van perceel en zonevlak, buffers en onregelmatige bouwvlakken vragen `shapely`/PostGIS [B1, B2, B5 §11, B13 §2.4, B14 R17-05] | regel: niets installeren zonder akkoord; deliverable 05 kiest variant 1 | eerste perceel dat over een zonegrens loopt of een complexe vorm heeft |
| W9 | Idealista 107655781 (K10), Idealista 111869151 en Servihabitat 06124187 zijn één object [B9, B11, B12] | zes gelijke kenmerken; enige route naar de klasse volgens de verkoper | 16 RC's of een schriftelijke bevestiging van Servihabitat |

### 3.2 Onbekend of tegenstrijdig (type 7)

1. Gelden de NUT na ca. 15-03-2025 nog? [B4 R12-04]
2. Netto (0,20) direct op een bestaande kavel, of eerst aantonen dat de 29,07 %-cessie is voldaan? [B3 §2.2]
3. Zijn de ocupación-percentages 20/30/50 % na Mod. I ongewijzigd? [B4 R12-07]
4. Welk grado geldt per urbanisatie? Plano B.1 is door niemand per perceel gelezen [B4].
5. Normen van PP Ermita II, PP La Guardia-3, PP Cansalades-Umbría; stand van oplevering van urbanisaties in 2026 [B3, B4].
6. Tasas voor licentie, DR, informe urbanístico en cédula in Xàbia [B3, B4].
7. Kust (deslinde, servidumbre 20/100 m) en waterlopen (DPH): MITECO-diensten onbereikbaar; mogelijk gemigreerd, dus "dienst vervallen tot tegendeel bewezen" [B6 F12].
8. ARPSI T100 = 1,951 (eenheid niet vermeld) tegenover PATRICOVA "< 0,8 m" op hetzelfde punt [B6].
9. Of Xàbia is toegetreden tot de Agencia Valenciana de Protección del Territorio (minimización, DT 28) [B6 A1].
10. Levertijd van de nota simple ("24 horas" of "inferior a dos horas") en of die in de praktijk RC en coördinatiestatus toont [B2].
11. Of een licentie en een architectenproject bij verkoop overdraagbaar zijn: in geen enkel onderzoeksrapport onderzocht.
12. Of een koper-in-spe een cédula mag aanvragen ("partes interesadas") [B3].
13. Met welke instelling van het zoekgebied (coördinatenstelsel) de GVA-planningslaag betrouwbaar antwoordt: R12 en R13 meldden verschillend gedrag [B3, B5; details E8].
14. De twee GVA-lagen spreken elkaar op de K07-pin tegen (PP Ermita II tegenover "Plan Parcial Montgó-2 / SUP Montgó-2") [B5].
15. K10: klasse "urbanizable" (Idealista, twee advertenties) of "urbano no consolidado, PGOU UA BALCON AL MAR 1" (Servihabitat); bestaan van een vastgesteld programa en de stand van de reparcelación "Ciudad La Guardia"; verkoop per kavel of als pakket; grond van de btw-plicht (20.Uno.20º of afstand, dus AJD 1,4 % of 2 %) [B9, B11, B12, B7].
16. Wegen (carreteras) en overige infrastructuur over of langs het perceel (leidingen, masten): welke wet per weg geldt, welke afstanden of beperkingen gelden. In geen onderzoeksstroom onderzocht [B3 §3.3].
17. Toegang en erfdienstbaarheden: of ingeschreven erfdienstbaarheden altijd in de nota simple staan, en hoe feitelijke toegang zonder bezoek vast te stellen is. Niet onderzocht [B1, B2].
18. Archeologische zones in de gemeentelijke catálogo (Mod. XVII): niet gelezen [B5 §8.1].

---

## 4. Tegenargumenten of aandachtspunten

**Waarom deze aanpak een deal kan kosten**
- **Snelheid.** Een informe urbanístico heeft een wettelijke termijn van een maand; een goede kavel kan eerder verkocht zijn. Tegenmaatregel om te laten toetsen: een aankoop onder opschortende voorwaarden (bevestigde RC, geldige licentie, informe) of een optie, zoals §22 van de masterprompt noemt. Juridische en fiscale gevolgen eerst laten beoordelen; niets toezeggen zonder Jan.
- **Te streng bij MIDDEL.** Een MIDDEL-koppeling is geen afwijzing maar een onderzoekswachtrij (§23). K07 en K08 blijven "verder onderzoeken", K10 blijft "watchlist".
- **Kosten per perceel.** Nota simple en informe zijn goedkoop, maar architect, topografie en geotechniek niet (bedragen ONBEKEND). Daarom alleen voor kandidaten die stap 8 en 10 zonder harde blokkade doorkomen.

**Waarom we een perceel ook met een HOOG-koppeling mogelijk niet moeten kopen**
- Een geclaimde licentie is geen geldige licentie. Termijnen: start binnen 6, afbouw binnen 24 maanden als de licentie niets anders zegt; verval na hoorzitting; na verval geldt het nieuwe plan (188.2, 244) [B3]. Een licentienummer uit 2020 in een advertentie is een waarschuwing, geen troef [B3 §4.2].
- Een aval de urbanización betekent dat de woning niet gebruikt mag worden vóór oplevering van de urbanisatie, en die voorwaarde gaat mee bij verkoop (187.1) [B4]. In 2013 meldde de gemeente dat zonder oplevering een cédula de habitabilidad en aansluitingen problematisch zijn (verouderde bron) [B3 §5].
- "Urbanizable" is geen bouwrecht; zonder vastgesteld programa zijn woningen verboden (226) [B3, B4].
- Montgó-flank: extra rapport van de Conselleria bij grondverzet en aansluitingen (PORN 109.5), met onbekende doorlooptijd [B6].
- Brand: na de afbakening van de bos-bebouwingsgrens hebben eigenaren zes maanden voor bijlage XI (strook tot 30 m, onderhoud elke 2 en 4 jaar voor eigen rekening) [B5, B6 A7].
- Advertentieparameters die exact op de PGOU-tabel lijken (K09) kunnen overgeschreven zijn, terwijl een plan parcial andere normen heeft [B10 R15-08].

**Wat de bronnen niet kunnen**
- "Geen beperking gevonden" is niet "geen beperking aanwezig": PATIVEL-ámbitos zijn lijnen (punt-in-polygoon geeft altijd 0), de brandinterface is een raster van ±500 m, de kustdeslinde was onbereikbaar [B5].
- Catastro bewijst geen eigendom, bouwrecht of legaliteit; de GVA-planningslaag is "carácter informativo" en bevat een vernietigde homologación [B1, B4].
- Idealista-velden spreken de tekst tegen; de assistent gedraagt zich niet deterministisch (filter, genegeerd of trefwoord) [B10].
- Drie BP-objecten in Jávea hebben een nepcoördinaat in Florida; BP 4104JAV heeft er geen [B6, C64].
- Wegen, toegang en erfdienstbaarheden zijn met geen enkele open dienst te toetsen; archeologische zones buiten het Inventario staan in een gemeentelijke catálogo die niemand heeft gelezen [B3 §3.3, B5 §8.1].
- Eén object kan per kanaal een andere planklasse hebben (K10: "urbanizable" op Idealista, "urbano no consolidado" bij de verkoper). Het kanaal dat het dichtst bij de eigenaar staat is een aanwijzing, geen bewijs [B11, B12].

**Rechten, licenties en privacy**
- **Catastro:** eigen gebruik en getransformeerde producten mogen; de originele gegevens verspreiden niet, en een eigen product mag niet "cartografía catastral" of "información catastral" heten [B2 A1]. Een dossier voor een investeerder of klant bevat dus onze analyse met bronvermelding, geen ongewijzigde Catastro-bestanden.
- **Servihabitat:** "Queda prohibida cualquier modalidad de explotación"; Solvia en Diglo hebben vergelijkbare verboden. Dus alleen handmatig lezen, geen crawler [B12 R10-14].
- **GVA/ICV:** CC BY 4.0, bronvermelding "Generalitat Valenciana / ICV" [B3]. **IGME:** contact vereist voor een betaalde dienst met toegevoegde waarde [B5]. **IDEE/MITECO:** vermelding MITECO [B5].
- **Nota simple:** vraagt een legitiem belang; naam, adres en DNI van de aanvrager worden 3 jaar bewaard [B2 A4]. Niet "voor de zekerheid" of in een lus aanvragen.
- **Persoonsgegevens:** een nota simple bevat eigenaarsgegevens. Alleen in het dossier bewaren voor zover nodig; geen persoonsprofielen; geen ongevraagde benadering van particuliere eigenaren (masterprompt §19, §26). In advertenties van particulieren geen namen of telefoonnummers overnemen [B2 A11].

---

## 5. Concrete vervolgstap

### 5.1 De komende stappen (in volgorde)

| # | Actie | Wie | Voorwaarde | Resultaat |
|---|---|---|---|---|
| 1 | Keten stap 3–5, 8 en 10 draaien voor de open punten: adresdienst [E2] op "MAR AMARILLO 300"; Catastro op de K07-pin en de BP-pin van 4676JAV; perceelpolygonen van 0281202, 2944017 en 2944012 over de GVA-planningslaag en de sectorale lagen leggen (ca. 20–30 verzoeken, één per dienst per perceel) | Deal Hunter-sessie | besluit 3 van Jan | K07/K08 van "signaal op pin" naar "signaal op kandidaat-perceel" |
| 2 | Conceptberichten aan Atina Inmobiliaria / BP (K07) en Grupo García (K08) klaarzetten met de documentvragen uit §2.6; **niet verzenden** | Deal Hunter-sessie; verzending door of na "ja" van Jan | besluit 1 | RC, licentie, project, aval |
| 3 | ⏸️ ACTIE VOOR JAN — een lokale architect (of urbanismo-advocaat) aanwijzen voor de vragen van §5.3 | Jan | — | bewijstype 6 voor de interpretaties |
| 4 | Na bevestigde RC van K07: nota simple van dat perceel en een informe urbanístico (art. 246.4) met de gemeentevragen G1–G7 | Jan of architect | besluit 2 | poort 1 en 2 voor K07 |
| 5 | ⏸️ ACTIE VOOR JAN — bij het Ajuntament de Xàbia opvragen: texto refundido van de normas urbanísticas, ordenanzas van PP Ermita II, ordenanzas fiscales (tasas licencia, informe, cédula) | Jan of architect | — | vult §2.3 punten 2–16 en 21 aan |
| 6 | MITECO-deslinde opnieuw proberen; download van `dpmt.zip` (12,2 MB) pas met akkoord van Jan | Deal Hunter-sessie | akkoord download | kusttoets 20/100 m |
| 7 | K10: adresdienst op Sergei Rachmaninov 4 en 8, planlaag en sectorale lagen (incl. PATIVEL) als eerste signaal op de perceelpolygonen die de adresdienst oplevert, niet op de pin (stap 8); conceptvraag aan Servihabitat om de 16 RC's, de ficha en het biedreglement klaarzetten; **niet verzenden** | Deal Hunter-sessie; verzending na "ja" van Jan | besluit 1 en 3 van Jan (zelfde soort contact en diensten als K07/K08) | klassesignaal en RC's; stop of S5-dossier |
| 8 | Bij de eerste nota simple controleren of erfdienstbaarheden en afecciones zichtbaar zijn; bij het eerste bezoek toegang en bereikbaarheid voor bouwverkeer vastleggen | Jan of architect | besluit 2 | invulblad §2.3-D, rijen toegang en lasten |

### 5.2 Wat dit betekent voor het systeem (fase B)

- De zekerheidsregels van stap 6 als geteste code, met regressietests op de echte gevallen uit R11: Mar Amarillo 5 (HOOG via adres), Rafalet-pin (MIDDEL), 112256480 (LAAG), 103305763 (RC in tekst faalt op oppervlakte), Villes del Vent (twee pins, twee klassen), K10 (drie advertenties in twee kanalen, twee klassen, btw in plaats van ITP: het systeem moet het cluster vormen, het klasseconflict tonen en geen bouwvolume geven). Dat dekt de testeisen "onjuiste locatiepinnen", "grondprijzen met voorbeeldwoningen", "verkeerde perceelkoppelingen" en "plannen die nog niet gelden" uit §28.
- **Acceptatiecriterium:** bij MIDDEL of LAAG verschijnt nergens een bouwvolume, en bij elk getal in het bouwmogelijkhedenoverzicht staat een document, artikel, status en bewijstype.
- Regeltabel voor PGOU-zona E en SNU als versiebeheerd bestand (waarde, document, artikel, kaartblad, status, datum, bewijstype), met de vlag "alleen buiten planes parciales".
- Per laag een dienststatus ("bereikbaar", "fout", "vervallen", "niet getoetst") en een datum van laatste controle; nooit "geen beperking". Wegen, toegang, erfdienstbaarheden en de gemeentelijke catálogo hebben standaard de status "niet getoetst".
- **Zoneringsrecord per perceel** (de invoer die deliverable 05 voor test T10 vraagt): klasse, instrument (PGOU, PP, PRI, UA), zone en grado, document met versie, datum en status (geldend, in procedure, vernietigd), artikel of kaartblad, bewijstype, controledatum, en een vlag "klasse tegenstrijdig tussen bronnen". In fase B vult Jan of de architect dit record na poort 2 in; stap 8 levert alleen het signaal (zie stap 8, afstemming met deliverable 05).
- Catastro-antwoorden cachen op RC, GVA-lagen per laag; geen sweep over heel Jávea [B1, B2, B5].

### 5.3 Openstaande interpretatievragen

**Aan de gemeente (schriftelijk, via informe urbanístico of cédula):**

| # | Vraag | Waarom | Bron |
|---|---|---|---|
| G1 | Worden de NUT (DOGV 20-09-2021) na ca. 15-03-2025 nog toegepast, of geldt het PGOU 1990/1991 weer volledig in casco en zona E? | conflict C1; raakt hoogte, dak, riolering | [B3, B4] |
| G2 | Past de gemeente 0,20 m²t/m² netto direct toe op kavels in ontsloten zona E-urbanisaties, of toetst ze per perceel de 29,07 %-cessie (anders 0,142 × bruto)? | tot 29 % verschil in m²t | [B3] |
| G3 | Welk grado geldt volgens plano B.1 voor Garroferal/Montgó-Ermita, El Rafalet, Pinosol, Tosalet, Cap Martí en Balcón al Mar, en zijn de ocupación-percentages na Mod. I ongewijzigd? | footprint 20/30/50 % | [B3, B4] |
| G4 | K07: valt het perceel onder PP Ermita II of onder het PG (SU)? Welke ordenanzas gelden? Is de urbanisatie opgeleverd? Welke licentie is verleend (nummer, datum, houder, termijnen) en is die nog geldig? | stop K07 | [B4, B6] |
| G5 | K08: is het perceel SU of SUZ, ligt het in een UA of plan, is er een vastgesteld programa, en bestaat de geclaimde licentie? | stop K08 | [B3, B9] |
| G6 | Weigert de gemeente licenties op grond van het niet-goedgekeurde PGE, en wat zou het PGE-voorstel op deze percelen veranderen? | conflict C2; risico-informatie | [B3] |
| G7 | Mag een koper-in-spe een cédula de garantía urbanística aanvragen, en wat zijn de tasas voor informe, cédula, licencia obra mayor en DR? | route en kosten | [B3, B4] |
| G8 | Legt de gemeente in SU de eisen van PATRICOVA-bijlage I op (vloerpeil 80 cm boven straat, kelderverbod) in l'Arenal en el Saladar? | ontwerp en kosten | [B5] |
| G9 | Wat is de cartografie van de bos-bebouwingsgrens (pleno 28-05-2026 volgens de GVA-laag) en vanaf wanneer loopt de termijn van zes maanden? | brandstrook | [B5, B6] |
| G10 | Is Xàbia toegetreden tot de Agencia Valenciana de Protección del Territorio (minimización)? | bestaande bouw in SNU | [B6] |
| G11 | Is Mod. nº 41 (VUT) met de licentieschorsing al in de BOP gepubliceerd? | verhuurscenario's | [B4] |
| G12 | Werkt de gemeente met ECUV's (art. 239.3) en levert dat tijdwinst op? | doorlooptijd | [B3] |
| G13 | Per perceel: grenst het aan een openbare weg, welke weg is het (gemeente, provincie, regio of staat), en geldt er een afstand of beschermingsstrook? | wegen en toegang niet onderzocht | [B3 §3.3] |
| G14 | K10: is de grond "urbanizable" of "urbano no consolidado" in de "UA Balcón al Mar 1"? Is er een vastgesteld programa, wat is de stand van de reparcelación "Ciudad La Guardia", wat is het lastenaandeel bij 26,85 %, en welke normen gelden? | S0 of S5 | [B9, B11, B12] |

**Aan de lokale architect:**

| # | Vraag | Waarom | Bron |
|---|---|---|---|
| A1 | Hoe telt de gemeente een overdekt terras of naya die "no esté cerrado por alguno de sus frentes" voor edificabilidad (half of vol) en voor ocupación? | ontwerpruimte | [B3 §2.3c] |
| A2 | Hoe wordt de kelderregel (plafond < 1,20 m boven natuurlijk terrein op alle punten van de omtrek, ≥ 2,5 m van de grens) op hellende kavels toegepast? | m² onder de woning | [B3 art. 8.1.27] |
| A3 | Telt een onoverdekt zwembad mee voor ocupación, en vraagt het op de Montgó-flank een PORN-rapport (grondverzet, 109.5.f)? | zwembad is standaard in het segment | [B3, B6 F6] |
| A4 | Wat is de geldende formule voor keermuren en hun tussenafstand bij helling (art. 8.1.23.2; OCR onleesbaar)? | kosten hellende kavels (K08) | [B3] |
| A5 | Welke oppervlakte accepteert de gemeente bij de licentie: Catastro, registraal of topografisch? | R7 | [B1, B2] |
| A6 | Past het villaproject van 310 m² bij K07 binnen de normen van PP Ermita II, en is aanpassing van het ontwerp mogelijk zonder nieuwe licentie? | waarde van scenario S1b | [B9] |
| A7 | Hoe worden frente 20 m, de rechthoek 15 × 24 m en de uitzondering (> 70 % en ≥ 700 m²) toegepast op onregelmatige kavels? | drempel bebouwbaarheid | [B3, Mod. XXV] |
| A8 | Hoe lang duurt een Estudio de Detalle voor een parcela mancomunada of agrupación in Xàbia, en is het haalbaar? | scenario S2 | [B3] |
| A9 | Welke doorlooptijd voor een licentie obra mayor ziet u in 2026 (ter vervanging van werkhypothese W6)? | planning | [B3 §4.5] |

**Aan een urbanismo-advocaat, hydraulisch ingenieur of kustjurist (alleen waar het speelt):**
- J1: Geldt het landbouwrapport van art. 211.1.b voor elke nieuwe woning in SNU? [B4]
- J2: Geldt de niet-verjaring in SNU (255.5) ook voor gebouwen die onder oud recht al verjaard waren (255.6)? [B5]
- J3: Welke overstromingsuitkomst geldt bij ARPSI T100 = 1,951 tegenover PATRICOVA "< 0,8 m" (voorzorgsbeginsel, PATRICOVA art. 10.2)? [B5, B6]
- J4: Was l'Arenal op 29-07-1988 stedelijk (servidumbre 20 m) of niet (100 m)? [B5]
- J5 (gestor of fiscalist): Waarom is de verkoop van K10 "sujeta y no exenta de IVA" (grond in urbanisatie of afstand van vrijstelling), dus AJD 1,4 % of 2 %, en is de btw voor de beoogde koopentiteit aftrekbaar? [B7 §1.3–1.4, B8 R14-06, B12 A3]
- J6 (urbanismo-advocaat): Wat houdt een aandeel van 26,85 % (K10) of een onverdeeld aandeel van 72,22 % (Sareb-perceel B) in een UA juridisch in: welke lasten en plichten gaan mee bij koop? [B11 §6]

---

## Bijlage A — Technische adressen en valkuilen (voor de bouwer van fase B)

Alle diensten open en zonder sleutel, getest op 14 of 15-09-2026 door R11–R13 of hun tegenspraak (type 3), tenzij anders vermeld. Geen sleutels of privé-feed-URL's opgenomen.

| Code | Dienst | Adres (met parameters) | Getest gedrag en valkuilen | Bron |
|---|---|---|---|---|
| E0 | Eigen BP-dienst (alleen lezen) | `http://127.0.0.1:3100/api/properties?town=Javea&limit=100` | plaatsnaamfilter is accentgevoelig: "Jávea" en "Xabia" geven 0 | [B10, C64] |
| E1 | Catastro: gegevens bij een RC (Consulta_DNPRC, JSON) | `https://ovc.catastro.meh.es/OVCServWeb/OVCWcfCallejero/COVCCallejero.svc/json/Consulta_DNPRC?Provincia=&Municipio=&RefCat={RC}` | parameter heet `RefCat`; `RC=` geeft fout 17. Velden: gebruik `luso`, gebouwde m² `sfc`, bouwjaar `ant`, perceel-m² `ss`; `ltp` alleen bij bebouwde percelen. Patroon voor stedelijke RC's in tekst: `[0-9]{7}[A-Z]{2}[0-9]{4}[A-Z]([0-9]{4}[A-Z]{2})?`; landelijke RC's hebben een ander formaat (voorbeeld 03082A01200623); de rústica-dienst Consulta_DNPPP is niet getest | [B1, B2 A14, B5, C4] |
| E2 | Catastro: RC bij een adres (Consulta_DNPLOC) | `https://ovc.catastro.meh.es/OVCServWeb/OVCWcfCallejero/COVCCallejero.svc/json/Consulta_DNPLOC?Provincia=ALICANTE&Municipio=JAVEA/XABIA&Sigla=CL&Calle={straat}&Numero={nr}` | getest op Mar Amarillo 4 en 5 en Pic de Rebalsadors 30 | [B1, B2, C5] |
| E3 | Catastro: percelen rond een coördinaat (Consulta_RCCOOR_Distancia) | `https://ovc.catastro.meh.es/ovcservweb/OVCSWLocalizacionRC/OVCCoordenadas.asmx/Consulta_RCCOOR_Distancia?SRS=EPSG:4326&Coordenada_X={lon}&Coordenada_Y={lat}` | de JSON-variant van RCCOOR vraagt `CoorX/CoorY`: ongedocumenteerd, met regressietest bewaken | [B2, C2, C6] |
| E4 | Catastro INSPIRE-kaartdienst percelen (WFS), rechthoek | `https://ovc.catastro.meh.es/INSPIRE/wfsCP.aspx?service=wfs&version=2&request=GetFeature&Typenames=cp.cadastralparcel&bbox={lat1},{lon1},{lat2},{lon2}&srsname=EPSG::4326` | geen paginering: een rechthoek van ca. 0,87 km² meldde 486 percelen en leverde er 477 | [B2, C7] |
| E5 | Catastro INSPIRE-kaartdienst: omtrek van één perceel (GetParcel) | `https://ovc.catastro.meh.es/INSPIRE/wfsCP.aspx?service=wfs&version=2&request=GetFeature&STOREDQUERIE_ID=GetParcel&refcat={RC14}&srsname=EPSG::4326` | in EPSG::4326 staan coördinaten in volgorde breedte-lengte; voor oppervlakte `srsname=EPSG::25830`. Het ATOM-gemeentebestand van Xàbia staat in EPSG:25831 (UTM-zone 31), niet 25830: wie een pin zelf naar UTM omrekent, gebruikt zone 31. Oppervlakte uit hoekpunten met de "shoelace"-formule (standaardbibliotheek) | [B2, C7, C10] |
| E6 | Catastro INSPIRE-kaartdienst gebouwen | `https://ovc.catastro.meh.es/INSPIRE/wfsBU.aspx` met `STOREDQUERIE_ID=GetBuildingByParcel` | — | [C8] |
| E7 | Catastro Sede: "Consulta descriptiva y gráfica" (pdf) | `https://www1.sedecatastro.gob.es/CYCBienInmueble/SECImprimirCroquisYDatos.aspx?del=3&mun=82&refcat={RC20}` | interactieve dienst: alleen handmatig; "no es una certificación catastral" | [B2, C15] |
| E8 | GVA/ICV planeamiento (WFS) | `https://terramapas.icv.gva.es/0702_Planeamiento`, typenames `ms:Planeamiento.Clasificacion` en `ms:Planeamiento.Zonificacion` | werkend: GetFeatureInfo of GetFeature met bbox. R13 kreeg alleen resultaat met een bbox in EPSG:25830, R12 met een kleine bbox rond het punt; een attribuutfilter gaf een serverfout. Bevat nog 20 vlakken van de vernietigde Portitxol-homologación | [B3, B4, B5, C27] |
| E9 | GVA/ICV infraestructura verde (WFS/WMS) en ArcGIS ordenación territorial | `https://terramapas.icv.gva.es/0701_InfraestructuraVerde` (laag `IVR.Inundacion`, GetFeatureInfo `INFO_FORMAT=geojson`); `https://carto.icv.gva.es/arcgis/rest/services/tm_infraestructuras/ordenacion_territorial/MapServer` (PATRICOVA lagen 4–10; PATIVEL Litoral laag 34; ámbito-lagen 30–32 zijn lijnen) | ArcGIS `query` met een omtrek (`esriGeometryPolygon`, inSR 25830) geeft de geraakte vlakken; punt-in-polygoon op lagen 30–32 geeft altijd 0, dus afstand berekenen | [B5 §3, §5.4, §11; B6; C32, C33] |
| E10 | IDEE ARPSI overstromingsrisico (WMS) | `https://servicios.idee.es/wms-inspire/riesgos-naturales/inundaciones` | eenheid van de waarde niet vermeld; "999" is een onbekende code | [B6, C46] |
| E11 | GVA/ICV PORN Montgó | `https://terramapas.icv.gva.es/0505_PORN` (`Montgo.PORN`, `Montgo.Zonificacion`, `Montgo.Parque`) | — | [B6, C35] |
| E12 | Red Natura 2000 | 0701 `IVR.ZEC`, `IVR.LIC`, `IVR.ZEPA`; `https://carto.icv.gva.es/arcgis/rest/services/tm_medio_ambiente/espacios_protegidos/MapServer` laag 21 | Montgó alleen als LIC | [B6, C39] |
| E13 | PATFOR en brand | `https://terramapas.icv.gva.es/0506_PATFOR`; `https://carto.icv.gva.es/arcgis/rest/services/tm_medio_ambiente/prevencion_de_incendios/MapServer` (lagen 8, 71, 104, 114, 123) | interface is een raster (cel ±500 m) | [B5, B6, C37, C38] |
| E14 | MITECO kustdomein (DPMT) | `https://wms.mapama.gob.es/sig/Costas/DPMT`; `https://gis.miteco.gob.es/web/dpmt`; download `dpmt.zip` via C45 | **niet werkend** op 15-09-2026 (NullReferenceException, verbindingsreset, 503); download vraagt akkoord | [B6, C44, C45] |
| E15 | MITECO waterlopen (DPH) | adres niet vastgelegd in R13 | **niet werkend** (zelfde storing) | [B5] |
| E16 | Minimización SNU | 0702 `MinimizacionViviendasSNU` | niet hercontroleerd in B6 | [B5] |
| E17 | Erfgoed | 0701 `IVR.Cultura.BIC.*`, `IVR.Cultura.BRL` | gemeentelijke catálogo zit niet in deze lagen | [B5 §8.1] |
| E18 | IGME geologische kaart 1:50.000 (WMS) | `https://mapas.igme.es/gis/services/Cartografia_Geologica/IGME_Geode_50/MapServer/WMSServer` | geen geotechniek | [B5, C47] |

Laagvolume-regel voor alle Catastro-diensten: per kandidaat, met cache op RC; bij overschrijding van een onbekende drempel volgt weigering "generalmente 10 días" [B2 R11-11].

---

## Bronnenlijst (URL · controledatum · bewijstype)

**Onderzoeksbestanden (intern)**
- [B1] R11 Catastro, Registro en perceelidentificatie — `/Users/root-admin/tree-es/deal-hunter/onderzoek/R11-catastro-registro-perceelidentificatie.md` · 14-09-2026 · 2/3/5
- [B2] R11 tegenspraak — `/Users/root-admin/tree-es/deal-hunter/onderzoek/R11-catastro-registro-perceelidentificatie.verificatie.md` · 15-09-2026 · 2/3/5
- [B3] R12 Urbanisme Xàbia — `/Users/root-admin/tree-es/deal-hunter/onderzoek/R12-urbanisme-xabia-plan-en-vergunning.md` · 15-09-2026 · 2/3
- [B4] R12 tegenspraak — `/Users/root-admin/tree-es/deal-hunter/onderzoek/R12-urbanisme-xabia-plan-en-vergunning.verificatie.md` · 15-09-2026 · 2/3
- [B5] R13 Regionaal, sectoraal, geoportalen — `/Users/root-admin/tree-es/deal-hunter/onderzoek/R13-regionaal-sectoraal-geoportalen.md` · 15-09-2026 · 2/3/5
- [B6] R13 tegenspraak — `/Users/root-admin/tree-es/deal-hunter/onderzoek/R13-regionaal-sectoraal-geoportalen.verificatie.md` · 15-09-2026 · 2/3/5
- [B7] R14 Financieel, fiscaal, kostenkengetallen — `/Users/root-admin/tree-es/deal-hunter/onderzoek/R14-financieel-fiscaal-kostenkengetallen.md` · 14/15-09-2026 · 1/2/5
- [B8] R14 tegenspraak — `/Users/root-admin/tree-es/deal-hunter/onderzoek/R14-financieel-fiscaal-kostenkengetallen.verificatie.md` · 15-09-2026 · 1/2
- [B9] R15 Kandidaten Jávea live — `/Users/root-admin/tree-es/deal-hunter/onderzoek/R15-kandidaten-javea-live.md` · 14-09-2026 · 1/3
- [B10] R15 tegenspraak — `/Users/root-admin/tree-es/deal-hunter/onderzoek/R15-kandidaten-javea-live.verificatie.md` · 15-09-2026 · 1/3
- [B11] R10 Banken, servicers en fondsen — `/Users/root-admin/tree-es/deal-hunter/onderzoek/R10-banken-servicers-fondsen.md` · 15-09-2026 · 1/3
- [B12] R10 tegenspraak — `/Users/root-admin/tree-es/deal-hunter/onderzoek/R10-banken-servicers-fondsen.verificatie.md` · 15-09-2026 · 1/3
- [B13] R17 Architectuur, MVP en kosten — `/Users/root-admin/tree-es/deal-hunter/onderzoek/R17-architectuur-mvp-kosten.md` · 14/15-09-2026 · 2/3/4
- [B14] R17 tegenspraak — `/Users/root-admin/tree-es/deal-hunter/onderzoek/R17-architectuur-mvp-kosten.verificatie.md` · 15-09-2026 · 2/3
- Deliverable 05 (bouwplan fase B), §3.4 en Deel 4, alleen gelezen voor de afstemming in stap 8 — `/Users/root-admin/tree-es/deal-hunter/05-bouwplan-fase-b-mvp.md` · 15-09-2026 · 4

**Catastro en Registro**
- [C1] https://ovc.catastro.meh.es/ovcservweb/OVCSWLocalizacionRC/OVCCoordenadas.asmx/Consulta_RCCOOR · 14/15-09-2026 (via B1/B2) · 3
- [C2] https://ovc.catastro.meh.es/ovcservweb/OVCSWLocalizacionRC/OVCCoordenadas.asmx/Consulta_RCCOOR_Distancia · 14/15-09-2026 · 3
- [C3] https://ovc.catastro.meh.es/ovcservweb/OVCSWLocalizacionRC/OVCCoordenadas.asmx/Consulta_CPMRC · 15-09-2026 · 3
- [C4] https://ovc.catastro.meh.es/OVCServWeb/OVCWcfCallejero/COVCCallejero.svc/json/Consulta_DNPRC · 14/15-09-2026 · 3
- [C5] https://ovc.catastro.meh.es/OVCServWeb/OVCWcfCallejero/COVCCallejero.svc/json/Consulta_DNPLOC · 14/15-09-2026 · 3
- [C6] https://ovc.catastro.meh.es/OVCServWeb/OVCWcfCallejero/COVCCoordenadas.svc/json/Consulta_RCCOOR · 14/15-09-2026 · 3
- [C7] https://ovc.catastro.meh.es/INSPIRE/wfsCP.aspx · 14/15-09-2026 · 3
- [C8] https://ovc.catastro.meh.es/INSPIRE/wfsBU.aspx · 14-09-2026 · 3
- [C9] https://ovc.catastro.meh.es/cartografia/INSPIRE/spadgcwms.aspx · 15-09-2026 · 3
- [C10] https://www.catastro.hacienda.gob.es/INSPIRE/CadastralParcels/03/ES.SDGC.CP.atom_03.xml · 15-09-2026 · 3
- [C11] https://www.catastro.hacienda.gob.es/ws/Webservices_Libres.pdf (v2.6) · 15-09-2026 · 2
- [C12] https://www.catastro.hacienda.gob.es/ayuda/condicionesuso.htm · 15-09-2026 · 2
- [C13] https://www.catastro.hacienda.gob.es/webinspire/documentos/Licencia.pdf · 15-09-2026 · 2
- [C14] https://www.catastro.hacienda.gob.es/documentos/normativa/res_230311.pdf · 15-09-2026 · 2
- [C15] https://www1.sedecatastro.gob.es/CYCBienInmueble/SECImprimirCroquisYDatos.aspx?del=3&mun=82&refcat=2944017BC5924S0001AL · 15-09-2026 · 3
- [C16] https://www1.sedecatastro.gob.es/Accesos/SECAccvr.aspx · 15-09-2026 · 3
- [C17] https://www.registradores.org/el-colegio/registro-de-la-propiedad · 15-09-2026 · 2
- [C18] https://www.registradores.org/en/-/cuando-cuesta-una-nota-simple-en-un-registro-de-la-propiedad · 15-09-2026 · 2
- [C19] https://www.boe.es/buscar/act.php?id=BOE-A-1946-2453 (Ley Hipotecaria, art. 9, 10) · 15-09-2026 · 2
- [C20] https://www.boe.es/buscar/act.php?id=BOE-A-2015-7046 (Ley 13/2015) · 15-09-2026 · 2

**Planologie Xàbia en regionale wetgeving**
- [C21] https://mediambient.gva.es/auto/urbanismo/reg-planeamiento/2%20ALICANTE/03082%20X%C0BIA/ · 15-09-2026 · 2
- [C22] https://mediambient.gva.es/auto/urbanismo/reg-planeamiento/2%20ALICANTE/03082%20X%C0BIA/1%20P.%20GENERAL/03082-1000%20PLAN%20GENERAL/3%20NORMAS%20URBAN%CDSTICAS/03082-1000%20ORDENANZAS.pdf · 15-09-2026 · 2
- [C23] https://mediambient.gva.es/auto/urbanismo/reg-planeamiento/2%20ALICANTE/03082%20X%C0BIA/1%20P.%20GENERAL/03082-1101%20PGMOD%20N%BA%20XXV%20CONDICIONES%20PARCELAS/1%20APROBACI%d3N/03082-1101%20PUBLICACI%d3N%20BOP.pdf · 15-09-2026 · 2
- [C24] https://dogv.gva.es/datos/2021/03/15/pdf/docv_9041.pdf · 15-09-2026 · 2
- [C25] https://dogv.gva.es/datos/2021/09/20/pdf/docv_9177.pdf · 15-09-2026 · 2
- [C26] https://www.boe.es/buscar/act.php?id=DOGV-r-2021-90283 (TRLOTUP, geconsolideerd tot 02-07-2026) · 15-09-2026 · 2
- [C27] https://terramapas.icv.gva.es/0702_Planeamiento?service=WFS&request=GetCapabilities · 15-09-2026 · 2 (dienst) / 3 (tests)
- [C28] https://datos.gob.es/es/catalogo/a10002983-planeamiento-urbanistico-de-la-comunitat-valenciana-clasificacion-urbanistica · 15-09-2026 · 2
- [C29] https://www.ajxabia.com/ver/7823/el-pleno-aprueba-la-propuesta-definitiva-de-plan-general-estructural-.html/ · 15-09-2026 · 2
- [C30] https://lamarina.eldiario.es/2025/02/17/generalitat-advierte-xabia-responsabilidad-licencias-plan-general-no-aprobado/ · 15-09-2026 · 1
- [C31] https://serviciostelematicosext.hacienda.gob.es/SGFAL/ConsultaTipos/aspx/descargaPDF.aspx?URLPDF=2026/C.VALENCIANA/Alicante.pdf · 15-09-2026 · 2

**Sectorale lagen en wetten**
- [C32] https://terramapas.icv.gva.es/0701_InfraestructuraVerde · 15-09-2026 · 3
- [C33] https://carto.icv.gva.es/arcgis/rest/services/tm_infraestructuras/ordenacion_territorial/MapServer · 15-09-2026 · 3
- [C34] https://mediambient.gva.es/documents/20551069/162377494/02+Normativa.pdf/5d2bca03-0f7f-4774-b602-4447cfb8dce7 (PATRICOVA) · 15-09-2026 · 2
- [C35] https://terramapas.icv.gva.es/0505_PORN · 15-09-2026 · 3
- [C36] https://dogv.gva.es/datos/2002/11/08/pdf/2002_12109.pdf (PORN Montgó) · 15-09-2026 · 2
- [C37] https://terramapas.icv.gva.es/0506_PATFOR · 15-09-2026 · 3
- [C38] https://carto.icv.gva.es/arcgis/rest/services/tm_medio_ambiente/prevencion_de_incendios/MapServer · 15-09-2026 · 3
- [C39] https://carto.icv.gva.es/arcgis/rest/services/tm_medio_ambiente/espacios_protegidos/MapServer · 15-09-2026 · 3
- [C40] https://dogv.gva.es/datos/2022/11/28/pdf/2022_11078.pdf (Decreto 197/2022) · 15-09-2026 · 2
- [C41] https://www.boe.es/buscar/act.php?id=BOE-A-2025-11647 (Ley 3/2025 costa valenciana) · 15-09-2026 · 2
- [C42] https://www.boe.es/buscar/act.php?id=BOE-A-1988-18762 (Ley 22/1988 de Costas) · 15-09-2026 · 2
- [C43] https://www.boe.es/buscar/act.php?id=BOE-A-2001-14276 (RDL 1/2001 Aguas) · 15-09-2026 · 2
- [C44] https://wms.mapama.gob.es/sig/Costas/DPMT en https://gis.miteco.gob.es/web/dpmt (mislukt) · 15-09-2026 · 3
- [C45] https://www.miteco.gob.es/es/cartografia-y-sig/ide/descargas/costas-medio-marino/deslinde-dpmt.html · 15-09-2026 · 2
- [C46] https://servicios.idee.es/wms-inspire/riesgos-naturales/inundaciones · 15-09-2026 · 3
- [C47] https://mapas.igme.es/gis/services/Cartografia_Geologica/IGME_Geode_50/MapServer/WMSServer · 15-09-2026 · 3
- [C48] https://www.boe.es/buscar/act.php?id=BOE-A-1998-17524 (Ley 4/1998 Patrimonio Cultural Valenciano) · 15-09-2026 · 2
- [C49] https://mediambient.gva.es/auto/planes-accion-territorial/PATIVEL/ · 15-09-2026 · 2
- [C50] https://amjasa.com/quienessomos/ en https://www.i-de.es/grid-connection/electric-supply · 15-09-2026 · 2

**Fiscaal en kosten**
- [C51] https://www.boe.es/buscar/act.php?id=BOE-A-1998-8202 (Ley 13/1997 CV, ITP/AJD) · 15-09-2026 · 2
- [C52] https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740 (Ley 37/1992 IVA) · 15-09-2026 · 2
- [C53] https://www.boe.es/buscar/act.php?id=BOE-A-2004-4214 (TRLRHL, art. 102) · 15-09-2026 · 2
- [C54] https://www.habitissimo.es/presupuestos/construccion-casas (bijgewerkt 18-06-2026) · 15-09-2026 · 1
- [C55] https://www.habitissimo.es/presupuestos/construccion-piscinas · https://www.habitissimo.es/presupuestos/muro-contencion · https://www.habitissimo.es/presupuestos/demolicion · 15-09-2026 · 1

**Advertenties en eigen feed** (Idealista-URL's zoals de officiële assistent ze gaf, patroon `https://www.idealista.com/es/inmueble/<code>/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail`; inhoud type 1, bestaan type 3)
- [C56] K07 https://www.idealista.com/es/inmueble/112280961/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail · 14/15-09-2026
- [C57] 112283303 (dubbel K07, adres zichtbaar), zelfde patroon · 15-09-2026
- [C58] 112256480 (dubbel K07, adres verborgen), zelfde patroon · 15-09-2026
- [C59] K08 https://www.idealista.com/es/inmueble/90705084/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail · 14/15-09-2026
- [C60] K09 109915149 en 111340209, zelfde patroon · 15-09-2026
- [C61] K10 107655781 en K11 111856637, zelfde patroon · 15-09-2026
- [C62] 112433736 en 36575877 (Mar Amarillo 5), zelfde patroon · 15-09-2026
- [C63] 103305763 (RC in tekst), zelfde patroon · 15-09-2026
- [C64] Eigen BP-dienst, alleen gelezen: http://127.0.0.1:3100/api/health en http://127.0.0.1:3100/api/properties?town=Javea&limit=100 (224 objecten, 56 "Javea"; 4676JAV en 4104JAV) · 15-09-2026 03:59 CEST · 3 (feedinhoud 1). Geen sleutels of privé-feed-URL's overgenomen.
- [C65] https://backgroundproperties.com/en/property/4676jav-spacious-plot-with-building-permit-for-sale-on-the-montgo-javea/ · https://backgroundproperties.com/en/property/4104jav-plot-for-sale-in-javea/ (publieke objectpagina's, uit de feed) · 15-09-2026 · 1

**Overig**
- [C66] https://alicanteplaza.es/alicanteplaza/xabia-planea-contratar-a-mas-personal-en-urbanismo-para-acabar-con-las-demoras-de-un-ano-en-licencias-de-obras (27-11-2023) · 15-09-2026 · 1
- [C67] https://en.javea.com/xabia-aprueba-la-regulacion-de-las-viviendas-turisticas-limite-por-barrios-y-suspension-de-nuevas-licencias/ (06-06-2026) · 15-09-2026 · 1
- [C68] https://www.dogv.gva.es/datos/2020/07/29/pdf/2020_6092.pdf (PLPIF Jávea) · 15-09-2026 · 2

**Aanvulling kritiekronde 15-09-2026** (via B7, B8, B11, B12; niet opnieuw zelf geopend)
- [C69] https://www.boe.es/buscar/act.php?id=BOE-A-1989-28111 (RD 1426/1989, arancel notarios) · 15-09-2026 (B8) · 2
- [C70] https://www.boe.es/buscar/act.php?id=BOE-A-1989-28112 (RD 1427/1989, arancel registradores) · 15-09-2026 (B8) · 2
- [C71] https://serviciostelematicosext.hacienda.gob.es/SGFAL/ConsultaTipos/aspx/ImpuestosExcel.aspx?provincia=TODAS&anosel=2026 (gemeentelijke tarieven 2026: IBI en ICIO Xàbia) · 15-09-2026 (B8) · 2
- [C72] https://www.bde.es/webbe/es/estadisticas/compartido/datos/pdf/a1901.pdf en https://www.bde.es/webbe/es/estadisticas/compartido/datos/pdf/a1903.pdf (Banco de España, tabellen 19.1 en 19.3) · 15-09-2026 (B8) · 2
- [C73] Servihabitat Profesionales, Sareb-perceel A: https://inversores.servihabitat.com/es/venta/promociones/terreno-urbanonoconsolidado/alicante-marinaalta-balconalmarjavea/06124187 · 15-09-2026 (B11, B12) · 1 (inhoud) / 3 (gezien)
- [C74] Servihabitat Profesionales, Sareb-perceel B: https://inversores.servihabitat.com/es/venta/promociones/terreno-urbanonoconsolidado/alicante-huertasur-xabia/06124173 · 15-09-2026 (B11, B12) · 1 / 3
- [C75] Idealista 111869151 (dubbel K10, "de bancos"), zelfde URL-patroon als C56; lijst https://www.idealista.com/es/venta-terrenos/javeaxabia-alicante/con-de-bancos/ · 15-09-2026 (B12, via de officiële Idealista-assistent) · 1 / 3
- Eigen berekeningen (pin-afstanden, oppervlakteafwijkingen, consistentietoetsen 310/1.567 en 259/1.299, rekenvoorbeeld) op waarden uit B1–B10, Python in de Hermes-venv · 15-09-2026 · 5

## Herzieningen

- 15-09-2026 (samenhangscontrole): K10 in de conclusie als "waarschijnlijk" (niet "vrijwel zeker") hetzelfde object als Idealista 111869151 en Sareb-perceel A (type 4); stap 8 afgestemd op deliverable 05 §3.4 (automatisch signaal op de perceelpolygoon, geen handmatige zoneringsinvoer als hoofdroute, PostGIS geen voorwaarde); K10-vervolgstap 7 niet meer op de pin; verwijzing naar de top-3 in deliverable 01 §1.2 bij de besluiten toegevoegd.

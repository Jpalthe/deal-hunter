# R15 — Live kandidaten in Jávea/Xàbia via de Idealista-assistent en de BP-feed

> **NA TEGENSPRAAK (15-09-2026).** Dit rapport is door een tweede agent gecontroleerd; zie `R15-kandidaten-javea-live.verificatie.md`. Betrouwbaarheid volgens die controle: middel.
> Weerlegd en in de eindstukken gecorrigeerd: R15-01; R15-02; R15-05; R15-14. Gebruik voor die punten de gecorrigeerde tekst in het verificatiebestand, niet de tekst hieronder.


**Controledatum:** 14-09-2026, 23:23–23:29 CEST
**Bronnen:** officiële Idealista-assistent (MCP van Idealista; 10 zoekopdrachten + 18 detailopvragingen), lokale Background Properties-feed (`http://127.0.0.1:3100`, dienst `com.tree.properties-api`).
**Status van dit document:** eerste kandidatenlijst, géén aankoopadvies. Alle prijzen zijn **vraagprijzen van één bron op één dag**; alle stedenbouwkundige beweringen zijn **beweringen van de aanbieder (bewijstype 1)** tenzij anders vermeld. Geen enkel object is bezichtigd, geen enkele licentie is gezien.

## Samenvatting (10 regels)

1. De Idealista-assistent leverde op 14-09-2026 in Jávea: 70 casas/chalets "para reformar" (50 opgehaald), 238 urbane/urbaniseerbare percelen (50 opgehaald), 333 percelen totaal (50 opgehaald), 1.273 chalets gesorteerd op prijsdaling (50 opgehaald), 19 pisos "para reformar", 0 objecten "de bancos", 0 "edificios". Samen 164 unieke Idealista-objecten (91 chalets, 7 casas de pueblo/fincas, 66 percelen) plus 19 pisos.
2. Uit die set zijn **14 kandidaten** geselecteerd: 6 renovatieobjecten, 5 percelen, 3 bijzondere situaties (onafgebouwd, meerdere eenheden, SL-eigendom/pakket). Voorlopige indeling: 9× verder onderzoeken, 4× watchlist, 1× afwijzen. Nergens "onderhandelen" of "bieden".
3. De BP-feed was om 23:23 weer beschikbaar: 225 objecten (laatste ophaalronde 23:00 CEST), waarvan **57 in Jávea** (24 percelen, 26 villa's, 5 appartementen, 2 zonder type). Let op: de API filtert exact op `town=Javea` (zonder accent); `Jávea` geeft 0.
4. **12 van de 57 BP-Jávea-objecten** staan aantoonbaar ook op Idealista (zelfde prijs én zelfde m²), waaronder kandidaat K07 (perceel Garroferal del Montgó met licentie, BP-ref 4676JAV). BP kent daarnaast minstens 8 objecten met renovatie-/perceelsignalen die niet in de Idealista-top-50 zaten.
5. Grootste vondsten: een casa de pueblo met dubbele toegang en claim van derde bouwlaag (K01, 1.720 €/m²), een centrumpand met claim "hasta tres viviendas" (K13, 1.068 €/m²), een villa bij Granadella met een complete onafgebouwde onderverdieping (K12), en drie percelen waarvan de aanbieder een verleende licentie claimt (K07, K08, en 112319915).
6. Grootste valkuilen gezien: een prijsdaling van −43% blijkt een villa in goede staat waar het losse perceel uit de advertentie is gehaald (111064307); een −32% perceel is "dotacional" zonder woonbestemming (K11); het goedkoopste huis per m² (K05, 859 €/m²) ligt volgens de aanbieder zelf in een barranco-beschermingszone zonder uitbreidingsrecht.
7. Vraagprijzen per m² gebouwd (98 unieke casas/chalets, Idealista, één dag): mediaan 3.594 €/m², spreiding 859–11.185. Centrum en Partida Tosal liggen het laagst (mediaan 2.417 resp. 2.158), Puerto en Adsubia het hoogst (mediaan 3.505 resp. 4.302). Dit is géén marktwaarde.
8. Datakwaliteit Idealista: propertyCode is géén objectidentiteit (18 groepen dubbele advertenties; één villa onder vijf codes in drie verschillende zones), pin en zone zijn benaderend en soms fout, gestructureerde velden "situación urbanística" spreken de tekst regelmatig tegen, en een prijsverlaging kan onzichtbaar blijven (109915149: tekst 325.000, prijsveld 299.000).
9. Toolbeperkingen: maximaal 50 resultaten zonder paginering (dekking percelen 15–21%, chalets 4%); vrije tekst wordt grotendeels genegeerd (vier verschillende chalet-zoekopdrachten gaven exact dezelfde 50 objecten); een zoekopdracht met "casco antiguo" werd naar **Pamplona** gegeocodeerd — altijd `locationName`/`subtitle` op "Jávea/Xàbia" controleren.
10. Eerstvolgende stap voor élke kandidaat is dezelfde: kadastrale referentie + nota simple + planologische toets bij het Ayuntamiento de Xàbia, vóór enige waardering. Jan's investeringskader (budget, rendementseis, entiteit) is nog onbekend, dus geen enkele kandidaat kan verder komen dan "verder onderzoeken".

---

## 1. Wat is gedaan (bewijstype 3)

### 1.1 Zoekopdrachten Idealista-assistent (locale es-ES, country es, SALE, maxResults 50)

| # | Zoekopdracht | propertyType | Door de tool toegepaste filter (uit `summary`/`searchUrl`) | Totaal | Opgehaald | Opmerking |
|---|---|---|---|---|---|---|
| Q1 | chalet para reformar en Jávea | CHALET | casas y chalets, "Usada / para reformar" | 70 | 50 | basisset renovatie |
| Q2a | casa de pueblo para reformar en el casco antiguo de Jávea | HOME | — | — | — | **toolfout** ("An error occurred while searching") |
| Q2b | idem | CHALET | casas y chalets, para reformar, **locationName "Casco Antiguo, Pamplona/Iruña"** | 1 | 1 | **verkeerd gegeocodeerd**, resultaat (Pamplona) verworpen |
| Q2c | casa de pueblo para reformar en Jávea | HOME | casas y chalets, para reformar | 70 | 50 | identiek aan Q1 (zelfde 50 codes) |
| Q3 | piso para reformar en Jávea | HOME | pisos/áticos/dúplex, para reformar | 19 | 19 | volledig |
| Q4 | terreno urbano edificable en Jávea | LAND | terrenos urbanos + urbanizables | 238 | 50 | 21% dekking |
| Q5 | parcela con licencia o proyecto en Jávea | LAND | terrenos (geen extra filter) | 333 | 50 | 15% dekking; 34 codes overlappen met Q4 |
| Q6 | finca rústica con casa para reformar en Jávea | CHALET | casas y chalets + fincas, para reformar | 70 | 50 | identiek aan Q1 |
| Q7a | obra inacabada o edificio en Jávea | BUILDING | edificios | 0 | 0 | **0 edificios in Jávea** |
| Q7b | idem | CHALET | edificios (tool negeerde CHALET) | 0 | 0 | |
| Q7c | chalet en construcción sin terminar, obra inacabada, en Jávea | CHALET | casas y chalets, para reformar | 70 | 50 | identiek aan Q1; "onafgebouwd" is geen filter |
| Q8 | chalet con bajada de precio en Jávea | CHALET | casas y chalets, `ordenado-por=rebajas-desc` | 1.273 | 50 | 4% dekking; top-50 prijsdalingen |
| Q9a | de bancos en Jávea | HOME | **locales o naves**, "De bancos" | 0 | 0 | tool koos verkeerde categorie |
| Q9b | viviendas de bancos en Jávea | HOME | casas y pisos, "De bancos" | 0 | 0 | **0 bankwoningen in Jávea** |

Lijst-URL's zoals de tool ze gaf (utm-parameters ongewijzigd):
- Q1/Q2c/Q6/Q7c: https://www.idealista.com/es/venta-viviendas/javeaxabia-alicante/con-chalets,para-reformar/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_list
- Q3: https://www.idealista.com/es/venta-viviendas/javeaxabia-alicante/con-pisos,para-reformar/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_list
- Q4: https://www.idealista.com/es/venta-terrenos/javeaxabia-alicante/con-terrenos-urbanos,terrenos-urbanizables/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_list
- Q5: https://www.idealista.com/es/venta-terrenos/javeaxabia-alicante/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_list
- Q8: https://www.idealista.com/es/venta-viviendas/javeaxabia-alicante/con-chalets/?ordenado-por=rebajas-desc&utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_list
- Q9b: https://www.idealista.com/es/venta-viviendas/javeaxabia-alicante/con-de-bancos/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_list

### 1.2 Verwerking
De vijf grote resultaatsets (Q1, Q4, Q5, Q6, Q8, plus Q2c/Q7c) waren te groot voor het venster en zijn als JSON-bestand verwerkt met `jq` (alle 164 records structureel: code, prijs, prijsdaling, m², kamers, typologie, lat/long, titel, trefwoordsignalen in de beschrijving). De volledige beschrijvingen van ~45 objecten met signalen zijn gelezen; voor 18 objecten is `property_detail` opgevraagd (levert extra: bouwjaar, perceel-m², bruikbare m², oriëntatie, "situación urbanística", energielabel, makelaarsnaam + eigen referentie, `modificationDateText`, `isAuction`, `outcome: active`). Q3 (19 pisos) kwam direct terug en is handmatig verwerkt.

Trefwoorden gezocht (Spaans): inacabad, sin terminar, en construcción, estructura, licencia, proyecto, edificabilidad, ocupación, solar, derrib/demol, ruina, S.L, sociedad, varias/dos/tres viviendas, apartamentos, edificio, hotel, segregar/segregación, dividir, subasta, banco, embargo, herencia, ampliar/ampliación, obra mayor. Vals-positieven gezien: "embargo" matchte "sin embargo" (107566400); "hotel" is vaak marketingtaal; "banco" matchte "banco corrido" (zitbank).

---

## 2. De 14 kandidaten

Legenda per kandidaat: **code + URL letterlijk uit de tool**, zone (Idealista-label), vraagprijs (+ daling volgens `priceDropInfo`), m², lat/long (**pin is benaderend; adres meestal verborgen; zonelabel soms aantoonbaar fout — zie §5**), citaat, claims zonder bewijs, dealhypothese (sjabloon §4 masterprompt), voorlopige indeling (§23). Makelaarsnamen zijn bedrijfsnamen; telefoonnummers en namen van particulieren zijn bewust weggelaten.

### 2A. Renovatieobjecten

#### K01 — Casa de pueblo met dubbele toegang, Calle Teuleria (Centro Ciudad)
- **propertyCode 108910753** — https://www.idealista.com/es/inmueble/108910753/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail
- Zelfde object lijkt ook onder **109038046** ("Casa de pueblo en Calle Teuleria", 399.000, 232 m²) en **108922636** ("Piso en Calle Teuleria s/n", 399.000, 232 m²; tekst noemt "licencia de obra mayor") te staan — zelfde prijs/m²/kamers, andere aanbieders [te verifiëren, bewijstype 4].
- Zone: Centro Ciudad (casco antiguo). Vraagprijs **399.000 €**, geen daling gemeld. 232 m² gebouwd (230 bruikbaar), perceel 161 m², 5 kamers, 2 baden, 2 verdiepingen, oriëntatie Z/O, energielabel F/E. Pin ±38,7898 / 0,1589. Aanbieder: MORAGUESPONS Mediterranean Houses (ref. V-1488). "Anuncio actualizado hace más de un mes".
- Citaat: "No es una casa para entrar a vivir. Es una casa para transformarla…"
- Claims zonder bewijs: "dos accesos independientes" → "dos viviendas totalmente independientes"; "patio interior… viable integrar una pequeña piscina"; "posibilidad de desarrollar una tercera planta, previa licencia". Bouwjaar niet vermeld.
- Dealhypothese: Dit object kan interessant zijn omdat het op 1.720 €/m² ligt tegen een centrum-mediaan van 2.417 €/m² (vraagprijzen) en zich volgens de tekst laat splitsen in twee eenheden, mits wordt bevestigd dat splitsing en een derde bouwlaag planologisch zijn toegestaan in de casco-antiguo-ordenanza en de constructie de opbouw draagt. De waarde ontstaat door integrale renovatie plus splitsing (twee verkoopbare of verhuurbare eenheden) en eventueel extra bouwlaag. De belangrijkste bedreiging is de erfgoed-/casco-regelgeving die opbouw en gevelwijziging beperkt, plus bouwlogistiek in een smalle straat. De eerstvolgende controle is de kadastrale referentie en de planologische toets (ordenanza casco antiguo, maximale hoogte, parkeereis) bij het Ayuntamiento, samen met een nota simple.
- Indeling: **verder onderzoeken** (route A of C).

#### K02 — Casa de pueblo met garage, casco antiguo (Centro Ciudad)
- **propertyCode 110974608** — https://www.idealista.com/es/inmueble/110974608/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail
- Zone: Centro Ciudad. **499.000 €**, geen daling gemeld. 264 m² gebouwd, 4 kamers, 1 bad, 2 verdiepingen, "acceso desde dos calles", garage met bovenliggend terras, energielabel G. Typologie in de tool: "flat", maar tekst: casa de pueblo (inconsistent). Pin ±38,7899 / 0,1629. Aanbieder: EURO JAVEA Real Estate (ref. EJA-1197). 1.890 €/m².
- Citaat: "ideal para quienes buscan un proyecto de reforma con carácter y gran potencial."
- Claims zonder bewijs: garage "con acceso directo" (in het casco zeldzaam; legaliteit van de garage-inrit niet aangetoond); geen perceel-m², geen bouwjaar.
- Dealhypothese: Dit object kan interessant zijn omdat een casa de pueblo met eigen garage en twee straattoegangen in het centrum een schaars eindproduct oplevert, mits de garage legaal is en de bouwkundige staat (1 badkamer, label G, "elementos originales") geen verborgen structurele kosten verbergt. De waarde ontstaat door een integrale, karaktervolle renovatie voor de eindgebruikersmarkt (of als opdracht voor Build/Live). De belangrijkste bedreiging is dat 499.000 € plus renovatie boven de aantoonbare eindwaarde in het centrum uitkomt — er is geen transactiereferentie. De eerstvolgende controle is kadaster + nota simple (garage als onderdeel van dezelfde finca?) en een bezichtiging met bouwkundige.
- Indeling: **verder onderzoeken** (route A/C), lagere prioriteit dan K01.

#### K03 — Klein huis op groot Montgó-perceel, Calle del Montgó (Montgó–Ermita)
- **propertyCode 110273579** — https://www.idealista.com/es/inmueble/110273579/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail
- Zone: Montgó–Ermita. **565.000 €**, was 595.000 (**−5%**). 120 m² gebouwd op **1.050 m²** perceel, 2 kamers (oorspronkelijk 3), 2 baden, garage, oriëntatie zuid, energielabel F (70 kWh/m²·jr). Pin ±38,7934 / 0,1269. Aanbieder: InmovillasJávea (ref. JV1071). Advertentie bijgewerkt 13 dagen geleden. 4.708 €/m² — hoog, omdat het huis klein is; de prijs zit in het perceel.
- Citaat: "edificabilidad no agotada del 20%".
- Claims zonder bewijs: wat "20%" betekent (20% van het perceel als totaal, of 20% resterend) is niet te herleiden; bouwjaar ontbreekt.
- Dealhypothese: Dit object kan interessant zijn omdat een klein, verouderd huis op een groot zuidgericht Montgó-perceel zich leent voor uitbreiding tot een volwaardige villa, mits het werkelijke resterende bouwvolume (coëfficiënt, bezettingsgraad, hoogte) via een certificado urbanístico wordt bevestigd. De waarde ontstaat door uitbreiding + renovatie (route A) of sloop/nieuwbouw als het volume dat toelaat. De belangrijkste bedreiging is dat men de perceelprijs betaalt terwijl het bestaande gebouw weinig waarde toevoegt en de uitbreiding beperkter blijkt dan geadverteerd. De eerstvolgende controle is kadastrale referentie + certificado urbanístico bij het Ayuntamiento.
- Indeling: **verder onderzoeken** (route A/B).

#### K04 — Chalet uit 1974 op 2.895 m², Carretera de Jesús Pobre (Partida Tosal)
- **propertyCode 112342245** — https://www.idealista.com/es/inmueble/112342245/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail (dubbel onder **108002564**, zelfde prijs/m²/kamers)
- Zone: Partida Tosal – Zona dels Castellans. **520.000 €**, geen daling gemeld. 241 m² gebouwd op **2.895 m²**, bouwjaar 1974, 3 kamers, 3 baden, zwembad "necesita ser reformada", cochera + trastero/studio, energielabel G. Pin ±38,7867 / 0,1426. Aanbieder: MG Villas (ref. MGC217401). Bijgewerkt 13 dagen geleden. 2.158 €/m².
- Citaat: "La casa necesita reforma integral… dispone todavía de más edificabilidad, pudiendo ampliar… unos 300m2 más."
- Claims zonder bewijs: +300 m² uitbreidbaar; "posibilidad de combinar vivienda con negocio en la parte de delante de la parcela" (impliceert gemengde/terciaire bestemming aan de weg — niet aangetoond).
- Dealhypothese: Dit object kan interessant zijn omdat het grote perceel en de geclaimde restcapaciteit (±300 m²) ruimte geven voor een tweede woning of forse uitbreiding, mits de bestemming (residentieel vs. terciair aan de carretera) en het resterende volume bevestigd worden en de ligging aan de doorgaande weg de eindwaarde niet drukt. De waarde ontstaat door uitbreiding/nieuwbouw op eigen grond (route B) of renovatie + splitsing. De belangrijkste bedreiging is verkeersligging en een 1974-constructie waarvan de renovatie duurder uitvalt dan sloop. De eerstvolgende controle is het certificado urbanístico (zone, coëfficiënt, mogelijke segregatie) en de kadastrale geometrie (ligt het perceel deels in wegreservering?).
- Indeling: **verder onderzoeken** (route B/A).

#### K05 — 460 m² chalet met binnenzwembad, Camino dels Castellans — goedkoopste per m², maar barranco-affectie
- **propertyCode 97576395** — https://www.idealista.com/es/inmueble/97576395/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail
- Zone: Partida Tosal – Zona dels Castellans. **395.000 €**, geen daling gemeld. 460 m² gebouwd op 980 m² (gestructureerd veld: 960 m²), 6 kamers, 5 baden, 3 niveaus, binnenzwembad met jacuzzi en sauna, riu-rau "de 11 ojos". Pin ±38,7906 / 0,1550. Aanbieder: LYT Properties (ref. LTV573-44). Bijgewerkt >2 maanden geleden. **859 €/m²** — laagste van de hele set.
- Citaat (aanbieder zelf): "de manera legal no es posible su ampliación o la construcción de una piscina por encontrarse en un área protegida por afección del cauce del barranco".
- Claims zonder bewijs: dat het bestaande volume wél legaal/geconsolideerd is; energielabel "A" in de tool (onwaarschijnlijk voor een renovatieobject — mogelijk invoerfout).
- Dealhypothese: Dit object kan interessant zijn omdat de prijs per m² ver onder alles in Jávea ligt en het volume (460 m²) al bestaat, mits wordt bevestigd dat het bestaande gebouw legaal is, verzekerbaar/financierbaar blijft en dat de barranco-affectie zich beperkt tot "geen uitbreiding" en niet tot "fuera de ordenación" of overstromingsrisico voor de lage verdieping. De waarde ontstaat door renovatie binnen het bestaande volume (geen vergunningtraject voor uitbreiding nodig). De belangrijkste bedreiging is een harde blokkade: bouwverbod op het perceel, overstromingsrisico of onverzekerbaarheid. De eerstvolgende controle is de ligging ten opzichte van het barranco (gemeentelijke kaart, overstromingsrisicokaarten van de regio en het waterschapsbeheer — instantie [te verifiëren]) en de legaliteitsstatus van het gebouw in kadaster/registro.
- Indeling: **watchlist** tot de barranco-toets is gedaan; bij "alleen geen uitbreiding" → verder onderzoeken; bij fuera de ordenación/overstromingszone → afwijzen.

#### K06 — Casco piso in het Puerto (Aduanas), particuliere verkoper, lang te koop
- **propertyCode 106514871** — https://www.idealista.com/es/inmueble/106514871/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail
- Zone: Puerto (Calle Virgen del Loreto; adres getoond). **345.000 €**, geen daling gemeld. 125 m² gebouwd (120 bruikbaar) + 15 m² terras, 1e verdieping met lift, trastero op het dak, 60 m van het strand. Energieverbruik 382,6 kWh/m²·jr (G). Pin ±38,7930 / 0,1812. **Particuliere aanbieder** (naam bewust niet overgenomen). "Anuncio actualizado hace más de 7 meses" — langste marketingduur van de set. 2.760 €/m².
- Citaat: "el piso está diáfano y cuenta con un baño, ofreciendo una base perfecta para una reforma integral".
- Claims zonder bewijs: "plano de una propuesta de distribución" (indelingsvoorstel, geen vergunning); of het casco ooit legaal is gestript (licencia de obra voor de eerdere sloopwerkzaamheden?).
- Dealhypothese: Dit object kan interessant zijn omdat een casco op 60 m van het strand een korte renovatie zonder sloopfase toelaat en een particuliere verkoper na 7+ maanden mogelijk beweegruimte heeft, mits de comunidad-situatie (statuten, achterstallige bijdragen, geplande gevel-/liftwerken) en de legaliteit van de casco-toestand bevestigd worden. De waarde ontstaat door een gerichte renovatie (keuken, twee badkamers, indeling) tot een verhuurbaar of verkoopbaar Puerto-appartement. De belangrijkste bedreiging is dat 2.760 €/m² casco + renovatie in de buurt komt van de vraagprijzen van gerenoveerde Puerto-appartementen (in Q3 tot 6.556 €/m² voor kleine gerenoveerde units, maar geen transactiebewijs). De eerstvolgende controle is nota simple + certificaat van de comunidad + kadastrale m².
- Indeling: **verder onderzoeken** (route A of C: renovatieopdracht).

Ook gezien in Q3 maar niet geselecteerd: 110753699 (Puerto, 137 m² diáfano, 340.000, 2.482 €/m² — vergelijkbaar met K06, zelfde straatkwadrant), 110511861 (Puerto, "Vivienda para terminar reforma", 365.000, 95 m² — half afgemaakte renovatie, bijzondere situatie op kleine schaal), 112333304 (Arenal-studio "en su estado de origen", 128.000, 35 m²), 111207667 (Arenal eerste lijn, "requiere reforma", 345.000, 79 m²), 111662708 (Arenal eerste lijn, "requiere de una actualización", 470.000, 96 m², parkeerplaats).

### 2B. Percelen

#### K07 — Perceel met verleende licentie en 70% betaald project, Garroferal del Montgó (Montgó–Ermita) — óók in de BP-feed
- **propertyCode 112280961** — https://www.idealista.com/es/inmueble/112280961/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail
- Dubbels op Idealista: **112256480** (505.000, Calle Pic de Rebalsadors), **112386422** (505.000), waarschijnlijk **112283303** (500.000, Calle Pic de Rebalsadors 30, 1.571 m²). **BP-feed ref. 4676JAV** (505.000, 1.570 m², Montgó-Ermita, zelfde inhoud; BP-URL: https://backgroundproperties.com/en/property/4676jav-spacious-plot-with-building-permit-for-sale-on-the-montgo-javea/).
- Zone: Montgó–Ermita. **505.000 €**, geen daling gemeld. **1.570 m²**, zuid. Pin ±38,7936 / 0,1214. Aanbieder Idealista: Atina Inmobiliaria (ref. T-3481A). 322 €/m² perceel.
- Citaat: "En el precio de venta se incluye la licencia de obras del Ayuntamiento, las tasas, el aval bancario de la urbanización y el 70 % del proyecto."
- Claims zonder bewijs: licentie verleend én betaald; geldigheidsduur/uitvoeringstermijn van de licentie; overdraagbaarheid van licentie en projectrechten (architect); projectvilla 310 m², 4 suites + zwembad (BP-tekst); "urbanización nueva" — terwijl het gestructureerde Idealista-veld "Terreno urbanizable / Calificado para otra" zegt (tegenstrijdig).
- Dealhypothese: Dit perceel kan interessant zijn omdat een verleende licentie maanden tot jaren vergunningstraject scheelt en de aanbetaalde projectkosten in de prijs zitten, mits licentienummer, datum, resterende uitvoeringstermijn en de overdraagbaarheid worden bevestigd en het ontwerp bruikbaar is (herontwerp = nieuwe licentie). De waarde ontstaat door direct bouwen (route B) of doorverkoop als bouwklaar pakket (route D). De belangrijkste bedreiging is een verlopen of verlopende licentie en een project dat niet bij de markt past. De eerstvolgende controle is een kopie van de licentie + het project + certificado urbanístico, en de kadastrale referentie.
- Indeling: **verder onderzoeken** (route B). Opmerking: dit object loopt via onze bestaande BP-relatie; benadering pas na akkoord van Jan.

#### K08 — Perceel met "licencia vigente", eigendom van een SL, Calle Mar Amarillo (El Rafalet)
- **propertyCode 90705084** — https://www.idealista.com/es/inmueble/90705084/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail
- Mogelijk hetzelfde perceel als **BP-ref. 4104JAV** (150.000, 1.100 m², Rafalet, doodlopende straat, "up to 2 floors") — prijs gelijk, m² wijkt 20 m² af, BP-tekst noemt geen licentie of SL [te verifiëren].
- Zone: El Rafalet (adres getoond: Calle Mar Amarillo 300). **150.000 €**, geen daling gemeld. 1.120 m² (tekst: "1000 m2"), hellend, uitzicht Montgó. Pin ±38,7621 / 0,1544. Aanbieder: Grupo García (ref. NC201823). Bijgewerkt 10 dagen geleden. 134 €/m² — onderkant van Rafalet (137–240 €/m² in deze set).
- Citaat: "parcela urbana… con licencia de construcción vigente… la parcela pertenece actualmente a una sociedad limitada española (SL)".
- Claims zonder bewijs: licentie geldig (nummer/datum ontbreken); "planos de la villa aprobados"; hoofdfoto is volgens de aanbieder zelf AI-gegenereerd; gestructureerd veld zegt "Terreno urbanizable / Calificado para otra" (tegenstrijdig met "parcela urbana").
- Dealhypothese: Dit perceel kan interessant zijn omdat de vraagprijs aan de onderkant van de zone ligt en een geldige licentie wordt geclaimd, mits de licentie (nummer, datum, termijn) wordt aangetoond en de SL-structuur wordt doorgelicht (asset deal vs. share deal; schulden en verplichtingen van de vennootschap). De waarde ontstaat door bouwklaar instappen tegen lage grondprijs (route B), eventueel met fiscale/structurele aspecten van een aandelenoverdracht die Jan met zijn adviseur moet beoordelen. De belangrijkste bedreiging is de helling (fundering- en keerwandkosten) en verborgen verplichtingen in de SL. De eerstvolgende controle is nota simple (op naam van de SL), de licentie zelf en het Registro Mercantil-uittreksel van de SL.
- Indeling: **verder onderzoeken** (route B; bijzondere situatie SL-eigendom).

#### K09 — Perceel Pinosol met expliciet geclaimde bouwparameters (Pinomar–Pinosol)
- **propertyCode 109915149** — https://www.idealista.com/es/inmueble/109915149/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail
- Zone: Pinomar–Pinosol (Urb. Pino Sol). **299.000 €** in het prijsveld; **de tekst zegt nog "325.000 €"** — een prijsverlaging die niet als `priceDropInfo` verschijnt (bewijstype 3). 1.299 m², zuid, water/elektra vermeld. Pin ±38,7563 / 0,1856. Aanbieder: Orange Villas (ref. OV4419; noemt eigen "constructora/promotora"). Bijgewerkt >3 maanden geleden. 230 €/m².
- Citaat: "Suelo Urbano – Residencial Extensivo (Zona E, grado II)… Edificabilidad 0,20 m²/m² (aprox. 259 m² construibles)… Ocupación máxima del 30%… PB + 1 planta… Parcela mínima 1.000 m²".
- Claims zonder bewijs: alle bovenstaande parameters; het gestructureerde veld zegt "Terreno urbanizable" (tegenstrijdig met "suelo urbano"). Opvallend: in dezelfde zone biedt 111340209 (Engel & Völkers) een perceel van **700 m²** aan als bebouwbaar met 210 m² — dat botst met de hier geclaimde minimale perceelgrootte van 1.000 m². Minstens één van beide advertenties klopt niet, of de zones verschillen.
- Dealhypothese: Dit perceel kan interessant zijn omdat de aanbieder concrete parameters noemt die snel te toetsen zijn en de prijs stilzwijgend is verlaagd, mits het certificado urbanístico de Zona E-grado II-parameters bevestigt en er geen bouwverplichting met de constructora van de makelaar aan vastzit. De waarde ontstaat door een villa van ±259 m² (route B) of door verkoop als bouwpakket (route D). De belangrijkste bedreiging is een gebonden bouwer of andere parameters dan geadverteerd. De eerstvolgende controle is de kadastrale referentie + certificado urbanístico; daarna de vergelijking met 111340209.
- Indeling: **verder onderzoeken** (route B).

#### K10 — 16 urbaniseerbare percelen als pakket, Balcón al Mar / "Ciudad La Guardia"
- **propertyCode 107655781** — https://www.idealista.com/es/inmueble/107655781/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail (dubbel: **111869151**, Calle Sergei Rachmaninov 4, zelfde cijfers)
- Zone: Portichol – Balcón al Mar (adres getoond: Calle Sergei Rachmaninov 8). **725.000 €**, was 904.000 (**−20%**). **17.775 m²** totaal; gestructureerd: "Superficie edificable 3.554 m²", "Terreno urbanizable", "residencial unifamiliar (chalets)", "2 plantas". Pin ±38,7411 / 0,2175. Aanbieder: Leukante Realty S.L. (Calpe; ref. SH0697). Bijgewerkt 4 dagen geleden. 41 €/m² — laagste perceelprijs van de set.
- Citaat: "Se venden 16 suelos urbanizables… plan de reparcelación Ciudad La Guardia… Edificabilidad máxima tras las gestiones y transformaciones pertinentes de 3.554 m2… Porcentaje de participación en el ámbito de 26,85 %."
- Claims zonder bewijs: dat de reparcelación doorgang vindt en wanneer; de urbanisatiekosten die bij 26,85% participatie horen; dat er 16 zelfstandige percelen van 1.000–1.422 m² uit komen.
- Dealhypothese: Dit pakket kan interessant zijn omdat de nominale grondprijs per toekomstig perceel (±45.000 €) ver onder de vraagprijzen voor bouwrijpe kavels in Balcón al Mar ligt (in deze set 272–828 €/m²), mits de status van het reparcelatieplan, de urbanisatiekosten, de doorlooptijd en eventuele stilstand/juridische geschillen worden bevestigd. De waarde ontstaat door grondontwikkeling: van "urbanizable" naar "solar" (route B, lange horizon, kapitaalintensief). De belangrijkste bedreiging is jarenlange vertraging of een programma dat nooit wordt uitgevoerd — "urbanizable" is geen bouwrecht. De eerstvolgende controle is de stand van het Programa/Proyecto de Reparcelación "Ciudad La Guardia" bij Urbanismo van het Ayuntamiento de Xàbia en de kadastrale referenties van alle 16 stukken.
- Indeling: **watchlist** (bijzondere situatie: pakket + pending reparcelación; past alleen bij een expliciet ontwikkelmandaat van Jan).

#### K11 — Perceel met −32% aan de Carretera de la Guardia — géén woonbestemming
- **propertyCode 111856637** — https://www.idealista.com/es/inmueble/111856637/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail
- Zone: El Tosalet – Cap Martí (adres getoond: Carretera de la Guardia s/n). **229.000 €**, was 336.000 (**−32%**). 2.867 m²; gestructureerd: "Terreno urbano (solar)", "terciario comercial", "edificable 299 m²". Pin ±38,7478 / 0,2061. Aanbieder: Pluricasa (Torremolinos). Bijgewerkt 11 uur geleden. 80 €/m².
- Citaat (aanbieder): "La Calificación urbanística de la parcela es Dotacional… No se permite el uso residencial en la parcela."
- Claims zonder bewijs: de toegestane gebruiken (docente, deportivo, socio-cultural, sanitario-asistencial, servicios públicos, administrativos, aparcamientos) en 299 m² bebouwbaar.
- Dealhypothese: Dit perceel is voor de routes A en B niet interessant omdat woningbouw volgens de aanbieder zelf is uitgesloten; het zou alleen interessant kunnen zijn als TREE een dotacional gebruik (sport, zorg, onderwijs, parkeren) zou willen exploiteren, mits dat gebruik en het bouwvolume worden bevestigd. De waarde zou dan ontstaan uit exploitatie, niet uit wederverkoop van woningen. De belangrijkste bedreiging is illiquiditeit: de prijsdaling illustreert dat de markt voor deze bestemming dun is. De eerstvolgende controle is er geen — tenzij Jan een dotacional concept heeft.
- Indeling: **afwijzen** voor het acquisitiekader; als les vastleggen ("prijsdaling ≠ kans"). Vergelijkbaar: BP-ref. 4649JAV (Mar Azul, 3.737 m², "Suelo Dotacional Privado", 530.000 €, 0,20 m²/m² → ±747 m², 2 lagen, 30% bezetting — alles claims van BP).

Ook gezien (percelen, niet geselecteerd, wel volgen): **112319915** Calle Adelfa, El Tosalet, 1.094 m², 340.000, "LICENCIA DE OBRA APROBADA, LISTO PARA CONSTRUIR" (claim; verder onderzoeken als K07/K08 tegenvallen); **106584455** Cuesta de San Antonio, Puerto, 1.000 m², 1.500.000, "licencia de construcción en trámite" (in aanvraag, dus niet verleend); **110699106** Avenida dels Furs, Puerto, 1.190 m² "solar comercial", 1.750.000, "licencia de obra concedida (LOM-2020/51)" voor een commercieel gebouw — een licentienummer uit 2020: geldigheid [te verifiëren]; **110085566/109162787** Avenida dels Furs, Puerto, 1.150 m², 2.850.000, "3.450 m2 edificables… PB + dos alturas + ático" (woongebouw, route B op grotere schaal — watchlist); **112384437** El Arenal, 2.669 m², 3.100.000, "alta edificabilidad" zonder cijfers; **111340209** Pinosol 700 m², 149.000 (zie K09; water/elektra "kunnen worden aangesloten vanaf het buurperceel" = niet aangesloten); **111040889** Costa Nova 999 m², 168.000 (−11%), tekst zonder enige bouwparameter.

### 2C. Bijzondere situaties

#### K12 — Villa bij Cala Granadella met complete onafgebouwde onderverdieping
- **propertyCode 111364793** — https://www.idealista.com/es/inmueble/111364793/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail
- Zone: La Granadella – Costa Nova. **795.000 €**, geen daling gemeld. Tool: 256 m² gebouwd; **tekst: "500 m² construidos, distribuidos en dos plantas"** (tegenstrijdig — vermoedelijk 256 m² afgebouwd + ±250 m² casco). Perceel **2.192 m²**, bouwjaar 1979, 6 kamers, 2 baden, geen verwarming, energielabel G, label "Vistas al mar". Pin ±38,7312 / 0,1935. Aanbieder: Engel & Völkers València (ref. W-048TXS). 3.105 €/m² (op 256 m²).
- Citaat: "En la planta inferior encontramos una construcción sin terminar, de las mismas dimensiones que la vivienda principal".
- Claims zonder bewijs: dat de onderverdieping legaal (vergund, binnen het bouwvolume) is; "2 minutos caminando de la cala"; mogelijkheid tot "apartamentos independientes".
- Dealhypothese: Dit object kan interessant zijn omdat het afbouwen van een bestaande casco-verdieping het bruikbare oppervlak bijna kan verdubbelen op een zeldzame locatie bij Granadella, mits het casco vergund is, binnen het toegestane volume valt en de locatie niet onder beschermd-landschapsregels valt die afbouw of gebruikswijziging blokkeren. De waarde ontstaat door afbouw + integrale renovatie tot één grote villa of hoofdhuis + gastenappartementen (route A). De belangrijkste bedreiging is een illegaal of "fuera de ordenación" casco en beperkingen door de natuurbescherming rond Granadella [precieze status te verifiëren]. De eerstvolgende controle is de kadastrale registratie (welke m² staan geregistreerd?), de vergunningshistorie bij het Ayuntamiento en de planologische zone.
- Indeling: **verder onderzoeken** (route A).

#### K13 — Centrumpand uit 1968, "hasta tres viviendas" + ruïne, met zeezicht
- **propertyCode 111439256** — https://www.idealista.com/es/inmueble/111439256/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail
- Zone: Centro Ciudad. **520.000 €**, geen daling gemeld. 487 m² gebouwd, 3 verdiepingen, bouwjaar 1968, 6 kamers, 4 baden, geen verwarming, label G, "Vistas al mar". Pin ±38,7921 / 0,1658. Aanbieder: Engel & Völkers València (ref. W-049N5K). **1.068 €/m²** — op één na laagste van de set. Renders bijgevoegd ("renders orientativos").
- Citaat: "posibilidad de configurar hasta tres viviendas independientes, además de una construcción adicional actualmente en estado de ruina… previa consulta y verificación con el Ayuntamiento".
- Claims zonder bewijs: drie eenheden toegestaan; de ruïne mag worden herbestemd (woning/parkeren/bergingen); "balcones con vistas al mar".
- Dealhypothese: Dit object kan interessant zijn omdat 487 m² in het centrum tegen 1.068 €/m² ruimte laat voor een splitsing in drie verkoopbare eenheden, mits de ordenanza splitsing toestaat (minimale woninggrootte, parkeernorm, división horizontal) en de constructie uit 1968 en de ruïne bouwkundig en juridisch houdbaar zijn. De waarde ontstaat door herontwikkeling naar meerdere eenheden (route A/B, strategie 3 "integrale renovatie of herontwikkeling"). De belangrijkste bedreiging is de parkeereis en een structurele renovatie die op sloop/nieuwbouw uitloopt. De eerstvolgende controle is kadaster + ordenanza-toets; daarna een constructeur.
- Indeling: **verder onderzoeken** (route A/B).

#### K14 — Centrumpand met de stoutste claim: "salen 12 viviendas", Calle Mare de Déu dels Àngels
- **propertyCode 108456665** — https://www.idealista.com/es/inmueble/108456665/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail
- Zone: Centro Ciudad. **650.000 €**, geen daling gemeld. 434 m² gebouwd, perceel 310 m², 8 kamers. Pin ±38,7899 / 0,1638. 1.498 €/m². (Detail niet opgevraagd; gegevens uit de zoekresultaten.)
- Citaat: "el edificio esta en ordenanza A CASCO. No tiene necesidad de reserva de aparcamiento y pueden construirse 4 alturas. Bajo +3 y bajocubierta… como la unidad mínima es de 100 metros cuadrados por vivienda salen 12 viviendas."
- Claims zonder bewijs: álles hierboven — ordenanza A, geen parkeerreservering, 4 bouwlagen + bajocubierta, minimale eenheid 100 m², 12 woningen. Dit zijn precies de getallen die de masterprompt verbiedt over te nemen zonder gemeentelijke bevestiging.
- Dealhypothese: Dit object kan interessant zijn omdat, áls de geclaimde ordenanza klopt, een sloop/nieuwbouw of herontwikkeling tot meerdere eenheden mogelijk is zonder parkeereis, mits die ordenanza-parameters letterlijk bij het Ayuntamiento worden bevestigd en erfgoedregels in het casco de sloop/opbouw niet blokkeren. De waarde ontstaat door verdichting (route B). De belangrijkste bedreiging is dat de claim onjuist of verouderd is — dan resteert een gewone renovatie op 650.000 €. De eerstvolgende controle is het certificado urbanístico met de exacte ordenanza-tekst voor dit perceel.
- Indeling: **watchlist** tot de ordenanza-claim is getoetst (die toets is goedkoop en snel; bij bevestiging → verder onderzoeken met hoge prioriteit).

Ook gezien (bijzondere situaties, niet geselecteerd): **110616065** casa de pueblo aan de Calle Mayor, 1930, 497.000 (−16%), 310 m² (tekst: 268 m²), "sin baño", local comercial beneden, "hasta 16 habitaciones" / "hotel boutique" (claim; L'Aurora Villas Selection) — watchlist voor een hotel-/apartementenconcept; **110592275** twee aaneengesloten 19e-eeuwse casas de pueblo onder één registro, 470+ m², bar-restaurant in bedrijf, 1.195.000 — hotel-boutique-claim; **111771387/108749746** villa Balcón al Mar op twee zelfstandige percelen (830 + 870 m²), 749.000 (−6%), "buen estado" — geen renovatie, wel een segregatie-/tweede-woning-scenario; de tekst bevat marktclaims ("aumentos futuros de valor del 15-25%") zonder bron en meldt dat de gevel op de foto's "con IA" is witgemaakt; **111064307** villa El Rafalet, 850.000 (was 1.495.000, **−43%**), maar "completamente reformada en 2024", "buen estado", en de tekst biedt het tegenoverliggende perceel mét licentie apart aan — de daling is vrijwel zeker een herdefinitie van het aanbod (villa zonder perceel), geen noodverkoop (bewijstype 4); **BP 4432JAV** = Idealista 106204351/108329572/110782663 (990.000, −18%): villa op 4.008 m² "currently still in a rural zone" met "a project has been proposed to include the property in a new urbanisation… 9 building plots" — een toekomstig plan is geen bouwrecht (§14–17 masterprompt); **BP 4628JAV** = 110837390/110839669 (725.000): finca 200 m² op 2.210 m² rústico + drie aangrenzende rustieke percelen (2.541 + 639 + 1.963 m²), zonder water en elektra — renovatie op rustieke grond volgt andere regels (alleen bestaand volume) [te verifiëren]; **BP 4544JAV** = 110436215 (850.000): 2.600 m² met huis, "possibility of division into two building plots" bij het Arenal; **BP C3XY4395JAV** (375.000): villa Tarraula, jarenlang restaurant "with business licence" — conversie horeca↔wonen.

### 2D. Overzichtstabel kandidaten

| ID | Code | Type | Zone (Idealista) | Vraagprijs | Daling | m² geb. / perceel | €/m² | Signaal | Indeling |
|---|---|---|---|---|---|---|---|---|---|
| K01 | 108910753 | casa de pueblo | Centro Ciudad | 399.000 | — | 232 / 161 | 1.720 | 2 toegangen, 3e laag "previa licencia" | verder onderzoeken |
| K02 | 110974608 | casa de pueblo | Centro Ciudad | 499.000 | — | 264 / ? | 1.890 | garage, 2 straten, label G | verder onderzoeken |
| K03 | 110273579 | chalet | Montgó–Ermita | 565.000 | −5% | 120 / 1.050 | 4.708 | "edificabilidad no agotada 20%" | verder onderzoeken |
| K04 | 112342245 | chalet 1974 | Partida Tosal | 520.000 | — | 241 / 2.895 | 2.158 | "reforma integral", +300 m² claim | verder onderzoeken |
| K05 | 97576395 | chalet | Partida Tosal | 395.000 | — | 460 / 980 | 859 | barranco-affectie, geen uitbreiding | watchlist |
| K06 | 106514871 | piso casco | Puerto | 345.000 | — | 125 / — | 2.760 | diáfano, particulier, >7 mnd | verder onderzoeken |
| K07 | 112280961 | perceel | Montgó–Ermita | 505.000 | — | — / 1.570 | 322 | licentie + 70% project (= BP 4676JAV) | verder onderzoeken |
| K08 | 90705084 | perceel | El Rafalet | 150.000 | — | — / 1.120 | 134 | "licencia vigente", SL-eigendom | verder onderzoeken |
| K09 | 109915149 | perceel | Pinomar–Pinosol | 299.000 | verborgen (tekst 325.000) | — / 1.299 | 230 | parameters 0,20 / 30% / PB+1 | verder onderzoeken |
| K10 | 107655781 | 16 percelen | Balcón al Mar | 725.000 | −20% | — / 17.775 | 41 | reparcelación "Ciudad La Guardia" | watchlist |
| K11 | 111856637 | perceel dotacional | El Tosalet | 229.000 | −32% | — / 2.867 | 80 | geen woonbestemming | afwijzen |
| K12 | 111364793 | villa 1979 | La Granadella | 795.000 | — | 256 (tekst 500) / 2.192 | 3.105 | onderverdieping "sin terminar" | verder onderzoeken |
| K13 | 111439256 | pand 1968 | Centro Ciudad | 520.000 | — | 487 / ? | 1.068 | "hasta tres viviendas" + ruïne | verder onderzoeken |
| K14 | 108456665 | pand | Centro Ciudad | 650.000 | — | 434 / 310 | 1.498 | "salen 12 viviendas" (claim) | watchlist |

Telling: renovatie 6 (K01–K06), percelen 5 (K07–K11), bijzonder 3 (K12–K14). Indeling: 9× verder onderzoeken, 4× watchlist, 1× afwijzen.

---

## 3. Vraagprijs per m² per zone — Idealista, 14-09-2026, één bron, één dag, géén marktwaarde

**Waarschuwing:** dit zijn vraagprijzen uit een onvolledige steekproef (top-50 per zoekopdracht), inclusief dubbele advertenties die op code zijn ontdubbeld maar niet op object. Zonelabels komen van Idealista en zijn aantoonbaar niet altijd juist (§5). Geen enkele transactieprijs is bekend. Bewijstype 5 (berekening op benoemde aannames).

### 3.1 Casas/chalets/fincas (98 unieke objecten met m² > 0, uit Q1/Q6/Q8)

| Zone (Idealista) | n | min €/m² | mediaan €/m² | max €/m² | gemiddelde |
|---|---|---|---|---|---|
| Centro Ciudad | 17 | 1.068 | 2.417 | 3.680 | 2.403 |
| Portichol – Balcón al Mar | 15 | 2.291 | 3.750 | 6.633 | 3.989 |
| El Tosalet – Cap Martí | 13 | 2.298 | 3.675 | 5.282 | 3.709 |
| Adsubia | 10 | 2.628 | 4.302 | 9.106 | 4.580 |
| La Lluca – La Tarraula | 7 | 2.944 | 3.617 | 8.759 | 4.378 |
| Partida Tosal – Zona dels Castellans | 7 | 859 | 2.158 | 3.675 | 2.213 |
| La Granadella – Costa Nova | 5 | 1.693 | 3.464 | 4.624 | 3.385 |
| Pinomar – Pinosol | 5 | 2.991 | 3.625 | 5.217 | 3.791 |
| Puerto | 5 | 2.702 | 3.505 | 11.185 | 5.201 |
| Montgó – Ermita | 4 | 2.010 | 3.648 | 4.708 | 3.504 |
| Monte Olimpo | 3 | 3.680 | 4.142 | 5.438 | 4.420 |
| Barrio Piver | 2 | 2.664 | 3.905 | 3.905 | 3.285 |
| El Rafalet | 2 | 2.866 | 3.148 | 3.148 | 3.007 |
| Sol de Este – Puerta Fenicia | 2 | 3.680 | 3.967 | 3.967 | 3.824 |
| Montañar | 1 | 3.119 | 3.119 | 3.119 | 3.119 |
| **Totaal** | **98** | **859** | **3.594** | **11.185** | **3.605** |

Lezing: Centro Ciudad en Partida Tosal zijn de enige zones waar de mediaan onder 2.500 €/m² ligt — daar zitten dan ook 8 van de 14 kandidaten. Uitschieters naar boven (Puerto 11.185, Adsubia 9.106, La Lluca 8.759) zijn luxevilla's waar de prijs in perceel en uitzicht zit, niet in gebouwde m².

### 3.2 Pisos "para reformar" (19 objecten, Q3)

| Zone | n | min | mediaan | max |
|---|---|---|---|---|
| Puerto | 7 | 2.267 | 3.242 | 6.556 |
| Centro Ciudad | 6 | 1.720 | 2.232 | 3.138 |
| Montañar | 3 | 4.896 | 6.085 | 6.238 |
| El Arenal | 3 | 3.013 | 3.657 | 4.367 |
| **Totaal** | **19** | **1.720** | **3.138** | **6.556** |

NB: het filter "para reformar" van Idealista is breed; 6 van de 19 teksten bevatten géén renovatiesignaal (o.a. 110824392 "muy buen estado", 112282029 "en proceso de reforma", 108983764 gemoderniseerd).

### 3.3 Percelen — vraagprijs per m² perceel (66 unieke percelen, Q4/Q5)

| Zone (Idealista) | n | min €/m² | mediaan €/m² | max €/m² |
|---|---|---|---|---|
| Montgó – Ermita | 11 | 90 | 317 | 477 |
| Puerto | 10 | 270 | 1.193 | 2.478 |
| Centro Ciudad | 6 | 126 | 717 | 2.250 |
| Partida Tosal – Zona dels Castellans | 6 | 129 | 200 | 771 |
| El Rafalet | 5 | 134 | 154 | 240 |
| La Granadella – Costa Nova | 5 | 168 | 200 | 372 |
| Portichol – Balcón al Mar | 5 | 41 | 272 | 828 |
| Monte Olimpo | 4 | 70 | 387 | 395 |
| Pinomar – Pinosol | 4 | 213 | 311 | 324 |
| El Tosalet – Cap Martí | 3 | 80 | 143 | 311 |
| Adsubia | 2 | 130 | 327 | 327 |
| La Lluca – La Tarraula | 2 | 117 | 204 | 204 |
| Barrio Piver / El Arenal / Sol de Este | 1 elk | 348 / 1.161 / 104 | | |
| **Totaal** | **66** | **41** | **279** | **2.478** |

Lezing: prijs per m² perceel zegt zonder bouwvolume niets — de goedkoopste (41 €/m², K10) is niet-bouwrijp "urbanizable", de duurste (2.478 €/m², Avenida dels Furs) draagt volgens de aanbieder 3.450 m² gebouw. Percelen vergelijk je pas na §14–16 van de masterprompt (identificatie + bouwmogelijkhedenoverzicht).

### 3.4 Prijsdalingen in de set (bewijstype 3)
54 van de 164 unieke Idealista-objecten hebben een `priceDropInfo`. Tien daarvan ≥ 15%: 111064307 (−43%, zie §2C: herdefinitie aanbod), 111856637 (−32%, K11, dotacional), 107655781/111869151 (−20%, K10), 106204351/108329572/110782663 (−18%, alle drie = BP 4432JAV, één villa), 106630682 (−18%, Monte Olimpo, 990.000), 111643516 (−17%, El Tosalet, 2.900.000), 110616065 (−16%, Calle Mayor). Conclusie: in deze steekproef valt elke grote daling te verklaren uit bestemming, herdefinitie of prijsniveau — geen enkele is bewijs van een gedwongen verkoop.

---

## 4. BP-feed: beschikbaarheid, Jávea-objecten, overlap

### 4.1 Beschikbaarheid (bewijstype 3)
- 23:23:16 CEST: `GET /api/health` → `{"status":"ok","properties":225,"lastFetch":"2026-09-14T21:00:08.787Z"}` (= 23:00:08 CEST). De dienst heeft dus na de mislukte ronde van 22:12 om 23:00 weer succesvol opgehaald. Om 23:28:55 ongewijzigd.
- `GET /api/properties?town=J%C3%A1vea&limit=100` → **0 objecten**. Oorzaak: `server.js` filtert `towns.includes(p.town.toLowerCase())` — exacte match, geen accentnormalisatie; de feed schrijft "Javea". `GET /api/properties?town=Javea&limit=100` → **57 objecten** (23:24:32). `/api/stats`: Javea 57; types feedbreed: Land 49, Villa 149, Apartment 18, Town house 4, Country house 1, Commercial 2, leeg 2; prijsbereik 58.500–4.500.000.
- Jávea-verdeling: Land 24, Villa 26, Apartment 5, leeg type 2. Velden zoals eerder vastgesteld (geen pool-element, geen status, geen prijshistorie; wel `date` per object).

### 4.2 BP-Jávea-objecten met renovatie- of perceelsignalen (bewijstype 1 = BP-tekst)

| BP-ref | Type | Zone (BP) | Prijs | m² geb./perceel | Signaal (BP-tekst) | Idealista-overlap |
|---|---|---|---|---|---|---|
| 4676JAV | Land | Montgó-Ermita | 505.000 | —/1.570 | "already granted and paid municipal building permit… 70% of the approved architectural project" | **K07** 112280961 (+112256480, 112386422) |
| 2032JAV | Land | Nova Xabia | 500.000 | —/1.700 | "a building license is included in the sales price" | niet in top-50 gezien |
| 4104JAV | Land | Rafalet | 150.000 | —/1.100 | cul-de-sac, "up to 2 floors may be built" | mogelijk **K08** 90705084 [te verifiëren] |
| 4603JAV | Land | Villes del Vent | 398.000 | —/1.008 | "building coefficient of 16.5%… basement of up to 200 m2… up to two floors" | 111295146 (zelfde tekst; Idealista-zone "Monte Olimpo") |
| C3XY4617JAV | Land | La Lluca | 470.000 | —/2.300 | "approximately 700 m2 can be built… two semi-detached villas of 350 m2 each" | 110436209 |
| 4544JAV | Land | Adsubia | 850.000 | 152/2.600 | "possibility of division into two building plots" | 110436215 |
| 4402JAV | Land | Tosalet 5 | 1.275.000 | —/3.000 | 3 aangrenzende kavels, alleen samen | 110436247 (Idealista-zone "Centro Ciudad" — **fout**) |
| 3498JAV | Land | Ambolo | 1.950.000 | —/2.355 | 2 kavels (1.110 + 1.245) | 111123865 |
| 4529JAV | Land | Granadella | 1.445.000 | —/3.885 | 2 kavels, los 515.000 + 930.600 | 111305549; kavel 1 = BP 4532JAV |
| 4649JAV | Land | Portichol/Mar Azul | 530.000 | —/3.737 | "Suelo Dotacional Privado", 0,20 m²/m², 2 lagen, 30% | — (vergelijk K11) |
| 3335JAV | Land | Montgo | 195.000 | —/1.500 (×2) | "still need to be urbanized… permit is available… building obligation" | — |
| 4654JAV | Land | La Cala | 302.404 | —/1.000 | "sold with a building obligation with a local constructor" | — |
| 4105JAV | Land | Cap de San Antonio | 375.000 | —/1.500 | "There is an antenna mast on the plot" | — |
| 3580JAV | Land | Montgo (Ctra Jesús Pobre) | 169.000 | —/1.500 | "commercial plot" | 100720381 / 87762573 |
| 4432JAV | Villa | Las Laderas | 990.000 | 269/4.008 | "currently still in a rural zone… project proposed… 9 building plots" | 106204351 / 108329572 / 110782663 (−18%) |
| 4628JAV | Villa | Las Laderas | 725.000 | 200/7.276 | "finca… no electricity or water… renovation project" | 110837390 / 110839669 |
| C3XY4395JAV | Villa | Tarraula | 375.000 | 157/1.227 | "had a business licence… well-established restaurant" | — |
| 4196JAV | Villa | Cap Marti | 950.000 | 314/1.400 | apart gastenverblijf + "rental licence" | — |

Vals-positieven in de BP-trefwoordscan: 4679JAV en C3XY4524JAV ("recently renovated" — gerenoveerd, niet te renoveren), 4642JAV ("rental licence"), C4XY4518JAV/4480JAV/4490JAV/3299JAV (nieuwbouw "under construction").

### 4.3 Overlap BP ↔ Idealista (bewijstype 3 voor de match, 4 voor de objectidentiteit)
Op exact gelijke prijs én gelijke m² (gebouwd of perceel) matchen **12 van de 57** BP-Jávea-objecten met Idealista-advertenties: 3498JAV, 4529JAV, 4402JAV, 4432JAV, 4544JAV, 4628JAV, 4676JAV, C3XY4617JAV, 4603JAV, 4607JAV, 4608JAV, 3580JAV. Omdat de Idealista-sets afgekapt zijn op 50, is de werkelijke overlap waarschijnlijk groter. Van de 14 kandidaten zit alleen **K07** met zekerheid in de BP-feed; **K08** mogelijk. De renovatiekandidaten K01–K06 en K12–K14 zitten **niet** in de BP-feed (BP-Jávea bevat maar 2 "Town house"-achtige objecten en 0 objecten met "para reformar"-signaal in het centrum).

---

## 5. Wat deze ronde leert over de bronnen (bewijstype 3 tenzij vermeld)

1. **Locatieresolutie is onbetrouwbaar.** "casa de pueblo para reformar en el casco antiguo de Jávea" werd opgelost naar "Casco Antiguo, Pamplona/Iruña" (`locationName`), ondanks "Jávea" in de query. Elke geautomatiseerde verwerking moet `locationName` en per object `suggestedTexts.subtitle` op "Jávea/Xàbia" controleren en anders het resultaat weggooien.
2. **Vrije tekst wordt grotendeels genegeerd.** Q1, Q2c, Q6 en Q7c gaven exact dezelfde 50 codes in dezelfde volgorde. De tool vertaalt de query naar Idealista-filters (typologie, "para reformar", "de bancos", sortering op rebajas) en negeert de rest. "Onafgebouwd", "licentie", "SL", "pakket" zijn alleen in de beschrijvingstekst te vinden.
3. **Geen paginering, max 50.** Dekking: para-reformar-chalets 50/70 (71%), pisos 19/19, urbane percelen 50/238 (21%), alle percelen 50/333 (15%), chalets op prijsdaling 50/1.273 (4%). Voor systematische dekking moet de zoekruimte worden opgeknipt (per zone, prijsband, typologie) — mits dat binnen de voorwaarden van de assistent valt (onbewezen, zie eerdere feiten).
4. **propertyCode ≠ object.** 18 groepen met identieke prijs/m²/kamers; één villa (610.000, 166 m²) onder vijf codes in drie zones (El Tosalet, Partida Tosal, Centro Ciudad); één villa (1.425.000, 380 m²) onder vijf codes; K01 onder drie codes. Deduplicatie moet op (prijs, m², kamers, tekstgelijkenis, foto-hash) — precies §11 van de masterprompt.
5. **Zone en pin zijn benaderend en soms fout.** BP 4402JAV (Tosalet 5) staat op Idealista als "Centro Ciudad"; BP 4432JAV (Las Laderas) staat als "Sol de Este", "Monte Olimpo" én "Centro Ciudad". `showAddress` is meestal false; waar true, staat er een straat + nummer (K06, K08, K10, K11, 110699106).
6. **Gestructureerde velden spreken de tekst tegen.** "Situación urbanística" zegt voor K07, K08 en K09 "Terreno urbanizable / Calificado para otra" terwijl de teksten "parcela urbana", "solar" en "licencia" claimen. Die velden zijn geen bewijs; het certificado urbanístico is dat wel.
7. **Prijsverlagingen zijn niet altijd zichtbaar** (K09: tekst 325.000, veld 299.000, geen `priceDropInfo`), en zichtbare verlagingen zijn niet altijd wat ze lijken (111064307 −43% na afsplitsen van een perceel; K11 −32% door bestemming).
8. **m²-tegenstrijdigheden** tussen veld en tekst (K12: 256 vs 500; 110616065: 310 vs 268; K05: 980 vs 960; K08: 1.120 vs 1.000).
9. **`modificationDateText`** ("hace más de 7 meses", "hace 4 días", "hace 11 horas") is de enige indicatie van marketingduur — grof, maar bruikbaar als proxy (bewijstype 1).
10. **`property_detail`** voegt toe: bouwjaar, perceel-m², bruikbare m², oriëntatie, energielabel met waarden, makelaarsnaam + eigen referentie + microsite-URL, `isAuction` (waar aanwezig false), `outcome: active`, labels (zeezicht). Het geeft géén publicatiedatum, géén prijshistorie, géén kadastrale referentie.
11. **Bankaanbod:** 0 woningen en 0 locales "de bancos" in Jávea op 14-09-2026. Bankvastgoed loopt hier niet via Idealista (zie stroom R08/R18 voor veilingen en servicers).
12. **Marketingclaims in advertenties** ("aumentos futuros de valor del 15-25%", "menos del 10% del stock", "alta rentabilidad") zijn zonder bron en mogen nergens in een dossier terugkomen.
13. **BP-API-filter** is hoofdlettergevoelig-ongevoelig maar accentgevoelig: `town=Javea` werkt, `town=Jávea` niet. Voor de eigen tooling: normaliseren of op `postcode`/`latitude` filteren.
14. **Beelden**: twee advertenties melden zelf AI-bewerkte beelden (K08 hoofdfoto "generada por IA"; 111771387 gevel "hecho blanco con IA"); K13 en K06 voegen renders/indelingsvoorstellen toe. Beeldanalyse moet die eerst herkennen (§13).

---

## 6. Wat níet is gedaan / beperkingen

- Geen enkele Idealista-pagina is via WebFetch geopend (geautomatiseerde verzoeken geven 403 en zijn in strijd met de voorwaarden — eerder vastgesteld). Alle Idealista-gegevens komen uitsluitend uit de officiële assistent.
- Geen kadastrale, registrale of gemeentelijke bron geraadpleegd in deze stroom (dat is het werk van de perceel- en juridische stromen). Alle "licentie"-, "edificabilidad"- en "ordenanza"-uitspraken hierboven zijn beweringen van aanbieders.
- Geen bezichtiging, geen foto-analyse.
- Q2a gaf een toolfout en is als Q2c herhaald; Q7 ("obra inacabada") is niet als filter beschikbaar; Q9 ("de bancos") gaf 0.
- De vier grote resultaatsets zijn structureel (jq) 100% verwerkt; de volledige beschrijvingen zijn gelezen voor de ~45 objecten met signalen en voor de 19 pisos — niet voor alle 164 objecten woord voor woord.
- Van K14 is geen `property_detail` opgevraagd (gegevens uit de lijst).

---

## 7. Open vragen

1. Valt gepland/systematisch gebruik (dagelijks, opgeknipt per zone) van de Idealista-assistent binnen de voorwaarden van die assistent? Zonder antwoord blijft dit "ALLEEN HANDMATIG / TECHNISCH ONDERZOEK NODIG".
2. Licentiestatus K07, K08, 112319915, 110699106 (LOM-2020/51 uit 2020): nummer, datum, uitvoeringstermijn, overdraagbaarheid.
3. Is de "Zona E grado II"-parameterset (K09) juist, en wat is de werkelijke minimale perceelgrootte in Pinosol (700 m²-perceel 111340209 vs. geclaimde 1.000 m²)?
4. Stand van de reparcelación "Ciudad La Guardia" (K10): goedgekeurd, in uitvoering, stilgevallen?
5. Barranco-affectie K05: welke instantie/kaart is leidend, en raakt die het bestaande gebouw?
6. Zijn K08 en BP 4104JAV hetzelfde perceel? Als ja: waarom noemt BP geen licentie?
7. Casco-antiguo-ordenanza (K01, K13, K14, 110616065): splitsing, opbouw, parkeernorm, erfgoed.
8. Legaliteit van de onafgebouwde onderverdieping K12 en de beschermingsstatus rond Granadella.
9. Jan's investeringskader (budget, rendementseis, doorlooptijd, entiteit TREE vs. Rocksure) — zonder dat kan geen kandidaat verder dan "verder onderzoeken".

---

## 8. Bronnenregister voor deze stroom (statussen §7 masterprompt)

| Bron | Type | Toegang | Status | Opmerking |
|---|---|---|---|---|
| Idealista-assistent (MCP van Idealista): `search_properties`, `property_detail` | portaal, officiële assistent | binnen Claude-sessie, interactief | GEVERIFIEERD EN ACTIEF (handmatig) / TECHNISCH ONDERZOEK NODIG (systematisch) | max 50, geen paginering, geen publicatiedatum, geen makelaarsnaam in lijst (wel in detail), locatieresolutie onbetrouwbaar; voorwaarden voor systematisch gebruik onbewezen |
| Background Properties Kyero-feed via `com.tree.properties-api` (127.0.0.1:3100) | professionele feed (eigen contract) | lokaal, alleen lezen | GEVERIFIEERD EN ACTIEF | 225 objecten, 57 Jávea; hersteld om 23:00 na DNS-storing; filter accentgevoelig; sleutels niet overgenomen |

---

## 9. Bronnenlijst (URL · controledatum · bewijstype)

Idealista-objecten (alle URL's letterlijk uit de assistent, 14-09-2026, bewijstype 1 voor inhoud / 3 voor het feit dat de advertentie actief was):
- K01 https://www.idealista.com/es/inmueble/108910753/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail
- K02 https://www.idealista.com/es/inmueble/110974608/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail
- K03 https://www.idealista.com/es/inmueble/110273579/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail
- K04 https://www.idealista.com/es/inmueble/112342245/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail
- K05 https://www.idealista.com/es/inmueble/97576395/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail
- K06 https://www.idealista.com/es/inmueble/106514871/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail
- K07 https://www.idealista.com/es/inmueble/112280961/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail
- K08 https://www.idealista.com/es/inmueble/90705084/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail
- K09 https://www.idealista.com/es/inmueble/109915149/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail
- K10 https://www.idealista.com/es/inmueble/107655781/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail
- K11 https://www.idealista.com/es/inmueble/111856637/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail
- K12 https://www.idealista.com/es/inmueble/111364793/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail
- K13 https://www.idealista.com/es/inmueble/111439256/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail
- K14 https://www.idealista.com/es/inmueble/108456665/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail
- Overige genoemde objecten (zelfde URL-patroon `https://www.idealista.com/es/inmueble/<code>/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail`): 109038046, 108922636, 108002564, 110753699, 110511861, 112333304, 111207667, 111662708, 112256480, 112386422, 112283303, 111869151, 112319915, 106584455, 110699106, 110085566, 109162787, 112384437, 111340209, 111040889, 110616065, 110592275, 111771387, 108749746, 111064307, 106204351, 108329572, 110782663, 110837390, 110839669, 110436215, 110436209, 110436247, 111123865, 111305549, 111295146, 100720381, 87762573, 107566400.
- Lijst-URL's Q1–Q9: zie §1.1 (14-09-2026, bewijstype 3).

Background Properties (via lokale feed, 14-09-2026 23:24, bewijstype 1 voor inhoud / 3 voor beschikbaarheid):
- 4676JAV https://backgroundproperties.com/en/property/4676jav-spacious-plot-with-building-permit-for-sale-on-the-montgo-javea/
- 4104JAV https://backgroundproperties.com/en/property/4104jav-plot-for-sale-in-javea/
- 2032JAV https://backgroundproperties.com/en/property/2032jav-building-plot-with-permit-and-beautiful-sea-view-for-sale-in-javea/
- 4603JAV https://backgroundproperties.com/en/property/4603jav-plot-with-sea-view-free-from-builder-for-sale-in-javea/
- C3XY4617JAV https://backgroundproperties.com/en/property/c3xy4617jav-spacious-building-plot-for-sale-in-la-lluca-javea/
- 4544JAV https://backgroundproperties.com/en/property/4541jav-plot-of-2600-m2-with-house-for-sale-within-walking-distance-of-the-sandy-beach-in-javea/
- 4402JAV https://backgroundproperties.com/en/property/4402jav-3-adjacent-building-plots-with-sea-views-for-sale-in-javea/
- 3498JAV https://backgroundproperties.com/en/property/3498jav-2-exclusive-building-plots-for-sale/
- 4529JAV https://backgroundproperties.com/en/property/4529jav-2-adjacent-plots-with-sea-views-for-sale-in-granadella-javea/
- 4649JAV https://backgroundproperties.com/en/property/4649jav-spacious-plot-for-sale-300m-from-portichol-beach/
- 3335JAV https://backgroundproperties.com/en/property/building-plot-for-sale-in-javea-2/
- 4654JAV https://backgroundproperties.com/en/property/4654jav-plots-for-sale-in-la-cala-javea/
- 4105JAV https://backgroundproperties.com/en/property/4105jav-plot-with-sea-view-for-sale-in-javea/
- 3580JAV https://backgroundproperties.com/en/property/3580jav-commercial-plot-for-sale-in-javea/
- 4432JAV https://backgroundproperties.com/en/property/4432jav-villa-on-large-plot-for-sale-in-javea/
- 4628JAV https://backgroundproperties.com/en/property/4628jav-traditional-finca-with-multiple-plots-for-sale-in-pinosol-las-laderas-javea/
- C3XY4395JAV https://backgroundproperties.com/en/property/c3xy4395jav-traditional-villa-with-business-license-on-flat-plot-for-sale-in-javea/
- 4196JAV https://backgroundproperties.com/en/property/4196jav-villa-with-separate-apartment-for-sale-in-javea/

Lokale bronnen (14-09-2026, bewijstype 3):
- `http://127.0.0.1:3100/api/health`, `/api/stats`, `/api/filters`, `/api/properties?town=Javea&limit=100` (23:23–23:29 CEST)
- `/Users/root-admin/tree-hermes/properties-api/server.js` (filterlogica `town`, regels 43–102; alleen gelezen)
- `/Users/root-admin/tree-es/deal-hunter/MASTERPROMPT.md` (secties 4, 5, 6, 7, 13, 23, 25)
- Werkbestanden (scratchpad, tijdelijk): `idealista/q*.json`, `bp-javea.json`

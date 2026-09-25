# N01 — Wat mag je bouwen per zone in Xàbia (Jávea)

**Controledatum 18-09-2026.** Machineleesbare versie: `N01-bouwregels-xabia.json` (zelfde map).
Voorganger: `R12-urbanisme-xabia-plan-en-vergunning.md` — dit stuk verfijnt dat rapport op vier punten
en herleest de sleutelpagina's van het plan opnieuw uit de bron.

---

## 1. De tabel

Eén regel per zone. Dit geldt **alleen** voor percelen die rechtstreeks onder de PGOU-zonetabel vallen.
Waarom dat een harde voorwaarde is, staat in §3.

| Zone | Edificabilidad (m²t per m² perceel) | Ocupación | Hoogte | Parcela mínima | Bron | Type |
|---|---|---|---|---|---|---|
| **E, grado I** | 0,20 neto · 0,142 bruto | 20 % | 1 bouwlaag · kroonlijst 3,5 m · totaal 6,00 m | per gebied, 500–1.500 m² (§4) | ordenanzas art. 10.5.1.3–6, full nº 146/147 | 2 |
| **E, grado II** — standaard | 0,20 neto · 0,142 bruto | 30 % | 2 bouwlagen · kroonlijst 7 m · totaal 9,50 m | per gebied, 500–1.500 m² (§4) | idem + art. 2.1.6 | 2 |
| **E, grado III** | 0,20 neto · 0,142 bruto | 50 % | 2 bouwlagen · kroonlijst 7 m · totaal 9,50 m | per gebied, 500–1.500 m² (§4) | idem | 2 |
| **E, zeven uitzonderingsgebieden** | **0,28 neto · 0,198 bruto** | als grado | als grado | Calvario 700 · Caleta-Puerto 500 · overige 1.000 | idem, "excluidas las cesiones" | 2 |
| **A — Casco** | **geen coëfficiënt**; rooilijn × bouwdiepte × bouwlagen | begane grond volledig; verdiepingen 20 m diep [OCR] | II 6,1/9,1 · III 9,0/12,0 · IV 12,0/15,0 · V 15,0/18,0 m (kroonlijst/totaal) | 700 m²; gevel nieuwe kavels ≤ 15 m | art. 10.1, Mod. I-blad full nº 131 | 2 |
| **B — Ensanche** | **geen coëfficiënt** | begane grond volledig; verdiepingen 20 m diep | volgens plano B.1 | 100 m², gevel ≥ 6 m | art. 10.2 [OCR] | 2 |
| **C — Edificación abierta** | per unidad de actuación via estudio de detalle; C3 0,80 neto, C3A 0,80 bruto | I 70 % · II–IV 50 % | volgens plano B.1 | I/II 500 m² · III/IV 1.000 m², gevel 20 m | art. 10.3, wijzigingsbladen | 2 |
| **D — Conjuntos arquitectónicos** | ONBEKEND | ONBEKEND | ONBEKEND | ONBEKEND | — | 7 |
| **F — Terciario (boulevard)** | ONBEKEND | ONBEKEND | 1 bouwlaag · 3,50 m | heel bouwblok | registerdoc. 03082-1020 | 2 |
| **G — Industrial** | ONBEKEND | ONBEKEND | ONBEKEND | ONBEKEND | — | 7 |
| **H — Comercial concentrado** | ONBEKEND | ONBEKEND | ONBEKEND | ONBEKEND | — | 7 |
| **SNU genérico I** (alles buiten El Plà en La Plana) | 0,03 volgens PGOU, max. 300 m²; **wet: bezetting ≤ 2 %** | 2 % (wet) | 2 bouwlagen · 7 m | PGOU 5.000 m²; **wet ≥ 10.000 m²** | titel VII pdf-p. 65 + TRLOTUP art. 211.1.b | 2 |
| **SNU genérico II** (La Plana) | 0,03, max. 300 m²; wet 2 % | 2 % | 2 bouwlagen · 5 m, gevel natuursteen | PGOU 5.000 m²; wet ≥ 10.000 m² | idem | 2 |
| **SNU genérico III** (El Plà) | 0,01, max. 300 m²; wet 2 % | 2 % | 2 bouwlagen · 7 m | 10.000 m², frente 40 m | idem | 2 |
| **SNUEP** (Granadella, Parque Natural del Montgó, PATIVEL) | **0** | — | — | — | titel VII; resolución 08-03-1991 | 2 |
| **SUZ met plan parcial** | uit het plan parcial zelf | idem | idem | idem | art. 2.1.3; GVA-zonelaag | 3 |
| **SUZ zonder programa** | **0** — woningbouw uitdrukkelijk verboden | — | — | niet splitsbaar | TRLOTUP art. 226.1 en 248.e | 2 |

Retranqueos, de verplichte afstanden tot de perceelgrenzen, staan in §5.

Brondocument voor alle PGOU-regels: `03082-1000 ORDENANZAS.pdf`, 240 bladzijden, uit het Registro
Autonòmic de Planejament van de Generalitat. Het is een scan zonder tekstlaag. De pagina's met de
zonetabellen heb ik als afbeelding gerenderd en met het oog gelezen, niet met tekstherkenning.
Waar dat niet kon staat **[OCR]**. Het bestand is op 15-09-2026 opgehaald, md5
`db38f0d14bd4b5953430aec35f640ffa`, drie keer onafhankelijk gedownload met dezelfde uitkomst.

---

## 2. Wat geldt nu, en wat nog niet

Dit is het punt waarop in Jávea het meeste misgaat, ook bij makelaars.

**Wat geldt:** het PGOU van 1990. Definitief goedgekeurd door de Comisión Territorial de Urbanismo
van Alicante op 31 januari 1990, gepubliceerd in het BOP van 26 februari 1990, met de restgebieden
bij besluit van de conseller van 8 maart 1991 (BOP 3 juni 1991). Daarbovenop 34 latere
modificaciones. Verder de regionale wet TRLOTUP, geconsolideerd 2 juli 2026, die op suelo no
urbanizable strenger is dan het PGOU en dus voorgaat.

**Wat niet geldt:** het Plan General Estructural, de nieuwe structuurvisie. De gemeenteraad keurde op
30 april 2019 de definitieve versie goed en stuurde die naar de Conselleria. Ruim zeven jaar later is
hij er nog niet doorheen. Ik heb op 18 september 2026 het Registro Autonòmic opnieuw uitgelezen: het
bevat voor Xàbia 34 instrumenten, en het PGE zit er niet bij (bewijstype 3). De Dirección General de
Urbanismo zou de gemeente in februari 2025 schriftelijk hebben gewaarschuwd dat vergunningen niet
mogen worden geweigerd op grond van een plan dat niet is vastgesteld — dat komt uit de pers, de brief
zelf hebben wij niet gezien (bewijstype 1, [te verifiëren]).

Voor ons rekenmodel is dat eenvoudig: **het PGE telt niet mee.** Wel als risicosignaal, want het plan
haalt ongeveer 8 miljoen m² uit de categorie urbanizable. Grond die vandaag urbanizable heet en
waarvoor nooit een programa is vastgesteld, is dus dubbel kwetsbaar — nu al geen woonbouwrecht
(TRLOTUP art. 226.1), en in het PGE waarschijnlijk gedeclassificeerd.

**De NUT.** Tussen 2021 en 2025 gold een gedeeltelijke schorsing van het PGOU met vervangende
noodregels, de Normas Urbanísticas Transitorias de Urgencia. De tekst zelf zegt (DOGV 20-09-2021,
punt Segundo): de normen gelden *"hasta la aprobación del Plan General Estructural de Jávea. En todo
caso, la suspensión finalizará una vez hayan transcurrido cuatro años desde la publicación del
Acuerdo del Consell de 5 de marzo de 2021"*. Die vier jaar liepen af rond 15 maart 2025. Of de normen
zelf daarmee ook vervielen, is een juridische vraag die niemand ons schriftelijk heeft beantwoord
(bewijstype 7).

Voor het rekenmodel is die vraag niet belangrijk, en dat is nieuw ten opzichte van R12: **ik heb de
volledige NUT-tekst doorzocht en er staat geen enkele edificabilidad- of ocupación-coëfficiënt in.**
De NUT raken de bouwhoogte in de oude kern (PB + I plus cambra in plaats van maximaal vijf
bouwlagen), de historische verkaveling, en in zona E de esthetiek en de afvalwaterzuivering. Het
bouwvolume in de urbanisaties raken ze niet.

**Modificación nº 41**, het plafond op toeristische verhuur, is op 28 mei 2026 aanvankelijk
goedgekeurd en lag 45 dagen ter inzage. Plafond 4.584 woningen voor de hele gemeente, verdeeld per
wijk. Raakt de exploitatie, niet het bouwvolume. Definitieve goedkeuring niet vastgesteld — als
exploitatie-uitgangspunt in een businesscase dus [te verifiëren].

---

## 3. De aanname van 0,20: waar klopt hij en waar niet

Het model rekent nu overal `min(0,20 × perceel; 450)` — in `dh/feasibility.py` regel 52 en 61 en in
`dh/prefilter.py` regel 121.

**De coëfficiënt zelf is goed gekozen.** Ik heb hem letterlijk teruggevonden op het originele
planblad full nº 147: *"la edificabilidad bruta se fija en 0,142 metros cuadrados techo por metro
cuadrado de parcela, siendo la edificabilidad neta de 0,2 m²t/m² de parcela"*. Voor het grootste deel
van de urbanisaties klopt 0,20 dus.

Maar de aanname staat of valt met één vraag die het model niet stelt: **valt dit perceel überhaupt
onder de PGOU-zonetabel?** Ik heb de zonelaag van de Generalitat voor Xàbia geteld (eigen telling,
18-09-2026, bewijstype 3): 356 zonevlakken, waarvan

- 178 rechtstreeks "Plan general" (50,0 %)
- 152 onder een eigen plan parcial, homologación, PRI, estudio de detalle of modificación puntual (42,7 %)
- 25 Plan general met sectorale bescherming erop, Montgó of PATIVEL (7,0 %)

Kijk je alleen naar de residentiële vlakken, dan valt bijna de helft — 129 van de 266 — onder een
eigen plan met eigen getallen. Het perceel bij Villes del Vent waar de advertentie 16,5 % noemt, is
daar een voorbeeld van: dat ligt in het plan parcial Cansalades-Umbría.

En van die 266 residentiële vlakken zijn er 140 **urbanizable** en 126 urbaan. Meer dan de helft van
de als residentieel gezoneerde grond is dus nog geen bouwgrond.

### Hoeveel zit het model ernaast

| Situatie | Werkelijke coëfficiënt | Model zit ernaast | Aandeel |
|---|---|---|---|
| Zona E, gewone gebieden, netto-lezing | 0,20 | **0 %** | 93,8 % van S.U. extensivo |
| Zona E, zeven uitzonderingsgebieden | 0,28 | **−28,6 %** (te laag) | 6,2 % van S.U. extensivo |
| Zona E, bruto-lezing als de cessie niet is voldaan | 0,142 | **+40,8 %** (te hoog) | per perceel |
| Zona C grado III | 0,80 | −75 % | — |
| Zona A casco en zona B | geen coëfficiënt | onbruikbaar | — |
| SNU genérico I en II | 0,03, max. 300 m² | +567 % | — |
| SNU genérico III, El Plà | 0,01, max. 300 m² | +1.900 % | — |
| SNUEP, Parque Natural, PATIVEL | 0 | oneindig te hoog | — |
| Urbanizable zonder programa | 0 | oneindig te hoog | 140 van 266 res. vlakken |

De aandelen bij zona E komen uit de oppervlaktetabel van het plan zelf (full nº 145–146). De som van
de 38 extensieve gebieden die ik heb overgetypt komt op 16.420.331 m², precies het totaal dat het
plan er zelf onder zet. Dat is een sluitende controle op mijn leeswerk.

De zeven gebieden met 0,28 in plaats van 0,20 zijn Calvario, Puchol, Soberana, Mesquides, Cuesta de
San Antonio, Caleta-Puerto en La Corona. Samen 1.019.211 m², ruim 6 % van het extensieve stadsgebied,
en het zijn juist de gebieden dicht bij het centrum en de haven. Daar rekent het model het bouwrecht
**40 % te klein** — een perceel van 1.000 m² in Puchol mag 280 m²t in plaats van 200 m²t.

### De bruto-netto-val

Dit is de grootste onzekerheid en hij zit niet in het model. Het plan kent twee getallen: 0,142 over
het bruto oppervlak inclusief wegen en cessiegronden, en 0,20 over het netto perceel. Het verschil is
de cessie van 29,07 % die in suelo extensivo moet worden afgestaan voor wegen en groen
(art. 4.1.7–4.1.9). Past de gemeente 0,20 zonder meer toe op een kavel in een al aangelegde
urbanisatie, of moet de eigenaar eerst aantonen dat die cessie is voldaan? Wij weten het niet
(bewijstype 7). Valt het negatief uit, dan rekent het model 41 % te veel bouwvolume — en dat is
precies de kant waar een miskleun geld kost.

### Het plafond van 450 m²

Het PGOU kent in zona E geen absoluut plafond in m². Het model knipt het bouwrecht af boven een
perceel van 2.250 m²:

| Perceel | PGOU 0,20 | Model | Afwijking |
|---|---|---|---|
| 3.000 m² | 600 m²t | 450 m²t | −25 % |
| 5.000 m² | 1.000 m²t | 450 m²t | −55 % |
| 10.000 m² | 2.000 m²t | 450 m²t | −77,5 % |

Als 450 m² een commerciële keuze is — grotere villa's verkopen slechter, of TREE bouwt ze niet — dan
is dat prima, maar dan hoort het als verkoopaanname in het kader, niet als bouwrecht in de
planregels. Nu lopen die twee door elkaar.

### Wat ik zou veranderen

1. Coëfficiënt uit `N01-bouwregels-xabia.json` halen op basis van het B.2-gebied, met 0,20 als
   terugval en 0,28 voor de zeven gebieden.
2. Naast het bouwvolume ook de footprint toetsen: `ocupación(grado) × perceel`, standaard 30 % (E2).
   Bij grado I is 20 % bindend en gaat er maar één bouwlaag op.
3. Een vlag `planregime` per object: `pgou_zona_e`, `eigen_plan`, `urbanizable_zonder_programa`,
   `snu`, `casco`. Alles buiten `pgou_zona_e` krijgt geen automatische rekensom maar een
   handmatig-vlag.
4. Bruto/netto als gevoeligheidsschuif, 0,142 tot 0,20, naast de bestaande schuiven.
5. Het plafond van 450 m² losknippen van de planregel.

---

## 4. Parcela mínima per gebied

Uit de tabel *Suelo urbano — resumen (SU)*, ordenanzas full nº 145–146, visueel gelezen. Bewijstype 2.
Welk gebied op een perceel van toepassing is, staat op plano B.2; de gebiedsnamen volgen ruwweg de
oude kadastrale toponiemen (art. 2.1.6).

Oppervlakte is het gebiedstotaal uit het plan, handig om te wegen hoe zwaar een gebied telt.

| Gebied | Parcela mín. | Opp. (m²) | Gebied | Parcela mín. | Opp. (m²) |
|---|---|---|---|---|---|
| Aduanas | 700 | 71.800 | Mar Azul | 1.000 | 91.400 |
| Casco | 700 | 89.820 | Masenes | 1.000 | 104.000 |
| Playas | 600 | 62.600 | Media Luna | 1.000 | 165.600 |
| Saladar | 1.000 | 99.700 | **Mesquides** | 1.000 | 286.925 |
| Granadella | 1.000 | 48.920 | Montgó | 1.500 | 822.949 |
| Adsubia-Cansalades | 1.000 | 700.420 | Montgó-Barranqueres | 1.500 | 564.310 |
| Adsubia-Cap Martí | 1.000 | 1.194.190 | Montgó-Castellans | 1.500 | 1.061.000 |
| Adsubia-Rebaldí | 1.000 | 749.468 | Montgó-Ermita | 1.500 | 1.271.700 |
| Balcón al Mar | 1.000 | 1.471.895 | Portichol 1 Norte | 1.500 | 133.200 |
| **C.S. Antonio** | 1.000 | 234.318 | Portichol 1 Sur | 1.000 | 127.800 |
| Cala Blanca Norte | 1.500 | 79.000 | Portichol 2 | 1.000 | 139.960 |
| Cala Blanca Sur | 1.000 | 170.400 | **Puchol** | 1.000 | 295.760 |
| **Caleta-Puerto** | 500 | 18.568 | Rafals | 1.000 | 42.000 |
| **Calvario** | 700 | 111.280 | Senioles | 1.500 | 422.700 |
| Cansalades | 1.000 | 150.400 | Senioles-Colomer | 1.500 | 1.069.310 |
| Capsades 1 | 1.000 | 78.000 | **Soberana** | 1.000 | 72.360 |
| Capsades 2 | 1.000 | 35.200 | Toscal-Cap Martí | 1.000 | 475.560 |
| Cap Martí | 1.000 | 213.720 | Tosalet | 1.000 | 1.066.130 |
| Costa Nova | 1.000 | 633.808 | Trencall | 1.000 | 172.000 |
| Covatelles | 1.500 | 550.720 | Valls | 1.500 | 410.400 |
| Entrepinos | 1.000 | 82.840 | | | |
| Lluca | 1.500 | 953.400 | | | |
| Lluca-Rafalet | 1.000 | 197.640 | | | |

**Vet** = de gebieden met 0,28 neto in plaats van 0,20. La Corona hoort daar ook bij (toegevoegd bij
Modificación I) maar komt in deze tabel niet voor; zijn parcela mínima is ONBEKEND.

**Splitsen** kan pas vanaf tweemaal het minimum (TRLOTUP art. 248.c). Dus 2.000 m² in Tosalet,
3.000 m² in Montgó-Ermita, 1.400 m² in het Casco.

**Kleinere kavels kunnen toch bebouwbaar zijn** als ze zijn ingesloten door bebouwde percelen, of als
het suelo urbano extensivo al vóór Modificación XXV als *consolidado por la urbanización* gold. De
ondergrens is dan 70 % van het gebiedsminimum met een absolute bodem van 700 m², plus een toegang van
minimaal 3 m (art. 10.5.1.1, tekst Mod. XXV, BOP nº 240 van 16-12-2016). Verder moet er een rechthoek
van 15 × 24 m in het perceel passen en is het gevelfront minimaal 20 m, of 10 m aan een doodlopende
weg.

---

## 5. Retranqueos, zwembad en bijgebouwen

**Afstanden in zona E** (art. 10.5.1.5, visueel gelezen op zowel het Mod. I-blad als het origineel):

| Grado | Tot de rooilijn | Tot de perceelgrens |
|---|---|---|
| I | 5 m | 5 m |
| II (standaard) | 5 m | 5 m |
| III | 0 m | 2,5 m |

Kelders en hellingbanen onder maaiveld blijven in de zones C, E, F, G en H minimaal 2,5 m van de
grens (art. 8.1.27).

**Telt het zwembad mee in de edificabilidad?** Nee. Het bassin staat niet in de opsomming van
art. 8.1.15 en is onder art. 8.1.5 noch overdekt noch gesloten, dus het telt ook niet mee voor de
ocupación. Het plan noemt het zwembad alleen als element van de urbanisatie, met afstandseisen. Dit
is mijn afleiding uit de plantekst, bewijstype 5 — de regels zeggen het niet met zoveel woorden.

Wat er wél over het zwembad in staat: 2 m van de perceelgrens, maximaal 2,5 m boven het natuurlijke
terrein, zuivering verplicht, en een pomphuis dat meer dan 1 m boven het terrein uitkomt op minimaal
5 m van de grens.

**Tellen bijgebouwen mee?** Ja, maar alleen als ze gesloten én overdekt zijn. Art. 10.5.1.7 zegt het
letterlijk: *"contarán como superficie edificada siempre que estén cerradas y cubiertas"*. Voor de
ocupación is de drempel lager — art. 8.1.5 telt alles wat overdekt **of** gesloten is. Een open
carport telt dus wel voor de bezetting en niet voor het bouwvolume.

**Wat verder meetelt** (art. 8.1.15): alle beloopbare verdiepingen behalve toegestane kelders;
terrassen, balkons en overdekte uitkragingen, ook als ze open zijn — half geteld bij een overdekt
terras dat aan één zijde openstaat. **Wat niet meetelt:** binnenpatio's ook als ze dicht zijn, platte
daken ook als je erop kunt lopen, openbare arcades, kassen en afdaken van doorschijnend materiaal met
een lichte demontabele constructie, en sierelementen op het dak.

**Carports:** geen zijwanden, dak van doorlatend materiaal zoals riet of beplanting, maximaal 30 m²
en 2,20 m hoog, hoekstijlen maximaal 25 × 25 cm. Daken van metselwerk, dakpan of vezelcement zijn
uitdrukkelijk verboden.

**Parkeren:** twee plaatsen per woning binnen het perceel. **Watertank:** elke woning een regeltank
van minimaal 10.000 liter, ingegraven of onder de woning. Dat laatste is een kostenpost die in
offertes vaak ontbreekt.

---

## 6. De wijken waar wij objecten hebben

De gebiedsnamen van plano B.2 zijn oude kadastrale toponiemen en vallen grotendeels samen met hoe wij
de wijken noemen. Waar dat zo is, is de koppeling hieronder eenvoudig; waar de naam niet voorkomt
staat ONBEKEND. De harde grens komt uit plano B.2, die alleen als scan in het register zit en niet
gegeorefereerd is. Bewijstype 5 voor de koppeling, 2 voor de getallen.

| Wijk | Zone | B.2-gebieden | Parcela mín. | Edificabilidad | Let op |
|---|---|---|---|---|---|
| **Montgó / Ermita** | E | Montgó, Montgó-Ermita, Montgó-Castellans, Montgó-Barranqueres | 1.500 m² | 0,20 | Parque Natural hogerop: geen nieuwbouw. Delen vallen onder Plan Parcial Ermita II. Splitsen pas vanaf 3.000 m² |
| **Centrum** | A + B | Casco, Calvario | 700 m² | geen coëfficiënt in zona A | Erfgoedregime NHT, toestemming Conselleria de Cultura. Calvario is zona E mét 0,28 |
| **Puerto / Arenal** | A, B, C, E door elkaar | Aduanas, Playas, Caleta-Puerto, Saladar | 500–1.000 m² | wisselt | Caleta-Puerto: 0,28 en de laagste parcela mínima van de gemeente (500 m²). Homologaciones Arenal-3 en Aduanes-1. PATIVEL langs de kust |
| **Tosalet / Adsubia** | E | Tosalet, Adsubia-Cansalades, Adsubia-Cap Martí, Adsubia-Rebaldí, Cansalades | 1.000 m² | 0,20 | Delen onder Plan Parcial Cansalades-10 en Cansalades-Umbría. Splitsen vanaf 2.000 m² |
| **Granadella / Balcón al Mar** | E | Granadella, Balcón al Mar, Cap Martí, Toscal-Cap Martí, Portichol 1 en 2, Covatelles | 1.000 m², Covatelles en Portichol 1 Norte 1.500 | 0,20 | La Granadella werd in 1991 SNUEP: geen nieuwbouw. Balcón al Mar is met 1.471.895 m² het grootste extensieve gebied |
| **Rafalet / Pinosol** | E | Lluca-Rafalet, Lluca, Rafals | 1.000 m², Lluca 1.500 | 0,20 | **Pinosol komt niet als eigen gebied in de B.2-tabel voor — ONBEKEND**. Homologación en PRI voor UE Lluca-Rafalet 7 en 13 |

---

## 7. Wat je per perceel moet ophalen voordat het model mag rekenen

In deze volgorde. Stap 1 tot en met 3 bepalen of de tabel uit §1 überhaupt van toepassing is.

1. **Kadastrale referentie en geometrie.** Zonder dat is de rest giswerk.
2. **Klasse en instrument** uit de zonelaag van de Generalitat (WFS `Planeamiento.Zonificacion` op de
   centroïde). Staat er een plan parcial, homologación, PRI of estudio de detalle in het veld
   `denominaci`, dan gelden díe normen en stopt de standaardrekensom.
3. **Is het suelo urbano of urbanizable?** Urbanizable zonder vastgesteld programa: bouwvolume 0.
4. **Gebied uit plano B.2** → parcela mínima en de coëfficiënt (0,20 of 0,28).
5. **Grado uit plano B.1** → ocupación, bouwlagen, hoogte, retranqueos. Geen letter = E2.
6. **Is het een solar?** Water, stroom, toegang en afvalwaterzuivering geregeld (art. 8.1.6). Veel
   extensieve urbanisaties hebben geen riolering.
7. **Informe urbanístico** van de gemeente of een cédula de garantía urbanística, het schriftelijke
   uittreksel waarin de gemeente het bouwrecht bevestigt (TRLOTUP art. 246). De cédula moet binnen een
   maand worden afgegeven en is een jaar geldig.

De zonelaag van de Generalitat is uitdrukkelijk informatief — *"El planeamiento aquí reflejado tiene
carácter informativo"* — en bevat aantoonbaar fouten: hij toont nog twintig vlakken van de
homologación Portitxol, die het register zelf als vernietigd markeert (TSJCV 26-04-2012). Gebruik hem
als filter, nooit als bouwrecht. Hetzelfde geldt voor de landelijke planviewer SIU van het
ministerie, die zichzelf omschrijft als "geen openbaar planregister".

**Vaste waarschuwing in elk dealdossier:** de uitkomst van de zonelaag en de PGOU-tabellen is een
eerste filter. Bouwrecht staat pas vast na een informe urbanístico of cédula, controle van het plan
parcial of de unidad de actuación, en toetsing door een lokale architect.

---

## 8. Wat ik niet heb kunnen vaststellen

- **Zones D, G en H**: parameters niet opgehaald. Voor ons werk weinig relevant (conjuntos
  arquitectónicos, industrie, geconcentreerde detailhandel), maar het staat er niet.
- **Ocupación in zona E na Modificación I.** Het vervangingsblad full nº 146 eindigt na punt 5,
  separación a linderos. De percentages 20/30/50 staan alleen op het doorgehaalde oorspronkelijke
  blad full nº 147. Of Modificación I ze ongewijzigd laat, is niet bevestigd. Dit corrigeert R12,
  dat schreef dat de alinea door de goedkeuringsstempel was afgedekt — het blad houdt er gewoon op.
- **Bruto of netto.** Of de gemeente 0,20 direct toepast op een kavel in een aangelegde urbanisatie,
  of eerst de cessie van 29,07 % toetst. Grootste financiële onzekerheid in dit stuk.
- **Gelden de NUT na 15 maart 2025 nog?** Open. Voor de edificabilidad maakt het niet uit, voor de
  bouwhoogte in het Casco wel.
- **Onder welk B.2-gebied valt Pinosol?** Niet in de tabel te vinden.
- **Parcela mínima van La Corona.** Wel 0,28, niet in de tabel.
- **Geconsolideerde plantekst.** Die bestaat niet. De register-pdf verwerkt Modificación I en een
  zona C-wijziging, maar niet Mod. XXV (2016) of Mod. 27 (2003). Er is geen texto refundido.
- **Plano B.1 en B.2 per perceel.** Scans in het register, niet gegeorefereerd. Zolang dat zo is,
  blijft "welk gebied, welk grado" handwerk.
- **De VUT-plafonds per wijk** uit Modificación 41: de gepubliceerde lijst geeft zes zones met
  percentages, maar de vertaalde weergave is intern tegenstrijdig over welke zone welk getal heeft.
  Niet overgenomen. Bewijstype 7.
- **robots.txt van mivau.gob.es** (landelijke planviewer) gaf 403, dus niet gecontroleerd en niet
  automatisch uitgelezen. Voor `ajxabia.com` gecontroleerd op 18-09-2026: alles toegestaan behalve
  `/bd/archivos/`. De publicatieborden op `sedelectronica.es` staan op `Disallow: /*` en zijn niet
  automatisch benaderd.

---

## ⏸️ ACTIE VOOR JAN

Drie dingen die alleen jij los kunt maken, op volgorde van wat ze opleveren.

1. **Vraag de gemeente schriftelijk of 0,20 netto direct geldt op bestaande kavels in aangelegde
   urbanisaties, of dat de cessie van 29,07 % eerst wordt getoetst.** Dit is één vraag per e-mail aan
   Urbanisme en het scheelt in elke berekening tot 41 % bouwvolume. Zeg het als je wilt dat ik een
   concept opstel; dan zet ik het in `acties/` klaar en gaat er niets weg zonder jouw akkoord.
2. **Vraag bij de gemeente het geldende texto refundido van de normas urbanísticas op**, of laat een
   lokale architect bevestigen dat de ocupación 20/30/50 na Modificación I nog staat.
3. **Bij elk perceel dat we serieus nemen: informe urbanístico aanvragen** (TRLOTUP art. 246.4). Dat
   is de enige papieren die telt. Kosten en doorlooptijd zijn me niet bekend — wil je dat ik dat
   uitzoek?

---

## 9. Bronnen

| # | Bron | URL | Datum | Type |
|---|---|---|---|---|
| 1 | PGOU Xàbia — Ordenanzas (240 blz.), Registro Autonòmic GVA | `https://mediambient.gva.es/auto/urbanismo/reg-planeamiento/2%20ALICANTE/03082%20X%C0BIA/1%20P.%20GENERAL/03082-1000%20PLAN%20GENERAL/3%20NORMAS%20URBAN%CDSTICAS/03082-1000%20ORDENANZAS.pdf` | 15-09-2026, herlezen 18-09-2026 | 2 |
| 2 | Registro Autonòmic, mapindex Xàbia — 34 instrumenten, geen PGE | `https://mediambient.gva.es/auto/urbanismo/reg-planeamiento/2%20ALICANTE/03082%20X%C0BIA/1%20P.%20GENERAL/` | 18-09-2026 | 3 |
| 3 | Acuerdo Consell 10-09-2021, NUT Xàbia, DOGV | `https://dogv.gva.es/` (DOGV 20-09-2021) | 15-09-2026, herlezen 18-09-2026 | 2 |
| 4 | Acuerdo Consell 05-03-2021, gedeeltelijke schorsing PGOU | `https://dogv.gva.es/datos/2021/03/15/pdf/docv_9041.pdf` | 15-09-2026 | 2 |
| 5 | TRLOTUP, geconsolideerde tekst 02-07-2026 | DOGV | 15-09-2026 | 2 |
| 6 | GVA-zonelaag, WFS `Planeamiento.Zonificacion` — eigen telling 356 vlakken Xàbia | `https://terramapas.icv.gva.es/0702_Planeamiento` | 18-09-2026 | 3 |
| 7 | Ayuntamiento de Xàbia, pleno 30-04-2019 keurt propuesta definitiva PGE goed | `https://www.ajxabia.com/ver/7823/el-pleno-aprueba-la-propuesta-definitiva-de-plan-general-estructural-.html/` | 18-09-2026 | 4 |
| 8 | Modificación XXV, condiciones de parcelas, BOP nº 240 van 16-12-2016 | Registro Autonòmic 03082-1101 | 15-09-2026 | 2 |
| 9 | Generalitat waarschuwt Xàbia over weigeren van vergunningen op grond van een niet vastgesteld plan | `https://lamarina.eldiario.es/2025/02/17/generalitat-advierte-xabia-responsabilidad-licencias-plan-general-no-aprobado/` | 18-09-2026 | 1 |
| 10 | Modificación nº 41 PGOU, VUT-plafond, pleno 28-05-2026 | `https://en.javea.com/xabia-aprueba-la-regulacion-de-las-viviendas-turisticas-limite-por-barrios-y-suspension-de-nuevas-licencias/` | 18-09-2026 | 1 |
| 11 | Sistema de Información Urbana (SIU), ministerie — "no es un registro público de planeamiento" | `https://www.mivau.gob.es/urbanismo-y-suelo/sistema-de-informacion-urbana` | 18-09-2026 | 4 |
| 12 | robots.txt ajxabia.com | `https://ajxabia.com/robots.txt` | 18-09-2026 | 1 |

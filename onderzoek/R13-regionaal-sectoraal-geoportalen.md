# R13 — Regionale wetgeving, sectorale beperkingen en geoportalen (Xàbia/Jávea)

> **NA TEGENSPRAAK (15-09-2026).** Dit rapport is door een tweede agent gecontroleerd; zie `R13-regionaal-sectoraal-geoportalen.verificatie.md`. Betrouwbaarheid volgens die controle: hoog.
> Weerlegd en in de eindstukken gecorrigeerd: R13-10. Gebruik voor die punten de gecorrigeerde tekst in het verificatiebestand, niet de tekst hieronder.


**Controledatum:** 15-09-2026 (alles wat in dit rapport "getest" of "gezien" heet, is op die datum gecontroleerd, tenzij anders vermeld)
**Stroom:** R13 · TREE Deal Hunter fase A · masterprompt §15 en §17
**Bewijstypen (§5):** 1 aanbieder · 2 officiële bron · 3 door ons vastgesteld (live test) · 4 AI-inferentie · 5 berekening op benoemde aannames · 6 professional · 7 onbekend/tegenstrijdig

## Samenvatting (10 regels)

1. De TRLOTUP (Decreto Legislativo 1/2021) is op boe.es geconsolideerd tot 02-07-2026 (Ley 3/2026 verwerkt, "actualización en proceso"); een "Ley 8/2024" die de TRLOTUP wijzigt bestaat niet — Ley 8/2024 is de toegankelijkheidswet. De grote wijzigingen zijn Ley 6/2024 (vereenvoudiging), Ley 3/2025 (kust) en Ley 3/2026.
2. Nieuwe vrijstaande woning op niet-bebouwbare grond (SNU): minimaal 1 ha per woning, maximaal 2 % bebouwd, buiten afvoergeulen, geen kern vormen (art. 211.1.b); stilzwijgen = afwijzing (art. 214.5); in SNU verjaart handhaving niet (art. 255.5).
3. Legalisering via "minimización de impacto territorial" kan alleen voor gebouwen die vóór 20-08-2014 volledig af waren (art. 228.3), en daarna mag er nooit meer bebouwd oppervlak bij (art. 231.3). De GVA-laag `MinimizacionViviendasSNU` telt 585 percelen in Xàbia.
4. PATRICOVA is bindend voor iedereen (art. 3). Op niet-bebouwbare grond met gevaarniveau 2–5 of geomorfologisch gevaar zijn woningen verboden (art. 18.2). Op stedelijke grond legt de gemeente aanpassingseisen op "tomando como referencia" bijlage I (art. 20).
5. Live test Arenal (38,7749157 / 0,1850741): PATRICOVA niveau 4 (zone AC07 "Riu de Xaló o de Gorgos", T100, waterdiepte < 0,8 m). De nationale ARPSI-kaart (IDEE) geeft op dat punt T10 = 0,073, T100 = 1,951 en T500 = 2,466 (eenheid niet vermeld, vermoedelijk meter). Dat is een tegenstrijdigheid die een deskundige moet beoordelen.
6. Volgens de officiële laag ligt in Xàbia ongeveer 820 ha in PATRICOVA-niveau 1–6 (±12 % van 6.894 ha) plus ongeveer 382 ha geomorfologisch gevaar. Het gaat om l'Arenal (P4/P6), el Saladar (P3, Barranco del Tosalet), de Gorgos-vallei (P1–P5) en de rand van de oude kern (P6); de haven/Duanes valt onder geomorfologisch gevaar.
7. Live test Granadella (38,7312412 / 0,1934719): beschermde plattelandsgrond (SNU-P ZRP-NA-MU), ZEC/ZEPA "Penya-segats de la Marina" zone B, strategisch bosterrein (PATFOR), brandinterface "Alta", binnen de brandperimeters van 2000 en 2016, 14 m van de Barranc de Martorell. Geen PATRICOVA-zone.
8. De Montgó-flank (pin K07 Montgó-Ermita) valt binnen het PORN Montgó-gebied, zone "Áreas urbanas y urbanizables". Grondverzet vraagt daar een voorafgaand rapport van de Conselleria (PORN art. 109.5.f); binnen het park geldt in principe een bouwverbod (art. 56). In de Zona de Uso Especial Les Planes is zonder plan especial geen nieuwbouw mogelijk, en daarna pas vanaf 10.000 m² (art. 56.2–3).
9. PATIVEL (Decreto 58/2018) is nog van kracht (TS 27-04-2022 heeft de nietigverklaring door de TSJCV gecasseerd), met gedeeltelijke vernietigingen die in 2025–2026 zijn uitgevoerd, maar niet voor Xàbia. Ley 3/2025 hernoemt het plan tot "Plan de Ordenación Costera" en gaat voor waar ze strijdig zijn. In Xàbia ligt ±56 ha Litoral 1 en ±10 ha Litoral 2 rond el Portitxol en Cap Negre.
10. Geoportalen: ICV terramapas (WMS/WFS, CC BY 4.0), ICV ArcGIS REST, IDEE, IGN PNOA, Catastro en IGME werken en zijn per punt te bevragen. De MITECO-diensten (SNCZI-WMS, DPMT/deslinde-WMS en -viewer) gaven op 15-09-2026 een serverfout, 503 of verbindingsreset; de deslindelijnen van Xàbia zijn daardoor niet getest (ONBEKEND).

---

## 0. Methode, testpunten en leeswijzer

- **Werkwijze:** wetteksten zijn gelezen als geconsolideerde tekst op boe.es of als DOGV-pdf; de pdf-tekst is lokaal uitgelezen met macOS PDFKit via een Swift-script in de scratchpad, zonder installatie. Kaartdiensten zijn rechtstreeks bevraagd met `curl`/`httpx`: GetCapabilities, GetFeatureInfo, WFS GetFeature en ArcGIS REST `identify`/`query`. De aantallen verzoeken zijn laag gehouden: per laag hooguit enkele verzoeken, geen tegelreeksen. De eindpunten komen uit de officiële configuratie van visor.gva.es (`https://icvficherosweb.icv.gva.es/00/geovisorgva/params/pro/configCapas.js`) en uit ministeriële catalogi, niet uit geheugen.
- **Oppervlakteschattingen** (bewijstype 5): het PATRICOVA-polygoon is doorsneden met de officiële gemeentegrens van Xàbia (ICV WFS `ICV.Municipios`: 6.893,84 ha) via een puntraster van 60 m (1 punt = 0,36 ha), een vereenvoudigde grens (±600 hoekpunten) en de aanname dat gevaarniveaus niet overlappen [te verifiëren]. De uitkomst is een orde van grootte, geen landmeting.
- **Plaatsnamen** komen uit de officiële Nomenclàtor Toponímic Valencià (ICV WFS `NTV.*`, bewijstype 2); het zijn zwaartepunten van de toponiemen, geen perceelsgrenzen.

### Testpunten

| Code | Coördinaat (lat, lon) | Herkomst | Kadastrale referentie (Catastro, getest) |
|---|---|---|---|
| P1 Arenal | 38,7749157 / 0,1850741 | opdracht | 5658011BC5955N (stedelijk) |
| P2 Granadella | 38,7312412 / 0,1934719 | opdracht | 03082A01200623 (landelijk, polígono 12, parcela 623) |
| P3 Montgó-flank | 38,7936 / 0,1214 | advertentiepin K07 uit R15 (bewijstype 1, benaderend) | niet opgevraagd |
| P4 Montgó-park | 38,8045 / 0,1500 | zelf gekozen punt binnen het park (ter controle) | niet opgevraagd |
| T-punten | zwaartepunten NTV-toponiemen (l'Arenal, el Saladar, les Duanes, el Pou del Moro, el Portitxol, enz.) | ICV Nomenclàtor | — |

---

## 1. Kernconclusies voor de Deal Hunter

1. **Zet de sectorale toets vóór de financiële analyse.** Vier lagen kunnen een dealhypothese onmiddellijk ongeldig maken, en alle vier zijn automatisch per coördinaat te bevragen: PATRICOVA (niveau en zone), PORN Montgó (ámbito en zone), Red Natura 2000 (ZEC/ZEPA met zone A–D) en de planclassificatie (SU/SUZ/SNU-C/SNU-P) (bewijstype 3).
2. **Een pin is geen perceel.** Van de 40 BP-objecten in Jávea met coördinaten hebben er 3 een nepcoördinaat (25,6865 / −80,4313, Florida), ligt er 1 buiten de gemeentegrens en delen er 2 exact dezelfde "centrum"-coördinaat (§10). Een sectorale uitslag op een advertentiepin is daarom hooguit een **signaal** (bewijstype 4) totdat Catastro de perceelgeometrie heeft bevestigd (zie R11).
3. **"Geen beperking gevonden" is niet hetzelfde als "geen beperking aanwezig".** Voorbeelden uit de tests: de PATIVEL-ámbitos zijn **lijnen**, geen vlakken, zodat een puntbevraging altijd 0 geeft (§5.4). De MITECO-deslindelaag was niet bereikbaar (§6.4). De raster-GFI van PATFOR/brandrisico geeft een cel van ±500 m terug, niet het perceel (§4.1).
4. **Renovatie in SNU is juridisch het riskantst.** Voor gebouwen zonder vergunning in SNU is er geen verjaring van handhaving (TRLOTUP art. 255.5). Na 15 jaar "gedogen" in ander grondgebied mag er niet worden verbouwd of uitgebreid (art. 256). Legalisering loopt via minimización en geeft nooit extra m² (art. 231.3). Een koper erft dit risico. De GVA-laag met woningen die in aanmerking komen voor minimización (585 percelen in Xàbia) is een goede eerste zeef, geen oordeel.
5. **Brand is een concrete kostenpost.** Xàbia heeft zijn cartografische afbakening van de bos-bebouwingsgrens volgens TRLOTUP DA 7 volgens de GVA-laag op 28-05-2026 in de gemeenteraad goedgekeurd. Eigenaren hebben daarna zes maanden om aan bijlage XI te voldoen, onder meer een strook van 30 m (DA 7.10). De eigen dossiertermijn is daarmee ±eind november 2026 (bewijstype 5, aanname: de datum in de laag is de aanvangsdatum) [te verifiëren bij het Ajuntament].

---

## 2. TRLOTUP — regionale ruimtelijke-ordeningswet (opdracht a)

### 2.1 Status en wijzigingen tot 2026

| Norm | Wat het doet voor de TRLOTUP (relevant voor ons) | Bron | Bewijstype |
|---|---|---|---|
| Decreto Legislativo 1/2021, 18-06 (DOGV 9129, 16-07-2021; in werking 17-07-2021) | Basistekst | boe.es DOGV-r-2021-90283 | 2 |
| Decreto-ley 7/2024 (9-07) → **Ley 6/2024, 5-12, de simplificación administrativa** (BOE-A-2025-1) | 55 wijzigingen; o.a. art. 228.2 (de voorwaarde "que conserven una parcelación de características rurales" is geschrapt), art. 210.6 (tertiair gebruik in SNU-kust, hotels ≥ 200 m van de kustlijn), art. 211.1.d–f, DA 7.11 | boe.es; historische versie 16-07-2021 van art. 228 vergeleken | 2/3 |
| Ley 2/2025, 15-04 (maatregelen na de DANA, BOE-A-2025-9743) | Art. 55.2, 194.1.c, 196.4.a, DT 24 | boe.es | 2 |
| **Ley 3/2025, 22-05, de protección y ordenación de la costa valenciana** (BOE-A-2025-11647; in werking 15-06-2025) | Art. 238.4: bij kustvergunningsplicht moet de gemeente vóór de bouwvergunning een **bindend rapport** van de Generalitat vragen; art. 105.1.h | boe.es | 2 |
| Decreto-ley 14/2025, 26-12 → **Ley 3/2026, 29-06, contra la hiperregulación** (BOE-A-2026-15683; in werking 03-07-2026) | Regeling van projecten van regionaal belang (art. 17, 63–66 ter), **art. 242.1 stilzwijgen**, DA 4 (ECUV), DT 4, 24 en 32, bijlage IV | boe.es | 2 |
| "Ley 8/2024" | **Geen TRLOTUP-wijziging.** Ley 8/2024 van 30-12 is de wet op de universele toegankelijkheid (BOE-A-2025-717) | boe.es (zoekresultaat) | 2 |
| Anteproyecto "Ley del Suelo de la Comunitat Valenciana" | **In procedure, niet van kracht.** Openbare inzage aangekondigd door de GVA (08-01-2026); volgens de pers heeft de Consell het voorontwerp op 17-07-2026 goedgekeurd [te verifiëren, niet-officiële bron] | mediambient.gva.es/…/urbanismo/novetats | 2 (inzage) / 1 (pers) |

Let op: op de BOE-pagina staat "Atención: última actualización en proceso". Wijzigingen van na 02-07-2026 kunnen dus nog ontbreken (bewijstype 3).

### 2.2 Niet-bebouwbare grond (SNU): vrijstaande woning

- **Art. 211.1.b** (bewijstype 2) — "vivienda aislada y familiar":
  - 1.º Perceel met een ononderbroken omtrek dat aan het minimum van het plan voldoet, "que en ningún caso será inferior a una hectárea por vivienda".
  - 2.º Bebouwd oppervlak ≤ 2 % van de finca; de rest blijft natuurlijk of in cultuur. Aanvullende voorzieningen zonder bouwwerk boven maaiveld ≤ 2 %.
  - 3.º Buiten de natuurlijke afvoergeulen; bestaande bomen en het terrein respecteren.
  - 4.º Drinkwater, afval en afvalwaterzuivering voor rekening van de eigenaar.
  - 5.º Geen kernvorming; geen groepering van woningen op één perceel.
  - Uitzondering alleen voor een woning die aan een agrarisch bedrijf is gebonden (≥ 1 arbeidseenheid of beroepsagrariër), mits het plan de zone heeft afgebakend en de landbouwconselleria gunstig adviseert.
- **Art. 210.2**: zolang geen plan het toestaat, maximaal **twee bouwlagen**, gemeten op elk punt van het maaiveld. **Art. 210.4–5**: nieuwbouw moet voldoen aan **bijlage XI** (brandpreventie). Bestaande bouw van vóór 20-08-2014 die wordt geregulariseerd, alleen voor zover het gemeentelijk brandpreventieplan dat vereist.
- **Art. 214.4**: de vergunning wordt verleend onder voorwaarde dat de koppeling van het minimumperceel en de **ondeelbaarheid** in het eigendomsregister worden ingeschreven. **Art. 214.5**: termijn verstreken = **afwijzing**.
- **Art. 215.1–2**: voor woningen (211.1.b) is geen DIC nodig, wel adviezen van de conselleria. In **SNU protegido** is een advies van de urbanismo-conselleria verplicht, plus dat van de beheerder van de beschermingswaarde (215.2.c).
- **Art. 216**: DIC (declaración de interés comunitario) voor industrie, tertiair gebruik (hotels, horeca) en art. 211.1.g; art. 211.2 vraagt minimaal 0,5 ha voor tertiair gebruik.
- **Art. 247–249**: splitsingen van landelijke percelen onder het minimum voor een vrijstaande woning zijn in principe niet toegestaan (art. 249, tekst gezien; details [te verifiëren]).

### 2.3 Bestaande woningen zonder vergunning: minimización, verjaring, regelingen van vóór 1975

| Regel | Inhoud | Bewijstype |
|---|---|---|
| Art. 228.2 | Groep woningen in SNU vanaf **3 woningen/ha** (lagere dichtheid mogelijk "por condiciones de proximidad, de infraestructuras y territoriales") | 2 |
| Art. 228.3 | Legalisering alleen van gebouwen "completamente acabadas antes del 20 de agosto de 2014". Zonder goedgekeurd instrument vervalt de weg en volgt handhaving (art. 250 e.v.) | 2 |
| Art. 228.4 / 230.4 | In beschermd gebied of bij beperkingen uit kust-, water-, **overstromings**- of infrastructuurwetgeving: **voorafgaand bindend advies** van de bevoegde overheid | 2 |
| Art. 228.5 / 230.2 | Bij bosgebied of overstromingsgebied: maatregelen, een verklaring dat de eigenaar het risico aanvaardt, en een **aantekening in het eigendomsregister** bij de verklaring van eerste ingebruikname | 2 |
| Art. 229 | Plan especial (vastgesteld door de conselleria) en programa de minimización. Kosten van gemeenschappelijke voorzieningen: 80 % naar m² bebouwd, 20 % naar perceeloppervlak; veranda's, sport en zwembad tellen voor 0,5 m² per m² | 2 |
| Art. 230 | Geïsoleerde woning: individuele verklaring door de **gemeenteraad** → minimización-vergunning (landschapsstudie, basisproject) → binnen **4 jaar** ingebruiknamevergunning | 2 |
| **Art. 231.3** | "no se podrá conceder ninguna licencia de obra o uso que implique una ampliación de la edificabilidad patrimonializada" — hooguit interne verbouwing en kleine hulpelementen, na bindend advies | 2 |
| **Art. 255.1 / 255.5** | Handhavingstermijn **15 jaar** na voltooiing, maar **niet** voor SNU, groen- en verkeersbestemmingen, publiek domein en erfgoed: daar verjaart het herstel van de rechtmatige toestand niet | 2 |
| Art. 256 | Na 15 jaar geen legalisering; "no podrán llevarse a cabo obras de reforma, ampliación o consolidación" | 2 |
| DT 26 | Geïsoleerde gebouwen in SNU die **vóór de Ley 19/1975** gereed waren en gebruik en typologie hebben behouden, worden gelijkgesteld met vergund | 2 |
| DT 28 | Geen minimización-procedure vóór het feitelijk functioneren van de Agencia Valenciana de Protección del Territorio (streefdatum 31-12-2021). Of die er nu is: [te verifiëren] | 2/7 |
| Art. 206 | Fuera de ordenación: alleen "obras de mera conservación"; het plan moet een overgangsregeling geven voor gebouwen die niet volledig passen | 2 |

**Kaartlaag (getest, bewijstype 3):** `https://terramapas.icv.gva.es/0702_Planeamiento`, laag `MinimizacionViviendasSNU` ("Viviendas susceptibles de minimización (1976-2014)"). Via WFS geeft deze in Xàbia **585 percelen** (type D 389 / R 196; klasse SNU-C 512, SNU-P 67, SUZ 6) met velden als `refcat`, `numero_viviendas` en `viviendas_anyo`. De betekenis van "D/R" en de juridische status van de laag zijn ONBEKEND. Opname in de laag betekent niet dat een woning illegaal is, en ontbreken betekent niet dat ze legaal is (bewijstype 4). Geen van de testpunten P1–P3 ligt in deze laag.

### 2.4 Vergunning, declaración responsable en stilzwijgen

- **Art. 232**: vergunningplichtig zijn o.a. nieuwbouw, grondverzet, splitsingen, prefab-woningen en ingrepen met erfgoedbelang.
- **Art. 233.1**: declaración responsable (DR) voor o.a. verbouwing zonder vervanging van hoofdconstructie, "mera reforma", niet-dragende muren en afrastering, eerste en volgende ingebruikname. **Art. 233.2**: DR **met certificaat** van een ECUV of beroepsvereniging voor constructieve verbouwing, sloop en gebruikswijziging. Let op: dit geldt niet voor beschermde gebouwen of omgevingen (233.1.a en c).
- **Art. 240**: termijnen: splitsing 1 maand, nieuwbouw of sloop 2 maanden, ingrepen in beschermde gebouwen 3 maanden, overige 2 maanden.
- **Art. 242.1** (versie Ley 3/2026): positief stilzwijgen alleen "en los supuestos del artículo 233.2.a), c), d) y g)" en bij PIA's; **alle overige vergunningen: negatief stilzwijgen** (242.2).
- **Art. 245**: nutsbedrijven (water, elektriciteit, gas, telecom) mogen alleen leveren tegen overlegging van de ruimtelijke en milieuvergunningen, en moeten levering stopzetten bij een stilleggingsbevel. Een aansluiting bewijst dus niets over legaliteit, en het ontbreken ervan kan juist een signaal zijn.

### 2.5 Cédula de garantía urbanística en schriftelijke informatie

- **Art. 246.1**: de gemeente geeft binnen **1 maand** een cédula af voor bebouwbare percelen, met zonering en classificatie. Geldigheid **maximaal 1 jaar**.
- **Art. 246.2**: bij een planwijziging binnen die termijn heeft de eigenaar recht op schadevergoeding, mits er geen openstaande afstands-, verevenings- of urbanisatieplichten zijn en dat op de cédula staat.
- **Art. 246.3**: de afgifte wordt opgeschort bij een opschorting van vergunningverlening.
- **Art. 246.4**: de gemeente moet op schriftelijk verzoek binnen 1 maand informeren over zonering, classificatie en programmering.

Voor de Deal Hunter is de cédula het instrument om de planologische status **schriftelijk** vast te leggen vóór een bod (⏸️ ACTIE VOOR JAN in §12).

### 2.6 Lokale planstatus in Xàbia (raakvlak met R12)

- In het GVA-planregister voor Xàbia staat de map "03082-0000 NUTU Xàbia" met het **Acuerdo del Consell van 10-09-2021** (normas urbanísticas transitorias de urgencia, [2021/9311]).
  - Het laatst vastgestelde PGOU dateert van 31-01-1990 (BOP 26-02-1990).
  - De NTU gelden "hasta la aprobación del Plan General Estructural", maar "la suspensión finalizará una vez hayan transcurrido cuatro años" na het Acuerdo van 05-03-2021 (DOGV 15-03-2021), dus rond 15-03-2025.
  - **Huidige status (verlengd, vervallen of vervangen door het PGE) is ONBEKEND.** Te verifiëren in R12 of bij het Ajuntament (bewijstype 2 voor de tekst, 7 voor de huidige status).
- NTU-norm 2 (oude kern, NHT zona A): elke ingreep met erfgoedbelang vraagt **voorafgaande toestemming van de cultuurconselleria**, met negatief stilzwijgen na 3 maanden. Verder: historische verkaveling en rooilijnen behouden, gevels van vóór 1940 behouden, nieuwbouw maximaal begane grond + 1, geen nieuwe semi-kelders (bewijstype 2).
- De GVA-planmozaïek (`0702_Planeamiento`, laag `Planeamiento.Clasificacion`) geeft op **P1**: SU / ZUR-RE "Zona urbanizada residencial" (Plan general). Het inventaris zegt "ARENAL-PLAYAS, ARENAL-1B-I", goedgekeurd 31-01-1990, TRLS1976.
- Op **P2**: SNU-P / ZRP-NA-MU "Zona rural protegida municipal (forestal, paisajística, medioambiental)".
- Op **P3**: SUZ / ZND-RE "PLAN PARCIAL ERMITA II", terwijl het grondinventaris "Plan Parcial Montgó-2 / SUP Montgó-2" noemt (PAI toegewezen, reparcelación goedgekeurd). **Tegenstrijdig tussen twee GVA-lagen (bewijstype 7).**

### 2.7 Interpretatiewaarschuwingen TRLOTUP

- De planmozaïek van de GVA vertaalt een PGOU uit 1990 naar LOTUP-codes. Een code als "SNU-C ZRC-FO" zegt niets over de werkelijke regels in de oude normas; dat blijft een gemeentelijke vraag.
- Art. 211.1.b regelt **nieuwe** woningen. Voor bestaande woningen in SNU gelden de minimización-, fuera de ordenación- en DT 26-routes.
- Art. 255.5 schrapt de verjaring in SNU. Of dit ook geldt voor gebouwen die al vóór de invoering van deze regel "verjaard" waren, is een juridische vraag (art. 255.6 verwijst naar de wet op het moment van voltooiing) → **bevoegd advocaat** (bewijstype 7).

---

## 3. PATRICOVA — overstromingsrisico (opdracht b)

### 3.1 Juridische werking (Decreto 201/2015, normativa; bewijstype 2)

- **Art. 3.1**: "Los particulares, al igual que la Administración, están obligados al cumplimiento". **Bindend** zijn de Planos de Ordenación en de Normativa. Het catalogus van maatregelen is indicatief. Bij tegenstrijdigheid gaat de tekst voor de kaart.
- **Art. 4.1**: onbepaalde geldigheid.
- **Art. 7 / 10**: de kaarten van de stroomgebiedsdistricten en die van de Generalitat zijn complementair. Bij equivalentie geldt het **voorzorgsbeginsel** (zwaarste waterdiepte-interval, langste herhalingstijd, art. 10.2). Bij tegenstrijdige studies gaat de gedetailleerdere schaal voor (art. 10.3).

| Niveau | Herhalingstijd | Waterdiepte | SNU (art. 18) | SUZ zonder PAI (art. 19) | SU en SUZ met PAI (art. 20) |
|---|---|---|---|---|---|
| 1 | < 25 jaar | > 0,8 m | geen herclassificatie (18.1); **niveau 1 staat niet in de verbodslijst van 18.2** — interpretatievraag | inundabiliteitsstudie vóór programmering | gemeente legt eisen op met bijlage I "como referencia" |
| 2 | 25–100 | > 0,8 m | **woningen verboden** (en veehouderij, tankstations, industrie, hotels, campings, strategische voorzieningen…) | idem | idem |
| 3 | < 25 | 0,15–0,8 m | idem verbod | idem | idem + extra eisen bijlage I-B |
| 4 | 25–100 | 0,15–0,8 m | idem verbod | idem | idem + bijlage I-B |
| 5 | 100–500 | > 0,8 m | idem verbod | idem | idem |
| 6 | 100–500 | 0,15–0,8 m | woningen en hotels **toegestaan** met aanpassing bijlage I (18.3) | idem | idem + bijlage I-B |
| Geomorfologisch | — | — | verbod zoals 18.2; ontheffing mogelijk met specifieke studie (18.4) | idem | idem |

- **Bijlage I-A** (alle zones): bij waterdiepte > 0,8 m een binnentrap naar het dak; nieuwbouw in stroomrichting; begane-grondvloer boven straatniveau. Wonen, industrie en handel onder maaiveld verboden (behalve opslag).
- **Bijlage I-B** (niveaus 3, 4, 6): geen kelder of semi-kelder, behalve bij intensief wonen onder strikte voorwaarden (alleen parkeren, waterdicht tot 1 m, pomp met aggregaat…). Begane grond **80 cm** boven straatniveau (vrijstelling mogelijk in geconsolideerd stedelijk gebied). Gevel waterdicht tot 1,5 m. Meterkast 70 cm boven de vloer. Afrastering waterdoorlatend boven 30 cm. Constructie berekend op 1,5 m waterdruk (T100).
- **Xàbia staat niet** in de lijst van gemeenten met "elevada peligrosidad" (DA 1ª/2ª); er bestaat een register per besluit. In de normtekst is Xàbia niet genoemd; het register zelf is niet ingezien → [te verifiëren].

### 3.2 Waar te bevragen (getest)

| Dienst | Eindpunt | Lagen | Bewijstype |
|---|---|---|---|
| ICV WMS/WFS Infraestructura Verde | `https://terramapas.icv.gva.es/0701_InfraestructuraVerde` | `IVR.Inundacion` (peligrosidad; GFI-formaten text/html, **geojson**, gml, text/plain; CRS o.a. EPSG:4326/25830/3857) | 3 |
| ICV ArcGIS REST "Ordenación territorial" | `https://carto.icv.gva.es/arcgis/rest/services/tm_infraestructuras/ordenacion_territorial/MapServer` | 1 Estudios de inundabilidad · 3 Red de cauces · 4–9 Peligrosidad 1–6 · 10 Geomorfológica · 12 Riesgo de inundación · (36–101 PATIVEL) | 3 |
| Visor | `https://visor.gva.es/visor/` (lagen `Ordenacion_Territorial;1…12`) | — | 2 |
| Normativa (pdf) | `https://mediambient.gva.es/documents/20551069/162377494/02+Normativa.pdf/5d2bca03-0f7f-4774-b602-4447cfb8dce7` | — | 2 |

**Puntbevraging (werkend recept):**
`…/0701_InfraestructuraVerde?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetFeatureInfo&LAYERS=IVR.Inundacion&QUERY_LAYERS=IVR.Inundacion&CRS=EPSG:4326&BBOX={lat-0.0005},{lon-0.0005},{lat+0.0005},{lon+0.0005}&WIDTH=101&HEIGHT=101&I=50&J=50&INFO_FORMAT=geojson`
Let op de volgorde lat,lon bij WMS 1.3.0 + EPSG:4326. Een alternatief is ArcGIS `identify` of `query` met een puntgeometrie.

### 3.3 Testresultaten

| Punt | PATRICOVA | Details | Bewijstype |
|---|---|---|---|
| **P1 Arenal** | **Niveau 4** | codigo AC07, zona "Riu de Xaló o de Gorgos", tipo INTERCUENCA (Algar↔Gorgos), T = 100, calado < 0,8 m; polygoon 95,29 ha. Laag 12 "Riesgo": "Medio" | 3 |
| **P2 Granadella** | geen zone | — | 3 |
| P3 Montgó-flank | geen zone | — | 3 |
| T l'Arenal (partida en urbanització) | Niveau 4 | AC07, T100, < 0,8 m | 3 |
| T el Saladar | **Niveau 3** | AC08 "Barranco del Tosalet", T25, < 0,8 m | 3 |
| T les Duanes de la Mar | Geomorfologisch | "Abanicos torrenciales", 41,9 ha | 3 |
| T el Pou del Moro | **Niveau 5** | AC07, T500, > 0,8 m | 3 |
| T Camí del Riu Gorgos | Niveau 4 | AC07 tipo RIO (Gorgos→zee) | 3 |
| T el Pla d'en Roca | Niveau 5 | AC07 RIO, T500, > 0,8 m | 3 |
| T el Portitxol, el Muntanyar de Baix, Plana de la Guàrdia | geen zone | — | 3 |

### 3.4 Welke delen van Xàbia liggen in een risicozone (officiële laag, 15-09-2026)

Query: ArcGIS `query` per laag (4–10) met de gemeentegrens van Xàbia als polygoon; per polygoon doorsneden met de planmozaïek en de dichtstbijzijnde officiële toponiemen.

| Niveau | Polygonen | ≈ ha in Xàbia (5) | Waar (dichtstbijzijnde NTV-toponiemen) | Planklasse (aandeel rasterpunten) |
|---|---|---|---|---|
| 1 | 1 (Gorgos) | 53 | les Senioles, el Pla d'en Roca (Gorgos-vallei landinwaarts) | SNU-P 69 % (vooral ZRP-CA "cauces"), SNU-C 25 % |
| 2 | 3 | 56 | les Comunes, la Fontana, els Benvinguts; grootste polygoon (466 ha) ligt vooral stroomopwaarts buiten Xàbia | SNU-C 74 % |
| 3 | 3 | 74 | **el Saladar/el Muntanyar de Baix (AC08 Tosalet, 29,8 ha, vrijwel geheel SUZ)**; el Planet (Gorgos, 41,7 ha); klein vlak bij l'Arenal/Punta de la Fontana (2,9 ha) | SNU-C 53 %, SUZ 41 % |
| 4 | 6 | 352 | **l'Arenal (95,3 ha)**; tussen dorp en haven (Freginal/Jovades, 72 + 93 ha, inclusief PP "Pou del Moro-1" en industriegebied); Muntanyar de Dalt/la Fontana (71,9 ha) | SUZ 38 %, SNU-C 35 %, **SU 25 %** |
| 5 | 5 | 187 | **el Pou del Moro (120 ha)**, les Comunes, les Senioles, la Riba | SNU-C 93 % |
| 6 | 2 | 98 | **el Salobre/l'Arenal (74,4 ha, inclusief "Homologación y PP SUP Saladar 2")**; **rand van de oude kern bij het gezondheidscentrum en het Convent dels Dominics (24,6 ha, inclusief ZUR-NHT)** | SU 39 %, SUZ 37 % |
| Geomorfologisch | 26 | ≈ 382 | vaguadas y barrancos (239 ha), abanicos torrenciales (65 ha, o.a. Duanes/haven), llanura aluvial (37 ha, o.a. kustvlakte SU/SUZ), cauces (32 ha), humedales (9 ha) | SNU-C 39 %, SU 33 %, SUZ 22 % |

- **Totaal niveau 1–6 ≈ 820 ha ≈ 12 % van de gemeente** (bewijstype 5; aannames in §0).
- **Gorgos-monding:** de vlakken van niveau 4 (72 ha, lon tot ±0,178) en de geomorfologische vlakken reiken tot de Duanes en de Muntanyar. De monding zelf is niet apart als punt bevraagd → [te verifiëren met de kaart].
- **Estudio de inundabilidad** in Xàbia (laag 1): expediente 2020/114 "ESTUDIO DE INUNDABILIDAD AREA RIOG ROQUETES1 RR1", goedgekeurd op 21-01-2021 (tijdstempel; datumconversie bewijstype 4), punt ±38,7918 / 0,1711. Zo'n studie kan de PATRICOVA-afbakening lokaal verfijnen (art. 11–13).

### 3.5 SNCZI/ARPSI als kruiscontrole — en een tegenstrijdigheid

- De MITECO-WMS voor SNCZI (`https://wms.mapama.gob.es/sig/agua/ZI_LaminasQ100` e.a., genoemd in de officiële MITECO-catalogus) gaven op 15-09-2026 een ServiceException ("NullReferenceException"). De nieuwe viewer `https://gis.miteco.gob.es/web/snczi` gaf een verbindingsreset (curl) of 503 (WebFetch). **Niet getest.**
- **Werkend alternatief:** IDEE `https://servicios.idee.es/wms-inspire/riesgos-naturales/inundaciones` — ARPSI-gevaarkaarten (RD 903/2010), lagen `NZ.Flood.FluvialT10/T100/T500`, `NZ.Flood.MarinaT100/T500`, `EL.GridCoverage` (MDT LiDAR). Voorwaarde: vrij gebruik met vermelding van MITECO.

| Punt | Fluvial T10 | T100 | T500 | Marina T100/T500 |
|---|---|---|---|---|
| P1 Arenal | 0,073 | **1,951** | 2,466 | −9999 |
| T l'Arenal (partida) | 0,733 | 1,705 | 2,245 | −9999 |
| P2 Granadella | 999 | 999 | 999 | −9999 |

- **Eenheid en betekenis van de rasterwaarden (`GRAY_INDEX`) staan niet in de capabilities of metadata die we zagen.** Vermoedelijk waterdiepte in meters en "999" = buiten het ARPSI-studiegebied [te verifiëren] (bewijstype 7).
- **Tegenstrijdigheid:** PATRICOVA noemt P1 "calado < 0,8 m bij T100"; de ARPSI-waarde bij T100 is 1,95 (als dat meters zijn). Volgens PATRICOVA art. 7 en 10.2 zijn beide kaarten complementair en geldt het voorzorgsbeginsel. **Geen conclusie forceren:** voorleggen aan een hydraulisch ingenieur of de gemeente (masterprompt §15). De bevoegde stroomgebiedsbeheerder is naar verwachting de Confederación Hidrográfica del Júcar [te verifiëren].

### 3.6 Waarschuwingen PATRICOVA

- De kaartlaag is de officiële afbakening, maar lokale inundabiliteitsstudies kunnen die wijzigen (art. 8.2, 11–13). Controleer laag 1.
- De eisen van bijlage I voor SU zijn "referencia" (art. 20). Of Xàbia ze oplegt, bepaalt de gemeente per vergunning.
- Niveau 1 ontbreekt letterlijk in art. 18.2 (SNU-verbod). Niveau 1 valt in de praktijk vaak samen met bedding en afvoerzone (ZRP-CA), maar dat is een interpretatievraag, geen vrijbrief.
- Laag 12 "Riesgo" is een risicoproduct (gevaar × kwetsbaarheid, art. 10). Het visor meldt bij een andere risicolaag ("Riesgos.Inundaciones"): "La cartografía del riesgo de inundación no está vigente, usar la del PATRICOVA." Gebruik voor beslissingen de gevaarlagen (4–10).

---

## 4. Bos, brand en natuur: PATFOR, brandpreventie, Montgó, Red Natura, microreservaten, Cap de la Nau–Granadella (opdracht c)

### 4.1 PATFOR (Decreto 58/2013, DOGV 7019, 08-05-2013; bewijstype 2)

- **Art. 28.1**: in bosterrein zijn werken en gebruik toegestaan die de stedenbouwwetgeving voor SNU (común of protegido) toelaat. **28.3**: herstel van bestaande gebouwen die herkenbaar zijn, met een **brandpreventieplan door een universitair opgeleide bostechnicus**.
- **Art. 29**: extra toegestane gebruiksvormen in "terreno forestal estratégico" (beheer, recreatie, biomassa).
- **Art. 30.1**: voor het verplichte bosadvies (Ley 3/1993 art. 62) is een brandpreventieplan verplicht. Let op: het artikel verwijst nog naar de ingetrokken Ley 10/2004 del Suelo No Urbanizable (bewijstype 4).
- **Art. 32**: interface stedelijk gebied–bos: onderbreking van minimaal 25 m plus een weg van 5 m (≥ 50 m bij helling > 30 %). **Geïsoleerde woningen: verdedigingsstrook ≥ 30 m** (≥ 50 m bij > 30 % helling), voor rekening van de eigenaar. Stedelijk gebied < 100 m van bos: boomkroondekking < 40 %, struiken < 10 %, snoeien, 3 m afstand tussen takken en gebouwen.
- **Geldigheid of wijzigingen na 2013** niet gecontroleerd → [te verifiëren].

**Laag:** `https://terramapas.icv.gva.es/0506_PATFOR` (WMS/WFS, CC BY 4.0). Lagen o.a. `SF.Forestal`, `Forestal.Forestal`, `Forestal.Estrategico`, `Planeamiento.TFE`, `Regulacion.Incendios.Urbano` (interface), `Regulacion.Incendios.Peligrosidad`, `Regulacion.Incendios.Riesgo` (niet bevraagbaar).

| Punt | Terreno forestal | TFE | Interface bos-bebouwing | Peligrosidad | Bewijstype |
|---|---|---|---|---|---|
| P1 | nee | nee | "1 – Sin interfaz" | klasse leeg | 3 |
| P2 | **ja (FORESTAL)** | **ja (PRODUCTIVIDAD)** | **"4 – Alta"** | "Moderado" | 3 |
| P3 | nee | nee | "2 – Casos aislados" | klasse leeg | 3 |

Waarschuwing: de interfacelaag is een raster. GFI gaf celcentra terug (P2-cel 38,7269 / 0,1911, ±500 m van het punt), dus dit is **geen perceelsoordeel** (bewijstype 3/4).

### 4.2 Brandpreventie (TRLOTUP DA 7 + bijlage XI; PLPIF; PPIF Montgó)

- **TRLOTUP DA 7** (bewijstype 2): gemeenten met bosgrond bakenen urbanisaties, kernen en gebouwen in bos of in de invloedszone af (Ley 3/1993 art. 57). Na goedkeuring door de gemeenteraad hebben de verplichten **6 maanden** om aan **bijlage XI** te voldoen (DA 7.10). Eigenaren zijn hoofdelijk aansprakelijk (DA 7.3). Er geldt een gedwongen erfdienstbaarheid van toegang (DA 7.7–8).
- **Bijlage XI** (bewijstype 2): omtrekstrook van minimaal 30 m; geïsoleerde gebouwen een verdedigingszone van ≥ 30 m, afhankelijk van de helling; zelfbeschermingsplannen.
- **Xàbia (ICV ArcGIS `prevencion_de_incendios`, getest, bewijstype 3):**
  - Laag 114 "Municipios interfaz": Jávea/Xàbia, estado **"Aprobado"**, `fechapleno` **2026-05-28**, `acplenario` "03082_Xàbia". De inhoudelijke Xàbia-cartografie (lagen 112/113) staat **niet** in de dienst; daar alleen Dénia → [te verifiëren bij het Ajuntament].
  - Laag 123 "Estado PLPIF": **plan local de prevención de incendios forestales goedgekeurd**, resolución 2020/6092 van 21-07-2020 (DOGV 29-07-2020), "15 años con revisión parcial cada 5 años". De DOGV-tekst is bevestigd: "Con carácter general el plan tiene una vigencia de quince años" (bewijstype 2).
  - Laag 127 "Fajas perimetrales": 61 stroken in Xàbia (±116,9 km), type "Banda perimetral áreas urbanizadas MANTENIMIENTO".
  - **P3** ligt in de **ZIF 500 m** (zona de influencia forestal) en in het ámbito van het **PPIF van het Parque Natural del Montgó** (resolución 2006/7461, 04-06-2006, DOCV 5299; "Aprobada revisión en 2020", "Revisión 2019-2029").
  - **P2** ligt binnen de branduitbreiding van **2000** (paraje "BCO. GRANADELLA", Xàbia) en **2016** (Cumbres del Sol, geregistreerd onder Benitatxell). **P4** ligt binnen de brand van 1999 ("LAS PLANAS").
- **TRLOTUP art. 7.4** (bewijstype 2): afgebrande bosgrond mag **30 jaar** niet naar SU/SUZ worden geherclassificeerd.

### 4.3 Parque Natural del Montgó, PORN/PRUG en de "área de amortiguación de impactos"

**Instrumenten** (parquesnaturales.gva.es, bewijstype 2):
- Decreto 25/1987 (instelling), gewijzigd door Decreto 110/1992.
- **PORN: Decreto 180/2002, 5-11 (DOGV 4374, 08-11-2002)**.
- **PRUG: Decreto 229/2007, 23-11**.
- Reserva marina Cap de Sant Antoni: Decreto 212/1993, gewijzigd door 110/2005; regeling Decreto 19/2015.
- PPIF: Resolución 04-06-2006, herzien 09-09-2020.

**Wettelijk kader:** Ley 11/1994 ENP art. 29 — áreas de amortiguación de impactos met regeling van gebruik, milieueffectbeoordeling of bindend advies van de parkbeheerder. **DA 6ª** stelt een amortiguación-gebied in rond het Montgó-park, "La delimitación y el régimen … son los establecidos … en los anexos normativos" van Decreto 180/2002 (bewijstype 2). Buiten het park geldt wat het PORN bepaalt (art. 33).

**PORN Montgó, bouwgerelateerde bepalingen** (bewijstype 2, Spaanse kolom van de DOGV):

| Artikel | Regel |
|---|---|
| 12 | Onbepaalde geldigheid tot herziening |
| 36.1 | SNU in de amortiguación-zone **moet SNU blijven**; bij planwijzigingen en DIC's is een **voorafgaand bindend rapport** van de Conselleria nodig |
| 55 | Het park is SNU van bijzondere bescherming. "Conectores ecológicos" in de amortiguación-zone: SNU van bijzondere bescherming. "Áreas naturales" idem, behalve bestaand SU/SUZ (→ SNU común). Overige zones behouden de classificatie uit het PGOU |
| **56.1** | "se prohibe la construcción de nuevas edificaciones dentro del Parque Natural", behalve voor beheer of publiek gebruik |
| **56.2–3** | Zona de Uso Especial **Les Planes**: plan especial vereist; "la parcela mínima … no podrá ser menor de diez mil metros cuadrados", splitsen verboden; tot goedkeuring **geen nieuwbouw** |
| **57** | SNU in de amortiguación-zone: verbouwing en remodellering van woningen alleen "en la medida en que no involucren un incremento apreciable en la superficie construida" en zonder negatieve effecten |
| 71 | Zonering: A.1 Park (Uso Restringido/Moderado/Especial), A.2 Reserva marina, B. Áreas periféricas de amortiguación (B.1 Conectores, B.2 Áreas naturales, B.3 Agrícolas, **B.4 Urbanas y urbanizables**, B.5 Expansión urbana preferente, B.6 Revisión de titularidad) |
| **109** | B.4 = "las urbanizaciones de las laderas del Montgó" en de randen van Dénia en Jávea: gebruik volgens het PGOU. Een **verplicht rapport** over deelplannen van SUZ (dichtheid, volume, gevelmaterialen, afrastering, zwembaden/garages, verlichting…). **109.5**: voorafgaand rapport van de Conselleria voor o.a. "(f) Cualquier actividad que implique movimiento de tierras o remodelación topográfica", nieuwe wateronttrekkingen, bovengrondse leidingen en rioolaansluitingen |

**Laag (getest):** `https://terramapas.icv.gva.es/0505_PORN`, lagen `Montgo.PORN` (ámbito, 7.432,85 ha, gemeenten Dénia, Gata de Gorgos, Xàbia, Ondara, Pedreguer), `Montgo.Zonificacion`, `Montgo.ZonificacionSantAntoni`, `Montgo.Parque`. Het visor meldt: "La delimitación aquí reflejada de los ámbitos de PORN, tiene carácter informativo" (bewijstype 2).

| Punt | PORN-ámbito | PORN-zone | Park | Bewijstype |
|---|---|---|---|---|
| P1 Arenal | nee | — | nee | 3 |
| **P3 Montgó-flank (K07)** | **ja** | **"Áreas urbanas y urbanizables"** (art. 109) | nee | 3 |
| P4 (in het park) | ja | "Uso Moderado" | ja (+ LIC ES5211007 "Montgó", ZEPA ES0000454 "Montgó - Cap de Sant Antoni", PRR 24 "El Montgó") | 3 |
| T les Duanes (haven) | ja | "Áreas urbanas y urbanizables" | nee | 3 |

**Gevolg voor de Montgó-flank (bewijstype 4):** in de urbanisaties op de flank (Garroferal, Montgó-Ermita, La Corona) geldt het PGOU, maar grondverzet, zwembaden en nieuwe aansluitingen vragen een extra rapport van de Conselleria (art. 109). Bij SUZ-deelplannen legt de Conselleria voorwaarden op. Reken op extra doorlooptijd; de omvang is ONBEKEND.

**Reserva natural marina Cap de Sant Antoni:** een mariene reserve, relevant voor zeegebruik, niet voor bouwen op land (bewijstype 4). Het PORN rekent de reserve tot het ámbito (art. 4).

### 4.4 Red Natura 2000 in Xàbia (ICV WFS/ArcGIS, getest)

| Gebied | Code | Instrument | In Xàbia | Testpunt |
|---|---|---|---|---|
| **ZEC Penya-segats de la Marina** | ES5213018 | **Decreto 197/2022, 18-11** (DOGV 28-11-2022): verklaring als ZEC + **norma de gestión** + grenswijziging; 952,6 ha (Xàbia, Benitatxell, Teulada) | ja | **P2: ZEC + ZEPA + LIC, zone B** (ArcGIS laag 21 "Zonificación Norma Gestión": zone B 787,17 ha) |
| ZEPA Penya-segats de la Marina | ES5213018 | aangewezen DOCV 6031 (09-06-2009) | ja | P2 |
| LIC Montgó | ES5211007 | lijst 22-07-1992, correctie DOCV 7262 (28-04-2014) | ja | P4 |
| ZEPA Montgó - Cap de Sant Antoni | ES0000454 | DOCV 6031 (09-06-2009) | ja | P4 |

- De laag `IVR.ZEC` toonde voor Montgó **geen** ZEC-verklaring (alleen LIC) → of Montgó al als ZEC is aangewezen: ONBEKEND.
- **Norma de gestión Penya-segats** (bewijstype 2, tekst gelezen; kolomtabellen niet betrouwbaar uitgelezen → pagina 63–64 van de pdf zelf lezen):
  - **Zona A**: habitats met bijzondere prioriteit. Hier zijn "incompatibles" o.a. nieuwe vrijstaande eengezinswoningen in SNU "con cualquier calificación" en de "reconstrucción o remodelación … cuando supongan un incremento de la superficie o volumen" (§5.2.1, 4).
  - **Zona B**: habitats van communautair belang (o.a. 9540 pinares, 5330 matorrales).
  - **Zona C**: vogel- en florasoorten.
  - **Zona D**: overige, waaronder SU/SUZ.
  - Voor A, B en C: gebruik strijdig met de classificatie is incompatibel (§5.2.3).
  - Evaluatie van effecten op Red Natura 2000 (Decreto 60/2012) geldt voor het hele gebied; woningbouw en uitbreiding in SNU staan expliciet op de lijst van projecten die beoordeeld moeten worden (§5.3).

### 4.5 Microreservaten voor flora in Xàbia (0502_Biodiversidad WFS, getest; bewijstype 3)

| Microreservaat | ha (officieel) | Besluit (link in laag) |
|---|---|---|
| Cova del Llop Marí | 6,44 | DOGV 03-11-2005 |
| Illot de la Mona | 0,068 | DOGV 10-03-2003 |
| Cap de la Nau | 1,45 | DOGV 24-04-2020 |
| Cap de Sant Antoni | 2,92 | DOGV 24-04-2020 |
| La Granadella | 0,74 | DOGV 24-04-2020 |
| Platja de la Barraca (Portitxol) | 0,842 | DOGV 07-11-2025 |

Geen microreservaat op P1, P2 of P3. Geen fauna-reserves, beschermde landschappen of parajes naturales municipales in de bbox.

### 4.6 Bossen (montes) in Xàbia

- Laag `IVR.Montes` ("Montes Catalogados"): **LA GRANADELLA** (hoofdvlak 645,1 ha), **MONTGÓ I** (215 ha), **LA PLANA DE SAN JERÓNIMO DE JUSTA** (±134–135 ha, meerdere vlakken).
- De ArcGIS-laag "Montes gestionados por la Conselleria" op P4 zegt echter voor AL3039: "Catalogado de Utilidad Pública: NO". **De twee lagen spreken elkaar tegen** over het "gecatalogiseerd" zijn (bewijstype 7).
- TRLOTUP art. 5.4: een gecatalogiseerd publiek bos in de eerste 10 km vanaf de kust staat alleen verenigbaar gebruik toe.

### 4.7 Cap de la Nau – Granadella: stapeling van beschermingen

1. ZEC/ZEPA Penya-segats de la Marina (Decreto 197/2022) met zonering A–D.
2. Microreservaten Cap de la Nau en La Granadella.
3. Bos "La Granadella" en PATFOR TFE/bosgrond.
4. Brandinterface "Alta" en brandhistorie 2000/2016 (art. 7.4: 30 jaar).
5. PATIVEL Litoral 1/2 rond el Portitxol en Cap Negre (§5).
6. Catálogo de playas-tramo "Xabia_6_Benitaxell_Teulada_1" (N1, natuurlijk; o.a. Cap Martí, Portitxol, Granadella).
7. BIC Torre La Granadella en Torre d'Ambolo; BIC-archeologische zone "Yacimiento romano Illeta del Portichol".
8. PGOU: SNU-P ZRP-NA-MU (P2).

Alles bewijstype 3 (lagen) en 2 (besluiten).

---

## 5. PATIVEL en de nieuwe kustwet (opdracht d)

### 5.1 Juridische status (gedateerde officiële bronnen)

| Datum | Gebeurtenis | Bron | Bewijstype |
|---|---|---|---|
| 04-05-2018 | **Decreto 58/2018** keurt PATIVEL + Catálogo de Playas goed (DOGV 8293, 11-05-2018). Jávea staat in de lijst van betrokken gemeenten (art. 3.3) | GVA-pdf "versión vigente 04.06.2025" | 2 |
| 11-02-2021 | TSJCV **Sentencia 46/2021** verklaart het decreet nietig; GVA-nota: niet onherroepelijk, "la aplicación del PATIVEL … no resulta afectada" | GVA "Nota informativa Sentencia PATIVEL.pdf" | 2 |
| 27-04-2022 | **Tribunal Supremo, Sentencia 491/2022** (casación 4049/2021): "estimar el recurso de casación … interpuesto por la Generalitat Valenciana" tegen TSJCV-sentencia 96/2021 (15-03-2021), die wordt vernietigd; terugverwijzing naar de TSJ voor de overige gronden | GVA "Sentencia TS 27-04-22 PATIVEL.pdf" (gelezen) | 2 |
| 03-06-2025 / 19-06-2025 / 08-05-2026 / 12-05-2026 | Publicatie van de **uitvoering van gedeeltelijke vernietigingen** voor Alcalà de Xivert, El Campello (3×), Moncofa, Peñíscola, San Fulgencio, Torrevieja en Villajoyosa; o.a. DA 1ª (flexibiliteit hotels) vernietigd (PO 120/2018, DOGV 10122) | GVA-map "Ejecucion de sentencias PATIVEL" | 2 |
| 15-06-2025 | **Ley 3/2025 costa valenciana** in werking. DA 1ª: PATIVEL "pasará a denominarse Plan de Ordenación Costera" en moet binnen 3 maanden worden herzien. **DT 2ª**: PATIVEL blijft van kracht voor zover niet strijdig; verboden en vergunningplichtig gebruik uit de wet "son de aplicación directa y prevalecen" | boe.es BOE-A-2025-11647 | 2 |
| 01-12-2025 | Voorafgaande openbare consultatie van het ontwerpdecreet **Plan de Ordenación Costera** | mediambient.gva.es novetats | 2 |
| 26-02 / 25-03-2026; 21-07-2026 | **Recurso de inconstitucionalidad 1550-2026** tegen Ley 3/2025: schorsing van art. 17 en DF 1ª (alleen voor bebouwing die de staatskustwet schendt), en van DA 4ª. **ATC 49/2026** (21-07-2026) handhaaft de schorsing van art. 17 en DF 1ª en heft die van DA 4ª op | boe.es (noten bij de artikelen) | 2 |

**Conclusie (bewijstype 2 + 4):** op 15-09-2026 is PATIVEL (Decreto 58/2018) van kracht, met gedeeltelijke vernietigingen die niet over Xàbia gaan. Voor zover strijdig gaat Ley 3/2025 voor. De vervanger (Plan de Ordenación Costera) is in voorbereiding en **nog geen geldend recht**. Of er nog een TSJCV-procedure loopt die Xàbia raakt: ONBEKEND. De geconsolideerde GVA-versie dateert van 04-06-2025, terwijl de uitvoeringen van mei 2026 daarin nog ontbreken.

### 5.2 Wat PATIVEL regelt (Normativa; bewijstype 2)

- **Art. 3**: strikt ámbito 0–500 m vanaf de binnengrens van de "ribera del mar" (valt samen met de invloedszone van de Ley de Costas); uitgebreid 500–1.000 m; verbinding 1.000–2.000 m. Het plan regelt **grond in de basissituatie landelijk**.
- **Art. 8–9 (Litoral 1, SNU de protección litoral):** blijft landelijk, ongeacht de classificatie (tenzij er een PAI binnen de termijn loopt). **Nieuwbouw verboden**, behalve voor beheer, recreatie of dotaties, landbouwhuisjes < 25 m² op ≥ 5.000 m², kassen enzovoort. Niet op hellingen > 25 %. **Art. 9.5: rehabilitatie en aanpassing van bestaande gebouwen** zijn toegestaan voor wonen, horeca, toerisme enzovoort, mits legaal of via minimización. **Uitbreiding tot 20 % alleen bij beschermde (gecatalogiseerde) gebouwen.** Landschapsstudie en rapporten van de Generalitat verplicht (9.6).
- **Art. 10–11 (Litoral 2, refuerzo):** bovendien hotel- en zorggebruik (bebouwing ≤ 10 %, twee lagen), eco-camping ≤ 20.000 m², tankstations; nooit omzetting naar wonen.
- **Art. 13 (suelo común del litoral, ≤ 1.000 m):** nieuwe SU/SUZ pas als 70 % van het bestaande SU/SUZ in de strook van 1.000 m bebouwd is; geen urbanisatie op hellingen > 25 % (30 % voor sectoren met vrijstaande woningen).

### 5.3 Ley 3/2025 — relevante punten voor aankopen aan de kust (bewijstype 2)

- **Art. 2**: litoraal = strook van 500 m (tot 2.000 m) vanaf de eerste niet door zee bespoelde grond.
- **Art. 23**: zones "protección ambiental", "mejora ambiental y paisajística" en "reordenación" (worden door het Plan de Ordenación Costera toegewezen).
- **Art. 44**: bouwen of gebruik in de **servidumbre de protección** vraagt voorafgaande **toestemming van de Generalitat**. **Art. 45**: bij een gemeentelijke bouwvergunning wordt dat een **bindend rapport** (termijn maximaal 6 maanden).
- **Art. 51**: voorkoops- en terugkooprecht van de Generalitat mogelijk in beschermings- en verbeteringsgebieden (melding binnen 60 dagen na de notariële akte; retracto 6 maanden). **Voor de Deal Hunter een due-diligencepunt zodra het Plan de Ordenación Costera zulke gebieden afbakent** (bewijstype 4).
- **DA 3ª**: gemeenten moeten binnen 3 jaar gronden ≤ 200 m van de kust aanwijzen die in 1988 feitelijk stedelijk waren (van belang voor de 20 m-regel, §6).

### 5.4 Wat PATIVEL betekent voor de kust van Xàbia (lagen getest, 15-09-2026)

- **Litoral 1 en 2 in Xàbia** (ArcGIS laag 34, doorsneden met de gemeentegrens; bewijstype 3/5):

| Categorie | ≈ ha in Xàbia | Waar (NTV) | Planklasse |
|---|---|---|---|
| Litoral 1 (object 16) | 49 | **el Portitxol** (partida, zwaartepunt 38,7576 / 0,2153) | SNU-P ZRP-NA-LG "PAT INFRAESTRUCTURA VERDA" |
| Litoral 1 (object 15) | 7,9 | Racó del Cap Negre / Carretera del Cap de la Nau | idem (+ rand PP "El Cabo") |
| Litoral 1 (object 14) | ±2 | grens met Benitatxell (vlak van 253 ha vooral buiten Xàbia) | idem |
| Litoral 2 (object 68) | 5,8 | el Portitxol (T-punt valt erin) | idem |
| Litoral 2 (object 69) | 4,0 | Plana de la Guàrdia / Cap Negre | idem |

- **Catálogo de playas** (laag 33):
  - Xabia_2 "La Grava, Muntanyar" (U1, stedelijk)
  - Xabia_3 "Muntanyar" (N2)
  - **Xabia_4 "El Arenal" (U1)**
  - Xabia_5 "Segundo Montañar, Primera y Segunda Caletas" (N2)
  - Denia_11_Xabia_1 "Les Rotes, Pope (Tango)" (N1, Silene hifacensis)
  - Xabia_6_Benitaxell_Teulada_1 "Cap Martí, Portitxol, Granadella…" (N1, vleermuisreserve)
- **Interpretatiewaarschuwing (bewijstype 3):** de lagen "Ámbito estricto/ampliado/conexión" (32/30/31) zijn **polylijnen** (grenslijnen op 500, 1.000 en 2.000 m), geen vlakken. Een punt-in-polygoon-test geeft **altijd 0**. Werkende methode: afstand tot de lijn (ArcGIS `query` met `distance`).
  - **P1** ligt ±416 m van de 500 m-lijn, 920 m van de 1.000 m-lijn en 1.916 m van de 2.000 m-lijn → P1 ligt **binnen het strikte ámbito**, ±80 m van de door PATIVEL gebruikte ribera. Waarschijnlijk is dat het **Canal de la Fontana** (NTV "Canal", 154 m) en niet het strand (404 m) (bewijstype 5/4). P1 is SU; PATIVEL regelt vooral landelijke grond, maar de kustbeperkingen van §6 kunnen gelden [te verifiëren met de deslinde].
  - **P2** ligt ±223 m van de 500 m-lijn → ±277 m van de ribera, binnen het strikte ámbito. Categorie hier: SNU-P binnen de ZEC (art. 6 "suelos litorales de protección ambiental" → eigen natuurregeling; bewijstype 4).

---

## 6. Ley de Costas en waterstaatsdomein (opdracht e)

### 6.1 Ley 22/1988 de Costas (boe.es, geconsolideerd tot 11-12-2015; bewijstype 2)

| Onderwerp | Regel |
|---|---|
| Servidumbre de protección (art. 23) | **100 m** landinwaarts vanaf de binnengrens van de ribera del mar; uit te breiden tot +100 m; bij rivieren met getijde-invloed te verkleinen tot 20 m (23.3, Ley 2/2013) |
| Verboden in de servidumbre (art. 25.1) | "a) Las edificaciones destinadas a residencia o habitación"; interurbane wegen; hoogspanningsleidingen; reclame enzovoort. Toegestaan zijn alleen gebruiksvormen die nergens anders kunnen of die het DPMT dienen, plus onoverdekte sportvoorzieningen (25.2) |
| Eerste 20 m (art. 24.2) | tijdelijke opslag en reddingswerk; geen afsluitingen, behoudens reglement |
| Servidumbre de tránsito (art. 27) | **6 m** vanaf de ribera, altijd vrij voor voetgangers en hulpdiensten; tot 20 m waar het doorkomen moeilijk is |
| Zona de influencia (art. 30) | minimaal **500 m**: parkeerreserves; geen "pantallas arquitectónicas"; dichtheid ≤ gemiddelde van het programmeerbare SUZ in de gemeente |
| **DT 3ª.3** | Grond die op 29-07-1988 **stedelijk** was: servidumbre de protección **20 m**, met bestaande rechten volgens DT 4ª; nieuwe woningen alleen onder strikte voorwaarden (homogenisering van de zeefront, gesloten bebouwing, ≤ 25 % van de gevellengte) |
| DT 3ª.1–2 | SNU of niet-geprogrammeerd SUZ in 1988: volledige 100 m. Geprogrammeerd SUZ zonder plan parcial: volledige toepassing |
| **DT 4ª.2.b–c** | Bestaande legale bouw in tránsito of protección: "obras de reparación, mejora, consolidación y modernización siempre que no impliquen aumento de volumen, altura ni superficie". Tránsito: vooraf een gunstig staatsrapport (2 maanden, positief stilzwijgen). **Bij volledige of gedeeltelijke sloop geldt voor nieuwbouw de wet volledig** |
| DT 4ª.3 | Die werken vereisen o.a. een verbetering van het energielabel met twee letters of naar B, en waterbesparing; declaración responsable bij de autonome gemeenschap |

- Uitvoeringsreglement: RD 876/2014 (Reglamento General de Costas) — niet gelezen, [te verifiëren].
- BOE-noot: DT 4ª.2.c van de **oorspronkelijke** tekst is door TC 149/1991 nietig verklaard. De huidige tekst komt van Ley 2/2013 → interpretatievraag voor een jurist (bewijstype 7).
- **Regionale laag erbovenop:** Ley 3/2025 art. 44–45 (toestemming of bindend rapport van de Generalitat in de servidumbre de protección); DT 3ª van die wet: overdracht van beheer van concessies en vergunningen in het DPMT pas na formele overdracht van diensten.

### 6.2 Waterstaatsdomein (Ley de Aguas, RDL 1/2001, geconsolideerd tot 28-12-2023; bewijstype 2)

- **Art. 6.1**: oevers van openbare waterlopen: **servidumbre 5 m** (openbaar gebruik) en **zona de policía 100 m** ("se condicionará el uso del suelo"). Bij monding in zee aanpasbaar (6.2).
- **P2** ligt ±14 m van de "Barranc de Martorell" (NTV) → binnen de 100 m-politiezone als dat een openbare waterloop is [te verifiëren]. Samen met TRLOTUP 211.1.b.3 ("fuera de los cursos naturales de escorrentías") is dat een harde toets voor elk bouwplan (bewijstype 4).
- De MITECO-WMS voor DPH ("DPHCartografico", "DPHDeslindado", "ZI_LaminasZFP") zijn opgenomen in de MITECO-catalogus, maar gaven op 15-09-2026 dezelfde serverfout → niet getest.

### 6.3 Wat betekent dit voor Arenal, haven, Portitxol en Granadella (bewijstype 4, te toetsen)

| Gebied | Kustkader (vermoedelijk) | Wat te checken |
|---|---|---|
| **l'Arenal** | Stedelijk sinds PGOU 1990 (inventaris: ARENAL-PLAYAS 31-01-1990, dus na 1988) → of de grond op **29-07-1988** al stedelijk was bepaalt 20 m of 100 m. Het Canal de la Fontana kan de ribera verleggen (P1-afstandsberekening). Tramo U1 in de Catálogo de playas. Bovendien PATRICOVA P4/P6 | deslinde en servidumbrelijn MITECO; classificatie in 1988 (PGOU van vóór 1990) → R12; bij verbouwing in de servidumbre: DT 4ª (geen volume, energielabel) + Generalitat-rapport (Ley 3/2025) |
| **Puerto / les Duanes** | Stedelijk (NHT-achtige zone rond het havenfront), PORN-ámbito "urbanas", PATRICOVA geomorfologisch, BRL "Refugio del Moll", haven = havendomein (Generalitat of Estado [te verifiëren]) | deslinde en havengebied; eventueel DT 3ª.3 regel 3ª (conjunto histórico) |
| **el Portitxol** | PATIVEL Litoral 1 (49 ha) en Litoral 2 (5,8 ha); SNU-P; BIC Torre del Portitxol en BRL Batería; microreservaat Platja de la Barraca; ZEC-rand | Litoral 1: geen nieuwbouw, rehabilitatie volgens art. 9.5; servidumbre 100 m (SNU in 1988, DT 3ª.1) [te verifiëren]; homologatie PG Portitxol "Anulado" (planregister) → R12 |
| **la Granadella** | SNU-P, ZEC zone B, bos, brand; ribera ±277 m (P2) → buiten de 100 m-servidumbre op P2 zelf (bewijstype 5), wel binnen de zona de influencia (500 m) | deslinde; ZEC-beoordeling; DPH-barranco |

### 6.4 Waar de deslindelijnen van Xàbia te raadplegen zijn — status 15-09-2026

| Route | Adres | Status | Bewijstype |
|---|---|---|---|
| MITECO-viewer DPMT | `https://gis.miteco.gob.es/web/dpmt` (volgens de MITECO-viewerpagina); oude `https://sig.miteco.gob.es/dpmt/` → 301 naar een migratiepagina | **verbindingsreset (curl) / HTTP 503 (WebFetch)** | 3 |
| MITECO WMS DPMT | `https://wms.mapama.gob.es/sig/Costas/DPMT` (+ `/SP`, `/NucleosExcluidos`, `/TerrenosIncluidos`) | **ServiceException NullReferenceException** (alle varianten) | 3 |
| MITECO-download | `https://gis.miteco.gob.es/descargas/app/DescargaFichero?f=dpmt.zip` (shp, 12,2 MB, "Updated 31/03/2026"); `sp.zip` (44,6 KB, 30-09-2024) | niet gedownload (akkoord nodig); host gaf een verbindingsreset | 2 (pagina) / 3 |
| Juridische waarde | MITECO: "Los datos disponibles tienen un carácter meramente informativo" | — | 2 |

---

## 7. Geoportalen: werkende eindpunten en laagnamen (opdracht f)

| Portaal / dienst | Eindpunt (getest) | Test en resultaat 15-09-2026 | Belangrijkste lagen | Licentie of voorwaarde |
|---|---|---|---|---|
| **Visor de Cartografía GVA** | `https://visor.gva.es/visor/`; laagconfiguratie `https://icvficherosweb.icv.gva.es/00/geovisorgva/params/pro/configCapas.js` | HTML 200; config 200 (448 kB) met alle service-URL's | alle onderstaande | — |
| ICV WMS/WFS Infraestructura Verde | `https://terramapas.icv.gva.es/0701_InfraestructuraVerde` | GetCapabilities 200; GFI (geojson) P1/P2/P3/P4; WFS GetFeature | `IVR.Inundacion`, `IVR.ParquesNaturales`, `IVR.ZEC`, `IVR.LIC`, `IVR.ZEPA`, `IVR.Montes`, `IVR.TFEPATFOR`, `IVR.Cultura.BIC.BIC`, `IVR.Cultura.BIC.Entornos`, `IVR.Cultura.BRL`, `IVR.PaisajesRelevancia`, `IVR.Cavidades`, `IVM.*` | "CC BY 4.0 Generalitat" |
| ICV WMS/WFS Planeamiento | `https://terramapas.icv.gva.es/0702_Planeamiento` | idem; WFS alleen met BBOX in **EPSG:25830** (BBOX in 4326 gaf 0 objecten; OGC-filter gaf een serverfout) | `Planeamiento.Clasificacion`, `Planeamiento.Zonificacion`, `Planeamiento.Dotaciones`, `InventarioSuSuz`, `MinimizacionViviendasSNU`, `DeclaracionInteresComunitario` | CC BY 4.0 |
| ICV WMS PATFOR | `https://terramapas.icv.gva.es/0506_PATFOR` | GetCapabilities + GFI | `SF.Forestal`, `Forestal.Estrategico`, `Regulacion.Incendios.Urbano`, `Regulacion.Incendios.Peligrosidad` | CC BY 4.0 |
| ICV WMS PORN / PRUG | `https://terramapas.icv.gva.es/0505_PORN`, `…/0505_PRUG` | PORN: GetCapabilities + GFI | `Montgo.PORN`, `Montgo.Zonificacion`, `Montgo.ZonificacionSantAntoni`, `Montgo.Parque` | CC BY 4.0; "carácter informativo" |
| ICV WMS Biodiversidad | `https://terramapas.icv.gva.es/0502_Biodiversidad` | GetCapabilities + GFI + WFS | `Microrreservas`, `Habitats10000.IntComHabitats`, `Reservas.ReservasFauna`, `MedioMarino.Fanerogamas` | CC BY 4.0 |
| ICV WMS Costas | `https://terramapas.icv.gva.es/0703_Costas` | GetCapabilities | alleen beeldmateriaal (luchtfoto's 1956–1998, schuine opnames), batimetrie — **geen deslinde** | CC BY 4.0 |
| ICV Nomenclàtor / grenzen | `https://terramapas.icv.gva.es/0103_NTV` (WFS `NTV.Puntos/Lineas/Poligonos`); `https://terramapas.icv.gva.es/0105_Delimitaciones` (WFS `ICV.Municipios`) | WFS 200 | toponiemen; gemeentegrens Xàbia 6.893,84 ha | — |
| ICV orthofoto 2024 | `https://terramapas.icv.gva.es/0202_2024CVAL0025` | GetCapabilities + GetMap (JPEG 500×400 rond P1) | `2024CVAL0025_RGB`, `2024CVAL0025_IRG` | — |
| ICV "Patrimonio GVA" | `https://terramapas.icv.gva.es/13_GeoPat` | GetCapabilities | `BienesInmueblesGVA` = **vastgoed in eigendom van de GVA, geen erfgoedcatalogus** | CC BY 4.0 |
| ICV ArcGIS REST | `https://carto.icv.gva.es/arcgis/rest/services/tm_infraestructuras/ordenacion_territorial/MapServer` · `…/tm_medio_ambiente/espacios_protegidos/MapServer` · `…/tm_medio_ambiente/forestal/MapServer` · `…/tm_medio_ambiente/prevencion_de_incendios/MapServer` | `?f=json` 200; `identify` en `query` (ArcGIS 10.61, maxRecordCount 2000, SR 3857) | zie §3.2, §4.2, §4.4 | niet vermeld in JSON [te verifiëren] |
| "Terrasit" | `terrasit.gva.es` | **DNS lost niet op** → oude merknaam; opgevolgd door terramapas / visor | — | — |
| **IDEE** — gevaar overstroming (ARPSI) | `https://servicios.idee.es/wms-inspire/riesgos-naturales/inundaciones` | GetCapabilities 200 + GFI (text/plain) | `NZ.Flood.FluvialT10/T100/T500`, `NZ.Flood.MarinaT100/T500`, `EL.GridCoverage` | vrij, vermelding MITECO |
| IGN PNOA (via IDEE) | `https://www.ign.es/wms-inspire/pnoa-ma` | GetCapabilities 200 | `OI.OrthoimageCoverage`, `OI.MosaicElement` | "CC BY 4.0 scne.es" |
| **SNCZI (MITECO)** | `https://wms.mapama.gob.es/sig/agua/ZI_LaminasQ100` e.a.; viewer `https://gis.miteco.gob.es/web/snczi` | **serverfout / reset / 503** | (Q10, Q50, Q100, Q500, ZFP, DPH, ARPSI) | vrij met vermelding |
| **Catastro** (kruislaag) | WMS `https://ovc.catastro.meh.es/Cartografia/WMS/ServidorWMS.aspx`; puntdienst `…/OVCCoordenadas.asmx/Consulta_RCCOOR` | GetCapabilities 200; GFI P1/P2 → kadastrale referentie; Consulta_RCCOOR idem | `Catastro`, `PARCELA`, `CONSTRU`, `SUBPARCE` (+ INSPIRE-WMS/WFS in R11) | "No tiene la categoría de cartografía oficial … No está permitida la descarga masiva" |
| **IGME** geologie | `https://mapas.igme.es/gis/services/Cartografia_Geologica/IGME_MAGNA_50/MapServer/WMSServer`; `…/IGME_Geode_50/MapServer/WMSServer` | GetCapabilities 200; GFI GEODE laag 1 op P1–P3 | GEODE: 0 Zonas, **1 Recintos geología**, 3 Cuaternario… | "No está permitido implementar un servicio de valor añadido no gratuito sin establecer contacto con el IGME" |

---

## 8. Erfgoed, geotechniek en nutsvoorzieningen (opdracht g)

### 8.1 Erfgoed en archeologie

- **Inventario General del Patrimonio Cultural Valenciano** via ICV (bewijstype 3; fiches op cultura.gva.es):
  - **BIC in Xàbia (10):** Iglesia Parroquial de San Bartolomé (monument, **met beschermde omgeving**), Casa forta de la Bardissa, Torre de Ambolo, Torre Bolufer, Torre Capçades, Torre Pelleter o del Pardalet, Torre de Portichol, Torre Torroner, Torre La Granadella, en de **archeologische zone "Yacimiento romano Illeta del Portichol"**.
  - **BRL in Xàbia (28):** o.a. Casas del Pósito, Molinos de la Plana (11×, etnologisch), Casa Escrivà (Hemeroscopea), Iglesia N.ª S.ª de Loreto, Monasterio N.ª S.ª de los Ángeles, Batería del Portixol, Campo de Aviación del Plà, Refugio del Moll.
  - Geen BIC-conjunto histórico-afbakening in Xàbia in de laag (de enige in de bbox is "Teulada Gótica Amurallada").
- **Oude kern (casco antiguo):**
  - Ley 4/1998 **DA 5ª** (geconsolideerd tot 17-08-2026): "Tienen la consideración de bienes inmuebles de relevancia local, mientras no se les excluya en los respectivos catálogos … 1. Los núcleos históricos tradicionales" (bewijstype 2).
  - Xàbia heeft planzones ZUR-NHT en de NTU-zone "NHT Zona A: Casco" (§2.6).
  - **Inferentie (bewijstype 4):** de casco antiguo is van rechtswege BRL, tenzij uitgesloten in de catalogus. Of dit in het Inventario als BRL is ingeschreven: ONBEKEND (niet in de BRL-laag).
- **Gemeentelijke Catálogo de bienes y espacios protegidos:** in het GVA-planregister voor Xàbia staan "03082-1002 PGMOD XVII AMPLIACIÓN CTLG" (met map "5 CATÁLOGO") en "03082-1000 PLAN GENERAL". Inhoud, datum en archeologische zones zijn **niet gelezen** → [te verifiëren]; handmatig via `https://mediambient.gva.es/auto/urbanismo/reg-planeamiento/2%20ALICANTE/03082%20X%C0BIA/`.
- **Juridisch:**
  - TRLOTUP art. 232.f: ingrepen met erfgoedbelang zijn vergunningplichtig; art. 233.1.a en c: DR niet mogelijk bij beschermde elementen of omgevingen (BIC/BRL) en archeologische aandachtsgebieden.
  - Art. 240.1.c: termijn 3 maanden.
  - Art. 255.5: geen verjaring bij Inventario-goederen.

### 8.2 Geotechniek

- **IGME GEODE 1:50.000** (bewijstype 3), GFI laag "Recintos geología":
  - P1 Arenal: "**Limos de albufera**" (Holoceen).
  - P2 Granadella: "Calizas, calizas margosas y margas. Albiense-Cenomaniense".
  - P3 Montgó-flank: "Depósitos aluviales, fondo de valle" (Holoceen).
- **Inferentie (bewijstype 4):** lagunaire silt bij P1 wijst op mogelijk slappe bodem en hoog grondwater. Een funderingsonderzoek (estudio geotécnico) is dan zeker nodig; kosten ONBEKEND.
- **Geen geotechnische WMS gevonden** in de IGME-map `Cartografia_Tematica` (wel hydrogeologie, doorlatendheid, karst). Een officiële geotechnische kaart is dus niet als dienst beschikbaar → per project een grondonderzoek door een bevoegd laboratorium of ingenieur (bewijstype 6 zodra uitgevoerd).

### 8.3 Nutsvoorzieningen (waar de informatie vandaan komt)

| Nut | Beheerder | Informatieroute | Bewijstype |
|---|---|---|---|
| Drinkwater en riolering Xàbia | **AMJASA – Aguas Municipales de Jávea S.A.** (gemeentelijk bedrijf sinds 1977; `https://amjasa.com/quienessomos/`) | Aansluiting of beschikbaarheid aanvragen bij AMJASA; procedure en tarieven niet op de site gezien → [te verifiëren] | 2 (bestaan) / 7 (procedure) |
| Elektriciteit | **i-DE Redes Eléctricas Inteligentes** (Iberdrola-groep) | Nieuwe aansluiting of vermogensverhoging via het portaal "Gestión de Expedientes de Acometida (GEA)" (`https://www.i-de.es/grid-connection/electric-supply`) | 2 |
| Wettelijke koppeling | TRLOTUP art. 245 | Levering alleen met vergunningen; stopzetting bij een handhavingsbevel | 2 |
| SNU | TRLOTUP art. 211.1.b.4 en 211.3 | Water, afval en zuivering voor rekening van de eigenaar; netuitbreiding voor rekening van de initiatiefnemer | 2 |
| PORN Montgó | art. 109.5.b en e | Nieuwe wateronttrekking en nieuwe water- of rioolaansluitingen: rapport van de Conselleria | 2 |

---

## 9. Laagfiches — per laag: wat, betekenis, waar, test P1/P2, waarschuwing

| Laag | Juridische betekenis | Waar bevragen | P1 Arenal | P2 Granadella | Waarschuwing ("geen beperking gevonden ≠ geen beperking") |
|---|---|---|---|---|---|
| PATRICOVA gevaar 1–6 + geomorf. | Bindend (art. 3); verboden in SNU (art. 18); voorwaarden in SU (art. 20) | 0701 `IVR.Inundacion`; ArcGIS ordenación 4–10 | **Niveau 4** (AC07, T100, < 0,8 m) | geen | Lokale inundabiliteitsstudies (laag 1) kunnen afwijken; niveau 1 niet in 18.2; ARPSI-tegenstrijdigheid |
| PATRICOVA risico | Afgeleid; niet voor besluiten | ArcGIS 12 | "Medio" | — | Gebruik de gevaarlagen |
| ARPSI (IDEE) | Gevaarkaart RD 903/2010; complementair (PATRICOVA art. 7) | IDEE inundaciones | T10 0,073 / T100 1,951 / T500 2,466 (eenheid ONBEKEND) | 999 (vermoedelijk buiten studie) | Alleen voor ARPSI-gebieden; eenheid verifiëren |
| SNCZI (MITECO) | Zonas inundables, DPH, ZFP | wms.mapama.gob.es / gis.miteco.gob.es | **niet getest** (serverfout) | niet getest | Onbereikbaar op 15-09-2026 |
| Planclassificatie | Mozaïek van geldende plannen (informatief) | 0702 `Planeamiento.Clasificacion` | SU ZUR-RE | SNU-P ZRP-NA-MU | PGOU 1990, NTU 2021 (status ONBEKEND); gemeente is leidend |
| Minimización SNU | Inventaris van kandidaten (1976–2014) | 0702 `MinimizacionViviendasSNU` | — | — | Niet in de laag ≠ legaal |
| PATFOR bosgrond / TFE | Voorwaarden art. 28–32; bosadvies | 0506 `SF.Forestal`, `Forestal.Estrategico` | nee | **ja / ja** | Rastergegevens grof; verdedigingsstrook 30 m |
| Brand: interface / PLPIF / ZIF / branden | TRLOTUP DA 7 + bijlage XI; art. 7.4 (30 jaar) | 0506 `Regulacion.Incendios.Urbano`; ArcGIS prevención 1–121, 103/107, 114, 123, 127 | "Sin interfaz"; PLPIF goedgekeurd | **"Alta"**; branden 2000 + 2016 | Afbakening Xàbia niet in de dienst (alleen status 28-05-2026) |
| PORN Montgó | Ley 11/1994 art. 29/DA 6ª; PORN art. 36, 55–57, 109 | 0505 `Montgo.PORN`, `Montgo.Zonificacion` | buiten | buiten | Delimitatie "informativo"; officiële kaart in het decreet |
| Parque Natural | Bouwverbod (PORN 56) | 0701 `IVR.ParquesNaturales` | nee | nee | — |
| ZEC/ZEPA/LIC + zonering | Norma de gestión (Decreto 197/2022); evaluatie van effecten (Decreto 60/2012) | 0701 `IVR.ZEC/LIC/ZEPA`; ArcGIS espacios 21–24 | nee | **ZEC + ZEPA + LIC, zone B** | Montgó: alleen LIC in de laag |
| Microreservaten | Besluiten per microreservaat | 0502 `Microrreservas` | nee | nee | Klein (0,07–6,4 ha); afstand meten |
| Montes | Bosregime, TRLOTUP 5.4 | 0701 `IVR.Montes`; ArcGIS forestal 25 | nee | nee (bos "La Granadella" dichtbij) | Lagen tegenstrijdig over "catalogado" |
| PATIVEL Litoral 1/2 | Decreto 58/2018 art. 8–11 (onder Ley 3/2025) | ArcGIS ordenación 34 | nee | nee | Het plan geldt voor grond in landelijke situatie |
| PATIVEL-ámbitos 500/1000/2000 m | Art. 3 | ArcGIS 32/30/31 (**lijnen**) | ±80 m van de ribera volgens de lijnafstand | ±277 m | Punt-in-polygoon werkt niet; afstand berekenen |
| Catálogo de playas | Kustgebruik (DPMT) | ArcGIS 33 | tramo Xabia_4 "El Arenal" U1 nabij | tramo Xabia_6 N1 nabij | Regelt strandgebruik, niet bouwen |
| Costas: DPMT / servidumbre | Ley 22/1988 art. 23–30, DT 3ª–4ª; Ley 3/2025 art. 44–45 | MITECO WMS/viewer/download | **niet getest** | niet getest | "carácter meramente informativo" |
| DPH-waterlopen | RDL 1/2001 art. 6 (5 m / 100 m) | MITECO DPH-WMS (onbereikbaar); NTV-lijnen als signaal | canal la Fontana 154 m | **barranc 14 m** | Een NTV-lijn is geen deslinde |
| BIC/BRL + omgevingen | Ley 4/1998; TRLOTUP 232.f, 233, 255.5 | 0701 `IVR.Cultura.*` (WMS/WFS) | nee | nee | NHT van rechtswege BRL (DA 5ª); archeologische zones in de gemeentelijke catalogus |
| Geologie | Geen juridische werking; technisch | IGME GEODE 50 | limos de albufera | kalk/mergel | Geen geotechnische dienst; grondonderzoek nodig |
| Catastro | Identificatie; geen bewijs van bouwrecht | Catastro WMS/OVC | 5658011BC5955N | 03082A01200623 | Geen officiële cartografie; zie R11 |

---

## 10. Proef op de eigen feed: BP-objecten tegen de sectorale lagen

Bron: `http://127.0.0.1:3100/api/properties?town=Javea&limit=100`, eigen dienst, alleen gelezen op 15-09-2026. Dit gaf **56 objecten** (in de eerdere meting 57), waarvan 40 met coördinaten (bewijstype 1 voor de coördinaten). De lagen zijn één keer per laag opgehaald en daarna lokaal met punt-in-polygoon getoetst; er zijn geen massale verzoeken gedaan.

- **Datakwaliteit (bewijstype 3):** 3 objecten hebben de nepcoördinaat 25,6865 / −80,4313 (Florida), 1 object ("Tosalet 5") ligt op 38,7089 / 0,064 (buiten Xàbia), 2 objecten ("Center", "Tarraula") hebben identieke coördinaten → 36 van de 40 liggen binnen de gemeentegrens.
- **Treffers (bewijstype 3 als laaguitslag, 4 als objectconclusie):** 12 van de 40 objecten raken ten minste één beperkende laag.

| BP-ref | Type / zone (aanbieder) | Planklasse | Sectorale treffers |
|---|---|---|---|
| C3XY4641JAV | Villa, Senioles | **SNU-P ZRP-CA** | **PATRICOVA niveau 1** + PORN "Conectores ambientales" |
| C4XY4619JAV | Apartment, Port | SU ZUR-RE | PATRICOVA niveau 4 + PORN "urbanas" |
| 4679JAV | (geen type), Adsubia | SNU-C ZRC-FO | PATRICOVA niveau 5 |
| 4642JAV | Apartment, Port | SUZ ZND-RE | PATRICOVA geomorfologisch |
| 4532JAV | Land, Costa Nova | SNU-P ZRP-NA-MU | ZEC Penya-segats de la Marina |
| 4603JAV | Land, Villes del Vent | SUZ ZND-RE | ZEC Penya-segats de la Marina |
| 4676JAV (= K07) | Land, Montgó-Ermita | SU ZUR-RE | PORN "urbanas" |
| 4480JAV, 4490JAV | Villa, El Garroferal | SU / SUZ | PORN "urbanas" |
| C3XY4492JAV | Villa, La Corona | SUZ | PORN "urbanas" |
| C3XY4678JAV, C3XY4395JAV | Center / Tarraula (gedeelde coördinaat) | SU ZUR-NHT | PORN "urbanas" (coördinaat verdacht) |

**Les:** de toets werkt technisch, en twee "Land"-objecten liggen volgens hun pin in een ZEC. Zolang de pin niet via Catastro aan een perceel is gekoppeld, hoort dit in het dossier als "signaal — perceelidentificatie ontbreekt" (masterprompt §14).

---

## 11. Hoe dit in de Deal Hunter kan (ontwerpnotitie, niets gebouwd)

1. **Automatiseerbaar per coördinaat of perceel (open data, zonder sleutel):**
   - PATRICOVA (0701 GFI of ArcGIS `identify`);
   - PORN (0505);
   - Red Natura en zonering (0701 + ArcGIS espacios 21);
   - PATFOR, interface en ZIF (0506 + ArcGIS prevención);
   - planklasse en minimización (0702);
   - PATIVEL Litoral 1/2 (ArcGIS 34) plus afstand tot de ámbito-lijnen (ArcGIS `query` + `distance`);
   - BIC/BRL (0701);
   - ARPSI (IDEE);
   - geologie (IGME);
   - kadastrale referentie (Catastro).

   Allemaal getest met `httpx` (aanwezig in de Hermes-venv). Geen shapely of pyproj nodig: UTM-omrekening en punt-in-polygoon zijn met ±60 regels Python gedaan, maar een ondersteunde bibliotheek is robuuster (installatie alleen met akkoord van Jan).
2. **Beter perceel dan pin:** perceelsgeometrie uit de Catastro-WFS (R11) → een ArcGIS `query` met de polygoon (`esriGeometryPolygon`, inSR 25830) geeft de oppervlakte-overlap in plaats van een punttreffer.
3. **Cachen per laag, niet per object:** PATRICOVA- en PATIVEL-polygonen voor Xàbia zijn een paar honderd kB; wekelijks verversen volstaat. Houd per laag de "datum van laatste controle" bij en een "dienst onbereikbaar"-status (MITECO!).
4. **Licenties:**
   - ICV CC BY 4.0: bronvermelding in dossiers.
   - IDEE/MITECO: vermelding MITECO.
   - Catastro: geen massale download.
   - **IGME: contact vereist bij een betaalde dienst met toegevoegde waarde** → bij commercieel gebruik eerst contact.
5. **Uitslagtaal in het dossier:** "Signaal (laag X, datum, bewijstype 3)" versus "Bevestigd (cédula of informe municipal, bewijstype 2/6)". Nooit "geen beperking".

---

## 12. Open vragen en ⏸️ ACTIE VOOR JAN

**Maximaal drie vragen aan Jan nu:**
1. Mag ik de MITECO-deslindebestanden downloaden zodra de server weer werkt? Het gaat om `dpmt.zip`, 12,2 MB (shapefile, bijgewerkt 31-03-2026), en `sp.zip`, 44,6 KB, van gis.miteco.gob.es. Dit is nodig voor de 100 m/20 m-toets aan de kust.
2. Welke gebieden hebben prioriteit voor een schriftelijke gemeentelijke bevestiging (cédula de garantía urbanística / informe urbanístico, art. 246) — bijvoorbeeld Arenal, de Montgó-flank of Portitxol?
3. Wil je een vaste lokale architect of ingenieur aanwijzen voor de interpretatievragen hieronder (bewijstype 6)?

**⏸️ ACTIE VOOR JAN**
- Per concreet object bij het Ajuntament de Xàbia (Urbanisme) opvragen: de cédula of het informe urbanístico (art. 246), de actuele status van NTU/PGE, en de cartografie van de brandinterface (goedgekeurd op 28-05-2026 volgens de GVA-laag) met de bijbehorende termijn.
- Bij de kustdienst (Demarcación de Costas Comunitat Valenciana-Sur [te verifiëren]) of via een kustjurist: de deslinde en servidumbre voor Arenal, Portitxol en de havenzone.

**Open onderzoeksvragen**
- Eenheid en betekenis van de IDEE-ARPSI-rasterwaarden (1,951 bij T100 op P1; "999" op P2) en de verhouding tot PATRICOVA niveau 4.
- Is Xàbia ingeschreven in het register van gemeenten met "elevada peligrosidad" (PATRICOVA DA 1ª)? Waarschijnlijk niet, maar het register is niet ingezien.
- Werkt de Agencia Valenciana de Protección del Territorio (TRLOTUP DT 28), zodat minimización-procedures weer mogelijk zijn?
- Betekenis van "tipo D/R" in `MinimizacionViviendasSNU`.
- Is de Montgó al als ZEC aangewezen (alleen LIC in de laag)?
- Bosgebied La Granadella / Montgó I: "gecatalogiseerd" of niet (tegenstrijdige lagen)?
- Is de casco antiguo van Xàbia in het Inventario als BRL/NHT ingeschreven (DA 5ª Ley 4/1998)? Hoe zien de gemeentelijke catalogus (PGMOD XVII) en de archeologische zones eruit?
- Hoe gaat Xàbia om met bijlage I van PATRICOVA in SU (art. 20): worden 80 cm vloerpeil en een kelderverbod opgelegd in Arenal en Saladar?
- PATIVEL: loopt er nog TSJCV-procedure na de terugverwijzing door het TS die Xàbia raakt? Wanneer wordt het Plan de Ordenación Costera vastgesteld?
- Ley 3/2025 art. 51 (voorkoopsrecht): worden er gebieden in Xàbia afgebakend?
- Classificatie van l'Arenal op 29-07-1988 (20 m of 100 m servidumbre) → raakvlak met R12.
- PATFOR na 2013 gewijzigd?

---

## 13. Geblokkeerd of mislukt

- **MITECO WMS** (`wms.mapama.gob.es/sig/agua/ZI_LaminasQ100`, `ZI_LaminasQ500`, `ZI_LaminasZFP`, `ZI_ARPSI`, `DPHCartografico`, `sig/Costas/DPMT`, `sig/Costas/SP`): HTTP 200 met ServiceException "NullReferenceException" bij alle geprobeerde parametervarianten (15-09-2026).
- **MITECO nieuwe GIS-host** `gis.miteco.gob.es` (viewer dpmt en snczi, downloads): curl "Connection reset by peer"; WebFetch HTTP 503. Niet geprobeerd te omzeilen.
- `sig.miteco.gob.es/snczi/` en `/dpmt/`: 301 naar een migratiepagina op mapa.gob.es.
- MITECO ISO-metadata (mapama.gob.es CSW GetRecordById voor de ARPSI-T100-laag): lege respons (122 bytes).
- `terrasit.gva.es`: DNS lost niet op.
- ICV WFS `0702_Planeamiento` met OGC-filter op `cod_ine_mun`: serverfout "FLTApplyFilterToLayer() failed"; BBOX in EPSG:4326 gaf 0 objecten. Opgelost met BBOX in EPSG:25830 en een filter aan clientzijde.
- ICV ArcGIS prevención laag 112/113 ("instalaciones en riesgo", "áreas susceptibles"): geen objecten voor Xàbia (alleen Dénia).
- `mediambient.gva.es/es/web/sistema-de-informacion-territorial/servicio-wms-69944`: HTTP 404.
- Kolomtabellen in de pdf van Decreto 197/2022 (zones A–D met X-markeringen) zijn niet betrouwbaar als tekst uit te lezen → pagina 63–64 handmatig bekijken.
- Niet gelezen of niet gedownload (bewust): RD 876/2014 Reglamento de Costas, PRUG Montgó (Decreto 229/2007), de besluiten per microreservaat, de gemeentelijke catalogus en de NTU-kaarten van Xàbia, de MITECO-deslindebestanden (download vraagt akkoord).

---

## 14. Bronnenlijst (URL · controledatum · bewijstype)

1. https://www.boe.es/buscar/act.php?id=DOGV-r-2021-90283 — TRLOTUP geconsolideerd (versie 02-07-2026; art. 5, 7, 206, 210–231 bis, 232–256, DT 26/28, DA 7, bijlage XI) · 15-09-2026 · 2
2. https://www.boe.es/buscar/act.php?id=DOGV-r-2021-90283&b=317&tn=1&p=20210716 — originele tekst art. 228 (2021) · 15-09-2026 · 2
3. https://www.boe.es/buscar/act.php?id=BOE-A-2025-1 — Ley 6/2024 simplificación administrativa · 15-09-2026 · 2
4. https://www.boe.es/buscar/act.php?id=BOE-A-2026-15683 — Ley 3/2026 hiperregulación · 15-09-2026 · 2
5. https://www.boe.es/buscar/doc.php?id=DOGV-r-2025-90320 — Decreto-ley 14/2025 (titel via zoekresultaat) · 15-09-2026 · 2
6. https://www.boe.es/buscar/act.php?id=BOE-A-2025-9743 — Ley 2/2025 DANA (titel) · 15-09-2026 · 2
7. https://www.boe.es/buscar/act.php?id=BOE-A-2025-717 — Ley 8/2024 accesibilidad (zoekresultaat) · 15-09-2026 · 2
8. https://www.boe.es/buscar/act.php?id=BOE-A-2025-11647 — Ley 3/2025 costa valenciana (versie 17-08-2026; art. 2, 17, 23, 44, 45, 50, 51, DA 1–4, DT 1–3, DF 2; TC-noten) · 15-09-2026 · 2
9. https://mediambient.gva.es/es/web/urbanismo/novetats — anteproyecto Ley del Suelo (08-01-2026), consulta POC (01-12-2025) · 15-09-2026 · 2
10. https://interdiario.es/2026/07/17/el-consell-aprueba-el-anteproyecto-de-ley-del-suelo-de-la-comunitat-valenciana — pers, voorontwerp Ley del Suelo · 15-09-2026 · 1 (niet-officieel)
11. https://mediambient.gva.es/documents/20551069/162377494/02+Normativa.pdf/5d2bca03-0f7f-4774-b602-4447cfb8dce7 — PATRICOVA Normativa (Decreto 201/2015) · 15-09-2026 · 2
12. https://mediambient.gva.es/es/web/planificacion-territorial-e-infraestructura-verde/cartografia-del-patricova — PATRICOVA-cartografie (visor, WMS, download) · 15-09-2026 · 2
13. https://visor.gva.es/visor/ en https://icvficherosweb.icv.gva.es/00/geovisorgva/params/pro/configCapas.js — laagconfiguratie van het GVA-visor · 15-09-2026 · 2/3
14. https://terramapas.icv.gva.es/0701_InfraestructuraVerde — WMS/WFS (GetCapabilities, GFI, GetFeature) · 15-09-2026 · 3
15. https://terramapas.icv.gva.es/0702_Planeamiento — WMS/WFS · 15-09-2026 · 3
16. https://terramapas.icv.gva.es/0506_PATFOR — WMS · 15-09-2026 · 3
17. https://terramapas.icv.gva.es/0505_PORN — WMS · 15-09-2026 · 3
18. https://terramapas.icv.gva.es/0502_Biodiversidad — WMS/WFS · 15-09-2026 · 3
19. https://terramapas.icv.gva.es/0703_Costas — WMS · 15-09-2026 · 3
20. https://terramapas.icv.gva.es/13_GeoPat — WMS · 15-09-2026 · 3
21. https://terramapas.icv.gva.es/0103_NTV en https://terramapas.icv.gva.es/0105_Delimitaciones — WFS toponiemen en gemeentegrens · 15-09-2026 · 3
22. https://terramapas.icv.gva.es/0202_2024CVAL0025 — orthofoto 2024 WMS · 15-09-2026 · 3
23. https://carto.icv.gva.es/arcgis/rest/services/tm_infraestructuras/ordenacion_territorial/MapServer — PATRICOVA- en PATIVEL-lagen (identify/query) · 15-09-2026 · 3
24. https://carto.icv.gva.es/arcgis/rest/services/tm_medio_ambiente/espacios_protegidos/MapServer — Red Natura en zonering · 15-09-2026 · 3
25. https://carto.icv.gva.es/arcgis/rest/services/tm_medio_ambiente/prevencion_de_incendios/MapServer — PLPIF, interface, ZIF, branden · 15-09-2026 · 3
26. https://carto.icv.gva.es/arcgis/rest/services/tm_medio_ambiente/forestal/MapServer — bossen · 15-09-2026 · 3
27. https://dogv.gva.es/datos/2020/07/29/pdf/2020_6092.pdf — Resolución 21-07-2020 PLPIF Jávea · 15-09-2026 · 2
28. https://dogv.gva.es/datos/2013/05/08/pdf/2013_4617.pdf — Decreto 58/2013 PATFOR (art. 28–32) · 15-09-2026 · 2
29. https://dogv.gva.es/datos/2002/11/08/pdf/2002_12109.pdf — Decreto 180/2002 PORN Montgó (art. 3, 4, 12, 36, 55–57, 71, 109) · 15-09-2026 · 2
30. https://parquesnaturales.gva.es/es/web/pn-el-montgo/legislacion-y-normativa — overzicht instrumenten Montgó (PRUG 229/2007, reserva marina, PPIF) · 15-09-2026 · 2
31. https://www.boe.es/buscar/act.php?id=BOE-A-1995-3325 — Ley 11/1994 ENP (art. 29, 33, DA 6ª) · 15-09-2026 · 2
32. https://dogv.gva.es/datos/2022/11/28/pdf/2022_11078.pdf — Decreto 197/2022 ZEC/ZEPA Penya-segats de la Marina (norma de gestión) · 15-09-2026 · 2
33. https://mediambient.gva.es/es/web/planificacion-territorial-e-infraestructura-verde/plan-de-accion-territorial-de-la-infraestructura-verde-del-litoral — PATIVEL-pagina · 15-09-2026 · 2
34. https://mediambient.gva.es/auto/planes-accion-territorial/PATIVEL/ — Decreto 58/2018 (versión vigente 04.06.2025), Nota informativa Sentencia 46/2021, Sentencia TS 27-04-2022 (491/2022) · 15-09-2026 · 2
35. https://mediambient.gva.es/auto/planes-accion-territorial/Ejecucion%20de%20sentencias%20PATIVEL/ — uitvoering van vonnissen 2025–2026 · 15-09-2026 · 2
36. https://www.poderjudicial.es/cgpj/es/Poder-Judicial/Tribunal-Supremo/Noticias-Judiciales/El-Tribunal-Supremo-estima-el-recurso-de-la-Generalitat-contra-la-sentencia-del-TSJ-de-la-Comunidad-Valenciana-que-declaro-nulo-el-Decreto-por-el-que-se-aprobo-el-Plan-Pativel — CGPJ-bericht TS PATIVEL (zoekresultaat) · 15-09-2026 · 2
37. https://www.boe.es/buscar/act.php?id=BOE-A-1988-18762 — Ley 22/1988 de Costas (art. 23–25, 27, 30, DT 3ª–4ª) · 15-09-2026 · 2
38. https://www.boe.es/buscar/act.php?id=BOE-A-2001-14276 — RDL 1/2001 Ley de Aguas (art. 6) · 15-09-2026 · 2
39. https://www.miteco.gob.es/en/costas/temas/procedimientos-gestion-dominio-publico-maritimo-terrestre/linea-deslinde.html — deslinde, "meramente informativo" · 15-09-2026 · 2
40. https://www.miteco.gob.es/en/cartografia-y-sig/ide/directorio_datos_servicios/costas/wms-inspire-costas.html — WMS-catalogus kust · 15-09-2026 · 2
41. https://www.miteco.gob.es/es/cartografia-y-sig/ide/descargas/costas-medio-marino/deslinde-dpmt.html — downloads DPMT (31-03-2026) · 15-09-2026 · 2
42. https://www.miteco.gob.es/en/cartografia-y-sig/ide/directorio_datos_servicios/agua/wms-inspire-agua.html — WMS-catalogus water (SNCZI) · 15-09-2026 · 2
43. https://www.miteco.gob.es/es/cartografia-y-sig/visores.html — viewers (gis.miteco.gob.es/web/snczi, /web/dpmt) · 15-09-2026 · 2
44. https://wms.mapama.gob.es/sig/agua/ZI_LaminasQ100 (en overige genoemde MITECO-WMS) — test mislukt (ServiceException) · 15-09-2026 · 3
45. https://servicios.idee.es/wms-inspire/riesgos-naturales/inundaciones — IDEE ARPSI-WMS (GetCapabilities, GFI) · 15-09-2026 · 3
46. https://www.idee.es/csw-codsi-idee/srv/api/records/f6c6eaac-2126-4a43-909f-3467380e6cde — metadata IDEE-dienst (gewijzigd 09-12-2025) · 15-09-2026 · 2
47. https://www.ign.es/wms-inspire/pnoa-ma — PNOA WMS · 15-09-2026 · 3
48. https://ovc.catastro.meh.es/Cartografia/WMS/ServidorWMS.aspx en https://ovc.catastro.meh.es/ovcservweb/OVCSWLocalizacionRC/OVCCoordenadas.asmx/Consulta_RCCOOR — Catastro WMS en coördinaatdienst · 15-09-2026 · 3
49. https://mapas.igme.es/gis/services/Cartografia_Geologica/IGME_Geode_50/MapServer/WMSServer en https://mapas.igme.es/gis/services/Cartografia_Geologica/IGME_MAGNA_50/MapServer/WMSServer — IGME WMS · 15-09-2026 · 3
50. https://mapas.igme.es/gis/rest/services/Cartografia_Tematica?f=json — IGME thematische diensten (geen geotechnische dienst) · 15-09-2026 · 3
51. https://www.boe.es/buscar/act.php?id=BOE-A-1998-17524 — Ley 4/1998 Patrimonio Cultural Valenciano (DA 5ª; versie 17-08-2026) · 15-09-2026 · 2
52. https://mediambient.gva.es/auto/urbanismo/reg-planeamiento/2%20ALICANTE/03082%20X%C0BIA/ — GVA-planregister Xàbia (NUTU, PGMOD, PP's) · 15-09-2026 · 2
53. https://mediambient.gva.es/auto/urbanismo/reg-planeamiento/2%20ALICANTE/03082%20X%C0BIA/1%20P.%20GENERAL/03082-0000%20NUTU%20X%E0bia/ — Acuerdo del Consell 10-09-2021, NTU Xàbia · 15-09-2026 · 2
54. https://amjasa.com/quienessomos/ — AMJASA (zoekresultaat) · 15-09-2026 · 2
55. https://www.i-de.es/grid-connection/electric-supply — i-DE, nieuwe aansluiting (zoekresultaat) · 15-09-2026 · 2
56. http://127.0.0.1:3100/api/properties?town=Javea&limit=100 — eigen BP-feed-API (alleen lezen; 56 objecten) · 15-09-2026 · 3 (coördinaten zelf: 1)
57. /Users/root-admin/tree-es/deal-hunter/onderzoek/R15-kandidaten-javea-live.md — pin K07 Montgó-Ermita · 14-09-2026 · 1
58. /Users/root-admin/tree-es/deal-hunter/onderzoek/R11-catastro-registro-perceelidentificatie.md — Catastro-diensten · 14-09-2026 · 3

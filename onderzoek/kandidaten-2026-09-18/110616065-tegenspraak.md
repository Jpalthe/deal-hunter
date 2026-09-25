# 110616065 — Tegenspraak op het systeemscenario

**Opdracht:** haal het scenario van ons eigen systeem onderuit, of laat het staan.
**Controledatum:** 18-09-2026 · **Object:** Idealista 110616065, vraagprijs € 497.000
**Bronnen:** officiële Idealista-assistent (MCP `property_detail` / `search_properties`, country `es`), onze eigen dossiers in `~/tree-es/deal-hunter/onderzoek/`, en openbare bronnen (Ayuntamiento de Xàbia, pers). Niet gescrapet, niet ingelogd.

Bewijstypen: (1) aanbieder zegt het · (2) officiële bron · (3) door ons vastgesteld · (5) berekening op benoemde aannames · (7) onbekend of tegenstrijdig.

**Oordeel vooraf: het scenario valt af.** Niet op een detail, maar op de fundering: het rekent met de verkoopprijzen van een andere wijk, op vierkante meters die nergens in de advertentie staan.

---

## 1. Het object is niet waar ons systeem denkt dat het is

Het scenario noemt dit "Country House in Granadella – Balcón al Mar". Dat is het niet.

De advertentie zegt letterlijk: *"En plena calle Mayor de Jávea"* en *"en el corazón del casco histórico"* (bewijstype 1). Idealista zet er als zone **Centro Ciudad** bij en de pin staat op 38,7879 / 0,1635 — de oude kern van Jávea, ruim vier kilometer van Granadella en Balcón al Mar (bewijstype 3).

Waar de fout vandaan komt is te zien: Idealista geeft `typology: countryHouse` met `subTypology: casaDePueblo`. "Country house" is de moederklasse waar het dorpshuis onder valt. Wie alleen de bovenste laag leest, zoekt het pand buiten het dorp.

Dat is geen etiketfout maar de hele som. Uit onze eigen metingen van 15-09-2026:

| Zone-reeks (eigen meting 15-09-2026) | n | mediaan €/m² |
|---|---|---|
| granadella_balcon · villa_renovated | 43 | **6.081** |
| centro · townhouse_renovated | 8 | **2.872** |

De 6.081 €/m² in het scenario is exact de mediaan van de **villa's in Granadella/Balcón al Mar**. Het systeem heeft de verkeerde zone-sleutel getrokken en daarna keurig doorgerekend.

---

## 2. Welke vierkante meters? Antwoord: onbekend — en 298 is verzonnen

Dit is onze grootste eigen foutbron, en hier gaat het twee keer mis.

**De advertentie spreekt zichzelf tegen** (bewijstype 7):

| Plaats in de advertentie | Opgave |
|---|---|
| Kenmerkenblok | **310 m² construidos** |
| Beschrijvende tekst | *"una superficie total de **268 m² construidos** en sus tres plantas"* |

Verschil: 42 m², 16% van de kleinste opgave. Idealista rekent zijn € 1.603/m² over 310; over 268 wordt dat € 1.854/m² (bewijstype 5).

**Het scenario rekent met 298 m², "gecorrigeerd van 310".** Dat getal staat nergens. Het is niet 310 en niet 268. Er is geen bron, geen meting en geen redenering die op 298 uitkomt. Een correctie die niet naar de wél genoemde tegenopgave (268) toe beweegt maar naar een eigen tussenwaarde, is een aanname die zich voordoet als een correctie.

**Wat er verder niet in staat** (alles bewijstype 7):

- Het API-veld heet `areas.usableArea` en staat op 310, terwijl het zichtbare label bij datzelfde getal "construidos" zegt. Construida en útil zijn niet hetzelfde; in oud metselwerk scheelt dat al gauw 10–15%. Een aparte superficie útil ontbreekt.
- Of de **terraza superior** meetelt. De tekst noemt hem; het veld `hasTerrace` staat op `false`.
- Of de **patio interior** meetelt.
- Of het **local comercial** op de begane grond in de 310 of de 268 zit. Dit is de kern: commerciële m² verkopen per m² heel anders dan woon-m².

**Wat je hieruit mag gebruiken:** de laagste, expliciet onderbouwde opgave — 268 m² construida over drie verdiepingen — met het voorbehoud dat een onbekend deel daarvan local comercial is. Niet 310, en zeker niet 298.

---

## 3. Planklasse en vergunning

| Punt | Stand | Bewijs |
|---|---|---|
| Grondklasse | Bebouwde historische kern, IBI € 319 per jaar (stedelijk). Vrijwel zeker **suelo urbano consolidado** — maar zonder certificado urbanístico blijft dat ONBEKEND | 1 / 7 |
| Urbanisatie niet opgeleverd | **Niet aan de orde** — dit is een bestaand pand in de oude kern, geen verkaveling | 3 |
| Aval bancario / bankgarantie | **Niet aan de orde** — bestaande bouw, geen koop op plan | 3 |
| Licencia de obra | Niet genoemd, niet aanwezig | 7 |
| Erfgoedbescherming | **ONBEKEND en doorslaggevend.** Pand uit 1930 in piedra tosca, in het casco histórico. Of het in het Catálogo de Protecciones van Xàbia staat en met welke graad, is uit openbare bronnen niet vast te stellen | 7 |
| Referencia catastral | Ontbreekt; `showAddress: false` | 7 |
| Bewoonbaarheid | "Sin baño", "para reformar", energiecertificaat "inmueble exento". Een geldige cédula de habitabilidad is er vermoedelijk niet | 1 / 7 |

**Goed nieuws voor Jan:** zijn twee harde uitsluitingen — bankgarantie en een niet-opgeleverde urbanisatie — raken dit object niet. Het valt niet daarop af.

**Maar de exit wel.** Het hele scenario leunt op het verhaal van de aanbieder: *"espacio necesario para desarrollar hasta 16 habitaciones"*, "hotel boutique". Openbare bron, Ayuntamiento de Xàbia en regionale pers (peildata 19-09-2025 en 06-02-2026, bewijstype 2): Xàbia heeft de afgifte van informes de compatibilidad urbanística voor toeristische woningen in plurifamiliaire typologie opgeschort en verlengt die opschorting; bij het opheffen komt er een plafond per wijk van **7% in het historisch centrum**, tegen 15% in Duanes en 25% in Tossalet. Juist het centrum is het strengst geregeld, juist omdat daar bewoners wegtrekken. Of dit pand binnen die 7% past, is ONBEKEND en niet door ons te bepalen.

---

## 4. De verkoopprijs per m²: drie echte voorbeelden uit dezelfde kern

Gezocht op 18-09-2026 met `search_properties` in district Centro Ciudad, Jávea/Xàbia, daarna elk voorbeeld apart opgehaald met `property_detail`. Dit zijn **vraagprijzen**, geen transactieprijzen.

| # | Code | Wat het is | Vraagprijs | m² | €/m² |
|---|---|---|---|---|---|
| 1 | 110749062 | Casco antiguo, bouwjaar 1945, 3 verdiepingen, 5 kamers / 5 badkamers, **lift net geïnstalleerd**, draaiend boutiquehotel, zeezicht, "buen estado" | € 995.000 | **268** | **3.713** |
| 2 | 109165181 | Calle d'Avall, 50 m van de kerk San Bartolomé, 4 verdiepingen, 5 en-suite kamers, **lift en gehandicaptenvoorziening, hostel-licentie**, draaiende hotelonderneming inbegrepen | € 995.000 | 280 | **3.554** |
| 3 | 112342242 | **Calle Major — dezelfde straat**, casa de pueblo uit 1806, 600 m² over 3 verdiepingen, twee huizen op één escritura, 10 kamers / 9 badkamers, werkende bar beneden, "buen estado" | € 1.195.000 | 600 | **1.992** |

Voorbeeld 1 is de zuiverste toets die er is: **exact dezelfde 268 m², in dezelfde oude kern, maar dan kláár** — gerenoveerd, met lift, met vijf badkamers, als draaiend hotel. Vraagprijs € 995.000.

Ons scenario zegt dat hetzelfde product na renovatie **€ 1.812.138** opbrengt. Dat is 82% boven een afgewerkt, draaiend, vergund voorbeeld op loopafstand.

Dit stemt overeen met onze eigen meting van 15-09-2026 (`H01-comparables-centro.md`): gerenoveerde dorpshuizen in de casco vragen 2.383–3.967 €/m², mediaan 2.872. Diezelfde notitie waarschuwt bovendien: *grote huizen (321–729 m²) zitten aan de onderkant (2.383–2.730 €/m²) — m² boven de ±250 worden in de casco minder betaald.* Voorbeeld 3 bewijst dat: 600 m² aan de Calle Major haalt maar 1.992 €/m².

**Conclusie: 6.081 €/m² is niet te verdedigen. Realistisch is 2.900–3.700 €/m², en dat bovenste getal hoort bij een product mét lift en mét draaiende exploitatie.**

---

## 5. Is 1.000 €/m² renovatie genoeg? Nee

Wat er werkelijk moet gebeuren (bewijstype 1, uit de advertentie zelf):

- Bouwjaar **1930**, dragend metselwerk in piedra tosca. Oude kernen hebben ondiepe fundering zonder gewapend beton — scheuren, verzakking en optrekkend vocht zijn het normale beeld, geen uitzondering.
- **Nul badkamers.** "Sin baño". Alle sanitair, riolering en leidingwerk moet van nul af aan in een stenen casco worden ingebracht.
- Alle installaties nieuw, drie verdiepingen plus dakterras, plus een patio.
- Wil het product de comparables uit §4 evenaren, dan hoort er een **lift** in — beide afgewerkte voorbeelden hebben er een, en voorbeeld 2 noemt de lift expliciet als onderdeel van de vergunde hostelstatus.
- Bij omzetting naar logies of meerdere eenheden komen daar CTE-eisen bij: brandveiligheid, geluidsisolatie, toegankelijkheid.
- Werken in de Calle Mayor: smalle straat, geen bouwplaatsopslag, aan- en afvoer per klein materieel. Dat is een toeslag, geen detail.
- Erfgoedbescherming is ONBEKEND. Als het pand gecatalogiseerd blijkt, komen gevelbehoud, materiaalvoorschriften en een langere vergunningsroute erbij.

Openbare marktcijfers voor 2026 (bewijstype 2, Spaanse aannemers- en offerteportalen): een reforma integral van een casa de pueblo loopt van circa 600 €/m² bij een gezonde structuur en alleen afwerking, tot circa 1.500 €/m² wanneer structuur, installaties en afwerking alle drie meemoeten; bij zeer oude woningen met structureel herstel wordt 1.400 €/m² overschreden.

Dit pand zit aan de **bovenkant** van dat spectrum: structuur uit 1930, installaties vanaf nul, sanitair vanaf nul. Het scenario rekent met 1.000 €/m² — onder het midden van de bandbreedte, voor een geval dat aan de zware kant ligt. Reken op **1.400–1.800 €/m²**, plus lift, plus honoraria architect en aparejador, plus ICIO en vergunningsleges, plus onvoorzien. Dat laatste is in een pand uit 1930 geen post maar een zekerheid.

Bij 268 m²: het scenario zet € 268.000 apart waar € 375.000–480.000 realistischer is, vóór lift en bijkomende kosten.

---

## 6. Wat er van de som overblijft

Herrekening met dezelfde structuur maar met houdbare invoer. Alle aannames staan erbij (bewijstype 5).

| Post | Scenario systeem | Herrekening |
|---|---|---|
| Oppervlakte | 298 m² (bron ontbreekt) | 268 m² construida (laagste onderbouwde opgave) |
| Verkoopprijs per m² | 6.081 (Granadella-villa's) | 3.634 (mediaan van de twee afgewerkte hotelcomparables) |
| **Verkoopopbrengst** | **€ 1.812.138** | **± € 974.000** |
| Renovatie | 1.000 €/m² = € 298.000 | 1.400 €/m² = € 375.200, excl. lift |
| Aankoop | € 497.000 | € 497.000 |
| Aankoopkosten (ITP 10% + notaris/registratie/advies, ± 13%) [te verifiëren] | niet zichtbaar | € 64.600 |
| Honoraria, ICIO, lift, onvoorzien (± 15% over bouw) | niet zichtbaar | ± € 56.000 |
| **Totaal erin** | — | **± € 993.000** |
| **Resultaat bij vraagprijs** | **+ € 644.612** | **± € 0, vóór financiering, 15 maanden doorlooptijd en verkoopkosten** |

Het positieve resultaat verdwijnt volledig. Niet omdat de renovatie tegenvalt, maar omdat de opbrengstkant met de prijzen van een andere wijk was ingevuld.

**Maximale koopprijs.** Het scenario zegt € 784.000. Met een opbrengst van € 974.000, bouwkosten van € 375.200, bijkomende kosten van € 56.000 en een aangenomen marge-eis van 20% over de totale kostprijs, blijft er voor grond en gebouw inclusief aankoopkosten circa € 380.000 over — een koopprijs van ruwweg **€ 300.000 tot € 350.000**. Dat is een factor 2,2 tot 2,6 onder wat het systeem als plafond noemt, en het ligt 30% onder de huidige vraagprijs.

Jan's rendementseis is nog niet vastgelegd (staat open in het projectgeheugen). De 20% hierboven is daarom een benoemde aanname, geen kader.

---

## 7. Het punt dat dit plan het snelst onderuit haalt

**De verkeerde wijk.** Eén foute zone-sleutel — `granadella_balcon` in plaats van `centro` — verdubbelt de aangenomen verkoopprijs per m² en is in zijn eentje goed voor het volledige verschil tussen "+ € 644.612" en "ongeveer nul". Alle andere bevindingen in dit rapport maken het beeld nog wat slechter, maar deze ene bepaalt de uitkomst.

Het bewijs ligt binnen handbereik en is niet te weerspreken: **hetzelfde aantal vierkante meters, in dezelfde oude kern, maar dan af, met lift en als draaiend hotel, staat te koop voor € 995.000** (110749062). Ons systeem wil er € 1.812.138 voor maken.

---

## 8. Wat wél standhoudt

Eerlijkheidshalve, want niet alles is mis:

- Het object bestaat, staat live (`outcome: active`) en de vraagprijs klopt (bewijstype 3).
- De prijs per m² van de **aankoop** is voor de casco laag: 1.603 €/m² over 310, of 1.854 €/m² over 268, tegen een mediaan van 2.872 voor gerenoveerd. Er zit dus wel degelijk een bruto gat.
- Jan's twee harde uitsluitingen (bankgarantie, niet-opgeleverde urbanisatie) zijn hier niet aan de orde.
- Eerder vastgelegd: de vraagprijs is met 16% gedaald (eigen meting 14-09-2026, `R15-kandidaten-javea-live.md`). Op zichzelf geen bewijs van verkoopdruk.

Het gat is er. Het is alleen ongeveer een derde van wat het systeem ervan maakt, en het moet een renovatie dekken die ongeveer anderhalf keer zo duur is als begroot. Daarmee blijft er niets over.

---

## ⏸️ ACTIE VOOR JAN

1. **Eerste vraag aan de verkoper** (zie ook de samenvatting): vraag de **nota simple en de referencia catastral** op. Daarmee is in één klap duidelijk hoeveel m² construida er per verdieping geregistreerd staat — 310 of 268 — en hoeveel daarvan het local comercial is.
2. Laat bij het Ayuntamiento de Xàbia een **certificado urbanístico** trekken en vraag daarbij expliciet of het pand in het **Catálogo de Protecciones** staat en met welke graad. Dit is de enige post die de renovatiebegroting nog verder kan laten ontsporen.
3. Vraag bij dezelfde gang na wat de stand is van de **toeristische vergunningen in het casco histórico** (het 7%-plafond). Zonder dat is het hotelverhaal van de aanbieder alleen een verhaal.
4. **Voor het systeem, niet voor de verkoper:** de zonetoekenning van dit object moet worden hersteld in `kader/comparables.json` en in `rapporten/dossiers/110616065.html`. En de regel die `countryHouse` naar een buitengebiedzone vertaalt, moet naar `subTypology` kijken — `casaDePueblo` hoort bij `centro`. Elk ander object met dezelfde typologie moet opnieuw langs.

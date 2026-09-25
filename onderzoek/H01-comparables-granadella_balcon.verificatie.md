# H01 — Tegenspraak op de vergelijkingsprijzen zone `granadella_balcon`

**Gecontroleerd bestand:** `onderzoek/H01-comparables-granadella_balcon.md` (versie 15-09-2026 10:41–10:52; niet aangepast).
**Rol:** tegenspreker. **Controledatum:** 15-09-2026. **Bron:** officiële Idealista-assistent (MCP `property_detail` + `search_properties`, country es, locale es-ES, maxResults 50). Bewijstype 3 (zelf gezien in de tool) voor prijs, m² en advertentietekst; 5 (eigen berekening) voor de kengetallen.
Alle bedragen zijn **vraagprijzen**, geen transactieprijzen. Kwartielen: lineaire interpolatie, zelfde methode als het origineel.

## 1. Oordelentabel

| Reeks | Origineel (n · p25 · mediaan · p75) | Oordeel | Gecorrigeerd (n · p25 · mediaan · p75) | Kern |
|---|---|---|---|---|
| **villa_renovated** | 34 · 4.851 · 6.248 · 7.378 | **Weerlegd** (n en kwartielen; mediaan houdt stand) | **43 · 4.746 · 6.081 · 7.248** | 3/3 voorbeelden kloppen; rekenkunde klopt; eigen zoekmediaan 6.155 (−1,5 %). Maar Granadella–Costa Nova is maar half bevraagd: 9 gerenoveerde/moderne objecten ontbreken. |
| **villa_new** | 26 · 4.178 · 4.727 · 6.651 | **Weerlegd** (n en kwartielen; mediaan houdt stand) | **31 · 4.139 · 4.750 · 6.645** | 3/3 voorbeelden kloppen; rekenkunde klopt; eigen zoekmediaan 4.773 (+1,0 %). In Granadella ontbreken 5 nieuwbouwobjecten. |
| **apartment_renovated** | 0 · — · — · — ("niet van toepassing") | **Weerlegd** | **1 · 4.906 · 4.906 · 4.906** | Er ís aanbod: één gerenoveerde bungalow (Granadella). **Te klein voor een betrouwbare mediaan.** |
| **apartment_new** | 0 · — · — · — ("niet van toepassing") | **Weerlegd** | **5 · 4.611 · 4.885 · 6.304** | Vijf nieuwbouwappartementen in Portichol–Balcón al Mar; vier daarvan in één complex. Grensgeval: formeel n = 5, in feite twee projecten. |
| **townhouse_renovated** | 0 · — · — · — (3 adosados "ter informatie") | **Weerlegd** | **5 · 3.611 · 4.815 · 5.000** | De drie adosados uit §6 van het origineel plus twee; vrijwel allemaal één renovatieproject van 260.000 €. Echte n ligt tussen 3 en 5. **Te klein/te geclusterd voor een betrouwbare mediaan.** |

**Kern voor Jan:** de hoofdcijfers voor villa's blijven overeind — gerenoveerd rond **6.100 €/m²** (was 6.248), nieuwbouw rond **4.750 €/m²** (was 4.727). Het origineel mist wel een flink deel van het Granadella-aanbod (het zocht daar alleen met het Idealista-label "Villas": 51 advertenties; de zone telt 133 "casas y chalets"). Voor K12 verandert de conclusie niet: 3.105 €/m² ligt ook onder de gecorrigeerde Granadella-p25 (4.369). De appartement- en rijtjeshuisreeksen zijn niet leeg, maar te dun om te gebruiken; voor K10 en K12 speelt dat geen rol.

## 2. Controle 1 — `property_detail` op voorbeelden (goedkoopste, duurste, mediaan)

| Reeks | Code | Tool: prijs / m² / €/m² | Staat volgens tool en tekst | Klopt? |
|---|---|---|---|---|
| villa_renovated (min) | 93589452 | 2.500.000 / 829 / 3.016 | "Construida en 2014"; 741 m² útiles; "Segunda mano/buen estado"; zone La Granadella – Costa Nova | ja (modern, ≥ 2014) |
| villa_renovated (max) | 110816768 | 5.500.000 / 340 / 16.176 | "ha sido renovada y mantenida con un nivel de detalle excepcional"; "Construido en 1980"; 222 m² útiles; Calle Franz Joseph Haydn | ja, maar **zwakke claim** (geen jaar, geen omvang; nieuw zwembad). Origineel vermeldt bouwjaar 1980 niet en vlagt niet. Uitschieter, raakt de mediaan niet. |
| villa_renovated (mediaan) | 106825516 | 2.700.000 / 432 / 6.250 | "construida en 2016"; "Construido en 2016"; zone Granadella | ja |
| villa_new (min) | 104311957 | 1.550.000 / 485 / 3.196 | promotie Villa Aurea, `notFinished`, "will be delivered as a turnkey project"; 235 m² útiles | ja (project). "met licentie" staat niet in de detailtekst **[te verifiëren]** |
| villa_new (max) | 107915996 | 2.145.000 / 209 / 10.263 | promotie "Villa BOUGAINVILLE", `notFinished`, status newdevelopment; Torre Ambolo 5 | ja |
| villa_new (mediaan) | 108643000 | 1.520.000 / 320 / 4.750 | promotie Villa Onyx, `notFinished`; Calle del Escabusso 35 (Granadella) | ja |

Voor apartment_renovated, apartment_new en townhouse_renovated noemt het origineel geen reeksvoorbeelden; die zijn via de zoekopdrachten in §3 gecontroleerd.

Geen van de zes geopende objecten is "para reformar". In alle zes is `priceByArea` = vraagprijs / `size`.

## 3. Controle 2 — onafhankelijke zoekopdrachten

| # | Query (tool koos) | Totaal / ontvangen | Uitkomst |
|---|---|---|---|
| A | casas y chalets reformados en Portichol (Portichol – Balcón al Mar; filter "Usada / buen estado") | 155 / 50 | 18 gerenoveerde/moderne objecten na ontdubbeling, allemaal al in het origineel. Mediaan **6.412** (origineel Balcón-deelreeks 6.306: +1,7 %). Eén grensgeval dat het origineel nergens noemt: 108474336 ("diseño vanguardista", 2.200.000 / 320 = 6.875; alleen claim aanbieder). Eén niet-vermelde doublure van Xicoria 4: 112437039 (1.350.000 / 222). |
| B | casas y chalets reformados en La Granadella – Costa Nova ("Usada / buen estado") | 117 / 50 | Toonde advertenties die niet in het origineel staan → aanleiding voor C–E. |
| C–E | casas y chalets en venta en La Granadella – Costa Nova, < 800.000 / 800.000–1.300.000 / > 1.300.000 | 41 + 48 + 44 = **133** / 133 | Volledige dekking van de zone. **100 van de 133 advertenties komen in het origineel niet voor** (het zocht daar alleen met het filter "Villas"). Alle 18 Granadella-objecten uit het origineel zitten erin. |
| F | casas y chalets de obra nueva en Portichol – Balcón al Mar | 11 / 11 | Alle 11 al in het origineel. Mediaan **4.773** (+1,0 % t.o.v. 4.727). |
| G | pisos y apartamentos … Portichol – Balcón al Mar | 0 | Niet bruikbaar: de tool voegde zelf "Con balcón" + "Vistas al mar" toe. |
| H | pisos, apartamentos y bungalows … Portichol | 10 / 10 | 5 nieuwbouwappartementen, 2 gerenoveerde "adosados" met type *flat*, 2 onafgewerkte studio's, 1 zonder claim. |
| I | pisos y apartamentos … La Granadella – Costa Nova | 3 / 3 | 1 gerenoveerde bungalow; 1 ático zonder claim; 1 "dúplex" dat eigenlijk een villa is. |
| J | adosados y pareados … Portichol – Balcón al Mar | 4 / 4 | De 3 gerenoveerde adosados uit §6 van het origineel + Apartamentos Halcón (geen renovatieclaim). |

**±15 %-toets:** villa_renovated: eigen selectie (A + C–E, n = 36) mediaan 6.155 → −1,5 % ✔. villa_new: F → +1,0 % ✔ (let op: F dekt alleen de obra-nueva-promoties in Balcón al Mar).

## 4. Wat ontbreekt — de onderbouwing van de correcties

### 4.1 villa_renovated: 9 objecten erbij (allemaal La Granadella – Costa Nova, tool-status "good")

| Code | Vraagprijs € / m² | €/m² | Claim in advertentietekst | Opmerking |
|---|---|---|---|---|
| 107585471 | 469.000 / 125 | 3.752 | "totalmente renovada y lista para entrar a vivir" (Jada Residence, 3 slk) | doublure 108578034 |
| 112555201 | 675.000 / 157 | 4.299 | "renovada con buen gusto", oorspronkelijk jaren 80 | — |
| 112221394 | 599.950 / 131 | 4.580 | jaren 80, "cuidadosamente renovada por los actuales propietarios" | ander huis dan 112555201 (andere m², ligging) |
| 108423317 | 1.250.000 / 250 | 5.000 | "completamente reformada en 2018" | La Guardia |
| 111990638 | 965.000 / 172 | 5.610 | "totalmente reformada con nuevas carpintería, pavimentos y sanitarios" | vermoedelijk zelfde huis als 111285031 en 110416947 (965.000 / 173) |
| 107928090 | 850.000 / 146 | 5.822 | "bellamente renovada", maar "actualmente en proceso de renovación completa" | **[belofte]**, zoals 101444351 in het origineel |
| 108397065 | 1.875.000 / 301 | 6.229 | "Reformada con una sensibilidad exquisita" | — |
| 111709121 | 995.000 / 151 | 6.589 | "En 2021, la villa fue completamente renovada" | — |
| 112363501 | 2.495.000 / 302 | 8.262 | "Construida en 2014" | mogelijk zelfde huis als 110880541 (2.495.000 / 400 m²); met 400 m² wordt het 6.238 en p75 7.150, mediaan gelijk |

URL's (verbatim uit de tool):
https://www.idealista.com/es/inmueble/107585471/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail
https://www.idealista.com/es/inmueble/112555201/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail
https://www.idealista.com/es/inmueble/112221394/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail
https://www.idealista.com/es/inmueble/108423317/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail
https://www.idealista.com/es/inmueble/111990638/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail
https://www.idealista.com/es/inmueble/107928090/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail
https://www.idealista.com/es/inmueble/108397065/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail
https://www.idealista.com/es/inmueble/111709121/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail
https://www.idealista.com/es/inmueble/112363501/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail

**Niet toegevoegd (bewust):** 109448652/109367461 ("villa… espaciosa, moderna", 795.000 / 220 = 3.614: alleen claim aanbieder; met dit object en 108474336 erbij: n = 45, mediaan 6.081, p75 7.226); 104830910/105746182 (bouwjaar 2007); 106837987 (alleen keuken en baden); 111990776, 110286199/110435758 (alleen zwembad); 112419922, 109184130, 112319569, 111298706 (te renoveren); 111743299 ("impecablemente mantenida", geen renovatie); de reeks van negen advertenties à 625.000 / 150 m² (alleen "moderno" over de keuken).

**Deelreeksen na correctie:** villa_renovated_granadella n = 18 · p25 4.369 · mediaan 5.764 · p75 6.504 (was 9 · 4.120 · 5.777 · 7.226). villa_renovated_strikt (de 12 gevlagde objecten van het origineel en de belofte 107928090 eruit) n = 30 · p25 4.986 · mediaan 6.155 · p75 7.026 (was 22 · 5.305 · 6.248 · 7.220).

### 4.2 villa_new: 5 objecten erbij (La Granadella – Costa Nova)

| Code | Vraagprijs € / m² | €/m² | Claim | Status |
|---|---|---|---|---|
| 111488078 | 1.495.000 / 420 | 3.560 | "villa de nueva construcción casi terminada" | bijna af |
| 112559160 | 1.050.000 / 291 | 3.608 | "Villa de obra nueva", Trencall, oplevering 2027, renders | project; doublure 112508408 |
| 112283552 | 1.050.000 / 197 | 5.330 | "obra nueva a estrenar – finalización prevista: Enero de 2027" | in aanbouw |
| 112558538 | 1.225.000 / 226 | 5.420 | "Ya ha comenzado la construcción… prevista para el verano de 2027" | in aanbouw |
| 110264143 | 2.500.000 / 356 | 7.022 | "villa de lujo de nueva construcción" | tool-status "good" (zoals 111169779 in het origineel) |

https://www.idealista.com/es/inmueble/111488078/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail
https://www.idealista.com/es/inmueble/112559160/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail
https://www.idealista.com/es/inmueble/112283552/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail
https://www.idealista.com/es/inmueble/112558538/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail
https://www.idealista.com/es/inmueble/110264143/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail

Deelreeks villa_new_granadella na correctie: n = 14 · p25 3.677 · mediaan 4.278 · p75 5.185 (was 9 · 3.686 · 4.242 · 4.455). Van de vijf zijn er nul aantoonbaar af; de kanttekening "nieuwbouw is grotendeels papier" wordt dus sterker.

### 4.3 apartment_renovated, apartment_new, townhouse_renovated

- **apartment_renovated (n = 1):** 111264150, La Granadella – Costa Nova, type *flat*: "bungalow totalmente reformado", 260.000 / 53 = 4.906. Ligt dicht bij de gerenoveerde adosados van 260.000 € in Balcón al Mar en kan bij hetzelfde project horen **[te verifiëren]**. https://www.idealista.com/es/inmueble/111264150/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail
- **apartment_new (n = 5), Portichol – Balcón al Mar:** 112497428 obra nueva 488.500 / 125 = 3.908; 111289156 "a estrenar… obra nueva" 415.000 / 90 = 4.611; 110908436 idem 425.000 / 87 = 4.885; 110085751 "a estrenar" 435.000 / 69 = 6.304; 110085760 "residencial completamente nuevo" 415.000 / 65 = 6.385. De laatste vier liggen in één complex (Residencial Unic, zelfde aanbieder). Niet meegeteld: 111916553 (geen nieuwbouw- of renovatieclaim).
  https://www.idealista.com/es/obra-nueva/112497428/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail
  https://www.idealista.com/es/inmueble/111289156/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail
  https://www.idealista.com/es/inmueble/110908436/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail
  https://www.idealista.com/es/inmueble/110085751/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail
  https://www.idealista.com/es/inmueble/110085760/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail
- **townhouse_renovated (n = 5):** 111904945 Santorini 260.000 / 73 = 3.562; 110306838 "adosado completamente reformado" (tool-type *flat*) 260.000 / 72 = 3.611; 110850566 "recién renovados" 260.000 / 54 = 4.815 (doublure 110799770, zelfde prijs en m², "renovado en 2025"); 109404683 Santorini 260.000 / 52 = 5.000; 110158525 Jada Residence 2 slk, "completamente renovado" 399.000 / 71 = 5.620 (Granadella; doublure 112169252, daar "Chalet adosado" genoemd). 110306838 is mogelijk dezelfde unit als 111904945 (72/73 m²); dan n = 4. Vier van de vijf komen uit één renovatieproject met één prijs. Niet meegeteld: 105453470 Apartamentos Halcón (geen renovatieclaim).
  https://www.idealista.com/es/inmueble/110306838/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail
  https://www.idealista.com/es/inmueble/110158525/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail

## 5. Controle 3 — ontdubbeling en rekenkunde

**Rekenkunde: klopt.** Alle acht rijen van de conclusietabel zijn nagerekend op de 34 + 26 voorbeeldwaarden, zowel met de volle quotiënten als met de afgeronde €/m². Afwijkingen van hooguit 1 € (p75 7.378 tegenover 7.378,5 of 7.379; strikt p75 7.220 tegenover 7.220,5; afgebouwd p75 6.363 tegenover 6.363,25) zijn afronding. Elke €/m² in de tabellen is gelijk aan vraagprijs / m². Er staat geen code twee keer in de lijsten, en ook geen combinatie van prijs en m² twee keer.

**Ontdubbeling binnen het gevonden aanbod: klopt**, met vier aanvullingen zonder invloed op de cijfers:
- 112437039 (1.350.000 / 222, "villa moderna", El Portitxol) is een vierde advertentie van Xicoria 4 (112322544).
- 108606776 en 108516329 (3.150.000 / 282) zijn extra doublures van 105516589. 108606776 zegt letterlijk "Totalmente renovada", dus dat object rust niet alleen op de claim "contemporáneo".
- 111284187 (1.350.000 / 220, "villa contemporánea", urbanización La Cala, label Granadella) is dezelfde villa als 111003348 (villa_new, label Balcón al Mar). De ontdubbelregel van het origineel ("zelfde zone") mist zulke zone-overschrijdende doublures; hier zou dat een dubbeltelling hebben opgeleverd als het object gevonden was.
- 111365184, 112547074 en 112246709 (4.500.000 / 677) zijn extra doublures van Villa Granadella (111917256).

**Volledigheid: klopt niet.** Het origineel meldt "Granadella/Costa Nova telt 51 villa's… 51 unieke advertenties gezien". Dat klopt alleen voor het Idealista-label "Villas". Zonder dat label telt de zone 133 casas y chalets, en daaronder zitten de 9 + 5 objecten uit §4. Voor Balcón al Mar is het origineel wél via "casas y chalets" in prijsbanden bevraagd; steekproef A leverde daar geen gemist gerenoveerd object op, alleen het grensgeval 108474336.

## 6. Overige bevindingen

1. **`kader/comparables.json` loopt achter.** Voor `granadella_balcon` staan daar nog de cijfers van de run van 09:38 (villa_renovated n = 31, mediaan 6.250; villa_new n = 20, mediaan 4.464), niet die van het gecontroleerde bestand (34 / 6.248 en 26 / 4.727). Welke versie de rekenaar gebruikt, is dus niet de versie die hier is gecontroleerd. (Niet aangepast; buiten deze opdracht.)
2. **110816768 (max van villa_renovated)** rust op een zwakke renovatieclaim en heeft bouwjaar 1980. Voorstel: vlag [claim aanbieder]. De mediaan verandert daar niet door.
3. **Momentopname.** Alle controles zijn gedaan op 15-09-2026. Advertenties en prijzen wisselen; kleine verschillen met een latere herhaling zijn normaal.
4. Telefoonnummers en namen van particulieren staan wel in de tooluitvoer, maar zijn niet overgenomen.

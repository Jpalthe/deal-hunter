# H01 — Vergelijkingsprijzen El Rafalet · Pinomar–Pinosol · La Lluca–Tarraula (Jávea)

**zone_key:** `rafalet_pinosol` · **kandidaten:** K08 (perceel El Rafalet, 90705084), K09 (perceel Pinosol, 109915149), K05 (chalet Partida Tosal, 97576395 — grenszone)
**Bron:** officiële Idealista-assistent (MCP `search_properties` + `property_detail`), locale es-ES, land es · **controledatum:** 15-09-2026 · **bewijstype:** 1 (tool-uitvoer, letterlijk) voor prijs, m², zone en bouwjaar; 3 (eigen beoordeling van de advertentietekst) voor de indeling "gerenoveerd/modern/nieuw".
**Let op:** alle bedragen zijn **vraagprijzen** (asking prices) van lopende advertenties op 15-09-2026. Het zijn géén transactieprijzen en géén marktwaarde. €/m² = vraagprijs ÷ m² gebouwd zoals de tool die geeft (veld `size`).

---

## 1. Conclusie in drie regels

1. **Gerenoveerde of moderne villa's** in de drie zones vragen op 15-09-2026 een **mediaan van 4.807 €/m²** (n = 20, p25–p75 4.147–5.845, spreiding 3.190–9.203). Zonder de twee grote fincas blijft de mediaan 4.807; de p75 zakt naar 5.662.
2. **Nieuwbouw** is dun gezaaid: 9 unieke objecten in drie zones, mediaan **5.717 €/m²** met een enorme spreiding (3.307–9.750). Drie daarvan zijn op-plan-aanbiedingen (perceel + licentie, of oplevering pas in 2027). Zonder die drie: mediaan **4.573** (n = 6, 3.307–9.750).
3. Per zone (gerenoveerd/modern): El Rafalet mediaan 5.660 (n = 5), Pinomar–Pinosol 4.760 (n = 7), La Lluca–Tarraula 4.546 (n = 8). Die steekproeven zijn te klein om het verschil als "zoneprijs" te lezen; ze hangen aan enkele objecten.

Wat dit betekent voor de kandidaten staat in §7 — zonder waarderingsclaim, alleen wat de cijfers laten zien.

---

## 2. Werkwijze (kort, controleerbaar)

- **Zoekopdrachten.** De zes gevraagde vrije-tekstqueries ("villa moderna reformada en Jávea Rafalet, Pinosol, Pinomar, La Lluca, Tarraula", "chalet reformado en …", "villa de diseño …", "obra nueva …", "villa a estrenar …", "villa de nueva construcción …") zijn letterlijk uitgevoerd (CHALET, SALE, maxResults 50). Bevinding (bewijstype 1, vandaag): de assistent geocodeert een query met meerdere wijknamen naar **één** wijk — steeds "La Lluca – La Tarraula" — en vertaalt "reformado/reformada" naar het filter **"Usada / buen estado"**, niet naar "gerenoveerd". "A estrenar" en "nueva construcción" worden het filter "Obra nueva" + subtype "Villas" (0 resultaten). Daarom zijn de drie zones **apart** bevraagd en is elke zone met meer dan 50 resultaten **opgesplitst op prijsband** (≤ 900.000 · 900.000–1.500.000 · > 1.500.000).
- **Dekking.** Chalets "buen estado" per zone volgens de tool: El Rafalet 22/22 (volledig), Pinomar–Pinosol 24 + 24 + 24 = 72 (totaal 71 volgens de tool; overlap op de bandgrens 1.500.000), La Lluca–Tarraula 21 + 33 + 16 = 70/70 (volledig), Partida Tosal 38/38 (volledig). Filter "obra nueva" per zone: Rafalet 1, Pinosol 2, La Lluca 1, Tosal 1. Totaal **208 unieke advertentiecodes** over vier zones in de scratchpad-dataset.
- **Indeling.** Elke advertentietekst is automatisch doorzocht op renovatie-, nieuwbouw-, "modern"- en uitsluitingssignalen (Spaans én Engels) en daarna **handmatig** beoordeeld. Regel: opgenomen als de tekst zegt dat de **villa zelf** (niet alleen keuken of zwembad) `reformada / renovada / modernizada / actualizada en su totalidad` is, of dat het een moderne/hedendaagse villa is met bouwjaar ≥ 2015 of expliciete "arquitectura contemporánea". Uitgesloten: `para reformar / a reformar / requiere reforma / potencial de renovación / oportunidad de restauración / proyecto`, status `renew`, objecten waarvan de prijs een extra bouwperceel of een tweede woning omvat, en zachte termen zonder bewijs ("cocina moderna", "hogar moderno", "villa de diseño" zonder jaar).
- **Deduplicatie.** Zelfde prijs + zelfde m² + zelfde zone = één object. Aanvullend handmatig samengevoegd waar de m² tussen advertenties van hetzelfde object afwijkt (Rafalet 850.000: 236/240/270 m²; La Lluca 3.450.000: 1.000/1.100/1.350 m²; Pinosol 1.685.000: 370/380 m²; La Lluca 1.795.000: 359/360 m²; Rafalet 1.088.000: 329/330 m²). In die gevallen is de m² genomen van de advertentie die met `property_detail` is gecontroleerd.
- **Bevestiging.** `property_detail` is opgevraagd voor **42 objecten**: alle 20 in `villa_renovated`, alle 9 in `villa_new`, alle 7 in de Tosal-reeksen, plus 6 twijfelgevallen die daarna zijn uitgesloten (102167151, 112031038, 112344706, 112273590, 108549029) of nogmaals bevestigd. Het veld "Construido en …" en de volledige tekst zijn gebruikt om renovatie/nieuwbouw te bevestigen.

---

## 3. Statistieken per reeks (€/m² gebouwd, vraagprijzen, 15-09-2026)

| Reeks | n (unieke objecten) | min | p25 | mediaan | p75 | max | Opmerking |
|---|---|---|---|---|---|---|---|
| `villa_renovated` | 20 | 3.190 | 4.147 | **4.807** | 5.845 | 9.203 | gerenoveerde of moderne villa’s, drie zones samen |
| `villa_renovated (zonder 2 fincas)` | 18 | 3.190 | 4.250 | **4.807** | 5.662 | 9.203 | zonder 112342262 (1.000 m² op 5.850 m²) en 108679725 (526 m² op 1 ha) |
| `villa_new` | 9 | 3.307 | 3.868 | **5.717** | 8.185 | 9.750 | nieuwbouw incl. 3 op-plan-aanbiedingen |
| `villa_new (zonder op plan)` | 6 | 3.307 | 3.637 | **4.573** | 5.607 | 9.750 | zonder 112093850 (perceel + licentie), 111718472 (14 mnd na start) en 112158635 (finca, juni 2027) |
| `villa_renovated_tosal` | 6 | 3.176 | 3.869 | **4.726** | 6.897 | 9.342 | grenszone K05 (Partida Tosal – Zona dels Castellans), apart gehouden |
| `villa_new_tosal` | 1 | 6.848 | 6.848 | **6.848** | 6.848 | 6.848 | één object; geen spreiding |

Per zone binnen `villa_renovated`: El Rafalet n = 5, mediaan 5.660 (3.602–6.878) · Pinomar–Pinosol n = 7, mediaan 4.760 (3.216–9.203) · La Lluca–Tarraula n = 8, mediaan 4.546 (3.190–7.510).

Percentielen lineair geïnterpoleerd over de gesorteerde waarden (methode "linear"). Alle waarden afgerond op hele euro's.

**Reeksen die voor deze zone niet van toepassing zijn:** `apartment_renovated` en `apartment_new` (Puerto/Arenal) en `townhouse_renovated` (casco) zijn hier niet bepaald — dit zijn villawijken zonder appartementen- of dorpshuizenaanbod in de tool-uitvoer. In de Tosal-set zaten 2 `terracedHouse`-objecten (112118494 en 111351541), waarvan het tweede feitelijk een casa de pueblo in het casco antiguo is met een foutief zonelabel; buiten beschouwing gelaten.

---

## 4. Reeks `villa_renovated` — gerenoveerde of moderne villa's (20 objecten)

| # | Code (link) | Vraagprijs € | m² gebouwd | €/m² | Bouwjaar (tool) | Zone · toelichting (bewijs uit tekst/`property_detail`) | Dubbele advertenties van hetzelfde object |
|---|---|---|---|---|---|---|---|
| 1 | [111452530](https://www.idealista.com/es/inmueble/111452530/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail) | 600.000 | 140 | **4.286** | 1955 | Rafalet · 'Completamente reformada', bouwjaar 1955, renovatiejaar onbekend, geen zwembad, perceel 1.656 m², label G | 112129659 |
| 2 | [111909291](https://www.idealista.com/es/inmueble/111909291/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail) | 850.000 | 236 | **3.602** | 1980 | Rafalet · bouwjaar 1980, 'renovada por completo en 2024', 6 slk, perceel 1.210 m² | 111064307 (270 m²), 111032018, 112152409, 112219829 (240 m²) |
| 3 | [112229028](https://www.idealista.com/es/inmueble/112229028/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail) | 1.149.000 | 203 | **5.660** | 1980 | Rafalet · bouwjaar 1980, 'recientemente renovada por completo', zonnepanelen 20 kW, perceel 822 m² | — |
| 4 | [109546138](https://www.idealista.com/es/inmueble/109546138/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail) | 1.495.000 | 264 | **5.663** | 2017 | Rafalet · MODERN: bouwjaar 2017, 'villa contemporánea', energielabel B/A, perceel 1.079 m² | — |
| 5 | [108153256](https://www.idealista.com/es/inmueble/108153256/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail) | 1.520.000 | 221 | **6.878** | onbekend | Rafalet · 'renovación completa en julio de 2026', aangeprezen als 'nueva construcción'; label C; perceel 961 m² | — |
| 6 | [109969426](https://www.idealista.com/es/inmueble/109969426/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail) | 750.000 | 152 | **4.934** | 2009 | La Lluca · bouwjaar 2009, 'renovada en 2023'; tekst noemt zelf Tosalet/urb. Cansalades; zeezicht | — |
| 7 | [111189527](https://www.idealista.com/es/inmueble/111189527/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail) | 995.000 | 205 | **4.854** | 2001 | La Lluca · bouwjaar 2001, 'recientemente reformada' (Covatelles), 179 m² nuttig, zonnepanelen | — |
| 8 | [111952972](https://www.idealista.com/es/inmueble/111952972/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail) | 1.190.000 | 373 | **3.190** | onbekend | La Lluca · 'cuidadosamente modernizada', architectuur behouden; prijs −5 % (was 1.250.000) | 111354929 |
| 9 | [110676663](https://www.idealista.com/es/inmueble/110676663/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail) | 1.495.000 | 386 | **3.873** | 2005 | La Lluca · bouwjaar 2005, hoofdvilla 'completamente renovada'; 3 woonruimtes op 4.596 m², toeristische verhuurlicentie | 111225638, 110694600, 111485403, 111503336, 111255936 |
| 10 | [110765633](https://www.idealista.com/es/inmueble/110765633/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail) | 1.695.000 | 400 | **4.238** | onbekend | La Lluca · Engelse tekst: 'completely renovated a few years ago', één laag 400 m² op 1.790 m² | — |
| 11 | [112509325](https://www.idealista.com/es/inmueble/112509325/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail) | 1.795.000 | 360 | **4.986** | 1983 | La Lluca · bouwjaar 1983; renovatie + uitbreiding LOOPT NOG (oplevering eind november); particuliere verkoper | 110843020 (359 m²) |
| 12 | [112342262](https://www.idealista.com/es/inmueble/112342262/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail) | 3.450.000 | 1000 | **3.450** | onbekend | La Lluca · finca 13 slk, 'modernizada recientemente', perceel 5.850 m² — UITSCHIETER (grootte) | 101444381, 102509721 (1.100 m²), 97471013 (1.350 m²), 111386322 (1.350 m²) |
| 13 | [108679725](https://www.idealista.com/es/inmueble/108679725/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail) | 3.950.000 | 526 | **7.510** | onbekend | La Lluca · 'totalmente renovada en 2025', finca 10.103 m² met stallen, label A — UITSCHIETER (perceel) | — |
| 14 | [112310283](https://www.idealista.com/es/inmueble/112310283/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail) | 695.000 | 146 | **4.760** | onbekend | Pinosol · 'Esta villa reformada', geen jaar (zwakste bewijs); apart appartement; perceel 759 m² | — |
| 15 | [112501089](https://www.idealista.com/es/inmueble/112501089/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail) | 799.950 | 173 | **4.624** | 2007 | Pinosol · bouwjaar 2007, 'renovación integral' 2023 incl. bekabeling/leidingen, nieuw zwembad | — |
| 16 | [111229059](https://www.idealista.com/es/inmueble/111229059/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail) | 845.000 | 130 | **6.500** | onbekend | Pinosol · 'recientemente reformada', één laag 130 m² op 1.999 m² — grondwaarde weegt zwaar | — |
| 17 | [109645331](https://www.idealista.com/es/inmueble/109645331/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail) | 849.000 | 264 | **3.216** | 1979 | Pinosol · bouwjaar 1979, 'recientemente renovada', zeezicht, verwarmd zwembad, 223 m² nuttig | — |
| 18 | [110668828](https://www.idealista.com/es/inmueble/110668828/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail) | 1.470.000 | 230 | **6.391** | 1979 | Pinosol · 'reformada' onder hoge energienormen, energielabel A, aerothermie + PV | — |
| 19 | [110895902](https://www.idealista.com/es/inmueble/110895902/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail) | 1.675.000 | 182 | **9.203** | 2026 (veld) | Pinosol · 'Villa totalmente renovada' door ontwikkelaar (Casa Luz), verkoop onder IVA, label A, veld 'construido en 2026' | — |
| 20 | [112329948](https://www.idealista.com/es/inmueble/112329948/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail) | 1.685.000 | 370 | **4.554** | 2005 | Pinosol · bouwjaar 2005, 'magníficamente reformada', 7 slk, zeezicht, apart appartement | 112158285, 112158272, 112447487, 112156107, 112161313, 112198432 (380 m²) |

Leeswijzer: "Bouwjaar (tool)" is het veld *Construido en* uit `property_detail`; "onbekend" = veld ontbreekt. Het renovatiejaar staat, waar de tekst het noemt, in de toelichting. Nrs. 1–5 El Rafalet, 6–13 La Lluca–Tarraula, 14–20 Pinomar–Pinosol.

---

## 5. Reeks `villa_new` — nieuwbouw en "a estrenar" (9 objecten)

| # | Code (link) | Vraagprijs € | m² gebouwd | €/m² | Bouwjaar (tool) | Zone · toelichting (bewijs uit tekst/`property_detail`) | Dubbele advertenties van hetzelfde object |
|---|---|---|---|---|---|---|---|
| 1 | [111918606](https://www.idealista.com/es/obra-nueva/111918606/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail) | 1.088.000 | 329 | **3.307** | nieuwbouw | Rafalet · obra nueva, 'lista en marzo de 2026 (sujeto a cambios)', promotie notFinished, perceel 1.085 m² | 110831782 (330 m²) |
| 2 | [112527650](https://www.idealista.com/es/inmueble/112527650/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail) | 950.000 | 180 | **5.278** | 2026 (veld) | Pinomar · veld 'construido en 2026'; tekst 'tradicional villa'; dubbele advertentie zegt 'la construcción es joven' — ZWAK | 112462622 |
| 3 | [112093850](https://www.idealista.com/es/obra-nueva/112093850/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail) | 1.150.000 | 177 | **6.497** | op plan | Pinosol · PROJECT: perceel 889 m² + goedgekeurde licentie, 'listo para construir', prijs excl. IVA | — |
| 4 | [106823897](https://www.idealista.com/es/inmueble/106823897/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail) | 1.275.000 | 223 | **5.717** | in aanbouw | Pinosol · 'diseño contemporáneo', 'fase final de su construcción'; advertentie > 1 jaar niet bijgewerkt; geen bouwjaar | — |
| 5 | [111656885](https://www.idealista.com/es/inmueble/111656885/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail) | 1.288.000 | 333 | **3.868** | 2026 (veld) | Pinosol · nieuwbouw, 'finalización marzo de 2027', tegels/afwerking nog te kiezen — in aanbouw | — |
| 6 | [112165476](https://www.idealista.com/es/inmueble/112165476/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail) | 1.495.000 | 420 | **3.560** | 2026 (veld) | Pinosol · 'nueva construcción', 'cerca de su finalización', veld 2026 | 112422911, 109868268 |
| 7 | [111718472](https://www.idealista.com/es/inmueble/111718472/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail) | 1.650.000 | 200 | **8.250** | op plan | Pinosol · 'Casa Renoir', obra nueva met licentie, 'entrega prevista en 14 meses desde el inicio de las obras' — op plan | — |
| 8 | [112515850](https://www.idealista.com/es/obra-nueva/112515850/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail) | 1.950.000 | 200 | **9.750** | nieuwbouw | Pinosol · obra nueva, promotie notFinished, zeezicht, projectlabel A | — |
| 9 | [112158635](https://www.idealista.com/es/obra-nueva/112158635/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail) | 3.495.000 | 427 | **8.185** | op plan | La Lluca · finca rústica obra nueva op 10.000 m² olijfgaard, 'finalización junio de 2027' — UITSCHIETER, op plan | 112158013 (zonder m²) |

Opmerkingen bij deze reeks:
- Het aanbod is dun: in drie zones samen 9 unieke objecten, waarvan **7 in Pinomar–Pinosol**, 1 in El Rafalet en 1 in La Lluca–Tarraula (een finca rústica op 10.000 m²; de tweede advertentie van dezelfde promotie, 112158013, geeft géén m²).
- Drie objecten zijn geen gebouwde villa maar een **op-plan-aanbieding**: 112093850 (perceel + licentie, bouw niet gestart, prijs excl. IVA), 111718472 (levering 14 maanden na start van de bouw) en 112158635 (oplevering juni 2027). Ze staan erin omdat ze wél laten zien wat er in deze zone voor een "nieuwe villa, opgeleverd" wordt gevraagd; de statistiek zonder die drie staat in §3. Nog eens drie zijn **in aanbouw** (111918606, 111656885 — oplevering maart 2027 —, 112165476) en één is "in de eindfase" volgens een advertentie die al > 1 jaar niet is bijgewerkt (106823897).
- 112527650 (950.000 €, 180 m²) is het zwakste geval: het veld zegt "construido en 2026", maar de tekst noemt het een "tradicional villa … bien cuidada"; alleen de dubbele advertentie 112462622 zegt "la construcción es joven". Mogelijk een invoerfout in het bouwjaar.
- Nieuwbouw wordt in de regel **exclusief 10 % IVA** aangeboden (112093850 zegt dat expliciet); tweedehands prijzen zijn "prijs zonder overdrachtsbelasting" (ITP 9 %, zie `kader/parameters.json`). Vergelijk dus niet één op één.
- 102167151 (Rafalet, 1.315.000 €, "chalet de reciente construcción", 380 m² in het veld maar "casa de 253 m²" in de tekst, geen bouwjaar, energielabel op standaardwaarde G, advertentie > 2 maanden oud) is **niet** opgenomen: onvoldoende bewijs dat het nieuwbouw is.
- Het `obra-nueva`-URL-pad in de tabel is letterlijk wat `search_properties` teruggaf; `property_detail` geeft dezelfde code onder `/es/inmueble/…/`.

---

## 6. Grenszone Partida Tosal – Zona dels Castellans (K05) — apart gehouden

Deze zone is niet in de hoofdreeksen gemengd: het is een andere Idealista-wijk (noordkant, tegen de Montgó) en K05 ligt er alleen aan de rand van. Zelfde methode.

### `villa_renovated_tosal` (6 objecten)
| # | Code (link) | Vraagprijs € | m² gebouwd | €/m² | Bouwjaar (tool) | Zone · toelichting (bewijs uit tekst/`property_detail`) | Dubbele advertenties van hetzelfde object |
|---|---|---|---|---|---|---|---|
| 1 | [110753189](https://www.idealista.com/es/inmueble/110753189/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail) | 720.000 | 165 | **4.364** | onbekend | Tosal · 'Completamente renovada', ibiza-stijl, één laag, label C, perceel 973 m² | — |
| 2 | [107385205](https://www.idealista.com/es/inmueble/107385205/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail) | 794.000 | 250 | **3.176** | 1978 | Tosal · bouwjaar 1978, 'reformada recientemente'; advertentie > 1 jaar niet bijgewerkt | — |
| 3 | [110122731](https://www.idealista.com/es/inmueble/110122731/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail) | 800.000 | 216 | **3.704** | 1982 | Tosal (Ctra. Jesús Pobre) · bouwjaar 1982, 'reforma integral de alta gama', label E | — |
| 4 | [111361293](https://www.idealista.com/es/inmueble/111361293/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail) | 1.399.000 | 275 | **5.087** | onbekend | Tosal · 'renovación integral' incl. elektra en leidingen; op loopafstand casco; 220 m² nuttig | — |
| 5 | [112504358](https://www.idealista.com/es/inmueble/112504358/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail) | 2.250.000 | 300 | **7.500** | onbekend | Tosal · 'recientemente renovada', vloerverwarming 2026, perceel 3.000 m² + gastenhuis | 112512860, 112469782, 112475999 |
| 6 | [111433078](https://www.idealista.com/es/inmueble/111433078/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail) | 3.550.000 | 380 | **9.342** | onbekend | Tosal (Montgó) · MODERN: 'Ca Malva', 'arquitectura contemporánea, minimalista', lift, infinity pool; geen jaar | — |

### `villa_new_tosal` (1 object)
| # | Code (link) | Vraagprijs € | m² gebouwd | €/m² | Bouwjaar (tool) | Zone · toelichting (bewijs uit tekst/`property_detail`) | Dubbele advertenties van hetzelfde object |
|---|---|---|---|---|---|---|---|
| 1 | [111928138](https://www.idealista.com/es/obra-nueva/111928138/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail) | 1.575.000 | 230 | **6.848** | nieuwbouw | Tosal · obra nueva, promotie notFinished, zeezicht, perceel 1.500 m² | — |

Niet opgenomen in Tosal ondanks "villa de diseño": 108549029 (1.695.000 €, 253 m², 6.700 €/m²) — geen bouwjaar, geen renovatieclaim, advertentie > 11 maanden oud; de term is hier marketing. K05 zelf (97576395, 395.000 €, 460 m², 859 €/m²) zat niet in de "buen estado"-set en is een renovatieobject, dus per definitie geen vergelijker voor deze reeksen.

---

## 7. Wat de cijfers zeggen voor K05, K08 en K09 (geen waardering, alleen wat er staat)

- **K08 (perceel El Rafalet, 150.000 €, 1.120 m², licentieclaim)** en **K09 (perceel Pinosol, 299.000 €, 1.299 m², claim 0,20 m²/m² ≈ 259 m² bebouwbaar)**: de relevante uitkomstreeks is `villa_new`. In Pinosol vragen afgebouwde of bijna-afgebouwde nieuwbouwvilla's 3.560–5.717 €/m² (112165476, 111656885, 106823897, 112527650) en luxe/kleinere objecten 8.250–9.750 €/m² (111718472, 112515850). In El Rafalet is er precies één nieuwbouwreferentie: 3.307 €/m² (111918606, 329 m² op 1.085 m²). Gerenoveerde villa's in Rafalet vragen 3.602–6.878 €/m² (mediaan 5.660). Wat dat oplevert na bouwkosten (opgave Jan: nieuwbouw 2.000 €/m² excl. btw, excl. architect/vergunning/zwembad/buitenruimte — `kader/investeringskader.md`) is een rekensom voor het dossier, niet voor dit rapport.
- **K05 (chalet Tosal, 460 m², 859 €/m², barranco-affectie, geen uitbreiding)**: de uitkomstreeks is `villa_renovated_tosal`: mediaan 4.726 €/m², onderkant 3.176–3.704 €/m² voor gerenoveerde villa's van 216–250 m² uit 1978–1982 (107385205, 110122731). Let op: geen enkele vergelijker in Tosal is zo groot als K05 (grootste gerenoveerde: 380 m²); grote volumes halen per m² doorgaans minder, en de barranco-kwestie (legaliteit, verzekerbaarheid) is een randvoorwaarde die geen vergelijker deelt.

---

## 8. Kanttekeningen (lees dit vóór je een cijfer overneemt)

1. **Vraagprijzen, geen transacties.** Alles hierboven is wat aanbieders vragen op 15-09-2026. Onderhandelingsmarges, stille prijsverlagingen (R15 §5.7) en niet-verkochte langlopers zitten erin. Zichtbaar in de tool: 111952972 −5 % (1.250.000 → 1.190.000). Van het Rafalet-object 850.000 € (111909291) bestaat ook een advertentie op 1.299.000 € inclusief een los bouwperceel (111909298) — dat is dus geen prijsdaling maar een andere aanbieding.
2. **Steekproef.** n = 20 / 9 / 6 / 1. De reeks `villa_new` hangt aan Pinosol; voor El Rafalet (1) en La Lluca (1, finca) is nieuwbouw feitelijk niet in de tool aanwezig. Per-zone-medianen (n = 5–8) zijn indicatief, geen zoneprijs.
3. **Zonelabels zijn benaderend en soms fout** (bewijstype 1, dit rapport): 109969426 staat als La Lluca maar noemt zelf "Tosalet / urbanización Cansalades"; 110085483 staat als Pinosol maar noemt "Adsubia / Cap Martí"; 108983977 staat als Pinosol maar noemt "urbanización Tosalet"; 109868268 noemt "Cap Martí – El Tossalet – Pinomar"; 111351541 staat als Tosal maar is een casa de pueblo in het casco antiguo. De pin (lat/lon) zit in de scratchpad-dataset en kan later tegen eigen wijkgrenzen worden gelegd.
4. **m² gebouwd is niet betrouwbaar.** Hetzelfde object wordt aangeboden met 236/240/270 m² (Rafalet 850.000), 1.000/1.100/1.350 m² (La Lluca 3.450.000), 370/380 m² (Pinosol 1.685.000) en 359/360 m² (La Lluca 1.795.000); 102167151 zegt 380 m² in het veld en 253 m² in de tekst; 108153256 zegt 221 m² in het veld en 222 m² in de tekst. Een verschil van 10–35 % in m² verschuift €/m² evenveel. Voor een dossier: kadastrale m² gebruiken, niet de advertentie.
5. **"Gerenoveerd" is een claim van de aanbieder.** Bevestigd is alleen wat `property_detail` en de tekst zeggen; niemand heeft de woningen gezien. Zwakste gevallen in de reeks: 112310283 (alleen "esta villa reformada", geen jaar) en 111952972 ("cuidadosamente modernizada", architectuur behouden). Het renovatiejaar ontbreekt bij 11 van de 20; het bouwjaar bij 7 van de 20. Eén object (112509325) is **nog in renovatie**; één (108153256) is "gerenoveerd in juli 2026" maar wordt als "nueva construcción" aangeprezen; één (109546138) is niet gerenoveerd maar modern (bouwjaar 2017).
6. **Bijzondere objecten die de spreiding oprekken:** twee fincas (1.000 m² op 5.850 m²; 526 m² op 1 ha met stallen) aan de onder- en bovenkant; een villa van 130 m² op 1.999 m² (6.500 €/m², grondwaarde); een ontwikkelaarsrenovatie die **onder IVA** wordt verkocht (110895902, 9.203 €/m², veld "construido en 2026"). Zie de kolom Toelichting; de statistiek zonder de fincas staat in §3.
7. **Nieuwbouw excl. IVA, deels op plan en deels in aanbouw** (zie §5). Eén "nieuwbouw"-object (106823897) is al > 1 jaar niet bijgewerkt terwijl de tekst "in de eindfase van de bouw" zegt; 111918606 zou "in maart 2026" klaar zijn en staat nog steeds als promotie "notFinished".
8. **Tool-eigenaardigheden (bewijstype 1, vandaag):** meerdere wijknamen in één query → één wijk; "reformado" → filter "buen estado"; "a estrenar"/"nueva construcción" → filter "obra nueva" + subtype "villa" (0 resultaten); geen paginering (prijsbanden nodig; prijsgrenzen zijn inclusief, dus overlap op de grens); `property_detail` geeft bouwjaar, perceel, energielabel en bijwerkdatum, maar géén publicatiedatum, prijshistorie of kadastrale referentie. De zoekresultaten bevatten wel telefoonnummers van aanbieders; die zijn hier bewust niet overgenomen.
9. **Datum.** Alle cijfers gelden voor 15-09-2026. De ruwe tool-uitvoer (JSON) staat in de sessie-scratchpad (`h01b/`: `merged.json` met 208 codes en `final.json` met de classificatie); die map is tijdelijk. Wil Jan dit periodiek herhalen, dan hoort dit in fase B als geautomatiseerde reeks (zie 05-bouwplan).
10. **Onafhankelijke herhaling.** Deze meting is op 15-09-2026 twee keer uitgevoerd (een eerdere run om ±09:38 en deze run); beide komen op dezelfde 20 gerenoveerde/moderne objecten en dezelfde medianen uit. Verschil: `villa_new` telt nu 9 in plaats van 8, omdat de chalet-zoekopdracht in La Lluca ditmaal de finca-advertentie 112158635 mét m² (427) teruggaf.

---

## 9. Uitgesloten objecten met reden (zodat niemand ze opnieuw hoeft te beoordelen)

| Code | Zone | Prijs / m² | Reden |
|---|---|---|---|
| 111909298 | Rafalet | 1.299.000 / 236 | prijs omvat een tweede bouwperceel (zelfde villa als 111909291) |
| 110552710 + 110873301 + 110627990 | Rafalet | 1.840.000 / 476 | prijs omvat 3.534 m² extra "suelo urbanizable" met reparcelatieproject; geen renovatie |
| 112109577 | Rafalet | 1.175.000 / 414 | "oportunidad de restauración" — renovatieproject |
| 112356353 | Rafalet | 599.950 / 205 | "para reformar", "potencial de renovación" |
| 102167151 | Rafalet | 1.315.000 / 380 | "reciente construcción" zonder jaar; m² tekst (253) ≠ veld (380); label G standaard — `property_detail` opgevraagd |
| 112394860 / 108137070 / 111386710 | La Lluca | 1.295.000 / 398–413 | twee woningen in één prijs (traditioneel + nieuw ibiza-stijl) |
| 111392277, 111441620, 107910566 | La Lluca | 1.295.000 / 333–401 | hoofdhuis "gran potencial de renovación" / status `renew`; alleen bijgebouw gerenoveerd |
| 112473328, 112440529 | La Lluca | 400.000 / 775.000 | renovatie- resp. nieuwbouwproject ("base para una renovación") |
| 110840687, 108408372, 111678428, 110836087, 110836711, 109522880, 110843390 | La Lluca | 995.000 / 294–328 | alleen keuken "reformada/renovada" |
| 107329954 | La Lluca | 1.600.000 / 400 | "reformada a lo largo de las décadas" — geen recente renovatie |
| 112273590 | La Lluca | 1.395.000 / 299 | "casa grande y moderno" — geen renovatieclaim, geen bouwjaar — `property_detail` opgevraagd |
| 111147949, 111988685 | La Lluca | 1.150.000 / 2.400.000 | bouwjaar 2004 in de tekst, geen renovatie |
| 110839159 | La Lluca | 990.000 / 273 | alleen zwembad nieuw en airco "a estrenar" |
| 112158013 | La Lluca | 3.495.000 / — | zelfde promotie als 112158635, maar zonder m² in de tool |
| 108983977, 108843125, 110291925, 112342256 | Pinosol | 1.200.000 / 230 | "para reformar" / "requiere reforma integral" |
| 110085483 | Pinosol | 695.000 / 245 | "proceso de transformación hacia una residencia de lujo" — project; tekst zegt Adsubia |
| 111486691 | Pinosol | 618.000 / 162 | "reformada en 2012" — te oud om als gerenoveerd te tellen |
| 112190871 | Pinosol | 899.000 / 218 | "construida en 2006", geen renovatie |
| 112031038 + 111786053 | Pinosol | 2.295.000 / 300 | alleen zwembad "completamente renovada"; villa-renovatie niet bevestigd (label A, geen jaar) — `property_detail` opgevraagd, twijfelgeval buiten de reeks |
| 112344706 | Pinosol | 1.095.000 / 164 | "interior bellamente moderno", "mejoras recientes" — geen renovatieclaim, geen jaar — `property_detail` opgevraagd |
| 111188744, 112462656, 106701467, 111779943, 108985802/108232227, 109231417-groep | Pinosol | — | alleen zachte termen ("cocina moderna", "hogar moderno", "sofisticación moderna"); 109231417 zegt zelf "no es una villa de líneas modernas" |
| 112342297, 97576604 (+3 dubbels), 107659062, 83667869, 112430983, 111351541, 108549029 | Tosal | — | te renoveren / renovatieproject / alleen zwembadzone gerenoveerd (2020) / perceel splitsbaar, geen renovatie / casco-huis met fout zonelabel / "villa de diseño" onbevestigd (`property_detail` opgevraagd) |

---

## 10. Uitgevoerde tool-aanroepen (log)

`search_properties` (CHALET, SALE, maxResults 50, es-ES/es), 18 aanroepen: de zes gevraagde meervoudige-wijkqueries (alle → La Lluca–Tarraula; 36 / 50 van 70 / 38 / 1 / 0 / 0 resultaten) · "chalet reformado en El Rafalet, Jávea" (22) · "chalet reformado en Pinomar – Pinosol, Jávea" in drie prijsbanden (24 / 24 / 24) · "chalet reformado en La Lluca – Tarraula, Jávea" in drie prijsbanden (21 / 33 / 16) · "chalet reformado en Partida Tosal – Zona dels Castellans, Jávea" (38) · "chalet obra nueva en …" voor Rafalet (1), Pinomar–Pinosol (2), La Lluca–Tarraula (1) en Partida Tosal (1).
`property_detail` (42×): 111452530, 111909291, 112229028, 109546138, 108153256, 102167151, 111918606, 112310283, 112501089, 111229059, 109645331, 112527650, 106823897, 111656885, 112165476, 111718472, 110895902, 112329948, 112031038, 112344706, 112093850, 112515850, 109969426, 111189527, 111952972, 110676663, 110765633, 112509325, 112342262, 108679725, 112273590, 112158635, 110753189, 107385205, 110122731, 111361293, 112504358, 111433078, 108549029, 111928138, 110668828.

Geen telefoonnummers of contactgegevens overgenomen; makelaarsnamen (`commercialName`) zijn bewust weggelaten — niet nodig voor de prijsreeks. Geen sleutels gebruikt: de Idealista-assistent draait als MCP binnen de sessie.

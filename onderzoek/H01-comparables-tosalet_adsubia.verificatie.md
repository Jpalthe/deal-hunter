# H01: tegenspraak op de vergelijkingsprijzen, zone `tosalet_adsubia`

**Gecontroleerd bestand:** `onderzoek/H01-comparables-tosalet_adsubia.md`. Daarin is niets aangepast; het ongewijzigde origineel staat ook in `kader/comparables.json`.
**Rol:** tegenspreker. **Controledatum:** 15-09-2026.
**Bron:** de officiële Idealista-assistent (MCP `property_detail` en `search_properties`, country es, locale es-ES). Bewijstype 1: het toolresultaat, letterlijk overgenomen.
**Alle bedragen zijn vraagprijzen**, geen transactieprijzen. Er zijn geen telefoonnummers of contactgegevens overgenomen.

## 1. Oordelentabel

| Reeks (zoals de rekenaar hem gebruikt) | Gerapporteerd (n / p25 / mediaan / p75) | Oordeel | Kern | Gecorrigeerd |
|---|---|---|---|---|
| **villa_renovated** | 26 / 3.973 / 4.782 / 6.153 | **Bevestigd** | Drie voorbeelden geopend (het goedkoopste, het duurste en het goedkoopste moderne object): prijs, m² en claim kloppen. Een eigen zoekopdracht geeft een mediaan van 4.358 (−8,9 %, binnen ±15 %). De rekenkunde klopt en de ontdubbeling klopt steekproefsgewijs. | – |
| **villa_new** | 12 / 4.153 / 5.361 / 5.942 | **Weerlegd** | Het duurste voorbeeld (111926896, Villa Amelia, 9.000 €/m²) is geen nieuwbouw. Het is een perceel met een ontwerp ("en fase de proyecto") en in het veld staat "Segunda mano/para reformar". Daarnaast zit er een chalet pareado in de villareeks (106502380, volgens het origineel "dus geen villa"). Een eigen zoekopdracht geeft een mediaan van 4.176 (−22 %, buiten ±15 %). | **n = 10, p25 4.108, mediaan 4.825, p75 5.907** |
| **townhouse_renovated** | 4 / 3.018 / 3.132 / 3.198 | **Niet te verifiëren** | Alle vier de voorbeelden geopend: prijs, m² en renovatie kloppen. De rekenkunde klopt. Maar 112243938 en 112428067 zijn waarschijnlijk hetzelfde huis en daarom niet te bevestigen als twee objecten. **Te klein voor een betrouwbare mediaan.** | Bij samenvoegen: n = 3, mediaan 3.081 of 3.182 (±2 %) |
| apartment_renovated | niet aanwezig | Niet te verifiëren | Deze reeks staat niet in H01 en niet in `comparables.json` voor deze zone ("niet van toepassing en niet bepaald"). | – |
| apartment_new | niet aanwezig | Niet te verifiëren | Idem. | – |

**Kern in één zin:** de villa_renovated-mediaan (±4.800 €/m²) houdt stand. De villa_new-mediaan van 5.361 is te hoog: er zitten een project zonder woning en een halfvrijstaand huis in, en gecorrigeerd komt hij op 4.825 uit.

## 2. Controle 1: `property_detail` op de voorbeelden

### 2.1 villa_renovated

| Code | Tool: prijs / m² construidos / €/m² | Klopt met H01 | Claim in de tool | Oordeel |
|---|---|---|---|---|
| 105971886 (goedkoopste, #1 strict) | 2.000.000 / 670 / 2.985; "Construido en 1980"; Segunda mano/buen estado | ja | "Villa de tres alturas totalmente reformada con ampliación … en el año 2012" | gerenoveerd. De renovatie is wel 14 jaar oud en de advertentie is "hace más de un año" bijgewerkt, zoals H01 ook meldt. |
| 112196807 (duurste, #19 strict) | 2.430.000 / 200 (190 útiles) / 12.150; "Construido en 2026"; perceel 1.009 m² | ja | "totalmente reformada … Reconstruida con materiales de altísima calidad" | gerenoveerd/herbouwd; een uitschieter, zoals H01 aangeeft |
| 111318619 (goedkoopste modern, #1) | 995.000 / 317 / 3.139; geen bouwjaar; perceel 727 m² | ja | "villa mediterránea de estilo contemporáneo"; geen renovatieclaim | past binnen de eigen definitie "modern". Let op: dit is presentatie, geen bewezen bouwjaar of renovatie. |

Bij alle drie is `priceByArea` van de tool gelijk aan vraagprijs ÷ m²-veld. Geen van de drie is "para reformar".

### 2.2 villa_new

| Code | Tool: prijs / m² / €/m² | Klopt met H01 | Status in de tool | Oordeel |
|---|---|---|---|---|
| 109963880 (goedkoopste, Begonia 21) | 990.000 / 350 (270 útiles) / 2.829 | ja | `newdevelopment`, promotie `notFinished`; tekst "270 m² construidos"; beelden: plattegronden, gevel en terrein | nieuwbouwproject, klopt. Het conflict tussen het m²-veld en de tekst (350 tegen 270) staat terecht in H01. |
| 112041902 (Villa Malva) | 1.800.000 / 219 (197 útiles) / 8.219 | ja | `newdevelopment`, "obra nueva terminada", promotie `finished` | nieuwbouw, klopt. Let op: de zustercode 110763829 schrijft "La vivienda **contará** con suelo radiante…" (toekomende tijd). |
| **111926896 (duurste, Villa Amelia)** | 1.800.000 / 200 (180 útiles) / 9.000 | cijfers ja | status `renew`; veld **"Segunda mano/para reformar"**; tekst: "proyecto de obra nueva … **actualmente en fase de proyecto**, con un plazo estimado de construcción de 12 meses desde el inicio de las obras"; 10 beelden: renders, uitzicht en plattegronden | **Voldoet niet aan de controle.** Er staat geen woning: de prijs is perceel plus te bouwen villa. Het object hoort niet in een reeks voor de verkoopprijs van een bestaande nieuwe villa. |

**Mogelijk dubbel, niet bewezen:** Villa Amelia (111926896) ligt volgens de tool ±20 m van Villa Malva (112041902/110763829); beide advertenties tonen het exacte adres. Ze hebben dezelfde vraagprijs (1.800.000), 4 slaapkamers, 2 bouwlagen en een perceel van 1.077 tegen 1.070 m². Maar de indeling in de tekst verschilt en de makelaars zijn verschillend, dus het kan ook een buurperceel zijn. Voor het oordeel maakt dit niet uit: Amelia valt al af als project.

### 2.3 townhouse_renovated (alle vier geopend)

| Code | Tool: prijs / m² / €/m² | Klopt met H01 | Claim in de tool | Oordeel |
|---|---|---|---|---|
| 112428067 | 385.000 (was 415.000, −7 %) / 136 (116 útiles) / 2.831; "Chalet adosado"; 1980 | ja | "recientemente renovado … cocina moderna, ventanas nuevas de PVC, cuadro eléctrico actualizado con cableado nuevo y paneles solares"; urbanisatie van 10 woningen | gerenoveerd |
| 112517370 | 419.000 / 136 (115 útiles) / 3.081; 1980 | ja | "vivienda pareada … cuidadosamente renovada y mejorada"; jacuzzi, laadpunt | gerenoveerd |
| 112243938 | 385.000 (was 415.000, −7 %) / 121 / 3.182; "Chalet pareado" | ja | "reformada en 2023"; jacuzzi, 10 zonnepanelen, laadpunt | gerenoveerd |
| 111952056 | 445.000 / 137 (120 útiles) / 3.248; 1980; VvE 130 €/maand | ja | "vivienda reformada … cocina totalmente reformada"; gemeenschappelijk zwembad | gerenoveerd |

## 3. Controle 2: eigen zoekopdrachten (één per reeks)

| Reeks | Zoekopdracht (letterlijk) | Filter die de tool toepaste | Totaal / opgehaald | Na eigen indeling en ontdubbeling | Mediaan | Afwijking t.o.v. H01 |
|---|---|---|---|---|---|---|
| villa_renovated | "villa totalmente reformada en El Tosalet - Cap Martí, Jávea/Xàbia" (CHALET) | Villas / Usada, buen estado; El Tosalet – Cap Martí | 71 / 50 | n = 12 (9 gerenoveerd, 3 modern) | **4.358** (p25 3.929, p75 6.290) | **−8,9 %**, binnen ±15 % |
| villa_new | "chalet de obra nueva en El Tosalet - Cap Martí, Jávea/Xàbia" (CHALET) | Chalets independientes / Obra nueva | 10 / 10 | n = 7 (Kentia 2 codes → 1, Malva 3 codes → 1) | **4.176** (p25 4.072, p75 4.825) | **−22,1 %**, buiten ±15 % |
| townhouse_renovated | "adosado o pareado reformado con piscina comunitaria en Adsubia, Jávea/Xàbia" (CHALET) | Chalets pareados + adosados / buen estado / con piscina; Adsubia | 2 / 2 | n = 2 (112428067, 112243938) | 3.006 | −4,0 %, maar n = 2 |

searchUrls (letterlijk):
- villa_renovated: https://www.idealista.com/es/venta-viviendas/javeaxabia/el-tosalet-cap-marti/con-villa,buen-estado/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_list
- villa_new: https://www.idealista.com/es/venta-viviendas/javeaxabia/el-tosalet-cap-marti/con-chalets-independientes,obra-nueva/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_list
- townhouse_renovated: https://www.idealista.com/es/venta-viviendas/javeaxabia/adsubia/con-chalets-pareados,chalets-adosados,piscina,buen-estado/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_list

**Toelichting villa_renovated.** Opgenomen op de tekst: 105714026, 112393237, 112104007, 111584760, 112437753, 111643516, 111329930, 108940959 (samen met 104650661 als één object), 112196807, plus de moderne objecten 98119662, 108920763 en 109011069 (samen met 102601416). Uitgesloten waren onder meer 110035697 ("se ofrece con una remodelación": een voorstel, geen uitgevoerde renovatie), 109945394 ("será objeto de una reforma integral"), 104650661 als apart object ("en proceso de renovación integral"), 110850877 (villa met 5 appartementen) en alle objecten waar alleen de keuken, het zwembad of "comodidades modernas" worden genoemd. Kanttekening: de tool gebruikt hetzelfde filter als zoekopdracht 1 van H01, dus de onderliggende advertenties zijn deels dezelfde. De indeling en de ontdubbeling zijn wel eigen werk. Adsubia valt buiten deze zoekopdracht.

**Toelichting villa_new.** Het filter "obra nueva" laat de villa's weg die als tweedehands staan geadverteerd (Kismet 5.928, Adsubia-Consum 5.846, Tosalet 5 5.983, Amelia 9.000) en ook het halfvrijstaande huis van Cumbres del Tosalet (5.389). De eigen definitie van H01 neemt tweedehands geadverteerde nieuwbouw bewust mee; dat is verdedigbaar. Daarom telt de afwijking van −22 % niet los als weerlegging. De weerlegging rust op twee objecten die niet aan de eigen definitie voldoen (§2.2 en §4).

## 4. Controle 3: ontdubbeling en rekenkunde

**Rekenkunde.** De percentielen zijn nagerekend op de voorbeeldlijsten in H01, met lineaire interpolatie en `statistics.median`, zelf herberekend als vraagprijs ÷ m²-veld:

| Reeks | Herberekend: n / min / p25 / mediaan / p75 / max | H01 |
|---|---|---|
| villa_renovated | 26 / 2.985 / 3.973 / 4.782 / 6.153 / 12.150 | identiek |
| villa_renovated_strict | 19 / 2.985 / 3.911 / 4.571 / 6.291 / 12.150 | identiek (p25 3.910: afronding) |
| villa_modern | 7 / 3.139 / 4.358 / 5.861 / 6.087 / 6.250 | identiek (p75 6.088: afronding) |
| zonder uitschieters > 9.000 | 24 / – / 3.929 / 4.505 / 6.084 / – | identiek (4.504: afronding) |
| villa_new | 12 / 2.829 / 4.154 / 5.361 / 5.942 / 9.000 | identiek (p25 4.153: afronding) |
| townhouse_renovated | 4 / 2.831 / 3.018 / 3.131 / 3.198 / 3.248 | identiek (3.132: afronding) |

De rekenkunde klopt dus. De fout in villa_new zit in de samenstelling van de reeks, niet in de som.

**Ontdubbeling.**
- *villa_renovated:* in de eigen zoekopdracht zijn de door H01 samengevoegde paren teruggezien (108940959/104650661, 109011069/102601416). De driedubbele code 112342298/110731539/110700468 (2.050.000/606) staat terecht niet in de reeks, want er is geen renovatieclaim. Er zijn geen gemiste dubbelen gevonden. **Bevestigd.**
- *villa_new:* Kentia (112043325/110824450) en Malva (112041902/110763829/110755736) zijn correct samengevoegd. Amelia–Malva is een mogelijk dubbel (§2.2), maar niet bewezen.
- *townhouse_renovated:* **112243938 en 112428067 zijn waarschijnlijk hetzelfde huis.** Beide hebben nu 385.000, eerder 415.000 (−30.000, −7 %), 3 slaapkamers en 2 badkamers. De indeling is dezelfde: woonkamer met open haard en een naya acristalada boven, drie slaapkamers beneden met de hoofdslaapkamer en-suite, en de andere twee delen een badkamer. Beide hebben zonnepanelen, een eigen garage en een gemeenschappelijk zwembad. Ze komen van twee verschillende makelaars en het m²-veld verschilt (121 tegen 136). Volgens de eigen regel van H01 ("samengevoegd waar … tekst overduidelijk hetzelfde object beschrijven met een afwijkend m²-veld") hadden ze samengevoegd moeten worden. Bewijzen kan het niet: de urbanisatie heeft ±10 gelijke woningen uit 1980, en alleen 112243938 noemt jacuzzi en laadpaal. Ook 112517370 noemt jacuzzi en laadpaal, maar tegen een andere prijs (419.000).

**Gevoeligheid townhouse_renovated:** samengevoegd met 136 m² wordt het n = 3 met mediaan 3.081; met 121 m² n = 3 met mediaan 3.182. De mediaan ligt dus stabiel rond 3.100 €/m², maar het aantal objecten is onzeker (2–4).

## 5. Gecorrigeerde villa_new

Twee objecten vallen uit de reeks:
1. **111926896 (Villa Amelia, 9.000 €/m²)**: een project zonder woning, met veldstatus "para reformar" (zelf gezien, §2.2).
2. **106502380 (Cumbres del Tosalet, 5.389 €/m²)**: een chalet pareado op een perceel van 403 m². Volgens H01 zelf "geen villa". Het object komt ook niet terug onder het filter "chalets independientes / obra nueva" (§3). Halfvrijstaande woningen horen, als ze meetellen, bij townhouse-achtige reeksen.

Resterende waarden (n = 10): 2.829, 4.058, 4.085, 4.176, 4.316, 5.333, 5.846, 5.928, 5.983, 8.219.
→ **p25 4.108 · mediaan 4.825 · p75 5.907** (min 2.829, max 8.219).

Gevoeligheid: zonder alleen Amelia wordt het n = 11 met mediaan 5.333; zonder alleen het halfvrijstaande huis n = 11 met mediaan 5.333. Pas samen verschuift de mediaan met −10 %. Ter vergelijking: de vorige versie van H01 (09:39) gaf voor villa_new n = 10 en mediaan 4.824 (bron: `_caveats` in `kader/comparables.json`). Die uitkomst ligt vrijwel gelijk aan deze correctie. De reeks blijft een mengsel van 4 opgeleverde villa's en 6 projecten; het origineel waarschuwt daar zelf ook voor.

## 6. Wat dit betekent voor de rekenaar

- **villa_renovated 4.782** kan blijven staan. Voor een voorzichtige exitprijs ligt de variant zonder uitschieters (4.504) meer voor de hand, omdat de twee zeezichtvilla's met veel grond de p75 opdrijven.
- **villa_new** moet omlaag naar een mediaan van **4.825** (p25 4.108, p75 5.907). Met 5.361 wordt de exitwaarde van een nieuwbouwvilla in deze zone ±11 % te hoog ingeschat.
- **townhouse_renovated** is te klein en waarschijnlijk niet goed ontdubbeld. Gebruik het cijfer hoogstens als indicatie (±3.000–3.250 €/m² vraagprijs), niet als harde mediaan.
- Er zijn geen appartementreeksen voor deze zone. Een kandidaat-appartement in Tosalet/Adsubia heeft dus geen eigen vergelijkingsbasis.

## 7. Bronnen

- Idealista-assistent (MCP), `property_detail` voor 105971886, 112196807, 111318619, 109963880, 111926896, 112041902, 112428067, 111952056, 112243938 en 112517370, op 15-09-2026.
- Idealista-assistent (MCP), `search_properties`: drie zoekopdrachten zoals in §3, op 15-09-2026. Het ruwe resultaat van de villa_renovated-zoekopdracht staat in het sessiekladblok (`v_ren.json`).
- `kader/comparables.json`, zone `tosalet_adsubia`: alleen gelezen, niet gewijzigd.

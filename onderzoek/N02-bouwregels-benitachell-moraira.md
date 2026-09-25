# N02 — Bouwregels El Poble Nou de Benitatxell en Teulada-Moraira

**Onderzoeksstroom:** N02 (TREE Deal Hunter) · **Controledatum:** 18-09-2026
**Vervolg op:** `R12-urbanisme-xabia-plan-en-vergunning.md` (Jávea/Xàbia)
**Status:** onderzoeksrapport, geen juridisch advies. Elke bouwconclusie per perceel vereist een schriftelijke bevestiging van de gemeente (informe urbanístico of cédula de garantía urbanística) of van een lokale architect.

**Bewijstypen:** 1 = zelf getest of opgehaald · 2 = officiële wettekst of planvoorschrift · 3 = officiële kaart of database · 4 = officiële publicatie van een overheid · 5 = eigen afleiding of berekening · 6 = bericht van een marktpartij · 7 = onbekend of onbevestigd.

---

## Samenvatting

1. **Benitatxell heeft geen PGOU maar Normas Subsidiarias uit 1987** (CTU Alicante 29-01-1987, BOP nº 36 van 13-02-1987). De gemeente heeft de volledige geconsolideerde tekst zelf online gezet, inclusief de voorschriften van alle achttien ontwikkelingsplannen. Dat is de beste bron die we voor enige gemeente in het werkgebied hebben. Bewijstype 2.
2. **Teulada werkt met een PGOU uit 2004** (CTU Alicante 21-12-2004, BOP 21-01-2005, DOGV 02-03-2005). Dat plan is door de rechter gedeeltelijk vernietigd, maar de gemeente bevestigt in officiële publicaties van 2017 én 2024 dat het het geldende plan is. Bewijstype 2.
3. **Voor Cumbre del Sol geldt een plan parcial uit 1975**, elf keer gewijzigd, laatst in 2022. Het rekent nog in kubieke meters per vierkante meter, niet in de moderne m²t/m². Bewijstype 2.
4. **De harde uitsluiting van Jan is voor Cumbre del Sol niet weg te nemen op basis van openbare bronnen.** Sterker: alle veertien vlakken die in Benitatxell als *suelo urbano* staan geregistreerd liggen in en om de dorpskern. Cumbre del Sol staat in de planningskaart van de Generalitat over de volle breedte als *suelo urbanizable*. Bewijstype 3, met het voorbehoud dat die kaart informatief is.
5. Het plan parcial van 1975 legt het onderhoud van wegen en openbare ruimte bij de eigenarenverenigingen en tot die tijd bij de ontwikkelaar, **"salvo que se haga cesión al Ayuntamiento"** — tenzij er overdracht aan de gemeente wordt afgesproken. Bewijstype 2.
6. Tegelijk onderhoudt de gemeente er wél: asfalteren, groen, brievenbussen, een eigen ploeg van gemeentebedrijf Poble Net. Dat is in het Spaanse recht juist een argument vóór stilzwijgende oplevering. De twee signalen wijzen dus tegengesteld. Bewijstype 4/6.
7. **VAPF heeft een privaat vetorecht.** Artikel 3.1.5.B van het plan parcial eist dat bouwplannen eerst door de ontwikkelaar of de eigenarenvereniging worden goedgekeurd, vóór de gemeentelijke vergunning. Voor een koper-ontwikkelaar is dat een reëel risico op de bouwplanning. Bewijstype 2.
8. **In Teulada zijn sinds 05-02-2024 vergunningen voor nieuwe twee-onder-een-kapwoningen in de zones AIS-1 en AIS-2 geschorst.** De gemeente wil terug naar één woning per perceel. Wie in Teulada een perceel koopt om er twee woningen op te zetten, koopt een aanname die op dit moment niet klopt. Bewijstype 2.
9. **De zoneparameters van Teulada zijn niet openbaar op te halen.** De normativa staat in het BOP-archief van Alicante en in het planregister van de Generalitat, en beide weigeren geautomatiseerde toegang. Voor Teulada blijft het dus: ficha urbanística per perceel opvragen. Bewijstype 1.
10. **Benitatxell heft 3 % ICIO**, tegen 4 % in Jávea, met kortingen tot 80 % voor renovatie — maar alleen binnen de aangewezen kernzone, niet in de urbanisaties. Bewijstype 4.

---

## 0. Werkwijze, toegang en beperkingen

### 0.1 Wat is gedaan

| Onderdeel | Toelichting |
|---|---|
| Documenten | De geconsolideerde Normas Urbanísticas van Benitatxell (187 blz.), het bijbehorende documento de síntesis, de ICIO-verordening, twee DOGV-publicaties van Teulada en een BOE-resolutie uit 1986. Alle als pdf opgehaald en lokaal ontleed. |
| Tekstwinning | Met de ingebouwde macOS-frameworks PDFKit en AppKit via een klein Swift-programma. Niets geïnstalleerd, conform regel 1 van de thuismap. De parametertabel van Benitatxell staat als afbeelding in de pdf en is als plaatje gerenderd en visueel gelezen. |
| Kaartdata | De open WFS-dienst van de Generalitat (`terramapas.icv.gva.es/0702_Planeamiento`), lagen Clasificación en Zonificación. 225 vlakken voor Benitatxell, 524 voor Teulada, met geometrie omgerekend van UTM 30N naar lengte- en breedtegraad. |
| Niet gedaan | Geen contact met een gemeente, geen formulieren ingevuld, geen inloggen, geen omzeilen van afschermingen. |

### 0.2 Drie bronnen die dicht zitten — belangrijk voor het bronnenregister

Dit is geen bijzaak. Het raakt direct wat de Deal Hunter automatisch kan volgen.

| Bron | robots.txt op 18-09-2026 | Gevolg |
|---|---|---|
| `mediambient.gva.es` — het Registro Autonómico de Instrumentos de Planeamiento, de hoofdbron van rapport R12 | Een groep met ruim tachtig AI-user-agents, waaronder `anthropic-ai`, `ClaudeBot`, `Claude-User`, `Claude-Web` en `Claude-SearchBot`, eindigend op `Disallow: /` | **Niet meer automatisch te lezen.** Ik heb er één mapoverzicht opgehaald voordat ik het hele bestand had gelezen, en daarna gestopt. Zet deze bron in het register op ALLEEN HANDMATIG. |
| `politicaterritorial.gva.es` | Zelfde blokkade | Idem |
| `www.dip-alicante.es` — het BOP-archief van Alicante, waar de normativa van Teulada in staat | `User-agent: *` met `Disallow: /` | Niet te lezen, ook niet handmatig via een script |

Bewijstype 1 (zelf opgehaald op 18-09-2026).

Wel gewoon toegankelijk: `dogv.gva.es`, `www.boe.es`, `terramapas.icv.gva.es` (geen robots.txt), `elpoblenoudebenitatxell.com` (geen robots.txt), `sede.diputacionalicante.es` en `www.vapf.com`.

Dat de hoofdbron van R12 nu dichtzit is op zichzelf nieuws voor het register: de Jávea-cijfers in R12 blijven geldig, maar zijn niet meer langs dezelfde weg te verversen.

### 0.3 Wat dit rapport niet is

De geconsolideerde tekst van Benitatxell draagt bovenaan elke pagina de zin: *"Este documento tiene carácter informativo y no tiene valor jurídico."* Dezelfde waarschuwing geldt voor de kaartlaag van de Generalitat. Voor een aankoopbesluit is per perceel een schriftelijke gemeentelijke bevestiging nodig.

---

## 1. El Poble Nou de Benitatxell

### 1.1 Welk plan geldt

| Wat | Antwoord | Bron | Type |
|---|---|---|---|
| Soort plan | **Normas Subsidiarias**, geen PGOU | Documento de síntesis §1.1: *"El planeamiento general vigente en El Poble Nou de Benitatxell, son unas Normas Subsidiarias"* — [1.1-Document-de-sintesi](https://elpoblenoudebenitatxell.com/wp-content/uploads/2025/12/1.1-Document-de-sintesi_Benitachell-V05_signat_signed.pdf) | 2 |
| Goedkeuring | Comisión Territorial de Urbanismo de Alicante, **29-01-1987** | idem | 2 |
| Publicatie | **BOP nº 36 van 13-02-1987** | idem | 2 |
| Geconsolideerde tekst | Opgesteld november 2022, ondertekend december 2022, gepubliceerd op de gemeentesite | [1.2-NN-UU-Text-Consolidat](https://elpoblenoudebenitatxell.com/wp-content/uploads/2025/12/1.2-NN-UU-Text-Consolidat_Benitatxell-V05_signat_signed.pdf) | 2 |
| Wijzigingen | 17 modificaciones puntuales en ordenanzas, van 13-06-1988 tot 25-11-2022 | Documento de síntesis §1.2 | 2 |
| Ontwikkelingsplannen | 18 annexen: 15 planes parciales, 2 planes de reforma interior, 1 plan especial | Geconsolideerde tekst, inhoudsopgave | 2 |
| Nieuw plan in de maak | Er wordt aan een **Plan General Estructural (PGE)** gewerkt. Er ligt een concept-Catálogo de Protecciones, maar dat is niet goedgekeurd en is daarom bewust buiten de geconsolideerde tekst gelaten | Documento de síntesis, §"Catálogo de protecciones" | 2 |

Het PGE is dus geen bouwrecht. Wel risico-informatie: als het ooit wordt vastgesteld kan het beschermingen toevoegen die er nu niet zijn.

### 1.2 De parametertabel (TABLA-1)

Dit is de kerntabel uit hoofdstuk 5 van de Normas Urbanísticas. Ik heb hem als afbeelding gerenderd en overgenomen.

| Klasse | Zone | Typologie | Parcela mínima (m²) | Ocupación (%) | Aantal bouwlagen | Edificabilidad (m²t/m²s) | Dichtheid (won./ha) |
|---|---|---|---|---|---|---|---|
| Suelo urbano | Casco urbano | CD-CM | — | Volgens eigen normativa, afhankelijk van typologie en straatbreedte | Zie 1.3 | Volgens eigen normativa | 30 |
| Suelo urbano | Industrial A | CD | 200 | 100 | 1 | 1,00 | — |
| Suelo urbano | Industrial B | IN | 600 | 50 | 1 | 0,50 | — |
| Suelo urbano | Deportiva | AS | — | 20 | 2 | 0,40 | — |
| Suelo urbano | Verde | AS | — | 5 | 1 | — | — |
| Suelo urbano | Escolar | CD-AS | Eigen normativa | 50 | 3 | 1,00 | — |
| Suelo urbanizable | **Residencial de ensanche (Ciudad Jardín)** | AS | **500** | **30** | **2** | **0,60** | 20 |
| Suelo urbanizable | Residencial de ensanche, tweede regel | AS | **700** | **25** | **2** | **0,50** | 20 |
| Suelo urbanizable | **Turístico-residencial** | AS | **700** | **30** | **2** | **0,25** | 16 |
| Suelo urbanizable | Turístico-residencial | AP (geschakeld) | **1.000** | **30** | **2** | **0,25** | 16 |
| Suelo urbanizable | Turístico-residencial | AG (rijtjes) | **5.000** | **35** | **2** | **0,25** | 16 |
| Suelo no urbanizable | Común y casco | AS | **5.000** | **6** | **2** | **0,08** | 4 |
| Suelo no urbanizable | Protección paisajística | AS | **25.000** | **2** | **1** | **0,02** | 2 |
| Suelo no urbanizable | Protección viaria | — | Alleen onderhoud, verbetering en verbreding van de weg | | | | |
| — | **Goedgekeurde planes parciales** | — | **"Se regirán por su normativa específica"** — dus de eigen voorschriften van dat plan, niet deze tabel | | | | |

Bron: geconsolideerde Normas Urbanísticas, blz. 28, TABLA-1. Bewijstype 2.

Drie dingen om te onthouden.

De kolomkop zegt *ALTURAS (m)* maar de waarden zijn 1, 2 en 3. Dat zijn bouwlagen, geen meters. Artikel 4.3.6.2 en de typologieregels bevestigen dat. Bewijstype 5, met steun uit bewijstype 2.

Er is **geen enkel bouwpercentage dat voor heel Benitatxell geldt**. Wie in een urbanisatie koopt, valt onder het plan parcial van die urbanisatie. De onderste regel van de tabel zegt dat letterlijk.

De twee regels bij Residencial de ensanche staan in de bron zonder toelichting op welk gebied welke geldt. Bewijstype 7 — bij de gemeente na te vragen.

### 1.3 Afstanden tot de perceelgrens en bouwhoogten

De tabel geeft geen afstanden. Die staan in artikel 3.2.1, bij de typologiedefinities.

| Typologie | Afstand tot perceelgrens | Afstand tot straat | Hoogte | Overig |
|---|---|---|---|---|
| **AS** — vrijstaand | Niet minder dan de bouwhoogte, **minimaal 3,00 m**, tot alle grenzen | Idem, minimaal 3,00 m | Max. 2 bouwlagen | — |
| **AP** — twee-onder-een-kap | Als AS, met vrije afstand tot de overige grenzen | Als AS | Max. 2 bouwlagen | — |
| **AG** — rijtjes | Niet minder dan de bouwhoogte, **minimaal 3 m** | **Minimaal 5 m** | Max. 2 bouwlagen | Blok max. 80 m lang |
| **IN** — industrieel | Niet minder dan de bouwhoogte, **minimaal 5,00 m** | Idem | Max. 7 m | In het casco mag het hele perceel bebouwd, met estudio de detalle |
| **CD** — gesloten bouwblok, dicht | n.v.t. | Rooilijn | Zie hieronder | Binnenplaats min. ¼ van de hoogte, min. 3 m; bouwdiepte max. 30 m |
| **CM** — gesloten bouwblok met binnenhof | Achtergevel tot achtergrens min. ½ van de hoogte, **min. 4,00 m** | Rooilijn | Zie hieronder | Bouwdiepte max. 25 m |

Bron: geconsolideerde Normas Urbanísticas, art. 3.2.1, blz. 9–11. Bewijstype 2.

Hoogten in het casco (art. 4.3.6.2), gemeten verticaal vanaf de stoep op elk punt van het gebouw:

| Bouwlagen | Maximale hoogte |
|---|---|
| 2 | 7,20 m |
| 3 | 10,20 m |
| 4 | 13,20 m |

Verdiepingshoogten: begane grond 3,00–4,50 m inclusief vloer, verdiepingen 2,70–3,50 m. De maximale hoogte is verplicht aan de hoofdstraten en pleinen; in de overige straten mogen twee lagen minder. Bewijstype 2.

In het casco geldt **geen minimale perceelgrootte** voor de gesloten typologieën. Artikel 4.3.6.1: *"Dada la estructura parcelaria del núcleo urbano no parece recomendable establecer una parcela mínima."* Alleen voor industrie geldt er wel een. Bewijstype 2.

Uitbouwen boven de straat (art. 4.3.6.3): gesloten erkers alleen in straten breder dan 8,00 m, uitkraging maximaal 7 % van de straatbreedte met een plafond van 1,50 m, en over ten hoogste de helft van de gevellengte. Balkons mogen in alle straten, zelfde uitkraging. Onderkant nooit lager dan 3,60 m boven de stoep. Bewijstype 2.

### 1.4 Suelo no urbanizable — let op de tegenspraak

Hier spreken drie bepalingen elkaar tegen.

| Bepaling | Minimale perceelgrootte SNU común | Bron | Type |
|---|---|---|---|
| TABLA-1 | 5.000 m², met voetnoot naar het goedkeuringsbesluit van de CTU, BOP nº 36 van 13-02-1987 | Normas Urbanísticas blz. 28 | 2 |
| Art. 4.1.6.1 | **0,25 hectare** (2.500 m²) | Normas Urbanísticas blz. 16 | 2 |
| Art. 4.1.8.3 | Elke nieuwe perceelsplitsing moet **meer dan 5.000 m²** opleveren; bij beschermd SNU 25.000 m² | Normas Urbanísticas blz. 19 | 2 |

Bovendien geldt de regionale wet boven het gemeentelijke plan. TRLOTUP art. 211.1.b eist inmiddels **minimaal 1 hectare per woning** en maximaal 2 % bebouwing (zie R12 §1.7). Reken voor Benitatxell dus op één hectare, niet op de oude gemeentelijke cijfers. Bewijstype 5, op basis van bewijstype 2.

Overige eisen in SNU común (art. 4.1.6.1): vrijstaand, maximaal 2 bouwlagen en 7 m, **5 m tot perceelgrenzen en openbare paden**, en **30 m afstand tot andere bewoonbare gebouwen**. Verder: ontwerp aangepast aan de omgeving, witte of aardkleuren, inheemse beplanting. Bewijstype 2.

Afstanden tot wegen (art. 4.1.6.2, gewijzigd door de MP van 10-04-1991, BOP nº 148 van 28-06-1996): 18,00 m tot comarcale, toegangs- en interlokale wegen, 18,00 m tot lokale wegen, 5,00 m tot buurtwegen, gemeten vanaf de buitenrand van het wegcunet. Bewijstype 2.

### 1.5 De achttien ontwikkelingsplannen

De geconsolideerde tekst bevat de voorschriften van elk plan als annex. Dit is de lijst met goedkeuringsdata — handig om per object meteen te weten welk regime geldt.

| Annex | Plan | Goedgekeurd |
|---|---|---|
| 1 | PP Raco de Nadal | CTU 03-02-2005, BOP nº 183 van 12-08-2005 |
| 2 | PP Castellons Vida | Pleno Teulada 26-02-1982, BOP nº 140 van 22-06-1982 |
| 3 | PP Los Molinos-1 (sector I-2) | Zie register |
| 4 | PP Los Molinos-2 (sector I-3) | Zie register |
| 5 | PP Les Fonts | Wijziging 25-11-2022, BOP nº 229 van 01-12-2022 |
| 6 | PP Calistros y Asegador | Zie register |
| 7 | PP La Joya | Wijziging 22-02-1998, BOP nº 88 van 20-04-1998 |
| 8 | PP Vista Montaña | Zie register |
| 9 | PP Alcassar I | Zie register |
| 10 | PP Pueblo Alcassar | 31-05-1976, BOP nº 135 van 16-06-1976 |
| 11 | PP Golden Valley | Wijziging 25-11-2022, BOP nº 229 van 01-12-2022 |
| 12 | PP El Madroñal | Zie register |
| 13 | PP Valle del Portet | Zie register |
| **14** | **PP Cumbres del Sol** | **CTU 06-02-1975, BOP van 25-02-1975** |
| **15** | **PP Enclaves Cumbres del Sol** | **CTU 19-11-1993, BOP nº 1 van 03-01-1994** |
| 16 | PRI La Sequia | Zie register |
| 17 | Plan Especial Puig de la Llorença | Conseller COPUT 13-06-1988 |
| **18** | **PRI Iris-Begonias (Cumbres del Sol)** | **Alcaldía nº 2022-1443 van 25-11-2022, BOP nº 229 van 01-12-2022** |

Bron: geconsolideerde Normas Urbanísticas, annexen; documento de síntesis §1.3. Bewijstype 2.

Twee tegenspraken in de bron zelf, beide te verifiëren (bewijstype 7):

- Het BOP-nummer van 25-02-1975 staat in annex 14 als **nº 46** en in het documento de síntesis als **nº 45**. Zelfde datum.
- Annex 14 dateert het PRI Iris-Begonias op **01-02-2018** ("aprobada por el Ayto."), annex 18 op **25-11-2022** (Resolución de Alcaldía, BOP 01-12-2022). Waarschijnlijk voorlopige en definitieve goedkeuring, maar dat staat er niet.

De gemeente publiceert ook de bijbehorende kaarten, per urbanisatie: [OP-11 Urbanización Cumbres del Sol y Enclaves](https://elpoblenoudebenitatxell.com/wp-content/uploads/2025/12/OP-11_Urbanizacion-Cumbres-del-Sol-Enclaves_signat_signed.pdf), en OP-01 tot en met OP-10 voor de andere urbanisaties en het casco. Bewijstype 3.

---

## 2. Cumbre del Sol — het gebied waar VAPF bouwt

### 2.1 Welk planregime geldt

| Wat | Antwoord | Bron | Type |
|---|---|---|---|
| Regime | **Plan Parcial "Cumbres del Sol"**, niet de zonetabel van de Normas Subsidiarias | TABLA-1, onderste regel: *"PLANES PARCIALES APROBADOS — SE REGIRÁN POR SU NORMATIVA ESPECÍFICA"* | 2 |
| Oorspronkelijke goedkeuring | Comisión Provincial de Urbanismo de Alicante, **06-02-1975**, BOP van 25-02-1975 | Geconsolideerde tekst, annex 14; documento de síntesis §1.3 nr. 1 | 2 |
| Wettelijke grondslag | Ley del Suelo van **15-05-1956**, art. 10 d | Annex 14, art. 3.1.1.A | 2 |
| Classificatie | *"Ordenación de suelo urbanizable residencial"* | Documento de síntesis §1.3 nr. 1 | 2 |
| Enclaves | Apart plan parcial, CTU 19-11-1993, tekstueel een **letterlijke kopie** van de voorschriften van Cumbre del Sol | Annex 15: *"COPIA LITERAL DE LAS ORDENANZAS DEL PLAN PARCIAL CUMBRE DEL SOL"* | 2 |

De keten van wijzigingen, zoals annex 14 hem zelf opsomt:

| Datum | Wijziging | Publicatie |
|---|---|---|
| 30-12-1987 | Declaración voor bescherming van de Puig de la Llorença; de zone "poblado marítimo" met jachthaven verdwijnt | Via Conseller COPUT 13-06-1988 |
| 13-06-1988 | MP nº 1 van de NN.SS. in het PP; voegt art. 3.9 toe | Resolución Conseller COPUT |
| 27-09-1989 | MP van het PP: **edificabilidad in sommige zones voor rijtjeswoningen van 0,48 naar 0,60 m²t/m²s**; splitsing van de zone instalaciones singulares | BOP nº 250 van 31-10-1989 |
| 14-12-1990 | Wijziging wegtracé, uitruil typologieën AG ↔ AIS | BOP van 19-01-1991 |
| 03-11-1993 | Ordenanzas complementarias, o.a. regeling van pergola's in het PP | BOP nº 269 van 23-11-1993 |
| 10-02-1995 | Wegtracés, hotelzone van 4.000 m², minder vrijstaande woningen | BOP nº 64 van 17-03-1995 |
| 11-12-2003 | Rooilijnen in vier deelgebieden: U3L, U3M (Magnolias), U2J (Jazmines) en Z-I. Geen verandering van edificabilidad of woningaantal | DOGV nº 4730 van 13-04-2004 |
| 07-10-2005 | Nieuwe weg in U3P (Palmeras); wegoppervlak van 3.882 naar 5.991 m² | DOGV nº 5207 van 27-02-2006 |
| 25-11-2022 | PRI Iris-Begonias; minimale perceelgrootte 300 m² voor alle gebruiken in dat deelgebied | BOP nº 229 van 01-12-2022 |

Bron: geconsolideerde Normas Urbanísticas annex 14 en 18, documento de síntesis §1.2. Bewijstype 2.

### 2.2 De bouwparameters van Cumbre del Sol

Let op de eenheid: het plan uit 1975 werkt met **volumen in m³ per m² perceel**, niet met edificabilidad in m²t/m².

#### Vrijstaande woningen (art. 3.4)

| Parameter | Waarde |
|---|---|
| Parcela mínima | **800 m²**. Tot 25 % van de percelen mag kleiner, maar nooit onder 600 m², en het gemiddelde van de unidad turística moet ≥ 800 m² blijven |
| Volume | **0,8 m³/m²** over het netto perceel |
| Hoogte | **2 bouwlagen of 7 m** |
| Afstand tot de perceellijn | **4 m** voor gesloten bebouwing; **3 m** voor open delen zoals veranda's, pergola's en garages |
| Afstand tot andere percelen | **4 m** gesloten bebouwing |
| Afstand tot wegen en paden | **5 m** |
| Terrassen en zwembaden | Mogen **tegen de grens** aan |
| Aanbouwen aan de erfgrens | Toegestaan als twee percelen gelijktijdig en met één architectonisch ontwerp bouwen |

#### Rijtjes- en geschakelde woningen (art. 3.3)

| Parameter | Waarde |
|---|---|
| Parcela colectiva mínima | **1.000 m²**, notarieel ondeelbaar |
| Volume | Subzona A **1,20 m³/m²**, subzona B **1,50** (subzone B ingevoerd bij de wijziging van 1989) |
| Minimale woninggrootte | 40 m² |
| Hoogte | **2 bouwlagen of 7 m** |
| Afstand tot de grens | **4 m of ½ bouwhoogte** |
| Afstand tot weg of pad | **5 m**, bij een terreinhelling onder 30 % |
| Afstand tot de achtergrens | **7 m** voor gesloten bouwdelen |
| Onderlinge afstand losse blokken | 3 m als er ramen van woonvertrekken op uitkijken, anders 2 m |

#### Instalaciones singulares (art. 3.2, na het PRI van 2022)

| Subzone | Gebruik | Ocupación | Volume | Hoogte |
|---|---|---|---|---|
| TR-I | Winkels en diensten, hotels verboden | 20 % | ≤ 2 m³/m² | 7 m / 2 lagen |
| TR-II | Hotels en motels, winkels verboden | 30 % | ≤ 2 m³/m² | **14 m / 4 lagen** |
| TR-III | Cultuur, sport, recreatie | Volgens programma | Volgens programma | Volgens programma |
| Alle | Sinds het PRI Iris-Begonias | | | Parcela mínima **300 m²** |

Afstand tot grens en straatas voor deze typologie: ≥ ⅓ van de bouwhoogte, minimaal 3 m.

Bron: geconsolideerde Normas Urbanísticas annex 14, art. 3.2 t/m 3.4, blz. 161–165. Bewijstype 2.

#### Aanvullende regels die in de praktijk knellen

- **Hoogte op een helling** (art. 3.1.7 en per zone): de kroonlijn mag niet meer dan één meter uitsteken boven het hoogste punt van de hoogste perceelgrens. Op de steile hellingen van Cumbre del Sol is dat vaak strenger dan de 7 meter.
- **Overdekte buitenruimte** (art. 3.1.8.D): veranda's, pergola's en overdekte terrassen tellen niet mee in het volume, maar mogen **samen niet meer zijn dan 50 %** van de toegestane gesloten oppervlakte op de begane grond.
- **Erfafscheidingen** (art. 3.1.9.C): dicht metselwerk tot 1,20 m bij hellingen onder 30 %, getrapt tot 2 m daarboven, met daar bovenop tot 0,80 m groen of transparant gaas. Totaal dus 2,00 of 2,80 m.
- **Tweede bouwlaag nooit groter dan de eerste** (art. 3.1.8.B). Elke volgende laag idem.

Bewijstype 2.

### 2.3 Van m³/m² naar m²t/m² — een bruikbare omrekening

Het rekenmodel van de Deal Hunter werkt in m² bruto vloeroppervlak. Het plan van 1975 in m³. Die twee zijn hier te koppelen, omdat één wijziging beide eenheden noemt voor dezelfde zone.

De wijziging van 27-09-1989 verhoogde de edificabilidad in sommige zones voor rijtjeswoningen **van 0,48 naar 0,60 m²t/m²s** (documento de síntesis, §1.2 nr. 3). Diezelfde wijziging voerde subzona B in. De geconsolideerde tekst noemt voor die zones subzona A **1,20 m³/m²** en subzona B **1,50**.

Dus:

```
1,20 m³/m²  ↔  0,48 m²t/m²     1,20 / 0,48 = 2,5
1,50 m³/m²  ↔  0,60 m²t/m²     1,50 / 0,60 = 2,5
```

De gemeente rekent met **2,5 m³ per m² vloeroppervlak**. Toegepast op de vrijstaande zone:

```
0,8 m³/m² ÷ 2,5 = 0,32 m²t/m²
```

Op een perceel van 800 m² komt dat neer op **ongeveer 256 m² bouwvolume**.

De koppeling 1,20 ↔ 0,48 en 1,50 ↔ 0,60 is bewijstype 2. De doorvertaling naar de vrijstaande zone is **bewijstype 5**: een afleiding, geen plantekst. Gebruik hem voor een eerste doorrekening en laat hem per perceel bevestigen.

### 2.4 Is de urbanisatie aan de gemeente opgeleverd?

Dit is de enige harde uitsluiting van Jan, dus hier het bewijs aan beide kanten.

#### Wat wijst op níet opgeleverd

| Bevinding | Bron | Type |
|---|---|---|
| **Alle veertien vlakken die in Benitatxell als *suelo urbano* staan, liggen in en om de dorpskern** — tussen 38,7305 en 38,7338 NB en 0,1388 en 0,1512 OL. Het grootste is 86,8 ha rond 38,7317 / 0,1422. In het hele kustgebied van Cumbre del Sol staat **geen enkel** vlak als suelo urbano | Eigen WFS-analyse van 225 vlakken, laag `Planeamiento.Clasificacion` en `.Zonificacion`, [terramapas.icv.gva.es](https://terramapas.icv.gva.es/0702_Planeamiento?service=WFS&request=GetCapabilities) | 3 |
| Het kustgebied telt 35 vlakken **SUZ / ZND-RE** ("zona de nuevo desarrollo residencial") en 5 **SUZ / ZND-TR**, plus 15 vlakken beschermd SNU-P onder het Plan Especial Puig de la Llorença | idem | 3 |
| Het plan zelf omschrijft Cumbre del Sol als *"Ordenación de suelo urbanizable residencial"* | Documento de síntesis §1.3 nr. 1 | 2 |
| Art. 3.1.4.B van het plan parcial: de infrastructuur en de openbare ruimte gaan over naar de **eigenarenverenigingen**, en tot die tijd blijven ze bij de ontwikkelaar — *"salvo que se haga cesión al Ayuntamiento u otros Organismo Público por acuerdo mutuo"* | Geconsolideerde tekst, annex 14, blz. 159 | 2 |
| De Normas Subsidiarias bakenen **geen áreas de reparto of unidades de ejecución** af, *"por no tenerlas previstas el planeamiento vigente"* — het is een plan van vóór dat stelsel | Documento de síntesis §3.6 | 2 |

#### Wat wijst op wél (deels) overgenomen

| Bevinding | Bron | Type |
|---|---|---|
| De gemeente heeft de straten in Cumbre del Sol laten asfalteren, samen met La Joya en Les Fonts | Gemeentelijk nieuwsbericht, [elpoblenoudebenitatxell.com](https://elpoblenoudebenitatxell.com/va/1575-finalizan-con-exito-los-trabajos-de-asfaltado-en-las-urbanizaciones-cumbre-del-sol-la-joya-y-les-fonts/) | 4 |
| Gemeentebedrijf **Poble Net S.L.** heeft sinds eind 2025 een ploeg van twee man die uitsluitend Cumbre del Sol en de andere bergurbanisaties onderhoudt: groen, wegen, paden, palmen | [elperiodic.com](https://www.elperiodic.com/palicante/benitatxell-gran-paso-lucha-contra-malas-hierbas-mantenimiento-caminos-zonas-verdes_1052123) en het gemeentelijke persbericht | 4 / 6 |
| De gemeente repareerde de brievenbussen van de urbanisatie | [javea.com, 16-12-2015](https://www.javea.com/los-buzones-de-la-urbanizacion-cumbres-del-sol-seran-reparados-por-el-consistorio-de-benitatxell/urbanizacion-cumbre-del-sol/) | 6 |

#### Conclusie

**Niet vastgesteld, en dat is geen vrijbrief.** Ik heb geen enkel besluit gevonden waarin de gemeente de urbanisatie formeel in ontvangst neemt, en ook geen besluit waarin dat wordt geweigerd. Wat ik wél vond wijst twee kanten op: de planologische status is ruim vijftig jaar na goedkeuring nog altijd *urbanizable*, terwijl de gemeente er feitelijk wegen en groen onderhoudt.

Dat laatste is juridisch relevant. In het Spaanse bestuursrecht kan onderhoud door de gemeente uitmonden in *recepción tácita*, stilzwijgende oplevering. Maar of dat hier speelt, en voor welke delen, is een vraag voor een urbanismo-advocaat, niet voor een rapport. **Bewijstype 7.**

Praktisch: Cumbre del Sol bestaat uit afzonderlijke unidades de ejecución die in verschillende jaren zijn aangelegd. De officiële stukken noemen er onder meer U3L, U3M (Magnolias), U2J (Jazmines), U3P (Palmeras), Z-I en het gebied Olivos – Pueblo del Mar (bewijstype 2). Het totale aantal deelgebieden staat niet in een officiële bron die ik heb gezien — bewijstype 7. De oplevering kan per deelgebied verschillen. Behandel de vraag dus per object, niet per urbanisatie.

### 2.5 VAPF heeft een vetorecht op je bouwplan

Artikel 3.1.5.B van het plan parcial, nog altijd in de geconsolideerde tekst:

> Met het oog op het esthetische aanzien van het geheel en voorafgaand aan de gemeentelijke vergunningprocedure worden de bouwplannen ter goedkeuring voorgelegd aan de ontwikkelaar of, in voorkomend geval, aan het bestuur van de eigenarenvereniging. Geen werk mag zonder die voorwaarde beginnen.

Bewijstype 2. Vrije weergave van de Spaanse tekst.

Dat is geen formaliteit. Wie in Cumbre del Sol koopt om te ontwikkelen, heeft naast de gemeente een tweede partij nodig die ja zegt — en die partij is tegelijk de grootste concurrerende aanbieder in hetzelfde gebied. Voor route A (kopen, renoveren, verkopen) is dat te overzien zolang het om onderhoud binnen de bestaande contour gaat. Voor route B (grond en projectontwikkeling) is het een risico dat in de prijs hoort.

Aanvullend: art. 3.1.4.A meldt dat het grootste deel van de grond eigendom is van V.A.P.F., S.A., dat tevens de ontwikkelaar is. Wat er sinds 1975 is verkocht, staat daar niet.

Ook interessant: art. 3.1.1.C bepaalt dat de voorschriften in de splitsingsakte en in het eigendomsregister worden opgenomen en **elke opvolgende koper binden**. Laat de nota simple en de escritura daarop nakijken.

### 2.6 Wat er in het gebied beschermd is

Het Plan Especial de protección del Puig de la Llorença (Conseller COPUT 13-06-1988) beschermt de Puig de la Llorença en Les Morres. Daarbij verdween de zone "poblado marítimo" met de geplande jachthaven, en verviel de bouwmogelijkheid daar.

In de kaartlaag van de Generalitat beslaan de vlakken onder dit plan samen ruim **1.100 hectare** in het kustgebied, geclassificeerd als SNU-P / ZRP-NA-MU. Bewijstype 3 (eigen telling van begrenzingsvakken; de opgegeven oppervlakte is die van de omhullende rechthoeken en dus een bovengrens).

Praktisch: een deel van wat in advertenties als "perceel in Cumbre del Sol" wordt aangeboden, kan in dit beschermde gebied liggen. Controleer dat vóór elke waardering.

---

## 3. Teulada-Moraira

### 3.1 Welk plan geldt

| Wat | Antwoord | Bron | Type |
|---|---|---|---|
| Soort plan | **PGOU** (Plan General de Ordenación Urbana) | [DOGV nº 10013, 26-12-2024](https://dogv.gva.es/datos/2024/12/26/pdf/2024_13025_es.pdf) | 2 |
| Goedkeuring | Comisión Territorial de Urbanismo de Alicante, **21-12-2004** | idem | 2 |
| Publicatie | BOP Alicante **21-01-2005**, met correctie van fouten in het BOP van **24-02-2005**; DOGV **02-03-2005** | idem | 2 |
| Wettelijk kader | Opgesteld en goedgekeurd onder de **LRAU** (Ley 6/1994 van 15-11-1994) | idem | 2 |
| Milieubeoordeling | DIA van 24-11-2003, positief onder voorwaarden, expediente 374-2002-AIA; gunstige resolutie 09-07-2004 | idem | 2 |
| Vorig plan | Revisión y adaptación van het PGOU, definitief goedgekeurd **23-09-1986**, BOE nº 246 van 14-10-1986 | [BOE-A-1986-27201](https://www.boe.es/diario_boe/txt.php?id=BOE-A-1986-27201) | 4 |
| Bevestiging dat het 2004-plan geldt | *"El planeamiento vigente en el municipio de Teulada es el Plan General de Ordenación Urbana aprobado por la Comisión Territorial de Urbanismo de Alicante con fecha 21 de diciembre de 2004"* — gemeentelijke publicatie van december 2024. Dezelfde formulering in een gemeentelijke publicatie van 2017 | DOGV 26-12-2024; [DOGV 20-07-2017](https://dogv.gva.es/datos/2017/07/20/pdf/2017_5882.pdf) | 2 |

### 3.2 De gedeeltelijke vernietigingen door de rechter

Dit is het belangrijkste verschil met Benitatxell: het Teuladese plan is meermaals bij de rechter onderuitgegaan, maar **niet in zijn geheel**.

| Uitspraak | Wat werd vernietigd | Grond | Bron | Type |
|---|---|---|---|---|
| Sentencia TSJCV **703/2007** | Het gebied **UBA-8** van het Plan General | Niet vermeld | Attribuut `denominaci` op zes vlakken in de kaartlaag van de Generalitat, eigen WFS-uitvraag | 3 |
| TSJCV **10-02-2009**, bevestigd door de Tribunal Supremo | Het gebied **UBA-8** in El Portet | Het plan is goedgekeurd **zonder het bindende rapport** van de Confederación Hidrográfica del Júcar over de bescherming van waterlopen. Eiser: vereniging SOS Moraira-Teulada | [teuladamorairadigital.es, 05-10-2012](https://teuladamorairadigital.es/archive/2524/el-tribunal-supremo-anula-el-acuerdo-de-aprobacion-del-pgou-de-teulada) | 1 (pers) |
| Tribunal Supremo **18-07-2013** | Gedeeltelijk het PGOU van 2004 én het PAI van sector **UZO-2** uit november 2005 | Gebrek aan motivering voor het toewijzen van de groenzone van sector UZO-F aan het winstgevende sector UZO-2, op meer dan vijf kilometer afstand | [teuladamorairadigital.es, 11-11-2014](https://teuladamorairadigital.es/archive/5016/el-ayuntamiento-cumple-la-sentencia-que-anula-en-parte-el-pgou-aprobado-en-2004-y-un-pai-del-2005) | 1 (pers) |

De twee eerste regels kunnen dezelfde zaak zijn, in verschillende instanties, of twee verschillende zaken. De uitspraken zelf heb ik niet gelezen — die staan niet in een bron die geautomatiseerd toegankelijk is. **Bewijstype 7 voor de precieze samenhang.**

Wat wel vaststaat: de gemeente bleef daarna modificaciones op hetzelfde plan vaststellen, tot en met nummer 38 in 2024, en noemt het plan in officiële stukken onverkort "vigente". De vernietigingen raakten dus afgebakende gebieden, niet het plan als geheel.

**Voor de praktijk:** ligt een object in of tegen UBA-8 (El Portet), UZO-2 of UZO-F, behandel het planregime dan als onzeker tot de gemeente schriftelijk het tegendeel bevestigt.

### 3.3 De zones volgens de kaartlaag van de Generalitat

De 524 vlakken in Teulada, uit de eigen WFS-uitvraag van 18-09-2026. Dit zijn de geharmoniseerde zonecodes van de Generalitat, **niet** de gemeentelijke zonecodes uit het PGOU.

| Klasse | Aantal vlakken |
|---|---|
| SU — suelo urbano | 241 |
| SUZ — suelo urbanizable | 106 |
| SNU-C — suelo no urbanizable común | 92 |
| SNU-P — suelo no urbanizable protegido | 85 |

| Zonecode | Omschrijving | Aantal |
|---|---|---|
| ZUR-RE | Zona urbanizada residencial | 188 |
| ZND-RE | Zona de nuevo desarrollo residencial | 93 |
| ZRC-AG | Zona rural común agropecuaria | 91 |
| ZUR-TR | Zona urbanizada terciaria | 38 |
| ZRP-CA | Zona rural protegida cauces (waterlopen) | 32 |
| ZRP-AG | Zona rural protegida agrícola | 24 |
| ZRP-CT | Zona rural protegida costas | 14 |
| ZRP-NA-MU | Zona rural protegida municipal | 12 |
| **ZUR-NHT** | **Zona urbanizada núcleo histórico tradicional** | **12** |
| ZND-TR | Zona de nuevo desarrollo terciaria | 7 |
| ZND-IN | Zona de nuevo desarrollo industrial | 6 |
| ZRP-NA-LG | Zona rural protegida legislación medioambiental | 3 |
| ZUR-IN | Zona urbanizada industrial | 3 |
| ZRC-EX | Zona rural común de explotación de recursos | 1 |

Bron: eigen WFS-uitvraag, laag `ms:Planeamiento.Zonificacion`, 18-09-2026. Bewijstype 3.

Bijna alles hangt aan expediente **20031342**, "Plan general" (498 vlakken). Daarnaast: Modificación nº 11 (10 vlakken, exp. 20110030), Modificación nº 1 (3), Modificación nº 18 (1), PATIVEL (3), een PRI comercial (3) en de zes vlakken van de vernietigde UBA-8.

### 3.4 Teulada tegenover Moraira — er zit wel degelijk verschil in

Ik heb de 524 vlakken gesplitst op 38,712 NB: daaronder ligt de kust (Moraira), daarboven het binnenland (Teulada). Grof, maar het beeld is eenduidig.

| Zone | Teulada, binnenland | Moraira, kust |
|---|---|---|
| ZUR-RE — bestaand woongebied | 46 vlakken | **142 vlakken** |
| ZND-RE — nieuw woongebied | 19 | **74** |
| ZRC-AG — agrarisch | **59 vlakken, ca. 2.788 ha** | 32 |
| ZUR-TR — winkels en horeca | 2 | **36** |
| ZRP-CT — kustbescherming | 0 | **14** |
| ZRP-NA-LG — beschermd bij milieuwet | 0 | 3 |
| **ZUR-NHT — historische kern** | **11 vlakken, ca. 17,8 ha** | **1 vlak, 0,6 ha** |
| ZND-IN + ZUR-IN — bedrijventerrein | **9** | 0 |
| Totaal | 175 vlakken | 349 vlakken |

Bron: eigen WFS-uitvraag en ruimtelijke indeling, 18-09-2026. Bewijstype 3 voor de zonegegevens, bewijstype 5 voor de indeling in twee kernen. Oppervlakten zijn die van de omhullende rechthoeken en dus een bovengrens.

Wat dit betekent:

**De historische kern zit in Teulada, niet in Moraira.** Elf van de twaalf ZUR-NHT-vlakken liggen rond 38,729 / 0,102 — het oude dorp op de heuvel. Moraira heeft één klein vlak van 0,6 ha rond 38,687 / 0,136, het oude kerngebied bij de kerk. Voor renovatieprojecten in een beschermde kern is Teulada dus het adres, en is het volume daar klein.

**Moraira is het woongebied.** Twee derde van alle vlakken en vrijwel alle bestaande woonzones liggen aan de kust. Daar zit ook al het terciaire vastgoed: 36 tegen 2.

**Teulada is agrarisch achterland.** Bijna 2.800 hectare ZRC-AG. Interessant voor route B, maar met de TRLOTUP-drempel van 1 hectare per woning.

**Alleen Moraira heeft kustbescherming.** Veertien vlakken ZRP-CT plus drie ZRP-NA-LG. Objecten in de eerste lijn moeten langs PATIVEL en de kustwet — een zelfstandige controle bij elke waardering.

### 3.5 De zone AIS en de vergunningstop voor twee-onder-een-kap

Dit is het punt waar in Teulada het meeste geld in omgaat, en het staat op losse schroeven.

| Feit | Bron | Type |
|---|---|---|
| De zone **AIS** (viviendas aisladas) kent de subzones **UBO** (suelo urbano), **UZE** (suelo urbano en ejecución) en **UZI** (suelo urbanizable met gedetailleerde ordening) | DOGV 26-12-2024, §4 | 2 |
| Het PGOU van 2004 stond in AIS **één vrijstaande woning per perceel** toe | idem, §1 | 2 |
| UBO beslaat **7.727.200 m²** bij een dichtheid van **7 woningen per hectare** en biedt ruimte aan **5.409 woningen**. UZE 387.452 m² / 337 woningen. UZI 166.949 m² / 107 woningen | idem, Alternativa 0 | 2 |
| De drie zones samen: 5.853 woningen, oftewel 14.633 inwoners bij 2,5 per woning — de helft van de 29.195 inwoners waarvoor het plan is ontworpen | idem | 2 |
| **Modificación nº 1** (CTU 20-11-2006) en **nº 19** (Pleno 07-03-2013) maakten **twee geschakelde woningen per perceel** mogelijk, tegen een financiële compensatie aan de gemeente | idem | 2 |
| Dat verdubbelt het potentieel naar 11.706 woningen en 29.266 inwoners in alleen die zones | idem | 2 |
| **Sinds 05-02-2024 zijn vergunningen voor nieuwe twee-onder-een-kapwoningen in AIS-1 en AIS-2 binnen suelo urbano (UBO) geschorst.** Raadsbesluit van 18-01-2024, gepubliceerd in DOGV nº 9781 van 05-02-2024, **voor maximaal twee jaar** | idem | 2 |
| **Modificación nº 38** moet de typologie terugbrengen naar één woning per perceel (Alternativa 1). Gunstig milieurapport van 03-12-2024, gepubliceerd 26-12-2024. Het Servicio Territorial de Urbanismo in Alicante gaf op 07-11-2024 een gunstig advies | idem | 2 |
| Het milieurapport vervalt als het plan niet **binnen vier jaar na publicatie** is vastgesteld — dus uiterlijk **26-12-2028** | idem, punt Cuarto | 2 |
| Andere modificaciones die AIS raken: nº 1 op art. 6.10 (structureel) en nº 1, 2, 5 en 19 op art. 6.11 (gedetailleerd) | idem, §3 | 2 |
| Modificación nº 2/2005 (BOP nº 26 van 01-02-2006) liet commercieel gebruik in AIS toe via een PRI, en gebruik TC aan de CV-746 Moraira–Calp | [DOGV 20-07-2017](https://dogv.gva.es/datos/2017/07/20/pdf/2017_5882.pdf) | 2 |
| Er bestaat ook een typologie **BE** (bloque exento) binnen AIS-2, en de zones **ADO** (rijtjeswoningen) en **TER** (terciair) | DOGV 20-07-2017 en [DOGV 10-07-2008](https://dogv.gva.es/datos/2008/07/10/pdf/2008_7548.pdf) | 2 |

**Waar het nu staat: onbekend.** De schorsing van 05-02-2024 liep maximaal twee jaar, dus tot omstreeks 05-02-2026. Vandaag is het 18-09-2026. Ik heb geen bron gevonden waaruit blijkt of modificación nº 38 inmiddels definitief is vastgesteld, of de schorsing is verlengd, of dat beide zijn afgelopen en de regel van twee geschakelde woningen weer geldt. **Bewijstype 7.** Dit is de belangrijkste openstaande vraag voor Teulada.

De richting is wel duidelijk. De gemeente motiveert het met drinkwater, riolering en wegbreedte, en noemt daarbij expliciet dat de watervoorziening van **Teulada én Benitatxell** uit balans raakt. Dat sluit aan op het bericht dat Xàbia in juli 2026 noodwater aan beide gemeenten begon te leveren ([lamarina.eldiario.es, 14-07-2026](https://lamarina.eldiario.es/2026/07/14/xabia-comenzo-a-enviar-la-pasada-semana-agua-de-urgencia-a-teulada-y-benitatxell-sin-haberse-cerrado-el-precio/), bewijstype 1). Water is in dit werkgebied een planologische rem geworden, niet alleen een nutsvoorziening.

### 3.6 Wat voor Teulada ONBEKEND blijft

Jan vroeg per woonzone om edificabilidad, ocupación, hoogte, minimale perceelgrootte en afstanden. Voor Benitatxell staat dat hierboven. **Voor Teulada kan ik het niet leveren.**

| Waarom | Type |
|---|---|
| De normativa van het PGOU 2004 is gepubliceerd in het BOP Alicante van 21-01-2005. Het BOP-archief op `www.dip-alicante.es` staat op `Disallow: /` voor alle user-agents | 1 |
| De geconsolideerde teksten en het planregister van de Generalitat staan op `mediambient.gva.es`, dat Claude-agents expliciet uitsluit | 1 |
| De gemeentesite `teuladamoraira.com.es` publiceert onder Urbanisme alleen een stratenregister en een kaartverwijzing, geen normativa | 1 |
| Het gemeentelijke geoportaal heeft wél een laag "Consulta PGOU" (laag-id 1164, via `visorteulada.geonet.es`), maar die is alleen via de kaartviewer te bevragen | 1 |
| Teulada heeft, anders dan Benitatxell, **geen geconsolideerde tekst op de eigen website** gezet | 1 |

Wat ik wél weet over de parameters, is dit: in UBO geldt een dichtheid van **7 woningen per hectare** (bewijstype 2). Dat is een structurele bovengrens, geen perceelregel, maar het geeft een orde van grootte: gemiddeld zo'n 1.430 m² perceel per woning.

**Verzin de rest niet.** Voor elk Teulada-object hoort een ficha urbanística of informe urbanístico van de gemeente in het dossier voordat er een richtprijs uit het model rolt.

---

## 4. Kosten: ICIO in Benitatxell

Relevant voor het rekenmodel, en gunstiger dan in Jávea.

| Onderdeel | Benitatxell | Jávea (ter vergelijking) |
|---|---|---|
| Tarief ICIO | **3 %** | 4 % (R12 §8) |
| Grondslag | De **hoogste** van: de begroting van de aanvrager, ondertekend door een bevoegd technicus of de aannemer, óf het gemeentelijke kostenmodel uit Anexo I | — |
| Buiten de grondslag | Btw, leges, honoraria van adviseurs en de winst van de aannemer | — |
| Verschuldigd vanaf | Het moment waarop het werk begint, ook zonder vergunning | — |

Kortingen (art. 7), **niet stapelbaar** — de hoogste geldt, en je moet er bij de vergunningaanvraag expliciet om vragen:

| Situatie | Korting |
|---|---|
| Renovatie binnen de aangewezen zone **Núcleo de Impulso Urbano (NIU)**, gedeeltelijk: dak, gevel of inpandig | **40 %** |
| Idem, integraal, mits traditionele bouwelementen en materialen behouden blijven | **80 %** |
| Nieuwe economische activiteit in de aangewezen zones van het casco | 50 % |
| Sociale woningbouw (VPO) | 50 % |
| Toegankelijkheid: lift, drempelvrije route — alleen bij renovatie, nooit bij nieuwbouw, en alleen over dat deel van de begroting | 90 % |
| Zonne-energie voor eigen gebruik, alleen over dat deel van de begroting | 50 % |
| Herstel of nieuwbouw van droge steenmuren op landbouwterrassen in SNU | 100 % |

Bron: Ordenanza fiscal reguladora del ICIO, definitieve wijziging na het raadsbesluit van 22-03-2024, gepubliceerd in het BOP Alicante nº 96 van 21-05-2024, aankondiging 3936/2024. [Pdf op de gemeentesite](https://elpoblenoudebenitatxell.com/wp-content/uploads/2024/12/20240521_Otros_BOP-2024_003936_ICIO.pdf). Bewijstype 4.

**Let op de reikwijdte.** De renovatiekortingen van 40 en 80 % gelden alleen binnen de NIU-zone uit Anexo II van de verordening. Cumbre del Sol valt daar vrijwel zeker buiten, maar de bijlage met de begrenzing heb ik niet gezien — **bewijstype 7**. Reken voor de urbanisaties dus op de volle 3 %.

Het tarief van Teulada is ONBEKEND: de fiscale verordeningen staan niet openbaar op de gemeentesite en het BOP-archief is dicht.

---

## 5. Wat hiervan direct het rekenmodel in kan

| Gegeven | Waarde | Waar te gebruiken | Type |
|---|---|---|---|
| ICIO Benitatxell | 3 % over de bouwkosten exclusief btw, honoraria en aannemerswinst | Kostenparameter per gemeente in `kader/` | 4 |
| Omrekening Cumbre del Sol | Volume ÷ **2,5** = m²t/m²s | Bouwvolume uit een perceeloppervlak | 5 (afgeleid uit 2) |
| Cumbre del Sol, vrijstaand | Perceel min. 800 m²; ca. **0,32 m²t/m²**; 2 lagen / 7 m; 4 m tot grens, 5 m tot weg | Voorfilter op perceeladvertenties | 2 + 5 |
| Cumbre del Sol, rijtjes | Perceel min. 1.000 m²; **0,48** of **0,60 m²t/m²**; 2 lagen / 7 m | idem | 2 |
| Benitatxell, turístico-residencial | 700 / 1.000 / 5.000 m² naar typologie; 30–35 % ocupación; **0,25 m²t/m²**; 2 lagen; 16 won./ha | idem | 2 |
| Benitatxell, ciudad jardín | 500 m² bij 0,60 of 700 m² bij 0,50 m²t/m²; 25–30 % ocupación; 2 lagen; 20 won./ha | idem | 2 |
| Benitatxell, casco | Geen minimale perceelgrootte; 2/3/4 lagen = 7,20 / 10,20 / 13,20 m | Splitsingsprojecten in de kern | 2 |
| Benitatxell, SNU | Reken op **1 ha per woning** (TRLOTUP), niet op de 2.500 of 5.000 m² uit het plan | Perceelfilter | 5 (op basis van 2) |
| Teulada, UBO | Dichtheid **7 woningen per hectare** | Grove bovengrens | 2 |
| **Uitsluitingsvlag Teulada** | Objecten in of naast **UBA-8**, **UZO-2** of **UZO-F**: planregime onzeker | Signaalregel in `dh/` | 1/7 |
| **Uitsluitingsvlag Teulada** | Aannames met **twee geschakelde woningen op één perceel** in AIS-1 of AIS-2: niet doorrekenen zonder bevestiging | Signaalregel | 2 |
| **Uitsluitingsvlag Benitatxell** | Objecten in de zone van het **Plan Especial Puig de la Llorença** (SNU-P): geen nieuwbouw | Signaalregel, te koppelen aan de WFS-laag | 3 |

De WFS-dienst `https://terramapas.icv.gva.es/0702_Planeamiento` is hiervoor bruikbaar: geen robots.txt, open licentie CC BY 4.0, en op een punt of een bbox te bevragen. Het veld `clas_suelo` geeft SU, SUZ, SNU-C of SNU-P en `zon_suelo` de zonecode. Daarmee kan het dashboard bij elk object meteen tonen of het in urbanizable of beschermd gebied ligt. **Juridisch is die laag informatief, niet bindend** — als filter prima, als bewijs niet.

---

## 6. Openstaande punten

### ⏸️ ACTIE VOOR JAN

Drie vragen, in deze volgorde.

**1. Cumbre del Sol — is de urbanisatie opgeleverd?**
Vraag het Ayuntamiento de El Poble Nou de Benitatxell schriftelijk, per deelgebied, niet voor de urbanisatie als geheel. De vraag luidt: is er een besluit tot *recepción de las obras de urbanización* voor het deelgebied waarin het perceel ligt, en zo nee, wie is verantwoordelijk voor onderhoud en aansluitingen — de gemeente, een *entidad urbanística de conservación*, of de ontwikkelaar? Vraag er meteen bij of het perceel als *solar* geldt.
Dit is de enige vraag die jouw harde uitsluiting kan beantwoorden. Alles wat ik online vond wijst twee kanten op.

**2. Teulada — geldt de vergunningstop voor twee-onder-een-kap nog?**
Vraag de afdeling Urbanisme van Teulada wat de stand is van modificación puntual nº 38, en of de schorsing uit DOGV nº 9781 van 05-02-2024 is verlengd of afgelopen. Zolang dat onduidelijk is, mag geen enkel Teulada-object in het model op twee woningen per perceel worden gerekend.

**3. Teulada — vraag de normativa op.**
De gemeente heeft, anders dan Benitatxell, geen geconsolideerde tekst online. Vraag om de geldende normas urbanísticas van het PGOU 2004, of minstens om de artikelen 6.10 en 6.11. Zonder dat blijft Teulada in ons model op schattingen draaien terwijl Benitatxell op plantekst draait.

### Voor het bronnenregister

| Regel | Voorstel |
|---|---|
| `mediambient.gva.es` (planregister GVA) | Status → **ALLEEN HANDMATIG**. robots.txt sluit Claude-agents uit sinds uiterlijk 18-09-2026 |
| `politicaterritorial.gva.es` | Idem |
| `www.dip-alicante.es` (BOP-archief) | Status → **UITGESLOTEN**. `Disallow: /` voor iedereen |
| `terramapas.icv.gva.es` — WFS planeamiento | Nieuwe regel, status **GEVERIFIEERD EN ACTIEF** na inbouw. Getest op 18-09-2026, 749 vlakken opgehaald voor twee gemeenten |
| `elpoblenoudebenitatxell.com` — WordPress REST API en documentenmap | Nieuwe regel. Geen robots.txt; `/wp-json/wp/v2/` geeft de planningsdocumenten en verordeningen gestructureerd terug |
| `dogv.gva.es` | Bruikbaar voor het volgen van planwijzigingen in beide gemeenten; pdf's met tekstlaag |
| `visorteulada.geonet.es` — laag "Consulta PGOU" | Kandidaat. Eigen host zonder robots.txt, moederdomein `geonet.es` staat `*` toe met crawl-delay 5 s. Eerst toestemming van de gemeente vragen voordat we er iets op bouwen |

### Interpretatievragen die ik niet heb geforceerd

| # | Vraag | Type |
|---|---|---|
| T1 | Is TSJCV 703/2007 dezelfde zaak als de uitspraak van 10-02-2009, of twee zaken? | 7 |
| T2 | Welke delen van het PGOU 2004 zijn precies vernietigd door de TS-uitspraak van 18-07-2013? | 7 |
| B1 | Geldt voor Residencial de ensanche de regel 500 m² / 0,60 of 700 m² / 0,50, en waar welke? | 7 |
| B2 | Is het PRI Iris-Begonias goedgekeurd in 2018 of in 2022? De geconsolideerde tekst noemt beide | 7 |
| B3 | Is het BOP-nummer van 25-02-1975 nº 45 of nº 46? | 7 |
| B4 | Waar loopt de NIU-grens uit Anexo II van de ICIO-verordening? Bepaalt of de renovatiekorting van 80 % ergens buiten het casco geldt | 7 |
| B5 | Geldt in Benitatxell in SNU nu 2.500 m², 5.000 m² of 1 hectare? De plantekst spreekt zichzelf tegen en de regionale wet gaat er hoe dan ook overheen | 7 |

---

## 7. Bronnen

**Benitatxell — officieel**
- Normas Urbanísticas, geconsolideerde tekst (187 blz.): https://elpoblenoudebenitatxell.com/wp-content/uploads/2025/12/1.2-NN-UU-Text-Consolidat_Benitatxell-V05_signat_signed.pdf
- Documento de síntesis: https://elpoblenoudebenitatxell.com/wp-content/uploads/2025/12/1.1-Document-de-sintesi_Benitachell-V05_signat_signed.pdf
- Kaart OP-11, Cumbres del Sol en Enclaves: https://elpoblenoudebenitatxell.com/wp-content/uploads/2025/12/OP-11_Urbanizacion-Cumbres-del-Sol-Enclaves_signat_signed.pdf
- Kaart OE-01, classificatie van de grond: https://elpoblenoudebenitatxell.com/wp-content/uploads/2025/12/OE-01_Clasificacion_suelo_signat_signed2.pdf
- ICIO-verordening, BOP nº 96 van 21-05-2024: https://elpoblenoudebenitatxell.com/wp-content/uploads/2024/12/20240521_Otros_BOP-2024_003936_ICIO.pdf
- Raadsbesluit 13-05-2024, uitleg van de PP-normativa voor terciair gebruik in Olivos / Pueblo del Mar: https://elpoblenoudebenitatxell.com/wp-content/uploads/2025/12/CRITERIO-INTERPRETATIVO-NORMATIVA-PP-CUMBRE-DEL-SOL-USOS-TERCIARIOS-ZONA-OLIVOS-PUEBLO-DEL-MAR.pdf
- Gemeentelijke documentenlijst via de REST API: https://elpoblenoudebenitatxell.com/wp-json/wp/v2/recurso_urbanismo?per_page=100

**Teulada — officieel**
- DOGV nº 10013 van 26-12-2024, milieurapport modificación nº 38: https://dogv.gva.es/datos/2024/12/26/pdf/2024_13025_es.pdf
- DOGV van 20-07-2017, PRI en estudio de detalle CV-746: https://dogv.gva.es/datos/2017/07/20/pdf/2017_5882.pdf
- DOGV van 10-07-2008, bases particulares PAI UBA-7: https://dogv.gva.es/datos/2008/07/10/pdf/2008_7548.pdf
- DOGV nº 5347 van 15-09-2006, modificación nº 3: https://dogv.gva.es/datos/2006/09/15/pdf/2006_M9872.pdf
- BOE-A-1986-27201, definitieve goedkeuring revisie PGOU Teulada 1986: https://www.boe.es/diario_boe/txt.php?id=BOE-A-1986-27201

**Kaartdata**
- WFS planeamiento Generalitat Valenciana: https://terramapas.icv.gva.es/0702_Planeamiento?service=WFS&request=GetCapabilities
- Kaartviewer: https://visor.gva.es/visor/?capas=spaicv0702_plan_clasificacion
- Geoportaal Teulada-Moraira: https://geoportal.teuladamoraira.org/

**Pers en secundair (bewijstype 1 en 6)**
- Tribunal Supremo vernietigt het goedkeuringsbesluit van het PGOU Teulada, 05-10-2012: https://teuladamorairadigital.es/archive/2524/el-tribunal-supremo-anula-el-acuerdo-de-aprobacion-del-pgou-de-teulada
- Gemeente voert de uitspraak uit die het PGOU 2004 en een PAI uit 2005 deels vernietigt, 11-11-2014: https://teuladamorairadigital.es/archive/5016/el-ayuntamiento-cumple-la-sentencia-que-anula-en-parte-el-pgou-aprobado-en-2004-y-un-pai-del-2005
- Onderhoudsploeg voor Cumbre del Sol: https://www.elperiodic.com/palicante/benitatxell-gran-paso-lucha-contra-malas-hierbas-mantenimiento-caminos-zonas-verdes_1052123
- Asfaltering Cumbre del Sol, La Joya en Les Fonts: https://elpoblenoudebenitatxell.com/va/1575-finalizan-con-exito-los-trabajos-de-asfaltado-en-las-urbanizaciones-cumbre-del-sol-la-joya-y-les-fonts/
- Brievenbussen Cumbre del Sol, 16-12-2015: https://www.javea.com/los-buzones-de-la-urbanizacion-cumbres-del-sol-seran-reparados-por-el-consistorio-de-benitatxell/urbanizacion-cumbre-del-sol/
- Xàbia levert noodwater aan Teulada en Benitatxell, 14-07-2026: https://lamarina.eldiario.es/2026/07/14/xabia-comenzo-a-enviar-la-pasada-semana-agua-de-urgencia-a-teulada-y-benitatxell-sin-haberse-cerrado-el-precio/
- VAPF over Cumbre del Sol: https://www.vapf.com/en/real-estate-developer/residential-areas/cumbre-del-sol

**Niet geraadpleegd wegens toegangsbeperking**
- `mediambient.gva.es` — planregister en geconsolideerde teksten van de Generalitat
- `politicaterritorial.gva.es`
- `www.dip-alicante.es` — BOP-archief Alicante
- De sedes electrónicas van Benitatxell en Teulada (zie de notitie in `CLAUDE.md` van 18-09-2026)

---

*Vaktermen: **PGOU** = Plan General de Ordenación Urbana, het gemeentelijke bestemmingsplan. **Normas Subsidiarias** = een lichtere planvorm voor kleine gemeenten, uit de tijd vóór de PGOU-plicht. **Plan parcial** = uitwerkingsplan voor één gebied. **PRI** = Plan de Reforma Interior, een herzieningsplan binnen bestaand gebied. **Suelo urbano** = bouwrijp stedelijk gebied. **Suelo urbanizable** = te ontwikkelen gebied, nog niet bouwrijp. **Suelo no urbanizable** = buitengebied. **Edificabilidad** = toegestaan vloeroppervlak per m² perceel. **Ocupación** = aandeel van het perceel dat bebouwd mag worden. **Parcela mínima** = kleinste perceel waarop gebouwd mag worden. **Retranqueo** = verplichte afstand tot de perceelgrens. **Recepción** = de formele overname van een urbanisatie door de gemeente. **ICIO** = de gemeentelijke bouwbelasting.*

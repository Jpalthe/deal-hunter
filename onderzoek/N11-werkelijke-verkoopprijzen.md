# N11 — Werkelijk betaalde verkoopprijzen per wijk: wat kunnen wij echt ophalen

Onderzoek voor TREE Deal Hunter · **26-09-2026** · werkgebied Jávea/Xàbia, Benitatxell, Teulada-Moraira
· alle HTTP-toetsen op die datum zelf uitgevoerd, hoogstens 1 verzoek per 2 seconden per host,
robots.txt vooraf gecontroleerd (ook voor `ClaudeBot`). `mediambient.gva.es` is niet bezocht.

**Bewijstypen (masterprompt §5):** 1 door aanbieder vermeld · 2 officiële bron · 3 door ons
vastgesteld · 4 AI-gevolgtrekking · 5 berekening · 6 professional · 7 onbekend of tegenstrijdig.

---

## Conclusie

1. **Ja, er bestaat een gratis, officiële bron met wérkelijke verkoopprijzen op wijkniveau, en die
   werkt vandaag: de *mapas de valores* van het Catastro.** Per gemeente wordt het grondgebied
   verdeeld in *ámbitos territoriales homogéneos* (Jávea 39 zones, Benitatxell 34, Teulada-Moraira 24)
   en per zone staat het *módulo de valor medio* van een representatieve woning. Het Catastro zegt
   zelf dat die modules uit de prijzen van álle notarieel verleden koopakten komen. Ik heb de dienst
   aangeroepen en de zones van de drie opgegeven percelen opgehaald (§1). Bewijstype 3 (eigen aanroep)
   op een bron van type 2.
2. **De valor de referencia per eenheid via Goolzoom is hiervoor níet de goede weg.** Hij werkt (2 van
   3 percelen gaven een bedrag), maar hij geeft alleen een getal zonder jaar, zonder zone en zonder
   onderbouwing, en hij hangt aan een kadastrale referentie die bij ons vaak niet het geadverteerde
   object is: over de 173 objecten die we al hebben, loopt valor de referencia ÷ vraagprijs van 0,07
   tot 12,4. Onbruikbaar als prijspeil (§2).
3. **Ministerio de Vivienda (MIVAU), Registradores, Notariado-CIEN en INE geven geen prijs per wijk.**
   Aantallen wél per gemeente (Jávea 276 verkopen in 2026T1), prijzen alleen per provincie of hoger.
   Eén uitzondering met echte waarde: MIVAU publiceert de **getaxeerde waarde per m² per gemeente**
   voor gemeenten boven 25.000 inwoners, en Jávea zit erin: **3.507,2 €/m² in 2026T2** (§3).
4. **Het Portal Estadístico del Notariado (penotariado.com) heeft precies wat wij willen — echte
   transactieprijzen per postcode, maandelijks — maar de voorwaarden verbieden commercieel gebruik.**
   De statistiek-API eist bovendien inloggen (ik heb géén account aangemaakt). Dit is een
   toestemmingsvraag, geen techniekvraag (§4). ⏸️ ACTIE VOOR JAN.
5. **Een "estadística de transmisiones" van het Catastro met prijzen bestaat niet.** De kadastrale
   statistiek gaat over het register (aantallen, gebruik, bouwjaren), niet over transacties (§7).
6. **Oordeel:** de Catastro-zonemodules zijn bruikbaar naast onze vraagprijzen, niet in plaats
   daarvan. Over onze acht wijken ligt de zonemodule op **0,53 tot 0,93 van onze vraagprijsmediaan**,
   mediaan ongeveer **0,70** (§8). De koppeling — tabel, matching op typologie en een waarschuwing in
   de rekensom — staat in §9.

Leeswijzer: §1 Catastro-waardekaarten · §2 Goolzoom/valor de referencia · §3 MIVAU · §4 Notariado ·
§5 Registradores · §6 INE · §7 kadastrale statistiek · §8 vergelijking en oordeel · §9 koppeling ·
daarna de acties voor Jan en de lijst van alle uitgevoerde verzoeken.

---

## 1. Catastro — *mapas de valores* / módulos de valor medio · **DIT IS DE VONDST**

### 1.1 Wat het is en waar het op rust

De Dirección General del Catastro stelt jaarlijks per gemeente *ámbitos territoriales homogéneos de
valoración* vast, definieert daarbinnen een representatief vastgoedproduct en berekent daarvoor een
*módulo de valor medio*. De FAQ van het Catastro zegt dat die modules zijn gebaseerd op de prijzen van
alle koopovereenkomsten die voor een notaris zijn gesloten of in het eigendomsregister zijn
ingeschreven, en dat zij overeenkomen met de gemiddelde prijzen van die koopovereenkomsten.
Bron: <https://www.catastro.hacienda.gob.es/es-ES/faqs.html> (opgehaald 26-09-2026, HTTP 200,
bewijstype 2).

Deze kaarten zijn de eerste stap naar de valor de referencia; de *factor de minoración* wordt pas
daarná op het individuele object toegepast. De module zelf is dus het **marktgemiddelde**, niet de
verlaagde fiscale waarde. (Zelfde FAQ-pagina.)

### 1.2 De dienst die wij werkelijk hebben aangeroepen

```
GET https://www1.sedecatastro.gob.es/Cartografia/SECDameGeoJSON.aspx
    ?del=03&mun=082&huso=3857&x=<X>&y=<Y>&suelo=N&tipo_mapa=vivienda&anyoZV=2027
```

Gevonden door de openbare kaartviewer van de Sede te lezen
(<https://www1.sedecatastro.gob.es/Cartografia/mapa.aspx?ZV=SI&BUSCAR=S&ANYOZV=2027&final=IAMIU>,
JavaScript `Cartografia/js/mapa.js`, functie `DameUrlZonasValor`). Geen sleutel, geen aanmelding,
geen certificaat.

Antwoord: `HTTP 200`, `application/geo+json`, ±1,1 MB, één FeatureCollection met alle zones van de
gemeente waarin het punt ligt. `del`/`mun` blijken genegeerd — **de coördinaat bepaalt de gemeente**
(vastgesteld 26-09-2026 door dezelfde `mun` met twee verschillende coördinaten aan te roepen:
verschillende antwoorden; bewijstype 3).

Per zone (feature) komen o.a. terug: `zona_valor`, `cod_zona` (de ATH-code), `num_inmuebles_uso_v`,
`area`, `ejercicio`, en een blok `Ptipo1` met `tipologia`, `superficie`, `superficie_suelo`,
`categoria`, `antiguedad`, `conservacion`, `val_tipo`, `val_tipo_m2`, `val_estandar`,
`val_estandar_m2`.

| Gemeente | del/mun | zones in antwoord | toetscoördinaat |
|---|---|---|---|
| Jávea/Xàbia | 3 / 82 | **39** | 0,1830 / 38,7647 |
| El Poble Nou de Benitatxell | 3 / 42 | **34** | 0,1636 / 38,7085 |
| Teulada-Moraira | 3 / 128 | **24** | 0,1430 / 38,6875 |

De kadastrale gemeentecodes zijn opgehaald bij het Catastro zelf: Teulada `cmc=128` via
`https://ovc.catastro.meh.es/ovcservweb/OVCSWLocalizacionRC/OVCCallejero.asmx/ConsultaMunicipio?Provincia=ALICANTE&Municipio=TEULADA`
(26-09-2026, HTTP 200), Benitatxell `del=03&mun=042` via de WMS-laag ZONA VALUE van
`https://ovc.catastro.meh.es/Cartografia/WMS/PonenciasWMS.aspx`.

### 1.3 De drie opgegeven percelen — werkelijke antwoorden

Punt-in-polygoon van de perceelcoördinaat op de opgehaalde zones (bewijstype 5 op bewijstype 3):

| Kadastrale referentie | Adres (uit `parcels`) | Zone | ATH-code | Representatief product | Module |
|---|---|---|---|---|---|
| `0481122BC5907N` | CL Penyaparda Prolg. 3 (El Garroferal) | **U21** | 36 | vrijstaand/geschakeld, 180 m² bebouwd, perceel 1.600 m², categorie Media, 50 jaar, Renovado (2.459 woningen in de zone) | **692.200 €** = 3.300 €/m² |
| `5246308BC5954N` | CL Jaume Huguet 6 (Adsubia) | **U20** | 127 | vrijstaand/geschakeld, 160 m² bebouwd, perceel 1.000 m², Media, 50 jaar, Renovado (3.025 woningen) | **547.400 €** = 3.200 €/m² |
| `6442010BC5964S` | PD Cam Cap Martí 317 (Tosalet) | **U20** | 127 | zelfde zone als hierboven | **547.400 €** = 3.200 €/m² |

Spreiding over heel Jávea (37 zones met een product): van **460 €/m²** (R30, 10 woningen) tot
**8.200 €/m²** (U11, 97 woningen). De duurste vijf: U11 8.200 · U08 7.300 · U10 6.800 · U15 6.700 ·
U14 5.800. Benitatxell topt op 8.900 €/m² (U10, 8 woningen), Teulada-Moraira op 8.900 €/m² (U05,
159 woningen).

### 1.4 Grenzen van wat dit zegt — belangrijk

- **Voor vrijstaande en geschakelde woningen publiceert het Catastro officieel een bedrag in euro's,
  niet een €/m².** De €/m² in de tabel hierboven is `val_tipo / superficie`; hij bevat dus óók de
  grondwaarde. Dat is goed nieuws voor ons, want onze vraagprijs per m² bebouwd bevat die ook — maar
  je mag hem niet vergelijken met een zuiver bouwkostenkental. (FAQ Catastro, 26-09-2026.)
- **De module hoort bij één specifiek product.** U20 gaat over een 50 jaar oude, gerenoveerde woning
  van 160 m² op 1.000 m². Een nieuwbouwvilla van 300 m² in diezelfde zone hoort daar niet bij.
- **Zones overlappen per typologie.** Van de 718 actieve objecten met coördinaat in onze database
  vielen er 375 binnen een waardezone, en **75 daarvan binnen twéé zones tegelijk** (een *vivienda
  colectiva*-zone en een *unifamiliar*-zone bovenop elkaar). De typologie van het object moet dus
  meebeslissen welke zone geldt — anders krijg je voor een villa het appartementenpeil. De overige
  343 liggen buiten elke stedelijke waardezone (rustieke grond, of een coördinaat die naast de
  bebouwing valt). Eigen berekening 26-09-2026, bewijstype 5.
- **`val_tipo_m2` versus `val_estandar_m2`:** in het antwoord staan twee reeksen, bijvoorbeeld U20
  3.200 en 3.600 €/m². Het verschil zit in `val_construccion_pt` tegenover `val_construccion_pe`. Wat
  die twee precies betekenen staat niet in de legenda die het Catastro publiceert
  (<https://www.catastro.hacienda.gob.es/ayuda/leyenda_mapavalores.htm>, 26-09-2026). **ONBEKEND** —
  na te zoeken in het *Informe Anual del Mercado Inmobiliario Urbano* (zie §8). De viewer zelf toont
  `val_tipo_mostrar`, dus de `val_tipo`-reeks; die houd ik daarom aan.
- **Afgeronde getallen.** De viewer rondt af op stappen van 25/50/100 (`redondeaPT` in `mapa.js`); de
  waarden in het JSON-antwoord zijn al afgerond (3.200, 3.300, 8.200 …).

### 1.5 Detailniveau, vertraging, rechten

| | |
|---|---|
| **Detailniveau** | zone binnen de gemeente (ATH). Jávea 39 zones — fijner dan onze acht wijken. |
| **Vertraging** | jaarlijks. De kaarten voor het VR-jaar **2027 zijn gepubliceerd op 25-09-2026** (één dag vóór dit onderzoek); het veld `ejercicio` in dat antwoord is **2026**. `anyoZV=2026` geeft `ejercicio` 2025, `anyoZV=2025` geeft niets terug. De waarnemingsperiode van de onderliggende transacties staat niet in het antwoord: **ONBEKEND**, na te lezen in het IAMIU. |
| **Rechten** | Aviso legal van het Catastro: gehele of gedeeltelijke reproductie van de inhoud van het portaal is toegestaan, mits de herkomst uitdrukkelijk wordt vermeld (<https://www.catastro.hacienda.gob.es/es-ES/avisolegal.html>, 26-09-2026). De WMS-dienst voegt toe: vrije toegang, maar massale download van kaartdelen is verboden (GetCapabilities van `PonenciasWMS.aspx`, veld `AccessConstraints`, 26-09-2026). Drie aanroepen per jaar (één per gemeente) blijft daar ruim binnen. |
| **Kosten** | nihil. |

---

## 2. Valor de referencia per eenheid via Goolzoom

Aangeroepen met de bestaande koppeling `dh/goolzoom.py` (sleutel uit `.env` via `config.load_env`,
nergens opgeschreven), 26-09-2026:

| Perceel | Eenheid (20 tekens) | `referencevalue` |
|---|---|---|
| `0481122BC5907N` (bouwgrond, *suelo sin edificar*, 1.622 m²) | `0481122BC5907N0001AI` | **leeg antwoord `{}`** — geen waarde |
| `5246308BC5954N` (woning, 275 m², 2005) | `5246308BC5954N0001TM` | **568.417,674375 €** |
| `6442010BC5964S` (woning, 251 m², 1973) | `6442010BC5964S0001US` | **372.752,112825 €** |

Waarom dit geen prijspeil per wijk oplevert:

1. **Het antwoord is kaal.** Alleen `{"referencevalue": <getal>}`. Geen jaar, geen zone, geen
   representatief product, geen module. Welk VR-jaar dit is: **ONBEKEND**.
2. **Het is per eenheid, niet per gebied.** Om een wijkpeil te maken zou je honderden eenheden moeten
   bevragen; dat kost geld (de sleutel is betaald, limiet 100.000 verzoeken per maand volgens de
   documentatie die op 25-09-2026 is gecontroleerd en in `dh/goolzoom.py` staat) terwijl het
   Catastro het gebiedsgemiddelde gratis weggeeft.
3. **De koppeling object → kadastrale referentie is bij ons te los.** Onze coördinaten uit
   advertenties zijn benaderend; de dichtstbijzijnde referentie is vaak de buurman of een ander
   gebouw op hetzelfde perceel. Over de 173 objecten die al een `ref_waarde` in de database hebben:

   | wijk | n | mediaan VR ÷ vraagprijs | laagste | hoogste |
   |---|---|---|---|---|
   | montgo_ermita | 43 | 1,07 | 0,30 | 6,29 |
   | moraira | 40 | 0,91 | 0,07 | 5,59 |
   | benitachell | 18 | 0,55 | 0,25 | 1,47 |
   | granadella_balcon | 18 | 0,63 | 0,24 | 3,20 |
   | rafalet_pinosol | 16 | 1,30 | 0,35 | 5,81 |
   | centro | 16 | 0,47 | 0,23 | 2,29 |
   | tosalet_adsubia | 9 | 0,67 | 0,28 | 2,06 |
   | puerto_arenal | 9 | 1,13 | 0,51 | 12,42 |
   | **alles** | **173** | **0,79** (p25 0,45 · p75 1,38) | 0,07 | 12,42 |

   Een verhouding die van 0,07 tot 12 loopt is geen prijssignaal maar ruis. (Eigen berekening
   26-09-2026, bewijstype 5.)
4. **Geen VR op onbebouwde grond.** Perceel `0481122BC5907N` is stedelijke grond zonder opstal en gaf
   niets terug. Waarom: **ONBEKEND** (de FAQ van het Catastro zegt hierover niets dat ik heb kunnen
   vinden).

**Wat de VR wél blijft doen:** hij is de fiscale ondergrens voor de overdrachtsbelasting (ITP/AJD) —
koop je onder de VR, dan betaal je belasting over de VR. Dat is een kostenpost in de doorrekening, en
daarvoor houden we hem. Niet als marktprijs.

---

## 3. Ministerio de Vivienda y Agenda Urbana (MIVAU, voorheen MITMA/Fomento)

Let op: **`www.mivau.gob.es` weigert ons** (HTTP 403, pagina "Página web bloqueada", 26-09-2026).
`cdn.mivau.gob.es` en `apps.fomento.gob.es` antwoorden wel gewoon.

### 3.1 Estadística de Transacciones Inmobiliarias (ETI) — open data

`https://cdn.mivau.gob.es/portal-web-mivau/Datos_MIVAU/CSV/VDP003_01.csv` (26-09-2026, HTTP 200,
1,04 MB). Kolommen: `CODCOMUNIDAD;COMUNIDAD;CODPROVINCIA;PROVINCIA;Tipo;Año;Trimestre;
Numero_Transacciones;Valor_Transacciones`. **Laagste niveau: provincie.** Bijgewerkt 30-07-2026,
kwartaalfrequentie, **licentie CC BY 4.0** (dataset `e05233601-transacciones-inmobiliarias-de-vivienda`
op datos.gob.es, opgehaald via de API, 26-09-2026). Hetzelfde geldt voor `VDP006_01.csv` (valor
tasado): ook provincie.

### 3.2 Boletín Estadístico Online — hier zit wél gemeenteniveau

`https://apps.fomento.gob.es/BoletinOnline2/?nivel=2&orden=34000000` en `...&orden=35000000`
(26-09-2026, HTTP 200). De bestanden zijn oude `.XLS` (BIFF8); uitgelezen met een eigen lezer op
alleen de standaardbibliotheek.

| Tabel | Niveau | Bevat |
|---|---|---|
| 2.1 `sedal/34010220.XLS` | **gemeente** (alle gemeenten, ook kleine) | **aantallen**, geen waarde |
| 3.1–3.4 `sedal/340201*.XLS` | CCAA + provincie | waarde en gemiddelde waarde |
| 4 `sedal/35103500.XLS` | **gemeente > 25.000 inwoners** | **valor tasado in €/m²** |

**Werkelijk opgehaalde cijfers:**

- Tabel 2.1, *transacciones de vivienda libre por municipios*: **Jávea/Xàbia 2026T1 = 276**
  (voorlopig). Voorafgaande kwartalen: 2025T4 286 · 2025T3 290 · 2025T2 243 · 2025T1 251.
  El Poble Nou de Benitatxell 2026T1 = 57. Teulada 2026T1 = 123.
- Tabel 3.3, *valor medio de las transacciones de vivienda libre*: **Alicante/Alacant 2026T1 =
  210.822,8 €** per woning (2025T4 195.790,4 €). Landelijk 2026T1 221.746,2 €. Dit is een
  gemiddelde **totaalprijs**, geen prijs per m², en alleen per provincie.
- Tabel 4, *valor tasado medio de vivienda libre*: **Jávea/Xàbia 2026T2 = 3.507,2 €/m²** (tot vijf
  jaar oud 3.942,0 · ouder dan vijf jaar 3.489,4), op **170 taxaties** (21 nieuw, 149 bestaand).
  Ter vergelijking Dénia 2026T2: 2.984,9 €/m². Benitatxell en Teulada staan er niet in (te weinig
  inwoners).

**Waarschuwing bij tabel 4:** *valor tasado* is een **taxatiewaarde** (ECO/805/2003-taxaties, in de
praktijk vooral hypotheekgerelateerd), geen transactieprijs. Het is een ander universum dan de
verkopen uit tabel 2.1 en niet een gemiddelde van betaalde prijzen. Wel: het is officieel, per
gemeente, per kwartaal, per m², en het volgt de markt. Bewijstype 2.

**Vertraging:** 2026T2 beschikbaar op 26-09-2026 → ongeveer **3 maanden**. Tabel 2.1 loopt tot 2026T1
(voorlopig) → ongeveer **6 maanden**.

**Rechten:** CC BY 4.0 voor de open-datareeksen (§3.1). Voor het Boletín Online zelf heb ik geen
aparte gebruiksvoorwaarde kunnen vinden omdat het moederdomein ons blokkeert: **[te verifiëren]**.
Praktisch: zelfde ministerie, zelfde statistiek, bronvermelding aanhouden.

---

## 4. Consejo General del Notariado — het Portal Estadístico (penotariado.com)

Dit is qua inhoud de beste bron die er bestaat, en juist daar zit het probleem.

### 4.1 Wat wij feitelijk hebben vastgesteld

`https://www.penotariado.com/` leidt naar `https://penotariado.com/inmobiliario/home` (HTTP 200,
26-09-2026). Geen `robots.txt` (HTTP 404), dus geen crawlverbod. De webapp praat met een REST-API
onder `/inmobiliario/rest/v1`. Deze onderdelen zijn openbaar en zonder sleutel bereikbaar (alle
opgehaald 26-09-2026, HTTP 200):

- `/public/masters/provinces` → 52 provincies, `03` = Alacant/Alicante.
- `/public/masters/municipalities` → **8.132 gemeenten**.
- `/public/masters/periods?lang=es` → 12 meses, 2 años, 5 años, 12 años.
- `/public/masters/location?locationCode=03082&locationType=MN` → `{"locationName":"Xàbia/Jávea"}`.
  Ook op postcode: `03730`, `03737`, `03738`, `03739` (Jávea), `03726` (Benitatxell), `03724`
  (Moraira) bestaan alle als geldige `CP`-locatie.
- Geldige niveaus volgens de foutmelding van de dienst zelf: **CP (postcode), MN (gemeente),
  PR (provincie), CA, PA**.

De statistiek zelf zit achter `/private/statistics?lang=…`. Aangeroepen met alle parameters:
**HTTP 400, `{"error":"invalid_request","error_description":"Authorization header not found"}`**.
In de JavaScript van het portaal staat dat de zoekopdracht alleen doorgaat als de gebruiker is
ingelogd, met een teller `basicNumberMonthlyQueries` en een foutcode `SST002` voor het bereiken van
de limiet.

**Ik heb géén account aangemaakt.** Accounts aanmaken doe ik niet.

### 4.2 Detailniveau, vertraging, rechten

| | |
|---|---|
| **Detailniveau** | **postcode** voor geregistreerde gebruikers; provincie voor niet-ingelogde bezoekers. Per gebied: gemiddelde prijs per m², gemiddelde oppervlakte, gemiddeld totaalbedrag, aantal transacties. |
| **Bron** | het *Índice Único Informatizado* van het notariaat — de akten zelf. Dus werkelijk betaalde prijzen. |
| **Vertraging** | maandelijkse bijwerking (volgens het portaal zelf). Exacte achterstand: **ONBEKEND**, niet te meten zonder inloggen. |
| **Limiet** | publiek profiel **0** statistiekopvragingen per maand; geregistreerd **50** per maand. Staat letterlijk in de voorwaardentabel. |
| **Rechten** | **Dit is de blokkade.** De gebruiksvoorwaarden verbieden gebruik van het portaal voor commerciële doeleinden, bepalen dat de gebruiker geen enkel recht op de gegevens verkrijgt en ze alleen in de persoonlijke sfeer mag gebruiken, en verbieden reproductie, verspreiding, omvorming en terbeschikkingstelling zonder voorafgaande uitdrukkelijke toestemming van de Consejo General del Notariado. Toestemming aanvragen kan via `soporte.penotariado@notariado.org`. Bron: <https://penotariado.com/inmobiliario/terminos-y-condiciones> en <https://penotariado.com/inmobiliario/aviso-legal>, beide opgehaald 26-09-2026, bewijstype 1. |

**Oordeel:** technisch haalbaar, juridisch nu niet. Deal Hunter is een commercieel acquisitiesysteem
en slaat gegevens op; dat is precies wat de voorwaarden uitsluiten. Niet gebruiken zonder schriftelijke
toestemming.

### 4.3 CIEN — de oude statistiekpagina's van het notariaat

`https://www.notariado.org/liferay/web/cien/estadisticas-principales/inmuebles` (HTTP 200,
26-09-2026). Hoofdstatistieken over vastgoed; **geen gemeenteniveau aangetroffen**.
Let op de robots.txt van `www.notariado.org` (26-09-2026): voor `User-agent: *` geldt `Crawl-delay: 5`
en **`Disallow: /es`** — het hele Spaanstalige deel van de site is voor ons afgesloten. De
CIEN-pagina's staan onder `/liferay/`, dus die mochten wel. De robots.txt bevat bovendien per
zoekmachine een `Content-Signal: ai-train=no, ai-input=no`.

---

## 5. Colegio de Registradores (CORPME)

`https://www.registradores.org/documents/d/guest/eri_2t_2026` — *Estadística Registral Inmobiliaria,
segundo trimestre 2026*, publicatie nr. 89, **augustus 2026**. Opgehaald 26-09-2026, HTTP 200,
`application/pdf`, 9,3 MB, 122 pagina's. Tekst uitgelezen met een eigen PDF-lezer (standaardbibliotheek).

**Werkelijk opgehaalde cijfers:**

| Reeks | Alicante/Alacant |
|---|---|
| Precio medio de vivienda, 2026T2 (kwartaalreeks) | **2.267 €/m²** (+2,4 % t.o.v. 2026T1) · nieuw 2.780 · bestaand 2.153 |
| Precio medio, jaarcijfer en jaarmutatie | **2.194 €/m²** (+11,7 %) · nieuw 2.799 (+10,7 %) · bestaand 2.054 (+12,2 %) |
| Hoofdstad Alacant/Alicante, jaarcijfer | 2.219 €/m² (+13,3 %) |
| Aantal verkopen 2026T2 | 12.298 (derde provincie van Spanje) |
| Aandeel kopers uit het buitenland | 46,43 % — het hoogste van alle provincies |
| Landelijk 2026T2 | 2.487 €/m², +2,4 % kwartaal, +9,2 % jaar |

- **Detailniveau:** CCAA, provincie en provinciehoofdsteden. **Geen gemeente.**
- **Vertraging:** kwartaal T2 gepubliceerd in augustus → ongeveer **2 maanden**. Snelste van alle
  bronnen hier.
- **Rechten:** het aviso legal van CORPME geeft de gebruiker een gebruiksrecht **binnen de
  huiselijke sfeer** en verbiedt wijzigen, kopiëren en reproduceren zonder uitdrukkelijke
  schriftelijke toestemming (<https://www.registradores.org/aviso-legal>, 26-09-2026, bewijstype 1).
  Overnemen van losse kerncijfers met bronvermelding in een intern stuk is gangbaar; een reeks
  overnemen in ons systeem: **eerst toestemming vragen**.
- `opendata.registradores.org` weigert onze verzoeken ("Request Rejected", WAF, 26-09-2026); die weg
  is dus niet geautomatiseerd begaanbaar.

---

## 6. INE

### 6.1 Índice de Precios de Vivienda (IPV)

API: `https://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/80270?nult=1&det=2` (26-09-2026, HTTP 200).
Tabel 80270 = *Índices por CCAA*. **Er bestaat geen provincie- of gemeenteniveau**: de zes IPV-tabellen
in de API zijn alle nationaal of per autonome regio.

**Comunitat Valenciana, 2026T2 (definitief):** index **111,696** (basisjaar ONBEKEND) ·
**+3,4 % t.o.v. het vorige kwartaal** · **+13,0 % op jaarbasis** · +6,9 % sinds jaarbegin.
Publicatiedatum volgens de API-metadata: **07-09-2026** → vertraging ongeveer **2 maanden**.

Dit is een index van herhaalde verkopen op basis van notariële gegevens; hij geeft geen niveau in
euro's, maar wél de beweging. Precies wat wij nodig hebben om de comparables van 15-09-2026 later bij
te werken.

### 6.2 Estadística de Transmisión de Derechos de la Propiedad (ETDP)

`https://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/49280?nult=1&det=2` (26-09-2026, HTTP 200).
Alleen **aantallen**, tot provincieniveau. Alicante/Alacant 2025: **53.669** woningverkopen, waarvan
vrije sector 51.331, nieuwbouw 10.353, bestaande bouw 43.316. Geen prijzen.

**Rechten INE:** de pagina met gebruiksvoorwaarden gaf ons geen leesbare inhoud; **[te verifiëren]**.

---

## 7. De "estadística de transmisiones" van het Catastro zelf

**Die bestaat niet als prijsstatistiek.** Wat het Catastro publiceert onder *Estadísticas catastrales*
(<https://www.catastro.hacienda.gob.es/es-ES/estadisticas.html>, 26-09-2026) is de stand van het
register: aantallen eenheden, gebruiksklassen, bouwjaren, kadastrale categorieën, onbebouwde
percelen, IBI. Kwartaalbestand opgehaald:
`https://www.catastro.hacienda.gob.es/documentos/estadisticas/trimestralesurbana/Urbana_T02_2026.csv`
(HTTP 200, 1,28 MB).

**Jávea/Xàbia (INE 03082), 2026T2:** 41.424 stedelijke eenheden · 26.969 met gebruik *residencial* ·
**3.960 percelen zonder bebouwing** met samen 7.474.104 m² (gemiddeld 1.887 m²) · totale stedelijke
oppervlakte 23.727.600 m² · **31 % braakliggend** · ponencia de valores uit **1994**. Geen enkel
prijsveld.

Wat er wél is aan prijsinformatie van het Catastro, is de *mapa de valores* uit §1 — en die is
inhoudelijk precies de transactiestatistiek die hier gezocht werd, alleen anders genoemd.

---

## 8. Vergelijking en oordeel

| Bron | Laagste niveau | Werkelijke prijs? | Vertraging | Rechten | Bruikbaar voor ons |
|---|---|---|---|---|---|
| **Catastro mapa de valores** | **zone binnen gemeente** (Jávea 39) | **ja**, gemiddelde van notariële koopakten | jaarlijks, laatst 25-09-2026 | reproductie met bronvermelding | **JA — direct inbouwen** |
| MIVAU tabel 4 (valor tasado) | gemeente > 25.000 inw. (Jávea wel, Benitatxell/Teulada niet) | nee, taxatiewaarde | ~3 mnd | CC BY 4.0 / [te verifiëren] | ja, als tweede ijkpunt |
| MIVAU tabel 2.1 | gemeente (alle) | alleen aantallen | ~6 mnd | CC BY 4.0 | ja, voor marktdrukte |
| MIVAU tabel 3.3 / ETI-CSV | provincie | ja, gemiddelde totaalprijs | ~3 mnd | CC BY 4.0 | beperkt |
| Registradores ERI | provincie + hoofdstad | ja, €/m² uit registratie | ~2 mnd | huiselijk gebruik; toestemming nodig | alleen als trend, met toestemming |
| Notariado penotariado.com | **postcode** | **ja**, uit de akten | maandelijks | **commercieel gebruik verboden** | **nee, tenzij Jan toestemming krijgt** |
| Notariado CIEN | provincie | ja | ONBEKEND | zie hierboven | beperkt |
| INE IPV | autonome regio | index, geen niveau | ~2 mnd | [te verifiëren] | ja, als tijdindex |
| INE ETDP | provincie | alleen aantallen | jaar/kwartaal | [te verifiëren] | beperkt |
| Catastro estadísticas | gemeente | nee | kwartaal | bronvermelding | nee (wel voorraadcijfers) |
| Goolzoom valor de referencia | per eenheid | afgeleid, fiscaal | jaarlijks | betaalde sleutel | alleen voor de ITP-berekening |

### 8.1 Hoe de Catastro-zonemodule zich verhoudt tot onze vraagprijzen

Elke actieve advertentie met coördinaat en wijk is in de opgehaalde zones geplaatst; daarna is per wijk
de mediaan van de zonemodule genomen, **alleen voor zones waarvan het representatieve product een
vrijstaande/geschakelde woning is**, en vergeleken met `villa_renovated.median` uit
`kader/comparables.json` (Idealista-vraagprijzen, 15-09-2026). Eigen berekening 26-09-2026,
bewijstype 5.

| Wijk | n objecten | module mediaan €/m² | module p25–p75 | vraagprijs mediaan €/m² | module ÷ vraagprijs |
|---|---|---|---|---|---|
| centro | 7 | 3.300 | 3.300–3.300 | 3.531 | **0,93** |
| montgo_ermita | 85 | 3.300 | 3.200–3.300 | 4.364 | **0,76** |
| moraira | 52 | 3.400 | 3.400–3.900 | 4.641 | **0,73** |
| puerto_arenal | 18 | 4.550 | 3.300–5.000 | 6.253 | **0,73** |
| tosalet_adsubia | 15 | 3.200 | 3.200–3.200 | 4.782 | **0,67** |
| rafalet_pinosol | 29 | 3.200 | 3.200–3.600 | 4.807 | **0,67** |
| benitachell | 1 | 3.000 | — | 4.614 | 0,65 |
| granadella_balcon | 51 | 3.200 | 3.200–3.600 | 6.081 | **0,53** |

Voor appartementen (zones met *vivienda colectiva* als representatief product) liggen de modules
duidelijk lager: centro 1.610 · moraira 2.680 · tosalet_adsubia 2.850 · puerto_arenal 3.280 €/m².

**Hoe dit te lezen.** Het verschil is géén zuivere "korting van vraagprijs naar transactieprijs". Er
zitten drie dingen in tegelijk: (a) vraagprijs boven verkoopprijs, (b) de module hoort bij een
gemiddelde 40–50 jaar oude woning van 140–180 m² terwijl onze comparables gerenoveerde villa's zijn,
en (c) een tijdverschil — de module komt uit oudere transacties, maar hoeveel ouder staat niet in het
antwoord (**ONBEKEND**, zie §1.5). Hoe die drie zich onderling verhouden, is met één jaargang niet te
scheiden. Dat de laagste verhouding (0,53) juist in Granadella/Balcón al Mar valt — de wijk met de
hoogste en meest gespreide vraagprijzen — past bij verklaring (b): daar staan de uitzonderlijke
objecten, niet het gemiddelde.

**Wat dit wél laat zien:** in geen enkele wijk ligt het gemiddelde werkelijk betaalde peil voor een
gewone woning bóven onze vraagprijsmediaan. Het risico in onze rekensom zit dus niet aan de kant van
een te laag ingeschatte verkoopwaarde, maar aan de kant van een te hoge. Dat is in ons kader (20 %
marge op de verkoopwaarde) precies het gevaarlijke uiteinde.

### 8.2 Oordeel

**Bruikbaar naast onze vraagprijzen: ja, en het is de belangrijkste aanvulling die wij deze ronde
konden vinden.** Niet als vervanging: de module is één gemiddelde per zone voor één standaardwoning,
terwijl onze rekensom per object een verkoopwaarde ná renovatie nodig heeft. Wel als **bovengrens-toets
en als tweede opinie** op `sale_band`.

---

## 9. Hoe wij het koppelen — concreet voorstel

1. **Nieuwe module `dh/zonewaarde.py`.** Eén aanroep per gemeente per jaar op
   `SECDameGeoJSON.aspx`, met een vaste coördinaat binnen die gemeente. Bewaren in een nieuwe tabel
   `value_zones` (gemeente, zona_valor, cod_zona, ejercicio, tipologia, superficie, superficie_suelo,
   categoria, antiguedad, conservacion, val_tipo, val_tipo_m2, geojson, fetched_at). Verversen: één
   keer per jaar, na eind september. Zelfde patroon als `dh/catastro.py`.
2. **Object → zone.** Punt-in-polygoon op de advertentiecoördinaat, en **kies bij overlap de zone
   waarvan de typologie bij het object past** (villa → *unifamiliar aislada/pareada*; appartement →
   *colectiva*; rijtjeshuis → *en hilera*). Zonder typologie: niet koppelen, liever niets dan het
   verkeerde peil.
3. **In het dossier tonen** naast de wijkprijs: "Kadaster, zone U20 (ATH 127): gemiddelde werkelijke
   prijs van een gerenoveerde woning van 160 m² op 1.000 m² = 547.400 €, oftewel 3.200 €/m²
   (mapa de valores 2027, Dirección General del Catastro)." Met de drie eigenschappen van het
   representatieve product erbij, anders is het cijfer misleidend.
4. **Een waarschuwing in `dh/feasibility.py`.** Als onze basis-verkoopwaarde per m² meer dan
   **tweemaal** de zonemodule is, een vlag zetten: "verkoopwaarde ligt ver boven het gemiddelde
   werkelijk betaalde peil in deze zone — controleer de comparables". Drempel 2,0 volgt uit de
   gemeten spreiding (0,53–0,93 op vraagprijzen, dus vraagprijs ÷ module ligt nu tussen 1,08 en 1,89);
   alles boven 2,0 valt buiten wat wij vandaag zien. Bewijstype 5, aan te scherpen zodra er een
   tweede jaargang is.
5. **Tijdindex.** `kader/comparables.json` staat vast op 15-09-2026. Vanaf nu bij elke ronde de
   INE-IPV voor Comunitat Valenciana meenemen (`DATOS_TABLA/80270`) en in het rapport melden hoeveel
   de markt sinds de peildatum is bewogen. Comparables pas herijken als de index meer dan ~5 % is
   opgelopen — bij +13 % per jaar is dat ongeveer elk halfjaar.
6. **Gemeentelijke ijkpunten opslaan** (klein, kwartaallijks, CC BY 4.0): MIVAU tabel 4 valor tasado
   Jávea, MIVAU tabel 2.1 aantallen voor de drie gemeenten, Registradores €/m² Alicante. Drie
   getallen per kwartaal; genoeg om te zien of onze aannames meelopen met de markt.
7. **Bronnenregister bijwerken:** vier nieuwe regels (Catastro mapa de valores, MIVAU Boletín,
   Registradores ERI, INE IPV) plus één regel penotariado.com met status **NIET TOEGESTAAN — wacht op
   toestemming**. Nog niet gedaan; hoort bij de uitvoering.

---

## ⏸️ ACTIE VOOR JAN

1. **Toestemming vragen aan het notariaat.** Eén e-mail naar `soporte.penotariado@notariado.org`
   met de vraag of TREE de gegevens van het Portal Estadístico del Notariado zakelijk mag gebruiken
   en opslaan (postcodeniveau, maandelijks). Dat is de enige bron met échte transactieprijzen tot op
   postcode. Zonder schriftelijk antwoord gebruiken wij hem niet. Ik kan het concept schrijven; het
   gaat pas weg na jouw "ja".
2. **Toestemming vragen aan het Colegio de Registradores** voor het overnemen van de provinciale
   €/m²-reeks in ons systeem — of besluiten dat wij die reeks alleen met de hand in rapporten
   noemen, met bronvermelding. Dat laatste kan zonder brief.
3. **Besluit:** mag ik de Catastro-zonemodule inbouwen zoals in §9 beschreven? Dat raakt de
   dossierweergave en zet een nieuwe waarschuwing op de haalbaarheidsberekening.

---

## Bijlage — alles wat werkelijk is aangeroepen (26-09-2026)

Alle verzoeken met `User-Agent: TREE-DealHunter/0.1`, hoogstens 1 per 2 s per host, robots.txt vooraf
gecontroleerd voor zowel onze eigen naam als `ClaudeBot`.

| # | Verzoek | Uitkomst |
|---|---|---|
| 1 | `robots.txt` van api.goolzoom.com, www.mitma.gob.es, apps.fomento.gob.es, www.registradores.org, www.notariado.org, www.ine.es, www.catastro.hacienda.gob.es, www.sedecatastro.gob.es, www.mivau.gob.es, cdn.mivau.gob.es, datos.gob.es, penotariado.com, opendata.registradores.org, ovc.catastro.meh.es | notariado.org verbiedt `/es`; de rest geen beletsel (404/403/geen bestand) |
| 2 | Goolzoom `cadastre/cadastralparcel/{rc14}/cadastralreferences` en `.../referencevalue` op 3 percelen | 1 leeg, 2 bedragen (§2) |
| 3 | `datos.gob.es/apidata/catalog/dataset/...` (2×) | dataset + CC BY 4.0 |
| 4 | `cdn.mivau.gob.es/.../VDP003_01.csv`, `VDP006_01.csv` | provincieniveau |
| 5 | `apps.fomento.gob.es/BoletinOnline2/` index + `sedal/34010220.XLS`, `34020150.XLS`, `35103500.XLS` | §3.2 |
| 6 | `www.registradores.org/documents/d/guest/eri_2t_2026` (PDF 9,3 MB) | §5 |
| 7 | `www.registradores.org/aviso-legal` | huiselijk gebruik |
| 8 | `opendata.registradores.org/...` | "Request Rejected" |
| 9 | `www.notariado.org/liferay/web/cien/estadisticas-principales/inmuebles` | CIEN, provinciaal |
| 10 | `penotariado.com`: home, buscador, 45 JS-bestanden, `/public/masters/{provinces,municipalities,periods,location}`, `/private/statistics`, voorwaarden en aviso legal | §4 |
| 11 | INE `wstempus`: `OPERACIONES_DISPONIBLES`, `TABLAS_OPERACION/{IPV,ETDP}`, `DATOS_TABLA/{80270,49280}`, `GRUPOS_TABLA/80270` | §6 |
| 12 | `www.catastro.hacienda.gob.es`: `/`, `es-ES/estadisticas.html`, `estadisticas_2.html`, `estadisticas_12.html`, `avisolegal.html`, `faqs.html`, `ayuda/leyenda_mapavalores.htm`, `documentos/estadisticas/trimestralesurbana/Urbana_T02_2026.csv` | §1, §7 |
| 13 | `www1.sedecatastro.gob.es`: `/Accesos/SECAccvr.aspx`, `/Cartografia/mapa.aspx?ZV=SI…`, `/Cartografia/js/mapa.js`, `/Cartografia/SECDameGeoJSON.aspx` (5×: Jávea 2027/2026/2025, Benitatxell, Teulada) | §1 |
| 14 | `ovc.catastro.meh.es`: `PonenciasWMS.aspx` GetCapabilities + 4× GetFeatureInfo, `OVCCallejero.asmx/ConsultaMunicipio` | zone U38 bij Jaume Huguet, gemeentecodes |

Twee hulpmiddelen zijn voor dit onderzoek geschreven en in de werkmap bewaard (alleen
standaardbibliotheek, niets geïnstalleerd):

- `tools/lees_xls.py` — leest oude `.xls`-bestanden (OLE2 + BIFF8), inclusief de valkuil dat een
  tekst uit de gedeelde stringtabel over een CONTINUE-recordgrens heen loopt en dan een nieuwe
  vlaggenbyte krijgt. Zonder die correctie viel juist de regel "Jávea/Xàbia" leeg.
- `tools/lees_pdf.py` — haalt tekst uit een PDF door per pagina de lettertypen op te zoeken en hun
  `ToUnicode`-tabel te volgen. Nodig omdat `pdftoppm`/poppler hier niet staat en wij niets
  installeren.

Zonder deze twee waren de cijfers van MIVAU en het Colegio de Registradores niet te lezen geweest.

# B06 — Open en officiële databronnen die we nog missen

**Werkgebied:** Jávea/Xàbia (INE 03082), El Poble Nou de Benitatxell/Benitachell (03042),
Teulada-Moraira (03128).
**Controledatum voor alles hieronder:** 16-09-2026.
**Bewijstypes:** 1 = door aanbieder vermeld · 2 = officiële bron · 3 = zelf vastgesteld ·
4 = afleiding · 5 = berekening · 6 = professional · 7 = onbekend/tegenstrijdig.

---

## Samenvatting (8 regels)

1. De grootste vondst is het **register van toeristische woningen van de Generalitat**: een dagelijks
   ververst open bestand met **per woning een kadastrale referentie**. Xàbia 4.302, Teulada 2.085,
   Benitatxell 748 objecten. Daarmee is de vraag "mag hier toeristisch worden verhuurd?" per object
   te beantwoorden in plaats van per gemeente.
2. Voor bouwvergunningen bestaat **geen open bron per vergunning**. Wel drie bruikbare omwegen, en één
   correctie: de tablón en het transparantieportaal van Xàbia zijn wél machinaal leesbaar.
3. Drie ICV-kaartlagen die we misten leveren echte objecten: **woningen op onbebouwbare grond die
   onder de minimalisatieregeling kunnen vallen** (585 in Xàbia), **bouwkundige keuringsrapporten
   IEEV.CV** (141 gebouwen), en het **energiecertificatenregister** (12.579 certificaten).
4. Alle drie hangen aan endpoints die deels al in het register staan (R2-60/R2-61): we kenden het
   adres, maar niet deze lagen.
5. Bij het **Catastro** is één ONBEKEND uit R11 opgelost: de **mapa de valores** is vrij toegankelijk
   zonder certificaat; alleen de waarde per object vraagt om DNI/NIE.
6. **Teulada en Benitatxell stonden helemaal niet in het register.** Beide hebben een leesbare sede
   electrónica; Teulada heeft bovendien een eigen gemeentelijke kaartviewer.
7. **PLACSP** heeft een werkende ATOM-feed voor heel Spanje — bruikbaar om verkoop van
   overheidsvastgoed en bouwopdrachten te volgen. TED, Diputación de Alicante en de
   vergunningenstatistiek van het ministerie leveren voor ons gebied **geen** objecten.
8. Rechten zijn overal in orde: CC BY 4.0 of CC BY, opslaan, bewaren, analyseren en tonen mag, mits
   de bron zichtbaar wordt vermeld. Twee aandachtspunten: persoonsgegevens in de tablón, en het
   verbod op geautomatiseerd gebruik van de interactieve Catastro-diensten.

---

## 1. Toeristische verhuur per object — de sterkste vondst

### 1.1 Registre de Turisme de la Comunitat Valenciana, viviendas de uso turístico

| | |
|---|---|
| Datasetpagina | `https://dadesobertes.gva.es/dataset/tur-gestur-vt` |
| CSV | `https://dadesobertes.gva.es/dataset/758f8f8e-c5af-4622-b268-a6c591710a51/resource/b1bdc28e-9813-422a-ab7a-63c21290493d/download/lista-de-viviendas-turisticas.csv` |
| JSON | `…/resource/e1497a11-d373-4e4d-a40a-bbed1879c567/download/lista-de-viviendas-turisticas.json` |
| XML | `…/resource/806c0640-b968-4646-b406-93c5e2483c66/download/lista-de-viviendas-turisticas.xml` |
| Catalogus-API | `https://dadesobertes.gva.es/api/3/action/package_show?id=tur-gestur-vt` |

**Zelf vastgesteld (bewijstype 3, 16-09-2026):**

- HTTP 200, `Content-Length` 15.178.202 bytes, `Last-Modified` **Wed, 16 Sep 2026 08:56:14 GMT**.
  Het bestand is dus vanochtend nog ververst; de catalogus meldt frequentie "Diaria".
- 89.988 regels voor de hele Comunitat Valenciana (Alicante 59.435, Valencia 17.231,
  Castellón 13.322).
- **Ons werkgebied: XÀBIA/JÁVEA 4.302 · TEULADA 2.085 · POBLE NOU DE BENITATXELL, EL/BENITACHELL 748.**
- **4.299 van de 4.302 Xàbia-regels hebben een volledige kadastrale referentie van 20 tekens** — dus
  op woningniveau, niet op perceelniveau.
- Velden (kolomkoppen uit het bestand zelf, betekenis uit de catalogus, bewijstype 3 + 2):
  `cod_municipio`, `cod_provincia`, `cp`, `direccion`, `dormit_totales`, `estudio`, `fecha_alta`,
  `habdoble`, `habindi`, `municipio`, `nombre`, `numplazasdoble`, `numplazasindi`, `plazas_totales`,
  `provincia`, `ref_catastral`, `rural`, `signatura` (inschrijvingsnummer, bv. `CV-VUT0504884-A`),
  `superficie`, `web`.
- Voorbeeldregel Xàbia: `AV ANGEL DOMENECH, 8, Bloque:A Es:2 Pl:01 Pt:D` ·
  RC `3274928BC5937N0014RU` · `CV-VUT0504884-A` · alta 29-01-2024 · 6 plaatsen · 110,00 m².
- Inschrijvingen per jaar in Xàbia: 2018 407, 2019 540, 2020 298, 2021 277, 2022 475, 2023 671,
  2024 703, 2025 67, 2026 232. Let op de knik in 2025 — oorzaak niet onderzocht, **niet interpreteren
  zonder navraag** (bewijstype 3 voor de telling, 7 voor de verklaring).

**Licentie (bewijstype 2/3):** de CKAN-API geeft `license_id: cc-by`, `license_title: Creative
Commons Attribution`. Opslaan, historie bewaren, met AI analyseren en aan Jan tonen mag, mits de bron
wordt vermeld. Voor de ICV-diensten hieronder geldt de expliciete ICV-formulering, zie §6.

**Waar we dit voor gebruiken:**

1. **Per kandidaat controleren of er al een VT-vergunning op zit.** Koppelen op de kadastrale
   referentie die we via Catastro toch al bepalen (R11). Dat is direct geld waard: een woning mét
   inschrijving in een wijk waar het plafond al vol zit, is meer waard dan dezelfde woning zonder.
2. **Toetsen aan modificación nº 41 PGOU.** R12 noteerde een plafond van 4.584 VUT met percentages
   per wijk (aanvankelijk goedgekeurd 28-05-2026, nog [te verifiëren] in de BOP). Het register telt nu
   4.302 ingeschreven woningen in Xàbia. Die twee getallen naast elkaar leggen mag, maar **de
   definities hoeven niet gelijk te zijn** (peildatum, wel/niet uitgeschreven woningen, meergezins vs.
   eengezins). Behandelen als signaal, niet als saldo — bewijstype 4.
3. **Wijkdichtheid.** Via de kadastrale referentie zijn de objecten op de kaart te zetten en per wijk
   te tellen, wat het dashboard al aankan.

**Beperkingen en zorgvuldigheid:**

- Het bestand bevat **adressen van woningen van particulieren**. Het is een openbaar register van een
  economische activiteit en er staan geen eigenaarsnamen in (het veld `nombre` bevat meestal
  "Vivienda <nummer>-A"), maar we behandelen het als bedrijfsregister: geen eigenaarsprofielen, geen
  ongevraagde benadering, niet doorgeven buiten Deal Hunter. Dat volgt uit masterprompt-regel 4 en 6.
- "Ingeschreven" is niet hetzelfde als "legaal en actief". De inschrijving is een declaración
  responsable met een geldigheid van vijf jaar; een gemeentelijk compatibiliteitsrapport hoort
  vooraf te gaan (datasetbeschrijving, bewijstype 2). Uitschrijvingen zijn in dit bestand niet als
  historie zichtbaar — daarvoor moeten wij zelf dagelijkse momentopnames bewaren.
- Er is geen coördinaat; de koppeling loopt via de kadastrale referentie of het adres.

### 1.2 De landelijke laag: Ventanilla Única Digital de Arrendamientos (NRA)

Sinds 01-07-2025 geldt Real Decreto 1312/2024: kortdurende verhuur vereist een landelijk
huurregistratienummer (NRA/NRUA), aangevraagd via het Registro de la Propiedad, met een digitale
ventanilla bij het Ministerio de Vivienda (bewijstype 1 — meerdere beroepsbronnen, zie bronnenlijst;
de officiële tekst zelf heb ik niet ingezien).

**Ik heb geen openbare opzoekdienst per object gevonden.** Zolang dat zo is, is dit voor ons geen
databron maar een controlepunt in het dossier. Status: ONBEKEND.
**Volgende stap:** de geconsolideerde tekst van RD 1312/2024 op boe.es lezen en nagaan of het
register openbaar raadpleegbaar is. Pas daarna opnemen in het register.

---

## 2. Bouwvergunningen en nieuwbouwstart in Xàbia — eerlijk antwoord

**Er is geen open bron die vergunningen per object publiceert.** Dat is de kern. Wat er wél is:

### 2.1 Correctie: de tablón en het transparantieportaal van Xàbia zijn machinaal leesbaar

R12 en registerregels R2-42/R2-69 noteerden dat `xabia.sedelectronica.es` JavaScript/Wicket is en
niet te lezen. **Dat klopt niet met een normale browser-User-Agent** (bewijstype 3, 16-09-2026 23:53):

| URL | Resultaat |
|---|---|
| `https://xabia.sedelectronica.es/board` | HTTP 200, 40.624 bytes, **volledige tabel in de HTML**: Document · Expedient · Procediment · Categoria · Descripció · Data de publicació |
| `https://xabia.sedelectronica.es/transparency/fcfa421c-24d4-4865-8f58-3ea515cd827e/` | HTTP 200, 25.775 bytes. Rubriek **"7. Urbanismo, Obras Públicas y Medio Ambiente"**: 7.1 Planeamiento Urbanístico (**2.741 documenten**), 7.2 Planes y Programas Medioambiente (0), 7.3 Normativa Urbanística y Planes Sectoriales (30), 7.4 Obras Públicas e Infraestructuras (24) |

Let op: dit is een **andere** transparantie-GUID dan die in R12 (`9dc46a0e-…`, ordenanzas fiscales).
De urbanisme-rubriek zit op `fcfa421c-…` en is bereikbaar via `https://www.ajxabia.com/ver/7151/urbanismo.html`,
dat er met een 301 naartoe doorverwijst.

Wat de tablón wél en niet geeft: publicatieplichtige aankondigingen en edicten
(bestemmingsplanprocedures, verordeningen, openbare inzage, invorderingsedicten), **niet elke
verleende bouwvergunning**. Voor de Deal Hunter is het bruikbaar om planwijzigingen en openbare
inzages in Xàbia automatisch te volgen — precies het punt dat R12 als "handmatig, maandelijkse
controle" had staan.

**⚠️ Persoonsgegevens.** In de tablón staan belastingedicten met NIF-nummers van particulieren
(zelf gezien, bewijstype 3). Als we dit automatiseren: filteren op de urbanisme-categorieën en de
rest niet opslaan.

### 2.2 Dezelfde route bestaat voor Teulada en Benitatxell — die stonden nergens in het register

| Gemeente | Sede electrónica | Gecontroleerd |
|---|---|---|
| Teulada-Moraira | `https://teuladamoraira.sedelectronica.es/board` | HTTP 200, 38.387 bytes, "Ayuntamiento de Teulada - Tablón de anuncios", met Perfil de contratante en Portal de transparencia |
| El Poble Nou de Benitatxell | `https://benitatxell.sedelectronica.es/board` | HTTP 200, 39.654 bytes, idem |

Bewijstype 3. Beide draaien op hetzelfde platform als Xàbia, dus dezelfde aanpak werkt.
Let op: `teulada.sedelectronica.es` is **niet** het juiste adres (geeft "Sede Electrónica
Indeterminada"); het is `teuladamoraira`.

Dit is een echt gat in het register: **van de drie gemeenten in het werkgebied stond alleen Xàbia
erin.**

### 2.3 De twee andere omwegen naar nieuwbouw

1. **Catastro ATOM-gebouwenbestand, tweemaal per jaar.** R11 heeft dit al geverifieerd
   (`A.ES.SDGC.BU.03082.zip`, 13.252.024 bytes, Last-Modified 21-08-2026). Nieuwe gebouwen verschijnen
   daarin met `dateOfConstruction`. Twee opeenvolgende versies vergelijken geeft de nieuwbouw van een
   half jaar — met een vertraging van maanden. Bewijstype 4 (afleiding op een geverifieerde bron).
2. **Energiecertificaten (§4.3).** Een nieuwbouwwoning krijgt vóór eerste oplevering een CEE. Het
   register is per object opvraagbaar. Sneller dan het Catastro, maar er staat geen afgiftedatum in
   de laag die ik heb gezien — alleen `validohasta`. Bewijstype 3/4.

### 2.4 Wat níet werkt voor Xàbia: de vergunningenstatistiek van het ministerie

De reeks "Construcción de edificios — licencias municipales de obra" van MIVAU/Fomento
(`https://apps.fomento.gob.es/BoletinOnline2/?nivel=2&orden=36000000`) gaat tot **comunidad autónoma,
provincie en gemeentegrootteklasse** (vijf klassen, <1.000 tot >50.000 inwoners), in XLS. Er is geen
uitsplitsing per gemeente buiten Canarias (bewijstype 2). Jávea valt in een klasse, niet onder een
eigen naam. **Voor ons dus context, geen objecten.**
`https://www.mivau.gob.es/informacion-para-el-ciudadano/informacion-estadistica/construccion/construccion-de-edificios`
gaf een 404 (bewijstype 3).

---

## 3. Woningen op onbebouwbare grond die geregulariseerd kunnen worden

**Dit is de vondst met de meeste kans op echte objecten voor route B.**

| | |
|---|---|
| Laag | `ms:MinimizacionViviendasSNU` |
| WFS | `https://terramapas.icv.gva.es/0702_Planeamiento?service=WFS&request=GetCapabilities` |
| Viewer | `https://visor.gva.es/visor/?capas=spaicv0702_minimiz_viviendas_snu` |
| Datasetpagina | `https://dadesobertes.gva.es/dataset/inventario-de-viviendas-susceptibles-de-acogerse-a-la-minimizacion-de-impacto-territorial-en-su` |

Het register kent endpoint `0702_Planeamiento` al (R2-60), maar alleen voor Clasificación en
Zonificación. De GetCapabilities geeft **zes** lagen (bewijstype 3):
`MinimizacionViviendasSNU`, `InventarioSuSuz`, `DeclaracionInteresComunitario`,
`Planeamiento.Dotaciones`, `Planeamiento.Zonificacion`, `Planeamiento.Clasificacion`.
`ows:AccessConstraints` = **"CC BY 4.0 Generalitat"**, `ows:Fees` = "No se aplican condiciones".

**Zelf gemeten (bewijstype 3, 16-09-2026):**

- Bbox Xàbia (38,7151–38,8193 N / 0,1015–0,2351 E): `numberMatched="966"`.
- Filter `cod_ine_mun = 03082`: **`numberMatched="585"`** — 585 woningen in Xàbia.
- Velden per object: `refcat` (kadastrale referentie van het perceel, 14 tekens), `cod_ine_mun`,
  `clas_suelo` (gezien: `SNU-C`, `SNU-P`), `area_construccion_m2`, `area_total_m2` (perceel),
  `porc_ocup`, `anyos_lista` (bouwjaar; gezien 1987, 1994, 2000), `anyos_diferentes`,
  `numero_viviendas`, `tipo`, `url_parcela_catastro` (directe link naar de Sede) en
  `url_download_muni_gpkg` (GeoPackage per gemeente).

**Wat het betekent.** De dataset selecteert woningen die volgens criteria van ouderdom,
perceelgrootte en bebouwingspercentage **in aanmerking zouden kunnen komen** voor de minimalisatie
van territoriale impact uit artikel 228 e.v. TRLOTUP. Dat is precies het soort object waar TREE
waarde toevoegt: een bestaande woning op onbebouwbare grond, buiten de reguliere markt, met een
juridisch pad naar regularisatie.

**Waarschuwing die in elk dossier moet.** "Susceptible" is geen recht. De regeling vereist een
gemeentelijk plan special en een besluit; R13 §2.3 beschrijft het kader. Dit is dus een **signaal
(bewijstype 3 voor de laag, 4 voor de conclusie)**, nooit een bouwconclusie. Het blijft ook binnen
masterprompt §14–17: eerst perceel identificeren, dan pas bouwconclusies.

**Ook nieuw op hetzelfde endpoint:** `InventarioSuSuz` (inventaris stedelijk en te verstedelijken
land) en `DeclaracionInteresComunitario` (DIC — toestemmingen voor activiteiten op onbebouwbare
grond). Beide nog niet getest.

---

## 4. Gebouwstaat, energie en huur: drie registers per object

### 4.1 IEEV.CV — bouwkundige keuringsrapporten per gebouw

| | |
|---|---|
| WFS | `https://terramapas.icv.gva.es/0801_GESIEE?service=WFS&request=GetCapabilities` |
| Lagen | `ms:GESIEE.Informes` (rapporten), `GESIEE.Parcelas` (percelen met verplichting) |
| CSV/GPKG | `…/0801_GESIEE?request=GetFeature&service=WFS&version=2.0.0&typename=GESIEE.Informes&outputformat=csv` (resp. `gpkg`) |
| Grondslag | Decreto 53/2018, de 27 d'abril, del Consell (bewijstype 2, datasetbeschrijving) |

**Zelf gemeten (bewijstype 3):** bbox Xàbia `numberMatched="141"`. Velden per gebouw:
`inf_refcatastral`, `inf_numieevcv` (bv. `IEE/U/2023/03/082/0000498`), `dir_nombrevia`,
`dir_numerovia`, `anyo_construccion`, `fecha_caducidad`, `count_intu`, **`estado_intu`** (gezien:
`INTu sin ejecutar`), `count_intm`, `emisionesletra`, `consumoletra`, `num_intervenciones`,
`urlgesie`, `evaluado` (gezien: `Completo`), `noms_mun`, `comarca`.

Voorbeeld: ADOLFO SUAREZ 20, bouwjaar 1925, RC `5481015BC5958S`, 3 dringende interventies, status
"INTu sin ejecutar", emissies C / verbruik D.

**Waarvoor:**
- **Risicotoets bij aankoop van een appartement.** "Dringende interventies niet uitgevoerd" betekent
  een openstaande verplichting en vrijwel zeker een derrama. Dat hoort in de rekensom.
- **Route C (Build).** Een gebouw met niet-uitgevoerde interventies is een concrete opdracht.
- De tweede laag, `GESIEE.Parcelas`, toont percelen met woongebouwen **ouder dan 50 jaar die het
  rapport verplicht moeten laten maken**. Het verschil tussen die twee lagen — verplicht maar nog
  geen rapport — is een lijst die nergens anders bestaat.

### 4.2 Energiecertificaten per object

| | |
|---|---|
| WFS | `https://terramapas.icv.gva.es/26_GCEE?service=WFS&request=GetCapabilities`, laag `ms:CEEEdificios` |
| Datasetpagina | `https://dadesobertes.gva.es/dataset/registro-de-certificados-de-eficiencia-energetica-en-la-comunitat-valenciana` |

**Zelf gemeten (bewijstype 3):** `AccessConstraints` = "CC BY 4.0 Generalitat". Bbox Xàbia
`numberMatched="12579"`. Velden: `codigo` (bv. `E2016VS069634`), `idcertificado`,
`cer_emicalificacion` en `cer_concalificacion` (letters A–G), `cer_emitotal`, `cer_contotal`,
`exp_direccion`, `exp_cp`, `validohasta`, **`ref_referencia`** (volledige RC, 20 tekens),
`ref_parcela` (14 tekens), `url_castellano` (publieke etiketpagina op `sgcee.aven.es`),
`cod_ine_mun`, `naturaleza` (urbana/rústica), `n_certificados`.

**Waarvoor:** het energielabel per object invullen — de BP-feed heeft `energy_rating` maar deels als
vrije tekst (R05). Verder zijn G-gelabelde objecten renovatiekandidaten, en een vers certificaat
gaat vaak vooraf aan verkoop of volgt op een renovatie. **Beperking:** ik zag geen afgiftedatum,
alleen `validohasta`; afgiftedatum ≈ `validohasta` min tien jaar is een afleiding (bewijstype 4/5)
die eerst getoetst moet worden.

### 4.3 Huurborgsommen — huurprijsindicatie per postcode

`https://dadesobertes.gva.es/dataset/viv-reg-fia-2026` (en één dataset per jaar terug tot 2020).
CSV/JSON/XLSX/XML, licentie cc-by. Velden: `anyo_datos`, `cod_municipio`, `cod_provincia`, `cp`,
`devuelta`, `importe_fianza`, `municipio`, `provincia` (bewijstype 2, catalogus).

Dit is het register van gestorte huurwaarborgen van de Generalitat. Per storting, met postcode en
bedrag, **maar zonder adres of object**. Bruikbaar als onafhankelijke huurprijsindicatie per postcode
naast de advertentieprijzen — geen objecten. Nog niet gedownload.

---

## 5. Catastro: één ONBEKEND uit R11 opgelost

R11 noteerde bij de valor de referencia: "Cl@ve/certificaat; wat zonder identificatie kan: ONBEKEND".
Dat is nu beantwoord (bewijstype 3, 16-09-2026):

| Dienst | URL | Resultaat |
|---|---|---|
| **Mapa de valores urbanos 2026** | `https://www1.sedecatastro.gob.es/Cartografia/mapa.aspx?ZV=SI&BUSCAR=S&ANYOZV=2026&final=IAMIU` | **HTTP 200, 124.335 bytes, geen inlogmuur** |
| Mapa de valores rústicos 2026 | `…/Cartografia/mapa.aspx?ZR=SI&anyoZV=2026&buscar=S&final=IAMIR` | niet apart getest |
| Valor de referencia per object | `https://www.sedecatastro.gob.es/Accesos/SECAccvrTC.aspx?destino=3&ejercicio=2026` | **HTTP 200 maar met authenticatieformulier**: DNI/NIE + nummer van het document + naam en achternaam |
| Ingang | `https://www1.sedecatastro.gob.es/Accesos/SECAccvr.aspx` | jaren 2022 t/m 2026, elk met mapa urbano, mapa rústico, Informe del Mercado Inmobiliario en consulta |

Letterlijk op de kaartpagina (bewijstype 2, citaat van de pagina zelf):
> "El mapa de valores refleja las conclusiones del análisis de las compraventas de viviendas
> realizadas ante Notario en los tres últimos años."

**Waarom dat belangrijk is.** Dit is een waardekaart per waardegebied die is gebouwd op **werkelijke
notariële koopsommen over drie jaar** — geen vraagprijzen. Voor de wijkprijzen in
`kader/comparables.json` is dat een onafhankelijke tweede meting naast H01. En de Informe del Mercado
Inmobiliario Urbano per jaar hoort bij dezelfde ingang (inhoud nog niet gezien, [te verifiëren]).

**Gebruiksrecht:** dit blijft een **interactieve dienst van de Sede**, en de condiciones de uso
daarvan verbieden geautomatiseerd of massaal gebruik (R11 §5). Dus **handmatig raadplegen per
dossier**, niet automatiseren. Dat is geen belemmering: het is een controle per kandidaat.

**Wat níet bruikbaar bleek:** de "Estadísticas catastrales — Catastro Inmobiliario Urbano" op
datos.gob.es (`e05250001`) noemt als periode 1990–2013, en de landingspagina
`https://www.catastro.hacienda.gob.es/esp/estadistica_1.asp` gaf een 404 (bewijstype 3). Lage
prioriteit.

---

## 6. SIGPAC — landbouwpercelen en werkelijk grondgebruik

| | |
|---|---|
| Dienstencatalogus | `https://sigpac-hubcloud.es/` |
| WMS | `https://wms.mapa.gob.es/sigpac/wms` |
| Diensten | listas de códigos, teselas vectoriales (MVT), WMS, OGC API, consulta, salidas gráficas, ATOM-download per gemeente |
| Licentie | CC BY 4.0 (link `https://creativecommons.org/licenses/by/4.0/deed.es` onderaan de cataloguspagina, bewijstype 3) |

De servicebeschrijving noemt de SIGPAC-lagen expliciet **datos de alto valor (HVD)** onder
Reglamento de Ejecución (UE) 2023/138 en de open-datarichtlijn (UE) 2019/1024 (bewijstype 2, tekst
op de pagina). HVD betekent: vrij, machineleesbaar, via API, zonder voorwaarden.

**Waarvoor:** bij rustieke percelen in Xàbia en Benitatxell zegt SIGPAC wat er feitelijk staat —
gebruikscode per recinto (olijf, matorral, improductivo), landschapselementen, helling. Dat vult
Catastro aan, dat vooral de juridische kant geeft. **SIGPAC-percelen zijn niet dezelfde geometrie
als kadastrale percelen**; niet door elkaar halen.

Niet getest per perceel in ons gebied — dat is de volgende stap.

---

## 7. Verkoop van overheidsvastgoed: PLACSP werkt, TED niet

### 7.1 PLACSP — ATOM-feed voor heel Spanje

`https://contrataciondelestado.es/sindicacion/sindicacion_643/licitacionesPerfilesContratanteCompleto3.atom`

**Geverifieerd (bewijstype 3, 16-09-2026):** geldige ATOM-feed, titel "Licitaciones publicadas en la
Plataforma de Contratación del Sector Público: licitacionesPerfilesContratanteCompleto v3",
`updated` **2026-09-16T20:23:42.303+02:00**, met paginering (`self`, `first`, `next`). Per entry:
aanbestedende dienst met DIR3 en NIF, contracttype met CPV-code, status (ADJ/RES/ANULADA), raming,
gunningsbedrag, aantal inschrijvingen.

Het register kent PLACSP alleen als het perfil del contratante van Xàbia (R2-42). Dit is dus een
**gemiste route bij een bekende partij**: de landelijke feed maakt het mogelijk om Xàbia, Teulada,
Benitatxell, de Diputación en de Generalitat automatisch te volgen op (a) enajenación van
gemeentelijk vastgoed en (b) bouw- en renovatieopdrachten (route C voor Build).

Daarnaast publiceert Hacienda zes datasets vanaf 2012:
`https://www.hacienda.gob.es/es-ES/GobiernoAbierto/Datos%20Abiertos/Paginas/licitaciones_plataforma_contratacion.aspx`
(licitaciones vanaf 2012, agregadas vanaf 2016, contratos menores vanaf 2018, encargos a medios
propios vanaf juli 2021, consultas preliminares vanaf april 2022, directorio de perfiles;
bewijstype 2).

**Twee praktische punten.** De feed is landelijk en dus groot — filteren op de DIR3/NIF van onze drie
gemeenten is noodzakelijk. En: **`curl` met de standaard macOS-certificaatbundel weigert deze host**
("self signed certificate in certificate chain", bewijstype 3) — dezelfde klasse probleem als R11
beschreef voor `www.catastro.hacienda.gob.es`. Oplossing is dezelfde: `httpx` met de certifi-bundel,
nooit `-k`.

### 7.2 TED — geen unieke objecten voor ons

TED is het aanbestedingsblad van de EU. De drempels liggen op €143.000 (AGE, diensten en leveringen)
respectievelijk €221.000 (overige bestuurslagen); onder die drempel wordt niet in het DOUE
gepubliceerd (bewijstype 1, samenvatting van marktbronnen; de drempelverordening zelf niet ingezien).
Verkoop van grond en gebouwen door een gemeente valt bovendien buiten de aanbestedingsrichtlijnen.
**Conclusie: geen dekking voor onze objecten.** Lage prioriteit, niet opnemen.

---

## 8. Statistiek en context: wat wél en niet iets toevoegt

### 8.1 INE — Censo de Población y Viviendas 2021 heeft een eigen API (gemiste route)

Registerregel R2-47 gebruikt de Tempus3-API van INE voor de IPV en de Transmisiones. Daarnaast
bestaat een **aparte API voor de censussen 2021**:
`https://www.ine.es/dyngs/DAB/index.htm?cid=1769`, basis-URL `https://www.ine.es/Censo2021/api`,
alleen POST met JSON; tabellen, variabelen en metrieken staan in bijgeleverde Excel-bestanden; twee
gelijktijdige verzoeken; licentie **CC BY-SA 4.0** (bewijstype 2, INE-pagina).

Waarvoor: woningen per gemeente en per censussectie naar type (hoofdwoning, niet-hoofdwoning, leeg)
en naar ouderdom. Dat zegt iets over waar de renovatievoorraad zit. **Context, geen objecten.**
Welke tabel precies de leegstand geeft, is nog niet uitgezocht ([te verifiëren]).

### 8.2 Diputación de Alicante open data — niets voor ons

`https://datosabiertos.diputacionalicante.es/catalogo/` — 35 datasets, gecontroleerd (bewijstype 3):
evolución presupuesto, mercados municipales, fiestas locales, revisión del padrón de habitantes,
deuda viva, presupuestos municipales, núcleos de población, banderas azules, geojson, elecciones,
entes diputación. **Geen vastgoed, geen urbanisme, geen vergunningen.** Lage prioriteit.

### 8.3 BOP Alicante — geen machineroute gevonden

`https://www.dip-alicante.es/bop2/` gaf **HTTP 403** (bewijstype 3). Ik heb geen RSS, XML-sumario of
API gevonden. Blijft handmatig, zoals R12 al vaststelde. Gezien §2.1 is de tablón van de gemeente
zelf nu het betere aanknopingspunt.

### 8.4 MIVAU — twee reeksen die we misten, allebei zonder gemeentedetail

Naast "Transacciones inmobiliarias" (R2-46) staan op hetzelfde Boletín-platform ook
**"Precio suelo urbano"** (`/el-ministerio/observatorios-y-estadisticas/estadisticas/precios-suelo-urbano`,
reeksen op `apps.fomento.gob.es/BoletinOnline2/?nivel=2&orden=36000000`) en **"Estimación del parque
de viviendas"**. Granulariteit: CCAA, provincie en gemeentegrootteklasse, XLS (bewijstype 2).
Grondprijs per m² voor de provincie Alicante is bruikbaar als plausibiliteitscontrole op onze eigen
perceelwaarden — meer niet.

### 8.5 Eurostat

Niet onderzocht. Eurostat publiceert huizenprijsindices op landniveau; voor de Marina Alta voegt dat
niets toe boven INE en MIVAU. Lage prioriteit, niet opgenomen.

### 8.6 GVA-vastgoed in eigendom

`https://dadesobertes.gva.es/dataset/hac-bie-inm` (Listado de bienes inmuebles de la Generalitat) en
`fincas-patrimoniales-de-la-generalitat`, licentie cc-by. Velden onder meer: `municipio`,
`clasificacion_suelo`, `calificacion_suelo`, `estado_inmueble`, `inscrito_registro_propiedad`,
`licencia_apertura`, `fecha_alta`, `fecha_baja`, `derecho_tercero` (bewijstype 2, catalogus).
Het register kent alleen de veilingpagina van de GVA (R2-72). Met deze lijst weten we **vóór** een
veiling wat de Generalitat in ons werkgebied bezit. Nog niet gedownload.

---

## 9. Gebruiksrechten — de bepalende zinnen

**ICV/GVA-geodiensten** (MinimizacionViviendasSNU, IEEV.CV, CEE, en de lagen die al in het register
staan). `https://icv.gva.es/es/condiciones-de-uso-de-la-geoinformacion-icv`, bewijstype 2:

> "La licencia Creative Commons que rige la información geográfica generada por el ICV (salvo que se
> indique lo contrario) es la de Atribución 4.0 Internacional (CC BY 4.0)"

Vermelding: "Producto año CC BY 4.0, Generalitat", zichtbaar geplaatst. Bij doorgifte aan derden
vraagt het ICV om uitdrukkelijke aanvaarding van dezelfde voorwaarden door de nieuwe gebruiker — dat
raakt ons niet zolang we intern werken en aan Jan tonen, maar wél als we ooit een afgeleide dataset
zouden doorgeven.

In de WFS-antwoorden zelf staat `ows:AccessConstraints` = "CC BY 4.0 Generalitat" en `ows:Fees` =
"No se aplican condiciones" (bewijstype 3, zelf gelezen in GetCapabilities van 0702 en 26_GCEE).

**dadesobertes.gva.es-datasets:** `license_id: cc-by` per dataset via de CKAN-API (bewijstype 2/3).
De algemene aviso legal-pagina van het portaal kon ik niet ophalen (§11).

**SIGPAC:** CC BY 4.0, plus HVD-status onder Reglamento (UE) 2023/138 (bewijstype 2/3).

**INE Censo 2021:** CC BY-SA 4.0 (bewijstype 2). Let op de *ShareAlike*: afgeleide datasets die we
zouden publiceren moeten dan onder dezelfde licentie. Intern gebruik en tonen aan Jan is geen
publicatie.

**Catastro Sede (mapa de valores):** vrij te raadplegen, maar de condiciones de uso van de
interactieve diensten verbieden geautomatiseerd of massaal gebruik (R11 §5). Handmatig per dossier.

**Samengevat voor alle nieuwe bronnen in §1 t/m §7:** opslaan **ja**, historie bewaren **ja**, met AI
analyseren **ja**, aan Jan tonen **ja** — telkens met bronvermelding. De enige uitzondering is de
Catastro-kaart, die niet geautomatiseerd mag.

---

## 10. Wat ik zou aansluiten, in volgorde

1. **VT-register** (§1.1). Dagelijkse momentopname, ontdubbelen op `signatura`, koppelen op
   kadastrale referentie. Levert direct een kolom "toeristische vergunning: ja/nee/sinds" in het
   dossier. Weinig werk, groot effect.
2. **MinimizacionViviendasSNU** (§3). 585 objecten in Xàbia met een kadastrale referentie. Filteren
   op perceelgrootte en bouwjaar, dan door de bestaande haalbaarheidsrekenaar. Elk object krijgt de
   waarschuwing "susceptible ≠ recht".
3. **Tablón van de drie gemeenten** (§2.1, §2.2). Eén keer per dag ophalen met een normale
   User-Agent, filteren op urbanisme-categorieën, geen persoonsgegevens opslaan.
4. **CEE-register** (§4.2). Energielabel per kandidaat automatisch invullen.
5. **IEEV.CV** (§4.1). Alleen als risicotoets bij appartementen en als bron voor Build-opdrachten.
6. **PLACSP-feed** (§7.1). Filteren op de DIR3/NIF van de drie gemeenten; met `httpx`, niet `curl`.
7. **Mapa de valores** (§5). Handmatig, per kandidaat, als tweede meting naast H01.

---

## 11. Geblokkeerd of mislukt

| Wat | Wat er gebeurde |
|---|---|
| `https://www.dip-alicante.es/bop2/` (BOP Alicante) | HTTP 403. Geen RSS/XML/API gevonden. |
| `https://geoportal.registradores.org/` | Pagina levert alleen het woord "Geoportal"; JavaScript-applicatie. De vraag uit R11 ("nota simple por geolocalización", "alertas geográficas") blijft onbeantwoord. |
| `https://contrataciondelestado.es/…` met `curl` | "self signed certificate in certificate chain". Werkt wel via een client met de certifi-bundel. |
| `https://www.mivau.gob.es/…/construccion-de-edificios` | HTTP 404 (ook met browser-User-Agent). Omgeleid naar de Boletín-reeksen. |
| `https://www.catastro.hacienda.gob.es/esp/estadistica_1.asp` | HTTP 404. |
| `https://www.sedecatastro.gob.es/Accesos/SECAccMapaValores.aspx` | HTTP 404 — bestaat niet; de juiste ingang is `SECAccvr.aspx`. |
| `https://dadesobertes.gva.es/es/pages/aviso-legal` en de portaalhomepage | 404 respectievelijk een lege respons van 77 bytes. Licentie wel per dataset via de API vastgesteld. |
| `geoportal.teuladamoraira.org` | Viewer werkt (HTTP 200), maar twee sondes naar `/geoserver/wms` en `/catalogo` gaven 404. Geen open OGC-eindpunt gevonden. |
| `teulada.sedelectronica.es` | Verkeerde host: "Sede Electrònica Indeterminada". Juiste host is `teuladamoraira.sedelectronica.es`. |
| Ventanilla Única Digital / NRA | Geen openbare opzoekdienst per object gevonden. Status ONBEKEND. |
| GVA-WFS met `PropertyIsEqualTo`-filter | Gaf een foutantwoord; met `PropertyIsLike` (de syntaxis die de laag zelf in `url_download_muni_gpkg` gebruikt) werkt het wel. |

---

## 12. Bronnenlijst (URL · controledatum · bewijstype)

1. `https://dadesobertes.gva.es/dataset/tur-gestur-vt` · 16-09-2026 · 2
2. `https://dadesobertes.gva.es/api/3/action/package_show?id=tur-gestur-vt` · 16-09-2026 · 3
3. CSV viviendas turísticas (HEAD + download, 15.178.202 bytes) · 16-09-2026 · 3
4. `https://cindi.gva.es/es/web/turisme/habitatges-dus-turistic` · 16-09-2026 · 2
5. `https://cindi.gva.es/es/web/turisme/llistat-oficial-empreses-turistiques` · 16-09-2026 · 1 (niet zelf geopend)
6. `https://terramapas.icv.gva.es/0702_Planeamiento?service=WFS&request=GetCapabilities` · 16-09-2026 · 3
7. WFS GetFeature `MinimizacionViviendasSNU`, bbox Xàbia en filter `cod_ine_mun=03082` · 16-09-2026 · 3
8. `https://dadesobertes.gva.es/dataset/inventario-de-viviendas-susceptibles-de-acogerse-a-la-minimizacion-de-impacto-territorial-en-su` · 16-09-2026 · 2
9. `https://terramapas.icv.gva.es/0801_GESIEE?…` (GESIEE.Informes, bbox Xàbia) · 16-09-2026 · 3
10. `https://dadesobertes.gva.es/dataset/ieev-cv-informes-de-evaluacion-del-edificio-de-viviendas-en-la-comunitat-valenciana` · 16-09-2026 · 2
11. `https://dadesobertes.gva.es/dataset/ieev-cv-edificaciones-con-mas-de-50-anos-de-antiguedad-y-uso-residencial6` · 16-09-2026 · 2
12. `https://terramapas.icv.gva.es/26_GCEE?…` (CEEEdificios, bbox Xàbia) · 16-09-2026 · 3
13. `https://dadesobertes.gva.es/dataset/registro-de-certificados-de-eficiencia-energetica-en-la-comunitat-valenciana` · 16-09-2026 · 2
14. `https://dadesobertes.gva.es/dataset/viv-reg-fia-2026` · 16-09-2026 · 2
15. `https://dadesobertes.gva.es/dataset/hac-bie-inm` · 16-09-2026 · 2
16. `https://icv.gva.es/es/condiciones-de-uso-de-la-geoinformacion-icv` · 16-09-2026 · 2
17. `https://sigpac-hubcloud.es/` en `https://sigpac-hubcloud.es/html/ssgs/descServicio.html` · 16-09-2026 · 3
18. `https://www.fega.gob.es/es/pepac-2023-2027/sistemas-gestion-y-control/sigpac/wms-de-sigpac` · 16-09-2026 · 1 (via zoekresultaat, niet zelf geopend)
19. `https://www1.sedecatastro.gob.es/Accesos/SECAccvr.aspx` · 16-09-2026 · 3
20. `https://www1.sedecatastro.gob.es/Cartografia/mapa.aspx?ZV=SI&BUSCAR=S&ANYOZV=2026&final=IAMIU` · 16-09-2026 · 3 (citaat: 2)
21. `https://www.sedecatastro.gob.es/Accesos/SECAccvrTC.aspx?destino=3&ejercicio=2026` · 16-09-2026 · 3
22. `https://datos.gob.es/es/catalogo/e05250001-estadisticas-catastrales-catastro-inmobiliario-urbano` · 16-09-2026 · 2
23. `https://xabia.sedelectronica.es/board` · 16-09-2026 · 3
24. `https://xabia.sedelectronica.es/transparency/fcfa421c-24d4-4865-8f58-3ea515cd827e/` · 16-09-2026 · 3
25. `https://www.ajxabia.com/ver/7151/urbanismo.html` (301 naar 24) · 16-09-2026 · 3
26. `https://www.ajxabia.com/ver/7175/urbanismo-hace-publica-la-nueva-cartografia-municipal-de-xabia-en-la-web-del-ayuntamiento.html` (CartoXàbia) · 16-09-2026 · 1
27. `https://teuladamoraira.sedelectronica.es/board` · 16-09-2026 · 3
28. `https://benitatxell.sedelectronica.es/board` · 16-09-2026 · 3
29. `https://geoportal.teuladamoraira.org/` · 16-09-2026 · 3
30. `https://contrataciondelestado.es/sindicacion/sindicacion_643/licitacionesPerfilesContratanteCompleto3.atom` · 16-09-2026 · 3
31. `https://www.hacienda.gob.es/es-ES/GobiernoAbierto/Datos%20Abiertos/Paginas/licitaciones_plataforma_contratacion.aspx` · 16-09-2026 · 2
32. `https://contrataciondelestado.es/wps/portal/plataforma/datos_abiertos/` · 16-09-2026 · 2
33. `https://ted.europa.eu/es/simap/european-public-procurement` · 16-09-2026 · 1 (via zoekresultaat)
34. `https://www.ine.es/dyngs/DAB/index.htm?cid=1769` (API Censo 2021) · 16-09-2026 · 2
35. `https://datosabiertos.diputacionalicante.es/catalogo/` · 16-09-2026 · 3
36. `https://www.dip-alicante.es/bop2/` · 16-09-2026 · 3 (403)
37. `https://www.mivau.gob.es/el-ministerio/observatorios-y-estadisticas/estadisticas/precios-suelo-urbano` · 16-09-2026 · 3
38. `https://apps.fomento.gob.es/BoletinOnline2/?nivel=2&orden=36000000` · 16-09-2026 · 2
39. `https://datos.gob.es/apidata/catalog/dataset/title/licitaciones` (datos.gob.es API, ontdekkingsroute) · 16-09-2026 · 3
40. `https://geoportal.registradores.org/` · 16-09-2026 · 3 (leeg)

**Intern (eerder vastgesteld):**
41. R11 — Catastro en Registro · `/Users/root-admin/tree-es/deal-hunter/onderzoek/R11-catastro-registro-perceelidentificatie.md` · 15-09-2026 · 3
42. R12 — Urbanisme Xàbia (mod. nº 41 VUT, transparantieportaal) · idem `/R12-urbanisme-xabia-plan-en-vergunning.md` · 15-09-2026 · 1/2
43. R13 — Geoportalen en sectorale lagen (ICV-endpoints, minimización-kader) · idem `/R13-regionaal-sectoraal-geoportalen.md` · 15-09-2026 · 2/3
44. `bronnenregister.json`, 75 regels · 16-09-2026 · 3

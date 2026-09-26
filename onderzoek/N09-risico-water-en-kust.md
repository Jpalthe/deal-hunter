# N09 — Overstromingszone en Kustwet per perceel: welke dienst antwoordt werkelijk

Onderzoek voor TREE Deal Hunter · opgesteld en getoetst **26-09-2026** · werkgebied Jávea/Xàbia
(provincie Alicante) · alle HTTP-toetsen op die datum zelf uitgevoerd, 222 verzoeken tussen 20:31 en
20:58, ten hoogste 1 verzoek per 2 seconden per host

**Bewijstypen (masterprompt §5):** 1 door aanbieder vermeld · 2 officiële bron · 3 door ons
vastgesteld · 4 AI-gevolgtrekking · 5 berekening · 6 professional · 7 onbekend of tegenstrijdig.

**Niet bezocht:** `mediambient.gva.es` — de robots.txt daarvan verbiedt ClaudeBot en Claude-User
uitdrukkelijk. Geen enkel verzoek naar die host gedaan.

---

## Conclusie

1. **Ja, dit kan volledig automatisch, per perceel, gratis en met toestemming.** Eén partij levert
   alles: de GeoServer van MITECO op `gis.miteco.gob.es`, werkruimte `agua` (overstroming) en
   werkruimte `costas` (Kustwet). Beide dienstbeschrijvingen zeggen vandaag zelf
   `Fees: CC BY 4.0. Nombrar a la fuente: Ministerio para la Transición Ecológica y el Reto
   Demográfico` en `AccessConstraints: Sin limitaciones al acceso público` (bewijstype 1, §2.2).
   Geen sleutel, geen aanmelding, geen kosten.
2. **Het is WFS, niet alleen WMS.** Dat is de belangrijkste winst tegenover N03 (18-09): je kunt met
   `INTERSECTS` de héle perceelgrens tegen de zone houden in plaats van één prikpunt, en je krijgt de
   kenmerken terug (zonenummer, rivier, studie, goedkeuringsdatum, debiet). Getoetst en werkend.
3. **De TLS-blokkade uit N03 bestaat niet meer.** N03 schreef dat `gis.miteco.gob.es` vanaf deze Mac
   onbereikbaar was en dat de koppeling in Node moest. Dat gold voor de systeem-curl (LibreSSL) en
   Python 3.9. De Hermes-venv draait **Python 3.11.15 met OpenSSL 3.5.5** en haalt alles moeiteloos
   op: 176 geslaagde verzoeken op die host vandaag. **De koppeling kan gewoon in Python.**
4. **De drie proefpercelen liggen geen van drieën in een overstromingszone en geen van drieën onder
   de Kustwet.** Niet "niets gevonden", maar gemeten: zie de tabel in §3. Twee onafhankelijke
   methoden (WFS `INTERSECTS` en WMS `GetFeatureInfo`) geven hetzelfde antwoord, en beide methoden
   zijn op een perceel dat er wél in ligt positief getest (§3.3).
5. **Een valstrik die ons vandaag zelf te pakken had:** het coördinatenstelsel verschilt **per laag
   binnen dezelfde GeoServer**. De overstromingslagen staan in EPSG:4258 (graden, breedte eerst), de
   twee belangrijkste kustlagen in EPSG:25830 (meters). Met de verkeerde volgorde krijg je geen
   foutmelding maar een leeg antwoord — mijn eerste kustronde gaf daardoor ten onrechte "geen
   deslinde binnen 3 km" voor een perceel dat er 820 m vandaan ligt. Zie §4.1. Dit móet in de code
   per laag vastliggen, met een vaste ijkcoördinaat per laag.
6. **De vondst met de meeste waarde voor Jan zit niet in de drie proefpercelen maar in de rest van
   de database.** Toen ik de kustlijnen van heel Jávea één keer ophaalde en lokaal doorrekende over
   alle 622 percelen met een grens: **25 percelen liggen binnen 20 m van de goedgekeurde
   DPMT-grens** en **46 binnen 100 m** — dat zijn de percelen waar de servidumbre de protección
   speelt en waar bouwen zonder toestemming van Costas niet kan. Daarnaast heeft **36 percelen**
   minstens één hoekpunt in de overstromingszone T500 van de Gorgos. Zie §3.4.
7. **Voorstel (§5):** één nieuwe module `dh/water_kust.py` plus `dh/enrich_water_kust.py`, net als
   `hoogte.py` / `enrich_helling.py`. Twee werkwijzen naast elkaar: **per perceel bevragen** (7 WFS-
   verzoeken) voor nieuwe objecten, en **één keer per maand het hele gebied ophalen en lokaal
   doorrekenen** (7 verzoeken voor álle percelen samen, ~5 MB) voor de bulk. De `clip`-parameter van
   GeoServer maakt dat tweede mogelijk en is vandaag getest.
8. **Wat dit níet is:** geen juridisch oordeel. De kaartlijn is de bestuurlijke weergave; het
   deslinde-dossier en het *certificado de Costas* zijn de rechtsbron. De uitkomst hier is een
   **zeef en een waarschuwing**, geen vrijwaring. Voor elk perceel dat door de zeef komt als "raakt
   of dichtbij" hoort een handmatige controle.

---

## 1. De vraag en de methode

De vraag: kunnen wij per kadastraal perceel in Jávea automatisch vaststellen of het (a) in een
overstromingszone ligt en (b) onder de Kustwet valt?

De methode: geen enkele bewering op gezag van documentatie. Elke dienst is echt aangeroepen, op
échte percelen uit `data/dealhunter.sqlite`, en wat hier staat is het antwoord dat terugkwam.
Alle verzoeken zijn gelogd (tijdstip, URL, status, aantal bytes, duur).

**De drie proefpercelen** (uit tabel `parcels`, grens uit de INSPIRE-kadasterdienst, EPSG:4326):

| Kadastrale referentie | Adres volgens kadaster | Gebruik | Perceel | Zwaartepunt (lon, lat) | Zwaartepunt (EPSG:25830) |
|---|---|---|---|---|---|
| `0481122BC5907N` | CL PENYAPARDA PROLG. 3, Jávea | onbebouwde grond | 1.622 m² | 0,126229 · 38,793996 | 771.518 · 4.298.560 |
| `5246308BC5954N` | CL JAUME HUGUET 6, Jávea (Adsubia) | residencial, bouwjaar 2005 | 1.024 m² | 0,182888 · 38,764450 | 776.554 · 4.295.450 |
| `6442010BC5964S` | PD CM CAP MARTI 317, Jávea (Tosalet) | residencial, bouwjaar 1973 | 697 m² | 0,194625 · 38,760603 | 777.589 · 4.295.059 |

**Vierde perceel als ijkpunt.** Omdat "niets gevonden" het gevaarlijkste antwoord is in een
geautomatiseerde zeef, is elke methode óók getoetst op een perceel waarvan ik eerst lokaal had
vastgesteld dát het in de zone ligt: `5553425BC5955S`, AV ARENAL 6(B) — en op `5958201BC5955N`,
AV MEDITERRANEO 2(B), waar de deslindelijn dwars over het perceel loopt. Beide gaven een positief
antwoord van de dienst. Zonder die twee ijkpunten was dit rapport niets waard.

### 1.1 Toestemming: wat de robots.txt van elke host zegt

| Host | robots.txt op 26-09-2026 | Oordeel |
|---|---|---|
| `mediambient.gva.es` | verbiedt ClaudeBot en Claude-User (`Disallow: /`) | **niet benaderd** |
| `gis.miteco.gob.es` | niet op te halen: de server verbreekt de verbinding op `/robots.txt` (HTTP-niveau, niet TLS) | **ONBEKEND**; de diensten zelf verklaren `Sin limitaciones al acceso público` |
| `servicios.idee.es` | idem, verbinding verbroken | **ONBEKEND**; `www.idee.es/robots.txt` geeft `User-Agent: * / Disallow:` (alles toegestaan) en de dienst verklaart `Fees: no conditions apply` |
| `sig.mapama.gob.es` | HTTP 200 maar de inhoud is de HTML-foutpagina van mapa.gob.es — er ís geen robots.txt | niets verboden |
| `www.chj.es` en `siajucar.chj.es` | HTTP 404 | niets verboden |
| `www.cartociudad.es` | HTTP 200 maar HTML (Liferay-pagina), geen robots.txt | niets verboden |
| `componentes.cnig.es` | HTTP 502 | ONBEKEND |
| `wms.mapama.gob.es` | niet op te halen, certificaatketen incompleet | ONBEKEND; dienst werkt sowieso niet (§2.6) |

Dat twee robots.txt-bestanden niet op te halen zijn, is een echt gat en het staat hieronder ook bij
de open punten. Wat er wél is: beide diensten verklaren in hun eigen dienstbeschrijving vrij gebruik,
het zijn INSPIRE-diensten waarvan de Europese richtlijn juist open bevraging voorschrijft, en het
tempo is 1 verzoek per 2 seconden. Dat is verdedigbaar, maar het is geen schriftelijke toestemming.

---

## 2. De bronnen, één voor één, met het werkelijke antwoord

### 2.1 SNCZI — waar het nu werkelijk staat

`https://sig.mapama.gob.es/snczi/` antwoordt (HTTP 200) maar is een **kijkvenster**, geen
gegevensdienst: het is de visor-pagina van MITECO. De gegevens erachter — het *Inventario de Zonas
Inundables*, de zones T10/T50/T100/T500, de zona de flujo preferente en het dominio público
hidráulico — worden geleverd door de GeoServer op `gis.miteco.gob.es`, werkruimte `agua`. Dáár is
alles bevraagbaar. Het oude adres `wms.mapama.gob.es/sig/Agua/ZonasInundables/wms.aspx` is dood
(§2.6). Bewijstype 3.

### 2.2 MITECO GeoServer, werkruimte `agua` — het nationale overstromingsregister

| | |
|---|---|
| Adres | `https://gis.miteco.gob.es/geoserver/agua/ows` (WFS) · `.../agua/wms` (WMS) |
| Formaat | WFS 2.0.0 (`application/json`, `csv`, GML) en WMS 1.3.0 (`text/plain`, `application/json`) |
| Kosten en recht | `Fees: CC BY 4.0. Nombrar a la fuente: Ministerio para la Transición Ecológica y el Reto Demográfico` · `AccessConstraints: Sin limitaciones al acceso público` — uit de WMS-GetCapabilities, gelezen 26-09-2026 (bewijstype 1) |
| Sleutel | geen |
| Omvang | 292 feature types in deze werkruimte |

De lagen die wij nodig hebben, alle acht bevraagbaar via WFS `GetFeature` (gecontroleerd met
`DescribeFeatureType`, geometrieveld heet overal `shape`):

| Laag | Wat het is | Kernvelden |
|---|---|---|
| `agua:Zi_laminas_q10` | overstromingszone T=10 jaar (hoge kans) | `id_zona, zona, rio, estudio, fecha_apro, q_m3_s` |
| `agua:Zi_laminas_q50` | T=50 jaar | idem |
| `agua:Zi_laminas_q100` | T=100 jaar (middelgrote kans) | idem |
| `agua:Zi_laminas_q500` | T=500 jaar (lage kans) | idem |
| `agua:ZI_Laminas_ZFP` | zona de flujo preferente — de zwaarste beperking | `id_zona, zona, rio, q_m3_s` |
| `agua:DPH_Estimado` | dominio público hidráulico plus de 5 m-servidumbre en de 100 m-politiezone, onderscheiden in het veld `tipo_zona` | `id_zona, zona, tipo_zona, rio` |
| `agua:DPH_Deslindado` | het ingemeten DPH | — |
| `agua:Zi_arpsi` | gebieden met significant overstromingsrisico | `apsfr_code, apsf_name, origen_inu, estado` |

**Werkelijk antwoord, ijkpunt 1 (perceel AV ARENAL 6(B), `5553425BC5955S`), WFS `INTERSECTS` op de
volledige perceelgrens:**

- `Zi_laminas_q10` → 1 treffer: `ES080_T010_301`, zona `70.30 RIU XALO O GORGOS`, rivier Río Gorgos,
  studie *SNCZI. Zonas Inundables del Sistema Marina Alta*, vastgesteld 31-10-2011, `q_m3_s` 142,379
- `Zi_laminas_q50` → 1 treffer: `ES080_T050_301`, `q_m3_s` 681,603
- `Zi_laminas_q100` → 1 treffer: `ES080_T100_301`
- `Zi_laminas_q500` → 1 treffer: `ES080_T500_301`
- `ZI_Laminas_ZFP` → 1 treffer: `ES080_ZFP_301`

Dat perceel ligt dus zelfs in de T10 én in de zona de flujo preferente. Dit is het bewijs dat de
methode werkt en dat een leeg antwoord elders echt leeg is.

**`DPH_Deslindado` is leeg voor Jávea.** Een bbox-bevraging over de hele gemeente
(`770000,4292000,782000,4302000` in EPSG:25830) geeft `numberMatched: 0`. Het DPH is hier dus nooit
officieel ingemeten; alleen de cartografische schatting `DPH_Estimado` bestaat. Dat is geen detail:
een geschatte DPH-grens kan bij een latere deslinde ergens anders blijken te liggen. Bewijstype 3.

**`Zi_arpsi` is een lijnenlaag, geen vlakkenlaag.** De geometrie van `ES080_ARPS_0006` (Río Gorgos)
komt terug als `MultiLineString`. `INTERSECTS` met een perceel levert daarom bijna nooit iets op;
gebruik `DWITHIN` met een straal. Bewijstype 3.

### 2.3 Confederación Hidrográfica del Júcar

| | |
|---|---|
| Adres | `https://siajucar.chj.es/gis?MAP=services/SIA/<kaartnaam>` |
| Formaat | WMS 1.3.0 **en** WFS 1.1.0 (beide antwoorden vandaag met een geldig capabilities-document) |
| Kosten en recht | `Fees: conditions unknown` · `AccessConstraints: None` — dus **ONBEKEND**, de aanbieder zegt het zelf niet |
| Robots | geen robots.txt (HTTP 404) |

Getoetste kaart: `Areas_con_riesgo_potencial_significativo_de_inundacion_ARPSI`. Ondersteunde
stelsels: CRS:84, EPSG:4326, EPSG:3857, EPSG:25830. Twee bevraagbare lagen.

**Werkelijk antwoord:** `GetFeatureInfo` op alle drie de proefpercelen, op het controlepunt bij de
Gorgos uit N03 en op het Arenal-perceel dat wél in T10 ligt → **vijf keer een leeg antwoord**
("GetFeatureInfo results" met geen enkel kenmerk, HTTP 200). Verklaring: de ARPSI is ook hier een
lijn langs de rivier, en een prikpunt raakt die lijn niet.

**Oordeel:** de CHJ-diensten leven en zijn bereikbaar, maar ze voegen voor onze vraag **niets toe**
aan MITECO, en het gebruiksrecht is er níet vastgelegd terwijl MITECO het wél vastlegt. Dit
bevestigt wat N03 op 18-09 na 156 kaarten al concludeerde. **Niet inbouwen.**

### 2.4 Kustwet (Ley de Costas) — MITECO GeoServer, werkruimte `costas`

| | |
|---|---|
| Adres | `https://gis.miteco.gob.es/geoserver/costas/ows` (WFS) · `.../costas/wms` |
| Formaat | WFS 2.0.0, GeoJSON |
| Kosten en recht | identiek aan `agua`: CC BY 4.0, `Sin limitaciones al acceso público` (gelezen 26-09-2026) |
| Omvang | 95 feature types |

De lagen die ertoe doen:

| Laag | Wat het is | CRS | Kernvelden |
|---|---|---|---|
| `costas:dominio_publico_maritimo_terrestre` | de **deslinde-lijnen**, drie soorten in het veld `tipo_linea` | **EPSG:25830** | `referencia, tm, tipo_linea, sit_admin, om, vertices, estado` |
| `costas:dpmt_terrenos_incluidos` | percelen die volledig in het DPMT liggen | **EPSG:25830** | `referencia, tm, tipo_linea, estado` |
| `costas:nucleos_excluidos` | uitgesloten kernen | EPSG:4258 | `referencia, tm, sit_admin` |
| `costas:Servidumbre_Proteccion` | **niet** de algemene zone — alleen losse kleine terreinen die door hun geringe omvang geheel binnen de SP vallen | EPSG:4258 | `referencia, tm, tipo_linea` |
| `costas:zim_laminas_q100` / `zim_laminas_q500` | overstroming van **mariene** oorsprong, T100 en T500 | EPSG:4258 | `id_zona, zona, cota_max, cota_media, estudio` |

De drie lijnsoorten in `tipo_linea`, alle drie aangetroffen in Jávea:

- `Límite DPMT aprobado` — de buitengrens van het openbaar zeedomein
- `Límite RM aprobada` — de *ribera del mar*
- `Límite SP aprobada` — de buitengrens van de servidumbre de protección
- (plus `Límite DPMT provisional o en tramitación`, in Jávea aanwezig maar ver van onze percelen)

**Werkelijk antwoord, ijkpunt 2 (perceel AV MEDITERRANEO 2(B), `5958201BC5955N`), WFS `INTERSECTS`
met de perceelgrens in EPSG:25830:** drie treffers —
`Límite DPMT aprobado` (dossier `DES01/13/03/0007`, O.M. 27-04-2016, `vertices: SI`),
`Límite RM aprobada` (zelfde dossier) en
`Límite DPMT aprobado` van `DES01/13/03/0007-DES04/01` (O.M. 26-09-2019, `vertices: NO`).
De deslindelijn loopt dus dwars over dat perceel. `dpmt_terrenos_incluidos` gaf daar 0 — die laag
gaat alleen over percelen die er *geheel* in liggen.

**Twee deslinde-dossiers dekken Jávea:** `DES01/13/03/0007` (O.M. 27-04-2016) en
`DES01/08/03/0001` (O.M. 05-04-2011), plus de aanvulling `DES01/13/03/0007-DES04/01`
(O.M. 26-09-2019). Bewijstype 1, uit de dienst zelf.

**Gemeten strookbreedte ter plaatse.** Vanaf het dichtstbijzijnde punt van de DPMT-lijn naar de
SP-lijn: **60,9 m** bij Adsubia en **20,0 m** bij Cap Martí. Die 20 m is precies de breedte die de
Kustwet voorschrijft op grond die bij de inwerkingtreding van de wet al *suelo urbano* was
(disposición transitoria tercera, punt 3, Ley 22/1988 — in N03 op 18-09 in de geconsolideerde tekst
op boe.es gelezen, bewijstype 2). **De breedte staat dus niet vast op 100 m en moet per plek uit de
twee lijnen worden gemeten, niet aangenomen.**

### 2.5 IDEE — landelijke controlekaart, en hij geeft iets wat MITECO niet geeft

| | |
|---|---|
| Adres | `https://servicios.idee.es/wms-inspire/riesgos-naturales/inundaciones` |
| Formaat | WMS 1.3.0, **rasterdienst** (`GetFeatureInfo` geeft `GRAY_INDEX`) |
| Kosten en recht | `Fees: no conditions apply` · `AccessConstraints: "Este servicio se puede usar de modo libre y gratuito en cualquier caso, siempre que se mencione al Ministerio para la Transición Ecológica y el Reto Demográfico como autor y propietario de la información."` (gelezen 26-09-2026, bewijstype 1) |
| Lagen | `NZ.Flood.FluvialT10`, `FluvialT100`, `FluvialT500`, `MarinaT100`, `MarinaT500`, `EL.GridCoverage` |

**Dit is geen ja/nee-laag maar een waterdiepte.** `GRAY_INDEX` is de *calado* in meters. Werkelijke
antwoorden:

| Punt | FluvialT10 | FluvialT100 | FluvialT500 | MarinaT100 | MarinaT500 |
|---|---|---|---|---|---|
| `0481122BC5907N` | 999,0 | 999,0 | 999,0 | −9999,0 | −9999,0 |
| `5246308BC5954N` | 999,0 | 999,0 | 999,0 | −9999,0 | −9999,0 |
| `6442010BC5964S` | 999,0 | 999,0 | 999,0 | −9999,0 | −9999,0 |
| ijkpunt Arenal `5553425BC5955S` | **0,064 m** | **1,376 m** | **1,882 m** | −9999,0 | −9999,0 |

**Let op de twee verschillende leegwaarden:** de fluviale lagen gebruiken `999.0` voor "geen
gegevens / buiten de zone", de mariene lagen `-9999.0`. Wie die als getal optelt, krijgt onzin.
Bewijstype 3.

De marine lagen geven zelfs bij het Arenal-perceel `-9999`, terwijl de vectorlaag
`costas:zim_laminas_q100` in Jávea wél mariene zones kent (`Playa de la Cala Blanca`,
`Playa de la Grava, Playa de Muntanyar`). **Voor mariene overstroming is de MITECO-vectorlaag de
bron; het IDEE-raster is daar onbetrouwbaar.** Voor fluviale overstroming is IDEE juist waardevol,
want het geeft de **waterdiepte** — en dat is het verschil tussen "staat 6 cm water" en "staat
1,9 m water", wat voor een renovatiebegroting en voor de verzekerbaarheid alles uitmaakt.

### 2.6 Wat niet werkt

- `https://wms.mapama.gob.es/...` — `SSL: CERTIFICATE_VERIFY_FAILED, unable to get local issuer
  certificate`. De certificaatketen van die host is incompleet. Ik heb de controle **niet**
  uitgeschakeld. Dood adres; N03 kwam op 18-09 tot dezelfde conclusie via een andere fout.
- `https://www.cartociudad.es` — de geocoder wérkt (op "Calle Jaume Huguet 6, Javea" antwoordt hij
  met `muni: Xàbia/Jávea`, `muniCode: 03082`, `postalCode: 03739`), maar de WMS bevat geen enkele
  laag met "inunda" of "costa". **Cartociudad is een adressendienst, geen risicodienst.** Als omweg
  voor deze vraag ongeschikt. Wel bruikbaar als we ooit van adres naar coördinaat moeten — maar dat
  doet `dh/catastro.py` al.
- `https://componentes.cnig.es/robots.txt` — HTTP 502.

---

## 3. De drie proefpercelen: het werkelijke antwoord

### 3.1 Overstroming

Exacte afstand in meters van de **perceelgrens** tot de zone (0,0 = het perceel ligt erin of raakt
de rand). Berekend op de geometrie die de dienst zelf teruggaf, geknipt op het gebied Jávea.

| Laag | `0481122BC5907N` | `5246308BC5954N` | `6442010BC5964S` | ijkpunt Arenal |
|---|---|---|---|---|
| `Zi_laminas_q10` (T10) | 1.424 m | 231 m | 231 m | **0 m** |
| `Zi_laminas_q50` (T50) | 1.383 m | 198 m | 212 m | **0 m** |
| `Zi_laminas_q100` (T100) | 1.383 m | 165 m | 196 m | **0 m** |
| `ZI_Laminas_ZFP` (flujo preferente) | 1.424 m | 226 m | 231 m | **0 m** |
| `DPH_Estimado` (waterloop + 5 m + 100 m) | 2.295 m | 2.210 m | 3.207 m | 1.807 m |
| `zim_laminas_q100` (marien) | 4.235 m | 1.027 m | 815 m | 378 m |
| `zim_laminas_q500` (marien) | 4.235 m | 1.027 m | 808 m | 378 m |
| `Zi_arpsi` (dichtstbijzijnde) | > 1.000 m | > 1.000 m | 500–1.000 m: `ES080_ARPS_0055` *Playa de la Cala Blanca*, origen `Marina`, `APROBADA` | — |

Dezelfde uitkomst, via de dienst zelf bevraagd (WFS `INTERSECTS` op de perceelgrens): **0 treffers
op alle acht de lagen, voor alle drie de percelen.** En nog eens via WMS `GetFeatureInfo` op het
zwaartepunt: **geen enkele treffer.** Drie methoden, hetzelfde antwoord.

**Conclusie per perceel:**
- `0481122BC5907N` (Penyaparda) — ruim buiten alles. Dichtstbijzijnde overstromingszone 1,4 km.
- `5246308BC5954N` (Jaume Huguet 6, Adsubia) — **buiten de zone, maar de T100 van de Gorgos begint
  op 165 m.** Dat is dichtbij genoeg om bij een herziening van de kaart te kunnen verschuiven.
- `6442010BC5964S` (Cap Martí) — buiten de zone; T100 op 196 m, en op 500–1.000 m ligt de mariene
  ARPSI *Playa de la Cala Blanca*.

### 3.2 Kustwet

Exacte afstand van de perceelgrens tot elke deslinde-lijnsoort, gerekend op de 45 lijnstukken die de
dienst voor heel Jávea teruggaf:

| Lijn | `0481122BC5907N` | `5246308BC5954N` | `6442010BC5964S` | ijkpunt `5958201BC5955N` |
|---|---|---|---|---|
| `Límite DPMT aprobado` | 4.143 m | 1.016 m | 841 m | **0,0 m** |
| `Límite RM aprobada` | 4.219 m | 1.048 m | 1.200 m | **0,1 m** |
| `Límite SP aprobada` | 4.043 m | 1.028 m | 821 m | **18,3 m** |
| strookbreedte DPMT→SP ter plaatse | — | 60,9 m | 20,0 m | — |
| `dpmt_terrenos_incluidos` | 0 treffers | 0 treffers | 0 treffers | 0 treffers |
| `nucleos_excluidos` | 0 treffers | 0 treffers | 0 treffers | — |

**Conclusie:** geen van de drie percelen valt onder de servidumbre de protección. Het bewijs is niet
"geen treffer" maar de rekensom: bij perceel 2 is de afstand tot de SP-lijn (1.028 m) en tot de
DPMT-lijn (1.016 m) elk ruim honderd keer de strookbreedte ter plaatse (60,9 m); het perceel ligt dus
niet tússen de twee lijnen maar ver landinwaarts. Bij perceel 3 idem (821 m en 841 m tegen een strook
van 20,0 m). Bij het ijkpunt is de verhouding omgekeerd: 0,0 m tot de DPMT-lijn en 18,3 m tot de
SP-lijn, dus dat perceel ligt in de strook.

### 3.3 Hoe ik weet dat de nullen echt nul zijn

Vier ijkingen, alle vier vandaag uitgevoerd:

1. **Overstroming, positief:** perceel `5553425BC5955S` → 5 van de 5 fluviale lagen geven een
   treffer. Niet-leeg is dus mogelijk met precies dezelfde aanroep.
2. **Kust, positief:** perceel `5958201BC5955N` → 3 treffers op de deslinde-lijnen.
3. **Volgorde van de coördinaten:** hetzelfde vlak rond hetzelfde punt, één keer met breedte eerst en
   één keer met lengte eerst. Breedte eerst → 1 treffer; lengte eerst → 0 treffers, zónder
   foutmelding. Dit is de stille fout waar N03 voor waarschuwde en die vandaag ook werkelijk optrad.
4. **Eenheid van `DWITHIN`:** een punt op ~5,2 km ten oosten van een punt binnen de T100-zone.
   `DWITHIN … 1000, meters` → 0 treffers; `… 5000, meters` → 1 treffer. GeoServer rekent dus
   werkelijk in meters, ook bij een laag in graden. Bewijstype 3.

### 3.4 Wat dit over de rest van de database zegt

Ik heb de deslinde-lijnen van heel Jávea één keer opgehaald (45 lijnstukken, 141 KB, één verzoek) en
lokaal de afstand berekend voor alle **622 percelen met een grens** in de database:

| Afstand tot `Límite DPMT aprobado` | Aantal percelen |
|---|---|
| minder dan 20 m | **25** |
| 20 tot 100 m | 21 |
| 100 tot 500 m | 75 |
| 500 m tot 2 km | 245 |
| 2 km of meer | 231 |

De dichtstbijzijnde staan met hun voeten in het water: `03042A00600119` (El Garsiva, Benitachell) en
`5956703BC5955N` op 0,0–0,2 m, `5958201BC5955N` (Av. Mediterráneo) op 0,1 m, `6652509BC5965S`
(Arenal-Montañar 14) op 0,3 m, `03082A00800002` (Saladar) en `03082A00700001` (polígono "COSTAS")
eveneens binnen een meter.

En met dezelfde werkwijze tegen de T500-zone van de Gorgos: **36 percelen** hebben minstens één
hoekpunt in de zone, waaronder Av. Arenal 6, Arenal-Montañar 43, Av. Augusta 30, Camí Fontana 10 en
een reeks kavels in Sortetes, Comunes en Clot de Guas.

**Dat is geen theorie maar de huidige aanbodlijst.** Die percelen worden nu doorgerekend alsof er
niets aan de hand is.

---

## 4. De valstrikken, opgeschreven zodat ze niet opnieuw toeslaan

### 4.1 Het coördinatenstelsel verschilt per laag, niet per dienst

| Laag | `DefaultCRS` | Volgorde in een CQL-filter |
|---|---|---|
| `agua:Zi_laminas_q10/q50/q100/q500` | `EPSG::4258` | **breedte lengte** (graden) |
| `agua:ZI_Laminas_ZFP`, `DPH_Estimado`, `DPH_Deslindado`, `Zi_arpsi` | `EPSG::4258` | breedte lengte |
| `costas:zim_laminas_q100/q500`, `nucleos_excluidos`, `Servidumbre_Proteccion` | `EPSG::4258` | breedte lengte |
| **`costas:dominio_publico_maritimo_terrestre`** | **`EPSG::25830`** | **X Y in meters** |
| **`costas:dpmt_terrenos_incluidos`** | **`EPSG::25830`** | **X Y in meters** |

Mijn eerste kustronde gebruikte graden op alle kustlagen. Uitkomst: "geen deslinde binnen 3.000 m"
voor alle drie de percelen — terwijl Cap Martí er 841 m vandaan ligt. HTTP 200, lege
FeatureCollection, geen enkele waarschuwing. **Leg daarom per laag het stelsel vast in de code en
laat elke ronde één ijkcoördinaat per laag meelopen die raak hóórt te zijn. Komt die leeg terug, dan
is de zeef stuk en niet het perceel schoon.**

### 4.2 Andere dingen die vandaag bleken

- **`propertyName` mag niet leeg zijn.** Een `propertyName=None` geeft HTTP 400 met een
  ExceptionReport, niet een genegeerde parameter.
- **Vraag de geometrie niet op als je hem niet nodig hebt.** Laat `shape` uit `propertyName` en het
  antwoord krimpt van megabytes naar honderden bytes.
- **De `clip`-parameter van GeoServer werkt op WFS.** `clip=POLYGON((...))` knipt de geometrie op het
  opgegeven vlak. Daarmee is het hele werkgebied in één verzoek per laag op te halen:
  Zi_laminas_q100 210 KB, Zi_laminas_q10 219 KB, ZI_Laminas_ZFP 1,5 MB, Zi_laminas_q50 1,6 MB,
  DPH_Estimado 1,4 MB, zim_laminas_q100 20 KB, zim_laminas_q500 20 KB. Samen ± 5 MB. Let op: aan de
  rand van het knipvlak ontstaat een kunstmatige lijn, dus afstanden groter dan ongeveer de helft van
  de marge zijn indicatief.
- **`agua:Zi_arpsi` en de CHJ-ARPSI zijn lijnen.** Gebruik `DWITHIN`, niet `INTERSECTS`.
- **De GeoServer serveert geen `/robots.txt`** maar wél `/geoserver/...`. Het verbreken van de
  verbinding op de wortel is dus geen blokkade van ons, maar een ontbrekend pad.

---

## 5. Voorstel: wat wij in `dh/` bouwen

Zelfde vorm als `dh/hoogte.py` + `dh/enrich_helling.py` (N08): een module die meet en een module die
de database vult, met de bron en het gebruiksrecht in de docstring.

### 5.1 `dh/water_kust.py` — de metende laag

Zeven aanroepen per perceel, alle op `https://gis.miteco.gob.es/geoserver/`, WFS 2.0.0,
`outputFormat=application/json`, `count=5`, en telkens met de volledige perceelgrens uit
`parcels.geojson` (afgekapt op 60 punten) als filtergeometrie:

| # | Werkruimte en laag | Filter | Geometrie in | `propertyName` |
|---|---|---|---|---|
| 1 | `agua:ZI_Laminas_ZFP` | `INTERSECTS(shape, <polygoon>)` | graden, breedte eerst | `id_zona,zona,rio,q_m3_s` |
| 2 | `agua:Zi_laminas_q100` | `INTERSECTS(shape, <polygoon>)` | graden | `id_zona,zona,rio,estudio,fecha_apro,q_m3_s` |
| 3 | `agua:Zi_laminas_q500` | `INTERSECTS(shape, <polygoon>)` | graden | idem |
| 4 | `agua:DPH_Estimado` | `DWITHIN(shape, <polygoon>, 100, meters)` | graden | `id_zona,zona,tipo_zona,rio` |
| 5 | `costas:dominio_publico_maritimo_terrestre` | `DWITHIN(shape, <polygoon>, 250, meters)` | **meters, EPSG:25830** | `referencia,tm,tipo_linea,sit_admin,om,vertices` |
| 6 | `costas:zim_laminas_q100` | `INTERSECTS(shape, <polygoon>)` | graden | `id_zona,zona,cota_max,estudio` |
| 7 | `servicios.idee.es` WMS `GetFeatureInfo` op `NZ.Flood.FluvialT100` en `FluvialT500` | zwaartepunt, EPSG:25830 | — | waterdiepte in meters |

Alleen als 5 iets oplevert, twee vervolgstappen: de lijngeometrie ophalen en (a) de afstand tot
`Límite DPMT aprobado` en tot `Límite SP aprobada` uitrekenen, (b) de strookbreedte ter plaatse
meten. De rekenregel voor "ligt in de servidumbre de protección" is dan:

> afstand(perceel, DPMT-lijn) + afstand(perceel, SP-lijn) ligt binnen 10 % van de strookbreedte ter
> plaatse → het perceel ligt **tussen** de twee lijnen, dus in de servidumbre.
> Is afstand(perceel, SP-lijn) kleiner dan afstand(perceel, DPMT-lijn), dan ligt het landinwaarts van
> de SP → erbuiten. Is het omgekeerd en is afstand(perceel, DPMT-lijn) ≈ 0 → het perceel raakt het
> DPMT zelf, en dat is de zwaarste uitkomst.

Getoetst op vier percelen (drie negatief, één positief) en op twee plaatsen waar de strookbreedte
verschilt (60,9 m en 20,0 m). Nooit de 100 m uit de wet aannemen: meet hem.

### 5.2 `dh/enrich_water_kust.py` — de vullende laag

Nieuwe kolommen op `parcels` (via `ALTER TABLE`, net als `enrich_helling.zorg_kolommen`):

| Kolom | Type | Inhoud |
|---|---|---|
| `zfp` | INTEGER | 1 = perceel ligt in de zona de flujo preferente |
| `inundacion_t100` | INTEGER | 1 = in de T100 |
| `inundacion_t500` | INTEGER | 1 = in de T500 |
| `inundacion_zona` | TEXT | `id_zona` van de raakste zone, bv. `ES080_T100_301` |
| `inundacion_rio` | TEXT | `rio` / `zona`, bv. `Río Gorgos` |
| `inundacion_studie` | TEXT | `estudio` + `fecha_apro` — wélke studie, van wanneer |
| `inundacion_afstand_m` | REAL | afstand tot de dichtstbijzijnde zone als het perceel er niet in ligt |
| `calado_t100_m` / `calado_t500_m` | REAL | waterdiepte uit IDEE; leeg bij 999 of −9999 |
| `dph_zone` | TEXT | `DPH Cartográfico` / `Zona de Servidumbre` / `Zona de Policía` binnen 100 m, of leeg |
| `marien_t100` | INTEGER | 1 = in `costas:zim_laminas_q100` |
| `kust_dpmt_m` | REAL | afstand tot `Límite DPMT aprobado` |
| `kust_sp_m` | REAL | afstand tot `Límite SP aprobada` |
| `kust_strook_m` | REAL | gemeten strookbreedte ter plaatse (20 of 100 m, of wat er staat) |
| `kust_oordeel` | TEXT | `in_dpmt` / `in_servidumbre` / `nabij` (< 250 m) / `buiten` |
| `kust_dossier` | TEXT | `referencia` + `sit_admin`, bv. `DES01/13/03/0007 (O.M. 27/04/2016)` |
| `water_kust_at` | TEXT | tijdstip van de meting |
| `water_kust_bron` | TEXT | vaste tekst met bron en licentie, voor de bronvermelding in dossiers |

Een perceelgrens verandert niet en deze kaarten veranderen zelden, dus: **één keer meten en bewaren**,
opnieuw alleen op verzoek (`--opnieuw`) of als de perceelgeometrie verandert. Voor de bulk van 622
percelen de weg uit §4.2: zeven `clip`-verzoeken voor het hele gebied, daarna lokaal rekenen —
dat is één ronde van ongeveer 15 seconden netwerk in plaats van 4.300 verzoeken.

### 5.3 Wat het systeem ermee doet

1. **`dh/signals.py`** krijgt er drie signalen bij: `zona_flujo_preferente`, `overstroming_t100`,
   `kustwet`. De ZFP is bouwkundig de zwaarste: daar is nieuwbouw in de regel uitgesloten.
2. **`dh/prefilter.py`** — een bouwkavel in de ZFP is geen bouwkavel. Net zoals `signals.py` nu al
   rustieke grond herkent, hoort dit een harde uitsluiter te worden.
3. **`tools/haalbaarheid.py`** — bij `inundacion_t100` of `calado_t100_m > 0` hoort een kostenpost of
   op zijn minst een waarschuwing: verhoogd bouwpeil, geen souterrain, hogere of geweigerde
   opstalverzekering. **Het bedrag daarvoor is ONBEKEND en moet Jan vaststellen** (zie de vragen).
4. **`dh/dossier.py`** — per object een regel met de zone, de studie, de datum en, als er iets speelt,
   de zin: *dit is een kaartuitslag, geen juridisch oordeel; vraag een certificado de Costas /
   informe del organismo de cuenca aan.*
5. **`dh/alerts.py`** — een perceel dat in de ZFP of in het DPMT ligt mag nooit in de categorie
   *direct* terechtkomen, hoe goed de rekensom ook is.

---

## 6. Wat wij niet weten

- **Wat er in de robots.txt van `gis.miteco.gob.es` en `servicios.idee.es` staat. ONBEKEND.** Beide
  hosts verbreken de verbinding op dat pad. De diensten verklaren zelf vrij gebruik.
- **Het gebruiksrecht van de CHJ-diensten. ONBEKEND** — `Fees: conditions unknown`. Voorstel: niet
  gebruiken, want ze voegen niets toe.
- **Of `DPH_Estimado` in Jávea ergens dichter bij onze percelen komt dan de gemeten 2,2–3,2 km.** De
  meting is gedaan op de geknipte geometrie; boven ongeveer 2 km is dat indicatief.
- **Of de zone T100 sinds de studie van 2011 is herzien.** De velden `fecha_apro` (31-10-2011) en
  `ciclo` zitten in de laag, maar of er een nieuwere cyclus loopt is niet nagegaan.
- **Wat een ligging in T100 of ZFP in Jávea financieel kost** — verzekeringspremie, weigering,
  verplichtingen van de gemeente bij de bouwvergunning. Niet onderzocht.
- **Of het gemeentelijk plan van Xàbia (PGOU) een eigen, strengere overstromingskaart kent.** De
  Valenciaanse PATRICOVA staat op `mediambient.gva.es` en die host is voor ons verboden terrein;
  N03 haalde PATRICOVA op 18-09 via `terramapas.icv.gva.es` en dat adres is vandaag niet opnieuw
  getoetst.

---

## 7. Bronnen, alle op 26-09-2026 aangeroepen

| # | URL | Wat eruit kwam | Bewijstype |
|---|---|---|---|
| 1 | `https://gis.miteco.gob.es/geoserver/agua/ows?service=WFS&request=GetCapabilities` | 292 feature types, alle overstromingslagen WFS-bevraagbaar | 1 |
| 2 | `https://gis.miteco.gob.es/geoserver/agua/wms?service=WMS&request=GetCapabilities` | `Fees: CC BY 4.0…`, `AccessConstraints: Sin limitaciones al acceso público` | 1 |
| 3 | `https://gis.miteco.gob.es/geoserver/agua/ows` — `DescribeFeatureType` op 4 lagen | geometrieveld `shape`, veldenlijst per laag | 1 |
| 4 | `https://gis.miteco.gob.es/geoserver/agua/ows` — `GetFeature` met `INTERSECTS` | 0 treffers op de drie percelen, 5 treffers op het ijkperceel | 3 |
| 5 | `https://gis.miteco.gob.es/geoserver/agua/ows` — `GetFeature` met `DWITHIN` | afstandsbereiken; eenheid meters geverifieerd | 3 |
| 6 | `https://gis.miteco.gob.es/geoserver/agua/wms` — `GetFeatureInfo` | geen treffer op de drie percelen (tweede methode) | 3 |
| 7 | `https://gis.miteco.gob.es/geoserver/costas/ows?service=WFS&request=GetCapabilities` | 95 feature types; DPMT-lagen in EPSG:25830 | 1 |
| 8 | `https://gis.miteco.gob.es/geoserver/costas/wms?service=WMS&request=GetCapabilities` | zelfde licentie als `agua` | 1 |
| 9 | `https://gis.miteco.gob.es/geoserver/costas/ows` — `GetFeature` DPMT | deslinde-dossiers `DES01/13/03/0007`, `DES01/08/03/0001`, `DES01/13/03/0007-DES04/01` | 1 |
| 10 | `https://servicios.idee.es/wms-inspire/riesgos-naturales/inundaciones` | 6 bevraagbare lagen; `Fees: no conditions apply`; waterdiepte 1,376 m op het ijkperceel | 1 en 3 |
| 11 | `https://siajucar.chj.es/gis?…ARPSI…&REQUEST=GetCapabilities` (WMS én WFS) | dienst leeft; `Fees: conditions unknown` | 1 |
| 12 | `https://siajucar.chj.es/gis?…GetFeatureInfo` | vijf keer leeg, ook op twee ijkpunten | 3 |
| 13 | `https://sig.mapama.gob.es/snczi/` | visor-pagina, geen gegevensdienst | 3 |
| 14 | `https://wms.mapama.gob.es/sig/Agua/ZonasInundables/wms.aspx` | `CERTIFICATE_VERIFY_FAILED` — dood | 3 |
| 15 | `https://www.cartociudad.es/geocoder/api/geocoder/findJsonp` | geocoder werkt; geen risicolagen in de WMS | 3 |
| 16 | `https://www.idee.es/robots.txt` | `User-Agent: * / Disallow:` | 1 |
| 17 | `https://www.chj.es/robots.txt`, `https://siajucar.chj.es/robots.txt` | HTTP 404, geen robots.txt | 1 |

**Ruw bewijs:** `onderzoek/N09-toetsen/` — `calls.jsonl` is het volledige logboek van alle 222
verzoeken (tijdstip, URL, status, bytes, duur); `res_*.json` zijn de antwoorden per bron;
`deslinde_javea.geojson` is de opgehaalde kustgrens van heel Jávea; `afstanden_kust_alle.json` de
berekende afstand van elk perceel in de database tot die grens.

Eerder werk waarop dit voortbouwt: `onderzoek/N03-risicokaarten.md` (18-09-2026) — dit rapport
bevestigt de laagnamen en adressen daaruit, corrigeert de conclusie dat de koppeling in Node moet,
en voegt WFS-bevraging, de CRS-per-laag-valstrik, de mariene lagen, de waterdiepte uit IDEE en de
meting over de hele database toe.

---

## ⏸️ ACTIE VOOR JAN — drie vragen

1. **Hoe hard moet de zeef zijn?** Mijn voorstel: een perceel in de *zona de flujo preferente* of in
   het *dominio público marítimo-terrestre* valt automatisch af als bouwkavel — daar is nieuwbouw in
   de regel uitgesloten. Een perceel in de T100 blijft meedoen maar met een waarschuwing. Ben je het
   daarmee eens, of wil je ook T100 automatisch laten afvallen?
2. **Wat kost een ligging in de overstromingszone in jouw begroting?** Verhoogd bouwpeil, geen
   souterrain, duurdere of geweigerde opstalverzekering — bij de helling hebben we € 15.000 en
   € 50.000 van jou gekregen en dat werkt goed. Hier heb ik geen getal en ik ga er geen verzinnen.
   Eén bedrag voor "in T100" en één voor "in de ZFP" is genoeg om mee te rekenen.
3. **Wil je dat ik de 25 percelen binnen 20 m van de kustgrens en de 36 percelen in de T500 nu meteen
   nalopen en als aparte lijst opleveren?** Die staan nu in het aanbod alsof er niets aan de hand is.
   Het is ongeveer een uur werk en het raakt objecten die al in je dagrapport hebben gestaan.

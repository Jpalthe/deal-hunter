# B03 — Ontwikkelaars, nieuwbouwnetwerken en hun feeds

**Onderzoeksstroom B03 · controledatum 16-09-2026 · werkgebied Jávea/Xàbia, Benitachell (Cumbre del Sol), Moraira/Teulada**

Bewijstypen: 1 = door aanbieder vermeld · 2 = officiële bron/juridisch document · 3 = zelf vastgesteld
· 4 = afleiding · 5 = berekening · 6 = professional · 7 = onbekend/tegenstrijdig.

Alles hieronder is één of twee nette verzoeken per site (WebFetch of curl met standaard browser-user-agent).
Geen scraping, niets omzeild. Waar een site alleen met JavaScript laadt of 403/404/500 gaf, staat dat als
beperking vermeld in §7.

---

## 0. Conclusie in het kort

1. **De grootste ontbrekende bron is Metainmo** (`spain.metainmo.com`, Propiedad Inmobiliaria Online S.L.,
   Alicante): een B2B-nieuwbouwplatform met een **betaalde XML-download van de hele databank**, en met
   werkelijke dekking in ons gebied — 9 promoties in Jávea, **19 in Benitachell**, 7 in Moraira
   (zelf geteld, 16-09-2026). Het staat niet in het register. Prioriteit **hoog**.
2. **AEDAS Homes bouwt groot in Jávea** (Unic, in verkoop vanaf 370.000 €; Brisas del Arenal, uitverkocht)
   en heeft een **API-portaal voor collaborators** (`colaboradores-api.aedashomes.com`, bestaat, geeft
   HTTP 200). AEDAS staat niet in tabel K-2 van R07 en niet in het register. Prioriteit **hoog** — vooral
   als afnemer/partner (route C en D), niet als koopkans.
3. **Bij Resales-Online (R2-24, al bekend) misten wij een route:** de *New Development MLS* met 550+ live
   projecten, inclusief Jávea, mét ontwikkelaarsdocumenten (plattegronden, prijslijsten, beschikbaarheids-
   sheets) en een **projectfeed naar de eigen website**. Dat is een ander product dan de resale-WebAPI V6
   waar wij op wachten. Prioriteit **hoog** — meenemen in hetzelfde lidmaatschapsgesprek.
4. **VAPF** (in R07 genoemd, niet in het register als eigen regel) heeft een **professioneel extranet**
   (`extranet.vapf.com`, HTTP 307 → `/es/`) en houdt jaarlijkse makelaarsconventies. VAPF is de
   dominante partij in Cumbre del Sol; Benitachell-nieuwbouw loopt praktisch via hen.
5. **Taylor Wimpey España** komt ons gebied wél binnen ("Aqua Phase 2 – Moraira" staat op hun
   *coming soon*-lijst), maar biedt geen zichtbaar makelaarsprogramma en geen feed.
6. **Metrovacesa, Neinor en TM Grupo Inmobiliario: geen bewijs van projecten in de Marina Alta.**
   Culmia zit in Dénia (aangrenzend, buiten onze drie gemeenten). Voor ons niet interessant — dat is
   hier ook het eerlijke antwoord.
7. **Voor route B (stilgevallen/onafgebouwd) levert de nieuwbouwhoek géén directe kanslijst op.** Wat
   het wél oplevert zijn drie indirecte routes die nog niet in het register staan: Brainsre-module
   *licencias de obra nueva*, de MIVAU-reeks *visados de dirección de obra en certificaciones de fin de
   obra*, en de **tablones van Benitatxell en Teulada** (het register kent alleen Xàbia).
8. Afgevallen na controle: **Vivia** (= Vivia Homes, huurbeheerder, geen koopaanbod), **obranueva.com**
   (cooperatievegestora Madrid/Alicante-stad, geen Marina Alta), **"Nuevaobra"** als merk bestaat niet;
   wat er wél is heet obranueva.org/obrasnuevas.com en had geen aantoonbare route voor ons.

---

## 1. Nieuwbouwaggregators met een LEESroute

### 1.1 Metainmo — B2B-nieuwbouwdatabank met XML-download · **NIEUW · prioriteit hoog**

| | |
|---|---|
| URL | https://spain.metainmo.com (juridisch: metainmo.com) |
| Exploitant | **Propiedad Inmobiliaria Online, S.L.**, N.I.F. **B16403891**, Avenida Maisonnave 28 bis 4, 03003 Alicante; Registro Mercantil de Alicante, Tomo 4655, Folio 198, Hoja A190957 (· 2) |
| Zakelijk contact | tel. +34 695 518 755 (· 2) |
| Toegang | Registratie als **agencia** + betaald abonnement (SaaS); XML zit in de tarieven "Básico + XML" en "Completo" (· 1) |

**Wat het is.** Geen consumentenportaal maar een verkoopinstrument voor makelaars: *"Explora la
herramienta de venta colaborativa de obra nueva B2B"* en *"La base de datos de obra nueva con comisiones
para agentes más completa de España"* (· 1). Naast obra nueva draaien er drie nevenrubrieken: *Viviendas
MLS Para colaborar*, *Listado de Solicitudes Colaborativas* (vraag van collega's) en *Viviendas de
portales* (· 3, zelf gezien in de navigatie).

**Dekking in ons werkgebied** (zelf geteld op de publieke overzichtspagina's, 16-09-2026, · 3):

| Gemeente | Promoties | URL |
|---|---|---|
| Jávea/Xàbia | **9** | `/alicante/javeaxabia/promociones` |
| Benitachell | **19** | `/alicante/benitachell/promociones` |
| Moraira | **7** | `/alicante/moraira/promociones` |
| Teulada | 0 | `/alicante/teulada/promociones` |
| Benissa (aangrenzend) | 8 | `/alicante/benissa/promociones` |
| Dénia (aangrenzend) | 5 | `/alicante/denia/promociones` |

De Jávea-lijst bevat onder meer *Montgó Villa* (2.600.000 €), *Montañar Residential* (610.702–840.653 €,
6 eenheden), *Unic Javea III en IV* (370.000–740.000 €), *Avenida de Palmela Residencial*
(385.000–650.000 €, 8 eenheden) en *Carretera del Cap de la Nau* (386.500–465.000 €, 8 eenheden) (· 3).
Daarnaast een aparte promotoradirectory: *"18 Promotoras en Jávea/Xàbia"* — *"listado de 18 empresas
urbanizadoras que disponen de una sede o proyectos de obra nueva en Jávea/Xàbia"* (· 1; de namenlijst
zelf laadt met JavaScript en is niet opgehaald, · 7).

**Uniek of niet?** **Deels.** *Avenida de Palmela* is herkenbaar Living Jávea en *Carretera del Cap de la
Nau* herkenbaar Adeya/Aelca — partijen die R07 al kent; *Unic* is AEDAS Homes (prijs vanaf 370.000 €
komt exact overeen met de AEDAS-projectpagina, · 3/4). Uniek is vooral (a) de losse villa-promoties van
kleine bouwers die op geen enkel portaal in ons register als "promotie" staan, (b) **Benitachell met 19
promoties**, waar ons huidige beeld vrijwel leeg is, en (c) de commerciële laag: provisie, betaalschema's,
memoria de calidades, directe contactpersoon bij de promotor.

**Kosten** (· 1, prijspagina 16-09-2026): vier tarieven (Básico, Básico + XML, Básico con informes,
Completo), maandelijks/kwartaal/halfjaar/jaar. De bedragen per tarief laden met JavaScript en zijn **niet
vastgesteld** (· 7). Wél zichtbaar: *"Registro del servicio 125 €"*, *"+1 XML para portales secundarios
20 €/mes"*, *"Usuarios adicionales de agencia para Back End 20 €/mes"*, *"Se aplica un IVA del 21 %
adicional"*, en 10 % korting voor verenigingen vanaf 10 gebruikers. Zelf opgegeven marktcijfers Costa
Blanca: *"350+ promociones · 8000+ inmuebles · 3-15 % comisión por venta"* (· 1).

**Gebruiksrechten — bepalend.** De *Condiciones generales de uso (Agencias)* zeggen (· 2, letterlijk):

> *"El presente documento regula la relación entre Metainmo y las agencias, estableciendo el marco bajo el
> cual se facilita el acceso a información relativa a inmuebles y promociones, incluyendo, entre otros,
> precios, disponibilidad, imágenes, planos y memorias de calidades, bajo un modelo de suscripción SaaS.
> Las agencias emplearán esta información para consultar las promociones y gestionar la venta de los
> inmuebles con sus propios clientes."*

> *"Queda prohibido modificar, copiar, reproducir, comunicar públicamente, transformar, distribuir o
> difundir, por cualquier medio, la totalidad o parte de los contenidos e información incluidos en
> Metainmo, así como cualquier otra información proveniente de la misma, sin la autorización previa,
> expresa y por escrito de Metainmo o, en su caso, del titular de los derechos correspondientes.
> No obstante, las agencias podrán utilizar el material gráfico disponible en la Plataforma exclusivamente
> para la promoción y venta de los inmuebles ofertados."*

En over de betrouwbaarheid: *"Metainmo no garantiza la exactitud ni la veracidad de los datos facilitados
por las promotoras, siendo estas las únicas responsables de los posibles errores"* (· 2).

**Vertaling naar onze vlaggen.**
- *automated_access*: ja, maar **alleen via het betaalde XML-tarief** — de publieke pagina's leeglezen valt
  onder het kopieerverbod (· 4).
- *storage*: **voorwaardelijk**. Het XML-tarief is er letterlijk voor *"integrarse con su sitio web o CRM"*,
  dus opslag in een eigen systeem is de bedoelde werkwijze; maar de algemene clausule verbiedt reproductie
  zonder schriftelijke toestemming. Dat is spanning die je vóór aansluiting schriftelijk wegneemt.
- *history* (prijshistorie bewaren): **ONBEKEND**, niet geregeld — expliciet vragen.
- *ai_analysis*: **ONBEKEND**, niet geregeld — expliciet vragen.
- *show_to_clients*: ja voor beeldmateriaal, maar *"exclusivamente para la promoción y venta de los
  inmuebles ofertados"* — dus niet los gebruiken in eigen acquisitierapporten (· 2/4).
- *personal_data*: bevat zakelijke contactpersonen van promotoren, geen particulieren (· 4).

**Volgende stap.** Offerte opvragen voor "Básico + XML" mét één schriftelijke vraag erbij: mogen wij de
XML in ons eigen systeem opslaan, historie bewaren en intern met AI analyseren voor acquisitie (niet voor
publicatie)? Zonder dat antwoord geen aansluiting.

### 1.2 Resales-Online **New Development MLS** — gemiste route bij een bekende partij · prioriteit hoog

Het register kent Resales-Online als R2-24 (MLS + CRM, WebAPI V6, resales). Het **nieuwbouwproduct is een
apart systeem**: *"over 550 live projects"* in Alicante en Murcia (· 1). Dekking wordt met naam genoemd:
*"Alicante, Benidorm, Javea, Finestrat, Orihuela Costa and Los Alcazares"* — **Jávea staat er expliciet in**;
Dénia, Moraira en Benitachell worden niet genoemd (· 1, 16-09-2026).

Wat agents krijgen: *"direct access to all the developer files: Floor plans, Branded Price lists,
Brochures, Availability sheets, Quality specifications, Payment schedules"* en de mogelijkheid om
*"Full new development projects, Price-range project listings, Single-unit properties"* automatisch naar
de eigen site te voeren (· 1). Kwaliteitsbewaking: *"The developer drop boxes are manually checked by hand
every 8-10 days with the date show when the projects were last checked"* (· 1).

Kosten: niet gepubliceerd; het blog noemt alleen een proefperiode (*"take a 2 week free trial with discount
code CB50/100"*) en een telefoonnummer (· 1) — de prijspagina was ook in R04 al geblokkeerd (· 7).
Rechten: dezelfde contractuele beperking als bij R2-24 — **CONTRACT OF TOESTEMMING NODIG** vóór intern
gebruik. Dit product wijzigt die conclusie niet, het verbreedt alleen waar we om moeten vragen.

**Volgende stap.** In het lopende lidmaatschapsspoor (R04 §3.2) expliciet óók de New Development MLS en de
projectfeed noemen, en dezelfde vier vragen stellen (opslaan, historie, AI, tonen aan Jan).

### 1.3 EstateNearMe (voorheen Inmofind) — promotoradirectory met dekking · prioriteit middel

`spain.inmofind.com` stuurt met HTTP 302 door naar `spain.estatenearme.com` (· 3, zelf vastgesteld) — het
portaal dat in de vakpers nog "Inmofind" heet, draait nu onder de naam EstateNearMe. Sitestructuur, menu's
en URL-patronen zijn vrijwel identiek aan Metainmo (· 4: waarschijnlijk hetzelfde platform of dezelfde
bouwer; **niet bevestigd**, · 7).

Bruikbaar is vooral de **promotoradirectory**: *"236 Promotoras inmobiliarias en Alicante Provincia"*, met
**14 promotoras in Jávea/Xàbia, 3 in Benitachell en 1 in Teulada** (· 1/3, 16-09-2026). Verder biedt de
zoekfunctie de filters *"Estado de la obra: Sobre plano · En construcción · Obra nueva terminada"* (· 3) —
relevant voor route B, zie §4.4. Er is een professionele kant (*"¿Eres un Profesional? Regístrate como
empresa · Publicar la cartera"*), maar **geen XML of API gevonden** (· 7). De promotielijsten per gemeente
konden wij niet aanroepen (de beproefde URL-patronen gaven 404, · 3).

**Uniek?** Als objectbron: nee/deels. Als **namenlijst van ontwikkelaars per gemeente** wel — dat is
precies de lijst die R07 nog niet had. Handmatig, één keer per kwartaal.

### 1.4 viviendasnuevas.com — klein, maar wel Cumbre del Sol · prioriteit laag

Exploitant: *"Marketing Digital Hispania S.L."* (· 1). Voor **La Cumbre del Sol** staan er drie promoties,
waaronder *Residencial Plus Jazmines* (vanaf 1.754.625 €) en *Vall del Portet* met status *"Todo vendido"*
(· 1, 16-09-2026). Er is een *"Alta de agente"*, maar geen XML, API of dataproduct gevonden (· 7).
Voegt naast Metainmo weinig toe; de statusvermelding "todo vendido" is wel bruikbaar als marktsignaal.

### 1.5 Afgevallen na controle (belangrijk om niet nog eens te onderzoeken)

| Partij | Wat het werkelijk is | Waarom niet interessant | Bron · type |
|---|---|---|---|
| **Vivia** (viviahomes.com) | Vivia Homes: beheerder van **huur**woningen in nieuwbouw | Geen koopaanbod, geen Marina Alta | zoekresultaat · 7 |
| **obranueva.com** | Gestora de cooperativas (Madrid, Alicante-stad, Murcia, Valladolid) | Eigen coöperatieprojecten; geen enkel project in de Marina Alta (zelf gelezen: Alicante-stad, Elche) | obranueva.com · 3 |
| **"Nuevaobra"** | Bestaat niet als merk; wat bestaat is obranueva.org / obrasnuevas.com | Geen aantoonbare leesroute of Marina Alta-dekking gevonden | · 7 |
| **Brainsre New Homes** | Geen apart product met die naam gevonden; wél een module *licencias de obra nueva* | Zie §4.1 — dát is de bruikbare route | · 7 |

---

## 2. Grote promotoras: bouwen ze hier werkelijk?

### 2.1 AEDAS Homes — **grootste nieuwbouwpartij in Jávea · NIEUW · prioriteit hoog**

Zelf vastgesteld op aedashomes.com (16-09-2026, · 3):

| Project | Plaats | Status op de site | Vanafprijs / maat |
|---|---|---|---|
| **Unic** | Jávea | *"En comercialización · Obra iniciada"* | *"Precio desde 370.000 €"*, nuttige oppervlakte 64,23 m², 2–3 slaapkamers |
| **Brisas del Arenal** | Jávea | *"Promoción vendida"* | 92 m², 2–4 slaapkamers |

Uit de vakpers (· 1, niet zelf op de AEDAS-site gecontroleerd): Unic telt **223 woningen** en de eerste
fase van 57 woningen wordt opgeleverd; AEDAS zou 16 projecten in de provincie Alicante hebben, met Jávea
en Dénia erbij.

**Route voor ons.** AEDAS koopt grond en verkoopt woningen; dit is geen koopkans (route A/B) maar een
**afnemer van percelen (route D)** en een potentiële opdrachtgever voor Build/Live (route C). Belangrijk
signaal voor de rekenmodellen: AEDAS zet in Jávea nieuwbouwappartementen weg vanaf 370.000 € — dat is een
harde ondergrens voor onze verkoopwaarden in de Arenal-zone.

**Koppeling.** `https://colaboradores-api.aedashomes.com/` bestaat en antwoordt met HTTP 200 en de tekst
*"Bienvenido al API del Portal de Colaboradores de AEDAS"* (· 3, zelf opgehaald). Er is geen openbare
documentatie en geen aanmeldpagina gevonden; toegang loopt kennelijk via een collaborator-overeenkomst
(· 4). In `robots.txt` staat verder `Disallow: /area-privada/` — een besloten deel voor partners (· 3).

**Volgende stap.** Vraag bij AEDAS Homes naar de voorwaarden van het collaborator-programma: provisie,
en of het Portal de Colaboradores een API/feed geeft met beschikbaarheid en prijzen die wij in ons eigen
systeem mogen opslaan.

### 2.2 Taylor Wimpey España — komt Moraira binnen · prioriteit middel

Op de eigen *coming soon*-pagina staat **"Aqua Phase 2 – Moraira, Alicante: 2 and 3-bed apartments.
Communal pool and gardens"**, naast *Luma – Calpe* en *Sora – Denia* (· 1, 16-09-2026). Dat is werkelijke
aanwezigheid in ons werkgebied. Er is **geen makelaars- of partnerpagina** op de site gevonden en geen
feed (· 3/7); wel organiseert het bedrijf bijeenkomsten met *"collaborating agents"* (· 1, persbericht).

### 2.3 Metrovacesa, Neinor, Culmia, TM Grupo — eerlijk antwoord: niet ons gebied

| Partij | Bevinding | Oordeel |
|---|---|---|
| **Metrovacesa** | 14 complexen in de Comunitat; in Alicante alleen Sant Joan d'Alacant en Alicante-stad (· 1, vakpers) | Geen dekking Marina Alta — **niet interessant** |
| **Neinor Homes** | 201 woningen in vier promoties in de Comunitat; geen Marina Alta genoemd (· 1, vakpers) | **Niet interessant** |
| **Culmia** | ca. 100 woningen in twee projecten: Rocafort en **Dénia** (· 1, vakpers) | Aangrenzend, buiten onze drie gemeenten — **laag** |
| **TM Grupo Inmobiliario** | Alicante-groep, >20.000 woningen, zwaartepunt zuidelijke Costa Blanca; **geen bewijs** van projecten in Jávea/Benitachell/Moraira, en geen openbaar "TM Partner"-programma gevonden (· 7) | **Niet interessant zonder nieuw bewijs** |
| **Aelca** | Al in R07: Adeya Jávea I en II, obras iniciadas | Bekend |
| **Amaro Homes / Solvilla** | In twee zoekrondes **geen bedrijf met die naam** aangetroffen dat in de provincie Alicante bouwt (· 7) | Naam mogelijk onjuist — laten vallen tot Jan de bron aanwijst |

---

## 3. Lokale ontwikkelaars en bouwers in Benitachell/Cumbre del Sol en Moraira

### 3.1 VAPF — de facto poortwachter van Cumbre del Sol · prioriteit hoog

In R07 staat VAPF al als partij; wat daar **niet** staat, is de zakelijke koppeling. Zelf vastgesteld
(16-09-2026, · 3): de site verwijst naar een **"Professional Area"** op `extranet.vapf.com`, die bestaat
(HTTP 307 → `https://extranet.vapf.com/es/`) en om inloggegevens vraagt. Aanbod volgens de eigen site
(· 1): villa's in **Jazmines, Lirios Design, Magnolias Design** (Cumbre del Sol), *Elements
Ecoresidences – Airen Collection*, appartementen **Montecala Gardens** (Cumbre del Sol) en **Allure**
(Calpe), plus villa's in Benissa (Raco Galeno) en Altea. Zij verkopen ook **losse percelen** — dat is voor
route B de enige structurele bron van bouwrijpe kavels in Benitachell (· 1, via R07).

VAPF houdt jaarlijkse bijeenkomsten voor samenwerkende makelaars (in 2026 met ruim 120 agenten,
· 1, vakpers) — er is dus een lopend collaboratorkanaal. Provisie en voorwaarden zijn niet openbaar (· 7).
`robots.txt` sluit alleen admin/login af; er is een `sitemap.xml`, maar **geen objectfeed** gevonden (· 3).

**Volgende stap.** Toegang vragen tot het VAPF-extranet als samenwerkende makelaar, en tegelijk vragen of
er een prijslijst/beschikbaarheid in XML of Excel wordt verstrekt en of wij die mogen bewaren.

### 3.2 Lokale bouwer-ontwikkelaars Moraira/Benissa/Benitachell — leads, geen feeds

Gevonden en nog niet in R07 of het register (· 1, alle uit eigen sitebeschrijving of zoekresultaat):

| Partij | Wat | Voor ons |
|---|---|---|
| **Villas Buigues** (villasbuigues.com) | Makelaar én constructora in Moraira; werkt in Moraira, Benissa, Benitachell | Route C/D; kandidaat voor rechtstreekse aanlevering |
| **JOG Promociones** (promocionesjog.es) | Familiebedrijf, >50 jaar; ontwerp en bouw van luxevilla's in Moraira en Benissa | Route C/D |
| **Grupo Moraira** (grupomoraira.es) | Nieuwbouwwoningen **en percelen** in Moraira, Benissa, Benitachell | Route B-lead (percelen); site stond 16-09 op *"System Updating"* (· 3) |
| **Max Villas** (max-villas.eu) | Villabouw in Benissa, Moraira, Altea en Jávea | Route C/D |
| **Inmobiliaria Celenia** (inmobiliariacelenia.com) | Bouw op maat in Moraira, Calpe, Benissa, Jávea, Altea, Dénia | Route C |
| **Costa Privee** (costaprivee.com) | **Geen promotor** maar makelaar gespecialiseerd in nieuwbouw Jávea/Dénia/Moraira/Calpe; Valencia, C/ Ciscar 47 | Route D; mogelijk bron van villa-nieuwbouw |
| **GestaliHome** (gestalihome.com) | Comercializadora gespecialiseerd in nieuwbouw Costa Blanca/Cálida, kantoor Alicante (Plaza Músico Óscar Tordera Iñesta 11); claimt *"approximately 90 % of new development promotions"*; heeft een project in **Teulada** | Route D; interessante partner, **geen feed of provisieprogramma openbaar** (· 7) |

**Oordeel.** Geen van deze partijen levert een feed; het zijn **leads voor rechtstreekse aanlevering**
(register R2-52) en voor Build/Live-omzet. Unieke objecten: **deels** — hun villa's staan meestal óók op
portalen, maar percelen en vroege fasen niet altijd.

---

## 4. Route B: stilgevallen en onafgebouwde projecten

R07 §2.4 concludeerde al dat portalen stilgevallen projecten niet als zodanig adverteren. Dit onderzoek
bevestigt dat en voegt drie routes toe die nog niet in het register staan.

### 4.1 Brainsre — module *licencias de obra nueva* · gemiste route bij bekende partij (R2-19) · middel

Brainsre publiceert per bouwvergunning *"el tipo y el subtipo de propiedad, el número de habitaciones,
los metros cuadrados y el municipio del activo inmobiliario"*, plus promotor, aantal woningen, startdatum
en budget (· 1). Landelijk (14.360+ vergunningaanvragen in 2023 genoemd). Toegang via het webplatform met
proefaccount; **API en tarieven niet vastgesteld** (· 7).

**Waarom relevant voor route B:** een vergunning uit 2021–2023 zonder oplevering is precies het signaal
"stilgevallen". Dit is de enige gevonden bron die vergunning, promotor en gemeente combineert.
Rechten: bij een dataleverancier geldt altijd contract — niets gebruiken zonder schriftelijke licentie.

### 4.2 MIVAU — *Obras en edificación: visados de dirección de obra en certificaciones de fin de obra* · gemiste reeks bij bekende partij (R2-46) · middel

Zelf gelezen op mivau.gob.es (16-09-2026, · 2):

> *"Estadística que resulta de la recopilación de información incluida en los formularios que los
> Aparejadores o Arquitectos Técnicos deben cumplimentar en los Colegios profesionales con ocasión del
> Visado de Encargo de dirección de obra y de la Certificación de fin de obra. Su información hace
> referencia a las modalidades de Obra nueva por tipología, Ampliación y Reforma o restauración de
> edificios."*

Er zijn **maandreeksen** en een nota metodológica. **De geografische fijnheid (provincie of gemeente) is
niet vastgesteld** — het boletín draait op JavaScript en gaf geen leesbare inhoud (· 7). Open data,
kosteloos; uniek object­niveau: **nee**, dit is context (het verschil tussen visados en fin de obra is een
maat voor stilstand in de provincie Alicante).

### 4.3 Tablones van Benitatxell en Teulada — **echte gat in het register** · prioriteit hoog

Het register kent alleen Xàbia (R2-42, R2-69). Zelf vastgesteld, 16-09-2026 (· 3):

- **El Poble Nou de Benitatxell:** `https://benitatxell.sedelectronica.es/board` — live tablón de
  anuncios, met kolommen Documento, Expediente, Procedimiento, Categoría, Fecha de Publicación; ook
  *Perfil de contratante* en *Portal de transparencia*.
- **Teulada:** `https://teuladamoraira.sedelectronica.es/board` — *"Ayuntamiento de Teulada – Tablón de
  anuncios"*. Let op: `teulada.sedelectronica.es` geeft *"Sede Electrónica Indeterminada"* — dat is het
  verkeerde adres.

Hier verschijnen (net als bij Xàbia) caducidad de licencia, órdenes de ejecución, declaraciones de ruina
en PAI-inzageperiodes — de publicaties die R07 als de werkelijke route naar stilgevallen projecten
aanwees. Twee derde van ons werkgebied ontbreekt nu in de monitor.

### 4.4 Statusfilters bij de nieuwbouwaggregators — zwak maar gratis

Zowel Metainmo als EstateNearMe filteren op *"Estado de la obra: Sobre plano / En construcción / Obra
nueva terminada"* (· 3). Een project dat kwartaal na kwartaal *en construcción* blijft, is een kandidaat.
Dit werkt alleen met een abonnement (het handmatig doorlopen van de publieke pagina's valt onder het
kopieerverbod van §1.1).

---

## 5. Publiceren versus lezen — wat is wat

| Bron | Lezen (aanbod van anderen) | Publiceren (ons aanbod) |
|---|---|---|
| Metainmo | **Ja** — XML-download van de databank (betaald tarief) | Ook mogelijk ("Publicar", MLS colaborativa) — voor ons niet het doel |
| Resales-Online New Development MLS | **Ja** — projecten + documenten + feed naar eigen site | Ja, resale-kant |
| EstateNearMe / Inmofind | Handmatig lezen; directory bruikbaar | *"Publicar la cartera"* |
| viviendasnuevas.com | Handmatig | *"Alta de agente"* |
| AEDAS Portal de Colaboradores | **Vermoedelijk ja** (API bestaat; inhoud onbekend) | n.v.t. |
| VAPF extranet | **Vermoedelijk ja** (prijslijsten/beschikbaarheid) | n.v.t. |
| Ontwikkelaarssites lokaal | Handmatig, geen feeds | n.v.t. |

---

## 6. Rechtenoverzicht (kort)

| Bron | Opslaan | Historie | AI-analyse | Tonen aan Jan | Basis |
|---|---|---|---|---|---|
| Metainmo | voorwaardelijk (XML-tarief is bedoeld voor CRM-integratie; algemene clausule verbiedt reproductie zonder schriftelijke toestemming) | ONBEKEND | ONBEKEND | ja, intern | Condiciones generales (Agencias) · 2 |
| Resales-Online New Dev MLS | contract nodig | contract nodig | contract nodig | ja, intern na contract | R2-24-voorwaarden · 2 |
| EstateNearMe | nee zonder afspraak | nee | nee | handmatig kijken mag | geen voorwaarden gevonden · 7 |
| AEDAS collaborator-API | ONBEKEND | ONBEKEND | ONBEKEND | ONBEKEND | geen openbare documentatie · 7 |
| VAPF extranet | ONBEKEND | ONBEKEND | ONBEKEND | ONBEKEND | achter login · 7 |
| Brainsre licencias | contract nodig | contract nodig | contract nodig | na contract | dataleverancier · 4 |
| MIVAU visados/fin de obra | ja (open data) | ja | ja | ja | overheidsstatistiek · 2 |
| Tablones Benitatxell/Teulada | ja (openbaar) | ja | ja | ja | sede electrónica · 2 |

---

## 7. Wat niet lukte (beperkingen, eerlijk vermeld)

- **Metainmo-tarieven per plan**: bedragen laden met JavaScript; alleen registratiekosten (125 €) en
  bijkomende posten (20 €/maand) zichtbaar.
- **Metainmo-promotoralijst Jávea (18 namen)**: JavaScript, niet opgehaald.
- **EstateNearMe**: promotielijsten per gemeente niet bereikbaar op de beproefde URL-patronen (404);
  aviso legal-pagina 404 → exploitant **niet vastgesteld**.
- **MIVAU boletín online** (`apps.fomento.gob.es/BoletinOnline2`): JavaScript, geen leesbare inhoud;
  de methodologische notitie op transportes.gob.es gaf HTTP 403; datos.gob.es-datasetpagina 404.
- **javeahomes.es** (lokale makelaar/constructora/promotora in Jávea): HTTP 500 — niet beoordeeld.
- **grupomoraira.es**: toonde *"System Updating"* — niet beoordeeld.
- **TM Grupo Inmobiliario**: geen partnerprogramma en geen Marina Alta-project gevonden; twee zoekrondes.
- **Amaro Homes** en **Solvilla**: geen bedrijf met die naam gevonden in de provincie Alicante.
- **Villas Guzmán**: niet gevonden; wat er in Moraira/Benissa bestaat zijn Villas Buigues, JOG, Max Villas.
- **Blue Sky**, **Living Inversiones**, **Prygesa**, **Ten Brinke**: R07 heeft ze al; er is in deze ronde
  **geen** feed, partnerprogramma of prijslijstroute bij hen gevonden (· 7).

---

## 8. Aanbevolen volgorde

1. **Metainmo** — offerte + rechtenvragen (hoog, kost geld, levert 35 promoties in ons gebied).
2. **Tablones Benitatxell en Teulada** — direct toevoegen aan de monitor; gratis, openbaar, en het dicht
   een gat dat twee van onze drie gemeenten betreft (hoog, geen kosten).
3. **Resales-Online** — New Development MLS meenemen in het lopende gesprek (hoog).
4. **AEDAS Homes** en **VAPF** — collaboratortoegang aanvragen (hoog voor route C/D, geen kosten).
5. **Brainsre licencias** — proefaccount en prijsindicatie (middel).
6. **Lokale bouwers Moraira/Benitachell** — opnemen in de partnerlijst R2-52 (middel).
7. **MIVAU visados/fin de obra** — als contextreeks toevoegen (laag, gratis).

### ⏸️ ACTIE VOOR JAN

1. **Metainmo** — akkoord nodig voor een betaald abonnement (registratie 125 € + maandtarief, bedrag nog
   onbekend). Wil je dat ik eerst een offerte opvraag zonder iets aan te gaan?
2. **AEDAS Homes en VAPF** — beide willen een makelaarsrelatie voordat ze toegang geven. Mag ik een
   conceptbericht klaarzetten (het gaat niet de deur uit zonder jouw "ja")?
3. **Resales-Online** — daar loopt al een spoor; zeg je akkoord om er de nieuwbouw-MLS bij te vragen?

---

## 9. Bronnen (URL · controledatum 16-09-2026 · bewijstype)

- https://spain.metainmo.com/ · 1
- https://spain.metainmo.com/page/promo · 1
- https://spain.metainmo.com/page/price · 1
- https://spain.metainmo.com/page/terminos · 2
- https://spain.metainmo.com/page/aviso-legal · 2
- https://spain.metainmo.com/alicante/javeaxabia/promociones · 3
- https://spain.metainmo.com/alicante/benitachell/promociones · 3
- https://spain.metainmo.com/alicante/moraira/promociones · 3
- https://spain.metainmo.com/alicante/teulada/promociones · 3
- https://spain.metainmo.com/alicante/javeaxabia/companies/promotoras · 1
- https://blog.resales-online.com/en/alicante-murcia-accurate-new-development-mls · 1
- https://blog.resales-online.com/en/new-development-mls-costa-blanca-resales-online · 1
- https://spain.inmofind.com/… → 302 → https://spain.estatenearme.com/… · 3
- https://spain.estatenearme.com/alicante/companies/promotoras · 1
- https://spain.estatenearme.com/ · 3
- https://viviendasnuevas.com/alicante/la-cumbre-del-sol/promociones/ · 1
- https://www.obranueva.com/ · 3
- https://www.aedashomes.com/pisos-en-venta-en-javea-obra-nueva-unic · 3
- https://www.aedashomes.com/pisos-en-venta-en-javea-obra-nueva-brisas-del-arenal · 3
- https://www.aedashomes.com/robots.txt · 3
- https://colaboradores-api.aedashomes.com/ · 3
- https://www.aedashomes.com/prensa/entrega-unic-javea (via zoekresultaat) · 1
- https://www.vapf.com/en/real-estate-developer/services · 1
- https://extranet.vapf.com/ · 3
- https://www.vapf.com/robots.txt en /sitemap.xml · 3
- https://taylorwimpeyspain.com/property/coming-soon-costa-blanca/ · 1
- https://taylorwimpeyspain.com/blog/taylor-wimpey-espana-commits-e32m-to-costa-blanca-identifying-top-areas-and-trends-for-2026/ · 1
- https://www.costaprivee.com/en/new-build-property-developer-on-the-costa-blanca-javea-denia-moraira-calpe/ · 1
- https://gestalihome.com/en/about-us · 1
- https://www.villasbuigues.com/ · 1 (zoekresultaat)
- https://promocionesjog.es/en/ · 1 (zoekresultaat)
- https://www.max-villas.eu/en/ · 1 (zoekresultaat)
- https://www.grupomoraira.es/ · 3 (site in onderhoud)
- https://brainsre.news/licencias-obra-nueva-brainsre-inmobiliario/ · 1
- https://www.mivau.gob.es/informacion-para-el-ciudadano/informacion-estadistica/construccion/obras-en-edificacion-visados-de-direccion-de-obra-de-los-colegios-de-arquitectos-tecnicos · 2
- https://benitatxell.sedelectronica.es/board · 3
- https://teuladamoraira.sedelectronica.es/board · 3
- https://viviahomes.com/ (afgevallen) · 7
- https://alicanteplaza.es/… "Aedas Homes y Metrovacesa, los 'reyes' de la obra nueva en la Comunitat" · 1

# R07 — Netwerken, ontwikkelaars, percelenspecialisten en vroege dealflow in de Marina Alta

> **NA TEGENSPRAAK (15-09-2026).** Dit rapport is door een tweede agent gecontroleerd; zie `R07-netwerken-ontwikkelaars-dealflow.verificatie.md`. Betrouwbaarheid volgens die controle: hoog.
> Weerlegd en in de eindstukken gecorrigeerd: R07-07; R07-19; R07-20. Gebruik voor die punten de gecorrigeerde tekst in het verificatiebestand, niet de tekst hieronder.


**Project:** TREE Deal Hunter, fase A · **Stroom:** R07 · **Controledatum:** 14-09-2026
**Relevante masterprompt-secties:** 5 (bewijstypen), 7 (bronnenregister), 9 (lokale makelaars en eigen dealflow), 26 (CRM, opvolging, geen ongevraagde massabenadering)

Bewijstypen (masterprompt §5): **1** door aanbieder vermeld · **2** in officiële bron aangetroffen · **3** door ons rechtstreeks vastgesteld · **4** AI-inferentie · **5** berekening op benoemde aannames · **6** door bevoegde professional bevestigd · **7** onbekend of tegenstrijdig.

## Samenvatting in tien regels

1. In de Comunitat Valenciana is bemiddeling in vastgoed sinds 16-10-2022 gebonden aan inschrijving in het **RAICV** (Decreto 98/2022): openbaar, gratis, verplicht; eisen zijn opleiding of 200 uur cursus, een kantoor, een borg van 60.000 € per vestiging en een beroepsaansprakelijkheidsverzekering van 600.000 € per schadegeval. Elke partner die wij inschakelen moet een RAICV-nummer hebben; of TREE Properties zelf is ingeschreven is niet gecontroleerd.
2. De relevante beroepsorganisaties zijn het **COAPI Alicante** (met de gedeelde bolsa APIRed, alleen voor colegiados), **ASICVAL** (400+ kantoren, "exclusiva compartida") en twee lokale MLS-verenigingen: **MLS Dénia** (opgericht 30-01-2014, 20 kantoren) en **MLS 03724 Teulada-Moraira**. Geen van deze bronnen zegt iets over het delen van aanbod vóór publicatie; toegang tot de gedeelde portefeuille is alleen voor leden.
3. In Jávea zelf is geen eigen makelaarsvereniging of MLS gevonden. De gemeente publiceert wel een lijst van 39 kantoren en promotoren op xabia.org, met adres en website: de basis voor het makelaarsregister uit §9.
4. Op Idealista staat hetzelfde perceel (1.570 m², 505.000 €, Montgó/Garroferal) bij zeven verschillende advertenties en een ander (889 m², 340.000 €) bij drie. Open, niet-exclusieve verkoop is in Jávea de norm; dat maakt rechtstreekse samenwerking met kantoren kansrijk, maar dedupliceren onmisbaar.
5. Actieve ontwikkelaars met bevestigde projecten in Jávea: Ten Brinke España (Marina Bay I/II/Sunset, 30 woningen in ontwerpfase op een perceel van 2.000 m² dat zij in 2024 kochten), Prygesa (Jávea Garden, 72 woningen, licentie verleend), Aelca (Adeya I/II, 25 en 10 woningen, in aanbouw), Living Inversiones (Living Jávea, 20 woningen, met sloop van een bestaand chalet), Promociones Jávea S.L. (sinds 1984, 23 percelen Cumbres del Tosalet), Miralbo Urbana S.L. (villabouwer) en VAPF (Benissa, Cumbre del Sol in Benitatxell, verkoopt losse percelen).
6. Stilgevallen projecten zijn op portalen niet zichtbaar gemaakt: de 66 obra-nueva-chalets op Idealista zijn allemaal van professionals en twee zijn "en construcción"; geen enkele advertentie noemt "obra parada". De route naar stilgevallen projecten loopt via gemeentelijke publicaties (BOP, sede electrónica) en via architecten, niet via portalen.
7. Percelen "met project en licentie" worden in Jávea door makelaars verkocht, niet door architecten: Luxia Properties (1.323 m², 350.000 €), InmoVillas Jávea (1.123 m², 420.000 €), Six Seconds Properties (192 m² in de haven met licentie voor 6 woningen, 650.000 €), MG Villas en Rimontgó. Op Idealista matchen 40 percelen de tekst "proyecto y licencia" (35 professioneel, 5 particulier; prijzen 150.000 – 2.000.000 €, mediaan 505.000 €).
8. Architectenbureaus die Jávea bedienen (Velló Monfort, Arquitectos Jávea, Studio Base, Innov-arq, QB Arquitectos, GV Arquitecnia) adverteren geen percelenbemiddeling. Het CTAA heeft een "bolsa de servicios al ciudadano" (achter inlog); het COAT Alicante was via onze tooling niet bereikbaar.
9. Particuliere kanalen (Milanuncios, Wallapop, Facebook) verbieden alle drie geautomatiseerde extractie en ongevraagde berichten in hun voorwaarden; de LSSI (art. 21) verbiedt ongevraagde elektronische reclame zonder uitdrukkelijke toestemming en de AEPD houdt daar strikt aan vast. Rechtmatig blijft: handmatig lezen, reageren op een concrete advertentie, een eigen inbound-kanaal en lidmaatschap van groepen volgens de groepsregels.
10. Sectie 5 van dit rapport bevat het zoekprofiel (drie categorieën, prijsklassen als werkhypothese), een aanleverformulier met 24 velden, een opvolgprocedure (ontvangst binnen 1 werkdag, eerste oordeel binnen 5, besluit binnen 10) en conceptberichten in het Spaans en Engels. Alles is CONCEPT; er wordt niets verzonden zonder akkoord van Jan.

## 0. Werkwijze en beperkingen

- Bronnen: officiële sites (gva.es, sede.gva.es, habitatge.gva.es, boe.es, aepd.es, xabia.org, ajxabia.com, xabia.sedelectronica.es), sites van verenigingen en colegios, eigen sites van ontwikkelaars en makelaars, gebruiksvoorwaarden van platforms, de officiële Idealista-assistent (MCP) en het lokale bestand `~/tree-es/properties/leadgen/docs/marktdata-bronnen.md`.
- Alle webcontroles zijn uitgevoerd op 14-09-2026. Passages uit bronnen staan in de oorspronkelijke taal tussen aanhalingstekens.
- Het WebSearch-budget van deze sessie raakte op na de laatste zoekronde; de resterende controles zijn met WebFetch en de Idealista-assistent gedaan. Wat daardoor niet meer kon, staat in sectie 8.
- Geen enkele lokale dienst is aangeraakt; er is niets geïnstalleerd; er zijn geen sleutels of tokens overgenomen.
- Persoonsgegevens van particulieren zijn weggelaten. Bedrijfsnamen en zakelijke contactgegevens van makelaars, ontwikkelaars en instanties staan er wel in.

## 1. Beroepsverenigingen en samenwerkingsnetwerken (opdracht a)

### 1.1 Het verplichte register: RAICV (Decreto 98/2022)

Het Registro de Agentes de Intermediación Inmobiliaria de la Comunitat Valenciana is het fundament onder elke samenwerking: wie in de regio bemiddelt, moet erin staan, en wij kunnen dat zelf controleren.

| Onderwerp | Wat de bron zegt | Bron · bewijstype |
|---|---|---|
| Karakter | Art. 4.1: "El Registro de Agentes de Intermediación Inmobiliaria de la Comunitat Valenciana es de titularidad pública, y naturaleza administrativa, gratuito y de carácter obligatorio." | Decreto 98/2022 via Iberley · 2 |
| Wie valt eronder | Art. 2.1: wie "se dedica de forma regular y remunerada, dentro del territorio de la Comunitat Valenciana, a prestar servicios de mediación, asesoramiento y gestión en operaciones inmobiliarias en relación con operaciones de compraventa, alquiler, permuta o cesión de bienes inmuebles." | Idem · 2 |
| Opleiding | Officiële API-titel, óf universitaire graad in "Ciencias Sociales y Jurídicas, Ingeniería o Arquitectura", óf "certificados de asistencia ... a cursos de formación académica de, al menos, 200 horas lectivas en materia inmobiliaria". | sede.gva.es, id_proc 22848 · 2 |
| Kantoor | Establecimiento abierto al público verplicht, tenzij de dienst "exclusivamente a distancia por vía electrónica o telemática" is; dan een "dirección física en el territorio de la Comunitat Valenciana". | Idem · 2 |
| Borg (aval/caución) | "60.000 euros por establecimiento abierto al público y año"; bij uitsluitend telematische dienstverlening "300.000 euros por agente y año de servicio". | Idem · 2 |
| Aansprakelijkheid (RC) | "600.000 euros por siniestro y año de seguro con un sublímite de 150.000 euros"; telematisch 1.000.000 € per schadegeval. | Idem · 2 |
| Nota de encargo | Art. 3: in de opdrachtbevestiging moeten staan "todos los datos referentes a su identificación profesional, ubicación, nombre de la entidad aseguradora o financiera, número de referencia de la garantía, y número de inscripción en el registro". | Iberley · 2 |
| Sancties | Art. 5.f: de bevoegde dirección general legt sancties op "por el incumplimiento de las normas relativas al Registro, de conformidad con lo que se disponga en la legislación vigente." | Iberley · 2 |
| Inwerkingtreding | Disposición final segunda: twee maanden na publicatie in het DOGV; publicatie DOGV nr. 9405 van 16-08-2022; ASICVAL: "entró en vigor el 16 de octubre de 2022". Overgangstermijn één jaar (DT 1ª). | Iberley, ASICVAL · 2 |
| Openbare raadpleging | habitatge.gva.es linkt naar "Registro Público de Agentes de Intermediación Inmobiliaria" (sforms.gva.es, formulier 62953). Het formulier laadt via JavaScript; de zoekvelden konden niet worden gelezen. Handmatig raadplegen kan. | habitatge.gva.es · 2/7 |
| Wettelijke grondslag | De GVA-procedurepagina noemt Decreto 98/2022 en Ley 2/2017. In de geconsolideerde BOE-tekst van Ley 2/2017 (stand 27-02-2023) is via onze fetch geen artikel over dit register gevonden. **[te verifiëren]** | sede.gva.es, boe.es · 7 |
| Kosten | Niet vermeld op de procedurepagina. ONBEKEND. | · 7 |

**Betekenis voor TREE.** Een partner zonder RAICV-nummer bemiddelt in strijd met het decreet; wij nemen het nummer daarom op als verplicht veld in het aanleverformulier (sectie 5.2) en controleren het in het openbare register. Of TREE Properties zelf een RAICV-inschrijving heeft, is in dit onderzoek niet vastgesteld (⏸️ ACTIE VOOR JAN, sectie 7). Voorbeelden uit de markt: COSTA HOUSES Luxury Villas vermeldt "RAICV 1077" en Select Villas of Moraira "RAICV 1311" (zoekresultaat, niet zelf op hun sites gecontroleerd · bewijstype 1/7).

### 1.2 COAPI Alicante, APIAL en de bolsa APIRed

| Onderwerp | Bevinding | Bron · bewijstype |
|---|---|---|
| Wat | Colegio Oficial de Agentes de la Propiedad Inmobiliaria de Alicante. Adres C/ Arzobispo Loaces 5, 03003 Alicante; tel. 965 98 41 25; coapi@apialicante.com. | apialicante.com · 1 |
| Colegiación | Eisen: meerderjarig; "hold a degree, graduate, diploma, engineer, architect, technical architect, technical engineer or the official title of Real Estate Agent"; geen strafblad dat de uitoefening belet. Aanvraag aan de president plus administratiekosten en contributie; bedragen niet gepubliceerd. | apialicante.com/en/the-api-profession/requirements · 1 |
| Asociados | Naast colegiados kent het colegio "asociados" van APIAL (Asociación de Profesionales Inmobiliarios de Alicante); eisen voor asociados niet gespecificeerd. | apialicante.com, artikel 09-09-2022 · 1 |
| RAICV-dienst | Het colegio regelt de collectieve inschrijving in het RAICV: "realizará los trámites para inscribirlos de forma colectiva", biedt "la formación requerida en el Decreto de 200 horas", "Seguro de Responsabilidad Civil incluido en la cuota mensual" en "Seguro de Caución con un coste muy ajustado". | apialicante.com/registro-api-coapi-alicante · 1 |
| Gedeelde bolsa | APIRed-Bolsa Inmobiliaria, gestart in 2018 met circa 1.000 objecten: "una aplicación denominada APIRed-Bolsa Inmobiliaria en la que los Agentes de la Propiedad Inmobiliaria pueden introducir las viviendas que gestionan". Toegang voor "los Agentes de la Propiedad Inmobiliaria colegiados de toda la provincia". Openbare zoekfunctie op apired.com; ledendeel achter "Área Privada". | inmodiario 19-04-2018; apired.com · 1 |
| Delen vóór publicatie | Nergens vermeld. | · 7 |

**Inschatting (bewijstype 4).** APIRed is een gedeelde etalage van colegiados, geen pre-market kanaal. Lidmaatschap heeft voor TREE alleen zin als de eigen makelaar aan de titeleis voldoet; de bolsa zelf is openbaar doorzoekbaar en levert dus geen informatievoorsprong.

### 1.3 ASICVAL

| Onderwerp | Bevinding | Bron · bewijstype |
|---|---|---|
| Wat | "Asociación de Inmobiliarias de la Comunitat Valenciana"; actief in Castellón, Valencia en Alicante. Cijfers op de site: 400+ kantoren, 430 verkooppunten, +1.200 professionals, "1.317 inmuebles en exclusiva" (peildatum van die cijfers niet vermeld). | asicval.es · 1 |
| Werkwijze | "Comercializamos en régimen de exclusiva compartida. Cuando comprometes tu piso con una agencia, todos trabajamos para venderlo." | asicval.es · 1 |
| Lidmaatschap | Knop "ASÓCIATE"; voorwaarden en contributie niet op de site. Leden kunnen "integrarse en las pólizas colectivas tanto de caución como de responsabilidad civil a un coste anual reducido". | asicval.es · 1 |
| Delen vóór publicatie | Niet vermeld. | · 7 |

### 1.4 MLS Dénia en MLS 03724 Teulada-Moraira

| Onderwerp | MLS Dénia | MLS 03724 Teulada-Moraira |
|---|---|---|
| Rechtsvorm | Vereniging zonder winstoogmerk, opgericht 30-01-2014, CIF G-54768957 (mlsdenia.com/en/about-us · 1) | "MLS Teulada-Moraira Real Estate Association (MLS: 03724)"; oprichtingsdatum niet op de site (mls03724.com · 1) |
| Omvang | "20 agencies" (about-us); homepage "Más de 20 Agencias"; partnerpagina bij Dénia Casas "more than 25 collaborating agencies" → tegenstrijdig (· 7) | About-us: "four founding agencies"; persbericht (zoekresultaat, niet zelf opgehaald): 16 kantoren → tegenstrijdig (· 7) |
| Werkgebied | Dénia en omliggende gemeenten (El Verger, Els Poblets, Pedreguer, Pego); de site heeft een zoekpagina "Jávea" (· 1) | Teulada-Moraira; het persbericht noemt ook Benissa, Benitachell, Calpe, Dénia, Jávea (· 7) |
| Werkwijze | "a system based on collaboration among real estate agencies by sharing available properties in a 'real estate pool' among all associated agencies"; contract "Multi-exclusive or Shared sale, which is a Premium service" (· 1) | "Information on properties that have been captured as a shared exclusive is shared"; "strict code of ethics and work procedures" (· 1) |
| Toetreding | "join upon request and approval, provided you meet the association's requirements regarding qualifications, training, and experience" (· 1) | Niet uitgewerkt; "we trust that more agencies will join us" (· 1) |
| Commissieverdeling | Niet gepubliceerd (· 7) | Niet gepubliceerd (· 7) |
| Ledenlijst | Niet op de site (· 7) | Niet op de site (· 7) |
| Contact | info@mlsdenia.com; 03724 Dénia | Ctra. Moraira a Calpe 27, 03724 Teulada; +34 965 058 105; info@mls03724.com |

**Inschatting (bewijstype 4).** Beide MLS-verenigingen delen exclusief aanbod alleen onder leden; ze zijn de enige structuren in de Marina Alta waar aanbod circuleert vóórdat elk lid het zelf publiceert. Toetreden vereist een RAICV-inschrijving en acceptatie door de leden. Voor Jávea is er géén eigen MLS gevonden; MLS Dénia heeft wel een Jávea-zoekpagina, wat wijst op leden met aanbod daar.

### 1.5 Ketens en netwerken met vestiging in Jávea

| Netwerk | Bevinding | Bron · bewijstype |
|---|---|---|
| Engel & Völkers | Gemeentelijke lijst: Av. de la Libertad 47, tel. 965 76 95 58. De E&V-site noemt voor Xàbia een kantoor "Valencia Jávea" op Avenida del Mediterráneo 238, 03738. Twee adressen → mogelijk verhuisd; **[te verifiëren]**. E&V meldt "484+" bemiddelde objecten in het gebied sinds 2022; niets over delen met derden. | xabia.org; engelvoelkers.com · 2/1/7 |
| RE/MAX Inmomas IV | Ctra. Cabo la Nao 124, tel. 966 66 56 51, inmomas.remax.es. | xabia.org · 2 |
| iad España | "12 real estate agents in Jávea or nearby" (03730). Registratienummers stonden niet op de opgehaalde pagina; een zoekresultaat noemde "RAICV 2218 · API A12191" (niet bevestigd · 7). | iadespana.es · 1 |

Deze netwerken delen aanbod intern (franchise/agentnetwerk); of zij aanbod met een buyer-side partner buiten het netwerk delen, is niet uit bronnen af te leiden (· 7).

### 1.6 Gemeentelijke lijst van kantoren en promotoren in Xàbia

Het Ayuntamiento de Xàbia publiceert op zijn toeristisch portaal een lijst "Inmobiliarias y promotores" (bewijstype 2). De opgehaalde tabel telde 39 bedrijven; de pagina zelf noemt volgens onze fetch 45 — het verschil is niet verklaard (· 7). De lijst maakt geen onderscheid tussen makelaars en promotoren. Dit is de startvoorraad voor het makelaarsregister uit masterprompt §9.

| Bedrijf | Adres | Website |
|---|---|---|
| Aguila Rent a Villa | Av. de Palmela 56 | aguilarent.com |
| Alensol S.L. | Ctra. de la Granadella 23 | alensol-javea.com |
| Antonio Roselló Luxury Living | — | arluxuryliving.com |
| A.V. Costamar S.L. | Av. Jaime I 15 | avcostamar.com |
| Bartolome Bas | Av. Libertad 2 | — |
| Cala Blanca Villas S.L. | Av. de la Fontana 2 | calablanca.com |
| Casitas Ibérica | Ctra. Jesús Pobre 164 | casitasiberica.com |
| Crown Properties S.L. | Av. de París 2 | crown-property.com |
| Deluxe Homes Javea | — | deluxehomesjavea.com |
| Engel & Völkers | Av. de la Libertad 47 | engelvoelkers.com |
| EuroJavea | C/ Presidente Adolfo Suárez 9 | eurojavea.com |
| FPI Inmobiliaria | Av. Rei Jaume I 12 | fpi-inmobiliaria.com |
| Giuliano-Villas.com | Av. de la Libertad 34 | giuliano-villas.com |
| Houses Investment Holdings | Av. de la Libertad, Bl. 7F | javeahouses.com |
| Indarte | Carrer Thiviers 2 | indarteinmobiliaria.com |
| Inmo Villas Jávea | Av. del Mediterráneo 41 | inmovillasjavea.com |
| Jávea Continental | Av. Jaime I 11 B | javeacontinental.com |
| Javea Homes | Av. de la Fontana 2 | javeahomes.es |
| Javea Immo | Av. de Estrasburgo | javeaimmo.com |
| Javea Home Finders | Av. Libertad 19 | javeahomefinders.com |
| L'Aurora Villas Selection | Ronda Norte 6 | lauroravillas.com |
| Llidomar Properties | Av. Príncipe de Asturias 13 | llidomarjavea.com |
| Maravilla Costa S.L. | Av. del Pla 124 | maravilla-costa.es |
| MG Villas | Av. de la Libertad 11 | mgvillas.com |
| Moragues Pons Inmobiliaria | Av. Ausias March 13 | moraguespons.com |
| New Life Property Spain | Av. de Lepanto 7 | newlifepropertyspain.com |
| Paradise Property Solutions | Av. de la Libertad, Bl. 5, 47 C | paradiserealestate.es |
| Promociones Jávea | Av. del Pla 124 | promocionesjavea.com |
| Proxabia | Av. La Fontana 2 | proxabia.com |
| Remax Inmomas IV | Ctra. Cabo la Nao 124 | inmomas.remax.es |
| Rimontgó | Av. de Lepanto 1 | rimontgo.es |
| Terramar Costablanca S.L. | Pza. President Adolfo Suárez 18 | terramar.es |
| ValuVillas | Ctra. Cabo la Nao 141 | valuvillas.com |
| Vicens Ash Properties | Av. del Pla 137 | vicensashjavea.es |
| Villa Lingo | Av. de la Fontana 18C | villalingo.com |
| Villalux S.L. | C.C. La Nao 5 | villalux.com |
| Villas Plots.com | Av. de la Libertad 19 | villas-plots.com |
| Xàbiacasa | C/ Sant Agustí | xabiacasa.com |
| Xabiga S.L. | C/ Cristo del Mar 33 | xabiga.net |

Niet op de gemeentelijke lijst, maar in dit onderzoek wel als aanbieder in Jávea gezien: Luxia Properties (Av. dels Furs 27, local 4, 03730 Xàbia), Six Seconds Properties SL, COSTA HOUSES Luxury Villas SL, Lucas Fox, Javea Estates, Euroholding Dénia Inmobiliaria S.L. (ehd.es), Dénia Casas, Grupo García (· 1, elk via eigen site of zoekresultaat).

### 1.7 Delen makelaars aanbod vóór publicatie? Wat de markt laat zien

- Geen enkele onderzochte vereniging of keten publiceert een regel over pre-market delen; alleen de twee MLS-verenigingen delen exclusief aanbod onder leden (· 1).
- Op Idealista (assistent, 14-09-2026, terrenos in Jávea met tekst "proyecto y licencia") staan 40 advertenties; daarvan zijn er zeven met exact 1.570 m² en 505.000 € met coördinaten binnen enkele honderden meters van elkaar (codes 112280961, 112386422, 112297090, 112297374, 112447297, 112311948, 112278145), drie met 889 m² en 340.000 € en drie met 1.570 m² en 750.000 € (· 3). Vier van de zeven beschrijvingen zijn woordelijk gelijk ("Parcela edificable con licencia de obras aprobada y proyecto de villa en ubicación privilegiada en Montgó ¿Sueña con construir su propia villa ...") (· 3).
- Gevolgtrekking (· 4): verkopers in Jávea geven hetzelfde object aan meerdere kantoren; exclusiviteit is de uitzondering. Voor TREE betekent dat: (1) een buyer-side samenwerking is voor kantoren aantrekkelijk, want zij concurreren om dezelfde objecten; (2) elke gedeelde tip moet direct op duplicaten worden gecontroleerd (coördinaten + oppervlakte + prijs, zoals in `marktdata-bronnen.md` beschreven); (3) een partner die iets aanlevert heeft zelden een mandaat — masterprompt §9: geen exclusiviteit of commissierecht veronderstellen zonder bevestiging.

## 2. Ontwikkelaars, promotoras en bouwbedrijven met Jávea-projecten (opdracht b)

### 2.1 Bevestigde partijen

| Partij | Wat wij zagen | Voor TREE relevant | Bron · bewijstype |
|---|---|---|---|
| **Ten Brinke España** (vestiging Madrid) | Bericht 18-07-2024: "adquiere una parcela de 2.000 m2" aan Calle Haya voor Residencial Marina Bay Sunset, 30 woningen met "garaje, trastero y amplias terrazas", "fase de diseño de la promoción"; derde meergezinsproject in Jávea. Zoekresultaat (niet zelf opgehaald): Marina Bay I 27 woningen (uitverkocht), Marina Bay II 37 woningen. | Koopt actief percelen in Jávea voor appartementen; kandidaat-afnemer voor grotere solares die wij tegenkomen (route D) en mogelijke afnemer van keukens/sanitair (route C). | tenbrinke.com · 1 |
| **Prygesa** (Planificación Residencial y Gestión S.A.U., Madrid; kantoor Valencia C/ Colón 60) | Jávea Garden, Calle Historiador Palau 23: 72 woningen, "Licencia de obra concedida", "En comercialización", vanaf 214.000 € + IVA; tel. 677 96 48 18. | Grote nieuwbouw in het centrum; partij die grond in het centrum zoekt. | prygesa.es · 1; lamarina.eldiario.es 16-04-2026 · 1 |
| **Aelca** (Valencia, C/ Finlandia 21) | Adeya Jávea: 25 woningen, Calle Cannes/Ctra. Cabo la Nao, "Obras iniciadas", vanaf 411.000 € + IVA. Adeya Jávea II: 10 woningen, "Obras iniciadas", vanaf 377.000 € + IVA; tel. +34 965 271 453. | Idem; Arenal-zone. | aelca.es · 1 |
| **Living Inversiones Profesionales Inmobiliarios** | Living Jávea: "20 exclusive homes", Av. de Palmela / C/ Tenista David Ferrer, fase "Marketing", 325.000 – 650.000 €, 11 van 20 beschikbaar. Idealista-vermelding en lamarina noemen 22 woningen en "demolición de chalé incluida" → aantal tegenstrijdig (· 7). | Concreet voorbeeld van sloop-herbouw van een chalet naar appartementen in Jávea; de partij kent dat traject. | livinginversiones.com · 1; lamarina · 1 |
| **Promociones Jávea S.L.** (Av. del Pla 124, local 15; tel. 965 79 27 69) | "se constituyó en 1984 como empresa inmobiliaria"; eigen promoties; diensten "conservación, administración, alquiler y reventa", project management, beleggingsprojecten. Projecten: Cumbres del Tosalet (urbanisatie met 23 percelen en villamodellen), Villas Cumbres del Tosalet, Golden Ray (bij Playa del Arenal), Beach Trade Center (kantoren). | Lokale promotor met eigen percelenvoorraad; potentiële bron én afnemer. | promocionesjavea.com · 1 |
| **Miralbo Urbana S.L.** (Av. de la Libertad 18 bajo F; tel. 965 036 330; sales@miralbo.com) | "especialistas desde más de 10 años en Arquitectura, Promoción, Diseño y Construcción de Villas de Lujo"; turnkey-bouw, verkoop van eigen villa's, "reformas integrales". Villa's Elysia/Elide/Aurea in Monte Olimpo op Idealista (zoekresultaat). Zocht via LinkedIn een aparejador (zoekresultaat). | Concurrent op villabouw én kandidaat-partner voor percelen die zij niet zelf bebouwen; koopt zelf grond (afgeleid uit "promoción" · 4). | miralbo.com · 1 |
| **VAPF** (Benissa, Avda. País Valencià 22; tel. +34 965 734 017) | "a leading luxury construction company on the Costa Blanca since 1963"; Cumbre del Sol ligt in Poble Nou de Benitatxell "between the towns of Jávea and Moraira"; verkoopt losse percelen ("plots for sale in Magnolias Design"). | Grootste percelenverkoper direct naast Jávea; relevant voor route B als benchmark en als bron van bouwrijpe kavels. | vapf.com · 1 |

### 2.2 Projecten waarvan de promotor niet is vastgesteld

| Project | Wat bekend is | Bron · bewijstype |
|---|---|---|
| Blooming Village | 20 appartementen (2–3 slaapkamers) + 7 adosados; 458.000 – 735.000 €; oplevering Q1 2028 (lamarina). Verkoop via Euroholding Dénia Inmobiliaria S.L. (ehd.es); promotor niet genoemd. | lamarina · 1; ehd.es · 1; promotor · 7 |
| Lemon Residence | 9 appartementen van 3 slaapkamers, 448.000 €, gereed eind 2026. | lamarina · 1; promotor · 7 |
| Villas Aires de Jávea (3 villa's), Villa Pura Vida (Balcón al Mar), Residencial Nusa Dua (9 woningen), Marina XI (14 woningen) | Alleen uit zoekresultaten van portalen; promotor onbekend. | yaencontre/portaalsnippets · 7 |

### 2.3 Brancheorganisatie van promotoren: PROVIA

"Asociación de Promotores Inmobiliarios de la Provincia de Alicante"; Edificio Rex, C/ Reyes Católicos 31 4ºA, 03003 Alicante; tel. 965 227 648 / 965 126 309. Diensten: advies, netwerkactiviteiten, observatorio, innovatiecommissies, convenios. Geen openbare ledenlijst; de pagina /asociados/ bestaat niet (404). PROVIA bezocht in 2022 Cumbre del Sol van VAPF (zoekresultaat). (provia.es · 1; ledenlijst · 7)

### 2.4 Stilgevallen projecten: wat zichtbaar is en wat niet

- **Portalen.** Idealista-assistent, "casa en construcción sin terminar o proyecto paralizado en Jávea", type chalet: 66 resultaten, 20 opgehaald, alle 20 van professionals en alle 20 gemarkeerd als nieuwbouw. Twee beschrijvingen noemen "en construcción" (Villa Azure, La Corona, 3.950.000 €, 402 m²; villa La Granadella, 4.500.000 €). Geen enkele advertentie gebruikt "paralizado", "sin terminar" of "obra parada" (· 3). Gevolgtrekking (· 4): stilgevallen projecten worden niet als zodanig geadverteerd; de zoekterm levert lopende nieuwbouw op.
- **Nieuws.** lamarina.eldiario.es (16-04-2026) beschrijft juist een bouwgolf ("complejos de lujo se alzan a velocidad de vértigo") en noemt als stilstand alleen de schooluitbreiding Trenc d'Alba ("lleva cuatro años paralizada"). xabiaaldia meldde eerder een onafgebouwd gebouw aan Avenida del Plà (zoekresultaat; artikel niet opgehaald · 7).
- **Gemeente.** Volume: in 2022 "240 solicitudes para obras mayores" (2019: 241; 2020: 179; 2021: 196), 936 obras menores en 105 expedientes de infracción urbanística (persbericht gemeente via xabiaaldia 13-01-2023 · 2). Vergunningen worden niet als lijst gepubliceerd: de pagina van de Junta de Gobierno Local bevat geen acuerdos of licenties; het tablón de anuncios (xabia.sedelectronica.es, openbaar) toonde op 14-09-2026 alleen personeels-, belasting- en begrotingsitems (· 3). Stedenbouwkundige instrumenten gaan wél via het Boletín Oficial de la Provincia en het tablón: voorbeeld PAI Adsubia Cap Martí 5, 6.892 m², 45 dagen ter inzage (xabiaaldia 08-03-2022 · 2).
- **Route (· 4).** Stilgevallen projecten zijn alleen te vinden via (1) architecten en aparejadores die de dirección de obra hadden, (2) BOP-publicaties over caducidad de licencia, órdenes de ejecución en declaraciones de ruina, (3) veilingen en insolventies (stroom veilingen), en (4) fysiek: bouwborden en stilstaande structuren. Dit rapport bewijst dat de portaalroute daarvoor niet werkt.

## 3. Architecten en aparejadores in en om Jávea (opdracht c)

### 3.1 Colegios

| Colegio | Bevinding | Bron · bewijstype |
|---|---|---|
| CTAA — Colegio Territorial de Arquitectos de Alicante (Plaza Gabriel Miró 2, 03001 Alicante; 965 21 84 00; colegio@ctaa.net) | Heeft een "Bolsa de servicios al ciudadano": "¡Encuentra al arquitecto que necesitas con un solo clic! El CTAA te ofrece una herramienta segura para encontrar arquitectos colegiados por especialidad y ubicación". De pagina zelf toont alleen "Inicia sesión para acceder a la bolsa de trabajo" — dus registratie vereist. Nieuwsbericht 04-09-2026: "Nueva bolsa de colaboración profesional entre arquitectos". | ctaa.net · 1 |
| COAT/COAATIE Alicante — Colegio Oficial de Aparejadores, Arquitectos Técnicos e Ingenieros de Edificación (C/ Catedrático Ferré Vidiella 7, 03005 Alicante; 96 592 48 40; colegio@coaatalicante.org) | Site aparejadoresalicante.org gaf bij ons een certificaatfout; of er een openbaar ledenregister is, is niet vastgesteld. | zoekresultaat · 7 |

### 3.2 Bureaus die Jávea bedienen

| Bureau | Vestiging | Diensten (eigen site) | Bemiddelt percelen met project? | Bron · bewijstype |
|---|---|---|---|---|
| Velló Monfort Arquitectes | Carrer Vallier 2, 4ºB, 46702 Gandía; 600 39 70 39 | "Proyectos obra nueva · Reformas integrales · Diseño de interiores · Dirección de obra"; "desde la primera idea y el estudio del solar hasta el proyecto, las licencias y la dirección de obra" | Niet vermeld | vellomonfortarquitectes.com · 1 |
| Arquitectos Jávea | Carrer Roques 9, 03730 Xàbia; 604 485 319; info@arquitectosjavea.com.es | "proyectos de arquitectura, reformas integrales, diseño de interiores, certificados técnicos, licencias de apertura y cambios de uso" | Niet vermeld | arquitectosjavea.com.es · 1 |
| Studio Base | Ctra. Moraira–Calp 159 (Moraira) en C/ Calatrava 13 (Valencia); +34 652 729 149 | "diseño de viviendas personalizadas", "consultoría y planificación" | Niet vermeld | studiobase.design · 1 |
| Innov-arq | Carrer Metge Adolfo Quiles 6, 03590 Altea; info@innov-arq.com | "new construction, renovations, and rehabilitations" en "permit management" | Niet vermeld | innov-arq.com · 1 |
| QB Arquitectos | Dénia, Valencia, Madrid; opgericht 2005 | "Recomendado" op javea.com | Niet vermeld | javea.com · 1 |
| GV Arquitecnia | — | Bioklimatisch/duurzaam; op javea.com | Niet vermeld | javea.com · 1 |
| Miralbo | Jávea | Ontwerp + promotie + bouw (zie 2.1) | Verkoopt eigen villa's/projecten | miralbo.com · 1 |

**Conclusie (· 4).** Geen enkel onderzocht bureau adverteert bemiddeling van "parcela con proyecto y licencia". De verkoop van zulke percelen loopt via makelaars (3.3). Architecten zijn niettemin de vroegste schakel: zij weten welk project een licentie heeft gekregen en welke opdrachtgever afhaakt. Daarom hoort een aparte partnerlijn voor architecten in sectie 5.

### 3.3 Wie percelen met project en licentie werkelijk aanbiedt

| Aanbieder | Object (14-09-2026) | Bron · bewijstype |
|---|---|---|
| Luxia Properties (Av. dels Furs 27, local 4, 03730 Xàbia; ventas@luxiaproperties.com) | Ref. JP144, Puerta Fenicia, 1.323 m², 350.000 €, "proyecto arquitectónico y licencia de obra concedida", villa 264 m² op drie niveaus | luxiaproperties.com · 1 |
| InmoVillas Jávea (Av. del Mediterráneo 41; +34 966 46 00 33) | Ref. JP135, Camí Cabanes (zuidzijde Arenal), 1.123 m², 420.000 €, "licencia completa y lista para la construcción, con planos aprobados", villa 287 m² | inmovillasjavea.com · 1 |
| Six Seconds Properties SL | Ref. JA-SO-1001, Jávea Puerto, 192 m², 650.000 €: "Parcela de 192 m2 en el centro del puerto de Jávea con proyecto con licencia para la edificación de 6 viviendas." | sixsecondsproperties.com · 1 |
| MG Villas Luxury Property (Av. de la Libertad 11; sinds 1994) | Aanbodpagina: "plots ... with a construction project and with a building license" | mgvillas.co.uk · 1 |
| Rimontgó (Av. de Lepanto 1; sinds 1959) | "Plot with building permit and project for a home in the Montgó area, Jávea"; verder drie percelen in Adsubia en één in Tossals | rimontgo.com · 1 |
| COSTA HOUSES Luxury Villas | Ref. 2732P, Balcón al Mar, "proyecto y licencia", villa 762 m² — alleen zoekresultaat; pagina kon niet worden opgehaald | zoekresultaat · 7 |
| Idealista (assistent) | 40 percelen in Jávea/Xàbia matchen de tekst "proyecto y licencia": 35 professioneel, 5 particulier; 150.000 – 2.000.000 €, mediaan 505.000 €; drie voorbeelden met concrete status: "licencia de construcción vigente" (Rafalet, 1.120 m², 150.000 €), "licencia de construcción en trámite" (Cuesta San Antonio, 1.000 m², 1.500.000 €), "proyecto y licencia de obra mayor en tramite" (1.064 m², 400.000 €). Eén advertentie biedt een perceel voor "15 unidades" zonder makelaar (684 m², 820.000 €). | Idealista-assistent · 3/1 |

Let op de verschillen in status: "licencia concedida", "licencia vigente", "licencia en trámite" en "proyecto presentado" zijn vier verschillende dingen; masterprompt §14–16 vraagt om verificatie bij de gemeente vóór elke bouwconclusie. Een licentie heeft bovendien een geldigheidstermijn; caducidad is niet gecontroleerd (· 7).

## 4. Particuliere kanalen: wat mag en wat niet (opdracht d)

### 4.1 De kanalen en hun voorwaarden

| Kanaal | Wat er staat | Toegang | Voorwaarden (letterlijk) | Bron · bewijstype |
|---|---|---|---|---|
| **Milanuncios** | Provinciepagina "+ 10.000 anuncios" casas Alicante; Jávea-pagina toonde provinciebrede resultaten; geen zichtbaar filter particular/profesional | Openbaar, zonder inlog | Condiciones de uso (22-12-2022), sectie 3: "No usar robots, spiders, 'scrapers' o cualquier otro medio automático para acceder al Portal para copiar, retirar, renovar o publicar contenido sin previo consentimiento escrito" (punt 9); "No almacenar o en cualquier forma recabar información o datos personales de terceros sin su consentimiento, incluidas las direcciones de correo electrónico" (punt 11); "No difundir comunicaciones no solicitadas o autorizadas" (punt 7). Normas de publicación (24-01-2023), inmobiliaria: "si quieres publicar o tienes publicados 3 o más anuncios, se deberá hacer a través de nuestra herramienta para profesionales, cuya contratación tiene un coste" (de fetch noemde elders een drempel van 6 — **[te verifiëren]**). | milanuncios.com · 1 |
| **Wallapop** | Pagina "inmobiliaria/javea": ruim 30 advertenties, mix van particulieren en professionals (o.a. SOLIDINMUEBLES, MAGNUS REAL ESTATE, doorplaatsingen van Yaencontre); van 60 €/maand garage tot 3.610.000 € | Openbaar, zonder inlog | Terms (laatste versie 10-04-2026): "Not to systematically extract or reuse part or all of the content of the Platform, without our express written consent. In particular, you may not (i) use search tools or robots, or (ii) extract data"; "Not to use external software tools (bots, etc.), unless such use is authorized or permitted by us"; niet-professionele gebruikers: "use our Services solely for your personal benefit and not for commercial purposes". | about.wallapop.com · 1 |
| **Facebook-groepen** | Groepen als "Jávea compra venta" zijn via zoekmachines niet te verifiëren; alleen algemene pagina's (Ajuntament, Jávea.com) kwamen naar boven. Bestaan en omvang: ONBEKEND. | Alleen ingelogd, per groep | Meta Terms of Service (ingangsdatum 01-01-2025), 3.2.3: "You must not access data from our Products or collect it using automated means"; 3.2.2: geen "spam"; 4.5.1: commercieel gebruik vereist acceptatie van de Commercial Terms. | facebook.com/legal/terms · 1; groepen · 7 |
| **Idealista, particulieren** | Assistent, "casa para reformar de particular en Jávea", chalets: 70 totaal, 30 opgehaald, alle 30 "professional" — de vrije tekst "de particular" filtert niet. Bij terrenos: 5 van 40 "private". | Via assistent | Zie R01; scrapen van idealista.com geeft 403 en is in strijd met de voorwaarden (marktdata-bronnen.md, 25-08-2026). | Idealista-assistent · 3 |

### 4.2 Het juridische kader

| Regel | Tekst / strekking | Bron · bewijstype |
|---|---|---|
| **LSSI art. 21.1** (Ley 34/2002, geconsolideerd, laatste wijziging 24-12-2024) | "Queda prohibido el envío de comunicaciones publicitarias o promocionales por correo electrónico u otro medio de comunicación electrónica equivalente que previamente no hubieran sido solicitadas o expresamente autorizadas por los destinatarios de las mismas". | boe.es BOE-A-2002-13758 · 2 |
| **LSSI art. 21.2** | Uitzondering alleen bij "una relación contractual previa", mits de gegevens rechtmatig verkregen zijn en het gaat om "productos o servicios de su propia empresa que sean similares a los que inicialmente fueron objeto de contratación". Elke mail moet een eenvoudig, gratis opt-out-adres bevatten. | boe.es · 2 |
| **AEPD, Gabinete Jurídico, informe 0164/2018** | Bevestigt dat art. 21 geen stilzwijgende toestemming toelaat ("es lo suficientemente claro al requerir un consentimiento expreso"), dat de LSSI als bijzondere wet vóór het RGPD gaat ("La Ley 34/2002 constituye norma especial") en haalt de Audiencia Nacional (09-01-2009, rec. 97/2007) aan: e-mailadressen die van websites zijn verzameld mogen niet zonder toestemming worden aangeschreven. | aepd.es · 2 |
| **LOPDGDD art. 19** (LO 3/2018, geconsolideerd 09-05-2023) | Vermoeden van gerechtvaardigd belang (RGPD art. 6.1.f) voor contactgegevens van personen bij een rechtspersoon en van "empresarios individuales y profesionales liberales", mits "únicamente los datos necesarios para su localización profesional" en het doel "únicamente mantener relaciones de cualquier índole con la persona jurídica". | boe.es BOE-A-2018-16673 · 2 |
| **Masterprompt §26** | "Automatiseer geen ongevraagde massabenadering van particuliere eigenaren." en: "Een rechtmatige gegevensverwerking betekent niet automatisch dat ieder marketingkanaal is toegestaan." | MASTERPROMPT.md · 3 |

**Wat dit samen betekent (· 4, juridische toets door een Spaanse advocaat blijft nodig):**

- Art. 19 LOPDGDD geeft een grondslag om zakelijke contactgegevens van makelaars, ontwikkelaars en architecten te bewaren en te gebruiken voor een zakelijke relatie. Dat regelt de gegevensverwerking, niet het kanaal.
- Art. 21 LSSI geldt voor het kanaal e-mail/WhatsApp/SMS en spreekt van "destinatarios" zonder onderscheid tussen particulier en bedrijf; de AEPD past de opt-in-regel strikt toe. Of een eerste zakelijke e-mail aan een makelaarskantoor eronder valt, is in onze bronnen niet met een eenduidige passage beslist → **[te verifiëren]**. Veilige lijn: eerste contact per telefoon of persoonlijk (LSSI ziet op elektronische reclame), of via het contactformulier van het kantoor; e-mail en WhatsApp pas nadat de ander daar uitdrukkelijk mee heeft ingestemd, en altijd met opt-out.
- Particuliere verkopers op Milanuncios, Wallapop of Facebook: het platform verbiedt automatisch verzamelen én het opslaan van hun contactgegevens; de LSSI verbiedt ongevraagde elektronische reclame. Massabenadering is dus én contractueel én wettelijk uitgesloten.

### 4.3 Wat rechtmatig kan

| Werkwijze | Waarom het kan | Voorwaarden |
|---|---|---|
| Handmatig lezen van openbare advertenties (Milanuncios, Wallapop, Facebook Marketplace als lid) voor eigen analyse | Lezen is normaal gebruik van het platform; geen bot, geen extractie | Geen opslag van naam/telefoon van particulieren; alleen objectkenmerken en advertentie-URL in het dossier; frequentie handmatig, geen scripts |
| Reageren op één concrete advertentie via het contactsysteem van het platform, met een echte vraag over dat object | De adverteerder nodigt zelf tot contact uit; het is een reactie, geen reclame-uiting | Eén bericht per object, geen sjabloon in bulk, geen doorverwijzing naar eigen diensten buiten de vraag; Wallapop alleen met een Professional/Business-account, Milanuncios via MA PRO als TREE zelf ≥ 3 advertenties plaatst |
| Eigen inbound-kanaal: pagina "Verkoop je huis of perceel in Jávea aan TREE" op treeproperties.es met toestemmingsvinkje, plus vermelding in eigen advertenties en nieuwsbrief | Toestemming wordt door de eigenaar zelf gegeven (LSSI art. 21.1 "expresamente autorizadas") | Privacyverklaring, doelbinding, bewaartermijn; GHL als CRM van waarheid (ADR-0014) |
| Lid worden van lokale Facebook-groepen als bedrijf en daar plaatsen wat de groepsregels toestaan (eigen zoekvraag, eigen aanbod) | Groepsregels en Meta Commercial Terms staan zakelijke deelname toe waar de beheerder dat toelaat | Geen scraping van ledenlijsten; geen privéberichten aan leden die niet zelf reageerden |
| Fysieke kanalen: bouwborden, "se vende"-borden, notarissen, administradores de fincas, gemeentelijke publicaties (BOP, tablón) | Geen elektronische communicatie, geen platform | RGPD blijft gelden voor wat je noteert; brief per post aan een particulier is geen LSSI-kanaal maar wel RGPD → per geval beoordelen **[te verifiëren]** |
| Professionele partners actief benaderen (makelaars, ontwikkelaars, architecten) | Art. 19 LOPDGDD; §26 verbiedt alleen massabenadering van particulieren | Persoonlijk, één op één, eerste contact telefonisch of aan de balie; zie sectie 5 |

**Wat niet mag (kort):** scrapers of "API's" van derden op Milanuncios/Wallapop/Facebook (Apify, Octoparse en soortgelijke diensten kwamen in zoekresultaten voorbij; het zijn niet-geautoriseerde bronnen in de zin van masterprompt §6), bulkberichten via platformchat, e-mailoogst van websites, WhatsApp-lijsten van particulieren, en automatische "wil je verkopen?"-mailings.

## 5. Professionele samenwerkingsaanpak voor vroege dealflow (opdracht e)

Alles in deze sectie is een voorstel. Bedragen zijn werkhypothesen tot Jan ze bevestigt; niets wordt verzonden of toegezegd zonder zijn akkoord. Afzender is **TREE** (Find. Build. Live.); Rocksure Capital blijft buiten deze communicatie.

### 5.1 Zoekprofiel voor partners: "Wat TREE in Jávea zoekt"

**Werkgebied:** Jávea/Xàbia en directe buurgemeenten (Benitatxell, Dénia, Gata de Gorgos, Teulada-Moraira). Objecten buiten dat gebied alleen als het om een bijzondere verkoop gaat.

| Categorie | Wat wij zoeken | Signalen die tellen | Prijsklasse (WERKHYPOTHESE) |
|---|---|---|---|
| **1. Bestaand vastgoed met renovatiepotentieel** | Vrijstaande woningen en appartementen op goede plek, bouwkundig bruikbaar, verouderd of onlogisch ingedeeld; sloop-herbouw-kandidaten; uitbreidbare woningen | Geen of oude reforma; lange marketinghistorie; prijsverlaging; slechte presentatie; erfenis- of pakketverkoop | Vraagprijs 250.000 – 900.000 € (op Idealista lagen 30 "para reformar"-chalets tussen 280.000 en 2.595.000 €, mediaan 790.000 €) |
| **2. Percelen en ontwikkelobjecten** | Bouwrijpe urbane percelen, percelen met project en/of licentie, stilgevallen of onafgebouwde projecten, structuren, solares in centrum en haven | Licentiestatus (concedida / vigente / en trámite), geldigheid, geotechniek, aansluitingen; meerdere advertenties van hetzelfde perceel | 150.000 – 800.000 € voor villapercelen (Idealista: 150.000 – 2.000.000 €, mediaan 505.000 €); meergezinssolares zonder plafond, per geval |
| **3. Bijzondere verkopen** | Bankvastgoed, executie- en faillissementsverkopen, verkopen door fondsen, situaties met juridische of technische complexiteit, "off-market" van een verkoper die niet wil adverteren | Verkoper onder tijdsdruk; onvolledige documentatie; bezetting; onduidelijke eigendom | Geen ondergrens; boven 1.500.000 € alleen met investeerder aan tafel |

**Wat wij niet zoeken:** afgebouwde nieuwbouw van promotoren zonder korting, huurobjecten, objecten zonder duidelijke titel, en alles wat buiten het RAICV of zonder verkoopbevoegdheid wordt aangeboden.

**Wat de partner van ons krijgt:** binnen 1 werkdag ontvangstbevestiging, binnen 5 werkdagen een eerste oordeel (interessant / nee / vragen), binnen 10 werkdagen een besluit over bezichtiging of bod, en altijd een reden bij een afwijzing. Het object blijft van de partner: TREE benadert de verkoper niet buiten de partner om.

### 5.2 Aanleverformulier (velden)

Uitvoering: een eenvoudig webformulier (GoHighLevel, want dat is het CRM van waarheid) plus een pdf-versie voor wie liever mailt. Velden met * zijn verplicht.

**A. Partner**
1. Bedrijfsnaam *
2. Contactpersoon en functie *
3. Telefoon * en e-mail *
4. RAICV-nummer * (makelaars) / colegiado-nummer (architecten) / CIF (ontwikkelaars)
5. Rol bij dit object *: listing agent met mandaat / kent de eigenaar zonder mandaat / eigen bezit / collega-tip
6. Mandaat aanwezig? *: exclusief / gedeeld / geen / onbekend — met datum en looptijd als bekend

**B. Object**
7. Categorie *: 1 renovatie / 2 perceel-ontwikkeling / 3 bijzondere verkoop
8. Gemeente en zone/urbanisatie *
9. Adres of, als dat niet mag, coördinaten of kadastrale referentie (referencia catastral)
10. Type object en huidige staat *
11. Perceeloppervlak (m²) en bebouwd oppervlak (m²) volgens welke bron (kadaster / registro / opgave verkoper)
12. Bouwjaar en laatste renovatie (als bekend)
13. Vraagprijs of prijsindicatie * en of die onderhandelbaar is volgens de partner
14. Bij percelen: planologische classificatie, licentiestatus (concedida / vigente / en trámite / geen), datum licentie, projectnaam en architect (bedrijf), geotechnisch onderzoek ja/nee
15. Bij stilgevallen projecten: fase van de bouw, reden van stilstand voor zover bekend, betrokken aannemer (bedrijf)
16. Bij bijzondere verkopen: soort verkoper (bank / fonds / curator / rechtbank / particulier via bewindvoerder), termijn, procedure
17. Waarom de partner dit object voor TREE ziet (vrije tekst, drie regels)
18. Is het object al ergens gepubliceerd? *: ja (welke portalen/kantoren) / nee / binnenkort — dit voedt de dedup-controle

**C. Documenten (optioneel bij aanlevering, verplicht vóór bod)**
19. Foto's, plattegronden, nota simple, IBI, certificado energético, licentie en project, cédula/licencia de ocupación

**D. Afspraken**
20. Gewenste vergoeding volgens partner: deelt in verkoperscommissie / finder's fee / anders — bedrag of percentage niet vooringevuld (zie 5.3)
21. Mag TREE de verkoper rechtstreeks spreken? ja / alleen samen / nee
22. Geheimhouding gewenst? ja / nee; bijzonderheden
23. Bevestiging *: "Ik lever deze informatie te goeder trouw aan en heb het recht dit object te delen." (vinkje)
24. Toestemming *: "TREE mag mij over dit en vergelijkbare objecten per e-mail en telefoon benaderen; ik kan dit elk moment intrekken." (vinkje — dit is de uitdrukkelijke toestemming uit LSSI art. 21)

### 5.3 Opvolgprocedure

| Stap | Termijn | Wie | Wat |
|---|---|---|---|
| 1. Ontvangst | binnen 1 werkdag | TREE (kantoor) | Bevestiging aan partner; dossier aanmaken in GHL met partner, object, categorie; dedup-controle tegen bestaande dossiers (referentie, coördinaten + oppervlak, prijs + slaapkamers + perceel) |
| 2. Eerste oordeel | binnen 5 werkdagen | Jan + bouwkundige | Bureaucontrole: kadaster/registro, planologie (bij percelen), marktvergelijking, eerste dealhypothese volgens masterprompt §4 ("Dit object kan interessant zijn omdat …, mits …") |
| 3. Besluit | binnen 10 werkdagen | Jan | Bezichtiging plannen / vragen stellen / afwijzen met reden. Afwijzingsreden altijd naar de partner, in twee regels |
| 4. Verdieping | na bezichtiging | TREE Build (bouwkundige), architect, advocaat | Technische keuring, licentie- en titelcontrole, begroting; documenten opvragen via de partner |
| 5. Bod | na akkoord Jan | Jan via partner | Schriftelijk, met voorbehouden; nooit rechtstreeks aan de verkoper als de partner een mandaat heeft |
| 6. Terugkoppeling | elke 2 weken zolang het dossier open is; eindbericht bij sluiting | TREE | Kort statusbericht aan de partner; bij aankoop een bedankje en de afgesproken vergoeding |

**Geheimhouding.** Aangeleverde objecten en documenten blijven binnen TREE en de ingeschakelde professionals (advocaat, architect, bouwkundige). TREE publiceert het object niet, deelt het niet met derden en benadert de verkoper niet buiten de partner om. Een korte wederzijdse geheimhoudingsafspraak (één A4) hoort bij de eerste samenwerking; tekst op te stellen door de advocaat van TREE.

**Commissie en vergoeding (alleen als voorstel; percentages door Jan vast te stellen).**
- Partner is listing agent met mandaat: de partner houdt zijn eigen commissie van de verkoper; TREE vraagt geen deling en betaalt niets extra. Dit is het gangbare tweemakelaarsmodel dat MLS Dénia beschrijft ("95% of real estate sales involve two agents, the seller's agent and the buyer's agent"); de verdeling tussen die twee is in geen enkele bron gepubliceerd (· 7).
- Partner is introducer zonder mandaat (kent de eigenaar, of een architect/ontwikkelaar die een afhakende opdrachtgever kent): finder's fee bij notariële overdracht, als percentage van de koopsom of een vast bedrag — bedrag ONBEKEND en door Jan te bepalen; alleen uitbetaalbaar aan een partij die dat rechtmatig mag ontvangen (bij bemiddelingsactiviteit: RAICV-ingeschreven).
- Partner is verkoper (ontwikkelaar/eigen bezit): geen vergoeding; rechtstreekse onderhandeling.
- Alle afspraken schriftelijk vóór de bezichtiging, in een nota de encargo of samenwerkingsbrief; geen exclusiviteit of commissierecht veronderstellen zonder handtekening (masterprompt §9).

**Registratie in het CRM (masterprompt §26).** Per dossier gescheiden statussen: objectstatus, onderzoeksstatus, investeringsstatus, commerciële contactstatus. Partnerprestaties bijhouden: aantal aangeleverde objecten, aantal bezichtigd, aantal geboden, aantal gekocht, gemiddelde reactietijd van TREE. Dat is de feedbacklus uit §26 en bepaalt wie een voorkeurspartner wordt.

**Volgorde van benaderen (voorstel).**
1. Kantoren die nu al percelen met project verkopen (Luxia, InmoVillas, Six Seconds, MG Villas, Rimontgó): zij hebben aantoonbaar de categorie-2-stroom.
2. Kantoren van de gemeentelijke lijst met lokaal, niet-gedeeld aanbod (te bepalen in het makelaarsregister van §9 na een dedup-analyse van hun sites).
3. MLS Dénia en MLS 03724: gesprek over buyer-side samenwerking of lidmaatschap (eis: RAICV van TREE Properties).
4. Ontwikkelaars (Promociones Jávea, Miralbo, Living Inversiones, Ten Brinke, Prygesa, Aelca): tweerichtingsrelatie — zij zoeken grond, wij zoeken hun afvallers en stilgevallen delen; plus route C (keukens/sanitair via Sani-Kitchen Projects).
5. Architecten (Velló Monfort, Arquitectos Jávea, Studio Base, Innov-arq, QB): partnerlijn "proyecto sin cliente".

### 5.4 Conceptberichten — CONCEPT, NIET VERZENDEN

Uitgangspunten: TREE is het onderwerp van de zin; feiten vóór bijvoeglijke naamwoorden; geen uitroeptekens; je/you; Spaans in tú (zakelijk klantcontact volgens de registermatrix — Jan kan voor eerste contact met een onbekend kantoor usted verkiezen; dan de hele tekst omzetten, nooit mengen). Eerste contact bij voorkeur telefonisch of persoonlijk; deze teksten zijn voor de opvolgmail nadat het kantoor daarmee heeft ingestemd, of voor het contactformulier van het kantoor. Plaatshouders staan tussen [ ].

**ES — aan een makelaarskantoor (opvolging na telefoongesprek)**

> Asunto: TREE busca en Jávea: reformas, parcelas y ventas especiales
>
> Hola [nombre],
>
> gracias por la llamada de esta mañana. Te dejo por escrito lo que buscamos, para que lo tengas a mano.
>
> TREE está en Jávea desde 2022. Compramos y reformamos, construimos y vendemos: agencia, obra y cocinas y baños bajo el mismo techo. Buscamos tres cosas en Jávea y alrededores: casas para reformar en buena ubicación, parcelas urbanas con o sin proyecto y ventas especiales (bancos, herencias, proyectos parados). Como orientación, casas entre 250.000 y 900.000 € y parcelas entre 150.000 y 800.000 €; fuera de ese rango, si el caso lo merece, también.
>
> Funciona así. Nos mandas la ficha, aunque sea con dos líneas y una foto. En un día te confirmamos que la tenemos. En cinco te decimos si nos interesa y, si no, por qué. En diez decidimos visita u oferta. El cliente sigue siendo tuyo: no hablamos con el propietario sin ti, y tu comisión con el vendedor no la tocamos.
>
> Si te encaja, te paso el formulario y un acuerdo de confidencialidad de una página. ¿Nos vemos la semana que viene en tu oficina? Martes o jueves por la mañana me viene bien.
>
> Un saludo,
> [Nombre] · TREE Properties · [teléfono] · [RAICV n.º — te verifiëren]
> Find. Build. Live.
>
> Si prefieres no recibir más correos de TREE, responde con "baja" y lo dejamos aquí.

**EN — to an estate agency (follow-up after a phone call)**

> Subject: What TREE is looking for in Jávea
>
> Hi [name],
>
> Thanks for the call this morning. Here is what we discussed, in writing.
>
> TREE has been in Jávea since 2022. We buy and renovate, we build, and we sell: the agency, the building team and the kitchen and bathroom side under one roof. In Jávea and the villages around it we look for three things: houses to renovate in a good spot, urban plots with or without a project, and special sales such as bank stock, inheritances and stalled projects. As a guide, houses between € 250,000 and € 900,000 and plots between € 150,000 and € 800,000. Outside that range, if the case deserves it, we still want to hear about it.
>
> This is how it works. You send us the basics, two lines and a photo is enough. Within one working day we confirm we have it. Within five we tell you whether we are interested, and if not, why. Within ten we decide on a viewing or an offer. The client stays yours: we do not speak to the owner without you, and your commission with the seller is not ours to touch.
>
> If that suits you, I will send the form and a one-page confidentiality note. Shall we meet at your office next week? Tuesday or Thursday morning works for me.
>
> Best,
> [Name] · TREE Properties · [phone] · [RAICV no. — to verify]
> Find. Build. Live.
>
> If you would rather not hear from TREE by e-mail, reply "stop" and we will leave it there.

**ES — aan een architectenbureau of ontwikkelaar (eerste bericht via contactformulier of na kennismaking)**

> Asunto: Proyectos con licencia que se quedan sin cliente
>
> Hola [nombre],
>
> soy [Nombre], de TREE, en Jávea. Construimos y reformamos aquí desde 2022, con equipo de obra propio.
>
> Te escribo por un caso concreto que se repite: un proyecto con licencia concedida, o a punto, cuyo cliente se echa atrás. La parcela se queda parada y el trabajo del estudio, en un cajón. A nosotros nos interesa exactamente eso: comprar la parcela con el proyecto y llevarlo a obra, contigo como arquitecto si el cliente lo permite.
>
> No pedimos exclusividad ni datos del propietario. Solo saber que existe el caso, para que tú lo plantees a tu cliente. Si sale, se formaliza con el propietario y ante notario; tu papel y tus honorarios los acordamos por escrito antes de nada.
>
> ¿Tienes media hora la semana que viene? Me acerco a tu estudio.
>
> Un saludo,
> [Nombre] · TREE · [teléfono]
> Find. Build. Live.

**EN — to a developer (first message via contact form or after an introduction)**

> Subject: Plots and stalled phases in Jávea
>
> Hi [name],
>
> I am [Name] from TREE in Jávea. We have built and renovated here since 2022 with our own site team, and we also sell.
>
> Two things you may run into where we can help. First, plots you have looked at but will not develop yourself: too small, wrong zoning, or the numbers do not work for a multi-unit scheme. Second, phases or single units that stall. We buy that kind of thing, and we can also take on finishing work, kitchens and bathrooms for what you do build.
>
> No exclusivity and no obligation. If a case comes up, one message is enough and we will give you an answer within ten working days.
>
> Half an hour next week? I am happy to come to your office.
>
> Best,
> [Name] · TREE · [phone]
> Find. Build. Live.

Twijfelpunten bij de conceptteksten: (1) de vermelding "RAICV n.º" veronderstelt dat TREE Properties is ingeschreven — controleren vóór gebruik; (2) de prijsklassen zijn werkhypothesen en horen pas in de tekst als Jan ze bevestigt; (3) de zin "tu comisión con el vendedor no la tocamos" is een voorstel voor de commissielijn en geen toezegging over finder's fees.

## 6. Bronnenregister voor deze stroom (masterprompt §7)

Statussen: GEVERIFIEERD EN ACTIEF · TOEGANG AANGEVRAAGD · CONTRACT OF TOESTEMMING NODIG · TECHNISCH ONDERZOEK NODIG · ALLEEN HANDMATIG · NIET GEBRUIKEN.

| Bron | Type | Toegang | Status | Opmerking |
|---|---|---|---|---|
| RAICV, openbaar register (habitatge.gva.es → sforms.gva.es) | Overheidsregister | Web, JS-formulier | ALLEEN HANDMATIG | Controle van elke partner; velden niet machinaal leesbaar |
| COAPI Alicante / APIAL / APIRed | Beroepsorganisatie + bolsa | Openbare zoekfunctie; ledendeel na colegiación | CONTRACT OF TOESTEMMING NODIG | Alleen colegiados; titeleis; contributie onbekend |
| ASICVAL | Vereniging | Lidmaatschap op aanvraag | CONTRACT OF TOESTEMMING NODIG | Voorwaarden niet gepubliceerd |
| MLS Dénia | MLS-vereniging | Lidmaatschap na goedkeuring | CONTRACT OF TOESTEMMING NODIG | Eis: kwalificatie, opleiding, ervaring; RAICV |
| MLS 03724 Teulada-Moraira | MLS-vereniging | Lidmaatschap | CONTRACT OF TOESTEMMING NODIG | Ledental tegenstrijdig (4 of 16) |
| Gemeentelijke lijst inmobiliarias y promotores (xabia.org) | Overheidspublicatie | Open web | GEVERIFIEERD EN ACTIEF (handmatig) | 39 regels opgehaald; pagina noemt 45 |
| Tablón de anuncios / sede electrónica Xàbia | Overheidspublicatie | Open web | ALLEEN HANDMATIG | Geen licentielijsten; wel stedenbouwkundige aankondigingen |
| Boletín Oficial de la Provincia de Alicante | Overheidspublicatie | Open web | TECHNISCH ONDERZOEK NODIG | Niet in deze stroom getest; route voor PAI, ruina, caducidad |
| Sites van ontwikkelaars (tenbrinke.com, prygesa.es, aelca.es, livinginversiones.com, promocionesjavea.com, miralbo.com, vapf.com) | Aanbieders | Open web | ALLEEN HANDMATIG | Kwartaalcontrole projectstatus; geen feeds gezien |
| PROVIA | Brancheorganisatie | Geen ledenlijst | ALLEEN HANDMATIG | Netwerkkanaal; lidmaatschap/contact per telefoon |
| CTAA bolsa de servicios | Colegio | Registratie vereist | TECHNISCH ONDERZOEK NODIG | Werking achter inlog onbekend |
| COAT Alicante | Colegio | Site niet bereikbaar via fetch | TECHNISCH ONDERZOEK NODIG | Certificaatfout |
| Makelaarssites met percelen (luxiaproperties.com, inmovillasjavea.com, sixsecondsproperties.com, mgvillas.com, rimontgo.com) | Aanbieders | Open web | ALLEEN HANDMATIG | Geen feeds of exports gezien; kandidaten voor rechtstreekse aanlevering |
| Milanuncios | Particulier/pro-platform | Open web; voorwaarden verbieden bots | ALLEEN HANDMATIG | Geen scraping, geen bulkcontact; MA PRO voor eigen advertenties |
| Wallapop | Particulier/pro-platform | Open web; voorwaarden verbieden extractie | ALLEEN HANDMATIG | Business-account nodig voor zakelijk gebruik |
| Facebook-groepen | Sociaal platform | Ingelogd lid | ALLEEN HANDMATIG | Geen automatische verzameling (Meta ToS 3.2.3) |
| Scrapers/"API's" van derden voor deze platforms | Commerciële scrapers | — | NIET GEBRUIKEN | In strijd met voorwaarden; masterprompt §6 |
| Idealista-assistent (MCP) | Officiële assistent | Aangesloten | GEVERIFIEERD EN ACTIEF (voorwaarden gepland gebruik: zie R01) | Vrije tekst "de particular" filtert niet op particulieren |

## 7. Open vragen voor Jan (⏸️ ACTIE VOOR JAN)

1. Is TREE Properties ingeschreven in het RAICV en wat is het nummer? Zonder dat nummer kunnen wij geen MLS-lidmaatschap aanvragen en hoort het niet in de conceptberichten.
2. Wil je dat TREE lid wordt van MLS Dénia en/of MLS 03724 (gedeeld exclusief aanbod, maar ook de plicht om eigen exclusieven te delen)? Dat vraagt een gesprek met beide besturen.
3. Bevestig of wijzig de prijsklassen in het zoekprofiel (250.000 – 900.000 € woningen; 150.000 – 800.000 € percelen).
4. Vergoedingsbeleid voor introducers zonder mandaat: finder's fee ja/nee, en hoe hoog. Zonder dat besluit blijft die regel in 5.3 leeg.
5. Aanspreekvorm Spaans in de partnercommunicatie: tú (voorstel) of usted.
6. Laat een Spaanse advocaat twee punten bevestigen: of een eerste zakelijke e-mail aan een makelaarskantoor onder LSSI art. 21 valt, en onder welke voorwaarden een brief per post aan een particuliere eigenaar toelaatbaar is.
7. Wie binnen TREE bewaakt de termijnen van 1/5/10 werkdagen en de tweewekelijkse terugkoppeling? Zonder eigenaar sterft de procedure.

## 8. Geblokkeerd of mislukt

- WebSearch-budget van de sessie op na de laatste zoekronde; enkele verificaties (o.a. het wetsartikel in Ley 2/2017, naam van de promotor van Blooming Village en Lemon Residence, ledenlijsten van MLS Dénia/MLS 03724, cuota COAPI) konden daardoor niet verder worden gezocht.
- aparejadoresalicante.org en aparejador.arquitectotecnico.eu: niet bereikbaar (certificaatfout resp. DNS).
- noticias.juridicas.com (Decreto 98/2022): certificaatfout; tekst via Iberley opgehaald.
- villas-plots.com: HTTP 403; costa-houses.com: fetch mislukt zonder output; mgvillas.com/P478 en provia.es/asociados: 404; mlsdenia.com/quienes-somos: 404; vellomonfortarquitectes.com/arquitectos-javea: HTTP 500 (hoofdpagina wel opgehaald).
- sforms.gva.es (RAICV-raadpleging): laadt via JavaScript; niet leesbaar via fetch. Niet omzeild.
- xabia.org noemt 45 bedrijven, de opgehaalde tabel telde 39: verschil niet opgelost.
- Facebook-groepen: niet via zoekmachine te verifiëren; niet ingelogd.
- Milanuncios-Jávea-pagina toonde provinciebrede resultaten; een Jávea-specifieke telling is niet gemaakt.

## 9. Bronnenlijst (URL · controledatum · bewijstype)

Wet- en regelgeving en overheid
- https://sede.gva.es/es/detall-tramit?id_proc=22848 · 14-09-2026 · 2 (RAICV: eisen, verzekeringen, grondslag)
- https://www.iberley.es/legislacion/decreto-98-2022-29-julio-consell-regula-registro-agentes-intermediacion-inmobiliaria-comunitat-valenciana-requisitos-inscripcion-27135412 · 14-09-2026 · 2 (tekst Decreto 98/2022, art. 2, 3, 4, 5, DT1, DF2)
- https://habitatge.gva.es/es/registres-en-materia-habitatge · 14-09-2026 · 2 (link openbaar register)
- https://sforms.gva.es/sformssistemaexplotacion/servletObtenerXMLns/ObtenerXMLorig?formulario=62953&SF_SIS_ICP=1 · 14-09-2026 · 7 (formulier laadt niet in fetch)
- https://www.boe.es/buscar/act.php?id=BOE-A-2017-2421 · 14-09-2026 · 7 (Ley 2/2017; registerartikel niet gevonden)
- https://www.boe.es/buscar/act.php?id=BOE-A-2002-13758&tn=1&p=20241224 · 14-09-2026 · 2 (LSSI art. 19–21)
- https://www.boe.es/buscar/act.php?id=BOE-A-2018-16673&tn=1&p=20230509 · 14-09-2026 · 2 (LOPDGDD art. 19)
- https://www.aepd.es/documento/2018-0164.pdf · 14-09-2026 · 2 (AEPD-informe over LSSI art. 21)
- https://www.xabia.org/ver/2098/Real-estate-agents-and-promoters.html · 14-09-2026 · 2 (gemeentelijke lijst)
- https://www.ajxabia.com/ver/1162/junta-de-gobierno-local.html/ · 14-09-2026 · 2 (JGL publiceert geen acuerdos)
- http://xabia.sedelectronica.es/board// · 14-09-2026 · 2/3 (tablón de anuncios)
- https://xabiaaldia.com/archive/152416/240-licencias-de-obra-mayor-en-xabia-en-2022 · 14-09-2026 · 2 (licentiecijfers gemeente, 13-01-2023)
- https://xabiaaldia.com/art/140185/sale-a-exposicion-al-publico-un-proyecto-urbanistico-en-una-parcela-de-6892-metros-cuadrados-de-xabia · 14-09-2026 · 2 (PAI ter inzage, 08-03-2022)

Beroepsorganisaties en netwerken
- https://www.apialicante.com/registro-api-coapi-alicante/ · 14-09-2026 · 1
- https://www.apialicante.com/en/the-api-profession/requirements/ · 14-09-2026 · 1
- https://www.apialicante.com/el-colegio-api-de-alicante-ayudara-a-que-todos-los-profesionales-puedan-formar-parte-del-registro-obligatorio-de-agentes-de-intermediacion-inmobiliaria/ · 14-09-2026 · 1 (09-09-2022)
- https://inmodiario.com/187/26340/colegio-api-alicante-pone-marcha-bolsa-inmobiliaria/ · 14-09-2026 · 1 (19-04-2018)
- http://www.apired.com/ · 14-09-2026 · 1
- https://asicval.es/ · 14-09-2026 · 1
- https://asicval.es/nuevo-registro-de-agentes-inmobiliarios-de-la-comunitat-valencia/ · 14-09-2026 · 1
- https://www.mlsdenia.com/ · 14-09-2026 · 1
- https://www.mlsdenia.com/en/about-us/ · 14-09-2026 · 1
- https://www.deniacasas.es/en/mls-denia/ · 14-09-2026 · 1
- https://www.mls03724.com/en/about-us/ · 14-09-2026 · 1
- https://provia.es/ · 14-09-2026 · 1
- https://www.engelvoelkers.com/es/en/real-estate-agent/valencian-community/xabia · 14-09-2026 · 1
- https://www.iadespana.es/en/find-real-estate-agent/xabia-javea-03730 · 14-09-2026 · 1
- https://www.ctaa.net/ en https://www.ctaa.net/bolsa-servicios-ciudadanos · 14-09-2026 · 1

Ontwikkelaars en projecten
- https://www.tenbrinke.com/es/noticias/noticias-reader/ten-brinke-espana-adquiere-una-parcela-de-2-000-m2-donde-desarrollara-residencial-marina-bay-sunset-tercer-proyecto-residencial-multifamiliar-en-javea-alicante.html · 14-09-2026 · 1 (18-07-2024)
- https://www.prygesa.es/obra-nueva/alicante/javea-garden · 14-09-2026 · 1
- https://www.aelca.es/es/proyectos/adeya-javea/ en https://www.aelca.es/es/proyectos/adeya-ii-javea/ · 14-09-2026 · 1
- https://www.livinginversiones.com/en/projects/living-javea-residential/ · 14-09-2026 · 1
- https://www.promocionesjavea.com/ · 14-09-2026 · 1
- https://www.miralbo.com/es-es · 14-09-2026 · 1
- https://www.vapf.com/en/real-estate-developer/residential-areas/cumbre-del-sol · 14-09-2026 · 1
- https://lamarina.eldiario.es/2026/04/16/el-urbanismo-voraz-de-xabia-complejos-de-lujo-se-alzan-a-velocidad-de-vertigo-al-lado-de-minipisos/ · 14-09-2026 · 1 (nieuws)
- https://www.ehd.es/en/for-sale/ground-floor-apartment-in-residential-blooming-village-javea-5963/ · 14-09-2026 · 1

Architecten
- https://vellomonfortarquitectes.com/ · 14-09-2026 · 1
- https://arquitectosjavea.com.es/nuestra-empresas/ · 14-09-2026 · 1
- https://studiobase.design/arquitectos-javea/ · 14-09-2026 · 1
- https://innov-arq.com/en/architects-javea/ · 14-09-2026 · 1
- https://www.javea.com/zona/comercios/construccion-bricolaje/arquitectos/ · 14-09-2026 · 1

Percelen met project (aanbieders)
- https://luxiaproperties.com/propiedad/parcela-en-venta-con-proyecto-y-licencia-en-puerta-fenicia-javea/ · 14-09-2026 · 1
- https://www.inmovillasjavea.com/propiedad/venta-cami-cabanes-parcela-604163 · 14-09-2026 · 1
- https://sixsecondsproperties.com/propiedad/1624/parcela-con-proyecto-y-licencia-en-javea-alicante/ · 14-09-2026 · 1
- https://www.mgvillas.co.uk/plots-for-sale/ · 14-09-2026 · 1
- https://www.rimontgo.com/properties/javea/plots-and-lands · 14-09-2026 · 1
- Idealista-assistent (MCP), zoekopdrachten "parcela con proyecto y licencia en Jávea" (LAND, 40 resultaten), "casa en construcción sin terminar o proyecto paralizado en Jávea" (CHALET, 66 totaal / 20 opgehaald), "casa para reformar de particular en Jávea" (CHALET, 70 totaal / 30 opgehaald); zoek-URL's: https://www.idealista.com/es/buscar/venta-terrenos/javeaxabia-alicante/parcela_con_proyecto_y_licencia_en_Javea/ ; https://www.idealista.com/es/venta-viviendas/javeaxabia-alicante/con-chalets,obra-nueva/ ; https://www.idealista.com/es/venta-viviendas/javeaxabia-alicante/con-chalets,para-reformar/ · 14-09-2026 · 3

Particuliere kanalen en voorwaarden
- https://scm-milanuncios-frontend-pro.milanuncios.com/statics/markdown/es/legal/terms-of-use.a7d9cbbb40.md · 14-09-2026 · 1 (voorwaarden 22-12-2022 / normas 24-01-2023)
- https://www.milanuncios.com/venta-de-casas-en-javea-alicante/ · 14-09-2026 · 1
- https://about.wallapop.com/en/legal-terms-and-conditions/ · 14-09-2026 · 1 (versie 10-04-2026)
- https://es.wallapop.com/inmobiliaria/javea · 14-09-2026 · 1
- https://www.facebook.com/legal/terms · 14-09-2026 · 1 (ingangsdatum 01-01-2025)

Intern
- /Users/root-admin/tree-es/deal-hunter/MASTERPROMPT.md · 14-09-2026 · 3
- /Users/root-admin/tree-es/properties/leadgen/docs/marktdata-bronnen.md · 14-09-2026 · 3 (Idealista 403, geen scraper)

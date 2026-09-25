# R16 — Rechten en compliance: portaalvoorwaarden, scraping, databankrecht, AVG/LSSI en beeldanalyse

> **NA TEGENSPRAAK (15-09-2026).** Dit rapport is door een tweede agent gecontroleerd; zie `R16-rechten-en-compliance.verificatie.md`. Betrouwbaarheid volgens die controle: hoog.
> Geen kernclaims weerlegd; wel eventuele aanvullingen en voorbehouden in het verificatiebestand.


**Controledatum:** 15-09-2026 (alles wat in dit rapport zelf is gecontroleerd). Waar een datum van 14-09-2026 staat, gaat het om een meting uit de eerdere ronde (R01–R17).
**Status:** juridisch vooronderzoek ter voorbereiding. Dit is geen juridisch advies en vervangt geen Spaanse advocaat. Punten die een advocaat moet bevestigen zijn gemarkeerd met **[advocaat]**.
**Bewijstypen (masterprompt §5):** 1 door aanbieder vermeld · 2 in officiële bron aangetroffen · 3 door ons rechtstreeks vastgesteld · 4 AI-gevolgtrekking · 5 berekening op benoemde aannames · 6 door bevoegde professional bevestigd · 7 onbekend of tegenstrijdig.

---

## Samenvatting (10 regels)

1. Geautomatiseerd ophalen, monitoren of opslaan van Idealista, Fotocasa/Habitaclia, pisos.com, Kyero en het BOE-veilingportaal is zonder schriftelijke toestemming niet toegestaan: de voorwaarden verbieden het (Idealista letterlijk "robot, spider, scraper"), het BOE-portaal sluit alle robots uit, en herhaalde systematische extractie valt onder het databankrecht (TRLPI art. 133.2).
2. Handmatig raadplegen voor eigen beoordeling is verdedigbaar. Een rechtmatige gebruiker mag niet-substantiële delen van een beschermde databank overnemen, en een contract kan dat niet uitsluiten (art. 134.1 en 134.3). Is de databank níet beschermd, dan gelden de voorwaarden onverkort (HvJ C-30/14) **[advocaat]**.
3. De tekst- en datamining-uitzondering (RDL 24/2021 art. 67) is geen vrijbrief. Ze geldt alleen voor rechtmatig toegankelijke werken, alleen voor reproductie en niet als de rechthebbende uitdrukkelijk voorbehoud maakt. Milanuncios maakt dat voorbehoud machineleesbaar voor AI-trainingscrawlers.
4. Advertentiefoto's zijn beschermd, als werk of als "mera fotografía" (25 jaar, art. 128). Downloaden om te analyseren of te hashen is al een reproductie (art. 18). Beeldvergelijking op portaalfoto's kan dus alleen met toestemming. Dat botst met het dHash-ontwerp in R17.
5. De aviso legal van Background Properties eist voor elk gebruik voorafgaande schriftelijke toestemming. TREE kreeg de feed voor de website. Opslag, historie, AI-analyse, beeldhashes en klantdossiers moeten schriftelijk worden vastgelegd; een conceptclausule staat in §6.4.
6. Open overheidsdata is wél bruikbaar. BOE-documenten mogen commercieel worden hergebruikt met bronvermelding (licentie van 27-06-2024). Catastro-webdiensten mogen voor eigen gebruik en getransformeerde producten. Registro-gegevens mogen niet in een databank voor commercialisering (RH art. 332.2), en het Registro Público Concursal verbiedt hergebruik van persoonsgegevens.
7. AVG: naam en telefoon van particuliere adverteerders zijn persoonsgegevens (pisos.com publiceert ze automatisch), net als namen van schuldenaren uit edictos en het Registro. Deal Hunter moet objectgericht werken en die gegevens niet opslaan. Een DPIA is vrijwel zeker nodig zodra veiling- of schuldenaarsgegevens worden gekoppeld (AEPD-lijst, criteria 4, 8 en 10).
8. Voor e-mail, WhatsApp en sms is voorafgaande toestemming nodig, ook richting makelaarskantoren als rechtspersoon (LSSI art. 21 en bijlage). Ongevraagd bellen kan alleen op gedocumenteerd gerechtvaardigd belang (Circular AEPD 1/2023) en na controle van de Robinsonlijst (LOPDGDD art. 23). Massabenadering van particulieren kan niet.
9. De DSA en de Data Act geven TREE geen recht op toegang tot portaaldata. Uit de AI-verordening gelden al AI-geletterdheid (art. 4) en het verbod op gezichtsdatabanken via scraping (art. 5.1.e).
10. ⏸️ ACTIE VOOR JAN: laat de BP-clausule toetsen en leg haar voor aan BP. Vraag Idealista schriftelijk om systematisch gebruik van de assistent. Laat de twaalf advocaatvragen uit §7 beantwoorden vóór de bouw van fase B.

---

## 0. Werkwijze, afbakening en beperkingen

| Onderdeel | Hoe | Resultaat |
|---|---|---|
| Wetteksten (ES) | BOE-open-data-API `legislacion-consolidada` (XML, laatste versie per artikel) | TRLPI, RDL 24/2021, LOPDGDD, LSSI, Ley 11/2022, Circular AEPD 1/2023, Ley 10/2025, Ley 37/2007, Ley 19/2015, TRLCI, Ley Hipotecaria, Reglamento Hipotecario, Ley 3/1991, Código Penal, Código Civil: gelezen (type 2) |
| EU-teksten | EUR-Lex gaf HTTP 202 met lege body (botcontrole) en is niet omzeild. In plaats daarvan de DOUE-kopieën op boe.es (`/buscar/doc.php?id=DOUE-L-…`) gebruikt | Richtlijn 96/9, AVG, AI-verordening, DSA en Data Act gelezen (type 2) |
| HvJ-arresten | curia.europa.eu en EUR-Lex niet bereikbaar voor de tekst; dictum via ipcuria.eu (secundaire vindplaats met letterlijke dictums) | C-203/02, C-202/12, C-30/14, C-762/19, C-621/22 (type 2, vindplaats secundair) |
| Spaanse rechtspraak | CENDOJ is JavaScript-only; Lexology gaf 403 | STS 572/2012 alleen via secundaire bron (type 7) |
| Voorwaarden portalen | `curl -sS -m 30` of WebFetch, één verzoek per pagina, geen omzeiling | Idealista (versie 20-11-2020), Habitaclia, pisos.com, Fotocasa-microsite, BP, RPC en BOE gelezen; Idealista-actueel, Fotocasa-portaal en Kyero geblokkeerd (zie §10) |
| robots.txt | Eén opvraging per host op 15-09-2026 | Type 3 |
| AEPD | aepd.es (pdf's en criteriapagina) | Circular 1/2023, EIPD-lijst, E/04809/2015, criterium AI-00059-2024 (type 2) |
| Lokaal | Eén leesverzoek aan de eigen dienst `127.0.0.1:3100` (`town=Javea`) om te controleren of er contactgegevens in de BP-omschrijvingen staan | Type 3 |

Wat ik **niet** heb gedaan: niets geïnstalleerd, geen dienst aangeraakt, geen portaal gecrawld, geen sleutels gelezen of overgenomen, geen namen van particulieren of schuldenaren overgenomen. WebSearch werkte in deze ronde.

Onderscheid in dit rapport: **"gezien"** = letterlijke tekst in een bron (type 2/3); **"afgeleid"** = mijn juridische gevolgtrekking (type 4), altijd als zodanig gemarkeerd.

---

## 1. Conclusie voor Jan (besluitgericht)

**Conclusie.** Deal Hunter kan juridisch verantwoord starten met drie soorten bronnen:
- **(1)** de BP-feed, zodra BP de rechten schriftelijk bevestigt;
- **(2)** open overheidsdata: BOE-API/RSS, Catastro-webdiensten en INSPIRE;
- **(3)** handmatig en ad hoc raadplegen van portalen en de Idealista-assistent, waarbij we alleen link, portaal-ID en ons eigen oordeel bewaren.

Alles wat daarbuiten ligt, heeft eerst een licentie of schriftelijke toestemming nodig. Dat geldt voor systematisch ophalen, prijshistorie van portalen, foto-analyse op portaalfoto's en klantdossiers met portaalfoto's.

**Onderbouwing.** Voorwaarden (§2), databankrecht en auteursrecht (§3), AVG en LSSI (§4).

**Aannames en onzekerheden.**
- Of de voorwaarden van Idealista ook een niet-geregistreerde bezoeker binden (browsewrap), is naar Spaans recht niet uitgemaakt. In de Ryanair-zaak vond de eerste aanleg geen contract (secundaire bron, type 7).
- Of een portaal een "substantiële investering" heeft gedaan, is per portaal een feitelijke vraag.
- De huidige versie van de Idealista-voorwaarden kon ik niet lezen (403).

**Tegenargumenten.**
- De Idealista-assistent is door Idealista zelf aangeboden om te zoeken, vergelijken en samenvatten. Dat maakt ad-hocgebruik sterker dan scraping.
- Kale feiten (prijs, m²) zijn geen auteursrechtelijk werk.
- Het HvJ eist bij databankinbreuk een risico voor de terugverdiening van de investering (C-762/19). Een beperkte interne selectie voor Jávea raakt dat misschien niet.

Die argumenten verkleinen het risico, maar maken systematische automatisering niet rechtmatig zonder toestemming **[advocaat]**.

**Vervolgstap.**
- ⏸️ ACTIE VOOR JAN: (a) conceptclausule §6.4 laten toetsen en aan BP voorleggen; (b) Idealista schriftelijk vragen of geplande, dagelijkse raadpleging via de assistent is toegestaan; (c) een Spaanse advocaat de vragen uit §7 laten beantwoorden.
- **Voor de bouw (R17):** geen dHash op Idealista-foto's en geen opslag van ruwe portaaldata. BP-snapshots pas opslaan na de schriftelijke bevestiging.

---

## 2. (a) Gebruiksvoorwaarden per bron — de clausules

### 2.1 Idealista (portaal en assistent)

| # | Document en versie | Clausule (letterlijk, kort) | Betekenis | URL | Type |
|---|---|---|---|---|---|
| I-1 | "Términos y Condiciones generales de idealista", *Última actualización 20 de noviembre, 2020* (gearchiveerde pdf, geldig tot 11-11-2021) | Verboden: "Acceder, controlar o copiar cualquier información … utilizando para ello cualquier tipo de robot, spider, scraper u otro medio automático o proceso manual para cualquier propósito, sin nuestro permiso expreso y por escrito." | Elke geautomatiseerde toegang, en zelfs handmatig systematisch kopiëren, vraagt schriftelijke toestemming | https://st1.idealista.com/ayuda/wp-content/uploads/2021/11/2021-Hasta-11-11-2021-Terminos-y-condiciones.pdf | 2 |
| I-2 | idem, zelfde lijst | Verbod om "las restricciones de los avisos de exclusión de robots" te schenden of maatregelen die toegang beperken te omzeilen; ook een verbod op "una carga irrazonable" | robots.txt en botbeveiliging zijn contractueel bindend gemaakt | idem | 2 |
| I-3 | idem, §8.1 | "no está permitido revender, realizar deep-links, utilizar, copiar, monitorizar (por ejemplo, spider, scrape), mostrar, descargar, guardar o reproducir el contenido … para cualquier actividad comercial o competitiva sin autorización previa y por escrito" | Ook **opslaan** ("guardar") en **tonen** ("mostrar") voor commerciële activiteit vraagt toestemming | idem | 2 |
| I-4 | idem, §8.1 | Gebruiker heeft "un derecho de uso estrictamente personal y privado" | Zakelijk gebruik valt buiten het standaardrecht | idem | 2 |
| I-5 | idem, §8.2 | Adverteerders geven Idealista een wereldwijde, sublicentieerbare licentie, o.a. voor "valoraciones y tasaciones de inmuebles, informes de precios, informes estadísticos, referencias históricas", ook na intrekking van de advertentie | Idealista bundelt de rechten; alleen Idealista kan ze doorlicentiëren (idealista/data) | idem | 2 |
| I-6 | idem, §6 "Servicios Adicionales" | Noemt "API" en "Servicio Vendor Leads" (contact tussen eigenaren en professionele adverteerders) als aparte diensten | Er bestaan officiële routes; condities per dienst ONBEKEND (R01) | idem | 2 |
| I-7 | idem, §11 | Deep-linken of "enmarcar" vraagt "permiso expreso y por escrito" | Relevant voor links op een eigen website; een link in een intern dossier of e-mail is afgeleid laag risico **[advocaat]** | idem | 2 / 4 |
| I-8 | idem, §14 | Spaans recht; rechtbanken van Madrid of van de woonplaats van de gebruiker | — | idem | 2 |
| I-9 | Actuele versie | `/ayuda/articulos/legal-statement/` gaf op 15-09-2026 HTTP 403 (curl en WebFetch); ook de pdf "2022-Hasta-24-08-2022" gaf 403. Zoekresultaten noemen een actuele versie van 30-04-2025 (R01, snippet) | Tekst van de actuele versie **[te verifiëren in een browser door Jan]** | https://www.idealista.com/ayuda/articulos/legal-statement/ | 7 |
| I-10 | Idealista-assistent (MCP), tool `guide_idealista_assistant`, opgevraagd 15-09-2026 | Beschrijft zoeken, filteren en "Compare several listings … or get a summary of their features" — geen gebruiksvoorwaarden, geen limieten, geen woord over opslag of automatisering | Door de aanbieder bedoeld gebruik: consumentgericht zoeken en vergelijken in de chat | MCP-tool (Idealista) | 1 / 3 |
| I-11 | robots.txt idealista.com, 15-09-2026, 586 regels | Eén blok `User-agent: *` met veel `Disallow`-regels (o.a. `/ajax/*`, `/facturas/*`, zoek- en filterpaden); **geen** AI-specifieke user-agents. Een regel `Disallow: /` voor alle bots heb ik vandaag **niet** gevonden; R01 meldde die op 14-09 wel | Afwijking met R01 **[te verifiëren]**; robots.txt is hoe dan ook geen licentie (masterprompt §7) | https://www.idealista.com/robots.txt | 3 / 7 |

### 2.2 Fotocasa en Habitaclia (Fotocasa Group / Adevinta)

| # | Document | Clausule (letterlijk, kort) | Betekenis | URL | Type |
|---|---|---|---|---|---|
| F-1 | Aviso legal van het portaal fotocasa.es | Juridische tekst wordt via JavaScript geladen; WebFetch zag op 15-09-2026 alleen de footer (zelfde als R02 op 14-09) | **Niet gelezen** — ⏸️ ACTIE VOOR JAN: in browser openen en als pdf bewaren | https://www.fotocasa.es/es/aviso-legal/ln | 3 (blokkade) |
| F-2 | "Condiciones legales" van de Fotocasa-microsite *Proyecto Vivienda* (Adevinta Spain, S.L.U., NIF B-83411652) | Verboden: "Utilizar mecanismos, software o scripts en relación con la utilización del Sitio Web" en "el copiado mediante tecnologías de buscador tipo "Robot/Crawler" … está prohibido expresamente." | Laat zien hoe de groep scraping formuleert; **geldt formeel voor de microsite, niet aantoonbaar voor het portaal** | https://www.fotocasa.es/proyecto-vivienda/condiciones-legales/ | 2 |
| F-3 | idem | Reproductie, distributie en aanpassing van inhoud (uitdrukkelijk ook "bases de datos") verboden "salvo autorización previa de sus legítimos titulares o cuando así resulte permitido por la ley" | De groep claimt uitdrukkelijk rechten op databanken | idem | 2 |
| F-4 | Términos y condiciones "Fotocasa Alquiler" (uit R02, 14-09-2026) | Verbod op reproduceren, kopiëren, distribueren "a menos que cuente con la autorización del titular" | Zelfde lijn; geen robotclausule gezien | https://www.fotocasa.es/gestion-alquiler/terminos-y-condiciones/ | 2 (R02) |
| H-1 | Condiciones Generales Habitaclia (Fotocasa Group, S.L.U., CIF B-70677125) | Toegang tot het portaal "ni confiere ningún derecho de utilización, alteración, transformación, explotación (en cualquiera de sus modalidades), reproducción, distribución o comunicación pública" zonder voorafgaande uitdrukkelijke toestemming | Hergebruik van content vraagt toestemming; de clausule noemt "bases de datos" als beschermd | https://www.habitaclia.com/hab_cliente/legalavisocontentmodal.asp | 2 |
| H-2 | idem | Wie foto's uploadt, "cede gratuitamente a la Empresa los derechos de explotación de propiedad intelectual sobre las mismas" (incl. watermerken tegen gebruik door derden) | Fotorechten liggen (ook) bij het portaal; derden hebben geen recht | idem | 2 |
| H-3 | idem | Geen clausule gevonden met "robot", "scrap" of "automat" (grep op volledige tekst, 15-09-2026) | Verbod op scraping volgt hier uit de IE-clausule en de wet, niet uit een robotclausule | idem | 3 |
| H-4 | idem, §12.1 | Spaans recht; rechter van de woonplaats van de gebruiker, anders Barcelona | — | idem | 2 |

### 2.3 pisos.com (HabitatSoft, S.L.)

| # | Clausule (letterlijk, kort) | Betekenis | URL | Type |
|---|---|---|---|---|
| P-1 | §3 "Propiedad Intelectual e Industrial": toegang geeft geen recht op "alteración, modificación, explotación, reproducción, distribución o comunicación pública"; de gebruiker gebruikt inhoud "para su propio uso y necesidades, y a no realizar en ningún caso una explotación comercial, directa o indirecta de los mismos" | Commerciële exploitatie van de inhoud is uitgesloten | https://www.pisos.com/avisolegal | 2 |
| P-2 | Publicatieregels: "Los datos personales proporcionados por el anunciante (nombre y el teléfono) … se publicarán de manera automática y serán visibles en el anuncio publicado." | **Particuliere advertenties bevatten naam en telefoon = persoonsgegevens** (zie §4.1) | idem | 2 |
| P-3 | DSA-sectie, "Última actualización: 30 de junio de 2026": gemiddeld 3.146.833 maandelijkse gebruikers | Ver onder de VLOP-drempel van 45 miljoen (DSA art. 33); geen DSA-toegangsroute | idem | 1 |
| P-4 | Geen robot- of scrapingclausule gevonden (grep op "robot", "scrap", "crawl") | Verbod volgt uit P-1 en de wet | idem | 3 |
| P-5 | robots.txt: `User-Agent: *` met o.a. `Disallow: /*.aspx`, `/WS/`; downloaders volledig uitgesloten | Geen licentie | https://www.pisos.com/robots.txt | 3 |

### 2.4 Kyero, Milanuncios, thinkSPAIN

| # | Bron | Bevinding | URL | Type |
|---|---|---|---|---|
| K-1 | Kyero Terms of use | curl: HTTP 403 met pagina "Checking your browser — Kyero"; WebFetch: 403. Niet omzeild. Een zoekresultaat met de titel "Kyero.com Terms of use. Updated 20-04-2026" vat samen dat systematische extractie of hergebruik "without prior written consent" en toegang via "robot, spider, scraper" verboden zijn | https://www.kyero.com/en/docs/terms/ | 7 (snippet) |
| K-2 | Kyero robots.txt | `User-agent: *`, `Crawl-delay: 1`, veel filterparameters uitgesloten (zie R03) | https://www.kyero.com/robots.txt | 3 |
| M-1 | Milanuncios robots.txt (15-09-2026) | Commentaar en regels: "AI training crawlers — blocked (content not licensed for model training)" voor GPTBot, ClaudeBot, Google-Extended, Amazonbot, CCBot en Bytespider (`Disallow: /`). "AI search/inference crawlers — allowed (search and RAG use permitted)" voor OAI-SearchBot, ChatGPT-User en Claude-SearchBot, met uitsluiting van o.a. `/datos-contacto/`, `/contacta/`, `/api/` | https://www.milanuncios.com/robots.txt | 3 |
| M-2 | Voorwaarden Milanuncios | Niet leesbaar (R02: 403 met botbeveiliging). Niet opnieuw geprobeerd | https://www.milanuncios.com/legal/condiciones-uso | 7 |
| T-1 | thinkSPAIN legal info (uit R03) | Inhoud eigendom van Think Web Content SL; transmissie, reproductie en opslag vragen "express written consent" | https://www.thinkspain.com/legal-info | 2 (R03) |

**Gevolgtrekking M-1 (type 4):** dit is een machineleesbaar voorbehoud in de zin van RDL 24/2021 art. 67.3 tegen AI-training. Het toestaan van "search/RAG"-crawlers geldt voor de genoemde user-agents van die AI-bedrijven. Het is **geen** toestemming voor een eigen scraper van TREE.

### 2.5 BOE-veilingportaal, BOE-hergebruik, Registro Público Concursal

| # | Bron | Clausule of feit (letterlijk, kort) | Betekenis | URL | Type |
|---|---|---|---|---|---|
| B-1 | robots.txt subastas.boe.es (15-09-2026) | `User-agent: *` / `Disallow: /` | Geen enkele robot toegestaan | https://subastas.boe.es/robots.txt | 3 |
| B-2 | Ley 19/2015, DA 2ª.2 | "Los sistemas de búsqueda que implante la Agencia Estatal Boletín Oficial del Estado contarán con los mecanismos necesarios para evitar la indexación y recuperación automática de los anuncios de subasta electrónica por medio de motores de búsqueda desde Internet." | Wettelijke basis voor de robotblokkade; doel is bescherming van persoonsgegevens | https://www.boe.es/buscar/act.php?id=BOE-A-2015-7851 | 2 |
| B-3 | Help van het portaal | Registratie vereist "que acepte las condiciones de uso del portal"; die tekst is zonder registratie niet gezien | Voorwaarden voor geregistreerde gebruikers ONBEKEND **[te verifiëren bij registratie door Jan]** | https://subastas.boe.es/ayuda.php | 2 / 7 |
| B-4 | Aviso legal AEBOE, "Condiciones de reutilización" (licencia tipo, Resolución 27-06-2024, eficacia 28-06-2024) | Hergebruik toegestaan "para fines comerciales y no comerciales", inclusief "extracción, reordenación y combinación de la información"; verplichte vermelding "Fuente de los datos: Agencia Estatal Boletín Oficial del Estado" of "Basado en datos de la Agencia Estatal Boletín Oficial del Estado", met link naar boe.es | Commercieel hergebruik van BOE-documenten is uitdrukkelijk toegestaan | https://www.boe.es/informacion/aviso_legal/index.php | 2 |
| B-5 | idem | "Cuando los documentos contengan datos de carácter personal, su reutilización deberá realizarse con pleno respeto al Reglamento (UE) 2016/679 … y a la Ley Orgánica 3/2018"; verboden "desnaturalizar el sentido"; geen suggestie van officieel karakter; AEBOE kan toegang "denegar o suspender … sin previo aviso" | De licentie dekt geen AVG-schending | idem | 2 |
| B-6 | idem, "Primera. Ámbito" | Geldt "con carácter general a los documentos alojados en la sede electrónica" van de AEBOE | **Of subastas.boe.es daaronder valt, staat er niet** — gezien B-1 en B-2 afgeleid: niet voor geautomatiseerde raadpleging van het portaal (type 4) | idem | 2 / 4 |
| B-7 | robots.txt boe.es (15-09-2026) | `Disallow: /boe_n/`, `/notificaciones/`, `/boe_j/`, `/edictos_judiciales/`, `/buscar/edictos_judiciales.php?` e.a. | Notificaties en gerechtelijke edicten zijn bewust uitgesloten van indexering; gebruik de open-data-API en RSS (R08) | https://www.boe.es/robots.txt | 3 |
| R-1 | Aviso legal Registro Público Concursal, §VII | "Queda expresamente prohibida su reutilización, tratamiento ulterior, cesión a terceros o utilización para fines distintos a los indicados." | Persoonsgegevens uit het RPC mogen niet in Deal Hunter worden opgenomen | https://www.publicidadconcursal.es/aviso-legal | 2 |
| R-2 | idem, §IV | Verboden: "indexaciones o robotizaciones del sitio Web del RPC, con el fin de recuperar automáticamente los datos" | Alleen handmatig | idem | 2 |

### 2.6 Background Properties (partnerfeed)

| # | Clausule (letterlijk, kort) | Betekenis | URL | Type |
|---|---|---|---|---|
| BP-1 | "la reproducción total o parcial, uso, explotación, distribución y comercialización, requiere en todo caso de la autorización escrita previa por parte del prestador" | Elk gebruik buiten wat BP schriftelijk toestaat is formeel onbevoegd | https://backgroundproperties.com/aviso-legal/ | 2 (bevestigd 15-09-2026; ook R05) |
| BP-2 | "El prestador NO AUTORIZA expresamente a que terceros puedan redirigir directamente a los contenidos concretos del sitio web" | Kan op hotlinken van foto's slaan **[advocaat / BP vragen]** | idem | 2 |
| BP-3 | Spaans recht; "Juzgados y Tribunales de ELCHE" | — | idem | 2 |
| BP-4 | Geen feedvoorwaarden en geen schriftelijke overeenkomst gevonden (R05, negatieve bevinding) | De rechten voor de website berusten op het feit dat BP de feed verstrekte, niet op een document | R05 | 3 / 7 |
| BP-5 | Lokale controle van 56 BP-objecten in Jávea (eigen dienst, 15-09-2026): in de omschrijvingen (5 talen) **0** e-mailadressen en **0** Spaanse telefoonnummerpatronen | De feed bevat in dit deel geen contactgegevens; foto's kunnen wel personen of interieurs bevatten (niet gecontroleerd) | http://127.0.0.1:3100/api/properties?town=Javea&limit=100 | 3 |

### 2.7 Catastro en Registro de la Propiedad

| # | Bron | Clausule of wettekst (letterlijk, kort) | Betekenis | URL | Type |
|---|---|---|---|---|---|
| C-1 | Licencia de acceso y uso de los servicios y conjuntos de datos INSPIRE (DG Catastro, versie 1.0, juli 2016) | Toegang tot de webdiensten "se autoriza para uso propio del usuario titular de la licencia, o para la elaboración y distribución de nuevos productos de valor añadido … siempre que ésta sea transformada"; "no se autoriza la difusión, distribución o comercialización de la información original" | Intern gebruik en afgeleide producten: ja. Kale doorlevering: nee | https://www.catastro.hacienda.gob.es/webinspire/documentos/Licencia.pdf | 2 |
| C-2 | idem | Dienst kan worden onderbroken bij een gebruik waarvan de "intensidad, frecuencia" de andere gebruikers schaadt; nieuwe producten mogen zich niet voordoen als "cartografía catastral" of "información catastral" | Rate limits respecteren; eigen kaarten niet zo noemen | idem | 2 |
| C-3 | TRLCI art. 51 | Beschermde gegevens: "el nombre, apellidos, razón social, código de identificación y domicilio" van de titularissen, plus "el valor catastral" | Eigenaarsnaam en kadastrale waarde vallen buiten de vrije diensten | https://www.boe.es/buscar/act.php?id=BOE-A-2004-4163 | 2 |
| C-4 | TRLCI art. 53.1 | Toegang tot beschermde gegevens alleen met "consentimiento expreso, específico y por escrito del afectado" of in limitatief opgesomde gevallen (o.a. notarissen/registradores, aangrenzende eigenaren, zakelijk gerechtigden, erfgenamen) | Een potentiële koper staat niet in die lijst (afgeleid, type 4) | idem | 2 |
| RP-1 | Ley Hipotecaria art. 221 | Registers zijn openbaar "para quienes tengan interés conocido en averiguar el estado de los bienes inmuebles o derechos reales inscritos" | Nota simple per object bij legitiem belang | https://www.boe.es/buscar/act.php?id=BOE-A-1946-2453 | 2 |
| RP-2 | Ley Hipotecaria art. 222.2 | Publiciteit "asegurando, al mismo tiempo, la imposibilidad de su manipulación o televaciado" | Geen bulk-overname | idem | 2 |
| RP-3 | Reglamento Hipotecario art. 332.2 | Verboden is directe toegang tot de databank van de registrador "así como su incorporación a base de datos para su comercialización o reventa" | Eigendoms- en lastengegevens niet in een doorverkoopbare of commerciële databank | https://www.boe.es/buscar/act.php?id=BOE-A-1947-3843 | 2 |
| RP-4 | Reglamento Hipotecario art. 332.3 | Legitiem belang vermoed bij o.a. "agentes de la propiedad inmobiliaria … siempre que expresen la causa de la consulta y ésta sea acorde con la finalidad del Registro" | TREE Properties kan als makelaar aanvragen, met opgave van reden | idem | 2 |

---

## 3. (b) Spaans en EU-recht

### 3.1 Sui-generisdatabankrecht (TRLPI art. 133 e.v.; Richtlijn 96/9)

| Regel | Wettekst (gezien) | Wat het voor Deal Hunter betekent (afgeleid, type 4) |
|---|---|---|
| Wat beschermd is | Art. 133.1: beschermt "la inversión sustancial … para la obtención, verificación o presentación de su contenido"; de fabrikant kan "la extracción y/o reutilización de la totalidad o de una parte sustancial" verbieden | Portalen die advertenties verzamelen, controleren en presenteren kunnen dit recht hebben; per portaal feitelijk te bewijzen |
| Herhaald en systematisch | Art. 133.2: niet toegestaan zijn "la extracción y/o reutilización repetidas o sistemáticas de partes no sustanciales" die in strijd zijn met normale exploitatie of de fabrikant onredelijk schaden | **Kern voor Deal Hunter:** een dagelijkse automatische kopie van "maar" het Jávea-deel kan hieronder vallen, ook als elk deel klein is |
| Extractie ≠ publiceren | Art. 133.3.b: extractie = "la transferencia permanente o temporal … a otro soporte"; art. 133.3.c: hergebruik = "puesta a disposición del público" | Alleen al het overzetten naar onze eigen database is extractie; publicatie is niet nodig voor inbreuk |
| Rechtmatige gebruiker | Art. 134.1: de fabrikant kan de rechtmatige gebruiker niet beletten "extraer y/o reutilizar partes no sustanciales … con independencia del fin"; art. 134.3: "Cualquier pacto en contrario … será nulo de pleno derecho" (EU: art. 8 en 15) | Handmatig een paar feiten van een advertentie noteren voor eigen beoordeling is een wettelijk recht, dat voorwaarden niet kunnen wegnemen **[advocaat]** |
| Grenzen | Art. 134.2: geen handelingen "contrarios a una explotación normal" of die rechthebbenden op werken in de databank (foto's, teksten) schaden | Het recht op niet-substantiële delen dekt niet het kopiëren van foto's |
| Uitzonderingen | Art. 135.1: alleen privé (niet-elektronisch), onderwijs/wetenschappelijk onderzoek "no comercial", openbare veiligheid of procedure | Geen uitzondering voor commerciële analyse |
| Duur | Art. 136: 15 jaar; elke substantiële wijziging start een nieuwe termijn | Dagelijks bijgewerkte portaldatabanken blijven feitelijk doorlopend beschermd |
| Andere regels blijven gelden | Art. 137: onverminderd o.a. "derecho contractual" en "protección de los datos de carácter personal" | Databankrecht, contract en AVG gelden naast elkaar |

**HvJ-rechtspraak (dictum gezien via ipcuria.eu; EUR-Lex geblokkeerd; type 2, vindplaats secundair):**

| Zaak | Kern | Relevantie |
|---|---|---|
| C-203/02 BHB v William Hill, 09-11-2004 | Investering in "obtaining" = middelen om bestaande gegevens te zoeken en te verzamelen, **niet** de middelen om de gegevens zelf te creëren | Een portaal creëert advertenties niet zelf, maar verzamelt ze. Dat pleit ervoor dat portalen wél een beschermde investering hebben (type 4) |
| C-202/12 Innoweb v Wegener, 19-12-2013 | Een "dedicated meta search engine" die zoekvragen realtime doorvertaalt en resultaten in eigen opmaak toont, is hergebruik van (een substantieel deel van) de databank | Een eigen zoek- en alertlaag bovenop een portaal is risicovol |
| C-762/19 CV-Online Latvia v Melons, 03-06-2021 | Kopiëren en indexeren van (een substantieel deel van) een vrij toegankelijke databank is extractie en hergebruik, te verbieden als het een risico vormt voor de terugverdiening van de investering; belangenafweging met toegang tot informatie | Beslissend criterium is het risico voor het verdienmodel van het portaal. idealista/data en DataVenues verkopen juist deze data (R01, R02). Afgeleid: **reëel risico** |
| C-30/14 Ryanair v PR Aviation, 15-01-2015 | De richtlijn is niet van toepassing op een databank zonder auteursrecht- of sui-generisbescherming; artt. 6(1), 8 en 15 beletten dan niet dat de maker **contractuele beperkingen** oplegt | Is een portaal niet beschermd, dan vervalt het wettelijke recht op niet-substantiële delen en gelden de voorwaarden (Idealista I-1/I-3) volledig, voor zover ze naar Spaans recht binden **[advocaat]** |

### 3.2 Auteursrecht op advertentieteksten en foto's

| Regel | Wettekst (gezien, TRLPI) | Betekenis (afgeleid) |
|---|---|---|
| Werken | Art. 10.1: beschermd zijn "creaciones originales", o.a. (a) geschriften, (f) "proyectos, planos … de obras arquitectónicas", (h) "obras fotográficas" | Originele advertentieteksten, plattegronden en ontwerpfoto's zijn werken; kale opsommingen (m², kamers) meestal niet |
| Meras fotografías | Art. 128: ook een niet-originele foto geeft "el derecho exclusivo de autorizar su reproducción, distribución y comunicación pública", 25 jaar | **Elke** vastgoedfoto is minstens 25 jaar beschermd |
| Reproductie | Art. 18: "la fijación directa o indirecta, provisional o permanente, por cualquier medio … de toda la obra o de parte de ella" | Een foto downloaden en in een cache zetten om te analyseren of te hashen is een reproductie |
| Tijdelijke kopie | Art. 31.1: vrij zijn tijdelijke reproducties zonder zelfstandige economische betekenis, "transitorios o accesorios", met als enig doel "una utilización lícita, entendiendo por tal la autorizada por el autor o por la ley" | Het tonen in de browser of de sessie van een medewerker valt hieronder; een bewaarde kopie of een verwerkingsketen buiten die toegestane weergave waarschijnlijk niet **[advocaat]** |
| Copia privada | Art. 31.2: alleen natuurlijke persoon, "no profesional ni empresarial"; art. 31.3.b sluit elektronische databanken uit | Niet bruikbaar voor TREE |
| Citaat | Art. 32.1: alleen "con fines docentes o de investigación" | Niet bruikbaar voor commerciële dossiers |
| Transformatie | Art. 21: vertaling, bewerking; bij databanken ook "la reordenación" | Een AI-herschrijving van een advertentietekst die als eigen tekst wordt gebruikt, is een bewerking |
| Uitzondering voor officiële teksten | Art. 13: wetten, "resoluciones de los órganos jurisdiccionales" en handelingen van publieke organen zijn niet beschermd | BOE-wetteksten en uitspraken zijn vrij van auteursrecht; persoonsgegevens en databankrecht blijven wel spelen |
| Medeaansprakelijkheid | Art. 138: aansprakelijk is ook wie meewerkt of "teniendo un interés económico directo … cuente con una capacidad de control sobre la conducta del infractor" | **Een ingehuurde scraperdienst (Apify e.a.) maakt TREE niet onschuldig** |

### 3.3 Tekst- en datamining (RDL 24/2021, art. 66–67)

- Art. 66.1 definieert TDM als "toda técnica analítica automatizada destinada a analizar textos y datos en formato digital a fin de generar información que incluye pautas, tendencias, correlaciones" (type 2).
- Art. 67.1: geen toestemming nodig "para las reproducciones de obras y otras prestaciones accesibles de forma legítima realizadas con fines de minería de textos y datos". Art. 67.7 geeft de rechtmatige gebruiker hetzelfde voor substantiële delen van een databank (type 2).
- Art. 67.2: bewaren mag "durante todo el tiempo que sea necesario", met respect voor de gegevensbescherming (type 2).
- Art. 67.3: de uitzondering vervalt "cuando los titulares de derechos hayan reservado expresamente el uso de las obras a medios de lectura mecánica u otros medios que resulten adecuados" (type 2).

**Gevolgtrekking (type 4) [advocaat]:**
- (a) "Accesibles de forma legítima": geautomatiseerde toegang die de voorwaarden schendt, is waarschijnlijk niet legitiem.
- (b) Idealista reserveert in zijn voorwaarden uitdrukkelijk tegen "monitorizar (spider, scrape)" en "guardar". Of een voorbehoud in voorwaarden "adecuado" is, is omstreden. Milanuncios doet het machineleesbaar (M-1).
- (c) De uitzondering dekt alleen reproductie voor analyse. Dossiers met foto's en teksten tonen aan klanten valt er niet onder.
- (d) Per-object-analyse ("heeft dít huis renovatie nodig?") past minder goed bij "pautas, tendencias, correlaciones" dan marktanalyse.

Conclusie: TDM is een argument voor interne analyse van **rechtmatig verkregen** content, zoals BP-content met akkoord. Het is geen basis om portalen te scrapen.

### 3.4 Rechtspraak over screen scraping

| Uitspraak | Wat vaststaat | Bron | Type |
|---|---|---|---|
| TS (Sala Civil) 572/2012, 09-10-2012, Ryanair v Atrápalo | Vorderingen van Ryanair afgewezen; lagere rechters oordeelden dat er geen databank in de zin van de wet was, alleen een computerprogramma; Ryanairs investering betrof het **genereren** van eigen vluchtgegevens; geen oneerlijke mededinging; in eerste aanleg geen contract via de websitevoorwaarden. Het TS deed geen uitspraak over de rechtmatigheid van scraping als zodanig. | LegalToday (S. García Sánchez, 14-01-2013), secundair; CENDOJ niet bereikbaar | 7 |
| TS (Sala Civil) 09-04-2014, Ryanair v online-reisbureau | Volgens de CGPJ-perskennis gedeeltelijk toegewezen voor Ryanair: een clausule over rechtstreeks boeken is niet in strijd met de goede trouw; wel oneerlijke denigratie door Ryanair. Geen overweging over scraping of databanken in de perskennis | https://www.poderjudicial.es/cgpj/en/Judiciary/Pressroom/News-archive/El-TS-estima-parcialmente-un-recurso-de-Ryanair-contra-una-agencia-de-viajes-on-line-por-las-clausulas-de-contratacion | 2 (perskennis) |
| Top Rural (Juzgado Mercantil Madrid, 20-06-2007) | Secundaire bronnen spreken elkaar tegen (civiel "geen oneerlijke mededinging" vs. strafrechtelijke "absolución") | artiureabogados.com; maestreabogados.com | 7 |
| Uitspraak "Idealista/Fotocasa tegen scraper" | **Niet gevonden** (twee gerichte zoekopdrachten, 15-09-2026) | — | 7 |

**Belangrijk verschil (type 4):** de Ryanair-lijn gaat over een aanbieder die eigen data creëert, en dat valt buiten het databankrecht (BHB). Vastgoedportalen **verzamelen** data van derden. Na C-202/12 en C-762/19 is het risico voor wie portalen systematisch kopieert daarom groter dan Ryanair/Atrápalo doet vermoeden.

### 3.5 Oneerlijke mededinging en strafrecht

- **Ley 3/1991 art. 11.2:** imitatie is oneerlijk als ze "comporte un aprovechamiento indebido de la reputación o el esfuerzo ajeno" (type 2). Een vergelijkbare dienst op basis van portaaldata kan hieronder vallen (type 4).
- **Código Penal art. 197 bis.1:** strafbaar is toegang tot een informatiesysteem "vulnerando las medidas de seguridad establecidas para impedirlo" (6 maanden tot 2 jaar) (type 2). Botbeveiliging omzeilen (Akamai/Cloudflare, "Checking your browser", captcha) is daarom geen civiele kwestie meer **[advocaat]**. Harde regel: nooit omzeilen, ook niet via derden.

### 3.6 Digital Services Act en Data Act

- **DSA art. 40.12:** zeer grote platforms moeten publiek toegankelijke data geven aan onderzoekers die voldoen aan art. 40.8 b–e, uitsluitend voor onderzoek naar systeemrisico's (art. 34). Art. 33.1: de drempel is "cuarenta y cinco millones" gemiddelde maandelijkse actieve ontvangers in de EU (type 2). TREE is geen onderzoeker in die zin. pisos.com meldt 3,1 miljoen gebruikers (P-3). Of Idealista als VLOP is aangewezen, is ONBEKEND. Conclusie: **geen toegangsroute** (type 4).
- **Data Act (Verordening 2023/2854) art. 43:** het sui-generisrecht geldt niet voor databanken met gegevens "obtenidos o generados por un producto conectado". De verordening gaat over data van verbonden producten en diensten (art. 1) (type 2). Portaaladvertenties vallen daar niet onder (type 4): **niet relevant** voor portaaltoegang.

### 3.7 AI-verordening (Verordening 2024/1689)

| Artikel | Tekst (gezien, BOE-DOUE-kopie) | Relevantie |
|---|---|---|
| Art. 4 | Aanbieders en "responsables del despliegue" zorgen voor "un nivel suficiente de alfabetización en materia de IA" van hun personeel | Geldt voor TREE als gebruiker van Claude en eigen AI-analyse; vastleggen wie getraind is |
| Art. 5.1.e | Verboden zijn AI-systemen "que creen o amplíen bases de datos de reconocimiento facial mediante la extracción no selectiva de imágenes faciales de internet" | Beeldanalyse en hashing nooit gebruiken om personen op foto's te herkennen; personen niet indexeren |
| Art. 50.4 | Wie beelden genereert of manipuleert die een "ultrasuplantación" vormen, maakt dat bekend | Relevant als Deal Hunter renovatievisualisaties maakt voor klanten |
| Art. 113 | Van toepassing vanaf 02-08-2026; hoofdstuk I–II vanaf 02-02-2025; art. 6.1 vanaf 02-08-2027 | Stand volgens de oorspronkelijke tekst; latere wijzigingen ("digital omnibus") **[te verifiëren]** |

Afgeleid (type 4): vastgoedselectie en renovatieanalyse zijn geen hoog-risicotoepassing in de zin van bijlage III. Dat heb ik niet artikelsgewijs gecontroleerd **[te verifiëren]**.

### 3.8 "Raadplegen voor eigen beoordeling" versus "opslaan, verrijken, doorleveren"

| Handeling | Juridische haak | Portaal zonder licentie | Met licentie of toestemming (BP) |
|---|---|---|---|
| 1. Advertentie bekijken in browser of assistentsessie | TRLPI 31.1; voorwaarden staan navigeren toe | Toegestaan | Toegestaan |
| 2. Link + portaal-ID + eigen notities bewaren | Geen reproductie van werk; minimale gegevens | Toegestaan (type 4) | Toegestaan |
| 3. Enkele feiten handmatig noteren (vraagprijs op datum, m², type) | Feiten geen werk; art. 134.1 (niet-substantieel) | Verdedigbaar **[advocaat]** | Toegestaan |
| 4. Schermafdruk of pdf als bewijs in één dossier | Reproductie (art. 18) | Grijs; hooguit als intern bewijsstuk, niet delen **[advocaat]** | Volgens akkoord |
| 5. Automatisch dagelijks ophalen | Voorwaarden I-1/I-3; art. 133.2; art. 197 bis bij omzeiling | **Niet toegestaan** | Toegestaan (feed) |
| 6. Opslaan en historie opbouwen (prijsverloop) | "guardar" (I-3); art. 133.2/133.3.b | **Niet toegestaan** | Pas na schriftelijke bevestiging |
| 7. Tekst en foto's met AI analyseren buiten de sessie | Reproductie; TDM art. 67 met voorbehoud | **Niet toegestaan** | Pas na schriftelijke bevestiging |
| 8. Beeldhashes berekenen en bewaren | Download = reproductie; hash zelf vermoedelijk geen reproductie (niet terug te rekenen) | **Niet toegestaan** (de download is het probleem) | Pas na schriftelijke bevestiging |
| 9. Verrijken met Catastro/BOE-data | Open licenties (C-1, B-4) | Alleen op eigen objectrecords zonder portaalcontent | Toegestaan |
| 10. Dossier met foto's/tekst naar klant of investeerder | Reproductie + distributie/mededeling; hergebruik (133.3.c) | **Niet toegestaan**; alleen link doorsturen | Pas na schriftelijke bevestiging |
| 11. Publiceren op een TREE-website | Mededeling aan het publiek | **Niet toegestaan** | Alleen treeproperties.es, voor zover bevestigd |

---

## 4. (c) AVG/LOPDGDD en LSSI-CE

### 4.1 Wanneer zijn advertentie- en brongegevens persoonsgegevens?

| Gegevens | Persoonsgegeven? | Onderbouwing | Type |
|---|---|---|---|
| Naam, e-mail, telefoon van een **particuliere** adverteerder | Ja | pisos.com publiceert "nombre y el teléfono" automatisch (P-2); Idealista-assistent geeft `userType` private/professional (R01) | 2 / 3 |
| Contactgegevens van een medewerker van een makelaarskantoor, of van een zelfstandige makelaar in die hoedanigheid | Ja, maar met wettelijk vermoeden van rechtmatigheid | LOPDGDD art. 19.1: vermoed onder AVG 6.1.f als het gaat om "datos necesarios para su localización profesional" en het doel "únicamente mantener relaciones" met de rechtspersoon is; art. 19.2 geldt ook voor "empresarios individuales y … profesionales liberales" | 2 |
| Objectgegevens (prijs, m², foto's van interieur) zonder koppeling aan een persoon | Meestal niet | Type 4; wordt wél persoonsgegeven zodra het object via adres, kadaster of registro aan een identificeerbare eigenaar is te koppelen | 4 |
| Exacte coördinaten of adres van een woning van een particuliere verkoper | Waarschijnlijk ja (identificeerbaar via Catastro/Registro) | Type 4 **[advocaat]** | 4 |
| Namen van schuldenaren, geëxecuteerden of eigenaren in edictos, veilingen, RPC en nota simple | Ja; bovendien gegevens over "situación financiera o de solvencia patrimonial" | AEPD EIPD-lijst criterium 4 (§4.4) | 2 |
| Foto's waarop personen herkenbaar zijn | Ja | Type 4; AI-verordening art. 5.1.e bij gezichtsherkenning | 4 |

### 4.2 Rechtsgrond en voorwaarden

- **AVG art. 5.1:** "limitación de la finalidad" (b), "minimización de datos" (c) en "limitación del plazo de conservación" (e) (type 2).
- **AVG art. 6.1.f:** gerechtvaardigd belang, "siempre que sobre dichos intereses no prevalezcan los intereses o los derechos y libertades fundamentales del interesado" (type 2). Voor TREE is dit de enige realistische grondslag voor gegevens uit openbare bronnen (type 4).
- **HvJ C-621/22 (04-10-2024), dictum:** een commercieel belang kan een gerechtvaardigd belang zijn, "only on condition that that processing is strictly necessary" en de belangen van betrokkenen niet zwaarder wegen; het belang moet "lawful" zijn (type 2, vindplaats ipcuria.eu). ECLI-nummer niet opgenomen: bronnen noemen :857 en :858 (type 7).
- **AEPD, criterium AI-00059-2024** ("Herramientas de data scraping para la evaluación de tendencias", gepubliceerd 25-11-2025): scraping "cuando recopila datos personales, sí implica un tratamiento"; zaak geseponeerd omdat alleen geaggregeerde informatie zonder identificeerbare personen werd getoond (type 2).
- **EDPB Guidelines 03/2026 on web scraping in the context of generative AI** (versie 1.0, aangenomen 07-07-2026 **voor publieke consultatie**; scope: training van generatieve AI, dus analoog en niet rechtstreeks van toepassing): minimalisatie door o.a. "exclude from the collection websites which clearly oppose the scraping of their content" (robots.txt, ai.txt, captcha); "the absence or non-applicability of a robots.txt file … does not amount to consent" (type 2).
- **Autoriteit Persoonsgegevens (NL), Handreiking scraping (mei 2024, versie april 2025):** alleen via zoekmachine, pdf en pagina gaven 403. Kern volgens snippets: scraping door private partijen "bijna nooit" toegestaan, alleen zeer gericht. Niet de Spaanse toezichthouder (type 7).

**Gevolgtrekking (type 4):** een belangenafweging (LIA) is verdedigbaar voor een **objectgericht** systeem dat geen persoonsgegevens van particulieren bewaart en makelaars alleen zakelijk registreert (art. 19). Ze is niet verdedigbaar voor een systeem dat eigenaars- of schuldenaarsprofielen opbouwt. Die zijn door de masterprompt ook uitgesloten.

### 4.3 Informatieplicht (AVG art. 14)

- Worden persoonsgegevens niet bij de betrokkene verkregen, dan moet o.a. "la fuente de la que proceden los datos personales y, en su caso, si proceden de fuentes de acceso público" worden gemeld (art. 14.2.f). Dat gebeurt binnen een maand, bij de eerste communicatie, of bij doorgifte (art. 14.3) (type 2).
- Uitzondering bij "esfuerzo desproporcionado", mits "medidas adecuadas … inclusive haciendo pública la información" (art. 14.5.b) (type 2).
- Afgeleid (type 4): wie makelaarscontacten in GoHighLevel zet, moet bij het eerste contact informeren. Wie geen persoonsgegevens van particulieren opslaat, heeft dit probleem niet: nog een reden om ze niet op te slaan.

### 4.4 DPIA (AVG art. 35; AEPD-lijst art. 35.4)

- Art. 35.1: verplicht bij "alto riesgo", "en particular si utiliza nuevas tecnologías" (type 2).
- AEPD-lijst: in "la mayoría de los casos" een DPIA bij **twee of meer** criteria (type 2). Relevant zijn:
  - **4.** gegevens die "la situación financiera o de solvencia patrimonial" laten zien;
  - **8.** "la asociación, combinación o enlace de registros de bases de datos de dos o más tratamientos con finalidades diferentes o por responsables distintos";
  - **10.** "nuevas tecnologías o un uso innovador".
- **Gevolgtrekking (type 4):**
  - Een veilingmodule die BOE-, Registro- en portaaldata aan objecten koppelt en met AI analyseert, raakt criteria 4, 8 en 10: **DPIA vereist** zodra er persoonsgegevens in zitten.
  - Een puur objectgerichte module zonder persoonsgegevens: geen DPIA, wel een vastgelegde afweging waarom niet.

### 4.5 BOE-edictos, veilingen, Registro, Catastro: doelbinding en het verbod op persoonsprofielen

1. **Publicatieregime.** LOPDGDD DA 7ª.1: in publicaties van bestuurshandelingen wordt de betrokkene aangeduid met naam plus vier willekeurige cijfers van het identiteitsdocument; in notificatie-anuncios alleen met het volledige documentnummer; "En ningún caso debe publicarse el nombre y apellidos de manera conjunta con el número completo" (type 2). Dit regime beperkt identificeerbaarheid; afgeleid: het doel is notificatie, niet hergebruik.
2. **Veilingportaal.** Ley 19/2015 DA 2ª.2 verplicht maatregelen tegen indexering en "recuperación automática" (B-2) (type 2).
3. **AEPD E/04809/2015 (subastafacil.com).**
   - Feiten: een commerciële site herpubliceerde veilingedicten met namen van geëxecuteerden, Google-vindbaar. Premiumgebruikers kregen "DATOS PERSONALES DEL DEUDOR para que lo puedas localizar y negociar con él".
   - Uitkomst: geseponeerd nadat de site indexering blokkeerde en gegevens op verzoek verwijderde. De AEPD verwees naar DA 2ª Ley 19/2015 als maatstaf.
   - Toen gold het oude LOPD-regime (type 2).
   - **Gevolgtrekking (type 4):** een sepot onder oud recht is geen vrijbrief. Het laat zien dat vindbaarheid en het benaderen van schuldenaren het risicopunt zijn.
4. **RPC.** Hergebruik van persoonsgegevens uitdrukkelijk verboden (R-1) (type 2).
5. **Registro.** Geen databank voor commercialisering (RP-3); publiciteit alleen voor een legitiem belang (RP-1, RP-4) (type 2).
6. **Catastro.** Eigenaarsnaam en kadastrale waarde zijn beschermd (C-3, C-4) (type 2).
7. **Ley 37/2007.** Art. 4.6: hergebruik van documenten met persoonsgegevens valt onder de LOPDGDD. Art. 3.3.k sluit documenten uit waarvan de toegang beperkt is om redenen van gegevensbescherming (type 2).

**Ontwerpregels (type 4, masterprompt §4, §26 en CLAUDE.md regel 4):**
- In de database staan **objecten**, geen personen: veiling-ID, lot, waarde, depósito, situación posesoria, rechtbank, termijnen.
- **Geen** namen van schuldenaren of eigenaren in doorzoekbare velden, geen koppeling persoon↔object over bronnen heen, geen zoekfunctie op naam.
- Is voor due diligence van een **concreet** bod een naam nodig (bijv. om de nota simple te matchen), dan alleen in het afgeschermde dossier, met een reden en een verwijderdatum (§4.6).
- Geen benadering van schuldenaren of geëxecuteerden op basis van edictos zonder juridisch akkoord **[advocaat]**. Doelbinding: de publicatie dient de veiling, niet onze acquisitie.

### 4.6 Bewaartermijnen en blokkering

| Regel | Tekst (gezien) | Type |
|---|---|---|
| AVG art. 5.1.e | Niet langer bewaren "del necesario para los fines del tratamiento" | 2 |
| LOPDGDD art. 32 | Bij verwijdering eerst **blokkeren**: alleen beschikbaar voor rechters, OM en toezichthouders, "solo por el plazo de prescripción"; daarna vernietigen | 2 |
| LOPDGDD art. 72–74 | Verjaring: zeer ernstig 3 jaar, ernstig 2 jaar, licht 1 jaar | 2 |
| Código Civil art. 1964.2 | Persoonlijke vorderingen zonder bijzondere termijn: 5 jaar | 2 |

De voorgestelde termijnen per brontype staan in §6.2 (werkhypothese, type 4).

### 4.7 Ongevraagde commerciële communicatie

**Wettelijk kader (gezien, type 2):**
- **LSSI bijlage f:** "Comunicación comercial" = elke communicatie "dirigida a la promoción, directa o indirecta, de la imagen o de los bienes o servicios de una empresa". **Bijlage d:** "Destinatario" = "persona física o jurídica".
- **LSSI art. 20.1:** elektronische commerciële communicatie "claramente identificables como tales", met herkenbare afzender.
- **LSSI art. 21.1:** verboden zijn reclame- of promotieberichten per "correo electrónico u otro medio de comunicación electrónica equivalente que previamente no hubieran sido solicitadas o expresamente autorizadas". Art. 21.2: uitzondering bij een eerdere contractuele relatie en soortgelijke eigen producten, met een eenvoudige en kosteloze afmeldmogelijkheid.
- **LSSI art. 22.1:** intrekking van toestemming moet eenvoudig en kosteloos; bij e-mail met een geldig e-mailadres.
- **LSSI art. 38–39:** massaal of "insistente o sistemático" versturen zonder art. 21 is **ernstig** (30.001–150.000 €); anders licht (tot 30.000 €).
- **Ley 11/2022 (LGT) art. 66.1:** (a) geen automatische oproepen zonder menselijke tussenkomst zonder voorafgaande toestemming; (b) geen "llamadas no deseadas con fines de comunicación comercial", tenzij toestemming of een andere grondslag van AVG art. 6.1.
- **Circular AEPD 1/2023 (26-06-2023, BOE 28-06-2023, niet ingetrokken of vernietigd volgens BOE-metadata 15-09-2026):**
  - Gerechtvaardigd belang is mogelijk, met een vooraf vastgelegde afweging (art. 3).
  - De AEPD vermoedt **geen** redelijke verwachting "en aquellos casos en los que no exista relación contractual vigente, solicitud o interacción previa y realizada durante el último año".
  - Robinson-systemen raadplegen (art. 4); art. 19 LOPDGDD voor professionals (art. 5).
  - Elk gesprek begint met identiteit, commercieel doel en opt-out; elke afwijzing is directe intrekking; opname als bewijs (art. 6).
- **LOPDGDD art. 23** (lid 1 gewijzigd door DF 4ª Ley 10/2025, van kracht 28-12-2025): wie direct marketing doet, moet "previamente consultar los sistemas de exclusión publicitaria" (art. 23.4), tenzij toestemming.

**Matrix per kanaal en doelgroep (gevolgtrekking, type 4; [advocaat] waar vermeld):**

| Kanaal | Makelaarskantoor (rechtspersoon, zakelijk adres) | Zelfstandige makelaar | Particuliere eigenaar/adverteerder | Schuldenaar/geëxecuteerde (uit edicto of veiling) |
|---|---|---|---|---|
| E-mail, WhatsApp, sms (commercieel: samenwerking, onze diensten) | **Voorafgaande toestemming nodig** (LSSI 21 + bijlage d); uitzondering alleen bij een bestaande klantrelatie (21.2) | Idem | **Voorafgaande toestemming nodig**; geen massa-automatisering (masterprompt §26) | **Niet doen** |
| E-mail of portaalformulier als **geïnteresseerde koper over dát object** (geen promotie van onze diensten) | Toegestaan: reactie op aanbod, geen "comunicación comercial" (type 4) **[advocaat]** | Idem | Verdedigbaar via het portaalformulier (Idealista I-1: "Contactar con los anunciantes de los inmuebles por los que estés interesado") **[advocaat]** | n.v.t. |
| Telefoon (commercieel) | Mogelijk op art. 19 LOPDGDD + Circular art. 5, met opt-out aan het begin | Idem | Alleen met gedocumenteerde LIA, Robinson-controle en opt-out; **geen** koude acquisitiebelrondes; zonder eerder contact vermoedt de AEPD geen redelijke verwachting (Circular art. 3) | **Niet doen** |
| Idealista-doorschakelnummer uit de assistent | Alleen voor vragen over dat object | Idem | Alleen voor vragen over dat object; niet voor het aanbieden van diensten | n.v.t. |
| Brief per post | Toegestaan met afzender en opt-out (AVG 6.1.f, art. 21 AVG) | Idem | Alleen met een rechtmatig verkregen adres: Catastro-naam beschermd (C-3), Registro niet voor marketing (RP-3). **Praktisch geen rechtmatige bron** **[advocaat]** | **Niet doen** |
| Officiële kanalen waar de eigenaar zelf voor kiest (Idealista "Vendor Leads", I-6) | n.v.t. | n.v.t. | Rechtmatige route (eigenaar kiest contact met professionals); condities ONBEKEND | n.v.t. |

---

## 5. (d) AI-analyse van foto's en teksten van derden

### 5.1 Wat mag onder "gebruik voor eigen analyse" en waar ligt de grens

| Vraag | Antwoord | Onderbouwing | Type |
|---|---|---|---|
| Mag een medewerker in een Claude-sessie een advertentie laten samenvatten of beoordelen? | Ja, verdedigbaar, zolang niets buiten de sessie wordt opgeslagen behalve link en eigen oordeel | Tijdelijke weergave (art. 31.1); de Idealista-assistent biedt zelf "summary" en "compare" (I-10) | 4 |
| Mag een script portaalfoto's downloaden en met AI of dHash analyseren? | **Nee, zonder toestemming** | Reproductie (art. 18); foto's beschermd (art. 10.1.h / 128); voorwaarden I-3 ("descargar, guardar"); TDM-voorbehoud (§3.3) | 2 / 4 |
| Is een beeldhash zelf een reproductie? | Vermoedelijk niet: een dHash van 64 bits laat geen reconstructie toe. Het downloaden om de hash te maken is het probleem | Art. 18 eist fixatie "que permita su comunicación o la obtención de copias" | 4 **[advocaat]** |
| Mag een AI-model van TREE worden getraind op portaalfoto's of -teksten? | **Nee** | Geen licentie; Milanuncios reserveert AI-training uitdrukkelijk (M-1); EDPB 03/2026 | 2 / 3 / 4 |
| Mag AI-output (renovatieschatting, beschrijving) in een klantdossier? | Ja als eigen analyse zonder overname van foto's of teksten; nee als het een herschrijving van de advertentietekst is (art. 21) of foto's bevat | Art. 21; §3.8 | 4 |
| Mag een renovatievisualisatie op basis van een portaalfoto worden gemaakt? | Nee zonder toestemming: bewerking van een beschermde foto; bij realistische beelden AI-verordening art. 50.4 | Art. 21, art. 128; AI-verordening art. 50.4 | 2 / 4 |
| Mogen BP-foto's en -teksten met AI worden geanalyseerd en gehasht? | Pas na schriftelijke bevestiging (§6.4); BP moet bovendien garanderen dat BP die rechten mag verlenen (BP is vaak niet de fotograaf) | BP-1 | 2 / 4 |
| Doorgifte van content aan een AI-aanbieder (Anthropic API) | Extra reproductie bij een verwerker. Nodig: licentie die "verwerking door dienstverleners" dekt, verwerkersovereenkomst bij persoonsgegevens, en voorwaarden zonder training op onze invoer | Niet in deze stroom geverifieerd | 7 **[te verifiëren]** |
| Personen op foto's | Niet analyseren of indexeren; geen gezichtsherkenning; bij voorkeur blurren vóór opslag van eigen foto's | AI-verordening art. 5.1.e; AVG | 2 / 4 |

**Conflict met R17 (type 4):** R17 §6.2 plant een "dHash op foto's: per advertentie de hashes van maximaal 8 foto's" als derde deduplicatietrap, ook voor Idealista-dubbels. Voor Idealista en andere portalen zonder licentie is dat **niet toegestaan**. Alternatief: deduplicatie op feiten (prijs, m², kamers, benaderde coördinaat), teksthash over **eigen** genormaliseerde velden, en menselijke controle. dHash alleen op BP-foto's na akkoord.

### 5.2 Catastro- en INSPIRE-licenties, BOE-hergebruik (Ley 37/2007)

| Bron | Wat mag | Voorwaarden | Type |
|---|---|---|---|
| Catastro-webdiensten en INSPIRE (CP, AD, BU) | Eigen gebruik; nieuwe producten met toegevoegde waarde na transformatie; commercieel gebruik van getransformeerde informatie | Geen doorlevering van originele data; geen suggestie van "cartografía catastral"; diensten niet overbelasten (C-1, C-2); bronvermelding (R11: Resolución 23-03-2011 voor massadownload) | 2 |
| Catastro beschermde gegevens | Niet via vrije diensten | TRLCI 51–53 | 2 |
| BOE-documenten (sede electrónica), open-data-API, RSS | Kopiëren, extraheren, combineren, commercieel | Bronvermelding met link; niet "desnaturalizar"; geen officieel karakter suggereren; AVG bij persoonsgegevens (B-4, B-5) | 2 |
| Ley 37/2007 algemeen | Art. 4.1: documenten van overheden zijn herbruikbaar voor "fines comerciales o no comerciales"; art. 4.4: overheden oefenen het databankrecht van art. 133 niet uit om hergebruik te beletten | Art. 3.3: niet voor documenten waarvoor "interés legítimo" nodig is (c), met IE-rechten van derden (e), of met toegangsbeperking om privacyredenen (k); art. 8: mogelijke licentievoorwaarden (bron, datum, geen verandering, doel bij persoonsgegevens, geen heridentificatie) | 2 |
| Registro de la Propiedad | Per object een nota simple bij legitiem belang | Niet hergebruiken als databank (RP-3); valt buiten Ley 37/2007 (art. 3.3.a noemt "la publicidad registral") | 2 |

---

## 6. (e) Compliance-matrix per brontype

### 6.1 Matrix

| Brontype | Voorbeelden | Toegestaan | Toegestaan onder voorwaarde | Niet toegestaan | Registerstatus (§7 masterprompt) |
|---|---|---|---|---|---|
| **A. Portaal zonder licentie** | idealista.com (web), fotocasa.es, habitaclia.com, pisos.com, kyero.com, thinkspain.com, milanuncios.com | Handmatig bekijken; eigen e-mailalerts ontvangen; link + portaal-ID + eigen oordeel in dossier; handmatig enkele feiten noteren met bron en datum; via portaalformulier reageren als geïnteresseerde koper | Automatisch uitlezen van alertmails in eigen mailbox (alleen link, ID, prijs; geen foto's) **[advocaat]**; schermafdruk als intern bewijsstuk **[advocaat]**; link naar advertentie delen met klant | Scrapers, crawlers, headless browsers, ook via derden (TRLPI 138); omzeilen van botbeveiliging (CP 197 bis); foto's of teksten downloaden, opslaan, hashen, AI-analyseren buiten de sessie; prijshistorie of databank opbouwen; herpubliceren; foto's of teksten naar klanten; AI-training | ALLEEN HANDMATIG (commerciële scrapers: NIET GEBRUIKEN) |
| **B. Officiële assistent** | Idealista-assistent (MCP) in Claude-sessie | Ad-hoczoekvragen door een medewerker; samenvatten en vergelijken in de sessie; link + propertyCode + eigen oordeel bewaren | **Na schriftelijke toestemming van Idealista:** geplande of dagelijkse zoekvragen, opslag van resultaten, prijsdalingshistorie, foto-URL's verwerken | Veel varianten draaien om de limiet van 50 te omzeilen en de databank te repliceren; doorschakelnummers voor commerciële benadering; foto's downloaden of hashen | ALLEEN HANDMATIG → CONTRACT OF TOESTEMMING NODIG voor systematisch gebruik |
| **C. Partnerfeed** | Background Properties (Kyero v3) | Ophalen met verstrekte sleutel; tonen op treeproperties.es (feitelijk gebruik, niet schriftelijk vastgelegd) | **Na schriftelijke bevestiging (§6.4):** opslag en historie; AI-analyse; beeldhashes; foto-cache; dossiers voor individuele klanten; gebruik door benoemde groepsentiteiten | Zonder bevestiging: alles buiten de website; sleutel delen; doorlevering; publicatie op andere sites; gebruik door Rocksure zonder besluit van Jan | CONTRACT OF TOESTEMMING NODIG (website-gebruik feitelijk actief) |
| **D. Open overheidsdata** | BOE-open-data-API (sumario, legislación), BOE-RSS, Catastro-webdiensten, INSPIRE WFS/WMS/ATOM | Ophalen via officiële API of dienst; opslaan; verrijken; commercieel gebruik van getransformeerde data; met bronvermelding en datum | Persoonsgegevens in BOE-documenten alleen als strikt nodig, niet doorzoekbaar, met verwijderdatum; Catastro-bulk via de Sede met identificatie; rate limits | Originele Catastro-data herdistribueren; officieel karakter suggereren; beschermde Catastro-gegevens zonder grondslag; persoonsprofielen | TECHNISCH ONDERZOEK NODIG (rechten in orde; nog niet actief) |
| **E. Veilingportaal en insolventieregisters** | subastas.boe.es, Registro Público Concursal, edictos judiciales | Handmatig raadplegen; e-mailalerts na registratie (natuurlijke persoon, Jan); BOE-RSS/sumario als trigger (type D) en daarna handmatig openen; objectgegevens in dossier | Gerichte geautomatiseerde raadpleging van één detailpagina per nieuw SUB-id: **pas na toestemming AEBOE**; naam van schuldenaar alleen in afgeschermd biedingsdossier als juridisch nodig | Crawlen (robots `Disallow: /`); eigen doorzoekbare databank met namen; publiceren; schuldenaren benaderen op basis van edictos; RPC-persoonsgegevens hergebruiken | ALLEEN HANDMATIG (automatisering: CONTRACT OF TOESTEMMING NODIG) |
| **F. Registro de la Propiedad** | Nota simple via registradores.org | Per kandidaat aanvragen met legitiem belang en opgave van reden | Eigenaarsgegevens alleen in het dossier van dat object, voor due diligence | Opname in commerciële of doorverkoopbare databank (RH 332.2); marketinggebruik van eigenaarsgegevens **[advocaat]** | ALLEEN HANDMATIG |

### 6.2 Bewaartermijnen (werkhypothese, type 4 — door advocaat te bevestigen)

| Categorie | Voorgestelde termijn | Na afloop | Grond |
|---|---|---|---|
| Eigen notities, links, portaal-ID's, handmatig genoteerde feiten (type A/B) | 24 maanden na laatste activiteit op het object | Verwijderen of anonimiseren tot marktstatistiek zonder objectidentiteit | Doelbinding; geen persoonsgegevens |
| BP-feedsnapshots en -historie (type C) | Zoals overeengekomen; voorstel: looptijd samenwerking + 24 maanden | Terugbrengen tot eigen afgeleide gegevens zonder BP-teksten en -foto's | Clausule §6.4 |
| BP-foto's (cache) | Maximaal 30 dagen na verdwijnen uit de feed, tenzij het object in een actief dossier zit | Verwijderen | BP-1; minimalisatie |
| Beeldhashes van BP-foto's | Zolang het objectrecord bestaat, maximaal einde samenwerking + 24 maanden | Verwijderen | Clausule §6.4 |
| Open overheidsdata zonder persoonsgegevens (type D) | Onbeperkt zolang relevant, met bron en datum | — | Licenties staan het toe |
| Persoonsgegevens van makelaars (GoHighLevel) | Zolang er een zakelijke relatie is; 24 maanden zonder contact → verwijderen; bezwaar direct verwerken | Blokkeren waar nodig (art. 32) | LOPDGDD 19; AVG 21 |
| Persoonsgegevens van particulieren die zelf contact zochten | Duur van het gesprek + 12 maanden zonder vervolg; bij transactie de wettelijke termijnen **[te verifiëren]** | Blokkeren tot verjaring (max. 3 jaar, art. 72), dan vernietigen | AVG 5.1.e; LOPDGDD 32, 72 |
| Namen van schuldenaren of eigenaren in een concreet biedingsdossier | Tot 12 maanden na afloop van de veiling; langer alleen bij daadwerkelijke aankoop (dan onderdeel van het aankoopdossier) | Blokkeren tot verjaring, dan vernietigen | Doelbinding; masterprompt |
| Bewijs van toestemmingen en licenties (BP-mail, Idealista-akkoord, AEBOE-akkoord) | Looptijd + 5 jaar | Verwijderen | CC art. 1964.2 |
| Toegangslogs van bronadapters (wat is wanneer opgehaald) | 24 maanden | Verwijderen | Aantonen dat we binnen de rechten bleven |

### 6.3 Wat we van BP en andere partners schriftelijk moeten vastleggen

1. **Wie** mag gebruiken: TREE Properties (rechtspersoon invullen) en eventueel andere groepsentiteiten, bij naam. Rocksure alleen na besluit van Jan.
2. **Welke feeds**: export-ID's (26, 27, 29, 30, 31, 32, 36), zonder sleutel in het document.
3. **Doelen**: (a) publicatie op treeproperties.es; (b) intern aanbodbeheer; (c) acquisitie- en marktanalyse (Deal Hunter); (d) dossiers voor individuele klanten of investeerders.
4. **Opslag en historie**: mag, hoe lang, ook na verdwijnen uit de feed.
5. **AI-analyse** van teksten en foto's, ook via dienstverleners die niet op de data trainen.
6. **Beeldvergelijking**: hashes berekenen en bewaren, onderling en met andere bronnen; geen publicatie.
7. **Foto's**: hotlinken of kopiëren; cachetermijn; watermerk.
8. **Tonen aan klanten**: welke velden, met of zonder BP-naam, zonder eigenaarsgegevens, geen doorplaatsing door de klant.
9. **Garantie** dat BP de rechten op foto's en teksten heeft of mag doorlicentiëren, plus vrijwaring.
10. **Persoonsgegevens**: de feed bevat geen eigenaarsgegevens; zo wel, dan de rolverdeling (zelfstandige verwerkingsverantwoordelijken) en een meldplicht.
11. **Einde**: wat moet weg en wat mag blijven (eigen analyses, geaggregeerde statistiek).
12. **Sleutel**: vertrouwelijk, gebonden aan TREE, melding bij rotatie, eventueel een testsleutel.
13. **Wijzigingen** van feedstructuur of voorwaarden: opzegtermijn.
14. **Recht en forum**: Spaans recht; forum volgens BP-aviso legal Elche, of in overleg Dénia/Alicante.

Hetzelfde sjabloon geldt voor lokale makelaars die een feed of lijst leveren (masterprompt §9).

### 6.4 Conceptclausule voor Background Properties

> **CONCEPT — niet versturen.** Juridisch te toetsen door een Spaanse advocaat. Pas na akkoord van Jan aan BP voorleggen (CLAUDE.md regel 4 en tree-es regel 2). De velden tussen [haken] vult Jan in. De Spaanse tekst is leidend omdat BP's aviso legal Spaans is en Spaans recht kiest; de Nederlandse tekst is een werkvertaling.

**Versión española (texto prevalente)**

> **Anexo de autorización de uso de datos — Feeds XML de Background Properties**
>
> **1. Partes y objeto.** [Nombre del titular de Background Properties / razón social], con CIF [·] ("BP"), autoriza a [razón social de TREE Properties], con CIF [·] ("el Licenciatario"), a acceder a los ficheros de exportación identificados como export_id [26, 27, 29, 30, 31, 32 y 36] (los "Feeds") y a utilizar su contenido (datos de los inmuebles, textos, fotografías, planos y demás elementos, en adelante los "Contenidos") en los términos de este anexo. Las claves de acceso son confidenciales y no forman parte de este documento.
>
> **2. Finalidades autorizadas.** El Licenciatario podrá utilizar los Contenidos para: (a) su publicación en el sitio web treeproperties.es; (b) la gestión interna de su cartera; (c) el análisis interno de mercado y de oportunidades de adquisición, renovación o desarrollo; y (d) la elaboración de informes o dosieres dirigidos a clientes o inversores concretos, en los términos de la cláusula 6. [Opcional: Esta autorización se extiende a las siguientes sociedades del grupo: (·).]
>
> **3. Almacenamiento e histórico.** El Licenciatario podrá descargar, almacenar y conservar copias de los Feeds y de los Contenidos, incluido un histórico de precios, características, disponibilidad y fechas de primera y última aparición, también respecto de inmuebles que hayan dejado de figurar en los Feeds, durante la vigencia de este anexo y durante [24] meses tras su terminación.
>
> **4. Análisis automatizado e inteligencia artificial.** El Licenciatario podrá analizar los Contenidos mediante herramientas automatizadas y de inteligencia artificial, propias o de proveedores que actúen por su cuenta, siempre que dichos proveedores no utilicen los Contenidos para entrenar modelos propios ni para fines distintos del servicio prestado al Licenciatario.
>
> **5. Comparación de imágenes y datos derivados.** El Licenciatario podrá calcular y conservar huellas o representaciones derivadas de las fotografías (por ejemplo, hashes perceptuales o vectores) y compararlas entre sí y con imágenes de otras fuentes lícitas, con el único fin de identificar inmuebles duplicados o cambios. Los datos derivados no se publicarán y no permitirán reconstruir las imágenes. No se utilizarán para identificar a personas físicas.
>
> **6. Comunicación a terceros.** Fuera de treeproperties.es, el Licenciatario solo podrá mostrar los Contenidos a clientes o inversores concretos, en el marco de una relación de intermediación o asesoramiento, sin datos personales de propietarios y sin autorizar su reproducción o publicación por dichos terceros. [Con / sin] mención de BP como fuente. Queda excluida la cesión de los Feeds o de los Contenidos en bloque a terceros.
>
> **7. Fotografías.** El Licenciatario podrá [enlazar directamente las imágenes desde los servidores de BP / copiar las imágenes en sus propios sistemas y conservarlas mientras el inmueble figure en los Feeds y hasta [30] días después, salvo que forme parte de un dosier activo].
>
> **8. Garantía.** BP declara que es titular de los derechos de propiedad intelectual sobre los Contenidos o que dispone de las autorizaciones necesarias de propietarios, agentes colaboradores y fotógrafos para conceder este anexo, y mantendrá indemne al Licenciatario frente a reclamaciones de terceros derivadas de un uso conforme a este anexo.
>
> **9. Datos personales.** BP no incluirá en los Feeds datos personales de propietarios u otros particulares. Si los incluyera, cada parte actuará como responsable independiente del tratamiento conforme al Reglamento (UE) 2016/679 y a la Ley Orgánica 3/2018, y BP lo comunicará al Licenciatario.
>
> **10. Duración y terminación.** Este anexo tiene duración indefinida y podrá terminarse por cualquiera de las partes con un preaviso de [30] días. A su terminación, el Licenciatario dejará de acceder a los Feeds, retirará los Contenidos de su sitio web en un plazo de [30] días y suprimirá fotografías y textos de BP en un plazo de [90] días, pudiendo conservar sus propios análisis, datos derivados conforme a la cláusula 5 y estadísticas agregadas sin textos ni fotografías de BP, así como el histórico previsto en la cláusula 3.
>
> **11. Claves y cambios técnicos.** Las claves de acceso se asignan al Licenciatario y no se comunicarán a terceros. BP avisará con antelación razonable de cambios de estructura, rotación de claves o suspensión de los Feeds.
>
> **12. Ley y jurisdicción.** Ley española. Juzgados y Tribunales de [Elche / Dénia / Alicante].

**Nederlandse werkvertaling (kern per artikel)**

> 1. BP geeft TREE Properties toestemming de feeds (export_id 26, 27, 29, 30, 31, 32, 36) te gebruiken; sleutels blijven vertrouwelijk en staan niet in het document.
> 2. Doelen: website treeproperties.es; intern aanbodbeheer; interne markt- en acquisitieanalyse; dossiers voor concrete klanten of investeerders; eventueel benoemde groepsentiteiten.
> 3. Opslaan en historie bewaren (prijs, kenmerken, beschikbaarheid, eerste en laatste vermelding), ook van objecten die uit de feed zijn verdwenen; tijdens de looptijd en 24 maanden daarna.
> 4. Analyse met automatische en AI-hulpmiddelen, ook via dienstverleners die niet op de data trainen.
> 5. Beeldhashes of vectoren berekenen en bewaren om dubbele objecten en wijzigingen te herkennen; niet publiceren; niet terug te rekenen tot beelden; geen herkenning van personen.
> 6. Buiten de website alleen tonen aan concrete klanten of investeerders, zonder eigenaarsgegevens, zonder recht op verdere verspreiding; geen overdracht van de feed als geheel.
> 7. Foto's: hotlinken óf kopiëren met een bewaartermijn van 30 dagen na verdwijnen (keuze invullen).
> 8. BP garandeert de rechten op foto's en teksten en vrijwaart TREE.
> 9. Geen persoonsgegevens van eigenaren in de feed; zo wel, dan zelfstandige verwerkingsverantwoordelijken en melding door BP.
> 10. Onbepaalde duur, opzegbaar met 30 dagen. Na einde: website binnen 30 dagen opschonen, BP-foto's en -teksten binnen 90 dagen verwijderen; eigen analyses, hashes, statistiek en de historie uit art. 3 blijven.
> 11. Sleutel gebonden aan TREE; tijdige melding van wijzigingen of rotatie.
> 12. Spaans recht; forum invullen.

**Toelichting (type 4):** R05 §6.4 stelt voor dat "een korte schriftelijke bevestiging per punt" voldoende is. Juridisch is een e-mail waarin BP deze tekst uitdrukkelijk aanvaardt beter dan niets. Een ondertekend addendum is sterker, vooral voor de garantie (art. 8) en voor wat na beëindiging mag blijven (art. 10) **[advocaat]**.

### 6.5 Vertaling naar het systeem (bouwregels, type 4)

- **Rechtenregister als poortwachter:** elke bronadapter leest vóór uitvoering de rechtenvelden (`automated_access`, `storage`, `history`, `ai_analysis`, `image_hashing`, `show_to_clients`, `retention_days`). Staat een veld op `unknown` of `no`, dan weigert de adapter. Dit past op de bevoegdheden-engine van tree-ai-agentic-os (R17 §1.3).
- **Geen `raw_json`-opslag** van portaalbronnen; voor BP pas na §6.4.
- **Persoonsgegevensfilter** vóór opslag: regex op telefoon en e-mail in teksten, `userType=private` → contactvelden niet bewaren.
- **Verwijderjobs** per categorie uit §6.2, met logregel.
- **Contactmodule**: geen verzendfunctie naar particulieren; bij makelaars eerst een toestemmingsstatus en de Robinson-controle; elke uitgaande actie via goedkeuring door Jan (masterprompt §27).

---

## 7. Punten die een Spaanse advocaat moet bevestigen

1. Binden de algemene voorwaarden van Idealista, Fotocasa en Kyero een niet-geregistreerde bezoeker (browsewrap), en een geregistreerde professionele gebruiker?
2. Hebben Idealista en Fotocasa een sui-generisdatabankrecht (substantiële investering in verzamelen, verifiëren, presenteren), en is het handmatig noteren van enkele feiten per advertentie "niet-substantieel" in de zin van art. 134.1 TRLPI?
3. Valt geplande, dagelijkse raadpleging van de officiële Idealista-assistent onder "monitorizar" en "guardar" (§8.1), ook als alleen link, propertyCode en prijs worden bewaard?
4. Mag TREE automatisch de e-mailalerts van portalen in de eigen mailbox uitlezen (link, ID, prijs), gezien de voorwaarden en art. 133.2 TRLPI?
5. Is een voorbehoud in algemene voorwaarden (zonder machineleesbaar signaal) een geldig TDM-voorbehoud onder RDL 24/2021 art. 67.3, en valt per-object-analyse onder "minería de textos y datos"?
6. Is het berekenen en bewaren van perceptuele hashes van foto's een reproductie of transformatie, en zo nee, is de tijdelijke download gedekt door art. 31.1 of 67?
7. Is het doorsturen van een advertentielink met eigen analyse aan een klant rechtmatig; en het tonen van BP-foto's in een klantdossier onder de conceptclausule?
8. Is een e-mail of portaalbericht aan een particuliere adverteerder als "geïnteresseerde koper" een commerciële communicatie (LSSI bijlage f), als TREE ook makelaar, aannemer of investeerder is?
9. Is koud bellen van particuliere eigenaren met een gevonden telefoonnummer ooit verdedigbaar onder Circular 1/2023, of feitelijk uitgesloten?
10. Welke rechtsgrond en welke termijnen gelden voor namen van schuldenaren of eigenaren in een biedingsdossier (BOE-edicto, nota simple), en mag TREE een geëxecuteerde vóór de veiling benaderen?
11. Is voor de veilingmodule (koppeling BOE, Registro, portaal en AI) een DPIA verplicht, en is TREE dan verantwoordelijke of gezamenlijk verantwoordelijke met BP of andere partners?
12. Toetsing van de conceptclausule §6.4: garantie en vrijwaring, rechten na beëindiging, forumkeuze, en de positie van Rocksure als afzonderlijk merk of entiteit.

---

## 8. Bronnenregister-invoer (masterprompt §7, rechtenvelden)

| Bron | Type | Toegang | Rechten AI / opslag / afgeleide data | Status |
|---|---|---|---|---|
| idealista.com (web) | Portaal | Web; automatisering contractueel verboden | Nee / nee / nee zonder schriftelijke toestemming | ALLEEN HANDMATIG |
| Idealista-assistent (MCP) | Officiële AI-assistent | Tool-aanroep in Claude-sessie; max. 50 resultaten | In-sessie ja; opslag en systematisch gebruik ONBEKEND → toestemming nodig | ALLEEN HANDMATIG / CONTRACT OF TOESTEMMING NODIG |
| fotocasa.es | Portaal | Web; voorwaarden JS-only | Nee / nee / nee | ALLEEN HANDMATIG |
| habitaclia.com | Portaal | Web | Nee / nee / nee | ALLEEN HANDMATIG |
| pisos.com | Portaal | Web | Nee / nee / nee; particulierengegevens zichtbaar | ALLEEN HANDMATIG |
| kyero.com | Portaal | Web; botcontrole | Nee / nee / nee (snippet) | ALLEEN HANDMATIG |
| milanuncios.com | Portaal | Web; botcontrole; AI-trainingsbots uitgesloten | Nee / nee / nee | ALLEEN HANDMATIG |
| Commerciële scrapers (Apify e.a.) | Derde partij | — | Geen geautoriseerde bron; medeaansprakelijkheid (TRLPI 138) | NIET GEBRUIKEN |
| Background Properties feeds | Partnerfeed Kyero v3 | Export-URL met geheime sleutel | Website feitelijk; rest ONBEKEND → schriftelijk vastleggen | CONTRACT OF TOESTEMMING NODIG |
| BOE open data (API sumario, legislación, RSS) | Overheid | Open API/RSS | Ja / ja / ja met bronvermelding; AVG bij persoonsgegevens | TECHNISCH ONDERZOEK NODIG |
| subastas.boe.es | Overheid, veilingen | Web + alerts na registratie; robots Disallow / | Handmatig; automatisering alleen met AEBOE-akkoord; geen namenbank | ALLEEN HANDMATIG |
| Registro Público Concursal | Overheid, insolventie | Web; robotisering verboden | Persoonsgegevens: hergebruik verboden | ALLEEN HANDMATIG |
| Catastro webdiensten/INSPIRE | Overheid | Open webdiensten | Eigen gebruik en getransformeerde producten ja; geen doorlevering origineel; beschermde gegevens nee | TECHNISCH ONDERZOEK NODIG |
| Registro de la Propiedad (nota simple) | Register | Per object, betaald, legitiem belang | Geen databank voor commercialisering | ALLEEN HANDMATIG |

---

## 9. Open vragen

1. Wat is de actuele tekst van de Idealista-voorwaarden (versie 30-04-2025 volgens snippets) en van het Fotocasa-portaal? Zijn er aparte voorwaarden voor de Idealista-app of MCP?
2. Heeft Idealista een route (API, "Vendor Leads", idealista/data) die dagelijkse monitoring van Jávea met opslagrecht dekt, en tegen welke kosten? (R01: offerte nodig.)
3. Welke "condiciones de uso" aanvaardt een geregistreerde gebruiker van subastas.boe.es, en geeft de AEBOE toestemming voor gerichte detailraadpleging per SUB-id?
4. Is Idealista aangewezen als VLOP onder de DSA? (Niet relevant voor toegang, wel voor context.)
5. Heeft R17 de voorwaarden van de AI-aanbieder (geen training op invoer, verwerkersovereenkomst, doorgifte buiten de EER) al vastgesteld? Anders een aparte controle.
6. Welke AI-verordeningstermijnen gelden na eventuele wijzigingen in 2025–2026?
7. Waarom zag R01 op 14-09 een `Disallow: /` in de robots.txt van Idealista en ik op 15-09 niet (andere user-agent of wijziging)?
8. Moet de veilingmodule onder TREE Properties, onder een aparte entiteit of onder Rocksure vallen? Dat bepaalt wie verwerkingsverantwoordelijke is (besluit van Jan).

---

## 10. Geblokkeerd of mislukt (niet omzeild)

| Wat | Resultaat | Gevolg |
|---|---|---|
| idealista.com `/ayuda/articulos/legal-statement/` (curl, WebFetch) en pdf "2022-Hasta-24-08-2022" | HTTP 403 | Versie 20-11-2020 gebruikt; actuele tekst [te verifiëren] |
| tracker.terminosycondiciones.es (doc 721) | Time-out en connection refused | Wijzigingshistorie niet gezien |
| fotocasa.es aviso legal | Alleen footer (JavaScript) | Microsite-voorwaarden als indicatie; portaaltekst [te verifiëren] |
| kyero.com/en/docs/terms/ | 403 "Checking your browser" (curl), 403 (WebFetch) | Alleen snippet (type 7) |
| EUR-Lex (Richtlijn 96/9, arresten) | HTTP 202 met lege body | BOE-DOUE-kopieën en ipcuria.eu gebruikt |
| curia.europa.eu persberichten | Twee door mij gekozen persberichtnummers bleken andere zaken te zijn | Niet gebruikt; dictums via ipcuria.eu |
| ippt.eu (C-762/19 pdf) | 403 | ipcuria.eu gebruikt |
| CENDOJ (STS 572/2012) en Lexology | JavaScript-only / 403 | Alleen secundaire bron LegalToday (type 7) |
| autoriteitpersoonsgegevens.nl (handreiking, pdf en pagina) | 403 | Alleen snippets (type 7) |
| catastro.hacienda.gob.es via curl | SSL-certificaatketen niet te verifiëren | Niet met `-k` omzeild; WebFetch gebruikt |
| backgroundproperties.com/robots.txt | 403 (botpagina) | Aviso legal wel gelezen |
| subastas.boe.es gebruiksvoorwaarden | Alleen na registratie | Niet gelezen |
| ECLI van C-621/22 | Bronnen noemen :857 en :858 | ECLI weggelaten |
| Een OCR-kopie van Idealista-voorwaarden ("17 de febrero de 2024") in de gedeelde scratchpad van deze sessie | Herkomst niet herleidbaar | **Niet gebruikt** als bewijs |
| Uitspraak "portaal tegen scraper" in Spanje | Niet gevonden (twee zoekopdrachten) | Vermeld als niet gevonden |

---

## 11. Bronnenlijst (URL · controledatum · bewijstype)

**Wetgeving Spanje (BOE, geconsolideerd, via open-data-API)**
- TRLPI (RDL 1/1996), art. 10, 12, 13, 18, 21, 31, 32, 34, 128, 133–138 — https://www.boe.es/buscar/act.php?id=BOE-A-1996-8930 · 15-09-2026 · 2
- RDL 24/2021, art. 65–67 (TDM) — https://www.boe.es/buscar/act.php?id=BOE-A-2021-17910 · 15-09-2026 · 2
- LOPDGDD (LO 3/2018), art. 19, 21, 23, 32, 72–74, DA 7ª — https://www.boe.es/buscar/act.php?id=BOE-A-2018-16673 · 15-09-2026 · 2
- Ley 10/2025, DF 4ª (wijziging art. 23 LOPDGDD) — https://www.boe.es/buscar/act.php?id=BOE-A-2025-26698 · 15-09-2026 · 2
- LSSI (Ley 34/2002), art. 19–22, 38, 39, bijlage — https://www.boe.es/buscar/act.php?id=BOE-A-2002-13758 · 15-09-2026 · 2
- Ley 11/2022 General de Telecomunicaciones, art. 66 — https://www.boe.es/buscar/act.php?id=BOE-A-2022-10757 · 15-09-2026 · 2
- Circular AEPD 1/2023 — https://www.boe.es/buscar/act.php?id=BOE-A-2023-15071 · 15-09-2026 · 2
- Ley 37/2007 hergebruik overheidsinformatie, art. 1–4, 8 — https://www.boe.es/buscar/act.php?id=BOE-A-2007-19814 · 15-09-2026 · 2
- Ley 19/2015, DA 2ª — https://www.boe.es/buscar/act.php?id=BOE-A-2015-7851 · 15-09-2026 · 2
- TRLCI (RDL 1/2004), art. 51–53 — https://www.boe.es/buscar/act.php?id=BOE-A-2004-4163 · 15-09-2026 · 2
- Ley Hipotecaria, art. 221–222 — https://www.boe.es/buscar/act.php?id=BOE-A-1946-2453 · 15-09-2026 · 2
- Reglamento Hipotecario, art. 332 — https://www.boe.es/buscar/act.php?id=BOE-A-1947-3843 · 15-09-2026 · 2
- Ley 3/1991 Competencia Desleal, art. 11 — https://www.boe.es/buscar/act.php?id=BOE-A-1991-628 · 15-09-2026 · 2
- Código Penal, art. 197 bis — https://www.boe.es/buscar/act.php?id=BOE-A-1995-25444 · 15-09-2026 · 2
- Código Civil, art. 1964 — https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763 · 15-09-2026 · 2

**EU-wetgeving (DOUE-kopieën op boe.es)**
- Richtlijn 96/9/EG, art. 7–9, 15 — https://www.boe.es/buscar/doc.php?id=DOUE-L-1996-80413 · 15-09-2026 · 2
- AVG (Verordening 2016/679), art. 5, 6, 14, 21, 35 — https://www.boe.es/buscar/doc.php?id=DOUE-L-2016-80807 · 15-09-2026 · 2
- AI-verordening (2024/1689), art. 4, 5, 50, 113 — https://www.boe.es/buscar/doc.php?id=DOUE-L-2024-81079 · 15-09-2026 · 2
- DSA (2022/2065), art. 33, 40 — https://www.boe.es/buscar/doc.php?id=DOUE-L-2022-81573 · 15-09-2026 · 2
- Data Act (2023/2854), art. 1, 43 — https://www.boe.es/buscar/doc.php?id=DOUE-L-2023-81895 · 15-09-2026 · 2

**Rechtspraak**
- HvJ C-203/02 BHB — https://ipcuria.eu/case?reference=C-203%2F02 · 15-09-2026 · 2 (vindplaats secundair)
- HvJ C-202/12 Innoweb — https://ipcuria.eu/case?reference=C-202%2F12 · 15-09-2026 · 2 (vindplaats secundair)
- HvJ C-30/14 Ryanair v PR Aviation — https://ipcuria.eu/case?reference=C-30%2F14 · 15-09-2026 · 2 (vindplaats secundair)
- HvJ C-762/19 CV-Online Latvia — https://ipcuria.eu/case?reference=C-762%2F19 · 15-09-2026 · 2 (vindplaats secundair)
- HvJ C-621/22 KNLTB — https://ipcuria.eu/case?reference=C-621%2F22 · 15-09-2026 · 2 (vindplaats secundair)
- STS 572/2012 Ryanair v Atrápalo (samenvatting) — https://www.legaltoday.com/practica-juridica/derecho-civil/nuevas-tecnologias-civil/ryanair-pierde-su-batalla-legal-frente-a-las-agencias-de-viajes-online-2013-01-14/ · 15-09-2026 · 7
- CGPJ-perskennis TS 09-04-2014 Ryanair — https://www.poderjudicial.es/cgpj/en/Judiciary/Pressroom/News-archive/El-TS-estima-parcialmente-un-recurso-de-Ryanair-contra-una-agencia-de-viajes-on-line-por-las-clausulas-de-contratacion · 15-09-2026 · 2
- Top Rural (secundair) — https://artiureabogados.com/base-de-datos-y-scraping-web/ · 15-09-2026 · 7

**Toezichthouders**
- AEPD, criterium AI-00059-2024 (data scraping) — https://www.aepd.es/informes-y-resoluciones/criterios-juridicos-aepd/herramientas-data-scraping-para-evaluacion-de-tendencias · 15-09-2026 · 2
- AEPD, E/04809/2015 (subastafacil.com) — https://www.aepd.es/documento/e-04809-2015.pdf · 15-09-2026 · 2
- AEPD, lijst EIPD art. 35.4 — https://www.aepd.es/documento/listas-dpia-es-35-4.pdf · 15-09-2026 · 2
- EDPB Guidelines 03/2026 web scraping (consultatieversie) — https://www.edpb.europa.eu/system/files/2026-07/edpb_guidelines_2020603_webscraping_v1_en_0.pdf · 15-09-2026 · 2
- Autoriteit Persoonsgegevens, Handreiking scraping (alleen snippet) — https://www.autoriteitpersoonsgegevens.nl/documenten/handreiking-scraping-door-particulieren-en-private-organisaties · 15-09-2026 · 7

**Voorwaarden en technische signalen van bronnen**
- Idealista T&C (versie 20-11-2020) — https://st1.idealista.com/ayuda/wp-content/uploads/2021/11/2021-Hasta-11-11-2021-Terminos-y-condiciones.pdf · 15-09-2026 · 2
- Idealista legal statement (actueel, 403) — https://www.idealista.com/ayuda/articulos/legal-statement/ · 15-09-2026 · 7
- Idealista robots.txt — https://www.idealista.com/robots.txt · 15-09-2026 · 3
- Idealista-assistent, `guide_idealista_assistant` (MCP-tool) · 15-09-2026 · 1/3
- Fotocasa aviso legal (JS-only) — https://www.fotocasa.es/es/aviso-legal/ln · 15-09-2026 · 3
- Fotocasa Proyecto Vivienda, condiciones legales — https://www.fotocasa.es/proyecto-vivienda/condiciones-legales/ · 15-09-2026 · 2
- Fotocasa Alquiler T&C (uit R02) — https://www.fotocasa.es/gestion-alquiler/terminos-y-condiciones/ · 14-09-2026 · 2
- Habitaclia Condiciones Generales — https://www.habitaclia.com/hab_cliente/legalavisocontentmodal.asp · 15-09-2026 · 2
- pisos.com aviso legal — https://www.pisos.com/avisolegal · 15-09-2026 · 2
- pisos.com robots.txt — https://www.pisos.com/robots.txt · 15-09-2026 · 3
- HabitatSoft legal notice — https://www.habitatsoft.com/legal-notice?culture=es-ES · 15-09-2026 · 2
- Kyero terms (403; snippet) — https://www.kyero.com/en/docs/terms/ · 15-09-2026 · 7
- Kyero robots.txt — https://www.kyero.com/robots.txt · 15-09-2026 · 3
- Milanuncios robots.txt — https://www.milanuncios.com/robots.txt · 15-09-2026 · 3
- thinkSPAIN legal info (uit R03) — https://www.thinkspain.com/legal-info · 14-09-2026 · 2
- subastas.boe.es robots.txt — https://subastas.boe.es/robots.txt · 15-09-2026 · 3
- subastas.boe.es help — https://subastas.boe.es/ayuda.php · 15-09-2026 · 2
- BOE aviso legal / condiciones de reutilización — https://www.boe.es/informacion/aviso_legal/index.php · 15-09-2026 · 2
- boe.es robots.txt — https://www.boe.es/robots.txt · 15-09-2026 · 3
- Registro Público Concursal aviso legal — https://www.publicidadconcursal.es/aviso-legal · 15-09-2026 · 2
- Background Properties aviso legal — https://backgroundproperties.com/aviso-legal/ · 15-09-2026 · 2
- Catastro INSPIRE-licentie — https://www.catastro.hacienda.gob.es/webinspire/documentos/Licencia.pdf · 15-09-2026 · 2
- Catastro INSPIRE-pagina — https://www.catastro.hacienda.gob.es/webinspire/index.html · 15-09-2026 · 2

**Lokaal (eigen dienst, alleen lezen)**
- properties-api, 56 BP-objecten Jávea, controle op contactgegevens — http://127.0.0.1:3100/api/properties?town=Javea&limit=100 · 15-09-2026 · 3
- Interne rapporten R01, R02, R03, R05 (+verificatie), R08, R09, R11, R17 — /Users/root-admin/tree-es/deal-hunter/onderzoek/ · 14-09-2026 · 3

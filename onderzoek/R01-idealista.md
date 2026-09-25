# R01 — Idealista: portaal, officiële API, idealista/data en de Idealista-assistent

> **NA TEGENSPRAAK (15-09-2026).** Dit rapport is door een tweede agent gecontroleerd; zie `R01-idealista.verificatie.md`. Betrouwbaarheid volgens die controle: hoog.
> Weerlegd en in de eindstukken gecorrigeerd: R01-08; R01-14; R01-20. Gebruik voor die punten de gecorrigeerde tekst in het verificatiebestand, niet de tekst hieronder.


**Project:** TREE Deal Hunter, fase A (bronnenkaart)
**Stroom:** R01 — Idealista
**Controledatum:** 14-09-2026
**Auteur:** onderzoeksagent (subagent), in opdracht van Jan / TREE Group
**Bewijstypen (masterprompt §5):** 1 door aanbieder vermeld · 2 in officiële bron aangetroffen · 3 door ons rechtstreeks vastgesteld · 4 AI-inferentie · 5 berekening op benoemde aannames · 6 door bevoegde professional bevestigd · 7 onbekend of tegenstrijdig

## Samenvatting (10 regels)

1. Idealista kent vier gescheiden routes: het publieke portaal (lezen verboden voor automaten), de officiële Search API (developers.idealista.com, alleen op aanvraag, geen gepubliceerde voorwaarden), idealista/data (commerciële datatak, offerte nodig) en de nieuwe Idealista-assistent voor AI-chat (ChatGPT-app sinds 13-03-2026; in deze sessie als MCP aangesloten).
2. De officiële Search API bestaat nog in 2026: developers.idealista.com stuurt door naar een aanvraagformulier (naam, e-mail, projectbeschrijving). Limieten, prijzen, toegestane doelen en of hij advertenties van derden mag teruggeven staan **niet** openbaar; alles daarover in blogs is ongeverifieerd.
3. idealista/data biedt "API de testigos actuales e históricos", "API de valoraciones y datos catastrales", buurtmetrieken, AVM (verwijst naar Orden ECO/805/2003 art. 21), Market Navigator en maatwerk-databestanden. Geen prijs, geen licentietekst online; contactformulier.
4. De gebruiksvoorwaarden (officiële pdf-versie 20-11-2020; huidige versie 30-04-2025 alleen via zoekmachine-snippet zichtbaar) verbieden expliciet toegang, controle of kopie via "robot, spider, scraper u otro medio automático o proceso manual" zonder schriftelijke toestemming, en verbieden "copiar, monitorizar (por ejemplo, spider, scrape)" voor commerciële of concurrerende doeleinden. robots.txt eindigt met `Disallow: /` voor alle bots.
5. De Idealista-assistent geeft echte advertenties met prijs, prijsdaling, m², kamers, lat/long, beschrijving, status en per resultaat een Idealista-doorschakelnummer. Het detail-endpoint geeft óók makelaarsnaam, externe referentie, energielabel en een grove wijzigingsdatum ("hace más de 3 meses"). Ontbreekt: publicatiedatum, exact adres bij de meeste objecten, paginering.
6. Meting Jávea (14-09-2026, via de assistent): 1.275 casas/chalets, waarvan 70 "para reformar" (mediaan van de 50 getoonde: 750.000 €); 569 pisos (19 para reformar); 333 terrenos (238 urbanos+urbanizables); 77 obra-nueva-promoties; 0 "de bancos"; 6 chalets gepubliceerd in de laatste 48 uur.
7. De assistent leidt filters af uit de tekst (para reformar, prijsband, últimas 48h, de bancos, urbanos/urbanizables) maar "bajada de precio" wordt een **sortering** (`ordenado-por=rebajas-desc`), geen filter. Maximaal 50 resultaten per aanroep, geen offset: volledige dekking vereist opsplitsen in deelzoekopdrachten.
8. Of dagelijks gepland gebruik van de assistent is toegestaan, wordt in geen enkele gevonden tekst geregeld. De tool is ontworpen voor consumenten (utm_project=leadGeneration, 8–15 resultaten aanbevolen). Eerlijk antwoord: ONBEKEND; schriftelijke toestemming vragen is de veilige weg.
9. Toegestane wijzigingsdetectie zonder automatisering: opgeslagen zoekopdrachten met e-mailalert (direct/dagelijks/wekelijks) voor nieuwe advertenties, en "guardar para después"/volgen per object voor prijsdalingen. Of die e-mails automatisch verwerkt mogen worden, regelen de voorwaarden niet.
10. Openbare prijsrapporten per gemeente (sala-de-prensa) bestaan, zijn maandelijks en sinds juli 2026 met nieuwe methodiek, maar de pagina's geven HTTP 403 aan onze tools: alleen handmatig in een browser overnemen (kwartier per maand).

## 1. Aanpak en beperkingen

| Wat | Hoe | Resultaat |
|---|---|---|
| Officiële pagina's | WebFetch + één enkelvoudige `curl` per URL (standaard UA, geen omzeiling) | `/data/*`, `/news/*`, `developers.idealista.com`, `robots.txt` en statische pdf's op `st1/st3.idealista.com`: bereikbaar. `/ayuda/*`, `/informacion/*`, `/sala-de-prensa/*`, `/tools/centrodeayuda/*`, `/valoracion-de-inmuebles/*`, idealista.pt en idealista.it: **HTTP 403** |
| Voorwaarden | Officiële pdf (versie 20-11-2020, geldig tot 11-11-2021) van `st1.idealista.com` volledig gelezen; huidige versie (30-04-2025) alleen via zoekmachine-snippets | Clausules letterlijk overgenomen uit de pdf; snippets bevestigen dezelfde bewoording maar zijn geen primaire bron |
| Assistent | 13 aanroepen van `search_properties`, 2 van `property_detail`, 1 `get_howto`, 1 `guide` | Alle uitkomsten hieronder, bewijstype 3 |
| Lokale bronnen | `~/tree-es/properties/leadgen/docs/marktdata-bronnen.md` (25/26-08-2026) | Bevestigd: 403 op geautomatiseerde verzoeken; idealista/data commercieel |

Alles wat hieronder als "gezien" staat, heb ik zelf in de bron gelezen. Wat ik afleid, staat als bewijstype 4. Wat ik niet kon openen, staat in §12.

## 2. (a) De officiële zoek-API — developers.idealista.com

**Bestaat nog.** `https://developers.idealista.com/` antwoordt met HTTP 302 naar `http://developers.idealista.com/access-request` (zelf gemeten met curl, bewijstype 3). Die pagina zegt: "Search API lets you integrate property information published on idealista into your site or app." en "To receive an API key get in touch and tell us a bit about your project." (bewijstype 2, 14-09-2026).

| Onderwerp | Bevinding | Bewijs |
|---|---|---|
| Aanvraagroute | Webformulier: naam, e-mail, projectbeschrijving, akkoord privacybeleid | 2 — access-request-pagina |
| Documentatie | Niet openbaar. `?action=help` toont hetzelfde formulier; geen endpoints, geen velden, geen auth-beschrijving | 3 — beide URL's gelezen |
| Gratis limieten | ONBEKEND. De veelgenoemde "100 verzoeken per maand" komt uitsluitend uit blogs en GitHub-readme's; het Medium-artikel daarover gaf 403; de readme van `yagueto/idealista-api` noemt géén limiet | 7 — [te verifiëren] |
| Commerciële voorwaarden | ONBEKEND; niets gepubliceerd | 7 |
| Advertenties van derden | De omschrijving "property information published on idealista" suggereert het hele aanbod, maar de contractuele reikwijdte is niet gepubliceerd | 4 — [te verifiëren] |
| Toegestane doelen | ONBEKEND. Derden beweren dat toegang beperkt is tot "vetted business partners"; niet in een officiële bron gezien | 7 |
| Velden/paginering | Onofficiële client documenteert `page`, `items_per_page`, `total`, `total_pages`, `element_list` en parameters `location_id`, `property_type`, `operation`, `max_items`, `num_page` | 7 — GitHub-readme, onofficieel |

**Conclusie:** de enige officiële stap is het formulier invullen met een eerlijke projectbeschrijving (acquisitie-monitoring Jávea voor een makelaar/bouwer). Pas na acceptatie krijgen we documentatie en voorwaarden. Architectuur hier niet op bouwen voordat die binnen zijn (masterprompt §6).

## 3. (b) idealista/data

Bron: `https://www.idealista.com/data/` en subpagina's (bereikbaar, bewijstype 2, 14-09-2026).

| Product | Wat de site zegt | Bron |
|---|---|---|
| API | "A través de una API podrás consultar nuestros datos, desarrollar un widget integrado en tu propia web, o generar ficheros de datos puntuales en varios formatos." | /data/asesoramiento-inmobiliario-tecnologico/api-comparables-y-metricas/ |
| Testigos (comparables) | "API de testigos actuales e históricos." — actuele én historische vergelijkingsobjecten | idem |
| Waarderingen/kadaster | "API de valoraciones y datos catastrales." | idem |
| Zone-metrieken | "Métricas de zona hasta nivel de barrio." | idem |
| AVM | Massawaardering met vergelijkingsmethode + ML; verwijst naar "la ley ECO / 805/2003 (Art. 21)"; alerts door vergelijking met kadaster en eerdere waarderingen | /data/consultoria-inmobiliaria/valoracion-automatica/ |
| Market Navigator | "Toda la información inmobiliaria en tiempo real", onbeperkte waarderingen, marktstudies per zone; ook via idealista/tools af te nemen | pdf Servicios profesionales (nov. 2022) p. 12; /data/agencias-inmobiliarias-servicios/ |
| Voor makelaars | Commercialisatie-audit van kantoren en objecten, benchmark tegen andere makelaars in dezelfde zone; maatwerkstudies | /data/agencias-inmobiliarias-servicios/ |
| Dataschaal | "2.632.762 inmuebles", "2.064 millones de búsquedas" per kwartaal, historie "21 años" (sinds 2005) | /data/ |
| Doelgroepen | Banken/servicers, taxateurs, promotoren, investeerders, makelaars, overige instellingen | /data/ |
| Prijs | **Niet gepubliceerd.** Alleen "Pedir más información" / contactformulier (naam, telefoon, e-mail, profiel, behoefte) | /data/ — 3 |
| Licentie voor opslag en AI-analyse | **Niet gepubliceerd.** Geen voorwaardentekst op de /data/-pagina's gevonden | 7 |

**Relevantie voor Deal Hunter:** dit is de enige door Idealista zelf aangeboden *leesroute* voor comparables en prijshistorie. Kosten en rechten (opslag, afgeleide data, AI-analyse) zijn pas na offerte bekend. Prijsindicatie: ONBEKEND — ik verzin geen bedrag.

## 4. (c) De Idealista-assistent (ChatGPT-app / MCP)

### 4.1 Officiële aankondiging

- idealista/news, 13-03-2026: "idealista launches its app on ChatGPT" — Idealista is naar eigen zeggen de eerste Spaanse vastgoedsite met een app in ChatGPT; zoeken in woningen, kamers, garages, bedrijfsruimte en percelen in natuurlijke taal; vergelijken en samenvatten in de chat. Woordvoerder Francisco Iñareta. Geen limieten, geen voorwaarden, geen vermelding van Claude of MCP in het bericht (bewijstype 2).
- OpenAI: apps in ChatGPT draaien op de Apps SDK/MCP; de directory is sinds december 2025 open (zoekresultaat; de OpenAI-pagina's zelf gaven 403 — bewijstype 7 voor het detail, [te verifiëren]).
- In deze sessie is de assistent als MCP-server aangesloten met vier tools: `search_properties`, `property_detail`, `get_howto` (alleen `listing.publish`), `guide_idealista_assistant`. Alle URL's die hij teruggeeft dragen `utm_medium=generativeAI&utm_campaign=appChatgpt&utm_source=idGpt&utm_project=leadGeneration` — dezelfde backend als de ChatGPT-app (bewijstype 3/4).

### 4.2 Wat de aanbieder zelf over de tool zegt (bewijstype 1, uit de tooldefinities en de guide)

- "Returns real listings (0–N results); never fabricate."
- Aanbevolen 8–15 resultaten, 5–10 bij nauwe zoekopdrachten; `maxResults` maximaal 50.
- "Do not use for questions about idealista services (pricing, publishing ads, support)."
- URL's inclusief utm-parameters ongewijzigd doorgeven.
- Guide-tekst: zoeken, filteren, kamers/garages/percelen, vergelijken en samenvatten; eindigt met "Where would you like to live?" — consumentgericht.

### 4.3 Gebruiksvoorwaarden van de assistent

**Niet gevonden.** Er is geen aparte voorwaardentekst voor de ChatGPT-app of de MCP-server aangetroffen — niet in het nieuwsbericht, niet in de tooldefinities, niet via zoeken op idealista.com. De algemene voorwaarden (§6) gaan over "la Web y Apps" en verbieden automatische toegang zonder schriftelijke toestemming; ze noemen AI-assistenten niet. Zoekresultaten melden dat de algemene voorwaarden voor het laatst op 30-04-2025 zijn bijgewerkt — vóór de lancering van de app (snippet, [te verifiëren]).

**Valt "elke ochtend dezelfde zoekopdracht" binnen de voorwaarden?** Eerlijk antwoord: **ONBEKEND (7)**. Argumenten:
- Vóór: de assistent is een door Idealista zelf aangeboden kanaal, geen scraper; elke oproep is een normale tool-aanroep met attributie-links; wij omzeilen niets.
- Tegen: het ontwerp (leadGeneration, 8–15 resultaten, consumentenvragen) en de algemene voorwaarden ("uso estrictamente personal y privado", verbod op "monitorizar" voor commerciële doeleinden) wijzen op incidenteel, persoonlijk gebruik. Een dagelijkse, programmatische reeks van tientallen aanroepen om een lokale database te vullen is precies "monitorizar" in commerciële context.
- Advies (4): handmatig en ad hoc gebruik door een medewerker is verdedigbaar; **systematisch gebruik pas na schriftelijke toestemming** van Idealista (de voorwaarden noemen zelf "permiso expreso y por escrito" als de uitweg). Zie register.

### 4.4 Wat de tool wél en niet geeft (bewijstype 3)

**`search_properties` — per resultaat aanwezig (bij 50/50 van de chalets):** `propertyCode`, `url`, `price`, `priceInfo` (incl. `priceDropInfo` met `formerPrice`, `priceDropValue`, `priceDropPercentage` als er een daling is), `size`, `rooms`, `bathrooms`, `latitude`/`longitude`, `showAddress` (true/false), `suggestedTexts.title` (wijk + gemeente, soms straat), `detailedType` (typology/subTypology), `description` (volledig), `features` (booleans), `status` (`renew` / `good` / `newdevelopment`), `isNewDevelopment`, `thumbnail` + precies 1 image, `contactInfo` (`userType` professional/private, `contactMethod`, één telefoonnummer = Idealista-doorschakelnummer), `priceByArea`. Bij pisos ook `floor` (42/50) en `parkingSpace` (40/50). Bij terrenos geen `rooms`/`bathrooms`/`status`.
**Per antwoord:** `total` (echte teller van Idealista), `summary` (de door de tool afgeleide filters), `searchUrl` (de overeenkomstige idealista.com-URL), `locationName`, `requestContext`.

**`property_detail` — extra ten opzichte van search:** `outcome: "active"`, alle foto's met tag (91 stuks bij het geteste chalet), `areas.usableArea`, `characteristicsDescriptions` (o.a. "Parcela de 1600 m²", "Segunda mano/para reformar", bij percelen "Superficie edificable 3.450 m²", "Terreno urbano (solar)", "Calificado para residencial en altura"), `energyCertification` (letter + kWh/m²·jaar, of "Inmueble exento"), `labels` (bijv. "Vistas al mar"), `modificationDateText` ("Anuncio actualizado hace más de 3 meses"), en in `contactInfo`: `commercialName` (makelaarsnaam), `externalReference` (referentie van de makelaar), `micrositeUrl`, `agencyLogo`, `agencyAddress`.

**Ontbreekt (in beide tools):** publicatiedatum, exacte wijzigingsdatum (alleen grove tekst in detail), exact adres bij `showAddress=false` (43/50 chalets), kadastrale referentie, prijshistorie (alleen de laatste daling), makelaarsnaam in zoekresultaten (wél in detail), paginering/offset, sortering als parameter, "verkocht"-signaal (niet getest wat `outcome` bij een verwijderde advertentie zegt — open vraag).

**Correctie op het lokale feit van 14-09-2026:** "geen makelaarsnaam" geldt voor `search_properties`; `property_detail` geeft hem wel (`commercialName`).

## 5. (d) Toegestane wijzigingsdetectie

| Mechanisme | Wat het doet | Bron en bewijs |
|---|---|---|
| Opgeslagen zoekopdracht + e-mailalert | Na een zoekopdracht "Guardar búsqueda"; keuze direct / dagelijks / wekelijks; alert bij **nieuwe** advertenties die voldoen | Helpcentrum (403 voor ons) via zoekmachine-snippet; idealista/news 30-11-2015: "idealista buscará cada día casa por ti… te avisará con una alerta en tu móvil o con un email" (2) |
| Object volgen ("guardar para después") | Meldingen bij "cambios relevantes… (bajadas de precio, más fotos, etc)" voor dat ene object | idealista/news-forum, officieel antwoord 22-04-2013 (2, oud) |
| Prijsdaling als filter | **Bestaat niet als filter** op idealista.com; wel als sortering (`ordenado-por=rebajas-desc`). De assistent vertaalt "con bajada de precio" naar die sortering en negeert dan het type-filter (1.844 = alle woningen) | 3 — eigen test |
| "Últimas 48h" | Wél een filter: `con-publicado_ultimas-48-horas`; 6 chalets in Jávea op 14-09-2026 | 3 — eigen test |
| Automatisch verwerken van alert-mails | Niet geregeld in de voorwaarden die ik las. De mails komen in onze eigen mailbox; verwerken daarvan is geen toegang tot de website. Juridisch niet bevestigd | 7 — [te verifiëren, bij voorkeur door een jurist] |

**Praktisch (4):** de combinatie "opgeslagen zoekopdrachten per segment (chalets para reformar Jávea; terrenos urbanos Jávea; pisos para reformar Jávea) met dagelijkse e-mail" + "handmatig volgen van shortlist-objecten" is de enige route die nu zeker binnen de regels valt. Ze levert: NIEUW GEPUBLICEERD (via alert), PRIJS GEWIJZIGD (alleen gevolgde objecten). Ze levert niet: NIET MEER GEVONDEN, STATUS GEWIJZIGD op portaalniveau.

## 6. (e) Gebruiksvoorwaarden en aviso legal — de clausules

Bron: "Términos y Condiciones generales de idealista", pdf op `st1.idealista.com/ayuda/wp-content/uploads/2021/11/2021-Hasta-11-11-2021-Terminos-y-condiciones.pdf`, "Ultima actualización: 20 de noviembre, 2020" (officiële, gearchiveerde versie; bewijstype 2). Aanbieder: Idealista, S.A.U., Plaza de las Cortes, Madrid, NIF A82505660. De huidige versie (30-04-2025 volgens zoekresultaten) staat op `/ayuda/articulos/legal-statement/` en gaf HTTP 403; zoekmachine-snippets van die pagina tonen dezelfde bewoording (robots, spiders, scrapers; "written permission"; robot exclusion; resell/deep-link/monitor). Ik markeer de actualiteit als [te verifiëren in een browser].

**Verboden gedrag (§ "¿Qué no puedes hacer?"), letterlijk:**
> "Acceder, controlar o copiar cualquier información incluida en esta Web y apps utilizando para ello cualquier tipo de robot, spider, scraper u otro medio automático o proceso manual para cualquier propósito, sin nuestro permiso expreso y por escrito."

Verder in dezelfde lijst (parafrase): de restricties van robots-exclusie niet schenden en beveiligingsmaatregelen niet omzeilen; geen onredelijke last op de infrastructuur; geen links of replicatie van inhoud zonder schriftelijke toestemming.

**Gevolg bij overtreding (letterlijk):**
> "…responderás por cualquier daño y perjuicio… y acuerdas mantener indemne a idealista."

Plus eenzijdige beëindiging van toegang zonder vooraankondiging.

**§8.1 Propiedad Intelectual e Industrial (letterlijk):**
> "no está permitido revender, realizar deep-links, utilizar, copiar, monitorizar (por ejemplo, spider, scrape), mostrar, descargar, guardar o reproducir el contenido… para cualquier actividad comercial o competitiva sin autorización previa y por escrito por nuestra parte."

Ook: de gebruiker heeft "tan solo… un derecho de uso estrictamente personal y privado"; alle rechten op materialen liggen bij Idealista of licentiegevers.

**§8.2 (relevant als wij zelf publiceren):** wie op Idealista publiceert, geeft een wereldwijde, sublicentieerbare licentie, uitdrukkelijk ook "para realizar valoraciones y tasaciones de inmuebles, informes de precios, informes estadísticos, referencias históricas", ook na intrekking van de advertentie. Idealista bouwt daar zijn prijsrapporten en idealista/data op.

**Databankrecht:** de term "derecho sui generis" of "base de datos" komt in de pdf niet voor; Idealista beroept zich contractueel op intellectuele eigendom en op het verbod op automatische toegang. Het wettelijke databankrecht (TRLPI art. 133 e.v.) heb ik in deze stroom niet zelf gecontroleerd — [te verifiëren]. Een jurisprudentiezoektocht leverde geen gepubliceerde uitspraak "Idealista tegen scraper" op; algemene rechtspraak (TS 9-10-2012 Ryanair/Atrápalo; HvJ C-202/12; C-762/19) is alleen als context genoemd in secundaire bronnen (7).

**robots.txt (bewijstype 3, opgehaald 14-09-2026, HTTP 200):** één `User-agent: *`-blok; talrijke `Disallow`-regels (sorteringen, paginering, `/usuario/`, `/favoritos/`, meer dan drie filters), expliciete `Allow` voor taalversies en zoekpaden zoals `/en/venta-viviendas/`, en aan het eind van het taalblok `Disallow: /`. Idealista voorziet dus alleen gecontroleerde indexering; robots.txt is bovendien "geen gebruikslicentie" (masterprompt §7).

## 7. (f) idealista/tools en feedpublicatie

| Onderdeel | Bevinding | Bewijs |
|---|---|---|
| idealista/tools | CRM voor makelaars: objecten aanmaken, foto's, contactregistratie, "Genera tus propios Análisis Comparativos de Mercado (ACM)", MLS-koppeling, "Multipublicación en diferentes portales", eigen website | pdf "Servicios para profesionales inmobiliarios", nov. 2022, p. 7–8 (2) |
| Market Navigator via tools | "realiza valoraciones ilimitadas y obtén completos Estudios de Mercado de cualquier zona"; "Compara el precio y la demanda de tu inmueble respecto a tu competencia" | idem p. 12 (2) |
| Aanbod in een zone downloaden | Helpcentrum-artikel "Cómo analizar la oferta en una zona" zou professionele klanten laten downloaden welke objecten in een zone te koop staan, incl. leads per 1.000 bezoeken | zoekmachine-snippet; pagina 403 — 7, [te verifiëren]. **Dit is potentieel de belangrijkste legitieme leesroute voor een makelaarsaccount** |
| Feedpublicatie (Kyero XML → Idealista) | Derden melden dat Idealista eind 2018 van XML naar JSON-import is overgestapt en een ILC-code (Idealista Load Code) per bureau uitgeeft; officiële tools-help gaf 403 | 7 — [te verifiëren] |
| Publiceren als particulier | `get_howto listing.publish`: eerste 2 advertenties gratis, adres verbergen 9,90 €, gratis waardering | 1 — tool |
| Wat publicatie ons oplevert | Een professioneel account (voorwaarde voor tools/Market Navigator) en statistieken over eigen advertenties. **Geen** leesrecht op andermans advertenties; §8.2 geeft Idealista juist rechten op onze data | 2/4 |

Voor TREE Properties is de vraag dus niet "kunnen we onze feed naar Idealista sturen" (dat kan, via CRM-koppeling of JSON/ILC), maar "wat krijgt een professioneel account aan marktinzicht terug" — en dat vergt een klantaccount plus eventueel Market Navigator. Kosten: ONBEKEND.

## 8. (g) Openbare prijsrapporten per gemeente (Jávea)

| Punt | Bevinding | Bewijs |
|---|---|---|
| Ingang | `https://www.idealista.com/sala-de-prensa/informes-precio-vivienda/` (index venta/alquiler per comunidad → provincia → municipio) | URL gezien in zoekresultaten; pagina 403 (7) |
| Jávea-pagina's | Gevonden URL-patroon: `…/informes-precio-vivienda/alquiler/comunitat-valenciana/alicante-alacant/javea-xabia/historico/`; het venta-equivalent is aannemelijk maar niet zelf geopend | 4 — [te verifiëren] |
| Frequentie | **Maandelijks**, niet per kwartaal: augustus-cijfers gepubliceerd 02-09-2026 (Spanje 2.924 €/m², +12,5 % j/j, −0,3 % m/m) | idealista/news 02-09-2026 (2) |
| Methodiek | Sinds juli 2026 nieuwe methodiek, met terugwerkende kracht op de hele reeks: "Los nuevos filtros… permiten identificar y excluir del cálculo productos como el alquiler de temporada o vacacional" + robuustere uitschieterdetectie. Oudere overgenomen cijfers zijn dus niet meer één-op-één vergelijkbaar | idem (2) |
| Jávea-indicatie | Zoekmachine-snippet van `/en/valoracion-de-inmuebles/javeaxabia-alicante`: gemiddeld 3.958 €/m² (pisos 4.078, casas 3.609; Centro 3.086, Puerto 4.454). Peildatum onbekend; pagina zelf 403 | 7 — [te verifiëren] |
| Gebruik | Handmatig overnemen met bronvermelding en peildatum, zoals de leadgen-notitie al adviseerde | 2/4 |

## 9. (h) Meting Jávea-dekking met de Idealista-assistent (14-09-2026, bewijstype 3)

Alle aanroepen: `country=es`, `operation=SALE`, locatie "Jávea" in de query; `locationName` telkens "Jávea/Xàbia, Alicante".

| Zoekopdracht (query) | propertyType | Door de tool afgeleide filters (`summary`) | `total` | Getoond |
|---|---|---|---|---|
| chalets para reformar en Jávea | CHALET | Casas y chalets · Usada / para reformar | **70** | 50 |
| casas y chalets en venta en Jávea | CHALET | Casas y chalets | **1.275** | 3 |
| pisos en venta en Jávea | HOME | Pisos, áticos, dúplex | **569** | 50 |
| pisos para reformar en Jávea | HOME | Pisos, áticos, dúplex · Usada / para reformar | **19** | 3 |
| terrenos en venta en Jávea | LAND | (geen extra filter) | **333** | 50 |
| terrenos urbanos edificables en Jávea | LAND | Urbanos · Urbanizables | **238** | 3 |
| obra nueva en venta en Jávea | HOME | Promociones de obra nueva | **77** | 5 |
| viviendas de bancos en Jávea | HOME | De bancos | **0** | 0 |
| chalets de bancos o en subasta en Jávea | CHALET | Casas y chalets · De bancos | **0** | 0 |
| chalets con bajada de precio en Jávea | CHALET | (geen filter; sortering `rebajas-desc`; type-filter genegeerd) | 1.844 | 5 |
| chalets publicados en las últimas 48 horas en Jávea | CHALET | Casas y chalets · Últimas 48h. | **6** | 3 |
| chalets rebajados para reformar en Jávea entre 300000 y 900000 euros | CHALET | 300.000 a 900.000 eur · Casas y chalets · Usada / para reformar ("rebajados" genegeerd) | **49** | 3 |
| houses to renovate in Jávea under 500000 euros (en-GB) | CHALET | Up to 500,000 euros · Houses · Pre-owned / needs renovating | **15** | 3 |

**Analyse van de 50 getoonde chalets para reformar:** 50 unieke codes; prijs 280.000–2.595.000 €, mediaan 750.000 €; 26 van 50 ≥ 750.000 €; 49 professioneel / 1 particulier; 32 verschillende doorschakelnummers (ruwe indicatie van het aantal aanbieders); 7 met zichtbaar adres; 2 met prijsdaling; subtypen: 35 vrijstaand, 5 rijtjes, 4 countryHouse, 2 casa de pueblo, 1 masía, 1 halfvrijstaand; status bij alle 50 "renew".
**Terrenos (50 van 333):** 150.000–3.100.000 €, mediaan 500.000 €; subtypen buildingLand 19, urban 15, onbenoemd 16; 48 professioneel.
**Pisos (50 van 569):** 260.000–1.300.000 €, mediaan 470.000 €; status good 39 / newdevelopment 9 / renew 2.

**Betekenis (4):** "de bancos" is in Jávea leeg — bankbezit moet uit andere bronnen komen (stroom veilingen/servicers). De 70 renovatie-chalets en 238 bouwrijpe percelen zijn het relevante speelveld; met maximaal 50 per aanroep en zonder offset zijn per segment 2–5 deelzoekopdrachten (prijsbanden) nodig voor volledige dekking. De teller `total` is betrouwbaar als nulmeting, maar zonder publicatiedatum is "nieuw" alleen via het 48-uursfilter te benaderen.

## 10. Bronnenregister — per toegangsroute (statussen uit masterprompt §7)

| # | Route | Type | Toegang | Status | Toelichting |
|---|---|---|---|---|---|
| 1 | idealista.com portaal, geautomatiseerd lezen | Portaal | Verboden in T&C; HTTP 403 op tools; robots.txt `Disallow: /` | **NIET GEBRUIKEN** | Ook geen "even handmatig geautomatiseerd" |
| 2 | Search API — developers.idealista.com | Officiële API (lezen) | Aanvraagformulier; voorwaarden pas na acceptatie | **CONTRACT OF TOESTEMMING NODIG** | Aanvraag is een besluit van Jan; projectbeschrijving eerlijk formuleren |
| 3 | idealista/data (API testigos/valoraciones, AVM, Market Navigator, maatwerkbestanden) | Commerciële dataleverancier | Contactformulier; prijs en licentie onbekend | **CONTRACT OF TOESTEMMING NODIG** | Enige officiële route naar comparables en prijshistorie |
| 4 | Idealista-assistent (MCP / ChatGPT-app) | Officiële consumententool | Werkt in deze sessie; ≤50 per aanroep; geen paginering | **ALLEEN HANDMATIG** (ad hoc); systematisch gebruik: **CONTRACT OF TOESTEMMING NODIG** | Voorwaarden regelen gepland gebruik niet |
| 5 | Opgeslagen zoekopdrachten + e-mailalerts; objecten volgen | Zoekmeldingen | Gratis account | **ALLEEN HANDMATIG** | Automatisch verwerken van eigen alert-mails: TECHNISCH ONDERZOEK NODIG (+ juridische check) |
| 6 | idealista/tools + Market Navigator (professioneel account) | Makelaarssoftware / datatool | Klantaccount vereist; kosten onbekend | **CONTRACT OF TOESTEMMING NODIG** | Mogelijk zone-download van aanbod; [te verifiëren] |
| 7 | Feedpublicatie naar Idealista (JSON/ILC via CRM, Kyero-koppeling) | Publicatiekoppeling | Professioneel account | **TECHNISCH ONDERZOEK NODIG** | Publiceren ≠ lezen; geeft geen marktdekking |
| 8 | Openbare prijsrapporten (sala-de-prensa, valoración-pagina's) | Publicatie | Alleen browser (tools krijgen 403) | **ALLEEN HANDMATIG** | Maandelijks; methodiekbreuk juli 2026 |

Velden per masterprompt §7 die voor álle routes ONBEKEND blijven: rate limits (behalve 50/aanroep bij route 4), kosten (routes 2, 3, 6), contractstatus (geen), rechten voor AI-analyse en afgeleide gegevens (niet gepubliceerd), opslag- en bewaarbeperkingen (niet gepubliceerd), contactpersoon (alleen formulieren).

## 11. Open vragen

1. Wat zijn de werkelijke voorwaarden, limieten en kosten van de Search API — en mag hij advertenties van derden teruggeven voor acquisitiedoeleinden? (Alleen via aanvraag te beantwoorden.)
2. Wat kost idealista/data voor Jávea/Marina Alta (testigos-API, prijshistorie) en welke rechten geeft de licentie voor opslag, afgeleide data en AI-analyse?
3. Regelt Idealista ergens (OpenAI-appvoorwaarden, MCP-servervoorwaarden) het gebruik van de assistent door bedrijven en door geplande taken? Schriftelijk navragen bij Idealista.
4. Wat geeft `property_detail.outcome` terug bij een verwijderde of verkochte advertentie? (Niet getest; bepalend voor "NIET MEER GEVONDEN".)
5. Is de huidige T&C-versie (30-04-2025) inhoudelijk gelijk aan de gelezen pdf-versie van 20-11-2020? In een browser controleren.
6. Bestaat de zone-download in idealista/tools ("Cómo analizar la oferta en una zona") nog en voor welke abonnementen?
7. Mag een ontvanger zijn eigen Idealista-alertmails automatisch parsen (geen toegang tot de site)? Juridisch advies.
8. Welke exacte URL en peildatum horen bij het Jávea-prijsrapport (venta), en zijn de cijfers per wijk beschikbaar?

## 12. Geblokkeerd of mislukt (niet omzeild)

- HTTP 403 (WebFetch én één enkelvoudige curl): `/informacion/aviso-legal/`, `/ayuda/articulos/legal-statement/` (es en en), `/ayuda/categorias/alertas-inmueble/`, `/ayuda/articulos/how-to-subscribe-to-the-alerts-service/`, `/sala-de-prensa/informes-precio-vivienda/` (index, CV-report, Jávea-historico), `/en/valoracion-de-inmuebles/javeaxabia-alicante`, `/peritos/`, `/tools/centrodeayuda/*` (publicación, ACM, oferta-en-una-zona), `/en/tools/software-recomendado-para-inmobiliarias`, idealista.pt en idealista.it voorwaardenpagina's, help.openai.com en openai.com/index (apps in ChatGPT), medium.com (API-artikel).
- ECONNREFUSED: tracker.terminosycondiciones.es/doc/721.
- Leeg/JS-only: apidojo.net/documentations/idealista.
- Eén MCP-aanroep (obra nueva, maxResults 50) faalde met een SSE-parsefout; herhaald met maxResults 5, geslaagd.
- Pdf "Servicios para profesionales" (nov. 2022) kon niet door WebFetch worden gelezen; tekst geëxtraheerd met macOS PDFKit (geen installatie) — inhoud dateert van 2022.
- Niet gedaan, bewust: geen requests met gewijzigde User-Agent, geen proxies, geen herhaalde bulkverzoeken, geen scraping-diensten van derden (Apify, ScrapingBee, "AnythingMCP" e.d. zijn geen geautoriseerde bronnen — masterprompt §6).

## 13. Bronnenlijst (URL · controledatum · bewijstype)

| Bron | URL | Datum | Type |
|---|---|---|---|
| developers.idealista.com (302 → access-request) | https://developers.idealista.com/ | 14-09-2026 | 2/3 |
| Request API access | http://developers.idealista.com/access-request | 14-09-2026 | 2 |
| Request API access (help) | https://developers.idealista.com/access-request?action=help | 14-09-2026 | 2 |
| idealista/data — overzicht | https://www.idealista.com/data/ | 14-09-2026 | 2 |
| idealista/data — API comparables y métricas | https://www.idealista.com/data/asesoramiento-inmobiliario-tecnologico/api-comparables-y-metricas/ | 14-09-2026 | 2 |
| idealista/data — valoración automática | https://www.idealista.com/data/consultoria-inmobiliaria/valoracion-automatica/ | 14-09-2026 | 2 |
| idealista/data — servicios agencias | https://www.idealista.com/data/agencias-inmobiliarias-servicios/ | 14-09-2026 | 2 |
| idealista/data — estudios de mercado | https://www.idealista.com/data/estudios-de-mercado/ | 14-09-2026 | 2 |
| idealista/news — app op ChatGPT | https://www.idealista.com/en/news/property-for-sale-in-spain/2026/03/13/887103-idealista-launches-its-app-on-chatgpt | 14-09-2026 | 2 |
| idealista/news — prijsindex augustus 2026 + methodiek | https://www.idealista.com/news/inmobiliario/vivienda/2026/09/02/912069-el-precio-de-la-vivienda-acumula-20-meses-de-subidas-anuales-a-doble-digito-tras-el | 14-09-2026 | 2 |
| idealista/news — alerts (2015) | https://www.idealista.com/news/inmobiliario/vivienda/2015/11/30/740133-estate-alerta-las-casas-te-buscan | 14-09-2026 | 2 |
| idealista/news-forum — aviso bajada de precio (2013) | https://www.idealista.com/news/foro/alquiler/608479-me-quiero-dar-de-alta-para-recibir-un-aviso-de-bajada-de-precio-de-un-piso | 14-09-2026 | 2 |
| Términos y Condiciones (pdf, versie 20-11-2020) | https://st1.idealista.com/ayuda/wp-content/uploads/2021/11/2021-Hasta-11-11-2021-Terminos-y-condiciones.pdf | 14-09-2026 | 2 |
| Términos y Condiciones (pdf, versie 01-04-2020) | https://st1.idealista.com/ayuda/wp-content/uploads/2020/04/2020-En-curso-Terminos-y-condiciones.pdf | 14-09-2026 | 2 |
| Términos y Condiciones — huidige pagina (403; alleen snippet) | https://www.idealista.com/ayuda/articulos/legal-statement/?lang=en | 14-09-2026 | 7 |
| Servicios para profesionales (pdf, nov. 2022) | https://st3.idealista.com/static/es/pdf/es/servicios_profesionales_idealista.pdf | 14-09-2026 | 2 |
| robots.txt | https://www.idealista.com/robots.txt | 14-09-2026 | 3 |
| Sala de prensa — prijsrapporten (403) | https://www.idealista.com/sala-de-prensa/informes-precio-vivienda/ | 14-09-2026 | 7 |
| Jávea alquiler-historico (URL uit zoekresultaat; 403) | https://www.idealista.com/sala-de-prensa/informes-precio-vivienda/alquiler/comunitat-valenciana/alicante-alacant/javea-xabia/historico/ | 14-09-2026 | 7 |
| Valoración Jávea (403; alleen snippet) | https://www.idealista.com/en/valoracion-de-inmuebles/javeaxabia-alicante | 14-09-2026 | 7 |
| Helpcentrum alerts (403; alleen snippet) | https://www.idealista.com/ayuda/categorias/alertas-inmueble/ | 14-09-2026 | 7 |
| idealista/tools help — oferta en una zona (403; alleen snippet) | https://www.idealista.com/tools/centrodeayuda/articulos/como-analizar-la-oferta-en-una-zona/ | 14-09-2026 | 7 |
| Idealista-assistent (MCP) — tooldefinities, guide, 13 zoekopdrachten, 2 details | (MCP-server in deze sessie; URL's in resultaten dragen utm_campaign=appChatgpt) | 14-09-2026 | 1/3 |
| Onofficiële API-client (readme) | https://github.com/yagueto/idealista-api | 14-09-2026 | 7 |
| Interne notitie marktdata (25/26-08-2026) | ~/tree-es/properties/leadgen/docs/marktdata-bronnen.md | 14-09-2026 | 3 |

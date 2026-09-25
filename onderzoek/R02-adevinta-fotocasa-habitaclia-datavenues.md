# R02 — Adevinta-portalen als leesbron: Fotocasa, Habitaclia, Milanuncios en DataVenues

> **NA TEGENSPRAAK (15-09-2026).** Dit rapport is door een tweede agent gecontroleerd; zie `R02-adevinta-fotocasa-habitaclia-datavenues.verificatie.md`. Betrouwbaarheid volgens die controle: middel.
> Weerlegd en in de eindstukken gecorrigeerd: R02-02; R02-08; R02-17; R02-18; R02-19. Gebruik voor die punten de gecorrigeerde tekst in het verificatiebestand, niet de tekst hieronder.


**Project:** TREE Deal Hunter, fase A, onderzoeksstroom R02
**Controledatum:** 14-09-2026 (alle bronnen op deze datum geraadpleegd, tenzij anders vermeld)
**Bewijstypen** (masterprompt §5): 1 door aanbieder vermeld · 2 in officiële bron aangetroffen · 3 door ons rechtstreeks vastgesteld · 4 AI-inferentie · 5 berekening op benoemde aannames · 6 door bevoegde professional bevestigd · 7 onbekend of tegenstrijdig
**Werkwijze:** uitsluitend openbare pagina's via WebFetch/curl (enkelvoudige verzoeken, geen bulk, geen omzeiling van blokkades), lokale bestanden alleen gelezen. De WebSearch-quotum van de sessie raakte halverwege op; het restant is met WebFetch, curl en de openbare WordPress-JSON van prensa.fotocasa.es gedaan.

## Samenvatting (10 regels)

1. Geen van de drie portalen biedt een officiële lees-API, leesfeed of dataset voor derden; Fotocasa Pro is uitsluitend een **publicatiekoppeling** (API key, één richting: CRM → Fotocasa/Habitaclia/Milanuncios).
2. Fotocasa en Habitaclia draaien op één platform onder één rechtspersoon, **Fotocasa Group, S.L.U.** (voorheen Adevinta Real Estate S.L.U.), sinds maart 2026 geconsolideerd door Scout24 (ImmoScout24); Milanuncios staat onder **Adevinta Motor S.L.U.** maar zit nog in de Fotocasa Pro-packs.
3. Geautomatiseerd uitlezen is contractueel niet toegestaan (Habitaclia/Fotocasa: geen reproductie of exploitatie van content zonder uitdrukkelijke toestemming) en technisch afgeschermd (Milanuncios blokkeert curl met "Pardon Our Interruption"; de hulpcentra van alle drie geven HTTP 403). De aviso legal van fotocasa.es zelf laadt alleen via JavaScript en kon niet worden geciteerd.
4. Alle commerciële "Fotocasa API's" (Happy Endpoint, Apify, Oxylabs, WebScrapingHub, Spider) zijn scrapers zonder autorisatie → **NIET GEBRUIKEN**.
5. Legitieme leesroutes zijn de portaaleigen alerts: Fotocasa (account + gemeente verplicht, e-mail/app "en pocos minutos", filter "a reformar", geen verzending 00:00–06:00), Habitaclia ("Recibir alertas por email") en Milanuncios ("Guardar búsqueda") → **ALLEEN HANDMATIG**.
6. De Índice Inmobiliario Fotocasa heeft een openbare pagina voor Jávea/Xàbia (september 2026: 4.236 €/m² verkoop, +11,0 % j/j, +81 % over de reeks) met negen wijken; methodologie: alleen pisos y áticos, dus géén villa-/perceelindex.
7. **DataVenues** (Fotocasa Pro Data) is de enige geautoriseerde route naar de gecombineerde aanbod-data van de drie portalen, met dagelijks ververste particulieren-advertenties incl. eigenaarscontact (DataVenues GO, 27-02-2026) en notariële sluitprijzen (29-05-2026). Prijzen niet gepubliceerd; licentievoorwaarden (opslag, AI-analyse, afgeleide data) nergens gevonden → **CONTRACT OF TOESTEMMING NODIG**.
8. datavenues.com was op 14-09-2026 onbereikbaar (time-out vanaf twee onafhankelijke routes); de aanvraagroute loopt via het Fotocasa Pro-formulier, 900 823 825 (bestaande klanten) of support@datavenues.com.
9. Indicatieve telling Jávea/Xàbia (14-09-2026, openbare zoekpagina's): Fotocasa 1.806 woningen / 51 "a reformar" / 295 terrenos; Habitaclia 1.758 woningen / 285 terrenos y solares / 7 particulieren; Milanuncios 2.735 woningen / 38 particulieren / 275 terrenos.
10. Advies voor de architectuur: de drie portalen alleen als handmatige alert-bronnen en als openbare prijsreferentie; DataVenues als te onderzoeken betaalde licentie (offerte + schriftelijke voorwaarden opvragen); geen enkele scraping-component bouwen.

---

## 1. Eigendom en structuur (context voor rechten en contactroute)

| Feit | Bewijs | Bron | Type |
|---|---|---|---|
| EQT kondigde op 23-07-2025 de overname van Adevinta Spain aan (Milanuncios, Fotocasa, Habitaclia, InfoJobs, coches.net), "más de 2.000 millones de euros", afronding "previsiblemente en el primer trimestre de 2026" | secundaire nieuwsbron | realtyinvestor.eu | 7 (niet in officiële EQT-bron nagelezen) |
| Scout24 SE kondigde op 18-09-2025 de overname van Fotocasa en Habitaclia van EQT aan, EV ca. EUR 153 mln; "subject to customary regulatory approvals and the prior completion of EQT's acquisition of Adevinta Spain, with closing expected within the next six months"; ca. 1 mln advertenties, ca. 14k makelaarsklanten, >8 mln maandelijkse gebruikers; merken blijven bestaan | officieel persbericht | scout24.com | 2 |
| Milanuncios en DataVenues worden in het Scout24-persbericht niet genoemd | zelf gecontroleerd | scout24.com | 3 |
| Scout24 Q2-2026-bericht (06-08-2026): "the Spanish business consolidated for a complete quarter for the first time in the second quarter"; consolidatie "as of March 2026"; entiteit "Fotocasa Group S.L.U. (formerly: Adevinta Real Estate S.L.U.)" | officieel IR-bericht | scout24.com | 2 |
| Footer fotocasa.es (14-09-2026): "©2026 Fotocasa Group, S.L.U." en blok "Fotocasa Group: Fotocasa · Habitaclia · ImmoScout24" met link naar immobilienscout24.de | zelf gezien | fotocasa.es | 3 |
| Aviso legal Habitaclia: "Identidad: Fotocasa Group, S.L.U. (en adelante, la Empresa o Habitaclia) CIF: B-70677125", Registro Mercantil de Madrid M-814608, "Calle Rosario Pino, 14-16, planta 10, 28020 Madrid" | officiële juridische tekst | habitaclia.com | 2 |
| Footer milanuncios.com (juridische sectie): "© 2026 Adevinta Motor S.L.U." | zelf gezien via WebFetch | milanuncios.com | 3 |
| Fotocasa Pro-packs (Start/Basic/Premium) bevatten op 14-09-2026 nog "Publicación ilimitada" op de drie portalen Fotocasa, habitaclia en Milanuncios | aanbieder | pro.fotocasa.es | 1 |
| Fotocasa Group zou bestaan uit Fotocasa, Habitaclia, Fotocasa Pro, DataVenues, Witei en Inmoweb; deal "completed" (artikel 06-03-2026) | secundaire vakpers | onlinemarketplaces.com | 7 (consistent met Scout24 Q2-bericht, maar samenstelling niet officieel bevestigd) |

**Gevolg voor ons:** de contractuele wederpartij voor Fotocasa, Habitaclia, Fotocasa Pro en DataVenues is nu Fotocasa Group, S.L.U. (Madrid); voor Milanuncios een andere Adevinta-entiteit. Wie DataVenues-licenties juridisch uitgeeft is niet in een primaire bron gezien → [te verifiëren] bij offerte.

---

## 2. Fotocasa (fotocasa.es)

### 2a. Publiceren versus lezen

| Vraag | Bevinding | Bron | Type |
|---|---|---|---|
| Bestaat er een officiële **lees-API** (advertenties of marktdata van anderen)? | **Niet gevonden.** Geen enkele Fotocasa- of Fotocasa Pro-pagina noemt een lees-API, leesfeed, dataset of developer-portaal. pro.fotocasa.es/recursos/ bevat alleen blog, Índice, Informes en Research; geen technische documentatie. De pagina "Fotocasa Pro Data Flow" uit de zoekresultaten geeft HTTP 404. | pro.fotocasa.es | 3 |
| Bestaat **Fotocasa Pro** als publicatiekoppeling? | Ja. Fotocasa Pro is sinds 18-02-2021 het gezamenlijke professionele merk van Fotocasa, habitaclia en Milanuncios. Publicatie via CRM vereist een door Fotocasa uitgegeven **API key**: Witei: "API key (you can find it yourself from Fotocasa, following the steps defined in its guide)"; Inmoweb: "Completa el campo proporcionado por Fotocasa: «API key»". Beide handleidingen beschrijven uitsluitend het **versturen** van advertenties; geen leesfunctie. | blogprofesional.fotocasa.es; faq.witei.com; ayuda.inmoweb.es | 1 |
| Technisch formaat en frequentie van de publicatiekoppeling | Een CRM-leverancier (InmoCMS, secundair) beschrijft twee opties: een JSON-feed die Fotocasa "cada 15 minutos" inleest, of een realtime API. **Niet in een Fotocasa-bron gezien.** | inmocms.com | 7 |
| Publieke technische documentatie van de Fotocasa Pro-API | Niet gevonden; fotocasa.pro/u/login en fotocasa.pro/u/aviso_legal laden alleen via JavaScript (WebFetch kreeg alleen de titel). | fotocasa.pro | 3 |
| Commerciële "Fotocasa API's" van derden | Happy Endpoint: "If you need already scraped data in CSV and Excel ready or need us to scrape data for you, contact us." Geen verwijzing naar toestemming van Fotocasa. Apify, Oxylabs, WebScrapingHub en Spider adverteren expliciet met het omzeilen van Akamai/Cloudflare-botbeveiliging. | docs.happyendpoint.com e.a. | 1 (eigen verklaring van de scraper-aanbieders) |
| Conclusie | **Publiceren: mogelijk via Fotocasa Pro-contract + API key. Lezen: geen geautoriseerde technische route.** Een publicatiekoppeling geeft geen recht op de markt (masterprompt §6). | — | 4 |

### 2b. Gebruiksvoorwaarden over geautomatiseerde toegang

| Document | Wat er staat | Bron | Type |
|---|---|---|---|
| Aviso legal fotocasa.es (`/es/aviso-legal/ln`) | **Niet leesbaar zonder JavaScript**: HTML van 409 kB bevat alleen de footer; de juridische tekst wordt client-side geladen. Twee WebFetch-pogingen en één curl gaven alleen navigatie. → tekst **[te verifiëren]** door Jan handmatig in de browser te openen en op te slaan. | fotocasa.es | 3 (blokkade vastgesteld) |
| Términos y condiciones "Fotocasa Alquiler" (gestión de alquiler, zelfde merk, wél leesbaar) | Entiteit "Adevinta Real Estate S.L.U." (oude naam). Verboden: "Reproducir, copiar, distribuir, transformar o modificar la información y los contenidos alojados en la Plataforma, a menos que cuente con la autorización del titular" en "El Usuario no deberá escanear o poner a prueba la vulnerabilidad de cualquier sistema o red de FOTOCASA". Geen expliciet woord "robot" of "scraping" aangetroffen. | fotocasa.es/gestion-alquiler/terminos-y-condiciones/ | 2 |
| Condiciones Generales Habitaclia (zelfde rechtspersoon en platform, zie §3) | Toegang tot de site "ni confiere ningún derecho de utilización, alteración, transformación, explotación (en cualquiera de sus modalidades), reproducción, distribución o comunicación pública sobre los contenidos [...] sin la previa y expresa autorización". Geen clausule over robots/automatische toegang gevonden (0 treffers op "robot", "automat", "scrap", "sui generis"). | habitaclia.com | 2 |
| robots.txt fotocasa.es | Verbiedt een lijst downloadtools (HTTrack, wget, libwww, Teleport, WebCopier, e.a.) volledig ("Disallow: /") en voor alle agents o.a. `/buscar/`, `/clientbin/`, `/facebookconnect/`. Let op: robots.txt is geen gebruikslicentie (masterprompt §7). | fotocasa.es/robots.txt | 3 |
| Hulpcentrum ayuda.fotocasa.es (Zendesk) | HTTP 403 voor WebFetch; artikelen "Crear mis alertas" en "Modificar las alertas" niet leesbaar. | ayuda.fotocasa.es | 3 |
| Eerder intern onderzoek 25/26-08-2026 | "Bouw geen scraper. Niet voor Idealista, niet voor Fotocasa." | ~/tree-es/properties/leadgen/docs/marktdata-bronnen.md r. 88 | 3 |

**Oordeel (type 4):** de leesbare voorwaarden van de groep verbieden reproductie/exploitatie van content zonder toestemming; de site is bovendien actief tegen bots beveiligd. Geautomatiseerd lezen van fotocasa.es valt buiten wat aantoonbaar is toegestaan → voor systematische verwerking **NIET GEBRUIKEN** zonder schriftelijke toestemming.

### 2c. E-mailalerts (handmatige, toegestane leesroute)

| Kenmerk | Bevinding | Bron | Type |
|---|---|---|---|
| Voorwaarden om een alert te maken | Account nodig; minimaal één gemeente kiezen ("Crear alerta" werkt niet op regio-niveau) | zoekresultaat ayuda.fotocasa.es (pagina zelf 403) | 7 |
| Kanalen en snelheid | E-mail of app-notificatie, "en pocos minutos" na publicatie; geen verzending "entre las doce y las seis de la mañana"; meerdere advertenties per bericht; frequentie instelbaar; filters aanpasbaar zonder alert te verwijderen; expliciet filter "a reformar" genoemd | fotocasa.es/fotocasa-life (27-11-2020) | 1 |
| Prijsdaling-alert | Filter "Con precio rebajado" bestaat, in 2023 alleen in de app: "por el momento no está disponible en la web de Fotocasa"; geldt voor zoekopdrachten, niet voor favorieten | fotocasa.es/fotocasa-life (16-11-2023) | 1 |
| Gedeelde alerts | Sinds 07-08-2025: één alert delen via WhatsApp/Telegram/e-mail/link; ontvangers "recibirán los mismos anuncios al mismo tiempo" | fotocasa.es/fotocasa-life (07-08-2025) | 1 |
| Ingang | "Mis alertas" → `/es/user/alerts` | footer fotocasa.es | 3 |
| Limiet op aantal alerts, retentie, toegestane verwerking van de alert-e-mails | ONBEKEND (hulpcentrum 403; voorwaarden niet leesbaar) | — | 7 |

**Praktisch:** alerts zijn bedoeld voor eindgebruikers. Of het doorsturen van alert-mails naar een eigen mailbox en het automatisch parsen daarvan binnen de voorwaarden valt, is niet vastgesteld → open vraag (zie §8).

### 2d. Índice Inmobiliario Fotocasa

| Kenmerk | Bevinding | Bron | Type |
|---|---|---|---|
| Bestaan en frequentie | Maandelijks sinds januari 2005 (verkoop); huurindex sinds december 2006; "desglosados por comunidades autónomas, provincias, municipios, distritos, barrios y principales calles" | fotocasa.es/indice-precio-vivienda; methodologie-pdf | 1 / 2 |
| Zit Jávea erin? | **Ja.** Pagina "Precio de venta de viviendas en Jávea \| Xàbia \| septiembre de 2026": 4.236 €/m² (september 2026), augustus 2026: 4.212 €/m²; variatie +0,6 % maand, +2,0 % kwartaal, +11,0 % jaar, +81 % over de hele reeks; "Fuente de los datos: Anuncios de Fotocasa". Ook Dénia (3.741), Benitachell (3.920), Teulada (2.840), Calpe (4.132) en de provincie Alicante (3.168) hebben een pagina. | fotocasa.es/es/indice-precio-vivienda/javea-xabia/todas-las-zonas; .../alicante-provincia/todas-las-zonas | 3 |
| Wijkniveau Jávea (sept 2026, €/m²) | Cap Martí–El Tossalet–Pinomar 4.679 · Centro ciudad 3.679 · La Granadella–Costa Nova 3.713 · Montañar–El Arenal 4.364 · Montgó–Ermita 4.162 · Partida Tosal–Zona dels Castellans 3.203 · Partides comunes–Adsubia 4.185 · Portichol–Balcón al Mar 5.545 · Puerto 4.418 | zelfde pagina | 3 |
| Methodologie (officiële pdf, huurvariant 2017; de verkoopvariant-URL gaf 404) | Vraagprijzen, geen transactieprijzen; particulieren én professionals; "La información se refiere a pisos y áticos, se excluyen otras viviendas, como apartamentos, dúplex y lofts y las unifamiliares, torres, chalés y casas adosadas"; filters: 25–300 m², 50.000–2.500.000 €, 100–15.000 €/m²; minimale steekproef 56–64 waarnemingen per categorie, anders "ns"; gemiddelde van de laatste 4 weken | prensa.fotocasa.es/wp-content/uploads/2017/12/Metodologia-indice-alquiler.pdf | 2 |
| Consequentie voor Jávea | De index meet flats/penthouses; het Jávea-segment dat ons interesseert (villa's, percelen, renovatie-objecten) valt buiten de steekproef. Bruikbaar als marktbarometer, niet als waardering per object. | — | 4 |
| Maandelijkse persberichten met gemeentetabellen | Persbericht 31-08-2026: "El precio medio de la vivienda de segunda mano sube en el 93% de los 591 municipios con variación interanual analizados por Fotocasa"; bijbehorende pdf (12 p.) bevat alleen uitschieter-tabellen; Jávea komt daarin niet voor (wel Alicante-provincie: +14,7 % j/j). Zoekopdracht op "Jávea" in de perssite geeft 5 berichten; o.a. rendementsbericht 26-06-2025: "Jávea / Xàbia (4,7%)" bruto huurrendement. | prensa.fotocasa.es (WP-JSON search); NdP-Espana-VENTA-Agosto-2026.pdf | 3 |
| Download-/API-mogelijkheid van de index | Niet gevonden; alleen webpagina's en persberichten met pdf. Rechten op hergebruik van de indexcijfers: ONBEKEND. | — | 7 |

### 2e. Indicatieve meting aanbod Jávea (openbare zoekpagina, 14-09-2026)

Uitgevoerd met enkelvoudige WebFetch-verzoeken op de openbare zoek-URL's (geen scraping, geen paginering). Fotocasa toonde geen captcha of cookiemuur aan WebFetch.

| Zoekopdracht | Kop op de pagina | URL | Type |
|---|---|---|---|
| Alle woningen te koop | "1.806 Casas y pisos en Jávea / Xàbia" | fotocasa.es/es/comprar/viviendas/javea-xabia/todas-las-zonas/l | 3 |
| Situación "a reformar" | "51 Casas y pisos a reformar en Jávea / Xàbia" (paginatitel identiek; filterblok "Situación de la vivienda" aanwezig). Kanttekening: de samenvattende tool twijfelde of alle getoonde kaarten het filter droegen; de kop en titel zijn wel eenduidig. | .../todas-las-zonas/a-reformar/l | 3 |
| Terrenos | "295 Terrenos en Jávea / Xàbia" | fotocasa.es/es/comprar/terrenos/javea-xabia/todas-las-zonas/l | 3 |
| Vergelijking met Idealista (lokaal feit 14-09-2026) | Idealista-assistent: 70 casas/chalets "para reformar", 238 terrenos | intern | 3 |

Waargenomen labels op advertentiekaarten: "Más de 3 meses", "ayer" (grove publicatieleeftijd), "Oportunidad", "Calidad Fotocasa" (type 3). Fotocasa toont dus wél een ruwe ouderdomsindicatie, maar geen exacte publicatiedatum in de lijstweergave.

### 2f. Particuliere verkopers op Fotocasa

"Publicar un anuncio como particular en Fotocasa es totalmente GRATIS"; tweede advertentie van hetzelfde type 19,95 €; adres verbergen 9,95 €; "Los anuncios de venta tienen una duración de 365 días" (fotocasa.es/es/poner-anuncio-gratis, type 1). Een filter "alleen particulieren" is op de Fotocasa-zoekpagina niet gezien (type 3, niet uitputtend). De particulieren-laag wordt commercieel via DataVenues verkocht (zie §5).

---

## 3. Habitaclia (habitaclia.com)

| Vraag | Bevinding | Bron | Type |
|---|---|---|---|
| Relatie met Fotocasa | Zelfde rechtspersoon (Fotocasa Group, S.L.U., CIF B-70677125, Madrid). Fotocasa Pro publiceert één advertentie op beide portalen; "Gestor de oportunidades" bundelt belnotificaties van Fotocasa én habitaclia; tellingen voor Xàbia zijn vrijwel gelijk (1.758 vs. 1.806). Fotocasa Pro noemt voor habitaclia "+5000 profesionales", "18M de visitas al mes", "900K de viviendas en contenido". | habitaclia.com/hab_cliente/legalavisocontentmodal.asp; pro.fotocasa.es/habitaclia/ | 2 / 1 / 3 |
| Eigen API of feed | Niet gevonden. De Condiciones Generales noemen geen XML, API of import (0 treffers). Publicatie voor professionals loopt via Fotocasa Pro ("desde un único panel centralizado"). Historisch bestond een eigen professionele omgeving (`hab_cliente`), maar dat is geen leesroute. | habitaclia.com; pro.fotocasa.es | 3 |
| Voorwaarden | Zie §2b: uitdrukkelijk verbod op reproductie/exploitatie zonder toestemming; foto's door adverteerders geüpload worden om niet aan het bedrijf gelicentieerd; geen expliciete robot-clausule. Wijzigingen worden "con 30 días de antelación" aangekondigd. | habitaclia.com | 2 |
| robots.txt | Verbiedt o.a. `/hab_usuarios/ajax/*`, `/hab_inmuebles/ajax/*`, alle sorteer-/filter-querystrings (`*ordenar=`, `*pag=`, `*hMinLat=` …) en `/*contactar.htm`. Geen licentie. | habitaclia.com/robots.txt | 3 |
| Dekking Costa Blanca (Xàbia, 14-09-2026) | "1.758 anuncios de viviendas en venta en Xàbia"; "285 anuncios de terrenos y solares en venta en Xàbia" (subcategorieën: terrenos residenciales, fincas rústicas, solares industriales, suelos para equipamientos, solares urbanos — zonder aantallen); "7 anuncios de viviendas de particulares en venta en Xàbia". Ook wijkpagina's (Montañar–El Arenal, Puerto). | habitaclia.com/viviendas-xabia.htm; .../terrenos_y_solares-xabia.htm; .../viviendas-particulares-xabia.htm | 3 |
| Filter "para reformar" | Geen URL-filter gevonden; de geprobeerde URL viel terug op de algemene pagina (1.758). Of het filter in de interface bestaat: ONBEKEND. | habitaclia.com | 3 / 7 |
| Alerts | Zoekpagina toont "Recibir alertas por email" en "Crear alerta"; hulpcentrum ayuda.habitaclia.com geeft 403. Frequentie en limieten: ONBEKEND. | habitaclia.com | 3 / 7 |
| Publicatie-/wijzigingsinformatie, historie | Niet zichtbaar in lijstweergave; niet onderzocht op detailniveau (zou herhaalde verzoeken vergen). | — | 7 |

**Oordeel:** Habitaclia levert voor Jávea geen ander aanbod dan Fotocasa (zelfde database), maar biedt wél een aparte particulieren-pagina (7 objecten) en een aparte terrenos-pagina. Status: **ALLEEN HANDMATIG** (alerts, zoekpagina).

---

## 4. Milanuncios (milanuncios.com, categorie inmobiliaria)

| Vraag | Bevinding | Bron | Type |
|---|---|---|---|
| Relevantie voor particulieren en percelen | Jávea/Xabia (14-09-2026): "2.735 anuncios" woningen te koop (kanttekening: de samenvattende tool zag ook een niet-vastgoedkaart in de lijst, dus mogelijk bredere categorie), "Venta de viviendas particular en Jávea/Xabia" **38 anuncios**, "Terrenos en Jávea/Xabia" **275 anuncios**. De categorie inmobiliaria onderscheidt viviendas, locales, oficinas, naves, terrenos (fincas rústicas, parcelas, solares), garajes, trasteros, edificios. Milanuncios zelf: "Compra-Venta de viviendas en Jávea/Xabia de particulares y bancos". Fotocasa Pro: "85M de visitas al mes", "990K de viviendas en venta", "112 millones de leads al año". | milanuncios.com/venta-de-viviendas-en-javea%7Cxabia-alicante/ (+ /particular.htm); milanuncios.com/terrenos-en-javea%7Cxabia-alicante/; pro.fotocasa.es/milanuncios/ | 3 / 1 |
| Voorwaarden (`/legal/condiciones-uso`) | **Niet gelezen.** curl: HTTP 403 met botbeveiligingspagina "Pardon Our Interruption"; WebFetch: alleen footer (JavaScript-rendering). Ook `/legal/aviso-legal` gaf dezelfde blokkade. Inhoud over automatische toegang: **[te verifiëren]** door Jan handmatig. | milanuncios.com | 3 (blokkade vastgesteld) |
| robots.txt | Verbiedt voor alle agents o.a. `/*vendedor=`, `/*pagina=`, `/*?pag`, `/datos-contacto/`, `/contacta/`, `/listing/`. Geen licentie. | milanuncios.com/robots.txt | 3 |
| Alerts | Knop "Guardar búsqueda" op de zoekpagina's; hulpcentrum ayuda.milanuncios.com geeft 403. Kanaal/frequentie: ONBEKEND. | milanuncios.com | 3 / 7 |
| Officiële API | Voor **publiceren**: via Fotocasa Pro (packs bevatten Milanuncios) en "Milanuncios Pro" (footerlink, niet onderzocht). Voor **lezen**: niets gevonden. Derden (Apify "Milanuncios Scraper & API", memo23, zen-studio) zijn scrapers → NIET GEBRUIKEN. | pro.fotocasa.es; apify.com | 1 / 3 |
| Rechtspersoon | "© 2026 Adevinta Motor S.L.U." (juridische sectie); Milanuncios staat dus **niet** onder Fotocasa Group/Scout24. Toekomst van de Fotocasa Pro-bundel met Milanuncios: ONBEKEND. | milanuncios.com | 3 / 7 |

**Oordeel:** Milanuncios is voor Jávea de portaalbron met de meeste zichtbare particulieren-advertenties (38 versus 7 op Habitaclia), maar voorwaarden zijn niet leesbaar en de site blokkeert geautomatiseerde clients. Status: **ALLEEN HANDMATIG** (opgeslagen zoekopdracht), voorwaarden **TECHNISCH/JURIDISCH ONDERZOEK NODIG**.

---

## 5. DataVenues (Fotocasa Pro Data)

### 5a. Wat het is

| Kenmerk | Bevinding | Bron | Type |
|---|---|---|---|
| Positionering | "Datos completos del mercado inmobiliario con Fotocasa DataVenues"; "Somos la única herramienta del mercado que cuenta con datos inmobiliarios de origen de Fotocasa, Habitaclia y Milanuncios"; "casi 3 millones de datos actualizados diariamente"; "más de 3 millones de inmuebles computados diariamente"; "Más de 12K profesionales registrados"; "Más de 11K descargas mensuales de informes" | pro.fotocasa.es/soluciones-fotocasa-pro-data/ | 1 |
| Historie | 18-02-2021: DataVenues als onderdeel van Fotocasa Pro, integreert Fotocasa, Habitaclia, kadaster, Agencia Tributaria, INE en Ministerio de Transportes; 21-09-2022: nieuwe versie (mobiele waardering met geolocatie, catastro + Google Maps, max. 2.000 resultaten per query, ES/EN, eAwards 2022) | blogprofesional.fotocasa.es | 1 |
| Ontvanger van de data | Webapplicatie (app.datavenues.com → login) voor professionals; geen bewijs van API-levering aan agentschappen | app.datavenues.com (302 → /login) | 3 |

### 5b. Producten

| Product | Inhoud | Voor wie | Bron | Type |
|---|---|---|---|---|
| **DataVenues** (volledig) | 1. Captación: "Anuncios de particulares actualizados diariamente para que seas el primero en localizar los mejores inmuebles"; 2. dagelijks ranking van alle gepubliceerde objecten; 3. Valoración DataVenues (statistisch model of vergelijkingsmethode); informes (pdf-rapporten) | makelaars/agentschappen | pro.fotocasa.es | 1 |
| **DataVenues GO** (27-02-2026) | Captación-platform: "no solo tienes acceso a los inmuebles publicados en los portales de Fotocasa Pro —Fotocasa, habitaclia y Milanuncios—, sino también al resto de grandes portales inmobiliarios"; "Acceder a los datos de contacto de los propietarios"; ook professioneel aanbod en nieuwbouw ("particular, profesional y obra nueva"); "radar de valoraciones". Witei-variant: "listado de inmuebles de particulares con teléfono de tu zona elegida", "Valoraciones ilimitadas", "Zonas de captación: 1", "Usuarios: 1" | agentschappen (captación) | blogprofesional.fotocasa.es; faq.witei.com | 1 |
| **DataVenues Lite** | Waarderingsmodule in pack "Fotocasa Pro Basic"; volledige DataVenues + "Captación de particulares" in pack "Premium" | Fotocasa Pro-klanten | pro.fotocasa.es/soluciones-packs/ | 1 |
| **DataVenues Widget** | Realtime online waardering op de eigen website "using all the data available on the main real estate portals on the market (fotocasa, habitaclia and milanuncios)"; via Witei "€30/month + VAT"; activering met "activation key (API Key) provided by Datavenues" | websites van makelaars (leadgeneratie) | faq.witei.com | 1 |
| **Notariële sluitprijzen** (29-05-2026) | "Entre los nuevos datos disponibles se incluirán referencias como el precio de cierre de la operación, la fecha de compraventa, la superficie del inmueble y el precio por metro cuadrado" (Consejo General del Notariado), voor "agencias, promotores, consultores, entidades financieras" | professionals | prensa.fotocasa.es | 1 |
| **API / feeds / datasets** | Alleen in een secundair, promotioneel blogartikel (06-05-2025): consultoras, servicers en banken zouden data kunnen "integrar [...] a través de APIs o feeds personalizados". Geen officiële DataVenues- of Fotocasa-pagina bevestigt dit; datavenues.com/productos/ onbereikbaar. **Niet bewezen.** | marketingdepymes.com | 7 |
| Indices | Geen apart DataVenues-indexproduct gezien; de openbare index is de Índice Inmobiliario Fotocasa (§2d). | — | 3 / 7 |

### 5c. Aanvraagroute, prijzen, licentie

| Onderwerp | Bevinding | Bron | Type |
|---|---|---|---|
| Aanvraagroute | Formulier pro.fotocasa.es/form-alta-cliente-profesional-inmobiliario/ (naam, e-mail, telefoon, bedrijf, provincie); "Si ya eres cliente, contacta con tu comercial o llámanos al 900 823 825"; demo-link datavenues.com/contratacion/ (onbereikbaar op 14-09-2026); support: support@datavenues.com (Witei-pagina); Habitaclia-verkoop: 900 535 048 | pro.fotocasa.es; faq.witei.com | 1 / 3 |
| Prijsindicatie | **Niet gepubliceerd** voor DataVenues, DataVenues GO of de packs Start/Basic/Premium. Enige openbare prijs: widget 30 €/maand + btw via Witei. Een DataVenues-licentie zou via de commerciële vertegenwoordiger van Fotocasa/Habitaclia lopen (zoekfragment, bron niet bereikbaar → 7). | — | 7 |
| Licentievoorwaarden (opslag, bewaartermijn, AI-analyse, afgeleide gegevens, beeldvergelijking, doorlevering) | **Nergens gevonden.** datavenues.com (incl. /metodologia/, /productos/, /sabermas/, /novedades/, /contratacion/) gaf op 14-09-2026 alleen time-outs (IP 18.200.204.210, geen bytes ontvangen, vanaf curl én WebFetch); fotocasa.pro/u/aviso_legal laadt alleen via JavaScript. → **CONTRACT OF TOESTEMMING NODIG**; voorwaarden schriftelijk opvragen vóór enige koppeling. | — | 3 / 7 |
| Persoonsgegevens | DataVenues GO levert "datos de contacto de los propietarios" (particulieren). Gebruik daarvan door ons valt onder de AVG (open beslissing Q-06) en masterprompt-regel 9; de licentie moet de rechtsgrond en het toegestane doel (acquisitie-benadering) dekken. | — | 4 |
| Bron van "resto de grandes portales" in DataVenues GO | Onbekend of dit op licentie of op eigen verzameling berust; raakt de juridische houdbaarheid van wat wij afnemen. → open vraag. | — | 7 |

**Oordeel:** DataVenues is de enige aantoonbaar geautoriseerde bron voor de aanbod-data van Fotocasa/Habitaclia/Milanuncios, en sinds 2026 met particulieren-contact én sluitprijzen precies het type data dat Deal Hunter nodig heeft. Het is een gesloten webapplicatie voor makelaars; TREE Properties (makelaardij, Find) is een legitieme afnemer. Levering per API is niet bewezen; verwacht handmatig gebruik of exports binnen de applicatie. Prijs en voorwaarden: offerte nodig.

---

## 6. Per portaal: publiceer-koppeling versus lees-toegang

| Portaal | Publiceren (onze advertenties) | Lezen (advertenties/markt van anderen) | Alerts | Openbare marktcijfers |
|---|---|---|---|---|
| Fotocasa | Ja — Fotocasa Pro, API key, via CRM (Witei/Inmoweb/andere); contract nodig; prijzen niet openbaar | Nee — geen API/feed; voorwaarden verbieden reproductie; botbeveiliging | Ja — account + gemeente, e-mail/app, filter "a reformar" | Ja — Índice per gemeente/wijk (pisos y áticos) |
| Habitaclia | Ja — via dezelfde Fotocasa Pro-koppeling | Nee — zelfde database en voorwaarden | Ja — "Recibir alertas por email" | Via Fotocasa-index |
| Milanuncios | Ja — via Fotocasa Pro-packs / Milanuncios Pro | Nee — voorwaarden niet leesbaar, curl geblokkeerd | Ja — "Guardar búsqueda" | Geen |
| DataVenues | n.v.t. | Ja, tegen licentie — webapplicatie met de drie portalen + andere portalen (GO) + particulieren-contact + notariële sluitprijzen; API niet bewezen | n.v.t. (ranking/radar in de app) | Ja, in de app (waardering, vraag/aanbod) |

---

## 7. Bronnenregister (masterprompt §7)

### 7a. Statusoverzicht

| # | Bron | Type aanbieder | Technische toegang | Status | Kern van de toelichting |
|---|---|---|---|---|---|
| R02-A | Fotocasa — zoekpagina en alerts | Vastgoedportaal (Fotocasa Group, S.L.U.) | Browser; alerts per e-mail/app | **ALLEEN HANDMATIG** | Geen lees-API; reproductie verboden; alerts zijn de toegestane route |
| R02-B | Fotocasa Pro — publicatiekoppeling | Idem, professioneel merk | API key via CRM; JSON/realtime (secundair) | **CONTRACT OF TOESTEMMING NODIG** | Alleen publiceren; geen leesrecht; of TREE al klant is: ONBEKEND |
| R02-C | Índice Inmobiliario Fotocasa | Idem, openbare statistiek | Webpagina's; pdf-persberichten | **ALLEEN HANDMATIG** | Jávea + 9 wijken; alleen pisos/áticos; hergebruiksrechten onbekend |
| R02-D | Habitaclia — zoekpagina en alerts | Idem (zelfde rechtspersoon) | Browser; alerts per e-mail | **ALLEEN HANDMATIG** | Zelfde database als Fotocasa; aparte particulieren- en terrenos-pagina's |
| R02-E | Milanuncios inmobiliaria | Adevinta Motor S.L.U. | Browser; "Guardar búsqueda" | **ALLEEN HANDMATIG** (voorwaarden: TECHNISCH ONDERZOEK NODIG) | Meeste particulieren-advertenties; voorwaarden niet leesbaar; botbeveiliging |
| R02-F | DataVenues / DataVenues GO / Lite / Widget | Datatak Fotocasa Group | Webapplicatie (login); widget met API key; API voor derden niet bewezen | **CONTRACT OF TOESTEMMING NODIG** | Enige geautoriseerde route; prijzen en licentievoorwaarden opvragen; site onbereikbaar op 14-09-2026 |
| R02-G | Derden-"API's"/scrapers (Happy Endpoint, Apify, Oxylabs, WebScrapingHub, Spider) | Commerciële scrapers | REST tegen betaling | **NIET GEBRUIKEN** | Eigen verklaring: gescrapete data; geen autorisatie; in strijd met voorwaarden |

### 7b. Registerkaart per bron (velden uit §7)

**R02-A/B/C — Fotocasa (fotocasa.es, pro.fotocasa.es)**
- Type aanbieder: vastgoedportaal + professioneel platform; rechtspersoon Fotocasa Group, S.L.U. (Madrid), onderdeel Scout24 sinds maart 2026.
- Dekking: landelijk; Jávea 1.806 woningen te koop, 295 terrenos (14-09-2026); Fotocasa Pro claimt 1,5 mln objecten en 13,8 K klanten.
- Technische toegang: lezen alleen via browser/alerts; publiceren via Fotocasa Pro API key.
- Beschikbare velden (lijstweergave, waargenomen): prijs, type, wijk, kamers, badkamers, oppervlak, labels ("Más de 3 meses", "ayer", "Oportunidad", "Calidad Fotocasa"), adverteerdernaam (bedrijf). Detailvelden niet onderzocht.
- Foto's/documenten: foto's ja; documenten ONBEKEND.
- Publicatie-/wijzigingsinformatie: grove leeftijdslabels; prijsdaling-alert in app; exacte datum ONBEKEND.
- Historie: geen voor advertenties; wel prijsindex sinds 2005.
- Verversing: alerts "en pocos minutos"; index maandelijks (gemiddelde laatste 4 weken).
- Rate limits: n.v.t. (geen API); botbeveiliging actief.
- Kosten: publiceren via packs, prijzen op aanvraag; particulier gratis; lezen n.v.t.
- Contractstatus: ONBEKEND of TREE Properties een Fotocasa Pro-account heeft → ⏸️ ACTIE VOOR JAN (zie §8).
- Toegestane gebruiksdoelen / AI-rechten / opslag / afgeleide gegevens: niet toegestaan zonder toestemming (reproductieverbod); aviso legal fotocasa.es zelf niet gelezen.
- Contact: formulier pro.fotocasa.es/form-alta-cliente-profesional-inmobiliario/; 900 823 825 (klanten).
- Laatste verificatie: 14-09-2026.
- Open vragen: tekst aviso legal; alert-limieten; of alert-mails geparsed mogen worden.
- Operationele status: handmatig bruikbaar.

**R02-D — Habitaclia (habitaclia.com)**
- Type/rechtspersoon: zelfde als Fotocasa (CIF B-70677125).
- Dekking: landelijk (oorsprong Catalonië); Xàbia 1.758 woningen, 285 terrenos y solares, 7 particulieren (14-09-2026).
- Technische toegang: browser; alerts per e-mail; geen API/XML in voorwaarden.
- Velden/foto's: als Fotocasa (zelfde database). Documenten ONBEKEND.
- Publicatie-/wijzigingsinformatie, historie: ONBEKEND.
- Verversing: als Fotocasa (aanname, type 4).
- Rate limits/kosten: n.v.t.; publiceren via Fotocasa Pro.
- Rechten: reproductie/exploitatie zonder toestemming verboden (Condiciones Generales); wijzigingen 30 dagen vooraf.
- Contact: 900 535 048 (verkoop, via Fotocasa Pro).
- Laatste verificatie: 14-09-2026. Open vragen: filter "para reformar"; alert-frequentie.

**R02-E — Milanuncios (milanuncios.com)**
- Type/rechtspersoon: generalistische marktplaats, Adevinta Motor S.L.U.
- Dekking: landelijk; Jávea 2.735 woningen (kanttekening categorie), 38 particulieren, 275 terrenos (14-09-2026).
- Technische toegang: browser (WebFetch werkt, curl geblokkeerd); "Guardar búsqueda"; geen lees-API.
- Velden: prijs, type, locatie, particulier/professioneel (via aparte pagina). Details niet onderzocht.
- Rechten: voorwaarden niet leesbaar → [te verifiëren].
- Kosten: publiceren via Fotocasa Pro of Milanuncios Pro; prijzen ONBEKEND.
- Contact: via Fotocasa Pro (900 823 825) of Milanuncios Pro.
- Laatste verificatie: 14-09-2026. Open vragen: voorwaardentekst; positie na de EQT/Scout24-splitsing.

**R02-F — DataVenues (datavenues.com, app.datavenues.com; Fotocasa Pro Data)**
- Type: commerciële vastgoeddata-aanbieder van Fotocasa Group.
- Dekking: landelijk; "casi 3 millones de datos actualizados diariamente"; Jávea-dekking niet zelf gezien (app achter login).
- Technische toegang: webapplicatie; widget met API key; API/feeds voor derden alleen in secundaire bron (7).
- Velden (volgens aanbieder): aanbod van drie portalen + andere grote portalen (GO), particulieren met telefoon, ranking, waardering, vraag/aanbod, kadaster, notariële sluitprijs/datum/oppervlak/€/m².
- Foto's/documenten: ONBEKEND.
- Publicatie-/wijzigingsinformatie: "actualizados diariamente"; historie ONBEKEND.
- Rate limits: ONBEKEND; Witei-variant 1 zone / 1 gebruiker.
- Kosten: op aanvraag; widget 30 €/maand + btw (Witei).
- Contractstatus: geen.
- Gebruiksdoelen/AI-rechten/opslag/afgeleide gegevens: ONBEKEND — voorwaarden niet vindbaar.
- Contact: formulier pro.fotocasa.es; 900 823 825; support@datavenues.com; datavenues.com/contratacion/ (onbereikbaar).
- Laatste verificatie: 14-09-2026. Open vragen: zie §8. Operationele status: niet aangesloten.

---

## 8. Open vragen en acties

**⏸️ ACTIE VOOR JAN**
1. Heeft TREE Properties al een Fotocasa Pro-account (publicatie via GHL of een CRM)? Zo ja: welk pack, en zit DataVenues (Lite/volledig) erin? Dat bepaalt of §5 al beschikbaar is zonder nieuwe kosten.
2. Open in de browser fotocasa.es/es/aviso-legal/ln, milanuncios.com/legal/condiciones-uso en fotocasa.pro/u/aviso_legal, en sla ze op als pdf in `deal-hunter/onderzoek/bronnen/`; ik kon deze teksten niet machinaal lezen.
3. Vraag bij Fotocasa Pro (formulier of 900 823 825) een offerte en de schriftelijke voorwaarden van DataVenues/DataVenues GO op, met expliciet de vragen: export/API mogelijk? opslag en bewaartermijn? gebruik voor AI-analyse en afgeleide dossiers? rechtsgrond voor eigenaarscontact (AVG)? dekking Jávea/Marina Alta? prijs per zone/gebruiker?

**Open onderzoeksvragen**
- Is het parsen van alert-e-mails van Fotocasa/Habitaclia/Milanuncios in een eigen mailbox toegestaan onder hun voorwaarden? (Niet vastgesteld.)
- Waar komt de "resto de grandes portales"-laag van DataVenues GO vandaan (licentie of eigen verzameling)? Dit raakt de houdbaarheid van wat wij afnemen.
- Blijft Milanuncios (Adevinta Motor) na de eigendomssplitsing in de Fotocasa Pro-bundel?
- Bestaat "Fotocasa Pro Data Flow" (404 op 14-09-2026) nog als product?
- Bevat DataVenues detailvelden op objectniveau (kadastrale referentie, publicatiedatum, prijshistorie) die onze Deal Hunter-identiteit (§11 masterprompt) zouden dekken?
- Mogen de cijfers van de Índice Inmobiliario Fotocasa in onze dossiers worden overgenomen met bronvermelding? (Hergebruiksvoorwaarden niet gevonden.)

---

## 9. Geblokkeerd of mislukt (transparant)

| URL | Resultaat | Actie |
|---|---|---|
| https://datavenues.com/ (+ /metodologia/, /sabermas/, /novedades/, /productos/, /contratacion/, /estudio-mercado-inmobiliario/) | Time-out (>20 s, 0 bytes) vanaf curl (2×) én WebFetch (7×); www → 301 naar apex; DNS 18.200.204.210 | Niet omzeild; secundaire bronnen (pro.fotocasa.es, Witei, blog) gebruikt |
| https://www.fotocasa.es/es/aviso-legal/ln | HTTP 200, maar tekst uitsluitend client-side (JavaScript) | Handmatig door Jan te lezen |
| https://www.fotocasa.pro/u/aviso_legal en /u/login | Alleen paginatitel geladen (JavaScript) | Idem |
| https://www.milanuncios.com/legal/condiciones-uso en /legal/aviso-legal | curl: HTTP 403 "Pardon Our Interruption" (botbeveiliging); WebFetch: alleen footer | Niet omzeild |
| https://www.milanuncios.com/terrenos-en-javea%7Cxabia-alicante/particular.htm (curl) | Botbeveiligingspagina | Niet omzeild |
| https://ayuda.fotocasa.es/…, https://ayuda.habitaclia.com/hc/es, https://ayuda.milanuncios.com/hc/es | HTTP 403 (Zendesk) | Alternatieve Fotocasa-Life-artikelen gebruikt |
| https://pro.fotocasa.es/data-flow/ | HTTP 404 | Product niet bevestigd |
| https://www.fotocasa.es/es/condiciones-legales/ | HTTP 404 | Juiste URL is /es/aviso-legal/ln |
| https://prensa.fotocasa.es/wp-content/uploads/2017/12/Metodologia-indice-venta.pdf | HTTP 404 | Huurvariant (2017) gebruikt als methodologiebron |
| https://prensa.fotocasa.es/tag/indice-inmobiliario/ | HTTP 500 | WP-JSON-zoekopdracht gebruikt |
| https://www.scout24.com/en/news-media/news (lijst) | HTTP 404 | IR-pagina en Q2-2026-bericht gebruikt |
| Officieel EQT-persbericht over Adevinta Spain | Niet opgehaald (WebSearch-quotum op) | Secundaire bron gemarkeerd als type 7 |
| WebSearch | Sessiequotum (200) bereikt halverwege | Verder met WebFetch/curl |

---

## 10. Bronnenlijst (URL · controledatum · bewijstype)

1. https://www.scout24.com/en/news-media/news/detail/scout24-acquires-spanish-online-real-estate-platforms-fotocasa-and-habitaclia · 14-09-2026 · 2
2. https://www.scout24.com/en/investor-relations/financial-news/ir-news/detail/scout24-maintains-strong-momentum-in-q2-with-20-revenue-growth-double-digit-organic-revenue-growth-and-18-adjusted-eps-growth · 14-09-2026 · 2
3. https://www.scout24.com/en/investor-relations/financial-news/ir-news/detail/scout24-unveils-the-agentic-os-for-real-estate-and-outlines-next-phase-of-scalable-growth-at-capital-markets-day-2026-1 · 14-09-2026 · 2
4. https://www.onlinemarketplaces.com/articles/investment-and-ma-roundup-scout24-acquires-fotocasa/ · 14-09-2026 · 7 (secundair)
5. https://www.onlinemarketplaces.com/articles/scout24-acquires-fotocasa-and-habitaclia-for-e153m/ · 14-09-2026 · 7 (secundair)
6. https://realtyinvestor.eu/news/eqt-compra-adevinta-portales-inmobiliarios.html · 14-09-2026 · 7 (secundair)
7. https://www.elnacional.cat/oneconomia/es/empresas/fotocasa-infojobs-que-pasara-empresas-adevinta-tiene-espana_1317307_102.html · 14-09-2026 · 7 (secundair)
8. https://www.fotocasa.es/ (footer, "Fotocasa Group, S.L.U.", ImmoScout24) · 14-09-2026 · 3
9. https://www.fotocasa.es/es/aviso-legal/ln · 14-09-2026 · 3 (niet leesbaar)
10. https://www.fotocasa.es/gestion-alquiler/terminos-y-condiciones/ · 14-09-2026 · 2
11. https://www.fotocasa.es/robots.txt · 14-09-2026 · 3
12. https://www.fotocasa.es/es/comprar/viviendas/javea-xabia/todas-las-zonas/l · 14-09-2026 · 3
13. https://www.fotocasa.es/es/comprar/viviendas/javea-xabia/todas-las-zonas/a-reformar/l · 14-09-2026 · 3
14. https://www.fotocasa.es/es/comprar/terrenos/javea-xabia/todas-las-zonas/l · 14-09-2026 · 3
15. https://www.fotocasa.es/es/poner-anuncio-gratis · 14-09-2026 · 1
16. https://www.fotocasa.es/indice-precio-vivienda · 14-09-2026 · 1
17. https://www.fotocasa.es/es/indice-precio-vivienda/javea-xabia/todas-las-zonas · 14-09-2026 · 3
18. https://www.fotocasa.es/es/indice-precio-vivienda/alicante-provincia/todas-las-zonas · 14-09-2026 · 3
19. https://prensa.fotocasa.es/wp-content/uploads/2017/12/Metodologia-indice-alquiler.pdf · 14-09-2026 · 2
20. https://prensa.fotocasa.es/el-precio-de-la-vivienda-sube-un-156-interanual-en-espana-en-agosto/ (+ pdf NdP-Espana-VENTA-Agosto-2026.pdf) · 14-09-2026 · 1
21. https://prensa.fotocasa.es/en-un-ano-desciende-la-rentabilidad-de-la-vivienda-en-el-81-de-costa/ · 14-09-2026 · 1
22. https://prensa.fotocasa.es/informes/ · 14-09-2026 · 1
23. https://prensa.fotocasa.es/wp-json/wp/v2/posts?search=Jávea · 14-09-2026 · 3
24. https://prensa.fotocasa.es/fotocasa-incorpora-el-precio-de-cierre-de-compraventa-del-consejo-general-del-notariado-en-su-herramienta-de-big-data-datavenues/ (29-05-2026) · 14-09-2026 · 1
25. https://www.fotocasa.es/fotocasa-life/fotocasa/fotocasa-renueva-alertas-ahora-mas-eficientes-ayudarte-encontrar-sitio/ (27-11-2020) · 14-09-2026 · 1
26. https://www.fotocasa.es/fotocasa-life/fotocasa/como-activar-la-alerta-de-pisos-que-han-bajado-de-precio/ (16-11-2023) · 14-09-2026 · 1
27. https://www.fotocasa.es/fotocasa-life/fotocasa/encuentra-tu-hogar-ideal-con-las-alertas-compartidas-de-fotocasa/ (07-08-2025) · 14-09-2026 · 1
28. https://pro.fotocasa.es/ · 14-09-2026 · 1
29. https://pro.fotocasa.es/fotocasa/ · 14-09-2026 · 1
30. https://pro.fotocasa.es/habitaclia/ · 14-09-2026 · 1
31. https://pro.fotocasa.es/milanuncios/ · 14-09-2026 · 1
32. https://pro.fotocasa.es/soluciones-fotocasa-pro-data/ · 14-09-2026 · 1
33. https://pro.fotocasa.es/soluciones-packs/ · 14-09-2026 · 1
34. https://pro.fotocasa.es/soluciones-gestor-de-oportunidades/ · 14-09-2026 · 1
35. https://pro.fotocasa.es/crm-inmobiliario/ · 14-09-2026 · 1
36. https://pro.fotocasa.es/recursos/ · 14-09-2026 · 1
37. https://pro.fotocasa.es/form-alta-cliente-profesional-inmobiliario/ · 14-09-2026 · 1
38. https://blogprofesional.fotocasa.es/fotocasa-habitaclia-milanuncios-unen-fotocasa-pro-marca-profesionales-inmobiliarios/ (18-02-2021) · 14-09-2026 · 1
39. https://blogprofesional.fotocasa.es/asi-es-la-nueva-version-mejorada-de-datavenues/ (21-09-2022) · 14-09-2026 · 1
40. https://blogprofesional.fotocasa.es/datavenues-go-herramienta-captacion-inmobiliaria (27-02-2026) · 14-09-2026 · 1
41. https://faq.witei.com/en/articles/118353-fotocasa-pro-real-estate-interconnection-in-fotocasa-habitaclia-and-milanuncios · 14-09-2026 · 1
42. https://faq.witei.com/es/articles/11077030-datavenues-go-plataforma-de-captacion-valoracion-y-analisis-de-mercado · 14-09-2026 · 1
43. https://faq.witei.com/en/articles/9229707-real-time-rating-widget · 14-09-2026 · 1
44. https://ayuda.inmoweb.es/2023/03/27/como-activo-la-publicacion-en-fotocasa/ · 14-09-2026 · 1
45. https://inmocms.com/como-publicar-una-agencia-inmobiliaria-en-fotocasa/ (alleen zoekfragment) · 14-09-2026 · 7
46. https://www.marketingdepymes.com/general/datavenues-la-herramienta-clave-para-dominar-el-mercado-inmobiliario-con-datos/ (06-05-2025) · 14-09-2026 · 7
47. https://app.datavenues.com/ (302 → /login) · 14-09-2026 · 3
48. https://datavenues.com/ en subpagina's · 14-09-2026 · 3 (time-out)
49. https://www.habitaclia.com/hab_cliente/legalavisocontentmodal.asp · 14-09-2026 · 2
50. https://www.habitaclia.com/robots.txt · 14-09-2026 · 3
51. https://www.habitaclia.com/viviendas-xabia.htm · 14-09-2026 · 3
52. https://www.habitaclia.com/terrenos_y_solares-xabia.htm · 14-09-2026 · 3
53. https://www.habitaclia.com/viviendas-particulares-xabia.htm · 14-09-2026 · 3
54. https://www.milanuncios.com/legal/condiciones-uso · 14-09-2026 · 3 (geblokkeerd)
55. https://www.milanuncios.com/robots.txt · 14-09-2026 · 3
56. https://www.milanuncios.com/inmobiliaria/ · 14-09-2026 · 3
57. https://www.milanuncios.com/venta-de-viviendas-en-javea%7Cxabia-alicante/ · 14-09-2026 · 3
58. https://www.milanuncios.com/venta-de-viviendas-en-javea%7Cxabia-alicante/particular.htm · 14-09-2026 · 3
59. https://www.milanuncios.com/terrenos-en-javea%7Cxabia-alicante/ · 14-09-2026 · 3
60. https://docs.happyendpoint.com/fotocasa/ · 14-09-2026 · 1 (scraper, eigen verklaring)
61. https://apify.com/parsebird/fotocasa-scraper, https://oxylabs.io/products/scraper-api/web/fotocasa, https://webscrapinghub.com/real-estate-scrapers/fotocasa-scraper, https://spider.cloud/scrapers/fotocasa-es-scraper/, https://apify.com/parsebird/milanuncios-scraper/api/mcp (alleen zoekfragmenten) · 14-09-2026 · 1
62. Lokaal: ~/tree-es/properties/leadgen/docs/marktdata-bronnen.md (25/26-08-2026) · 14-09-2026 · 3
63. Lokaal feit: Idealista-assistent 14-09-2026 (70 "para reformar", 238 terrenos) · 3

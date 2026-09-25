# R06 — Register van makelaars die in Jávea/Xàbia aanbieden

> **NA TEGENSPRAAK (15-09-2026).** Dit rapport is door een tweede agent gecontroleerd; zie `R06-makelaars-javea-register.verificatie.md`. Betrouwbaarheid volgens die controle: middel.
> Weerlegd en in de eindstukken gecorrigeerd: R06-06; R06-18; R06-19. Gebruik voor die punten de gecorrigeerde tekst in het verificatiebestand, niet de tekst hieronder.


**Project:** TREE Deal Hunter, fase A · **Stroom:** R06 (masterprompt §9) · **Controledatum:** 14-09-2026 · **Auteur:** onderzoeksagent (Claude) · **Status:** concept, ter beoordeling door Jan

Bewijstypen (masterprompt §5): **1** door aanbieder/portaal vermeld · **2** officiële bron · **3** door ons rechtstreeks vastgesteld (site zelf geopend of technisch gecontroleerd) · **4** AI-gevolgtrekking · **5** berekening · **6** bevoegde professional · **7** onbekend/tegenstrijdig.

## Samenvatting (10 regels)

1. Het register telt **61 geverifieerde kantoren** (eigen site of bedrijfsprofiel gezien) plus **31 alleen-op-naam-bekende** namen uit directories; de meest volledige openbare directory (Trustlocal) noemt **95** kantoren voor Xàbia/Jávea, Javea Guide **44**, Jávea.com **24**, Indomio **27** (zoeksnippet).
2. De grote portaal-aanbiederpagina's (Idealista, Fotocasa, Kyero, Indomio, yaencontre) blokkeren geautomatiseerd ophalen (HTTP 403/404); dit register steunt daarom op de kantoorsites zelf (bewijstype 3), lokale directories (1) en de officiële Idealista-assistent (1).
3. Het CRM-/websitelandschap is herkenbaar en geconcentreerd: **Paagees** (≥ 15 sites in de regio, o.a. MG Villas, Montgó Villas, Villadom, Javea Immo, Arzuaga, Homes to be Happy, Holidaydream, Bindley, Ferrando, Benimo, Villa Mediterránea, J. Morató, Selenhome, Javea Casas, Terramar via Sooprema-variant), **Inmoweb** (Randof, Javea Continental, Xabiacasa — met "Inmoweb MLS"), **Mediaelx** (Bocasa, Casas Ambiente, Tabaira, Orange Villas), **Mobilia** (Vicens Ash), **Inmobalia** (Euro Javea, InmoVillas), **Sooprema** (Terramar, Calablanca, Benitachell Properties), **Houzez/WPResidence/RealHomes-WordPress** (Background Properties, Javea Mia, Xabiga, Luxia, Ashton, AV Costamar).
4. **Gedeelde voorraad is de norm**: Background Properties presenteert zichzelf als "listing service" voor "40+ leading … real estate agents"; Casas Costa Blanca toont beelden van backgroundproperties.com, Optima-CRM, RealtySoft en Max-Villas; AR Luxury Living host beelden op backgroundproperties.com en crown-property.com; 123 Javea Villas claimt "access to all major estate agents properties"; Xabiacasa is "Member of Inmoweb MLS".
5. Kantoren met een **eigen percelenrubriek** en aantoonbaar veel percelen: Coldwell Banker Solaris (11 van 50 "terreno urbano"-advertenties in de Idealista-assistent dragen ref. CBS…), Engel & Völkers (3 percelen met naam), Euro Javea (2), Holidaydream (48 parcelas, Moraira-kantoor), Villa Mediterránea Calpe (72 plots), Rimontgó (3 Jávea-plots), Plots Direct S.L. (specialist "plot and build", sinds 2003), Moraguespons, Vicens Ash, Arzuaga, InmoVillas, Atina, Javea Home Finders, Alta Villas, Paradise, Terramar, Luxia.
6. Kantoren met een **eigen renovatie-/reformar-ingang**: Moraguespons (URL /a-reformar/), 123 Javea Villas, Euro Javea, Terramar, Holidaydream ("Reformas"), Plots Direct, Luxia ("Reformada"), Javea Mia ("POTENTIAL"), Villalux en Llidomar (renovatie-objecten in etalage), Crown (renovatiedienst), Miralbo (luxe totaalrenovaties, bouwer).
7. **Bankvastgoed**: de Idealista-assistent gaf op 14-09-2026 **0** resultaten met filter "de bancos" in Jávea; Paradise, 123 Javea Villas, Javea Continental, Xabiacasa en Benitachell Properties hebben wél een bank-/"entidad financiera"-rubriek of -filter op hun site (inhoud niet gecontroleerd).
8. Zones (Idealista-assistent, eigen zoekopdrachten, 70 renovatie-chalets en 106 unieke percelen bekeken): renovatieobjecten clusteren in **Montgó (15), casco antiguo (10), Arenal (7), Pueblo (5), Puerto (5), Pinosol (4), El Tosalet (3), Cap Martí (3)**; percelen in **Montgó (14–15), Arenal (10), Puerto (10), Pueblo (6), La Corona (4), La Lluca (4), Rafalet (3), Pinosol (3), Ermita (2–4), Costa Nova, Granadella, Balcón al Mar, Ambolo (2)**.
9. Openbare feeds: geen enkel kantoor publiceert een open XML/JSON-aanbodfeed; wat bestaat zijn **sitemaps** (bij 45 sites HTTP 200 op /sitemap.xml) en de **privé Kyero-feed van Background Properties** (export_id 26/27/29/30/31/32/36, sleutel nooit overnemen). Een sitemap is géén gebruikslicentie (masterprompt §7).
10. Niet bewezen/onbekend: het domein van **Koch & Varlet Luxury Realtors** (2 dure projectobjecten, ref. KV…), wie achter de **"LTV…"-referenties** zit, en of Costa Houses, Lucas Fox, Villas-Plots, Signature Villas, Spanienobjekte en Inmobiliaria Javea vanaf deze machine bereikbaar zijn (blokkade of DNS-fout).

## 1. Werkwijze

| Stap | Wat | Bewijstype |
|---|---|---|
| Meertalige zoekopdrachten (NL/EN/ES/DE/FR: "inmobiliaria Jávea/Xàbia", "estate agents Javea", "makelaar Jávea", "Immobilien Javea", "agence immobilière Javea", "parcelas Jávea", "casa para reformar Jávea", ketens) | 23 zoekopdrachten tot het sessiebudget (200) op was | 1 |
| Directories geopend | Trustlocal (95), Javea Guide (44, 3 pagina's), Jávea.com (24 + profielen), Kyero/Idealista/Indomio/yaencontre/Fotocasa (geblokkeerd) | 1 |
| Kantoorsites geopend met WebFetch | 58 sites (waarvan 9 geblokkeerd/onbereikbaar) | 3 |
| Lichte technische controle: één GET op de homepage + één HEAD op /sitemap.xml per site, HTML bewaard en op platformkenmerken doorzocht (generator-tag, thema-pad, CRM-domeinen, hreflang, mailto/tel) | 84 domeinen | 3 |
| Idealista-assistent (officiële MCP): 7 zoekopdrachten Jávea (para reformar ×4, terrenos ×3, de bancos ×1), max. 50 per aanroep; beschrijvingen doorzocht op kantoornamen en zones | 176 unieke advertenties gezien | 1 |

Let op bij de Idealista-assistent: de tool geeft **geen makelaarsnaam**; de telefoonnummers (960 37…, 965 02…, 865 44…) zijn **doorschakelnummers van Idealista**, geen kantoornummers. Alleen waar een kantoor zichzelf in de advertentietekst noemt (bijv. "ref: CBS…", "Engel & Völkers presenta…") is toewijzing mogelijk. Domeinen van kantoren zonder bekende site zijn als hypothese getoetst; alleen domeinen waarvan de paginatitel het kantoor bevestigt, staan in het register.

## 2. Dekking van de zoektocht

| Bron | Resultaat 14-09-2026 | Bewijs |
|---|---|---|
| idealista.com/en/agencias-inmobiliarias/javeaxabia-alicante/inmobiliarias | HTTP 403 (WebFetch); zoeksnippet noemt Atina, Selenhome, Moraguespons | 7/1 |
| fotocasa.es agencias Jávea | HTTP 404 op de gegokte URL; zoekresultaat wijst naar generieke pagina | 7 |
| kyero.com/en/spain/estate-agents/javea-l1895 | HTTP 403; zoeksnippets: Javea Home Finders (a4121), 123 Javea Villas (a8639), Euro Javea (a6414), Rentals Javea (a22873, verhuur); "1,712 homes for sale and rent" | 1 |
| indomio.es agencias Jávea | HTTP 403; snippet: "27 real estate agencies" | 1 |
| yaencontre.com/inmobiliarias/javea-xabia | HTTP 403 | 7 |
| trustlocal.es (Xàbia, agencia inmobiliaria) | 95 "verified" kantoren; 13 met naam zichtbaar | 1 |
| javeaguide.com/javea-estate-agents (+ /page2, /page3) | 44 kantoren met straatadres | 1 |
| en.javea.com/zona/comercios/inmobiliaria/agencia-inmobiliaria/ | 24 profielen (incl. verhuurders en bouwers) | 1 |
| houzz.de "Immobilienmakler Jávea" | snippet: "69 local real estate experts" | 1 |
| inmobiliariasenalicante.com/agencias/javea-xabia/ | tweemaal mislukt (geen uitvoer) | 7 |

## 3. Register

Legenda kolom "Rubrieken": **P** percelen/terrenos · **R** para reformar/renovatie · **N** nieuwbouw/projecten · **B** bankvastgoed. ✓ = eigen rubriek/filter gezien; (✓) = renovatie-object of -dienst zichtbaar zonder aparte rubriek; – = niet gezien. "Sitemap" = HTTP-code van /sitemap.xml (bewijstype 3). Kolom "Uniek/gedeeld" is een **AI-inschatting (4)** met de reden erbij; niets is bevestigd door het kantoor zelf.

### 3A. Kantoren gevestigd in Jávea/Xàbia — site zelf gezien (bewijstype 3, aangevuld met 1)

| Nr | Kantoor | Website | Vestiging (Jávea) | Talen | Platform/CRM (herkend) | Rubrieken | Jávea-aantal (indicatief) | Uniek/gedeeld (reden) | Sitemap/feed | Contactroute | Bewijs |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Background Properties (BP) | backgroundproperties.com | Jávea (adres niet op site) | ES/EN/NL/DE/FR (hreflang) | WordPress + WPML + Elementor + **Houzez-thema**; Kyero-v3-XML-export via wp-load (privé, sleutel) | – – – – (site toont vooral verkochte objecten) | Feed: 56 Jávea-objecten op 25-08-2026 (lokale API) | **Gedeeld**: "professional listing firm", "40+ leading national and international real estate agents" | sitemap 404; homepage antwoordt 403 aan curl maar levert de pagina | hola@backgroundproperties.com · +34 670 412 191 | 3 |
| 2 | COSTA HOUSES Luxury Villas S.L. | costa-houses.com (vanaf deze machine onbereikbaar: verbinding mislukt) | Av. del Pla 126, 1º-26 (CCA) · The Hub, Av. de la Llibertat 19 · Moraira: Calle Mar 15 | ES/EN/NL (site heeft /es/, /en/, /nl/-paden) | ONBEKEND | ONBEKEND | Idealista-snippet: 60 objecten Jávea, €499k–€5,5M | ONBEKEND; in assistent 1× met naam (perceel) | ONBEKEND | info@costa-houses.com · 966 364 579 | 1 (Jávea.com-profiel, Trustlocal 9,9, snippets) |
| 3 | MORAGUESPONS Mediterranean Houses | moraguespons.com | Av. Ausias March 13, local 4 | ES/EN/FR/DE/NL | ONBEKEND (geen herkenbare markers; eigen "cliëntenportaal" en online waardering) | P✓ R✓ (URL /venta/villa/javea/a-reformar/) N✓ B– | Per wijk getoond, bijv. "Montañar – El Arenal: 38 propiedades" | Deels eigen (eigen "exclusieve selectie"), rest ONBEKEND | sitemap 200 | info@moraguespons.es · +34 96 579 39 42 | 3 |
| 4 | Rimontgó (Forbes Global Properties) | rimontgo.com | Av. Lepanto 1 · Paseo Amanecer bl. 9 L-10 (Arenal); ook Valencia, Madrid | ES/EN/FR/DE/NL/PL | Eigen site (Next.js) | P✓ (3 Jávea-plots) R– N– B– | 3 percelen Jávea op de plot-pagina | Vermoedelijk eigen mandaten (luxe segment, sinds 1959) | sitemap 200 | +34 96 579 10 35 · e-mail niet getoond | 3 |
| 5 | Ahermar | ahermar.com | Av. de la Fontana 4 (Arenal) | ES/EN/FR | ONBEKEND | P✓ (filter) R– N– B– | 3 verkoop op homepage | ONBEKEND | sitemap 404 | javea@ahermar.com · +34 965 792 592 | 3 |
| 6 | Javea Home Finders | javeahomefinders.com | Av. de la Libertad 19, local 11 (+ Puerto) | EN/ES/FR/DE/NL | **EasyInmo** (generator-tag) / GetSmart "websites & CRM"; API, GVA, AIPP | P✓ R– N✓ B– | 8 uitgelicht | ONBEKEND | sitemap 200; Kyero-adverteerder (a4121) | info@javeahomefinders.com · +34 966 470 133 | 3 |
| 7 | Crown Properties (sinds 1970) | crown-property.com | Avd. París 2 (Arenal) | ES/EN/DE/FR/NL | ONBEKEND (curl krijgt "Security Check") | P✓ R(✓ renovatiedienst) N✓ B– | Categorieën totaal: 152 luxe villa's, 439 villa's, 127 app. (niet Jávea-specifiek) | Gedeeld waarschijnlijk: AR Luxury Living host beelden op crown-property.com | sitemap 200 | info@crown-property.com · +34 965 790 862 | 3 |
| 8 | Engel & Völkers València – Jávea | engelvoelkers.com/es/en/shops/valencia-javea | Av. del Mediterráneo 238 (site); Javea Guide: Av. de la Libertad 47-C | ES/EN (+ concernbrede talen) | Concernplatform (Next.js) | P✓ (land-filter) R– N✓ B– | **109** resultaten gemeente Xàbia (site) | Eigen mandaten + netwerk; 4 advertenties met naam in assistent (3 percelen, 1 finca "reforma integral") | sitemap 200 | +34 963 51 78 97 (shop); Javea Guide: +34 965 76 95 58 | 3 |
| 9 | Hamiltons of London (Jávea-kantoor) | hamiltonsoflondon.net | Av. Lepanto 13 | ES/EN/DE/FR/NL/RU/PL | ONBEKEND ("Security Check") | P✓ (filter) R– N(✓ badge) B– | ± 20+ (5 pagina's) | ONBEKEND | sitemap 200 | info@javea-hamiltons.net · +34 96 579 08 03 | 3 |
| 10 | Vicens Ash Properties | vicensash.com | Ctra. Cap de la Nau Pla 137 | ES/DE/EN/FR/NL | **Mobilia** ("Creado con Mobilia", static.mobiliagestion.es) | P✓ ("Terrenos") R(✓ renovatieplanning) N✓ ("Promociones") B– | 12 op homepage | ONBEKEND; partner van Jávea.com | sitemap 200 | info@vicensash.com · +34 966 461 643 | 3 |
| 11 | Paradise Real Estate / Paradise Javea | paradiserealestate.co.uk | Av. de la Libertad bl. 5, 47-C | ES/EN/FR/NL/SV/DE | Eigen CRM ("paradisepro"); adverteert op Kyero, Rightmove, Idealista, Fotocasa (site) | P✓ R– N✓ **B✓** ("Bank repossessed") | **225** objecten Jávea (site) | Vermoedelijk gedeeld (omvang) | sitemap 200 | admin@paradiserealestate.es · +34 966 472 595 | 3 |
| 12 | Valuvillas | valuvillas.com | Ctra. Cabo la Nao Pla 141 (Javea Guide) | ONBEKEND | WordPress + Elementor (Hello-thema) | ONBEKEND (pagina 403 voor WebFetch) | ONBEKEND | ONBEKEND | sitemap 200 | ONBEKEND | 3 (techniek) / 1 |
| 13 | Villalux | villalux.com | Av. del Pla (Javea Guide) | ES/EN/DE/FR/NL/PL | Onbekend CRM-webplatform met assetpad `crm/pages/agencies/villaluxjavea` (zelfde leverancier als nr. 24, 37, 28, B-Area) | P✓ R(✓ "complete renovation in Montgó") N(✓ "licensed project") B– | 6 per pagina | ONBEKEND; "built and sold" → deels eigen bouw | sitemap 200 | niet getoond | 3 |
| 14 | Alta Villas | altavillas.com | Av. Libertad 19, local 12 | EN/ES/FR/NL/DE/NO/SV | ONBEKEND | P✓ R– N✓ B– | ± 8 uitgelicht | ONBEKEND | sitemap 500 | office@altavillas.com · +34 965 796 311 | 3 |
| 15 | InmoVillasJávea (sinds 1997) | inmovillasjavea.com | Av. Augusta 22, bajo 7 (site); Javea Guide: Av. del Mediterráneo 41 | EN/ES/FR/NL | WordPress + **Inmobalia**-media (media.inmobalia.com) | P✓ (eigen parcelas-pagina) R– N✓ B– | Idealista-snippet: 34 objecten | Deels eigen ("WhatsApp VIP off-market"); licentie EGVT-00230-A | sitemap 200 | info@inmovillasjavea.com · +34 96 646 00 33 | 3 |
| 16 | Deseo Homes | deseohomes.com | Camí de les Adsubies 381 | NL/EN/DE/ES | WordPress (GeneratePress); "kyero"-verwijzingen in HTML | – – – – | ± 10 uitgelicht | ONBEKEND; RAICV | sitemap 200 | +34 644 629 510 · e-mail via site | 3 |
| 17 | RANDOF Real Estate | randofrealestate.com | Av. de la Libertad 47, bl. 5 (+ 2× Dénia) | EN/ES/NL/DE/FR/PL | **Inmoweb** ("Hecho con Inmoweb") | P✓ R– N✓ B– | 6 in "for sale" | ONBEKEND; 1 renovatievilla met naam in assistent | sitemap 200 | 965 036 919 · e-mail niet getoond | 3 |
| 18 | Atina Inmobiliaria (Jávea, Gandía, Daimús) | atinainmobiliaria.com/javea | Venecia 2 (site); Javea Guide: Av. Mediterráneo 27 | ES/NL/EN/FR | WordPress (WPML, Bricks-thema) | P✓ R– N✓ B– | ± 25 op pagina; Idealista-snippet: 40 Jávea | ONBEKEND | sitemap 200 | javea@atinainmobiliaria.com · +34 966 461 128 | 3 |
| 19 | Javea Mia | javeamia.com | CC Arenal, Ctra. Cabo la Nao Pla 130, 1-09 | EN/ES/NL/FR/DE | WordPress + **Houzez** | P✓ R(✓ "POTENTIAL") N✓ B– | ± 50 (verkoop + verhuur) | ONBEKEND; APIAL A611, RAICV 6054; niet meer op Habitaclia | sitemap 200 | info@javeamia.com · +34 966 27 64 04 | 3 |
| 20 | Inmobiliaria Javea Continental | javeacontinental.com | Av. Rey Jaime I 11-B | 10 talen | **Inmoweb** | P✓ R– N– **B✓** (filter "entidad financiera") | 15 (13 verkoop) | ONBEKEND | sitemap 200 | 965 796 366 · e-mail niet getoond | 3 |
| 21 | Grupo García (Jalón, Jávea, Moraira, Madrid) | grupo-garcia.es | Jávea-kantoor (adres niet getoond) | ES/EN | WordPress (Bricks) | P– R– N✓ B– | 18 luxe villa's op Jávea-pagina | ONBEKEND | sitemap 200 | info@grupo-garcia.es · +34 966 482 480 | 3 |
| 22 | Luxia Properties | luxiaproperties.com | Av. dels Furs 27, local 4 | "multilingüe" | WordPress + **WPResidence** + Elementor | P✓ R✓ ("Reformada") N✓ B– | claim: 22 exclusieve villa's | Deels eigen (claim exclusiviteit, niet bevestigd) | sitemap 200 | ventas@luxiaproperties.com · +34 655 468 942 | 3 |
| 23 | Llidomar Properties | llidomarjavea.com | adres niet getoond | ES/EN/FR | Onbekend CRM-webplatform (`crm/pages/agencies/llidomarjavea`) | P✓ R(✓) N– B– | 65 villa's / 35 app. (heel Costa Blanca) | ONBEKEND | sitemap 200 | info@llidomarjavea.com · +34 965 791 505 | 3 |
| 24 | Villadom Immo | villadomjavea.com | Av. Fontana 8, bajo | ES/EN/DE/FR/NL | **Paagees** (Paagees Shield) | – – – – | 6 uitgelicht | ONBEKEND; 1 renovatieobject met naam in assistent | sitemap 200 | info@villadomjavea.com · +34 96 579 48 62 | 3 |
| 25 | Javea Immo (sinds 1997) | javeaimmo.com | Av. de Estrasburgo, local 3 | ES/EN/DE/FR/NL/PL/RU | **Paagees** | P✓ (rústicas) R– N✓ B– | 10 uitgelicht | ONBEKEND | sitemap 200 | info@javeaimmo.com · +34 678 626 407 | 3 |
| 26 | Arzuaga Inmobiliaria | arzuagainmobiliaria.com | C/ Ronda Norte 11 | ES/EN/DE/FR/NL/IT | **Paagees** | P✓ (filter tot >10.000 m²) R– N✓ B– | 225 objecten getoond (Jávea-aandeel onduidelijk) | Vermoedelijk gedeeld (omvang vs. één kantoor) | sitemap 200 | info@arzuagainmobiliaria.com · +34 865 71 61 18 | 3 |
| 27 | AR Luxury Living | arluxuryliving.com | adres niet getoond | ES/EN/DE/FR | Onbekend CRM-webplatform (`crm/pages/agencies/antoniorosello`); beelden gehost op backgroundproperties.com en crown-property.com | P✓ R– N✓ B– | 4 nieuwbouwvilla's €3,995M–€4,5M | **Gedeeld** (beeldbronnen van BP en Crown) | sitemap 200 | niet getoond | 3 |
| 28 | Homes to be Happy | homestobehappy.com | C/ Campaneta 19 | ES/EN/DE/FR | **Paagees** | P✓ R– N✓ B– | 26 nieuwbouwprojecten Jávea | Vermoedelijk gedeeld (projectaggregator) | sitemap 200 | info@homestobehappy.com · +34 600 000 393 | 3 |
| 29 | Montgó Villas | montgovillas.com | Jávea (adres niet getoond) | ES/DE/EN/FR/IT/NL/PL/RU | **Paagees** ("Paagees Webs para Inmobiliarias") | P✓ R– N✓ B– | 94 objecten (site) | ONBEKEND | sitemap 200 | info@montgovillas.com · +34 647 555 215 | 3 |
| 30 | MG Villas Luxury Property (sinds 1994) | mgvillas.co.uk | Av. de la Libertad 11, local 11 (Arenal) | EN (+ hreflang DE/ES/FR/NL) | **Paagees** | P✓ R(✓) N✓ B– | 20 per pagina; Idealista-snippet: 121 totaal, 35 Jávea | ONBEKEND | sitemap 200 | info@mgvillas.com · +34 965 770 699 | 3 |
| 31 | 123 Javea Villas (sinds 1996) | 123javeavillas.com | Av. Marina Española 5 (Puerto); Páginas Amarillas: Av. dels Furs 1 | EN/FR/ES/NL/DE/NO/RU | "Advance Agent estate agency software" (site) | P✓ R✓ N✓ **B✓** ("repossessions") | 6+6 uitgelicht; Idealista-snippet: 30 | **Gedeeld**: "direct from the owners" én "access to all major estate agents properties" | sitemap 200; Kyero-adverteerder (a8639) | info@123javeavillas.com · +34 865 824 482 | 3 |
| 32 | Euro Javea Real Estate (sinds 1998) | eurojavea.com | Pl. Presidente Adolfo Suárez 9 (Puerto) | ES/NL/FR/EN | WordPress + **Inmobalia**-media | P✓ R✓ N✓ (Ca Áurea, "Euro Javea Projects") B– | ± 10 uitgelicht | Deels eigen ("secret sales", eigen projecten); 2 percelen met naam in assistent (Puerto-solar 1.190 m², Granadella) | sitemap 200; Kyero-adverteerder (a6414) | info@eurojavea.com · +34 96 579 42 90 | 3 |
| 33 | Xabiga S.L. Construcciones y Servicios | xabiga.com (xabiga.net weigert verbinding) | C/ Santísimo Cristo del Mar 33 (Puerto) | ES/EN/FR | WordPress + **Houzez** + Elementor | – – – –; bouwbedrijf | 8 | ONBEKEND | sitemap 200 | inmoxabiga@gmail.com · 965 795 219 | 3 |
| 34 | Xabiacasa Mediterranean Properties | xabiacasa.com | C/ Sant Agustí 3 | EN/ES | **Inmoweb** — "Member of Inmoweb MLS" | P✓ R– N✓ **B✓** (filter) | 11 op homepage | **Gedeeld** (MLS-lid) | sitemap 200 | 678 878 343 · e-mail niet getoond | 3 |
| 35 | Andrea & Olaf Real Estate | andreayolaf.com | Jávea (Jávea.com-profiel) | ES (site-titel) | ONBEKEND | ONBEKEND (subpagina 404) | ONBEKEND | ONBEKEND | sitemap 200 | info@andreayolaf.immo · +34 606 935 434 | 3 (homepage-HTML) / 1 |
| 36 | Klaus Hildenbrand | klaus-hildenbrand.com | Camí Pou del Moro 4 | ES/EN/DE/FR | Onbekend CRM-webplatform (`crm/pages/agencies/klaus`) | P✓ R– N– B– | 5 uitgelicht | ONBEKEND; API-lid; 1× met naam in assistent | sitemap 200 | office@klaus-hildenbrand.com · +34 687 818 833 | 3 |
| 37 | TerramaR Costa Blanca | terramar.es | Pl. Adolfo Suárez 18 (Puerto) | ES/EN/DE/FR/NL/RU/NO/SV | **Sooprema** (Paagees Shield op curl) | P✓ R✓ N✓ B– | ± 40 | Deels eigen: bouw + verkoop nieuwbouw, projectmanagement (Jávea.com) | sitemap 200 | info@terramar.es · 966 460 560 | 3 |
| 38 | Soluciones Inmobiliaria Jávea (Real Estate Solutions Jávea) | solucionesinmojavea.com | Av. Trenc d'Alba 1 | meertalig | WordPress | P✓ R– N✓ B– | 36 Jávea | ONBEKEND; RAICV 1.738 | sitemap 200 | info@solucionesinmojavea.com · +34 96 694 39 53 | 3 |
| 39 | Casitas Iberica (25 jaar) | casitasiberica.com | Ctra. Jesús Pobre 164 | EN/ES/NL/FR/DE | WordPress (eigen thema) | – – – – | 6 uitgelicht | **Gedeeld**: "property finding service through our network of local estate agents" | sitemap 404 | info@casitasiberica.com · +34 965 794 408 | 3 |
| 40 | Ashton Villas | ashtonvillas.com | Av. Augusta 20 (Javea Guide) | DE/EN/ES/FR/NL | WordPress + **RealHomes** + WPML | – – – – | 18 pagina's | ONBEKEND | sitemap 200 | info@ashtonvillas.com · +34 637 052 484 | 3 |
| 41 | AV Costamar S.L. | avcostamar.com | Av. Rey Jaume I 15 (Javea Guide) | ES/EN/FR/DE/RU/ZH | WordPress + **RealHomes** | P– R– N✓ B– | 3 op homepage | ONBEKEND | sitemap 200 | niet getoond | 3 |
| 42 | Coldwell Banker Solaris Real Estate | coldwellbanker.es/inmobiliaria-javea-solaris | Av. de la Libertad 12, bajo (Arenal) | ES/EN/FR/DE | Concernsite Coldwell Banker Spain | P– (geen aparte rubriek op site) R– N✓ B– | 6 uitgelicht; **assistent: 11 van 50 "terreno urbano"-advertenties dragen ref. CBS…** | Eigen mandaten waarschijnlijk (eigen referenties) | sitemap 200 | +34 865 61 53 75 · e-mail via site | 3 + 1 |
| 43 | Miralbo Urbana S.L. (bouwer/ontwikkelaar) | miralbo.com | Av. de Libertad 18, bajo F | EN/ES/DE/FR/NL/PL | ONBEKEND | P– R✓ ("luxury full renovations") N✓ B– | niet gekwantificeerd | **Eigen** (bouwt en verkoopt eigen villa's) | sitemap 200 | sales@miralbo.com · 965 036 330 | 3 |
| 44 | Plots Direct S.L. (sinds 2003) | plotsdirect.com | Ctra. Cabo la Nao Pla 258 (Javea Guide) | 13 talen | ONBEKEND | P✓ R✓ N✓ (design & build) B– | ± 9 uitgelicht | ONBEKEND | sitemap 200 | niet getoond | 3 |
| 45 | Javea Casas (sinds 1999) | javeacasas.com | C/ Cicerón 8 (Javea Guide) | EN/ES/DE/FR/NL | **Paagees** | P– R– N✓ B– | 124 objecten | Vermoedelijk gedeeld (omvang) | sitemap 200 | niet getoond | 3 |
| 46 | Selenhome | selenhome.com | adres niet getoond | 8 talen | **Paagees** | P✓ R– N✓ B– | Idealista-snippet: 7 Jávea | ONBEKEND | sitemap 200 | niet getoond | 3 |
| 47 | Marina Villas Jávea | website niet gevonden | Av. del Pla 110 | ONBEKEND | ONBEKEND | bouw/ontwikkeling, VvE-beheer, verhuur (Jávea.com) | ONBEKEND | ONBEKEND | ONBEKEND | 965 79 64 60 | 1 |
| 48 | Maravilla Costa Real Estate | website niet gevonden | Av. del Pla 124, L-8 | ONBEKEND | ONBEKEND | ONBEKEND | ONBEKEND | ONBEKEND | ONBEKEND | 965 794 515 | 1 |
| 49 | Jávea Promotions | website niet gevonden | Av. del Pla 124, local 15 | ONBEKEND | ONBEKEND | bouw + verkoop (Jávea.com) | ONBEKEND | ONBEKEND | ONBEKEND | 965 79 27 69 | 1 |
| 50 | Class & Villas | classandvillas.com | Av. del Pla 126-2.25 | ES/EN/FR/DE/NL/RU | eigen site | – | 3 objecten (1 Jávea) | **Geen makelaar**: magazine/publicatie | sitemap 200 | info@classandvillas.com · +34 965 79 66 11 | 3 |

### 3B. Kantoren buiten Jávea met aantoonbaar Jávea-aanbod (site zelf gezien)

| Nr | Kantoor | Website | Vestiging | Talen | Platform/CRM | Rubrieken | Jávea-aantal | Uniek/gedeeld (reden) | Sitemap | Contactroute | Bewijs |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 51 | Casas Ambiente | casas-ambiente.com | Moraira, Av. de la Paz 10 | EN/ES/FR/DE/NL | **Mediaelx** (ontwerp & CRM) | P✓ R– N✓ B– | **42** Jávea | **Gedeeld**: MLS/REALTOR-vermeldingen | 403 | info@casas-ambiente.com · +34 966 498 595 | 3 |
| 52 | BoCasa | bocasa.nl | Moraira, Av. Madrid 16 | EN/NL/ES | **Mediaelx** | P– R– N✓ B– | 12 per pagina | ONBEKEND; API 0146, RAICV 2081 | 403 | info@bocasa.nl · +34 666 628 676 | 3 |
| 53 | Tabaira Real Estate | tabairarealestate.com | Moraira, C/ Iglesia 4 | EN/ES/DE/NL/FR | **Mediaelx** | P– R– N(✓ filter) B– | 12 per pagina | ONBEKEND | 403 | info@tabairarealestate.com · +34 965 744 179 | 3 |
| 54 | Orange Villas | orangevillas.com | Moraira, Ctra. Moraira–Calpe 19 | EN/ES/FR/NL/DE | **Mediaelx** | P✓ R– N✓ B– | Jávea-pagina toonde 0 (filter) | ONBEKEND; 1× met naam in assistent (perceel) | 403 | info@orangevillas.com · +34 966 491 163 | 3 |
| 55 | Casas Costa Blanca | casascostablanca.nl | Moraira | NL/EN/ES | WordPress (OceanWP); beelden van backgroundproperties.com, optima-crm.com, realtysoftcrm.com, max-villas.eu | P✓ R– N✓ B– | 12 op homepage | **Gedeeld** (vier externe beeldbronnen, incl. BP) | 200 | +34 634 366 548 · e-mail via site | 3 |
| 56 | Inmobiliaria Celenia | inmobiliariacelenia.com | Moraira, C/ Dr. Calatayud 55 | ES/EN/DE/RU/PL | Drupal 7 | P✓ R– N✓ (eigen bouwdienst) B– | niet gekwantificeerd | ONBEKEND | 200 | info@inmobiliariacelenia.com · +34 966 490 179 | 3 |
| 57 | Bindley Properties | bindleyproperties.com | Moraira, Av. Madrid 11 | EN (+DE/ES/FR/NL) | **Paagees** | P✓ R– N✓ B– | Jávea-categorieën aanwezig, aantal niet getoond | ONBEKEND | 200 | info@bindleyproperties.com · +34 965 049 701 | 3 |
| 58 | Ferrando Estate Agents (35 jaar) | ferrando-moraira.com | Moraira | ES/EN/DE/FR/NL/SV | **Paagees** | P✓ R– N✓ B– | niet getoond | ONBEKEND | 200 | +34 96 574 45 75 · e-mail niet getoond | 3 |
| 59 | Holidaydream Homes Costa Blanca | holidaydream.es | Moraira, C/ Laurel 15 | ES/EN (+DE/FR/NL hreflang) | **Paagees** | P✓ (48 parcelas) R✓ ("Reformas") N✓ B– | **71** Jávea | ONBEKEND; RAICV 1595 | 200 | ventas@holidaydream.es · +34 678 959 272 | 3 |
| 60 | Benitachell Properties S.L. | benitachellproperties.com | Benitachell, C/ Padre Plácido 57 | ES/EN/DE/FR/NL/RU | **Sooprema** (Mattis-framework) | P✓ R– N✓ **B✓** ("Propiedades de Banco") | ≥ 1 zichtbaar | ONBEKEND | 404 | info@benitachellproperties.com · +34 966 493 572 | 3 |
| 61 | Laura Villas | lauravillas.com | Benitachell, Cumbre del Sol 101-M | ES/EN/FR | eigen site (Temps) | P✓ R– N✓ B– | niet getoond | ONBEKEND; RAICV 2423 | 200 | +34 627 931 965 · e-mail via site | 3 |
| 62 | AREA Costa Blanca | areacostablanca.es | Benissa, Av. de la Marina 302 (+ Calpe) | ES/EN/NL/FR/DE/RU | Onbekend CRM-webplatform (`crm/pages/agencies/areacostablanca`); FIABCI, GIPE | P– R– N✓ B– | Jávea in filters, aantal niet getoond | ONBEKEND | 200 | info@areacostablanca.com · +34 966 11 24 28 | 3 |
| 63 | Benimo-Villas | benimo-villas.com | Benissa, Av. de la Marina 44 | ES/EN/DE/NL/FR | **Paagees** | P✓ R(✓) N✓ B– | "Villas for sale in Javea"-link | ONBEKEND | 200 | info@benimo-villas.com · +34 965 74 78 74 | 3 |
| 64 | Villa Mediterránea | villamediterranea.es | Calpe, C/ Doctor Fleming 4 | ES/EN/DE/FR/NL/RU/DA | **Paagees** | P✓ (**72** plots) R(✓) N✓ B– | Jávea als zoekstad | ONBEKEND | 200 | info@villamediterranea.es · +34 965 83 21 22 | 3 |
| 65 | Agencia J. Morató (sinds 1972) | agenciamorato.com | Calpe, Av. Gabriel Miró 38A | ES/EN/DE/FR/NL/RU/PL | **Paagees** | P✓ (32) R– N✓ B– | Jávea in filters | ONBEKEND | 200 | info@agenciamorato.com · +34 965 839 083 | 3 |
| 66 | MP Villas | mpvillas.com | Calpe | ES/EN/DE/FR/NL | **Inmovilla** (apinmo.com-API, inmovilla.com) | ONBEKEND | ONBEKEND (pagina 404) | ONBEKEND | 200 | niet getoond | 3 (techniek) |
| 67 | Calablanca | calablanca.com | Jávea/Costa Blanca Norte (site: "based in Jávea") | 10 talen | **Sooprema** | P✓ R– N✓ B– | Jávea-wijken (Arenal, Puerto, Tosalet) | ONBEKEND; 1× met naam in assistent (perceel) | 404 | (+34) 96 646 19 50 · e-mail niet getoond | 3 |
| 68 | Fine & Country Costa Blanca North | fineandcountry.es/en/costa-blanca-north-estate-agents | Dénia, Marina de Dénia, Dársena de Babor ed. E | EN/ES/FR/NL/DE | MyF&C, Nurtur.tech; F&C-netwerk (300+ vestigingen) | P– R– N✓ B– | 6 Jávea | ONBEKEND | 200 | costablancanorth@fineandcountry.com · +34 966 675 768 | 3 |
| 69 | Berkshire Hathaway HomeServices Costa Blanca | bhhscostablanca.com | Dénia, Carrer Diana 7 · Altea | NL/ES (+DE/EN/FR hreflang) | WordPress + Elementor | P– R– N✓ B– | villa's €949k–€3,95M; wijkpagina's Portichol, Granadella | ONBEKEND | 200 | +34 965 64 11 25 · e-mail niet getoond | 3 |
| 70 | MNM Costa Blanca | mnmcostablanca.es | Els Poblets, C/ Mirrarosa 3B | NL/EN/ES/DE | ONBEKEND | – – – – | 4 Jávea | ONBEKEND | 200 | 0034 966 475 997 · e-mail via site | 3 |
| 71 | Villa Lingo | villalingo.com | Dénia, Camí dels Lladres 5 (Javea Guide: Av. de la Libertad 18 L-4) | EN/FR/ES | ONBEKEND | P✓ R– N– B– | ± 8–10 | ONBEKEND | 200 | niet getoond | 3 |
| 72 | Inmover | inmover.com | Els Poblets · El Verger | ONBEKEND | **Paagees** | ONBEKEND | Dénia–Oliva (Jávea niet genoemd) | ONBEKEND | 200 | 966 475 267 | 3 (techniek) / 1 |
| 73 | Alveo / J'achète en Espagne | alveo.co/agent-immobilier/javea | Alicante, C/ Valdés 11 | FR/ES/EN | Webflow; **Witei**-vermelding in HTML | – – – – | **0** Jávea-objecten getoond | Netwerk van Franstalige kantoren | 200 | alicante@alveo.co · +34 965 02 72 01 | 3 |
| 74 | Costa Blanca Sotheby's International Realty | spain-sothebysrealty.com (alleen Madrid-HQ zichtbaar) | Alicante, Carrer Girona 31 (LuxuryEstate-snippet) | EN/ES | concernplatform | N✓ (elders in Spanje) | Jávea: niet getoond (7) | ONBEKEND | 200 | +34 919 041 929 (HQ) | 1/7 |
| 75 | Casasdediez | casasdediez.com | Oliva Nova | ES | WordPress + Elementor | – | niet Jávea-gericht (site) | – | 200 | hola@casasdediez.com · 961 356 984 | 3 |

### 3C. Kantoren met bekende naam en (meestal) adres, site niet bereikbaar of niet gevonden (bewijstype 1, niet geverifieerd)

| Kantoor | Bron | Adres/opmerking | Status |
|---|---|---|---|
| Lucas Fox Jávea (Dils; partner Savills) | zoeksnippet lucasfox.com/offices/jav.html; assistent 1× met naam ("villa a renovar íntegramente") | Pl. Adolfo Suárez 23, Puerto · +34 965 79 33 63 · sinds 2021 | Site 403 (Cloudflare "Just a moment") |
| Koch & Varlet Luxury Realtors | assistent: 2 objecten > €700k met ref. KV146V (Villa Imperio, La Corona, €3,95M) en KV156V (€1,8M) | domein ONBEKEND (6 hypothesen mislukt) | Website [te verifiëren] |
| Villas-Plots (sinds 2004) | zoeksnippet; Javea Guide | Av. de la Libertad 19, L-5 | Site 403 |
| Signature Villas (sinds 2001, bouw + verkoop) | zoeksnippet | Jávea | Verbinding geweigerd |
| Inmobiliaria Javea (familiebedrijf, 30+ jaar) | zoeksnippet | Jávea | DNS-fout vanaf deze machine |
| Spanienobjekte (Duitstalig) | zoeksnippet (Jávea-pagina) | ONBEKEND | Site 403 (Cloudflare) |
| Giuliano Villas | Trustlocal 8,7; Javea Guide | Av. de la Llibertat 34, L-3 | domein giulianovillas.com lost niet op |
| Immo Belgica | Trustlocal | Ctra. Cap de la Nau Pla 130 | website ONBEKEND |
| Blom Group Real Estate, Silvia Piera Inmobiliaria, Premium Villas Costa Blanca, Select Villas of Moraira, catorce inmobiliaria, Montesinos Falcón, Marti Projects | Trustlocal (8,8–9,0) | geen adres; martiprojects.com bestaat maar geeft 403 (Cloudflare) — identiteit niet bevestigd | website ONBEKEND |
| Hernani Homes (Av. Fontana 2, L-7b), Euro Villas Javea (Av. Colomer 6), Casaconnections (Ctra. Cabo la Nao Pla 116-4), A.F. Costa Blanca S.L. (Av. Fontana 2, L-2), Be Spoiled (Av. de la Llibertat 12), Casas de Levante, Acre (Av. Arenal 1), HG Hamburg, Houses (Paseo Amanecer bl. 1 L-5), Javea 1 (Av. Rey Jaime I 9), Javea Online (C/ del Vedat 2), La Nao en Mestral (Pl. Almirante Bastarreche), Sukup & Partner (C/ Sant. Cristo del Mar 21), Ultimate Property Javea (Av. del Pla), Villa Mia (Ctra. Benitachell km 1) | Javea Guide (44) | adressen zoals vermeld | niet geverifieerd; javea1.com/villamia.es leeg; javeahomes.com "System Updating" |
| Bemax Javea (C/ Andrés Lambert 24) | Javea Guide | bemaxjavea.com: "Account Suspended" | vermoedelijk inactief |
| BonCasa Costa Blanca / MMC Property Services | Jávea.com | Carrer Nancy 1, local 33 · Info@mmcpropertyservices.com | vakantieverhuur/beheer, geen verkoopmakelaar |
| Habitat Dénia, Denia Luxe Lofts, Aguila Rent a Villa, Quality Rent a Villa, Rental Villalux, Rentals Javea (Kyero) | Jávea.com / Kyero | verhuur/beheer of Dénia | buiten focus |
| Grupo Moraira | zoekresultaat | grupomoraira.es: "System Updating" | tijdelijk onbereikbaar |
| Jávea.com (mediabedrijf) | eigen site | Real-estate-sectie is een contenthub met partners Aguila, Vicens Ash, Xabiga, Quality Rent a Villa — géén eigen makelaardij | geen makelaar |

## 4. Platform-/CRM-landschap en wat dat betekent

| Platform | Herkend bij (bewijstype 3) | Betekenis voor Deal Hunter |
|---|---|---|
| **Paagees** ("Paagees Webs para Inmobiliarias"; curl krijgt "Paagees Shield") | Villadom, Javea Immo, Arzuaga, Homes to be Happy, Montgó Villas, MG Villas, Javea Casas, Selenhome, Bindley, Ferrando, Holidaydream, Benimo, Villa Mediterránea, J. Morató, Inmover, Terramar (shield) | Grootste gemeenschappelijke noemer in de Marina Alta. Paagees beschermt de homepage tegen bots (Shield), dus geautomatiseerd lezen is bewust bemoeilijkt — behandel als "ALLEEN HANDMATIG" tenzij het kantoor zelf een export geeft. |
| **Inmoweb** ("Hecho con Inmoweb Software Inmobiliario"; Xabiacasa: "Member of Inmoweb MLS") | Randof, Javea Continental, Xabiacasa | Inmoweb kent een MLS: kantoren op Inmoweb delen zeer waarschijnlijk voorraad onderling (4). |
| **Mediaelx** ("Ontwerp & CRM: Mediaelx") | Bocasa, Casas Ambiente, Tabaira, Orange Villas (alle Moraira) | Zelfde leverancier voor het Moraira-cluster; sitemap.xml gaf 403. |
| **Mobilia** (mobiliagestion.es) | Vicens Ash | CRM met eigen websitemodule. |
| **Inmobalia** (media.inmobalia.com) | Euro Javea, InmoVillas Jávea | CRM met portaalkoppelingen. |
| **Sooprema** | Terramar, Calablanca, Benitachell Properties | CRM/website met "entidad financiera"-filter bij twee van de drie. |
| **Inmovilla** (apinmo.com) | MP Villas (Calpe) | Inmovilla is volgens eigen site het CRM "van 90% van de MLS-systemen" in Spanje (1); in Jávea zelf niet aangetroffen. |
| **EasyInmo / GetSmart** | Javea Home Finders | — |
| **Witei** (vermelding in HTML) | Alveo | — |
| **WordPress-vastgoedthema's**: Houzez (BP, Javea Mia, Xabiga), WPResidence (Luxia), RealHomes (Ashton, AV Costamar); overig WordPress (Atina, Grupo García, Deseo, BHHS, Valuvillas, Casas Costa Blanca, Soluciones Inmo, Casitas Iberica, Casasdediez) | — | Houzez/WPResidence hebben doorgaans een importmodule voor XML-feeds — bij BP is dat aantoonbaar de Kyero-export (feed bestaat, privé). |
| Onbekend CRM-webplatform met assetpad `crm/pages/agencies/<kantoor>` | Villalux, Llidomar, Klaus Hildenbrand, AR Luxury Living, AREA Costa Blanca | Zelfde leverancier (4); naam niet gevonden — [te verifiëren]. |
| Concernplatforms | Engel & Völkers, Lucas Fox, Coldwell Banker, Fine & Country, Sotheby's, Rimontgó (eigen Next.js) | Eigen mandaten, internationaal netwerk; data alleen via het kantoor. |

## 5. Uniek versus gedeeld aanbod (inschatting, bewijstype 4 met reden)

| Categorie | Kantoren | Reden |
|---|---|---|
| **Aantoonbaar gedeelde voorraad** | Background Properties (listing service voor 40+ kantoren), Casas Costa Blanca (beelden van BP/Optima/RealtySoft/Max-Villas), AR Luxury Living (beelden op BP en Crown), Xabiacasa (Inmoweb MLS), Casas Ambiente (MLS/REALTOR), 123 Javea Villas (eigen claim), Casitas Iberica (eigen claim "network of local estate agents") | op de site zelf gezien (3) |
| **Vermoedelijk gedeeld (omvang of MLS-platform)** | Paradise (225), Arzuaga (225), Javea Casas (124), Homes to be Happy (26 projecten), Randof en Javea Continental (Inmoweb), Crown (beelden hergebruikt door AR Luxury) | 4 |
| **Deels eigen mandaten / projecten** | Euro Javea ("secret sales", Ca Áurea), Moraguespons ("exclusieve selectie"), InmoVillas ("WhatsApp VIP off-market"), Luxia (22 exclusieve villa's, claim), Terramar (bouw + verkoop), Miralbo (bouwer), Xabiga (bouwer), Villalux ("built and sold"), Coldwell Banker Solaris (eigen ref. CBS…), Koch & Varlet (eigen ref. KV…), Engel & Völkers, Lucas Fox, Rimontgó | 3/1; exclusiviteit niet bevestigd (masterprompt §9: geen exclusiviteit veronderstellen) |

## 6. Wie voert opvallend vaak renovatieobjecten en percelen — en waar

### 6a. Op basis van de eigen rubrieken (bewijstype 3)

| Signaal | Kantoren |
|---|---|
| Aparte **reformar/renovatie**-rubriek of -URL | Moraguespons (/a-reformar/), Terramar ("reforma"), Holidaydream ("Reformas"), 123 Javea Villas, Euro Javea, Plots Direct, Luxia ("Reformada"), Javea Mia ("POTENTIAL") |
| Renovatie-object of -dienst in de etalage | Villalux (villa "complete renovation in Montgó"), Llidomar, Crown (renovatiedienst), Vicens Ash (renovatieplanning), Miralbo (totaalrenovaties), Benimo |
| Aparte **percelen**-rubriek met getal | Villa Mediterránea (72), Holidaydream (48), J. Morató (32), Rimontgó (3 Jávea) |
| Percelen-rubriek/filter zonder getal | Moraguespons, Vicens Ash, Ahermar, Javea Home Finders, Crown, Hamiltons, Paradise, Alta Villas, InmoVillas, Randof, Atina, Javea Mia, Javea Continental, Luxia, Llidomar, Javea Immo (rústicas), Arzuaga, AR Luxury, Homes to be Happy, Montgó Villas, MG Villas, 123 Javea Villas, Euro Javea, Xabiacasa, Klaus Hildenbrand, Terramar, Soluciones Inmo, Plots Direct, Selenhome, Casas Costa Blanca, Celenia, Bindley, Ferrando, Benitachell Properties, Laura Villas, Benimo, Villa Lingo, Engel & Völkers, Orange Villas |
| **Bank-/entidad-financiera**-rubriek of -filter | Paradise, 123 Javea Villas, Javea Continental, Xabiacasa, Benitachell Properties (inhoud niet gecontroleerd; assistent: 0 "de bancos" in Jávea) |

### 6b. Op basis van de Idealista-assistent (bewijstype 1; alleen zelfbenoemde kantoren)

Eigen zoekopdrachten 14-09-2026 (Jávea/Xàbia, verkoop): "casa para reformar" CHALET — totaal **70** (alle 70 gezien via drie prijsvensters); "para reformar" in district Puerto — **15**; "terreno urbano" LAND — totaal **129** (83 gezien via twee vensters); "parcela ≥ €300.000" — totaal **239** (50 gezien); "de bancos" — **0**. Aandeel particulier: 1–5 per 50.

| Kantoor (zelf genoemd in advertentietekst) | Percelen | Renovatie | Opmerking |
|---|---|---|---|
| **Coldwell Banker Solaris** (ref. CBS…) | 11 van 50 "terreno urbano" + 1 ≤ €300k + 1 ≥ €300k (o.a. CBS295/733/819/820/762/756N/818N/260/613/485/826/065) | 3 (> €700k: CBSJ745 La Corona €2,25M, CBS626 €2,175M, CBS919N €1,495M) | Grootste zichtbare perceelvoerder; o.a. parcel van €1,6M "para promotores / residencia asistida" en perceel "con proyecto y licencia" (CBS756N) |
| **Engel & Völkers** | 3 (Torre Ambolo €460k; 1.066 m² €750k; 1.029 m² €500k) | 1 (finca "reforma integral" centrum, €520k) | |
| **Euro Javea** | 2 (Puerto, commercieel solar 1.190 m² €1,75M "en exclusiva"; La Granadella €450k) | – | |
| **Koch & Varlet Luxury Realtors** (ref. KV…) | – | 2 (> €700k; nieuwbouw/project La Corona) | website onbekend |
| Moraguespons | – | 1 (€399k, "proyecto con identidad") | |
| Villadom Immo | – | 1 (€800k, casa señorial) | |
| Lucas Fox | – | 1 (€640k, "villa a renovar íntegramente") | |
| Randof | – | 1 (€430k) | |
| Klaus Hildenbrand | – | 1 (≤ €700k) | |
| Atina, Calablanca, Costa Houses, Orange Villas | 1 elk | – | |
| Onbekend kantoor met ref. "LTV…" (LTV327/376/573) | 2 | 1 | [te verifiëren] |

Ongeveer 80% van de advertenties noemt geen kantoor; de rest is dus niet toe te wijzen zonder handmatig de advertentie te openen.

### 6c. Zones (telling van zonenamen in de advertentieteksten, bewijstype 1/4)

| Zone (masterprompt-lijst) | Renovatie-chalets (van 70) | Percelen (van 106 unieke) | Opmerking |
|---|---|---|---|
| Montgó – Ermita | 15 (+ Ermita 1) | 14–15 (+ Ermita 2–4) | grootste cluster in beide categorieën; ook fincas in het natuurpark (geen nieuwbouw toegestaan volgens advertentie) |
| Casco antiguo / Pueblo | 10 / 5 | 2–3 / 4–6 | dorpshuizen "a reformar"; ook een villa met 7 slaapkamers €750k aan de rand van het centrum |
| Puerto / Puchol / La Corona | 5 / 1–2 / 1–2 | 10 / 1 / 4 | Puerto-district apart: 15 renovatie-objecten (pisos vanaf €295k; villa's Puchol €750k ×2) |
| Arenal / Montañar | 7 / 1 | 10 | vooral appartementen |
| Pinosol | 4 | 3 | |
| El Tosalet | 3 | 1–2 | Cumbres del Tosalet (nieuwbouw) genoemd in zoekresultaat |
| Cap Martí | 3 | 1 | |
| La Lluca – Tarraula | 2 / 1 | 4 / 2 | |
| Portitxol | 2 | 1 | |
| Granadella – Costa Nova | 1 | 2 / 2 | Euro Javea-perceel Granadella |
| Adsubia | 1 | – | Aires de Jávea (4 nieuwbouwvilla's, zoekresultaat) |
| Rafalet | 1 | 3 | |
| Castellans | 1 | 1 | |
| Balcón al Mar / Ambolo | – / 1 | 2 / 2 | E&V-perceel Torre Ambolo |
| Cala Blanca, La Cala, Cap Negre, Jesús Pobre, Mezquida, Cuesta San Antonio, La Plana, Piver | 1 elk | 1–2 elk | |

## 7. Feeds en technische toegang (bestaan noteren, niet gebruiken)

| Type | Bevinding | Bewijs |
|---|---|---|
| Openbare XML/JSON-aanbodfeed van een kantoor | **Geen enkele gevonden** op 84 gecontroleerde domeinen | 3 |
| Privé Kyero-v3-XML (BP) | Bestaat: wp-load.php-export met security_key; export_id 26/27/29/30/31/32 (commissie × categorie) en 36 ("alles"); parser-velden zoals in de lokale feiten; geen pool-, status- of prijshistorieveld | 3 (lokaal) |
| /sitemap.xml aanwezig (HTTP 200) | 45 domeinen, o.a. Moraguespons, Rimontgó, Home Finders, Crown, Hamiltons, Vicens Ash, Paradise, Valuvillas, Villalux, InmoVillas, Deseo, BHHS, Randof, Atina, Javea Mia, Javea Continental, Grupo García, Luxia, Llidomar, Villadom, Javea Immo, Arzuaga, AR Luxury, Homes to be Happy, Montgó Villas, MG Villas, 123 Javea Villas, Euro Javea, Xabiga, Xabiacasa, Klaus Hildenbrand, Terramar, Soluciones Inmo, Ashton, AV Costamar, Coldwell Banker, Miralbo, Plots Direct, Javea Casas, Selenhome, E&V, Fine & Country, Casas Costa Blanca, Holidaydream, Bindley, Ferrando, Benimo, Villa Mediterránea, J. Morató, Villa Lingo, Inmover, Celenia | 3 |
| /sitemap.xml geweigerd (403) | Mediaelx-sites (Bocasa, Casas Ambiente, Tabaira, Orange Villas), Lucas Fox, Spanienobjekte | 3 |
| /sitemap.xml afwezig (404/500) | BP, Ahermar, Alta Villas (500), Casitas Iberica, Benitachell Properties, Calablanca, Villas-Plots | 3 |
| Bot-bescherming op homepage | Paagees Shield (≥ 16 sites), Cloudflare (Lucas Fox, Spanienobjekte, Marti Projects), "Security Check" bij Crown, Hamiltons, Paradise, Villalux, Klaus Hildenbrand; BP antwoordt 403 met inhoud | 3 |
| Portaal-aanbiederpagina's | Idealista/Kyero/Indomio/yaencontre 403 — consistent met eerder onderzoek (25/26-08-2026): geautomatiseerde toegang tot Idealista is niet toegestaan | 3 |

Conclusie voor het bronnenregister (§7 masterprompt): elk kantoor hierboven staat op **ALLEEN HANDMATIG** of **CONTRACT OF TOESTEMMING NODIG**; alleen BP is **GEVERIFIEERD EN ACTIEF** (privé-feed). Een sitemap of een Paagees-/Inmoweb-site is geen licentie om te lezen.

## 8. Aanzet samenwerkingsaanpak (masterprompt §9 — concept, niets verzonden)

1. **Eerste ring (eigen mandaten + percelen/renovatie zichtbaar):** Coldwell Banker Solaris, Engel & Völkers Jávea, Euro Javea, Moraguespons, Terramar, Vicens Ash, InmoVillas, Rimontgó, Lucas Fox, Plots Direct, Luxia, Montgó Villas, MG Villas, Villalux.
2. **Tweede ring (groot gedeeld aanbod, snel overzicht):** Paradise, Arzuaga, Javea Casas, Casas Ambiente, Holidaydream, Javea Home Finders, Crown, Hamiltons, 123 Javea Villas.
3. **Bouwers/ontwikkelaars met eigen projecten:** Miralbo, Terramar, Xabiga, Signature Villas [te verifiëren], Euro Javea Projects, Homes to be Happy (aggregator).
4. Werkvorm: één zoekprofiel (zones, prijsband, staat, perceelkenmerken), een aanleverformulier van één pagina, en een vaste opvolgtermijn; geen exclusiviteit of commissie veronderstellen (§9). Conceptberichten pas na akkoord van Jan.

## 9. Open vragen

1. Website en vestiging van **Koch & Varlet Luxury Realtors** (KV-referenties) en van het kantoor achter **"LTV…"**-referenties.
2. Welke leverancier zit achter het CRM-webplatform met assetpad `crm/pages/agencies/…` (Villalux, Llidomar, Klaus Hildenbrand, AR Luxury Living, AREA Costa Blanca)?
3. Werkt Coldwell Banker Solaris met eigen mandaten of ook via BP/MLS? (Eigen referentiecodes wijzen op eigen voorraad, niet bevestigd.)
4. Zijn Costa Houses, Lucas Fox, Villas-Plots, Signature Villas, Spanienobjekte en Inmobiliaria Javea bereikbaar vanaf een gewone browser (blokkade lijkt IP-/botgerelateerd)?
5. Idealista-aanbiederpagina's per kantoor (aantallen per kantoor) alleen handmatig te raadplegen — wie doet de eerste handmatige telling (Atina 40, InmoVillas 34, MG Villas 35, 123 Javea 30, Selenhome 7, Costa Houses 60, E&V 109 zijn snippets van 14-09-2026)?
6. Is gepland gebruik van de Idealista-assistent (MCP) voor systematische zone-analyses toegestaan onder de voorwaarden van die assistent? (Niet bewezen; §7.)
7. Welke van de 31 alleen-op-naam-bekende kantoren zijn nog actief (Bemax "Account Suspended", Javea Homes "System Updating")?

## 10. Geblokkeerd of mislukt

- WebSearch-budget van de sessie (200) was na 23 zoekopdrachten van deze stroom uitgeput (gedeeld met andere stromen); de resterende naamsverificaties zijn via directe domeincontrole gedaan.
- Idealista (agencias-pagina, pro-pagina's), Kyero (agentenpagina's), Indomio, yaencontre: HTTP 403; Fotocasa-agenciapagina: 404.
- inmobiliariasenalicante.com: tweemaal geen uitvoer.
- Kantoorsites: costa-houses.com (verbinding mislukt, curl 000), lucasfox.com (403), villas-plots.com (403), signaturevillas.es (verbinding geweigerd), spanienobjekte.com (403), inmobiliariajavea.es (DNS), javeaestateagent.com (mislukt), xabiga.net (verbinding geweigerd; xabiga.com werkt), grupomoraira.es en javeahomes.com ("System Updating"), bemaxjavea.com ("Account Suspended"), boncasa.es (hostingplaceholder), martiprojects.com (Cloudflare 403), javeaguide.com/…?page=2 (gaf pagina 1; /page2 en /page3 werkten).
- Niet oplossende domeinhypothesen (dus niet bevestigd): giulianovillas.com, hernanihomes.com, casaconnections.com, eurovillasjavea.com, terramarcostablanca.com, maravillacosta.com, marinavillasjavea.com, inmover.es, javeapromotions.com, premiumvillascostablanca.com, silviapiera.com, catorceinmobiliaria.com, selectvillas.es, bespoiled.es, casasdelevante.com, afcostablanca.com, immobelgica.com, blomgroup.es, montesinosfalcon.com, kochvarlet.(com/es), koch-varlet.(com/es), cbsolaris.com, coldwellbankersolaris.com, plotsdirect.es, sukup-partner.com, ultimatepropertyjavea.com, javeaonline.com. acre.es bleek een architectenbureau in Madrid (niet het Jávea-kantoor "Acre").

## Bronnenlijst (URL · controledatum 14-09-2026 · bewijstype)

Directories en portalen
- https://trustlocal.es/alacant-alicante/xabia-javea/agencia-inmobiliaria/ · 1
- https://www.javeaguide.com/javea-estate-agents (+ /page2, /page3, /engel-voelkers) · 1
- https://en.javea.com/zona/comercios/inmobiliaria/agencia-inmobiliaria/ (+ profielen /terramar-costa-blanca/, /mmc-property-services/, /soluciones-inmobiliaria-javea/, /promociones-javea/, /maravilla-costa-inmobiliaria/, /marina-villas-javea/, /inmover/, /habitat-denia/, /costa-houses-luxury-villas-s-l/, /oferta-inmobiliaria/) · 1
- https://www.idealista.com/en/agencias-inmobiliarias/javeaxabia-alicante/inmobiliarias · 7 (403); zoeksnippets Idealista "pro"-pagina's (Atina, InmovillasJávea, MG Villas, 123 Javea Villas, Selenhome, Engel & Völkers València, inmobiliarias-de-lujo) · 1
- https://www.kyero.com/en/spain/estate-agents/javea-l1895 · 7 (403); zoeksnippets Kyero-profielen a4121, a8639, a6414, a22873 · 1
- https://www.indomio.es/en/agencias-inmobiliarias/javea-xabia/ · 7 (403); snippet "27 agencies" · 1
- https://www.yaencontre.com/inmobiliarias/javea-xabia · 7 (403)
- https://english.habitaclia.com/real_estate-javea_mia_19399_1/ · 1
- Idealista-assistent (officiële MCP), zoekopdrachten Jávea/Xàbia 14-09-2026: para reformar CHALET (totaal 70), para reformar ≥ €700k (40), ≤ €700k (30), para reformar district Puerto HOME (15), terreno urbano LAND (129), parcela ≥ €300k LAND (239), terreno urbano ≤ €300k (33), "de bancos" HOME (0) · 1

Kantoorsites (bewijstype 3; "techniek" = alleen HTML-controle)
- https://backgroundproperties.com/ · 3 (HTML: WPML, Elementor, Houzez; WebFetch: "40+ … real estate agents")
- https://www.moraguespons.com/ · 3 · https://www.rimontgo.com/properties/javea/plots-and-lands · 3 · https://www.ahermar.com/ · 3
- https://www.javeahomefinders.com/ · 3 · https://www.crown-property.com/en/ en /en/about-us/ · 3
- https://www.engelvoelkers.com/es/en/shops/valencia-javea en …/properties/res/sale/real-estate/valencian-community/munc-xabia · 3
- https://www.hamiltonsoflondon.net/javea-estate-agents/ · 3 · https://www.vicensash.com/ · 3 · https://www.paradiserealestate.co.uk/ · 3
- https://www.valuvillas.com/ · 3 (techniek; inhoud 403) · https://www.villalux.com/villas-for-sale-in-javea/ · 3 · https://altavillas.com/ · 3
- https://www.inmovillasjavea.com/en · 3 · https://www.deseohomes.com/nl/makelaar-in-javea · 3 · https://www.randofrealestate.com/gb/ · 3
- https://atinainmobiliaria.com/javea/ · 3 · https://javeamia.com/ · 3 · https://www.javeacontinental.com/gb/ · 3
- https://grupo-garcia.es/venta/javea/villas-de-lujo/ · 3 · https://luxiaproperties.com/ · 3 · https://www.llidomarjavea.com/en/ · 3
- https://www.villadomjavea.com/en/ · 3 · https://www.javeaimmo.com/ · 3 · https://www.arzuagainmobiliaria.com/ · 3
- https://www.arluxuryliving.com/en/new-construction-in-javea/ · 3 · https://www.homestobehappy.com/en/new-build-for-sale-in-javea/ · 3
- https://www.montgovillas.com/en/ · 3 · https://www.mgvillas.co.uk/villas-for-sale-in-javea/ · 3 · https://www.123javeavillas.com/ · 3
- https://www.eurojavea.com/ · 3 · https://www.xabiga.com/ · 3 · https://www.xabiacasa.com/gb/ · 3 · https://www.andreayolaf.com/ · 3 (techniek)
- https://www.klaus-hildenbrand.com/en/ · 3 · https://www.terramar.es/ · 3 · https://solucionesinmojavea.com/ · 3 · https://www.casitasiberica.com/ · 3
- https://www.ashtonvillas.com/ · 3 · https://www.avcostamar.com/ · 3 · https://www.coldwellbanker.es/inmobiliaria-javea-solaris · 3
- https://www.miralbo.com/ · 3 · https://www.plotsdirect.com/ · 3 · https://www.javeacasas.com/ · 3 · https://www.selenhome.com/ · 3
- https://www.classandvillas.com/en/ · 3
- https://casas-ambiente.com/dutch-real-estate-agent-in-javea.html · 3 · https://bocasa.nl/en/dutch-estate-agent-in-javea.html · 3 · https://tabairarealestate.com/estate-agents-in-javea.html · 3 · https://orangevillas.com/estate-agents-in-javea.html · 3
- https://casascostablanca.nl/en/home/ · 3 · https://www.inmobiliariacelenia.com/ · 3 · https://www.bindleyproperties.com/ · 3 · https://www.ferrando-moraira.com/villas-for-sale-in-benitachell/ · 3
- https://www.holidaydream.es/venta/javea/ · 3 · https://www.benitachellproperties.com/ · 3 · https://lauravillas.com/inmobiliaria-calpe · 3
- https://www.areacostablanca.es/ · 3 · https://www.benimo-villas.com/en/ · 3 · https://www.villamediterranea.es/en/ · 3 · https://www.agenciamorato.com/en/ · 3 · https://www.mpvillas.com/ · 3 (techniek)
- https://www.calablanca.com/ · 3 · https://www.fineandcountry.es/en/costa-blanca-north-estate-agents · 3 · https://www.bhhscostablanca.com/nl/makelaar-in-javea/ · 3
- https://www.mnmcostablanca.es/inmobiliaria-moraira · 3 · https://www.villalingo.com/ · 3 · https://www.inmover.com/ · 3 (techniek) · https://www.alveo.co/agent-immobilier/javea · 3
- https://www.spain-sothebysrealty.com/ · 3 (Jávea niet getoond → 7) · https://www.casasdediez.com/ · 3
- Geblokkeerd/onbereikbaar (7): https://www.costa-houses.com/ · https://www.lucasfox.com/offices/jav.html · https://www.villas-plots.com/ · https://signaturevillas.es/ · https://spanienobjekte.com/ · https://www.inmobiliariajavea.es/ · https://www.javeaestateagent.com/ · https://www.xabiga.net/ · https://www.grupomoraira.es/ · https://www.martiprojects.com/

Zoeksnippets (bewijstype 1, pagina zelf niet geopend): lucasfox.com/offices/jav.html (adres, telefoon, Savills, 2021) · luxuryestate.com (Costa Blanca Sotheby's, Alicante) · engelvoelkers.com nieuwsbericht "New Engel & Völkers shops in Dénia and Jávea" · paginasamarillas.es (123 Javea Villas, Av. dels Furs 1) · inmovilla.com (CRM-claim) · houzz.de (69 experts) · fineandcountry.es contactpagina.

Lokale bronnen (bewijstype 3): ~/tree-hermes/properties-api/feeds.js (export_id's, zonder sleutel) · ~/tree-es/properties/leadgen/docs/marktdata-bronnen.md (Idealista 403, voorwaarden) · ~/tree-es/properties/leadgen/docs/bronnenregister-2026-Q1.md · masterprompt §5, §6, §7, §9.

# R10 — Bank-, fonds- en servicerkanalen: actuele namen, portalen en dekking in Jávea

> **NA TEGENSPRAAK (15-09-2026).** Dit rapport is door een tweede agent gecontroleerd; zie `R10-banken-servicers-fondsen.verificatie.md`. Betrouwbaarheid volgens die controle: hoog.
> Weerlegd en in de eindstukken gecorrigeerd: R10-01. Gebruik voor die punten de gecorrigeerde tekst in het verificatiebestand, niet de tekst hieronder.


**Onderzoeksstroom:** R10 (masterprompt §18; ook §5, §6, §7)
**Controledatum:** 15-09-2026 (eerdere metingen van 14-09-2026 staan er met die datum bij)
**Uitgevoerd door:** onderzoeksagent fase A, TREE Deal Hunter
**Werkwijze:** WebSearch en WebFetch op officiële en bedrijfseigen pagina's, losse `curl`-controles van openbare pagina's (één pagina per vraag, met pauzes, geen bulk), de officiële Idealista-assistent, en de eigen woningfeed (poort 3100, alleen lezen). Geen accounts aangemaakt, geen formulieren verstuurd, geen bestanden gedownload en geen blokkades omzeild.

---

## Samenvatting (10 regels)

1. **Bankaanbod in Jávea is vandaag bijna nul.** Woningen: 0 op Idealista ("de bancos"), 0 bij Servihabitat, 0 bij Diglo; Solvia heeft geen Jávea-pagina. Percelen: **1 bij Idealista en 2 bij Servihabitat Profesionales**. Allebei niet-geconsolideerde bouwgrond, bedoeld voor professionele kopers (bewijstype 3).
2. In de hele Marina Alta staat op Idealista **1 bankwoning** (Calp, Banca March) en staan er **20 bankpercelen**, vooral in Pego, El Ràfol d'Almúnia, El Verger en Benitachell (bewijstype 3).
3. **Sareb** mag volgens de wet hooguit 15 jaar bestaan (BOE, RD 1559/2012 art. 16.3), dus tot eind 2027. Meer dan 40.000 woningen en ongeveer 2.400 percelen gaan naar de staatswoningbouwer **Casa 47**; alleen de rest wordt nog verkocht (bewijstype 2).
4. De verkoop voor Sareb loopt tot en met 2026 via **Aliseda-Anticipa en Hipoges**. Het nieuwe contract (mei 2026) gaat naar **Servihabitat en Aliseda-Anticipa**, maar de bezwaarprocedure van Hipoges houdt Lot A sinds 03-08-2026 stil (pers, [te verifiëren]).
5. **Haya bestaat niet meer als apart kanaal.** Intrum heeft Haya, Solvia, Aktua en HRE samengevoegd tot Solvia Servicios Inmobiliarios; haya.es gaf op 15-09-2026 een serverfout (HTTP 522).
6. **Het landschap schuift nog.** Pollen Street (Hipoges en Finsolutia) koopt Servihabitat (pers, 03-08-2026). Santander brengt zijn vastgoed en het grootste deel van zijn probleemleningen onder bij Diglo (pers, 08-04-2026). Namen en mandaten kunnen dus binnen maanden weer veranderen.
7. **Geen enkel kanaal biedt een openbare lees-API of feed.** Wel zijn er e-mailalerts en opgeslagen zoekopdrachten, maar alleen met een account. De gebruiksvoorwaarden van Servihabitat, Solvia en Diglo verbieden commerciële exploitatie, extractie en hergebruik zonder toestemming (bewijstype 1).
8. Voor automatisch ophalen zijn deze sites gesloten: Sareb (403 via Imperva), Altamira (403), Bankinter (Cloudflare-controle). Aliseda, Hipoges, Anticipa, EscogeCasa en Cimenta2 tonen alleen iets met JavaScript. Die kanalen kunnen alleen handmatig.
9. **Leningen en probleemleningen (NPL):** grote pakketten gaan via aanbestedingen en adviseurs voor institutionele kopers (TED 140491-2026). Daar zitten wij niet aan tafel. Losse leningen en *cesiones de remate* verkopen Aliseda, Diglo en Hipoges wel aan particuliere beleggers. Een lening kopen is niet hetzelfde als het huis kopen; zonder juridische beoordeling doen we dit niet.
10. **Advies: geen dagelijkse monitor.** Beter werkt een wekelijkse check "de bancos" (Jávea en Marina Alta, woningen en percelen) via de Idealista-assistent, e-mailalerts bij 4 servicers (accounts door Jan) en één handmatige ronde per kwartaal. De echte voorsprong zit in route D: erkend samenwerkend makelaar (*API colaborador*) worden bij een servicer [te verifiëren].

---

## 1. Conclusie voor Jan (besluitgericht)

**Conclusie.** Bank-, fonds- en servicerkanalen zijn in Jávea op dit moment geen serieuze bron van renovatiewoningen. Wat er is, is **grond**: professionele, vaak onverdeelde of nog niet geconsolideerde bouwgrond met stedenbouwkundige voorwaarden. Een dagelijkse monitor met eigen code levert te weinig op en loopt juridisch vast op de gebruiksvoorwaarden van de portalen.

**Onderbouwing.**
- Idealista-assistent, 15-09-2026: Jávea "de bancos" woningen **0**, percelen **1**, bedrijfsruimtes **0**. Marina Alta: woningen **1**, percelen **20** (§5, bewijstype 3).
- Servihabitat (publiek portaal), 15-09-2026: Marina Alta 0 woningen, 18 percelen (geen in Jávea). Profesionales-portaal: 9 percelen, waarvan **1 in Balcón al Mar (Jávea)**; een tweede Jávea-perceel staat verkeerd ingedeeld onder de comarca "huerta sur" (§5 en §6, bewijstype 3).
- Solvia, 15-09-2026: geen Jávea-pagina in de sitemap en geen objecten op de Jávea-URL. Wel woningen in Dénia (6), Calp (17), Benissa (4), Teulada (1), Ondara (2) en Pego (2), maar slechts een deel draagt het label "INMUEBLE DE BANCO" (bewijstype 3).
- Onze eigen woningfeed van Background Properties: 56 objecten in "Javea" op 15-09-2026, **0** van een bank of servicer (bewijstype 3).
- Op 14-09-2026 vond R08 in Xàbia/Jávea 0 veilingen en bij de rechtbank van Dénia 0 veilingen (bewijstype 3, uit R08).

**Aannames.** Tellingen zijn momentopnames. Servicers publiceren niet alles op Idealista en niet alles met het label "de bancos" (bewijstype 4). Aliseda, Hipoges, Altamira, Unicaja, Cimenta2, EscogeCasa en Bankinter konden we niet tellen.

**Tegenargumenten.**
- (a) Bankgrond kan precies de B-route-kans zijn (grond en ontwikkeling). Het perceel in Balcón al Mar is 20 % in prijs gezakt (904.000 → 725.000 €).
- (b) Nieuw bankvastgoed ontstaat pas na executie en veiling (R08/R09). Wie de BOE-veilingen volgt, ziet de voorraad eerder dan de servicers.
- (c) Servicers bieden sommige objecten eerst aan hun samenwerkende makelaars aan; die zie je op geen enkel portaal.

**Vervolgstap.**
1. De twee Jávea-percelen doorgeven aan R11/R15 voor kadastrale en planologische identificatie. Geen contact met de verkoper zonder "ja" van Jan.
2. Een lichte monitoropzet kiezen (§8).
3. Jan laten beslissen over accounts, alerts en een aanvraag als samenwerkend makelaar (§10).

---

## 2. Begrippen: wat wordt er eigenlijk verkocht (masterprompt §18)

| Soort | Wat je koopt | Wie verkoopt | Toegankelijk voor TREE? | Bron / type |
|---|---|---|---|---|
| **REO van een bank** (vastgoed in eigendom van een bank) | Het vastgoed zelf (vol eigendom, soms onverdeeld aandeel of zonder bezit) | De bank of haar vastgoeddochter (bijv. BuildingCenter, Cimenta2), vaak via een servicer | Ja, via het retail- of professionele portaal | caixabank.com 25-05-2023 (1); cajamar.es → cimenta2.com (3) |
| **Vastgoed van een fonds, via een servicer** | Het vastgoed zelf; de servicer is makelaar/beheerder, niet de eigenaar | Servihabitat, Solvia, Aliseda, Hipoges, Altamira/doValue, Diglo | Ja, via hun portalen en samenwerkende makelaars | Diglo aviso legal: "inmuebles propiedad de terceros, comercializados por DIGLO" (1) |
| **Obra parada / zonder bezit / onverdeeld** | Vastgoed met technische of juridische gebreken, verkocht aan professionals | Servihabitat Profesionales, Solvia, Aliseda | Ja, maar alleen als professional; juridisch onderzoek nodig | inversores.servihabitat.com: "Los inmuebles no reúnen los requisitos técnicos o documentales para ser comprados por consumidores y usuarios" (1) |
| **Losse lening / NPL met hypotheek** | Een vordering met het vastgoed als onderpand. **Niet het huis.** | Aliseda (/npl/), Diglo ("Venta de Créditos"), Hipoges (portaal voor schuldbeleggers) | Technisch ja, maar een apart juridisch traject (executie, rangorde, bewoning); in fase A niet gebruiken | alisedainmobiliaria.com sitemap-loans.xml (3); digloservicer.com/oportunidades/venta-credito (3) |
| **Cesión de remate** (overname van het veilingrecht van de schuldeiser) | De positie van de executant in een lopende veiling | Diglo, Aliseda, Hipoges | Idem: juridische beoordeling verplicht (§19) | digloservicer.com (3) |
| **NPL- of REO-portefeuille** (honderden tot duizenden objecten of leningen) | Een pakket | Sareb, banken, via adviseurs en aanbestedingen | **Nee.** Institutioneel; minimumomvang en eisen ver boven onze schaal (bewijstype 4) | TED 140491-2026 (2); Infobae 27-01-2026 (1, pers) |

**Let op (bewijstype 4):** vastgoed van een bank betekent niet dat die bank failliet is. Een servicer is bijna nooit de eigenaar. De Brains-kaart citeert: "Los servicers no son propietarios de la inmensa mayoría de los activos que gestionan" (brainsre.news, 26-03-2026, bijgewerkt 07-08-2026, pers).

---

## 3. Kaart van de sector in september 2026

Bewijstypen: 1 = door de partij zelf vermeld (eigen site of persbericht, of in de pers aan haar toegeschreven, dan "1-pers"); 2 = officiële bron (BOE, TED, ministerie); 3 = door ons vastgesteld op 15-09-2026; 4 = gevolgtrekking; 7 = onbekend of tegenstrijdig.

| Partij | Eigenaar (2026) | Rol en bekende mandaten | Verkoopportaal | Automatisch leesbaar? | Bewijs |
|---|---|---|---|---|---|
| **Sareb** | Publiek-private "bad bank"; in de TED-aankondiging een "Empresa pública bajo el control de una autoridad estatal" | Eigenaar van REO en leningen; afbouw tot eind 2027; transfer naar Casa 47 | sareb.es/buscador-de-inmuebles (verwijst naar de servicers) | **Nee**: 403 (Imperva) | TED 140491-2026 (2); BOE RD 1559/2012 (2) |
| **Aliseda Inmobiliaria** (+ **Anticipa**) | Blackstone; volgens pers 2023/24 met een Santander-minderheidsbelang [te verifiëren] | Servicer van Sareb (2022–2026, en opnieuw vanaf 2026); eigen REO/NPL van Blackstone | alisedainmobiliaria.com (Anticipa-objecten met "ant"-referentie staan in dezelfde sitemap) | **Nee**: alleen JavaScript; sitemap openbaar | sitemap (3); El Español 13-06-2024 (1-pers); Brains 2026 (1-pers) |
| **Hipoges** | Pollen Street Capital (overname "julio 2026" volgens Brains) [te verifiëren] | Servicer van Sareb 2022–2026 (leningen en retail); tekent bezwaar aan tegen de gunning van Lot A | realestate.hipoges.com | **Nee**: alleen JavaScript; activa-sitemap leeg | hipoges.com (1); Brains 12-08-2026 (1-pers) |
| **Servihabitat** | Coral Homes (Lone Star 80 %, CaixaBank 20 %); verkoop aan Hipoges/Finsolutia (Pollen Street) aangekondigd | Coral Homes, Green, Kutxabank; Sareb-grond (NEO); nieuw Sareb-contract 2026 | servihabitat.com (particulieren), inversores.servihabitat.com (professionals) | **Ja, server-gerenderd**, maar voorwaarden verbieden exploitatie | eigen site (1/3); ON ECONOMIA 03-08-2026 (1-pers) |
| **Solvia** (incl. Haya, Aktua, HRE) | Intrum AB | CaixaBank/BuildingCenter (verkoop, 2023, 3 jaar + 18 mnd), Ibercaja (tot 2029), Sabadell (historisch, sinds 2019); BBVA-portefeuille via Haya (verloopt 2026 volgens pers) | solvia.es | **Ja, server-gerenderd**, maar voorwaarden: alleen "uso propio y personal" | caixabank.com (1); ibercaja.com (1); idealista/news 16-12-2024 (1-pers) |
| **Haya Real Estate** | Intrum (overgenomen 2023; gefuseerd in Solvia, dec 2024) | Geen apart kanaal meer | haya.es → **HTTP 522** op 15-09-2026 | Nee | curl (3); idealista/news (1-pers) |
| **Altamira / doValue** | doValue S.p.A.; Santander verkocht zijn 15 % | Servicer van leningen en vastgoed; nieuwe SLA met Santander (dec 2025) | altamirainmuebles.com (volgens dovalue.es) | **Nee**: 403 zonder browser | dovalue.es (1); Stockopedia 03-12-2025 (1-pers) |
| **Diglo** | 100 % Grupo Santander (eigen site: "100% Grupo Banco Santander") | Vastgoed van Santander en het grootste deel van de probleemleningen (april 2026) | digloservicer.com (**niet** diglo.com: dat is een Amerikaanse webwinkel) | **Ja, server-gerenderd**, maar voorwaarden verbieden "extracción y/o reutilización" | eigen site (1/3); idealista/news 08-04-2026 (1-pers) |
| **CaixaBank** | Bank; vastgoeddochter BuildingCenter | Verkoop via Solvia-Intrum (sinds 2023); portaal Facilitea Casa (2025, incl. BuildingCenter-objecten) | faciliteacasa.com (van CaixaBank Group) | Deels server-gerenderd; Jávea-slug geeft 0 (niet sluitend) | caixabank.com 25-05-2023 (1); faciliteacasa.com (3) |
| **BBVA** | Bank | Vastgoed historisch via Haya (nu Solvia); Intrum-akkoord 04-12-2024 betreft **private banking**, geen REO | Geen eigen Spaans portaal gevonden | – | intrum.es (1); El Español 28-08-2024 (1-pers) |
| **Banco Sabadell** | Bank | Verkocht Solvia aan Intrum (2019) met servicingcontract | Via solvia.es | – | intrum.es-titel (1); huidige looptijd ONBEKEND |
| **Bankinter** | Bank | Eigen vastgoedportaal (klein aanbod) | bankinter.com/www/es-es/cgi/ebk+inm+home | **Nee**: Cloudflare-controle | curl (3) |
| **Unicaja** | Bank (portaal "Unicaja Banco S.A., titular de la página web") | Intern (GIA) volgens pers | unicajainmuebles.com | Formulier gezien; direct GET → foutpagina; handmatig | eigen site (1/3) |
| **Kutxabank** | Bank | Servicer is Servihabitat (sinds 2022: 9.000 activa, volgens pers) | via servihabitat.com/es/kutxabankinmobiliaria | Idem Servihabitat | servihabitat.com (1/3); elEconomista 2022 (1-pers) |
| **Cajamar** | Coöperatieve bank | Eigen vastgoedbedrijf **Cimenta2, Gestión e Inversiones, S.A.** | cimenta2.com (zoekfunctie alleen met JavaScript) | Nee | cajamar.es → cimenta2.com (3) |
| **Abanca** | Bank | Portaal EscogeCasa | escogecasa.es (alleen JavaScript) | Nee | curl (3); Idealista-profiel "ESCOGEcasa" onder /pro/abanca/ (1, via zoekresultaat) |
| **Ibercaja** | Bank | Intrum/Solvia tot 2029 (portefeuille 200 M€) | ibercaja.es/particulares/portalinmobiliario/ → solvia.es; oude subdomein bestaat niet meer (DNS) | Via Solvia | ibercaja.com 02-12-2025 (1); curl/dig (3) |
| **Banca March** *(niet gevraagd, wel gevonden)* | Bank | Adverteert "de bancos"-objecten in Marina Alta op Idealista | via Idealista (profiel /pro/banca-march/) | Via Idealista-assistent | Idealista property_detail (3) |

---

## 4. Per partij

### 4.1 Sareb

| Onderwerp | Bevinding | Bron | Type |
|---|---|---|---|
| Maximale duur | Art. 16.3 RD 1559/2012: de looptijd "no podrá ser superior a 15 años"; geconsolideerde tekst bijgewerkt 19-01-2022 | https://www.boe.es/buscar/act.php?id=BOE-A-2012-14118 | 2 |
| Einddatum | 28-11-2027 als "cierre" en "liquidación comercial a finales de 2027", volgens pers; Sareb verwacht zelf niet alles in 2027 te kunnen verkopen | eldiario.es 29-05-2026; elEconomista 04/2024 (titel) | 1-pers |
| Transfer naar Casa 47 | Akkoord Consejo de Ministros 01-07-2025, gepubliceerd als Orden PJC/784/2025 (BOE 23-07-2025) | https://www.boe.es/diario_boe/txt.php?id=BOE-A-2025-15292 | 2 |
| Criteria woningen | Gemeenten > 5.000 inwoners (Jávea valt daaronder, bewijstype 4); woningen "de hasta 85 m2 útiles independientemente del valor de tasación" of tot 150 m² onder een waardegrens | idem | 2 |
| Criteria grond | > 150 m², "uso global residencial plurifamiliar", geschikt voor "promociones de 30 o más viviendas", in vol eigendom van Sareb | idem | 2 |
| Omvang | "más de 40.000 viviendas y cerca de 2.400 suelos" (voorlopige identificatie, geen afgeronde transfer) | https://www.casa47.es/en/traspaso-vivienda-y-suelo | 2 |
| Gevolg voor Jávea | Kleine Sareb-woningen en meergezinsgrond in Jávea gaan eerder naar Casa 47 dan de vrije markt op; wat overblijft voor verkoop zijn vooral grotere woningen, eengezinsgrond en objecten met gebreken | afgeleid van de criteria | 4 |
| Servicers 2022–2026 | Hipoges en Anticipa-Aliseda: leningen en retail-woningen, plus voorbereiding van de Casa 47-transfer | eldiario.es 29-05-2026 | 1-pers |
| Nieuw contract 2026 | Servihabitat en Anticipa-Aliseda krijgen de hoogste scores; 174 M€ maximaal; 4.860 M€ nettoboekwaarde; 2 jaar + 4 maanden overdracht + 2 × 1 jaar verlenging | https://www.eldiario.es/economia/servihabitat-anticipa-aliseda-llevan-ultimo-gran-contrato-sareb-174-millones-deshacerse-4-860-m_1_13260273.html | 1-pers |
| Bezwaar | Hipoges vecht de gunning van Lot A aan (Servihabitat 92,27 punten tegen Hipoges 87,02); Sareb zette het proces op 03-08-2026 stil; uitspraak "en cuestión de días o semanas" | https://brainsre.news/disputa-hipoges-servihabitat-viviendas-sareb/ (12-08-2026) | 1-pers; afloop **7** |
| Nieuwbouw, grond | Nieuwbouwprojecten via Árqura Homes/Aelca, eigen afgebouwde projecten via Grupo Domo, ontwikkelgrond via Serviland. **Alleen gezien in een zoekmachinesamenvatting van sareb.es** (pagina zelf geblokkeerd) | sareb.es/preguntas-frecuentes (403) | 1, **laag**, [te verifiëren] |
| Zoekfunctie | Sareb heeft "Buscador de inmuebles"; de samenvatting noemt maandelijkse updates en objecten in "toma de posesión". Pagina geblokkeerd | https://www.sareb.es/buscador-de-inmuebles/ | 1, **laag** |
| Leningportefeuilles | Aanbesteding "Servicio de asesor financiero para venta de carteras": adviseur voor verkoop van "carteras de deuda mayoritariamente unsecured" in 2026 (mogelijk 2027); geraamde waarde 820.000 € excl. btw; 12 maanden + 1 verlenging; intern nr. 2026-P043 (OJ S 41/2026) | https://ted.europa.eu/es/notice/140491-2026/pdf | 2 |
| Financiën | Verlies 2025: 3.140 M€; senior schuld eind 2025: 27.790 M€ | idealista/news 30-07-2026; elEconomista 07/2026 (via zoekresultaat) | 1-pers |
| Live telling Jávea | **ONBEKEND**: sareb.es blokkeert automatische toegang (403, Imperva) | – | 3 (blokkade) |

**Oordeel (4):** voor TREE is Sareb geen eigen kanaal. Relevant is alleen wat Aliseda of Servihabitat voor Sareb aanbiedt, en dat zien we via hun portalen of Idealista. De onzekerheid over Lot A kan de verkoop tot eind 2026 vertragen [te verifiëren].

### 4.2 Aliseda Inmobiliaria en Anticipa (Blackstone)

| Onderwerp | Bevinding | Bron | Type |
|---|---|---|---|
| Juridische entiteit | Aliseda Servicios de Gestión Inmobiliaria SL, NIF B86875689 (bedrijfsregisterdienst; aviso legal niet leesbaar) | empresia.es / infonif (zoekresultaat) | 1, middel |
| Eigenaar | Blackstone (51 %) met Santander als minderheid (pers 2023/24); Brains 2026 noemt alleen Blackstone | El Español 13-06-2024; brainsre.news 2026 | 1-pers, **7** (verhouding onzeker) |
| Portaal | alisedainmobiliaria.com: Angular-app, HTML-omhulsel van 3,9 KB zonder objecten; WebFetch ziet alleen "Aliseda" | curl, WebFetch | 3 |
| Sitemaps (openbaar) | sitemap-index-aliseda.xml met inmuebles (es/en/fr), promociones, categorieën; plus **sitemap-loans.xml** (URL's /npl/…) en sitemap-investors.xml | https://www.alisedainmobiliaria.com/robots.txt | 3 |
| Omvang | Spaanse objectsitemap: **5.505** object-URL's (heel Spanje; niet noodzakelijk actief); een deel met prefix "ant" (Anticipa) | sitemap-inmuebles-aliseda-es-0.xml | 3 |
| Marina Alta (categoriepagina's in de sitemap) | Terreinen: Benigembla, Benissa, Dénia, **Jávea/Xàbia**, Teulada. Woningen: Benitachell, Calp, Ondara, Pedreguer. Obra parada: Gata de Gorgos. Garages: Beniarbeig | sitemap-category-aliseda-es-0.xml | 3 (signaal, **geen** live telling) |
| Account-functies | robots.txt noemt /mis-busquedas, /mis-favoritos, /reserva/agendar-visita: opgeslagen zoekopdrachten en reserveren met account | robots.txt | 3 |
| NPL-verkoop | Sectie "inversion/prestamos-y-cesiones-remate/npls" en pagina's "Comprar NPL: n Inmuebles asociados al NPL" | zoekresultaten van alisedainmobiliaria.com | 1 |
| API/feed | Niet gevonden | – | 3 |
| Voorwaarden | Aviso legal niet leesbaar (alleen JavaScript) | – | 7 |
| Live telling Jávea | **ONBEKEND** (alleen JavaScript). De categoriepagina voor Jávea-grond bestaat in de sitemap | – | 3/7 |

### 4.3 Hipoges

| Onderwerp | Bevinding | Bron | Type |
|---|---|---|---|
| Rol | "la compañía de referencia en la gestión de activos"; portaal "Portal Inmobiliario" | https://www.hipoges.com | 1 |
| Portaal | realestate.hipoges.com/es: meta "Venta y alquiler de inmuebles al mejor precio"; alleen JavaScript (5,6 KB) | curl | 3 |
| Sitemap | activo_es_sitemap.xml is leeg (54 bytes, 0 URL's) | curl | 3 |
| Aanbod voor schuldbeleggers | "más de 2.500" NPL's met hypotheek, > 500 M€ (pers); aparte teams voor veilingen, *cesiones de remate*, objecten zonder bezit, grond en onafgebouwde projecten | estrategiasdeinversion.com; observatorioinmobiliario.es | 1-pers, laag |
| Eigenaar | Pollen Street Capital (overname "julio 2026") | brainsre.news 2026 | 1-pers, [te verifiëren] |
| Live telling Jávea | **ONBEKEND** | – | 3/7 |

### 4.4 Servihabitat (gecontroleerd kanaal; server-gerenderd)

| Onderwerp | Bevinding | Bron | Type |
|---|---|---|---|
| Juridische entiteit | "Servihabitat Servicios Inmobiliarios, S.L.U. … CIF B-66082629 … Avenida de Burgos, 12, 28036 Madrid" | https://www.servihabitat.com/es/terminos-generales-de-uso | 1 |
| Eigenaar | Coral Homes (Lone Star 80 %, CaixaBank/BuildingCenter 20 %); akkoord over verkoop aan Hipoges en Finsolutia (Pollen Street) | ON ECONOMIA 03-08-2026 | 1-pers, [te verifiëren: closing] |
| Opdrachtgevers op de site | Links "Inmuebles Kutxabank", "Inmuebles de Coral Homes" (740 in verkoop), "Inmuebles de Green" (492 in verkoop). Het woord "Sareb" komt op de homepage niet voor | servihabitat.com/es/, /es/land/coralhomes, /es/land/green | 3 |
| Zoekfilters | URL-patroon /es/venta/{type}/{provincie}-{comarca}-{gemeente}, bijv. …/terreno/alicante-marinaalta; typen vivienda, local, terreno, edificio, obra parada, "Viviendas sin posesión" | eigen pagina's | 3 |
| Alerts | "+ Crear alerta", "Guardar búsqueda", "Te informaremos si bajan de precio" (account nodig) | idem | 3 |
| Professioneel portaal | inversores.servihabitat.com: "Esta página está destinada para profesionales"; "Alta como profesional"; categorieën fincas rústicas, suelos, viviendas sin posesión, naves | https://inversores.servihabitat.com/es/ | 1 |
| Eigen veilingvorm | "WOW! Venta Especial": online biedproces met tijdklok en borg, via "API Colaborador" (hier: **Agente de la Propiedad Inmobiliaria**, geen software-API) | https://www.servihabitat.com/es/wowventasespeciales | 1 |
| Samenwerkende makelaars | Netwerk van *API colaboradores*; een makelaar in Calp presenteert zich als "agente colaborador oficial" | zoekresultaten (leukanterealty.com e.a.) | 1, laag |
| Voorwaarden | "Queda prohibida cualquier modalidad de explotación, incluyendo todo tipo de reproducción, distribución, cesión a terceros…" | terminos-generales-de-uso | 1 |
| robots.txt | Sluit o.a. /venta (zonder taalprefix) en filterparameters uit; /es/venta/… is toegestaan | https://www.servihabitat.com/robots.txt | 3 |
| API/feed | Niet gevonden | – | 3 |

**Live tellingen Servihabitat, 15-09-2026 (bewijstype 3; getal zoals het portaal het toont):**

| Portaal | Selectie | Alicante | Marina Alta | Jávea |
|---|---|---|---|---|
| Particulieren | Woningen | **74** (o.a. Marina Baja 33, Vega Baja 20) | **0** | **0** |
| Particulieren | Terreinen | **41** | **18**: Benitachell 2, Pego 6, El Ràfol d'Almúnia 8, El Verger 2 | **0** |
| Particulieren | Bedrijfsruimtes | 9 | 0 | 0 |
| Particulieren | Gebouwen | 0 | 0 | 0 |
| Profesionales | Woningen | 5 | 0 | 0 |
| Profesionales | Terreinen | **66** | **9**: "balcon al mar (javea)" 1, Pego 5, Teulada 1, El Verger 2 | **1 in de lijst + 1 onder de verkeerde comarca** (§6) |
| Profesionales | Obra parada | 0 | – | – |

**Lessen (bewijstype 3):**
- Het professionele portaal toont aanbod dat op het publieke portaal ontbreekt.
- De plaatsindeling is onbetrouwbaar: het Cap Martí-perceel staat onder "alicante-huertasur-xabia" en telt daardoor niet mee in Marina Alta. Elke koppeling moet op coördinaten of gemeentecode normaliseren, niet op de naam van de comarca.

### 4.5 Solvia (Intrum), inclusief Haya

| Onderwerp | Bevinding | Bron | Type |
|---|---|---|---|
| Juridische entiteit | "Solvia está provista de C.I.F. nº A-86744349"; c/ Vía de los Poblados nº 3, Madrid | https://www.solvia.es/es/aviso-legal | 1 |
| Fusie | Intrum voegt Haya Real Estate, Solvia, Aktua en HRE samen tot Solvia Servicios Inmobiliarios (ca. 170.000 activa) | https://www.idealista.com/news/inmobiliario/empresas/2024/12/16/824621-intrum-fusiona-sus-servicers-inmobiliarios-para-simplificar-su-estructura-en-espana | 1-pers |
| haya.es | DNS naar Cloudflare; HTTPS geeft **522** op 15-09-2026 | curl | 3 |
| Mandaten | CaixaBank/BuildingCenter: "Solvia-lntrum" voor verkoop en onderhoud, 3 jaar + 18 maanden (persbericht 25-05-2023) | https://www.caixabank.com/en/headlines/news/buildingcenter-selects-the-new-servicing-providers-for-the-sale-maintenance-and-rental-management-of-caixabanks-real-estate-portfolio-for-the-forthcoming-three-years | 1 |
| | Ibercaja: vernieuwd tot 2029, portefeuille 200 M€ (02-12-2025) | https://www.ibercaja.com/detalle-sala-de-prensa/noticias/9885 | 1 |
| | BBVA: akkoord van 04-12-2024 gaat over beleggingsvraag van private-bankingklanten, **niet** over BBVA's eigen vastgoed | https://www.intrum.es/empresas/sobre-intrum/comunicacion/noticias/intrum-firma-un-acuerdo-con-bbva-para-la-comercializacion-de-activos-inmobiliarios-dirigidos-a-banca-privada-y-altos-patrimonios/ | 1 |
| | Sabadell: servicingcontract sinds de verkoop van Solvia (2019); huidige looptijd ONBEKEND | intrum.es (titel) | 1 / 7 |
| Zoekfilters | /es/comprar/{type}/{provincie}/{gemeente}; "Provincia, población, CP…" | solvia.es | 3 |
| Alerts | Na registratie: "podrás crear alertas y saber al instante todas las novedades y actualizaciones de los inmuebles de tu zona" | solvia.es | 1 |
| Professionals | /es/login-profesional ("Acceso al Área Profesionales") | solvia.es | 3 |
| Labels | "INMUEBLE DE BANCO" en "EN SITUACIÓN ESPECIAL" bij een deel van de objecten; andere zijn "A estrenar" (nieuwbouw) | lijstpagina's Alicante | 3 |
| Voorwaarden | 4.4.2: gebruik alleen "para uso propio y personal"; geen handelingen die "suponga una explotación comercial" | aviso-legal | 1 |
| robots.txt | Sluit /api/ en /ajax/ uit; sitemap.xml met 44 deelsitemaps | https://www.solvia.es/robots.txt | 3 |

**Live tellingen Solvia, 15-09-2026 (bewijstype 3):**

| Selectie | Alicante | Marina Alta (gemeentepagina's) | Jávea |
|---|---|---|---|
| Woningen | **511** | Dénia 6 · Calp 17 · Benissa 4 · Teulada 1 · Ondara 2 · Pego 2 · Pedreguer en Gata: geen telling getoond | Geen gemeentepagina in de sitemap; /javea toont geen objecten → **waarschijnlijk 0** (4) |
| Grond | **202** | Benissa 1 · Pego 1 (beide met label "INMUEBLE DE BANCO"). Op de Alicante-pagina staan ook Dénia-objecten (Monte Pego II, C/ Riu Senia, Ronda Murallas), maar /suelos/alicante/denia gaf geen telling | Geen pagina → **waarschijnlijk 0** (4) |

### 4.6 Altamira en doValue

| Onderwerp | Bevinding | Bron | Type |
|---|---|---|---|
| Wie | "un servicer líder en España, especializado en la gestión de carteras de crédito y activos inmobiliarios de bancos e inversores"; merknaam doValue; vastgoedportaal altamirainmuebles.com | https://dovalue.es/ | 1 |
| Santander | Santander verkocht zijn 15 % in doValue España; nieuwe "Strategic Service Level Agreement" met Santander (03-12-2025). Reikwijdte niet in de bron | brainsre.news; stockopedia.com | 1-pers |
| Tegenstrijdigheid | idealista/news (08-04-2026): Diglo krijgt het vastgoed "y de la mayor parte de su cartera de créditos impagados" van Santander. Hoe dit zich verhoudt tot de doValue-SLA is onduidelijk | – | **7** |
| Portaal | altamirainmuebles.com geeft **403** aan WebFetch en aan curl zonder browser-UA; niet omzeild | curl, WebFetch | 3 |
| Live telling Jávea | **ONBEKEND** | – | 7 |

### 4.7 Diglo (Santander)

| Onderwerp | Bevinding | Bron | Type |
|---|---|---|---|
| Juridische entiteit | "Diglo Servicer Company 2021, S.L., con C.I.F. B-67915298"; Calle Josefa Valcárcel 34, Madrid | https://digloservicer.com/aviso-legal | 1 |
| Rol | Doel van de site: "inmuebles propiedad de terceros, comercializados por DIGLO"; lijstpagina's: "100% Grupo Banco Santander" | idem; lijstpagina's | 1 |
| Mandaat 2026 | Vastgoed van Santander en het grootste deel van de probleemleningen | https://www.idealista.com/news/finanzas/economia/2026/04/08/892128-diglo-gestionara-la-venta-de-los-activos-inmobiliarios-de-banco-santander-y-la-mayoria | 1-pers |
| Filters | /venta-{type}/cualquiera/{provincie}; typen casas-pisos, terrenos, locales, naves, obras-paradas, hoteles | digloservicer.com | 3 |
| Alerts | "Activa ahora tu alerta personalizada" (account nodig) | obras-paradas-pagina | 1 |
| Beleggers | "Venta de Créditos": "comprar cesión de créditos, venta en subastas y cesiones de remates con garantía de activos inmobiliarios"; ook "El precio lo pones tú" | /oportunidades/venta-credito | 1 |
| Voorwaarden | "queda expresamente prohibido … extracción y/o reutilización del Sitio Web, sus Contenidos" | aviso-legal | 1 |
| Institutionele verkoop | Diglo zet 40 M€ aan dubieuze leningen te koop (27-01-2026) | infobae.com (titel) | 1-pers |
| **Live telling 15-09-2026** | Alicante casas-pisos **4** (Redován, Cocentaina, Callosa de Segura, Elche) · locales **20** (o.a. Benissa, Dénia) · obras paradas **0** · terrenos: pagina valt terug op "342 inmuebles de banco en venta en España", dus geen Alicante-terrein zichtbaar · **Jávea 0** | lijstpagina's | 3 |

### 4.8 CaixaBank (BuildingCenter, Facilitea Casa)

| Onderwerp | Bevinding | Bron | Type |
|---|---|---|---|
| Vastgoeddochter | BuildingCenter koos Solvia-Intrum (verkoop en onderhoud), Azzam (verhuur) en Haya (onderhoud ex-Bankia) | caixabank.com 25-05-2023 | 1 |
| Einde contract | 3 jaar + 18 maanden → basisperiode rond medio 2026; verlenging of opvolger **ONBEKEND** | afgeleid | 4, [te verifiëren] |
| Intern servicing | Kop: "CaixaBank internalizará toda la operativa de servicing en tres años" (artikel geeft 403) | ejeprime.com | 1-pers, **laag** |
| Portaal | Facilitea Casa (Facilitea Selectplace S.A.U., CaixaBank Group); catalogus bevat volgens CaixaBank objecten van BuildingCenter; vooral makelaarsaanbod | caixabank.com (zoekresultaat); faciliteacasa.com | 1 |
| Telling | "17422 casas y pisos en Alicante" (alle aanbieders); /Jávea en /Xàbia tonen "0" (slug-normalisatie onbewezen) | faciliteacasa.com | 3; Jávea-waarde **7** |
| Voor TREE Properties | "Únete como inmobiliaria": publiceren zonder kosten volgens CaixaBank. Dat is een publicatiekanaal, geen lees-API | facilitea.com (zoekresultaat) | 1 |
| Servihabitat | CaixaBank bezit via BuildingCenter 20 % van Coral Homes, eigenaar van Servihabitat | ON ECONOMIA | 1-pers |

### 4.9 BBVA

| Onderwerp | Bevinding | Bron | Type |
|---|---|---|---|
| Kanaal | Geen eigen Spaans vastgoedportaal gevonden (bbva.com-zoekopdracht gaf Mexico en algemene pagina's); bbvavivienda.com: TLS-certificaatfout en HTTP/2-fout | WebSearch; curl | 3 |
| Historisch | Haya beheerde BBVA-vastgoed; volgens El Español (28-08-2024) verlopen in 2026 contracten voor een BBVA-portefeuille van ca. 3.000 M€ bij Intrum | elespanol.com | 1-pers |
| Huidig | **ONBEKEND** (verlengd, opnieuw aanbesteed of intern) | – | 7 |

### 4.10 Banco Sabadell

Solvia was van Sabadell en is sinds 2019 van Intrum, met een contract voor beheer en verkoop van Sabadells *adjudicados* (intrum.es, titel "Intrum completa la adquisición de Solvia a Banco Sabadell"; bewijstype 1). Sabadell-objecten staan dus op solvia.es. Een apart Sabadell-portaal of de huidige looptijd is niet gevonden (7).

### 4.11 Bankinter

Portaal op bankinter.com/www/es-es/cgi/ebk+inm+home (zoekresultaat). Op 15-09-2026 gaf dat een 403 met Cloudflare-controle ("Just a moment..."); niet omzeild (bewijstype 3). Een zoekresultaat van Fotocasa noemt "44 inmuebles de BANKINTER en venta en España" (derde partij, datum onbekend; 7). Jávea: ONBEKEND.

### 4.12 Unicaja

| Onderwerp | Bevinding | Bron | Type |
|---|---|---|---|
| Portaal | unicajainmuebles.com; "Unicaja Banco S.A., titular de la página web" | cookietekst op de site | 1 |
| Filters | Type, operación, provincie (Alicante = 3), gemeente, zone, postcode, en "PUBLICADO: ÚLTIMA SEMANA / ÚLTIMO MES": bruikbaar om nieuw aanbod te zien | formulier | 3 |
| Toegang | Een GET met exact de formuliervelden gaf twee keer /errorPublico.do (ook met sessiecookie); daarna gestopt | curl | 3 |
| Live telling Jávea | **ONBEKEND**: alleen handmatig | – | 7 |

### 4.13 Kutxabank

Servihabitat beheert Kutxabanks vastgoed. Op de homepage van Servihabitat staat de link "Inmuebles Kutxabank" (/es/kutxabankinmobiliaria, titel "KutxaBank Home ES - Servihabitat", noindex; bewijstype 3). Volgens de pers ging het in 2022 om 9.000 activa (elEconomista, titel; 1-pers). Tellingen voor Jávea: zie Servihabitat (0 woningen, 0 publiek, 1–2 professionele percelen van onbekende eigenaar). Kutxabank publiceert daarnaast pdf-lijsten van samenwerkende makelaars per regio, ook voor de Comunidad Valenciana (zoekresultaat, clientes.kutxabank.es; niet geopend).

### 4.14 Cajamar

De pagina "Portal de inmuebles disponibles" op cajamar.es verwijst naar **cimenta2.com**. Voettekst daar: "© 2026 Cimenta2, Gestión e Inversiones, S.A." (bewijstype 3). Promoties: o.a. "Suelos urbanos y urbanizables con grandes descuentos". De geavanceerde zoekfunctie (/buscador-avanzado/) toont zonder JavaScript geen objecten, dus een telling voor Jávea is **ONBEKEND**. robots.txt: "Disallow:" (leeg). Oude persberichten over Cajamar met Haya staan nog op cajamar.es; volgens Brains (2026) nam Cajamar het beheer terug (juni 2024; 1-pers, [te verifiëren]).

### 4.15 Abanca

Portaal **EscogeCasa** (escogecasa.es, titel "EscogeCasa | Encuentra tu próximo hogar"; HTML van 2,9 KB, alleen JavaScript; bewijstype 3). De koppeling aan Abanca blijkt uit het Idealista-profiel "ESCOGEcasa" onder /pro/abanca/ (zoekresultaat; 1). Jávea: **ONBEKEND**.

### 4.16 Ibercaja

De eigen pagina zegt: "Encuentra tu nueva casa de la mano de Solvia e Ibercaja", met een doorverwijzing naar solvia.es (?esOrigenProducto=IBERCAJA) (bewijstype 1). Het oude subdomein portalinmobiliario.ibercaja.es is niet meer vindbaar in DNS (bewijstype 3). Contract met Intrum tot 2029 (§4.5).

### 4.17 Gespecialiseerde platforms

| Platform | Wat | Bevestigd? | Advies |
|---|---|---|---|
| Servihabitat "WOW! Venta Especial" | Eigen online biedverkoop met borg | Ja, eigen site (1) | Meenemen in de handmatige ronde |
| Diglo "Venta de Créditos" / "El precio lo pones tú" | Leningen, veilingen, *cesiones de remate*; biedactie | Ja, eigen site (1/3) | Niet in fase A (juridisch) |
| Aliseda NPL-sectie | Losse NPL's met onderpand | Ja: sitemap en paginatitels (1/3) | Niet in fase A (juridisch) |
| Hipoges schuldbeleggersportaal | NPL's, *cesiones de remate* | Alleen pers (1-pers) | Niet in fase A |
| BidX1 | Online veilingen voor fondsen (Spanje sinds 2019) | Alleen pers 2019–2020; status 2026 niet vastgesteld | TECHNISCH ONDERZOEK NODIG |
| Inmubi, Fencia, cristinamoriones.com, comprardeudahipotecaria.com | Doorverkoop of bemiddeling van NPL's, *cesiones de remate*, objecten zonder bezit | **Niet** bevestigd als geautoriseerd kanaal van een bank of servicer; alleen zelfbeschrijving of blog (Subastanomics) | NIET GEBRUIKEN tot er bewijs van mandaat is |

---

## 5. Live metingen via de Idealista-assistent (15-09-2026, bewijstype 3)

Aanroepen: locale es-ES, country es, operatie SALE. **Controleer altijd of het veld `summary` "De bancos" bevat:** in één aanroep verviel het filter stilletjes (zie Q9).

| # | Zoekopdracht (kern) | Type | Locatie volgens de tool | Filter "De bancos" toegepast? | Totaal |
|---|---|---|---|---|---|
| Q1 | viviendas de bancos Jávea | HOME | Jávea/Xàbia | ja | **0** (gelijk aan 14-09) |
| Q2 | terrenos de bancos Jávea | LAND | Jávea/Xàbia | ja | **1** (code 111869151) |
| Q3 | locales/naves/edificios de bancos Jávea | WAREHOUSE | Jávea/Xàbia | ja | **0** |
| Q4 | viviendas de bancos Dénia "(cerca de Jávea)" | HOME | **Carretera de Denia (in Jávea)** | ja | 0, maar verkeerde locatie |
| Q5 | casas y pisos de bancos municipio de Dénia | HOME | Denia | ja | **0** |
| Q6 | terrenos de bancos Dénia | LAND | Denia | ja | **2** (Monte Pego) |
| Q7 | terrenos de bancos Benitachell | LAND | Benitachell | ja | **1** |
| Q8 | terrenos de bancos Teulada (2 varianten) | LAND | Carretera Moraira a Teulada / **Calle Cruz del Sur (Jávea)** | ja | 0, maar verkeerde locatie → niet sluitend |
| Q9 | locales/naves/oficinas de bancos comarca Marina Alta | WAREHOUSE | Marina Alta | **nee** (summary zonder "De bancos"; 462 gewone objecten) | ongeldig |
| Q10 | casas y pisos de bancos (Benissa / Pedreguer / Teulada) | HOME | tool koos **Marina Alta** | ja | **1** (Calp, Banca March) |
| Q11 | casas y pisos de bancos Gata de Gorgos | HOME | Avenida de la Marina Alta (Gata) | ja | 0, straatniveau |
| Q12 | terrenos de bancos comarca Marina Alta | LAND | Marina Alta | ja | **20** |

**Verdeling van de 20 bankpercelen in Marina Alta (Q12):** Jávea 1 · El Ràfol d'Almúnia 4 · Dénia/Monte Pego 2 · Pego 6 · El Verger 2 · Benitachell 1 · Benissa 1 (rústico) · Jalón 1 · Calp 1 · Moraira 1. Doorschakelnummers: 16 via het Servihabitat-nummer (bij 111869151 via `property_detail` bevestigd als "Servihabitat"), 4 via het nummer dat bij 91172562 als "Banca March" is bevestigd.

**Nieuwe waarnemingen over de tool (bewijstype 3):**
1. `property_detail` geeft wél `commercialName` (bijv. "Servihabitat", "Banca March"), `externalReference`, `micrositeUrl` en "Anuncio actualizado hace 3 días". De eerdere lokale notitie "geen makelaarsnaam" geldt alleen voor `search_properties`.
2. De verplichte vermelding "Jávea" in de zoekvraag laat de tool bij buurgemeenten soms een straat in Jávea kiezen (Q4, Q8). Gebruik voor buurgemeenten de comarca-formulering "comarca Marina Alta" (Q10, Q12).
3. Idealista's "de bancos" dekt niet alles. Solvia toont 6 woningen in Dénia en 17 in Calp, terwijl Idealista in heel Marina Alta 1 bankwoning telt. Óf die Solvia-objecten zijn geen bankbezit (Solvia verkoopt ook nieuwbouw), óf ze hebben dat label niet (bewijstype 4).

---

## 6. De twee Jávea-percelen uit bank- en servicerkanalen (objectgericht, niet beoordeeld)

> Alleen gegevens zoals de aanbieder ze vermeldt (bewijstype 1), door ons gezien op 15-09-2026 (bewijstype 3). Planologische beweringen zijn **[te verifiëren]** via R11 (kadaster en register) en de gemeente. Geen biedadvies. Eigenaar ONBEKEND: Servihabitat verkoopt voor meerdere opdrachtgevers.

| Veld | Perceel A: Balcón al Mar | Perceel B: Toscal–Cap Martí |
|---|---|---|
| Kanaal | Servihabitat Profesionales + Idealista ("de bancos") | Alleen Servihabitat Profesionales (niet in de Idealista-lijst gezien) |
| Referenties | Servihabitat promotie 06124187 / eenheid 06145700 (link-id 60709759); Idealista 111869151 (externalReference 60709763) | Servihabitat promotie 06124173 / eenheid 60709315 |
| Aanbod | "TERRENO URBANO NO CONSOLIDADO, 16 fincas con un total de 17.775 m2", sector "PGOU UA BALCON AL MAR 1" | "1 finca de suelo urbano no consolidado" van 4.622 m², "72,22%" van de UA Toscal-Cap Martí |
| Prijs | 725.000 € ("Desde"); Idealista: eerder 904.000 € (−20 %) | "Precio a consultar" |
| Bouwmogelijkheid volgens aanbieder | Max. 3.554 m²c "tras las gestiones y transformaciones pertinentes"; gemiddeld 222 m²c per woning; aandeel 26,85 % | "edificabilidad prevista es de 623 m2, para un total de 3 viviendas unifamiliares"; programa en urbanisatieproject goedgekeurd, herverkaveling "en curso" |
| Verkoopvoorwaarden | "destinada a profesionales"; btw-plichtig; Idealista: "posible proceso competitivo o … (POV)" en "periodo de transparencia de 20 días naturales máximo" | "destinada a profesionales"; btw-plichtig |
| Plaatsindeling op het portaal | comarca Marina Alta, "balcon al mar (javea)" | **Verkeerd:** "huerta sur / xabia" |
| Routes | B (grond en ontwikkeling); mogelijk D | B |
| Rode vlaggen (4) | Niet geconsolideerd: urbanisatiekosten en -plichten, termijnen, 26,85 % betekent medeplichtigheid in het plangebied, verkocht als pakket van 16 fincas | Onverdeeld aandeel (72,22 %) in een lopende herverkaveling; prijs onbekend |
| Vervolg | R11: fincas en kadastrale referenties vaststellen; stand van de UA bij Xàbia Urbanismo; ficha opvragen (download = akkoord Jan) | Idem |

---

## 7. Leningen, NPL's en portefeuilles: eerlijk over onze positie

1. **Portefeuilles** (Sareb, banken) worden via adviseurs en aanbestedingen verkocht aan institutionele partijen. De TED-aanbesteding 140491-2026 gaat alleen al over de *adviseur*, met een geraamde waarde van 820.000 € (bewijstype 2). **TREE zit hier niet aan tafel** en hoeft dat ook niet (bewijstype 4).
2. **Losse NPL's en *cesiones de remate*** worden wel online aangeboden aan "inversores especializados": Aliseda (/npl/), Diglo ("Venta de Créditos"), Hipoges (bewijstype 1/3). Wat je dan koopt is een vordering of een positie in een veiling, niet het huis. Rangorde van lasten, bewoning, doorlooptijd van de executie en proceskosten bepalen het resultaat (§19; zie R09). **Zonder advocaat geen stap.**
3. **Leningen zijn geen bron voor een monitor.** De juiste bron voor executies in Jávea is de BOE (R08: Sección IV, rechtbank Dénia), plus het Registro Público Concursal voor faillissementen.
4. **Persoonsgegevens:** NPL-fiches kunnen tot schuldenaars herleidbaar zijn. Geen profielen bouwen (§19). Die pagina's nemen we niet op in onze database.

---

## 8. Is een dagelijkse monitor de moeite waard?

**Nee.** Wel een lichte, grotendeels handmatige opzet.

| Optie | Wat | Waarde voor Jávea | Toegang en rechten | Beoordeling |
|---|---|---|---|---|
| A. Eigen dagelijkse crawler op servicerportalen | HTML ophalen van Servihabitat, Solvia en Diglo | Gemiddeld 0–2 relevante objecten in Jávea; enkele tientallen in Marina Alta | **Strijdig** met de voorwaarden (exploitatie, extractie); de andere portalen zijn geblokkeerd of alleen JavaScript | **NIET GEBRUIKEN** |
| B. Wekelijkse check via de Idealista-assistent | 4 aanroepen: Jávea HOME en LAND "de bancos", Marina Alta HOME en LAND "de bancos"; nieuwe codes opslaan en detail ophalen | Vangt Servihabitat- en Banca March-objecten; mist Solvia en Aliseda deels | Officiële assistent; gepland of systematisch gebruik is nog **onbewezen** (R01) | Bruikbaar handmatig in een sessie; gepland: TECHNISCH ONDERZOEK NODIG |
| C. E-mailalerts van servicers | Zoekopdrachten opslaan voor Marina Alta en Alicante, grond en woningen: Servihabitat (particulier + professional), Solvia, Diglo, Aliseda | Rechtstreeks van de bron, geen scraping | Eigen functie van het portaal; **account nodig** (Jan maakt het aan) | **Aanbevolen** |
| D. Handmatige ronde per kwartaal | Unicaja (filter "última semana/mes"), Cimenta2, EscogeCasa, Bankinter, Altamira, Hipoges, Facilitea Casa, Sareb-zoekfunctie | Dekt de kanalen die we niet kunnen tellen | Gewone browser, geen automatisering | **Aanbevolen**, ca. 1–2 uur per kwartaal (5: aanname 8 portalen × 10–15 min) |
| E. Samenwerkend makelaar (*API colaborador*) bij servicers | TREE Properties aanmelden bij Servihabitat, Solvia en Aliseda voor Marina Alta | Vroege toegang tot aanbod dat niet op portalen staat; commissie (route D) | Contract of toestemming nodig; voorwaarden **ONBEKEND** | **Onderzoeken** (besluit Jan) |
| F. BOE-veilingen en RPC | Zie R08/R09 | Bron van toekomstig bankvastgoed | Officieel, open data | Loopt via R08 |

**Waarom niet dagelijks (4/5):**
- Onze metingen tonen in Jávea 0 bankwoningen en 1–2 percelen die al weken of maanden online staan (Idealista: "actualizado hace 3 días", met een eerdere prijs, dus niet nieuw).
- Bij een aanname van 0–2 nieuwe bankobjecten per maand in Jávea (5) is het verschil tussen dagelijks en wekelijks kijken verwaarloosbaar. Het verkoopproces met transparantieperiode en POV duurt zelf al tot 20 dagen.
- Een dagelijkse crawler brengt juridisch risico en onderhoud (wisselende URL-patronen, fusies, JavaScript-portalen) zonder aantoonbaar voordeel.

---

## 9. Registerregels (masterprompt §7)

| Naam | URL | Type | Toegang | Status | Opmerkingen |
|---|---|---|---|---|---|
| Sareb, zoekfunctie | https://www.sareb.es/buscador-de-inmuebles/ | Eigenaar REO/leningen (publiek-privaat) | Web; 403 (Imperva) voor automatisering | ALLEEN HANDMATIG | Afbouw tot eind 2027; Casa 47-transfer; verkoop via servicers |
| Sareb, aanbestedingen | https://ted.europa.eu/es/notice/140491-2026/pdf (en contrataciondelestado.es) | Officiële aanbestedingen | Open | ALLEEN HANDMATIG | Laat portefeuilleverkoop en servicercontracten zien; geen objecten |
| Casa 47, transfer Sareb | https://www.casa47.es/en/traspaso-vivienda-y-suelo | Publieke entiteit | Open | ALLEEN HANDMATIG | Context: welk Sareb-aanbod van de markt verdwijnt |
| Servihabitat (particulieren) | https://www.servihabitat.com/es/ | Servicer (Coral Homes, Green, Kutxabank e.a.) | Server-gerenderd web; alerts met account | ALLEEN HANDMATIG | Voorwaarden verbieden exploitatie; 15-09: Marina Alta 0 woningen, 18 terreinen, Jávea 0 |
| Servihabitat Profesionales | https://inversores.servihabitat.com/es/ | Professioneel servicerportaal | Web; "Alta como profesional" | ALLEEN HANDMATIG | 15-09: 2 Jávea-percelen; account door Jan |
| Solvia (Intrum; incl. Haya, Aktua, HRE) | https://www.solvia.es | Servicer (CaixaBank, Ibercaja, Sabadell e.a.) | Server-gerenderd web; alerts met account | ALLEEN HANDMATIG | Voorwaarden: "uso propio y personal"; Jávea waarschijnlijk 0 |
| Haya Real Estate | https://www.haya.es | Voormalige servicer | HTTP 522 | NIET GEBRUIKEN | Opgegaan in Solvia (dec 2024) |
| Aliseda Inmobiliaria (+ Anticipa) | https://www.alisedainmobiliaria.com | Servicer/eigenaar (Blackstone); Sareb-servicer | Alleen JavaScript; openbare sitemaps | ALLEEN HANDMATIG | Categoriepagina Jávea-grond in sitemap; NPL-sectie; telling onbekend |
| Anticipa | https://anticipa.com | Blackstone (vooral verhuur) | Alleen JavaScript | ALLEEN HANDMATIG | Verkoopobjecten lijken via het Aliseda-portaal te lopen ("ant"-refs) (4) |
| Hipoges Real Estate | https://realestate.hipoges.com/es | Servicer (Sareb 2022–26; Pollen Street) | Alleen JavaScript; lege sitemap | ALLEEN HANDMATIG | Bezwaar tegen Sareb Lot A |
| Altamira / doValue | https://www.altamirainmuebles.com | Servicer | 403 zonder browser | ALLEEN HANDMATIG | Relatie met Santander 2026 tegenstrijdig |
| Diglo | https://digloservicer.com | Servicer 100 % Santander | Server-gerenderd; alerts met account | ALLEEN HANDMATIG | Voorwaarden verbieden extractie; Alicante 4 woningen, 20 bedrijfsruimtes; Jávea 0 |
| Diglo "Venta de Créditos" | https://digloservicer.com/oportunidades/venta-credito | Leningen, *cesiones de remate* | Web | NIET GEBRUIKEN | Pas na juridische beoordeling (§19) |
| Aliseda NPL / *cesiones de remate* | https://www.alisedainmobiliaria.com/inversion/prestamos-y-cesiones-remate/npls | Leningen | Alleen JavaScript | NIET GEBRUIKEN | Idem |
| CaixaBank / Facilitea Casa | https://www.faciliteacasa.com | Bankportaal (incl. BuildingCenter) + makelaars | Server-gerenderd; slug voor Jávea onduidelijk | ALLEEN HANDMATIG | Publiceren als makelaar kosteloos volgens CaixaBank (publicatie ≠ lezen) |
| BBVA (vastgoed) | – | Bank | Geen portaal gevonden | TECHNISCH ONDERZOEK NODIG | Kanaal 2026 ONBEKEND (Haya/Intrum-contract verloopt 2026) |
| Banco Sabadell (vastgoed) | via https://www.solvia.es | Bank | via Solvia | ALLEEN HANDMATIG | Looptijd contract ONBEKEND |
| Bankinter, vastgoedportaal | https://www.bankinter.com/www/es-es/cgi/ebk+inm+home | Bank | Cloudflare-controle | ALLEEN HANDMATIG | Klein aanbod (derde partij: 44) |
| Unicaja Inmuebles | https://unicajainmuebles.com | Bank | Formulier; direct verzoek → foutpagina | ALLEEN HANDMATIG | Filter "publicado última semana/mes" |
| Kutxabank (via Servihabitat) | https://www.servihabitat.com/es/kutxabankinmobiliaria | Bank via servicer | idem Servihabitat | ALLEEN HANDMATIG | – |
| Cajamar / Cimenta2 | https://cimenta2.com | Vastgoedbedrijf van de bank | Zoekfunctie alleen met JavaScript | ALLEEN HANDMATIG | Promotie "suelos urbanos y urbanizables" |
| Abanca / EscogeCasa | https://www.escogecasa.es | Bankportaal | Alleen JavaScript | ALLEEN HANDMATIG | – |
| Ibercaja (via Solvia) | https://www.ibercaja.es/particulares/portalinmobiliario/ | Bank → Solvia | Verwijzing | ALLEEN HANDMATIG | Intrum tot 2029 |
| Banca March (via Idealista) | https://www.idealista.com/es/pro/banca-march/ | Bank (adverteerder) | Via Idealista-assistent | ALLEEN HANDMATIG | 4 van de 20 bankpercelen en 1 bankwoning in Marina Alta |
| Idealista-assistent, filter "de bancos" | (MCP van Idealista) | Portaalzoekfunctie | Sessie-tool | TECHNISCH ONDERZOEK NODIG | Handmatig bruikbaar; gepland gebruik onbewezen; filter kan vervallen (Q9) |
| BidX1 | https://bidx1.com | Online veilingplatform voor fondsen | Web | TECHNISCH ONDERZOEK NODIG | Status Spanje 2026 niet vastgesteld |
| Inmubi / Fencia / cristinamoriones.com / comprardeudahipotecaria.com | (zoekresultaten) | Tussenpersonen voor NPL's en *cesiones de remate* | Web | NIET GEBRUIKEN | Mandaat van een bank of servicer niet bevestigd |

---

## 10. Open vragen en ⏸️ ACTIE VOOR JAN

**⏸️ ACTIE VOOR JAN (maximaal drie):**
1. **Accounts en alerts:** wilt u zelf accounts aanmaken bij Servihabitat (particulier én professioneel, op naam van het bedrijf), Solvia, Diglo en Aliseda? Dan met zoekopdrachten voor Marina Alta, grond en woningen. Wij mogen geen accounts aanmaken; daarna richten we de verwerking van de alertmails in.
2. **Samenwerkend makelaar:** wilt u dat we onderzoeken, en na uw "ja" navragen, of TREE Properties *API colaborador* kan worden bij Servihabitat, Solvia of Aliseda voor Marina Alta? Dat hoort bij route D en levert vroege toegang op.
3. **Twee Jávea-percelen:** mogen R11/R15 ze identificeren (kadaster, register, stand van de UA) en mogen we de ficha-pdf's van Servihabitat downloaden? Er gaat niets naar de verkoper zonder uw akkoord.

**Open vragen (onderzoek):**
- Wie is eigenaar van perceel A en B (Sareb, Coral Homes of een ander)? Servihabitat gebruikt voor beide `productBrand 8003`, andere Marina Alta-percelen hebben 5000; de betekenis van die codes is ONBEKEND.
- Heeft Aliseda nu werkelijk grond in Jávea? De categoriepagina staat in de sitemap, maar een telling kon niet.
- Welk kanaal verkoopt BBVA-vastgoed in 2026, en is het contract van CaixaBank met Solvia (2023, 3 jaar + 18 mnd) verlengd?
- Afloop van het bezwaar tegen Sareb Lot A (Servihabitat of Hipoges) en de gevolgen voor de verkoop van Sareb-woningen in de Comunidad Valenciana.
- Hoe verhouden de doValue-SLA met Santander (dec 2025) en het Diglo-mandaat (apr 2026) zich tot elkaar?
- Is gepland of systematisch gebruik van de Idealista-assistent binnen de voorwaarden (gedeeld met R01)?
- Welke slug gebruikt Facilitea Casa voor Jávea/Xàbia, en is daar een filter op BuildingCenter?
- Tellingen voor Jávea bij Unicaja, Cimenta2, EscogeCasa, Bankinter, Altamira en Hipoges (alleen handmatig in een browser).

---

## 11. Geblokkeerd of mislukt

- **sareb.es** (FAQ, /en/inmuebles/, semestrale pdf): HTTP 403 via Imperva/Incapsula voor WebFetch en curl. Niet omzeild; Sareb-uitspraken uit zoekmachinesamenvattingen als "laag" gemarkeerd.
- **altamirainmuebles.com**: 403 voor WebFetch en curl zonder browser-UA. Niet omzeild.
- **bankinter.com** (vastgoedportaal): Cloudflare-controle ("Just a moment…"). Niet omzeild.
- **haya.es**: HTTP 522 (Cloudflare, oorsprong onbereikbaar).
- **alisedainmobiliaria.com, anticipa.com, realestate.hipoges.com, escogecasa.es, cimenta2.com/buscador-avanzado**: alleen JavaScript, dus geen tellingen. Geen browser-rendering gebruikt (conform opdracht).
- **unicajainmuebles.com**: zoekverzoek gaf twee keer /errorPublico.do; gestopt.
- **bbvavivienda.com**: TLS-certificaatfout (WebFetch) en HTTP/2-protocolfout (curl).
- **portalinmobiliario.ibercaja.es**: host bestaat niet meer (DNS).
- **ejeprime.com** en **eleconomista.es** (enkele artikelen): 403; alleen koppen gebruikt, als "laag" gemarkeerd.
- **Hipoges-sitemap**: activo_es_sitemap.xml leeg.
- **Idealista-assistent**: bij buurgemeenten plaatste de tool de zoekopdracht soms in een straat in Jávea (Q4, Q8); in één aanroep verviel het filter "de bancos" (Q9, ongeldig).
- **Solvia /suelos/alicante/denia, /pedreguer, /calpe, /ondara**: geen telling gevonden in de HTML, dus niet sluitend.
- **Facilitea Casa**: Jávea/Xàbia-slug gaf 0 terwijl Alicante 17.422 gaf; slug-normalisatie onbewezen.
- WebSearch werkte in deze ronde wel (geen budgetfout).

---

## 12. Bronnenlijst (controledatum 15-09-2026 tenzij anders vermeld)

| # | Bron | URL | Bewijstype |
|---|---|---|---|
| 1 | BOE: RD 1559/2012 (geconsolideerd, art. 16.3) | https://www.boe.es/buscar/act.php?id=BOE-A-2012-14118 | 2 |
| 2 | BOE: Orden PJC/784/2025 (criteria Sareb → SEPES/Casa 47) | https://www.boe.es/diario_boe/txt.php?id=BOE-A-2025-15292 | 2 |
| 3 | Casa 47: Traspaso Vivienda y Suelo | https://www.casa47.es/en/traspaso-vivienda-y-suelo | 2 |
| 4 | TED 140491-2026: Sareb, adviseur verkoop schuldportefeuilles | https://ted.europa.eu/es/notice/140491-2026/pdf | 2 |
| 5 | eldiario.es 29-05-2026: Servihabitat en Anticipa-Aliseda, Sareb-contract | https://www.eldiario.es/economia/servihabitat-anticipa-aliseda-llevan-ultimo-gran-contrato-sareb-174-millones-deshacerse-4-860-m_1_13260273.html | 1-pers |
| 6 | Brains RE News 12-08-2026: bezwaar Hipoges tegen Servihabitat | https://brainsre.news/disputa-hipoges-servihabitat-viviendas-sareb/ | 1-pers |
| 7 | Brains RE News 26-03/07-08-2026: kaart servicers | https://brainsre.news/servicers-inmobiliarios-espana/ | 1-pers (secundair) |
| 8 | ON ECONOMIA 03-08-2026: Hipoges en Finsolutia kopen Servihabitat | https://www.elnacional.cat/oneconomia/es/empresas/hipoges-finsolutia-compran-servihabitat-antiguo-servicer-caixabank_1676885_102.html | 1-pers |
| 9 | Servihabitat: homepage en lijstpagina's Alicante/Marina Alta | https://www.servihabitat.com/es/ ; https://www.servihabitat.com/es/venta/vivienda/alicante ; https://www.servihabitat.com/es/venta/terreno/alicante-marinaalta | 1/3 |
| 10 | Servihabitat: gebruiksvoorwaarden | https://www.servihabitat.com/es/terminos-generales-de-uso | 1 |
| 11 | Servihabitat: WOW Venta Especial | https://www.servihabitat.com/es/wowventasespeciales | 1 |
| 12 | Servihabitat Profesionales: portaal en Jávea-fiches | https://inversores.servihabitat.com/es/ ; https://inversores.servihabitat.com/es/venta/terreno/alicante-marinaalta ; https://inversores.servihabitat.com/es/venta/promociones/terreno-urbanonoconsolidado/alicante-marinaalta-balconalmarjavea/06124187 ; https://inversores.servihabitat.com/es/venta/promociones/terreno-urbanonoconsolidado/alicante-huertasur-xabia/06124173 | 1/3 |
| 13 | Servihabitat: Coral Homes, Green, Kutxabank | https://www.servihabitat.com/es/land/coralhomes ; https://www.servihabitat.com/es/land/green ; https://www.servihabitat.com/es/kutxabankinmobiliaria | 3 |
| 14 | Solvia: homepage, lijstpagina's, sitemap, aviso legal | https://www.solvia.es ; https://www.solvia.es/es/comprar/viviendas/alicante ; https://www.solvia.es/es/comprar/suelos/alicante ; https://www.solvia.es/sitemap.xml ; https://www.solvia.es/es/aviso-legal | 1/3 |
| 15 | idealista/news 16-12-2024: fusie Haya, Solvia, Aktua, HRE | https://www.idealista.com/news/inmobiliario/empresas/2024/12/16/824621-intrum-fusiona-sus-servicers-inmobiliarios-para-simplificar-su-estructura-en-espana | 1-pers |
| 16 | CaixaBank 25-05-2023: BuildingCenter kiest servicers | https://www.caixabank.com/en/headlines/news/buildingcenter-selects-the-new-servicing-providers-for-the-sale-maintenance-and-rental-management-of-caixabanks-real-estate-portfolio-for-the-forthcoming-three-years | 1 |
| 17 | Ibercaja 02-12-2025: alliantie met Intrum tot 2029 | https://www.ibercaja.com/detalle-sala-de-prensa/noticias/9885 | 1 |
| 18 | Ibercaja: portal inmobiliario → Solvia | https://www.ibercaja.es/particulares/portalinmobiliario/ | 1 |
| 19 | Intrum 04-12-2024: akkoord met BBVA (private banking) | https://www.intrum.es/empresas/sobre-intrum/comunicacion/noticias/intrum-firma-un-acuerdo-con-bbva-para-la-comercializacion-de-activos-inmobiliarios-dirigidos-a-banca-privada-y-altos-patrimonios/ | 1 |
| 20 | Diglo: homepage, lijstpagina's Alicante, Venta de Créditos, aviso legal | https://digloservicer.com/ ; https://digloservicer.com/venta-casas-pisos/cualquiera/alicante ; https://digloservicer.com/venta-locales/cualquiera/alicante ; https://digloservicer.com/oportunidades/venta-credito ; https://digloservicer.com/aviso-legal | 1/3 |
| 21 | idealista/news 08-04-2026: Diglo krijgt vastgoed en leningen van Santander | https://www.idealista.com/news/finanzas/economia/2026/04/08/892128-diglo-gestionara-la-venta-de-los-activos-inmobiliarios-de-banco-santander-y-la-mayoria | 1-pers |
| 22 | doValue España: zelfbeschrijving en portaal | https://dovalue.es/ | 1 |
| 23 | Stockopedia 03-12-2025: nieuwe SLA doValue en Santander | https://www.stockopedia.com/share-prices/do-value-s-p-a-BIT:DOV/news/brief-dovalue-signs-a-new-strategic-service-level-agreement-with-banco-santander-in-spain-019e69fa-df3c-7b63-9220-d5c576f187f1/ | 1-pers |
| 24 | Aliseda: robots.txt en sitemaps (categorieën, objecten, leningen) | https://www.alisedainmobiliaria.com/robots.txt ; https://www.alisedainmobiliaria.com/sitemap-category-aliseda-es-0.xml ; https://www.alisedainmobiliaria.com/sitemap-inmuebles-aliseda-es-0.xml ; https://www.alisedainmobiliaria.com/sitemap-loans.xml | 3 |
| 25 | Aliseda: NPL-sectie (paginatitel via zoekresultaat) | https://www.alisedainmobiliaria.com/inversion/prestamos-y-cesiones-remate/npls | 1 |
| 26 | El Español 13-06-2024: grondportefeuille Aliseda (Blackstone) | https://www.elespanol.com/invertia/observatorios/vivienda/20240613/cartera-suelos-servicer-blackstone-espana-aliseda-levanta-apetito-llega-millones/862414087_0.html | 1-pers |
| 27 | Hipoges: homepage en vastgoedportaal/sitemap | https://www.hipoges.com ; https://realestate.hipoges.com/es ; https://realestate.hipoges.com/activo_es_sitemap.xml | 1/3 |
| 28 | Estrategias de Inversión: Hipoges-portaal voor schuldbeleggers | https://www.estrategiasdeinversion.com/amp/hipoges-impulsa-su-portal-para-inversores-especializados-n-936995 | 1-pers (laag) |
| 29 | Facilitea Casa: homepage en lijstpagina Alicante/Jávea | https://www.faciliteacasa.com ; https://faciliteacasa.com/viviendas/comprar/Alicante | 3 |
| 30 | Unicaja Inmuebles | https://unicajainmuebles.com/ | 1/3 |
| 31 | Cajamar: portal de inmuebles → Cimenta2 | https://www.cajamar.es/es/comun/inmuebles/ ; https://cimenta2.com/ | 3 |
| 32 | EscogeCasa (Abanca) | https://www.escogecasa.es | 3 |
| 33 | Bankinter: vastgoedportaal (geblokkeerd) | https://www.bankinter.com/www/es-es/cgi/ebk+inm+home | 3 |
| 34 | Haya (522) | https://www.haya.es | 3 |
| 35 | Idealista-assistent: search_properties Q1–Q12 en property_detail 111869151 en 91172562 | https://www.idealista.com/es/venta-terrenos/javeaxabia-alicante/con-de-bancos/ ; https://www.idealista.com/es/venta-viviendas/javeaxabia-alicante/con-de-bancos/ ; https://www.idealista.com/es/venta-terrenos/alicante/marina-alta/con-de-bancos/ ; https://www.idealista.com/es/venta-viviendas/alicante/marina-alta/con-de-bancos/ (alle met utm-parameters zoals de tool ze gaf) | 3 |
| 36 | Eigen woningfeed Background Properties (alleen lezen) | http://127.0.0.1:3100/api/properties?town=Javea&limit=100 | 3 |
| 37 | El Español 28-08-2024: servicercontracten die aflopen (BBVA/Intrum) | https://www.elespanol.com/invertia/observatorios/vivienda/20240828/grandes-servicers-juegan-proximos-meses-contratos-activos/881412225_0.html | 1-pers (titel/samenvatting) |
| 38 | Infobae 27-01-2026: Diglo verkoopt 40 M€ aan dubieuze leningen | https://www.infobae.com/america/agencias/2026/01/27/diglo-banco-santander-pone-en-venta-40-millones-de-euros-de-prestamos-dudosos/ | 1-pers (titel) |
| 39 | Subastanomics: nieuwe NPL- en CDR-platforms na Auctree | https://subastanomics.com/nueva-via-tras-auctree-para-la-venta-de-npl-en-espana/ | 7 (blog, niet geverifieerd) |
| 40 | R08 (14-09-2026): 0 veilingen in Jávea en Dénia | /Users/root-admin/tree-es/deal-hunter/onderzoek/R08-veilingen-portalen-toegang.md | 3 (intern) |
| 41 | R01 en R15 (14-09-2026): 0 "de bancos"-woningen in Jávea | /Users/root-admin/tree-es/deal-hunter/onderzoek/R01-idealista.md ; R15-kandidaten-javea-live.md | 3 (intern) |

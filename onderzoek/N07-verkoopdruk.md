# N07 — Verkoopdruk: welke openbare signalen bestaan er, en wat mogen wij ermee

**Onderzoeksstroom:** N07 (verkoopdruk en bijzondere verkoopsituaties)
**Controledatum:** 18-09-2026. Alle metingen in dit rapport zijn van die dag, tenzij er een andere datum bij staat.
**Uitgevoerd door:** onderzoeksagent, TREE Deal Hunter
**Werkwijze:** wetteksten rechtstreeks uit de open-data-API van het BOE (`legislacion-consolidada`, XML, laatste geldende versie per artikel). Losse `curl`-verzoeken met een gewone browser-User-Agent, één tot drie per host, geen bulk. Elke `robots.txt` apart opgehaald vóór het lezen. De officiële Idealista-assistent voor twee zoekopdrachten. Onze eigen woningfeed op poort 3100 en onze eigen database alleen gelezen. Geen accounts aangemaakt, geen formulieren verstuurd, geen captcha opgelost, geen blokkade omzeild, geen namen van particulieren overgenomen.
**Bewijstypen (masterprompt §5):** 1 zelf getest of opgehaald · 2 officiële wettekst of planvoorschrift · 3 officiële kaart of database · 4 officiële publicatie van een overheid · 5 eigen afleiding of berekening · 6 bericht van een marktpartij · 7 onbekend of onbevestigd.

---

## Samenvatting (12 regels)

1. **Het beste signaal dat we hebben, hebben we al en gebruiken we niet.** De BP-feed levert bij elk object een datumveld. Over 224 objecten is de mediaan 127 dagen, het gemiddelde 223, de oudste 737. Tweeënveertig objecten staan er langer dan een jaar in, acht daarvan langer dan twee jaar. Dat is looptijd op de markt, gratis, uit een bron waar we al toestemming voor hebben (type 1).
2. **De tweede helft daarvan is prijshistorie, en die bouwen we nu pas op.** De tabel `snapshots` bewaart per ronde de prijs per object: 2.086 regels, 239 objecten met meer dan één meting, en tot nu toe één echte prijswijziging. Dat is geen tekortkoming van het ontwerp, alleen van de leeftijd — we meten pas sinds 15-09 (type 1).
3. **De officiële Idealista-assistent geeft prijsverlagingen rechtstreeks terug.** Bij elk object zit `priceDropInfo` met de vorige prijs, het bedrag en het percentage. Twee treffers in Jávea op 18-09: 643.000 → 595.000 € (−7 %) en 595.000 → 565.000 € (−5 %). De achterliggende zoekopdracht sorteert op `rebajas-desc`. Dit is de enige route naar portaalprijshistorie die wij mogen gebruiken (type 1).
4. **Erfenis en echtscheiding zijn in advertentieteksten niet te vinden. Gemeten, niet aangenomen.** In 2,38 miljoen tekens BP-feed: nul keer *herencia*, nul keer *heredero*, nul keer *proindiviso*, nul keer *divorcio*, nul keer *urge*. Bij Idealista gaf "venta por herencia" in Jávea nul resultaten, en ook nul in Alicante-stad — daar valt de vrije-tekstzoekfunctie zelf op door de mand, niet de markt (type 1).
5. **In het eigendomsregister staat het wél, en daar mogen we bij — per pand, niet per persoon.** Artikel 221 Ley Hipotecaria maakt het register openbaar voor wie een *interés conocido* heeft. Artikel 332.3 van het Reglamento Hipotecario vermoedt dat belang bij vastgoedprofessionals, mits je de reden van de opvraging noemt. Dat is de nota simple, het uittreksel per finca (type 2).
6. **Diezelfde artikelen zetten de grens waar wij niet overheen gaan.** Artikel 332.2 verbiedt letterlijk het opnemen van registergegevens *"in een database ter commercialisering of doorverkoop"*. En artikel 222.10 Ley Hipotecaria sluit telematische toegang tot de Índice de Personas zonder tussenkomst van een registrador uit. Zoeken op persoon kan dus niet, en een eigen registerdatabank mag niet (type 2).
7. **Het Catastro is voor eigendomsvragen dicht.** Artikel 51 van de kadasterwet noemt naam, bedrijfsnaam, identificatienummer, adres van de eigenaar én de kadastrale waarde uitdrukkelijk beschermde gegevens. Artikel 53 somt de uitzonderingen limitatief op. "Uitzoeken wie de eigenaar is om hem te benaderen" staat er niet bij (type 2).
8. **Voor vennootschappen in liquidatie is er één nieuw kanaal dat we misten: het Portal de Liquidaciones Concursales.** Daar publiceert de curator wat er te koop is, met filters op provincie én gemeente. De haak: op beide zoekformulieren van publicidadconcursal.es zit een captcha. Automatisch uitlezen zou die moeten omzeilen, en dat doen we niet. **Handmatig, en verder niets** (type 1).
9. **Executieveilingen bestaan hier nauwelijks.** De AEAT-lijst telt vandaag 269 onroerende kavels in heel Spanje, waarvan 6 in de provincie Alicante en **nul in Jávea, Benitachell, Teulada of Moraira**. Dichtstbijzijnde: Dénia, taxatie 40.945,66 €. Dat bevestigt R08 en R10 voor de derde keer (type 1).
10. **Er zit een fout in ons eigen systeem.** De AEAT-adapter leest elke ronde een bestand op `www2.agenciatributaria.gob.es`, en de robots.txt van die host zegt `Disallow: /`. De dataset mag hergebruikt worden, de host wil geen crawlers. Dat zijn twee verschillende dingen en wij hebben alleen naar het eerste gekeken. Voorstel in §12 (type 1).
11. **De Valenciaanse erfbelasting haalt de lucht uit het erfenisverhaal.** Sinds 28 mei 2023 geldt 99 % korting op de aanslag voor kinderen, ouders en echtgenoot. Wie erft in de eerste lijn hoeft niet te verkopen om de fiscus te betalen. Broers, neven en niet-verwanten vallen er wél buiten, en daar zit bij buitenlandse eigenaren een reëel deel van de gevallen (type 2/4).
12. **Advies: bouw het signaal dat van ons is, koop het signaal dat mag, en laat de rest handwerk.** Looptijd en prijsdaling uit eigen feed en snapshots automatiseren. Idealista handmatig via de assistent. Nota simple per dossier, pas ná selectie. Liquidaties, veilingen en gemeentelijke verkopen als linkjes op de telefoonpagina, niet als koppeling.

---

## 1. Conclusie voor Jan (besluitgericht)

**Conclusie.** Verkoopdruk is in Spanje wel degelijk openbaar zichtbaar, maar niet waar de meeste mensen hem zoeken. Niet in de advertentietekst — daar staat het simpelweg niet. Wel in drie dingen: **hoe lang iets al te koop staat**, **wat er in het eigendomsregister aan lasten op het pand staat**, en **wie de verkoper is: een curator, een bank, een gemeente**.

Van die drie hebben we de eerste al in huis en gebruiken we hem niet. Dat is de grootste winst van dit onderzoek, en hij kost niets.

De tweede, de nota simple, is het uittreksel uit het eigendomsregister. Daar staat op wie eigenaar is, hoe het pand is verkregen — koop, erfenis, toewijzing — en welke lasten erop rusten: hypotheek, beslag, vruchtgebruik. Voor jou als vastgoedprofessional wordt een legitiem belang vermoed, dus je kunt hem opvragen. Maar per pand, tegen betaling, en pas op het moment dat we een concreet dossier hebben. Niet vooraf en niet in bulk.

De derde is bladwerk: bekijken wie er verkoopt. Curatoren publiceren op het faillissementsregister, gemeenten op hun aanbestedingsprofiel, de Generalitat op haar eigen veilingpagina. Alle drie openbaar, alle drie klein in dit gebied, geen van drieën geschikt voor een koppeling.

En één ding moeten we hardop zeggen: **de klassieke "distressed seller"-jacht uit Angelsaksische vastgoedboeken kan hier niet.** Niet omdat het technisch moeilijk is, maar omdat het in Spanje bij wet is dichtgezet. Zoeken op persoon in het eigendomsregister mag niet zonder tussenkomst van een registrador. Eigendomsgegevens uit het Catastro zijn beschermd. Een eigen databank van registergegevens is uitdrukkelijk verboden. Wie een lijst maakt van "mensen in de problemen met een huis in Jávea" en die benadert, overtreedt vier regels tegelijk. Dat doen we dus niet, en we bouwen er ook geen gereedschap voor.

**Onderbouwing.**
- Eigen BP-feed, 224 objecten, 18-09-2026: datumveld bij alle 224, mediaan 127 dagen, maximum 737, 42 boven een jaar. In ons werkgebied 97 objecten, mediaan 127 dagen, 15 boven een jaar (type 1, §4).
- Eigen database `data/dealhunter.sqlite`, 18-09-2026: `snapshots` 2.086 regels, 239 objecten met meer dan één meting, 1 prijswijziging sinds 15-09 (type 1, §4).
- Idealista-assistent, 18-09-2026: veld `priceInfo.price.priceDropInfo` met `formerPrice`, `priceDropValue`, `priceDropPercentage`; 69 te renoveren woningen in Jávea, twee met prijsdaling (type 1, §4).
- Ley Hipotecaria art. 221 en 222, Reglamento Hipotecario art. 332 (type 2, §6 en §8).
- TRLCI art. 51 en 53 (type 2, §2).
- AEAT-veilinglijst `bienes.js`, 18-09-2026: 269 kavels, 6 in provincie Alicante, 0 in onze gemeenten (type 1, §9).
- Ley 6/2023 van de Comunitat Valenciana, 99 % korting erfbelasting groepen I en II vanaf 28-05-2023 (type 2, §6).

**Aannames.**
- Het datumveld in de BP-feed is naar alle waarschijnlijkheid de datum waarop het object bij Background Properties is aangemaakt, niet de eerste publicatiedatum bij de aanbiedende makelaar. Een pand kan dus al langer te koop staan dan wij zien. Als maat voor *relatieve* looptijd tussen objecten werkt het, als absolute leeftijd is het **[te verifiëren]** bij BP (type 5).
- Dat wij nul distress-woorden in de advertenties vinden, betekent dat de makelaars in dit segment ze niet opschrijven. Het betekent niet dat de situaties er niet zijn (type 5).
- Bij de Idealista-assistent tel ik wat de assistent teruggeeft, niet wat er op het portaal staat. De vrije-tekstzoekfunctie bleek trefwoorden in de omschrijving niet te doorzoeken; ik heb dat vastgesteld, niet opgelost (type 1).

**Tegenargumenten.**
- (a) **Lang te koop staan is net zo vaak een verkeerde prijs als verkoopdruk.** Een villa van 3,5 miljoen die 737 dagen staat, staat te duur. De eigenaar heeft geen haast; hij heeft een luchtkasteel. Het signaal is bruikbaar als *ingang voor een bod*, niet als bewijs van nood.
- (b) **Wie echt met spoed moet verkopen, zet zijn huis niet op een portaal.** Die belt de makelaar die hij kent, of een opkoper. Dan zie je het in geen enkele van deze bronnen, en is route R06/R07 — de makelaar met haast — de vindplaats.
- (c) **De erfbelastingkorting van 99 % ontmantelt het meest genoemde motief.** Wie in de eerste lijn erft, hoeft in de Comunitat Valenciana niet te verkopen om de belasting te betalen. Blijft over: de gemeentelijke plusvalía, en erfgenamen die ver weg wonen en een huis niet willen onderhouden. Dat is een andersoortige druk, en een zachtere.
- (d) **De veilingkant is hier drie keer onafhankelijk leeg gemeten.** R08 op 14-09, R10 op 15-09, B04 op 16-09, en vandaag opnieuw via de AEAT-lijst. Wie hier op executie wacht, wacht.

**Vervolgstap.** Zie §13. Kort: één bouwopdracht voor onszelf (looptijd en prijsdaling in de rapportage), één herstel (AEAT-adapter), één vraag aan BP (wat is dat datumveld), en vier handmatige links op de telefoonpagina.

---

## 2. De privacygrens — wat wij niet doen, ook al kan het

Dit hoofdstuk staat vooraan met opzet. Bij een onderwerp als dit is de verleiding het probleem, niet de onwetendheid.

### 2.1 Zeven dingen die technisch kunnen en die wij niet doen

| Nr | Wat technisch kan | Waarom wij het niet doen |
|---|---|---|
| V-1 | Een lijst maken van mensen met een beslag, een faillissement of een executie op hun naam | Verwerking van persoonsgegevens zonder grondslag. Artikel 332.2 Reglamento Hipotecario verbiedt bovendien uitdrukkelijk het opnemen van registergegevens in een databank. Het Registro Público Concursal beperkt gebruik van zijn gegevens tot de doelen van de faillissementswet |
| V-2 | In het Catastro opzoeken wie eigenaar is van een perceel dat ons bevalt | Naam, adres en identificatienummer van de eigenaar zijn beschermde gegevens (art. 51 TRLCI). De uitzonderingen in art. 53 dekken ons geval niet |
| V-3 | In het eigendomsregister zoeken op naam van een persoon of een vennootschap | Artikel 222.10 Ley Hipotecaria sluit rechtstreekse telematische toegang tot de Índice de Personas uit. Dat loopt altijd via een registrador, met opgaaf van reden |
| V-4 | De captcha op publicidadconcursal.es omzeilen en de liquidatielijst automatisch uitlezen | Een captcha is een beveiligingsmaatregel. Omzeilen is uitgesloten, ongeacht wat het oplevert |
| V-5 | Eigenaren van wie wij weten dat ze onder druk staan, ongevraagd benaderen | Massabenadering van particulieren is uitgesloten (masterprompt §4). Voor e-mail, WhatsApp en sms is voorafgaande toestemming nodig; ongevraagd bellen kan alleen op gedocumenteerd gerechtvaardigd belang, na controle van de Robinsonlijst (zie R16 §4) |
| V-6 | Een dossier bijhouden per persoon in plaats van per pand | Zodra wij gegevens over een persoon uit een register halen en bewaren, geldt artikel 14 AVG: die persoon moet binnen een maand horen dat wij zijn gegevens hebben. Wij willen dat niet en we hoeven het ook niet, want wij kopen panden, geen mensen |
| V-7 | Gerechtelijke edictos automatisch uitlezen uit het Tablón Edictal Judicial Único | De robots.txt van boe.es sluit `/edictos_judiciales/` en `/boe_j/` expliciet uit. En de inhoud is precies waar het misgaat: namen van schuldenaren |

### 2.2 De enige vorm die wél mag

Objectgericht. Wij bewaren: het pand, de prijs, de vraag hoe lang het al te koop staat, de kadastrale referentie, de lasten die op de finca rusten, en onze eigen beoordeling. Wij bewaren niet: wie de eigenaar is, waarom hij verkoopt, of er een scheiding speelt, of hij schulden heeft.

De praktische toets is simpel. **Kun je de regel in de database aan de betrokkene laten zien zonder je te schamen?** Staat er "villa X, 620 dagen te koop, twee keer verlaagd, hypotheek van Sabadell op de finca", dan kan dat. Staat er "eigenaar in scheiding, heeft geld nodig", dan niet.

### 2.3 Waarom "het is toch openbaar" geen argument is

Drie bronnen in dit rapport zijn openbaar en toch beperkt in gebruik, elk om een andere reden:

- **Het Registro Público Concursal** is vrij toegankelijk zonder belang aan te tonen, maar het gebruik van de gegevens is beperkt tot de doelen van de faillissementswetgeving (aviso legal, 18-09-2026). Openbaar betekent hier: je mag kijken, niet: je mag er een product van maken.
- **Het eigendomsregister** is openbaar voor wie belang heeft, maar de wet verbiedt in dezelfde adem het bouwen van een databank (art. 332.2 RH).
- **Het Tablón Edictal Judicial Único** is vrij toegankelijk voor vier maanden, maar de site vraagt crawlers weg te blijven en de inhoud bestaat uit namen van gedaagden.

Openbaarheid is in Spanje bijna altijd *doelgebonden*. De vraag is nooit alleen "mag ik dit zien", maar "mag ik dit zien hiervóór".

---

## 3. De zeven signalen in één tabel

| # | Signaal | Beste bron | Openbaar | Automatisch lezen | AVG-grens | Bruikbaar voor ons |
|---|---|---|---|---|---|---|
| 1 | Lang te koop, prijsverlaging | Eigen BP-feed + eigen `snapshots`; Idealista-assistent | Eigen data | **Ja, eigen bron** | Geen persoonsgegevens in het spel | **Hoog — meteen** |
| 2 | Erfenis, nalatenschap | Nota simple per finca; advertentietekst | Register: voor wie belang heeft | Nee, per dossier | Titularis is persoonsgegeven; niet bewaren | Middel — per dossier |
| 3 | Echtscheiding, verdeling | Nota simple (proindiviso); gerechtelijke verkoop | Deels | Nee | Zwaarste categorie in dit rapport | **Laag — niet actief zoeken** |
| 4 | Vennootschap in liquidatie of faillissement | BORME (draait al) + Portal de Liquidaciones Concursales | Ja | BORME ja, liquidatieportaal **nee (captcha)** | Rechtspersoon is geen persoonsgegeven; bestuurders wél | Middel — half gebouwd |
| 5 | Beslag, hypotheekachterstand, executie | Nota simple (cargas); AEAT-lijst; BOE-veilingportaal | Ja | AEAT **robots verbiedt het**; BOE-portaal `Disallow: /` | Namen van schuldenaren nooit opslaan | Laag hier — markt is leeg |
| 6 | Bank- en servicervastgoed | Aliseda-sitemap, Servihabitat, Solvia, Diglo | Ja | Alleen sitemaps; pagina's zijn JavaScript | Zakelijke tegenpartij | Laag — 0 woningen in Jávea |
| 7 | Verkoop door gemeente of Generalitat | PLACSP (open data), GVA-veilingpagina, DOGV-alerts, BOP Alicante | Ja | PLACSP ja; GVA en DOGV ja; BOP nee | Geen | Middel — traag maar schoon |

---

## 4. Signaal 1 — Lang te koop staan en herhaalde prijsverlagingen

De opdracht vraagt expliciet: hoe meet je dit **zonder portalen te scrapen**. Er zijn drie antwoorden en ze zijn alle drie beschikbaar.

### 4.1 Het datumveld in onze eigen feed

De BP-feed geeft per object een veld `date`. Ik heb alle drie de pagina's opgehaald (224 objecten, 18-09-2026) en de leeftijd uitgerekend ten opzichte van vandaag.

| Maat | Hele feed (224) | Ons werkgebied (97) |
|---|---|---|
| Kortste | 2 dagen | — |
| Mediaan | 127 dagen | 127 dagen |
| Gemiddeld | 223 dagen | — |
| Langste | 737 dagen | 737 dagen |
| Langer dan 1 jaar | 42 objecten | 15 objecten |
| Langer dan 2 jaar | 8 objecten | — |

Verdeling over de hele feed: 57 objecten tot 90 dagen, 75 tussen 90 en 180, 50 tussen 180 en 365, 34 tussen een en twee jaar, en 8 boven de twee jaar.

De vier oudste, alle met datum 737 dagen geleden: Altea 3.500.000 €, La Nucia 2.500.000 €, **Jávea 3.589.000 €** (ref. 6303JAV), Calpe 2.450.000 €. Daarna Benitachell 2.720.000 € op 700 dagen (ref. 6232BELL).

Let op wat daar staat. De langstlopende objecten zijn de **duurste**. Dat onderstreept tegenargument (a): looptijd meet in dit segment vooral een prijs die de markt niet volgt. Het blijft een goede ingang voor een gesprek, maar noem het geen nood.

**Wat dit waard is.** Nul euro extra, nul juridisch risico, en het staat al in huis. Onze rapportage gebruikt dit veld vandaag nergens: het dashboard en de telefoonpagina sorteren op `first_seen_at`, de dag waarop *wij* het object voor het eerst zagen. Dat is voor bijna alles 15-09, dus die sortering zegt niets. Het veld `source_date` staat wel in de database bij alle 225 BP-objecten, en wordt door geen enkel scherm gelezen (gecontroleerd in `dh/summary.py`, `dh/report.py`, `dh/dashboard.py` en de twee javascriptbestanden). Dat is de duidelijkste bouwopdracht uit dit hele rapport.

**Voorbehoud.** Of `date` de eerste publicatiedatum is of de aanmaakdatum in het CRM van Background Properties is niet vastgesteld — **[te verifiëren]**, één vraag aan BP.

### 4.2 Onze eigen prijshistorie

De tabel `snapshots` legt per ronde vast wat een object kost. Stand 18-09-2026: 2.086 regels, 239 objecten met meer dan één meting, en één object waarbij de prijs daadwerkelijk is veranderd. Het gebeurtenissenlogboek noteert dat als `PRIJS GEWIJZIGD`.

Dat lijkt mager en dat is het ook, maar de reden is banaal: we meten sinds 15-09, dus drie dagen. De machinerie werkt, hij heeft alleen nog geen tijd gehad. Over drie maanden is dit het scherpste signaal dat we bezitten, en het is volledig van onszelf — geen portaalvoorwaarde raakt eraan.

**Wat er nog moet gebeuren.** Twee dingen. Bewaar per object de eerste gemeten prijs, zodat "totale daling sinds wij kijken" in één blik te zien is. En trek een grens waarboven een daling een melding waard is; nu bestaan er meldingen op haalbaarheid, niet op prijsbeweging (`dh/alerts.py`).

### 4.3 De officiële Idealista-assistent

Dit is de enige route naar portaalprijshistorie die wij mogen gebruiken. Scrapen van Idealista is verboden door de voorwaarden en door het databankrecht (R16 §1 en §2). De assistent is een officiële koppeling van Idealista zelf.

Gemeten op 18-09-2026, zoekopdracht "huizen te koop in Jávea met prijsverlaging, opknapper": 69 resultaten in de categorie "Usada / para reformar". De assistent geeft per object een blok terug:

```
"priceInfo": { "price": { "amount": 595000, "currencySuffix": "€",
  "priceDropInfo": { "formerPrice": 643000, "priceDropValue": 48000,
                     "priceDropPercentage": 7 } } }
```

Twee treffers met een daling:

| Object | Was | Nu | Daling | Wijk |
|---|---|---|---|---|
| 110934596, finca rústica, 238 m² | 643.000 € | 595.000 € | −48.000 € (−7 %) | Puerto, Montgó |
| 110273579, vrijstaand, 120 m² op 1.050 m² | 595.000 € | 565.000 € | −30.000 € (−5 %) | Montgó–Ermita |

De onderliggende zoekopdracht die de assistent teruggeeft eindigt op `?ordenado-por=rebajas-desc`. Idealista heeft dus een eigen sortering op prijsverlaging, en die is via de assistent te bereiken.

**De grens.** De assistent geeft ook telefoonnummers terug van de aanbiedende kantoren (`userType: professional`). Dat zijn zakelijke contactgegevens, maar ze horen niet in onze database. Wij bewaren van een Idealista-resultaat alleen: portaal-ID, link, prijs, oppervlakte, wijk, en de prijsdaling. Verder niets. Dat is ook wat R16 §1 voorschrijft.

**Handmatig blijft handmatig.** De assistent werkt binnen een Claude-sessie. Hem in een nachtelijke ronde aanroepen is een ander gebruik dan waarvoor hij bedoeld is. De aanvraag voor de Search API loopt al (TODO, `acties/2026-09-15-idealista-search-api-aanvraag.md`); tot die er is, is dit een wekelijkse handeling, geen koppeling.

### 4.4 Wat we bewust niet doen

Prijshistorie kopen bij een dataleverancier is een optie die R04 al beschreef, maar de dekking van Jávea is bij alle partijen mager en de prijs hoog. Zolang onze eigen snapshots aangroeien, is dat geld dat we niet uitgeven.

---

## 5. Signaal 2 — Erfenis en nalatenschap

### 5.1 De advertentietekst: gemeten, en het werkt niet

De gedachte is aantrekkelijk: makelaars schrijven "venta por herencia" in de tekst, dus zoek op dat woord. Ik heb het op twee onafhankelijke manieren gemeten en het klopt hier niet.

**Onze eigen feed**, 224 objecten, 2.376.843 tekens aan omschrijving en kenmerken (18-09-2026):

| Term | Treffers |
|---|---|
| herencia / heredero | 0 |
| proindiviso | 0 |
| urge / urgente / motivated seller | 0 |
| divorcio / divorce | 0 |
| rebajado / reduced price | 1 |
| banco / embargo / subasta | 3 |

**De Idealista-assistent**, 18-09-2026: "venta por herencia en Jávea Xàbia, vivienda de herederos" gaf nul resultaten. Ter controle dezelfde vraag voor Alicante-stad, waar zulke advertenties zeker bestaan: ook nul. Daarmee weet ik genoeg — de vrije-tekstzoekfunctie van de assistent doorzoekt de omschrijvingen niet op trefwoord. Dat is een beperking van het gereedschap, geen uitspraak over de markt.

**Conclusie:** op de advertentietekst valt in ons segment geen erfenissignaal te bouwen. De Jávea-markt is buitenlandse villa's, verkocht door kantoren die in nette marketingtaal schrijven. Die zetten dit er niet in. Het kan wél lonen in het centrum van Jávea, bij Spaanse dorpswoningen, en dan zie je het bij het bezichtigen — niet in een bestand.

### 5.2 Het eigendomsregister: daar staat het wel

De nota simple, het uittreksel uit het eigendomsregister, laat per finca zien wie de ingeschreven eigenaar is en **hoe hij eigenaar is geworden**. Staat daar een *adjudicación hereditaria* of een *aceptación de herencia*, dan is het pand vererfd. Zijn er drie of vier eigenaren met elk een breukdeel, dan is het een *proindiviso* — mede-eigendom — en dat is in de praktijk de meest voorkomende vorm van vastgelopen erfenis.

Artikel 222.5 Ley Hipotecaria schrijft voor wat er minimaal in staat: de identificatie van de finca, *"la identidad del titular o titulares de derechos inscritos"* en de omvang, aard en beperkingen daarvan, plus alle verboden of beperkingen die op de eigenaren of de rechten rusten.

**Mag jij die opvragen?** Ja, met een reden. Artikel 221 maakt het register openbaar voor wie *"interés conocido"* heeft. Artikel 332.3 van het Reglamento Hipotecario zegt daarbij letterlijk dat het belang wordt vermoed bij wie een beroeps- of bedrijfsmatige activiteit uitoefent die met het rechtsverkeer in onroerend goed te maken heeft, waarbij *"agentes de la propiedad inmobiliaria y demás profesionales que desempeñen actividades similares"* met zoveel woorden genoemd worden — mits de aanvrager *"expresen la causa de la consulta"* en die reden past bij het doel van het register.

Kosten: het basisarancel is 3,005061 € per finca (R11 §6); de onlineprijs met toeslagen is **[te verifiëren]**. Levering telematisch, circa 24 uur.

### 5.3 Waarom het motief zwakker is dan gedacht

De standaardredenering luidt: erfgenamen moeten binnen zes maanden erfbelasting betalen, dus ze moeten snel verkopen. In de Comunitat Valenciana klopt dat sinds twee jaar niet meer voor de belangrijkste groep.

Ley 6/2023 van 22 november van de Generalitat, die Ley 13/1997 wijzigt, voert een korting van **99 % op de aanslag** in voor verkrijgingen bij overlijden door verwanten van groep I en II — kinderen, kleinkinderen, ouders, grootouders en de echtgenoot — met terugwerkende kracht tot 28 mei 2023.

Wat blijft er dan over aan druk?

- **Groep III en IV vallen erbuiten:** broers en zussen, neven en nichten, en niet-verwanten. Bij buitenlandse eigenaren zonder kinderen in de buurt is dat geen uitzondering.
- **De plusvalía municipal blijft.** Die is gemeentelijk, staat los van de erfbelasting, en heeft een eigen termijn van zes maanden na overlijden, met zes maanden verlenging op verzoek. Veel gemeenten kennen kortingen van 50 tot 95 % voor de eerste woning van directe familie, maar niet voor een tweede woning aan de kust.
- **Onderhoud en afstand.** Erfgenamen in Manchester of Düsseldorf met een villa in het Montgó betalen IBI, verzekering, tuin en zwembad voor een huis dat leegstaat. Dat is een reële, en meestal geduldige, druk.

De zuivere fiscale klok is dus grotendeels weg. Wat overblijft is traag en menselijk, en dat past bij hoe wij willen kopen.

### 5.4 Werkwijze die binnen de regels blijft

1. Selecteer op looptijd en prijsdaling (§4). Erfenis is geen zoekingang.
2. Valt een object op, vraag de kadastrale referentie op (die halen we al automatisch bij het Catastro via `Consulta_RCCOOR_Distancia`, één verzoek per seconde, gecachet).
3. **Pas dan** één nota simple, met de reden "beoordeling van een mogelijke aankoop". Dat is een legitieme reden en het is ook de waarheid.
4. Wat we uit de nota simple **in het dossier zetten:** de lasten, de oppervlakte, het aantal ingeschreven rechthebbenden, en of het pand een *proindiviso* is. **Wat niet:** namen, adressen, identificatienummers, burgerlijke staat.
5. Onderhandelen doet de advocaat of de makelaar, met de erfgenamen, via het kantoor dat het pand aanbiedt. Wij benaderen geen erfgenamen rechtstreeks.

---

## 6. Signaal 3 — Echtscheiding en verdeling

Dit is het gevoeligste punt in dit rapport, en het kortste. Niet omdat er weinig over te zeggen valt, maar omdat het antwoord bijna overal "nee" is.

### 6.1 Wat er juridisch gebeurt

Als twee mensen samen een huis bezitten en niet meer samen verder willen, loopt dat via de *división de cosa común*. Artikel 400 van het Burgerlijk Wetboek: *"Ningún copropietario estará obligado a permanecer en la comunidad"* — niemand hoeft in een mede-eigendom te blijven. Artikel 404: is de zaak in wezen ondeelbaar en willen de mede-eigenaren hem niet aan één van hen toewijzen met vergoeding aan de anderen, dan wordt hij verkocht en de opbrengst verdeeld.

Bij een erfenis geldt hetzelfde via artikel 1062: één erfgenaam die om openbare verkoop vraagt, is genoeg om die af te dwingen, *"con admisión de licitadores extraños"* — met toelating van buitenstaanders.

Dat is precies het moment waarop een pand onder de marktprijs kan wisselen: bij een gerechtelijke verkoop na een mislukte verdeling. Het is ook precies het moment waarop het een executieveiling wordt, en daarmee valt het onder signaal 5.

### 6.2 Wat je zou kunnen zien, en waarom je er niet naar zoekt

In de nota simple is een verdeling zichtbaar als meerdere eigenaren met een breukdeel. De burgerlijke staat van de eigenaar staat er traditioneel ook in — *casado en régimen de gananciales*, gehuwd in gemeenschap. Een gerechtelijke verkoop verschijnt in het Tablón Edictal Judicial Único en in het BOE-veilingportaal, met de naam van de gedaagde.

Alle drie die routes leveren persoonsgegevens over de privésituatie van iemand. Geen bijzondere categorie in de zin van artikel 9 AVG, maar wel gegevens waar niemand een vreemde in wil zien snuffelen.

**Wat wij doen:** niets actiefs. Wij zoeken niet op scheiding, wij leiden geen scheiding af uit een eigendomsverdeling, en wij noteren nergens dat wij dat vermoeden.

**Wat wél mag en verstandig is:** als een pand ons om andere redenen bevalt en de nota simple laat vier eigenaren met breukdelen zien, dan is dat een **onderhandelingsfeit**, geen persoonsfeit. Het betekent: er moeten vier handtekeningen komen, dat duurt langer, en de advocaat moet vooraf checken of ze het eens zijn. Dat noteren we — als eigenschap van het pand.

**Wat nooit:** contact met één van de mede-eigenaren buiten het aanbiedende kantoor om, met het idee er tussen te komen. Dat is niet alleen juridisch onverstandig, het is de snelste manier om in Jávea je naam kwijt te raken.

### 6.3 De grens hardop

Er bestaan bedrijven die precies dit doen: breukdelen van mede-eigenaren opkopen bij scheidingen en vastgelopen erfenissen, om daarna de verdeling af te dwingen. Het is legaal. Het is geen TREE. Als Jan die route ooit wil overwegen, is dat een aparte beslissing met een advocaat erbij, niet iets wat uit dit systeem mag rollen.

---

## 7. Signaal 4 — Vennootschappen in liquidatie of faillissement

Hier ligt de meeste nieuwe winst, en één harde grens.

### 7.1 Wat al draait: de BORME

Sinds vandaag, 18-09-2026, leest de adapter `dh/adapters/borme.py` elke ronde de sumario-API van het handelsblad plus het provincie-item voor Alicante. Dat item heeft gestructureerde XML, dus er komt geen PDF-ontleding aan te pas.

Opgeslagen worden **alleen**: rechtspersoon, registernummer, handeling, sector en datum. Nooit de aankondigingstekst, want daarin staan bestuurders en vereffenaars bij naam. Dat is een bewuste keuze en hij moet zo blijven.

De eerste ronde leverde zeven signalen, waarvan twee in vastgoed of bouw:

| Vennootschap | Handeling | Sector | Gepubliceerd |
|---|---|---|---|
| GESTIO INMOBILIARIA LA FOIA SL | ontbinding, liquidatie, opheffing | vastgoed of bouw | 09-09-2026 |
| INMOBILIARIA GARCIA HUERTAS SL | kapitaalvermindering | vastgoed of bouw | 09-09-2026 |
| RODMES BOCH-CREVILLENTE SL EN LIQUIDACION | ontbinding, liquidatie | — | 09-09-2026 |
| ECOATLAS FOOD AND NUTRITION SL | ontbinding, liquidatie, opheffing | — | 09-09-2026 |
| MULLIGAN EUROPE SL | ontbinding, liquidatie, opheffing | — | 09-09-2026 |
| ESPACIO ARTE Y VOLUMEN SL | ontbinding, opheffing | — | 10-09-2026 |
| PROSEBA HOLDING COMPANY SL | ontbinding, liquidatie, opheffing | — | 10-09-2026 |

### 7.2 Het gat: van vennootschap naar haar onroerend goed

Dit is de vraag die de opdracht stelt, en het eerlijke antwoord is: **die stap is in Spanje met opzet lastig gemaakt.**

Er bestaat een centrale index waarmee het zou kunnen. Artikel 332.9 van het Reglamento Hipotecario noemt de *Índice General Informatizado de fincas y derechos*, waar alle registradores rechtstreeks op zijn aangesloten, *"dejando constancia en sus archivos de la identidad del solicitante y del motivo de la solicitud"* — met vastlegging van wie het vroeg en waarom.

Maar artikel 222.10 Ley Hipotecaria sluit de achterdeur: zelfs een ambtenaar die uit hoofde van zijn functie toegang heeft, *"no podrá acceder telemáticamente sin intermediación del registrador al Índice de Personas."* Voor ons betekent dat: zoeken op naam van een vennootschap kan alleen via een registrador, met opgaaf van reden, en de opvraging wordt vastgelegd.

**Onze werkwijze, als een BORME-signaal er echt toe doet:** de advocaat vraagt bij de registrador een *certificación* of nota naar de goederen van die vennootschap, met als reden een concrete koopbelangstelling. Dat is een handeling van een professional met een dossier, geen achtergrondcontrole. Wij bouwen daar geen gereedschap voor en wij doen het niet standaard.

En de rem daarop: artikel 332.2 RH verbiedt *"su incorporación a base de datos para su comercialización o reventa"*. De uitkomst gaat dus in het dossier van dat ene object en niet in onze database.

### 7.3 Nieuw gevonden: het Portal de Liquidaciones Concursales

Dit stond nog niet in ons register en het is de belangrijkste vondst van deze ronde.

Op `https://www.publicidadconcursal.es/liquidaciones` publiceert het faillissementsregister wat er bij vennootschappen in liquidatie te koop staat. De curator moet die informatie aanleveren; de koopmogelijkheid verschijnt op dezelfde dag als de faillissementsverklaring en verdwijnt automatisch na twee jaar. De grondslag zit in de zesde aanvullende bepaling bij de faillissementswet, ingevoerd door Ley 16/2022.

Het zoekformulier heeft precies de velden die wij willen (zelf vastgesteld, 18-09-2026, type 1):

- procedurevorm, met zeven varianten, waaronder verkoop van productie-eenheden in de liquidatiefase (art. 415 bis TRLC) en buitengerechtelijke verkoop;
- verkoopwijze: onderhandse verkoop, veiling, of anders;
- bedrijfsnaam, NIF en CNAE-sector;
- **provincie en gemeente**, zowel van de statutaire zetel als van de hoofdvestiging.

**En dan de streep.** Op het formulier zitten drie captchavelden: `captcha`, `captchaRange`, `captchaAnswer`. Hetzelfde geldt voor het gewone zoekscherm van het register. De robots.txt van de site staat alles toe (`Disallow:` leeg, met een sitemap), maar de captcha zegt in de praktijk iets anders, en de aviso legal beperkt het gebruik tot huishoudelijk gebruik en verbiedt reproductie of verspreiding zonder schriftelijke toestemming van CORPME.

**Oordeel: ALLEEN HANDMATIG.** Een link op de telefoonpagina onder Veilingen, naast de publicatieborden. Eén keer per maand doorkijken op provincie Alicante kost vijf minuten.

### 7.4 Wat dit realistisch oplevert

Een bouwbedrijf in liquidatie bezit soms percelen, soms halfafgebouwde projecten, soms alleen busjes en steigers. De BORME zegt niet welke. De liquidatieportaal-vermelding gaat bovendien meestal over een *unidad productiva*, een draaiend bedrijfsonderdeel, en niet over één los perceel.

Dus: dit is een **waarschuwingskanaal**, geen zoekkanaal. Het zegt ons weken tot maanden vóór de markt dat er iets los gaat komen in de buurt. Wat er precies loskomt, moet een mens uitzoeken.

---

## 8. Signaal 5 — Beslag, hypotheekachterstand en executie

### 8.1 De nota simple is hier het enige echte gereedschap

Een *embargo* — beslag — en een hypotheekachterstand die tot executie leidt, staan als *carga* in het eigendomsregister. Artikel 222.5 Ley Hipotecaria verplicht de registrador om in de nota simple *"en todo caso"* alle verboden en beperkingen te vermelden die op de eigenaren of de ingeschreven rechten rusten.

Dat is direct praktisch. Staat er een hypotheek van 380.000 € op een pand dat voor 420.000 € te koop staat, dan weet je meteen twee dingen: er is weinig ruimte, en de bank zit mee aan tafel. Staat er een beslag van de belastingdienst bij, dan verandert de hele onderhandeling.

Artikel 332.5 RH voegt daar iets bruikbaars aan toe: het legitieme belang wordt *vermoed* wanneer de informatie wordt gevraagd met het oog op belastingen, **vastgoedwaarderingen**, of het verstrekken van hypothecaire leningen. Een taxatie voor een aankoopbeslissing valt daar netjes onder.

### 8.2 De veilingkanalen, en hoe leeg ze zijn

**De AEAT-lijst** (belastingdienst) staat al in onze monitor. Gemeten op 18-09-2026: 269 onroerende kavels in heel Spanje, waarvan 6 in de provincie Alicante en **nul in Jávea, Benitachell, Teulada of Moraira**.

| Plaats | Taxatie | Overblijvende lasten | Einde veiling |
|---|---|---|---|
| Orihuela | 109.299,65 € | 16.191,27 € | 21-09-2026 |
| **Dénia** | 40.945,66 € | 0 € | 21-09-2026 |
| San Juan de Alicante | 75.488,81 € | 61.738,16 € | 05-10-2026 |
| Muro de Alcoy | 71.652,53 € | 63.083,86 € | 05-10-2026 |
| Torrevieja | 60.047,73 € | 0 € | 28-09-2026 |
| Alicante stad | 164.593,94 € | 79.730,61 € | 05-10-2026 |

Let op de kolom lasten. Bij San Juan en Muro de Alcoy is de overblijvende last 82 respectievelijk 88 procent van de taxatie. Dat is precies de valkuil uit masterprompt §18: veilingwaarde is geen marktwaarde, en eerdere lasten kunnen blijven bestaan.

**Het BOE-veilingportaal** (`subastas.boe.es`) is de hoofdbron voor gerechtelijke veilingen. De robots.txt luidt `User-agent: *` / `Disallow: /` — alles dicht. Handmatig raadplegen mag, automatisch lezen niet. Dat bevestigt R16 §1.

**Het Tablón Edictal Judicial Único** op `boe.es/edictos_judiciales` bundelt sinds 1 juni 2021 alle gerechtelijke bekendmakingen die vroeger op losse prikborden hingen. Vier maanden vrij toegankelijk, daarna alleen met verificatiecode. Zoeken kan op vrije tekst en rechtsgebied, **niet op provincie of gemeente** — voor ons dus slecht bruikbaar. En de robots.txt van boe.es sluit zowel `/edictos_judiciales/` als `/boe_j/` uit. Handmatig, incidenteel, meer niet.

### 8.3 Een fout in ons eigen systeem

Onze AEAT-adapter haalt elke ronde `https://www2.agenciatributaria.gob.es/static_files/.../bienes.js` op. De robots.txt van die host is:

```
User-agent: *
Disallow: /robots.txt
Disallow: /
```

Alles dicht, dus. De adapter vermeldt terecht dat de dataset onder CC BY 4.0 valt met verplichte bronvermelding, maar dat gaat over het **hergebruik van de gegevens**, niet over het **ophalen bij deze host**. Wij hebben die twee door elkaar gehaald.

Ter vergelijking: `sede.agenciatributaria.gob.es` en `www.agenciatributaria.es` hebben een genuanceerde robots.txt die alleen bepaalde mappen sluit. Alleen `www2` staat volledig dicht.

**Voorstel.** Zet de adapter stil tot dit is uitgezocht. Kijk of dezelfde lijst via een toegestaan pad te krijgen is, of via het open-dataportaal `datos.gob.es`. Lukt dat niet, dan wordt de AEAT-lijst een handmatige link, net als de publicatieborden. Gezien de uitkomst — al maanden nul kavels in onze gemeenten — kost dat ons vrijwel niets. Zie §13.

---

## 9. Signaal 6 — Vastgoed van banken en servicers in de Marina Alta

Dit is in R10 (15-09) en B04 (16-09) uitgezocht. Ik heb één ding opnieuw gemeten en verder niets, om geen oude tellingen als nieuw te presenteren.

**De stand uit R10, 15-09-2026:** nul bankwoningen in Jávea bij Idealista, Servihabitat en Diglo. Solvia heeft geen Jávea-pagina. In de hele Marina Alta één bankwoning (Calp) en twintig bankpercelen. Servihabitat Profesionales had één perceel in Balcón al Mar, 20 % in prijs gezakt van 904.000 naar 725.000 €.

**Wie er actief is:** Aliseda-Anticipa, Servihabitat, Hipoges, Diglo en Solvia. Haya bestaat niet meer als apart merk (opgegaan in Solvia onder Intrum) en Anida evenmin. Sareb wordt afgebouwd; meer dan 40.000 woningen gaan naar de staatswoningbouwer Casa 47.

**Vandaag opnieuw gemeten** (type 1): de sitemap `sitemap-investors.xml` van Aliseda telt 3.639 URL's en bevat nog steeds eigen landpagina's voor **Jávea/Xàbia** — alles, stedelijke grond én finca rústica — en voor **Teulada**, waaronder te ontwikkelen grond. In drie talen. Benitachell komt niet voor. De onderliggende pagina's zijn JavaScript en leveren zonder browser niets.

**Hoe zij aanbieden.** Geen van deze partijen heeft een openbare lees-API of feed. Wel e-mailmeldingen en opgeslagen zoekopdrachten, maar alleen met een account. De voorwaarden van Servihabitat, Solvia en Diglo verbieden commerciële exploitatie en extractie zonder toestemming. Servicers bieden bovendien een deel van hun voorraad eerst aan hun eigen samenwerkende makelaars aan — dat zie je op geen enkel portaal.

**Werkwijze.** Accounts met gebiedsmeldingen zet Jan zelf op; dat is voor een mens toegestaan en voor een robot niet. De Aliseda-sitemap mogen wij wekelijks ophalen als kompas — hij staat in hun eigen robots.txt genoemd, wat een uitnodiging is om hem te lezen. Wat erin staat zegt alleen *dat* er iets ligt en *waar*, niet wat of voor hoeveel. De gebruiksvoorwaarden van Aliseda zijn onbekend, want ook de aviso legal is zonder JavaScript niet te lezen. Dus: signaleren mag, de pagina openen doet Jan.

**Eerlijke waardering:** dit kanaal levert in Jávea vandaag geen woningen. Het levert grond, en die grond is professioneel, vaak nog niet geconsolideerd, en met stedenbouwkundige voorwaarden. Dat is route B, niet route A.

---

## 10. Signaal 7 — Verkoop door de gemeente of de Generalitat

Het schoonste signaal in dit rapport. Geen persoonsgegevens, geen omstreden voorwaarden, alles openbaar. Alleen traag en zeldzaam.

### 10.1 De gemeente

Als een gemeente een perceel of pand van haar patrimonium verkoopt, gebeurt dat in beginsel via openbare veiling. Artikel 112.1 van het Reglamento de Bienes de las Entidades Locales bepaalt dat de voorbereiding en gunning van zulke verkopen de regels voor gemeentelijke aanbestedingen volgen. Artikel 118 voegt toe dat er vooraf een technische waardering moet liggen die de reële waarde vaststelt — die taxatie zit dus in het dossier.

De verkoop zelf valt buiten de aanbestedingswet. Artikel 9.2 van Ley 9/2017 sluit koop, schenking, ruil en verhuur van onroerend goed uitdrukkelijk uit; die worden geregeerd door het vermogensrecht. Toch verschijnt de aankondiging in de praktijk op het *perfil del contratante*, het aanbestedingsprofiel, omdat artikel 112.1 RBEL naar diezelfde regels verwijst.

**Waar dat te vinden is.** Het aanbestedingsprofiel van Xàbia is aangesloten op de Plataforma de Contratación del Sector Público. Die heeft echte open data: ATOM-sindicatie, dagelijks en maandelijks, plus ZIP-bestanden per jaar en per maand, volgens het patroon `…/sindicacion/sindicacion_1044/PlataformasAgregadasSinMenores_AAAAMM.zip`. Formaat is ATOM 1.0 met CODICE-specificaties.

Daarnaast is er het **BOP Alicante**, het provinciale publicatieblad. Dat weigert crawlers (vastgesteld 18-09, zie TODO en registerregels R2-42, R2-76, R2-77). Handmatige link dus.

### 10.2 De Generalitat

De Conselleria de Hacienda verkoopt via de Dirección General de Patrimonio panden die niet meer nodig zijn voor een publieke taak — woningen, garages, bedrijfsruimten, percelen, landbouwgrond — die tot het privédomein behoren.

Twee pagina's zijn relevant:

- `https://hisenda.gva.es/es/web/subastas/inmuebles` — wat nu te veilen staat. Op 18-09-2026 stonden er drie dossiers: EIN 758/2025, EIN 54/2025 en EIN 129/2023. De overzichtspagina noemt geen gemeente of provincie; dat staat in de afzonderlijke stukken.
- `https://hisenda.gva.es/es/web/subastas/inmuebles1` — afgeronde verkopen. Bruikbaar om te zien wat er werkelijk voor betaald is.

Daarnaast bestaat er een *Previsión de Enajenaciones*, een vooruitblik op wat de Generalitat van plan is te verkopen. De pagina verwijst voor details door naar de veilingpagina; wat er precies op de lijst staat en hoe vaak die wordt bijgewerkt is **[te verifiëren]**.

Loopt een veiling zonder bod, dan mag de Generalitat onderhands verkopen — dat kan ook bij een waarde onder 100.000 € of bij een voorkeursrecht van een derde. Onder de rijksregeling geldt hetzelfde principe: artikel 137.4.d van Ley 33/2003 staat directe gunning toe na een mislukte veiling, binnen een jaar en niet onder de eerder aangekondigde voorwaarden.

**Mag dit automatisch gelezen worden?** De robots.txt van `hisenda.gva.es` zegt `User-agent: *` / `Allow: /`. Maar daarna volgt een lijst van negentig bots met `Disallow: /`, waaronder alle bekende AI-crawlers en ook `Scrapy`. Sede.gva.es doet hetzelfde met een lege `Disallow:` voor iedereen en dezelfde botlijst.

Zo lees ik dat: een gewone, rustige lezer mag de pagina ophalen; het is een openbare aankondiging die bedoeld is om gelezen te worden. Wat de site expliciet weigert, zijn AI-trainingscrawlers en scraperframeworks. Onze adapter zou zich dus onder een eigen, herkenbare naam moeten melden, één verzoek per dag, niet meer. Dat is verdedigbaar. **[advocaat]** als we het echt gaan bouwen.

### 10.3 Wat er gratis en zonder discussie kan

De DOGV, het publicatieblad van de Generalitat, heeft een gratis alertdienst per onderwerp, onder andere voor administratieve aanbesteding en voor stedenbouw. De robots.txt sluit alleen een handvol losse oude PDF's uit en verder niets.

Dat is de simpelste route van allemaal: één inschrijving, en de aankondigingen komen per e-mail binnen. Het automatisch inlezen van die mails is een aparte vraag die pas na een juridische toets aan de orde is (staat al zo in TODO).

---

## 11. Wat dit betekent voor het bronnenregister

Voorstel voor `bronnenregister.json`. Nog niet doorgevoerd — dat doen we als Jan akkoord is met §13.

| Nieuwe regel | Bron | Status | Rechten |
|---|---|---|---|
| Portal de Liquidaciones Concursales | `https://www.publicidadconcursal.es/liquidaciones` | **ALLEEN HANDMATIG** (captcha) | `automated_access: no`, `storage: no`, `personal_data: conditional` |
| Registro Público Concursal — consulta | `https://www.publicidadconcursal.es/consulta-publicidad-concursal-new` | **ALLEEN HANDMATIG** (captcha) | idem |
| Tablón Edictal Judicial Único | `https://www.boe.es/edictos_judiciales/` | **ALLEEN HANDMATIG** (robots verbiedt) | `automated_access: no`, `personal_data: yes` |
| PLACSP — open data ATOM/ZIP | `https://contrataciondelsectorpublico.gob.es/sindicacion/…` | **TECHNISCH ONDERZOEK NODIG** | open data, licentie nog na te lezen |
| GVA — subastas de inmuebles | `https://hisenda.gva.es/es/web/subastas/inmuebles` | **TECHNISCH ONDERZOEK NODIG** | robots staat gewone lezers toe, weigert 90 bots |
| DOGV — alertas | `https://dogv.gva.es/es/alertas-del-diari-oficial` | **ALLEEN HANDMATIG** (inschrijving door Jan) | gratis |
| Registro de la Propiedad — nota simple per finca | `https://sede.registradores.org/` | **ALLEEN HANDMATIG** (bestaand, R11) | `storage: conditional` — alleen in het dossier, nooit in de databank (art. 332.2 RH) |

En één wijziging op een bestaande regel: **AEAT-veilinglijst** van actief naar **GEBLOKKEERD DOOR ROBOTS**, tot §13 punt 2 is afgerond.

---

## 12. Wat ik niet heb kunnen vaststellen

Eerlijk, want anders is het rapport niets waard.

1. **Of het veld `date` in de BP-feed de eerste publicatiedatum is.** Daar hangt de hele waarde van signaal 1 aan. Eén vraag aan Background Properties.
2. **De licentietekst van de PLACSP open data.** De ingang `contrataciondelsectorpublico.gob.es` gaf een SSL-fout bij `curl` (zelfondertekend certificaat in de keten) en de beschrijvingspagina op `datos.gob.es` gaf 404. Dat de data open is, staat vast uit meerdere bronnen; de exacte licentienaam niet.
3. **Of er op dit moment iets van de Generalitat in de provincie Alicante te koop staat.** De overzichtspagina noemt drie dossiernummers zonder plaatsnaam. Dat uitzoeken kost drie pagina's openen en dat is werk voor een mens.
4. **De onlineprijs van een nota simple.** Het basisarancel is 3,005061 € per finca; wat registradores.org er online voor rekent, staat achter een inlog.
5. **Wat er precies op de *Previsión de Enajenaciones* van de Generalitat staat en hoe vaak die wordt bijgewerkt.** De pagina verwijst alleen door.
6. **Of de robots.txt van `hisenda.gva.es` een eigen, nette adapter zou toestaan.** Mijn lezing is ja, maar dit is een juridisch oordeel en geen meting. **[advocaat]**
7. **Of de gebruiksvoorwaarden van Aliseda het wekelijks ophalen van hun sitemap toestaan.** Hun aviso legal is zonder JavaScript niet te lezen. Blijft ONBEKEND, zoals B04 al vaststelde.
8. **Hoe vaak `herencia` of `proindiviso` voorkomt in advertenties van Spaanse dorpswoningen in het centrum van Jávea.** Die staan grotendeels niet in onze feed, en de Idealista-assistent kan er niet op zoeken.

---

## 13. Vervolgstappen

### Voor ons (S)

1. **Looptijd en prijsdaling zichtbaar maken.** Neem in het dagrapport, het dashboard en de telefoonpagina per object op: hoeveel dagen sinds de feeddatum, en de prijsverandering sinds onze eerste meting. Eén gedeelde functie in `dh/summary.py`, zodat de getallen overal gelijk blijven. Dit is de grootste opbrengst van dit rapport en hij kost een middag.
2. **De AEAT-adapter stilzetten en uitzoeken.** De robots.txt van `www2.agenciatributaria.gob.es` verbiedt wat wij doen. Zoek een toegestaan pad of zet de bron om naar een handmatige link. Kost ons feitelijk niets — die lijst is in onze gemeenten al maanden leeg.
3. **Een prijsdalingsmelding toevoegen** aan `dh/alerts.py`, naast de bestaande meldingen op haalbaarheid. Voorstel voor de drempel: 5 % of meer daling ten opzichte van onze eerste meting, of twee verlagingen achter elkaar.
4. **Drie links toevoegen** aan `config.TABLONES` op de telefoonpagina: het Portal de Liquidaciones Concursales, de GVA-veilingpagina en het BOP Alicante.
5. **Het bronnenregister bijwerken** volgens §11, ná akkoord.

### ⏸️ ACTIE VOOR JAN

1. **Eén vraag aan Background Properties.** "Is het datumveld in de feed de datum waarop de woning voor het eerst te koop is gezet, of de datum waarop hij bij jullie is ingevoerd?" Van het antwoord hangt af of wij "staat 737 dagen te koop" hard mogen zeggen of alleen "staat bij ons het langst in de lijst".
2. **Inschrijven op de DOGV-alerts** voor administratieve aanbesteding en stedenbouw. Gratis, één formulier, en het is de schoonste bron in dit hele rapport: `https://dogv.gva.es/es/alertas-del-diari-oficial`.
3. **Een vraag aan de advocaat, als je dit verder wilt brengen.** Precies één: mag TREE Properties als vastgoedprofessional zich beroepen op het vermoeden van legitiem belang in artikel 332.3 van het Reglamento Hipotecario om een nota simple op te vragen voor een pand waarin wij koopbelangstelling hebben — en wat mogen wij van die nota simple vastleggen in ons eigen systeem zonder artikel 332.2 te schenden? Dat is de scharniervraag van dit hele onderwerp.

---

## 14. Bronnen

Formaat: URL · controledatum · bewijstype.

**Wetteksten (BOE, open-data-API `legislacion-consolidada`, XML, laatst geldende versie)**

1. `https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-1946-2453/texto/bloque/a221` — Ley Hipotecaria art. 221 · 18-09-2026 · 2
2. `https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-1946-2453/texto/bloque/a222` — Ley Hipotecaria art. 222 · 18-09-2026 · 2
3. `https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-1947-3843/texto/bloque/a332` — Reglamento Hipotecario art. 332 · 18-09-2026 · 2
4. `https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-1889-4763/texto/bloque/art400` — Código Civil art. 400 · 18-09-2026 · 2
5. `https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-1889-4763/texto/bloque/art404` — Código Civil art. 404 · 18-09-2026 · 2
6. `https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-1889-4763/texto/bloque/art1062` — Código Civil art. 1062 · 18-09-2026 · 2
7. `https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-2004-4163/texto/bloque/a51` — TRLCI art. 51, beschermde kadastergegevens · 18-09-2026 · 2
8. `https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-2004-4163/texto/bloque/a53` — TRLCI art. 53, toegang tot beschermde kadastergegevens · 18-09-2026 · 2
9. `https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-2003-20254/texto/bloque/a137` — Ley 33/2003 art. 137, vormen van vervreemding · 18-09-2026 · 2
10. `https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-1986-17958/texto/bloque/art112` — Reglamento de Bienes EL art. 112 · 18-09-2026 · 2
11. `https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-1986-17958/texto/bloque/art118` — Reglamento de Bienes EL art. 118, voorafgaande taxatie · 18-09-2026 · 2
12. `https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-2017-12902/texto/bloque/a9` — Ley 9/2017 art. 9.2, uitsluiting vastgoedverkoop · 18-09-2026 · 2
13. `https://www.boe.es/buscar/doc.php?id=BOE-A-2023-26466` — Ley 6/2023 Comunitat Valenciana, 99 % korting erfbelasting groepen I en II vanaf 28-05-2023 · 18-09-2026 · 2
14. `https://www.boe.es/buscar/doc.php?id=DOUE-L-2016-80807` — AVG art. 14, informatieplicht bij gegevens die niet bij de betrokkene zijn verkregen, termijn één maand · 18-09-2026 · 2

**Registers en portalen**

15. `https://www.publicidadconcursal.es/` — Registro Público Concursal, hoofdpagina, server-gerenderd, HTTP 200 · 18-09-2026 · 1
16. `https://www.publicidadconcursal.es/liquidaciones` — Portal de Liquidaciones Concursales; zeven procedurevormen, verkoopwijze, provincie- en gemeentefilter, **drie captchavelden** · 18-09-2026 · 1
17. `https://www.publicidadconcursal.es/consulta-publicidad-concursal-new` — zoekscherm met provinciefilter en captcha · 18-09-2026 · 1
18. `https://www.publicidadconcursal.es/robots.txt` — `User-Agent: *` / `Disallow:` (leeg) + sitemap · 18-09-2026 · 1
19. `https://www.registradores.org/publicidad-concursal-aviso-legal` — gebruiksrecht beperkt tot huishoudelijk gebruik; reproductie, openbaarmaking en verspreiding zonder schriftelijke toestemming van CORPME verboden · 18-09-2026 · 1
20. `https://www.boe.es/buscar/ayudas/edictos_judiciales_ayuda.php` — TEJU: vier maanden vrij toegankelijk, zoeken op vrije tekst en rechtsgebied, geen provinciefilter · 18-09-2026 · 4
21. `https://www.boe.es/robots.txt` — `Disallow: /edictos_judiciales/`, `/boe_j/`, `/notificaciones/`, `/boe_n/` · 18-09-2026 · 1
22. `https://subastas.boe.es/robots.txt` — `User-agent: *` / `Disallow: /` · 18-09-2026 · 1
23. `https://www2.agenciatributaria.gob.es/robots.txt` — `Disallow: /` · 18-09-2026 · 1
24. `https://sede.agenciatributaria.gob.es/robots.txt` — alleen `NoIx`-mappen gesloten · 18-09-2026 · 1
25. `https://www2.agenciatributaria.gob.es/static_files/common/internet/dep/taiif/subastaInmuebles/data2/bienes.js` — 269 onroerende kavels, 6 in provincie 3 (Alicante), 0 in onze gemeenten · 18-09-2026 · 1
26. `https://sede.registradores.org/` — nota simple en certificación, per finca, login vereist · 14-09-2026 (uit R11) · 2

**Overheidsverkoop**

27. `https://hisenda.gva.es/es/web/subastas` — navigatie naar te veilen en verkochte panden · 18-09-2026 · 4
28. `https://hisenda.gva.es/es/web/subastas/inmuebles` — drie lopende dossiers: EIN 758/2025, EIN 54/2025, EIN 129/2023 · 18-09-2026 · 1
29. `https://hisenda.gva.es/robots.txt` — `User-agent: *` / `Allow: /`, daarna 90 benoemde bots met `Disallow: /`, waaronder `Scrapy` en alle AI-crawlers · 18-09-2026 · 1
30. `https://sede.gva.es/robots.txt` — lege `Disallow:` voor iedereen, daarna dezelfde botlijst · 18-09-2026 · 1
31. `https://sede.gva.es/es/detall-tramit?id_proc=G111809` — trámite "Enajenación mediante subasta pública de bienes inmuebles patrimoniales", EIN 758/2025 · 18-09-2026 · 4
32. `https://hisenda.gva.es/es/web/prevision-enajenaciones/preguntas-frecuentes` — patrimoniale goederen, veiling als regel, onderhandse verkoop bij mislukte veiling, waarde onder 100.000 € of voorkeursrecht · 18-09-2026 · 4
33. `https://dogv.gva.es/robots.txt` — alleen losse oude PDF's uitgesloten · 18-09-2026 · 1
34. `https://dogv.gva.es/es/alertas-del-diari-oficial` — gratis alertdienst per onderwerp · 18-09-2026 · 4
35. `https://contrataciondelsectorpublico.gob.es/wps/portal/DatosAbiertos` — ATOM 1.0 met CODICE, dagelijkse en maandelijkse sindicatie, ZIP per jaar en maand · 18-09-2026 · 4 (licentietekst niet gezien, zie §12)
36. `https://www.ajxabia.com/ver/8130/el-ayuntamiento-de-xabia-activa-la-plataforma-de-licitacion-electronica.html/` — aanbestedingsprofiel van Xàbia is aangesloten op PLACSP · 18-09-2026 · 4

**Banken en servicers**

37. `https://www.alisedainmobiliaria.com/sitemap-investors.xml` — 3.639 URL's; landpagina's voor Jávea/Xàbia (alles, stedelijke grond, finca rústica) en Teulada (alles, te ontwikkelen grond), in ES, EN en FR · 18-09-2026 · 1
38. R10 §5 en §6 — 0 bankwoningen in Jávea bij Idealista, Servihabitat en Diglo; 1 perceel Balcón al Mar, 904.000 → 725.000 € · 15-09-2026 · 1

**Eigen bronnen**

39. `http://127.0.0.1:3100/api/properties?page=1..3&limit=100` — BP-feed, 224 objecten; datumveld bij alle 224; mediaan 127 dagen, maximum 737; 2.376.843 tekens omschrijving; nul treffers op herencia, heredero, proindiviso, urge en divorcio · 18-09-2026 · 1
40. `~/tree-es/deal-hunter/data/dealhunter.sqlite` — `snapshots` 2.086 regels, 239 objecten met meer dan één meting, 1 prijswijziging; `companies` 7 BORME-signalen waarvan 2 in vastgoed of bouw · 18-09-2026 · 1
41. Officiële Idealista-assistent (MCP), zoekopdracht Jávea "prijsverlaging, opknapper" — 69 resultaten, veld `priceDropInfo`, twee objecten met daling; onderliggende sortering `rebajas-desc` · 18-09-2026 · 1
42. Officiële Idealista-assistent, zoekopdracht "venta por herencia" in Jávea en in Alicante-stad — beide nul resultaten; vrije tekst doorzoekt de omschrijving niet · 18-09-2026 · 1

**Eerdere rapporten in deze map**

43. `onderzoek/R10-banken-servicers-fondsen.md` · 15-09-2026
44. `onderzoek/R11-catastro-registro-perceelidentificatie.md` — nota simple, arancel, FLOTI · 14/15-09-2026
45. `onderzoek/R16-rechten-en-compliance.md` — portaalvoorwaarden, databankrecht, AVG, LSSI, Robinsonlijst · 15-09-2026
46. `onderzoek/B04-banken-veilingen-npl.md` — Aliseda-sitemaps, BORME-API, veilingaggregatoren · 16-09-2026

---

## 15. Eén alinea om te onthouden

Verkoopdruk zoeken in Spanje is niet het probleem. Het probleem is dat de plekken waar hij zichtbaar is — het eigendomsregister, het kadaster, de gerechtelijke prikborden — juist daarom op slot zitten voor wie er systematisch doorheen wil. Dat is geen bureaucratische pech; het is precies wat die sloten moeten doen. Wat overblijft is minder spectaculair en beter houdbaar: een pand dat al 620 dagen te koop staat en twee keer in prijs is gezakt, met een makelaar die de telefoon opneemt. Dat signaal hebben we al in huis, het kost niets, en de eigenaar krijgt een eerlijk bod in plaats van een koude bel van iemand die zijn nota simple heeft gelezen.

# B04 — Nieuwe kanalen voor bankvastgoed, liquidaties en veilingen

**Onderzoeksstroom:** B04 (bronnenverbreding, vervolg op R08, R09 en R10)
**Controledatum:** 16-09-2026 (alle metingen hieronder zijn van die dag, tenzij anders vermeld)
**Uitgevoerd door:** onderzoeksagent fase B, TREE Deal Hunter
**Werkwijze:** WebSearch en WebFetch op officiële en bedrijfseigen pagina's, plus losse `curl`-controles met een standaard browser-User-Agent (één tot drie verzoeken per site, geen bulk, geen omzeiling). Robots.txt en sitemaps zijn opgehaald omdat sites die zelf publiceren om gelezen te worden. Geen accounts aangemaakt, geen formulieren verstuurd, geen bestanden van derden geïnstalleerd, geen blokkade omzeild.
**Bewijstypen:** 1 door aanbieder vermeld · 2 officiële bron · 3 zelf vastgesteld · 4 afleiding · 5 berekening · 6 professional · 7 onbekend/tegenstrijdig

---

## Samenvatting (8 regels)

1. **De grootste vondst is een gemiste route bij een partij die we al kenden: Aliseda publiceert drie openbare sitemaps** — 5.549 objecten, 6.549 NPL-dossiers en 3.639 investeringspagina's — en daarin staan **land-pagina's voor Jávea/Xàbia én Teulada**. R10 kon Aliseda niet tellen omdat de site JavaScript vereist; de sitemap omzeilt dat probleem niet voor de inhoud, maar wel voor de vraag *of er iets ligt* (type 3/4).
2. **Tweede vondst: `diariodesubastas.com` (Auction Live, S.L., CIF B10632131)** — een verse, actieve veilingaggregator met 5.170 kavels, gratis account, e-mailmeldingen en een open sitemap. Dit is precies het "machinaal of per e-mail te volgen" kanaal dat de opdracht zoekt (type 1/3).
3. **En die aggregator bewijst meteen hoe leeg ons gebied is.** Van 5.170 kavels vallen er 233 in de provincie Alicante en **4 in onze drie gemeenten — vier trasteros (bergingen) in Teulada**. Nul in Jávea/Xàbia, nul in Benitachell, nul in Moraira. Dat bevestigt R08 (Xàbia = 0) onafhankelijk (type 3).
4. **Derde vondst: de BORME-sumario-API van het BOE werkt en staat niet in ons register.** Dagelijks een eigen item "ALICANTE/ALACANT" in Sectie A (Empresarios. Actos inscritos). Dat is de vroegste machineleesbare waarschuwing voor ontbinding, liquidatie en faillissement van lokale bouw- en promotiebedrijven (type 3).
5. **Vierde vondst: `subastasprocuradores.com` heeft wél een sitemap** (66 kavels, robots staat alles toe behalve `/error/`). R08 noteerde "geen RSS/alertas/API gezien" — de sitemap was gemist. De provincie staat niet in de URL, dus tellen kost 66 losse verzoeken; dat hebben we bewust niet gedaan.
6. **Addmeet is echt, maar niet voor ons.** 133 veiling-URL's in de sitemap, zwaartepunt Madrid (33) en Alcalá de Henares (15), kantoren en bedrijfsruimte; **één enkele in de provincie Alicante en nul in onze gemeenten**. Premium kost 3.000 €/kwartaal en is bedoeld voor beleggers met meer dan 7 M€ vermogen (type 1/3).
7. **Vier namen van de opdrachtlijst vallen af met bewijs:** Ansorena is een kunst- en juwelenhuis zonder vastgoed; Axactor koopt alleen schuld en heeft geen woningportaal; Gescobro is incasso van Cerberus, geen vastgoed; en **Anida bestaat niet meer** — `anida.es` leidt door naar een ongerelateerd bedrijf, `divarian.com` antwoordt niet.
8. **Advies: twee dingen doen, de rest laten.** (a) Jan maakt een gratis account op Diario de Subastas met een gebiedsmelding; (b) wij bouwen de BORME-Alicante-lezer, want die is open data, kost niets en is de enige echt nieuwe voorsprong. Aliseda Jávea/Teulada handmatig natrekken. Escrapalia, Auctelia, Addmeet en subastapublica.info niet aansluiten.

---

## 1. Conclusie voor Jan (besluitgericht)

**Conclusie.** Er zijn drie kanalen bijgekomen die de moeite waard zijn, en ze leveren alle drie iets anders. Diario de Subastas geeft u **één e-mail in plaats van tien portalen**. De BORME-API geeft ons **een signaal weken vóór de veiling**: als een bouwbedrijf in Alicante wordt ontbonden of in liquidatie gaat, staat dat in het handelsblad lang voordat het pand in het veilingportaal opduikt. En Aliseda blijkt in Jávea en Teulada grond te hebben liggen die R10 niet kon zien.

Tegelijk is de eerlijke oogst van de veilingkant zelf klein. Ik heb vandaag in onze drie gemeenten **vier bergingen in Teulada** gevonden en verder niets. Dat is geen meetfout van één bron: het komt overeen met wat R08 op 14-09 vond (Xàbia 0, rechtbank Dénia 0) en met wat R10 op 15-09 vond (0 bankwoningen in Jávea). Veilingen zijn voor ons dus een **wachtkanaal**, geen zoekkanaal.

**Onderbouwing.**
- Diario de Subastas, sitemap `sitemap-auctions.xml`, 16-09-2026: 5.170 kavel-URL's; 233 met "alicante/alacant"; 4 met "teulada"; 0 met javea/xabia/benitachell/moraira (type 3, zelf geteld).
- Alicante-uitsplitsing op URL-naam: 82 viviendas, 28 garajes, 24 generiek "inmueble", 16 fincas, 12 solares, 8 locales, 5 trasteros, 1 nave (type 3/4 — de indeling komt uit het URL-pad, niet uit een veld).
- Aliseda `sitemap-investors.xml`, 16-09-2026: 3.639 URL's, waarvan 99 onder `/alicante/`, met eigen pagina's voor `javeaxabia` (finca rústica én suelo urbano) en `teulada` (suelo urbanizable) (type 3 voor de URL's, type 4 voor de conclusie dat er dus voorraad ligt).
- BORME-sumario-API, 15-09-2026 (dag 178): HTTP 200, JSON én XML, Sectie A bevat item `BORME-A-2026-178-03` met titel "ALICANTE/ALACANT" (type 3).
- Addmeet `sitemap.xml`, 16-09-2026: 1.457 URL's, 133 met `/subasta/`, daarvan 1 in de provincie Alicante en 0 in onze gemeenten (type 3).

**Aannames.**
- Alle tellingen zijn momentopnames van één dag. Veilingvoorraad draait snel.
- Ik tel op **URL-tekst**, niet op een gestructureerd gemeenteveld. Een kavel dat in de URL alleen "alicante" heet maar feitelijk in Xàbia ligt, telt bij mij als provincie en niet als gemeente. De telling van onze drie gemeenten is daarom een **ondergrens**, geen exact getal (type 4).
- Dat Aliseda een land-pagina voor Jávea/Xàbia in haar sitemap zet, betekent vrijwel zeker dat er voorraad ligt, maar bewezen is het niet: de pagina zelf is niet leesbaar zonder JavaScript.

**Tegenargumenten.**
- (a) Een aggregator is een tussenpersoon. Diario de Subastas haalt zijn gegevens uit het BOE-portaal, AEAT en TGSS — bronnen die wij al rechtstreeks en rechtmatig lezen. De toegevoegde waarde is het gemak van de melding, niet nieuwe objecten. Neemt de site iets niet mee, dan missen wij het ook.
- (b) De BORME geeft bedrijfsgebeurtenissen, geen panden. Van "bouwbedrijf X in liquidatie" naar "dit perceel in Jávea komt vrij" zit nog een hele stap, en die stap raakt aan gegevens van personen — daar blijven wij af (masterprompt §19).
- (c) Dat de veilingen leeg zijn, kán ook betekenen dat de dure kustgemeenten hun problemen onderhands oplossen. Dan is niet de veiling maar de makelaar-met-haast de vindplaats, en dat is route R06/R07, niet deze.

**Vervolgstap.** Zie §8. Kort: één account voor Jan, één lezer voor ons, één handmatige controle bij Aliseda.

---

## 2. Wat is nieuw — overzicht

| # | Kanaal | Soort | Route | Uniek in ons gebied | Prioriteit |
|---|---|---|---|---|---|
| B04-01 | Aliseda — openbare sitemaps (`-loans`, `-investors`, `-inmuebles`) | Gemiste route bij bekende partij | XML-sitemap (index); inhoud JS-only | **Deels — ja voor grond in Jávea/Xàbia en Teulada** | **Hoog** |
| B04-02 | Diario de Subastas (Auction Live, S.L.) | Nieuwe aggregator | Portaal + gratis account + e-mailmelding; open sitemap | Nee (aggregeert bronnen die wij al hebben) | **Hoog** |
| B04-03 | BORME sumario-API (BOE open data) | Nieuwe officiële bron | JSON/XML-API, dagelijks | Deels — signaal, geen object | **Hoog** |
| B04-04 | subastasprocuradores.com — sitemap | Gemiste route bij bekende partij | XML-sitemap, 66 kavels | Onbekend (provincie niet in URL) | Middel |
| B04-05 | Addmeet (Addmeet networks, S.L.U.) | Nieuw portaal | Portaal + sitemap + nieuwsbrief | Nee — 1 in provincie, 0 in gemeenten | Laag |
| B04-06 | Escrapalia Inmuebles (Surus) | Nieuw portaal | Portaal, JS-only; robots blokkeert filters | Nee — Alicante leeg | Laag |
| B04-07 | TED — notices search API (EU) | Nieuwe officiële bron | REST-API, open | Nee — alleen context (aanbestedingen Sareb/Casa 47) | Laag |
| B04-08 | subastapublica.info | Nieuwe aggregator | Portaal; sitemap met 3 pagina's | Onbekend, waarschijnlijk nee | Laag |
| — | Ansorena, Auctelia, Axactor, Gescobro/Cerberus, Anida | **Afgevallen met bewijs** | — | Nee | — |

---

## 3. De kanalen één voor één

### B04-01 · Aliseda — de sitemaps die we over het hoofd zagen

R10 schreef: "Aliseda, Hipoges, Anticipa, EscogeCasa en Cimenta2 tonen alleen iets met JavaScript. Die kanalen kunnen alleen handmatig." Dat klopt voor de pagina's. Het klopt niet voor de **index**.

`https://www.alisedainmobiliaria.com/robots.txt` (16-09-2026, HTTP 200) noemt drie sitemaps en nodigt daarmee expliciet uit tot ophalen:

```
Sitemap: https://www.alisedainmobiliaria.com/sitemap-index-aliseda.xml
Sitemap: https://www.alisedainmobiliaria.com/sitemap-loans.xml
Sitemap: https://www.alisedainmobiliaria.com/sitemap-investors.xml
```

Wat erin zit (zelf opgehaald en geteld, 16-09-2026, type 3):

| Sitemap | URL's | Inhoud |
|---|---|---|
| `sitemap-loans.xml` | **6.549** | `/npl/<id>` — losse leningdossiers (NPL). Sluit aan op register-regel R2-34 |
| `sitemap-investors.xml` | **3.639** | `/inversion/suelos/...` per regio/provincie/gemeente, in ES, EN en FR |
| `sitemap-inmuebles-aliseda-es-0.xml` | **5.549** | `/inmueble/<id>` — objecten, id's ondoorzichtig, **geen plaatsnaam in de URL** |
| `sitemap-index-aliseda.xml` | 10 sitemaps | inmuebles (es/en/fr), promociones (es/en/fr), category (es/en/fr), blog |

**De treffers in ons werkgebied** (uit `sitemap-investors.xml`, type 3):

- `…/inversion/suelos/todos/comunidad-valenciana/alicante/javeaxabia`
- `…/inversion/suelos/suelos-urbanos/comunidad-valenciana/alicante/javeaxabia`
- `…/inversion/suelos/finca-rustica/comunidad-valenciana/alicante/javeaxabia`
- `…/inversion/suelos/todos/comunidad-valenciana/alicante/teulada`
- `…/inversion/suelos/suelos-urbanizables/comunidad-valenciana/alicante/teulada`

Dus: **suelo urbano en finca rústica in Jávea/Xàbia, suelo urbanizable in Teulada.** 99 van de 3.639 investeringspagina's liggen onder `/alicante/`. Benitachell komt niet voor.

**De beperking, eerlijk.** De site is een volledige JavaScript-applicatie. Elke pagina die ik opvroeg — de Jávea-grondpagina, een NPL-dossier, en `/aviso-legal` — gaf exact 3.890 bytes HTML met alleen `<title>Aliseda</title>` en verder niets (type 3). De sitemap vertelt ons dus *dat* er iets is en *waar*, maar niet *wat*, *hoe groot* of *voor hoeveel*. En omdat ook de aviso legal niet zonder JavaScript te lezen is, **kennen wij de gebruiksvoorwaarden van Aliseda niet** — opslaan, historie bewaren en met AI analyseren staat daarmee op ONBEKEND.

**Wat dit waard is.** De sitemap is geen vervanging van de site, maar wel een gratis kompas: hij zegt in welke gemeenten Aliseda voorraad heeft. Voor Jávea en Teulada wijst hij aan dat er iets ligt dat R10 niet kon vinden. Dat is genoeg voor één handmatige controle in de browser.

> ⏸️ **ACTIE VOOR JAN** — Vijf minuten in de browser: open de drie Jávea-links en de twee Teulada-links hierboven en kijk wat er staat. Wat u ziet, geven we door aan R11/R15 voor kadastrale identificatie.

**Gemiste route bij dezelfde partij — samengevat:** Aliseda stond al in het register (R2-33, R2-34) als "alleen handmatig, JS". Nieuw is dat er een open XML-index bestaat mét gemeentenamen, en dat die index ons werkgebied raakt.

---

### B04-02 · Diario de Subastas — de aggregator die per e-mail werkt

**Wie.** `Auction Live, S.L.`, CIF `B10632131`, Calle Velázquez 105, 28006 Madrid (avisos legales, 16-09-2026, type 1). De site noemt zich "el concentrador por excelencia de subastas públicas y privadas" en zegt door ENISA erkend te zijn als startup.

**Wat het aggregeert.** BOE, AEAT, TGSS, gerechtelijke en concursale veilingen, plus particuliere huizen zoals Catawiki en Route 66 Auctions. De homepage meldt: **"Hoy hay +5.1 K subastas activas"** over **"+14 portales públicos y privados"** (type 1).

**Wat ik zelf gemeten heb** (`sitemap-auctions.xml`, 16-09-2026, type 3):

| Meting | Aantal |
|---|---|
| Kavel-URL's totaal | **5.170** |
| Waarvan onroerend goed (`/subasta/inmueble/` + `/subasta/inmuebles/`) | 2.342 |
| Overig (horloges 1.393, voertuigen 755, roerend 667, overig 13) | 2.828 |
| URL's met "alicante" of "alacant" | **233** |
| **Onze drie gemeenten** | **4** — alle vier `trasteros-en-teulada-alicante` |
| Jávea / Xàbia | **0** |
| Benitachell | **0** |
| Moraira (als eigen naam) | **0** |
| Dénia (ter vergelijking) | 2 |

Uitsplitsing van de Alicante-treffers op URL-naam: 82 viviendas, 28 garajes, 24 generiek "inmueble", 16 fincas, 12 solares, 8 locales, 5 trasteros, 1 nave (type 3/4).

**Toegang en kosten.** Registratie is "gratis"; de site adverteert **"Recibe avisos inmediatos de nuevas oportunidades"** plus favorieten en zoekgeschiedenis. Er is een pad `/subastas-en-seguimiento/` (gevolgde veilingen) dat in robots.txt privé is gezet. Geen RSS, geen API gevonden (type 1/3).

**Rechten — de bepalende zinnen.** De avisos legales bevatten **geen** clausule over geautomatiseerde toegang, robots of scraping (type 3, vastgesteld door er expliciet naar te zoeken). Wel een intellectueel-eigendomsclaim:

> "Todos los contenidos del sitio web, incluyendo textos, fotografías, gráficos, imágenes, iconos, tecnología, software, así como su diseño gráfico y códigos fuente, constituyen una obra cuya propiedad pertenece a Diario de Subastas."

En een aansprakelijkheidsuitsluiting:

> "Diario de Subastas no se hace responsable de la información contenida en las subastas publicadas, siendo responsabilidad de las entidades organizadoras de las mismas."

**Hoe ik dit lees.** De robots.txt staat het kruipen van `/subasta/...`-pagina's uitdrukkelijk toe (met een commentaarregel gedateerd 2026-09-09), en er is geen scrapingverbod. Maar zij claimen eigendom op de inhoud, en de onderliggende feiten komen uit het BOE — dat wij al rechtstreeks als open data lezen. **Dus: niet leegtrekken.** De verstandige route is de e-mailmelding: dat is precies waarvoor de dienst gemaakt is, het kost niets, en het levert ons een menselijke trigger in plaats van een juridisch grijze datastroom.

> ⏸️ **ACTIE VOOR JAN** — Gratis account aanmaken op `diariodesubastas.com` met een opgeslagen zoekopdracht op de provincie Alicante, categorie inmuebles. De meldingen komen dan in uw mailbox; wij lezen ze pas als u dat wilt.

---

### B04-03 · BORME sumario-API — de vroegste waarschuwing, en gratis

Het register kent de BOE-sumario-API (R2-36). De **BORME**-variant staat er niet in, terwijl die op dezelfde open-datavoorwaarden draait.

**Getest op 16-09-2026** (type 3):

```
GET https://www.boe.es/datosabiertos/api/borme/sumario/20260915
Accept: application/json  → HTTP 200, application/json, 47.201 bytes
Accept: application/xml   → HTTP 200, application/xml,  25.751 bytes
```

Wat eruit komt voor die dag (BORME nr. 178):

| Sectie | Naam | Items |
|---|---|---|
| A | SECCIÓN PRIMERA. Empresarios. **Actos inscritos** | 25 (één per provincie) — waaronder `BORME-A-2026-178-03` met titel **"ALICANTE/ALACANT"** |
| B | SECCIÓN PRIMERA. Empresarios. Otros actos publicados en el Registro Mercantil | 5 (Barcelona, Cádiz, Madrid, Sevilla, Valencia) |
| C | SECCIÓN SEGUNDA. Anuncios y avisos legales | 0 die dag |

**Waarom dit voor ons telt.** Sectie A bevat de ingeschreven handelingen: oprichting, benoeming, **disolución**, **liquidación**, benoeming van een **liquidador**, en concursale aantekeningen. Een bouwbedrijf of promotora in de Marina Alta die kopje onder gaat, verschijnt hier **maanden vóór** het moment waarop een pand in het veilingportaal of bij een servicer opduikt. Dat is de enige plek in dit hele onderzoek waar wij een echte voorsprong kunnen nemen in plaats van meekijken.

**De beperking, eerlijk.** De API levert per provincie een **PDF-verwijzing**, geen gestructureerde lijst van handelingen. Het Alicante-item van 15-09 was een PDF van 382 KB. Om er "liquidación" of "concurso" uit te halen moet die PDF gelezen en ontleed worden. Dat is te doen, maar het is werk, en de tekst is onbetrouwbare invoer (masterprompt §27).

**De tweede beperking, belangrijker.** Wat hier staat zijn **bedrijfsgegevens**, maar er staan ook namen van bestuurders en liquidateurs in. Wij bewaren alleen de **rechtspersoon, het handelingstype en de datum**, nooit natuurlijke personen (masterprompt §19). Van bedrijf naar pand komen we via Catastro en Registro op naam van de rechtspersoon — dat is R11-werk en hoort in een apart besluit.

**Rechten.** De BOE-open-datapagina stelt: "Tenga en cuenta que la reutilización de la información supone la aceptación de las condiciones de reutilización" (type 2). Dit is dezelfde regeling waaronder wij de BOE-sumario-API al gebruiken (R2-36: hergebruik gratis, bronvermelding verplicht). Ratelimits zijn niet gepubliceerd — dus één ophaalronde per dag, niet meer.

---

### B04-04 · subastasprocuradores.com — er ís een index

R08 noteerde: "geen RSS/alertas/API gezien" en zette het kanaal op TECHNISCH ONDERZOEK NODIG. Er is wel degelijk een machineleesbare ingang.

`https://www.subastasprocuradores.com/robots.txt` (16-09-2026, type 3):

```
user-agent: *
disallow: /error/
sitemap: https://www.subastasprocuradores.com/sitemap.xml
```

`sitemap.xml`: **70 URL's, waarvan 66 kavels** onder `/subastas/<id>` met ondoorzichtige id's (type 3). De robots.txt sluit niets uit behalve de foutpagina — dit is een expliciete uitnodiging aan crawlers.

Een kavelpagina is **server-gerenderd**: de `<title>` bevat de volledige omschrijving, bijvoorbeeld "Subasta: S87 — Parcela edificada en Praça do Chile, Av Almirante Reis, Arroios, Lisboa". De locatie is dus zonder JavaScript te lezen (type 3, één pagina gecontroleerd).

**Waarom ik niet geteld heb.** De provincie zit niet in de URL. Een telling van Alicante vraagt 66 losse verzoeken. Dat gaat over de grens van "één of twee nette verzoeken per site" en is voor een eenmalige meting niet te rechtvaardigen. Als dit kanaal in productie gaat, is één ronde van 66 verzoeken per dag met een pauze ertussen wél verdedigbaar — maar dat is een beslissing, geen vanzelfsprekendheid.

**Wat we al wisten (R2-40, R08 §6.4):** 4 % commissie op onroerend goed, 15 % op roerend; waarborg per bankoverschrijving; registratie één per persoon; rechtbanken van Madrid bevoegd. Over scrapen staat niets in de voorwaarden (type 3, R08).

**Prioriteit middel.** Het portaal is echt en officieel (Consejo General de Procuradores, entidad especializada onder LEC art. 641), maar 66 kavels landelijk is weinig, en de kans dat daar een villa in Jávea tussen zit is klein. Aansluiten pas als B04-02 en B04-03 draaien.

---

### B04-05 · Addmeet — echt, netjes, en leeg bij ons

**Wie.** `Addmeet networks, S.L.U.`, Registro Mercantil de Barcelona, tomo 41761, folio 29, hoja B-396022 (términos y condiciones, 16-09-2026, type 1).

**Technisch.** `robots.txt` (HTTP 200) blokkeert alleen `/index.php`, `/condiciones_subasta` en de asset-mappen, en wijst naar `sitemap_index.xml` → `sitemap.xml`. Die laatste is 594.839 bytes met **1.457 URL's**, waarvan **133 met `/subasta/`** (type 3).

**Dekking — de eerlijke uitkomst** (type 3, geteld op URL):

| Plaats | Veilingen |
|---|---|
| Madrid | 33 |
| Alcalá de Henares | 15 |
| Zaragoza | 5 |
| Palma de Mallorca | 4 |
| Sevilla / Málaga | 3 / 3 |
| **Provincie Alicante** | **1** (solar residencial, wijk Los Ángeles, stad Alicante) |
| **Jávea / Xàbia / Benitachell / Moraira / Teulada** | **0** |

Het aanbod is bovendien overwegend **commercieel**: 128 URL's "oficinas-edificio-oficinas", 20 "trastero-edificio-trasteros", 17 "nave-logistica". Woningen en villa's zitten er nauwelijks in.

**Toegang en kosten.** Het portaal is een **publicatieplatform**, geen leesdienst. De tarievenpagina (type 1): standaardadvertentie **300 €/kwartaal**, Premium/off-market **3.000 €/kwartaal** (1.500 € met Premium-contact). Om als Premium-belegger meldingen te krijgen van de 45 verborgen "mercado cerrado"-advertenties geldt een drempel van **meer dan 7 M€ aan vermogen met LTV < 60 %**. De site meldt letterlijk: "45 anuncios de mercado cerrado no visibles por usted". Er is een nieuwsbrief (`/newsletter`) en per zoekopdracht "Guardar como alerta"; geen RSS, geen API, geen export (type 1/3).

**Rechten.** De términos y condiciones bevatten **geen** clausule over geautomatiseerde toegang of scraping (type 3, expliciet nagezocht). Wel: "no podrá retirar ni alterar ningún aviso sobre derecho de autor (copyright), marca comercial u otros avisos sobre propiedad industrial e intelectual". Aviso legal, condiciones de uso en política de privacidad staan onder de paden `/aviso_legal`, `/politica_de_privacidad` en `/terminos_y_condiciones_de_uso` (gevonden in de footer; mijn eerste gok op koppeltekens gaf 404).

**Oordeel: laag.** Technisch de netste van het stel, inhoudelijk niet ons gebied en niet ons producttype. Niet aansluiten. Wél onthouden voor de dag dat TREE Constructions een bedrijfspand of logistieke kavel zoekt.

---

### B04-06 · Escrapalia Inmuebles (Surus) — dicht en leeg

**Wie.** Escrapalia is het veilingplatform van **Surus**; `inmuebles.escrapalia.com` is het aparte vastgoedportaal. Surus presenteert zich als *entidad especializada* voor concursale liquidaties en stelt "el único entidad especializada en tener un portal de subastas exclusivo para la comercialización de activos inmobiliarios" (surusin.com, via zoekresultaat, type 1/4 — niet op de bronpagina zelf geverifieerd).

**Technisch — en dit is bepalend.** `robots.txt` van beide domeinen (16-09-2026, type 3) sluit het vastgoeddeel en alle filters expliciet uit:

```
Disallow: */categoria/inmuebles*
Disallow: */category/inmuebles*
Disallow: *province=*
Disallow: *location=*
Disallow: *saleType=*
Disallow: *priceMin=*   (en zo verder)
```

Daarmee is elke geautomatiseerde ingang op de vastgoedcategorie **verboden door de site zelf**. De sitemap van `inmuebles.escrapalia.com` bevat maar 8 URL's en alleen statische pagina's (home, categoría, eventos, faq, contacto, cómo vender) — geen kavels.

**Dekking.** De categorie-pagina levert bij een gewoon verzoek 3.571 bytes HTML zonder enige kavel, prijs of plaatsnaam: een JavaScript-schil (type 3). Er bestaat een filter-URL `…/es/categoria?country=España&province=Alicante`, maar die valt onder het robots-verbod. Uit een zoekresultaat op die pagina komt naar voren dat Alicante op dit moment **nul** kavels heeft in alle vastgoedcategorieën (type 4 — afgeleid uit een zoekfragment, niet zelf op de pagina gezien).

**Voorwaarden.** Ik heb de condiciones-de-uso-pagina niet kunnen lezen (`/es/condiciones-de-uso/` gaf de JS-schil terug). Gebruiksrechten: **ONBEKEND**. Wel weten we uit R08 dat het zusterplatform eActivos machinale toegang uitdrukkelijk verbiedt; het is redelijk te veronderstellen dat Escrapalia een vergelijkbare lijn volgt, maar dat is een vermoeden (type 4), geen vaststelling.

**Oordeel: laag, alleen handmatig.** Het platform is legitiem en relevant voor faillissementsvastgoed in heel Spanje, maar ons gebied is er leeg, en de site verbiedt zelf de enige manier waarop wij het efficiënt zouden volgen. Handmatig bezoeken mag; aansluiten niet.

---

### B04-07 · TED — de aanbestedingen rond Sareb en Casa 47

De opdracht vraagt naar "Sareb Casa 47 en hun aanbestedingen". Hier is het antwoord in twee delen.

**Casa 47 levert ons niets.** `casa47.es/traspaso-vivienda-y-suelo` (16-09-2026, type 1/2) beschrijft een **eenrichtingsoverdracht van Sareb naar Casa 47 zonder tegenprestatie** — geen aankoop, geen markt, geen inkoopformulier voor eigenaren of ontwikkelaars, geen lijst of feed van objecten. De criteria zijn bovendien voor ons irrelevant: woningen tot 85 m² (of tot 150 m² bij een bescheiden taxatie), grond vanaf 150 m² met capaciteit voor **30+ woningen** in *residencial plurifamiliar*. Dat is sociale-huurstapelbouw; wij doen villa's en percelen aan de kust. Ongeveer 40.000 woningen en 2.400 percelen gaan die kant op, wat betekent dat de voorraad die Sareb nog vrij mag verkopen **krimpt**, niet groeit.

Er is één indirecte kans die géén bron is maar wel het vermelden waard: Casa 47 is een **koper** van grond met woningcapaciteit. Voor route B (grond en projectontwikkeling) is dat eerder een mogelijke afnemer dan een leverancier. Buiten scope van B04 — doorgeven aan R07.

**TED is wel een echte machineleesbare ingang, maar voor context.** De zoek-API van Tenders Electronic Daily antwoordt zonder account of sleutel:

```
POST https://api.ted.europa.eu/v3/notices/search
Content-Type: application/json
→ HTTP 200, application/json
```

(16-09-2026, type 3 — de API werkt; mijn eerste zoekvraag op `buyer-name="Sareb"` gaf 0 treffers en een full-text-variant filterde niet goed, dus de **zoeksyntaxis moet nog uitgezocht worden**. Ik claim hier alleen dat het eindpunt open is en JSON teruggeeft, niet dat ik Sareb-aanbestedingen heb opgehaald.)

**Waarde.** R10 verwees al naar TED-aankondiging 140491-2026 rond de Sareb-mandaten. Wie deze API volgt, ziet **wie welke portefeuille gaat beheren** voordat de pers het meldt — nuttig om te weten bij welke servicer je moet aankloppen, maar het levert geen enkel object op. **Prioriteit laag**, en alleen als er ooit tijd over is.

---

### B04-08 · subastapublica.info — niet beoordeeld, vermoedelijk marginaal

`robots.txt` (HTTP 200) bevat alleen een sitemapverwijzing zonder enige beperking. De sitemap zelf telt **3 URL's**: de homepage, `vehiculos.php` en `otros-bienes.php` (type 3). Geen kavelpagina's, geen vastgoedcategorie in de index. Het lijkt een oudere PHP-site met een beperkte opzet. Ik heb er geen verdere verzoeken aan besteed. **Prioriteit laag; niet aansluiten.**

---

## 4. Afgevallen met bewijs — en waarom dat winst is

| Partij | Wat ik vaststelde | Bron / datum | Type |
|---|---|---|---|
| **Ansorena** | Veilinghuis in Madrid (Alcalá 52) voor **juwelen, horloges, kunst en antiek**, opgericht 1845. Geen vastgoedtak, geen inmuebles-categorie. | ansorena.com (HTTP 200) + zoekresultaten, 16-09-2026 | 3/4 |
| **Auctelia** | Site laadt alleen met JavaScript ("Chargement…"); geen leesbare inhoud. In Spaanse vastgoedveilingzoekopdrachten komt de naam niet voor. Positionering is industrieel materieel, niet onroerend goed. | auctelia.com/es/, 16-09-2026 | 3/7 |
| **Axactor** | `axactor.es` → `axactor.com/es/`. Drie diensten: "Gestionamos Deuda / 3PC", "BPO & Carve Out", "Compramos porfolios de deuda / NPL". **Geen woningportaal, geen objectenlijst, geen REO-verkoop aan particulieren.** | axactor.com/es/, 16-09-2026 | 1/3 |
| **Gescobro (Cerberus)** | Incassobedrijf van Cerberus; geen vastgoedportaal gevonden. Het REO-vastgoed van Cerberus in Spanje loopt via Altamira/doValue en Anticipa/Aliseda — beide al in het register. | zoekresultaten, 16-09-2026 | 4 |
| **Anida** | **Bestaat niet meer als kanaal.** `anida.es` (HTTP 200) leidt door naar `epoca.es`, een ongerelateerd bedrijf. `divarian.com` (de BBVA/Cerberus-opvolger) geeft geen antwoord. | curl, 16-09-2026 | 3 |
| **Cerberus "Proyecto Gloria"** | Verkoop van circa 3.300 woningen (≈800 M€), met objecten in onder meer Alicante; begeleid door Deutsche Bank, eerste biedingen februari 2026. **Institutioneel; portefeuilleverkoop, geen losse objecten.** | persberichten via zoekresultaten, 16-09-2026 | 4, [te verifiëren] |
| **Notariële veilingportalen** | `subastas.notariado.org` en `subastasnotariales.org` **resolven niet**. Dit bevestigt R09: notariële veilingen lopen via het BOE-portaal, niet via een eigen portaal van het notariaat. | curl, 16-09-2026 | 3 |

Vijf namen van de opdrachtlijst kunnen hiermee definitief uit de wachtrij. Dat scheelt volgende ronden werk.

---

## 5. Al bekend — stond al in het register

Deze partijen kwamen in mijn zoekwerk langs maar staan er al in; ik heb ze alleen genoemd waar ik een **nieuwe route** vond.

- **eActivos** (R2-41) — bevestigd verbod op "sistemas mecanizados"; geen nieuwe route gevonden.
- **subastasprocuradores.com** (R2-40) — **wél nieuwe route**: zie B04-04.
- **Aliseda / Anticipa** (R2-33, R2-34) — **wél nieuwe route**: zie B04-01.
- **Sareb** (R2-33) · **Diglo** (R2-32) · **Servihabitat** (R2-30) · **Solvia/Intrum** (R2-31) · **Altamira/doValue, Hipoges, Cimenta2, EscogeCasa, Unicaja, Bankinter** (R2-33) · **Finsolutia** (R2-33) — geen nieuwe leesroute gevonden.
- **Portal de Subastas del BOE** (R2-35) · **BOE sumario-API en RSS** (R2-36) · **AEAT-veilinglijst** (R2-37) · **TGSS** (R2-38) · **Registro Público Concursal en Portal de liquidaciones** (R2-39) · **SUMA** (R2-70) · **GVA hisenda** (R2-72) · **Patrimonio del Estado** (R2-73) · **TEJU** (R2-74) — ongewijzigd.
- **Haya** (R2-31) — opgegaan in Solvia (Intrum); bevestigd dat dit geen apart kanaal meer is.
- Ook de commerciële aggregatoren die R08 ongeverifieerd liet (AlertaSubastas, InversorBOE, AutoBastas, datos-publicos.es) blijven ongeverifieerd; **Diario de Subastas** is uit diezelfde familie maar is hier voor het eerst wél nagelopen.

---

## 6. Beperkingen, blokkades en wat niet gelukt is

| Wat | Wat er gebeurde | Gevolg |
|---|---|---|
| Aliseda — alle pagina's | 3.890 bytes, alleen `<title>Aliseda</title>`; volledige JS-applicatie | Inhoud, prijzen en **de aviso legal** niet leesbaar; rechten ONBEKEND |
| Escrapalia — vastgoedcategorie | `robots.txt` verbiedt `*/categoria/inmuebles*` en alle filterparameters | Geen telling mogelijk; alleen handmatig |
| Escrapalia — voorwaarden | `/es/condiciones-de-uso/` gaf de JS-schil | Gebruiksrechten ONBEKEND |
| Auctelia | Pagina toont alleen "Chargement…" | Aanbod en dekking niet vast te stellen |
| Addmeet — legal pages | `/aviso-legal`, `/condiciones-de-uso`, `/politica-privacidad` gaven 404; de echte paden gebruiken underscores | Opgelost via de footer; términos gelezen |
| Diario de Subastas — `/terminos/` | 404; de juiste paden zijn `/avisos-legales/`, `/politica-privacidad/`, `/politica-cookies/` | Opgelost |
| subastasprocuradores — Alicante-telling | Provincie staat niet in de URL; tellen kost 66 losse verzoeken | **Bewust niet gedaan** (verzoekbudget) |
| Aliseda `sitemap-inmuebles` | 5.549 objecten met ondoorzichtige id's, geen plaatsnaam in de URL | Geen geografische telling mogelijk zonder 5.549 verzoeken — niet gedaan |
| TED-API | Werkt (HTTP 200, JSON), maar mijn zoeksyntaxis filterde niet correct op `Sareb` | Alleen "eindpunt is open" geclaimd, geen resultaten |
| BORME | API geeft per provincie een PDF, geen gestructureerde handelingen | PDF-ontleding nodig vóór productiegebruik |
| `divarian.com`, `gescobro.es`, `bcmglobal.es`, `pepperadvantage.es` | Geen antwoord (curl exit 6 / 000) | Niet te beoordelen |

---

## 7. Rechten per nieuw kanaal (masterprompt §7, rechtenvlaggen)

| Kanaal | Geautomatiseerd | Opslaan | Historie | AI-analyse | Tonen aan Jan | Bepalende zin / grond |
|---|---|---|---|---|---|---|
| BORME sumario-API | **ja** | ja | ja | ja | ja | BOE open data: "la reutilización de la información supone la aceptación de las condiciones de reutilización"; gratis, bronvermelding verplicht (type 2) |
| TED notices API | **ja** | ja | ja | ja | ja | EU open data; eindpunt zonder sleutel bereikbaar (type 3) |
| Diario de Subastas | **nee** (wel e-mailmelding) | conditioneel | conditioneel | conditioneel | ja | IE-claim: "Todos los contenidos del sitio web … constituyen una obra cuya propiedad pertenece a Diario de Subastas" (type 1). Geen scrapingverbod, maar geen toestemming voor hergebruik |
| subastasprocuradores.com | **conditioneel** | onbekend | onbekend | onbekend | ja | robots staat alles toe behalve `/error/`; geen clausule over automatisering aangetroffen (type 3) |
| Addmeet | **conditioneel** | onbekend | onbekend | onbekend | ja | robots laat `/buscador/` toe; geen scrapingclausule in de términos (type 3); wel IE-claim op copyrightvermeldingen |
| Aliseda (sitemaps) | **onbekend** | onbekend | onbekend | onbekend | ja | robots noemt de sitemaps zelf; aviso legal niet leesbaar zonder JS (type 3) → **voorwaarden ONBEKEND** |
| Escrapalia Inmuebles | **nee** | onbekend | onbekend | onbekend | ja | `Disallow: */categoria/inmuebles*` plus alle filterparameters (type 3) |
| subastapublica.info | onbekend | onbekend | onbekend | onbekend | ja | robots zonder beperkingen, verder niet onderzocht (type 3) |

Voor alle kanalen geldt onverkort masterprompt §19: **geen persoonsgegevens van schuldenaren, eigenaren of bestuurders opslaan.** Bij de BORME is dat geen bijzaak maar de kern van de zorgvuldigheid — die PDF's staan er vol mee.

---

## 8. Vervolgstappen

**Wat wij doen (na akkoord):**
1. **BORME-Alicante-lezer bouwen.** Dagelijks één verzoek aan de sumario-API, het Alicante-item eruit, PDF ontleden op `disolución`, `liquidación`, `concurso` en `liquidador`; alleen rechtspersoon, handelingstype en datum bewaren. Kosten: nul. Dit is de enige echte voorsprong uit dit onderzoek.
2. **Aliseda-sitemapwacht.** Wekelijks `sitemap-investors.xml` ophalen en kijken of er gemeenten uit ons werkgebied bij komen of verdwijnen. Eén verzoek per week. Geen inhoud, alleen signalering.
3. **Niet aansluiten:** Escrapalia (verboden), Addmeet (leeg en commercieel), subastapublica.info (marginaal), TED (geen objecten), subastasprocuradores (pas als 1 en 2 draaien).

**⏸️ ACTIE VOOR JAN — drie dingen, samen een halfuur:**
1. **Gratis account op `diariodesubastas.com`** met een opgeslagen zoekopdracht op provincie Alicante, categorie inmuebles, en meldingen aan. U krijgt dan zelf de e-mails.
2. **Vijf Aliseda-links openen** (§B04-01) en doorgeven wat u ziet in Jávea/Xàbia en Teulada. Hun site werkt alleen in een echte browser.
3. **Beslissen over de BORME-lezer.** Wilt u dat wij bedrijfsontbindingen in de provincie Alicante volgen als vroeg signaal? Het kost ons bouwtijd en niets aan abonnement, maar het raakt aan gegevens van bedrijven in nood — dus liever met uw expliciete "ja".

Eén ding dat ik **niet** aanraad: een aanvraag als *API colaborador* bij Aliseda naar aanleiding van dit onderzoek. R10 noemde die route terecht (route D), maar wat ik vandaag zag — de collaborator-app "Aliseda Inmobiliaria-API" in de App Store, uitgegeven door `ALISEDA SERVICIOS DE GESTIÓN INMOBILIARIA, S.L.`, beschreven als "destinada a gestores asociados a Aliseda" met toegang tot "Candidatos, Cuentas, Oportunidades, Activos Inmobiliarios, Productos" (type 1, 16-09-2026) — is een **verkoopgereedschap voor hun eigen netwerk**, geen datakanaal. Het is de moeite waard als TREE Properties toch al makelaarsprovisie bij servicers wil verdienen, maar niet als bron voor Deal Hunter. Dat is een handelsbeslissing van u, geen technische van ons.

---

## 9. Bronnen (alle gecontroleerd op 16-09-2026)

| URL | Wat | Type |
|---|---|---|
| https://www.alisedainmobiliaria.com/robots.txt | Drie sitemapverwijzingen | 3 |
| https://www.alisedainmobiliaria.com/sitemap-loans.xml | 6.549 NPL-URL's | 3 |
| https://www.alisedainmobiliaria.com/sitemap-investors.xml | 3.639 URL's, 99 in Alicante, Jávea/Xàbia en Teulada aanwezig | 3 |
| https://www.alisedainmobiliaria.com/sitemap-index-aliseda.xml | 10 sitemaps | 3 |
| https://www.alisedainmobiliaria.com/sitemap-inmuebles-aliseda-es-0.xml | 5.549 objecten, geen plaatsnaam in de URL | 3 |
| https://www.alisedainmobiliaria.com/inversion/suelos/todos/comunidad-valenciana/alicante/javeaxabia | JS-schil, 3.890 bytes | 3 |
| https://apps.apple.com/es/app/aliseda-inmobiliaria-api/id1498907271 | Collaborator-app, "destinada a gestores asociados a Aliseda" | 1 |
| https://diariodesubastas.com/ | "+5.1 K subastas activas", "+14 portales", gratis account, "avisos inmediatos" | 1 |
| https://diariodesubastas.com/robots.txt | Crawlen van `/subasta/...` toegestaan; commentaar gedateerd 2026-09-09 | 3 |
| https://diariodesubastas.com/sitemap-auctions.xml | 5.170 kavels; 233 Alicante; 4 Teulada; 0 Jávea/Benitachell/Moraira | 3 |
| https://diariodesubastas.com/avisos-legales/ | Auction Live, S.L., CIF B10632131; IE-claim; geen scrapingclausule | 1/3 |
| https://www.boe.es/datosabiertos/api/borme/sumario/20260915 | HTTP 200 JSON en XML; Sectie A item "ALICANTE/ALACANT" | 3 |
| https://www.boe.es/datosabiertos/ | Hergebruikvoorwaarden; vier gedocumenteerde API's | 2 |
| https://www.subastasprocuradores.com/robots.txt | Alleen `/error/` uitgesloten; sitemap vermeld | 3 |
| https://www.subastasprocuradores.com/sitemap.xml | 70 URL's, 66 kavels | 3 |
| https://www.addmeet.com/robots.txt · /sitemap/sitemap.xml | 1.457 URL's, 133 veilingen, 1 in provincie Alicante | 3 |
| https://www.addmeet.com/tarifas | 300 €/kwartaal standaard, 3.000 € Premium, drempel 7 M€ vermogen | 1 |
| https://www.addmeet.com/terminos_y_condiciones_de_uso | Addmeet networks, S.L.U.; geen scrapingclausule | 1/3 |
| https://www.addmeet.com/inversiones-inmobiliarias/subastas-inmobiliarias | "45 anuncios de mercado cerrado no visibles por usted" | 1 |
| https://www.escrapalia.com/robots.txt · https://inmuebles.escrapalia.com/robots.txt | `Disallow: */categoria/inmuebles*` en alle filterparameters | 3 |
| https://inmuebles.escrapalia.com/sitemap.xml | 8 URL's, alleen statische pagina's | 3 |
| https://inmuebles.escrapalia.com/es/categoria/ | JS-schil, 3.571 bytes | 3 |
| https://www.casa47.es/en/traspaso-vivienda-y-suelo | Overdracht van Sareb zonder tegenprestatie; criteria ≤85/150 m², grond 30+ woningen | 1/2 |
| https://api.ted.europa.eu/v3/notices/search | HTTP 200, JSON, zonder sleutel bereikbaar | 3 |
| https://www.axactor.com/es/ | Drie schulddiensten, geen vastgoedportaal | 1/3 |
| https://www.ansorena.com/es | Juwelen-, horloge- en kunstveilingen; geen vastgoed | 3/4 |
| https://www.auctelia.com/es/ | Alleen "Chargement…" | 3 |
| https://www.anida.es/ → https://www.epoca.es/ | Doorverwijzing naar ongerelateerd bedrijf | 3 |
| https://subastapublica.info/robots.txt · /sitemap.xml | 3 URL's, geen kavelindex | 3 |
| https://subastas.notariado.org/ · https://www.subastasnotariales.org/ | Resolven niet | 3 |
| https://www.subastasprocuradores.com/subastas/g5h3n79wgyfxs37o | Kavelpagina server-gerenderd; locatie in `<title>` | 3 |

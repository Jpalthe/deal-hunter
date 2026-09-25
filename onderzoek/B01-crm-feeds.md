# B01 — Makelaars-CRM's en de feeds die een partnerkantoor ons mag geven

**Stroom:** B01 · **Controledatum alle regels:** 16-09-2026 · **Werkgebied:** Jávea/Xàbia, Benitachell, Moraira/Teulada
**Bronnenregister gelezen:** `/Users/root-admin/tree-es/deal-hunter/bronnenregister.json` (75 regels)
**Voorkennis gelezen:** R03, R04 (§3.5 CRM-exports), R06 (kantorenregister + verificatie), R07

Bewijstypen: 1 = door aanbieder vermeld · 2 = officiële bron · 3 = zelf vastgesteld · 4 = afleiding · 5 = berekening · 6 = professional · 7 = onbekend/tegenstrijdig.

---

## 1. De kern in tien regels

1. De belangrijkste vondst is geen nieuwe partij maar een **misgelopen route**: **Inmoweb** en **Mediaelx/LetsINMO** hebben allebei een gedocumenteerde, zelfbediende exportfunctie die letterlijk is gebouwd om een XML-link aan een *colaborador* te geven. Drie Jávea-kantoren en vier Moraira-kantoren zitten op die twee systemen.
2. **Paagees is geen CRM** maar een weblaag. Elk Paagees-kantoor in de Marina Alta (≥ 16 sites) draait dus al op een XML-feed of API van een onderliggend CRM. Die feed bestaat al; hij hoeft alleen naar ons gedupliceerd te worden.
3. **Correctie op R06:** het niet-thuisgebrachte webplatform met assetpad `crm/pages/agencies/<naam>` is **Sooprema**. Zelf vastgesteld bij Llidomar (Jávea) en AREA Costa Blanca (Benissa). Sooprema's voetafdruk hier is dus groter dan R06 vermeldde.
4. **Nieuwe rechtenbeperking bij Witei**, die in R2-29 ontbreekt: het servicecontract verbiedt het gebruik van Witei "as a tool to facilitate collaboration between independent companies and, in particular, real estate agencies", op straffe van directe opzegging van alle betrokken accounts.
5. **MLS Costa (R2-26) had een gemiste leesroute:** gratis account = alleen feed *in*; betaald = "XML Feed out … with all the properties within MLS COSTA", of een *circle* in Inmovilla. Dat is een echte leesroute op een gedeelde voorraad met Costa Blanca-dekking.
6. **Resales-Online (R2-24) had eveneens een gemiste route — en die loopt dood.** De "Static XML feed for shared properties" bestaat, maar: "This feed can only be used for your own website. It cannot be used with portals or other third-party sites."
7. **Apibolsa/INMOPC (R2-27) had een gemiste route:** elk CRM dat Kyero 3.0 genereert kan aanleveren, en "Se pueden descargar las copias de seguridad de los inmuebles compartidos".
8. **Nieuw en concreet voor ons gebied:** **RedSP** (Dénia) — nieuwbouwdatabase, 730+ promociones / ±2.100 referenties op de Costa Blanca, te lezen via XML (Kyero V3) of rechtstreeks in Inmovilla, vanaf ±€29–40 per maand.
9. **Nieuw:** **EasyInmo** (Alicante, bouwer van RedSP, MLScosta en FreeMLS, en het systeem achter Javea Home Finders) adverteert met "Unlimited XML Feeds In" én "Unlimited XML Feeds Out".
10. **Nieuw, klein:** FreeMLS.es (gratis), Babysteps MLS (€39 p/m), MLS España/Anaconda (39 objecten in Jávea gezien), Optima-CRM, Inmogesco, Inmotek, RealtySoft, InmolinkCRM.

---

## 2. Wat een bevriend kantoor ons technisch kan geven, per systeem

Doorslaggevend onderscheid (masterprompt §3): een koppeling om **onze** advertenties te publiceren is voor Deal Hunter waardeloos; we zoeken routes om **andermans** aanbod te lezen, en feeds die een partner ons rechtmatig mag geven.

### 2.1 Systemen met een gedocumenteerde, zelfbediende export naar een derde

| CRM | Formaat | Zelfbediend? | Sleutel/beveiliging | Alleen eigen objecten? | Bewijs |
|---|---|---|---|---|---|
| **Inmoweb** | XML ("Esta exportación (en inglés, *XML feed*) está en formato XML, un formato apto para que cualquier portal o **colaborador** que necesite importar tus inmuebles, lo utilice") | Ja, via het beheerpaneel | "es necesario que generes una clave (en inglés *API key*) para cada portal o colaborador al que desees concederle acceso"; toegang per e-mailadres van de ontvanger, "revocar el acceso en cualquier momento" | Ja: "todos los inmuebles **publicados en tu página web** con todas las características públicas" | 1 — ayuda.inmoweb.es (16-09-2026) |
| **Mediaelx / LetsINMO** | XML | Ja: "LetsINMO real estate CRM is **self-managing software** so you **can create as many XML Feed as you want**" | Niet vermeld | Keuze: "Genuine properties, Imported properties, All properties" — dus óók geïmporteerde objecten van derden | 1 — mediaelx.net (16-09-2026) |
| **Witei** | Kyero v3 ("XML is based on the Kyero XML specifications"), max. 50 foto's | Ja ("Copy XML link of publication") | Niet vermeld | Eigen objecten | 1 — faq.witei.com (16-09-2026) |
| **Inmovilla** | Dagelijkse XML + REST-API (JSON) | Nee — token wordt door Inmovilla verstrekt | "Todos las peticiones deberán ir siempre acompañadas de un token que se facilitará desde Inmovilla"; "solicitarnos un token asociado a vuestra agencia" | Per agentschap | 1 — procesos.apinmo.com/api/v1/apidoc/ (16-09-2026) |
| **Inmogesco** | XML; daarnaast XLS- en CSV-export | Ja: XML activeren en de URL versturen | Niet vermeld | Keuze per portaal | 1 via zoekfragment inmogesco.com (16-09-2026) |
| **Sooprema** | REST-API met sleutel; XML genoemd | Nee — via Sooprema | "Para realizar llamadas a la API se deberá proporcionar una clave de llamada"; voor live data: "la agencia en cuestión deberá ser cliente activo de Sooprema" | Per agentschap | 1 — sooprema.com/api-desarrolladores/ (16-09-2026) |
| **Optima-CRM** | XML, JSON, API | Ja | Niet vermeld | — | 1 — optima-crm.com/es/mls (16-09-2026) |
| **EasyInmo** | "Unlimited XML Feeds In" / "Unlimited XML Feeds Out" | Ja (naar eigen zeggen) | Niet vermeld | — | 1 — easyinmo.es (16-09-2026) |
| **Mobilia** | Publieke API met Swagger (al in R2-29) | Via kantoor | — | Per agentschap | 1 (R04 §3.5) |

**Verversing en vertraging (relevant voor "wie is als eerste bij de nieuwe advertentie"):**
- Witei: elke 60 minuten — "Witei updates XML files every 60 minutes" (1).
- Inmoweb: alleen 's nachts beschikbaar — "los feeds XML de Inmoweb se encuentran disponibles desde las 18:00 horas de un día hasta las 09:00 horas del día siguiente" (1). Dat is een harde beperking: overdag geen feed.
- Inmovilla XML: "Mediante un fichero en formato XML generado de forma diaria" (1); de API is realtime.
- Inmogesco: "las propiedades se volcarán todos los días a las 23:00" (1 via zoekfragment).
- Mediaelx: "Daily automatic synchronization" (1).

### 2.2 Wat de voorwaarden zeggen over doorgeven aan een derde zoals TREE

| Systeem | Bepalende tekst | Gevolg voor ons |
|---|---|---|
| **Witei** | "The use of Witei as a tool to facilitate collaboration between independent companies and, in particular, real estate agencies … is completely prohibited." Plus: "Witei reserves the right to terminate the Service Agreement immediately … In case of detecting that the Customer is using his account in a manner contrary to these terms." (1, faq.witei.com/en/articles/6548820, 16-09-2026) | **Rood vlagje.** De exporthulp zegt "Share this link with your external website or portal", maar het contract verbiedt samenwerking tussen zelfstandige kantoren. Een Witei-kantoor dat ons zijn feed geeft riskeert zijn account als dat als collaboration wordt gelezen. Nooit zelf aandringen; laat het kantoor dit bij Witei bevestigen. |
| **Inmoweb** | De exportfunctie is expliciet bedoeld voor "cualquier portal o **colaborador**", met een intrekbare sleutel per ontvanger (1) | **Groen.** Systeemontwerp dekt precies ons geval. Alleen eigen gepubliceerde objecten — dus geen MLS-objecten van collega's: juridisch de schoonste route. |
| **Mediaelx/LetsINMO** | "Once you have created the XML you can send it to your collaborators" (1) | **Groen, met één voorbehoud:** de exportkeuze omvat ook "Imported properties" en "All properties". Wij moeten schriftelijk vragen om **alleen eigen objecten**, anders krijgen we objecten van derden waar het kantoor geen doorgeefrecht op heeft (lijn R04 §3.5, type 4). |
| **Resales-Online** | "This feed can only be used for your own website. It cannot be used with portals or other third-party sites." Verder: alleen accountbeheerders, IP-adres verplicht, nachtelijke verversing, max. 50 foto's (1, support.resales-online.com/en/articles/9773072, 16-09-2026) | **Rood.** Bevestigt R2-24: netwerkobjecten mogen niet naar ons. Sluit de open vraag in het register af. |
| **Optima-CRM** | "export to wherever you want in whichever format, without asking for our permission" (1, optima-crm.com/es/mls) | **Groen op leveranciersniveau.** Zegt niets over de rechten van de eigenaar en de fotograaf; die blijven staan. |
| **Inmovilla** | Geen bepaling over derden gevonden op de gelezen pagina's (7) | Token wordt door Inmovilla aan het *kantoor* verstrekt; doorgifte aan ons is dus een afspraak tussen ons en het kantoor, met Inmovilla als sleutelhouder. |
| **Sooprema** | Live data alleen als "la agencia en cuestión deberá ser cliente activo de Sooprema" (1) | Route loopt via het kantoor, niet via ons. |

**Juridische lijn blijft ongewijzigd (R04 §3.5, type 4, [te verifiëren] door een Spaanse jurist):** een kantoor mag ons een feed van zijn **eigen** objecten geven; objecten die het zelf via een MLS van collega's ontvangt niet. Nieuw bewijs dat die lijn klopt: Resales-Online verbiedt het letterlijk, en Witei verbiedt zelfs de samenwerking als zodanig.

### 2.3 De weblaag: Paagees (en waarom dat goed nieuws is)

Paagees (c/ Carlos Sentí 33, Dénia) is **geen CRM**: "No cambies de CRM. Paagees se conecta al que ya usas" en het "se actualiza sola con los inmuebles de tu CRM". Verbindt met: **Inmovilla, Inmoweb, Sooprema, Mobilia, Inmogesco, Inmotek, Witei, Casafari** en "cualquier CRM con XML o API" (1, paagees.com, 16-09-2026).

Gevolg: elk Paagees-kantoor in ons gebied — Villadom, Javea Immo, Arzuaga, Homes to be Happy, Montgó Villas, MG Villas, Javea Casas, Selenhome, Bindley, Ferrando, Holidaydream, Benimo, Villa Mediterránea, J. Morató, Inmover, Klaus Hildenbrand — heeft **al** een werkende XML/API-uitgang draaien. De vraag aan zo'n kantoor is dus niet "kunt u iets bouwen", maar "mag de feed die uw website al voedt ook naar ons".

Zelf vastgesteld (3, 16-09-2026): `klaus-hildenbrand.com`, `villalux.com` en `arluxuryliving.com` antwoorden op een gewone curl met "Powered by Paagees Shield" in plaats van de pagina. Voor die drie blijft het onderliggende CRM dus **ONBEKEND**; niet omzeild.

### 2.4 Correctie op R06: `crm/pages/agencies/` = Sooprema

R06 noemde vijf sites met een niet-thuisgebracht "CRM-webplatform" (assetpad `crm/pages/agencies/<naam>`): Villalux, Llidomar, AR Luxury Living, AREA Costa Blanca, Klaus Hildenbrand.

Zelf vastgesteld op 16-09-2026 (3), één GET per domein:
- `llidomarjavea.com` — HTTP 200; 32× "sooprema", 5× "mobilia" in de HTML; enige externe leveranciershost: `www.sooprema.com`.
- `areacostablanca.es` — HTTP 200; 21× "sooprema", 8× "mobilia".

**Conclusie:** dat platform is Sooprema. De Sooprema-voetafdruk in het werkgebied wordt daarmee: TerramaR (Jávea Puerto), Calablanca (Jávea), Benitachell Properties (Benitachell), **Llidomar (Jávea)** en **AREA Costa Blanca (Benissa)** — en mogelijk Villalux en AR Luxury Living (beide afgeschermd, niet bevestigd, 7).

---

## 3. Gedeelde voorraad (bolsa / colaboración / MLS-module) met dekking in ons gebied

### 3.1 Nieuw of met een nieuwe route

| Netwerk | Wat het is | Dekking Marina Alta | Route | Kosten | Bewijs |
|---|---|---|---|---|---|
| **Inmoweb MLS** | MLS binnen het CRM Inmoweb; ook privékringen met eigen commissie- en gedragsregels | "Madrid, Barcelona, Málaga, Valencia y Alicante"; **Xabiacasa (Jávea) noemt zich "Member of Inmoweb MLS"** | Lidmaatschap via Inmoweb-abonnement; automatisch overnemen van andermans objecten op de eigen site "en 5 minutos" | Inmoweb "desde 28,83€/mes"; MLS-prijs niet apart vermeld | 1 (inmoweb.es/mls-inmobiliario/) + 3 (R06) |
| **MLS Costa** | Deelnetwerk voor resales, gebouwd door EasyInmo | "Properties mainly located in Costa Blanca, Costa Calida, Costa de Almeria and Costa del Sol"; Jávea/Moraira niet met naam | **Gratis account:** alleen feed *in*. **Betaald:** "XML Feed out for your own website/property portals **or access to a circle in inmovilla with all the properties within MLS COSTA**" | Gratis tier bevestigd; betaald tarief niet gepubliceerd | 1 (mlscosta.com/en/agent-in-spain, 16-09-2026) |
| **RedSP** | Nieuwbouwdatabase (obra nueva) voor makelaars, HQ Dénia | "+730 developments across Costa Blanca, Costa Cálida, Almeria coast and Costa del Sol"; **1.940 listings** (info-site) resp. "2.100+ references" (agency-pagina) — klein verschil (7). Jávea/Benitachell/Cumbre del Sol niet met naam genoemd | "Via XML feed or directly in Inmovilla"; feedversies "Kyero V3, redsp v3 or redsp v4" | Zone 1: "40€ 29€ /month" (jaarlijks) of "40€ 35€ /month" (per kwartaal), na setupkosten | 1 (redsp.info en redsp.net/en/im-a-real-estate-agency, 16-09-2026) |
| **Babysteps MLS** | Vrij deelnetwerk voor makelaars in Spanje | "currently serves Spain"; geen regio-uitsplitsing | "Connect your property feed once and we import and refresh your listings automatically" — "any standard XML or JSON feed"; handmatig kan ook | Aanbieden en bladeren gratis; samenwerkingsfuncties "39 euros a month" | 1 (babystepsmls.com, 16-09-2026) |
| **FreeMLS.es** | Gratis deelnetwerk (EasyInmo) | Niet per regio gespecificeerd | "Upload your Direct Listings via XML Feed"; feed *uit* met andermans objecten niet vermeld (7) | "FREE" | 1 (freemls.es/en/property-agent-in-spain, 16-09-2026) |
| **MLS España / Anaconda Solutions** | "la bolsa inmobiliaria común española", sinds 2002; technische ruggengraat Anaconda (initiatief 2017, gedragen door MLS, RE/MAX en Look & Find) | mls.es: "más de 700 oficinas en España". **Zelf gezien: 39 objecten voor Jávea/Xàbia op mls-españa.com** (3, 16-09-2026) | Lidmaatschap; "Posibilidad de operar en el sistema con diferentes softwares". Geen API/XML op de gelezen pagina's (7) | Niet gepubliceerd | 1 + 3 |
| **Sooprema MLS / red inmobiliaria** | Deelfunctie binnen Sooprema, ook met niet-Sooprema-kantoren | Volgt de Sooprema-kantoren (zie §2.4): 5 in ons gebied | Binnen het CRM | In abonnement €39–99 p/m | 1 via zoekfragment; niet op de gelezen pagina's bevestigd (7) |
| **Casafari Connect** | Deal- en commissiedeling binnen Casafari Property Sourcing | "Portugal, Spain, France, Italy or Germany"; "Around 650 brands"; geen regio-uitsplitsing | Casafari-abonnement | Zie R2-18 | 1 via zoekfragment casafari.com |

### 3.2 Gemiste routes bij partijen die al in het register staan

- **R2-24 Resales-Online** — de open vraag "artikel Static XML feed for shared properties" is nu beantwoord: de feed bestaat, maar mag uitsluitend op de eigen website van het lid. **Dit sluit de route definitief.** (1)
- **R2-26 MLS Costa** — betaald lidmaatschap geeft wél een XML-feed *uit* met de hele MLS Costa-voorraad, of een Inmovilla-circle. Status kan van "TECHNISCH ONDERZOEK NODIG" naar een concrete offerteaanvraag. (1)
- **R2-26 MLS Mediaelx** — "over 3,000 properties available", Costa Blanca/Cálida/Sol, "import properties from other agents directly to your website and export yours effortlessly", "Daily automatic synchronization". Aantal leden staat niet op de eigen MLS-pagina; "more than 45" komt uit een nieuwsbericht van dezelfde partij (1). (1)
- **R2-27 APIred/Apibolsa (INMOPC)** — twee concrete zinnen die er niet stonden: "Si lo desea podrá exportar de forma automática todos sus inmuebles compartidos a la bolsa, **siempre y cuando su software inmobiliario genere un XML con formato Kyero 3.0**" en "**Se pueden descargar las copias de seguridad de los inmuebles compartidos**". Dus: aansluiten kan met elk Kyero-3.0-CRM, en een lid kan de gedeelde voorraad downloaden. (1, inmopc.com/software-para-inmobiliaria-bolsa-mls.html en apibolsa.es, 16-09-2026)
- **R2-28 Agora MLS** — blijft NIET GEBRUIKEN (geen kantoren in Jávea/Dénia/Moraira), maar context: Agora MLS, Club Notegés en Inmovilla koppelden hun bestanden al op **27-11-2020** tot "más de 3.300 profesionales que operan desde 638 oficinas"; de koppeling loopt technisch via Inmovilla. Verklaart waarom Inmovilla's bolsa zo groot is. (1, observatorioinmobiliario.es)
- **R2-29 Inmovilla** — de bolsa werkt met **kantoor-tot-kantoor-kringen**: "compartir con" + het kantoornummer van de tegenpartij; je kunt de hele portefeuille of een selectie delen en filteren op type, operatie en prijs; toegang is **wederkerig** — de ander moet hetzelfde doen. Gedeelde voorraad: "más de 3.200 agencias inmobiliarias y 15.000 agentes" (via zoekfragment; inmovilla.com gaf ons HTTP 403, zie §5). Elders adverteert Inmovilla met "+4.700 agencias" en "la mayor Bolsa CRM de España" — twee getallen naast elkaar, dus **7**.

---

## 4. Wie gebruikt wat in Jávea, Benitachell en Moraira

Samengesteld uit R06/R06-verificatie (3, 14–15-09-2026) plus de correctie van §2.4 (3, 16-09-2026). Alleen kantoren waar het systeem daadwerkelijk aan de site is af te lezen.

| Systeem | Kantoren in het werkgebied | Exportroute | Waarde voor ons |
|---|---|---|---|
| **Paagees** (weblaag) | Villadom, Javea Immo, Arzuaga, Homes to be Happy, Montgó Villas, MG Villas, Javea Casas, Selenhome, Klaus Hildenbrand (Jávea); Bindley, Ferrando, **Holidaydream** (Moraira); Benimo (Benissa); Villa Mediterránea, J. Morató (Calpe); Inmover | De feed bestaat al — vragen om een kopie | Hoog in aantal; onderliggend CRM per kantoor nog te bepalen |
| **Inmoweb** | **RANDOF** (Jávea + 2× Dénia), **Javea Continental** (Jávea), **Xabiacasa** (Jávea, "Member of Inmoweb MLS") | Sleutel per colaborador, twee klikken, intrekbaar | **Hoogste** — schoonste rechten, laagste drempel |
| **Mediaelx / LetsINMO** | **Casas Ambiente** (Moraira, 42 Jávea-objecten), **BoCasa**, **Tabaira**, **Orange Villas** (Moraira) | XML-link zelf aanmaken en mailen | Hoog; wel expliciet "alleen eigen objecten" vragen |
| **Sooprema** | **TerramaR** (Jávea Puerto), **Calablanca** (Jávea), **Llidomar** (Jávea), **Benitachell Properties** (Benitachell), AREA Costa Blanca (Benissa) | REST-API, loopt via Sooprema; kantoor moet actief klant zijn | Middel — meer stappen |
| **Mobilia** | **Vicens Ash** (Jávea; eigen rubriek "Terrenos", renovatieplanning, "Promociones") | Publieke API met Swagger | Hoog op inhoud, middel op techniek |
| **Inmobalia** (media-host) | Euro Javea, InmoVillas Jávea | XML/API, maar Inmobalia zelf is Costa del Sol (R2-28) | Middel |
| **Inmovilla** (apinmo-infrastructuur) | MP Villas (Calpe); beelden van `fotos15.apinmo.com` bij AR Luxury Living (Jávea) | Token via Inmovilla; of een gedeelde kring | Middel |
| **EasyInmo** | **Javea Home Finders** (Jávea) | "Unlimited XML Feeds Out" | Hoog — te toetsen |
| **Optima-CRM / RealtySoft / max-villas / cbpropertysales e.a.** | Casas Costa Blanca (Moraira) leest ≥ 9 externe beeldhosts (R06-08) | Per bron | Dit kantoor is zelf een aggregator: het heeft doorgeefrechten van anderen nodig, dus juridisch het lastigst |
| **Onbekend / afgeschermd** | Costa Houses, Lucas Fox, Crown, Hamiltons, Paradise ("paradisepro"), Moraguespons, Ahermar, Alta Villas, Plots Direct, Miralbo, Koch & Varlet | — | Openstaand |

---

## 5. Wat niet lukte

| Poging | Uitkomst | Gevolg |
|---|---|---|
| `https://www.inmovilla.com/` (WebFetch) | **HTTP 403** | Aantallen agencies/agents alleen via zoekfragment — geen eigen bronwaarneming |
| `https://inmovilla.com/mls-inmobiliarios/` (WebFetch) | **HTTP 403** | idem |
| `https://inmovilla.com/ventajas-acuerdos-entre-oficinas/` (WebFetch) | **HTTP 403** | Beschrijving van de kringen komt uit zoekfragmenten (1/7) |
| `https://www.xn--mls-espaa-s6a.com/rss/100/100/es/index.xml` (curl) | **HTTP 404**, 6.609 bytes HTML-foutpagina | Geen publieke feed op dat pad; niet verder gezocht |
| `villalux.com`, `arluxuryliving.com`, `klaus-hildenbrand.com` (curl) | "Powered by Paagees Shield" i.p.v. de pagina | CRM onbevestigd; botcontrole niet omzeild (R16 §3.5) |
| Vitrio, Inmovip, Inmobook, Inmoflow | Geen Spaans makelaars-CRM met die naam gevonden; zoekmachine viel terug op Inmovilla/Inmogesco/Inmoplus/INMOPC | **Bestaan niet aantoonbaar in deze betekenis** — zelfde categorie als "Propertyflows" in R04 §3.5 |
| Propertybase / Lofty | "operates in 60+ countries" resp. "75,000 professionals", geen Spanje-specifieke of Marina Alta-dekking gevonden | NIET GEBRUIKEN voor dit doel |
| PropHero | Geen CRM maar een beleggingsplatform ("invest from €25,000 in shared properties or €100,000 to own a full property") | Geen databron; hooguit een kopende partij in de markt |
| HabitatSoft, eGO Real Estate, Inmotek | Bestaan en zijn groot (HabitatSoft "more than 8,000"; eGO "more than 3000 real estate agencies"), maar geen publieke feeddocumentatie en **geen enkel kantoor in Jávea/Benitachell/Moraira gevonden dat ze gebruikt** | Laag; alleen noteren |
| Sooprema MLS-functie | Alleen via zoekfragment; staat niet op de pagina's die wij zelf ophaalden | **7** — te bevestigen bij Sooprema |
| Optima-CRM MLS | Geen ledental, geen dekking, geen prijs op de pagina | Onvolledig |

---

## 6. Beoordeling: levert het uníeke objecten in ons werkgebied?

| Bron | Unieke objecten | Waarom |
|---|---|---|
| Feed van een partnerkantoor (Inmoweb, Mediaelx, Witei, Mobilia, Sooprema, Inmovilla) | **Ja** | Eigen mandaten komen vaak vóór brede publicatie in het CRM te staan. Dit is de enige route naar aanbod dat nog niet op Idealista staat. |
| MLS Costa (betaald, feed uit) | **Deels** | Costa Blanca-breed; overlap met de portalen onbekend, Jávea-aandeel niet gepubliceerd |
| Inmoweb MLS | **Deels** | 250.000 objecten landelijk; Alicante genoemd, ons gebied alleen via Xabiacasa aangetoond |
| RedSP | **Deels** | Nieuwbouw is grotendeels ook elders zichtbaar, maar de *bundeling per promoción met prijs- en beschikbaarheidsmutaties* is uniek en precies wat een acquisitiesysteem mist |
| MLS Mediaelx | **Deels** | 3.000+ objecten Costa Blanca/Cálida/Sol |
| Apibolsa/INMOPC | **Deels** | Provincie Alicante via het Colegio; Jávea-aandeel nog steeds ongemeten |
| MLS España / Anaconda | **Deels** | 39 objecten Jávea gezien; de statistiekpagina van mls.es dateert uit 2019 — het netwerk oogt niet groeiend |
| FreeMLS, Babysteps MLS | **Onbekend** | Jong/klein, geen regiocijfers |
| Casafari Connect | **Nee** | Deal- en commissiedeling, geen datafeed; de data zit in de al bekende Casafari-API (R2-18) |
| Paagees, Property Portal Marketing, Estate Agent Feeds, xmlcombined | **Nee** | Publicatiekant. Alleen indirect nuttig: ze bewijzen dat de feed al bestaat |
| Propertybase/Lofty, eGO, HabitatSoft, Inmotek, PropHero | **Nee** | Geen aantoonbare dekking in de Marina Alta |

---

## 7. De drie kantoren waar wij als eerste om een feed vragen

Gekozen op twee assen: (a) hoeveel **eigen** aanbod van het soort dat Deal Hunter zoekt — percelen, renovatie, eigen mandaten — en (b) hoe klein de technische en juridische drempel is om ons een feed te geven.

### 1. RANDOF Real Estate (Jávea, Av. de la Libertad 47 bl. 5, + twee kantoren in Dénia) — **Inmoweb**
Waarom eerst: Inmoweb is het enige systeem waar de export *per colaborador* is ontworpen, met een intrekbare sleutel, en waar de feed **uitsluitend eigen gepubliceerde objecten** bevat. Daarmee vervalt het hele MLS-doorgeefprobleem. Drie vestigingen betekent Jávea én Dénia-aanbod in één feed. Contact: +34 965 036 919.
Voorbehoud: overdag geen feed (18:00–09:00); voor ons prima, wij halen 's nachts op.

### 2. Casas Ambiente (Moraira, Av. de la Paz 10) — **Mediaelx / LetsINMO**
Waarom: 42 Jávea-objecten op de eigen site (R06, 3) vanuit Moraira — dat is het grensgebied Jávea/Benitachell/Moraira waar wij het slechtst gedekt zijn. De export is zelfbediend en de handleiding zegt letterlijk dat je de link naar je *collaborator* mailt. Contact: info@casas-ambiente.com · +34 966 498 595.
Voorbehoud: uitdrukkelijk "Genuine properties" vragen, niet "All properties" — anders zitten er objecten van derden in.

### 3. Vicens Ash Properties (Jávea, Ctra. Cap de la Nau Pla 137) — **Mobilia**
Waarom: het profiel past het best op Deal Hunter — eigen rubriek "Terrenos", renovatieplanning en een eigen rubriek "Promociones". Mobilia heeft een publieke API met Swagger, dus de koppeling is geen maatwerk. Contact: info@vicensash.com · +34 966 461 643.

**Reserve, in deze volgorde:** Javea Home Finders (EasyInmo, "unlimited XML feeds out"), Holidaydream Moraira (48 parcelas en 71 Jávea-objecten, Paagees-weblaag met nog onbekend CRM), TerramaR Jávea (Sooprema, bouwt en verkoopt zelf).
**Voorlopig niet vragen:** kantoren op **Witei** — het servicecontract verbiedt samenwerking tussen zelfstandige kantoren (§2.2). En **Casas Costa Blanca**, dat zelf van negen externe bronnen leest en dus geen doorgeefrecht heeft.

---

## 8. ⏸️ ACTIE VOOR JAN — conceptbericht (nog niets verstuurd)

Niets hiervan gaat de deur uit zonder jouw "ja" (regel 2 van `~/tree-es/CLAUDE.md`). Eerste contact bij voorkeur telefonisch of persoonlijk (R07 §4.2); onderstaande tekst is de bevestiging per mail daarna.

**Spaans:**

> Asunto: Colaboración TREE Properties — acceso a vuestra cartera propia
>
> Estimado/a [naam],
>
> Soy Jan van der Plas, de TREE Properties (Jávea). Estamos montando un sistema interno de análisis de mercado para la Marina Alta: seguimos precios, tiempos en mercado y oportunidades de reforma en Xàbia, Benitachell y Teulada-Moraira.
>
> Nos gustaría incluir vuestra cartera. Lo que pedimos es concreto: el **XML feed de vuestros inmuebles propios** — el mismo que ya alimenta vuestra web. En [Inmoweb / LetsINMO] se genera en dos clics desde vuestro panel y podéis revocarlo cuando queráis.
>
> Nuestro compromiso, por escrito:
> · Uso **exclusivamente interno** para análisis; no republicamos vuestros inmuebles en ninguna web ni portal.
> · **Solo vuestros inmuebles propios**, nunca los que recibáis de colegas por MLS.
> · Guardamos los datos mientras dure el acuerdo y los borramos a petición vuestra.
> · Si un cliente nuestro se interesa por un inmueble vuestro, os lo enviamos a vosotros con la comisión compartida habitual.
>
> ¿Os viene bien que pase por la oficina esta semana para verlo en diez minutos?
>
> Un saludo cordial,
> Jan van der Plas — TREE Properties, Jávea · [telefoon] · [e-mail]

**Engels (voor kantoren die in het Engels werken, zoals RANDOF en Casas Ambiente):**

> Subject: Working together — access to your own listings
>
> Dear [naam],
>
> I'm Jan van der Plas of TREE Properties in Jávea. We are building an in-house market analysis tool for the Marina Alta — prices, time on market and renovation opportunities in Xàbia, Benitachell and Teulada-Moraira.
>
> We would like your agency in it. What we are asking for is narrow: the **XML feed of your own listings** — the same one that already feeds your website. In [Inmoweb / LetsINMO] it takes two clicks in your admin panel, and you can revoke it at any time.
>
> What we commit to, in writing:
> · **Internal analysis only.** We do not republish your properties on any website or portal.
> · **Your own listings only** — never properties you receive from colleagues through an MLS.
> · We keep the data for the term of the agreement and delete it on your request.
> · If one of our buyers is interested in one of your properties, the lead goes to you, on the usual shared-commission basis.
>
> Could I drop by your office this week? Ten minutes is enough.
>
> Kind regards,
> Jan van der Plas — TREE Properties, Jávea · [telefoon] · [e-mail]

**Bij een "ja" hoort een korte schriftelijke afspraak** (sjabloon R16 §6.3) met vijf punten: doel (acquisitieanalyse), AI-verwerking toegestaan, bewaartermijn, géén herpublicatie, beeldvergelijking alleen intern.

---

## 9. Voorstel voor het bronnenregister

**Nieuwe regels:** Inmoweb (CRM + exportfeed) · Inmoweb MLS · Sooprema · Mediaelx/LetsINMO CRM-export · Inmogesco · Inmotek · Optima-CRM · EasyInmo · RedSP · FreeMLS.es · Babysteps MLS · MLS España/Anaconda Solutions · Paagees (weblaag, publicatiekant) · Casafari Connect · RealtySoft · InmolinkCRM · Property Portal Marketing (publicatiekant).

**Bij te werken regels:** R2-24 (static feed bestaat maar mag niet naar derden — open vraag sluiten) · R2-26 (MLS Costa: betaalde feed-uit met de hele voorraad) · R2-27 (Kyero 3.0-aanlevering + downloadbare back-up van gedeelde objecten) · R2-29 (Witei-verbod op samenwerking; Inmovilla-tokenroute en kringen; Mediaelx toevoegen) · R2-50 (Sooprema-correctie op het `crm/pages/agencies`-platform).

**Statusvoorstel:** alle kantoorfeeds blijven **CONTRACT OF TOESTEMMING NODIG**; MLS Costa, RedSP, Inmoweb MLS en Apibolsa gaan naar **TECHNISCH ONDERZOEK NODIG** (offerte/dekkingsvraag); Resales-Online static feed naar **NIET GEBRUIKEN**; Witei-kantoren krijgen een waarschuwingsnoot.

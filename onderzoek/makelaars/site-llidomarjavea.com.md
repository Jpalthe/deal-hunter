# Llidomar Properties — toets op automatisch lezen

- **Website:** https://www.llidomarjavea.com (bedrijf volgens de eigen juridische pagina: Llidomar Properties S.L., Avda. Arenal 5, 03730 Jávea; algemeen contact +34 965 791 505, info@llidomarjavea.com, kantoor ma–vr 09:30–17:00). Let op: `K01-kantoren-javea.json` noemt Av. Príncipe de Asturias 13 als adres — de site zelf zegt Avda. Arenal 5 **[te verifiëren]**.
- **Datum toets:** 24-09-2026, 23:15–23:20 lokale tijd (server-datumkoppen 21:15–21:19 UTC).
- **Opgehaald (5 verzoeken, telkens ≥ 14 s tussenruimte, conform de Crawl-delay in robots.txt):** robots.txt, sitemap.xml, aanbodpagina `/venta/`, één objectpagina, `/aviso-legal/`. Niets omzeild, niet ingelogd, geen formulieren.
- **Advies: lezen** — het mag volgens robots.txt, de voorwaarden verbieden geen automatisch lezen, en de pagina's zijn goed leesbaar (prijs, m², perceel, plaats en referentie staan in gewone HTML en deels in og-tags). Voorwaarden: 14 s tussen verzoeken, de sitemap als index gebruiken (geen pagineringspagina's), alleen kale feiten bewaren, geen foto's of teksten overnemen. Omdat de site op **Sooprema** draait, is een exportfeed vragen een net alternatief.

## 1. robots.txt — toegestaan, met een crawl-delay van 14 seconden

Bron: https://www.llidomarjavea.com/robots.txt (24-09-2026, HTTP 200, 5.717 bytes, `last-modified` 25-07-2025). Geen `Sitemap:`-regel.

Relevante regels voor `User-agent: *` (letterlijk):

```
User-agent: *
Disallow: /cgi-bin/
Disallow: /images/
Disallow: /html/formulario/llamanos/
Disallow: /html/formulario/48horas/
Disallow: /admin/
Disallow: /html/galeriamodal/*
Disallow: /html/formucontraoferta/*
Disallow: /*/*/*/pagina/*
Disallow: /*/*/*/pages/*
Disallow: /*/*/*/page/*
Disallow: /*/*/*/seite/*
Disallow: /portal/proceso/secciones/
Disallow: /portal/proceso/newsletter/
Disallow: */imprimir/*
Disallow: */print/*
Allow: /
[...]
User-agent: *
Crawl-delay: 14
```

- **Aanbod- en objectpagina's mogen gelezen worden**: `Allow: /`, en `/venta/`, `/alquiler/` en `/venta/<object>/` vallen onder geen enkele `Disallow`.
- Uitgesloten zijn formulieren, de beheeromgeving, galerij-modals, printversies en pagineringspagina's van het patroon `/x/y/z/pagina/…`. De echte paginering van de site is `/venta/pagina-2/` t/m `/venta/pagina-5/` — die valt letterlijk níet onder dat patroon, maar de bedoeling is duidelijk: **niet door de paginering lopen**. Dat hoeft ook niet, want de sitemap geeft alle eigen objecten.
- **`Crawl-delay: 14`**: maximaal één verzoek per 14 seconden. Bij ~100 objectpagina's is een volledige ronde dus ~25 minuten; dat is prima voor een dagelijkse of wekelijkse run.
- Daarnaast staat een lange lijst van ~130 specifieke bots op `Disallow: /` (o.a. Wget, HTTrack, Python-urllib, WebZip, Teleport, EmailCollector). **Gevolg:** nooit lezen met een standaard-User-Agent van Wget of Python-urllib; altijd een eigen, herkenbare User-Agent gebruiken (bij deze toets: `TREE-DealHunter-check/1.0`).

## 2. Gebruiksvoorwaarden — geen scrapingverbod, wél een verbod op hergebruik van de inhoud

Bron: https://www.llidomarjavea.com/aviso-legal/ (24-09-2026, HTTP 200; de link staat in het contactformulier op elke objectpagina). De pagina bundelt "Condiciones generales de uso", privacy en cookiebeleid van Llidomar Properties S.L.

De woorden scraping, robot, crawler, bot, automatisch uitlezen of massaal downloaden **komen niet voor** (gecontroleerd op scrap/robot/crawl/bot/automat/extrac/masiv). Wat er wél staat, samengevat:

- Onder "Compromisos y obligaciones de los usuarios": gebruik van de site mag niet onwettig of schadelijk zijn en mag de normale werking van de site niet hinderen. Over de inhoud is verboden: reproductie, verspreiding of wijziging zonder toestemming van de rechthebbenden, en gebruik "para fines comerciales o publicitarios".
- Onder "Derechos de propiedad intelectual e industrial": reproductie, verspreiding en openbaarmaking van (delen van) de inhoud **met commercieel oogmerk** is uitdrukkelijk verboden zonder toestemming van de site; de site (tekst, foto's, structuur, selectie en ordening) is auteursrechtelijk beschermd.
- De objectpagina's laden bovendien een Sooprema-script `prevent-images-rightclick` — het kantoor wil duidelijk niet dat foto's gekopieerd worden.

**Betekenis voor Deal Hunter:** automatisch lezen wordt niet verboden, maar de inhoud (foto's, beschrijvingsteksten, de "selectie en ordening") mag niet worden overgenomen of doorgepubliceerd, en zeker niet commercieel. Dus: alleen kale feiten vastleggen (referentie, prijs, type, plaats/zone, bebouwd m², perceel m², bouwjaar, link naar de bron) voor eigen analyse; geen foto's of teksten opslaan; niets herpubliceren; en de site niet belasten (14 s). Wil Jan meer dan dat, dan is toestemming of een feed nodig.

## 3. Sitemap — 117 URL's, 85 eigen verkoopobjecten en 16 huurobjecten

Bron: https://www.llidomarjavea.com/sitemap.xml (24-09-2026, HTTP 200, 22 kB; niet vermeld in robots.txt, gevonden op het standaardadres).

- 117 URL's: 1 home, 15 vaste pagina's (conocenos, servicios, vender, comprar, contacto, promos, en de lijstpagina's `/venta/`, `/alquiler/`, `/alquiler-anual/`, `/alquiler-de-temporada/`, `/villas-de-lujo-en-venta-en-javea-y-la-costa-blanca/`, `/apartamentos-en-venta/`, `/parcelas-en-venta/`, `/chalets-en-venta/`, `/casas-de-pueblo/`), **85 objectpagina's onder `/venta/`** en **16 onder `/alquiler/`**. Geen blog- of juridische pagina's.
- Objectpatroon: `/venta/<beschrijvende-slug>-<referentie>/`, referentie in de slug (LL6060, EX2079, LLC3036, C1019 — 56× "ll", 24× "ex", 3× "llc", 1× "exc", 1× "c"). Engels en Frans bestaan als `/en/for-sale/...-ll6060/` en `/fr/vente/...-ll6060/` (hreflang op de objectpagina), maar staan niet in de sitemap.
- Trefwoorden in de 85 verkoopslugs: villa 19, apartamento/apartmento 15, casa (incl. casa-de-pueblo 8, casa-de-campo) 15, parcela 9, local (comercial) 8, solar 5, terreno 5, piso 3, proyecto 3, chalet 2, adosado 2, duplex 2, finca 2, edificio 1, traspaso 1. Opvallend veel grond en renovatie-objecten: parcela/solar/terreno samen 19, plus "a reformar", "casa a construir con licencia", "reparcelación", "proyecto en construcción".
- `lastmod`: 19 objecten in september 2026, 5 in augustus, 16 in juli — de sitemap wordt actief bijgehouden (home `lastmod` 24-09-2026).

## 4. Aanbodpagina en objectpagina

**Aanbodpagina te koop:** https://www.llidomarjavea.com/venta/ (24-09-2026, HTTP 200, 338 kB). Tekst op de pagina: "Se han encontrado un total de **164** propiedades". Twintig kaarten per pagina, gesorteerd op prijs oplopend (13.500 € t/m 279.000 € op pagina 1), paginering `/venta/pagina-2/` … `/pagina-5/` zichtbaar. Per kaart: referentie (`property-3__reference`), prijs (`property-3__price-text`, soms "Consultar"), bebouwd m², perceel m², slaap-/badkamers, titel met link — **de plaats staat niet als apart veld op de kaart**, alleen in de titel. De filters bevatten plaatsen (Jávea, Benitachell, Moraira, Benissa, Calpe, Dénia, Altea, Gata de Gorgos, Ondara, …) en Jávea-zones (Cansalades, Castellans, Granadella, Portichol, Tarraula, Thiviers, …), als URL's van de vorm `/venta/javea/` — die zijn volgens robots.txt toegestaan en geven bij een volgende ronde per plaats een exacte telling.

**Belangrijk verschil 164 vs 85:** de kaarten laden hun foto's uit `/objetos/temp/source/<account>/…`. Op pagina 1 komen 17 van de 20 kaarten uit account `llidomarjavea` en 3 uit andere Sooprema-accounts (`hispania`, `crown`, `javeacasas`; referenties HH1CDMAZ, LLCRFZCZD3, LLJCZBR1FL). De 164 op de site zijn dus **eigen aanbod (≈ 85, de sitemap) plus gedeelde objecten van andere Sooprema-kantoren** (≈ 79) **[te verifiëren]**. Voor Deal Hunter telt vooral het eigen aanbod; de gedeelde objecten duiken ook op bij de bronkantoren (Crown Property staat al in deze reeks).

**Objectpagina bekeken:** https://www.llidomarjavea.com/venta/villa-con-piscina-privada-y-amplio-jardin-en-javea-ll6060/ (24-09-2026, HTTP 200; `<meta name="robots" content="index,follow">`, canonical op zichzelf, hreflang es/en/fr).

- `<script type="application/ld+json">`: **nee, 0 blokken.** Geen schema.org.
- **og-tags: ja** — `og:url`, `og:type` (website), `og:title` ("VILLA CON PISCINA PRIVADA Y AMPLIO JARDÍN EN JAVEA"), `og:description` (eerste zin van de beschrijving), `og:image` (`/opi/363412`, 640×425), `og:locale` es_ES, `og:site_name` "Llidomar Jávea". **Geen prijs, oppervlakte of plaats in de og-tags.**
- In de gewone HTML/tekst staat wél alles: `<title>` "… | Ref: LL6060"; kop met "Ref. LL6060 · 650.000 € · 260 m2 · 1.558 m2 · 4 · 3"; tabel "Características": Tipo Chalet/Villa, Dormitorios 4, Baños 3, **Terreno 1.558 m²**, **Superficie construida 260 m²**, **Construido en 1964**, Plantas 2, Calefacción, Piscina, Parking, Orientación Suroeste, Tipo de terreno Llano; energiecertificaat "EN TRÁMITE"; "Ubicación aproximada" (Leaflet-kaart, geen leesbare coördinaten in de HTML gevonden). **Plaats: Jávea** (in titel en beschrijving; geen zone/straat als apart veld op deze pagina).
- Dit is een typisch Deal-Hunter-profiel: villa uit 1964 op 1.558 m² perceel, 260 m² bebouwd, € 650.000 → ~€ 2.500/m² bebouwd, renovatie-kandidaat **[te verifiëren via bezichtiging/kadaster]**.

## 5. Systeem: Sooprema

Bevestigd via de HTML van `/venta/` en de objectpagina (24-09-2026):

- Vendor-paden `/crm/pages/vendor/sooprema/…` (sooprema-captcha, favorites, floating-thumbnail, jquery-leaflet, prevent-images-rightclick, bootstrap-xx-1440) en thema `/crm/pages/agencies/llidomarjavea/theme/css/style.min.css?v=0.3.29`.
- Cookie-categorieën `sooprema_functional`, `sooprema_statistics`, `sooprema_marketing`; afbeeldingen van gedeelde objecten rechtstreeks vanaf `www.sooprema.com/objetos/…`.
- Serverkop `server: Apache`, HTML-commentaar met rendertijd (`<!-- 0.476 s -->`), kaart-componenten `property-3` / `property-7`, tellerblok `report-1-content-number`.
- Geen `<meta name="generator">`, geen "powered by"-tekst.

Dit sluit aan bij het bronnenregister (R2-88: Llidomar als Sooprema-kantoor). Sooprema levert kantoren standaard XML-exportfeeds voor portalen; een feed vragen is dus technisch eenvoudig voor het kantoor.

## 6. Omvang en dekking Jávea / Benitachell / Moraira

- **Aanbod te koop:** 164 volgens de teller op de site, waarvan ≈ 85 eigen objecten (sitemap) en de rest gedeeld uit het Sooprema-netwerk **[te verifiëren]**. Te huur: 16 (sitemap).
- **Dekking, op basis van de 85 eigen verkoopslugs** (plaats staat niet apart op de kaarten, dus dit is een schatting uit de URL's):
  - Expliciet Jávea 34, Benitachell 4, Moraira/Teulada 2 → **39 unieke objecten (46 %)**.
  - Nog eens ≈ 20 slugs noemen een Jávea-wijk zonder de plaatsnaam (Arenal 5, Tosalet 3, La Corona 3, Montgó 2, casco antiguo 2, Cala Blanca, Pinosol, Puerto, Plaza del Convent, Plaza Marina Alta) → samen **≈ 59 (≈ 70 %)**.
  - Expliciet elders: Benissa 2, Mont-ral (Tarragona) 2, Calpe 1, Dénia 1, Altea 1, Gata de Gorgos 1 → 8 (9 %).
  - Rest (≈ 18) niet uit de slug af te leiden.
  - **Conclusie: minstens twee derde, waarschijnlijk 75–85 % van het eigen aanbod ligt in Jávea, Benitachell of Moraira — verreweg het meeste in Jávea.** Exacte cijfers: bij de volgende ronde de toegestane filter-URL's `/venta/javea/`, `/venta/benitachell/` en `/venta/moraira/` lezen (3 verzoeken).

## Advies en werkwijze

**Lezen**, onder deze voorwaarden:

1. Eén verzoek per **14 seconden** (robots.txt), eigen herkenbare User-Agent, nooit Wget/Python-urllib-standaardnamen.
2. **Sitemap als index** (85 eigen objecten + 16 huur), niet de paginering. Nieuwe objecten herkennen aan nieuwe URL's en `lastmod`.
3. Per object alleen feiten bewaren: referentie, prijs, type, plaats, bebouwd/perceel m², bouwjaar, slaap-/badkamers, URL, datum gezien. **Geen foto's, geen beschrijvingsteksten** (auteursrecht + commercieel-gebruiksverbod in de voorwaarden).
4. Gedeelde objecten (foto-account ≠ `llidomarjavea`) apart markeren; die komen van andere kantoren.
5. Nettere weg: het kantoor om een **Sooprema-feed** vragen — dat is voor hen een standaardfunctie en het geeft ook plaats/zone als veld. ⏸️ ACTIE VOOR JAN als hij dat wil: één mail naar info@llidomarjavea.com.

## Bronnen (alle 24-09-2026)

- https://www.llidomarjavea.com/robots.txt
- https://www.llidomarjavea.com/sitemap.xml
- https://www.llidomarjavea.com/venta/
- https://www.llidomarjavea.com/venta/villa-con-piscina-privada-y-amplio-jardin-en-javea-ll6060/
- https://www.llidomarjavea.com/aviso-legal/
- Lokaal: `K01-kantoren-javea.json`, `K02-kantoren-benitachell-moraira.json` (adres en Sooprema-vermelding).
- Webzoekbudget was op; er is niets buiten de site zelf geraadpleegd.

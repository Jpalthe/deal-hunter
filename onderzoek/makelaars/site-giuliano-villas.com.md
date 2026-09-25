# Giuliano Villas — toets op automatisch lezen

**Datum controle:** 24-09-2026 · **Opgegeven adres:** http://www.giuliano-villas.com · **Werkelijke site:** https://www.costablancajaveaproperties.com
**Kantoor:** Giuliano Villas SL, Avenida de la Libertad 34, local 3, 03730 Jávea (Alicante) · tel. +34 96 6470865 / +34 651 850 647 (bron: voettekst homepage, 24-09-2026)

## Samenvatting in gewone taal

Het opgegeven adres giuliano-villas.com is alleen nog een doorstuurpagina uit 2013. De echte site staat op
costablancajaveaproperties.com (Engels; er zijn ook .es, .de en .fr-versies). Die site staat automatisch lezen toe,
maar met drie beperkingen: (1) alleen de éérste pagina van elke lijst mag gelezen worden, de vervolgpagina's niet;
(2) de site vraagt om 14 seconden pauze tussen verzoeken; (3) tientallen bekende kopieerprogramma's zijn met naam
geblokkeerd, dus onze lezer moet zich eerlijk onder eigen naam melden. Er is geen sitemap en geen gebruiksvoorwaarden-
pagina gevonden. Objectpagina's zijn goed leesbaar (prijs, m², perceel, plaats, referentie staan in de HTML), maar
zonder schema.org-gegevens. Het aanbod is groot (tot ~456 vermeldingen, inclusief verkochte) en ligt voor ruwweg
twee derde tot driekwart in Jávea/Benitachell. **Advies: lezen**, beperkt tot pagina 1 van de lijsten plus de
objectpagina's; voor volledige dekking het kantoor om een feed vragen.

## 1. robots.txt

- **Opgegeven domein:** http://www.giuliano-villas.com/robots.txt → **404 Not Found** (Apache), 24-09-2026. De homepage
  http://www.giuliano-villas.com/ is een bestand van 102 bytes (Last-Modified 14-02-2013) met alleen
  `window.location='http://www.costablancajaveaproperties.com'`. De https-variant geeft een certificaatfout.
- **Werkelijke site:** https://www.costablancajaveaproperties.com/robots.txt (Last-Modified 25-07-2025), opgehaald 24-09-2026.
  Voor `User-agent: *` geldt, letterlijk geciteerd:
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
  Disallow: /*/*/*/stranitsa/*
  Disallow: /*/*/*/siden/*
  Disallow: /portal/proceso/secciones/
  Disallow: /portal/proceso/newsletter/
  Disallow: /giuliano/proceso/enviar/
  Disallow: */html/galeriamodal/*
  Disallow: */imprimir/*
  Disallow: */print/*
  Disallow: */drucken/*
  Disallow: */imprimer/*
  Disallow: */afdrukken/*
  Allow: /
  ```
  en helemaal onderaan een tweede blok:
  ```
  User-agent: *
  Crawl-delay: 14
  ```
- **Uitleg:** objectpagina's (`/property/...`) en de eerste pagina van de aanbodlijsten mogen gelezen worden.
  De vervolgpagina's van lijsten (`/properties/sell/all/page/2/` enz.) vallen onder `Disallow: /*/*/*/page/*` en mogen
  dus **niet**. Printversies (`/print/a4/...`), formulieren en de fotogalerij-modal mogen ook niet. Tussen verzoeken
  wordt 14 seconden gevraagd.
- Daarnaast staan ruim 100 bots met naam op `Disallow: /` — onder meer `Wget`, `Python-urllib`, `httplib`,
  `HTTrack 3.0`, `WebCopier`, `Offline Explorer`, `EmailCollector`. Dat is een duidelijk signaal dat massaal kopiëren
  ongewenst is. Een lezer die zich eerlijk met een eigen naam meldt (bijv. `TREE-DealHunter`) valt onder de `*`-regels.
- Geen `Sitemap:`-regel.

## 2. Gebruiksvoorwaarden

**Niet gevonden.** Op de homepage en de objectpagina staat geen link naar een aviso legal, privacybeleid of
voorwaarden; de voettekst bevat alleen adres, telefoonnummers, "Site Map" (zonder werkende link) en
"©2013 Giuliano Villas SL". Er is wel een cookiebanner ("Customize Cookies", alleen JavaScript). Binnen het budget van
vijf pagina's is niet naar een verborgen adres als `/aviso-legal/` geraden. Conclusie: geen vindbaar verbod op
automatisch lezen, maar ook geen expliciete toestemming.

## 3. Sitemap

- Geen `Sitemap:`-regel in robots.txt.
- https://www.costablancajaveaproperties.com/sitemap.xml → 301 naar `/sitemap.xml/` → **404** (eigen foutpagina
  "Ops, it seems that we do not find what you are looking for"), 24-09-2026.
- `/sitemap_index.xml` niet geprobeerd (paginabudget). Aantal object-URL's in sitemap: **niet vast te stellen**.

## 4. Aanbodpagina en objectpagina

- **Aanbodpagina (menu "Resales"):** https://www.costablancajaveaproperties.com/properties/sell/all/ — 12 kaarten per
  pagina, paginering met laatste pagina `/page/38/` (opgehaald 24-09-2026). Nieuwbouw: `/properties/sell/work-new/`.
  Landingspagina's zonder paginering-blokkade op het derde niveau: `/villas-for-sale-in-javea/`,
  `/luxury-villas-for-sale-in-javea/`, `/apartments-for-sale-in-javea/`,
  `/properties/category/giuliano-villas-s-exclusive/`.
  Per kaart in de HTML: titel (`<h3>`), `Ref. G-nnnn`, plaats (`JAVEA - COSTA NOVA`), prijs (`class="fila precio"`),
  label (`class="etiquetaprop"`). Pagina 1 op 24-09-2026: labels Sold: 6, Reserved: 2; prijzen 0 € (8x), P.O.A. (3x), 80.000 € (1x).
  De lijst toont dus ook verkochte objecten (prijs 0 €) en projecten zonder prijs (P.O.A.).
- **Objectpagina:** https://www.costablancajaveaproperties.com/property/luxurious-villa-in-cumbre-del-sol-g-3516/
  (24-09-2026):
  - `<script type="application/ld+json">`: **niet aanwezig** (0 stuks, ook niet op homepage/lijst).
  - og-tags: `og:type=product`, `og:title="Luxurious villa in Cumbre del Sol"`, `og:description`, `og:image`,
    `og:url`, `og:site_name="Giuliano Villas"`, `og:locale=en_EN`, `og:image:width/height`. Geen prijs in og-tags.
  - In de HTML: **Ref. G-3516**, **prijs 1.150.000 €** (ook `<input name="precio" value="1150000">`),
    **bebouwd 215 m²** (`class="constru"`), **perceel 980 m²** (`class="parcela"`), 4 slaapkamers, 3 badkamers, zwembad.
    **Plaats:** verborgen veld `formvisitadatos` met JSON
    `{"id":"326629","titulo":"Luxurious villa in Cumbre del Sol","construido":"215.00","habitaciones":"4","precio":"1.150.000€","localizacion":"BENITACHELL"}`.
  - Het blok "Similar Properties" toont naast eigen `G-`-referenties ook referenties in ander formaat
    (`POA786804`, `HH1R8TTNT`): waarschijnlijk gedeelde objecten van andere kantoren **[te verifiëren]**.

## 5. Systeem achter de site

Geen van de bekende pakketten (Inmoweb, Mediaelx/LetsINMO, Sooprema, Inmovilla, Witei, WordPress). Aanwijzingen:
`<meta name="generator" content="Mattis-Framework 4.0">`, `<meta name="application-name" content="App-pagina-web-mattis">`,
JavaScript-aanroep `madstudio.ini()`, paden `/objetos/cache/giulianovillas/…`, `/core/objetos/js/…`,
`/imagenes/web/giulianovillas/…`, Spaanse class-namen (`PaginacionPaginas`, `fila precio`, `etiquetaprop`),
cookies `PHPSESSID` en `LANG`, server Apache. Conclusie: **eigen bouw / maatwerkframework "Mattis" van een Spaans
webbureau** (PHP). Of dit framework een exportfeed kent is onbekend **[te verifiëren]** — webzoeken was in deze sessie
niet beschikbaar.

## 6. Schatting aanbod en dekking Jávea/Benitachell/Moraira

- **Aantal:** 38 pagina's × 12 kaarten = **maximaal ~456 vermeldingen** in "Resales" (inclusief verkochte objecten en
  projecten zonder prijs); het werkelijke aantal te koop is lager en niet exact te tellen zonder de geblokkeerde
  vervolgpagina's. Nieuwbouwlijst niet geteld.
- **Dekking (steekproef 24-09-2026):** pagina 1 van de lijst: 8 van 12 in Jávea (Costa Nova, Cap Martí, Adsubia 3×,
  Avenida Augusta, Town, Covatelles), 0 Benitachell, 0 Moraira; overige: Jesús Pobre (Dénia), Benissa, Teulada,
  Els Poblets. Homepage-uitgelicht: 11 objecten, waarvan minstens 8 in Jávea en 1 in Cumbre del Sol (Benitachell).
  Samen 23 objecten, 17 in het doelgebied → **ruwweg twee derde tot driekwart**. Eigen omschrijving van de site:
  "specialized in JAVEA - MORAIRA - DENIA". Zoekfilter kent zones van Jávea (Arenal, Montgó, Tosalet, Balcón al Mar,
  Portichol, Cansalades enz.), Benitachell/Cumbre del Sol en Moraira (Moravit, Pla del Mar, San Jaime, Benimeit enz.).

## Advies: **lezen** (beperkt)

- Wél: objectpagina's `/property/...`, pagina 1 van `/properties/sell/all/`, `/properties/sell/work-new/` en de vier
  landingspagina's. Nieuwe objecten verschijnen op pagina 1, dus dagelijks pagina 1 lezen vangt nieuwe vermeldingen.
- Niet: vervolgpagina's (`/page/N/`), printversies, formulieren, galerij-modal.
- Tempo: **14 seconden** tussen verzoeken (Crawl-delay), eerlijke eigen User-Agent, geen browser nabootsen.
- Velden: prijs uit `input[name=precio]`, plaats/m²/kamers uit `formvisitadatos`, perceel uit `class="parcela"`,
  referentie uit de titel (`Ref: G-nnnn`). Referenties zonder `G-` zijn waarschijnlijk gedeelde objecten.
- Volledige dekking (alle ~450) is alleen netjes haalbaar via het kantoor zelf.

⏸️ ACTIE VOOR JAN: als je het hele aanbod wilt (niet alleen pagina 1), vraag Giuliano Villas om een feed of
samenwerking; het is een Jávea-kantoor met een groot eigen bestand. Beslis ook of dagelijks pagina 1 lezen volstaat.

## Opgehaalde pagina's (24-09-2026)

1. http://www.giuliano-villas.com/robots.txt (404) · 2. http://www.giuliano-villas.com/ (doorstuurpagina)
3. https://www.costablancajaveaproperties.com/robots.txt · 4. https://www.costablancajaveaproperties.com/
5. https://www.costablancajaveaproperties.com/sitemap.xml (404) · 6. …/property/luxurious-villa-in-cumbre-del-sol-g-3516/
7. …/properties/sell/all/ — steeds met minstens 2 s, op de echte site 14 s, tussenpauze; niet ingelogd, geen formulieren.

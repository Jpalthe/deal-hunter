# Sansy Villas Jávea — toets op automatisch lezen

- **Website:** https://www.sansyvillasjavea.com
- **Datum toets:** 24-09-2026 (23:37–23:40 CEST; servertijd 21:37–21:40 UTC)
- **Rechtspersoon:** Sansy Villas Jávea, S.L. — CIF B-54997077 — bron: https://www.sansyvillasjavea.com/privacidad (aviso legal, 24-09-2026)
- **Kantoor:** Ctra. Cabo de la Nao Pla 135, Local 12, 03730 Jávea (Alicante) — zelfde bron
- **Algemene contactkanalen:** info@sansyvillasjavea.com · telefoon staat op de aviso legal — zelfde bron
- **Opgehaalde pagina's (5, steeds ≥ 28 s ertussen):** `/robots.txt`, `/sitemap.xml`, één objectpagina (ref. JV1026),
  `/privacidad`, de aanbodpagina `buscar.php?o=Venta`. Daarnaast, buiten de makelaarssite, de startpagina's van
  inmobigrama.com en inmoserver.com om het systeem te herkennen.

## Advies: LEZEN

robots.txt staat het aanbod toe, de aviso legal verbiedt automatisch lezen niet, en de objectpagina's zijn gewone
server-gerenderde HTML met prijs, bouw- en perceeloppervlak, plaats, wijk en referentie als tekst. Er is geen
JSON-LD, dus er is een eigen parser nodig; de og-tags geven prijs, m² en slaapkamers alvast in één regel. Spelregels:

1. Nooit sneller dan één pagina per twee seconden (295 objectpagina's = ca. 10 minuten voor een volledige ronde).
2. Teksten en foto's **niet overnemen of publiceren**: de aviso legal eist voor reproductie, verspreiding en
   commercieel gebruik vooraf schriftelijke toestemming (zie punt 2). Intern lezen, vergelijken en scoren is wat anders.
3. Eigen, herkenbare User-Agent met contactadres gebruiken en niet één van de in robots.txt genoemde tools
   (wget, HTTrack, enz.) nabootsen.

## 1. robots.txt

- URL: https://www.sansyvillasjavea.com/robots.txt (HTTP 200, 24-09-2026, 1.194 bytes)
- Het blok voor iedereen luidt letterlijk:

```
User-agent: *
Disallow: /wp-content/cache
Disallow: /trackback
Disallow: /category/*/*
Disallow: /*/trackback
Allow: /wp-admin/admin-ajax.php
```

- Geen van die paden raakt het aanbod: de objectpagina's staan direct onder de root
  (`/Venta-Villa-Jávea-Xàbia-Montgó-811`) en de zoekpagina is `/buscar.php`. **Een `User-agent: *` mag het aanbod dus lezen.**
- Daarnaast expliciet `Allow: /` voor ChatGPT-User, GPTBot, **ClaudeBot**, PerplexityBot en Google-Extended.
- Een lang blok met ruim 40 downloadtools (HTTrack, wget, WebZIP, Teleport, Offline Explorer …) heeft **geen**
  Disallow-regel eronder; technisch dus geen verbod, maar de bedoeling is duidelijk: geen site-kopieertools.
- Twee eigenaardigheden: de paden zijn WordPress-paden terwijl de site geen WordPress is, en de regel
  `Sitemap: https://www.inmobiliaria7.es/sitemap.xml` wijst naar een **ander domein**. Het bestand is een
  hergebruikt sjabloon van de websitebouwer (niet opgehaald; ander domein, buiten scope).
- Geen `Crawl-delay`.

## 2. Gebruiksvoorwaarden (aviso legal)

- Er is één juridische pagina: https://www.sansyvillasjavea.com/privacidad (HTTP 200, 24-09-2026), met de ankers
  `#aviso-legal` en `#politica-cookies` in de voettekst. Geen aparte "condiciones"- of "terms"-pagina; ook niet in de sitemap.
- Kopjes: LSSI-identificatie, "Propiedad" (intellectueel eigendom), tratamiento de datos personales, ley aplicable y
  jurisdicción, cookiebeleid.
- **Geen expliciet verbod** op scraping, crawling, bots of automatisch lezen: de woorden scraping, robot, crawler,
  automatizado en base de datos komen op de pagina niet voor (gecontroleerd op de opgehaalde tekst, 24-09-2026).
- Wel een algemene auteursrechtbepaling (citaat, Spaans): "la reproducción total o parcial, uso, explotación,
  distribución y comercialización, requiere en todo caso de la autorización escrita previa por parte del RESPONSABLE".
  Ongeoorloofd gebruik geldt als "un incumplimiento grave de los derechos de propiedad intelectual o industrial".
- Conclusie: automatisch lezen is niet verboden; **overnemen** van teksten en foto's wel zonder toestemming.
- Contactformulieren hebben een captcha en een privacy-vinkje; niet gebruikt (geen formulieren, geen inlog).

## 3. Sitemap

- URL: https://www.sansyvillasjavea.com/sitemap.xml (HTTP 200, 742 kB, 24-09-2026). Gevonden op het standaardpad;
  de Sitemap-regel in robots.txt wijst zoals gezegd naar een ander domein.
- **303 URL's**, waarvan **295 objectpagina's** (patroon `/{Venta|Alquiler}-{Type}-{Gemeente}-{Wijk}-{id}`):
  - **288 te koop** (`Venta-…`)
  - 7 te huur (`Alquiler-…`: 5 Jávea, 1 Benitachell, 1 Moraira)
  - 8 overige: home, `quienes_somos`, `encuentranos`, `contactar`, `encargo_venta`, `valoracion_vivienda` en de twee
    zoekpagina's `buscar.php?o=Venta` / `?o=Alquiler`
- Elke URL heeft 16 `hreflang`-varianten via `?idioma=xx` (es, en, nl, de, fr, ru, pl, …) — dezelfde pagina, dus
  niet apart ophalen.
- `lastmod`: alle objecten staan op 22, 23 of 24-09-2026, steeds om 19:44:05 UTC — de sitemap wordt dagelijks
  opnieuw gegenereerd. Dat 279 van de 303 op 23-09 staan maakt onwaarschijnlijk dat `lastmod` de echte wijzigingsdatum
  van het object is; bruikbaarheid als wijzigingsdetector [te verifiëren]. Veiliger: de lijst met ID's dagelijks
  vergelijken (nieuw/verdwenen) en prijzen op de pagina's zelf controleren.

## 4. Aanbodpagina en één objectpagina

- **Aanbod te koop:** https://www.sansyvillasjavea.com/buscar.php?br=&o=Venta&check_tipo_inmueble%5B%5D=&p=&check_zona%5B%5D=&md=&pd=&ph=
  (HTTP 200, 24-09-2026; titel "Venta de inmuebles en Jávea"). 12 objecten per pagina, paginering via JavaScript
  (`pagina(2)` … `pagina(24)`): 24 × 12 = **288**, exact het aantal uit de sitemap. Voor het lezen is de sitemap
  makkelijker dan deze zoekpagina.
- **Bekeken object:** https://www.sansyvillasjavea.com/Venta-Villa-J%C3%A1vea-X%C3%A0bia-Montg%C3%B3-811
  (HTTP 200, 180 kB, 24-09-2026). Titel: "venta de villa en Jávea-Xàbia, Montgó Id:0104811".
- **JSON-LD (schema.org): NEE** — geen `<script type="application/ld+json">`, ook geen microdata (`itemprop`).
- **Open Graph: JA, beperkt** — `og:url`, `og:title`, `og:type` (website), `og:image` (foto op
  `www.inmoserver.com/fotos/1227/ir/811_….jpg`) en `og:description`:
  "Sansy Villas Jávea: venta de villa en Jávea-Xàbia, Montgó. 600 m2 , 5 dormitorios, 2.600.000 €".
  `meta description` is identiek. Geen `og:price`, geen canonical.
- Gegevens als gewone tekst in de HTML:
  - Prijs: **2.600.000 €**
  - Bouwoppervlak: **600 m²** ("600 m² construidos"; beschrijving: "casi 600 m², a los que se suman 476 m² de terrazas")
  - Perceel: **1.675 m²** ("1675 m² metros de parcela")
  - Kenmerkenregel: `600 m2 · 5 · 8 · 3 · sur` → 5 slaapkamers, vermoedelijk 8 badkamers en oriëntatie zuid
    (betekenis van het derde getal [te verifiëren])
  - Referentie: **JV1026** (kantoorreferentie); `Id:0104811` = kantoorcode 0104 + intern nummer 811 (ook in de URL)
  - Plaats en wijk: **Jávea-Xàbia, Montgó** — de wijk is een eigen veld in het URL-patroon (`…-Jávea-Xàbia-Montgó-811`)
  - Kaart via Leaflet; coördinaten niet als platte tekst in de HTML gevonden [te verifiëren]
  - Hypotheekrekenmodule (600/400/300 €, 291.200 €) — negeren bij het parsen
- Onder het object een blok met vergelijkbare woningen in Montgó (678, 222, 58, 893, 302).
- Opvallend: de beschrijving noemt het project "un proyecto exclusivo de InmoVillasJávea" — een **ander kantoor**
  (zie `site-inmovillasjavea.com.md`). Een deel van het aanbod lijkt dus gedeeld/samenwerkingsaanbod dat ook elders
  zichtbaar is [te verifiëren]; ontdubbelen op adres/wijk/prijs blijft nodig.

## 5. Systeem achter de site: Inmobigrama (niet in de standaardlijst)

Bewijs (24-09-2026, uit de HTML van de objectpagina en de dienstdomeinen):
- jQuery wordt geladen van `https://www.inmobigrama.com/js/jquery-3.6.3.min.js`
- Alle foto's staan op `https://www.inmoserver.com/fotos/1227/{ir|wm|nwm}/…` (kantoornummer 1227 bij die fotoserver)
- Eigen PHP-opzet: `buscar.php` met `check_tipo_inmueble[]` / `check_zona[]`, mappen `web_librerias/` (Bootstrap,
  Leaflet, photo-sphere-viewer, html2canvas) en `web_plantillas/formularios/…`, `web_plantillas/utilidades/captcha`,
  taalwissel via `?idioma=`, referentieformaat `Id:0104811`
- Cookies volgens het cookiebeleid: `PHPSESSID`, `XSRF-TOKEN`, `idioma`; geen Set-Cookie bij gewoon lezen
- Server: Apache, HSTS; geen "powered by"-regel, geen `generator`-meta
- https://www.inmobigrama.com (24-09-2026) presenteert zich als vastgoed-CRM met websites voor kantoren,
  portaalkoppelingen (Idealista, Fotocasa, Pisos.com) en een MLS; gevestigd in El Puerto de Santa María. Inmovilla
  wordt daar nergens genoemd. https://www.inmoserver.com toont alleen de naam "Inmoserver" — wie erachter zit
  [te verifiëren], maar het is de fotoserver van deze site.

Dus **niet** Inmoweb, Mediaelx, Sooprema, Inmovilla, Witei of WordPress (de WordPress-paden in robots.txt zijn
sjabloonresten). Inmobigrama levert portaalfeeds, dus een exportfeed voor derden bestaat in principe
[te verifiëren] — voor dit advies niet nodig, want lezen mag. De MLS-functie verklaart mogelijk het gedeelde aanbod.

## 6. Omvang en dekking Jávea / Benitachell / Moraira

Geteld op de gemeentenaam in de URL van de 288 te-koop-objecten in de sitemap (24-09-2026):

| Gemeente | Objecten | Aandeel |
|---|---|---|
| Jávea / Xàbia | 131 | 45 % |
| Benitachell (incl. Cumbre del Sol, Jazmines) | 27 | 9 % |
| Teulada-Moraira (Moraira 10 + Teulada 8) | 18 | 6 % |
| **Subtotaal doelgebied** | **176** | **61 %** |
| Calpe | 30 | 10 % |
| Dénia | 25 | 9 % |
| Pedreguer | 12 | 4 % |
| Benissa | 8 | 3 % |
| Pego, Altea (6 elk), El Verger (4), Ondara, Oliva (3 elk), Benidorm (2) | 24 | 8 % |
| Overig, 1 elk (Orba, Parcent, Senija, Benidoleig, Adsubia, Els Poblets, Castell de Castells, Vall, Xeresa, Daimús, Guardamar …) | 13 | 5 % |

- Geschatte omvang: **288 objecten te koop + 7 te huur = 295**, waarvan **176 (61 %) in Jávea, Benitachell of Moraira**.
- Type (te koop): villa 168 · appartement 38 · chalet 26 · casa 19 · **terreno 13 (12 in Jávea, 1 Benidoleig)** ·
  dúplex 6 · piso 5 · ático 4 · finca (rústica) 4 · local 2 · hotel 2 · bungalow 2 · gebouw 1.
- Prijzen op pagina 1 van het aanbod lopen van 180.000 € tot 1.695.000 €; het bekeken object zit op 2.600.000 €.
- Voor Deal Hunter het interessantst: de 12 Jávea-percelen (`Venta-Terreno-Jávea-Xàbia-…`, o.a. Costa Nova) en
  de 2 fincas rústicas (Jávea casco antiguo 904, Benitachell 1383).

## Aanbevolen leesstrategie

1. Eén keer per dag `/sitemap.xml` lezen (1 verzoek, 742 kB) en de lijst met object-ID's vergelijken met gisteren.
2. Nieuwe objecten en een dagelijkse steekproef (of alles: 295 × 2 s ≈ 10 min) ophalen met 1 verzoek per 2 s,
   herkenbare User-Agent en contactadres; `?idioma=`-varianten overslaan.
3. Velden uit de HTML: prijs (`2.600.000 €`-notatie), bouw-m² en perceel-m² uit de beschrijving/kenmerkenregel,
   slaap-/badkamers, referentie ("Referencia: JV1026"), gemeente en wijk uit de URL. `og:description` als snelle
   controle (m², slaapkamers, prijs in één regel).
4. Foto's niet downloaden; alleen de `og:image`-URL bewaren als verwijzing.
5. Ontdubbelen tegen inmovillasjavea.com en de portals: het aanbod is deels gedeeld.

## Verzoekenlog (servertijd UTC, 24-09-2026)

| # | URL | Tijd | HTTP |
|---|---|---|---|
| 1 | https://www.sansyvillasjavea.com/robots.txt | 21:37:33 | 200 |
| 2 | https://www.sansyvillasjavea.com/sitemap.xml | 21:38:01 | 200 |
| 3 | https://www.sansyvillasjavea.com/Venta-Villa-Jávea-Xàbia-Montgó-811 | 21:38:56 | 200 |
| 4 | https://www.sansyvillasjavea.com/privacidad | 21:39:30 | 200 |
| 5 | https://www.sansyvillasjavea.com/buscar.php?…o=Venta… | 21:40:26 | 200 |

Buiten de makelaarssite: https://www.inmobigrama.com/ en https://www.inmoserver.com/ (elk 1 verzoek, ter herkenning
van het systeem). Webzoekopdrachten waren in deze sessie niet meer beschikbaar; de systeemherkenning berust op de
technische sporen hierboven.

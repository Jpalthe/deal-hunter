# RANDOF Real Estate — www.randofrealestate.com

Toets op automatisch lezen · TREE Deal Hunter · datum: 24-09-2026

**Advies: lezen** — robots.txt staat een `User-agent: *` toe om de objectpagina's
en de sitemap te lezen, de voorwaarden verbieden automatisch lezen niet, en de
objectpagina's zijn gewone HTML met prijs, oppervlaktes, referentie en plaats in
vaste velden. Twee kanttekeningen: (1) de paginering van de zoekresultaten
(`&i=…&c=…`) is voor alle bots verboden, dus lees via **sitemap.xml** en niet
via de resultatenpagina; (2) de voorwaarden staan kopieën alleen toe voor
eigen, particulier gebruik — dus intern analyseren mag, teksten en foto's
opnieuw publiceren niet. Groot en relevant aanbod: 388 objecten in de sitemap,
waarvan 141 (36 %) in Jávea, Benitachell of Moraira.

## Kantoor

- Bedrijf: FERRANDO EXCLUSIVE RESIDENTIAL SL, handelsnaam Randof / RANDOF Real
  Estate (CIF B54734553). Bron: https://www.randofrealestate.com/lopd/ (24-09-2026)
- Kantoren (voettekst van https://www.randofrealestate.com/results/?id_tipo_operacion=1, 24-09-2026):
  - Dénia — Calle Diana 12 (fiscaal adres), 03700 Dénia · 965 036 919
  - Dénia — Calle Marqués de Campo 55, 03700 Dénia · 965 354 331
  - Jávea — Avenida de la Libertad 47, Bloque 5, 03730 Jávea · 965 769 558
- Algemeen e-mail: info@randofrealestate.com (uit de aviso legal)
- Doet verkoop, verhuur (`id_tipo_operacion=2`) en een derde categorie
  (`id_tipo_operacion=6`, waarschijnlijk nieuwbouw/promoties — niet geopend).
  Site in vijf talen: ES (root), EN (`/gb/`), DE, FR, NL (`/nl/`).

## 1. robots.txt — toegestaan, met uitzonderingen

Bron: https://www.randofrealestate.com/robots.txt (HTTP 200, `Last-Modified`
04-08-2026, opgehaald 24-09-2026). Het bestand is lang (5,1 kB): het blokkeert
eerst ruim 150 met naam genoemde bots volledig (`Disallow: /`), waaronder
SemrushBot, Bytespider, ahrefsbot, dotbot, Baiduspider, ia_archiver en de
downloadtools HTTrack, Wget/wget, WebCopier, WebZIP, Teleport, libwww, httplib,
lwp-trivial. Voor alle overige lezers staat er aan het eind:

```
User-agent: *
Disallow: /*?*modo=
Disallow: /*?*od=
Disallow: /*?*dt=
Disallow: /*?*i=
Disallow: /*?*c=
```

Uitleg: een `User-agent: *` mag alles lezen behalve URL's met een querystring
waarin `modo=` (weergave), `od=` (sortering), `dt=`, `i=` of `c=` voorkomt. Dat
raakt precies de resultatenpagina: de paginering daar werkt met `…&i=33&c=33`
(bladzijde 2), `&i=66&c=33` enz. — **verboden**. De objectpagina's
(`/…-es979975.html`), de categoriepagina's (`/villas-de-lujo-en-venta-6-1.html`)
en `/sitemap.xml` hebben geen querystring en zijn **toegestaan**. Ook de eerste
resultatenpagina `/results/?id_tipo_operacion=1` is toegestaan (geen van de vijf
parameters). Geen `Sitemap:`-regel. Let op: een eigen lezer moet zich niet als
wget, curl-achtige downloadtool of "httplib" melden; een neutrale User-Agent met
contactadres is verstandig. De server zit achter een BitNinja-WAF (header
`server: BitNinja-WafPro`), dus rustig blijven.

## 2. Voorwaarden — geen verbod op automatisch lezen gevonden

Bron: https://www.randofrealestate.com/lopd/ ("Avisos legales", HTTP 200,
24-09-2026). Eén pagina met de privacyverklaring, het aviso legal en de
gebruiksvoorwaarden (LSSICE). Doorzocht op scraping, robot, automat-, extrac-,
crawl, base de datos: geen enkele bepaling over automatisch lezen, bots of
databankrechten.

Wel relevant (parafrase, met één letterlijk citaat):

- Privacyverklaring, blok intellectueel eigendom: reproductie, kopie of
  wijziging van ontwerp en inhoud van de site is verboden (auteurs- en
  merkrecht).
- Aviso legal, punt 4 "Propiedad industrial e intelectual": citeren en
  verwijzen mag; een kopie van de inhoud maken mag "siempre y cuando, sea para
  su exclusivo y particular uso"; verspreiden of publiceren aan anderen vereist
  uitdrukkelijke toestemming.
- Punt 7 "Hipervínculos": de gebruiker verbindt zich de site of inhoud niet te
  reproduceren, ook niet via een hyperlink, zonder schriftelijke toestemming.

Conclusie: **geen verbod op scraping**; wel een gebruikelijk hergebruikverbod.
Intern lezen en analyseren voor Deal Hunter valt onder eigen gebruik; teksten,
foto's of complete objectbeschrijvingen mogen niet worden overgenomen in iets
wat naar buiten gaat. Foto's staan bovendien op Google Cloud Storage van
Inmoweb (`static.inmoweb.es/clients/2677/…`), niet op de eigen site.

## 3. Sitemap — aanwezig en compleet

- https://www.randofrealestate.com/sitemap.xml (HTTP 200, `application/xml`,
  312 kB, 24-09-2026). Geen sitemap-index, alles in één bestand; elke URL heeft
  `changefreq=daily`.
- Totaal **2186 URL's**: ES 453 · EN 447 · DE 431 · FR 431 · NL 424.
- Object-URL's: **1940** = **388 unieke objecten × 5 talen**. Patroon:
  `/casa-chalet-en-javea-…-con-piscina-es940632.html` (ES), `/gb/…-gb940632.html`,
  `/nl/…-nl940632.html`. Het getal is het Inmoweb-object-ID; de kantoorreferentie
  (LUX0065, CHA0087, PAR0070) staat alleen op de pagina zelf.
- Overige URL's: categoriepagina's per type × operatie (`…-en-venta-1-1.html`,
  `…-en-alquiler-1-2.html`, `…-6.html`), `/results/?id_tipo_operacion=1|2|6`,
  `/blog/…` (ca. 25 berichten), `/lopd/`, `/contact/`, `/aboutus/`,
  `/form_captacion/`, `/pages/servicios/`, `/pages/venda-su-casa/`.

Verdeling van de 388 objecten naar type (uit de ES-URL's): casa/chalet 154,
apartamento 87, villa de lujo 61, ático 29, parcela 20, casa adosada 14, casa de
campo 7, local 4, casa de pueblo 4, piso 2, estudio 2, solar urbano 1, garaje 1,
dúplex 1, bungalow 1.

## 4. Aanbodpagina en objectpagina

**Aanbodpagina (te koop):** https://www.randofrealestate.com/results/?id_tipo_operacion=1
(HTTP 200, 24-09-2026). Teller onderaan: "Mostrando 1 a 33 de 358" → **358
objecten te koop**, 33 per bladzijde, ca. 11 bladzijden. De bladzijden 2 t/m 11
gaan via `&i=33&c=33` … `&i=330&c=33` en zijn per robots.txt verboden; sortering
(`od=`) en weergave (`modo=`) ook. Daarom: objectlijst uit de sitemap halen.
Verschil sitemap (388) − te koop (358) = ca. 30 objecten verhuur/overig.

**Objectpagina:** https://www.randofrealestate.com/villa-de-lujo-en-javea-portichol-con-piscina-es979975.html
(HTTP 200, 100 kB, 24-09-2026). Server zet cookie `last_seen=979975`.

- `<script type="application/ld+json">`: **niet aanwezig** (0 blokken).
- og-tags: `og:type` = website, `og:title` = "Venta Villa de Lujo en Jávea,…"
  (afgekapt), `og:description` (begin van de tekst), `og:locale` = es,
  `og:url`, `og:image` (foto op static.inmoweb.es). **Geen** prijs, oppervlakte
  of referentie in og.
- In de zichtbare HTML wél alles, in vaste velden:
  - `Nº de referencia: LUX0065`
  - `<div class="precio">Precio: 3.995.000€`
  - `Sup. Construida 420 m²` · `Sup. Parcela 1605 m²`
  - `Habitaciones 4` · `Baños 5`
  - kenmerkenblok: `Provincia: Alicante · Población: Jávea · Zona: Portichol ·
    Tipo de obra: Obra Nueva · Certificación energética (consumo): B`
  - blok "Propiedades similares" met kaarten (`data-ref="CHA0087"`,
    `class="numeroRef"`), inclusief label "Vendido" — verkochte objecten blijven
    dus zichtbaar; bij het lezen op status filteren.
- Titelveld `<title>`: "Venta Villa de Lujo en Jávea, Portichol con Piscina".

Leesbaarheid: goed. Geen JavaScript nodig; alle waarden staan server-side in de
HTML met herkenbare labels en css-klassen (`precio`, `numeroRef`, `referencia`).

## 5. Systeem: Inmoweb

Aanwijzingen (objectpagina en resultatenpagina, 24-09-2026):

- css/js van `storage.googleapis.com/staticweb.inmoweb.es/web_framework/…`
  (`estructura_04/main.css`, `tema_1.css`) en `…/assets/template/cms/…`.
- Foto's en logo van `storage.googleapis.com/static.inmoweb.es/clients/2677/…`
  → Inmoweb-klantnummer **2677**.
- URL-patroon `-es<id>.html` / `-gb<id>.html` en `/results/?id_tipo_operacion=`,
  parameters `modo`, `od`, `i`, `c` — standaard Inmoweb-webframework.
- "inmoweb" komt 134× voor in de broncode; voettekst "Hecho con Software
  inmobiliario" (de gebruikelijke Inmoweb-vermelding).
- Hosting: Plesk (`x-powered-by: PleskLin`), PHP 8.3.33, Caddy als proxy,
  BitNinja-WAF. Geen WordPress, geen `wp-content`.

Inmoweb levert standaard XML-exportfeeds aan portalen; als lezen ooit
ongewenst blijkt, is "feed vragen" het alternatief.

## 6. Omvang en dekking Jávea / Benitachell / Moraira

Uit de 388 ES-object-URL's in de sitemap (plaatsnaam na "-en-"):

| Plaats | Objecten |
|---|---|
| Dénia | 141 |
| **Jávea** | **94** |
| **Benitachell (incl. Cumbre del Sol)** | **26** |
| **Moraira** | **21** |
| Pedreguer (o.a. La Sella) | 20 |
| Benissa | 20 |
| Finestrat, Ondara, Llíber, Calpe, Benidorm, Alfaz del Pi | 5–6 elk |
| Teulada | 4 |
| overige (Els Poblets, Altea, Pego, Oliva, La Xara, El Verger, …) | 1–4 elk |

**Jávea + Benitachell + Moraira = 141 van 388 (36 %)**; met Teulada 145 (37 %).
Jávea naar zone: Montañar II/Arenal/Cala Blanca 19, Montgó 13, Balcón al
Mar/Ambolo 11, Adsubia/Pinosol 10, Tosalet/Cap Martí 10, Montañar I 7, Costa
Nova/Granadella 6, La Lluca/golf 4, Portichol 3, Puerto/La Corona 3, centrum 1,
zonder zone 7.

Voor Deal Hunter relevant: 11 percelen in het doelgebied — Jávea 6 (Montgó ×3,
Balcón al Mar, Costa Nova, Puerto/La Corona), Moraira 2, Teulada 3.
Bijvoorbeeld https://www.randofrealestate.com/parcela-en-javea-montgo-javea-es1741039.html.

Schatting totaal aanbod: **ca. 360 te koop** (teller 358 op 24-09-2026), 388
objecten incl. verhuur in de sitemap; van de sitemap-objecten ligt ruim een
derde in Jávea/Benitachell/Moraira, het zwaartepunt ligt in Dénia.

## Aanpak voor de lezer

1. Elke dag `/sitemap.xml` ophalen; ES-URL's met `-es<id>.html` eruit filteren
   (388 stuks). Eén taal lezen — de NL-versie (`/nl/…-nl<id>.html`) bestaat ook
   voor alle 388, maar vijf talen lezen is vijfvoudige belasting zonder meerwaarde.
2. Alleen nieuwe of gewijzigde ID's openen; nooit sneller dan één pagina per
   twee seconden (388 pagina's ≈ 13 minuten bij een volledige ronde).
3. Uit de HTML halen: referentie, prijs, Sup. Construida, Sup. Parcela,
   Población, Zona, Tipo de obra, status (Vendido/Reservado).
4. Niet doen: bladeren via `&i=`/`&c=`, sorteren via `od=`, foto's downloaden,
   teksten overnemen naar buiten (voorwaarden punt 4 en 7).
5. Plan B: via de Jávea-vestiging een Inmoweb-XML-feed vragen — dat geeft ook
   de velden die de website niet toont.

## Opgehaalde pagina's (5 van 5, 24-09-2026, ≥ 2 s tussenpoos)

1. https://www.randofrealestate.com/robots.txt — 200
2. https://www.randofrealestate.com/sitemap.xml — 200
3. https://www.randofrealestate.com/lopd/ — 200
4. https://www.randofrealestate.com/results/?id_tipo_operacion=1 — 200
5. https://www.randofrealestate.com/villa-de-lujo-en-javea-portichol-con-piscina-es979975.html — 200

# RE/MAX Inmomás IV — www.remaxinmomas.es

Toets op automatisch lezen · TREE Deal Hunter · datum: 24-09-2026

**Advies: lezen** — robots.txt staat alles toe, er zijn geen gebruiksvoorwaarden
gevonden die automatisch lezen verbieden, de sitemap geeft alle 1.216
object-URL's kant-en-klaar, en de objectpagina's zijn gewone server-gerenderde
HTML met vaste labels. Twee kanttekeningen: (1) dit is de **groepssite van vier
RE/MAX-kantoren** (Elche, La Marina, Alicante Centro, Jávea) en het aanbod loopt
over de hele provincie — maar zo'n 8 % ligt in Jávea, Benitachell of Moraira,
dus filteren op plaats is nodig; (2) prijs en oppervlaktes staan alleen in de
zichtbare HTML, niet in JSON-LD of og-tags. Plan B: het systeem erachter is
Inmovilla, dat een exportfeed kent.

## Kantoor

- Rechtspersoon achter de site: GRUPO INMOMÁS, CIF B54829767, Calle Conrado
  del Campo 16, Elche (Alicante). Bron: https://www.remaxinmomas.es/politica-de-privacidad/ (24-09-2026).
- De site bundelt vier kantoren; het Jávea-kantoor is "RE/MAX Inmomás IV"
  (pagina `/el-grupo/agencia-inmobiliaria-javea-remax-inmomas-iv/`, niet
  opgehaald). Bron: page-sitemap.xml en het menu op de objectpagina (24-09-2026).
- Algemene contactkanalen: `/contacto/`, WhatsApp-knop op elke objectpagina,
  Facebook `inmomas.remax`, X `@remaxinmomas`, YouTube `@inmomasremax4747`
  (uit het Organization-blok in de JSON-LD). Telefoonnummer niet opgehaald.
- Naast verkoop ook verhuur en vakantieverhuur (menu "Servicio vacacional";
  minstens één Jávea-object is een winterverhuur okt 2026–mei 2027) en
  RE/MAX Commercial / Collection.

## 1. robots.txt — toegestaan

Bron: https://www.remaxinmomas.es/robots.txt (HTTP 200, 24-09-2026 21:22 UTC).
Volledige inhoud:

```
# START YOAST BLOCK
# ---------------------------
User-agent: *
Disallow:

Sitemap: https://www.remaxinmomas.es/sitemap_index.xml
# ---------------------------
# END YOAST BLOCK
```

Uitleg: `User-agent: *` met een **lege** `Disallow:` betekent dat alles mag,
ook `/propiedad/…` en `/propiedades/`. Het is de standaard-robots.txt van de
Yoast SEO-plugin. (De response draagt `X-Robots-Tag: noindex, follow`, maar dat
gaat over het indexeren van robots.txt zelf en zegt niets over lezen.)

## 2. Voorwaarden — niet gevonden

Gezocht op drie manieren, allemaal zonder resultaat:

- Voettekst en menu van de objectpagina: alleen links naar
  `/politica-de-cookies/` en `/politica-de-privacidad/`. Geen "Aviso legal",
  "Términos" of "Condiciones". De link "Departamento Legal"
  (`/servicios/departamento-legal/`) is een dienstenpagina, geen voorwaarden.
- page-sitemap.xml (27 pagina-URL's, 24-09-2026): geen aviso legal of
  condiciones.
- https://www.remaxinmomas.es/aviso-legal/ → **HTTP 404** ("Page not found",
  24-09-2026).

Privacyverklaring https://www.remaxinmomas.es/politica-de-privacidad/ (HTTP
200, 24-09-2026, ±14.000 tekens): standaard AVG-tekst. Geen enkele bepaling
over scraping, robots, automatisch lezen, databankrechten of hergebruik. De
enige treffers op "automatizadas" en "rastrear" gaan over profilering (AVG) en
over cookies (Complianz-tekst), niet over het lezen van de site.

Conclusie: verbod niet gevonden. Let wel: geen verbod is geen vrijbrief —
foto's en beschrijvingsteksten blijven auteursrechtelijk beschermd. Alleen
kengetallen overnemen (prijs, m², perceel, plaats, referentie, URL), geen
foto's of teksten kopiëren.

## 3. Sitemap — aanwezig, 1.216 object-URL's

- robots.txt wijst naar https://www.remaxinmomas.es/sitemap_index.xml (Yoast).
- De index (HTTP 200, 24-09-2026) bevat acht sitemaps: `post-`, `page-`,
  `nexora_property-` (2×), `nexora_agent-`, `category-`, `post_tag-`,
  `author-sitemap.xml`.
- Objecten: https://www.remaxinmomas.es/nexora_property-sitemap.xml (1.000
  URL's) + https://www.remaxinmomas.es/nexora_property-sitemap2.xml (216 URL's)
  = **1.216 object-URL's**, allemaal van de vorm
  `https://www.remaxinmomas.es/propiedad/<slug>/`.
- Alle `lastmod`-waarden liggen tussen 2026-09-24T03:00:31 en 03:01:05 UTC:
  het aanbod wordt elke nacht rond 03:00 in één keer opnieuw ingelezen. Wie
  de sitemaps ná 03:30 leest, heeft de dagstand.

## 4. Aanbodpagina en objectpagina

- Aanbodpagina: https://www.remaxinmomas.es/propiedades/ ("Listado de
  Propiedades"), plus een zoekpagina `/buscador/`. Niet opgehaald (budget);
  links komen uit het menu van de objectpagina.
- Geopende objectpagina (HTTP 200, 24-09-2026):
  https://www.remaxinmomas.es/propiedad/oportunidad-unica-para-inversores-gran-finca-de-2-600-m%c2%b2-en-el-tosalet-javea-a-minutos-de-la-playa-del-arenal/

Wat er op de pagina staat (zichtbare HTML, blok `nexora-single`):

| Veld | Waarde |
|---|---|
| Prijs | 830.000 € |
| Referentie | REF. 3009_031879 |
| Type | Casa (breadcrumb: Inicio › Venta › Casa › Jávea - Xàbia) |
| Bebouwd | 114 m² (tekst: "aprox. 115 m² construidos") |
| Perceel | Terreno 2.600 m² |
| Plaats | Partida Comunes-Adsubia, 03739, Jávea - Xàbia, Alicante (El Tosalet / Cap Martí) |
| Overig | 4 slaapkamers, 2 badkamers, bouwjaar 1983, "Entrar a vivir", energielabel G/G, 35 foto's |

- **JSON-LD**: één `<script type="application/ld+json">`, van Yoast: `WebPage`,
  `BreadcrumbList`, `WebSite`, `Organization`. Géén `RealEstateListing`,
  `Offer` of prijs. Dus wel aanwezig, maar niet bruikbaar voor objectgegevens.
- **og-tags**: `og:locale=es_ES`, `og:type=article`, `og:title` (= paginatitel),
  `og:description` (eerste regels van de beschrijving, afgekapt met
  `[&hellip;]`), `og:url`, `og:site_name`, `twitter:card`, `twitter:site`.
  Géén `og:image`, geen prijs.
- Conclusie: prijs, m², perceel, plaats en referentie zijn alleen uit de
  zichtbare HTML te halen. Dat is goed te doen: vaste CSS-klassen
  (`nexora-info-item`, `nexora-info-value`, `nexora-feature`), server-side
  gerenderd, geen JavaScript nodig, geen cookies gezet, geen botbescherming
  gezien (alle verzoeken HTTP 200 met een gewone browser-User-Agent).

Terzijde voor Deal Hunter: dit object is zelf een kandidaat — 2.600 m² in El
Tosalet, "en exclusiva" bij Inmomás IV, en de tekst noemt "posible segregación
futura de la parcela (sujeto a la aprobación de la normativa urbanística)"
[te verifiëren].

## 5. Systeem — WordPress met eigen plugin "Nexora", gevoed door Inmovilla

- `<meta name="generator">`: WordPress 7.1.2, Elementor 4.3.1 (+ Elementor
  Pro), Redux 4.5.15, Site Kit by Google 1.186.0. Thema: `hello-elementor`.
  Verder Yoast SEO 28.5, Complianz (cookies), GTranslate (machinale
  vertaling; de bronpagina is Spaans, `inLanguage: es`), Essential Addons,
  Safe SVG, HFCM. Bron: HTML van de objectpagina, 24-09-2026.
- Aanbod draait op een eigen plugin `/wp-content/plugins/nexora/` met de
  custom post types `nexora_property` en `nexora_agent` (zie sitemapnamen en
  16 verwijzingen in de HTML). Dit is geen bekend commercieel pakket
  (geen Inmoweb, Mediaelx, Sooprema, Witei).
- De data komt uit **Inmovilla**: alle 35 foto's staan op
  `https://fotos15.apinmo.com/…` (apinmo.com is de foto-CDN van Inmovilla) en
  de referentie `3009_031879` heeft het Inmovilla-formaat
  kantoornummer_objectnummer [te verifiëren]. De nachtelijke sync om 03:00
  past daarbij. Inmovilla kent een XML-/API-export naar portalen, dus een
  feed vragen is een reëel alternatief.
- Ook gezien: `www.fxdw.es` (2×, vermoedelijk de bouwer van de site) en
  `app.gestioncanal.com` (1×, onbekend). Server: Apache/Plesk, PHP 8.5.10.

## 6. Omvang en dekking Jávea / Benitachell / Moraira

Telling op de slugs van de 1.216 object-URL's (24-09-2026):

| Plaats in slug | Aantal |
|---|---|
| Jávea / Xàbia | 36 |
| Benitachell / Cumbre del Sol / Poble Nou | 48 |
| Moraira / Teulada | 13 |
| **Samen** | **97 (≈ 8 %)** |

Dit is een ondergrens: 269 slugs noemen geen plaats (bijv.
`villa-en-venta-…-2`); daarvan zal een deel ook in dit gebied liggen.
Realistische schatting: 8–12 % van het aanbod, ofwel 100–145 objecten.
Koop en huur zitten door elkaar in dezelfde sitemap (de breadcrumb
"Venta"/"Alquiler" op de objectpagina maakt het onderscheid).

Ter vergelijking, de grootste andere plaatsen in de slugs: Finestrat 95,
Torrevieja 77, Calpe 68, Elche 58, Alicante 37, Benidorm 37, Dénia 24,
Benissa 21, Altea 21. Typen (slugs): villa 233, apartamento 216, chalet 71,
piso 57, local 46, casa 45, terreno 39, solar 30, finca 30, parcela 28,
adosado 28.

## Aanpak als we gaan lezen

1. Elke dag ná 03:30 de twee `nexora_property-sitemap*.xml` ophalen (2
   verzoeken) en de URL-lijst vergelijken met gisteren: nieuw, weg, gewijzigd.
2. Slugs filteren op `javea|xabia|benitachell|cumbre-del-sol|poble-nou|moraira|teulada`;
   objecten zonder plaats in de slug alleen bij de eerste ronde openen om de
   plaats uit de breadcrumb te halen, daarna in een lijst bewaren.
3. Objectpagina's één per 2–3 seconden, met herkenbare User-Agent en een
   contactadres; alleen kengetallen opslaan, geen foto's of teksten.
4. Plan B (als de site wijzigt of het niet meer mag): Inmovilla-feed vragen
   bij het Jávea-kantoor — zie "⏸️ ACTIE VOOR JAN" hieronder.

⏸️ ACTIE VOOR JAN (optioneel): bij een goed contact met het Jávea-kantoor
vragen of ze hun Inmovilla-export (XML) willen delen; dat scheelt lezen en is
netter. Niet nodig om te starten.

## Verantwoording — wat is opgehaald

Alle verzoeken op 24-09-2026, elk in een aparte stap (ruim meer dan 2 seconden
ertussen), met een gewone browser-User-Agent aangevuld met
"TREE-DealHunter-check". Geen inlog, geen formulieren.

| # | URL | Soort | Status |
|---|---|---|---|
| 1 | /robots.txt | robots | 200 |
| 2 | /sitemap_index.xml | sitemap | 200 |
| 3 | /nexora_property-sitemap.xml | sitemap | 200 |
| 4 | /nexora_property-sitemap2.xml | sitemap | 200 |
| 5 | /propiedad/oportunidad-unica-…-el-tosalet-javea-…/ | HTML-pagina | 200 |
| 6 | /page-sitemap.xml | sitemap | 200 |
| 7 | /politica-de-privacidad/ | HTML-pagina | 200 |
| 8 | /aviso-legal/ | HTML-pagina (controle) | 404 |

Drie HTML-pagina's, binnen het budget van vijf; robots.txt en de vier
sitemap-bestanden zijn machinebestanden en apart geteld. Niet opgehaald:
homepage, aanbodpagina `/propiedades/`, cookiebeleid, kantoorpagina Jávea.

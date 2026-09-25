# Toets automatisch lezen — Moragues Pons Mediterranean Houses

- **Website:** https://www.moraguespons.com
- **Datum toets:** 24-09-2026 (avond, CEST)
- **Bedrijf (uit aviso legal + JSON-LD):** DESARROLLOS MORAGUES PUGA S.L., CIF B42634618, kantoor Avda. Ausias March 13, Local 4, 03730 Jávea. Algemene kanalen: info@moraguespons.es, +34 96 579 39 42. Talen: ES, EN, FR, DE, NL.
- **Verzoeken aan de site:** 5 (robots.txt, sitemap.xml, sitemap-es.xml, /aviso-legal/, één objectpagina), met minimaal 3 seconden ertussen (`curl --rate 20/m`). Niet opgehaald: de aanbodpagina /venta/ en /llms.txt (budget van vijf pagina's).

## Advies: **lezen** — met voorwaarden

robots.txt staat het toe, de voorwaarden verbieden automatisch lezen niet expliciet, en de objectpagina's zijn uitstekend leesbaar (volledige schema.org JSON-LD met prijs, m², perceel, plaats). Wel bevat het aviso legal een algemene clausule tegen kopiëren/reproduceren met commerciële doeleinden zonder toestemming. Daarom:

1. Alleen kerngegevens vastleggen (prijs, m², perceel, plaats, referentie, URL, datum) voor interne signalering — geen teksten of foto's overnemen of herpubliceren.
2. Tempo laag houden: één verzoek per 2–3 seconden, bij voorkeur 's nachts; de voorwaarden noemen "massaal verbruik van computerbronnen" expliciet als verboden.
3. Herkenbare user-agent met contactadres gebruiken.
4. ⏸️ ACTIE VOOR JAN (aanbevolen, niet verplicht): een korte, vriendelijke mail naar het kantoor dat TREE hun openbare aanbod automatisch volgt voor eigen zoekwerk, en of ze een feed/export hebben. Dat maakt de commerciële-reproductieclausule een non-issue en past bij een collega-makelaar in dezelfde plaats.

## 1. robots.txt

Bron: https://www.moraguespons.com/robots.txt — opgehaald 24-09-2026 21:16 UTC, HTTP 200, `Last-Modified: 04-05-2026`, 238 bytes, server LiteSpeed.

Volledige inhoud:

```
# LLM-friendly content summary available at:
# https://www.moraguespons.com/llms.txt

User-agent: *
Allow: /

User-agent: *
Disallow: /login/

User-agent: *
Disallow: /admin/*

Sitemap: https://www.moraguespons.com/sitemap.xml
```

**Oordeel: toegestaan.** `User-agent: *` mag alles lezen behalve `/login/` en `/admin/*`. De aanbodpagina's (`/venta/...`, `/alquiler/...`) vallen daar niet onder. Opvallend: de site verwijst zelf naar een `llms.txt` ("LLM-friendly content summary") — de eigenaar houdt dus bewust rekening met automatische lezers. Niet opgehaald (budget); aanrader voor de volgende ronde.

## 2. Gebruiksvoorwaarden (aviso legal)

Bron: https://www.moraguespons.com/aviso-legal/ — opgehaald 24-09-2026 (HTTP 200). Aparte pagina's bestaan ook voor /politica-privacidad/ en /cookies/ (staan in de sitemap, niet opgehaald).

- Het woord scraping, robot, crawler, "automatizado" of "extracción" komt **niet** voor. Automatisch lezen wordt dus niet expliciet verboden.
- Wel relevant (letterlijke citaten, Spaans):
  - Onder "Acceso y utilización", verboden gebruik b): "obstaculizar el acceso de otros usuarios al sitio web y a sus servicios mediante el consumo masivo de los recursos informáticos" → geen zware belasting; ons tempo van 1 per 2–3 s is daar ver van.
  - Verboden gebruik d): "Reproducir, copiar, distribuir, poner a disposición o de cualquier otra forma comunicar públicamente, transformar o modificar los contenidos, a menos que se cuente con la autorización del titular".
  - Onder "Propiedad intelectual": "Quedan expresamente prohibidas la reproducción, la transformación, la distribución y la comunicación pública […] de la totalidad o parte de los contenidos de este sitio Web, con fines comerciales, en cualquier soporte y por cualquier medio, sin la autorización […]".
  - Toegestaan: "Podrá visualizar los elementos del portal Web e incluso imprimirlos, copiarlos y almacenarlos […] siempre y cuando sea, única y exclusivamente, para su uso personal y privado."
  - Curiositeit: voor het plaatsen van een hyperlink naar de site vragen ze vooraf schriftelijke toestemming ("previamente deberán solicitar autorización por escrito").

**Oordeel: geen expliciet scraping-verbod**, wel een standaard IE-clausule tegen commerciële reproductie. Intern signaleren van prijs/m²/plaats is iets anders dan reproduceren of publiceren, maar het is een grijs gebied — vandaar de voorwaarden bij het advies.

## 3. Sitemap

- Index: https://www.moraguespons.com/sitemap.xml (814 bytes) → vijf taal-sitemaps: sitemap-es.xml, -en, -fr, -de, -nl.
- Geteld in https://www.moraguespons.com/sitemap-es.xml (HTTP 200, `Last-Modified: 14-09-2026`, 2,2 MB, met image-extensie: 12.479 afbeeldingsverwijzingen, allemaal op het eigen domein onder `/uploads/images/xxl/…`):
  - **1.075 URL's** in totaal.
  - Structuur: `/venta/<type>/<plaats>/<kenmerk>/` zijn filter-/landingspagina's (bijv. `/venta/villa-de-lujo/javea/piscina/`); individuele objecten staan direct onder `/venta/<slug-met-referentie>/` of `/alquiler/<slug>/`.
  - **575 verkoopobjecten** (URL's `/venta/<slug>/` zonder categorie-slug), waarvan 385 met een klassieke referentie aan het eind van de slug (V-, S-, A-, P-, LC-) en circa 190 nieuwbouw-units met projectcodes (bijv. `…-corinthia_7`, `…-eb1-29`, `…-unic_242e`, `…-puerto-de-javea-1-j`).
  - Verdeling van de 385 klassieke referenties: 183 V (villa), 83 S (perceel/solar), 79 A (appartement), 5 P (parking), 4 LC (bedrijfsruimte).
  - **64 huurobjecten** onder `/alquiler/<slug>/`.
  - Jongste `lastmod`-waarden: 11-09-2026 — de sitemap wordt actief bijgehouden.
  - Overige URL's: blogartikelen (bijna allemaal over Jávea), dienstenpagina's (compra-venta, invertir, personal shopper, marketing, proyectos, valoracion-vivienda), contact, aviso legal, privacy, cookies.
- Kanttekening [te verifiëren]: of de sitemap ook verkochte/ingetrokken objecten bevat, is zonder de aanbodpagina niet vast te stellen. De nieuwbouw-units tellen elk apart mee en blazen het aantal op; als "projecten" zijn het er hooguit een handvol.

## 4. Aanbodpagina en objectpagina

- **Aanbodpagina:** https://www.moraguespons.com/venta/ (staat in de sitemap en in de breadcrumb-JSON-LD van de objectpagina: "Venta" → `/venta/`; verder `/venta/villa/`, `/venta/villa/javea/`, `/venta/nueva-construccion/`, `/venta/javea/`). Niet opgehaald vanwege het paginabudget; de live teller is dus niet gezien.
- **Voorbeeld-objectpagina:** https://www.moraguespons.com/venta/villa-de-lujo-en-javea-v-364/ — opgehaald 24-09-2026 (HTTP 200, 638 KB html; CSS staat inline).
  - `<title>`: "Villa de lujo en Jávea - V-364"; canonical + hreflang naar vijf talen, NL-versie: https://www.moraguespons.com/nl/verkoop/luxevilla-in-javea-v-364/
  - **JSON-LD (2 blokken, geldige JSON):**
    1. `RealEstateAgent` (@graph): bedrijfsnaam, legalName, vatID, adres, geo-coördinaten, openingstijden, areaServed (Jávea/Xàbia, Moraira, Benissa, Calpe, Altea, Dénia, Costa Blanca), sameAs (Facebook, Instagram, LinkedIn, YouTube).
    2. `SingleFamilyResidence` + `BreadcrumbList`: `name` "Villa de lujo en Jávea", `additionalType` "Villa", `numberOfBedrooms` 4, `numberOfBathroomsTotal` 3, **`floorSize` 253 MTK (m²)**, **`lotSize` 1265 MTK**, `amenityFeature` (pool, garden, terrace, garage, heating), **`address.addressLocality` "Partida Comunes – Adsubia, Jávea/Xàbia"**, `image` (5 webp's), **`offers.price` 1315000 EUR**, `availability` InStock, `seller`/`broker` → organisatie. Breadcrumb: Venta → Villas → Jávea/Xàbia → Partida Comunes – Adsubia.
    - **Referentie:** V-364 staat in title, URL en in `data-property-ref="V-364"` op het formulier (plus intern `data-property-id="11"`), maar **niet** als apart JSON-LD-veld (geen `identifier`/`sku`). Uit de URL-slug te halen.
  - **og-tags:** og:url, og:type=website, og:title "Villa de lujo en Jávea", og:description (afgekapt na ~60 tekens), og:image (400×400-crop via `/imageurl-crop/…`), og:locale es_ES, og:site_name MORAGUESPONS, og:updated_time; twitter:card/title/description/image. Geen og:price — prijs alleen via JSON-LD of zichtbare tekst.
  - **Zichtbare tekst ter controle:** "1.315.000 € 253m2 1.265m2 4 Hab. 3 Baños", "REF. V-364", oriëntatie "Norte, Sur", bouwjaar 2008, "CEE: En trámite", "Ver 23 fotos". Ook een blok "Propiedades similares" met drie andere villa's (prijs, m², perceel).
  - Formulieren aanwezig (contact/afspraak/terugbellen) — niet gebruikt.

Conclusie: **JSON-LD ja, OpenGraph ja.** Voor Deal Hunter volstaat het uitlezen van blok 2 per objectpagina; alles wat we nodig hebben staat erin.

## 5. Systeem achter de site

**Eigen bouw (maatwerk)** — geen enkel kenmerk van Inmoweb, Mediaelx/LetsINMO, Sooprema, Inmovilla, Witei of WordPress (geen wp-content/wp-json, geen vendor-domeinen, geen "powered by"). Aanwijzingen:

- Alle assets op het eigen domein: één gebundeld script `/assets/js/js_property/1762188829.js` (Unix-tijdstempel als versienummer), losse libs `/js/noty.min.js`, `/js/sly.min.js`, `/js/widget-cita.js`, `/owl.carousel/…`, `/css/datepicker.min.css`; jQuery + Bootstrap-achtige classes, Magnific Popup, Font Awesome.
- Afbeeldingen onder `/uploads/images/{sm,lg,xxl}/2026/<nnn>/<slug>-<id>-<n>.webp` en een eigen crop-proxy `/imageurl-crop/400x400/80/<hash>/<base64-url>`.
- Eigen cookie-banner (`cookie_consent_alert`, cookies `cookie_consent_preferences`, `cookie_consent_alert_closed`, `previousUrl`), GA4 (`gtag`), Google Maps voor de kaart, geen externe CMP.
- Eigen endpoints: `/solicitar-llamada/`, sitemap-XSL `/sitemap.xsl`, `llms.txt`, per taal vertaalde slugs (`/en/for-sale/…`, `/nl/verkoop/…`).
- Een Engelstalig ontwikkelaarscommentaar in de HTML over de hero-layout en het watermerk — typisch voor maatwerk.
- Server: LiteSpeed, HTTP/2 + HTTP/3, lange cache-headers (6 maanden op robots/sitemap).

[te verifiëren] Het kan een white-label platform van een klein bureau zijn zonder zichtbare branding; dat verandert niets aan de leesbaarheid. Een exportfeed is er in elk geval niet zichtbaar — bij "feed vragen" zou dat dus een handmatige afspraak worden.

## 6. Omvang en dekking Jávea/Benitachell/Moraira

Op basis van de 575 verkoop-slugs in sitemap-es.xml (telling op plaatsnamen in de URL, 24-09-2026):

| Gebied | Aantal | Aandeel |
|---|---|---|
| Jávea/Xàbia (woord in slug) | 450 | 78% |
| Jávea-zones zonder het woord (Montgó, Arenal, Granadella, Balcón al Mar, Portichol, Tosalet, Adsubia, Cap Martí, Pinosol, Rafalet, La Nao, Puerto) | 27 | 5% |
| Benitachell / Cumbre del Sol / Poble Nou | 5 | 1% |
| Moraira / Teulada | 11 | 2% |
| Elders (Dénia, Benissa, Calpe, Altea, Pedreguer, Gata, Parcent, Llíber, Orba, Ondara, Pego, El Verger …) | 25 | 4% |
| Geen plaats in slug | 57 | 10% |

**Jávea + Benitachell + Moraira: minimaal 493 van 575 = 86%** (de 57 zonder plaatsnaam zijn waarschijnlijk grotendeels ook Jávea, gezien de rest). Huur: 42 van 64 in Jávea.

Voor Deal Hunter interessant: **83 percelen (S-referenties)** en een flink aantal oudere villa's (bouwjaren staan op de pagina), grotendeels in Jávea. Dit kantoor is een primaire bron voor de Jávea-markt.

## Wat is niet gedaan / open

- /venta/ (live aantal) en /llms.txt niet opgehaald — paginabudget van vijf.
- De NL-sitemap en NL-pagina's niet bekeken; slugs en JSON-LD zullen identiek van opbouw zijn (hreflang wijst 1-op-1).
- Niet gecontroleerd of de sitemap verkochte objecten bevat.
- Persoonsnamen die op de pagina staan (medewerker in het contactblok) zijn bewust niet overgenomen.

## Bronnen

- https://www.moraguespons.com/robots.txt (24-09-2026)
- https://www.moraguespons.com/sitemap.xml en https://www.moraguespons.com/sitemap-es.xml (24-09-2026)
- https://www.moraguespons.com/aviso-legal/ (24-09-2026)
- https://www.moraguespons.com/venta/villa-de-lujo-en-javea-v-364/ (24-09-2026)
- Ruwe bestanden van deze toets: `/private/tmp/claude-501/-Users-root-admin-tree-es/a3ae9710-3e66-42bb-b602-476120d4027d/scratchpad/moraguespons/` (tijdelijk, sessiegebonden)

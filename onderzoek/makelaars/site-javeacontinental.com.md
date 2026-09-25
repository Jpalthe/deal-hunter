# Jávea Continental — toets op automatisch lezen

- **Site:** https://www.javeacontinental.com
- **Bedrijfsnaam op de site:** INMOBILIARIA JAVEA CONTINENTAL
- **Kantoor (footer):** Avda. Rey Jaime 1º, núm. 11-B, 03730 Jávea (Alicante) · tel. (0034) 965 796 366 · info@javeacontinental.com
- **Datum toets:** 24-09-2026 (alle bronnen op die dag opgehaald, 5 verzoeken, 2 s ertussen)
- **Advies: LEZEN**

## 1. robots.txt — toegestaan

Bron: https://www.javeacontinental.com/robots.txt (HTTP 200, 292 regels, 24-09-2026)

Het bestand blokkeert ~140 met naam genoemde bots (o.a. SemrushBot, Bytespider, ahrefsbot,
dotbot, Baiduspider, wget, HTTrack, WebCopier, Teleport). Voor alle overige lezers geldt
alleen het laatste blok:

```
User-agent: *
Disallow: /*?*modo=
Disallow: /*?*od=
Disallow: /*?*dt=
Disallow: /*?*i=
Disallow: /*?*c=
```

Dus: aanbodpagina's en objectpagina's mogen gelezen worden. Alleen URL's met de
query-parameters `modo=`, `od=`, `dt=`, `i=` of `c=` (sorteer-, datum- en filtervarianten)
zijn uitgesloten. Er staat geen `Sitemap:`-regel en geen `Crawl-delay`.

Praktisch: gebruik een eigen, herkenbare User-agent (niet `wget`/`HTTrack`, die staan op naam
geblokkeerd) en blijf van de vijf parameters af. De server draait achter een BitNinja-WAF
(header `server: BitNinja-WafPro`), dus rustig lezen is nodig om niet geblokkeerd te raken.

## 2. Voorwaarden — geen verbod gevonden

Bron: https://www.javeacontinental.com/lopd/ (HTTP 200, titel "Avisos legales", 24-09-2026).
Dit is de enige juridische pagina waar de site naar linkt (footer "Avisos legales"; het
contactformulier noemt het "política de privacidad y normas de uso"). Daarnaast is er
`/cookie_policy/` (niet opgehaald).

De pagina bevat uitsluitend: bescherming van persoonsgegevens (LOPD 15/1999), rechten van
betrokkenen, doorgifte aan derden, externe links, toepasselijk Spaans recht, wijzigingen van
het privacybeleid en een cookie-alinea. Gezocht op scraping, robots, automatisch, extracción,
reproducción, base de datos, propiedad intelectual, prohibido, condiciones de uso: **nul
treffers**. Er zijn geen aparte gebruiksvoorwaarden (términos y condiciones) op de site.
Conclusie: de voorwaarden verbieden automatisch lezen niet.

## 3. Sitemap — 676 URL's, 49 objecten

Bron: https://www.javeacontinental.com/sitemap.xml (HTTP 200, 86.821 bytes, 24-09-2026)

- 676 URL's, verdeeld over 10 talen (es zonder prefix, gb, nl, de, fr, it, da, se, no, ru).
- 490 URL's zijn objectpagina's (patroon `...-<taal><id>.html`, bv. `-es175619.html`),
  dat zijn **49 unieke objecten × 10 talen**. Lees alleen de Spaanse (of Nederlandse) variant.
- Per taal 8 categoriepagina's te koop (`apartamentos-en-venta-1-1.html`, `bungalows-…-2-1`,
  `casas-chalets-…-3-1`, `casas-de-campo-…-16-1`, `estudios-…-4-1`, `locales-comerciales-…-10-1`,
  `parcelas-…-5-1`, `villas-de-lujo-…-6-1`), 1 huurcategorie, en `results/?id_tipo_operacion=1`
  (alles te koop) / `=2` (huur). Rest: home, blog, aboutus, contact, lopd, form_captacion, pages.
- Trefwoorden in URL's: venta 8, for-sale 8, te-koop 8, apartamento 28, villa 125, parcela 3,
  property 2.

Verdeling van de 49 objecten (op basis van de Spaanse URL's): 26 appartementen, 8 luxe villa's,
7 casa/chalet, 2 casas de campo, 2 percelen (Jávea, La Corona), 2 bedrijfsruimtes, 1 bungalow,
1 studio.

## 4. Objectpagina — geen JSON-LD, wel og:-tags en leesbare velden

Aanbodpagina: https://www.javeacontinental.com/results/?id_tipo_operacion=1
(parameter `id_tipo_operacion` valt niet onder de robots-uitsluitingen).

Voorbeeld: https://www.javeacontinental.com/casa-chalet-en-javea-tosalet-con-piscina-es175619.html
(HTTP 200, 24-09-2026)

- `<script type="application/ld+json">`: **niet aanwezig** (0 blokken). Microdata: alleen `itemprop="image"`.
- og:-tags: `og:type=website`, `og:title="Venta Casa / Chalet en Jávea,..."` (afgekapt),
  `og:description` (begin van de beschrijvingstekst), `og:locale=es`, `og:url`, `og:image`
  (foto op storage.googleapis.com/static.inmoweb.es/clients/429/property/175619/…).
  Geen prijs of oppervlakte in de og:-tags.
- Zichtbare HTML (wél gestructureerd, met vaste labels): "Nº de referencia: Jcc108 ·
  Precio: 1.348.000€ · Sup. Construida 400 m² · Sup. Parcela 1650 m² · Habitaciones 6 · Baños 4",
  plaats "Jávea, TOSALET". Let op: de interne id in de URL (175619) is niet de
  kantoorreferentie (Jcc108).
- hreflang-links naar alle 10 taalversies; cookie `last_seen=<id>` wordt gezet.
- Zoekfilter "Población" kent alleen España > Alicante > Jávea met wijken (Ambolo, Arenal,
  Capsades, Freginal, La Corona, La Guardia, Montañar I, Pinosol, Piver, Playa del Arenal,
  Puchol, Pueblo, Puerta Fenicia, Puerto, Tarraula, Thiviers, Tosalet, Vía Augusta).

## 5. Systeem: Inmoweb

Aanwijzingen (homepage en objectpagina, 24-09-2026):
- CSS/afbeeldingen op `storage.googleapis.com/static.inmoweb.es/clients/429/…` en
  `staticweb.inmoweb.es/web_framework/…` (klantnummer 429).
- Footer: "Hecho con Software inmobiliario" met link naar www.inmoweb.es.
- Inmoweb-typische paden: `/results/?id_tipo_operacion=`, `/form_captacion/`, `/lopd/`,
  categorie-URL's `-<type>-<operatie>.html`; robots-uitsluitingen `modo=`/`od=`/`dt=`/`i=`/`c=`.
- Hosting: Plesk, PHP 8.3, Caddy, BitNinja-WAF. Geen WordPress-sporen.

Inmoweb kent exportfeeds (XML) voor portalen; met maar 49 objecten is een feed vragen een
goedkoop alternatief, maar niet nodig.

## 6. Omvang en dekking

- Geschat aanbod: **49 objecten** (sitemap, 24-09-2026; mogelijk zit daar een enkele
  huurwoning bij, de URL toont de operatie niet).
- Ligging: **49 van 49 in Jávea** (100%). 0 in Benitachell, 0 in Moraira. De paginatitel van
  de home noemt "Javea, Denia, Moraira", maar het aanbod en het zoekfilter zijn puur Jávea.
- Voor de Deal Hunter interessant: 2 percelen (Jávea en La Corona), 7 chalets, 2 casas de campo
  en 8 luxe villa's; de rest zijn appartementen (vooral Puerto de Jávea en Arenal).

## Advies en leesrecept

**Lezen.** robots.txt staat het toe, de voorwaarden zeggen er niets over, de sitemap is compleet
en de objectpagina's zijn leesbaar via vaste labels in de HTML.

1. Lees `/sitemap.xml`, filter op `-es<cijfers>.html` (49 URL's).
2. Per object: prijs, Sup. Construida, Sup. Parcela, Habitaciones, Baños, Nº de referencia,
   wijk uit de titel; foto's uit og:image. Geen JSON-LD, dus parsen op de labels.
3. Nooit sneller dan één pagina per twee seconden; eigen User-agent; geen URL's met
   `modo=`, `od=`, `dt=`, `i=`, `c=`.
4. Nieuwe objecten herkennen: sitemap dagelijks vergelijken (changefreq staat op daily).

# Xàbiacasa (XABIACASA Mediterranean Properties) — toets op automatisch lezen

- Website: https://www.xabiacasa.com
- Kantoor: C/ Sant Agustí 3, 03730 Jávea (Alicante) — algemeen telefoonnummer en e-mail staan op de site (bron: https://www.xabiacasa.com/lopd/, 24-09-2026)
- Datum toets: 24-09-2026 (alle bronnen op deze datum opgehaald)
- Opgehaalde pagina's (5, telkens minimaal 2 seconden ertussen): robots.txt, sitemap.xml, /lopd/, /results/?id_tipo_operacion=1, één objectpagina

## Advies: LEZEN

robots.txt staat het toe, er zijn geen gebruiksvoorwaarden die het verbieden, en de objectpagina's zijn gewone server-gerenderde HTML met duidelijk gelabelde velden. Klein aanbod (19 objecten te koop), dus één keer per dag de sitemap lezen en de objectpagina's volgen is genoeg.

Spelregels bij het lezen:
1. Geen URL's met de parameters `modo=`, `od=`, `dt=`, `i=` of `c=` opvragen (die verbiedt robots.txt voor iedereen). Sorteer- en weergaveknoppen op de aanbodpagina gebruiken precies die parameters — dus niet aanklikken/volgen. De sitemap en de kale objectpagina's zijn voldoende.
2. Eigen, herkenbare User-agent gebruiken (bijv. `TREE-DealHunter/1.0 (+contact)`) — robots.txt blokkeert expliciet download-tools zoals wget, HTTrack, WebCopier, libwww en veel SEO-bots. De eigenaar wil duidelijk geen bulk-downloaders; niet onder zo'n naam of anoniem lezen.
3. Hooguit 1 verzoek per 2 seconden; de site draait achter een BitNinja-WAF (header `server: BitNinja-WafPro`), die snelle lezers blokkeert.

## 1. robots.txt

Bron: https://www.xabiacasa.com/robots.txt (HTTP 200, 290 regels, 24-09-2026)

De regel voor iedereen (`User-agent: *`) staat helemaal onderaan en verbiedt alleen vijf URL-parameters:

```
User-agent: *
Disallow: /*?*modo=
Disallow: /*?*od=
Disallow: /*?*dt=
Disallow: /*?*i=
Disallow: /*?*c=
```

Aanbodpagina's (`/casas-chalets-en-venta-3-1.html`, `/results/?id_tipo_operacion=1`) en objectpagina's (`/…-es1548786.html`) vallen daar niet onder: **toegestaan**.

Daarnaast staan er ruim 140 blokken die specifieke bots volledig uitsluiten (`Disallow: /`), onder meer SemrushBot, Bytespider, ahrefsbot, dotbot, Baiduspider, en download-tools: wget/Wget, HTTrack, WebCopier, WebStripper, WebZIP, Teleport, Offline Explorer, libwww, larbin, Xenu. Voorbeeld:

```
User-agent: HTTrack
Disallow:/
User-agent: wget
Disallow:/
```

Geen `Sitemap:`-regel, geen `Crawl-delay`.

## 2. Gebruiksvoorwaarden

- Enige juridische pagina in de voettekst: "Avisos legales" → https://www.xabiacasa.com/lopd/ (plus /cookie_policy/). Er is geen aparte pagina met términos/condiciones de uso gevonden; de voettekst linkt er niet naar en de sitemap bevat er geen.
- Inhoud van /lopd/: uitsluitend gegevensbescherming (LOPD 15/1999): welke persoonsgegevens uit de formulieren worden bewaard, rechten van betrokkenen, externe links, Spaans recht van toepassing, wijzigingen van het privacybeleid. Citaat van de kopjes: "Protección de datos de carácter personal", "Derecho de acceso, rectificación y cancelación", "Divulgación de la información a terceras partes", "Enlaces externos", "Cuestiones legales", "Cambios en la Política de Privacidad".
- **Geen enkele zin over automatisch lezen, scraping, hergebruik van aanbodgegevens of databankrechten.** De tekst is gedateerd (verwijst nog naar LOPD 1999, niet naar de AVG).
- Bij de formulieren staat "Acepto la política de privacidad y normas de uso de xabiacasa.com", maar die "normas de uso" verwijzen naar dezelfde /lopd/-pagina.

Conclusie: voorwaarden verbieden scraping niet (status: niet gevonden).

## 3. Sitemap

Bron: https://www.xabiacasa.com/sitemap.xml (HTTP 200, application/xml, 15,7 kB, 24-09-2026). Niet vermeld in robots.txt, wel op de standaardplek. Eén bestand, geen index.

- Totaal 140 `<loc>`-URL's.
- Objectpagina's: 48 = 24 Spaans (`/…-es<nummer>.html`) + 24 Engelse spiegels (`/gb/…-gb<nummer>.html`). Dus **24 unieke objecten** (koop én huur samen).
- Categorie/aanbodpagina's: 28 (14 per taal: 9 koopcategorieën, 3 huurcategorieën, 2 resultaatpagina's).
- Overig: home, blog (ca. 50 artikelen), /lopd/, /contact/, /aboutus/, /form_captacion/, /appointment.
- `changefreq` = daily op de aanbodpagina's.

Objectnummers in de URL (bijv. 1548786) zijn de interne Inmoweb-ID's; de zichtbare referentie is een eigen code (XC1447).

## 4. Aanbodpagina en objectpagina

Aanbodpagina te koop: https://www.xabiacasa.com/results/?id_tipo_operacion=1 (HTTP 200). Onderaan staat "Mostrando 1 a 12 de 19" → **19 objecten te koop**, 2 pagina's. Per kaart staan: soort, referentie, plaats, korte tekst, slaapkamers, badkamers, oppervlakte en prijs.

Objectpagina: https://www.xabiacasa.com/casa-chalet-en-javea-con-piscina-es1548786.html (HTTP 200, 74,6 kB)

- `<script type="application/ld+json">`: **niet aanwezig** (0 blokken). Ook geen microdata behalve `itemprop="image"`.
- og-tags: `og:type=website`, `og:title="Venta Casa / Chalet en Jávea con Piscina"`, `og:description` (eerste regels van de tekst), `og:url`, `og:image` (foto op storage.googleapis.com/static.inmoweb.es/clients/921/property/1548786/…), `og:locale=es`. Geen prijs of oppervlakte in de og-tags.
- `hreflang`: es + en (Engelse spiegel /gb/villa-in-javea-with-swimming-pool-gb1548786.html).
- In de zichtbare HTML (server-gerenderd, gelabelde velden onder "Detalle"): referentie **XC1447**, prijs **895.000 €**, Sup. Construida **340 m²**, Sup. Parcela **2900 m²**, 3 slaapkamers, 3 badkamers, Población **Jávea**, Provincia Alicante, Tipo de obra Segunda mano, energiecertificaat "TA" (in aanvraag), privézwembad, garage, gasverwarming. Ligging volgens de tekst: zone Montgó, 2 km van het centrum.
- Eigenschappen die het systeem kent en die voor deal-selectie nuttig zijn: tags "Oportunidad", "Ocasión", "Precio reducido", "De entidad financiera", "Reservado", "Vendido"; filter "Precio rebajado"; publicatiedatumfilter (48 h / 7 dagen / maand).

Bruikbaarheid: goed. Alles staat als gewone tekst met vaste labels in de HTML; geen JavaScript nodig.

## 5. Systeem achter de site: Inmoweb

Bewijs (24-09-2026, uit de opgehaalde HTML):
- Voettekst: `<a href="https://www.inmoweb.es/" title="Hecho con Inmoweb Software Inmobiliario">Software inmobiliario</a>`
- CSS: `//storage.googleapis.com/static.inmoweb.es/clients/921/css/main.min.css` en `staticweb.inmoweb.es/web_framework/…` → Inmoweb-klantnummer 921.
- Foto's: `static.inmoweb.es/clients/921/property/<id>/image/…`
- URL-patroon `/results/?id_tipo_operacion=1`, parameters `modo=`, `od=`, `dt=` en cookie `last_seen=<object-id>` — standaard Inmoweb-webframework.
- Badge "Member of" met `mls_member.png`: het kantoor zit in een MLS-samenwerking; een deel van het aanbod kan gedeeld aanbod van collega-kantoren zijn. Dedupliceren op referentie/adres tegen andere bronnen.
- Hosting: Plesk, Caddy, PHP 8.3, BitNinja-WAF.

Inmoweb kent een exportfeed (XML) voor portalen; mocht lezen ooit toch ongewenst blijken, is "feed vragen" het alternatief. Nu niet nodig.

## 6. Omvang en dekking Jávea / Benitachell / Moraira

- Te koop: 19 objecten (bron: "Mostrando 1 a 12 de 19", 24-09-2026). Te huur: 5 (24 unieke objecten in de sitemap min 19 koop; huurcategorieën: chalets, adosados, locales comerciales).
- Van de 24 unieke objecten in de sitemap liggen er volgens de URL 18 in Jávea, 2 in Benissa, 1 in Dénia (Les Marines), 1 in El Verger, 1 in Pedreguer, 1 in Teulada.
- Op pagina 1 van het koopaanbod (12 objecten): 8 Jávea, 1 Les Marines/Dénia, 1 Benissa, 1 El Verger, 1 Teulada. Prijzen van 2.000 € (weekaandeel in een resort, geen woning) tot 480.000 €; pagina 2 bevat de duurdere objecten (o.a. vier chalets met zwembad in Jávea, waaronder XC1447 à 895.000 €).
- Schatting Jávea-dekking van het koopaanbod: **circa 14–15 van de 19 (≈ 75 %)** — bijna alles Jávea, verder Marina Alta-dorpen. **Benitachell en Moraira: 0** gevonden objecten (Benitachell komt alleen voor in een leeg "Promociones"-zoekmenu; Teulada betreft het dorp, niet Moraira).
- Interessant voor Deal Hunter (pagina 1, 24-09-2026): XC5487 "Se vende NUDA PROPIEDAD … ideal para los inversores" (casa de campo Jávea, 338.000 €), XC1448 "A REFORMAR" (casa Seniola Jávea, 395.000 €), XC5499 casa de pueblo casco histórico Jávea 7 kamers 176 m² (339.000 €). Nog te toetsen [te verifiëren].

## Samenvatting voor de lezer-configuratie

| Onderdeel | Waarde |
|---|---|
| Startpunt | https://www.xabiacasa.com/sitemap.xml → alle `/…-es<id>.html` (alleen Spaanse versie lezen) |
| Aanbod te koop | https://www.xabiacasa.com/results/?id_tipo_operacion=1 (alleen zonder extra parameters) |
| Velden op objectpagina | Nº de referencia, Precio, Sup. Construida, Sup. Parcela, Habitaciones, Baños, Población, Tipo de operación, Tipo de obra, tags |
| JSON-LD / og-prijs | nee / nee — tekstvelden gebruiken |
| Verboden | URL's met `modo=`, `od=`, `dt=`, `i=`, `c=`; anonieme of tool-User-agents |
| Tempo | ≤ 1 verzoek per 2 s; ca. 25 verzoeken per dag volstaan |

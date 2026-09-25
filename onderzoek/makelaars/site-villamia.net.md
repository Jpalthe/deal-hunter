# VillaMia Real Estate S.L. — toets op automatisch lezen

- Website: https://www.villamia.net
- Datum toets: 24-09-2026
- Opgehaald: 5 pagina's (robots.txt, sitemap-index, verkoop-sitemap, één objectpagina, Aviso Legal), één per verzoek, ruim twee seconden ertussen. Geen inlog, geen formulieren.
- Kantoor (bedrijfsgegevens uit het Aviso Legal): VillaMia Real Estate S.L., CIF B70933429, Av. de la Llibertat 9H, 03730 Xàbia; tel. 96 579 4139; info@villamia.net.

## Advies: **feed vragen** (niet zelf scrapen)

robots.txt staat lezen toe, maar de gebruiksvoorwaarden verbieden het overnemen en hergebruiken van de inhoud voor commercieel of professioneel gebruik, tenzij de eigenaar toestemming geeft. Het aanbod is voor driekwart Jávea/Benitachell/Moraira (77 van 102 objecten), dus het kantoor is de moeite van een rechtstreekse vraag waard. Er is geen bekend exportsysteem (Inmoweb, Mediaelx, Sooprema) achter de site; of VillaMia een portaalfeed (XML) heeft die ze kunnen delen, is **[te verifiëren]** — dat is precies de vraag om te stellen.

## 1. robots.txt — toegestaan

Bron: https://www.villamia.net/robots.txt (24-09-2026). Volledige inhoud:

```
User-agent: *
Disallow: /wp-admin/
Allow: /wp-admin/admin-ajax.php

Sitemap: https://www.villamia.net/sitemaps.xml
```

`User-agent: *` mag alles lezen behalve `/wp-admin/`. De aanbodpagina's (`/property-sales/...`) zijn niet uitgesloten.

## 2. Gebruiksvoorwaarden — verbieden overnemen voor commercieel gebruik

Bron: https://www.villamia.net/aviso-legal/ (24-09-2026), "Condiciones Generales de Uso", punt 4 (Derechos de propiedad intelectual e industrial). Het woord "scraping" of "robot" komt niet voor, maar de strekking is duidelijk:

> "...quedando expresamente prohibidos al Usuario la reproducción, transformación, distribución, comunicación pública, puesta a disposición, **extracción, reutilización**, reenvío o la utilización de cualquier naturaleza, por cualquier medio o procedimiento, de cualquiera de ellos, salvo en los casos en que esté legalmente permitido o **sea autorizado por el titular** de los correspondientes derechos."

> "El Usuario podrá visualizar y obtener una copia privada temporal de los Contenidos para su exclusivo uso personal y privado ... **siempre que no sea con la finalidad de desarrollar actividades de carácter comercial o profesional.** El Usuario deberá abstenerse de obtener, o intentar obtener, los Contenidos por medios o procedimientos distintos de los que en cada caso se hayan puesto a su disposición..."

Conclusie: automatisch uitlezen voor TREE Deal Hunter (professioneel gebruik) is zonder toestemming van VillaMia niet toegestaan. Met toestemming wél ("autorizado por el titular"). Geschillen: rechtbank Dénia, Spaans recht.

## 3. Sitemap — 102 objecten te koop

- Sitemap-index: https://www.villamia.net/sitemaps.xml (24-09-2026) — verwijst o.a. naar `property_sale-sitemap1.xml`, `property_rental-sitemap1.xml`, `property_winterlet-sitemap1.xml` en `town_property_sale-sitemap1.xml`.
- Verkoop-sitemap: https://www.villamia.net/property_sale-sitemap1.xml (lastmod 23-09-2026): **103 URL's**, waarvan 1 de overzichtspagina en **102 objectpagina's**. Alle onder `/property-sales/<type>-in-<plaats>-for-sale-<referentie>/`. Oudste lastmod 31-05-2025, nieuwste 23-09-2026.
- Verdeling naar type (uit de URL-slug): villa 66, appartement 11, perceel 10, townhouse 7, penthouse 3, gedeeld eigendom villa 2, finca 1, duplex 1, commercieel 1.
- Alleen de verkoop-sitemap is opgehaald; verhuur en winterverhuur niet geteld.

## 4. Aanbodpagina en objectpagina — goed leesbaar, met JSON-LD en og-tags

- Aanbodpagina: https://www.villamia.net/property-sales/ (uit de sitemap en het menu "Sales"; niet apart opgehaald om binnen vijf pagina's te blijven).
- Objectpagina bekeken: https://www.villamia.net/property-sales/villa-in-javea-for-sale-vm-2951d/ (24-09-2026).

JSON-LD (`<script type="application/ld+json">`, `@type: RealEstateListing`) staat erop en bevat: naam "Villa in Jávea for sale VM 2951d", plaats Jávea (addressLocality) / Alicante / ES, prijs 949000 EUR (offers.price), woonoppervlak 286 m² (floorSize), perceel "1251 sq m" (additionalProperty "Plot Size"), 3 slaapkamers, 2 badkamers, foto-URL, datePosted "11th September 2026". De referentie zit alleen in de naam/URL, niet als apart veld.

Open Graph: og:title, og:description, og:url, og:image (1024x768), og:type=article, og:site_name=VillaMia, og:locale=en_GB; plus twitter:card. Geen prijs in de og-tags.

Zichtbare tekst op de pagina: "Reference VM 2951d · Town Jávea · Type Villa · Build 286 m² · Plot 1,251 m² · Orientation North-facing · Bedrooms 3 · Bathrooms 2 · 949,000 €". Canonical aanwezig, geen hreflang (vertaling via GTranslate).

## 5. Systeem achter de site — WordPress, eigen bouw (Oxygen)

Aanwijzingen (objectpagina en headers, 24-09-2026):
- `<link rel="https://api.w.org/" href="https://www.villamia.net/wp-json/">` en `?p=187449` shortlink → WordPress.
- Body-classes `single-property_sale postid-187449 wp-theme-oxygen-is-not-a-theme oxygen-body`; paden `/wp-content/themes/oxygen-is-not-a-theme/` → Oxygen Builder met een eigen custom post type `property_sale` (ook `property_rental`, `property_winterlet`).
- Plugins in de paden: `litespeed-cache`, `gtranslate`, `independent-analytics-pro`. Server LiteSpeed, QUIC.cloud-optimalisatie. Geen cookies gezet bij een gewone GET.
- Geen sporen van Inmoweb, Mediaelx/LetsINMO, Sooprema, Inmovilla, Witei of een bekende vastgoed-plugin (WPResidence, Houzez, Estatik, Property Hive).

Conclusie: eigen maatwerk op WordPress. Geen bekend standaard-exportkanaal; wel de gebruikelijke WordPress-REST-API (`/wp-json/`), maar die gebruiken valt onder hetzelfde verbod als scrapen.

## 6. Omvang en dekking Jávea/Benitachell/Moraira

Telling op plaatsnaam in de 102 object-URL's (24-09-2026):

| Plaats | Aantal |
|---|---|
| Jávea | 70 |
| Moraira | 4 |
| Benitachell | 3 |
| **Subtotaal doelgebied** | **77 (≈ 75%)** |
| Dénia | 13 |
| Gata de Gorgos | 3 |
| Teulada | 2 |
| Benissa | 2 |
| Calpe, Orba, La Nucía, Els Poblets, Llíber | 1 elk |

De footer bevestigt de focus: "rentals, sales and property management in Jávea, Moraira and Denia".

## ⏸️ ACTIE VOOR JAN

Wil je het aanbod van VillaMia in Deal Hunter, dan is de nette weg een korte vraag aan het kantoor (info@villamia.net / 96 579 4139): toestemming om het aanbod automatisch te lezen, of een XML-feed zoals ze die aan portalen leveren. Zonder dat akkoord blijft deze site buiten de automatische lezer.

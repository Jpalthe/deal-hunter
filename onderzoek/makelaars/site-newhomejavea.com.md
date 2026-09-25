# New Home Javea — toets op automatisch lezen

- **Site:** https://www.newhomejavea.com
- **Bedrijfsnaam (footer):** New Home Rentals & Sales
- **Kantoor (footer + aviso legal):** Ctra. del Cap de la Nau Pla / Avd. del Pla 126, kantoor 2.05, 03730 Xàbia (Alicante)
- **Algemene kanalen:** info@newhomejavea.com · +34 654 43 84 25 (WhatsApp) · 865 52 96 89 · ma–vr 9:30–17:30, za 10:00–13:00
- **Datum toets:** 24-09-2026 (vijf ophalingen, ruim twee seconden ertussen)
- **Advies:** **lezen** — toegestaan en technisch simpel, maar **lage prioriteit**: dit is een vakantieverhuurkantoor met op dit moment maar één woning te koop.

## 1. robots.txt — toegestaan

Bron: https://www.newhomejavea.com/robots.txt (24-09-2026, HTTP 200, Last-Modified 05-03-2025). Volledige inhoud, twee regels:

```
User-Agent: *
Sitemap: https://www.newhomejavea.com/sitemaps.xml
```

Geen enkele `Disallow`-regel. Een `User-agent: *` mag dus alles lezen, ook de aanbod- en objectpagina's.

## 2. Voorwaarden — geen verbod gevonden

Bron: https://www.newhomejavea.com/aviso-legal/ (24-09-2026, HTTP 200). De pagina bevat alleen de wettelijk verplichte identificatie van de verantwoordelijke (art. 10 LSSI: naam, NIF, adres, telefoon, e-mail) en verder niets — geen bepalingen over gebruik van de site, intellectueel eigendom, databankrechten, robots of scraping. (Persoonsgegevens van de verantwoordelijke bewust niet overgenomen.)

Niet gecontroleerd (buiten de limiet van vijf pagina's): `/condiciones-generales/`, `/politica-de-privacidad/`, `/politica-de-cookies/`. Op de objectpagina verwijst "Condiciones generales" naar het Avantio-script `verCondicionesGenerales.php`; dat zijn naar alle waarschijnlijkheid de **boekingsvoorwaarden** voor huurders, geen gebruiksvoorwaarden van de site [te verifiëren].

## 3. Sitemap — 25 objecten, waarvan 1 te koop

- Index: https://www.newhomejavea.com/sitemaps.xml (24-09-2026) → twee deelsitemaps:
  - https://www.newhomejavea.com/web-sitemap/sitemap.xml (statische pagina's; **niet opgehaald**)
  - https://www.newhomejavea.com/olb-sitemap/ (objecten; opgehaald 24-09-2026)
- De objectsitemap bevat **156 URL's**: 6 categoriepagina's (verhuur, per taal) en 150 objectpagina's in zes talen (es, en, nl, fr, de, ru).
- Uniek per referentienummer: **25 objecten**
  - 18 × `/alquiler/` (vakantieverhuur)
  - 6 × `/alquiler-larga-estancia/` (winter-/langetermijnverhuur)
  - **1 × `/venta/` (te koop)**
- URL's die op "venta/sale" matchen: 6 (= hetzelfde object in zes talen). Op "villa/apartamento/parcela/property/inmueble" matchen alleen verhuurobjecten.

## 4. Aanbodpagina en objectpagina

- **Aanbodpagina te koop:** https://www.newhomejavea.com/venta/ventas-d0/ (link "Ventas" in het menu; niet geopend).
- **Geopende objectpagina:** https://www.newhomejavea.com/venta/chalet-benitachell-casa-independiente-en-venta-en-cumbre-del-sol-690636.html (24-09-2026, HTTP 200, 115 kB)

**JSON-LD** (`<script type="application/ld+json">`, één blok): `@type: Product`; `name: "Casa independiente en venta en Cumbre del Sol"`; `offers: AggregateOffer, lowPrice 520000, priceCurrency EUR`; `geo: 38.7174578 / 0.165124`; `containsPlace: Benitachell`; `brand: "New Home Rentals & Sales For Sale"`; `identifier`, `sku`, `mpn` **leeg**; `image` (1 foto); `description` (volledige tekst, met daarin 912 m² perceel en 221 m² bebouwd).

**og-tags:** `og:title`, `og:description` (bevat "parcela de 912 m²" en "221 m² construidos"), `og:type = website`, `og:url`, `og:image` (650×450), plus twitter-tags.

**In de paginatekst:** 520.000 € · 221 m² Vivienda · 912 m² Parcela · 3 dormitorios · 3 baños · "Cumbres del Sol, Benitachell". Een expliciet referentieveld staat er **niet**; het nummer **690636** staat alleen in de URL.

Kanttekening: oppervlakte en perceel zitten níet als veld in de JSON-LD, alleen in de beschrijvende tekst en in het kenmerkenblok op de pagina. Een lezer moet dus prijs en plaats uit JSON-LD halen en m² uit de HTML.

## 5. Systeem achter de site — Avantio

Geen van de genoemde makelaars-CMS'en. De site draait op **Avantio** (vakantieverhuursoftware uit Valencia):
- footer: "Software de alquiler vacacional Avantio" met link naar avantio.com
- scripts/css van `crs.avantio.com`, `fwk.avantio.com`, `fw-scss-compiler.avantio.pro` (parameters `bk=bk_newhomejavea`, `urlOlb`; "OLB" = Avantio's online-boekingsmodule, vandaar `olb-sitemap`)
- eigen thema-bestanden onder `/child/...`; xajax en jQuery 3.4.1; cookie `PHPSESSID`
- Spaanse HTML-commentaren ("aquí se abre #centro")

Avantio kent kanaalkoppelingen en een API voor **verhuur**; een exportfeed voor verkoopobjecten is er, voor zover bekend, niet [te verifiëren]. "Feed vragen" is hier dus geen zinvol alternatief — en ook niet nodig, want lezen mag.

## 6. Omvang en dekking

- Circa **25 objecten** online, waarvan **1 te koop** (24-09-2026). De verkoopactiviteit is een bijzaak naast vakantieverhuur.
- Dekking Jávea/Benitachell/Moraira: **vrijwel 100 %** — 23 objecten met plaatsnaam Jávea in de URL, 1 Benitachell (Cumbre del Sol), 1 URL zonder plaatsnaam (`-711072.html`). Moraira komt niet voor.

## Advies voor de Deal Hunter

**Lezen, lage prioriteit.** robots.txt en de aviso legal staan het toe, de HTML is statisch (server-side gerenderd, geen inlog, geen JavaScript nodig om de gegevens te zien) en de sitemap geeft alle objecten met referentienummer. Praktisch: één keer per week `/olb-sitemap/` ophalen en alleen nieuwe `/venta/`-URL's openen — dat zijn per keer hooguit een paar pagina's. Het huidige verkoopobject (Cumbre del Sol, 520.000 €, 221 m² op 912 m², "gran potencial de reforma") is op zichzelf een kandidaat voor de renovatielijst.

Niet gedaan: de aanbodpagina en de web-sitemap zijn niet geopend, en de condiciones generales/privacyverklaring zijn niet gelezen (limiet van vijf pagina's).

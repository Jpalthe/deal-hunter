# Plots Direct S.L. — plotsdirect.com

Toets op automatisch lezen · 24-09-2026 (opgehaald 21:45–21:49 UTC) · TREE Deal Hunter

**Advies: lezen** — robots.txt staat alles uitdrukkelijk toe, er zijn geen gebruiksvoorwaarden die automatisch lezen verbieden, en de objectpagina's zijn gewone server-gerenderde HTML met vaste labels (h1, "Price:", "Location:", "Plot area:"). De sitemap geeft de complete lijst objectpagina's. Wel netjes: één pagina per twee seconden en een herkenbare user-agent. Voor Deal Hunter extra interessant: 64 van de 115 objecten zijn **bouwpercelen**, 82 liggen in Jávea.

Vijf pagina's opgehaald (het maximum): robots.txt, homepage, sitemap.xml, `/privacy` en één objectpagina. Niet geopend: de aanbodlijst `properties-for-sale---21866`, `/contact`, `/sitemap_index.xml`.

## 1. robots.txt — bestaat, staat alles toe

- Bron: https://plotsdirect.com/robots.txt → HTTP 200 (24-09-2026). Volledige inhoud, twee regels:

```
User-agent: *
Allow: /
```

- Geen `Disallow`, geen `Crawl-delay`, geen `Sitemap:`-regel. Voor `User-agent: *` mogen dus alle aanbod- en objectpagina's gelezen worden.

## 2. Gebruiksvoorwaarden — niet gevonden; alleen een privacyverklaring

- Op de homepage en op de objectpagina staan in kop-, menu- en voettekst geen links naar "terms", "legal notice", "aviso legal", "disclaimer" of "condiciones". De voettekst bevat alleen: "Plots Direct S.L. - Privacy Policy - Contact us" (24-09-2026).
- Bron privacy: https://plotsdirect.com/privacy → HTTP 200 (24-09-2026). Kop: "Plots Direct website privacy and cookie information". Inhoud: AVG-verklaring (welke gegevens verzameld worden, bewaartermijn, rechten, cookies, Google Analytics, links naar derden). Geen enkele zin over scraping, robots, crawlers, automatisch lezen, auteursrecht, databankrecht of licenties — de trefwoorden scrap/robot/crawl/automat/reproduc/copyright/licen komen niet in de tekst voor.
- Conclusie: **geen verbod gevonden**; er zijn geen voorwaarden die het gebruik van de site regelen. Wie het formeel zeker wil weten kan het kantoor vragen via de contactpagina `/contact`.

## 3. Sitemap — aanwezig, 1.332 URL's, waarvan 115 objectpagina's

- Bron: https://plotsdirect.com/sitemap.xml → HTTP 200, `application/xml`, 174 kB, `last-modified: 17-09-2026` (24-09-2026). Geen sitemap-index; alle URL's staan in één bestand met `<lastmod>2026-09-17</lastmod>`.
- Totaal **1.332 URL's**. Verdeling:
  - **115 objectpagina's** met patroon `/<id>-<type>-for-sale-<plaats>`, bv. `/8-plot-for-sale-javea-xabia-alicante`. ID's lopen van 2 tot 1998.
  - **115 printversies** `/print-<id>` (PDF-weergave van dezelfde 115 objecten; één-op-één overlap).
  - **ca. 1.100 lijst-/filterpagina's**: gepagineerde zoekresultaten met de filters in de slug, bv. `/properties-for-sale-0-0-0-0-0-0-0---3`, `/javea-xabia-property-for-sale-19-3-21866-0-0-0-0-0-0`, `/plots-for-sale-spain-…`, `/valencian-community-property-for-sale-19-…`. Die zijn voor ons ruis.
- Telling op de gevraagde trefwoorden (in de URL, hoofdletterongevoelig): "property" 507, "villa" 130, "apartment" 17, "finca" 16, "land" 5, "townhouse" 1; "venta", "inmueble", "apartamento" en "parcela" 0 (de site is Engelstalig). "plot" komt in álle 1.332 URL's voor omdat het in de domeinnaam zit — die telling zegt niets. De bruikbare telling is de 115 objectpagina's hierboven.
- Objectpagina's per type: perceel (plot) 64 · villa 33 · hotel 6 · ligplaats jachthaven 6 · bedrijfspand 3 · appartement 2 · finca 1.

## 4. Aanbodpagina en objectpagina

- Aanbodpagina (menu-link "property for sale in Javea"): https://plotsdirect.com/properties-for-sale---21866 (21866 lijkt de plaatscode van Jávea; ook `/javea-property-for-sale-19-3-21866-0-0-0-0`). Niet geopend vanwege het paginabudget; de sitemap dekt de objecten al.
- Objectpagina geopend: https://plotsdirect.com/8-plot-for-sale-javea-xabia-alicante → HTTP 200, 18 kB (24-09-2026).

**JSON-LD** (`<script type="application/ld+json">`): **geen**, ook niet op de homepage. Ook geen microdata (`itemprop` komt 0 keer voor). Wel een verouderde Google-RDFa-kruimelpad (`typeof="v:Breadcrumb"`): Spain › Valencian Community › Alicante › Javea / Xàbia › Plots › Ref:PDVAL3722.

**og:-tags**: **geen** (ook geen twitter:-tags, geen canonical). Alleen `<title>` "Javea / Xàbia plot for sale Alicante PDVAL3722" en een `<meta name="Description">` met één zin beschrijving plus het algemene telefoonnummer van het kantoor.

**Wat er wél in de gewone HTML staat** (vaste labels, makkelijk te lezen):

| Veld | Waar in de HTML | Waarde op de voorbeeldpagina |
|---|---|---|
| Titel + type + plaats + referentie | `<h1>` | Plot For Sale in Javea / Xàbia, Alicante (PDVAL3722) |
| Prijs | `<h3>Price: …</h3>` | € 450.000 |
| Referentie | in h1, title en kruimelpad "Ref:" | PDVAL3722 |
| Plaats / zone | `<p>Location: …</p>` in `div#txt` | Tossals (Jávea) |
| Perceel | `<li>Plot area: …</li>` | 1.530 m² |
| Woonoppervlakte | n.v.t. (perceel); bij villa's naar verwachting een eigen `<li>` [te verifiëren] | — |
| Afstanden | `<li>` Beach / Shops / School / Golf / Town / Marina | 4 km / 1 km / 2 km / 5 km / 1 km / 4 km |
| Kenmerken | `<h4>Property Features</h4>` + `<ul>` | South facing, Completely flat, No cables overhead, Road to road plot |
| Beschrijving | `<p>`'s in `div#txt` | vrije tekst (uitzicht Montgó, water en stroom aan de perceelgrens, ligging Tossals-weg) |
| Foto's | `pics/<id>/<id>a.jpg` … | 3 foto's |
| PDF | link `print-8` ("Download plot PDVAL3722 as a PDF document") | — |

Op de pagina staan drie formulieren (één aanvraagformulier "Enquire on reference", twee zoekformulieren). Niet gebruikt en niet nodig: alle gegevens staan in de HTML.

## 5. Systeem achter de site — eigen bouw

Aanwijzingen (24-09-2026):
- Eén css- en één js-bestand met eigen naam: `structure/plotsd.css?1677507745` en `structure/plotsd.js?1639054512` ("plotsd" = Plots Direct). Foto's in `pics/<object-id>/`, iconen in `images/`, homepagefoto's in `build/`.
- Cookies: `SESSIONID` (sessie) en `PD2013` (persistent, één jaar, versleutelde waarde; "PD" = Plots Direct). Server: Apache. Geen `x-powered-by`.
- Geen `generator`-meta, geen HTML-commentaar, geen "powered by", geen `wp-content`/`wp-json`, geen sporen van Inmoweb, Mediaelx/LetsINMO, Sooprema, Inmovilla of Witei.
- Eigen URL-schema waarin de zoekfilters als cijferreeks in de slug staan (`…-19-3-21866-1-0-0-0-0-0-0`), eigen referentieformaat `PDVAL####`, valutakiezer met 16 munten, vertalingen via Google Translate-links, jQuery, Google Analytics.

Conclusie: **eigen bouw** (klassieke PHP/Apache-site, ontwerp uit de periode 2013–2023 gezien de tijdstempels). Dus geen standaard exportfeed om te vragen; wel bruikbaar: de sitemap als objectlijst en de `print-<id>`-PDF per object.

## 6. Omvang en dekking Jávea / Benitachell / Moraira

- Geschat aanbod: **115 objecten** (telling uit sitemap.xml van 17-09-2026). De homepage spreekt zelf van een "extensive portfolio of property for sale in Javea and neighbouring towns" en meldt "Established in Javea in 2003" en "designed and built 48 villas on its plots" [te verifiëren — eigen claim van de site].
- Ligging volgens de plaats in de URL: **Jávea/Xàbia 82 · Moraira 7 · Benitachell 4 = 93 van 115 (81 %)**. Rest: Alicante-stad 5, Dénia 3, Calpe 2, Villajoyosa 2, Marbella 2, en één in Xaló, Benissa, Jesús Pobre, Beniarbeig, La Nucía, Barcelona, Ibiza en Sotogrande.
- Voor Deal Hunter: 64 percelen, waarvan het merendeel in Jávea. Dit is het meest perceel-gerichte kantoor tot nu toe in dit onderzoek.

## Praktisch voor het leesscript

1. Lees `https://plotsdirect.com/sitemap.xml` en houd alleen URL's over die na de domeinnaam met `<cijfers>-` beginnen (115 stuks). Sla `print-<id>` en alle filterpagina's over.
2. Per objectpagina: h1 (type, plaats, ref), h3 "Price:", `p` "Location:", `li` "Plot area:" (en bij villa's de overige `li`-regels), `h4 Property Features` + lijst, alinea's in `div#txt`.
3. Tempo: één pagina per twee seconden → 115 pagina's in ca. 4 minuten. Herkenbare user-agent met contactadres.
4. Controle: vergelijk het aantal objecten op de aanbodlijst `properties-for-sale---21866` met de 115 uit de sitemap; de sitemap is een week oud en kan nieuwe objecten missen [te verifiëren].
5. Kantoorgegevens (zonder persoonsnamen): Plots Direct S.L., Jávea, contact via `/contact`.

Bronnen: https://plotsdirect.com/robots.txt · https://plotsdirect.com/ · https://plotsdirect.com/sitemap.xml · https://plotsdirect.com/privacy · https://plotsdirect.com/8-plot-for-sale-javea-xabia-alicante — alle opgehaald 24-09-2026.

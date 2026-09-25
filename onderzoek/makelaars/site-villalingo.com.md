# Villa Lingo Real Estate — toets op automatisch lezen

Datum toets: 24-09-2026 · Site: https://www.villalingo.com · Kantoor: grupo Villa Lingo S.L, Camí dels Lladres 5, 03700 Dénia (bron: https://www.villalingo.com/disclaimer, 24-09-2026). Algemene kanalen: +34 660 360 685, info@villalingo.com (zelfde bron). Taalversies: es.villalingo.com en fr.villalingo.com (bron: homepage, 24-09-2026).

Opgehaald (5 pagina's, meer dan twee seconden tussen elk verzoek): robots.txt, sitemap.xml, homepage, /disclaimer, /property-833. Niets anders geopend.

## Advies: LEZEN — met twee kanttekeningen

Automatisch lezen mag (robots.txt staat alles toe, de voorwaarden verbieden niets) en de objectpagina's zijn leesbaar. Maar: de sitemap is onbruikbaar en lijkt op een gehackte site te wijzen, en er staat geen gestructureerde data (JSON-LD) op de pagina's. Een lezer moet dus de HTML-tekst zelf uitpluizen en mag de sitemap niet als bron gebruiken.

## 1. robots.txt — toegestaan

Bron: https://www.villalingo.com/robots.txt (24-09-2026, laatst gewijzigd 21-07-2026 volgens de server). Letterlijk:

```
User-agent: *
Allow: /
Sitemap: https://www.villalingo.com/sitemap.xml
Sitemap: https://www.villalingo.com/sitemap813.xml
… (nog 19 genummerde sitemap-bestanden: sitemap795, 689, 276, 444, 457, 290, 836, 796, 254, 698, 712, 571, 750, 679, 243, 558, 478, 518, 749)
```

`User-agent: *` mag dus alles lezen, ook de aanbodpagina's. Er staat geen Disallow en geen Crawl-delay. De 20 genummerde sitemap-bestanden zijn verdacht (zie punt 3); die heb ik niet geopend.

## 2. Voorwaarden — geen verbod gevonden

De site heeft geen aparte "terms"- of "aviso legal"-pagina. De contactformulieren verwijzen met "general conditions of use" naar /disclaimer (bron: HTML van https://www.villalingo.com/property-833, 24-09-2026). Die pagina (https://www.villalingo.com/disclaimer, 24-09-2026) bevat vijf kopjes: Accuracy of Information, External Links, Limitation of Liability, Changes to the Website, Contact Information. Kern van de strekking: de informatie is alleen ter algemene informatie, zonder garantie op juistheid; gebruik is op eigen risico; het kantoor is niet aansprakelijk voor schade door gebruik van de site. Nergens een verbod op automatisch lezen, scraping, bots, hergebruik of databankrechten.

Niet geopend (budget van vijf pagina's op): /privacy-policy-cookies. Dat is een privacy- en cookiepagina (TermsFeed-cookiebanner); de kans dat daar een scrapingverbod staat is klein, maar het is niet gecontroleerd. [te verifiëren]

## 3. Sitemap — gevonden, maar onbruikbaar (waarschijnlijk spam-injectie)

Bron: https://www.villalingo.com/sitemap.xml (24-09-2026). 1.902 URL's, allemaal met lastmod 2026-09-25. Daarvan:
- 1 echte pagina: de homepage;
- 874 URL's van het type `/?q=i6m6m8e6c9h8a4n6i1c7al`;
- 647 URL's onder `/shops/…`;
- de rest paden van willekeurige Engelse woorden plus een cijferreeks, zoals `/tarrace/duplexer/6334893581`.

Aantal URL's dat op een object lijkt (venta, property, inmueble, villa, apartamento, parcela, plot, sale): 0. Geen enkele `/property-NNN`-pagina en geen enkele aanbodpagina staat in de sitemap.

Dit patroon (gegenereerde spam-URL's, tientallen genummerde sitemap-bestanden in robots.txt) is kenmerkend voor een SEO-spam-injectie op een gehackte site. De homepage, de disclaimer en de objectpagina die ik las bevatten die spam-inhoud niet (gecontroleerd op dezelfde patronen: 0 treffers). Of de site werkelijk gecompromitteerd is, kan ik van buitenaf niet met zekerheid zeggen. [te verifiëren]

Gevolg voor ons: de sitemap nooit als bron gebruiken; objecten uitsluitend vinden via de aanbodpagina's (punt 4).

## 4. Aanbodpagina en objectpagina

Aanbod (gevonden in de navigatie op de homepage, 24-09-2026, zelf niet geopend):
- https://www.villalingo.com/properties-for-sale-in-costa-blanca (alles)
- per plaats: https://www.villalingo.com/buy-property-on-the-costa-blanca/property-for-sale-in-javea, …/property-for-sale-in-benitachell, …/property-for-sale-in-moraira, …/property-for-sale-in-denia, …/property-for-sale-in-benissa, …/property-for-sale-in-altea
- selecties: …/featured-properties-for-sale-on-the-costa-blanca, …/properties-for-sale-in-costa-blanca-under-200-000eur, …/luxury-properties-for-sale-in-northern-costa-blanca

Objectpagina's hebben het patroon https://www.villalingo.com/property-NNN (NNN = referentienummer).

Geopend: https://www.villalingo.com/property-833 (24-09-2026).
- JSON-LD (`<script type="application/ld+json">`): **geen** op de objectpagina. (De homepage heeft er wel twee: een ImageObject en een LocalBusiness met lege adresvelden — niets over objecten.)
- og-tags: alleen `og:image` (foto uit /thumbnails/800x600/uploads/photos/properties/1015/…). Geen og:title, og:description, og:price of description-meta.
- Canonical wijst fout naar de homepage (`http://www.villalingo.com`), dus daar valt niets uit te halen.
- In de zichtbare HTML-tekst staat wél alles: titel "Versatile 4-Bedroom Villa with Montgó Views & Dual Living Spaces – Javea", plaats "Javea, Covatelles", prijs 779 998€ ("Fees charged to the seller"), bouwoppervlak 270m², perceel 1 000m², 4 slaapkamers, 3 badkamers, referentie 833, plus een kenmerkenlijst (zonnepanelen, apart appartement, zwembad, carport, uitzicht op de Montgó) en een beschrijving.

Conclusie: leesbaar, maar per object moet de lezer prijs, oppervlaktes, plaats en referentie uit de paginatekst halen (vaste labels: "Build size", "Plot size", "Reference :", prijs met "€"). Op de homepage staan dezelfde velden compact in elke objectkaart, bijvoorbeeld "Villa , 4 Bedrooms Javea, Covatelles 779 998€ 270m² - Reference : 833".

## 5. Systeem achter de site — eigen bouw op Laravel

Aanwijzingen (homepage en objectpagina, 24-09-2026):
- cookies `laravel_session` en `XSRF-TOKEN`, formulierveld `_token` → Laravel (PHP-framework), dus maatwerk;
- sjabloonpad `/assets/templates/villalingo/…`, foto's in `/uploads/photos/properties/<id>/`, schaalversies via `/thumbnails/800x600/…`;
- cookiebanner van TermsFeed; Google Analytics (gtag) en reCAPTCHA;
- server meldt `o2switch-PowerBoost-v3` (Franse hostingpartij);
- geen enkel spoor van Inmoweb, Mediaelx/LetsINMO, Sooprema, Inmovilla, Witei of WordPress.

Er is dus geen bekende exportfeed. Als lezen ooit niet meer mag, is de enige weg het kantoor zelf om een uitwisseling te vragen.

## 6. Omvang en dekking Jávea / Benitachell / Moraira

Op de homepage staan 34 verschillende objecten (referenties 27 t/m 836; bron: homepage, 24-09-2026). Verdeling naar plaats: Jávea 9, Moraira 6, Benitachell 6, Benissa 3, Pedreguer 3, Dénia 2, Calpe 2, Teulada 1, Altea 1, Benidorm 1. Ons werkgebied (Jávea + Benitachell + Moraira): 21 van 34 = 62%. Naar type: 19 villa's, 9 percelen, 3 appartementen, 2 commercieel, 1 rijwoning.

Het totale aanbod heb ik niet vastgesteld: de aanbodpagina zelf is niet geopend (budget). De 34 op de homepage zijn een ondergrens; het hoogste referentienummer (836) zegt alleen dat er ooit ruim 800 records zijn aangemaakt, niet hoeveel er nu te koop staan. [te verifiëren bij de eerste echte leesronde]

Relevant voor Deal Hunter: het kantoor heeft opvallend veel percelen (9 van 34, o.a. Moraira Benimeit 996 m² voor 140 000€ en Benissa 10 780 m² voor 167 500€) en een pagina "under 200 000€" — precies de categorieën waar wij naar zoeken.

## Wat er bij een leesronde moet gebeuren

1. Alleen de aanbodpagina's en `/property-NNN` lezen; sitemap en genummerde sitemap-bestanden negeren.
2. Hoogstens één verzoek per twee seconden; identificeerbare User-agent.
3. Velden uit de HTML-tekst halen (labels hierboven); geen JSON-LD beschikbaar.
4. Omdat de site mogelijk gehackt is: alleen HTML lezen, nooit bestanden downloaden of scripts uitvoeren van deze site.

⏸️ ACTIE VOOR JAN (optioneel): de eigenaar van Villa Lingo een collegiale hint geven dat zijn sitemap vol spam-URL's staat — dat is meestal een teken van een inbraak, en hij ziet het zelf waarschijnlijk niet.

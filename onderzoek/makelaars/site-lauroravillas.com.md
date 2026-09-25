# L'Aurora Villas Selection — toets op automatisch lezen

**Website:** https://www.lauroravillas.com
**Datum controle:** 24-09-2026
**Kantoor:** Ronda Norte 6, 03730 Jávea (Alicante) · kantoortelefoon 966 172 981 · WhatsApp-knop op de site wijst naar +34 966 172 981
(bron: voettekst van de site, 24-09-2026). De juridische houder van de site is een natuurlijke persoon (eenmanszaak); naam en
persoonlijke gegevens bewust niet overgenomen.

**Advies: LEZEN.** robots.txt laat een gewone bot toe op alle aanbod- en objectpagina's, er zijn geen gebruiksvoorwaarden die
scraping verbieden, en de objectpagina's zijn gewone, goed leesbare HTML (label/waarde). Het systeem is Inmoweb, dat ook een
exportfeed kent — een tweede optie als het kantoor daar aan meewerkt [te verifiëren].

---

## 1. robots.txt — toegestaan (met kleine uitzonderingen)

Bron: https://www.lauroravillas.com/robots.txt (HTTP 200, 24-09-2026).

Het bestand blokkeert eerst een lange lijst specifieke bots volledig (o.a. SemrushBot, Bytespider, HTTrack, wget/Wget,
libwww, httplib, lwp-trivial, ia_archiver, ahrefsbot, dotbot, Baiduspider — elk met `Disallow: /`). Voor alle overige bots geldt:

```
User-agent: *
Disallow: /*?*modo=
Disallow: /*?*od=
Disallow: /*?*dt=
Disallow: /*?*i=
Disallow: /*?*c=
```

Conclusie: een `User-agent: *` mag de aanbodpagina's en objectpagina's lezen. Alleen URL's met de queryparameters
`modo=`, `od=`, `dt=`, `i=` of `c=` (sorteer-/filtervarianten) zijn verboden. Alle object-URL's en categoriepagina's zijn
schone `.html`-adressen zonder vraagteken en vallen dus buiten die regels. Er staat geen `Sitemap:`-regel in.

Praktisch: gebruik een eigen, herkenbare user-agent (niet wget/libwww/httplib, die staan op de zwarte lijst) en laat
`/results/?...`-URL's links liggen; de categoriepagina's per type volstaan.

## 2. Gebruiksvoorwaarden — geen verbod gevonden

De site heeft geen aparte pagina met "aviso legal" of "términos". De voetlink **"Avisos legales"** wijst naar
https://www.lauroravillas.com/lopd/ (HTTP 200, 24-09-2026). Die pagina bevat uitsluitend:

- **"POLÍTICA DE PRIVACIDAD"** volgens RGPD (EU 2016/679) en LOPDGDD 3/2018: verantwoordelijke, ontvangers, rechtsgrond,
  rechten van betrokkenen, en de verwerkingen (contactformulier, nieuwsbrief, chatbot);
- **"III. POLITICA DE COOKIES"** (soorten cookies).

Er staat **niets** in over automatisch lezen, scraping, robots, reproductie, databankrechten of intellectueel eigendom.
Gezocht op: scrap, robot, automat, crawl, extrac, reproduc, copia, base de datos, prohib, propiedad intelectual,
condiciones de uso — nul relevante treffers. Bij het contactformulier staat de tekst "Acepto la política de privacidad y
normas de uso de lauroravillas.com", maar de gelinkte pagina bevat geen "normas de uso" buiten de privacyverklaring.
Er is ook een /cookie_policy/-pagina (niet geopend; limiet van vijf pagina's).

Oordeel: voorwaarden die scraping verbieden — **niet gevonden**.

## 3. Sitemap — 750 URL's, 50 unieke objecten

Bron: https://www.lauroravillas.com/sitemap.xml (HTTP 200, 95,8 kB, 24-09-2026). Geen sitemap-index, één bestand.

| | aantal |
|---|---|
| URL's totaal | 750 |
| Talen | 12 (es op de root; gb, nl, de, fr, ru, pt, no, fi, se, da, it als prefix — elke taal ±61–65 URL's) |
| Spaanse root-URL's | 65 |
| waarvan objectpagina's (`…-esNNNNNNN.html`) | **50**, allemaal unieke referenties |
| categoriepagina's koop | 5 (apartamentos, casas-chalets, casas-de-pueblo, locales-comerciales, parcelas — `…-en-venta-N-1.html`) |
| categoriepagina huur | 1 (`apartamentos-en-alquiler-1-2.html`) |
| overig | `/results/?id_tipo_operacion=1` en `=2`, home, `/lopd/`, `/form_captacion/`, `/contact/`, `/aboutus/`, `/appointment` |

De 50 objecten naar type: 17 apartamento, 15 casa de pueblo, 13 casa/chalet, 3 parcela, 2 local comercial.
Koop en huur zitten door elkaar (de URL-slug maakt geen onderscheid); volgens het menu gaat het bij huur om een handjevol
appartementen (Cala Blanca/Jávea en Dénia). Dus circa 45–48 objecten te koop.

Controle op volledigheid: de categoriepagina "Casas / Chalets en venta" meldt **"Mostrando 1 a 13 de 13"** en linkt naar
precies de 13 casa-chalet-URL's uit de sitemap. De sitemap lijkt dus compleet en actueel (`changefreq: daily`).

## 4. Aanbodpagina en objectpagina

**Aanbodpagina (koop, villa's):** https://www.lauroravillas.com/casas-chalets-en-venta-3-1.html (HTTP 200, 24-09-2026).
13 objecten, prijzen zichtbaar in de lijst (192.000 € t/m 1.250.000 €), elke kaart linkt naar de objectpagina.
Paginering volgt het patroon `…-3-<paginanummer>.html`. Het totaaloverzicht koop staat in de sitemap als
`/results/?id_tipo_operacion=1` (niet geopend).

**Objectpagina:** https://www.lauroravillas.com/casa-chalet-en-javea-la-plana-es1776570.html (HTTP 200, 24-09-2026).

- `<script type="application/ld+json">`: **niet aanwezig** (0 blokken). Ook geen microdata behalve één `itemprop="image"`.
- **og:-tags:** `og:type=website`, `og:title="Venta Casa / Chalet en Jávea, LA PLANA"`, `og:locale=es`, `og:url`,
  `og:image` (foto op `static.inmoweb.es/clients/236/property/1776570/…`). Geen og:price of og:description.
  `<meta name="author" content="inmoweb.es">`; hreflang-links naar de 11 andere talen.
- **In de HTML (label/waarde, goed te parsen):** Nº de referencia **LAU2923** · Precio **192.000 €** · Sup. Útil **58 m²** ·
  1 habitación · 1 baño · Provincia Alicante · Población **Jávea** · Zona **LA PLANA** · Tipo de obra Segunda mano ·
  energielabel "Exento". Het veld "Sup. Parcela (m²)" staat in de sjabloon maar is bij dit object leeg; de omschrijving noemt
  "un terreno de aproximadamente 600 m²". Sjabloon kent ook een label **"Precio rebajado"** (prijsverlaging) — handig voor
  het signaleren van deals.

De cookie `last_seen=<objectnummer>` wordt gezet bij het openen van een object.

## 5. Systeem: Inmoweb

Zeker Inmoweb, op grond van:
- alle css/js van het framework komt van `storage.googleapis.com/staticweb.inmoweb.es/web_framework/…`;
- alle foto's en logo's van `storage.googleapis.com/static.inmoweb.es/clients/236/…` (klantnummer 236);
- `<meta name="author" content="inmoweb.es">`;
- voettekst "Hecho con Software inmobiliario" met link naar https://www.inmoweb.es/ (title "Hecho con Inmoweb Software
  Inmobiliario");
- serverkoppen: `server: BitNinja-WafPro`, `via: 2.0 Caddy`, `x-powered-by: PHP/8.3.33` en `PleskLin`.

Inmoweb levert als CRM ook XML-exportfeeds aan portalen; of dit kantoor die wil delen is een vraag aan het kantoor
[te verifiëren].

## 6. Omvang en dekking Jávea / Benitachell / Moraira

Schatting: **50 objecten** in totaal (koop + huur), waarvan circa 45–48 te koop. Bron: sitemap 24-09-2026.

Naar plaats (uit de URL-slugs van de 50 objecten):

| plaats | aantal |
|---|---|
| **Jávea** (pueblo, Montgó, La Plana, Tosalet, Castellans, Cansalades, Cala Blanca, Arenal, Frechinal, Montañar II) | **30** |
| Gata de Gorgos | 9 |
| Dénia | 2 |
| Pedreguer | 2 |
| **Benitachell** | **1** |
| **Teulada** (gemeente van Moraira; Moraira zelf 0) | **1** |
| Pego, Orba, Ondara, Jesús Pobre, Cazorla (Jaén) | 1 elk |

Dekking Jávea + Benitachell + Teulada/Moraira: **32 van 50 = 64 %**. Zwaartepunt Jávea-dorp (casas de pueblo en
appartementen) plus Gata de Gorgos; weinig kustvilla's boven de miljoen.

## Werkwijze en ophaallog (max. vijf pagina's, minstens 2 s tussenpoos)

1. https://www.lauroravillas.com/robots.txt — 200
2. https://www.lauroravillas.com/sitemap.xml — 200 (95.841 bytes)
3. https://www.lauroravillas.com/lopd/ — 200
4. https://www.lauroravillas.com/casas-chalets-en-venta-3-1.html — 200
5. https://www.lauroravillas.com/casa-chalet-en-javea-la-plana-es1776570.html — 200

Pagina's 3–5 in één curl-sessie met `--rate 20/m` (één verzoek per 3 s); alle analyse daarna op de lokale kopieën.
Niet ingelogd, geen formulieren gebruikt, niets omzeild.

## Aanbeveling voor de lezer (Deal Hunter)

- Bron: de sitemap (dagelijks), filter op `…-es[0-9]+.html`; ±50 pagina's per ronde, één per 2–3 s → 2–3 minuten.
- Eigen user-agent met contactadres; nooit wget/libwww/httplib als naam; geen `?`-URL's.
- Parse: referentie, prijs, "Precio rebajado", Sup. Útil / Construida / Parcela, Población, Zona, Tipo de obra.
- Alternatief: het kantoor om de Inmoweb-feed vragen (⏸️ ACTIE VOOR JAN, alleen als hij dat wil).

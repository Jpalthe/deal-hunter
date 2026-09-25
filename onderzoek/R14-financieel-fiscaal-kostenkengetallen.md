# R14 — Financiële en fiscale parameters Comunitat Valenciana 2026 en kostenkengetallen bouw/renovatie

> **NA TEGENSPRAAK (15-09-2026).** Dit rapport is door een tweede agent gecontroleerd; zie `R14-financieel-fiscaal-kostenkengetallen.verificatie.md`. Betrouwbaarheid volgens die controle: hoog.
> Weerlegd en in de eindstukken gecorrigeerd: R14-13; R14-17. Gebruik voor die punten de gecorrigeerde tekst in het verificatiebestand, niet de tekst hieronder.


**Project:** TREE Deal Hunter, fase A · **Stroom:** R14 · **Controledatum van alle bronnen:** 14-09-2026 (avond)
**Masterprompt-secties:** 20 (waardering), 21 (volledige financiële analyse), 22 (maximale koopprijs)
**Bewijstypen (masterprompt §5):** 1 door aanbieder vermeld · 2 in officiële bron aangetroffen · 3 door ons rechtstreeks vastgesteld · 4 AI-inferentie · 5 berekening op benoemde aannames · 6 door bevoegde professional bevestigd · 7 onbekend of tegenstrijdig
**Aanvulling 15-09-2026 (hervatte ronde):** het gat "installaties" en "beperkte opwaardering" uit opdracht d is gedicht in **§4.5** (marktindicaties, bewijstype 1, lage zekerheid); de rekenfunctie van §6.4 is opnieuw uitgevoerd met identieke uitvoer; R12 bestaat nog steeds niet (§5.3). Alle overige cijfers hebben controledatum 14-09-2026.

## Samenvatting (10 regels)

1. **ITP Comunitat Valenciana is per 1 juni 2026 verlaagd van 10 % naar 9 %** (11 % boven 1.000.000 €); AJD algemeen van 1,5 % naar 1,4 % (Ley 5/2025, art. 33–34; BOE-geconsolideerde Ley 13/1997 art. 13–14; bevestigd op de ATV-tarieventabel). Voor een investeerder/vennootschap gelden geen verlaagde ITP-tarieven: die zijn alleen voor vivienda habitual, jongeren, VPO, gezinnen, ontvolkingsgemeenten en landbouwpercelen.
2. **Heffingsgrondslag ITP/AJD = de hoogste van prijs en Catastro-*valor de referencia*** (art. 10.2 TRLITPAJD, Ley 11/2021). Bij veilingen is de grondslag volgens het Reglamento de verwervingsprijs (art. 39 RITP) — de verhouding tot de valor de referencia is **tegenstrijdig/niet geverifieerd (bewijstype 7)**; de ATV hanteert voor veilingtoewijzing tariefcode TS0 = 9 %.
3. **Btw:** 21 % algemeen; 10 % op eerste levering van woningen, op bouw-/rehabilitatiecontracten promotor–aannemer voor overwegend woningen, en op renovatie/reparatie voor particulieren (woning ≥ 2 jaar, materiaal ≤ 40 %). Solares van ondernemers: 21 % (+ AJD 1,4 %). Tweede levering: btw-vrij → ITP, tenzij afstand van vrijstelling (dan AJD 2 %).
4. **Notaris- en registerkosten zijn wettelijk geregeld en klein**: RD 1426/1989 en RD 1427/1989, Número 2, degressieve schaal met 5 % korting. Rekenvoorbeeld (alleen matriz/inschrijving, excl. btw): bij 500.000 € ≈ 483 € notaris + 262 € register; bij 1.000.000 € ≈ 645 € + 367 € (bewijstype 5).
5. **Winstbelasting:** IS 25 % algemeen; micro-ondernemingen (< 1 M€ omzet) in 2026: 19 % tot 50.000 € / 21 % daarboven; ERD (< 10 M€): 23 % in 2026 (DT 44ª LIS). IRPF-spaarschaal 2026: 19 / 21 / 23 / 27 / 30 %. Niet-resident verkoper: 19 % (EU/EER) en de koper houdt 3 % in (art. 25 LIRNR).
6. **Plusvalía (IIVTNU):** verkoper betaalt (koper is plaatsvervanger bij niet-resident natuurlijke persoon); grondslag = kadastrale grondwaarde × coëfficiënt per jaar (wettelijke maxima in art. 107.4 TRLRHL, tabel in dit rapport) of het werkelijke verschil; nultarief bij geen waardestijging; tarief ≤ 30 %. **Het Xàbia-tarief en de gemeentelijke coëfficiënten zijn niet gevonden (ordenanzas alleen via JavaScript-portaal bereikbaar) — ONBEKEND.**
7. **Lokale heffingen Xàbia:** IBI-tarief ONBEKEND (wettelijk 0,4–1,10 %; de gemeente meldt een verlaging van het IBI-tarief in 2025), ICIO-tarief ONBEKEND (wettelijk ≤ 4 % op PEM), tasa licencia ONBEKEND. Wel bevestigd: nieuwe afvalheffing per 1-1-2025 (Ordenanza Fiscal 03/03) met variabel deel naar kadastrale waarde en 20 € per toeristische slaapplaats.
8. **Financiering (Banco de España):** Euríbor 12 maanden augustus 2026 = 2,954 % (officieel, BOE 2-9-2026); september 2026 nog niet gepubliceerd [te verifiëren]. Gemiddelde rente nieuwe woninghypotheken juli 2026 (TEDR, voorlopig) 2,89 %; nieuwe leningen aan niet-financiële vennootschappen 3,68 %. Voorwaarden voor niet-residenten/vennootschappen worden niet officieel gepubliceerd: ONBEKEND.
9. **Bouwkosten:** geen officiële gratis €/m²-referentie gevonden. De IVE-database BDC 2026 is betaald (69,99 €/jaar online; 225 € installeerbaar); het ministerie-portaal met visado-PEM gaf HTTP 403; COAAT Alicante gaf een certificaatfout; CTAA/COACV publiceren geen módulo op hun startpagina. Beschikbare marktindicaties (habitissimo, bewijstype 1, lage zekerheid, landelijk, btw-status onduidelijk): nieuwbouw 800–1.200 €/m², integrale renovatie 650–900 €/m² (breed 400–1.200), keuken 3.500–12.500 €, badkamer 1.200–4.500 €, zwembad 10.000–19.000 €, sloop 10–90 €/m², keermuur 90–250 €/m². **Voor het Jávea-villasegment ontoereikend; Jans eigen nacalculaties zijn de enige geschikte bron (ACTIE VOOR JAN).**
10. **Rekenmodel:** sectie 6 geeft de kostenposten per route met bron en zekerheid, de terugrekening van de maximale koopprijs in woorden en als geteste Python-functie (bisectie, zonder externe libraries). De rendementseis is een **ONBEKENDE input van Jan**; tijdsaannames wachten op R12 (nog niet beschikbaar op 14-09-2026 23:40).

---

## 0. Methode en beperkingen van deze stroom

| Punt | Toelichting |
|---|---|
| Zoekbudget | Het sessiebrede WebSearch-budget was bij aanvang van R14 op (200/200). Alle bronnen zijn daarom rechtstreeks opgehaald via bekende officiële URL's (WebFetch/curl); geen enkele zoekopdracht was mogelijk. Waar een URL niet bekend was, staat ONBEKEND. |
| Wetteksten | Via de officiële **BOE-API "legislación consolidada"** (`https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/{ID}/texto/bloque/{blok}`, header `Accept: application/xml`). Per artikel is de **geldende** versie gebruikt (laatste tekstblok, met de wijzigingsnoten van de BOE). Menselijk leesbare versie: `https://www.boe.es/buscar/act.php?id={ID}`. |
| Regionale wet | Ley 13/1997 CV staat geconsolideerd op boe.es onder **BOE-A-1998-8202** (art. 13 bijgewerkt 02-07-2026, art. 14 bijgewerkt 31-05-2025). |
| Gemeentelijk | De ordenanzas fiscales van Xàbia staan achter een JavaScript-portaal (sede electrónica, links met opaque `?x=`-tokens). Niet omzeild; lokale tarieven blijven ONBEKEND. |
| Marktcijfers bouw | Alleen wat zonder zoekmachine bereikbaar was. Bewust geen blogs; wél de prijsgidsen van één groot offerteplatform, expliciet met lage zekerheid. |
| Eigen data | In `~/tree-es/constructions` staan alleen websitedocumenten; het vertrouwelijke projectwerkboek dat de CLAUDE.md daar noemt, staat niet in de map. Er zijn dus **geen eigen kengetallen** in bestanden gevonden. |
| Wat R14 niet doet | Geen fiscaal advies; alleen tarieven en regels met bron. Structuurkeuzes (vennootschap/privé, rehabilitación-route) zijn als **AI-inferentie (4)** gemarkeerd en moeten door een gestor/fiscalist worden bevestigd (6). |

---

## 1. Aankoopbelastingen Comunitat Valenciana 2026 (opdracht a)

### 1.1 ITP (Transmisiones Patrimoniales Onerosas) — algemeen tarief

| Parameter | Waarde | Sinds | Bron | Bewijs | Btw |
|---|---|---|---|---|---|
| ITP onroerend goed, algemeen | **9 %** | Feiten belastbaar vanaf **01-06-2026** | Ley 13/1997 CV art. 13.Uno (BOE-A-1998-8202, blok a13, bijgewerkt 02-07-2026): "El 9 % en las adquisiciones de inmuebles…"; gewijzigd door art. 33 Ley 5/2025 (BOE-A-2025-11959). ATV-tabel: codes TU0 (solares) 9, TU1 (viviendas) 9, TU2 (locales) 9, TR0–TR2 (rústicos) 9. | 2 | n.v.t. (ITP is geen btw; niet terugvorderbaar) |
| ITP boven 1.000.000 € | **11 %** over de hele grondslag | ongewijzigd | Zelfde artikel: "cuando el valor … sea superior a un millón de euros, el tipo aplicable será el 11 %"; ATV code TUM 11. | 2 | — |
| Vorig algemeen tarief | 10 % | tot 31-05-2026 | BOE-noot "Redacción anterior" bij art. 13.Uno. | 2 | — |
| Anti-splitsingsregel | Aankopen van dezelfde finca van dezelfde verkoper binnen 3 jaar tellen als één transmissie voor het tarief | — | Art. 13.Ocho Ley 13/1997. Relevant als een perceel en woning of aangrenzende percelen apart worden gekocht. | 2 | — |
| Staats-suppletoir tarief | 6 % (alleen als een CA geen tarief heeft) | — | Art. 11.1.a TRLITPAJD (BOE-A-1993-25359). Niet van toepassing in CV. | 2 | — |
| Aangiftetermijn | 1 maand vanaf de akte (modelo 600) | — | Art. 14 bis.Uno Ley 13/1997. | 2 | — |

### 1.2 Verlaagde ITP-tarieven (alleen wat in Ley 13/1997 art. 13 en de ATV-tabel staat)

Geen van deze tarieven geldt voor een aankoop door een vennootschap of investeerder voor renovatie/verkoop; ze zijn opgenomen omdat ze de **koperszijde** van onze verkoop beïnvloeden (een jonge koper van een woning ≤ 180.000 € betaalt 6 % in plaats van 9 %).

| Tarief | Geval (samengevat) | Voorwaarde/drempel | ATV-code | Bron | Bewijs |
|---|---|---|---|---|---|
| 8 % | VPO régimen general, eerste vivienda habitual, waarde > 180.000 € | — | TO0 | Art. 13.Dos.1 | 2 |
| 8 % | Eerste vivienda habitual jongeren < 35 jaar, waarde > 180.000 € | IRPF-inkomensgrens art. 4.Cuatro | TU4 | Art. 13.Dos.2 | 2 |
| 8 % | Onroerend goed in overdracht van een compleet bedrijf / door jonge ondernemers of hun vennootschappen | 3 jaar behoud, omzet ≤ 10 M€, activiteit in CV | TU5, TU6 | Art. 13.Dos.3–4 | 2 |
| 6 % | Eerste vivienda habitual jongeren < 35 jaar, waarde ≤ 180.000 € | IRPF-inkomensgrens | TJ8 | Art. 13.Tres.1 | 2 |
| 6 % | VPO régimen general ≤ 180.000 €, eerste vivienda habitual | — | TG8 | Art. 13.Tres.2 | 2 |
| 4 % | Waarde > 180.000 €: VPO régimen especial; familia numerosa/monoparental; discapacidad ≥ 65 % (of ≥ 33 % intellectueel/mentaal); slachtoffers gendergeweld — alle als vivienda habitual | inkomensgrenzen waar vermeld | TU8, TU9, TU7, TUV | Art. 13.Cuatro.1 | 2 |
| 4 % | Zetel/werkplek in "área industrial avanzada"; zetel in gemeente met ontvolkingsrisico | 3 jaar behoud, ≥ 1 voltijdwerknemer (despoblamiento), geen vermogensbeheer-activiteit | TAI, TUS | Art. 13.Cuatro.2–3 | 2 |
| 4 % | Percelen met "vocación agraria" gekocht door natuurlijke personen | 5 jaar agrarisch gebruik, inschrijving Registro de Explotaciones | TR3 | Art. 13.Cuatro.4 | 2 |
| 3 % | Waarde ≤ 180.000 €: VPO régimen especial; familia numerosa/monoparental; discapacidad; gendergeweld — als vivienda habitual | idem | TE8, TF8, TD8, TV8 | Art. 13.Cinco | 2 |
| Vormvereiste | Verlaagde tarieven (Dos–Cinco) alleen als de koop in openbare akte is of binnen de aangiftetermijn wordt geformaliseerd | — | — | Art. 13.Siete | 2 |
| Niet gevonden | Een verlaagd tarief voor **vastgoedbedrijven die kopen voor wederverkoop** (zoals sommige andere CA's kennen) staat **niet** in art. 13 Ley 13/1997 en niet in de ATV-tabel. | — | — | Art. 13 volledig gelezen | 2 (afwezigheid) |

### 1.3 AJD (Actos Jurídicos Documentados, modaliteit documentos notariales)

| Parameter | Waarde | Sinds | Bron | Bewijs |
|---|---|---|---|---|
| AJD algemeen ("en los demás casos") | **1,4 %** | Feiten vanaf 01-06-2026 (was 1,5 %) | Ley 13/1997 art. 14.Cuatro; gewijzigd door art. 34 Ley 5/2025. ATV: DN0 segregación 1,4; DN1 agrupación 1,4; **DN2 declaración de obra nueva 1,4; DN3 división horizontal 1,4; DN4 entregas sujetas al IVA 1,4**; DN9 otros 1,4. | 2 |
| AJD bij afstand van btw-vrijstelling (art. 20.Dos LIVA) | **2 %** | — | Art. 14.Dos Ley 13/1997; ATV code DA4. | 2 |
| AJD op hypotheekakten | **2 %**, sujeto pasivo = de geldgever (prestamista) | — | Art. 14.Tres Ley 13/1997; ATV DN5. Voor de koper dus geen kostenpost. | 2 |
| AJD vivienda habitual | 0,1 % | — | Art. 14.Uno.a; ATV DA1. | 2 |
| Anotaciones preventivas | 0,5 % | — | ATV code AP0. | 2 |
| Staats-suppletoir | 0,5 % | — | Art. 31.2 TRLITPAJD. Niet van toepassing in CV. | 2 |
| Grondslag AJD bij *declaración de obra nueva* / división horizontal (route B) | ONBEKEND in deze stroom (art. 70 RITP niet opgehaald) | — | — | 7 — [te verifiëren] |

### 1.4 Btw (IVA) op vastgoed en bouw

| Situatie | Btw | Bron (Ley 37/1992, BOE-A-1992-28740) | Bewijs | Terugvorderbaar? |
|---|---|---|---|---|
| Algemeen tarief | **21 %** | Art. 90.Uno (sinds 01-09-2012) | 2 | Alleen voor een btw-plichtige koper met aftrekrecht (4) |
| Eerste levering woning door promotor (incl. max. 2 garages en bijgebouwen) — **nieuwbouw** | **10 %** (+ AJD 1,4 % op de akte) | Art. 91.Uno.1.7º; art. 20.Uno.22º.A (definitie eerste levering; niet meer "eerste" na ≥ 2 jaar ononderbroken gebruik) | 2 | Niet voor particuliere eindkoper |
| Bouw- of rehabilitatiecontract **promotor ↔ aannemer** voor gebouwen die overwegend (≥ 50 % oppervlak) woning zijn | **10 %** | Art. 91.Uno.3.1º; ook keuken-/badkamerkasten geleverd en geplaatst onder direct contract met de promotor: 10 % (art. 91.Uno.3.2º) | 2 | Ja, voor de promotor-vennootschap die met btw verkoopt (4) |
| Renovatie/reparatie van een woning voor een **particulier** (niet-ondernemer, eigen gebruik) of VvE; woning ≥ 2 jaar opgeleverd; materiaal door aannemer ≤ 40 % van de grondslag | **10 %** | Art. 91.Uno.2.10º | 2 | Nee (particulier) |
| Renovatie voor een **vennootschap** die niet aan de rehabilitación-definitie voldoet | **21 %** | Volgt uit art. 90 en de voorwaarden van art. 91.Uno.2.10º (destinatario = persona física) | 2 + 4 | Niet aftrekbaar als de latere verkoop btw-vrij is (tweede levering) — [te verifiëren bij fiscalist] |
| Definitie **rehabilitación** (maakt de verkoop daarna weer een "eerste levering" met btw 10 % en geeft aftrekrecht op de bouw-btw) | > 50 % van de projectkosten voor structuur/gevel/dak (of analoge werken) **én** totale kosten > 25 % van de aankoopprijs (of marktwaarde) exclusief grondaandeel | Art. 20.Uno.22º.B | 2 | Structuurkeuze: 4 — laten toetsen |
| **Solares / bouwrijpe grond** geleverd door een ondernemer | **21 %** (+ AJD 1,4 %) | Art. 20.Uno.20º stelt alleen rústicos/niet-bebouwbare grond vrij; solares en grond met bouwvergunning zijn "edificables" en dus belast | 2 | Ja voor btw-plichtige promotor (4) |
| Grond of tweedehands woning van een **particulier** | Geen btw → **ITP 9 % / 11 %** | Buiten btw-sfeer (art. 4/5 LIVA, niet opgehaald) — algemene regel | 2 (ITP-kant) | Nee |
| Tweede levering door ondernemer (bijv. bank, promotor na 2 jaar verhuur) | Btw-vrij → ITP 9 %; **afstand van vrijstelling** mogelijk als koper btw-plichtig is met (gedeeltelijk) aftrekrecht → btw 21 % (verlegd) + **AJD 2 %** | Art. 20.Uno.22º.A en 20.Dos; AJD art. 14.Dos Ley 13/1997 | 2 | Ja bij afstand (4) |
| Gebouw dat wordt gekocht om te slopen vóór nieuwe promotie | **Niet** vrijgesteld → btw 21 % als verkoper ondernemer is | Art. 20.Uno.22º.A.c en art. 91.Uno.1.7º (geen 10 %) | 2 | Ja voor promotor (4) |

### 1.5 Valor de referencia als minimale heffingsgrondslag

| Punt | Inhoud | Bron | Bewijs |
|---|---|---|---|
| Regel | "En el caso de los bienes inmuebles, su valor será el valor de referencia previsto en la normativa reguladora del catastro inmobiliario, a la fecha de devengo del impuesto. No obstante, si el valor … declarado …, el precio … o ambos son superiores a su valor de referencia, se tomará como base imponible la mayor de estas magnitudes." | Art. 10.2 TRLITPAJD (BOE-A-1993-25359, blok a10), ingevoegd door art. 6.2 Ley 11/2021 (BOE-A-2021-11473) | 2 |
| Zonder valor de referencia | Grondslag = hoogste van aangegeven waarde, prijs of marktwaarde, met mogelijkheid van controle | Art. 10.2, derde alinea | 2 |
| Bezwaar | Alleen via rectificatie van de zelfaangifte of bezwaar tegen de aanslag; Catastro geeft bindend rapport | Art. 10.3–10.4 | 2 |
| Praktische toegang | Per object opvraagbaar in de Sede del Catastro, **alleen na authenticatie** (certificaat/Cl@ve) — zie R04 | R04 §bron 66: https://www1.sedecatastro.gob.es/Accesos/SECAccvr.aspx | 2 (R04) |
| Gevolg voor het model | ITP/AJD rekenen over max(prijs, valor de referencia). Bij "deals" onder marktprijs (veiling, distress) kan de belasting hoger uitvallen dan 9 % van de prijs. Per kandidaat de valor de referencia opvragen vóór het bod. | — | 4 |

### 1.6 ITP bij veilingtoewijzing (subasta judicial, administrativa, notarial)

| Punt | Inhoud | Bron | Bewijs |
|---|---|---|---|
| Tarief | 9 % (ATV tariefcode **TS0** "Transmisión de inmuebles rústicos y urbanos en subasta judicial, administrativa o notarial") | https://atv.gva.es/es/itpajd | 2 |
| Grondslag volgens Reglamento | "En las transmisiones realizadas mediante subasta pública, notarial, judicial o administrativa, servirá de base el valor de adquisición, siempre que consista en un precio en dinero marcado por la Ley o determinado por autoridades o funcionarios idóneos para ello." De BOE noteert dat het artikel deels is vernietigd door TS 3-11-1997 (fundamento 12). | Art. 39 RD 828/1995 (BOE-A-1995-15071, blok a39) | 2 |
| Verhouding tot valor de referencia (art. 10.2 TRLITP, 2021) | **Tegenstrijdig / niet geverifieerd:** de wet (2021) zegt "valor de referencia tenzij prijs hoger", het Reglamento (1995) zegt "valor de adquisición". Welke regel de ATV in 2026 toepast op veilingen is in deze stroom niet vastgesteld. | — | 7 — vraag aan gestor; meenemen in R08-veilingdossier |
| Aanvullend | Bij bankvastgoed dat de bank als ondernemer levert: mogelijk btw-regime i.p.v. ITP (tweede levering vrijgesteld, afstand mogelijk). | Art. 20.Uno.22º LIVA | 4 |

### 1.7 Beslisregel per transactie (samenvatting; AI-inferentie 4, per deal door gestor te bevestigen)

| Wat wordt gekocht | Van wie | Belasting koper | Aftrekbaar? |
|---|---|---|---|
| Tweedehands woning/villa | particulier | ITP 9 % (11 % > 1 M€) over max(prijs, valor de referencia) | nee |
| Tweedehands woning | ondernemer (bank, promotor, SL) | ITP 9 % — of bij afstand van vrijstelling btw 21 % verlegd + AJD 2 % | alleen bij afstand |
| Nieuwbouwwoning | promotor | btw 10 % + AJD 1,4 % | nee (tenzij btw-plichtige koper) |
| Solar/bouwkavel | particulier | ITP 9 % | nee |
| Solar/bouwkavel | ondernemer | btw 21 % + AJD 1,4 % | ja voor promotor-SL (4) |
| Rústico/niet-bebouwbaar | ondernemer | btw-vrij → ITP 9 % (afstand mogelijk) | — |
| Veilingtoewijzing | rechtbank/administratie | ITP 9 % (TS0); grondslag zie 1.6 | nee |

---

## 2. Transactiekosten (opdracht b)

### 2.1 Notaris — RD 1426/1989, Anexo I, Número 2 "Documentos de cuantía" (BOE-A-1989-28111, blok ani; bedragen in euro sinds Instrucción 22-05-2002)

| Waarde-tranche van het object | Tarief | Bewijs |
|---|---|---|
| tot 6.010,12 € | 90,151816 € vast | 2 |
| 6.010,13 – 30.050,61 € | 4,5 ‰ over het meerdere | 2 |
| 30.050,62 – 60.101,21 € | 1,50 ‰ | 2 |
| 60.101,22 – 150.253,03 € | 1 ‰ | 2 |
| 150.253,04 – 601.012,10 € | 0,5 ‰ | 2 |
| 601.012,10 – 6.010.121,04 € | 0,3 ‰ | 2 |
| boven 6.010.121,04 € | vrij overeen te komen | 2 |
| Korting | **−5 %** op het bedrag van Número 2 (DA 8.1.1 RDL 8/2010, noot in de BOE-tekst); daarnaast mag de notaris tot 10 % korting geven (notariado.org "Qué cuesta", bewijstype 1) | 2 / 1 |
| Reductie | −25 % bij hypotheekakten; −50 % o.a. bij VPO-transmissies | 2 |
| Veiling / buitengerechtelijke executie | Número 2 over de *precio de remate o adjudicación* (Número 6.4 van het arancel) | 2 |
| Btw op het honorarium | Het arancel noemt btw niet; de notarisfactuur is naar algemene regel btw-plichtig (21 %) — [te verifiëren] | 4 |
| Let op | Número 2 is alleen de *matriz*. De factuur bevat daarnaast folios (3,005061 €/pagina vanaf het 5e blad), kopieën, diligencias e.d.; "todos los notarios cobran lo mismo por servicios idénticos" (notariado.org, 1). Reken voor de villa-klasse indicatief het dubbele van Número 2 [aanname, 5]. | 2 / 1 / 5 |

### 2.2 Registro de la Propiedad — RD 1427/1989, Número 2 "Inscripciones" (BOE-A-1989-28112, blok numero2; versie RD 1612/2011)

| Waarde-tranche | Tarief | Bewijs |
|---|---|---|
| tot 6.010,12 € | 24,040484 € | 2 |
| 6.010,13 – 30.050,61 € | 1,75 ‰ | 2 |
| 30.050,62 – 60.101,21 € | 1,25 ‰ | 2 |
| 60.101,22 – 150.253,03 € | 0,75 ‰ | 2 |
| 150.253,04 – 601.012,10 € | 0,30 ‰ | 2 |
| boven 601.012,10 € | 0,20 ‰ | 2 |
| Minimum / maximum | "no podrá superar los 2.181,673939 euros ni ser inferior a 24,040484 euros" | 2 |
| Korting | −5 % (RDL 8/2010) | 2 |
| Reductie | 75 % van het tarief bij hypotheken; 70 % bij segregaciones/agrupaciones/divisiones en eerste inschrijving van elementen in propiedad horizontal (route B!) | 2 |
| Btw | Zie notaris: [te verifiëren], vermoedelijk 21 % | 4 |

**Rekenvoorbeeld (bewijstype 5; alleen Número 2, na 5 % korting, excl. btw, excl. bijkomende posten):**

| Koopsom | Notaris matriz | Register inschrijving | ITP 9 %/11 % |
|---|---|---|---|
| 250.000 € | 364,26 € | 191,15 € | 22.500 € |
| 500.000 € | 483,01 € | 262,40 € | 45.000 € |
| 1.000.000 € | 644,71 € | 367,00 € | 90.000 € |
| 1.200.000 € | ≈ 700 € | ≈ 405 € | 132.000 € (11 % over alles) |

Conclusie: notaris en register samen zijn < 0,2 % van de koopsom; **ITP is de dominante aankoopkostenpost** (9 % → 11 % boven 1 M€: een sprong van 20.000 € extra bij 1.000.001 € t.o.v. 1.000.000 €, art. 13.Ocho voorkomt kunstmatig splitsen).

### 2.3 Gestoría, due diligence (advocaat), taxatie

| Post | Gepubliceerd tarief? | Bron | Bewijs |
|---|---|---|---|
| Gestoría (afhandeling modelo 600, inschrijving, plusvalía-aangifte) | Niet gevonden; geen wettelijk tarief | — | 7 — ONBEKEND; offerte vragen |
| Advocaat/due diligence (nota simple, lasten, urbanistische controle, contracten) | Geen gepubliceerde tarieven; **beroepsorganisaties mogen geen tariefrichtlijnen geven**: "Los Colegios Profesionales … no podrán establecer baremos orientativos ni cualquier otra orientación, recomendación, directriz, norma o regla sobre honorarios profesionales" | Art. 14 Ley 2/1974 (BOE-A-1974-289, blok a14; ingevoegd door Ley 25/2009) | 2 (verbod) / 7 (bedrag) |
| Taxatie (tasación ECO/805/2003 door erkende tasadora, nodig bij hypotheek) | Geen gepubliceerd tarief gevonden | — | 7 — ONBEKEND |
| Architect/aparejador (honoraria) | Idem art. 14 Ley 2/1974: geen baremos. Marktindicatie op één platform: "honorarios (10-12 %)" van de bouwsom (habitissimo, construcción casas, bijgewerkt 18-06-2026) | https://www.habitissimo.es/presupuestos/construccion-casas | 2 (verbod) / 1 (10–12 %, lage zekerheid) |

---

## 3. Verkoopkosten (opdracht c)

| Post | Waarde | Bron | Bewijs | Btw |
|---|---|---|---|---|
| Makelaarscommissie Costa Blanca — gepubliceerde bron | Niet gevonden (geen zoekbudget; portalen/verenigingen publiceren geen vaste percentages) | — | 7 | — |
| Makelaarscommissie — **eigen netwerk** | BP-exports zijn gesplitst op **5 %** en **3–4 %** netwerkcommissie (export_id 26/27 e.a.; geen sleutels overgenomen) | `~/tree-hermes/properties-api/feeds.js` (alleen gelezen); R05 | 3 | Commissie is dienst → **+21 % btw** (algemene regel, 4) |
| Commissie bij veilingplatform procuradores | 4 % op inmuebles | R08 (subastasprocuradores.com) | 1 (via R08) | — |
| Modelaanname verkoopkosten | 3–5 % + btw, plus staging/fotografie/juridisch [ONBEKEND] | — | 5 | — |
| **Plusvalía municipal (IIVTNU)** — wie betaalt | Verkoper (contribuyente) bij overdracht onder bezwarende titel; **koper is plaatsvervangend belastingplichtige als de verkoper een niet-residente natuurlijke persoon is** | Art. 106.1.b en 106.2 TRLRHL (BOE-A-2004-4214, blok a106) | 2 | n.v.t. |
| IIVTNU — grondslag (objectieve methode) | Kadastrale **grondwaarde** op het moment van overdracht × coëfficiënt per aantal volle jaren bezit (< 1 jaar pro rata per maand). Wettelijke **maximumcoëfficiënten** in de geldende tekst (BOE 14-09-2026): < 1 jaar 0,15 · 1 jr 0,15 · 2 jr 0,14 · 3 jr 0,14 · 4 jr 0,16 · 5 jr 0,18 · 6 jr 0,19 · 7 jr 0,20 · 8 jr 0,19 · 9 jr 0,15 · 10 jr 0,12 · 11 jr 0,10 · 12–15 jr 0,09 · 16 jr 0,10 · 17 jr 0,13 · 18 jr 0,17 · 19 jr 0,23 · ≥ 20 jr 0,40. **Let op:** de BOE-noten melden dat de coëfficiëntenupdates voor 2025 (RDL 9/2024) en 2026 (RDL 16/2025) door het Congres zijn ingetrokken; de geconsolideerde tabel hierboven is dus de geldende. | Art. 107.4 TRLRHL (blok a107, geldende versie) | 2 |
| IIVTNU — werkelijke methode | Op verzoek: grondslag = werkelijke waardestijging van de grond (verschil koop/verkoop × kadastraal grondaandeel) als die lager is | Art. 107.5 en 104.5 TRLRHL | 2 |
| IIVTNU — geen heffing zonder waardestijging | "No se producirá la sujeción al impuesto en las transmisiones de terrenos respecto de los cuales se constate la inexistencia de incremento de valor" | Art. 104.5 TRLRHL | 2 |
| IIVTNU — tarief | ≤ 30 % (gemeente kiest; per periode mogelijk) | Art. 108.1 TRLRHL | 2 |
| IIVTNU — **Xàbia**: tarief en gemeentelijke coëfficiënten | **ONBEKEND** — ordenanza niet bereikbaar (JS-portaal); alleen vindbaar via de sede electrónica of Xàbia Gestió Tributària (C/ Mayor 15, 965 790 500, gestio.tributaria@ajxabia.org) | https://www.ajxabia.com/ver/1189/ordenanzas-fiscales.html → https://xabia.sedelectronica.es/transparency/9dc46a0e-8b13-4022-824e-000f75336158/ | 7 |
| Modelaanname plusvalía bij korte bezitsduur (route A: 1–2 jaar) | coëfficiënt 0,15/0,14 × kadastrale grondwaarde × ≤ 30 % — vaak beperkt bedrag; of nihil bij werkelijke methode als de grond niet in waarde steeg. Berekenen per object met kadastrale grondwaarde. | — | 5 |
| **IRPF** op vermogenswinst (particulier verkoper, resident) — schaal 2026 | 19 % tot 6.000 € · 21 % 6.000–50.000 · 23 % 50.000–200.000 · 27 % 200.000–300.000 · 30 % daarboven (staatsdeel art. 66: 9,5/10,5/11,5/13,5/15 + autonoom deel art. 76 idem) | Ley 35/2006 art. 66 en 76 (BOE-A-2006-20764), geldend sinds 1-1-2025 (Ley 7/2024) | 2 |
| **IS** (vennootschap) — algemeen | **25 %** | Art. 29.1 Ley 27/2014 (BOE-A-2014-12328) | 2 |
| IS — micro-onderneming (netto-omzet vorig jaar < 1 M€) | 2026: **19 %** tot 50.000 € grondslag, **21 %** daarboven (2025: 21/22; eindregime 17/20) | DT 44ª LIS (blok dt-6) en art. 29.1 | 2 |
| IS — entidad de reducida dimensión (art. 101, < 10 M€) | 2026: **23 %** (2025: 24; 2027: 22; 2028: 21; eindregime 20) | DT 44ª LIS | 2 |
| IS — nieuw opgerichte vennootschap | 15 % in het eerste winstjaar en het volgende; **niet** voor entidades patrimoniales en niet bij voortzetting van een eerder door verbonden personen gedreven activiteit | Art. 29.1 LIS | 2 |
| **IRNR** — niet-residente verkoper (EU/EER) | 19 % op de winst; **koper houdt 3 % van de prijs in** (modelo 211) — geldt ook voor ons als koper van een niet-resident in Jávea | Art. 25.1.a/f en 25.2 RDLeg 5/2004 (BOE-A-2004-4527) | 2 |
| Certificado de eficiencia energética | Verplicht bij verkoop; kosten niet gereguleerd; registratietarief GVA niet gevonden | — | 7 — ONBEKEND |
| Cédula / declaración responsable de segunda ocupación (Xàbia) | Gemeentelijke tasa niet gevonden (ordenanza tasas niet bereikbaar) | — | 7 — ONBEKEND |

---

## 4. Bouw- en renovatiekosten 2025/2026 Alicante/Costa Blanca (opdracht d)

### 4.1 Status van de referentiebronnen

| Bron | Wat het is | Toegang/kosten | Gevonden €/m²? | Bron-URL | Bewijs | Registerstatus |
|---|---|---|---|---|---|---|
| **IVE — Base de Datos de Construcción (BDC 2026)** | Officiële prijzendatabank van het Instituto Valenciano de la Edificación (Generalitat) | Betaald: "Suscripción IVE online" 69,99 € (registratie 35 € + 35 €/jaar) of "BDC26 BC3 instalable" 225 € (3 activaties, Presto/Arquímedes/Menfis); downloads van edities sinds 2015 | Niet zonder abonnement; bdc.five.es toont alleen een splash | https://productos.five.es/producto/base-de-datos-de-construccion · https://bdc.five.es/ | 1 | CONTRACT OF TOESTEMMING NODIG (aankoop abonnement, akkoord Jan) |
| **CYPE Generador de precios** | Commerciële eenheidsprijzen-generator (> 6.500 eenheden, obra nueva/rehabilitación) | Gratis na registratie; gebruiksvoorwaarden in "aviso legal" | Geen totaal-€/m² zichtbaar zonder login | https://www.generadordeprecios.info/ · https://shop.cype.com/es/aviso-legal/ | 1 | TECHNISCH ONDERZOEK NODIG (voorwaarden overname prijzen) |
| Ministerio de Transportes — Visados de dirección de obra (PEM en m² per provincie) | Officiële statistiek waaruit PEM/m² per provincie te berekenen is | **HTTP 403** voor deze sessie | Nee | https://www.transportes.gob.es/…/visados-de-direccion-de-obra | 7 | TECHNISCH ONDERZOEK NODIG (handmatig downloaden) |
| CSCAE "Datos de visado 2025" (5-2-2026) | Landelijke visadocijfers: 36.575.205 m² visado (+3,56 %), 122.122 nieuwbouwwoningen, 55.558 rehabilitaties; Comunitat Valenciana +7,08 % oppervlak | Openbaar | Geen PEM/m², geen provincie | https://www.cscae.com/index.php/cscae/sala-de-comunicacion/9340-sector-edificacion-vigor-2025-niveles | 2 | ALLEEN HANDMATIG |
| COACV (Colegio de Arquitectos CV) | Startpagina noemt "Cálculo de Tasas" en "Datos estadísticos" onder Visado | Geen módulo/€/m² op de startpagina | Nee | https://www.coacv.org/ | 7 | TECHNISCH ONDERZOEK NODIG |
| CTAA (Colegio de Arquitectos de Alicante) | Startpagina zonder módulo; /visado/ = 404 | — | Nee | https://www.ctaa.net/ | 7 | TECHNISCH ONDERZOEK NODIG (bellen: 965 21 84 00) |
| COAATIE Alicante | TLS-certificaatfout op https en http-omleiding; niet omzeild | — | Nee | https://www.coaatalicante.org/ | 7 | TECHNISCH ONDERZOEK NODIG |
| **Eigen nacalculaties TREE Constructions** | Excel-projectadministratie van Jan (buiten deze mappen) | Niet in bestanden gevonden | — | `~/tree-es/constructions/CLAUDE.md` | 3 (afwezigheid) | ⏸️ ACTIE VOOR JAN |
| habitissimo prijsgidsen | Offerteplatform; landelijke gemiddelden op basis van offerteaanvragen | Openbaar | Ja, zie 4.3 | zie 4.3 | 1 (lage zekerheid) | ALLEEN HANDMATIG (indicatie) |

### 4.2 Definities en opslagen: PEM, PEC, honoraria, ICIO/tasas, btw

| Begrip | Definitie / waarde | Bron | Bewijs |
|---|---|---|---|
| **PEM** (presupuesto de ejecución material) | Som van hoeveelheden × eenheidsprijzen + partidas alzadas; excl. algemene kosten, winst, honoraria, btw | Art. 131 RD 1098/2001 (BOE-A-2001-19995, blok a131) | 2 |
| **PEC / presupuesto base de licitación** (aannemingssom) | PEM + gastos generales **13–17 %** + beneficio industrial **6 %** (conventie uit het publieke aanbestedingsrecht; in private contracten vrij, maar in de praktijk de rekenbasis van aannemers) | Art. 131.1.a–b RD 1098/2001 | 2 (definitie) / 4 (toepassing privaat) |
| Btw over de aannemingssom | 10 % of 21 % (zie 1.4) over PEM + GG + BI | Art. 131.2 RD 1098/2001; art. 90–91 LIVA | 2 |
| Honoraria architect/aparejador | Geen officiële percentages (verbod op baremos, art. 14 Ley 2/1974); marktindicatie 10–12 % (habitissimo, 1) | zie 2.3 | 2 / 1 |
| **ICIO** | Grondslag = "coste real y efectivo … coste de ejecución material" **exclusief** btw, tasas, honoraria en aannemerswinst; tarief door gemeente, **≤ 4 %**; verschuldigd bij start van de werken | Art. 102.1–102.4 TRLRHL (blok a102) | 2 |
| ICIO Xàbia | ONBEKEND (ordenanza niet bereikbaar) — model rekent conservatief met het wettelijk maximum 4 % | — | 7 / 5 |
| Tasa por licencia urbanística Xàbia | ONBEKEND | — | 7 |
| "Llave en mano" (turnkey) villa | = PEC + honoraria + ICIO/tasas + aansluitingen + btw + eventueel keuken/inrichting; geen officiële definitie | — | 4 |

### 4.3 Bandbreedtes per m² — wat er wél met bron beschikbaar is (bewijstype 1, lage zekerheid, landelijk; btw-status per pagina niet eenduidig)

> Waarschuwing: dit zijn gemiddelden van offerteaanvragen op één platform, voor het hele land en vooral voor standaardwoningen. Het villasegment van Jávea (hellend terrein, uitzichtlocaties, hoog afwerkingsniveau, keermuren, zwembad, kelderparkeren) ligt naar verwachting **boven** deze bandbreedtes — dat is een inferentie (4), geen meting. Gebruik ze uitsluitend als ondergrens-sanity-check totdat eigen nacalculaties of de IVE-BDC beschikbaar zijn.

| Post | Indicatie | Datum bijgewerkt | Basis | URL | Bewijs |
|---|---|---|---|---|---|
| Nieuwbouw woning (bouw, zonder grond) | gemiddeld **1.000 €/m²**, bandbreedte **800–1.200 €/m²**; Comunitat Valenciana "850 €/m²"; voorbeeld 240 m² sleutelklaar ≈ 230.000 €; bijkomend: "honorarios (10-12 %)", "licencias (6 %)", "trámites (5 %)" | 18-06-2026 | 105.630 offerteaanvragen | https://www.habitissimo.es/presupuestos/construccion-casas | 1 |
| Integrale renovatie | gemiddeld **750 €/m²**, bandbreedte **650–900 €/m²**; breed "400–600 €/m² (medio-baja) tot 800–1.200 €/m²"; Alicante-projecten 25.000–38.000 € (kleine projecten) | 04-02-2025 | 274.165 offerteaanvragen | https://www.habitissimo.es/presupuestos/reforma-integral | 1 |
| Gerichte renovatie — keuken | gemiddeld **8.000 €** (3.500–12.500 €); ≈ 850 €/m²; Alicante 3.000–7.000 € | 04-02-2025 | 92.649 aanvragen | https://www.habitissimo.es/presupuestos/reforma-cocinas | 1 |
| Gerichte renovatie — badkamer | gemiddeld **3.000 €** (1.200–4.500 €); 650–750 €/m²; Valencia 1.800–4.000 € | 10-06-2026 | 192.633 aanvragen | https://www.habitissimo.es/presupuestos/reforma-banos | 1 |
| Installaties (elektra, water, klimaat) | Niet opgehaald op 14-09-2026 — **aangevuld op 15-09-2026, zie §4.5** | — | — | — | 1 (§4.5) |
| Beperkte opwaardering (schilderwerk, vloeren, kozijnen) | Niet opgehaald op 14-09-2026 — **aangevuld op 15-09-2026, zie §4.5** | — | — | — | 1 (§4.5) |
| Zwembad (≈ 50 m³) | gemiddeld **14.000 €** (10.000–19.000 €); ingegraven 16.000 €; verwarmd 20.000 € | 04-02-2025 | 67.386 aanvragen | https://www.habitissimo.es/presupuestos/construccion-piscinas | 1 |
| Keermuren / buitenruimte op hellend terrein | gemiddeld **150 €/m²** muurvlak (90–250 €/m²; breed 70–200 €/m²); 10 m natuursteen 2.500 €, schanskorf 1.200 €, betonblok 1.000 € | 16-09-2024 | 26.506 aanvragen | https://www.habitissimo.es/presupuestos/muros-de-contencion | 1 |
| Sloop woning | gemiddeld **50 €/m²** (10–90 €/m²); 150 m² woning ≈ 9.000 €; handmatig vanaf 5 €/m², machinaal vanaf 60 €/m² | 10-06-2026 | 15.208 aanvragen | https://www.habitissimo.es/presupuestos/demoliciones | 1 |
| Nieuwbouw villa Jávea — PEM en llave en mano | **ONBEKEND** in officiële/semi-officiële bron; alleen te vullen uit IVE-BDC of eigen nacalculatie | — | — | — | 7 |

### 4.4 Wat nodig is om 4.3 bruikbaar te maken

⏸️ **ACTIE VOOR JAN:** lever uit de Excel-projectadministratie 3–5 nacalculaties (PEM en aanneemsom per m² bebouwd, exclusief btw, met jaar) voor: (1) nieuwbouw villa, (2) integrale renovatie, (3) keuken + badkamers via Sani-Kitchen Projects, (4) zwembad, (5) keermuren/terrein. Dat is de enige bron met bewijstype 3 voor het Jávea-segment. Daarnaast: beslissen of de IVE-BDC-online (69,99 €/jaar) wordt aangeschaft (regel: niets kopen zonder akkoord).

### 4.5 Aanvulling 15-09-2026 — installaties en beperkte opwaardering

**Waarom:** in §4.3 stonden deze twee posten uit opdracht d als "niet opgehaald". Ze zijn op 15-09-2026 aangevuld uit dezelfde prijsgidsen van habitissimo (geen zoekmachine gebruikt; de gidsen zijn gevonden via de overzichtspagina https://www.habitissimo.es/presupuestos). Zelfde waarschuwing als §4.3: landelijke gemiddelden uit offerteaanvragen, vooral voor appartementen van 70–90 m², **btw-status op geen enkele pagina vermeld** (7), en niet representatief voor het villasegment van Jávea (4). De pagina's zijn via WebFetch samengevat; alleen de elektra-bedragen zijn daarna letterlijk nagecontroleerd (citaten hieronder). Controledatum van deze regels: 15-09-2026.

**Installaties (onderdeel van gerichte renovatie)**

| Post | Indicatie volgens de bron | Pagina bijgewerkt | Basis | URL | Bewijs | Btw |
|---|---|---|---|---|---|---|
| Elektrische installatie volledig vernieuwen (woning) | vanaf **1.700 €**; bij 90 m² met ca. 60 lichtpunten tot **3.000 €**. Letterlijk: "en una vivienda de 90 m² y con unos 60 puntos de luz, el precio puede alcanzar los 3.000 €" | 10-06-2026 | + 140.908 offerteaanvragen | https://www.habitissimo.es/presupuestos/electricistas | 1 | niet vermeld (7) |
| Elektricien — uurtarief en klussen | gemiddeld 35 €/u (15–75 €/u); Alicante (klussen, van klein tot groot) 75–3.800 € | 10-06-2026 | idem | idem | 1 | niet vermeld |
| Loodgieterswerk (fontanería) volledig, woning | **2.000–3.500 €**; losse klus gemiddeld 175 € (60–580 €); Alicante uurtarief 25–35 €/u | 10-06-2026 | + 78.950 aanvragen | https://www.habitissimo.es/presupuestos/fontaneros | 1 | niet vermeld |
| Airconditioning / klimaat | gemiddeld **2.300 €** (800–5.000 €); split 550–1.500 €; multisplit 1.000–2.500 €; kanalen/cassette 1.500–5.000 €; Alicante 600–3.000 € | 04-02-2025 | + 166.851 aanvragen | https://www.habitissimo.es/presupuestos/aire-acondicionado | 1 | niet vermeld |
| Deelposten in een woningrenovatie (richtbedragen per post, hele woning) | elektra ≈ **3.000 €**; fontanería/verwarming ≈ **10.000 €**; binnen- en buitentimmerwerk ≈ **5.000 €**; schilderwerk ≈ **1.500 €** (4–15 €/m²); vloeren 10–80 €/m² materiaal + 10–25 €/m² arbeid | 10-06-2026 | + 274.165 aanvragen | https://www.habitissimo.es/presupuestos/reformas-viviendas | 1 | niet vermeld |

**Beperkte opwaardering (cosmetisch: schilderwerk, vloeren, kozijnen)**

| Post | Indicatie volgens de bron | Pagina bijgewerkt | Basis | URL | Bewijs | Btw |
|---|---|---|---|---|---|---|
| Schilderwerk binnen | gemiddeld **14 €/m²** (5–50 €/m²); binnenmuren 10–15 €/m², 15–25 €/m² inclusief egaliseren; appartement 90 m² ≈ **1.200 €** | 18-06-2026 | + 315.282 aanvragen | https://www.habitissimo.es/presupuestos/pintores | 1 | niet vermeld |
| Vloer vervangen (materiaal + plaatsing) | gemiddeld **40 €/m²** (15–80 €/m²); hout 35 · porcelánico 10–20 · laminaat 20 · gietvloer 40 · vinyl 15 · terrazzo 20 · marmer 60 · microcement 75 €/m² | 10-06-2026 | + 30.968 aanvragen | https://www.habitissimo.es/presupuestos/cambiar-suelo | 1 | niet vermeld |
| PVC-ramen | gemiddeld **350 €/stuk** (250–600 €); 100–250 €/m²; Alicante 100–400 €/stuk | 23-10-2024 | + 89.708 aanvragen | https://www.habitissimo.es/presupuestos/ventanas-pvc | 1 | niet vermeld |

**Tegenstrijdigheid binnen dezelfde bron (bewijstype 7):** de gids *reforma integral* (bijgewerkt 04-02-2025, §4.3) noemt gemiddeld 750 €/m² (650–900 €/m²); de gids *reformas viviendas* (bijgewerkt 10-06-2026) noemt gemiddeld **550 €/m² (460–650 €/m²)**, met kwaliteitsklassen 400–600 / 600–800 / 800–1.000 €/m² — en beide pagina's melden hetzelfde aantal aanvragen (274.165). Eén "gemiddelde" voor integrale renovatie is daarom niet te geven; het model hanteert tot de nacalculaties van Jan binnen zijn de brede band **400–1.200 €/m²** als sanity-check en géén puntwaarde.

**Gebruik in het model (bewijstype 4/5):**
- Route A "gerichte renovatie" = som van posten (keuken §4.3 + badkamers §4.3 × aantal + elektra + fontanería + klimaat), niet €/m² × oppervlak. Opschalen van appartementbedragen naar een villa van 200–300 m² is een **aanname** (5); lineair schalen op m² is niet onderbouwd.
- Route A "beperkte opwaardering" = schilderwerk m² wandoppervlak × €/m² + vloeren m² × €/m² + kozijnen × aantal. Het wandoppervlak per object uit de plattegrond meten; hiervoor is in dit rapport geen kengetal met bron.
- Btw: alle bedragen behandelen als **excl. btw [te verifiëren]**; voor een SL als koper 21 % erbovenop (§1.4), tenzij de rehabilitación-route geldt.

---

## 5. Financiering en holdingkosten (opdracht e)

### 5.1 Rente en referentietarieven (Banco de España, Boletín Estadístico, hoofdstuk 19)

| Parameter | Waarde | Periode | Bron | Bewijs |
|---|---|---|---|---|
| **Euríbor 12 maanden** (officiële hypotheekreferentie) | **2,954 %** | augustus 2026 (gepubliceerd BOE 02-09-2026) | Tabel 19.1 kolom 5: https://www.bde.es/webbe/es/estadisticas/compartido/datos/pdf/a1901.pdf; persbericht BdE 01-09-2026 "El euríbor se sitúa en el 2,954 % en agosto, 0,840 puntos más que hace un año" | 2 |
| Euríbor 12 m, verloop 2026 | jan 2,245 · feb 2,221 · mrt 2,565 · apr 2,747 · mei 2,804 · jun 2,798 · jul 2,855 · aug 2,954 | — | Tabel 19.1 | 2 |
| Euríbor 12 m **september 2026** | Nog niet gepubliceerd op 14-09-2026 (maand loopt) — **[te verifiëren]** begin oktober | — | — | 7 |
| Euríbor 3 m / 6 m | 2,513 % / 2,713 % | aug 2026 | Tabel 19.1 | 2 |
| IRPH (tipo medio préstamos hipotecarios > 3 años, entidades) | 3,077 % | jul 2026 | Tabel 19.1 kolom 11 | 2 |
| IRS 5 jaar / 10 jaar | 3,067 % / 3,227 % | aug 2026 | Tabel 19.1 kolom 24/26 | 2 |
| Wettelijke rente / fiscale vertragingsrente / handelsvertragingsrente | 3,25 % / 5,25 % / 10,40 % | 2026 (2e halfjaar) | Tabel 19.1 kolommen 16–19 | 2 |
| **Nieuwe woninghypotheken huishoudens (TEDR, gewogen gemiddelde)** | **2,89 %** (voorlopig); naar rentevastperiode: ≤ 1 jr 3,16 · 1–5 jr 3,79 · 5–10 jr 3,80 · > 10 jr 2,66 | jul 2026 | Tabel 19.4: https://www.bde.es/webbe/es/estadisticas/compartido/datos/pdf/a1904.pdf | 2 |
| Nieuwe leningen aan **niet-financiële vennootschappen** (TEDR) | **3,68 %** (heronderhandelingen 3,92 %) | jul 2026 | Tabel 19.3: https://www.bde.es/webbe/es/estadisticas/compartido/datos/pdf/a1903.pdf | 2 |
| Krediet huishoudens "otros fines" (incl. individuele ondernemers) | 4,56 % | jul 2026 | Tabel 19.3/19.4 | 2 |
| Hypotheekrente/LTV voor **niet-residenten** of **vennootschappen** (promotor-/bridge-financiering) | Niet officieel gepubliceerd; per bank individueel | — | — | 7 — ONBEKEND; offertes bij 2–3 banken |
| Opmerking | TEDR = zonder kosten/verzekeringen; TAE ligt hoger. Modelaanname rente route A/B: Euríbor 12 m + opslag [ONBEKEND] — werkhypothese 4,5 % voor niet-hypothecaire projectfinanciering, expliciet te vervangen | — | 5 |

### 5.2 Holdingkosten per object

| Post | Waarde | Bron | Bewijs |
|---|---|---|---|
| **IBI** — wettelijke bandbreedte stedelijk | min./suppletoir **0,4 %**, max. **1,10 %** van de kadastrale waarde (+ opslagen tot 0,07/0,06 punten bij bepaalde gemeenten); tot 50 % opslag mogelijk op permanent leegstaande woningen | Art. 72.1, 72.3, 72.4 TRLRHL (blok a72) | 2 |
| IBI — **Xàbia** tarief 2025/2026 | **ONBEKEND**; de gemeente meldt: "Gracias a la rebaja del tipo impositivo del IBI en 2025…" (verlaging in 2025, percentage niet genoemd) | Gids nieuwe afvalheffing (p. 4): https://www.ajxabia.com/bd/archivos/archivo5252.pdf | 2 (verlaging) / 7 (tarief) |
| **Tasa de residuos Xàbia** | Nieuwe Ordenanza Fiscal 03/03, in werking 01-01-2025 (Ley 7/2022): niet meer vast, **variabel deel via coëfficiënt op de kadastrale waarde**; **+ 20 € per toeristische slaapplaats** (registro AVT); eigenaar van een local is belastingplichtig; kortingen 50 % (pensioen naar IPREM-grens, familia numerosa, kwetsbaarheid); bedrag per woning alleen via Oficina Virtual Tributaria | Gids (p. 2–6) en aviso: https://www.ajxabia.com/bd/archivos/archivo5255.pdf; https://xabiagt.com/ | 2 (regels) / 7 (bedrag) |
| Kadastrale waarde per object | Nodig voor IBI, afvalheffing en plusvalía; opvraagbaar per referentie (Sede Catastro; zie R04) | R04 | 2 |
| Opstalverzekering, comunidad de propietarios, water/elektra/alarm, tuin/zwembadonderhoud | Geen gepubliceerde referenties opgehaald | — | 7 — ONBEKEND; werkhypothese in model als "holding_per_maand", door Jan in te vullen |
| Verplichte 10-jaars verzekering (seguro decenal) bij nieuwbouw voor verkoop (route B) | Verplicht volgens LOE (Ley 38/1999) — niet opgehaald; premie ONBEKEND | — | 4 / 7 — [te verifiëren] |

### 5.3 Tijdsaannames (uit R12 — nog niet beschikbaar)

R12 bestond op 14-09-2026 23:40 nog niet in `onderzoek/`. **Hercontrole 15-09-2026:** nog steeds geen R12-bestand in `~/tree-es/deal-hunter/` of `onderzoek/` (mapinhoud bekeken; bewijstype 3). Het model gebruikt daarom benoemde **placeholders**: licentietermijn Xàbia (obra mayor / declaración responsable), bouwduur villa, verkoopduur in Jávea. Zodra R12 er is, worden die waarden overgenomen met bron. Tot dan: in alle berekeningen `maanden_totaal` expliciet als aanname tonen.

---

## 6. Rekenmodel-schets route A en route B (opdracht f)

### 6.1 Kostenposten route A — kopen, renoveren, verkopen (masterprompt §21)

| Post | Waarde / formule | Bron | Zekerheid (bewijstype) | Btw |
|---|---|---|---|---|
| Koopprijs P | variabele (te bepalen) | — | — | — |
| ITP | 9 % × max(P, valor de referencia); 11 % als grondslag > 1 M€ | §1.1, §1.5 | 2 | geen |
| Notaris + register | schaal §2.1–2.2 (≈ 0,15 % bij 500 k€), + kopieën; + btw [te verifiëren] | §2 | 2 / 5 | 21 % (4) |
| Gestoría, advocaat, taxatie | ONBEKEND — invullen | §2.3 | 7 | 21 % |
| Bouwkosten renovatie (PEM + GG + BI) | uit eigen nacalculatie; noodindicatie §4.3 | §4 | 3 (na ACTIE) / 1 | **21 %** voor vennootschap; niet-aftrekbaar als verkoop btw-vrij (tenzij rehabilitación-route) — 4 |
| Honoraria architect/aparejador | ONBEKEND (indicatie 10–12 %) | §2.3 | 1 | 21 % |
| ICIO + tasa licencia | ≤ 4 % × PEM (Xàbia-tarief ONBEKEND) + tasa ONBEKEND | §4.2 | 2 / 7 | geen |
| Financieringskosten | (P × LTV + bouw × LTC) × rente × maanden/12; rente = Euríbor 12 m (2,954 % aug 2026) + opslag ONBEKEND | §5.1 | 2 / 7 | geen |
| Holdingkosten | IBI (tarief ONBEKEND × kadastrale waarde) + afvalheffing + verzekering + nuts + comunidad, × maanden | §5.2 | 7 | — |
| Verkoopkosten | commissie 3–5 % + 21 % btw (eigen netwerk, 3); CEE en cédula ONBEKEND | §3 | 3 / 7 | 21 % |
| Plusvalía IIVTNU | grondwaarde kadastraal × coëfficiënt (0,15/0,14 bij 1–3 jaar) × tarief ≤ 30 % (Xàbia ONBEKEND), of nihil bij geen stijging | §3 | 2 / 7 | — |
| Risicoreserve | % van bouw + honoraria — **input Jan** (werkhypothese 10 %) | — | 5 | — |
| Winstbelasting (buiten projectresultaat) | IS 25 % / 19–21 % (micro) / 23 % (ERD) of IRPF 19–30 % | §3 | 2 | — |
| **Rendementseis** | **ONBEKEND — input van Jan** (op totale projectkosten, op eigen vermogen, of als marge op verkoop) | masterprompt §3 | 7 | — |

### 6.2 Kostenposten route B — perceel kopen, bouwen, verkopen

| Post | Waarde / formule | Bron | Zekerheid | Btw |
|---|---|---|---|---|
| Grondprijs P | variabele | — | — | — |
| Belasting op grond | van particulier: ITP 9 %/11 %; van ondernemer: btw 21 % (aftrekbaar voor promotor-SL, 4) + AJD 1,4 % | §1.4, §1.7 | 2 | zie links |
| Notaris/register grond | schaal §2 | §2 | 2 | 21 % |
| Bouwkosten villa (PEM + 13–17 % GG + 6 % BI) | eigen nacalculatie; landelijke indicatie 800–1.200 €/m² (1, lage zekerheid; Jávea-villa vermoedelijk hoger, 4) | §4 | 3 / 1 | **10 %** (contract promotor–aannemer, woning ≥ 50 %) — aftrekbaar voor de promotor die met btw verkoopt (4) |
| Zwembad, keermuren, terrein, aansluitingen | indicaties §4.3; aansluitkosten nuts ONBEKEND | §4.3 | 1 / 7 | 10 %/21 % [te verifiëren per post] |
| Honoraria (proyecto, dirección de obra, aparejador, geotechniek, topografie, CEE) | ONBEKEND (indicatie 10–12 % totaal) | §2.3 | 1 | 21 % |
| ICIO ≤ 4 % × PEM + tasa licencia obra mayor | Xàbia ONBEKEND | §4.2 | 2 / 7 | — |
| AJD declaración de obra nueva + (evt.) división horizontal | 1,4 % (grondslag [te verifiëren], §1.3) | §1.3 | 2 / 7 | — |
| Seguro decenal, OCT | verplicht bij verkoop nieuwbouw; premie ONBEKEND | §5.2 | 4 / 7 | — |
| Financiering | grond + bouw × rente × tijd (NFC-rente jul 2026 3,68 % als referentie; promotorlening ONBEKEND) | §5.1 | 2 / 7 | — |
| Verkoop: btw 10 % is voor rekening koper; opbrengst voor ons = prijs excl. btw; koper betaalt ook AJD 1,4 % | §1.4 | 2 | — |
| Verkoopkosten, plusvalía, reserve, rendementseis | als route A | — | — | — |

### 6.3 Maximale koopprijs — formule in woorden

1. Kies het **conservatieve scenario** voor de verkoopopbrengst (§20: bandbreedte, peildatum, vergelijkingsobjecten) en de tijdsduur (R12).
2. Tel alle kosten die **niet** van de koopprijs afhangen: bouw + honoraria + ICIO/tasas + holding + reserve + verkoopkosten + plusvalía.
3. Bepaal de kosten die **wél** van de koopprijs afhangen: ITP (9 %/11 % over max(P, valor de referencia)), notaris/register (schaal), financieringsrente over het gefinancierde deel van P, en de risicoreserve als die (deels) op P is gebaseerd.
4. Het projectresultaat vóór winstbelasting = verkoopopbrengst − P − prijsafhankelijke kosten(P) − vaste kosten (§21).
5. **Rendementseis (input Jan)** als drempel: bijvoorbeeld resultaat ≥ r × totale projectkosten (rendement op kosten) of resultaat ≥ m × verkoopopbrengst (marge).
6. Omdat de belastingen en de rente van P afhangen (en het 11 %-tarief bij 1 M€ een sprong maakt), is er geen gesloten formule: **itereer** — begin met P = 0 en P = verkoopopbrengst, neem het midden, bereken het resultaat, en verklein het interval tot de hoogste P waarbij de eis nog wordt gehaald (bisectie, ca. 60 stappen tot op de euro).
7. Rapporteer naast dit maximum ook: vraagprijs, indicatieve marktwaarde, openingsbod en gewenste uitkomst (§22), en de gevoeligheid voor −10 % opbrengst, +15 % bouwkosten en +6 maanden.

### 6.4 Python-functie (zonder externe libraries; getest onder Python 3.9 op 14-09-2026)

```python
# Rekenmodel-schets TREE Deal Hunter (R14). Alle standaardwaarden zijn wettelijke tarieven (bewijstype 2)
# of expliciet gemarkeerde werkhypothesen; ONBEKENDE posten staan op 0 en moeten worden ingevuld.

def arancel_schaal(waarde, schaal, vast_eerste_tranche):
    """Degressieve schaal (RD 1426/1989 en RD 1427/1989, Número 2). Excl. btw."""
    bedrag = vast_eerste_tranche
    ondergrens = 6010.12
    for bovengrens, promille in schaal:
        if waarde > ondergrens:
            bedrag += (min(waarde, bovengrens) - ondergrens) * promille / 1000.0
        ondergrens = bovengrens
    return bedrag

NOTARIS_SCHAAL  = [(30050.61, 4.5), (60101.21, 1.5), (150253.03, 1.0), (601012.10, 0.5), (6010121.04, 0.3)]
REGISTER_SCHAAL = [(30050.61, 1.75), (60101.21, 1.25), (150253.03, 0.75), (601012.10, 0.30), (10**12, 0.20)]

def notaris_matriz(waarde):
    """Número 2 arancel notarial, minus 5 % rebaja (RDL 8/2010). Excl. btw, excl. kopieën/folios."""
    return arancel_schaal(waarde, NOTARIS_SCHAAL, 90.151816) * 0.95

def register_inscripcion(waarde):
    """Número 2 arancel registral, minus 5 % rebaja; min 24,04 / max 2.181,67 euro. Excl. btw."""
    b = arancel_schaal(waarde, REGISTER_SCHAAL, 24.040484)
    return max(24.040484, min(2181.673939, b)) * 0.95

def itp_cv(prijs, valor_referencia=None):
    """ITP Comunitat Valenciana vanaf 01-06-2026: 9 % (art. 13.Uno Ley 13/1997), 11 % boven 1.000.000 euro.
    Grondslag = max(prijs, valor de referencia) (art. 10.2 TRLITPAJD)."""
    grondslag = max(prijs, valor_referencia or 0)
    return grondslag * (0.11 if grondslag > 1_000_000 else 0.09)

def aankoopkosten(prijs, regime="ITP", valor_referencia=None, ajd_tarief=0.014, iva_tarief=0.21,
                  gestoria=0.0, due_diligence=0.0, taxatie=0.0):
    """regime 'ITP' (tweedehands/particulier) of 'IVA' (nieuwbouw 10 % / solar van ondernemer 21 %, + AJD 1,4 %).
    gestoria, due_diligence, taxatie: ONBEKEND -> invullen."""
    if regime == "ITP":
        belasting = itp_cv(prijs, valor_referencia)
    else:
        belasting = prijs * iva_tarief + prijs * ajd_tarief
    return belasting + notaris_matriz(prijs) + register_inscripcion(prijs) + gestoria + due_diligence + taxatie

def projectresultaat(koopprijs, p):
    """Projectresultaat vóór winstbelasting volgens masterprompt §21. p = dict met parameters."""
    aankoop = aankoopkosten(koopprijs, p["regime"], p.get("valor_referencia"),
                            gestoria=p.get("gestoria", 0), due_diligence=p.get("due_diligence", 0),
                            taxatie=p.get("taxatie", 0))
    bouw = p["bouwkosten_excl_btw"] * (1 + p["btw_bouw"] * (0 if p.get("btw_terugvorderbaar") else 1))
    honoraria = p["bouwkosten_excl_btw"] * p["honoraria_pct"]
    icio = p["pem"] * p["icio_tarief"] + p.get("tasa_licentie", 0)
    projectkosten = koopprijs + aankoop + bouw + honoraria + icio + p.get("overig", 0)
    maanden = p["maanden_totaal"]                       # placeholder tot R12
    financiering = (koopprijs * p["ltv"] + bouw * p.get("ltc_bouw", 0)) * p["rente_jaar"] * maanden / 12.0
    holding = p["holding_per_maand"] * maanden          # IBI, afval, verzekering, nuts: ONBEKEND -> invullen
    reserve = (bouw + honoraria) * p["risicoreserve_pct"]
    verkoop = p["verkoopopbrengst"]                     # conservatief scenario, excl. btw bij nieuwbouw
    verkoopkosten = verkoop * p["makelaar_pct"] + p.get("plusvalia", 0) + p.get("overige_verkoopkosten", 0)
    resultaat = verkoop - projectkosten - financiering - holding - reserve - verkoopkosten
    totaal_kosten = projectkosten + financiering + holding + reserve + verkoopkosten
    return {"resultaat": resultaat, "totaal_kosten": totaal_kosten, "aankoopkosten": aankoop,
            "marge_op_verkoop": resultaat / verkoop if verkoop else None,
            "rendement_op_kosten": resultaat / totaal_kosten if totaal_kosten else None}

def maximale_koopprijs(p, rendementseis_op_kosten, laag=0.0, hoog=None, iteraties=60):
    """Bisectie: hoogste koopprijs waarbij resultaat / totale kosten >= rendementseis.
    rendementseis_op_kosten is een ONBEKENDE input van Jan (bijv. 0.15)."""
    hoog = hoog if hoog is not None else p["verkoopopbrengst"]
    for _ in range(iteraties):
        mid = (laag + hoog) / 2.0
        r = projectresultaat(mid, p)
        if r["rendement_op_kosten"] is not None and r["rendement_op_kosten"] >= rendementseis_op_kosten:
            laag = mid
        else:
            hoog = mid
    return laag
```

**Testuitvoer (bewijstype 5, uitsluitend ter illustratie van de werking — de parameters zijn werkhypothesen, geen bevestigde cijfers van Jan):** met verkoopopbrengst 1.100.000 €, renovatie 250.000 € excl. btw (btw 21 % niet terugvorderbaar), honoraria 10 %, ICIO 4 % over PEM 210.000 €, 14 maanden, rente 4,5 % op 0 % LTV (dus 0), holding 400 €/maand, reserve 10 %, makelaar 4 %:

| Rendementseis op totale kosten | Maximale koopprijs | Projectresultaat | Marge op verkoop |
|---|---|---|---|
| 10 % | 533.009 € | 100.000 € | 9,1 % |
| 15 % | 493.148 € | 143.478 € | 13,0 % |
| 20 % | 456.609 € | 183.333 € | 16,7 % |

Notaris/register uit dezelfde functie: 250.000 € → 364,26 / 191,15 €; 500.000 € → 483,01 / 262,40 €; 1.000.000 € → 644,71 / 367,00 €.

**Hercontrole 15-09-2026 (bewijstype 3):** de code hierboven is letterlijk uit dit bestand geknipt en opnieuw uitgevoerd met `/usr/bin/python3` (3.9) en dezelfde parameters; de uitvoer is identiek aan beide tabellen (533.009 / 493.148 / 456.609 €; notaris/register idem). Beperkingen van de schets die daarbij opvielen (4): (a) honoraria krijgen in de functie geen btw; (b) bij `regime="IVA"` telt de btw op de grond altijd als kosten, ook als een promotor-SL die kan aftrekken — voor route B dan `iva_tarief=0` meegeven en alleen AJD rekenen; (c) de risicoreserve wordt over bouwkosten inclusief niet-aftrekbare btw berekend.

---

## 7. Open vragen en acties

**Open vragen (voor gestor/fiscalist, bewijstype 6 nodig):**
1. Welke grondslag hanteert de ATV in 2026 bij veilingtoewijzing: precio de remate (art. 39 RITP) of valor de referencia (art. 10.2 TRLITP)?
2. Is de rehabilitación-route (art. 20.Uno.22º.B LIVA: > 25 % van de aankoopprijs excl. grond én > 50 % structuur/gevel/dak) haalbaar en fiscaal voordelig voor route A (verkoop met btw 10 % i.p.v. ITP 9 % voor de koper; aftrek van 10 %-bouw-btw)? Zo niet: is de 21 %-btw op renovatie voor de SL definitief niet aftrekbaar?
3. Grondslag AJD 1,4 % bij declaración de obra nueva (route B) en bij división horizontal.
4. Btw op notaris- en registerhonoraria (21 %?) en op de makelaarscommissie.
5. Welke entiteit koopt (TREE, Rocksure Capital, privé) → IS 25 %/23 %/19–21 % of IRPF 19–30 %; is de vennootschap een "entidad patrimonial" (dan geen verlaagde IS-tarieven)?

**⏸️ ACTIE VOOR JAN**
- Rendementseis vaststellen (op totale kosten, op eigen vermogen of als marge) en maximale projectduur — zonder dat blijft §6 een schets.
- 3–5 nacalculaties uit de Excel-administratie aanleveren (€/m² PEM en aanneemsom, excl. btw, met jaar) — enige bron met bewijstype 3 voor Jávea.
- Akkoord (of niet) voor aanschaf IVE-BDC online (69,99 €/jaar).
- Xàbia Gestió Tributària (965 790 500 / gestio.tributaria@ajxabia.org) vragen om de ordenanzas IBI, IIVTNU, ICIO en tasas 2026 als pdf — of zelf inloggen in de Oficina Virtual Tributaria; daarmee vervallen vier ONBEKENDS.
- Twee of drie banken vragen naar voorwaarden voor promotor-/renovatiefinanciering aan een SL (rente, LTV/LTC, looptijd).

**Vervolg voor het systeem:** parameters van dit rapport in één bestand `parameters-2026.yaml` zetten (waarde, bron, datum, bewijstype, geldig-vanaf) zodat het model per kandidaat dezelfde bronvermelding reproduceert; Euríbor maandelijks bijwerken uit BdE-tabel 19.1 (openbare pdf).

---

## 8. Bronnenregister (per aanbieder; statussen uit masterprompt §7)

| Bron | Type | Toegang | Status | Notities |
|---|---|---|---|---|
| BOE — datos abiertos API legislación consolidada | Officieel | Open API (XML), zonder sleutel | GEVERIFIEERD EN ACTIEF | Per artikel geldende tekst + wijzigingsnoten; ideaal voor jaarlijkse hercontrole. Zoekfunctie van de API niet werkend; ID's via ELI-URL's te vinden. |
| Agència Tributària Valenciana (atv.gva.es) | Officieel | HTML, open | GEVERIFIEERD EN ACTIEF | Tarieventabel modelo 600 met alle codes; FAQ; normativa-links. |
| hisenda.gva.es (legislació) | Officieel | HTML/pdf | ALLEEN HANDMATIG | Pdf-link Ley 13/1997 gaf 404; BOE-consolidatie is beter. |
| Banco de España — Boletín Estadístico hfst. 19 | Officieel | Open pdf/xlsx per tabel | GEVERIFIEERD EN ACTIEF | Maandelijks; Euríbor officieel na BOE-publicatie. |
| Ajuntament de Xàbia / Xàbia Gestió Tributària | Officieel gemeentelijk | HTML + pdf; ordenanzas achter JS-portaal | ALLEEN HANDMATIG | Afvalheffing-gids gelezen; IBI/ICIO/IIVTNU-tarieven niet bereikbaar. |
| Dirección General del Catastro — valor de referencia | Officieel | Na authenticatie (zie R04) | ALLEEN HANDMATIG | Per object nodig vóór elk bod. |
| Consejo General del Notariado (notariado.org) | Beroepsorganisatie | HTML + pdf | ALLEEN HANDMATIG | Bevestigt uniforme tarieven en 10 % korting; schaal zelf uit BOE. |
| Colegio de Registradores (registradores.org) | Beroepsorganisatie | HTML | ALLEEN HANDMATIG | Geen arancel-pagina gevonden; schaal uit BOE. |
| IVE — BDC 2026 | Officieel instituut (Generalitat) | Betaald abonnement | CONTRACT OF TOESTEMMING NODIG | 69,99 €/jaar online; 225 € installeerbaar. |
| CYPE Generador de precios | Commercieel | Gratis na registratie | TECHNISCH ONDERZOEK NODIG | Gebruiksvoorwaarden (aviso legal) nog te lezen vóór overname van prijzen. |
| Ministerio de Transportes — visados | Officieel | HTTP 403 in deze sessie | TECHNISCH ONDERZOEK NODIG | Handmatig downloaden; geeft PEM/m² per provincie. |
| CSCAE | Beroepsorganisatie | Open | ALLEEN HANDMATIG | Alleen landelijke volumes. |
| COACV / CTAA / COAATIE Alicante | Beroepsorganisaties | HTML (COAAT: certificaatfout) | TECHNISCH ONDERZOEK NODIG | Módulo/tasas de visado mogelijk op dieperliggende pagina's; telefonisch navragen. |
| habitissimo prijsgidsen | Commercieel platform | Open | ALLEEN HANDMATIG | Alleen als indicatie (1); landelijk; btw-status onduidelijk. |
| Background Properties feeds (commissielabels) | Eigen netwerk | Bestaande feed (sleutels geheim) | GEVERIFIEERD EN ACTIEF | Zie R05; 5 % vs 3–4 %. |

---

## 9. Bronnenlijst (URL · controledatum 14-09-2026 · bewijstype)

1. Ley 13/1997 CV (geconsolideerd, art. 13 bijgewerkt 02-07-2026; art. 14 31-05-2025) — https://www.boe.es/buscar/act.php?id=BOE-A-1998-8202 · API-blokken a13, a14, a14bis · 2
2. Ley 5/2025, de 30 de mayo (CV; art. 33–34 verlaging ITP/AJD per 01-06-2026) — verwijzing BOE-A-2025-11959 in de BOE-noten · 2
3. ATV — Impuesto sobre Transmisiones Patrimoniales y AJD, tariefcodes modelo 600 — https://atv.gva.es/es/itpajd · 2
4. ATV — Normativa ITPAJD — https://atv.gva.es/es/normativa-itpajd · 2
5. ATV — FAQ ITPAJD (valor de referencia; code TS0) — https://atv.gva.es/es/transmisiones-patrimoniales-y-actos-juridicos-documentados · 2
6. hisenda.gva.es — Legislació (verwijzing Ley 13/1997, RD 828/1995) — https://hisenda.gva.es/es/web/tributos/legislacio · 2
7. RDLeg 1/1993 TRLITPAJD art. 10, 11, 31 — https://www.boe.es/buscar/act.php?id=BOE-A-1993-25359 · 2
8. Ley 11/2021 (valor de referencia, art. 6.2) — https://www.boe.es/buscar/act.php?id=BOE-A-2021-11473 · 2
9. RD 828/1995 Reglamento ITPAJD art. 39 (subasta) — https://www.boe.es/buscar/act.php?id=BOE-A-1995-15071 · 2
10. Ley 37/1992 IVA art. 20.Uno.20º/22º, 20.Dos, 90, 91 — https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740 · 2
11. Ley 35/2006 IRPF art. 66 en 76 — https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764 · 2
12. Ley 27/2014 IS art. 29 en DT 44ª — https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328 · 2
13. RDLeg 5/2004 IRNR art. 25 — https://www.boe.es/buscar/act.php?id=BOE-A-2004-4527 · 2
14. RDLeg 2/2004 TRLRHL art. 72, 102, 104, 106, 107, 108 — https://www.boe.es/buscar/act.php?id=BOE-A-2004-4214 · 2
15. RD 1426/1989 Arancel de los Notarios, Anexo I Número 2 — https://www.boe.es/buscar/act.php?id=BOE-A-1989-28111 · 2
16. RD 1427/1989 Arancel de los Registradores, Número 2 — https://www.boe.es/buscar/act.php?id=BOE-A-1989-28112 · 2
17. RD 1098/2001 art. 131 (PEM, GG 13–17 %, BI 6 %) — https://www.boe.es/buscar/act.php?id=BOE-A-2001-19995 · 2
18. Ley 2/1974 Colegios Profesionales art. 14 (verbod baremos) — https://www.boe.es/buscar/act.php?id=BOE-A-1974-289 · 2
19. BOE datos abiertos API (gebruikt endpoint) — https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/{ID}/texto/bloque/{blok} · 2
20. Banco de España, Boletín Estadístico tabel 19.1 (Euríbor, IRPH, IRS, wettelijke rente) — https://www.bde.es/webbe/es/estadisticas/compartido/datos/pdf/a1901.pdf · 2
21. Banco de España tabel 19.2 — https://www.bde.es/webbe/es/estadisticas/compartido/datos/pdf/a1902.pdf · 2
22. Banco de España tabel 19.3 (TEDR NFC) — https://www.bde.es/webbe/es/estadisticas/compartido/datos/pdf/a1903.pdf · 2
23. Banco de España tabel 19.4 (TEDR woninghypotheken) — https://www.bde.es/webbe/es/estadisticas/compartido/datos/pdf/a1904.pdf · 2
24. Banco de España persbericht 01-09-2026 Euríbor augustus — https://www.bde.es/wbe/es/noticias-eventos/actualidad-banco-espana/notas-banco-espana/el-euribor-se-situa-en-el-2952-en-agosto-0838-puntos-mas-que-hace-un-ano.html (titel meldt 2,954 %) · 2
25. Banco de España — themapagina tipos de interés — https://www.bde.es/webbe/es/estadisticas/temas/tipos-interes.html · 2
26. Ajuntament de Xàbia — Ordenanzas fiscales (verwijzing) — https://www.ajxabia.com/ver/1189/ordenanzas-fiscales.html · 2
27. Ajuntament de Xàbia — Gestión tributaria — https://www.ajxabia.com/ver/10196/gestion-tributaria.html · 2
28. Xàbia Gestió Tributària — Guía completa nueva tasa de basuras 2025 — https://www.ajxabia.com/bd/archivos/archivo5252.pdf · 2
29. Xàbia Gestió Tributària — Aviso informativo tasa de residuos 2025 — https://www.ajxabia.com/bd/archivos/archivo5255.pdf · 2
30. Xàbia Gestió Tributària — site — https://xabiagt.com/ en https://xabiagt.com/preguntas-frecuentes · 2
31. Sede electrónica Xàbia — portal de transparència (ordenanzas; JS) — https://xabia.sedelectronica.es/transparency/9dc46a0e-8b13-4022-824e-000f75336158/ · 7
32. Oficina Virtual Tributaria Xàbia — https://xabia.tributoslocales.es/ · 7
33. Catastro — valor de referencia (via R04) — https://www1.sedecatastro.gob.es/Accesos/SECAccvr.aspx · 2
34. Consejo General del Notariado — "Qué cuesta" — https://www.notariado.org/portal/qu%C3%A9-cuesta · 1
35. Colegio de Registradores — https://www.registradores.org/ · 7 (niets gevonden)
36. IVE — https://www.five.es/ · https://bdc.five.es/ · https://productos.five.es/producto/base-de-datos-de-construccion · 1
37. CYPE Generador de precios — https://www.generadordeprecios.info/ · https://generadordeprecios.info/obra_nueva · https://shop.cype.com/es/aviso-legal/ · 1
38. CSCAE — Datos de visado 2025 (05-02-2026) — https://www.cscae.com/index.php/cscae/sala-de-comunicacion/9340-sector-edificacion-vigor-2025-niveles · 2
39. COACV — https://www.coacv.org/ · 7 · CTAA — https://www.ctaa.net/ · 7 · COAATIE Alicante — https://www.coaatalicante.org/ · 7 (certificaatfout)
40. Ministerio de Transportes — visados de dirección de obra — https://www.transportes.gob.es/informacion-para-el-ciudadano/informacion-estadistica/construccion/construccion-de-edificios/visados-de-direccion-de-obra · 7 (HTTP 403)
41. habitissimo — construcción casas (18-06-2026) — https://www.habitissimo.es/presupuestos/construccion-casas · 1
42. habitissimo — reforma integral (04-02-2025) — https://www.habitissimo.es/presupuestos/reforma-integral · 1
43. habitissimo — reforma cocinas (04-02-2025) — https://www.habitissimo.es/presupuestos/reforma-cocinas · 1
44. habitissimo — reforma baños (10-06-2026) — https://www.habitissimo.es/presupuestos/reforma-banos · 1
45. habitissimo — construcción piscinas (04-02-2025) — https://www.habitissimo.es/presupuestos/construccion-piscinas · 1
46. habitissimo — demoliciones (10-06-2026) — https://www.habitissimo.es/presupuestos/demoliciones · 1
47. habitissimo — muros de contención (16-09-2024) — https://www.habitissimo.es/presupuestos/muros-de-contencion · 1
48. Eigen feedconfiguratie BP (commissielabels; sleutels niet overgenomen) — `~/tree-hermes/properties-api/feeds.js` · 3
49. Interne rapporten R04 (valor de referencia), R05 (BP-commissies), R08 (veilingplatforms, 4 %) — `~/tree-es/deal-hunter/onderzoek/` · 2/3

**Aanvulling 15-09-2026 (controledatum 15-09-2026):**

50. habitissimo — overzicht prijsgidsen (vindplaats van 51–56) — https://www.habitissimo.es/presupuestos · 1
51. habitissimo — electricistas (bijgewerkt 10-06-2026; elektra volledig vanaf 1.700 €, 90 m² tot 3.000 €) — https://www.habitissimo.es/presupuestos/electricistas · 1
52. habitissimo — fontaneros (10-06-2026; fontanería volledig 2.000–3.500 €) — https://www.habitissimo.es/presupuestos/fontaneros · 1
53. habitissimo — aire acondicionado (04-02-2025; gemiddeld 2.300 €) — https://www.habitissimo.es/presupuestos/aire-acondicionado · 1
54. habitissimo — reformas viviendas (10-06-2026; 550 €/m², deelposten) — https://www.habitissimo.es/presupuestos/reformas-viviendas · 1 (tegenstrijdig met 42 → 7 voor één gemiddelde)
55. habitissimo — pintores (18-06-2026; 14 €/m²) en cambiar suelo (10-06-2026; 40 €/m²) — https://www.habitissimo.es/presupuestos/pintores · https://www.habitissimo.es/presupuestos/cambiar-suelo · 1
56. habitissimo — ventanas PVC (23-10-2024; 350 €/stuk) — https://www.habitissimo.es/presupuestos/ventanas-pvc · 1
57. Eigen hercontrole rekenfunctie §6.4 en mapinhoud (geen R12) — lokaal, `/usr/bin/python3` · 3

**Geblokkeerd of mislukt in deze stroom:** WebSearch-budget op (0 zoekopdrachten mogelijk); atv.gva.es/es/tributos-impuestos-itpajd (404); hisenda.gva.es pdf Ley 13/1997 (404); transportes.gob.es visados (403); coaatalicante.org (TLS-certificaatfout, niet omzeild); ctaa.net/visado/ (404); catastro.hacienda.gob.es/esp/estadisticas.asp (404); Xàbia transparantieportaal (JS-only, ordenanzas onbereikbaar); xabia.tributoslocales.es (JS-app); BOE-zoekpagina (ongeldige parameters) en BOE-API-zoekfunctie (500); BOE-API blok "dt-44" bestaat niet (DT 44ª zit in blok dt-6); Read van meerpagina-pdf met paginaselectie (pdftoppm ontbreekt — volledige lezing werkte wel).
**15-09-2026:** WebSearch niet gebruikt (sessiebudget eerder op); aanvulling uitsluitend via WebFetch op habitissimo-pagina's, alle zeven bereikbaar. Geen van die pagina's vermeldt of de bedragen inclusief of exclusief btw zijn.

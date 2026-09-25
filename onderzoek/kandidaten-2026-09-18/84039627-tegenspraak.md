# 84039627 — tegenspraak op ons eigen rekenmodel

**Perceel El Rafalet, Jávea/Xàbia · vraagprijs € 234.000 · 18-09-2026**

Opdracht: probeer het basisscenario van ons systeem onderuit te halen. Dat is gelukt, op twee
onafhankelijke gronden. Eén ervan is dodelijk.

Bronnen: officiële Idealista-assistent (`property_detail` en `search_properties`, 18-09-2026),
ons eigen `kader/investeringskader.md` en `onderzoek/N01-bouwregels-xabia.md`. Niet gescrapet,
niet ingelogd. Geen persoonsgegevens overgenomen.

Bewijstype tussen haakjes: (1) door aanbieder vermeld · (2) officiële bron · (3) door ons
vastgesteld · (5) berekening op benoemde aannames · (7) onbekend of tegenstrijdig.

---

## Wat ons systeem beweert

| | |
|---|---|
| Scenario | Nieuwbouw villa 341 m² (0,20 × perceel 1.707 m²), 24 maanden |
| Verkoopopbrengst | € 1.949.497 bij € 5.717 per m² |
| Resultaat bij vraagprijs | € 635.907 |
| Maximale koopprijs | € 525.000 |

Alle vier de regels houden geen stand.

---

## Weerlegging 1 — je mag hier geen woning bouwen (dodelijk)

De advertentie zegt onder *Situación urbanística* letterlijk: **"Calificado para terciario
comercial"** (1). En in de beschrijving: *"Idela para supermercados, restaurantes o empresas
servicios que presten servicios a las urbanizaciones cercanas."* Supermarkten, restaurants,
dienstverleners. Wonen wordt nergens genoemd — niet in de kenmerken, niet in de tekst.

Het hele scenario "nieuwbouw villa 341 m²" veronderstelt een woonbestemming. Die is er volgens
de verkopende partij zelf niet. Ons eigen onderzoek naar de bouwregels van Xàbia
(`onderzoek/N01-bouwregels-xabia.md`) kent *Terciario* en *Comercial concentrado* als aparte
zoneklassen, los van de woonzones, met parameters die daar als ONBEKEND staan (3).

Dit is geen detail dat je met een correctie repareert. Zonder woonbestemming is er geen villa,
geen 341 m², geen verkoopopbrengst van € 1.949.497 en geen resultaat van € 635.907. De hele
rij valt weg.

**Belangrijk voor de bewijslast:** ik kan niet uit een officiële bron aantonen dát wonen
verboden is — daarvoor is een *informe urbanístico* op de kadastrale referentie nodig, en die
hebben we niet (7). Maar de richting van het bewijs is nu omgekeerd. Ons systeem nam
woonbestemming aan zonder enige onderbouwing; de advertentie spreekt die aanname expliciet
tegen. Wie het villascenario wil handhaven, moet nu aantonen dat wonen mág.

---

## Weerlegging 2 — € 5.717 per m² is te hoog, ook als je het perceel residentieel maakt

Stel dat weerlegging 1 wegvalt en er mag tóch een villa komen. Dan nog klopt de verkoopprijs niet.

Ik heb vandaag met de officiële assistent gezocht naar **nieuwe en gerenoveerde woningen van
300–400 m²** in dezelfde wijk en de buurwijk — dus op vergelijkbare omvang, want dát is waar het
misgaat. El Rafalet: 5 objecten. Pinomar–Pinosol: 13 objecten.

De drie gevraagde voorbeelden, alle drie nieuw of net gerenoveerd, alle drie in de maat:

| # | Object | Wijk | Wat het is | m² | Vraagprijs | €/m² |
|---|---|---|---|---|---|---|
| 1 | [111918606](https://www.idealista.com/obra-nueva/111918606/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail) | **El Rafalet** | obra nueva, 3 lagen, zwembad, perceel 1.085 m² | 329 | € 1.088.000 | **3.307** |
| 2 | [111656885](https://www.idealista.com/inmueble/111656885/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail) | Pinosol | nieuwbouw, oplevering maart 2027 | 333 | € 1.288.000 | **3.868** |
| 3 | [112329948](https://www.idealista.com/inmueble/112329948/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail) | Pinosol | "magníficamente reformada", zeezicht, 3 lagen | 370 | € 1.685.000 | **4.554** |

Alle drie bewijstype (1), opgehaald 18-09-2026.

De volledige reeks in die maatklasse, tien unieke objecten over beide wijken (3):

1.912 · 2.279 · 2.676 · 3.307 · 3.461 · 3.827 · 3.868 · 4.554 · 4.600 · 7.650 €/m²

**Mediaan € 3.644 per m².** Eén van de tien staat boven € 5.717: een volledig gemeubileerde
luxevilla van 300 m² op 2.135 m² grond, sleutelklaar met inventaris (112031038). Dat is geen
referentie voor een ontwikkelproject.

Waar komt onze € 5.717 dan vandaan? Uit `H01-comparables-rafalet_pinosol.md`: het is de mediaan
van de reeks `villa_new`, n = 9, spreiding 3.307–9.750, over drie wijken samen. Dat rapport
waarschuwt er zelf al voor — "n = 9", "hangt aan Pinosol", "voor El Rafalet is nieuwbouw feitelijk
niet in de tool aanwezig" (n = 1). Het getal € 5.717 is bovendien afkomstig van één advertentie
(106823897, 223 m²) die volgens datzelfde rapport **meer dan een jaar niet is bijgewerkt** (3).

En de kern van de fout: die reeks bevat vooral kleine objecten van 177–223 m². Grotere huizen
brengen per m² minder op. Op 300–400 m² — precies de maat van ons scenario — komt niets in de
buurt van 5.717. Wij hebben een €/m² van kleine villa's op een grote villa geplakt.

Wat dat doet met de opbrengst (5):

| Aanname | 341 m² × €/m² | Verschil met ons model |
|---|---|---|
| Ons systeem: 5.717 | € 1.949.497 | — |
| Nieuwbouw Pinosol: 3.868 | € 1.318.988 | **− € 630.509** |
| Nieuwbouw El Rafalet: 3.307 | € 1.127.687 | **− € 821.810** |

Het geclaimde resultaat van € 635.907 verdampt bij beide. Bij de El Rafalet-referentie — de
enige nieuwbouwreferentie in de eigen wijk — gaat het project in de min voordat je aan
financiering, verkoopkosten of winst toekomt.

---

## 1. Welke vierkante meters zitten er in de opgave

Er staat geen gebouw op het perceel, dus *construida* tegenover *útil* speelt hier niet. Idealista
vult `size` én `usableArea` allebei met 1.705 — dat is grond, geen opstal (3). Terras, kelder en
garage komen niet voor.

Maar de opgave is intern tegenstrijdig:

| Veld in de advertentie | Waarde |
|---|---|
| Superficie total del terreno | 1.705 m² (1) |
| **Superficie mínima en venta** | **2.220 m²** (1) |
| Superficie edificable | 400 m² (1) |
| Bouwlagen | 2 plantas edificables (1) |

De minimale verkoopoppervlakte is **515 m² groter dan het hele perceel**. Dat kan niet allebei
kloppen (7). Ofwel het perceel is in werkelijkheid 2.220 m², ofwel dit deel wordt verkocht uit een
groter geheel — en dan ligt de kavelgrens nog niet vast. Uit de advertentie is niet te bepalen
welke van de twee.

Drie dingen die hieruit volgen:

- **Ons systeem rekent met 1.707 m². Dat getal staat nergens in de advertentie.** Vandaag staat er
  1.705. Klein verschil, maar het betekent dat onze pijplijn niet op het actuele veld rekent (3).
- **Het bouwrecht in de advertentie is 400 m², niet 341 m².** 400 ÷ 1.705 = 0,235 m² per m²
  perceel, hoger dan de 0,20 die ons model als vuistregel gebruikt. Dat lijkt gunstig, maar het is
  een ánder bouwrecht: 400 m² commercieel, geen 341 m² woning.
- **Of die 400 m² het totaal is over beide lagen of de oppervlakte per laag, staat er niet** (7).
  Dat scheelt een factor twee.

Prijs per meter, op de genoemde getallen (5): € 234.000 ÷ 1.705 = **€ 137 per m² grond** (gelijk aan
Idealista's eigen `priceByArea`), of € 105 als 2.220 klopt. Per m² bouwrecht: € 234.000 ÷ 400 =
**€ 585**.

---

## 2. Planklasse en vergunning

Wat de advertentie zegt (alles bewijstype 1):

- **Terreno urbano (solar)** — stedelijke grond, bouwrijp. Het veld `subTypology` staat op `urban`,
  consistent (3). Geen *urbanizable*, geen *rústico*. Dat is het goede nieuws.
- **Calificado para terciario comercial** — zie weerlegging 1.
- **2 plantas edificables**, toegang via stadsweg, water, elektriciteit en straatverlichting aanwezig.
- Uit de beschrijving: *"El solar ya ha sido totalmente gestionado urbanísticamente, habiéndose
  realizado las cesiones de suelo, así como todas las obras de urbanización ya aprobadas y
  recepcionadas por el ayuntamiento."* De grondafdracht is gedaan en de urbanisatiewerken zijn door
  de gemeente **opgeleverd en overgenomen**.

**Over Jans harde uitsluiting.** Een **aval bancario** wordt nergens genoemd, en een nog lopende
urbanisatie evenmin — integendeel, de verkoper claimt dat de urbanisatie is opgeleverd. Op de tekst
afgaand is dit dus géén uitsluiting. Maar het is een bewering in een verkooptekst, geen document (1).
De *recepción de obras de urbanización* is een gemeentelijk besluit en dus opvraagbaar; tot dat op
tafel ligt, blijft de uitsluitingsgrond formeel open (7).

**Vergunning: niets.** Geen licencia de obra, geen vergunningnummer, geen goedgekeurd project, geen
architect (7). *"Puede ser edificada de inmediato"* gaat over de grond, niet over papieren.

---

## 3. Is € 1.000 per m² renovatie genoeg?

**Nee — de vraag is niet van toepassing, en dat is op zichzelf een fout in het model.**

Er ís geen pand. Er valt niets te renoveren. Het toepasselijke kengetal uit
`kader/investeringskader.md` is Jans eigen nieuwbouwnorm: **€ 2.000 per m², exclusief btw, en
uitsluitend bouwkosten — architect, vergunning, zwembad en buitenruimte komen daar bovenop.** Dat
is dus twee keer het renovatiegetal, plus posten.

Een ruwe toets op die norm, met de genoemde aannames (5) — geen van deze percentages is
geverifieerd, ze staan er om de orde van grootte te laten zien:

- 341 m² × € 2.000 = € 682.000 kale bouwkosten
- 10 % btw op nieuwbouw ≈ € 68.200
- architect, vergunning en technische begeleiding, stel 10 % ≈ € 68.200 **[te verifiëren]**
- zwembad en buitenruimte, stel € 80.000–120.000 **[te verifiëren]**
- grond € 234.000, plus overdrachtsbelasting: levering van bouwgrond door een ondernemer is in de
  regel 21 % btw in plaats van ITP ≈ € 49.140 **[te verifiëren door een fiscalist]**

Samen ruwweg **€ 1,18–1,22 miljoen**, nog vóór financiering over 24 maanden, verkoopkosten en winst.
Zet daar de El Rafalet-nieuwbouwreferentie tegenover — € 1.127.687 — en het project staat in de min.
Zelfs bij de Pinosol-referentie van € 1.318.988 blijft er geen € 635.907 over, maar hooguit een
marge van een ton die door rentelasten en verkoopkosten wordt opgegeten.

En voor de bestemming die er wél op zit — een supermarkt- of restaurantcasco — geldt een heel ander
kostenprofiel, dat wij niet hebben: **ONBEKEND** (7).

---

## 4. Het punt dat dit plan het snelst onderuit haalt

**Eén zin in de advertentie: "Calificado para terciario comercial".**

Niet de prijs per m², niet de bouwkosten, niet de oppervlakte-verwarring. Die zijn allemaal te
corrigeren. Een commerciële bestemming is dat niet: die maakt het hele scenario onmogelijk in plaats
van onrendabel. En het kost nul euro en één telefoontje om vast te stellen of het klopt.

Daarachter, op afstand, staat de tweede: **wij passen een €/m² van kleine villa's toe op grote
villa's.** Dat is geen fout in dit dossier alleen — het zit in de methode en raakt elk object waar
het scenario boven de 300 m² uitkomt. Dat is het waard om apart na te lopen.

---

## Wat er wél klopt

Om eerlijk te blijven tegenover het systeem:

- De rekenkunde is zuiver. 341 × 5.717 = 1.949.497 klopt tot op de euro. De invoer deugt niet,
  de som wel.
- *Terreno urbano (solar)* is de gunstigste planklasse die er is. Geen urbanizable, geen rústico.
- Geen aval bancario en een opgeleverde urbanisatie — als dat klopt, koop je hier geen wachttijd
  en geen urbanisatiebijdrage. Dat is precies wat de meeste percelen in dit dossier wél meebrengen.
- € 585 per m² bouwrecht is in absolute zin laag. Alleen: zonder één commerciële referentie in
  Jávea is dat een getal zonder betekenis (3).

---

## Oordeel: **valt af**

Niet omdat het perceel slecht is, maar omdat het object dat wij hebben doorgerekend niet bestaat.
Het dossier `rapporten/dossiers/84039627.html` staat nu op "kopen, mits het basisscenario
standhoudt". Dat basisscenario houdt geen stand.

Als route A (kopen, villa bouwen, verkopen) is dit object van de lijst. Als **route B of C** —
zelf ontwikkelen en verhuren, of de bouw doen voor een partij die er een supermarkt of restaurant
wil — is het niet beoordeeld en kán het interessant zijn. Daar hebben wij geen enkele referentie
voor.

---

## Vervolgstappen

1. Dossier `rapporten/dossiers/84039627.html` op non-actief zetten of van een waarschuwing voorzien.
2. Methodefout herstellen: de €/m²-reeks stratificeren naar omvang. Nu wordt een mediaan over
   177–420 m² toegepast op scenario's van 300+ m². Dit raakt meer objecten dan alleen dit perceel.
3. Pijplijn laat 1.707 m² zien waar de advertentie 1.705 m² zegt — uitzoeken waar dat getal vandaan
   komt.
4. Kadastrale referentie ophalen via Catastro op de benaderende coördinaten (38,764 / 0,151;
   `showAddress` staat op `false`), en daarmee vaststellen of het perceel 1.705 of 2.220 m² is.

⏸️ **ACTIE VOOR JAN**

**De eerste vraag aan de verkoper, vóór alles:** *"Mag er op dit perceel gewoond worden, of is de
bestemming uitsluitend terciario comercial? Graag de informe urbanístico en de kadastrale
referentie."* Eén vraag, en het antwoord beslist of hier verder tijd in gaat.

Twee vragen aan jou:

- **Wil je commercieel vastgoed überhaupt in het zoekprofiel?** Het investeringskader gaat over
  woningen. Zeg je nee, dan gaat dit object van de lijst en hoeft er niets meer te gebeuren.
- **Zeg je ja,** dan hebben we een verkoop- of huurreferentie voor terciario in Jávea nodig. Die
  hebben we niet en die haal ik niet uit een portaal. Ken je een partij die daar cijfers over heeft?

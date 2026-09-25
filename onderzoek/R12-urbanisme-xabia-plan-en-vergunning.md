# R12 — Urbanisme Xàbia: geldend plan, nieuw PGE, zones en parameters, vergunningsroute en leges

> **NA TEGENSPRAAK (15-09-2026).** Dit rapport is door een tweede agent gecontroleerd; zie `R12-urbanisme-xabia-plan-en-vergunning.verificatie.md`. Betrouwbaarheid volgens die controle: middel.
> Weerlegd en in de eindstukken gecorrigeerd: R12-09; R12-10. Gebruik voor die punten de gecorrigeerde tekst in het verificatiebestand, niet de tekst hieronder.


**Onderzoeksstroom:** R12 (fase A, TREE Deal Hunter) · **Controledatum:** 15-09-2026 · **Masterprompt:** §5, §6, §7, §15, §16, §17
**Status:** onderzoeksrapport, geen juridisch advies. Elke bouwconclusie per perceel vereist bevestiging door gemeente en/of lokale architect (bewijstype 6).

## Samenvatting (10 regels)

1. **Geldend plan = PGOU van 1990/1991**: goedgekeurd door de Comisión Territorial de Urbanismo op 31-01-1990 (BOP 26-02-1990), met de restgebieden (La Granadella, SUP residencial intensivo) bij resolución van de conseller van 08-03-1991 (BOP 03-06-1991). Bewijstype 2.
2. **Het nieuwe Plan General Estructural (PGE) is niet in werking.** Pleno keurde de "propuesta definitiva" goed op 30-04-2019; definitieve goedkeuring door de Conselleria is nergens gevonden. In feb. 2025 schreef de Dirección General de Urbanismo volgens de pers dat het PGE als niet-goedgekeurd plan "carente de validez y eficacia" is. Toekomstig plan ≠ bouwrecht.
3. De **gedeeltelijke schorsing van het PGOU plus de Normas Urbanísticas Transitorias de Urgencia (NUT)** (casco, estética/depuración in zona E, nieuwe red primaria) liep volgens de DOGV-teksten **uiterlijk tot ca. 15-03-2025**. Of de NUT daarna nog worden toegepast is een open interpretatievraag (bewijstype 7).
4. De **ordenanzas van het PGOU (240 blz. scan)** zijn opgehaald uit het officiële Registro Autonómico (GVA), ge-OCR'd en op sleutelpagina's visueel gecontroleerd. De zone van een perceel volgt uit plano B.1 (letters A–H; residencial extensivo zonder letter = E2) en de parcela mínima uit plano B.2 + tabel art. 10.5.1.
5. **Zona E (villa-urbanisaties):** parcela mínima per gebied 500–1.500 m² (bv. Tosalet 1.000; Montgó-Ermita, -Castellans, -Barranqueres 1.500), edificabilidad **0,142 m²t/m² bruto = 0,20 m²t/m² neto** (sommige gebieden 0,198/0,28), ocupación 20/30/50 % per grado, 1–2 plantas, 5 m tot grenzen (grado I/II), zwembad 2 m van grens. Géén uniform percentage voor heel Jávea.
6. **Veel urbanisaties vallen niet onder de PGOU-zonetabel maar onder een eigen Plan Parcial/homologación** (bv. het K07-perceel Garroferal ligt volgens de GVA-laag in "PLAN PARCIAL ERMITA II", suelo urbanizable). Die documenten staan niet in het register → per perceel opvragen.
7. **Suelo no urbanizable:** het PGOU staat op genérico-grond een woning toe vanaf 5.000 m² (Plà 10.000 m²), maar de regionale wet (TRLOTUP art. 211.1.b) eist nu **minimaal 1 ha per woning en max. 2 % bebouwing**; protección ecológico-paisajística: geen nieuwbouw.
8. **Vergunningen (TRLOTUP, geconsolideerd 02-07-2026):** nieuwbouw = licencia (wettelijke termijn 2 maanden, stilzwijgen = weigering); verbouw en 1e/2e ocupación = declaración responsable; cédula de garantía urbanística binnen 1 maand, 1 jaar geldig; alternatief via ECUV-certificaat.
9. **Leges:** ICIO Xàbia **4,00 %** (2025 en 2026, Ministerio de Hacienda) = wettelijk maximum; tasa por licencia urbanística **ONBEKEND** (ordenanzas alleen via JavaScript-portaal). Praktijkdoorlooptijd: "hasta un año" volgens gemeentelijke bronnen in de pers (nov. 2023) [te verifiëren].
10. **Automatiseerbaar:** de open GVA/ICV-WFS (CC BY 4.0) geeft per coördinaat klasse, zone en planinstrument — getest op 7 punten in Jávea. Juridisch alleen "carácter informativo" en niet volledig actueel (geannuleerde homologación Portitxol staat er nog in).

---

## 0. Werkwijze, afbakening en beperkingen

| Onderdeel | Toelichting |
|---|---|
| Bronnen | DOGV-pdf's (dogv.gva.es), BOP Alicante (via het GVA-register), het Registro Autonómico de Instrumentos de Planeamiento (open directory van de GVA), BOE-geconsolideerde TRLOTUP, Ministerio de Hacienda (SGFAL), ajxabia.com, ICV/GVA-WFS, persberichten met datum (xabiaaldia, lamarina.eldiario, javea.com, Alicante Plaza). |
| Scans | De PGOU-documenten in het register zijn scans zonder tekstlaag. Tekst is lokaal gewonnen met de ingebouwde macOS-frameworks PDFKit + Vision (Swift, niets geïnstalleerd). Sleutelpagina's (tabellen parcela mínima, zona E, casco, art. 8.1.15, 4.1.9, SNU grado I/II) zijn als afbeelding gerenderd en visueel gelezen (§15: "lees de oorspronkelijke pagina"). Waar alleen OCR is gebruikt staat **[OCR]**. |
| Volledigheid | Het register bevat 33 instrumenten onder "Plan General" en 24 onder "Planeamiento diferido". Xàbia kent modificaciones tot ten minste nº 71 (register 03082-1102); het register is dus **geen volledige lijst** en bevat ook niet alle planes parciales (bv. Ermita II ontbreekt). |
| Lokale data | Alleen lezen: `GET http://127.0.0.1:3100/api/properties?town=Javea&limit=100` (56 objecten, 24 × "Land") en R11/R15 als voorbeeldpercelen. Geen sleutels of feed-URL's overgenomen. |
| Niet gedaan | Geen contact met gemeente; geen omzeiling van het JavaScript-portaal van de sede electrónica; geen bulkdownload van plankaarten. |
| Zoekbudget | WebSearch werkte in deze ronde weer (ca. 30 zoekopdrachten). |

---

## 1. Welk plan geldt vandaag? (opdracht a)

### 1.1 Tijdlijn met bron en bewijstype

| Datum | Gebeurtenis | Bron | Type |
|---|---|---|---|
| 31-01-1990 | CTU Alicante keurt de "Revisión-Adaptación del Plan General" definitief goed (behalve La Granadella en SUP residencial intensivo); BOP 26-02-1990 | Acuerdo Consell 05-03-2021 (DOGV 15-03-2021) en NUT-acuerdo (DOGV 9177, 20-09-2021): "se aprobó definitivamente por la entonces Comisión Provincial de Urbanismo de Alicante, en fecha 31 de enero de 1990 (BOP 26.02.1990)" | 2 |
| 29-01-1991 / 08-03-1991 | CTU adviseert gunstig; conseller keurt La Granadella (→ SNU protección ecológico-paisajística) en SUP residencial intensivo definitief goed; publicatie BOP nº 125 van 03-06-1991; volgens het Consell-acuerdo 2021 ook DOGV nº 1548 (22-05-1991) en normas in BOP 06-06-1991 | Registerdocs 03082-1000 1_CTU.pdf en 2_BOP.pdf (OCR); DOGV 15-03-2021 | 2 |
| 1992–2019 | Minstens 33 modificaciones/homologaciones in het GVA-register (zie 1.3) | Registro Autonómico | 2 |
| 26-01-2007 | Decreto 11/2007: gedeeltelijke schorsing van het PG (licencias de parcelación, edificación y demolición) in afgebakende gebieden tot de información pública van de revisie (DOGV 5438, 29-01-2007) | Registerdoc 03082-1000 3_DOGV.pdf (OCR) | 2 (historisch) |
| 24-11-2011 (resp. 08-11-2011) | Documento de referencia (milieubeoordeling) van de planrevisie | DOGV 2021/3029 (07-04-2021) en DOGV 15-03-2021 (twee verschillende data genoemd) | 2 / 7 (datumconflict) |
| 01-06-2017 | Pleno: versión preliminar PGE in participación pública (DOCV 8057, 07-06-2017), plus schorsing van licenties waar oude en nieuwe ordening onverenigbaar zijn en schorsing PAI's ADN-4, MES-2 en MES-3 | ajxabia.com/ver/6807 (01-06-2017); DOGV 15-03-2021 | 2 |
| 24-01 t/m 21-02-2019 | Nieuwe exposición pública van de versión preliminar (extra 201.220 m² beschermd) | ajxabia.com/ver/7741 (24-01-2019) | 2 |
| 30-04-2019 | Pleno keurt "propuesta definitiva de Plan General Estructural" goed voor validatie door de Conselleria; ca. 8 miljoen m² minder suelo urbanizable, +40 % dotacional | ajxabia.com/ver/7823 (30-04-2019) | 2 |
| 07-06-2019 | Licentieschorsing van 2017 verloopt | DOGV 15-03-2021 | 2 |
| 18-12-2019 | Consell vraagt vijf extra sectorale rapporten (CHJ, movilidad, planificación, PATIVEL, PATRICOVA) | xabiaaldia 18-12-2019 | 1 (pers) |
| 05-03-2021 (DOGV 15-03-2021) | Consell: **gedeeltelijke schorsing van het PGOU** (red primaria nieuw, zona A casco deels, zona E art. 10.5.2 en 10.5.3). "La suspensión se mantendrá hasta la entrada en vigor del Plan general de Xàbia. En todo caso, la suspensión finalizará transcurridos cuatro años desde la publicación de este acuerdo." | DOGV 9041, 15-03-2021, blz. 750–753 | 2 |
| 10-09-2021 (DOGV 9177, 20-09-2021) | Consell keurt de **NUT** goed: 4 normas transitorias; in werking daags na publicatie, "hasta la aprobación del Plan General Estructural", maar schorsing eindigt in elk geval na vier jaar vanaf DOGV 15-03-2021 | DOGV 9177, 20-09-2021, blz. 155–160 | 2 |
| 30-04-2019 → 2025 | PGE niet definitief goedgekeurd | lamarina.eldiario 17-02-2025; xabiaaldia 18-02-2025 | 1 (pers, citeert brief Generalitat) |
| feb. 2025 | Brief Dirección General de Urbanismo: licenties moeten volgens PGOU 1990/1991; weigeren op basis van het PGE is "improcedente" | idem | 1 (pers) — brief zelf niet gezien |
| feb. 2025 | Uitspraak TSJCV erkent dat de gemeente elke aanvraag mag toetsen aan geldende normen (datum/nummer niet gevonden) | en.javea.com 19-02-2025 | 1 / 7 |
| ca. 15/16-03-2025 | **Einde vierjaarstermijn schorsing PGOU** (afgeleid uit DOGV-tekst) | DOGV 15-03-2021 + DOGV 20-09-2021 | 5 (datumberekening) |
| 28-05-2026 | Pleno: aanvankelijke goedkeuring **modificación nº 41 PGOU** (viviendas turísticas, plafond per wijk) + schorsing nieuwe licenties voor meergezins-VUT (1 jaar of tot definitieve goedkeuring) | en.javea.com 06-06-2026; lamarina.eldiario 29-05-2026 | 1 (pers) [te verifiëren in BOP] |
| 25-08-2026 | GVA-planningslaag (Clasificación/Zonificación) bijgewerkt; toont voor Xàbia uitsluitend PGOU-1990-instrumenten, geen PGE | datos.gob.es-dataset + eigen WFS-test | 2 / 3 |
| 15-09-2026 | **Geen bron gevonden** die definitieve goedkeuring of publicatie van het PGE meldt; het register heeft geen PGE-map | Registro Autonómico (eigen crawl); WFS | 3 ("niet gevonden" ≠ "bestaat niet") |

### 1.2 Conclusie planstatus

| Document | Status op 15-09-2026 | Toepassen als bouwrecht? |
|---|---|---|
| PGOU 1990/1991 + in het register opgenomen modificaciones | Vastgesteld, gepubliceerd, **in werking** | Ja |
| Planes parciales, PRI's, homologaciones, estudios de detalle ("planeamiento diferido") | In werking per instrument; de Portitxol-homologación is **vernietigd** (TSJCV, uitspraak 26-04-2012, recurso 201/09; register: "Anulado") | Ja, per instrument; Portitxol niet |
| NUT (DOGV 20-09-2021) | Formeel "hasta la aprobación del PGE", maar gekoppeld aan een schorsing die uiterlijk ca. 15-03-2025 eindigde; de Abogacía de la Generalitat noemde ze normen "para el ámbito de la suspensión hasta que se produzca su levantamiento" (DOGV 15-03-2021) | **Onzeker** (bewijstype 7): vóór aankoop schriftelijk laten bevestigen |
| PGE (propuesta definitiva pleno 30-04-2019) | In procedure bij de Conselleria; niet goedgekeurd, niet gepubliceerd, niet in werking | **Nee.** Wel risico-informatie (declassificatie, nieuwe wegen) |
| Mod. nº 41 (VUT) | Aanvankelijk goedgekeurd 28-05-2026 (pers) | Nee als bouwrecht; de gekoppelde licentieschorsing wel, zodra gepubliceerd [te verifiëren] |

Wettelijk kader: de Conselleria keurt plannen met ordenación estructural definitief goed (TRLOTUP art. 44.3.c); de Consell kan plannen schorsen en NUT vaststellen (art. 44.7); na twee jaar licentieschorsing volgt vijf jaar verbod op herhaling en daarna alleen nog schorsing plus NUT (art. 69.3). Bron: BOE, geconsolideerde tekst DOGV-r-2021-90283, laatste update 02-07-2026. Bewijstype 2.

### 1.3 Modificaciones, homologaciones en afgeleide plannen in het GVA-register

Datum = zitting CTU of pleno volgens de OCR van het goedkeuringsdocument (**[OCR]**, eerste datum in het document; ter controle).

| Registernr. | Instrument | Onderwerp (uit goedkeuringsdoc of mapnaam) | Goedkeuring |
|---|---|---|---|
| 03082-1005 | Mod. nº I | "subsanación de errores materiales y alteraciones puntuales"; bevat vervangende bladen van de ordenanzas ("Ordenación MODIFICADA 114-A/B/C", o.a. art. 8.1.27, zona A casco, zona E) | CTU 01-10-1993; conseller 14-02-1994 (DOGV 2227, 15-03-1994) |
| 03082-1027 | Mod. nº II | subsanación de errores y alteraciones | CTU 28-05-1993 / 01-10-1993 |
| 03082-1003 | Mod. nº 2 | UA Mar Azul | CTU 22-06-1992 |
| 03082-1009 | Mod. nº III | aansluiting Ronda Sur | CTU 09-06-1994 |
| 03082-1010 | Mod. nº IV | viario UE Montgó-6 en Montgó-10 | CTU 10-02-1995 |
| 03082-1004 | Mod. nº V | ordenanza edificación abierta, Montañar-I (vermoedelijk de vervangende bladen zona C in de ordenanzas-pdf, gestempeld "MOD. P. Nº 5", pleno 1994 [OCR; nummering te verifiëren]) | CTU 07-04-1995 |
| 03082-1006 | Mod. nº 5 | UA-ACM-26 | CTU 08-10-1993 |
| 03082-1007 | Mod. nº 6 | UA CVM-2 | CTU 19-11-1993 |
| 03082-1008 | Mod. nº 7 | UA Lluca-Rafalets 5 en 12 | CTU 19-11-1993 |
| 03082-1018 | Mod. nº 8 | UA Mar Azul nº 6 | CTU 19-11-1993 |
| 03082-1014 | Mod. nº 9 | ordenanza C1 in UA | CTU 20-12-1996 |
| 03082-1011 | Mod. nº 10 | vial UA CSA-3 | CTU 08-10-1996 |
| 03082-1012 | Mod. nº 11 | vial UA-ACM-22 | CTU 08-03-1996 |
| 03082-1028 | Mod. nº 13 | gebruikswijziging perceel (deportivo/socio-cultural) | CTU 22-07-1996 |
| 03082-1015 | Mod. nº 15 | viario in UA | CTU 16-11-1998 |
| 03082-1013 | Mod. nº 16 | schrappen vial (Partida Castellans) | CTU 30-01-1998 |
| 03082-1024 | Mod. nº 21 | uitbreiding dotacional educativo-cultural | CTU 29-07-2009 |
| 03082-1026 | Mod. nº 25 | grens suelo urbano extensivo / SUNP | [OCR: datum niet leesbaar] |
| 03082-1016 | Mod. nº 27 | uso hotelero en zona E; nieuwe tekst art. 10.5.4 en 10.5.7 | conseller 01-04-2003; correctie 21-10-2003 (DOGV 4665, 08-01-2004) |
| 03082-1017 | Mod. nº 38 | SUE Adsubia-Rebaldí | CTU 04-02-2003 |
| 03082-1019 | Mod. nº 42 | UA MC-11-A | CTU 03-02-2005 |
| 03082-1020 | Mod. nº XII ("Art. 106") | zona F terciario (paseo marítimo): 1 planta, 3,50 m | CTU 11-04-2006 (BOP 19-05-2006) |
| 03082-1021 | Mod. nº XIV | La Granadella | CTU 30-09-2003 |
| 03082-1023 | Mod. nº XV | drie dotacionele blokken in casco | CTU 03-02-2005 |
| 03082-1022 | Mod. nº XVI | art. 3.x (planes especiales, o.a. Parque del Montgó) | CTU 15-03-2004 |
| 03082-1002 | Mod. nº XVII | uitbreiding Catálogo de Bienes y Espacios Protegidos | CTU 27-03-2008 |
| 03082-1025 | Mod. nº 46 | herbegrenzing sector Saladar 2 | CTU 25-01-2010 |
| 03082-1029 | Mod. SUNP Cansalades-Lluca | sector SUNP | CTU 27-09-1991 |
| 03082-1100 | Mod. nº XXXV | nieuw wegtracé c/ Menkar, SUE Montgó-Ermita | Pleno 21-12-2015 (BOP nº 9, 15-01-2016) |
| **03082-1101** | **Mod. nº XXV** | **art. 8.1.2 parcela, 8.1.3 parcela mínima, 10.5.1.1 parcela edificable zona E** (8.1.6 solar geschorst) | **Pleno 27-10-2016 (BOP nº 240, 16-12-2016)** |
| 03082-1102 | Mod. nº 71 | UE Adsubia-Rebaldí-5 | Pleno 30-04-2019; ingeschreven 12-11-2021 |
| 03082-1001 | Homologación modificativa Portitxol | — | CTU 03-05-2006; **vernietigd** (TSJCV 26-04-2012) |

Planeamiento diferido in het register (mapnamen): PP El Cabo (1990), PP turístico La Marquetona, PP Pou del Moro-1, PP Pla-1 (+ mod.), PP hotel-apart Capsades-9, PP SUP Rafals, mod. Plan Especial La Fontana, homologación + PP Cansalades-Umbría, homologación + PP Aduanes-1, homologación + PRI UD/UE Arenal, homologación + PRI UE ACM, homologación + PRI Lluca-San Rafael, homologación + PRI UE ML-4, homologación PRI UA Adsubia-Cap Martí-38, homologación + PP Saladar-2, PP Cansalades-10, ED Aduana Norte-3B, mod. PP La Guardia-1, mod. ED Roig Roquetes-1, twee ED's in PP Cansalades-10, ED SUE Adsubia-Cap Martí, ED Av. Mediterráneo parc. 212–216. Bewijstype 2.

In de GVA-planningslaag staan voor Xàbia daarnaast o.a. "PLAN PARCIAL ERMITA II" (exp. 19940463) en "PLAN PARCIAL LA GUARDIA-3" (exp. 19981338), **zonder** documenten in het register. Ook staat er een deelgebied "PLAN GENERAL (AFECTADO POR SENTENCIA DEL TSJCV DE 15/NOV./2000)" in (bewijstype 3, eigen WFS-telling; inhoud van die uitspraak niet onderzocht).

### 1.4 Wat de NUT (2021) regelden: relevant voor oude vergunningen en als "voorproefje" van het PGE

Bron: DOGV 9177 (20-09-2021), annex I. Bewijstype 2.

| Norma | Gebied | Inhoud (samengevat) |
|---|---|---|
| NT 1 | Bestaande bebouwing in de **nieuwe Xarxa Primària Estructural** van het PGE (gele zones op de kaart "Àmbits de suspensió de llicències", juli 2019) | Regime "fuera de ordenación" (art. 192.3 Ley 5/2014) |
| NT 2 | Núcleo Histórico Tradicional (NHT), zona A casco | Toestemming Conselleria de Cultura voor ingrepen met "trascendencia patrimonial" (3 maanden stilzwijgen = weigering); historische verkaveling en rooilijnen behouden; gevels van vóór 1940 behouden; nieuwbouw **PB+I plus cambra**, "Quedan prohibidos los semisótanos de nueva planta"; cornisa 8,40 m (2 pl. + cambra), 6,50 m (2 pl.), 3,50 m (1 pl.); pannendak 25–35 %; geen zichtbare zonnepanelen/airco vanaf de openbare weg |
| NT 3 | Zona E (art. 10.5.2) | Tijdelijke oplossingen zonder riolering (collector > 100 m): gecertificeerde afvalwatertank met erkende ophaaldienst; bestaande septische systemen mogen blijven |
| NT 4 | Zona E (art. 10.5.3) | Villa: minimaal 50 % van de dakprojectie hellend met teja árabe; **max. twee zichtbare bouwlagen** (PB + planta piso); 1 boom per 50 m² perceel; verharding max. 50 % van de onbebouwde ruimte; muren 1 m + 2 m hekwerk |

De kaart van de schorsingsgebieden (registerdoc "Ámbitos_suspensión_licencias.pdf", Departament d'Urbanisme, juli 2019) laat zien dat vrijwel alle urbanisaties (groen: "Àmbits de Sòl Urbà Extensiu"), het casco (rood: "Sòl d'Ordenança A"), stroken voor de red primaria (geel) en wegbeschermingszones (oranje) eronder vielen. Bewijstype 2 (kaart visueel gelezen).

### 1.5 Conflicten en interpretatievragen (niet geforceerd opgelost)

| # | Conflict | Standpunt A | Standpunt B | Wat nodig is |
|---|---|---|---|---|
| C1 | Gelden de NUT na ca. 15-03-2025 nog? | NUT-tekst: "estarán en vigor hasta la aprobación del Plan General Estructural" | Zelfde tekst + Consell-acuerdo: schorsing eindigt na 4 jaar; NUT waren bedoeld "para el ámbito de la suspensión"; Generalitat (feb. 2025, pers): toetsen aan PGOU 1990/1991. Een opiniestuk (lamarina.eldiario 20-06-2025) schrijft dat Xàbia werkt met "Normas Transitorias de Urgencia" | Schriftelijk informe urbanístico van de gemeente (TRLOTUP art. 246.4) of advies van een urbanismo-advocaat. **Bewijstype 7** |
| C2 | Weigert de gemeente licenties op grond van het niet-goedgekeurde PGE? | Generalitat/APTD (pers, feb. 2025): ja, feitelijke verlenging van de schorsing | Regidor de Urbanismo (pers, feb. 2025): "licenses are being issued, they are not suspended"; TSJCV erkent toetsingsruimte | Per perceel: navragen of het PGE daar een andere klasse/zone geeft (declassificatie = hoger weigeringsrisico). **Bewijstype 7** |
| C3 | Casco: "4 alturas" (advertentie K14, R15) vs. PB+I (NUT) | Mod. nº I PGOU: bouwhoogte per blok volgens plano B.1 (II t/m V plantas mogelijk) | NUT NT 2 (2021–2025): nieuwbouw PB+I + cambra in het NHT; erfgoedwet (NHT) blijft relevant | Plano B.1 voor dat blok + schriftelijke bevestiging + toets Conselleria de Cultura. **Bewijstype 7** |
| C4 | Datum documento de referencia | 24-11-2011 (Ajuntament, DOGV 07-04-2021) | 08-11-2011 (Consell, DOGV 15-03-2021) | Niet belangrijk voor bouwrecht; genoteerd |
| C5 | Volledigheid van de geconsolideerde ordenanzas | Registerpdf bevat vervangende bladen van Mod. I en van de zona C-wijziging (gestempeld "MOD. P. Nº 5", vermoedelijk Mod. V) | Latere modificaciones (bv. XXV uit 2016, 27 uit 2003) staan níet in die pdf verwerkt | Gemeente vragen om de geldende "texto refundido" van de normas |

---

## 2. Zones en parameters voor woningbouw (opdracht b)

### 2.1 Zo bepaal je welke regels op een perceel van toepassing zijn

1. **Klasse en instrument**: suelo urbano (SU), urbanizable (SUP/SUNP, in de GVA-laag "SUZ") of no urbanizable (SNU). Ligt het perceel in een plan parcial, PRI, homologación of UA, dan gelden eerst díe normen; het PGOU verwijst naar "los cuadros de delimitación (Anexo 1/3)" en de "correspondientes Planes Parciales". Bron: ordenanzas art. 2.1.3, 10.3.2, 10.5.1.1. Bewijstype 2.
2. **Zone**: "En el Plano de Ordenación B1 se señalan con letras (de la A a la H)…"; residencial extensivo zonder letter = **zona E2**. Bron: ordenanzas art. 2.1.6 (pdf-p. 17). Bewijstype 2.
3. **Gebied voor parcela mínima en edificabilidad (zona E)**: plano B.2, gebiedsnamen ruwweg naar kadastrale toponiemen; "tienen validez para la determinación de la edificabilidad en suelo extensivo y para el establecimiento de la parcela mínima". Bron: art. 2.1.6. Bewijstype 2.
4. **Wijzigingen**: modificaciones per gebied (§1.3) en de NUT-vraag (C1).
5. **Sectorale lagen**: parque natural, PATIVEL, costas, cauces, carreteras, catálogo (§3.3 en §6).

Onderdeel A: Zones A (casco), B (ensanche), C (edificación abierta), D (conjuntos arquitectónicos), E (residencial extensivo), F (comercial/terciario), G (industrial), H (comercial concentrado). Bron: inhoudsopgave titel X (pdf-p. 135–167). Bewijstype 2.

**Documentbron voor heel §2:** Registro Autonómico GVA, 03082-1000 PLAN GENERAL / 3 NORMAS URBANÍSTICAS / "03082-1000 ORDENANZAS.pdf" (240 blz., koptekst "Revisió i Adaptació del Pla General d'Ordenació Urbana — Març 1989", deels "Texte refundit. Aprovació definitiva. Gener 1990", met vervangende bladen van Mod. I en van een zona C-wijziging gestempeld "MOD. P. Nº 5", vermoedelijk Mod. V). "pdf-p." = paginanummer in die pdf; "full nº" = oorspronkelijk bladnummer.

### 2.2 Algemene definities (titel VIII), bepalend voor bruto/netto en wat meetelt

| Art. | Regel (samengevat; citaat waar essentieel) | pdf-p. | Type |
|---|---|---|---|
| 8.1.3 (versie Mod. XXV, 2016) | Parcela mínima in m² grond; geen verkavelingen onder het minimum; in suelo urbano met gewijzigd minimum mag worden gebouwd op kavels volgens de oude normen als de vorm niet is gewijzigd na de aanvankelijke goedkeuring van het PG (05-09-1988), met bewijs (registro, parcelación); samenvoegingen die het aantal woningen verlagen mogen; grenscorrecties toegestaan; geen minimum voor dotacionele percelen | BOP 16-12-2016 blz. 3–4 | 2 |
| 8.1.5 | Ocupación = overdekte of gesloten oppervlakte op begane grond of funderingsaanzet t.o.v. het **totale** perceel; "superficie cubierta" = elke doorlopende, permanente overkapping (dus ook porches/naya's); "cerrada" = verticale elementen > 40 cm; uitkragingen > 3 m hoogte en niet gesloten tellen niet | 72–73 | 2 |
| 8.1.6 | Solar in residencial extensivo: water, stroom, toegang, afvalwaterzuivering volgens 10.5.2.3 (strengere eisen in Casco, Aduanas, Arenal, Montañar). Mod. XXV wilde 8.1.6 wijzigen; **dat deel is geschorst** | 74; BOP 16-12-2016 | 2 |
| 8.1.13 / 8.1.14 | **Edificabilidad bruta** = m² bebouwbaar / m² polígono **inclusief** interne wegen en cessiegronden; **neta** = t.o.v. netto perceel **exclusief** wegen en cessies | 76 | 2 |
| 8.1.15 | Meetellend vloeroppervlak: alle beloopbare verdiepingen **behalve toegestane kelders**; overdekte terrassen, balkons en uitbouwen tellen mee, "se considerará la mitad cuando sean terrazas cubiertas y no esté cerrado por alguno de sus frentes"; permanente bijgebouwen tellen mee. Niet: binnenpatio's, platte daken, openbare arcades, lichte kassen/afdaken. Max. volume = m² × 3 m (wonen) | 77 (visueel) | 2 |
| 8.1.19 | Aantal bouwlagen incl. begane grond, **excl. semisótanos** en ruimte onder hellend dak | 78 [OCR] | 2 |
| 8.1.23.2 | Extensief: kroonlijsthoogte t.o.v. natuurlijk terrein; keermuren max. 2,5 m hoog met tussenafstand afhankelijk van helling [formule OCR onleesbaar]; afstand gevel–keermuur idem | 80 [OCR] | 2 |
| 8.1.26 | Boven kroonlijst: dakvlak max. 25°; zolder telt mee boven 1,80 m vrije hoogte; trappenhuis/lift max. 3,10 m | 81 [OCR] | 2 |
| 8.1.27 (Mod. I) | Buiten zones A/B: kelder = bouwdeel **onder de footprint** met bovenkant plafond < 1,20 m boven natuurlijk terrein, gemeten op alle punten van de omtrek; kruipruimtes < 1,80 m vrij tellen niet mee; **in zones C, E, F, G, H moeten kelders en hellingbanen onder maaiveld ≥ 2,5 m van de perceelgrens blijven** | 82–84 | 2 |
| 4.1.8 / 4.1.9 | **Bruto/netto in zona E:** "derecho de aprovechamiento" **0,142 m²t/m² bruto** tegenover "edificabilidad" **0,20 m²t/m² solar neto** (gebieden Calvario, Puchol, Soberana, Mesquides, Cuesta de S. Antonio en Caleta Puerto: 0,198 / 0,28); zones C, F, G, H: 0,58 / 1. Het verschil ("29,07 % de cesiones en suelo extensivo") moet worden afgestaan voor wegen en groen, zo nodig via een discontinue actuación/transferencia de aprovechamiento | 34, 37 (visueel) | 2 |

**Interpretatievraag (bewijstype 7):** geldt 0,20 m²t/m² op het **netto** perceel direct voor een bestaande kavel in een al ontsloten urbanisatie, of moet de eigenaar eerst aantonen dat de 29,07 % cessie is voldaan (anders 0,142 × bruto)? Per perceel voorleggen aan gemeente/architect.

### 2.3 Zona E — Residencial extensivo (Montgó, Tosalet, Cap Martí, Balcón al Mar e.d.)

Bron: ordenanzas art. 10.5 (pdf-p. 156–167; tabellen en zona E visueel gelezen), Mod. XXV (BOP 16-12-2016), Mod. 27 (DOGV 08-01-2004). Bewijstype 2. **Let op:** alleen voor percelen die feitelijk onder de PGOU-zone E vallen en niet onder een plan parcial of UA met eigen tabel.

**a) Parcela mínima per gebied (art. 10.5.1.1, tabel "Suelo urbano – resumen", full nº 145–146, visueel gelezen):**

| Gebied (plano B.2) | Parcela mín. (m²) | Gebied | Parcela mín. (m²) |
|---|---|---|---|
| Aduanas (intensief/extensief) | 700 | Covatelles | 1.500 |
| Casco (intensief/extensief) | 700 | Entrepinos | 1.000 |
| Playas (intensief/extensief) | 600 | Lluca | 1.500 |
| Saladar (intensief/extensief) | 1.000 | Lluca-Rafalet | 1.000 |
| Granadella (intensief/extensief) | 1.000 | Mar Azul | 1.000 |
| Adsubia-Cansalades | 1.000 | Masenes | 1.000 |
| Adsubia-Cap Martí | 1.000 | Media Luna | 1.000 |
| Adsubia-Rebaldí | 1.000 | Mesquides | 1.000 |
| Balcón al Mar | 1.000 | Montgó | 1.500 |
| C.S. Antonio | 1.000 | Montgó-Barranqueres | 1.500 |
| Cala Blanca Norte | 1.500 | Montgó-Castellans | 1.500 |
| Cala Blanca Sur | 1.000 | Montgó-Ermita | 1.500 |
| Caleta-Puerto | 500 | Portichol 1 Norte | 1.500 |
| Calvario | 700 | Portichol 1 Sur | 1.000 |
| Cansalades | 1.000 | Portichol 2 | 1.000 |
| Capsades 1 | 1.000 | Puchol | 1.000 |
| Capsades 2 | 1.000 | Rafals | 1.000 |
| Cap Martí | 1.000 | Senioles | 1.500 |
| Costa Nova | 1.000 | Senioles-Colomer | 1.500 |
| Soberana | 1.000 | Toscal-Cap Martí | 1.000 |
| Tosalet | 1.000 | Trencall | 1.000 |
| Valls | 1.500 | | |

Nog te checken: of latere modificaciones deze tabel voor bepaalde gebieden hebben veranderd (niet in het register gevonden) [te verifiëren].

**b) Overige perceeleisen (art. 10.5.1.1, tekst Mod. XXV, BOP 16-12-2016):**
- Frente de parcela 20 m; aan een doodlopende weg ("cul de sac") 10 m.
- Er moet een rechthoek van 15 × 24 m in het perceel passen.
- Uitzonderingen (kleinere kavels bebouwbaar): (a) ingesloten door percelen met bestaande bebouwing; (b) percelen onder art. 8.1.3.3; (c) percelen in "suelos urbanos extensivos, categorizados como consolidados por la urbanización" die aantoonbaar al zo waren vóór de información pública van Mod. XXV. In alle gevallen: "Se deberá superar siempre el 70% de la superficie mínima de parcela fijada para cada zona, con un mínimo de 700 m2", met minimaal 3,0 m toegang vanaf een berijdbare weg.
- **Splitsen:** percelen kleiner dan tweemaal het minimum zijn ondeelbaar (TRLOTUP art. 248.c; PGOU art. 8.1.3 oud: "indivisibles"). Bewijstype 2.

**c) Bebouwingsparameters (art. 10.5.1.2–8; Mod. I-blad full nº 146–147 en oorspronkelijk blad full nº 147; visueel):**

| Parameter | Grado I | Grado II (standaard "E2") | Grado III |
|---|---|---|---|
| Edificabilidad | 0,142 m²t/m² bruto; **0,20 m²t/m² neto** (Calvario, Puchol, Soberana, Mesquides, Cuesta S. Antonio, Caleta Puerto en, volgens Mod. I, La Corona: 0,198 bruto / 0,28 neto, "excluidas las cesiones") | idem | idem |
| Max. bouwlagen | 1 | 2 | 2 |
| Kroonlijsthoogte (A.L.C.) | 3,5 m | 7 m | 7 m |
| Totale hoogte | 6,00 m | 9,50 m | 9,50 m |
| Afstand tot rooilijn (fachada) | 5 m | 5 m | 0 m |
| Afstand tot perceelgrens (lindero) | 5 m | 5 m | 2,5 m |
| Ocupación máxima | 20 % | 30 % | 50 % |

- Welk grado geldt, staat op plano B.1; zonder letter = E2. De ocupación-alinea staat wél op het oorspronkelijke (doorgehaalde) blad full nº 147, maar is op het vervangende Mod. I-blad afgedekt door de goedkeuringsstempel → **[te verifiëren]** of die percentages ongewijzigd zijn.
- **Bijgebouwen:** gesloten én overdekte bijgebouwen tellen als bebouwde oppervlakte. Poorten 1 m terug van de rooilijn, max. 3 m hoog.
- **Carports:** geen zijwanden, dak van doorlatend materiaal (riet, planten), max. 30 m² en 2,20 m hoog, palen max. 25 × 25 cm.
- **Zwembaden:** "La distancia a lindes de vasos de piscinas y demás elementos de obra complementarios de la urbanización será de 2 m" (Mod. I-blad full nº 147 en oorspronkelijk blad full nº 148, beide 2 m), max. 2,5 m boven natuurlijk terrein; pomphuis > 1 m hoog op ≥ 5 m van de grens; zuivering verplicht.
- **Barbecues:** overdekt ≥ 5 m van de grens, open en ≤ 2 m hoog op de helft daarvan.
- **Omheinde droogplaatsen** ≤ 2,5 m hoog: 2,5 m van de grens.
- **Septic tank / zinkput:** 5 m van de gevel, 2 m van de grens. Elke woning heeft een watertank van ≥ 10.000 l nodig (onder de woning of ingegraven).
- **Kelder ("8. Sótano"):** "se admiten en vertical de lo edificado en plantas superiores", met bovenkant plafond < 1,20 m boven natuurlijk terrein (art. 8.1.27) en ≥ 2,5 m van de grens. Kelders tellen niet mee voor edificabilidad (art. 8.1.15.a).
- **Naya's, porches, overdekte terrassen:** geen aparte regel in zona E gevonden. Algemene regels: ze tellen voor ocupación (overdekt = bezet, art. 8.1.5) en voor edificabilidad (volledig of half, art. 8.1.15.b). **[Interpretatievraag]** hoe de gemeente "no esté cerrado por alguno de sus frentes" toepast.
- **Garages:** zie carport en kelder. Een in het talud ingegraven garage krijgt de deur ≥ 1 m terug van de rooilijn en ≥ 5 m van de grens met overliggende percelen (art. 10.5.3.7; NUT NT 4 zelfde tekst).
- **Parkeren:** "dos plazas por vivienda en el interior de la parcela" (art. 10.5.4.3, tekst Mod. 27, DOGV 08-01-2004).
- **Gebruik:** "Uso global: residencia unifamiliar. Edificación aislada". Toegestaan naast wonen, onder voorwaarden: commercieel/recreatief/hotel aan viario de sistema general of hoofdweg (> 10 m breed), socio-cultural, docente, sanitario, público-administrativo. Voor niet-woonfuncties: ≥ 10 m tot grenzen, gevellengte ≤ 35 m, perceel ondeelbaar. Hotel buiten hoofdwegen alleen 4–5 sterren, perceel ≥ 5.000 m² en max. 1.500 m² vloeroppervlak (art. 10.5.7).
- **Meer woningen op één perceel:**
  - Art. 10.5.5 **agrupación** (via Estudio de Detalle): ≥ 100 m² per woning, per twee geschakeld, groepen van max. 10, perceel ≥ 5.000 m², niet meer woningen dan bij losse verkaveling volgens het minimum. Bovenste derde van een hellend perceel grenzend aan SNUEP blijft onbebouwd; 15 m tot grenzen en rooilijn.
  - Art. 10.5.6 **parcela mancomunada** (ED): perceel ≥ **1,3 × n × parcela mínima**, 10 m tussen woningen, woning ≥ 100 m², perceel ondeelbaar ingeschreven, geen hekken binnen het perceel, totaal ≤ maximum van de zone. Bron pdf-p. 157–167 [deels OCR]. Bewijstype 2.
- **Esthetiek (art. 10.5.3 oorspronkelijk):** vrije ruimte houdt natuurlijk maaiveld, terrassering respecteert het oorspronkelijke profiel, 1 boom per 50 m², muur 1 m + 2 m hekwerk, uitkraging max. 50 cm in grado III. De verhardingsgrens is in de OCR onleesbaar [OCR, pdf-p. 156 controleren]. Onder de NUT (2021–2025) aangescherpt, zie §1.4.

**d) Rekenvoorbeeld (bewijstype 5, alleen methode, geen bouwrecht)** — perceel 1.572 m² in gebied Montgó-Ermita, uitsluitend als PGOU zona E2 met netto = bruto:
- Parcela mínima 1.500 m² → bebouwbaar, niet splitsbaar (< 3.000 m²).
- Maximaal vloeroppervlak: 1.572 × 0,20 = **314 m²t** (of 1.572 × 0,142 = 223 m²t als de cessievraag negatief uitvalt).
- Maximale footprint: 1.572 × 30 % = **472 m²**. Het vloeroppervlak is de beperkende factor; niet vermenigvuldigen met het aantal bouwlagen.
- **Maar:** het K07-perceel met deze oppervlakte (R11/R15) ligt volgens de GVA-laag in **Plan Parcial Ermita II** (§2.8). Dan gelden de ordenanzas van dat plan parcial, niet deze tabel.

### 2.4 Zona A — Casco (oude kern)

Bronnen: ordenanzas art. 10.1 (Mod. I-blad full nº 131 "Modificación Nº 114-C", goedgekeurd 14-02-1994, visueel), NUT NT 2 (2021). Bewijstype 2.

| Parameter | PGOU (Mod. I) | NUT NHT (2021 – ca. 03-2025, zie C1) |
|---|---|---|
| Parcela mínima | Moet een minimale woning kunnen bevatten (max. 2 bouwlagen gerekend); nieuwe verkavelingen gevelbreedte ≤ 15 m (hoekperceel 15/25 m) | Historische verkaveling behouden |
| Rooilijn | Volgens de plankaart, geen terugliggende gevels | Historische rooilijnen, geen terugliggende gevels of voorpatio's |
| Bezetting / diepte | Begane grond volledig; verdiepingen tot 20 m vanaf de rooilijn [OCR] | Traditionele typologie; hoofdvolume 8–11 m diep |
| Bouwlagen | Volgens plano B.1 per blok | PB + I (+ cambra); hogere gebouwen "fuera de ordenación" |
| Kroonlijst / totaal | II: 6,1 / 9,1 m · III: 9,0 / 12,0 · IV: 12,0 / 15,0 · V: 15,0 / 18,0 m | 3,50 m (1 pl.) · 6,50 (2) · 8,40 (2 + cambra) |
| Tolerantie | Twee bouwlagen minder toegestaan, behalve tussen al geconsolideerde gebouwen | — |
| Kelder | "Se admite una planta sótano situada dentro de la superficie ocupable" | Nieuwe semisótanos verboden |
| Dak | Hellend, teja árabe; dakterras max. 50 % van het dak, eerste 3 m aan straatzijde hellend [OCR] | Teja árabe 25–35 %, nok max. 2,25 m, geen dakkapellen |
| Parkeren | Nieuwbouw van ≤ 4 woningen geen reserve; anders 0,6 plaats per woning [OCR, pdf-p. 139] | — |
| Erfgoed | — | Toestemming Conselleria de Cultura bij "trascendencia patrimonial" |

**Dealmakerspunt:** advertentie K14 (R15) belooft "4 alturas… 12 viviendas" onder "ordenanza A CASCO". Dat kan alleen als plano B.1 daar IV aangeeft én de NUT-/erfgoedbeperking niet (meer) geldt. Tot schriftelijke bevestiging: 7.

### 2.5 Zona B (Ensanche) en zona C (Edificación abierta) — kort

| Zone | Kern | Bron | Type |
|---|---|---|---|
| B Ensanche | Perceel ≥ 100 m² en ≥ 6 m gevel; begane grond volledig, verdiepingen 20 m diep bij binnenterrein; bouwlagen volgens B.1; kelders toegestaan; tolerantie twee lagen minder; dak hellend teja árabe | art. 10.2 (pdf-p. 139–141) [OCR] | 2 |
| C Edificación abierta (o.a. Montañar I; Arenal/Puerto afhankelijk van B.1) | Grado I–IV: perceel 500 / 500 / 1.000 / 1.000 m², gevel 20 m. Afstand tot rooilijn vrij / ≥ 5 / ≥ 14 m aan zeezijde (anders 5) / ≥ 5 m; tot grens ≥ 5 m of ½ kroonlijsthoogte (min. 5 m). Ocupación 70 / 50 / 50 / 50 %. Edificabilidad per UA via Estudio de Detalle; C3 0,80 m²t/m² neto en C3A 0,80 bruto (wijzigingsblad "MOD. P. Nº 5", vermoedelijk Mod. V). Bouwlagen volgens B.1 | art. 10.3 (wijzigingsbladen pdf-p. 143–145) [deels OCR] | 2 |
| F Terciario (strandboulevard) | 1 bouwlaag, 3,50 m, perceel = heel bouwblok, verplichte "naya" rondom (Mod. XII) | registerdoc 03082-1020 NNUU | 2 |

Arenal en Puerto: **welke zone per blok geldt, is niet vastgesteld** (plano B.1 niet gelezen; er gelden ook homologaciones/PRI's, zoals Arenal-3). Niet generaliseren.

### 2.6 Suelo urbanizable

| Situatie | Regel | Bron | Type |
|---|---|---|---|
| SUP met goedgekeurd plan parcial ("SUEP", in uitvoering) | Parameters uit het plan parcial; licenties onder de toenmalige art. 42 TRLS; percelen worden solar pas na urbanisatie | ordenanzas art. 2.1.3 (pdf-p. 15–16) | 2 |
| Bouwen vóór de urbanisatie klaar is | Alleen met "afianzamiento del importe íntegro del coste de las obras de urbanización" en de verplichting het gebouw niet te gebruiken tot de urbanisatie klaar is; die voorwaarde gaat mee bij verkoop en komt in de akte van obra nueva | **TRLOTUP art. 187.1** | 2 |
| SUNP zonder PAU | El Plà volgt SNU grado III; overige SUNP volgen SNU genérico grado I | ordenanzas art. 6.1.2 (pdf-p. 57) | 2 |
| Urbanizable zonder vastgesteld programa (huidige wet) | Alleen agrarische en vergelijkbare bouwwerken en nutsvoorzieningen; "quedando prohibidas las edificaciones características de las zonas urbanas"; niet splitsbaar | TRLOTUP art. 226.1, 248.e | 2 |
| Afgebroken PAI | Situatie volgens de afwikkeling (art. 172) | TRLOTUP art. 226.2 | 2 |
| PGE-voorstel | Ca. 8 miljoen m² urbanizable minder (2019); versie 2017: van 10,5 naar 2,89 miljoen m²; Saladar I–III en golfsector gedeclassificeerd | ajxabia.com/ver/7823; en.javea.com 08-06-2017 | 2 / 1 |

**Dealmakerspunt:** grond die in 1990 urbanizable werd maar niet ontwikkeld is, heeft **geen woonbouwrecht** zolang er geen goedgekeurd programa is. Het PGE-voorstel wil een groot deel ervan declassificeren. Een prijs op basis van "urbanizable" is dan speculatie (bewijstype 4).

### 2.7 Wat níet in de PGOU-normen staat of niet is gevonden

| Onderwerp | Bevinding |
|---|---|
| Aparte regels voor naya's/porches in zona E | Niet gevonden; alleen via art. 8.1.5 en 8.1.15 |
| Aantal woningen per perceel in zona E | Uitgangspunt één (unifamiliar aislada); meer alleen via 10.5.5/10.5.6 met Estudio de Detalle |
| Geldende tekst na alle modificaciones | Niet beschikbaar als geconsolideerde versie (C5) |
| Plano B.1/B.2 digitaal per perceel | Scans in het register (72 "Planos de ORD"); niet gegeorefereerd gelezen. "Cartoxabia" (ajxabia 15-02-2018) genoemd, maar geen werkende URL gevonden |
| Normas van het PGE 2019 | Niet opgehaald (alleen informatief) |

### 2.8 Proef: GVA-planningslaag op echte advertentiepunten (bewijstype 3 voor de uitkomst; laag zelf informatief)

Dienst: `https://terramapas.icv.gva.es/0702_Planeamiento` (WFS 2.0; typenames `ms:Planeamiento.Clasificacion` en `ms:Planeamiento.Zonificacion`; `Fees` "No se aplican condiciones", `AccessConstraints` "CC BY 4.0 Generalitat"). Disclaimer in de datasetbeschrijving: "El planeamiento aquí reflejado tiene carácter informativo." Getest op 15-09-2026 met een bbox van ±0,00015° rond het punt; één verzoek per punt.

| Punt (bron) | Advertentieclaim | GVA-laag: instrument · klasse · zone | Gevolg voor de dealcheck |
|---|---|---|---|
| K07 / BP 4676JAV Garroferal, Montgó-Ermita (R11-pin 38.7940774, 0.123362) | "licencia de obras aprobada", "aval bancario de la urbanización" | **PLAN PARCIAL "ERMITA II"** (exp. 19940463) · SUZ · ZND-RE | Normen van PP Ermita II opvragen; aval past bij art. 187 (urbanisatie niet opgeleverd?) |
| K08 El Rafalet, c/ Mar Amarillo (38.7620527, 0.1543695) | "parcela urbana… licencia vigente" | Plan general · **SUZ** · ZND-RE | Klasse spreekt advertentie tegen → stand van de urbanisatie en licentie verifiëren |
| K14 casco (38.7899, 0.1638, pin benaderend) | "ordenanza A CASCO… 4 alturas" | Plan general · SU · **ZUR-NHT** | Erfgoedregime NHT + C3 |
| BP 4544JAV Adsubia (38.764457, 0.182689) | 2.600 m² splitsbaar in 2 × 1.300 m² | Plan general · SU · ZUR-RE | Bij zona E Adsubia-gebied 1.000 m² ≥ 2 × minimum (plus 20 m gevel en rechthoek 15 × 24 m) = theoretisch mogelijk; parcelación-licentie nodig (art. 247) |
| BP 4603JAV Villes del Vent (38.738017, 0.162393) | "coeficiente de edificabilidad del 16,5 %… sótano 200 m2" | **HOMOLOGACIÓN Y PLAN PARCIAL SUNP CANSALADES-UMBRÍA** (exp. 20011281) · SUZ · ZND-RE | Parameters uit het PP, niet uit de PGOU-tabel |
| BP 4623JAV Tosalet 5 (38.762048, 0.169001) | "terreno edificable… urbanización moderna" | Plan general · **SUZ** · ZND-RE (2 features) | Status urbanisatie en programa checken |
| BP 4649JAV Mar Azul/Portichol (38.750034, 0.219812) | "Suelo Dotacional Privado, 0,20, 2 plantas (9,50 m)" | Plan general · SU · ZUR-RE | Geen dotacional-onderscheid in deze laag; Mod. nº 2/8 (UA Mar Azul) raadplegen |

**Telling voor Xàbia** (bbox rond de gemeente, gefilterd op `cod_ine_mun=03082`; eigen telling, bewijstype 3): 356 zonevlakken — SUZ/ZND-RE 140; SU/ZUR-RE 126; SNU-P/ZRP-NA-MU 24; SNU-P/ZRP-NA-LG 18; SNU-C/ZRC-FO 12; SUZ/ZND-TR 9; SNU-P/ZRP-CA 9; SU/ZUR-NHT 5; SNU-P/ZRP-CR 4; SU/ZUR-IN 3; SNU-P/ZRP-CT 2; SU/ZUR-TR 2; SUZ/ZND-IN 1; 1 onleesbaar record.

**Datakwaliteit:** de laag bevat nog 20 vlakken "HOMOLOGACIÓN MODIFICATIVA DEL PLAN GENERAL, AREA DEL PORTITXOL", terwijl het register die homologación als "Anulado" markeert (TSJCV 26-04-2012). Gebruik de laag daarom alleen als **eerste filter**, nooit als bouwrecht.

---

## 3. Suelo no urbanizable in Xàbia (opdracht c)

### 3.1 Categorieën

| Bron | Categorieën |
|---|---|
| PGOU titel VII (art. 7.1.1, pdf-p. 61) | (a) "Zona no urbanizable genérica, Grados 1, 2 y 3"; (b) "Zona no urbanizable de Protección Ecológico-Paisajística" (SNUEP); plus aparte bescherming van archeologische vindplaatsen en historisch-artistieke gebouwen. Grado I = alle genérico-grond behalve El Plà en La Plana; grado II = La Plana; grado III = El Plà. La Granadella werd in 1991 SNU protección ecológico-paisajística, met SNU grado 1-regels voor de bestaande woningen in het gehucht |
| GVA-laag (geharmoniseerd, informatief) | SNU-P: ZRP-NA-MU (gemeentelijk beschermd: bos/landschap), ZRP-NA-LG (milieuwetgeving: Parque Natural del Montgó, PATIVEL), ZRP-CA (waterlopen), ZRP-CR (wegen), ZRP-CT (kust); SNU-C: ZRC-FO (gewoon, bos). Instrumenten o.a. "PLAN GENERAL (Parque Natural de El Montgó)" en "PAT INFRAESTRUCTURA VERDE DEL LITORAL (PATIVEL)" |

"Agrícola" als gemeentelijke categorie: het PGOU kent "protección agrícola" alleen via El Plà (SUNP → SNU grado III) en de verwijzing in art. 6.1.2. De PGE-versie 2019 herclassificeerde delen van Rebaldí en Capsades "de protección forestal a agrícola" (ajxabia.com/ver/7741), maar dat plan geldt niet.

### 3.2 Nieuwbouw woning: PGOU tegenover de huidige regionale wet

| Eis | PGOU 1990 grado I (pdf-p. 65, visueel) | PGOU grado II La Plana | PGOU grado III El Plà | **TRLOTUP art. 211.1.b (geldend)** |
|---|---|---|---|---|
| Minimumperceel | 5.000 m² ("una unidad por parcela catastral") | 5.000 m² | 10.000 m² | **"en ningún caso será inferior a una hectárea por vivienda"** |
| Edificabilidad / bezetting | 0,03 m²/m², max. 300 m² | 0,03, max. 300 m² | 0,01, max. 300 m² | **Bezetting ≤ 2 %** van de finca; bijbehorende voorzieningen zonder bouwwerk op maaiveld ≤ 2 % |
| Hoogte / lagen | 7 m / 2 | 5 m / 2, gevel natuursteen | 7 m / 2 | Zonder plan max. 2 lagen (art. 210.2) |
| Afstanden | 10 m tot grenzen; frente 20 m aan kadastrale weg | idem | frente 40 m | Buiten afstroomgeulen; bomen en topografie respecteren |
| Overig | Watertank 10.000 l; zuivering volgens 10.5.2.3; geen nieuwe wegen; muur max. 1 m; CPU-goedkeuring (oud recht) | idem | idem | Plan moet de gebieden aanwijzen; geen kernvorming; geen meerdere woningen op één perceel; water/afval/afvalwater op kosten eigenaar; licentie met inschrijving van de gekoppelde minimumoppervlakte (art. 214.4); **stilzwijgen = weigering** (art. 214.5); in SNU protegido rapport Conselleria de Urbanismo (art. 215.2.c) |
| SNUEP | "No se permite ningún tipo de edificación de nueva planta" (art. 7.3.3, pdf-p. 70) | — | — | Beschermd regime; alleen wat plan en sectorwet toestaan |

**Afgeleide conclusie (bewijstype 4, laten bevestigen):** in SNU genérico mag vandaag feitelijk **pas vanaf 10.000 m²** een woning, met max. 2 % bezetting (bij 1 ha: 200 m² footprint), en alleen als het plan dat gebied aanwijst. De 5.000 m² van het PGOU is door de strengere wet achterhaald. In SNUEP en Parque Natural: geen nieuwe woning. Bestaande woningen in SNU: minimalisatieregime (art. 228 e.v.); de GVA-laag "MinimizacionViviendasSNU" bestaat, maar is niet voor Xàbia bevraagd.

### 3.3 Sectorale lagen die in Xàbia vaak spelen (alleen gesignaleerd; inhoud niet onderzocht in R12)

| Laag | Officiële grondslag | Status R12 |
|---|---|---|
| Parque Natural del Montgó | Decreto 25/1987 (declaratie); Decreto 180/2002 (PORN); Decreto 229/2007 (PRUG) | Lijst gezien op parquesnaturales.gva.es; tekst PORN niet bereikt (cma.gva.es DNS-fout) |
| PATIVEL (kust) | Decreto 58/2018 | Bestaan bevestigd via GVA-laag; hernoeming in 2025 alleen in een zoeksamenvatting gezien [te verifiëren] |
| Costas, cauces, carreteras | Sectorwetten; GVA-zones ZRP-CT/CA/CR | Niet onderzocht |
| PATRICOVA (overstroming) | In 2019 door de Consell als rapport voor het PGE gevraagd | Niet onderzocht (zie terrein-/risicostroom) |
| Catálogo de Bienes y Espacios Protegidos | Mod. nº XVII (CTU 27-03-2008) | Documenten in het register; niet gelezen |

---

## 4. Vergunningsroute, termijnen en leges (opdracht d)

Wettelijke bron: TRLOTUP (Decreto Legislativo 1/2021), geconsolideerd BOE, update 02-07-2026. Bewijstype 2.

### 4.1 Welk instrument voor welk werk

| Werk | Instrument | Artikel |
|---|---|---|
| Nieuwbouw, uitbreiding met nieuw volume, prefab woning | **Licencia urbanística** (proyecto técnico + informe técnico en jurídico) | 232.b–c; 239.2 |
| Grondverzet, verkaveling, splitsing | Licencia (parcelación binnen 1 maand te beslissen) | 232.a; 240.1.a; 247 |
| Ingrepen in gecatalogiseerde gebouwen met erfgoedbelang | Licencia de intervención (3 maanden) | 232.f; 236; 240.1.c |
| Verbouw die de constructie raakt zonder hoofddraagelementen te vervangen; gevel/interieur; gewone renovatie; muren en hekken; **eerste ocupación en "segundo y siguientes actos de ocupación de viviendas"** | **Declaración responsable (DR)** — direct starten na indiening | 233.1; 241.3 |
| Constructieve verbouw, sloop, functiewijziging, werk in de ondergrond, nieuwe paden | DR **plus certificaat** van een certificeringsinstelling of beroepsorde | 233.2 |
| Tijdelijke werken/functies | Licencia provisional (max. 5 jaar in suelo urbano/urbanizable sin programar) | 235 |
| SNU | Licencia, eventueel na declaración de interés comunitario; sectorale rapporten | 214–216 |

Bij een DR geldt het plan dat van kracht is op de indieningsdatum (art. 241.6); bij een licentie het plan op de beslisdatum, tenzij de termijn is overschreden (art. 238.2).

### 4.2 Termijnen, stilzwijgen en vervallen

| Onderwerp | Regel | Artikel |
|---|---|---|
| Nieuwbouw of daarmee gelijk te stellen verbouw; sloop | Beslissing binnen **2 maanden** | 240.1.b |
| Overige licenties | 2 maanden | 240.1.d |
| Stilzwijgen | **Positief** alleen in de gevallen van art. 233.2.a, c, d, g; alle andere licenties (dus nieuwbouw) bij stilzwijgen **geweigerd** | 242 |
| Uitvoeringstermijn | Volgens licentie; anders 6 maanden om te starten en 24 maanden om af te bouwen, max. 6 maanden onderbreking | 188.2 |
| Verval | Na hoorzitting; verlenging max. gelijk aan de oorspronkelijke termijn, mits de licentie nog past in het dan geldende plan; na verval nieuwe licentie volgens het nieuwe plan | 244 |
| ECUV-route | Aanvrager voegt certificaat van een Entidad Colaboradora (ECUV) bij; vervangt het technisch rapport van de gemeente; geen cédula nodig | 238.3; 239.3–5 |

**Dealmakerspunt:** een "licencia concedida" uit 2020 (bv. LOM-2020/51 in R15) kan vervallen zijn als de werken niet binnen de termijn zijn gestart. Altijd de licentie zelf met termijnen en eventuele verlengingen opvragen (bewijstype 4 → 2 na inzage).

### 4.3 Cédula de garantía urbanística, informe urbanístico, certificado de compatibilidad

| Instrument | Wat het is | Termijn / geldigheid | Kosten in Xàbia | Aanvraag |
|---|---|---|---|---|
| **Cédula de garantía urbanística** (art. 246.1–3) | Vermeldt zonering en klasse van een bebouwbaar perceel; tijdens de geldigheid krijgt de eigenaar schadevergoeding bij latere planwijziging, mits geen openstaande cessie-, verdelings- of urbanisatieplichten (die moeten in de cédula staan) | Uitgifte binnen **1 maand**; geldig max. **1 jaar**; wordt opgeschort tijdens een licentieschorsing | **ONBEKEND** (tasa niet gevonden) | "a petición de las partes interesadas": of een koper-in-spe telt als belanghebbende [te verifiëren]; loket: sede electrónica / OAC Urbanismo |
| **Informe urbanístico schriftelijk** (art. 246.4) | "la obligación de informar por escrito a cualquier solicitante respecto de la zonificación, clasificación y programación urbanística de los terrenos" | 1 maand | ONBEKEND | Iedere aanvrager |
| Certificado/informe de compatibilidad urbanística | Voor activiteiten (bv. horeca, VUT) | Niet onderzocht | ONBEKEND | Niet onderzocht; alleen commerciële sites gevonden, geen officiële Xàbia-pagina [te verifiëren] |

### 4.4 Leges en belastingen

| Heffing | Xàbia | Bron | Type |
|---|---|---|---|
| **ICIO** | **4,00 %** in 2025 en 2026 ("Tipo impositivo en porcentaje") | Ministerio de Hacienda, SGFAL, "Impuesto sobre construcciones, instalaciones y obras — Alicante/Alacant", jaren 2025 en 2026 | 2 |
| ICIO grondslag | Werkelijke uitvoeringskosten (PEM), exclusief btw, tasas, honoraria en aannemerswinst; wettelijk max. 4 % | TRLRHL art. 102 (via R14) | 2 |
| Tasa por licencia urbanística / DR / cédula | **ONBEKEND.** Een zoeksamenvatting noemt een "Tasa por el otorgamiento de licencias urbanísticas" in de BOP van 12-07-2010 — niet geverifieerd | Ordenanzas fiscales alleen via `xabia.sedelectronica.es/transparency/9dc46a0e-…` (JavaScript) | 7 |
| Neveninformatie voor R14 | Zelfde Hacienda-bron, 2026: IBI urbano **0,83 %**, rústico 0,60 %, laatste kadastrale herziening **1995**; IIVTNU (plusvalía) tipo **30,00 %** voor alle periodes | Ministerio de Hacienda SGFAL 2026 | 2 |

### 4.5 Werkelijke doorlooptijden (praktijk)

| Gegeven | Bron (datum) | Type |
|---|---|---|
| "esperas de hasta un año" voor bouwvergunningen; "seis o siete meses" zou redelijk zijn; ca. 30 % minder technisch personeel dan tien jaar eerder (2 architecten, 1 landmeter, 1 tekenaar); herziening RPT in voorbereiding | Alicante Plaza, 27-11-2023, op basis van "fuentes municipales" | 1 [te verifiëren] |
| 2022: 240 aanvragen obra mayor (2019: 241; 2020: 179; 2021: 196), 936 obras menores, 63 primera ocupación, 659 segunda ocupación, 105 handhavingsdossiers | xabiaaldia 13-01-2023 ("comunicado íntegro del Ayuntamiento"), via R07-verificatie | 2/1 |
| Aantal bouwvergunningen +25 % sinds 2023; 200–230 nieuwe woningen per jaar | lamarina.eldiario 29-05-2026 (samenvatting, niet letterlijk) | 1 [te verifiëren] |
| Wettelijke termijn nieuwbouw | 2 maanden (art. 240) | 2 |

**Planningsaanname voor het dealmodel (bewijstype 5, geen feit):** reken voor een licentie obra mayor in Xàbia met **6–12 maanden** vanaf een volledig dossier, plus de tijd voor sectorale rapporten (kust, parque natural, erfgoed) waar van toepassing. Te valideren met 2–3 lokale architecten (bewijstype 6).

---

## 5. Lokale bijzonderheden (opdracht e)

| Onderwerp | Bevinding | Bron | Type |
|---|---|---|---|
| Opeenvolgende schorsingen | 2005–2007 gemeentelijk + Decreto 11/2007 → 2017–2019 licentieschorsing PGE → 2021–2025 schorsing PGOU + NUT → 2025 kritiek Generalitat op "de facto" weigeringen | DOGV 29-01-2007, DOGV 15-03-2021, DOGV 20-09-2021, pers feb. 2025 | 2 / 1 |
| Moratorium toeristische verhuur | Mod. nº 41 PGOU aanvankelijk goedgekeurd 28-05-2026: plafond 4.584 VUT, per wijk (o.a. casco 6 %, Puerto 12 %, Tosalet 25 %, Montgó 20 %); nieuwe licenties voor meergezins-VUT 1 jaar geschorst na BOP-publicatie; vorige schorsing liep in april af | en.javea.com 06-06-2026 | 1 [te verifiëren in BOP] |
| Red primaria nieuw (PGE) | Bestaande bebouwing in die stroken was onder NUT NT 1 "fuera de ordenación"; na 2025 onduidelijk, maar signaal voor toekomstige onteigening/tracés | DOGV 20-09-2021 + kaart juli 2019 | 2 / 4 |
| Urbanisaties niet opgeleverd | 2013: Las Laderas (70 percelen) en Pi Ver (226) opgeleverd; nog open: Pou de Moro I (152 woningen), Adsubia-Rebaldí 29, La Cala, Residencial Puerto de Jávea. Zonder oplevering geen cédula de habitabilidad en problemen met stroom- en wateraansluiting. Actuele lijst niet gevonden | ajxabia.com/ver/4540 (22-02-2013) | 2 (verouderd) |
| Aval bancario de urbanización | Wettelijke grondslag: afianzamiento van de volledige urbanisatiekosten bij gelijktijdig bouwen en urbaniseren; geen gebruik vóór oplevering; voorwaarde gaat mee bij verkoop (art. 187.1). Oplevering en garantietermijn: art. 168 (3 maanden stilzwijgen = opgeleverd; 12 maanden garantie) | TRLOTUP | 2 |
| Garroferal-advertentie (K07) | Prijs omvat "aval bancario de la urbanización"; perceel in PP Ermita II (GVA-laag) → waarschijnlijk urbanisatie niet (volledig) opgeleverd | R15 + WFS-test | 4 |
| Cesiones | Zona E: 29,07 % cessie verrekend in 0,142 bruto / 0,20 netto; UA's: cessie vóór licentie; transferencias van aprovechamiento als fysieke cessie onmogelijk is | ordenanzas art. 4.1.7–4.1.9 | 2 |
| Cargas de urbanización | Eigenaar betaalt urbanisatie (art. 4.1.6 PGOU; TRLOTUP 187.2); in PAI's retasación/cuotas (TRLOTUP 150–153) | ordenanzas; TRLOTUP | 2 |
| Cédula de garantía urbanística | Zie §4.3; opgeschort tijdens licentieschorsing (art. 246.3) | TRLOTUP | 2 |
| Stilgevallen of te declassificeren gebieden | PGE-voorstel: −8 miljoen m² urbanizable (o.a. Saladar, golfsector); PAI's ADN-4, MES-2, MES-3 in 2017 geschorst; Portitxol-homologación vernietigd (2012); deel PG "afectado por sentencia del TSJCV de 15/nov./2000" | ajxabia 2019; DOGV 15-03-2021; register; WFS | 2 / 3 |
| Riolering | Veel extensieve urbanisaties zonder collector: septic tanks of afvalwatertanks; bij verkoop zuivering en aansluiting checken (PGOU 10.5.2; NUT NT 3; TRLOTUP 186.2.c) | ordenanzas; DOGV 2021; TRLOTUP | 2 |

---

## 6. Controlelijst per perceel: vult het bouwmogelijkhedenoverzicht van §16 (opdracht f)

Voorwaarde vooraf (§14): exacte kadastrale referentie en geometrie (R11). Zonder die gegevens: "Bouwmogelijkheden nog niet betrouwbaar te bepalen: exacte perceelidentificatie ontbreekt."

| # | Onderdeel (§16) | Primaire bron | Hoe verkrijgen | Automatiseerbaar? | Bewijstype na afronding |
|---|---|---|---|---|---|
| 1 | Klasse en bestemming | Plano A.1/B.1 PGOU + modificaciones; planes parciales | (a) GVA-WFS `Planeamiento.Zonificacion` op perceelcentroïde (filter); (b) registerkaart; (c) **informe urbanístico** art. 246.4 | (a) ja, als filter | 2 (a/b informatief) → 2/6 (c) |
| 2 | Hoofd- en nevenfuncties | Ordenanzas titel X per zone (bv. 10.5.4 tekst Mod. 27) of PP-ordenanzas | Zone uit #1 → artikel | Deels (regeltabel per zone) | 2 |
| 3 | Bouwrijpheid (solar / urbanisatie opgeleverd / aval nodig) | PGOU 8.1.6; TRLOTUP 186–187, 168; recepción-akte | Gemeente: stand van de recepción van de urbanisatie; ter plaatse riolering/water/stroom | Nee | 2 + 3 |
| 4 | Minimumperceel en eisen | Tabel 10.5.1.1 (Mod. XXV), UA/PP-tabellen | Gebied B.2 → tabel; gevel 20 m; rechthoek 15 × 24 m; 70 %-regel | Ja voor tabel; geometrie via Catastro-WFS (R11) | 2 / 5 |
| 5 | Splitsen / samenvoegen | TRLOTUP 247–248; PGOU 8.1.3 | ≥ 2 × minimum; licencia de parcelación | Rekenregel ja | 2 / 5 |
| 6 | Aantal woningen | 10.5.4 (unifamiliar aislada), 10.5.5 (agrupación ≥ 5.000 m²), 10.5.6 (1,3·n·minimum); casco: B.1 + NHT | Rekenregel + Estudio de Detalle | Rekenregel ja; ED nee | 2 / 5 |
| 7 | Edificabilidad | 4.1.9 + 10.5.1.3; PP-ordenanzas | Bruto/netto-vraag per perceel | Ja (met aanname) | 5 → 6 |
| 8 | Ocupación | 10.5.1.6 per grado; 8.1.5 | Grado uit B.1 (zonder letter: E2) | Ja (met aanname grado) | 5 → 2 |
| 9 | Hoogte en bouwlagen | 10.5.1.4; casco B.1 + NHT-vraag; SNU 210.2 | Plankaart | Deels | 2 |
| 10 | Rooilijnen en afstanden | B.3 (alineaciones), 10.5.1.5; kelders 2,5 m (8.1.27.D) | Plankaart + topografische meting | Nee | 2 + 3 |
| 11 | Kelders | 8.1.15.a, 8.1.19, 8.1.27; casco NHT (nieuwe semisótanos verboden 2021–2025) | Ontwerp toetsen | Nee | 2 → 6 |
| 12 | Naya's, terrassen, overkappingen | 8.1.5; 8.1.15.b; carports 30 m² | Architect + gemeentelijke uitleg | Nee | 7 → 6 |
| 13 | Garages en bijgebouwen | 10.5.1.7; 10.5.3.7 | Ontwerp | Nee | 2 |
| 14 | Zwembad | 10.5.1.7 (2 m van de grens, ≤ 2,5 m boven terrein, pomphuis 5 m) | Ontwerp | Nee | 2 |
| 15 | Parkeren | 10.5.4.3 (2 per woning); casco 10.1.4.3 [OCR] | Tabel | Ja | 2 |
| 16 | Ontsluiting en aansluitingen | 8.1.6; 10.5.2; NUT NT 3 (historisch); TRLOTUP 186 | Nutsbedrijven; afstand collector (> 100 m?) | Deels (GIS) | 3 |
| 17 | Bestaande bebouwing en afwijkende status | Licenties/cédulas in het archief; fuera de ordenación (TRLOTUP 206); red primaria PGE | Gemeente-archief; Catastro-bouwjaar (R11); nota simple | Nee | 2 |
| 18 | Stedenbouwkundige lasten | Cessies 29,07 %; UA-/PAI-cuotas; aval (187); retasación | Gemeente + nota simple (afecciones) | Nee | 2 |
| 19 | Sectorale beperkingen | Parque Natural Montgó (PORN/PRUG), PATIVEL, costas, cauces, carreteras, PATRICOVA, catálogo, NHT | GVA-zones ZRP-*; sectorale visors | Deels | 2 (laag) → 2 (rapport) |
| 20 | Benodigde onderzoeken | Geotechniek, topografie, estudio de inundabilidad, paisaje (SNU/NHT), arqueología | Architect | Nee | 6 |
| 21 | Vergunningsroute | TRLOTUP 232–246 | Zie §4 | Beslisboom ja | 2 |
| 22 | Planstatus en PGE-risico | DOGV/BOP; register; PGE-documentatie 2019 | Vraag C1/C2 schriftelijk; PGE-kaart voor dat perceel | Nee | 7 → 2/6 |
| 23 | Open interpretatievragen | — | Lijst per perceel naar architect/gemeente | — | 7 |

**Verplichte waarschuwing in elk dealdossier:** "Uitkomst van de GVA-laag en de PGOU-tabellen is een eerste filter. Bouwrecht pas na informe urbanístico of cédula (art. 246 TRLOTUP), controle van plan parcial/UA, en toets door een lokale architect."

---

## 7. Wat dit betekent voor de Deal Hunter-architectuur (kort)

| Stap | Bron | Status |
|---|---|---|
| Perceelcentroïde → klasse, zone, instrument | GVA/ICV-WFS 0702_Planeamiento (CC BY 4.0) | **Getest** (7 punten); bruikbaar als filter. Filteren op attribuut werkte niet (MapServer-fout); bbox werkt |
| Instrument → normdocument | Registro Autonómico (open directory) | Getest; scans, OCR nodig; onvolledig |
| PGOU-regeltabel zona E en SNU | Dit rapport (handmatig gecontroleerd) | Kan als versiebeheerde regeltabel met bronpagina; per update opnieuw controleren |
| Planstatus / schorsingen | DOGV/BOP, pers | Handmatig; maandelijkse controle voorgesteld |
| Informe urbanístico / cédula | Gemeente | **Alleen handmatig** (⏸️ Jan / architect) |

---

## 8. Bronnenregister (sectie 7-statussen)

| Naam | URL | Type | Toegang | Status | Opmerkingen |
|---|---|---|---|---|---|
| Registro Autonómico de Instrumentos de Planeamiento (GVA), map Xàbia | https://mediambient.gva.es/auto/urbanismo/reg-planeamiento/2%20ALICANTE/03082%20X%C0BIA/ | Overheid, primaire planbron | Open HTTP-directory, geen sleutel | GEVERIFIEERD EN ACTIEF | Scans zonder tekstlaag; niet alle modificaciones en planes parciales (Ermita II ontbreekt); geen PGE |
| ICV/GVA WFS/WMS Planeamiento urbanístico | https://terramapas.icv.gva.es/0702_Planeamiento?service=WFS&request=GetCapabilities | Overheid, geodata | Open, CC BY 4.0, "No se aplican condiciones" | GEVERIFIEERD EN ACTIEF | Informatief; laag bijgewerkt 25-08-2026; bevat geannuleerde Portitxol-homologación; attribuutfilter faalt, bbox werkt |
| Visor GVA planeamiento | https://visor.gva.es/visor/?capas=spaicv0702_plan_clasificacion | Overheid, viewer | Open (browser) | ALLEEN HANDMATIG | Niet geopend in R12 |
| DOGV (pdf-archief) | https://dogv.gva.es/datos/2021/09/20/pdf/docv_9177.pdf ; https://dogv.gva.es/datos/2021/03/15/pdf/docv_9041.pdf | Officieel publicatieblad | Open pdf | GEVERIFIEERD EN ACTIEF | Zoekfunctie ("ficha_disposicion") via iframe/JS niet bruikbaar |
| BOE legislación consolidada — TRLOTUP | https://www.boe.es/buscar/act.php?id=DOGV-r-2021-90283 | Officiële wettekst | Open | GEVERIFIEERD EN ACTIEF | Update 02-07-2026 |
| BOP Alicante (sede) | https://sede.diputacionalicante.es/consultas-bop/ | Officieel publicatieblad | Open, zoeken per datum | ALLEEN HANDMATIG | Geen full-text; datum van ordenanzas fiscales Xàbia onbekend |
| Ministerio de Hacienda — tipos tributos locales | https://serviciostelematicosext.hacienda.gob.es/SGFAL/ConsultaTipos/aspx/descargaPDF.aspx?URLPDF=2026/C.VALENCIANA/Alicante.pdf | Overheid, fiscale statistiek | Open pdf | GEVERIFIEERD EN ACTIEF | ICIO, IBI, IIVTNU per gemeente; geen tasas |
| Sede electrónica Xàbia (transparencia, ordenanzas, trámites) | https://xabia.sedelectronica.es/transparency/9dc46a0e-8b13-4022-824e-000f75336158/ | Gemeente | JavaScript/Wicket; /info.0 redirect-lus | ALLEEN HANDMATIG | Niet omzeild; ordenanzas fiscales en trámites Urbanismo niet gelezen |
| ajxabia.com (nieuws Urbanismo) | https://www.ajxabia.com/ver/7823/el-pleno-aprueba-la-propuesta-definitiva-de-plan-general-estructural-.html/ | Gemeente, persberichten | Open | ALLEEN HANDMATIG | Gedateerde persberichten; urbanismo-pagina verwijst naar de sede |
| Cartoxabia (gemeentelijke GIS) | (geen URL gevonden; genoemd op ajxabia.com/ver/7175, 15-02-2018) | Gemeente, GIS | Onbekend | TECHNISCH ONDERZOEK NODIG | Bestaan en actualiteit onbekend |
| MIVAU Sistema de Información Urbana (SIU) | https://www.mivau.gob.es/urbanismo-y-suelo/sistema-de-informacion-urbana | Rijksoverheid | HTTP 403 voor WebFetch | TECHNISCH ONDERZOEK NODIG | Volgens beschrijving planfiguur en datum per gemeente; niet getest |
| Parques Naturales GVA — Montgó normativa | https://parquesnaturales.gva.es/es/web/pn-el-montgo/legislacion-y-normativa | Overheid | Open | ALLEEN HANDMATIG | Decreten gezien, teksten niet gelezen |
| Pers: xabiaaldia, lamarina.eldiario.es, en.javea.com, alicanteplaza.es | zie bronnenlijst | Secundaire bron | Open | ALLEEN HANDMATIG | Alleen voor data/signalen; nooit voor bouwrecht |
| BP-feed via eigen dienst (lezen) | http://127.0.0.1:3100/api/properties?town=Javea&limit=100 | Eigen dienst (B2B-feed) | Lokaal | GEVERIFIEERD EN ACTIEF | 56 objecten "Javea" op 15-09-2026; gebruikt als testpunten |

---

## 9. Open vragen

1. **C1:** worden de NUT (DOGV 20-09-2021) na ca. 15-03-2025 nog toegepast, of geldt het PGOU 1990/1991 weer volledig in casco en zona E? (Schriftelijk van de gemeente of een advocaat.)
2. Wat is de actuele procedurestatus van het PGE bij de Conselleria (milieubeoordeling, rapporten 2019, eventuele nieuwe versie)? Geen bron van na feb. 2025 gevonden.
3. Past de gemeente 0,20 m²t/m² netto direct toe op kavels in al ontsloten zona E-urbanisaties, of wordt de 29,07 %-cessie per perceel getoetst?
4. Welke grados (E1/E2/E3) gelden in Montgó, Tosalet, Cap Martí en Balcón al Mar volgens plano B.1? Zijn de ocupación-percentages op het Mod. I-blad ongewijzigd?
5. Welke normen en welke stand van urbanisatie/oplevering gelden in PP Ermita II, La Guardia-3, Tosalet 5 en El Rafalet (K07/K08)?
6. Hoe hoog zijn de tasas voor licencia obra mayor, DR, cédula de garantía urbanística en informe urbanístico in Xàbia?
7. Mag een koper zonder eigendom (of met optie/volmacht) een cédula aanvragen ("partes interesadas")?
8. Is Mod. nº 41 (VUT) met licentieschorsing al in de BOP gepubliceerd, en voor welke zones?
9. Welke urbanisaties zijn in 2026 nog niet opgeleverd? De gemeentelijke lijst van 2013 is verouderd.
10. Werkt de gemeente met ECUV's (art. 239.3) en levert dat in de praktijk tijdwinst op?

**⏸️ ACTIE VOOR JAN** (maximaal drie, in volgorde van waarde):
1. Laat een lokale architect of de OAC Urbanismo voor **één concreet perceel** (bijv. K07 Garroferal of een ander topkandidaat) een **informe urbanístico** (art. 246.4) aanvragen, met expliciet de vragen C1 (NUT), het plan parcial/de zone en de urbanisatiestatus. Dat is de lakmoesproef voor de hele checklist.
2. Vraag bij Xàbia Gestió Tributària / Urbanismo de **ordenanzas fiscales** (tasa licencias urbanísticas, ICIO-bonificaties) en de **texto refundido van de normas urbanísticas** als pdf (het portaal is voor ons niet leesbaar).
3. Beslis of de Deal Hunter de **GVA-planningslaag automatisch** mag gebruiken als eerste filter (CC BY 4.0, bronvermelding "Generalitat Valenciana / ICV"), met de vaste waarschuwing dat dit geen bouwrecht is.

---

## 10. Geblokkeerd of mislukt

| Wat | Resultaat | Omzeild? |
|---|---|---|
| `xabia.sedelectronica.es` (transparencia, ordenanzas fiscales/no fiscales, catalogus trámites) | JavaScript/Wicket-links; `/info.0` gaf "Too many redirects"; `/catalog/` 404 | Nee |
| `ajxabia.com/ver/7151/urbanismo.html`, `/ver/1189`, `/ver/7314` | Verwijzen naar hetzelfde JS-portaal | Nee |
| MIVAU SIU (mivau.gob.es) | HTTP 403 | Nee |
| cma.gva.es (PORN Montgó) | DNS-fout (ENOTFOUND) | Nee |
| mediambient.gva.es proceso "normas urbanísticas transitorias Jávea" | HTTP 404 (verouderde link) | Vervangen door DOGV-pdf |
| dadesobertes.gva.es resource-pagina planeamiento | HTTP 404 | Vervangen door datos.gob.es + GetCapabilities |
| DOGV "ficha_disposicion" (Decreto 58/2018) | Inhoud in iframe, niet leesbaar | Nee |
| WFS-attribuutfilter `cod_ine_mun=03082` | HTTP 403 / MapServer-queryfout | Vervangen door bbox |
| xabia.portaldelcomerciante.com (ordenanzas) | HTTP 404 | Nee |
| Scans PGOU (register) | Geen tekstlaag; OCR met ingebouwde macOS Vision; OCR-fouten in tabellen en slechte scans (pdf-p. 34–39, 79–84, 136, 162, 164) → sleutelpagina's visueel gecontroleerd; overige waarden gemarkeerd **[OCR]** | n.v.t. |
| Tasa licencia urbanística Xàbia | Niet gevonden | — |
| Uitspraken TSJCV (feb. 2025 en 15-11-2000) | Nummer/inhoud niet gevonden | — |
| TED-notice 491827-2025 (zoekresultaat "plan general") | Bleek Diputación de Valencia, niet relevant | — |

---

## Bronnenlijst (URL · controledatum · bewijstype)

**Officieel — plannen en registers**
1. DOGV nº 9177, 20-09-2021, Acuerdo de 10-09-2021 del Consell (NUT Jávea), blz. 155–160 — https://dogv.gva.es/datos/2021/09/20/pdf/docv_9177.pdf · 15-09-2026 · 2
2. DOGV nº 9041, 15-03-2021, Acuerdo de 05-03-2021 del Consell (suspensión parcial PGOU Jávea), blz. 750–753 — https://dogv.gva.es/datos/2021/03/15/pdf/docv_9041.pdf · 15-09-2026 · 2
3. DOGV 07-04-2021, Ajuntament de Xàbia, informe ambiental ED Roig Roquetes-1 (planejament vigent) — https://dogv.gva.es/datos/2021/04/07/pdf/2021_3029.pdf · 15-09-2026 · 2
4. Registro Autonómico GVA — map Xàbia (index) — https://mediambient.gva.es/auto/urbanismo/reg-planeamiento/2%20ALICANTE/03082%20X%C0BIA/ · 15-09-2026 · 2
5. Idem — PGOU Ordenanzas (240 blz.) — https://mediambient.gva.es/auto/urbanismo/reg-planeamiento/2%20ALICANTE/03082%20X%C0BIA/1%20P.%20GENERAL/03082-1000%20PLAN%20GENERAL/3%20NORMAS%20URBAN%CDSTICAS/03082-1000%20ORDENANZAS.pdf · 15-09-2026 · 2
6. Idem — PGOU aprobación: 1_CTU.pdf, 2_BOP.pdf (BOP nº 125, 03-06-1991), 3_DOGV.pdf (Decreto 11/2007, DOGV 5438), 4_INF RESOLUCIÓN CTU.pdf — map …/03082-1000%20PLAN%20GENERAL/1%20APROBACI%D3N/ · 15-09-2026 · 2
7. Idem — NUTU Xàbia: Ámbitos_suspensión_licencias.pdf (kaart juli 2019), Clasificación_suelo.pdf (plano A.1 1990), Acuerdo Consell aprobación NUTU — map …/1%20P.%20GENERAL/03082-0000%20NUTU%20X%E0bia/ · 15-09-2026 · 2
8. Idem — Mod. nº XXV (BOP nº 240, 16-12-2016; certificaat pleno 27-10-2016) — map …/03082-1101%20PGMOD%20N%BA%20XXV%20CONDICIONES%20PARCELAS/ · 15-09-2026 · 2
9. Idem — Mod. nº 27 (DOGV nº 4665, 08-01-2004; resolución 01-04-2003; memoria) — map …/03082-1016%20PGMOD%2027%20ORDENANZAS/ · 15-09-2026 · 2
10. Idem — Mod. nº I (DOGV nº 2227, 15-03-1994) — map …/03082-1005%20PGMOD%201/ · 15-09-2026 · 2
11. Idem — Mod. nº XII/"Art. 106" (BOP nº 113, 19-05-2006; NNUU zona F) — map …/03082-1020%20PGMOD%20ART%20106/ · 15-09-2026 · 2
12. Idem — Mod. nº XXXV (BOP nº 9, 15-01-2016) — map …/03082-1100%20PGMOD%20n%BA%20XXXV/ · 15-09-2026 · 2
13. Idem — Mod. nº 71 (inschrijving 12-11-2021; pleno 30-04-2019) — map …/03082-1102%20PGMOD%20n%BA71,%20UE%20AR-5/ · 15-09-2026 · 2
14. Idem — overige goedkeuringsdocumenten Mod. 2, II, III, IV, V, 5, 6, 7, 8, 9, 10, 11, 13, 15, 16, 21, 25, 38, 42, XIV, XV, XVI, XVII, 46, SUNP Cansalades-Lluca (OCR) — map …/1%20P.%20GENERAL/ · 15-09-2026 · 2
15. Idem — Homologación Portitxol (Anulado), sentencia TSJCV 26-04-2012, recurso 201/09 — map …/03082-1001%20HOMOLOGACI%D3N%20PG%20PORTITXOL%20(Anulado)/ · 15-09-2026 · 2
16. Idem — Planeamiento diferido (lijst) — https://mediambient.gva.es/auto/urbanismo/reg-planeamiento/2%20ALICANTE/03082%20X%C0BIA/2%20P.%20DIFERIDO/ · 15-09-2026 · 2
17. GVA — Planeamiento urbanístico vigente (registerpagina) — https://mediambient.gva.es/es/web/urbanismo/registro-autonomico-de-instrumentos-de-planeamiento-urbanistico · 15-09-2026 · 2

**Officieel — geodata**
18. ICV WFS 0702_Planeamiento, GetCapabilities en GetFeature (Clasificacion, Zonificacion) — https://terramapas.icv.gva.es/0702_Planeamiento?service=WFS&request=GetCapabilities · 15-09-2026 · 2 (dienst) / 3 (eigen tests)
19. datos.gob.es — dataset "Planeamiento Urbanístico de la Comunitat Valenciana: Clasificación urbanística" (update 25-08-2026, disclaimer) — https://datos.gob.es/es/catalogo/a10002983-planeamiento-urbanistico-de-la-comunitat-valenciana-clasificacion-urbanistica · 15-09-2026 · 2
20. ICV — definitie velden planeamiento — https://icvficherosweb.icv.gva.es/04/geonetwork/definicion_datos/0702_urbanismo_planeamiento_mdatos.pdf · 15-09-2026 · 2

**Officieel — wetgeving en fiscaliteit**
21. BOE — Decreto Legislativo 1/2021 (TRLOTUP), geconsolideerd, update 02-07-2026 (art. 44, 68–70, 168, 186–188, 206, 210–216, 226, 232–249) — https://www.boe.es/buscar/act.php?id=DOGV-r-2021-90283 en https://www.boe.es/buscar/pdf/2021/DOGV-r-2021-90283-consolidado.pdf · 15-09-2026 · 2
22. Ministerio de Hacienda SGFAL — Tipos tributos locales Alicante 2026 (ICIO 4,00; IBI 0,83; IIVTNU 30) — https://serviciostelematicosext.hacienda.gob.es/SGFAL/ConsultaTipos/aspx/descargaPDF.aspx?URLPDF=2026/C.VALENCIANA/Alicante.pdf · 15-09-2026 · 2
23. Idem 2025 (ICIO 4,00) — https://serviciostelematicosext.hacienda.gob.es/SGFAL/ConsultaTipos/aspx/descargaPDF.aspx?URLPDF=2025/C.VALENCIANA/Alicante.pdf · 15-09-2026 · 2
24. Parques Naturales GVA — PN El Montgó, legislación — https://parquesnaturales.gva.es/es/web/pn-el-montgo/legislacion-y-normativa · 15-09-2026 · 2
25. BOP Alicante — consultas — https://sede.diputacionalicante.es/consultas-bop/ · 15-09-2026 · 2 (alleen zoekvorm)

**Gemeente Xàbia (ajxabia.com)**
26. "El pleno aprueba la propuesta definitiva de Plan General Estructural" (30-04-2019) — https://www.ajxabia.com/ver/7823/el-pleno-aprueba-la-propuesta-definitiva-de-plan-general-estructural-.html/ · 15-09-2026 · 2
27. "El Ayuntamiento de Xàbia aprueba someter a exposición pública la versión preliminar del PGE" (01-06-2017) — https://www.ajxabia.com/ver/6807/el-ayuntamiento-de-xabia-aprueba-someter-a-exposicion-publica-la-version-preliminar-del-plan-general-estructural.html/ · 15-09-2026 · 2
28. "La versión preliminar del Plan General de Xàbia protege otros 201.220 metros cuadrados" (24-01-2019) — https://www.ajxabia.com/ver/7741/la-version-preliminar-del-plan-general-de-xabia-protege-otros-201-220-metros-cuadrados-tras-estudiar-informes-y-alegaciones--.html/ · 15-09-2026 · 2
29. "Urbanismo hace pública la nueva cartografía municipal" (15-02-2018) — https://www.ajxabia.com/ver/7175/urbanismo-hace-publica-la-nueva-cartografia-municipal-de-xabia-en-la-web-del-ayuntamiento.html · 15-09-2026 · 2
30. "El Ayuntamiento de Xàbia recepciona la urbanización Las Laderas" (22-02-2013) — https://www.ajxabia.com/ver/4540/el-ayuntamiento-de-xabia-recepciona-la-urbanizacion-las-laderas.html/ · 15-09-2026 · 2
31. Ordenanzas fiscales / no fiscales (verwijzing naar sede) — https://www.ajxabia.com/ver/1189/ordenanzas-fiscales.html ; https://www.ajxabia.com/ver/7314/ordenanzas-no-fiscales-y-reglamentos.html · 15-09-2026 · 2 (alleen verwijzing)
32. Sede electrónica, portal de transparencia (ordenanzas fiscales) — https://xabia.sedelectronica.es/transparency/9dc46a0e-8b13-4022-824e-000f75336158/ · 15-09-2026 · 7 (niet leesbaar)

**Pers (secundair, met datum)**
33. lamarina.eldiario.es, "La Generalitat advierte a Xàbia de posibles responsabilidades legales…" (17-02-2025) — https://lamarina.eldiario.es/2025/02/17/generalitat-advierte-xabia-responsabilidad-licencias-plan-general-no-aprobado/ · 15-09-2026 · 1
34. xabiaaldia, "La Generalitat advierte a Xàbia de que no puede denegar licencias basándose en un PGOU no aprobado" (18-02-2025) — https://xabiaaldia.com/art/156998/la-generalitat-advierte-a-xabia-de-que-no-puede-denegar-licencias-basandose-en-un-pgou-no-aprobado · 15-09-2026 · 1
35. en.javea.com, "Urban planning debate in Xàbia: Generalitat and TSJ…" (19-02-2025) — https://en.javea.com/debate-urbanistico-en-xabia-generalitat-y-tsj-marcan-posturas-ante-la-otorgacion-de-licencias/ · 15-09-2026 · 1
36. xabiaaldia, "El Consell exige a Xàbia cinco nuevos informes sectoriales…" (18-12-2019) — https://xabiaaldia.com/archive/113095/el-consell-exige-a-xabia-cinco-nuevos-informes-sectoriales-para-aprobar-el-nuevo-plan-general-estructural · 15-09-2026 · 1
37. xabiaaldia, "El Consell acuerda la suspensión parcial del PGOU de Xàbia…" (05-03-2021) — https://xabiaaldia.com/art/127062/el-consell-acuerda-la-suspension-parcial-del-pgou-de-xabia-y-el-inicio-del-procedimiento-de-aprobacion-de-las-normas-transitorias-de-urgencia · 15-09-2026 · 1
38. xabiaaldia, "El Diari Oficial de la Generalitat publica las Normas Urbanísticas Transitorias de Xàbia" (22-09-2021) — https://xabiaaldia.com/art/133952/el-diari-oficial-de-la-generalitat-publica-las-normas-urbanisticas-transitorias-de-xabia · 15-09-2026 · 1
39. Alicante Plaza, "Xàbia planea contratar a más personal en Urbanismo para acabar con las demoras de un año en licencias de obras" (27-11-2023) — https://alicanteplaza.es/alicanteplaza/xabia-planea-contratar-a-mas-personal-en-urbanismo-para-acabar-con-las-demoras-de-un-ano-en-licencias-de-obras · 15-09-2026 · 1
40. en.javea.com, "Xàbia approves regulations for tourist accommodations…" (06-06-2026) — https://en.javea.com/xabia-aprueba-la-regulacion-de-las-viviendas-turisticas-limite-por-barrios-y-suspension-de-nuevas-licencias/ · 15-09-2026 · 1
41. lamarina.eldiario.es, "Xàbia permitirá al menos 360 viviendas turísticas más…" (29-05-2026) — https://lamarina.eldiario.es/2026/05/29/xabia-permitira-al-menos-360-viviendas-turisticas-mas-con-los-votos-favorables-del-gobierno-local-y-compromis/ · 15-09-2026 · 1
42. lamarina.eldiario.es, opinie "Xàbia: La urgencia de un urbanismo transparente y actualizado" (20-06-2025) — https://lamarina.eldiario.es/2025/06/20/xabia-la-urgencia-de-un-urbanismo-transparente-y-actualizado/ · 15-09-2026 · 1 (opinie)
43. en.javea.com, "Xàbia approves the General Structural Plan for the next 20 years" (30-04-2019) — https://en.javea.com/xabia-aprueba-el-plan-general-estructural-para-los-proximos-20-anos/ · 15-09-2026 · 1
44. en.javea.com, "The new General Structural Plan reduces urban expansion" (08-06-2017) — https://en.javea.com/nuevo-plan-general-estructural-reduce-la-expansion-urbanistica/ · 15-09-2026 · 1
45. Alicante Plaza, "El Consell aprueba las normas urbanísticas transitorias de urgencia de Xàbia" (10-09-2021) — https://alicanteplaza.es/alicanteplaza/el-consell-aprueba-las-normas-urbanisticas-transitorias-de-urgencia-de-xabia · 15-09-2026 · 1

**Intern (eerder vastgesteld)**
46. R07-verificatie (licentiecijfers 2022) — /Users/root-admin/tree-es/deal-hunter/onderzoek/R07-netwerken-ontwikkelaars-dealflow.verificatie.md · 14-09-2026 · 2/1
47. R11 (Catastro-coördinaten K07/K08) — /Users/root-admin/tree-es/deal-hunter/onderzoek/R11-catastro-registro-perceelidentificatie.md · 14-09-2026 · 3
48. R14 (ICIO-grondslag TRLRHL art. 102) — /Users/root-admin/tree-es/deal-hunter/onderzoek/R14-financieel-fiscaal-kostenkengetallen.md · 14-09-2026 · 2
49. R15 (kandidaten K07, K08, K14 met advertentiecitaten) — /Users/root-admin/tree-es/deal-hunter/onderzoek/R15-kandidaten-javea-live.md · 14-09-2026 · 1
50. Eigen dienst BP-feed (alleen lezen) — http://127.0.0.1:3100/api/properties?town=Javea&limit=100 · 15-09-2026 · 3 (feed) / 1 (advertentieteksten)

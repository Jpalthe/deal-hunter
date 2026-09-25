# H01 — Vergelijkingsprijzen Puerto en El Arenal (Jávea): vraagprijs per m² gebouwd

**Zone-sleutel:** `puerto_arenal` · **Bron:** officiële Idealista-assistent (MCP `search_properties` + `property_detail`, locale es-ES, country es, maxResults 50) · **Peildatum:** 15-09-2026 (verse zoekronde 10:41–11:05 uur; vervangt de versie van 09:39 van dezelfde dag, zie §10) · **Bewijstype:** 2 (portaaldata via officiële tool); classificatie en controle door de agent.

> **Alle bedragen zijn VRAAGPRIJZEN** (advertenties), geen transactieprijzen. €/m² = vraagprijs / m² gebouwd zoals de tool die geeft (afgerond op hele euro's). Niets hieronder is een taxatie. Kandidaat K06 (106514871) is op 15-09-2026 met `property_detail` bevestigd: actief, 345.000 € / 125 m² gebouwd = 2.760 €/m², staat "Segunda mano/para reformar", particuliere verkoper (naam en straat bewust niet overgenomen).

## 1. Conclusie in één oogopslag

| Reeks | n | min | p25 | mediaan | p75 | max |
|---|---|---|---|---|---|---|
| villa_renovated — villa’s gerenoveerd/modern, Puerto + El Arenal | 12 | 3.270 | 4.295 | 6.253 | 7.302 | 11.458 |
|   · waarvan Puerto | 9 | 3.270 | 5.749 | 6.759 | 7.401 | 11.458 |
|   · waarvan El Arenal | 3 | 4.250 | 4.280 | 4.310 | 4.559 | 4.808 |
| villa_new — nieuwbouwvilla’s in aanbouw, Puerto + El Arenal | 2 | 6.810 | 7.564 | 8.318 | 9.072 | 9.826 |
|   · waarvan Puerto (La Corona) | 2 | 6.810 | 7.564 | 8.318 | 9.072 | 9.826 |
|   · waarvan El Arenal | 0 | – | – | – | – | – |
| apartment_renovated — appartementen gerenoveerd (tekst bevestigd), Puerto + El Arenal | 45 | 2.633 | 3.580 | 4.235 | 5.064 | 9.725 |
|   · waarvan Puerto (relevant voor K06) | 10 | 3.778 | 4.400 | 5.024 | 5.468 | 9.725 |
|   · waarvan El Arenal | 35 | 2.633 | 3.401 | 4.174 | 4.988 | 6.611 |
| apartment_new — nieuwbouw / a estrenar / gebouwd 2023–2026, Puerto + El Arenal | 43 | 1.630 | 3.412 | 3.944 | 5.528 | 8.380 |
|   · waarvan Puerto | 1 | 5.500 | 5.500 | 5.500 | 5.500 | 5.500 |
|   · waarvan El Arenal | 42 | 1.630 | 3.390 | 3.876 | 5.528 | 8.380 |

Gevoeligheden (zelfde data, andere afbakening):

| Reeks | n | min | p25 | mediaan | p75 | max |
|---|---|---|---|---|---|---|
| villa_renovated zonder 111071067 (1983, alleen keuken/elektra vernieuwd) en 108111394 (gebouwd 2020) | 10 | 3.788 | 4.434 | 6.253 | 7.142 | 9.494 |
| villa_renovated Puerto zonder 108111394 | 8 | 3.270 | 5.259 | 6.758 | 7.302 | 9.494 |
| apartment_renovated Puerto zonder 112431449 (40 m², m² twijfelachtig) | 9 | 3.778 | 4.286 | 4.862 | 5.320 | 5.557 |
| apartment_renovated Puerto, alleen 80–150 m² (grootteklasse K06) | 4 | 3.778 | 4.159 | 4.515 | 4.774 | 4.862 |
| apartment_renovated Puerto + Arenal, alleen 80–150 m² | 23 | 2.633 | 3.232 | 3.778 | 4.463 | 6.611 |
| apartment_new zonder 110963269 (tuin-unit) en zonder units > 190 m² | 36 | 2.977 | 3.581 | 4.602 | 5.666 | 8.380 |
| apartment_new alleen units ≤ 120 m² (zonder 110963269) | 18 | 3.250 | 4.770 | 5.570 | 7.032 | 8.380 |

Context (breder dan gerenoveerd; alleen als ondergrens "bewoonbaar"):

| Reeks | n | min | p25 | mediaan | p75 | max |
|---|---|---|---|---|---|---|
| villa_buen_estado_all — vrijstaande villa’s "buen estado" zonder reformar-/nieuwbouwsignaal | 40 | 2.500 | 4.302 | 5.238 | 6.799 | 11.458 |
|   · Puerto | 34 | 2.500 | 4.822 | 5.288 | 7.116 | 11.458 |
|   · El Arenal | 6 | 3.249 | 4.053 | 4.280 | 4.684 | 5.208 |
| apartment_buen_estado_all — appartementen "buen estado" zonder reformar-/nieuwbouwsignaal | 156 | 1.399 | 3.454 | 4.342 | 5.137 | 15.000 |
|   · Puerto | 36 | 1.399 | 3.202 | 4.873 | 5.745 | 9.725 |
|   · El Arenal | 120 | 2.357 | 3.456 | 4.233 | 4.988 | 15.000 |
| villa_new_javea_ref — nieuwbouwvilla’s heel Jávea (NIET Puerto/Arenal; alleen referentie) | 43 | 2.829 | 3.996 | 4.316 | 6.254 | 10.263 |

**Wat dit zegt voor Jan (kort):**

- **K06 (Puerto, casco, 2.760 €/m² vraagprijs).** Gerenoveerde appartementen in Puerto vragen mediaan **5.024 €/m²** (n=10, kwartielen 4.400–5.468). Maar let op de grootte: de Puerto-comparables zijn bijna allemaal 29–90 m²; in de grootteklasse van K06 (80–150 m²) zijn er maar 4 (mediaan 4.515 €/m², spreiding 3.778–4.862). Over beide zones samen halen gerenoveerde appartementen van 80–150 m² mediaan **3.778 €/m²** (n=23). Voor het rekenmodel van K06 is daarom 3.800–4.900 €/m² vraagprijs na renovatie de voorzichtige band (afgeleid uit de 80–150 m²-reeks Puerto, 3.778–4.862); 5.000+ komt in Puerto alleen voor bij units ≤ 75 m², en in El Arenal bij units ≤ 80 m², bij eerste lijn (110614251) en bij één ático dúplex van 123 m² (107191794). Geen transactiebewijs.
- **Nieuwbouwappartementen** bestaan in Puerto nauwelijks (n=1: 110983899, gebouwd 2026, 5.500 €/m²); in El Arenal zijn het promoties (Arenal Jávea Beach / Avenida de París 2, Adeya Jávea / Calle Cannes 3, Marina Bay Sunset / Calle Bruselas 102, Estrasburgo 5, Montañar Beach / Atenas 41) met een enorme spreiding: 6.000–8.400 €/m² voor kleine units bij het strand tegenover 2.350–3.000 €/m² voor units van 175–314 m² gebouwd. Beperkt tot ≤ 120 m²: mediaan 5.570 €/m² (n=18).
- **Villa's gerenoveerd/modern**: Puerto (La Corona, Cuesta de San Antonio) mediaan **6.759 €/m²** (n=9, spreiding 3.270–11.458); El Arenal maar n=3 (4.250–4.808 €/m²). Het zijn luxeobjecten (0,6–3,4 M€).
- **Nieuwbouwvilla's**: in de zone alleen twee villa's in aanbouw in La Corona (Puerto), beide 3.950.000 €: Villa Imperio (111823302, 580 m², 6.810 €/m², "Construido en 2027") en Villa Azure (110755799, 402 m², 9.826 €/m², oplevering Q4 2027). In El Arenal: 0. Dat zijn prijzen op plan, geen opgeleverde woningen. De Jávea-brede referentie (Tosalet, Portichol, Pinosol, Sol de Este) ligt op mediaan 4.316 €/m² (n=43) — andere markt, alleen ter oriëntatie.

## 2. Werkwijze

1. **Zoekopdrachten** (23 stuks, letterlijk in §9) via de Idealista-assistent. De tool kent geen filter "reformado": zij vertaalt dat naar de staat *Usada/buen estado*, en "a estrenar/obra nueva" naar *Obra nueva*. "Puerto y Arenal" in één zoekopdracht levert óf een "zona personalizada" met 0 resultaten óf alleen Puerto op; daarom zijn beide Idealista-zones apart bevraagd. Reeksen groter dan 50 zijn opgesplitst op prijsband tot elke band ≤ 50 gaf (Puerto casas y chalets 61 = 25 + 37; Puerto pisos 58 = 34 + 24; El Arenal pisos 160 = 30 + 41 + 46 + 44 met randoverlap op de bandgrenzen; Puerto casas y chalets álle staten 70 = 30 + 40). Ook zonder staatfilter gezocht (§9 nr. 20–23) omdat nieuwbouwvilla's in aanbouw bij Idealista soms als "segunda mano" of zelfs "para reformar" staan (111823302).
2. **Samenvoegen**: 388 unieke advertenties (incl. 46 Jávea-brede nieuwbouwvilla's als referentie en enkele "a reformar"-objecten uit de zoekopdrachten zonder staatfilter). **Ontdubbelen**: zelfde vraagprijs + zelfde m² gebouwd + zelfde zone = één object; representant is de advertentie waarop de classificatie steunt (anders de laagste code), de overige codes staan als "dubbels" in de tabellen. Twee advertenties van hetzelfde object met afwijkende m² (Villa Imperio 580 vs 700 m²) zijn handmatig samengevoegd.
3. **Classificatie op advertentietekst** (genormaliseerd, zonder accenten):
   - *gerenoveerd*: expliciet `reformad-`, `renovad-`, `rehabilitad-`, `reconstruid-`, `modernizad-`, `actualizad-` of `reforma/renovación integral/completa/total` op het hele object; bij villa's ook `villa moderna`, `villa de diseño`, `arquitectura/diseño contemporáneo` (modern ontwerp). Losse formuleringen ('cocina moderna', 'comodidades modernas', 'exterior renovado' van de gemeenschap) tellen niet.
   - *uitgesloten uit gerenoveerd*: staat "a reformar" (Idealista-status `renew`), `para/a reformar`, `necesita/requiere reforma`, `para actualizar`, `posibilidad(es) de actualización/reforma`, `sin reformar`, `para terminar`; en gedeeltelijke renovaties (alleen bad of keuken, `semi reformado`, `parcialmente`, `exceptuando la cocina`) — 13 appartementen daardoor buiten de reeks gelaten (lijst in §5).
   - *nieuw*: Idealista-status `newdevelopment` (promotie), of in de tekst/kenmerken `a estrenar`, `obra nueva`, `nueva construcción`, `construido en 2023–2027`. Drie "a estrenar"-advertenties bleken volledig gerenoveerde tweedehandswoningen ("todo nuevo a estrenar", "reformado a estrenar") en staan in *gerenoveerd* (111399396, 111463998, 110388818).
4. **Controle met `property_detail`** op 40 objecten, gemarkeerd met (D): bouwjaar, staat, tekst, oppervlakten. Gevolgen: **109649453/111002156** (Finca Mezquida, 1980, "mantiene su estructura original", ontwikkelpotentieel) is níet gerenoveerd en geschrapt; **111343157** (Calle Penáguila, 3.950.000 €, bioscoop/gym/wellness/lift, "ha sido proyectada", label A) is hetzelfde nieuwbouwproject als Villa Imperio **111823302** (Penáguila 45, 3.950.000 €, "Construido en 2027", structuur klaar) en verhuist naar *villa_new*; **110755799** Villa Azure (promotie, in aanbouw, oplevering Q4 2027) toegevoegd aan *villa_new*; **106665192** (2.735 €/m², "villa de estilo moderno") is een perceel met project en geschrapt; **109709911** zit "en la fase final de una reforma integral" (opgenomen, met kanttekening); **110983899** staat als "segunda mano" maar is gebouwd in 2026 → *apartment_new* Puerto; **109870004** noemt in de tekst 40 m² maar in de kenmerken 82 m² (kenmerken gebruikt).
5. **Statistiek**: n, min, p25, mediaan, p75, max van vraagprijs / m² gebouwd; percentielen lineair geïnterpoleerd. Villa's zonder m² zouden zijn overgeslagen (kwam niet voor).

## 3. Reeks villa_renovated — villa's gerenoveerd of modern (Puerto + El Arenal)

| Reeks | n | min | p25 | mediaan | p75 | max |
|---|---|---|---|---|---|---|
| villa_renovated | 12 | 3.270 | 4.295 | 6.253 | 7.302 | 11.458 |
|   · Puerto | 9 | 3.270 | 5.749 | 6.759 | 7.401 | 11.458 |
|   · El Arenal | 3 | 4.250 | 4.280 | 4.310 | 4.559 | 4.808 |
|   · zonder 111071067 en 108111394 | 10 | 3.788 | 4.434 | 6.253 | 7.142 | 9.494 |

Voorbeelden (8, alle met `property_detail` gecontroleerd):

| Code | Zone | Vraagprijs € | m² | €/m² | Bouwjaar / renovatie | Label | URL |
|---|---|---|---|---|---|---|---|
| 111998394 | Puerto | 1.125.000 | 152 | 7.401 | 1996 | magníficamente renovada, bouwjaar 1996, gelijkvloers, 842 m² perceel (D); 4 dubbele advertenties | https://www.idealista.com/es/inmueble/111998394/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 111807268 | Puerto | 1.890.000 | 260 | 7.269 | reconstruida | totalmente renovada / reconstruida a partir de la estructura original, 874 m² perceel, noemt zichzelf Balcón al Mar (D) | https://www.idealista.com/es/inmueble/111807268/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 111286574 | Puerto | 3.400.000 | 503 | 6.759 | 1983 | cuidadosamente renovada, bouwjaar 1983, Cuesta de San Antonio, 1.618 m² perceel, hoofdhuis + gastenhuis (D) | https://www.idealista.com/es/inmueble/111286574/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 109709911 | Puerto | 3.300.000 | 574 | 5.749 | reforma in eindfase | reforma integral in eindfase — nog niet klaar, La Corona, infinity pool (D) | https://www.idealista.com/es/inmueble/109709911/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 111720790 | Puerto | 625.000 | 165 | 3.788 | ref. 2023 | villa reformada, reforma integral 2023, 1.000 m² perceel, kleinste villa in de reeks (D) | https://www.idealista.com/es/inmueble/111720790/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 108332489 | El Arenal | 1.190.000 | 280 | 4.250 | n.v. | renovación completa, Montañar II / Cala Blanca, 100 m van zee; perceel in unidad de ejecución volgens tekst [te verifiëren] (D) | https://www.idealista.com/es/inmueble/108332489/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 112265864 | El Arenal | 1.250.000 | 260 | 4.808 | ref. 2018 | completamente reformado en 2018, energielabel C, Cap de la Nau, 1.700 m² perceel (D); 5 dubbele advertenties | https://www.idealista.com/es/inmueble/112265864/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 108111394 | Puerto | 2.750.000 | 240 | 11.458 | 2020 | gebouwd 2020, villa contemporánea, binnenzwembad, lift, 1.645 m² perceel — modern, niet gerenoveerd (D) | https://www.idealista.com/es/inmueble/108111394/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |

Volledige reeks:

| Code | Zone | Vraagprijs € | m² | €/m² | (D) | Dubbels (zelfde prijs+m²+zone) | Titel (Idealista) |
|---|---|---|---|---|---|---|---|
| 111071067 | Puerto | 2.600.000 | 795 | 3.270 | D | 110604173 | Casa o chalet independiente en Puerto, Jávea/Xàbia |
| 111720790 | Puerto | 625.000 | 165 | 3.788 | D | – | Casa o chalet independiente en Puerto, Jávea/Xàbia |
| 108332489 | El Arenal | 1.190.000 | 280 | 4.250 | D | – | Casa o chalet independiente en Calle Esparta, El Arenal, Jávea/Xàbia |
| 112209448 | El Arenal | 1.250.000 | 290 | 4.310 | D | – | Casa o chalet independiente en El Arenal, Jávea/Xàbia |
| 112265864 | El Arenal | 1.250.000 | 260 | 4.808 | D | 111543783, 111576828, 111777540, 111676743, 112225050 | Casa o chalet independiente en Carretera del Cap de la Nau Pla, El Arenal, Jávea/Xàbia |
| 109709911 | Puerto | 3.300.000 | 574 | 5.749 | D | – | Casa o chalet independiente en Puerto, Jávea/Xàbia |
| 109843783 | Puerto | 3.250.000 | 481 | 6.757 | D | – | Casa o chalet independiente en Puerto, Jávea/Xàbia |
| 111286574 | Puerto | 3.400.000 | 503 | 6.759 | D | – | Casa o chalet independiente en Cuesta de San Antonio, Puerto, Jávea/Xàbia |
| 111807268 | Puerto | 1.890.000 | 260 | 7.269 | D | – | Casa o chalet en Calle Penáguila, Puerto, Jávea/Xàbia |
| 111998394 | Puerto | 1.125.000 | 152 | 7.401 | D | 112281618, 112526422, 112413770, 112505992 | Casa o chalet independiente en Puerto, Jávea/Xàbia |
| 105665335 | Puerto | 3.000.000 | 316 | 9.494 | D | – | Casa o chalet independiente en Puerto, Jávea/Xàbia |
| 108111394 | Puerto | 2.750.000 | 240 | 11.458 | D | – | Casa o chalet independiente en Calle Petrer, Puerto, Jávea/Xàbia |

Kanttekeningen bij deze reeks: 'Puerto' is bij Idealista een brede zone; de villa's liggen op de hellingen (La Corona, Cuesta de San Antonio, Calle Petrer) met zeezicht, niet aan de haven zelf. 111071067 (795 m², 1983) noemt zichzelf "villa moderna" maar noemt alleen de keuken ("hace 1,5 años") en de elektra als vernieuwd — vandaar de gevoeligheidsregel. De €/m² daalt bij zeer grote villa's (795 m² → 3.270) en stijgt bij kleine, volledig vernieuwde villa's (152 m² → 7.401).

## 4. Reeks villa_new — nieuwbouwvilla's (Puerto + El Arenal)

**n = 2, beide in La Corona (Puerto), beide in aanbouw; El Arenal n = 0.** Met het filter *Obra nueva* (villa/chalet) gaven zowel Puerto als El Arenal 0 resultaten (§9 nr. 3, 4, 18); de twee objecten kwamen alleen naar boven via de zoekopdrachten zónder staatfilter, omdat Idealista ze als "casa o chalet" (niet als "villa") en in één geval als "segunda mano/para reformar" heeft staan.

| Reeks | n | min | p25 | mediaan | p75 | max |
|---|---|---|---|---|---|---|
| villa_new (Puerto) | 2 | 6.810 | 7.564 | 8.318 | 9.072 | 9.826 |

| Code | Zone | Vraagprijs € | m² | €/m² | Bouwjaar / renovatie | Label | URL |
|---|---|---|---|---|---|---|---|
| 111823302 | Puerto | 3.950.000 | 580 | 6.810 | 2027 (in aanbouw) | Villa Imperio, Calle Penáguila 45 — nueva construcción, "Construido en 2027", structuur klaar, 455 m² nuttig, 1.487 m² perceel, lift, binnenzwembad; Idealista-staat ten onrechte "para reformar" (D). Zelfde project als 111343157 (700 m² gebouwd → 5.643 €/m²) | https://www.idealista.com/es/inmueble/111823302/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 110755799 | Puerto | 3.950.000 | 402 | 9.826 | oplevering Q4 2027 (in aanbouw) | Villa Azure, Calle La Sella 42 — promotie obra nueva, in aanbouw, oplevering laatste kwartaal 2027, 316 m² nuttig, 935 m² perceel, lift (D) | https://www.idealista.com/es/obra-nueva/110755799/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |

Beide zijn prijzen op plan (promotionType notFinished / in ejecución), niet van opgeleverde woningen. Ter referentie buiten de zone (zoekopdracht "villa obra nueva a estrenar en Jávea/Xàbia", 46 advertenties, 43 objecten na ontdubbelen): mediaan 4.316 €/m², kwartielen 3.996–6.254, spreiding 2.829–10.263. Dichtst bij Arenal volgens de Idealista-zonelabels: Portichol–Balcón al Mar 107915996 (2.145.000 € / 209 m² = 10.263 €/m²), 110783694 (3.200.000 € / 400 m² = 8.000), 111326512 (1.450.000 € / 205 m² = 7.073); El Tosalet–Cap Martí 110763829 (1.800.000 € / 219 m² = 8.219), 110824450 (1.600.000 € / 300 m² = 5.333), 108645413 (2.050.000 € / 475 m² = 4.316); Pinomar–Pinosol 112515850 (1.950.000 € / 200 m² = 9.750); Sol de Este 111946911 (1.195.000 € / 300 m² = 3.983). URL-patroon: https://www.idealista.com/es/inmueble/<code>/ met dezelfde utm-parameters als in de tabellen.

## 5. Reeks apartment_renovated — appartementen gerenoveerd (Puerto + El Arenal)

| Reeks | n | min | p25 | mediaan | p75 | max |
|---|---|---|---|---|---|---|
| apartment_renovated | 45 | 2.633 | 3.580 | 4.235 | 5.064 | 9.725 |
|   · Puerto (relevant voor K06) | 10 | 3.778 | 4.400 | 5.024 | 5.468 | 9.725 |
|   · El Arenal | 35 | 2.633 | 3.401 | 4.174 | 4.988 | 6.611 |
|   · Puerto zonder 112431449 | 9 | 3.778 | 4.286 | 4.862 | 5.320 | 5.557 |
|   · Puerto, alleen 80–150 m² | 4 | 3.778 | 4.159 | 4.515 | 4.774 | 4.862 |
|   · Puerto + Arenal, alleen 80–150 m² | 23 | 2.633 | 3.232 | 3.778 | 4.463 | 6.611 |

Voorbeelden Puerto (8 — relevant voor K06; alle (D)):

| Code | Zone | Vraagprijs € | m² | €/m² | Bouwjaar / renovatie | Label | URL |
|---|---|---|---|---|---|---|---|
| 109870004 | Puerto | 389.000 | 82 | 4.744 | 1960 | completamente reformado, bouwjaar 1960, Calle Churruca, dakterras met zeezicht, zonder lift; tekst noemt 40 m², kenmerken 82 m² (D) | https://www.idealista.com/es/inmueble/109870004/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 108883032 | Puerto | 389.000 | 70 | 5.557 | n.v. | recientemente reformado, Playa La Grava, terras met zeezicht, zonder lift (D) | https://www.idealista.com/es/inmueble/108883032/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 110279888 | Puerto | 389.000 | 80 | 4.862 | n.v. | perfectamente renovado "estilo Ibiza", 80 m² gebouwd / 70 nuttig, zonder lift (D) | https://www.idealista.com/es/inmueble/110279888/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 108819856 | Puerto | 399.000 | 75 | 5.320 | 1960 / ref. 2025 | reformada completamente en 2025, bouwjaar 1960, dúplex Churruca, 75 m² gebouwd / 60 nuttig (D) | https://www.idealista.com/es/inmueble/108819856/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 111071237 | Puerto | 630.000 | 147 | 4.286 | 1980 / ref. 2023 | ático recién reformado en 2023, bouwjaar 1980, 147 m², lift, garage — grootste Puerto-comparable (D) | https://www.idealista.com/es/inmueble/111071237/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 108265680 | Puerto | 340.000 | 90 | 3.778 | 1990 | completamente renovado, bouwjaar 1990, 90 m², lift, garage, 140 m van strand (D); dubbel 111665579 | https://www.idealista.com/es/inmueble/108265680/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 108146741 | Puerto | 270.000 | 71 | 3.803 | 1988 | residencial 1988, "ha sido reformado", 1 slaapkamer, 71 m² gebouwd / 61 nuttig, zwembaden (D) | https://www.idealista.com/es/inmueble/108146741/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 112431449 | Puerto | 389.000 | 40 | 9.725 | n.v. | meticulosamente renovada; 40 m² gebouwd voor 2 slk / 2 bad op twee verdiepingen — m² twijfelachtig, €/m² niet bruikbaar (D) | https://www.idealista.com/es/inmueble/112431449/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |

Voorbeelden El Arenal (6; alle (D)):

| Code | Zone | Vraagprijs € | m² | €/m² | Bouwjaar / renovatie | Label | URL |
|---|---|---|---|---|---|---|---|
| 110614251 | El Arenal | 595.000 | 90 | 6.611 | 1982 | completamente reformada, bouwjaar 1982, eerste lijn Montañar II (Avenida de Ultramar), domotica (D); 2 dubbels | https://www.idealista.com/es/inmueble/110614251/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 111444238 | El Arenal | 430.000 | 70 | 6.143 | 1983 | totalmente reformado, bouwjaar 1983, 100 m van Arenal-strand, lift, parkeerplaats (D) | https://www.idealista.com/es/inmueble/111444238/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 112011823 | El Arenal | 295.000 | 109 | 2.706 | n.v. | completamente reformado, Montañar II, 3 slk / 1 bad, zonder lift — laagste €/m² op één na (D) | https://www.idealista.com/es/inmueble/112011823/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 107191794 | El Arenal | 695.000 | 123 | 5.650 | 2006 | ático dúplex bellamente reformado, bouwjaar 2006, Calle Cannes, garage 35 m² (D) | https://www.idealista.com/es/inmueble/107191794/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 111364826 | El Arenal | 360.000 | 85 | 4.235 | 1967 / ref. 2026 | reforma integral 2026 (leidingen, elektra, keuken), bouwjaar 1967, 30 m van het strand, gevel van het complex ook vernieuwd (D) | https://www.idealista.com/es/inmueble/111364826/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 112384680 | El Arenal | 720.000 | 179 | 4.022 | 2002 / ref. | reformada integralmente, bouwjaar 2002, Residencial Nou Fontana, 179 m² — groot, lage €/m² (D) | https://www.idealista.com/es/inmueble/112384680/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |

Volledige reeks:

| Code | Zone | Vraagprijs € | m² | €/m² | (D) | Dubbels (zelfde prijs+m²+zone) | Titel (Idealista) |
|---|---|---|---|---|---|---|---|
| 112219701 | El Arenal | 395.000 | 150 | 2.633 |  | – | Piso en Urbanización la Isla, 1 a, El Arenal, Jávea/Xàbia |
| 112011823 | El Arenal | 295.000 | 109 | 2.706 | D | – | Piso en El Arenal, Jávea/Xàbia |
| 110220894 | El Arenal | 320.000 | 114 | 2.807 |  | – | Piso en El Arenal, Jávea/Xàbia |
| 110002487 | El Arenal | 320.000 | 110 | 2.909 |  | – | Piso en Calle Saint Tropez, El Arenal, Jávea/Xàbia |
| 102716034 | El Arenal | 415.000 | 135 | 3.074 |  | – | Piso en Carretera del Cap de la Nau Pla, El Arenal, Jávea/Xàbia |
| 112231070 | El Arenal | 385.000 | 123 | 3.130 |  | – | Piso en Carretera del Cap de la Nau Pla, El Arenal, Jávea/Xàbia |
| 40525993 | El Arenal | 214.000 | 66 | 3.242 |  | – | Piso en Calle Tropez, 4, El Arenal, Jávea/Xàbia |
| 111541292 | El Arenal | 300.000 | 90 | 3.333 |  | – | Piso en El Arenal, Jávea/Xàbia |
| 111955042 | El Arenal | 299.000 | 89 | 3.360 |  | – | Piso en Calle Niza, 10, El Arenal, Jávea/Xàbia |
| 109124963 | El Arenal | 265.000 | 77 | 3.442 |  | 110911443 | Piso en Avenida de Paris, El Arenal, Jávea/Xàbia |
| 111582637 | El Arenal | 325.000 | 94 | 3.457 |  | 112212044 | Piso en Calle Tesalónica, El Arenal, Jávea/Xàbia |
| 112382674 | El Arenal | 315.000 | 88 | 3.580 |  | – | Piso en El Arenal, Jávea/Xàbia |
| 111392054 | El Arenal | 275.000 | 76 | 3.618 |  | – | Piso en Avenida de Paris, El Arenal, Jávea/Xàbia |
| 110557697 | El Arenal | 480.000 | 132 | 3.636 |  | 112514439, 110293603, 112381941, 112369399 | Piso en Calle Larissa, El Arenal, Jávea/Xàbia |
| 110388818 | El Arenal | 225.000 | 60 | 3.750 |  | 110418334 | Piso en El Arenal, Jávea/Xàbia |
| 108265680 | Puerto | 340.000 | 90 | 3.778 | D | 111665579 | Piso en Calle Doctor Fleming, Puerto, Jávea/Xàbia |
| 108146741 | Puerto | 270.000 | 71 | 3.803 | D | – | Piso en Avenida dels Furs, Puerto, Jávea/Xàbia |
| 112384680 | El Arenal | 720.000 | 179 | 4.022 | D | – | Dúplex en Augusta, El Arenal, Jávea/Xàbia |
| 111399396 | El Arenal | 329.500 | 80 | 4.119 |  | – | Piso en Avenida de Paris, El Arenal, Jávea/Xàbia |
| 107839349 | El Arenal | 359.000 | 86 | 4.174 |  | – | Piso en El Arenal, Jávea/Xàbia |
| 109108469 | El Arenal | 465.000 | 111 | 4.189 |  | – | Piso en El Arenal, Jávea/Xàbia |
| 112518540 | El Arenal | 223.000 | 53 | 4.208 |  | – | Piso en Calle Saint Tropez, El Arenal, Jávea/Xàbia |
| 111364826 | El Arenal | 360.000 | 85 | 4.235 | D | – | Piso en Avenida de la Llibertat, El Arenal, Jávea/Xàbia |
| 111071237 | Puerto | 630.000 | 147 | 4.286 | D | 110602085 | Ático en Puerto, Jávea/Xàbia |
| 109074152 | El Arenal | 320.000 | 70 | 4.571 |  | – | Piso en El Arenal, Jávea/Xàbia |
| 111690073 | El Arenal | 230.000 | 50 | 4.600 |  | – | Piso en El Arenal, Jávea/Xàbia |
| 111695117 | El Arenal | 399.000 | 86 | 4.640 |  | – | Piso en El Arenal, Jávea/Xàbia |
| 109724318 | El Arenal | 235.000 | 50 | 4.700 |  | – | Piso en El Arenal, Jávea/Xàbia |
| 109870004 | Puerto | 389.000 | 82 | 4.744 | D | – | Piso en Calle Churruca, Puerto, Jávea/Xàbia |
| 110279888 | Puerto | 389.000 | 80 | 4.862 | D | – | Piso en Puerto, Jávea/Xàbia |
| 110905573 | El Arenal | 389.000 | 78 | 4.987 |  | – | Piso en Avenida de l'Arenal, 14, El Arenal, Jávea/Xàbia |
| 112059566 | El Arenal | 249.500 | 50 | 4.990 |  | – | Piso en El Arenal, Jávea/Xàbia |
| 112214123 | El Arenal | 390.000 | 78 | 5.000 |  | – | Piso en El Arenal, Jávea/Xàbia |
| 111463998 | El Arenal | 395.000 | 78 | 5.064 |  | – | Piso en Urbanización la Isla, El Arenal, Jávea/Xàbia |
| 111759336 | El Arenal | 399.999 | 78 | 5.128 |  | 111842964 | Piso en El Arenal, Jávea/Xàbia |
| 108899315 | Puerto | 389.000 | 75 | 5.187 |  | 110085576 | Dúplex en Calle Churruca, Puerto, Jávea/Xàbia |
| 112521823 | El Arenal | 414.000 | 78 | 5.308 |  | – | Piso en El Arenal, Jávea/Xàbia |
| 108819856 | Puerto | 399.000 | 75 | 5.320 | D | – | Dúplex en Calle Churruca, Puerto, Jávea/Xàbia |
| 111510217 | El Arenal | 430.000 | 80 | 5.375 |  | 111453701 | Piso en Avenida de l'Arenal, El Arenal, Jávea/Xàbia |
| 112371402 | Puerto | 160.000 | 29 | 5.517 |  | – | Estudio en Puerto, Jávea/Xàbia |
| 108883032 | Puerto | 389.000 | 70 | 5.557 | D | – | Piso en Puerto, Jávea/Xàbia |
| 107191794 | El Arenal | 695.000 | 123 | 5.650 | D | – | Piso en Calle Cannes, El Arenal, Jávea/Xàbia |
| 111444238 | El Arenal | 430.000 | 70 | 6.143 | D | 111540143 | Piso en El Arenal, Jávea/Xàbia |
| 110614251 | El Arenal | 595.000 | 90 | 6.611 | D | 112035222, 110792158 | Piso en Avenida de Ultramar, El Arenal, Jávea/Xàbia |
| 112431449 | Puerto | 389.000 | 40 | 9.725 | D | – | Piso en Puerto, Jávea/Xàbia |

Buiten de reeks gelaten wegens gedeeltelijke renovatie of alleen "mogelijkheid tot reforma" (wel status buen estado): Puerto 110648030 (parcialmente reformada, 5.615 €/m²), 110658641 (reformada exceptuando la cocina, 6.083), 111361608 (semi reformado, 6.694), 111039245 (alleen "posibilidad de reforma integral", 1.399); El Arenal 111787733, 111212545 (alleen keuken), 112418349, 109779134, 111212541, 111501634 (alleen een badkamer), 111897376 (alleen badkamers), 112460169 (badkamers + keuken deels), 111865931 (studio, marketingtekst over "propiedades reformadas" in het algemeen).

## 6. Reeks apartment_new — nieuwbouwappartementen (Puerto + El Arenal)

| Reeks | n | min | p25 | mediaan | p75 | max |
|---|---|---|---|---|---|---|
| apartment_new | 43 | 1.630 | 3.412 | 3.944 | 5.528 | 8.380 |
|   · Puerto | 1 | 5.500 | 5.500 | 5.500 | 5.500 | 5.500 |
|   · El Arenal | 42 | 1.630 | 3.390 | 3.876 | 5.528 | 8.380 |
|   · zonder 110963269 (tuin-unit) en zonder units > 190 m² | 36 | 2.977 | 3.581 | 4.602 | 5.666 | 8.380 |
|   · alleen units ≤ 120 m² (zonder 110963269) | 18 | 3.250 | 4.770 | 5.570 | 7.032 | 8.380 |

Samenstelling: 34 advertenties met Idealista-status *obra nueva* in El Arenal (promoties Arenal Jávea Beach / Avenida de París 2, Adeya Jávea I–II / Calle Cannes 3, Marina Bay Sunset / Calle Bruselas 102, Estrasburgo 5, Montañar Beach / Atenas 41, plus een complex met units van 143–314 m² zonder adres), plus 9 advertenties met status "segunda mano" die in de tekst of kenmerken a estrenar / obra nueva / gebouwd 2023–2026 zijn (8 in El Arenal, 1 in Puerto). Na ontdubbelen 43 objecten.

Voorbeelden (8; alle (D)):

| Code | Zone | Vraagprijs € | m² | €/m² | Bouwjaar / renovatie | Label | URL |
|---|---|---|---|---|---|---|---|
| 110983899 | Puerto | 495.000 | 90 | 5.500 | 2026 | Puerto, Avenida d’Ausiàs March — gebouwd 2026, energielabel A, aerothermie, zwembad, garage; enige nieuwbouwvergelijking in Puerto (D) | https://www.idealista.com/es/inmueble/110983899/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 109077975 | El Arenal | 693.000 | 94 | 7.372 | in aanbouw | promotie Arenal Jávea Beach (Avenida de París 2), in aanbouw (notFinished), 2e verdieping (D) | https://www.idealista.com/es/obra-nueva/109077975/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 112383441 | El Arenal | 489.000 | 124 | 3.944 | in aanbouw | promotie Adeya Jávea II (Calle Cannes 3), in aanbouw, ático 124 m² gebouwd / 95 nuttig (D) | https://www.idealista.com/es/obra-nueva/112383441/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 111035010 | El Arenal | 490.000 | 103 | 4.757 | a estrenar | a estrenar, begane grond met 110 m² terras, verkocht als "segunda mano" (D) | https://www.idealista.com/es/inmueble/111035010/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 110479584 | El Arenal | 699.000 | 95 | 7.358 | 2023 | gebouwd 2023, "completamente nuevo", zonder lift (D) | https://www.idealista.com/es/inmueble/110479584/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 108102709 | El Arenal | 490.000 | 90 | 5.444 | 2024 | gebouwd 2024, residencial La Bardisa, label A, garage inbegrepen (D) | https://www.idealista.com/es/inmueble/108102709/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 111862474 | El Arenal | 449.000 | 101 | 4.446 | 2026 | gebouwd 2026, Cap de la Nau Pla 95 — tekst noemt Portichol/Balcón al Mar, Idealista-zone El Arenal (D) | https://www.idealista.com/es/inmueble/111862474/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |
| 110963269 | El Arenal | 440.000 | 270 | 1.630 | in aanbouw | promotie Marina Bay Sunset: 270 m² gebouwd maar 55 m² nuttig (begane grond met tuin) — €/m² vertekend (D) | https://www.idealista.com/es/obra-nueva/110963269/?utm_medium=generativeAI&utm_campaign=appChatgpt&utm_creation=link&utm_source=idGpt&utm_project=leadGeneration&utm_link=inChat_detail |

Volledige reeks:

| Code | Zone | Vraagprijs € | m² | €/m² | (D) | Dubbels (zelfde prijs+m²+zone) | Titel (Idealista) |
|---|---|---|---|---|---|---|---|
| 110963269 | El Arenal | 440.000 | 270 | 1.630 | D | – | Piso en Calle Bruselas, 102, El Arenal, Jávea/Xàbia |
| 111251497 | El Arenal | 740.000 | 314 | 2.357 |  | 111242789 | Piso en El Arenal, Jávea/Xàbia |
| 111511576 | El Arenal | 675.000 | 265 | 2.547 |  | – | Piso en El Arenal, Jávea/Xàbia |
| 111511604 | El Arenal | 565.000 | 202 | 2.797 |  | – | Piso en El Arenal, Jávea/Xàbia |
| 111511579 | El Arenal | 551.000 | 194 | 2.840 |  | – | Piso en El Arenal, Jávea/Xàbia |
| 111252102 | El Arenal | 618.000 | 215 | 2.874 |  | – | Ático en El Arenal, Jávea/Xàbia |
| 111511612 | El Arenal | 521.000 | 175 | 2.977 |  | – | Piso en El Arenal, Jávea/Xàbia |
| 110963677 | El Arenal | 580.000 | 181 | 3.204 |  | – | Ático en Calle Bruselas, 102, El Arenal, Jávea/Xàbia |
| 110162536 | El Arenal | 377.000 | 116 | 3.250 |  | – | Piso en Calle Cannes, 3, El Arenal, Jávea/Xàbia |
| 110162516 | El Arenal | 412.000 | 123 | 3.350 |  | – | Piso en Calle Cannes, 3, El Arenal, Jávea/Xàbia |
| 110162660 | El Arenal | 411.000 | 122 | 3.369 |  | – | Piso en Calle Cannes, 3, El Arenal, Jávea/Xàbia |
| 110963519 | El Arenal | 525.000 | 152 | 3.454 |  | – | Piso en Calle Bruselas, 102, El Arenal, Jávea/Xàbia |
| 110963673 | El Arenal | 598.500 | 171 | 3.500 |  | – | Ático en Calle Bruselas, 102, El Arenal, Jávea/Xàbia |
| 111251997 | El Arenal | 647.000 | 184 | 3.516 |  | 111242862 | Dúplex en El Arenal, Jávea/Xàbia |
| 112503635 | El Arenal | 475.000 | 133 | 3.571 | D | – | Piso en Carretera del Cap de la Nau Pla, 95, El Arenal, Jávea/Xàbia |
| 110963560 | El Arenal | 598.500 | 167 | 3.584 |  | – | Ático en Calle Bruselas, 102, El Arenal, Jávea/Xàbia |
| 111251660 | El Arenal | 515.000 | 143 | 3.601 |  | 111242826 | Ático en El Arenal, Jávea/Xàbia |
| 107601223 | El Arenal | 685.000 | 185 | 3.703 |  | – | Ático en Estrasburgo, 5, El Arenal, Jávea/Xàbia |
| 107601269 | El Arenal | 755.000 | 202 | 3.738 |  | – | Ático en Estrasburgo, 5, El Arenal, Jávea/Xàbia |
| 112135804 | El Arenal | 373.000 | 99 | 3.768 |  | – | Piso en Calle Cannes, 3, El Arenal, Jávea/Xàbia |
| 110162538 | El Arenal | 358.000 | 94 | 3.809 |  | – | Piso en Calle Cannes, 3, El Arenal, Jávea/Xàbia |
| 112383441 | El Arenal | 489.000 | 124 | 3.944 | D | – | Ático en Calle Cannes, 3, El Arenal, Jávea/Xàbia |
| 107891560 | El Arenal | 635.000 | 155 | 4.097 |  | – | Ático en Estrasburgo, 5, El Arenal, Jávea/Xàbia |
| 110422405 | El Arenal | 709.000 | 163 | 4.350 |  | – | Ático en Atenas, 41, El Arenal, Jávea/Xàbia |
| 111862474 | El Arenal | 449.000 | 101 | 4.446 | D | – | Piso en Carretera del Cap de la Nau Pla, 95, El Arenal, Jávea/Xàbia |
| 111035010 | El Arenal | 490.000 | 103 | 4.757 | D | – | Piso en El Arenal, Jávea/Xàbia |
| 111003829 | El Arenal | 500.000 | 104 | 4.808 |  | – | Piso en El Arenal, Jávea/Xàbia |
| 110422372 | El Arenal | 625.000 | 129 | 4.845 |  | – | Piso en Atenas, 41, El Arenal, Jávea/Xàbia |
| 108864058 | El Arenal | 610.000 | 122 | 5.000 |  | – | Piso en Estrasburgo, 5, El Arenal, Jávea/Xàbia |
| 107601278 | El Arenal | 680.000 | 132 | 5.152 |  | – | Piso en Estrasburgo, 5, El Arenal, Jávea/Xàbia |
| 108102709 | El Arenal | 490.000 | 90 | 5.444 | D | – | Piso en Calle Cannes, El Arenal, Jávea/Xàbia |
| 110983899 | Puerto | 495.000 | 90 | 5.500 | D | – | Piso en Avenida d'Ausiàs March, Puerto, Jávea/Xàbia |
| 112194212 | El Arenal | 550.000 | 99 | 5.556 |  | – | Piso en Estrasburgo, 5, El Arenal, Jávea/Xàbia |
| 112312343 | El Arenal | 525.000 | 94 | 5.585 |  | – | Piso en Calle Cannes, El Arenal, Jávea/Xàbia |
| 111676293 | El Arenal | 762.000 | 129 | 5.907 |  | – | Piso en Atenas, 41, El Arenal, Jávea/Xàbia |
| 109077974 | El Arenal | 589.000 | 97 | 6.072 |  | – | Piso en Avenida de Paris, 2, El Arenal, Jávea/Xàbia |
| 111280884 | El Arenal | 565.000 | 90 | 6.278 |  | – | Piso en El Arenal, Jávea/Xàbia |
| 111676508 | El Arenal | 709.000 | 107 | 6.626 |  | – | Piso en Avenida de Paris, 2, El Arenal, Jávea/Xàbia |
| 109077965 | El Arenal | 688.000 | 96 | 7.167 |  | – | Piso en Avenida de Paris, 2, El Arenal, Jávea/Xàbia |
| 110479584 | El Arenal | 699.000 | 95 | 7.358 | D | – | Piso en El Arenal, Jávea/Xàbia |
| 109077975 | El Arenal | 693.000 | 94 | 7.372 | D | – | Piso en Avenida de Paris, 2, El Arenal, Jávea/Xàbia |
| 109077831 | El Arenal | 798.000 | 103 | 7.748 |  | – | Ático en Avenida de Paris, 2, El Arenal, Jávea/Xàbia |
| 109077990 | El Arenal | 771.000 | 92 | 8.380 |  | – | Ático en Avenida de Paris, 2, El Arenal, Jávea/Xàbia |

## 7. Context-reeksen (breder dan gerenoveerd)

Alle "buen estado"-advertenties in de twee zones zonder reformar- of nieuwbouwsignaal, dus inclusief bewoonbare maar niet-gerenoveerde woningen. Alleen als ondergrens van "wat de markt vraagt voor bewoonbaar".

| Reeks | n | min | p25 | mediaan | p75 | max |
|---|---|---|---|---|---|---|
| villa_buen_estado_all (vrijstaand) | 40 | 2.500 | 4.302 | 5.238 | 6.799 | 11.458 |
|   · Puerto | 34 | 2.500 | 4.822 | 5.288 | 7.116 | 11.458 |
|   · El Arenal | 6 | 3.249 | 4.053 | 4.280 | 4.684 | 5.208 |
| apartment_buen_estado_all | 156 | 1.399 | 3.454 | 4.342 | 5.137 | 15.000 |
|   · Puerto | 36 | 1.399 | 3.202 | 4.873 | 5.745 | 9.725 |
|   · El Arenal | 120 | 2.357 | 3.456 | 4.233 | 4.988 | 15.000 |

Rijtjeshuizen: geen aparte reeks voor deze zone (townhouse_renovated hoort bij het casco). Ter informatie gevonden: Puerto 112374691 (adosado "reformada y mantenida", 625.000 € / 131 m² = 4.771 €/m²), 110117537 (adosado, 550.000 € / 90 m² = 6.111); El Arenal 107723159 (adosado "renovada", 460.000 € / 120 m² = 3.833), 112412197 (bungalow reformado, 540.000 € / 70 m² = 7.714), 112197785 (adosado "arquitectura moderna", 465.000 € / 218 m² = 2.133).

## 8. Kanttekeningen

1. **Vraagprijzen, geen transacties.** Idealista toont wat verkopers vragen; werkelijke transactieprijzen liggen in de regel lager en het verschil is per object onbekend. Gebruik deze cijfers als bovengrens/richtpunt, nooit als taxatie.
2. **Zonelabels zijn benaderend.** "Puerto" en "El Arenal" zijn de zones van Idealista, niet de buurten zoals Jan ze kent. Puerto-villa's liggen op La Corona/Cuesta de San Antonio; "El Arenal"-appartementen omvatten Montañar II en Cala Blanca; 111862474/112503635 (Cap de la Nau Pla 95) noemen zichzelf Portichol/Balcón al Mar; 111807268 noemt zichzelf Balcón al Mar maar staat bij Idealista in Puerto. K06 ligt in Aduanas (haven zelf, tweede lijn) — de Puerto-comparables 109870004, 108883032, 110279888, 108819856, 108265680 en 112431449 liggen daar in de buurt (Churruca, La Grava, Doctor Fleming); 110983899 en 108146741 liggen westelijker (Ausiàs March, Avenida dels Furs).
3. **Steekproef.** De reeksen zijn compleet voor wat de tool op 15-09-2026 teruggaf (de som van de prijsbanden dekt elk totaal), maar het blijft één portaal op één dag. Gerenoveerde villa's n=12 (El Arenal n=3), nieuwbouwvilla's n=2, nieuwbouwappartementen Puerto n=1, gerenoveerde appartementen Puerto in de grootteklasse van K06 n=4 — voor die deelreeksen hebben kwartielen weinig betekenis.
4. **Classificatie op advertentietekst.** "Gerenoveerd" is wat de verkoper schrijft; 40 objecten zijn met `property_detail` gecontroleerd (bouwjaar, staat), de rest alleen op tekst. Idealista's veld "staat" kent alleen buen estado / a reformar / obra nueva, dus "gerenoveerd" is nooit een portaalveld. Een renovatie van 2015 (111541292) of 2018 (112265864) telt hier ook als gerenoveerd.
5. **m² gebouwd is soms onbetrouwbaar.** 110963269: 270 m² gebouwd tegenover 55 m² nuttig → 1.630 €/m² is geen marktcijfer. 112431449: 40 m² voor 2 slaapkamers/2 badkamers op twee verdiepingen → 9.725 €/m² is onwaarschijnlijk. 109870004: tekst 40 m², kenmerken 82 m². Villa Imperio: 580 m² (111823302) tegenover 700 m² (111343157) voor hetzelfde project. De medianen zijn robuust tegen deze uitschieters; min/max niet.
6. **Grootte drukt €/m².** Nieuwbouw-units van 175–314 m² en villa's van 700–795 m² trekken de onderkant omlaag; studio's en units van 29–60 m² het omgekeerde. Vergelijk K06 (125 m²) daarom met de 80–150 m²-reeksen, niet met de totale mediaan.
7. **Dubbele advertenties** zijn talrijk (zelfde object bij meerdere makelaars): villa Cap de la Nau 6×, villa Puerto 111998394 5×, appartement Larissa 5×, Ultramar 3×. Ontdubbeld op prijs+m²+zone; dubbels met een andere prijs of m² blijven aparte regels, behalve Villa Imperio (handmatig samengevoegd).
8. **Toolbeperkingen.** Maximaal 50 resultaten per aanroep, geen paginering, geen filter "reformado". Zoekopdrachten met "Puerto y Arenal" in één zin werken niet (0 resultaten of alleen Puerto). Nieuwbouwvilla's in aanbouw zijn bij Idealista niet altijd als "obra nueva" of "villa" getagd — alleen de zoekopdracht zonder staatfilter vond ze.
9. **Geen telefoonnummers, namen van particulieren of sleutels** overgenomen; alle URL's staan letterlijk zoals de tool ze gaf (inclusief utm-parameters).
10. **Peildatum 15-09-2026, momentopname.** Tussen 09:26 en 10:45 uur wisselden al twee advertenties in El Arenal (300–400k: 42 → 41; > 520k: 45 → 44). 109709911 is een renovatie in eindfase; Villa Imperio, Villa Azure en de Arenal-promoties zijn in aanbouw — hun vraagprijs is een prijs op plan.

## 9. Zoeklog (bron en datum: Idealista-assistent, 15-09-2026, 10:41–11:05 uur)

| # | Zoekopdracht (letterlijk) | Type | Door de tool toegepast | Totaal | Opgehaald |
|---|---|---|---|---|---|
| 1 | chalet reformado en Puerto, Jávea/Xàbia | CHALET | Puerto · casas y chalets · buen estado | 61 | 50 |
| 2 | chalet reformado en El Arenal, Jávea/Xàbia | CHALET | El Arenal · casas y chalets · buen estado | 22 | 22 |
| 3 | villa obra nueva a estrenar en Puerto, Jávea/Xàbia | CHALET | Puerto · villa · obra nueva | 0 | 0 |
| 4 | villa obra nueva a estrenar en El Arenal, Jávea/Xàbia | CHALET | El Arenal · villa · obra nueva | 0 | 0 |
| 5 | piso reformado en Puerto, Jávea/Xàbia | HOME | Puerto · pisos · buen estado | 58 | 50 |
| 6 | piso obra nueva a estrenar en Puerto, Jávea/Xàbia | HOME | Puerto · pisos · obra nueva | 0 | 0 |
| 7 | piso obra nueva a estrenar en El Arenal, Jávea/Xàbia | HOME | El Arenal · pisos · obra nueva | 34 | 34 |
| 8 | chalet reformado en Puerto, Jávea/Xàbia hasta 1.500.000 euros | CHALET | Puerto · casas y chalets · buen estado · < 1,5 M | 25 | 25 |
| 9 | chalet reformado en Puerto, Jávea/Xàbia más de 1.500.000 euros | CHALET | idem · > 1,5 M | 37 | 37 |
| 10 | piso reformado en Puerto, Jávea/Xàbia hasta 400.000 euros | HOME | Puerto · pisos · buen estado · < 400k | 34 | 34 |
| 11 | piso reformado en Puerto, Jávea/Xàbia más de 400.000 euros | HOME | idem · > 400k | 24 | 24 |
| 12 | piso reformado en El Arenal, Jávea/Xàbia hasta 300.000 euros | HOME | El Arenal · pisos · buen estado · < 300k | 30 | 30 |
| 13 | piso reformado en El Arenal, Jávea/Xàbia entre 300.000 y 400.000 euros | HOME | idem · 300–400k | 41 | 41 |
| 14 | piso reformado en El Arenal, Jávea/Xàbia entre 400.000 y 520.000 euros | HOME | idem · 400–520k | 46 | 46 |
| 15 | piso reformado en El Arenal, Jávea/Xàbia más de 520.000 euros | HOME | idem · > 520k | 44 | 44 |
| 16 | villa moderna reformada en Jávea Puerto y Arenal | CHALET | "zona personalizada" · villa · buen estado | 0 | 0 |
| 17 | villa de diseño en Jávea Puerto y Arenal | CHALET | Puerto · villas (geen staatfilter) | 24 | 24 |
| 18 | villa de nueva construcción en Jávea Puerto y Arenal | CHALET | Puerto · villa · obra nueva | 0 | 0 |
| 19 | villa obra nueva a estrenar en Jávea/Xàbia | CHALET | Jávea/Xàbia · villa · obra nueva (referentie) | 46 | 46 |
| 20 | casa o chalet en Puerto, Jávea/Xàbia | CHALET | Puerto · casas y chalets · alle staten | 70 | 50 |
| 21 | casa o chalet en El Arenal, Jávea/Xàbia | CHALET | El Arenal · casas y chalets · alle staten | 22 | 22 |
| 22 | casa o chalet en Puerto, Jávea/Xàbia hasta 1.500.000 euros | CHALET | Puerto · alle staten · < 1,5 M | 30 | 30 |
| 23 | casa o chalet en Puerto, Jávea/Xàbia más de 1.500.000 euros | CHALET | Puerto · alle staten · > 1,5 M | 40 | 40 |

`property_detail` uitgevoerd op 40 objecten (alle "active" op 15-09-2026): villa's 111823302, 111998394, 111807268, 111286574, 109709911, 108111394, 109649453, 111071067, 108332489, 112209448, 112265864, 109843783, 105665335, 111343157, 110755799, 111720790; appartementen Puerto 109870004, 108883032, 110279888, 108819856, 111071237, 112431449, 108265680, 108146741, 110983899; appartementen El Arenal 110614251, 111444238, 112011823, 107191794, 111364826, 112384680, 109077975, 112383441, 111035010, 110479584, 108102709, 110963269, 111862474, 112503635; kandidaat K06 106514871.

Ruwe data en scripts (niet in de projectmap): scratchpad `pa2/` van deze sessie (`r*.json` = letterlijke toolantwoorden, `analyse2.py`, `final2.py`, `series2.json`, `make_md2.py`).

## 10. Verschillen met de versie van 09:39 (zelfde dag)

Dit bestand vervangt de eerdere versie van 15-09-2026 09:39. Verschillen, alle op basis van `property_detail`-controles in deze ronde:

- **villa_renovated 14 → 12**: 109649453 (Finca Mezquida, 1980, structuur origineel, ontwikkelpotentieel) was ten onrechte opgenomen; 111343157 bleek het nieuwbouwproject Villa Imperio en is naar villa_new verhuisd. Mediaan Puerto 6.757 → 6.759 €/m², totaal 6.107 → 6.253 €/m².
- **villa_new 0 → 2**: Villa Imperio (111823302) en Villa Azure (110755799), beide in aanbouw in La Corona, gevonden via zoekopdrachten zonder staatfilter (nr. 17, 20, 22, 23).
- **apartment_renovated en apartment_new**: dezelfde objecten en cijfers (45 resp. 43); extra dubbele advertentiecodes vastgesteld (110602085, 110293603, 112381941, 111453701, 111540143, 110604173, 112281618, 112413770, 112505992, 111777540, 111676743, 112225050).
- Nieuw toegevoegd: gevoeligheidsreeksen op grootteklasse 80–150 m² (K06) en de controle van K06 zelf.

# ⏸️ ACTIE VOOR JAN — stand 15-09-2026 (fase B gestart)

> **Let op:** de lopende lijst staat sinds 16-09 in `../TODO.md`. Dit document blijft staan als
> toelichting bij de punten van 15-09; nieuwe punten komen alleen nog in TODO.md.

Gerangschikt op wat het eerst nodig is. Niets hiervan doet het systeem zelf.

## Vandaag/morgen
1. **Bezorging aanzetten.** Maak in Discord (categorie "TREE Agenten 2.0") een kanaal
   `#deal-hunter` en een webhook (Kanaalinstellingen → Integraties → Webhooks → URL kopiëren).
   Zet die URL in `~/tree-es/deal-hunter/.env` als `DISCORD_WEBHOOK_URL=`. Voor e-mail:
   `RESEND_API_KEY=`, `DH_EMAIL_FROM=` (een geverifieerd afzenderdomein in Resend) en
   `DH_EMAIL_TO=` (jouw adres). Tot dan staan de rapporten alleen op de reviewpagina.
2. **AI-classificatie aanzetten (optioneel, binnen 100 €/maand).** Zet `ANTHROPIC_API_KEY=`
   in dezelfde `.env`. Ik heb bewust niet de sleutel uit Tree AI OS gekopieerd; dat is jouw
   keuze (aparte sleutel is netter voor kostenbewaking).
3. **Bericht K07 goedkeuren.** Concept in `acties/2026-09-15-bericht-K07-aanbieder.md`:
   kies de route (via Background Properties of rechtstreeks Atina) en zeg "ja" of pas aan.
4. **Idealista Search API aanvragen.** Tekst in `acties/2026-09-15-idealista-search-api-aanvraag.md`;
   formulier op http://developers.idealista.com/access-request, op naam van TREE.
5. **Schriftelijke BP-afspraak in de map zetten** (`~/tree-es/deal-hunter/kader/`), zodat de
   gebruiksrechten in het bronnenregister van "door Jan gemeld" naar "document gezien" gaan.

## Deze week
0. **Resales-Online (nieuw, 16-09).** Twee vragen vooraf: is TREE Properties al lid, en zo nee, wat kost
   lidmaatschap? En: geeft Resales-Online schriftelijk toestemming om objecten van andere leden intern
   op te slaan en te analyseren? Hun voorwaarden staan alleen weergave op je eigen website toe en
   verbieden het doorgeven van andermans objecten aan derden. Eigen objecten van TREE mogen altijd.
   Zodra beide rond zijn, kan de koppeling op hun WebAPI V6 (API-sleutel per IP-adres) worden gebouwd.
6. **Namen doorgeven:** vaste advocaat + gestor (veilingdossiers, twaalf juridische vragen uit
   R16 §7) en vaste architect (eerste opdracht: informe urbanístico K07).
7. **Accounts met e-mailmeldingen aanmaken:** Idealista (zoekopdrachten "Jávea para reformar",
   "terrenos Jávea/Benitachell/Moraira"), Fotocasa, subastas.boe.es (alleen als natuurlijk persoon;
   meldingen op Xàbia/Jávea/Javea, postcodes 03730/03737/03738, orgaan Dénia), Servihabitat
   Profesionales. Doorsturen van die mails naar het systeem: pas na juridische check.
8. **Drie tot vijf nacalculaties** van TREE Constructions (€/m² excl. btw, met jaartal) voor:
   nieuwe villa, integrale renovatie, keuken+badkamers, zwembad, keermuren. De 1.000/2.000 €/m²
   staan nu als jouw opgave in het model; nacalculaties maken er bewijs van.
9. **Honoraria en commissie bevestigen.** Het model rekent nu met 17 % honoraria (architect 12 %
   + aparejador 5 % over PEM) en 5 % makelaarscommissie + btw. Die twee aannames bepalen samen
   ruwweg 60.000–100.000 € van de maximale koopprijs per deal (zie `tools/gevoeligheid.py`).

## Kennisgeving (geen actie)
- **Dashboard:** https://mac-mini-van-root-admin.tail69022d.ts.net:8710 (alleen via Tailscale). Kaart met
  kadaster en luchtfoto, blokken per kansrijkheid, dossier per object met drie maximale koopprijzen
  en wat-als-schuiven, oordeel per object. Rekent met 20 % winstmarge op verkoopwaarde en 8 % honoraria.
- Nieuwe diensten op de Mac: `com.tree.deal-hunter` (10:00 en 15:00) en
  `com.tree.deal-hunter-review` (reviewpagina, poort 8710, via Tailscale).
- Tailscale heeft één extra route: https://mac-mini-van-root-admin.tail69022d.ts.net:8710
  (alleen tailnet). Uitzetten: `tailscale serve --https=8710 off`.
- Er is niets geïnstalleerd; alles draait op de bestaande Python-omgeving en SQLite.

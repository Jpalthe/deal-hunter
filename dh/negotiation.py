"""Onderhandelplan per object: openingsbod, streefprijs, weglooppunt en de argumenten erbij.

Geen onderhandelkunst uit de losse pols: elk bedrag komt uit de rekenmodule en elk argument komt
uit iets wat wij hebben vastgesteld. Staat er geen bewijs onder, dan staat het argument er niet.

Uitgangspunten (kader van Jan, 15 en 17-09-2026):
- Boven de maximale koopprijs in het basisscenario koopt hij niet. Dat is het weglooppunt.
- De streefprijs is de voorzichtige maximale koopprijs; daar is de marge ook gehaald als de
  verkoopprijzen tegenvallen.
- Het openingsbod ligt onder de streefprijs, maar niet zo laag dat het gesprek stopt.
"""
from __future__ import annotations

import json
from datetime import date, datetime

from . import config

# Jan 26-09-2026: "openen op € 222.000 bij een vraagprijs van € 338.000 is 35 % eronder; zo worden
# wij niet serieus genomen". De oorzaak was dat er twee kortingen op elkaar stapelden: eerst 90 % van
# wat de deal draagt, en daar nog eens 92 % van. Samen 83 %, en dat bovenop een plafond dat zelf al
# onder de vraagprijs lag. Nu is er nog één stap: een bescheiden marge onder het weglooppunt, zodat
# er ruimte is om elkaar te vinden zonder dat het bod als niet serieus overkomt.
OPENING_ONDER_PLAFOND = 0.04   # openingsbod onder wat de deal draagt
STREEF_ONDER_PLAFOND = 0.02    # streefprijs onder wat de deal draagt
BODEM_VAN_VRAAGPRIJS = 0.55  # lager openen dan dit leest als niet serieus; dan eerst onderbouwen
KLOOF_TE_GROOT = 0.50        # draagt de deal minder dan dit deel van de vraagprijs, dan is er niets te onderhandelen
STIL_NA_DAGEN = 120          # zo lang te koop = onderhandelruimte

# Jan 26-09-2026: hoe ver je onder de vraagprijs mag openen hangt af van hoe lang iets te koop staat.
# Bij een verse advertentie is een scherp bod niet serieus; bij een woning die er al een jaar staat
# begrijpt iedereen het. De trap hieronder is zijn eigen indeling.
BODTRAP = ((90, 0.15), (180, 0.20), (365, 0.25))   # tot zoveel dagen: hoogstens zoveel korting


def _te_koop_sinds(listing: dict) -> tuple[int | None, str]:
    """Hoe lang staat dit te koop, en hoe zeker weten wij dat?

    Alleen de datum van de bron zelf telt. `first_seen` is wanneer wíj het voor het eerst zagen, en
    de meeste makelaarssites lezen wij pas sinds deze week; een woning die daar gisteren opdook kan
    er al een jaar staan. Die datum als leeftijd gebruiken zou de trap hierboven op een verzinsel
    laten rusten."""
    d = _dagen(listing.get("source_date"))
    if d is not None and d >= 0:
        return d, "bron"
    return None, "onbekend"


def max_korting(listing: dict) -> tuple[float | None, int | None, str]:
    """De grootste korting waarmee je nog serieus opent. None betekent: geen grens."""
    dagen, herkomst = _te_koop_sinds(listing)
    if dagen is None:
        return None, None, herkomst          # niet bekend: dan leggen wij geen grens op
    for grens, korting in BODTRAP:
        if dagen < grens:
            return korting, dagen, herkomst
    return None, dagen, herkomst             # langer dan een jaar: verder mag


def _dagen(iso: str | None) -> int | None:
    if not iso:
        return None
    try:
        d = datetime.fromisoformat(iso).date()
    except ValueError:
        return None
    return (datetime.now(config.TZ).date() - d).days


def _eur(v) -> str:
    return "onbekend" if v is None else f"€ {round(v):,}".replace(",", ".")


def plan(listing: dict, best: dict | None, parcel: dict | None = None,
         history: list | None = None, signals: dict | None = None) -> dict:
    """Bouwt het onderhandelplan. `best` is het gekozen scenario uit feasibility.compute."""
    ask = listing.get("price")
    sig = signals or {}
    out: dict = {"asking": ask, "arguments": [], "levers": [], "risks": [], "verdict": None}

    if not ask or not best or not best.get("available"):
        out["verdict"] = "Nog geen bod te onderbouwen: de rekensom is niet rond."
        return out

    mp = best["max_price"]
    plafond = mp["base"]          # wat de deal draagt; hierboven verdien je niets meer
    ruimte = plafond / ask - 1    # positief: de vraagprijs past al binnen wat de deal draagt

    if plafond >= ask:
        # De vraagprijs past. Dan onderhandel je een gewone korting, niet omhoog.
        walk = round(ask)
        target = round(ask * 0.95 / 1000) * 1000
        opening = round(ask * 0.90 / 1000) * 1000
    else:
        walk = plafond
        # De streefprijs hoort tussen het voorzichtige en het basisscenario te liggen, niet óp het
        # voorzichtige. Anders krijg je een openingsbod dat niemand serieus neemt: bij een villa van
        # € 533.000 die de deal tot € 380.000 draagt, kwam er met de oude regel € 78.000 uit, omdat
        # het voorzichtige scenario daar op € 85.000 uitkwam. Het voorzichtige getal blijft apart
        # zichtbaar als "voorzichtig gerekend"; dát is de grens die je in je hoofd houdt.
        target = round(plafond * (1 - STREEF_ONDER_PLAFOND) / 1000) * 1000
        opening = round(plafond * (1 - OPENING_ONDER_PLAFOND) / 1000) * 1000
    opening = max(min(opening, target), 0)
    target = min(target, walk)
    # Hoe ver de vraagprijs boven het haalbare staat. Dat is de echte onderhandelafstand, en die
    # verzin je niet weg met een lager openingsbod.
    kloof_pct = round(1 - plafond / ask, 3) if ask else None

    # De ondergrens van een serieus bod, als wij weten hoe lang het te koop staat.
    korting_max, dagen_te_koop, leeftijd_bron = max_korting(listing)
    beleefd = round(ask * (1 - korting_max)) if korting_max is not None else None
    serieus_mogelijk = True
    if beleefd is not None:
        if beleefd > walk:
            # Een serieus bod zou boven je eigen grens liggen. Dan valt hier niets te openen.
            serieus_mogelijk = False
        else:
            opening = max(opening, round(beleefd / 1000) * 1000)
            target = max(target, opening)
    laag = opening < ask * BODEM_VAN_VRAAGPRIJS
    # Draagt de deal maar een fractie van de vraagprijs, dan is een openingsbod geen onderhandel-
    # positie meer maar een conclusie. Dat hoort er ook zo te staan in plaats van als bedrag.
    kloof = plafond < ask * KLOOF_TE_GROOT

    out.update({
        "ceiling": plafond,                  # wat de deal maximaal draagt
        "headroom": round(ruimte, 3),        # lucht boven de vraagprijs, voor het geval er concurrentie is
        "walk_away": walk,
        "target": target,
        "opening": opening,
        "opening_pct_of_asking": round(opening / ask - 1, 3) if ask else None,
        "target_pct_of_asking": round(target / ask - 1, 3) if ask else None,
        "walk_pct_of_asking": round(walk / ask - 1, 3) if ask else None,
        "opening_is_laag": laag,
        "kloof_pct": kloof_pct,
        "serieus_mogelijk": serieus_mogelijk,
        "max_korting": korting_max,
        "dagen_te_koop": dagen_te_koop,
        "leeftijd_bron": leeftijd_bron,
        "serieus_tekst": (None if serieus_mogelijk else
                          f"Een serieus bod zou hier {_eur(beleefd)} zijn, en dat ligt boven de "
                          f"{_eur(walk)} die dit project draagt. Zolang de vraagprijs niet zakt, "
                          f"valt hier niet te openen."),
        "kloof_te_groot": kloof,
        "kloof_tekst": (f"De deal draagt {_eur(plafond)} tegenover een vraagprijs van {_eur(ask)}. "
                        f"Dat is geen onderhandeling meer. Alleen de moeite waard als de verkoper "
                        f"echt moet, of als er iets in de aanname niet klopt.") if kloof else None,
    })

    # ---------------------------------------------------------------- argumenten
    a = out["arguments"]

    dagen = _dagen(listing.get("first_seen"))
    if dagen is not None and dagen >= STIL_NA_DAGEN:
        a.append({"punt": f"Staat al {dagen} dagen bij ons in beeld zonder verkoop.",
                  "gebruik": "Vraag waarom het nog te koop staat en wat er eerder is geboden.",
                  "bewijs": "eigen waarneming sinds de eerste ronde"})

    hist = history or []
    if len(hist) >= 2:
        eerste, laatste = hist[0][1], hist[-1][1]
        if eerste and laatste and laatste < eerste:
            pct = (laatste - eerste) / eerste * 100
            a.append({"punt": f"De prijs is al {abs(pct):.0f} % gezakt, van {_eur(eerste)} naar {_eur(laatste)}.",
                      "gebruik": "Wie één keer zakt, zakt vaker. Noem het niet als verwijt maar als richting.",
                      "bewijs": "prijsverloop in ons eigen bestand"})

    for s in (sig.get("verkoopdruk") or []):
        tekst = {
            "bank of servicer": ("De aanbieder is een bank of een servicer.",
                                 "Die sturen op doorlooptijd en kwartaalcijfers, niet op de laatste euro. Bied schriftelijk en met een termijn."),
            "gerechtelijke procedure": ("Het pand komt uit een gerechtelijke procedure.",
                                        "Vraag naar bezit, ontruiming en schulden voordat je over prijs praat; dat is je grootste hefboom."),
            "erfenis": ("Er is sprake van een nalatenschap.",
                        "Meerdere erfgenamen willen meestal snel en gelijk verdelen. Een korte, zekere afwikkeling is meer waard dan de hoogste prijs."),
            "scheiding": ("Er is sprake van een verdeling tussen twee partijen.",
                          "Zekerheid en tempo tellen zwaar. Bied één bedrag, geen constructies."),
            "haast bij verkoper": ("De advertentie zegt zelf dat het snel moet.",
                                   "Zet daar een korte, harde termijn tegenover met een aanbetaling die klaarstaat."),
            "bouw stilgelegd": ("De bouw ligt stil.",
                                "Een vergunning die verloopt is een kostenpost voor de verkoper en een argument voor jou."),
            "prijs verlaagd": ("De vraagprijs is verlaagd.",
                               "Vraag wanneer en waarom; het antwoord vertelt je hoeveel er nog in zit."),
        }.get(s)
        if tekst:
            a.append({"punt": tekst[0], "gebruik": tekst[1], "bewijs": "signaal uit de advertentietekst"})

    p = parcel or {}
    for m in (json.loads(p.get("mismatches") or "[]") if isinstance(p.get("mismatches"), str) else (p.get("mismatches") or [])):
        a.append({"punt": m, "gebruik": "Laat de verkoper het verschil verklaren vóór je een bedrag noemt. "
                                        "Elk niet verklaard verschil is een korting of een voorbehoud.",
                  "bewijs": "Sede Electrónica del Catastro"})

    for b in (sig.get("blockers") or [])[:8]:
        out["risks"].append(b)
    for w in (best.get("warnings") or []):
        out["risks"].append(w)
    if out["risks"]:
        out["voorbehouden"] = (
            "Zet deze punten als ontbindende voorwaarde in het bod, niet als prijsargument. Je koopt pas als ze "
            "bewezen zijn, en tot die tijd is elk bedrag voorwaardelijk.")

    # ---------------------------------------------------------------- hefbomen
    lev = out["levers"]
    sc = best
    lev.append({"punt": "Betalen met eigen geld, geen financieringsvoorbehoud.",
                "waarde": "Dat is in dit segment vaak twee tot vier weken sneller dan een koper met hypotheek, en dat is geld waard voor een verkoper met haast."})
    if sc.get("months"):
        lev.append({"punt": f"Wij kunnen binnen {sc['months']} maanden leveren en verkopen.",
                    "waarde": "Zeg dat niet tegen de verkoper, maar reken ermee: elke maand langer kost je vaste lasten en rente op eigen geld."})
    lev.append({"punt": "Aanbetaling staat klaar.",
                "waarde": f"Tot {_eur(150000)} volgens het kader. Een hogere arras penitenciales koopt tijd en exclusiviteit."})
    if (sc.get("fitout") or {}).get("total"):
        lev.append({"punt": "Keuken, badkamers en tegels komen uit eigen huis.",
                    "waarde": f"{_eur(sc['fitout']['total'])} aan werk dat binnen de groep blijft; dat is marge die een gewone koper niet heeft."})
    if sc.get("channel", {}).get("used") == "intern":
        lev.append({"punt": "TREE Properties verkoopt het eindproduct zelf.",
                    "waarde": f"Scheelt {_eur(sc['channel'].get('saved_vs_extern'))} aan courtage tegenover een externe makelaar. "
                              "Dat is precies de ruimte die je bij de aankoop kunt inzetten."})

    # ---------------------------------------------------------------- oordeel
    if ask <= mp["conservative"]:
        out["verdict"] = (f"Kopen. Bij de vraagprijs van {_eur(ask)} haal je de marge zelfs als de verkoopprijzen tegenvallen. "
                          f"Open op {_eur(out['opening'])}; boven de vraagprijs ga je niet, want dat hoeft niet.")
    elif plafond >= ask:
        voorzichtig = mp["conservative"]
        if voorzichtig and voorzichtig < ask:
            out["verdict"] = (f"Alleen kopen als het basisscenario uitkomt. Daarin draagt de deal {_eur(plafond)} en past de "
                              f"vraagprijs van {_eur(ask)}. Maar in het voorzichtige scenario is de bovengrens {_eur(voorzichtig)}, "
                              f"dus {_eur(ask - voorzichtig)} onder de vraagprijs. Vallen de verkoopprijzen tegen, dan verlies je geld. "
                              f"Open op {_eur(out['opening'])} en houd {_eur(voorzichtig)} als echte grens in je hoofd.")
        else:
            out["verdict"] = (f"Kopen. De deal draagt {_eur(plafond)} en ook voorzichtig gerekend blijft de vraagprijs van "
                              f"{_eur(ask)} eronder. Open op {_eur(out['opening'])} en streef naar {_eur(target)}.")
    elif plafond >= 0.70 * ask:
        out["verdict"] = (f"Onderhandelen. Je moet {abs(out['walk_pct_of_asking']) * 100:.0f} % onder de vraagprijs komen: "
                          f"de deal draagt {_eur(plafond)} tegenover een vraagprijs van {_eur(ask)}. Open op {_eur(out['opening'])} "
                          f"en stop boven {_eur(walk)}.")
    else:
        out["verdict"] = (f"Niet bieden op deze prijs. De deal draagt {_eur(plafond)} en er wordt {_eur(ask)} gevraagd. "
                          f"Dat gat van {abs(out['walk_pct_of_asking']) * 100:.0f} % ga je niet dichten. Op de volglijst, terugkijken bij een prijsdaling.")

    if laag:
        out["opening_toelichting"] = (
            f"Dit openingsbod ligt {abs(out['opening_pct_of_asking']) * 100:.0f} % onder de vraagprijs. Zo laag openen werkt "
            "alleen als je het onderbouwt. Stuur de rekensom mee, of noem eerst de punten hierboven en laat de verkoper zelf zakken.")
    return out


def markdown(p: dict) -> str:
    """Het plan als leesbare tekst voor het dossier."""
    if not p.get("walk_away"):
        return p.get("verdict") or ""
    lines = [p["verdict"], "",
             f"- Openingsbod: **{_eur(p['opening'])}** ({p['opening_pct_of_asking'] * 100:+.0f} %)",
             f"- Streefprijs: **{_eur(p['target'])}** ({p['target_pct_of_asking'] * 100:+.0f} %)",
             f"- Weglopen boven: **{_eur(p['walk_away'])}** ({p['walk_pct_of_asking'] * 100:+.0f} %)",
             f"- Wat de deal draagt: {_eur(p['ceiling'])}" + (f", dus {_eur(p['ceiling'] - p['asking'])} speling boven de vraagprijs als er concurrentie is" if p.get('headroom', 0) > 0 else "")]
    if p.get("opening_toelichting"):
        lines += ["", p["opening_toelichting"]]
    if p.get("risks"):
        lines += ["", "**Voorbehouden, niet onderhandelbaar**", p.get("voorbehouden", "")]
        lines += [f"- {r}" for r in p["risks"][:8]]
    if p["arguments"]:
        lines += ["", "**Wat je aan tafel gebruikt**"]
        lines += [f"- {a['punt']} {a['gebruik']}" for a in p["arguments"]]
    if p["levers"]:
        lines += ["", "**Wat jij te bieden hebt dat een ander niet heeft**"]
        lines += [f"- {l['punt']} {l['waarde']}" for l in p["levers"]]
    return "\n".join(lines)

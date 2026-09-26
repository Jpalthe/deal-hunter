"""Meldingen bij sterke kansen (keuze van Jan, 17-09-2026).

Twee categorieën, met verschil in toon:

  direct    — het object haalt de winstmarge al bij de vraagprijs (klasse groen of blauw).
              Zeldzaam, dus dat mag onderbreken: apart bericht in Discord.
  verzamel  — het object is haalbaar binnen 30 % korting op de vraagprijs (klasse oranje).
              Dat zijn er meer, dus die gaan in één verzamelbericht mee met de ronde.

Een object meldt hoogstens één keer per categorie. Opnieuw melden gebeurt alleen als de categorie
beter wordt (verzamel → direct) of als de vraagprijs sinds de vorige melding met meer dan 2 % is
gezakt. Zonder DISCORD_WEBHOOK_URL wordt er niets verstuurd; de melding wordt wél vastgelegd en is
zichtbaar op het dashboard en de telefoonpagina.
"""
from __future__ import annotations

import json
import logging
import re
from functools import lru_cache
from datetime import datetime

import httpx

from . import config, focus
from .store import Store

log = logging.getLogger("dh.alerts")

DIRECT_CLASSES = ("groen", "blauw")
COLLECT_CLASSES = ("oranje",)
REPEAT_DROP = 0.02          # opnieuw melden bij meer dan 2 % prijsdaling sinds de vorige melding
TIER_RANK = {"verzamel": 1, "direct": 2}


def tier_for(item: dict) -> str | None:
    """Categorie op basis van de kleurklasse van het object; alleen betrouwbaar gerekende objecten
    die binnen de focus vallen (Jan 25-09-2026: Jávea, renoveren of ombouwen)."""
    if not focus.past(item):
        return None
    if not item.get("reliable"):
        return None
    if item.get("calc") and item["calc"].get("result", 0) < 0:
        return None
    cls = item.get("class")
    if cls in DIRECT_CLASSES:
        return "direct"
    if cls in COLLECT_CLASSES:
        return "verzamel"
    return None


def is_new(store: Store, item: dict, tier: str) -> bool:
    prev = store.last_alert(int(item["id"]))
    if prev is None:
        return True
    if TIER_RANK[tier] > TIER_RANK.get(prev["tier"], 0):
        return True
    old, new = prev["price"], item.get("price")
    return bool(old and new and (old - new) / old > REPEAT_DROP)


def collect(store: Store, items: list[dict]) -> dict[str, list[dict]]:
    """Bepaalt welke objecten nu gemeld moeten worden. Schrijft nog niets weg."""
    out: dict[str, list[dict]] = {"direct": [], "verzamel": []}
    for it in items:
        t = tier_for(it)
        if t and is_new(store, it, t):
            out[t].append(it)
    out["direct"].sort(key=lambda x: -(x.get("room") or 0))
    out["verzamel"].sort(key=lambda x: -(x.get("room") or 0))
    return out


def _eur(v) -> str:
    return "onbekend" if v is None else f"€ {round(v):,}".replace(",", ".")


def line(it: dict) -> str:
    room = it.get("room")
    room_txt = f"{room * 100:+.0f} % t.o.v. vraagprijs" if room is not None else "ruimte onbekend"
    calc = it.get("calc") or {}
    res = f"resultaat {_eur(calc.get('result'))} bij marge {calc.get('margin', 0) * 100:.0f} %" if calc else ""
    where = " · ".join(x for x in [it.get("zone_label") or it.get("area_label"), it.get("location")] if x)
    return (f"- **{it.get('ref')}** {where} — vraagprijs {_eur(it.get('price'))}, "
            f"maximaal {_eur(it.get('max_price', {}).get('base'))} ({room_txt}). {it.get('scenario') or ''} {res}".rstrip())


def herinneringen_tekst(rijen: list[dict]) -> str:
    """Wie je vandaag moet terugbellen (Jan, 26-09-2026: mee in het bericht van 08:00)."""
    if not rijen:
        return ""
    r = [f"📞 **{len(rijen)} keer terugbellen vandaag**"]
    for h in rijen[:10]:
        notitie = (h.get("notitie") or "").strip().replace("\n", " ")
        r.append(f"- **{h.get('source_ref')}** {_eur(h.get('price'))}"
                 + (f" — {notitie[:120]}" if notitie else "")
                 + (f" (stond op {h['volgende_stap']})" if h.get("volgende_stap") else ""))
    return "\n".join(r)


def message(direct: list[dict], collected: list[dict], report_url: str | None) -> str | None:
    """De begeleidende regel boven de kaartjes. Kort houden: het detail staat in de kaartjes.

    Jan 26-09-2026: het oude bericht was één lap tekst met per object acht getallen op één regel.
    Wat hij miste was juist het eenvoudigste — bij welke makelaar het staat en een link erheen."""
    if not direct and not collected:
        return None
    delen = []
    if direct:
        delen.append(f"🟢 **{len(direct)} sterke kans{'en' if len(direct) != 1 else ''}**")
    if collected:
        delen.append(f"🟠 {len(collected)} binnen onderhandelbereik")
    regels = [" · ".join(delen)]
    getoond = len(direct[:MAX_KAARTJES]) + max(0, MAX_KAARTJES - len(direct[:MAX_KAARTJES]))
    totaal = len(direct) + len(collected)
    if totaal > MAX_KAARTJES:
        regels.append(f"De {MAX_KAARTJES} sterkste staan hieronder; de rest in de app.")
    regels.append("Tik op de titel om de advertentie te openen. Controleer perceel en vergunning "
                  "vóór enig contact.")
    if report_url:
        regels.append(f"Volledig rapport: {report_url}")
    return "\n".join(regels)


def kaartjes_voor(direct: list[dict], collected: list[dict]) -> list[dict]:
    """De objecten als kaartjes, sterkste eerst."""
    return [kaartje(i) for i in (direct + collected)][:MAX_KAARTJES]


def _html(text: str) -> str:
    """Van het Discord-bericht naar een leesbare mail. Geen opmaaktaal, geen afbeeldingen."""
    import html as h
    regels = []
    for r in text.split("\n"):
        r = r.strip()
        if not r:
            regels.append("<p style='margin:0.6em 0'></p>")
            continue
        veilig = h.escape(r)
        veilig = veilig.replace("**", "")          # de vetmarkering van Discord zegt hier niets
        if r.startswith("- "):
            regels.append(f"<li style='margin:0.25em 0'>{veilig[2:]}</li>")
        else:
            regels.append(f"<p style='margin:0.6em 0'>{veilig}</p>")
    body = "".join(regels).replace("<li", "<ul style='margin:0.4em 0;padding-left:1.1em'><li", 1)
    if "<li" in body:
        body += "</ul>"
    return ("<div style=\"font:15px/1.55 -apple-system,Helvetica,Arial,sans-serif;color:#2b3331;"
            "max-width:36em\"><p style='font:500 12px/1 monospace;letter-spacing:.2em;color:#b8a07a'>"
            "TREE DEAL HUNTER</p>" + body + "</div>")


def send_email(env: dict, text: str, onderwerp: str) -> str:
    """Tweede kanaal naast Discord (Jan, 25-09-2026). Via Resend, dat een gewone HTTPS-API heeft;
    er is dus niets geïnstalleerd."""
    sleutel, naar = env.get("RESEND_API_KEY"), env.get("DH_EMAIL_TO")
    if not sleutel or not naar:
        ontbreekt = " en ".join(x for x, v in (("RESEND_API_KEY", sleutel), ("DH_EMAIL_TO", naar)) if not v)
        return f"e-mail: overgeslagen (geen {ontbreekt} in .env)"
    van = env.get("DH_EMAIL_FROM") or "Deal Hunter <onboarding@resend.dev>"
    try:
        with httpx.Client(timeout=25) as c:
            r = c.post("https://api.resend.com/emails",
                       headers={"Authorization": f"Bearer {sleutel}"},
                       json={"from": van, "to": [a.strip() for a in str(naar).split(",") if a.strip()],
                             "subject": onderwerp, "html": _html(text), "text": text})
            if r.status_code >= 300:
                return f"e-mail: fout {r.status_code}"
    except Exception as e:  # noqa: BLE001
        return f"e-mail: fout {str(e)[:100]}"
    return "e-mail: verzonden"


def bezorg(env: dict, text: str, onderwerp: str = "Deal Hunter",
           kaartjes: list[dict] | None = None) -> str:
    """Beide kanalen. Eén kanaal dat uitvalt mag het andere niet tegenhouden."""
    return " · ".join((send(env, text, kaartjes), send_email(env, text, onderwerp)))


def is_bezorgd(uitslag: str | None) -> bool:
    """Is deze melding langs minstens één kanaal écht de deur uit gegaan?

    Aanleiding (26-09-2026): 24 meldingen zijn maandenlang stilletjes
    overgeslagen omdat er geen webhook in .env stond. De uitslag werd wél
    netjes vastgelegd, maar niemand las die ooit — Jan dacht dat er simpelweg
    geen kansen waren. Deze functie maakt dat verschil leesbaar voor de app.
    """
    if not uitslag:
        return False
    if uitslag.startswith("nulmeting"):
        return False          # bewust niet verstuurd, geen storing
    return "verzonden" in uitslag


def bezorgstand(store: Store) -> dict:
    """Hoeveel meldingen zijn er niet aangekomen, en waarom niet.

    De app toont dit als balk bovenaan; zie /api/bezorgstand.
    """
    gemist, laatste_fout, laatst_gelukt = 0, None, None
    for at, delivered in store.con.execute(
        "SELECT at, delivered FROM alerts ORDER BY at"
    ):
        if is_bezorgd(delivered):
            laatst_gelukt = at
        elif delivered and not str(delivered).startswith("nulmeting"):
            gemist += 1
            laatste_fout = delivered
    return {
        "gemist": gemist,
        "laatste_fout": laatste_fout,
        "laatst_gelukt": laatst_gelukt,
        "werkt": gemist == 0 or bool(laatst_gelukt),
    }


# Discord kleurt de streep links van een kaartje. Zelfde kleuren als in de app.
KLEUR = {"groen": 0x2F7A55, "blauw": 0x2F6386, "oranje": 0xB86E12,
         "grijs": 0x8C918E, "onzeker": 0x7D6A9C}
MAX_KAARTJES = 10          # de bovengrens van Discord per bericht


@lru_cache(maxsize=1)
def _kantoornamen() -> dict:
    """Host → de naam zoals het kantoor zichzelf noemt, uit kader/makelaars.json."""
    try:
        d = json.loads((config.KADER / "makelaars.json").read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    uit = {}
    for k in d.get("kantoren") or []:
        w = (k.get("website") or "").split("//")[-1].replace("www.", "").strip("/")
        naam = re.sub(r"\s*\(.*?\)\s*", " ", k.get("naam") or "").strip()
        naam = re.sub(r",?\s*(S\.L\.U?\.?|S\.A\.)\s*$", "", naam).strip()
        if w and naam:
            uit[w] = naam
    return uit


def _bron(it: dict) -> str:
    """Bij welke aanbieder de advertentie staat. Jan miste dit in het bericht (26-09-2026)."""
    if it.get("kantoor"):
        return str(it["kantoor"])
    b = str(it.get("source") or "")
    if b.startswith("makelaar:"):
        host = b.split(":", 1)[1]
        uit = _kantoornamen().get(host)
        if uit:
            return uit
        naam = host.rsplit(".", 1)[0].replace("-", " ")
        return naam[:1].upper() + naam[1:]
    return {"bp": "Background Properties", "idealista": "Idealista",
            "idealista-zoek": "Idealista"}.get(b, b or "onbekend")


def kaartje(it: dict) -> dict:
    """Eén object als Discord-kaartje: te scannen, met de bron en een link naar de advertentie.

    Waarom dit er is: het oude bericht was één lap tekst waarin per regel de referentie, de wijk, de
    vraagprijs, de maximale prijs, het percentage, het scenario, het resultaat en de marge stonden.
    Dat leest niemand. Nu staan de vier bedragen in vakjes, is de titel aanklikbaar naar de
    advertentie, en staat eronder bij wie hij staat."""
    c = it.get("calc") or {}
    bod = it.get("bod") or {}
    waar = it.get("zone_label") or it.get("area_label") or "Jávea"
    velden = []
    if c.get("result") is not None:
        # Jan 26-09-2026: het resultaat ook als percentage. Het rendement op de kosten is zijn eigen
        # eis (25 %), dus dat getal zegt in één oogopslag of het object die haalt.
        deel = ""
        if c.get("roi_on_costs") is not None:
            deel = f"\n{c['roi_on_costs'] * 100:.0f} % op de kosten"
            if c.get("margin") is not None:
                deel += f" · {c['margin'] * 100:.0f} % marge"
        velden.append({"name": "Resultaat", "value": _eur(c.get("result")) + deel, "inline": True})
    # Jan 26-09-2026: "per maand" mag van het kaartje af. Wat hij wél wil weten is hoe ver de
    # vraagprijs boven het haalbare staat, want dat is de echte onderhandelafstand.
    if bod.get("opening"):
        velden.append({"name": "Openen op", "value": _eur(bod["opening"]), "inline": True})
    if bod.get("walk"):
        velden.append({"name": "Niet hoger dan", "value": _eur(bod["walk"]), "inline": True})
    if bod.get("kloof_pct") is not None and bod["kloof_pct"] > 0.01:
        velden.append({"name": "Vraagprijs te hoog met",
                       "value": f"{bod['kloof_pct'] * 100:.0f} %", "inline": True})
    if c.get("financing_per_5pct"):
        velden.append({"name": f"Rente {c.get('financing_rate', 0) * 100:.0f} %",
                       "value": f"{_eur(c['financing'])}\nelke 5 % meer: {_eur(c['financing_per_5pct'])}",
                       "inline": True})
    velden.append({"name": "Staat bij", "value": _bron(it), "inline": True})
    if it.get("bronnen", 1) > 1:
        velden.append({"name": "Ook bij", "value": ", ".join(
            o.get("bron", "?") for o in (it.get("ook_bij") or []))[:60], "inline": True})
    onder = [str(it.get("ref") or "")]
    if c.get("months"):
        onder.append(f"{c['months']} maanden")
    if it.get("water", {}) and (it.get("water") or {}).get("waarschuwing"):
        onder.append("let op: water")
    kaart = {
        "title": f"{waar} · {_eur(it.get('price'))}"[:250],
        "color": KLEUR.get(it.get("class"), 0x8C918E),
        "description": (it.get("scenario") or "")[:180],
        "fields": velden[:6],
        "footer": {"text": " · ".join(x for x in onder if x)[:120]},
    }
    u = str(it.get("url") or "")
    if u.startswith("http"):
        kaart["url"] = u
    return kaart


def send(env: dict, text: str, kaartjes: list[dict] | None = None) -> str:
    url = env.get("DISCORD_WEBHOOK_URL")
    if not url:
        return "discord: overgeslagen (geen DISCORD_WEBHOOK_URL in .env)"
    chunks = [text[i:i + 1900] for i in range(0, len(text), 1900)][:3]
    try:
        with httpx.Client(timeout=20) as c:
            for n, ch in enumerate(chunks):
                lading = {"content": ch, "username": "TREE Deal Hunter"}
                if kaartjes and n == 0:
                    lading["embeds"] = kaartjes[:MAX_KAARTJES]
                r = c.post(url, json=lading)
                if r.status_code >= 300:
                    return f"discord: fout {r.status_code} {r.text[:120]}"
    except Exception as e:  # noqa: BLE001
        return f"discord: fout {str(e)[:100]}"
    return f"discord: verzonden ({len(chunks)} bericht(en))"


def run(store: Store, run_id: int, items: list[dict], env: dict, report_url: str | None = None,
        deliver: bool = True) -> dict:
    """Bepaalt, verstuurt en registreert de meldingen van deze ronde.

    De eerste keer is een nulmeting: alles wat nu al aan de eis voldoet staat er vaak al weken, en
    dat is geen nieuws. Die ronde wordt alleen vastgelegd, met één korte regel als bericht."""
    baseline = store.con.execute("SELECT COUNT(*) FROM alerts").fetchone()[0] == 0
    found = collect(store, items)
    if not deliver and not baseline:
        # Een proefronde mag de meldingen niet opmaken: dan zou de echte ronde erna niets meer
        # te melden hebben. Alleen laten zien wat er gemeld zou worden.
        log.info("proefronde: %s direct, %s verzamel; niets vastgelegd", len(found["direct"]), len(found["verzamel"]))
        return {"direct": len(found["direct"]), "verzamel": len(found["verzamel"]),
                "status": "proefronde, niet verstuurd en niet vastgelegd",
                "refs": [i.get("ref") for i in found["direct"]][:10]}
    if baseline:
        n = len(found["direct"]) + len(found["verzamel"])
        status = "nulmeting, niet als melding verstuurd"
        if n and deliver:
            status = "nulmeting — " + bezorg(env, f"Meldingen staan aan. Nulmeting: {len(found['direct'])} objecten halen de marge al bij de "
                               f"vraagprijs en {len(found['verzamel'])} zijn haalbaar binnen 30 % korting. "
                                                       f"Vanaf nu meldt het systeem alleen wat daarbij komt.",
                                              "Deal Hunter: meldingen staan aan")
        for tier in ("direct", "verzamel"):
            for it in found[tier]:
                store.add_alert(run_id, int(it["id"]), tier, it.get("class"), it.get("price"),
                                (it.get("max_price") or {}).get("base"), it.get("room"), delivered=status)
        log.info("meldingen: nulmeting met %s objecten", n)
        return {"direct": 0, "verzamel": 0, "nulmeting": n, "status": status, "refs": []}
    # Terugbelafspraken die vandaag aflopen gaan mee in hetzelfde bericht.
    vandaag = datetime.now(config.TZ).date().isoformat()
    try:
        terug = store.herinneringen(vandaag)
    except Exception:  # noqa: BLE001 — een kapotte herinnering mag de meldingen niet tegenhouden
        terug = []
    kop = herinneringen_tekst(terug)
    text = message(found["direct"], found["verzamel"], report_url)
    if kop:
        text = kop + ("\n\n" + text if text else "")
    status = "niets te melden"
    if text:
        onderwerp = (f"Deal Hunter: {len(found['direct'])} sterke kans"
                     f"{'en' if len(found['direct']) != 1 else ''}" if found["direct"]
                     else f"Deal Hunter: {len(found['verzamel'])} binnen onderhandelbereik")
        status = bezorg(env, text, onderwerp,
                        kaartjes_voor(found["direct"], found["verzamel"])) if deliver else "niet verstuurd (dry-run)"
    for tier in ("direct", "verzamel"):
        for it in found[tier]:
            store.add_alert(run_id, int(it["id"]), tier, it.get("class"), it.get("price"),
                            (it.get("max_price") or {}).get("base"), it.get("room"), delivered=status)
    if terug and "verzonden" in status:
        store.herinnering_verstuurd([int(h["listing_id"]) for h in terug])
    log.info("meldingen: %s direct, %s verzamel, %s herinneringen — %s",
             len(found["direct"]), len(found["verzamel"]), len(terug), status)
    return {"direct": len(found["direct"]), "verzamel": len(found["verzamel"]),
            "herinneringen": len(terug), "status": status,
            "refs": [i.get("ref") for i in found["direct"]][:10]}

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

import logging
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
    """Bouwt het Discord-bericht. Geeft None als er niets te melden is."""
    if not direct and not collected:
        return None
    parts: list[str] = []
    if direct:
        parts.append(f"🟢 **{len(direct)} sterke kans{'en' if len(direct) != 1 else ''}** — haalt de marge al bij de vraagprijs.")
        parts += [line(i) for i in direct[:10]]
        parts.append("Controleer perceel en vergunning vóór enig contact. Er gaat niets de deur uit zonder jouw akkoord.")
    if collected:
        parts.append("")
        parts.append(f"🟠 **{len(collected)} binnen onderhandelbereik** — haalbaar tot 30 % onder de vraagprijs.")
        parts += [line(i) for i in collected[:15]]
    if report_url:
        parts.append(f"\nVolledig rapport: {report_url}")
    return "\n".join(parts)


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


def bezorg(env: dict, text: str, onderwerp: str = "Deal Hunter") -> str:
    """Beide kanalen. Eén kanaal dat uitvalt mag het andere niet tegenhouden."""
    return " · ".join((send(env, text), send_email(env, text, onderwerp)))


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


def send(env: dict, text: str) -> str:
    url = env.get("DISCORD_WEBHOOK_URL")
    if not url:
        return "discord: overgeslagen (geen DISCORD_WEBHOOK_URL in .env)"
    chunks = [text[i:i + 1900] for i in range(0, len(text), 1900)][:3]
    try:
        with httpx.Client(timeout=20) as c:
            for ch in chunks:
                r = c.post(url, json={"content": ch, "username": "TREE Deal Hunter"})
                if r.status_code >= 300:
                    return f"discord: fout {r.status_code}"
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
        status = bezorg(env, text, onderwerp) if deliver else "niet verstuurd (dry-run)"
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

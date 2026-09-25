#!/usr/bin/env python3
"""Overzicht van de makelaarskantoren: wie mogen we lezen, bij wie vragen we een feed, wie slaan we over.

  python3 tools/rapport_makelaars.py   →  rapporten/makelaars.html

Bronnen: kader/makelaars.json (de kantoren die door een agent zijn getoetst, met advies),
onderzoek/makelaars/toets-script.json (de kantoren die alleen met het script op robots.txt en
sitemap zijn getoetst) en de database (hoeveel objecten we per kantoor werkelijk hebben gelezen).
"""
from __future__ import annotations

import html
import json
import os
import re
import sys
from datetime import datetime

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

from dh import config  # noqa: E402
from dh.store import Store  # noqa: E402

OUT = config.ROOT / "rapporten" / "makelaars.html"
E = html.escape
VOLGORDE = ["lezen", "feed vragen", "handmatig toetsen", "overslaan"]
KOP = {
    "lezen": ("Lezen: draait mee in de dagelijkse ronde",
              "Robots.txt staat het toe en de voorwaarden verbieden niets, of er zijn geen voorwaarden gevonden. "
              "De lezer haalt hier elke ronde het aanbod op, nooit sneller dan één verzoek per twee seconden, "
              "of trager als de site dat vraagt."),
    "feed vragen": ("Feed vragen: niet lezen, wel benaderen",
                    "Hier verbieden de voorwaarden of robots.txt het automatisch lezen, maar het systeem achter de site kent een "
                    "exportfeed voor samenwerkingspartners. De conceptmail staat klaar; versturen doet Jan."),
    "handmatig toetsen": ("Handmatig toetsen: nog niet beslist",
                          "Alleen met het script gecontroleerd op robots.txt en sitemap, of de voorwaarden zijn nog niet gelezen. "
                          "Pas na die controle wordt het lezen of feed vragen."),
    "overslaan": ("Overslaan", "Geen makelaar, geen aanbod in ons gebied, of lezen mag niet en er is geen feed."),
}


def host(u: str) -> str:
    return re.sub(r"^https?://", "", u or "").replace("www.", "").split("/")[0].lower()


def laad() -> list[dict]:
    mk = json.loads((config.KADER / "makelaars.json").read_text(encoding="utf-8"))
    rows = {host(k["website"]): dict(k, toets="agent") for k in mk.get("kantoren") or []}
    p = config.ROOT / "onderzoek" / "makelaars" / "toets-script.json"
    if p.exists():
        for r in json.loads(p.read_text(encoding="utf-8")):
            h = r.get("host")
            if not h or h in rows:
                continue
            rows[h] = {
                "naam": r.get("naam") or h, "website": r.get("website") or f"https://{h}", "cms": r.get("cms"),
                "advies": r.get("advies") or "handmatig toetsen", "robots": r.get("robots_regels_voor_ster"),
                "voorwaarden": "link gevonden, nog niet gelezen" if r.get("voorwaarden_link") else "geen link gevonden",
                "geschat_aantal": r.get("objectpaginas"), "gebied": f"{r.get('in_gebied_volgens_url', 0)} objectpagina's in ons gebied volgens de URL",
                "opmerking": r.get("toelichting"), "toets": "script", "crawl_delay_s": r.get("crawl_delay"),
            }
    inv = config.ROOT / "onderzoek" / "makelaars" / "inventaris-2026-09-24.json"
    plaats = {}
    if inv.exists():
        for h, g in (json.loads(inv.read_text(encoding="utf-8")).get("gevonden") or {}).items():
            plaats[h] = g.get("plaats")
    store = Store()
    try:
        gelezen = {}
        for r in store.con.execute("SELECT source, COUNT(*) n, SUM(CASE WHEN signals LIKE '%\"alleen_bij_makelaar\": true%' THEN 1 ELSE 0 END) ex "
                                   "FROM listings WHERE source LIKE 'makelaar:%' AND gone_at IS NULL GROUP BY source"):
            gelezen[r["source"].split(":", 1)[1]] = (r["n"], r["ex"])
    finally:
        store.close()
    uit = []
    for h, k in rows.items():
        n, ex = gelezen.get(h, (0, 0))
        k.update({"host": h, "plaats": k.get("plaats") or plaats.get(h) or "", "gelezen": n, "niet_op_portaal": ex})
        uit.append(k)
    uit.sort(key=lambda k: (VOLGORDE.index(k["advies"]) if k["advies"] in VOLGORDE else 9, -(k["gelezen"] or 0), (k["naam"] or "").lower()))
    return uit


CSS = """
:root{color-scheme:light dark;--paper:#f7f5f0;--surface:#fffefb;--sunk:#efebe3;--ink:#2b3331;--ink2:#1c2220;--muted:#69706c;--beige:#b8a07a;
--rule:rgba(43,51,49,.14);--groen:#2f7a55;--groen-bg:#e2f0e8;--blauw:#2f6386;--blauw-bg:#e3edf4;--oranje:#b86e12;--oranje-bg:#f6ead6;--grijs:#8c918e;--grijs-bg:#ecebe7;
--display:"Newsreader","Iowan Old Style",Georgia,serif;--body:"Inter Tight","Helvetica Neue",Arial,system-ui,sans-serif;--mono:"JetBrains Mono",Menlo,monospace}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--paper:#1a201e;--surface:#222a28;--sunk:#2a3230;--ink:#e4e1d9;--ink2:#f3f0e9;--muted:#a3a8a2;--beige:#cbb48d;--rule:rgba(228,225,217,.14);
--groen:#8ccfae;--groen-bg:#1f3529;--blauw:#8dbad8;--blauw-bg:#1f3340;--oranje:#e0b567;--oranje-bg:#3b3020;--grijs:#a9aea9;--grijs-bg:#2b3230}}
:root[data-theme="dark"]{--paper:#1a201e;--surface:#222a28;--sunk:#2a3230;--ink:#e4e1d9;--ink2:#f3f0e9;--muted:#a3a8a2;--beige:#cbb48d;--rule:rgba(228,225,217,.14);
--groen:#8ccfae;--groen-bg:#1f3529;--blauw:#8dbad8;--blauw-bg:#1f3340;--oranje:#e0b567;--oranje-bg:#3b3020;--grijs:#a9aea9;--grijs-bg:#2b3230}
*{box-sizing:border-box}body{margin:0;background:var(--paper);color:var(--ink);font:15px/1.55 var(--body)}
.wrap{max-width:60rem;margin:0 auto;padding:0 1.1rem 4rem}
header{border-bottom:1px solid var(--rule);padding:1.6rem 0 1rem;margin-bottom:1rem}
.eyebrow{font-family:var(--mono);font-size:.68rem;letter-spacing:.18em;text-transform:uppercase;color:var(--beige)}
h1{font-family:var(--display);font-weight:500;font-size:2rem;margin:.3rem 0 .2rem;color:var(--ink2);line-height:1.12}
h2{font-family:var(--display);font-weight:500;font-size:1.3rem;margin:2rem 0 .3rem;color:var(--ink2)}
.sub,.uitleg{color:var(--muted);font-size:.9rem;margin:.2rem 0 .6rem;max-width:46rem}
.tiles{display:grid;grid-template-columns:repeat(auto-fit,minmax(9rem,1fr));gap:.6rem;margin:1rem 0}
.tile{background:var(--surface);border:1px solid var(--rule);border-radius:8px;padding:.6rem .8rem}
.tile b{display:block;font-family:var(--display);font-size:1.6rem;color:var(--ink2);font-weight:500}.tile span{font-size:.8rem;color:var(--muted)}
.wrapx{overflow-x:auto}table{width:100%;border-collapse:collapse;font-size:.86rem}
th,td{text-align:left;padding:.45rem .5rem .45rem 0;border-bottom:1px solid var(--rule);vertical-align:top}
th{font-family:var(--mono);font-size:.64rem;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);font-weight:500}
td.n{text-align:right;font-family:var(--mono);white-space:nowrap}
.pill{display:inline-block;font-size:.7rem;padding:.12rem .5rem;border-radius:99px;background:var(--grijs-bg);color:var(--grijs);white-space:nowrap}
.pill.lezen{background:var(--groen-bg);color:var(--groen)}.pill.feed{background:var(--blauw-bg);color:var(--blauw)}.pill.hand{background:var(--oranje-bg);color:var(--oranje)}
.k{font-weight:600;color:var(--ink2)}.k a{color:inherit;text-decoration-color:var(--beige)}
.w{color:var(--muted);font-size:.8rem;display:block}
details{margin-top:.15rem}summary{cursor:pointer;color:var(--muted);font-size:.78rem}
.opm{font-size:.8rem;color:var(--muted);margin:.25rem 0 0;max-width:38rem}
footer{border-top:1px solid var(--rule);margin-top:2.5rem;padding-top:1rem;font-size:.8rem;color:var(--muted)}
"""


def rij(k: dict) -> str:
    adv = k["advies"]
    cls = {"lezen": "lezen", "feed vragen": "feed", "handmatig toetsen": "hand"}.get(adv, "")
    web = k["website"] if str(k["website"]).startswith("http") else "https://" + str(k["website"])
    delay = f" · {k['crawl_delay_s']:.0f} s tussen verzoeken" if k.get("crawl_delay_s") else ""
    opm = (k.get("opmerking") or "")[:420]
    robots = (k.get("robots") or "")[:400]
    return f"""<tr>
<td><span class="k"><a href="{E(web)}" target="_blank" rel="noopener noreferrer">{E(k['naam'])}</a></span><span class="w">{E(k['host'])}{E(delay)}</span></td>
<td>{E(k.get('plaats') or '—')}</td>
<td>{E(k.get('cms') or '—')}</td>
<td>{E(k.get('voorwaarden') or '—')}</td>
<td class="n">{k.get('geschat_aantal') if k.get('geschat_aantal') not in (None, '') else '—'}</td>
<td class="n">{k['gelezen'] or '—'}</td>
<td class="n">{k['niet_op_portaal'] or '—'}</td>
<td><span class="pill {cls}">{E(adv)}</span><span class="w">{E(k.get('toets') == 'script' and 'script' or 'agent')}</span>
{f'<details><summary>waarom</summary><p class="opm">{E(opm)}</p><p class="opm">{E(robots)}</p></details>' if opm or robots else ''}</td>
</tr>"""


def main() -> int:
    rows = laad()
    per = {a: [k for k in rows if k["advies"] == a] for a in VOLGORDE}
    overig = [k for k in rows if k["advies"] not in VOLGORDE]
    gelezen_tot = sum(k["gelezen"] for k in rows)
    ex_tot = sum(k["niet_op_portaal"] for k in rows)
    secties = ""
    for a in VOLGORDE:
        ks = per[a] + (overig if a == "handmatig toetsen" else [])
        if not ks:
            continue
        titel, uitleg = KOP[a]
        secties += f"""<h2>{E(titel)} <span class="sub" style="display:inline">({len(ks)})</span></h2><p class="uitleg">{E(uitleg)}</p>
<div class="wrapx"><table><tr><th>Kantoor</th><th>Plaats</th><th>Systeem</th><th>Voorwaarden</th><th class="n">Aanbod</th><th class="n">Gelezen</th><th class="n">Niet op portalen</th><th>Advies</th></tr>
{''.join(rij(k) for k in ks)}</table></div>"""
    doc = f"""<!doctype html><html lang="nl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Makelaars in beeld</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Newsreader:opsz,wght@6..72,400;6..72,500&family=Inter+Tight:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap">
<style>{CSS}</style></head><body><div class="wrap">
<header><div class="eyebrow">TREE Deal Hunter · bronnen</div><h1>Makelaars in Jávea, Benitachell en Moraira</h1>
<p class="sub">Welke kantoren de dealmaker mag uitlezen, bij wie we een feed vragen, en wie afvalt. Stand {E(datetime.now(config.TZ).strftime('%d-%m-%Y %H:%M'))}.</p></header>
<div class="tiles">
<div class="tile"><b>{len(rows)}</b><span>kantoren met eigen site</span></div>
<div class="tile"><b>{len(per['lezen'])}</b><span>mogen gelezen worden</span></div>
<div class="tile"><b>{len(per['feed vragen'])}</b><span>feed vragen</span></div>
<div class="tile"><b>{len(per['handmatig toetsen']) + len(overig)}</b><span>nog handmatig toetsen</span></div>
<div class="tile"><b>{gelezen_tot}</b><span>objecten al ingelezen</span></div>
<div class="tile"><b>{ex_tot}</b><span>niet gezien op de portalen die wij volgen</span></div>
</div>
<p class="uitleg">Toets per kantoor: robots.txt (mag een gewone lezer de aanbodpagina's openen?), de gebruiksvoorwaarden (verbieden ze automatisch lezen?), de sitemap en het systeem achter de site. "Agent" betekent dat een onderzoeksagent de site en de voorwaarden heeft gelezen; "script" dat alleen robots.txt, sitemap en homepage zijn gecontroleerd en de voorwaarden nog niet.
"Niet gezien op de portalen die wij volgen" betekent: niet gevonden in de feed van Background Properties en niet in onze Idealista-oogst. Wij zien maar een deel van Idealista, dus dat is geen bewijs dat een object nergens anders staat.</p>
{secties}
<footer><p>Er wordt alleen gelezen waar het mag. Waar het niet mag wordt niets omzeild; daar vragen we het kantoor om zijn eigen exportfeed. Er is met geen enkel kantoor contact opgenomen; dat doet Jan.</p></footer>
</div></body></html>"""
    OUT.write_text(doc, encoding="utf-8")
    print(f"geschreven: {OUT} ({len(rows)} kantoren: lezen {len(per['lezen'])}, feed {len(per['feed vragen'])}, "
          f"handmatig {len(per['handmatig toetsen']) + len(overig)}, overslaan {len(per['overslaan'])})")
    return 0


if __name__ == "__main__":
    sys.exit(main())

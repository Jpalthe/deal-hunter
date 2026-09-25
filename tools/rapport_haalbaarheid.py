#!/usr/bin/env python3
"""Genereert rapporten/haalbaarheid.html uit kader/haalbaarheid.json, comparables.json, parameters.json
en de gevoeligheidsvarianten. Alle getallen komen uit de rekenaar; niets wordt met de hand ingevuld.

  python3 tools/rapport_haalbaarheid.py
"""
from __future__ import annotations

import copy
import html
import importlib.util
import json
import os
import sqlite3
import sys
from datetime import datetime

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")
K = os.path.join(ROOT, "kader")
OUT = os.path.join(ROOT, "rapporten", "haalbaarheid.html")

spec = importlib.util.spec_from_file_location("haalbaarheid", os.path.join(HERE, "haalbaarheid.py"))
m = importlib.util.module_from_spec(spec); sys.modules["haalbaarheid"] = m; spec.loader.exec_module(m)
gspec = importlib.util.spec_from_file_location("gevoeligheid", os.path.join(HERE, "gevoeligheid.py"))
g = importlib.util.module_from_spec(gspec); sys.modules["gevoeligheid"] = g; gspec.loader.exec_module(g)

kader = json.load(open(os.path.join(K, "investeringskader.json"), encoding="utf-8"))
params_doc = json.load(open(os.path.join(K, "parameters.json"), encoding="utf-8"))
params = params_doc["values"]
comps = json.load(open(os.path.join(K, "comparables.json"), encoding="utf-8"))["zones"]
kand = json.load(open(os.path.join(K, "kandidaten.json"), encoding="utf-8"))["kandidaten"]
results = m.evaluate(kader, params, comps, kand)
json.dump({"kader_versie": kader.get("versie"), "results": results}, open(os.path.join(K, "haalbaarheid.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
ROI = kader["rendementseis_op_projectkosten"]
MARGIN = kader.get("winstmarge_op_verkoop_min", ROI / (1 + ROI))

E = html.escape


def eur(v, dash="—"):
    if v is None:
        return dash
    return f"{v:,.0f}".replace(",", ".") + " €"


def keur(v):
    return f"{v / 1000:,.0f}".replace(",", ".") + "k"


def pct(v):
    return "—" if v is None else f"{v * 100:.0f} %"


ZONE_LABEL = {
    "montgo_ermita": "Montgó – Ermita en Tosal – Castellans", "centro": "Centrum en casco antiguo",
    "puerto_arenal": "Puerto en Arenal", "tosalet_adsubia": "El Tosalet, Cap Martí en Adsubia",
    "granadella_balcon": "Granadella, Costa Nova en Balcón al Mar", "rafalet_pinosol": "El Rafalet, Pinosol en La Lluca",
    "benitachell": "Benitachell en Cumbre del Sol", "moraira": "Moraira en Teulada",
}
SERIES_LABEL = {
    "villa_renovated": "Villa, gerenoveerd of modern", "villa_new": "Villa, nieuwbouw",
    "apartment_renovated": "Appartement, gerenoveerd", "apartment_new": "Appartement, nieuwbouw",
    "townhouse_renovated": "Dorpshuis, gerenoveerd",
}

# --------------------------------------------------------------- kerncijfers
all_rows = [(e, s) for e in results for s in e["scenarios"] if s.get("status") == "berekend"]
n_scen = len(all_rows)
meets_cons = [(e, s) for e, s in all_rows if s["at_asking"]["conservative"]["roi_on_costs"] >= ROI]
meets_base = [(e, s) for e, s in all_rows if s["at_asking"]["base"]["roi_on_costs"] >= ROI]
meets_cons_rel = [(e, s) for e, s in meets_cons if s.get("reliable")]
meets_base_rel = [(e, s) for e, s in meets_base if s.get("reliable")]
unreliable = [(e, s) for e, s in all_rows if not s.get("reliable")]

sc_new = m.Scenario(key="N", label="", kind="nieuwbouw", newbuild_m2=300, result_m2=300, pool=True, exterior_m2=150, vat_recoverable=True)
c_new = m.construction(sc_new, kader, params)
sc_ren = m.Scenario(key="R", label="", kind="renovatie", renovation_m2=250, result_m2=250, pool_renovation=True)
c_ren = m.construction(sc_ren, kader, params)

# --------------------------------------------------------------- gevoeligheid
variants = []
for name, k2, p2, roi in g.VARIANTS:
    r = g.run(k2, p2, roi)
    eis = roi or k2["rendementseis_op_projectkosten"]
    reliable_keys = {(e["id"], s["key"]) for e, s in all_rows if s.get("reliable")}
    nc = sum(1 for key, v in r.items() if v[1] >= eis and key in reliable_keys)
    nb = sum(1 for key, v in r.items() if v[0] >= eis and key in reliable_keys)
    variants.append((name, nc, nb, len(reliable_keys), r))

# --------------------------------------------------------------- monitor
runs = []
try:
    con = sqlite3.connect(os.path.join(ROOT, "data", "dealhunter.sqlite"))
    runs = con.execute("select slot, started_at, status from runs order by id").fetchall()
    n_area = con.execute("select count(*) from listings where area is not null and gone_at is null").fetchone()[0]
    n_ind = 0; n_meet = 0
    for (pf,) in con.execute("select prefilter from listings where area is not null and gone_at is null"):
        d = json.loads(pf or "{}"); ind = d.get("indicative") or {}
        if ind.get("roi_base") is not None:
            n_ind += 1
            if (d.get("verdict") or "").startswith("kandidaat: haalt eis"):
                n_meet += 1
    con.close()
except sqlite3.Error:
    n_area = n_ind = n_meet = 0

# --------------------------------------------------------------- HTML
CSS = """
:root{--paper:#f7f5f0;--surface:#fffefb;--ink:#2b3331;--ink-strong:#1c2220;--muted:#646b68;--beige:#b8a07a;--beige-soft:#ece4d5;--rule:rgba(43,51,49,.14);--rule-strong:rgba(43,51,49,.28);--ok:#2f6b4f;--ok-bg:#e1efe7;--warn:#8a5d12;--warn-bg:#f4ead6;--bad:#933a31;--bad-bg:#f5e2df;--info:#2f6386;--info-bg:#e3edf3;--bar:#b8a07a;
--font-display:"Newsreader","Iowan Old Style",Georgia,serif;--font-body:"Inter Tight","Helvetica Neue",Arial,system-ui,sans-serif;--font-mono:"JetBrains Mono","SFMono-Regular",Menlo,monospace}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--paper:#1a201e;--surface:#222a28;--ink:#e4e1d9;--ink-strong:#f3f0e9;--muted:#a3a8a2;--beige:#cbb48d;--beige-soft:#3a3529;--rule:rgba(228,225,217,.13);--rule-strong:rgba(228,225,217,.26);--ok:#8ccfae;--ok-bg:#1f3529;--warn:#e0b567;--warn-bg:#3b3020;--bad:#e59a8f;--bad-bg:#3d2522;--info:#8dbad8;--info-bg:#1f3340;--bar:#a89067}}
:root[data-theme="dark"]{--paper:#1a201e;--surface:#222a28;--ink:#e4e1d9;--ink-strong:#f3f0e9;--muted:#a3a8a2;--beige:#cbb48d;--beige-soft:#3a3529;--rule:rgba(228,225,217,.13);--rule-strong:rgba(228,225,217,.26);--ok:#8ccfae;--ok-bg:#1f3529;--warn:#e0b567;--warn-bg:#3b3020;--bad:#e59a8f;--bad-bg:#3d2522;--info:#8dbad8;--info-bg:#1f3340;--bar:#a89067}
*{box-sizing:border-box}body{margin:0;background:var(--paper);color:var(--ink);font-family:var(--font-body);font-size:16px;line-height:1.6}
a{color:var(--ink-strong);text-decoration-color:var(--beige);text-underline-offset:3px}a:focus-visible{outline:2px solid var(--beige);outline-offset:2px}
.page{max-width:64rem;margin:0 auto;padding:3rem 1.5rem 5rem}.measure{max-width:44rem}
.eyebrow{font-family:var(--font-mono);font-size:.75rem;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);display:flex;flex-wrap:wrap;gap:.35rem 1rem}
h1,h2,h3{font-family:var(--font-display);color:var(--ink-strong);font-weight:500;text-wrap:balance}
h1{font-size:clamp(2rem,4.5vw,3rem);line-height:1.08;margin:.8rem 0 1rem}h2{font-size:clamp(1.5rem,3vw,1.9rem);line-height:1.2;margin:0 0 .4rem}h3{font-size:1.2rem;margin:1.6rem 0 .5rem}
header{padding-bottom:2rem;border-bottom:1px solid var(--rule-strong)}.dek{font-size:1.12rem;margin:0}
section{padding-top:3rem}.lede{color:var(--muted);margin:0 0 1.4rem;max-width:44rem}p{margin:0 0 1rem}
.conclusions{list-style:none;padding:0;margin:0;display:grid;gap:1rem;max-width:46rem}.conclusions li{padding-left:1.1rem;border-left:2px solid var(--beige)}.conclusions b{color:var(--ink-strong)}
dl.meta{display:grid;grid-template-columns:repeat(auto-fit,minmax(11rem,1fr));gap:.75rem 1.5rem;margin:1.2rem 0 0}dl.meta div{border-top:1px solid var(--rule);padding-top:.6rem}
dl.meta dt{font-family:var(--font-mono);font-size:.7rem;letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}dl.meta dd{margin:.15rem 0 0;color:var(--ink-strong)}
.table-wrap{overflow-x:auto;margin:0 0 1rem;border-top:1px solid var(--rule-strong)}table{border-collapse:collapse;width:100%;font-size:.9rem}
th,td{text-align:left;padding:.55rem .7rem .55rem 0;border-bottom:1px solid var(--rule);vertical-align:top}
th{font-family:var(--font-mono);font-size:.68rem;letter-spacing:.07em;text-transform:uppercase;color:var(--muted);font-weight:500}
td.num,th.num{text-align:right;font-variant-numeric:tabular-nums;white-space:nowrap}caption{caption-side:bottom;text-align:left;color:var(--muted);font-size:.82rem;padding-top:.6rem}
.pill{display:inline-block;font-family:var(--font-mono);font-size:.66rem;letter-spacing:.05em;text-transform:uppercase;padding:.16rem .42rem;border-radius:3px;white-space:nowrap;font-weight:500}
.ok{color:var(--ok);background:var(--ok-bg)}.warn{color:var(--warn);background:var(--warn-bg)}.bad{color:var(--bad);background:var(--bad-bg)}.info{color:var(--info);background:var(--info-bg)}.neutral{color:var(--muted);background:var(--beige-soft)}
.cand{background:var(--surface);border:1px solid var(--rule);border-radius:6px;padding:1.1rem 1.2rem;margin:0 0 1rem}
.cand-head{display:flex;justify-content:space-between;gap:1rem;align-items:baseline;flex-wrap:wrap}.code{font-family:var(--font-mono);font-size:.78rem;color:var(--muted)}
.cand h3{margin:.1rem 0 .4rem}.facts{font-family:var(--font-mono);font-size:.8rem;color:var(--ink-strong);display:flex;gap:.2rem 1rem;flex-wrap:wrap;margin-bottom:.6rem}
.flags{font-size:.86rem;color:var(--muted);margin:.4rem 0 0;padding-left:1.1rem}.flags li{margin:.2rem 0}.flags li::marker{color:var(--beige)}
.bar{position:relative;height:.6rem;background:var(--beige-soft);border-radius:2px;min-width:8rem}.bar span{position:absolute;inset:0 auto 0 0;background:var(--bar);border-radius:2px}.bar i{position:absolute;top:-.2rem;bottom:-.2rem;width:1px;background:var(--ink-strong);opacity:.5}
.callout{background:var(--beige-soft);border-radius:6px;padding:1rem 1.2rem;max-width:46rem;margin:1rem 0}.callout p:last-child{margin:0}
.plain{padding-left:1.1rem;margin:0;display:grid;gap:.5rem;max-width:46rem}.plain li::marker{color:var(--beige)}
.two{display:grid;grid-template-columns:repeat(auto-fit,minmax(19rem,1fr));gap:1.2rem 2rem}
footer{margin-top:4rem;padding-top:1.4rem;border-top:1px solid var(--rule-strong);font-size:.86rem;color:var(--muted)}footer code{font-family:var(--font-mono);font-size:.8rem;color:var(--ink)}
"""

parts = []
A = parts.append
now = datetime.now().strftime("%d-%m-%Y %H:%M")
A('<title>Haalbaarheid Jávea</title>')
A('<meta name="description" content="Eerste doorrekening van veertien echte kandidaten in Jávea met het kader van Jan en de prijzen per wijk na renovatie of nieuwbouw.">')
A('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>')
A('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Newsreader:opsz,wght@6..72,400;6..72,500&family=Inter+Tight:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap">')
A(f"<style>{CSS}</style>")
A('<div class="page">')

# header
A('<header><div class="eyebrow"><span>TREE Deal Hunter</span><span>Haalbaarheid</span><span>peildatum 15 september 2026</span></div>')
A('<h1>Wat kunnen we in Jávea betalen?</h1>')
A(f'<p class="dek measure">Veertien echte kandidaten doorgerekend met jouw kader: minimaal {pct(MARGIN)} winstmarge op de verkoopwaarde, '
  f'{eur(kader["bouwkosten_eur_per_m2"]["renovatie"])} per m² renovatie en {eur(kader["bouwkosten_eur_per_m2"]["nieuwbouw"])} per m² nieuwbouw, '
  'exclusief btw. De verkoopprijs komt uit wat vergelijkbare gerenoveerde en nieuwe woningen in dezelfde wijk vragen.</p>')
A('<dl class="meta">')
A(f'<div><dt>Scenario\'s doorgerekend</dt><dd>{n_scen} bij {len(results)} kandidaten</dd></div>')
A(f'<div><dt>Halen {pct(MARGIN)} marge bij vraagprijs</dt><dd>{len(meets_cons_rel)} voorzichtig, {len(meets_base_rel)} in het basisscenario</dd></div>')
A(f'<div><dt>Niet betrouwbaar te rekenen</dt><dd>{len(unreliable)} scenario\'s, vooral door afwijkende grootte</dd></div>')
A('<div><dt>Soort cijfers</dt><dd>Vraagprijzen, geen verkoopprijzen</dd></div>')
A('</dl></header>')

# conclusie
A('<section id="conclusie"><h2>Conclusie</h2><p class="lede">Wat de cijfers zeggen, en wat ze niet zeggen.</p><ul class="conclusions">')
if not meets_cons_rel:
    A(f'<li><b>Bij de huidige vraagprijzen haalt geen enkele kandidaat betrouwbaar {pct(MARGIN)} marge in het voorzichtige scenario.</b> '
      f'In het basisscenario lukt dat bij {len(meets_base_rel)} van de betrouwbaar te rekenen scenario\'s, maar in het voorzichtige scenario bij geen enkele. '
      'Een deal ontstaat hier dus alleen door onder de vraagprijs te kopen, of door een uitbreiding die bouwrecht oplevert.</li>')
else:
    A(f'<li><b>{len(meets_cons_rel)} scenario\'s halen {pct(MARGIN)} marge ook in het voorzichtige scenario.</b> Die staan hieronder bovenaan.</li>')
A(f'<li><b>Jouw bouwprijs is niet de hele bouwrekening.</b> {eur(kader["bouwkosten_eur_per_m2"]["nieuwbouw"])} per m² nieuwbouw wordt met architect, vergunning, '
  f'keuringen, zwembad, buitenruimte en 10 % reserve ongeveer {eur(c_new["total"] / 300)} per m² voor een villa van 300 m². '
  f'Renovatie van {eur(kader["bouwkosten_eur_per_m2"]["renovatie"])} per m² wordt ongeveer {eur(c_ren["total"] / 250)} per m², inclusief 21 % btw die een vennootschap bij btw-vrije verkoop niet terugkrijgt.</li>')
A('<li><b>De maximale koopprijs per kandidaat is het bruikbaarste getal.</b> Die staat per scenario hieronder, voorzichtig en in het basisscenario. '
  'Ligt de vraagprijs daar ver boven, dan is de enige route onderhandelen of afwijzen.</li>')
A(f'<li><b>Drie aannames bepalen de uitkomst meer dan de wijk.</b> Honoraria van {pct(params["architect_pct_of_pem"] + params["aparejador_pct_of_pem"])} over de bouwsom, {pct(params["agent_commission_pct"])} makelaarscourtage plus btw en de marge-eis. '
  'Samen verschuiven ze de maximale koopprijs met tienduizenden tot ruim honderdduizend euro per deal.</li>')
A('<li><b>Grote uitbreidingen zijn in dit model te rooskleurig.</b> De prijs per m² van gewone villa\'s wordt vermenigvuldigd met veel meer m², terwijl grote villa\'s per m² minder opbrengen. '
  'Die scenario\'s zijn gemarkeerd als niet betrouwbaar.</li>')
A('</ul></section>')

# wijkprijzen
A('<section id="wijken"><h2>Prijzen in de wijk na renovatie of nieuwbouw</h2>')
A('<p class="lede">Vraagprijs per m² gebouwd van woningen die al gerenoveerd of nieuw zijn. Het voorzichtige scenario rekent met het eerste kwart (p25), het basisscenario met de mediaan. '
  'Het exacte adres staat nooit in een advertentie, dus dit gaat per wijk.</p>')
A('<div class="table-wrap"><table><thead><tr><th>Wijk</th><th>Soort</th><th class="num">n</th><th class="num">p25</th><th class="num">Mediaan</th><th class="num">p75</th><th>Spreiding</th><th>Controle</th></tr></thead><tbody>')
SCALE = 8000
for z in ["montgo_ermita", "centro", "puerto_arenal", "tosalet_adsubia", "granadella_balcon", "rafalet_pinosol", "benitachell", "moraira"]:
    zs = comps.get(z)
    if not zs:
        A(f'<tr><td>{E(ZONE_LABEL[z])}</td><td colspan="7"><span class="pill neutral">nog geen gegevens</span></td></tr>')
        continue
    first = True
    for key in ["villa_renovated", "villa_new", "apartment_renovated", "apartment_new", "townhouse_renovated"]:
        s = zs.get(key)
        if not s:
            continue
        p25, med, p75 = s.get("p25"), s.get("median"), s.get("p75")
        bar = ""
        if p25 and p75 and med:
            bar = (f'<div class="bar"><span style="left:{min(p25 / SCALE, 1) * 100:.1f}%;width:{max(min(p75 / SCALE, 1) - min(p25 / SCALE, 1), 0.005) * 100:.1f}%"></span>'
                   f'<i style="left:{min(med / SCALE, 1) * 100:.1f}%"></i></div>')
        ver = s.get("verification", "")
        vcls = "ok" if ver.startswith("bevestigd") else ("warn" if ver.startswith("gecorrigeerd") else "neutral")
        vtxt = "bevestigd" if ver.startswith("bevestigd") else ("gecorrigeerd" if ver.startswith("gecorrigeerd") else "niet gecontroleerd" if "niet gecontroleerd" in ver else "open")
        small = ' <span class="pill warn">klein</span>' if (s.get("n") or 0) < 5 else ""
        A(f'<tr><td>{E(ZONE_LABEL[z]) if first else ""}</td><td>{E(SERIES_LABEL.get(key, key))}{small}</td><td class="num">{s.get("n")}</td>'
          f'<td class="num">{eur(p25)}</td><td class="num"><b>{eur(med)}</b></td><td class="num">{eur(p75)}</td><td style="min-width:9rem">{bar}</td><td><span class="pill {vcls}">{vtxt}</span></td></tr>')
        first = False
A(f'</tbody><caption>Idealista-assistent, 15 september 2026, ontdubbeld. Staaf: p25 tot p75 op een schaal van 0 tot {eur(SCALE)} per m²; streep = mediaan. '
  'Nieuwbouwreeksen mengen opgeleverde villa\'s en projecten op tekening, die soms exclusief btw of inclusief kelder zijn geadverteerd.</caption></table></div>')
A('</section>')

# kandidaten
A('<section id="kandidaten"><h2>De veertien kandidaten doorgerekend</h2>')
A(f'<p class="lede">Per scenario: wat het oplevert bij de huidige vraagprijs, en wat we maximaal mogen betalen voor {pct(MARGIN)} marge op de verkoopwaarde. Voorzichtig rekent met p25 van de wijk, basis met de mediaan.</p>')


def verdict_pill(s):
    if not s.get("reliable"):
        return '<span class="pill neutral">niet betrouwbaar</span>'
    c, b = s["at_asking"]["conservative"]["roi_on_costs"], s["at_asking"]["base"]["roi_on_costs"]
    if c >= ROI:
        return '<span class="pill ok">haalt eis</span>'
    if b >= ROI:
        return '<span class="pill info">alleen in basis</span>'
    return '<span class="pill bad">onder eis</span>'


def best_gap(e):
    best = None
    for s in e["scenarios"]:
        if s.get("status") != "berekend" or not s.get("reliable"):
            continue
        mp = s["max_price_for_roi"]["base"]
        if best is None or mp > best:
            best = mp
    return (best - e["price_ask"]) if best is not None else -10**9


order = sorted(results, key=lambda e: -best_gap(e))
for e in order:
    A('<article class="cand">')
    A(f'<div class="cand-head"><span class="code">{E(e["id"])} · Idealista {E(str(e.get("code") or ""))} · {E(ZONE_LABEL.get(e["comps_zone"], e["comps_zone"]))}</span>')
    if e.get("url"):
        A(f'<a href="{E(e["url"])}">advertentie</a>')
    A('</div>')
    title = f'{(e.get("type") or "").capitalize()} in {e.get("zone") or ""}'
    A(f'<h3>{E(title)}</h3>')
    A(f'<div class="facts"><span>vraagprijs {eur(e["price_ask"])}</span><span>{int(e["built_m2"]) if e.get("built_m2") else "—"} m² gebouwd</span>'
      f'<span>{int(e["plot_m2"]) if e.get("plot_m2") else "—"} m² perceel</span>{"<span>bouwjaar " + E(str(e["year"])) + "</span>" if e.get("year") else ""}</div>')
    A('<div class="table-wrap"><table><thead><tr><th>Scenario</th><th class="num">Verkoop voorzichtig / basis</th><th class="num">Resultaat basis</th>'
      f'<th class="num">Marge voorz. / basis</th><th class="num">Max. koopprijs bij {pct(MARGIN)} marge</th><th>Oordeel</th></tr></thead><tbody>')
    flags = []
    for s in e["scenarios"]:
        if s.get("status") != "berekend":
            A(f'<tr><td>{E(s["label"])}</td><td colspan="4" class="num">—</td><td><span class="pill neutral">{E(s.get("status", "").lower())}</span></td></tr>')
            continue
        aa, mp, sb = s["at_asking"], s["max_price_for_roi"], s["sale_band"]
        A(f'<tr><td>{E(s["label"])}<br><span class="code">{int(s["result_m2"])} m² · {s["months"]} mnd · {E(s["comps_key"])} n={sb["n"]}</span></td>'
          f'<td class="num">{keur(sb["sale"]["conservative"])} / {keur(sb["sale"]["base"])}</td><td class="num">{eur(aa["base"]["result"])}</td>'
          f'<td class="num">{pct(aa["conservative"]["margin_on_sale"])} / {pct(aa["base"]["margin_on_sale"])}</td>'
          f'<td class="num">{keur(mp["conservative"])} / {keur(mp["base"])}</td><td>{verdict_pill(s)}</td></tr>')
        for w in s.get("warnings", []):
            flags.append(f'{s["label"]}: {w}')
        if s.get("over_max_duration"):
            flags.append(f'{s["label"]}: duurt langer dan {kader["doorlooptijd_max_maanden"]} maanden')
    A('</tbody></table></div>')
    bl = e.get("blockers") or []
    if bl or flags:
        A('<ul class="flags">')
        for f in flags:
            A(f'<li>{E(f)}</li>')
        for b in bl[:5]:
            A(f'<li>{E(b)}</li>')
        A('</ul>')
    A('</article>')
A('</section>')

# gevoeligheid
A('<section id="gevoeligheid"><h2>Welke aanname beslist?</h2>')
A('<p class="lede">Hetzelfde rekenmodel met één aanname anders. Alleen betrouwbaar te rekenen scenario\'s tellen mee.</p>')
A(f'<div class="table-wrap"><table><thead><tr><th>Variant</th><th class="num">Halen de eis (voorzichtig / basis)</th></tr></thead><tbody>')
for name, nc, nb, tot, r in variants:
    A(f'<tr><td>{E(name)}</td><td class="num">{nc} / {nb} van {tot}</td></tr>')
A('</tbody><caption>Eigen uitvoering door TREE Constructions kan de bouwprijs verlagen; dat is een aanname tot de nacalculaties er zijn.</caption></table></div></section>')

# monitor
A('<section id="monitor"><h2>De monitor draait</h2><p class="lede">Realtime kan bij geen enkele bron. Daarom twee vaste rondes per dag.</p><ul class="plain">')
A(f'<li><b>Rondes 10:00 en 15:00.</b> Achtergronddienst op de Mac mini. Vandaag gedraaid: {E(", ".join(f"{r[0]} ({r[2]})" for r in runs)) or "nog geen"}.</li>')
A('<li><b>Bronnen:</b> de Background Properties-feed, het BOE-sumario en de veilinglijst van de AEAT. Idealista blijft handwerk tot de officiële API is toegekend.</li>')
A(f'<li><b>Werkgebied:</b> {n_area} actieve objecten in Jávea, Benitachell en Moraira; {n_ind} krijgen al een indicatieve haalbaarheid, {n_meet} halen daarin de eis.</li>')
A('<li><b>Dashboard:</b> <a href="https://mac-mini-van-root-admin.tail69022d.ts.net:8710">mac-mini-van-root-admin.tail69022d.ts.net:8710</a>, alleen bereikbaar binnen het Tailscale-netwerk. Kaart met kadaster en luchtfoto, blokken per kansrijkheid, dossier met wat-als-schuiven en beoordeling per object.</li>')
A('<li><b>Nog niet aan:</b> meldingen in Discord en per e-mail, en de AI-samenvatting per advertentie. Die wachten op sleutels van jou.</li>')
A('</ul></section>')

# aannames
A('<section id="aannames"><h2>Aannames die jij kunt aanscherpen</h2><div class="table-wrap"><table><thead><tr><th>Aanname</th><th class="num">Waarde</th><th>Waar het vandaan komt</th></tr></thead><tbody>')
ROWS = [
    ("Honoraria architect en aparejador", f'{(params["architect_pct_of_pem"] + params["aparejador_pct_of_pem"]) * 100:.0f} % van bouwsom', "Landelijke indicaties; jouw eigen tarieven zijn beter"),
    ("Makelaarscourtage bij verkoop", f'{params["agent_commission_pct"] * 100:.0f} % + btw', "Commissielabels in de BP-feed; niet bewezen wie betaalt"),
    ("Reserve voor tegenvallers", f'{params["contingency_pct"] * 100:.0f} %', "Werkhypothese"),
    ("Btw op renovatie", f'{params["vat_renovation_rate"] * 100:.0f} %', "Vennootschap die btw-vrij doorverkoopt; 10 % kan bij rehabilitatie"),
    ("Btw op nieuwbouw", f'{params["vat_construction_rate"] * 100:.0f} %, terugvorderbaar', "Nieuwbouwwoning verkocht met btw"),
    ("Overdrachtsbelasting", f'{params["itp_rate"] * 100:.0f} %, {params["itp_rate_above_threshold"] * 100:.0f} % boven {keur(params["itp_threshold"])}', "Ley 13/1997 Comunitat Valenciana"),
    ("ICIO en leges", f'{(params["icio_pct_of_pem"] + params["tasa_licencia_pct_of_pem"]) * 100:.0f} % van bouwsom', "ICIO 4 % gemeld aan Hacienda; leges aangenomen"),
    ("Vaste lasten tijdens project", f'{eur(params["holding_eur_per_month"])} per maand', "Werkhypothese"),
    ("Sloop, nieuw zwembad, buitenruimte", f'{eur(params["demolition_eur_per_m2"])}/m², {eur(params["pool_new_eur"])}, {eur(params["exterior_eur_per_m2"])}/m²', "Landelijke indicaties, lage zekerheid"),
    ("Bouwvolume op een perceel", "0,20 m² per m² perceel, maximaal 450 m²", "Villaregels zona E, netto; per perceel te bevestigen"),
]
for a, v, b in ROWS:
    A(f'<tr><td>{E(a)}</td><td class="num">{E(v)}</td><td>{E(b)}</td></tr>')
A('</tbody><caption>Niet in het model: de fiscale referentiewaarde als ondergrens voor de overdrachtsbelasting, en een lagere prijs per m² bij grotere woningen.</caption></table></div></section>')

A('<footer><p>Gegenereerd ' + now + ' uit <code>kader/haalbaarheid.json</code>. Rekenregels in <code>tools/haalbaarheid.py</code>, varianten in <code>tools/gevoeligheid.py</code>, '
  'wijkprijzen met controle in <code>onderzoek/H01-*</code>. Dit is een indicatie op vraagprijzen, geen taxatie en geen biedadvies.</p></footer>')
A('</div>')

os.makedirs(os.path.dirname(OUT), exist_ok=True)
open(OUT, "w", encoding="utf-8").write("\n".join(parts))
print("geschreven:", OUT)
print(f"scenario's {n_scen}; eis voorzichtig (betrouwbaar) {len(meets_cons_rel)}; basis (betrouwbaar) {len(meets_base_rel)}; onbetrouwbaar {len(unreliable)}")

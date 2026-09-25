#!/usr/bin/env python3
"""Mobiele momentopname van de Deal Hunter: één bestand, werkt zonder Tailscale en zonder server.

Leest dezelfde gegevens als het dashboard (SQLite + kader) en schrijft rapporten/mobiel.html.
Geen kaart: kaarttegels laden niet in een gepubliceerde pagina. De kaart staat op het dashboard.

  python3 tools/rapport_mobiel.py
"""
from __future__ import annotations

import html
import json
import os
import sys
from datetime import datetime

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

from dh import config, dashboard, feasibility, focus, summary  # noqa: E402
from dh.store import Store  # noqa: E402

OUT = config.ROOT / "rapporten" / "mobiel.html"
E = html.escape


def num(v) -> str:
    """Getal met punt als duizendtalscheiding."""
    return "—" if v is None else f"{v:,.0f}".replace(",", ".")


def eur(v) -> str:
    return "—" if v is None else num(v) + " €"

store = Store()
# Dezelfde focus als de app, anders staat hier 502 en op de telefoon 167 en weet je niet meer welk
# getal klopt. Volgorde ook gelijk: winst per maand (Jan, 25-09-2026).
_ev7 = summary.events_since(store, 7)
_ctx = summary.bouw_ctx(store)
_alles = [summary.listing_summary(store, r, _ev7, _ctx) for r in focus.rijen(store)]
items = [i for i in _alles if i.get("tab") == focus.KANSEN and i.get("merk") != "weg"]
items.sort(key=lambda x: -(x.get("per_maand") or -1e12))
store.close()

auction_rows = dashboard.auctions()
zones = dashboard.zones()
kader, params, comps, _ = feasibility.inputs()
MARGIN = kader.get("winstmarge_op_verkoop_min", 0.20)

for it in items:
    it["price_m2"] = round(it["price"] / it["built_m2"]) if (it["price"] and it["built_m2"]) else None
    it["price_m2_plot"] = round(it["price"] / it["plot_m2"]) if (it["price"] and it["plot_m2"] and not it["built_m2"]) else None

order = {"groen": 0, "blauw": 1, "oranje": 2, "onzeker": 3, "grijs": 4, "geen": 5}
items.sort(key=lambda x: (order.get(x["class"], 9), -(x["room"] or -9)))

data = {
    "generated": datetime.now(config.TZ).strftime("%d-%m-%Y %H:%M"),
    "margin": MARGIN,
    "kader": {"reno": kader["bouwkosten_eur_per_m2"]["renovatie"], "new": kader["bouwkosten_eur_per_m2"]["nieuwbouw"],
              "fees": round(params["architect_pct_of_pem"] + params["aparejador_pct_of_pem"], 4)},
    "items": [{k: it[k] for k in ("id", "source", "ref", "kandidaat", "area_label", "zone_label", "location", "type", "category",
                                  "price", "built_m2", "plot_m2", "class", "class_label", "scenario", "max_price", "margin_at_asking",
                                  "room", "reliable", "warnings", "reason", "signals", "blockers", "events_7d", "url", "price_m2", "price_m2_plot",
                                  "calc", "result_m2")}
              for it in items],
    "auctions": auction_rows,
    "zones": zones,
    "counts": {c: sum(1 for i in items if i["class"] == c) for c in order},
}

CSS = """
:root{color-scheme:light dark;--paper:#f7f5f0;--surface:#fffefb;--sunk:#efebe3;--ink:#2b3331;--ink-strong:#1c2220;--muted:#69706c;--beige:#b8a07a;--beige-soft:#ece4d5;--rule:rgba(43,51,49,.13);--rule-strong:rgba(43,51,49,.26);
--groen:#2f7a55;--groen-bg:#e2f0e8;--blauw:#2f6386;--blauw-bg:#e3edf4;--oranje:#b86e12;--oranje-bg:#f6ead6;--grijs:#8c918e;--grijs-bg:#ecebe7;--onzeker:#7d6a9c;--onzeker-bg:#ece7f3;--veiling:#7a3f5c;--veiling-bg:#f3e4eb;
--font-display:"Newsreader","Iowan Old Style",Georgia,serif;--font-body:"Inter Tight","Helvetica Neue",Arial,system-ui,sans-serif;--font-mono:"JetBrains Mono","SFMono-Regular",Menlo,monospace}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--paper:#1a201e;--surface:#222a28;--sunk:#2a3230;--ink:#e4e1d9;--ink-strong:#f3f0e9;--muted:#a3a8a2;--beige:#cbb48d;--beige-soft:#3a3529;--rule:rgba(228,225,217,.13);--rule-strong:rgba(228,225,217,.26);
--groen:#8ccfae;--groen-bg:#1f3529;--blauw:#8dbad8;--blauw-bg:#1f3340;--oranje:#e0b567;--oranje-bg:#3b3020;--grijs:#a9aea9;--grijs-bg:#2b3230;--onzeker:#b6a5d2;--onzeker-bg:#2f2740;--veiling:#d9a5bd;--veiling-bg:#3a2530}}
:root[data-theme="dark"]{--paper:#1a201e;--surface:#222a28;--sunk:#2a3230;--ink:#e4e1d9;--ink-strong:#f3f0e9;--muted:#a3a8a2;--beige:#cbb48d;--beige-soft:#3a3529;--rule:rgba(228,225,217,.13);--rule-strong:rgba(228,225,217,.26);--groen:#8ccfae;--groen-bg:#1f3529;--blauw:#8dbad8;--blauw-bg:#1f3340;--oranje:#e0b567;--oranje-bg:#3b3020;--grijs:#a9aea9;--grijs-bg:#2b3230;--onzeker:#b6a5d2;--onzeker-bg:#2f2740;--veiling:#d9a5bd;--veiling-bg:#3a2530}
*{box-sizing:border-box}body{margin:0;background:var(--paper);color:var(--ink);font:16px/1.5 var(--font-body);-webkit-text-size-adjust:100%}
a{color:var(--ink-strong);text-decoration-color:var(--beige);text-underline-offset:3px}:focus-visible{outline:2px solid var(--beige);outline-offset:2px}
.wrap{max-width:46rem;margin:0 auto;padding:0 0 3rem}
header{background:var(--ink-strong);color:#ece9e2;padding:1rem 1rem .9rem;position:sticky;top:0;z-index:5}
.brand{font-family:var(--font-mono);font-size:.7rem;letter-spacing:.2em;color:var(--beige)}
h1{font-family:var(--font-display);font-weight:500;font-size:1.5rem;margin:.2rem 0 .35rem;line-height:1.15}
header p{margin:0;font-size:.82rem;color:#c9c6bd}
.counts{display:flex;gap:.35rem;flex-wrap:wrap;margin-top:.6rem}
.count{font-family:var(--font-mono);font-size:.7rem;padding:.2rem .5rem;border-radius:99px;border:1px solid rgba(255,255,255,.2);display:inline-flex;gap:.35rem;align-items:center}
.dot{width:.55rem;height:.55rem;border-radius:50%;display:inline-block;flex:none}
.dot.groen{background:var(--groen)}.dot.blauw{background:var(--blauw)}.dot.oranje{background:var(--oranje)}.dot.grijs{background:var(--grijs)}.dot.onzeker{background:var(--onzeker)}.dot.geen{background:transparent;border:1.5px solid var(--grijs)}.dot.veiling{background:var(--veiling);border-radius:2px}
nav.filters{position:sticky;top:0;z-index:4;background:var(--paper);border-bottom:1px solid var(--rule);padding:.6rem 1rem;display:flex;gap:.35rem;overflow-x:auto;-webkit-overflow-scrolling:touch}
.chip{border:1px solid var(--rule-strong);background:var(--surface);color:inherit;border-radius:99px;padding:.45rem .75rem;font-size:.82rem;white-space:nowrap;cursor:pointer;min-height:2.2rem}
.chip.on{background:var(--ink-strong);color:var(--paper);border-color:var(--ink-strong)}
main{padding:.8rem 1rem}
.card{background:var(--surface);border:1px solid var(--rule);border-radius:10px;padding:.85rem .9rem;margin-bottom:.6rem}
.card>summary{list-style:none;cursor:pointer}.card>summary::-webkit-details-marker{display:none}
.top{display:flex;align-items:center;gap:.4rem;font-family:var(--font-mono);font-size:.76rem;color:var(--muted)}
.top .where{margin-left:auto;text-align:right;font-family:var(--font-body)}
.price{font-family:var(--font-display);font-size:1.45rem;color:var(--ink-strong);margin:.25rem 0 .1rem;font-variant-numeric:tabular-nums}
.sub{font-family:var(--font-mono);font-size:.74rem;color:var(--muted)}
.triple{display:grid;grid-template-columns:repeat(3,1fr);gap:.35rem;margin:.15rem 0 .4rem}
.triple-cap{font-family:var(--font-mono);font-size:.6rem;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);margin:.5rem 0 0}
.triple div{background:var(--sunk);border-radius:6px;padding:.35rem .45rem}
.triple span{display:block;font-size:.6rem;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;text-transform:uppercase;letter-spacing:.05em;color:var(--muted)}
.triple b{font-family:var(--font-mono);font-weight:500;font-size:.88rem;color:var(--ink-strong);font-variant-numeric:tabular-nums}
.sum{display:grid;grid-template-columns:1fr;gap:.2rem;margin:.1rem 0 .4rem}
.sum div{display:flex;justify-content:space-between;gap:.4rem;font-size:.78rem;border-bottom:1px dotted var(--rule);padding-bottom:.12rem}
.sum span{color:var(--muted)}.sum b{font-family:var(--font-mono);font-weight:500;font-variant-numeric:tabular-nums;color:var(--ink-strong)}
.sum b.pos{color:var(--groen)}.sum b.neg{color:#b4453a}
.sumline{margin:0 0 .4rem;font-size:.76rem;color:var(--muted);font-variant-numeric:tabular-nums}
.badges{display:flex;flex-wrap:wrap;gap:.3rem}
.badge{font-family:var(--font-mono);font-size:.64rem;letter-spacing:.04em;text-transform:uppercase;padding:.16rem .42rem;border-radius:3px;background:var(--grijs-bg);color:var(--muted)}
.badge.groen{background:var(--groen-bg);color:var(--groen)}.badge.blauw{background:var(--blauw-bg);color:var(--blauw)}.badge.oranje{background:var(--oranje-bg);color:var(--oranje)}.badge.onzeker{background:var(--onzeker-bg);color:var(--onzeker)}.badge.veiling{background:var(--veiling-bg);color:var(--veiling)}
.detail{border-top:1px solid var(--rule);margin-top:.6rem;padding-top:.6rem;font-size:.86rem;display:grid;gap:.5rem}
.detail dl{display:grid;grid-template-columns:auto 1fr;gap:.2rem .7rem;margin:0}
.detail dt{color:var(--muted);font-size:.78rem}.detail dd{margin:0;font-variant-numeric:tabular-nums}
.detail ul{margin:0;padding-left:1.1rem}.detail li{margin:.15rem 0}
.hint{color:var(--muted);font-size:.8rem}
h2{font-family:var(--font-display);font-weight:500;font-size:1.2rem;margin:1.6rem 0 .5rem;color:var(--ink-strong)}
table{width:100%;border-collapse:collapse;font-size:.85rem}
th,td{text-align:left;padding:.4rem .5rem .4rem 0;border-bottom:1px solid var(--rule)}
th{font-family:var(--font-mono);font-size:.62rem;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);font-weight:500}
td.num{text-align:right;font-family:var(--font-mono);font-variant-numeric:tabular-nums;white-space:nowrap}
footer{padding:1.5rem 1rem 3rem;color:var(--muted);font-size:.8rem;border-top:1px solid var(--rule);margin-top:1.5rem}
.empty{padding:2rem 0;text-align:center;color:var(--muted)}
ol.uitleg{padding-left:1.2rem;font-size:.88rem;display:grid;gap:.45rem;margin:0}
ol.uitleg li::marker{color:var(--beige);font-family:var(--font-mono)}
ol.uitleg b{color:var(--ink-strong)}
"""

JS = """
const D = window.__DH__;
const esc = (v) => String(v ?? "").replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
const safeUrl = (u) => (typeof u === "string" && /^https?:\\/\\//i.test(u) ? u : null);
const nf = new Intl.NumberFormat("nl-NL", { maximumFractionDigits: 0 });
const eur = (v) => (v == null ? "—" : nf.format(Math.round(v)) + " €");
const keur = (v) => (v == null ? "—" : v >= 1e6 ? (v / 1e6).toFixed(2).replace(".", ",") + " M" : nf.format(Math.round(v / 1000)) + "k");
const pct = (v) => (v == null ? "—" : (v * 100).toFixed(0) + " %");
const signed = (v) => (v == null ? "—" : (v > 0 ? "+" : v < 0 ? "−" : "") + Math.abs(v * 100).toFixed(0) + " %");
let filter = "kansen";

function sumBlock(x) {
  const c = x.calc;
  if (!c) return "";
  const m2s = x.result_m2 ? nf.format(x.result_m2) + " m²" : "";
  return `<div class="sum">
    <div><span>Aankoop + kosten</span><b>${keur(c.acquisition)}</b></div>
    <div><span>Bouw ${esc(m2s)}</span><b>${keur(c.build)}</b></div>
    <div><span>Verkoop ${esc(m2s)} × ${nf.format(c.eur_m2_sale)}</span><b>${keur(c.sale)}</b></div>
    <div><span>Resultaat</span><b class="${c.result >= 0 ? "pos" : "neg"}">${c.result >= 0 ? "+" : "−"}${keur(Math.abs(c.result))}</b></div>
  </div><p class="sumline">marge ${pct(c.margin)} · rendement op kosten ${pct(c.roi_on_costs)} · ${esc(c.months)} mnd · basisscenario bij vraagprijs</p>`;
}

function card(x) {
  const mp = x.max_price, mg = x.margin_at_asking;
  const link = safeUrl(x.url);
  return `<details class="card">
    <summary>
      <div class="top"><span class="dot ${x.class}"></span><span>${esc(x.kandidaat ? x.kandidaat + " · " : "")}${esc(x.ref)}</span><span class="where">${esc(x.zone_label || x.area_label)}</span></div>
      <div class="price">${eur(x.price)}</div>
      <div class="sub">${x.built_m2 ? nf.format(x.built_m2) + " m² gebouwd" : "geen woning"}${x.plot_m2 ? " · perceel " + nf.format(x.plot_m2) + " m²" : ""}${x.price_m2 ? " · " + nf.format(x.price_m2) + " €/m²" : x.price_m2_plot ? " · " + nf.format(x.price_m2_plot) + " €/m² perceel" : ""}</div>
      ${mp ? `<p class="triple-cap">Maximale koopprijs bij ${pct(D.margin)} marge</p><div class="triple"><div><span>Voorzichtig</span><b>${keur(mp.conservative)}</b></div><div><span>Basis</span><b>${keur(mp.base)}</b></div><div><span>Gunstig</span><b>${keur(mp.upside)}</b></div></div>${sumBlock(x)}` : `<p class="hint">${esc(x.reason || "Geen indicatie")}</p>`}
      <div class="badges"><span class="badge ${x.class}">${x.room != null ? "Ruimte " + signed(x.room) : esc(x.class_label)}</span>${x.reliable === false ? '<span class="badge onzeker">onzeker</span>' : ""}${(x.events_7d || []).map((e) => `<span class="badge">${esc(e.toLowerCase())}</span>`).join("")}</div>
    </summary>
    <div class="detail">
      ${x.calc ? `<p class="hint">Aankoop en kosten ${eur(x.calc.acquisition)} + bouw ${eur(x.calc.build)} + overige ${eur(x.calc.other)} = <b>${eur(x.calc.total_costs)}</b>. Verkoop ${nf.format(x.result_m2)} m² × ${nf.format(x.calc.eur_m2_sale)} €/m² = <b>${eur(x.calc.sale)}</b>. Resultaat <b>${eur(x.calc.result)}</b>. Bouw is ${nf.format(x.calc.eur_m2_build)} €/m² inclusief honoraria, leges, reserve en btw.</p>` : ""}
      ${x.scenario ? `<dl><dt>Scenario</dt><dd>${esc(x.scenario)}</dd>
        <dt>Marge bij vraagprijs</dt><dd>${pct(mg?.conservative)} / ${pct(mg?.base)} / ${pct(mg?.upside)}</dd>
        <dt>Soort</dt><dd>${esc(x.type || "")} · ${esc(x.category || "")}</dd></dl>` : ""}
      ${x.warnings?.length ? `<p class="hint">${x.warnings.map(esc).join("<br>")}</p>` : ""}
      ${x.signals?.length ? `<p class="hint">Signalen: ${x.signals.map(esc).join(", ")}</p>` : ""}
      ${x.blockers?.length ? `<ul>${x.blockers.map((b) => `<li>${esc(b)}</li>`).join("")}</ul>` : ""}
      ${link ? `<a href="${esc(link)}" target="_blank" rel="noopener">Advertentie openen ↗</a>` : ""}
    </div></details>`;
}

const isLoss = (x) => !!(x.calc && x.calc.result < 0);

function render() {
  const f = {
    kansen: (x) => ["groen", "blauw", "oranje"].includes(x.class),
    percelen: (x) => x.category === "perceel",
    renovatie: (x) => (x.category || "").startsWith("renovatie") || (x.category || "").startsWith("appartement"),
    kandidaten: (x) => x.source === "idealista",
    verlies: isLoss,
    alles: () => true,
  }[filter];
  const hideLoss = !["verlies", "alles"].includes(filter);
  const rows = D.items.filter((x) => f(x) && (!hideLoss || !isLoss(x)));
  const hidden = hideLoss ? D.items.filter((x) => f(x) && isLoss(x)).length : 0;
  document.querySelector("#list").innerHTML = rows.length ? rows.map(card).join("") : '<div class="empty">Niets in deze selectie.</div>';
  document.querySelector("#listmeta").textContent = `${rows.length} van ${D.items.length} objecten · maximale koopprijs voorzichtig / basis / gunstig bij ${pct(D.margin)} marge`
    + (hidden ? ` · ${hidden} met verlies verborgen` : "");
}

document.querySelectorAll("[data-f]").forEach((b) => b.addEventListener("click", () => {
  filter = b.dataset.f;
  document.querySelectorAll("[data-f]").forEach((x) => x.classList.toggle("on", x === b));
  render();
}));
render();
"""


def rows_zones() -> str:
    def cell(sr):
        return f'{num(sr["median"])}<br><span class="hint">n={sr["n"]}</span>' if sr else "—"

    rows = []
    for z in zones:
        rows.append(
            "<tr><td><b>" + E(z["label"]) + "</b></td>"
            + '<td class="num">' + cell(z.get("villa_renovated")) + "</td>"
            + '<td class="num">' + cell(z.get("villa_new")) + "</td>"
            + '<td class="num">' + cell(z.get("apartment_renovated")) + "</td></tr>"
        )
    return "".join(rows)


def rows_auctions() -> str:
    if not auction_rows:
        return '<p class="hint">Geen lopende veilingen met bekende ligging.</p>'
    cards = []
    for a in auction_rows:
        badges = "".join('<span class="badge">' + E(b) + "</span>" for b in (a["blockers"] or [])[:3])
        cards.append(
            '<div class="card"><div class="top"><span class="dot veiling"></span><span>' + E(a["sub"]) + "</span>"
            + '<span class="where">' + E(a["town"] or "ligging onbekend") + "</span></div>"
            + '<div class="price">' + eur(a["valuation"]) + "</div>"
            + '<div class="sub">' + E(a["source"]) + " · sluit " + E(a["end_date"] or "onbekend") + "</div>"
            + '<div class="badges">' + badges + "</div></div>"
        )
    return "".join(cards)


counts = data["counts"]
html_out = f"""<!doctype html>
<html lang="nl"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Deal Hunter onderweg</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Newsreader:opsz,wght@6..72,400;6..72,500&family=Inter+Tight:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap">
<style>{CSS}</style></head>
<body><div class="wrap">
<header>
  <div class="brand">TREE DEAL HUNTER</div>
  <h1>Kansen in Jávea, Benitachell en Moraira</h1>
  <p>Momentopname {E(data['generated'])} · {len(data['items'])} objecten · marge-eis {int(MARGIN * 100)} % op verkoopwaarde</p>
  <div class="counts">
    <span class="count"><span class="dot groen"></span>{counts.get('groen', 0)} ook voorzichtig</span>
    <span class="count"><span class="dot blauw"></span>{counts.get('blauw', 0)} in basis</span>
    <span class="count"><span class="dot oranje"></span>{counts.get('oranje', 0)} tot 30 % zakken</span>
    <span class="count"><span class="dot onzeker"></span>{counts.get('onzeker', 0)} onzeker</span>
    <span class="count"><span class="dot veiling"></span>{len(auction_rows)} veilingen in Alicante</span>
  </div>
</header>

<nav class="filters">
  <button class="chip on" data-f="kansen">Kansen</button>
  <button class="chip" data-f="percelen">Percelen</button>
  <button class="chip" data-f="renovatie">Renovatie</button>
  <button class="chip" data-f="kandidaten">Kandidaten</button>
  <button class="chip" data-f="verlies">Verlies</button>
  <button class="chip" data-f="alles">Alles</button>
</nav>

<main>
  <p class="hint" id="listmeta"></p>
  <div id="list"></div>

  <h2>Wijkprijzen per m²</h2>
  <table><thead><tr><th>Wijk</th><th class="num">Gerenoveerd</th><th class="num">Nieuwbouw</th><th class="num">Appartement</th></tr></thead>
  <tbody>{rows_zones()}</tbody></table>
  <p class="hint">Mediaan vraagprijs per m² gebouwd, gemeten 15 september 2026 en per wijk gecontroleerd.</p>

  <h2>Veilingen in de provincie Alicante</h2>
  {rows_auctions()}
</main>

<h2>Hoe dit gerekend is</h2>
  <ol class="uitleg">
    <li><b>Scenario.</b> Bij een woning: integrale renovatie van het bestaande oppervlak, en waar het perceel het toelaat ook sloop en nieuwbouw. Bij een perceel: nieuwbouw van 0,20 m² per m² perceel, een aanname op de villaregels van zona E die per perceel bevestigd moet worden.</li>
    <li><b>Bouwkosten.</b> Jouw tarieven: {num(data['kader']['reno'])} €/m² renovatie en {num(data['kader']['new'])} €/m² nieuwbouw, exclusief btw. Daarbovenop: {int(data['kader']['fees'] * 100)} % honoraria, ICIO en leges, onderzoek, zwembad en buitenruimte, 10 % reserve en de btw die niet terugvorderbaar is.</li>
    <li><b>Aankoopkosten.</b> Overdrachtsbelasting 9 % (11 % boven 1 miljoen over het hele bedrag), of btw plus AJD bij een perceel van een ondernemer, plus notaris, register en onderzoek.</li>
    <li><b>Verkoopopbrengst.</b> Het verkoopbare oppervlak maal de vraagprijs per m² van gerenoveerde of nieuwe woningen in dezelfde wijk. Vraagprijzen, geen transactieprijzen.</li>
    <li><b>Marge.</b> Resultaat gedeeld door de verkoopopbrengst. Jouw eis is {int(MARGIN * 100)} %. De maximale koopprijs is teruggerekend: de hoogste koopprijs waarbij die marge nog wordt gehaald.</li>
    <li><b>Wat je niet ziet.</b> Objecten waarbij de rekensom bij de vraagprijs verlies geeft, staan standaard verborgen. Ze zijn te bekijken onder Verlies of Alles; ze verdwijnen niet uit het systeem, want een prijsdaling kan ze alsnog interessant maken.</li>
    <li><b>De drie blokken.</b> Voorzichtig rekent met het laagste kwart van de wijkprijzen, basis met de mediaan, gunstig met het hoogste kwart. Dezelfde kosten, alleen een andere verkoopprijs.</li>
  </ol>

<footer>
  <p>Tik op een object voor scenario, marge en blokkades. Bedragen zijn maximale koopprijzen bij {int(MARGIN * 100)} % winstmarge op de verkoopwaarde, gerekend met {num(data['kader']['reno'])} €/m² renovatie, {num(data['kader']['new'])} €/m² nieuwbouw en {int(data['kader']['fees'] * 100)} % honoraria, exclusief btw.</p>
  <p>Verkoopprijzen komen uit vraagprijzen van vergelijkbare gerenoveerde of nieuwe woningen in dezelfde wijk. Vraagprijzen zijn geen transactieprijzen; dit is een indicatie, geen taxatie en geen biedadvies.</p>
  <p>Kaart, kadaster, luchtfoto en de wat-als-schuiven staan op het dashboard: <a href="https://mac-mini-van-root-admin.tail69022d.ts.net:8710">mac-mini-van-root-admin.tail69022d.ts.net:8710</a>, bereikbaar zodra je telefoon met Tailscale verbonden is.</p>
</footer>
</div>
<script>window.__DH__ = {json.dumps(data, ensure_ascii=False)};</script>
<script>{JS}</script>
</body></html>"""

OUT.write_text(html_out, encoding="utf-8")
print("geschreven:", OUT, f"({len(html_out) // 1024} kB, {len(data['items'])} objecten)")

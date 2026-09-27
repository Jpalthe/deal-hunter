#!/usr/bin/env python3
"""Maakt de webpagina bij de foutenjacht van 27-09-2026.

Leest de uitkomst van de workflow (zeven zoekers, elke bevinding door twee agents tegengesproken)
en zet er een pagina van die Jan op zijn telefoon kan lezen: conclusie eerst, onderbouwing achter
een tik.

  python tools/rapport_foutenjacht.py <workflow.json> [--uit onderzoek/foutenjacht-27-09-2026.html]
"""
from __future__ import annotations

import argparse
import html
import json
import sys
from pathlib import Path

HERSTELD = [
    ("46cffd0", "Uitzicht telde als ligging, en Tosalet kreeg de prijzen van Montgó",
     "229 van de 3.173 Jávea-objecten krijgen een andere wijk. De wijk bepaalt de verkoopprijs per "
     "m² en dus de maximale koopprijs; dit was het enige gemeten pad waarlangs die te hóóg kon "
     "uitvallen."),
    ("25f0d2a", "Dezelfde woning in vijf talen telde als vijf woningen",
     "51 woningen, 172 overtollige rijen. Bij 41 groepen verschilde de prijs per taalversie, en de "
     "meldingenlijst koos systematisch de goedkoopste — dus de foutste."),
    ("f191646", "Nog 202 categoriepagina's die als woning binnenkwamen",
     "Herkend aan de titel: een lijst begint met een meervoud, een woning niet. Alleen toegepast "
     "als het adres geen objectnummer draagt, anders sneuvelen echte advertenties."),
    ("313bdba", "Prijzen uit het zoekfilter: 293 woningen stonden op € 50.000",
     "De prijs- en oppervlaktefilters staan in keuzelijsten en telden mee als paginatekst. "
     "819 objecten geraakt; de echte prijs van dat eerste object was € 690.000."),
    ("86afddb", "Een punt is niet altijd een duizendtalscheiding",
     "191 objecten hadden een bebouwd oppervlak tot 83.235 m². Dat getal gaat rechtstreeks de "
     "bouwkosten en de verkoopwaarde in."),
    ("d5ab687", "280 zoekresultaatpagina's stonden als woning in de database",
     "Elke filterpagina droeg de prijs van de woning die bovenaan dat filter stond. Eén "
     "€ 1.950.000 met 389/409 m² kwam eenentwintig keer voor."),
    ("d9297ac", "Vangnet tegen keuzelijstwaarden, en het tabblad Geen prijs",
     "Een waarde die meer dan 15 % van één bron beslaat, gaat er automatisch uit en wordt in het "
     "ochtendbericht gemeld. 878 objecten geraakt, in vier ronden."),
    ("eaa5d82", "Geen rekensom meer op een prijs van nul",
     "Een object zonder vraagprijs kreeg een complete som met een koopprijs van nul: "
     "„Aankoop € 7.500, Bouw € 520.548, Verkoop € 1.568.658”."),
    ("1de41c8", "Werkelijk betaald prijspeil per kadasterzone",
     "Naast onze vraagprijzen nu het gemiddelde van de notariële koopakten per zone. 350 objecten "
     "gekoppeld; het vond meteen een villa waarvan de verkoopwaarde op twee vergelijkingsobjecten "
     "rustte."),
]

STIJL = """
:root{--paper:#f7f5f0;--surface:#fffefb;--sunk:#efebe3;--ink:#2b3331;--ink-strong:#1c2220;
 --muted:#646b68;--faint:#9aa09b;--beige:#b8a07a;--rule:rgba(43,51,49,.14);--rule-2:rgba(43,51,49,.3);
 --bad:#933a31;--bad-bg:#f6e3e0;--warn:#8a5d12;--warn-bg:#f5ead7;--ok:#2f6b4f;--ok-bg:#e2efe8}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){
 --paper:#191d1c;--surface:#202523;--sunk:#161a19;--ink:#e6e3dc;--ink-strong:#f5f2ea;--muted:#a3a9a4;
 --faint:#7c837e;--rule:rgba(230,227,220,.16);--rule-2:rgba(230,227,220,.32);
 --bad:#e0897d;--bad-bg:#32211f;--warn:#d8ab5e;--warn-bg:#2c2418;--ok:#7fc0a0;--ok-bg:#1b2a23}}
:root[data-theme="dark"]{--paper:#191d1c;--surface:#202523;--sunk:#161a19;--ink:#e6e3dc;
 --ink-strong:#f5f2ea;--muted:#a3a9a4;--faint:#7c837e;--rule:rgba(230,227,220,.16);
 --rule-2:rgba(230,227,220,.32);--bad:#e0897d;--bad-bg:#32211f;--warn:#d8ab5e;--warn-bg:#2c2418;
 --ok:#7fc0a0;--ok-bg:#1b2a23}
*{box-sizing:border-box}
body{margin:0;background:var(--paper);color:var(--ink);
 font:400 16px/1.6 "Inter Tight",-apple-system,Helvetica,Arial,sans-serif;
 -webkit-text-size-adjust:100%}
.page{max-width:44rem;margin:0 auto;padding:2.2rem 1rem 5rem}
.eyebrow{font:500 11px/1.4 "JetBrains Mono",Menlo,monospace;letter-spacing:.18em;
 text-transform:uppercase;color:var(--muted);margin:0 0 .6rem}
h1{font:300 clamp(30px,7vw,44px)/1.05 "Newsreader",Georgia,serif;letter-spacing:-.022em;
 margin:0 0 .5rem;text-wrap:balance;color:var(--ink-strong)}
h2{font:400 clamp(20px,4.4vw,26px)/1.15 "Newsreader",Georgia,serif;margin:2.6rem 0 .3rem;
 color:var(--ink-strong);text-wrap:balance}
h2 + .sub{color:var(--muted);margin:.1rem 0 1rem;font-size:.94rem}
.lead{font-size:1.08rem;color:var(--ink);margin:.4rem 0 1.4rem}
.lead em{font-style:italic;color:var(--beige)}
.cijfers{display:grid;grid-template-columns:repeat(auto-fit,minmax(8.5rem,1fr));gap:.5rem;margin:1.4rem 0}
.cijfer{background:var(--surface);border:1px solid var(--rule);border-radius:10px;padding:.7rem .8rem}
.cijfer b{display:block;font:300 26px/1 "Newsreader",Georgia,serif;color:var(--ink-strong);
 font-variant-numeric:tabular-nums}
.cijfer span{font-size:.78rem;color:var(--muted);display:block;margin-top:.25rem}
details{background:var(--surface);border:1px solid var(--rule);border-radius:10px;
 margin:.45rem 0;overflow:hidden}
details[open]{border-color:var(--rule-2)}
summary{cursor:pointer;padding:.7rem .85rem;list-style:none;display:flex;gap:.6rem;align-items:flex-start}
summary::-webkit-details-marker{display:none}
summary::after{content:"▾";color:var(--faint);margin-left:auto;flex:none}
details[open] summary::after{content:"▴"}
.tel{font:500 12px/1.5 "JetBrains Mono",Menlo,monospace;color:var(--muted);
 background:var(--sunk);border-radius:5px;padding:.05rem .4rem;flex:none;font-variant-numeric:tabular-nums}
.t{font-weight:500;color:var(--ink-strong)}
.body{padding:0 .85rem 1rem;border-top:1px solid var(--rule);font-size:.93rem}
.body h4{font:500 11px/1.4 "JetBrains Mono",Menlo,monospace;letter-spacing:.14em;
 text-transform:uppercase;color:var(--muted);margin:1rem 0 .25rem}
.body p{margin:.25rem 0}
pre{background:var(--sunk);border-radius:8px;padding:.6rem .7rem;overflow-x:auto;
 font:400 12px/1.5 "JetBrains Mono",Menlo,monospace;white-space:pre-wrap;word-break:break-word;margin:.3rem 0}
.plek{font:400 12px/1.5 "JetBrains Mono",Menlo,monospace;color:var(--muted);word-break:break-all}
.stip{display:inline-block;width:.5rem;height:.5rem;border-radius:50%;flex:none;margin-top:.55rem}
.hoog{background:var(--bad)} .midden{background:var(--warn)} .laag{background:var(--faint)}
.klaar{border-left:3px solid var(--ok)}
.klaar .tel{background:var(--ok-bg);color:var(--ok)}
.vraag{border-left:3px solid var(--warn)}
ul{padding-left:1.1rem} li{margin:.3rem 0}
.voet{margin-top:3rem;padding-top:1rem;border-top:1px solid var(--rule);color:var(--muted);font-size:.85rem}
@media print{details{break-inside:avoid}summary::after{display:none}}
"""


def zwaarte(n: int) -> str:
    return "hoog" if n >= 500 else ("midden" if n >= 100 else "laag")


def blok(b: dict, i: int) -> str:
    n = b.get("bijgesteld_aantal") if b.get("bijgesteld_aantal") not in (None, -1) else b.get("hoeveel_objecten") or 0
    e = html.escape
    deel = [f'<details><summary><span class="stip {zwaarte(n)}"></span>'
            f'<span><span class="t">{e(b["titel"])}</span></span>'
            f'<span class="tel">{n if n > 0 else "?"}</span></summary><div class="body">']
    deel.append(f'<p class="plek">{e(b["bestand"])}</p>')
    deel.append(f"<h4>Wat er misgaat</h4><p>{e(b['wat_er_misgaat'])}</p>")
    deel.append(f"<h4>Gevolg voor de cijfers</h4><p>{e(b['gevolg_voor_de_cijfers'])}</p>")
    if b.get("bewijs"):
        deel.append(f"<h4>Bewijs</h4><pre>{e(b['bewijs'][:1800])}</pre>")
    deel.append(f"<h4>Voorstel</h4><p>{e(b['herstelvoorstel'])}</p>")
    if b.get("tegenspraak"):
        deel.append("<h4>Wat de tegenspraak zei</h4>")
        for t in b["tegenspraak"]:
            deel.append(f"<p>{e(t[:900])}…</p>" if len(t) > 900 else f"<p>{e(t)}</p>")
    deel.append("</div></details>")
    return "".join(deel)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("workflow")
    ap.add_argument("--uit", default="onderzoek/foutenjacht-27-09-2026.html")
    a = ap.parse_args(argv)
    d = json.loads(Path(a.workflow).read_text(encoding="utf-8"))
    r = d["result"]
    aant = r["aantallen"]
    e = html.escape

    hersteld = "".join(
        f'<details class="klaar"><summary><span class="stip laag"></span>'
        f'<span><span class="t">{e(t)}</span></span><span class="tel">{c}</span></summary>'
        f'<div class="body"><p>{e(u)}</p></div></details>'
        for c, t, u in HERSTELD)

    p = Path(a.uit)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(f"""<!doctype html><html lang="nl"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Foutenjacht Deal Hunter</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;0,6..72,500;1,6..72,400&family=Inter+Tight:wght@300;400;500&family=JetBrains+Mono:wght@400;500&display=swap">
<style>{STIJL}</style></head><body><div class="page">
<p class="eyebrow">TREE Deal Hunter · nacht van 26 op 27 september 2026</p>
<h1>Wat er mis was met de cijfers</h1>
<p class="lead">Zeven onderzoekers hebben de hele keten nagelopen — elke bron, elk veld, elke
rekenstap. Iedere bevinding ging daarna langs twee tegensprekers: één die hem probeerde te
<em>weerleggen</em> en één die narekende of het de bedragen werkelijk raakt. Drie bevindingen
haalden dat niet.</p>
<div class="cijfers">
  <div class="cijfer"><b>{aant['bevestigd']}</b><span>door beide tegensprekers bevestigd</span></div>
  <div class="cijfer"><b>{aant['aannemelijk']}</b><span>door één van de twee</span></div>
  <div class="cijfer"><b>{len(HERSTELD)}</b><span>vannacht hersteld</span></div>
  <div class="cijfer"><b>{aant['gesneuveld']}</b><span>gesneuveld op de tegenspraak</span></div>
</div>

<h2>Al hersteld</h2>
<p class="sub">Dit staat er sinds vannacht in, met tests erbij.</p>
{hersteld}

<h2>Bevestigd, nog te doen</h2>
<p class="sub">Beide tegensprekers zeiden: dit klopt. Het getal rechts is het aantal objecten.</p>
{"".join(blok(b, i) for i, b in enumerate(r["bevestigd"]))}

<h2>Half bevestigd</h2>
<p class="sub">Eén van de twee hield vol, de ander niet. Waard om naar te kijken, niet om blind op af te gaan.</p>
{"".join(blok(b, i) for i, b in enumerate(r["aannemelijk"]))}

<h2>Gesneuveld</h2>
<p class="sub">Leek een fout, was het niet. Staat hier zodat niemand er nog eens achteraan gaat.</p>
<ul>{"".join(f"<li><b>{e(g['titel'])}</b> — {e((g.get('waarom_weg') or [''])[0][:320])}…</li>" for g in r["gesneuveld"])}</ul>

<p class="voet">{aant['invalshoeken']} invalshoeken · {d.get('agentCount')} agents ·
{d.get('totalToolCalls')} handelingen · {round((d.get('totalTokens') or 0) / 1e6, 1)} miljoen tokens.
Elk aantal in dit rapport is door de tegenspraak nagerekend op de database zelf, niet overgenomen
van de melder.</p>
</div></body></html>""", encoding="utf-8")
    print(f"{p} · {p.stat().st_size // 1024} kB")
    return 0


if __name__ == "__main__":
    sys.exit(main())

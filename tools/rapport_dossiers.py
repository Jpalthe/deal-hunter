#!/usr/bin/env python3
"""Maakt per object een volledig dossier als webpagina, plus een besluitpagina die ze samenvat.

  python3 tools/rapport_dossiers.py [--aantal 8] [--refs 90705084,4104JAV]

Schrijft naar rapporten/dossiers/. Elke pagina staat op zichzelf: geen server, geen kaarttegels.
De perceelgrens wordt als tekening meegegeven, met schaalbalk, zodat hij ook offline klopt.
"""
from __future__ import annotations

import argparse
import html
import json
import math
import os
import sys
from datetime import datetime

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

from dh import config, dossier, negotiation  # noqa: E402
from dh.store import Store  # noqa: E402

OUT = config.ROOT / "rapporten" / "dossiers"
E = html.escape


def num(v) -> str:
    return "—" if v in (None, "") else f"{float(v):,.0f}".replace(",", ".")


def eur(v) -> str:
    return "—" if v in (None, "") else "€&nbsp;" + num(v)


def pct(v, d=0) -> str:
    return "—" if v is None else f"{v * 100:.{d}f}&nbsp;%"


def sgn(v) -> str:
    return "—" if v is None else f"{v * 100:+.0f}&nbsp;%"


def datum(iso: str | None) -> str:
    if not iso:
        return "—"
    try:
        return datetime.fromisoformat(iso).strftime("%d-%m-%Y")
    except ValueError:
        return E(iso)


# ----------------------------------------------------------------- tekeningen

def perceel_svg(geojson: dict | None, w: int = 620, h: int = 380) -> str:
    """Tekent de perceelgrens met een schaalbalk. Geen kaarttegels: dit werkt overal."""
    if not geojson:
        return '<p class="leeg">Geen perceelgrens opgehaald.</p>'
    rings = geojson["coordinates"] if geojson["type"] == "Polygon" else [r[0] for r in geojson["coordinates"]]
    pts = [p for r in rings for p in r]
    if len(pts) < 3:
        return '<p class="leeg">Geen bruikbare perceelgrens.</p>'
    lons = [p[0] for p in pts]; lats = [p[1] for p in pts]
    lat0 = sum(lats) / len(lats)
    # meters per graad op deze breedte, zodat de vorm niet uitrekt
    mx = 111320 * math.cos(math.radians(lat0))
    my = 110540
    xs = [(lo - min(lons)) * mx for lo in lons]
    ys = [(max(lats) - la) * my for la in lats]
    bw, bh = max(max(xs), 1e-6), max(max(ys), 1e-6)
    pad = 26
    s = min((w - 2 * pad) / bw, (h - 2 * pad) / bh)
    ox = (w - bw * s) / 2
    oy = (h - bh * s) / 2

    def path(ring):
        d = []
        for i, (lo, la) in enumerate(ring):
            x = ox + (lo - min(lons)) * mx * s
            y = oy + (max(lats) - la) * my * s
            d.append(f"{'M' if i == 0 else 'L'}{x:.1f},{y:.1f}")
        return " ".join(d) + " Z"

    # schaalbalk: een rond getal meters dat ongeveer een kwart van de breedte beslaat
    doel = bw / 4
    stap = next((x for x in (5, 10, 20, 25, 50, 100, 200, 250, 500, 1000) if x >= doel), 1000)
    bar = stap * s
    paths = "".join(f'<path d="{path(r)}" class="perceel"/>' for r in rings)
    return f"""<svg viewBox="0 0 {w} {h}" class="tekening" role="img" aria-label="Perceelgrens volgens het kadaster">
  <rect width="{w}" height="{h}" class="veld"/>
  {paths}
  <g class="schaal">
    <line x1="{pad}" y1="{h - 18}" x2="{pad + bar:.1f}" y2="{h - 18}"/>
    <line x1="{pad}" y1="{h - 23}" x2="{pad}" y2="{h - 13}"/>
    <line x1="{pad + bar:.1f}" y1="{h - 23}" x2="{pad + bar:.1f}" y2="{h - 13}"/>
    <text x="{pad + bar / 2:.1f}" y="{h - 24}">{stap} m</text>
  </g>
  <g class="noord"><text x="{w - 22}" y="{pad}">N</text><path d="M{w - 18},{pad + 4} l0,14 m0,-14 l-4,5 m4,-5 l4,5"/></g>
</svg>"""


def prijslijn_svg(hist: list, w: int = 620, h: int = 90) -> str:
    """Prijsverloop als lijn. Eén waarneming geeft geen lijn, dan zeggen we dat."""
    pts = [(i, p) for i, (_, p) in enumerate(hist) if p]
    if len(pts) < 2:
        return '<p class="leeg">Nog één waarneming: geen verloop om te tonen.</p>'
    ys = [p for _, p in pts]
    lo, hi = min(ys), max(ys)
    rng = (hi - lo) or 1
    pad = 14
    step = (w - 2 * pad) / (len(pts) - 1)
    d = " ".join(f"{'M' if i == 0 else 'L'}{pad + i * step:.1f},{h - pad - (p - lo) / rng * (h - 2 * pad):.1f}"
                 for i, (_, p) in enumerate(pts))
    dots = "".join(f'<circle cx="{pad + i * step:.1f}" cy="{h - pad - (p - lo) / rng * (h - 2 * pad):.1f}" r="3"/>'
                   for i, (_, p) in enumerate(pts))
    return (f'<svg viewBox="0 0 {w} {h}" class="lijn" role="img" aria-label="Prijsverloop">'
            f'<path d="{d}"/>{dots}</svg>'
            f'<p class="bijschrift">Van {eur(ys[0])} naar {eur(ys[-1])} in {len(pts)} waarnemingen.</p>')


# ----------------------------------------------------------------- onderdelen

def blok_besluit(d: dict) -> str:
    n = d["negotiation"]
    it = d["item"]
    best = d["best"]
    if not best or not n.get("walk_away"):
        return f'<div class="besluit geen"><p class="oordeel">{E(n.get("verdict") or "Niet te rekenen.")}</p></div>'
    kleur = {"groen": "groen", "blauw": "blauw", "oranje": "oranje"}.get(it["class"], "grijs")
    return f"""<div class="besluit {kleur}">
  <p class="oordeel">{E(n["verdict"])}</p>
  <div class="bedragen">
    <div><span class="k">Openingsbod</span><b>{eur(n['opening'])}</b><span class="m">{sgn(n['opening_pct_of_asking'])}</span></div>
    <div><span class="k">Streefprijs</span><b>{eur(n['target'])}</b><span class="m">{sgn(n['target_pct_of_asking'])}</span></div>
    <div><span class="k">Niet hoger dan</span><b>{eur(n['walk_away'])}</b><span class="m">{sgn(n['walk_pct_of_asking'])}</span></div>
    <div><span class="k">Wat de deal draagt</span><b>{eur(n['ceiling'])}</b><span class="m">basisscenario</span></div>
  </div>
  {f'<p class="let-op">{E(n["opening_toelichting"])}</p>' if n.get("opening_toelichting") else ''}
</div>"""


def blok_object(d: dict) -> str:
    l = d["listing"]
    it = d["item"]
    rijen = [
        ("Type", E(l["type"] or "—")),
        ("Vraagprijs", eur(l["price"])),
        ("Gebouwd", f'{num(l["built_m2"])} m²' if l["built_m2"] else "—"),
        ("Perceel", f'{num(l["plot_m2"])} m²' if l["plot_m2"] else "—"),
        ("Prijs per m² gebouwd", eur(l["eur_m2"]) if l["eur_m2"] else "—"),
        ("Prijs per m² perceel", eur(l["eur_m2_plot"]) if l["eur_m2_plot"] else "—"),
        ("Slaapkamers en badkamers", f'{l["beds"] or "—"} / {l["baths"] or "—"}'),
        ("In beeld sinds", f'{datum(l["first_seen"])}' + (f' ({l["days_on"]} dagen)' if l["days_on"] else "")),
        ("Bron", E({"bp": "Background Properties-feed", "idealista": "Idealista, handmatig dossier",
                    "idealista-zoek": "Idealista-assistent"}.get(d["source"],
                   ("Eigen website van " + (it.get("kantoor") or d["source"].split(":", 1)[-1])) if d["source"].startswith("makelaar:") else d["source"]))),
    ]
    if d["source"].startswith("makelaar:"):
        rijen.append(("Ook op een portaal", ("Niet gezien in de portaalbronnen die wij volgen (de feed en onze Idealista-oogst). "
                                              "Dat is geen bewijs dat het nergens anders staat; wij zien maar een deel van Idealista.")
                      if it.get("alleen_bij_makelaar") else f"Ja, ook gezien bij {E(str(it.get('portaal') or 'een portaal'))}."))
    tab = "".join(f"<tr><th>{k}</th><td>{v}</td></tr>" for k, v in rijen)
    url = l["url"] if isinstance(l["url"], str) and l["url"].startswith("https://") else None
    return f"""<h2>Het object</h2>
<p class="waar">{E(it['zone_label'] or it['area_label'] or '')}{' · ' + E(l['location']) if l['location'] else ''}</p>
<table class="kv">{tab}</table>
{f'<p><a href="{E(url)}" target="_blank" rel="noopener noreferrer">Advertentie openen</a></p>' if url else ''}
{prijslijn_svg(d["price_history"])}
{f'<p class="omschrijving">{E(l["desc"])}</p>' if l.get("desc") else ''}"""


def blok_perceel(d: dict) -> str:
    p = d["parcel"]
    if not p or not p.get("rc"):
        return ('<h2>Het perceel</h2><p class="leeg">Nog niet opgehaald bij het kadaster. '
                'Zonder kadastrale referentie is elke bouwconclusie een aanname.</p>')
    afst = p.get("distance_m")
    afst_tekst = ("De pin van de advertentie ligt binnen dit perceel." if afst == 0
                  else f"De pin ligt {afst:.0f} meter van dit perceel." if afst is not None else "Afstand onbekend.")
    rijen = [
        ("Kadastrale referentie", f'<code>{E(p["rc"])}</code>'),
        ("Adres volgens het kadaster", E(p.get("address") or "—")),
        ("Oppervlakte volgens het kadaster", f'{num(p.get("plot_m2"))} m²' if p.get("plot_m2") else "—"),
        ("Bebouwd volgens het kadaster", f'{num(p.get("built_m2"))} m²' if p.get("built_m2") is not None else "—"),
        ("Gebruik", E(p.get("use_text") or "—")),
        ("Bouwjaar", str(p["year"]) if p.get("year") else "—"),
    ]
    tab = "".join(f"<tr><th>{k}</th><td>{v}</td></tr>" for k, v in rijen)
    waarsch = "".join(f'<p class="waarschuwing">{E(w)}</p>' for w in (p.get("warnings") or []))
    mismatch = "".join(f'<p class="afwijking">{E(m)}</p>' for m in (p.get("mismatches") or []))
    links = f'<p><a href="https://www1.sedecatastro.gob.es/Cartografia/mapa.aspx?refcat={E(p["rc"])}" target="_blank" rel="noopener noreferrer">Kadasterkaart</a>'
    if d["listing"].get("lat"):
        links += (f' · <a href="https://www.google.com/maps/search/?api=1&amp;query={d["listing"]["lat"]},{d["listing"]["lon"]}"'
                  ' target="_blank" rel="noopener noreferrer">Luchtfoto</a>')
    links += "</p>"
    return f"""<h2>Het perceel</h2>
<p class="waar">{afst_tekst}</p>
<table class="kv">{tab}</table>
{perceel_svg(p.get("geojson"))}
<p class="bijschrift">Perceelgrens volgens het kadaster, op schaal. Het kadaster zegt niets over eigendom; dat staat in de nota simple.</p>
{mismatch}{waarsch}{links}"""


def blok_bestemming(d: dict) -> str:
    """De officiële bestemming van dít perceel, uit de urbanismelaag van de Generalitat Valenciana.

    Deze laag beantwoordt de vraag die vóór het bouwvolume komt: mag hier gewoond worden. Zij geeft
    géén edificabilidad, geen bebouwingspercentage en geen hoogte; dat blijft de informe urbanística.
    Daarom staat dit blok los van 'Wat hier mag'."""
    u = (d.get("item") or {}).get("urbanisme")
    if not u or not u.get("classificatie"):
        return ('<h2>Officiële bestemming</h2><p class="leeg">Nog niet opgevraagd. Dat kan pas als het '
                'perceel bekend is: zonder kadastrale referentie valt er niets te bevragen.</p>')
    g = u.get("duiding") or {}
    rijen = [("Classificatie", f"{E(u['classificatie'])} — {E(g.get('soort') or 'ONBEKEND')}"),
             ("Zonering", E(u.get("zonering") or "ONBEKEND")),
             ("Omschrijving", E(u.get("omschrijving") or "ONBEKEND")),
             ("Plan", E(u.get("plan") or "ONBEKEND")),
             ("Mag hier gewoond worden", E({"ja": "Ja, in beginsel", "voorwaardelijk": "Alleen voorwaardelijk",
                                            "nee": "Nee", "onbekend": "ONBEKEND"}[g.get("wonen", "onbekend")]))]
    tab = "".join(f"<tr><th>{k}</th><td>{v}</td></tr>" for k, v in rijen)
    return f"""<h2>Officiële bestemming</h2>
<table class="kv">{tab}</table>
<p>{E(g.get('tekst') or '')}</p>
<p class="bron">Bron: {E(u.get('bron') or '—')} via Goolzoom, opgevraagd {E((u.get('opgevraagd') or '—')[:10])}.
Deze laag zegt <b>niets</b> over hoevéél er gebouwd mag worden; dat staat in de informe urbanística.</p>"""


def blok_tegenspraak(d: dict) -> str:
    """Waar de advertentie en het kadaster elkaar tegenspreken."""
    t = (d.get("item") or {}).get("tegenspraak") or []
    if not t:
        return ""
    li = "".join(f"<li>{E(x)}</li>" for x in t)
    return f"""<h2>Advertentie tegenover kadaster</h2><ul class="waarsch">{li}</ul>
<p>Twee verklaringen, allebei het uitzoeken waard: de pin uit de advertentie wijst het verkeerde
perceel aan, óf er staat bebouwing die de advertentie niet noemt. Het tweede geval kan gunstig zijn:
een bestaand legaal gebouw geeft soms bouwrechten die nieuwbouw op kale grond niet krijgt. Vast te
stellen met de nota simple en het gemeentelijk archief.</p>"""


def blok_mag(d: dict) -> str:
    z = d["zone_rules"]
    best = d["best"]
    if not z:
        aanname = ""
        if best and best.get("kind") == "nieuwbouw":
            aanname = ('<p class="aanname">De rekensom gaat uit van 0,20 m² bouwvolume per m² perceel. Dat is een '
                       'werkaanname op de villaregels van zona E en geen vastgesteld recht voor dit perceel.</p>')
        return ('<h2>Wat hier mag</h2><p class="leeg">De bouwregels voor deze wijk zijn nog niet vastgelegd.</p>'
                + aanname +
                '<p>Vast te stellen met een informe urbanístico bij de gemeente, op de kadastrale referentie hierboven.</p>')
    NAAM = {
        "wijk": "Wijk", "zone": "Zone in het plan",
        "edificabilidad_neto": "Bouwvolume per m² perceel",
        "parcela_minima_m2": "Minimale perceelgrootte (m²)",
        "ocupacion_pct": "Maximaal bebouwd deel van het perceel (%)",
        "bouwlagen": "Bouwlagen", "hoogte_kroonlijst_m": "Hoogte tot de kroonlijst (m)",
        "hoogte_totaal_m": "Totale hoogte (m)", "retranqueo_m": "Afstand tot de perceelgrens (m)",
        "max_per_woning_m2": "Praktisch plafond per woning (m²)", "let_op": "Let op",
    }
    rijen = [(NAAM[k], E(str(v))) for k, v in z.items()
             if k in NAAM and v not in (None, "")]
    if not z.get("uitgezocht", True) and "edificabilidad_neto" in z:
        rijen.append(("Zekerheid", "Deze wijk is nog niet apart uitgezocht; hier geldt de standaardaanname."))
    tab = "".join(f"<tr><th>{k}</th><td>{v}</td></tr>" for k, v in rijen)
    return f"""<h2>Wat hier mag</h2>
<table class="kv">{tab}</table>
<p class="bron">Bron: {E(z.get('bron') or 'ONBEKEND')} · vastgelegd {E(z.get('datum') or '—')}. Blijft een indicatie tot de gemeente het per perceel bevestigt.</p>"""


def blok_risico(d: dict) -> str:
    r = d["risks"]
    if not r:
        return ('<h2>Risico\'s op de kaart</h2><p class="leeg">De risicokaarten zijn voor dit perceel nog niet bevraagd.</p>'
                '<p>Het gaat om overstroming (PATRICOVA), brandgevaar, beschermde natuur, de kustzone en de afstand tot een barranco.</p>')
    rijen = "".join(f'<tr><th>{E(k)}</th><td>{E(str(v))}</td></tr>' for k, v in r.items() if k != "bron")
    return f'<h2>Risico\'s op de kaart</h2><table class="kv">{rijen}</table>' + \
           (f'<p class="bron">Bron: {E(r.get("bron") or "")}</p>' if r.get("bron") else "")


def blok_rekensom(d: dict) -> str:
    best = d["best"]
    if not best:
        return f'<h2>De rekensom</h2><p class="leeg">{E(d["feasibility"].get("reason") or "Niet te rekenen.")}</p>'
    s = best["sum"]
    mp = best["max_price"]
    comps = best["comps"]
    posten = "".join(f'<tr><th>{E(b["label"])}</th><td class="n">{eur(b["eur"])}</td></tr>' for b in best["breakdown"])
    fo = best.get("fitout") or {}
    drie = f"""<table class="drie">
<tr><th></th><th class="n">Voorzichtig</th><th class="n">Basis</th><th class="n">Gunstig</th></tr>
<tr><th>Verkoopprijs per m²</th><td class="n">{num(comps['eur_m2']['conservative'])}</td><td class="n">{num(comps['eur_m2']['base'])}</td><td class="n">{num(comps['eur_m2']['upside'])}</td></tr>
<tr><th>Verkoopopbrengst</th><td class="n">{eur(best['sale']['conservative'])}</td><td class="n">{eur(best['sale']['base'])}</td><td class="n">{eur(best['sale']['upside'])}</td></tr>
<tr><th>Resultaat bij de vraagprijs</th><td class="n">{eur(best['result_at_asking']['conservative'])}</td><td class="n">{eur(best['result_at_asking']['base'])}</td><td class="n">{eur(best['result_at_asking']['upside'])}</td></tr>
<tr><th>Marge op de verkoop</th><td class="n">{pct(best['margin_at_asking']['conservative'])}</td><td class="n">{pct(best['margin_at_asking']['base'])}</td><td class="n">{pct(best['margin_at_asking']['upside'])}</td></tr>
<tr class="uit"><th>Maximale koopprijs</th><td class="n">{eur(mp['conservative']) if mp['conservative'] > 0 else 'niet haalbaar'}</td><td class="n">{eur(mp['base'])}</td><td class="n">{eur(mp['upside'])}</td></tr>
</table>"""
    kanaal = best.get("channel") or {}
    kanaal_tekst = ""
    if kanaal.get("used") == "intern":
        ander = kanaal.get("max_price_other", {}).get("base")
        kanaal_tekst = (f'<p class="kanaal">Gerekend met verkoop door TREE Properties zelf. Zou een externe makelaar verkopen, '
                        f'dan zakt de maximale koopprijs in het basisscenario naar {eur(ander)}. Het verschil, '
                        f'{eur(kanaal.get("saved_vs_extern"))} aan courtage, is de ruimte die je bij de aankoop kunt inzetten.</p>')
    skp = ""
    if s.get("skp_revenue"):
        skp = (f'<p class="skp">Keuken en badkamers ({fo.get("kitchens", "?")} keuken(s), {fo.get("bathrooms", "?")} badkamers) '
               f'staan voor {eur(s["skp_revenue"])} in de bouwsom. Dat werk gaat naar je eigen bedrijf; bij een brutomarge van '
               f'30 % is dat {eur(s["skp_margin"])} extra voor de groep, wat het groepsresultaat op {eur(s["group_result"])} brengt.</p>')
    comp_tab = ""
    if d["comps"]:
        c = d["comps"]
        vb = "".join(f'<tr><td>{E(str(e.get("label") or e.get("code") or ""))[:60]}</td><td class="n">{num(e.get("m2"))} m²</td>'
                     f'<td class="n">{eur(e.get("price"))}</td><td class="n">{num(e.get("eur_m2"))}</td></tr>'
                     for e in (c.get("examples") or []))
        comp_tab = f"""<h3>Waar de verkoopprijs vandaan komt</h3>
<p>{c['n']} vergelijkbare woningen in dezelfde wijk. Laagste kwart {num(c['p25'])} €/m², mediaan {num(c['median'])} €/m², hoogste kwart {num(c['p75'])} €/m².
Dit zijn vraagprijzen, geen transactieprijzen.</p>
<table class="vb"><tr><th>Object</th><th class="n">m²</th><th class="n">Vraagprijs</th><th class="n">€/m²</th></tr>{vb}</table>"""
    return f"""<h2>De rekensom</h2>
<p class="scenario">{E(best['label'])} · {best['months']} maanden · {num(best['result_m2'])} m² verkoopbaar</p>
<div class="samenvatting">
  <div><span class="k">Aankoop</span><b>{eur(s['acquisition'])}</b></div>
  <div><span class="k">Bouw</span><b>{eur(s['build'])}</b></div>
  <div><span class="k">Overig</span><b>{eur(s['other'])}</b></div>
  <div><span class="k">Verkoop</span><b>{eur(s['sale'])}</b></div>
  <div class="uit"><span class="k">Resultaat</span><b class="{'pos' if s['result'] >= 0 else 'neg'}">{eur(s['result'])}</b></div>
</div>
<p class="kengetallen">Marge op de verkoop {pct(s['margin'])} · rendement op de kosten {pct(s['roi_on_costs'])} ·
bouwkosten {num(s['eur_m2_build'])} €/m² · verkoopprijs {num(s['eur_m2_sale'])} €/m² · eigen geld nodig {eur(best.get('equity_needed'))}</p>
{skp}
<h3>Alle kostenposten</h3>
<table class="kv posten">{posten}<tr class="uit"><th>Totale kosten</th><td class="n">{eur(best['total_costs_base'])}</td></tr></table>
<h3>Drie uitkomsten</h3>
{drie}{kanaal_tekst}
{comp_tab}"""


def blok_onderhandelen(d: dict) -> str:
    n = d["negotiation"]
    if not n.get("walk_away"):
        return ""
    arg = "".join(f'<li><b>{E(a["punt"])}</b> {E(a["gebruik"])}</li>' for a in n["arguments"])
    lev = "".join(f'<li><b>{E(l["punt"])}</b> {E(l["waarde"])}</li>' for l in n["levers"])
    risk = "".join(f"<li>{E(r)}</li>" for r in (n.get("risks") or [])[:10])
    return f"""<h2>Onderhandelplan</h2>
{f'<h3>Wat je aan tafel gebruikt</h3><ul class="arg">{arg}</ul>' if arg else ''}
{f'<h3>Wat jij te bieden hebt dat een ander niet heeft</h3><ul class="arg">{lev}</ul>' if lev else ''}
{f'<h3>Voorbehouden</h3><p>{E(n.get("voorbehouden", ""))}</p><ul class="risk">{risk}</ul>' if risk else ''}"""


def blok_bewijs(d: dict) -> str:
    tb = "".join(f'<tr><th>{E(x["wat"])}</th><td>{E(x["hoe"])}</td></tr>' for x in d["te_bewijzen"])
    vs = "".join(f'<tr><td>{E(x["wie"])}</td><td>{E(x["wat"])}</td><td>{E(x["wanneer"])}</td></tr>' for x in d["vervolgstappen"])
    return f"""<h2>Wat er nog bewezen moet worden</h2>
<table class="kv">{tb}</table>
<h2>Vervolgstappen</h2>
<table class="stappen"><tr><th>Wie</th><th>Wat</th><th>Wanneer</th></tr>{vs}</table>"""


# ----------------------------------------------------------------- pagina

CSS = """
:root{color-scheme:light dark;--paper:#f7f5f0;--surface:#fffefb;--sunk:#efebe3;--ink:#2b3331;--ink2:#1c2220;
--muted:#69706c;--beige:#b8a07a;--rule:rgba(43,51,49,.14);--rule2:rgba(43,51,49,.3);
--groen:#2f7a55;--groen-bg:#e2f0e8;--blauw:#2f6386;--blauw-bg:#e3edf4;--oranje:#b86e12;--oranje-bg:#f6ead6;
--grijs:#8c918e;--grijs-bg:#ecebe7;--paars:#7d6a9c;--paars-bg:#ece7f3;--rood:#9b3a31;--rood-bg:#f7e6e4;
--display:"Newsreader","Iowan Old Style",Georgia,serif;--body:"Inter Tight","Helvetica Neue",Arial,system-ui,sans-serif;
--mono:"JetBrains Mono","SFMono-Regular",Menlo,monospace}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--paper:#1a201e;--surface:#222a28;--sunk:#2a3230;
--ink:#e4e1d9;--ink2:#f3f0e9;--muted:#a3a8a2;--beige:#cbb48d;--rule:rgba(228,225,217,.14);--rule2:rgba(228,225,217,.3);
--groen:#8ccfae;--groen-bg:#1f3529;--blauw:#8dbad8;--blauw-bg:#1f3340;--oranje:#e0b567;--oranje-bg:#3b3020;
--grijs:#a9aea9;--grijs-bg:#2b3230;--paars:#b6a5d2;--paars-bg:#2f2740;--rood:#e0938a;--rood-bg:#3a2522}}
:root[data-theme="dark"]{--paper:#1a201e;--surface:#222a28;--sunk:#2a3230;--ink:#e4e1d9;--ink2:#f3f0e9;--muted:#a3a8a2;
--beige:#cbb48d;--rule:rgba(228,225,217,.14);--rule2:rgba(228,225,217,.3);--groen:#8ccfae;--groen-bg:#1f3529;
--blauw:#8dbad8;--blauw-bg:#1f3340;--oranje:#e0b567;--oranje-bg:#3b3020;--grijs:#a9aea9;--grijs-bg:#2b3230;
--paars:#b6a5d2;--paars-bg:#2f2740;--rood:#e0938a;--rood-bg:#3a2522}
*{box-sizing:border-box}body{margin:0;background:var(--paper);color:var(--ink);font:16px/1.6 var(--body);-webkit-text-size-adjust:100%}
.wrap{max-width:48rem;margin:0 auto;padding:0 1.1rem 4rem}
header{border-bottom:1px solid var(--rule);padding:1.6rem 0 1.1rem;margin-bottom:1.2rem}
.eyebrow{font-family:var(--mono);font-size:.68rem;letter-spacing:.18em;text-transform:uppercase;color:var(--beige)}
h1{font-family:var(--display);font-weight:500;font-size:2rem;line-height:1.12;margin:.3rem 0 .2rem;color:var(--ink2);text-wrap:balance}
h2{font-family:var(--display);font-weight:500;font-size:1.35rem;margin:2.2rem 0 .5rem;color:var(--ink2);
border-top:1px solid var(--rule);padding-top:1.1rem}
h3{font-size:.95rem;font-weight:600;margin:1.4rem 0 .35rem;color:var(--ink2)}
p{margin:.5rem 0}a{color:var(--ink2);text-decoration-color:var(--beige);text-underline-offset:3px}
.sub{color:var(--muted);font-size:.9rem}
.besluit{border-left:4px solid var(--grijs);background:var(--grijs-bg);border-radius:8px;padding:1rem 1.1rem;margin:1.2rem 0}
.besluit.groen{border-color:var(--groen);background:var(--groen-bg)}
.besluit.blauw{border-color:var(--blauw);background:var(--blauw-bg)}
.besluit.oranje{border-color:var(--oranje);background:var(--oranje-bg)}
.oordeel{font-family:var(--display);font-size:1.15rem;line-height:1.35;margin:0 0 .8rem;color:var(--ink2)}
.bedragen{display:grid;grid-template-columns:repeat(auto-fit,minmax(8.5rem,1fr));gap:.6rem}
.bedragen div{background:var(--surface);border-radius:6px;padding:.5rem .6rem}
.bedragen .k{display:block;font-size:.68rem;text-transform:uppercase;letter-spacing:.05em;color:var(--muted)}
.bedragen b{display:block;font-family:var(--mono);font-size:1.05rem;color:var(--ink2);font-variant-numeric:tabular-nums}
.bedragen .m{font-size:.7rem;color:var(--muted)}
.let-op{margin:.7rem 0 0;font-size:.88rem;color:var(--muted)}
table{width:100%;border-collapse:collapse;font-size:.92rem;margin:.6rem 0}
th,td{text-align:left;padding:.42rem .5rem .42rem 0;border-bottom:1px solid var(--rule);vertical-align:top}
.kv th{width:16rem;color:var(--muted);font-weight:400}
td.n,th.n{text-align:right;font-family:var(--mono);font-variant-numeric:tabular-nums;white-space:nowrap}
.posten th{width:auto}
tr.uit th,tr.uit td{border-top:2px solid var(--rule2);font-weight:600;color:var(--ink2)}
.drie th:first-child{color:var(--muted);font-weight:400}
.vb{font-size:.85rem}
.samenvatting{display:grid;grid-template-columns:repeat(auto-fit,minmax(7rem,1fr));gap:1px;background:var(--rule);
border:1px solid var(--rule);border-radius:8px;overflow:hidden;margin:.8rem 0}
.samenvatting div{background:var(--surface);padding:.6rem .7rem}
.samenvatting .k{display:block;font-size:.68rem;text-transform:uppercase;letter-spacing:.05em;color:var(--muted)}
.samenvatting b{font-family:var(--mono);font-size:1.02rem;font-variant-numeric:tabular-nums;color:var(--ink2)}
.samenvatting b.pos{color:var(--groen)}.samenvatting b.neg{color:var(--rood)}
.kengetallen,.bron,.bijschrift{font-size:.85rem;color:var(--muted)}
.scenario{font-weight:600;color:var(--ink2)}
.kanaal,.skp{background:var(--sunk);border-radius:6px;padding:.6rem .7rem;font-size:.9rem}
.waarschuwing{background:var(--paars-bg);border-left:3px solid var(--paars);padding:.5rem .7rem;border-radius:5px;font-size:.9rem}
.afwijking{background:var(--oranje-bg);border-left:3px solid var(--oranje);padding:.5rem .7rem;border-radius:5px;font-size:.9rem}
.aanname{background:var(--sunk);border-left:3px solid var(--beige);padding:.5rem .7rem;border-radius:5px;font-size:.9rem}
.leeg{color:var(--muted);font-style:italic}
ul.arg,ul.risk{padding-left:1.1rem;margin:.4rem 0}ul.arg li,ul.risk li{margin:.35rem 0}
ul.risk li{color:var(--ink)}
.tekening{width:100%;height:auto;background:var(--surface);border:1px solid var(--rule);border-radius:8px;margin:.6rem 0}
.tekening .veld{fill:var(--surface)}
.tekening .perceel{fill:rgba(184,160,122,.22);stroke:var(--ink2);stroke-width:1.6;stroke-linejoin:round}
.tekening .schaal line{stroke:var(--muted);stroke-width:1.2}
.tekening .schaal text{fill:var(--muted);font:500 11px var(--mono);text-anchor:middle}
.tekening .noord text{fill:var(--muted);font:500 12px var(--body);text-anchor:middle}
.tekening .noord path{stroke:var(--muted);stroke-width:1.3;fill:none}
.lijn{width:100%;height:auto;background:var(--surface);border:1px solid var(--rule);border-radius:8px}
.lijn path{fill:none;stroke:var(--blauw);stroke-width:2}.lijn circle{fill:var(--blauw)}
.omschrijving{background:var(--sunk);border-radius:6px;padding:.7rem .8rem;font-size:.9rem;color:var(--muted)}
.stappen th{color:var(--muted);font-weight:400;font-size:.8rem;text-transform:uppercase;letter-spacing:.04em}
code{font-family:var(--mono);font-size:.9em;background:var(--sunk);padding:.1rem .3rem;border-radius:3px}
footer{border-top:1px solid var(--rule);margin-top:2.5rem;padding-top:1rem;font-size:.82rem;color:var(--muted)}
.terug{font-size:.85rem}
"""


def pagina(d: dict) -> str:
    it = d["item"]
    titel = f"{it['zone_label'] or it['area_label'] or 'Object'} · {d['ref']}"
    return f"""<!doctype html><html lang="nl"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Dossier {E(d['ref'])}</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Newsreader:opsz,wght@6..72,400;6..72,500&family=Inter+Tight:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap">
<style>{CSS}</style></head><body><div class="wrap">
<header>
  <div class="eyebrow">TREE Deal Hunter · dossier</div>
  <h1>{E(titel)}</h1>
  <p class="sub">{E(d['listing']['type'] or '')} · vraagprijs {eur(d['listing']['price'])} ·
  {E(it['class_label'])} · opgesteld {E(datum(d['gegenereerd']))}</p>
</header>
{blok_besluit(d)}
{blok_object(d)}
{blok_perceel(d)}
{blok_tegenspraak(d)}
{blok_bestemming(d)}
{blok_mag(d)}
{blok_risico(d)}
{blok_rekensom(d)}
{blok_onderhandelen(d)}
{blok_bewijs(d)}
<footer>
<p>Alle bedragen zijn exclusief btw tenzij anders vermeld. Verkoopprijzen komen uit vraagprijzen van vergelijkbare
woningen in dezelfde wijk; dat zijn geen transactieprijzen. Dit dossier is een onderbouwing voor een besluit, geen
taxatie en geen biedadvies. Percelen, vergunningen en lasten moeten per object bevestigd worden met een nota simple
en een informe urbanístico voordat er een bod uitgaat.</p>
<p>Er is niets verstuurd en er is met niemand contact opgenomen. Dat gebeurt pas na een uitdrukkelijk akkoord van Jan.</p>
</footer>
</div></body></html>"""


def index(dd: list[dict]) -> str:
    rijen = []
    for d in dd:
        it, n, best = d["item"], d["negotiation"], d["best"]
        c = (best or {}).get("sum") or {}
        rijen.append(f"""<tr>
<td><a href="{E(d['ref'])}.html">{E(it['zone_label'] or it['area_label'] or '')}</a><br><span class="ref">{E(d['ref'])}</span></td>
<td class="n">{eur(d['listing']['price'])}</td>
<td class="n">{eur(n.get('opening'))}</td>
<td class="n">{eur(n.get('walk_away'))}</td>
<td class="n">{eur(c.get('result'))}</td>
<td class="n">{c.get('months', '—')}</td>
<td>{E((n.get('verdict') or '').split('.')[0])}</td></tr>""")
    top = dd[0] if dd else None
    kop = ""
    if top:
        kop = (f"<p class=\"oordeel\">Als je er vannacht één zou kiezen: {E(top['item']['zone_label'] or top['ref'])} "
               f"({E(top['ref'])}). {E((top['negotiation'].get('verdict') or '').split('.')[0])}.</p>")
    return f"""<!doctype html><html lang="nl"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Deal Hunter besluit</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Newsreader:opsz,wght@6..72,400;6..72,500&family=Inter+Tight:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap">
<style>{CSS}</style></head><body><div class="wrap">
<header><div class="eyebrow">TREE Deal Hunter</div>
<h1>Waar ik mee door zou gaan</h1>
<p class="sub">{len(dd)} dossiers · {E(datetime.now(config.TZ).strftime('%d-%m-%Y %H:%M'))}</p></header>
<div class="besluit blauw">{kop}</div>
<table><tr><th>Object</th><th class="n">Vraagprijs</th><th class="n">Openen op</th><th class="n">Niet hoger</th>
<th class="n">Resultaat</th><th class="n">Mnd</th><th>Oordeel</th></tr>{''.join(rijen)}</table>
<p class="sub">De volgorde is wat een project per maand oplevert, gecorrigeerd voor het aantal punten dat nog bewezen moet worden.
Een object dat niemand heeft nagelopen krijgt twee open punten toegekend: geen bevindingen is niet hetzelfde als geen risico.</p>
<footer><p>Vraagprijzen, geen transactieprijzen. Geen taxatie en geen biedadvies. Er is met niemand contact opgenomen.</p></footer>
</div></body></html>"""


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--aantal", type=int, default=8)
    ap.add_argument("--refs", default="")
    a = ap.parse_args(argv)
    OUT.mkdir(parents=True, exist_ok=True)
    store = Store()
    try:
        if a.refs:
            refs = [x.strip() for x in a.refs.split(",") if x.strip()]
            q = ",".join("?" * len(refs))
            rows = store.con.execute(f"SELECT * FROM listings WHERE source_ref IN ({q})", refs).fetchall()
        else:
            top = dossier.rank(store, a.aantal)
            ids = [t["id"] for t in top]
            q = ",".join("?" * len(ids))
            rows = store.con.execute(f"SELECT * FROM listings WHERE id IN ({q})", ids).fetchall()
            rows = sorted(rows, key=lambda r: ids.index(r["id"]))
        dd = []
        for r in rows:
            d = dossier.build(store, r)
            (OUT / f"{d['ref']}.html").write_text(pagina(d), encoding="utf-8")
            dd.append(d)
            print(f"geschreven: rapporten/dossiers/{d['ref']}.html")
        (OUT / "index.html").write_text(index(dd), encoding="utf-8")
        print(f"geschreven: rapporten/dossiers/index.html ({len(dd)} dossiers)")
    finally:
        store.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())

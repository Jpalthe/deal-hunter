"""Rapport in drie niveaus (masterprompt §24): managementsamenvatting, gerangschikte selecties,
volledig overzicht. HTML (huisstijl TREE) en Markdown. Tijdzone Europe/Madrid."""
from __future__ import annotations

import json
from datetime import datetime, date

from jinja2 import Environment, BaseLoader, select_autoescape

from . import config

HTML = r"""<!doctype html><html lang="nl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Deal Hunter {{ slot }} {{ day }}</title>
<style>
:root{--paper:#f7f5f0;--ink:#2b3331;--ink2:#1c2220;--muted:#646b68;--beige:#b8a07a;--soft:#ece4d5;--rule:rgba(43,51,49,.14);--ok:#2f6b4f;--okbg:#e1efe7;--warn:#8a5d12;--warnbg:#f4ead6;--bad:#933a31;--badbg:#f5e2df;--info:#2f6386;--infobg:#e3edf3}
body{margin:0;background:var(--paper);color:var(--ink);font:15px/1.55 "Inter Tight","Helvetica Neue",Arial,sans-serif}
.page{max-width:62rem;margin:0 auto;padding:2rem 1.2rem 4rem}
h1,h2,h3{font-family:Newsreader,Georgia,serif;font-weight:500;color:var(--ink2);margin:0 0 .4rem}
h1{font-size:2rem;line-height:1.1}h2{font-size:1.5rem;margin-top:2.2rem;border-top:1px solid var(--rule);padding-top:1.2rem}h3{font-size:1.15rem;margin-top:1.4rem}
.eyebrow{font:12px/1.4 "JetBrains Mono",Menlo,monospace;letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}
table{border-collapse:collapse;width:100%;font-size:.9rem;margin:.5rem 0 1rem}th,td{text-align:left;padding:.45rem .6rem .45rem 0;border-bottom:1px solid var(--rule);vertical-align:top}
th{font:11px/1.4 "JetBrains Mono",Menlo,monospace;letter-spacing:.07em;text-transform:uppercase;color:var(--muted);font-weight:500}
td.n,th.n{text-align:right;font-variant-numeric:tabular-nums;white-space:nowrap}
.wrap{overflow-x:auto}.pill{display:inline-block;font:11px/1.2 "JetBrains Mono",Menlo,monospace;letter-spacing:.05em;text-transform:uppercase;padding:.15rem .4rem;border-radius:3px;white-space:nowrap}
.ok{color:var(--ok);background:var(--okbg)}.warn{color:var(--warn);background:var(--warnbg)}.bad{color:var(--bad);background:var(--badbg)}.info{color:var(--info);background:var(--infobg)}.neutral{color:var(--muted);background:var(--soft)}
.tiles{display:grid;grid-template-columns:repeat(auto-fit,minmax(9rem,1fr));gap:.6rem;margin:1rem 0}.tile{background:#fffefb;border:1px solid var(--rule);border-radius:6px;padding:.7rem .9rem}.tile b{display:block;font-size:1.5rem;font-family:Newsreader,Georgia,serif;font-weight:500;color:var(--ink2)}.tile span{font-size:.8rem;color:var(--muted)}
.note{color:var(--muted);font-size:.9rem}.callout{background:var(--soft);border-radius:6px;padding:.9rem 1.1rem;margin:1rem 0}
ul{padding-left:1.1rem}li{margin:.25rem 0}a{color:var(--ink2);text-decoration-color:var(--beige)}
</style></head><body><div class="page">
<div class="eyebrow">TREE Deal Hunter · ronde {{ slot }} · {{ day }} · {{ area_label }}</div>
<h1>{{ headline }}</h1>
<p class="note">Bronnen: {{ sources_line }}. Alle prijzen zijn vraagprijzen. Indicatieve haalbaarheid rekent met het kader van Jan (minimaal 20 % winstmarge op de verkoopwaarde, 1.000 €/m² renovatie, 2.000 €/m² nieuwbouw, 8 % honoraria, excl. btw) en vergelijkingsprijzen per wijk; het is geen waardering en geen advies. Kaart, dossiers en wat-als-berekening: <a href="https://mac-mini-van-root-admin.tail69022d.ts.net:8710">dashboard</a> (alleen via Tailscale).</p>

<h2>Niveau 1 — Managementsamenvatting</h2>
<div class="tiles">
{% for t in tiles %}<div class="tile"><b>{{ t.value }}</b><span>{{ t.label }}</span></div>{% endfor %}
</div>
{% if baseline %}<div class="callout"><b>Nulmeting.</b> Dit is de eerste ronde: alle objecten zijn als uitgangspunt vastgelegd. Vanaf de volgende ronde worden nieuwe, gewijzigde en verdwenen objecten gemeld.</div>{% endif %}
<h3>Wat vandaag aandacht verdient</h3>
{% if attention %}<ul>{% for a in attention %}<li>{{ a }}</li>{% endfor %}</ul>{% else %}<p><b>Geen sterke kansen in deze ronde.</b> Dat is een eerlijke uitkomst, geen storing: de bronnen zijn gelezen (zie bronstatus).</p>{% endif %}
<h3>Bronstatus</h3>
<div class="wrap"><table><tr><th>Bron</th><th>Status</th><th class="n">Aantal</th><th>Toelichting</th></tr>
{% for s in source_rows %}<tr><td>{{ s.name }}</td><td><span class="pill {{ s.cls }}">{{ s.status }}</span></td><td class="n">{{ s.count }}</td><td>{{ s.note }}</td></tr>{% endfor %}
</table></div>
{% if weggestreept %}<h3>Weggestreept deze ronde</h3>
<p class="note">Deze waarden stonden bij zoveel objecten van dezelfde bron dat zij niet uit de advertentie kunnen komen, maar uit het zoekfilter op die site. Ze staan nu op onbekend; de objecten zelf blijven staan onder Onvolledig.</p>
<ul>{% for r in weggestreept %}<li>{{ r }}</li>{% endfor %}</ul>{% endif %}
{% if deadlines %}<h3>Naderende veilingdeadlines (≤ 14 dagen)</h3><div class="wrap"><table><tr><th>Sluiting</th><th>Veiling</th><th>Waar</th><th class="n">Taxatie</th><th>Blokkades</th></tr>
{% for d in deadlines %}<tr><td>{{ d.end_date }}</td><td><a href="{{ d.url }}">{{ d.sub }}</a></td><td>{{ d.where }}</td><td class="n">{{ d.valuation }}</td><td>{{ d.blockers }}</td></tr>{% endfor %}</table></div>{% endif %}

<h2>Niveau 2 — Gerangschikte selecties</h2>
{% for sec in sections %}
<h3>{{ sec.title }} <span class="note">({{ sec.rows|length }})</span></h3>
{% if sec.rows %}<div class="wrap"><table><tr><th>Object</th><th>Waar</th><th class="n">Vraagprijs</th><th class="n">m² geb. / perc.</th><th>Signalen</th><th>Indicatie</th><th>Status</th></tr>
{% for r in sec.rows %}<tr><td><a href="{{ r.url }}">{{ r.ref }}</a><br><span class="note">{{ r.type }}</span></td><td>{{ r.where }}</td><td class="n">{{ r.price }}{% if r.price_change %}<br><span class="pill {{ 'ok' if r.price_change.startswith('−') else 'warn' }}">{{ r.price_change }}</span>{% endif %}</td><td class="n">{{ r.m2 }}</td><td>{{ r.signals }}</td><td>{{ r.indicative }}</td><td><span class="pill {{ r.cls }}">{{ r.status }}</span></td></tr>{% endfor %}
</table></div>{% else %}<p class="note">Niets in deze categorie.</p>{% endif %}
{% endfor %}

<h2>Niveau 3 — Volledig overzicht van nieuw en gewijzigd</h2>
{% if all_rows %}<div class="wrap"><table><tr><th>Gebeurtenis</th><th>Object</th><th>Waar</th><th class="n">Vraagprijs</th><th class="n">m² geb. / perc.</th><th>Categorie</th><th>Voorfilter</th></tr>
{% for r in all_rows %}<tr><td><span class="pill {{ r.ev_cls }}">{{ r.event }}</span></td><td><a href="{{ r.url }}">{{ r.ref }}</a> <span class="note">{{ r.type }}</span></td><td>{{ r.where }}</td><td class="n">{{ r.price }}</td><td class="n">{{ r.m2 }}</td><td>{{ r.category }}</td><td>{{ r.verdict }}</td></tr>{% endfor %}
</table></div>{% else %}<p class="note">Geen nieuwe of gewijzigde objecten in het werkgebied.</p>{% endif %}

{% if companies %}<h3>Vennootschappen onder druk (handelsregister Alicante, 14 dagen)</h3>
<div class="wrap"><table><tr><th>Vennootschap</th><th>Handeling</th><th>Sector</th><th>Plaats</th><th>Datum</th></tr>
{% for c in companies %}<tr><td><a href="{{ c.url }}">{{ c.name }}</a></td><td>{{ c.acts }}</td><td>{{ c.sector }}</td><td>{{ c.place }}</td><td>{{ c.date }}</td></tr>{% endfor %}
</table></div>
<p class="note">Alleen de rechtspersoon, de handeling en de datum worden bewaard; namen van bestuurders en vereffenaars niet. Een ontbinding is een signaal, geen aanbod: of er onroerend goed bij zit moet je zelf nagaan.</p>{% endif %}

<h3>Publicatieborden van de gemeenten</h3>
<p class="note">Deze borden mogen niet automatisch gelezen worden (robots.txt verbiedt het, gecontroleerd 17-09-2026), dus open ze zelf: {% for b in tablones %}<a href="{{ b.url }}">{{ b.town }}</a>{% if not loop.last %} · {% endif %}{% endfor %}.</p>

<h2>Prioriteiten</h2>
{% if priorities %}<ul>{% for p in priorities %}<li>{{ p }}</li>{% endfor %}</ul>{% else %}<p class="note">Geen nieuwe acties uit deze ronde.</p>{% endif %}
<p class="note">Gegenereerd {{ generated }} · run {{ run_id }} · {{ attribution }}</p>
</div></body></html>"""


def eur(v) -> str:
    if v is None:
        return "—"
    return f"{v:,.0f} €".replace(",", ".")


def safe_url(u) -> str:
    return u if isinstance(u, str) and u.lower().startswith(("http://", "https://")) else "#"


def m2(b, p) -> str:
    return f"{int(b) if b else '—'} / {int(p) if p else '—'}"


def _cls_for(verdict: str) -> str:
    if verdict.startswith("kandidaat: haalt eis"):
        return "ok"
    if verdict.startswith("kandidaat"):
        return "info"
    if verdict == "watchlist":
        return "warn"
    return "neutral"


def build(ctx: dict) -> tuple[str, str]:
    env = Environment(loader=BaseLoader(), autoescape=select_autoescape(["html"]))
    html = env.from_string(HTML).render(**ctx)
    # Markdown-samenvatting (Discord/e-mail)
    md = [f"# Deal Hunter — ronde {ctx['slot']} · {ctx['day']}", "", f"**{ctx['headline']}**", "", "Dashboard: https://mac-mini-van-root-admin.tail69022d.ts.net:8710", ""]
    md += [f"- {t['label']}: **{t['value']}**" for t in ctx["tiles"]]
    md += ["", "**Aandacht:**"] + ([f"- {a}" for a in ctx["attention"]] or ["- Geen sterke kansen in deze ronde."])
    md += ["", "**Bronnen:** " + "; ".join(f"{s['name']}: {s['status']} ({s['count']})" for s in ctx["source_rows"])]
    if ctx.get("weggestreept"):
        md += ["", "**Weggestreept deze ronde** (waarde kwam uit een zoekfilter, niet uit de advertentie):"]
        md += [f"- {r}" for r in ctx["weggestreept"]]
    if ctx["deadlines"]:
        md += ["", "**Veilingdeadlines ≤ 14 dagen:**"] + [f"- {d['end_date']} · {d['sub']} · {d['where']} · {d['valuation']} · {d['blockers']}" for d in ctx["deadlines"]]
    for sec in ctx["sections"]:
        if sec["rows"]:
            md += ["", f"**{sec['title']}**"] + [f"- {r['ref']} · {r['where']} · {r['price']} · {r['m2']} m² · {r['status']} · {r['url']}" for r in sec["rows"][:8]]
    if ctx.get("companies"):
        md += ["", "**Vennootschappen onder druk (14 dagen):**"] + [
            f"- {c['name']} · {c['acts']}" + (f" · {c['sector']}" if c["sector"] != "—" else "") + f" · {c['date']}"
            for c in ctx["companies"][:8]]
    if ctx["priorities"]:
        md += ["", "**Prioriteiten:**"] + [f"- {p}" for p in ctx["priorities"]]
    return html, "\n".join(md)


def context(store, run_id: int, slot: str, source_meta: dict, baseline: bool, listing_events: dict, auction_events: dict) -> dict:
    """Bouwt de rapportcontext uit de opslag en de gebeurtenissen van deze run."""
    now = datetime.now(config.TZ)
    ev_rows = store.events_for_run(run_id)
    by_kind: dict[str, list] = {}
    for e in ev_rows:
        by_kind.setdefault(e["kind"], []).append(e)

    def listing_row(row, event: str = "") -> dict:
        pf = json.loads(row["prefilter"] or "{}")
        sig = json.loads(row["signals"] or "{}")
        ind = pf.get("indicative") or {}
        ind_txt = "—"
        if ind and (ind.get("max_price") or ind.get("roi_base") is not None):
            mp = ind.get("max_price") or {}
            ind_txt = (f"max. koopprijs {eur(mp.get('conservative'))} / {eur(mp.get('base'))} / {eur(mp.get('upside'))} "
                       f"(voorzichtig / basis / gunstig; {ind['scenario']}, n={ind['comps_n']})")
        elif ind.get("note"):
            ind_txt = ind["note"]
        sigs = ", ".join((sig.get("renovation_signals") or [])[:3] + (sig.get("licence_claims") or [])[:2] + (sig.get("special_signals") or [])[:2]) or "—"
        hist = store.price_history(int(row["id"]))
        pc = ""
        if len(hist) >= 2 and hist[-2][1] and hist[-1][1]:
            d = (hist[-1][1] - hist[-2][1]) / hist[-2][1] * 100
            pc = f"{'−' if d < 0 else '+'}{abs(d):.1f} % (was {eur(hist[-2][1])})"
        verdict = pf.get("verdict", "—")
        return {"ref": row["source_ref"], "url": safe_url(row["url"]), "type": row["type"], "where": f"{row['town_raw'] or ''} · {row['location_detail'] or ''}".strip(" ·"),
                "price": eur(row["price"]), "price_change": pc, "m2": m2(row["built_m2"], row["plot_m2"]), "signals": sigs,
                "indicative": ind_txt, "status": verdict, "cls": _cls_for(verdict), "category": pf.get("category", row["category"] or "—"),
                "verdict": verdict, "event": event, "ev_cls": {"NIEUW": "ok", "PRIJS GEWIJZIGD": "warn", "NIET MEER GEVONDEN": "bad", "OPNIEUW AANGEBODEN": "info", "GEWIJZIGD": "neutral", "NULMETING": "neutral"}.get(event, "neutral"),
                "_roi": ind.get("roi_conservative") if ind else None, "_price": row["price"] or 0}

    # alle actieve advertenties in het werkgebied, met voorfilter
    active = store.active_listings(area_only=True)
    cats = {"Beste renovatieobjecten": [], "Beste percelen en ontwikkelkansen": [], "Appartementen aan zee met renovatiesignaal": [], "Bijzondere situaties": []}
    for row in active:
        pf = json.loads(row["prefilter"] or "{}")
        if not pf.get("verdict", "").startswith(("kandidaat", "watchlist")):
            continue
        r = listing_row(row)
        c = pf.get("category")
        if c == "renovatie":
            cats["Beste renovatieobjecten"].append(r)
        elif c == "perceel":
            cats["Beste percelen en ontwikkelkansen"].append(r)
        elif c and c.startswith("appartement"):
            cats["Appartementen aan zee met renovatiesignaal"].append(r)
        elif c == "bijzonder":
            cats["Bijzondere situaties"].append(r)
    for k in cats:
        cats[k].sort(key=lambda r: (-(r["_roi"] if r["_roi"] is not None else -9), r["_price"]))
        cats[k] = cats[k][:12]

    price_changes = []
    for e in by_kind.get("PRIJS GEWIJZIGD", []):
        rows = store.listings_by_ids([e["listing_id"]])
        if rows:
            price_changes.append(listing_row(rows[0], "PRIJS GEWIJZIGD"))
    sections = [{"title": k, "rows": v} for k, v in cats.items()] + [{"title": "Prijswijzigingen deze ronde", "rows": price_changes}]

    # veilingen
    deadlines, auction_rows = [], []
    today = now.date()
    for a in store.active_auctions():
        bl = json.loads(a["blockers"] or "[]")
        where = f"{a['town'] or ''} {a['postcode'] or ''}".strip() or ("ligging onbekend" if a["source"] == "boe" else "—")
        sub = (json.loads(a["sub_ids"] or "[]") or [a["boe_id"] or a["source_ref"]])[0]
        item = {"end_date": a["end_date"] or "—", "sub": sub, "where": f"{'AEAT' if a['source']=='aeat' else a['department'] or 'BOE'} · {where}",
                "valuation": eur(a["valuation"]), "blockers": "; ".join(bl) or "—", "url": safe_url(a["url"]), "area": a["area"]}
        if a["area"]:
            auction_rows.append(item)
        if a["end_date"]:
            try:
                dd = date.fromisoformat(a["end_date"][:10])
                if 0 <= (dd - today).days <= 14 and (a["area"] or a["source"] == "boe" and (a["town"] or "").startswith("DENIA")):
                    deadlines.append(item)
            except ValueError:
                pass
    sections.append({"title": "Veilingen in het werkgebied (AEAT-lijst; BOE alleen met bevestigde ligging)", "rows": [
        {"ref": r["sub"], "url": safe_url(r["url"]), "type": "veiling", "where": r["where"], "price": r["valuation"], "price_change": "", "m2": "—",
         "signals": r["blockers"], "indicative": f"sluit {r['end_date']}", "status": "onderzoeken", "cls": "info"} for r in auction_rows]})

    # niveau 3
    all_rows = []
    for kind in ("NIEUW", "PRIJS GEWIJZIGD", "OPNIEUW AANGEBODEN", "GEWIJZIGD", "NIET MEER GEVONDEN"):
        for e in by_kind.get(kind, []):
            if e["listing_id"]:
                rows = store.listings_by_ids([e["listing_id"]])
                if rows and rows[0]["area"]:
                    all_rows.append(listing_row(rows[0], kind))

    # vennootschappen onder druk (BORME). Alleen rechtspersoon, handeling en datum.
    company_rows = []
    for c in store.recent_companies(days=14, limit=25):
        company_rows.append({"name": c["name"], "acts": ", ".join(json.loads(c["acts"] or "[]")),
                             "sector": c["sector"] or "—", "place": c["place"] or "—",
                             "date": c["published_on"] or "—", "url": safe_url(c["url"]),
                             "prio": c["priority"] or 0})
    company_rows.sort(key=lambda r: (-r["prio"], r["date"]), reverse=False)

    counts = {k: len(v) for k, v in by_kind.items()}
    n_area = len(active)
    n_cand = sum(len(s["rows"]) for s in sections[:4])
    tiles = [
        {"value": source_meta.get("bp", {}).get("fetched", "—"), "label": "advertenties ontvangen (BP)"},
        {"value": n_area, "label": "actieve objecten in werkgebied"},
        {"value": counts.get("NIEUW", 0) if not baseline else counts.get("NULMETING", 0), "label": "nieuw" if not baseline else "vastgelegd (nulmeting)"},
        {"value": counts.get("PRIJS GEWIJZIGD", 0), "label": "prijs gewijzigd"},
        {"value": counts.get("NIET MEER GEVONDEN", 0), "label": "niet meer gevonden"},
        {"value": n_cand, "label": "kandidaten en watchlist"},
        {"value": len(auction_rows), "label": "veilingen in werkgebied"},
        {"value": len(company_rows), "label": "vennootschappen onder druk (14 dagen)"},
    ]
    attention = []
    for sec in sections[:4]:
        for r in sec["rows"]:
            if r["status"].startswith("kandidaat: haalt eis"):
                attention.append(f"{r['ref']} ({r['where']}, {r['price']}): {r['indicative']} — {r['url']}")
    for r in price_changes:
        if r["price_change"].startswith("−"):
            attention.append(f"Prijsdaling {r['price_change']} bij {r['ref']} ({r['where']}, nu {r['price']}) — {r['url']}")
    for d in deadlines:
        attention.append(f"Veiling {d['sub']} sluit {d['end_date']} ({d['where']}; {d['blockers']}) — {d['url']}")
    attention = attention[:10]

    src_rows = []
    for key, name in (("bp", "Background Properties-feed"), ("boe", "BOE-sumario"), ("aeat", "AEAT-veilinglijst"),
                      ("borme", "BORME (handelsregister Alicante)")):
        s = store.source(key)
        m = source_meta.get(key, {})
        ok = bool(s and s["last_status"] == "ok")
        src_rows.append({"name": name, "status": "gelezen" if ok else "BRON NIET BEREIKBAAR", "cls": "ok" if ok else "bad",
                         "count": m.get("fetched", m.get("count", s["last_count"] if s else "—")) if (m or s) else "—",
                         "note": m.get("note") or (s["last_error"] if s and s["last_error"] else "")})

    priorities = []
    for a in attention[:5]:
        priorities.append(f"{a.split(' — ')[0]} → dossier openen, kadastrale referentie en documenten opvragen (na akkoord Jan) — Jan/architect — binnen 3 werkdagen")
    headline = ("Nulmeting vastgelegd" if baseline else
                f"{counts.get('NIEUW', 0)} nieuw, {counts.get('PRIJS GEWIJZIGD', 0)} prijswijzigingen, {len(attention)} punten die aandacht vragen")
    return {
        "slot": slot, "day": now.strftime("%d-%m-%Y"), "area_label": "Jávea · Benitachell · Moraira", "headline": headline,
        "sources_line": "; ".join(f"{s['name']} ({s['status']})" for s in src_rows), "tiles": tiles, "baseline": baseline,
        "attention": attention, "source_rows": src_rows, "deadlines": deadlines, "sections": sections, "all_rows": all_rows,
        "priorities": priorities, "generated": now.strftime("%d-%m-%Y %H:%M %Z"), "run_id": run_id,
        "companies": company_rows, "tablones": [{"town": a, "url": b} for a, b in config.TABLONES],
        "attribution": config.AEAT_ATTRIBUTION + " · " + config.BORME_ATTRIBUTION,
        # Waarden die deze ronde zijn weggestreept omdat ze een hele bron domineren en dus uit een
        # keuzelijst komen. Hoort in het bericht: er verdwijnt een bedrag uit de lijst en Jan moet
        # weten waarom (besluit 27-09-2026).
        "weggestreept": (source_meta.get("weggestreept") or {}).get("regels") or [],
    }

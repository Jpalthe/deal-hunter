"""TREE Deal Hunter — dashboard (FastAPI + statische frontend).

Draait als launchd-dienst com.tree.deal-hunter-review op 127.0.0.1:8710. Leest de SQLite-opslag,
rekent haalbaarheid live met tools/haalbaarheid.py, schrijft alleen beoordelingen. Geen
contactgegevens, geen berichten naar buiten.

TOEGANG (sinds 26-09-2026) — er zit nu wél een slot in: middleware `bewaak_toegang`
met een wachtwoord en een ondertekend sessiecookie (zie dh/toegang.py). Dat slot staat
UIT zolang er geen DH_WACHTWOORD_HASH is ingesteld; zet er dus een via /instellingen.
Het blijft de tweede laag: Cloudflare Access aan de rand van de tunnel is de eerste.
Ontsluit deze dienst nooit zonder dat er minstens één slot vóór of in staat.
"""
from __future__ import annotations

import json
import re
import threading
import time
from collections import OrderedDict
from datetime import datetime, timedelta

import httpx
from defusedxml import ElementTree as ET
from fastapi import Body, FastAPI, HTTPException, Query, Request
from fastapi.responses import FileResponse, HTMLResponse, JSONResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles

from . import alerts, config, dubbel, feasibility, focus, toegang, zonewaarde
from .store import Store
from .summary import (bouw_ctx as summary_ctx, AREA_LABEL, CLASS_LABEL, ZONE_LABEL, events_since, jload,
                      listing_summary)

STATIC = config.ROOT / "dh" / "static"
app = FastAPI(title="TREE Deal Hunter", docs_url=None, redoc_url=None, openapi_url=None)
app.mount("/static", StaticFiles(directory=str(STATIC)), name="static")


# ── Toegang ──────────────────────────────────────────────────────────────────
# Tweede slot, achter Cloudflare Access. Staat uit zolang er geen wachtwoord is
# ingesteld (`python3 scripts/zet-wachtwoord.py`), zodat dit een draaiende
# dienst niet stilzet. Zie dh/toegang.py voor het waarom.

INLOG_PAGINA = """<!doctype html>
<html lang="nl"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Deal Hunter</title>
<meta name="robots" content="noindex,nofollow">
<meta name="theme-color" content="#1C2220">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Newsreader:opsz,wght@6..72,300;6..72,400&family=Inter+Tight:wght@400;500&family=JetBrains+Mono:wght@400&display=swap">
<style>
 /* Huisstijl TREE: vier kleuren, drie letterfamilies, geen radius, geen schaduw. */
 :root{--paper:#F7F5F0;--pine:#2B3331;--deep:#1C2220;--beige:#B8A07A;
       --pine-70:rgba(43,51,49,.7);--pine-45:rgba(43,51,49,.45);
       --rule:rgba(43,51,49,.28);--fout:#8C3A2B;
       --serif:"Newsreader",Georgia,serif;--sans:"Inter Tight",Arial,sans-serif;
       --mono:"JetBrains Mono",Consolas,monospace}
 *{box-sizing:border-box}
 body{margin:0;min-height:100vh;background:var(--paper);color:var(--pine);
      font:17px/1.6 var(--sans);display:grid;grid-template-rows:auto 1fr}
 /* Het beeld staat boven het formulier, nooit eronder: de kop hoort op papier. */
 .beeld{height:38vh;min-height:220px;background:#ded9d0 url("/static/beeld/inloggen.jpg") center 62%/cover no-repeat}
 main{display:grid;place-items:center;padding:48px 24px 64px}
 form{width:min(92vw,380px);display:grid;gap:24px}
 .merk{font:400 11px/1 var(--mono);letter-spacing:.18em;text-transform:uppercase;color:var(--pine-45)}
 h1{font:300 40px/1.05 var(--serif);letter-spacing:-.022em;margin:14px 0 6px}
 .onder{font-size:15px;color:var(--pine-70);margin:0}
 label{font:400 11px/1 var(--mono);letter-spacing:.18em;text-transform:uppercase;color:var(--pine-45);display:block;margin-bottom:8px}
 input{width:100%;padding:13px 16px;border:1px solid rgba(43,51,49,.55);border-radius:0;
       background:transparent;font:400 16px/1.4 var(--sans);color:var(--pine)}
 input:focus-visible{outline:2px solid var(--pine);outline-offset:2px}
 button{width:100%;min-height:44px;padding:13px;border:0;border-radius:0;background:var(--pine);
        color:var(--paper);font:500 14px/1 var(--sans);letter-spacing:.02em;cursor:pointer;
        transition:background 200ms ease-out}
 button:hover{background:var(--deep)}
 p.fout{margin:0;padding:8px 0 8px 16px;border-left:2px solid var(--fout);color:var(--fout);font-size:15px}
 .voet{margin-top:8px;padding-top:20px;border-top:1px solid rgba(43,51,49,.14);
       font-size:14px;color:var(--pine-45)}
 @media(min-width:900px){
   body{grid-template-rows:none;grid-template-columns:1fr 1fr}
   .beeld{height:100vh;min-height:0;background-position:center 55%}
   main{padding:24px}
 }
</style></head><body>
<div class="beeld" role="img" aria-label="De geterrasseerde heuvels achter J&aacute;vea bij het eerste licht, met verspreide huizen en de Montg&oacute; in de nevel."></div>
<main>
<form method="post" action="/inloggen">
 <div>
  <p class="merk">TREE &middot; Find. Build. Live.</p>
  <h1>Deal Hunter</h1>
  <p class="onder">Renovatieobjecten, percelen en veilingen in de Marina Alta.</p>
 </div>
 __FOUT__
 <div>
  <label for="ww">Wachtwoord</label>
  <input id="ww" type="password" name="wachtwoord" autofocus
         autocomplete="current-password" required>
 </div>
 <button type="submit">Openen</button>
 <p class="voet">Dit dashboard bevat maximale koopprijzen en onderhandelplannen. Alleen voor Jan.</p>
</form>
</main></body></html>"""


def _inlogpagina(fout: str = "") -> HTMLResponse:
    melding = f'<p class="fout">{fout}</p>' if fout else ""
    status = 401 if fout else 200
    return HTMLResponse(INLOG_PAGINA.replace("__FOUT__", melding), status_code=status)


@app.get("/inloggen", response_class=HTMLResponse)
def inlogpagina():
    return _inlogpagina()


@app.post("/inloggen")
async def inloggen(request: Request):
    """Formulier handmatig ontleden: zo is python-multipart niet nodig."""
    from urllib.parse import parse_qs

    adres = request.client.host if request.client else "onbekend"
    if toegang.te_veel_pogingen(adres):
        return _inlogpagina("Te veel pogingen. Probeer het over een kwartier opnieuw.")

    ruw = (await request.body()).decode("utf-8", "replace")
    wachtwoord = (parse_qs(ruw).get("wachtwoord") or [""])[0]

    if not toegang.klopt_wachtwoord(wachtwoord):
        toegang.noteer_poging(adres)
        return _inlogpagina("Dat wachtwoord klopt niet.")

    toegang.wis_pogingen(adres)
    antwoord = RedirectResponse("/m", status_code=303)
    antwoord.set_cookie(
        toegang.COOKIE_NAAM,
        toegang.maak_cookie(),
        max_age=toegang.GELDIG_SECONDEN,
        httponly=True,
        samesite="lax",
        # Alleen over https, behalve lokaal op de Mac zelf.
        secure=request.url.scheme == "https",
        path="/",
    )
    return antwoord


@app.post("/api/wachtwoord")
def wachtwoord_zetten(body: dict = Body(...)):
    """Zet of wijzigt het wachtwoord — bedoeld voor de telefoon.

    Alleen de hash gaat naar .env; het wachtwoord zelf wordt nergens bewaard,
    gelogd of teruggetoond. Staat er al een wachtwoord, dan moet het oude mee:
    anders zou iemand met een geldige sessie het stilletjes kunnen overnemen.
    """
    nieuw = str(body.get("nieuw") or "")
    if len(nieuw) < 12:
        raise HTTPException(400, "Kies er een van minstens twaalf tekens.")
    if toegang.controle_actief():
        if not toegang.klopt_wachtwoord(str(body.get("oud") or "")):
            raise HTTPException(400, "Het huidige wachtwoord klopt niet.")
    config.save_env_key("DH_WACHTWOORD_HASH", toegang.maak_hash(nieuw))
    # Alle bestaande cookies vervallen: de ondertekensleutel hangt aan de hash.
    return {"ok": True, "opnieuw_inloggen": True}


@app.get("/api/bezorgstand")
def bezorgstand():
    """Komen de meldingen aan? De app toont dit als balk bovenaan.

    Tot 26-09-2026 ging dit geruisloos mis: 24 meldingen zijn overgeslagen
    omdat er geen webhook in .env stond, en dat was nergens te zien.
    """
    store = Store()
    try:
        return alerts.bezorgstand(store)
    finally:
        store.close()


@app.get("/api/toegang")
def toegang_status():
    """Zegt alleen óf er een wachtwoord staat, nooit wat het is."""
    return {"beveiligd": toegang.controle_actief()}


@app.middleware("http")
async def bewaak_toegang(request: Request, call_next):
    if not toegang.controle_actief() or toegang.pad_is_vrij(request.url.path):
        return await call_next(request)
    if toegang.cookie_geldig(request.cookies.get(toegang.COOKIE_NAAM)):
        return await call_next(request)
    # TREE Hub leest de kansen uit; dat is een programma zonder browser en dus
    # zonder cookie. Alleen lezen, alleen op /api/, en alleen als er werkelijk
    # een DH_DIENST_TOKEN is ingesteld.
    if request.url.path.startswith("/api/") and request.method == "GET":
        if toegang.token_klopt(request.headers.get(toegang.TOKEN_KOP)):
            return await call_next(request)
    # Een pagina krijgt de inlog te zien; een API-verzoek een eerlijke 401,
    # zodat de app niet stilletjes HTML in een JSON-veld krijgt.
    if request.url.path.startswith("/api/"):
        return JSONResponse({"error": "niet_aangemeld"}, status_code=401)
    return _inlogpagina()


_VERSIE = re.compile(r'(?P<attr>href|src)="(?P<pad>/static/[^"?]+\.(?:css|js))"')


def _pagina(naam: str) -> HTMLResponse:
    """Een HTML-pagina met een versiemerk achter elke eigen stylesheet en script.

    Zonder dit merk houdt de browser de oude app.css en app.js vast. Op de
    telefoon is dat erger dan op een laptop: een webapp op het beginscherm
    ververst niet met ctrl-F5, dus een verbetering komt daar pas aan als de
    cache uit zichzelf verloopt. Het merk is de wijzigingstijd van het bestand
    zelf, dus het verandert precies wanneer het bestand verandert en op geen
    enkel ander moment."""
    html = (STATIC / naam).read_text(encoding="utf-8")

    def merk(m: "re.Match[str]") -> str:
        bestand = STATIC / m.group("pad").removeprefix("/static/")
        try:
            v = int(bestand.stat().st_mtime)
        except OSError:
            return m.group(0)
        return f'{m.group("attr")}="{m.group("pad")}?v={v}"'

    return HTMLResponse(_VERSIE.sub(merk, html))


@app.get("/", response_class=HTMLResponse)
def index():
    return _pagina("index.html")


@app.get("/m", response_class=HTMLResponse)
def mobile():
    """Telefoonpagina: los van het dashboard, gemaakt voor duimbediening en een icoon op het beginscherm."""
    return _pagina("m.html")


@app.get("/manifest.webmanifest")
def manifest():
    return FileResponse(str(STATIC / "manifest.webmanifest"), media_type="application/manifest+json")


@app.get("/apple-touch-icon.png")
def apple_icon():
    return FileResponse(str(STATIC / "icon-180.png"), media_type="image/png")


DOSSIERS = config.ROOT / "rapporten" / "dossiers"


@app.get("/dossiers/{name}")
def dossier_page(name: str):
    """Een dossier als losse pagina. Alleen bestanden uit de dossiermap, geen paden erbuiten."""
    if "/" in name or ".." in name or not name.endswith(".html"):
        raise HTTPException(404)
    p = DOSSIERS / name
    if not p.exists():
        raise HTTPException(404, "dossier nog niet gemaakt")
    return FileResponse(str(p), media_type="text/html")


@app.get("/api/dossiers")
def dossiers():
    """Welke dossiers er klaarstaan, en welke objecten er volgens de rangschikking een verdienen."""
    store = Store()
    try:
        klaar = sorted(p.stem for p in DOSSIERS.glob("*.html") if p.stem != "index") if DOSSIERS.exists() else []
        from . import dossier as dz
        top = dz.rank(store, 12)
        return {"klaar": klaar, "index": (DOSSIERS / "index.html").exists(),
                "aanbevolen": [{"id": t["id"], "ref": t["ref"], "zone": t["zone_label"] or t["area_label"],
                                "price": t["price"], "result": (t.get("calc") or {}).get("result"),
                                "months": (t.get("calc") or {}).get("months"), "class": t["class"],
                                "open_punten": t.get("_open_punten"), "niet_onderzocht": t.get("_niet_onderzocht"),
                                "heeft_dossier": t["ref"] in klaar} for t in top]}
    finally:
        store.close()


@app.get("/api/companies")
def companies(days: int = Query(30, ge=1, le=365)):
    """Vennootschappen in ontbinding, liquidatie of faillissement (BORME, provincie Alicante).
    Alleen rechtspersoon, handeling en datum; nooit namen van bestuurders of vereffenaars."""
    store = Store()
    try:
        return [{"id": r["id"], "name": r["name"], "registry_no": r["registry_no"], "acts": jload(r["acts"], []),
                 "sector": r["sector"], "place": r["place"], "area": r["area"], "priority": r["priority"],
                 "published_on": r["published_on"], "url": r["url"], "borme_id": r["borme_id"]}
                for r in store.recent_companies(days=days)]
    finally:
        store.close()


@app.get("/api/alerts")
def alerts_list(days: int = Query(14, ge=1, le=120)):
    """Wat er de afgelopen dagen als sterke kans is gemeld, met de vraagprijs op dat moment."""
    store = Store()
    try:
        rows = store.alerts_since(days=days)
        by_id = {}
        for r in rows:
            ref = store.con.execute("SELECT source_ref, area, location_detail FROM listings WHERE id=?", (r["listing_id"],)).fetchone()
            by_id.setdefault(int(r["listing_id"]), {
                "listing_id": r["listing_id"], "tier": r["tier"], "class": r["class"], "at": r["at"],
                "price": r["price"], "max_price": r["max_price"], "room": r["room"],
                "ref": ref["source_ref"] if ref else None, "area": ref["area"] if ref else None,
                "location": ref["location_detail"] if ref else None, "delivered": r["delivered"],
                "baseline": "nulmeting" in (r["delivered"] or "")})
        return list(by_id.values())
    finally:
        store.close()


@app.get("/api/tablones")
def tablones():
    """De drie gemeentelijke publicatieborden: handmatig openen. Hun robots.txt verbiedt automatisch
    lezen (gecontroleerd 17-09-2026), dus het systeem haalt hier niets op."""
    return {"note": "Automatisch lezen is niet toegestaan (robots.txt). Open deze borden zelf.",
            "boards": [{"town": t, "url": u} for t, u in config.TABLONES]}


# De samenvatting rekent alle 1.600 objecten door en kost zo'n vijf seconden; de lijst kost er twee.
# Die uitkomsten veranderen alleen als er een ronde draait of als Jan een merkje zet, dus ze worden
# kort bewaard. Zonder dit wachtte de telefoon tien seconden op een compleet scherm.
_CACHE: dict[str, tuple[float, object]] = {}
_CACHE_LOCK = threading.Lock()
CACHE_S = 120


def _stand() -> str:
    """Een goedkope vingerafdruk van de databasestand.

    De rondes draaien in een ánder proces dan deze webdienst, dus een cache op tijd alleen zou na
    een ronde nog twee minuten oude cijfers tonen. Deze drie tellingen kosten milliseconden en
    veranderen zodra er iets gebeurt."""
    store = Store()
    try:
        r = store.con.execute(
            "SELECT (SELECT MAX(id) FROM snapshots), (SELECT MAX(id) FROM events), "
            "(SELECT COUNT(*) FROM markeringen), (SELECT MAX(at) FROM markeringen)").fetchone()
        return "|".join(str(x) for x in r)
    except Exception:  # noqa: BLE001
        return "onbekend"
    finally:
        store.close()


def _cached(sleutel: str, maak):
    sleutel = f"{sleutel}@{_stand()}"
    with _CACHE_LOCK:
        hit = _CACHE.get(sleutel)
        if hit and (time.time() - hit[0]) < CACHE_S:
            return hit[1]
    waarde = maak()
    with _CACHE_LOCK:
        _CACHE[sleutel] = (time.time(), waarde)
    return waarde


def _cache_leeg() -> None:
    with _CACHE_LOCK:
        _CACHE.clear()


@app.get("/api/summary")
def summary():
    return _cached("summary", _summary_bouw)


def _summary_bouw():
    store = Store()
    try:
        ev7 = events_since(store, 7)
        rows = store.active_listings(area_only=True)
        items = [listing_summary(store, r, ev7) for r in rows]
        by_class: dict[str, int] = {}
        for it in items:
            by_class[it["class"]] = by_class.get(it["class"], 0) + 1
        runs = [dict(r) for r in store.con.execute("SELECT slot, started_at, finished_at, status FROM runs WHERE slot NOT LIKE 'import%' ORDER BY id DESC LIMIT 6")]
        sources = [dict(r) for r in store.con.execute("SELECT key, last_success_at, last_attempt_at, last_status, last_count, last_error FROM sources")]
        auctions = [a for a in store.active_auctions() if a["area"]]
        new7 = sum(1 for it in items if "NIEUW" in it["events_7d"])
        drops7 = sum(1 for it in items if "PRIJS GEWIJZIGD" in it["events_7d"])
        now = datetime.now(config.TZ)
        # Jan 25-09-2026: 's ochtends en aan het begin van de avond (launchd 08:00 en 18:30)
        slots = [now.replace(hour=h, minute=m, second=0, microsecond=0) for h, m in ((8, 0), (18, 30))]
        nxt = next((s for s in slots if s > now), slots[0] + timedelta(days=1))
        kader, params, _, _ = feasibility.inputs()
        return {
            "generated": now.isoformat(timespec="seconds"), "next_run": nxt.isoformat(timespec="minutes"),
            "counts": {"active": len(items), "by_area": {a: sum(1 for i in items if i["area"] == a) for a in AREA_LABEL},
                       "by_class": by_class, "new_7d": new7, "price_changes_7d": drops7, "auctions_in_area": len(auctions),
                       "idealista": sum(1 for i in items if i["source"] == "idealista"), "reviewed": sum(1 for i in items if i["review"]),
                       "alerts_14d": len({int(a["listing_id"]) for a in store.alerts_since(14)}),
                       "companies_30d": len(store.recent_companies(days=30))},
            "runs": runs, "sources": sources, "ai_cost_month": round(store.ai_cost_month(), 2),
            "kader": {"margin": kader.get("winstmarge_op_verkoop_min", 0.20), "reno_rate": kader["bouwkosten_eur_per_m2"]["renovatie"],
                      "new_rate": kader["bouwkosten_eur_per_m2"]["nieuwbouw"], "fees_pct": round(params["architect_pct_of_pem"] + params["aparejador_pct_of_pem"], 4),
                      "commission_pct": params["agent_commission_pct"], "budget": kader.get("koopbudget_eur"),
                      "months": kader.get("doorlooptijd_max_maanden"),
                      "finance_rate": params.get("finance_rate_default"),
                      "doorlooptijd": kader.get("doorlooptijd"), "capaciteit": kader.get("capaciteit")},
            "class_labels": CLASS_LABEL, "zone_labels": ZONE_LABEL, "area_labels": AREA_LABEL,
            "focus": {**focus.instelling(), "omschrijving": focus.omschrijving(),
                      "aantal": sum(1 for i in items if focus.past(i))},
        }
    finally:
        store.close()


def focus_rijen(store: Store):
    """Zie dh/focus.rijen: alleen de rijen die binnen de focus kunnen vallen."""
    return focus.rijen(store)


@app.get("/api/listings")
def listings(focus_only: bool = Query(False, alias="focus"),
             tab: str = Query("", description="kansen, teduur, later, buiten, onvolledig of leeg voor alle")):
    """De objecten voor de app.

    Zonder `focus` en zonder `tab`: alles wat actief is. Met `focus=1` of een `tab`: alleen de rijen
    die op een tabblad kunnen belanden, wat schelen 1.214 → ongeveer 670 doorrekeningen."""
    return _cached(f"listings:{focus_only}:{tab}", lambda: _listings_bouw(focus_only, tab))


def _listings_bouw(focus_only: bool, tab: str):
    store = Store()
    try:
        ev7 = events_since(store, 7)
        beperkt = bool(focus_only or tab)
        rows = focus_rijen(store) if beperkt else store.active_listings(area_only=True)
        ctx = summary_ctx(store)
        items = [listing_summary(store, r, ev7, ctx) for r in rows]
        if tab:
            gevraagd = {t.strip() for t in tab.split(",") if t.strip()}
            uit = [i for i in items if i.get("tab") in gevraagd]
            # Dezelfde woning via twee bronnen wordt één kaartje (Jan 26-09-2026). Per tabblad
            # samenvoegen, anders zou een woning van het ene tabblad er op het andere bij verdwijnen.
            if (focus.instelling().get("dubbel_samenvoegen", True)):
                samen = []
                for t in gevraagd:
                    samen += dubbel.voeg_samen([i for i in uit if i.get("tab") == t])
                return samen
            return uit
        if focus_only:
            return [i for i in items if i.get("in_focus")]
        return items
    finally:
        store.close()


@app.get("/instellingen", response_class=HTMLResponse)
def instellingen_pagina():
    return FileResponse(config.ROOT / "dh" / "static" / "instellingen.html")


# Vorm waaraan een Discord-webhook moet voldoen. Voorkomt dat er per ongeluk iets anders in .env
# belandt, bijvoorbeeld een bot-token of een halve link.
WEBHOOK_VORM = re.compile(r"^https://(?:ptb\.|canary\.)?discord(?:app)?\.com/api/webhooks/\d{5,}/[\w-]{20,}$")
EMAIL_VORM = re.compile(r"^[^@\s,]+@[^@\s,]+\.[a-z]{2,}$", re.I)


@app.get("/api/instellingen")
def instellingen_lezen():
    """Welke sleutels zijn gevuld. Nooit de waarden zelf, ook niet gedeeltelijk."""
    env = config.load_env()
    # Het wachtwoord staat bewust niet in deze lijst: het hoort in een echt
    # wachtwoordveld (POST /api/wachtwoord), niet in een gewoon tekstvak.
    return {"sleutels": [{"naam": k, "uitleg": v, "gevuld": bool((env.get(k) or "").strip())}
                         for k, v in config.INSTELBAAR.items()
                         if k != "DH_WACHTWOORD_HASH"]}


@app.post("/api/instellingen")
def instellingen_zetten(body: dict = Body(...)):
    """Zet één sleutel. Bedoeld voor de telefoon: Jan kan daar geen bestand bewerken."""
    naam = str(body.get("naam") or "")
    waarde = str(body.get("waarde") or "").strip()
    if naam not in config.INSTELBAAR:
        raise HTTPException(400, "onbekende instelling")
    if naam == "DH_WACHTWOORD_HASH":
        # Hier komt nooit een wachtwoord binnen: dat zou het onversleuteld in
        # .env zetten. Zetten gaat via /api/wachtwoord, dat eerst hasht.
        raise HTTPException(400, "het wachtwoord zet je via het wachtwoordveld")
    if waarde:
        if naam == "DISCORD_WEBHOOK_URL" and not WEBHOOK_VORM.match(waarde):
            raise HTTPException(400, "Dat ziet er niet uit als een Discord-webhook. "
                                     "Hij begint met https://discord.com/api/webhooks/ en heeft daarna "
                                     "een nummer en een lange code.")
        if naam == "RESEND_API_KEY" and not waarde.startswith("re_"):
            raise HTTPException(400, "Een sleutel van Resend begint met re_.")
        if naam in ("DH_EMAIL_TO", "DH_EMAIL_FROM"):
            adres = waarde.split("<")[-1].rstrip(">").strip()
            if not EMAIL_VORM.match(adres):
                raise HTTPException(400, "Dat is geen geldig e-mailadres.")
    try:
        config.save_env_key(naam, waarde)
    except ValueError as e:
        raise HTTPException(400, str(e)) from e
    return {"ok": True, "naam": naam, "gevuld": bool(waarde)}


@app.post("/api/instellingen/test")
def instellingen_test():
    """Stuurt één proefbericht via de kanalen die zijn ingesteld."""
    env = config.load_env()
    tekst = ("Proefbericht van TREE Deal Hunter. Staat dit er, dan komen de meldingen van 08:00 en "
             "18:30 voortaan binnen.")
    return {"status": alerts.bezorg(env, tekst, "Deal Hunter: proefbericht")}


DATUM = re.compile(r"^\d{4}-\d{2}-\d{2}$")


@app.post("/api/markeer")
def markeer(body: dict = Body(...)):
    """Boeiend, gebeld, bod uit of weg — met een notitie en een datum om aan herinnerd te worden.

    Notitie en datum worden alleen overschreven als ze zijn meegegeven, zodat een andere stand
    aanklikken niet wist wat je eerder opschreef."""
    lid, merk = body.get("id"), str(body.get("merk") or "geen")
    if not lid:
        raise HTTPException(400, "id ontbreekt")
    notitie = body.get("notitie")
    if notitie is not None:
        notitie = str(notitie)[:1000]
    stap = body.get("volgende_stap")
    if stap:
        stap = str(stap).strip()
        if not DATUM.match(stap):
            raise HTTPException(400, "de datum moet als JJJJ-MM-DD worden gegeven")
    else:
        stap = None
    store = Store()
    try:
        if not store.con.execute("SELECT 1 FROM listings WHERE id=?", (int(lid),)).fetchone():
            raise HTTPException(404, "object bestaat niet")
        store.markeer(int(lid), merk, notitie, stap)
        _cache_leeg()
        m = store.markeringen().get(int(lid)) or {}
        return {"ok": True, "id": int(lid), "merk": m.get("merk"),
                "notitie": m.get("notitie"), "volgende_stap": m.get("volgende_stap")}
    except ValueError as e:
        raise HTTPException(400, str(e)) from e
    finally:
        store.close()


@app.get("/api/listing/{lid}")
def listing(lid: int):
    store = Store()
    try:
        r = store.con.execute("SELECT * FROM listings WHERE id=?", (lid,)).fetchone()
        if not r:
            raise HTTPException(404)
        d = dict(r)
        base = listing_summary(store, r, events_since(store, 7))
        try:
            res = feasibility.compute(d)
        except Exception as e:  # noqa: BLE001
            res = {"available": False, "reason": f"rekenfout: {str(e)[:120]}", "scenarios": []}
        sig = jload(d["signals"], {})
        _, _, comps, kand = feasibility.inputs()
        k = next((c for c in kand if str(c.get("code")) == str(d["source_ref"])), None) if d["source"] == "idealista" else None
        comp_series = {}
        for s in res.get("scenarios", []):
            if s.get("available"):
                zk, sk = (s["comps"]["series"].split(":", 1) if ":" in s["comps"]["series"] else (s["comps"]["zone"], s["comps"]["series"]))
                c = comps.get(zk, {}).get(sk)
                if c:
                    comp_series[s["comps"]["series"]] = {"zone": ZONE_LABEL.get(zk, zk), "n": c.get("n"), "p25": c.get("p25"), "median": c.get("median"),
                                                          "p75": c.get("p75"), "verification": c.get("verification"),
                                                          "examples": [{kk: e.get(kk) for kk in ("code", "price", "m2", "eur_m2", "year", "label")} for e in (c.get("examples") or [])[:6]]}
        reviews = [dict(x) for x in store.con.execute("SELECT verdict, note, by, at FROM reviews WHERE listing_id=? ORDER BY id DESC LIMIT 10", (lid,))]
        events = [dict(x) for x in store.con.execute("SELECT kind, at, details FROM events WHERE listing_id=? ORDER BY id DESC LIMIT 20", (lid,))]
        # Het werkelijk betaalde peil van de kadastrale waardezone. Het bedrag alleen is misleidend,
        # dus de zin die zegt bij welke woning het hoort gaat mee (onderzoek N11 §9.3).
        zwr = store.con.execute("SELECT * FROM zonewaarde WHERE listing_id=?", (lid,)).fetchone()
        zw = {**dict(zwr), "omschrijving": zonewaarde.omschrijving(zwr), "bron": zonewaarde.BRON} \
            if zwr and zwr["val_tipo_m2"] else None
        return {
            **base, "feasibility": res, "comps": comp_series, "price_history": store.price_history(lid),
            "zonewaarde": zw,
            "desc": d["desc_excerpt"], "features": jload(d["features"], []), "beds": d["beds"], "baths": d["baths"],
            "signals_full": sig, "reviews": reviews, "events": events,
            "kandidaat_info": {"id": k["id"], "claims": k.get("claims", []), "blockers": k.get("blockers", []), "pin_note": k.get("pin_note")} if k else None,
        }
    finally:
        store.close()


@app.post("/api/listing/{lid}/wat-als")
def what_if(lid: int, body: dict = Body(...)):
    allowed = {"margin": (0.05, 0.5), "reno_rate": (300, 4000), "new_rate": (800, 6000), "fees_pct": (0.0, 0.3),
               "commission_pct": (0.0, 0.1), "sale_adj": (-0.5, 0.5), "price": (1, 20_000_000), "result_m2": (20, 5000),
               "kitchen_eur": (0, 150_000), "bathroom_eur": (0, 60_000),
               # Jan werkt met meerdere investeerders die elk een ander tarief rekenen (25-09-2026)
               "finance_rate": (0.0, 0.40)}
    ov = {}
    if body.get("sale_channel") in ("intern", "extern"):
        ov["sale_channel"] = body["sale_channel"]
    if body.get("slope") in ("vlak", "licht", "steil"):
        ov["slope"] = body["slope"]
    for key, (lo, hi) in allowed.items():
        if key in body and body[key] is not None:
            try:
                v = float(body[key])
            except (TypeError, ValueError):
                raise HTTPException(400, f"ongeldige waarde voor {key}")
            if not lo <= v <= hi:
                raise HTTPException(400, f"{key} buiten bereik {lo}–{hi}")
            ov[key] = v
    store = Store()
    try:
        r = store.con.execute("SELECT * FROM listings WHERE id=?", (lid,)).fetchone()
        if not r:
            raise HTTPException(404)
        return feasibility.compute(dict(r), ov, body.get("scenario_key"))
    finally:
        store.close()


@app.get("/api/auctions")
def auctions():
    store = Store()
    try:
        out = []
        for a in store.active_auctions():
            if a["source"] == "boe" and not (a["town"] or "").startswith("DENIA") and not a["area"]:
                continue
            rv = store.latest_review(auction_id=int(a["id"]))
            subs = jload(a["sub_ids"], [])
            out.append({"id": a["id"], "source": "AEAT" if a["source"] == "aeat" else "BOE", "sub": (subs or [a["boe_id"] or a["source_ref"]])[0],
                        "title": a["title"], "department": a["department"], "town": a["town"], "postcode": a["postcode"], "area": a["area"],
                        "valuation": a["valuation"], "end_date": a["end_date"], "lat": a["lat"] if config.valid_coord(a["lat"], a["lon"]) else None,
                        "lon": a["lon"] if config.valid_coord(a["lat"], a["lon"]) else None, "url": a["url"],
                        "blockers": jload(a["blockers"], []), "review": {"verdict": rv["verdict"], "note": rv["note"]} if rv else None})
        return out
    finally:
        store.close()


@app.get("/api/zones")
def zones():
    """Wijkprijzen met een zwaartepunt uit de geldige coördinaten van objecten in die wijk."""
    store = Store()
    try:
        pts: dict[str, list[tuple[float, float]]] = {}
        for r in store.con.execute("SELECT lat, lon, prefilter, area, source FROM listings WHERE gone_at IS NULL AND lat IS NOT NULL"):
            if not config.valid_coord(r["lat"], r["lon"]):
                continue
            z = jload(r["prefilter"], {}).get("zone") or (r["area"] if r["area"] in ("benitachell", "moraira") else None)
            if z:
                pts.setdefault(z, []).append((r["lat"], r["lon"]))
    finally:
        store.close()
    _, _, comps, _ = feasibility.inputs()
    out = []
    for z, series in comps.items():
        p = pts.get(z, [])
        if not p:
            continue
        lats = sorted(a for a, _ in p); lons = sorted(b for _, b in p)
        lat, lon = lats[len(lats) // 2], lons[len(lons) // 2]   # mediaan: robuust tegen uitschieters
        def s(key):
            c = series.get(key) or {}
            return {"n": c.get("n"), "p25": c.get("p25"), "median": c.get("median"), "p75": c.get("p75"), "verification": c.get("verification")} if c.get("n") else None
        out.append({"zone": z, "label": ZONE_LABEL.get(z, z), "lat": lat, "lon": lon, "points": len(p),
                    "villa_renovated": s("villa_renovated"), "villa_new": s("villa_new"), "apartment_renovated": s("apartment_renovated"),
                    "townhouse_renovated": s("townhouse_renovated")})
    return out


_cat_lock = threading.Lock()
_cat_cache: "OrderedDict[tuple, dict]" = OrderedDict()
_cat_next = [0.0]          # vroegste tijdstip voor het volgende verzoek aan Catastro
CAT_CACHE_MAX = 500
CAT_MAX_WAIT = 3.0


@app.get("/api/catastro")
def catastro(lat: float = Query(...), lon: float = Query(...)):
    """Kadastrale referentie op een punt (Catastro Consulta_RCCOOR_Distancia). Maximaal 1 verzoek per seconde, gecachet."""
    if not config.valid_coord(lat, lon):
        raise HTTPException(400, "punt buiten het werkgebied")
    key = (round(lat, 5), round(lon, 5))
    with _cat_lock:
        if key in _cat_cache:
            _cat_cache.move_to_end(key)
            return _cat_cache[key]
        now = time.time()
        slot = max(now, _cat_next[0])
        wait = slot - now
        if wait > CAT_MAX_WAIT:
            raise HTTPException(429, "te veel perceelopvragingen tegelijk; probeer het over enkele seconden opnieuw")
        _cat_next[0] = slot + 1.0
    if wait > 0:
        time.sleep(wait)
    url = "https://ovc.catastro.meh.es/ovcservweb/OVCSWLocalizacionRC/OVCCoordenadas.asmx/Consulta_RCCOOR_Distancia"
    try:
        r = httpx.get(url, params={"SRS": "EPSG:4326", "Coordenada_X": f"{lon:.6f}", "Coordenada_Y": f"{lat:.6f}"},
                      timeout=15, headers={"User-Agent": config.USER_AGENT})
        r.raise_for_status()
        root = ET.fromstring(r.content)
    except Exception as e:  # noqa: BLE001
        raise HTTPException(502, f"Catastro niet bereikbaar: {str(e)[:120]}")
    ns = {"c": "http://www.catastro.meh.es/"}
    parcels = []
    for pd in root.findall(".//c:pcd", ns) or root.findall(".//c:coord", ns):
        pc1 = pd.findtext(".//c:pc1", default="", namespaces=ns)
        pc2 = pd.findtext(".//c:pc2", default="", namespaces=ns)
        if not re.fullmatch(r"[0-9A-Z]{7}", pc1 or "") or not re.fullmatch(r"[0-9A-Z]{7}", pc2 or ""):
            continue
        parcels.append({"rc": pc1 + pc2, "address": pd.findtext(".//c:ldt", default="", namespaces=ns),
                        "distance_m": pd.findtext(".//c:dis", default=None, namespaces=ns),
                        "sede_url": f"https://www1.sedecatastro.gob.es/Cartografia/mapa.aspx?refcat={pc1}{pc2}"})
    err = root.findtext(".//c:des", default=None, namespaces=ns)
    out = {"lat": lat, "lon": lon, "parcels": parcels[:5], "error": err if not parcels else None,
           "source": "Sede Electrónica del Catastro, Consulta_RCCOOR_Distancia", "note": "Een punt is geen perceelidentificatie; bevestigen met nota simple."}
    with _cat_lock:
        _cat_cache[key] = out
        while len(_cat_cache) > CAT_CACHE_MAX:
            _cat_cache.popitem(last=False)
    return out


@app.post("/api/review")
def review(body: dict = Body(...)):
    verdict = body.get("verdict")
    if verdict not in ("interessant", "watchlist", "afwijzen"):
        raise HTTPException(400, "onbekend oordeel")

    def as_id(v):
        if v is None:
            return None
        if isinstance(v, bool) or not isinstance(v, (int, str)) or not re.fullmatch(r"[1-9][0-9]{0,9}", str(v)):
            raise HTTPException(400, "id moet een positief geheel getal zijn")
        return int(v)

    lid, aid = as_id(body.get("listing_id")), as_id(body.get("auction_id"))
    if (lid is None) == (aid is None):
        raise HTTPException(400, "geef precies één van listing_id of auction_id")
    note = re.sub(r"\s+", " ", str(body.get("note") or ""))[:300]
    store = Store()
    try:
        table = "listings" if lid else "auctions"
        if not store.con.execute(f"SELECT 1 FROM {table} WHERE id=?", (lid or aid,)).fetchone():
            raise HTTPException(404, "object niet gevonden")
        store.add_review(verdict, note, "Jan", listing_id=lid, auction_id=aid)
    finally:
        store.close()
    return {"ok": True}


@app.get("/api/reports")
def reports():
    files = sorted((p.name for p in config.REPORTS.glob("*.html") if p.name != "laatste.html"), reverse=True)
    return {"daily": files[:30], "haalbaarheid": (config.ROOT / "rapporten" / "haalbaarheid.html").exists()}


@app.get("/rapporten/haalbaarheid.html")
def rapport_haalbaarheid():
    p = config.ROOT / "rapporten" / "haalbaarheid.html"
    if not p.exists():
        raise HTTPException(404)
    return FileResponse(str(p), media_type="text/html")


@app.get("/rapporten/{name}")
def rapport(name: str):
    if "/" in name or ".." in name or not (name.endswith(".html") or name.endswith(".md")):
        raise HTTPException(404)
    p = config.REPORTS / name
    if not p.exists():
        raise HTTPException(404)
    return FileResponse(str(p), media_type="text/html" if name.endswith(".html") else "text/markdown")


@app.get("/rapporten/")
def rapporten_redirect():
    return RedirectResponse("/#rapporten")

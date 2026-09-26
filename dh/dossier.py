"""Alles wat in één dossier hoort, uit één functie.

Het dossier beantwoordt de tien vragen uit de masterprompt §1 voor één object: wat wordt er
aangeboden, waarom is het interessant, wat voegen wij toe, wat mag er, wat kost het, wat levert het
op, welke risico's, wat is de maximale prijs, hoe onderhandel je, en wat is de volgende stap.

Bronnen: de database (advertentie, prijsverloop, gebeurtenissen), het kadaster (tabel parcels),
de rekenmodule, het onderhandelplan, en de vastgelegde bouwregels per wijk als die er zijn.
Wat niet is vastgesteld heet hier ONBEKEND en wordt niet ingevuld met een gok.
"""
from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path

from . import config, feasibility, focus, negotiation, summary, zonewaarde
from .store import Store

BOUWREGELS = config.KADER / "bouwregels.json"
RISICOS = config.KADER / "risicos.json"


def _load(p: Path) -> dict:
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}


def zone_rules(area: str | None, zone: str | None) -> dict | None:
    """Bouwregels voor de wijk, als die zijn vastgelegd in kader/bouwregels.json."""
    d = _load(BOUWREGELS)
    if not d:
        return None
    for key in (f"{area}:{zone}", zone or "", area or ""):
        if key and key in (d.get("zones") or {}):
            return {**d["zones"][key], "sleutel": key, "bron": d.get("bron"), "datum": d.get("datum")}
    return None


def risk_layers(lid: int) -> dict | None:
    """Vastgelegde risicokaarten per object, als de kaartlagen zijn bevraagd."""
    d = _load(RISICOS)
    return (d.get("per_listing") or {}).get(str(lid))


def days_on(iso: str | None) -> int | None:
    if not iso:
        return None
    try:
        return (datetime.now(config.TZ).date() - datetime.fromisoformat(iso).date()).days
    except ValueError:
        return None


def build(store: Store, row, ev7: dict | None = None) -> dict:
    """Bouwt het volledige dossier voor één advertentie."""
    d = dict(row)
    lid = int(d["id"])
    item = summary.listing_summary(store, row, ev7 or {})
    try:
        res = feasibility.compute(d)
    except Exception as e:  # noqa: BLE001
        res = {"available": False, "reason": f"rekenfout: {str(e)[:150]}", "scenarios": []}
    best = next((s for s in res.get("scenarios", []) if s.get("key") == res.get("best_key")), None)
    sig = summary.jload(d["signals"], {})
    par = store.parcel(lid)
    parcel = dict(par) if par else None
    if parcel:
        for k in ("nearby", "warnings", "mismatches"):
            parcel[k] = summary.jload(parcel.get(k), [])
        parcel["geojson"] = summary.jload(parcel.get("geojson"), None)
    # Het gemiddelde werkelijk betaalde peil van de kadastrale waardezone. Tweede opinie naast de
    # wijkreeks, die op vraagprijzen rust. Het bedrag zonder de omschrijving erbij is misleidend,
    # dus die zin gaat mee (onderzoek N11 §9.3).
    zwr = store.con.execute("SELECT * FROM zonewaarde WHERE listing_id=?", (lid,)).fetchone()
    zw = None
    if zwr:
        z = dict(zwr)
        zw = {**z, "omschrijving": zonewaarde.omschrijving(z), "bron": zonewaarde.BRON} if z.get("val_tipo_m2") \
            else {"reden": z.get("reden"), "at": z.get("at")}
    hist = store.price_history(lid)
    events = [dict(x) for x in store.con.execute(
        "SELECT kind, at, details FROM events WHERE listing_id=? ORDER BY id DESC LIMIT 25", (lid,))]
    reviews = [dict(x) for x in store.con.execute(
        "SELECT verdict, note, by, at FROM reviews WHERE listing_id=? ORDER BY id DESC LIMIT 5", (lid,))]
    onderhandel = negotiation.plan(item, best, parcel, hist, sig)

    # vergelijkingsreeks achter de verkoopprijs
    comps = None
    if best and best.get("comps"):
        _, _, all_comps, _ = feasibility.inputs()
        zk = best["comps"]["zone"]
        sk = best["comps"]["series"].split(":", 1)[-1]
        c = (all_comps.get(zk) or {}).get(sk)
        if c:
            comps = {"zone": zk, "series": sk, "n": c.get("n"), "min": c.get("min"), "p25": c.get("p25"),
                     "median": c.get("median"), "p75": c.get("p75"), "verification": c.get("verification"),
                     "examples": (c.get("examples") or [])[:8], "source": c.get("source"), "date": c.get("date")}

    # wat er nog bewezen moet worden
    te_bewijzen = []
    if not parcel or not parcel.get("rc"):
        te_bewijzen.append(("Welk perceel dit is", "Nota simple bij het Registro de la Propiedad, het eigendomsregister."))
    else:
        te_bewijzen.append((f"Dat perceel {parcel['rc']} het te koop staande perceel is",
                            "Nota simple op naam van de verkoper; het kadaster zegt niets over eigendom."))
    if (sig.get("licence_claims") or []):
        te_bewijzen.append(("De vergunning waar de aanbieder naar verwijst",
                            "Kopie van de licencia de obra met nummer, datum en de termijn waarbinnen gebouwd moet zijn."))
    te_bewijzen.append(("Wat er op dit perceel mag",
                        "Informe urbanístico of cédula urbanística bij de gemeente, op de kadastrale referentie."))
    te_bewijzen.append(("Of er lasten op rusten",
                        "Nota simple: hypotheek, embargo, erfdienstbaarheid, vruchtgebruik."))
    if d.get("built_m2"):
        te_bewijzen.append(("Of het gebouwde legaal is",
                            "Vergelijking kadaster, eigendomsregister en gemeentelijk archief; bij twijfel certificado de antigüedad."))

    vervolg = [
        {"wie": "Jan", "wat": "Beslissen of dit dossier doorgaat", "wanneer": "vandaag"},
        {"wie": "Advocaat of gestor", "wat": "Nota simple opvragen en lezen", "wanneer": "binnen 3 werkdagen"},
        {"wie": "Architect", "wat": "Informe urbanístico aanvragen op de kadastrale referentie", "wanneer": "binnen 5 werkdagen"},
        {"wie": "Jan", "wat": "Bezichtigen en de verkoper naar de voorbehouden vragen", "wanneer": "binnen 1 week"},
        {"wie": "Systeem", "wat": "Prijs volgen en melden bij een daling", "wanneer": "doorlopend"},
    ]

    return {
        "id": lid, "ref": d["source_ref"], "source": d["source"], "item": item,
        "listing": {"type": d["type"], "price": d["price"], "built_m2": d["built_m2"], "plot_m2": d["plot_m2"],
                    "beds": d["beds"], "baths": d["baths"], "url": d["url"], "title": d["title"],
                    "desc": d["desc_excerpt"], "features": summary.jload(d["features"], []),
                    "town": d["town_raw"], "location": d["location_detail"], "lat": d["lat"], "lon": d["lon"],
                    "first_seen": d["first_seen_at"], "days_on": days_on(d["first_seen_at"]),
                    "eur_m2": round(d["price"] / d["built_m2"]) if d["price"] and d["built_m2"] else None,
                    "eur_m2_plot": round(d["price"] / d["plot_m2"]) if d["price"] and d["plot_m2"] else None},
        "feasibility": res, "best": best, "comps": comps,
        "parcel": parcel, "zone_rules": zone_rules(d["area"], item.get("zone")), "risks": risk_layers(lid),
        "zonewaarde": zw,
        "signals": sig, "price_history": hist, "events": events, "reviews": reviews,
        "negotiation": onderhandel,
        "te_bewijzen": [{"wat": a, "hoe": b} for a, b in te_bewijzen],
        "vervolgstappen": vervolg,
        "gegenereerd": datetime.now(config.TZ).isoformat(timespec="minutes"),
    }


# Signalen die van een object direct afblijven maken (harde uitsluiting van Jan)
HARDE_UITSLUITING = ("urbanisatie niet opgeleverd", "urbanización no recepcionada", "bankgarantie")


def rank(store: Store, limit: int = 8) -> list[dict]:
    """De objecten die een dossier verdienen.

    Volgorde: wat een project per maand oplevert, gecorrigeerd voor het aantal open risico's.
    Jan 17-09-2026: bij gelijk resultaat gaat een korter project voor, en een object dat te mooi
    lijkt verdient eerst wantrouwen. Elke blokkade die nog niet is weggenomen verlaagt daarom de
    kans dat het project werkelijk zo eindigt; vijf open punten halen de score ongeveer door twee.
    Objecten met de harde uitsluiting vallen helemaal af."""
    ev7 = summary.events_since(store, 7)
    items = focus.filter([summary.listing_summary(store, r, ev7) for r in focus.rijen(store)])
    ok = []
    for it in items:
        c = it.get("calc") or {}
        if not it.get("reliable") or not c or c.get("result", 0) <= 0:
            continue
        if it.get("class") in ("grijs", "geen"):
            continue
        if it.get("uitgesloten"):
            continue
        blok = it.get("blockers") or []
        tekst = " ".join(blok).lower()
        if any(h in tekst for h in HARDE_UITSLUITING):
            it["_uitgesloten"] = "harde uitsluiting: urbanisatie niet opgeleverd"
            continue
        maanden = max(c.get("months") or 24, 1)
        it["_per_maand"] = c["result"] / maanden
        # Een object uit de feed dat nog niemand heeft nagelopen heeft geen nul risico, alleen geen
        # bevindingen. Dat telt hier als twee open punten, zodat onderzochte objecten niet worden
        # gestraft voor het feit dat wij ernaar hebben gekeken.
        onderzocht = bool(it.get("kandidaat")) or it.get("source", "").startswith("idealista")
        it["_niet_onderzocht"] = not onderzocht
        it["_open_punten"] = len(blok) if onderzocht else max(len(blok), 2)
        it["_kans"] = round(1 / (1 + 0.15 * it["_open_punten"]), 3)
        it["_score"] = it["_per_maand"] * it["_kans"]
        ok.append(it)
    ok.sort(key=lambda x: -x["_score"])
    return ok[:limit]

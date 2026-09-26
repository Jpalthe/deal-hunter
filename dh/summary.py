"""Samenvatting van één advertentie: dezelfde cijfers voor het dashboard, de telefoonpagina,
de meldingen en de momentopname. Eén plek, zodat de bedragen overal gelijk zijn.
"""
from __future__ import annotations

import json
from datetime import datetime, timedelta

from . import (config, feasibility, focus as focusmod, goolzoom, negotiation, perceel,
               renovatie, verkoopbaarheid)
# Hier hernoemd zodat bestaande aanroepen en tests blijven werken.
perceel_is_het_object = perceel.perceel_is_het_object
tegenspraak = perceel.tegenspraak
from .store import Store

ZONE_LABEL = {
    "montgo_ermita": "Montgó – Ermita", "centro": "Centrum", "puerto_arenal": "Puerto – Arenal",
    "tosalet_adsubia": "Tosalet – Adsubia", "granadella_balcon": "Granadella – Balcón al Mar",
    "rafalet_pinosol": "Rafalet – Pinosol", "benitachell": "Benitachell", "moraira": "Moraira",
}
AREA_LABEL = {"javea": "Jávea", "benitachell": "Benitachell", "moraira": "Moraira"}
CLASS_LABEL = {"groen": "Haalt marge, ook voorzichtig", "blauw": "Haalt marge in basis",
               "oranje": "Onderhandelbaar tot 30 %", "grijs": "Onder de marge",
               "onzeker": "Niet betrouwbaar te rekenen", "geen": "Geen indicatie"}


def jload(v, default):
    try:
        return json.loads(v) if v else default
    except (TypeError, json.JSONDecodeError):
        return default


def events_since(store: Store, days: int) -> dict[int, list[str]]:
    since = (datetime.now(config.TZ) - timedelta(days=days)).isoformat(timespec="seconds")
    out: dict[int, list[str]] = {}
    for r in store.con.execute(
            "SELECT listing_id, kind FROM events WHERE listing_id IS NOT NULL AND at >= ? "
            "AND kind NOT IN ('NULMETING','GEÏMPORTEERD')", (since,)):
        out.setdefault(int(r["listing_id"]), []).append(r["kind"])
    return out


def bouw_ctx(store: Store) -> dict:
    """Eén keer ophalen wat anders per object een query zou kosten.

    Bij 512 objecten scheelt dat ruim duizend losse bevragingen per keer dat de lijst wordt
    opgebouwd, en de telefoon wacht daarop."""
    urb: dict[int, dict] = {}
    try:
        goolzoom.zorg_tabel(store)
        for r in store.con.execute("SELECT * FROM urbanism"):
            d = dict(r)
            if d.get("classificatie"):
                d["duiding"] = goolzoom.duiding(d["classificatie"])
                d["bron"] = d.get("databron_url") or goolzoom.BRON_URL
                urb[int(d["listing_id"])] = d
    except Exception:  # noqa: BLE001 — zonder bestemming werkt de rest gewoon door
        urb = {}
    par: dict[int, dict] = {}
    try:
        for r in store.con.execute("SELECT listing_id, year, rc, built_m2, plot_m2, distance_m, use_text FROM parcels"):
            par[int(r["listing_id"])] = dict(r)
    except Exception:  # noqa: BLE001
        par = {}
    try:
        _, _, comps, _ = feasibility.inputs()
    except Exception:  # noqa: BLE001
        comps = {}
    try:
        merken = store.markeringen()
    except Exception:  # noqa: BLE001
        merken = {}
    return {"urb": urb, "parcels": par, "comps": comps, "merken": merken}


APPARTEMENT = ("flat", "apartment", "appartement", "studio", "penthouse", "duplex", "atico", "ático")


def fiscale_waarschuwing(price, ref_waarde, eenheden, itp_pct: float = 0.10) -> dict | None:
    """De valor de referencia is de ondergrens voor de overdrachtsbelasting.

    Jan 25-09-2026: niet meerekenen in de som, wel tonen. Ligt de fiscale waarde boven de
    vraagprijs, dan betaal je belasting over het hogere bedrag; dat verschil staat hier.

    Alleen tonen als vaststaat dat het kadastrale perceel het object is; zie
    `perceel_is_het_object`. Anders vergelijk je twee verschillende dingen."""
    if not price or not ref_waarde or ref_waarde <= price:
        return None
    if eenheden and eenheden > 1:
        return None            # meerdere eenheden op het perceel: de som zegt niets over deze koop
    verschil = round(ref_waarde - price)
    return {"ref_waarde": round(ref_waarde), "verschil": verschil,
            "extra_belasting": round(verschil * itp_pct),
            "eenheden": eenheden,
            "onzeker": bool(eenheden and eenheden > 1),
            "tekst": (f"De fiscale waarde ligt € {verschil:,} boven de vraagprijs. "
                      f"Over dat verschil betaal je alsnog overdrachtsbelasting: "
                      f"ongeveer € {round(verschil * itp_pct):,} extra.").replace(",", ".")}


def listing_summary(store: Store, row, ev7: dict, ctx: dict | None = None) -> dict:
    ctx = ctx if ctx is not None else bouw_ctx(store)
    d = dict(row)
    try:
        res = feasibility.compute(d)
    except Exception as e:  # noqa: BLE001 — één kapot object mag het overzicht niet platleggen
        res = {"available": False, "reason": f"rekenfout: {str(e)[:120]}", "scenarios": []}
    best = next((s for s in res.get("scenarios", []) if s.get("key") == res.get("best_key")), None)
    cls = feasibility.classify(d["price"], best)
    pf = jload(d["prefilter"], {})
    sig = jload(d["signals"], {})
    rv = store.latest_review(listing_id=int(d["id"]))
    hist = store.price_history(int(d["id"]))
    drop = None
    if len(hist) >= 2 and hist[0][1] and hist[-1][1] and hist[-1][1] < hist[0][1]:
        drop = round((hist[-1][1] - hist[0][1]) / hist[0][1], 4)
    al = store.last_alert(int(d["id"]))
    out = {
        "id": d["id"], "source": d["source"], "ref": d["source_ref"], "kandidaat": sig.get("kandidaat_id"),
        "area": d["area"], "area_label": AREA_LABEL.get(d["area"], d["area"]), "zone": res.get("zone") or pf.get("zone"),
        "zone_label": ZONE_LABEL.get(res.get("zone") or pf.get("zone"), ""), "location": d["location_detail"],
        "type": d["type"], "category": pf.get("category") or d["category"], "price": d["price"],
        "built_m2": d["built_m2"], "plot_m2": d["plot_m2"], "lat": d["lat"], "lon": d["lon"], "url": d["url"],
        "image_url": (d["image_url"] if "image_url" in d.keys() else None),
        "first_seen": d["first_seen_at"], "source_date": d["source_date"],
        "class": cls, "class_label": CLASS_LABEL[cls],
        "scenario": best["label"] if best else None,
        "max_price": best["max_price"] if best else None,
        "margin_at_asking": best["margin_at_asking"] if best else None,
        "room": round(best["max_price"]["base"] / d["price"] - 1, 4) if (best and d["price"]) else None,
        "calc": (best or {}).get("sum"), "result_m2": (best or {}).get("result_m2"),
        "reliable": best["reliable"] if best else None,
        "warnings": (best["warnings"] + best.get("notes", [])) if best else [],
        "reason": None if best else res.get("reason"),
        "signals": (sig.get("renovation_signals") or [])[:3] + (sig.get("licence_claims") or [])[:2],
        "blockers": sig.get("blockers", [])[:4],
        "uitgesloten": sig.get("uitgesloten"),
        # makelaarssites: van welk kantoor, en of het object ook op een portaal staat
        "kantoor": sig.get("kantoor"),
        "alleen_bij_makelaar": bool(sig.get("alleen_bij_makelaar")),
        "portaal": (sig.get("portaal") or {}).get("source") if sig.get("portaal") else None,
        "events_7d": sorted(set(ev7.get(int(d["id"]), []))), "price_drop": drop,
        "alert": {"tier": al["tier"], "at": al["at"]} if al else None,
        "review": {"verdict": rv["verdict"], "note": rv["note"], "at": rv["at"]} if rv else None,
    }
    # Korte haalbaarheid per object: wat je zou bieden en waar je stopt. Zelfde rekenregels als het
    # dossier, zodat de app en het dossier hetzelfde zeggen.
    try:
        p = negotiation.plan(out, best, None, hist, sig)
    except Exception:  # noqa: BLE001 — een kapot object mag de lijst niet platleggen
        p = {}
    lid = int(d["id"])
    # Officiële bestemming (Goolzoom → IDEV). Niet opgevraagd blijft ONBEKEND, geen afwijzing.
    u = (ctx.get("urb") or {}).get(lid)
    out["urbanisme"] = {
        "classificatie": u.get("classificatie"), "zonering": u.get("zonering"),
        "omschrijving": u.get("omschrijving"), "plan": u.get("plan"),
        "duiding": u.get("duiding"), "bron": u.get("bron"), "opgevraagd": u.get("fetched_at"),
    } if u else None
    out["bestemming"] = (u or {}).get("duiding", {}).get("soort") if u else None
    out["bestemming_wonen"] = ((u or {}).get("duiding") or {}).get("wonen", "onbekend") if u else "onbekend"
    # Renovatievermoeden uit de vier kenmerken van Jan
    par = (ctx.get("parcels") or {}).get(lid)
    tekst = " ".join(x for x in (d.get("title"), d.get("desc_excerpt")) if x)
    summary_features = jload(d["features"], [])
    out["renovatie"] = renovatie.beoordeel(out, par, sig, ctx.get("comps"), tekst=tekst)
    # Gewone woning die tóch een opknapper is: oud én meer dan 40 % onder de wijkprijs (Jan 26-09).
    ok = (focusmod.instelling().get("opknapper_vermoeden") or {})
    # Waar de eindkoper op let. Indicator, nooit een uitsluiting (Jan 26-09-2026).
    out["koper"] = verkoopbaarheid.beoordeel(out, tekst, summary_features)
    if sig.get("zonder_lift_hoog") and not out.get("uitgesloten"):
        out["uitgesloten"] = f"harde uitsluiting: {sig['zonder_lift_hoog']}"
    # Doorstroomzone van de rivier of openbaar zeegebied: daar wordt niet gebouwd (Jan 26-09-2026).
    if sig.get("water_uitsluiting") and not out.get("uitgesloten"):
        out["uitgesloten"] = f"harde uitsluiting: {sig['water_uitsluiting']}"
    out["water"] = {"waarschuwing": sig.get("water_waarschuwing"),
                    "uitsluiting": sig.get("water_uitsluiting")} if (
                        sig.get("water_waarschuwing") or sig.get("water_uitsluiting")) else None
    out["opknapper"] = renovatie.opknapper_vermoeden(
        {**out, "titel_en_tekst": tekst}, par, ctx.get("comps"),
        int(ok.get("bouwjaar_voor", 1995)), float(ok.get("korting_op_wijkprijs_min", 0.40))
    ) if ok.get("aan") else None
    # Overdrachtsbelasting: waarschuwen als de fiscale waarde boven de vraagprijs ligt
    out["perceel_zeker"] = perceel_is_het_object(out, par)
    out["tegenspraak"] = tegenspraak(out, par)
    out["fiscaal"] = fiscale_waarschuwing(d["price"], (u or {}).get("ref_waarde"),
                                          (u or {}).get("ref_eenheden")) if (u and out["perceel_zeker"]) else None
    out["appartement"] = any(a in (d["type"] or "").lower() for a in APPARTEMENT) or \
        (out.get("category") or "").startswith("appartement")
    # Volgorde in de app: winst per maand, gedempt door het aantal open punten. Dezelfde maat als
    # de ranglijst van de dossiers, zodat app en dossier dezelfde koploper aanwijzen.
    c = out.get("calc") or {}
    if c.get("result") and out.get("reliable") and not out.get("uitgesloten"):
        maanden = max(c.get("months") or 24, 1)
        onderzocht = bool(out.get("kandidaat")) or str(out.get("source", "")).startswith("idealista")
        open_punten = len(out.get("blockers") or []) if onderzocht else max(len(out.get("blockers") or []), 2)
        out["per_maand"] = round(c["result"] / maanden * (1 / (1 + 0.15 * open_punten)))
    else:
        out["per_maand"] = None
    mk = (ctx.get("merken") or {}).get(lid) or {}
    out["merk"] = mk.get("merk")
    out["notitie"] = mk.get("notitie")
    out["volgende_stap"] = mk.get("volgende_stap")
    # Het bod moet vóór het tabblad staan: focus.tab kijkt of er nog een serieus bod
    # mogelijk is, en zonder bod zou dat oordeel stilzwijgend overgeslagen worden.
    out["bod"] = {"oordeel": p.get("verdict"), "opening": p.get("opening"), "streef": p.get("target"),
                  "walk": p.get("walk_away"), "plafond": p.get("ceiling"),
                  "voorzichtig": (best or {}).get("max_price", {}).get("conservative"),
                  "opening_pct": p.get("opening_pct_of_asking"), "risicos": (p.get("risks") or [])[:3],
                  "kloof": bool(p.get("kloof_te_groot")), "kloof_tekst": p.get("kloof_tekst"),
                  "kloof_pct": p.get("kloof_pct"), "serieus_mogelijk": p.get("serieus_mogelijk", True),
                  "serieus_tekst": p.get("serieus_tekst"), "dagen_te_koop": p.get("dagen_te_koop"),
                  "max_korting": p.get("max_korting")} if p.get("walk_away") else None
    out["tab"] = focusmod.tab(out, out["urbanisme"])
    out["in_focus"] = out["tab"] == focusmod.KANSEN
    return out


def all_active(store: Store) -> list[dict]:
    ev7 = events_since(store, 7)
    ctx = bouw_ctx(store)
    return [listing_summary(store, r, ev7, ctx) for r in store.active_listings(area_only=True)]

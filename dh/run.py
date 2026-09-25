"""Eén ronde van de Deal Hunter-monitor.

  python -m dh.run --slot 10:00 [--dry-run] [--no-deliver] [--no-ai]

Stappen: BP-feed lezen → nieuw/prijs/verdwenen (met lege-feedbescherming) → signalen en voorfilter
→ optionele AI-classificatie binnen budget → BOE en AEAT → rapport (HTML + MD) → bezorging → log.
Idempotent per ronde; een vergrendelbestand voorkomt overlappende runs.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import logging
import os
import shutil
import sys
import time
import traceback
from datetime import datetime
from pathlib import Path

from . import alerts, config, deliver, prefilter, report, signals, summary
from .adapters import aeat, boe, borme, bp
from .store import Store

LOCK = config.DATA / "run.lock"


def setup_logging() -> None:
    config.LOGS.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s: %(message)s",
                        handlers=[logging.FileHandler(config.LOGS / "dh.log", encoding="utf-8"), logging.StreamHandler(sys.stdout)])


def step_bp(store: Store, run_id: int, pf: prefilter.Prefilter, env: dict, use_ai: bool, meta: dict) -> dict:
    log = logging.getLogger("dh.bp")
    try:
        items, m = bp.fetch()
    except Exception as e:  # noqa: BLE001
        store.source_status("bp", False, error=str(e)[:300])
        store.add_event(run_id, "BRON NIET BEREIKBAAR", details={"bron": "bp", "fout": str(e)[:300]})
        log.warning("BP niet bereikbaar: %s", e)
        return {"note": f"niet bereikbaar: {str(e)[:120]}"}
    prev = store.source("bp")
    prev_count = prev["last_count"] if prev and prev["last_count"] else None
    shrink_pct = None
    if prev_count:
        shrink_pct = (prev_count - len(items)) / prev_count * 100
    guard = shrink_pct is not None and shrink_pct > config.BP_SHRINK_ABORT_PCT
    seen: set[str] = set()
    kinds: dict[str, int] = {}
    ai_budget = float(pf.kader.get("ai_budget_eur_maand", 100))
    from . import classify
    for p in items:
        rec = bp.normalise(p)
        seen.add(rec["source_ref"])
        lid, kind, _ = store.upsert_listing(run_id, "bp", rec)
        kinds[kind] = kinds.get(kind, 0) + 1
        sig = signals.analyse(rec["_text"], rec["_features"], rec["type"], bool(rec["new_build"]))
        pfr = pf.run(rec, sig)
        ai = None
        if use_ai and kind in ("NIEUW", "PRIJS GEWIJZIGD", "GEWIJZIGD", "OPNIEUW AANGEBODEN", "NULMETING") and rec["area"] and pfr["verdict"] != "buiten kader":
            ai = classify.classify(rec, env, store, run_id, ai_budget)
        store.set_analysis(lid, signals=sig, category=pfr["category"], prefilter=pfr, ai=ai)
    if guard:
        store.add_event(run_id, "BRON NIET BEREIKBAAR", details={"bron": "bp", "reden": f"krimp {shrink_pct:.0f} % boven drempel; geen 'verdwenen'-meldingen"})
        store.source_status("bp", False, count=len(items), error=f"krimp {shrink_pct:.0f} %")
        m["note"] = f"krimp {shrink_pct:.0f} % boven de drempel van {config.BP_SHRINK_ABORT_PCT} %: verdwijningen niet gemeld"
    else:
        gone = store.mark_gone(run_id, "bp", seen)
        kinds["NIET MEER GEVONDEN"] = len(gone)
        store.source_status("bp", True, count=len(items))
        m["note"] = f"lastFetch {m.get('lastFetch')}; {m.get('warning', '')}".strip("; ")
    m["kinds"] = kinds
    log.info("BP: %s objecten, gebeurtenissen %s", len(items), kinds)
    return m


def step_boe(store: Store, run_id: int, dry: bool) -> dict:
    log = logging.getLogger("dh.boe")
    try:
        recs, m = boe.collect(boe.days_to_check(), max_detail=0 if dry else 25)
    except Exception as e:  # noqa: BLE001
        store.source_status("boe", False, error=str(e)[:300])
        store.add_event(run_id, "BRON NIET BEREIKBAAR", details={"bron": "boe", "fout": str(e)[:300]})
        return {"note": f"niet bereikbaar: {str(e)[:120]}"}
    n = 0
    for r in recs:
        a = boe.to_auction(r)
        if a:
            store.upsert_auction(run_id, "boe", a)
            n += 1
    store.source_status("boe", True, count=n)
    m["fetched"] = n
    m["note"] = "; ".join(f"{d}: {s}" for d, s in m["days"].items())
    log.info("BOE: %s kandidaat-items, %s detailverzoeken", n, m["detail_requests"])
    return m


def step_aeat(store: Store, run_id: int) -> dict:
    log = logging.getLogger("dh.aeat")
    try:
        arr, version = aeat.fetch()
    except Exception as e:  # noqa: BLE001
        store.source_status("aeat", False, error=str(e)[:300])
        store.add_event(run_id, "BRON NIET BEREIKBAAR", details={"bron": "aeat", "fout": str(e)[:300]})
        return {"note": f"niet bereikbaar: {str(e)[:120]}"}
    sel = aeat.select(arr)
    seen = set()
    for a in sel:
        seen.add(a["source_ref"])
        store.upsert_auction(run_id, "aeat", a)
    store.mark_auctions_gone(run_id, "aeat", seen)
    store.source_status("aeat", True, count=len(sel))
    in_area = sum(1 for a in sel if a["area"])
    log.info("AEAT: %s records landelijk, %s in Alicante, %s in werkgebied (versie %s)", len(arr), len(sel), in_area, version)
    return {"fetched": len(sel), "note": f"lijstversie {version}; {in_area} in werkgebied; {len(arr)} landelijk"}


def step_borme(store: Store, run_id: int) -> dict:
    """Handelsregister: vennootschappen in ontbinding, liquidatie of faillissement in Alicante."""
    log = logging.getLogger("dh.borme")
    try:
        recs, m = borme.collect(borme.days_to_check())
    except Exception as e:  # noqa: BLE001
        store.source_status("borme", False, error=str(e)[:300])
        store.add_event(run_id, "BRON NIET BEREIKBAAR", details={"bron": "borme", "fout": str(e)[:300]})
        return {"note": f"niet bereikbaar: {str(e)[:120]}"}
    new = 0
    for r in recs:
        _, kind = store.upsert_company(run_id, "borme", r)
        if kind == "NIEUW":
            new += 1
    store.source_status("borme", True, count=len(recs))
    vastgoed = sum(1 for r in recs if r.get("sector"))
    m["fetched"] = len(recs)
    m["new"] = new
    m["note"] = f"{len(recs)} signalen, {new} nieuw, {vastgoed} in vastgoed of bouw; " + "; ".join(f"{d}: {s}" for d, s in m["days"].items())
    log.info("BORME: %s signalen (%s nieuw, %s vastgoed)", len(recs), new, vastgoed)
    return m


def step_makelaars(store: Store, run_id: int, max_per_site: int | None = None) -> dict:
    """Eigen websites van makelaars: alleen de kantoren waarvoor lezen is toegestaan (kader/makelaars.json)."""
    log = logging.getLogger("dh.makelaars")
    from . import import_makelaars
    from .adapters import makelaars
    try:
        per_site, verslag = makelaars.lees_alles(max_per_site=max_per_site)
    except Exception as e:  # noqa: BLE001
        store.add_event(run_id, "BRON NIET BEREIKBAAR", details={"bron": "makelaars", "fout": str(e)[:300]})
        return {"note": f"niet bereikbaar: {str(e)[:120]}"}
    kandidaten = import_makelaars.portaal_kandidaten(store)
    pf = prefilter.Prefilter()
    tot = {"kantoren": len(per_site), "objecten": 0, "in_werkgebied": 0, "nieuw": 0, "alleen_bij_makelaar": 0}
    for host, recs in per_site.items():
        bron = f"makelaar:{host}"
        gezien: set[str] = set()
        for rec in recs:
            tot["objecten"] += 1
            if not rec.get("area"):
                continue
            tot["in_werkgebied"] += 1
            kantoor = rec.pop("_kantoor", host)
            rec.pop("_verhuur", None)
            gezien.add(rec["source_ref"])
            lid, kind, _ = store.upsert_listing(run_id, bron, rec)
            if kind in ("NIEUW", "NULMETING"):
                tot["nieuw"] += 1
            sig = signals.analyse(rec["_text"], rec["_features"], rec["type"], bool(rec["new_build"]))
            match = import_makelaars.zoek_op_portaal(rec, kandidaten)
            sig["kantoor"], sig["portaal"] = kantoor, match
            if not match:
                sig["alleen_bij_makelaar"] = True
                tot["alleen_bij_makelaar"] += 1
            pfr = pf.run(rec, sig)
            store.set_analysis(lid, signals=sig, category=pfr["category"], prefilter=pfr)
        store.mark_gone(run_id, bron, gezien)
        store.source_status(bron, True, count=len(gezien))
    for host, v in (verslag.get("kantoren") or {}).items():
        if v.get("fout"):
            store.source_status(f"makelaar:{host}", False, error=v["fout"])
    tot["note"] = (f"{tot['kantoren']} kantoren, {tot['in_werkgebied']} objecten in werkgebied, "
                   f"{tot['alleen_bij_makelaar']} alleen bij de makelaar; overgeslagen: "
                   f"{', '.join(o['kantoor'] for o in verslag.get('overgeslagen', [])) or 'geen'}")
    log.info("makelaars: %s", tot["note"])
    return tot


def refresh_mobile() -> str:
    """Maakt de momentopname voor onderweg opnieuw (rapporten/mobiel.html). Publiceren blijft handwerk."""
    log = logging.getLogger("dh.mobiel")
    try:
        spec = importlib.util.spec_from_file_location("rapport_mobiel", config.ROOT / "tools" / "rapport_mobiel.py")
        mod = importlib.util.module_from_spec(spec)
        sys.modules["rapport_mobiel"] = mod
        spec.loader.exec_module(mod)  # type: ignore[union-attr] — schrijft het bestand bij het uitvoeren
        return f"vernieuwd: {getattr(mod, 'OUT', 'rapporten/mobiel.html')}"
    except Exception as e:  # noqa: BLE001 — een mislukte momentopname mag de ronde niet laten vallen
        log.warning("momentopname mislukt: %s", e)
        return f"mislukt: {str(e)[:150]}"


def step_verrijken(budget_s: int = 12 * 60) -> dict:
    """Vult van nieuwe objecten het perceel, de bestemming en de helling aan.

    Zonder deze stap krijgen objecten die vanochtend binnenkwamen geen kadastrale referentie, geen
    officiële bestemming en geen gemeten helling — en dan mist hun rekensom het grondwerk en staat de
    bestemming op ONBEKEND. Alle drie de bronnen zijn gratis; Goolzoom kost wel geld per bevraging,
    vandaar het budget. Wat deze ronde niet lukt, komt de volgende aan de beurt."""
    log = logging.getLogger("dh.verrijken")
    uit: dict = {}
    begin = time.time()
    # Per ronde hoogstens zoveel objecten per bron. Catastro en het hoogtemodel zijn gratis; Goolzoom
    # kost geld per bevraging, dus die krijgt de kleinste portie. Wat blijft liggen komt de volgende
    # ronde aan de beurt, en er zijn twee rondes per dag.
    stappen = (("percelen", "dh.enrich_parcels", 400),
               ("bestemming", "dh.enrich_urbanisme", 250),
               ("helling", "dh.enrich_helling", 400))
    for naam, mod, limiet in stappen:
        if time.time() - begin > budget_s:
            uit[naam] = "overgeslagen: tijdbudget op"
            continue
        try:
            m = importlib.import_module(mod)
            uit[naam] = m.run(limit=limiet)
        except Exception as e:  # noqa: BLE001 — een bron die hapert mag de ronde niet laten vallen
            log.warning("%s mislukt: %s", naam, str(e)[:150])
            uit[naam] = f"mislukt: {str(e)[:120]}"
    try:
        from . import enrich_helling
        uit["helling_gekoppeld"] = enrich_helling.koppel()
    except Exception as e:  # noqa: BLE001
        uit["helling_gekoppeld"] = f"mislukt: {str(e)[:120]}"
    # Herberekenen met de nieuwe bestemming en helling erin; `reanalyse` heeft alleen een main().
    try:
        from . import reanalyse
        uit["herberekend"] = "ok" if reanalyse.main() == 0 else "afgesloten met een fout"
    except Exception as e:  # noqa: BLE001
        uit["herberekend"] = f"mislukt: {str(e)[:120]}"
    return uit


def warm_cache() -> str:
    """Stookt de webdienst warm na een ronde.

    De samenvatting kost zo'n vijf seconden rekenwerk. Doet de ronde dat zelf, dan is het scherm op
    Jans telefoon om 08:00 meteen gevuld in plaats van na tien seconden. Draait de dienst niet, dan
    is dat geen probleem: de app rekent het bij de eerste blik alsnog uit."""
    log = logging.getLogger("dh.warm")
    try:
        import httpx
        with httpx.Client(timeout=120) as c:
            for pad in ("/api/summary", "/api/listings?tab=kansen,later,buiten"):
                c.get("http://127.0.0.1:8710" + pad)
        return "webdienst warmgestookt"
    except Exception as e:  # noqa: BLE001 — een koude cache mag de ronde niet laten vallen
        log.info("warmstoken overgeslagen: %s", str(e)[:100])
        return f"overgeslagen: {str(e)[:100]}"


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--slot", default="auto")
    ap.add_argument("--dry-run", action="store_true", help="geen detailverzoeken bij BOE, geen bezorging")
    ap.add_argument("--no-deliver", action="store_true")
    ap.add_argument("--no-ai", action="store_true")
    a = ap.parse_args(argv)
    setup_logging()
    log = logging.getLogger("dh.run")
    slot = a.slot if a.slot != "auto" else datetime.now(config.TZ).strftime("%H:%M")
    config.DATA.mkdir(parents=True, exist_ok=True)
    if LOCK.exists():
        age = datetime.now().timestamp() - LOCK.stat().st_mtime
        if age < 3 * 3600:
            log.error("vergrendeld: een andere ronde loopt (lock %.0f s oud)", age)
            return 2
        LOCK.unlink()
    LOCK.write_text(str(os.getpid()))
    env = config.load_env()
    store = Store()
    run_id = store.start_run(slot)
    baseline = store.is_baseline(run_id)
    status, meta = "ok", {}
    try:
        pf = prefilter.Prefilter()
        meta["bp"] = step_bp(store, run_id, pf, env, use_ai=not a.no_ai, meta=meta)
        meta["boe"] = step_boe(store, run_id, dry=a.dry_run)
        meta["aeat"] = step_aeat(store, run_id)
        meta["borme"] = step_borme(store, run_id)
        meta["makelaars"] = step_makelaars(store, run_id)
        # Nieuwe objecten meteen verrijken: perceel, bestemming en helling. Moet vóór het rapport,
        # anders rekent deze ronde nog zonder grondwerk en zonder bestemming.
        store.con.commit()
        meta["verrijken"] = step_verrijken()
        ctx = report.context(store, run_id, slot, meta, baseline, {}, {})
        html, md = report.build(ctx)
        config.REPORTS.mkdir(parents=True, exist_ok=True)
        stamp = datetime.now(config.TZ).strftime("%Y-%m-%d-%H%M")
        out_html = config.REPORTS / f"{stamp}.html"
        out_md = config.REPORTS / f"{stamp}.md"
        out_html.write_text(html, encoding="utf-8")
        out_md.write_text(md, encoding="utf-8")
        shutil.copyfile(out_html, config.REPORTS / "laatste.html")
        shutil.copyfile(out_md, config.REPORTS / "laatste.md")
        meta["report"] = str(out_html)
        if a.dry_run or a.no_deliver:
            meta["delivery"] = ["overgeslagen (dry-run/no-deliver)"]
        else:
            url = env.get("DH_REPORT_BASE_URL")
            link = f"{url.rstrip('/')}/{out_html.name}" if url else None
            meta["delivery"] = [deliver.discord(env, md, link),
                                deliver.email(env, f"Deal Hunter {slot} {ctx['day']}: {ctx['headline']}", html)]
        log.info("rapport: %s; bezorging: %s", out_html, meta["delivery"])
        items = summary.all_active(store)
        meta["meldingen"] = alerts.run(store, run_id, items, env,
                                       report_url=(env.get("DH_REPORT_BASE_URL") or "").rstrip("/") + "/" + out_html.name if env.get("DH_REPORT_BASE_URL") else None,
                                       deliver=not (a.dry_run or a.no_deliver))
        meta["mobiel"] = refresh_mobile()
        meta["cache"] = warm_cache()
    except Exception:  # noqa: BLE001
        status = "fout"
        meta["traceback"] = traceback.format_exc()[-2000:]
        log.exception("ronde mislukt")
    finally:
        store.finish_run(run_id, status, meta)
        store.close()
        LOCK.unlink(missing_ok=True)
    print(json.dumps({k: v for k, v in meta.items() if k != "traceback"}, ensure_ascii=False, indent=1, default=str))
    return 0 if status == "ok" else 1


if __name__ == "__main__":
    sys.exit(main())

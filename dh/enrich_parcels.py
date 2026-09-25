"""Haalt voor elk object met coördinaten het perceel op bij het kadaster en legt het vast.

  python -m dh.enrich_parcels [--limit 200] [--only 90705084,4104JAV] [--force]

Eén verzoek per seconde per dienst, drie diensten per object, dus reken op ongeveer drie seconden
per object. De uitkomst gaat in de tabel `parcels` en wordt daarna niet opnieuw opgehaald, tenzij
je --force meegeeft.

Wat er wordt vastgelegd: kadastrale referentie, afstand van de pin tot het perceel, adres, gebruik,
bebouwd oppervlak volgens het kadaster, bouwjaar, officiële perceeloppervlakte en de perceelgrens.
Geen eigenaren: die geeft de dienst niet en die vragen wij niet op.
"""
from __future__ import annotations

import argparse
import json
import sys
import time

from . import catastro, config
from .store import Store


def flag_shared_pins(store: Store) -> int:
    """Markeert percelen waarvan de pin door meerdere advertenties wordt gedeeld.

    De feed van Background Properties publiceert geen adressen; de coördinaat is dan het middelpunt
    van een wijk. Het perceel dat het kadaster op dat punt teruggeeft is dan willekeurig, en een
    verschil tussen advertentie en kadaster zegt niets over het object. Dat moet zichtbaar zijn,
    anders presenteren wij ruis als bevinding."""
    rows = store.con.execute(
        "SELECT ROUND(lat,5) la, ROUND(lon,5) lo, COUNT(*) n, GROUP_CONCAT(source_ref) refs "
        "FROM listings WHERE gone_at IS NULL AND lat IS NOT NULL GROUP BY la, lo HAVING n > 1").fetchall()
    gedeeld = {(r["la"], r["lo"]): (r["n"], r["refs"]) for r in rows}
    n = 0
    for p in store.con.execute("SELECT p.listing_id, l.lat, l.lon, p.warnings FROM parcels p "
                               "JOIN listings l ON l.id = p.listing_id WHERE l.lat IS NOT NULL").fetchall():
        key = (round(p["lat"], 5), round(p["lon"], 5))
        if key not in gedeeld:
            continue
        aantal = gedeeld[key][0]
        w = json.loads(p["warnings"] or "[]")
        melding = (f"De pin wordt gedeeld door {aantal} advertenties en is dus geen adres maar een middelpunt van een wijk. "
                   "Welk perceel hier werkelijk bij hoort is niet vastgesteld; het verschil met het kadaster zegt nog niets.")
        if melding not in w:
            w.insert(0, melding)
            store.con.execute("UPDATE parcels SET warnings=?, mismatches='[]' WHERE listing_id=?",
                              (json.dumps(w, ensure_ascii=False), p["listing_id"]))
            n += 1
    store.con.commit()
    return n


def run(limit: int = 200, only: list[str] | None = None, force: bool = False, quiet: bool = False) -> dict:
    store = Store()
    try:
        if only:
            q = ",".join("?" * len(only))
            rows = store.con.execute(
                f"SELECT * FROM listings WHERE source_ref IN ({q}) AND lat IS NOT NULL", only).fetchall()
        elif force:
            rows = store.con.execute(
                "SELECT * FROM listings WHERE gone_at IS NULL AND area IS NOT NULL AND lat IS NOT NULL LIMIT ?",
                (limit,)).fetchall()
        else:
            rows = store.parcels_missing(limit)
        stats = {"bekeken": 0, "gevonden": 0, "mislukt": 0, "afwijkingen": 0, "ver_van_de_pin": 0}
        for r in rows:
            stats["bekeken"] += 1
            try:
                e = catastro.enrich(r["lat"], r["lon"])
            except Exception as ex:  # noqa: BLE001 — één kapot antwoord mag de ronde niet stoppen
                store.save_parcel(int(r["id"]), {"error": f"niet bereikbaar: {str(ex)[:150]}"}, [])
                stats["mislukt"] += 1
                continue
            mism = catastro.compare(e, r["plot_m2"], r["built_m2"])
            store.save_parcel(int(r["id"]), e, mism)
            if e.get("rc"):
                stats["gevonden"] += 1
            else:
                stats["mislukt"] += 1
            if mism:
                stats["afwijkingen"] += 1
            if (e.get("distance_m") or 0) > catastro.ZEKER_M:
                stats["ver_van_de_pin"] += 1
            if not quiet:
                d = e.get("distance_m")
                print(f"{r['source_ref']:>14}  {e.get('rc') or '—':<16} "
                      f"{('in perceel' if d == 0 else f'{d:.1f} m' if d is not None else '—'):>11}  "
                      f"{(e.get('plot_m2') or 0):>7.0f} m²  {'; '.join(mism)[:80]}", flush=True)
        stats["gedeelde_pin"] = flag_shared_pins(store)
        return stats
    finally:
        store.close()


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=200)
    ap.add_argument("--only", default="")
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--quiet", action="store_true")
    a = ap.parse_args(argv)
    t0 = time.time()
    stats = run(a.limit, [x.strip() for x in a.only.split(",") if x.strip()] or None, a.force, a.quiet)
    print(f"{stats} in {time.time() - t0:.0f} s")
    return 0


if __name__ == "__main__":
    sys.exit(main())

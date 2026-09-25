"""Meet per perceel de helling en legt die vast, zodat de rekenaar het grondwerk kan meetellen.

Jan 25-09-2026: € 15.000 bij een licht hellend perceel, € 50.000 bij een steil perceel. Zonder een
gemeten helling rekent het model niets, en dat is precies de kostenpost die op de hellingen bij
Montgó en Balcón al Mar de grootste tegenvaller vormt.

Bron en methode: zie `dh/hoogte.py` en onderzoek/N08-helling-percelen.md. Gratis, geen sleutel,
CC BY 4.0. Een perceelgrens verandert niet, dus wat gemeten is wordt niet opnieuw opgehaald.
"""
from __future__ import annotations

import argparse
import json
import sys

import httpx

from . import config, focus, hoogte, perceel
from .store import Store

KOLOMMEN = (("helling", "REAL"), ("helling_p90", "REAL"), ("helling_oordeel", "TEXT"),
            ("hoogte_min", "REAL"), ("hoogte_max", "REAL"), ("helling_at", "TEXT"))


def zorg_kolommen(store) -> None:
    heeft = {r[1] for r in store.con.execute("PRAGMA table_info(parcels)")}
    for naam, soort in KOLOMMEN:
        if naam not in heeft:
            store.con.execute(f"ALTER TABLE parcels ADD COLUMN {naam} {soort}")
    store.con.commit()


def run(limit: int = 0, opnieuw: bool = False, alle: bool = False) -> dict:
    store = Store()
    zorg_kolommen(store)
    if alle:
        ids = [int(r["listing_id"]) for r in store.con.execute(
            "SELECT listing_id FROM parcels WHERE geojson IS NOT NULL")]
    else:
        ids = [int(r["id"]) for r in focus.rijen(store)]
    q = "SELECT listing_id, geojson, helling_oordeel FROM parcels WHERE geojson IS NOT NULL AND listing_id IN ({})"
    rijen = []
    for i in range(0, len(ids), 400):                     # SQLite heeft een grens op het aantal parameters
        deel = ids[i:i + 400]
        rijen += list(store.con.execute(q.format(",".join("?" * len(deel))), deel))
    todo = [r for r in rijen if opnieuw or not r["helling_oordeel"]]
    if limit:
        todo = todo[:limit]
    telling = {"percelen": len(rijen), "te_doen": len(todo), "gemeten": 0, "mislukt": 0,
               "vlak": 0, "licht": 0, "steil": 0}
    with httpx.Client(timeout=config.HTTP_TIMEOUT) as cl:
        for r in todo:
            try:
                m = hoogte.meet(json.loads(r["geojson"]), cl)
            except Exception:  # noqa: BLE001 — één kapot perceel mag de ronde niet laten vallen
                m = None
            if not m:
                telling["mislukt"] += 1
                continue
            store.con.execute(
                "UPDATE parcels SET helling=?, helling_p90=?, helling_oordeel=?, hoogte_min=?, "
                "hoogte_max=?, helling_at=datetime('now') WHERE listing_id=?",
                (m["helling"], m["helling_p90"], m["oordeel"], m["hoogte_min"], m["hoogte_max"],
                 int(r["listing_id"])))
            store.con.commit()
            telling["gemeten"] += 1
            telling[m["oordeel"]] = telling.get(m["oordeel"], 0) + 1
    store.close()
    return telling


def koppel(store=None) -> dict:
    """Zet de gemeten helling door naar de advertentie, maar alleen als het perceel het object ís.

    Bij één object uit het onderzoek was de advertentie een ático van 20 m² en het kadastrale perceel
    eronder een sportcomplex van 1.949 m². De helling van dat complex zegt niets over die woning, en
    een toeslag van € 50.000 zou daar pure verzinsel zijn. Daarom dezelfde toets als voor de fiscale
    waarde: afstand klein én de maten spreken elkaar niet tegen."""
    eigen = store is None
    store = store or Store()
    telling = {"met_helling": 0, "niet_gekoppeld": 0, "vlak": 0, "licht": 0, "steil": 0}
    rijen = store.con.execute(
        """SELECT l.id, l.plot_m2, l.built_m2, l.category, l.type, l.signals,
                  p.helling_oordeel, p.helling,
                  p.distance_m, p.plot_m2 AS p_plot, p.built_m2 AS p_built
           FROM listings l JOIN parcels p ON p.listing_id = l.id
           WHERE p.helling_oordeel IS NOT NULL AND l.gone_at IS NULL""").fetchall()
    for r in rijen:
        item = {"plot_m2": r["plot_m2"], "built_m2": r["built_m2"],
                "category": r["category"], "type": r["type"]}
        par = {"distance_m": r["distance_m"], "plot_m2": r["p_plot"], "built_m2": r["p_built"]}
        # Voor de hélling telt of het dezelfde grond is, niet of het gebouw klopt.
        gekoppeld = perceel.grond_is_hetzelfde(item, par)
        try:
            sg = json.loads(r["signals"] or "{}")
        except (TypeError, json.JSONDecodeError):
            sg = {}
        sg.pop("helling", None)
        sg.pop("helling_onzeker", None)
        if gekoppeld:
            sg["helling"] = r["helling_oordeel"]
            telling["met_helling"] += 1
            telling[r["helling_oordeel"]] = telling.get(r["helling_oordeel"], 0) + 1
        else:
            sg["helling_onzeker"] = r["helling_oordeel"]
            telling["niet_gekoppeld"] += 1
        sg["helling_pct"] = r["helling"]
        store.con.execute("UPDATE listings SET signals=? WHERE id=?",
                          (json.dumps(sg, ensure_ascii=False), int(r["id"])))
    store.con.commit()
    if eigen:
        store.close()
    return telling


if __name__ == "__main__":
    a = argparse.ArgumentParser(description="Helling per perceel meten bij het hoogtemodel van het IGN")
    a.add_argument("--limit", type=int, default=0)
    a.add_argument("--opnieuw", action="store_true")
    a.add_argument("--alle", action="store_true", help="ook percelen buiten de focus")
    a.add_argument("--alleen-koppelen", action="store_true", help="niet meten, alleen doorzetten")
    args = a.parse_args()
    if not args.alleen_koppelen:
        print(run(args.limit, args.opnieuw, args.alle))
    print(koppel())
    sys.exit(0)

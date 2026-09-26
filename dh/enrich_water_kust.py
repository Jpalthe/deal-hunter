"""Vult per perceel de overstromings- en kustgegevens uit de kaarten van het ministerie.

Jan, 26-09-2026: alleen het zwaarste valt automatisch af — een perceel in de doorstroomzone van de
rivier of in het openbaar zeegebied. De honderdjaarszone blijft in de lijst staan mét waarschuwing,
en er komt geen extra kostenpost bij; dat bedrag is niet vastgesteld en wordt hier dus niet verzonnen.

De zones van heel Jávea worden in zes verzoeken opgehaald en bewaard; daarna rekent alles lokaal.
Een perceelgrens verandert niet en deze kaarten zelden, dus één keer meten is genoeg.
"""
from __future__ import annotations

import argparse
import json
import sys

from . import water_kust
from .store import Store

KOLOMMEN = (("zfp", "INTEGER"), ("inundacion_t100", "INTEGER"), ("inundacion_t500", "INTEGER"),
            ("inundacion_zona", "TEXT"), ("inundacion_rio", "TEXT"), ("inundacion_studie", "TEXT"),
            ("inundacion_afstand_m", "REAL"), ("dph_zone", "TEXT"), ("marien_t100", "INTEGER"),
            ("kust_dpmt_m", "REAL"), ("kust_sp_m", "REAL"), ("kust_strook_m", "REAL"),
            ("kust_oordeel", "TEXT"), ("kust_dossier", "TEXT"),
            ("water_uitsluiting", "TEXT"), ("water_kust_at", "TEXT"))


def zorg_kolommen(store) -> None:
    heeft = {r[1] for r in store.con.execute("PRAGMA table_info(parcels)")}
    for naam, soort in KOLOMMEN:
        if naam not in heeft:
            store.con.execute(f"ALTER TABLE parcels ADD COLUMN {naam} {soort}")
    store.con.commit()


def run(limit: int = 0, opnieuw: bool = False) -> dict:
    store = Store()
    zorg_kolommen(store)
    zones = water_kust.haal_zones(opnieuw=opnieuw)
    if not any((zones.get("lagen") or {}).get(k, {}).get("vormen") for k in ("zfp", "t100", "dpmt")):
        store.close()
        return {"overgeslagen": "geen zones opgehaald; bron niet bereikbaar"}
    q = "SELECT listing_id, geojson FROM parcels WHERE geojson IS NOT NULL"
    if not opnieuw:
        q += " AND water_kust_at IS NULL"
    rijen = store.con.execute(q).fetchall()
    if limit:
        rijen = rijen[:limit]
    telling = {"te_doen": len(rijen), "gemeten": 0, "mislukt": 0,
               "zfp": 0, "t100": 0, "t500": 0, "in_dpmt": 0, "in_servidumbre": 0, "uitgesloten": 0}
    for r in rijen:
        try:
            m = water_kust.meet(json.loads(r["geojson"]), zones)
        except Exception:  # noqa: BLE001 — één kapotte grens mag de ronde niet laten vallen
            m = None
        if not m:
            telling["mislukt"] += 1
            continue
        store.con.execute(
            """UPDATE parcels SET zfp=?, inundacion_t100=?, inundacion_t500=?, inundacion_zona=?,
                   inundacion_rio=?, inundacion_studie=?, inundacion_afstand_m=?, dph_zone=?,
                   marien_t100=?, kust_dpmt_m=?, kust_sp_m=?, kust_strook_m=?, kust_oordeel=?,
                   kust_dossier=?, water_uitsluiting=?, water_kust_at=datetime('now')
               WHERE listing_id=?""",
            (int(bool(m.get("zfp"))), int(bool(m.get("t100"))), int(bool(m.get("t500"))),
             m.get("t100_zone") or m.get("t500_zone"), m.get("t100_rio") or m.get("t500_rio"),
             m.get("t100_studie") or m.get("t500_studie"), m.get("t100_afstand_m"),
             m.get("dph_zone"), int(bool(m.get("marien_t100"))), m.get("kust_dpmt_m"),
             m.get("kust_sp_m"), m.get("kust_strook_m"), m.get("kust_oordeel"),
             m.get("kust_dossier"), m.get("uitsluiting"), int(r["listing_id"])))
        telling["gemeten"] += 1
        for k in ("zfp", "t100", "t500"):
            if m.get(k):
                telling[k] += 1
        if m.get("kust_oordeel") in ("in_dpmt", "in_servidumbre"):
            telling[m["kust_oordeel"]] += 1
        if m.get("uitsluiting"):
            telling["uitgesloten"] += 1
        store.con.commit()
    store.close()
    return telling


def koppel(store=None) -> dict:
    """Zet de uitslag door naar de advertentie: uitsluiting hard, de rest als waarschuwing."""
    eigen = store is None
    store = store or Store()
    telling = {"uitgesloten": 0, "gewaarschuwd": 0}
    rijen = store.con.execute(
        """SELECT l.id, l.signals, p.zfp, p.inundacion_t100, p.inundacion_t500, p.inundacion_rio,
                  p.kust_oordeel, p.water_uitsluiting, p.distance_m
           FROM listings l JOIN parcels p ON p.listing_id = l.id
           WHERE p.water_kust_at IS NOT NULL AND l.gone_at IS NULL""").fetchall()
    for r in rijen:
        # Ligt de pin ver van het perceel, dan zegt de kaartuitslag niets over dit object.
        if (r["distance_m"] or 0) > 25:
            continue
        try:
            sg = json.loads(r["signals"] or "{}")
        except (TypeError, json.JSONDecodeError):
            sg = {}
        m = {"zfp": r["zfp"], "t100": r["inundacion_t100"], "t500": r["inundacion_t500"],
             "t100_rio": r["inundacion_rio"], "kust_oordeel": r["kust_oordeel"]}
        for sleutel in ("water_uitsluiting", "water_waarschuwing"):
            sg.pop(sleutel, None)
        if r["water_uitsluiting"]:
            sg["water_uitsluiting"] = r["water_uitsluiting"]
            telling["uitgesloten"] += 1
        w = water_kust.waarschuwing(m)
        if w:
            sg["water_waarschuwing"] = w
            telling["gewaarschuwd"] += 1
        store.con.execute("UPDATE listings SET signals=? WHERE id=?",
                          (json.dumps(sg, ensure_ascii=False), int(r["id"])))
    store.con.commit()
    if eigen:
        store.close()
    return telling


if __name__ == "__main__":
    a = argparse.ArgumentParser(description="Overstroming en kustwet per perceel ophalen bij MITECO")
    a.add_argument("--limit", type=int, default=0)
    a.add_argument("--opnieuw", action="store_true")
    args = a.parse_args()
    print(run(args.limit, args.opnieuw))
    print(koppel())
    sys.exit(0)

"""Koppelt elke advertentie met een coördinaat aan de kadastrale waardezone waarin zij ligt.

De zones komen in drie verzoeken binnen (één per gemeente) en daarna rekent alles lokaal: punt in
vlak, en bij overlap beslist de typologie. Zones veranderen hoogstens één keer per jaar, dus het
zonebestand blijft staan tot iemand `--zones-opnieuw` meegeeft.

Ook wat níet gekoppeld kon worden krijgt een rij, met de reden erbij. Zo is aan de tabel te zien
of een object nog niet is nagekeken of wél is nagekeken en geen zone heeft.
"""
from __future__ import annotations

import argparse
import sys

from . import zonewaarde
from .store import Store, now_iso

VELDEN = ("gemeente", "gemeente_naam", "zona_valor", "cod_zona", "ejercicio", "num_inmuebles",
          "tipologia", "categoria", "antiguedad", "conservacion", "superficie", "superficie_suelo",
          "val_tipo", "val_tipo_m2", "val_estandar_m2")


def run(limit: int = 0, opnieuw: bool = False, zones_opnieuw: bool = False) -> dict:
    store = Store()
    zones = zonewaarde.haal_zones(opnieuw=zones_opnieuw)
    beschikbaar = sum(len(g.get("zones") or []) for g in (zones.get("gemeenten") or {}).values())
    if not beschikbaar:
        store.close()
        return {"overgeslagen": "geen waardezones opgehaald; het kadaster antwoordde niet"}
    q = ("SELECT l.id, l.lat, l.lon, l.type FROM listings l "
         "WHERE l.gone_at IS NULL AND l.lat IS NOT NULL AND l.lon IS NOT NULL")
    if not opnieuw:
        q += " AND l.id NOT IN (SELECT listing_id FROM zonewaarde)"
    if limit:
        q += f" LIMIT {int(limit)}"
    rijen = store.con.execute(q).fetchall()
    gekoppeld = overgeslagen = 0
    redenen: dict[str, int] = {}
    for r in rijen:
        u = zonewaarde.zoek(r["lat"], r["lon"], r["type"], zones)
        rij = {k: (u.get(k) if u.get("gevonden") else None) for k in VELDEN}
        rij.update(listing_id=int(r["id"]), overlap=u.get("overlap"), reden=u.get("reden"), at=now_iso())
        kolommen = ", ".join(rij)
        store.con.execute(f"INSERT OR REPLACE INTO zonewaarde ({kolommen}) "
                          f"VALUES ({', '.join(':' + k for k in rij)})", rij)
        if u.get("gevonden"):
            gekoppeld += 1
        else:
            overgeslagen += 1
            sleutel = (u.get("reden") or "onbekend").split(" (")[0]
            redenen[sleutel] = redenen.get(sleutel, 0) + 1
    store.con.commit()
    store.close()
    return {"bekeken": len(rijen), "gekoppeld": gekoppeld, "niet_gekoppeld": overgeslagen,
            "redenen": redenen, "zones_beschikbaar": beschikbaar,
            "jaargang": {k: g.get("ejercicio") for k, g in (zones.get("gemeenten") or {}).items()}}


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Advertenties koppelen aan de kadastrale waardezones")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--opnieuw", action="store_true", help="ook advertenties die al een rij hebben")
    ap.add_argument("--zones-opnieuw", action="store_true", help="de zones opnieuw bij het kadaster ophalen")
    a = ap.parse_args(argv)
    uit = run(limit=a.limit, opnieuw=a.opnieuw, zones_opnieuw=a.zones_opnieuw)
    for k, v in uit.items():
        print(f"{k}: {v}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

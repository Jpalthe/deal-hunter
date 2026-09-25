"""Vult per object de bestemming en de fiscale referentiewaarde uit Goolzoom.

Alleen objecten binnen de focus en alleen als er een kadastrale referentie ligt: zonder perceel is
er niets te bevragen. Wat er al staat en jonger is dan `goolzoom.VERVERS_DAGEN` wordt overgeslagen,
want elke bevraging kost geld.

De referentiewaarde wordt alleen opgehaald als het perceel één of enkele eenheden heeft. Bij een
perceel met veel eenheden (een appartementengebouw) zegt de som niets over wat er te koop staat;
dan bewaren wij alleen het aantal.
"""
from __future__ import annotations

import argparse
import sys

import httpx

from . import config, focus, goolzoom
from .store import Store

MAX_EENHEDEN_VOOR_WAARDE = 4


def een(store, rij, client) -> dict:
    lid = int(rij["id"])
    par = store.parcel(lid)
    rc = (dict(par).get("rc") if par else None) or ""
    if len(rc) != goolzoom.RC14:
        return {"id": lid, "status": "geen perceel"}
    try:
        u = goolzoom.urbanisme(rc, "classification", client)
        if not u:
            goolzoom.bewaar(store, lid, None, error="geen urbanismegegevens voor dit perceel")
            return {"id": lid, "status": "leeg"}
        eh = goolzoom.eenheden(rc, client)
        waarde, aantal = None, len(eh)
        if 0 < aantal <= MAX_EENHEDEN_VOOR_WAARDE:
            som = 0.0
            for e in eh:
                v = goolzoom.referentiewaarde(e["rc"], client)
                if v:
                    som += v
            waarde = round(som) if som > 0 else None
        goolzoom.bewaar(store, lid, u, ref_waarde=waarde, ref_eenheden=aantal)
        return {"id": lid, "status": "ok", "cls": u.get("classificatie"),
                "zone": u.get("zonering"), "waarde": waarde, "eenheden": aantal}
    except Exception as e:  # noqa: BLE001
        goolzoom.bewaar(store, lid, None, error=f"{type(e).__name__}: {str(e)[:150]}")
        return {"id": lid, "status": "fout", "fout": f"{type(e).__name__}: {str(e)[:120]}"}


def run(limit: int = 0, opnieuw: bool = False) -> dict:
    if not goolzoom.beschikbaar():
        return {"overgeslagen": "GOOLZOOM_API_KEY ontbreekt in .env"}
    store = Store()
    goolzoom.zorg_tabel(store)
    rijen = [r for r in focus.rijen(store)]
    todo = [r for r in rijen if opnieuw or not goolzoom.vers(store, int(r["id"]))]
    if limit:
        todo = todo[:limit]
    telling = {"in_focus": len(rijen), "te_doen": len(todo), "ok": 0, "leeg": 0,
               "geen perceel": 0, "fout": 0, "wonen_nee": 0, "wonen_voorwaardelijk": 0, "met_waarde": 0}
    with httpx.Client(timeout=config.HTTP_TIMEOUT) as client:
        for r in todo:
            res = een(store, r, client)
            telling[res["status"]] = telling.get(res["status"], 0) + 1
            if res["status"] == "ok":
                d = goolzoom.duiding(res.get("cls"))
                if d["wonen"] == "nee":
                    telling["wonen_nee"] += 1
                elif d["wonen"] == "voorwaardelijk":
                    telling["wonen_voorwaardelijk"] += 1
                if res.get("waarde"):
                    telling["met_waarde"] += 1
    store.close()
    return telling


if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Bestemming en referentiewaarde ophalen bij Goolzoom")
    p.add_argument("--limit", type=int, default=0, help="hoogstens zoveel objecten")
    p.add_argument("--opnieuw", action="store_true", help="ook wat al opgehaald is opnieuw ophalen")
    a = p.parse_args()
    out = run(a.limit, a.opnieuw)
    print({k: v for k, v in out.items() if v})
    sys.exit(0)

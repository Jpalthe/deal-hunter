"""Haalt alsnog de coördinaat op bij de makelaarssites waarvan dat mag.

Alleen de sites die in `onderzoek/N12-coordinaten-makelaarssites.json` als bruikbaar zijn gemeten
(zie dh/coordinaat.py). Eén verzoek per object, met dezelfde beleefdheidsregels als de leesronde:
robots.txt vooraf, pauze tussen verzoeken.

Ná afloop nog één controle die tijdens het lezen niet te maken is: komt hetzelfde punt bij meer dan
drie objecten van dezelfde site voor, dan is het geen adres maar een standaardwaarde, en gaan die
objecten alsnog leeg de database in. Zo kan een site die tijdens de meting vier keer netjes
antwoordde ons alsnog niet vervuilen.
"""
from __future__ import annotations

import argparse
import sys

import httpx

from . import config, coordinaat
from .adapters.makelaars import Site, laad_kantoren
from .store import Store

MAX_ZELFDE_PUNT = 3


def run(limit: int = 0, hosts: list[str] | None = None) -> dict:
    toegestaan = coordinaat.toegestane_sites()
    if hosts:
        toegestaan = {h: p for h, p in toegestaan.items() if h in hosts}
    if not toegestaan:
        return {"overgeslagen": "geen enkele site is gemeten als bruikbaar"}
    kantoren = {k.host: k for k in laad_kantoren()}
    store = Store()
    uit: dict = {"sites": {}, "gevonden": 0, "geweigerd_dubbel": 0}
    with httpx.Client(timeout=config.HTTP_TIMEOUT, follow_redirects=True,
                      headers={"User-Agent": config.USER_AGENT, "Accept-Language": "es,en;q=0.8,nl;q=0.6"}) as c:
        for host in toegestaan:
            k = kantoren.get(host)
            if not k or not k.toegestaan:
                uit["sites"][host] = "niet (meer) toegestaan in kader/makelaars.json"
                continue
            q = ("SELECT id, url FROM listings WHERE source=? AND gone_at IS NULL AND lat IS NULL "
                 "AND url IS NOT NULL ORDER BY id")
            par: tuple = (f"makelaar:{host}",)
            if limit:
                q += " LIMIT ?"
                par = par + (int(limit),)
            rijen = store.con.execute(q, par).fetchall()
            s = Site(k, c)
            punten: dict[int, tuple[float, float]] = {}
            gelezen = 0
            for r in rijen:
                t = s.haal(r["url"])
                if t is None:
                    continue
                gelezen += 1
                p = coordinaat.uit_pagina(t, host)
                if p:
                    punten[int(r["id"])] = p
            # standaardwaarden eruit: een punt dat bij meer dan drie objecten hoort, is geen adres
            hoevaak: dict[tuple, int] = {}
            for p in punten.values():
                hoevaak[p] = hoevaak.get(p, 0) + 1
            dubbel = {p for p, n in hoevaak.items() if n > MAX_ZELFDE_PUNT}
            schoon = {lid: p for lid, p in punten.items() if p not in dubbel}
            for lid, (la, lo) in schoon.items():
                store.con.execute("UPDATE listings SET lat=?, lon=? WHERE id=?", (la, lo, lid))
            store.con.commit()
            uit["gevonden"] += len(schoon)
            uit["geweigerd_dubbel"] += len(punten) - len(schoon)
            uit["sites"][host] = {"bekeken": len(rijen), "gelezen": gelezen, "gevonden": len(schoon),
                                  "geweigerd_dubbel": len(punten) - len(schoon),
                                  "dubbele_punten": sorted(dubbel)[:3]}
            print(f"{host:28s} {len(schoon):4d} van {len(rijen)} objecten", flush=True)
    store.close()
    return uit


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Coördinaten ophalen bij de gemeten makelaarssites")
    ap.add_argument("--limit", type=int, default=0, help="hoogstens zoveel objecten per site")
    ap.add_argument("--hosts", default="")
    a = ap.parse_args(argv)
    for k, v in run(a.limit, [h.strip() for h in a.hosts.split(",") if h.strip()] or None).items():
        print(f"{k}: {v}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

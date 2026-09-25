"""Zet de oogst van de officiële Idealista-assistent in de database als bron 'idealista-zoek'.

De bestanden in onderzoek/idealista/*.json zijn geschreven door zoekagents die de assistent
bevragen. Scrapen gebeurt niet en mag niet; dit is de enige toegestane weg naar Idealista tot de
Search API is toegekend.

  python -m dh.import_idealista [--dir onderzoek/idealista]

Idempotent: dezelfde advertentie in twee zoekopdrachten wordt één rij. Prijsdalingen die de
assistent meldt worden als gebeurtenis vastgelegd, ook als wij het object voor het eerst zien.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

from . import config, prefilter, signals
from .store import Store

SOURCE = "idealista-zoek"

# Idealista-typologie → het type zoals de rest van het systeem het kent
TYPE = {
    "land": "Land", "chalet": "Villa", "flat": "Apartment", "penthouse": "Penthouse",
    "duplex": "Duplex", "studio": "Studio", "countryHouse": "Country House", "building": "Building",
    "premise": "Commercial", "garage": "Garage", "office": "Office", "storageRoom": "Storage",
}
SUB = {"terracedHouse": "Town house", "semidetachedHouse": "Town house", "independantHouse": "Villa",
       "casaDePueblo": "Town house", "casaDeAldea": "Country House", "cortijo": "Country House",
       "masia": "Country House", "castillo": "Country House"}

# Signalen uit de oogst die als blokkade of als kans gelden
BLOKKADES = {
    "urbanisatie niet opgeleverd": "Urbanisatie mogelijk niet opgeleverd aan de gemeente — dit is de harde uitsluiting van Jan",
    "bankgarantie": "Bankgarantie genoemd: wijst op een urbanisatie die de gemeente nog niet heeft overgenomen",
    "zonder vergunning": "Bouwwerk zonder vergunning genoemd",
    "verdeeld eigendom": "Onverdeeld aandeel of gedeeld eigendom",
    "vruchtgebruik": "Blote eigendom of vruchtgebruik",
    "gerechtelijke procedure": "Verkregen via een gerechtelijke procedure: bezit en staat vaak onbekend",
    "bouw stilgelegd": "Stilgelegde bouw: vergunningstermijn kan verlopen zijn",
}
DRUK = {"bank of servicer", "gerechtelijke procedure", "erfenis", "scheiding", "haast bij verkoper", "prijs verlaagd", "bouw stilgelegd"}


def load(d: Path) -> list[dict]:
    """Leest alle oogstbestanden en ontdubbelt op advertentiecode."""
    out: dict[str, dict] = {}
    for f in sorted(d.glob("*.json")):
        try:
            j = json.loads(f.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError) as e:
            print(f"overgeslagen: {f.name} ({e})", file=sys.stderr)
            continue
        for o in j.get("objecten") or []:
            code = str(o.get("code") or "").strip()
            if not code:
                continue
            o["_slice"] = j.get("slice") or f.stem
            prev = out.get(code)
            if prev is None:
                out[code] = o
            else:
                # samenvoegen: de rijkste beschrijving en alle signalen behouden
                if len(o.get("desc") or "") > len(prev.get("desc") or ""):
                    prev["desc"] = o["desc"]
                prev["signalen"] = sorted(set((prev.get("signalen") or []) + (o.get("signalen") or [])))
                for k in ("plot_size", "size", "rooms", "bathrooms", "former_price", "price_drop_pct", "lat", "lon"):
                    if prev.get(k) in (None, 0) and o.get(k) not in (None, 0):
                        prev[k] = o[k]
    return list(out.values())


def normalise(o: dict) -> dict:
    title = str(o.get("title") or "")
    subtitle = str(o.get("subtitle") or "")
    desc = str(o.get("desc") or "")
    typ = SUB.get(o.get("sub_typology")) or TYPE.get(o.get("typology")) or (o.get("typology") or "")
    # De plaatsnaam staat in de ondertitel ("Jávea/Xàbia, Alicante"); de wijk in de titel.
    town_raw = subtitle.split(",")[0].strip() if subtitle else ""
    # Idealista zet de titel neer als "<soort> en <straat en wijk>, <plaats>". De wijk is dus wat er
    # tussen " en " en de plaatsnaam staat. Zonder deze regel kwam de plaatsnaam zelf als wijk binnen
    # en viel de vergelijkingsreeks op de verkeerde wijk terug.
    kop = title.rsplit(",", 1)[0] if "," in title else title
    loc = kop.split(" en ", 1)[1].strip() if " en " in kop else kop.strip()
    if town_raw and loc.lower() == town_raw.lower():
        loc = ""
    text = f"{title} {desc}"
    return {
        "source_ref": str(o["code"]),
        "area": config.area_of(town_raw, None, f"{title} {desc[:300]}"),
        "town": config.norm_place(town_raw),
        "town_raw": town_raw,
        "postcode": None,
        "type": typ,
        "price": o.get("price"),
        "currency": "EUR",
        "built_m2": o.get("size") if typ != "Land" else None,
        "plot_m2": o.get("plot_size") or (o.get("size") if typ == "Land" else None),
        "beds": int(o["rooms"]) if isinstance(o.get("rooms"), (int, float)) else None,
        "baths": int(o["bathrooms"]) if isinstance(o.get("bathrooms"), (int, float)) else None,
        "lat": o.get("lat") if config.valid_coord(o.get("lat"), o.get("lon")) else None,
        "lon": o.get("lon") if config.valid_coord(o.get("lat"), o.get("lon")) else None,
        "location_detail": loc,
        "url": o.get("url"),
        "title": title[:200],
        "desc_hash": hashlib.sha256(desc.encode("utf-8")).hexdigest()[:16],
        "desc_excerpt": desc[:600],
        "features": o.get("signalen") or [],
        "images_count": 0,
        "source_date": None,
        "new_build": 1 if o.get("new_development") else 0,
        "_text": text,
        "_features": " ".join(o.get("signalen") or []),
        "_raw": o,
    }


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", default=str(config.ROOT / "onderzoek" / "idealista"))
    a = ap.parse_args(argv)
    d = Path(a.dir)
    if not d.exists():
        print(f"geen oogstmap: {d}", file=sys.stderr)
        return 1
    rows = load(d)
    if not rows:
        print("geen objecten gevonden in de oogst", file=sys.stderr)
        return 1

    pf = prefilter.Prefilter()
    store = Store()
    run_id = store.start_run("import-idealista")
    seen: set[str] = set()
    stats = {"nieuw": 0, "bijgewerkt": 0, "buiten_werkgebied": 0, "prijsdalingen": 0, "druk": 0}
    for o in rows:
        rec = normalise(o)
        if not rec["area"]:
            stats["buiten_werkgebied"] += 1
            continue
        seen.add(rec["source_ref"])
        raw = rec.pop("_raw")
        lid, kind, _ = store.upsert_listing(run_id, SOURCE, rec)
        stats["nieuw" if kind in ("NIEUW", "NULMETING") else "bijgewerkt"] += 1

        sig = signals.analyse(rec["_text"], rec["_features"], rec["type"], bool(rec["new_build"]))
        oogst = raw.get("signalen") or []
        sig["oogst_signalen"] = oogst
        sig["blockers"] = list(dict.fromkeys((sig.get("blockers") or []) + [BLOKKADES[s] for s in oogst if s in BLOKKADES]))
        drukte = sorted(set(oogst) & DRUK)
        if raw.get("price_drop_pct"):
            drukte = sorted(set(drukte + ["prijs verlaagd"]))
        sig["verkoopdruk"] = drukte
        if drukte:
            stats["druk"] += 1
        pfr = pf.run(rec, sig)
        store.set_analysis(lid, signals=sig, category=pfr["category"], prefilter=pfr)

        # Prijsdaling die Idealista zelf meldt, ook bij een eerste waarneming
        if raw.get("former_price") and raw.get("price") and raw["former_price"] > raw["price"]:
            store.add_event(run_id, "PRIJS GEWIJZIGD", listing_id=lid,
                            details={"van": raw["former_price"], "naar": raw["price"],
                                     "pct": -abs(raw.get("price_drop_pct") or round((raw["former_price"] - raw["price"]) / raw["former_price"] * 100)),
                                     "bron": "Idealista-assistent meldt een prijsverlaging"})
            stats["prijsdalingen"] += 1

    gone = store.mark_gone(run_id, SOURCE, seen)
    store.source_status(SOURCE, True, count=len(seen))
    store.finish_run(run_id, "ok", {**stats, "niet_meer_gevonden": len(gone)})
    store.close()
    print(json.dumps({**stats, "niet_meer_gevonden": len(gone), "in_werkgebied": len(seen)}, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())

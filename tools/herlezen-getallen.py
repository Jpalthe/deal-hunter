#!/usr/bin/env python3
"""Leest objecten opnieuw waarvan de getallen niet kunnen kloppen.

Aanleiding 27-09-2026: `_num` haalde élke punt uit een getal weg, omdat een punt in Spanje
duizendtallen scheidt. In een JSON-LD-veld is hij een decimaalteken: `"floorSize": "795.00"` werd
zo 79.500 m². 191 objecten hadden daardoor een bebouwd oppervlak dat niet bestaat, tot 83.235 m²
aan toe. Die getallen gaan rechtstreeks de bouwkosten en de verkoopwaarde in, dus een fout hier
verandert elk bedrag in het dossier.

De lezer is hersteld; dit haalt de pagina's van de getroffen objecten opnieuw op en zet de
gecorrigeerde waarden terug. Alleen prijs, oppervlak, slaapkamers en badkamers worden bijgewerkt —
verder blijft de advertentie zoals zij was.

  python tools/herlezen-getallen.py           # laat zien wat er zou veranderen
  python tools/herlezen-getallen.py --doen
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import httpx

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from dh import config                                              # noqa: E402
from dh.adapters.makelaars import Site, laad_kantoren, ontleed     # noqa: E402
from dh.store import Store                                         # noqa: E402

# Grenzen waarboven een waarde niet van een woning kan zijn. Ruim genomen: een perceel van
# 108.000 m² bestaat hier wél (en staat ook echt in de lijst), een woning van 1.500 m² niet.
ONMOGELIJK = "(built_m2 > 1500 OR plot_m2 > 60000 OR price > 15000000)"
VELDEN = ("price", "built_m2", "plot_m2", "beds", "baths")

# Tweede soort fout, gevonden dezelfde dag: waarden uit een keuzelijst. De prijs- en
# oppervlaktefilters bovenaan een site staan in <option>-elementen en telden mee als paginatekst,
# dus de lezer pakte de eerste waarde uit het filter. Gevolg: 293 objecten van één site met een
# vraagprijs van € 50.000 (de echte was € 690.000) en 138 van een andere met 50 m² bebouwd.
# Herkenbaar doordat één waarde een groot deel van één bron beslaat; bij een echte portaalbron komt
# de vaakste prijs op een paar procent uit (idealista-zoek: 19 van ruim achthonderd).
MIN_AANTAL = 9
MIN_AANDEEL = 0.15


def gedeelde_waarden(store) -> list[tuple[str, str, float, int, int]]:
    """(bron, veld, waarde, aantal, totaal) voor waarden die een bron domineren."""
    uit = []
    for veld in ("price", "built_m2", "plot_m2"):
        for r in store.con.execute(f"""
            WITH v AS (SELECT source, {veld} w, count(*) n FROM listings
                       WHERE gone_at IS NULL AND {veld} IS NOT NULL GROUP BY 1,2),
                 t AS (SELECT source, count(*) tot FROM listings
                       WHERE gone_at IS NULL AND {veld} IS NOT NULL GROUP BY 1)
            SELECT v.source, v.w, v.n, t.tot FROM v JOIN t ON t.source=v.source
            WHERE v.n >= ? AND v.n * 1.0 / t.tot >= ?""", (MIN_AANTAL, MIN_AANDEEL)):
            uit.append((r["source"], veld, r["w"], r["n"], r["tot"]))
    return uit


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--doen", action="store_true")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--gedeeld", action="store_true",
                    help="ook objecten met een waarde die een hele bron domineert (keuzelijstwaarden)")
    a = ap.parse_args(argv)
    store = Store()
    waar = ONMOGELIJK
    if a.gedeeld:
        gd = gedeelde_waarden(store)
        print("waarden die een bron domineren en dus uit een keuzelijst komen:")
        for bron, veld, w, n, tot in sorted(gd, key=lambda x: -x[3]):
            print(f"  {n:4d} van {tot:4d}  {veld:9s} {w:>10,.0f}   {bron.split(':')[-1]}".replace(",", "."))
        if gd:
            stukken = " OR ".join(f"(source='{b}' AND {v}={w})" for b, v, w, _, _ in gd)
            waar = f"({waar} OR {stukken})"
    q = (f"SELECT id, source, url, title, price, built_m2, plot_m2, beds, baths FROM listings "
         f"WHERE gone_at IS NULL AND source LIKE 'makelaar:%' AND {waar} ORDER BY id")
    if a.limit:
        q += f" LIMIT {int(a.limit)}"
    rijen = store.con.execute(q).fetchall()
    kantoren = {k.host: k for k in laad_kantoren()}
    print(f"\n{len(rijen)} objecten om opnieuw te lezen")
    sites: dict[str, Site] = {}
    gewijzigd = mislukt = ongewijzigd = 0
    # Rem tegen een site die onder het lezen dichtklapt. Op 27-09-2026 leverde lauroravillas bij een
    # ronde van achthonderd pagina's honderddertig keer dezelfde prijs; drie dezelfde pagina's, los
    # opgehaald, gaven wél de echte bedragen. De site gaf onder druk een standaardpagina terug en
    # wij schreven die weg — de herstelronde maakte de gegevens dus slechter. Komt bij een site
    # vijf keer achter elkaar hetzelfde nieuwe getal, dan stoppen wij met die site.
    achtereen: dict[str, list] = {}
    gestaakt: set[str] = set()
    MAX_ACHTEREEN = 5
    with httpx.Client(timeout=config.HTTP_TIMEOUT, follow_redirects=True,
                      headers={"User-Agent": config.USER_AGENT, "Accept-Language": "es,en;q=0.8,nl;q=0.6"}) as c:
        for r in rijen:
            host = r["source"].split(":", 1)[-1]
            if host in gestaakt:
                continue
            k = kantoren.get(host)
            if not k or not k.toegestaan:
                mislukt += 1
                continue
            s = sites.get(host) or sites.setdefault(host, Site(k, c))
            t = s.haal(r["url"])
            rec = ontleed(t, r["url"], k) if t else None
            if not rec:
                mislukt += 1
                continue
            # Alleen bijwerken waar de nieuwe lezing werkelijk iets oplevert. Geeft zij niets,
            # dan houden wij wat er stond: een leeg veld is geen correctie maar verlies.
            anders = {v: rec.get(v) for v in VELDEN
                      if rec.get(v) and (rec.get(v) or 0) != (r[v] or 0)}
            if not anders:
                ongewijzigd += 1
                continue
            vinger = tuple(sorted((v, n) for v, n in anders.items()))
            reeks = achtereen.setdefault(host, [])
            reeks.append(vinger)
            if len(reeks) >= MAX_ACHTEREEN and len(set(reeks[-MAX_ACHTEREEN:])) == 1:
                gestaakt.add(host)
                print(f"  GESTAAKT {host}: {MAX_ACHTEREEN} keer achter elkaar dezelfde nieuwe waarde "
                      f"{vinger}. Dat is geen advertentie maar een standaardpagina; deze site is "
                      f"niet bijgewerkt.", flush=True)
                continue
            gewijzigd += 1
            print(f"  {r['id']:5d} {host:24s} " + ", ".join(
                f"{v}: {r[v] or 0:.0f} → {n or 0:.0f}" for v, n in anders.items()))
            if a.doen:
                store.con.execute(
                    "UPDATE listings SET " + ", ".join(f"{v}=?" for v in anders) + " WHERE id=?",
                    tuple(anders.values()) + (r["id"],))
    if a.doen:
        store.con.commit()
    store.close()
    if gestaakt:
        print("\ngestaakte sites (gaven steeds hetzelfde terug, niet bijgewerkt): " + ", ".join(sorted(gestaakt)))
    print(f"\ngewijzigd {gewijzigd} · ongewijzigd {ongewijzigd} · niet gelukt {mislukt}"
          + ("" if a.doen else "  — niets opgeslagen; met --doen wel"))
    return 0


if __name__ == "__main__":
    sys.exit(main())

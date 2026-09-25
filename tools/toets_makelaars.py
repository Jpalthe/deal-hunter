#!/usr/bin/env python3
"""Toetst makelaarssites op automatisch lezen, zonder agents: alleen robots.txt, sitemap en homepage.

  python3 tools/toets_makelaars.py [--hosts bestand.txt] [--uit onderzoek/makelaars/toets-script.json]

Per site, hooguit vier verzoeken met twee seconden ertussen:
  1. robots.txt: mag User-agent * de aanbodpagina's lezen? Crawl-delay? Sitemap-regels?
  2. de sitemap: hoeveel URL's lijken op objectpagina's, en hoeveel daarvan liggen in ons gebied
  3. de homepage: welk systeem (Inmoweb, Mediaelx, Sooprema, Inmovilla, Witei, WordPress, eGO), en
     staat er een link naar aviso legal of voorwaarden (die pagina wordt hier niet gelezen; dat is
     mensenwerk of een aparte stap)
  4. niets anders: geen objectpagina's, geen formulieren

Het advies is voorzichtig: "lezen" alleen als robots.txt het toestaat én er een sitemap of
aanbodpagina is gevonden; "feed vragen" als robots.txt het verbiedt en het systeem een export
kent; "handmatig toetsen" als de voorwaarden nog niet zijn gelezen of niets is gevonden.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.robotparser
from urllib.parse import urljoin

import httpx

UA = "TREE-DealHunter/0.1 (intern gebruik; contact via treeproperties.es)"
PAUZE = 2.0
GEBIED = re.compile(r"(javea|xabia|benitachell|benitatxell|cumbre|moraira|teulada)", re.I)
OBJECT = re.compile(r"(-es\d{4,9}\.html$|-gb\d{4,9}\.html$|/(venta|sale|for-sale|te-koop|kaufen|inmueble|property|propiedad|villa|chalet|parcela|apartamento|casa)[-/][^/]*\d)", re.I)
CMS = [("inmoweb", "Inmoweb"), ("mediaelx", "Mediaelx"), ("letsinmo", "Mediaelx"), ("sooprema", "Sooprema"),
       ("inmovilla", "Inmovilla"), ("witei", "Witei"), ("egorealestate", "eGO"), ("ego-realestate", "eGO"),
       ("wp-content", "WordPress"), ("paagees", "Paagees"), ("resales-online", "Resales-Online"), ("kyero", "Kyero-widget")]
VOORWAARDEN = re.compile(r'href="([^"]*(aviso|legal|terms|condicion|privac)[^"]*)"', re.I)
EXPORT_CMS = {"Inmoweb", "Mediaelx", "Sooprema", "Inmovilla"}


def toets(host: str, c: httpx.Client) -> dict:
    web = f"https://{host}"
    uit = {"host": host, "website": web, "datum": time.strftime("%d-%m-%Y")}
    rp = urllib.robotparser.RobotFileParser()
    sitemaps: list[str] = []
    try:
        r = c.get(urljoin(web, "/robots.txt"))
        uit["robots_http"] = r.status_code
        if r.status_code == 200 and "<html" not in r.text[:300].lower():
            rp.parse(r.text.splitlines())
            uit["robots_regels_voor_ster"] = "\n".join(
                l for l in r.text.splitlines() if l.strip())[:600]
            sitemaps = [l.split(":", 1)[1].strip() for l in r.text.splitlines() if l.lower().startswith("sitemap:")]
            d = rp.crawl_delay("*")
            uit["crawl_delay"] = d
        else:
            rp.parse([])
            uit["robots_regels_voor_ster"] = "geen robots.txt" if r.status_code != 200 else "robots.txt is een HTML-pagina (geen echte robots)"
    except Exception as e:  # noqa: BLE001
        uit["robots_http"] = f"fout: {str(e)[:80]}"
        rp.parse([])
    time.sleep(PAUZE)
    mag_alles = rp.can_fetch("*", web + "/") and rp.can_fetch("*", web + "/venta/") and rp.can_fetch("*", web + "/properties/")
    uit["robots_toegestaan"] = "ja" if mag_alles else "nee"

    # sitemap
    n_obj = n_gebied = 0
    gevonden_sm = None
    for sm in sitemaps + [urljoin(web, p) for p in ("/sitemap.xml", "/sitemap_index.xml")]:
        try:
            r = c.get(sm)
            if r.status_code != 200 or "<loc>" not in r.text:
                continue
            locs = re.findall(r"<loc>\s*([^<\s]+)\s*</loc>", r.text)
            if locs and all(l.endswith(".xml") for l in locs[:5]):
                time.sleep(PAUZE)
                sub = []
                for l in locs[:6]:
                    try:
                        r2 = c.get(l)
                        if r2.status_code == 200:
                            sub += re.findall(r"<loc>\s*([^<\s]+)\s*</loc>", r2.text)
                    except Exception:  # noqa: BLE001
                        pass
                    time.sleep(1.0)
                locs = sub
            gevonden_sm = sm
            objs = [l for l in locs if OBJECT.search(l)]
            n_obj = len(objs)
            n_gebied = sum(1 for l in objs if GEBIED.search(l))
            break
        except Exception:  # noqa: BLE001
            continue
        finally:
            time.sleep(PAUZE)
    uit.update({"sitemap": gevonden_sm, "objectpaginas": n_obj, "in_gebied_volgens_url": n_gebied})

    # homepage: systeem en link naar voorwaarden
    try:
        r = c.get(web + "/")
        t = r.text.lower()
        uit["homepage_http"] = r.status_code
        uit["cms"] = next((naam for spoor, naam in CMS if spoor in t), "onbekend")
        m = VOORWAARDEN.search(r.text)
        uit["voorwaarden_link"] = urljoin(web, m.group(1)) if m else None
        uit["botcontrole"] = bool(re.search(r"(verifying your browser|security check|cf-chl|captcha)", t))
    except Exception as e:  # noqa: BLE001
        uit["homepage_http"] = f"fout: {str(e)[:80]}"
        uit["cms"] = "onbekend"
    time.sleep(PAUZE)

    if uit.get("botcontrole"):
        uit["advies"] = "handmatig toetsen"
        uit["toelichting"] = "De homepage toont een botcontrole. Niet omzeilen; eerst kijken of het kantoor een feed heeft."
    elif uit["robots_toegestaan"] == "nee":
        uit["advies"] = "feed vragen" if uit.get("cms") in EXPORT_CMS else "overslaan"
        uit["toelichting"] = "robots.txt verbiedt automatisch lezen van de aanbodpagina's."
    elif n_obj == 0 and not gevonden_sm:
        uit["advies"] = "handmatig toetsen"
        uit["toelichting"] = "robots.txt staat lezen toe, maar geen sitemap gevonden; de aanbodpagina's moeten met de hand worden aangewezen."
    else:
        uit["advies"] = "lezen"
        uit["toelichting"] = (f"robots.txt staat lezen toe; sitemap met {n_obj} objectpagina's, {n_gebied} in ons gebied volgens de URL. "
                              + ("Voorwaarden gevonden maar niet gelezen: eerst nakijken." if uit.get("voorwaarden_link") else "Geen link naar voorwaarden gevonden."))
    return uit


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--hosts", default="onderzoek/makelaars/nog-te-toetsen.txt")
    ap.add_argument("--uit", default="onderzoek/makelaars/toets-script.json")
    a = ap.parse_args()
    hosts = [h.strip() for h in open(a.hosts, encoding="utf-8") if h.strip()]
    uit = []
    with httpx.Client(timeout=20, follow_redirects=True, headers={"User-Agent": UA, "Accept-Language": "es,en;q=0.8"}) as c:
        for i, h in enumerate(hosts, 1):
            try:
                res = toets(h, c)
            except Exception as e:  # noqa: BLE001
                res = {"host": h, "advies": "handmatig toetsen", "toelichting": f"fout: {str(e)[:100]}"}
            uit.append(res)
            print(f"{i:>3}/{len(hosts)} {h:<38} {res.get('advies'):<18} obj {res.get('objectpaginas', 0):>5}  gebied {res.get('in_gebied_volgens_url', 0):>4}  {res.get('cms', '?')}", flush=True)
            json.dump(uit, open(a.uit, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    return 0


if __name__ == "__main__":
    sys.exit(main())

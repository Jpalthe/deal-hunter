"""Haalt van objecten die al in de database staan alsnog de eerste foto op.

De makelaarsadapter bewaart sinds 25-09-2026 de `og:image` van elke objectpagina, maar de objecten
die daarvoor zijn ingelezen hebben er geen. Die pagina's opnieuw helemaal lezen kost een volle ronde;
alleen de foto ophalen is één verzoek per object.

Zelfde regels als de gewone leesronde: robots.txt eerst, de crawl-delay van de site aanhouden, en
niets ophalen van een kantoor waarvan het advies niet 'lezen' is.
"""
from __future__ import annotations

import argparse
import html as htmlmod
import re
import sys
from urllib.parse import urlparse

import httpx

sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent.parent))

from dh import config, focus  # noqa: E402
from dh.adapters.makelaars import Site, laad_kantoren  # noqa: E402
from dh.store import Store  # noqa: E402

OG = re.compile(r'<meta[^>]+property=["\']og:image["\'][^>]+content=["\']([^"\']+)["\']', re.I)
OG2 = re.compile(r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+property=["\']og:image["\']', re.I)


def eerste_foto(t: str, basis: str) -> str | None:
    for pat in (OG, OG2):
        m = pat.search(t)
        if m:
            u = htmlmod.unescape(m.group(1)).strip()
            if u.startswith("//"):
                u = "https:" + u
            if u.startswith("http"):
                return u
    return None


def run(limit: int = 0) -> dict:
    store = Store()
    kantoren = {k.host: k for k in laad_kantoren()}
    rijen = [r for r in focus.rijen(store)
             if str(r["source"]).startswith("makelaar:") and not (r["image_url"] or "").strip() and r["url"]]
    if limit:
        rijen = rijen[:limit]
    per_host: dict[str, list] = {}
    for r in rijen:
        per_host.setdefault(str(r["source"]).split(":", 1)[1], []).append(r)
    telling = {"te_doen": len(rijen), "gevonden": 0, "geen": 0, "overgeslagen": 0, "sites": 0}
    with httpx.Client(timeout=config.HTTP_TIMEOUT, follow_redirects=True,
                      headers={"User-Agent": config.USER_AGENT}) as client:
        for host, lijst in per_host.items():
            k = kantoren.get(host)
            if not k or k.advies != "lezen":
                telling["overgeslagen"] += len(lijst)
                continue
            telling["sites"] += 1
            site = Site(k, client)
            for r in lijst:
                u = str(r["url"] or "")
                if urlparse(u).netloc.lower().replace("www.", "") != host:
                    telling["overgeslagen"] += 1
                    continue
                t = site.haal(u)
                foto = eerste_foto(t, u) if t else None
                if foto:
                    store.con.execute("UPDATE listings SET image_url=? WHERE id=?", (foto, int(r["id"])))
                    store.con.commit()      # meteen vastleggen: een lange transactie zet de
                    telling["gevonden"] += 1  # database op slot voor de webdienst
                else:
                    telling["geen"] += 1
            store.con.commit()
            print(f"  {host}: {telling['gevonden']} foto's tot nu toe", flush=True)
    store.con.commit()
    store.close()
    return telling


if __name__ == "__main__":
    a = argparse.ArgumentParser(description="Eerste foto ophalen voor objecten die er nog geen hebben")
    a.add_argument("--limit", type=int, default=0)
    print(run(a.parse_args().limit))

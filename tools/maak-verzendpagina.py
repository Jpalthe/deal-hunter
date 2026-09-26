#!/usr/bin/env python3
"""Bouwt acties/feed-aanvraag/versturen.html opnieuw uit de conceptmails ernaast.

De pagina was met de hand gemaakt, dus een kantoor erbij betekende honderd kilobyte HTML
bijwerken. Dit leest elk .md-bestand in die map en zet de kaartjes en de gegevensregel opnieuw.
De vormgeving en het script van de pagina blijven onaangeroerd: alleen het stuk tussen het eerste
<article> en het laatste </article>, plus de regel `const MAILS = [...]`, wordt vervangen.

  python tools/maak-verzendpagina.py
"""
from __future__ import annotations

import html
import json
import re
import sys
from pathlib import Path

MAP = Path(__file__).resolve().parent.parent / "acties" / "feed-aanvraag"
PAGINA = MAP / "versturen.html"

KAARTJE = """<article class="m" data-i="{i}">
  <header><h2>{naam}</h2>
    <a href="{web}" target="_blank" rel="noopener noreferrer">site openen ↗</a></header>
  <label>E-mailadres van het kantoor
    <input type="email" class="adres" placeholder="staat op hun contactpagina"></label>
  <div class="knoppen">
    <button class="kopieer">Tekst kopiëren</button>
    <button class="open">Openen in Mail</button>
    <button class="klaar">Verstuurd</button>
  </div>
  <details><summary>De tekst lezen</summary><pre class="body">{body}</pre></details>
  <p class="st"></p>
</article>"""


def lees(p: Path) -> dict | None:
    t = p.read_text(encoding="utf-8")
    naam = re.search(r"^#\s*Feed aanvragen bij\s+(.+)$", t, re.M)
    web = re.search(r"^\*\*Website:\*\*\s*(\S+)", t, re.M)
    onderwerp = re.search(r"^\*\*Onderwerp:\*\*\s*(.+)$", t, re.M)
    if not (naam and web and onderwerp):
        print(f"  overgeslagen (kop, website of onderwerp ontbreekt): {p.name}")
        return None
    # de brief begint bij de eerste scheidingslijn ná het onderwerp
    rest = t[onderwerp.end():]
    m = re.search(r"^---\s*$", rest, re.M)
    if not m:
        print(f"  overgeslagen (geen scheidingslijn na het onderwerp): {p.name}")
        return None
    return {"naam": naam.group(1).strip(), "web": web.group(1).strip(),
            "onderwerp": onderwerp.group(1).strip(), "body": rest[m.end():].strip()}


def main() -> int:
    mails = [m for m in (lees(p) for p in sorted(MAP.glob("*.md")) if p.name != "README.md") if m]
    if not mails:
        print("geen conceptmails gevonden", file=sys.stderr)
        return 1
    pagina = PAGINA.read_text(encoding="utf-8")
    begin, eind = pagina.find("<article class=\"m\""), pagina.rfind("</article>")
    if begin < 0 or eind < 0:
        print("kon de kaartjes niet vinden in versturen.html", file=sys.stderr)
        return 1
    kaartjes = "\n".join(
        KAARTJE.format(i=i, naam=html.escape(m["naam"]), web=html.escape(m["web"]),
                       body=html.escape(m["body"]))
        for i, m in enumerate(mails))
    nieuw = pagina[:begin] + kaartjes + pagina[eind + len("</article>"):]
    # Let op: de vervangtekst gaat als lambda mee. Een gewone string zou door re.sub worden
    # gelezen als sjabloon, en dan wordt elke \\n in de JSON een echte regelovergang — waarmee de
    # gegevensregel ongeldige JavaScript wordt (gebeurd op 27-09-2026).
    regel = "const MAILS = " + json.dumps(mails, ensure_ascii=False) + ";"
    nieuw, aantal = re.subn(r"^const MAILS = \[.*$", lambda _m: regel, nieuw, count=1, flags=re.M)
    if aantal != 1:
        print("de gegevensregel is niet vervangen", file=sys.stderr)
        return 1
    # controle: de gegevensregel moet weer geldige JSON op één regel zijn
    terug = re.search(r"^const MAILS = (\[.*\]);$", nieuw, re.M)
    if not terug or len(json.loads(terug.group(1))) != len(mails):
        print("de gegevensregel is niet leesbaar teruggeschreven", file=sys.stderr)
        return 1
    PAGINA.write_text(nieuw, encoding="utf-8")
    print(f"{len(mails)} kantoren op de pagina, {len(nieuw) // 1024} kB")
    for m in mails:
        print(f"  {m['naam']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Eenmalig: stuur één samenvatting van de meldingen die nooit zijn aangekomen.

Aanleiding (26-09-2026). Tussen 18 en 26 september zijn veertien meldingen
overgeslagen omdat er geen DISCORD_WEBHOOK_URL in `.env` stond. De uitslag werd
per melding netjes vastgelegd — "overgeslagen (geen DISCORD_WEBHOOK_URL)" —
maar niemand las dat ooit terug, en Jan dacht dat er simpelweg geen kansen
waren. Keuze van Jan: één samenvattend bericht, geen veertien losse.

Gebruik:
    python3 tools/gemiste_meldingen.py            # laat alleen zien
    python3 tools/gemiste_meldingen.py --sturen   # stuurt het bericht

Na afloop krijgen de betrokken meldingen een uitslag die zegt dat ze alsnog
in de samenvatting zijn meegegaan, zodat ze niet nóg een keer langskomen.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from dh import alerts, config  # noqa: E402
from dh.store import Store  # noqa: E402
from dh.summary import bouw_ctx, events_since, listing_summary  # noqa: E402

NAGEZONDEN = "discord: alsnog verzonden in de samenvatting van 26-09-2026"


def gemiste_regels(store: Store) -> list[tuple[int, str, str]]:
    """(alert-id, wanneer, categorie) van alles wat nooit is verstuurd."""
    uit = []
    for aid, at, tier, delivered in store.con.execute(
        "SELECT id, at, tier, delivered FROM alerts ORDER BY at"
    ):
        if alerts.is_bezorgd(delivered):
            continue
        if delivered and str(delivered).startswith("nulmeting"):
            continue          # bewust niet verstuurd
        uit.append((aid, at, tier))
    return uit


def main() -> int:
    sturen = "--sturen" in sys.argv
    store = Store()
    try:
        gemist = gemiste_regels(store)
        if not gemist:
            print("Niets gemist — alle meldingen zijn aangekomen.")
            return 0

        ids = [aid for aid, _, _ in gemist]
        plaatsen = ",".join("?" * len(ids))
        rijen = store.con.execute(
            f"SELECT l.* FROM listings l JOIN alerts a ON a.listing_id = l.id "
            f"WHERE a.id IN ({plaatsen})",
            ids,
        ).fetchall()

        ctx = bouw_ctx(store)
        ev7 = events_since(store, 7)
        items, nog_actief = [], 0
        for r in rijen:
            it = listing_summary(store, r, ev7, ctx)
            # 'verdwenen' betekent dat de advertentie weg is; dat is voor Jan
            # het verschil tussen een gemiste kans en een dode kans.
            it["_actief"] = (dict(r).get("status") or "") != "verdwenen"
            nog_actief += 1 if it["_actief"] else 0
            items.append(it)

        items.sort(key=lambda x: (not x["_actief"], -(x.get("room") or 0)))

        kop = (f"📭 **{len(gemist)} meldingen die je nooit hebt gekregen**\n"
               f"Tussen 18 en 26 september is er geen bezorgkanaal ingesteld geweest, "
               f"waardoor deze kansen zijn blijven liggen. Daarvan staan er nog "
               f"**{nog_actief}** te koop.\n")
        regels = [kop]
        for it in items[:20]:
            merk = "" if it["_actief"] else "  _(advertentie is inmiddels weg)_"
            regels.append(alerts.line(it) + merk)
        if len(items) > 20:
            regels.append(f"\n…en nog {len(items) - 20}. Alles staat in de app.")
        bericht = "\n".join(regels)

        if not sturen:
            print(bericht)
            print(f"\n[proef — nog niets verstuurd. Voeg --sturen toe.]")
            return 0

        env = config.load_env()
        uitslag = alerts.bezorg(env, bericht, onderwerp="Deal Hunter — gemiste kansen")
        print("Bezorging:", uitslag)

        if alerts.is_bezorgd(uitslag):
            store.con.executemany(
                "UPDATE alerts SET delivered = ? WHERE id = ?",
                [(NAGEZONDEN, aid) for aid in ids],
            )
            store.con.commit()
            print(f"{len(ids)} meldingen bijgewerkt — ze komen niet opnieuw langs.")
        else:
            print("Niet verstuurd; de meldingen blijven als gemist staan.")
        return 0
    finally:
        store.close()


if __name__ == "__main__":
    raise SystemExit(main())

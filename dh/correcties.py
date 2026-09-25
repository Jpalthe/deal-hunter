"""Handmatig gecontroleerde correcties op wat een bron doorgeeft.

Een advertentie kan er naast zitten en een feed kan een veld leeg laten. Wat hier staat is
nagekeken en gaat voor de bron. Elke correctie draagt haar eigen herkomst mee, zodat in het
dossier te zien is waar het getal vandaan komt en wanneer het is gecontroleerd.

  python -m dh.correcties        toepassen op alles wat in de database staat
"""
from __future__ import annotations

import json
import sys

from . import config
from .store import Store

PAD = config.KADER / "correcties.json"
VELDEN = ("plot_m2", "built_m2", "price", "type", "beds", "baths")


def laden() -> dict:
    try:
        return json.loads(PAD.read_text(encoding="utf-8")).get("per_referentie") or {}
    except (OSError, json.JSONDecodeError):
        return {}


def toepassen(store: Store) -> dict:
    """Zet de gecontroleerde waarden in de database en legt de herkomst vast bij het object."""
    corr = laden()
    stats = {"objecten": 0, "velden": 0, "niet_gevonden": []}
    for ref, c in corr.items():
        rows = store.con.execute("SELECT * FROM listings WHERE source_ref=?", (ref,)).fetchall()
        if not rows:
            stats["niet_gevonden"].append(ref)
            continue
        for r in rows:
            sets, vals, gewijzigd = [], [], {}
            for v in VELDEN:
                if v in c and c[v] is not None and r[v] != c[v]:
                    sets.append(f"{v}=?"); vals.append(c[v])
                    gewijzigd[v] = {"was": r[v], "wordt": c[v]}
            if sets:
                store.con.execute(f"UPDATE listings SET {', '.join(sets)} WHERE id=?", vals + [r["id"]])
                stats["velden"] += len(sets)
            sig = json.loads(r["signals"] or "{}")
            sig["correcties"] = {"gewijzigd": gewijzigd, "bron": c.get("bron"), "let_op": c.get("let_op"),
                                 "uitsluiten": c.get("uitsluiten")}
            extra = [x for x in (c.get("let_op"), c.get("uitsluiten")) if x]
            if extra:
                sig["blockers"] = list(dict.fromkeys((sig.get("blockers") or []) + extra))
            if c.get("uitsluiten"):
                sig["uitgesloten"] = c["uitsluiten"]
                stats["uitgesloten"] = stats.get("uitgesloten", 0) + 1
            store.con.execute("UPDATE listings SET signals=? WHERE id=?",
                              (json.dumps(sig, ensure_ascii=False), r["id"]))
            stats["objecten"] += 1
    store.con.commit()
    return stats


def main() -> int:
    store = Store()
    try:
        print(json.dumps(toepassen(store), ensure_ascii=False, indent=1))
    finally:
        store.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())

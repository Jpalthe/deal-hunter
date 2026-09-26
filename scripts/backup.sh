#!/bin/bash
# Nachtelijke back-up van de Deal Hunter-database.
# SQLite's eigen backup-opdracht, want een kale cp van een draaiende database geeft een halve kopie.
# Bewaart 14 nachten; ouder gaat weg.
set -euo pipefail
export PATH="$HOME/.local/bin:/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin"
MAP="$HOME/tree-es/deal-hunter"
UIT="$MAP/data/backups"
mkdir -p "$UIT"
"$HOME/.hermes/hermes-agent/venv/bin/python" - <<'PY'
import sqlite3, pathlib, datetime, os
map_ = pathlib.Path(os.environ["HOME"]) / "tree-es" / "deal-hunter"
uit = map_ / "data" / "backups" / f"dealhunter-{datetime.datetime.now():%Y%m%d-%H%M}.sqlite"
bron = sqlite3.connect(str(map_ / "data" / "dealhunter.sqlite"))
doel = sqlite3.connect(str(uit))
with doel:
    bron.backup(doel)
doel.close(); bron.close()
print(f"back-up: {uit.name} ({uit.stat().st_size // 1024} kB)")
PY
# retentie: veertien nachten
ls -1t "$UIT"/dealhunter-*.sqlite 2>/dev/null | tail -n +15 | while read -r oud; do rm -f "$oud"; done

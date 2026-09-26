"""SQLite-opslag van de Deal Hunter (variant 1, geen installaties).

Entiteiten (masterprompt §11): advertentie (listings), momentopname (snapshots),
gebeurtenis (events), veiling (auctions), run (runs), bronstatus (sources),
beoordeling door Jan (reviews), AI-verbruik (ai_usage).
"""
from __future__ import annotations

import hashlib
import json
import sqlite3
from datetime import datetime, timedelta
from pathlib import Path

from . import config

SCHEMA = """
CREATE TABLE IF NOT EXISTS runs (
  id INTEGER PRIMARY KEY, slot TEXT, started_at TEXT NOT NULL, finished_at TEXT,
  status TEXT, baseline INTEGER DEFAULT 0, notes TEXT
);
CREATE TABLE IF NOT EXISTS sources (
  key TEXT PRIMARY KEY, last_success_at TEXT, last_attempt_at TEXT, last_status TEXT,
  last_count INTEGER, last_error TEXT
);
CREATE TABLE IF NOT EXISTS listings (
  id INTEGER PRIMARY KEY, source TEXT NOT NULL, source_ref TEXT NOT NULL,
  area TEXT, town TEXT, town_raw TEXT, postcode TEXT, type TEXT, price REAL, currency TEXT,
  built_m2 REAL, plot_m2 REAL, beds INTEGER, baths INTEGER, lat REAL, lon REAL,
  location_detail TEXT, url TEXT, title TEXT, desc_hash TEXT, desc_excerpt TEXT,
  features TEXT, images_count INTEGER, source_date TEXT, new_build INTEGER,
  first_seen_at TEXT, last_seen_at TEXT, last_fetch_at TEXT, gone_at TEXT,
  signals TEXT, category TEXT, prefilter TEXT, ai TEXT,
  UNIQUE(source, source_ref)
);
CREATE INDEX IF NOT EXISTS ix_listings_area ON listings(area, gone_at);
CREATE TABLE IF NOT EXISTS snapshots (
  id INTEGER PRIMARY KEY, listing_id INTEGER NOT NULL, run_id INTEGER NOT NULL,
  seen_at TEXT NOT NULL, price REAL, fields_hash TEXT
);
CREATE INDEX IF NOT EXISTS ix_snapshots_listing ON snapshots(listing_id, seen_at);
CREATE TABLE IF NOT EXISTS events (
  id INTEGER PRIMARY KEY, run_id INTEGER, listing_id INTEGER, auction_id INTEGER,
  kind TEXT NOT NULL, at TEXT NOT NULL, details TEXT
);
CREATE INDEX IF NOT EXISTS ix_events_run ON events(run_id, kind);
CREATE TABLE IF NOT EXISTS auctions (
  id INTEGER PRIMARY KEY, source TEXT NOT NULL, source_ref TEXT NOT NULL,
  sub_ids TEXT, boe_id TEXT, title TEXT, department TEXT, area TEXT, town TEXT, postcode TEXT,
  address TEXT, ref_catastral TEXT, cru TEXT, tipo TEXT, valuation REAL, cargas REAL,
  derecho TEXT, pct REAL, end_date TEXT, lat REAL, lon REAL, url TEXT, blockers TEXT,
  first_seen_at TEXT, last_seen_at TEXT, gone_at TEXT, raw TEXT,
  UNIQUE(source, source_ref)
);
CREATE TABLE IF NOT EXISTS reviews (
  id INTEGER PRIMARY KEY, listing_id INTEGER, auction_id INTEGER, verdict TEXT NOT NULL,
  note TEXT, by TEXT, at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS parcels (
  listing_id INTEGER PRIMARY KEY, rc TEXT, distance_m REAL, address TEXT, use_text TEXT,
  built_m2 REAL, plot_m2 REAL, year INTEGER, geojson TEXT, nearby TEXT,
  warnings TEXT, mismatches TEXT, fetched_at TEXT, error TEXT
);
CREATE INDEX IF NOT EXISTS ix_parcels_rc ON parcels(rc);
CREATE TABLE IF NOT EXISTS companies (
  id INTEGER PRIMARY KEY, source TEXT NOT NULL, source_ref TEXT NOT NULL,
  name TEXT, registry_no TEXT, acts TEXT, sector TEXT, place TEXT, area TEXT,
  priority INTEGER, borme_id TEXT, url TEXT, published_on TEXT,
  first_seen_at TEXT, last_seen_at TEXT,
  UNIQUE(source, source_ref)
);
CREATE INDEX IF NOT EXISTS ix_companies_pub ON companies(published_on);
CREATE TABLE IF NOT EXISTS alerts (
  id INTEGER PRIMARY KEY, listing_id INTEGER NOT NULL, tier TEXT NOT NULL, class TEXT,
  price REAL, max_price REAL, room REAL, at TEXT NOT NULL, delivered TEXT, run_id INTEGER
);
CREATE INDEX IF NOT EXISTS ix_alerts_listing ON alerts(listing_id, at);
CREATE TABLE IF NOT EXISTS markeringen (
  listing_id INTEGER PRIMARY KEY,
  merk TEXT NOT NULL,
  notitie TEXT,
  volgende_stap TEXT,          -- datum waarop Jan eraan herinnerd wil worden (JJJJ-MM-DD)
  herinnerd_at TEXT,           -- wanneer de herinnering is verstuurd, zodat het maar één keer gebeurt
  at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS zonewaarde (
  -- Het gemiddelde werkelijk betaalde prijspeil van de kadastrale waardezone waarin dit object
  -- ligt. Eén rij per advertentie met een coördinaat, ook als er niets te koppelen viel: dan staat
  -- in `reden` waarom, zodat "niet gekoppeld" te onderscheiden is van "nog niet gekeken".
  listing_id INTEGER PRIMARY KEY, gemeente TEXT, gemeente_naam TEXT,
  zona_valor TEXT, cod_zona TEXT, ejercicio INTEGER, num_inmuebles INTEGER,
  tipologia TEXT, categoria TEXT, antiguedad INTEGER, conservacion TEXT,
  superficie REAL, superficie_suelo REAL,
  val_tipo REAL, val_tipo_m2 REAL, val_estandar_m2 REAL,
  overlap INTEGER, reden TEXT, at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS ai_usage (
  id INTEGER PRIMARY KEY, run_id INTEGER, model TEXT, input_tokens INTEGER, output_tokens INTEGER,
  cost_eur REAL, at TEXT NOT NULL
);
"""

LISTING_FIELDS = [
    "area", "town", "town_raw", "postcode", "type", "price", "currency", "built_m2", "plot_m2", "beds", "baths",
    "lat", "lon", "location_detail", "url", "title", "desc_hash", "desc_excerpt", "features", "images_count",
    "source_date", "new_build",
]
# Velden waarvan een wijziging telt als 'materieel' (masterprompt §10)
MATERIAL_FIELDS = ["price", "built_m2", "plot_m2", "type", "town", "desc_hash"]


def now_iso() -> str:
    return datetime.now(config.TZ).isoformat(timespec="seconds")


def fields_hash(d: dict) -> str:
    key = "|".join(str(d.get(k, "")) for k in MATERIAL_FIELDS)
    return hashlib.sha256(key.encode("utf-8")).hexdigest()[:16]


class Store:
    def __init__(self, path: Path | None = None):
        self.path = Path(path or config.DB_PATH)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.con = sqlite3.connect(str(self.path))
        self.con.row_factory = sqlite3.Row
        self.con.execute("PRAGMA journal_mode=WAL")
        # Twee processen schrijven hier tegelijk: de ronde en de webdienst. Zonder wachttijd geeft
        # SQLite meteen "database is locked" en verliest de gebruiker zijn tik op een knop.
        self.con.execute("PRAGMA busy_timeout=15000")
        self.con.execute("PRAGMA foreign_keys=ON")
        self.con.executescript(SCHEMA)
        self._migreer()

    def _migreer(self) -> None:
        """Kolommen die later zijn bijgekomen. Ontbreekt er één, dan wordt hij toegevoegd."""
        for tabel, kolom, soort in (("listings", "image_url", "TEXT"),
                                    ("markeringen", "volgende_stap", "TEXT"),
                                    ("markeringen", "herinnerd_at", "TEXT")):
            heeft = any(r[1] == kolom for r in self.con.execute(f"PRAGMA table_info({tabel})"))
            if not heeft:
                self.con.execute(f"ALTER TABLE {tabel} ADD COLUMN {kolom} {soort}")
        self.con.commit()

    # ---- runs
    def start_run(self, slot: str) -> int:
        baseline = 1 if self.count_listings() == 0 else 0
        cur = self.con.execute("INSERT INTO runs(slot, started_at, status, baseline) VALUES (?,?,?,?)",
                               (slot, now_iso(), "running", baseline))
        self.con.commit()
        return int(cur.lastrowid)

    def finish_run(self, run_id: int, status: str, notes: dict | None = None) -> None:
        self.con.execute("UPDATE runs SET finished_at=?, status=?, notes=? WHERE id=?",
                         (now_iso(), status, json.dumps(notes or {}, ensure_ascii=False), run_id))
        self.con.commit()

    def is_baseline(self, run_id: int) -> bool:
        r = self.con.execute("SELECT baseline FROM runs WHERE id=?", (run_id,)).fetchone()
        return bool(r and r["baseline"])

    # ---- sources
    def source_status(self, key: str, ok: bool, count: int | None = None, error: str | None = None) -> None:
        t = now_iso()
        self.con.execute(
            "INSERT INTO sources(key, last_attempt_at, last_status, last_count, last_error, last_success_at) VALUES (?,?,?,?,?,?) "
            "ON CONFLICT(key) DO UPDATE SET last_attempt_at=excluded.last_attempt_at, last_status=excluded.last_status, "
            "last_error=excluded.last_error, last_count=COALESCE(excluded.last_count, sources.last_count), "
            "last_success_at=COALESCE(excluded.last_success_at, sources.last_success_at)",
            (key, t, "ok" if ok else "fout", count, error, t if ok else None))
        self.con.commit()

    def source(self, key: str) -> sqlite3.Row | None:
        return self.con.execute("SELECT * FROM sources WHERE key=?", (key,)).fetchone()

    # ---- listings
    def count_listings(self, source: str | None = None, active_only: bool = True) -> int:
        q = "SELECT COUNT(*) FROM listings WHERE 1=1"
        args: list = []
        if source:
            q += " AND source=?"; args.append(source)
        if active_only:
            q += " AND gone_at IS NULL"
        return int(self.con.execute(q, args).fetchone()[0])

    def get_listing(self, source: str, ref: str) -> sqlite3.Row | None:
        return self.con.execute("SELECT * FROM listings WHERE source=? AND source_ref=?", (source, ref)).fetchone()

    def upsert_listing(self, run_id: int, source: str, rec: dict) -> tuple[int, str, dict]:
        """Slaat een advertentie op. Geeft (listing_id, gebeurtenis, details) terug.
        Gebeurtenis: 'NIEUW' | 'PRIJS GEWIJZIGD' | 'GEWIJZIGD' | 'ONGEWIJZIGD' | 'OPNIEUW AANGEBODEN'."""
        t = now_iso()
        ref = str(rec["source_ref"])
        vals = {k: rec.get(k) for k in LISTING_FIELDS}
        vals["features"] = json.dumps(vals.get("features") or [], ensure_ascii=False) if not isinstance(vals.get("features"), str) else vals["features"]
        h = fields_hash(vals)
        row = self.get_listing(source, ref)
        details: dict = {}
        if row is None:
            cols = ["source", "source_ref"] + LISTING_FIELDS + ["first_seen_at", "last_seen_at", "last_fetch_at"]
            self.con.execute(f"INSERT INTO listings({','.join(cols)}) VALUES ({','.join('?' * len(cols))})",
                             [source, ref] + [vals[k] for k in LISTING_FIELDS] + [t, t, t])
            lid = int(self.con.execute("SELECT id FROM listings WHERE source=? AND source_ref=?", (source, ref)).fetchone()[0])
            kind = "NIEUW"
        else:
            lid = int(row["id"])
            old_price = row["price"]
            was_gone = row["gone_at"] is not None
            old_hash = None
            last = self.con.execute("SELECT fields_hash, price FROM snapshots WHERE listing_id=? ORDER BY id DESC LIMIT 1", (lid,)).fetchone()
            if last:
                old_hash = last["fields_hash"]
            sets = ", ".join(f"{k}=?" for k in LISTING_FIELDS)
            self.con.execute(f"UPDATE listings SET {sets}, last_seen_at=?, last_fetch_at=?, gone_at=NULL WHERE id=?",
                             [vals[k] for k in LISTING_FIELDS] + [t, t, lid])
            if was_gone:
                kind = "OPNIEUW AANGEBODEN"
                details = {"gone_at": row["gone_at"]}
            elif old_price is not None and vals["price"] is not None and float(old_price) != float(vals["price"]):
                kind = "PRIJS GEWIJZIGD"
                details = {"van": old_price, "naar": vals["price"],
                           "pct": round((float(vals["price"]) - float(old_price)) / float(old_price) * 100, 1) if old_price else None}
            elif old_hash and old_hash != h:
                kind = "GEWIJZIGD"
            else:
                kind = "ONGEWIJZIGD"
        if rec.get("image_url"):
            self.con.execute("UPDATE listings SET image_url=? WHERE id=?", (rec["image_url"], lid))
        self.con.execute("INSERT INTO snapshots(listing_id, run_id, seen_at, price, fields_hash) VALUES (?,?,?,?,?)",
                         (lid, run_id, t, vals["price"], h))
        if kind != "ONGEWIJZIGD":
            ev = "NULMETING" if (kind == "NIEUW" and self.is_baseline(run_id)) else kind
            self.add_event(run_id, ev, listing_id=lid, details=details)
            kind = ev
        return lid, kind, details

    def mark_gone(self, run_id: int, source: str, seen_refs: set[str]) -> list[int]:
        """Markeert advertenties van deze bron die niet in de huidige momentopname zitten."""
        rows = self.con.execute("SELECT id, source_ref FROM listings WHERE source=? AND gone_at IS NULL", (source,)).fetchall()
        gone = [int(r["id"]) for r in rows if r["source_ref"] not in seen_refs]
        t = now_iso()
        for lid in gone:
            self.con.execute("UPDATE listings SET gone_at=? WHERE id=?", (t, lid))
            self.add_event(run_id, "NIET MEER GEVONDEN", listing_id=lid, details={"let_op": "niet gelijk aan verkocht"})
        self.con.commit()
        return gone

    def set_analysis(self, lid: int, signals: dict | None = None, category: str | None = None,
                     prefilter: dict | None = None, ai: dict | None = None) -> None:
        if signals is not None:
            self.con.execute("UPDATE listings SET signals=? WHERE id=?", (json.dumps(signals, ensure_ascii=False), lid))
        if category is not None:
            self.con.execute("UPDATE listings SET category=? WHERE id=?", (category, lid))
        if prefilter is not None:
            self.con.execute("UPDATE listings SET prefilter=? WHERE id=?", (json.dumps(prefilter, ensure_ascii=False), lid))
        if ai is not None:
            self.con.execute("UPDATE listings SET ai=? WHERE id=?", (json.dumps(ai, ensure_ascii=False), lid))
        self.con.commit()

    def price_history(self, lid: int) -> list[tuple[str, float | None]]:
        rows = self.con.execute("SELECT seen_at, price FROM snapshots WHERE listing_id=? ORDER BY id", (lid,)).fetchall()
        out: list[tuple[str, float | None]] = []
        for r in rows:
            if not out or out[-1][1] != r["price"]:
                out.append((r["seen_at"], r["price"]))
        return out

    # ---- events
    def add_event(self, run_id: int, kind: str, listing_id: int | None = None, auction_id: int | None = None,
                  details: dict | None = None) -> None:
        self.con.execute("INSERT INTO events(run_id, listing_id, auction_id, kind, at, details) VALUES (?,?,?,?,?,?)",
                         (run_id, listing_id, auction_id, kind, now_iso(), json.dumps(details or {}, ensure_ascii=False)))

    def events_for_run(self, run_id: int) -> list[sqlite3.Row]:
        return self.con.execute("SELECT * FROM events WHERE run_id=? ORDER BY id", (run_id,)).fetchall()

    # ---- auctions
    def upsert_auction(self, run_id: int, source: str, rec: dict) -> tuple[int, str]:
        t = now_iso()
        ref = str(rec["source_ref"])
        row = self.con.execute("SELECT * FROM auctions WHERE source=? AND source_ref=?", (source, ref)).fetchone()
        cols = ["sub_ids", "boe_id", "title", "department", "area", "town", "postcode", "address", "ref_catastral", "cru",
                "tipo", "valuation", "cargas", "derecho", "pct", "end_date", "lat", "lon", "url", "blockers", "raw"]
        vals = []
        for c in cols:
            v = rec.get(c)
            if c in ("sub_ids", "blockers", "raw") and not isinstance(v, str) and v is not None:
                v = json.dumps(v, ensure_ascii=False)
            vals.append(v)
        if row is None:
            self.con.execute(f"INSERT INTO auctions(source, source_ref, {','.join(cols)}, first_seen_at, last_seen_at) "
                             f"VALUES (?,?,{','.join('?' * len(cols))},?,?)", [source, ref] + vals + [t, t])
            aid = int(self.con.execute("SELECT id FROM auctions WHERE source=? AND source_ref=?", (source, ref)).fetchone()[0])
            kind = "NULMETING" if self.is_baseline(run_id) else "NIEUW GEPUBLICEERD"
            self.add_event(run_id, kind, auction_id=aid, details={"bron": source})
        else:
            aid = int(row["id"])
            sets = ", ".join(f"{c}=?" for c in cols)
            self.con.execute(f"UPDATE auctions SET {sets}, last_seen_at=?, gone_at=NULL WHERE id=?", vals + [t, aid])
            kind = "ONGEWIJZIGD"
            if row["gone_at"]:
                kind = "OPNIEUW AANGEBODEN"; self.add_event(run_id, kind, auction_id=aid)
            elif row["valuation"] is not None and rec.get("valuation") is not None and float(row["valuation"]) != float(rec["valuation"]):
                kind = "STATUS GEWIJZIGD"; self.add_event(run_id, kind, auction_id=aid, details={"valuation_van": row["valuation"], "naar": rec.get("valuation")})
        self.con.commit()
        return aid, kind

    def mark_auctions_gone(self, run_id: int, source: str, seen_refs: set[str]) -> list[int]:
        rows = self.con.execute("SELECT id, source_ref FROM auctions WHERE source=? AND gone_at IS NULL", (source,)).fetchall()
        gone = [int(r["id"]) for r in rows if r["source_ref"] not in seen_refs]
        t = now_iso()
        for aid in gone:
            self.con.execute("UPDATE auctions SET gone_at=? WHERE id=?", (t, aid))
            self.add_event(run_id, "NIET MEER GEVONDEN", auction_id=aid, details={"let_op": "verdwenen uit de lijst, niet gelijk aan gegund"})
        self.con.commit()
        return gone

    # ---- percelen (kadaster)
    def save_parcel(self, listing_id: int, e: dict, mismatches: list[str]) -> None:
        d = e.get("detail") or {}
        g = e.get("geometry") or {}
        self.con.execute(
            "INSERT INTO parcels(listing_id, rc, distance_m, address, use_text, built_m2, plot_m2, year, geojson, "
            "nearby, warnings, mismatches, fetched_at, error) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?) "
            "ON CONFLICT(listing_id) DO UPDATE SET rc=excluded.rc, distance_m=excluded.distance_m, address=excluded.address, "
            "use_text=excluded.use_text, built_m2=excluded.built_m2, plot_m2=excluded.plot_m2, year=excluded.year, "
            "geojson=excluded.geojson, nearby=excluded.nearby, warnings=excluded.warnings, mismatches=excluded.mismatches, "
            "fetched_at=excluded.fetched_at, error=excluded.error",
            (listing_id, e.get("rc"), e.get("distance_m"), d.get("address"), d.get("use"),
             d.get("built_m2"), g.get("area_m2"), d.get("year"),
             json.dumps(g.get("geojson"), ensure_ascii=False) if g.get("geojson") else None,
             json.dumps(e.get("nearby") or [], ensure_ascii=False),
             json.dumps(e.get("warnings") or [], ensure_ascii=False),
             json.dumps(mismatches or [], ensure_ascii=False),
             now_iso(), e.get("error") or d.get("error") or g.get("error")))
        self.con.commit()

    def parcel(self, listing_id: int) -> sqlite3.Row | None:
        return self.con.execute("SELECT * FROM parcels WHERE listing_id=?", (listing_id,)).fetchone()

    def parcels_missing(self, limit: int = 500) -> list[sqlite3.Row]:
        """Actieve objecten met coördinaten waarvoor nog geen perceel is opgehaald."""
        return self.con.execute(
            "SELECT l.* FROM listings l LEFT JOIN parcels p ON p.listing_id = l.id "
            "WHERE l.gone_at IS NULL AND l.area IS NOT NULL AND l.lat IS NOT NULL "
            "AND (p.listing_id IS NULL OR (p.rc IS NULL AND p.error IS NOT NULL)) LIMIT ?", (limit,)).fetchall()

    # ---- vennootschapssignalen (BORME)
    def upsert_company(self, run_id: int, source: str, rec: dict) -> tuple[int, str]:
        """Slaat één vennootschapssignaal op. Nooit de tekst van de aankondiging (persoonsgegevens)."""
        t = now_iso()
        ref = str(rec["source_ref"])
        row = self.con.execute("SELECT id FROM companies WHERE source=? AND source_ref=?", (source, ref)).fetchone()
        cols = ["name", "registry_no", "acts", "sector", "place", "area", "priority", "borme_id", "url", "published_on"]
        vals = [json.dumps(rec.get(c), ensure_ascii=False) if c == "acts" else rec.get(c) for c in cols]
        if row is None:
            self.con.execute(f"INSERT INTO companies(source, source_ref, {','.join(cols)}, first_seen_at, last_seen_at) "
                             f"VALUES (?,?,{','.join('?' * len(cols))},?,?)", [source, ref] + vals + [t, t])
            cid = int(self.con.execute("SELECT id FROM companies WHERE source=? AND source_ref=?", (source, ref)).fetchone()[0])
            self.add_event(run_id, "VENNOOTSCHAP IN MOEILIJKHEDEN",
                           details={"bron": source, "naam": rec.get("name"), "handelingen": rec.get("acts"),
                                    "plaats": rec.get("place"), "prioriteit": rec.get("priority")})
            self.con.commit()
            return cid, "NIEUW"
        cid = int(row["id"])
        self.con.execute("UPDATE companies SET last_seen_at=? WHERE id=?", (t, cid))
        self.con.commit()
        return cid, "ONGEWIJZIGD"

    def recent_companies(self, days: int = 30, limit: int = 100) -> list[sqlite3.Row]:
        since = (datetime.now(config.TZ) - timedelta(days=days)).date().isoformat()
        return self.con.execute(
            "SELECT * FROM companies WHERE published_on >= ? ORDER BY priority DESC, published_on DESC LIMIT ?",
            (since, limit)).fetchall()

    # ---- meldingen bij sterke kansen
    def last_alert(self, listing_id: int) -> sqlite3.Row | None:
        return self.con.execute("SELECT * FROM alerts WHERE listing_id=? ORDER BY id DESC LIMIT 1", (listing_id,)).fetchone()

    def add_alert(self, run_id: int, listing_id: int, tier: str, cls: str, price: float | None,
                  max_price: float | None, room: float | None, delivered: str = "") -> int:
        cur = self.con.execute(
            "INSERT INTO alerts(listing_id, tier, class, price, max_price, room, at, delivered, run_id) VALUES (?,?,?,?,?,?,?,?,?)",
            (listing_id, tier, cls, price, max_price, room, now_iso(), delivered, run_id))
        self.con.commit()
        return int(cur.lastrowid)

    def alerts_since(self, days: int = 14) -> list[sqlite3.Row]:
        since = (datetime.now(config.TZ) - timedelta(days=days)).isoformat(timespec="seconds")
        return self.con.execute("SELECT * FROM alerts WHERE at >= ? ORDER BY id DESC", (since,)).fetchall()

    def active_auctions(self) -> list[sqlite3.Row]:
        return self.con.execute("SELECT * FROM auctions WHERE gone_at IS NULL ORDER BY end_date").fetchall()

    # ---- queries voor het rapport
    def listings_by_ids(self, ids: list[int]) -> list[sqlite3.Row]:
        if not ids:
            return []
        q = f"SELECT * FROM listings WHERE id IN ({','.join('?' * len(ids))})"
        return self.con.execute(q, ids).fetchall()

    def active_listings(self, area_only: bool = True) -> list[sqlite3.Row]:
        q = "SELECT * FROM listings WHERE gone_at IS NULL"
        if area_only:
            q += " AND area IS NOT NULL"
        return self.con.execute(q + " ORDER BY area, price").fetchall()

    def ai_cost_month(self) -> float:
        ym = datetime.now(config.TZ).strftime("%Y-%m")
        r = self.con.execute("SELECT COALESCE(SUM(cost_eur),0) FROM ai_usage WHERE substr(at,1,7)=?", (ym,)).fetchone()
        return float(r[0])

    def add_ai_usage(self, run_id: int, model: str, inp: int, out: int, cost_eur: float) -> None:
        self.con.execute("INSERT INTO ai_usage(run_id, model, input_tokens, output_tokens, cost_eur, at) VALUES (?,?,?,?,?,?)",
                         (run_id, model, inp, out, cost_eur, now_iso()))
        self.con.commit()

    def add_review(self, verdict: str, note: str = "", by: str = "Jan", listing_id: int | None = None, auction_id: int | None = None) -> None:
        self.con.execute("INSERT INTO reviews(listing_id, auction_id, verdict, note, by, at) VALUES (?,?,?,?,?,?)",
                         (listing_id, auction_id, verdict, note, by, now_iso()))
        self.con.commit()

    def latest_review(self, listing_id: int | None = None, auction_id: int | None = None) -> sqlite3.Row | None:
        if listing_id:
            return self.con.execute("SELECT * FROM reviews WHERE listing_id=? ORDER BY id DESC LIMIT 1", (listing_id,)).fetchone()
        return self.con.execute("SELECT * FROM reviews WHERE auction_id=? ORDER BY id DESC LIMIT 1", (auction_id,)).fetchone()

    # ---- markeringen: boeiend, weg, gebeld (Jan 25-09-2026)
    # Jan 26-09-2026: na gebeld komt er nog één stand bij. Wat hij koopt verlaat deze app.
    MERKEN = ("boeiend", "gebeld", "bod", "weg")

    def markeer(self, listing_id: int, merk: str, notitie: str | None = None,
                volgende_stap: str | None = None) -> None:
        """Zet of wist een merkje, met een notitie en een datum om aan herinnerd te worden.

        Notitie en datum worden alleen overschreven als ze zijn meegegeven; zo kun je een merkje
        wijzigen zonder wat je eerder opschreef kwijt te raken."""
        if merk in ("geen", "", None):
            self.con.execute("DELETE FROM markeringen WHERE listing_id=?", (listing_id,))
            self.con.commit()
            return
        if merk not in self.MERKEN:
            raise ValueError(f"onbekend merk: {merk}")
        if volgende_stap:
            import re as _re
            if not _re.fullmatch(r"\d{4}-\d{2}-\d{2}", volgende_stap):
                raise ValueError("de datum moet als JJJJ-MM-DD worden gegeven")
        self.con.execute(
            """INSERT INTO markeringen(listing_id, merk, notitie, volgende_stap, at)
               VALUES (?,?,?,?,?)
               ON CONFLICT(listing_id) DO UPDATE SET
                 merk=excluded.merk,
                 notitie=COALESCE(excluded.notitie, markeringen.notitie),
                 volgende_stap=COALESCE(excluded.volgende_stap, markeringen.volgende_stap),
                 herinnerd_at=CASE WHEN excluded.volgende_stap IS NOT NULL
                                   THEN NULL ELSE markeringen.herinnerd_at END,
                 at=excluded.at""",
            (listing_id, merk, notitie, volgende_stap, now_iso()))
        self.con.commit()

    def markeringen(self) -> dict[int, dict]:
        return {int(r["listing_id"]): {"merk": r["merk"], "notitie": r["notitie"],
                                       "volgende_stap": r["volgende_stap"], "at": r["at"]}
                for r in self.con.execute("SELECT * FROM markeringen")}

    def herinneringen(self, op: str) -> list[dict]:
        """Wie er vandaag of eerder teruggebeld moet worden en nog niet is herinnerd."""
        return [dict(r) for r in self.con.execute(
            """SELECT m.listing_id, m.merk, m.notitie, m.volgende_stap, l.source_ref, l.price,
                      l.title, l.url
               FROM markeringen m JOIN listings l ON l.id = m.listing_id
               WHERE m.volgende_stap IS NOT NULL AND m.volgende_stap <= ?
                 AND m.herinnerd_at IS NULL AND m.merk <> 'weg'
               ORDER BY m.volgende_stap""", (op,))]

    def herinnering_verstuurd(self, ids: list[int]) -> None:
        for i in ids:
            self.con.execute("UPDATE markeringen SET herinnerd_at=? WHERE listing_id=?", (now_iso(), i))
        self.con.commit()

    def close(self) -> None:
        self.con.commit()
        self.con.close()

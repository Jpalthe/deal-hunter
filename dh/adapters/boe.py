"""Adapter BOE-sumario (open data, hergebruiklicentie AEBOE 27-06-2024).

Leest per dag het sumario (JSON), selecteert in Sección IV (Administración de Justicia) en
V-B (Otros anuncios oficiales) de items die op veilingen in ons gebied kunnen wijzen, en haalt
per geselecteerd item één keer de aankondigingstekst op om alleen de SUB-id's en het orgaan
te lezen. De tekst zelf wordt niet opgeslagen (persoonsgegevens, deliverable 04 §2.10).
Let op (deliverable 04): een BOE-aankondiging noemt nooit de plaats van het goed; een treffer
op "DENIA" is het orgaan, niet de ligging. Bevestiging alleen via portaalalert of handmatig.
"""
from __future__ import annotations

import html
import re
import time
from datetime import date, datetime, timedelta

import httpx

from .. import config

SUB_RE = re.compile(r"SUB-[A-Z]{2}-\d{4}-[A-Z0-9]+")
PRIORITY_TITLE = re.compile(r"\bD[EÉ]NIA\b", re.I)
SECONDARY_TITLE = re.compile(r"ALICANTE|ALACANT|VAL[EÈ]NCIA|SUMA GESTI[OÓ]N|AGENCIA (ESTATAL DE ADMINISTRACI[OÓ]N )?TRIBUTARIA|TESORER[IÍ]A GENERAL|SUBASTA", re.I)


def _items_of(dep: dict) -> list[dict]:
    out: list[dict] = []
    it = dep.get("item")
    if isinstance(it, list):
        out.extend(it)
    elif isinstance(it, dict):
        out.append(it)
    texto = dep.get("texto")
    if isinstance(texto, dict):
        ep = texto.get("epigrafe")
        eps = ep if isinstance(ep, list) else ([ep] if isinstance(ep, dict) else [])
        for e in eps:
            it2 = e.get("item")
            if isinstance(it2, list):
                out.extend(it2)
            elif isinstance(it2, dict):
                out.append(it2)
    return out


def parse_sumario(j: dict) -> list[dict]:
    """Geeft kandidaat-items terug met sectie, departement, id, titel, url en prioriteit."""
    out: list[dict] = []
    try:
        diarios = j["data"]["sumario"]["diario"]
    except (KeyError, TypeError):
        return out
    for diario in diarios:
        for sec in diario.get("seccion", []) or []:
            code = str(sec.get("codigo"))
            if code not in config.BOE_SECTIONS:
                continue
            deps = sec.get("departamento")
            deps = deps if isinstance(deps, list) else ([deps] if isinstance(deps, dict) else [])
            for dep in deps:
                dname = str(dep.get("nombre") or "")
                for it in _items_of(dep):
                    title = str(it.get("titulo") or "")
                    prio = 0
                    if code == "4":
                        if PRIORITY_TITLE.search(title):
                            prio = 2
                        elif SECONDARY_TITLE.search(title):
                            prio = 1
                    else:  # 5B
                        if SECONDARY_TITLE.search(title) or SECONDARY_TITLE.search(dname):
                            prio = 2 if re.search(r"SUMA|D[EÉ]NIA|ALICANTE|ALACANT", title + " " + dname, re.I) else 1
                    if prio == 0:
                        continue
                    out.append({
                        "section": code, "department": dname, "boe_id": it.get("identificador"),
                        "title": title, "url": it.get("url_html") or config.BOE_TXT_URL.format(id=it.get("identificador")),
                        "priority": prio,
                    })
    return out


def fetch_sumario(day: date) -> tuple[dict | None, str]:
    url = config.BOE_SUMARIO_URL.format(yyyymmdd=day.strftime("%Y%m%d"))
    with httpx.Client(timeout=config.HTTP_TIMEOUT, headers={"User-Agent": config.USER_AGENT, "Accept": "application/json"}) as c:
        r = c.get(url)
    if r.status_code == 404:
        return None, "geen sumario (404): nog niet gepubliceerd of geen editie"
    r.raise_for_status()
    return r.json(), "ok"


def fetch_sub_ids(boe_id: str, client: httpx.Client) -> tuple[list[str], str]:
    """Haalt de aankondiging op en geeft alleen SUB-id's en een korte orgaanregel terug."""
    r = client.get(config.BOE_TXT_URL.format(id=boe_id))
    r.raise_for_status()
    t = re.sub(r"<[^>]+>", " ", r.text)
    t = html.unescape(re.sub(r"\s+", " ", t))
    ids = sorted(set(SUB_RE.findall(t)))
    m = re.search(r"Departamento:\s*([^.]{3,120})", t)
    organ = m.group(1).strip() if m else ""
    return ids, organ


def collect(days: list[date], max_detail: int = 25, pause: float = 1.5) -> tuple[list[dict], dict]:
    """Verzamelt kandidaat-veilingitems voor de gegeven dagen. Eén detailverzoek per item, gespreid."""
    records: list[dict] = []
    meta: dict = {"days": {}, "detail_requests": 0}
    with httpx.Client(timeout=config.HTTP_TIMEOUT, headers={"User-Agent": config.USER_AGENT}) as c:
        for d in days:
            j, status = fetch_sumario(d)
            meta["days"][d.isoformat()] = status
            if not j:
                continue
            items = parse_sumario(j)
            items.sort(key=lambda x: -x["priority"])
            for it in items:
                if meta["detail_requests"] >= max_detail:
                    it["sub_ids"] = []; it["organ"] = ""; it["detail"] = "overgeslagen (limiet)"
                else:
                    try:
                        ids, organ = fetch_sub_ids(it["boe_id"], c)
                        it["sub_ids"], it["organ"], it["detail"] = ids, organ, "ok"
                    except Exception as e:  # noqa: BLE001
                        it["sub_ids"], it["organ"], it["detail"] = [], "", f"fout: {e}"
                    meta["detail_requests"] += 1
                    time.sleep(pause)
                it["day"] = d.isoformat()
                records.append(it)
    return records, meta


def to_auction(rec: dict) -> dict | None:
    """Alleen items met een SUB-id of een expliciet veilingwoord in de titel worden veilingrecords."""
    if not rec.get("sub_ids") and not re.search(r"subasta", rec.get("title", ""), re.I):
        return None
    return {
        "source_ref": rec["boe_id"],
        "sub_ids": rec.get("sub_ids") or [],
        "boe_id": rec["boe_id"],
        "title": rec["title"][:200],
        "department": (rec.get("organ") or rec.get("department") or "")[:200],
        "area": None,   # BOE noemt de ligging niet (LEC 646.1); alleen handmatig te bevestigen
        "town": "DENIA (orgaan)" if PRIORITY_TITLE.search(rec["title"]) else None,
        "url": rec["url"],
        "blockers": ["ligging onbekend: handmatige controle op het portaal nodig"],
        "raw": {"section": rec["section"], "day": rec["day"], "priority": rec["priority"], "detail": rec.get("detail")},
    }


def days_to_check(today: date | None = None) -> list[date]:
    t = today or datetime.now(config.TZ).date()
    return [t - timedelta(days=1), t]

"""Adapter BORME-sumario (open data, zelfde hergebruikregeling als de BOE-sumario-API).

Waarom: het handelsregister meldt ontbinding, liquidatie en faillissement van vennootschappen
eerder dan de markt het merkt. Een bouw-, promotie- of vastgoedvennootschap in liquidatie in de
provincie Alicante is het vroegste signaal dat er onroerend goed onder druk op de markt komt.

Wat er wél wordt opgeslagen: naam van de vennootschap, registernummer, soort handeling, datum,
BORME-id en de link. Wat er nóóit wordt opgeslagen: de tekst van de aankondiging zelf. Die noemt
bestuurders, vereffenaars en enige aandeelhouders bij naam — persoonsgegevens die wij voor dit doel
niet nodig hebben (masterprompt: geen persoonsprofielen).

Bron: https://www.boe.es/datosabiertos/api/borme/sumario/{yyyymmdd} → per provincie één item in
Sección A met een `url_xml`. Bronvermelding: Boletín Oficial del Registro Mercantil (BOE).
"""
from __future__ import annotations

import re
import time
from datetime import date, datetime, timedelta

import httpx
from defusedxml import ElementTree as ET

from .. import config

# Handelingen die op druk wijzen. Per sleutel het Nederlandse label dat wij opslaan.
DISTRESS = [
    (re.compile(r"\bConcurso\b", re.I), "faillissement (concurso)"),
    (re.compile(r"Suspensi[oó]n de pagos", re.I), "surseance"),
    (re.compile(r"\bQuiebra\b", re.I), "faillissement (quiebra)"),
    (re.compile(r"Disoluci[oó]n", re.I), "ontbinding"),
    (re.compile(r"Liquidaci[oó]n|Liquidador", re.I), "liquidatie"),
    (re.compile(r"Extinci[oó]n", re.I), "opheffing"),
    (re.compile(r"Cierre provisional (de la )?hoja registral", re.I), "registerblad gesloten"),
    (re.compile(r"Reducci[oó]n de capital", re.I), "kapitaalvermindering"),
]
# Namen die op vastgoed, bouw of ontwikkeling wijzen.
SECTOR = re.compile(
    r"INMOBILIARI|PROMOCION|PROMOCIÓN|PROMOTORA|CONSTRUCCION|CONSTRUCCIÓN|CONSTRUCTORA|VIVIENDA|"
    r"RESIDENCIAL|URBANIZ|SOLAR|TERRENO|FINCAS|EDIFICACI|OBRAS|ARQUITECT|APARTAMENT|VILLAS|CHALET|"
    r"PROPERTIES|REAL ESTATE|ESTATES|HOMES|DESARROLLOS|PATRIMONI|ALQUILER|ARRENDAMIENT", re.I)
# Plaatsen in en rond het werkgebied; komt alleen voor als het domicilie in de regel staat.
PLACES = {
    "javea": re.compile(r"\bJ[AÁ]VEA\b|\bX[AÀ]BIA\b", re.I),
    "benitachell": re.compile(r"BENITACHELL|BENITATXELL|POBLE NOU", re.I),
    "moraira": re.compile(r"\bMORAIRA\b|\bTEULADA\b", re.I),
    "denia": re.compile(r"\bD[EÉ]NIA\b", re.I),
    "calpe": re.compile(r"\bCALPE\b|\bCALP\b", re.I),
    "benissa": re.compile(r"\bBENISSA\b", re.I),
    "gata": re.compile(r"GATA DE GORGOS", re.I),
    "pedreguer": re.compile(r"\bPEDREGUER\b", re.I),
}
ARTICULO = re.compile(r"^\s*(\d{3,8})\s*-\s*(.+?)\.?\s*$")
REG_DATE = re.compile(r"\(\s*(\d{1,2})\.(\d{1,2})\.(\d{2})\s*\)")
PROVINCE_TITLE = re.compile(r"ALICANTE|ALACANT", re.I)


def sumario_url(day: date) -> str:
    return config.BORME_SUMARIO_URL.format(yyyymmdd=day.strftime("%Y%m%d"))


def fetch_sumario(day: date) -> tuple[dict | None, str]:
    with httpx.Client(timeout=config.HTTP_TIMEOUT, headers={"User-Agent": config.USER_AGENT, "Accept": "application/json"}) as c:
        r = c.get(sumario_url(day))
    if r.status_code == 404:
        return None, "geen sumario (404): geen editie op deze dag"
    r.raise_for_status()
    return r.json(), "ok"


def province_items(j: dict, province: re.Pattern = PROVINCE_TITLE) -> list[dict]:
    """Geeft de items uit Sección A waarvan de titel de provincie is (één per provincie per dag)."""
    out: list[dict] = []
    try:
        diarios = j["data"]["sumario"]["diario"]
    except (KeyError, TypeError):
        return out
    for diario in diarios:
        secs = diario.get("seccion") or []
        secs = secs if isinstance(secs, list) else [secs]
        for sec in secs:
            if str(sec.get("codigo")).upper() != "A":
                continue
            items = sec.get("item")
            items = items if isinstance(items, list) else ([items] if items else [])
            for it in items:
                if province.search(str(it.get("titulo") or "")):
                    out.append({"borme_id": it.get("identificador"), "title": it.get("titulo"),
                                "url_xml": it.get("url_xml"), "url_html": it.get("url_html")})
    return out


def _acts(paragraph: str) -> list[str]:
    found = []
    for rx, label in DISTRESS:
        if rx.search(paragraph) and label not in found:
            found.append(label)
    return found


def _reg_date(paragraph: str, fallback: date) -> str | None:
    m = REG_DATE.search(paragraph)
    if not m:
        return None
    d, mo, y = int(m.group(1)), int(m.group(2)), int(m.group(3))
    try:
        return date(2000 + y, mo, d).isoformat()
    except ValueError:
        return None


def parse_province_xml(xml_bytes: bytes, borme_id: str, url_html: str, published: date) -> list[dict]:
    """Ontleedt de provincie-XML tot records per vennootschap. Alleen handelingen die op druk wijzen.

    De tekst van de aankondiging wordt niet teruggegeven: die bevat namen van bestuurders en
    vereffenaars. Alleen de handelingssoort, de vennootschapsnaam en het registernummer blijven over.
    """
    root = ET.fromstring(xml_bytes)
    out: list[dict] = []
    current: tuple[str, str] | None = None
    for p in root.findall(".//texto/p") or root.findall(".//p"):
        cls = (p.get("class") or "").strip()
        text = " ".join("".join(p.itertext()).split())
        if not text:
            continue
        if cls == "articulo":
            m = ARTICULO.match(text)
            current = (m.group(1), m.group(2).strip()) if m else (None, text.strip())
            continue
        if cls != "parrafo" or not current:
            continue
        acts = _acts(text)
        if not acts:
            current = None
            continue
        name = current[1]
        sector = bool(SECTOR.search(name))
        place = next((k for k, rx in PLACES.items() if rx.search(text) or rx.search(name)), None)
        in_area = place in ("javea", "benitachell", "moraira")
        hard = any(a.startswith(("faillissement", "ontbinding", "liquidatie", "opheffing", "surseance")) for a in acts)
        prio = 2 if (hard and (sector or in_area)) else (1 if hard else 0)
        if prio == 0 and not (sector and acts):
            current = None
            continue
        out.append({
            "source_ref": f"{borme_id}#{current[0] or name[:40]}",
            "borme_id": borme_id,
            "registry_no": current[0],
            "name": name[:200],
            "acts": acts,
            "sector": "vastgoed of bouw" if sector else None,
            "place": place,
            "area": place if in_area else None,
            "priority": prio,
            "url": url_html,
            "published_on": _reg_date(text, published) or published.isoformat(),
        })
        current = None
    return out


def collect(days: list[date], pause: float = 1.0) -> tuple[list[dict], dict]:
    """Verzamelt vennootschapssignalen voor de provincie Alicante over de gegeven dagen."""
    recs: list[dict] = []
    meta: dict = {"days": {}, "detail_requests": 0}
    with httpx.Client(timeout=config.HTTP_TIMEOUT, headers={"User-Agent": config.USER_AGENT}) as c:
        for d in days:
            try:
                j, status = fetch_sumario(d)
            except Exception as e:  # noqa: BLE001
                meta["days"][d.isoformat()] = f"fout: {str(e)[:100]}"
                continue
            meta["days"][d.isoformat()] = status
            if not j:
                continue
            items = province_items(j)
            if not items:
                meta["days"][d.isoformat()] = "ok, geen Alicante-item"
                continue
            for it in items:
                if not it.get("url_xml"):
                    continue
                try:
                    r = c.get(it["url_xml"])
                    r.raise_for_status()
                    recs.extend(parse_province_xml(r.content, it["borme_id"], it.get("url_html") or it["url_xml"], d))
                except Exception as e:  # noqa: BLE001
                    meta["days"][d.isoformat()] = f"{status}; detail fout: {str(e)[:80]}"
                meta["detail_requests"] += 1
                time.sleep(pause)
    return recs, meta


def days_to_check(today: date | None = None) -> list[date]:
    """BORME verschijnt op werkdagen; twee dagen terugkijken vangt een gemiste ronde op."""
    t = today or datetime.now(config.TZ).date()
    return [t - timedelta(days=2), t - timedelta(days=1), t]

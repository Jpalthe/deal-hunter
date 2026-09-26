"""Configuratie van de Deal Hunter-monitor. Geheimen komen uit .env (rechten 600), nooit uit code."""
from __future__ import annotations

import os
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parent.parent          # ~/tree-es/deal-hunter
DATA = ROOT / "data"
DB_PATH = DATA / "dealhunter.sqlite"
REPORTS = ROOT / "rapporten" / "dagelijks"
LOGS = ROOT / "logs"
KADER = ROOT / "kader"
TZ = ZoneInfo("Europe/Madrid")

# Werkgebied (investeringskader 15-09-2026). Plaatsnamen zoals ze in bronnen voorkomen;
# vergelijking gebeurt op genormaliseerde vorm (kleine letters, zonder accenten).
WORK_AREA = {
    "javea": ["javea", "jávea", "xàbia", "xabia", "javea/xabia", "jávea/xàbia"],
    "benitachell": ["benitachell", "benitatxell", "el poble nou de benitatxell", "poble nou de benitatxell", "cumbre del sol"],
    "moraira": ["moraira", "teulada", "teulada-moraira", "moraira-teulada"],
}
# Plausibele coördinaten voor Marina Alta (WGS84). Punten daarbuiten zijn feedfouten (bv. 0,0) en worden genegeerd.
REGION_BBOX = (38.60, 38.90, -0.10, 0.30)


def valid_coord(lat, lon) -> bool:
    try:
        la, lo = float(lat), float(lon)
    except (TypeError, ValueError):
        return False
    return REGION_BBOX[0] <= la <= REGION_BBOX[1] and REGION_BBOX[2] <= lo <= REGION_BBOX[3]


# Postcodes (deliverable 04; volledigheid [te verifiëren])
POSTCODES = {"03730", "03737", "03738", "03739", "03726", "03724", "03725"}

# Investeringskader (kader/investeringskader.json is leidend; dit zijn alleen fallbacks)
BUDGET_MIN = 500_000
BUDGET_MAX = 1_000_000
PLOT_BUDGET_MIN = 100_000

# BOE: departamenten en titels die op veilingen wijzen (deliverable 04 §2.9)
BOE_SECTIONS = {"4", "5B"}
BOE_DEPT_KEYWORDS = ["TRIBUNALES DE INSTANCIA", "SERVICIOS COMUNES PROCESALES", "SECCIÓN MERCANTIL", "SECCION MERCANTIL",
                     "JUZGADO", "MINISTERIO DE HACIENDA", "SEGURIDAD SOCIAL", "ADMINISTRACIÓN LOCAL", "ADMINISTRACION LOCAL"]
BOE_TITLE_KEYWORDS = ["DENIA", "DÉNIA", "ALICANTE", "ALACANT", "SUMA GESTIÓN", "SUMA GESTION", "SUBASTA", "AGENCIA TRIBUTARIA", "TESORERÍA GENERAL", "TESORERIA GENERAL"]
BOE_SUMARIO_URL = "https://www.boe.es/datosabiertos/api/boe/sumario/{yyyymmdd}"
BOE_TXT_URL = "https://www.boe.es/diario_boe/txt.php?id={id}"
BORME_SUMARIO_URL = "https://www.boe.es/datosabiertos/api/borme/sumario/{yyyymmdd}"
BORME_ATTRIBUTION = "Boletín Oficial del Registro Mercantil (BOE), hergebruik met bronvermelding"
# Publicatieborden van de drie gemeenten: robots.txt van sedelectronica.es verbiedt geautomatiseerd
# lezen ("Disallow: /*", alleen /info en / toegestaan, gecontroleerd 17-09-2026). Daarom alleen
# handmatig openen; de links staan in het rapport en op de telefoonpagina.
TABLONES = [
    ("Xàbia", "https://xabia.sedelectronica.es/board"),
    ("El Poble Nou de Benitatxell", "https://benitatxell.sedelectronica.es/board"),
    ("Teulada-Moraira", "https://teuladamoraira.sedelectronica.es/board"),
]
AEAT_BIENES_URL = "https://www2.agenciatributaria.gob.es/static_files/common/internet/dep/taiif/subastaInmuebles/data2/bienes.js"
AEAT_ATTRIBUTION = "Lista de bienes a subastar por la AEAT (CC BY 4.0), https://sede.agenciatributaria.gob.es/Sede/subastas.html"
BP_LOCAL_API = os.environ.get("DH_BP_LOCAL_API", "http://127.0.0.1:3100")
BP_SHRINK_ABORT_PCT = 30   # zelfde drempel als de website-import: bij >30 % krimp geen 'verdwenen'-gebeurtenissen

USER_AGENT = "TREE-DealHunter/0.1 (intern gebruik; contact via treeproperties.es)"
HTTP_TIMEOUT = 30


def load_env(path: Path | None = None) -> dict:
    """Leest ROOT/.env (KEY=VALUE per regel). Geen geheimen loggen."""
    p = path or (ROOT / ".env")
    env: dict[str, str] = {}
    if p.exists():
        for line in p.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            env[k.strip()] = v.strip().strip('"').strip("'")
    for k in ("ANTHROPIC_API_KEY", "DISCORD_WEBHOOK_URL", "RESEND_API_KEY", "DH_EMAIL_TO", "DH_EMAIL_FROM",
              "GOOLZOOM_API_KEY"):
        if k in os.environ and k not in env:
            env[k] = os.environ[k]
    return env


# Sleutels die via het instellingenscherm gezet mogen worden. Bewust een korte, vaste lijst: zo kan
# een verkeerd verzoek nooit een willekeurige regel in .env schrijven.
INSTELBAAR = {
    "DISCORD_WEBHOOK_URL": "Discord-webhook voor meldingen op je telefoon",
    "RESEND_API_KEY": "Sleutel van Resend om e-mail te versturen",
    "DH_EMAIL_TO": "Adres waar de e-mail heen gaat",
    "DH_EMAIL_FROM": "Afzender van de e-mail (mag leeg)",
    "ANTHROPIC_API_KEY": "Sleutel voor de AI-classificatie",
    # Let op: hier staat een hash, nooit het wachtwoord zelf. Zetten gaat via
    # POST /api/wachtwoord, dat eerst hasht; het algemene instellingen-eindpunt
    # weigert deze sleutel met opzet.
    "DH_WACHTWOORD_HASH": "Wachtwoord om het dashboard te openen",
}


def save_env_key(sleutel: str, waarde: str, path: Path | None = None) -> None:
    """Zet één sleutel in .env. Bestaande regels blijven staan, rechten blijven 600.

    Geschreven omdat Jan vanaf zijn telefoon geen bestand kan bewerken. De waarde wordt nergens
    gelogd en nergens teruggetoond; het scherm zegt alleen of een sleutel gevuld is."""
    if sleutel not in INSTELBAAR:
        raise ValueError(f"deze sleutel mag hier niet gezet worden: {sleutel}")
    if "\n" in waarde or "\r" in waarde:
        raise ValueError("een waarde mag geen nieuwe regel bevatten")
    p = path or (ROOT / ".env")
    regels = p.read_text(encoding="utf-8").splitlines() if p.exists() else []
    nieuw, gezien = [], False
    for r in regels:
        if r.split("=", 1)[0].strip() == sleutel:
            if not gezien:
                nieuw.append(f"{sleutel}={waarde}")
                gezien = True
            continue                      # eventuele dubbele regels verdwijnen
        nieuw.append(r)
    if not gezien:
        nieuw.append(f"{sleutel}={waarde}")
    tijdelijk = p.with_suffix(".env.nieuw")
    tijdelijk.write_text("\n".join(nieuw).rstrip("\n") + "\n", encoding="utf-8")
    tijdelijk.chmod(0o600)
    tijdelijk.replace(p)                  # in één stap, zodat .env nooit half geschreven is
    p.chmod(0o600)


def norm_place(s: str | None) -> str:
    import unicodedata
    if not s:
        return ""
    t = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower().strip()
    return " ".join(t.split())


def area_of(town: str | None, postcode: str | None = None, extra_text: str | None = None) -> str | None:
    """Geeft 'javea' | 'benitachell' | 'moraira' of None. Postcode en vrije tekst als fallback."""
    t = norm_place(town)
    for key, names in WORK_AREA.items():
        for n in names:
            if t == norm_place(n) or (t and norm_place(n) in t and len(t) < 40):
                return key
    if postcode and str(postcode).strip() in POSTCODES:
        pc = str(postcode).strip()
        return "javea" if pc in {"03730", "03737", "03738", "03739"} else ("benitachell" if pc == "03726" else "moraira")
    if extra_text:
        e = norm_place(extra_text)
        for key, names in WORK_AREA.items():
            if any(norm_place(n) in e for n in names):
                return key
    return None

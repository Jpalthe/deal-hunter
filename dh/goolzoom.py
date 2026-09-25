"""Goolzoom: bestemming per perceel en de fiscale referentiewaarde.

Wat deze koppeling toevoegt boven het kadaster (`dh/catastro.py`), dat alleen zegt wát er staat:

  urbanplanning/cadastralparcel/{rc14}/{laag}/data   welke bestemming op dit perceel rust
  cadastre/cadastralparcel/{rc14}/cadastralreferences  de eenheden op dit perceel (20 tekens)
  cadastre/cadastralreference/{rc20}/referencevalue    de valor de referencia van een eenheid
  cadastre/latlng/{lat}/{lng}/geo                      punt → perceelgrens

Bron van de urbanismelaag is IDEV (Generalitat Valenciana), niet Goolzoom zelf; dat staat in elk
antwoord onder `datasource` en wordt meegeschreven.

Grens van wat dit zegt (masterprompt §14-17). De laag geeft de **classificatie** (stedelijk,
urbaniseerbaar, niet-urbaniseerbaar) en de **zonering**. Zij geeft GEEN edificabilidad, geen
bebouwingspercentage, geen bouwhoogte en geen minimale perceelsmaat. Een bouwvolume mag hier dus
nooit uit worden afgeleid; dat blijft de informe urbanística bij de gemeente. Wat deze koppeling
wél afdoende beantwoordt, is de vraag die ervóór komt: mag hier überhaupt gewoond worden.

Voorwaarden en limieten (gecontroleerd 25-09-2026, https://www.goolzoom.com/api/TermsOfUse.aspx en
/api/documentation/General.aspx): 10 verzoeken per seconde, piek 5, 100.000 per maand. Elke
bevraging kost geld, dus alles wordt in de database bewaard en pas na VERVERS_DAGEN opnieuw
opgehaald. De sleutel staat in .env en komt nooit in een rapport, prompt of logregel.
"""
from __future__ import annotations

import threading
import time
from datetime import datetime, timedelta

import httpx

from . import config

BASIS = "https://api.goolzoom.com/v1/"
BRON_URL = "https://www.goolzoom.com/api/documentation/UrbanPlanning.aspx"
VERVERS_DAGEN = 90          # een bestemmingsplan verandert niet per week
VERZOEKEN_PER_S = 3.0       # ruim onder de toegestane 10/s
RC14 = 14
RC20 = 20

_lock = threading.Lock()
_next = [0.0]


def beschikbaar() -> bool:
    return bool(config.load_env().get("GOOLZOOM_API_KEY"))


def _wacht() -> None:
    with _lock:
        nu = time.monotonic()
        if nu < _next[0]:
            time.sleep(_next[0] - nu)
        _next[0] = max(nu, _next[0]) + 1.0 / VERZOEKEN_PER_S


def _get(pad: str, client: httpx.Client | None = None):
    """Eén GET. Geeft het JSON-antwoord, of None bij 404/leeg. Fouten worden opgegooid."""
    sleutel = config.load_env().get("GOOLZOOM_API_KEY")
    if not sleutel:
        raise RuntimeError("GOOLZOOM_API_KEY ontbreekt in .env")
    kop = {"x-api-key": sleutel, "User-Agent": config.USER_AGENT}
    _wacht()
    eigen = client is None
    cl = client or httpx.Client(timeout=config.HTTP_TIMEOUT)
    try:
        r = cl.get(BASIS + pad, headers=kop)
        if r.status_code == 404:
            return None
        if r.status_code in (401, 403):
            raise RuntimeError(f"Goolzoom weigert de sleutel (HTTP {r.status_code})")
        r.raise_for_status()
        if not r.text.strip():
            return None
        return r.json()
    finally:
        if eigen:
            cl.close()


# ---------------------------------------------------------------- losse bevragingen

def urbanisme(rc14: str, laag: str = "classification", client=None) -> dict | None:
    """Bestemming van één perceel. Laag is 'classification' of 'qualification'."""
    if not rc14 or len(rc14) != RC14:
        return None
    d = _get(f"urbanplanning/cadastralparcel/{rc14}/{laag}/data", client)
    if not d or not isinstance(d.get("data"), dict):
        return None
    g = d["data"]
    # De sleutelnamen komen letterlijk uit het antwoord, inclusief hun tikfout ("mMunicipio").
    return {
        "rc": rc14,
        "laag": laag,
        "gemeente": g.get("Nombre del municipio"),
        "ine": g.get("Código INE del mMunicipio"),
        "plan": g.get("Denominación"),
        "expediente": g.get("Expediente"),
        "classificatie": g.get("Clasificación del Suelo"),
        "zonering": g.get("Zonificación del Suelo"),
        "omschrijving": g.get("Descripción"),
        "plan_url": g.get("Documentación"),
        "databron": (d.get("datasource") or {}).get("sourcename"),
        "databron_url": (d.get("datasource") or {}).get("sourceurl"),
    }


def eenheden(rc14: str, client=None) -> list[dict]:
    """De eenheden (20 tekens) op één perceel."""
    if not rc14 or len(rc14) != RC14:
        return []
    d = _get(f"cadastre/cadastralparcel/{rc14}/cadastralreferences", client)
    uit = []
    for e in (d or {}).get("cadastralreferences") or []:
        # het veld heet in het antwoord "cadatralreference" (tikfout aan hun kant)
        ref = e.get("cadatralreference") or e.get("cadastralreference")
        if ref and len(ref) == RC20:
            uit.append({"rc": ref, "oppervlak": e.get("area"), "verdieping": e.get("floor")})
    return uit


def referentiewaarde(rc20: str, client=None) -> float | None:
    """Valor de referencia van één eenheid: de fiscale ondergrens voor de overdrachtsbelasting."""
    if not rc20 or len(rc20) != RC20:
        return None
    d = _get(f"cadastre/cadastralreference/{rc20}/referencevalue", client)
    if isinstance(d, dict):
        v = d.get("referencevalue")
        if isinstance(v, (int, float)) and v > 0:
            return float(v)
    return None


# ---------------------------------------------------------------- duiding

# De classificatiecodes zijn de Spaanse wettelijke hoofdindeling; de omschrijving bij de zonering
# komt letterlijk uit het antwoord en wordt niet vertaald of uitgelegd.
BETEKENIS = {
    "SU":    ("stedelijk", "Stedelijk terrein. Bouwen is in beginsel mogelijk; hoevéél zegt de gemeente."),
    "SUZ":   ("urbaniseerbaar", "Urbaniseerbaar, nog niet stedelijk. Pas te bebouwen na een goedgekeurd "
                                "ontwikkelingsplan, en de urbanisatiekosten komen voor rekening van de eigenaar."),
    "SNU":   ("niet-urbaniseerbaar", "Niet-urbaniseerbaar terrein. Geen woningbouw zonder uitzonderingsprocedure."),
    "SNU-C": ("niet-urbaniseerbaar", "Niet-urbaniseerbaar, gewone rustieke grond. Geen woningbouw zonder "
                                     "uitzonderingsprocedure."),
    "SNU-P": ("niet-urbaniseerbaar", "Niet-urbaniseerbaar én beschermd. Woningbouw is hier praktisch uitgesloten."),
}
# Wat het voor ons betekent: mag hier gewoond worden? ja / voorwaardelijk / nee / onbekend
GEVOLG = {"stedelijk": "ja", "urbaniseerbaar": "voorwaardelijk", "niet-urbaniseerbaar": "nee"}


def duiding(cls: str | None) -> dict:
    """Van de code naar één uitspraak. Onbekende codes blijven ONBEKEND."""
    c = (cls or "").strip().upper()
    hit = BETEKENIS.get(c) or BETEKENIS.get(c.split("-")[0])
    if not hit:
        return {"soort": None, "wonen": "onbekend", "tekst": "De bestemming is niet vastgesteld."}
    soort, tekst = hit
    return {"soort": soort, "wonen": GEVOLG.get(soort, "onbekend"), "tekst": tekst}


# ---------------------------------------------------------------- opslag

TABEL = """
CREATE TABLE IF NOT EXISTS urbanism (
  listing_id INTEGER PRIMARY KEY,
  rc TEXT, classificatie TEXT, zonering TEXT, omschrijving TEXT,
  plan TEXT, expediente TEXT, plan_url TEXT, gemeente TEXT,
  databron TEXT, databron_url TEXT,
  ref_waarde REAL, ref_eenheden INTEGER,
  fetched_at TEXT, error TEXT
);
"""


def zorg_tabel(store) -> None:
    store.con.executescript(TABEL)
    store.con.commit()


def bewaar(store, listing_id: int, u: dict | None, ref_waarde=None, ref_eenheden=None, error=None) -> None:
    zorg_tabel(store)
    u = u or {}
    store.con.execute(
        """INSERT INTO urbanism (listing_id, rc, classificatie, zonering, omschrijving, plan, expediente,
                                 plan_url, gemeente, databron, databron_url, ref_waarde, ref_eenheden,
                                 fetched_at, error)
           VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
           ON CONFLICT(listing_id) DO UPDATE SET
             rc=excluded.rc, classificatie=excluded.classificatie, zonering=excluded.zonering,
             omschrijving=excluded.omschrijving, plan=excluded.plan, expediente=excluded.expediente,
             plan_url=excluded.plan_url, gemeente=excluded.gemeente, databron=excluded.databron,
             databron_url=excluded.databron_url, ref_waarde=excluded.ref_waarde,
             ref_eenheden=excluded.ref_eenheden, fetched_at=excluded.fetched_at, error=excluded.error""",
        (listing_id, u.get("rc"), u.get("classificatie"), u.get("zonering"), u.get("omschrijving"),
         u.get("plan"), u.get("expediente"), u.get("plan_url"), u.get("gemeente"),
         u.get("databron"), u.get("databron_url"), ref_waarde, ref_eenheden,
         datetime.now(config.TZ).isoformat(timespec="seconds"), error))
    store.con.commit()


def lees(store, listing_id: int) -> dict | None:
    """Wat wij van dit object weten, met de duiding erbij. Geen netwerkverkeer."""
    try:
        zorg_tabel(store)
        r = store.con.execute("SELECT * FROM urbanism WHERE listing_id=?", (listing_id,)).fetchone()
    except Exception:  # noqa: BLE001
        return None
    if not r:
        return None
    d = dict(r)
    if d.get("error") and not d.get("classificatie"):
        return None
    d["duiding"] = duiding(d.get("classificatie"))
    d["bron"] = d.get("databron_url") or BRON_URL
    return d


def vers(store, listing_id: int) -> bool:
    """Staat er een antwoord dat nog niet aan vervanging toe is?"""
    r = lees(store, listing_id)
    if not r or not r.get("fetched_at"):
        return False
    try:
        op = datetime.fromisoformat(r["fetched_at"])
    except ValueError:
        return False
    return datetime.now(config.TZ) - op < timedelta(days=VERVERS_DAGEN)

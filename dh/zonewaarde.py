"""Het werkelijk betaalde prijspeil per wijk, uit de waardekaarten van het kadaster.

Onze vergelijkingsprijzen in `kader/comparables.json` zijn **vraagprijzen** van Idealista. Wat een
huis werkelijk opbracht staat daar niet in. Het Catastro verdeelt elke gemeente in *ámbitos
territoriales homogéneos* en stelt per zone een *módulo de valor medio* vast voor één
representatieve woning. Volgens het Catastro zelf komen die modules uit de prijzen van álle
koopakten die voor een notaris zijn gesloten. Dat is het dichtste bij een echte verkoopprijs per
wijk dat gratis en toegestaan te krijgen is (onderzoek N11, 26-09-2026).

Wat de module wél is: het gemiddelde van de werkelijk betaalde prijzen in die zone, vóór de
*factor de minoración* — dus het marktgemiddelde, niet de verlaagde fiscale waarde.

Wat de module **niet** is:
  - geen waarde van dít object. Hij hoort bij één standaardwoning: in zone U20 van Jávea een
    gerenoveerde woning van 50 jaar oud, 160 m² op 1.000 m². Een nieuwbouwvilla van 300 m² in
    dezelfde zone hoort daar niet bij.
  - geen actuele prijs. Uit welke jaren de transacties komen staat niet in het antwoord: ONBEKEND.
  - niet vergelijkbaar met een bouwkostenkental. Voor vrijstaande woningen zit de grondwaarde
    erin, net als in onze vraagprijs per m² bebouwd.

Daarom wordt de module hier gebruikt als tweede opinie op de verkoopwaarde, nooit als vervanging
van de wijkreeks.

Bron: Dirección General del Catastro, mapa de valores, `SECDameGeoJSON.aspx`. Openbaar, geen
sleutel, reproductie met bronvermelding. Eén verzoek per gemeente per jaargang.
"""
from __future__ import annotations

import json
import math
import sqlite3
import threading
import time
from datetime import datetime

import httpx

from . import config

DIENST = "https://www1.sedecatastro.gob.es/Cartografia/SECDameGeoJSON.aspx"
CACHE = config.DATA / "waardezones.json"
BRON = ("Dirección General del Catastro, mapa de valores (módulos de valor medio per ámbito "
        "territorial homogéneo), https://www1.sedecatastro.gob.es/Cartografia/mapa.aspx?ZV=SI")
PAUZE_S = 2.0
_laatste = [0.0]
_slot = threading.Lock()

# Per gemeente: kadastrale delegatie/gemeente en een punt dat er zeker in ligt. De dienst negeert
# del/mun en kijkt alleen naar de coördinaat (vastgesteld in onderzoek N11 §1.2), maar wij sturen ze
# mee zoals de kaartviewer dat doet en controleren het antwoord op id_municipio.
GEMEENTEN = {
    "javea": {"naam": "Jávea/Xàbia", "del": "03", "mun": "082", "punt": (0.1830, 38.7647)},
    "benitachell": {"naam": "El Poble Nou de Benitatxell", "del": "03", "mun": "042", "punt": (0.1636, 38.7085)},
    "moraira": {"naam": "Teulada-Moraira", "del": "03", "mun": "128", "punt": (0.1430, 38.6875)},
}

# Welke representatieve typologie hoort bij welk soort advertentie. Staat er niets in deze tabel,
# dan koppelen wij niet: liever geen prijspeil dan het verkeerde (onderzoek N11 §9.2).
TYPOLOGIE = {
    "villa": "aislada",
    "country house": "aislada",
    "land": "aislada",            # een kavel wordt een vrijstaande woning; de zone is dezelfde
    "apartment": "colectiva",
    "town house": "hilera",
}
# De officiële omschrijvingen waarin die sleutelwoorden voorkomen:
#   "Vivienda unifamiliar aislada/pareada" · "Vivienda colectiva" · "Vivienda unifamiliar en hilera"


def _wacht() -> None:
    with _slot:
        nu = time.time()
        moment = max(nu, _laatste[0])
        _laatste[0] = moment + PAUZE_S
    rust = moment - time.time()
    if rust > 0:
        time.sleep(rust)


def _naar_mercator(lon: float, lat: float) -> tuple[float, float]:
    """WGS84 → Web Mercator (EPSG:3857). De dienst wil x/y in meters, niet in graden."""
    x = lon * 20037508.34 / 180.0
    y = math.log(math.tan((90.0 + lat) * math.pi / 360.0)) / (math.pi / 180.0) * 20037508.34 / 180.0
    return x, y


def _punt(co) -> tuple[float, float]:
    """Eén punt uit de geometrie als (lon, lat).

    Let op: de x/y in de aanvraag moeten in Web Mercator, maar de geometrie in het antwoord komt
    terug in gewone graden. Wie de teruggave nog eens omrekent, houdt niets over (26-09-2026).
    Een paar waarvan het eerste getal boven de 38 ligt staat omgekeerd; Jávea ligt rond lon 0,2."""
    x, y = float(co[0]), float(co[1])
    if 38.0 < x < 39.5 and -1.0 < y < 1.5:
        return (y, x)
    return (x, y)


def _ringen(geom) -> list[list[list[tuple[float, float]]]]:
    """Alle vlakken als [buitenring, gat, gat, ...], omgerekend naar lon/lat.

    Gaten tellen mee: een waardezone kan een stuk uitsparen dat bij een andere zone hoort. Wie
    alleen de buitenring leest, plakt zo'n punt aan de verkeerde zone."""
    if not isinstance(geom, dict):
        return []
    soort, co = geom.get("type"), geom.get("coordinates") or []
    vlakken = [co] if soort == "Polygon" else (co if soort == "MultiPolygon" else [])
    uit = []
    for vlak in vlakken:
        ringen = [[_punt(p) for p in ring] for ring in vlak if len(ring) >= 4]
        if ringen:
            uit.append(ringen)
    return uit


def _in_ring(x: float, y: float, ring) -> bool:
    binnen = False
    j = len(ring) - 1
    for i in range(len(ring)):
        xi, yi = ring[i]
        xj, yj = ring[j]
        if (yi > y) != (yj > y) and x < (xj - xi) * (y - yi) / ((yj - yi) or 1e-15) + xi:
            binnen = not binnen
        j = i
    return binnen


def _in_vlak(lon: float, lat: float, vlak) -> bool:
    if not _in_ring(lon, lat, vlak[0]):
        return False
    return not any(_in_ring(lon, lat, gat) for gat in vlak[1:])


def _zone_uit(f: dict) -> dict | None:
    """Eén feature uit het antwoord naar de velden die wij bewaren."""
    p = f.get("properties") or {}
    t = p.get("Ptipo1") or {}
    if not t.get("tipologia") or not t.get("val_tipo"):
        return None            # zone zonder representatief product: die zegt niets over prijs
    vlakken = _ringen(f.get("geometry"))
    if not vlakken:
        return None
    return {
        "zona_valor": p.get("zona_valor"), "cod_zona": str(p.get("cod_zona") or ""),
        "ejercicio": p.get("ejercicio"), "num_inmuebles": p.get("num_inmuebles_uso_v"),
        "tipologia": t.get("tipologia"), "categoria": t.get("categoria"),
        "antiguedad": t.get("antiguedad"), "conservacion": t.get("conservacion"),
        "superficie": t.get("superficie"), "superficie_suelo": t.get("superficie_suelo"),
        "val_tipo": t.get("val_tipo"), "val_tipo_m2": t.get("val_tipo_m2"),
        "val_estandar_m2": t.get("val_estandar_m2"),
        "vlakken": vlakken,
    }


def haal_zones(client=None, opnieuw: bool = False, anyo: str = "2027") -> dict:
    """Haalt de waardezones van de drie gemeenten op en bewaart ze. Drie verzoeken per jaar.

    De ponencia verandert hoogstens één keer per jaar, dus het bestand blijft staan tot iemand
    `opnieuw` meegeeft. Welke jaargang het antwoord bevat lezen wij uit `ejercicio`; wat wij
    vragen is niet per se wat wij krijgen."""
    if CACHE.exists() and not opnieuw:
        try:
            return json.loads(CACHE.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            pass
    eigen = client is None
    cl = client or httpx.Client(timeout=120)
    uit: dict = {"bron": BRON, "opgehaald_op": datetime.now(config.TZ).isoformat(timespec="seconds"),
                 "gevraagde_jaargang": anyo, "gemeenten": {}}
    try:
        for sleutel, g in GEMEENTEN.items():
            x, y = _naar_mercator(*g["punt"])
            par = {"del": g["del"], "mun": g["mun"], "huso": "3857", "x": f"{x:.2f}", "y": f"{y:.2f}",
                   "suelo": "N", "tipo_mapa": "vivienda", "anyoZV": anyo}
            _wacht()
            try:
                r = cl.get(DIENST, params=par, headers={"User-Agent": config.USER_AGENT})
                d = r.json() if r.status_code == 200 else {}
            except Exception as e:  # noqa: BLE001 — één gemeente die hapert mag de rest niet stoppen
                uit["gemeenten"][sleutel] = {"naam": g["naam"], "zones": [], "fout": str(e)[:160]}
                continue
            zones = [z for z in (_zone_uit(f) for f in (d.get("features") or [])) if z]
            jaren = {z["ejercicio"] for z in zones if z.get("ejercicio")}
            uit["gemeenten"][sleutel] = {"naam": g["naam"], "zones": zones,
                                         "ejercicio": (sorted(jaren)[-1] if jaren else None),
                                         "aantal_features": len(d.get("features") or [])}
    finally:
        if eigen:
            cl.close()
    CACHE.parent.mkdir(parents=True, exist_ok=True)
    CACHE.write_text(json.dumps(uit, ensure_ascii=False), encoding="utf-8")
    return uit


def _past(tipologia: str, wens: str) -> bool:
    t = (tipologia or "").lower()
    if wens == "aislada":
        return "aislada" in t or "pareada" in t
    if wens == "hilera":
        return "hilera" in t
    if wens == "colectiva":
        return "colectiva" in t
    return False


def zoek(lat: float, lon: float, soort: str | None, zones: dict | None = None) -> dict:
    """Welke waardezone hoort bij dit punt en dit soort object.

    Geeft altijd een oordeel terug, ook als er niets te koppelen valt — dan staat in `reden`
    waarom. Bij overlap (een punt kan in de villazone én in de appartementenzone liggen) beslist
    de typologie; past er geen enkele, dan koppelen wij niet."""
    z = zones if zones is not None else haal_zones()
    wens = TYPOLOGIE.get((soort or "").strip().lower())
    raak = []
    for sleutel, g in (z.get("gemeenten") or {}).items():
        for zone in g.get("zones") or []:
            if any(_in_vlak(lon, lat, v) for v in zone["vlakken"]):
                raak.append({**{k: v for k, v in zone.items() if k != "vlakken"},
                             "gemeente": sleutel, "gemeente_naam": g.get("naam")})
    if not raak:
        return {"gevonden": False, "overlap": 0, "reden": "punt ligt buiten alle waardezones van het kadaster"}
    if not wens:
        return {"gevonden": False, "overlap": len(raak),
                "reden": f"soort {soort or 'onbekend'!r} hoort bij geen enkele representatieve typologie"}
    passend = [r for r in raak if _past(r["tipologia"], wens)]
    if not passend:
        heeft = ", ".join(sorted({r["tipologia"] for r in raak}))
        return {"gevonden": False, "overlap": len(raak),
                "reden": f"geen zone met de passende typologie op dit punt (hier: {heeft})"}
    # Meerdere zones met dezelfde typologie op één punt hoort niet voor te komen. Gebeurt het toch,
    # dan nemen wij de zone met de meeste woningen: die is het best onderbouwd.
    beste = max(passend, key=lambda r: (r.get("num_inmuebles") or 0))
    return {"gevonden": True, "overlap": len(raak), "reden": None, **beste}


# De Spaanse termen van het kadaster in gewoon Nederlands. Jan leest deze zin, niet de bron.
NL_TIPOLOGIE = {"aislada": "vrijstaande of geschakelde woning", "hilera": "rijwoning",
                "colectiva": "appartement"}
NL_STAAT = {"renovado": "gerenoveerd", "normal": "normale staat", "reformado": "verbouwd",
            "ruinoso": "bouwvallig", "deficiente": "slechte staat", "regular": "redelijke staat"}
NL_CATEGORIE = {"alta": "hoge afwerking", "media": "gemiddelde afwerking", "baja": "eenvoudige afwerking"}


def _nl_tipologie(t: str | None) -> str:
    for sleutel, woord in NL_TIPOLOGIE.items():
        if sleutel in (t or "").lower():
            return woord
    return t or "woning"


def omschrijving(z) -> str:
    """Eén zin die zegt waar het bedrag bij hoort. Zonder die zin is het getal misleidend.

    Werkt zowel op de uitkomst van `zoek()` als op een rij uit de tabel `zonewaarde`."""
    z = dict(z) if z else {}
    if not z.get("val_tipo_m2"):
        return ""
    eu = lambda v: f"{v:,.0f}".replace(",", ".")      # noqa: E731 — duizendtallen met een punt
    euro, m2 = eu(z["val_tipo"]), eu(z["val_tipo_m2"])
    staat = NL_STAAT.get((z.get("conservacion") or "").lower(), (z.get("conservacion") or "").lower())
    grond = f" op {eu(z['superficie_suelo'])} m² grond" if z.get("superficie_suelo") else ""
    return (f"Kadaster, zone {z['zona_valor']} (ATH {z['cod_zona']}): een {_nl_tipologie(z.get('tipologia'))} "
            f"van {eu(z.get('superficie') or 0)} m²{grond}, {z.get('antiguedad')} jaar oud, {staat}, "
            f"deed hier gemiddeld € {euro} — oftewel € {m2} per m². Gemiddelde van de notariële "
            f"koopakten in deze zone, jaargang {z.get('ejercicio')}.")


# ------------------------------------------------- opgeslagen uitkomst per advertentie

_geheugen: dict = {"stempel": None, "per_listing": {}}
_geheugen_slot = threading.Lock()


def per_listing(pad=None) -> dict[int, dict]:
    """De opgeslagen koppeling advertentie → waardezone, uit de tabel `zonewaarde`.

    Wordt bij elke aanroep gecontroleerd op een stempel (aantal rijen + laatste tijdstip), zodat een
    draaiend dashboard de nieuwe cijfers ziet zodra de verrijking heeft gelopen, maar niet bij elke
    advertentie de hele tabel opnieuw leest."""
    p = str(pad or config.DB_PATH)
    try:
        con = sqlite3.connect(f"file:{p}?mode=ro", uri=True, timeout=5)
    except sqlite3.Error:
        return {}
    try:
        con.row_factory = sqlite3.Row
        try:
            stempel = tuple(con.execute("SELECT count(*), max(at) FROM zonewaarde").fetchone())
        except sqlite3.OperationalError:
            return {}                     # tabel bestaat nog niet: nog niet verrijkt
        with _geheugen_slot:
            if _geheugen["stempel"] == (p, stempel):
                return _geheugen["per_listing"]
        rijen = {int(r["listing_id"]): dict(r)
                 for r in con.execute("SELECT * FROM zonewaarde WHERE val_tipo_m2 IS NOT NULL")}
        with _geheugen_slot:
            _geheugen["stempel"], _geheugen["per_listing"] = (p, stempel), rijen
        return rijen
    finally:
        con.close()


def module_voor(listing_id) -> dict | None:
    """De waardezone van één advertentie, of None als er geen koppeling is."""
    try:
        return per_listing().get(int(listing_id))
    except (TypeError, ValueError):
        return None


# Drempels voor de verhouding tussen onze aangenomen verkoopwaarde per m² en het zonegemiddelde.
#
# Onderzoek N11 §9.4 stelde één drempel van 2,0 voor, afgeleid uit wijkmedianen van VRAAGprijzen
# (0,53–0,93 van de module, dus 1,08–1,89 andersom). Hier vergelijken wij iets anders: de
# verkoopwaarde ná renovatie of nieuwbouw van één object. Die ligt van nature hoger dan de
# wijkmediaan, want de module hoort bij een 40 tot 50 jaar oude woning in gemiddelde staat.
#
# Gemeten op onze eigen 343 scenario's met een zonemodule (26-09-2026): mediaan 1,54 · p75 1,92 ·
# p90 2,27 · hoogste 3,42. Bij 2,0 zou een vijfde van alle scenario's onbetrouwbaar worden — dat is
# geen signaal maar ruis. Daarom twee niveaus:
#   vanaf 2,0  een opmerking: hoog, maar met een grondige renovatie te verklaren (20 % van de gevallen)
#   vanaf 2,5  een waarschuwing: boven ongeveer de 97e percentiel van wat wij zien (3 %)
# Onder 1,0 gaat het de andere kant op: dan ligt onze verkoopwaarde ónder het zonegemiddelde, en
# is de vergelijkingsreeks vermoedelijk te laag voor dit object.
DREMPEL_OPMERKING = 2.0
DREMPEL = 2.5


def oordeel(eur_m2_verkoop: float | None, z: dict | None) -> tuple[str, str] | None:
    """Vergelijkt onze verkoopwaarde met het zonegemiddelde.

    Geeft ("waarschuwing" | "opmerking", tekst) of None. Een waarschuwing raakt de betrouwbaarheid
    van het scenario, een opmerking niet."""
    if not eur_m2_verkoop or not z or not z.get("val_tipo_m2"):
        return None
    mod = float(z["val_tipo_m2"])
    if mod <= 0:
        return None
    keer = eur_m2_verkoop / mod
    zone = z.get("zona_valor")
    ons = f"{eur_m2_verkoop:,.0f}".replace(",", ".")
    hun = f"{mod:,.0f}".replace(",", ".")
    x = f"{keer:.1f}".replace(".", ",")          # Nederlandse komma, zoals overal in de app
    if keer >= DREMPEL:
        return ("waarschuwing",
                f"verkoopwaarde € {ons}/m² is {x}× het gemiddelde werkelijk betaalde peil in "
                f"kadasterzone {zone} (€ {hun}/m²) — controleer de vergelijkingsobjecten")
    if keer >= DREMPEL_OPMERKING:
        return ("opmerking",
                f"verkoopwaarde € {ons}/m² is {x}× het zonegemiddelde van het kadaster "
                f"(zone {zone}, € {hun}/m²). Voor een grondig gerenoveerd huis kan dat kloppen — "
                f"de module hoort bij een woning van {z.get('antiguedad')} jaar in gemiddelde staat")
    if keer < 1.0:
        return ("opmerking",
                f"verkoopwaarde € {ons}/m² ligt ónder het zonegemiddelde van het kadaster "
                f"(zone {zone}, € {hun}/m²) — de vergelijkingsreeks is hier mogelijk te laag")
    return None

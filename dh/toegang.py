"""Toegangscontrole voor het Deal Hunter-dashboard.

Waarom dit bestaat
------------------
Deal Hunter bevat maximale koopprijzen, weglooppunten en onderhandelplannen:
uitsluitend voor de eigenaar. Tot 25-09-2026 was de beveiliging het netwerk
(Tailscale, daarna alleen 127.0.0.1). Zodra de dienst via Cloudflare Tunnel
bereikbaar wordt, is dat niet genoeg meer.

Cloudflare Access blijft het slot aan de rand — dit is de tweede laag, voor het
geval een hostname ooit verkeerd staat of iemand op het lokale netwerk komt.
Let op: cloudflared verbindt zélf met 127.0.0.1, dus het clientadres is voor
tunnelverkeer en lokaal verkeer identiek. Onderscheid op IP kan daarom niet;
daarom een cookie.

Gedrag
------
- Geen `DH_WACHTWOORD_HASH` in de omgeving → de controle staat UIT en de dienst
  werkt precies als voorheen. Dat is bewust: het zet een draaiende dienst niet
  stil. Zet een wachtwoord met `python3 scripts/zet-wachtwoord.py`.
- Wel een hash → elk verzoek vereist een geldig cookie, behalve de inlogpagina
  en de statische bestanden die de webapp nodig heeft.

Alleen standaardbibliotheek; geen extra afhankelijkheden.
"""

from __future__ import annotations

import base64
import hashlib
import hmac
import os
import secrets
import time

COOKIE_NAAM = "dh_sessie"
GELDIG_SECONDEN = 90 * 24 * 3600  # 90 dagen: een webapp op het beginscherm
                                  # die elke dag opnieuw vraagt, wordt niet gebruikt.

# Paden die zonder inlog bereikbaar blijven. Bewust kort gehouden.
VRIJE_PADEN = ("/inloggen", "/static/", "/manifest.webmanifest", "/favicon.ico")

# Eenvoudige rem op raden: per adres vijf pogingen per kwartier, zoals in Tree AI OS.
_POGINGEN: dict[str, list[float]] = {}
MAX_POGINGEN = 5
POGING_VENSTER = 15 * 60


def _hash(wachtwoord: str, salt: bytes) -> bytes:
    """scrypt met parameters die op deze Mac ruim onder een seconde blijven."""
    return hashlib.scrypt(
        wachtwoord.encode("utf-8"), salt=salt, n=2**14, r=8, p=1, dklen=32
    )


def maak_hash(wachtwoord: str) -> str:
    """Geeft de regel die in .env hoort: scrypt$<salt>$<hash>, beide base64."""
    salt = secrets.token_bytes(16)
    digest = _hash(wachtwoord, salt)
    b64 = lambda b: base64.urlsafe_b64encode(b).decode("ascii").rstrip("=")  # noqa: E731
    return f"scrypt${b64(salt)}${b64(digest)}"


def _ontleed(opgeslagen: str) -> tuple[bytes, bytes] | None:
    try:
        soort, salt_b64, hash_b64 = opgeslagen.split("$")
        if soort != "scrypt":
            return None
        pad = lambda s: s + "=" * (-len(s) % 4)  # noqa: E731
        return (
            base64.urlsafe_b64decode(pad(salt_b64)),
            base64.urlsafe_b64decode(pad(hash_b64)),
        )
    except Exception:
        return None


def hash_uit_omgeving() -> str | None:
    """De opgeslagen hash, uit de omgeving of uit .env.

    `.env` wordt hier niet in `os.environ` geladen maar door `config.load_env()`
    in een dict gelezen; we kijken daarom op beide plekken. Bewust elke keer
    opnieuw lezen: zo werkt een wachtwoordwissel zonder de dienst te herstarten,
    en .env is klein.
    """
    waarde = (os.environ.get("DH_WACHTWOORD_HASH") or "").strip()
    if waarde:
        return waarde
    try:
        from . import config

        waarde = (config.load_env().get("DH_WACHTWOORD_HASH") or "").strip()
    except Exception:
        waarde = ""
    return waarde or None


def controle_actief() -> bool:
    """True zodra er een wachtwoord is ingesteld."""
    return hash_uit_omgeving() is not None


def klopt_wachtwoord(wachtwoord: str) -> bool:
    opgeslagen = hash_uit_omgeving()
    if not opgeslagen:
        return False
    ontleed = _ontleed(opgeslagen)
    if ontleed is None:
        return False
    salt, verwacht = ontleed
    return hmac.compare_digest(_hash(wachtwoord, salt), verwacht)


def _sleutel() -> bytes:
    """Ondertekensleutel, afgeleid van de opgeslagen hash.

    Zo is er geen tweede geheim nodig, en verlopen alle cookies vanzelf zodra
    het wachtwoord wijzigt.
    """
    return hashlib.sha256(
        (hash_uit_omgeving() or "").encode("utf-8") + b"dh-cookie-v1"
    ).digest()


def maak_cookie() -> str:
    verloopt = int(time.time()) + GELDIG_SECONDEN
    bericht = str(verloopt).encode("ascii")
    ondertekening = hmac.new(_sleutel(), bericht, hashlib.sha256).digest()
    b64 = lambda b: base64.urlsafe_b64encode(b).decode("ascii").rstrip("=")  # noqa: E731
    return f"{verloopt}.{b64(ondertekening)}"


def cookie_geldig(waarde: str | None) -> bool:
    if not waarde:
        return False
    try:
        verloopt_s, ondertekening_b64 = waarde.split(".", 1)
        verloopt = int(verloopt_s)
    except Exception:
        return False
    if verloopt < time.time():
        return False
    verwacht = hmac.new(_sleutel(), verloopt_s.encode("ascii"), hashlib.sha256).digest()
    pad = ondertekening_b64 + "=" * (-len(ondertekening_b64) % 4)
    try:
        gegeven = base64.urlsafe_b64decode(pad)
    except Exception:
        return False
    return hmac.compare_digest(verwacht, gegeven)


def te_veel_pogingen(adres: str) -> bool:
    nu = time.time()
    pogingen = [t for t in _POGINGEN.get(adres, []) if nu - t < POGING_VENSTER]
    _POGINGEN[adres] = pogingen
    return len(pogingen) >= MAX_POGINGEN


def noteer_poging(adres: str) -> None:
    _POGINGEN.setdefault(adres, []).append(time.time())


def wis_pogingen(adres: str) -> None:
    _POGINGEN.pop(adres, None)


def pad_is_vrij(pad: str) -> bool:
    return any(pad == p or pad.startswith(p) for p in VRIJE_PADEN)


# --- dienst-token ------------------------------------------------------------
#
# TREE Hub draait op dezelfde machine en laat de kansen zien op de telefoon.
# Dat is een programma en geen mens: het heeft geen browser en dus geen cookie.
# Daarom een gedeeld geheim in een kopregel.
#
# Bewust zo klein mogelijk gehouden:
#   - staat er geen DH_DIENST_TOKEN, dan bestaat deze weg niet. Geen token in
#     de omgeving betekent dat er niets te omzeilen valt.
#   - alleen lezen via /api/ — de token geeft geen toegang tot de pagina's en
#     is geen vervanging van het wachtwoord.
#   - vergelijken in vaste tijd, zodat de duur van het antwoord niet verraadt
#     hoeveel tekens klopten.

TOKEN_KOP = "x-dh-token"


def token_uit_omgeving() -> str | None:
    waarde = (os.environ.get("DH_DIENST_TOKEN") or "").strip()
    if waarde:
        return waarde
    try:
        from . import config

        waarde = (config.load_env().get("DH_DIENST_TOKEN") or "").strip()
    except Exception:
        waarde = ""
    return waarde or None


def token_klopt(gegeven: str | None) -> bool:
    verwacht = token_uit_omgeving()
    if not verwacht or not gegeven:
        return False
    return hmac.compare_digest(verwacht, gegeven)

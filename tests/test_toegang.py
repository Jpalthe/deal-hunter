"""Toegangscontrole: staat het slot dicht als er een wachtwoord is, en open als er geen is.

Het gedrag zonder wachtwoord is bewust: een draaiende dienst mag niet stilvallen
doordat er code bij komt. Maar zodra er een wachtwoord staat, moet elk pad dicht
zijn — ook de schrijvende endpoints, want daar zit het risico.
"""

from __future__ import annotations

import pytest
from fastapi.testclient import TestClient

from dh import toegang
from dh.dashboard import app

WACHTWOORD = "een-lang-genoeg-wachtwoord"


@pytest.fixture()
def zonder_wachtwoord(monkeypatch):
    monkeypatch.setattr(toegang, "hash_uit_omgeving", lambda: None)
    return TestClient(app)


@pytest.fixture()
def met_wachtwoord(monkeypatch):
    hash_ = toegang.maak_hash(WACHTWOORD)
    monkeypatch.setattr(toegang, "hash_uit_omgeving", lambda: hash_)
    toegang._POGINGEN.clear()
    return TestClient(app)


def test_zonder_wachtwoord_blijft_alles_bereikbaar(zonder_wachtwoord):
    """Anders zou het toevoegen van deze code de dienst stilzetten."""
    assert zonder_wachtwoord.get("/api/toegang").json() == {"beveiligd": False}
    assert zonder_wachtwoord.get("/", follow_redirects=False).status_code == 200


def test_met_wachtwoord_is_de_pagina_dicht(met_wachtwoord):
    antwoord = met_wachtwoord.get("/", follow_redirects=False)
    assert antwoord.status_code == 200
    assert "Wachtwoord" in antwoord.text          # de inlogpagina
    assert "Deal Hunter" in antwoord.text
    # En vooral: niet de inhoud van het dashboard.
    assert "listing" not in antwoord.text.lower()


def test_api_geeft_401_in_plaats_van_html(met_wachtwoord):
    """Een JSON-verzoek hoort een eerlijke 401 te krijgen, geen inlogpagina."""
    antwoord = met_wachtwoord.get("/api/summary")
    assert antwoord.status_code == 401
    assert antwoord.json() == {"error": "niet_aangemeld"}


def test_schrijvende_endpoints_zijn_dicht(met_wachtwoord):
    """Dit is het punt waar het echt om gaat: vijf endpoints kunnen schrijven."""
    for pad, methode in (
        ("/api/markeer", "post"),
        ("/api/review", "post"),
        ("/api/instellingen", "post"),
        ("/api/wachtwoord", "post"),
    ):
        antwoord = getattr(met_wachtwoord, methode)(pad, json={})
        assert antwoord.status_code == 401, f"{pad} stond open ({antwoord.status_code})"


def test_inloggen_en_daarna_binnen(met_wachtwoord):
    fout = met_wachtwoord.post("/inloggen", data={"wachtwoord": "verkeerd"})
    assert fout.status_code == 401
    assert "klopt niet" in fout.text

    goed = met_wachtwoord.post(
        "/inloggen", data={"wachtwoord": WACHTWOORD}, follow_redirects=False
    )
    assert goed.status_code == 303
    assert toegang.COOKIE_NAAM in goed.cookies

    # De client houdt het cookie vast; nu moet de API wél antwoorden.
    assert met_wachtwoord.get("/api/toegang").status_code == 200


def test_geknoeid_cookie_geeft_geen_toegang(met_wachtwoord):
    met_wachtwoord.post("/inloggen", data={"wachtwoord": WACHTWOORD})
    met_wachtwoord.cookies.set(toegang.COOKIE_NAAM, "9999999999.onzin")
    assert met_wachtwoord.get("/api/summary").status_code == 401


def test_verlopen_cookie_geeft_geen_toegang(met_wachtwoord):
    import base64
    import hashlib
    import hmac

    verlopen = "1000000000"  # ruim in het verleden
    sleutel = hashlib.sha256(
        (toegang.hash_uit_omgeving() or "").encode() + b"dh-cookie-v1"
    ).digest()
    ondertekening = hmac.new(sleutel, verlopen.encode(), hashlib.sha256).digest()
    b64 = base64.urlsafe_b64encode(ondertekening).decode().rstrip("=")
    assert toegang.cookie_geldig(f"{verlopen}.{b64}") is False


def test_inlogpagina_en_iconen_blijven_vrij(met_wachtwoord):
    """Zonder deze paden kun je niet inloggen en werkt de webapp niet."""
    assert met_wachtwoord.get("/inloggen").status_code == 200
    assert toegang.pad_is_vrij("/manifest.webmanifest")
    assert toegang.pad_is_vrij("/static/m.css")
    assert not toegang.pad_is_vrij("/api/summary")


def test_rem_op_raden(met_wachtwoord):
    for _ in range(toegang.MAX_POGINGEN):
        met_wachtwoord.post("/inloggen", data={"wachtwoord": "fout"})
    geblokkeerd = met_wachtwoord.post("/inloggen", data={"wachtwoord": WACHTWOORD})
    assert "Te veel pogingen" in geblokkeerd.text


def test_wachtwoord_wijzigen_vereist_het_oude(met_wachtwoord):
    met_wachtwoord.post("/inloggen", data={"wachtwoord": WACHTWOORD})
    zonder_oud = met_wachtwoord.post(
        "/api/wachtwoord", json={"nieuw": "nog-een-lang-wachtwoord"}
    )
    assert zonder_oud.status_code == 400
    te_kort = met_wachtwoord.post("/api/wachtwoord", json={"nieuw": "kort"})
    assert te_kort.status_code == 400

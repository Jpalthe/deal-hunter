"""Acceptatietests fase B (masterprompt §28): lege feed, prijswijziging, verdwenen, herpublicatie,
krimpbescherming, signalen met negatieve vorm, AEAT- en BOE-parsing op echte structuren."""
import json, sys, tempfile
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from dh import signals, config
from dh.store import Store
from dh.adapters import aeat, boe, bp


def _rec(ref, price, town="Javea", built=200, plot=1000, text="Villa para reformar con vistas", typ="Villa"):
    return {"source_ref": ref, "area": config.area_of(town), "town": config.norm_place(town), "town_raw": town, "postcode": None,
            "type": typ, "price": price, "currency": "EUR", "built_m2": built, "plot_m2": plot, "beds": 3, "baths": 2,
            "lat": None, "lon": None, "location_detail": "Montgo", "url": "https://x/" + ref, "title": "t", "desc_hash": "h" + text[:5],
            "desc_excerpt": text, "features": ["Pool"], "images_count": 3, "source_date": "2026-09-01", "new_build": 0,
            "_text": text, "_features": "Pool"}


def test_events_sequence():
    with tempfile.TemporaryDirectory() as d:
        s = Store(Path(d) / "t.sqlite")
        r1 = s.start_run("test")
        assert s.is_baseline(r1)
        lid, kind, _ = s.upsert_listing(r1, "bp", _rec("A1", 500000))
        assert kind == "NULMETING"
        s.upsert_listing(r1, "bp", _rec("B2", 700000))
        s.mark_gone(r1, "bp", {"A1", "B2"})
        s.finish_run(r1, "ok")
        r2 = s.start_run("test")
        assert not s.is_baseline(r2)
        _, k1, det = s.upsert_listing(r2, "bp", _rec("A1", 450000))
        assert k1 == "PRIJS GEWIJZIGD" and det["pct"] == -10.0
        _, k2, _ = s.upsert_listing(r2, "bp", _rec("C3", 600000))
        assert k2 == "NIEUW"
        gone = s.mark_gone(r2, "bp", {"A1", "C3"})
        assert len(gone) == 1
        r3 = s.start_run("test")
        _, k3, _ = s.upsert_listing(r3, "bp", _rec("B2", 700000))
        assert k3 == "OPNIEUW AANGEBODEN"
        assert [p for _, p in s.price_history(lid)] == [500000, 450000]
        s.close()


def test_area_and_signals():
    assert config.area_of("Javea") == "javea" and config.area_of("Jávea/Xàbia") == "javea"
    assert config.area_of("El Poble Nou de Benitatxell") == "benitachell" and config.area_of("Moraira") == "moraira"
    assert config.area_of("Denia") is None and config.area_of(None, "03730") == "javea"
    a = signals.analyse("Villa para reformar con gran potencial, licencia de obras concedida", "", "Villa")
    assert a["category"] == "renovatie" and a["licence_claims"]
    b = signals.analyse("Villa con reforma integral realizada en 2022, lista para entrar a vivir", "", "Villa")
    assert b["renovation_score"] == 0 and b["category"] == "overig"
    c = signals.analyse("Parcela urbana de 1.000 m2 con proyecto aprobado", "", "Land")
    assert c["category"] == "perceel"
    d = signals.analyse("Piso to renovate near the beach", "", "Apartment")
    assert d["category"] == "appartement-renovatie"


def test_aeat_parse_real_structure():
    js = ('/* Version: 20260914 15:23:07 */ const inmueblesSubasta = [{"id":"1","tipo":1,"subasta":"SUB-AT-2026-1","derecho":1,'
          '"porcTitularidad":25.0,"codProvincia":3,"direccion":"CL LLAC COMO 5, 03700 DENIA","refCatastro":"X","valoracion":40945.66,'
          '"cargas":0,"finSubasta":"2026-09-21","descripcion":"PISO","cru":"c","gpsLat":"38.84","gpsLong":"0.10","capital":"True",'
          '"interes":"1","municipioCod":"3063","cp":3700,"fotos":[]},{"id":"2","tipo":1,"subasta":"SUB-AT-2026-2","derecho":1,'
          '"porcTitularidad":100,"codProvincia":3,"direccion":"CL X 1, 03730 JAVEA","refCatastro":"Y","valoracion":100,"cargas":5000,'
          '"finSubasta":"2026-10-01","descripcion":"VIVIENDA","cru":"d","gpsLat":"38.79","gpsLong":"0.16","capital":"True","interes":"1",'
          '"municipioCod":"3082","cp":3730,"fotos":[]},{"id":"3","tipo":1,"subasta":"S","derecho":1,"porcTitularidad":100,"codProvincia":28,'
          '"direccion":"MADRID","valoracion":1,"cargas":0,"fotos":[]}]; const mueblesSubasta = [{"id":"m"}];')
    arr, version = aeat.parse(js)
    assert version.startswith("20260914") and len(arr) == 3
    sel = aeat.select(arr)
    assert len(sel) == 2
    denia, javea = sel
    assert denia["area"] is None and "onverdeeld aandeel: 25 %" in denia["blockers"] and denia["postcode"] == "03700"
    assert javea["area"] == "javea" and any("lasten" in b for b in javea["blockers"])


def test_boe_parse_real_structure():
    j = {"data": {"sumario": {"diario": [{"seccion": [
        {"codigo": "4", "nombre": "IV", "departamento": [
            {"codigo": "9603", "nombre": "TRIBUNALES DE INSTANCIA. SECCIÓN CIVIL", "item": [
                {"identificador": "BOE-B-2026-1", "titulo": "DENIA", "url_html": "https://www.boe.es/diario_boe/txt.php?id=BOE-B-2026-1"},
                {"identificador": "BOE-B-2026-2", "titulo": "ALBACETE", "url_html": "u2"}]}]},
        {"codigo": "5B", "nombre": "V-B", "departamento": [
            {"codigo": "9525", "nombre": "ADMINISTRACIÓN LOCAL", "item": {"identificador": "BOE-B-2026-3", "titulo": "SUMA GESTIÓN TRIBUTARIA. DIPUTACIÓN DE ALICANTE", "url_html": "u3"}}]},
        {"codigo": "1", "nombre": "I", "departamento": {"codigo": "1", "nombre": "MIN", "texto": {"epigrafe": [{"nombre": "e", "item": [{"identificador": "BOE-A-1", "titulo": "Resolución"}]}]}}},
    ]}]}}}
    items = boe.parse_sumario(j)
    ids = {i["boe_id"]: i["priority"] for i in items}
    assert ids == {"BOE-B-2026-1": 2, "BOE-B-2026-3": 2}
    assert boe.SUB_RE.findall("Subasta SUB-RC-2026-0026I20260030 y SUB-JA-2026-123456") == ["SUB-RC-2026-0026I20260030", "SUB-JA-2026-123456"]


def test_bp_normalise_and_shrink_guard():
    p = {"ref": "4676JAV", "date": "2026-09-01", "price": 505000, "type": "Land", "town": "Javea", "locationDetail": "Montgo-Ermita",
         "surface_area": None, "plotArea": 1570, "builtArea": None, "desc": {"en": "Plot with building permit"}, "features": [], "images": [], "url": {"en": "https://bp/x"}}
    r = bp.normalise(p)
    assert r["area"] == "javea" and r["plot_m2"] == 1570 and r["source_ref"] == "4676JAV"
    assert config.BP_SHRINK_ABORT_PCT == 30


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_"):
            fn(); print("ok", name)


def test_what_if_m2_scales_costs():
    """Review-bevinding 1: meer verkoopbaar m² bij renovatie moet ook bouwkosten verhogen."""
    from dh import feasibility
    import sqlite3
    con = sqlite3.connect(str(config.DB_PATH)); con.row_factory = sqlite3.Row
    row = con.execute("SELECT * FROM listings WHERE source='idealista' AND source_ref='112342245'").fetchone()
    if row is None:
        return  # database zonder kandidaten: niets te testen
    d = dict(row)
    base = feasibility.compute(d, {}, "R_integraal")
    s0 = next(s for s in base["scenarios"] if s["key"] == "R_integraal")
    bigger = feasibility.compute(d, {"result_m2": s0["result_m2"] + 100}, "R_integraal")
    s1 = next(s for s in bigger["scenarios"] if s["key"] == "R_integraal")
    build0 = next(b["eur"] for b in s0["breakdown"] if b["label"] == "Bouw en sloop")
    build1 = next(b["eur"] for b in s1["breakdown"] if b["label"] == "Bouw en sloop")
    assert s1["newbuild_m2"] == 100 and build1 > build0
    # override geldt alleen voor het gekozen scenario
    other = next(s for s in bigger["scenarios"] if s["key"] != "R_integraal")
    assert other["result_m2"] == other["base_result_m2"]


# ---------------------------------------------------------------- BORME en meldingen (18-09-2026)

BORME_XML = b"""<?xml version="1.0" encoding="UTF-8"?>
<documento><metadatos><identificador>BORME-A-2026-179-03</identificador></metadatos><texto>
<p class="articulo">415561 - GESTIO INMOBILIARIA LA FOIA SL.</p>
<p class="parrafo">Ceses/Dimisiones. Adm. Unico: NOMBRE APELLIDO. Liquidador: NOMBRE APELLIDO. Disolucion. Voluntaria. Extincion.  Datos registrales. S 8 , H A 35126, I/A 5 ( 9.09.26).</p>
<p class="articulo">415562 - PANADERIA DEL PUERTO SL.</p>
<p class="parrafo">Constitucion. Domicilio: C/ REI JAUME I 5 B (JAVEA). Capital: 3.000,00 Euros.  Datos registrales. S 8 , H A 208034, I/A 1 ( 9.09.26).</p>
<p class="articulo">415563 - HOSTELERIA MORAIRA SL.</p>
<p class="parrafo">Concurso. Declaracion de concurso de acreedores. Domicilio: MORAIRA.  Datos registrales. S 8 , H A 9 , I/A 2 ( 10.09.26).</p>
</texto></documento>"""


def test_borme_alleen_druksignalen_en_geen_persoonsgegevens():
    from datetime import date
    from dh.adapters import borme
    recs = borme.parse_province_xml(BORME_XML, "BORME-A-2026-179-03", "https://www.boe.es/x", date(2026, 9, 16))
    namen = [r["name"] for r in recs]
    assert "GESTIO INMOBILIARIA LA FOIA SL" in namen          # ontbinding + vastgoednaam
    assert "HOSTELERIA MORAIRA SL" in namen                    # faillissement
    assert "PANADERIA DEL PUERTO SL" not in namen              # alleen oprichting: geen signaal
    blob = json.dumps(recs, ensure_ascii=False)
    assert "NOMBRE APELLIDO" not in blob                       # nooit bestuurders of vereffenaars bewaren
    assert "Liquidador" not in blob
    foia = next(r for r in recs if r["name"].startswith("GESTIO"))
    assert foia["priority"] == 2 and foia["sector"] == "vastgoed of bouw"
    assert foia["published_on"] == "2026-09-09"
    mor = next(r for r in recs if r["name"].startswith("HOSTELERIA"))
    assert mor["area"] == "moraira" and "faillissement (concurso)" in mor["acts"]


def _item(i, cls, reliable=True, result=100000, price=600000, room=0.1, area="javea",
          category="renovatie", urbanisme=None):
    # prijs boven de ondergrens voor een pand (€ 500.000, kader 25-09-2026), anders valt het object
    # al op de prijs af en meet de test niet wat zij denkt te meten
    return {"id": i, "ref": f"R{i}", "class": cls, "reliable": reliable, "price": price, "room": room,
            "calc": {"result": result, "margin": 0.25}, "max_price": {"base": price * (1 + room)},
            "zone_label": "Centrum", "location": "x", "scenario": "s", "area": area,
            "category": category, "urbanisme": urbanisme}


def test_meldingen_categorie_en_herhaling():
    with tempfile.TemporaryDirectory() as d:
        from dh import alerts
        s = Store(Path(d) / "t.sqlite")
        run = s.start_run("test")
        items = [_item(1, "groen"), _item(2, "oranje"), _item(3, "grijs"),
                 _item(4, "blauw", reliable=False), _item(5, "blauw", result=-5000),
                 _item(6, "groen", area="moraira"),                 # ander tabblad: geen melding
                 _item(7, "groen", category="appartement"),         # geen renovatie of ombouw: geen melding
                 _item(9, "groen", category="perceel", price=150000),   # perceel telt gewoon mee
                 _item(10, "groen", urbanisme={"duiding": {"soort": "niet-urbaniseerbaar"}})]  # bestemming
        found = alerts.collect(s, items)
        # groen telt, en een perceel ook. Niet: onbetrouwbaar, verlies, een ander tabblad, de
        # verkeerde soort, of een vastgestelde niet-stedelijke bestemming.
        assert [i["id"] for i in found["direct"]] == [1, 9]
        assert [i["id"] for i in found["verzamel"]] == [2]
        # nulmeting: vastleggen, niet als melding versturen
        out = alerts.run(s, run, items, env={}, deliver=False)
        assert out["nulmeting"] == 3 and out["direct"] == 0
        # tweede ronde zonder verandering: niets nieuws
        assert alerts.run(s, run, items, env={}, deliver=False)["direct"] == 0
        # prijsdaling van meer dan 2 % meldt opnieuw
        zakker = _item(1, "groen", price=540000)      # 10 % onder de 600.000 van de nulmeting
        assert alerts.run(s, run, [zakker], env={}, deliver=False)["direct"] == 1
        # stijging van categorie meldt ook opnieuw
        assert alerts.run(s, run, [_item(2, "blauw", price=600000)], env={}, deliver=False)["direct"] == 1
        s.close()


# ---------------------------------------------------------------- makelaarssites (24-09-2026)

INMOWEB_PAGINA = """<html><head><title>Venta Casa adosada en Jávea</title>
<meta property="og:title" content="Venta Casa adosada en Jávea"><meta property="og:description" content="Casa adosada con jardín en Jávea, zona Pinosol."></head><body>
<nav>Buscar inmuebles <a>Venta</a> <a>Alquiler</a> Nº de referencia Indique la referencia Habitaciones >= 2 Baños 1 2 Precio: de a €</nav>
<div class="destacados"><p>Villa en Moraira 295.000 €</p></div>
<div class="ficha"><p>Nº de referencia: XC5500</p><p>Precio: 387.000€</p><p>Sup. Construida 229 m²</p><p>Sup. Parcela 752 m²</p>
<p>Habitaciones 4</p><p>Baños 1</p><p>Casa adosada con jardín en Jávea, zona Pinosol, a cinco minutos del centro. Necesita una actualización completa de cocina y baños pero la estructura está en buen estado y la orientación es sur.</p></div>
</body></html>"""


def test_makelaar_ontleed_leest_vanaf_de_referentie():
    from dh.adapters import makelaars as M
    k = M.Kantoor(naam="Test", website="https://www.example.com", host="example.com", toegestaan=True)
    r = M.ontleed(INMOWEB_PAGINA, "https://www.example.com/casa-adosada-en-javea-es1765350.html", k)
    assert r["source_ref"] == "XC5500"             # niet "Indique" uit het zoekformulier
    assert r["price"] == 387000                    # niet de 295.000 uit het blok met uitgelichte woningen
    assert r["built_m2"] == 229 and r["plot_m2"] == 752
    assert r["beds"] == 4 and r["baths"] == 1      # niet de filters ">= 2" en "1 2"
    assert r["type"] == "Town house" and r["area"] == "javea"
    assert r["_verhuur"] is False                  # "Alquiler" in het menu maakt het geen verhuur
    huur = M.ontleed(INMOWEB_PAGINA.replace("Venta Casa adosada", "Alquiler Casa adosada"),
                     "https://www.example.com/x-es1.html", k)
    assert huur["_verhuur"] is True


def test_makelaar_portaalvergelijking():
    from dh import import_makelaars as I
    kand = [{"id": 1, "source": "idealista-zoek", "source_ref": "110285200", "area": "javea", "price": 387000, "built_m2": 229, "plot_m2": 750, "type": "Town house"},
            {"id": 2, "source": "bp", "source_ref": "1234JAV", "area": "javea", "price": 900000, "built_m2": 300, "plot_m2": 1200, "type": "Villa"}]
    rec = {"area": "javea", "price": 387000, "built_m2": 229, "plot_m2": 752, "type": "Town house"}
    m = I.zoek_op_portaal(rec, kand)
    assert m and m["ref"] == "110285200" and m["score"] == 2
    assert I.zoek_op_portaal({"area": "javea", "price": 386000, "built_m2": 120, "plot_m2": None, "type": "Apartment"}, kand) is None
    assert I.zoek_op_portaal({"area": "moraira", "price": 387000, "built_m2": 229, "plot_m2": 752, "type": "Town house"}, kand) is None


# ---------------------------------------------------------------- focus, renovatie, perceel (25-09-2026)

def test_focus_tabbladen():
    """Het tabblad volgt uit gebied, soort en bestemming.

    De grenzen worden hier expliciet meegegeven en niet uit `investeringskader.json` gelezen: anders
    toetst deze test de instelling van vandaag in plaats van de logica. Jan haalde de prijsgrenzen er
    op 25-09 weer uit; die wijziging mag deze test niet laten omvallen."""
    from dh import focus
    met_grenzen = {**focus.STANDAARD, "ondergrens_perceel": 100000, "ondergrens_pand": 500000}
    stedelijk = {"duiding": {"soort": "stedelijk"}}
    rustiek = {"duiding": {"soort": "niet-urbaniseerbaar"}}
    urbaniseerbaar = {"duiding": {"soort": "urbaniseerbaar"}}
    geval = [
        ({"area": "javea", "category": "renovatie", "price": 600000}, None, focus.KANSEN),
        ({"area": "javea", "category": "renovatie", "price": 300000}, None, None),          # onder € 500.000
        ({"area": "javea", "category": "perceel", "price": 150000}, None, focus.KANSEN),    # boven € 100.000
        ({"area": "javea", "category": "perceel", "price": 80000}, None, None),
        # Jan 25-09-2026: op 'misschien later' hoort alleen wat ooit bebouwd mág worden.
        ({"area": "javea", "category": "perceel", "price": 150000}, rustiek, None),
        ({"area": "javea", "category": "perceel", "price": 150000}, urbaniseerbaar, focus.LATER),
        ({"area": "javea", "category": "perceel", "price": 150000}, stedelijk, focus.KANSEN),
        ({"area": "moraira", "category": "renovatie", "price": 700000}, None, focus.BUITEN),
        ({"area": "javea", "category": "villa-gewoon", "price": 900000}, None, None),       # geen renovatieobject
        # sloop en nieuwbouw telt altijd mee, ook als de voorfilter het een gewone woning noemt
        ({"area": "javea", "category": "villa-gewoon", "price": 900000, "scenario": "sloop en nieuwbouw"}, None, focus.KANSEN),
        # Zonder prijs valt nog steeds niets áf — maar sinds 27-09-2026 hoort zo'n object op een
        # eigen tabblad in plaats van tussen de kansen. Aanleiding: 819 objecten bleken een prijs
        # uit een zoekfilter te dragen; die prijzen zijn weggestreept en dan blijft er niets te
        # rekenen over. Weggooien is erger, want de advertentie bestaat wel (besluit Jan).
        ({"area": "javea", "category": "renovatie", "price": None, "type": "Villa"}, None, focus.ONVOLLEDIG),
        ({"area": "moraira", "category": "renovatie", "price": None, "type": "Apartment"}, None, focus.ONVOLLEDIG),
        # De categorie telt hier bewust níet mee: die wordt mede uit de prijs afgeleid, dus zodra de
        # prijs is weggestreept valt een object terug op "overig". Zou de categorie gelden, dan
        # verdween juist wat wij zichtbaar wilden houden (240 villa's op 27-09-2026).
        ({"area": "javea", "category": "overig", "price": None, "type": "Villa"}, None, focus.ONVOLLEDIG),
        # het soort telt wél: een winkelpand of een garage hoort er ook zonder prijs niet bij
        ({"area": "javea", "category": "overig", "price": None, "type": "Commercial"}, None, None),
        ({"area": "javea", "category": "renovatie", "price": None}, None, None),   # soort onbekend
        # buiten het werkgebied blijft het ook zonder prijs buiten beeld
        ({"area": "denia", "category": "renovatie", "price": None, "type": "Villa"}, None, None),
    ]
    for item, urb, verwacht in geval:
        assert focus.tab(item, urb, met_grenzen) == verwacht, (item, urb)
    # een niet opgevraagde bestemming is geen afwijzing
    assert focus.tab({"area": "javea", "category": "perceel", "price": 150000}, None, met_grenzen) == focus.KANSEN
    # zonder grenzen (de keuze van Jan, 25-09) valt niets meer op de prijs af
    # met de oudere regel bleef rustieke grond wél op het tabblad staan
    ruim = {**met_grenzen, "later_alleen_urbaniseerbaar": False}
    assert focus.tab({"area": "javea", "category": "perceel", "price": 150000}, rustiek, ruim) == focus.LATER
    zonder = {**focus.STANDAARD, "ondergrens_perceel": None, "ondergrens_pand": None, "bovengrens": None}
    assert focus.tab({"area": "javea", "category": "renovatie", "price": 45000}, None, zonder) == focus.KANSEN
    assert focus.tab({"area": "javea", "category": "renovatie", "price": 9000000}, None, zonder) == focus.KANSEN


def test_kader_is_leesbaar():
    """Het kader dat nu in de map staat moet te lezen zijn en de drie tabbladen kennen."""
    from dh import focus
    focus.instelling.cache_clear()
    f = focus.instelling()
    assert "javea" in [g.lower() for g in f["gebieden"]]
    assert f["categorieen"], "zonder categorieën valt alles in de hoofdlijst"
    for sleutel in ("ondergrens_perceel", "ondergrens_pand", "bovengrens"):
        assert sleutel in f


def test_renovatie_vier_kenmerken():
    from dh import renovatie
    comps = {"tosalet_adsubia": {"villa_renovated": {"p25": 3900}}}
    it = {"price": 480000, "built_m2": 160, "plot_m2": 1200, "zone": "tosalet_adsubia", "type": "villa"}
    vol = renovatie.beoordeel(it, {"year": 1979}, {"renovation_signals": ["para reformar"]}, comps,
                              tekst="Villa para reformar")
    assert vol["punten"] == 4 and vol["waardig"]
    # een pand dat net verbouwd is, telt niet als oud en niet aangepakt — ook niet in de
    # vrouwelijke Spaanse vorm, waar de eerste versie van dit patroon overheen las
    for woord in ("recién reformada", "reformado", "renovada", "fully renovated"):
        r = renovatie.beoordeel({"price": 900000, "built_m2": 200, "plot_m2": 400, "zone": "centro"},
                                {"year": 1980}, {}, comps, tekst=f"Villa {woord} con piscina")
        assert r["verbouwd_geclaimd"], woord
        assert "Gebouwd in" not in " ".join(r["redenen"]), woord
    # groot perceel, klein huis telt op zichzelf
    r = renovatie.beoordeel({"price": 9e6, "built_m2": 100, "plot_m2": 1000, "zone": "centro"}, None, {}, comps)
    assert r["punten"] == 1 and "ruimte over" in r["redenen"][0]


def test_perceel_vastgesteld_en_tegenspraak():
    """Een advertentie voor kale grond op een perceel waar het kadaster een huis ziet staan, is geen
    vastgesteld perceel. Zonder die toets kwam er een fiscale waarschuwing van vier ton uit lucht."""
    from dh import summary
    grond = {"plot_m2": 1500, "built_m2": None}
    bebouwd_perceel = {"distance_m": 0.0, "plot_m2": 1513, "built_m2": 304, "year": 2006}
    assert not summary.perceel_is_het_object(grond, bebouwd_perceel)
    assert summary.tegenspraak(grond, bebouwd_perceel)[0].startswith("Aangeboden als grond")
    # klopt het wel, dan is het perceel vastgesteld en is er geen tegenspraak
    huis = {"plot_m2": 800, "built_m2": 220}
    goed = {"distance_m": 3.0, "plot_m2": 820, "built_m2": 240}
    assert summary.perceel_is_het_object(huis, goed)
    assert summary.tegenspraak(huis, goed) == []
    # een perceel dat vele malen groter is, is een verkeerde koppeling en geen tegenspraak
    reus = {"distance_m": 0.0, "plot_m2": 529708, "built_m2": 0}
    assert not summary.perceel_is_het_object({"plot_m2": 809, "built_m2": None}, reus)
    assert summary.tegenspraak({"plot_m2": 809, "built_m2": None}, reus) == []
    # te ver weg: niets vaststellen en niets beweren
    assert not summary.perceel_is_het_object(huis, {**goed, "distance_m": 60})
    assert summary.tegenspraak(huis, {**goed, "distance_m": 60}) == []


def test_fiscale_waarschuwing():
    from dh import summary
    assert summary.fiscale_waarschuwing(300000, 250000, 1) is None       # fiscale waarde eronder
    assert summary.fiscale_waarschuwing(300000, 340000, 3) is None       # meerdere eenheden zegt niets
    w = summary.fiscale_waarschuwing(300000, 340000, 1)
    assert w["verschil"] == 40000 and w["extra_belasting"] == 4000
    assert "€ 40.000" in w["tekst"]


def test_markeringen():
    from dh import goolzoom  # noqa: F401 — tabel wordt door de store zelf aangemaakt
    with tempfile.TemporaryDirectory() as d:
        s = Store(Path(d) / "t.sqlite")
        s.markeer(7, "boeiend")
        assert s.markeringen()[7]["merk"] == "boeiend"
        s.markeer(7, "gebeld")                       # overschrijven, niet stapelen
        assert s.markeringen()[7]["merk"] == "gebeld" and len(s.markeringen()) == 1
        s.markeer(7, "geen")
        assert s.markeringen() == {}
        try:
            s.markeer(7, "onzin")
            raise AssertionError("onbekend merk had geweigerd moeten worden")
        except ValueError:
            pass
        s.close()


def test_goolzoom_duiding():
    from dh import goolzoom
    assert goolzoom.duiding("SU")["wonen"] == "ja"
    assert goolzoom.duiding("SUZ")["wonen"] == "voorwaardelijk"
    assert goolzoom.duiding("SNU-C")["wonen"] == "nee"
    assert goolzoom.duiding("SNU-P")["wonen"] == "nee"
    assert goolzoom.duiding("ZOMAARWAT")["wonen"] == "onbekend"
    assert goolzoom.duiding(None)["soort"] is None


def test_overzichtspagina_is_geen_woning():
    """Zoek- en categoriepagina's zagen eruit als een woning: zelfde woorden in de URL, en een prijs
    uit het zoekfilter. Zo kwamen er 32 spookobjecten van € 50.000 in de database."""
    from dh.adapters.makelaars import is_overzichtspagina
    geen_woning = [
        ("https://www.javeahouses.com/busqueda-propiedades/page/13/", "Búsqueda Propiedades – Página 13"),
        ("https://www.javeahouses.com/busqueda-propiedades/?view=list", "Búsqueda Propiedades"),
        ("https://www.javeahouses.com/property-type/casa-adosada/", "Casa adosada – Inmobiliaria"),
        ("https://x.com/propiedades/?orderby=price", "Villas – x"),
    ]
    for url, titel in geen_woning:
        assert is_overzichtspagina(url, titel), url
    wel_woning = [
        ("https://www.inmovillasjavea.com/en/property/sale-javea-villa-549386", "Villa in Tosalet with sea views"),
        ("https://x.com/venta/chalet-es123456.html", "Chalet de 4 dormitorios en Jávea"),
        ("https://x.com/property/villa-montgo-ref-4410", "Villa Montgó ref 4410"),
    ]
    for url, titel in wel_woning:
        assert not is_overzichtspagina(url, titel), url


def test_openingsbod_stapelt_geen_twee_kortingen():
    """Het openingsbod hoort dicht bij wat de deal draagt te liggen, niet twee kortingen daaronder.

    Twee fouten zaten hier achter elkaar. Eerst stond de streefprijs óp het voorzichtige scenario,
    waardoor er op een villa van € 533.000 een bod van € 78.000 uitkwam. Daarna bleef er nog een
    stapeling over: 90 % van wat de deal draagt, en daar nog eens 92 % van. Jan 26-09-2026: "openen
    op € 222.000 bij een vraagprijs van € 338.000 is 35 % eronder, zo worden wij niet serieus
    genomen"."""
    from dh import negotiation
    p = negotiation.plan({"price": 533000},
                         {"available": True, "max_price": {"base": 380000, "conservative": 85000}})
    assert p["walk_away"] == 380000
    # hoogstens een bescheiden stap onder het weglooppunt, niet twee kortingen
    assert p["opening"] >= 380000 * 0.93, p["opening"]
    assert p["opening"] <= p["target"] <= p["walk_away"]
    # het object uit Jans voorbeeld: vraagprijs 338.000, de deal draagt 268.000
    j = negotiation.plan({"price": 338000},
                         {"available": True, "max_price": {"base": 268000, "conservative": 136000}})
    assert j["opening"] >= 250000, j["opening"]          # was € 222.000
    assert j["opening"] / 338000 - 1 > -0.27              # was -34 %
    assert round(j["kloof_pct"], 2) == 0.21               # de vraagprijs staat 21 % te hoog
    # past de vraagprijs al binnen wat de deal draagt, dan onderhandel je een gewone korting
    q = negotiation.plan({"price": 500000},
                         {"available": True, "max_price": {"base": 600000, "conservative": 520000}})
    assert q["walk_away"] == 500000 and q["opening"] == 450000
    # boven de vraagprijs wordt nooit geboden
    assert q["opening"] < 500000 and q["target"] <= 500000


def test_kloof_te_groot_is_geen_bod():
    """Draagt de deal maar een fractie van de vraagprijs, dan is een openingsbod een verzinsel.
    Eén object droeg € 5.000 op een vraagprijs van € 169.000; de app bood daar 3 % van de vraagprijs."""
    from dh import negotiation
    p = negotiation.plan({"price": 169000},
                         {"available": True, "max_price": {"base": 5000, "conservative": 3000}})
    assert p["kloof_te_groot"] and p["kloof_tekst"]
    q = negotiation.plan({"price": 533000},
                         {"available": True, "max_price": {"base": 380000, "conservative": 85000}})
    assert not q["kloof_te_groot"] and q["kloof_tekst"] is None


# ---------------------------------------------------------------- financiering en doorlooptijd (25-09-2026)

def _rekenmodule():
    import importlib.util, sys as _sys
    spec = importlib.util.spec_from_file_location("haalbaarheid_test", Path(__file__).resolve().parents[1] / "tools" / "haalbaarheid.py")
    mod = importlib.util.module_from_spec(spec)
    _sys.modules["haalbaarheid_test"] = mod          # dataclass heeft de module in sys.modules nodig
    spec.loader.exec_module(mod)
    return mod


def test_doorlooptijd_uit_drie_blokken():
    """Jan 25-09-2026: vergunning, bouw en verkoop apart. Het totaal is daarvan afgeleid."""
    h = _rekenmodule()
    sc = h.Scenario(key="R", label="renovatie", kind="renovatie", renovation_m2=200, result_m2=200,
                    permit_months=0, build_months=6, sale_months=3)
    assert sc.months == 9
    nb = h.Scenario(key="N", label="nieuwbouw", kind="nieuwbouw", newbuild_m2=300, result_m2=300,
                    permit_months=5, build_months=12, sale_months=3)
    assert nb.months == 20
    # zonder de blokken blijft het oude vaste getal staan
    oud = h.Scenario(key="O", label="oud", kind="renovatie", renovation_m2=100, result_m2=100, months=15)
    assert oud.months == 15


def test_rente_over_aankoop_en_bouw():
    """100 % geleend: rente over aankoop vanaf dag één, over de bouw gemiddeld de helft."""
    h = _rekenmodule()
    p = {"finance_rate_default": 0.15, "finance_fee_pct": 0.0}
    sc = h.Scenario(key="N", label="n", kind="nieuwbouw", newbuild_m2=300, result_m2=300,
                    permit_months=5, build_months=12, sale_months=3)
    f = h.financing(400000, 50000, 600000, sc, p)
    # aankoop: 450.000 × 15 % × 20/12 = 112.500
    assert round(f["on_purchase"]) == 112500, f["on_purchase"]
    # bouw: 600.000 × 15 % × 12/12 / 2 = 45.000
    assert round(f["on_build"]) == 45000, f["on_build"]
    assert round(f["total"]) == 157500
    # het tarief is per project te wijzigen (Jan werkt met meerdere investeerders)
    half = h.financing(400000, 50000, 600000, sc, p, rate=0.075)
    assert round(half["total"]) == round(f["total"] / 2)
    # nul procent kost niets
    assert h.financing(400000, 50000, 600000, sc, p, rate=0.0)["total"] == 0


def test_grondwerk_op_een_helling():
    h = _rekenmodule()
    p = {"earthworks_light_eur": 15000, "earthworks_steep_eur": 50000}
    maak = lambda helling: h.Scenario(key="X", label="x", kind="nieuwbouw", newbuild_m2=200,
                                      result_m2=200, slope=helling)
    assert h.earthworks(maak(None), p) == 0        # niet vastgesteld: niets rekenen
    assert h.earthworks(maak("vlak"), p) == 0
    assert h.earthworks(maak("licht"), p) == 15000
    assert h.earthworks(maak("steil"), p) == 50000


def test_rente_drukt_de_maximale_koopprijs():
    """Duurder geld betekent dat je minder kunt betalen voor hetzelfde object."""
    h = _rekenmodule()
    k = {"rendementseis_op_projectkosten": 0.25, "doorlooptijd_max_maanden": 24,
         "bouwkosten_eur_per_m2": {"renovatie": 1000, "nieuwbouw": 2000},
         "verkoop_via_eigen_kantoor": True}
    p = json.loads((Path(__file__).resolve().parents[1] / "kader" / "parameters.json").read_text())["values"]
    sc = h.Scenario(key="N", label="n", kind="nieuwbouw", newbuild_m2=300, result_m2=300,
                    permit_months=5, build_months=12, sale_months=3, vat_recoverable=True)
    goedkoop = h.max_price(sc, 1_500_000, k, p, False, 0.25, finance_rate=0.05)
    duur = h.max_price(sc, 1_500_000, k, p, False, 0.25, finance_rate=0.20)
    assert goedkoop > duur, (goedkoop, duur)
    # en de rente zit werkelijk in de kosten
    r = h.project(500_000, sc, 1_500_000, k, p, False, finance_rate=0.15)
    assert r["financing"]["total"] > 0
    assert r["financing"]["per_month"] > 0
    zonder = h.project(500_000, sc, 1_500_000, k, p, False, finance_rate=0.0)
    assert r["total_costs"] > zonder["total_costs"]
    assert r["result"] < zonder["result"]


def test_toelichting_maakt_niet_onbetrouwbaar():
    """Een opmerking over de kostenbasis mag de hele som niet als onbetrouwbaar bestempelen.
    Daarop vielen eerder goede renovaties uit de ranglijst."""
    from dh import feasibility
    import inspect
    bron = inspect.getsource(feasibility)
    assert '"notes": notities' in bron, "de toelichtingen horen apart van de waarschuwingen"
    assert '"reliable": not warnings' in bron, "alleen waarschuwingen bepalen de betrouwbaarheid"


def test_de_drie_kostengroepen_tellen_op():
    """Aankoop plus bouw plus overig moet gelijk zijn aan de totale kosten.

    Toen rente en grondwerk erbij kwamen, klopte dat niet meer: de app toonde vier bedragen die
    samen niet uitkwamen op wat er werkelijk uitgegeven wordt."""
    from dh import feasibility
    from dh.store import Store
    s = Store()
    try:
        rijen = s.con.execute(
            "SELECT * FROM listings WHERE gone_at IS NULL AND price IS NOT NULL LIMIT 40").fetchall()
        gecontroleerd = 0
        for r in rijen:
            res = feasibility.compute(dict(r))
            for sc in res.get("scenarios", []):
                c = sc.get("sum")
                if not c:
                    continue
                opgeteld = c["acquisition"] + c["build"] + c["other"]
                assert abs(opgeteld - c["total_costs"]) <= 3, (sc["key"], opgeteld, c["total_costs"])
                assert c["result"] == round(c["sale"] - c["total_costs"]) or abs(
                    c["result"] - (c["sale"] - c["total_costs"])) <= 3
                gecontroleerd += 1
        assert gecontroleerd > 0, "geen enkel scenario gecontroleerd"
    finally:
        s.close()


def test_hoogte_projectie_en_helling():
    """De omzetting naar UTM en de hellingberekening, zonder netwerk.

    De projectie is met de hand uitgeschreven omdat pyproj hier niet geïnstalleerd is; daarom wordt
    hij tegen een bekend punt gelegd. Het kadaster geeft voor perceel 5246308BC5954N in Jávea een
    zwaartepunt rond 38,78 N / 0,17 O; dat hoort in zone 30N rond x = 776.500, y = 4.295.400."""
    from dh import hoogte
    x, y = hoogte.naar_utm30(0.1735161608, 38.782446298)
    assert 770000 < x < 782000, x
    assert 4290000 < y < 4300000, y
    # de projectie moet omkeerbaar consistent zijn: 5 m naar het oosten is ongeveer 5 m in x
    x2, _ = hoogte.naar_utm30(0.1735161608 + 5 / (111320 * 0.78), 38.782446298)
    assert 4.0 < (x2 - x) < 6.0, x2 - x

    # een vlak raster geeft helling nul, een schuin raster geeft de verwachte helling
    vlak = {"ncols": 3, "nrows": 3, "x0": 0.0, "y0": 0.0, "cell": 5.0, "nodata": -9999.0,
            "z": [[10.0] * 3 for _ in range(3)]}
    assert hoogte.hellingen(vlak, [])[0] == 0.0
    # 1 meter stijging per 5 meter naar het oosten = 20 %
    schuin = {"ncols": 3, "nrows": 3, "x0": 0.0, "y0": 0.0, "cell": 5.0, "nodata": -9999.0,
              "z": [[0.0, 1.0, 2.0]] * 3}
    assert abs(hoogte.hellingen(schuin, [])[0] - 0.20) < 0.001
    # drempels
    assert hoogte.oordeel(0.05) == "vlak"
    assert hoogte.oordeel(0.10) == "licht"
    assert hoogte.oordeel(0.30) == "steil"
    assert hoogte.oordeel(None) is None


def test_asc_lezen():
    """Het antwoord van de hoogtedienst is een ASCII-grid in een multipart-bericht."""
    from dh import hoogte
    tekst = ("--wcs\r\nContent-Type: text/plain\r\n\r\n"
             "ncols        3\n"
             "nrows        2\n"
             "xllcorner    776520.000000000000\n"
             "yllcorner    4295435.000000000000\n"
             "cellsize     5.000000000000\n"
             "NODATA_value -9999\n"
             " 12.031 12.380 12.995\n"
             " 13.001 13.100 13.200\n"
             "--wcs--\r\n")
    r = hoogte.lees_asc(tekst)
    assert r["ncols"] == 3 and r["nrows"] == 2
    assert r["cell"] == 5.0 and r["x0"] == 776520.0
    assert r["z"][0][0] == 12.031 and r["z"][1][2] == 13.200
    assert hoogte.lees_asc("geen grid hier") is None


def test_helling_telt_alleen_bij_een_vastgesteld_perceel():
    """Een ático van 20 m² boven een sportcomplex van 1.949 m² krijgt geen grondwerktoeslag."""
    from dh import perceel
    atico = {"plot_m2": None, "built_m2": 20}
    complex_eronder = {"distance_m": 0.0, "plot_m2": 1949, "built_m2": 1200}
    assert not perceel.perceel_is_het_object(atico, complex_eronder)
    echt = {"plot_m2": 1600, "built_m2": 250}
    eigen = {"distance_m": 2.0, "plot_m2": 1622, "built_m2": 260}
    assert perceel.perceel_is_het_object(echt, eigen)


def test_grond_is_hetzelfde_is_losser_dan_de_fiscale_toets():
    """Voor de helling telt of het dezelfde grond is; voor de fiscale waarde of het hetzelfde object is.

    Een perceel dat als grond te koop staat terwijl het kadaster er een schuur ziet, is fiscaal niet
    vastgesteld maar landschappelijk wel dezelfde helling."""
    from dh import perceel
    grond = {"plot_m2": 1840, "built_m2": None, "category": "perceel", "type": "Land"}
    met_schuur = {"distance_m": 1.0, "plot_m2": 1900, "built_m2": 334}
    assert not perceel.perceel_is_het_object(grond, met_schuur)   # fiscaal: niet vastgesteld
    assert perceel.grond_is_hetzelfde(grond, met_schuur)          # helling: wel dezelfde grond
    # een appartement koopt de helling eronder niet
    atico = {"plot_m2": None, "built_m2": 20, "category": "appartement-renovatie", "type": "Apartment"}
    assert not perceel.grond_is_hetzelfde(atico, {"distance_m": 0.0, "plot_m2": 1949, "built_m2": 1200})
    # een perceel dat vele malen groter is, is een andere lap grond
    assert not perceel.grond_is_hetzelfde({"plot_m2": 800, "category": "perceel"},
                                          {"distance_m": 0.0, "plot_m2": 529708})
    # te ver van de pin: niets vaststellen
    assert not perceel.grond_is_hetzelfde(grond, {**met_schuur, "distance_m": 80})


def test_env_schrijven_is_beperkt_en_veilig():
    """Het instellingenscherm schrijft in .env. Dat mag alleen voor een vaste lijst sleutels,
    bestaande regels blijven staan, en de rechten blijven 600."""
    from dh import config
    with tempfile.TemporaryDirectory() as d:
        p = Path(d) / "t.env"
        p.write_text("GOOLZOOM_API_KEY=blijf-van-mij-af\nDH_EMAIL_TO=oud@x.nl\n", encoding="utf-8")
        config.save_env_key("DH_EMAIL_TO", "nieuw@x.nl", p)
        config.save_env_key("DISCORD_WEBHOOK_URL", "https://discord.com/api/webhooks/1/abc", p)
        tekst = p.read_text(encoding="utf-8")
        assert "GOOLZOOM_API_KEY=blijf-van-mij-af" in tekst       # andere sleutels blijven ongemoeid
        assert "DH_EMAIL_TO=nieuw@x.nl" in tekst
        assert tekst.count("DH_EMAIL_TO=") == 1                   # geen dubbele regels
        assert "DISCORD_WEBHOOK_URL=https://discord.com/api/webhooks/1/abc" in tekst
        assert oct(p.stat().st_mode & 0o777) == "0o600"
        # wissen laat de regel leeg achter, niet verdwijnen
        config.save_env_key("DISCORD_WEBHOOK_URL", "", p)
        assert "DISCORD_WEBHOOK_URL=" in p.read_text(encoding="utf-8")
        # een sleutel buiten de lijst wordt geweigerd
        for verboden in ("PATH", "AWS_SECRET", "GOOLZOOM_API_KEY"):
            try:
                config.save_env_key(verboden, "x", p)
                raise AssertionError(f"{verboden} had geweigerd moeten worden")
            except ValueError:
                pass
        # een waarde met een nieuwe regel zou een tweede sleutel kunnen smokkelen
        try:
            config.save_env_key("DH_EMAIL_TO", "a@b.nl\nPATH=/kwaad", p)
            raise AssertionError("een nieuwe regel in de waarde had geweigerd moeten worden")
        except ValueError:
            pass


def test_webhookvorm_weigert_wat_geen_webhook_is():
    """Een bot-token of een halve link mag niet als webhook in .env belanden."""
    from dh import dashboard
    goed = "https://discord.com/api/webhooks/1234567890123/" + "x" * 40
    assert dashboard.WEBHOOK_VORM.match(goed)
    for slecht in ("hallo", "https://discord.com/api/webhooks/kort",
                   "MTIzNDU2.Gabcde.bot-token-achtig", "http://discord.com/api/webhooks/1/" + "x" * 40,
                   "https://example.com/api/webhooks/1/" + "x" * 40):
        assert not dashboard.WEBHOOK_VORM.match(slecht), slecht


# ---------------------------------------------------------------- gevonden op 26-09-2026

def test_bedrijfsovername_is_geen_vastgoedkoop():
    """Een traspaso is de overname van een lopend bedrijf. Drie daarvan stonden als villa van € 500
    tot € 2.900 boven aan de lijst omdat de prijs zo laag was."""
    for tekst in ("Se traspasa restaurante en pleno corazon del casco antiguo de Javea",
                  "LOCAL EN TRASPASO ARENAL JAVEA junto al Paseo David Ferrer",
                  "Traspaso de negocio con licencia en vigor"):
        r = signals.analyse(tekst)
        assert r["geen_koop"], tekst
        assert r["category"] == "geen-koop", (tekst, r["category"])
    # een gewone woning blijft gewoon een woning
    r = signals.analyse("Villa para reformar con vistas al mar")
    assert not r["geen_koop"] and r["category"] == "renovatie"


def test_niet_verkavelde_grond_ook_in_het_duits_en_engels():
    """Makelaars in Jávea publiceren in vier talen. 'Zu urbanisieren' betekent precies wat Jan hard
    uitsluit, en werd niet herkend omdat er alleen Spaanse patronen stonden."""
    for tekst in ("Baugrundstueck in Pinomar zu urbanisieren",
                  "Building plot to be urbanised in Javea",
                  "Plot pending urbanisation", "Grundstueck nicht erschlossen"):
        assert signals.analyse(tekst)["not_urbanised_signals"], tekst
    assert not signals.analyse("Bouwkavel in een afgeronde urbanisatie")["not_urbanised_signals"]


def test_titel_telt_mee_bij_het_herberekenen():
    """Het beslissende woord staat vaak in de titel, niet in de omschrijving. Bij makelaarssites is
    de omschrijving soms zelfs de cookiemelding van de site."""
    import inspect
    from dh import reanalyse
    bron = inspect.getsource(reanalyse)
    assert 'r["title"]' in bron, "de titel hoort mee te gaan naar de signaalanalyse"
    # en de herberekening mag makelaarsobjecten niet overslaan
    assert 'startswith("makelaar:")' in bron, "makelaarsobjecten horen ook opnieuw langs de signalen"
    # de titel alleen is genoeg om het te herkennen
    alleen_titel = signals.analyse("Baugrundstueck in Pinomar zu urbanisieren")
    assert alleen_titel["not_urbanised_signals"]


# ---------------------------------------------------------------- keuzes van Jan, 26-09-2026

def test_dubbele_woning_wordt_een_kaartje():
    from dh import dubbel
    idealista = {"id": 1, "area": "javea", "price": 340000, "plot_m2": 900, "lat": 38.7,
                 "source": "idealista", "ref": "A", "first_seen": "2026-09-01"}
    kantoor = {"id": 2, "area": "javea", "price": 341000, "plot_m2": 920, "lat": None,
               "source": "makelaar:y.com", "ref": "B", "first_seen": "2026-09-20", "kantoor": "Y"}
    ander = {"id": 3, "area": "javea", "price": 500000, "plot_m2": 900, "source": "bp", "ref": "C"}
    uit = dubbel.voeg_samen([idealista, kantoor, ander])
    assert len(uit) == 2
    hoofd = next(x for x in uit if x["ref"] == "A")          # die met coördinaat wordt de hoofdregel
    assert hoofd["bronnen"] == 2 and hoofd["ook_bij"][0]["bron"] == "Y"
    assert hoofd["prijsverschil_tussen_bronnen"] == 1000

    # Twee advertenties bij hetzelfde kantoor zijn twee woningen, geen dubbeling. Zonder deze regel
    # werden tien appartementen van xabiacasa.com met dezelfde prijs tot één kaartje geplakt.
    zelfde_kantoor = [{"id": n, "area": "javea", "price": 230000, "built_m2": 90,
                       "source": "makelaar:x.com", "ref": f"R{n}"} for n in range(10)]
    assert len(dubbel.voeg_samen(zelfde_kantoor)) == 10

    # zonder een maat om op te vergelijken voegen wij niets samen
    kaal = [{"id": 1, "area": "javea", "price": 340000, "source": "a", "ref": "D"},
            {"id": 2, "area": "javea", "price": 340000, "source": "b", "ref": "E"}]
    assert len(dubbel.voeg_samen(kaal)) == 2

    # en A~B, B~C mag niet stilletjes A en C aan elkaar rijgen
    keten = [{"id": 1, "area": "javea", "price": 300000, "plot_m2": 1000, "source": "a", "ref": "A"},
             {"id": 2, "area": "javea", "price": 301500, "plot_m2": 1040, "source": "b", "ref": "B"},
             {"id": 3, "area": "javea", "price": 303000, "plot_m2": 1090, "source": "c", "ref": "C"}]
    samen = dubbel.voeg_samen(keten)
    assert all(x.get("bronnen", 1) <= 2 for x in samen), [x.get("bronnen") for x in samen]


def test_opknapper_alleen_bij_oud_en_ver_onder_de_wijkprijs():
    """Jan 26-09-2026: een gewoon huis komt erbij als het van vóór 1995 is én meer dan 40 % onder
    de wijkprijs staat. Eén van de twee is niet genoeg."""
    from dh import renovatie
    comps = {"tosalet_adsubia": {"villa_renovated": {"median": 4000}}}
    it = lambda prijs: {"price": prijs, "built_m2": 200, "zone": "tosalet_adsubia", "type": "villa"}
    goed = renovatie.opknapper_vermoeden(it(400000), {"year": 1978}, comps)   # € 2.000/m², 50 % eronder
    assert goed and goed["korting"] == 0.5 and "1978" in goed["reden"]
    assert renovatie.opknapper_vermoeden(it(560000), {"year": 1978}, comps) is None   # maar 30 % eronder
    assert renovatie.opknapper_vermoeden(it(400000), {"year": 2015}, comps) is None   # te nieuw
    assert renovatie.opknapper_vermoeden(it(400000), None, comps) is None             # geen bouwjaar
    # een pand dat net verbouwd is telt niet, ook al is het oud en goedkoop
    assert renovatie.opknapper_vermoeden(
        {**it(400000), "titel_en_tekst": "Villa recién reformada"}, {"year": 1978}, comps) is None


def test_terugbelherinnering():
    """Notitie plus datum, en de herinnering gaat maar één keer de deur uit."""
    from dh import alerts
    with tempfile.TemporaryDirectory() as d:
        s = Store(Path(d) / "t.sqlite")
        s.con.execute("INSERT INTO listings(source, source_ref, title, price, first_seen_at,"
                      " last_seen_at, last_fetch_at) VALUES ('t','R1','Villa',340000,'x','x','x')")
        s.con.commit()
        lid = int(s.con.execute("SELECT id FROM listings").fetchone()[0])
        s.markeer(lid, "gebeld", "Maria wil praten vanaf 310", "2026-10-03")
        assert s.markeringen()[lid]["volgende_stap"] == "2026-10-03"
        # een andere stand aanklikken mag de notitie niet wissen
        s.markeer(lid, "bod")
        assert s.markeringen()[lid]["notitie"] == "Maria wil praten vanaf 310"
        assert s.markeringen()[lid]["merk"] == "bod"
        assert s.herinneringen("2026-10-02") == []          # nog niet aan de beurt
        rijen = s.herinneringen("2026-10-03")
        assert len(rijen) == 1 and rijen[0]["source_ref"] == "R1"
        tekst = alerts.herinneringen_tekst(rijen)
        assert "terugbellen vandaag" in tekst and "Maria" in tekst
        s.herinnering_verstuurd([lid])
        assert s.herinneringen("2026-10-03") == []          # niet twee keer
        # een weggeklikt object herinnert nergens meer aan
        s.markeer(lid, "gebeld", None, "2026-10-04")
        s.markeer(lid, "weg")
        assert s.herinneringen("2026-10-04") == []
        s.close()


def test_koperswensen_zijn_een_indicator_en_geen_uitsluiting():
    """Jan 26-09-2026: zeezicht, zwembad, loopafstand en gelijkvloers tellen allemaal, maar objecten
    die er niet aan voldoen mogen uitdrukkelijk niet worden weggelaten."""
    from dh import verkoopbaarheid as V
    lang = ("Villa con vistas al mar y piscina privada, todo en una planta, muy tranquila y "
            "cerca de todos los servicios del pueblo de Javea")
    vol = V.beoordeel({"lat": 38.7869, "lon": 0.1790}, lang)
    assert vol["punten"] == 4 and vol["van"] == 4
    kaal = V.beoordeel({"lat": 38.74, "lon": 0.22},
                       "Casa de campo tranquila en el interior de Javea con mucho terreno, "
                       "rodeada de naranjos y con acceso por camino rural sin asfaltar")
    assert kaal["punten"] == 0                      # nul punten, maar het object blijft bestaan
    assert kaal["missers"], "ver van de kern hoort als misser te worden genoemd"
    # bij een perceel tellen zwembad en gelijkvloers niet mee; die bouw je er zelf bij
    kavel = V.beoordeel({"category": "perceel", "lat": 38.7869, "lon": 0.1790}, lang)
    assert kavel["van"] == 2 and kavel["soort"] == "perceel"
    # te weinig tekst is geen nul, dat is onbekend
    onbekend = V.beoordeel({"lat": 38.79, "lon": 0.18}, "Villa")
    assert onbekend["punten"] is None and "Niet te beoordelen" in onbekend["toelichting"]


def test_appartement_zonder_lift_boven_de_tweede():
    """Harde uitsluiting van Jan. Zwijgt de advertentie over de lift, dan sluiten wij niets uit."""
    from dh import verkoopbaarheid as V
    assert V.appartement_zonder_lift_hoog("Apartamento en 3ª planta sin ascensor")
    assert V.appartement_zonder_lift_hoog("Apartment on the fourth floor without a lift")
    assert V.appartement_zonder_lift_hoog("Appartement 5ª planta, zonder lift")
    assert V.appartement_zonder_lift_hoog("Piso tercera planta con ascensor") is None
    assert V.appartement_zonder_lift_hoog("Apartamento 3ª planta") is None      # zwijgt over de lift
    assert V.appartement_zonder_lift_hoog("Apartamento planta baja sin ascensor") is None
    assert V.appartement_zonder_lift_hoog("") is None


def test_afstand_klopt_ongeveer():
    from dh import verkoopbaarheid as V
    # twee punten van ongeveer 1,3 km uit elkaar in Jávea: Puerto–Arenal en het Centrum
    d = V.afstand_m(38.78728, 0.17944, 38.78664, 0.16393)
    assert 1200 < d < 1500, d
    assert V.afstand_m(38.78728, 0.17944, 38.78728, 0.17944) == 0


def test_kustoordeel_niet_op_een_kilometer_van_zee():
    """De eerste versie zei "in de kustzone" over een perceel op 1.012 meter van het water, alleen
    omdat dat net iets dichter bij de ene lijn lag dan bij de andere. Op die afstand zegt dat niets."""
    from dh import water_kust as W
    assert W._kustoordeel(0.5, 40) == "in_dpmt"           # raakt het openbaar zeegebied
    assert W._kustoordeel(30, 70) == "in_servidumbre"     # tussen de twee lijnen
    assert W._kustoordeel(120, 30) == "nabij"             # landwaarts van de beschermingsgrens
    assert W._kustoordeel(200, None) == "nabij"
    assert W._kustoordeel(900, 950) == "buiten"           # de fout die eruit moest
    assert W._kustoordeel(1012, 1028) == "buiten"
    assert W._kustoordeel(None, None) == "buiten"


def test_alleen_het_zwaarste_water_sluit_uit():
    """Jan 26-09-2026: doorstroomzone en openbaar zeegebied vallen af; de honderdjaarszone blijft
    staan met een waarschuwing, en zonder extra kostenpost."""
    from dh import water_kust as W
    assert W._uitsluiting({"zfp": True}) and "doorstroomzone" in W._uitsluiting({"zfp": True})
    assert W._uitsluiting({"kust_oordeel": "in_dpmt"})
    assert W._uitsluiting({"t100": True}) is None                  # blijft in de lijst
    assert W._uitsluiting({"kust_oordeel": "in_servidumbre"}) is None
    assert W.waarschuwing({"t100": True, "t100_rio": "Río Gorgos"}).startswith("Ligt in de honderdjaarszone")
    assert W.waarschuwing({"kust_oordeel": "in_servidumbre"})
    assert W.waarschuwing({}) is None


def test_coordinaten_worden_rechtgezet():
    """Het coördinatenstelsel verschilt per laag, niet per dienst. Met de verkeerde volgorde krijg je
    HTTP 200 met een lege lijst en géén waarschuwing; daarom zet de module de volgorde zelf recht."""
    from dh import water_kust as W
    assert W._normaliseer([0.18, 38.79]) == (0.18, 38.79)      # al goed
    assert W._normaliseer([38.79, 0.18]) == (0.18, 38.79)      # omgedraaid
    # een vierkant van 100 bij 100 meter rond een punt in Jávea
    ring = [(0.180, 38.790), (0.181, 38.790), (0.181, 38.791), (0.180, 38.791), (0.180, 38.790)]
    assert W.in_ring(0.1805, 38.7905, ring)
    assert not W.in_ring(0.200, 38.790, ring)
    d = W.afstand_tot_ring_m((0.190, 38.7905), ring, 38.79)
    assert 700 < d < 850, d                                     # ongeveer 780 meter naar het oosten


def test_discordkaartje_toont_bron_en_link():
    """Jan 26-09-2026: het oude bericht was één lap tekst, zonder bron en zonder link."""
    from dh import alerts
    it = {"id": 1, "ref": "CHA0730", "zone_label": "Granadella – Balcón al Mar", "price": 430000,
          "class": "blauw", "scenario": "Sloop en nieuwbouw 291 m²", "per_maand": 14814,
          "source": "makelaar:randofrealestate.com",
          "url": "https://www.randofrealestate.com/casa-chalet-es1771041.html",
          "calc": {"result": 385168, "months": 20},
          "bod": {"opening": 354000, "walk": 368000, "kloof_pct": 0.14}}
    k = alerts.kaartje(it)
    assert k["title"].startswith("Granadella") and "430.000" in k["title"]
    assert k["url"] == it["url"]                                   # de titel is aanklikbaar
    namen = {f["name"]: f["value"] for f in k["fields"]}
    assert namen["Resultaat"] == "€ 385.168"
    assert "Per maand" not in namen, "Jan wilde die van het kaartje af (26-09-2026)"
    assert namen["Openen op"] == "€ 354.000"
    assert namen["Staat bij"] == "Randof Real Estate"              # naam, niet het webadres
    assert namen["Niet hoger dan"] == "€ 368.000"
    assert namen["Vraagprijs te hoog met"] == "14 %"   # de echte onderhandelafstand
    assert "CHA0730" in k["footer"]["text"] and "20 maanden" in k["footer"]["text"]
    # een object zonder link krijgt geen url-veld in plaats van een kapotte
    zonder = alerts.kaartje({**it, "url": ""})
    assert "url" not in zonder
    # de begeleidende tekst blijft kort
    tekst = alerts.message([it], [], None)
    assert len(tekst) < 300, tekst
    assert "sterke kans" in tekst
    # en niet meer dan tien kaartjes, want dat is de grens van Discord
    veel = alerts.kaartjes_voor([it] * 8, [it] * 8)
    assert len(veel) == alerts.MAX_KAARTJES == 10


def test_rente_is_recht_evenredig_en_dat_staat_erbij():
    """Jan 26-09-2026: standaard 5 %, want dat is het tarief van één investeerder en van daaruit
    rekent hij zelf 10 of 15 % uit. Dat kan alleen als de rente lineair is in het percentage, en
    daarom staat het bedrag per 5 procentpunt er los bij."""
    h = _rekenmodule()
    p = {"finance_rate_default": 0.05, "finance_fee_pct": 0.0}
    sc = h.Scenario(key="N", label="n", kind="nieuwbouw", newbuild_m2=300, result_m2=300,
                    permit_months=5, build_months=12, sale_months=3)
    vijf = h.financing(400000, 50000, 600000, sc, p, rate=0.05)["total"]
    tien = h.financing(400000, 50000, 600000, sc, p, rate=0.10)["total"]
    vijftien = h.financing(400000, 50000, 600000, sc, p, rate=0.15)["total"]
    assert abs(tien - 2 * vijf) < 1, (vijf, tien)
    assert abs(vijftien - 3 * vijf) < 1, (vijf, vijftien)
    # en het resultaat zakt met precies dat bedrag per 5 procentpunt
    k = {"rendementseis_op_projectkosten": 0.25, "doorlooptijd_max_maanden": 24,
         "bouwkosten_eur_per_m2": {"renovatie": 1000, "nieuwbouw": 2000},
         "verkoop_via_eigen_kantoor": True}
    par = json.loads((Path(__file__).resolve().parents[1] / "kader" / "parameters.json").read_text())["values"]
    r5 = h.project(400000, sc, 1_500_000, k, par, False, finance_rate=0.05)
    r10 = h.project(400000, sc, 1_500_000, k, par, False, finance_rate=0.10)
    assert abs((r5["result"] - r10["result"]) - r5["financing"]["total"]) < 2
    # het standaardtarief in de parameters staat op 5 %
    assert par["finance_rate_default"] == 0.05


def test_bodtrap_hangt_aan_hoe_lang_iets_te_koop_staat():
    """Jan 26-09-2026: hoe ver je onder de vraagprijs mag openen hangt af van hoe lang het te koop
    staat. Bij een verse advertentie is een scherp bod niet serieus."""
    from dh import negotiation
    from datetime import date, timedelta
    def plan(ask, plafond, dagen):
        sd = (date.today() - timedelta(days=dagen)).isoformat() if dagen is not None else None
        return negotiation.plan({"price": ask, "source_date": sd},
                                {"available": True, "max_price": {"base": plafond, "conservative": plafond * 0.5}})
    # vraagprijs 338.000, de deal draagt 268.000 — dat is 21 % eronder
    assert plan(338000, 268000, 10)["serieus_mogelijk"] is False      # vers: hoogstens 15 % korting
    assert plan(338000, 268000, 100)["serieus_mogelijk"] is False     # 3 maanden: hoogstens 20 %
    assert plan(338000, 268000, 200)["serieus_mogelijk"] is True      # 6 maanden: 25 % mag
    assert plan(338000, 268000, 400)["serieus_mogelijk"] is True      # ouder dan een jaar: vrij
    # wij weten van de meeste objecten niet hoe lang ze te koop staan; dan leggen wij geen grens op
    onbekend = plan(338000, 268000, None)
    assert onbekend["serieus_mogelijk"] is True and onbekend["max_korting"] is None
    assert onbekend["leeftijd_bron"] == "onbekend"
    # first_seen telt niet als leeftijd: wij lezen de meeste sites pas sinds deze week
    from dh import negotiation as N
    assert N._te_koop_sinds({"first_seen": "2020-01-01"}) == (None, "onbekend")
    # past de vraagprijs bijna, dan is een net bod gewoon mogelijk
    dichtbij = plan(338000, 320000, 10)
    assert dichtbij["serieus_mogelijk"] and dichtbij["opening"] >= 338000 * 0.85


def test_waardezone_geometrie_leest_graden_en_respecteert_gaten():
    """Twee valkuilen in de waardekaart van het kadaster.

    De eerste: de aanvraag wil x/y in Web Mercator, maar de geometrie komt terug in gewone graden.
    Wie de teruggave nóg eens omrekent, houdt coördinaten rond 0,000002 over en dan ligt geen enkel
    object meer in een zone (gebeurd op 26-09-2026, nul treffers op 718 objecten).
    De tweede: een waardezone kan een stuk uitsparen dat bij een andere zone hoort. Alleen de
    buitenring lezen plakt zo'n punt aan de verkeerde zone — en dus aan het verkeerde prijspeil."""
    from dh import zonewaarde as Z
    assert Z._punt([0.18, 38.79]) == (0.18, 38.79)
    assert Z._punt([38.79, 0.18]) == (0.18, 38.79)          # omgedraaid paar
    x, y = Z._naar_mercator(0.1830, 38.7647)
    assert 20000 < x < 21000 and 4_680_000 < y < 4_700_000, (x, y)
    buiten = [(0.10, 38.70), (0.30, 38.70), (0.30, 38.90), (0.10, 38.90), (0.10, 38.70)]
    gat = [(0.18, 38.78), (0.22, 38.78), (0.22, 38.82), (0.18, 38.82), (0.18, 38.78)]
    geom = {"type": "Polygon", "coordinates": [buiten, gat]}
    vlak = Z._ringen(geom)[0]
    assert len(vlak) == 2                                    # het gat is niet weggegooid
    assert Z._in_vlak(0.12, 38.72, vlak)                     # binnen, buiten het gat
    assert not Z._in_vlak(0.20, 38.80, vlak)                 # midden in het gat: niet deze zone
    assert not Z._in_vlak(0.50, 38.80, vlak)


def test_waardezone_koppelt_alleen_bij_de_passende_typologie():
    """De module hoort bij één representatief product. Een appartement in een villazone krijgt dus
    géén prijspeil: liever niets dan het verkeerde (onderzoek N11 §9.2)."""
    from dh import zonewaarde as Z
    vlak = [[(0.10, 38.70), (0.30, 38.70), (0.30, 38.90), (0.10, 38.90), (0.10, 38.70)]]
    zones = {"gemeenten": {"javea": {"naam": "Jávea/Xàbia", "zones": [
        {"zona_valor": "U20", "cod_zona": "127", "ejercicio": 2026, "num_inmuebles": 3025,
         "tipologia": "Vivienda unifamiliar aislada/pareada", "categoria": "Media", "antiguedad": 50,
         "conservacion": "Renovado", "superficie": 160.0, "superficie_suelo": 1000.0,
         "val_tipo": 547400.0, "val_tipo_m2": 3200.0, "val_estandar_m2": 3500.0, "vlakken": [vlak]}]}}}
    villa = Z.zoek(38.80, 0.20, "Villa", zones)
    assert villa["gevonden"] and villa["zona_valor"] == "U20" and villa["val_tipo_m2"] == 3200.0
    assert Z.zoek(38.80, 0.20, "Land", zones)["gevonden"]              # kavel wordt een villa
    appartement = Z.zoek(38.80, 0.20, "Apartment", zones)
    assert not appartement["gevonden"] and appartement["overlap"] == 1
    assert "typologie" in appartement["reden"]
    kantoor = Z.zoek(38.80, 0.20, "Building", zones)
    assert not kantoor["gevonden"] and "geen enkele representatieve typologie" in kantoor["reden"]
    assert not Z.zoek(38.60, 0.50, "Villa", zones)["gevonden"]          # buiten alle zones
    assert "vrijstaande of geschakelde woning" in Z.omschrijving(villa)
    assert "€ 547.200" not in Z.omschrijving(villa) and "€ 547.400" in Z.omschrijving(villa)


def test_prijspeil_waarschuwt_pas_bij_het_extreme():
    """Onderzoek N11 stelde één drempel van 2,0 voor. Op onze eigen scenario's (mediaan 1,54,
    p90 2,27) zou die een vijfde van alles onbetrouwbaar maken. Daarom: opmerking vanaf 2,0,
    waarschuwing pas vanaf 2,5 — en ook een opmerking als wij ónder het zonegemiddelde zitten."""
    from dh import zonewaarde as Z
    z = {"val_tipo_m2": 3200.0, "zona_valor": "U20", "antiguedad": 50}
    assert Z.oordeel(4800, z) is None                       # 1,5× — gewoon een gerenoveerd huis
    soort, tekst = Z.oordeel(6600, z)                       # 2,1×
    assert soort == "opmerking" and "zonegemiddelde" in tekst
    soort, tekst = Z.oordeel(8400, z)                       # 2,6×
    assert soort == "waarschuwing" and "controleer de vergelijkingsobjecten" in tekst
    soort, tekst = Z.oordeel(2900, z)                       # onder het zonegemiddelde
    assert soort == "opmerking" and "mogelijk te laag" in tekst
    assert Z.oordeel(8400, None) is None
    assert Z.oordeel(None, z) is None
    assert Z.oordeel(8400, {"val_tipo_m2": 0}) is None


def test_coordinaat_alleen_van_een_gemeten_site():
    """De valkuil van 27-09-2026: op tien van de drieëndertig makelaarssites staat op élke
    objectpagina dezelfde coördinaat — die van het kantoor. Overnemen betekent dat helling,
    overstromingsrisico en prijspeil op het kantoor van de makelaar worden uitgerekend, met dezelfde
    stelligheid als een echte meting. Daarom leest de module een meetrapport in plaats van een lijst
    patronen, en doet zij niets voor een site die niet is gemeten."""
    from dh import coordinaat as C
    html = '<div data-lat="38.78894" data-lng="0.16642"></div>'
    rapport = {"paginas_per_site": 4, "sites": {
        "gemeten.com": {"bruikbaar_patroon": "data-attribuut", "patronen": {}},
        "kantoor.com": {"bruikbaar_patroon": None,
                        "patronen": {"data-attribuut": {"vast_op_elke_pagina": [[38.78894, 0.16642]]}}}}}
    import json, pathlib, tempfile
    C._meting.cache_clear()
    try:
        with tempfile.TemporaryDirectory() as d:
            p = pathlib.Path(d) / "meting.json"
            p.write_text(json.dumps(rapport), encoding="utf-8")
            oud, C.METING = C.METING, p
            try:
                C._meting.cache_clear()
                assert C.toegestane_sites() == {"gemeten.com": "data-attribuut"}
                assert C.uit_pagina(html, "kantoor.com") is None      # niet gemeten als bruikbaar
                assert C.uit_pagina(html, "onbekend.com") is None     # helemaal niet gemeten
                # het punt staat op de lijst vaste punten van kantoor.com en wordt overal geweigerd
                assert C.uit_pagina(html, "gemeten.com") is None
                goed = '<div data-lat="38.76845" data-lng="0.19710"></div>'
                assert C.uit_pagina(goed, "gemeten.com") == (38.76845, 0.1971)
                assert C.uit_pagina(goed, "WWW.Gemeten.com") == (38.76845, 0.1971)
                # twee verschillende punten op één pagina: wij weten niet welke het object is
                twee = goed + '<div data-lat="38.70000" data-lng="0.20000"></div>'
                assert C.uit_pagina(twee, "gemeten.com") is None
                # buiten het werkgebied telt niet mee
                ver = '<div data-lat="40.41670" data-lng="-3.70330"></div>'
                assert C.uit_pagina(ver, "gemeten.com") is None
            finally:
                C.METING = oud
    finally:
        C._meting.cache_clear()


def test_coordinaat_vertrouwt_geen_meting_van_een_enkele_pagina():
    """"Verandert per object" is niet vast te stellen op één of twee pagina's. Een rapport dat op
    te weinig pagina's rust, zet dus geen enkele site aan."""
    from dh import coordinaat as C
    import json, tempfile, pathlib
    with tempfile.TemporaryDirectory() as d:
        p = pathlib.Path(d) / "meting.json"
        p.write_text(json.dumps({"paginas_per_site": 1, "sites": {
            "site.com": {"bruikbaar_patroon": "json", "patronen": {}}}}), encoding="utf-8")
        oud, C.METING = C.METING, p
        try:
            C._meting.cache_clear()
            assert C.toegestane_sites() == {}
        finally:
            C.METING = oud
            C._meting.cache_clear()


def test_zoekresultaatpagina_is_geen_woning():
    """Op 27-09-2026 stonden er 280 zoekresultaatpagina's als woning in de database, 277 van één
    site. Elk droeg de prijs en het oppervlak van de woning die toevallig bovenaan dat filter stond:
    € 1.950.000 met 389/409 m², eenentwintig keer. Over één ervan was al een melding gestuurd."""
    from dh.adapters.makelaars import is_overzichtspagina, is_zoekopdracht
    nep = [
        "https://www.xabiacasa.com/results/?type%5B0%5D=1&id_tipo_operacion=1&od=prd.d",
        "https://www.xabiacasa.com/results/?id_tipo_operacion=1",
        "https://www.javeacontinental.com/results/?lan=&id_tipo_operacion=1&precio_min=",
        "https://www.villalingo.com/?q=g6i1g3a5n1t6i5n0e547",
    ]
    echt = [
        "https://www.xabiacasa.com/apartamento-en-javea-con-piscina-es1765346.html",
        "https://www.costablancajaveaproperties.com/property/apartment-in-javea-cmaoiji6/",
        "https://voorbeeld.es/ficha?id=12345",          # één verwijzing naar één object mag wel
        "https://voorbeeld.es/inmueble?ref=AB-1234",
    ]
    for u in nep:
        assert is_overzichtspagina(u, None), u
    for u in echt:
        assert not is_overzichtspagina(u, None), u
    assert not is_zoekopdracht("https://voorbeeld.es/villa-in-javea")      # helemaal geen parameters
    assert is_zoekopdracht("https://voorbeeld.es/x?id=1&type=2")           # twee parameters: een filter
    assert is_zoekopdracht("https://voorbeeld.es/x?id=" + "9" * 40)        # geen verwijzing maar een sleutel


def test_punt_is_niet_altijd_een_duizendtalscheiding():
    """In Spanje scheidt een punt duizendtallen ("1.760"), maar in een JSON-LD-veld is hij een
    decimaalteken ("795.00"). De oude lezer haalde élke punt weg en maakte van 795,00 m² dus
    79.500 m². 191 objecten hadden daardoor een oppervlak dat niet bestaat, tot 83.235 m² aan toe —
    en dat getal gaat rechtstreeks de bouwkosten en de verkoopwaarde in."""
    from dh.adapters.makelaars import _num
    assert _num("795.00") == 795            # de fout die eruit moest
    assert _num("389.00") == 389
    assert _num("1.760") == 1760            # drie cijfers erachter: duizendtallen
    assert _num("2.600.000") == 2600000
    assert _num("83.235") == 83235
    assert _num("1.234,56") == 1234.56      # Spaanse schrijfwijze
    assert _num("1,234.56") == 1234.56      # Engelse schrijfwijze
    assert _num("1,5") == 1.5
    assert _num("1 760") == 1760            # spatie als scheiding
    assert _num(" 1.760 ") == 1760  # vaste en smalle spatie
    assert _num("389") == 389
    assert _num("") is None and _num(None) is None and _num("abc") is None


def test_keuzelijst_telt_niet_mee_als_paginatekst():
    """De prijs- en oppervlaktefilters bovenaan een makelaarssite staan in <option>-elementen.
    Die telden mee als tekst, en de prijslezer pakte de eerste waarde boven de 20.000 — dus de
    laagste stap van het filter. 293 van de 320 objecten van één site stonden zo op € 50.000
    terwijl de woning € 690.000 kostte; 138 objecten van een andere site kregen 50 m² bebouwd."""
    from dh.adapters.makelaars import _tekst
    html = ('<select name="precio"><option value="50000">50.000 €</option>'
            '<option value="100000">100.000 €</option></select>'
            '<datalist id="m2"><option>50 m2</option></datalist>'
            '<div class="precio">690.000 €</div><p>Superficie construida: 214 m2</p>')
    txt = _tekst(html)
    assert "690.000" in txt and "214" in txt
    assert "50.000" not in txt and "100.000" not in txt
    assert "50 m2" not in txt
    # gewone tekst blijft ongemoeid, ook als er het woord option in staat
    assert "een optie" in _tekst("<p>een optie</p>")

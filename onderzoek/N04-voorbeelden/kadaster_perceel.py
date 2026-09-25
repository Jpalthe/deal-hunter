#!/usr/bin/env python3
"""Kadastrale referentie -> perceel + gebouwen, als GeoJSON.

Gebruik:  python3 kadaster_perceel.py 6442021BC5964S [uitvoermap]

Haalt op bij de Sede Electronica del Catastro (gratis, geen sleutel):
  1. Consulta_DNPRC (JSON)  -> perceeloppervlakte ss, bebouwd sfc, bouwjaar ant,
                               en per bouwdeel gebruik/verdieping/m2
  2. WFS Cadastral Parcels  -> perceelgrens (GML) + officiele areaValue
  3. WFS Buildings          -> gebouwvoetafdruk, bouwjaar, bouwlagen, zwembad

Schrijft <RC>.geojson (WGS84) en print een samenvatting.
Bron: Direccion General del Catastro. Verplichte bronvermelding bij hergebruik.
"""
import json
import math
import re
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

OVC = "https://ovc.catastro.meh.es"
UA = {"User-Agent": "TREE-DealHunter/1.0 (onderzoek; contact via tree.es)"}
NS = {
    "gml": "http://www.opengis.net/gml/3.2",
    "cp": "http://inspire.ec.europa.eu/schemas/cp/4.0",
    "bu": "http://inspire.jrc.ec.europa.eu/schemas/bu-ext2d/2.0",
    "buc": "http://inspire.jrc.ec.europa.eu/schemas/bu-core2d/2.0",
}
_last = [0.0]


def haal(url):
    """Eén verzoek per seconde, zoals de eigen gebruiksregel van dit project."""
    wacht = _last[0] + 1.0 - time.monotonic()
    if wacht > 0:
        time.sleep(wacht)
    _last[0] = time.monotonic()
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=40) as r:
        return r.read()


def dnprc(rc):
    url = (f"{OVC}/OVCServWeb/OVCWcfCallejero/COVCCallejero.svc/json/Consulta_DNPRC"
           f"?Provincia=&Municipio=&RefCat={urllib.parse.quote(rc)}")
    return json.loads(haal(url))


def wfs(dienst, query, rc, srs):
    url = (f"{OVC}/INSPIRE/wfs{dienst}.aspx?service=wfs&version=2.0.0&request=GetFeature"
           f"&STOREDQUERIE_ID={query}&refcat={urllib.parse.quote(rc)}&srsname=EPSG::{srs}")
    return haal(url).decode("ISO-8859-1")


def ringen(xml_tekst, lat_eerst):
    """Alle gml:posList in het document -> lijst van ringen [[lon,lat],...]."""
    uit = []
    for m in re.finditer(r"<gml:posList[^>]*>([^<]+)</gml:posList>", xml_tekst):
        g = [float(x) for x in m.group(1).split()]
        paren = list(zip(g[0::2], g[1::2]))
        uit.append([[b, a] if lat_eerst else [a, b] for a, b in paren])
    return uit


def shoelace(ring):
    """Oppervlakte in vierkante eenheden van het stelsel (dus m2 bij UTM)."""
    s = 0.0
    for (x1, y1), (x2, y2) in zip(ring, ring[1:]):
        s += x1 * y2 - x2 * y1
    return abs(s) / 2.0


def punt_in_ring(lon, lat, ring):
    binnen = False
    for (x1, y1), (x2, y2) in zip(ring, ring[1:]):
        if (y1 > lat) != (y2 > lat):
            snij = x1 + (lat - y1) * (x2 - x1) / (y2 - y1)
            if lon < snij:
                binnen = not binnen
    return binnen


def hoofd(rc, uitmap="."):
    rc = rc.strip().upper().replace(" ", "")
    d = dnprc(rc)
    if "lerr" in d.get("consulta_dnprcResult", {}):
        print("Catastro-fout:", json.dumps(d, ensure_ascii=False))
        return 1
    bico = d["consulta_dnprcResult"]["bico"]
    bi, finca = bico["bi"], bico["finca"]
    ss = int(finca["dff"]["ss"])                       # perceeloppervlakte m2
    sfc = int(bi["debi"].get("sfc", 0))                # superficie construida m2
    ant = bi["debi"].get("ant")                        # bouwjaar
    lcons = bico.get("lcons", [])
    if isinstance(lcons, dict):
        lcons = [lcons]

    cp_geo = wfs("CP", "GetParcel", rc, "4326")
    cp_utm = wfs("CP", "GetParcel", rc, "25830")
    bu_geo = wfs("BU", "GetBuildingByParcel", rc, "4326")
    bu_utm = wfs("BU", "GetBuildingByParcel", rc, "25830")
    part_geo = wfs("BU", "GetBuildingPartByParcel", rc, "4326")
    ov_geo = wfs("BU", "GetOtherBuildingByParcel", rc, "4326")

    m = re.search(r'<cp:areaValue uom="m2">(\d+)</cp:areaValue>', cp_geo)
    area_wfs = int(m.group(1)) if m else None
    perceel = ringen(cp_geo, lat_eerst=True)
    perceel_utm = ringen(cp_utm, lat_eerst=False)
    opp_eigen = round(sum(shoelace(r) for r in perceel_utm), 1)

    gebouwen = ringen(bu_geo, lat_eerst=True)
    delen = ringen(part_geo, lat_eerst=True)
    overig = ringen(ov_geo, lat_eerst=True)
    voet_utm = round(sum(shoelace(r) for r in ringen(bu_utm, lat_eerst=False)), 1)
    zwembad = "openAirPool" in ov_geo
    mj = re.search(r"<bu-core2d:beginning>(\d{4})", bu_geo)
    bouwjaar_wfs = mj.group(1) if mj else None
    lagen = [int(x) for x in re.findall(r"<bu-ext2d:numberOfFloorsAboveGround>(\d+)<", part_geo)]
    onder = [int(x) for x in re.findall(r"<bu-ext2d:numberOfFloorsBelowGround>(\d+)<", part_geo)]
    staat = re.findall(r"<bu-core2d:conditionOfConstruction>([a-zA-Z]+)<", bu_geo)

    fc = {"type": "FeatureCollection", "features": [],
          "metadata": {"referencia_catastral": rc,
                       "bron": "Direccion General del Catastro (INSPIRE WFS + OVC)",
                       "opgehaald": time.strftime("%Y-%m-%d")}}
    for i, ring in enumerate(perceel):
        fc["features"].append({"type": "Feature", "id": f"{rc}.parcel.{i}",
                               "geometry": {"type": "Polygon", "coordinates": [ring]},
                               "properties": {"soort": "perceel", "refcat": rc,
                                              "oppervlakte_m2_wfs": area_wfs,
                                              "oppervlakte_m2_dnprc": ss,
                                              "oppervlakte_m2_berekend": opp_eigen}})
    for naam, ringenlijst in (("gebouw", gebouwen), ("bouwdeel", delen), ("bijwerk", overig)):
        for i, ring in enumerate(ringenlijst):
            fc["features"].append({"type": "Feature", "id": f"{rc}.{naam}.{i}",
                                   "geometry": {"type": "Polygon", "coordinates": [ring]},
                                   "properties": {"soort": naam, "refcat": rc,
                                                  "bouwjaar": bouwjaar_wfs}})
    pad = f"{uitmap.rstrip('/')}/{rc}.geojson"
    with open(pad, "w", encoding="utf-8") as f:
        json.dump(fc, f, ensure_ascii=False, indent=1)

    print(f"Kadastrale referentie : {rc}")
    print(f"Adres                 : {bi.get('ldt')}")
    print(f"Perceeltype           : {finca.get('ltp')}")
    print(f"Perceel (DNPRC ss)    : {ss} m2")
    print(f"Perceel (WFS areaValue): {area_wfs} m2")
    print(f"Perceel (zelf berekend): {opp_eigen} m2  [shoelace op EPSG:25830]")
    print(f"Bebouwd (sfc)         : {sfc} m2 superficie construida")
    print(f"Bouwjaar (ant / WFS)  : {ant} / {bouwjaar_wfs}")
    print(f"Voetafdruk gebouw     : {voet_utm} m2 ; staat: {', '.join(staat) or '?'}")
    print(f"Bouwlagen per bouwdeel: boven {lagen or '?'} / onder {onder or '?'}")
    print(f"Zwembad in kadaster   : {'ja' if zwembad else 'nee'}")
    print(f"Bebouwingsgraad       : {round(100*voet_utm/ss,1) if ss else '?'} % van het perceel")
    som = 0
    for c in lcons:
        li = c.get("dt", {}).get("lourb", {}).get("loint", {})
        stl = int(c["dfcons"]["stl"])
        som += stl
        print(f"   - {c['lcd']:<12} verdieping {li.get('pt','?'):>3}  {stl:>5} m2  "
              f"{c.get('dvcons',{}).get('dtip','')}")
    if lcons:
        print(f"   som bouwdelen      : {som} m2 (moet gelijk zijn aan sfc {sfc})")
    print(f"GeoJSON geschreven    : {pad}")
    return 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    sys.exit(hoofd(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else "."))

"""Meting: adverteerde oppervlakte (Kyero-feed built) vs kadastrale opbouw (Catastro OVC).

Leest villa's met coordinaten uit dealhunter.sqlite, vraagt per punt de kadastrale
referentie op (Consulta_RCCOOR) en daarna de niet-beschermde gegevens (Consulta_DNPRC).
Bewaart per object: totale kadastrale superficie construida, en de opsplitsing per
gebruikssoort (VIVIENDA, PORCHE, TERRAZA, APARCAMIENTO, ALMACEN, SOTANO, DEPORTIVO ...).

Geen persoonsgegevens: DNPRC levert alleen 'datos no protegidos' (geen eigenaren).
Snelheid: 1 verzoek per 1,2 s, zoals de dashboardkoppeling.
"""
import json, sqlite3, sys, time, urllib.parse, urllib.request
import xml.etree.ElementTree as ET

NS = {"c": "http://www.catastro.meh.es/"}
UA = "TREE-DealHunter/onderzoek (contact: jvwp.am@gmail.com)"
DB = "/Users/root-admin/tree-es/deal-hunter/data/dealhunter.sqlite"
OUT = "/private/tmp/claude-501/-Users-root-admin-tree-es/a3ae9710-3e66-42bb-b602-476120d4027d/scratchpad/catastro_meting.json"
PAUSE = 1.2


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8", "replace")


def rc_op_punt(lat, lon):
    q = urllib.parse.urlencode({"SRS": "EPSG:4326", "Coordenada_X": lon, "Coordenada_Y": lat})
    x = ET.fromstring(get(
        "https://ovc.catastro.meh.es/ovcservweb/OVCSWLocalizacionRC/OVCCoordenadas.asmx/Consulta_RCCOOR?" + q))
    c = x.find(".//c:coord", NS)
    if c is None:
        return None, None
    pc1 = c.findtext("c:pc/c:pc1", "", NS)
    pc2 = c.findtext("c:pc/c:pc2", "", NS)
    return (pc1 + pc2) or None, c.findtext("c:ldt", "", NS)


def dnprc(rc):
    q = urllib.parse.urlencode({"Provincia": "", "Municipio": "", "RC": rc})
    x = ET.fromstring(get(
        "https://ovc.catastro.meh.es/ovcservweb/OVCSWLocalizacionRC/OVCCallejero.asmx/Consulta_DNPRC?" + q))
    err = x.find(".//c:err", NS)
    if err is not None:
        return {"fout": (err.findtext("c:des", "", NS) or "").strip()}
    uit = {"panden": [], "elementen": []}
    for bi in x.iter("{http://www.catastro.meh.es/}bi"):
        d = bi.find("c:debi", NS)
        uit["panden"].append({
            "ldt": bi.findtext("c:ldt", "", NS),
            "uso": d.findtext("c:luso", "", NS) if d is not None else "",
            "sfc": float(d.findtext("c:sfc", "0", NS) or 0) if d is not None else 0,
            "bouwjaar": d.findtext("c:ant", "", NS) if d is not None else "",
        })
    for c in x.iter("{http://www.catastro.meh.es/}cons"):
        stl = c.findtext("c:dfcons/c:stl", "", NS)
        uit["elementen"].append({
            "soort": (c.findtext("c:lcd", "", NS) or "").strip(),
            "m2": float(stl) if stl else 0.0,
        })
    return uit


def main():
    con = sqlite3.connect(DB)
    rijen = con.execute(
        "SELECT id, source, source_ref, type, area, price, built_m2, plot_m2, lat, lon, url "
        "FROM listings WHERE gone_at IS NULL AND lat IS NOT NULL AND built_m2 > 0 "
        "AND type IN ('Villa','Country house','Town house') ORDER BY id").fetchall()
    print(f"{len(rijen)} objecten", flush=True)
    res = []
    for i, r in enumerate(rijen, 1):
        rec = dict(zip(["id", "source", "ref", "type", "wijk", "prijs", "adv_built",
                        "adv_plot", "lat", "lon", "url"], r))
        try:
            rc, ldt = rc_op_punt(rec["lat"], rec["lon"])
            time.sleep(PAUSE)
            rec["rc"] = rc
            rec["ldt_punt"] = ldt
            if rc:
                rec["cat"] = dnprc(rc)
                time.sleep(PAUSE)
        except Exception as e:
            rec["fout"] = f"{type(e).__name__}: {e}"
            time.sleep(PAUSE)
        res.append(rec)
        if i % 10 == 0:
            print(f"  {i}/{len(rijen)}", flush=True)
            json.dump(res, open(OUT, "w"), ensure_ascii=False, indent=1)
    json.dump(res, open(OUT, "w"), ensure_ascii=False, indent=1)
    print("klaar ->", OUT, flush=True)


if __name__ == "__main__":
    main()

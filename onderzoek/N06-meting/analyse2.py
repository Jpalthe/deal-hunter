"""Tweede analyse, met de werkelijke kadastrale gebruikscodes.

Twee vragen, apart gehouden:
A. Waaruit bestaat de kadastrale 'superficie construida' van een villaperceel hier?
   (onafhankelijk van de vraag of de speld het juiste perceel raakte)
B. Hoe groot is het gat tussen de advertentie en het kadaster? (alleen als vlag bruikbaar)
"""
import json, statistics, collections

P = "/private/tmp/claude-501/-Users-root-admin-tree-es/a3ae9710-3e66-42bb-b602-476120d4027d/scratchpad/"
d = json.load(open(P + "catastro_meting.json"))

WONEN = {"VIVIENDA"}
# Catastro zet het rekenpercentage in de code zelf
BUITEN = {"SOPORT. 50%", "PORCHE 100%", "PORCHE 50%", "TERR.C 100%", "TERR.C 50%",
          "TERRAZA", "PORCHE", "SOLARIUM", "BALCON", "TERRAZA 50%", "SOPORTAL"}
BIJ = {"APARCAMIENTO", "ALMACEN", "TRASTERO", "GARAJE", "BODEGA", "SOTANO"}
NIET_WOON_BESTEMMING = {"ENSEÑANZA", "COMERCIO", "OCIO HOSTEL.", "INDUSTRIAL", "OFICINAS",
                        "SANIDAD", "RELIGIOSO", "ESPECTACULO", "CULTURAL"}

alles = []
for r in d:
    cat = r.get("cat") or {}
    if not r.get("rc") or cat.get("fout") or not cat.get("elementen"):
        continue
    panden = cat["panden"]
    per = collections.Counter()
    codes = set()
    for e in cat["elementen"]:
        s = e["soort"].strip()
        codes.add(s)
        groep = ("wonen" if s in WONEN else "buiten" if s in BUITEN
                 else "bij" if s in BIJ else "overig")
        per[groep] += e["m2"]
    alles.append({
        "ref": r["ref"], "rc": r["rc"], "wijk": r["wijk"], "prijs": r["prijs"],
        "adv": r["adv_built"], "adv_plot": r["adv_plot"],
        "cat_tot": sum(p["sfc"] for p in panden), "n_bi": len(panden),
        "usos": sorted({p["uso"] for p in panden}),
        "bouwjaar": panden[0]["bouwjaar"] if panden else "",
        "ldt": panden[0]["ldt"] if panden else "",
        "codes": sorted(codes), **{k: per[k] for k in ("wonen", "buiten", "bij", "overig")},
    })

# --- A. schone deelverzameling: eengezins-villaperceel ---
schoon = [x for x in alles
          if x["n_bi"] == 1
          and x["usos"] == ["Residencial"]
          and x["wonen"] > 0
          and not (set(x["codes"]) & NIET_WOON_BESTEMMING)
          and 60 <= x["cat_tot"] <= 1500]

print(f"kadastrale opvragingen met bebouwing : {len(alles)}")
print(f"schone eengezins-villapercelen       : {len(schoon)}")
print()


def stat(naam, w, pct=False):
    if not w:
        print(f"{naam}: geen"); return
    w = sorted(w); f = 100 if pct else 1; e = "%" if pct else ""
    print(f"{naam}: n={len(w):3d}  mediaan={statistics.median(w)*f:6.1f}{e}  "
          f"gem={statistics.fmean(w)*f:6.1f}{e}  p25={w[len(w)//4]*f:6.1f}{e}  "
          f"p75={w[3*len(w)//4]*f:6.1f}{e}  max={w[-1]*f:6.1f}{e}")


print("=== A. samenstelling van de kadastrale superficie construida (villapercelen) ===")
stat("aandeel WONEN                    ", [x["wonen"] / x["cat_tot"] for x in schoon], True)
stat("aandeel overdekte buitenruimte   ", [x["buiten"] / x["cat_tot"] for x in schoon], True)
stat("aandeel garage/berging/kelder    ", [x["bij"] / x["cat_tot"] for x in schoon], True)
stat("aandeel overig (zwembad/sport)   ", [x["overig"] / x["cat_tot"] for x in schoon], True)
print()
stat("kadastraal totaal / kadastraal WONEN", [x["cat_tot"] / x["wonen"] for x in schoon])
print("  (= hoeveel hoger de volledige kadastrale opgave ligt dan het pure woondeel)")
print()
n_b = sum(1 for x in schoon if x["buiten"] > 0)
n_j = sum(1 for x in schoon if x["bij"] > 0)
n_o = sum(1 for x in schoon if x["overig"] > 0)
print(f"percelen met overdekte buitenruimte in het kadaster : {n_b}/{len(schoon)}")
print(f"percelen met garage/berging/kelder                  : {n_j}/{len(schoon)}")
print(f"percelen met overig (meestal zwembad, 'DEPORTIVO')   : {n_o}/{len(schoon)}")
print()
codes = collections.Counter(c for x in schoon for c in x["codes"])
print("codes in de schone verzameling:", dict(codes.most_common()))

print()
print("=== B. gat advertentie vs kadaster (alleen als vlag) ===")
g = [x for x in schoon if x["adv"] and x["cat_tot"] > 0]
stat("advertentie / kadastraal TOTAAL", [x["adv"] / x["cat_tot"] for x in g])
stat("advertentie / kadastraal WONEN ", [x["adv"] / x["wonen"] for x in g])
binnen = sum(1 for x in g if 0.85 <= x["adv"] / x["cat_tot"] <= 1.15)
print(f"advertentie binnen 15% van het kadastrale totaal: {binnen}/{len(g)}")
hoger = sum(1 for x in g if x["adv"] / x["cat_tot"] > 1.15)
lager = sum(1 for x in g if x["adv"] / x["cat_tot"] < 0.85)
print(f"  advertentie >15% hoger: {hoger}/{len(g)}   >15% lager: {lager}/{len(g)}")

json.dump({"alles": alles, "schoon": schoon}, open(P + "analyse2.json", "w"),
          ensure_ascii=False, indent=1)

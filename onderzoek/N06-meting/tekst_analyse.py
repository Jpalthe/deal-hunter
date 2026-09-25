"""Herkenning: staat er in de advertentietekst een aanwijzing dat terras, kelder of
garage in de opgegeven oppervlakte zit?

Leest de live momentopname van de woningfeed (poort 3100, alleen lezen) en test een
aantal patronen op de volledige beschrijvingen in alle talen. Doel: meten hoe vaak
de tekst een tweede getal noemt, en of dat getal past bij het veld builtArea.
"""
import json, re, urllib.request, collections

BASE = "http://127.0.0.1:3100"
UA = "TREE-DealHunter/onderzoek"


def haal():
    items, page = [], 1
    while True:
        req = urllib.request.Request(
            f"{BASE}/api/properties?page={page}&limit=100&sort=ref&order=asc",
            headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=30) as r:
            j = json.load(r)
        items += j.get("properties", [])
        pg = j.get("pagination", {})
        if page >= int(pg.get("totalPages", 1)):
            return items
        page += 1


# getal + m2 met maximaal 40 tekens context ervoor/erna
GETAL = re.compile(r"(\d{1,3}(?:[.,]\d{3})*(?:[.,]\d{1,2})?|\d+(?:[.,]\d{1,2})?)\s*(?:m2|m²|m\^2|sqm|sq\.?\s?m|square met\w*|metros? cuadrados?|vierkante meter)", re.I)

TREFWOORD = {
    "terras":   r"terra(?:ce|za|s|sse)|naya|solarium|solárium|solarium|porch|porche|balcon|balkon|balcony|dakterras|roof\s*terrace|azotea",
    "kelder":   r"basement|s[oó]tano|kelder|semi-?basement|lower\s+(?:level|floor|ground)|planta\s+s[oó]tano|souterrain",
    "garage":   r"garage|garaje|carport|aparcamiento|parking|cochera",
    "berging":  r"trastero|almac[eé]n|storage|utility\s+room|abstellraum|bodega",
    "gast":     r"guest\s*(?:house|apartment|flat)|casa\s+de\s+invitados|apartamento\s+de\s+invitados|g[aä]stehaus|g[aä]stewohnung|annex|anexo|casita",
    "bebouwd":  r"built\s*(?:area|size|surface)|superficie\s+construida|constru[ií]d[oa]s?|bebaute\s+fl[aä]che|bebouwd",
    "nuttig":   r"superficie\s+[uú]til|[uú]tiles|usable\s+(?:area|surface)|habitable|living\s+(?:area|space|surface)|woonoppervlak|wohnfl[aä]che",
    "inclusief": r"incl\w*\s+(?:terra|garag|s[oó]tano|kelder|porch|basement)|including\s+(?:terrace|garage|basement)|inclu(?:ye|ido|idos|sief)\s+",
    "totaal":   r"\btotal\b|\btotaal\b|\bin\s+total\b|en\s+total|insgesamt",
}
PAT = {k: re.compile(v, re.I) for k, v in TREFWOORD.items()}


def _naar_getal(s):
    """'32.37' en '32,37' -> 32.37 ; '1.350' en '1,350' -> 1350 ; '25,208' -> 25208.

    Regel: staat er na het laatste scheidingsteken precies 3 cijfers, dan is het een
    duizendtalteken; staan er 1 of 2 cijfers, dan is het een decimaalteken.
    """
    m = re.search(r"[.,](\d+)$", s)
    if m and len(m.group(1)) == 3:
        heel = re.sub(r"[.,]", "", s)
        return float(heel) if heel.isdigit() else None
    kop, _, staart = s.rpartition(",") if "," in s[-3:] else s.rpartition(".")
    if kop:
        heel = re.sub(r"[.,]", "", kop)
        return float(f"{heel}.{staart}") if heel.isdigit() and staart.isdigit() else None
    heel = re.sub(r"[.,]", "", s)
    return float(heel) if heel.isdigit() else None


def main():
    items = haal()
    print(f"objecten in de momentopname: {len(items)}")
    tel = collections.Counter()
    villas, bruikbaar = 0, []
    for p in items:
        tekst = " ".join(v or "" for v in (p.get("desc") or {}).values())
        tekst += " " + " ".join(p.get("features") or [])
        if not tekst.strip():
            tel["geen tekst"] += 1
            continue
        tel["met tekst"] += 1
        if (p.get("type") or "") in ("Villa", "Country house", "Town house"):
            villas += 1
        raak = {k: bool(r.search(tekst)) for k, r in PAT.items()}
        for k, v in raak.items():
            if v:
                tel["trefwoord " + k] += 1
        # getallen met m2 in de tekst
        getallen = []
        for m in GETAL.finditer(tekst):
            w = _naar_getal(m.group(1))
            if w is None:
                continue
            if 5 <= w <= 20000:
                voor = tekst[max(0, m.start() - 45):m.start()].lower()
                na = tekst[m.end():m.end() + 25].lower()
                soort = None
                for k in ("terras", "kelder", "garage", "berging", "gast", "nuttig", "bebouwd"):
                    if PAT[k].search(voor) or PAT[k].search(na):
                        soort = k
                        break
                getallen.append((w, soort, voor[-40:].strip()))
        if getallen:
            tel["tekst met m2-getal"] += 1
        soorten = {s for _, s, _ in getallen if s}
        for s in soorten:
            tel["m2-getal bij " + s] += 1
        b = p.get("builtArea")
        if b and getallen:
            # staat het bebouwde getal letterlijk in de tekst?
            if any(abs(w - float(b)) <= 2 for w, _, _ in getallen):
                tel["builtArea komt letterlijk in tekst voor"] += 1
            # groter getal dan builtArea genoemd?
            if any(w > float(b) * 1.05 and w < float(b) * 4 for w, _, _ in getallen):
                tel["groter getal dan builtArea in tekst"] += 1
        bruikbaar.append({"ref": p.get("ref"), "type": p.get("type"), "town": p.get("town"),
                          "built": p.get("builtArea"), "plot": p.get("plotArea"),
                          "getallen": getallen[:12], "raak": [k for k, v in raak.items() if v]})
    print(f"villa-achtig: {villas}")
    for k, v in tel.most_common():
        print(f"  {v:5d}  {k}")
    json.dump(bruikbaar, open(
        "/private/tmp/claude-501/-Users-root-admin-tree-es/a3ae9710-3e66-42bb-b602-476120d4027d/scratchpad/tekst_analyse.json",
        "w"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()

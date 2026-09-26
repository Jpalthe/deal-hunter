"""Lezer voor de eigen websites van makelaars.

Waarom: niet elke makelaar zet alles op de portalen. Wat alleen op de eigen site staat, ziet
niemand anders — en dat is precies het aanbod waar minder concurrentie op zit.

Hoe, binnen de regels van Jan:
  1. Eerst robots.txt. Verbiedt die het lezen van de aanbodpagina's, dan lezen we niet en vragen we
     die makelaar om zijn feed. Er wordt niets omzeild en nergens ingelogd.
  2. Dan de sitemap en de aanbodpagina's (te koop), daaruit de objectpagina's.
  3. Per objectpagina: eerst schema.org JSON-LD als dat er staat, anders de Open Graph-tags, anders
     de zichtbare tekst met vaste patronen (referentie, prijs, bebouwd, perceel, slaapkamers).
  4. Nooit sneller dan één verzoek per twee seconden per site, met een herkenbare User-Agent.

Wat er wordt bewaard: dezelfde velden als bij elke andere bron. Geen namen van medewerkers of
eigenaren, geen telefoonnummers uit de pagina.

De lijst met kantoren staat in kader/makelaars.json; per kantoor staat daar of lezen is toegestaan
en wat de aanbodpagina's zijn. Die lijst komt uit de inventaris van 24-09-2026 en is per site
nagelopen op robots.txt en gebruiksvoorwaarden.
"""
from __future__ import annotations

import hashlib
import html as htmlmod
import json
import logging
import re
import time
import urllib.robotparser
from dataclasses import dataclass, field
from urllib.parse import urljoin, urlparse

import httpx

from .. import config, coordinaat

log = logging.getLogger("dh.makelaars")

KANTOREN = config.KADER / "makelaars.json"
PAUZE_S = 2.0                 # minimaal tussen twee verzoeken aan dezelfde site
MAX_OBJECTEN_PER_SITE = 400   # bovengrens per ronde, zodat één grote site de ronde niet opeet
MAX_INDEXPAGINAS = 40
RONDE_BUDGET_S = 75 * 60      # een ronde leest hooguit 75 minuten; de rest komt de volgende ronde aan de beurt
STAND = config.DATA / "makelaars-stand.json"   # wanneer welk kantoor voor het laatst is gelezen

# Objectpagina's herkennen aan de URL. Ruim, want elke site doet het anders; de pagina zelf beslist.
OBJECT_URL = re.compile(
    r"(venta|sale|verkauf|te-koop|inmueble|property|propiedad|propiedades|villa|chalet|parcela|solar|terreno|"
    r"apartamento|apartment|piso|casa|finca|townhouse|bungalow|ref[-_/]?\d|-es\d{4,9}\.html|-gb\d{4,9}\.html|"
    r"/p/\d+|/id/\d+|property-\d+|inmueble-\d+)", re.I)
INDEX_URL = re.compile(r"(venta|sale|for-sale|comprar|buy|te-koop|kaufen|propiedades|properties|inmuebles|listado|resultados)", re.I)
VERHUUR = re.compile(r"(alquiler|rent|huur|miete|vermiet|rental)", re.I)
NIET_OBJECT = re.compile(r"(contact|about|nosotros|sobre|blog|noticias|news|privacy|cookies|legal|aviso|login|wp-|\.(jpg|jpeg|png|gif|webp|pdf|css|js)$)", re.I)
# Overzichts- en categoriepagina's zien er bedrieglijk uit als een objectpagina: ze hebben dezelfde
# woorden in de URL en er staan prijzen op. Elf rijen van javeahouses.com bleken zo in de database
# te zijn beland, alle met dezelfde prijs van € 50.000 uit het zoekfilter. Die filteren wij hier weg.
OVERZICHT_URL = re.compile(
    r"(/page/\d+|[?&](?:view|orderby|sort|pagina|paged)=|/property-type/|/tipo-de-propiedad/|/property-city/|"
    r"/categoria/|/category/|/tag/|/zona/|/location/|/busqueda|/search|/resultados|/listado)", re.I)
OVERZICHT_TITEL = re.compile(
    r"^(b[uú]squeda|resultados|propiedades|properties|inmuebles|listado|zoekresultaten|p[aá]gina\s*\d|"
    r"apartamento|apartamentos|villa|villas|chalet|chalets|casa adosada|tienda|parcela|parcelas|"
    r"edificio apartamentos|local comercial|bungalow|[aá]tico|d[uú]plex|estudio|finca)\s*(–|-|\||$)", re.I)


def is_overzichtspagina(url: str, titel: str | None) -> bool:
    """Een overzichts- of categoriepagina is geen woning, ook al staat er een prijs op."""
    if OVERZICHT_URL.search(url or ""):
        return True
    return bool(OVERZICHT_TITEL.match((titel or "").strip()))

# Tekstpatronen op de pagina, in het Spaans, Engels, Nederlands en Duits
PRIJS = re.compile(r"(?:€|EUR|euros?)\s*([\d]{1,3}(?:[.\s]\d{3})+|\d{5,8})|([\d]{1,3}(?:[.\s]\d{3})+|\d{5,8})\s*(?:€|EUR|euros?)", re.I)
REF = re.compile(r"(?:N[ºo°]?\.?\s*(?:de\s+)?referencia|referencia|reference|ref\.?|referentie|objekt-?nr\.?|kenmerk)\s*[:#]?\s*([A-Z0-9][A-Z0-9\-_/]{2,20})", re.I)
BEBOUWD = re.compile(r"(?:sup(?:erficie)?\.?\s*(?:construida|útil|util|vivienda)?|built|constructed|living area|wohnfl[aä]che|bebouwd|woonopp(?:ervlak)?)\s*:?\s*(\d{2,5})\s*m", re.I)
PERCEEL = re.compile(r"(?:parcela|solar|terreno|plot|grundst[uü]ck|perceel|kavel|land)\s*(?:size|area|de)?\s*:?\s*(\d{3,6})\s*m", re.I)
# Twee vormen: "Habitaciones 4" (label eerst) en "4 habitaciones" (getal eerst). Label eerst wint,
# anders leest "Habitaciones 4 Baños 1" als "4 baños".
SLAAP_LABEL = re.compile(r"(?:habitaciones|dormitorios|bedrooms|slaapkamers|schlafzimmer)\s*:?\s*(\d{1,2})\b", re.I)
SLAAP_GETAL = re.compile(r"\b(\d{1,2})\s*(?:habitaciones|dormitorios|bedrooms|beds?|slaapkamers|schlafzimmer)\b", re.I)
BAD_LABEL = re.compile(r"(?:baños|bathrooms|badkamers|badezimmer)\s*:?\s*(\d{1,2})\b", re.I)
BAD_GETAL = re.compile(r"\b(\d{1,2})\s*(?:baños|bathrooms|baths?|badkamers|badezimmer)\b", re.I)
M2_LOS = re.compile(r"(\d{2,6})\s*m(?:2|²)")


@dataclass
class Kantoor:
    naam: str
    website: str
    host: str
    toegestaan: bool
    aanbod_urls: list[str] = field(default_factory=list)
    sitemap_url: str | None = None
    cms: str | None = None
    advies: str = "lezen"
    plaats: str | None = None
    crawl_delay: float | None = None


def laad_kantoren() -> list[Kantoor]:
    try:
        d = json.loads(KANTOREN.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return []
    out = []
    for k in d.get("kantoren") or []:
        w = (k.get("website") or "").strip()
        if not w:
            continue
        if not w.startswith("http"):
            w = "https://" + w
        host = urlparse(w).netloc.lower().replace("www.", "")
        out.append(Kantoor(naam=k.get("naam") or host, website=w, host=host,
                           toegestaan=(k.get("advies") == "lezen"), aanbod_urls=list(k.get("aanbod_urls") or []),
                           sitemap_url=k.get("sitemap_url"), cms=k.get("cms"), advies=k.get("advies") or "lezen",
                           plaats=k.get("plaats"), crawl_delay=k.get("crawl_delay_s")))
    return out


class Site:
    """Eén makelaarssite: beleefd ophalen, robots respecteren, objectpagina's vinden en lezen."""

    def __init__(self, k: Kantoor, client: httpx.Client):
        self.k = k
        self.c = client
        self.laatste = 0.0
        self.robots = urllib.robotparser.RobotFileParser()
        self.robots_ok = None
        self.verzoeken = 0
        self.pauze = max(PAUZE_S, float(k.crawl_delay or 0))

    # ---------------------------------------------------------------- ophalen
    def _wacht(self) -> None:
        d = time.time() - self.laatste
        if d < self.pauze:
            time.sleep(self.pauze - d)
        self.laatste = time.time()

    def mag(self, url: str) -> bool:
        if self.robots_ok is None:
            robots_url = urljoin(self.k.website, "/robots.txt")
            try:
                self._wacht()
                r = self.c.get(robots_url)
                self.verzoeken += 1
                if r.status_code == 200:
                    self.robots.parse(r.text.splitlines())
                    self.robots_ok = True
                    try:
                        cd = self.robots.crawl_delay(config.USER_AGENT) or self.robots.crawl_delay("*")
                        if cd:
                            self.pauze = max(self.pauze, float(cd))
                    except Exception:  # noqa: BLE001
                        pass
                else:
                    self.robots.parse([])          # geen robots.txt: niets verboden
                    self.robots_ok = True
            except Exception as e:  # noqa: BLE001
                log.warning("%s: robots.txt niet leesbaar (%s); site overgeslagen", self.k.host, e)
                self.robots_ok = False
        if not self.robots_ok:
            return False
        return self.robots.can_fetch(config.USER_AGENT, url) and self.robots.can_fetch("*", url)

    def haal(self, url: str) -> str | None:
        if not self.mag(url):
            log.info("%s: robots.txt verbiedt %s", self.k.host, url)
            return None
        self._wacht()
        try:
            r = self.c.get(url)
            self.verzoeken += 1
            if r.status_code != 200 or "text/html" not in (r.headers.get("content-type") or "") and "xml" not in (r.headers.get("content-type") or ""):
                return None
            return r.text
        except Exception as e:  # noqa: BLE001
            log.info("%s: %s niet opgehaald (%s)", self.k.host, url, str(e)[:80])
            return None

    # ---------------------------------------------------------------- vinden
    def sitemap_urls(self) -> list[str]:
        kandidaten = [self.k.sitemap_url] if self.k.sitemap_url else []
        kandidaten += [urljoin(self.k.website, p) for p in ("/sitemap.xml", "/sitemap_index.xml", "/sitemap-index.xml")]
        for regel in getattr(self.robots, "sitemaps", None) or []:
            kandidaten.append(regel)
        gezien, out = set(), []
        for sm in kandidaten:
            if not sm or sm in gezien:
                continue
            gezien.add(sm)
            t = self.haal(sm)
            if not t:
                continue
            locs = re.findall(r"<loc>\s*([^<\s]+)\s*</loc>", t)
            # een sitemap-index verwijst naar deelsitemaps
            for loc in locs:
                if loc.endswith(".xml") and loc not in gezien and len(gezien) < 12:
                    gezien.add(loc)
                    t2 = self.haal(loc)
                    if t2:
                        out += re.findall(r"<loc>\s*([^<\s]+)\s*</loc>", t2)
                else:
                    out.append(loc)
            if out:
                break
        return out

    def objecten_uit_index(self, url: str) -> tuple[list[str], list[str]]:
        """Objectlinks en vervolgpagina's van één aanbodpagina."""
        t = self.haal(url)
        if not t:
            return [], []
        links = set()
        for href in re.findall(r'href=["\']([^"\'#]+)["\']', t):
            u = urljoin(url, htmlmod.unescape(href))
            if urlparse(u).netloc.lower().replace("www.", "") != self.k.host:
                continue
            links.add(u.split("#")[0])
        objecten = [u for u in links if OBJECT_URL.search(u) and not NIET_OBJECT.search(u) and not VERHUUR.search(u)
                    and not INDEX_URL.search(u.rsplit("/", 1)[-1]) or (OBJECT_URL.search(u) and re.search(r"-(es|gb|en|nl|de)\d{4,9}\.html$", u))]
        vervolg = [u for u in links if u != url and INDEX_URL.search(u) and not VERHUUR.search(u)
                   and (re.search(r"(page|pagina|p)=\d+|-\d+-\d+\.html$|/page/\d+|/\d+/?$", u))]
        return sorted(set(objecten)), sorted(set(vervolg))

    def vind_objecten(self) -> list[str]:
        out: set[str] = set()
        for loc in self.sitemap_urls():
            if OBJECT_URL.search(loc) and not NIET_OBJECT.search(loc) and not VERHUUR.search(loc) \
                    and not OVERZICHT_URL.search(loc) \
                    and not re.search(r"-en-venta-\d+-\d+\.html$", loc):
                out.add(loc)
        te_doen = list(self.k.aanbod_urls)
        gezien: set[str] = set()
        while te_doen and len(gezien) < MAX_INDEXPAGINAS and len(out) < MAX_OBJECTEN_PER_SITE:
            u = te_doen.pop(0)
            if u in gezien:
                continue
            gezien.add(u)
            objs, vervolg = self.objecten_uit_index(u)
            out.update(o for o in objs if not OVERZICHT_URL.search(o))
            te_doen += [v for v in vervolg if v not in gezien]
        # tweetalige Inmoweb-sites: dezelfde woning als -es en -gb; één taal is genoeg
        per_id: dict[str, str] = {}
        rest = []
        for u in sorted(out):
            m = re.search(r"-(es|gb|en|nl|de|fr)(\d{4,9})\.html$", u)
            if m:
                per_id.setdefault(m.group(2), u)
            else:
                rest.append(u)
        return (list(per_id.values()) + rest)[:MAX_OBJECTEN_PER_SITE]

    # ---------------------------------------------------------------- lezen
    def lees(self, url: str) -> dict | None:
        t = self.haal(url)
        if not t:
            return None
        rec = ontleed(t, url, self.k)
        if not rec or not rec.get("price"):
            return None
        if rec.get("_verhuur"):
            return None
        return rec


# -------------------------------------------------------------------- ontleden

def _num(s) -> float | None:
    if s is None:
        return None
    s = str(s).replace(".", "").replace(" ", "").replace(" ", "").replace(",", ".")
    try:
        return float(s)
    except ValueError:
        return None


def _jsonld(t: str) -> list[dict]:
    out = []
    for m in re.findall(r"<script[^>]+ld\+json[^>]*>(.*?)</script>", t, re.S | re.I):
        try:
            j = json.loads(m.strip())
        except json.JSONDecodeError:
            continue
        if isinstance(j, dict) and "@graph" in j:
            out += [x for x in j["@graph"] if isinstance(x, dict)]
        elif isinstance(j, list):
            out += [x for x in j if isinstance(x, dict)]
        elif isinstance(j, dict):
            out.append(j)
    return out


def _tekst(t: str) -> str:
    t2 = re.sub(r"<script.*?</script>|<style.*?</style>|<noscript.*?</noscript>", " ", t, flags=re.S | re.I)
    t2 = re.sub(r"<(br|/p|/div|/li|/h\d|/tr)[^>]*>", "\n", t2, flags=re.I)
    txt = htmlmod.unescape(re.sub(r"<[^>]+>", " ", t2))
    return re.sub(r"[ \t\r\f\v]+", " ", txt)


def ontleed(t: str, url: str, k: Kantoor) -> dict | None:
    """Van HTML naar het gewone advertentierecord. Bronvolgorde: JSON-LD, Open Graph, tekst."""
    og = {a.lower(): htmlmod.unescape(b) for a, b in re.findall(r'<meta[^>]+property=["\'](og:[a-z:_]+)["\'][^>]+content=["\']([^"\']*)["\']', t, re.I)}
    title = og.get("og:title") or htmlmod.unescape((re.search(r"<title>(.*?)</title>", t, re.S | re.I) or [None, ""])[1]).strip()
    txt = _tekst(t)
    # Tweede zeef, nu de titel bekend is: een categorie- of zoekpagina is geen woning.
    if is_overzichtspagina(url, title):
        return None
    # Verhuur alleen herkennen aan de titel: het zoekmenu bovenaan bevat op elke pagina het woord "Alquiler".
    verhuur = bool(VERHUUR.search(title or "")) or bool(re.search(r"\b(alquiler|for rent|te huur|zu vermieten)\b", url, re.I))

    price = built = plot = beds = baths = None
    ref = None
    town = None
    desc = og.get("og:description") or ""
    lat = lon = None

    for j in _jsonld(t):
        typ = str(j.get("@type") or "").lower()
        offers = j.get("offers") if isinstance(j.get("offers"), dict) else (j.get("offers") or [None])[0] if isinstance(j.get("offers"), list) else None
        if offers and offers.get("price") and price is None:
            price = _num(offers.get("price"))
        if j.get("price") and price is None:
            price = _num(j.get("price"))
        fs = j.get("floorSize") or j.get("size")
        if isinstance(fs, dict) and fs.get("value") and built is None:
            built = _num(fs.get("value"))
        if j.get("numberOfRooms") and beds is None:
            beds = int(_num(j.get("numberOfRooms")) or 0) or None
        if j.get("numberOfBathroomsTotal") and baths is None:
            baths = int(_num(j.get("numberOfBathroomsTotal")) or 0) or None
        adr = j.get("address")
        if isinstance(adr, dict) and adr.get("addressLocality") and not town:
            town = str(adr["addressLocality"])
        geo = j.get("geo")
        if isinstance(geo, dict) and geo.get("latitude") and geo.get("longitude"):
            lat, lon = _num(geo["latitude"]), _num(geo["longitude"])
        if j.get("description") and not desc:
            desc = str(j["description"])
        if j.get("sku") and not ref:
            ref = str(j["sku"])
        if typ in ("realestatelisting", "product", "residence", "house", "apartment", "singlefamilyresidence", "offer") and not title:
            title = str(j.get("name") or "")

    # De echte referentie heeft een cijfer in zich; "Indique la referencia" uit het zoekformulier niet.
    # Vanaf die regel begint het detailblok; daarvóór staan menu's, filters en uitgelichte woningen
    # met hun eigen prijzen, die anders meelezen.
    detail = txt
    if ref is None:
        for m in REF.finditer(txt):
            w = m.group(1).strip(".:")
            if re.search(r"\d", w) and not re.fullmatch(r"\d{1,2}", w) and len(w) >= 3:
                ref = w
                detail = txt[m.start():]
                break
    if price is None:
        # eerst de prijs vlak na de referentie (het detailblok), pas daarna de rest van de pagina
        for stuk in (detail[:1200], txt[:6000]):
            for m in PRIJS.finditer(stuk):
                v = _num(m.group(1) or m.group(2))
                if v and 20_000 <= v <= 30_000_000:
                    price = v
                    break
            if price is not None:
                break
    if built is None:
        m = BEBOUWD.search(detail)
        if m:
            built = _num(m.group(1))
    if plot is None:
        m = PERCEEL.search(detail)
        if m:
            plot = _num(m.group(1))
    if beds is None:
        m = SLAAP_LABEL.search(detail) or SLAAP_GETAL.search(detail)
        if m:
            b = int(m.group(1))
            beds = b if 0 < b <= 15 else None
    if baths is None:
        m = BAD_LABEL.search(detail) or BAD_GETAL.search(detail)
        if m:
            b = int(m.group(1))
            baths = b if 0 < b <= 12 else None
    if built is None and plot is None:
        # kale m²-getallen: de eerste redelijke is meestal bebouwd, een grote tweede het perceel
        ms = [_num(x) for x in M2_LOS.findall(detail[:8000])]
        ms = [x for x in ms if x]
        if ms:
            built = next((x for x in ms if 30 <= x <= 2000), None)
            plot = next((x for x in ms if x >= 300 and x != built), None)

    # type uit titel of URL
    laag = f"{title} {url}".lower()
    if re.search(r"parcela|solar|terreno|plot|grundst|kavel|\bland\b", laag):
        typ_ = "Land"
    elif re.search(r"apartamento|apartment|piso|ático|atico|penthouse|appartement|wohnung", laag):
        typ_ = "Apartment"
    elif re.search(r"adosad|townhouse|terraced|casa de pueblo|rijwoning|reihenhaus|casa-de-pueblo", laag):
        typ_ = "Town house"
    elif re.search(r"local|comercial|commercial|nave|oficina|garaje|garage|trastero", laag):
        typ_ = "Commercial"
    elif re.search(r"finca|casa de campo|country|cortijo|masia|landhaus", laag):
        typ_ = "Country House"
    else:
        typ_ = "Villa"
    if typ_ == "Land":
        plot = plot or built
        built = None

    # Plaats: eerst uit de URL (Inmoweb zet "-en-<plaats>-" in elk adres), dan uit de titel, dan uit de
    # omschrijving. Nooit uit de paginatekst: het menu noemt op elke pagina alle plaatsen, en dan
    # wordt een villa in Benitachell een villa in Jávea.
    PLAATSEN = (("javea", "Jávea"), ("xabia", "Jávea"), ("benitachell", "Benitachell"), ("benitatxell", "Benitachell"),
                ("cumbre-del-sol", "Benitachell"), ("cumbre del sol", "Benitachell"), ("moraira", "Moraira"),
                ("teulada", "Teulada"), ("denia", "Dénia"), ("calpe", "Calpe"), ("calp", "Calpe"), ("benissa", "Benissa"),
                ("gata-de-gorgos", "Gata de Gorgos"), ("gata de gorgos", "Gata de Gorgos"), ("pedreguer", "Pedreguer"),
                ("ondara", "Ondara"), ("altea", "Altea"), ("benidorm", "Benidorm"), ("alfaz", "L'Alfàs del Pi"),
                ("finestrat", "Finestrat"), ("el-verger", "El Verger"), ("orba", "Orba"), ("pego", "Pego"),
                ("els-poblets", "Els Poblets"), ("oliva", "Oliva"))

    def _plaats(s: str) -> str | None:
        s = (s or "").lower().replace("á", "a").replace("à", "a").replace("é", "e").replace("è", "e")
        for sleutel, naam in PLAATSEN:
            if sleutel in s:
                return naam
        return None

    if not town:
        m_url = re.search(r"-en-([a-z\-]+?)(?:-con-|-es\d|-gb\d|-\d|\.html)", url.lower())
        town = _plaats(m_url.group(1) if m_url else "") or _plaats(title) or _plaats(desc[:400])
    area = config.area_of(town or "", None, None)

    tekst_beschrijving = desc or ""
    if len(tekst_beschrijving) < 120:
        # een langer stuk lopende tekst uit de pagina, zonder menu's: de langste alinea
        alineas = [a.strip() for a in txt.split("\n") if len(a.strip()) > 120]
        if alineas:
            tekst_beschrijving = max(alineas, key=len)[:1500]

    if not config.valid_coord(lat, lon):
        # Geen geo in de JSON-LD. Sommige sites zetten het punt elders in de pagina, maar alleen
        # bij een site waarvan gemeten is dat dat punt per object verschilt (zie dh/coordinaat.py).
        punt = coordinaat.uit_pagina(t, k.host)
        if punt:
            lat, lon = punt

    rec = {
        "source_ref": ref or hashlib.sha1(url.encode("utf-8")).hexdigest()[:12],
        "area": area, "town": config.norm_place(town or ""), "town_raw": town or "", "postcode": None,
        "type": typ_, "price": price, "currency": "EUR",
        "built_m2": built, "plot_m2": plot, "beds": beds, "baths": baths,
        "lat": lat if config.valid_coord(lat, lon) else None, "lon": lon if config.valid_coord(lat, lon) else None,
        "location_detail": "", "url": url, "title": (title or "")[:200],
        "desc_hash": hashlib.sha256(tekst_beschrijving.encode("utf-8")).hexdigest()[:16],
        "desc_excerpt": tekst_beschrijving[:600], "features": [], "images_count": len(re.findall(r"<img", t)),
        "image_url": (og.get("og:image") or "").strip() or None,
        "source_date": None, "new_build": 1 if re.search(r"obra nueva|new build|nieuwbouw|neubau", laag) else 0,
        "_text": f"{title} {tekst_beschrijving}", "_features": "", "_verhuur": verhuur, "_kantoor": k.naam,
    }
    return rec


# -------------------------------------------------------------------- ronde

def lees_alles(alleen: list[str] | None = None, max_per_site: int | None = None) -> tuple[dict[str, list[dict]], dict]:
    """Leest alle toegestane kantoren. Geeft per kantoor de records en een verslag."""
    kantoren = laad_kantoren()
    if alleen:
        kantoren = [k for k in kantoren if k.host in alleen or k.naam in alleen]
    verslag: dict = {"kantoren": {}, "overgeslagen": [], "uitgesteld": []}
    uit: dict[str, list[dict]] = {}
    # Rotatie: het kantoor dat het langst niet is gelezen gaat voor. Zo komt met een tijdbudget per
    # ronde elk kantoor om de beurt aan bod in plaats van altijd dezelfde eerste tien.
    try:
        stand = json.loads(STAND.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        stand = {}
    if not alleen:
        kantoren.sort(key=lambda k: stand.get(k.host, 0))
    start = time.time()
    with httpx.Client(timeout=config.HTTP_TIMEOUT, follow_redirects=True,
                      headers={"User-Agent": config.USER_AGENT, "Accept-Language": "es,en;q=0.8,nl;q=0.6"}) as c:
        for k in kantoren:
            if not k.toegestaan:
                verslag["overgeslagen"].append({"kantoor": k.naam, "reden": f"advies: {k.advies}"})
                continue
            if not alleen and time.time() - start > RONDE_BUDGET_S:
                verslag["uitgesteld"].append(k.naam)
                continue
            site = Site(k, c)
            t0 = time.time()
            try:
                urls = site.vind_objecten()
                if max_per_site:
                    urls = urls[:max_per_site]
                recs = []
                for u in urls:
                    r = site.lees(u)
                    if r:
                        recs.append(r)
                uit[k.host] = recs
                verslag["kantoren"][k.host] = {"kantoor": k.naam, "objectpagina's": len(urls), "gelezen": len(recs),
                                               "in_werkgebied": sum(1 for r in recs if r["area"]),
                                               "verzoeken": site.verzoeken, "seconden": round(time.time() - t0)}
                log.info("%s: %s objectpagina's, %s gelezen, %s in werkgebied", k.host, len(urls), len(recs),
                         verslag["kantoren"][k.host]["in_werkgebied"])
                stand[k.host] = time.time()
                try:
                    STAND.parent.mkdir(parents=True, exist_ok=True)
                    STAND.write_text(json.dumps(stand), encoding="utf-8")
                except OSError:
                    pass
            except Exception as e:  # noqa: BLE001 — één kapotte site mag de ronde niet stoppen
                verslag["kantoren"][k.host] = {"kantoor": k.naam, "fout": str(e)[:160]}
                log.warning("%s: mislukt (%s)", k.host, e)
    return uit, verslag

"""Tekst uit een PDF halen met alleen de standaardbibliotheek.

Genoeg voor rapporten die met gewone objecten zijn opgebouwd (geen objectstromen voor de
paginabomen): per pagina de /Resources /Font opzoeken, de /ToUnicode-CMap lezen en de
Tj/TJ-operatoren daarmee terugvertalen naar leesbare tekst.
"""
from __future__ import annotations
import re, sys, zlib


class Pdf:
    def __init__(self, pad: str):
        self.d = open(pad, "rb").read()
        self.obj: dict[int, tuple[int, int]] = {}
        for m in re.finditer(rb"(?:^|[\r\n\s])(\d+)\s+(\d+)\s+obj\b", self.d):
            self.obj[int(m.group(1))] = (m.end(), m.start())
        self._cache: dict[int, bytes] = {}

    def ruw(self, nr: int) -> bytes:
        if nr in self._cache:
            return self._cache[nr]
        if nr not in self.obj:
            return b""
        s = self.obj[nr][0]
        e = self.d.find(b"endobj", s)
        b = self.d[s:e if e > 0 else s + 200000]
        self._cache[nr] = b
        return b

    def stroom(self, nr: int) -> bytes:
        b = self.ruw(nr)
        m = re.search(rb"stream\r?\n", b)
        if not m:
            return b""
        e = b.rfind(b"endstream")
        rauw = b[m.end():e if e > 0 else len(b)]
        if b"/FlateDecode" in b[:m.start()]:
            try:
                return zlib.decompress(rauw)
            except Exception:  # noqa: BLE001
                try:
                    return zlib.decompressobj().decompress(rauw)
                except Exception:  # noqa: BLE001
                    return b""
        return rauw


def _cmap(data: bytes) -> dict[int, str]:
    kaart: dict[int, str] = {}
    for m in re.finditer(rb"beginbfchar(.*?)endbfchar", data, re.S):
        for a, b in re.findall(rb"<([0-9A-Fa-f]+)>\s*<([0-9A-Fa-f]+)>", m.group(1)):
            kaart[int(a, 16)] = _uni(b)
    for m in re.finditer(rb"beginbfrange(.*?)endbfrange", data, re.S):
        blok = m.group(1)
        for a, b, c in re.findall(rb"<([0-9A-Fa-f]+)>\s*<([0-9A-Fa-f]+)>\s*<([0-9A-Fa-f]+)>", blok):
            lo, hi, st = int(a, 16), int(b, 16), int(c, 16)
            for i in range(lo, min(hi, lo + 65535) + 1):
                kaart[i] = chr(st + (i - lo))
    return kaart


def _uni(hexs: bytes) -> str:
    b = bytes.fromhex(hexs.decode())
    try:
        return b.decode("utf-16-be")
    except Exception:  # noqa: BLE001
        return b.decode("latin-1", "replace")


def paginas(pad: str):
    p = Pdf(pad)
    # paginaobjecten in documentvolgorde: /Type /Page met /Contents
    pagnrs = [nr for nr in sorted(p.obj) if re.search(rb"/Type\s*/Page[^s]", p.ruw(nr))]
    fontcache: dict[int, dict[int, str]] = {}
    for nr in pagnrs:
        body = p.ruw(nr)
        # fonts
        fonts: dict[str, dict[int, str]] = {}
        fm = re.search(rb"/Font\s*(\d+)\s+0\s+R", body)
        fontdict = p.ruw(int(fm.group(1))) if fm else body
        for naam, ref in re.findall(rb"/(\w+)\s+(\d+)\s+0\s+R", fontdict):
            fo = int(ref)
            if fo not in fontcache:
                tu = re.search(rb"/ToUnicode\s+(\d+)\s+0\s+R", p.ruw(fo))
                fontcache[fo] = _cmap(p.stroom(int(tu.group(1)))) if tu else {}
            fonts[naam.decode()] = fontcache[fo]
        # inhoud
        inhoud = b""
        cm = re.search(rb"/Contents\s+(\d+)\s+0\s+R", body)
        if cm:
            inhoud = p.stroom(int(cm.group(1)))
        else:
            cm = re.search(rb"/Contents\s*\[(.*?)\]", body, re.S)
            if cm:
                for ref in re.findall(rb"(\d+)\s+0\s+R", cm.group(1)):
                    inhoud += p.stroom(int(ref)) + b"\n"
        yield nr, _tekst(inhoud, fonts)


def _tekst(inhoud: bytes, fonts: dict[str, dict[int, str]]) -> str:
    uit: list[str] = []
    huidig: dict[int, str] = {}
    for m in re.finditer(rb"/(\w+)\s+[\d.]+\s+Tf|<([0-9A-Fa-f\s]*)>\s*Tj|\((?:\\.|[^\\()])*\)\s*Tj|\[(.*?)\]\s*TJ|\bTd\b|\bTD\b|\bT\*\b|\bTJ\b", inhoud, re.S):
        s = m.group(0)
        if s.endswith(b"Tf"):
            huidig = fonts.get(m.group(1).decode(), {})
        elif m.group(2) is not None:
            uit.append(_hex(m.group(2), huidig))
        elif s.endswith(b"Tj"):
            uit.append(s[s.find(b"(") + 1:s.rfind(b")")].decode("latin-1"))
        elif m.group(3) is not None:
            for h in re.findall(rb"<([0-9A-Fa-f\s]*)>", m.group(3)):
                uit.append(_hex(h, huidig))
            for t in re.findall(rb"\((?:\\.|[^\\()])*\)", m.group(3)):
                uit.append(t[1:-1].decode("latin-1"))
    return "".join(uit)


def _hex(h: bytes, kaart: dict[int, str]) -> str:
    hs = re.sub(rb"\s", b"", h)
    uit = []
    for i in range(0, len(hs) - 1, 4):
        code = int(hs[i:i + 4], 16)
        uit.append(kaart.get(code, ""))
    return "".join(uit)


if __name__ == "__main__":
    zoek = sys.argv[2] if len(sys.argv) > 2 else None
    for nr, t in paginas(sys.argv[1]):
        if zoek and zoek.lower() not in t.lower():
            continue
        print("=" * 30, "object", nr)
        print(t[:4000])

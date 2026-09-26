"""Minimale lezer voor oude .xls (OLE2 + BIFF8). Alleen standaardbibliotheek.

Genoeg om de tabellen van het Boletín Estadístico Online te lezen: tekst (SST/LABELSST),
getallen (NUMBER, RK, MULRK) en formule-uitkomsten die als getal zijn opgeslagen.
"""
from __future__ import annotations
import struct, sys


# ------------------------------------------------------------------ OLE2
def _ole_streams(data: bytes) -> dict[str, bytes]:
    assert data[:8] == b"\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1", "geen OLE2-bestand"
    ssz = 1 << struct.unpack_from("<H", data, 30)[0]
    mssz = 1 << struct.unpack_from("<H", data, 32)[0]
    n_fat = struct.unpack_from("<I", data, 44)[0]
    dir_start = struct.unpack_from("<I", data, 48)[0]
    mini_start = struct.unpack_from("<I", data, 60)[0]
    difat_start = struct.unpack_from("<I", data, 68)[0]
    n_difat = struct.unpack_from("<I", data, 72)[0]

    def sector(i: int) -> bytes:
        off = 512 + i * ssz
        return data[off:off + ssz]

    # DIFAT
    difat = list(struct.unpack_from("<109I", data, 76))
    nxt = difat_start
    for _ in range(n_difat):
        if nxt >= 0xFFFFFFFA:
            break
        s = sector(nxt)
        vals = struct.unpack(f"<{ssz // 4}I", s)
        difat.extend(vals[:-1])
        nxt = vals[-1]
    difat = [d for d in difat[:n_fat] if d < 0xFFFFFFFA]

    fat: list[int] = []
    for d in difat:
        fat.extend(struct.unpack(f"<{ssz // 4}I", sector(d)))

    def chain(start: int) -> list[int]:
        out, cur, seen = [], start, set()
        while cur < 0xFFFFFFFA and cur not in seen:
            seen.add(cur); out.append(cur); cur = fat[cur] if cur < len(fat) else 0xFFFFFFFE
        return out

    def read(start: int, size: int | None = None) -> bytes:
        b = b"".join(sector(i) for i in chain(start))
        return b[:size] if size else b

    # directory
    dirdata = read(dir_start)
    entries = []
    for i in range(0, len(dirdata), 128):
        e = dirdata[i:i + 128]
        if len(e) < 128:
            break
        nlen = struct.unpack_from("<H", e, 64)[0]
        name = e[:max(0, nlen - 2)].decode("utf-16-le", "replace")
        typ = e[66]
        sect = struct.unpack_from("<I", e, 116)[0]
        size = struct.unpack_from("<I", e, 120)[0]
        entries.append((name, typ, sect, size))

    root = next((e for e in entries if e[1] == 5), None)
    mini_stream = read(root[2]) if root else b""
    minifat_raw = read(mini_start) if mini_start < 0xFFFFFFFA else b""
    minifat = list(struct.unpack(f"<{len(minifat_raw) // 4}I", minifat_raw)) if minifat_raw else []

    def read_mini(start: int, size: int) -> bytes:
        out, cur, seen = [], start, set()
        while cur < 0xFFFFFFFA and cur not in seen:
            seen.add(cur)
            out.append(mini_stream[cur * mssz:(cur + 1) * mssz])
            cur = minifat[cur] if cur < len(minifat) else 0xFFFFFFFE
        return b"".join(out)[:size]

    streams = {}
    for name, typ, sect, size in entries:
        if typ != 2:
            continue
        streams[name] = read(sect, size) if size >= 4096 else read_mini(sect, size)
    return streams


# ------------------------------------------------------------------ BIFF8
def _rk(v: int) -> float:
    cents = v & 1
    if v & 2:
        num = float(v >> 2)
    else:
        num = struct.unpack("<d", struct.pack("<q", (v & 0xFFFFFFFC) << 32))[0]
    return num / 100 if cents else num


def _uni(data: bytes, pos: int) -> tuple[str, int]:
    """Korte Unicode-string (16-bits lengte) vanaf pos; geeft (tekst, nieuwe pos)."""
    n = struct.unpack_from("<H", data, pos)[0]
    flags = data[pos + 2]
    pos += 3
    rich = phon = 0
    if flags & 0x08:
        rich = struct.unpack_from("<H", data, pos)[0]; pos += 2
    if flags & 0x04:
        phon = struct.unpack_from("<I", data, pos)[0]; pos += 4
    if flags & 0x01:
        s = data[pos:pos + n * 2].decode("utf-16-le", "replace"); pos += n * 2
    else:
        s = data[pos:pos + n].decode("cp1252", "replace"); pos += n
    pos += rich * 4 + phon
    return s, pos


def _records(stream: bytes):
    pos = 0
    while pos + 4 <= len(stream):
        rid, ln = struct.unpack_from("<HH", stream, pos)
        body = stream[pos + 4:pos + 4 + ln]
        pos += 4 + ln
        yield rid, body, pos


class _Chunks:
    """De SST staat verspreid over SST + CONTINUE-records. Een string mag over de grens lopen;
    het eerste byte van het volgende record is dan een nieuwe vlaggenbyte (samengeperst of niet).
    Deze lezer houdt daarom de recordgrenzen vast in plaats van alles aaneen te plakken."""

    def __init__(self, delen: list[bytes]):
        self.delen = delen
        self.i = 0
        self.p = 0

    def klaar(self) -> bool:
        while self.i < len(self.delen) and self.p >= len(self.delen[self.i]):
            self.i += 1
            self.p = 0
        return self.i >= len(self.delen)

    def over(self) -> int:
        return 0 if self.klaar() else len(self.delen[self.i]) - self.p

    def bytes(self, n: int) -> bytes:
        """n bytes die niet over een recordgrens lopen (kopteksten doen dat nooit)."""
        if self.klaar():
            raise EOFError
        d = self.delen[self.i][self.p:self.p + n]
        self.p += n
        return d

    def tekst(self, tekens: int, breed: bool) -> str:
        uit = []
        while tekens > 0:
            if self.klaar():
                break
            beschikbaar = self.over()
            if beschikbaar == 0:
                continue
            per = 2 if breed else 1
            neem = min(tekens, beschikbaar // per)
            if neem == 0:                      # rest van dit record past niet: naar het volgende
                self.p = len(self.delen[self.i])
                continue
            rauw = self.bytes(neem * per)
            uit.append(rauw.decode("utf-16-le" if breed else "cp1252", "replace"))
            tekens -= neem
            if tekens > 0:                     # string loopt door in het volgende record
                self.p = len(self.delen[self.i])
                if self.klaar():
                    break
                breed = bool(self.bytes(1)[0] & 0x01)
        return "".join(uit)

    def sla_over(self, n: int) -> None:
        while n > 0 and not self.klaar():
            neem = min(n, self.over())
            self.p += neem
            n -= neem


def _sst(stream: bytes) -> list[str]:
    delen: list[bytes] = []
    total = 0
    pos = 0
    gevonden = False
    while pos + 4 <= len(stream):
        rid, ln = struct.unpack_from("<HH", stream, pos)
        body = stream[pos + 4:pos + 4 + ln]
        pos += 4 + ln
        if rid == 0x00FC:
            total = struct.unpack_from("<I", body, 4)[0]
            delen.append(body[8:])
            gevonden = True
            continue
        if gevonden:
            if rid == 0x003C:
                delen.append(body)
                continue
            break
    ch = _Chunks(delen)
    out: list[str] = []
    for _ in range(total):
        try:
            if ch.klaar():
                break
            n = struct.unpack("<H", ch.bytes(2))[0]
            flags = ch.bytes(1)[0]
            rich = struct.unpack("<H", ch.bytes(2))[0] if flags & 0x08 else 0
            phon = struct.unpack("<I", ch.bytes(4))[0] if flags & 0x04 else 0
            s = ch.tekst(n, bool(flags & 0x01))
            ch.sla_over(rich * 4 + phon)
            out.append(s)
        except Exception:  # noqa: BLE001
            break
    return out


def sheets(path: str) -> dict[str, dict[tuple[int, int], object]]:
    data = open(path, "rb").read()
    st = _ole_streams(data)
    wb = st.get("Workbook") or st.get("Book")
    sst = _sst(wb)
    # BOUNDSHEET geeft naam + beginpositie van elke bladstroom
    bounds = []
    for rid, body, _ in _records(wb):
        if rid == 0x0085:
            off = struct.unpack_from("<I", body, 0)[0]
            nlen = body[6]
            flags = body[7]
            nm = body[8:8 + nlen * 2].decode("utf-16-le", "replace") if flags & 1 else body[8:8 + nlen].decode("cp1252", "replace")
            bounds.append((nm, off))
        if rid == 0x000A and bounds:
            break
    uit = {}
    for i, (nm, off) in enumerate(bounds):
        eind = bounds[i + 1][1] if i + 1 < len(bounds) else len(wb)
        cellen: dict[tuple[int, int], object] = {}
        for rid, body, _ in _records(wb[off:eind]):
            if rid == 0x000A:
                break
            if rid == 0x00FD and len(body) >= 10:          # LABELSST
                r, c, idx = struct.unpack_from("<HH", body, 0) + (struct.unpack_from("<I", body, 6)[0],)
                cellen[(r, c)] = sst[idx] if idx < len(sst) else ""
            elif rid == 0x0203 and len(body) >= 14:        # NUMBER
                r, c = struct.unpack_from("<HH", body, 0)
                cellen[(r, c)] = struct.unpack_from("<d", body, 6)[0]
            elif rid == 0x027E and len(body) >= 10:        # RK
                r, c = struct.unpack_from("<HH", body, 0)
                cellen[(r, c)] = _rk(struct.unpack_from("<I", body, 6)[0])
            elif rid == 0x00BD and len(body) >= 6:         # MULRK
                r, c1 = struct.unpack_from("<HH", body, 0)
                c2 = struct.unpack_from("<H", body, len(body) - 2)[0]
                p = 4
                for c in range(c1, c2 + 1):
                    cellen[(r, c)] = _rk(struct.unpack_from("<I", body, p + 2)[0])
                    p += 6
            elif rid == 0x0006 and len(body) >= 20:        # FORMULA met getaluitkomst
                r, c = struct.unpack_from("<HH", body, 0)
                raw = body[6:14]
                if raw[6:8] != b"\xff\xff":
                    cellen[(r, c)] = struct.unpack("<d", raw)[0]
        uit[nm] = cellen
    return uit


if __name__ == "__main__":
    for nm, cel in sheets(sys.argv[1]).items():
        print("=" * 60, nm, len(cel))

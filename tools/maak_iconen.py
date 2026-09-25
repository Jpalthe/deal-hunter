#!/usr/bin/env python3
"""Maakt de pictogrammen voor het icoon op het beginscherm (180, 192 en 512 pixels).

Geen bibliotheken: PNG wordt hier met zlib en struct geschreven. Beeldmerk: een donkergroen vlak
met een lichte boomvorm, in de kleuren van het dashboard. Eén keer draaien is genoeg; het icoon
verandert niet mee met de inhoud.

  python3 tools/maak_iconen.py
"""
from __future__ import annotations

import os
import struct
import sys
import zlib

OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "dh", "static")
BG = (28, 34, 32)          # --deep-pine
LEAF = (184, 160, 122)     # --beige
TRUNK = (140, 120, 90)


def png(path: str, size: int, pixels) -> None:
    raw = b"".join(b"\x00" + bytes(v for x in range(size) for v in pixels(x, y)) for y in range(size))

    def chunk(tag: bytes, data: bytes) -> bytes:
        return struct.pack(">I", len(data)) + tag + data + struct.pack(">I", zlib.crc32(tag + data) & 0xFFFFFFFF)

    ihdr = struct.pack(">IIBBBBB", size, size, 8, 2, 0, 0, 0)   # 8 bit, truecolour
    blob = b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", ihdr) + chunk(b"IDAT", zlib.compress(raw, 9)) + chunk(b"IEND", b"")
    with open(path, "wb") as f:
        f.write(blob)


def make(size: int) -> None:
    s = size
    cx = s / 2

    def px(x: int, y: int):
        u, v = (x + 0.5) / s, (y + 0.5) / s
        # afgeronde hoeken: buiten de vorm blijft het vlak donker, er is geen transparantie nodig
        # drie kruinen van de boom (driehoeken), van boven naar beneden breder
        for top, bottom, half in ((0.16, 0.44, 0.20), (0.32, 0.60, 0.27), (0.48, 0.76, 0.34)):
            if top <= v <= bottom:
                w = half * (v - top) / (bottom - top)
                if abs(u - 0.5) <= w:
                    return LEAF
        if 0.74 <= v <= 0.86 and abs(x + 0.5 - cx) <= s * 0.045:
            return TRUNK
        return BG

    png(os.path.join(OUT_DIR, f"icon-{size}.png"), size, px)


if __name__ == "__main__":
    for n in (180, 192, 512):
        make(n)
        print("geschreven:", os.path.normpath(os.path.join(OUT_DIR, f"icon-{n}.png")))
    sys.exit(0)

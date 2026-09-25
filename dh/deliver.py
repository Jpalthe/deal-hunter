"""Bezorging: Discord-webhook en e-mail (Resend). Zonder sleutels wordt bezorging overgeslagen en gelogd.
Er wordt nooit iets naar makelaars, banken of eigenaren gestuurd; alleen naar Jan."""
from __future__ import annotations

import logging

import httpx

log = logging.getLogger("dh.deliver")


def discord(env: dict, md: str, report_url: str | None) -> str:
    url = env.get("DISCORD_WEBHOOK_URL")
    if not url:
        return "discord: overgeslagen (geen DISCORD_WEBHOOK_URL in .env)"
    content = md
    if report_url:
        content += f"\n\nVolledig rapport: {report_url}"
    # Discord: max 2000 tekens per bericht
    chunks = [content[i:i + 1900] for i in range(0, len(content), 1900)][:4]
    with httpx.Client(timeout=20) as c:
        for ch in chunks:
            r = c.post(url, json={"content": ch, "username": "TREE Deal Hunter"})
            if r.status_code >= 300:
                return f"discord: fout {r.status_code}"
    return f"discord: verzonden ({len(chunks)} bericht(en))"


def email(env: dict, subject: str, html: str) -> str:
    key, to, frm = env.get("RESEND_API_KEY"), env.get("DH_EMAIL_TO"), env.get("DH_EMAIL_FROM")
    if not (key and to and frm):
        return "e-mail: overgeslagen (RESEND_API_KEY, DH_EMAIL_TO of DH_EMAIL_FROM ontbreekt in .env)"
    with httpx.Client(timeout=20) as c:
        r = c.post("https://api.resend.com/emails", headers={"Authorization": f"Bearer {key}"},
                   json={"from": frm, "to": [t.strip() for t in to.split(",")], "subject": subject, "html": html})
    if r.status_code >= 300:
        return f"e-mail: fout {r.status_code} {r.text[:120]}"
    return "e-mail: verzonden"

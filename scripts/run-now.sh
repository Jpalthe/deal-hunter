#!/bin/zsh
# Eén ronde van de Deal Hunter draaien (zelfde omgeving als launchd).
cd /Users/root-admin/tree-es/deal-hunter || exit 1
exec /Users/root-admin/.hermes/hermes-agent/venv/bin/python -m dh.run "$@"

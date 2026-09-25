"""Compatibiliteit: de launchd-dienst start dh.review:app. Het dashboard staat in dh/dashboard.py."""
from .dashboard import app  # noqa: F401

# /// script
# name = "spoolman-settings-manager"
# version = "0.1.0"
# requires-python = ">=3.9"
# dependencies = []
# ///

import json
import os
from pathlib import Path

DEFAULT_SETTINGS = {
    "spoolman_url": "http://localhost:7912",
    "api_key": "",
    "username": "",
    "password": "",
    "auth_mode": "none",
    "timeout_seconds": 10,
    "preset_dir": "",
    "naming_template": "{brand} {type} {spool_id}",
    "gcode_template": "SET_ACTIVE_SPOOL ID={spool_id}",
    "import_fields": [
        "brand",
        "type",
        "color",
        "spool_id",
        "material",
        "weight",
        "remaining_weight"
    ],
    "show_existing_items": True,
    "auto_select_new_items": True,
    "duplicate_action": "ask",
    "selected_endpoints": [
        "/api/v1/filaments",
        "/api/v1/spools",
        "/api/filaments",
        "/api/spools"
    ]
}

class SettingsManager:
    def __init__(self, app_dir=None):
        if app_dir is None:
            app_dir = os.path.join(os.path.expanduser("~"), ".orcaslicer", "plugins", "spoolman")
        self.app_dir = Path(app_dir)
        self.app_dir.mkdir(parents=True, exist_ok=True)
        self.settings_path = self.app_dir / "settings.json"

    def default_settings(self):
        return json.loads(json.dumps(DEFAULT_SETTINGS))

    def load(self):
        if not self.settings_path.exists():
            self.save(self.default_settings())
            return self.default_settings()

        try:
            with open(self.settings_path, "r", encoding="utf-8") as f:
                loaded = json.load(f)
        except (ValueError, OSError):
            loaded = self.default_settings()

        merged = self.default_settings()
        merged.update(loaded)
        return merged

    def save(self, settings):
        with open(self.settings_path, "w", encoding="utf-8") as f:
            json.dump(settings, f, indent=2, ensure_ascii=False)
            f.write("\n")

    def get(self, key, default=None):
        settings = self.load()
        return settings.get(key, default)

    def set(self, key, value):
        settings = self.load()
        settings[key] = value
        self.save(settings)

    def validate(self):
        settings = self.load()
        errors = []

        if not settings.get("spoolman_url", "").strip():
            errors.append("SpoolMan URL is required")

        if settings.get("auth_mode") == "api_key" and not settings.get("api_key", "").strip():
            errors.append("API key is required when auth mode is api_key")

        if settings.get("auth_mode") == "basic" and (
            not settings.get("username", "").strip() or not settings.get("password", "").strip()
        ):
            errors.append("Username and password are required when auth mode is basic")

        if settings.get("preset_dir", "").strip() and not os.path.exists(settings["preset_dir"]):
            errors.append("Configured preset directory does not exist")

        if not settings.get("naming_template", "").strip():
            errors.append("Naming template cannot be empty")

        return errors

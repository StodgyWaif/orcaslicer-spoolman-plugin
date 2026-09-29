# /// script
# name = "spoolman-importer"
# version = "0.1.0"
# requires-python = ">=3.9"
# dependencies = ["requests>=2.28.0"]
# ///

"""SpoolMan Importer for OrcaSlicer - All-in-one plugin"""

import json
import os
import re
from pathlib import Path
from typing import Dict, List, Any, Optional
import requests


# ============================================================================
# Settings Manager
# ============================================================================

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
    "import_fields": ["brand", "type", "color", "spool_id", "material", "weight", "remaining_weight"],
    "show_existing_items": True,
    "auto_select_new_items": True,
    "duplicate_action": "ask",
    "selected_endpoints": ["/api/v1/filaments", "/api/v1/spools", "/api/filaments", "/api/spools"]
}


class SettingsManager:
    """Manages plugin settings persistence"""
    
    def __init__(self, app_dir: Optional[str] = None):
        if app_dir is None:
            app_dir = os.path.join(os.path.expanduser("~"), ".orcaslicer", "plugins", "spoolman")
        self.app_dir = Path(app_dir)
        self.app_dir.mkdir(parents=True, exist_ok=True)
        self.settings_path = self.app_dir / "settings.json"

    def default_settings(self) -> Dict[str, Any]:
        return json.loads(json.dumps(DEFAULT_SETTINGS))

    def load(self) -> Dict[str, Any]:
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

    def save(self, settings: Dict[str, Any]) -> None:
        with open(self.settings_path, "w", encoding="utf-8") as f:
            json.dump(settings, f, indent=2, ensure_ascii=False)
            f.write("\n")

    def get(self, key: str, default: Any = None) -> Any:
        settings = self.load()
        return settings.get(key, default)

    def set(self, key: str, value: Any) -> None:
        settings = self.load()
        settings[key] = value
        self.save(settings)


# ============================================================================
# SpoolMan API Client
# ============================================================================

class SpoolManClient:
    """Fetches filament data from SpoolMan server"""
    
    def __init__(self, settings: Dict[str, Any]):
        self.settings = settings
        self.session = requests.Session()
        self.session.headers.update({"Accept": "application/json"})

    def _build_base_url(self) -> str:
        base_url = self.settings.get("spoolman_url", "").strip().rstrip("/")
        if not base_url:
            raise ValueError("SpoolMan URL is not configured")
        return base_url

    def _auth_headers(self) -> Dict[str, str]:
        mode = self.settings.get("auth_mode", "none")
        headers = {}

        if mode == "api_key":
            api_key = self.settings.get("api_key", "").strip()
            if api_key:
                headers["Authorization"] = f"Bearer {api_key}"
        elif mode == "basic":
            username = self.settings.get("username", "").strip()
            password = self.settings.get("password", "").strip()
            if username and password:
                self.session.auth = (username, password)

        return headers

    def _request_json(self, url: str) -> Any:
        headers = self._auth_headers()
        if headers:
            self.session.headers.update(headers)

        response = self.session.get(url, timeout=self.settings.get("timeout_seconds", 10))
        response.raise_for_status()

        response_text = response.text.strip()
        if not response_text:
            return []

        try:
            return response.json()
        except ValueError:
            raise ValueError("SpoolMan response is not valid JSON")

    def fetch_filaments(self) -> List[Dict[str, Any]]:
        """Fetch filament inventory from SpoolMan"""
        base_url = self._build_base_url()
        endpoints = self.settings.get("selected_endpoints", [
            "/api/v1/filaments",
            "/api/v1/spools",
            "/api/filaments",
            "/api/spools"
        ])

        last_error = None
        for endpoint in endpoints:
            url = base_url + endpoint
            try:
                data = self._request_json(url)
                items = self._normalize_filaments(data)
                if items:
                    return items
            except Exception as exc:
                last_error = exc
                continue

        if last_error:
            raise last_error
        return []

    def _normalize_filaments(self, payload: Any) -> List[Dict[str, Any]]:
        """Normalize SpoolMan response to standard format"""
        if isinstance(payload, list):
            records = payload
        elif isinstance(payload, dict):
            if "filaments" in payload:
                records = payload["filaments"]
            elif "data" in payload:
                records = payload["data"]
            elif "spools" in payload:
                records = payload["spools"]
            else:
                records = [payload]
        else:
            return []

        normalized = []
        for item in records:
            if not isinstance(item, dict):
                continue

            record = {
                "spool_id": item.get("spool_id") or item.get("id") or item.get("spoolId") or item.get("name"),
                "brand": item.get("brand") or item.get("manufacturer") or item.get("vendor") or "Unknown",
                "type": item.get("type") or item.get("material") or item.get("material_type") or item.get("filament_type") or "Unknown",
                "material": item.get("material") or item.get("filament_type") or item.get("type") or "Unknown",
                "color": item.get("color") or item.get("colour") or item.get("filament_color") or "Unknown",
                "weight": item.get("weight") or item.get("remaining_weight") or item.get("spool_weight"),
                "remaining_weight": item.get("remaining_weight") or item.get("weight") or item.get("spool_weight"),
                "diameter": item.get("diameter") or item.get("filament_diameter"),
                "density": item.get("density") or item.get("filament_density"),
                "nozzle_temp": item.get("nozzle_temp") or item.get("nozzle_temperature"),
                "bed_temp": item.get("bed_temp") or item.get("bed_temperature"),
                "price": item.get("price"),
                "notes": item.get("notes") or item.get("comment") or "",
                "raw": item
            }
            normalized.append(record)
        return normalized


# ============================================================================
# Preset Importer
# ============================================================================

class PresetImportBuilder:
    """Creates OrcaSlicer filament presets from SpoolMan data"""
    
    def __init__(self, settings: Dict[str, Any]):
        self.settings = settings

    def build_name(self, item: Dict[str, Any], naming_template: Optional[str] = None) -> str:
        """Generate preset name from template"""
        template = naming_template or "{brand} {type} {spool_id}"
        variables = {
            "brand": str(item.get("brand", "") or "Unknown"),
            "type": str(item.get("type", "") or item.get("material", "") or "Unknown"),
            "material": str(item.get("material", "") or "Unknown"),
            "color": str(item.get("color", "") or "Unknown"),
            "spool_id": str(item.get("spool_id", "") or "Unknown"),
            "weight": str(item.get("weight", "") or ""),
            "remaining_weight": str(item.get("remaining_weight", "") or ""),
            "diameter": str(item.get("diameter", "") or ""),
            "density": str(item.get("density", "") or ""),
            "nozzle_temp": str(item.get("nozzle_temp", "") or ""),
            "bed_temp": str(item.get("bed_temp", "") or ""),
            "notes": str(item.get("notes", "") or "")
        }

        try:
            rendered = template.format(**variables)
        except Exception:
            rendered = f"{variables['brand']} {variables['type']} {variables['spool_id']}"

        sanitized = re.sub(r"[^A-Za-z0-9 _\-().]", "_", rendered)
        sanitized = sanitized.strip()
        return sanitized or "Imported_Filament"

    def build_gcode(self, item: Dict[str, Any], gcode_template: Optional[str] = None) -> str:
        """Generate G-code from template"""
        template = gcode_template or "SET_ACTIVE_SPOOL ID={spool_id}"
        variables = {
            "brand": str(item.get("brand", "") or ""),
            "type": str(item.get("type", "") or item.get("material", "") or ""),
            "material": str(item.get("material", "") or ""),
            "color": str(item.get("color", "") or ""),
            "spool_id": str(item.get("spool_id", "") or ""),
            "weight": str(item.get("weight", "") or ""),
            "remaining_weight": str(item.get("remaining_weight", "") or ""),
            "diameter": str(item.get("diameter", "") or ""),
            "density": str(item.get("density", "") or ""),
            "nozzle_temp": str(item.get("nozzle_temp", "") or ""),
            "bed_temp": str(item.get("bed_temp", "") or ""),
            "notes": str(item.get("notes", "") or "")
        }

        try:
            rendered = template.format(**variables)
        except Exception:
            rendered = ""
        return rendered

    def create_import_directory(self) -> str:
        """Get or create preset import directory"""
        preset_dir = self.settings.get("preset_dir", "").strip()
        if not preset_dir:
            preset_dir = os.path.join(os.path.expanduser("~"), ".orcaslicer", "user", "presets", "filaments")
        os.makedirs(preset_dir, exist_ok=True)
        return preset_dir

    def write_preset_file(self, item: Dict[str, Any]) -> str:
        """Write filament preset file"""
        preset_dir = self.create_import_directory()
        
        name = self.build_name(item, self.settings.get("naming_template", "{brand} {type} {spool_id}"))
        filename = f"{name}.json"
        full_path = os.path.join(preset_dir, filename)

        content = {
            "name": name,
            "vendor": item.get("brand", "Unknown"),
            "type": item.get("type", item.get("material", "Unknown")),
            "color": item.get("color", "Unknown"),
            "diameter": str(item.get("diameter") or "1.75"),
            "density": str(item.get("density") or "1.24"),
            "nozzle_temperature": str(item.get("nozzle_temp") or "220"),
            "bed_temperature": str(item.get("bed_temp") or "60"),
            "spool_id": str(item.get("spool_id", "")),
            "material": item.get("material", item.get("type", "Unknown")),
            "gcode": self.build_gcode(item, self.settings.get("gcode_template", "SET_ACTIVE_SPOOL ID={spool_id}"))
        }

        with open(full_path, "w", encoding="utf-8") as f:
            json.dump(content, f, indent=2, ensure_ascii=False)
            f.write("\n")

        return full_path


# ============================================================================
# SpoolMan Page Plugin
# ============================================================================

class SpoolManPage:
    """Main plugin page for SpoolMan integration"""
    
    def __init__(self):
        self.settings_manager = SettingsManager()
        self.settings = self.settings_manager.load()
        self.records: List[Dict[str, Any]] = []
        print("[SpoolMan] SpoolManPage initialized successfully")

    def show_settings_panel(self) -> Dict[str, Any]:
        """Return settings configuration panel"""
        return {
            "title": "SpoolMan Settings",
            "sections": [
                {
                    "name": "Server Connection",
                    "fields": [
                        {
                            "key": "spoolman_url",
                            "label": "SpoolMan URL",
                            "type": "text",
                            "value": self.settings.get("spoolman_url", "http://localhost:7912"),
                            "hint": "e.g., http://localhost:7912"
                        },
                        {
                            "key": "auth_mode",
                            "label": "Authentication Mode",
                            "type": "choice",
                            "choices": ["none", "api_key", "basic"],
                            "value": self.settings.get("auth_mode", "none")
                        },
                        {
                            "key": "api_key",
                            "label": "API Key",
                            "type": "password",
                            "value": self.settings.get("api_key", "")
                        },
                        {
                            "key": "username",
                            "label": "Username",
                            "type": "text",
                            "value": self.settings.get("username", "")
                        },
                        {
                            "key": "password",
                            "label": "Password",
                            "type": "password",
                            "value": self.settings.get("password", "")
                        }
                    ]
                },
                {
                    "name": "Import Options",
                    "fields": [
                        {
                            "key": "naming_template",
                            "label": "Preset Naming Template",
                            "type": "text",
                            "value": self.settings.get("naming_template", "{brand} {type} {spool_id}"),
                            "hint": "Available: {brand}, {type}, {color}, {spool_id}, {material}, {weight}, {diameter}, {nozzle_temp}, {bed_temp}"
                        },
                        {
                            "key": "gcode_template",
                            "label": "Filament Start G-code",
                            "type": "textarea",
                            "value": self.settings.get("gcode_template", "SET_ACTIVE_SPOOL ID={spool_id}"),
                            "hint": "Use variables like {spool_id}, {brand}, {type}, etc."
                        },
                        {
                            "key": "preset_dir",
                            "label": "Preset Directory (optional)",
                            "type": "folder",
                            "value": self.settings.get("preset_dir", "")
                        }
                    ]
                }
            ]
        }

    def fetch_filaments(self) -> Dict[str, Any]:
        """Fetch filaments from SpoolMan"""
        try:
            client = SpoolManClient(self.settings)
            self.records = client.fetch_filaments()
            return {
                "status": "success",
                "message": f"Fetched {len(self.records)} filaments",
                "count": len(self.records)
            }
        except Exception as e:
            return {
                "status": "error",
                "message": f"Failed to fetch: {str(e)}"
            }

    def import_selected(self, indexes: List[int]) -> Dict[str, Any]:
        """Import selected filaments"""
        try:
            importer = PresetImportBuilder(self.settings)
            count = 0
            for idx in indexes:
                if idx < len(self.records):
                    importer.write_preset_file(self.records[idx])
                    count += 1
            return {
                "status": "success",
                "message": f"Imported {count} filaments"
            }
        except Exception as e:
            return {
                "status": "error",
                "message": f"Import failed: {str(e)}"
            }

    def save_settings(self, settings: Dict[str, Any]) -> Dict[str, Any]:
        """Save plugin settings"""
        try:
            self.settings_manager.save(settings)
            self.settings = settings
            return {"status": "success"}
        except Exception as e:
            return {"status": "error", "message": str(e)}


# Export the plugin page class
__all__ = ["SpoolManPage"]

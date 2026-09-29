# /// script
# requires-python = ">=3.9"
# dependencies = []
# [project]
# name = "spoolman-preset-importer"
# version = "0.1.0"
# /// 

import os
import re
from pathlib import Path

class PresetImportBuilder:
    def __init__(self, settings):
        self.settings = settings

    def build_name(self, item, naming_template):
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
            rendered = f"{variables.get('brand', 'Unknown')} {variables.get('type', 'Unknown')} {variables.get('spool_id', 'Unknown')}"

        sanitized = re.sub(r"[^A-Za-z0-9 _\\-().]", "_", rendered)
        sanitized = sanitized.strip()
        return sanitized or "Imported_Filament"

    def build_gcode(self, item, gcode_template):
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
            rendered = gcode_template.format(**variables)
        except Exception:
            rendered = ""

        return rendered

    def build_preset_values(self, item):
        preset = {
            "name": self.build_name(item, self.settings.get("naming_template", "{brand} {type} {spool_id}")),
            "filament_vendor": item.get("brand", "Unknown"),
            "filament_type": item.get("type", item.get("material", "Unknown")),
            "filament_colour": item.get("color", "Unknown"),
            "filament_diameter": item.get("diameter") or "1.75",
            "filament_density": item.get("density") or "1.24",
            "nozzle_temperature": item.get("nozzle_temp") or "220",
            "bed_temperature": item.get("bed_temp") or "60",
            "spool_id": str(item.get("spool_id", "")),
            "material": item.get("material", item.get("type", "Unknown")),
            "raw": item
        }

        return preset

    def create_import_directory(self):
        preset_dir = self.settings.get("preset_dir", "").strip()
        if not preset_dir:
            preset_dir = os.path.join(os.path.expanduser("~"), ".orcaslicer", "user", "presets", "filaments")
        os.makedirs(preset_dir, exist_ok=True)
        return preset_dir

    def write_preset_file(self, item):
        preset_dir = self.create_import_directory()
        preset = self.build_preset_values(item)
        filename = f"{preset['name']}.json"
        full_path = os.path.join(preset_dir, filename)

        content = {
            "name": preset["name"],
            "vendor": preset["filament_vendor"],
            "type": preset["filament_type"],
            "color": preset["filament_colour"],
            "diameter": str(preset["filament_diameter"]),
            "density": str(preset["filament_density"]),
            "nozzle_temperature": str(preset["nozzle_temperature"]),
            "bed_temperature": str(preset["bed_temperature"]),
            "spool_id": str(preset["spool_id"]),
            "material": preset["material"],
            "gcode": self.build_gcode(item, self.settings.get("gcode_template", "SET_ACTIVE_SPOOL ID={spool_id}"))
        }

        with open(full_path, "w", encoding="utf-8") as f:
            import json
            json.dump(content, f, indent=2, ensure_ascii=False)
            f.write("\n")

        return full_path

    def detect_duplicates(self, items):
        seen = {}
        duplicates = []

        for idx, item in enumerate(items):
            spool_id = str(item.get("spool_id", "") or "unknown")
            name = self.build_name(item, self.settings.get("naming_template", "{brand} {type} {spool_id}"))
            key = spool_id.lower()
            if key not in seen:
                seen[key] = name
            else:
                duplicates.append({
                    "spool_id": spool_id,
                    "name": name,
                    "duplicate_of": seen[key]
                })

        return duplicates

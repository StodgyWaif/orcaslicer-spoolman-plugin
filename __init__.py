# /// script
# name = "spoolman-importer"
# version = "0.1.0"
# description = "Imports filament inventory from a SpoolMan server"
# requires-python = ">=3.9"
# dependencies = ["requests>=2.28.0"]
# ///

"""SpoolMan Importer for OrcaSlicer"""

from .settings_manager import SettingsManager
from .spoolman_api import SpoolManClient
from .preset_importer import PresetImportBuilder


class SpoolManPage:
    """Main plugin page class"""
    
    def __init__(self):
        self.settings_manager = SettingsManager()
        self.settings = self.settings_manager.load()
        self.records = []
        print("[SpoolMan] SpoolManPage initialized")
    
    def show_settings_panel(self):
        """Return settings configuration"""
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
                            "value": self.settings.get("spoolman_url", "http://localhost:7912")
                        },
                        {
                            "key": "auth_mode",
                            "label": "Auth Mode",
                            "type": "choice",
                            "choices": ["none", "api_key", "basic"],
                            "value": self.settings.get("auth_mode", "none")
                        }
                    ]
                }
            ]
        }
    
    def fetch_filaments(self):
        """Fetch from SpoolMan"""
        try:
            client = SpoolManClient(self.settings)
            self.records = client.fetch_filaments()
            return {"status": "success", "count": len(self.records)}
        except Exception as e:
            return {"status": "error", "message": str(e)}
    
    def import_selected(self, indexes):
        """Import selected filaments"""
        try:
            importer = PresetImportBuilder(self.settings)
            count = 0
            for idx in indexes:
                if idx < len(self.records):
                    importer.write_preset_file(self.records[idx])
                    count += 1
            return {"status": "success", "count": count}
        except Exception as e:
            return {"status": "error", "message": str(e)}


__all__ = ["SpoolManPage", "SettingsManager", "SpoolManClient", "PresetImportBuilder"]

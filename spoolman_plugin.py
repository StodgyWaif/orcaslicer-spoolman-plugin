# /// script
# name = "spoolman-importer"
# version = "0.1.0"
# description = "Imports filament inventory from a SpoolMan server into OrcaSlicer filament presets."
# requires-python = ">=3.9"
# dependencies = ["requests>=2.28.0"]
# ///

"""
SpoolMan Importer Plugin for OrcaSlicer
Main plugin entry point and Pages UI
"""

import json
import os
from pathlib import Path

try:
    from settings_manager import SettingsManager
    from spoolman_api import SpoolManClient
    from preset_importer import PresetImportBuilder
except ImportError as e:
    print(f"[SpoolMan] Import error: {e}")
    class SettingsManager:
        def load(self):
            return {}
        def save(self, settings):
            pass


class SpoolManPage:
    """
    SpoolMan Importer Page - Main UI entry point
    This class provides the UI for configuring and importing from SpoolMan
    """

    def __init__(self):
        """Initialize the SpoolMan page plugin"""
        self.settings_manager = SettingsManager()
        self.settings = self.settings_manager.load()
        self.records = []
        self.selected_indexes = set()
        
        print("[SpoolMan] Page initialized successfully")

    def show_settings_panel(self):
        """Display the settings configuration panel"""
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
                            "value": self.settings.get("api_key", ""),
                            "condition": "auth_mode == 'api_key'"
                        },
                        {
                            "key": "username",
                            "label": "Username",
                            "type": "text",
                            "value": self.settings.get("username", ""),
                            "condition": "auth_mode == 'basic'"
                        },
                        {
                            "key": "password",
                            "label": "Password",
                            "type": "password",
                            "value": self.settings.get("password", ""),
                            "condition": "auth_mode == 'basic'"
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
                            "label": "Filament Start G-code Template",
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

    def on_fetch_from_spoolman(self):
        """Fetch filament inventory from SpoolMan server"""
        try:
            client = SpoolManClient(self.settings)
            self.records = client.fetch_filaments()
            return {
                "status": "success",
                "message": f"Fetched {len(self.records)} filaments from SpoolMan",
                "records": self.records
            }
        except Exception as e:
            return {
                "status": "error",
                "message": f"Failed to fetch from SpoolMan: {str(e)}"
            }

    def on_import_selected(self, selected_indexes):
        """Import selected filaments into OrcaSlicer"""
        try:
            importer = PresetImportBuilder(self.settings)
            imported_count = 0
            
            for idx in selected_indexes:
                if idx < len(self.records):
                    item = self.records[idx]
                    importer.write_preset_file(item)
                    imported_count += 1
            
            return {
                "status": "success",
                "message": f"Successfully imported {imported_count} filament presets"
            }
        except Exception as e:
            return {
                "status": "error",
                "message": f"Import failed: {str(e)}"
            }

    def on_save_settings(self, new_settings):
        """Save plugin settings"""
        try:
            self.settings_manager.save(new_settings)
            self.settings = new_settings
            return {
                "status": "success",
                "message": "Settings saved successfully"
            }
        except Exception as e:
            return {
                "status": "error",
                "message": f"Failed to save settings: {str(e)}"
            }


def get_plugin_page():
    """Factory function to create the plugin page"""
    return SpoolManPage()

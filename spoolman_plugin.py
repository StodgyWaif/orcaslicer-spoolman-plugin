import os
import json

try:
    import wx
except ImportError:
    wx = None

from settings_manager import SettingsManager
from spoolman_api import SpoolManClient
from preset_importer import PresetImportBuilder

class SpoolManPage:
    """
    Simple starter page object.
    This class is intentionally lightweight and meant to be adapted to the actual OrcaSlicer
    pages plugin API in your installed version.
    """

    def __init__(self, parent=None):
        self.parent = parent
        self.settings_manager = SettingsManager()
        self.settings = self.settings_manager.load()
        self.importer = PresetImportBuilder(self.settings)
        self.records = []
        self.selected_indexes = set()

        if wx is not None:
            self.panel = self._build_ui()

    def _build_ui(self):
        panel = wx.Panel(self.parent, -1)
        sizer = wx.BoxSizer(wx.VERTICAL)

        # Server Settings
        server_box = wx.StaticBox(panel, -1, "SpoolMan Settings")
        server_sizer = wx.StaticBoxSizer(server_box, wx.VERTICAL)

        url_text = wx.TextCtrl(panel, value=self.settings.get("spoolman_url", ""))
        api_key_text = wx.TextCtrl(panel, value=self.settings.get("api_key", ""))
        username_text = wx.TextCtrl(panel, value=self.settings.get("username", ""))
        password_text = wx.TextCtrl(panel, value=self.settings.get("password", ""), style=wx.TE_PASSWORD)
        auth_choice = wx.Choice(panel, choices=["none", "api_key", "basic"])
        auth_choice.SetStringSelection(self.settings.get("auth_mode", "none"))

        server_sizer.Add(wx.StaticText(panel, -1, "URL"), 0, wx.ALL | wx.ALIGN_LEFT, 5)
        server_sizer.Add(url_text, 0, wx.ALL | wx.EXPAND, 5)
        server_sizer.Add(wx.StaticText(panel, -1, "API key"), 0, wx.ALL | wx.ALIGN_LEFT, 5)
        server_sizer.Add(api_key_text, 0, wx.ALL | wx.EXPAND, 5)
        server_sizer.Add(wx.StaticText(panel, -1, "Username"), 0, wx.ALL | wx.ALIGN_LEFT, 5)
        server_sizer.Add(username_text, 0, wx.ALL | wx.EXPAND, 5)
        server_sizer.Add(wx.StaticText(panel, -1, "Password"), 0, wx.ALL | wx.ALIGN_LEFT, 5)
        server_sizer.Add(password_text, 0, wx.ALL | wx.EXPAND, 5)
        server_sizer.Add(wx.StaticText(panel, -1, "Auth mode"), 0, wx.ALL | wx.ALIGN_LEFT, 5)
        server_sizer.Add(auth_choice, 0, wx.ALL | wx.EXPAND, 5)

        # Import Settings
        import_box = wx.StaticBox(panel, -1, "Import Options")
        import_sizer = wx.StaticBoxSizer(import_box, wx.VERTICAL)

        naming_t = wx.TextCtrl(panel, value=self.settings.get("naming_template", "{brand} {type} {spool_id}"))
        gcode_t = wx.TextCtrl(panel, value=self.settings.get("gcode_template", "SET_ACTIVE_SPOOL ID={spool_id}"))
        preset_dir_t = wx.TextCtrl(panel, value=self.settings.get("preset_dir", ""))
        import_fields_t = wx.TextCtrl(panel, value=", ".join(self.settings.get("import_fields", [])))
        import_sizer.Add(wx.StaticText(panel, -1, "Naming template"), 0, wx.ALL | wx.ALIGN_LEFT, 5)
        import_sizer.Add(naming_t, 0, wx.ALL | wx.EXPAND, 5)
        import_sizer.Add(wx.StaticText(panel, -1, "G-code template"), 0, wx.ALL | wx.ALIGN_LEFT, 5)
        import_sizer.Add(gcode_t, 0, wx.ALL | wx.EXPAND, 5)
        import_sizer.Add(wx.StaticText(panel, -1, "Preset directory"), 0, wx.ALL | wx.ALIGN_LEFT, 5)
        import_sizer.Add(preset_dir_t, 0, wx.ALL | wx.EXPAND, 5)
        import_sizer.Add(wx.StaticText(panel, -1, "Import fields"), 0, wx.ALL | wx.ALIGN_LEFT, 5)
        import_sizer.Add(import_fields_t, 0, wx.ALL | wx.EXPAND, 5)

        # Actions
        button_sizer = wx.BoxSizer(wx.HORIZONTAL)
        save_button = wx.Button(panel, label="Save Settings")
        fetch_button = wx.Button(panel, label="Fetch SpoolMan")
        import_button = wx.Button(panel, label="Import Selected")

        button_sizer.Add(save_button, 0, wx.ALL, 5)
        button_sizer.Add(fetch_button, 0, wx.ALL, 5)
        button_sizer.Add(import_button, 0, wx.ALL, 5)

        sizer.Add(server_sizer, 0, wx.ALL | wx.EXPAND, 5)
        sizer.Add(import_sizer, 0, wx.ALL | wx.EXPAND, 5)
        sizer.Add(button_sizer, 0, wx.ALL, 5)

        panel.SetSizerAndFit(sizer)

        def save_settings(event=None):
            settings = self.settings_manager.load()
            settings["spoolman_url"] = url_text.GetValue()
            settings["api_key"] = api_key_text.GetValue()
            settings["username"] = username_text.GetValue()
            settings["password"] = password_text.GetValue()
            settings["auth_mode"] = auth_choice.GetStringSelection()
            settings["naming_template"] = naming_t.GetValue()
            settings["gcode_template"] = gcode_t.GetValue()
            settings["preset_dir"] = preset_dir_t.GetValue()
            settings["import_fields"] = [field.strip() for field in import_fields_t.GetValue().split(",") if field.strip()]
            self.settings_manager.save(settings)
            self.settings = settings

        def fetch_from_spoolman(event=None):
            save_settings()
            client = SpoolManClient(self.settings)
            try:
                self.records = client.fetch_filaments()
                print(f"Fetched {len(self.records)} records from SpoolMan")
            except Exception as exc:
                print(f"SpoolMan fetch failed: {exc}")

        def import_selected(event=None):
            save_settings()
            for idx, item in enumerate(self.records):
                if idx not in self.selected_indexes:
                    continue
                self.importer.write_preset_file(item)

        save_button.Bind(wx.EVT_BUTTON, save_settings)
        fetch_button.Bind(wx.EVT_BUTTON, fetch_from_spoolman)
        import_button.Bind(wx.EVT_BUTTON, import_selected)

        return panel

    def fetch_records(self):
        client = SpoolManClient(self.settings)
        return client.fetch_filaments()

    def run(self):
        if wx is None:
            print("wxPython not available in this environment")
            return
        self.panel.Show()

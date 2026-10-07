# Installation

## Tested Environment

This plugin was tested on **OrcaSlicer 2.5.0-dev**. Other OrcaSlicer builds may work, but should be treated as unverified until reported by testers.

## Cloud Installation
The recommended installation method is via the Orca Cloud plugin subscription.
https://cloud.orcaslicer.com/p/4e00554f8f78


## Local Installation

1. Open the repository's [Releases page](https://github.com/StodgyWaif/orcaslicer-spoolman-plugin/releases).
2. Expand **Assets** for the desired release.
3. Download `spoolman_plugin_win_x86_64.py`.
4. Open OrcaSlicer.
5. Open the **Plugins** window.
6. Select **Install local plugin**.
7. Choose the downloaded `spoolman_plugin_win_x86_64.py`.
8. Refresh the plugin list or fully restart OrcaSlicer.
9. Confirm **SpoolMan Importer** appears and reports the expected version.

The installation file should retain the name:

```text
spoolman_plugin_win_x86_64.py
```

## First-Run Checklist

1. Open **SpoolMan Importer > Settings**.
2. Enter the SpoolMan base URL.
3. Test the connection.
4. Confirm the active OrcaSlicer user filament folder.
5. Discover SpoolMan fields.
6. Review field mappings.
7. Save settings.
8. Refresh inventory.
9. Run Import Preview before importing.

## Upgrading an Existing Installation

1. Open **Settings > Advanced: Index and Folder Maintenance**.
2. Create and validate a full backup.
3. Preserve the currently installed `spoolman_plugin_win_x86_64.py` separately.
4. Download the new release asset.
5. Replace or reinstall the plugin through OrcaSlicer's Plugins window.
6. Fully close and restart OrcaSlicer.
7. Confirm the displayed plugin version.
8. Refresh inventory.
9. Run **Preview SpoolMan Changes** before applying bulk updates.

Existing settings and index data should be normalized automatically, but keep the previous working plugin file until testing is complete.

## Uninstalling

Removing the plugin does not automatically remove:

- Generated OrcaSlicer filament presets.
- Plugin backup files.
- Full backup ZIP archives.
- Plugin settings.
- The plugin import index.

Review these items separately if a complete cleanup is required.

## Distribution Types

### Local Installation

Installed manually from `spoolman_plugin_win_x86_64.py`. GitHub release notifications can be used to identify newer versions.

### Plugin Hub Installation

When the plugin becomes available through OrcaSlicer Plugin Hub, installation and updates may be managed by OrcaSlicer instead of by manual file replacement.

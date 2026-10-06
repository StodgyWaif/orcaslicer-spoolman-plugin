# OrcaSlicer SpoolMan Importer

A development-stage OrcaSlicer plugin that reads SpoolMan inventory and creates or maintains OrcaSlicer filament presets.

> **Development status:** v1.0.72 is an external-testing build. Back up OrcaSlicer presets before testing and review every Import Preview or Synchronization Preview before writing changes.

## Highlights

- Reads spool, filament, vendor, and custom-field data from SpoolMan
- Creates OrcaSlicer filament presets with preview-first workflows
- Supports configurable field mappings and independent plate temperatures
- Recognizes the custom spool field `date_acquired`
- Tracks linked presets, moved files, missing files, and multi-profile spools
- Provides preset backups, full backups, restoration, diagnostics, themes, and update notifications

## Requirements

- A compatible OrcaSlicer build with Python plugin support
- A reachable SpoolMan server
- Permission to write to the selected OrcaSlicer user filament-preset folder

## Quick start

1. Download `spoolman_plugin.py` from the latest GitHub release.
2. In OrcaSlicer, open **Plugins** and choose **Install local plugin**.
3. Restart OrcaSlicer if requested.
4. Open **SpoolMan Importer > Settings**.
5. Enter the SpoolMan URL and select the OrcaSlicer filament folder.
6. Save settings, refresh inventory, and run an Import Preview before importing.

See [Installation](INSTALLATION.md), [Configuration](CONFIGURATION.md), and [Troubleshooting](TROUBLESHOOTING.md).

## Safety model

- SpoolMan is treated as a read-oriented source for preset generation.
- Imports and synchronization are preview-first.
- Existing presets are backed up before managed updates.
- Missing or invalid mapped values do not erase existing Orca values.
- The update checker is informational and does not install files automatically.

## Support

- Use the Bug Report issue template for reproducible defects.
- Use the Feature Request template for proposed enhancements.
- Inspect diagnostic bundles before uploading them publicly.

## License

Choose and add a repository license before broad public distribution. GitHub's license chooser can add a standard license from the repository interface.

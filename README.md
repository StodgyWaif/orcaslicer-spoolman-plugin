# OrcaSlicer SpoolMan Importer

A development-stage OrcaSlicer plugin that reads SpoolMan inventory and creates or maintains OrcaSlicer filament presets.

> **Development status:** v1.0.72 is an external-testing build. This build was tested on **OrcaSlicer 2.5.0-dev**. Compatibility with other OrcaSlicer versions has not yet been fully verified. Back up OrcaSlicer presets before testing and review every Import Preview or Synchronization Preview before writing changes.

## Highlights

- Reads spool, filament, vendor, and custom-field data from SpoolMan
- Creates OrcaSlicer filament presets with preview-first workflows
- Supports configurable field mappings and independent plate temperatures
- Recognizes the user-created spool custom field `date_acquired`
- Tracks linked presets, moved files, missing files, and multi-profile spools
- Provides preset backups, full backups, restoration, diagnostics, themes, and update notifications

## Screenshots

### Inventory and Import Queue

![SpoolMan inventory, filters, status, and Import Queue](screenshots/importer-inventory.png)

### Settings and Common Preferences

![SpoolMan Importer settings and common preferences](screenshots/settings-common-preferences.png)

### Field Mappings and SpoolMan Field Reference

![SpoolMan field mappings and discovered field reference](screenshots/field-mappings.png)

### Managed Orca Profiles

![Managed Orca Profiles status, bulk updates, and linked presets](screenshots/managed-orca-profiles.png)

### Import Preview

![Import Preview showing planned preset changes](screenshots/import-preview.png)

### Backup and Maintenance

![Backup, restore, diagnostics, and maintenance controls](screenshots/backup-maintenance.png)

## Requirements

- A compatible OrcaSlicer build with Python plugin support
- Tested development environment: **OrcaSlicer 2.5.0-dev**
- A reachable SpoolMan server
- Permission to write to the selected OrcaSlicer user filament-preset folder

## Quick start

1. Download `spoolman_plugin.py` from the desired GitHub release.
2. In OrcaSlicer, open **Plugins** and choose **Install local plugin**.
3. Restart OrcaSlicer if requested.
4. Open **SpoolMan Importer > Settings**.
5. Enter the SpoolMan URL and select the OrcaSlicer filament folder.
6. Save settings, refresh inventory, and run an Import Preview before importing.

See [Installation](INSTALLATION.md), [Configuration](CONFIGURATION.md), [Field Mappings](FIELD_MAPPINGS.md), [Backup and Restore](BACKUP_AND_RESTORE.md), and [Troubleshooting](TROUBLESHOOTING.md).

## Safety model

- SpoolMan is treated as a read-oriented source for preset generation.
- Imports and synchronization are preview-first.
- Existing presets are backed up before managed updates.
- Missing or invalid mapped values do not erase existing Orca values.
- The update checker is informational and does not install files automatically.

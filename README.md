# OrcaSlicer SpoolMan Importer

A development-stage OrcaSlicer plugin that reads SpoolMan inventory and creates or maintains OrcaSlicer filament presets.

> [!CAUTION]
> Version 1.0.72 is a development prerelease tested on
> **OrcaSlicer 2.5.0-dev**. The plugin can create and update
> OrcaSlicer filament preset files. Create a full backup before
> testing imports, synchronization, cleanup, or restoration.

## Features

### Inventory and Importing

- Browse SpoolMan inventory inside OrcaSlicer
- Search, filter, sort, and customize visible columns
- Highlight and filter low-filament spools
- Open individual SpoolMan records in the default browser
- Preview generated presets before writing files
- Control how existing presets are handled

### OrcaSlicer Preset Management

- Generate OrcaSlicer filament presets from SpoolMan records
- Track one or more Orca presets linked to a spool
- Preview differences before synchronization
- Bulk update selected managed fields
- Detect missing, moved, renamed, and locally modified presets
- Back up presets before managed changes

### SpoolMan Field Integration

- Discover built-in and custom spool, filament, and vendor fields
- Configure SpoolMan-to-Orca field mappings
- Map plate temperatures independently
- Validate numeric values before writing them
- Support optional spool custom fields such as `date_acquired`

### Recovery and Diagnostics

- Preset backups
- Import-index backups
- Full ZIP backup and computer transfer
- Pre-restore safety backups
- Diagnostic export with optional sanitized error excerpts
- Stable and Development update-notification channels

## Documentation

- [Installation](INSTALLATION.md)
- [Configuration](CONFIGURATION.md)
- [Field Mappings](FIELD_MAPPINGS.md)
- [Backup and Restore](BACKUP_AND_RESTORE.md)
- [Troubleshooting](TROUBLESHOOTING.md)
- [Changelog](CHANGELOG.md)
- [ocs/RELEASE_CHECKLIST.md

## Download and Install

> Version 1.0.72 was tested on **OrcaSlicer 2.5.0-dev**.

1. Download `spoolman_plugin.py` from the
   [latest GitHub release](https://github.com/StodgyWaif/orcaslicer-spoolman-plugin/releases).
2. Open OrcaSlicer's **Plugins** window.
3. Select **Install local plugin**.
4. Choose `spoolman_plugin.py`.
5. Fully restart OrcaSlicer.
6. Open **SpoolMan Importer > Settings**.

[Installation Guide](INSTALLATION.md) |
[Configuration Guide](CONFIGURATION.md) |
[Troubleshooting](TROUBLESHOOTING.md)

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

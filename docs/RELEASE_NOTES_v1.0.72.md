# SpoolMan Importer v1.0.72

Development prerelease for external testing.

## Tested Environment

- OrcaSlicer 2.5.0-dev
- Local Python plugin installation
- SpoolMan REST API
- OrcaSlicer user filament presets

## Highlights

- SpoolMan inventory browsing, filtering, sorting, and low-filament status
- Preview-first OrcaSlicer filament preset generation
- Built-in and custom SpoolMan field discovery
- Configurable SpoolMan-to-Orca field mappings
- Independent plate-temperature mappings
- Managed Orca profile synchronization
- Bulk updates for existing managed presets
- Preset, index, and full ZIP backups
- Restore and computer-transfer workflows
- Stable and Development update-notification channels
- Orca Dark, Midnight Blue, Graphite, and Light themes

## Safety

- Existing managed presets are backed up before synchronization changes.
- Blank, missing, or invalid mapped values do not erase existing Orca values.
- Imports and synchronization are preview-first.
- Update checks do not download or install files automatically.

## Custom Fields

The plugin discovers custom spool, filament, and vendor fields.

The optional spool field `date_acquired` is supported when present. `date_acquired` is a user-created custom field and is not a default SpoolMan field.

## Installation

1. Expand **Assets** below.
2. Download `spoolman_plugin.py`.
3. Install it through OrcaSlicer's Plugins window.
4. Fully restart OrcaSlicer.
5. Open **SpoolMan Importer > Settings**.

## Important

This is a prerelease. Create a full backup before testing bulk imports, preset synchronization, cleanup, or restoration.

Please report reproducible problems through the Bug Report issue template.

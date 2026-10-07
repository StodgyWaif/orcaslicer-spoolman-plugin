# Configuration

> The v1.0.72 configuration workflow documented here was tested on **OrcaSlicer 2.5.0-dev**. Menu names or plugin-management behavior may differ in other builds.

## SpoolMan Connection

Enter the base URL used to reach SpoolMan. Do not append an individual API endpoint such as `/api/v1/spool`.

Examples:

```text
http://spoolman.local:7912
https://spoolman.example.com
```

Use **Test Connection** before continuing.

## OrcaSlicer Filament Folder

Select the active user filament-preset folder for the OrcaSlicer profile in use. Validate the detected path before allowing writes.

Folder changes may require an OrcaSlicer restart.

## Common Preferences

### Plugin Theme

Choose one of the supported themes:

- Orca Dark
- Midnight Blue
- Graphite
- Light

### Low Filament Threshold

Spools at or below the configured remaining weight are marked as low filament.

Set the threshold to `0` to disable low-filament warnings.

### Existing Preset Behavior

Controls what Import Preview proposes when a generated preset filename already exists.

Always review Import Preview before overwriting or updating an existing preset.

### Visible Inventory Columns

Choose which optional columns appear in the inventory table. At least one column must remain visible.

### Tab Visibility

Controls whether the SpoolMan Web UI and SpoolMan Importer tabs are registered with OrcaSlicer. Tab changes may require a full OrcaSlicer restart.

## Inventory Selection Behavior

When a selected spool becomes hidden by search, filtering, or **Hide Imported**, the plugin removes that spool from the Import Queue.

Clearing the filter does not restore the previous selection. This prevents hidden spools from being imported accidentally.

Sorting does not remove selections because sorting does not hide rows.

## Naming Templates

Naming templates control generated preset names. Available variables are shown in Settings.

The `{{acquired_date}}` value resolves in this order:

1. `spool.extra.date_acquired`
2. The built-in spool registration timestamp
3. Blank when neither value is valid

`date_acquired` is a user-created spool custom field and is not a default SpoolMan field.

## G-Code Templates

Start and end G-code templates can use supported template variables. Review generated G-code in Import Preview before writing the preset.

## Field Mappings

Field mappings determine where supported Orca values come from. See [FIELD_MAPPINGS.md](FIELD_MAPPINGS.md).

## Temporary Bulk-Update Selections

The checkboxes under **Bulk Update Existing Presets** apply only to the current operation.

They are:

- Not global plugin settings.
- Not saved by **Save Settings**.
- Not used for new imports from the main Importer table.
- Used only by the bulk-update operation.

A selected field is written only when the existing preset value is missing or differs from the SpoolMan-derived value.

## Update Notifications

### Stable

Ignores GitHub prereleases and reports only eligible non-prerelease versions.

### Development

Includes eligible GitHub prereleases.

### Disabled

Performs no update checks.

Update checks are informational. The plugin does not automatically download, replace, or install plugin files.

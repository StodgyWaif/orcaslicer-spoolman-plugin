# Screenshot Guide

Use **OrcaSlicer 2.5.0-dev** and plugin **v1.0.72** so the screenshots match the documented testing environment.

## General rules

- Use the **Orca Dark** theme for the main screenshot set.
- Capture at approximately 1600 × 900 or larger when possible.
- Capture the OrcaSlicer window or relevant plugin panel only.
- Remove or obscure private server names, IP addresses, usernames, local paths, pricing, comments, and private spool data.
- Never show credentials, tokens, or unreviewed diagnostic logs.
- Save PNG files with the exact filenames below.
- Avoid arrows and annotations in the primary screenshots.

## Required screenshots

### `importer-inventory.png`

Capture the main Importer with:

- Inventory status cards
- Search and filters
- Refresh, Select All, Select None, and Hide Imported
- Several inventory rows
- At least two different profile statuses, if available
- Import Queue on the right

### `settings-common-preferences.png`

Capture Settings with:

- Common Preferences
- Plugin Theme
- Low Filament Threshold
- Existing Preset Behavior
- Visible Inventory Columns
- Tab visibility

### `field-mappings.png`

Capture the Field Mappings section with:

- Several mapping rows
- Acquired date mapped to `spool.extra.date_acquired`
- **Show All SpoolMan Fields**
- Both Built-in and Custom rows in the field table
- The `date_acquired` custom-field row visible

### `managed-orca-profiles.png`

Capture **Advanced: Managed Orca Profiles** with:

- Step 1: Check profile status
- Step 2: Bulk Update Existing Presets
- Step 3: Review Linked Presets by Spool
- Summary cards
- One selected spool with linked presets, if available

### `import-preview.png`

Open Import Preview for one safe spool and capture:

- Planned action
- Generated preset name
- Target summary
- Existing-versus-proposed values
- Cancel and Execute Import controls

Obscure identifying local paths if shown.

### `backup-maintenance.png`

Capture **Advanced: Index and Folder Maintenance** with:

- Detection and diagnostics
- Preset backups
- Import-index backups
- Full backup and transfer
- Diagnostic export

Do not display unreviewed diagnostic content.

## Add screenshots to GitHub

1. Create a repository folder named `screenshots`.
2. Upload all six PNG files using the exact names above.
3. Commit with:

```text
Add v1.0.72 plugin screenshots
```

4. Open `README.md` on GitHub.
5. Confirm all images render.
6. If a screenshot is too large, resize the PNG and keep the same filename.

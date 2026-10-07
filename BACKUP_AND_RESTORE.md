# Backup and Restore

Use the plugin's backup tools before large imports, synchronization, cleanup, upgrades, restoration, or computer migration.

The v1.0.72 backup and restore workflow was tested on **OrcaSlicer 2.5.0-dev**.

## Backup Types

### Preset Backup

Created before an existing managed Orca preset is changed. Use this to restore an individual preset JSON file.

### Import-Index Backup

Preserves the plugin's record of which SpoolMan spools are linked to which Orca preset files.

Restoring the index does not automatically restore a missing preset file.

### Full Backup

Packages plugin settings, import-index data, and applicable managed preset data into a ZIP archive for recovery or computer transfer.

### Pre-Restore Safety Backup

Created before a restore operation so the pre-restore state can be recovered if necessary.

### Diagnostic Export

Intended for troubleshooting. A diagnostic package is not a replacement for a full backup.

## Before a Full Backup

1. Confirm the active OrcaSlicer profile.
2. Confirm the active filament-preset folder.
3. Refresh inventory and profile status.
4. Resolve unexpected missing or moved files when practical.
5. Create the full backup.
6. Validate the generated archive.
7. Copy the ZIP to storage outside the OrcaSlicer configuration directory.

## Restore Checklist

> [!WARNING]
> Always verify the active OrcaSlicer profile and destination filament folder before restoring preset files. Paths restored from another computer may not be valid on the destination computer.

1. Preserve the destination computer's current plugin settings and presets.
2. Validate the backup archive.
3. Review the destination OrcaSlicer profile and filament folder.
4. Restore the backup.
5. Recheck machine-specific paths before any write operation.
6. Refresh inventory.
7. Refresh profile status.
8. Run Preview SpoolMan Changes.

## Computer Transfer

When transferring to another computer:

- Do not assume source-computer paths are valid on the destination.
- Select the destination OrcaSlicer profile explicitly.
- Select and validate the destination filament folder explicitly.
- Review field mappings after SpoolMan connection is restored.
- Preview synchronization before applying updates.

## Restore Limitations

A restored import index can reference preset files that are not present on the destination computer. Use Managed Orca Profiles to relink moved files or remove confirmed-missing index entries.

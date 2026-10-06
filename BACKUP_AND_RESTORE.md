# Backup and Restore

## Before bulk operations

Use the plugin's backup tools before large imports, synchronization, cleanup, upgrades, or computer migration.

## Preset backups

A changed managed preset is backed up before a synchronization write. Preset backups support focused rollback of an individual preset.

## Full backup

A full backup can include plugin settings, the import index, and applicable managed data. Store the ZIP outside the OrcaSlicer configuration directory.

## Restore checklist

1. Preserve the destination computer's current settings and presets.
2. Validate the backup archive.
3. Review the destination OrcaSlicer profile and filament folder.
4. Restore the backup.
5. Recheck machine-specific paths before any write operation.
6. Refresh inventory and preview synchronization.

## Important

A restored path from another computer must not be assumed valid. Select and validate the destination folder explicitly.

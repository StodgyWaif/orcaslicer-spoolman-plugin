# Troubleshooting

## Plugin does not load

- Confirm the file is named `spoolman_plugin.py`.
- Fully restart OrcaSlicer.
- Open the plugin Diagnostics tab and review the load error.
- Reinstall the last confirmed build if necessary.

## SpoolMan connection fails

- Confirm the base URL opens from the same computer.
- Check protocol, host, port, reverse proxy, and firewall rules.
- Do not append `/api/v1/spool` to the configured base URL.

## Inventory is empty or stale

- Use Refresh Inventory.
- Review the status cards and recovery message.
- Confirm SpoolMan returns non-archived spools.

## Preset cannot be updated

- Run Refresh Profile Status.
- Preview SpoolMan Changes.
- Relink moved or renamed files.
- Remove only confirmed-missing index entries.
- Validate the OrcaSlicer filament folder.

## Field value is not written

- Discover SpoolMan fields.
- Confirm the source path, type, and populated count.
- Check that the value is non-empty and valid for the target.
- Remember that blank mappings leave targets unmanaged.

## Diagnostic bundle

Create a diagnostic bundle from Settings. Inspect the archive before attaching it to a public issue. Remove any information that should not be shared.

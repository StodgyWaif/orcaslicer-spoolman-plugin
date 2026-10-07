# Troubleshooting

## Compatibility Note

The current development build was tested on **OrcaSlicer 2.5.0-dev**. When reporting a problem from another OrcaSlicer build, include the complete OrcaSlicer version and whether the plugin was installed locally or through Plugin Hub.

## Plugin Does Not Load

- Confirm the file is named `spoolman_plugin.py`.
- Fully restart OrcaSlicer.
- Review the plugin Diagnostics tab.
- Reinstall the last confirmed release asset.
- Preserve the failing file and diagnostic details for a bug report.

## Importer Page Is Blank

- Fully restart OrcaSlicer.
- Confirm the installed plugin version.
- Review the plugin Diagnostics tab.
- Reinstall the last confirmed release asset.
- Report any generated-page or JavaScript error shown by OrcaSlicer.

## SpoolMan Connection Test Fails

- Confirm the configured value is the SpoolMan base URL.
- Check protocol, hostname, port, reverse proxy, and firewall rules.
- Do not append `/api/v1/spool`.
- Confirm the URL opens from the same computer.

## SpoolMan Tab Shows an Error

- Confirm the SpoolMan base URL is correct.
- Open the same URL in an external browser.
- Check reverse-proxy behavior and base-path configuration.
- Remember that spool-record links intentionally open in the external system browser.

## Inventory Returns No Spools

- Confirm SpoolMan contains active, non-archived spools.
- Review the inventory refresh status cards.
- Retry **Refresh Inventory**.
- Verify that filters are not hiding all rows.

## Imported Preset Does Not Appear

- Fully restart OrcaSlicer if instructed.
- Confirm the active user filament folder.
- Confirm the generated JSON file exists.
- Review Last Import and the diagnostic log.

## Orca Filament Folder Cannot Be Validated

- Confirm the selected folder belongs to the active OrcaSlicer user profile.
- Confirm the folder exists and is writable.
- Avoid selecting a system preset folder.
- Re-run folder detection and diagnostics.

## Preset Is Missing or Moved

- Open **Managed Orca Profiles**.
- Select **Refresh Profile Status**.
- Relink moved or renamed presets.
- Remove an index entry only when the missing file is confirmed.

## Custom Field Does Not Appear

- Run **Show All SpoolMan Fields**.
- Confirm the field's entity scope: spool, filament, or vendor.
- Confirm at least one current record has a populated value.
- Verify the custom-field key rather than only its display name.

## Mapped Value Is Skipped

- Confirm the source path exists.
- Confirm the field contains a value for that spool.
- Confirm the source type is compatible with the target.
- Confirm the value is within the target validation range.
- Remember that unavailable values are intentionally omitted rather than used to erase existing Orca values.

## Update Check Fails

- Confirm internet access to GitHub.
- Verify the selected Stable or Development channel.
- Confirm the repository has a published eligible release.
- Confirm the release is not a draft.
- An update-check failure does not affect SpoolMan inventory access.

## Full Backup Fails Validation

- Confirm the destination is writable.
- Confirm there is sufficient free disk space.
- Retry after closing software that may be locking files.
- Review plugin diagnostics.
- Do not rely on an archive that the plugin reports as invalid.

## Diagnostic Bundle

Inspect every diagnostic archive before attaching it to a public issue. Remove information that should not be shared, including credentials, private server URLs, private paths, and personal data.

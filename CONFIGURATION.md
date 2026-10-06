# Configuration

## SpoolMan connection

Enter the base URL used to reach SpoolMan. Do not append an individual API endpoint. Test the connection before continuing.

## OrcaSlicer filament folder

Select the active user filament-preset folder for the OrcaSlicer profile in use. Validate the detected path before allowing writes.

## Import behavior

Review duplicate handling, naming templates, inventory columns, low-filament threshold, theme, and tab visibility. Import Preview should be used before every unfamiliar bulk import.

## Naming dates

`{{acquired_date}}` resolves in this order:

1. `spool.extra.date_acquired`
2. SpoolMan's built-in spool registration timestamp
3. Blank when neither value is valid

`date_acquired` is a user-created spool custom field, not a default SpoolMan field.

## Updates

- **Stable:** ignores prereleases.
- **Development:** includes eligible prereleases.
- **Disabled:** performs no update checks.

Update checks are informational only and never replace the plugin file automatically.

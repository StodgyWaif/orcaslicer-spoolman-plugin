# Configuration

> The v1.0.72 configuration workflow documented here was tested on **OrcaSlicer 2.5.0-dev**. Menu names or plugin-management behavior may differ in other builds.

## SpoolMan connection

Enter the base URL used to reach SpoolMan. Do not append an individual API endpoint. Test the connection before continuing.

## OrcaSlicer filament folder

Select the active user filament-preset folder for the OrcaSlicer profile in use. Validate the detected path before allowing writes.

## Naming dates

`{{acquired_date}}` resolves from the user-created spool custom field `spool.extra.date_acquired`, then falls back to the spool registration timestamp when needed. `date_acquired` is not a default SpoolMan field.

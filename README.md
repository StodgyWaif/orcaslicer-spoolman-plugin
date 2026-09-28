````markdown
# SpoolMan Importer for OrcaSlicer

This project is a starter plugin for OrcaSlicer that imports filament inventory from a SpoolMan server and creates a simple preset export structure.

This is intended as a learning scaffold and starting point for a real OrcaSlicer plugin integration.

## Features

- SpoolMan URL + auth settings
- Configurable naming template
- Configurable g-code template
- Preset directory configuration
- Fetch inventory from SpoolMan
- Import selected records into a generated preset output

## Project structure

- `manifest.json` — plugin manifest
- `settings_manager.py` — user settings persistence
- `spoolman_api.py` — SpoolMan API client
- `preset_importer.py` — preset creation logic
- `spoolman_plugin.py` — UI page and main plugin logic

## Typical workflow

1. Edit settings in the plugin page
2. Set SpoolMan host URL
3. Save settings
4. Fetch filament inventory
5. Review the list
6. Select which items to import
7. Export or create preset files

## Important note

This plugin is intentionally simplified. For a real OrcaSlicer build, you will likely need to adapt:
- the page registration format
- the page class names
- how preset files are written
- how the plugin is discovered by the active OrcaSlicer version

## License

MIT

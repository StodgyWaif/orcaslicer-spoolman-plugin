# Contributing

Thank you for helping improve the OrcaSlicer SpoolMan Importer.

## Reporting Issues

Use the GitHub issue templates and include:

- Plugin version
- OrcaSlicer version
- SpoolMan version
- Operating system
- Installation type
- Reproduction steps
- Expected behavior
- Actual behavior

Inspect every diagnostic bundle before uploading it publicly.

## Proposed Code Changes

- Base changes on the current development branch.
- Preserve preview-first behavior.
- Do not simulate missing SpoolMan data.
- Do not erase Orca values when mapped source values are unavailable.
- Preserve preset-backup behavior before managed writes.
- Keep destructive operations explicit and user-initiated.
- Maintain compatibility with existing settings and index data when practical.

## Validation Requirements

Before submitting a code change, test:

- Strict Python compilation
- Full plugin module import
- Generated Importer HTML rendering
- Embedded JavaScript syntax
- Plugin loading in OrcaSlicer
- Inventory refresh
- Import Preview
- Synchronization Preview
- Backup creation
- Light and dark themes
- Fresh installation
- Upgrade from an earlier settings format

## Documentation Changes

Update applicable documentation and screenshots when changing:

- User-visible labels
- Settings organization
- Installation steps
- Field mappings
- Backup behavior
- Release behavior

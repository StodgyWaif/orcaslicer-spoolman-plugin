# Field Mappings

Field mappings connect a SpoolMan source path to a supported OrcaSlicer preset target.

## Source path examples

```text
spool.location
spool.extra.date_acquired
filament.density
filament.settings_extruder_temp
filament.extra.flow_ratio
vendor.name
```

## Recommended process

1. Open **Settings > SpoolMan Field Mappings**.
2. Select **Show All SpoolMan Fields**.
3. Review entity, source path, type, unit, populated count, and sample.
4. Enter or select sources for the desired targets.
5. Save field mappings.
6. Run Import Preview or Preview SpoolMan Changes.

## Safety behavior

- A blank mapping leaves the target unmanaged.
- Missing or empty source values are omitted.
- Invalid numeric values are omitted.
- Unavailable sources do not erase existing Orca values.
- Explicit mappings take precedence over legacy aliases.

## Plate temperatures

Regular and initial-layer values can be mapped independently for textured, cool, engineering, and smooth/high-temperature plates. The general SpoolMan bed temperature may be used as a fallback when desired.

# Field Mappings

Field mappings connect a SpoolMan source path to a supported OrcaSlicer preset target.

## Discovering Fields

1. Open **Settings > SpoolMan Field Mappings**.
2. Select **Show All SpoolMan Fields**.
3. Review the entity, source path, kind, type, unit, populated count, sample value, and mapping status.
4. Enter or select sources for the desired targets.
5. Save field mappings.
6. Run Import Preview or Preview SpoolMan Changes.

## Source Scopes

### Spool Fields

Values associated with one physical spool.

Examples:

```text
spool.location
spool.registered
spool.remaining_weight
spool.extra.date_acquired
```

### Filament Fields

Values shared by spools using the same SpoolMan filament record.

Examples:

```text
filament.density
filament.diameter
filament.settings_extruder_temp
filament.settings_bed_temp
filament.extra.flow_ratio
```

### Vendor Fields

Values associated with the filament manufacturer.

Examples:

```text
vendor.name
vendor.empty_spool_weight
vendor.extra.example_key
```

## Built-In and Custom Paths

Built-in values use paths such as:

```text
filament.density
spool.location
vendor.name
```

Custom fields use `extra` paths such as:

```text
spool.extra.date_acquired
filament.extra.max_volumetric_speed
vendor.extra.example_key
```

Custom-field values are decoded according to the discovered field definitions when available.

## Recommended Default Mappings

```text
Acquired date                  spool.extra.date_acquired
Density                        filament.density
Diameter                       filament.diameter
Flow ratio                     filament.extra.flow_ratio
Maximum volumetric speed       filament.extra.max_volumetric_speed
Nozzle temperature             filament.settings_extruder_temp
Initial nozzle temperature     filament.settings_extruder_temp
Plate temperatures             filament.settings_bed_temp
```

The plate-temperature mappings can be replaced with separate custom fields when different temperatures are stored for each plate type.

## Plate Temperatures

Regular and initial-layer values can be mapped independently for:

- Textured plate
- Cool plate
- Engineering plate
- Smooth or high-temperature plate

The general SpoolMan bed temperature may be retained as a fallback when desired.

## Missing and Invalid Values

- A blank mapping leaves the Orca target unmanaged.
- A missing source value is omitted.
- An empty custom-field value is omitted.
- Invalid numeric values are omitted.
- Values outside the supported target range are omitted.
- An unavailable value does not erase an existing Orca preset value.
- Explicit mappings take precedence over legacy source aliases.

## `date_acquired`

`date_acquired` is an optional user-created spool custom field. It is not included by default in SpoolMan.

Recommended configuration:

```text
Entity: spool
Key: date_acquired
Suggested type: datetime
Mapping path: spool.extra.date_acquired
```

When unavailable, the acquired-date template value may fall back to the built-in spool registration timestamp.

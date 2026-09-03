# Prototype data dictionary

The committed workbooks are empty schema examples. No operational dataset is included or authorized. Missing observations remain missing and must never be converted to neutral, healthy, or zero status.

| Schema | Example fields | Validation and sensitivity |
|---|---|---|
| Pasture conditions | `pasture_id`, `date`, `condition_score`, `notes` | Example score range 1–5; identifiers and notes may be sensitive |
| Grazing log | `pasture_id`, `date`, `animal_count`, `days_grazed`, `pasture_area_acres` | Numeric values non-negative; operationally sensitive |
| Groundwater | `well_id`, `date`, `water_level_ft`, `lat`, `lon` | Coordinates valid WGS84; locations highly sensitive; local vertical datum required |
| Animal condition | `herd_id`, `date`, `condition_score`, `notes` | Example score range 1–9; operationally sensitive |
| Pasture-water link | `pasture_id`, `well_id` | Sensitive infrastructure relationship |

Names, fields, ranges, units, and required status must be reviewed and approved before operational use.

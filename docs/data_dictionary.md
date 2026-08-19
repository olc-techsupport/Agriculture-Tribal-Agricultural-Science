# Data dictionary
# Data dictionary

Operational files are local, governed data and never committed. Dates use ISO `YYYY-MM-DD`.

| Dataset | Required fields | Validation and sensitivity |
|---|---|---|
| Pasture conditions | `pasture_id`, `date`, `condition_score`, `notes` | Score 1–5; identifiers/notes may be sensitive |
| Grazing log | `pasture_id`, `date`, `animal_count`, `days_grazed`, `pasture_area_acres` | Values non-negative; operationally sensitive |
| Groundwater | `well_id`, `date`, `water_level_ft`, `lat`, `lon` | Coordinates valid WGS84 and highly sensitive; record local vertical datum |
| Animal condition | `herd_id`, `date`, `condition_score`, `notes` | Score 1–9; operationally sensitive |
| Pasture-water link | `pasture_id`, `well_id` | Sensitive infrastructure relationship |

Missing observations remain missing; they are never converted to neutral or healthy status.
Operational files are local, governed data and are never committed. Dates use ISO `YYYY-MM-DD` format.

| Dataset | Required fields | Validation and sensitivity |
|---|---|---|
| Pasture conditions | `pasture_id`, `date`, `condition_score`, `notes` | Score 1–5; identifiers and notes may be sensitive |
| Grazing log | `pasture_id`, `date`, `animal_count`, `days_grazed`, `pasture_area_acres` | Numeric values non-negative; operationally sensitive |
| Groundwater | `well_id`, `date`, `water_level_ft`, `lat`, `lon` | Coordinates valid WGS84 and highly sensitive; document local vertical datum |
| Animal condition | `herd_id`, `date`, `condition_score`, `notes` | Score 1–9; operationally sensitive |
| Pasture-water link | `pasture_id`, `well_id` | Sensitive infrastructure relationship |

Missing observations remain missing. They must not be converted to neutral or healthy status.

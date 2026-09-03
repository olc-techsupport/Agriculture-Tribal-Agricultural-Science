# Tribal Agriculture and Land Health in South Dakota
**Authors:** Lilly Jones, PhD (Daear Consulting, LLC)  
**Developed for:** Oglala Lakota College  
**Funding:** Developed as part of a project funded by USDA NIFA  
**Project role:** Daear Consulting LLC developed the geospatial code, workflows, and documentation under contract to Oglala Lakota College.  
**Primary instructional focus:** Pine Ridge and Oglala Lakota; other geographies are regional context only  
**Status:** Public-data educational analysis; operational prototype inactive pending locally authorized governance   
**License:** Apache License 2.0 (code; review of other materials is pending)

## Data Sovereignty and Governance (draft under review)
This repository contains workflows developed for use in support of Oglala Lakota College and Oglala Sioux Tribe–related research, education, and data activities. Public availability of code or documentation does not imply that Tribal data, knowledge, or derived information are open or unrestricted. Use of Tribal data and knowledge remains subject to applicable Tribal governance, permissions, protocols, and data sovereignty requirements.


## Overview
This repository provides reproducible public-data analyses and learning-design
stubs for OLC. It does not represent or operate on behalf of South Dakota Tribal
Nations, and it does not establish approved agricultural or land-management decisions.

It operates on two parallel tracks:

### Track 1: Analysis Notebooks (Public Data)
Jupyter notebooks using publicly available data to establish regional context:
satellite vegetation condition (NDVI), drought indices, federal agricultural
statistics, weather, and groundwater. These notebooks show what satellite and
federal data can and cannot see about Tribal agricultural lands and motivate
the case for Tribal-led data collection.

### Track 2: Inactive Schema Prototype
A schema-validation and local-dashboard prototype illustrating possible fields for observational data:
pasture condition scores, grazing logs, animal condition scores, and well levels.
**No Tribal observational data is included or authorized for use.** The committed spreadsheets are empty schema examples. The prototype does not grant authority to collect or process data and is not a deployment. A governing Nation must approve purposes, stewardship, infrastructure, users, retention, location handling, analysis, and release rules before use.

## Data Sovereignty
Potential reference frameworks remain under local review:
| Framework | What it governs |
|---|---|
| **OCAP®** | Canadian First Nations framework; local applicability must not be assumed |
| **CARE** | Collective Benefit, Authority to Control, Responsibility, Ethics |
| **FAIR** | Technical standards: Findable, Accessible, Interoperable, Reusable |

Naming a framework does not imply that OLC, OST, or another Nation has adopted it. See `docs/data_governance.md`.

**Critical distinction in this repo:**
- `data/raw/`, `data/processed/` gitignored. Tribal data stays on Tribal infrastructure.
- `data/templates/` committed. Entry templates for field staff.
- `data/cache/` gitignored. Public data cache.

## Repository Structure
```
tribal_ag_sd/
├── notebooks/              # Analysis notebooks (public data)
├── scripts/                # Notebook runner, validation, templates, local pipeline
├── app/                    # Streamlit dashboard
│   └── components/
├── src/                    # Shared Python modules
│   ├── data/               # Constants, loaders, validators
│   ├── viz/                # Styles, charts, maps
│   └── indigenous/         # Data sovereignty framework
├── data/
│   ├── templates/          # COMMITTED: Excel entry templates for field staff
│   ├── raw/                # GITIGNORED: Tribal observational data
│   ├── processed/          # GITIGNORED: Pipeline outputs
│   └── cache/              # GITIGNORED: Public data cache
├── config/
│   └── config.yaml         # All thresholds: adjust here, not in code
├── scripts/
│   └── run_pipeline.py     # Single-command pipeline runner
├── docs/
│   ├── field_guide.md      # How to collect data; what scores mean
│   ├── data_dictionary.md  # Every column defined
│   └── methodology.md      # Decision rules explained for transparency
└── environment.yml
```

## Analysis Notebooks
| Notebook | Focus | Data Source | Tribes |
|---|---|---|---|
| 01_land_base_context | Land area, trust land, jurisdiction | Census TIGER | All SD |
| 02_drought_climate_context | Historical drought frequency and severity | NOAA PDSI | All SD |
| 03_vegetation_condition_ndvi | Satellite vegetation proxy for pasture condition | MODIS MOD13Q1 | Pine Ridge, Rosebud |
| 04_usda_nass_agricultural_context | County-level livestock and agricultural statistics | USDA NASS | All SD |
| 05_water_availability | USGS groundwater monitoring coverage and gaps | USGS NWIS | Pine Ridge, Rosebud |
| 06_system_stress_index | Combined drought and vegetation stress indicator | PDSI/NDVI | All SD |
| 07_climate_projections_agriculture | Projected temperature and precip change | MACAv2 | Pine Ridge, Rosebud |

## Quick Start

### Analysis notebooks
```bash
conda env create -f environment.yml
conda activate tribal-ag-sd
python scripts/run_notebooks.py
python scripts/validate_project.py
```
The notebooks run in numeric dependency order. Executed copies are written to `outputs/executed_notebooks/`; source notebooks are not overwritten.

Notebook 03 uses the ORNL MODIS service, which limits each request to ten composite tiles; downloads are chunked and cached and can take substantial time on the first run. Notebook 04 requires `NASS_API_KEY`. A run stops on missing credentials or upstream failure rather than substituting synthetic or neutral data.
### Inactive schema prototype
```bash
# Do not add operational data without an approved governance process.
# The following validates empty/example schemas during development only.
python scripts/create_templates.py
python scripts/run_pipeline.py
```
### Dashboard
```bash
streamlit run app/app.py
```
The dashboard is local-only evaluation software. Do not load operational data or deploy it until the governing Nation approves the complete governance gate.

### Tests and environment lock

```bash
pytest -q
conda-lock -f environment.yaml -p win-64 -p linux-64
```

Commit the generated lock file when dependency resolution is intentionally refreshed.

After producing or importing public artifacts, run `python scripts/write_provenance.py` to record checksums and the Git revision. Presence in `outputs/` does not itself mean an artifact has passed scientific or Tribal release review.

## Environment Variables
Create a `.env` file in the repo root (never committed):
```
# USDA NASS API key (free: https://quickstats.nass.usda.gov/api)
NASS_API_KEY=your_key

# Census API key (free: https://api.census.gov/data/key_signup.html)
CENSUS_API_KEY=your_key

# SynopticData token for RAWS weather stations (free: https://synopticdata.com)
SYNOPTIC_TOKEN=your_token
```

## Data Templates
Field data entry templates are in `data/templates/`:

| Template | Contents |
|---|---|
| `pasture_conditions_template.xlsx` | pasture_id, date, condition_score (1–5), notes |
| `grazing_log_template.xlsx` | pasture_id, date, animal_count, days_grazed, pasture_area_acres |
| `groundwater_template.xlsx` | well_id, date, water_level_ft, lat, lon |
| `animal_condition_template.xlsx` | herd_id, date, condition_score (1–9 BCS), notes |
| `pasture_water_link_template.xlsx` | pasture_id, well_id |

## Example Condition-Score Configuration

These are unapproved software examples, not OLC/OST or NRCS-endorsed action rules.

| Score | Meaning | Dashboard Color | Action |
|---|---|---|---|
| 5 | Excellent | 🟢 Green | Graze OK |
| 4 | Good | 🟢 Green | Graze OK |
| 3 | Fair | 🟡 Yellow | Monitor |
| 2 | Poor | 🟠 Orange | Reduce grazing |
| 1 | Critical | 🔴 Red | REST |

## Learning and review materials

The notebook learning sections are stubs. OLC will develop the full instructional materials, facilitation choices, and curriculum. See `docs/learning_design.md`, `docs/facilitator_guide.md`, `docs/assumptions_register.md`, and `docs/review_checklist.md`.

## Citation

Citation metadata, author order, OLC attribution, copyright ownership, and complete NIFA award details remain pending review.

## Data Governance Contact

The appropriate OLC/OST governance contact and release authority remain to be confirmed. Daear Consulting LLC is the development contractor and should not be represented as Tribal data-governance authority.

# Tribal Agriculture and Land Health in South Dakota

**Authors:** Lilly Jones, PhD (Daear Consulting, LLC)  
**Primary Focus:** Oglala Lakota (Pine Ridge), Sicangu Lakota (Rosebud)  
**In Scope:** All South Dakota Tribal Nations  
**Status:** Active development

## Overview
This repository supports Tribal land managers, agricultural programs, and decision
makers working on agriculture, rangeland health, and food sovereignty across South
Dakota Tribal Nations.

It operates on two parallel tracks:

### Track 1: Analysis Notebooks (Public Data)
Jupyter notebooks using publicly available data to establish regional context:
satellite vegetation condition (NDVI), drought indices, federal agricultural
statistics, weather, and groundwater. These notebooks show what satellite and
federal data can and cannot see about Tribal agricultural lands and motivate
the case for Tribal-led data collection.

### Track 2: Operational Pipeline and Dashboard (Tribal Data)

A processing pipeline and Streamlit dashboard for Tribal observational data:
pasture condition scores, grazing logs, animal condition scores, and well levels.
**Tribal observational data is never committed to this repository.** It lives on
Tribal infrastructure and is governed by the Tribal Nation that collected it.

## Data Sovereignty
This project is guided by three complementary frameworks:
| Framework | What it governs |
|---|---|
| **OCAP®** | Tribal Nations own, control, access, and possess their data |
| **CARE** | Collective Benefit, Authority to Control, Responsibility, Ethics |
| **FAIR** | Technical standards: Findable, Accessible, Interoperable, Reusable |

FAIR is the technical floor. CARE and OCAP® are the ethical layer that FAIR alone
does not address.

**Critical distinction in this repo:**
- `data/raw/`, `data/processed/` gitignored. Tribal data stays on Tribal infrastructure.
- `data/templates/` committed. Entry templates for field staff.
- `data/cache/` gitignored. Public data cache.

## Repository Structure
```
tribal_ag_sd/
├── notebooks/              # Analysis notebooks (public data)
├── pipeline/               # Data processing scripts (Tribal data)
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
jupyter lab notebooks/
```
### Operational pipeline (requires Tribal data in data/raw/)
```bash
# Add data files to data/raw/ using templates from data/templates/
python scripts/run_pipeline.py
```
### Dashboard
```bash
streamlit run app/app.py
```

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

## Condition Score Reference (NRCS 5-Point Scale)

| Score | Meaning | Dashboard Color | Action |
|---|---|---|---|
| 5 | Excellent | 🟢 Green | Graze OK |
| 4 | Good | 🟢 Green | Graze OK |
| 3 | Fair | 🟡 Yellow | Monitor |
| 2 | Poor | 🟠 Orange | Reduce grazing |
| 1 | Critical | 🔴 Red | REST |

## Citation
Jones, L. and Sanovia, J., (2025). Tribal Agriculture and Land Health in South Dakota. Daear Consulting, LLC.

## Data Governance Contact

For questions about data use, Tribal data governance, or collaboration:  
**James Sanovia, MS**  
Daear Consulting, LLC  
[daearconsulting@gmail.com](mailto:daearconsulting@gmail.com)

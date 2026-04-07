"""
constants.py: Shared constants for Tribal Agriculture & Land Health series.

Scope: South Dakota Tribal Nations, with primary focus on Oglala Lakota
(Pine Ridge) and secondary focus on Rosebud Sioux.

Design principles
- SD_TRIBES_PRIMARY : Pine Ridge and Rosebud: real or near-real data expected
- SD_TRIBES_ALL     : All South Dakota Tribal Nations in scope
- Relative paths throughout (public repo)
- Real data only in analysis notebooks: no synthetic data
- Tribal observational data (pasture, grazing, wells) is NEVER committed
"""

from pathlib import Path

# Repo root 
REPO_ROOT  = Path(__file__).resolve().parents[3]

# Data directories 
DATA_DIR       = REPO_ROOT / "data"
RAW_DIR        = DATA_DIR / "raw"
PROCESSED_DIR  = DATA_DIR / "processed"
CACHE_DIR      = DATA_DIR / "cache"
TEMPLATES_DIR  = DATA_DIR / "templates"
OUTPUTS_DIR    = REPO_ROOT / "outputs"

# Coordinate reference systems 
CRS_GEOGRAPHIC = "EPSG:4326"    # WGS84 geographic
CRS_PROJECTED  = "EPSG:5070"    # Albers Equal Area CONUS (for area/distance)

# South Dakota Tribal Nations 
# Primary focus: analysis notebooks use real or near-real data
SD_TRIBES_PRIMARY = [
    "Oglala Lakota",       # Pine Ridge: largest reservation in SD by land area
    "Rosebud Sioux",       # Rosebud: adjacent to Pine Ridge, similar ecology and geology
]

# Secondary focus: notebooks extended where public data supports it
SD_TRIBES_SECONDARY = [
    "Standing Rock Sioux",
    "Cheyenne River Sioux",
    "Lower Brule Sioux",
    "Crow Creek Sioux",
    "Sisseton Wahpeton Oyate",
    "Flandreau Santee Sioux",
]

# All SD Tribes in scope
SD_TRIBES_ALL = SD_TRIBES_PRIMARY + SD_TRIBES_SECONDARY

# Census TIGER AIANNH name matching: exact strings as they appear in Census data
# These may differ slightly from common-use names above
CENSUS_NAME_MAP = {
    "Oglala Lakota":           "Pine Ridge",
    "Rosebud Sioux":           "Rosebud",
    "Standing Rock Sioux":     "Standing Rock",
    "Cheyenne River Sioux":    "Cheyenne River",
    "Lower Brule Sioux":       "Lower Brule",
    "Crow Creek Sioux":        "Crow Creek",
    "Sisseton Wahpeton Oyate": "Lake Traverse",
    "Flandreau Santee Sioux":  "Flandreau",
}

# Reverse map for convenience
CENSUS_TO_COMMON = {v: k for k, v in CENSUS_NAME_MAP.items()}

# South Dakota bounding box 
SD_BBOX = (-104.06, 42.48, -96.44, 45.95)   # (min_lon, min_lat, max_lon, max_lat)

# Pine Ridge/southern SD focus bbox (covers Pine Ridge + Rosebud + adjacent)
PINE_RIDGE_BBOX = (-103.5, 42.5, -100.0, 44.0)

# Pasture condition score definitions
# USDA NRCS 5-point condition scale
PASTURE_CONDITION_LABELS = {
    5: "Excellent",
    4: "Good",
    3: "Fair",
    2: "Poor",
    1: "Critical",
}

PASTURE_STATUS_THRESHOLDS = {
    "critical":  2,   # condition_score <= 2
    "watch":     3,   # condition_score == 3
    "healthy":   4,   # condition_score >= 4
}

# Drought index thresholds (PDSI) 
# Palmer Drought Severity Index
PDSI_THRESHOLDS = {
    "extreme_drought":  -4.0,
    "severe_drought":   -3.0,
    "moderate_drought": -2.0,
    "mild_drought":     -1.0,
    "normal":            0.0,
    "mild_wet":          1.0,
    "moderate_wet":      2.0,
}

# NDVI thresholds (vegetation condition proxy)
# Moderate Resolution Imaging Spectroradiometer (MODIS)
# Growing season NDVI (May–September) for mixed-grass prairie
NDVI_THRESHOLDS = {
    "poor":     0.25,   # Below this = poor vegetation condition
    "fair":     0.35,
    "good":     0.45,
    "excellent": 0.55,
}

# Grazing pressure thresholds 
# Animals × days/pasture acres (Animal Unit Days/acre)
GRAZING_PRESSURE_THRESHOLDS = {
    "low":      3.0,
    "moderate": 5.0,
    "high":     7.0,
    "critical": 10.0,
}

# Public data URLs
CENSUS_TIGER_BASE       = "https://www2.census.gov/geo/tiger"
CENSUS_AIAN_URL         = (
    f"{CENSUS_TIGER_BASE}/TIGER2023/AIANNH/tl_2023_us_aiannh.zip"
)

# USDA NASS QuickStats API base
USDA_NASS_API_BASE      = "https://quickstats.nass.usda.gov/api"

# NOAA PDSI/drought data
NOAA_DROUGHT_BASE       = "https://www.ncei.noaa.gov/pub/data/cirs/climdiv"

# USGS groundwater (NWIS)
USGS_NWIS_BASE          = "https://waterservices.usgs.gov/nwis"

# gridMET (weather)
GRIDMET_BASE            = "https://thredds.northwestknowledge.net/thredds/dodsC/MET"

# MACAv2 climate projections
MACA_THREDDS_BASE       = "http://thredds.northwestknowledge.net:8080/thredds/dodsC/"

# Operational data paths (gitignored: Tribal observational data)
# These paths are used by the pipeline only. Files at these paths are never
# committed to version control. See data/templates/ for entry templates.
PASTURE_CONDITIONS_RAW  = RAW_DIR / "pasture_conditions.csv"
GRAZING_LOG_RAW         = RAW_DIR / "grazing_log.csv"
GROUNDWATER_RAW         = RAW_DIR / "groundwater.csv"
ANIMAL_CONDITION_RAW    = RAW_DIR / "animal_condition.csv"
PASTURE_WATER_LINK_RAW  = RAW_DIR / "pasture_water_link.csv"

PASTURE_PROCESSED       = PROCESSED_DIR / "agriculture.parquet"
GRAZING_PROCESSED       = PROCESSED_DIR / "grazing.parquet"
GROUNDWATER_PROCESSED   = PROCESSED_DIR / "groundwater.parquet"
RECOVERY_PROCESSED      = PROCESSED_DIR / "recovery.parquet"
WATER_LINK_PROCESSED    = PROCESSED_DIR / "water_pasture_link.parquet"

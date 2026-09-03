from __future__ import annotations

"""
sovereignty.py Data governance framework for Tribal Agriculture series.

This module records draft governance notes and data-source distinctions.
It does not implement governance, establish consent, or claim that OLC, OST,
or another Nation has adopted a named framework. It distinguishes:

  PUBLIC DATA     : federal/public datasets used in analysis notebooks
  TRIBAL DATA     : Tribal observational data used in the pipeline only

Tribal observational data (pasture conditions, grazing logs, animal counts,
well levels) is NEVER committed to this repository. Only templates, processing
scripts, and documentation are version-controlled.

References
OCAP®  : https://fnigc.ca/ocap-training/
CARE   : https://www.gida-global.org/care
FAIR   : https://www.go-fair.org/fair-principles/

IEEE 2890-2025: Recommended Practice for Provenance of Indigenous Peoples' Data
  The first international standard for Indigenous data provenance. Establishes
  common parameters for describing and recording how data about or related to
  Indigenous Peoples should be disclosed, connected to people and place, and
  governed across its lifecycle — including AI/ML and biodiversity contexts.
  Reference: https://standards.ieee.org/ieee/2890/10318/

"""

from dataclasses import dataclass, field
from typing import Optional


# Data source registry 

@dataclass
class DataSource:
    name:          str
    url:           str
    steward:       str
    tribal_data:   bool          # True = Tribal observational data (not for public repo)
    license:       str
    fair_notes:    str
    attribution:   str
    ocap_notes:    Optional[str] = None
    care_notes:    Optional[str] = None


DATA_SOURCES: dict[str, DataSource] = {

    "census_aiannh": DataSource(
        name="Census TIGER AIANNH Boundaries",
        url="https://www.census.gov/cgi-bin/geo/shapefiles/index.php",
        steward="US Census Bureau",
        tribal_data=False,
        license="Public domain (federal government)",
        fair_notes=(
            "TIGER 2023 vintage. American Indian/Alaska Native/Native Hawaiian "
            "Areas shapefile. WGS84. Available via HTTPS download."
        ),
        attribution="US Census Bureau, TIGER/Line Shapefiles (2023).",
        ocap_notes=(
            "Census-defined boundaries are for statistical purposes only. "
            "They do not represent legal jurisdiction or Tribal self-definition. "
            "Tribal Nations were not the primary stewards of this data collection. "
            "Use common-name designations (ex. 'Oglala Lakota') not Census codes."
        ),
        care_notes=(
            "Census data was collected by the federal government under federal "
            "authority, not under Tribal Authority to Control. Collective Benefit "
            "to Tribal Nations depends on how results are applied."
        ),
    ),

    "usda_nass": DataSource(
        name="USDA NASS QuickStats Agricultural Census",
        url="https://quickstats.nass.usda.gov/",
        steward="USDA National Agricultural Statistics Service",
        tribal_data=False,
        license="Public domain (federal government)",
        fair_notes=(
            "County-level agricultural statistics including livestock counts, "
            "crop production, land use. Quinquennial census + annual surveys. "
            "Free API access: register at https://quickstats.nass.usda.gov/api"
        ),
        attribution=(
            "USDA National Agricultural Statistics Service (NASS). "
            "Census of Agriculture and agricultural surveys."
        ),
        ocap_notes=(
            "NASS data is county-level and does not distinguish Tribal land from "
            "non-Tribal land within a county. It is a proxy only. Tribal Nations "
            "own their own agricultural data; NASS does not represent Tribal "
            "agricultural knowledge or Tribal-specific conditions."
        ),
        care_notes=(
            "NASS county data systematically undercounts Tribal agricultural "
            "activity because federal trust land reporting differs from fee "
            "simple land. Analysis using NASS should note this limitation "
            "explicitly to avoid misrepresenting Tribal agricultural capacity."
        ),
    ),

    "noaa_pdsi": DataSource(
        name="NOAA Climate Division Palmer Drought Severity Index",
        url="https://www.ncei.noaa.gov/pub/data/cirs/climdiv/",
        steward="NOAA National Centers for Environmental Information",
        tribal_data=False,
        license="Public domain (federal government)",
        fair_notes=(
            "Monthly PDSI by NOAA climate division. South Dakota has 9 climate "
            "divisions. Covers 1895–present. Text file format, updated monthly."
        ),
        attribution=(
            "NOAA National Centers for Environmental Information. "
            "Climate Division Data: Palmer Drought Severity Index."
        ),
        care_notes=(
            "Drought index is based on climate division boundaries that do not "
            "correspond to Tribal land boundaries. Values should be interpreted "
            "as regional context, not Tribal-specific drought conditions."
        ),
    ),

    "modis_ndvi": DataSource(
        name="MODIS Terra Vegetation Indices (MOD13Q1)",
        url="https://lpdaac.usgs.gov/products/mod13q1v061/",
        steward="NASA Land Processes Distributed Active Archive Center (LP DAAC)",
        tribal_data=False,
        license="Public domain (NASA)",
        fair_notes=(
            "16-day composite NDVI at 250m resolution. Terra MODIS Collection 6.1. "
            "Available via NASA Earthdata (free registration required) or "
            "Google Earth Engine (MODIS/061/MOD13Q1)."
        ),
        attribution=(
            "Didan, K. (2021). MODIS/Terra Vegetation Indices 16-Day L3 Global "
            "250m SIN Grid V061. NASA EOSDIS Land Processes DAAC. "
            "doi: 10.5067/MODIS/MOD13Q1.061"
        ),
        ocap_notes=(
            "NDVI is a satellite-derived proxy for vegetation condition. It does "
            "not capture Tribal knowledge of pasture quality, species composition, "
            "or cultural significance of specific plant communities."
        ),
        care_notes=(
            "NDVI is used here as a public data proxy that motivates Tribal-led "
            "on-the-ground observation (pasture condition scoring). The goal is to "
            "show what satellite data cannot see, not to replace Tribal knowledge."
        ),
    ),

    "usgs_nwis_groundwater": DataSource(
        name="USGS National Water Information System Groundwater",
        url="https://waterservices.usgs.gov/nwis/",
        steward="US Geological Survey",
        tribal_data=False,
        license="Public domain (federal government)",
        fair_notes=(
            "Well water level measurements via USGS NWIS REST API. "
            "Coverage is sparse on many Tribal lands, so gaps are a finding, "
            "not an absence of groundwater importance."
        ),
        attribution="USGS National Water Information System (NWIS).",
        care_notes=(
            "USGS monitoring well coverage is much sparser on Tribal lands than "
            "in the selected query. Causes and equity implications require "
            "additional evidence and locally authorized review."
        ),
    ),

    "gridmet": DataSource(
        name="gridMET Daily Surface Meteorological Data",
        url="https://www.climatologylab.org/gridmet.html",
        steward="University of Idaho Climatology Lab",
        tribal_data=False,
        license="Creative Commons CC0",
        fair_notes=(
            "Daily 4km gridded surface meteorology for CONUS. Variables include "
            "temperature, precipitation, wind, humidity, ETo, and fire indices. "
            "Access via OPeNDAP THREDDS. 1979–present."
        ),
        attribution=(
            "Abatzoglou, J.T. (2013). Development of gridded surface meteorological "
            "data for ecological applications and modelling. International Journal "
            "of Climatology. doi:10.1002/joc.3413"
        ),
    ),

    "pasture_conditions": DataSource(
        name="Tribal Pasture Condition Observations",
        url="",
        steward="Tribal Nation: data ownership per OCAP® principles",
        tribal_data=True,
        license="Tribal data: not for public distribution",
        fair_notes=(
            "Field-collected pasture condition scores (1–5 NRCS scale). "
            "Collected by Tribal land managers. Schema defined in "
            "data/templates/pasture_conditions_template.xlsx"
        ),
        attribution="[Tribal Nation name] Land Management Program.",
        ocap_notes=(
            "This data is Owned, Controlled, Accessed, and Possessed by the "
            "Tribal Nation that collected it. It is never committed to this "
            "repository. It resides on Tribal infrastructure. Any sharing, "
            "aggregation, or publication of this data requires explicit Tribal "
            "consent and governance review."
        ),
        care_notes=(
            "Collective Benefit: analysis results are returned to the Tribal "
            "Nation first before any external sharing. "
            "Authority to Control: Tribal Nation controls all access decisions. "
            "Responsibility: analysis supports Tribal land management goals. "
            "Ethics: data is not used for purposes beyond those agreed with the Tribe."
        ),
    ),

    "grazing_log": DataSource(
        name="Tribal Grazing Log",
        url="",
        steward="Tribal Nation: data ownership per OCAP® principles",
        tribal_data=True,
        license="Tribal data: not for public distribution",
        fair_notes=(
            "Field-collected grazing records: pasture, date, animal count, days. "
            "Schema: data/templates/grazing_log_template.xlsx"
        ),
        attribution="[Tribal Nation name] Land Management Program.",
        ocap_notes=(
            "Grazing and livestock data is sensitive operational information. "
            "It is Owned and Controlled by the Tribal Nation. Never committed "
            "to version control. Tribal consent required for any use beyond "
            "internal land management."
        ),
        care_notes=(
            "Grazing data represents generations of Tribal ranching and bison "
            "management knowledge. Analysis must center Tribal land management "
            "goals, not external agricultural productivity frameworks."
        ),
    ),

    "groundwater_tribal": DataSource(
        name="Tribal Groundwater/Well Level Observations",
        url="",
        steward="Tribal Nation: data ownership per OCAP® principles",
        tribal_data=True,
        license="Tribal data: not for public distribution",
        fair_notes=(
            "Well water level measurements collected by Tribal water programs. "
            "Schema: data/templates/groundwater_template.xlsx"
        ),
        attribution="[Tribal Nation name] Water Resources Program.",
        ocap_notes=(
            "Water data is sovereign. The Tribal Nation owns, controls, and "
            "possesses this data. It is never committed to version control. "
            "Location data for wells is particularly sensitive."
        ),
        care_notes=(
            "Water is central to Tribal sovereignty, treaty rights, and cultural "
            "practice. Analysis must serve Tribal water management goals and "
            "support Tribal water rights assertions."
        ),
    ),
}


# Acknowledgment and citation functions 

_FRAMEWORK_PREAMBLE = """
DATA GOVERNANCE ACKNOWLEDGMENT (DRAFT; LOCAL REVIEW PENDING)
This analysis uses data that describes Indigenous and Tribal lands,
communities, and agricultural and water systems. This project is
informed by reference frameworks whose local applicability remains under review:

OCAP®  : A Canadian First Nations framework included as a reference point;
  naming it does not mean it has been adopted locally.
  Reference: https://fnigc.ca/ocap-training/

CARE   : Data use must deliver Collective Benefit to Indigenous peoples,
  respect their Authority to Control, uphold Responsibility to
  communities, and center Ethics across the full data lifecycle.
  Reference: https://www.gida-global.org/care

FAIR   : Data is Findable, Accessible, Interoperable, and Reusable.
  FAIR governs technical standards; it does not determine local authority,
  ethics, permission, or release decisions.
  Reference: https://www.go-fair.org/fair-principles/

IEEE 2890-2025 : Recommended Practice for Provenance of Indigenous Peoples' Data.
  Establishes common parameters for Indigenous data provenance : describing and
  recording how data about Indigenous Peoples should be disclosed, connected to
  people and place, and governed across its lifecycle.
  Reference: https://standards.ieee.org/ieee/2890/10318/

CRITICAL DISTINCTION IN THIS SERIES:
  PUBLIC DATA  : federal/public datasets used in analysis notebooks.
                 These are openly accessible and described below.
  TRIBAL DATA  : Tribal observational data (pasture conditions, grazing
                 logs, animal counts, well levels). This data is NEVER
                 committed to this repository. It lives on Tribal
                 infrastructure only under a separately approved process.
                 No such operational dataset is included or authorized here.
"""

_TEK_DISCLAIMER = """
TRADITIONAL ECOLOGICAL KNOWLEDGE (TEK) DISCLAIMER
This analysis uses publicly available proxy data (satellite NDVI,
federal weather stations, USDA statistics) as approximations of
conditions on Tribal lands. These proxies do not represent:

  • Tribal knowledge of specific plant communities and their meaning
  • Multi-generational grazing and land management knowledge
  • Seasonal patterns observed through Tribal cultural practice
  • The relationship between land condition and cultural wellbeing

The repository cannot authorize collection from or validation by local
knowledge holders. Any such process requires appropriate governance,
consent, purpose, and local authority before it begins.
"""


def print_data_acknowledgment(source_keys: list[str] | None = None) -> None:
    print(_FRAMEWORK_PREAMBLE)
    print(_TEK_DISCLAIMER)
    if source_keys:
        print("DATA SOURCES USED IN THIS ANALYSIS:")
        for key in source_keys:
            src = DATA_SOURCES.get(key)
            if src is None:
                continue
            tribal_flag = " [TRIBAL DATA: NOT IN REPO]" if src.tribal_data else ""
            print(f"\n  • {src.name}{tribal_flag}")
            print(f"    Steward : {src.steward}")
            if src.ocap_notes:
                print(f"    OCAP®   : {src.ocap_notes}")
            if src.care_notes:
                print(f"    CARE    : {src.care_notes}")


def generate_citations(source_keys: list[str]) -> str:
    lines = ["REFERENCES AND DATA CITATIONS", ]
    for key in source_keys:
        src = DATA_SOURCES.get(key)
        if src and src.attribution:
            lines.append(f"\n{src.name}:")
            lines.append(f"  {src.attribution}")
            if src.url:
                lines.append(f"  URL: {src.url}")
    return "\n".join(lines)


def check_tribal_data_governance(source_key: str) -> dict:
    """
    Returns governance requirements for a data source.
    Use before loading any Tribal observational data.
    """
    src = DATA_SOURCES.get(source_key)
    if src is None:
        return {"error": f"Unknown source key: {source_key}"}
    return {
        "source":          src.name,
        "tribal_data":     src.tribal_data,
        "consent_required": src.tribal_data,
        "commit_to_repo":  not src.tribal_data,
        "ocap_notes":      src.ocap_notes,
        "care_notes":      src.care_notes,
    }

#  My GeoDev Lab Africa Project

## Project: 
### 🔗 Lagos Flood Resilience and Access to Essential Services

### 🔗 Purpose

  The platform will allow users to select a settlement, view its flood-exposure information and compare dated flood observations. Users can also explore how possible road closures could make journeys to essential services longer or leave a settlement without a usable route. Each result will include its source, date and limitations.


### 🔗  Project Question
  Which settlement areas in Eti-Osa may be exposed to flooding, what dated flood evidence is available, and how could road disruption affect access to essential services?


#### `NOTE:` This repo documents my 12months GeoDevLabAfrica Cohort-One Project workflow. See full [project-brief.md](/project-brief.md) here 

---
# Project Progress

| Month | Week | Activites | Output |
|---|---|---|---|
| **Month 1** | **Week 1** | Define the spatial problem and source datasets | Project question, study area and required datasets established |
| **Month 1** | **Week 2** | Get, organise and describe the data | Datasets acquired, organised and documented |
| **Month 1** | **Week 3** | Prepare data through Cleaning, Extraction, clipping and reprojection | ETI-OSA datasets prepared for spatial analysis |
| **Month 1** | **Week 4** | Perform spatial operations and analysis | This analysis identifies settlement areas in Eti-Osa that are both low-lying (≤5 m          elevation) and within 500 m of the Atlantic coast, Lagos Lagoon or selected mapped waterways. |
| **Month 2** | **Week 5** | Set up Python, UV, VSCode and terminal | Python dev environment established and first .py file (`hello.py`) successfully executed |

---

# Month 1 — GIS Project Foundation

**Month 1** covered **Weeks 1–4** and established the GIS foundation of the project.

This month was about defining a spatial problem `Lagos Flood Resilience and Access to Essential Services`, identifying relevant datasets, sourcing for these datasets, performed Data Cleaning and Extraction, determining the limitation of the Datasets and analysing these datasets

## Week 1 — Defining a spatial problem and Sourcing Data

### Tasks Completed

- Defined the first project question : **Which settlement areas in Eti-Osa are located in places that may be more exposed to flooding because they are both low-lying and close to major water features?**
- Selected **Eti-Osa** LGA as the study area.
- Identified the datasets required for the analysis.
- Datasets Needed:
  - Eti-Osa Boundary
  - Natural Water
  - Coastline
  - Eti-Osa Elevation Data
  - Eti-Osa Settlement Extents

### Result

A clearly defined spatial problem, study area and initial dataset requirements were established.

**Task documentation:** [`project-brief.md`](/doc/01-project-brief.md)


## Week 2 — Getting and Describing the Data

### Tasks Completed

- Created a structured project folder.
- Organised raw datasets and project files.
- Downloaded the required datasets to the **raw data folder**.
- Obtained relevant datasets from different sources.
- Documented important characteristics of the datasets, including:
  - Data sources
  - Feature counts
  - Geometry types
  - Coordinate reference systems
  - Attributes
  - Missing values
  - Geometry quality
  - Spatial coverage
  - Potential data-quality issues / limitation

### Result

The outcome was an organised and structured project folder and dataset with a clear documentaion before starting any analysis

**Task documentation:** [`data-notes.md`](/doc/02-data-notes.md)


---

## Week 3 — Data Quality Preparation: Clipping and Reprojection

### Tasks Completed

- Clipped the geographic datasets to the **Eti-Osa Boundary Layer**.
- Examined each of the datasets quality: **COMPLETENESS:** ,**CURRENCY:**, **POSITIONAL:** , **ATTRIBUTE:** , **FITNESS:**
- Reprojected the datasets from **EPSG:4326 — WGS 84** to **WGS 84 / **EPSG:32631 — WGS 84 / UTM Zone 31N**.
- Prepared the datasets for distance and area calculations.
- **Calculated study-area size:** approximately **243.42 km²**, measured using the projected EPSG:32631 boundary.

### Result

A consistent set of **clipped and projected datasets** was produced, creating datasets ready and appropriate for the analysis 

**Task documentation:** [`data-preparation.md`](/doc/03-data-preparation.md)

## Week 4 — Spatial Operations and Analysis

### Major Tasks

- Used the **Raster Calculator** to identify land at or below **5 m elevation**.
- Created **500-metre buffers** around selected water features, including the coastline, water bodies, rivers, streams and canals.
- Merged and dissolved the buffer outputs into a single **water-proximity zone**.
- Used **intersection** to combine low elevation and water proximity into a **potential flood-exposure zone**.
- Used **clip** to extract settlement extents falling within the potential flood-exposure zone.
- Calculated settlement areas and checked the spatial outputs.

### Result

The spatial analysis produced:

1. A **low-elevation zone** representing land at **≤ 5 m elevation**.
2. A combined **500 m water-proximity zone**.
3. A **potential flood-exposure zone** where both screening conditions overlap.
4. Mapped settlement extents located within the potential flood-exposure zone.

Out of **5,895 mapped settlement extents**, **2,264 (38.4%)** have some area within the potential flood-exposure zone.

These outputs provide the foundation for identifying low-lying settlements near major water features and for further analysis of flood exposure and its potential effects on access to essential services in Eti-Osa LGA.


**Task documentation:** [`month-1-summary.md`](month-1-summary.md)
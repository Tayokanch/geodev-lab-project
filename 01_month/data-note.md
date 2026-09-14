# Week 2 Data Note

## Project

**Flood Exposure Screening in Eti-Osa LGA, Lagos**

## Research Question

Which settlement areas in Eti-Osa are located in low-elevation areas and close to major water bodies?

---

## 1. Eti-Osa LGA Boundary

- **Source:** GRID3 Nigeria Operational LGA Boundaries
- **Source URL:**  [URL](https://data.grid3.org/datasets/GRID3%3A%3Agrid3-nga-operational-lga-boundaries/about)
- **File**: [Downloaded File](/01_month/data/eti_osa_boundary.gpkg)
- **Geometry:** Polygon
- **Feature count:** 1
- **Original CRS:** WGS 84 / EPSG:4326
- **Analysis CRS:** WGS 84 / UTM Zone 31N — EPSG:32631
- **Key columns:** `osm_id`, `name`, `geometry_type`
- **Missing values:** No important missing values affecting the analysis.
- **Observations:**
The Eti-Osa LGA polygon was extracted from the national GRID3 boundary dataset and is used to define the study area and clip other datasets.

---

## 2. Natural Water

- **Source:** OpenStreetMap, extracted using QuickOSM in QGIS
- **Source URL:** [URL](https://www.openstreetmap.org)
- **File**: [Downloaded File](/01_month/data/natural_water.gpkg)
- **Geometry:** Polygon
- **Feature count:** 4
- **Original CRS:** WGS 84 / EPSG:4326
- **Analysis CRS:** WGS 84 / UTM Zone 31N — EPSG:32631
- **Key columns:** `name`, `natural`, `water`
- **Missing values:** One features contained NULL value `water` type field 


- **Observations:**
The original extraction contained water, wetland, lagoon, river, lake, pond and wastewater features. The dataset was cleaned to retain relevant lagoon and river water polygons.

---

## 3. Coastal Line

- **Source URL:** [URL](https://www.openstreetmap.org)
- **File**: [Downloaded File](/01_month/data/natural_coastline.gpkg)
- **Geometry:** Line
- **Feature count:** 3
- **Original CRS:** WGS 84 / EPSG:4326
- **Analysis CRS:** WGS 84 / UTM Zone 31N — EPSG:32631
- **Key columns:** `osm_type`
- **Missing values:** None

---

## 4. Eti-Osa DEM

- **Source:** SRTM GL1 Global 30 m via OpenTopography
- **Download method:** OpenTopography DEM Downloader plugin in QGIS
- **Source URL:** [URL](https://portal.opentopography.org/raster?jobId=rt1780001421000)
- **File**: [Downloaded File](/01_month/data/eti_osa_DEM.tif)
- **Data type:** Single-band raster (GeoTIFF, Int16)
- **Resolution:** Approximately 30.7 m
- **Raster dimensions:** 992 × 471 pixels
- **Original CRS:** WGS 84 / EPSG:4326
- **Analysis CRS:** WGS 84 / UTM Zone 31N — EPSG:32631
- **NoData value:** -32768
- **Minimum elevation:** -12 m
- **Maximum elevation:** 35 m
- **Mean elevation:** Approximately 3.97 m
- **Valid data:** 55.22%

- **Observations:**
The SRTM DEM was downloaded directly into QGIS using the OpenTopography DEM Downloader and clipped to the Eti-Osa study area. It was reprojected to EPSG:32631 for analysis. The DEM will be used to identify areas at or below the project's 5 m elevation threshold.

---

## 5. Eti-Osa Settlement Extents

- **Source:** GRID3 Nigeria Settlement Extents v4.1
- **Source URL:** [URL](https://data.grid3.org/datasets/GRID3%3A%3Agrid3-nga-settlement-extents-v4-1/about)
- **File**: [Downloaded File](/01_month/data/eti_osa_settlement.gpkg)
- **Geometry:** Polygon
- **Feature count:** 5895
- **Original CRS:** WGS 84 / EPSG:4326
- **Analysis CRS:** WGS 84 / UTM Zone 31N — EPSG:32631
- **Key columns:** block_area_sqm, building_count , building_count_density etc
- **Missing values:** None

- **Observations:**
The layer represents mapped settlement footprints rather than settlement point locations. It will be used to identify and measure settlement areas that overlap with the low-elevation and major-water proximity zones.

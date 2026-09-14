# Week 2 Data Note

## Project

**Flood Exposure Screening in Eti-Osa LGA, Lagos**

## Research Question

Which settlement areas in Eti-Osa are located in low-elevation areas and close to major water bodies?

---

## 1. Nigeria Operational LGA Boundaries

- **Source:** GRID3 Nigeria Operational LGA Boundaries
- **Source URL:**  [URL](https://data.grid3.org/datasets/GRID3%3A%3Agrid3-nga-operational-lga-boundaries/about)
- **Downloaded**: September 2026
- **Geometry:** Polygon
- **Feature count:** 774
- **Original CRS:** WGS 84 / EPSG:4326
- **Key columns:** `osm_id`, `name`, `geometry_type`
- **Missing values:** No important missing values.

- **Observations:**
The Eti-Osa LGA polygon will be extracted from this dataset for study area and will be clipped to other relevant datasets.

---

## 2. Natural Water

- **Source:** OpenStreetMap, extracted using QuickOSM in QGIS
- **Query**: `natural=water within eti-osa boundary layer extent  `
- **Extracted**: September 2026
- **Geometry:** Polygon
- **Feature count:** 69
- **Original CRS:** WGS 84 / EPSG:4326
- **Key columns:** `name`, `natural`, `water`, `place`, `description`
- **Missing values:** Yes, there's a couple of fields and features that contains NULL
  
- **Observations:**
The contained water, wetland, lagoon, river, lake, pond and wastewater features. This dataset will be cleaned to retain relevant lagoon and river water polygons.

---

## 3. Coastal Line
- **Source:** OpenStreetMap, extracted using QuickOSM in QGIS
- **Query**: `natural=coastalline within eti-osa boundary layer extent  `
- **Extracted**: September 2026
- **Geometry:** Line
- **Feature count:** 3
- **Original CRS:** WGS 84 / EPSG:4326
- **Key columns:** `osm_type`
- **Missing values:** None

---

## 4. Eti-Osa DEM

- **Source:** SRTM GL1 Global 30 m via OpenTopography
- **Method:** OpenTopography DEM Downloader plugin in QGIS
- **Extracted**: September 2026
- **Source URL:** [URL](https://portal.opentopography.org/raster?jobId=rt1780001421000)
- **Data type:** Single-band raster (GeoTIFF, Int16)
- **Resolution:** Approximately 30.7 m
- **Raster dimensions:** 992 × 471 pixels
- **Original CRS:** WGS 84 / EPSG:4326
- **NoData value:** -32768
- **Minimum elevation:** -12 m
- **Maximum elevation:** 35 m
- **Mean elevation:** Approximately 3.97 m
- **Valid data:** 55.22%

- **Observations:**
The SRTM DEM was downloaded directly into QGIS using the OpenTopography DEM Downloader and clipped to the Eti-Osa study area. It will be reprojected to EPSG:32631 for analysis. The DEM will be used to identify areas at or below the project's 5 m elevation threshold.

---

## 5. Eti-Osa Settlement Extents

- **Source:** GRID3 Nigeria Settlement Extents v4.1
- **Source URL:** [URL](https://data.grid3.org/datasets/GRID3%3A%3Agrid3-nga-settlement-extents-v4-1/about)
- **Downloaded**: September 2026
- **Geometry:** Polygon
- **Feature count:** 9097
- **Original CRS:** WGS 84 / EPSG:4326
- **Key columns:** block_area_sqm, building_count , building_count_density, etc.
- **Missing values:** None

- **Observations:**
The layer represents mapped settlement footprints. It will be used to identify and measure settlement areas that overlap with the low-elevation and major-water proximity zones.

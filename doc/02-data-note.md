# Week 2 Data Note

## Project

**Flood Exposure Screening in Eti-Osa LGA, Lagos**

## Research Question

Which settlement areas in Eti-Osa are located in low-elevation areas and close to major water bodies?

---

## 1. Eti-Osa Boundary Layer

* **Source:** GRID3 Nigeria Operational LGA Boundaries
* **Source URL:** https://data.grid3.org/datasets/GRID3%3A%3Agrid3-nga-operational-lga-boundaries/about
* **Downloaded:** September 2026
* **Geometry:** Polygon
* **Feature count:** 774 features in the source dataset
* **Original CRS:** WGS 84 / EPSG:4326
* **Key columns:** `name`, `type`, `boundary`, `admin_level`
* **Missing values:** No important missing values were identified in the fields required for this project.

**Observations:**
The source dataset contains LGA boundaries across Nigeria. The Eti-Osa LGA polygon will be extracted and used as the study-area boundary for clipping and analysing the other project datasets.

---

## 2. Natural Water

* **Source:** OpenStreetMap, extracted using QuickOSM in QGIS
* **Query:** `natural=water` within the Eti-Osa boundary layer extent
* **Extracted:** `9 September 2026`
* **Geometry:** Polygon
* **Feature count:** 69 features in the original extraction
* **Original CRS:** WGS 84 / EPSG:4326
* **Key columns:** `name`, `natural`, `water`, `place`, `description`
* **Missing values:** Several optional attributes contain NULL values, including some `name` and `water` values.

**Observations:**
The original extraction contained different water-related features, including lagoon, river, lake, pond and wastewater classifications, as well as some NULL values. The dataset was reviewed and cleaned to retain water polygons relevant to the Month 1 analysis, particularly lagoon and river features. Wetlands, ponds, wastewater features and the isolated lake within LUFASI Nature Park were excluded from the primary analysis.

---

## 3. Coastline

* **Source:** OpenStreetMap, extracted using QuickOSM in QGIS
* **Query:** `natural=coastline` within the Eti-Osa boundary layer extent
* **Extracted:** September 2026
* **Geometry:** Line
* **Feature count:** 3
* **Original CRS:** WGS 84 / EPSG:4326
* **Key columns:** `osm_type`
* **Missing values:** No important missing values affecting its intended use.

**Observations:**
The layer represents the Atlantic-facing coastline within the study area. It will be used alongside major natural water features to represent proximity to coastal water.

---

## 4. Eti-Osa DEM

* **Source:** SRTM GL1 Global 30 m via OpenTopography
* **Method:** OpenTopography DEM Downloader plugin in QGIS
* **Source URL:** https://portal.opentopography.org/raster?jobId=rt1780001421000
* **Extracted:** September 2026
* **Data type:** Single-band raster, GeoTIFF, Int16
* **Resolution:** Approximately 30.7 m
* **Raster dimensions:** 992 × 471 pixels
* **Original CRS:** WGS 84 / EPSG:4326
* **Analysis CRS:** WGS 84 / UTM Zone 31N — EPSG:32631
* **NoData value:** -32768
* **Minimum elevation:** -12 m
* **Maximum elevation:** 35 m
* **Mean elevation:** Approximately 3.97 m
* **Valid data:** 55.22%

**Observations:**
The SRTM DEM was downloaded into QGIS using the OpenTopography DEM Downloader and clipped to the Eti-Osa study area. It has been prepared for analysis in EPSG:32631. The raster will be used to identify areas at or below the project's 5 m elevation threshold.


---

## 5. Eti-Osa Settlement Extents

* **Source:** GRID3 Nigeria Settlement Extents v4.1
* **Source URL:** https://data.grid3.org/datasets/GRID3%3A%3Agrid3-nga-settlement-extents-v4-1/about
* **Downloaded:** September 2026
* **Geometry:** Polygon
* **Feature count:** 9,097
* **Original CRS:** WGS 84 / EPSG:4326
* **Key columns:** `block_area_sqm`, `building_count`, `building_count_density`
* **Missing values:** No important missing values were identified in the fields required for this project.

**Observations:**
The dataset represents mapped settlement footprints rather than settlement point locations. It will be used to identify and measure settlement areas that overlap with the low-elevation and major-water proximity zones.

---

## Overall Data Quality Considerations

The datasets provide a suitable foundation for a preliminary flood-exposure screening of Eti-Osa LGA. However, the analysis has several limitations that should be considered when interpreting the results.

The OpenStreetMap natural-water dataset is incomplete in some areas and may therefore underestimate proximity to relevant water bodies. The SRTM DEM provides approximately 30 m elevation data and is suitable for broad screening, but it does not represent recent terrain changes and is not precise enough for engineering-level flood modelling.

The final Month 1 results should therefore be interpreted as a **screening of potential exposure** rather than a prediction of where flooding will definitely occur.



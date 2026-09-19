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

### Quality Note

* **COMPLETENESS:** The dataset contains an Eti-Osa LGA boundary covering the full study area required for this project.

* **CURRENCY:** The dataset was last updated on `10 April 2023`.

* **POSITIONAL:** The Eti-Osa boundary visually aligns closely with the corresponding administrative boundary shown on the OSM basemap, with no obvious large positional offset observed.

* **ATTRIBUTE:** The dataset contains the essential administrative attributes required to identify the study area, including `name`, `type`, `boundary` and `admin_level`.

* **FITNESS:** Suitable for defining the Eti-Osa study area and for clipping the settlement, elevation and water datasets to a common analysis extent.

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

### Quality Note

* **COMPLETENESS:** Coverage is incomplete. Visual comparison with the OSM basemap showed that some visible water bodies were not present in the extracted dataset. This may cause some areas near unmapped water bodies to be missed in the proximity analysis.

* **CURRENCY:** The most recent update identified in the dataset was `30 July 2025`.

* **POSITIONAL:** The mapped water polygons generally align well with the corresponding water features shown on the OSM basemap. No obvious systematic positional offset was observed, although some water bodies are incompletely mapped.

* **ATTRIBUTE:** The main fields required for classification are `name`, `natural` and `water`. Most retained features have usable water-type information, but some features contain NULL values and at least one feature could not be confidently classified from its attributes alone.

* **FITNESS:** Suitable for preliminary proximity analysis of mapped major water bodies. However, incomplete OSM water coverage may cause the analysis to underestimate exposure in areas where relevant water features have not been mapped.

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

### Quality Note

* **COMPLETENESS:** The extracted coastline appears continuous across the Atlantic-facing section of the Eti-Osa study area, with no obvious major gaps observed during visual inspection.

* **CURRENCY:** The most recent update identified was `1 December 2025`.

* **POSITIONAL:** The coastline visually aligns with the coastal boundary shown on the OSM basemap, with no obvious systematic displacement observed.

* **ATTRIBUTE:** The layer contains limited attribute information, but the OSM coastline classification is sufficient for identifying the feature for this analysis.

* **FITNESS:** Suitable for representing proximity to the Atlantic coast and for creating the planned 500 m coastal proximity zone used in the Month 1 flood-exposure screening.

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

### Quality Note

* **COMPLETENESS:** The DEM covers the Eti-Osa study area. Approximately 55.22% of the rectangular raster contains valid elevation values, while the remaining cells are NoData, mainly representing areas outside the clipped LGA boundary.

* **CURRENCY:** SRTM elevation data was collected during the Shuttle Radar Topography Mission in February 2000.

* **POSITIONAL:** The DEM is correctly georeferenced and visually aligns with the Eti-Osa boundary after reprojection. Its approximately 30 m spatial resolution limits representation of very small or fine-scale terrain features.

* **ATTRIBUTE:** Elevation is stored in a single raster band. Valid elevation values range from -12 m to 35 m, with a mean of approximately 3.97 m. The NoData value is -32768.

* **FITNESS:** Suitable for broad low-elevation screening across Eti-Osa. However, its resolution and vertical limitations mean it should not be treated as an engineering-grade elevation model or used for precise property-level flood prediction.

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

### Quality Note

* **COMPLETENESS:** The settlement polygons provide extensive coverage of built-up areas across Eti-Osa. Visual comparison with the basemap did not reveal obvious large built-up areas missing from the dataset, although full completeness cannot be guaranteed through visual inspection alone.

* **CURRENCY:** The dataset was last updated on `4 August 2026`.

* **POSITIONAL:** Settlement polygons generally correspond visually with mapped built-up areas, with no obvious systematic positional displacement observed.

* **ATTRIBUTE:** Important quantitative attributes such as `block_area_sqm`, `building_count` and `building_count_density` are available and appear consistently structured. No important NULL values were identified in the fields required for this project.

* **FITNESS:** Suitable for representing settlement footprints and for calculating the amount and proportion of settlement area intersecting the low-elevation and major-water proximity zones.

---

## Overall Data Quality Considerations

The datasets provide a suitable foundation for a preliminary flood-exposure screening of Eti-Osa LGA. However, the analysis has several limitations that should be considered when interpreting the results.

The OpenStreetMap natural-water dataset is incomplete in some areas and may therefore underestimate proximity to relevant water bodies. The SRTM DEM provides approximately 30 m elevation data and is suitable for broad screening, but it does not represent recent terrain changes and is not precise enough for engineering-level flood modelling.

The final Month 1 results would therefore be interpreted as a **screening of potential exposure** rather than a prediction of where flooding will definitely occur.


## CRS and Preparation

* All source layers were originally provided in **EPSG:4326 — WGS 84**.
* **Study area:** Eti-Osa LGA, extracted from the GRID3 Nigeria Operational LGA Boundaries dataset.
* Relevant datasets were clipped to the Eti-Osa study area and prepared for analysis in **EPSG:32631 — WGS 84 / UTM Zone 31N**.
* **Calculated study-area size:** approximately **243.42 km²**, measured using the projected EPSG:32631 boundary.
* Raw source files were kept unchanged, while cleaned, clipped and reprojected working files were stored separately in [processed file](/my-project/data/processed/) .

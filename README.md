# geodev-lab-project

# Project Brief: Flood Exposure Screening in Eti-Osa LGA, Lagos

## Part 1: The question

Which settlement areas in Eti-Osa Local Government Area lie below 5 metres elevation and within 500 metres of the Atlantic coast, Lagos Lagoon or a mapped waterway?

## Part 2: Why it matters

Flooding is a recurring problem in Eti-Osa. An initial exposure map could help emergency and environmental officers identify settlement areas that may need closer investigation, field assessment or more detailed flood analysis. The map would be used as an initial screening tool rather than as a prediction of exactly where flooding will occur.

## Part 3: The data I need

* Eti-Osa Local Government Area boundary
* Settlement extent polygons for Eti-Osa
* Elevation data at approximately 30 metre resolution
* Atlantic coastline, Lagos Lagoon and mapped waterways

## Part 4: Where the data comes from

* **LGA boundary:** GRID3 NGA Operational LGA Boundaries
  [GRID3 LGA Boundaries dataset](https://data.grid3.org/datasets/GRID3%3A%3Agrid3-nga-operational-lga-boundaries/about)

* **Settlement extents:** GRID3 NGA Settlement Extents v4.1, August 2026
  [GRID3 Settlement Extents v4.1](https://data.grid3.org/datasets/GRID3%3A%3Agrid3-nga-settlement-extents-v4-1/about)

* **Elevation:** SRTM GL1 Global 30 m, accessed through OpenTopography
  [SRTM GL1 30 m dataset](https://portal.opentopography.org/raster?jobId=rt1780001421000)

* **Coastline, lagoon and waterways:** OpenStreetMap, using the Nigeria extract from Geofabrik and clipping the required features to Eti-Osa
  [OpenStreetMap Nigeria data extract](https://download.geofabrik.de/africa/nigeria.html?utm_source=chatgpt.com)

## Part 5: What I would build

I would build a clear flood-exposure screening map of Eti-Osa showing settlement areas that meet both conditions: land below 5 metres elevation and location within 500 metres of the coast, lagoon or a mapped waterway.

This would form the first version of my one-year GeoDev Lab project, which I can build on over time by adding population, building and observed flood-event data as my geospatial skills develop.

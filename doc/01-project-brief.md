# Project Brief: 
## Lagos Flood Resilience and Access to Essential Services

 ###  Study area: `Eti-Osa LGA, Lagos`


## 🔗 Project Question

Which communities in Eti-Osa occupy potentially flood-exposed locations, what dated evidence of flooding is available, and how could road disruption affect access to essential services?

## Why it matters

Flooding is a recurring concern in parts of Eti-Osa, and Lagos State flood warnings reinforce the need for continued assessment and preparedness. I am building this platform to help users identify settlement areas that may be exposed to flooding and explore how possible road closures could make essential services harder to reach. The platform will make these analyses repeatable and accessible through an interactive map.

## The data I need

* Eti-Osa Local Government Area boundary
* Settlement extent polygons for Eti-Osa
* Elevation data at approximately 30 metre resolution
* Atlantic coastline, Lagos Lagoon and mapped waterways
* Mapped essential infrastructure

## Where the data comes from

* **LGA boundary:** GRID3 NGA Operational LGA Boundaries
  [GRID3 LGA Boundaries dataset](https://data.grid3.org/datasets/GRID3%3A%3Agrid3-nga-operational-lga-boundaries/about)

* **Settlement extents:** GRID3 NGA Settlement Extents v4.1, August 2026
  [GRID3 Settlement Extents v4.1](https://data.grid3.org/datasets/GRID3%3A%3Agrid3-nga-settlement-extents-v4-1/about)

* **Elevation:** SRTM GL1 Global 30 m, accessed through OpenTopography
  [SRTM GL1 30 m dataset](https://portal.opentopography.org/raster?jobId=rt1780001421000)

* **Coastline, lagoon and waterways:** OpenStreetMap, using the Nigeria extract from Geofabrik and clipping the required features to Eti-Osa
  [OpenStreetMap Nigeria data extract](https://download.geofabrik.de/africa/nigeria.html?utm_source=chatgpt.com)

* **Essential Infastructure**:  OpenStreetMap, using the Nigeria extract from Geofabrik and clipping the required features to Eti-Osa
  [OpenStreetMap Nigeria data extract](https://download.geofabrik.de/africa/nigeria.html?utm_source=chatgpt.com)


## What I would build

The project would start from a clear flood-exposure screening map of Eti-Osa showing settlement areas that meet both conditions: land below 5 metres elevation and location within 500 metres of the coast, lagoon or a mapped waterway to a geospatial platform to that examine potential flood exposure and access to essential services in Eti-Osa LGA, Lagos. The project will combine settlement, elevation, water, population, building and transport data with dated flood evidence where available.

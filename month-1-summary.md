# Month 1 Summary — Potential Flood Exposure Screening in Eti-Osa LGA

## Question
Which mapped settlement extents in Eti-Osa LGA fall within land that is both **≤ 5m elevation** and **within 500m of selected water bodies or waterways**?

## Spatial Operations
The analysis was carried out in **EPSG:32631 — WGS 84 / UTM zone 31N**.

Key operations included:

## Spatial Operations

The analysis was carried out in **EPSG:32631 — WGS 84 / UTM zone 31N**.

**Raster Calculator** — identify land at **≤ 5 m elevation**  
↓  
**Buffer** — create **500m proximity zones** around selected water bodies or waterway

↓  
**Merge & Dissolve** — combine the water-proximity zones  
↓  
**Intersection** — combine low elevation and water proximity to create the **potential flood-exposure zone**  
↓  
**Clip** — extract settlement extents falling within the potential flood-exposure zone

## Expected vs Actual Result
I expected potentially exposed settlement areas to be concentrated around the Atlantic coast, Lagos Lagoon, rivers, streams, canals and other low-lying areas.

The result broadly matched this expectation. out of **5,895 mapped settlement extents**, **2,264 (38.4%)** have some area within the potential flood-exposure zone.

## Result Checks
The result was checked by:

- visually comparing exposed areas with the source settlement and water layers;
- comparing feature counts before and after clipping;
- checking calculated settlement areas for reasonable values;
- inspecting one settlement feature manually against the exposure-zone boundary.

## What Surprised Me
Potential exposure was not limited to the coastline. some inland settlement areas also met both screening criteria because they are low-lying and close to mapped waterways or water bodies.

## Datasets Used
check [data-note.md](/doc/02-data-note.md)

## Data Still Needed
Further analysis would benefit from:

- observed or historical flood-event data;
- rainfall data;
- drainage-network and drainage-capacity data;
- population or building exposure data.

## Map Output
![Potential Flood-Exposed Settlement Areas in Eti-Osa LGA](/Maps/Potential_Flood_Exposed_Settlement_Map.png)

> **Note:** This is a screening analysis, not a flood prediction model. Potential exposure means that a settlement area meets the selected elevation and water-proximity criteria.
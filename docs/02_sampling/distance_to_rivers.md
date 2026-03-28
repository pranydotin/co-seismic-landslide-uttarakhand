# Distance to Rivers — Frequency Ratio Classification

## Overview
Proximity to river channels is a primary conditioning factor for landslide susceptibility. Rivers exert both mechanical and hydrological influence on adjacent slopes — through lateral erosion and undercutting of valley walls, elevated groundwater tables near channel banks, and increased saturation during flood events. The closer a slope is to a river channel, the greater its exposure to these destabilising processes.

## Data Description
- **Type:** Continuous raster
- **Unit:** Metres (m)
- **Source:** HydroRIVERS dataset
- **Processing:** River network filtered by stream order → clipped to study area → rasterised at 30 m → Euclidean distance computed
- **Resolution:** 30 m (EPSG:32644)
- **Tool:** `Raster → Analysis → Proximity (Raster Distance)` in QGIS

## Classification

Distance to rivers in the study area falls within a very short range (< 100 m), indicating dense drainage network coverage. Classes are defined using equal-interval breaks across this compressed range:

| Class | Range (m) | Proximity interpretation |
|-------|-----------|--------------------------|
| 1 | < 24.27 | Immediately adjacent — direct undercutting risk |
| 2 | 24.27 – 47.13 | Very close — high hydrological influence |
| 3 | 47.13 – 69.99 | Moderate proximity |
| 4 | 69.99 – 92.85 | Low proximity — reduced direct influence |
| 5 | ≥ 92.85 | Distant — minimal direct channel effect |

> Note: The narrow distance range (0–~100 m) reflects the high drainage density of the study area. Even small differences in proximity carry hydrological significance given the steep valley morphology.

## Raster Calculator Expression (QGIS)

```
("distance_from_rivers@1" < 24.27) * 1 +
("distance_from_rivers@1" >= 24.27 AND "distance_from_rivers@1" < 47.13) * 2 +
("distance_from_rivers@1" >= 47.13 AND "distance_from_rivers@1" < 69.99) * 3 +
("distance_from_rivers@1" >= 69.99 AND "distance_from_rivers@1" < 92.85) * 4 +
("distance_from_rivers@1" >= 92.85) * 5
```

## Output Settings
- **Output file:** `FR_dist_rivers.tif`
- **Data type:** Int16
- **Compression:** DEFLATE
- **Purpose:** Temporary — used only for LSI computation. Delete after non-landslide points are generated.

## Interpretation
Pixels in class 1 (< 24 m from a channel) are directly exposed to bank erosion, undercutting, and elevated water table effects — conditions strongly associated with landslide initiation. The influence diminishes with distance, with class 5 representing terrain largely decoupled from direct channel processes. The inverse relationship between distance and susceptibility is well-established in the literature.

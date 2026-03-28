# Distance to Roads — Frequency Ratio Classification

## Overview
Proximity to roads is one of the most consistent anthropogenic conditioning factors in landslide susceptibility assessment. Road construction in mountainous terrain involves slope cutting, removal of lateral support, disruption of natural drainage, and vegetation clearance — all of which reduce slope stability. The effect is most intense in the immediate vicinity of the road and diminishes with distance.

## Data Description
- **Type:** Continuous raster
- **Unit:** Metres (m)
- **Source:** OpenStreetMap (OSM)
- **Processing:** Relevant road classes filtered → clipped to study area → rasterised at 30 m → Euclidean distance computed
- **Resolution:** 30 m (EPSG:32644)
- **Tool:** `Raster → Analysis → Proximity (Raster Distance)` in QGIS

## Classification

Distance to roads was classified into 5 classes using threshold-based breaks that reflect known zones of anthropogenic influence on slope stability:

| Class | Range (m) | Influence zone |
|-------|-----------|----------------|
| 1 | < 500 | Immediate — direct cut-slope and drainage disruption |
| 2 | 500 – 1,000 | Near — significant construction influence |
| 3 | 1,000 – 2,000 | Moderate — reduced but measurable influence |
| 4 | 2,000 – 5,000 | Distant — marginal anthropogenic effect |
| 5 | ≥ 5,000 | Remote — negligible road influence |

## Raster Calculator Expression (QGIS)

```
("proximity_road@1" < 500) * 1 +
("proximity_road@1" >= 500  AND "proximity_road@1" < 1000) * 2 +
("proximity_road@1" >= 1000 AND "proximity_road@1" < 2000) * 3 +
("proximity_road@1" >= 2000 AND "proximity_road@1" < 5000) * 4 +
("proximity_road@1" >= 5000) * 5
```

## Output Settings
- **Output file:** `FR_dist_roads.tif`
- **Data type:** Int16
- **Compression:** DEFLATE
- **Purpose:** Temporary — used only for LSI computation. Delete after non-landslide points are generated.

## Interpretation
Class 1 (< 500 m) captures the zone of maximum anthropogenic disturbance — cut slopes, compacted fill, severed drainage, and destabilised natural slopes. Studies consistently report the highest landslide density within 500–1,000 m of roads in mountainous regions. Class 5 (> 5,000 m) represents natural terrain with minimal road-related modification, serving as a stable reference for absence point sampling.

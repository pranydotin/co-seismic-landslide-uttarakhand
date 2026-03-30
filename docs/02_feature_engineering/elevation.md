# Elevation — Factor Classification

## Overview

Elevation represents terrain height above sea level and is a composite proxy for a range of environmental controls on landslide occurrence — including temperature, precipitation regime, vegetation type, soil development, and the degree of tectonic uplift and erosional dissection. Although elevation itself does not directly trigger landslides, it co-varies strongly with conditions that do.

## Data Description

- **Type:** Continuous raster
- **Unit:** Metres (m)
- **Source:** SRTM DEM
- **Processing:** Mosaicked tiles → reprojected to EPSG:32644 → clipped to study area
- **Resolution:** 30 m

## Classification

Elevation was classified into 5 equal-interval classes based on the observed range within the study area:

| Class | Range (m)     | Terrain zone                             |
| ----- | ------------- | ---------------------------------------- |
| 1     | < 1,909       | Low elevation — valley floors, foothills |
| 2     | 1,909 – 3,818 | Mid elevation — transitional slopes      |
| 3     | 3,818 – 5,727 | High elevation — alpine terrain          |
| 4     | 5,727 – 7,637 | Very high — sub-nival zone               |
| 5     | ≥ 7,637       | Extreme elevation — glaciated peaks      |

## Raster Calculator Expression (QGIS)

```
("utm_Elevation@1" < 1909) * 1 +
("utm_Elevation@1" >= 1909 AND "utm_Elevation@1" < 3818) * 2 +
("utm_Elevation@1" >= 3818 AND "utm_Elevation@1" < 5727) * 3 +
("utm_Elevation@1" >= 5727 AND "utm_Elevation@1" < 7637) * 4 +
("utm_Elevation@1" >= 7637) * 5
```

## Output Settings

- **Output file:** `elevation_class.tif`
- **Data type:** Int16
- **Compression:** DEFLATE
- **Purpose:** Temporary — used only for LSI computation. Delete after non-landslide points are generated.

## Interpretation

Mid-elevation zones (classes 2–3) typically concentrate the highest landslide frequency in mountain regions — they coincide with the steepest gradients, highest precipitation, and most active erosion. Very high elevation zones (classes 4–5) are often glaciated or snow-covered and may show lower landslide density despite extreme relief. Actual FR scores are determined empirically from inventory overlap.

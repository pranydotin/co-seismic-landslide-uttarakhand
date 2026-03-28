# Terrain Ruggedness Index (TRI) — Frequency Ratio Classification

## Overview
The Terrain Ruggedness Index (TRI) quantifies the heterogeneity of the terrain surface by measuring the mean absolute difference in elevation between a focal cell and its eight neighbouring cells. It captures the complexity and roughness of the landscape, which is related to the degree of erosion, tectonic dissection, and slope instability.

## Data Description
- **Type:** Continuous raster
- **Derived from:** SRTM DEM
- **Resolution:** 30 m (EPSG:32644)

## Classification

TRI values are strongly right-skewed — the majority of pixels cluster at low values with a long tail toward rugged terrain. Break points reflect this distribution:

| Class | Range | Terrain description |
|-------|-------|---------------------|
| 1 | < 0.034 | Flat — near-zero local relief |
| 2 | 0.034 – 0.879 | Gently undulating |
| 3 | 0.879 – 6.154 | Moderately rugged |
| 4 | 6.154 – 9.448 | Highly rugged |
| 5 | ≥ 9.448 | Extremely rugged — dissected terrain |

## Raster Calculator Expression (QGIS)

```
("utm_Terrain Ruggedness Index@1" < 0.034) * 1 +
("utm_Terrain Ruggedness Index@1" >= 0.034 AND "utm_Terrain Ruggedness Index@1" < 0.879) * 2 +
("utm_Terrain Ruggedness Index@1" >= 0.879 AND "utm_Terrain Ruggedness Index@1" < 6.154) * 3 +
("utm_Terrain Ruggedness Index@1" >= 6.154 AND "utm_Terrain Ruggedness Index@1" < 9.448) * 4 +
("utm_Terrain Ruggedness Index@1" >= 9.448) * 5
```

## Output Settings
- **Output file:** `FR_tri.tif`
- **Data type:** Int16
- **Compression:** DEFLATE
- **Purpose:** Temporary — used only for LSI computation. Delete after non-landslide points are generated.

## Interpretation
Higher TRI classes reflect greater surface complexity, typically associated with steep and actively eroding slopes where landslides are more frequent. Flat terrain (class 1) is geomorphologically stable and represents ideal absence point territory.

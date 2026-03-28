# Sand Content — Frequency Ratio Classification

## Overview
Sand content governs soil drainage capacity and structural cohesion. Sandy soils drain rapidly but exhibit low inter-particle cohesion, making them susceptible to granular flow and shallow failure when slope angle is sufficient. Conversely, high sand content in otherwise fine-textured soils can create preferential flow paths that concentrate pore-water pressure.

## Data Description
- **Type:** Continuous raster
- **Unit:** Percentage (%)
- **Source:** HWSD2 (Harmonised World Soil Database v2)
- **Processing:** Depth-weighted average, 0–40 cm
- **Resolution:** 30 m (EPSG:32644)

## Classification

Sand was classified into 5 classes based on equal-interval breaks across the study area data range:

| Class | Range (%) | Description |
|-------|-----------|-------------|
| 1 | < 45 | Low sand — fine-textured soil dominant |
| 2 | 45 – 50 | Moderately low sand |
| 3 | 50 – 55 | Moderate sand content |
| 4 | 55 – 60 | Moderately high sand |
| 5 | ≥ 60 | High sand — loose structure, low cohesion |

## Raster Calculator Expression (QGIS)

```
("utm_sand_0_40@1" < 45) * 1 +
("utm_sand_0_40@1" >= 45 AND "utm_sand_0_40@1" < 50) * 2 +
("utm_sand_0_40@1" >= 50 AND "utm_sand_0_40@1" < 55) * 3 +
("utm_sand_0_40@1" >= 55 AND "utm_sand_0_40@1" < 60) * 4 +
("utm_sand_0_40@1" >= 60) * 5
```

## Output Settings
- **Output file:** `FR_sand.tif`
- **Data type:** Int16
- **Compression:** DEFLATE
- **Purpose:** Temporary — used only for LSI computation. Delete after non-landslide points are generated.

## Interpretation
Very high sand content (class 5) indicates loose, low-cohesion soils that are prone to granular failure on steeper slopes. The relationship between sand content and landslide frequency is best understood in combination with slope gradient and TWI, as drainage capacity interacts strongly with terrain position.

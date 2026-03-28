# NDVI — Frequency Ratio Classification

## Overview
The Normalised Difference Vegetation Index (NDVI) represents vegetation density and vigour. Vegetation plays a stabilising role on slopes through root reinforcement, interception of precipitation, and evapotranspiration-driven reduction of soil moisture. Areas with sparse or absent vegetation are more susceptible to surface erosion and mass movement.

## Data Description
- **Type:** Continuous raster
- **Range:** −1 to 1
- **Source:** Sentinel-2 (Bands B4 and B8)
- **Resolution:** 30 m (EPSG:32644)

## Classification

NDVI was classified into 6 classes reflecting vegetation density transitions:

| Class | Range | Vegetation description |
|-------|-------|------------------------|
| 1 | < 0 | Water bodies, bare rock, built-up — no vegetation |
| 2 | 0.0 – 0.2 | Very sparse vegetation |
| 3 | 0.2 – 0.4 | Low vegetation cover |
| 4 | 0.4 – 0.6 | Moderate vegetation cover |
| 5 | 0.6 – 0.8 | Dense vegetation cover |
| 6 | ≥ 0.8 | Very dense / closed canopy |

> Note: NDVI uses 6 classes (unlike the 5-class scheme applied to most other factors) to better resolve the gradient from bare surface to dense canopy, which has direct physical significance for slope stability.

## Raster Calculator Expression (QGIS)

```
("utm_NDVI_districts@1" < 0) * 1 +
("utm_NDVI_districts@1" >= 0   AND "utm_NDVI_districts@1" < 0.2) * 2 +
("utm_NDVI_districts@1" >= 0.2 AND "utm_NDVI_districts@1" < 0.4) * 3 +
("utm_NDVI_districts@1" >= 0.4 AND "utm_NDVI_districts@1" < 0.6) * 4 +
("utm_NDVI_districts@1" >= 0.6 AND "utm_NDVI_districts@1" < 0.8) * 5 +
("utm_NDVI_districts@1" >= 0.8) * 6
```

## Output Settings
- **Output file:** `FR_ndvi.tif`
- **Data type:** Int16
- **Compression:** DEFLATE
- **Purpose:** Temporary — used only for LSI computation. Delete after non-landslide points are generated.

## Interpretation
Lower NDVI classes (1–2) correspond to bare or sparsely vegetated surfaces with reduced root cohesion and higher erosion vulnerability, indicating elevated landslide susceptibility. Higher classes (5–6) represent well-vegetated stable slopes.

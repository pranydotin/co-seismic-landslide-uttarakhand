# Silt Content — Frequency Ratio Classification

## Overview
Silt content influences soil permeability, water retention, and susceptibility to liquefaction under saturated conditions. Silt-dominated soils have lower hydraulic conductivity than sandy soils, causing water to accumulate within the profile and elevate pore-water pressure — a primary driver of slope failure.

## Data Description
- **Type:** Continuous raster
- **Unit:** Percentage (%)
- **Source:** HWSD2 (Harmonised World Soil Database v2)
- **Processing:** Depth-weighted average, 0–40 cm
- **Resolution:** 30 m (EPSG:32644)

## Classification

Silt was classified into 5 classes based on equal-interval breaks across the study area data range:

| Class | Range (%) | Description |
|-------|-----------|-------------|
| 1 | < 20 | Low silt — predominantly sand/clay matrix |
| 2 | 20 – 25 | Moderately low silt |
| 3 | 25 – 30 | Moderate silt content |
| 4 | 30 – 35 | Moderately high silt |
| 5 | ≥ 35 | High silt — elevated water retention risk |

## Raster Calculator Expression (QGIS)

```
("utm_silt_0_40@1" < 20) * 1 +
("utm_silt_0_40@1" >= 20 AND "utm_silt_0_40@1" < 25) * 2 +
("utm_silt_0_40@1" >= 25 AND "utm_silt_0_40@1" < 30) * 3 +
("utm_silt_0_40@1" >= 30 AND "utm_silt_0_40@1" < 35) * 4 +
("utm_silt_0_40@1" >= 35) * 5
```

## Output Settings
- **Output file:** `FR_silt.tif`
- **Data type:** Int16
- **Compression:** DEFLATE
- **Purpose:** Temporary — used only for LSI computation. Delete after non-landslide points are generated.

## Interpretation
Higher silt content classes increase water retention within the soil profile, reducing drainage efficiency and promoting pore-water pressure build-up during rainfall events — conditions conducive to shallow translational landslides.

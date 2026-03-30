# Slope — Factor Classification

## Overview

Slope gradient is one of the most critical conditioning factors in landslide susceptibility assessment. It directly controls the gravitational shear stress acting on slope materials — steeper slopes generate higher downslope force, increasing the probability of mass movement initiation.

## Data Description

- **Type:** Continuous raster
- **Unit:** Radians (as derived from SRTM DEM)
- **Source:** SRTM DEM → QGIS terrain analysis
- **Resolution:** 30 m (EPSG:32644)

## Classification

Slope was classified into 5 classes based on geomorphological thresholds:

| Class | Range (radians) | Terrain description                         |
| ----- | --------------- | ------------------------------------------- |
| 1     | < 0.02          | Near-flat — negligible gravitational stress |
| 2     | 0.02 – 0.08     | Gentle slope — low instability              |
| 3     | 0.08 – 0.25     | Moderate slope — transitional zone          |
| 4     | 0.25 – 0.60     | Steep slope — elevated landslide risk       |
| 5     | ≥ 0.60          | Very steep — high gravitational stress      |

## Raster Calculator Expression (QGIS)

```
("utm_Slope@1" < 0.02) * 1 +
("utm_Slope@1" >= 0.02 AND "utm_Slope@1" < 0.08) * 2 +
("utm_Slope@1" >= 0.08 AND "utm_Slope@1" < 0.25) * 3 +
("utm_Slope@1" >= 0.25 AND "utm_Slope@1" < 0.6) * 4 +
("utm_Slope@1" >= 0.6) * 5
```

## Output Settings

- **Output file:** `slope_class.tif`
- **Data type:** Int16
- **Compression:** DEFLATE
- **Purpose:** Temporary — used only for LSI computation. Delete after non-landslide points are generated.

## Interpretation

Higher slope class → greater gravitational driving force → higher landslide susceptibility. Very flat areas (class 1) are considered stable reference zones and are preferentially used for absence point sampling.

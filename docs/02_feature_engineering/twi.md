# Topographic Wetness Index (TWI) — Factor Classification

## Overview

The Topographic Wetness Index (TWI) represents the tendency of each pixel to accumulate water based on its upslope contributing area and local slope gradient. It serves as a proxy for soil moisture distribution — a key control on pore-water pressure and thus on slope stability.

## Data Description

- **Type:** Continuous raster
- **Formula:** TWI = ln(a / tan β), where _a_ = specific catchment area, _β_ = slope angle
- **Derived from:** SRTM DEM → sink-filled → flow direction → flow accumulation → TWI
- **Resolution:** 30 m (EPSG:32644)

## Classification

TWI was classified into 5 classes using equal-interval breaks across the observed data range:

| Class | Range       | Hydrological interpretation         |
| ----- | ----------- | ----------------------------------- |
| 1     | < 5.5       | Dry — well-drained ridge positions  |
| 2     | 5.5 – 12.5  | Moderately dry                      |
| 3     | 12.5 – 19.5 | Moderate moisture accumulation      |
| 4     | 19.5 – 26.5 | High moisture — convergent terrain  |
| 5     | ≥ 26.5      | Very high — valley bottoms, hollows |

## Raster Calculator Expression (QGIS)

```
("utm_Topographic Wetness Index@1" < 5.5) * 1 +
("utm_Topographic Wetness Index@1" >= 5.5  AND "utm_Topographic Wetness Index@1" < 12.5) * 2 +
("utm_Topographic Wetness Index@1" >= 12.5 AND "utm_Topographic Wetness Index@1" < 19.5) * 3 +
("utm_Topographic Wetness Index@1" >= 19.5 AND "utm_Topographic Wetness Index@1" < 26.5) * 4 +
("utm_Topographic Wetness Index@1" >= 26.5) * 5
```

## Output Settings

- **Output file:** `twi_class.tif`
- **Data type:** Int16
- **Compression:** DEFLATE
- **Purpose:** Temporary — used only for LSI computation. Delete after non-landslide points are generated.

## Interpretation

High TWI classes (4–5) indicate terrain positions where water converges and saturates the soil column, increasing pore-water pressure and reducing effective shear strength — conditions directly associated with landslide initiation. Low TWI classes (1–2) represent dry, well-drained positions with lower susceptibility.

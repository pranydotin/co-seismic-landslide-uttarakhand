# Profile Curvature — Factor Classification

## Overview

Profile curvature measures the rate of change of slope gradient in the direction of maximum slope (i.e., along the flow path). It controls the acceleration or deceleration of water and debris moving downslope, with direct implications for erosion intensity and landslide initiation.

## Data Description

- **Type:** Continuous raster
- **Range:** Negative (concave) to positive (convex)
- **Derived from:** SRTM DEM
- **Resolution:** 30 m (EPSG:32644)

## Classification

Classification is centred on zero, with thresholds reflecting geomorphologically meaningful curvature transitions:

| Class | Range        | Geomorphological interpretation                          |
| ----- | ------------ | -------------------------------------------------------- |
| 1     | < −0.1       | Strongly concave — rapid flow acceleration, high erosion |
| 2     | −0.1 – −0.01 | Mildly concave — moderate flow acceleration              |
| 3     | −0.01 – 0.01 | Planar — linear flow, minimal acceleration               |
| 4     | 0.01 – 0.1   | Mildly convex — flow deceleration                        |
| 5     | ≥ 0.1        | Strongly convex — runoff dispersion, lower risk          |

## Raster Calculator Expression (QGIS)

```
("utm_Profile Curvature@1" < -0.1) * 1 +
("utm_Profile Curvature@1" >= -0.1  AND "utm_Profile Curvature@1" < -0.01) * 2 +
("utm_Profile Curvature@1" >= -0.01 AND "utm_Profile Curvature@1" < 0.01)  * 3 +
("utm_Profile Curvature@1" >= 0.01  AND "utm_Profile Curvature@1" < 0.1)   * 4 +
("utm_Profile Curvature@1" >= 0.1) * 5
```

> Note: The layer name contains a space — ensure `"utm_Profile Curvature@1"` is typed exactly as shown in the QGIS Raster Calculator.

## Output Settings

- **Output file:** `profile_curv_class.tif`
- **Data type:** Int16
- **Compression:** DEFLATE
- **Purpose:** Temporary — used only for LSI computation. Delete after non-landslide points are generated.

## Interpretation

Concave profiles (classes 1–2) accelerate downslope flow and concentrate runoff, promoting soil saturation and increasing shear stress along the failure plane. Convex profiles (classes 4–5) disperse flow and are associated with more stable terrain conditions.

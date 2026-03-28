# Plan Curvature — Frequency Ratio Classification

## Overview
Plan curvature measures the rate of change of aspect in the horizontal plane — perpendicular to the slope direction. It controls the lateral convergence or divergence of surface and subsurface flow, influencing soil moisture patterns and pore-water pressure distribution across the hillslope.

## Data Description
- **Type:** Continuous raster
- **Range:** Negative (convergent) to positive (divergent)
- **Derived from:** SRTM DEM
- **Resolution:** 30 m (EPSG:32644)

## Classification

Classification is centred on zero with wider break values than profile curvature, reflecting the larger magnitude range typical of plan curvature:

| Class | Range | Hydrological interpretation |
|-------|-------|-----------------------------|
| 1 | < −0.5 | Strongly concave — strong lateral flow convergence |
| 2 | −0.5 – −0.05 | Mildly concave — moderate convergence |
| 3 | −0.05 – 0.05 | Planar — uniform lateral flow |
| 4 | 0.05 – 0.5 | Mildly convex — moderate divergence |
| 5 | ≥ 0.5 | Strongly convex — strong lateral flow divergence |

## Raster Calculator Expression (QGIS)

```
("utm_Plan Curvature@1" < -0.5) * 1 +
("utm_Plan Curvature@1" >= -0.5  AND "utm_Plan Curvature@1" < -0.05) * 2 +
("utm_Plan Curvature@1" >= -0.05 AND "utm_Plan Curvature@1" < 0.05)  * 3 +
("utm_Plan Curvature@1" >= 0.05  AND "utm_Plan Curvature@1" < 0.5)   * 4 +
("utm_Plan Curvature@1" >= 0.5) * 5
```

> Note: The layer name contains a space — ensure `"utm_Plan Curvature@1"` is typed exactly as shown in the QGIS Raster Calculator.

## Output Settings
- **Output file:** `FR_plan_curv.tif`
- **Data type:** Int16
- **Compression:** DEFLATE
- **Purpose:** Temporary — used only for LSI computation. Delete after non-landslide points are generated.

## Interpretation
Strongly concave plan curvature (class 1) marks topographic hollows and swales where lateral subsurface flow converges, building up pore-water pressure and reducing effective soil cohesion — classic conditions for debris flow initiation. Divergent areas (classes 4–5) drain laterally and maintain lower moisture levels, representing more stable terrain.

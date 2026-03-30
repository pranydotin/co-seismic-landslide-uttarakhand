# Distance to Faults — Factor Classification

## Overview

Proximity to geological fault lines is a primary structural control on landslide susceptibility. Fault zones are characterised by fractured, brecciated, and weakened rock mass with reduced shear strength. Repeated tectonic displacement along fault planes produces a corridor of mechanically degraded material that is disproportionately prone to slope failure. Additionally, faults act as conduits for groundwater movement, further destabilising adjacent slopes through elevated pore-water pressure.

## Data Description

- **Type:** Continuous raster
- **Unit:** Metres (m)
- **Source:** NGDR (National Geoscience Data Repository)
- **Processing:** Fault lines loaded as GeoJSON → reprojected to EPSG:32644 → clipped to study area → rasterised (burn value = 1) → Euclidean distance computed
- **Resolution:** 30 m (EPSG:32644)
- **Tool:** `Raster → Analysis → Proximity (Raster Distance)` in QGIS

## Classification

Distance to faults was classified into 5 classes with progressively wider intervals reflecting the diminishing structural influence of fault zones with distance:

| Class | Range (m)      | Structural influence                               |
| ----- | -------------- | -------------------------------------------------- |
| 1     | < 1,000        | Immediate fault zone — heavily fractured rock mass |
| 2     | 1,000 – 2,000  | Near fault — significant structural weakening      |
| 3     | 2,000 – 5,000  | Moderate distance — reduced fracture density       |
| 4     | 5,000 – 10,000 | Distant — limited direct structural influence      |
| 5     | ≥ 10,000       | Remote — structurally intact bedrock               |

> Note: The wider intervals at greater distances (classes 3–5 span 3,000–5,000 m each) reflect the exponential decay of fault-related rock mass degradation with distance from the fault trace.

## Raster Calculator Expression (QGIS)

```
("proximity_fault_clipped@1" < 1000) * 1 +
("proximity_fault_clipped@1" >= 1000  AND "proximity_fault_clipped@1" < 2000)  * 2 +
("proximity_fault_clipped@1" >= 2000  AND "proximity_fault_clipped@1" < 5000)  * 3 +
("proximity_fault_clipped@1" >= 5000  AND "proximity_fault_clipped@1" < 10000) * 4 +
("proximity_fault_clipped@1" >= 10000) * 5
```

## Output Settings

- **Output file:** `fault_class.tif`
- **Data type:** Int16
- **Compression:** DEFLATE
- **Purpose:** Temporary — used only for LSI computation. Delete after non-landslide points are generated.

## Interpretation

Pixels in class 1 (< 1,000 m from a fault) lie within the primary damage zone where rock mass quality is severely degraded, joint density is high, and groundwater routing is concentrated. Landslide frequency is expected to be highest in this zone. Class 5 (> 10,000 m) represents structurally competent terrain well removed from tectonic discontinuities, making it appropriate for absence point sampling under the M3 strategy.

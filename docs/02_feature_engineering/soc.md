# Soil Organic Carbon (SOC) — Factor Classification (Initial Feature)

## Overview

Soil Organic Carbon (SOC) influences soil cohesion, aggregate stability, and water retention capacity. Soils with higher organic carbon content generally exhibit better structural integrity, while low-SOC soils tend to be more erodible and susceptible to failure under saturated conditions.

## Data Description

- **Type:** Continuous raster
- **Source:** HWSD2 (Harmonised World Soil Database v2)
- **Processing:** Depth-weighted average across 0–20 cm and 20–40 cm layers; share-weighted component aggregation
- **Resolution:** 30 m (EPSG:32644)

## Classification

SOC was classified into 5 classes using threshold-based breaks derived from the data distribution:

| Class | Range       | Soil stability implication            |
| ----- | ----------- | ------------------------------------- |
| 1     | < 1.45      | Very low SOC — poor cohesion          |
| 2     | 1.45 – 1.75 | Low SOC                               |
| 3     | 1.75 – 2.10 | Moderate SOC                          |
| 4     | 2.10 – 2.50 | High SOC                              |
| 5     | ≥ 2.50      | Very high SOC — strong soil structure |

## Raster Calculator Expression (QGIS)

```
("utm_soc_0_40@1" < 1.45) * 1 +
("utm_soc_0_40@1" >= 1.45 AND "utm_soc_0_40@1" < 1.75) * 2 +
("utm_soc_0_40@1" >= 1.75 AND "utm_soc_0_40@1" < 2.10) * 3 +
("utm_soc_0_40@1" >= 2.10 AND "utm_soc_0_40@1" < 2.50) * 4 +
("utm_soc_0_40@1" >= 2.50) * 5
```

## Output Settings

- **Output file:** `soc_class.tif`
- **Data type:** Int16
- **Compression:** DEFLATE
- **Purpose:** Intermediate — evaluated for use in LSI computation but excluded after Frequency Ratio (FR) analysis due to instability

## Interpretation

Lower SOC classes indicate degraded soils with reduced binding capacity, increasing susceptibility to erosion and shallow failure. Higher SOC classes generally correspond to more stable, well-structured soils, though this relationship may vary with local lithology and land use.

## Note on Feature Usage

Although this variable was derived and classified as part of the initial feature set, it was excluded from the final landslide susceptibility model.

Frequency Ratio (FR) analysis revealed unstable and physically unrealistic values, primarily due to highly skewed distributions and sparse landslide occurrences within certain classes. These effects were further amplified in high-altitude regions where soil properties are poorly represented or absent.

To ensure model robustness and avoid bias, this feature was not included in the final LSI computation. Soil conditions were instead represented using categorical soil mapping units (SMU).

# Clay Content — Factor Classification (Initial Feature)

## Overview

Clay content governs the plasticity, permeability, and shrink-swell behaviour of soil. High clay content reduces hydraulic conductivity, causing water to pond within the soil profile during rainfall and elevating pore-water pressure. When pore-water pressure exceeds the frictional resistance of the slope, shear failure occurs. Clay-rich soils are also prone to softening upon wetting, reducing residual shear strength over repeated wet-dry cycles.

## Data Description

- **Type:** Continuous raster
- **Unit:** Percentage (%)
- **Source:** HWSD2 (Harmonised World Soil Database v2)
- **Processing:** Depth-weighted average across 0–20 cm and 20–40 cm layers; share-weighted component aggregation per mapping unit
- **Resolution:** 30 m (EPSG:32644)

## Classification

Clay content in the study area falls within a narrow range (approximately 15–20%), reflecting relatively uniform soil texture. Classes are therefore defined with fine-interval breaks to resolve within-range variability:

| Class | Range (%)   | Description                                              |
| ----- | ----------- | -------------------------------------------------------- |
| 1     | < 15.5      | Low clay — higher drainage capacity                      |
| 2     | 15.5 – 16.8 | Moderately low clay                                      |
| 3     | 16.8 – 18.0 | Moderate clay content                                    |
| 4     | 18.0 – 19.5 | Moderately high clay                                     |
| 5     | ≥ 19.5      | High clay — elevated water retention and swell potential |

> Note: The narrow class intervals (1–1.5% per band) reflect the compressed data range in the study area. Despite the small absolute differences, these bands capture meaningful hydraulic contrasts in fine-textured soils.

## Raster Calculator Expression (QGIS)

```
("utm_clay_0_40@1" < 15.5) * 1 +
("utm_clay_0_40@1" >= 15.5 AND "utm_clay_0_40@1" < 16.8) * 2 +
("utm_clay_0_40@1" >= 16.8 AND "utm_clay_0_40@1" < 18.0) * 3 +
("utm_clay_0_40@1" >= 18.0 AND "utm_clay_0_40@1" < 19.5) * 4 +
("utm_clay_0_40@1" >= 19.5) * 5
```

## Output Settings

- **Output file:** `clay_class.tif`
- **Data type:** Int16
- **Compression:** DEFLATE
- **Purpose:** Intermediate — evaluated for use in LSI computation but excluded after Frequency Ratio (FR) analysis due to instability

## Interpretation

Higher clay classes (4–5) indicate soils with restricted drainage and elevated pore-water pressure potential during rainfall events, increasing susceptibility to shallow translational failures. The effect of clay is most pronounced when combined with steep slope gradients and high TWI values.

## Note on Feature Usage

Although this variable was derived and classified as part of the initial feature set, it was excluded from the final landslide susceptibility model.

Frequency Ratio (FR) analysis revealed unstable and physically unrealistic values, primarily due to highly skewed distributions and sparse landslide occurrences within certain classes. These effects were further amplified in high-altitude regions where soil properties are poorly represented or absent.

To ensure model robustness and avoid bias, this feature was not included in the final LSI computation. Soil conditions were instead represented using categorical soil mapping units (SMU).

# Soil Properties (HWSD2)

## Dataset Overview

Soil texture and organic carbon were derived from the **Harmonized World Soil Database v2 (HWSD2)** and initially considered as conditioning factors for landslide susceptibility analysis.

These variables describe the physical and chemical properties of soil that influence infiltration, drainage, and slope stability, which are important factors in landslide susceptibility.

---

## Data Source

- **Dataset:** Harmonized World Soil Database (HWSD2)
- **Provider:** FAO / IIASA
- **Format:** Microsoft Access Database (`.mdb`)

Tables used:

- HWSD2_SMU
- HWSD2_LAYERS

The spatial representation of soil mapping units was obtained from the HWSD2 SMU raster layer.

---

## Soil Database Structure

The HWSD2 dataset follows a hierarchical structure:

```text
Soil Mapping Unit (SMU)
    └── Soil Components
          └── Soil Layers
```

Each **mapping unit (SMU)** may contain multiple soil components.
Each component represents a soil type occupying a certain proportion of the mapping unit.

Each component contains several **depth layers**, such as:\
0–20 cm\
20–40 cm\
40–60 cm\
...

---

## Depth Selection

For this study, soil properties were derived for the **0–40 cm soil depth**.

The following layers were used:\
0–20 cm\
20–40 cm

These layers were combined to obtain a **depth-weighted average soil property for 0–40 cm**.

---

## Depth Weighted Aggregation

For each soil component, values from the two layers were combined using a depth-weighted mean.

$$
X_{0-40} =
\frac{(X_{0-20} \times 20) + (X_{20-40} \times 20)}{40}
$$

Where:

- $X_{0-20}$ = soil property at 0–20 cm
- $X_{20-40}$ = soil property at 20–40 cm

This produced a **component-level soil property for the 0–40 cm depth interval**.

---

## Mapping Unit Aggregation

Each soil component contributes to the mapping unit according to its **area share (`SHARE`)**.

The final mapping unit value was calculated as a **share-weighted average**.

$$
X_{SMU} =
\frac{\sum (X_i \times SHARE_i)}{\sum SHARE_i}
$$

Where:

- $X_i$ = component soil property
- $SHARE_i$ = percentage area of component within the mapping unit

This produced **one soil value per mapping unit**.

---

## Data Cleaning

The HWSD2 database uses placeholder values to represent missing data.

| Value | Meaning        |
| ----- | -------------- |
| -4    | Missing data   |
| -7    | Not applicable |

These values were replaced with **NaN** before aggregation to avoid bias in calculations.

---

## Glacier and Hard Rock Mask

In high elevation regions of the study area, large portions of the terrain consist of glaciers or exposed bedrock where soil is absent or extremely shallow.
Since soil properties such as clay, sand, silt, and organic carbon are not defined in these regions, a binary mask layer representing **glacier and hard rock areas** was created.

The mask raster was defined as:

| Value | Description                    |
| ----- | ------------------------------ |
| 0     | Soil present                   |
| 1     | Glacier or hard rock (no soil) |

The resulting raster layer was saved as: ` glacier_hardrock_mask.tif`

This layer identifies regions where soil parameters are not applicable and helps distinguish soil-covered terrain from areas dominated by ice or exposed bedrock.

## Raster Generation

The aggregated soil properties were joined to the **SMU polygon layer** and converted to raster format in QGIS.

Rasterization parameters:

- **Field used:** soil property
- **Resolution:** 0.008333° (~1 km)
- **Projection:** EPSG:4326

Generated raster layers:

- clay_0_40.tif
- sand_0_40.tif
- silt_0_40.tif
- soc_0_40.tif

---

## Validation

To ensure data consistency, the following condition was verified:

$$
Clay + Sand + Silt \approx 100\%
$$

This confirmed the integrity of the soil texture fractions after aggregation.

---

## Role in Study (Initial Consideration)

### Clay

_(Not used in final model; excluded after FR analysis)_

Clay content represents the proportion of fine soil particles.
Higher clay content generally reduces soil permeability and increases water retention.
Excess water accumulation can weaken soil structure and increase landslide susceptibility.

---

### Sand

_(Not used in final model; excluded after FR analysis)_

Sand represents the coarse fraction of soil particles.
Higher sand content typically increases soil permeability and drainage capacity.
However, sandy soils may have lower cohesion, which can influence slope stability under certain conditions.

---

### Silt

_(Not used in final model; excluded after FR analysis)_

Silt consists of medium-sized soil particles and contributes to soil structure and moisture retention.
High silt content can increase soil erodibility and reduce slope stability under saturated conditions.

---

### Soil Organic Carbon (SOC)

_(Not used in final model; excluded after FR analysis)_

Soil organic carbon reflects the amount of organic matter present in the soil.
Higher organic carbon levels improve soil aggregation and structure, which can enhance slope stability and reduce erosion.

## Feature Selection and Exclusion

Following the computation of Frequency Ratio (FR) values, soil property variables (clay, sand, silt, and soil organic carbon) exhibited unstable and physically unrealistic behavior.

In particular, certain classes produced extremely high FR values due to sparse landslide occurrences and highly skewed distributions. This instability arises from the sensitivity of FR to small denominator values and uneven class representation.

Additionally, in high-altitude regions of the study area, large portions of terrain consist of glaciers and exposed bedrock, where soil properties are either absent or poorly represented. This further reduces the reliability of continuous soil variables in the Himalayan context.

Due to these limitations, continuous soil properties were excluded from further analysis to improve model robustness and reduce bias in susceptibility estimation.

Instead, soil was represented using categorical soil mapping units (SMU) derived from the HWSD2 dataset, which provide a more stable and interpretable representation of soil conditions.

## Soil Type Representation (Final Variable)

To address the limitations of continuous soil properties, soil was represented using Soil Mapping Units (SMU) derived from the HWSD2 dataset.

Each SMU represents a composite soil unit consisting of multiple soil components and their proportional distribution within a mapping unit.

The SMU raster was used directly as a categorical variable, where each unique value corresponds to a distinct soil unit.

This representation provides:

- Stable class distribution
- Reduced sensitivity to sparse landslide occurrences
- Improved compatibility with Frequency Ratio (FR) analysis

Unlike continuous soil fractions, SMU-based representation captures integrated soil characteristics and is more suitable for heterogeneous mountainous terrain.

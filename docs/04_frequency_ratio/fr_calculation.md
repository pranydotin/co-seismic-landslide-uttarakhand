# Frequency Ratio (FR) Calculation

## Overview

The Frequency Ratio (FR) method is a bivariate statistical approach used to quantify the relationship between conditioning factor classes and landslide occurrence. In this study, FR is computed after excluding low-slope areas to ensure physically meaningful susceptibility modeling.

To improve statistical stability and prevent dominance of rare classes, FR values are clipped and log-transformed before generating the Landslide Susceptibility Index (LSI).

---

## Preprocessing Constraint (Slope Mask)

Landslides are unlikely to occur on very low slopes. Therefore, a slope threshold was applied:

$$Slope \ge 10\degree - 15\degree (\approx 0.17–0.26 \space radians)$$

- Pixels below this threshold were excluded from:
  - Landslide counts (N)
  - Total pixel counts (S)
- FR was computed only within this masked domain

---

## Formula

### Frequency Ratio

$$FR = \frac{n_i / N}{s_i / S}$$

| Symbol | Definition                              |
| ------ | --------------------------------------- |
| $n_i$  | Number of landslide points in class $i$ |
| $N$    | Total landslide points (masked domain)  |
| $s_i$  | Number of pixels in class $i$           |
| $S$    | Total pixels (masked domain)            |

**Interpretation:**

- `FR > 1` → class contributes to landslide occurrence above the area-weighted expectation → higher susceptibility
- `FR < 1` → class contributes below expectation → lower susceptibility
- `FR = 0` → no landslides recorded in this class

---

## FR Stabilization

To avoid instability from:

- rare classes (very small $s_i$)
- zero landslide classes

the following adjustments were applied:

### 1. Zero handling

$
FR = 0 \rightarrow  replaced \space with \space 0.01
$

### 2. Upper clipping

$
FR \leq 5
$

### 3. Log transformation

$
W_ij = \log(FR_i)
$

This transformation:

- Reduces skewness
- Prevents dominance of extreme values
- Enables additive combination across factors

---

### Raster Weighting and Alignment

Each classified raster was reclassified using its corresponding log(FR) weights to generate weighted rasters.

Since input rasters had varying spatial resolutions and extents, all rasters were resampled to a common grid (slope raster reference) using nearest-neighbor interpolation. This ensured:
- Consistent spatial resolution
- Proper pixel-wise summation
- Elimination of alignment errors

---

### Landslide Susceptibility Index (LSI)

The final susceptibility index is computed as:

$$LSI = \sum_{j=1}^{n} W_{ij}$$

where:
- $ W_{ij} = \log(FR_{ij}) $

The resulting LSI raster represents cumulative landslide susceptibility.

---

## Data Inputs

### 1. Landslide Points with Class Values

**File:** `landslide_points_sampled.csv`<br/>
Filtered using slope threshold


### 2. Class-wise Pixel Counts

**File:** `combined_pixels.csv`<br/>
Adjusted to exclude low-slope classes

---

## Steps

### Step 1 — Extract Pixel Counts (QGIS)

For each classified factor raster:

```
Processing Toolbox → Raster Analysis → Unique Values Report
```

Output fields: `value` (class), `count` (pixel count)
Saved as: `unique_values_<factor>_class.csv`

### Step 2 — Extract Landslide Class Values (QGIS)

For each classified factor raster:

```
Processing Toolbox → Raster Analysis → Sample Raster Values
```

Input: Landslide point layer + classified raster
Output: Point layer with class column appended
Final export: `landslide_points_sampled.csv`

### Step 3 — Aggregate Pixel Counts (Python)

Merge all 13 unique value CSVs into `combined_pixels.csv` with columns: `factor`, `class`, `Npix_i`

### Step 4 — Compute FR (Python)

```python
FR = (Nls_i / N) / (Npix_i / S)
```

- `LULC class 0` (background pixels) excluded
- FR values of `inf` or `NaN` replaced with `0`

**Output:** `FR_results_13features.csv`

---

## Key Results

| Factor              | High-FR Class     | FR   | Interpretation                                            |
| ------------------- | ----------------- | ---- | --------------------------------------------------------- |
| LULC — Shrubland    | Class 20          | 5.00 | Low root cohesion; degraded slopes; high erosion (capped) |
| LULC — Built-up     | Class 50          | 3.80 | Anthropogenic disturbance; slope cutting                  |
| Profile Curvature   | Class 3 (concave) | 3.73 | Flow convergence; pore pressure buildup                   |
| Plan Curvature      | Class 3 (concave) | 3.49 | Lateral flow convergence                                  |
| Proximity to Roads  | Class 1 (≤200m)   | 2.80 | Road cuts and slope destabilization                       |
| Elevation           | Class 1 (low)     | 2.61 | Valley zones; infrastructure concentration                |
| Proximity to Rivers | Class 1 (≤200m)   | 1.93 | Toe erosion and bank undercutting                         |
| TWI                 | Class 2           | 1.86 | Soil saturation and runoff concentration                  |
| Slope               | Class 3           | 1.68 | Optimal failure slope range                               |
| LULC — Grassland    | Class 30          | 1.52 | Moderate vegetation; limited root strength                |

> Note: Extremely high FR values for certain LULC classes were capped at 5 to prevent dominance caused by small-area class effects.

---

## LSI Map Generation

After FR computation, each classified factor raster was reclassified by its FR values using:

**QGIS** — `Raster Calculator`

```
W_slope + W_aspect + W_elevation + W_plan_curv +
W_profile_curv + W_twi + W_tri + W_ndvi + W_lulc +
W_proximity_roads + W_proximity_rivers + W_proximity_fault +
W_max_rainfall + W_mean_monsoon + W_mean_rainfall +
W_flow_accumulation
```

**Output:** `LSI_map.tif` — continuous surface of cumulative landslide susceptibility

---
### Classification of Susceptibility

The continuous LSI map was classified into five susceptibility zones using the Quantile classification method:

- Very Low
- Low
- Moderate
- High
- Very High

---

## Validation (ROC/AUC)

Model validation was performed using Receiver Operating Characteristic (ROC) analysis.

### Validation Procedure

- Landslide points were assigned label = 1
- Random non-landslide (pseudo-absence) points were assigned label = 0
- Non-landslide points were generated outside a 500 m buffer around known landslides
- LSI values were extracted using the QGIS “Sample Raster Values” tool
- Rows containing NoData values (masked low-slope areas) were removed

### ROC Computation

ROC analysis was performed in Python using:

```python
from sklearn.metrics import roc_curve, auc

fpr, tpr, _ = roc_curve(y_true, y_score)
roc_auc = auc(fpr, tpr)

print("AUC:", roc_auc)
```

### Result
The FR-based susceptibility model achieved
$AUC \approx 0.68$ indicating moderate predictive performance.

The result is consistent with the limitations of the bivariate FR approach, which does not account for interactions between conditioning factors.

---

### Interpretation of LSI Values

Higher positive LSI values indicate greater cumulative susceptibility, while strongly negative values correspond to relatively stable terrain conditions.

---

### Map Layout and Visualization

The final map was prepared using QGIS Print Layout with the following elements:

- Title: Landslide Susceptibility Map of Uttarakhand (FR Model)
- Legend: Categorized susceptibility classes
- Scale bar (kilometers)
- North arrow
- District boundaries with labels
- Annotation indicating slope-based masking


Low-slope regions $(\lt 10\degree - 15\degree)$ are intentionally displayed as blank areas to reflect exclusion from analysis.

---

### Key Observations
- High susceptibility zones are concentrated in:
    - Steep slopes
    - Concave terrain
    - Shrubland regions
    - Areas near roads and rivers
- Moderate zones represent transitional geomorphic conditions
- Low susceptibility zones correspond to:
    - Gentle slopes
    - Stable vegetation cover
    - Reduced geomorphic activity

The spatial distribution of susceptibility zones is generally consistent with known geomorphological characteristics of the Himalayan terrain.

---
## Output Files

| File                           | Description                               |
| ------------------------------ | ----------------------------------------- |
| `landslide_points_sampled.csv` | Landslide points with all class values    |
| `combined_pixels.csv`          | Class-wise pixel counts for all factors   |
| `FR_results_13features.csv`    | FR values for all 16 conditioning factors              |
| `FR_<factor>.tif`              | FR-reclassified raster per factor         |
| `LSI_map.tif`                  | Final LSI surface (sum of all FR rasters) |

---

## Notes

- Total study area pixels (S) derived from slope raster as it provides complete Uttarakhand coverage
- Soil type (SMU categorical) included as 13th factor replacing excluded soil percentage rasters
- LSI map subsequently classified into 5 similarity zones using Natural Breaks (Jenks) for non-landslide point selection

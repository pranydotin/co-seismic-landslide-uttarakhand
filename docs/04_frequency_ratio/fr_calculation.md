# Frequency Ratio (FR) Calculation

## Overview

The Frequency Ratio (FR) method is a bivariate statistical technique used to quantify the spatial association between each class of a conditioning factor and historical landslide occurrences. It forms the basis for computing the Landslide Susceptibility Index (LSI), which is subsequently used for similarity zoning and non-landslide point selection.

---

## Formula

### Frequency Ratio

$$FR = \frac{n_i / N}{s_i / S}$$

| Symbol | Definition | Source |
|--------|-----------|--------|
| $n_i$ | Number of landslide points in class $i$ of a factor | `landslide_points_sampled.csv` |
| $N$ | Total landslide points in study area = **16,019** | Landslide inventory |
| $s_i$ | Number of pixels in class $i$ of a factor | `combined_pixels.csv` |
| $S$ | Total pixels in study area = **66,499,208** | Slope raster (complete coverage) |

**Interpretation:**
- `FR > 1` → class contributes to landslide occurrence above the area-weighted expectation → higher susceptibility
- `FR < 1` → class contributes below expectation → lower susceptibility
- `FR = 0` → no landslides recorded in this class

---

### Landslide Susceptibility Index (LSI)

$$LSI = \sum_{j=1}^{n} FR_{ij}$$

where $FR_{ij}$ is the Frequency Ratio of class $i$ for factor $j$, summed across all $n$ conditioning factors per pixel.

The LSI produces a continuous surface representing cumulative landslide susceptibility based on all conditioning factors.

---

## Data Inputs

### 1. Landslide Points with Class Values
**File:** `landslide_points_sampled.csv`  
**Source:** QGIS — Sample Raster Values tool  
**Content:** 16,019 landslide points with class values for all 13 conditioning factors appended as columns

### 2. Class-wise Pixel Counts
**File:** `combined_pixels.csv`  
**Source:** QGIS — Unique Values Report tool → merged via Python  
**Columns:** `factor`, `class`, `Npix_i`

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

| Factor | High-FR Class | FR | Interpretation |
|--------|-------------|-----|----------------|
| Proximity to Roads | Class 1 (≤200m) | 2.49 | Strongest anthropogenic driver |
| LULC — Shrubland | Class 20 | 2.71 | Low root cohesion, high erosion risk |
| Profile Curvature — Concave | Class 2 | 2.60 | Water concentration increases pore pressure |
| Proximity to Rivers | Class 1 (≤200m) | 1.83 | Fluvial toe erosion |
| Elevation — Low | Class 1 | 1.72 | LHz geology + dense infrastructure |
| Proximity to Faults | Class 1 (≤200m) | 1.67 | Fractured rock mass |
| Slope — Steep | Class 4 (30–40°) | 1.56 | Near angle of repose |
| NDVI — Sparse | Class 3 | 1.53 | Transitional/degraded vegetation |

---

## LSI Map Generation

After FR computation, each classified factor raster was reclassified by its FR values using:

**QGIS** — `Raster Calculator`

```
FR_slope + FR_aspect + FR_elevation + FR_plan_curv +
FR_profile_curv + FR_twi + FR_tri + FR_ndvi + FR_lulc +
FR_soil_type + FR_proximity_roads + FR_proximity_rivers +
FR_proximity_fault
```

**Output:** `LSI_map.tif` — continuous surface of cumulative landslide susceptibility

---

## Output Files

| File | Description |
|------|-------------|
| `landslide_points_sampled.csv` | Landslide points with all class values |
| `combined_pixels.csv` | Class-wise pixel counts for all factors |
| `FR_results_13features.csv` | FR values for all 13 factors |
| `FR_<factor>.tif` | FR-reclassified raster per factor |
| `LSI_map.tif` | Final LSI surface (sum of all FR rasters) |

---

## Notes

- Total study area pixels (S) derived from slope raster as it provides complete Uttarakhand coverage
- Soil type (SMU categorical) included as 13th factor replacing excluded soil percentage rasters
- LSI map subsequently classified into 5 similarity zones using Natural Breaks (Jenks) for non-landslide point selection

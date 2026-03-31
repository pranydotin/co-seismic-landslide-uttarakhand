# Raster Classification of Conditioning Factors

## Overview

Each conditioning factor raster was classified into discrete classes prior to Frequency Ratio (FR) computation. Classification converts continuous raster values into meaningful categorical intervals that can be statistically associated with landslide occurrence.

All rasters were pre-processed to a uniform spatial resolution of **30 m × 30 m**, projected to **UTM Zone 44N (EPSG:32644)**, and clipped to the Uttarakhand state boundary before classification.

---

## Tool

**QGIS** — Reclassify by Table  
`Processing Toolbox → Raster Analysis → Reclassify by Table`

---

## Classification Schemes

### 1. Slope (degrees)

| Class | Range | Description |
|-------|-------|-------------|
| 1 | 0 – 10° | Flat to gentle |
| 2 | 10 – 20° | Moderate |
| 3 | 20 – 30° | Moderately steep |
| 4 | 30 – 40° | Steep |
| 5 | > 40° | Very steep |

---

### 2. Aspect (degrees)

| Class | Range | Direction |
|-------|-------|-----------|
| 1 | 0 – 45° | North |
| 2 | 45 – 90° | Northeast |
| 3 | 90 – 135° | East |
| 4 | 135 – 180° | Southeast |
| 5 | 180 – 225° | South |
| 6 | 225 – 270° | Southwest |
| 7 | 270 – 315° | West |
| 8 | 315 – 360° | Northwest |

---

### 3. Elevation (metres)

| Class | Range |
|-------|-------|
| 1 | 169 – 1000 m |
| 2 | 1000 – 2000 m |
| 3 | 2000 – 3000 m |
| 4 | 3000 – 4000 m |
| 5 | > 4000 m |

> Classified using Natural Breaks (Jenks) to reflect physiographic zones of Uttarakhand.

---

### 4. Plan Curvature

| Class | Range | Description |
|-------|-------|-------------|
| 1 | < -1.0 | Strongly concave |
| 2 | -1.0 – -0.5 | Slightly concave |
| 3 | -0.5 – 0.5 | Flat |
| 4 | 0.5 – 1.0 | Slightly convex |
| 5 | > 1.0 | Strongly convex |

---

### 5. Profile Curvature

| Class | Range | Description |
|-------|-------|-------------|
| 1 | < -1.0 | Strongly concave |
| 2 | -1.0 – -0.5 | Slightly concave |
| 3 | -0.5 – 0.5 | Flat |
| 4 | 0.5 – 1.0 | Slightly convex |
| 5 | > 1.0 | Strongly convex |

---

### 6. TWI (Topographic Wetness Index)

| Class | Range | Description |
|-------|-------|-------------|
| 1 | < 4.5 | Very low moisture accumulation |
| 2 | 4.5 – 5.8 | Low |
| 3 | 5.8 – 7.2 | Moderate |
| 4 | 7.2 – 8.8 | High |
| 5 | > 8.8 | Very high moisture accumulation |

---

### 7. TRI (Terrain Ruggedness Index)

| Class | Range | Description |
|-------|-------|-------------|
| 2 | 0 – 5 | Smooth terrain |
| 3 | 5 – 10 | Low ruggedness |
| 4 | 10 – 15 | Moderate ruggedness |
| 5 | > 15 | High ruggedness |

> Note: Class 1 absent in study area data.

---

### 8. NDVI

| Class | Range | Description |
|-------|-------|-------------|
| 1 | < 0.0 | Bare / water / snow |
| 2 | 0.0 – 0.1 | Very sparse vegetation |
| 3 | 0.1 – 0.2 | Sparse vegetation |
| 4 | 0.2 – 0.3 | Moderate vegetation |
| 5 | 0.3 – 0.4 | Dense vegetation |
| 6 | > 0.4 | Very dense vegetation |

---

### 9. LULC (ESA WorldCover)

LULC is a **categorical raster** — original ESA WorldCover class values are retained without reclassification.

| Class Value | Land Cover Type |
|-------------|----------------|
| 10 | Tree cover |
| 20 | Shrubland |
| 30 | Grassland |
| 40 | Cropland |
| 50 | Built-up |
| 60 | Bare / sparse vegetation |
| 70 | Snow and ice |
| 80 | Permanent water bodies |
| 90 | Herbaceous wetland |
| 100 | Moss and lichen |

---

### 10. Soil Type (FAO-HWSD)

Soil type is treated as a **categorical variable** using **Soil Mapping Unit (SMU)** codes from the FAO Harmonized World Soil Database (HWSD). Each SMU represents a composite soil unit consisting of multiple soil components and their proportional distribution within a mapping unit.

Original SMU codes are retained as class values — no reclassification applied.

> **Note on exclusion of soil percentage factors:** Continuous soil property rasters (clay %, sand %, silt %, and SOC) were excluded from analysis. Uttarakhand's extensive rocky, glaciated, and high-altitude barren terrain returns NoData for these variables, resulting in extremely small pixel counts per class and physically unrealistic FR values (e.g., sand class FR > 1000). The categorical SMU-based soil type raster provides complete spatial coverage and is scientifically appropriate for regional-scale LSA.

---

### 11. Distance to Roads (metres)

| Class | Range |
|-------|-------|
| 1 | 0 – 200 m |
| 2 | 200 – 400 m |
| 3 | 400 – 600 m |
| 4 | 600 – 800 m |
| 5 | > 800 m |

---

### 12. Distance to Rivers (metres)

| Class | Range |
|-------|-------|
| 1 | 0 – 200 m |
| 2 | 200 – 400 m |
| 3 | 400 – 600 m |
| 4 | 600 – 800 m |
| 5 | > 800 m |

---

### 13. Distance to Faults (metres)

| Class | Range |
|-------|-------|
| 1 | 0 – 200 m |
| 2 | 200 – 400 m |
| 3 | 400 – 600 m |
| 4 | 600 – 800 m |
| 5 | > 800 m |

---

## Output Files

All classified rasters saved as GeoTIFF with naming convention `<factor>_class.tif`:

| Factor | Output File |
|--------|-------------|
| Slope | `slope_class.tif` |
| Aspect | `aspect_class.tif` |
| Elevation | `elevation_class.tif` |
| Plan Curvature | `plan_curvature_class.tif` |
| Profile Curvature | `profile_curvature_class.tif` |
| TWI | `twi_class.tif` |
| TRI | `tri_class.tif` |
| NDVI | `ndvi_class.tif` |
| LULC | `lulc_class.tif` |
| Soil Type | `soil_type_class.tif` |
| Distance to Roads | `proximity_roads_class.tif` |
| Distance to Rivers | `proximity_rivers_class.tif` |
| Distance to Faults | `proximity_fault_class.tif` |

---

## Pixel Count Extraction and Aggregation

After classification, class-wise pixel counts were extracted from each raster and consolidated into a single dataset for use in FR computation.

### Step 1 — Extract Unique Values per Raster (QGIS)

For each classified raster:
```
Processing Toolbox → Raster Analysis → Unique Values Report
```

**Output fields:**
- `value` → raster class value
- `count` → number of pixels in that class

Each raster produced a CSV file named:
```
unique_values_<factor>_class.csv
```

Stored in: `data/interim/`

### Step 2 — Aggregate into Combined Dataset (Python)

All 13 CSV files were merged into a single structured dataset using a Python script:

- Read all CSV files from `data/interim/`
- Extracted factor name from each filename
- Standardized column names: `value` → `class`, `count` → `Npix_i`
- Added `factor` column to identify each conditioning variable
- Concatenated all into a single DataFrame

**Output:** `data/unique_value/combined_pixels.csv`

**Structure:**

| factor | class | Npix_i |
|--------|-------|--------|
| slope | 1 | 12,062,360 |
| slope | 2 | 9,885,811 |
| ndvi | 1 | 12,292,731 |
| lulc | 10 | 395,627,798 |
| ... | ... | ... |

**Total rows:** 89 (sum of classes across all 13 factors)

This file serves as the primary input for FR calculation alongside `landslide_points_sampled.csv`.

---

## Notes

- Continuous factors classified using equal interval or natural breaks as appropriate
- Categorical factors (LULC, Soil Type) retain original class values
- All outputs use **Int16** data type
- NoData value: **-9999**

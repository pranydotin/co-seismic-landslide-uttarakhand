# FR Reclassification of Conditioning Factor Rasters

## Overview

Each classified conditioning factor raster was reclassified by its corresponding Frequency Ratio (FR) values. This converts discrete class values into continuous FR weights, where each pixel receives the FR value of its class. The output rasters serve as direct inputs for LSI map generation.

---

## Tool

**Python** — `rasterio`, `numpy`, `pandas`
Script: `scripts/fr_reclassification.py`

---

## Input Files

| Input                                    | Description                                    |
| ---------------------------------------- | ---------------------------------------------- |
| `classified_rasters/<factor>.tif`        | Classified raster for each conditioning factor |
| `data/processed/FR_results_features.csv` | FR values per class per factor                 |

**FR CSV structure:**

| factor | class | Npix_i     | Nls_i | FR    |
| ------ | ----- | ---------- | ----- | ----- |
| slope  | 1     | 12,062,360 | 163   | 0.056 |
| slope  | 2     | 9,885,811  | 1,104 | 0.464 |
| ...    | ...   | ...        | ...   | ...   |

---

## Raster to Factor Mapping

| Raster Filename              | Factor Name (in FR CSV)  |
| ---------------------------- | ------------------------ |
| `slope_class.tif`            | `slope`                  |
| `utm_Aspect_class.tif`       | `utm_Aspect`             |
| `elevation_class.tif`        | `elevation`              |
| `plan_curv_class.tif`        | `plan_curv`              |
| `profile_curv_class.tif`     | `profile_curv`           |
| `twi_class.tif`              | `twi`                    |
| `tri_class.tif`              | `tri`                    |
| `ndvi_class.tif`             | `ndvi`                   |
| `utm_lulc.tif`               | `unique_values_utm_lulc` |
| `proximity_roads_class.tif`  | `proximity_roads`        |
| `proximity_rivers_class.tif` | `proximity_rivers`       |
| `proximity_fault_class.tif`  | `proximity_fault`        |
| `utm_soil_type.tif`          | `soil_class`             |

---

## Processing Logic

### Step 1 — Build FR Lookup

FR values loaded from `FR_results_features.csv` and structured as a nested dictionary mapping each factor's class values to their corresponding FR values.

### Step 2 — Block-wise Reclassification

Each raster is processed **block by block** using `rasterio.block_windows()` — critical for large rasters such as LULC (700M+ pixels) and Soil Type to avoid memory overflow.

For each block:

1. Read pixel values as float array
2. Identify unique class values excluding NoData
3. Map each class value to its FR value from the lookup dictionary
4. Classes absent from FR table assigned FR = 0.0
5. NoData pixels assigned output value = -9999

### Step 3 — Write Output

Output rasters written with LZW compression and 256 x 256 tiling for efficient storage and partial reads.

---

## Output Profile

| Parameter   | Value              |
| ----------- | ------------------ |
| dtype       | `float32`          |
| NoData      | `-9999`            |
| Compression | `LZW`              |
| Tiling      | `256 x 256` blocks |

---

## Output Files

Saved to: `layers/output_fr_rasters/`
Naming convention: `FR_<raster_name>.tif`

| Output File                     | Factor             |
| ------------------------------- | ------------------ |
| `FR_slope_class.tif`            | Slope              |
| `FR_utm_Aspect_class.tif`       | Aspect             |
| `FR_elevation_class.tif`        | Elevation          |
| `FR_plan_curv_class.tif`        | Plan Curvature     |
| `FR_profile_curv_class.tif`     | Profile Curvature  |
| `FR_twi_class.tif`              | TWI                |
| `FR_tri_class.tif`              | TRI                |
| `FR_ndvi_class.tif`             | NDVI               |
| `FR_utm_lulc.tif`               | LULC               |
| `FR_proximity_roads_class.tif`  | Distance to Roads  |
| `FR_proximity_rivers_class.tif` | Distance to Rivers |
| `FR_proximity_fault_class.tif`  | Distance to Faults |
| `FR_utm_soil_type.tif`          | Soil Type          |

---

## Notes

- Block-wise processing used throughout to handle large rasters without memory overflow
- LZW compression applied to reduce output file size
- Any class value absent from the FR table is assigned FR = 0.0
- 13 of 13 rasters successfully reclassified

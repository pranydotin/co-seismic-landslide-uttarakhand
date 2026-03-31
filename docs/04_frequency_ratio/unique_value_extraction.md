## Unique Value Extraction and Aggregation of Conditioning Factors

### Overview

This step involves generating class-wise pixel statistics for all conditioning factors required for Frequency Ratio (FR) modeling. Unique raster values and their corresponding pixel counts were extracted using QGIS and consolidated into a single structured dataset using Python.

---

### Input Data

A total of 16 classified conditioning factor rasters were used:

- Slope
- Aspect
- Elevation
- Plan Curvature
- Profile Curvature
- Flow Accumulation
- TWI (Topographic Wetness Index)
- TRI (Terrain Ruggedness Index)
- NDVI
- Land Use/Land Cover (LULC)
- Distance from Roads
- Distance from Rivers
- Distance from Faults
- Soil properties (Clay, Sand, Silt, SOC)

All raster layers:

- Were aligned spatially
- Had identical resolution and extent
- Were projected in UTM Zone 44N (EPSG:32644)

---

### Methodology

#### 1. Unique Value Extraction (QGIS)

Class-wise pixel counts were extracted using the **Unique Values Report** tool in QGIS:

**Tool Path:**
`Processing Toolbox → Raster analysis → Unique values report`

**Output Fields:**

- `value` → raster class
- `count` → number of pixels in each class

Each raster produced a CSV file with the naming convention:
`unique_values_<factor>_class.csv`

Examples:

```
unique_values_slope_class.csv
unique_values_ndvi_class.csv
unique_values_elevation_class.csv
```

---

#### 2. Data Storage

All generated CSV files were stored in:
_data/interim/_

These files represent intermediate outputs containing class-wise pixel distributions.

---

#### 3. Aggregation Using Python

A Python script (`combine_csv.py`) was used to merge all CSV files into a unified dataset.

**Processing Steps:**

- Read all CSV files from the directory
- Extract factor names from filenames
- Standardize column names (`value`, `count`)
- Rename columns:
  - `value` → `class`
  - `count` → `Npix_i`
- Add a new column `factor` indicating the conditioning variable
- Concatenate all data into a single DataFrame

---

### Output

The combined dataset was saved as: _data/unique_value/combined_pixels.csv_

**Structure:**

| factor | class | Npix_i |
| ------ | ----- | ------ |
| slope  | 1     | ...    |
| slope  | 2     | ...    |
| ndvi   | 1     | ...    |
| ...    | ...   | ...    |

---

### Purpose

This dataset provides:

- Class-wise pixel distribution for each conditioning factor
- Required input for computing Frequency Ratio (FR)
- A standardized structure for further statistical analysis

---

### Notes

- CSV files are intermediate outputs and can be regenerated from raster layers
- The aggregation process is automated to ensure reproducibility
- This step serves as a transition from GIS-based preprocessing to statistical modeling

---

### Next Step

The next stage involves:

- Extracting landslide pixel counts per class (`Nls_i`)
- Computing Frequency Ratio (FR) values

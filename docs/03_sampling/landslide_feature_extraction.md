## Landslide Feature Extraction from Raster Layers

### Overview

This step involves extracting conditioning factor values at known landslide locations to construct the feature set for the landslide class. Raster values from all conditioning layers are sampled at landslide point locations to generate a structured dataset for further analysis.

---

### Input Data

- **Landslide Inventory:** Point vector layer representing mapped landslide locations
- **Conditioning Factor Rasters (16 layers):**
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

All rasters:

- Share identical spatial resolution (30 m)
- Are aligned spatially
- Use the same coordinate reference system (EPSG:32644)

---

### Methodology

#### Tool Used

**Tool:** Sample Raster Values
**Access Path:** Processing Toolbox → Raster analysis → Sample raster values
**Software:** QGIS (Processing framework)

---

#### Procedure

- The landslide point layer is used as the input vector layer
- All conditioning factor rasters are provided as input raster layers
- Raster values are extracted at each landslide point location
- Each raster contributes one attribute field to the output

---

### Output

The output is a point layer with extracted raster values:

point_id | slope | aspect | elevation | ... | soc

Each row corresponds to a landslide point, and each column represents a conditioning factor value at that location.

---

### Purpose

This dataset serves as:

- The feature representation of the **landslide class (positive samples)**
- Input for subsequent modeling and analysis
- A structured dataset for comparison with non-landslide samples

---

### Notes

- This step is part of dataset construction and is independent of Frequency Ratio (FR) computation
- Accurate spatial alignment of raster layers is required to ensure correct value extraction
- Missing or null values should be handled appropriately before further analysis

---

### Next Step

Subsequent steps include:

- Preparation of class-wise raster statistics for Frequency Ratio (FR) computation
- Generation of a landslide susceptibility map
- Sampling of non-landslide points and extraction of corresponding raster values

# Pseudo-Absence Generation and ML Dataset Preparation

## Objective

The objective of this stage was to generate scientifically valid pseudo-absence (non-landslide) samples for machine learning-based landslide susceptibility modeling using the Frequency Ratio (FR)-derived Landslide Susceptibility Index (LSI) map.

---

# Step 1: Generate LSI Classes

The continuous LSI map generated from the FR model was reclassified into five susceptibility zones:

| Class | Susceptibility |
|---|---|
| 1 | Very Low |
| 2 | Low |
| 3 | Moderate |
| 4 | High |
| 5 | Very High |

The classification was performed in QGIS using:

```text
Layer Properties → Symbology → Quantile Classification
```

---

# Step 2: Create Low Susceptibility Mask

A raster mask representing low-risk regions was generated using Raster Calculator.

### Expression
```
("LSI_classes@1" = 1) OR ("LSI_classes@1" = 2)
```
This retained:

- Very Low susceptibility zones
- Low susceptibility zones

The output raster was saved as: ```low_lsi_mask.tif```

---

# Step 3: Generate Pseudo-Absence Points Using Python

Due to performance limitations caused by highly fragmented polygonized raster geometries in QGIS, pseudo-absence points were generated directly from the raster mask using Python.

The workflow included:

- reading the raster mask
- identifying valid low-susceptibility pixels
- random sampling of pixels
- conversion to geographic coordinates
- export as point geometries

The raster-based approach was computationally more efficient and avoided:

 Output file: ```pseudo_absence_points.gpkg```

---
# Step 4: Remove Points Near Landslides

To avoid generating pseudo-absence samples near known landslide locations, a 500 m exclusion buffer was created around landslide points in QGIS.

### Buffer Creation

QGIS Tool: ```Processing → Buffer```

Parameters:

- **Input**: Landslide points
- **Distance**: 500 meters
- **Dissolve result**: Enabled


 Output: ```landslide_buffer_500.gpkg```

---

# Step 5: Filter Pseudo-Absence Points

Pseudo-absence points located within the landslide buffer were removed using the QGIS "Extract by Location" tool.



QGIS Tool: ```Processing → Extract by Location```

Parameters:
| Parameter       | Value                 |
| --------------- | --------------------- |
| Input Layer     | pseudo_absence_points |
| Predicate       | disjoint              |
| Intersect Layer | landslide_buffer_500  |

 Output:
```
pseudo_absence_filtered.gpkg
```
This retained only pseudo-absence points:

- located in low susceptibility zones
- outside landslide influence regions
---

# Step 6: Extract Conditioning Factor Values

Raster predictor values were extracted for:

- landslide points
- pseudo-absence points

using **QGIS Tool**: ```Processing → Sample Raster Values```

Conditioning Factors Used:
| No. | Conditioning Factor   |
| --- | --------------------- |
| 1   | Slope                 |
| 2   | Aspect                |
| 3   | Elevation             |
| 4   | Plan Curvature        |
| 5   | Profile Curvature     |
| 6   | TWI                   |
| 7   | TRI                   |
| 8   | NDVI                  |
| 9   | LULC                  |
| 10  | Proximity to Roads    |
| 11  | Proximity to Rivers   |
| 12  | Proximity to Faults   |
| 13  | Maximum Rainfall      |
| 14  | Mean Monsoon Rainfall |
| 15  | Mean Rainfall         |
| 16  | Log Flow Accumulation |

### Important Note

Only original conditioning factor rasters were sampled.

The following layers were NOT used as ML predictors:

- FR weight rasters
- LSI raster
- classified rasters

This was done to prevent data leakage and model bias.

---
# Step 7: Assign Labels

The datasets were labeled as follows:
| Sample Type    | Label |
| -------------- | ----- |
| Landslide      | 1     |
| Pseudo-absence | 0     |
---

# Step 8: Export CSV Files

The sampled datasets were exported as:
```
landslide_ml.csv
pseudoabsence_ml.csv
```

---

# Step 9: Combine Datasets
Both datasets were merged to create the final machine learning dataset.

Output file: ```final_ml_dataset.csv```

This dataset contains:

- landslide samples
- pseudo-absence samples
- conditioning factor predictor values
- binary class labels

and is ready for:

- multicollinearity analysis (VIF)
- machine learning model training
- susceptibility prediction
- model validation
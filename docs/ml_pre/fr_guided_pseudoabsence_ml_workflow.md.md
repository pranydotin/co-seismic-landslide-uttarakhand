# FR-Guided Pseudo-Absence Generation and ML Dataset Preparation

## Objective

The objective of this stage was to generate pseudo-absence (non-landslide) samples for machine learning-based landslide susceptibility modelling using Frequency Ratio (FR)-derived susceptibility zones. Low susceptibility regions identified from the FR-based Landslide Susceptibility Index (LSI) map were considered environmentally stable terrain suitable for pseudo-absence generation.

---

# Step 1: Generate Landslide Susceptibility Classes

The continuous Landslide Susceptibility Index (LSI) raster generated from the Frequency Ratio model was classified into five susceptibility zones using Quantile Classification in QGIS.

## Susceptibility Classes

| Class | Susceptibility Zone |
|---|---|
| 1 | Very Low |
| 2 | Low |
| 3 | Moderate |
| 4 | High |
| 5 | Very High |

## QGIS Procedure

Layer Properties → Symbology → Quantile Classification

The classified raster was exported as:

LSI_classes.tif

---

# Step 2: Create Low Susceptibility Mask

A raster mask representing environmentally stable low-susceptibility terrain was generated using Raster Calculator.

## Raster Calculator Expression

("LSI_classes@1" = 1) OR ("LSI_classes@1" = 2)

The expression retained:

- Very Low susceptibility zones
- Low susceptibility zones

The resulting raster was saved as:

low_lsi_mask.tif

---

# Step 3: Generate Pseudo-Absence Points Using Python

Polygonization of the low susceptibility raster produced highly fragmented geometries that caused significant computational overhead during random point generation in QGIS. Therefore, pseudo-absence points were generated directly from raster pixels using Python.

## Raster-Based Sampling Workflow

The workflow included:

- reading the binary raster mask
- identifying valid low-susceptibility pixels
- random sampling of valid raster cells
- converting raster indices to geographic coordinates
- generating point geometries
- exporting the points as a GeoPackage vector layer

The raster-based approach was computationally efficient and avoided:

- polygon fragmentation issues
- excessive memory consumption
- QGIS random point generation failures

## Output

pseudo_absence_points.gpkg

---

# Step 4: Remove Points Near Known Landslides

To avoid generating pseudo-absence samples near known landslide locations, a 500 m exclusion buffer was created around all landslide points.

## QGIS Tool

Processing Toolbox → Buffer

## Parameters

| Parameter | Value |
|---|---|
| Input Layer | Landslide points |
| Buffer Distance | 500 m |
| Dissolve Result | Enabled |

## Output

landslide_buffer_500.gpkg

---

# Step 5: Filter Pseudo-Absence Points

Pseudo-absence points intersecting the landslide exclusion buffer were removed using spatial filtering.

## QGIS Tool

Processing Toolbox → Extract by Location

## Parameters

| Parameter | Value |
|---|---|
| Input Layer | pseudo_absence_points |
| Predicate | disjoint |
| Intersect Layer | landslide_buffer_500 |

## Output

pseudo_absence_filtered.gpkg

The resulting pseudo-absence points were therefore:

- located within FR-derived low susceptibility terrain
- spatially separated from known landslides
- environmentally stable according to FR susceptibility mapping

---

# Step 6: Extract Conditioning Factor Values

Raster predictor values were extracted for both:

- landslide points
- pseudo-absence points

using QGIS:

Processing Toolbox → Sample Raster Values

---

# Conditioning Factors Used

| No. | Conditioning Factor |
|---|---|
| 1 | Slope |
| 2 | Aspect |
| 3 | Elevation |
| 4 | Plan Curvature |
| 5 | Profile Curvature |
| 6 | Topographic Wetness Index (TWI) |
| 7 | Terrain Ruggedness Index (TRI) |
| 8 | NDVI |
| 9 | Land Use/Land Cover (LULC) |
| 10 | Proximity to Roads |
| 11 | Proximity to Rivers |
| 12 | Proximity to Faults |
| 13 | Maximum Rainfall |
| 14 | Mean Monsoon Rainfall |
| 15 | Mean Annual Rainfall |
| 16 | Log Flow Accumulation |

---

# Hydrological Feature Derivation

Flow accumulation exhibited strong positive skewness. Therefore, logarithmic transformation was applied prior to modelling:

FA_log = ln(FA + 1)

where:

- FA = raw flow accumulation
- FA_log = log-transformed flow accumulation

This transformation reduced the influence of extreme river-channel accumulation values and improved statistical stability.

---

# Important Note on Predictor Selection

Only original conditioning factor rasters were used as machine learning predictors.

The following layers were intentionally excluded:

- Frequency Ratio weight rasters
- Landslide Susceptibility Index (LSI) raster
- Classified susceptibility rasters

This was done to prevent:

- data leakage
- circular modelling
- artificially inflated predictive performance

---

# Step 7: Assign Binary Labels

The extracted datasets were assigned binary class labels:

| Sample Type | Label |
|---|---|
| Landslide | 1 |
| Pseudo-absence | 0 |

---

# Step 8: Export CSV Files

The sampled datasets were exported as CSV files:

- landslide_ml.csv
- pseudoabsence_ml.csv

---

# Step 9: Merge Datasets

Both datasets were merged to generate the final machine learning dataset.

## Output

final_ml_dataset.csv

The final dataset contained:

- landslide samples
- pseudo-absence samples
- extracted conditioning factor values
- binary class labels

and was subsequently used for:

- multicollinearity analysis (VIF)
- machine learning model development
- susceptibility prediction
- model validation
- comparative ML performance evaluation

---

# Methodological Limitation

FR-guided pseudo-absence sampling selects non-landslide samples exclusively from environmentally stable low-susceptibility terrain. This may increase class separability and produce optimistic model performance estimates, particularly for nonlinear ensemble methods such as Random Forest and XGBoost. Therefore, an additional environmentally constrained random pseudo-absence framework was also evaluated for comparative robustness assessment.
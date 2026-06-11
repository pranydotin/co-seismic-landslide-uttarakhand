# Environmentally Constrained Random Pseudo-Absence Generation and ML Dataset Preparation

## Objective

The objective of this stage was to generate environmentally realistic pseudo-absence samples for machine learning-based landslide susceptibility modelling using random sampling constrained by geomorphologically plausible mountainous terrain conditions.

Unlike FR-guided pseudo-absence generation, this framework avoided susceptibility-based sample selection to reduce artificial class separability and provide a more robust assessment of machine learning model generalization.

---

# Step 1: Generate Slope-Constrained Terrain Mask

A terrain suitability mask was generated from the slope raster to identify geomorphologically plausible landslide-prone mountainous terrain.

Because the slope raster was stored in radians, the threshold corresponding to 15° slope was converted as:

:contentReference[oaicite:0]{index=0}

## Raster Calculator Expression

if("utm_Slope@1" > 0.2618, 1, 0)

This retained terrain with:

- slope greater than 15°
- mountainous geomorphology
- physically realistic landslide terrain conditions

## Output

slope_mask_15deg.tif

---

# Step 2: Generate Random Pseudo-Absence Points Using Python

Direct polygon-based random point generation in QGIS produced computational limitations because mountainous terrain masks were highly fragmented. Therefore, pseudo-absence points were generated directly from raster pixels using Python.

## Raster-Based Sampling Workflow

The workflow included:

- reading the binary slope mask raster
- identifying valid mountainous terrain pixels
- random sampling of raster cells
- conversion of raster indices to spatial coordinates
- generation of point geometries
- export as GeoPackage vector layer

This approach was computationally efficient and avoided:

- polygon fragmentation issues
- excessive random point generation attempts
- QGIS memory limitations

## Output

pseudo_absence_points_v2.gpkg

---

# Step 3: Remove Points Near Known Landslides

To avoid sampling pseudo-absence points within landslide influence regions, a 500 m exclusion buffer was created around known landslide locations.

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

# Step 4: Filter Pseudo-Absence Points

Pseudo-absence points intersecting the landslide exclusion buffer were removed using spatial filtering.

## QGIS Tool

Processing Toolbox → Extract by Location

## Parameters

| Parameter | Value |
|---|---|
| Input Layer | pseudo_absence_points_v2 |
| Predicate | disjoint |
| Intersect Layer | landslide_buffer_500 |

## Output

pseudo_absence_filtered_v2.gpkg

The resulting pseudo-absence points were therefore:

- located in mountainous terrain
- outside known landslide influence zones
- randomly distributed across environmentally plausible terrain

---

# Step 5: Extract Conditioning Factor Values

Raster predictor values were extracted for:

- landslide points
- random pseudo-absence points

using:

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

# Hydrological Feature Transformation

Flow accumulation exhibited strong positive skewness. Therefore, logarithmic transformation was applied:

:contentReference[oaicite:1]{index=1}

This transformation reduced the influence of extreme accumulation values and improved statistical stability.

---

# Important Note on Predictor Selection

Only original conditioning factor rasters were used as machine learning predictors.

The following layers were excluded:

- FR weight rasters
- LSI raster
- classified susceptibility rasters

This prevented:

- data leakage
- circular prediction
- susceptibility-driven pseudo-label bias

---

# Step 6: Assign Binary Labels

Binary labels were assigned as follows:

| Sample Type | Label |
|---|---|
| Landslide | 1 |
| Pseudo-absence | 0 |

---

# Step 7: Export CSV Files

The sampled datasets were exported as:

- landslide_random_ml.csv
- pseudoabsence_random_ml.csv

---

# Step 8: Merge Datasets

Both datasets were merged to create the final machine learning dataset.

## Output

final_random_ml_dataset.csv

The final dataset contained:

- landslide samples
- environmentally constrained random pseudo-absence samples
- conditioning factor predictor values
- binary class labels

and was used for:

- multicollinearity analysis (VIF)
- machine learning model development
- susceptibility prediction
- ROC analysis
- comparative model evaluation

---

# Multicollinearity Analysis

Variance Inflation Factor (VIF) analysis was performed to identify highly collinear variables.

Hydrologically dependent variables exhibited strong multicollinearity, particularly:

- Flow Accumulation
- TWI
- Rainfall variables

TWI was computed as:

:contentReference[oaicite:2]{index=2}

where:

- A_s = specific catchment area
- β = local slope angle

Because TWI is mathematically dependent on flow accumulation and slope, high multicollinearity was expected.

Iterative VIF-based feature elimination was therefore performed.

Final retained predictors were:

- Aspect
- Elevation
- Slope
- Plan Curvature
- Profile Curvature
- TRI
- NDVI
- LULC
- Proximity to Roads
- Proximity to Rivers
- Proximity to Faults
- Maximum Rainfall

---

# Methodological Significance

Compared with FR-guided pseudo-absence sampling, environmentally constrained random pseudo-absence sampling produced:

- lower but more realistic predictive performance
- reduced susceptibility-space separability
- improved robustness of machine learning evaluation

This framework therefore provided a more conservative and scientifically defensible assessment of landslide susceptibility prediction performance.
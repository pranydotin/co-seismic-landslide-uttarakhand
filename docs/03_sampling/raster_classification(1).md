# Raster Classification of Conditioning Factors

## Overview

Each conditioning factor raster was classified into discrete classes using QGIS Raster Calculator. Break values were determined by inspecting the unique value distribution of each raster, ensuring meaningful and data-driven class boundaries. All rasters were pre-processed to a uniform spatial resolution of **30 m × 30 m**, projected to **UTM Zone 44N (EPSG:32644)**, and clipped to the Uttarakhand state boundary before classification.

---

## Tool

**QGIS** — Raster Calculator
`Raster → Raster Calculator`

---

## Excluded Soil Variables

All soil-related rasters were excluded from classification and LSI computation:

| Variable                 | Reason for Exclusion                                                                                    |
| ------------------------ | ------------------------------------------------------------------------------------------------------- |
| Clay (%)                 | NoData over rocky/glaciated terrain — FR unreliable                                                     |
| Sand (%)                 | NoData over rocky/glaciated terrain — FR unreliable                                                     |
| Silt (%)                 | NoData over rocky/glaciated terrain — FR unreliable                                                     |
| SOC                      | NoData over rocky/glaciated terrain — FR unreliable                                                     |
| Soil Type (FAO-HWSD SMU) | Only 0.11% spatial coverage (71,836 / 66,499,208 pixels) — FR values up to 1598, physically unrealistic |

> All soil variables were excluded for the same reason: extensive rocky, glaciated, and high-altitude barren terrain in Uttarakhand's Higher and Tethys Himalayan zones returns NoData for soil datasets, producing extremely small class pixel counts and physically unrealistic FR values.

---

## Final Factor List (16 conditioning factors)

| #   | Factor                  | Input Raster                         | Output File                   | Classes |
| --- | ----------------------- | ------------------------------------ | ----------------------------- | ------- |
| 1   | NDVI                    | `utm_ndvi`                           | `ndvi_class.tif`              | 2       |
| 2   | Elevation               | `utm_Elevation`                      | `elevation_class.tif`         | 4       |
| 3   | Plan Curvature          | `utm_Plan Curvature`                 | `plan_curv_class.tif`         | 5       |
| 4   | Profile Curvature       | `utm_Profile Curvature`              | `profile_curv_class.tif`      | 5       |
| 5   | Distance to Faults      | `proximity_faults`                   | `proximity_fault_class.tif`   | 4       |
| 6   | Distance to Rivers      | `proximity_river`                    | `proximity_rivers_class.tif`  | 4       |
| 7   | Distance to Roads       | `proximity_roads`                    | `proximity_roads_class.tif`   | 4       |
| 8   | Slope                   | `utm_Slope`                          | `slope_class.tif`             | 4       |
| 9   | TRI                     | `utm_Terrain Ruggedness Index (TRI)` | `tri_class.tif`               | 4       |
| 10  | TWI                     | `utm_Topographic Wetness Index`      | `twi_class.tif`               | 4       |
| 11  | Aspect                  | `utm_Aspect`                         | `aspect_class.tif`            | 8       |
| 12  | LULC                    | `utm_lulc`                           | `lulc_class.tif`              | 10      |
| 13  | Flow Accumulation (log) | `log_flow_accumulation`              | `flow_accumulation_class.tif` | 4       |
| 14  | Mean Rainfall           | `mean_rainfall`                      | `mean_rainfall_class.tif`     | 4       |
| 15  | Monsoon Rainfall        | `monsoon_rainfall`                   | `monsoon_rainfall_class.tif`  | 4       |
| 16  | Max Rainfall            | `max_rainfall`                       | `max_rainfall_class.tif`      | 4       |

---

## Classification Expressions

### 1. NDVI

Break values derived from unique value distribution. Classified into 2 classes reflecting the dominant vegetation threshold in Uttarakhand terrain.

| Class | Range    | Description                |
| ----- | -------- | -------------------------- |
| 1     | < 0.2869 | Low to moderate vegetation |
| 2     | ≥ 0.2869 | Dense vegetation           |

```
("utm_ndvi@1" < 0.2868992) * 1 +
("utm_ndvi@1" >= 0.2868992) * 2
```

---

### 2. Elevation (metres)

Classified into 4 classes using Natural Breaks reflecting Uttarakhand's physiographic zones.

| Class | Range (m)   | Description                                     |
| ----- | ----------- | ----------------------------------------------- |
| 1     | < 959.98    | Low elevation — Tarai / Sub-Himalayan           |
| 2     | 960 – 1705  | Mid elevation — Lesser Himalayan foothills      |
| 3     | 1705 – 3393 | High elevation — Lesser / Higher Himalayan      |
| 4     | ≥ 3393      | Very high elevation — Higher / Tethys Himalayan |

```
("utm_Elevation@1" < 959.9829879) * 1 +
("utm_Elevation@1" >= 959.9829879 AND "utm_Elevation@1" < 1705.002051) * 2 +
("utm_Elevation@1" >= 1705.002051 AND "utm_Elevation@1" < 3393.1317645) * 3 +
("utm_Elevation@1" >= 3393.1317645) * 4
```

---

### 3. Plan Curvature

Classified into 5 classes capturing the full range from strongly concave to strongly convex. Controls lateral water flow convergence and divergence.

| Class | Range             | Description                         |
| ----- | ----------------- | ----------------------------------- |
| 1     | < -0.0055         | Strongly concave — flow convergence |
| 2     | -0.0055 – -0.0013 | Slightly concave                    |
| 3     | -0.0013 – 0.0012  | Flat / planar                       |
| 4     | 0.0012 – 0.0053   | Slightly convex                     |
| 5     | ≥ 0.0053          | Strongly convex — flow divergence   |

```
("utm_Plan Curvature@1" < -0.0054812) * 1 +
("utm_Plan Curvature@1" >= -0.0054812 AND "utm_Plan Curvature@1" < -0.0013229) * 2 +
("utm_Plan Curvature@1" >= -0.0013229 AND "utm_Plan Curvature@1" < 0.0011721) * 3 +
("utm_Plan Curvature@1" >= 0.0011721 AND "utm_Plan Curvature@1" < 0.0053305) * 4 +
("utm_Plan Curvature@1" >= 0.0053305) * 5
```

---

### 4. Profile Curvature

Classified into 5 classes. Controls flow acceleration/deceleration along slope direction and influences erosion and deposition.

| Class | Range             | Description                          |
| ----- | ----------------- | ------------------------------------ |
| 1     | < -0.0014         | Strongly concave — flow acceleration |
| 2     | -0.0014 – -0.0003 | Slightly concave                     |
| 3     | -0.0003 – 0.0002  | Flat / linear                        |
| 4     | 0.0002 – 0.0012   | Slightly convex                      |
| 5     | ≥ 0.0012          | Strongly convex — flow deceleration  |

```
("utm_Profile Curvature@1" < -0.0013666) * 1 +
("utm_Profile Curvature@1" >= -0.0013666 AND "utm_Profile Curvature@1" < -0.0003258) * 2 +
("utm_Profile Curvature@1" >= -0.0003258 AND "utm_Profile Curvature@1" < 0.0001859) * 3 +
("utm_Profile Curvature@1" >= 0.0001859 AND "utm_Profile Curvature@1" < 0.0012425) * 4 +
("utm_Profile Curvature@1" >= 0.0012425) * 5
```

---

### 5. Distance to Faults (metres)

Classified into 4 classes with progressively wider intervals reflecting the exponential decay of fault-related structural weakening with distance. Fault zones are characterised by fractured, brecciated rock mass with reduced shear strength and elevated pore-water pressure.

| Class | Range (m)     | Structural Influence                               |
| ----- | ------------- | -------------------------------------------------- |
| 1     | < 1,351       | Immediate fault zone — heavily fractured rock mass |
| 2     | 1,351 – 3,248 | Near fault — significant structural weakening      |
| 3     | 3,248 – 7,127 | Moderate distance — reduced fracture density       |
| 4     | ≥ 7,127       | Remote — structurally intact bedrock               |

```
("proximity_faults@1" < 1351.332472) * 1 +
("proximity_faults@1" >= 1351.332472 AND "proximity_faults@1" < 3247.7620122) * 2 +
("proximity_faults@1" >= 3247.7620122 AND "proximity_faults@1" < 7126.9394988) * 3 +
("proximity_faults@1" >= 7126.9394988) * 4
```

---

### 6. Distance to Rivers (metres)

Classified into 4 classes. Proximity to rivers captures fluvial undercutting of slope toes and elevated soil moisture, both of which reduce slope stability.

| Class | Range (m)     | Influence                                       |
| ----- | ------------- | ----------------------------------------------- |
| 1     | < 14.87       | Immediate riverbank — active toe erosion        |
| 2     | 14.87 – 32.00 | Near river — elevated moisture and erosion risk |
| 3     | 32.00 – 53.34 | Moderate distance                               |
| 4     | ≥ 53.34       | Distant — limited direct fluvial influence      |

```
("proximity_river@1" < 14.8660769) * 1 +
("proximity_river@1" >= 14.8660769 AND "proximity_river@1" < 31.9999882) * 2 +
("proximity_river@1" >= 31.9999882 AND "proximity_river@1" < 53.3385374) * 3 +
("proximity_river@1" >= 53.3385374) * 4
```

---

### 7. Distance to Roads (metres)

Classified into 4 classes. Road construction is a primary anthropogenic driver of slope instability in Uttarakhand through slope cutting, drainage disruption, and increased loading.

| Class | Range (m)   | Anthropogenic Influence                  |
| ----- | ----------- | ---------------------------------------- |
| 1     | < 247       | Immediate road zone — active disturbance |
| 2     | 247 – 953   | Near road — moderate disturbance         |
| 3     | 953 – 4,062 | Transitional zone                        |
| 4     | ≥ 4,062     | Remote — minimal road influence          |

```
("proximity_roads@1" < 247.3827321) * 1 +
("proximity_roads@1" >= 247.3827321 AND "proximity_roads@1" < 953.420733) * 2 +
("proximity_roads@1" >= 953.420733 AND "proximity_roads@1" < 4061.5347923) * 3 +
("proximity_roads@1" >= 4061.5347923) * 4
```

---

### 8. Slope (radians)

Classified into 4 classes. Note: slope values are in **radians** from the source DEM processing.

| Class | Range (rad)     | Approx. Degrees | Description |
| ----- | --------------- | --------------- | ----------- |
| 1     | < 0.2094        | < 12°           | Gentle      |
| 2     | 0.2094 – 0.4287 | 12° – 24.6°     | Moderate    |
| 3     | 0.4287 – 0.5979 | 24.6° – 34.2°   | Steep       |
| 4     | ≥ 0.5979        | ≥ 34.2°         | Very steep  |

```
("utm_Slope@1" < 0.2093987) * 1 +
("utm_Slope@1" >= 0.2093987 AND "utm_Slope@1" < 0.4287241) * 2 +
("utm_Slope@1" >= 0.4287241 AND "utm_Slope@1" < 0.5979172) * 3 +
("utm_Slope@1" >= 0.5979172) * 4
```

---

### 9. TRI — Terrain Ruggedness Index

Classified into 4 classes capturing terrain complexity from smooth to highly rugged.

| Class | Range          | Description         |
| ----- | -------------- | ------------------- |
| 1     | < 4.167        | Smooth terrain      |
| 2     | 4.167 – 8.454  | Low ruggedness      |
| 3     | 8.454 – 12.491 | Moderate ruggedness |
| 4     | ≥ 12.491       | High ruggedness     |

```
("utm_Terrain Ruggedness Index (TRI)@1" < 4.1671596) * 1 +
("utm_Terrain Ruggedness Index (TRI)@1" >= 4.1671596 AND "utm_Terrain Ruggedness Index (TRI)@1" < 8.4544103) * 2 +
("utm_Terrain Ruggedness Index (TRI)@1" >= 8.4544103 AND "utm_Terrain Ruggedness Index (TRI)@1" < 12.4908041) * 3 +
("utm_Terrain Ruggedness Index (TRI)@1" >= 12.4908041) * 4
```

---

### 10. TWI — Topographic Wetness Index

Classified into 4 classes reflecting soil moisture accumulation potential.

| Class | Range         | Description                       |
| ----- | ------------- | --------------------------------- |
| 1     | < 5.494       | Low moisture accumulation         |
| 2     | 5.494 – 6.448 | Moderate                          |
| 3     | 6.448 – 7.987 | High moisture accumulation        |
| 4     | ≥ 7.987       | Very high — convergent flow zones |

```
("utm_Topographic Wetness Index@1" < 5.4938805) * 1 +
("utm_Topographic Wetness Index@1" >= 5.4938805 AND "utm_Topographic Wetness Index@1" < 6.4477251) * 2 +
("utm_Topographic Wetness Index@1" >= 6.4477251 AND "utm_Topographic Wetness Index@1" < 7.9874802) * 3 +
("utm_Topographic Wetness Index@1" >= 7.9874802) * 4
```

---

### 11. Flow Accumulation (log-transformed)

Flow accumulation represents upstream contributing area and surface runoff concentration. Due to skewness in the data, a logarithmic transformation was applied prior to classification

`$ln("utm_Flow Accumulation@1" + 1)$`

Classified into 4 classes based on quantile breaks applied to the log-transformed raster

| Class | Range (log scale) | Description                      |
| ----- | ----------------- | -------------------------------- |
| 1     | $ \lt 8.062$      | Very low flow — ridges / divides |
| 2     | $8.062 – 8.894$   | Low accumulation                 |
| 3     | $8.894 – 10.034$  | Moderate accumulation            |
| 4     | $\ge10.034$       | High accumulation — channels     |

```
("log_flow_accumulation@1" < 8.0623724) * 1 +
("log_flow_accumulation@1" >= 8.0623724 AND "log_flow_accumulation@1" < 8.8943169) * 2 +
("log_flow_accumulation@1" >= 8.8943169 AND "log_flow_accumulation@1" < 10.0338558) * 3 +
("log_flow_accumulation@1" >= 10.0338558) * 4
```

---

### 12. Aspect

Categorical raster — classified into 8 directional classes representing slope orientation. Aspect influences solar radiation, moisture retention, and vegetation type, all of which indirectly affect slope stability.

| Class | Range (°) | Direction |
| ----- | --------- | --------- |
| 1     | 0 – 45    | North     |
| 2     | 45 – 90   | Northeast |
| 3     | 90 – 135  | East      |
| 4     | 135 – 180 | Southeast |
| 5     | 180 – 225 | South     |
| 6     | 225 – 270 | Southwest |
| 7     | 270 – 315 | West      |
| 8     | 315 – 360 | Northwest |

---

### 13. LULC — Land Use / Land Cover

Categorical raster — ESA WorldCover 2022 class values retained as-is. No reclassification applied.

| Class Value | Land Cover Type          |
| ----------- | ------------------------ |
| 10          | Tree cover               |
| 20          | Shrubland                |
| 30          | Grassland                |
| 40          | Cropland                 |
| 50          | Built-up                 |
| 60          | Bare / sparse vegetation |
| 70          | Snow and ice             |
| 80          | Permanent water bodies   |
| 90          | Herbaceous wetland       |
| 100         | Moss and lichen          |

---

### 14. Mean Rainfall

Classified into 4 classes representing increasing average precipitation intensity.

| Class | Range (mm)  | Direction          |
| ----- | ----------- | ------------------ |
| 1     | $ \lt 100 $ | Low rainfall       |
| 2     | $100 - 150$ | Moderate rainfall  |
| 3     | $150 – 200$ | High rainfall      |
| 4     | $ \ge 200 $ | Very high rainfall |

```
("mean_rainfall@1" < 100) * 1 +
("mean_rainfall@1" >= 100 AND "mean_rainfall@1" < 150) * 2 +
("mean_rainfall@1" >= 150 AND "mean_rainfall@1" < 200) * 3 +
("mean_rainfall@1" >= 200) * 4
```

---

### 15. Monsoon Rainfall

Captures seasonal concentration of rainfall (critical for landslide triggering in Himalayas).

| Class | Range (mm)  | Direction        |
| ----- | ----------- | ---------------- |
| 1     | $ \lt 200 $ | Weak monsoon     |
| 2     | $200 - 350$ | Moderate monsoon |
| 3     | $350 – 500$ | Strong monsoon   |
| 4     | $ \ge 500 $ | Extreme monsoon  |

```
("monsoon_rainfall@1" < 200) * 1 +
("monsoon_rainfall@1" >= 200 AND "monsoon_rainfall@1" < 350) * 2 +
("monsoon_rainfall@1" >= 350 AND "monsoon_rainfall@1" < 500) * 3 +
("monsoon_rainfall@1" >= 500) * 4
```

---

### 16. Maximum Rainfall

Represents extreme rainfall events (important for slope failure thresholds).

| Class | Range (mm)   | Direction                                     |
| ----- | ------------ | --------------------------------------------- |
| 1     | $ \lt 400 $  | Low intensity events                          |
| 2     | $400 - 800$  | Moderate extreme rainfall                     |
| 3     | $800 – 1200$ | High intensity events — potential instability |
| 4     | $ \ge 1200 $ | Extreme rainfall — high failure probability   |

```
("max_rainfall@1" < 400) * 1 +
("max_rainfall@1" >= 400 AND "max_rainfall@1" < 800) * 2 +
("max_rainfall@1" >= 800 AND "max_rainfall@1" < 1200) * 3 +
("max_rainfall@1" >= 1200) * 4
```

---

## Output Settings

| Parameter   | Value                     |
| ----------- | ------------------------- |
| Data type   | Int16                     |
| Compression | DEFLATE                   |
| NoData      | -9999                     |
| CRS         | EPSG:32644 (UTM Zone 44N) |
| Resolution  | 30 m × 30 m               |

---

## Pixel Count Extraction and Aggregation

After classification, class-wise pixel counts were extracted from each raster for use in FR computation.

### Step 1 — Extract Unique Values per Raster (QGIS)

```
Processing Toolbox → Raster Analysis → Unique Values Report
```

Output fields: `value` (class), `count` (pixel count)
Saved as: `unique_values_<factor>_class.csv` in `data/interim/`

### Step 2 — Aggregate into Combined Dataset (Python)

All CSV files merged into a single structured dataset.

**Output:** `data/unique_value/combined_pixels.csv`

| factor | class | Npix_i     |
| ------ | ----- | ---------- |
| slope  | 1     | 12,062,360 |
| ndvi   | 1     | ...        |
| ...    | ...   | ...        |

This file is the primary input for FR calculation alongside `landslide_points_sampled.csv`.

---

## Notes

- Break values for continuous factors derived from unique value inspection in QGIS — not arbitrary fixed intervals
- Categorical factors (Aspect, LULC) retain original class values without reclassification
- Slope values are in **radians** — class boundaries reflect radian thresholds, not degrees
- This file supersedes all individual factor classification MD files

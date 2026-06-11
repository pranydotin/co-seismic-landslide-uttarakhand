# Machine Learning Dataset Preparation and Initial Modelling

---

# 1. Final Machine Learning Dataset Preparation

The final machine learning dataset was prepared by combining landslide samples (`label = 1`) and pseudo-absence samples (`label = 0`) extracted from the conditioning factor rasters.

The merged dataset initially contained:
- inventory metadata,
- descriptive textual attributes,
- administrative information,
- spatial identifiers,
- raster-derived conditioning factors.

Only raster-derived predictor variables relevant to landslide susceptibility modelling were retained for machine learning analysis.

---

# 2. Selected Conditioning Factors

The following conditioning factors were retained as independent predictor variables:

| Predictor Variable |
|---|
| ASPECT_11 |
| ELEVATION_11 |
| SLOPE_11 |
| PLAN_CURV_11 |
| PROFILE_CURV_11 |
| TWI_11 |
| TRI_11 |
| NDVI_11 |
| LULC_11 |
| PROXIMITY_ROADS_11 |
| PROXIMITY_RIVERS_11 |
| PROXIMITY_FAULTS_11 |
| MAX_RAINFALL_11 |
| MEAN_RAINFALL_11 |
| MONSOON_RAINFALL_11 |
| FLOW_ACC_11 |

The target variable used for supervised classification was:

| Variable | Meaning |
|---|---|
| label | 1 = landslide, 0 = non-landslide |

---

# 3. Removal of Non-Predictive Variables

The following categories of variables were removed from the machine learning dataset:
- landslide inventory metadata,
- textual descriptions,
- administrative attributes,
- geometry fields,
- event information,
- latitude/longitude coordinates,
- unique identifiers.

Examples include:
- gid,
- slide_no,
- latitude,
- longitude,
- abstract,
- district,
- village,
- slide_name,
- fid.

Latitude and longitude were intentionally excluded to avoid spatial leakage and location memorization during model training.

---

# 4. Missing Value Handling

Missing values were identified primarily within:
- rainfall rasters,
- proximity fault raster.

Rows containing missing raster values were removed from the dataset.

Final missing-value statistics:

| Variable | Missing Values |
|---|---:|
| PROXIMITY_FAULTS_11 | 1 |
| MAX_RAINFALL_11 | 235 |
| MEAN_RAINFALL_11 | 235 |
| MONSOON_RAINFALL_11 | 129 |

After removing missing records, the final cleaned dataset contained:

| Dataset Property | Value |
|---|---:|
| Total Samples | 30,421 |
| Predictor Variables | 16 |
| Landslide Samples | 15,913 |
| Non-Landslide Samples | 14,508 |

The dataset exhibited near-balanced class distribution suitable for supervised binary classification.

---

# 5. Variance Inflation Factor (VIF) Analysis

Variance Inflation Factor (VIF) analysis was performed to assess multicollinearity among predictor variables prior to machine learning modelling.

The VIF for each predictor was computed using:

```python
variance_inflation_factor()
```

The general threshold adopted was:

```text
VIF > 10
```

indicating severe multicollinearity.

---

# 6. Initial VIF Results

The initial VIF analysis revealed severe multicollinearity among:
- rainfall-derived variables,
- hydrological variables.

Initial high-VIF variables included:

| Variable | Initial VIF |
|---|---:|
| FLOW_ACC_11 | 482.90 |
| MONSOON_RAINFALL_11 | 481.55 |
| MEAN_RAINFALL_11 | 216.06 |
| MAX_RAINFALL_11 | 136.52 |
| TWI_11 | 13.03 |
| ELEVATION_11 | 12.54 |

The extreme VIF values resulted primarily from:
- strong redundancy among rainfall variables,
- mathematical dependence between TWI and flow accumulation.

TWI is computed as:

$$ TWI = \ln \left(\frac{A_s}{\tan \beta}\right)$$

\[
TWI = \ln\left(\frac{A_s}{\tan \beta}\right)
\]


where:
- $A_s$ = specific catchment area,
- $\beta$ = local slope angle.

---

# 7. Iterative Multicollinearity Reduction

An iterative VIF reduction workflow was implemented.

The following variables were sequentially removed:

| Removed Variable | Reason |
|---|---|
| FLOW_ACC_11 | redundancy with TWI |
| MEAN_RAINFALL_11 | redundancy with monsoon rainfall |
| MAX_RAINFALL_11 | redundancy with monsoon rainfall |

Although `ELEVATION_11` exhibited a VIF value slightly greater than 10 $(VIF \approx  12.5)$, it was retained because elevation is a geomorphologically fundamental terrain variable and comparative modelling demonstrated improved predictive performance when elevation was included.



---

# 8. Final Predictor Set After VIF Reduction

The final predictor variables retained for machine learning modelling were:

| Final Predictors |
|---|
| ASPECT_11 |
| ELEVATION_11 |
| SLOPE_11 |
| PLAN_CURV_11 |
| PROFILE_CURV_11 |
| TWI_11 |
| TRI_11 |
| NDVI_11 |
| LULC_11 |
| PROXIMITY_ROADS_11 |
| PROXIMITY_RIVERS_11 |
| PROXIMITY_FAULTS_11 |
| MONSOON_RAINFALL_11 |

Final VIF values were considered acceptable for machine learning modelling.

---

# 9. Train–Validation–Test Split

The cleaned machine learning dataset was divided using stratified random sampling to preserve class balance.

The dataset split configuration was:

| Subset | Samples | Percentage |
|---|---:|---:|
| Training Set | 18,252 | 60% |
| Validation Set | 6,084 | 20% |
| Testing Set | 6,085 | 20% |

The subsets were used as follows:

| Subset | Purpose |
|---|---|
| Training | model fitting |
| Validation | model evaluation and tuning |
| Testing | final independent assessment |

---

# 10. Feature Standardization

Feature standardization was applied using:

```python
StandardScaler()
```

Standardization was performed only for:
- Logistic Regression,
- Support Vector Machine (SVM),

because these algorithms are sensitive to feature scaling.

Tree-based algorithms:
- Random Forest,
- XGBoost,

were trained using unscaled predictor variables because tree models are scale-invariant.

---

# 11. Baseline Machine Learning Models

The following baseline machine learning models were initially evaluated:

| Model |
|---|
| Logistic Regression |
| Random Forest |
| Support Vector Machine (SVM) |
| XGBoost |

Model evaluation metrics included:
- Accuracy,
- Precision,
- Recall,
- F1-score,
- ROC-AUC,
- confusion matrix,
- classification report.

ROC curves were generated for comparative model assessment.

---

# 12. Initial Model Performance

## Logistic Regression

| Metric | Value |
|---|---:|
| Accuracy | 0.900 |
| Precision | 0.878 |
| Recall | 0.941 |
| F1-score | 0.908 |
| ROC-AUC | 0.963 |

## Support Vector Machine (SVM)

| Metric | Value |
|---|---:|
| Accuracy | 0.922 |
| Precision | 0.905 |
| Recall | 0.951 |
| F1-score | 0.927 |
| ROC-AUC | 0.973 |

Both Logistic Regression and SVM substantially outperformed the Frequency Ratio model $(FR AUC \approx 0.68)$ indicating that machine learning models captured nonlinear interactions and complex predictor relationships more effectively than the bivariate FR approach.

---

# 13. Detection of Potential Optimistic Bias

Tree-based ensemble models produced near-perfect validation performance:

| Model | ROC-AUC |
|---|---:|
| Random Forest | 1.000 |
| XGBoost | 1.000 |

with perfect confusion matrices and classification metrics.

This behaviour suggested possible:
- optimistic bias,
- residual spatial autocorrelation,
- overly separable pseudo-absence sampling.

The pseudo-absence samples had been generated from:
- Very Low and Low susceptibility zones derived from the FR susceptibility map.

Consequently, non-landslide samples originated predominantly from terrain already characterized as low susceptibility, which may have artificially simplified the classification problem for tree-based models.

---

# 14. Methodological Refinement

To address potential optimistic bias, an improved pseudo-absence sampling strategy was proposed.

The refined strategy involves:
1. excluding known landslide locations,
2. excluding 500 m landslide buffers,
3. constraining sampling to mountainous terrain,
4. restricting sampling to slopes greater than 15°,
5. avoiding FR- or LSI-guided susceptibility zones during pseudo-absence generation.

This environmentally constrained pseudo-absence strategy is expected to produce more realistic and robust machine learning evaluation results.
import pandas as pd

# ── 1. Load both files ──────────────────────────────────────────────────────
pixels_df = pd.read_csv('./data/processed/combined_pixels.csv')
lands_df = pd.read_csv('./data/processed/landslide_points_sampled.csv',
                       low_memory=False)

# ── 2. Keep only 12 valid features (remove soil properties) ─────────────────
# Removed: clay, sand, silt_soil, soc_soil (unreliable - rocky/glacier areas)

col_to_factor = {
    'slope_class1': 'slope',
    'aspect_class1': 'utm_Aspect',
    'elevation_class1': 'elevation',
    'plan_curvature_class1': 'plan_curv',
    'profile_curvature_class1': 'profile_curv',
    'twi_class1': 'twi',
    'tri_class1': 'tri',
    'ndvi_class1': 'ndvi',
    'lulc_class1': 'unique_values_utm_lulc',
    'proximity_roads_class': 'proximity_roads',
    'proximity_rivers_class': 'proximity_rivers',
    'proximity_fault_class': 'proximity_fault',
    'soil_type1': 'soil_type'
}

# ── 3. Constants ─────────────────────────────────────────────────────────────
N = len(lands_df)
# Use slope as reference for total pixels (most complete coverage)
S = pixels_df[pixels_df['factor'] == 'slope']['Npix_i'].sum()

print(f"Total landslide points   (N): {N:,}")
print(f"Total study area pixels  (S): {S:,}")
print(f"Features used: {len(col_to_factor)}\n")

# ── 4. Calculate FR for each factor ──────────────────────────────────────────
all_results = []

for col, factor in col_to_factor.items():

    # --- ni: landslide count per class ---
    ni = (lands_df[col]
          .value_counts()
          .rename_axis('class')
          .reset_index(name='Nls_i'))
    ni['class'] = ni['class'].astype(float)

    # --- si: pixel count per class ---
    si = pixels_df[pixels_df['factor'] == factor][['class', 'Npix_i']].copy()
    si['class'] = si['class'].astype(float)

    # --- merge ---
    merged = si.merge(ni, on='class', how='left')
    merged['Nls_i'] = merged['Nls_i'].fillna(0)

    # --- FR calculation ---
    merged['factor'] = factor
    merged['N'] = N
    merged['S'] = S
    merged['FR'] = (merged['Nls_i'] / N) / (merged['Npix_i'] / S)

    # Replace inf/nan with 0
    merged['FR'] = merged['FR'].replace([float('inf'), float('nan')], 0)

    all_results.append(merged)

# ── 5. Combine all results ────────────────────────────────────────────────────
fr_df = pd.concat(all_results, ignore_index=True)
fr_df = fr_df[['factor', 'class', 'Npix_i', 'Nls_i', 'N', 'S', 'FR']]
fr_df = fr_df.sort_values(['factor', 'class']).reset_index(drop=True)

# ── 6. Save ───────────────────────────────────────────────────────────────────
fr_df.to_csv('./data/processed/FR_results_features.csv', index=False)

# ── 7. Print summary ──────────────────────────────────────────────────────────
print("=" * 55)
print("         FR RESULTS — 12 FEATURES")
print("=" * 55)

for factor in fr_df['factor'].unique():
    sub = fr_df[fr_df['factor'] == factor][['class', 'Npix_i', 'Nls_i', 'FR']]
    print(f"\n--- {factor} ---")
    print(sub.to_string(index=False))

print("\n Saved: FR_results_12features.csv")

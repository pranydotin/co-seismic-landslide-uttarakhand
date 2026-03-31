import os
import numpy as np
import pandas as pd
import rasterio
from rasterio.transform import from_origin


input_folder = "/mnt/d/My Drive/cosesmic/layers/classified_rasters"

# Folder where FR rasters and LSI map will be saved (will be created if needed)
output_folder = "/mnt/d/My Drive/cosesmic/layers/output_fr_rasters"

# Path to your FR results CSV
fr_csv_path = "./data/processed/FR_results_features.csv"

# ── RASTER FILENAME TO FACTOR NAME MAPPING ───────────────────────────────────
# Left  = your actual raster filename (without .tif)
# Right = factor name exactly as it appears in FR_results_features.csv

raster_to_factor = {
    "slope_class": "slope",
    "utm_Aspect_class": "utm_Aspect",
    "elevation_class": "elevation",
    "plan_curv_class": "plan_curv",
    "profile_curv_class": "profile_curv",
    "twi_class": "twi",
    "tri_class": "tri",
    "ndvi_class": "ndvi",
    "utm_lulc": "unique_values_utm_lulc",
    "proximity_roads_class": "proximity_roads",
    "proximity_rivers_class": "proximity_rivers",
    "proximity_fault_class": "proximity_fault",
    "utm_soil_type": "soil_class"
}

# ── MAIN SCRIPT — NO CHANGES NEEDED BELOW THIS LINE ─────────────────────────

os.makedirs(output_folder, exist_ok=True)

# Load FR table
fr_df = pd.read_csv(fr_csv_path)
print(f"✅ Loaded FR table: {len(fr_df)} rows\n")

# Build lookup: {factor: {class_value: FR_value}}
fr_lookup = {}
for factor, group in fr_df.groupby("factor"):
    fr_lookup[factor] = dict(zip(group["class"].astype(float), group["FR"]))

print("FR lookup built for factors:")
for k in fr_lookup:
    print(f"   {k}: {len(fr_lookup[k])} classes")
print()

# ── STEP 1: Reclassify each raster ───────────────────────────────────────────
fr_raster_paths = []

for raster_name, factor in raster_to_factor.items():

    input_path = os.path.join(input_folder, raster_name + ".tif")
    output_path = os.path.join(output_folder, f"FR_{raster_name}.tif")

    if not os.path.exists(input_path):
        print(f"⚠️  WARNING: File not found — {input_path}")
        print(f"   Check your raster_to_factor mapping for '{raster_name}'")
        continue

    if factor not in fr_lookup:
        print(
            f"⚠️  WARNING: Factor '{factor}' not found in FR table — skipping {raster_name}")
        continue

    class_to_fr = fr_lookup[factor]

    with rasterio.open(input_path) as src:
        data = src.read(1).astype(float)
        profile = src.profile.copy()
        nodata = src.nodata if src.nodata is not None else -9999

    # Create output array filled with 0
    fr_array = np.zeros_like(data, dtype=np.float32)

    # Replace each class value with its FR value
    unique_classes = np.unique(data[data != nodata])
    for cls in unique_classes:
        fr_val = class_to_fr.get(float(cls), 0.0)
        fr_array[data == cls] = fr_val

    # Keep NoData as NoData
    fr_array[data == nodata] = -9999

    # Save reclassified raster
    profile.update(dtype=rasterio.float32, nodata=-9999)

    with rasterio.open(output_path, "w", **profile) as dst:
        dst.write(fr_array, 1)

    fr_raster_paths.append(output_path)
    print(f"✅ Reclassified: {raster_name} → FR_{raster_name}.tif")

print(f"\n✅ {len(fr_raster_paths)} / {len(raster_to_factor)} rasters reclassified\n")

# ── STEP 2: Sum all FR rasters → LSI map ─────────────────────────────────────
if len(fr_raster_paths) == 0:
    print("❌ No rasters to sum — check warnings above")
else:
    print("Generating LSI map by summing all FR rasters...")

    # Read first raster to get shape and profile
    with rasterio.open(fr_raster_paths[0]) as src:
        lsi = np.zeros(src.shape, dtype=np.float32)
        valid = np.ones(src.shape, dtype=bool)
        profile = src.profile.copy()

    # Sum all FR rasters (only where all are valid)
    for path in fr_raster_paths:
        with rasterio.open(path) as src:
            data = src.read(1).astype(np.float32)
            nodata = src.nodata if src.nodata is not None else -9999
            mask = data == nodata
            valid &= ~mask
            data[mask] = 0
            lsi += data

    # Set NoData where any raster had NoData
    lsi[~valid] = -9999

    # Save LSI map
    lsi_path = os.path.join(output_folder, "LSI_map.tif")
    profile.update(dtype=rasterio.float32, nodata=-9999)

    with rasterio.open(lsi_path, "w", **profile) as dst:
        dst.write(lsi, 1)

    # Print LSI statistics (excluding NoData)
    lsi_valid = lsi[valid]
    print(f"\n✅ LSI map saved: LSI_map.tif")
    print(f"   Min LSI  : {lsi_valid.min():.4f}")
    print(f"   Max LSI  : {lsi_valid.max():.4f}")
    print(f"   Mean LSI : {lsi_valid.mean():.4f}")
    print(f"   Std LSI  : {lsi_valid.std():.4f}")

    print("\n🎉 Done! Output files in:", output_folder)
    print("   Next step: Load LSI_map.tif in QGIS and classify into 5 zones using Natural Breaks")

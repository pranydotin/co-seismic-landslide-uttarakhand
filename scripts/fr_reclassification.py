import os
import numpy as np
import pandas as pd
import rasterio


input_folder = "/mnt/d/My Drive/cosesmic/layers/classified_rasters"
output_folder = "/mnt/d/My Drive/cosesmic/layers/output_fr_rasters"
fr_csv_path = "./data/processed/FR_results_features.csv"

os.makedirs(output_folder, exist_ok=True)

# ── RASTER FILENAME TO FACTOR NAME MAPPING ───────────────────────────────────
# Left  = actual raster filename (without .tif)
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

# Load FR table
fr_df = pd.read_csv(fr_csv_path)


# Build lookup: {factor: {class_value: FR_value}}
fr_lookup = {}
for factor, group in fr_df.groupby("factor"):
    fr_lookup[factor] = dict(zip(group["class"].astype(float), group["FR"]))

# ── STEP: Reclassify each raster ───────────────────────────────────────────
fr_raster_paths = []

for raster_name, factor in raster_to_factor.items():

    input_path = os.path.join(input_folder, raster_name + ".tif")
    output_path = os.path.join(output_folder, f"FR_{raster_name}.tif")

    if not os.path.exists(input_path):
        print(f"WARNING: File not found — {input_path}")
        continue

    if factor not in fr_lookup:
        print(
            f"WARNING: Factor '{factor}' not found in FR table — skipping {raster_name}")
        continue

    class_to_fr = fr_lookup[factor]

    try:
        with rasterio.open(input_path) as src:
            profile = src.profile.copy()
            input_nodata = src.nodata if src.nodata is not None else -9999

            # Update profile for output raster, explicitly setting tiled=True and block sizes
            output_profile = profile.copy()
            output_profile.update(dtype=rasterio.float32, nodata=-9999,
                                  compress='LZW', tiled=True, blockxsize=256, blockysize=256)

            with rasterio.open(output_path, "w", **output_profile) as dst:
                for ji, window in src.block_windows(1):
                    data_block = src.read(1, window=window).astype(float)

                    fr_block_array = np.zeros_like(
                        data_block, dtype=np.float32)

                    unique_classes_block = np.unique(
                        data_block[data_block != input_nodata])
                    for cls in unique_classes_block:
                        fr_val = class_to_fr.get(float(cls), 0.0)
                        fr_block_array[data_block == cls] = fr_val

                    fr_block_array[data_block == input_nodata] = -9999

                    dst.write(fr_block_array, 1, window=window)

        fr_raster_paths.append(output_path)
        print(f"Reclassified: {raster_name} → FR_{raster_name}.tif")
    except Exception as e:
        print(f"Error processing {raster_name}: {e}")

print(f"\n{len(fr_raster_paths)} / {len(raster_to_factor)} rasters reclassified\n")

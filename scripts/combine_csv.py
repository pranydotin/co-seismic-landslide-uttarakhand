import pandas as pd
import os
import re
import sys


def extract_factor_name(filename):

    match = re.search(r'unique_values_(.*?)_class\.csv', filename)
    if match:
        return match.group(1)
    return filename.replace(".csv", "")


def combine_csv(folder_path, output_path):
    all_dfs = []

    if not os.path.exists(folder_path):
        print(f"[ERROR] Folder not found: {folder_path}")
        sys.exit(1)

    files = [f for f in os.listdir(folder_path) if f.endswith(".csv")]

    print(f"[INFO] Found {len(files)} CSV files")

    for file in files:
        file_path = os.path.join(folder_path, file)
        print(f"[INFO] Processing: {file}")

        try:
            df = pd.read_csv(file_path)

            # Normalize column names
            df.columns = [col.strip().lower() for col in df.columns]

            if 'value' not in df.columns or 'count' not in df.columns:
                print(
                    f"[WARNING] Skipping {file} (missing 'value' or 'count')")
                continue

            df = df[['value', 'count']].copy()

            # Extract factor name properly
            factor_name = extract_factor_name(file)
            df['factor'] = factor_name

            # Rename columns
            df = df.rename(columns={
                'value': 'class',
                'count': 'Npix_i'
            })

            all_dfs.append(df)

        except Exception as e:
            print(f"[ERROR] Failed to process {file}: {e}")

    if not all_dfs:
        print("[ERROR] No valid CSV files processed.")
        sys.exit(1)

    final_df = pd.concat(all_dfs, ignore_index=True)

    # Sort nicely
    final_df = final_df.sort_values(by=['factor', 'class'])

    # Save
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    final_df.to_csv(output_path, index=False)

    print(f"[SUCCESS] Combined CSV saved to: {output_path}")
    print(f"[INFO] Total rows: {len(final_df)}")


if __name__ == "__main__":
    input_folder = "./data/interim/"
    output_dir = "./data/processed/"
    output_file = os.path.join(output_dir, "combined_pixels.csv")

    combine_csv(input_folder, output_file)

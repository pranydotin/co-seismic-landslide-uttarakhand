# Rainfall (CHIRPS v3.0)

## Dataset Overview

Rainfall is a critical triggering factor for landslides, influencing soil saturation, pore water pressure, and slope instability. Satellite-derived rainfall data were used to represent spatial and temporal variability in precipitation over the study area.

The CHIRPS (Climate Hazards Group InfraRed Precipitation with Station data) dataset provides high-resolution gridded rainfall estimates, combining satellite imagery with in-situ station data.

---

## Data Source

| Property                | Details                      |
| ----------------------- | ---------------------------- |
| **Dataset**             | CHIRPS v3.0 Rainfall Data    |
| **Provider**            | Climate Hazards Group (UCSB) |
| **Access Platform**     | https://data.chc.ucsb.edu    |
| **Data Format**         | GeoTIFF                      |
| **Spatial Resolution**  | 0.05° (~5 km)                |
| **Temporal Resolution** | Monthly                      |
| **Projection**          | WGS 84 (`EPSG:4326`)         |

---

## Study Area Preparation

Rainfall data were processed in QGIS using the following workflow:

1. Downloading monthly CHIRPS rainfall data for a 10-year period (2015–2024).
2. Clipping all raster layers to the Uttarakhand administrative boundary.
3. Generating rainfall derivatives using raster aggregation:
   - Mean rainfall (long-term average)
   - Maximum rainfall (extreme events)
   - Monsoon rainfall (June–September average)
4. Reclassifying continuous rainfall rasters into four classes using raster calculator based on data distribution.

Output files:

- `mean_rain_class.tif`
- `max_rain_class.tif`
- `monsoon_rain_class.tif`

---

## Rainfall Classification

### Mean Rainfall

| Class | Range (mm) |
| ----- | ---------- |
| 1     | < 100      |
| 2     | 100 – 150  |
| 3     | 150 – 200  |
| 4     | ≥ 200      |

---

### Monsoon Rainfall

| Class | Range (mm) |
| ----- | ---------- |
| 1     | < 200      |
| 2     | 200 – 350  |
| 3     | 350 – 500  |
| 4     | ≥ 500      |

---

### Maximum Rainfall

| Class | Range (mm) |
| ----- | ---------- |
| 1     | < 400      |
| 2     | 400 – 800  |
| 3     | 800 – 1200 |
| 4     | ≥ 1200     |

---

## Role in Study

Rainfall plays a significant role in landslide occurrence by influencing soil moisture conditions and triggering slope failures.

- **Mean rainfall** represents long-term moisture availability and background saturation conditions.
- **Maximum rainfall** captures extreme precipitation events that can directly trigger landslides.
- **Monsoon rainfall** reflects seasonal concentration of rainfall, which is particularly relevant in the Himalayan region.

These rainfall-derived factors are incorporated into the Frequency Ratio (FR) model to quantify their contribution to landslide susceptibility.

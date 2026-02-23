# Land Use Land Cover (LULC) Data

## Dataset Overview

Land Use Land Cover (LULC) data were obtained from the **ESA WorldCover 10 m global land cover product (Version 200, 2021)**.

The dataset is developed by the European Space Agency (ESA) under the ESA WorldCover initiative and was accessed through the Terrascope platform operated by VITO.

---

## Data Source

- **Product Name:** ESA WorldCover 10m v200 (2021)
- **Provider:** European Space Agency (ESA)
- **Access Platform:** Terrascope (VITO)
- **Data Format:** GeoTIFF
- **Spatial Resolution:** 10 meters
- **Original CRS:** EPSG:4326 (WGS84 Geographic Coordinate System)

Official references:

- https://esa-worldcover.org
- https://terrascope.be

---

## Classification Scheme

The ESA WorldCover dataset contains 11 land cover classes:

| Code | Class Name               |
| ---- | ------------------------ |
| 10   | Tree Cover               |
| 20   | Shrubland                |
| 30   | Grassland                |
| 40   | Cropland                 |
| 50   | Built-up                 |
| 60   | Bare / Sparse Vegetation |
| 70   | Snow and Ice             |
| 80   | Permanent Water Bodies   |
| 90   | Herbaceous Wetland       |
| 95   | Mangroves                |
| 100  | Moss and Lichen          |

---

## Study Area Preparation

The downloaded global tile(s) were processed in QGIS and prepared for analysis using the following steps:

1. Mosaic of relevant tiles (if multiple tiles were required).
2. Reprojection from EPSG:4326 to UTM Zone 43N (EPSG:32643).
3. Clipping using the Uttarakhand administrative boundary shapefile.
4. Verification of class values after reprojection.

---

## Resampling Method

Since ESA WorldCover is a **categorical raster dataset**, the following interpolation rule was applied:

- **Resampling Method:** Nearest Neighbor
- Bilinear or cubic interpolation was NOT used to preserve class integrity.

---

## Role in Study

The LULC raster is used as an environmental conditioning factor in the co-seismic landslide susceptibility modeling framework.

The processed raster will be integrated into the final feature stack for machine learning-based susceptibility assessment.

# Landslide Inventory Data

## Dataset Overview

The landslide inventory dataset consists of spatial point locations representing recorded landslide occurrences within Uttarakhand.

The dataset was obtained from the GeoDataIndia portal and downloaded in GeoJSON format. It is used as the dependent variable (landslide presence) in the co-seismic landslide susceptibility modeling framework.

---

## Data Source

- **Source Platform:** https://geodataindia.gov.in/
- **Dataset Type:** Landslide occurrence points
- **Geometry Type:** Point
- **Data Format:** GeoJSON (.geojson)
- **Original CRS:** EPSG:4326 (WGS84 Geographic Coordinate System)

The dataset contains geographic coordinates along with associated attribute information describing landslide events.

---

## Data Preparation

The landslide inventory was processed using the following steps:

1. CRS verification and reprojection to UTM Zone 43N (EPSG:32643).
2. Validation of point geometries.
3. Removal of duplicate records (if present).
4. Spatial filtering to ensure all points fall within the Uttarakhand boundary.

---

## Sampling Strategy

The landslide points represent presence locations. Stable (non-landslide) locations will be generated separately using controlled spatial sampling for supervised machine learning.

---

## Role in Study

The landslide inventory serves as the response variable in the landslide susceptibility modeling framework.

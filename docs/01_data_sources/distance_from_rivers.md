# Distance to Rivers

## Dataset Overview

The Distance to Rivers dataset represents the Euclidean distance of each grid cell from the nearest river channel within the study area.

This dataset was derived from the HydroRIVERS dataset and is used to quantify the spatial influence of river proximity on terrain stability. Areas closer to rivers are generally more susceptible to erosion, undercutting, and increased soil moisture, which can contribute to landslide occurrence.

---

## Data Source

- **Dataset:** HydroRIVERS
- **Provider:** HydroSHEDS
- **Access Platform:** https://www.hydrosheds.org/
- **Data Format:** File Geodatabase (GDB)
- **Data Type:** Vector (Line)
- **Original CRS:** `EPSG:4326` (WGS84 Geographic Coordinate System)

---

## Study Area Preparation

The HydroRIVERS dataset was processed in QGIS and prepared for analysis using the following steps:

1. Loading the HydroRIVERS dataset from the File Geodatabase.
2. Filtering the river network using the stream order attribute (`ORD_STRA <= 3`) to retain major and medium river channels.
3. Creating a buffer around the Uttarakhand boundary to preserve river segments near the edges of the study area.
4. Clipping the river network using the buffered boundary.
5. Reprojecting the clipped river layer to UTM Zone 44N (EPSG:32644).
6. Applying a 30-meter buffer to the river lines to improve raster representation.
7. Converting the buffered river layer into raster format with a spatial resolution of 30 meters.
8. Computing Euclidean distance using the Proximity tool.
9. Clipping the resulting distance raster using the Uttarakhand administrative boundary.

---

## Processing Method

The distance to rivers raster was generated using raster-based proximity analysis in QGIS.

The workflow included:

- Rasterization of buffered river features using a burn value of 1.
- Computation of Euclidean distance from river pixels.
- Generation of a continuous raster where each pixel represents distance to the nearest river in meters.

---

## Output Characteristics

- **Output File:** `distance_rivers.tif`
- **Spatial Resolution:** 30 meters
- **Projection:** UTM Zone 44N (`EPSG:32644`)
- **Data Type:** Continuous raster
- **Units:** Meters

---

## Role in Study

Distance to rivers is an important hydrological conditioning factor in landslide susceptibility analysis.

Areas located near river channels are more vulnerable due to:

- River bank erosion
- Slope undercutting
- Increased groundwater saturation
- Concentration of surface and subsurface flow

This variable is incorporated into the final feature stack for machine learning-based landslide susceptibility modeling.

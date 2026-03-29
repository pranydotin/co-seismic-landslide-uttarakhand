# Distance to Roads

## Dataset Overview

The Distance to Roads dataset represents the Euclidean distance of each grid cell from the nearest road within the study area.

This dataset was derived from OpenStreetMap (OSM) road network data and is used to quantify the spatial influence of road proximity on terrain stability. Areas closer to roads are often more susceptible to landslides due to slope cutting, vegetation removal, and altered drainage patterns.

---

## Data Source

- Dataset: OpenStreetMap Roads
- Provider: OpenStreetMap Contributors
- Access Platform: https://download.geofabrik.de/
- Data Format: GeoPackage (GPKG)
- Data Type: Vector (Line)
- Original CRS: EPSG:4326 (WGS84 Geographic Coordinate System)

---

## Study Area Preparation

The road network dataset was processed in QGIS and prepared for analysis using the following steps:

1. Loading the GeoPackage dataset into QGIS.
2. Extracting the roads layer (`gis_osm_roads_free_1`).
3. Filtering the road network to remove non-relevant classes such as footpaths, tracks, and pedestrian routes.
4. Retaining major and minor road classes including motorway, trunk, primary, secondary, tertiary, residential, service, and unclassified roads.
5. Clipping the road network using the Uttarakhand boundary.
6. Reprojecting the clipped road layer to UTM Zone 44N (EPSG:32644).
7. Converting the road network into raster format with a spatial resolution of 30 meters.

---

## Processing Method

The distance to roads raster was generated using raster-based proximity analysis in QGIS.

The workflow included:

- Rasterization of road features using a burn value of 1.
- **NoData correction:** After rasterization, road pixels were incorrectly assigned NoData values instead of the intended burn value. A Python script using GDAL was applied via the QGIS Python Console to replace all NoData values with 0, restoring valid pixel values at road locations before proximity computation.
- Computation of Euclidean distance from road pixels using the Proximity tool.
- Generation of a continuous raster where each pixel represents distance to the nearest road in meters.

---

## Output Characteristics

- Output File: distance_roads.tif
- Spatial Resolution: 30 meters
- Projection: UTM Zone 44N (EPSG:32644)
- Data Type: Continuous raster
- Units: Meters

---

## Role in Study

Distance to roads is an important anthropogenic conditioning factor in landslide susceptibility analysis.

Areas located near roads are more vulnerable due to:

- Slope cutting and excavation
- Destabilization of natural slopes
- Increased surface runoff and drainage alteration
- Vegetation removal

This variable is incorporated into the final feature stack for machine learning-based landslide susceptibility modeling.

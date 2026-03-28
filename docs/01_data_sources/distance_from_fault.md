# Distance to Faults

## Dataset Overview

The Distance to Faults dataset represents the Euclidean distance of each grid cell from the nearest geological fault within the study area.

This dataset was derived from geological fault data obtained from the National Geoscience Data Repository (NGDR) and is used to quantify the spatial influence of tectonic structures on terrain stability. Areas closer to faults are more susceptible to landslides due to fractured rock masses, structural weaknesses, and increased seismic activity.

---

## Data Source

- **Dataset**: Geological Faults (1:50K Scale)
- **Provider**: Geological Survey of India (GSI)
- **Access Platform**: https://geodataindia.gov.in
- **Data Repository**: National Geoscience Data Repository (NGDR)
- **Data Format**: GeoJSON
- **Data Type**: Vector (Line)
- **Original CRS**: `EPSG:4326` (WGS84 Geographic Coordinate System)

---

## Study Area Preparation

The fault dataset was processed in QGIS and prepared for analysis using the following steps:

1. Loading the fault shapefile into QGIS.
2. Merging multiple fault layers (if applicable) into a single unified layer.
3. Clipping the fault dataset using the Uttarakhand boundary.
4. Reprojecting the clipped fault layer to UTM Zone 44N (`EPSG:32644`).
5. Converting the fault layer into raster format using a spatial resolution of 30 meters.
6. Assigning a burn value of 1 to fault pixels during rasterization to distinguish fault locations from non-fault areas.

---

## Processing Method

The distance to faults raster was generated using raster-based proximity analysis in QGIS.

The workflow included:

- Rasterization of fault features with a burn value of 1.
- Computation of Euclidean distance from fault pixels using the Proximity tool.
- Use of georeferenced units to ensure distance values are calculated in meters.
- Generation of a continuous raster where each pixel represents distance to the nearest fault.

---

## Output Characteristics

- Output File: distance_faults.tif
- Spatial Resolution: 30 meters
- Projection: UTM Zone 44N (`EPSG:32644`)
- Data Type: Continuous raster
- Units: Meters

---

## Role in Study

Distance to faults is a critical geological conditioning factor in landslide susceptibility analysis.

Areas located near faults are more vulnerable due to:

- Presence of fractured and weak rock zones
- Increased permeability and water infiltration
- Structural discontinuities in the terrain
- Potential seismic activity influencing slope stability

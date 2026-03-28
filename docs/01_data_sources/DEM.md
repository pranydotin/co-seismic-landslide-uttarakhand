# Digital Elevation Model (DEM)

## Dataset Overview

The Digital Elevation Model (DEM) represents the elevation of the terrain surface for the study area. It provides the base dataset required for deriving terrain parameters such as slope, aspect, curvature, flow accumulation, and topographic wetness index.

---

## Data Source

| Property | Details |
|---|---|
| **Dataset** | SRTM Digital Elevation Model |
| **Provider** | NASA / USGS |
| **Access Platform** | USGS EarthExplorer |
| **Data Format** | GeoTIFF |
| **Spatial Resolution** | 30 meters |
| **Projection** | UTM Zone 44N (`EPSG:32644`) |

---

## Study Area Preparation

The DEM data were processed in QGIS using the following steps:

1. Downloading the required SRTM tiles covering the study area.
2. Merging the tiles where necessary.
3. Reprojecting the DEM to UTM Zone 44N (EPSG:32644).
4. Clipping the DEM using the Uttarakhand administrative boundary shapefile.

Output file: `DEM_UK.tif`

---

## Role in Study

The Digital Elevation Model provides the fundamental representation of terrain elevation in the study area. It serves as the base dataset from which all other terrain derivatives such as slope, aspect, curvature, and hydrological indices are calculated.

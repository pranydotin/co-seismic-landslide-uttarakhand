# Normalized Difference Vegetation Index (NDVI)

## Dataset Overview

The Normalized Difference Vegetation Index (NDVI) was derived from Sentinel-2 Level-2A surface reflectance imagery obtained through the Copernicus Data Space Ecosystem.

NDVI represents vegetation density and condition and is widely used as an environmental conditioning factor in landslide susceptibility studies.

---

## Data Source

- **Satellite Mission:** Sentinel-2
- **Product Level:** Level-2A (Surface Reflectance)
- **Access Platform:** Copernicus Data Space Browser
- **Platform URL:** https://browser.dataspace.copernicus.eu/
- **Provider:** Copernicus Programme (European Space Agency)
- **Spatial Resolution:** 10 meters
- **Bands Used:**
  - B4 (Red, 10 m resolution)
  - B8 (Near Infrared, 10 m resolution)
- **Original CRS:** EPSG:4326 (WGS84 Geographic Coordinate System)

Official mission reference:
https://sentinels.copernicus.eu/web/sentinel/missions/sentinel-2

---

## NDVI Computation

NDVI was calculated using the standard normalized difference vegetation index formula:

$$
NDVI = \frac{NIR - Red}{NIR + Red}
$$

For Sentinel-2 imagery, the bands correspond to:

$$
NDVI = \frac{B8 - B4}{B8 + B4}
$$

Where:

- **B8** = Near Infrared (NIR) band
- **B4** = Red band

The calculation was performed using raster operations in QGIS/Python after extracting the required spectral bands.

---

## Study Area Preparation

The derived NDVI raster was processed using the following steps:

1. Extraction of B4 and B8 bands from Sentinel-2 Level-2A imagery.
2. NDVI computation using raster calculator.
3. Reprojection to UTM Zone 43N (EPSG:32643).
4. Clipping using the Uttarakhand administrative boundary GeoJSON.
5. Verification of spatial alignment with other environmental layers.

---

## Role in Study

NDVI is incorporated as an environmental conditioning factor representing vegetation cover in the co-seismic landslide susceptibility modeling framework.

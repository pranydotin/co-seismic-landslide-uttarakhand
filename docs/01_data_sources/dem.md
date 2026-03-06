# Digital Elevation Model (DEM)

## Dataset Overview

The Digital Elevation Model (DEM) represents the elevation of the terrain surface for the study area.
It provides the base dataset required for deriving terrain parameters such as slope and curvature.

---

## Data Source

- **Dataset:** SRTM Digital Elevation Model
- **Provider:** NASA / USGS
- **Access Platform:** USGS EarthExplorer
- **Data Format:** GeoTIFF
- **Spatial Resolution:** 30 meters
- **Projection:** UTM Zone 44N (EPSG:32644)

---

## Study Area Preparation

The DEM data were processed in QGIS using the following steps:

1. Downloading the required SRTM tiles covering the study area.
2. Merging the tiles where necessary.
3. Reprojecting the DEM to UTM Zone 44N (EPSG:32644).
4. Clipping the DEM using the Uttarakhand administrative boundary shapefile.

The processed DEM was saved as:

```
DEM_UK.tif
```

---

# Slope

## Description

Slope represents the steepness of the terrain and is calculated as the rate of change in elevation between neighboring cells.

Higher slope values generally indicate steeper terrain, which is more susceptible to landslides due to gravitational forces acting on slope materials.

---

## QGIS Processing

Slope was derived from the DEM using the QGIS terrain analysis tool:

```
Raster → Terrain Analysis → Slope
```

Parameters used:

- **Input layer:** DEM_UK
- **Z-factor:** 1
- **Output unit:** Degrees

The resulting raster was saved as:

```
slope.tif
```

---

# Curvature

Curvature describes the rate of change of slope and helps identify concave and convex terrain features.

Two curvature measures were generated for the analysis.

---

## Profile Curvature

Profile curvature measures the curvature of the surface **in the direction of slope**.

It influences the acceleration and deceleration of surface runoff along the slope.

### Processing

Profile curvature was generated using the SAGA terrain analysis tools in QGIS:

```
Processing Toolbox → SAGA → Terrain Analysis → Slope, Aspect, Curvature
```

Output file:

```
profile_curvature.tif
```

---

## Plan Curvature

Plan curvature measures curvature **perpendicular to the slope direction**.

It controls the convergence and divergence of water flow across the terrain surface.

### Processing

Plan curvature was generated using the same SAGA terrain analysis tool in QGIS.

Output file:

```
plan_curvature.tif
```

---

## Role in Study

### DEM

The Digital Elevation Model provides the fundamental terrain representation of the study area. It serves as the base dataset from which other terrain derivatives such as slope and curvature are calculated. Elevation also influences climatic conditions, vegetation distribution, and geomorphological processes that may affect landslide occurrence.

---

### Slope

Slope represents the steepness of the terrain and is one of the most important factors influencing landslides. Steeper slopes experience higher gravitational stress, which increases the likelihood of slope instability and mass movement.

---

### Profile Curvature

Profile curvature describes the curvature of the terrain along the direction of maximum slope. It affects the acceleration or deceleration of surface runoff, which influences erosion and deposition processes on slopes.

---

### Plan Curvature

Plan curvature represents the curvature of the terrain perpendicular to the slope direction. It controls the convergence and divergence of surface flow. Areas with converging flow tend to accumulate water and sediments, which can increase landslide susceptibility.

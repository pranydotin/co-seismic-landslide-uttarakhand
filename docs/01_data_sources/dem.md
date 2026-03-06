# Digital Elevation Model (DEM)

## Dataset Overview

The Digital Elevation Model (DEM) represents the elevation of the terrain surface for the study area.
It provides the base dataset required for deriving terrain parameters such as slope, aspect, curvature, flow accumulation, and topographic wetness index.

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

## Processing

Slope was derived from the DEM using terrain analysis tools:

```
Terrain Analysis → Morphometry → Slope, Aspect, Curvature
```

The resulting raster was saved as:

```
slope.tif
```

---

# Aspect

## Description

Aspect represents the direction that a slope faces relative to north. It influences solar radiation, soil moisture, and vegetation distribution.

These environmental factors can indirectly affect slope stability and landslide occurrence.

---

## Processing

Aspect was generated using the same terrain morphometry tool.

Output file:

```
aspect.tif
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

```
Terrain Analysis → Morphometry → Slope, Aspect, Curvature
```

Output file:

```
profile_curvature.tif
```

---

## Plan Curvature

Plan curvature represents the curvature of the terrain perpendicular to the slope direction.

It controls the convergence and divergence of water flow across the terrain surface.

### Processing

Plan curvature was generated using the same SAGA terrain analysis tool.

Output file:

```
plan_curvature.tif
```

---

# Flow Accumulation

## Description

Flow accumulation represents the amount of upstream contributing area flowing into each grid cell. Cells with high flow accumulation values typically correspond to drainage channels or valley bottoms.

This parameter is important for identifying water concentration zones.

---

## Processing

Before calculating flow accumulation, sinks in the DEM were filled to ensure proper drainage flow.

```
Terrain Analysis → Preprocessing → Fill Sinks (Wang & Liu)
```

Flow accumulation was then calculated from the filled DEM.

```
Terrain Analysis → Hydrology → Flow Accumulation
```

Output file:

```
flow_accumulation.tif
```

---

# Topographic Wetness Index (TWI)

## Description

The Topographic Wetness Index represents the spatial distribution of soil moisture based on terrain shape and drainage patterns.

The index is calculated as:

$$
TWI = \ln \left(\frac{A_s}{\tan \beta}\right)
$$

Where:

- $A_s$ = specific catchment area
- $β$ = slope angle

Higher $TWI$ values generally indicate wetter areas such as valleys and drainage lines.

---

## Processing

TWI was calculated using the slope and flow accumulation layers.

```
Terrain Analysis → Hydrology → Topographic Wetness Index
```

Output file:

```
twi.tif
```

---

# Terrain Ruggedness Index (TRI)

## Description

Terrain Ruggedness Index measures the amount of elevation difference between a grid cell and its surrounding cells. It quantifies the roughness or ruggedness of terrain.

The index is calculated as:

$$
TRI = \left(\sum (E_c - E_i)^2 \right)^2
$$

Where:

- $E_c$ = elevation of the central cell
- $E_i$ = elevation of neighboring cells

High TRI values typically correspond to rugged mountainous areas.

---

## Processing

TRI was calculated from the DEM using terrain analysis tools.

```
Terrain Analysis → Morphometry → Terrain Ruggedness Index
```

Output file:

```
tri.tif
```

---

## Role in Study

### DEM

The Digital Elevation Model provides the fundamental representation of terrain elevation in the study area. It serves as the base dataset from which all other terrain derivatives such as slope, aspect, curvature, and hydrological indices are calculated.

---

### Slope

Slope represents the steepness of the terrain. Areas with steeper slopes are generally more susceptible to landslides due to increased gravitational forces acting on soil and rock materials.

---

## Aspect

Aspect indicates the direction that a slope faces. It influences microclimatic conditions such as solar radiation, soil moisture, and vegetation cover, which can indirectly affect slope stability.

---

### Profile Curvature

Profile curvature describes the curvature of the terrain along the direction of maximum slope. It affects the acceleration or deceleration of surface runoff, which influences erosion and deposition processes on slopes.

---

### Plan Curvature

Plan curvature represents the curvature of the terrain perpendicular to the slope direction. It controls the convergence and divergence of surface flow. Areas with converging flow tend to accumulate water and sediments, which can increase landslide susceptibility.

---

## Flow Accumulation

Flow accumulation represents the amount of upstream contributing area flowing into a grid cell. High values typically correspond to drainage channels and valley bottoms where water accumulates.

---

## Topographic Wetness Index (TWI)

The Topographic Wetness Index indicates the spatial distribution of soil moisture based on terrain shape and drainage patterns. Areas with higher TWI values are more likely to experience water saturation.

---

## Terrain Ruggedness Index (TRI)

Terrain Ruggedness Index measures the variability in elevation between a cell and its surrounding cells. Higher TRI values indicate more rugged terrain, which can influence slope stability and erosion processes.

# Aspect

## Description

Aspect represents the direction that a slope faces relative to north. It influences solar radiation, soil moisture, and vegetation distribution, which can indirectly affect slope stability and landslide occurrence.

---

## Processing

Aspect was generated from the DEM using terrain morphometry tools:

```
Terrain Analysis → Morphometry → Slope, Aspect, Curvature
```

Output file: `aspect.tif`

The original aspect raster contains continuous values ranging from **0° to 360°**. It was reclassified into categorical directional classes using the QGIS Raster Calculator:

| Value | Direction |
|---|---|
| 0 | Flat |
| 1 | North |
| 2 | Northeast |
| 3 | East |
| 4 | Southeast |
| 5 | South |
| 6 | Southwest |
| 7 | West |
| 8 | Northwest |

Reclassified output file: `aspect_class.tif`

This categorical representation is commonly used in landslide susceptibility studies to simplify interpretation and statistical modelling.

---

## Role in Study

Aspect indicates the direction that a slope faces. It influences microclimatic conditions such as solar radiation, soil moisture, and vegetation cover, which can indirectly affect slope stability.

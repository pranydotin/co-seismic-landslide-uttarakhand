# Curvature

## Description

Curvature describes the rate of change of slope and helps identify concave and convex terrain features. Two curvature measures were generated for the analysis.

---

## Profile Curvature

Profile curvature measures the curvature of the surface **in the direction of slope**. It influences the acceleration and deceleration of surface runoff along the slope.

### Processing

```
Terrain Analysis → Morphometry → Slope, Aspect, Curvature
```

Output file: `profile_curvature.tif`

### Role in Study

Profile curvature describes the curvature of the terrain along the direction of maximum slope. It affects the acceleration or deceleration of surface runoff, which influences erosion and deposition processes on slopes.

---

## Plan Curvature

Plan curvature represents the curvature of the terrain **perpendicular to the slope direction**. It controls the convergence and divergence of water flow across the terrain surface.

### Processing

```
Terrain Analysis → Morphometry → Slope, Aspect, Curvature
```

Output file: `plan_curvature.tif`

### Role in Study

Plan curvature controls the convergence and divergence of surface flow. Areas with converging flow tend to accumulate water and sediments, which can increase landslide susceptibility.

# Terrain Ruggedness Index (TRI)

## Description

Terrain Ruggedness Index measures the amount of elevation difference between a grid cell and its surrounding cells. It quantifies the roughness or ruggedness of terrain. High TRI values typically correspond to rugged mountainous areas.

The index is calculated as:

$$
TRI = \left(\sum (E_c - E_i)^2 \right)^{0.5}
$$

Where:

- $E_c$ = elevation of the central cell
- $E_i$ = elevation of neighboring cells

---

## Processing

TRI was calculated from the DEM using terrain analysis tools:

```
Terrain Analysis → Morphometry → Terrain Ruggedness Index
```

Output file: `tri.tif`

---

## Role in Study

Terrain Ruggedness Index measures the variability in elevation between a cell and its surrounding cells. Higher TRI values indicate more rugged terrain, which can influence slope stability and erosion processes.

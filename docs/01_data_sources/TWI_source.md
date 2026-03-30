# Topographic Wetness Index (TWI)

## Description

The Topographic Wetness Index represents the spatial distribution of soil moisture based on terrain shape and drainage patterns. Higher TWI values generally indicate wetter areas such as valleys and drainage lines.

The index is calculated as:

$$
TWI = \ln \left(\frac{A_s}{\tan \beta}\right)
$$

Where:

- $A_s$ = specific catchment area
- $\beta$ = slope angle

---

## Processing

TWI was calculated using the slope and flow accumulation layers:

```
Terrain Analysis → Hydrology → Topographic Wetness Index
```

Output file: `twi.tif`

---

## Role in Study

The Topographic Wetness Index indicates the spatial distribution of soil moisture based on terrain shape and drainage patterns. Areas with higher TWI values are more likely to experience water saturation.

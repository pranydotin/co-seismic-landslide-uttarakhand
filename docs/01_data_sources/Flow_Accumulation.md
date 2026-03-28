# Flow Accumulation

## Description

Flow accumulation represents the amount of upstream contributing area flowing into each grid cell. Cells with high flow accumulation values typically correspond to drainage channels or valley bottoms. This parameter is important for identifying water concentration zones.

---

## Processing

Before calculating flow accumulation, sinks in the DEM were filled to ensure proper drainage flow:

```
Terrain Analysis → Preprocessing → Fill Sinks (Wang & Liu)
```

Flow accumulation was then calculated from the filled DEM:

```
Terrain Analysis → Hydrology → Flow Accumulation
```

Output file: `flow_accumulation.tif`

---

## Role in Study

Flow accumulation represents the amount of upstream contributing area flowing into a grid cell. High values typically correspond to drainage channels and valley bottoms where water accumulates.

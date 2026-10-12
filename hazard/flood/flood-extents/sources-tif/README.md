# Flood Depth Sources

This directory intentionally does not store the flood depth source GeoTIFFs.

They are large rebuildable inputs, not seed artifacts. Regenerate them locally from the IBF repository:

```bash
cd data
uv run python -m data_management.seed_data_management.flood.build_flood_depth_sources
```

Sources:

- Flood depth: [JRC/GloFAS global river flood hazard maps](https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/CEMS-GLOFAS/flood_hazard/) v2.1.2, `_depth.tif` tiles (water depth in metres, ~90 m).
- Lake mask: [HydroLAKES](https://www.hydrosheds.org/products/hydrolakes) v1.0 polygons.

The operational seed artifacts are the converted files in `../data-png/`. The scripts are maintained in:

```text
IBF/data/data_management/seed_data_management/flood/
```

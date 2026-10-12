# Flood extent maps

Nation-wide flood extent rasters per return period. Used in floods pipeline to create event flood extent and calculate exposure.

- `sources-tif/` — source GeoTIFFs, named `{ISO3}_flood_extent_rp{N}.tif`. Large rebuildable inputs, not committed; see [sources-tif/README.md](sources-tif/README.md). Never fetched over HTTP.
- `data-png/` — generated output, named `{ISO3}_flood_extent_rp{N}.png` plus a `_metadata.json` per file and one `{ISO3}_flood_extents_manifest.json` per country. This is what the pipeline fetches over HTTP.

Both are produced by scripts in the [IBF repo](https://github.com/rodekruis/IBF/tree/main/data/data_management/seed_data_management/flood): `build_flood_depth_sources.py` builds `sources-tif/`, and `convert_flood_depth_to_png.py` converts it into `data-png/`.

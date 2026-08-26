# Flood extent maps

Nation-wide flood extent rasters per return period. Used in floods pipeline to create event flood extent and calculate exposure.

- `sources-tif/` — source GeoTIFFs, named `flood_map_{ISO3}_RP{N}.tif`. Read only by the conversion script, on a local checkout. Never fetched over HTTP.
- `data-png/` — generated output, named `{ISO3}_flood_extent_rp{N}.png` plus a `_metadata.json` per file and one `{ISO3}_flood_extents_manifest.json` per country. This is what the pipeline fetches over HTTP.

Conversion is done by `convert_flood_depth_to_png.py` in the [IBF repo](https://github.com/rodekruis/IBF/tree/main/data).

The two naming conventions (`flood_map_ETH_RP10.tif` vs `ETH_flood_extent_rp10.png`) are historical
and inconsistent; align them when the conversion script is next touched.

## Pending: move `sources-tif/` to blob storage

`sources-tif/` is ~700 MB — the largest thing in this repository — and is never fetched over HTTP.
It does not need to be in git. Once the files are uploaded to blob storage and the location is
recorded here, remove them and point `convert_flood_depth_to_png.py` at the new location:

```sh
git rm -r hazard/flood/flood-extents/sources-tif
```

Note that this shrinks the working tree but not `.git` — the blobs stay in history unless the
history is rewritten separately.

TODO: add the original source of the flood extent rasters.

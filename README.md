# IBF seed and mock data repository

Seed and mock data for the [IBF backend and pipelines](https://github.com/rodekruis/IBF).

## File size limit

**Individual file sizes must be kept below 100mb.** Above that [git-lfs](https://git-lfs.com/) would
be needed, which has proved to come with problems for our setup.

## This repository is a runtime dependency, not just a data dump

The deployed API service and the pipelines fetch files from this repo **over HTTP at runtime**, from
`https://raw.githubusercontent.com/rodekruis/IBF-seed-data/refs/heads/main/...`.

Two consequences:

- **Paths are a contract.** Renaming or moving a folder or file breaks running services. Such a change must land together with a matching PR in the IBF repo.
- **`main` is production.** Because consumers pin to `refs/heads/main`, a commit here takes effect immediately, everywhere, with no rollback step.

## Layout

```
admin-areas/          Admin area geometry and placeCodes
exposure/             What is at risk (population)
hazard/               Static, hazard-specific inputs
  flood/
  drought/
mock-forecasts/       Stand-in forecast feeds for MOCK_ALERT / MOCK_NO_ALERT runs
reference/            Country reference data cached from external APIs
```

The organising principle is **subject first, hazard second**. Each folder answers "what is this data
about?" — admin areas, exposure, a hazard, a forecast feed — which is a property of the data itself
and stays true no matter who or what consumes it.

## Data

### admin-areas

Admin area geometry and codes. `processed/` is the ready-to-use output; see
[admin-areas/README.md](admin-areas/README.md).

### exposure/population

Population rasters as value-encoded PNGs. Also the input for the population figures written onto
`admin-areas/processed/`.

### hazard/flood

- `glofas-stations/{ISO3}_station_thresholds.json` — per-station discharge thresholds by return period, plus station coordinates and the admin pcodes each station covers. This is the only flood threshold file the current pipeline reads.
- `glofas-stations/locations-all-countries/` — station locations for 44 countries. For the 7 supported countries this duplicates the coordinates already in the threshold files; the remaining countries are kept as a starting point for onboarding. Provenance and currency are unknown.
- `flood-extents/` — nation-wide flood extent per return period. See [its README](hazard/flood/flood-extents/README.md).

### hazard/drought

`ETH_climate_region_district_mapping.csv` maps Ethiopian districts to climate regions (Belg, Meher,
Southern, …). It is **not read by any code**. It is the provenance for the hardcoded
`ETH_DROUGHT_CONFIGS` `spatialExtentPlaceCodes` arrays in
`services/api-service/src/seed/seed-data/seed-alert-configs.const.ts`, which carry a standing TODO
about sourcing them from this repo instead. Keep the two in sync until that TODO is resolved.

### mock-forecasts

Stand-in forecast feeds used by the `MOCK_ALERT` and `MOCK_NO_ALERT` pipeline run targets. In
production these arrive fresh each cycle from GloFAS, ECMWF and NOAA; here they are frozen
snapshots — mostly synthetic, with the tropical-cyclone fixtures being real historical cycles.
See [mock-forecasts/README.md](mock-forecasts/README.md).

### reference/go-data

Country-related data — hospital locations, Red Cross branch locations, admin area extents — cached
from the IFRC GO API. Nothing reads it yet; it is a cache and can be regenerated at any time.

## How this data is produced

Most of this repo is **generated output**, written by scripts in
[`data/data_management/seed_data_management/`](https://github.com/rodekruis/IBF/tree/main/data/data_management/seed_data_management)
in the IBF repo. 

> **Never hand-edit generated output.** Change the source, or the script, and re-run it. A manual edit will be silently overwritten on the next run, and leaves no trace of how the value got there.

Note that source and generated output are not always both stored here: `exposure/population/` keeps
only the output because the WorldPop GeoTIFFs are too large, while `hazard/flood/glofas-stations/`
has no generating script at all.
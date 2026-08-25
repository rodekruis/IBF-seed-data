# IBF seed and mock data repository

Seed and mock data for the [IBF backend and pipelines](https://github.com/rodekruis/IBF).

## File size limit

**Individual file sizes must be kept below 100mb.** Above that [git-lfs](https://git-lfs.com/) would
be needed, which has proved to come with problems for our setup.

## This repository is a runtime dependency, not just a data dump

The deployed API service and the pipelines fetch files from this repo **over HTTP at runtime**, from
`https://raw.githubusercontent.com/rodekruis/IBF-seed-data/refs/heads/main/...`.

Two consequences:

- **Paths are a contract.** Renaming or moving a folder listed under [Consumed paths](#consumed-paths) breaks running services. Such a change must land together with a matching PR in the IBF repo.
- **`main` is production.** Because consumers pin to `refs/heads/main`, a commit here takes effect immediately, everywhere, with no rollback step.

## Layout

```
admin-areas/          Admin area geometry and codes
  processed/            Ready-to-use output — this is what gets seeded
  sources/              Inputs the processed output is generated from
exposure/             What is at risk (population)
hazard/               Static, hazard-specific inputs
  flood/
  drought/
mock-forecasts/       Stand-in forecast feeds for MOCK_ALERT / MOCK_NO_ALERT runs
reference/            Country reference data cached from external APIs
```

The organising principle is **subject first, hazard second**. Data is deliberately *not* filed by
which service consumes it — most of it ends up in the database and is then used by pipelines,
backend and frontend alike, so that split would be arbitrary and would drift.

Two conventions worth knowing:

- **Generated output lives next to, but separate from, its sources.** `admin-areas/processed/` is produced from `admin-areas/sources/`; `data-png/` folders are produced from raster sources. Never hand-edit generated output — change the source and re-run the script.
- **`data-png`** means value-encoded PNG (pixel values carry data, not colour), not a visual map.

## Consumed paths

Everything below is read by code. Changing these paths requires a matching IBF PR.

| Path | Consumer | How |
| --- | --- | --- |
| `admin-areas/processed/{ISO3}_adm{N}.json` | API service seeding | HTTP |
| `hazard/flood/glofas-stations/{ISO3}_station_thresholds.json` | API service seeding | HTTP |
| `exposure/population/data-png/{ISO3}_population{,_metadata}.{png,json}` | API service seeding | HTTP |
| `hazard/flood/flood-extents/data-png/` | Flood pipeline | HTTP |
| `mock-forecasts/flood/glofas-discharge/` | Flood pipeline, mock runs | HTTP |
| `mock-forecasts/tropical-cyclone/{ISO3}/gefs-{wind,track}/` | Tropical cyclone pipeline, mock runs | HTTP |
| `admin-areas/`, `hazard/flood/flood-extents/sources-tif/`, `reference/` | `IBF/data/data_management/seed_data_management/*.py` | Local checkout via `SEED_DATA_REPO_ROOT` |

## Data

### admin-areas

Admin area geometry and codes. `processed/` is the ready-to-use output; see
[admin-areas/README.md](admin-areas/README.md).

### exposure/population

Population rasters as value-encoded PNGs, fetched from WorldPop and converted by
`fetch_population_raster.py` in [the IBF repo](https://github.com/rodekruis/IBF/tree/main/data).

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
from the IFRC GO API (e.g. `https://goadmin.ifrc.org/api/v2/country/?limit=9999`) by
`fetch_go_data.py` in [the IBF repo](https://github.com/rodekruis/IBF/tree/main/data). Nothing reads
it yet; it is a cache and can be regenerated at any time.

## Repository size

The working tree is ~2 GB and `.git` is ~2.7 GB, because generated binaries are committed and every
regeneration adds a permanent blob. Note that the 100 MB file size limit above caps individual files
but does nothing about total repo size — the real cost is churn on generated rasters and GeoJSON.

`hazard/flood/flood-extents/sources-tif/` (~700 MB) is the single largest item and is only ever read
by one local script. It is staged for removal to blob storage; see
[its README](hazard/flood/flood-extents/README.md).

# Admin Areas

Admin-area geometry, hierarchy codes, and population attributes used by the API service and pipelines.

`processed/` contains the operational seed artifacts. These files are generated from configured upstream sources and should not be hand-edited. To change them, update the processing configuration and rerun the admin-area workflow in the IBF repository:

```text
IBF/data/data_management/seed_data_management/admin_areas/
```

See the [admin-area processing README](https://github.com/rodekruis/IBF/tree/main/data/data_management/seed_data_management/admin_areas) in the IBF repository.

## processed

The API service seeds admin areas from `admin-areas/processed/`.

Each processed file is a GeoJSON `FeatureCollection` named `{COUNTRY}_adm{LEVEL}.json`. Features use a stable property schema with:

- the feature's own `ADM{LEVEL}_PCODE` and `ADM{LEVEL}_EN`;
- ancestor `ADM*_PCODE` values;
- `POPULATION`;
- valid `MultiPolygon` geometry.

The active country/level/source configuration, processing scripts, and validation report are maintained in the IBF repository.

## sources/hdx

HDX COD-AB extracts are large rebuildable inputs and are not committed here. The directory contains only a README. Regenerate local HDX source files from the IBF repository when processing admin areas.

## sources/gadm

GADM source files are used for configured countries that rely on GADM, currently Kenya. They can be regenerated from https://gadm.org/data.html by the IBF admin-area workflow.

## sources/ibf-v1

IBF v1 admin-area sources are retained as historical reference data only. They are not part of the active admin-area processing workflow.

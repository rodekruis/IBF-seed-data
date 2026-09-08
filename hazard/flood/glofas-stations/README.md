# GloFAS Station Thresholds

The `*_station_thresholds.json` files contain one record per GloFAS station. The `pcodes` field contains the admin-area place codes used for that country's flood alert configuration and runtime exposure calculation.

## Migrating Station Mappings

Mappings are migrated by the flood-specific
`migrate_glofas_station_area_mapping` script in the IBF repository. The script
transfers the existing station footprints from the old admin-area dataset to
the new admin-area dataset using spatial overlap:

```bash
cd /path/to/IBF/data
uv run python -m data_management.seed_data_management.flood.migrate_glofas_station_area_mapping \
	--old-seed-repo /path/to/old-IBF-seed-data \
	--new-seed-repo /path/to/IBF-seed-data \
	--old-seed-revision <old-seed-revision> \
	--new-seed-revision <new-seed-revision> \
	--output-directory /tmp/ibf-glofas-migration
```

The default per-area threshold is 25%: a new area must have at least 25% of its
area covered by the old station footprint. A migration is flagged for review
when the accepted new areas cover less than 90% of the old footprint. These
thresholds are recorded in each `{country}_migration_manifest.json` file.

The migration processes ETH, KEN, MWI, PHL, SSD, UGA, and ZMB. ZMB migrates
old adm3 station mappings to new adm4 areas; the other countries retain their
existing deepest admin level. Review the generated reports before copying the
threshold files into this directory.

```bash
cp /tmp/ibf-glofas-migration/*_station_thresholds.json /path/to/IBF-seed-data/hazard/flood/glofas-stations/
cp /tmp/ibf-glofas-migration/*_migration_manifest.json /path/to/IBF-seed-data/hazard/flood/glofas-stations/
```

The migration manifests preserve the old and new seed revisions, source paths,
thresholds, and output paths. Commit each manifest with its corresponding
threshold file so the one-time mapping decision remains reproducible. The
spatial migration is not a recurring forecast update; rerun it only when the
admin-area dataset or the station mappings are intentionally migrated again.

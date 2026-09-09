# HDX Admin-Area Sources

This directory intentionally does not store raw HDX COD-AB extracts.

The raw HDX files are large rebuildable inputs, not seed artifacts. Regenerate them locally from the IBF repository when admin-area processing is needed:

```bash
cd data
python -m data_management.seed_data_management.admin_areas.fetch_hdx_admin_areas
```

The operational seed artifacts are the processed files in `admin-areas/processed/`. The processing workflow and validation report are maintained in:

```text
IBF/data/data_management/seed_data_management/admin_areas/
```

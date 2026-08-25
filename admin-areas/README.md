# Admin areas

Admin area geometry and codes.

`processed/` is generated from `sources/`. Never hand-edit `processed/` — change a source and re-run
the relevant script in
[IBF/data/data_management/seed_data_management](https://github.com/rodekruis/IBF/tree/main/data).

### processed

The admin areas that are ready to use by the pipeline, backend, etc. This is the folder the API
service seeds from, over HTTP.

As of April 2026, here are the sources:
Admin 0: GADM
Admin 1, 2, 3, 4: Ibf v1

Produced by `convert_gadm_admin_areas.py` and `populate_ibf_v1_admin_area_parents.py`, then cleaned
by `clean_all_processed_admin_areas.py` and enriched by `add_population_to_admin_areas.py`.

### sources/ibf-v1

Admin areas (lvl 1 to 4) imported from [IBF v1 repo](https://github.com/rodekruis/IBF-system/tree/master/services/API-service/src/scripts/git-lfs). The source(s) are varied and they may be out of date. Not all countries are in the data. These are - until officially migrating - the sources, as used by both the pipeline and the back-end.

Because of this, we'll need to move to `sources/gadm` eventually.

### sources/gadm

Admin areas (lvl 0 to 3) fetched from https://gadm.org/data.html. Not all countries have admin level 3 and 4 though (i.e. Zimbabwe only has 0, 1, and 2). 

For now, we're using admin 0 for the processed data. For the other levels, this data is in here for testing/prototyping purposes only. We will need to move to using this data eventually, but we'll need different sources for admin 3 and 4 for some of the countries.

Admin 0 covers 246 countries, well beyond the countries IBF currently supports. This is intentional:
the portal can display any country's outline.

See [the IBF repo](https://github.com/rodekruis/IBF/tree/main/data) for more information on how this data is fetched.

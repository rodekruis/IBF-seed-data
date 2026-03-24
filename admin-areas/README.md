# IBF seed and mock data repository

Data related to admin area geometry and codes. 

### combined

These are the processed admin-areas that are ready to use by the pipeline, backend, etc.

### admin-areas-v1

Admin areas (lvl 1 to 4) imported from [IBF v1 repo](https://github.com/rodekruis/IBF-system/tree/master/services/API-service/src/scripts/git-lfs). The source(s) are varied and they may be out of date. Not all countries are in the data. These are - until officially migrating - the sources, as used by both the pipeline and the back-end.

Because of this, we'll need to move to admin-areas-gadm eventually.

### admin-areas-gadm

Admin areas (lvl 0 to 3) fetched from https://gadm.org/data.html. Not all countries have admin level 3 and 4 though (i.e. Zimbabwe). 

For now, this data is in here for testing/prototyping purposes only. We will need to move to using this data eventually, but we'll need different sources for admin 3 and 4 for some of the countries.

See [the IBF repo](https://github.com/rodekruis/IBF/tree/main/data) for more information on how this data is fetched.

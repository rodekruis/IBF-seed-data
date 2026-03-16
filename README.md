# IBF seed and mock data repository

This repository contains all seed and mock data for the [IBF backend and pipelines](https://github.com/rodekruis/IBF).

## File size limit

Individual file sizes should be kept below 100mb. Above that [git-lfs](https://git-lfs.com/) would be needed, which has proved to come with problems for our setup.

## Data

Descriptions and notes for the stored data in the repo

### admin-areas

Admin areas (lvl 1 to 4) imported from [IBF v1 repo](https://github.com/rodekruis/IBF-system/tree/master/services/API-service/src/scripts/git-lfs). The source(s) are varied and they may be out of date. Not all countries are in the data. These are - until officially migrating - the sources, as used by both the pipeline and the back-end.

Because of this, we'll need to move to admin-areas-gadm eventually.

### admin-areas-gadm

Admin areas (lvl 0 to 3) fetched from https://gadm.org/data.html. Not all countries have admin level 3 and 4 though (i.e. Zimbabwe). 

For now, this data is in here for testing/prototyping purposes only. We will need to move to using this data eventually, but we'll need different sources for admin 3 and 4 for some of the countries.

See [the IBF repo](https://github.com/rodekruis/IBF/tree/main/data) for more information on how this data is fetched.

### country-data/go-data

This includes various country-related data, such as hospital locations and admin area extents, that is fetched from the GO backend api, such as https://goadmin.ifrc.org/api/v2/country/?limit=9999.

See [the IBF repo](https://github.com/rodekruis/IBF/tree/main/data) for more information on how this data is fetched.

### country-data/glofas-loc

Location data for glofas stations per country in csv.
It's not clear where this data came from or how out of date it is. We'll need to figure out how to update this as well as add more countries.

### raster-data

Raster map data, such as population data.
Population data is fetched by scripts in [the IBF repo](https://github.com/rodekruis/IBF/tree/main/data).

### pipelines

Data ingested by the pipelines. Includes both actual source data (such as station to admin-area mappings) as well as mock data, needed for test runs. The pipeline code is in [the IBF repo](https://github.com/rodekruis/IBF/tree/main/data).

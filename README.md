# IBF seed and mock data repository

This repository contains all seed and mock data for the [IBF backend and pipelines](https://github.com/rodekruis/IBF).

## File size limit

Individual file sizes should be kept below 100mb. Above that [git-lfs](https://git-lfs.com/) would be needed, which has proved to come with problems for our setup.

## Data

Descriptions and notes for the stored data in the repo

### admin-areas

Admin areas (lvl 1 to 3) imported from [IBF v1 repo](https://github.com/rodekruis/IBF-system/tree/master/services/API-service/src/scripts/git-lfs). The source(s) are varied and they may be out of date. Not all countries are in the data.

Because of this, we'll need to move to admin-areas-gadm eventually.

### admin-areas-gadm

Admin areas (lvl 0 to 3) fetched from https://gadm.org/data.html 

Not all countries have admin level 3 though (i.e. Zimbabwe). We will need to move to using this data eventually, but we'll need different sources for admin 3 for some of the countries.

See [the IBF repo](https://github.com/rodekruis/IBF/tree/main/data) for more information on how this data is fetched.

### country-data/go-data

This includes various country-related data, such as hospital locations and admin area extents, that is fetched from the GO backend api, such as https://goadmin.ifrc.org/api/v2/country/?limit=9999.

See [the IBF repo](https://github.com/rodekruis/IBF/tree/main/data) for more information on how this data is fetched.

### country-data/glofas-loc

Location data for glofas stations per country in csv.
It's not clear where this data came from or how out of date it is. I heard we got in an email from someone. We'll need to figure out how to update this as well as add more countries.

### pipelines

Data ingested by the pipelines for test runs. The pipeline code is in [the IBF repo](https://github.com/rodekruis/IBF/tree/main/data).

### raster-data

Raster map data, such as population or disaster data.
Population data is fetched by scripts in [the IBF repo](https://github.com/rodekruis/IBF/tree/main/data).

Disaster data comes from mock runs of the pipeline. It was initially populated with mock data from IBFv1. [See here](https://github.com/rodekruis/IBF-system/blob/master/services/API-service/geoserver-volume/raster-files/README.md) for that initial source.

# IBF seed and mock data repository

This repository contains all seed and mock data for the [IBF backend and pipelines](https://github.com/rodekruis/IBF).

## File size limit

Individual file sizes should be kept below 100mb. Above that [git-lfs](https://git-lfs.com/) would be needed, which has proved to come with problems for our setup.

## Data

Descriptions and notes for the stored data in the repo

### admin-areas

Admin areas (lvl 1 to 3) imported from IBF. The source(s) are varied and they may be out of date. There are also only a few countries in the data.

Because of this, we'll need to move to admin-areas-gadm eventually.

### admin-areas-gadm

Admin areas (lvl 0 to 3) fetched from https://gadm.org/data.html 

Not all countries have admin level 3 though (i.e. Zimbabwe). We will need to move to using this data eventually, but we'll need different sources for admin 3 for some of the countries.

### country-data

This includes various country-related data, such as hospital locations and admin area extents.

### pipelines

Data ingested by the pipelines for test runs.

### raster-data

Raster map data, such as population or disaster data.

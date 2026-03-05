from scripts.shared.DataHelpers import target_countries_ISO_A3
from scripts.shared.DownloadHelpers import downloadBinaryObject
from pathlib import Path

baseUrl = "ftp://ftp.worldpop.org//GIS/Population_Density/Global_2000_2020_1km_UNadj/2020"

# Output dirs
baseOutputDir = "../../raster-data/population"
greyscaleOutputDir = Path(__file__).parent / f"{baseOutputDir}/greyscale/"
greyscaleOutputDir.mkdir(exist_ok=True)
rgbOutputDir = Path(__file__).parent / f"{baseOutputDir}/rgb/"
rgbOutputDir.mkdir(exist_ok=True)

def getUrl(country_ISO_A3):
    return f"{baseUrl}{country_ISO_A3.upper()}/{country_ISO_A3.lower()}_pd_2020_1km_UNadj.tif"

if __name__ == "__main__":
    # Dictionary of export file names, with the source URL
    urls = {f"{country}_population" : getUrl(country) for country in target_countries_ISO_A3}
    for name, url in urls.items():
        # Download the raw file
        binObject = downloadBinaryObject(url)
        # Convert and save it to PNG
        if binObject:
            output_path = greyscaleOutputDir / f"{name}.tif"
            output_path.parent.mkdir(parents=True, exist_ok=True)
            with open(output_path, "wb") as f:
                f.write(binObject)


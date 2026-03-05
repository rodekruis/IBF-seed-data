"""
This script fetches the population raster data from an external source.
The frontend uses PNG in EPSG:3857, so this script also converts the files for that step as well.
The geo metadata is saved as JSON.
"""

from shared.DataHelpers import target_countries_ISO_A3
from shared.DownloadHelpers import downloadBinaryObject
from shared.ImageHelpers import geotiffToArray
from pathlib import Path
import json
from PIL import Image


baseUrl = "ftp://ftp.worldpop.org//GIS/Population_Density/Global_2000_2020_1km_UNadj/2020/"

# Output dirs
baseOutputDir = "../raster-data/population"
greyscaleOutputDir = Path(__file__).parent / f"{baseOutputDir}/greyscale/"
greyscaleOutputDir.mkdir(parents=True, exist_ok=True)

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
            metaData, imgData = geotiffToArray(binObject)
            
            # Write metadata as JSON
            json_path = greyscaleOutputDir / f"{name}_metadata.json"
            with open(json_path, 'w') as f:
                json.dump(metaData, f, indent=2)
            
            # Write image as BW PNG
            bw_path = greyscaleOutputDir / f"{name}.png"
            bw_img = Image.fromarray(imgData, mode='L')
            bw_img.save(bw_path, optimize=True)
        else:
            print(f"Error: Failed to download data for {name} from {url}")


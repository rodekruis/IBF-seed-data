"""
This script colorizes grayscale PNGs that were produced by the GeoTIFF -> PNG flow in PopulationRasterFetcher.py
"""

from shared.DataHelpers import target_countries_ISO_A3
from shared.ImageHelpers import colorizeImageArray
from pathlib import Path
import json
from PIL import Image

# Output dirs
baseOutputDir = "../raster-data/population"
greyscaleOutputDir = Path(__file__).parent / f"{baseOutputDir}/greyscale/"
greyscaleOutputDir.mkdir(parents=True, exist_ok=True)
rgbaOutputDir = Path(__file__).parent / f"{baseOutputDir}/rgba/"
rgbaOutputDir.mkdir(parents=True, exist_ok=True)

metadataEnding = "_population_metadata.json"
rasterEnding = "_population.png"

if __name__ == "__main__":

    for country in target_countries_ISO_A3:

        # open the BW image from file as binary
        bwImageFile = greyscaleOutputDir  / f"{country.upper()}{rasterEnding}"
        print (f"Reading file from {bwImageFile}")
        if not bwImageFile.exists():
            print(f"Error: image file {bwImageFile} does not exist. Skipping {country}.")
            continue

        binObject = bwImageFile.read_bytes()

        # convert to color
        colorImageData = colorizeImageArray(binObject, [0,200,0,0], [100,100,255,255], log_scale=True)
        
        # Write image as color PNG
        color_path = rgbaOutputDir / f"{country}{rasterEnding}"
        color_img = Image.fromarray(colorImageData, mode='RGBA')
        color_img.save(color_path, optimize=True)

        # copy metadata file from the bw dir to the color dir
        metadataFile = greyscaleOutputDir / f"{country.upper()}{metadataEnding}"
        if metadataFile.exists():
            with open(metadataFile, 'r') as f:
                metadata = json.load(f)
            newMetadataFile = rgbaOutputDir / f"{country.upper()}{metadataEnding}"
            with open(newMetadataFile, 'w') as f:
                json.dump(metadata, f, indent=2)
        else:
            print(f"Warning: Metadata file {metadataFile} does not exist. Skipping metadata copy for {country}.")

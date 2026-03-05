"""
Helper functions relating to image processing
"""

import rasterio
from rasterio.io import MemoryFile
from rasterio.warp import calculate_default_transform, reproject, Resampling
from rasterio.transform import array_bounds
from rasterio.crs import CRS
import numpy as np
from PIL import Image
import io

"""
Colorize a grayscale image between two colors.
log_scale: whether or not to convert to a logarithmic scale.
"""
def colorizeImageArray(imgArray: bytes, color1 : tuple, color2: tuple, log_scale : bool):
    img = Image.open(io.BytesIO(imgArray))
    imgBW = np.array(img, dtype=np.float32)

    # optional: convert the data to logarithmic scale
    if log_scale:
        imgBW = np.log1p(imgBW)
        # Since values under 1 will be negative now, set these to 0
        imgBW[imgBW < 0] = 0  # log(1 + x) to handle zero values

    # Normalize to 0-1 range for color interpolation
    img_max = np.nanmax(imgBW)
    if img_max != 0:
        normalized = imgBW / img_max 
    
    # Create RGBA array - lerp between color1 and color2
    height, width = imgBW.shape
    img_array_rgba = np.zeros((height, width, 4), dtype=np.uint8)
    
    # Set alpha to 0 for pixels with values less than 1, else lerp between the two colors
    for i in range(height):
        for j in range(width):
            if imgBW[i, j] == 0:
                img_array_rgba[i, j] = [0, 0, 0, 0]
            else:
                # lerp between color1 and 2 based on the normalized value from the greyscale array
                n  = normalized[i, j]
                img_array_rgba[i, j, 0] = int(color1[0] * (1 - n) + color2[0] * n)
                img_array_rgba[i, j, 1] = int(color1[1] * (1 - n) + color2[1] * n)
                img_array_rgba[i, j, 2] = int(color1[2] * (1 - n) + color2[2] * n)
                img_array_rgba[i, j, 3] = int(color1[3] * (1 - n) + color2[3] * n)

    return img_array_rgba

"""
Convert a GeoTIFF to EPSG:3857, and return it as an array that is formatted to easily be written to a grayscale PNG.
Metadata is also returned.
"""
def geotiffToArray(tif_data: bytes):
    
    # Open the GeoTIFF from binary data
    with MemoryFile(tif_data) as memfile:
        with memfile.open() as src:
            # Reproject to EPSG:3857
            targetCrs = CRS.from_epsg(3857)            
            transform, width, height = calculate_default_transform(
                src.crs, targetCrs, src.width, src.height, *src.bounds
            )
            
            reprojData = np.empty((height, width), dtype=src.dtypes[0])
            
            reproject(
                source=rasterio.band(src, 1),
                destination=reprojData,
                src_transform=src.transform,
                src_crs=src.crs,
                dst_transform=transform,
                dst_crs=targetCrs,
                resampling=Resampling.bilinear
            )
            
            # Calculate the new bounds in 3857
            new_bounds = array_bounds(height, width, transform)
            
            # Get meta data
            geo_data = {
                'width': width,
                'height': height,
                'count': src.count,
                'crs': str(targetCrs),
                'transform': list(transform),
                'bounds': {
                    'left': new_bounds[0],
                    'bottom': new_bounds[1],
                    'right': new_bounds[2],
                    'top': new_bounds[3]
                },
                'res': (transform[0], -transform[4]),
                'scales': src.scales,
                'offsets': src.offsets
            }

            # This script only supports NoData values of zero or less
            if src.nodata is not None and src.nodata > 0:
                print(f"Error: Only NoData values of 0 or less are supported. NoData value: {src.nodata}.")
            
            # Normalize data to 0-255
            normData = (reprojData / reprojData.max()) * 255

            # Set 0 as the new nodata value, and make other data start at 1            
            for i in range(normData.shape[0]):
                for j in range(normData.shape[1]):
                    if normData[i, j] < 0:
                        normData[i, j] = 0
                    else:
                        normData[i, j] += 1
            
            # cast to uint8 for PNG output
            img_array_bw = normData.astype(np.uint8)
            return geo_data, img_array_bw
"""
This class is responsible for reading an image into memory as a 2D array of 1-byte pixels.
"""
from scipy import ndimage
from edge_improvement import PROJECT_ROOT
from edge_improvement.data.image import Image
import os


class ImageReader:

    @staticmethod
    def read(image_file, gray_scale=True):
        image_file = os.path.join(PROJECT_ROOT, image_file)
        return Image(ndimage.imread(image_file, flatten=gray_scale), image_file)


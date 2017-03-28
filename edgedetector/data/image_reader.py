"""
This class is responsible for reading an image into memory as a 2D array of 1-byte pixels.
"""
from scipy import ndimage
from edgedetector import IMAGES_DIR
import os

from edgedetector.data.image import Image


class ImageReader:

    @staticmethod
    def read(image_file, gray_scale=True):
        return Image(ndimage.imread(os.path.join(IMAGES_DIR, image_file), flatten=gray_scale), image_file)


"""
This class is responsible for reading an image into memory as a 2D array of 1-byte pixels.
"""
import os

from scipy import ndimage
from skimage import img_as_bool

from common.data.image import Image
from edge_improvement import PROJECT_ROOT


class ImageReader:
    @staticmethod
    def read(image_file, gray_scale=True):
        # TODO: Consider image denoising (see: http://scikit-image.org/docs/dev/auto_examples/filters/plot_denoise.html).
        image_file = os.path.join(PROJECT_ROOT, image_file)
        return Image(ndimage.imread(image_file, flatten=gray_scale), image_file)

    @staticmethod
    def read_binary(image_file):
        image_file = os.path.join(PROJECT_ROOT, image_file)
        return img_as_bool(ndimage.imread(image_file, mode='L'))

"""
This class is responsible for performing threshold operation based on the local neighbourhood of a pixel.
"""
from skimage.filters import threshold_local

from optimal_filter.solver.threshold.abstract_thresholding import AbstractThresholding


class LocalThresholding(AbstractThresholding):
    """
    Note that the local thresholding may be modified in many various ways (see the documentation of the threshold_local
    function used below).
    """

    def classify(self, image):
        threshold = threshold_local(image,
                                    3)  # TODO: Make this invocation more powerful by configuring additional parameters via the config file.
        return image > threshold

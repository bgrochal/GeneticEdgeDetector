"""
This class is responsible for performing threshold operation based on the Yen's method.
"""
from skimage.filters import threshold_yen

from optimal_filter.solver.threshold.abstract_thresholding import AbstractThresholding


class YenThresholding(AbstractThresholding):
    def classify(self, image):
        return super().classify_below(image, threshold_yen)

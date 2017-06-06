"""
This class is responsible for performing threshold operation based on the Otsu's method.
"""
from skimage.filters import threshold_otsu

from optimal_filter.solver.threshold.abstract_thresholding import AbstractThresholding


class OtsuThresholding(AbstractThresholding):
    def classify(self, image):
        return super().classify_below(image, threshold_otsu)

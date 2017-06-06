"""
This class is responsible for performing threshold operation based on the method of minimum.
"""
from skimage.filters import threshold_minimum

from optimal_filter.solver.threshold.abstract_thresholding import AbstractThresholding


class MinimumThresholding(AbstractThresholding):
    def classify(self, image):
        return super().classify_above(image, threshold_minimum)

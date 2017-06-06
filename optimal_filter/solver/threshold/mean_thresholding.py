"""
This class is responsible for performing threshold operation based on the mean of grayscale values.
"""
from skimage.filters import threshold_mean

from optimal_filter.solver.threshold.abstract_thresholding import AbstractThresholding


class MeanThresholding(AbstractThresholding):
    def classify(self, image):
        return super().classify_above(image, threshold_mean)

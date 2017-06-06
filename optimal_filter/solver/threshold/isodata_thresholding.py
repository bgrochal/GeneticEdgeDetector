"""
This class is responsible for performing threshold operation based on the ISODATA method.
"""
from skimage.filters import threshold_isodata

from optimal_filter.solver.threshold.abstract_thresholding import AbstractThresholding


class IsodataThresholding(AbstractThresholding):
    def classify(self, image):
        return super().classify_above(image, threshold_isodata)

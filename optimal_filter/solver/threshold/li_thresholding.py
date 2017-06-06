"""
This class is responsible for performing threshold operation based on the Li's Minimum Cross Entrophy method.
"""
from skimage.filters import threshold_li

from optimal_filter.solver.threshold.abstract_thresholding import AbstractThresholding


class LiThresholding(AbstractThresholding):
    def classify(self, image):
        return super().classify_above(image, threshold_li)

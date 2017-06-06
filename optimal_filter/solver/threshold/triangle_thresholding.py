"""
This class is responsible for performing threshold operation based on the triangle algorithm.
"""
from skimage.filters import threshold_triangle

from optimal_filter.solver.threshold.abstract_thresholding import AbstractThresholding


class TriangleThresholding(AbstractThresholding):
    def classify(self, image):
        return super().classify_above(image, threshold_triangle)

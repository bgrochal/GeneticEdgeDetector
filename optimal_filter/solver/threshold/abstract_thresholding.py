"""
This class defines basic interface for performing threshold operation (classifying gray-scale image to the binary one).
"""
from abc import ABC, abstractmethod


class AbstractThresholding(ABC):
    @abstractmethod
    def classify(self, image):
        raise NotImplementedError

    def classify_above(self, image, thresholding_function):
        threshold = thresholding_function(image)
        return image > threshold

    def classify_below(self, image, thresholding_function):
        threshold = thresholding_function(image)
        return image <= threshold

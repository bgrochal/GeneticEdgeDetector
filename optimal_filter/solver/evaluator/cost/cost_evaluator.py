"""
This class implements evaluation of genotype's cost function.
"""
import numpy as np
from scipy import ndimage


def get_convolved_image(image, dy_mask):
    dx_mask = np.rot90(dy_mask)

    dy_convolution = ndimage.convolve(image, dy_mask)
    dx_convolution = ndimage.convolve(image, dx_mask)

    # It is necessary to divide the convolution by the sum of elements in the mask to prevent convolved values by
    # exceeding the initial range (i.e. [0, 255] in this case).
    mask_values_sum = abs(np.sum(dy_mask))
    if mask_values_sum > 1:
        dy_convolution = dy_convolution / mask_values_sum
        dx_convolution = dx_convolution / mask_values_sum

    return np.sqrt((np.square(dy_convolution) + np.square(dx_convolution)) / 2)


class CostEvaluator:
    def __init__(self, image, target_deviation, threshold):
        self.image = image
        self.target_deviation = target_deviation
        self.threshold = threshold

    def evaluate(self, genotype):
        dy_mask = genotype.genes
        convolved_image = get_convolved_image(self.image, dy_mask)
        binary_image = self.threshold.classify(convolved_image)
        genotype.cost = abs(binary_image.std() - self.target_deviation)
        return genotype.cost

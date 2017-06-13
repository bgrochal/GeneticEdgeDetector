"""
This class implements evaluation of genotype's cost function.
"""
import numpy as np
from scipy import ndimage


def get_magnitude_grid(image, dy_mask):
    dx_mask = np.rot90(dy_mask)
    dy_convolution = ndimage.convolve(image, dy_mask) / np.sum(dy_mask)
    dx_convolution = ndimage.convolve(image, dx_mask) / np.sum(dy_mask)

    # Normalization of the convolution to the [0, 1] interval.
    # See: http://ics.p.lodz.pl/~adamwoj/WSFI/PO/3_wyklad_PO.pdf (slide 12).
    # TODO: Improve performance of this implementation (it takes definitely too long).
    min_value = dy_convolution.min()
    values_range = (dy_convolution.max() - min_value)
    for (i, j), value in np.ndenumerate(dy_convolution):
        dy_convolution[i][j] = (value - min_value) / values_range
    min_value = dx_convolution.min()
    values_range = (dx_convolution.max() - min_value)
    for (i, j), value in np.ndenumerate(dx_convolution):
        dx_convolution[i][j] = (value - min_value) / values_range
    return np.sqrt((np.square(dy_convolution) + np.square(dx_convolution)) / 2)


class CostEvaluator:
    def __init__(self, image, threshold, target_deviation):
        self.image = image
        self.threshold = threshold
        self.target_deviation = target_deviation

    def evaluate(self, genotype):
        dy_mask = genotype.genes
        magnitude_grid = get_magnitude_grid(self.image, dy_mask)
        binary_image = self.threshold.classify(magnitude_grid)
        genotype.cost = abs(binary_image.std() - self.target_deviation)
        return genotype.cost

"""
This class creates a population of individuals (so called gene pool) using Robert's Cross edge detection algorithm.
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage

from edge_improvement.solver.population.domain_initializer import DomainInitializer


class RobertsCrossInitializer(DomainInitializer):
    def __init__(self, population_size, image, similarity, threshold):
        super().__init__(population_size, image.shape, similarity, threshold)
        self.image = image

    def initialize(self):
        def compute_roberts_cross():
            cross_vertical = np.array([
                [0, 0, 0],
                [0, 1, 0],
                [0, 0, -1]
            ])
            cross_horizontal = np.array([
                [0, 0, 0],
                [0, 0, 1],
                [0, -1, 0]
            ])

            # Computing edge pixels using the Robert's Cross algorithm.
            vertical_matrix = ndimage.convolve(self.image.image_matrix, cross_vertical)
            horizontal_matrix = ndimage.convolve(self.image.image_matrix, cross_horizontal)
            roberts_cross = np.sqrt(np.square(vertical_matrix) + np.square(horizontal_matrix))

            # TODO: Is this the right technique?
            # Normalizing output of the Robert's Cross algorithm to the [0, 1] interval.
            normalizer = plt.Normalize(roberts_cross.min(), roberts_cross.max())
            return normalizer(roberts_cross)

        edge_image = compute_roberts_cross()
        edge_image = self.perform_threshold(edge_image)
        return [self._generate_random_genotype(edge_image) for _ in range(self.population_size)]

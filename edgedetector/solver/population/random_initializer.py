"""
This class creates a population of individuals (so called gene pool) with random genotypes centered around the enhanced
image represented by the dissimilarity matrix.
"""

from edgedetector.solver.population.initializer import Initializer


class RandomInitializer(Initializer):
    def __init__(self, population_size, image, similarity, threshold, dissimilarity_matrix):
        super().__init__(population_size, image.shape, similarity, threshold)
        self.dissimilarity_matrix = dissimilarity_matrix

    def initialize(self):
        return [self._generate_random_genotype(self.dissimilarity_matrix) for _ in range(self.population_size)]

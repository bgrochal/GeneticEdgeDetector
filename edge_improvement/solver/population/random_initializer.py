"""
This class creates a population of individuals (so called gene pool) with random genotypes centered around the enhanced
image represented by the dissimilarity matrix.
"""
from edge_improvement.solver.population.domain_initializer import DomainInitializer


class RandomInitializer(DomainInitializer):
    def __init__(self, population_size, image, similarity, threshold, dissimilarity_matrix):
        super().__init__(population_size, image.shape, similarity, threshold)
        self.dissimilarity_matrix = dissimilarity_matrix

    def initialize(self):
        dissimilarity_matrix_threshold = self.perform_threshold(self.dissimilarity_matrix)
        return [self._generate_random_genotype(dissimilarity_matrix_threshold) for _ in range(self.population_size)]

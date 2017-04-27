"""
This class creates a population of individuals (so called gene pool) with random genotypes centered around the enhanced
image represented by the dissimilarity matrix.
"""
import sys
from random import random

from edgedetector.solver.population.genotype import Genotype
from edgedetector.solver.population.initializer import Initializer


class RandomInitializer(Initializer):
    def __init__(self, genotype_shape, population_size, threshold, similarity, dissimilarity_matrix):
        self.genotype_shape = genotype_shape
        self.population_size = population_size
        self.threshold = threshold
        self.similarity = similarity
        self.dissimilarity_matrix = dissimilarity_matrix

    def initialize(self):
        def generate_random_genotype():
            initial_cost = sys.maxsize
            genotype = Genotype(self.genotype_shape, initial_cost)
            for i in range(genotype.genes.shape[0]):
                for j in range(genotype.genes.shape[1]):
                    if random() <= self.similarity:
                        genotype.genes[i][j] = True if self.dissimilarity_matrix[i][j] >= self.threshold else False
                    else:
                        genotype.genes[i][j] = 0
            return genotype

        return [generate_random_genotype() for _ in range(self.population_size)]

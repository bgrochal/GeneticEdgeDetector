"""
This class creates a population of individuals (so called gene pool) with random genotypes.
"""
from edgedetector.solver.population.genotype import Genotype
from edgedetector.solver.population.initializer import Initializer

import sys
from random import choice


class RandomInitializer(Initializer):
    def __init__(self, genotype_shape, population_size):
        self.genotype_shape = genotype_shape
        self.population_size = population_size

    def initialize(self):
        def generate_random_genotype():
            initial_cost = sys.maxsize
            genotype = Genotype(self.genotype_shape, initial_cost)
            for i in range(genotype.genes.shape[0]):
                for j in range(genotype.genes.shape[1]):
                    genotype.genes[i][j] = choice([0, 1])
            return genotype

        return [generate_random_genotype() for _ in range(self.population_size)]

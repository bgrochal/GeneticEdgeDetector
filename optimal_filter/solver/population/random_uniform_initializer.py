"""
This class generates a population of individuals (so called gene pool) with genotypes, which values are chosen randomly
from the uniform distribution on the [-1, 1] interval.
"""
import sys
from random import uniform

from common.solver.population.initializer import Initializer
from optimal_filter.solver.population.genotype import Genotype


class RandomUniformInitializer(Initializer):
    def __init__(self, population_size, genotype_shape):
        super().__init__(population_size, genotype_shape)

    def initialize(self):
        return [self._generate_random_genotype() for _ in range(self.population_size)]

    def _generate_random_genotype(self):
        genotype = Genotype(sys.maxsize)
        for i in range(self.genotype_shape[0]):
            for j in range(self.genotype_shape[1]):
                genotype.genes[i][j] = uniform(-1, 1)
        return genotype

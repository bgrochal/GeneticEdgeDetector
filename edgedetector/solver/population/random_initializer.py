"""
This class creates a population of individuals (so called gene pool) with random genotypes.
"""
from random import choice

from edgedetector.solver.population.genotype import Genotype
from edgedetector.solver.population.initializer import Initializer


class RandomInitializer(Initializer):
    def __init__(self, genotype_shape):
        self.genotype_shape = genotype_shape

    def initialize(self, population_size):
        def generate_random_genotype():
            genotype = Genotype(self.genotype_shape)
            for i in range(genotype.genes.shape[0]):
                for j in range(genotype.genes.shape[1]):
                    genotype.genes[i][j] = choice([0, 1])
            return genotype

        return [generate_random_genotype() for i in range(population_size)]

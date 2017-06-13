"""
This class defines crossover operation acting randomly on two chosen individuals (genotypes). This crossover operator
chooses one gene (i.e. a pair (x,y) of coordinates) and exchanges it between the offsprings.
"""
import sys
from random import random, randrange

import numpy as np

from common.solver.crossover.crossover import Crossover
from optimal_filter.solver.population.genotype import Genotype


class RandomSingleGeneCrossover(Crossover):
    def __init__(self, probability):
        super().__init__(probability)

    def cross(self, first_genotype, second_genotype):
        assert first_genotype.genes.shape == second_genotype.genes.shape

        first_offspring_genotype = Genotype(sys.maxsize)
        first_offspring_genotype.genes = np.copy(first_genotype.genes)
        second_offspring_genotype = Genotype(sys.maxsize)
        second_offspring_genotype.genes = np.copy(second_genotype.genes)

        if random() <= self.probability:
            genotype_shape = first_offspring_genotype.genes.shape
            gene_coordinate_x = randrange(genotype_shape[0])
            gene_coordinate_y = randrange(genotype_shape[1])

            first_offspring_genotype.genes[gene_coordinate_x][gene_coordinate_y] = \
                second_genotype.genes[gene_coordinate_x][gene_coordinate_y]
            second_offspring_genotype.genes[gene_coordinate_x][gene_coordinate_y] = \
                first_genotype.genes[gene_coordinate_x][gene_coordinate_y]

        return first_offspring_genotype, second_offspring_genotype

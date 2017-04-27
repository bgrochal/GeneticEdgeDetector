"""
This class defines crossover operation acting on two randomly chosen individuals (genotypes).
"""

import sys
from random import random, randrange

import numpy as np

from edgedetector.solver.crossover.crossover import Crossover
from edgedetector.solver.population.genotype import Genotype


class RandomCrossover(Crossover):
    def __init__(self, probability, site_range):
        self.probability = probability
        self.site_range = site_range
        self.initial_cost = sys.maxsize

    def cross(self, first_genotype, second_genotype):
        def _get_random_sites(shape):
            rows, columns = shape
            row_start = randrange(0, rows - self.site_range)
            row_end = randrange(row_start + 1, row_start + self.site_range + 1)
            column_start = randrange(0, columns - self.site_range)
            column_end = randrange(column_start + 1, column_start + self.site_range + 1)
            return (row_start, row_end), (column_start, column_end)

        assert first_genotype.genes.shape == second_genotype.genes.shape
        genotype_shape = first_genotype.genes.shape

        first_offspring_genotype = Genotype(genotype_shape, self.initial_cost)
        first_offspring_genotype.genes = np.copy(first_genotype.genes)
        second_offspring_genotype = Genotype(genotype_shape, self.initial_cost)
        second_offspring_genotype.genes = np.copy(second_genotype.genes)

        if random() <= self.probability:
            row_sites, column_sites = _get_random_sites(genotype_shape)
            first_offspring_genotype.genes[row_sites[0]:(row_sites[1] + 1), column_sites[0]:(column_sites[1] + 1)] = \
                second_genotype.genes[row_sites[0]:(row_sites[1] + 1), column_sites[0]:(column_sites[1] + 1)]
            second_offspring_genotype.genes[row_sites[0]:(row_sites[1] + 1), column_sites[0]:(column_sites[1] + 1)] = \
                first_genotype.genes[row_sites[0]:(row_sites[1] + 1), column_sites[0]:(column_sites[1] + 1)]
            return first_offspring_genotype, second_offspring_genotype

        return first_offspring_genotype, second_offspring_genotype

"""
This class defines crossover operation acting on two randomly chosen individuals (genotypes).
"""

import sys
from random import random, randrange

import numpy as np

from edge_improvement.solver.crossover.crossover import Crossover
from edge_improvement.solver.population.genotype import Genotype


class RandomCrossover(Crossover):
    def __init__(self, probability, row_site_range, column_site_range):
        self.probability = probability
        self.row_site_range = row_site_range
        self.column_site_range = column_site_range
        self.initial_cost = sys.maxsize

    def cross(self, first_genotype, second_genotype):
        def _get_random_sites(shape):
            rows, columns = shape
            row_start = randrange(0, max([rows - self.row_site_range, 0]))
            row_end = randrange(row_start + 1, min([row_start + self.row_site_range + 1, rows]))
            column_start = randrange(0, max([columns - self.column_site_range, 0]))
            column_end = randrange(column_start + 1, min([column_start + self.column_site_range + 1, columns]))
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

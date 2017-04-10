"""
This class defines crossover operation acting on two randomly chosen individuals (genotypes).
"""
from random import random, sample

import numpy as np

from edgedetector.solver.crossover.crossover import Crossover
from edgedetector.solver.population.genotype import Genotype


def _get_random_sites(shape):
    return sorted(sample(range(shape[0]), 2)), sorted(sample(range(shape[1]), 2))


class RandomCrossover(Crossover):
    def __init__(self, probability):
        self.probability = probability

    def cross(self, first_genotype, second_genotype):
        if random() <= self.probability:
            assert first_genotype.genes.shape == second_genotype.genes.shape
            genotype_shape = first_genotype.genes.shape

            first_offspring_genotype = Genotype(genotype_shape)
            first_offspring_genotype.genes = np.copy(first_genotype.genes)
            second_offspring_genotype = Genotype(genotype_shape)
            second_offspring_genotype.genes = np.copy(second_genotype.genes)

            x_sites, y_sites = _get_random_sites(genotype_shape)
            for x_site in x_sites:
                first_offspring_genotype.genes[x_site][y_sites[0]:y_sites[1]] = \
                    second_genotype.genes[x_site][y_sites[0]:y_sites[1]]
                second_offspring_genotype.genes[x_site][y_sites[0]:y_sites[1]] = \
                    first_genotype.genes[x_site][y_sites[0]:y_sites[1]]
            return first_offspring_genotype, second_offspring_genotype

        return first_genotype, second_genotype

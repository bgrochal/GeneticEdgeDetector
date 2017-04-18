"""
This class defines crossover operation acting on two randomly chosen individuals (genotypes).
"""
import os
from random import random, sample

import numpy as np

from edgedetector import RESOURCES_DIR
from edgedetector.config.config_reader import ConfigReader
from edgedetector.solver.crossover.crossover import Crossover
from edgedetector.solver.population.genotype import Genotype


def _get_random_sites(shape):
    return sorted(sample(range(shape[0]), 2)), sorted(sample(range(shape[1]), 2))


class RandomCrossover(Crossover):
    def __init__(self, probability):
        self.probability = probability
        self.initial_cost = ConfigReader(os.path.join(RESOURCES_DIR, 'config/config.yml')).\
            get_property(['misc', 'infinity'])

    def cross(self, first_genotype, second_genotype):
        if random() <= self.probability:
            assert first_genotype.genes.shape == second_genotype.genes.shape
            genotype_shape = first_genotype.genes.shape

            first_offspring_genotype = Genotype(genotype_shape, self.initial_cost)
            first_offspring_genotype.genes = np.copy(first_genotype.genes)
            second_offspring_genotype = Genotype(genotype_shape, self.initial_cost)
            second_offspring_genotype.genes = np.copy(second_genotype.genes)

            x_sites, y_sites = _get_random_sites(genotype_shape)
            first_offspring_genotype.genes[x_sites[0]:(x_sites[1] + 1), y_sites[0]:(y_sites[1] + 1)] = \
                second_genotype.genes[x_sites[0]:(x_sites[1] + 1), y_sites[0]:(y_sites[1] + 1)]
            second_offspring_genotype.genes[x_sites[0]:(x_sites[1] + 1), y_sites[0]:(y_sites[1] + 1)] = \
                first_genotype.genes[x_sites[0]:(x_sites[1] + 1), y_sites[0]:(y_sites[1] + 1)]
            return first_offspring_genotype, second_offspring_genotype

        return first_genotype, second_genotype

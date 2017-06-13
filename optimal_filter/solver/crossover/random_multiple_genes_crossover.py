"""
This class defines scattering-crossover operation acting randomly on two chosen individuals (genotypes). This crossover
operator draws a 9-bit string representing the genes, which undergo the replacement, i.e. if the i-th bit of the string
is 1, then the genotype[i/3][i%3] bit is exchanged between the offsprings.
"""
import random
import sys

import numpy as np

from common.solver.crossover.crossover import Crossover
from optimal_filter.solver.population.genotype import Genotype


class RandomMultipleGenesCrossover(Crossover):
    def __init__(self, probability):
        super().__init__(probability)

    def cross(self, first_genotype, second_genotype):
        def _get_bit(position, number):
            return (number & (1 << position)) != 0

        assert first_genotype.genes.shape == second_genotype.genes.shape

        first_offspring_genotype = Genotype(sys.maxsize)
        first_offspring_genotype.genes = np.copy(first_genotype.genes)
        second_offspring_genotype = Genotype(sys.maxsize)
        second_offspring_genotype.genes = np.copy(second_genotype.genes)

        random_bits = random.getrandbits(9)
        for i in range(9):
            if _get_bit(i, random_bits):
                gene_coordinate_x = int(i / 3)
                gene_coordinate_y = i % 3

                first_offspring_genotype.genes[gene_coordinate_x][gene_coordinate_y] = \
                    second_genotype.genes[gene_coordinate_x][gene_coordinate_y]
                second_offspring_genotype.genes[gene_coordinate_x][gene_coordinate_y] = \
                    first_genotype.genes[gene_coordinate_x][gene_coordinate_y]

        return first_offspring_genotype, second_offspring_genotype

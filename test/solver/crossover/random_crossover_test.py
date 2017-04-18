"""
This class contains tests for RandomCrossover class.
"""
from unittest import TestCase, mock

import numpy as np

from edgedetector.solver.crossover import random_crossover
from edgedetector.solver.crossover.random_crossover import RandomCrossover
from edgedetector.solver.population.genotype import Genotype


class RandomCrossoverTest(TestCase):
    def __init__(self, methodName='runTest'):
        super().__init__(methodName)
        self.random_crossover_probable = RandomCrossover(1.0)
        self.random_crossover_improbable = RandomCrossover(0.0)

    def setUp(self):
        self.first_genotype = Genotype((11, 5), 0)
        self.first_genotype.genes = np.array([
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0],
            [1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1],
            [1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1],
            [1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0]])

        self.second_genotype = Genotype((11, 5), 0)
        self.second_genotype.genes = np.array([
            [1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1],
            [1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1],
            [1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1],
            [1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1],
            [1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1]])

    @mock.patch.object(random_crossover, '_get_random_sites')
    def test_cross_improbable(self, mock_get_random_sites):
        mock_get_random_sites.return_value = [1, 3], [2, 9]

        first_offspring_genotype, second_offspring_genotype = \
            self.random_crossover_improbable.cross(self.first_genotype, self.second_genotype)
        np.testing.assert_array_equal(first_offspring_genotype.genes, self.first_genotype.genes)
        np.testing.assert_array_equal(second_offspring_genotype.genes, self.second_genotype.genes)

    @mock.patch.object(random_crossover, '_get_random_sites')
    def test_cross_probable(self, mock_get_random_sites):
        mock_get_random_sites.return_value = [1, 3], [2, 9]

        first_offspring_genotype, second_offspring_genotype = \
            self.random_crossover_probable.cross(self.first_genotype, self.second_genotype)
        np.testing.assert_array_equal(first_offspring_genotype.genes, np.array([
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0],  # first_genotype[1][0:2], second_genotype[1][2:10], first_genotype[1][10]
            [1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1],  # first_genotype[2][0:2], second_genotype[2][2:10], first_genotype[2][10]
            [1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1],  # first_genotype[3][0:2], second_genotype[3][2:10], first_genotype[3][10]
            [1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0]]))
        np.testing.assert_array_equal(second_offspring_genotype.genes, np.array([
            [1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1],
            [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],  # second_genotype[1][0:2], first_genotype[1][2:10], second_genotype[1][10]
            [1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1],  # second_genotype[2][0:2], first_genotype[2][2:10], second_genotype[2][10]
            [1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1],  # second_genotype[3][0:2], first_genotype[3][2:10], second_genotype[3][10]
            [1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1]]))

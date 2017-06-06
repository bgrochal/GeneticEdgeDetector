"""
This class contains tests for RandomInitializer class.
"""
from unittest import TestCase

import numpy as np

from edge_improvement.solver.population.random_initializer import RandomInitializer


class RandomInitializerTest(TestCase):
    def __init__(self, methodName='runTest'):
        super().__init__(methodName)
        self.population_size = 5
        self.shape = (10, 10)
        self.initializer = RandomInitializer(self.population_size, np.zeros(self.shape), 0.8, 0.1, np.zeros(self.shape))

    def test_initialize(self):
        population = self.initializer.initialize()
        self.assertIsInstance(population, list)
        self.assertEqual(len(population), self.population_size)

        for individual in population:
            self.assertEqual(individual.genes.shape, self.shape)

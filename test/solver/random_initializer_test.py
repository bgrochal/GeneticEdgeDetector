"""
This class contains tests for RandomInitializer class.
"""
from unittest import TestCase

import numpy as np

from edgedetector.solver.population.random_initializer import RandomInitializer


class RandomInitializerTest(TestCase):
    def __init__(self, methodName='runTest'):
        super().__init__(methodName)
        self.shape = (10, 10)
        self.initializer = RandomInitializer(self.shape, 5, 0.1, 0.8, np.zeros(self.shape))

    def test_initialize(self):
        population = self.initializer.initialize()
        self.assertIsInstance(population, list)
        self.assertEqual(len(population), 5)

        for individual in population:
            self.assertEqual(individual.genes.shape, (10, 10))

"""
This class contains tests for RandomMutation class.
"""
from unittest import TestCase, mock

import numpy as np

from edgedetector.solver.mutation import random_mutation
from edgedetector.solver.mutation.random_mutation import RandomMutation
from edgedetector.solver.population.genotype import Genotype


class RandomMutationTest(TestCase):
    def __init__(self, methodName='runTest'):
        super().__init__(methodName)
        self.randomMutation = RandomMutation(0.008)

    @mock.patch.object(random_mutation, '_get_random_list')
    def test_mutate(self, mock_get_random_list):
        mock_get_random_list.return_value = np.array([[0.0080, 0.0081], [0.5314, 0.0079]])
        genotype = Genotype((2, 2))

        for i in range(genotype.genes.shape[0]):
            for j in range(genotype.genes.shape[1]):
                self.assertEqual(genotype.genes[i][j], 0)

        self.randomMutation.mutate(genotype)

        self.assertEqual(genotype.genes[0][0], 1)
        self.assertEqual(genotype.genes[0][1], 0)
        self.assertEqual(genotype.genes[1][0], 0)
        self.assertEqual(genotype.genes[1][1], 1)

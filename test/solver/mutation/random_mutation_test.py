"""
This class contains tests for RandomMutation class.
"""
from unittest import TestCase, mock

import numpy as np

from edge_improvement.solver.mutation import random_mutation
from edge_improvement.solver.mutation.random_mutation import RandomMutation
from edge_improvement.solver.population.genotype import Genotype


class RandomMutationTest(TestCase):
    def __init__(self, methodName='runTest'):
        super().__init__(methodName)
        self.random_mutation = RandomMutation(0.008, 0)

    @mock.patch.object(random_mutation, '_get_random_list')
    def test_mutate(self, mock_get_random_list):
        mock_get_random_list.return_value = np.array([[0.0080, 0.0081], [0.5314, 0.0079]])
        genotype = Genotype((2, 2), 0)
        genotype.genes = np.array([[1, 0], [1, 1]])

        np.testing.assert_array_equal(genotype.genes, np.array([[1, 0], [1, 1]]))
        self.random_mutation.mutate(genotype)
        np.testing.assert_array_equal(genotype.genes, np.array([[0, 0], [1, 0]]))

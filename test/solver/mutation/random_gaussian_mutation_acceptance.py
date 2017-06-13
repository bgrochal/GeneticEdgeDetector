"""
This class contains acceptance tests for the truncated Gaussian (normal) random distribution generator.
"""
from unittest import TestCase

from matplotlib import pyplot as plt

from optimal_filter.solver.mutation import random_gaussian_mutation


class RandomGaussianMutationAcceptance(TestCase):
    def __init__(self, methodName='runTest'):
        super().__init__(methodName)
        self.generator = random_gaussian_mutation.truncated_gaussian_generator(-1, 1, 0, 0.33)

    def test_distribution(self):
        plt.hist(self.generator.rvs(10000), bins=11)
        plt.show()

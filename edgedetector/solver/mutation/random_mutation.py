"""
This class defines crossover operation acting on randomly chosen genes belonging to given genotype.
"""
from operator import xor
from random import random

import numpy as np

from edgedetector.solver.mutation.mutation import Mutation


def _get_random_list(shape):
    return np.array([[random() for _ in range(shape[1])] for _ in range(shape[0])])


class RandomMutation(Mutation):
    def __init__(self, probability):
        self.probability = probability

    def mutate(self, genotype):
        random_list = _get_random_list(genotype.genes.shape)

        for i in range(random_list.shape[0]):
            for j in range(random_list.shape[1]):
`                if random_list[i][j] <= self.probability and genotype.get_neighbours_count(i, j) >= 2:
                    genotype.genes[i][j] = xor(bool(genotype.genes[i][j]), bool(1))

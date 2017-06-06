"""
This class defines mutation operation acting on randomly chosen genes belonging to given genotype. This mutation
operator adds a randomly chosen number (from the uniform distribution on the [-1, 1] interval) to the value of chosen
gene (and truncates the new value to the [-1, 1] interval if necessary).
"""
from random import uniform

from common.solver.mutation.mutation import _get_random_list


class RandomUniformMutation:
    def __init__(self, probability):
        self.probability = probability

    def mutate(self, genotype):
        random_list = _get_random_list(genotype.genes.shape)
        for i in range(random_list.shape[0]):
            for j in range(random_list.shape[1]):
                if random_list[i][j] <= self.probability:
                    genotype.genes[i][j] += uniform(-1, 1)
                    genotype.genes[i][j] = min(genotype.genes[i][j], 1)
                    genotype.genes[i][j] = max(genotype.genes[i][j], -1)

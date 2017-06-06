"""
This class defines mutation operation acting on randomly chosen genes belonging to given genotype.
"""
from operator import xor

from common.solver.mutation.mutation import Mutation, _get_random_list


class RandomMutation(Mutation):
    def __init__(self, probability, neighbours_min):
        super().__init__(probability)
        self.neighbours_min = neighbours_min

    def mutate(self, genotype):
        random_list = _get_random_list(genotype.genes.shape)
        for i in range(random_list.shape[0]):
            for j in range(random_list.shape[1]):
                if random_list[i][j] <= self.probability.mutation_probability  and genotype.get_neighbours_count(i, j) >= self.neighbours_min:
                    genotype.genes[i][j] = xor(bool(genotype.genes[i][j]), bool(1))

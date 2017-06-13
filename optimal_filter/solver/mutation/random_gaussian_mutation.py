"""
This class defines mutation operation acting on randomly chosen genes belonging to given genotype. This mutation
operator adds a randomly chosen number (from the truncated Gaussian (normal) distribution on the [-1, 1] interval) to
the value of chosen gene (and truncates the new value to the [-1, 1] interval if necessary).
"""
from scipy import stats

from common.solver.mutation.mutation import Mutation, _get_random_list


def truncated_gaussian_generator(lower_bound, upper_bound, mean, scale):
    return stats.truncnorm((lower_bound - mean) / scale, (upper_bound - mean) / scale, loc=mean, scale=scale)


class RandomGaussianMutation(Mutation):
    def __init__(self, probability):
        super().__init__(probability)
        self.generator = truncated_gaussian_generator(-1, 1, 0, 0.33)

    def mutate(self, genotype):
        random_list = _get_random_list(genotype.genes.shape)
        for i in range(random_list.shape[0]):
            for j in range(random_list.shape[1]):
                if random_list[i][j] <= self.probability:
                    genotype.genes[i][j] += self.generator.rvs(1)
                    genotype.genes[i][j] = min(genotype.genes[i][j], 1.0)
                    genotype.genes[i][j] = max(genotype.genes[i][j], -1.0)

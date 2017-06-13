"""
This class is responsible for creating objects of subclasses of abstract class Mutation.
"""
from optimal_filter.solver.mutation.random_gaussian_mutation import RandomGaussianMutation
from optimal_filter.solver.mutation.random_uniform_mutation import RandomUniformMutation


class MutationFactory:
    @staticmethod
    def create(config, probability):
        class_ = config['class']

        if class_ == 'RandomUniformMutation':
            return RandomUniformMutation(probability.mutation_probability)
        if class_ == 'RandomGaussianMutation':
            return RandomGaussianMutation(probability.mutation_probability)
        raise NameError('Unknown class: {}'.format(class_))

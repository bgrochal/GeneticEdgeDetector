"""
This class is responsible for creating objects of subclasses of abstract class Initializer.
"""
from optimal_filter.solver.population.random_uniform_initializer import RandomUniformInitializer


class InitializerFactory:
    @staticmethod
    def create(config):
        size = config['initialSize']
        class_ = config['class']

        if class_ == 'RandomUniformInitializer':
            return RandomUniformInitializer(size, (3, 3))
        raise NameError('Unknown class: {}'.format(class_))

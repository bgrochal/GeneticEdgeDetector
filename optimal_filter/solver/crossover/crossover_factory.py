"""
This class is responsible for creating objects of subclasses of abstract class Crossover
"""
from optimal_filter.solver.crossover.random_crossover import RandomCrossover


class CrossoverFactory:
    @staticmethod
    def create(config, probability):
        class_ = config['class']

        if class_ == 'RandomCrossover':
            return RandomCrossover(probability)
        raise NameError("Unknown class: {}".format(class_))

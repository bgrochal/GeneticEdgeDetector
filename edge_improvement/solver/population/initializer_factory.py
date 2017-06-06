"""
This class is responsible for creating objects of subclasses of abstract
class Initializer
"""

from edge_improvement.solver.population.random_initializer import RandomInitializer
from edge_improvement.solver.population.roberts_cross_initializer import RobertsCrossInitializer


class InitializerFactory:
    @staticmethod
    def create(config, image, dissimilarity_matrix):
        size = config['initialSize']
        similarity = config['similarityToReference']
        threshold = config['threshold']
        class_ = config['class']

        if class_ == 'RandomInitializer':
            return RandomInitializer(size, image, similarity, threshold, dissimilarity_matrix)
        if class_ == 'RobertsCrossInitializer':
            return RobertsCrossInitializer(size, image, similarity, threshold)

        raise NameError('Unknown class: {}'.format(class_))

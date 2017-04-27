"""This class is responsible for creating objects of subclasses of abstract
class Initializer"""

from edgedetector.solver.population.random_initializer import RandomInitializer


class InitializerFactory:
    @staticmethod
    def create(config, image, dissimilarity_matrix):
        size = config['initialSize']
        class_ = config['class']
        if class_ == 'RandomInitializer':
            threshold = config['threshold']
            similarity = config['similarityToReference']
            return RandomInitializer(image.shape, size, threshold, similarity, dissimilarity_matrix)
        raise NameError('Unknown class: {}'.format(class_))

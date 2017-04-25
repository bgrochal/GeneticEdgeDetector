"""This class is responsible for creating objects of subclasses of abstract
class Initializer"""

from edgedetector.solver.population.random_initializer import RandomInitializer


class InitializerFactory:

    @staticmethod
    def create(config, shape):
        size = config['initialSize']
        class_ = config['class']
        if class_ == "RandomInitializer":
            return RandomInitializer(shape, size)
        raise NameError("Unknown class: {}".format(class_))

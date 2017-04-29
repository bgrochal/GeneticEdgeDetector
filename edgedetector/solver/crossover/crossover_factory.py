"""
This class is responsible for creating objects of subclasses of abstract
class Crossover
"""

from edgedetector.solver.crossover.random_crossover import RandomCrossover


class CrossoverFactory:
    @staticmethod
    def create(config):
        probability = config['probability']
        class_ = config['class']
        if class_ == "RandomCrossover":
            row_site_range = config['rowSiteRange']
            column_site_range = config['columnSiteRange']
            return RandomCrossover(probability, row_site_range, column_site_range)
        raise NameError("Unknown class: {}".format(class_))

"""
This class is responsible for creating objects of subclasses of abstract class Crossover
"""
from optimal_filter.solver.crossover.random_multiple_genes_crossover import RandomMultipleGenesCrossover
from optimal_filter.solver.crossover.random_single_gene_crossover import RandomSingleGeneCrossover


class CrossoverFactory:
    @staticmethod
    def create(config, probability):
        class_ = config['class']

        if class_ == 'RandomSingleGeneCrossover':
            return RandomSingleGeneCrossover(probability.crossover_probability)
        if class_ == 'RandomMultipleGenesCrossover':
            return RandomMultipleGenesCrossover(probability.crossover_probability)
        raise NameError('Unknown class: {}'.format(class_))

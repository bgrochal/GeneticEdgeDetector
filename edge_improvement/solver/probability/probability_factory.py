"""
This class is responsible for creating objects of class Probability or its subclasses.
"""
from edge_improvement.solver.probability.probability import IntelligentProbability, Probability


class ProbabilityFactory:
    @staticmethod
    def create(config):
        class_ = config['class']
        base_crossover_prob = config['crossover']
        base_mutation_prob = config['mutation']
        if class_ == "Default":
            return Probability(base_crossover_prob, base_mutation_prob)
        elif class_ == "Intelligent":
            return IntelligentProbability(base_crossover_prob, base_mutation_prob)
        raise NameError("Unknown class: {}".format(class_))

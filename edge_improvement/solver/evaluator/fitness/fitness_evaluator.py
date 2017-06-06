"""
This class implements evaluation of genotype's fitness function.
"""
from edge_improvement.solver.evaluator.evaluator import Evaluator


class FitnessEvaluator(Evaluator):
    def __init__(self, coefficient):
        self.worst_genotype = None
        self.coefficient = coefficient

    def evaluate(self, genotype):
        genotype.fitness = (self.worst_genotype.cost - genotype.cost) ** self.coefficient
        return genotype.fitness

"""
This class implements evaluation of genotype's dissimilarity cost function.
"""
from edge_improvement.solver.evaluator.cost.abstract_cost_evaluator import AbstractCostEvaluator


class DissimilarityCostEvaluator(AbstractCostEvaluator):
    def __init__(self, dissimilarity_matrix, config):
        self.dissimilarity_matrix = dissimilarity_matrix
        super().__init__()
        self.weight = config["dissimilarity"]

    def evaluate_window(self, row, column):
        if self.matrix[row, column]:
            return 0
        else:
            return self.dissimilarity_matrix[row, column]

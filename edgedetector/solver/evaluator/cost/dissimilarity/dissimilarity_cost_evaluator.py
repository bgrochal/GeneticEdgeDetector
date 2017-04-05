"""
This class implements evaluation of genotype's dissimilarity cost function.
"""
from edgedetector.solver.evaluator.cost.cost_evaluator import CostEvaluator


class DissimilarityCostEvaluator(CostEvaluator):

    def __init__(self, dissimilarity_matrix):
        self.dissimilarity_matrix = dissimilarity_matrix
        super().__init__()

    def evaluate_window(self, row, column):
        if self.matrix[row, column]:
            return 0
        else:
            return self.dissimilarity_matrix[row, column]

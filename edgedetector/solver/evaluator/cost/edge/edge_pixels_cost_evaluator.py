"""
This class implements evaluation of genotype's number of edge pixels cost function.
"""
from edgedetector.solver.evaluator.cost.cost_evaluator import CostEvaluator


class EdgePixelsCostEvaluator(CostEvaluator):

    def evaluate_window(self, row, column):
        return 1 if self.matrix[row, column] else 0

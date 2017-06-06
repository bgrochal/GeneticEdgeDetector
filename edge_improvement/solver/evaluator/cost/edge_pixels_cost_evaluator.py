"""
This class implements evaluation of genotype's number of edge pixels cost function.
"""
from edge_improvement.solver.evaluator.cost.abstract_cost_evaluator import AbstractCostEvaluator


class EdgePixelsCostEvaluator(AbstractCostEvaluator):
    def __init__(self, config):
        super().__init__()
        self.weight = config["edge"]

    def evaluate_window(self, row, column):
        return 1 if self.matrix[row, column] else 0

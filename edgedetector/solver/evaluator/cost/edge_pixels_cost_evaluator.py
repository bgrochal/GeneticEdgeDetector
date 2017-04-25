"""
This class implements evaluation of genotype's number of edge pixels cost function.
"""
from edgedetector.solver.evaluator.cost.abstract_cost_evaluator import AbstractCostEvaluator


class EdgePixelsCostEvaluator(AbstractCostEvaluator):

    def __init__(self, config):
        self.weight = config["edge"]
        super().__init__()

    def evaluate_window(self, row, column):
        return 1 if self.matrix[row, column] else 0

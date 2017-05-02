"""
This class implements evaluation of genotype's fragmentation cost function.
"""
from edgedetector.solver.evaluator.cost.abstract_cost_evaluator import AbstractCostEvaluator


class FragmentationCostEvaluator(AbstractCostEvaluator):

    def __init__(self, config):
        super().__init__()
        self.weight = config["fragmentation"]

    def evaluate_window(self, row, column):
        neighbours = self._find_neighbour_edge_pixels(row, column)
        if len(neighbours) == 0:
            return 1
        if len(neighbours) == 1:
            return 0.5
        return 0

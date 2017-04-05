"""
This class implements evaluation of genotype's fragmentation cost function.
"""
from edgedetector.solver.evaluator.cost.cost_evaluator import CostEvaluator


class FragmentationCostEvaluator(CostEvaluator):

    def evaluate_window(self, row, column):
        neighbours = self._find_neighbour_edge_pixels(row, column)
        if len(neighbours) == 0:
            return 1
        if len(neighbours) == 1:
            return 0.5
        return 0

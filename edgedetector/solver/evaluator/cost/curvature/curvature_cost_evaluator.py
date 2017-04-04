"""
This class implements evaluation of genotype's curvature cost function.
"""
from edgedetector.solver.evaluator.cost.cost_evaluator import CostEvaluator


class CurvatureCostEvaluator(CostEvaluator):

    def evaluate_window(self, row, column):
        if not self.matrix[row, column]:
            return 0
        neighbours = self._find_neighbour_edge_pixels(row, column)
        if len(neighbours) >= 3:
            # you can always draw line turning by more than 45 deg.
            return 1
        if len(neighbours) <= 1:
            return 0
        [(x1, y1), (x2, y2)] = neighbours
        if x1 != x2 and y1 != y2:
            return 1
        return 0.5



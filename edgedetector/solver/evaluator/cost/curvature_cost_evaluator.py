"""
This class implements evaluation of genotype's curvature cost function.
"""
from edgedetector.solver.evaluator.cost.abstract_cost_evaluator import AbstractCostEvaluator


class CurvatureCostEvaluator(AbstractCostEvaluator):

    def __init__(self, config):
        super().__init__()
        self.weight = config["curvature"]

    def evaluate_window(self, row, column):
        if not self.matrix[row, column]:
            return 0
        neighbours = self._find_neighbour_edge_pixels(row, column)
        if len(neighbours) >= 3:
            # you can always draw line turning by more than 45 deg.
            return 1
        if len(neighbours) <= 1:
            return 0
        [n1, n2] = neighbours
        if __class__.__turns_by_45((row, column), n1, n2):
            return 0.5
        if __class__.__inline((row, column), n1, n2):
            return 0
        return 1

    @staticmethod
    def __turns_by_45(center, p1, p2):
        return (__class__.__turns_by_45_from_line(center, p1, p2) or
                __class__.__turns_by_45_from_line(center, p2, p1))

    @staticmethod
    def __turns_by_45_from_line(center, p1, p2):
        """Checks if p2 turns by 45 degrees from line
        determined by center and p1"""
        (x1, y1) = center
        (x2, y2) = p1
        (x3, y3) = p2
        return ((x1 == x2 or y1 == y2) and
                x3 != x1 and y3 != y1 and x3 != x2 and y3 != y2)

    @staticmethod
    def __inline(p1, p2, p3):
        (x1, y1) = p1
        (x2, y2) = p2
        (x3, y3) = p3
        return ((x1 == x2 == x3) or                         # horizontal
                (y1 == y2 == y3) or                         # vertical
                ((x1 != x2 and x2 != x3 and x1 != x3) and   # diagonals
                 (y1 != y2 and y2 != y3 and y1 != y3)))

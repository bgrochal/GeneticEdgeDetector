"""
This class implements evaluation of genotype's thickness cost function.
"""
from queue import Queue

from edge_improvement.solver.evaluator.cost.abstract_cost_evaluator import AbstractCostEvaluator


class ThicknessCostEvaluator(AbstractCostEvaluator):
    def __init__(self, config):
        super().__init__()
        self.weight = config["thickness"]

    @staticmethod
    def neighbour_bfs(neighbours):
        if len(neighbours) == 0:
            return True

        visit_list = [False] * len(neighbours)
        q = Queue()
        q.put(neighbours[0])
        visit_list[0] = True

        while not q.empty():
            n_i, n_j = q.get()
            for i in range(0, len(neighbours)):
                c_i, c_j = neighbours[i]
                if not visit_list[i] and abs(n_i - c_i) <= 1 and abs(n_j - c_j) <= 1:
                    q.put((c_i, c_j))
                    visit_list[i] = True

        for i in range(0, len(neighbours)):
            if not visit_list[i]:
                return True

        return False

    def evaluate_window(self, row, column):
        if not self.matrix[row, column]:
            return 0

        neighbour = self._find_neighbour_edge_pixels(row, column)
        if self.neighbour_bfs(neighbour):
            return 0
        else:
            return 1

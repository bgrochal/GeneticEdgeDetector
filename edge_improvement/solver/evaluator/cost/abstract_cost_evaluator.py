"""
This class contains common interface for computing cost functions.
"""
from abc import abstractmethod

import numpy as np

from common.solver.evaluator.evaluator import Evaluator


class AbstractCostEvaluator(Evaluator):
    def __init__(self):
        self.matrix = None
        self.weight = 0

    def evaluate(self, genotype):
        self.matrix = __class__._add_guard_ring(genotype.genes)
        rows, columns = genotype.genes.shape
        cost = 0
        for row in range(rows):
            for column in range(columns):
                cost += self.evaluate_window(row, column)
        return self.weight * cost

    @abstractmethod
    def evaluate_window(self, row, column):
        raise NotImplementedError

    @staticmethod
    def _add_guard_ring(matrix):
        ring = np.zeros(tuple(s + 2 for s in matrix.shape))
        ring[tuple((slice(1, -1) for _ in matrix.shape))] = matrix
        return ring

    def _find_neighbour_edge_pixels(self, row, column):
        neighbour_edge_pixels = []
        for i in range(row - 1, row + 2):
            for j in range(column - 1, column + 2):
                if i != row and j != column and self.matrix[i, j]:
                    neighbour_edge_pixels.append((i, j))
        return neighbour_edge_pixels

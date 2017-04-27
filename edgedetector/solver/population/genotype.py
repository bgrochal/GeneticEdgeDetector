"""
This class represents single chromosome of an individual, which states for a solution of the problem.
"""
import numpy as np


class Genotype:
    def __init__(self, image_shape, cost, fitness=0):
        self.genes = np.zeros(image_shape, dtype=bool)
        self.cost = cost
        self.fitness = fitness

    def get_neighbours_count(self, row, column):
        max_rows, max_columns = self.genes.shape
        row_start = max([row - 1, 0])
        row_end = min([row + 1, max_rows - 1])
        column_start = max([column - 1, 0])
        column_end = min([column + 1, max_columns - 1])

        neighbours = 0
        for i in range(row_start, row_end + 1):
            for j in range(column_start, column_end + 1):
                if self.genes[i][j]:
                    neighbours += 1
        return neighbours

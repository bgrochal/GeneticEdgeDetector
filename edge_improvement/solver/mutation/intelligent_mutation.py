"""
This class defines "intelligent" / "knowledge augmented" mutation operator, which explores local edge structure before
performing changes on given pixel.
"""
from operator import xor
from random import random, sample

import numpy as np

from common.solver.mutation.mutation import Mutation, _get_random_list

#           LEFT    CENTER    RIGHT
# TOP     (-1,  1)  (0,  1)  (1,  1)
# MIDDLE  (-1,  0)  (0,  0)  (1,  0)
# BOTTOM  (-1, -1)  (0, -1)  (1, -1)

BOTTOM_LEFT = (-1, -1)
MIDDLE_LEFT = (-1, 0)
TOP_LEFT = (-1, 1)

BOTTOM_CENTER = (0, -1)
MIDDLE_CENTER = (0, 0)
TOP_CENTER = (0, 1)

BOTTOM_RIGHT = (1, -1)
MIDDLE_RIGHT = (1, 0)
TOP_RIGHT = (1, 1)

# Mutation strategies defined for each configuration (either valid or invalid, with respect to the rotation by 90 degs),
# where examined pixel has exactly one edge-pixel neighbour.
mutation_strategies_one_neighbour = [
    # o x o
    # o x o
    # o o o
    {
        'pattern': [TOP_CENTER, MIDDLE_CENTER],
        'rotations': 4,
        'flips': [{'flip': [BOTTOM_CENTER], 'probability': 0.45}, {'flip': [BOTTOM_LEFT], 'probability': 0.2},
                  {'flip': [BOTTOM_RIGHT], 'probability': 0.2}, {'flip': [MIDDLE_CENTER], 'probability': 0.1},
                  {'flip': [TOP_CENTER, MIDDLE_CENTER], 'probability': 0.05}]
    },

    # x o o
    # o x o
    # o o o
    {
        'pattern': [TOP_LEFT, MIDDLE_CENTER],
        'rotations': 4,
        'flips': [{'flip': [BOTTOM_RIGHT], 'probability': 0.45}, {'flip': [MIDDLE_RIGHT], 'probability': 0.2},
                  {'flip': [BOTTOM_CENTER], 'probability': 0.2}, {'flip': [MIDDLE_CENTER], 'probability': 0.1},
                  {'flip': [TOP_LEFT, MIDDLE_CENTER], 'probability': 0.05}]
    }
]

# Mutation strategies defined for each configuration (either valid or invalid, with respect to the rotation by 90 degs),
# where examined pixel has exactly two edge-pixel neighbours.
mutation_strategies_two_neighbours = [
    # x x o
    # o x o
    # o o o
    {
        'pattern': [TOP_LEFT, TOP_CENTER, MIDDLE_CENTER],
        'rotations': 4,
        'flips': [{'flip': [TOP_CENTER], 'probability': 0.35}, {'flip': [TOP_LEFT], 'probability': 0.35},
                  {'flip': [MIDDLE_CENTER], 'probability': 0.25},
                  {'flip': [TOP_LEFT, TOP_CENTER, MIDDLE_CENTER], 'probability': 0.05}]
    },

    # o x x
    # o x o
    # o o o
    {
        'pattern': [TOP_CENTER, TOP_RIGHT, MIDDLE_CENTER],
        'rotations': 4,
        'flips': [{'flip': [TOP_CENTER], 'probability': 0.35}, {'flip': [TOP_RIGHT], 'probability': 0.35},
                  {'flip': [MIDDLE_CENTER], 'probability': 0.25},
                  {'flip': [TOP_CENTER, TOP_RIGHT, MIDDLE_CENTER], 'probability': 0.05}]
    },

    # x o x
    # o x o
    # o o o
    {
        'pattern': [TOP_LEFT, TOP_RIGHT, MIDDLE_CENTER],
        'rotations': 4,
        'flips': [{'flip': [TOP_RIGHT], 'probability': 0.25}, {'flip': [TOP_LEFT], 'probability': 0.25},
                  {'flip': [TOP_CENTER, MIDDLE_CENTER], 'probability': 0.15},
                  {'flip': [MIDDLE_LEFT, TOP_LEFT], 'probability': 0.15},
                  {'flip': [MIDDLE_RIGHT, TOP_RIGHT], 'probability': 0.15},
                  {'flip': [TOP_LEFT, TOP_RIGHT, MIDDLE_CENTER], 'probability': 0.05}]
    },

    # x o o
    # o x o
    # o x o
    {
        'pattern': [TOP_LEFT, BOTTOM_CENTER, MIDDLE_CENTER],
        'rotations': 4,
        'flips': [{'flip': [TOP_LEFT], 'probability': 0.25}, {'flip': [BOTTOM_CENTER], 'probability': 0.25},
                  {'flip': [TOP_LEFT, TOP_CENTER], 'probability': 0.2},
                  {'flip': [BOTTOM_CENTER, BOTTOM_RIGHT], 'probability': 0.2},
                  {'flip': [MIDDLE_LEFT, MIDDLE_CENTER], 'probability': 0.05},
                  {'flip': [TOP_LEFT, BOTTOM_CENTER, MIDDLE_CENTER], 'probability': 0.05}]
    },

    # o o x
    # o x o
    # o x o
    {
        'pattern': [BOTTOM_CENTER, TOP_RIGHT, MIDDLE_CENTER],
        'rotations': 4,
        'flips': [{'flip': [TOP_RIGHT], 'probability': 0.25}, {'flip': [BOTTOM_CENTER], 'probability': 0.25},
                  {'flip': [TOP_CENTER, TOP_RIGHT], 'probability': 0.2},
                  {'flip': [BOTTOM_LEFT, BOTTOM_CENTER], 'probability': 0.2},
                  {'flip': [MIDDLE_CENTER, MIDDLE_RIGHT], 'probability': 0.05},
                  {'flip': [BOTTOM_CENTER, TOP_RIGHT, MIDDLE_CENTER], 'probability': 0.05}]
    },

    # o x o
    # x x o
    # o o o
    {
        'pattern': [MIDDLE_LEFT, TOP_CENTER, MIDDLE_CENTER],
        'rotations': 4,
        'flips': [{'flip': [MIDDLE_LEFT], 'probability': 0.35}, {'flip': [TOP_CENTER], 'probability': 0.35},
                  {'flip': [MIDDLE_CENTER], 'probability': 0.25},
                  {'flip': [MIDDLE_LEFT, TOP_CENTER, MIDDLE_CENTER], 'probability': 0.05}]
    },

    # o x o
    # o x o
    # o x o
    {
        'pattern': [BOTTOM_CENTER, TOP_CENTER, MIDDLE_CENTER],
        'rotations': 2,
        'flips': [{'flip': [TOP_CENTER, TOP_RIGHT], 'probability': 0.15},
                  {'flip': [TOP_LEFT, TOP_CENTER], 'probability': 0.15},
                  {'flip': [BOTTOM_LEFT, BOTTOM_CENTER], 'probability': 0.15},
                  {'flip': [BOTTOM_CENTER, BOTTOM_RIGHT], 'probability': 0.15},
                  {'flip': [MIDDLE_CENTER, MIDDLE_RIGHT], 'probability': 0.1},
                  {'flip': [MIDDLE_LEFT, MIDDLE_CENTER], 'probability': 0.1},
                  {'flip': [TOP_LEFT, TOP_CENTER, BOTTOM_CENTER, BOTTOM_RIGHT], 'probability': 0.05},
                  {'flip': [BOTTOM_LEFT, BOTTOM_CENTER, TOP_CENTER, TOP_RIGHT], 'probability': 0.05},
                  {'flip': [], 'probability': 0.05},
                  {'flip': [BOTTOM_CENTER, TOP_CENTER, MIDDLE_CENTER], 'probability': 0.05}]
    },

    # x o o
    # o x o
    # o o x
    {
        'pattern': [TOP_LEFT, BOTTOM_RIGHT, MIDDLE_CENTER],
        'rotations': 2,
        'flips': [{'flip': [TOP_LEFT, TOP_CENTER], 'probability': 0.15},
                  {'flip': [BOTTOM_CENTER, BOTTOM_RIGHT], 'probability': 0.15},
                  {'flip': [MIDDLE_LEFT, TOP_LEFT], 'probability': 0.15},
                  {'flip': [BOTTOM_RIGHT, MIDDLE_RIGHT], 'probability': 0.15},
                  {'flip': [MIDDLE_LEFT, TOP_LEFT, BOTTOM_RIGHT, MIDDLE_RIGHT], 'probability': 0.1},
                  {'flip': [TOP_LEFT, TOP_CENTER, BOTTOM_CENTER, BOTTOM_RIGHT], 'probability': 0.1},
                  {'flip': [BOTTOM_LEFT, TOP_LEFT, BOTTOM_RIGHT, TOP_RIGHT], 'probability': 0.1},
                  {'flip': [], 'probability': 0.05},
                  {'flip': [TOP_LEFT, BOTTOM_RIGHT, MIDDLE_CENTER], 'probability': 0.05}]
    }
]

# Mutation strategies defined for configurations suggested in the article, where examined pixel has exactly three edge-
# pixel neighbours. For other configurations the mutation algorithm takes one pixel with True value randomly and flips
# its value (to False).
mutation_strategies_three_neighbours = [
    # o x x
    # o x o
    # x o o
    {
        'pattern': [BOTTOM_LEFT, TOP_CENTER, TOP_RIGHT, MIDDLE_CENTER],
        'rotations': 4,
        'flips': [{'flip': [TOP_CENTER], 'probability': 0.5}, {'flip': [TOP_RIGHT], 'probability': 0.45},
                  {'flip': [BOTTOM_LEFT, TOP_CENTER, TOP_RIGHT, MIDDLE_CENTER], 'probability': 0.05}]
    },

    # x x o
    # o x o
    # o o x
    {
        'pattern': [TOP_LEFT, TOP_CENTER, BOTTOM_RIGHT, MIDDLE_CENTER],
        'rotations': 4,
        'flips': [{'flip': [TOP_CENTER], 'probability': 0.5}, {'flip': [TOP_LEFT], 'probability': 0.45},
                  {'flip': [TOP_LEFT, TOP_CENTER, BOTTOM_RIGHT, MIDDLE_CENTER], 'probability': 0.05}]
    },

    # x x o
    # o x o
    # x o o
    {
        'pattern': [BOTTOM_LEFT, TOP_LEFT, TOP_CENTER, MIDDLE_CENTER],
        'rotations': 4,
        'flips': [{'flip': [TOP_LEFT], 'probability': 0.5}, {'flip': [TOP_CENTER], 'probability': 0.45},
                  {'flip': [BOTTOM_LEFT, TOP_LEFT, TOP_CENTER, MIDDLE_CENTER], 'probability': 0.05}]
    },

    # o x x
    # o x o
    # o o x
    {
        'pattern': [TOP_CENTER, BOTTOM_RIGHT, TOP_RIGHT, MIDDLE_CENTER],
        'rotations': 4,
        'flips': [{'flip': [TOP_RIGHT], 'probability': 0.5}, {'flip': [TOP_CENTER], 'probability': 0.45},
                  {'flip': [TOP_CENTER, BOTTOM_RIGHT, TOP_RIGHT, MIDDLE_CENTER], 'probability': 0.05}]
    },

    # o x o
    # o x o
    # x x o
    {
        'pattern': [BOTTOM_LEFT, BOTTOM_CENTER, TOP_CENTER, MIDDLE_CENTER],
        'rotations': 4,
        'flips': [{'flip': [BOTTOM_LEFT], 'probability': 0.5}, {'flip': [BOTTOM_CENTER], 'probability': 0.45},
                  {'flip': [BOTTOM_LEFT, BOTTOM_CENTER, TOP_CENTER, MIDDLE_CENTER], 'probability': 0.05}]
    },

    # o x o
    # o x o
    # o x x
    {
        'pattern': [BOTTOM_CENTER, TOP_CENTER, BOTTOM_RIGHT, MIDDLE_CENTER],
        'rotations': 4,
        'flips': [{'flip': [BOTTOM_RIGHT], 'probability': 0.5}, {'flip': [BOTTOM_CENTER], 'probability': 0.45},
                  {'flip': [BOTTOM_CENTER, TOP_CENTER, BOTTOM_RIGHT, MIDDLE_CENTER], 'probability': 0.05}]
    },

    # x o o
    # x x o
    # x o o
    {
        'pattern': [BOTTOM_LEFT, MIDDLE_LEFT, TOP_LEFT, MIDDLE_CENTER],
        'rotations': 4,
        'flips': [{'flip': [MIDDLE_CENTER], 'probability': 0.5}, {'flip': [MIDDLE_LEFT], 'probability': 0.45},
                  {'flip': [BOTTOM_LEFT, MIDDLE_LEFT, TOP_LEFT, MIDDLE_CENTER], 'probability': 0.05}]
    },

    # x x o
    # x x o
    # o o o
    {
        'pattern': [MIDDLE_LEFT, TOP_LEFT, TOP_CENTER, MIDDLE_CENTER],
        'rotations': 4,
        'flips': [{'flip': [MIDDLE_LEFT, TOP_CENTER], 'probability': 0.2},
                  {'flip': [MIDDLE_LEFT, TOP_LEFT], 'probability': 0.2},
                  {'flip': [TOP_LEFT, TOP_CENTER], 'probability': 0.2},
                  {'flip': [TOP_LEFT, MIDDLE_CENTER], 'probability': 0.1},
                  {'flip': [TOP_CENTER, MIDDLE_CENTER], 'probability': 0.1},
                  {'flip': [MIDDLE_LEFT, MIDDLE_CENTER], 'probability': 0.1},
                  {'flip': [], 'probability': 0.05},
                  {'flip': [MIDDLE_LEFT, TOP_LEFT, TOP_CENTER, MIDDLE_CENTER], 'probability': 0.05}]
    }
]


class IntelligentMutation(Mutation):
    def __init__(self, probability):
        super().__init__(probability)

    def mutate(self, genotype):
        # Acts the intelligent mutation operator on given pixel represented by coordinates: (row, column).
        def perform_mutation(row, column):
            # Returns 3x3 boolean matrix representing a structure of pixels represented by the 'pattern' list,
            def get_strategy_matrix(mutation_pattern):
                matrix = np.zeros((3, 3), dtype=bool)
                for point in mutation_pattern:
                    matrix[1 + point[0]][1 + point[1]] = True
                return matrix

            # Return 3x3 boolean matrix representing a structure of pixels after performing mutation (defined by some
            # element of the 'flips' list) on a matrix defined by the 'pattern' list.
            def get_mutated_matrix(strategy):
                matrix = get_strategy_matrix(strategy['pattern'])
                current_probability = 0
                probability = random()

                for flip_strategy in strategy['flips']:
                    current_probability += flip_strategy['probability']
                    if probability <= current_probability:
                        for flip in flip_strategy['flip']:
                            matrix[flip[0] + 1, flip[1] + 1] = xor(bool(matrix[flip[0] + 1, flip[1]] + 1), bool(1))
                        return matrix

            # Returns 3x3 matrix (padded with zeros if necessary) containing a neighbourhood of requested pixel.
            def get_neighbourhood(first_row, last_row, first_column, last_column):
                neighbourhood_window = np.zeros((3, 3))
                neighbourhood_window[first_row:last_row, first_column:last_column] = \
                    genotype.genes[max([row - 1, 0]):min([row + 2, genotype.genes.shape[0]]),
                    max([column - 1, 0]):min([column + 2, genotype.genes.shape[1]])]
                return neighbourhood_window

            # Rotates given matrix by 90 degrees as many times, as defined by the rotations parameter.
            def rotate(matrix, rotations):
                for _ in range(rotations):
                    matrix = np.rot90(matrix)
                return matrix

            # Looks up given list of strategies and performs one of these; then returns a modified neighbourhood window
            # (or None if mutation was not performed).
            def lookup_strategies(strategies):
                first_row = 0
                first_column = 0
                last_row = 3
                last_column = 3

                if row == 0:
                    first_row = 1
                if column == 0:
                    first_column = 1
                if row == genotype.genes.shape[0] - 1:
                    last_row = 2
                if column == genotype.genes.shape[1] - 1:
                    last_column = 2

                neighbourhood_matrix = get_neighbourhood(first_row, last_row, first_column, last_column)
                for strategy in strategies:
                    strategy_matrix = get_strategy_matrix(strategy['pattern'])
                    for rotations_count in range(strategy['rotations']):
                        if np.array_equal(neighbourhood_matrix, strategy_matrix):
                            mutated_matrix = rotate(get_mutated_matrix(strategy), rotations_count)
                            if mutated_matrix is not None:
                                genotype.genes[max([row - 1, 0]):min([row + 2, genotype.genes.shape[0]]),
                                max([column - 1, 0]):min([column + 2, genotype.genes.shape[1]])] = \
                                    mutated_matrix[first_row:last_row, first_column:last_column]
                            return mutated_matrix
                        strategy_matrix = rotate(strategy_matrix, 1)

            neighbours_count = genotype.get_neighbours_count(row, column)
            mutated_window = None

            if neighbours_count == 0:
                return
            if neighbours_count == 1:
                mutated_window = lookup_strategies(mutation_strategies_one_neighbour)
                assert mutated_window is not None
            if neighbours_count == 2:
                mutated_window = lookup_strategies(mutation_strategies_two_neighbours)
                assert mutated_window is not None
            if neighbours_count == 3:
                mutated_window = lookup_strategies(mutation_strategies_three_neighbours)
            # Performs random mutation which is equivalent to change value of one random pixel from True to False.
            if neighbours_count >= 4 or (neighbours_count == 3 and mutated_window is None):
                true_values = []
                for window_row in range(max([row - 1, 0]), min([row + 2, genotype.genes.shape[0]])):
                    for window_column in range(max([column - 1, 0]), min([column + 2, genotype.genes.shape[1]])):
                        if genotype.genes[window_row][window_column]:
                            true_values.append((window_row, window_column))
                position = sample(range(len(true_values)), 1)
                genotype.genes[true_values[position[0]][0], true_values[position[0]][1]] = False

        # Getting 2D array of random numbers corresponding to the probability of mutation
        random_list = _get_random_list(genotype.genes.shape)
        for i in range(random_list.shape[0]):
            for j in range(random_list.shape[1]):
                if random_list[i][j] <= self.probability and genotype.genes[i][j]:
                    perform_mutation(i, j)

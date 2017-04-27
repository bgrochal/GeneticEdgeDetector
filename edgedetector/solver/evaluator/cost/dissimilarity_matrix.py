"""
This class represents the enhanced image, i. e. a matrix of pixels wherein each pixel value is proportional to the
degree of region dissimilarity that exists at that pixel site.
"""

import numpy as np

# (-1, 1)    (0, 1)    (1, 1)
# (-1, 0)    (0, 0)    (1, 0)
# (-1,-1)    (0,-1)    (1,-1)
dissimilarity_patterns = [
    # o o o
    # x x o
    # o o x
    # o o
    {
        "darker": [(-1, -2), (-1, -1), (0, -2), (0, -1)],
        "border": [(-1, 0), (1, -1), (0, 0)],
        "lighter": [(-1, 1), (0, 1), (1, 0), (1, 1)],
        "shift": [(-1, 0), (1, 0), (0, -1), (0, 1)]
    },

    # o o x o
    # o o x o
    #   x o o
    {
        "darker": [(-2, 0), (-2, 1), (-1, 0), (-1, 1)],
        "border": [(-1, -1), (0, 1), (0, 0)],
        "lighter": [(0, -1), (1, -1), (1, 0), (1, 1)],
        "shift": [(-1, 0), (1, 0), (0, -1), (0, 1)]
    },

    #   o o
    # x o o
    # o x x
    # o o o
    {
        "darker": [(0, 1), (0, 2), (1, 1), (1, 2)],
        "border": [(-1, 1), (1, 0), (0, 0)],
        "lighter": [(-1, -1), (-1, 0), (0, -1), (1, -1)],
        "shift": [(-1, 0), (1, 0), (0, -1), (0, 1)]
    },

    # o o x
    # o x o o
    # o x o o
    {
        "darker": [(1, -1), (1, 0), (2, -1), (2, 0)],
        "border": [(0, -1), (1, 1), (0, 0)],
        "lighter": [(-1, -1), (-1, 0), (-1, 1), (0, 1)],
        "shift": [(-1, 0), (1, 0), (0, -1), (0, 1)]
    },

    # o o
    # o o x
    # x x o
    # o o o
    {
        "darker": [(-1, 1), (-1, 2), (0, 1), (0, 2)],
        "border": [(-1, 0), (1, 1), (0, 0)],
        "lighter": [(-1, -1), (0, -1), (1, -1), (1, 0)],
        "shift": [(-1, 0), (1, 0), (0, -1), (0, 1)]
    },

    # o x o o
    # o x o o
    # o o x
    {
        "darker": [(1, 0), (1, 1), (2, 0), (2, 1)],
        "border": [(0, 1), (1, -1), (0, 0)],
        "lighter": [(-1, -1), (-1, 0), (-1, 1), (0, -1)],
        "shift": [(-1, 0), (1, 0), (0, -1), (0, 1)]
    },

    # o o o
    # o x x
    # x o o
    #   o o
    {
        "darker": [(0, -2), (0, -1), (1, -2), (1, -1)],
        "border": [(-1, -1), (1, 0), (0, 0)],
        "lighter": [(-1, 0), (-1, 1), (0, 1), (1, 1)],
        "shift": [(-1, 0), (1, 0), (0, -1), (0, 1)]
    },

    #   x o o
    # o o x o
    # o o x o
    {
        "darker": [(-2, -1), (-2, 0), (-1, -1), (-1, 0)],
        "border": [(-1, 1), (0, -1), (0, 0)],
        "lighter": [(0, 1), (1, -1), (1, 0), (1, 1)],
        "shift": [(-1, 0), (1, 0), (0, -1), (0, 1)]
    },

    #     o
    #   o o x
    # o o x o o
    #   x o o
    #     o
    {
        "darker": [(0, -2), (0, -1), (1, -1), (1, 0), (2, 0)],
        "border": [(-1, -1), (1, 1), (0, 0)],
        "lighter": [(-2, 0), (-1, 0), (-1, 1), (0, 1), (0, 2)],
        "shift": [(1, -1), (-1, 1)]
    },

    #     o
    #   x o o
    # o o x o o
    #   o o x
    #     o
    {
        "darker": [(0, 1), (0, 2), (1, 0), (1, 1), (2, 0)],
        "border": [(-1, 1), (1, -1), (0, 0)],
        "lighter": [(-2, 0), (-1, -1), (-1, 0), (0, -2), (0, -1)],
        "shift": [(-1, -1), (1, 1)]
    },

    # o o x o o
    # o o x o o
    # o o x o o
    {
        "darker": [(1, -1), (1, 0), (1, 1), (2, -1), (2, 0), (2, 1)],
        "border": [(0, -1), (0, 1), (0, 0)],
        "lighter": [(-2, -1), (-2, 0), (-2, 1), (-1, -1), (-1, 0), (-1, 1)],
        "shift": [(-1, 0), (1, 0)]
    },

    # o o o
    # o o o
    # x x x
    # o o o
    # o o o
    {
        "darker": [(-1, -2), (-1, -1), (0, -2), (0, -1), (1, -2), (1, -1)],
        "border": [(-1, 0), (1, 0), (0, 0)],
        "lighter": [(-1, 1), (-1, 2), (0, 1), (0, 2), (1, 1), (1, 2)],
        "shift": [(0, -1), (0, 1)]
    }
]


def default_average_dissimilarity_function(image, R2, R1):
    dark_avg = 0.0
    light_avg = 0.0

    for p_row, p_col in R2:
        dark_avg += image[p_row, p_col]

    for p_row, p_col in R1:
        light_avg += image[p_row, p_col]

    dark_avg /= len(R2)
    light_avg /= len(R1)

    return abs(dark_avg - light_avg) / 255


#
#   dissimilarity_function = function(img, R2, R1)
#   img - image matrix, R2 - dark region, R1 - light region
#   returns value of dissimilarity between those two pixel regions (float)
#
class DissimilarityMatrix:
    def __init__(self, image_matrix, dissimilarity_function=default_average_dissimilarity_function):
        self.matrix = np.zeros(image_matrix.shape, dtype=float)
        self.rows, self.columns = image_matrix.shape
        self.image_matrix = image_matrix
        self.dissimilarity_function = dissimilarity_function
        for row in range(self.rows):
            for column in range(self.columns):
                best_figure, best_value = self.find_best_figure(row, column)
                if not self.is_better_shift(row, column, best_figure, best_value):
                    self.update_dissimilarity(row, column, best_figure["border"], best_value / 3)
        self.truncate_values()

    def calculate_figure(self, p_row, p_col, figure_map):
        dark_region_pixels = []
        light_region_pixels = []

        for v_row, v_col in figure_map["darker"]:
            if self.rows > (p_row + v_row) >= 0 and self.columns > (p_col + v_col) >= 0:
                dark_region_pixels.append((p_row + v_row, p_col + v_col))

        for v_row, v_col in figure_map["lighter"]:
            if self.rows > (p_row + v_row) >= 0 and self.columns > (p_col + v_col) >= 0:
                light_region_pixels.append((p_row + v_row, p_col + v_col))

        if not dark_region_pixels or not light_region_pixels:
            return 0

        return self.dissimilarity_function(self.image_matrix, dark_region_pixels, light_region_pixels)

    def find_best_figure(self, p_row, p_col):
        curr_best_value = 0.0
        curr_best_ind = 0

        for i in range(len(dissimilarity_patterns)):
            new_figure_value = self.calculate_figure(p_row, p_col, dissimilarity_patterns[i])
            if curr_best_value < new_figure_value:
                curr_best_value = new_figure_value
                curr_best_ind = i

        return dissimilarity_patterns[curr_best_ind], curr_best_value

    def is_better_shift(self, p_row, p_col, best_figure, best_value):
        any_value_larger = False

        for v_row, v_col in best_figure["shift"]:
            if self.rows > p_row + v_row >= 0 and self.columns > p_col + v_col >= 0:
                shift_value = self.calculate_figure(p_row + v_row, p_col + v_col, best_figure)
                if shift_value > best_value:
                    any_value_larger = True
                    break
        return any_value_larger

    def update_dissimilarity(self, p_row, p_col, border_pixels, value):
        for v_row, v_col in border_pixels:
            if self.rows > (p_row + v_row) >= 0 and self.columns > (p_col + v_col) >= 0:
                self.matrix[p_row + v_row, p_col + v_col] += value

    def truncate_values(self):
        rows, columns = self.matrix.shape

        for row in range(rows):
            for column in range(columns):
                if self.matrix[row, column] > 1:
                    self.matrix[row, column] = 1

    def __getitem__(self, p_row, p_col):
        return self.matrix[p_row, p_col]

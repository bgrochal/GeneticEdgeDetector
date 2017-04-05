import numpy as np

dissimilarity_patterns = [
    {
        "darker": [],
        "border": [],
        "lighter": [],
        "shift": []
    },
    {
        "darker": [],
        "border": [],
        "lighter": [],
        "shift": []
    },
    {
        "darker": [],
        "border": [],
        "lighter": [],
        "shift": []
    },
    {
        "darker": [],
        "border": [],
        "lighter": [],
        "shift": []
    },
    {
        "darker": [],
        "border": [],
        "lighter": [],
        "shift": []
    },
    {
        "darker": [],
        "border": [],
        "lighter": [],
        "shift": []
    },
    {
        "darker": [],
        "border": [],
        "lighter": [],
        "shift": []
    },
    {
        "darker": [],
        "border": [],
        "lighter": [],
        "shift": []
    },
    {
        "darker": [],
        "border": [],
        "lighter": [],
        "shift": []
    },
    {
        "darker": [],
        "border": [],
        "lighter": [],
        "shift": []
    },
    {
        "darker": [],
        "border": [],
        "lighter": [],
        "shift": []
    },
    {
        "darker": [],
        "border": [],
        "lighter": [],
        "shift": []
    }
]


#
#   dissimilarity_function = function(img, R2, R1)
#   img - image matrix, R2 - dark region, R1 - light region
#   returns value of dissimilarity between those two pixel regions (float)
#
class DissimilarityMatrix:

    def __init__(self, image_matrix, dissimilarity_function):
        self.matrix = np.zeros(image_matrix.shape, dtype=float)
        rows, columns = image_matrix.shape
        self.image_matrix = image_matrix
        self.dissimilarity_function = dissimilarity_function
        for row in range(rows):
            for column in range(columns):
                best_figure, best_value = self.find_best_figure(row, column)
                any_shift_larger, best_shift_value, _ = self.find_best_shift(row, column, best_figure, best_value)
                if not any_shift_larger:
                    self.update_dissimilarity(row, column, best_figure["border"], best_shift_value/3)
        self.truncate_values()

    def calculate_figure(self, p_row, p_col, figure_map):
        dark_region_pixels = []
        light_region_pixels = []

        for v_row, v_col in figure_map["darker"]:
            dark_region_pixels.append((p_row + v_row, p_col + v_col))

        for v_row, v_col in figure_map["lighter"]:
            light_region_pixels.append((p_row + v_row, p_col + v_col))

        return self.dissimilarity_function(self.image_matrix, dark_region_pixels, light_region_pixels)

    def find_best_figure(self, p_row, p_col):
        curr_best_value = 0.0
        curr_best_ind = 0

        for i in range(len(dissimilarity_patterns)):
            new_figure_value = self.calculate_figure(
                p_row, p_col,
                dissimilarity_patterns[i])
            if curr_best_value < new_figure_value:
                curr_best_value = new_figure_value
                curr_best_ind = i

        return dissimilarity_patterns[curr_best_ind], curr_best_value

    def find_best_shift(self, p_row, p_col, best_figure, best_value):
        smallest_shift_value = 10000
        best_shift_vec = (None, None)
        any_value_larger = False

        for v_row, v_col in best_figure["shift"]:
            shift_value = self.calculate_figure(p_row + v_row, p_col + v_col, best_figure)
            if shift_value > best_value:
                any_value_larger = True
                break
            if shift_value < smallest_shift_value:
                smallest_shift_value = shift_value
                best_shift_vec = (v_row, v_col)

        return any_value_larger, smallest_shift_value, best_shift_vec

    def update_dissimilarity(self, p_row, p_col, border_pixels, value):
        for v_row, v_col in border_pixels:
            self.matrix[p_row + v_row, p_col + v_col] += value

    def truncate_values(self):
        rows, columns = self.matrix.shape

        for row in range(rows):
            for column in range(columns):
                if self.matrix[row, column] > 1:
                    self.matrix[row, column] = 1

    def __getitem__(self, p_row, p_col):
        return self.matrix[p_row, p_col]

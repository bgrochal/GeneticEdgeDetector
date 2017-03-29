import numpy as np


class Image:

    def __init__(self, image_matrix, file_name):
        self.image_matrix = image_matrix
        self.edge_matrix = np.ones(image_matrix.shape, dtype=bool)
        self.file_name = file_name
        super().__init__()


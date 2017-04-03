"""
This class represents single chromosome of an individual, which states for a solution of the problem.
"""
import numpy as np


class Genotype:
    def __init__(self, image_shape):
        self.genes = np.zeros(image_shape, dtype=bool)

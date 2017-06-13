"""
This class represents single chromosome of an individual, which states for a solution of the problem.
"""
import numpy as np


class Genotype:
    def __init__(self, cost, fitness=0):
        self.genes = np.zeros((3, 3))
        self.cost = cost
        self.fitness = fitness

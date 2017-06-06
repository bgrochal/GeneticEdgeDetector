"""
This class contains common interface for creating a population of individuals (so called gene pool).
"""
import sys
from random import random

import numpy as np

from common.solver.population.initializer import Initializer
from edge_improvement.solver.population.genotype import Genotype


class DomainInitializer(Initializer):
    def __init__(self, population_size, genotype_shape, similarity, threshold):
        super().__init__(population_size, genotype_shape)
        self.similarity = similarity
        self.threshold = threshold

    def initialize(self):
        raise NotImplementedError

    def perform_threshold(self, reference_image):
        threshold_image = np.zeros(reference_image.shape, dtype=bool)
        for i in range(reference_image.shape[0]):
            for j in range(reference_image.shape[1]):
                threshold_image[i][j] = True if reference_image[i][j] >= self.threshold else False
        return threshold_image

    def _generate_random_genotype(self, reference_image):
        genotype = Genotype(self.genotype_shape, sys.maxsize)
        for i in range(genotype.genes.shape[0]):
            for j in range(genotype.genes.shape[1]):
                genotype.genes[i][j] = reference_image[i][j] if random() <= self.similarity else False
        return genotype

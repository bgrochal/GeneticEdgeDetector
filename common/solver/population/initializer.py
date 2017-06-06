"""
This class defines basic interface for creating initial population.
"""
from abc import ABC, abstractmethod


class Initializer(ABC):
    def __init__(self, population_size, genotype_shape):
        self.population_size = population_size
        self.genotype_shape = genotype_shape

    @abstractmethod
    def initialize(self):
        # TODO: Should we prevent creating two initial individuals with exactly the same genotype?
        # TODO: Should we also ensure with 100% probability that not all generated genotypes are exactly the same?
        raise NotImplementedError

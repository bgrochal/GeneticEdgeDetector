"""
This class defines basic interface for performing crossover operation.
"""
from abc import ABC, abstractmethod


class Crossover(ABC):

    def __init__(self, probability):
        self.probability = probability

    @abstractmethod
    def cross(self, first_genotype, second_genotype):
        raise NotImplementedError

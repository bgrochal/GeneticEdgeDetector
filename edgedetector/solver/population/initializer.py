"""
This class creates a population of individuals (so called gene pool).
"""
from abc import ABC, abstractmethod


class Initializer(ABC):
    @abstractmethod
    def initialize(self):
        # TODO: Should we prevent creating two initial individuals with exactly the same genotype?
        # TODO: Should we also ensure with 100% probability that not all generated genotypes are exactly the same?
        raise NotImplementedError

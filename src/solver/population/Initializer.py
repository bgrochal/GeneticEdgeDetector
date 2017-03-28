"""
This class creates a population of individuals (so called gene pool).
"""
from abc import ABC, abstractmethod


class Initializer(ABC):
    @abstractmethod
    def initialize(self, population_size):
        raise NotImplementedError

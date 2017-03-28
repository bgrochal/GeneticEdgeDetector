"""
This class defines basic interface for performing mutation operation.
"""
from abc import ABC, abstractmethod


class Mutation(ABC):
    @abstractmethod
    def mutate(self, genotype):
        raise NotImplementedError

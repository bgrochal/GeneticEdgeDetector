"""
This class defines basic interface for evaluating mathematical expressions.
"""
from abc import ABC, abstractmethod


class Evaluator(ABC):
    @abstractmethod
    def evaluate(self, genotype):
        raise NotImplementedError

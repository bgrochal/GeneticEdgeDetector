"""
This class defines basic interface for running genetic algorithm until the condition is satisfied.
"""
from abc import ABC, abstractmethod


class StopCondition(ABC):
    def __init__(self, probability):
        self.probability = probability

    def run(self, function):
        result = None
        while not self.condition():
            result = function()
            self.probability.update()
        return result

    @abstractmethod
    def condition(self):
        raise NotImplementedError

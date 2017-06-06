"""
This class defines basic interface for running genetic algorithm until condition is satisfied.
"""
from abc import ABC, abstractmethod


class StopCondition(ABC):
    def run(self, function):
        result = None
        while not self.condition():
            result = function()
        return result

    @abstractmethod
    def condition(self):
        raise NotImplementedError

"""
This class defines basic interface for performing selection operation.
"""
from abc import ABC, abstractmethod


class Selection(ABC):
    @abstractmethod
    def select(self, population):
        raise NotImplementedError

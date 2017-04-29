"""
This class defines basic interface for performing mutation operation.
"""

from abc import ABC, abstractmethod
from random import random

import numpy as np


def _get_random_list(shape):
    return np.array([[random() for _ in range(shape[1])] for _ in range(shape[0])])


class Mutation(ABC):
    def __init__(self, probability):
        super().__init__()
        self.probability = probability

    @abstractmethod
    def mutate(self, genotype):
        raise NotImplementedError

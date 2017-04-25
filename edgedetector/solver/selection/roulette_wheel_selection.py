"""
This class defines roulette wheel selection operation.
"""
from random import random

from edgedetector.solver.selection.selection import Selection


def _get_roulette_table(population):
    overall_fitness = sum([genotype.fitness for genotype in population])
    roulette_fitness = {genotype: normalized_fitness for (genotype, normalized_fitness) in zip(
        [genotype for genotype in population], [genotype.fitness / overall_fitness for genotype in population])}
    roulette_fitness = sorted(roulette_fitness.items(), key=lambda item: item[1], reverse=True)

    interval_start = 0
    roulette_table = dict()
    for (genotype, normalized_fitness) in roulette_fitness:
        roulette_table[genotype] = (interval_start, interval_start + normalized_fitness)
        interval_start += normalized_fitness

    return roulette_table


def _get_genotype(roulette_table, roulette_result):
    for (key, value) in roulette_table.items():
        if value[0] <= roulette_result < value[1]:
            return key


class RouletteWheelSelection(Selection):
    def __init__(self, repetition):
        super().__init__()
        self.method = self._select_with_repetition if repetition else self._select_without_repetition

    def select(self, population):
        roulette_table = _get_roulette_table(population)
        return self.method(roulette_table)

    def _select_with_repetition(self, roulette_table):
        return _get_genotype(roulette_table, random()), _get_genotype(roulette_table, random())

    def _select_without_repetition(self, roulette_table):
        first_parent = _get_genotype(roulette_table, random())
        second_parent = None

        while second_parent is None:
            selected_parent = _get_genotype(roulette_table, random())
            if selected_parent != first_parent:
                second_parent = selected_parent

        return first_parent, second_parent

"""
This class contains tests for RouletteWheelSelection class.
"""
from unittest import mock

from edge_improvement.solver.population.genotype import Genotype
from edge_improvement.solver.selection import roulette_wheel_selection
from edge_improvement.solver.selection.roulette_wheel_selection import RouletteWheelSelection
from test.solver.selection.roulette_wheel_selection_core import RouletteWheelSelectionCore


class RouletteWheelSelectionTest(RouletteWheelSelectionCore.RouletteWheelSelection):
    def setUp(self):
        shape = (2, 2)
        self.population = [Genotype(shape, None, fitness=0), Genotype(shape, None, fitness=1),
                           Genotype(shape, None, fitness=2), Genotype(shape, None, fitness=3),
                           Genotype(shape, None, fitness=4)]

    def test_get_roulette_table(self):
        overall_fitness = sum([genotype.fitness for genotype in self.population])
        self.assertEqual(overall_fitness, 10)

        expected_table = dict()
        for i in reversed(range(len(self.population))):
            interval_beginning = 0
            for j in reversed(range(i + 1, len(self.population))):
                interval_beginning += self.population[j].fitness / overall_fitness
            expected_table[self.population[i]] = (interval_beginning,
                                                  interval_beginning + self.population[i].fitness / overall_fitness)
        self.assertDictEqual(roulette_wheel_selection._get_roulette_table(self.population), expected_table)

    def test_get_genotype(self):
        roulette_table = roulette_wheel_selection._get_roulette_table(self.population)

        self.assertEqual(roulette_wheel_selection._get_genotype(roulette_table, 0.0), self.population[4])
        self.assertEqual(roulette_wheel_selection._get_genotype(roulette_table, 0.39999), self.population[4])
        self.assertEqual(roulette_wheel_selection._get_genotype(roulette_table, 0.4), self.population[3])

    @mock.patch.object(roulette_wheel_selection, 'random')
    def test_select_with_repetition_with_same_genotypes(self, mock_random):
        selection = RouletteWheelSelection(True)
        mock_random.side_effect = [0.2, 0.3]

        roulette_table = roulette_wheel_selection._get_roulette_table(self.population)
        self.assertTupleEqual(selection.select(roulette_table), (self.population[4], self.population[4]))

    @mock.patch.object(roulette_wheel_selection, 'random')
    def test_select_with_repetition_with_different_genotypes(self, mock_random):
        selection = RouletteWheelSelection(True)
        mock_random.side_effect = [0.25, 0.45]

        roulette_table = roulette_wheel_selection._get_roulette_table(self.population)
        self.assertTupleEqual(selection.select(roulette_table), (self.population[4], self.population[3]))

    @mock.patch.object(roulette_wheel_selection, 'random')
    def test_select_without_repetition_with_same_genotypes(self, mock_random):
        selection = RouletteWheelSelection(False)
        mock_random.side_effect = [0.2, 0.3, 0.5]

        roulette_table = roulette_wheel_selection._get_roulette_table(self.population)
        self.assertTupleEqual(selection._select_without_repetition(roulette_table),
                              (self.population[4], self.population[3]))

    @mock.patch.object(roulette_wheel_selection, 'random')
    def test_select_without_repetition_with_different_genotypes(self, mock_random):
        selection = RouletteWheelSelection(False)
        mock_random.side_effect = [0.25, 0.45]

        roulette_table = roulette_wheel_selection._get_roulette_table(self.population)
        self.assertTupleEqual(selection._select_without_repetition(roulette_table),
                              (self.population[4], self.population[3]))

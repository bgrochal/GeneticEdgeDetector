"""
This class contains acceptance tests for the biased roulette wheel selection mechanism.
"""
import matplotlib.pyplot as plt
import numpy as np

from edgedetector.config.config_reader import ConfigReader
from edgedetector.solver.population.genotype import Genotype
from test.solver.selection.roulette_wheel_selection_core import RouletteWheelSelectionCore


class RouletteWheelSelectionAcceptance(RouletteWheelSelectionCore.RouletteWheelSelection):
    def setUp(self):
        shape = (5, 5)
        self.population = [Genotype(shape, None, fitness=12), Genotype(shape, None, fitness=4),
                           Genotype(shape, None, fitness=8), Genotype(shape, None, fitness=15),
                           Genotype(shape, None, fitness=7), Genotype(shape, None, fitness=30),
                           Genotype(shape, None, fitness=10), Genotype(shape, None, fitness=10),
                           Genotype(shape, None, fitness=1), Genotype(shape, None, fitness=3),
                           Genotype(shape, None, fitness=0)]

        config = ConfigReader('config.yml')
        self.draws = config.get_property(['distribution', 'draws'])
        self.cycles = config.get_property(['distribution', 'cycles'])

    def test_selection_distribution(self):
        def add_to_histogram(histogram, key):
            if key in histogram.keys():
                histogram[key] += 1
            else:
                histogram[key] = 1

        results = []
        for cycle in range(self.cycles):
            selection_histogram = dict()
            for iteration in range(self.draws):
                first_genotype, second_genotype = self.selection.select(self.population)
                add_to_histogram(selection_histogram, first_genotype)
                add_to_histogram(selection_histogram, second_genotype)
            selection_histogram = {key: value / (2 * self.draws) for (key, value) in selection_histogram.items()}
            results.append(selection_histogram)

        average_histogram = []
        deviation_histogram = []
        for genotype in self.population:
            genotype_results = [histogram[genotype] for histogram in results if genotype in histogram.keys()]
            if len(genotype_results) > 0:
                average_histogram.append(np.mean(genotype_results))
                deviation_histogram.append(np.std(genotype_results))

        # Plotting histogram.
        plt.title('Normalized distribution of the biased roulette wheel selection.')
        plt.xticks(np.arange(10) + 0.45, ['Genotype 1', 'Genotype 2', 'Genotype 3', 'Genotype 4', 'Genotype 5',
                                          'Genotype 6', 'Genotype 7', 'Genotype 8', 'Genotype 9', 'Genotype 10'])
        plt.xlabel('Genotype')
        plt.ylabel('Fraction of draws including particular genotype')
        plt.ylim((0, max(average_histogram + deviation_histogram) + 0.05))

        plt.bar(np.arange(10) + 0.1, average_histogram, yerr=deviation_histogram, color='green', ecolor='black')
        plt.show()

        # Printing summary statistics.
        for i in range(len(self.population) - 1):
            lower_bound = (average_histogram[i] - deviation_histogram[i]) * 100
            upper_bound = (average_histogram[i] + deviation_histogram[i]) * 100
            print("fitness: {0:05.2f}; range: {1:05.2f} - {2:05.2f}{3:}".format(
                self.population[i].fitness, lower_bound, upper_bound,
                "" if lower_bound <= self.population[i].fitness <= upper_bound else "\tWRONG"))

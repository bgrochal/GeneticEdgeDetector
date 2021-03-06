"""
This class defines main algorithm of a solver for genetic algorithms.
"""
import logging
from abc import ABC, abstractmethod

import numpy as np

from common.data.image_reader import ImageReader


class AbstractSolver(ABC):
    def __init__(self, config):
        self.config = config

        image_file = config['data']['inputPath']
        self.output_file = config['data']['outputPath']
        self.image = ImageReader.read(image_file)

        self._initialize_specific_variables()
        self.population = self._initialize_population()
        self.cost_evaluator = self._initialize_overall_cost_evaluator()
        self.fitness_evaluator = self._initialize_fitness_evaluator()
        self.probability = self._initialize_probability()
        self.selection = self._initialize_selection()
        self.crossover = self._initialize_crossover()
        self.mutation = self._initialize_mutation()
        self.stop_condition = self._initialize_stop_condition()

    def solve(self):
        best_fitness, best_genotype = self.stop_condition.run(self.__generation)
        self._manage_results(best_genotype, best_fitness)

    def __generation(self):
        best_fitness, best_genotype = self.__evaluate()

        # Dumping necessary information to a logfile.
        population_costs = np.array([genotype.cost for genotype in self.population])
        logging.info('%s %s %s %s', str(self.stop_condition.steps), str(best_genotype.cost),
                                    str(population_costs.mean()), str(population_costs.std()))

        self.__breed(best_genotype)
        print('fitness of best genotype: {:.4f}; cost of best genotype: {:.4f}'.format(best_fitness, best_genotype.cost))

        # TODO: The line below is tightly coupled with the type of the stop condition used. Remove this line when
        # changing the stop condition. Refactor this one.
        self.stop_condition.best_cost = best_genotype.cost
        return best_fitness, best_genotype

    def __evaluate(self):
        worst_cost, worst_genotype = self.__count_costs()
        return self.__count_fitness(worst_genotype)

    def __count_costs(self):
        worst_cost = 0
        worst_genotype = None
        for genotype in self.population:
            cost = self.cost_evaluator.evaluate(genotype)
            if cost > worst_cost:
                worst_cost = cost
                worst_genotype = genotype
        return worst_cost, worst_genotype

    def __count_fitness(self, worst_genotype):
        best_fitness = 0
        best_genotype = None
        self.fitness_evaluator.worst_genotype = worst_genotype
        for genotype in self.population:
            fitness = self.fitness_evaluator.evaluate(genotype)
            if fitness > best_fitness:
                best_fitness = fitness
                best_genotype = genotype
        return best_fitness, best_genotype

    def __breed(self, best_genotype):
        offspring_population = [best_genotype]
        while len(offspring_population) != len(self.population):
            first_mate, second_mate = self.selection.select(self.population)
            first_offspring, second_offspring = self.crossover.cross(first_mate, second_mate)
            self.mutation.mutate(first_offspring)
            self.mutation.mutate(second_offspring)
            offspring_population.extend((first_offspring, second_offspring))
        self.population = offspring_population

    @abstractmethod
    def _initialize_specific_variables(self):
        raise NotImplementedError

    @abstractmethod
    def _initialize_population(self):
        raise NotImplementedError

    @abstractmethod
    def _initialize_overall_cost_evaluator(self):
        raise NotImplementedError

    @abstractmethod
    def _initialize_fitness_evaluator(self):
        raise NotImplementedError

    @abstractmethod
    def _initialize_probability(self):
        raise NotImplementedError

    @abstractmethod
    def _initialize_selection(self):
        raise NotImplementedError

    @abstractmethod
    def _initialize_crossover(self):
        raise NotImplementedError

    @abstractmethod
    def _initialize_mutation(self):
        raise NotImplementedError

    @abstractmethod
    def _initialize_stop_condition(self):
        raise NotImplementedError

    @abstractmethod
    def _manage_results(self, best_genotype, best_fitness):
        raise NotImplementedError

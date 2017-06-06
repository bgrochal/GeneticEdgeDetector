"""
This class defines main algorithm of a solver for genetic algorithms.
"""
from common.data.image_reader import ImageReader
from common.data.image_writer import ImageWriter
from common.solver.selection.selection_factory import SelectionFactory
from common.solver.stopcondition.stop_condition_factory import StopConditionFactory
from edge_improvement.solver.crossover.crossover_factory import CrossoverFactory
from edge_improvement.solver.evaluator.cost.dissimilarity_matrix import DissimilarityMatrix
from edge_improvement.solver.evaluator.cost.overall_cost_evaluator import OverallCostEvaluator
from edge_improvement.solver.evaluator.fitness.fitness_evaluator import FitnessEvaluator
from edge_improvement.solver.mutation.mutation_factory import MutationFactory
from edge_improvement.solver.population.initializer_factory import InitializerFactory
from edgedetector.solver.probability.probability_factory import ProbabilityFactory


class Solver:
    def __init__(self, config):
        self.config = config
        image_file = config["data"]["inputPath"]
        self.output_file = config["data"]["outputPath"]
        self.image = ImageReader.read(image_file)
        self.probability = ProbabilityFactory.create(config["algorithm"]["probability"])
        self.dissimilarity_matrix = DissimilarityMatrix(self.image.image_matrix).matrix
        self.population = self.__initialize_population()
        self.fitness_evaluator = self.__initialize_fitness_evaluator()
        self.cost_evaluator = self.__initialize_overall_cost_evaluator()
        self.crossover = self.__initialize_crossover()
        self.mutation = self.__initialize_mutation()
        self.selection = self.__initialize_selection()
        self.stop_condition = self.__initialize_stop_condition()

    def solve(self):
        best_fitness, best_genotype = self.stop_condition.run(self.__generation)
        self.image.edge_matrix = best_genotype.genes
        ImageWriter.write(self.image, self.output_file, best_fitness, best_genotype.cost)

    def __generation(self):
        best_fitness, best_genotype = self.__evaluate()
        self.__breed(best_genotype)
        print("fitness of best genotype: {}; cost of best genotype: {}".format(best_fitness, best_genotype.cost))
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

    def __initialize_population(self):
        config = self.config['algorithm']["initializer"]
        initializer = InitializerFactory.create(config, self.image, self.dissimilarity_matrix)
        return initializer.initialize()

    def __initialize_fitness_evaluator(self):
        return FitnessEvaluator(
            self.config["algorithm"]["fitness"]["powerCoefficient"])

    def __initialize_overall_cost_evaluator(self):
        return OverallCostEvaluator(
            self.config["algorithm"]["cost"]["weights"],
            self.dissimilarity_matrix
        )

    def __initialize_crossover(self):
        config = self.config['algorithm']["crossover"]
        return CrossoverFactory.create(config, self.probability)

    def __initialize_mutation(self):
        config = self.config['algorithm']["mutation"]
        return MutationFactory.create(config, self.probability)

    def __initialize_selection(self):
        config = self.config['algorithm']["selection"]
        return SelectionFactory.create(config)

    def __initialize_stop_condition(self):
        config = self.config['algorithm']["stopCondition"]
        return StopConditionFactory.create(config, self.probability)
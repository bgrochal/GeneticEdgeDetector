"""
This class defines the algorithm of the solver for the edge improvement algorithm.
"""
from common.data.image_writer import ImageWriter
from common.solver.abstract_solver import AbstractSolver
from common.solver.evaluator.fitness.fitness_evaluator import FitnessEvaluator
from common.solver.probability.probability_factory import ProbabilityFactory
from common.solver.selection.selection_factory import SelectionFactory
from common.solver.stopcondition.stop_condition_factory import StopConditionFactory
from edge_improvement.solver.crossover.crossover_factory import CrossoverFactory
from edge_improvement.solver.evaluator.cost.dissimilarity_matrix import DissimilarityMatrix
from edge_improvement.solver.evaluator.cost.overall_cost_evaluator import OverallCostEvaluator
from edge_improvement.solver.mutation.mutation_factory import MutationFactory
from edge_improvement.solver.population.initializer_factory import InitializerFactory


class EdgeImprovementSolver(AbstractSolver):
    def __init__(self, config):
        super().__init__(config)

    def _initialize_specific_variables(self):
        self.dissimilarity_matrix = DissimilarityMatrix(self.image.image_matrix).matrix

    def _initialize_population(self):
        config = self.config['algorithm']['initializer']
        initializer = InitializerFactory.create(config, self.image, self.dissimilarity_matrix)
        return initializer.initialize()

    def _initialize_overall_cost_evaluator(self):
        config = self.config['algorithm']['cost']
        overall_cost_evaluator = OverallCostEvaluator(config['weights'], self.dissimilarity_matrix)
        return overall_cost_evaluator

    def _initialize_fitness_evaluator(self):
        config = self.config['algorithm']['fitness']
        fitness_evaluator = FitnessEvaluator(config['powerCoefficient'])
        return fitness_evaluator

    def _initialize_probability(self):
        config = self.config['algorithm']['probability']
        probability = ProbabilityFactory.create(config)
        return probability

    def _initialize_selection(self):
        config = self.config['algorithm']['selection']
        selection = SelectionFactory.create(config)
        return selection

    def _initialize_crossover(self):
        config = self.config['algorithm']['crossover']
        crossover = CrossoverFactory.create(config, self.probability)
        return crossover

    def _initialize_mutation(self):
        config = self.config['algorithm']['mutation']
        mutation = MutationFactory.create(config, self.probability)
        return mutation

    def _initialize_stop_condition(self):
        config = self.config['algorithm']['stopCondition']
        stop_condition = StopConditionFactory.create(config, self.probability)
        return stop_condition

    def _manage_results(self, best_genotype, best_fitness):
        self.image.edge_matrix = best_genotype.genes
        ImageWriter.write(self.image, self.output_file, best_fitness, best_genotype.cost)

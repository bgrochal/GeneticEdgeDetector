"""
This class defines the algorithm of the solver for the optimal filter algorithm.
"""
from common.solver.abstract_solver import AbstractSolver
from common.solver.evaluator.fitness.fitness_evaluator import FitnessEvaluator
from common.solver.probability.probability_factory import ProbabilityFactory
from common.solver.selection.selection_factory import SelectionFactory
from common.solver.stopcondition.stop_condition_factory import StopConditionFactory
from optimal_filter.solver.crossover.crossover_factory import CrossoverFactory
from optimal_filter.solver.evaluator.cost.cost_evaluator import CostEvaluator, get_convolved_image
from optimal_filter.solver.mutation.mutation_factory import MutationFactory
from optimal_filter.solver.population.initializer_factory import InitializerFactory
from optimal_filter.solver.threshold.thresholding_factory import ThresholdingFactory


class OptimalFilterSolver(AbstractSolver):
    def __init__(self, config):
        super().__init__(config)

    def _initialize_specific_variables(self):
        config = self.config['algorithm']['threshold']
        self.threshold = ThresholdingFactory.create(config)

    def _initialize_population(self):
        config = self.config['algorithm']['initializer']
        initializer = InitializerFactory.create(config)
        return initializer.initialize()

    def _initialize_overall_cost_evaluator(self):
        config = self.config['algorithm']['cost']
        overall_cost_evaluator = CostEvaluator(self.image.image_matrix, config['targetDeviation'])
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

    def _get_edge_matrix(self, best_genotype):
        convolved_image = get_convolved_image(self.image.image_matrix, best_genotype.genes)
        return self.threshold.classify(convolved_image)

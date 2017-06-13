"""
This class is responsible for creating objects of abstract class StopCondition.
"""
from common.solver.stopcondition.best_solution_unchanged_stop_condition import BestSolutionUnchangedStopCondition
from common.solver.stopcondition.fitness_or_max_steps_stop_condition import FitnessOrMaxStepsStopCondition
from common.solver.stopcondition.steps_number_stop_condition import StepsNumberStopCondition


class StopConditionFactory:
    @staticmethod
    def create(config, probability):
        class_ = config['class']

        if class_ == 'BestSolutionUnchangedStopCondition':
            steps = config['steps']
            return BestSolutionUnchangedStopCondition(steps, probability)
        if class_ == 'FitnessOrMaxStepsStopCondition':
            desired_fitness = config['desiredFitness']
            fitness_tolerance = config['fitnessTolerance']
            max_steps = config['maxSteps']
            return FitnessOrMaxStepsStopCondition(desired_fitness, fitness_tolerance, max_steps, probability)
        if class_ == 'StepsNumberStopCondition':
            max_steps = config['maxSteps']
            return StepsNumberStopCondition(max_steps, probability)
        raise NameError('Unknown class: {}'.format(class_))

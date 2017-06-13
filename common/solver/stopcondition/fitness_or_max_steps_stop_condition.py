"""
This class is responsible for stopping the execution of the algorithm when the desired fitness has been reached (with
respect to given tolerance) or the maximum number of iterations have been performed.
"""
import sys

from common.solver.stopcondition.stop_condition import StopCondition


class FitnessOrMaxStepsStopCondition(StopCondition):
    def __init__(self, desired_fitness, fitness_tolerance, max_steps, probability):
        super().__init__(probability)
        self.desired_fitness = desired_fitness
        self.fitness_tolerance = fitness_tolerance
        self.max_steps = max_steps

        self.best_cost = sys.maxsize
        self.steps = 0

    def condition(self):
        self.steps += 1
        return abs(self.desired_fitness - self.best_cost) < self.fitness_tolerance or self.steps > self.max_steps

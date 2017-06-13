"""
This class is responsible for stopping the execution of the algorithm when the best solution (equivalently - fitness)
has not been changed since the specified number of iterations.
"""
import sys

from common.solver.stopcondition.stop_condition import StopCondition


class BestSolutionUnchangedStopCondition(StopCondition):
    def __init__(self, steps, probability):
        super().__init__(probability)
        self.steps = steps

        self.last_iteration_fitness = sys.maxsize
        self.best_fitness = sys.maxsize
        self.steps_since_unchanged = 0

    def condition(self):
        if self.last_iteration_fitness != self.best_fitness:
            self.steps_since_unchanged = 0
        else:
            self.steps_since_unchanged += 1

        self.last_iteration_fitness = self.best_fitness
        return self.steps_since_unchanged > self.steps

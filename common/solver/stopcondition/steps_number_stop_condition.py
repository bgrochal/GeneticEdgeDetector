"""
This class is responsible for stopping the execution of the algorithm when specified number of steps passed.
"""
from common.solver.stopcondition.stop_condition import StopCondition


class StepsNumberStopCondition(StopCondition):
    def __init__(self, max_steps, probability):
        super().__init__(probability)
        self.max_steps = max_steps

        self.steps = 0

    def condition(self):
        self.steps += 1
        return self.steps > self.max_steps

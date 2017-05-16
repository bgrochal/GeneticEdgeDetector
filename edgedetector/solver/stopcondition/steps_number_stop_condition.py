"""
This class defines basic interface for running genetic algorith unil
condition is satisfied
"""
from edgedetector.solver.stopcondition.stop_condition import StopCondition


class StepsNumberStopCondition(StopCondition):

    def __init__(self, max_steps, probability):
        super().__init__(probability)
        self.max_steps = max_steps
        self.steps = 0

    def condition(self):
        self.steps += 1
        return self.steps > self.max_steps

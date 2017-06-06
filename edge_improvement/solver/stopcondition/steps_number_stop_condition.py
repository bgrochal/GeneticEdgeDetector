"""
This class defines basic interface for running genetic algorith unil
condition is satisfied
"""
from edge_improvement.solver.stopcondition.stop_condition import StopCondition


class StepsNumberStopCondition(StopCondition):

    def __init__(self, max_steps):
        self.max_steps = max_steps
        self.steps = 0

    def condition(self):
        self.steps += 1
        return self.steps > self.max_steps

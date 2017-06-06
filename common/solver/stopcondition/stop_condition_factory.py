"""
This class is responsible for creating objects of abstract class StopCondition.
"""
from common.solver.stopcondition.steps_number_stop_condition import StepsNumberStopCondition


class StopConditionFactory:
    @staticmethod
    def create(config):
        class_ = config['class']
        if class_ == "StepsNumberStopCondition":
            max_steps = config['maxSteps']
            return StepsNumberStopCondition(max_steps)
        raise NameError("Unknown class: {}".format(class_))

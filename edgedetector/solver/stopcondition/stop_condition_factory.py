from edgedetector.solver.stopcondition.steps_number_stop_condition import \
    StepsNumberStopCondition


class StopConditionFactory:

    @staticmethod
    def create(config, probability):
        class_ = config['class']
        if class_ == "StepsNumberStopCondition":
            max_steps = config['maxSteps']
            return StepsNumberStopCondition(max_steps, probability)
        raise NameError("Unknown class: {}".format(class_))

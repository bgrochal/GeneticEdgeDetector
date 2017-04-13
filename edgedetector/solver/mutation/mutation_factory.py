"""This class is responsible for creating objects of subclasses of abstract
class Mutation"""

from edgedetector.solver.mutation.random_mutation import RandomMutation


class MutationFactory:

    @staticmethod
    def create(config):
        probability = config['probability']
        class_ = config['class']
        if class_ == "RandomMutation":
            return RandomMutation(probability)
        raise NameError("Unknown class: {}".format(class_))

"""This class is responsible for creating objects of subclasses of abstract
class Mutation"""

from edgedetector.solver.mutation.intelligent_mutation import IntelligentMutation
from edgedetector.solver.mutation.random_mutation import RandomMutation


class MutationFactory:
    @staticmethod
    def create(config):
        probability = config['probability']
        class_ = config['class']
        if class_ == 'RandomMutation':
            neighbours_min = config['neighboursMin']
            return RandomMutation(probability, neighbours_min)
        if class_ == 'IntelligentMutation':
            return IntelligentMutation(probability)
        raise NameError('Unknown class: {}'.format(class_))

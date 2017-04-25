"""This class is responsible for creating objects of subclasses of abstract
class Selection"""

from edgedetector.solver.selection.roulette_wheel_selection import \
    RouletteWheelSelection
from edgedetector.solver.selection.tournament_selection import \
    TournamentSelection


class SelectionFactory:
    @staticmethod
    def create(config):
        class_ = config['class']
        if class_ == "RouletteWheelSelection":
            return RouletteWheelSelection(config['repetition'])
        if class_ == "TournamentSelection":
            return TournamentSelection()
        raise NameError("Unknown class: {}".format(class_))

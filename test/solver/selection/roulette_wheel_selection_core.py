"""
This class defines a skeleton for tests of the biased roulette wheel selection mechanism.
"""
from unittest import TestCase

from edgedetector.solver.selection.roulette_wheel_selection import RouletteWheelSelection


class RouletteWheelSelectionCore:
    class RouletteWheelSelection(TestCase):
        def __init__(self, methodName='runTest'):
            super().__init__(methodName)
            self.selection = RouletteWheelSelection()

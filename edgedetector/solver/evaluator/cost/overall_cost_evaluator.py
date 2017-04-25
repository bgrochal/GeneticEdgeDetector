"""
This class implements evaluation of genotype's cost function.
"""
from edgedetector.solver.evaluator.cost.curvature_cost_evaluator import CurvatureCostEvaluator
from edgedetector.solver.evaluator.cost.dissimilarity_cost_evaluator import DissimilarityCostEvaluator
from edgedetector.solver.evaluator.cost.edge_pixels_cost_evaluator import EdgePixelsCostEvaluator
from edgedetector.solver.evaluator.cost.fragmentation_cost_evaluator import FragmentationCostEvaluator
from edgedetector.solver.evaluator.cost.thickness_cost_evaluator import ThicknessCostEvaluator
from edgedetector.solver.evaluator.evaluator import Evaluator


class OverallCostEvaluator(Evaluator):
    def __init__(self, config, dissimilarity_matrix):
        self.cost_evaluators = [
            CurvatureCostEvaluator(config),
            DissimilarityCostEvaluator(dissimilarity_matrix, config),
            ThicknessCostEvaluator(config),
            FragmentationCostEvaluator(config),
            EdgePixelsCostEvaluator(config)
        ]

    def evaluate(self, genotype):
        cost = 0
        for evaluator in self.cost_evaluators:
            cost += evaluator.evaluate(genotype)
        genotype.cost = cost
        return cost

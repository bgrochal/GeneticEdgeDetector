"""
This class implements evaluation of genotype's cost function.
"""
from edge_improvement.solver.evaluator.cost.curvature_cost_evaluator import CurvatureCostEvaluator
from edge_improvement.solver.evaluator.cost.dissimilarity_cost_evaluator import DissimilarityCostEvaluator
from edge_improvement.solver.evaluator.cost.edge_pixels_cost_evaluator import EdgePixelsCostEvaluator
from edge_improvement.solver.evaluator.cost.fragmentation_cost_evaluator import FragmentationCostEvaluator
from edge_improvement.solver.evaluator.cost.thickness_cost_evaluator import ThicknessCostEvaluator
from edge_improvement.solver.evaluator.evaluator import Evaluator


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

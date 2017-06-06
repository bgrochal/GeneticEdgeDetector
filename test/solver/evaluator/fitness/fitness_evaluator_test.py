"""
This class contains tests for FitnessEvaluator class.
"""
from unittest import TestCase

from common.solver.evaluator.fitness import FitnessEvaluator
from edge_improvement.solver.population.genotype import Genotype


class FitnessEvaluatorTest(TestCase):
    def __init__(self, method_name='runTest'):
        super().__init__(method_name)
        self.fitness_evaluator = FitnessEvaluator(2.0)

    def test_evaluate(self):
        genotype_shape = (10, 10)
        genotypes = [Genotype(genotype_shape, 2), Genotype(genotype_shape, 1), Genotype(genotype_shape, 0)]

        for genotype in genotypes:
            self.assertEqual(genotype.fitness, 0)

        self.fitness_evaluator.worst_genotype = genotypes[0]
        for genotype in genotypes:
            self.fitness_evaluator.evaluate(genotype)

        self.assertListEqual([genotype.fitness for genotype in genotypes], [0.0, 1.0, 4.0])

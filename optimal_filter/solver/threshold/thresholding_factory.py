"""
This class is responsible for creating objects of subclasses of abstract class Mutation.
"""
from optimal_filter.solver.threshold.isodata_thresholding import IsodataThresholding
from optimal_filter.solver.threshold.otsu_thresholding import OtsuThresholding


class ThresholdingFactory:
    @staticmethod
    def create(config):
        class_ = config['class']

        if class_ == 'IsodataThresholding':
            return IsodataThresholding()
        if class_ == 'OtsuThresholding':
            return OtsuThresholding()
        raise NameError('Unknown class: {}'.format(class_))

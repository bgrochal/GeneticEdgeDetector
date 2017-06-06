"""
This class is responsible for creating objects of subclasses of abstract class Mutation.
"""
from optimal_filter.solver.threshold.isodata_thresholding import IsodataThresholding
from optimal_filter.solver.threshold.li_thresholding import LiThresholding
from optimal_filter.solver.threshold.local_thresholding import LocalThresholding
from optimal_filter.solver.threshold.mean_thresholding import MeanThresholding
from optimal_filter.solver.threshold.minimum_thresholding import MinimumThresholding
from optimal_filter.solver.threshold.otsu_thresholding import OtsuThresholding
from optimal_filter.solver.threshold.triangle_thresholding import TriangleThresholding
from optimal_filter.solver.threshold.yen_thresholding import YenThresholding


class ThresholdingFactory:
    @staticmethod
    def create(class_):
        if class_ == 'IsodataThresholding':
            return IsodataThresholding()
        if class_ == 'LiThresholding':
            return LiThresholding()
        if class_ == 'LocalThresholding':
            return LocalThresholding()
        if class_ == 'MeanThresholding':
            return MeanThresholding()
        if class_ == 'MinimumThresholding':
            return MinimumThresholding()
        if class_ == 'OtsuThresholding':
            return OtsuThresholding()
        if class_ == 'TriangleThresholding':
            return TriangleThresholding()
        if class_ == 'YenThresholding':
            return YenThresholding()
        raise NameError('Unknown class: {}'.format(class_))

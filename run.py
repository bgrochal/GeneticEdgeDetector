"""
This script defines an application entry point.
"""
import logging
import os
from time import time

from common.config.config_reader import ConfigReader
from edge_improvement import CONFIG_DIR
from edge_improvement.solver.solver import EdgeImprovementSolver
from optimal_filter.solver.solver import OptimalFilterSolver


def main():
    start = time()
    solver = _get_optimal_filter_solver()
    mid = time()
    print('Initialized in {:.2f} s'.format(mid - start))
    solver.solve()
    print('Finished in {:.2f} s'.format(time() - mid))


def _get_edge_improvement_solver():
    config = ConfigReader(os.path.join(CONFIG_DIR, 'config_edge_improvement.yml'))
    return EdgeImprovementSolver(config)


def _get_optimal_filter_solver():
    config = ConfigReader(os.path.join(CONFIG_DIR, 'config_optimal_filter.yml'))
    logging.basicConfig(filename=config['data']['logsOutputPath'], format='%(message)s', level=logging.INFO)
    logging.info('[ITERATION] [LOWEST COST IN POPULATION] [AVERAGE COST IN POPULATION] [COST STD IN POPULATION]')
    return OptimalFilterSolver(config)


if __name__ == '__main__':
    main()

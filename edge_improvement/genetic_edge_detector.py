"""
This script defines an application entry point.
"""
import os
from time import time

from common.config.config_reader import ConfigReader
from edge_improvement import CONFIG_DIR
from edge_improvement.solver.solver import Solver


def main():
    config = ConfigReader(os.path.join(CONFIG_DIR, 'config.yml'))
    start = time()
    solver = Solver(config)
    mid = time()
    print("Initialized in {:.2f} s".format(mid - start))
    solver.solve()
    print("Finished in {:.2f} s".format(time() - mid))


if __name__ == '__main__':
    main()

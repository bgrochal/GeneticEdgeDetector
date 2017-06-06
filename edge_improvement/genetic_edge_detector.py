"""
This script defines an application entry point.
"""
from edge_improvement import CONFIG_DIR
from edge_improvement.config.config_reader import ConfigReader
from edge_improvement.solver.solver import Solver

import os
from time import time


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

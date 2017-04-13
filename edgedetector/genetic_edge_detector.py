"""
This script defines an application entry point.
"""
from edgedetector import CONFIG_DIR
from edgedetector.config.config_reader import ConfigReader
from edgedetector.solver.solver import Solver

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

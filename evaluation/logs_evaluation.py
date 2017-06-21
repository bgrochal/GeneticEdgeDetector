"""
This script presents the genetic algorithm's performance based on the log files.
"""
import os

import matplotlib.patches as mpatches
import numpy as np
from matplotlib import pyplot as plt

from common.config.config_reader import ConfigReader
from edge_improvement import CONFIG_DIR, PROJECT_ROOT


def main():
    config = ConfigReader(os.path.join(CONFIG_DIR, 'config_evaluation.yml'))

    multiple_runs_lowest_cost = []

    for log_file_path in config['logs']['obtainedFiles']:
        with open(os.path.join(PROJECT_ROOT, log_file_path), 'r') as log_file:
            iterations = log_file.read().splitlines()

        single_run_lowest_costs = []
        single_run_avg_cost = []
        single_run_std_cost = []

        # SPLITTING THE FILE CONTENT INTO APPROPRIATE STRUCTURES. #
        for iteration in iterations[1::]:
            values = iteration.split(' ')
            single_run_lowest_costs.append(values[1])
            single_run_avg_cost.append(values[2])
            single_run_std_cost.append(values[3])
        multiple_runs_lowest_cost.append(single_run_lowest_costs)

        # PLOTTING THE PERFORMANCE OF SINGLE ALGORITHM RUN. #
        domain = np.arange(1, len(iterations))
        plt.plot(domain, single_run_lowest_costs, '.r-', zorder=3)
        plt.plot(domain, single_run_avg_cost, '.g-', zorder=2)
        plt.plot(domain, np.add(np.array(single_run_avg_cost, dtype=float), np.array(single_run_std_cost, dtype=float)), '.b-', zorder=1)
        plt.plot(domain, np.subtract(np.array(single_run_avg_cost, dtype=float), np.array(single_run_std_cost, dtype=float)), '.b-', zorder=1)

        plt.xlabel('Iterations')
        plt.title('Average cost of the population (with the standard deviation ribbon) and the lowest cost in the population.')
        plt.xlim(domain[0] - 0.1, domain[-1] + 0.1)

        red_patch = mpatches.Patch(color='r', label='Lowest cost in population')
        green_patch = mpatches.Patch(color='g', label='Average cost of population')
        blue_patch = mpatches.Patch(color='b', label='Standard deviation ribbon of the average cost')
        plt.legend(handles=[red_patch, green_patch, blue_patch], loc=9, bbox_to_anchor=(0.5, -0.07), ncol=3)

        plt.grid()
        plt.show()

    # PLOTTING THE AGGREGATED PERFORMANCE OF ALL ALGORITHM RUNS. #
    max_iterations = np.array([len(run) for run in multiple_runs_lowest_cost]).max()
    lowest_costs_by_iterations = np.empty((max_iterations, 0)).tolist()
    for run in multiple_runs_lowest_cost:
        for iteration in range(len(run)):
            lowest_costs_by_iterations[iteration].append(run[iteration])

    for iteration in range(len(lowest_costs_by_iterations)):
        lowest_costs_by_iterations[iteration] = np.array(lowest_costs_by_iterations[iteration], dtype=float)
    avg_costs_by_iterations = np.array([costs_by_iteration.mean() for costs_by_iteration in lowest_costs_by_iterations])
    std_costs_by_iterations = np.array([costs_by_iteration.std() for costs_by_iteration in lowest_costs_by_iterations])

    domain = np.arange(1, max_iterations + 1)
    plt.plot(domain, avg_costs_by_iterations, '.r-', zorder=2)
    plt.plot(domain, np.add(avg_costs_by_iterations, std_costs_by_iterations), '.b-', zorder=1)
    plt.plot(domain, np.subtract(avg_costs_by_iterations, std_costs_by_iterations), '.b-', zorder=1)

    plt.xlabel('Iterations')
    plt.title('Average lowest cost by iteration (with the standard deviation ribbon).')
    plt.xlim(domain[0] - 0.1, domain[-1] + 0.1)

    red_patch = mpatches.Patch(color='r', label='Average lowest cost in population')
    blue_patch = mpatches.Patch(color='b', label='Standard deviation ribbon of the average lowest cost')
    plt.legend(handles=[red_patch, blue_patch], loc=9, bbox_to_anchor=(0.5, -0.07), ncol=2)

    plt.grid()
    plt.show()


if __name__ == '__main__':
    main()

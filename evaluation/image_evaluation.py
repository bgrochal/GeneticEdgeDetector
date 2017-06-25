"""
This script evaluates the genetic algorithm's performance against the Canny edge detector based on the produced images.
"""
import os

import matplotlib.patches as mpatches
import numpy as np
from matplotlib import pyplot as plt

from common.config.config_reader import ConfigReader
from common.data.image_reader import ImageReader
from edge_improvement import CONFIG_DIR


def main():
    config = ConfigReader(os.path.join(CONFIG_DIR, 'config_evaluation.yml'))

    reference_image = ImageReader.read_binary(config['images']['referenceFile'])
    labels = []
    true_detections = []
    false_detections = []
    precision_recall_relationship = []
    accuracy_values = []
    histograms = []
    images_std = []
    images_mean = []
    images_cost = []

    # ANALYSIS FOR THE REFERENCE IMAGE. #
    reference_image_ones = np.count_nonzero(reference_image)
    reference_image_zeros = reference_image.shape[0] * reference_image.shape[1] - reference_image_ones

    reference_image_mean = reference_image.mean()
    reference_image_std = reference_image.std()

    for obtained_file_path in config['images']['obtainedFiles']:
        obtained_image = ImageReader.read_binary(obtained_file_path)
        assert reference_image.shape == obtained_image.shape

        # CONFUSION MATRIX - CALCULATION OF THE PRECISION AND THE RECALL VALUES. #
        true_positives = 0
        true_negatives = 0
        false_positives = 0
        false_negatives = 0

        for (i, j) in np.ndindex(reference_image.shape):
            if reference_image[i][j] and obtained_image[i][j]:
                true_positives += 1
            elif not reference_image[i][j] and not obtained_image[i][j]:
                true_negatives += 1
            elif reference_image[i][j] and not obtained_image[i][j]:
                false_negatives += 1
            elif not reference_image[i][j] and obtained_image[i][j]:
                false_positives += 1

        precision = true_positives / (true_positives + false_positives)
        recall = true_positives / (true_positives + false_negatives)
        accuracy = (true_positives + true_negatives) / (true_positives + true_negatives + false_positives + false_negatives)

        # ANALYSIS OF THE IMAGE'S HISTOGRAM. #
        obtained_image_ones = np.count_nonzero(obtained_image)
        obtained_image_zeros = obtained_image.shape[0] * obtained_image.shape[1] - obtained_image_ones

        # ANALYSIS OF THE IMAGE'S PROPERTIES. #
        obtained_image_mean = obtained_image.mean()
        obtained_image_std = obtained_image.std()
        obtained_image_cost = obtained_image_std - reference_image_std

        # SAVING DATA TO FURTHER ANALYSIS. #
        solution_number = obtained_file_path.split('_')[-1].split('.')[0]
        labels.append('Solution {} (thinned)'.format(solution_number) if 'thinned' in obtained_file_path.split('_')[-2]
                      else 'Solution {}'.format(solution_number).center(24, ' '))
        true_detections.append((true_negatives, true_positives))
        false_detections.append((false_negatives, false_positives))
        precision_recall_relationship.append((precision, recall))
        accuracy_values.append(accuracy)
        histograms.append((obtained_image_zeros, obtained_image_ones))
        images_std.append(obtained_image_std)
        images_mean.append(obtained_image_mean)
        images_cost.append(obtained_image_cost)

    # TRUE/FALSE POSITIVES/NEGATIVES CHARTS PLOTTING. #
    def add_labels(data):
        for index in range(len(data)):
            plt.annotate(s=labels[index], xy=data[index], xytext=(-50, 5), xycoords='data', textcoords='offset points', fontsize=10)

    plt.subplot(121)
    plt.scatter([point[0] for point in true_detections], [point[1] for point in true_detections])
    plt.title('Number of pixels properly classified to positive and negative classes.')

    add_labels(true_detections)
    plt.xlabel('True negatives')
    plt.ylabel('True positives')

    plt.grid()

    plt.subplot(122)
    plt.scatter([point[0] for point in false_detections], [point[1] for point in false_detections])
    plt.title('Number of pixels improperly classified to positive and negative classes.')

    add_labels(false_detections)
    plt.xlabel('False negatives')
    plt.ylabel('False positives')

    plt.grid()

    plt.subplots_adjust(left=0.05, right=0.98, top=0.96, bottom=0.06)
    plt.show()

    # PRECISION VS RECALL CHART PLOTTING. #
    plt.scatter([point[0] for point in precision_recall_relationship],
                [point[1] for point in precision_recall_relationship])
    plt.title('Precision vs Recall relationship.')

    add_labels(precision_recall_relationship)
    plt.xlabel('Precision')
    plt.ylabel('Recall')

    plt.grid()
    plt.show()

    # COMBINED HISTOGRAM OF IMAGES PLOTTING. #
    figure, plots = plt.subplots(ncols=2, sharey=True)

    plots[0].barh(range(len(histograms)), [histogram[0] for histogram in histograms], align='center')
    plots[0].barh(len(histograms), reference_image_zeros, align='center', color='g')
    plots[0].set_title('Number of zeros in the image\'s histogram.')

    plots[0].set_yticks(range(len(histograms) + 1))
    plots[0].set_yticklabels(labels + ['Canny'.center(24)])
    plots[0].yaxis.tick_right()
    plots[0].invert_xaxis()

    plots[0].grid()

    plots[1].barh(range(len(histograms)), [histogram[1] for histogram in histograms], align='center')
    plots[1].barh(len(histograms), reference_image_ones, align='center', color='g')
    plots[1].set_title('Number of ones in the image\'s histogram.')

    plots[1].set_xlim(reversed(plots[0].get_xlim()))

    plots[1].grid()

    plt.subplots_adjust(left=0.02, right=0.98, top=0.96, bottom=0.04, wspace=0.18)
    plt.show()

    # IMAGE'S PROPERTIES PLOTTING. #
    assert len(images_std) == len(images_mean) == len(images_cost)
    data_length = len(images_std) + 1

    domain = range(data_length)
    plt.scatter(domain, [reference_image_std] + images_std, color='r')
    plt.scatter(domain, [reference_image_mean] + images_mean, color='g')
    plt.scatter(domain, [0] + images_cost, color='b')
    plt.title('Standard deviation, mean and cost of images.')

    plt.xticks(range(data_length), rotation='vertical')
    plt.gca().set_xticklabels(['Canny'.center(24)] + labels)
    plt.xlim(domain[0] - 0.5, domain[-1] + 0.5)

    plt.yticks(np.arange(plt.gca().get_ylim()[0], plt.gca().get_ylim()[1], 0.05))

    red_patch = mpatches.Patch(color='r', label='Standard deviation')
    green_patch = mpatches.Patch(color='g', label='Mean value')
    blue_patch = mpatches.Patch(color='b', label='Cost (non-absolute)')
    plt.legend(handles=[red_patch, green_patch, blue_patch], loc=3)

    plt.subplots_adjust(top=0.97, bottom=0.16)
    plt.grid()
    plt.show()


if __name__ == '__main__':
    main()

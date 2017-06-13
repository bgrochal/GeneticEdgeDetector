"""
This script performs the Canny edge detection process on the input image.
"""
import os
from time import time

from skimage import feature

from common.config.config_reader import ConfigReader
from common.data.image_reader import ImageReader
from common.data.image_writer import ImageWriter
from edge_improvement import CONFIG_DIR


def main():
    start = time()

    config = ConfigReader(os.path.join(CONFIG_DIR, 'config_canny.yml'))

    image_file = config['data']['inputPath']
    output_file = config['data']['outputPath']
    image = ImageReader.read(image_file)

    mid = time()
    print('Initialized in {:.2f} s'.format(mid - start))

    sigma = config['algorithm']['cannyParameters']['sigma']
    low_threshold = config['algorithm']['cannyParameters']['lowThreshold']
    high_threshold = config['algorithm']['cannyParameters']['highThreshold']
    binary = feature.canny(image.image_matrix, sigma=sigma, low_threshold=low_threshold, high_threshold=high_threshold)

    image.edge_matrix = binary
    ImageWriter.show_grayscale(binary)
    ImageWriter.show(image)

    print('Finished in {:.2f} s'.format(time() - mid))


if __name__ == '__main__':
    main()

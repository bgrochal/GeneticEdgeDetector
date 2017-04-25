"""
This class is responsible for saving a 2D array of 1-bit pixels into storage memory.
"""
from matplotlib import pyplot as plt

from edgedetector import PROJECT_ROOT
import os


class ImageWriter:

    @staticmethod
    def show(image):
        rgba = __class__.__merge_with_edges(image)
        plt.imshow(rgba, cmap='gray', interpolation='nearest')
        plt.show()
        plt.clf()

    @staticmethod
    def write(image, output_file):
        path = os.path.join(PROJECT_ROOT, output_file)
        rgba = __class__.__merge_with_edges(image)
        plt.imshow(rgba, cmap='gray', interpolation='nearest')
        plt.savefig(path)
        plt.clf()

    @staticmethod
    def __merge_with_edges(image):
        img = image.image_matrix
        mask = image.edge_matrix
        cmap = plt.cm.gray
        norm = plt.Normalize(img.min(), img.max())
        rgba = cmap(norm(img))
        for x in range(img.shape[0]):
            for y in range(img.shape[1]):
                if mask[x][y]:
                    rgba[x, y, :3] = 1, 0, 0
        return rgba

"""
This class is responsible for saving a 2D array of 1-bit pixels into storage memory.
"""
import os
from time import time

from matplotlib import pyplot as plt
from skimage import img_as_uint
from skimage.io import imsave

from edge_improvement import PROJECT_ROOT


class ImageWriter:
    @staticmethod
    def show(image, title=''):
        rgba = __class__.__merge_with_edges(image)
        plt.title(title)
        plt.imshow(rgba, cmap='gray', interpolation='nearest')
        plt.show()
        plt.clf()

    @staticmethod
    def show_grayscale(image, title=''):
        plt.title(title)
        plt.imshow(image, cmap='gray', interpolation='nearest')
        plt.show()
        plt.clf()

    @staticmethod
    def write(image, output_file, fitness, cost):
        path = os.path.join(PROJECT_ROOT, output_file)
        rgba = __class__.__merge_with_edges(image)
        plt.imshow(rgba, cmap='gray', interpolation='nearest')
        path, ext = os.path.splitext(path)
        path = ''.join([path, str(int(time())), ext])
        text = 'fitness={fitness}\ncost={cost}'.format(fitness=fitness, cost=cost)
        plt.figtext(.1, .0, text)
        plt.savefig(path)
        plt.clf()

    @staticmethod
    def write_binary(image, output_file):
        path = os.path.join(PROJECT_ROOT, output_file)
        imsave(path, img_as_uint(image))

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

"""
This script defines an application entry point.
"""

from edgedetector.data.image_reader import ImageReader

import numpy as np
from edgedetector.data.image_writer import ImageWriter


def main():

    img = ImageReader.read("megan.png")
    # random "edges"
    img.edge_matrix = np.random.randint(0, 2, img.edge_matrix.shape, dtype=bool)
    img_writer = ImageWriter()
    # img_writer.show(img)
    img_writer.write(img, "megan_out.png")

if __name__ == '__main__':
    main()

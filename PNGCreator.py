import matplotlib.pyplot as plt
import matplotlib.cm as cm
from Creator import Creator


class PNGCreator(Creator):

    def __init__(self, matrix):
        self.matrix = matrix

    def draw(self):
        plt.imshow(self.matrix, cmap=cm.Oranges, interpolation='bilinear')
        plt.colorbar()
        plt.show()

    def save(self, filename):
        plt.imsave(filename, arr=self.matrix, cmap=cm.Oranges)

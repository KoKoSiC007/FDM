import imageio

from Creator import Creator


class GifCreator(Creator):

    def __init__(self, gif_name, files):
        self.gif_name = gif_name
        self.files = files

    def save(self):
        with imageio.get_writer(f'gifs/{self.gif_name}', mode='I') as writer:
            for filename in self.files:
                image = imageio.imread(filename)
                writer.append_data(image)

import matplotlib.pyplot as plt


class ImageRenderer:
    """
    Renderer that is used by the Grid environment. It plots a grid and each rectangle can have its own color.
    Additionally it is possible to plot arrows (left, right, up, down) to visualize a learned policy. The origin
    of the grid is the left-lower corner.
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def plot_grid(self):
        """
        Plots a grid with shape: width (=columns) x height (=rows)
        Returns
        -------

        """
        ax = plt.axes()

        # plot borders
        ax.plot((0, 0), (1, 0), linewidth=1, linestyle="--", c="black")
        ax.plot((0, 1), (1, 1), linewidth=1, linestyle="--", c="black")
        ax.plot((1, 1), (1, 0), linewidth=1, linestyle="--", c="black")
        ax.plot((0, 1), (0, 0), linewidth=1, linestyle="--", c="black")

        # plot grid
        for i in range(1, self.width):
            ax.plot((1 / self.width * i, 1 / self.width * i), (0, 1), linewidth=1, linestyle="--", c="black")
            ax.plot((0, 1), (1 / self.height * i, 1 / self.height * i), linewidth=1, linestyle="--", c="black")

    def plot_rect(self, pos, color):
        """
        Plots a
        Parameters
        ----------
        pos: position of the rectangle. lower-left corner = (0, 0)
        color: color that can be interpreted by matplotlib (e.g. black, red)

        Returns
        -------

        """
        rectangle = plt.Rectangle((pos[0] * 1 / self.width, pos[1] * 1 / self.height), 1 / self.width, 1 / self.height,
                                  fc=color)
        plt.gca().add_patch(rectangle)

    def plot_right(self, pos):
        plt.arrow(x=(pos[0] / self.width) + 0.02,
                  y=(pos[1] / self.height) + 1 / self.height / 2,
                  dx=(1 / self.width) - 0.05,
                  dy=0,
                  head_width=0.03,
                  head_length=0.02,
                  fc="black")

    def plot_left(self, pos):
        plt.arrow(x=((pos[0] + 1) / self.width) - 0.02,
                  y=(pos[1] / self.height) + 1 / self.height / 2,
                  dx=-1 / self.width + 0.05,
                  dy=0,
                  head_width=0.03,
                  head_length=0.02,
                  fc="black")

    def plot_up(self, pos):
        plt.arrow(x=pos[0] / self.width + 1 / self.width / 2,
                  y=pos[1] / self.height + 0.02,
                  dx=0,
                  dy=1 / self.height - 0.05,
                  head_width=0.03,
                  head_length=0.02,
                  fc="black")

    def plot_down(self, pos):
        plt.arrow(x=(pos[0] / self.width) + 1 / self.width / 2,
                  y=(pos[1] / self.height) + 1 / self.height - 0.02,
                  dx=0,
                  dy=-1 / self.height + 0.05,
                  head_width=0.03,
                  head_length=0.02,
                  fc="black")

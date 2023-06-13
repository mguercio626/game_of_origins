import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


class ScatterRunner:

    def __init__(self, universe, interval):
        self.interval = interval
        self.universe = universe

    def start(self):
        # Create the figure and axis
        fig, ax = plt.subplots()

        # Initialize an empty scatter plot
        scatter = ax.scatter([], [], c='blue')

        # Set the axis limits
        ax.set_xlim(0, self.universe.size_x)
        ax.set_ylim(0, self.universe.size_y)

        # Animation update function
        def update(frame):
            self.universe.update()

            # Update the scatter plot data
            scatter.set_offsets(self.universe.get_scatter_info())

            return scatter,

        # Create the animation
        animation = FuncAnimation(fig, update, frames=100, interval=self.interval, blit=True)

        # Show the animation
        plt.show()

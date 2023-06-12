import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from origins.em import create_particle


class ScatterRunner:

    def __init__(self, universe):
        self._universe = universe

    def start(self):
        # Create the figure and axis
        fig, ax = plt.subplots()

        # Initialize an empty scatter plot
        scatter = ax.scatter([], [], c='blue')

        # Set the axis limits
        ax.set_xlim(0, self._universe.x)
        ax.set_ylim(0, self._universe.y)

        # Animation update function
        def update(frame):
            self._universe.update()

            # Update the scatter plot data
            scatter.set_offsets(self.universe.get_scatter_info())

            return scatter,

        # Create the animation
        animation = FuncAnimation(fig, update, frames=100, interval=200, blit=True)

        # Show the animation
        plt.show()

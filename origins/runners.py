import networkx as nx
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
        scatter = ax.scatter([], [], c=[], cmap="coolwarm", edgecolors="black")
        # Set the axis limits
        ax.set_xlim(0, self.universe.size_x)
        ax.set_ylim(0, self.universe.size_y)

        # Animation update function
        def update(frame):
            self.universe.update()

            # Update the scatter plot data
            scatter.set_offsets(self.universe.get_positions())
            scatter.set_sizes(self.universe.get_masses())
            scatter.set_array(self.universe.get_charges())

            return (scatter,)

        # Create the animation
        animation = FuncAnimation(fig, update, frames=100, interval=self.interval, blit=True)

        # Show the animation
        plt.show()


class GraphRunner:
    def __init__(self, universe, interval):
        self.interval = interval
        self.universe = universe

    def start(self):
        plt.rcParams["figure.figsize"] = [7.50, 3.50]
        plt.rcParams["figure.autolayout"] = True

        # Create the figure and axis
        fig = plt.figure()

        # Animation update function
        def update(frame):
            self.universe.update()
            fig.clear()
            nx.draw(self.universe.particle_graph, with_labels=True)

        # Create the animation
        nx.draw(self.universe.particle_graph, with_labels=True)
        animation = FuncAnimation(fig, update, frames=100, interval=self.interval, blit=True)

        # Show the animation
        plt.show()

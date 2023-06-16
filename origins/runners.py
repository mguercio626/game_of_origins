import networkx as nx
from matplotlib import pyplot as plt, animation
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
        # plt.rcParams["figure.figsize"] = [7.50, 3.50]
        # plt.rcParams["figure.autolayout"] = True

        fig, ax = plt.subplots()
        ax.set_xlim(0, self.universe.size_x)
        ax.set_ylim(0, self.universe.size_y)

        G = self.universe.particle_graph

        positions = {atom: (atom.x, atom.y) for atom in self.universe.atoms}
        node_sizes = self.universe.get_masses()
        node_colors = self.universe.get_charges()
        nx.draw(
            G,
            positions,
            ax=ax,
            with_labels=False,
            node_size=node_sizes,
            node_color=node_colors,
            cmap="coolwarm",
            edge_color="black",
        )

        def animate(frame):
            ax.clear()
            self.universe.update()
            positions = {atom: (atom.x, atom.y) for atom in self.universe.atoms}

            ax.set_xlim(0, self.universe.size_x)
            ax.set_ylim(0, self.universe.size_y)
            nx.draw(
                G,
                positions,
                ax=ax,
                with_labels=False,
                node_size=node_sizes,
                node_color=node_colors,
                cmap="coolwarm",
                edge_color="black",
            )

        ani = animation.FuncAnimation(fig, animate, frames=100, interval=self.interval, repeat=True)

        plt.show()

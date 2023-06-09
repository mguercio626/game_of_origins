import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from origins.em import create_particle

# Create the figure and axis
fig, ax = plt.subplots()

# Initialize an empty scatter plot
scatter = ax.scatter([], [], c='blue')

# Set the axis limits
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

particles = [create_particle() for i in range(10)]

# Animation update function
def update(frame):
    # Generate new random data for each frame
    x = [particle['x'] for particle in particles]
    y = [particle['y'] for particle in particles]

    # Update the scatter plot data
    scatter.set_offsets(np.column_stack((x, y)))

    return scatter,

# Create the animation
animation = FuncAnimation(fig, update, frames=100, interval=200, blit=True)

# Show the animation
plt.show()

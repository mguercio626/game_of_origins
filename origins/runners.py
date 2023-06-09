import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Create the figure and axis
fig, ax = plt.subplots()

# Initialize an empty plot
line, = ax.plot([], [])

# Set the axis limits
ax.set_xlim(0, 10)
ax.set_ylim(-1, 1)

# Animation update function
def update(frame):
    x = np.linspace(0, 10, 1000)
    y = np.sin(2 * np.pi * (x - 0.01 * frame))
    line.set_data(x, y)
    return line,

# Create the animation
animation = FuncAnimation(fig, update, frames=100, interval=50, blit=True)

# Show the animation
plt.show()
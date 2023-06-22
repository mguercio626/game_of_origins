import random
from origins.visual import print_array
from pprint import pprint


def create_universe(size):
    """
    Creates the game of life universe.
    Parameters
    ----------
    x: int
        x-dimension of universe
    y: int
        y-dimension of universe
    """
    return [[random.randint(0,1) for x in range(5)]for y in range(5)]


def count_neighbors(universe, x, y):
    # Count number of active neighbors with wrap around.
    size = len(universe)
    count = universe[x][(y-1)%size] + universe[x][(y+1)%size] + \
            universe[(x-1)%size][y] + universe[(x+1)%size][y] + \
            universe[(x-1)%size][(y-1)%size] + universe[(x-1)%size][(y+1)%size] + \
            universe[(x+1)%size][(y-1)%size] + universe[(x+1)%size][(y+1)%size]
    return count


def update_universe(universe):
    """
    if a square has 4 or more neighbors then it dies.
    if a square has 0 or 1 neighbors it dies.
    if an empty square has 3 neighbors then it becomes alive.
    """
    size = len(universe)
    for x in range(size):
        for y in range(size):
            count=count_neighbors(universe,x,y)
            if count in [2,3]:
                universe[x][y]=1
            else:
                universe[x][y]=0



def run(size, n):
    """
    Run the simulation.
    x: int
        x-dimension of universe
    y: int
        y-dimension of universe
    n: int
        number of iterations
    """

    universe = create_universe(size)
    for i in range(n):
        update_universe(universe)
        pprint(universe)

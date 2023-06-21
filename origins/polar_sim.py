import random
from origins.runners import GraphRunner
from origins.universe import Ion, Universe, Electric, Exclusion

size_x = 5
size_y = 5

water = [Ion(x=1.9, y=1, vx=0, vy=0, mass=1, charge=1, name='H'),
         Ion(x=1.1, y=1.1, vx=0, vy=0, mass=1, charge=1, name='H'),
         Ion(x=1, y=1, vx=0, vy=0, mass=16, charge=-1, name='O')]


universe = Universe(water, size_x, size_y, forces=[Electric(0.1), Exclusion(0.01)])
runner = GraphRunner(universe, interval=(10))
runner.start()

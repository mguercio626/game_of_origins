import random
from origins.runners import GraphRunner
from origins.universe import Ion, Universe, Electric, Exclusion

water = [Ion(x=1.9, y=1, vx=0, vy=0, mass=1, charge=1, name='H'),
         Ion(x=1.1, y=1.1, vx=0, vy=0, mass=1, charge=1, name='H'),
         Ion(x=1, y=1, vx=0, vy=0, mass=16, charge=-1, name='O')]
size_x = 5
size_y = 5

atoms = []
for i in range(100):
    atom = Ion(max_x=size_x, max_y=size_y)
    atom.randomize()
    atoms.append(atom)

universe = Universe(water, size_x, size_y, forces=[Electric(0.01), Exclusion(0.01)])
runner = GraphRunner(universe, interval=(20))
runner.start()

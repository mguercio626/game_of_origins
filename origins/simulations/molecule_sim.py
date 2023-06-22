import random
from origins.runners import GraphRunner
from origins.universe import Ion, Universe, Electric, Exclusion

size_x = 5
size_y = 5

atoms = []
for i in range(100):
    atom = Ion(max_x=size_x, max_y=size_y)
    atom.randomize()
    atoms.append(atom)

universe = Universe(atoms, size_x, size_y, forces=[Electric(0.1), Exclusion(0.01)])
runner = GraphRunner(universe, interval=(10))
runner.start()

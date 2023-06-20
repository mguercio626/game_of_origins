import random
from origins.runners import GraphRunner
from origins.universe import Ion, Universe, Electric, Exclusion

# atoms = [Ion(x=10, y=10, vx=10, vy=10, mass=10, charge=10, name='A'),
#        Ion(x=20, y=20, vx=10, vy=10, mass=10, charge=10, name='B')
size_x = 50
size_y = 50

atoms = []
for i in range(100):
    atom = Ion(max_x=size_x, max_y=size_y)
    atom.randomize()
    atoms.append(atom)

universe = Universe(atoms, size_x, size_y, forces=[Electric(0.1), Exclusion(0.1)])
runner = GraphRunner(universe, interval=(20))
runner.start()

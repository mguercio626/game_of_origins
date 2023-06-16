import random
from origins.runners import GraphRunner
from origins.universe import Ion, Universe, Electric, Collision

# atoms = [Ion(x=10, y=10, vx=10, vy=10, mass=10, charge=10, name='A'),
#        Ion(x=20, y=20, vx=10, vy=10, mass=10, charge=10, name='B')]

atoms = []
for i in range(25):
    atom = Ion()
    atom.randomize()
    atoms.append(atom)

universe = Universe(atoms, 25, 25, forces=[Electric(10), Collision(1)])
runner = GraphRunner(universe, interval=(20))
runner.start()

import random
from origins.runners import ScatterRunner
from origins.universe import Ion, Universe, Electric

# atoms = [Ion(x=10, y=10, vx=10, vy=10, mass=10, charge=10, name='A'),
#        Ion(x=20, y=20, vx=10, vy=10, mass=10, charge=10, name='B')]

atoms = []
for i in range(10):
    atom = Ion()
    atom.randomize()
    atoms.append(atom)

universe = Universe(atoms, 25, 25, forces=[Electric(1)])
runner = ScatterRunner(universe, interval=(20))
runner.start()

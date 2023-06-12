import random
from origins.runner import ScatterRunner
from origins.universe import Ion, Universe, Electric


#def create_particle(max_x=10,max_y=10,max_x_speed=10,max_y_speed=10,min_charge=-10,max_charge=10,max_mass=10):
#    return {'x' : random.random()*max_x,
#            'y' : random.random()*max_y,
#            'vx' : random.random()*max_x_speed,
#            'vy' : random.random()*max_y_speed,
#            'charge' : random.randint(min_charge,max_charge),
#            'mass' : random.random()*max_mass}


atoms = []
for i in range(2):
    atom = Ion()
    atom.randomize()
    atoms.append(atom)
universe = Universe(atoms, 100, 100, forces=[Electric()])
runner = ScatterRunner(universe)
runner.start()
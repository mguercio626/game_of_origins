import random

def distance(atom1, atom2):
    x=atom1.x-atom2.x
    y=atom1.y-atom2.y
    return (x**2+y**2)**.5

def components(magnitude, atom1, atom2):
    x_dist = atom1.x - atom2.x
    y_dist = atom1.y - atom2.y
    total_dist =distance(atom1, atom2)
    xratio = abs(x_dist) / total_dist
    yratio = abs(y_dist) / total_dist
    x = magnitude * xratio
    y = magnitude * yratio
    return x, y


class Force():
    """
    The definition of a force.
    """
    def __init__(self, multiplier):
        self.multiplier = multiplier

    def apply(self, atoms):
        raise NotImplementedError("This is a base class, this method must be overridden in the derived class.")
    

class Wind(Force):
    """
    The definition of a force.
    """
    def apply(self, atoms):
        for atom in atoms:
            atom.x += self.multiplier


class Electric(Force):
    
    def force(self, atom1, atom2):
        return (self.multiplier * atom1.charge * atom2.charge) \
                /distance(atom1,atom2)**2
    
    def apply(self, atoms):

        def attractive(magnitude, atom1, atom2):
            if atom1.x<atom2.x:
                atom1.vx += abs(fx)/atom1.mass
                atom2.vx -= abs(fx)/atom2.mass
            else:
                atom1.vx -= abs(fx)/atom1.mass
                atom2.vx += abs(fx)/atom2.mass
            if atom1.y < atom2.y:
                atom1.vy += abs(fy)/atom1.mass
                atom2.vy -= abs(fy)/atom2.mass
            else:
                atom1.vy -= abs(fy)/atom1.mass
                atom2.vy += abs(fy)/atom2.mass

        def repulsive(magnitude, atom1, atom2):
            if atom1.x<atom2.x:
                atom1.vx -= abs(fx)/atom1.mass
                atom2.vx += abs(fx)/atom2.mass
            else:
                atom1.vx += abs(fx)/atom1.mass
                atom2.vx -= abs(fx)/atom2.mass
            if atom1.y < atom2.y:
                atom1.vy -= abs(fy)/atom1.mass
                atom2.vy += abs(fy)/atom2.mass
            else:
                atom1.vy += abs(fy)/atom1.mass
                atom2.vy -= abs(fy)/atom2.mass

        for atom1 in atoms:
             for atom2 in atoms:
                 if atom1 is not atom2:
                     magnitude = self.force(atom1,atom2)
                     fx, fy = components(magnitude, atom1, atom2)
                     if magnitude<0:
                         repulsive(magnitude,atom1,atom2)
                     else: 
                         attractive(magnitude,atom1,atom2)
        
                           
class Atom():
    """
    The most basic object in the universe.
    """
    def __init__(self, x=0, y=0, vx=0, vy=0, mass=0):
        self.max_x = 10
        self.max_y = 10
        self.max_vx = 10
        self.max_vy = 10
        self.max_mass = 10
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.mass = mass
    
    def randomize(self):
        self.x = random.random()*self.max_x
        self.y = random.random()*self.max_y
        self.vx = random.random()*self.max_vx
        self.vy = random.random()*self.max_vy
        self.mass = random.random()*self.max_mass

class Ion(Atom):

    def __init__(self, x=0, y=0, vx=0, vy=0, mass=0, charge=0):
        self.max_charge = 10
        self.min_charge = 10
        self.charge = charge
        super().__init__(x, y, vx, vy, mass)

    def randomize(self):
        self.charge = random.randint(self.min_charge, self.max_charge)
        super().randomize()



class Molecule():
    """
    A group of Atoms.
    """
    pass


class Universe():

    def __init__(self, atoms, size_x, size_y,  forces=[Electric(10)],
                 iteration_time=200):
        self.size_x = size_x
        self.size_y = size_y
        self.atoms = atoms
        self.forces = forces
        self.iteration_time = iteration_time

    def update(self):
        for atom in self.atoms:
            atom.x += atom.vx * self.iteration_time
            atom.y += atom.vy * self.iteration_time
        for force in self.forces:
            force.apply(self.atoms)

    def get_scatter_info(self):
        return [(atom.x,atom.y) for atom in self.atoms]

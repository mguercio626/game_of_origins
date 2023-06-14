from itertools import combinations
import random
import time

def distance(atom1, atom2):
    x=atom1.x-atom2.x
    y=atom1.y-atom2.y
    return (x**2+y**2)**.5

def components(magnitude, atom1, atom2):
    x_dist = atom1.x - atom2.x
    y_dist = atom1.y - atom2.y
    total_dist = distance(atom1, atom2)
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
    
    #def force(self, atom1, atom2):
    #    return (self.multiplier * atom1.charge * atom2.charge) \
    #            /distance(atom1,atom2)**2

    def force_components(self, atom1, atom2):
        """
        returns the x and y components of the force of atom2 on atom1.
        """
        dist = distance(atom1, atom2)
        magnitude = (self.multiplier * atom1.charge * atom2.charge)/dist**2
        xratio = (atom1.x - atom2.x) / dist
        yratio = (atom1.y - atom2.y) / dist
        #print(f"distance: {dist}, magnitude: {magnitude}, xratio: {xratio}, yratio: {yratio}")
        fx = magnitude * xratio 
        fy = magnitude * yratio
        return fx, fy

    
    def apply(self, atoms):

        #def attractive(magnitude, atom1, atom2):
        #    fx, fy = components(magnitude, atom1, atom2)
        #    if atom1.x<atom2.x:
        #        atom1.vx += abs(fx)/atom1.mass
        #        atom2.vx -= abs(fx)/atom2.mass
        #    else:
        #        atom1.vx -= abs(fx)/atom1.mass
        #        atom2.vx += abs(fx)/atom2.mass
        #    if atom1.y < atom2.y:
        #        atom1.vy += abs(fy)/atom1.mass
        #        atom2.vy -= abs(fy)/atom2.mass
        #    else:
        #        atom1.vy -= abs(fy)/atom1.mass
        #        atom2.vy += abs(fy)/atom2.mass

        #def repulsive(magnitude, atom1, atom2):
        #    fx, fy = components(magnitude, atom1, atom2)
        #    if atom1.x<atom2.x:
        #        atom1.vx -= abs(fx)/atom1.mass
        #        atom2.vx += abs(fx)/atom2.mass
        #    else:
        #        atom1.vx += abs(fx)/atom1.mass
        #        atom2.vx -= abs(fx)/atom2.mass
        #    if atom1.y < atom2.y:
        #        atom1.vy -= abs(fy)/atom1.mass
        #        atom2.vy += abs(fy)/atom2.mass
        #    else:
        #        atom1.vy += abs(fy)/atom1.mass
        #        atom2.vy -= abs(fy)/atom2.mass

        for atom1,atom2 in combinations(atoms,2):

            fx, fy = self.force_components(atom1, atom2)
            atom1.vx += fx/atom1.mass
            atom1.vy += fy/atom1.mass

            fx, fy = self.force_components(atom2, atom1)
            atom2.vx += fx/atom2.mass
            atom2.vy += fy/atom2.mass
            
            #magnitude = self.force(atom1,atom2)
            
            ##if magnitude<0:
            #   # repulsive(magnitude,atom1,atom2)
          #  #else: 
            #   # attractive(magnitude,atom1,atom2)
        
                           
class Atom():
    """
    The most basic object in the universe.
    """
    def __init__(self, x=0, y=0, vx=0, vy=0, mass=0, name='atom'):
        self.name = name
        self.max_x = 100
        self.max_y = 100
        self.max_vx = 10
        self.max_vy = 10
        self.max_mass = 5
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

    def __init__(self, x=0, y=0, vx=0, vy=0, mass=0, charge=0, name='ion'):
        self.max_charge = 10
        self.min_charge = -10
        self.charge = charge
        super().__init__(x, y, vx, vy, mass, name=name)

    def randomize(self):
        self.charge = random.randint(self.min_charge, self.max_charge)
        super().randomize()



class Molecule():
    """
    A group of Atoms.
    """
    pass


class Universe():

    def __init__(self, atoms, size_x, size_y,  forces=[Electric(10)]):
        self.size_x = size_x
        self.size_y = size_y
        self.atoms = atoms
        self.forces = forces
        self.t1 = None

    def update_position(self, atom, delta_t):
        """
        Update the position of an Atom.
        Atoms will bounce off the boundaries of the Universe.
        """

        future_x = atom.x + (atom.vx * delta_t)
        future_y = atom.y + (atom.vy * delta_t)

        if future_x <= 0 or future_x >= self.size_x:
            atom.vx*=-1
        if future_y <= 0 or future_y >= self.size_y:
            atom.vy*=-1

        atom.x += atom.vx * delta_t
        atom.y += atom.vy * delta_t

    def collisions(self,atoms,min_distance=1):
         for atom1,atom2 in combinations(atoms,2):
            if abs(atom1.x-atom2.x) < min_distance and \
            abs(atom1.y-atom2.y) < min_distance: 
                 atom1.vx *= -1
                 atom1.vy *= -1
                 atom2.vx *= -1
                 atom2.vx *= -1   

    def update(self):
        # Figure out the time since the last update.
        if self.t1 is None:
            self.t1 = time.time()
        t2 = time.time()
        delta_t = t2 - self.t1

        # Apply the forces to the atoms.
        # Applying a force changes the x and y velocity of the atoms.
        for force in self.forces:
            force.apply(self.atoms)
       
        #Prevents atoms from being in same location by having collisions 
        self.collisions(self.atoms)

         # Update the positions of the atoms.
        for atom in self.atoms:
            self.update_position(atom, delta_t)
        
        self.t1 = t2

    def get_scatter_info(self):
        return [(atom.x,atom.y) for atom in self.atoms]

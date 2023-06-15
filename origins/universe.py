from itertools import combinations
import random
import time

def distance(atom1, atom2):
    x=atom1.x-atom2.x
    y=atom1.y-atom2.y
    return (x**2+y**2)**.5


def components(magnitude, atom1, atom2):
    """
    returns the x and y components of the force of atom2 on atom1.
    """
    dist = max(distance(atom1, atom2), 1E-9)
    xratio = (atom1.x - atom2.x) / dist
    yratio = (atom1.y - atom2.y) / dist
    fx = magnitude * xratio
    fy = magnitude * yratio
    return fx, fy


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
        dist = max(distance(atom1, atom2), 1E-9)
        magnitude = (self.multiplier * atom1.charge * atom2.charge)/dist**2
        xratio = (atom1.x - atom2.x) / dist
        yratio = (atom1.y - atom2.y) / dist
        #print(f"distance: {dist}, magnitude: {magnitude}, xratio: {xratio}, yratio: {yratio}")
        fx = magnitude * xratio
        fy = magnitude * yratio
        return fx, fy

    def apply(self, atoms):

        for atom1,atom2 in combinations(atoms,2):

            fx, fy = self.force_components(atom1, atom2)
            atom1.vx += fx/atom1.mass
            atom1.vy += fy/atom1.mass

            fx, fy = self.force_components(atom2, atom1)
            atom2.vx += fx/atom2.mass
            atom2.vy += fy/atom2.mass


class Atom():
    """
    The most basic object in the universe.
    """
    def __init__(self, x=0, y=0, vx=0, vy=0, mass=0, name='atom'):
        self.name = name
        self.max_x = 25
        self.max_y = 25
        self.max_vx = 10
        self.max_vy = 10
        self.max_mass = 50
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
        self.max_charge = 2
        self.min_charge = -2
        self.charge = charge
        super().__init__(x, y, vx, vy, mass, name=name)

    def randomize(self):
        self.charge = random.randint(self.min_charge, self.max_charge)
        super().randomize()


class Molecule():
    """
    A group of Atoms.
    Maybe we don't need this.
    """
    pass


class Universe():

    def __init__(self, atoms, size_x, size_y, forces=[Electric(10)]):
        self.size_x = size_x
        self.size_y = size_y
        self.atoms = atoms
        self.bonds = {atom: set() for atom in atoms}
        self.forces = forces
        self.t1 = None

    def opposite_bond(self, atom1, atom2):
        if atom1.charge == -atom2.charge:
            self.bonds[atom1].add(atom2)
            self.bonds[atom2].add(atom1)
            return True
        else:
            return False

    def deflect(self, atom1, atom2):
        atom1.vx *= -1
        atom1.vy *= -1
        atom2.vx *= -1
        atom2.vx *= -1

    def update_atom_position(self, atom, delta_t):
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

    def update_molecule_position(self, molecule):
        """
        Update the position of a molecule.
        The new position of the atoms in a molecule need to be determined together.
        """

        # TODO: Need to update this code. its probably not working.
        atom1.vx = atom2.vx
        atom1.vy = atom2.vx
        bond_x, bond_y = components(bond_length, atom1, atom2)
        atom1.x = atom2.x + bond_x
        atom1.y = atom2.y + bond_y
        atom1.charge = 0
        atom2.charge = 0

    def find_molecules(self):
        """
        Looks in the dictionary self.bonds to find the set of molecules.
        """
        return []

    def collisions(self, atoms, min_distance=1, bond_length=0.5):
        """
        Handle Atom collisions.
        If two atoms collide either form a bond or deflect.
        """

        collisions = [(atom1, atom2) for atom1, atom2 in combinations(atoms,2)
                      if distance(atom1,atom2) < min_distance]
        for atom1, atom2 in collisions:
            bond_formed = self.opposite_bond(atom1, atom2)
            if not bond_formed:
                self.deflect(atom1, atom2)

    def update(self):
        """
        Update the Universe.
        """

        # Figure out the time since the last update.
        if self.t1 is None:
            self.t1 = time.time()
        t2 = time.time()
        delta_t = t2 - self.t1

        # Handle Atom collisions.
        self.collisions(self.atoms)

        # Apply the forces to the atoms.
        for force in self.forces:
            force.apply(self.atoms)

        # Update the positions of the atoms.
        free_atoms = [atom for atom in self.atoms if not len(self.bonds[atom])]
        for atom in free_atoms:
            self.update_atom_position(atom, delta_t)

        # Update the position of the molecules.
        # The function find_molecules needs to be written.
        molecules = self.find_molecules()
        for molecule in molecules:
            self.update_molecule_position(molecule, delta_t)

        self.t1 = t2

    def get_positions(self):
        return [(atom.x,atom.y) for atom in self.atoms]

    def get_masses(self):
        return [atom.mass for atom in self.atoms]

    def get_charges(self):
        return [atom.charge for atom in self.atoms]

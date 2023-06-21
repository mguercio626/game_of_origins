from itertools import combinations
import random
import statistics
import time
import networkx as nx


def distance(atom1, atom2):
    """
    Returns the distance between two atoms
    """
    x = atom1.x - atom2.x
    y = atom1.y - atom2.y
    return (x**2 + y**2) ** 0.5


def components(magnitude, atom1, atom2):
    """
    Returns the x and y components of the force of atom2 on atom1
    """
    dist = max(distance(atom1, atom2), 1e-9)
    xratio = (atom1.x - atom2.x) / dist
    yratio = (atom1.y - atom2.y) / dist
    fx = magnitude * xratio
    fy = magnitude * yratio
    return fx, fy


class Force:
    """
    This represents the base class for all of the forces in the universe
    """

    def __init__(self, multiplier):
        self.multiplier = multiplier

    def apply(self, atoms):
        raise NotImplementedError("This is a base class, this method must be overridden in the derived class.")


class Wind(Force):
    """
    This represents an extended class for a basic force to replicate wind.
    """

    def apply(self, atoms):
        for atom in atoms:
            atom.x += self.multiplier


class Electric(Force):
    """ "
    The definition of an electrical force between atoms with charges.
    """

    def force_components(self, atom1, atom2):
        """
        Returns the x and y components of the force of atom2 on atom1.
        """
        dist = max(distance(atom1, atom2), 1e-9)
        magnitude = (self.multiplier * atom1.charge * atom2.charge) / dist**2
        xratio = (atom1.x - atom2.x) / dist
        yratio = (atom1.y - atom2.y) / dist

        fx = magnitude * xratio
        fy = magnitude * yratio
        return fx, fy

    def apply(self, atoms):
        """
        This finds and applies the electrical force between all combinations of 2 atoms in the universe"
        """
        for atom1, atom2 in combinations(atoms, 2):
            fx, fy = self.force_components(atom1, atom2)
            atom1.vx += fx / atom1.mass
            atom1.vy += fy / atom1.mass

            fx, fy = self.force_components(atom2, atom1)
            atom2.vx += fx / atom2.mass
            atom2.vy += fy / atom2.mass


class Exclusion(Force):
    """
    The definition of a force due to atoms becoming too close to each other
    """

    def force_components(self, atom1, atom2):
        """
        Returns the x and y components of the force of atom2 on atom1.
        """
        dist = max(distance(atom1, atom2), 1e-9)
        magnitude = (-1 * self.multiplier * atom1.charge * atom2.charge) / (dist*10)**3
        xratio = (atom1.x - atom2.x) / dist
        yratio = (atom1.y - atom2.y) / dist

        fx = magnitude * xratio
        fy = magnitude * yratio
        return fx, fy

    def apply(self, atoms):
        """
        This finds and applies the electrical force between all combinations of 2 atoms in the universe"
        """
        for atom1, atom2 in combinations(atoms, 2):
            fx, fy = self.force_components(atom1, atom2)
            atom1.vx += fx / atom1.mass
            atom1.vy += fy / atom1.mass

            fx, fy = self.force_components(atom2, atom1)
            atom2.vx += fx / atom2.mass
            atom2.vy += fy / atom2.mass


class Atom:
    """
    The most basic object in the universe.
    """

    def __init__(self, x=0, y=0, vx=0, vy=0, mass=0, name="atom", max_x=25, max_y=25):
        self.name = name
        # Maximum positions, velocities, and masses of all atoms when randomly generating atoms
        self.max_x = max_x
        self.max_y = max_y
        self.max_vx = 10
        self.max_vy = 10
        self.max_mass = 50
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.mass = mass

    def randomize(self):
        """
        This randomly generates atom's positions, velcoties, and masses
        """
        self.x = random.random() * self.max_x
        self.y = random.random() * self.max_y
        self.vx = random.random() * self.max_vx
        self.vy = random.random() * self.max_vy
        self.mass = random.random() * self.max_mass


class Ion(Atom):
    """
    An extended class of atoms that has charges.
    """

    def __init__(self, x=0, y=0, vx=0, vy=0, mass=0, charge=0, name="ion", *args, **kwargs):
        # Maximum and minimum charges of ions randomly generated
        self.max_charge = 2
        self.min_charge = -2
        self.charge = charge
        super().__init__(x, y, vx, vy, mass, name=name, *args, **kwargs)

    def randomize(self):
        self.charge = random.randint(self.min_charge, self.max_charge)
        super().randomize()


class Universe:
    """
    The universe in which all objects exist.
    """

    def __init__(self, atoms, size_x, size_y, forces=[Electric(10)]):
        self.size_x = size_x
        self.size_y = size_y
        self.atoms = atoms
        self.forces = forces
        self.t1 = None
        self.particle_graph = nx.Graph()
        self.particle_graph.add_nodes_from(atoms)

    def opposite_bond(self, atom1, atom2):
        if atom1.charge == -atom2.charge:
            self.particle_graph.add_edge(atom1, atom2)
            return True
        else:
            return False

    def deflect(self, atom1, atom2):
        atom1.vx *= -0.5
        atom1.vy *= -0.5
        atom2.vx *= -0.5
        atom2.vx *= -0.5

    def update_atom_position(self, atom, delta_t):
        """
        Update the position of an Atom.
        Atoms will bounce off the boundaries of the Universe.
        """

        future_x = atom.x + (atom.vx * delta_t)
        future_y = atom.y + (atom.vy * delta_t)

        if future_x <= 0 or future_x >= self.size_x:
            atom.vx *= -0.5
        if future_y <= 0 or future_y >= self.size_y:
            atom.vy *= -0.5

        atom.x += atom.vx * delta_t
        atom.y += atom.vy * delta_t

    def update_molecule_position(self, molecule, delta_t):
        """
        Update the position of a molecule.
        The new position of the atoms in a molecule need to be determined together.
        """
        vx = statistics.mean([atom.vx for atom in molecule])
        vy = statistics.mean([atom.vy for atom in molecule])
        for atom in molecule:
            atom.vx = vx
            atom.vy = vy
            self.update_atom_position(atom, delta_t)

        # Skip this code for now, becuase its not working yet.
        return
        # TODO: Need to update this code. its probably not working.
        atom1.vx = atom2.vx
        atom1.vy = atom2.vx
        bond_x, bond_y = components(bond_length, atom1, atom2)
        atom1.x = atom2.x + bond_x
        atom1.y = atom2.y + bond_y
        atom1.charge = 0
        atom2.charge = 0

    def collisions(self, min_distance=1, bond_length=0.5):
        """
        Handle Atom collisions.
        If two atoms collide either form a bond or deflect.
        """

        collisions = [
            (atom1, atom2) for atom1, atom2 in combinations(self.atoms, 2) if distance(atom1, atom2) < min_distance
        ]
        for atom1, atom2 in collisions:
            bond_formed = self.opposite_bond(atom1, atom2)
        # if not bond_formed:
        # self.deflect(atom1, atom2)

    def break_bonds(self, max_bond_dist=2):
        bonds = self.particle_graph.edges
        for atom1, atom2 in bonds:
            if distance(atom1, atom2) > max_bond_dist:
                self.particle_graph.remove_edge(atom1, atom2)

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
        self.collisions()
        self.break_bonds()

        # Apply the forces to the atoms.
        for force in self.forces:
            force.apply(self.atoms)

        # Separate atoms and molcules and update positions
        #for component in nx.connected_components(self.particle_graph):
        #    if len(component) == 1:
        #        self.update_atom_position(component.pop(), delta_t)
        #    elif len(component) > 1:
        #        self.update_molecule_position(component, delta_t)
        for atom in self.atoms:
            self.update_atom_position(atom, delta_t)

        self.t1 = t2

    def get_positions(self):
        """
        Returns the (x,y) positions for all atoms in the universe
        """
        return [(atom.x, atom.y) for atom in self.atoms]

    def get_masses(self):
        """
        Returns the masses for all atoms in the universe
        """
        return [atom.mass for atom in self.atoms]

    def get_charges(self):
        """
        Returns the charges for all atoms in the universe
        """
        return [atom.charge for atom in self.atoms]

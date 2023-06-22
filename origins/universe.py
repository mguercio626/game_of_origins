from itertools import combinations
import random
import statistics
import time
import networkx as nx

from origins.forces import Electric
from origins.calculations import distance, components


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

from itertools import combinations
from origins.calculations import distance, components

class Force:
    """
    This represents the base class for all of the forces in the universe
    """

    def __init__(self, multiplier):
        self.multiplier = multiplier


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

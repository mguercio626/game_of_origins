
class Force():
    """
    The definition of a force.
    """
    pass


class Atom():
    """
    The most basic object in the universe.
    """
    pass


class Molecule():
    """
    A group of Atoms.
    """
    pass


class Universe():

    def __init__(self, atoms, forces, x, y):
        self.x = x
        self.y = y
        self._atoms = atoms
        self._forces = forces

    def update():
        for force in self._forces:
            apply_force(atoms, force)

    def get_scatter_info():
        return [(atom['x'],atom['y']) for atom in self._atoms]

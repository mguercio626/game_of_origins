import random

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

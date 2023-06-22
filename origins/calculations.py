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

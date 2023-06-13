from origins.universe import Ion, Universe, Electric



def test_y0():
    print("Y0")
    atom1 = Ion(x=10, y=0, vx=10, vy=10, mass=10, charge=10, name='A')
    atom2 = Ion(x=20, y=0, vx=10, vy=10, mass=10, charge=10, name='A')
    electric = Electric(1)
    print(electric.force_components(atom1, atom2))
    print(electric.force_components(atom2, atom1))

def test_x0():
    print("X0")
    atom1 = Ion(x=0, y=10, vx=10, vy=10, mass=10, charge=7, name='A')
    atom2 = Ion(x=0, y=20, vx=10, vy=10, mass=10, charge=7, name='A')
    electric = Electric(1)
    print(electric.force_components(atom1, atom2))
    print(electric.force_components(atom2, atom1))

def test_angle():
    print("X0")
    atom1 = Ion(x=0, y=0, vx=10, vy=10, mass=10, charge=7, name='A')
    atom2 = Ion(x=10, y=10, vx=10, vy=10, mass=10, charge=7, name='A')
    electric = Electric(1)
    print(electric.force_components(atom1, atom2))
    print(electric.force_components(atom2, atom1))

def test_opposites():
    print("X0")
    atom1 = Ion(x=0, y=0, vx=10, vy=10, mass=10, charge=7, name='A')
    atom2 = Ion(x=10, y=10, vx=10, vy=10, mass=10, charge=-7, name='A')
    electric = Electric(1)
    print(electric.force_components(atom1, atom2))
    print(electric.force_components(atom2, atom1))


test_y0()
test_x0()
test_angle()
test_opposites()
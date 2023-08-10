# Origins
This project is a from-scratch mathematical/computational exploration of the origin of life.
Specifically to understand how complexity can emerge from building blocks and forces.
For our purposes, we define life as something that has self-replication.

This project is still in its early stages.

---

## Installation

```
pip install -e .
```
---

## Features

#### Visualization

- matplotlib scatter plotter
- networkx plotter

#### Universe

The Universe is the object that has atoms and forces.
The Universe applies the forces to the atoms, and updates their positions.
To create a Universe you supply it with the atoms and the forces that you want to use.

- Universe - pure python universe
- NumpyUniverse - Universe that uses numpy. (todo)
- GPUUniverse - Universe that uses gpu. (todo)


#### Atoms

Atoms are the basic building blocks.

- Atom - an atom with a mass
- Ion - atom with a mass and charge


#### Forces

A Force changes the velocity of the atoms.

- Wind - A Force moves atoms in a fixed direction.
- Electric - A Force that attracts or repels atoms to each other based on their charge.
- Exclusion - A Force that prevents atoms from occupying the same location.
- Gravity - A Force the causes masses to be attracted to each other. (todo)

#### Runners

A runner is the object that runs the Universe or Universes, and displays the results.  So far this just means visualization. Eventually we would like this to include to multiprocess, multinode, and gpu simulations.

---

## Usage

```
# Imports
import random
from origins.runners import GraphRunner
from origins.universe import Universe
from origins.atoms import Ion
from origins.forces import Electric, Exclusion

# Make some Atoms:
atoms = [Ion(x=1.9, y=1, vx=0, vy=0, mass=1, charge=1, name='H'),
         Ion(x=1.1, y=1.1, vx=0, vy=0, mass=1, charge=1, name='H'),
         Ion(x=1, y=1, vx=0, vy=0, mass=16, charge=-1, name='O')]

# Make some Forces:
forces=[Electric(0.1), Exclusion(0.01)]

# Make the Universe and give it your atoms and forces.
size_x = 5
size_y = 5
universe = Universe(atoms, size_x, size_y, forces=forces)

# Pass the Universe to the Runner, which will run the universe and do visualization.
runner = GraphRunner(universe, interval=(10))
runner.start()
```

## Simulations

The python scripts located in the simulations folder run simulations that have notable properties. For example, polar_sim.py has a Universe with Electric and Exclusion forces and three atoms resembling the Hydrogen and Oxygen of water. Two of the atoms are negatively charged, and one is is positively charged. They fail to form a stable molecule because the two negatively charged atoms repel each other. This suggests that point charges are not sufficient to produce complexity like life. What else is necessary to form stable molecules and create greater complexity?


## Universal Measurements

We plan to add code to quantify the complexity of the simulation. This would allow us to start to understand the effects of the forces and atoms on complexity.

This would also let us brute force a large number of simulations and pick out the most interesting ones or determine the correlation between the parameters and complexity.

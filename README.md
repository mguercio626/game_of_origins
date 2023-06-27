# Origins
This project is a mathematical/computational exploration of the origin of life.
Specifially, to understand how complextity can emerge from a set of building blocks and forces.
For our purposes we define life as something that has self-replication.

This project is still in it's early stages.

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

A runner is the object that runs the Universe or Universes, and displays the results.  So far this just means visualization. Eventually we would like this to expand to multiprocess, multinode, and gpu simulations.

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

The python scripts located in the simulations folder run simulations that have notable properties. For example polar_sim.py has a Universe with Electric and Exclusion forces, and three atoms that resemble the two Hydrogen and Oxygen of water. Two atoms are negatively charged and the other is positively charged. They fail to form a stable molecule because the two negatively charged atoms repel each other. Which suggests that point charges are not sufficient from produce complexity like life. What else is neccessary to form stable molecules, and produce greater complexity?


## Universal Measurements

We plan to add code to quantify the complexity of the simulation, this would allow us to start to understand the effects of the forces and atoms on complexity.

This would also let us brute force large number of simulations and pick out the most interesting ones, or determine the correlation between the parameters and complexity.

---

## Garrett thoughts.
Before I share my thoughts I want to preface them by saying that I don't know much about this topic.

I think the general problem of the origin of life is a mathmatical and computational problem, while the specific problem of life in our universe is an experimental problem.

The second law of thermodynamics says that the entropy of the universe will always increase over time. Another way of stating the second law of thermodynamics is that energy will always become less clumped up over time.  The second law of thermodynamics is true because the unordered state is more probable. So you could say that the universe progresses to the more probable.

We could define life as something that self replicates.  Self-replication has exponential growth. Once we introduce life into the universe, the ordered state of self-replicators starts to become more probable, relative to the disordered state. Perhaps another way to describe evolution, other than the phrase, "survival of the fittest", is survival of the most probable.

Life appears to be resisting the march towards entropy, at the cost of energy.  The overall entropy of the system is still increasing.

Self-replication requires actuation, logic, and composition of these components. Maybe we can figure out some of the requirements for logic and actuation to emerge. Or, given a system that has logic and actuation, understand some of the requirements for self-replication to emerge.

Maybe we can use AI to improve the computation speed. Instead of computing the value of n(n+1)/2 forces (between each combination of atoms) and then upding the atom positions, maybe we can train an AI make a good guess at the particle positions of the next iteration.

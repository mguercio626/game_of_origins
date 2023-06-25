# Origins
The purpose of this project is to explore the origin of life.
Specifially, to understand how complextity can emerge from a set of building blocks and forces.

This project is still in its early stages.

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


## Installation

```
pip install -e .
```

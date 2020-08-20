# Object-oriented Serpent input generator
The code will allow to generate input files for [Serpent](https://www.sciencedirect.com/science/article/pii/S0306454914004095). The application is thought for the computation of multi-group cross-sections in nuclear reactors with pin-lattice geometry.

## Geometry Definition
The following objects can be used to define the geometry of the problem:
- Pin: elementary unit.
- Group: an ensemble of pins or an ensemble of "ensembles of pins".
- Root: universe zero associated to the boundary conditions.

## Materials Definition
The material object contains: name, composition, temperature, density, and information on S(\alpha, \beta) library.

## Cross-sections
- Selection of group interfaces/structure.
- Methodology to compute cross-sections, e.g. B1, P1.

## Detectors
Definition of tallies/detectors on  Cartesian grid.

## Fission Matrix
Defintion of the fission matrix on a Cartesian grid.

## Criticality Cycle
Parameters corresponding to the options in "set pop" card.

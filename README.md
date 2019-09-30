# Project: serpent-writer
The code will allow to generate [Serpent](https://www.sciencedirect.com/science/article/pii/S0306454914004095) input-files for the computation of multi-group cross-sections of reactors with pin-lattice geometry. 

## Geometry Definition
The following objects can be used to define the geometry of the problem:
- Pin: elementary unit.
- Group: an ensemble of pins or an ensemble of "an ensemble of pins".
- Root: universe zero to which the boundary conditions are associated.

## Materials Definition
The material object contains: name, composition, temperature, density, and information on S(\alpha, \beta) library.

## Cross-sections
The following two options are allowed:
- Selection of group interfaces/structure.
- Methodology to compute cross-sections, e.g. B1, P1.

## Detectors
It is allowed to define tallies/detectors on  Cartesian grid. 

## Fission Matrix
The fission matrix of the problem can be computed on a Cartesian grid.

## Criticality Cycle
Parameters corresponding to the options in "set pop" card can be defined.



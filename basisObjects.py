""" The script contains the  super-cells building blocks"""


class PinCell:
    """
    Class to define the a pin unit

    Parameters
    ----------
    name: string
        ID for pin
    dimensions: tuple
        radii vector
    materials: tuple
        materials vector

    Attributes
    ----------
    name: string
        ID for pin
    radii: tuple
        radii vector
    materials: tuple
        materials vector.
        It must have same length of radii
    """

    def __init__(self, name, dimensions, materials):
        self.name = name
        self.radii = dimensions
        self.materials = materials
        self._pre_check()

    def _pre_check(self):
        assert(isinstance(self.name, str))
        assert(isinstance(self.radii, tuple))
        assert(isinstance(self.materials, tuple))
        assert(len(self.radii) == len(self.materials))


class AssmCell:
    """
        Class to define the an assembly unit

        Parameters
        ----------
        name: str
            Name of super-cell
        pin_map: tuple
            Pins Map
        pitch: float
``          Pitch between assemblies
        type_lattice: string
            Type of lattice. Currently
            Cartesian is the only option

        Attributes
        ----------
        name: str
            Name of super-cell
        pin_map: tuple
            Pins Map
        pitch: float
``          Pitch between assemblies
        type_lattice: string
            Type of lattice. Currently
            "cartesian" is the only option
        """

    def __init__(self, name, pin_map, pitch, type_lattice='square'):
        self.name = name
        self.map = pin_map
        self.pitch = pitch
        self.typeLattice = type_lattice

    def _pre_check(self):
        assert(isinstance(self.name, str))
        assert(isinstance(self.map, tuple))
        assert(isinstance(self.pitch, float))
        assert(isinstance(self.typeLattice, str))


class SuperCell:
    """
    Class to define the a super-cell unit,
    e.g assembly and reflector, or single
    assembly

    Parameters
    ----------
    name: str
        Name of super-cell
    assm_map: tuple
        Assembly Map
    pitch: float
        Pitch between assemblies
    boundary_condition: string
        String for boundary conditions

    Attributes
    ----------
    name: string
        ID for the super-cell
    map: tuple
        Assembly map
    bc: string
        Contains boundary conditions,
        'reflective': reflective bc
        'vacuum': vacuum bc
        'periodic': periodic bc
    """

    def __init__(self, name, assm_map, pitch, boundary_condition):
        self.name = name
        self.map = assm_map
        self.pitch = pitch
        self.bc = boundary_condition
        self._pre_check()

    def _pre_check(self):
        assert(isinstance(self.name, str))
        assert(isinstance(self.map, tuple))
        assert(self.bc == 'reflective' or self.bc == 'vacuum')


class GeometryStructure:
    """
    Class containing information on the full geometry

    Parameters
    ----------
    name: string
        ID for the super-cell
    pin_set: object
        Tuple of PinCell objects
    assm_set: object
        Tuple of AssmCell objects
   super_cell: object
        Contains the super-cell specifications


    Attributes
    ----------
    name: string
        ID for the super-cell
    pins: object
        Tuple of PinCell objects
    assemblies: object
        Tuple of AssmCell objects
    cell: object
        Contains the super-cell specifications
    bc: string
        Contains boundary conditions,
        'reflective': reflective bc
        'vacuum': vacuum bc
        'periodic': periodic bc
    """

    def __init__(self, name, pin_set, assm_set, super_cell):
        self.name = name
        self.pins = pin_set
        self.assemblies = assm_set
        self.cell = super_cell
        self.bc = super_cell.bc


class Material:
    """
    Materials class

    Parameters
    ----------
    name: string
        ID for the super-cell
    density: float
        density in g/cc
    temperature: float
        material temperature in K
    composition: list
        list containing zaids and corresponding number densities
    moder: int
        moder=0, no moderator
        moder='' library utilized for the moderator

    Attributes
    ----------
    name: string
        ID for the super-cell
    density: float
        density in g/cc
    temperature: float
        material temperature in K
    composition: list
        list containing zaids and corresponding number densities
    moder: int
        moder=0, no moderator
        moder='' library utilized for the moderator

    """

    def __init__(self, name, density, temperature, composition, moder=0):
        self.name = name
        self.density = density
        self.temperature = temperature
        self.composition = composition
        self.moder = moder

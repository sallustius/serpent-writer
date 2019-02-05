""" The script contains the  super-cells building blocks. See the classes'
docstrings for more information

    1) Pin(name, dimensions, materials)
    2) Assm(name, pin_map, pitch, type_lattice)
    3) Cell(name, assm_map, pitch, type_lattice)
    4) Geometry(name, pin_set, assm_set, bc)
    5) Material(name, density, temperature, composition, moder)
    6) FissionMatrix(type_fm, limits)
"""
MAX_NUM = 1e+37


class Pin:
    """
    Class to define the a pin unit

    Parameters
    ----------
    name: string
        ID for pin
    dimensions: list
        radii vector
    materials: list
        materials vector

    Attributes
    ----------
    name: string
        ID for pin
    radii: list
        radii vector
    materials: list
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
        assert(isinstance(self.radii, list))
        assert(isinstance(self.materials, list))
        assert(len(self.radii) == len(self.materials))


class Assm:
    """
        Class to define the an assembly unit

        Parameters
        ----------
        name: str
            Name of super-cell
        pin_map: list
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
        pin_map: list
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
        assert(isinstance(self.map, list))
        assert(isinstance(self.pitch, float))
        assert(isinstance(self.typeLattice, str))


class Cell:
    """
    Class to define the a super-cell unit,
    e.g assembly and reflector, or single
    assembly

    Parameters
    ----------
    name: str
        Name of super-cell
    assm_map: list
        Assembly Map
    pitch: float
        Pitch between assemblies
    boundary_condition: string
        String for boundary conditions

    Attributes
    ----------
    name: string
        ID for the super-cell
    map: list
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
        assert(isinstance(self.map, list))
        assert(self.bc == 'reflective' or self.bc == 'vacuum'
               or self.bc == 'periodic')


class Geometry:
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
        List of PinCell objects
    assm: object
        List of AssmCell objects
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
        self.assm = assm_set
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


class FissionMatrix:
    """
    The class appends fission matrix specifications for Serpent files

    Parameters
    ----------
    limits: list or tuple
        six-elements list containing fission matrix limits
    type_fm: str
        cartesian is currently the only allowed value

    Attributes
    ----------
    Limits: list or tuple
        six-elements list containing fission matrix limits
    typeFM: str
        cartesian is currently the only allowed value

"""

    def __init__(self, type_fm='cartesian',
                 limits=(0, 1, 10, 0, 1, 10, -MAX_NUM, MAX_NUM, 1)):
        self.typeFM = type_fm
        self.Limits = limits

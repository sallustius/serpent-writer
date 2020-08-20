""" The script contains the building blocks for geometry and material.

    1) Pin(name, dimensions, materials)
    2) Group(name, pin_map, pitch, type_lattice)
    3) Root(name, group_map, pitch, type_lattice)
    4) Geometry(name, pin_set, group_set, bc)
    5) Material(name, density, temperature, composition, moder)
    6) Detector(type, limits, numberOfElements)
    7) FissionMatrix(type_fm, limits)
    8) XSecGeneration(GroupInterfaces, universes)

    Enhancements:
    1) Add fum option to the cross-sections
    2) Add burn, vol, tmp, tft, rgb, fix options to material card
    3) Add different options for root
"""
MAX_NUM = 1e+37
detectorDictionary = {'fissionSource': '-7', 'power': '-8'}


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


class Group:
    """
        Class to define the an assembly unit

        Parameters
        ----------
        name: str
            Name of super-cell
        pin_map: list
            Pins Map
        pitch: float
            Pitch between assemblies
        type_lattice: string
            Type of lattice. Currently
            square or stack

        Attributes
        ----------
        name: str
            Name of super-cell
        pin_map: list
            Pins Map
        pitch: float
            Pitch between assemblies
        type_lattice: string
            Type of lattice
        """

    def __init__(self, name, pin_map, pitch, type_lattice='square'):
        self.name = name
        self.map = pin_map
        self.pitch = pitch
        self.typeLattice = type_lattice

    def _pre_check(self):
        assert(isinstance(self.name, str))
        assert(isinstance(self.map, list))
        assert(isinstance(self.typeLattice, str))
        assert (self.typeLattice == 'square' or self.typeLattice == 'stack')


class Root:
    """
    Class to define the universe zero associated to the boundary conditions

    Parameters
    ----------
    name: str
        Name of super-cell
    group_map: list
        Assembly Map
    pitch: float
        Pitch between assemblies
    boundary_condition: list
        String for boundary conditions.
        bc[0]: radial b.c.
        bc[1]: axial b.c.

    Attributes
    ----------
    name: string
        ID for the super-cell
    map: list
        Assembly map
    bc: list
        Two-elements list containing boundary conditions,
        'reflective': reflective bc
        'vacuum': vacuum bc
        'periodic': periodic bc
    """

    def __init__(self, name, group_map, pitch, boundary_condition):
        self.name = name
        self.map = group_map
        self.pitch = pitch
        self.bc = boundary_condition
        self._pre_check()

    def _pre_check(self):
        assert(isinstance(self.name, str))
        assert(isinstance(self.map, list))
        assert(self.bc[0] == 'reflective' or self.bc[0] == 'vacuum'
               or self.bc[0] == 'periodic')
        assert (self.bc[1] == 'reflective' or self.bc[1] == 'vacuum'
                or self.bc[1] == 'periodic')



class Root:
    """
    Class to define the universe zero associated to the boundary conditions

    Parameters
    ----------
    name: str
        Name of super-cell
    dimensions: list
        L_x, L_y, L_z
    boundary_condition: list
        String for boundary conditions.
        bc[0]: radial b.c.
        bc[1]: axial b.c.

    Attributes
    ----------
    name: string
        ID for the super-cell
    dimensions: list
        Assembly map
    bc: list
        Two-elements list containing boundary conditions,
        'reflective': reflective bc
        'vacuum': vacuum bc
        'periodic': periodic bc
    """

    def __init__(self, name, dimensions, boundary_condition):
        self.name = name
        self.dimensions = dimensions
        self.bc = boundary_condition
        self._pre_check()

    def _pre_check(self):
        assert(isinstance(self.name, str))
        assert(isinstance(self.dimensions, list))
        assert(self.bc[0] == 'reflective' or self.bc[0] == 'vacuum'
               or self.bc[0] == 'periodic')
        assert (self.bc[1] == 'reflective' or self.bc[1] == 'vacuum'
                or self.bc[1] == 'periodic')


class Geometry:
    """
    Class containing full geometry. Input for the writer.

    Parameters
    ----------
    name: string
        ID for the super-cell
    pin_set: object
        Tuple of PinCell objects
    group_set: object
        Tuple of GroupCell objects
    super_cell: object
        Contains the super-cell specifications


    Attributes
    ----------
    name: string
        ID for the super-cell
    pins: object
        List of PinCell objects
    group: object
        List of GroupCell objects
    root: object
        Contains the super-cell specifications
    """

    def __init__(self, name, pin_set, group_set=None, root=None):
        self.name = name
        self.pins = pin_set
        self.group = group_set
        self.root = root


class Material:
    """
    Materials class

    Parameters
    ----------
    name: string
        ID for the super-cell
    density: str
        density in g/cc
    temperature: str
        material temperature in K
    composition: list
        list containing zaids and corresponding number densities
    moder: str
        moder=None, no moderator
        moder='' library utilized for the moderator

    Attributes
    ----------
    name: string
        ID for the super-cell
    density: str
        density in g/cc
    temperature: str
        material temperature in K
    composition: list
        list containing zaids and corresponding number densities
    moder: str
        moder=None, no moderator
        moder='' library utilized for the moderator
    param: str
        'mass' concentration
        'molar' concentration
    """

    def __init__(self, name, density, temperature, composition,
                 param='mass', moder=None, modeName='lwtr'):
        self.name = name
        self.density = density
        self.temperature = temperature
        self.composition = composition
        self.param = param
        self.moder = moder
        self.moderName = modeName

    def _pre_check(self):
        assert(isinstance(self.name, str))
        assert (isinstance(self.density, str))
        assert(isinstance(self.temperature, str))
        assert(isinstance(self.composition, list))
        assert(self.param == 'mass' or self.param == 'molar')
        assert(isinstance(self.moder, str))
        assert(isinstance(self.modeName, str))


class Detector:
    """
    The class defines a detector defined on a Cartesian grid.

    Parameters
    -----------
    name: str
        name of the detector
    limits: list
        lengths of discretized domain on x, y, and z direction
    nx_ny_nz: list
        number of elements along x, y, and z
    det_type: str
        type of detector. Allowed values are 'fissionSource' and 'power'

    Attributes
    -----------
    name: str
        name of the detector
    dimensions: list
        extension of the domain assuming origin in zero
    nx_ny_nz: list
        number of elements along x, y, and z direction
    detectorType: str
        type of detector. Allowed values are 'fissionSource' and 'power'.
    """

    def __init__(self, name, limits=(0, 1, 0, 1, -MAX_NUM, MAX_NUM),
                 nx_ny_nz=(10, 10, 1), det_type='fissionSource'):
        self.name = name
        self.dimensions = limits
        self.numberOfCells = nx_ny_nz
        self.detectorType = detectorDictionary[det_type]
        self._pre_check()

    def _pre_check(self):
        assert(isinstance(self.name, str))
        assert(isinstance(self.dimensions, list))
        assert (isinstance(self.numberOfCells, list))
        assert(isinstance(self.detectorType, str))


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
    numberOfCells: list
        number of cells in x-y-z directions
    dimensions: list or tuple
        six-elements list containing fission matrix limits
    typeFM: str
        'Cartesian' is currently the only allowed value
"""

    def __init__(self, type_fm='cartesian',
                 limits=(0, 1, 0, 1, -MAX_NUM, MAX_NUM),
                 nx_ny_nz=(1, 1, 10)):
        self.typeFM = type_fm
        self.dimensions = limits
        self.numberOfCells = nx_ny_nz

    def _pre_check(self):
        assert(isinstance(self.typeFM, str))
        assert(isinstance(self.dimensions, list))
        assert(isinstance(self.numberOfCells, list))


class XSecGeneration:
    """
    The object contains information for cross-sections' generation

    Parameters
    ----------
    universes: list or tuple
        list containing universes for which cross-sections are generated
    name_group: str
        Name of group structure
    group_boundaries: list
        Group boundaries (G+1)

    Attributes
    ----------
    universes: list or tuple
        list containing universes for which cross-sections
    name_group: str
        Name of group structure
    nameStructure: list
        Group boundaries (G+1)
    """
    def __init__(self, name_group='default2',
                 group_boundaries=None, universes=None):
        self.universes = universes
        self.groupBoundaries = group_boundaries
        self.nameStructure = name_group

    def _pre_check(self):
        assert(isinstance(self.universes, list))
        assert(isinstance(self.groupBoundaries, list))
        assert(isinstance(self.nameStructure, str))

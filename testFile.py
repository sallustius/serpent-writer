""" The code generates the inputs for the fission matrix calculations"""

from objectZoo import Pin, Assm, Cell, Geometry, Material, FissionMatrix
from inputWriter import SerpentWriter as sW

# FilePaths
filePath = 'miniCore.i'
libX = '/nv/hp22/dkotlyar6/data/Codes/DATA/sss_endfb7u.xsdata'
# Pin
radiiP = [0.410, 0.475, 1.26]
nPins = 17
# Assembly
pitchA = nPins*radiiP[-1]
pin_map = [['ff'] * nPins] * nPins
# SuperCell
assm_map = [['a1', 'a2']]

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %                 MATERIALS                          %
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
materials = []
# FUEL
composition = [['92235.09c', 1.0], ['92238.09c', 1.0], ['92239.09c', 1.0]]
fuel = Material('fuel', -10.9, 900, composition, 'mass')
materials.append(fuel)
# WATER
composition = [['1001.06c', 0.6666667], ['8016.06c', 0.3333333]]
water = Material('water', -0.700452, 600, composition, 'molar', 'lwj3.11t ')
materials.append(water)
# Clad
composition = [['40000.06c', 1.0]]
clad = Material('clad', -6.5, 600, composition, 'molar')
materials.append(clad)

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %                 GEOMETRY                           %
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

pin1 = Pin('ff', radiiP, [fuel.name, water.name, clad.name])
a1 = Assm('a1', pin_map, radiiP[-1])
a2 = Assm('a2', pin_map, radiiP[-1])
superCell = Cell('Super', assm_map, pitchA, ['reflective', 'vacuum'])
geometry = Geometry('miniCore', [pin1], [a1, a2], superCell)

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %                 SETTINGS                           %
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
settings = {'pop': 100000,
            'active cycles': 100,
            'inactive cycles': 50,
            'k guess': 1.0,
            'ures': '92238.09c',
            'lib': libX
            }
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %                 DETECTORS                          %
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
fm = FissionMatrix('cartesian',
                   [-pitchA, pitchA, nPins*2, -pitchA/2, pitchA/2, nPins,
                    -1e37, 1e37, 1])

# EXECUTE
serpentInp = sW(filePath, geometry, materials, settings, fm)
serpentInp.write()

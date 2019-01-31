""" The code generates the inputs for the fission matrix calculations"""

# import matplotlib.pyplot as plt
# import detectorWriter as detW
# import fissionMatrixReader as fM

import basisObjects as bO
import geometryWriter as gW

# Create a supercell with two assemblies of the same type
pin1 = bO.PinCell('1', (1, 2, 3), ('m1', 'm2', 'm3'))
assm1 = bO.AssmCell('assm1',
                    (('1', '1', '1'), ('1', '1', '1'), ('1', '1', '1')), 1.3)
assm3 = bO.AssmCell('assm3',
                    (('1', '1', '1'), ('1', '1', '1'), ('1', '1', '1')), 1.3)
superCell = bO.SuperCell('sc', (('assm1', 'assm3'), ('assm3', 'assm1')),
                         12.34, 'reflective')

pins = (pin1,)
assemblies = (assm1, assm3)
geometry = bO.GeometryStructure('firstTrial', pins, assemblies, superCell)

print(assm1.map)
print('-------------------')
print(geometry.pins[0].name)
print(geometry.assemblies[1].name)
print(geometry.bc)

f = gW.GeometryWriter('MiniCore.i', geometry)
print(f.fp)
f.write()
#  Constants
# nameFile = 'miniCore'
# pitch = 21.42
# numElements = 17
# # Limits of domain
# # x-coordinate
# x_max = pitch * (numElements * .5)
# x_min = -x_max
# x_num = numElements
# # y-coordinate
# y_max = x_max
# y_min = -y_max
# y_num = x_num
# # z-coordinate
# z_min = -1e37
# z_max = 1e37
# z_num = 1
#
# # Fission Matrix Detector Attached to nameFile
# LL = (x_min, x_max, x_num, y_min, y_max, y_num, z_min, z_max, z_num)
# fissionMatrixDef = detW.FissionMatrixWriter(nameFile, 'cartesian', LL)
# fissionMatrixDef.write()
#
# # Read fission matrix
# fissionRead = fM.FissionMatrixReader('FilesMATLAB/miniCore_fmtx0.m')
# fissionRead.read()
# A = fissionRead.fMat
# k, e = np.linalg.eig(A)
#
# plt.figure(1)
# plt.plot(k)
#
# plt.figure(2)
# dom = e[:, 0]/sum(e[:, 0])
# dom1 = [float(xx) for xx in dom]
# plt.plot(dom1)
#
# dom1 = np.reshape(dom1, [5, 5])
# plt.figure(3)
# plt.imshow(dom1)
#
# plt.show()

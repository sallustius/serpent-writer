""" The code generates the inputs for the fission matrix calculations"""

import numpy as np
import matplotlib.pyplot as plt
import detector as det
import fissionMatrixReader as fM

#  Constants
nameFile = 'miniCore'
pitch = 21.42
numElements = 17
# Limits of domain
# x-coordinate
x_max = pitch * (numElements * .5)
x_min = -x_max
x_num = numElements
# y-coordinate
y_max = x_max
y_min = -y_max
y_num = x_num
# z-coordinate
z_min = -1e37
z_max = 1e37
z_num = 1

# Fission Matrix Detector Attached to nameFile
LL = (x_min, x_max, x_num, y_min, y_max, y_num, z_min, z_max, z_num)
fissionMatrixDef = det.FissionMatrixWriter(nameFile, 'cartesian', LL)
fissionMatrixDef.write()

# Read fission matrix
fissionRead = fM.FissionMatrixReader('miniCore_fmtx0.m')
fissionRead.read()
A = fissionRead.fMat
k, e = np.linalg.eig(A)

plt.figure(1)
plt.plot(k)

plt.figure(2)
dom = e[:, 0]/sum(e[:, 0])
dom1 = [float(xx) for xx in dom]
plt.plot(dom1)

dom1 = np.reshape(dom1, [5, 5])
plt.figure(3)
plt.imshow(dom1)

plt.show()

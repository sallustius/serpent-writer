""" The code writes the geometry input for Serpent"""

import numpy as np


class PinCellWrite:
    """
    The class translates the PinCell object in Serpent input-file
    """

    def __init__(self, filePath, pinX):
        self.filePath = filePath
        self.pinX = pinX

    def _writePin(self, fp):
        fp.write('pin %s \n' % self.pinX.name)
        for ii in range(0, np.size(self.pinX.dimensions) - 1):
            fp.write('%s   %.4f \n' % (self.pinX.materials[ii],
                                     self.pinX.dimensions[ii]))
        fp.write('%s  \n' % (self.pinX.materials[-1]))

    def _writeCell(self, fp):
        fp.write('\nsurf 1 sqc 0.0 0.0 %s \n' % self.pinX.dimensions[-1])
        fp.write('cell 1  0 fill %s -1 \n' % self.pinX.name)
        fp.write('cell 99 0 outside 1 \n')

    def write(self):
        fp = open(self.filePath, 'w')
        self._writePin(fp)
        self._writeCell(fp)
        fp.close()


class PinCell:
    """
    Class building pin geometry

    Parameters:
        - name
        - radii's vector
        - matList: list of material associated to anular sectors
    """

    def __init__(self, name, dimensions, materials):
        self.name = name
        self.dimensions = dimensions
        self.materials = materials


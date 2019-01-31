""" The code writes the geometry input for Serpent"""
import numpy as np


class GeometryWriter:
    """
    Class to write geometry section in Serpent input file

    Parameters
    ----------
    file_path: string
        File path
    geometry: Geometry object
        radii vector

    """
    def __init__(self, file_path, geometry):
        self.title = geometry.name
        self.fp = file_path
        self.pins = geometry.pins
        self.assm = geometry.assemblies
        self.cell = geometry.cell
        self.bc = geometry.bc

    def write(self):
        fp = open(self.fp, 'w')
        fp.write('set title "%s"\n\n' % self.title)
        self._write_pins(fp)
        self._write_assms(fp)
        self._write_cell(fp)
        self._write_box(fp)
        fp.close()

    def _write_pins(self, fp):
        fp.write('%--- PINS DEFINITIONS\n')
        for jj in range(0, len(self.pins)):
            fp.write('pin %s \n' % self.pins[jj].name)
            for ii in range(0, np.size(self.pins[jj].radii) - 1):
                fp.write('%s   %.4f \n' % (self.pins[jj].materials[ii],
                                           self.pins[jj].radii[ii]))
            fp.write('%s  \n\n' % (self.pins[jj].materials[-1]))

    def _write_assms(self, fp):
        fp.write('%--- ASSEMBLIES DEFINITIONS\n')
        for ii in range(0, len(self.assm)):
            fp.write('lat %s 1 0.0 0.0 %d %d %.2f\n'
                     % (self.assm[ii].name, len(self.assm[ii].map),
                        len(self.assm[ii].map), self.assm[ii].pitch))
            for jj in range(0, 3):
                for kk in range(0, 3):
                    fp.write('%s ' % self.assm[ii].map[jj][kk])
                fp.write('\n')
            fp.write('\n')

    def _write_cell(self, fp):
        fp.write('%--- SUPER-CELL DEFINITION\n')
        fp.write('lat %s 1 0.0 0.0 %d %d %.2f\n'
                 % (self.cell.name, 2,
                    2, self.cell.pitch))
        for jj in range(0, 2):
            for kk in range(0, 2):
                fp.write('%s ' % self.cell.map[jj][kk])
            fp.write('\n')
        fp.write('\n')

    def _write_box(self, fp):
        fp.write('surf 5 cuboid %.2f %.2f %.2f %.2f %.2f %.2f \n'
                 % (-160.65, 160.65, -160.65, 160.65, -10.71, 10.71))
        fp.write('cell 98  0 fill %s   -5\n' % self.cell.name)
        fp.write('cell 99  0 outside   5\n')
        fp.write('set bc 1 1 2\n')

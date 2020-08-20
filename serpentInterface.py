""" Interface to create Serpent input file"""
import numpy as np

MAX_NUM = 1e+37


class SerpentWriter:
    """
    SerpentWriter creates the input file

    Parameters
    ----------
    file_path: str
        filePath
    geometry: object
        geometry object
    materials: list
        contains materials objects
    settings: dict
        contains settings for k-eff calculations
    detectors: object
        contains detectors
    fission_matrix: object
        contains fission matrix specifications
    x_sec_generation: object
        contains

    Attributes
    ----------



    """
    def __init__(self, file_path, title, geometry, materials, settings,
                 detectors=None, x_sec_generation=None, fission_matrix=None):
        self.fp = file_path
        self.geometry = geometry
        self.materials = materials
        self.settings = settings
        self.detectors = detectors
        self.xs = x_sec_generation
        self.fm = fission_matrix
        self.title = title

    def write(self):
        file = open(self.fp, 'w')
        file.write('set title "%s"\n\n' % self.title)
        # Create object instances
        m = MaterialsWriter(file, self.materials)
        g = GeometryWriter(file, self.geometry)
        s = SettingsWriter(file, self.settings)
        # Write on input file
        m.mat_write()
        g.geo_write()
        s.set_write()
        if self.detectors:
            d = DetectorWriter(file, self.detectors)
            d.det_write()
        if self.xs:
            x = XSecWriter(file, self.xs)
            x.xs_write()
        if self.fm:
            f = FMWriter(file, self.fm)
            f.fm_write()
        # Close file
        file.close()


class GeometryWriter:

    def __init__(self, file_path, geometry):
        self.fp = file_path
        self.g = geometry

    def geo_write(self):
        self.fp.write('% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n')
        self.fp.write('%\t\t GEOMETRY\n')
        self.fp.write('% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n\n')
        if self.g.pins:
            self._write_pins(self.fp)
        if self.g.group:
            self._write_assms(self.fp)
        if self.g.root:
            self._write_root(self.fp)

    def _write_pins(self, fp):
        fp.write('%--- Pins\n')
        for jj in range(0, len(self.g.pins)):
            fp.write('pin %s \n' % self.g.pins[jj].name)
            for ii in range(0, np.size(self.g.pins[jj].radii) - 1):
                fp.write('%s   %.4f \n' % (self.g.pins[jj].materials[ii],
                                           self.g.pins[jj].radii[ii]))
            fp.write('%s  \n\n' % self.g.pins[jj].materials[-1])

        if self.g.group is None:
            fp.write('\nsurf s1 sqc 0.0 0.0 %.2f\n'
                     % (self.g.pins[0].radii[-1]))
            fp.write('cell 98  0 fill %s   -s1\n' % self.g.pins[0].name)
            fp.write('cell 99  0 outside   s1\n')
            fp.write('set bc 2\n')
            fp.write('\n')

    def _write_assms(self, fp):
        fp.write('%--- Assemblies\n')
        for ii in range(0, len(self.g.group)):
            if self.g.group[ii].typeLattice == 'square':
                fp.write('lat %s 1 0.0 0.0 %d %d %.3f\n'
                         % (self.g.group[ii].name, len(self.g.group[ii].map),
                            len(self.g.group[ii].map), self.g.group[ii].pitch))
                for jj in range(0, np.size(self.g.group[ii].map, 0)):
                    for kk in range(0, np.size(self.g.group[ii].map, 1)):
                        fp.write('%s ' % self.g.group[ii].map[jj][kk])
                    fp.write('\n')
                fp.write('\n')
            elif self.g.group[ii].typeLattice == 'stack':
                fp.write('lat %s 9 0.0 0.0 %d\n'
                         % (self.g.group[ii].name, len(self.g.group[ii].map)))
                print(self.g.group[ii].map)
                print(len(self.g.group[ii].map))

                for jj in range(0, len(self.g.group[ii].map)):
                    fp.write('%.3f %s\n' % (self.g.group[ii].pitch[jj], self.g.group[ii].map[jj]))
                fp.write('\n')
            else:
                TypeError('Error in group-type. Existing types:'
                          ' square, and stack')

    def _write_bc(self, fp):
        if self.g.root.bc[0] == 'reflective':
            if self.g.root.bc[1] == 'reflective':
                fp.write('set bc 2\n')
            elif self.g.root.bc[1] == 'vacuum':
                fp.write('set bc 2 2 1\n')
        elif self.g.root.bc[0] == 'vacuum':
            if self.g.root.bc[1] == 'reflective':
                fp.write('set bc 1 1 2\n')
            elif self.g.root.bc[1] == 'vacuum':
                fp.write('set bc 1 1 1\n')
        else:
            ValueError('bc can be either reflective or vacuum')
        fp.write('\n')

    def _write_root(self, fp):
        fp.write('%--- Root universe\n')
        fp.write('surf 1000 cuboid -%.3f %.3f -%.3f %.3f '
                 '0.000 %.2f\n' %(self.g.root.dimensions[0]/2,
                                  self.g.root.dimensions[0]/2,
                                  self.g.root.dimensions[1]/2,
                                  self.g.root.dimensions[1]/2,
                                  self.g.root.dimensions[2]))
        fp.write('cell 110  0  fill %s    -1000\n' % self.g.root.name)
        fp.write('cell 112  0  outside     1000\n')
        # Write boundary conditions
        self._write_bc(fp)


class MaterialsWriter:
    def __init__(self, file_path, materials):
        self.lista = materials
        self.fp = file_path

    def mat_write(self):
        """ Iterates over materials in the list"""
        self.fp.write('% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n')
        self.fp.write('%\t\t MATERIALS\n')
        self.fp.write('% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n\n')
        for ii in range(0, len(self.lista)):
            if self.lista[ii].moder and self.lista[ii].density is not 'sum':
                self.fp.write('therm %s %s\n' % (self.lista[ii].moderName, self.lista[ii].moder))
                self.fp.write('mat %s -%.3f moder %s 1001\n'
                              % (self.lista[ii].name, float(self.lista[ii].density), self.lista[ii].moderName) )
            elif self.lista[ii].moder is None \
                    and self.lista[ii].density is 'sum':
                self.fp.write('mat %s sum\n' % self.lista[ii].name)
            elif self.lista[ii].moder \
                    and self.lista[ii].density is 'sum':
                self.fp.write('therm %s %s\n' % (self.lista[ii].moderName, self.lista[ii].moder))
                self.fp.write('mat %s sum moder %s 1001\n'
                              % (self.lista[ii].name, self.lista[ii].moderName))
            else:
                self.fp.write('mat %s -%s\n' %
                              (self.lista[ii].name, self.lista[ii].density))

            lunghezza = np.size(self.lista[ii].composition, 0)
            if self.lista[ii].param == 'mass':
                for jj in range(0, lunghezza):
                    self.fp.write('%s -%s\n' %
                                  (self.lista[ii].composition[jj][0],
                                   self.lista[ii].composition[jj][1]))
            elif self.lista[ii].param == 'molar':
                for jj in range(0, lunghezza):
                    self.fp.write('%s %s\n' %
                                  (self.lista[ii].composition[jj][0],
                                   self.lista[ii].composition[jj][1]))

            self.fp.write('\n')

class SettingsWriter:
    def __init__(self, file_path, settings):
        self.set = settings
        self.fp = file_path

    def set_write(self):
        self.fp.write('% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n')
        self.fp.write('%\t\t SETTINGS\n')
        self.fp.write('% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n\n')
        self.fp.write('set pop %s %s %s %s \n' %
                      (self.set['pop'], self.set['active cycles'],
                       self.set['inactive cycles'], self.set['k guess']))
        self.fp.write('% -- Cross-sections\n')
        self.fp.write('set acelib "%s"\n' % self.set['lib'])
        if self.set['ures'] != 0:
            self.fp.write('set ures 1 3 %s \n' % self.set['ures'])


class XSecWriter:
    def __init__(self, file_path, xs_data):
        self.fp = file_path
        self.xs = xs_data

    def xs_write(self):
        self.fp.write('\n% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n')
        self.fp.write('%\t\t CROSS-SECTIONS\n')
        self.fp.write('% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n\n')
        self.fp.write('set nfg %s\n' % self.xs.nameStructure)
        if self.xs.groupBoundaries:
            string = ' '
            string = string.join(map(str, self.xs.groupBoundaries))
            self.fp.write('ene %s 1 %s\n' % (self.xs.nameStructure, string))
        if self.xs.universes:
            string = '\n'
            string = string.join(map(str, self.xs.universes))
            self.fp.write('set gcu %s \n\n' % string)


class FMWriter:
    def __init__(self, file_path, fission_matrix):
        self.fp = file_path
        self.fm = fission_matrix

    def _pre_check(self):
        if self.fm.typeFM == 'cartesian':
            flag = 4
        else:
            flag = 0
        return flag

    def _fission_matrix_cart(self, flag):
        string = 'set fmtx %d %.2f %.2f %d ' \
                 '%.2f %.2f %d %.2e %.2e %d\n' \
                 % (flag,
                    self.fm.dimensions[0], self.fm.dimensions[1],
                    self.fm.numberOfCells[0], self.fm.dimensions[2],
                    self.fm.dimensions[3], self.fm.numberOfCells[1],
                    self.fm.dimensions[4], self.fm.dimensions[5],
                    self.fm.numberOfCells[2],)
        return string

    def fm_write(self):
        flag = self._pre_check()
        if flag == 0:
            raise ValueError('Only supported FM-type is "cartesian"')
        print('Appending fission matrix definition')
        self.fp.write('% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n')
        self.fp.write('%\t\t FISSION MATRIX\n')
        self.fp.write('% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n\n')
        self.fp.write(self._fission_matrix_cart(flag))
        print('Completed')


class DetectorWriter:
    def __init__(self, file_path, detector):
        self.fp = file_path
        self.det = detector

    def _detector_cart(self):
        string = 'det %s dr -8 void dx %.2f %.2f %.0f ' \
                 'dy %.2f %.2f %.0f dz %.2f %.2f %.0f\n' \
                 % (self.det.name,
                    self.det.dimensions[0], self.det.dimensions[1],
                    self.det.numberOfCells[0], self.det.dimensions[2],
                    self.det.dimensions[3], self.det.numberOfCells[1],
                    self.det.dimensions[4], self.det.dimensions[5],
                    self.det.numberOfCells[2])
        return string

    def det_write(self):
        self.fp.write('% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n')
        self.fp.write('%\t\t DETECTORS\n')
        self.fp.write('% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n\n')
        self.fp.write(self._detector_cart())

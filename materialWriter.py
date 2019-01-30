import numpy as np


class Material:
    """
    Materials class
    """

    def __init__(self, name, density, temperature, composition, moder=0):
        self.name = name
        self.density = density
        self.temperature = temperature
        self.composition = composition
        self.moder = moder


class MatObjWriter:
    """
    Writes the material section in a Serpent input file
    """

    def __init__(self, materialLista, filePath):
        self.lista = materialLista
        self.filePath = filePath

    def write(self):
        """ Iterates over materials in the dictionary"""
        fp = open(self.filePath, 'w')
        for ii in range(0, len(self.lista)):
            if self.lista[ii].moder == 0:
                fp.write('\n\nmat %s %s' % (
                self.lista[ii].name, self.lista[ii].density))
            else:
                fp.write('\n\nmat %s %s moder lwtr 1001' % (
                self.lista[ii].name, self.lista[ii].density))
            lunghezza = np.size(self.lista[ii].composition, 0)
            for jj in range(0, lunghezza):
                fp.write('\n%s %s' % (self.lista[ii].composition[jj][0],
                                      self.lista[ii].composition[jj][1]))
        fp.close()

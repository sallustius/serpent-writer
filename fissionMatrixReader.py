""" Fission Matrix Reader"""

from numpy import zeros
import re
from utils import dim_check, str2vec


# Regular Expressions
fMVal = r'fmtx_t\s+\(\s*(\d+),\s*(\d+)\)\s+=\s+([\d\+\.E-]+)\s;\s ' \
        r'fmtx_t_err\s+\(\s*(\d+),\s*(\d+)\)\s+=\s+([\d\+\.E-]+)'
dimsEx = r'fmtx_t\s+=\s+zeros\((\d+),(\d+)\)'


class FissionMatrixReader:
    """
    Class responsible for reading fission matrix output
    """
    def __init__(self, file_path):
        self.fp = file_path
        self.fMat = None
        self.fMatU = None
        self.domEigVal = None
        self.domEigVec = None
        self.domRatio = None
        self.eigValVec = None
        self.eigVecMat = None

    def _pre_check(self):
        with open(self.fp) as check:
            for line in check:
                if line[:4] == 'fmtx' in line:
                    return
        raise Warning('Unable to find fission matrix data '
                      'in {}'.format(self.fp))

    def _meta_find(self, reg_ex):
        with open(self.fp) as fp:
            for lineNo, line in enumerate(fp):
                meta_string = re.match(reg_ex, line)
                if meta_string is not None:
                    meta_list = str2vec(meta_string.groups())
                    return meta_list, fp

    def _fission_matrix_read(self, dims):
        """
        Populates dense fission matrix
        """
        fp = open(self.fp)
        self.fMat = zeros((int(dims[0]), int(dims[1])))
        self.fMatU = zeros((int(dims[0]), int(dims[1])))
        for lineNo, line in enumerate(fp):
            m = re.match(fMVal, line)
            if m is not None:
                lista = str2vec(m.groups())
                self.fMat[int(lista[0]) - 1, int(lista[1]) - 1] = lista[2]
                self.fMatU[int(lista[0]) - 1, int(lista[1]) - 1] = lista[5]
        fp.close()
        return self.fMat, self.fMatU

    def read(self):
        """
        Reads the fission matrix output file.
        """
        dims, fp = self._meta_find(dimsEx)
        dim_check(dims)
        self._fission_matrix_read(dims)

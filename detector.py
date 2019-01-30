""" Writer for detector cards"""

MAX_NUM = 1e37


class FissionMatrixWriter:
    """
    The class appends fission matrix specifications for Serpent files
    """

    def __init__(self, file_path, type_fm='cartesian',
                 limits=(0, 1, 10, 0, 1, 10, 0, 1, 10)):
        self.filePath = file_path
        self.typeFM = type_fm
        self.Limits = limits

    def _pre_check(self):
        if self.typeFM == 'cartesian':
            flag = 4
        else:
            flag = 0
        return flag

    def _fission_matrix_cart(self, flag):
        string = 'set fmtx %d %.2f %.2f %d ' \
                 '%.2f %.2f %d %.2e %.2e %d\n' \
                 % (flag,
                    self.Limits[0], self.Limits[1], self.Limits[2],
                    self.Limits[3], self.Limits[4], self.Limits[5],
                    self.Limits[6], self.Limits[7], self.Limits[8],)
        return string

    def write(self):
        flag = self._pre_check()
        if flag == 0:
            raise ValueError('Only supported FM-type is "cartesian"')
        fp = open(self.filePath + '_DET', 'a')
        print('Appending line to the file %s', self.filePath)
        string = self._fission_matrix_cart(flag)
        fp.write(string)
        print('Completed')
        fp.close()

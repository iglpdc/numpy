
from numpy.testing import *
set_package_path()
import numpy.core.umath as ncu
from numpy import array
import numpy as N
restore_path()

types = [N.bool_, N.byte, N.ubyte, N.short, N.ushort, N.intc, N.uintc,
         N.int_, N.uint, N.longlong, N.ulonglong,
         N.single, N.double, N.longdouble, N.csingle,
         N.cdouble, N.clongdouble]

# These were generated using old umath
typeconv = array([
    [ 0,  1,  2,  3,  4,  5,  6,  5,  6,  9, 10, 11, 12, 13, 14, 15, 16],
    [ 1,  1,  3,  3,  4,  5,  6,  5,  6,  9, 10, 11, 12, 13, 14, 15, 16],
    [ 2,  3,  2,  3,  4,  5,  6,  5,  6,  9, 10, 11, 12, 13, 14, 15, 16],
    [ 3,  3,  3,  3,  5,  5,  6,  5,  6,  9, 10, 11, 12, 13, 14, 15, 16],
    [ 4,  4,  4,  5,  4,  5,  6,  5,  6,  9, 10, 11, 12, 13, 14, 15, 16],
    [ 5,  5,  5,  5,  5,  5,  9,  5,  9,  9, 10, 12, 12, 13, 15, 15, 16],
    [ 6,  6,  6,  6,  6,  9,  6,  9,  6,  9, 10, 12, 12, 13, 15, 15, 16],
    [ 7,  7,  7,  7,  7,  7,  9,  7,  9,  9, 10, 12, 12, 13, 15, 15, 16],
    [ 8,  8,  8,  8,  8,  9,  8,  9,  8,  9, 10, 12, 12, 13, 15, 15, 16],
    [ 9,  9,  9,  9,  9,  9,  9,  9,  9,  9, 12, 12, 12, 13, 15, 15, 16],
    [10, 10, 10, 10, 10, 10, 10, 10, 10, 12, 10, 12, 12, 13, 15, 15, 16],
    [11, 11, 11, 11, 11, 12, 12, 12, 12, 12, 12, 11, 12, 13, 14, 15, 16],
    [12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 13, 15, 15, 16],
    [13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 16, 16, 16],
    [14, 14, 14, 14, 14, 15, 15, 15, 15, 15, 15, 14, 15, 16, 14, 15, 16],
    [15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 16, 15, 15, 16],
    [16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16]
    ])

typeconv2 = array([
    ['?','b','B','h','H','i','I','i','I','q','Q','f','d','g','F','D','G'],
    ['b','b','h','h','H','i','I','i','I','q','Q','f','d','g','F','D','G'],
    ['B','h','B','h','H','i','I','i','I','q','Q','f','d','g','F','D','G'],
    ['h','h','h','h','i','i','I','i','I','q','Q','f','d','g','F','D','G'],
    ['H','H','H','i','H','i','I','i','I','q','Q','f','d','g','F','D','G'],
    ['i','i','i','i','i','i','q','i','q','q','Q','d','d','g','D','D','G'],
    ['I','I','I','I','I','q','I','q','I','q','Q','d','d','g','D','D','G'],
    ['l','l','l','l','l','l','q','l','q','q','Q','d','d','g','D','D','G'],
    ['L','L','L','L','L','q','L','q','L','q','Q','d','d','g','D','D','G'],
    ['q','q','q','q','q','q','q','q','q','q','d','d','d','g','D','D','G'],
    ['Q','Q','Q','Q','Q','Q','Q','Q','Q','d','Q','d','d','g','D','D','G'],
    ['f','f','f','f','f','d','d','d','d','d','d','f','d','g','F','D','G'],
    ['d','d','d','d','d','d','d','d','d','d','d','d','d','g','D','D','G'],
    ['g','g','g','g','g','g','g','g','g','g','g','g','g','g','G','G','G'],
    ['F','F','F','F','F','D','D','D','D','D','D','F','D','G','F','D','G'],
    ['D','D','D','D','D','D','D','D','D','D','D','D','D','G','D','D','G'],
    ['G','G','G','G','G','G','G','G','G','G','G','G','G','G','G','G','G']
    ],'S1')

class test_types(ScipyTestCase):
    def check_types(self, level=1):
        # list of types
        for k, atype in enumerate(types):
            vala = atype(3)
            for l, btype in enumerate(types):
                valb = btype(1)
                val = vala+valb
                assert val.dtype.num == typeconv[k,l] and \
                       val.dtype.char == typeconv2[k,l], \
                       "error with (%d,%d)" % (k,l)

if __name__ == "__main__":
    NumpyTest().run()

## \file operator_1d.py

## The 1D operator class contains the basic info for constructing
#  a 1-dimensional linear operator such as a spatial derivative using
#  a stencil for a finite difference scheme.

import stencil

## The Operator1D class
class Operator1D():

    ## 1D Operator constructor
    #  \param s_list A list of stencil index points
    #  \param deg The degree of the desired derivative
    def __init__(self, s_list, deg):
        self.stncl = stencil.Stencil(s_list)
        self.deg = deg
        self.accuracy = self.stncl.N - self.deg
        assert self.accuracy > 0, '''Improper 1D operator formation: 
                                  increase number of stencil points!'''
        self.weights = self.stncl.get_weights(deg)

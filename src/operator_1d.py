## \file operator_1d.py

## The 1D operator class contains the basic info for constructing
#  a 1-dimensional linear operator such as a spatial derivative using
#  a stencil for a finite difference scheme.

from src import stencil

## The Operator1D class
class Operator1D():

    ## 1D Operator constructor
    #  \param s_list A list of stencil index points
    #  \param deg The degree of the desired derivative
    def __init__(self, s_list, deg):
        
        ## \var stncl A stencil object
        self.stncl = stencil.Stencil(s_list)

        ## \var deg The derivative degree
        self.deg = deg

        ## \var accuracy Accuracy of the approximation, which is
        #  equal to the number of stencil points minus the
        #  derivative degree
        self.accuracy = self.stncl.N - self.deg
        assert self.accuracy > 0, \
        'Improper 1D operator formation: increase number of stencil points!'

        ## \var weights The appropriate weighting coefficients for
        #  the finite difference approximation
        self.weights = self.stncl.get_weights(deg)

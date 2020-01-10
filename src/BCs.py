## @file 
# file containing the abstract base class for representing the PDE problem's boundary conditions.
#
# Uses the 'abc' module to utilize pythonic abstract base classes
# Uses numpy for internal handling of arrays

import abc
import numpy

## Abstract base class for representing the PDE problem's boundary conditions.
class BCs(abc.ABC):
    
    ## The constructor 
    def __init__(self):
        pass
    
    ## Method to spit out the contained boundary conditions, for debugging and planning.
    def print_BCs(self):
        pass
    
## Child BCs class for handling one side with static Dirichlet boundary conditions.
class Dirichlet(BCs):
    
    ## The constructor
    # @param side Int- the value of the side whose BCs are being represented
    # @param vals Numpy array- the static values set
    def __init__(self,side,vals):
        self.side = side
        self.vals = vals
        
    def print_BCs(self):
        print("This boundary value object represents side {} and has Dirichlet"
              " boundary conditions.\n".format(self.side))
        print("Set boundary values:{}\n".format(self.vals))
## @file BCs.py
# file containing the abstract base class for representing the PDE problem's boundary conditions.
#
# Uses the 'abc' module to utilize pythonic abstract base classes
# Uses numpy for internal handling of arrays

import abc

## Abstract base class for representing the PDE problem's boundary conditions.
class BCs(abc.ABC):
    
    ## The constructor 
    def __init__(self):
        pass
    
    ## Method to spit out the contained boundary conditions, for debugging and planning.
    def print_BCs(self):
        pass
   
    ## Method to return the boundary this boundary applies to
    def get_bd(self):
        pass
    
    ## Method to return the type of boundary condition the object is holding.
    def get_bctype(self):
        pass
    

        
    
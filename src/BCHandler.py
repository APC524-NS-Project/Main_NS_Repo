## @file BCHandler.py
#
# file containing the abstract base class for applying the PDE problem's boundary conditions.
#
# Uses the 'abc' module to utilize pythonic abstract base classes

import abc

## Abstract base class for implementing the PDE problem's boundary conditions.
class BCHandler(abc.ABC):
    
    ## The constructor 
    def __init__(self):
        pass
    
    ## Method to implement the contained boundary conditions
    def set_BCs(self):
        pass
    
    ## Method to check if the correct type of boundary conditions have been passed to the handler
    def check_BCtype(self):
        pass
   

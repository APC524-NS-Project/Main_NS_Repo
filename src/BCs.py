## @file 
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
    
## Child BCs class for handling one side with static boundary conditions.
class StaticBCs(BCs):
    bctype = "None"
    ## The constructor
    # @param dimen Int- starting at 0, indicating which dimension the boundary conditions are being applied to.
    # @param side Char- 'l' or 'r', the side whose BCs are being represented
    # @param vals Numpy array- the static values set
    def __init__(self,dimen,side,vals):
        self.dimen = dimen
        self.side = side
        self.bound_vals = vals
        
    ## Method to spit out the contained boundary conditions, for debugging and planning.
    #
    # Mentions the side number, the kind of boundary, and spits out the prescribed values.        
    def print_BCs(self):
        print("This boundary value object represents side {} and has {}"
              " boundary conditions.\n".format(self.side,self.bctype))
        print("Set boundary values:{}\n".format(self.bound_vals))
    
    ## Method to return the side that this boundary condition applies to 
    def get_bd(self):
        return self.dimen, self.side
    
    ## Method to return the boundary condition values, as a numpy array
    def get_bcs(self):
        return self.bound_vals
    
    ## Method to return the type of boundary condition the object is holding.
    def get_bctype(self):
        return self.bctype
    
## Child BCs class for handling one side with static Dirichlet boundary conditions.
class Dirichlet(StaticBCs):
    bctype = "Dirichlet"    
        
## Child BCs class for handling one side with static Neumann boundary conditions.
class Neumann(StaticBCs):
    bctype = "Neumann"     
        
    
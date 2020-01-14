## @file static_bcs.py
# file containing the class(es) for representing static boundary conditions.
#
import src.BCs as bcs

## Child BCs class for handling one side with static boundary conditions.
# @var bctype the kind of boundary condition being specified
class StaticBCs(bcs.BCs):
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
## \file conduct_heat_eqn.py

from src import problem

## The conductive heat equation problem with no advective
#  transport in the form dT/dt = alpha * laplacian(T)
#  where T is temperature and alpha is the thermal diffusivity.
class ConductHeatEqn(Problem):

    ## The constructor
    #  \param alpha The value of the thermal diffusivity.
    #  Default value is 1 m^2/s.
    def __init__(self, alpha=1):
        
        ## \var ops_set_flag False if the operators have not
        #  been defined
        self.ops_set_flag = False

        ## \var ops A tuple containing strings for the names of
        #  each required operator. Just laplacian here.
        self.ops = ('laplacian',)

        ## \var laplacian The laplacian operator
        self.laplacian = None

        ## \var alpha The value of the thermal diffusivity
        self.alpha = alpha

    ## The set_ops function takes a dictionary of linear
    #  operators defined elsewhere and sets them to the
    #  correct member variables in the problem.
    #  \param lin_ops_dict Dictionary of linear operators
    def set_ops(self, lin_ops_dict):
        self.laplacian = lin_ops_dict['laplacian']
        self.ops_set_flag = True
        return

    ## The RHS function applies the defined operators to the
    #  grid argument in a defined manner.
    #  
    #  Here the RHS evaluates alpha * laplacian(val_grid)
    #  \param val_grid The spatial grid of current values
    #  \return The grid containing the evaluated RHS values
    def RHS(self, val_grid):
        assert self.ops_set_flag, '''The RHS operators must 
                                  be defined before calling
                                  RHS()!'''
        return self.alpha * self.laplacian(val_grid)

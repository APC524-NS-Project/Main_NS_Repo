## \file time_stepper.py

## \package time_stepper
#  These objects drive the solution to the temporal part of the
#  PDE problem. This consists of advancing the current time of
#  the problem by one step. This can be implemented in many ways,
#  the simplest of which is a Forward Euler method.
#  
#  The time stepper is called along with a grid by the main
#  driver class and should return another grid with values that
#  have been updated in time. This grid will then be passed back
#  to the spatial driver for further modification. The main
#  method of the time stepper class is simply called step().


## The abstract TimeStepper class
class TimeStepper():

    ## The main step method of the time stepper.
    #  
    #  This method must be overwritten in the child class where
    #  the actual implementation algorithm is defined.
    #  \param val_grid The spatial grid of values at the current time
    #  \param rhs_grid The spatial grid of RHS values
    #  \param dt The time step size
    #  \return Spatial grid with new values for the next time step
    def step(self, val_grid, rhs_grid, dt):
        pass


## A concrete Forward Euler subclass of TimeStepper
#  
#  The Forward Euler method uses a simple forward finite difference
#  approach to estimate a value at the next time step. This is done
#  with the approximation {u(t+dt) - u(t)}/dt = RHS which can be
#  rearranged to give u(t+dt) = u(t) + dt*RHS.
class ForwardEuler(TimeStepper):

    ## The step method of the Forward Euler class
    #  
    #  Implements the basic Forward Euler algorithm on the input
    #  grid object.
    #  \param val_grid The spatial grid of values at the current time
    #  \param rhs_grid The spatial grid of RHS values
    #  \param dt The time step size
    #  \return Spatial grid with new values for the next time step
    def step(self, val_grid, rhs_grid, dt):
        assert ( self.get_num_grid_elems(val_grid) == 
                 self.get_num_grid_elems(rhs_grid),
                 "Grid objects must be equally sized!" )
        
        new_val_grid = val_grid + dt * rhs_grid
        return new_val_grid

    ## A method for determining the number of elements in a grid
    #  
    #  This is just the product of the spatial dimensions of the
    #  grid.
    #  \param grid_obj The grid to be querried
    #  \return The number of elements in the grid
    def get_num_grid_elems(self, grid_obj):
        grid_phys_dim = grid_obj.get_phys_dim()
        num_grid_elems = 1
        for item in grid_phys_dim:
            num_grid_elems *= item
        return num_grid_elems

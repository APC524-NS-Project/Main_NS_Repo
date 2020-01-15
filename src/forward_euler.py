## \file forward_euler.py

from src import time_stepper

## A concrete Forward Euler subclass of TimeStepper
#  
#  The Forward Euler method uses a simple forward finite difference
#  approach to estimate a value at the next time step. This is done
#  with the approximation {u(t+dt) - u(t)}/dt = RHS which can be
#  rearranged to give u(t+dt) = u(t) + dt*RHS.
class ForwardEuler(time_stepper.TimeStepper):

    ## The step method of the Forward Euler class
    #  
    #  Implements the basic Forward Euler algorithm on the input
    #  grid object.
    #  \param val_grid The spatial grid of values at the current time
    #  \param rhs_grid The spatial grid of RHS values
    #  \param dt The time step size
    #  \return Spatial grid with new values for the next time step
    def step(self, val_grid, rhs_grid, dt):
        assert val_grid.gqshape == rhs_grid.gqshape, \
               "Grid objects must be equally sized!"
        
        new_val_grid = val_grid + dt * rhs_grid
        return new_val_grid


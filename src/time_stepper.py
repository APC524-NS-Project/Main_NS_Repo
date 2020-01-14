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


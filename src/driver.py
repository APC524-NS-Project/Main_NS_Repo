## \file driver.py

## \package driver
#  This is the main driver class for solving the PDE problem.
#  It contains methods to call the main methods of the spatial
#  driver and the time stepper.

## The main Driver class
class Driver():

    ## The constructor for the Driver class
    #  \param space_driver A SpatialDriver instance
    #  \param time_stepper A TimeStepper instance
    def __init__(self, space_driver, time_stepper):
        self.space_driver = space_driver
        self.time_stepper = time_stepper

    ## Advance the full probelm one time step
    #  \param t The current time
    #  \param dt The time step size
    #  \param val_grid A spatial grid object
    #  \return The grid output from the time stepper
    def full_advance(self, t, dt, val_grid):
        val_grid, rhs_grid = self.space_driver.solve(t, val_grid)
        val_grid = self.time_stepper.step(val_grid, rhs_grid, dt)
        return val_grid

    ## Solve the full problem for a pre-defined number of
    #  time steps
    #  \param tstart The initial time value
    #  \param tend The ending time value
    #  \param dt The time step size
    #  \param val_grid A spatial grid object
    def full_solve(self, tstart, tend, dt, val_grid):
        Nsteps = int((tend - tstart)/dt)
        t = start
        for i in range(Nsteps):
            val_grid = self.full_advance(t, dt, val_grid)
            t += dt

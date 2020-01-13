## \file logger.py

## The Logger class
#  
#  Basically a list wrapper. Just appends time and grid values to
#  a list stored in the object. Logger.log_list[index] returns the
#  [t, val_grid] pair at that index.
class Logger():

    ## The constructor initializes an empty list
    def __init__(self):
        self.log_list = []

    ## The log function appends the current timestep
    #  \param t The current time value
    #  \param val_grid The current spatial grid values to be logged
    def log(self, t, val_grid):
        self.log_list.append([t, val_grid])
        return

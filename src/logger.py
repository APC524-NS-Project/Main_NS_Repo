## \file logger.py

import numpy as np

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
    
    ## Function to get the log_list element at a particular frame.
    # \param i Int- the frame that is desired, starting from 0
    # This is basically a wrapper of LoggerObject.log_list[i], in case we ever want to change how the log stores its stuff.
    def get_frame(self,i):
        return self.log_list[i]
    
    ## Function to return the number of frame currently contained in the Logger
    # This is a wrapper of len(LoggerObject.log_list) in case we ever change how the log stores its stuff.
    def get_nframes(self):
        return len(self.log_list)
    
    ## Function to get the min and max values of the data contained in the Logger
    def get_data_limits(self):
        maxdat = -np.inf
        mindat = np.inf
        for item in self.log_list:
            grid = item[1]
            maxdat = max(maxdat,grid.max())
            mindat = min(mindat,grid.min())
            
        return (mindat,maxdat)
        
    

import numpy as np
from abc import ABC, ABCMeta, abstractmethod

## the GridSpec abstract base class
class GridSpec(ABC):
    pass
    
## the CartesianGridSpec class
class CartesianGridSpec(GridSpec):
 
    ## The constructor for the CartesianGridSpec
    # Initialize the CartesianGridSpec with coordination, dimention, and shape of Grid
    # @param coords A tuple of tuples where the dimension of the gridspec and the inner tuples difine the coordinate space
     def __init__(self, coords):
     # A coordination object
     self.coords = coords
     # A dimention object
     self.ndim = len(coords)
     # A Shape object
     self.gridshape = tuple([len(c) for c in self.coords])
            
## The GridQty abstract base class
class GridQty(ABC):
    
    ## The constructor for the GridQty
    # Initialize the GridQty with self.spec(undefined yet),
    # slef.gqshape(contains gridshape defined in CartesianGridSpec & qtyshape that defined & called later),
    # slef.and grid that called makegrid func defined later.
    def __init__(self, spec, initial_vals):
        self.spec = spec
        self.gqshape = self.spec.gridshape + self._qtyshape()
        self.grid = self._makegrid(self.gqshape) #or, initial_vals
     
    ## A non-abstract child must override each abstract method inherited from its parent 
    # by defining a method with the same signature and same return type.
    # Here defines: _qtyshape
    # for the childclass GridScalar and GridVector
    @abstractmethod 
    def _qtyshape(self):
        pass
    
    ## Static method knows nothing about the class and just deals with the parameters.
    # Here defines: _makegrid
    # **kwards: whatever keywords that also want to include in the grid
    # np.array require opject (could be set with initial_vals), or leave it as np.empty that has null grid
    @staticmethod
    def _makegrid(shape, **kwargs):
        return np.empty(shape = shape, **kwargs)  #or, mp.array(initial_vals)   
    
    ## Getattr method: acquire the valus in the grid
    # do not use getattribute
    def __getattr__(self, attr):
        return getattr(self.grid, attr)  #through grid: do attr without shape defined
    
    ## Static method knows nothing about the class and just deals with the parameters.
    # Here defines: _indexify   
    # *splat turns tuples to integrals for range()
    @staticmethod
    def _indexify(indices):
        idxs = [range(*t) for t in indices]
        return np.ix_(idxs)
    
    ## Getslice func.
    # Squeeze cancel all the 1-dim element in the tuple, could be useful in Setslice
    def getslice(self, indices, squeeze = False):
        idxs = self._indexify(indices)
        result = self.grid[idxs]
        if squeeze:
            result = self.squeeze(result)
        return result
    
    ## Setslice func.
    # get the shape of slice, reshape value.np
    def setslice(self, indices, value):
        idxs = self._indexify(indices)
        values_np = np.array(values)
        slice_shape = self.grid[idxs].shape
        self.grid[idxs] = values_np.reshape(slice_shape)
        return 

## the GridScalar childclass
class GridScalar(GridQty):
    def _qtyshape(self):
            return ()
        
## the GridVector childclass          
class GridVector(GridQty):
    def _qtyshape(self):
            return (self.spec.ndim, )  
        

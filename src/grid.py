## @file grid.py
import numpy as np
from abc import ABC, ABCMeta, abstractmethod
from src import operatormatrix

## the GridSpec abstract base class
class GridSpec(ABC):
    pass
    
## the CartesianGridSpec class
class CartesianGridSpec(GridSpec):
 
    ## The constructor for the CartesianGridSpec
    # Initialize the CartesianGridSpec with coordination, dimention, and shape of Grid
    # @param coords A tuple of tuples where the dimension of the gridspec and the inner tuples defines the coordinate space
    # @var ndim The number of dimensions of the gridspec
    # @var gridshape Tuple representing the number of points in each dimension.
    # @var spacing Tuple of the spacings (dx) in each dimension
    # The coordinates MUST BE EVENLY SPACED IN EACH DIMENSION
    def __init__(self, coords):
         # A coordination object
         self.coords = coords #MUST B
         # A dimention object
         self.ndim = len(coords)
         # A Shape object
         self.gridshape = tuple([len(c) for c in self.coords])
         self.spacing = self._getspacing()
         
    def _getspacing(self):
        spacing_list = []
        for coord in self.coords:
            spacing_list.append(coord[1]-coord[0])
            
        spacing=tuple(spacing_list)
        return spacing
            
## The GridQty abstract base class
class GridQty(ABC):
    
    ## The constructor for the GridQty
    # @param spec The GridSpec object with which to initialize the GridQty
    # @var gqshape(contains gridshape defined in CartesianGridSpec & qtyshape that defined & called later),
    # @var grid Numpy array with necessary dimensions, Instantiated by makegrid func defined later.
    def __init__(self, spec, initial_vals):
        self.spec = spec
        self.gqshape = self.spec.gridshape + self._qtyshape()
        self.grid = self._makegrid(self.gqshape, initial_vals) 
     
    ## Abstract method _qtyshape, to return the dimensions of the stored object (versus the GridSpec)
    #A non-abstract child must override each abstract method inherited from its parent 
    # by defining a method with the same signature and same return type.
    @abstractmethod 
    def _qtyshape(self):
        pass
    
    ## Static method _makegrid
    # **kwards: whatever keywords that also want to include in the grid
    # static method that is agnostic to the particular child class calling it.
    @staticmethod
    def _makegrid(shape, initial_vals, **kwargs):
        starting_array = np.array(initial_vals,**kwargs)
        shaped_array=starting_array.reshape(shape)
        return shaped_array  #or, mp.array(initial_vals)   
    
    ## Getattr method: If a method isn't specified for a GridQty object, instead try doing operations on the grid attribute
    # @param attr The attribute of GridQty we are attempting to reference
    def __getattr__(self, attr):     # do not use getattribute
        return getattr(self.grid, attr)  #through grid: do attr without shape defined
    
    
    ## _indexify method for use by getslice and setslice methods  
    # Static method knows nothing about the class and just deals with the parameters.
    @staticmethod
    def _indexify(indices):
        idxs = [range(*t) for t in indices]     # *splat turns tuples to integrals for range()
        return np.ix_(*idxs)
    
    ## Getslice method
    # @param indices idxs A tuple of indices for the slice ((start,noninclusive end),(start,noninclusive end),...)
    # @param squeeze Sets whether to squeeze the array or not
    # squeese cancels all the 1-dim element in the tuple
    def getslice(self, indices, squeeze = False):
        idxs = self._indexify(indices)
        result = self.grid[idxs]
        if squeeze:
            result = self.squeeze(result)
        return result
    
    ## Setslice method
    # @param indices A tuple of indices for the slice ((start,noninclusive end),(start,noninclusive end),...)
    # @param values An iterable containing the values we want to set the specified slice to.
    def setslice(self, indices, values):
        idxs = self._indexify(indices)
        values_np = np.array(values)
        slice_shape = self.grid[idxs].shape
        self.grid[idxs] = values_np.reshape(slice_shape)
        return 

## the GridScalar childclass
class GridScalar(GridQty):
    def _qtyshape(self):
            return ()
    
    ## __add__
    # reformat magic method to add grids together element wise     
    def __add__(self, other):
        if isinstance(other,GridScalar):
            added_np_grid = self.grid.__add__(other.grid)
        else:
            added_np_grid = self.grid.__add__(other)
        
        return GridScalar(self.spec,added_np_grid)

    def __radd__(self, other):
        if other == 0:
            return self
        else:
            return self.__add__(other)

    ## __mul__
    # reformat magic method of multiply to multiply two grids together elementwise
    def __mul__(self,other):
        if isinstance(other,GridScalar):
            muled_np_grid = self.grid.__mul__(other.grid)
        else:
            muled_np_grid = self.grid.__mul__(other)
        
        return GridScalar(self.spec,muled_np_grid)  

    def __rmul__(self, other):
        return self.__mul__(other)

    ## _ravel
    # call np.ravel method on the underlying grid
    def _ravel(self):
        return np.ravel(self.grid)

    ## applyOp
    # apply a linear operator to a grid
    #
    # First ravel the grid into a 1D array. Then have the opmat dot that grid 
    # Finally, reshape the new_grid and use it to instantiate a new grid object to be returned
    # @param opmat An OperatorMatrix object
    # @var new_grid np array of the output of the operator applied to the grid
    def applyOp(self,opmat):
        if isinstance(opmat,operatormatrix.OperatorMatrix):
            flat_grid = self._ravel()
            new_grid = opmat.dot(flat_grid)
            new_grid = np.reshape(new_grid,self.spec.gridshape)
            return GridScalar(self.spec,new_grid)
        else:
            raise TypeError("Attempted to apply a non-operator matrix as an operator")

        
## the GridVector childclass          
class GridVector(GridQty):
    def _qtyshape(self):
            return (self.spec.ndim,)
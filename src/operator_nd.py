## \file operator_nd.py

## The N-dimensional operator class simply contains a tuple of
#  Operator1D objects, as well as the value of N.

## The OperatorND class
class OperatorND():

    ## The N-D operator constructor
    #  \param ops1d Must be a tuple of 1D operators
    def __init__(self, ops1d=()):
        
        assert isinstance(ops1d, tuple), \
        'Constructor argument must be a tuple!'

        assert len(ops1d) > 0, \
        'Argument must contain at least one 1D operator object!'

        ## \var ops1d A tuple of Operator1D objects
        self.ops1d = ops1d

        ## \var dim The number of 1D operators contained in this object
        self.dim = len(self.ops1d)

    def __getitem__(self,key):
        return self.ops1d.__getitem__(key)
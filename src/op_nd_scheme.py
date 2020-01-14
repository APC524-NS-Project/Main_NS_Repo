## \file op_nd_scheme.py

## The N-dimensional operator scheme class contains a tuple of
#  operator objects. The first item in the tuple corresponds
#  to the OperatorND to be used on the "interior" portion of
#  the grid. The second item is a sub-tuple of edge operators. 
#  This argument should take the form:
#  
#  ( z_edge_ops, y_edge_ops, x_edge_ops )
#  
#  The length of the edge operator tuple should be equal to the
#  dim attribute of the interior operator.


## The OperatorNDScheme class
class OperatorNDScheme():

    ## The scheme constructor
    #  \param opND_int An OperatorND object to be applied to the
    #  grid interior
    #  \param edge_op1D A tuple of Operator1D objects to be
    #  applied at the grid edges
    def __init__(self, opND_int, edge_op1D=()):

        assert isinstance(edge_op1D, tuple), \
        'Edge operators must be passed as a tuple! See the documentation!'

        assert opND_int.dim == len(edge_op1D), \
        'Length of edge operator tuple must match dimensionality of interior operator!'

        ## \var scheme The tuple with info about the linear operator
        self.scheme = (opND_int, edge_op1D)

        ## \var interior The interior operator
        self.interior = opND_int

        ## \var edge The tuple of 1D edge operators
        self.edge = edge_op1D

        self.dim = opND_int.dim

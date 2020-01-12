## \file op_nd_scheme.py

## The N-dimensional operator scheme class contains a tuple of
#  OperatorND objects. The first item in the tuple corresponds
#  to the OperatorND to be used on the "interior" portion of
#  the grid. The second item is a sub-tuple of sub-tuples. This
#  argument should take the form:
#  
#  ( (x_opND_L1, x_opND_R1, x_opND_L2, x_opND_R2, etc.),
#    (y_opND_L1, y_opND_R1, y_opND_L2, y_opND_R2, etc.),
#    etc. for as many axes as you need )
#  
#  where L and R correspond to the left and right (or low and
#  high) ends of the axis of interest. The edge operators will
#  be applied from the outside in (x_opND_L1 corresponds to the
#  outermost points at the left end of the x-axis, L2 would be
#  the next step inward, and so on).
#  
#  The length of the edge operator tuple should be equal to the
#  dim attribute of the interior operator.


## The OperatorNDScheme class
class OperatorNDScheme():

    ## The scheme constructor
    #  \param opND_int An OperatorND object to be applied to the
    #  grid interior
    #  \param edge_opND
    def __init__(opND_int, edge_opND=()):

        assert isinstance(edge_opND, tuple), '''Edge operators must
                                             be passed as a tuple!
                                             See the documentation!'''

        assert opND_int.dim == len(edge_opND), '''Length of edge
                                               operator tuple must
                                               match dimensionality
                                               of interior operator!'''

        ## \var scheme The tuple with info about the linear operator
        self.scheme = (opND_int, edge_opND)

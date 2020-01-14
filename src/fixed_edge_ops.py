## \file fixed_edge_ops.py

from src import edge_operator

## The fixed edge operator class handles the operators applied
#  to the edges of the grid which correspond to fixed boundary
#  conditions in the evaluation of the RHS of the PDE.
#  
#  The arguments are tuples of 1D operators. Each tuple corresponds
#  to either the left or right edge of the axis.
class FixedEdgeOps(edge_operator.EdgeOperator):

    ## The constructor
    def __init__(self, left_ops_tup, right_ops_tup):

        ## \var name The type of boundary: 'fixed'
        self.name = None
        self._set_name()

        assert isinstance(left_ops_tup, tuple), \
                'Arguments must be tuples of Operator1D objects!'

        assert isinstance(right_ops_tup, tuple), \
                'Arguments must be tuples of Operator1D objects!'

        assert len(left_ops_tup) > 0, \
                'Left side operator tuple cannot be empty!'

        assert len(right_ops_tup) > 0, \
                'Right side operator tuple cannot be empty!'

        ## \var left The tuple of left edge operators
        self.left = left_ops_tup

        ## \var right The tuple of right edge operators
        self.right = right_ops_tup


    ## Private method for setting name attribute
    def _set_name(self):
        self.name = 'fixed'


## \file periodic_edge_ops.py

from src import edge_operator

## The periodic edge operator subclass of edge operator will
#  handle the operators applied to grid edges with periodic
#  boundary conditions in the evaluation of the RHS of the PDE.
class PeriodicEdgeOps(edge_operator.EdgeOperator):

    ## The constructor
    def __init__(self):
        
        ## \var name The type of boundary: 'periodic'
        self.name = None
        self._set_name()

    def _set_name(self):
        self.name = 'periodic'


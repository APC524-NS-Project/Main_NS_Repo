## \file edge_operator.py

## The abstract edge operator class will handle the operators
#  applied to the edges of the grid in the evaluation of the
#  RHS of the PDE.
class EdgeOperator():

    ## The constructor must define a name attribute
    def __init__(self):

        ## \var name Either 'fixed' or 'periodic'
        self.name = None
        self._set_name()

    ## The private method for setting the name attribute
    def _set_name(self):
        pass

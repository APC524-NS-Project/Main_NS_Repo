## \file problem.py

## The abstract Problem class
#  
#  Concrete sublclasses define the constant parameters and RHS
#  function operators
class Problem():

    ## The constructor initializes the problem with operator
    #  members and constant parameter members
    def __init__(self):

        ## \var ops_set_flag False if the operators have not
        #  been defined
        self.ops_set_flag = False

        ## \var ops A tuple containing strings for the names of
        #  each required operator object
        self.ops = ()

    ## The RHS function applies the defined operators to the
    #  grid argument in a defined manner.
    def RHS(self):
        pass

    ## The set_ops function takes a dictionary of linear 
    #  operators defined elsewhere and sets them to the
    #  correct member variables in the problem.
    def set_ops(self):
        pass




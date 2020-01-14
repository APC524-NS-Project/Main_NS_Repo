## @file dirichlet_hand.py
#
# file containing the abstract base class for applying the PDE problem's boundary conditions.
#
import src.BCHandler as bch

##  Base class for implementing the PDE problem's boundary conditions.
class DirichletHand(bch.BCHandler):
    
    ## The constructor
    # @param bc_list List of BCs objects containing the desired boundary conditions.
    def __init__(self,bc_list):
        self.bc_type="Dirichlet"
        self.bc_list=bc_list
        self._check_BCtype()
            
    
    ## Method to build up the tuple needed to reference the needed slice
    # @param bc the specific BCs object to use
    # @param gridqty the GridQty object to set boundaries for
    def _BC_idxs_tuple(self,bc,gridqty):
        qty_dim = gridqty.ndim #should call numpy ndim attr on gridqty.grid
        bc_dimen,bc_side = bc.get_bd()
        #translate symbology to numbers
        if bc_side == 'r':
            bc_idx = -1
        elif bc_side == 'l':
            bc_idx = 0
        else:
            raise ValueError("Boundary condition side specification should be left 'l' or right 'r'.") 
        
        #build the tuple (as a list first)
        idxs_list = []
        for i in range(qty_dim):
            if i == bc_dimen:
                idxs_list.append(tuple(bc_idx))
            else:
                idxs_list.append((0,gridqty.gqshape[i]))
        
        idxs=tuple(idxs_list)
        return idxs
    
    ## Method to implement the contained boundary conditions
    # @param time the current timestep (for use in time-dependent boundary conditions)
    # @param gridqty the GridQty object to set boundaries for
    def set_BCs(self,time,gridqty):
        for bc in self.bc_list:
            idxs = self._BC_idxs_tuple(bc,gridqty)
            try:
                gridqty.setslice(idxs,bc.vals)
            except:
                print("Incorrect boundary condition dimensions were specified. Try again.\n")
            
    
    ## Method to check if the correct type of boundary conditions have been passed to the handler
    def _check_BCtype(self):
        for bc in self.bc_list:
            assert self.bc_type.lower() == bc.get_bctype().lower(), "At least one boundary condition did not match the BCHandler's specified type, {}".format(self.bc_type)
            
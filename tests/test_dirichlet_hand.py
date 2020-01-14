# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 10:19:15 2020

@author: kbergste
"""

import unittest

import src.static_bcs as sbcs
import src.dirichlet_hand as dh
import src.grid as grid
import numpy as np

class DirichletHandTest(unittest.TestCase):

    def setUp(self):
        self.dimen1 = 0
        self.dimen2 = 1
        self.side1 = 'r'
        self.side2 = 'l'
        self.vals = np.array([1.,2.,3.,4.])
        self.bc_list=[sbcs.Dirichlet(self.dimen1,self.side1,self.vals),sbcs.Dirichlet(self.dimen2,self.side2,self.vals)]
        self.bch=dh.DirichletHand(self.bc_list)
        
        self.coords=((0,1,2,3),(3,4,5,6))
        self.initial_vals = np.zeros((4,4))
        self.time = 0
        self.gspec = grid.CartesianGridSpec(self.coords)
        self.gscl = grid.GridScalar(self.gspec,self.initial_vals)
    
    def test_init(self):
        self.assertEqual(self.bc_list,self.bch.bc_list)

    def test_BC_idxs_tuple(self):
        idxs = self.bch._BC_idxs_tuple(self.bch.bc_list[0],self.gscl)
        #for first boundary, returned tuple should be ((-1,0),(0,4))
        self.assertEqual(idxs,((-1,0),(0,4)))
        
        
    def test_set_BCs(self):
        self.bch.set_BCs(self.time,self.gscl)
        bc_added=self.initial_vals
        bc_added[-1,:]= self.vals
        bc_added[:,0]= self.vals
        np.array_equal(self.gscl.grid,bc_added)
        
        
        
if __name__ == '__main__':
    unittest.main()
    
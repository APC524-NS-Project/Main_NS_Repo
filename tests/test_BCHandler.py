# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 10:19:15 2020

@author: kbergste
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import unittest

import src.BCs as BCs
import src.BCHandler as BCHandler
import numpy

class DirichletHandTest(unittest.TestCase):

    def setUp(self):
        self.dimen = 1
        self.side = 'r'
        self.vals = numpy.array([1.,2.,3.,4.])
        self.bc_list=[BCs.Dirichlet(self.dimen,self.side,self.vals),BCs.Dirichlet(self.dimen,self.side,self.vals)]
        self.bch=BCHandler.DirichletHand(self.bc_list)
    
    def test_init(self):
        self.assertEqual(self.bc_list,self.bch.bc_list)
        
        
if __name__ == '__main__':
    unittest.main()
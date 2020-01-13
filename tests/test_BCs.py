# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 10:18:22 2020

@author: kbergste
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import unittest
import src.BCs as BCs
import numpy

class DirichletTest(unittest.TestCase):
    def setUp(self):
        self.dimen = 1
        self.side = 'r'
        self.vals=numpy.array([4.,5.,6.,7.])
        self.bcs=BCs.Dirichlet(self.dimen,self.side,self.vals)
        
    def test_init(self): #checks that the attributes were assigned correctly
        self.assertEqual(self.side,self.bcs.side)
        self.assertEqual(self.dimen,self.bcs.dimen)
        self.assertEqual(self.vals[0],self.bcs.bound_vals[0])
        
    def test_get_bd(self): #checks that boundary info is returned correctly
        dimen,side = self.bcs.get_bd()
        self.assertEqual(self.side,side)
        self.assertEqual(self.dimen,dimen)
        
    def test_get_bctype(self): #checks that bc type is returned correctly
        self.assertEqual(self.bcs.get_bctype().lower(),"dirichlet")
        
class NeumannTest(unittest.TestCase):
    def setUp(self):
        self.dimen = 1
        self.side = 'r'
        self.vals=numpy.array([4.,5.,6.,7.])
        self.bcs=BCs.Neumann(self.dimen,self.side,self.vals)
        
    def test_init(self): #checks that the attributes were assigned correctly
        self.assertEqual(self.side,self.bcs.side)
        self.assertEqual(self.dimen,self.bcs.dimen)
        self.assertEqual(self.vals[0],self.bcs.bound_vals[0])
        
    def test_get_bd(self): #checks that boundary info is returned correctly
        dimen,side = self.bcs.get_bd()
        self.assertEqual(self.side,side)
        self.assertEqual(self.dimen,dimen)
        
    def test_get_bctype(self): #checks that bc type is returned correctly
        self.assertEqual(self.bcs.get_bctype().lower(),"neumann")

if __name__ == '__main__':
    unittest.main()
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
        self.side = 5
        self.vals=numpy.array([4.,5.,6.,7.])
        self.bcs=BCs.Dirichlet(self.side,self.vals)
        
    def test_init(self): #checks that the attributes were assigned correctly
        self.assertEqual(self.side,self.bcs.side)
        self.assertEqual(self.vals[0],self.bcs.vals[0])
        
    def test_get_bd(self): #checks that side number is returned correctly
        self.assertEqual(self.side,self.bcs.get_bd())

if __name__ == '__main__':
    unittest.main()
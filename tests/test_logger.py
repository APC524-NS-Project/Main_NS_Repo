# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 14:57:24 2020

@author: kbergste
"""
import unittest
import src.logger as logger
import src.grid as grid
import numpy as np

class TestLogger(unittest.TestCase):
    def setUp(self):
        test_shape = ((-1,-.5,0,.5,1),(-2,0,2,4))
        self.tgrid = np.ones((5,4))
        self.tgrid[3,2]=12
        self.tgrid[1,1]=5
        self.gspec = grid.CartesianGridSpec(test_shape)
        self.grid = grid.GridScalar(self.gspec,self.tgrid)
        self.logg = logger.Logger()
        #instantiate two items in the log_list
        self.logg.log(0.,self.grid)
        self.logg.log(3.,self.grid)
        
    def test_log(self):
        self.assertEqual(len(self.logg.log_list),2) #2 elements in log_list
        self.assertEqual(len(self.logg.log_list[0]),2) #each element is a 2-element list
        self.assertEqual(isinstance(self.logg.log_list[0][1],grid.GridScalar),True) #obj in right place
        
    def test_get_frame(self):
        self.assertEqual(self.logg.get_frame(1)[0],3.) #recovers correct time using get_frame

    def test_get_nframes(self):
        self.assertEqual(self.logg.get_nframes(),2) #recovers correct time using get_frame
        
    def test_get_data_limits(self):
        self.assertEqual(self.logg.get_data_limits(),(1,12))

if __name__ == '__main__':
    unittest.main()    
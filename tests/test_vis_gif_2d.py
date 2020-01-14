# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 15:31:39 2020

@author: kbergste
"""

import unittest
import src.logger as logger
import src.grid as grid
import src.vis_gif_2d as vis
import numpy as np

class TestVisGif2d(unittest.TestCase):
    def setUp(self):
        test_shape = ((-1,-.5,0,.5,1),(-2,0,2,4))
        self.tgrid = np.ones((5,4))
        self.gspec = grid.CartesianGridSpec(test_shape)
        self.grid = grid.GridScalar(self.gspec,self.tgrid)
        self.logg = logger.Logger()
        self.vis = vis.VisGif2d(r"tests/test_outs/")
        #instantiate many items in the log_list
        for i in range(50):
            self.logg.log(i,self.grid+i)
            
    def test_make_2d_movie(self):
        self.vis.make_2d_movie(self.logg)
        #basically if this doesn't crash it's good
        
        
if __name__ == '__main__':
    unittest.main() 
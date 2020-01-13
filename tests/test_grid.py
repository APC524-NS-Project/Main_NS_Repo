import unittest
import numpy as np
from src import grid

class testGrid(unittest.TestCase):
	def setUp(self):
		test_shape = (2,4,3)
		self.grid = grid.GridQty(test_shape)

		self.tgrid = np.array([[[0,0,0],
							[0,0,0],
							[0,0,0],
							[0,0,0]],
							[[1,1,1],
							[1,1,1],
							[1,1,1],
							[1,1,1]]])

	def test_getslice(self):
		indices = ((0,2),(0,2),(1,3))
		idxs = [range(*t) for t in indices]
        
		self.array_equal(self.tgrid[self.grid.getslice(indices)],self.tgrid[np.ix_(idxs)])

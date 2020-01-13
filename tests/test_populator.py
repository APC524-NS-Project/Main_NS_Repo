import unittest
from src import populator
from src import OperatorMatrix
import numpy as np

class testPopulator(unittest.TestCase):
	def setUp(self):
		mock1 = mockSpec((2,4),1)
		inputs = ((mock1,0),)
		self.populs = (populator.Populator(inputs[0][0],inputs[0][1]),)

	#test _get_single_index method of populator
	def test_GSI(self):
		inputs = (([2,0],[0,1],[3,1]),)
		outputs_exp = ((2,4,7),)
		for idx,popul in enumerate(self.populs):
			for idx2,coord in enumerate(inputs[idx]):
				output = popul._get_single_index(coord)

				self.assertEqual(output,outputs_exp[idx][idx2])

	def test_set_row(self):
		op1d = mockOp1D([-1,0,1],[1,-2,1],2)
		popul = self.populs[0]
		opmat = OperatorMatrix.OperatorMatrix(8)
		coords = [1,0]
		opindex = popul._get_single_index(coords)

		# Build correct output
		opmat_out = OperatorMatrix.OperatorMatrix(8)
		opmat_out[1,0] = 1
		opmat_out[1,1] = -2
		opmat_out[1,2] = 1

		# Test function
		popul._set_row(op1d,coords,opmat,opindex)

		np.testing.assert_array_equal(opmat.array,opmat_out.array)

class mockSpec():
	def __init__(self,shape,dx):
		self.shape = shape
		self.dx = dx

class mockOp1D():
	def __init__(self,stencil,weights,d):
		self.stencil = stencil
		self.weights = weights
		self.d = d
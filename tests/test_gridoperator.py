import unittest
import numpy as np
from src import gridoperator
from src import operatormatrix
from mock import Mock
from mock import MagicMock

class testGridOp(unittest.TestCase):
	def setUp(self):
		self.gop = object.__new__(gridoperator.GridOperator)
		self.mockfd = op1d([0,1,2],[1,-2,1],2)
		self.mockbd = op1d([-2,-1,0],[1,-2,1],2)
		self.mockcd = op1d([-1,0,1],[1,-2,1],2)


	def test_getInt(self):
		mock1d = op1d([-1,0,2],[1,-2,1],2)
		test_N = 5
		out_cor = (1,3)
		out = self.gop._get_Int(mock1d,test_N)
		self.assertEqual(out_cor,out)

		mock1d = op1d([-1,0,1],[1,-2,1],2)
		test_N = 4
		out_cor = (1,3)
		out = self.gop._get_Int(mock1d,test_N)
		self.assertEqual(out_cor,out)

	def test_instantization1d(self):
		self.mockSpec = Mock()
		self.mockSpec.dx = 1
		self.mockSpec.gridshape = (4,)
		self.mockSpec.ndim = 1

		self.mockScheme = Mock()
		self.mockScheme.dim = 1
		self.mockScheme.interior = [self.mockcd]

		self.mockScheme.edge = (((self.mockfd,),(self.mockbd,)),)

		self.gop_test = gridoperator.GridOperator(self.mockSpec,self.mockScheme)

		out_cor = operatormatrix.OperatorMatrix(4)
		out_cor[0,0:3] = self.mockfd.weights
		out_cor[1,0:3] = self.mockcd.weights
		out_cor[2,1:4] = self.mockcd.weights
		out_cor[3,1:4] = self.mockbd.weights

		self.compare_arrays(out_cor.array,self.gop_test.opmats[0].array)

	def test_instatization2dx(self):
		self.mockSpec2 = Mock()
		self.mockSpec2.dx = 1
		self.mockSpec2.gridshape = (3,3)
		self.mockSpec2.ndim = 2

		self.mockScheme2 = Mock()
		self.mockScheme2.dim = 2
		self.mockScheme2.interior = [None,self.mockcd]

		self.mockScheme2.edge = (None,((self.mockfd,),(self.mockbd,)))

		self.gop_test2 = gridoperator.GridOperator(self.mockSpec2,self.mockScheme2)

		out_cor = operatormatrix.OperatorMatrix(9)
		int_points = [1,4,7]
		for pt in int_points:
			out_cor[pt,pt-1:pt+2] = self.mockcd.weights

		left_points = [0,3,6]
		for pt in left_points:
			out_cor[pt,pt:pt+3] = self.mockfd.weights

		right_points = [2,5,8]
		for pt in right_points:
			out_cor[pt,pt-2:pt+1] = self.mockbd.weights

		self.compare_arrays(out_cor.array,self.gop_test2.opmats[1].array)



	def compare_arrays(self,ar1,ar2):
		np.testing.assert_array_equal(ar1,ar2,verbose=True)



class op1d():
	def __init__(self,s,weights,d):
		self.weights = weights
		self.stncl = stencil(s)

		self.d = d

class stencil():
	def __init__(self,s):
		self.s = s
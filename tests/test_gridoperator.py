import unittest
import numpy as np
from src import gridoperator
from src import operatormatrix
from mock import Mock
from mock import MagicMock

class testGridOp(unittest.TestCase):
	def setUp(self):
		self.gop = object.__new__(gridoperator.GridOperator)

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

	def test_instantization(self):
		self.mockSpec = Mock()
		self.mockSpec.dx = 1
		self.mockSpec.gridshape = (4,)
		self.mockSpec.ndim = 1

		self.mockScheme = Mock()
		self.mockScheme.dim = 1
		self.mockcd = op1d([-1,0,1],[1,-2,1],2)
		self.mockScheme.interior = [self.mockcd]
		# self.mockScheme.interior[0].stcl = Mock()		
		# self.mockScheme.interior[0].stcl.s = MagicMock(return_value=[-1,0,1])
		# self.mockScheme.interior[0].weights = MagicMock(return_value = [1,-2,1])

		self.mockfd = op1d([0,1,2],[1,-2,1],2)
		# self.mockfd = Mock()
		# self.mockfd.stcl = Mock()
		# self.mockfd.stcl.s = MagicMock(return_value=[0,1,2])
		# self.mockfd.weights = MagicMock(return_value=[1,-2,1])

		self.mockbd = op1d([-2,-1,0],[1,-2,1],2)
		# self.mockbd = Mock()
		# self.mockbd.stcl = Mock()
		# self.mockbd.stcl.s = MagicMock(return_value=[-2,-1,0])
		# self.mockbd.stcl.s = MagicMock(return_value=[1,-2,1])

		self.mockScheme.edge = (((self.mockfd,),(self.mockbd,)),)

		gop_test = gridoperator.GridOperator(self.mockSpec,self.mockScheme)

		out_cor = operatormatrix.OperatorMatrix(4)
		out_cor[0,0:3] = self.mockfd.weights
		out_cor[1,0:3] = self.mockcd.weights
		out_cor[2,1:4] = self.mockcd.weights
		out_cor[3,1:4] = self.mockbd.weights

		self.compare_arrays(out_cor.array,gop_test.opmats[0].array)

	def compare_arrays(self,ar1,ar2):
		np.testing.assert_array_equal(ar1,ar2)



class op1d():
	def __init__(self,s,weights,d):
		self.weights = weights
		self.stncl = stencil(s)

		self.d = d

class stencil():
	def __init__(self,s):
		self.s = s
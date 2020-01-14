import unittest
import numpy as np
from src import gridoperator
from src import operatormatrix

class testGridOp(unittest.TestCase):
	def setUp(self):
		self.gop = object.__new__(gridoperator.GridOperator)

	def test_getInt(self):
		mock1d = Mock()
		mock1d.stcl = Mock()
		mock1d.s = [-1,0,2]
		test_N = 5
		out_cor = (1,3)
		out = self.gop._get_Int(mock1d,test_N)
		self.assertEqual(out_cor,out)

	def test_instantization(self):
		self.mockSpec = Mock()
		self.mockSpec.dx = 1
		self.mockSpec.gridshape = (4,)
		self.mockSpec.ndim = 1

		self.mockScheme = Mock()
		self.mockScheme.interior = [Mock()]
		self.mockScheme.interior[0].stcl = Mock()		
		self.mockScheme.interior[0].stcl.s = [-1,0,1]
		self.mockScheme.interior[0].weights = [1,-2,1]

		self.mockfd = Mock()
		self.mockfd.stcl = Mock()
		self.mockfd.stcl.s = [0,1,2]
		self.mockfd.weights = [1,-2,1]

		self.mockbd = Mock()
		self.mockbd.stcl = Mock()
		self.mockbd.stcl.s = [-2,-1,0]
		self.mockbd.stcl.s = [1,-2,1]

		self.mockScheme.edge = ((self.mockbd,),(self.mockfd,))

		gop_test = gridoperator.GridOperator(self.mockSpec,self.mockScheme)

		out_cor = operatormatrix.OperatorMatrix(4)
		out_cor[0,0:3] = self.mockfd.stcl.s
		out_cor[1,0:3] = self.mockScheme.interior[0].stcl.s
		out_cor[2,1:4] = self.mockScheme.interior[0].stcl.s
		out_cor[3,1:4] = self.mockbd.stcl.s

		self.compare_arrays(out_cor.array,gop_test.opmats[0].array)

	def compare_arrays(self,ar1,ar2):
		np.testing.assert_array_equal(ar1,ar2)


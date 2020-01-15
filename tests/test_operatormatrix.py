import unittest
import numpy as np
from src import operatormatrix

class testOpMat(unittest.TestCase):
	def test_add(self):
		op1 = operatormatrix.OperatorMatrix(3)
		op2 = operatormatrix.OperatorMatrix(3)
		op1[0,0] = 1
		op2[0,1] = 2

		op3 = operatormatrix.OperatorMatrix(3)
		op3[0,0:2] = [1,2]

		op4 = op1 + op2

		np.testing.assert_array_equal(op4.array.todense(),op3.array.todense())
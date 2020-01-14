from unittest import TestCase
import numpy as np
from src import stencil, operator_1d

class test_Operator1D(TestCase):
	def test_init(self):
		# tests are tuple consisting of array containing s, array containing correct weight output, and order of derivative
		tests = ((np.array([-2,-1,0]),np.array([[1,-2,1]]),2),
				(np.array([-4,-3,-2,-1,0,1,2,3,4]),np.array([[1./280,-4./105,1./5,-4./5,0.,4./5,-1./5,4./105,-1./280]]),1),
				(np.array([-1,0,1]),np.array([[1,-2,1]]),2))

		for test in tests:
			op1d = operator_1d.Operator1D(test[0], test[2])
			np.testing.assert_almost_equal(op1d.weights,test[1])

from unittest import TestCase
import numpy as np
from src import stencil

class test_Stencil(TestCase):
	def test_stencil_matrix(self):
		# tests are tuples consisting of array containing indicies s and an array corresponding to the correct output of s_matrix
		tests = (([-2,-1,0,1,2],np.array([[ 1, 1,1,1,1],
										[-2,-1,0,1,2],
										[ 4, 1,0,1,4],
										[-8,-1,0,1,8],
										[16, 1,0,1,16]])),
					(np.array([-2,-1,0]),np.array([[ 1, 1,1],
								[-2,-1,0],
								[ 4, 1, 0]])))

		for test in tests:
			stcl = stencil.Stencil(test[0])
			stcl._stencil_matrix()

			np.testing.assert_array_equal(stcl.s_matrix,test[1])

	def test_weights(self):
		# tests are tuple consisting of array containing s, array containing correct weight output, and order of derivative
		tests = ((np.array([-2,-1,0]),np.array([[1,-2,1]]),2),
				(np.array([-4,-3,-2,-1,0,1,2,3,4]),np.array([[1./280,-4./105,1./5,-4./5,0.,4./5,-1./5,4./105,-1./280]]),1),
				(np.array([-1,0,1]),np.array([[1,-2,1]]),2))

		for test in tests:
			stcl = stencil.Stencil(test[0])
			weights = stcl.get_weights(test[2])
			np.testing.assert_almost_equal(weights,test[1])
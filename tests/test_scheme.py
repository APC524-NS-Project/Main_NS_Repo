from unittest import TestCase
import numpy as np
from src import scheme

## test_finite_difference_stencil_factory
# unittests for finite_difference_stencil_factory classs
class test_FDSF(TestCase):


	def setUp(self):
		self.factory = scheme.finite_dif_stencil_factory()

	## test_stencil_matrix
	# verify that the stencil matrix function correctly generates the stencil matricies
	def test_stencil_matrix(self):
		test_s = np.array([-2,-1,0,1,2])
		test_a_cor = np.array([[ 1, 1,1,1,1],
								[-2,-1,0,1,2],
								[ 4, 1,0,1,4],
								[-8,-1,0,1,8],
								[16, 1,0,1,16]])

		test_a = self.factory._stencil_matrix(test_s)

		np.testing.assert_array_equal(test_a, test_a_cor)

		test_s = np.array([-2,-1,0])
		test_a_cor = np.array([[ 1, 1,1],
								[-2,-1,0],
								[ 4, 1, 0]])

		test_a = self.factory._stencil_matrix(test_s)

		np.testing.assert_array_equal(test_a,test_a_cor)

	## test_gen_stencil
	# verify that the gen_stencil function correctly generates FD stencils for a given stencil point set and equation order
	# only check that the array is almost equal to the reference values due to floating point arithmatic
	def test_gen_stencil(self):
		s = np.array([-2,-1,0])
		a_cor = np.array([[1,-2,1]])
		d = 2

		a = self.factory.gen_stencil(d,s)
		np.testing.assert_almost_equal(a,a_cor)

		s = np.array([-4,-3,-2,-1,0,1,2,3,4])
		a_cor = np.array([[1./280,-4./105,1./5,-4./5,0.,4./5,-1./5,4./105,-1./280]])
		d = 1

		a = self.factory.gen_stencil(d,s)
		np.testing.assert_almost_equal(a,a_cor)

		s = np.array([-1,0,1])
		a_cor = np.array([[1,-2,1]])
		d = 2

		a = self.factory.gen_stencil(d,s)
		np.testing.assert_almost_equal(a,a_cor)

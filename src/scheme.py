## @package scheme
# Implementation of various Forward Difference schemes
# Package contains relevant classes to produce Scheme classes, which have the ability to produce discretizations elementary linear operators for a given Grid object

import numpy as np
from abc import ABC
import math

## finite_dif_stencil_factory
# Generates stencils for an arbitrary finite difference scheme
class finite_dif_stencil_factory:

	## gen_stencil
	# Returns an array containing finite difference coefficients for a given set of arbitrary stencil points
	# Implentation according to formula given in https://en.wikipedia.org/wiki/Finite_difference_coefficient for arbitrary stencil points
	## @var d
	# Order of derivative
	## @var s
	# Numpy array containing set of arbitrary stencil points of dimension N
	## @var s_matrix
	# Matrix comprising the LHS of the arbitrary stencil point formula
	## @var s_matrix_inv
	# Inverse of s_matrix
	## @var rhs_matrix
	# Matrix consiting of the RHS of the arbirtrary stencil point forumla. Only non-zero value is d! at the index d. Matrix has dimensions Nx1
	## @var a_matrix
	# matrix of stencil coefficient values of size Nx1
	def gen_stencil(self,d,s):
		s_matrix = self._stencil_matrix(s)
		s_matrix_inv = np.linalg.inv(s_matrix)

		rhs_matrix = np.zeros((N,1))
		rhs_matrix[d] = math.factorial(d)

		a_matrix = s_matrix_inv * rhs_matrix

		return a_matrix

	## _stencil_matrix
	# Generates LHS matrix of stencil points. matrix has dimensions NxN
	## @var N
	# Number of stencil points
	## @var s_matrix
	# Matrix of size NxN with rows consisting of the stencil points raised to the power of that row's index
	def _stencil_matrix(s):
		N = s.size()
		s_matrix = np.zeros((N,N))

		for i in range(N):
			s_matrix[i,:] = np.power(s,i)

		return s_matrix


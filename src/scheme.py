## @package scheme
# Implementation of various Forward Difference schemes
# Package contains relevant classes to produce Scheme classes, which have the ability to produce discretizations elementary linear operators for a given Grid object

import numpy as np
from abc import ABC

## finite_dif_stencil_factory
# Generates stencils for an arbitrary finite difference scheme
class finite_dif_stencil_factory:

	## gen_stencil
	# returns an array containing finite difference coefficients for a given set of arbitrary stencil points
	# implentation according to formula given in https://en.wikipedia.org/wiki/Finite_difference_coefficient for arbitrary stencil points
	## @var d
	# order of derivative
	## @var s
	# numpy array containing set of arbitrary stencil points of dimension N
	def gen_stencil(d,s):



	## _stencil_matrix
	# generates LHS matrix of stencil points. matrix has dimensions NxN
	## @var N
	# number of stencil points
	## @var s_matrix
	# matrix of size NxN with rows consisting of the stencil points raised to the power of that row's index
	def _stencil_matrix(s):
		N = s.size()
		s_matrix = np.zeros((N,N))

		for i in range(N):
			s_matrix[i,:] = np.power(s,i)

		return s_matrix


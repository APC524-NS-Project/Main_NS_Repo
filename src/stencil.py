import math
import numpy as np

## Stencil
# A finite difference stencil to calculate an operator.

class Stencil():
	## Constructor
	# Constructs stencil from an initial array.
	#
	# @param s list containing index of points contained in stencil. 0 corresponds to point operator is calculating for. Implemented as numpy array
	# @var N number of stencil points
	def __init__(self, s):
		self.s = np.array(s)
		self.N = len(self.s)


	## get_weights
	# Generates list of FD weights for a given stencil.
	#
	# Computes FD weights for a given stencil computing a derivative of degree d
	# Implementation of algorithm given in https://en.wikipedia.org/wiki/Finite_difference_coefficient for arbitrary stencil points
	# @param d degree of derivative
	# @var s_matrix_inv inverse of stencil matrix
	# @var rhs_matrix matrix comprising rhs of aribtrary stencil points forumula
	# @var weights computed by algorithm
	def get_weights(self,d):
		self._stencil_matrix()
		s_matrix_inv = np.linalg.inv(self.s_matrix)

		rhs_matrix = np.zeros((self.N,1))
		rhs_matrix[d] = math.factorial(d)

		weights = np.dot(s_matrix_inv,rhs_matrix)

		return np.transpose(weights)

	## _stencil_matrix
	# Generates matrix of stencil coefficients
	#
	# Matrix has rows corresponding to stencil index location raised to a power equal to the index of the row
	# @var s_matrix matrix of stencil indicies for use in valculation
	def _stencil_matrix(self):
		self.s_matrix = np.zeros((self.N,self.N))

		for i in range(self.N):
			self.s_matrix[i,:] = np.power(self.s,i)
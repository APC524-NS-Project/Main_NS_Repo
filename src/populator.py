import numpy as np
import math

## Populator
# Function to populate an op_matrix according to a particular 1d operator
#
# CLass can take a 1d operator and a portion of a grid to generate FD values for each index in a matrix operator that can then calculate that finite difference.
class Populator():
	## Constructor
	# Constructs Populator
	#
	# @params spec A grid specification object corresponding to the grid on which the FD is being calculated
	# @params op1d An Operator1D object containing a stencil and a set of weights for that stencil
	# @params dim The dimension along which the 1D operator is being applied
	def __init__(self,spec,op1d,dim):
		self.shape = spec.shape
		self.op1d = op1d
		self.dim = dim

	## populate_op
	# Populates rows of an operator matrix for specified grid points
	#
	# Applies finite difference stencil to generate rows of an operator matrix corresponding to 
	def populate_op(self,mesh,op_mat):


	## _get_single_index
	# Generates a single flattened index for an n-dimensional grid position.
	#
	# Private method which returns the corresponding to a particular set of n-dimensional coordinates specifying location on a grid.
	# @params coords A list of coordinates with length equal to length(self.shape).
	# @vars index The index corresponding to a row-major flattening operation applied to the n-dimensional matrix to express it as a 1D matrix.
	def _get_single_index(self,coords):
		index = 0
		for idx, val in enumerate(self.shape):
			if idx = 0:
				index += coords[idx]
			else:
				idx = += coords[idx]*sum(self.shape[0:idx])

		return index



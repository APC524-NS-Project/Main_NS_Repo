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
	# @params dim The dimension along which the 1D operator is being applied
	# @var dx The grid spacing in real space
	def __init__(self,spec,dim):
		self.shape = spec.gridshape
		self.dim = dim
		self.dx = spec.dx

	## populate_op
	# Populates rows of an operator matrix for specified grid points
	#
	# Applies finite difference stencil to generate rows of an operator matrix corresponding to 
	# @param mesh Tuple of size n where each object is a grid containing the index of that grid position in the n-th dimension of the grid. Mesh has been pre-sorted to remove boundaries (areas where the given op1d won't fit)
	# @param op_mat Operator matrix which will have values populated according to the FD scheme specified in the Operator1D.
	# @params op1d An Operator1D object containing a stencil and a set of weights for that stencil.
	# @var total_points total number of points in subset of grid that we want to fill in the mat_op for
	# @var coords n-dimensional coordinates of point given by different grid meshes
	# @var op_index row index of the row corresponding to the current point in the operator matrix
	def populate_op(self,mesh,op_mat,op1d):
		total_points = np.prod(mesh.shape)

		for point in range(0,total_points):
			coords = []
			for axis in mesh.meshes:
				coords.append(axis.flat[point])

			op_index = self._get_single_index(coords)
			self._set_row(op1d,coords,op_mat,op_index)


	## _set_row
	# Method used by populate_op to set a single row of the operator matrix	
	#
	# Generates new coordinates as modified in the relevant dimension by the stencil, then uses the weight associated by that stencil point modified by the grid spacing to generate the particular value of operator matrix at that point.
	# @var new_coords Coordinates modified by the value in the stencil in the dimesion the op_matrix is being populated for
	# @var weight_index single index value in the flattened grid corresponding to 
	def _set_row(self,op1d,coords,op_mat, op_index):
		for idx, weight in enumerate(op1d.weights):
			new_coords = coords.copy()
			new_coords[self.dim] += op1d.stncl.s[idx]
			weight_index = self._get_single_index(new_coords)
			op_mat[op_index,weight_index] = weight/np.power(self.dx,op1d.d)

	## _get_single_index
	# Generates a single flattened index for an n-dimensional grid position.
	#
	# Private method which returns the corresponding to a particular set of n-dimensional coordinates specifying location on a grid.
	# @params coords A list of coordinates with length equal to length(self.shape).
	# @vars index The index corresponding to a row-major flattening operation applied to the n-dimensional matrix to express it as a 1D matrix.
	def _get_single_index(self,coords):
		index = 0
		for idx, val in enumerate(self.shape):
			if idx == len(self.shape)-1:
				index += coords[idx]
			else:
				index += coords[idx]*sum(self.shape[idx+1:])

		return index



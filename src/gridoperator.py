## @file gridoperator.py
#
# Based on a grid and an n-diemnsional scheme this class generates a corresponding grid operator
# The grid operator is a callable object that if given a gridqty that shares a gridspec the grid operator will return 
# a gridqty of the same size with the results of the given finite difference operator applied to the 
# initial gridqty
# Grid operator uses the interior and boundary nd operators in nd scheme along with a populator to generate 
# operator matricies for each dimension and then combines them to produce a single operator matrix

import numpy as np
import operatormatrix
import mesh
import populator

## GridOperator
# GridOperator class definition
class GridOperator():
	# @var opmats list to hold the operatormatricies generated for each dimension
	opmats = []

	## Contstructor
	# Constructs grid operator.
	#
	# Constructor is responsible for generating an operator matrix for each dimesion of the underlying grid.
	# It does this by populating the operator matrix with the given FD weights for both the interior FD operator as 
	# well as the operators for each boundary, applying a new 1d operator for each index contained in the boundary layer
	# as laid out in the op_nd_scheme specification. Note that the dimensions of the grid MUST match the dimensions of the NDscheme
	# @param spec a GridSpec object corresponding to the grid on which the GridOperator will be applied
	# @param ndscheme an OperatorNDScheme object containing an interior ND operator as well as a tuple of boundary operators. Must have same dimensions as grid
	def __init__(self,spec,ndscheme):
		self.spec = spec
		self.ndscheme = ndscheme

		if self.spec.dim != self.ndscheme.dim:
			raise ValueError("ND Scheme does not have the appropriate dimensions for this Grid")

		for idx in range(self.spec.dim):
			if self.ndscheme.interior[idx] != None:
				interior = self._get_Int(self.ndscheme.interior[idx],self.spec.gridshape[idx])




	## _get_Int
	# return a tuple corresponding to the coordinates of the interior
	#
	# @params op1d a Operator1D object
	# @params size length of grid in a particular dimension
	# @var bll index of leftmost interior point
	# @var blr index to the right of rightmost interior point
	def _get_Int(self,op1d,size):
		bll = - op1d.stcl.s[0]
		blr = size - op1d.stcl.s[-1]

		return (bll,blr)

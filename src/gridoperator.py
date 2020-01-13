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
	# @var opmats list to hold the operator matricies generated for each dimension
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
	# @var basemesh a Mesh object instantiated to match the shape of the underlying Grid
	# @var N size of the operator matrix, consists of the product of the size of each axis in grid
	# @var idx integer representation of the dimension being evaluated, where the representation corresponds to the dimension's index in spec.gridshape
	# @var opmat an OperatorMatrix that will be filled 
	# @var popul Populator object for the given dimension being considered
	# @var interior coordinates of the interior of the 
	# @var opmats recast opmats list to a tuple after instantiation 
	# @var scalar_op The given grid operator linearlly combined such that it would act on a scalar and return a scalar
	def __init__(self,spec,ndscheme):
		self.spec = spec
		self.ndscheme = ndscheme

		if self.spec.ndim != self.ndscheme.dim:
			raise ValueError("ND Scheme does not have the appropriate dimensions for this Grid")

		self.basemesh = mesh.Mesh(self.spec.gridshape)
		self.N = np.product(spec.gridshape)

		for idx in range(self.spec.ndim):
			if self.ndscheme.interior[idx] != None:
				opmat = operatormatrix.OperatorMatrix(self.N)
				popul = populator.Populator(self.spec,idx)

				interior = self._get_Int(self.ndscheme.interior[idx],self.spec.gridshape[idx])
				self._apply_op(popul,opmat,self.ndscheme.interior[idx],interior)

				self._bl_set(popul,opmat,self.ndscheme.edge[idx],interior,self.spec.gridshape[idx])

				opmats.append(opmat)
			else:
				opmats.append(None)

		opmats = tuple(opmats)

		

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

	## _apply_op
	# Apply a 1d operator to a subset of the mesh using the populator
	#
	# Create an appropriate slices tuple for the given slice in the dimension of the populator.
	# Then use that to generate a submesh and then call the Populator's populate_op function on that given sub_mesh
	# @params popul a Populator object
	# @params opmat an OperatorMatrix object
	# @params op1d a Operator1D object
	# @params slc a tuple containing (start, end) of a particular slice of the mesh
	# @var slices a set of slices for each dimension
	# @var sub_mesh a sliced version of the main mesh sliced by the tuple pairs in slices
	def _apply_op(self,popul,opmat,op1d,slc):
		slices = [(None,)]*self.spec.ndim
		slices[popul.dim] = slc

		sub_mesh = self.mesh.sub_slice(slices)
		popul.populate_op(sub_mesh,opmat,op1d)

	## _bl_set
	# set the FD scheme for the Boundary Layer operators in the OperatorMatrix
	#
	# Takes a set of edge operators in the form 
	# ((op1D_L1, op1D_L2,...),(op1D_R1, op1D_R2,...))
	# and applies them to each layer of the boundary layer in the grid, where the boundary layer are the non-interior points
	# the Left side is the side with idx = 0
	# A different op1d is specified for each slice of the boundary layer
	# @params a Populator object
	# @params an OperatorMatrix object
	# @params edgeop a tuple of edge operators in the form ((op1D_L1, op1D_L2,...),(op1D_R1, op1D_R2,...))
	# @params layer_dim a tuple corresponding to the left and rightmost edges of the interior points
	# @params N total size of the layer
	# @var slc a tuple containing the appropriate indexes for a single value slice of the mesh
	def _bl_set(self,popul,opmat,edgeop,layer_dim,N):
		for idx in range(layer_dim[0]):
			slc = (idx,idx+1)
			self._apply_op(popul,opmat,edgeop[0][idx],slc)

		for idx in range(N-layer_dim[0]):
			slc = (N-1-idx,N-idx)
			self._apply_op(popul,opmat,edgeop[1][idx],slc)

	def __call__(self,grid):
		
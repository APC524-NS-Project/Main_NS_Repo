import unittest
from src import populator
from src import operatormatrix
from src import mesh
import numpy as np
import mock

class testPopulator(unittest.TestCase):
	def setUp(self):
		mock1 = mockSpec((2,4),(1,1))
		inputs = ((mock1,1),)
		self.populs = (populator.Populator(inputs[0][0],inputs[0][1]),)

	#test _get_single_index method of populator
	def test_GSI(self):
		inputs = (([0,2],[1,0],[1,3]),)
		outputs_exp = ((2,4,7),)
		for idx,popul in enumerate(self.populs):
			for idx2,coord in enumerate(inputs[idx]):
				output = popul._get_single_index(coord)

				self.assertEqual(output,outputs_exp[idx][idx2])

	def test_set_row(self):
		op1d = mockOp1D([-1,0,1],[1,-2,1],2)
		popul = self.populs[0]
		opmat = operatormatrix.OperatorMatrix(8)
		coords = [0,1]
		opindex = popul._get_single_index(coords)

		# Build correct output
		opmat_out = operatormatrix.OperatorMatrix(8)
		opmat_out[1,0] = 1
		opmat_out[1,1] = -2
		opmat_out[1,2] = 1

		# Test function
		popul._set_row(op1d,coords,opmat,opindex)

		self.array_equal(opmat.array.toarray(),opmat_out.array.toarray())

		op1d = mockOp1D([-2,-1,0],[1,-2,1],2)
		mock2 = mockSpec((4,),(1,))
		popul = populator.Populator(mock2,0)
		opmat = operatormatrix.OperatorMatrix(4)
		coords = [3]
		opindex = popul._get_single_index(coords)

		# Build correct output
		opmat_out = operatormatrix.OperatorMatrix(4)
		opmat_out[3,-3] = 1
		opmat_out[3,-2] = -2
		opmat_out[3,-1] = 1

		# Test function
		popul._set_row(op1d,coords,opmat,opindex)

		self.array_equal(opmat.array.toarray(),opmat_out.array.toarray())

	def test_populate(self):
		popul = self.populs[0]
		op1d = mockOp1D([-1,0,1],[1,-2,1],2)
		opmat = operatormatrix.OperatorMatrix(8)
		gridmesh = mesh.Mesh(popul.shape)

		#subslice out the center of the mesh corresponding to areas where this stencil can fit
		sub_mesh = gridmesh.sub_slice(((0,2),(1,3)))

		# generate correct operator matrix
		op_out = operatormatrix.OperatorMatrix(8)
		indexes = [1,2,5,6]
		for idx in indexes:
			op_out[idx,idx-1:idx+2] = [1,-2,1]

		popul.populate_op(sub_mesh,opmat,op1d)

		self.array_equal(opmat.array.toarray(),op_out.array.toarray())

	def array_equal(self,ar1,ar2):
		np.testing.assert_array_equal(ar1,ar2)


class mockSpec():
	def __init__(self,shape,dx):
		self.gridshape = shape
		self.spacing = dx

class mockOp1D():
	def __init__(self,stencil,weights,d):
		self.stncl = mock.Mock()
		self.stncl.s = stencil
		self.weights = weights
		self.deg = d
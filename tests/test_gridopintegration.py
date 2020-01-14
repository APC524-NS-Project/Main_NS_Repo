import unittest
import numpy as np
from src import operator_1d
from src import operator_nd
from src import op_nd_scheme
from src import gridoperator
from src import fixed_edge_ops
from src import grid
from src import operatormatrix

class testGridInt(unittest.TestCase):
	def setUp(self):
		self.opcd = operator_1d.Operator1D([-1,0,1],2)
		self.opbd = operator_1d.Operator1D([-2,-1,0],2)
		self.opfd = operator_1d.Operator1D([0,1,2],2)
		self.laplace_int = operator_nd.OperatorND((self.opcd,self.opcd))
		self.edge = fixed_edge_ops.FixedEdgeOps((self.opfd,),(self.opbd,))

		self.laplace_scheme = op_nd_scheme.OperatorNDScheme(self.laplace_int,(self.edge,self.edge))

		self.spec = grid.CartesianGridSpec(((0,1,2),(0,1,2)))

		self.grid_op = gridoperator.GridOperator(self.spec,self.laplace_scheme)

		# Define correct output
		x_out_cor = operatormatrix.OperatorMatrix(9)
		int_points = [1,4,7]
		weights = [1,-2,1]
		for pt in int_points:
			x_out_cor[pt,pt-1:pt+2] = weights

		left_points = [0,3,6]
		for pt in left_points:
			x_out_cor[pt,pt:pt+3] = weights

		right_points = [2,5,8]
		for pt in right_points:
			x_out_cor[pt,pt-2:pt+1] = weights

		y_out_cor = operatormatrix.OperatorMatrix(9)
		yweights = [1,0,0,-2,0,0,1]
		for j in range(3):
			for i in range(3):
				y_out_cor[3*i+j,j:j+7] = yweights

		self.laplace_cor = x_out_cor + y_out_cor

	def test_integration(self):
		
		self.compare_arrays(self.laplace_cor.toarray(),self.grid_op.scalar_op.toarray())

	def test_applyOpintegration(self):
		tgrid = np.zeros((3,3))
		tgrid[1,1] = 1
		tgrid = grid.GridScalar(self.spec,tgrid)

		result_grid = tgrid.applyOp(self.grid_op.scalar_op)

		result_cor = np.zeros((3,3))
		result_cor[1,:] = [-2,-4,-2]
		result_cor[0,1] = -2
		result_cor[2,1] = -2

		self.compare_arrays(result_grid.grid,result_cor)


	def compare_arrays(self,ar1,ar2):
		np.testing.assert_array_almost_equal(ar1,ar2)
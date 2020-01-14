import unittest
import numpy as np
from src import operator_1d
from src import operator_nd
from src import op_nd_scheme
from src import gridoperator
from src import fixed_edge_ops
from src import grid

class testGridInt(unittest.TestCase):
	def setUp(self):
		self.opcd = operator_1d.Operator1D([-1,0,1],2)
		self.opbd = operator_1d.Operator1D([-2,-1,0],2)
		self.opfd = operator_1d.Operator1D([0,1,2],2)

	def test_integration(self):
		laplace_int = operator_nd.OperatorND((self.opcd,self.opcd))
		edge = fixed_edge_ops.FixedEdgeOps((self.opfd,),(self.opbd,))

		laplace_scheme = op_nd_scheme.OperatorNDScheme(laplace_int,(edges,edges))


		spec = grid.CartesianGridSpec(((0,1,2),(0,1,2)))

		grid_op = gridoperator.GridOperator(spec,laplace_scheme)

		# Define correct outputs
		x_out_cor = operatormatrix.OperatorMatrix(9)
		int_points = [1,4,7]
		for pt in int_points:
			x_out_cor[pt,pt-1:pt+2] = self.mockcd.weights

		left_points = [0,3,6]
		for pt in left_points:
			x_out_cor[pt,pt:pt+3] = self.mockfd.weights

		right_points = [2,5,8]
		for pt in right_points:
			x_out_cor[pt,pt-2:pt+1] = self.mockbd.weights

		y_out_cor = operatormatrix.OperatorMatrix(9)
		yweights = [1,0,0,-2,0,0,1]
		for j in range(3):
			for i in range(3):
				y_out_cor[3*i+j,j:j+7] = yweights

		laplace_cor = x_out_cor + y_out_cor

	def compare_arrays(self,ar1,ar2):
		np.testing.assert_array_equal(ar1,ar2,verbose=True)
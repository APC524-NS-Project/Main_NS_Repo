import numpy as np
from src import operator_1d
from src import operator_nd
from src import op_nd_scheme
from src import fixed_edge_ops
from src import grid
from src import gridoperator

def main():
	nx = 100
	ny = 100
	dx = 2 / (nx - 1)
	dy = 2 / (ny - 1)

	x = np.linspace(0, 2, nx)
	y = np.linspace(0, 2, ny)
	coords=(tuple(x),tuple(y))


	# Sloppily assign initial conditions
	u = np.zeros((ny, nx))
	# set hat function I.C. : u(.5<=x<=1 && .5<=y<=1 ) is 2
	u[int(.5 / dy):int(1 / dy + 1),int(.5 / dx):int(1 / dx + 1)] = 2  

	# Make the interior laplacian operator
	# A first order, center difference, 2nd derivative
	d2_int = operator_1d.Operator1D([-1,0,1], 2)
	# The OperatorND object for a 2D laplacian
	laplac_int = operator_nd.OperatorND((d2_int, d2_int))

	# Make the exterior laplacian operators
	d2_left = operator_1d.Operator1D([0,1,2], 2)
	d2_right = operator_1d.Operator1D([-2,-1,0], 2)
	x_edge_ops = fixed_edge_ops.FixedEdgeOps( (d2_left,), (d2_right,) )
	y_edge_ops = fixed_edge_ops.FixedEdgeOps( (d2_left,), (d2_right,) )

	# Full laplacian operator
	laplacian = op_nd_scheme.OperatorNDScheme( laplac_int, (y_edge_ops, x_edge_ops) )

	gridspec = grid.CartesianGridSpec(coords)

	test_grid = grid.GridScalar(gridspec,u)

	lapl_op = gridoperator.GridOperator(gridspec,laplacian)

	out_grid = lapl_op(test_grid)

if __name__ == "__main__":
	main()
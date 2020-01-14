
from src import operator_1d
from src import operator_nd
from src import op_nd_scheme
from src import fixed_edge_ops

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

# Make the dictionary
ops_dict = {'laplacian': laplacian}

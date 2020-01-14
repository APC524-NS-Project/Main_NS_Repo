import numpy as np
from src import operator_1d
from src import operator_nd
from src import op_nd_scheme

# initialize desired parameters (that the user would specify)

t_start = 0.0 # start time
t_end = 10.0 # end time
dt = 0.01 # time step size

#sloppily define the solution grid and stuff
nx = 31
ny = 31
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

# Full laplacian operator
laplacian = op_nd_scheme.OperatorNDScheme(laplac_int,
                                           ( ((d2_left,),(d2_right,)),
                                             ((d2_left,),(d2_right,))
                                           )
                                         )

# Make the dictionary
ops_dict = {'laplacian': laplacian}

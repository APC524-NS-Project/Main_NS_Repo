import numpy as np
from src import grid
from src import static_bcs
from src import dirichlet_hand
from src import logger
from src import forward_euler
from src import conduct_heat_eqn
from src import spatial_driver
from src import driver
import initializer

gspec = grid.CartesianGridSpec(initializer.coords)
grid_u = grid.GridScalar(gspec,initializer.u)  # initial grid of temperature values

#set each of the boundaries (using all dirichlet zero for now)
BCs = []
BCs.append(static_bcs.Dirichlet(0,'l',np.zeros(grid_u.shape[0])))
BCs.append(static_bcs.Dirichlet(0,'r',np.zeros(grid_u.shape[0])))
BCs.append(static_bcs.Dirichlet(1,'l',np.zeros(grid_u.shape[0])))
BCs.append(static_bcs.Dirichlet(1,'r',np.zeros(grid_u.shape[0])))

bound_handlr = dirichlet_hand.DirichletHand(BCs)

data_logger = logger.Logger()

time_stpr = forward_euler.ForwardEuler()

prblm = conduct_heat_eqn.ConductHeatEqn(alpha=0.05)

prblm.set_ops(initializer.ops_dict)

space_drive = spatial_driver.SpatialDriver(bound_handlr,
                                           prblm,
                                           data_logger)

drive = driver.Driver(space_drive, time_stpr)

drive.full_solve(initializer.t_start, initializer.t_end, initializer.dt, grid_u)

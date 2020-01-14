
from src import static_bcs
from src import dirichlet_hand
from src import logger
from src import forward_euler
from src import conduct_heat_eqn
from src import spatial_driver
from src import driver
import initializer

t_start = 0.0 # start time
t_end = 10.0 # end time
dt = 0.01 # time step size

grid_T = None # initial grid of temperature values

#set each of the boundaries (using all dirichlet zero for now)
BCs = []
BCs.append(static_bcs.Dirichlet(0,'l',0))
BCs.append(static_bcs.Dirichlet(0,'r',0))
BCs.append(static_bcs.Dirichlet(1,'l',0))
BCs.append(static_bcs.Dirichlet(1,'r',0))
#set each of the boundaries (using all dirichlet zero for now)
BCs = []
BCs.append(static_bcs.Dirichlet(0,'l',None))
BCs.append(static_bcs.Dirichlet(0,'r',None))
BCs.append(static_bcs.Dirichlet(1,'l',None))
BCs.append(static_bcs.Dirichlet(1,'r',None))

bound_handlr = dirichlet_hand.DirichletHand(BCs)

data_logger = logger.Logger()

time_stpr = forward_euler.ForwardEuler()

prblm = conduct_heat_eqn.ConductHeatEqn(alpha=0.05)

prblm.set_ops(initializer.ops_dict)

space_drive = spatial_driver.SpatialDriver(bound_handlr,
                                           prblm,
                                           data_logger)

drive = driver.Driver(space_drive, time_stpr)

drive.full_solve(t_start, t_end, dt, grid_T)

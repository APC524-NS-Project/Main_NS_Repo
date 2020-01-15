from . import visualizer
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator

class PlotEnd(visualizer.Visualizer):
	def __init__(self,outloc):
		self.outloc = outloc

	def plot1d(self,log,name="",**kwargs):
		fext = "1d_end_"+name
		suffix = ".png"
		last_frame = log.get_frame(-1)

		initial_frame = log.get_frame(0)

		if last_frame[1].spec.ndim != 1:
			raise IndexError("Attempting to do a 1d plot of a multi dimensional grid")

		x = last_frame[1].spec.coords
		x = np.transpose(np.array(x))

		plt.figure()
		plt.subplot(211)
		plt.plot(x,initial_frame[1].grid,**kwargs)
		plt.subplot(212)
		plt.plot(x,last_frame[1].grid,**kwargs)
		plt.savefig(self.outloc+fext+suffix)
		plt.close(fig='all')


	def plot2d(self,log,name="",**kwargs):
		fext = "2d_end_"+name
		suffix = ".png"
		last_frame = log.get_frame(-1)

		initial_frame = log.get_frame(0)

		if last_frame[1].spec.ndim != 2:
			raise IndexError("Attempting to do a 2d plot of a multi dimensional grid")

		x,y=log.get_frame(0)[1].spec.coords #sets up coordinates for plot using GridSpec coordinate tuple
		xmesh,ymesh=np.meshgrid(x,y,indexing='ij')
		levels = MaxNLocator(nbins=15).tick_values(initial_frame[1].grid.min(), initial_frame[1].grid.max())

		cmap = plt.get_cmap('PiYG')
		norm = BoundaryNorm(levels, ncolors=cmap.N, clip=True)

		fig, (ax0, ax1) = plt.subplots(nrows=2)

		cf0 = ax0.contourf(x,y,initial_frame[1].grid, levels=levels,cmap=cmap,**kwargs)
		fig.colorbar(cf0, ax=ax0)
		ax1.set_title('Initial State')

		cf1 = ax1.contourf(x,y,last_frame[1].grid, levels=levels,cmap=cmap,**kwargs)
		fig.colorbar(cf1, ax=ax1)
		ax1.set_title('Final State')

		fig.tight_layout()

		plt.savefig(self.outloc+fext+suffix)
		plt.close(fig='all')


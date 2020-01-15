## @file plot_end
# Visualizer sub class for plotting the first and last frames of the solution to a 
# 1d and a 2d problem
# Uses pyplot.plot and pyplot.contourf respectively to generate the desired plots
from . import visualizer
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator

## PLotEnd
# Implementation of plot_end package as a class
class PlotEnd(visualizer.Visualizer):
	## Constructor
	#
	# @param outloc directory name for output to be saved to
	def __init__(self,outloc):
		self.outloc = outloc

	## plot1d
	# class to plot first and last frames of a 1d grid held in a logger
	#
	# plots a 1d contour of the first and last frames of the PDE solution and saves them to the outputs director
	# uses matplotlib to actually generate the plots
	# @param log a Logger() object
	# @param name a string containing the desired name of the file
	# @param **kwargs keyword arguments that will be passed to the plt.plot function
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

	## plot2d
	# class to plot first and last frames of a 2d grid held in a logger
	#
	# plots a 2d contour of the first and last frames of the PDE solution and saves them to the outputs director
	# uses matplotlib to actually generate the plots
	# @param log a Logger() object
	# @param name a string containing the desired name of the file
	# @param **kwargs keyword arguments that will be passed to the plt.contourf function
	def plot2d(self,log,name="",**kwargs):
		fext = "2d_end_"+name
		suffix = ".png"
		last_frame = log.get_frame(-1)

		initial_frame = log.get_frame(0)

		if last_frame[1].spec.ndim != 2:
			raise IndexError("Attempting to do a 2d plot of a multi dimensional grid")

		x,y=log.get_frame(0)[1].spec.coords #sets up coordinates for plot using GridSpec coordinate tuple
		xmesh,ymesh=np.meshgrid(x,y,indexing='ij')
		levels1 = MaxNLocator(nbins=15).tick_values(initial_frame[1].grid.min(), initial_frame[1].grid.max())
		levels2 = MaxNLocator(nbins=15).tick_values(last_frame[1].grid.min(), last_frame[1].grid.max())

		cmap = plt.get_cmap('PiYG')

		fig, (ax0, ax1) = plt.subplots(nrows=2)

		cf0 = ax0.contourf(x,y,initial_frame[1].grid, levels=levels1,cmap=cmap,**kwargs)
		fig.colorbar(cf0, ax=ax0)
		ax1.set_title('Initial State')

		cf1 = ax1.contourf(x,y,last_frame[1].grid, levels=levels2,cmap=cmap,**kwargs)
		fig.colorbar(cf1, ax=ax1)
		ax1.set_title('Final State')

		fig.tight_layout()

		plt.savefig(self.outloc+fext+suffix)
		plt.close(fig='all')


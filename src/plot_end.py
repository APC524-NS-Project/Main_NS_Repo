from . import visualizer
import numpy as np
import matplotlib.pyplot as plt

class PlotEnd(visualizer.Visualizer):
	def __init__(self,outloc):
		self.outloc = outloc

	def plot1d(self,log,name="",**kwargs):
		fext = "1d_end_"+name
		suffix = ".png"
		last_frame = log.get_frame(-1)

		if last_frame[1].spec.ndim != 1:
			raise IndexError("Attempting to do a 1d plot of a multi dimensional grid")

		x = last_frame[1].spec.coords
		x = np.array(x)

		plt.plot(x,last_frame[1].grid)
		plt.savefig(self.outloc+fext+suffix)
		plt.close(fig='all')



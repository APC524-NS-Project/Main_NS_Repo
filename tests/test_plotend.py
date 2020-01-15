import unittest
from src import plot_end
import mock
import numpy as np

class testPlotEnd(unittest.TestCase):
	def setUp(self):
		self.plot = plot_end.PlotEnd(r"tests/test_outs/")
		self.log1d = Logger('1d')
		self.log2d = Logger('2d')

	def test_plot1d(self):
		self.plot.plot1d(self.log1d,"test")

	def test_plot2d(self):
		self.plot.plot2d(self.log2d,"test")


class Logger():
	def __init__(self,gridtype):
		if gridtype == '1d':
			self.grid = Grid1D()
		elif gridtype == '2d':
			self.grid = Grid2D()

	def get_frame(self,i):
		return [0,self.grid]

class Grid1D():
	def __init__(self):
		self.spec = mock.Mock()
		self.spec.coords = (0,1,2,3,4,5)
		self.spec.ndim = 1
		self.grid = np.array([5,4,3,2,1,0])

class Grid2D():
	def __init__(self):
		self.spec = mock.Mock()
		self.spec.coords = ((0,1,2,3,4,5),(0,1,2,3,4,5))
		self.spec.ndim = 2
		self.grid = np.ones((6,6))
		self.grid[1:5,1:5] = 1
		self.grid[2:4,2:4] = 2
		self.grid[3,3] = 3